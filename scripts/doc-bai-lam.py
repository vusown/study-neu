#!/usr/bin/env python3
"""Chuyển văn bản trang review bài trắc nghiệm (copy từ elearning.neu.edu.vn) thành JSON cho nap-cau-hoi.py.

    python3 scripts/doc-bai-lam.py bai-lam.txt lan-lam.json --lan 5 [--ten "bài luyện tập tổng hợp"]

Văn bản dán có dạng: "Câu hỏi N … Đoạn văn câu hỏi <đề> Select one: a. <pa> b. <pa> … The correct answer is: <đáp án>".
- Câu "Không trả lời" thì không đánh ❌; câu đã trả lời mà có "Câu trả lời của bạn sai" thì "sai": true.
- "giai_thich" để "?" và "chu_de" để "": chạy nap-cau-hoi.py --dry-run để biết câu nào mới,
  rồi điền giải thích và chủ đề cho các câu mới trước khi nạp thật.
"""
import json
import re
import sys


def parse(text):
    out = []
    for blk in re.split(r"(?m)^Câu hỏi \d+\s*$", text)[1:]:
        m = re.search(r"Đoạn văn câu hỏi\s*\n(.*?)\nSelect one:\s*\n(.*?)\n(?:Phản hồi|The correct answer is:)", blk, re.S)
        if not m:
            raise SystemExit(f"Không đọc được câu:\n{blk[:300]}")
        de = "\n".join(l.strip() for l in m.group(1).strip().splitlines() if l.strip())
        parts = re.split(r"(?m)^\s*([a-h])\.\s*$", m.group(2))
        pa = [" ".join(p.split()) for p in parts[2::2]]
        dung_txt = " ".join(re.search(r"The correct answer is:\s*(.*?)\s*$", blk, re.S).group(1).split())
        idx = [i for i, p in enumerate(pa) if p == dung_txt]
        if len(idx) != 1:
            raise SystemExit(f"Không khớp đáp án '{dung_txt}' với phương án {pa}")
        answered = "Không trả lời" not in blk.split("Đoạn văn câu hỏi")[0]
        q = {"de": de, "pa": pa, "dung": "ABCDEFGH"[idx[0]], "giai_thich": "?", "chu_de": ""}
        if answered and "Câu trả lời của bạn sai" in blk:
            q["sai"] = True
        out.append(q)
    return out


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    lan = sys.argv[sys.argv.index("--lan") + 1] if "--lan" in sys.argv else "?"
    ten = f" ({sys.argv[sys.argv.index('--ten') + 1]})" if "--ten" in sys.argv else ""
    cau = parse(open(sys.argv[1], encoding="utf-8").read())
    data = {
        "tieu_de": f"Trắc nghiệm hệ thống — lần {lan}{ten}",
        "ghi_chu": "Đáp án theo phần \"The correct answer is\" của hệ thống. Chỉ ghi các câu mới.",
        "nguon": f"Hệ thống — lần {lan}",
        "cau": cau,
    }
    json.dump(data, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Đọc được {len(cau)} câu, {sum(q.get('sai', False) for q in cau)} câu làm sai.")


if __name__ == "__main__":
    main()
