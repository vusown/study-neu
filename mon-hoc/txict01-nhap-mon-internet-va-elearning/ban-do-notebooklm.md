# Bản đồ tra cứu cho NotebookLM — Nhập môn Internet và E-learning (Introduction to Internet and E-learning)

> File này giúp NotebookLM (và người đọc) **biết câu hỏi, kiến thức nằm ở file nào, mục nào**.
> Tạo tự động bằng `scripts/tao-ban-do-notebooklm.py`, đừng sửa tay. Sửa ngân hàng hoặc đề cương xong thì chạy lại script.
>
> **Hướng dẫn cho NotebookLM khi trả lời:**
> - Luôn dẫn **số câu gốc** ("câu N" trong `ngan-hang-cau-hoi.md`) và tên file nguồn.
> - Đáp án trắc nghiệm lấy đúng phương án có ✅. Không tự suy luận đáp án khác, kể cả khi bài giảng nói khác (xem các câu ⚡).
> - Câu tự luận chỉ có **đáp án gợi ý**; phần đánh ⚠️ là phần không có trong bài giảng.

## Thông tin môn

| | |
|---|---|
| Mã học phần | TXICT01 (bài giảng cũ ghi ICT101) |
| Học kỳ | 05/07 |
| Hình thức thi cuối kỳ | Trắc nghiệm khách quan trên giấy, **50 câu / 60 phút**, 0,20 điểm/câu, không dùng tài liệu |
| Tổng số câu trong ngân hàng | **215** |

## 1. Nguồn tải lên NotebookLM

Tạo **một notebook cho mỗi môn**, tải lên các file sau.

| File | Nội dung | Dùng khi hỏi |
|---|---|---|
| `ban-do-notebooklm.md` | Bản đồ này | Câu hỏi nằm ở đâu, chủ đề nào có câu nào |
| `ngan-hang-theo-chu-de.md` | 215 câu gom theo bài, chủ đề, mỗi chủ đề có dòng 🔑 Ghi nhớ | Học thuộc, ôn theo chủ đề, tạo quiz |
| `ngan-hang-cau-hoi.md` | Cùng 215 câu, xếp theo nguồn (đề thi, lần làm hệ thống) | Tra số câu gốc, nguồn của câu |
| `de-cuong.md` | Tóm tắt kiến thức theo bài, mức ⭐, mục 🎯 Đề hỏi gì | Giải thích kiến thức, vì sao đáp án đúng |
| `cach-hoc-thuoc.md` | Đề ra gì, bảng thuộc lòng, bẫy, cặp dễ nhầm, lịch học | Mẹo nhớ, bẫy đề, kế hoạch ôn |
| `README.md` | Thông tin môn, cách tính điểm, lịch học | Điểm, điều kiện thi, hình thức thi |
| `tai-lieu/00-de-cuong-chi-tiet-hoc-phan.pdf` | Đề cương chi tiết học phần (scan, 2025) | Tài liệu gốc. Bản scan, NotebookLM có thể đọc sót chữ |
| `tai-lieu/00-de-thi-thu.pdf` | Đề thi thử ICT101, mã đề 1, có đáp án | Tài liệu gốc |
| `tai-lieu/00-huong-dan-su-dung-neu-elearning.pdf` | Hướng dẫn sử dụng NEU E-learning (09/2018) | Tài liệu gốc |
| `tai-lieu/bai-1-nhung-khai-niem-co-ban.pdf` | Bài 1 — Những khái niệm cơ bản (2018) | Tài liệu gốc |
| `tai-lieu/bai-2-kien-truc-mang-internet.pdf` | Bài 2 — Kiến trúc mạng Internet (2018) | Tài liệu gốc |
| `tai-lieu/bai-3-huong-dan-su-dung-dich-vu-internet.pdf` | Bài 3 — Hướng dẫn sử dụng một số dịch vụ Internet thông dụng | Tài liệu gốc |
| `tai-lieu/bai-4-mo-hinh-he-thong-elearning.pdf` | Bài 4 — Mô hình hệ thống E-learning | Tài liệu gốc |

## 2. Quy ước đọc

- **Số câu:** trong `ngan-hang-cau-hoi.md`, "**Câu N.**" là **số câu gốc**. Trong `ngan-hang-theo-chu-de.md`, "**Câu k.** _(câu N)_" thì k chỉ là số thứ tự trong file chủ đề, **N mới là số câu gốc**.
- **Mã chủ đề** dạng `2.3` = Bài 2, chủ đề 3 trong `ngan-hang-theo-chu-de.md`.
- **Nguồn câu** ghi cuối đề, ví dụ _(Hệ thống — lần 3)_, _(Đề mẫu 2)_, _(Ôn tập Bài 1)_.

