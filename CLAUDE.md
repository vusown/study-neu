# CLAUDE.md

Repo cá nhân tổng hợp tài liệu, đề cương, ngân hàng câu hỏi và phương pháp ôn tập cho các môn học tại Đại học Kinh tế Quốc dân (NEU). Toàn bộ nội dung viết bằng **tiếng Việt**, định dạng Markdown.

## Quy ước

- Mỗi môn một thư mục trong `mon-hoc/`, tạo bằng cách copy `mon-hoc/_mau/`. Tên thư mục: chữ thường, không dấu, nối `-`, có mã học phần phía trước nếu biết.
- `README.md` ở gốc là mục lục: bảng link tới từng môn và file đề cương/câu hỏi của môn đó. Không đặt nội dung môn học ở gốc.
- Mỗi môn có 5 file (mẫu trong `mon-hoc/_mau/`): `README.md` (thông tin, điểm, tài liệu, kinh nghiệm, phương pháp ôn tập riêng của môn, kế hoạch), `de-cuong.md` (theo bài, có mức ⭐ và mục 🎯 "Đề hỏi gì"), `ngan-hang-cau-hoi.md` (đáp án hiện rõ để học thuộc, ghi nguồn từng câu), `ngan-hang-theo-chu-de.md` (cùng các câu, gom theo chủ đề), `cach-hoc-thuoc.md` (đề thi ra gì, khung trả lời, bảng thuộc lòng, bẫy hệ thống, cặp dễ nhầm, lịch học).
- File gốc (PDF, slide, đề thi scan…) copy vào `tai-lieu/` trong thư mục môn, đổi tên dạng không dấu `bai-N-ten-bai.pdf` (file chung như đề cương học phần đặt tiền tố `00-`), rồi liệt kê kèm link trong mục "Tài liệu" của `README.md` môn.
- `ngan-hang-cau-hoi.md` là **một file duy nhất** chứa câu hỏi để học thuộc, **chỉ gồm câu lấy từ hệ thống/đề thật** (không thêm câu tự soạn). Format: `**Câu N.** ... _(nguồn)_`, 4 dòng `- A.`…`- D.`, đáp án đúng in đậm kèm ✅ (`- **B. ...** ✅`), giải thích một dòng `> 💡 ...`. Trùng = cùng đề + cùng 4 phương án (bất kể thứ tự) thì không thêm. Đáp án hệ thống luôn thắng suy luận. Câu tự luận (Đúng/Sai có giải thích, tình huống) lấy nguyên văn từ đề thi mẫu, câu ôn tập bài giảng: đáp án viết dạng `> ✅ **Đúng/Sai/Gợi ý trả lời:**` kèm ý gạch đầu dòng, ghi rõ là đáp án gợi ý soạn theo bài giảng; phần nào không có trong bài giảng thì đánh dấu ⚠️.
- `ngan-hang-theo-chu-de.md` chứa cùng các câu đó nhưng gom theo chủ đề (mỗi chủ đề có dòng `> 🔑 **Ghi nhớ:**`, mỗi câu ghi `_(câu N)_` trỏ về số câu gốc). Thêm hoặc sửa câu trong `ngan-hang-cau-hoi.md` thì cập nhật cả file theo chủ đề, mục 🎯 "Đề hỏi gì" trong `de-cuong.md` nếu có ý mới.
- `ban-do-notebooklm.md` (bản đồ tra cứu cho NotebookLM) **tạo tự động** bằng `python3 scripts/tao-ban-do-notebooklm.py`, không sửa tay. Chạy lại script mỗi khi sửa ngân hàng câu hỏi, đề cương, cách học thuộc hoặc README môn.
- Khi thêm môn, thêm một dòng vào bảng "Danh sách môn học" trong `README.md` gốc.
- Phương pháp ôn tập nằm trong từng môn, không có thư mục phương pháp chung.
- Không bịa thông tin cụ thể về môn (giảng viên, mã học phần, trọng số điểm, đề thi). Nếu chưa có nguồn thì để trống hoặc đánh dấu "cần xác minh". Không tự soạn câu hỏi vào ngân hàng.
