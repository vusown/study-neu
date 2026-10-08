# 📚 Study NEU — Mục lục

Tổng hợp tài liệu, đề cương, ngân hàng câu hỏi và phương pháp ôn tập cho từng môn học tại **Đại học Kinh tế Quốc dân (NEU)**.

## Danh sách môn học

| Môn | Học kỳ | Tín chỉ | Trạng thái | Đề cương | Câu hỏi | Điểm |
|-----|--------|---------|------------|----------|---------|------|
| [Phát triển kỹ năng cá nhân](mon-hoc/txpsd01-phat-trien-ky-nang-ca-nhan/README.md) (TXPSD01) | 05/07 | 3 | 🟡 | [📄](mon-hoc/txpsd01-phat-trien-ky-nang-ca-nhan/de-cuong.md) | [❓](mon-hoc/txpsd01-phat-trien-ky-nang-ca-nhan/ngan-hang-theo-chu-de.md) | |
| [Nhập môn Internet và E-learning](mon-hoc/txict01-nhap-mon-internet-va-elearning/README.md) (TXICT01) | 05/07 | 3 | 🟡 | [📄](mon-hoc/txict01-nhap-mon-internet-va-elearning/de-cuong.md) | [❓](mon-hoc/txict01-nhap-mon-internet-va-elearning/ngan-hang-theo-chu-de.md) | |
| [Kỹ năng quản trị](mon-hoc/txqtkd116-ky-nang-quan-tri/README.md) (TXQTKD116) | 06/09 | 3 | 🟡 | [📄](mon-hoc/txqtkd116-ky-nang-quan-tri/de-cuong.md) | [❓](mon-hoc/txqtkd116-ky-nang-quan-tri/ngan-hang-theo-chu-de.md) | |

Học kỳ: ghi theo **mã học kỳ** của trường (VD `05/07`). Một năm có 4 học kỳ, không theo chu kỳ cố định.
Trạng thái: 🟢 đã xong · 🟡 đang học · ⚪ chưa học

<!--
Mẫu một dòng:
| [Kinh tế vi mô 1](mon-hoc/kinh-te-vi-mo-1/README.md) | 05/07 | 3 | 🟡 | [📄](mon-hoc/kinh-te-vi-mo-1/de-cuong.md) | [❓](mon-hoc/kinh-te-vi-mo-1/ngan-hang-cau-hoi.md) | |
-->

## Tra cứu bằng NotebookLM

Mỗi môn có file `ban-do-notebooklm.md`: bản đồ cho biết câu hỏi, kiến thức nằm ở file nào, mục nào. Tạo **một notebook cho mỗi môn**, tải lên các file `.md` của môn (kèm tài liệu gốc trong `tai-lieu/` nếu cần).

Sau khi sửa ngân hàng câu hỏi hoặc đề cương, tạo lại bản đồ:

```bash
python3 scripts/tao-ban-do-notebooklm.py
```

## Thêm môn mới

```bash
cp -r mon-hoc/_mau mon-hoc/<ten-mon>
```

Tên thư mục viết chữ thường, không dấu, nối bằng `-`, có mã học phần phía trước nếu biết. Ví dụ: `kthn1101-kinh-te-vi-mo-1`. Copy tài liệu gốc (PDF, slide…) vào `mon-hoc/<ten-mon>/tai-lieu/`, rồi thêm một dòng vào bảng trên.