| Ký hiệu | Nghĩa |
|---|---|
| ✅ | Đáp án đúng (trắc nghiệm: đáp án hệ thống/đề thi; tự luận: đáp án gợi ý) |
| ⚡ | Câu có bẫy, hoặc hệ thống chấm khác bài giảng |
| ❌ | Câu từng làm sai |
| ⚠️ | Nội dung không có trong bài giảng, cần xác minh |
| 🔑 | Dòng Ghi nhớ đầu mỗi chủ đề |
| 💡 | Giải thích đáp án |
| 🎯 | Mục "Đề hỏi gì" trong đề cương |
| ⭐⭐⭐ / ⭐⭐ / ⭐ | Chắc chắn ra / hay ra / ít ra |

**Lưu ý về nguồn và cách đánh số bài** (chép từ đầu `de-cuong.md`):

> Tóm tắt từ slide trong [`tai-lieu/`](tai-lieu/). Slide là **bản cũ ICT101 (2018)**, chia bài khác đề cương 2025. Bảng dưới cho biết bài cũ ứng với bài mới nào.

| Bài trong đề cương 2025 (đề thi theo cách chia này) | Số câu thi | Đọc phần nào bên dưới |
|------|:---:|------|
| Bài 1 — Tổng quan về Internet | 10 | Bài 1 slide (lịch sử Internet, nhà cung cấp) + Bài 2 slide mục 2.1 (phương thức kết nối) |
| Bài 2 — Các dịch vụ Internet thông dụng | 10 | Bài 2 slide (TCP/IP, IP, tên miền, WWW, email, FTP, chat) |
| Bài 3 — Giới thiệu về giáo dục điện tử | 9 | Bài 1 slide (phần E-learning) + Bài 4 slide (khái niệm, đặc điểm, Sloan) |
| Bài 4 — Phương pháp và quy trình học E-learning | 9 | Bài 4 slide (mô hình, chuẩn, quy trình) + **phần 🎯 bên dưới** (slide thiếu) |
| Bài 5 — Hướng dẫn công cụ E-learning & NeuElearning | 12 | Bài 3 slide (trình duyệt, Google, tải tệp, email, chat) + Phụ lục hướng dẫn NEU E-learning |

## 3. Các phần của `ngan-hang-cau-hoi.md`

| Phần | Câu gốc | Số câu |
|---|---|---|
| Đề thi thử ICT101 — Mã đề 1 (50 câu, 60 phút) | 1–50 | 50 |
| Bài luyện tập trên hệ thống — lần 1 (40 câu) | 51–87 | 37 |
| Bài luyện tập trên hệ thống — lần 2 (40 câu) | 88–125 | 38 |
| Bài luyện tập trên hệ thống — lần 3 (40 câu) | 126–155 | 30 |
| Bài luyện tập trên hệ thống — lần 4 (40 câu) | 156–182 | 27 |
| Bài luyện tập trên hệ thống — lần 5 (40 câu) | 183–192 | 10 |
| Bài luyện tập trên hệ thống — lần 6 (40 câu) | 193–202 | 10 |
| Bài luyện tập trên hệ thống — lần 7 (40 câu) | 203–212 | 10 |
| Bài luyện tập trên hệ thống — lần 8 (câu 11–20 của đề; câu 1–10 và 21–40 trùng hết) | 213–215 | 3 |

## 4. Bản đồ chủ đề

Mỗi dòng là một chủ đề trong `ngan-hang-theo-chu-de.md`. Cột **Câu gốc** dùng để tìm câu trong `ngan-hang-cau-hoi.md`; tìm một số câu trong cột này để biết câu đó thuộc chủ đề nào.

### Bài 1 — Tổng quan về Internet (28 câu)

| Mã | Chủ đề | Số câu | Câu gốc | Câu ⚡ | Từ khóa |
|---|---|---|---|---|---|
| 1.1 | Khái niệm và lịch sử Internet | 6 | 4, 51, 53–54, 57, 94 | — | Inter-network · TCP/IP = Transmission Control Protocol / Internet Protocol · Bộ Quốc phòng Mỹ · 1969 · 1974 · 19/11/1997 |
| 1.2 | Nhà cung cấp dịch vụ Internet | 5 | 52, 56, 59, 89, 93 | — | ISP · IAP · IXP, Internet Exchange Provider · làm được việc của ISP, ngược lại thì không · ICP = Internet Content Provider · nội dung thông tin · OSP = Online Service Provider |
| 1.3 | Phương thức kết nối | 16 | 6, 60, 63, 96–97, 99–100, 104, 126–127, 161, 165, 183, 187, 190, 209 | — | không thường trực · chậm nhất · Băng rộng · Leased-Line · HDSL · bất đối xứng · VDSL · đều cao · Asymmetrical · modem ADSL chuyên dụng · Wireless Fidelity · không dây |
| 1.4 | Dịch vụ cơ bản và tổng hợp | 1 | 34 | — | cơ bản · tổng hợp |

