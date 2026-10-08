#!/usr/bin/env python3
"""Tạo ban-do-notebooklm.md cho từng môn trong mon-hoc/ (bỏ qua _mau).

Chạy lại sau mỗi lần sửa ngân hàng câu hỏi, đề cương hoặc cách học thuộc:
    python3 scripts/tao-ban-do-notebooklm.py            # tất cả các môn
    python3 scripts/tao-ban-do-notebooklm.py txqtkd116  # chỉ môn có tên thư mục chứa chuỗi này
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "mon-hoc"
OUT = "ban-do-notebooklm.md"
STOP = {"sai", "đúng", "không", "tất cả", "có", "chưa"}


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


def info_rows(readme):
    """Lấy vài dòng thông tin chung từ bảng đầu README."""
    rows = {}
    for key in ("Mã học phần", "Học kỳ", "Hình thức thi cuối kỳ"):
        m = re.search(rf"(?m)^\| {re.escape(key)} \| (.*?) \|\s*$", readme)
        if m:
            rows[key] = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", m.group(1))
    return rows


def lead_quote(text):
    """Khối trích dẫn (>) và bảng ngay sau tiêu đề # của file."""
    out, started = [], False
    for line in text.splitlines()[1:]:
        if line.startswith(">") or (started and line.startswith("|")):
            out.append(line)
            started = True
        elif not line.strip():
            if started:
                out.append("")
        elif started:
            break
    return "\n".join(out).strip()


def describe_material(name, readme):
    """Mô tả file trong tai-lieu/ dựa vào dòng README có link tới file."""
    line = next((l for l in readme.splitlines() if f"tai-lieu/{name})" in l), "")
    m = re.search(rf"\[([^\]]+)\]\(tai-lieu/{re.escape(name)}\)", line)
    text = m.group(1) if m else ""
    if not text or text.lower() in ("pdf", "docx", "slide"):
        cell = re.match(r"\|\s*([^|]+?)\s*\|", line)
        text = f"Bài {cell.group(1)}" if cell else name
        if "-slide" in name:
            text += " — slide"
        if re.search(rf"tai-lieu/{re.escape(name)}\)\s*\(scan\)", line):
            text += " (scan)"
    return text


def bank_sections(bank):
    """Các mục ## của ngân hàng gốc và khoảng số câu trong mỗi mục."""
    out = []
    for part in re.split(r"(?m)^(?=## )", bank)[1:]:
        title = part.splitlines()[0][3:].strip()
        nums = [int(x) for x in re.findall(r"(?m)^\*\*Câu (\d+)\.\*\*", part)]
        if nums:
            out.append((title, min(nums), max(nums), len(nums)))
    return out


def keywords(ghi_nho, limit=12):
    seen, out = set(), []
    for k in re.findall(r"\*\*(.+?)\*\*", ghi_nho):
        k = k.strip(" .:;,")
        if len(k) < 3 or len(k) > 60 or k.lower() in seen or k.lower() in STOP:
            continue
        seen.add(k.lower())
        out.append(k)
        if len(out) == limit:
            break
    return " · ".join(out)


def ranges(nums):
    nums = sorted(nums)
    out, start, prev = [], None, None
    for n in nums:
        if start is None:
            start = prev = n
        elif n == prev + 1:
            prev = n
        else:
            out.append(f"{start}–{prev}" if prev > start else str(start))
            start = prev = n
    if start is not None:
        out.append(f"{start}–{prev}" if prev > start else str(start))
    return ", ".join(out)


def topic_map(topic):
    """[(bài, [(mã, tên, số câu, [câu gốc], ⚡ [câu gốc], từ khóa)])]"""
    lessons = []
    for part in re.split(r"(?m)^(?=## )", topic)[1:]:
        title = part.splitlines()[0][3:].strip()
        if title.startswith("Mục lục"):
            continue
        items = []
        for sec in re.split(r"(?m)^(?=### )", part)[1:]:
            h = re.match(r"### (\S+)\s+(.*?)\s*\((\d+) câu\)", sec)
            if not h:
                continue
            blocks = re.split(r"(?m)^(?=\*\*Câu \d+\.\*\* _\(câu)", sec)[1:]
            refs, traps = [], []
            for b in blocks:
                n = int(re.match(r"\*\*Câu \d+\.\*\* _\(câu (\d+)\)_", b).group(1))
                refs.append(n)
                if "⚡" in b:
                    traps.append(n)
            g = re.search(r"(?m)^> 🔑 \*\*Ghi nhớ:\*\*(.*)$", sec)
            items.append((h.group(1).rstrip("."), h.group(2), int(h.group(3)),
                          refs, traps, keywords(g.group(1)) if g else ""))
        if items:
            lessons.append((title, items))
    return lessons


