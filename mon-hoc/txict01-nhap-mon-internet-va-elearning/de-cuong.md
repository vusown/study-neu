# Đề cương — Nhập môn Internet và E-learning

> Tóm tắt từ slide trong [`tai-lieu/`](tai-lieu/). Slide là **bản cũ ICT101 (2018)**, chia bài khác đề cương 2025. Bảng dưới cho biết bài cũ ứng với bài mới nào.

| Bài trong đề cương 2025 (đề thi theo cách chia này) | Số câu thi | Đọc phần nào bên dưới |
|------|:---:|------|
| Bài 1 — Tổng quan về Internet | 10 | Bài 1 slide (lịch sử Internet, nhà cung cấp) + Bài 2 slide mục 2.1 (phương thức kết nối) |
| Bài 2 — Các dịch vụ Internet thông dụng | 10 | Bài 2 slide (TCP/IP, IP, tên miền, WWW, email, FTP, chat) |
| Bài 3 — Giới thiệu về giáo dục điện tử | 9 | Bài 1 slide (phần E-learning) + Bài 4 slide (khái niệm, đặc điểm, Sloan) |
| Bài 4 — Phương pháp và quy trình học E-learning | 9 | Bài 4 slide (mô hình, chuẩn, quy trình) + **phần 🎯 bên dưới** (slide thiếu) |
| Bài 5 — Hướng dẫn công cụ E-learning & NeuElearning | 12 | Bài 3 slide (trình duyệt, Google, tải tệp, email, chat) + Phụ lục hướng dẫn NEU E-learning |

## Mục lục