### Bài 2 — Các dịch vụ Internet thông dụng (78 câu)

| Mã | Chủ đề | Số câu | Câu gốc | Câu ⚡ | Từ khóa |
|---|---|---|---|---|---|
| 2.1 | Giao thức và kiến trúc mạng | 17 | 61–62, 65, 101, 130, 135, 156, 159–160, 163–164, 186, 189, 196, 199, 211, 215 | 101 | Address Resolution Protocol · RARP = Reverse ARP · HTML không phải · Local Area Network · Metropolitan Area Network · Wide Area Network · TCP/IP · FTP = File Transfer Protocol · TFTP = Trivial FTP · SMTP = Simple Mail Transfer Protocol · Telnet · NFS |
| 2.2 | Địa chỉ IP, IPv6 | 22 | 19, 21, 48, 66, 105, 133–134, 158, 184–185, 191–194, 202–204, 207–208, 210, 212, 214 | — | địa chỉ IP · 2 phiên bản · 32 bit · 4 octet · A.B.C.D · 0–255 · quảng bá · được · 128 bit · 8 cụm · dấu hai chấm · 2^96 |
| 2.3 | Tên miền | 14 | 39, 43, 69, 102, 128, 131–132, 157, 162, 188, 195, 200–201, 213 | — | Domain Name System · tên miền · dễ nhớ hơn · dấu chấm · IP hoặc tên miền · 255 · edu cấp 2 · neu cấp 3 |
| 2.4 | Dịch vụ Web | 10 | 37, 47, 67–68, 71, 73, 98, 171, 205–206 | — | HTTP = HyperText Transfer Protocol · World Wide Web · trình duyệt · ứng dụng · uploading · URL · HyperText Markup Language · htm/.html |
| 2.5 | Thư điện tử | 10 | 9, 26, 49, 64, 103, 112, 129, 145, 197–198 | 64, 103, 198 | MUA = Mail User Agent · người_dùng@tên_miền · MTA = Message Transfer Agent · định tuyến, xử lý · khả năng truy cập Internet · giới hạn dung lượng đính kèm · bảo mật phụ thuộc nhà cung cấp · Subject |
| 2.6 | Các dịch vụ khác | 5 | 8, 74–75, 114, 172 | — | WAIS · Telnet · máy chủ ở xa · diễn đàn · lấy dữ liệu từ Internet xuống máy |

### Bài 3 — Giới thiệu về giáo dục điện tử (29 câu)

| Mã | Chủ đề | Số câu | Câu gốc | Câu ⚡ | Từ khóa |
|---|---|---|---|---|---|
| 3.1 | Khái niệm, định nghĩa, quá trình phát triển | 14 | 18, 23, 55, 58, 88, 90–92, 95, 116–117, 152, 179, 182 | — | Electronic · Horton · Compare Infobase · MASIE · Lance Dublin · Sun · nhóm C và D · nhóm B (1–29%) · 30–79% · lấy giảng viên làm trung tâm · CBT = Computer Based Training · Web |
| 3.2 | Đặc điểm, ưu và nhược điểm | 8 | 2, 30, 40, 84, 87, 151, 154, 180 | — | linh hoạt · có hợp tác · học liệu hấp dẫn · giáo án phân nhánh linh hoạt · lợi ích học trên mạng chưa được khẳng định |
| 3.3 | Chuẩn và phần mềm | 7 | 22, 45, 83, 120, 125, 149, 155 | — | Sharable Content Object Reference Model · ADL · đóng gói · đóng gói – trao đổi thông tin – metadata – chất lượng · chuẩn/đặc tả · metadata · 1998 |

### Bài 4 — Phương pháp và quy trình học E-learning (25 câu)

| Mã | Chủ đề | Số câu | Câu gốc | Câu ⚡ | Từ khóa |
|---|---|---|---|---|---|
| 4.1 | Quy trình học, kế hoạch và mục tiêu học tập | 9 | 27, 29, 35–36, 38, 80, 118, 150, 176 | 176 | Học tập · chính của sinh viên · Tiếp thu bài giảng – Thảo luận – Thực hành – Thi cử · bước Học tập · Tiếp thu bài giảng – Tương tác – Luyện tập – Kiểm tra và thi · kế hoạch học tập |
| 4.2 | Học liệu đa phương tiện, bài trắc nghiệm | 3 | 17, 33, 153 | — | truyền tải nội dung · tự đánh giá · trắc nghiệm trực tuyến |
| 4.3 | Trao đổi đồng bộ, không đồng bộ, diễn đàn | 3 | 15, 28, 41 | — | Email · không có mô tả trực quan · không trả lời ngay |
| 4.4 | Mô hình hệ thống: LMS, LCMS, kiến trúc Web | 10 | 81–82, 85–86, 119, 123, 146–148, 178 | — | LCMS = Learning Content Management System · cho phép tạo và tái sử dụng · LMS · từ LCMS · 3 phần · LCMS · môi trường đa người dùng · LMS = Learning Management System · cho phép nhiều giao diện riêng · cho phép |