def headings(text, levels=("## ",)):
    return [l for l in text.splitlines() if l.startswith(levels)]


def build(d):
    readme = read(d / "README.md")
    bank = read(d / "ngan-hang-cau-hoi.md")
    topic = read(d / "ngan-hang-theo-chu-de.md")
    outline = read(d / "de-cuong.md")
    guide = read(d / "cach-hoc-thuoc.md")
    name = readme.splitlines()[0].lstrip("# ").strip() if readme else d.name
    total = len(re.findall(r"(?m)^\*\*Câu \d+\.\*\*", bank))
    info = info_rows(readme)

    L = [f"# Bản đồ tra cứu cho NotebookLM — {name}", ""]
    L += [
        "> File này giúp NotebookLM (và người đọc) **biết câu hỏi, kiến thức nằm ở file nào, mục nào**.",
        "> Tạo tự động bằng `scripts/tao-ban-do-notebooklm.py`, đừng sửa tay. Sửa ngân hàng hoặc đề cương xong thì chạy lại script.",
        ">",
        "> **Hướng dẫn cho NotebookLM khi trả lời:**",
        "> - Luôn dẫn **số câu gốc** (\"câu N\" trong `ngan-hang-cau-hoi.md`) và tên file nguồn.",
        "> - Đáp án trắc nghiệm lấy đúng phương án có ✅. Không tự suy luận đáp án khác, kể cả khi bài giảng nói khác (xem các câu ⚡).",
        "> - Câu tự luận chỉ có **đáp án gợi ý**; phần đánh ⚠️ là phần không có trong bài giảng.",
        "",
    ]
    if info:
        L += ["## Thông tin môn", "", "| | |", "|---|---|"]
        L += [f"| {k} | {v} |" for k, v in info.items()]
        L += [f"| Tổng số câu trong ngân hàng | **{total}** |", ""]

    # 1. Nguồn
    L += ["## 1. Nguồn tải lên NotebookLM", "",
          "Tạo **một notebook cho mỗi môn**, tải lên các file sau.", "",
          "| File | Nội dung | Dùng khi hỏi |", "|---|---|---|",
          f"| `{OUT}` | Bản đồ này | Câu hỏi nằm ở đâu, chủ đề nào có câu nào |",
          f"| `ngan-hang-theo-chu-de.md` | {total} câu gom theo bài, chủ đề, mỗi chủ đề có dòng 🔑 Ghi nhớ | Học thuộc, ôn theo chủ đề, tạo quiz |",
          f"| `ngan-hang-cau-hoi.md` | Cùng {total} câu, xếp theo nguồn (đề thi, lần làm hệ thống) | Tra số câu gốc, nguồn của câu |",
          "| `de-cuong.md` | Tóm tắt kiến thức theo bài, mức ⭐, mục 🎯 Đề hỏi gì | Giải thích kiến thức, vì sao đáp án đúng |",
          "| `cach-hoc-thuoc.md` | Đề ra gì, bảng thuộc lòng, bẫy, cặp dễ nhầm, lịch học | Mẹo nhớ, bẫy đề, kế hoạch ôn |",
          "| `README.md` | Thông tin môn, cách tính điểm, lịch học | Điểm, điều kiện thi, hình thức thi |"]
    tl = d / "tai-lieu"
    if tl.is_dir():
        for f in sorted(tl.iterdir()):
            note = "Tài liệu gốc"
            if f.suffix.lower() == ".docx":
                note += ". Nếu NotebookLM không nhận .docx thì mở bằng Google Docs rồi thêm từ Drive"
            desc = describe_material(f.name, readme)
            if "scan" in desc.lower():
                note += ". Bản scan, NotebookLM có thể đọc sót chữ"
            L.append(f"| `tai-lieu/{f.name}` | {desc} | {note} |")
    L.append("")

    # 2. Quy ước
    L += ["## 2. Quy ước đọc", "",
          "- **Số câu:** trong `ngan-hang-cau-hoi.md`, \"**Câu N.**\" là **số câu gốc**. "
          "Trong `ngan-hang-theo-chu-de.md`, \"**Câu k.** _(câu N)_\" thì k chỉ là số thứ tự trong file chủ đề, **N mới là số câu gốc**.",
          "- **Mã chủ đề** dạng `2.3` = Bài 2, chủ đề 3 trong `ngan-hang-theo-chu-de.md`.",
          "- **Nguồn câu** ghi cuối đề, ví dụ _(Hệ thống — lần 3)_, _(Đề mẫu 2)_, _(Ôn tập Bài 1)_.", "",
          "| Ký hiệu | Nghĩa |", "|---|---|",
          "| ✅ | Đáp án đúng (trắc nghiệm: đáp án hệ thống/đề thi; tự luận: đáp án gợi ý) |",
          "| ⚡ | Câu có bẫy, hoặc hệ thống chấm khác bài giảng |",
          "| ❌ | Câu từng làm sai |",
          "| ⚠️ | Nội dung không có trong bài giảng, cần xác minh |",
          "| 🔑 | Dòng Ghi nhớ đầu mỗi chủ đề |",
          "| 💡 | Giải thích đáp án |",
          "| 🎯 | Mục \"Đề hỏi gì\" trong đề cương |",
          "| ⭐⭐⭐ / ⭐⭐ / ⭐ | Chắc chắn ra / hay ra / ít ra |", ""]
    lq = lead_quote(outline)
    if lq:
        L += ["**Lưu ý về nguồn và cách đánh số bài** (chép từ đầu `de-cuong.md`):", "", lq, ""]

    # 3. Các phần của ngân hàng gốc
    secs = bank_sections(bank)
    if secs:
        L += ["## 3. Các phần của `ngan-hang-cau-hoi.md`", "",
              "| Phần | Câu gốc | Số câu |", "|---|---|---|"]
        L += [f"| {t} | {a}–{b} | {n} |" for t, a, b, n in secs]
        L.append("")

    # 4. Bản đồ chủ đề
    lessons = topic_map(topic)
    if lessons:
        L += ["## 4. Bản đồ chủ đề", "",
              "Mỗi dòng là một chủ đề trong `ngan-hang-theo-chu-de.md`. Cột **Câu gốc** dùng để tìm câu trong `ngan-hang-cau-hoi.md`; "
              "tìm một số câu trong cột này để biết câu đó thuộc chủ đề nào.", ""]
        for title, items in lessons:
            n = sum(i[2] for i in items)
            L += [f"### {title} ({n} câu)", "",
                  "| Mã | Chủ đề | Số câu | Câu gốc | Câu ⚡ | Từ khóa |", "|---|---|---|---|---|---|"]
            for code, tname, cnt, refs, traps, kw in items:
                L.append(f"| {code} | {tname} | {cnt} | {ranges(refs)} | {ranges(traps) or '—'} | {kw} |")
            L.append("")

    # 5. Mục lục đề cương và cách học thuộc
    for fname, text, label in (("de-cuong.md", outline, "Đề cương"), ("cach-hoc-thuoc.md", guide, "Cách học thuộc")):
        hs = [h for h in headings(text, ("## ", "### ")) if "Mục lục" not in h]
        if hs:
            L += [f"## {'5' if fname == 'de-cuong.md' else '6'}. Mục lục `{fname}` ({label})", ""]
            for h in hs:
                L.append(("- " if h.startswith("## ") else "  - ") + h.lstrip("# ").strip())
            L.append("")

    # 7. Câu hỏi mẫu
    ex_code = lessons[0][1][0][0] if lessons else "1.1"
    traps = [n for _, items in lessons for i in items for n in i[4]]
    ex_num = max(traps) if traps else (lessons[0][1][0][3][0] if lessons and lessons[0][1][0][3] else 1)
    L += ["## 7. Câu hỏi mẫu nên hỏi NotebookLM", "",
          f"- \"Câu {ex_num} đáp án là gì, vì sao là bẫy? Giải thích theo đề cương.\"",
          f"- \"Tạo quiz 10 câu từ chủ đề {ex_code}, chỉ dùng câu có sẵn trong ngân hàng, giữ nguyên đáp án ✅.\"",
          "- \"Liệt kê tất cả câu ⚡ của Bài 2 kèm đáp án và lý do là bẫy.\"",
          "- \"Đọc dòng 🔑 Ghi nhớ của mọi chủ đề Bài 1 rồi tóm tắt thành 10 ý.\"",
          "- \"Những cặp khái niệm nào dễ nhầm? Lấy từ cach-hoc-thuoc.md.\"",
          "- \"Tạo Audio Overview ôn Bài 3, nhấn mạnh các câu ⚡.\"", ""]
    return "\n".join(L)


def main():
    flt = sys.argv[1] if len(sys.argv) > 1 else ""
    for d in sorted(ROOT.iterdir()):
        if not d.is_dir() or d.name.startswith("_") or flt not in d.name:
            continue
        (d / OUT).write_text(build(d), encoding="utf-8")
        print("ghi", d / OUT)


if __name__ == "__main__":
    main()
