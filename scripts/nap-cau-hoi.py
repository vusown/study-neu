#!/usr/bin/env python3
"""Nạp một lần làm trắc nghiệm hệ thống vào ngân hàng câu hỏi của một môn.

    python3 scripts/nap-cau-hoi.py mon-hoc/<mon> lan-lam.json            # nạp
    python3 scripts/nap-cau-hoi.py mon-hoc/<mon> lan-lam.json --dry-run  # chỉ báo câu mới/trùng

lan-lam.json:
{
  "tieu_de": "Trắc nghiệm hệ thống — lần 1 (...)",   # tiêu đề mục ## nối vào ngan-hang-cau-hoi.md
  "ghi_chu": "Chỉ ghi các câu mới.",                  # dòng > dưới tiêu đề
  "nguon": "Hệ thống — lần 1",                        # ghi cuối đề mỗi câu
  "cau": [{"de": "...", "pa": ["...", "..."], "dung": "B", "giai_thich": "...", "chu_de": "1.2", "sai": false}]
}

- Trùng = cùng đề và cùng tập phương án (bất kể thứ tự), so sau khi bỏ dấu câu, **, ✅, ⚡, ❌ và nguồn _(...)_.
- Có thể tạo file JSON từ văn bản trang review bằng scripts/doc-bai-lam.py.
- Câu mới được đánh số tiếp theo, nối vào cuối ngan-hang-cau-hoi.md và chèn vào cuối chủ đề "chu_de"
  trong ngan-hang-theo-chu-de.md (chủ đề phải có sẵn). Số câu ở tiêu đề chủ đề, mục lục và dòng
  "Gồm đúng N câu" được cập nhật. "sai": true thêm ❌ sau đề.
- Dòng 🔑 Ghi nhớ, README, cach-hoc-thuoc.md sửa tay; sau đó chạy lại scripts/tao-ban-do-notebooklm.py.
"""
import json
import re
import sys
from pathlib import Path

OPT = re.compile(r"^- (\*\*)?([A-H])\.\s*")


def norm(t):
    t = re.sub(r"_\(.*?\)_|❌|\*\*|✅|⚡|[“”\"'.,:?;!…]", "", t)
    return " ".join(t.split()).lower()


def existing_keys(bank):
    keys = {}
    for b in re.split(r"(?m)^(?=\*\*Câu \d+\.\*\*)", bank):
        # Đề có thể nhiều dòng (bảng số liệu): lấy hết phần trước phương án đầu tiên.
        m = re.match(r"\*\*Câu (\d+)\.\*\*(.*?)(?=\n- (?:\*\*)?[A-H]\.|\Z)", b, re.S)
        if not m:
            continue
        opts = [OPT.sub("", l) for l in b.splitlines() if OPT.match(l)]
        if len(opts) >= 2:
            keys[(norm(m.group(2)), tuple(sorted(norm(o) for o in opts)))] = int(m.group(1))
    return keys


def block(n, q, src):
    mark = " ❌" if q.get("sai") else ""
    opts = "\n".join(
        f"- **{L}. {o}** ✅" if L == q["dung"] else f"- {L}. {o}"
        for L, o in zip("ABCDEFGH", q["pa"])
    )
    return f"**Câu {n}.** {q['de']}{mark} _({src})_\n\n{opts}\n\n> 💡 ✅ Đáp án hệ thống. {q['giai_thich']}"


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    d, data = Path(sys.argv[1]), json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    dry = "--dry-run" in sys.argv
    f_bank, f_topic = d / "ngan-hang-cau-hoi.md", d / "ngan-hang-theo-chu-de.md"
    bank, topic = f_bank.read_text(encoding="utf-8"), f_topic.read_text(encoding="utf-8")

    seen = existing_keys(bank)
    n = max(int(x) for x in re.findall(r"(?m)^\*\*Câu (\d+)\.\*\*", bank))
    new, dup = [], []
    for i, q in enumerate(data["cau"], 1):
        assert q["dung"] in "ABCDEFGH"[: len(q["pa"])], f"câu {i}: đáp án ngoài phương án"
        k = (norm(q["de"]), tuple(sorted(norm(o) for o in q["pa"])))
        if k in seen:
            dup.append((i, seen[k]))
            continue
        if not dry:
            assert q["giai_thich"] != "?", f"câu {i}: chưa có giải thích"
            assert re.search(rf"(?m)^### {re.escape(q['chu_de'])}\. ", topic), f"câu {i}: không có chủ đề {q['chu_de']}"
        n += 1
        seen[k] = n
        new.append((i, n, q))

    print(f"Mới: {len(new)} câu → " + ", ".join(f"{i}→câu {m} ({q['chu_de']})" for i, m, q in new))
    print(f"Trùng: {len(dup)} câu → " + ", ".join(f"{i}=câu {m}" for i, m in dup))
    if dry or not new:
        return

    src = data["nguon"]
    sec = "\n\n".join(block(m, q, src) for _, m, q in new)
    bank = bank.rstrip("\n") + f"\n\n## {data['tieu_de']}\n\n> {data['ghi_chu']}\n\n{sec}\n"

    lines = topic.split("\n")
    for _, m, q in new:
        h = next(j for j, l in enumerate(lines) if l.startswith(f"### {q['chu_de']}. "))
        end = next((j for j in range(h + 1, len(lines)) if re.match(r"(##|---)", lines[j])), len(lines))
        while lines[end - 1].strip() == "":
            end -= 1
        cnt = int(re.search(r"\((\d+) câu\)$", lines[h]).group(1)) + 1
        lines[h] = re.sub(r"\(\d+ câu\)$", f"({cnt} câu)", lines[h])
        b = re.sub(r"^\*\*Câu \d+\.\*\*", f"**Câu {cnt}.** _(câu {m})_", block(m, q, src))
        lines[end:end] = [""] + b.split("\n")
    topic = "\n".join(lines)

    # Cập nhật số câu từng bài trong mục lục và tổng số câu.
    for sec_m in re.finditer(r"(?m)^## (Bài \S+ — .*)$", topic):
        title = sec_m.group(1)
        rest = topic[sec_m.end():]
        nxt = re.search(r"(?m)^## ", rest)
        c = len(re.findall(r"_\(câu \d+\)_", rest[: nxt.start()] if nxt else rest))
        topic = re.sub(rf"(?m)^(- \[{re.escape(title)}\]\(.*?\) — )\d+ câu$", rf"\g<1>{c} câu", topic)
    topic = re.sub(r"Gồm đúng \d+ câu", f"Gồm đúng {n} câu", topic)

    f_bank.write_text(bank, encoding="utf-8")
    f_topic.write_text(topic, encoding="utf-8")
    print(f"Đã ghi. Ngân hàng có {n} câu.")


if __name__ == "__main__":
    main()