### Bài 5 — Hướng dẫn sử dụng công cụ E-learning và NEU Elearning (55 câu)

| Mã | Chủ đề | Số câu | Câu gốc | Câu ⚡ | Từ khóa |
|---|---|---|---|---|---|
| 5.1 | Trình duyệt và phần mềm | 9 | 10, 16, 31, 79, 111, 143–144, 174–175 | 174 | Internet Explorer · IDM · Home · không sửa được · chuột phải → Open in New Window · Adobe Reader |
| 5.2 | Tìm kiếm Google | 14 | 5, 24, 32, 72, 76–78, 106, 108, 113, 136, 142, 167, 169 | — | Safari · tách thành từng từ đơn · "cả cụm" · "A" +"B" · site:com · filetype:doc · đồng nghĩa · ngày xác định |
| 5.3 | Email (Yahoo Mail) | 14 | 12, 42, 50, 70, 107, 115, 137–140, 166, 168, 170, 173 | 50, 70 | Attach Files · Subject · Sent · Bcc · Microsoft · POP/IMAP · Sổ địa chỉ · Danh bạ · Mật khẩu |
| 5.4 | Chat | 4 | 7, 109–110, 141 | — | YM, WLM, Skype · IDM · Instant Message · Web Chat |
| 5.5 | Diễn đàn | 2 | 1, 46 | 1 | không chỉnh sửa · Tải file từ máy |
| 5.6 | Hệ thống NEU Elearning | 12 | 3, 11, 13–14, 20, 25, 44, 121–122, 124, 177, 181 | — | Moodle · Google Mail · Cập nhật hồ sơ cá nhân · 2 kiểu |

## 5. Mục lục `de-cuong.md` (Đề cương)

- 🎯 Đề thi hỏi gì
- Bài 1 (slide 2018): Những khái niệm cơ bản
  - Mục tiêu
  - Tóm tắt nội dung
  - Khái niệm / số liệu / danh sách cần thuộc
- Bài 2 (slide 2018): Kiến trúc mạng Internet – Địa chỉ IP và tên miền – Một số dịch vụ Internet thông dụng
  - Mục tiêu
  - Tóm tắt nội dung
  - Khái niệm / số liệu / danh sách cần thuộc
- Bài 3 (slide 2018): Hướng dẫn sử dụng một số dịch vụ Internet thông dụng
  - Mục tiêu
  - Tóm tắt nội dung
  - Khái niệm / thao tác / danh sách cần thuộc
- Bài 4 (slide 2018): Mô hình hệ thống E-learning
  - Mục tiêu
  - Tóm tắt nội dung
  - Khái niệm / số liệu / danh sách cần thuộc
- Phụ lục: Hướng dẫn sử dụng hệ thống NEU E-learning
  - Tóm tắt (theo mục, tên chức năng/menu/nút)
  - Chi tiết cần thuộc

## 6. Mục lục `cach-hoc-thuoc.md` (Cách học thuộc)

- 1. Cách học thuộc 215 câu
  - Ưu tiên theo số câu
  - Mỗi chủ đề làm 3 bước
  - Nhớ đáp án bằng từ khóa, không nhớ chữ cái
  - Học viết tắt theo "khuôn"
- 2. Quy luật đáp án
- 3. Bảng con số, năm, viết tắt
- 4. Những cặp dễ nhầm
- 5. Lịch học thuộc

## 7. Câu hỏi mẫu nên hỏi NotebookLM

- "Câu 198 đáp án là gì, vì sao là bẫy? Giải thích theo đề cương."
- "Tạo quiz 10 câu từ chủ đề 1.1, chỉ dùng câu có sẵn trong ngân hàng, giữ nguyên đáp án ✅."
- "Liệt kê tất cả câu ⚡ của Bài 2 kèm đáp án và lý do là bẫy."
- "Đọc dòng 🔑 Ghi nhớ của mọi chủ đề Bài 1 rồi tóm tắt thành 10 ý."
- "Những cặp khái niệm nào dễ nhầm? Lấy từ cach-hoc-thuoc.md."
- "Tạo Audio Overview ôn Bài 3, nhấn mạnh các câu ⚡."