- [🎯 Đề thi hỏi gì](#-đề-thi-hỏi-gì)
- [Bài 1 (slide 2018): Những khái niệm cơ bản](#bài-1-slide-2018-những-khái-niệm-cơ-bản)
- [Bài 2 (slide 2018): Kiến trúc mạng, IP, tên miền, dịch vụ](#bài-2-slide-2018-kiến-trúc-mạng-internet--địa-chỉ-ip-và-tên-miền--một-số-dịch-vụ-internet-thông-dụng)
- [Bài 3 (slide 2018): Hướng dẫn sử dụng dịch vụ Internet](#bài-3-slide-2018-hướng-dẫn-sử-dụng-một-số-dịch-vụ-internet-thông-dụng)
- [Bài 4 (slide 2018): Mô hình hệ thống E-learning](#bài-4-slide-2018-mô-hình-hệ-thống-e-learning)
- [Phụ lục: Hướng dẫn sử dụng NEU E-learning](#phụ-lục-hướng-dẫn-sử-dụng-hệ-thống-neu-e-learning)

---

## 🎯 Đề thi hỏi gì

> Tóm tắt **215 câu** trong ngân hàng (50 câu đề thi thử + 165 câu bài luyện tập trên hệ thống), xếp theo 5 bài của đề cương 2025. Học kèm [ngân hàng theo chủ đề](ngan-hang-theo-chu-de.md). **Phần này ưu tiên học trước.**
> Nhiều ý ở Bài 4 (kế hoạch học tập, học liệu, trao đổi đồng bộ/không đồng bộ, 2 kiểu bài trắc nghiệm, hộp thư dựa trên Google Mail) **không có trong slide** đang có, chỉ có trong ngân hàng câu hỏi.

**Bài 1 — Tổng quan về Internet**
- *Khái niệm và lịch sử Internet* (6 câu): Internet = **Inter-network** (mạng của các mạng), liên kết bằng **TCP/IP = Transmission Control Protocol / Internet Protocol**. Hình thành từ dự án **Bộ Quốc phòng Mỹ** (ARPANET, **1969**). Thuật ngữ Internet có từ **1974**. Việt Nam hòa mạng **19/11/1997**.
- *Nhà cung cấp dịch vụ Internet* (5 câu): **ISP**: cấp quyền truy cập + Email, Web, FTP, Telnet, Chat. **IAP** (= **IXP, Internet Exchange Provider**): cung cấp đường truyền, **làm được việc của ISP, ngược lại thì không**. **ICP = Internet Content Provider**: cung cấp **nội dung thông tin** (kinh tế, giáo dục…). **OSP = Online Service Provider**: dịch vụ ứng dụng (mua bán, ngân hàng, tư vấn, đào tạo).
- *Phương thức kết nối* (16 câu): Quay số (dial-up): modem + đường điện thoại, **không thường trực**, **chậm nhất** (20–56 Kbps). **Băng rộng**: tốc độ cao **và** kết nối 24/24. **Leased-Line** (kênh thuê riêng) là phương thức kết nối, còn TCP/IP, NetBEUI, IPX/SPX là bộ giao thức. **HDSL** nhanh hơn ADSL nhưng **không** dùng chung đường điện thoại. DSL **bất đối xứng**: ADSL, RADSL, **VDSL**. DSL đối xứng: IDSL, SDSL, HDSL (download = upload, **đều cao**). ADSL = **Asymmetrical** DSL, cần **modem ADSL chuyên dụng**. Wi-Fi = **Wireless Fidelity** (IEEE 802.11). Hotspot: kết nối **không dây** qua thiết bị thu phát **không dây**.
- *Dịch vụ cơ bản và tổng hợp* (1 câu): E-Mail là dịch vụ **cơ bản**. E-Government, E-learning, E-Banking là dịch vụ **tổng hợp**.

**Bài 2 — Các dịch vụ Internet thông dụng**
- *Giao thức và kiến trúc mạng* (17 câu): ARP = **Address Resolution Protocol** (IP → MAC); **RARP = Reverse ARP** (MAC → IP). Bộ giao thức: NetBEUI, TCP/IP, IPX/SPX. **HTML không phải** giao thức. LAN = **Local Area Network**, MAN = **Metropolitan Area Network**, WAN = **Wide Area Network**. Bộ giao thức mạng: **TCP/IP**, IPX/SPX, NetBEUI (HTTP, HTML thì không). Truyền tệp: **FTP = File Transfer Protocol**; **TFTP = Trivial FTP** (không kết nối, UDP). **SMTP = Simple Mail Transfer Protocol** (truyền thư). **Telnet**: truy nhập từ xa. **NFS** (Network File System, Sun Microsystems): truy xuất file ở xa như đĩa cứng mạng.
- *Địa chỉ IP, IPv6* (22 câu): Mỗi máy có **địa chỉ IP**; có **2 phiên bản** (IPv4, IPv6). IPv6 không gian lớn hơn, định tuyến và bảo mật tốt hơn IPv4. IPv4: **32 bit**, **4 octet**, dạng **A.B.C.D**, mỗi octet **0–255** (256 là sai). Địa chỉ **quảng bá** (dành riêng) không gán cho thiết bị. IP công cộng: duy nhất, toàn cầu, **được** định tuyến trên Internet. IPv6: **128 bit**, **8 cụm**, mỗi cụm **4** ký số hệ 16. IPv6 phân cách bằng **dấu hai chấm**, nhiều gấp **2^96** lần IPv4. Dấu **::** chỉ được dùng **một lần** trong một địa chỉ IPv6.
- *Tên miền* (14 câu): DNS = **Domain Name System**. Domain Name = **tên miền**, **dễ nhớ hơn** IP, phân cách bằng **dấu chấm**; truy nhập máy chủ bằng **IP hoặc tên miền**. Mỗi cấp ≤ **63** ký tự; đầy đủ ≤ **255** ký tự, chỉ gồm a-z, 0-9 và "-" (không có @, _, &). Đếm cấp từ phải sang: neu.edu.vn: vn cấp 1 (ccTLD), **edu cấp 2**, **neu cấp 3**. **.vn** Việt Nam, **.fr** Pháp.
- *Dịch vụ Web* (10 câu): Web dùng **HTTP = HyperText Transfer Protocol**; xem trang web = dịch vụ **World Wide Web** bằng **trình duyệt** (phần mềm **ứng dụng**, không phải phần mềm hệ thống); sao chép trang lên web server = **uploading**; truy cập website cần **URL**. HTML = **HyperText Markup Language**. Mọi web server chạy **.htm/.html**.
- *Thư điện tử* (10 câu): **MUA = Mail User Agent** (tương tác người dùng; không phải "Use"/"Application"), địa chỉ email dạng **người_dùng@tên_miền**, **MTA = Message Transfer Agent** (**định tuyến, xử lý** bản tin). Bắt buộc: **khả năng truy cập Internet**. Webmail: gần như miễn phí, có Internet + trình duyệt là dùng được, đơn giản; nhược điểm: **giới hạn dung lượng đính kèm**, hộp thư bị hạn chế, **bảo mật phụ thuộc nhà cung cấp**. **Subject** mô tả ngắn nội dung thư.
- *Các dịch vụ khác* (5 câu): **WAIS** tìm kiếm dữ liệu. **Telnet**: kết nối **máy chủ ở xa**, dùng khả năng xử lý của nó. Tạo chủ đề, đăng bài, phản hồi = **diễn đàn**. Tải tệp = **lấy dữ liệu từ Internet xuống máy**.

**Bài 3 — Giới thiệu về giáo dục điện tử**
- *Khái niệm, định nghĩa, quá trình phát triển* (14 câu): E = **Electronic**. Định nghĩa: **Horton** = Web và Internet; **Compare Infobase** = CNTT và truyền thông; **MASIE** = chuẩn bị, truyền tải, quản lý… cục bộ hay toàn cục; **Lance Dublin** (doanh nghiệp) = nâng cao hoạt động tổ chức, phát triển cá nhân; **Sun** = Internet, TV, video tape, CBT. Sloan: e-learning là **nhóm C và D** (không phải A, B); "sử dụng công nghệ Internet" là **nhóm B (1–29%)**; truyền thống = **không** có nội dung qua Internet; trực tuyến = **tất cả** trên Internet; **30–79%** là e-learning. Giai đoạn: trước 1983 **lấy giảng viên làm trung tâm**; 1984–1993 **CBT = Computer Based Training**; 1994–1999 công nghệ **Web**.
- *Đặc điểm, ưu và nhược điểm* (8 câu): 8 đặc điểm: mọi lúc mọi nơi, học liệu hấp dẫn, **linh hoạt** khối lượng kiến thức, cá nhân hóa, cập nhật nhanh, **có hợp tác**, theo dõi chặt chẽ, dịch vụ đồng bộ. Chọn bài giảng theo tốc độ mạng là **học liệu hấp dẫn**. Lấy người học làm trung tâm, về nội dung: **giáo án phân nhánh linh hoạt**. Nhược điểm theo cơ sở đào tạo: **lợi ích học trên mạng chưa được khẳng định**.
- *Chuẩn và phần mềm* (7 câu): SCORM = **Sharable Content Object Reference Model**, do **ADL** đưa ra. Ghép khóa học thành gói = chuẩn **đóng gói**. 4 nhóm chuẩn: **đóng gói – trao đổi thông tin – metadata – chất lượng** (không có "phân tích hệ thống"). Các thành phần hiểu nhau nhờ **chuẩn/đặc tả**. Mô tả khóa học để tìm kiếm, phân loại là chuẩn **metadata** (không phải đóng gói). "Moodle phát triển từ **1998**" là **sai**.

**Bài 4 — Phương pháp và quy trình học E-learning**
- *Quy trình học, kế hoạch và mục tiêu học tập* (9 câu): Quy trình 3 bước: Đăng ký → Tìm hiểu thông tin lớp → **Học tập**. 4 hoạt động **chính của sinh viên**: **Tiếp thu bài giảng – Thảo luận – Thực hành – Thi cử** (không có lướt web, gặp mặt nhóm). ⚡ Riêng **bước Học tập** gồm: **Tiếp thu bài giảng – Tương tác – Luyện tập – Kiểm tra và thi**. Nắm vững **kế hoạch học tập**; kế hoạch **không** gồm mục tiêu. Mục tiêu = thay đổi nhận thức, kỹ năng, hành vi; mô tả những gì phải đạt; **không** để biết giảng viên nào dạy.
- *Học liệu đa phương tiện, bài trắc nghiệm* (3 câu): Học liệu → **truyền tải nội dung**. Trắc nghiệm → **tự đánh giá**; lớp E-learning đánh giá chủ yếu bằng **trắc nghiệm trực tuyến**.
- *Trao đổi đồng bộ, không đồng bộ, diễn đàn* (3 câu): **Email** là công cụ không đồng bộ. Thách thức của không đồng bộ: **không có mô tả trực quan**. Diễn đàn **không trả lời ngay** (nhược điểm).
- *Mô hình hệ thống: LMS, LCMS, kiến trúc Web* (10 câu): **LCMS = Learning Content Management System**: quản lý nội dung, **cho phép tạo và tái sử dụng** đơn vị nội dung nhỏ. **LMS**: quản lý phân phối, tìm kiếm nội dung (quá trình học), lấy vị trí khóa học và hoạt động sinh viên **từ LCMS**. Hệ thống E-learning có **3 phần**: hạ tầng truyền thông và mạng – hạ tầng phần mềm – nội dung đào tạo. **LCMS** là **môi trường đa người dùng**. **LMS = Learning Management System**: yêu cầu kỹ thuật (trình duyệt chuẩn, module, tích hợp email), bảo mật (**có** hạn chế truy nhập theo người dùng, đa lớp), giao diện **cho phép nhiều giao diện riêng** cho nhóm người dùng. Kiến trúc Web **cho phép** tăng tương hợp, mở rộng, dùng Intranet và Internet công cộng.

**Bài 5 — Hướng dẫn sử dụng công cụ E-learning và NEU Elearning**
- *Trình duyệt và phần mềm* (9 câu): Khởi động trình duyệt: **Internet Explorer**. Tải tệp: **IDM**. Nút **Home** về trang nhà. Khi duyệt web **không sửa được** nội dung trang. Mở cửa sổ mới: **chuột phải → Open in New Window**. PDF: **Adobe Reader**. SnagIt không phải phần mềm tải tệp.
- *Tìm kiếm Google* (14 câu): **Safari** là trình duyệt, không phải công cụ tìm kiếm. Không ngoặc kép thì **tách thành từng từ đơn**. Cụm chính xác: **"cả cụm"**; vừa cụm này vừa cụm kia: **"A" +"B"**. Lọc tên miền: **site:com**; định dạng: **filetype:doc**. Tìm được tiếng Việt. Toán tử: + kết hợp, − loại trừ, " " chính xác, ~ **đồng nghĩa** (không có trái nghĩa). Ký tự trống không đổi kết quả; Google không tìm tất cả trang web. Tìm kiếm nâng cao không tìm được theo **ngày xác định**.
- *Email (Yahoo Mail)* (14 câu): Người nhận chính: **To**. Đính kèm: **Attach Files**. Inbox thư đến. Chủ đề: **Subject**. Thư đã gửi: **Sent** (Inbox thư đến, Drafts nháp). Giấu người nhận: **Bcc**. Outlook là của **Microsoft**, dùng **POP/IMAP**. Nhớ địa chỉ: **Sổ địa chỉ**, nếu không có thì **Danh bạ**. **Mật khẩu** chứa được @.
- *Chat* (4 câu): Phần mềm chat: **YM, WLM, Skype**. **IDM** là phần mềm tải tệp, không chat. IM = **Instant Message**; hai hình thức chat: **Web Chat** và **IM**.
- *Diễn đàn* (2 câu): Thường **không chỉnh sửa** được bài đã có. Chèn ảnh vào bài NEU Elearning: **Tải file từ máy**.
- *Hệ thống NEU Elearning* (12 câu): Dựa trên **Moodle**. **Không** đổi được tên đăng nhập, **không** đổi mật khẩu của bạn khác. Hệ thống hỗ trợ học tập: diễn đàn, thư điện tử NEU, tin nhắn giảng viên. Hộp thư dựa trên **Google Mail**. Đổi ảnh: bấm tên → **Cập nhật hồ sơ cá nhân**. **2 kiểu** trắc nghiệm: không tính điểm (tự do) và tính điểm (giới hạn lần, thời gian, **không** làm bất kỳ lúc nào).

---

## Bài 1 (slide 2018): Những khái niệm cơ bản

> Slide ghi "chia ra thành **4 thời kỳ**" phát triển e-learning nhưng liệt kê **5 mốc** (trước 1983; 1984–1993; 1994–1999; 2000–2005; 2006 đến nay). Văn bản ghi "Năm 1968 hình thành ARPANET" và "nối thành mạng vào năm 1969", còn Hình 1.1 ghi "ARPANET được thành lập" ở mốc **1969**. Hình 1.1 ghi "NSFNET thay thế ARPANET" ở mốc 1986, trong khi văn bản ghi ARPANET ngừng hoạt động khoảng **1990**. Bài này không có định nghĩa của Sloan Consortium và không nhắc SCORM.

### Mục tiêu
- Hiểu được những khái niệm cơ bản về Internet và e-learning.
- Phân biệt được vai trò của các nhà cung cấp dịch vụ Internet.
- Nắm được quá trình phát triển của Internet và e-learning trên thế giới và ở Việt Nam.

### Tóm tắt nội dung

**1.1. Lịch sử phát triển Internet**

- **Khái niệm Internet:** Internet là viết tắt của **Inter-network**, một mạng máy tính rất lớn kết nối các mạng máy tính khác nhau trên toàn cầu, nên được gọi là **"mạng của các mạng máy tính"**. Các mạng này liên kết với nhau dựa trên bộ giao thức **TCP/IP** (Transmission Control Protocol – Internet Protocol: giao thức điều khiển truyền dẫn – giao thức Internet). Giao thức là **ngôn ngữ giao tiếp chung** giữa các máy tính, giống như một "ngôn ngữ quốc tế" kiểu tiếng Anh.
- Internet giúp chuyển tải thông tin nhanh, cung cấp thông tin như một **thư viện toàn cầu**, và là **diễn đàn** để người dùng trao đổi, giao tiếp.
- **Các mốc lịch sử** (Internet hình thành từ **cuối những năm 1960**):
  - **ARPANET:** mạng do **Bộ Quốc phòng Mỹ** thiết lập. Cơ quan **ARPA** (Advanced Research Project Agency) đề nghị liên kết **4 điểm**: Viện Nghiên cứu **Stanford**, ĐH tổng hợp California tại **Los Angeles**, **UC – Santa Barbara** và ĐH tổng hợp **Utah**. 4 điểm này được nối mạng năm **1969**, đánh dấu **sự ra đời của Internet ngày nay**. ARPANET là **mạng thử nghiệm phục vụ nghiên cứu quốc phòng**.
  - **4 đặc trưng mạng ARPANET hướng tới** (mạng có khả năng khắc phục sự cố):
    1. Vẫn tiếp tục hoạt động ngay cả khi có nhiều kết nối bị hỏng.
    2. Các máy tính có phần cứng khác nhau đều có thể sử dụng mạng.
    3. Tự động điều chỉnh hướng truyền thông tin, bỏ qua phần bị hư hỏng.
    4. Là mạng của các mạng máy tính, tức là dễ mở rộng liên kết.
  - Ban đầu đường truyền chậm (kết nối dây xa nhanh nhất **50 kbit/giây**), ít máy (đến **1982** chỉ khoảng **200 máy chủ**). Máy kết nối chủ yếu thuộc cơ quan Bộ Quốc phòng Mỹ và các trường đại học.
  - **Ethernet:** được phát triển tại **Trung tâm nghiên cứu Palo Alto của Xerox**. Đây là kỹ thuật dùng trong **mạng cục bộ**, sau trở thành một chuẩn quan trọng để kết nối mạng cục bộ.
  - **TCP/IP:** **DARPA** (tên mới của ARPA) hợp nhất TCP/IP vào phiên bản hệ điều hành **UNIX** của ĐH California ở **Berkeley**. "TCP/IP trên Ethernet" trở thành cách thông dụng để các trạm làm việc nối với nhau. **Giữa thập kỷ 1980**, TCP/IP được dùng cho kết nối liên khu vực, mạng cục bộ và mạng liên khu vực.
  - **Thuật ngữ "Internet"** xuất hiện lần đầu khoảng năm **1974**, khi mạng vẫn còn tên ARPANET.
  - **NSFNET:** vào **giữa thập kỷ 1980**, Quỹ khoa học quốc gia Mỹ **NSF** (National Science Foundation) lập mạng liên kết các trung tâm máy tính lớn, gọi là NSFNET. Slide nói **"mạng này chính là mạng Internet"**. Điểm quan trọng của NSFNET là **cho phép mọi người cùng sử dụng**. Đây là mốc lịch sử quan trọng của Internet.
  - **ARPANET ngừng hoạt động** khoảng năm **1990**, sau **gần 20 năm** tồn tại, vì nhiều doanh nghiệp đã chuyển sang NSFNET.
- **Hình 1.1 (sơ đồ lịch sử):** 1969 ARPANET được thành lập → 1983 ARPANET sử dụng bộ giao thức TCP/IP → 1986 NSFNET thay thế ARPANET → 1996 11 triệu máy tính kết nối → 2004 800 triệu máy tính kết nối.

**1.1.3. Internet tại Việt Nam và các nhà cung cấp dịch vụ**

- Ngày **19/11/1997** Việt Nam hòa vào mạng Internet toàn cầu.
- Hết **Quý III/2012**: **31.196.878** người dùng, chiếm **35,49%** dân số. Việt Nam đứng thứ **18/20** thế giới, thứ **8** châu Á, thứ **3** Đông Nam Á. So với năm 2000, số người dùng tăng **hơn 15 lần**. Số liệu theo **VNNIC**.
- **Các nhà cung cấp dịch vụ:**
  - **ISP** (Internet Service Provider, nhà cung cấp dịch vụ Internet) cấp quyền truy cập Internet qua mạng viễn thông và các dịch vụ **Email, Web, FTP, Telnet, Chat**. ISP được **IAP** cấp cổng truy cập vào Internet. Việt Nam có **16 ISP** đăng ký, các ISP lớn gồm **VNPT, FPT, Viettel**.
  - **IAP** (Internet Access Provider, nhà cung cấp dịch vụ đường truyền để kết nối với Internet), còn gọi là **IXP** (Internet Exchange Provider). Nếu coi Internet là "siêu xa lộ thông tin" thì IAP cung cấp phương tiện đưa người dùng vào xa lộ. **IAP có thể làm cả chức năng của ISP, nhưng ISP không làm được chức năng của IAP.** Một IAP thường phục vụ nhiều ISP. Các IXP/IAP ở Việt Nam: **VNPT, FPT, Viettel, ETC** (viễn thông điện lực), **SPT** (Sài Gòn), **HANOITELECOM**, **VTC**.
  - **ISP dùng riêng** được cung cấp đầy đủ dịch vụ Internet. Điểm khác ISP **duy nhất** là **không kinh doanh**. Đây là loại hình của cơ quan hành chính, trường đại học, viện nghiên cứu.
  - **ICP** (Internet Content Provider, nhà cung cấp dịch vụ **nội dung thông tin**) đưa thông tin kinh tế, giáo dục, thể thao, chính trị, quân sự lên mạng và cập nhật định kỳ.
  - **OSP** (Online Service Provider, nhà cung cấp dịch vụ **ứng dụng** Internet) cung cấp mua bán qua mạng, giao dịch ngân hàng, tư vấn, đào tạo…
  - **USER** (người sử dụng) là tổ chức hoặc cá nhân dùng Internet **thông qua ISP**. Người dùng cần **thỏa thuận với một ISP hoặc ISP dùng riêng** về dịch vụ được dùng và cách thanh toán.
- **Phương thức kết nối của người dùng:** qua đường điện thoại, vệ tinh, không dây, kênh thuê riêng… Có thể kết nối **trực tiếp** đến nhà cung cấp hoặc **qua mạng cục bộ** đã có liên kết Internet (Hình 1.4).
- **Hình 1.5 (quan hệ IAP – ISP – ICP – USER):** Internet ↔ IAP qua **Leased line** (kênh thuê riêng). IAP → ISP qua Leased line. ISP → ICP qua Leased line. ISP → USER qua Leased line, hoặc qua **PSTN** (mạng điện thoại công cộng) và **Modem**.

**1.2. Quá trình phát triển e-learning**

- **E-learning** là viết tắt của **Electronic Learning**. Hiểu đơn giản, đó là quá trình đào tạo trong đó việc dạy và học dựa trên **phương tiện điện tử** như TV, máy tính, mạng Internet… E-learning cho phép học **mọi lúc, mọi nơi, không kể tuổi tác**, đồng thời tiết kiệm thời gian và kinh phí.
- E-learning được áp dụng rộng rãi ở các nước phát triển như **Anh, Mỹ, Nhật**. Tập đoàn dữ liệu quốc tế **IDG** nhận định e-learning sẽ phát triển bùng nổ.
- **Các giai đoạn phát triển e-learning:**
  - **Trước năm 1983:** máy tính chưa phổ biến. Phương pháp phổ biến nhất là **"Lấy giảng viên làm trung tâm"**, tức đào tạo truyền thống.
  - **1984–1993:** ra đời **Windows 3.1, máy Macintosh, PowerPoint** và các công cụ đa phương tiện, mở ra **kỷ nguyên đa phương tiện**. Bài giảng có hình ảnh, âm thanh dựa trên công nghệ **CBT** (Computer Based Training), phân phối qua **CD-ROM hoặc đĩa mềm**. Người học có thể mua về tự học, nhưng **sự hướng dẫn của giảng viên rất hạn chế**.
  - **1994–1999:** **công nghệ Web** ra đời. Thư điện tử, trình duyệt, trang Web viết bằng **HTML và JAVA**, truyền âm thanh và hình ảnh qua mạng trở nên phổ dụng. Có e-mail, CBT, **Intranet** với text và hình ảnh đơn giản, đào tạo qua Web với hình ảnh chuyển động tốc độ thấp.
  - **2000–2005:** JAVA, ứng dụng mạng IP, băng thông cao hơn, công nghệ thiết kế Web tiên tiến tạo ra cách mạng đào tạo giá rẻ, chất lượng cao. Slide gọi giai đoạn này là **"làn sóng thứ 2 của e-learning"**.
  - **2006 đến nay:** Internet tốc độ cao, Web có **flash**, xử lý ảnh và video tốc độ cao. Xuất hiện lớp học **truyền hình trực tiếp (online)**, kho video truy cập mọi lúc, bài học đồng bộ âm thanh, hình ảnh và slide, trao đổi trực tiếp với giảng viên (**chat**).
- **Xu hướng quan hệ Dạy – Học:** **Lấy người Thầy làm trung tâm (Dạy) → Tạo sự bình đẳng giữa Thầy và Trò (Dạy – Học) → Lấy học Trò làm trung tâm (Học)**. Vì vậy e-learning luôn được hiểu **gắn với quá trình Học** hơn là với quá trình dạy – học.
- **Hình thức triển khai:** đơn giản nhất là **bài giảng điện tử trên CD-ROM** để tự học. Phức tạp hơn là **lớp học trên Internet có quản lý hệ thống**. Hệ thống e-learning gồm nhiều thành phần chức năng tách riêng, mỗi thành phần cung cấp một dịch vụ, nhưng được tập trung trong **một hệ thống thống nhất**. Về bản chất vẫn là truyền tải kiến thức từ giảng viên đến người học **dưới sự giám sát của hệ thống quản lý**.
- **Kênh phân phối nội dung:** Internet, intranet/extranet (**LAN/WAN**), băng audio và video, vệ tinh quảng bá, truyền hình tương tác, CD-ROM và các học liệu điện tử khác. Người học học bằng máy tính, qua **trang Web của một lớp học ảo**.

### Khái niệm / số liệu / danh sách cần thuộc

**Viết tắt**

| Viết tắt | Đầy đủ | Nghĩa |
|---|---|---|
| Internet | Inter-network | mạng của các mạng máy tính |
| TCP/IP | Transmission Control Protocol – Internet Protocol | giao thức điều khiển truyền dẫn – giao thức Internet |
| ARPA | Advanced Research Project Agency | cơ quan quản lý dự án nghiên cứu cấp cao, Bộ Quốc phòng Mỹ |
| DARPA | – | tên mới của ARPA |
| NSF | National Science Foundation | Quỹ khoa học quốc gia Mỹ |
| ISP | Internet Service Provider | nhà cung cấp dịch vụ Internet |
| IAP | Internet Access Provider | nhà cung cấp dịch vụ đường truyền kết nối Internet |
| IXP | Internet Exchange Provider | tên khác của IAP |
| ICP | Internet Content Provider | nhà cung cấp nội dung thông tin |
| OSP | Online Service Provider | nhà cung cấp dịch vụ ứng dụng Internet |
| PSTN | – | mạng điện thoại công cộng (Hình 1.5) |
| VNNIC | – | nguồn số liệu Internet Việt Nam |
| E-learning | Electronic Learning | học tập điện tử |
| CBT | Computer Based Training | đào tạo dựa trên máy tính |
| IDG | – | Tập đoàn dữ liệu quốc tế |

**Định nghĩa e-learning (nguyên văn theo slide, kèm tác giả)**

| Tác giả / nguồn | Định nghĩa |
|---|---|
| **William Horton** | "E-learning là sử dụng các **công nghệ Web và Internet** trong học tập." |
| **Compare Infobase Inc** | "E-learning là một thuật ngữ dùng để mô tả việc học tập, đào tạo dựa trên **công nghệ thông tin và truyền thông**." |
| **MASIE Center** | "E-learning nghĩa là việc học tập hay đào tạo được **chuẩn bị, truyền tải hoặc quản lý** sử dụng nhiều công cụ của công nghệ thông tin, truyền thông khác nhau và được thực hiện ở **mức cục bộ hay toàn cục**." |
| **Sun Microsystems, Inc** | "Việc học tập được truyền tải hoặc hỗ trợ qua **công nghệ điện tử**. Việc truyền tải qua nhiều kĩ thuật khác nhau như Internet, TV, video tape, các **hệ thống giảng dạy thông minh**, và việc đào tạo dựa trên máy tính (**CBT**)." |
| **e-learning site** | "Việc truyền tải các **hoạt động, quá trình, và sự kiện** đào tạo và học tập thông qua các phương tiện điện tử như Internet, intranet, extranet, CD-ROM, video tape, DVD, TV, các thiết bị cá nhân..." |
| **Lance Dublin** (hướng tới **e-learning trong doanh nghiệp**) | "Việc sử dụng công nghệ để tạo ra, đưa các dữ liệu có giá trị, thông tin, học tập và kiến thức với mục đích **nâng cao hoạt động của tổ chức và phát triển khả năng cá nhân**." |

- **Kết luận của bài về e-learning:** "hệ thống đào tạo sử dụng các **công nghệ đa phương tiện dựa trên nền tảng Internet**". Hiểu cụ thể hơn: "quá trình học **thông qua mạng Internet và công nghệ Web**".

**Năm và con số**

| Mốc | Sự kiện / con số |
|---|---|
| Cuối những năm 1960 | Internet bắt đầu hình thành |
| 1968 | Hình thành mạng ARPANET (theo văn bản) |
| 1969 | 4 điểm được nối mạng, đánh dấu sự ra đời của Internet (Hình 1.1: ARPANET thành lập) |
| ~1974 | Thuật ngữ "Internet" xuất hiện lần đầu |
| 1982 | Khoảng 200 máy chủ trên ARPANET |
| 1983 | ARPANET sử dụng TCP/IP (Hình 1.1) |
| Giữa thập kỷ 1980 | NSFNET ra đời; TCP/IP dùng cho kết nối liên khu vực |
| 1986 | NSFNET thay thế ARPANET (Hình 1.1) |
| ~1990 | ARPANET ngừng hoạt động, sau gần 20 năm tồn tại |
| 1996 / 2004 | 11 triệu / 800 triệu máy tính kết nối (Hình 1.1) |
| 19/11/1997 | Việt Nam hòa vào Internet toàn cầu |
| Quý III/2012 | Việt Nam có 31.196.878 người dùng (35,49% dân số); xếp hạng 18/20 thế giới, 8 châu Á, 3 Đông Nam Á; tăng hơn 15 lần so với năm 2000 |

- **50 kbit/s:** tốc độ truyền nhanh nhất của kết nối dây xa thời kỳ đầu.
- **4 điểm** của ARPANET ban đầu; **4 đặc trưng** mạng ARPANET hướng tới.
- **16 ISP** đăng ký ở Việt Nam.

**Danh sách và phân loại**
- 4 điểm ARPANET: Stanford, UCLA, UC Santa Barbara, ĐH Utah.
- Các nhà cung cấp: **IAP/IXP → ISP (và ISP dùng riêng) → ICP, OSP → USER**.
- 3 ISP lớn: VNPT, FPT, Viettel. IXP/IAP: VNPT, FPT, Viettel, ETC, SPT, HANOITELECOM, VTC.
- Các giai đoạn e-learning: trước 1983 → 1984–1993 (CBT, CD-ROM) → 1994–1999 (Web) → 2000–2005 (làn sóng thứ 2) → 2006 đến nay (online, video, chat).

---

## Bài 2 (slide 2018): Kiến trúc mạng Internet – Địa chỉ IP và tên miền – Một số dịch vụ Internet thông dụng
> Tên bài tự đặt theo nội dung (file thiếu trang tiêu đề).

> **File PDF bắt đầu từ trang 12** ("Tình huống dẫn nhập"), thiếu trang 11 gồm tiêu đề bài, Hướng dẫn học, Nội dung và Mục tiêu.
>
> **Lỗi và mâu thuẫn trong slide (thi nên chọn theo slide nhưng cần cẩn thận):**
> - Tốc độ dial-up ghi "dao động từ **2056Kbps**" (có lẽ là 20–56 Kbps).
> - Tốc độ IDSL ghi **144Mbps** trong văn bản, nhưng bảng ghi **144 Kbps**.
> - VDSL ghi upload 2,3 Mbps trong văn bản, nhưng bảng ghi 1,6 / 3,2 / 6,4 Mbps.
> - ADSL ghi upload 16–640 Kbps trong văn bản, nhưng bảng ghi "tải lên tối đa 1,5 Mbps".
> - WAN bị chú thích sai là "Wireless Local Area Network" ở mục Leased-line. Ở mục DECnet, slide ghi đúng WAN = Wide Area Network.
> - Cổng chat ghi "6667 hoặc 5000" ở mục Port, nhưng mục Chat ghi "6667 hoặc 23". HTTP ghi ở "cổng 8080".
> - Tên miền home.vnn.vn được gán cho "VDC", nhưng www.home.vnn.vn lại được gán cho "VNNIC".
> - Slide ghi có "**16** hệ thống máy chủ tên miền ở mức ROOT".
> - Phần TCP/IP bị vỡ một dòng "(API- Application Programming Interface".
> - Có lỗi gõ: "Coltrol", "Digtal Equipment Corpration", "Windows 95, 97", "MNS messenger", "kết nối luống 3 pha".

### Mục tiêu
Slide thiếu trang này (cần xác minh). Ba câu hỏi dẫn nhập của bài:
1. Kiến trúc tổng quát của Internet như thế nào? Có các phương thức nào để kết nối Internet? Các giao thức kết nối mạng?
2. Địa chỉ IP và tên miền là gì? Vai trò của hệ thống tên miền?
3. Có các loại dịch vụ Internet thông dụng nào?

### Tóm tắt nội dung

**2.1. Kiến trúc mạng Internet**

- **Kiến trúc tổng quát:** Internet là một **liên mạng** kết nối các mạng nhỏ hơn qua kết nối viễn thông. Thiết bị kết nối các mạng là **cổng nối Internet (Internet Gateway)** hoặc **bộ định tuyến (Router)**. **Đối với người dùng, Internet chỉ là một mạng duy nhất.**
- **5 phương thức kết nối chính:** **điện thoại (dial-up), băng rộng, vệ tinh, không dây, kênh thuê riêng**. Lưu ý: phần tóm lược cuối bài chỉ liệt kê 4 phương thức (kênh thuê riêng, băng rộng, quay số, không dây).
  1. **Dial-up (quay số qua mạng điện thoại):** cần **đường điện thoại và Modem**. Người dùng quay số của ISP, ví dụ số **1260** của **VNN**. Tốc độ lý thuyết "2056Kbps" (xem ghi chú lỗi), thực tế khó đạt **56Kbps**. Đây là phương thức **chậm nhất**.
  2. **Băng rộng:** tốc độ cao, **luôn kết nối 24/24**. Gồm các công nghệ **DSL** (Digital Subscriber Line, kênh thuê bao số) và **modem cáp**, tốc độ **521Kbps** trở lên, **xấp xỉ gấp 9 lần** dial-up.
     - **DSL bất đối xứng** (**ADSL, RADSL, VDSL**): download nhanh hơn upload, **có thể chia sẻ chung với đường điện thoại**.
       - **ADSL** (Asymmetrical DSL): truyền qua đường dây điện thoại sẵn có, trên **một đôi dây**. Download **1,5–9 Mbps**, upload **16–640 Kbps**. Cần **modem ADSL chuyên dụng**.
         - ADSL1: 1,5 Mbps xuống / 16 Kbps lên, hỗ trợ **MPEG-1**.
         - ADSL2: 3 Mbps xuống / 16 Kbps lên, hỗ trợ **2 dòng MPEG-1**.
         - ADSL3: 6 Mbps xuống / ít nhất 64 Kbps lên, hỗ trợ **MPEG-2**.
         - ADSL dùng phổ biến hiện nay: lý thuyết **8 Mbps** nhận / **2 Mbps** gửi.
       - **RADSL** (Rate Adaptive DSL): ADSL **tự điều chỉnh tốc độ theo chất lượng tín hiệu**, còn gọi là **"ADSL có tốc độ biến đổi"**. Thực tế nhiều công nghệ ADSL là RADSL.
       - **VDSL/VHDSL** (Very High Bit Rate DSL): tốc độ tải xuống **cao nhất trong các xDSL, 52 Mbps**. Hoạt động tốt trong **mạng mạch vòng ngắn**. Truyền dẫn chủ yếu bằng cáp quang, chỉ dùng cáp đồng ở đầu cuối.
     - **DSL đối xứng** (**HDSL, SDSL, IDSL**): download bằng upload, **không chia sẻ với đường điện thoại**.
       - **HDSL** (High Bit Rate DSL): nhanh hơn ADSL, truyền **T1** qua **2 cặp cáp**, dài tối đa **3.657 m**. **HDSL-2** chỉ cần **1 cặp**, dài tối đa **5.486 m**. Tốc độ **668 Kbps – 2,048 Mbps (E1)**.
       - **SDSL** (Symmetric DSL): phiên bản của HDSL nhưng chỉ dùng **1 cặp cáp**, tốc độ **160 Kbps – 1,5 Mbps**.
       - **IDSL** (ISDN DSL): khoảng cách xa nhất, **7.924 m**, tốc độ 144 (xem ghi chú lỗi).
     - **Cable modem:** truyền dữ liệu qua **mạng truyền hình cáp**, nối máy tính qua **cổng Ethernet** nên **luôn sẵn sàng**, không cần quay số. Tốc độ phụ thuộc **số người dùng cùng lúc**, tối đa hiện nay **2 Mbps**.
  3. **Vệ tinh:** dùng cho vùng sâu, vùng xa, hải đảo. Có **3 loại**: phát đa hướng "một chiều" (one-way), phản hồi "một chiều", và truy cập vệ tinh "2 chiều". Loại **2 chiều** có upstream tối đa **1 Mbps**, **độ trễ 1 giây**.
  4. **Không dây:**
     - **Hotspot:** địa điểm cung cấp kết nối không dây và truy cập Internet tốc độ cao qua **Wireless Access Point**.
     - **Wi-Fi** (**Wireless Fidelity**): tập hợp chuẩn cho **WLAN** (Wireless Local Area Network) dựa trên **IEEE 802.11**.
       - 802.11: 1–2 Mbps.
       - 802.11a: lên tới **54 Mbps**.
       - 802.11b (còn gọi là **802.11 High Rate** hoặc Wi-Fi): tối đa **11 Mbps**.
       - 802.11g: tối đa **trên 20 Mbps**.
     - **WiMAX** (**IEEE 802.16**): băng rộng không dây, phủ sóng tới **50 km**. Kết nối các hotspot Wi-Fi tới Internet, chia sẻ dữ liệu tới **70 Mbps**, đủ cho **60 doanh nghiệp** dùng đường T1 cùng lúc và **hơn 1000 người** dùng DSL 1 Mbps.
  5. **Kênh thuê riêng (Leased-Line):** kết nối trực tiếp giữa các node mạng, có **cổng kết nối quốc tế riêng biệt**, dành cho văn phòng, công ty cần chất lượng cao. Tốc độ **từ 256 Kbps đến hàng chục Gbps**, cam kết tốt nhất về độ ổn định.
     - Thiết bị đầu cuối **CSU/DSU** (Channel Service Unit/Data Service Unit) phụ thuộc nhà cung cấp. Chuẩn kết nối chính: **HDSL, G703**.
     - Mỗi kết nối kênh thuê riêng cần **một giao tiếp WAN**: nối tới 10 điểm thì cần **10 giao tiếp WAN**.
     - **Nhược điểm:** đầu tư thiết bị ban đầu lớn, không linh hoạt khi mở rộng, quản lý phức tạp, chi phí thuê kênh lớn khi khoảng cách xa.
     - **Giao thức dùng với leased-line: HDLC, PPP, LAPB.**
       - **HDLC** (High-level Data Link Control): **chỉ dùng khi cả hai phía là bộ định tuyến Cisco**.
       - **PPP** (Point-to-Point Protocol): **chuẩn quốc tế**, tương thích mọi hãng. **Bắt buộc dùng** khi một phía là Cisco và phía kia là hãng thứ ba. Là giao thức **lớp 2**, cho phép nhiều giao thức mạng chạy trên nó nên **phổ biến**.
       - **LAPB** (Link Access Procedure Balanced): giao thức **lớp 2** tương tự **X.25**, **ít được sử dụng**.

**2.1.3. Các giao thức kết nối mạng**

- **Giao thức (Protocol):** **tập hợp những quy tắc, quy ước truyền thông** về khuôn dạng cú pháp dữ liệu, thủ tục gửi và nhận, kiểm soát chất lượng truyền.
- **Các bộ giao thức:**
  - **NetBEUI** (NetBIOS Enhanced User Interface, giao diện người dùng nâng cao NetBIOS): do **Microsoft** phát triển, là giao thức **ngầm định của Windows trước Windows 2000**. Nhanh, hiệu quả, hợp với **mạng nội bộ chỉ dùng Windows**, có **phân giải tên sẵn**, không cần thiết lập. Được cung cấp theo sản phẩm **IBM**. **Nhược điểm: không hỗ trợ định tuyến**, chỉ dùng trong mạng Microsoft.
  - **IPX/SPX:** bộ giao thức chuẩn của **Novell NetWare**.
    - **IPX** (Internetwork Packet Exchange) tương tự IP, **không bảo đảm** chuyển giao, gói tin có thể bị router "đánh rơi".
    - **SPX** (Sequenced Packet Exchange) thuộc **lớp vận chuyển (transport) trong mô hình OSI 7 lớp**, tương tự TCP, **đảm bảo** truyền chính xác, dùng IPX làm cơ chế vận chuyển.
    - **Ưu điểm:** nhỏ, nhanh, hiệu quả trên mạng cục bộ, **hỗ trợ định tuyến**.
  - **DECnet:** bộ giao thức độc quyền của **Digital Equipment Corporation**. Định nghĩa truyền thông qua **LAN, MAN, WAN**, **hỗ trợ định tuyến**.
  - **TCP/IP:** ưu điểm chính là **liên kết hoạt động nhiều loại máy tính khác nhau**. Là **tiêu chuẩn thực tế** cho kết nối liên mạng và Internet toàn cầu.

**2.1.3.3. Bộ giao thức TCP/IP**

- **Lịch sử:** gắn với ARPAnet của Bộ Quốc phòng Mỹ. Được dùng rộng rãi nhất **vì tính mở**. Hai giao thức chủ yếu là **TCP** và **IP**.
  - **1981:** TCP/IPv4 hoàn tất, phổ biến cho máy dùng **UNIX**.
  - **1994:** có **bản thảo IPv6** để cải tiến hạn chế của IPv4.
- **Mô hình TCP/IP có 4 tầng** (từ dưới lên):
  1. **Truy cập mạng (Network Access):** tầng **thấp nhất**, gồm thiết bị giao tiếp mạng, truy cập đường truyền vật lý. Ví dụ Ethernet, Fast Ethernet, Token Ring, FDDI (Hình 2.10). Tương ứng tầng **Data Link + Physical** của OSI, còn gọi là "Host-to-network".
  2. **Liên mạng (Internet):** cung cấp **địa chỉ logic** độc lập phần cứng và **chức năng định tuyến**, gắn kết địa chỉ vật lý với địa chỉ logic. Giao thức: **IP, ICMP, IGMP** (hình vẽ có thêm **ARP, RARP**). Tương ứng tầng **Network** của OSI.
  3. **Giao vận (Transport):** kiểm soát luồng, kiểm tra lỗi, xác nhận. Đóng vai trò giao diện cho ứng dụng mạng. Hai giao thức chính: **TCP và UDP**.
  4. **Ứng dụng (Application):** tầng **trên cùng**, hỗ trợ **API**. Tương ứng **Application + Presentation + Session** của OSI.
- **Mô hình OSI** (Open System Interconnection Reference Model) có **7 tầng**: Application, Presentation, Session, Transport, Network, Data Link, Physical.
- **Truyền và nhận dữ liệu:**
  - **Khi truyền**, dữ liệu đi từ tầng ứng dụng **xuống** tầng truy cập mạng. Mỗi tầng **thêm header vào trước** phần dữ liệu.
  - **Khi nhận**, quá trình đi theo chiều **ngược lại**: mỗi tầng **tách header** rồi chuyển lên tầng trên.
- **Đơn vị dữ liệu theo tầng:**

| Tầng | Dùng TCP | Dùng UDP |
|---|---|---|
| Ứng dụng | **stream** (đơn vị là Byte) | **message** |
| Giao vận | **Segment** | **Datagram** |
| Internet | **Datagram** | **Datagram** |
| Truy cập mạng | **Frame** | **Frame** |

- **Giao thức tầng ứng dụng:**
  - **FTP** (File Transfer Protocol): truyền tệp, **dùng TCP**.
  - **NFS** (Network File System): hệ thống file phân tán của **Sun Microsystems**, truy xuất file ở xa như một đĩa cứng trên mạng.
  - **Telnet** (Terminal Emulation): truy nhập từ xa.
  - **SNMP** (Simple Network Management Protocol): thu thập thống kê, hiệu suất, bảo mật (quản lý mạng).
  - **SMTP** (Simple Mail Transfer Protocol): truyền thư điện tử.
  - **LPD** (Line Printer Daemon Protocol): dịch vụ nền cho máy in dòng.
  - **DNS** (Domain Name System): quy tắc sử dụng tên miền.
  - **TFTP** (Trivial FTP): dạng khác của FTP, **không kết nối, dùng UDP**.
  - Hình 2.12 phân nhóm: File Transfer (TFTP, FTP, NFS); E-mail (SMTP); Remote Login (Telnet, rlogin); Network Management (SNMP); Name Management (DNS).
- **TCP:** giao thức **có liên kết (Connection-oriented)**, đơn vị là **segment**. Chức năng: truyền dữ liệu, **dồn kênh**, đảm bảo tin cậy, **điều khiển luồng**, kết nối theo **phương thức 3 pha** (slide ghi "kết nối luống 3 pha", thường gọi là bắt tay 3 bước). Header **20 bytes**.
  - **Các trường TCP Segment:** Source Port **16 bit**, Destination Port **16 bit**, Sequence Number **32 bit**, Acknowledgment Number **32 bit**, Header Length **4 bit**, Reserved **6 bit** (luôn = 0), Code bits **6 bit**, Window **16 bit**, Checksum **16 bit** (kiểm lỗi theo **CRC**), Urgent Pointer **16 bit**, Options, Padding, TCP data.
  - Nếu SYN được thiết lập thì Sequence Number là **ISN** (Initial Sequence Number), byte dữ liệu đầu tiên là **ISN+1**. ISN được **khởi tạo ngẫu nhiên**.
  - **6 bit điều khiển: URG, ACK, PSH, RST, SYN, FIN.**
    - URG = 1 khi có dữ liệu khẩn (chỉ ra ở Urgent Pointer).
    - PSH: chuyển dữ liệu đi ngay.
    - RST: báo lỗi và khởi động lại kết nối.
    - SYN = 1 khi thiết lập kết nối.
    - FIN = 1 khi trạm nguồn hết thông tin.
  - **Window:** số byte trạm nguồn sẵn sàng nhận.
  - **Padding:** toàn số 0, giúp header kết thúc ở mốc **32 bit**.
  - **TCP data:** độ dài tối đa mặc định **536 byte**, có thể chỉnh trong Options.
- **Số hiệu cổng (Port):** một tiến trình ứng dụng truy nhập TCP qua **port**. Số cổng dài **2 byte**.
  - Theo slide: HTTP/web ở cổng **8080**; chat ở **6667 hoặc 5000**.
  - **IANA** (Internet Assigned Numbers Authority) đưa ra danh sách cổng thông dụng.
  - Cổng **< 1024** là port "danh tiếng" (định nghĩa trong **RFC 3232**). Cổng **≥ 1024** được gán động.
  - **Hình 2.16:** FTP **21**, Telnet **23**, SMTP **25**, DNS **53**, TFTP **69**, SNMP **161**, RIP **520**. Trong hình, FTP, Telnet, SMTP, DNS chạy trên TCP; TFTP, SNMP, RIP chạy trên UDP.
- **Socket = Số hiệu cổng + địa chỉ IP + tên giao thức tầng truyền tải (TCP).**
  - Một cặp **địa chỉ IP** nguồn/đích xác định duy nhất quan hệ giữa **2 thiết bị**.
  - Một cặp **Socket** nguồn/đích xác định duy nhất quan hệ giữa **2 ứng dụng**.
- **UDP** (User Datagram Protocol): giao thức **không liên kết (Connectionless)**, dịch vụ **không tin cậy**, **không dùng cơ chế Window**, đơn vị là **datagram**.
  - Có chức năng truyền dữ liệu và **dồn kênh** bằng số hiệu cổng, giống TCP.
  - **Không** phục hồi dữ liệu, **không** sắp xếp dữ liệu.
  - Khuôn dạng **không có** trường Sequence, Acknowledgment, Window.
  - **Lợi thế so với TCP:** datagram ngắn hơn; không đợi xác nhận nên **bộ nhớ giải phóng nhanh hơn**, không trì hoãn ứng dụng.
- **IP** (Internet Protocol): thuộc **tầng mạng của OSI**, kết nối các mạng con thành liên mạng. Là giao thức **không liên kết**, đơn vị là **IP datagram**.
  - **Các trường IP Datagram:**
    - **VERS** 4 bit: phiên bản IP.
    - **HLEN** 4 bit: độ dài header theo đơn vị từ 32 bit; **tối thiểu 5 từ (20 bytes), tối đa 15 từ (60 bytes)**.
    - **Type of service** 8 bit: ưu tiên, độ trễ, năng suất, độ tin cậy.
    - **Total Length** 16 bit: độ dài cả gói (header + data).
    - **Identification** 16 bit: dùng để ráp lại các phân đoạn.
    - **Flags** 3 bit: điều khiển phân đoạn (fragment).
    - **Fragment Offset** 13 bit: tính theo đơn vị **8 bytes**.
    - **Time to Live** 8 bit: thời gian tồn tại tính bằng giây. **Giảm 1 khi qua mỗi router**, bằng 0 thì gói bị xóa, tránh gói tin bị quẩn.
    - **Protocol** 8 bit: giao thức tầng trên.
    - **Header Checksum** 16 bit.
    - **Source Address 32 bit**, **Destination Address 32 bit**.
    - Options, Padding (mốc 32 bit).
    - **Data:** bội của 8 bytes, tối đa **65.535 bytes (64 KB)**.
  - **Mã Protocol:**

| Mã | Giao thức | Mã | Giao thức |
|---|---|---|---|
| 0 | Reserved | 8 | EGP |
| 1 | ICMP | 9 | Private Interior Routing Protocol |
| 2 | IGMP | **17** | **UDP** |
| 3 | GGP | 41 | IPv6 |
| 4 | IP (IP encapsulation) | 50 | ESP |
| 5 | Stream | 51 | AH |
| **6** | **TCP** | 89 | Open Shortest Path First |

- **ICMP** (Internet Control Message Protocol): **giao thức thông báo lỗi**. Các thông điệp: Destination Unreachable, Echo Request and Reply, Redirect, Time Exceeded, Router Advertisement, Router Solicitation…
- **ARP** (Address Resolution Protocol): chuyển **IP → MAC** (địa chỉ vật lý).
- **RARP** (Reverse ARP): chuyển **MAC → IP**.

**2.2. Địa chỉ IP và tên miền**

- Mỗi máy tính cần **một địa chỉ duy nhất** trong mạng, giống số thuê bao điện thoại di động.
- **IPv4:**
  - Dài **32 bit**, gồm **4 octet**, mỗi octet **8 bit** có giá trị **0..255**.
  - Biểu diễn bằng **4 cụm số thập phân cách nhau bởi dấu chấm** (ví dụ 203.119.9.0).
  - Là phiên bản **đầu tiên**, cung cấp **2^32 = 4.294.967.296** (khoảng **4 tỉ**) địa chỉ.
  - Mỗi địa chỉ gồm **NetworkID** và **HostID**.
- **Các lớp IPv4:**
  - **A, B, C** dùng gán địa chỉ.
  - **Lớp D: Multicast.**
  - **Lớp E: Research.**

| Lớp | Bit đầu | Dạng | Số mạng | Số host/mạng | Vùng lý thuyết | Vùng sử dụng | Ví dụ |
|---|---|---|---|---|---|---|---|
| A | 0 | N.H.H.H | 2^7 − 2 = **126** | 2^24 − 2 = **16.777.214** | 0.0.0.0 – 127.255.255.255 | 1.0.0.1 – 126.255.255.254 | 120.122.1.2; 1.2.3.4 |
| B | 10 | N.N.H.H | 2^14 − 2 = **16.382** | 2^16 − 2 = **65.534** | 128.0.0.0 – 191.255.255.255 | 128.1.0.1 – 191.254.255.254 | 140.108.2.2; 191.222.2.10 |
| C | 110 | N.N.N.H | 2^21 − 2 = **2.097.150** | 2^8 − 2 = **254** | 192.0.0.0 – 223.255.255.255 | 192.0.1.1 – 223.255.254.254 | 192.168.10.2 |

  - Octet đầu (range trên hình): A **1–126**, B **128–191**, C **192–223**.
  - Mạng có bit NetID **toàn 0 hoặc toàn 1** thì không được phân bổ:
    - Lớp A: 0.Y.Z.T và 127.Y.Z.T.
    - Lớp B: 128.0.Z.T và 191.255.Z.T.
    - Lớp C: 192.0.0.T và 223.255.255.T.
- **Địa chỉ dành riêng** (không gán cho thiết bị):
  - **Địa chỉ mạng:** bit HostID **toàn 0**, dùng để định danh chính mạng đó.
  - **Địa chỉ quảng bá (broadcast):** bit HostID **toàn 1**, gửi gói tới mọi thiết bị trong mạng.
- **IP Public và IP Private:**
  - **IP công cộng:** duy nhất, toàn cầu, chuẩn hóa. Lấy từ nhà cung cấp hoặc đăng ký có phí.
  - **IP riêng:** **không định tuyến trên Internet Backbone**, router Internet loại bỏ ngay. Có **3 khối**:
    - Lớp A: **10.0.0.0 – 10.255.255.255**.
    - Lớp B: **172.16.0.0 – 172.31.255.255**.
    - Lớp C: **192.168.0.0 – 192.168.255.255**.
  - **NAT** (Network Address Translation): thông dịch địa chỉ riêng thành địa chỉ công cộng khi kết nối Internet.
- **IPv6:** thế hệ mới thay thế IPv4.
  - **2 mục đích:** (1) thay thế nguồn IPv4 cạn kiệt; (2) khắc phục nhược điểm thiết kế của IPv4.
  - Dài **128 bit**, biểu diễn bằng các cụm số **hệ 16 (hexa)** cách nhau bởi **dấu hai chấm (:)**. Có **8 cụm**, mỗi cụm **16 bit**. Mỗi ký số hexa (0–9, A–F) = **4 bit**.
  - Ví dụ dạng chuẩn: 2001:0010:3456:6EFD:00AC:0DEC:DDEE:EEBD.
  - Không gian địa chỉ **2^128**.
  - **Mục tiêu thiết kế IPv6:**
    - Không gian địa chỉ lớn hơn, dễ quản lý.
    - Khôi phục kết nối **đầu cuối – đầu cuối** và **loại bỏ hoàn toàn NAT**.
    - Quản trị TCP/IP dễ hơn: **tự động cấu hình không cần máy chủ DHCP** (DHCP = Dynamic Host Configuration Protocol, dùng trong IPv4).
    - Định tuyến **hoàn toàn phân cấp**.
    - Hỗ trợ tốt hơn **Multicast** (ở IPv4 chỉ là tùy chọn).
    - Hỗ trợ tốt hơn **bảo mật**.
    - Hỗ trợ tốt hơn **di động**.
  - **Rút gọn IPv6:** (1) bỏ các số 0 đứng đầu; (2) thay nhiều nhóm 0 liên tiếp bằng **"::"**. **Dấu "::" chỉ xuất hiện duy nhất một lần.**
    - Ví dụ: ADBF:0000:0000:0000:0000:000A:00AB:0ACD → cách 1: ADBF:0:0:0:0:A:AB:ACD → cách 2: **ADBF::A:AB:ACD**.
- **Tên miền (Domain Name):** nhận dạng vị trí máy tính bằng **tên tương ứng với địa chỉ IP**, thực hiện qua **DNS** (Domain Name System).
  - Ví dụ: **home.vnn.vn ↔ 203.162.0.12** (trang chủ của VDC).
  - DNS chuyển **tên miền → IP và ngược lại**.
  - Thời đầu, DNS dùng CSDL **tập trung** trong file **hosts.txt** do **NIC** (Network Information Center) ở Mỹ giữ. Nay là **CSDL phân bố (phân tán)**.
  - **ICANN** (the Internet Corporation for Assigned Names and Numbers) quản lý **mức ROOT** và cấp phát tên miền dưới mức cao nhất. Slide ghi có **16** hệ thống máy chủ tên miền mức ROOT.
  - DNS dùng **CSDL phân tán, phân cấp hình cây**. Slide ví DNS như **mô hình quản lý công dân** (tên ↔ số chứng minh thư).
  - **Tên miền gốc (ROOT)** biểu diễn bằng dấu **"."**. Dưới ROOT có **2 loại**:
    - **gTLDs** (generic Top Level Domains): tên miền cấp cao **dùng chung** (.com, .org, .net…).
    - **ccTLDs** (country code Top Level Domains): tên miền cấp cao **mã quốc gia** (.vn, .jp, .kr…).
  - **Máy chủ tên miền (Domain Name Server):** chứa CSDL chuyển đổi giữa tên miền và IP.
- **Hoạt động DNS** (ví dụ truy cập www.google.com):
  1. Máy người dùng gửi yêu cầu tới **máy chủ tên miền cục bộ (ISP DNS Server)**.
  2. Máy chủ cục bộ kiểm tra CSDL của nó. Nếu có thì trả IP về.
  3. Nếu không có, máy chủ cục bộ hỏi **máy chủ mức Root**. Root trả về địa chỉ máy chủ quản lý đuôi **.com**.
  4. Máy chủ cục bộ hỏi máy chủ **.com**, nhận về địa chỉ máy chủ **google.com**.
  5. Máy chủ cục bộ hỏi máy chủ google.com, nhận về IP của www.google.com.
  6. Máy chủ cục bộ chuyển IP này cho máy người dùng.
  7. Máy người dùng mở **phiên kết nối TCP/IP** tới máy chủ web.
- **Cấu tạo tên miền:** các máy cùng tổ chức hoặc lĩnh vực được nhóm vào một **Domain**, chia nhỏ thành **Sub Domain**. Các phần phân cách bằng **dấu chấm**, cấu trúc là **cây phân cấp**.
  - Ví dụ **www.home.vnn.vn**: **www** là tên máy chủ; **home** là tên miền **cấp 3** (Third Level); **vnn** là tên miền **mức 2** (Second Level); **vn** là tên miền **mức cao nhất (ccTLD)**.
- **Quy tắc đặt tên miền:**
  - Đơn giản, gợi nhớ, phù hợp mục đích và phạm vi hoạt động.
  - **Mỗi tên miền tối đa 63 ký tự** (kể cả dấu "."), dùng **a-z, A-Z, 0-9 và "-"**.
  - **Tên miền đầy đủ không vượt quá 255 ký tự.**
  - Việt Nam **cho phép đăng ký tên miền tiếng Việt**.

**2.3. Một số dịch vụ Internet thông dụng**

Các dịch vụ **web, thư điện tử, truyền tệp đều hoạt động theo mô hình Client/Server**.

- **World Wide Web (WWW):** một trong những dịch vụ **phổ biến nhất**. Hoạt động theo mô hình **Khách/Chủ (Client/Server)**.
  - **Máy chủ web** chạy phần mềm **Web server**, lưu trang web, nhận và trả lời yêu cầu.
  - **Máy khách** chạy **trình duyệt** (Internet Explorer, Netscape Navigator, Firefox…).
  - **HTTP** (Hyper Text Transfer Protocol, giao thức truyền tải siêu văn bản) là giao thức cơ bản của WWW, truyền file từ Web server tới trình duyệt. HTTP là **giao thức ứng dụng của bộ TCP/IP**.
  - **URL** = Uniform Resource Locator.
  - **HTTPS** (Hypertext Transfer Protocol Secure) = HTTP + **SSL** (Secure Sockets Layer) hoặc **TLS** (Transport Layer Security), dùng cho giao dịch nhạy cảm. HTTPS do **Netscape Communications** tạo năm **1994** cho **Netscape Navigator**, ban đầu dùng mã hóa **SSL**. Phiên bản hiện hành chỉ định bởi **RFC 2818, tháng 5/2000**.
  - **Trang web** là **tài liệu siêu văn bản**, mã hóa bằng **HTML** (HyperText Markup Language). **Liên kết siêu văn bản (hyperlink) là nền móng của WWW.**
  - **WebSite** là tập hợp các trang web liên quan. Sao chép trang lên Web Server gọi là **tải lên (uploading)**.
  - Mọi Web Server đều chạy được file **.htm/.html**. Mỗi loại phục vụ kiểu file riêng:
    - **IIS** (Microsoft) → .asp, .aspx.
    - **Apache** → .php.
    - **Sun Java System Web Server** → .jsp.
  - **Trình duyệt Web:** phần mềm ứng dụng cài trên **máy trạm**, để duyệt tài liệu siêu văn bản.
- **Thư điện tử:** slide gọi đây là **"dịch vụ thông dụng nhất của Internet"**, cho phép gửi thông điệp tới một người hoặc một nhóm người, có **đính kèm tệp**.
  - **3 ưu điểm:** (1) tốc độ cao, chuyển tải toàn cầu; (2) giá thành thấp; (3) linh hoạt về thời gian.
  - **Hệ thống gồm 2 phần:**
    - **MUA** (Mail User Agent): tương tác trực tiếp với người dùng cuối, giúp **nhận, soạn, lưu, gửi** bản tin.
    - **MTA** (Message Transfer Agent): **định tuyến** bản tin, xử lý để bản tin đến đúng hệ thống đích.
  - Mỗi người dùng phải có **tài khoản**, đăng ký miễn phí hoặc do nhà cung cấp cấp.
  - **Hai khuôn dạng địa chỉ** (thêm một dạng kết hợp):
    - **Địa chỉ miền (DomainBase Address):** dùng nhiều trên **Windows**, là dạng **thông dụng nhất**, cấu trúc **hình cây**, xác định **địa chỉ đích tuyệt đối**.
    - **UUCP** (Unix to Unix Copy Command): dùng nhiều trên **Unix**.
    - **Địa chỉ hỗn hợp:** kết hợp hai dạng trên.
  - Khuôn dạng địa chỉ miền: **Thông_tin_người_dùng@thông_tin_tên_miền**. Ví dụ tuxa@neu.edu.vn.
  - **Cấu trúc bản tin:**
    - **Header** (đầu bản tin): MUA dùng địa chỉ trong header để phân bản tin vào đúng hộp thư. Gồm các trường:
      - **To:** người nhận.
      - **From:** người gửi.
      - **Subject:** mô tả ngắn nội dung.
      - **Cc:** người nhận ngoài người nhận chính.
      - **Bcc:** người nhận bí mật, người ở To và Cc không biết.
    - **Body** (thân bản tin): nội dung.
- **Truyền file (FTP – File Transfer Protocol):** chuyển file giữa các máy. Hỗ trợ **mọi dạng file**, cả văn bản **ASCII** (American Standard Code for Information Interchange) lẫn file **nhị phân**. Máy chủ FTP có thể quy định **quyền truy nhập** từng thư mục, file và **giới hạn số người** truy nhập cùng lúc.
- **Chat:** hội thoại trực tiếp trên Internet. Có thể chat **trực tiếp** (Online) hoặc **gián tiếp** (Offline). Hình thức: **text, voice, web-cam**. Có thể chat trên cả **mạng LAN**.
  - **Text chat:** gõ lời nhắn rồi Enter. Ở Việt Nam, **text chat phổ biến**.
  - **Voice chat:** chi phí ít hơn điện thoại nhưng cần **máy mạnh, đường truyền lớn, ổn định**.
  - **Webcam:** thiết bị camera để truyền hình ảnh. Chương trình hỗ trợ: Yahoo! Messenger, MSN Messenger…
  - **2 cách dùng text chat:**
    - **Web chat:** chọn **Nickname** và **chatroom** trên trang web.
    - **Chat client:** phổ biến nhất là **MIRC**. Cần biết **Server chat** (ví dụ irc.saigonnet.vn, chat.fpt.com, irc.vietchat.com) và **Port chat 6667 hoặc 23**. Phòng chat ví dụ: #lobby, #netcenter, #vietchat, #saigonnet.
  - **Chat server:**
    - MIRC: người dùng tự nhập IRC Server.
    - AOL: **login.oscar.aol.com**.
    - ICQ: **login.icq.com**.

### Khái niệm / số liệu / danh sách cần thuộc

**Định nghĩa**
- **Giao thức (Protocol):** "Tập hợp những quy tắc, quy ước truyền thông đó được gọi là giao thức của mạng."
- **Internet (tóm lược):** "một liên mạng máy tính toàn cầu được kết nối từ hàng nghìn mạng máy tính trên khắp thế giới."
- **Hotspot:** "một địa điểm mà tại đó có cung cấp các dịch vụ kết nối không dây và dịch vụ truy cập Internet tốc độ cao, thông qua hoạt động của các thiết bị thu phát không dây (Wireless Access Point)."
- **Băng rộng:** "loại hình kết nối Internet tốc độ cao và luôn trong trạng thái kết nối 24/24."
- **Leased-Line:** "hình thức kết nối trực tiếp giữa các node mạng sử dụng kênh truyền dẫn số liệu thuê riêng".
- **Tên miền:** "sự nhận dạng vị trí của một máy tính trên mạng Internet thông qua tên tương ứng với địa chỉ IP của máy tính đó."
- **Socket** = số hiệu cổng + địa chỉ IP + tên giao thức tầng truyền tải.
- **Địa chỉ mạng** = HostID toàn 0. **Địa chỉ quảng bá** = HostID toàn 1.

**Viết tắt**

| Viết tắt | Đầy đủ |
|---|---|
| DSL / ADSL / RADSL / VDSL | Digital Subscriber Line / Asymmetrical DSL / Rate Adaptive DSL / Very High Bit Rate DSL |
| HDSL / SDSL / IDSL | High Bit Rate DSL / Symmetric DSL / ISDN Digital Subscriber Line |
| Wi-Fi | Wireless Fidelity |
| WLAN | Wireless Local Area Network |
| PDA | Personal Digital Assistant |
| WiMAX | (IEEE 802.16) |
| CSU/DSU | Channel Service Unit / Data Service Unit |
| HDLC | High-level Data Link Control |
| PPP | Point-to-Point Protocol |
| LAPB | Link Access Procedure Balanced |
| NetBEUI | NetBIOS Enhanced User Interface |
| IPX / SPX | Internetwork Packet Exchange / Sequenced Packet Exchange |
| LAN / MAN / WAN | Local / Metropolitan / Wide Area Network |
| OSI | Open System Interconnection (Reference Model) |
| API | Application Programming Interface |
| TCP / UDP / IP | Transmission Control Protocol / User Datagram Protocol / Internet Protocol |
| ICMP / IGMP | Internet Control Message Protocol / Internet Group Management (Message) Protocol |
| ARP / RARP | Address Resolution Protocol / Reverse Address Resolution Protocol |
| FTP / TFTP / NFS | File Transfer Protocol / Trivial FTP / Network File System |
| SNMP / SMTP / LPD | Simple Network Management Protocol / Simple Mail Transfer Protocol / Line Printer Daemon |
| DNS | Domain Name System |
| ISN | Initial Sequence Number |
| IANA | Internet Assigned Numbers Authority |
| NAT | Network Address Translation |
| DHCP | Dynamic Host Configuration Protocol |
| ICANN | Internet Corporation for Assigned Names and Numbers |
| NIC | Network Information Center |
| gTLDs / ccTLDs | generic Top Level Domains / country code Top Level Domains |
| HTTP / HTTPS | Hyper Text Transfer Protocol / Hypertext Transfer Protocol Secure |
| SSL / TLS | Secure Sockets Layer / Transport Layer Security |
| HTML / URL | HyperText Markup Language / Uniform Resource Locator |
| MUA / MTA | Mail User Agent / Message Transfer Agent |
| UUCP | Unix to Unix Copy Command |
| ASCII | American Standard Code for Information Interchange |

**Con số then chốt**

| Nội dung | Con số |
|---|---|
| IPv4 | 32 bit = 4 octet × 8 bit; mỗi octet 0..255; 2^32 = 4.294.967.296 (~4 tỉ) |
| IPv6 | 128 bit = 8 cụm × 16 bit (hexa, dấu ":"); 2^128 địa chỉ |
| IPv6 so với IPv4 | 2^128 / 2^32 = **2^96 lần** (tự suy từ hai con số trên, slide không ghi trực tiếp) |
| Tên miền | mỗi tên tối đa **63** ký tự; tên miền đầy đủ ≤ **255** ký tự |
| Máy chủ ROOT | **16** (theo slide) |
| Dial-up | thực tế khó đạt 56 Kbps; số quay VNN **1260** |
| Băng rộng | ≥ 521 Kbps, ~9 lần dial-up |
| ADSL | 1,5–9 Mbps xuống, 16–640 Kbps lên; ADSL hiện nay 8 / 2 Mbps |
| VDSL | 52 Mbps xuống (cao nhất xDSL) |
| HDSL | 2 cặp cáp, 3.657 m; HDSL-2: 1 cặp cáp, 5.486 m; 668 Kbps – 2,048 Mbps (E1); T1 = 1,544 Mbps |
| SDSL | 1 cặp cáp; 160 Kbps – 1,5 Mbps |
| IDSL | 7.924 m |
| Cable modem | tối đa 2 Mbps |
| Vệ tinh 2 chiều | upstream 1 Mbps, trễ 1 giây |
| Wi-Fi | 802.11: 1–2 Mbps; a: 54; b: 11; g: > 20 Mbps |
| WiMAX | 50 km; 70 Mbps; 60 doanh nghiệp T1; > 1000 người DSL 1 Mbps |
| Leased-line | 256 Kbps – hàng chục Gbps |
| TCP header | 20 bytes; TCP data mặc định 536 byte |
| Port | 2 byte; < 1024 là port danh tiếng (RFC 3232); ≥ 1024 gán động |
| IP header (HLEN) | 20–60 bytes (5–15 từ 32 bit) |
| IP data | tối đa 65.535 bytes (64 KB) |
| Fragment Offset | đơn vị 8 bytes |
| Mã Protocol | TCP = 6, UDP = 17, ICMP = 1, IGMP = 2 |
| Mốc năm | TCP/IPv4: 1981; bản thảo IPv6: 1994; HTTPS: 1994 (Netscape); RFC 2818: 5/2000 |
| Số tầng | TCP/IP: 4; OSI: 7 |

**Phân loại / danh sách**
- **5 phương thức kết nối:** dial-up, băng rộng, vệ tinh, không dây, kênh thuê riêng.
- **DSL bất đối xứng** (dùng chung đường điện thoại): ADSL, RADSL, VDSL. **DSL đối xứng** (không dùng chung): HDSL, SDSL, IDSL.
- **3 loại Internet vệ tinh:** one-way phát đa hướng, phản hồi một chiều, 2 chiều.
- **Giao thức leased-line:** HDLC (chỉ Cisco–Cisco), PPP (chuẩn quốc tế, phổ biến), LAPB (ít dùng).
- **Bộ giao thức:** NetBEUI (Microsoft, không định tuyến), IPX/SPX (Novell, có định tuyến), DECnet (Digital Equipment, có định tuyến), TCP/IP (chuẩn Internet).
- **4 tầng TCP/IP và giao thức:**
  - Ứng dụng: FTP, TFTP, Telnet, SMTP, LPD, NFS, SNMP, DNS, X Window.
  - Giao vận: TCP (có liên kết), UDP (không liên kết).
  - Liên mạng: IP, ICMP, ARP, RARP (văn bản còn nêu IGMP).
  - Truy cập mạng: Ethernet, Fast Ethernet, Token Ring, FDDI.
- **Có liên kết:** TCP. **Không liên kết:** UDP, IP, TFTP (dùng UDP).
- **6 bit điều khiển TCP:** URG, ACK, PSH, RST, SYN, FIN.
- **Lớp IPv4:** A, B, C (gán địa chỉ); D (Multicast); E (Research). Octet đầu: A 1–126, B 128–191, C 192–223.
- **IP riêng:** 10.0.0.0/8 (lớp A), 172.16–172.31 (lớp B), 192.168 (lớp C).
- **gTLDs (bảng slide):**
  - com: thương mại.
  - edu: giáo dục.
  - gov: chính phủ.
  - int: tổ chức quốc tế.
  - mil: quân sự.
  - net: nhà cung cấp dịch vụ web, net.
  - biz: trang thương mại (Business).
  - info: thông tin.
  - org: tổ chức phi chính phủ / phi lợi nhuận.
- **ccTLDs (bảng slide):** at Áo; be Bỉ; ca Canada; fi Phần Lan; fr Pháp; de CHLB Đức; il Israel; it Italia; jp Nhật; vn Việt Nam.
- **Các bước hoạt động DNS:** người dùng → DNS cục bộ (ISP) → Root → máy chủ .com → máy chủ google.com → DNS cục bộ → người dùng → mở kết nối TCP/IP.
- **Các thành phần tên miền** (www.home.vnn.vn): tên máy chủ (www) → cấp 3 (home) → mức 2 (vnn) → mức cao nhất ccTLD (vn).
- **Thư điện tử:** 2 phần MUA/MTA; 3 ưu điểm (tốc độ và toàn cầu, giá thấp, linh hoạt thời gian); 2 khuôn dạng địa chỉ (miền, UUCP) và dạng hỗn hợp; Header (To, From, Subject, Cc, Bcc) và Body.
- **Web server và kiểu file:** IIS → asp/aspx; Apache → php; Sun Java System Web Server → jsp.
- **Chat:** text, voice, webcam; web chat và chat client (MIRC); server AOL login.oscar.aol.com, ICQ login.icq.com.

---

## Bài 3 (slide 2018): Hướng dẫn sử dụng một số dịch vụ Internet thông dụng
> Ghi chú về slide (file `Bai3_HuongDanInternet.pdf`, 119 trang, đánh số trang in 65–183):
> - Các mục được đánh số **4.x** (4.1 Web, 4.2 Thư điện tử, 4.3 Chat), chân trang từ tr.158 ghi `NEU_ICT101_Bai4_...` → giáo trình gốc có thể coi đây là "Bài 4"; khi ôn đối chiếu theo tên bài.
> - Mục tiêu có ghi "Đăng ký thành viên và tham gia **diễn đàn**" nhưng **không có mục hướng dẫn diễn đàn**, chỉ có 1 câu trong phần tóm lược cuối bài.
> - **Không có** nội dung về Telnet, Gopher, WAIS hay các kiểu kết nối Internet (quay số, modem…) → nằm ở bài khác, không có trong file này.
> - Nhiều tên nút chỉ có trong ảnh chụp: nút đính kèm của Yahoo! Mail là **biểu tượng kẹp giấy** (slide không ghi tên chữ, không có chữ "Attach Files"); mục "Tìm kiếm theo phạm vi" (Google Hình ảnh) chỉ có ảnh, không có lời giải thích.
> - Một số lỗi trong slide: ví dụ `site:` ghi "tìm… **ngoại trừ** các trang xuất xứ từ www.technologyreview.com" (mâu thuẫn với định nghĩa `site:` = chỉ tìm trong tên miền đó); Gmail "Thư đã gửi" bị lặp 2 dòng; ví dụ bộ lọc gắn nhãn "Sinh vien" nhưng lại nói xem bằng nhãn "Công việc"; IDM ghi "Tel a Friend" / "Tell a Friend"; tham số Google ghi "relate:" ở mô tả nhưng cú pháp là `related:`; "Instance Message" (đúng: Instant Message); "Mailbox Leanup" (đúng: Mailbox Cleanup); "AotoArchive" (AutoArchive).

### Mục tiêu
- Duyệt web thành thạo.
- Tìm kiếm thông tin trên Internet theo **từ khóa** hoặc theo **chủ đề**.
- Tải các tệp tin từ Internet xuống máy tính.
- Đăng ký tài khoản thư điện tử miễn phí của **Yahoo, Google** và dùng để gửi/nhận thư.
- Sử dụng thành thạo **Microsoft Outlook** để quản lý thư điện tử.
- Thảo luận trực tuyến bằng **Yahoo Messenger, Yahoo! WebMessenger**.
- Đăng ký thành viên và tham gia diễn đàn.

Nội dung bài gồm 3 phần: **Dịch vụ World Wide Web**, **Dịch vụ thư điện tử**, **Dịch vụ chat**.

### Tóm tắt nội dung

#### 4.1. Dịch vụ World Wide Web

**4.1.1. Trình duyệt Web**

*Internet Explorer 9 (IE)*
- Windows Internet Explorer (trước đây Microsoft Internet Explorer, viết tắt **MSIE/IE**), do **Microsoft** phát triển, là thành phần của Windows **từ năm 1995**. Trình duyệt nhiều người dùng nhất **từ 1999**, đỉnh **~95% thị phần năm 2002–2003** (IE5, IE6). Đối thủ đáng kể: **Mozilla Firefox**.
- Phiên bản mới nhất (theo slide): **9.0**, cập nhật miễn phí cho **Windows 7 SP1** và **Windows Vista SP2**.
- **Ưu điểm**: máy nào cũng có; nhiều trang thiết kế cho IE nên hiển thị đẹp nhất. **Nhược điểm**: nạp trang không nhanh; dễ bị mã độc, virus lợi dụng lỗ hổng.
- **Khởi động**: nhấp đúp biểu tượng IE trên màn hình nền, hoặc **Start → Programs → Internet Explorer**. **Đóng**: nút **Close** (góc trên phải) hoặc **Alt + F4**.
- **Các nút lệnh chính** trên thanh công cụ:
  1. **Back**: quay lại trang đã xem trước đó.
  2. **Forward**: chuyển tới trang đã xem sau khi nhấn Back.
  3. **Stop**: ngừng tải nội dung trang đang xem.
  4. **Refresh**: tải lại toàn bộ trang hiện tại (khi trang lỗi hiển thị hoặc muốn cập nhật).
  5. **Home**: hiển thị trang đã chọn làm **trang chủ**; nếu chưa chọn thì hiển thị **trang trắng**.
  6. **Search**: mở cửa sổ **Search Companion**, nhập từ cần tìm → Enter hoặc nút Search; nhấn Search lần nữa để đóng.
  7. **Favorites**: nơi lưu các địa chỉ liên kết đến trang web. Thêm: mở trang → nút **Add** → hộp **Add Favorites** (tên tự động ở ô **Name**, có thể sửa) → **Create in** để chọn/tạo Folder → **OK**. Nhấn Favorites lần nữa để đóng.
  8. **History**: xem lại các trang đã xem trong thời gian qua; nhấn lần nữa để đóng.
  9. **Address**: ô nhập địa chỉ trang web (VD gõ `http://www.neu.edu.vn` rồi Enter).
- **Mở trong cửa sổ/tab mới**: chuột phải vào siêu liên kết → **Open in new window** / **Open in new tab**.
- **Lưu trang web**: **File → Save as…** → chọn nơi lưu ở **Save in**, tên ở **File name**; **Save as type** chọn **Web Page, complete (\*.htm, \*.html)** để lưu toàn bộ nội dung và hình ảnh; **Encoding** chọn **Unicode (UTF-8)** cho trang tiếng Việt (thường tự chọn) → **Save**.
- **In**: xem trước **Tools → Print → Print Preview**; in **Tools → Print → Print**; chọn máy in, in tất cả hoặc **Page Range** → **Print**.
- **Tìm từ trong trang**: **File → Find (on this page)** → nhập vào ô **Find what** → Enter.
- **Tăng/giảm cỡ chữ**: **File → Zoom** → chọn kích thước.
- **Tắt tải ảnh** (tăng tốc): **Tools → Internet Options → thẻ Advanced** → mục **Multimedia** → bỏ chọn tùy chọn hiển thị ảnh → đóng và khởi động lại trình duyệt.
- **Thiết lập trang chủ**: **Tools → Internet Options → tab General** → mục **Home page** nhập địa chỉ; hoặc **Use Current** (trang đang xem), **Use Default** (trang mặc định của Microsoft), **Use Blank** (không chọn trang nào) → **OK**.
- **Thêm trang yêu thích** (như đánh dấu sách; có thể sắp xếp theo chủ đề, nhóm): menu **Favorites → Add to Favorites** → hộp **Add a Favorite** → nhập tên gợi nhớ → **OK**. Mở lại: menu **Favorites** → chọn địa chỉ.
- **History**: danh sách địa chỉ các trang đã thăm, lưu trong khoảng thời gian xác định; mở bằng nút trên thanh công cụ → tab **History** (hiện ở bên phải màn hình).
- **Temporary Internet Files** (IE mặc định lưu trang đã xem vào đây):
  - Xóa: **Tools → Internet Options → tab General → Delete** trong phần **Browsing history**.
  - Di chuyển: tab General → **Settings** (Browsing history) → **Move Folder**.
  - Xem: **View Files** (xem tệp trong thư mục); **View Objects** (xem các file chương trình tải về từ IE).
  - Giới hạn dung lượng: thông số **Disk space to use**.

*Trình duyệt khác* (cách dùng giống IE)
- **Firefox**: miễn phí, phát triển bởi **cộng đồng phi lợi nhuận**; tốc độ và bảo mật cao; mở rộng bằng **Extension**. Ưu: hỗ trợ tốt chuẩn web hiện đại, nhanh hơn IE, an toàn hơn IE (hạn chế **phishing**, mã độc). Nhược: trang thiết kế theo IE hiển thị không tốt; phải cài **Extension/Plug-ins** để xem multimedia. Tải: `http://getfirefox.com` (trang chủ) / `http://www.mozilla.com/en-US/firefox/`.
- **Google Chrome**: miễn phí, của **Google**, dùng nền tảng **V8 engine**; dự án mã nguồn mở đứng sau là **Chromium**. Bản cài tiếng Việt khoảng **555 KB**; nút **Tải xuống Google Chrome** → **Chấp nhận và Cài đặt**; nếu có **Security Warning** → **Run**.
- **Opera**: của **Opera Software**, "trình duyệt dành cho tốc độ"; chức năng **Opera Turbo** tăng tốc khi kết nối chậm (WiFi công cộng, **quay số dial-up**); chặn cửa sổ quảng cáo hữu hiệu. Bản cài khoảng **10 MB**, tại `http://www.opera.com/download/`. Mặc định tự làm trình duyệt mặc định; bỏ chọn ô **Set Opera as default browser** nếu không muốn.
- **Safari**: của **Apple**, cài kèm **Mac OS X**; beta ngày **7/1/2003**; mặc định từ **Mac OS X v10.3**; mặc định trên **iPhone, iPad, iPod touch**. Bản Windows phát hành **11/6/2007** (XP, Vista, 7). Bản ổn định mới nhất (theo slide) **6.0.4 (16/04/2013)**. Tháng 3/2013 Safari đứng **thứ 4** (sau Chrome, IE, Firefox).

**4.1.2. Tìm kiếm thông tin**

*Giới thiệu chung*
- Thông tin trên Internet có thể đúng, sai hoặc chưa đầy đủ → tìm từ **nhiều nguồn** rồi so sánh, tổng hợp.
- Các trang tìm kiếm thông dụng: **Google, Yahoo, AltaVista, Lycos, AllTheWeb**…
- **Từ khóa (Key Words)**: từ đại diện cho thông tin cần tìm. Không rõ ràng → quá nhiều kết quả; **quá dài** → có thể không có kết quả. VD: "vi tính" (quá nhiều), "cách sử dụng máy vi tính" (rất ít/không có), "sử dụng vi tính" (tối ưu hơn).
- Máy tìm kiếm **không** tìm tất cả trang web, chỉ tìm trong **danh sách website chúng lưu trữ** (tự tìm được trước đó hoặc website đăng ký) → mỗi công cụ cho kết quả khác nhau, sắp xếp theo tiêu chí khác nhau. Kết quả thường **10 mục/trang**, kèm mô tả ngắn.
- **Chú ý quan trọng**:
  - **Số ký tự trống giữa các từ không làm thay đổi kết quả tìm kiếm.**
  - **Máy tìm kiếm không phân biệt chữ hoa và chữ thường.**

*Phép toán trong từ khóa* (hầu hết công cụ hỗ trợ)
- **Dấu cộng `+`**: tìm trang chứa **tất cả** các chữ, không theo thứ tự. VD `+Linux +script +tutor`.
- **Dấu trừ `-`**: **loại bỏ** trang chứa chữ/cụm từ đứng ngay sau dấu trừ. VD `+car +hibrid -sale -Prius -Insight`.

*Ký tự đặc biệt*
- **Ngoặc kép `" "`**: tìm **nguyên văn** cụm từ. VD `"cách cài windows xp"`.
- **Dấu ngã `~`** (đặc biệt trong **Google**): tìm cả **từ đồng nghĩa (synonym) tiếng Anh**. VD `~food facts` → cả "nutrition facts"; hữu ích khi tài liệu quá hiếm.

*Tham số tìm kiếm* — kết thúc bằng **dấu hai chấm (:)**; chữ (hoặc cụm từ trong ngoặc kép) **đứng ngay sau** dấu này bị chi phối, các phần khác giữ nguyên nghĩa.

| Giới hạn theo | Công cụ → tham số |
|---|---|
| Tên miền | **AltaVista**: `host:`; **Excite, Google, Yahoo**: `site:`; **AllTheWeb**: `domain:`, `url:`, `site:` (VD `deutch domain:.de`) |
| Tiêu đề | **AltaVista, AllTheWeb, Inktomi (MSN, HotBot)**: `title:`; **Google, Teoma**: `intitle:` và `allintitle:` (allintitle ảnh hưởng **tất cả** chữ sau dấu :) |
| Địa chỉ (URL) | **Google**: `inurl:` (một chữ), `allinurl:` (nhiều chữ); **Inktomi, AOL, GoTo, HotBot**: `originurl:`; **Yahoo**: `u:`; **Excite**: `url:` |
| Liên kết (Link) | **Google, Yahoo**: `link:` (Yahoo yêu cầu địa chỉ có đủ tiền tố `http://`); **MSN**: `linkdomain:` |
| Loại tập tin | `filetype:` đuôi tệp |

- `filetype:` — **Google** hỗ trợ: PDF, Word (.doc), Excel (.xls), PowerPoint (.ppt), Rich Text (.rtf), PostScript (.ps), Text (.txt), HTML (.htm/.html), WordPerfect (.wpd)…; **Yahoo**: HTML, PDF, Excel, PowerPoint, Word, RSS/XML (.xml), .txt; **MSN** chỉ: HTML, PDF, PowerPoint (.pps/.ppt), Word, Excel. VD `laser filetype:pdf`.
- Với công cụ tìm kiếm, **.htm khác .html** → muốn tìm đủ file HTML nên tìm **2 lần**.

*Ký tự thay thế (wildcard)* — 2 loại: **dấu sao `*`** và **dấu chấm hỏi `?`**
- **`*`**: thay cho **một dãy bất kỳ** ký tự (chữ, số, dấu). VD `t*ng` → tướng, từng, tuồng… Khác với `*` trong DOS/Linux/Windows (không giới hạn trong một từ): trong công cụ tìm kiếm `*` **bị giới hạn trong một từ** (VD `my*` không khớp "My Documents" nhưng khớp "mysql.php"). Hỗ trợ: AltaVista, Inktomi (iWon), Northern Light, Gigablast, Google, Yahoo, MSN…
- **`?`**: thay cho **đúng một ký tự**. VD `ph?ng` → phong, ph@ng… nhưng **không** phải phượng, "ph ng", phug. Hỗ trợ: **AOL Search, Inktomi (iWon)**.

*Tìm kiếm với Google* — địa chỉ `https://www.google.com.vn/`
- Giao diện trang chủ: **Mục (1)** ô tìm kiếm (nhập câu điều kiện); **Mục (2)** nút khởi động tìm kiếm; **Mục (3)** nút tìm kiếm và **mở ngay địa chỉ Web đầu tiên** trong danh sách kết quả. (Trong ảnh chụp: nút (2) là "Tìm với Google", nút (3) là nút "…trang đầu tiên tìm được".)
- Thủ thuật Google Search:

| Mục đích | Ký hiệu / tham số | Cú pháp – ví dụ |
|---|---|---|
| Loại bỏ một từ | `-` | `từ khóa - từ loại bỏ`; VD `vi tính-máy` |
| Bắt buộc có một từ | `+` | `từ khóa + từ bắt buộc`; VD `vi tính +máy` |
| Rút gọn từ khóa (đại diện 1, nhiều ký tự hoặc từ khóa quá dài) | `*` | `từ khóa* từ khóa`; VD `máy * tính` → "máy vi tính" |
| Tìm chính xác | `" "` | `"máy tính xách tay"` |
| Theo **tiêu đề** trang | `intitle:` | `intitle:quantrimang` |
| Trong một **tên miền** | `site:` | `vi tính site:quantrimang.com` |
| Trong **địa chỉ URL** | `inurl:` | `inurl:quantrimang` |
| Tìm **tập tin** | `filetype:` | `joomla filetype:pdf` |
| Trang **liên quan** | `related:` | `related:joomla` |
| Trang **không còn hoạt động** (bản lưu của Google) | `cache:` | `cache:www.quantrimang.com` |
| Kết hợp tham số | — | `vi tính filetype:zip site:quantrimang.com` |

- **Google Image Search**: vào `http://www.google.com.vn` → nhấn chữ **Hình ảnh** trên thanh trình đơn → nhập từ khóa → nút **kính lúp màu xanh** hoặc Enter. Kết quả dạng ảnh thu nhỏ (**Thumbnail**); nên chuột phải → mở ảnh trong trang mới.
- **Tìm kiếm nâng cao (hình ảnh)** theo các tiêu chí:
  - **Kích thước**: Mọi kích thước (**Any size**), Lớn (**Large**), Trung bình (**Medium**), Biểu tượng (**Icon** – nhỏ/thumbnail), Lớn hơn (**Larger than** – chọn kích thước trong danh sách thả xuống), Chính xác (**Exactly** – nhập chiều rộng, chiều cao).
  - **Màu sắc**: nhấn vào ô màu → ảnh có màu chủ đạo tương ứng.
  - **Phạm vi** (chỉ có ảnh, slide không giải thích).
  - **Chủ đề**: kết quả được nhóm theo chủ đề liên quan đến từ khóa.
  - **Hiển thị kích thước ảnh**.

**4.1.3. Công cụ tải tập tin từ website**

*Internet Download Manager (IDM)*
- Tăng tốc thông minh: **chia nhỏ gói dữ liệu**, tải nhiều phần an toàn; khác các chương trình khác (chỉ chia khi bắt đầu), IDM **chia nhỏ trong suốt tiến trình download**; kết nối liên tục nhiều lần không cần đăng nhập thêm.
- Cửa sổ chính: danh sách tệp (kích thước, tình trạng, thời gian dự kiến, tốc độ…); sắp xếp bằng cách nhấp tiêu đề cột.
- **Các nút điều khiển**: **Add URL, Start/Resume, Stop, Stop All, Delete, Options, Scheduler, Tell a Friend**.
  - **Add URL**: tải tệp bằng đường dẫn; đánh dấu **Use authorization** để nhập thông tin đăng nhập máy chủ; hợp lệ → hộp **Save as**; mô tả ở **Download Properties**.
  - **Cancel** (hủy), **Pause** (tạm dừng), **Stop All** (dừng tất cả).
  - **Delete**: xóa khỏi danh sách (chỉ khi đã tải xong hoặc đã dừng; chưa xong thì IDM hỏi xác nhận).
  - **Delete Completed**: xóa tất cả tệp đã tải xong (**chỉ có ở bản đã đăng ký**).
  - **Scheduler**: đặt lịch tải.
  - **Tell a Friend**: giới thiệu IDM cho bạn bè.
- **Categories (Danh mục)** bên trái; thư mục định sẵn: **Music, Video, Programs, Documents, Compressed**; IDM tự gợi ý thư mục theo phần mở rộng.
- Tùy biến: phiên bản chuẩn có **4 thanh công cụ** (nút 3D lớn, 3D nhỏ, cổ điển lớn, cổ điển nhỏ); chuột phải thanh công cụ → **Look for new toolbars**, **Customize**; sắp xếp nút/cột bằng **Move Up / Move Down**.
- **Cách bắt đầu tải**:
  - IDM **tự bắt liên kết** trong trình duyệt (IE, MSN Explorer, AOL, Opera, Mozilla, Netscape, Chrome) theo danh sách phần mở rộng (sửa ở **Download → General**). Hộp thoại có nút **Download Later** (thêm vào danh sách, chưa tải) và **Start Download** (tải ngay).
  - Giữ **CTRL** khi nhấp liên kết trong IE để ép IDM tải (tùy chọn "Use ALT key with IE click monitoring"). Nếu IDM lỗi → giữ **Alt** khi nhấp để tải bằng chế độ thường của trình duyệt.
  - IDM nhận URL trong **bộ nhớ tạm (clipboard)** → hiện hộp thoại → **OK**.
  - **Menu chuột phải**: **Download with IDM** / **Download all links with IDM**.
  - Thêm URL bằng tay: nút **Add URL**.
  - **Dòng lệnh**: `idman /s` hoặc `idman /d URL [/p local_path] [/f local_file_name] [/q] [/h] [/n] [/a]`. `/d` tải một tệp; `/s` bắt đầu xếp lịch; `/p` đường dẫn lưu; `/f` tên tệp lưu; `/q` tự đóng khi tải xong (chỉ lần đầu); `/h` **ngắt kết nối** sau khi tải xong; `/n` **chế độ im lặng**; `/a` thêm vào danh sách nhưng không tải. Các tham số /a, /h, /n, /q, /f, /p chỉ dùng kèm `/d URL`.
- **Hộp thoại Options gồm 9 thẻ**: **General, File Types, Connection, Save To, Downloads, Proxy, Site logins, Dial-Up, Sounds**.
  - **General**: tự khởi động, tích hợp trình duyệt, giám sát clipboard; nút **Add Browser…**; module **IEMonitor.exe** giám sát nhấp chuột cho trình duyệt nhân IE; **Advanced browser integration**; nút **Keys** (hộp "Using special keys"). Opera/Mozilla tích hợp qua **plugin** (không hỗ trợ phím đặc biệt).
  - **File Types**: danh sách loại tệp IDM tải; danh sách **"don't start downloading"** cho trang web không muốn tải; dùng `*` thay ký tự (VD `*.tonec.com`).
  - **Connection**: chọn tốc độ kết nối; tránh đặt **Max Connection Number lớn hơn 4**; bảng **Exceptions** cho từng máy chủ (máy chủ FTP giới hạn 1 hoặc 2 kết nối); giới hạn tốc độ (VD **40MB/hour** hoặc không quá **150MB/4 hour**).
  - **Save To**: thư mục mặc định theo loại tệp; **Temporary Directory** (thư mục lưu tạm).
  - **Downloads**: "Don't show" (ẩn Download progress), "Show download complete dialog", "Show minimized", "Show start download dialog", "Start download immediately while displaying Download File Info dialog", "Ignore file modification time changes when resuming a download"; cấu hình chương trình **quét virus** ("Browse", "Command line parameters").
  - **Proxy**: thiết lập máy chủ trung gian; nút **Get from IE** (chép cấu hình proxy từ IE/Netscape); **Use FTP in PASV** = chế độ **thụ động (passive)** của FTP, bật khi mạng sau **tường lửa (firewall)** hoặc proxy.
  - **Site Logins** (chỉ bản đăng ký): danh sách Username/Password cho trang yêu cầu xác thực; nút **New**.
  - **Dial-Up**: dùng dịch vụ **Dial-Up chuẩn của Windows**, chọn kết nối, lưu user/password (**Apply**, **Save Password**), số lần quay số (**0 – vô tận**) và khoảng thời gian giữa các lần.
  - **Sounds**: âm thanh cho sự kiện tải (âm chuẩn Windows ở thư mục `windows/media`; nút **Browse**, **Play**).

*FlashGet*
- Chia nhỏ File để tăng tốc; cho phép **tiếp tục khi bị gián đoạn** mà không phải tải lại từ đầu.
- Tải miễn phí tại `http://www.flashget.com/index_en.html` (hoặc mua CD-ROM); cài bằng **Next**. Chạy độc lập, **mặc định tích hợp vào IE**; trình duyệt khác cần cài thêm tiện ích (Add-ons, Plugin, Extension).
- Thiết lập: **Tools → Options**:
  - Tab **Task Manager → Task Default** → **Download Properties**: mặc định lưu ở **ổ C, thư mục Downloads** (đổi bằng nút **Browser**).
  - **General Setting → General**: bỏ chọn **Launch Flashget on System Startup** để không tự chạy khi khởi động máy.
  - **Download Settings**: **Max task** (số file tải cùng lượt), **Max download speed**.
- Sử dụng qua trình duyệt: nhấn vào file → cửa sổ **Add new download** → **Download**; hoặc chuột phải → **Download by FlashGet3** / **Download all link by FlashGet3**.
- Sử dụng độc lập: nút **New (dấu +)** → nhập địa chỉ ở mục **URL** → **OK**. Nút **Pause**, **Start** (tiếp tục, kể cả sau khi mất mạng/mất điện), **Delete**; thứ tự tải từ trên xuống, đổi bằng **mũi tên lên/xuống**; **Tools → Shut Down PC When Done** (tự tắt máy khi tải xong).
- **Firefox** cần Add-ons **FlashGot**; **Google Chrome** cần Extension **Downloaders**.

*Free YouTube Downloader*
- Tải và lưu video YouTube; **chuyển đổi định dạng** (kể cả tệp trên ổ cứng) để xem trên iPad, iPhone…; nhiều mức chất lượng kể cả **HD**.
- Cách dùng: copy/paste **URL** video vào trường trống → chọn định dạng đầu ra (VD **Windows Media Video**) từ danh sách thả xuống.

#### 4.2. Dịch vụ thư điện tử

**4.2.1. Webmail**

*Gmail*
- Webmail của **Google**, dung lượng **lớn hơn 10 Gigabyte**, hỗ trợ nhiều ngôn ngữ (có tiếng Việt). Tài khoản Gmail đồng thời là tài khoản các ứng dụng trực tuyến khác của Google.
- Cốt lõi: **kỹ thuật tìm kiếm mạnh** của Google → không cần sắp xếp thư; hiển thị thư cùng các trả lời theo **ngữ cảnh cuộc bàn luận**.
- **Đăng ký**: vào `http://mail.google.com` → **"Tạo một tài khoản mới"** → trang **"Tạo tài khoản Google mới"**: **Tên**; **Chọn tên người dùng** (Google kiểm tra đã tồn tại chưa, trùng phải đặt tên khác); **Tạo mật khẩu** (**phải trên 8 ký tự**); **Xác nhận lại mật khẩu**; **Sinh nhật**; **Giới tính** → kéo xuống điền tiếp → tích **"Tôi đồng ý với Điều khoản dịch vụ và Chính sách bảo mật của Google"** → **"Bước tiếp theo"** → có thể **"thêm ảnh tiểu sử"** → **"Bước tiếp theo"**.
- **Đăng nhập**: `http://mail.google.com/` → Tên người dùng + Mật khẩu → **Đăng nhập**.
- **Menu chính**: **Soạn** (tạo, gửi thư mới); **Hộp thư đến** (số trong ngoặc () = số thư **chưa xem**); **Thư gắn dấu sao**; **Thư đã gửi** (bản sao thư đã gửi); **Thư nháp** (thư chưa viết xong/chưa gửi). Nhãn khác: **Tất cả các thư** (kể cả thư lưu trữ), **Spam** (thư rác), **Thùng rác** (thư đã xóa), **Personal** (nhãn Cá nhân).
- **Soạn và gửi thư**: **Soạn** → ô **Tới** → **Thêm Cc** / **Thêm Bcc**; nhiều địa chỉ cách nhau bằng **dấu phẩy (,)** → **Chủ đề** → nội dung → **Đính kèm tệp** (Browse) → **Gửi** / **Lưu bây giờ** (vào Thư nháp) / **Hủy**.
  - **Cc** = "carbon copy" (bản sao): mọi người nhận thấy tên những người trong dòng Cc.
  - **Bcc** = "blind carbon copy" (bản sao ẩn): người nhận Bcc **bị ẩn** với tất cả người nhận khác (kể cả người Bcc khác). Người ở "Đến" thấy mình là người nhận duy nhất; người Bcc biết thư đã gửi tới người ở "Đến".
  - Gmail **không cho gửi file .EXE** và **file ZIP chứa EXE** → nén thành **.rar** hoặc đổi phần mở rộng (VD .abc) và báo người nhận.
- **Đọc thư**: Gmail tự phân loại; "Hộp thư đến (1)" = 1 thư mới chưa đọc → nhấn tiêu đề thư.
- **Đổi mật khẩu**: **"Bảo mật" → "Đổi mật khẩu"** → nhập mật khẩu hiện tại, mật khẩu mới, nhập lại → **"Thay đổi mật khẩu"** → quay về màn hình Cài đặt tài khoản.
- **Chữ ký**: **Cài đặt → Chữ ký** → đánh dấu ô, nhập chữ ký (có thể chứa tên, địa chỉ, SĐT, câu thơ… và hình ảnh) → **Lưu thay đổi**.
- **Tiện ích quản lý thư**:
  - **Gắn dấu sao** (ngôi sao màu vàng): chọn thư → **"Tác vụ khác" → "Thêm dấu sao"**; bỏ: **"Xóa dấu sao"**; xem ở **"Thư gắn dấu sao"** (ngay dưới Hộp thư đến).
  - **Nhãn**: mặc định có **Khác, Theo dõi, Ưu tiên** và **4 nhãn ẩn: Trò chuyện, Tất cả thư, Spam, Thùng rác**; tạo nhãn: **"4 nhãn khác" → "Tạo nhãn mới"** → nhập tên → OK.
  - **Bộ lọc**: chọn thư mẫu → **"Tác vụ khác" → "Lọc thư dựa theo những thư này"** → có **5 điều kiện** lọc → **"Tạo bộ lọc với tìm kiếm này"** → chọn hành động (VD **"Áp dụng nhãn"**, **"Đồng thời áp dụng bộ lọc..."**) → **"Tạo bộ lọc"**. Thư lọc có thể tự gắn sao, gắn nhãn, chuyển vào hộp thư quy định.
  - **Lưu trữ**: chọn thư → **"Lưu trữ"** (thư **không mất, chỉ ẩn**); xem lại: **"Danh sách mở rộng" → "Tất cả thư"**; phục hồi: **"Chuyển tới Hộp thư đến"**.
  - **Thư rác**: chọn thư → **"Báo cáo spam"** → thư từ địa chỉ đó tự vào hộp **Spam**, **tự xóa sau 30 ngày**; bỏ: mở Spam → **"Không phải spam"**.
  - **Xóa**: **"Xóa"** → vào **"Thùng rác"**, **tự xóa sau 30 ngày**; xóa hẳn: trong Thùng rác → **"Xóa vĩnh viễn"** (nút **Chọn** để chọn theo tiêu chí).
- **Tự động trả lời**: **Cài đặt → Tự động trả lời thư** → **Bật tự động trả lời thư** → **Ngày đầu tiên** (mũi tên << >> đổi tháng/năm) → nhập **Chủ đề**, nội dung → (tùy chọn) ô **Kết thúc** + ngày kết thúc → **Lưu thay đổi**.

*Yahoo! Mail*
- Toàn bộ thư, địa chỉ, thông tin lưu trên **máy dịch vụ của Yahoo!** → dùng ở bất cứ đâu có máy tính nối Internet.
- **Đăng ký**: `http://vn.mail.yahoo.com` → **Tạo tài khoản** → đặt **Tên truy nhập** và chọn **tên miền** (VD yahoo.com, **yahoo.com.vn**); tên đã có người dùng → có **gợi ý** tên khác bên dưới → ô **Mật khẩu** và **Đánh lại mật khẩu** (chú ý **độ mạnh yếu** mật khẩu – không bắt buộc nhưng nên đặt mạnh; nhập lại sai thì Yahoo yêu cầu nhập lại) → **"Tạo tài khoản"** → chọn **hai câu hỏi** bảo mật và trả lời → nhập **chuỗi mã hiển thị trong hình** → **Xong** → bảng chúc mừng → **Bắt đầu**.
- **Đăng nhập**: `http://vn.mail.yahoo.com` → **Đăng nhập** → Tên truy nhập + Mật khẩu; trục trặc → **"Tôi không vào được tài khoản của mình"** / **"Trợ giúp về đăng nhập"**.
- **Thư mục chính**: **Thư đến**, **Thư nháp** (thư đang soạn và lưu), **Đã gửi** (bản sao thư đã gửi), **Thư rác** (nút **Xóa hết**), **Thùng rác** (nút **Xóa hết**); nút **Thêm** để tạo thư mục mới. Các thẻ trên cùng (ảnh chụp): **Hộp thư đến, Danh bạ, Lịch**.
- **Gửi thư**: nút **Viết thư** → **Đến** (hoặc nhấn chữ **Đến** để chọn địa chỉ trong **Danh bạ**) → **CC/BCC** (nhiều địa chỉ cách nhau dấu phẩy) → **Chủ đề** (dòng hiển thị trong hộp Thư đến của người nhận) → nội dung → đính kèm bằng **nút biểu tượng kẹp giấy** → **Lưu thư nháp** (nếu chưa xong) → **Gửi** → thông báo **"Thư đã gửi"** → **Viết thư** (thư khác) hoặc **Trở lại hộp thư đến**. Thư bị trả về → nhận thư báo lỗi.
- **Xem thư**: tự kiểm tra khi đăng nhập, hoặc nút **Kiểm tra thư** → **Thư đến** → nhấn **Chủ đề**. Chức năng: **Xóa, Trả lời, Chuyển tiếp** (chuyển thư đến địa chỉ khác), **Thư rác**, **Di chuyển** (sang thư mục khác).
- **Thoát**: **Thoát** (phía trên, bên phải).
- **Đổi mật khẩu**: nhấp tên đăng nhập trong lời chào **"Xin chào, …"** (góc trên phải) → **Thông tin tài khoản** → xác nhận mật khẩu → **Đăng nhập** → mục **"Đăng nhập và Bảo mật"** → **Đổi mật khẩu của bạn** → mật khẩu hiện tại / mới / xác nhận → **Lưu**.
  - **Mật khẩu Yahoo phân biệt chữ hoa, chữ thường và dài ít nhất 6 ký tự.**
  - Mật khẩu Yahoo! có hiệu lực cho **toàn bộ tài khoản Yahoo!** (Mail, Messenger, các trang khác).

**4.2.2. Microsoft Outlook (2007)**

*Cấu hình nhận thư Gmail bằng Outlook*
- Trên Gmail: **Cài đặt (Settings) → Chuyển tiếp và POP/IMAP (Forward and Pop/Imap)** → chọn **Enable POP for all mail** (bật POP cho tất cả thư) hoặc **Enable POP for mail that arrives from now on** (chỉ thư đến từ nay) và **Enable IMAP** (IMAP = chế độ **vẫn lưu thư trên máy chủ**) → **Save Changes**.
- Trên Outlook: **Start → All Programs → Microsoft Office → Microsoft Office Outlook 2007**. Lần đầu → hộp **"Account Configuration"** → **Yes** → **Next**. Không phải lần đầu → **Tools → Account Settings** → tab **E-mail** → **New…** → trang **Add New E-mail Account** nhập thông tin (**không** chọn "Manually configure server settings or additional server types") → **Next** → **Finish**.

*Giao diện Outlook 2007*
- Giao diện mới tên **Ribbon** (soạn thảo dựa trên **Word 2007**): **Tabs** (VD tab **Message**) → **Groups** (VD nhóm **Basic Text**) → hộp **Font**.
- **Thanh công cụ mini**: tô khối văn bản → chuột phải → thanh hiện chìm, trỏ vào thì nổi lên.
- Phím tắt: bắt đầu bằng **Alt** hoặc **Ctrl**; VD **Alt + F** (mở nút File), **Ctrl + N** (email mới).
- **Calendar**: tab **Day, Week, Month**; nút quay lại/chuyển tiếp; **Tasks** theo dõi ghi chú (gắn cờ, tô màu).
- **Contacts**: lưu trữ thông tin đối tác để dễ tìm kiếm.

*Thao tác cơ bản*
- **Tạo email mới** (3 cách): biểu tượng **New Mail Message**; **File → New → Mail Message**; **Ctrl + N**. Điền **To**, **Subject**, nội dung → **Send**.
- Gửi cho nhiều người: ghi thêm địa chỉ vào hộp **CC**.
- **Chữ ký**: nút **Signature → Signatures** → **New** → nhập tên tiêu đề chữ ký → OK → nhập/trang trí (Font, màu…). Chữ ký đầu tiên tạo ra được Outlook **mặc định áp dụng cho mọi thư mới**. Chữ ký gồm thường: **tên, chuyên môn, địa chỉ và số điện thoại** (có thể thêm website, logo, ảnh – nhưng ảnh làm chậm gửi, nên dung lượng nhỏ).
- **Trả lời**: nút **Reply** (form mới ghi sẵn địa chỉ người gửi) → **Send**.
- **Thêm Contact**: nút **Contacts** trong **Navigation Pane** → **New** → form **New Contact** → **Save and Close**.
- **Đính kèm file**: To → Subject → biểu tượng **Attach File** → chọn file → **Insert** hoặc Enter → **Send**.
- **Chèn hình**: **Insert → Picture**; chọn hình để hiện công cụ chỉnh sửa.
- **Xem trước file đính kèm** trước khi mở/lưu (an toàn, tránh mã độc) trong cửa sổ đọc.
- **Tạo nhiệm vụ (Task)**: nút **Tasks** (Navigation Bar) → nhấp **Type a New Task** → gõ tên → **Enter**.
- **To-Do Bar** (tính năng mới của Outlook 2007): tập hợp việc cần làm gồm **các tác vụ đã nhập, vài cuộc hẹn kế tiếp, email đã gắn cờ**.
- **Gắn cờ**: chuột phải tiêu đề email → **Follow Up** → chọn màu cờ (hoặc chuột phải vào lá cờ mờ bên phải tiêu đề).
- **Đánh dấu nhiệm vụ hoàn tất**: **Tasks** (hoặc **Ctrl + 4**) → **Simple List** trong **Current View** → đánh dấu hộp ở **cột thứ hai từ trái** → tên đổi màu và bị **gạch ngang**.
- **Tô màu email** (VD thư sếp màu đỏ): **Tools → Organize** → hộp **Ways to Organize Outlook** → **Using Colors** → **Color message** chọn **From** → nhập địa chỉ → chọn màu → **Apply Color**.
- **Thẻ màu Categories**: chuột phải tiêu đề → **Categorize** → chọn màu.
- **Tạo thư mục**: chuột phải **INBOX** → **New Folder** → đặt tên → OK. Di chuyển thư: **kéo thả**, hoặc chuột phải → **Move To Folder** → chọn thư mục → OK. "Xóa" thư mục khỏi danh sách: chuột phải → **Remove from Favorite Folders** (chỉ **ẩn**, vẫn còn trong Inbox).
- **Tìm email nhanh**: công cụ **Instant Search** (nhập địa chỉ email hoặc từ trong nội dung).

*Kích thước hộp thư*
- VD giới hạn: **90 MB** cảnh báo; **100 MB** không gửi được; **110 MB** không nhận được. Outlook đặt giới hạn **20 GB**.
- Xem dung lượng: **Folder Sizes**; đơn vị thường là **KB**; **1024 KB = 1 MB; 1024 MB = 1 GB**.
- Kích cỡ trung bình một email **khoảng 30 KB**; giới hạn hộp thư do **quản trị hệ thống máy chủ** đặt, **không đổi được trong Outlook**.
- **Tools → Mailbox Cleanup**: xem dung lượng các thư mục.
- **Lưu file đính kèm ra đĩa**: mở email → biểu tượng **Microsoft (Office)** → **Save As** → **Save attachments** → chọn đường dẫn → OK.
- **Xóa vĩnh viễn**: thư xóa vào **Deleted Items**; vào Deleted Items → chọn → chuột phải **Delete**; hoặc chuột phải thư mục Deleted Items → **Empty Deleted Items Folder** → OK.
- **Junk Mail**: lọc và chứa **thư rác (Spam)** như thư quảng cáo.

*Lưu trữ*
- **AutoArchive**: email tự chuyển vào **thư mục tự lưu trữ**; thư mục con tự tạo.
- **Thư mục cá nhân (Personal Folders)**: **File → New → Outlook Data File → Office Outlook Personal Folders (.pst)** → OK. Tạo thư mục con: chuột phải **Personal Folders → New Folder**. Di chuyển: **Move to Folder** hoặc kéo thả.
- **Lưu email ra ổ đĩa (backup)**: công cụ **Import and Export** trong trình đơn **File** (dùng khi muốn sao lưu **toàn bộ** hộp thư).

*Electronic Business Card*
- Tạo từ thông tin liên lạc của chính mình (có thể tạo nhiều card cho nhiều vai trò).
- Hộp thoại **Fields**: **Add** (thêm), **Remove** (xóa); **Move Field Up / Move Field Down** (đổi vị trí); **Edit Business Card** để chỉnh/trang trí.
- Gửi kèm: trong email mới → **Business Card → Other Business Card** → chọn card → đính kèm dạng file **.vcf** (định dạng **vCard** – tiêu chuẩn tạo, chia sẻ danh thiếp ảo trên Internet).
- Có thể chèn card vào **chữ ký** (hiển thị kích thước khác 100%). Muốn sửa card: xóa file .vcf (hoặc thẻ trong chữ ký) → quay lại **Contacts** để sửa.
- Tạo khoảng trắng: di chuyển trường **Blank Line** lên/xuống.

#### 4.3. Dịch vụ chat

**4.3.1. Instant Message – Yahoo! Messenger (YM)**
- Cho phép **Chat** (tán gẫu), **Instant message** (tin nhắn nhanh), **SMS**, **Video Call**, **PC Calls**… **Miễn phí**; bản tiếng Việt cho Windows tải tại `http://vn.messenger.yahoo.com/`.
- **Cài đặt**: nhấp đúp tệp → cảnh báo nhấn **Run** → **Tiếp** → đánh dấu chấp nhận điều khoản → **Tiếp** → **Cài đặt** (máy phải nối Internet) → **Hoàn tất**.
- **Tài khoản**: tài khoản YM **chính là** tài khoản Yahoo! Mail (và ngược lại). Tạo mới: dòng **"Đăng ký tài khoản Yahoo!..."**. **Tên truy nhập = phần đầu của địa chỉ Yahoo! Mail** (VD `abc@yahoo.com` → `abc`).
- **Tùy chọn đăng nhập**: **Nhớ tên truy nhập và mật khẩu** (chỉ dùng trên máy riêng); **Đăng nhập tự động**; **Đăng nhập ẩn** (người khác không biết bạn đang trực tuyến) → nút **Đăng nhập**.
- **Thoát**: menu **Messenger → Thoát** (Sign Out, Offline) → **Có** → thoát lần nữa để đóng chương trình. Chọn **Đóng** thì chỉ đóng cửa sổ, **không thoát tài khoản** (mở lại bằng biểu tượng YM ở **khay hệ thống**, góc dưới phải).
- **Thêm bạn**: nút **Thêm bạn** (**dấu +**, dưới menu **Danh Bạ**) → cửa sổ **Thêm vào danh sách Messenger**: nhập Tên truy nhập YM hoặc địa chỉ Yahoo! Mail; mạng chọn **Yahoo! Messenger**; số di động theo cú pháp **+[mã quốc gia][số điện thoại]** (VD 0911111111 → **+84911111111**, **84** là mã Việt Nam, **bỏ số 0 đầu**) → **Tiếp** → chọn nhóm (mặc định **Bạn bè**), lời giới thiệu, nút **Thay đổi** (tên hiển thị) → **Tiếp** → YM thêm vào **danh sách Messenger và Sổ địa chỉ**, gửi tin nhắn xin phép → **Hoàn tất** (phải chờ người kia đồng ý).
- **Nhận yêu cầu kết bạn**: **Chấp nhận**, **Từ chối**, hoặc **Bỏ qua**.
- **Xóa bạn**: chuột phải tên → **Xóa** → (tùy chọn) ô **"Và xóa khỏi Sổ địa chỉ"** → **Có**.
- **Chú ý**: thêm tên ai vào danh bạ **phải được người đó đồng ý** (và ngược lại); xóa ai khỏi danh bạ của mình thì tên mình **vẫn còn** trong danh bạ của họ và họ **vẫn nhắn tin được**.
- **Phòng chat**: gia nhập hoặc tạo **Phòng tán gẫu (Chat Room)**.
- **Gọi thoại (Voice chat/Voice call)**: cần máy nối Internet, cài YM, có **Micro** và **loa/tai nghe (Headphone)**; người được gọi phải có trong danh bạ. Khi bạn **Online**, tên sáng lên → chuột phải → **Gọi thoại**. Trong cuộc gọi: nút **Chờ** (tạm ngưng), **Kết thúc**; vẫn nhắn tin được bằng bàn phím.
- **Nhận cuộc gọi**: 3 lựa chọn **Chấp nhận / Từ chối / Chỉ nhận tin nhắn**. Lần đầu dùng → chương trình **Hỗ trợ cài đặt cuộc gọi** (kiểm tra Micro → **Tiếp** → loa → **Tiếp** → Webcam → **Hoàn tất**); chỉnh âm bằng **Volume Control**. Chi phí: chỉ phí **kết nối Internet**; mạng chậm thì tiếng không rõ, hay ngắt.

**4.3.2. Webchat** (chat trực tiếp từ website, **không cần cài phần mềm**)
- **Yahoo! WebMessenger** (Messenger trong Yahoo! Mail): chat cả với bạn trên **Facebook** và **Windows Live**, không cần cài đặt.
  - Gửi tin cho liên lạc đã có: nhấp **hình tam giác** bên trái chữ **Messenger** → danh sách liên lạc online → nhấp liên lạc → nhập tin → **Enter**. Nếu đã đăng xuất, nhấp **biểu tượng tia sét** cạnh "Messenger" để đăng nhập.
  - Gửi cho người **chưa có trong Sổ địa chỉ**: cạnh nút **"Compose"** nhấp mũi tên xuống → **Instant Message** → nhập tên truy nhập hoặc email → Enter → nhập tin → Enter.
  - Mặc định Messenger trong Yahoo! Mail **được bật** khi đăng nhập Mail; Yahoo! Mail **lưu trạng thái** Messenger (lần trước Offline thì lần sau vẫn Offline).
  - Đăng xuất: nhấp **hình tia sét màu vàng** bên phải chữ Messenger (cột trái).
- **eBuddy**: hỗ trợ tiếng Việt, `http://www.ebuddy.com`.
- **KoolIM**: `www.koolim.com`, **chưa hỗ trợ giao diện tiếng Việt**, có **tiện ích Firefox**.

#### Tóm lược cuối bài
- Mỗi sinh viên cần đăng ký tài khoản thư điện tử (phổ biến nhất: miễn phí của **Google** và **Yahoo**); một thư gửi được cho nhiều người (**CC** hoặc **BCC**) và đính kèm file.
- **Dịch vụ truyền tệp** cho phép tải dữ liệu từ Internet xuống máy (VD phần mềm miễn phí).
- **Dịch vụ chat** cho phép thảo luận trực tuyến; phổ biến nhất là **Yahoo Messenger**.
- **Dịch vụ diễn đàn** cho phép thảo luận nội dung quan tâm; **muốn tham gia phải đăng ký thành viên**.

### Khái niệm / thao tác / danh sách cần thuộc

**Con số & quy tắc**
- IE thành phần Windows từ **1995**; nhiều người dùng nhất từ **1999**; ~**95%** thị phần **2002–2003** (IE5, IE6); bản mới nhất **9.0**.
- Chrome: **V8 engine**, mã nguồn mở **Chromium**, bản cài ~**555 KB**. Opera ~**10 MB**, **Opera Turbo**. Safari: beta **7/1/2003**, bản Windows **11/6/2007**, thứ **4** (3/2013).
- Tìm kiếm: **số ký tự trống không ảnh hưởng**; **không phân biệt hoa/thường**; kết quả **10 mục/trang**; `.htm` ≠ `.html` → tìm 2 lần.
- `*` = dãy ký tự bất kỳ (trong giới hạn một từ); `?` = **đúng một** ký tự.
- **Gmail**: dung lượng > **10 GB**; mật khẩu **trên 8 ký tự**; không gửi **.EXE** (và ZIP chứa EXE); Spam và Thùng rác tự xóa sau **30 ngày**; **4 nhãn ẩn** (Trò chuyện, Tất cả thư, Spam, Thùng rác); bộ lọc có **5 điều kiện**.
- **Yahoo**: mật khẩu **phân biệt hoa/thường, ít nhất 6 ký tự**; đăng ký cần **2 câu hỏi bảo mật** + **mã trong hình**; một mật khẩu dùng cho **toàn bộ** dịch vụ Yahoo!.
- **YM**: tên truy nhập = phần trước `@`; SĐT dạng **+84** + số bỏ 0 đầu.
- **IDM**: Options có **9 thẻ**; **Max Connection Number ≤ 4**; **4 kiểu thanh công cụ**; 5 danh mục mặc định (Music, Video, Programs, Documents, Compressed).
- **Outlook**: giới hạn **20 GB**; ví dụ **90/100/110 MB** (cảnh báo/không gửi/không nhận); email trung bình **~30 KB**; **1024 KB = 1 MB, 1024 MB = 1 GB**; **Ctrl + N** thư mới, **Ctrl + 4** Tasks; Business Card dạng **.vcf (vCard)**; Personal Folders dạng **.pst**.

**Nút IE (9 nút)**: Back – Forward – Stop – Refresh – **Home** (trang chủ; chưa đặt thì trang trắng) – Search (Search Companion) – Favorites – History – Address.

**Đường dẫn menu IE**
- Trang chủ: Tools → Internet Options → General → Home page (**Use Current / Use Default / Use Blank**).
- Tắt ảnh: Tools → Internet Options → **Advanced** → Multimedia.
- Xóa file tạm: Tools → Internet Options → General → Browsing history → **Delete**; **Settings → Move Folder / View Files / View Objects / Disk space to use**.
- Lưu trang: File → Save as → **Web Page, complete**; Encoding **UTF-8**.
- In: Tools → Print → **Print Preview** / **Print**. Tìm trong trang: **Find (on this page)** → ô **Find what**. Zoom: File → Zoom.

**Phím tắt**
| Trình duyệt | Phím tắt |
|---|---|
| IE | **Alt** hiện thanh menu; **Alt+M** về trang chủ; **Alt+C** xem lịch sử, Feed, Favorites; **Ctrl+J** xem file tải xuống; **Ctrl+L** chuyển sang địa chỉ mới; **Ctrl+D** đánh dấu trang yêu thích; **Ctrl+B** tìm mục yêu thích; **Ctrl+T** tab mới; **F5** tải lại; **Ctrl+F4** đóng tab; **Alt+F4** đóng IE |
| Firefox | **Alt+D** con trỏ lên thanh địa chỉ; **Alt+Home** về trang chủ; **Ctrl+-/Ctrl++** thu/phóng; **Ctrl+S** ghi trang; **Ctrl+n** tới tab thứ n; **Alt+Shift+Delete** xóa dữ liệu cá nhân; **Ctrl+N** cửa sổ mới; **Alt+<** về trang trước; **Ctrl+F4** đóng tab |
| Chrome | **Ctrl++/Ctrl+-** phóng/thu cỡ chữ; **Ctrl+0** cỡ chữ chuẩn; **Ctrl+U** xem nguồn trang; **Ctrl+F5** reload nhanh hơn; **Ctrl+H** lịch sử; **Ctrl+Tab** tab kế; **Ctrl+T** tab mới; **Ctrl+P** in; **Alt+Home** trang chủ |

**Công cụ tìm kiếm ↔ tham số** (xem bảng ở trên): `host:` (AltaVista); `site:` (Excite, Google, Yahoo); `domain:` (AllTheWeb); `title:` (AltaVista, AllTheWeb, Inktomi); `intitle:/allintitle:` (Google, Teoma); `inurl:/allinurl:` (Google); `originurl:` (Inktomi, AOL, GoTo, HotBot); `u:` (Yahoo); `url:` (Excite); `link:` (Google, Yahoo); `linkdomain:` (MSN); `~` đồng nghĩa (Google); `related:`, `cache:` (Google).

**Google tìm kiếm hình ảnh nâng cao** — tiêu chí: **Kích thước** (Any size, Large, Medium, Icon, Larger than, Exactly), **Màu sắc**, **Phạm vi**, **Chủ đề**, hiển thị kích thước ảnh.

**Phần mềm theo nhóm**
- Trình duyệt: **Internet Explorer, Firefox, Google Chrome, Opera, Safari**.
- Máy tìm kiếm: **Google, Yahoo, AltaVista, Lycos, AllTheWeb** (ngoài ra trong bảng tham số: Excite, Teoma, Inktomi/HotBot/MSN, AOL, GoTo, Northern Light, Gigablast, iWon).
- Tải tệp: **Internet Download Manager (IDM), FlashGet, Free YouTube Downloader** (FlashGot = Add-on Firefox cho FlashGet; Downloaders = Extension Chrome cho FlashGet).
- Webmail: **Gmail, Yahoo! Mail**. Phần mềm thư trên máy: **Microsoft Outlook 2007**.
- Chat cài đặt: **Yahoo! Messenger**. Webchat: **Yahoo! WebMessenger, eBuddy, KoolIM**.

**Tên nút/chức năng hay hỏi**
- Gmail: **Soạn**, **Tới / Thêm Cc / Thêm Bcc**, **Chủ đề**, **Đính kèm tệp**, **Gửi / Lưu bây giờ / Hủy**, **Tác vụ khác**, **Lưu trữ**, **Báo cáo spam / Không phải spam**, **Xóa vĩnh viễn**, **Cài đặt → Chữ ký / Tự động trả lời thư**, **Bảo mật → Đổi mật khẩu**.
- Yahoo! Mail: **Tạo tài khoản**, **Đánh lại mật khẩu**, **Viết thư**, **Đến** (chọn từ **Danh bạ**), **CC/BCC**, **Chủ đề**, nút **kẹp giấy** (đính kèm), **Lưu thư nháp**, **Gửi**, **Kiểm tra thư**, **Chuyển tiếp**, **Di chuyển**, **Xóa hết** (Thư rác, Thùng rác), **Thêm** (thư mục), **Thoát**, **Thông tin tài khoản → Đổi mật khẩu của bạn**.
- YM: **Thêm bạn (+)**, **Sổ địa chỉ** / Danh bạ, **Đăng nhập ẩn**, **Gọi thoại**, **Chờ / Kết thúc**, **Chấp nhận / Từ chối / Bỏ qua / Chỉ nhận tin nhắn**, **Phòng tán gẫu (Chat Room)**.
- Outlook: **New Mail Message**, **Attach File**, **Reply**, **Send**, **Signature**, **Follow Up**, **Categorize**, **Move To Folder**, **Instant Search**, **Mailbox Cleanup**, **Empty Deleted Items Folder**, **Junk Mail**, **AutoArchive**, **Import and Export**, **Ways to Organize Outlook → Using Colors → Apply Color**.
- IDM: **Add URL, Start/Resume, Stop, Stop All, Delete, Delete Completed, Options, Scheduler, Tell a Friend, Download Later, Start Download, Download with IDM**.
- FlashGet: **New (+), Pause, Start, Delete, Add new download, Download by FlashGet3, Shut Down PC When Done, Max task, Max download speed**.

**Phân biệt dễ nhầm**
- **Cc** (người nhận khác **thấy**) vs **Bcc** (người nhận khác **không thấy**).
- **POP** (tải thư về) vs **IMAP** (vẫn **lưu thư trên máy chủ**).
- Gmail **Lưu trữ** (ẩn, không mất) vs **Xóa** (vào Thùng rác, 30 ngày) vs **Xóa vĩnh viễn**.
- YM **Đóng** (vẫn đăng nhập, ở khay hệ thống) vs **Thoát** (đăng xuất).
- IE **Favorites** (địa chỉ tự lưu để xem lại) vs **History** (trang đã thăm tự ghi lại).
- `intitle:` (tiêu đề) vs `inurl:` (địa chỉ) vs `site:` (tên miền) vs `filetype:` (loại tệp) vs `related:` (liên quan) vs `cache:` (trang ngưng hoạt động).

---

## Bài 4 (slide 2018): Mô hình hệ thống E-learning

> Nguồn: `Bai4_MoHinhElearning.pdf` (21 trang, đánh số trang sách 45–65). Lưu ý: tiêu đề là "Bài 4" nhưng các mục bên trong đánh số **3.x** (3.1, 3.2, Hình 3.1–3.5), nên đề có thể trích "Hình 3.5" v.v.

### Mục tiêu

Theo slide, sau bài này sinh viên cần:
- Hiểu rõ **chức năng chính của các thành phần** trong mô hình chức năng hệ thống e-learning.
- Hiểu rõ **cấu trúc và hoạt động** của hệ thống e-learning.
- Trình bày được **các chuẩn và đặc tả** cho hệ thống e-learning.
- Đánh giá được **ưu điểm, nhược điểm** của hệ thống e-learning.

Nội dung bài gồm 2 phần: (1) Mô hình chức năng hệ thống e-learning; (2) Mô hình hệ thống e-learning.

Hướng dẫn học (đầu bài): học đúng lịch trình theo tuần, làm đủ bài luyện tập, tham gia thảo luận trên diễn đàn; làm việc nhóm, trao đổi với giảng viên tại lớp hoặc qua email; tham khảo trang Web môn học.

### Tóm tắt nội dung

**3.1. Mô hình chức năng hệ thống**
- **ADL** (Viện nghiên cứu công nghệ giáo dục từ xa) đưa ra **SCORM** (Sharable Content Object Reference Model – mô hình tham chiếu đối tượng nội dung chia sẻ), định nghĩa môi trường e-learning là một kiểu **LMS**.
- SCORM không mô tả chi tiết các khối chức năng của LMS, chỉ tập trung vào chức năng **phân phối và theo dõi** nội dung học.
- SCORM định nghĩa **2 phân hệ**: **LCMS** (hệ thống quản lý nội dung học tập) và **LMS** (hệ thống quản lý học tập).
- Hình 3.1 (mô hình chức năng): 3 tác nhân là **Chuyên viên phát triển nội dung** (làm việc với LCMS), **Giảng viên** (với LMS), **Sinh viên**.
  - Khối LCMS: Công cụ thiết kế & tích hợp nội dung; Quản lý nội dung học tập; Ngân hàng nội dung; Công cụ theo dõi học tập.
  - Khối LMS: Công cụ cho giảng viên; Quản lý khóa học; Quản lý hồ sơ; CSDL người dùng; Công cụ truy nhập & đánh giá; Quản lý đăng nhập.
- **LCMS (3.1.1)**: môi trường **đa người dùng**, nơi các cơ sở phát triển nội dung **tạo ra, lưu trữ, sử dụng lại, quản lý và phân phối** nội dung học tập từ một **kho dữ liệu trung tâm**; cho phép tạo và tái sử dụng đơn vị nội dung nhỏ. Để tương hợp (interoperability), LCMS phù hợp các tiêu chuẩn về **siêu dữ liệu nội dung, đóng gói nội dung, truyền thông nội dung**.
- **LMS (3.1.2)**: hệ thống dịch vụ quản lý việc **phân phối và tìm kiếm** nội dung học tập cho người học → LMS **quản lý các quá trình học tập**. LMS trao đổi hồ sơ, thông tin đăng nhập với hệ thống khác; lấy vị trí khóa học và hoạt động của sinh viên từ LCMS.
- Yêu cầu của một LMS điển hình chia 5 nhóm: (1) chung, (2) kỹ thuật, (3) điều khiển truy nhập & bảo mật, (4) giao diện người dùng, (5) chức năng (chung; đăng ký–giám sát; báo cáo; chuẩn hóa e-learning; quản lý chương trình giảng dạy; kiểm tra) — chi tiết ở phần dưới.
- **Dịch vụ Web** phù hợp để liên kết/tương hợp các hệ thống e-learning vì: thông tin trao đổi (LOM, đóng gói IMS) tuân thủ **XML**; kiến trúc Web là nền tảng, **độc lập ngôn ngữ**; cho phép dùng cả Intranet và Internet công cộng (lựa chọn công nghệ mạng "trong suốt").
- Các hệ thống trao đổi bản tin qua tương tác của các **tác nhân (agent) dịch vụ Web**. *Nhà cung cấp dịch vụ người dùng* = đơn vị cung cấp hạ tầng máy chủ; *Nhà cung cấp nội dung* = các cơ sở đào tạo.

**3.2. Mô hình hệ thống e-learning**
- **3.2.1.** Hệ thống e-learning gồm **3 phần chính**: hạ tầng truyền thông & mạng; hạ tầng phần mềm; nội dung đào tạo (hạ tầng thông tin – phần **quan trọng**). Hình 3.2, 3.3 minh họa thành phần và mạng trung tâm; có bảng chức năng các thiết bị (Web/Database/Content/Mail Server, Tape Backup, Router, Firewall, Switch, Load Balancing).
- Phát triển e-learning tốn **chi phí rất lớn giai đoạn đầu** (hạ tầng phần cứng, phần mềm LMS/LCMS, phát triển nội dung, đội ngũ…).
- Cần tuân theo chuẩn để có 4 khả năng: tương hợp, tái sử dụng, quản lý, truy nhập.
- **3.2.2. Chuẩn và đặc tả**: là thành phần **kết nối** tất cả các thành phần (LMS, LCMS, công cụ soạn bài, kho bài giảng hiểu và tương tác nhau qua chuẩn). 4 nhóm chuẩn: đóng gói, trao đổi thông tin, metadata, chất lượng.
- **3.2.3. Hoạt động của hệ thống** (Hình 3.4 – cấu trúc điển hình): các thành phần Giảng viên (A), Sinh viên/Học viên (B), Phòng biên tập–xây dựng chương trình (C), Phòng quản lý đào tạo (D), Cổng thông tin người dùng, LCMS (1), LMS (2), Công cụ hỗ trợ học tập (3), Công cụ thiết kế bài giảng (4), Ngân hàng kiến thức (I), Ngân hàng bài giảng điện tử (II).
- **Quy trình học tập e-learning của sinh viên: 3 bước** (Hình 3.5).
- **3.2.4. Các đặc điểm** của e-learning (8 đặc điểm), phân loại lớp học của Sloan Consortium, ưu/nhược điểm theo quan điểm cơ sở đào tạo và người học.

### Khái niệm / số liệu / danh sách cần thuộc

#### A. Quy trình học tập e-learning của sinh viên – 3 bước ⭐⭐⭐ (Hình 3.5)
1. **Bước 1: Đăng ký học tập**
2. **Bước 2: Tìm hiểu thông tin lớp học**
3. **Bước 3: Học tập**, gồm (theo hình):
   - Tiếp thu bài giảng
   - Tương tác (Phụ đạo – Trao đổi với bạn)
   - Luyện tập
   - Kiểm tra và Thi kết thúc môn học

#### B. Đặc điểm của hệ thống e-learning – 8 đặc điểm ⭐⭐⭐
Bản chất: e-learning cũng là một hình thức **đào tạo từ xa**.
1. **Học mọi lúc, mọi nơi** – Internet xóa khoảng cách thời gian, không gian.
2. **Học liệu hấp dẫn** – multimedia (text, hình ảnh, âm thanh), có thể **tương tác** với bài học → tăng khả năng nắm bắt kiến thức.
3. **Linh hoạt về khối lượng kiến thức cần tiếp thu** – phục vụ theo nhu cầu, không bám thời gian biểu cố định; người học tự điều chỉnh quá trình học.
4. **Nội dung thay đổi phù hợp cho từng cá nhân** – chọn đơn vị tri thức theo trình độ và điều kiện truy nhập mạng.
5. **Cập nhật mới nhanh**.
6. **Học có sự hợp tác, phối hợp** – trao đổi giữa sinh viên với nhau và với giảng viên qua mạng.
7. **Tiến trình học được theo dõi chặt chẽ và cung cấp công cụ tự đánh giá** – có **kế hoạch học tập chi tiết đến từng tuần**; công cụ tự đánh giá (ví dụ **trắc nghiệm trực tuyến, bài tập trực tuyến**); **lưu vết** hoạt động người học.
8. **Các dịch vụ đào tạo được triển khai đồng bộ** – giải đáp trực tuyến, tư vấn học tập, tư vấn hướng nghiệp, hỗ trợ tìm việc làm…

#### C. Phân loại lớp học – Sloan Consortium (Hội đồng nghiên cứu e-learning Hoa Kỳ), **năm 2006** ⭐⭐
| Nhóm | % nội dung qua Internet | Loại lớp | Mô tả |
|---|---|---|---|
| A | 0% | Truyền thống | Tất cả trực tiếp |
| B | 1–29% | Sử dụng công nghệ Internet | Đăng học liệu (đề cương, bài tập, bài giảng) lên Internet; thầy trò gặp mặt trực tiếp |
| C | 30–79% | Kết hợp (Blended/Hybrid) | Có cả trao đổi trên Internet và buổi gặp trực tiếp |
| D | 80+% | Trực tuyến (Online) | Tất cả trên Internet, không gặp mặt |

→ Lớp ở mức **C và D** được coi là lớp học **e-learning**.

#### D. Mô hình chức năng & mô hình hệ thống ⭐⭐⭐
- Mô hình chức năng gồm **2 thành phần chính**: **LCMS** và **LMS** (theo SCORM của **ADL**).
- Hệ thống e-learning gồm **3 phần chính**:
  1. **Hạ tầng truyền thông và mạng** – thiết bị đầu cuối người dùng, thiết bị tại cơ sở cung cấp dịch vụ, mạng truyền thông…
  2. **Hạ tầng phần mềm** – phần mềm LMS, LCMS (ví dụ MacroMedia, Authorware, Toolbook…).
  3. **Nội dung đào tạo (hạ tầng thông tin)** – phần **quan trọng**: nội dung khóa học, phần mềm dạy học (courseware)…
- LCMS = tập trung **xây dựng và phát triển nội dung**; LMS = **hỗ trợ học tập và quản lý học tập** (đăng ký, giúp đỡ, kiểm tra…) → LMS là **giao diện chính cho sinh viên học tập** và phòng quản lý đào tạo quản lý việc học.

#### E. Thành phần trong hoạt động hệ thống (Hình 3.4) ⭐⭐
- **Giảng viên (A)**: cung cấp nội dung cho phòng (C) dựa trên kết quả dự kiến nhận từ phòng (D); tương tác với sinh viên qua LMS.
- **Sinh viên (B)**: dùng cổng thông tin người dùng để học, trao đổi với giảng viên (qua LMS), dùng công cụ hỗ trợ.
- **Phòng biên tập, xây dựng chương trình (C)**: kỹ thuật viên thiết kế bài giảng điện tử **theo chuẩn SCORM**; sản phẩm đưa vào Ngân hàng bài giảng điện tử (II).
- **Phòng quản lý đào tạo (D)**: quản lý đào tạo qua LMS; tập hợp nhu cầu sinh viên → yêu cầu cho giảng viên → **chu trình kín**.
- **Cổng thông tin người dùng (user's portal)**: giao diện chính cho A, B, C, D; truy cập qua Internet từ máy tính hoặc thiết bị di động.
- **LCMS (1)**: A và C hợp tác trong môi trường đa người dùng; kết nối với (I) và (II).
- **LMS (2)**: hỗ trợ học tập + quản lý học tập.
- **Công cụ hỗ trợ học tập (3)**: thư viện điện tử, phòng thực hành ảo, trò chơi… (có thể tích hợp vào LMS).
- **Công cụ thiết kế bài giảng điện tử (4)**: thiết bị studio (máy ảnh, máy quay, máy ghi âm), phần mềm xử lý multimedia → công cụ chính cho phòng (C).
- **Ngân hàng kiến thức (I)**: CSDL đơn vị kiến thức cơ bản, **tái sử dụng** được; (C) quản lý qua LCMS.
- **Ngân hàng bài giảng điện tử (II)**: CSDL bài giảng điện tử; sinh viên truy cập qua **LMS**.

#### F. 4 khả năng cần đạt khi tuân theo chuẩn ⭐⭐
Tương hợp (**Interoperability**) – Tái sử dụng (**Re-usability**) – Quản lý (**Manageability**) sinh viên, nội dung – Truy nhập (**Accessibility**).

#### G. 4 nhóm chuẩn e-learning ⭐⭐⭐
1. **Chuẩn đóng gói (packaging)** – ghép các khóa học từ công cụ/nhà sản xuất khác nhau thành gói; chuyển giữa các LMS/LCMS không phải cấu trúc lại.
2. **Chuẩn trao đổi thông tin (communication)** – hệ thống quản lý hiển thị từng bài, theo dõi kết quả kiểm tra, quá trình học. Gồm **2 phần: giao thức và mô hình dữ liệu**.
3. **Chuẩn metadata** – mô tả khóa học/module để tìm kiếm, phân loại.
4. **Chuẩn chất lượng (quality)** – thiết kế khóa học + khả năng hỗ trợ người tàn tật.

**Chuẩn đóng gói phổ biến:**
- **AICC** (Aviation Industry CBT Committee) – cần nhiều file, thiết kế cấu trúc phức tạp; nhược: phức tạp khi thực thi, **không hỗ trợ sử dụng lại module ở mức thấp**.
- **IMS Content and Packaging** (IMS Global Consortium) – đơn giản và chặt chẽ hơn; Microsoft LRN Toolkit hỗ trợ.
- **SCORM** – kết hợp nhiều đặc tả, trong đó có IMS Content and Packaging; các phiên bản **1.1, 1.2, 2004**; là chuẩn đóng gói **được sử dụng nhiều nhất**.
- File manifest: bắt buộc tên **`imsmanifest.xml`**, tuân theo XML; gồm **4 phần**: **Meta-data**, **Organizations** (như mục lục), **Resources**, **Sub-manifests**.
- Định dạng gộp file khuyến cáo: **ZIP (PKZIP), JAR, CAB**. Cách thực thi chuẩn theo công nghệ cụ thể gọi là **binding** (không phải phần lõi của chuẩn).
- Công cụ đóng gói: **ReloadEditor** (mã nguồn mở, SCORM 1.2/2004), **eXe** (mã nguồn mở, soạn bài không cần biết HTML/XML).

**Chuẩn trao đổi thông tin:**
- Giao thức = luật trao đổi (thời điểm bắt đầu/kết thúc, luồng thông tin); mô hình dữ liệu = dữ liệu trao đổi (điểm, tên SV, mức độ hoàn thành).
- **AICC**: AGRs (AICC Guidelines and Recommendations); **AGR006** về CMI (computer-managed instruction) – Web, mainframe, đĩa; **AGR010** chỉ đào tạo dựa trên Web.
- **SCORM**: **RTE** (Runtime Environment) quy định trao đổi giữa hệ thống quản lý đào tạo và **SCO** (Sharable Content Object) tương ứng một module.

**Chuẩn metadata** (metadata = dữ liệu về dữ liệu):
- 3 đặc tả: **IEEE 1484.12** Learning Object Metadata; **IMS** Learning Resources Meta-data; **SCORM** Meta-data.
- IMS và SCORM viết "meta-data"; IEEE và đa số viết "metadata".
- **IEEE metadata** là đặc tả **duy nhất được chứng nhận là chuẩn**.
- 13 thành phần chính (IEEE 1484.12): Title, Language, Description, Keyword, Structure, Aggregation Level, Version, Format, Size, Location, Requirement, Duration, Cost.

**Chuẩn chất lượng:**
- Chuẩn thiết kế: **e-learning Courseware Certification Standards** của **ASTD** e-learning Certification Institute (thiết kế giao diện, tương thích hệ điều hành/công cụ, chất lượng sản xuất, thiết kế giảng dạy).
- Chuẩn tính truy cập được: cho người tàn tật; **chưa có chuẩn riêng cho e-learning**, tận dụng chuẩn CNTT và nội dung Web.

#### H. Yêu cầu LMS điển hình – các ý dễ hỏi ⭐
- Chung: nâng cấp số người dùng không hạn chế; người dùng thông thường (giáo viên) dùng được; là **ứng dụng Web**; đa ngôn ngữ (cơ bản tiếng Anh, tiếng Việt).
- Kỹ thuật: tương thích trình duyệt chuẩn; tích hợp **ERP, HR, CRM**; thiết kế theo **module**; học qua đường thoại; tích hợp thư điện tử.
- Bảo mật: ID + mật khẩu; ngăn đăng ký trái phép; hạn chế truy nhập bản ghi cá nhân (chỉ người học, người giám sát, người quản lý chương trình); bảo mật **đa lớp (ít nhất 2 lớp)**.
- Chức năng chung có: **diễn đàn nội bộ, thư điện tử cục bộ, chat trực tuyến**; tính học phí.
- Đăng ký – giám sát: nhiều loại khóa học (**ILT**, đồng bộ, không đồng bộ…); xác nhận đăng ký ngay qua **e-mail**; ngăn **đăng ký lặp**; theo dõi sự có mặt…
- Chuẩn hóa: tích hợp khóa học theo **SCORM và AICC**; hỗ trợ khóa học từ bên thứ 3; công cụ ToolBook, Authorware, Dreamweaver.
- Kiểm tra – dạng câu hỏi: **đa lựa chọn; đúng/sai; điền vào chỗ trống; kéo thả; câu trả lời ngắn**; chọn ngẫu nhiên câu hỏi; giới hạn số lần làm; giới hạn thời gian; kiểm tra trước/trong/sau khóa học; hỗ trợ bài luận; kết quả lưu trong CSDL.

#### I. Ưu – nhược điểm ⭐⭐
**Cơ sở đào tạo**
- Ưu: giảm chi phí tổ chức & quản lý (dạy hàng ngàn SV với chi phí chỉ cao hơn chút so với 20 SV); rút ngắn thời gian đào tạo; cần ít phương tiện hơn; GV và SV không phải đi lại nhiều; tổng hợp được kiến thức.
- Nhược: chi phí phát triển lớn (**gấp 5–10 lần** khóa học thông thường cùng nội dung); yêu cầu kỹ năng mới; lợi ích chưa được khẳng định; đòi hỏi thiết kế lại (do SV thiếu mạng tốc độ cao).

**Người học**
- Ưu: học bất cứ lúc nào, nơi đâu; không phải đi lại, không phải nghỉ việc; tự quyết định việc học; khả năng truy cập nâng cao (người khiếm thính/thị, học ngoại ngữ hai, chứng khó đọc); kiểm tra tính xác thực (tự ôn, tự kiểm tra "không có ai giám sát và cho điểm").
- Nhược: kỹ thuật phức tạp; chi phí kỹ thuật cao; việc học có thể buồn tẻ (thiếu bạn bè, tiếp xúc); **yêu cầu ý thức cá nhân cao hơn**.
- Khắc phục buồn tẻ: thảo luận/chat với giảng viên và bạn học qua mạng, tham dự **diễn đàn**.

#### J. Thiết bị mạng trung tâm (Hình 3.3) ⭐
- Web Server: Web hosting, phân loại & chuyển hướng kết nối.
- Database Server: quản trị, lưu trữ dữ liệu dịch vụ; tự động backup; đồng bộ với nhà cung cấp khác.
- Content Server: lưu trữ dữ liệu bài học **multimedia**.
- Mail Server: thư điện tử riêng của hệ thống.
- Tape Backup: sao lưu. Router: **Internet Gateway**. Firewall: chống truy nhập không hợp lệ. Switch: đầu kết nối server, phòng soạn bài, phòng quản trị. Load Balancing: phân tải truy xuất multimedia.

---

## Phụ lục: Hướng dẫn sử dụng hệ thống NEU E-learning

> Nguồn: `HDSD-elearning.pdf` – "Hướng dẫn sử dụng hệ thống đào tạo trực tuyến NeuElearning", Trung tâm Đào tạo từ xa – ĐH KTQD, TS.GVC Trịnh Hoài Sơn, Hà Nội 09/2018 (38 trang). Học viên = người học.

### Tóm tắt (theo mục, tên chức năng/menu/nút)

**1. Giới thiệu**
- NEU Elearning (Cổng thông tin học tập trực tuyến ĐH KTQD) xây dựng trên **môi trường mã nguồn mở Moodle**.
- Mục tiêu: cung cấp, hỗ trợ học viên tiếp cận nguồn học liệu phong phú, đa dạng; giúp **tự học, tự bồi dưỡng ngay tại chỗ, thường xuyên, liên tục**.
- Địa chỉ: **http://elearning.neu.edu.vn**

**2. Đăng nhập và thiết lập tài khoản**
- 2.1 Đăng nhập: mở trình duyệt → vào trang chủ → chọn **(login)** ở **góc trên bên phải** → nhập **Tên đăng nhập (hoặc email)** + **Mật khẩu** → nút **ĐĂNG NHẬP** hoặc phím Enter. Đúng → chuyển đến **Trang cá nhân**.
- 2.2 Đăng xuất: bấm biểu tượng người dùng/ảnh/tên ở góc trên bên phải → **Thoát**.
- 2.3 Thay đổi mật khẩu (nên đổi ở **lần đăng nhập đầu tiên**): biểu tượng người dùng → **Tùy chọn** → (Tài khoản người dùng / User account) **Sửa hồ sơ cá nhân** → nhập mật khẩu mới ("Click to enter text") → nút **Cập nhật hồ sơ**.
- 2.4 Thay đổi Hồ sơ cá nhân (ảnh, họ tên, ngày sinh, giới tính, địa chỉ, sở thích…): biểu tượng người dùng → **Tùy chọn** → **Sửa hồ sơ cá nhân** → cập nhật → **CẬP NHẬT HỒ SƠ**.
- 2.5 Quên mật khẩu: chưa khai báo email → liên hệ **Trung tâm Đào tạo từ xa**; đã khai báo → trang Đăng nhập → liên kết **Quên mật khẩu** → nhập Tên đăng nhập hoặc Email → **Tìm kiếm** → nhận email "**Yêu cầu đặt lại mật khẩu**" → nhấp liên kết → nhập + xác nhận mật khẩu → **LƯU NHỮNG THAY ĐỔI** (hệ thống tự đăng nhập).
- 2.6 Trang cá nhân: mục **TRANG CÁ NHÂN** trên thanh thực đơn chính; gồm **Home, Dashboard, Events, My Courses**.

**3. Học tập**
- 3.1 Truy cập khóa học: Trang cá nhân → thẻ **MyCourses** → chọn lớp.
- 3.2.1 Làm bài trắc nghiệm: xem ở **Timeline** hoặc **Upcoming Events** → nút **Attempt quiz now** → điều hướng bằng **Quiz Navigation** (lề trên bên trái), **Next page / Previous Page** → nộp sớm: **Finish attempt…** → **Nộp bài và kết thúc**.
- 3.2.2 Xem lại bài trắc nghiệm: hệ thống báo tổng số lần làm và điểm mỗi lần.
- 3.2.3 Làm và nộp bài tự luận: xem submission status, grading status, hạn chót, thời gian còn lại, submission comments → nút **Add submission** → chọn tệp hoặc **kéo thả** → **Lưu những thay đổi**.
- 3.2.4 Xem điểm tích lũy (3 cách): menu góc trên phải → **Điểm**; thẻ **This course** → **Điểm số**; cây tài nguyên lề trái → lớp → **Điểm số**. Bảng điểm gồm **Overview report** và **User report**.
- 3.2.5 Mở bài giảng trực tuyến (**SCORM**): nút **Enter**.
- 3.2.6 Diễn đàn (forum) + **Chatroom**.
- 3.2.7 Điểm danh theo tuần: mục **Điểm danh** → **Submit attendance** (*từ năm 2019 không còn sử dụng*).
- 3.2.8 Tin nhắn với giảng viên: lề trái → **Message my teacher** → chọn tên giảng viên; theo dõi ở hộp **Inbox** (góc trên bên phải, cạnh tên mình).
- 3.2.9 Download tài nguyên: bấm tên tệp hoặc nút **Download**.

**4. Ứng dụng di động** (Android, iOS)
- Cài **Ứng dụng Moodle** từ Google Play/App Store → nhập **elearning.neu.edu.vn** vào ô **Site address** → **Connect!** → **Username / Password** → **Log in** (ứng dụng lưu tài khoản, lần sau không cần đăng nhập lại).
- Đăng xuất: menu góc trên bên trái → **Logout**.
- **Course overview**: 2 tab **Timeline** và **Courses**. Hiển thị toàn bộ nội dung: **All sections**.
- Tài liệu là tệp **PDF** (cần app đọc PDF: Google PDF Viewer, iBooks, Foxit…).
- Bài giảng trực tuyến chuẩn **SCORM**: vùng **Start a new Attempt** → **Enter**.
- Diễn đàn: **Add a new discussion topic** → **Subject** + **Message** (+ **Add file**) → **Post to forum**; trả lời: **Reply** → Message → **Post to forum**.
- Làm bài trắc nghiệm: **Attempt quiz now** → tích ô tròn → **Next** → **Submit all and finish** → **OK** (hoặc **Return to Attempt**).
- Xem điểm: menu → **Grades**.

### Chi tiết cần thuộc

- ⭐⭐⭐ NEU Elearning dựa trên **mã nguồn mở Moodle**; địa chỉ **elearning.neu.edu.vn**; tài liệu HDSD năm **09/2018**.
- ⭐⭐⭐ **Đổi ảnh đại diện / hồ sơ / mật khẩu**: biểu tượng người dùng (góc trên phải) → **Tùy chọn** → **Sửa hồ sơ cá nhân** → **Cập nhật hồ sơ**. Nên dùng ảnh chân dung hiện thời để thuận tiện **nhận dạng, đối chiếu**; nên khai báo **email chính xác** để nhận thông báo/phục hồi tài khoản.
- ⭐⭐ Mật khẩu mới: **ít nhất 8 ký tự**, gồm **chữ thường, chữ hoa, chữ số, ký tự đặc biệt** (ví dụ `Tx-113452`).
- ⭐⭐ Trang cá nhân 4 mục: **Home** (danh sách lớp, thông báo toàn thể), **Dashboard** (dòng thời gian, công việc/bài tập đã–đang–sẽ làm), **Events** (sự kiện sắp xảy ra, bài tập sắp hết hạn), **My Courses** (danh sách lớp của mình).
- ⭐⭐⭐ Cấu trúc một lớp học: (1) **Thông tin tổng quát** (giới thiệu lớp, diễn đàn, đề cương chi tiết, quy định chung); (2) **Tài liệu tham khảo** (không bắt buộc, khuyến khích đọc); (3) **Nội dung học tập theo từng tuần**; thông thường lớp học **8 tuần**.
- ⭐⭐⭐ Tài nguyên mỗi tuần: **Slide bài giảng** (tệp **PDF**, xem trực tuyến hoặc tải về); **Bài giảng online** (lời giảng của GV theo slide, có thể có video hướng dẫn thực hành); **Bài kiểm tra**; tài nguyên khác.
- ⭐⭐⭐ Bài kiểm tra theo HDSD có 2 dạng:
  - **Trắc nghiệm**: nội dung theo kiến thức tuần; **được làm lại nhiều lần**, **chấm tự động**, **lấy điểm cao nhất** (chính sách có thể đổi thành **trung bình cộng** các lần làm, sẽ được thông báo trước).
  - **Viết luận (tự luận)**: giảng viên chấm.
- ⭐⭐⭐ Tài nguyên học liệu truy cập **bất cứ lúc nào**, nhưng bài kiểm tra tuần **chỉ mở trong khoảng thời gian của tuần đó**; **không làm = 0 điểm**. **Điểm kiểm tra 20%** của môn = **trung bình cộng** các bài kiểm tra trong **8 tuần**.
- ⭐⭐ Điểm trắc nghiệm hiển thị = số câu đúng / tổng số câu; quy hệ 10 = (số câu đúng / tổng câu) × 10. Trong User report xem cột **Phần trăm**.
- ⭐⭐ Trong khi làm bài: còn thời gian thì **được sửa** phương án đã chọn; có thể bỏ qua câu khó và quay lại bằng cách bấm số hiệu câu trên Quiz Navigation.
- ⭐⭐ Nộp bài tự luận: tệp **< 4 MB**; tệp lớn → upload lên dịch vụ đám mây và nộp tệp Word chứa link; video lớn → upload **YouTube** rồi nộp link.
- ⭐⭐ Bài giảng trực tuyến (SCORM): slide chạy trên trình duyệt, có lời giảng, video GV, trình diễn thực hành; trình duyệt cần **trình chạy Flash**; nên xem trên **máy tính** (trên di động tốn tài nguyên, rất chậm); có thể xem tiếp từ lần trước, chọn nội dung ở cửa sổ bên trái.
- ⭐⭐⭐ **Diễn đàn** – học viên có thể: nhận **thông báo công khai** của GV/ban quản lý; theo dõi và tham gia **thảo luận** chủ đề môn học; **đặt câu hỏi, đề nghị trợ giúp công khai**; **thêm chủ đề (Topic) mới**, viết **bình luận** (comment/phúc đáp). Nội dung luôn được **cán bộ quản lý theo dõi, kiểm soát**; nội dung không liên quan bị xóa, cấm, cảnh báo.
- ⭐⭐ **Chatroom**: cho học viên **đang online** trong lớp cùng nói chuyện.
- ⭐⭐ **Tin nhắn riêng tư** với GV: **Message my teacher** (lề trái lớp học); theo dõi qua **Inbox** (góc trên phải). Nếu đăng ký email, mỗi tin nhắn hệ thống sẽ gửi **email thông báo**.
- ⭐ Download được: **đề cương chi tiết** môn học, **tệp tài liệu tham khảo**.
- ⭐ Điểm danh theo tuần: **từ năm 2019 không còn sử dụng**.
- ⭐⭐ Ứng dụng di động: **Moodle** (Android & iOS); Site address = elearning.neu.edu.vn.
