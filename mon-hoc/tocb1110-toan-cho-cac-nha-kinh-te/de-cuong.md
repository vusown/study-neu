# Đề cương — Toán cho các nhà kinh tế

> **Nguồn:** 12 file bài giảng (slide) trong [`tai-lieu/`](tai-lieu/) và [đề cương chi tiết học phần](tai-lieu/00-de-cuong-chi-tiet-hoc-phan.pdf). Đánh số bài **theo file bài giảng** (12 bài).
>
> **Mức độ ra thi:** ⭐⭐⭐ chắc chắn ra · ⭐⭐ hay ra · ⭐ ít ra. Chưa có đề thi mẫu nên mức sao dựa vào ma trận đề (Phụ lục 1 đề cương) và các ví dụ ứng dụng trong bài giảng.
>
> **Mỗi bài có mục 🎯 "Đề hỏi gì"**. Bài mẫu và lời giải nằm ở [ngan-hang-theo-chu-de.md](ngan-hang-theo-chu-de.md).
>
> ⚠️ là chỗ bổ sung ngoài bài giảng. ⚡ là chỗ dễ nhầm hoặc slide in nhầm.
>
> **Số viết theo kiểu bài giảng:** dấu chấm thập phân, dấu phẩy phân cách nghìn (6,800 = sáu nghìn tám trăm; 0.67 = không phẩy sáu bảy).
>
> **Đối chiếu số bài** (đề cương chi tiết 2025 chia 9 bài, cùng 6 chương):
>
> | Bài giảng | Chương | Đề cương 2025 (tuần, LTTN) | Ma trận đề |
> |---|---|---|---|
> | 1. Hàm số và giới hạn | 1 | Bài 1 (1.1–1.3) | Lecture 1 · Nhớ |
> | 2. Đạo hàm và vi phân (Phần 1) | 2 | Bài 2 (2.1–2.3) | Lecture 2 · Nhớ |
> | 3. Đạo hàm và vi phân (Phần 2) | 2 | Bài 3 (2.4–2.5) | Lecture 3 · Hiểu |
> | 4. Ứng dụng của đạo hàm (Phần 1) | 3 | Bài 4 (3.1–3.2) | Lecture 4 · Vận dụng |
> | 5. Ứng dụng của đạo hàm (Phần 2) | 3 | Bài 4 (3.3–3.4) | Lecture 4 · Vận dụng |
> | 6. Phép toán tích phân (Phần 1) | 4 | Bài 5 (4.1–4.3) | Lecture 5 · Nhớ |
> | 7. Phép toán tích phân (Phần 2) | 4 | Bài 6 (4.4–4.5) | Lecture 6 · Hiểu |
> | 8. Chủ đề tích phân chọn lọc (Phần 1) | 5 | Bài 7 (5.1) | Lecture 7 · Nhớ |
> | 9. Chủ đề tích phân chọn lọc (Phần 2) | 5 | Bài 7 (5.2–5.3) | Lecture 7 · Nhớ |
> | 10. Hàm số nhiều biến và đạo hàm riêng | 6 | Bài 8 (6.1–6.2) | Lecture 8 · Hiểu |
> | 11. Cực trị hàm nhiều biến (Phần 1) | 6 | Bài 9 (6.3) | Lecture 9 · Vận dụng |
> | 12. Cực trị hàm nhiều biến (Phần 2) | 6 | Bài 9 (6.4) | Lecture 9 · Vận dụng |

## Mục lục

- [Bài 1: Hàm số và giới hạn — ⭐⭐](#bài-1-hàm-số-và-giới-hạn--)
- [Bài 2: Đạo hàm và vi phân của hàm số (Phần 1) — ⭐⭐⭐](#bài-2-đạo-hàm-và-vi-phân-của-hàm-số-phần-1--)
- [Bài 3: Đạo hàm và vi phân của hàm số (Phần 2) — ⭐⭐⭐](#bài-3-đạo-hàm-và-vi-phân-của-hàm-số-phần-2--)
- [Bài 4: Một số ứng dụng của đạo hàm (Phần 1) — ⭐⭐⭐](#bài-4-một-số-ứng-dụng-của-đạo-hàm-phần-1--)
- [Bài 5: Một số ứng dụng của đạo hàm (Phần 2) — ⭐⭐⭐](#bài-5-một-số-ứng-dụng-của-đạo-hàm-phần-2--)
- [Bài 6: Phép toán tích phân (Phần 1) — ⭐⭐⭐](#bài-6-phép-toán-tích-phân-phần-1--)
- [Bài 7: Phép toán tích phân (Phần 2) — Các ứng dụng của tích phân — ⭐⭐⭐](#bài-7-phép-toán-tích-phân-phần-2--các-ứng-dụng-của-tích-phân--)
- [Bài 8: Một số chủ đề chọn lọc về tích phân (Phần 1) — ⭐⭐](#bài-8-một-số-chủ-đề-chọn-lọc-về-tích-phân-phần-1--)
- [Bài 9: Một số chủ đề tích phân chọn lọc (Phần 2) — ⭐⭐](#bài-9-một-số-chủ-đề-tích-phân-chọn-lọc-phần-2--)
- [Bài 10: Hàm số nhiều biến và đạo hàm riêng — ⭐⭐⭐](#bài-10-hàm-số-nhiều-biến-và-đạo-hàm-riêng--)
- [Bài 11: Cực trị của hàm số nhiều biến (Phần 1) — ⭐⭐⭐](#bài-11-cực-trị-của-hàm-số-nhiều-biến-phần-1--)
- [Bài 12: Cực trị của hàm số nhiều biến (Phần 2) — ⭐⭐⭐](#bài-12-cực-trị-của-hàm-số-nhiều-biến-phần-2--)

---

## Bài 1: Hàm số và giới hạn — ⭐⭐

> Bài giảng: TS. Phùng Minh Đức. Đề cương: Bài 1 · Chương 1 · mục 1.1 Hàm số, 1.2 Các mô hình hàm số, 1.3 Giới hạn của hàm số. Ma trận đề: Lecture 1 (Nhớ).

### Tóm tắt
- **Hàm** f cho tương ứng mỗi x ∈ A với **một và chỉ một** y ∈ B. A là **tập xác định**, B là **tập giá trị**. Không chỉ định thì lấy **miền xác định tự nhiên** (mọi x làm f(x) có nghĩa).
- **Các hàm kinh tế:** cầu p = D(x), cung p = S(x), doanh thu **R(x) = x·p(x)**, chi phí C(x), lợi nhuận **P(x) = R(x) − C(x)**, các hàm bình quân **AC, AR, AP** (chia cho x).
- **Hàm hợp** f[g(x)]: thay u = g(x) vào công thức f(u), giống dây chuyền lắp ráp (máy g rồi đến máy f).
- **Lập mô hình toán học:** Bài toán thực tế → Mô hình toán học → Diễn giải → Kiểm nghiệm → quay lại (hình thành mô hình, phân tích, dự đoán, điều chỉnh).
- **Cân bằng thị trường:** **S(xₑ) = D(xₑ)**, giá cân bằng pₑ = S(xₑ) = D(xₑ). S > D là **dư thừa**, S < D là **thiếu hụt**.
- **Hòa vốn:** giao điểm của C(x) và R(x). Trước điểm hòa vốn **thua lỗ** (C > R), sau điểm hòa vốn **có lợi nhuận** (R > C).
- **Giới hạn** lim_{x→c} f(x) = L: f(x) tiến gần L khi x tiến gần c **từ cả hai phía**. Giới hạn nói về hành vi **gần** c, không phụ thuộc giá trị **tại** c.
- **Tính chất giới hạn:** giới hạn của tổng, hiệu, tích, thương (mẫu ≠ 0), lũy thừa bằng tổng, hiệu, tích, thương, lũy thừa các giới hạn. Đa thức và phân thức (mẫu ≠ 0) thì **thay thẳng x = c**.
- **Giới hạn tại vô hạn** (x → ±∞): lim A/xᵏ = 0 với k > 0. **Giới hạn vô cực** (lim = ±∞): f(x) tăng/giảm không bị chặn khi x → c.

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Hàm kinh tế:**
  - **R(x) = x·p(x)**
  - **P(x) = R(x) − C(x)**
  - **AC(x) = C(x)/x; AR(x) = R(x)/x; AP(x) = P(x)/x**
- **Hàm hợp:** cho y = f(u), u = g(x) ⇒ **y = f[g(x)]** (thay toàn bộ u bằng g(x)).
- **Cân bằng thị trường:** giải **S(x) = D(x)** được xₑ (lấy nghiệm x ≥ 0) rồi **pₑ = S(xₑ) = D(xₑ)**.
- **Hòa vốn:** giải **R(x) = C(x)** (tương đương **P(x) = 0**), loại nghiệm âm hoặc vượt công suất; giá tại điểm hòa vốn p = p(x).
- **Có lợi nhuận:** **P(x) > 0**. Với P(x) bậc hai hệ số x² âm thì P > 0 ở **giữa hai nghiệm**.
- **Lợi nhuận lớn nhất của P(x) = ax² + bx + c (a < 0):** đạt tại **x = −b/(2a)** (đỉnh parabol), giá trị lớn nhất là P(−b/(2a)).
- **Các bước bài lập mô hình (Ví dụ 5):**
  1. Đặt ẩn x (giá bán).
  2. Biểu diễn số lần thay đổi giá: x − giá cũ.
  3. Biểu diễn lượng bán theo x.
  4. Lợi nhuận mỗi đơn vị = x − chi phí mỗi đơn vị.
  5. P(x) = (lượng bán)·(lợi nhuận mỗi đơn vị), khai triển thành ax² + bx + c.
  6. Tìm đỉnh x = −b/(2a), tính P tại đỉnh.
- **Tính chất giới hạn** (khi lim f, lim g tồn tại):
  - lim [f ± g] = lim f ± lim g
  - lim k·f = k·lim f
  - lim [f·g] = lim f · lim g
  - lim f/g = lim f / lim g nếu **lim g ≠ 0**
  - lim [f]ᵖ = [lim f]ᵖ nếu [lim f]ᵖ tồn tại
  - lim_{x→c} k = k; lim_{x→c} x = c
  - **lim_{x→c} P(x) = P(c); lim_{x→c} P(x)/Q(x) = P(c)/Q(c) nếu Q(c) ≠ 0** (P, Q là đa thức)
- **Giới hạn tại vô hạn:** **lim_{x→+∞} A/xᵏ = 0 và lim_{x→−∞} A/xᵏ = 0** (A, k hằng số, k > 0, xᵏ xác định với mọi x).

### 1.1. Hàm số, tập xác định, giá trị của hàm ⭐⭐
- Hàm là quy tắc gán mỗi x ∈ A với **đúng một** y ∈ B; y = f(x) là giá trị của f tại x. x là **biến độc lập**, y là **biến phụ thuộc**. Tập xác định và tập giá trị là tập số thực thì gọi là **hàm số**.
- Hai cách hiểu: hàm như **ánh xạ** (mũi tên từ A sang B) và hàm như **cỗ máy** (đầu vào x → máy f → đầu ra f(x)).
- **Tìm tập xác định:** tìm mọi x để biểu thức có nghĩa. Ví dụ 1: f(x) = √(3 − 2x)/(x² + 4), mẫu x² + 4 > 0 với mọi x nên chỉ cần 3 − 2x ≥ 0 ⇔ x ≤ 3/2, **D = (−∞; 3/2]**; f(1) = 1/5.
- ⚠️ (bổ sung, slide tr. 4 bị cắt phần này) Các điều kiện hay gặp: **mẫu ≠ 0**, **biểu thức dưới căn bậc chẵn ≥ 0**.
- **Hàm cho bởi nhiều công thức:** xem x thuộc khoảng nào rồi dùng đúng công thức. Ví dụ 2: S(t) = 8.1 − 1.7t (t < 3), S(t) = 6t² − 36t + 57 (t ≥ 3); S(2) = 4.7, S(7.5) = 124.5. Ý nghĩa: t tính từ 1/1/2000 nên t = 2 là ngày 1/1/2002, t = 7.5 là ngày 1/7/2007.

### 1.2. Các hàm số trong kinh tế học và hàm hợp ⭐⭐⭐
- **Hàm cầu D(x):** giá p = D(x) phải trả cho mỗi đơn vị khi x đơn vị được cầu.
- **Hàm cung S(x):** đơn giá p = S(x) mà nhà sản xuất sẵn sàng cung cấp x đơn vị.
- **Doanh thu R(x) = x·p(x)**; **chi phí C(x)**; **lợi nhuận P(x) = R(x) − C(x)**; **bình quân AC = C/x, AR = R/x, AP = P/x**.
- Ví dụ 3 (máy pha cà phê): p(x) = −0.27x + 51, C(x) = 2.23x² + 3.5x + 85 ⇒ **AC(4) = 33.67** đô la/máy; R(x) = −0.27x² + 51x; **P(x) = −2.5x² + 47.5x − 85**; có lợi nhuận khi **2 < x < 17** (nghìn máy).
- **Hàm hợp f[g(x)]:** thay u = g(x) vào f(u). Ví dụ 4: f(u) = u² + 3u + 1, g(x) = x + 1 ⇒ **f[g(x)] = x² + 5x + 5**, **g[f(u)] = u² + 3u + 2**. Thứ tự hợp khác thì kết quả khác.

### 1.3. Mô hình hàm số: lập mô hình, cân bằng thị trường, hòa vốn ⭐⭐⭐
- **Quy trình lập mô hình:** Bài toán thực tế —(hình thành mô hình)→ Mô hình toán học —(phân tích)→ Diễn giải —(dự đoán)→ Kiểm nghiệm —(điều chỉnh)→ Bài toán thực tế.
- Ví dụ 5 (giấy in): chi phí $2/ream, giá $5 bán 4,000 reams/tháng, tăng $1 thì bán giảm 400 reams ⇒ P(x) = [4,000 − 400(x − 5)](x − 2) = **−400x² + 6,800x − 12,000**; giá tối ưu **x = 8.5** đô la, lợi nhuận tối đa **16,900** đô la.
- **Cân bằng thị trường:** S(xₑ) = D(xₑ), pₑ = S(xₑ) = D(xₑ). Trên đồ thị, đường cung đi lên, đường cầu đi xuống, cắt nhau tại điểm cân bằng (xₑ, pₑ). Phía trên điểm cân bằng (S > D) là **dư thừa**, phía dưới (S < D) là **thiếu hụt**.
- Ví dụ 6: S(x) = x² + 14, D(x) = 174 − 6x ⇒ **xₑ = 10, pₑ = 114**. Đường cung bắt đầu từ p = 14, đường cầu từ p = 174 và cắt trục x tại 29.
- **Phân tích hòa vốn:** điểm hòa vốn là giao điểm của C(x) và R(x). Đường doanh thu đi qua gốc, đường chi phí bắt đầu từ chi phí cố định (> 0). Bên trái điểm hòa vốn **thua lỗ**, bên phải **có lợi nhuận**.
- Ví dụ 7 (ghế Emory): p = 1,500 − 3x, chi phí cố định $66,500, $20/chiếc, công suất tối đa 300 ⇒ R(x) = 1,500x − 3x², C(x) = 66,500 + 20x; hòa vốn **x = 50, p = 1,350**; bán 35 chiếc thì **lỗ $18,375**.

### 1.4. Giới hạn của hàm số ⭐⭐
- **Định nghĩa trực quan:** f(x) tiến gần L khi x tiến gần c **từ cả hai phía** thì **lim_{x→c} f(x) = L**.
- Giới hạn mô tả hành vi **gần** c, không phải **tại** c: ba hàm cùng có lim_{x→3} f(x) = 4 dù (a) f(3) = 4, (b) f(3) ≠ 4, (c) f không xác định tại 3.
- **Không tồn tại giới hạn** khi: (a) hai phía tiến tới hai giá trị khác nhau (hàm bậc thang bằng 3 bên trái, 5 bên phải x = 2); (b) đồ thị tăng vọt lên vô hạn khi x → 2.
- **Tính chất giới hạn:** xem bảng công thức. Đa thức: thay thẳng. Phân thức: thay thẳng nếu mẫu ≠ 0.
- Ví dụ 8: lim_{x→1} (3x³ − 8)/(x − 2): mẫu → −1 ≠ 0 nên = (3 − 8)/(1 − 2) = **5**.

### 1.5. Các giới hạn liên quan đến vô hạn ⭐⭐
- **Giới hạn tại vô hạn:** f(x) tiến gần L khi x tăng không bị chặn: **lim_{x→+∞} f(x) = L**; khi x giảm không bị chặn: **lim_{x→−∞} f(x) = M**.
- **Chú ý:** A, k hằng số, k > 0 ⇒ **lim_{x→±∞} A/xᵏ = 0**.
- **Giới hạn vô cực:** lim_{x→c} f(x) = +∞ nếu f(x) tăng không bị chặn khi x → c; = −∞ nếu giảm không bị chặn.
- Ý nghĩa kinh tế/thực tế: giới hạn khi t → +∞ là **giá trị dài hạn**. Ví dụ 9 (nồng độ thuốc): C(t) = 0.4/(t^1.2 + 1) + 0.013 ⇒ C(0) = **0.413**; thay đổi trong giờ thứ 5 là C(5) − C(4) ≈ **−0.0131** (đang giảm); nồng độ tồn dư lim_{t→+∞} C(t) = **0.013** mg/ml.

### ⚡ Dễ nhầm
- **"Giờ thứ 5"** là khoảng từ t = 4 đến t = 5, nên thay đổi = **C(5) − C(4)**, không phải C(6) − C(5) hay C(5) − C(0).
- **Ví dụ 9, slide ghi** C(5) = 0.0506 và C(4) = 0.0637 (in nhầm, quên cộng 0.013). Đúng là C(5) ≈ 0.0636, C(4) ≈ 0.0767. Hiệu số −0.0131 vẫn đúng vì 0.013 triệt tiêu. Slide còn ghi "lim_{N→+∞}" ở bước giữa, đúng là lim_{t→+∞}.
- **Ví dụ 5, slide ghi** x = 6,800/(2(−400)) (thiếu dấu trừ, thay đúng như viết sẽ ra −8.5). Công thức đúng **x = −b/(2a) = −6,800/(2·(−400)) = 8.5**.
- **Đơn vị trong Ví dụ 3:** C tính bằng nghìn đô la, x bằng nghìn máy nên AC(4) = 134.68/4 = 33.67 là **đô la/máy** (không phải nghìn đô la/máy). "4,000 máy" ứng với **x = 4**.
- **Loại nghiệm:** cân bằng thị trường loại nghiệm âm (Ví dụ 6 loại x = −16); hòa vốn loại nghiệm vượt công suất (Ví dụ 7 loại x ≈ 443.33 > 300). Slide không ghi bước loại, đi thi phải ghi.
- **Ví dụ 6:** lời giải a) slide chỉ ghi x = 10; đề hỏi cả mức giá nên phải tính thêm **pₑ = 114**.
- **Thứ tự hàm hợp:** f[g(x)] ≠ g[f(x)] nói chung (Ví dụ 4: x² + 5x + 5 khác u² + 3u + 2).
- **Giới hạn ≠ giá trị tại điểm:** lim_{x→c} f(x) có thể tồn tại dù f(c) khác L hoặc f không xác định tại c.
- **Giới hạn tại vô hạn** (x → ±∞, kết quả là số) khác **giới hạn vô cực** (x → c, kết quả là ±∞).
- **Quy tắc thương** chỉ dùng khi **giới hạn của mẫu ≠ 0**. ⚠️ (bổ sung) Mẫu → 0 thì không thay thẳng được; bài giảng không có ví dụ dạng này.
- **Dư thừa / thiếu hụt:** S(x) > D(x) là **dư thừa**, S(x) < D(x) là **thiếu hụt** (đừng đảo).
- **Ký hiệu:** lợi nhuận trong bài giảng là **P(x)** (không dùng π); đề có thể dùng P vừa cho lợi nhuận vừa cho dân số, đọc kỹ.
- Slide tr. 23 viết "tiến gần đến số L" nhưng ký hiệu lim_{x→−∞} f(x) = **M** (không thống nhất chữ, không ảnh hưởng nội dung).

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Tìm tập xác định của hàm có căn và phân thức (Ví dụ 1); tính giá trị hàm, kể cả hàm cho bởi nhiều công thức (Ví dụ 2).
  - Tìm hàm hợp f[g(x)] hoặc g[f(x)] (Ví dụ 4).
  - Công thức R = x·p, P = R − C, AC = C/x; tính AC tại một mức sản lượng (Ví dụ 3a).
  - Điều kiện cân bằng thị trường S = D; nhận biết dư thừa (S > D) và thiếu hụt (S < D); tìm xₑ, pₑ (Ví dụ 6).
  - Điểm hòa vốn là giao của R(x) và C(x) (Ví dụ 7).
  - Tính giới hạn đa thức, phân thức bằng cách thay số (Ví dụ 8); giới hạn tại vô hạn dạng A/xᵏ → 0 (Ví dụ 9c).
  - Câu lý thuyết: giới hạn tồn tại khi hai phía tiến tới cùng một số; giới hạn không phụ thuộc giá trị tại điểm.
- **Tự luận:**
  - Lập hàm doanh thu, lợi nhuận từ hàm cầu và hàm chi phí, tìm khoảng sản lượng có lợi nhuận: mẫu **Ví dụ 3**.
  - Lập mô hình lợi nhuận theo giá bán rồi tìm giá tối ưu (đỉnh parabol): mẫu **Ví dụ 5**. (Bài 4–5 sẽ giải dạng này bằng đạo hàm.)
  - Cân bằng thị trường và phác họa đường cung cầu: mẫu **Ví dụ 6**.
  - Phân tích hòa vốn, tính lãi/lỗ tại một mức sản lượng: mẫu **Ví dụ 7**.
  - Bài thực tế có giá trị ban đầu, thay đổi trong một khoảng, giá trị dài hạn (giới hạn tại vô hạn): mẫu **Ví dụ 9**.

---

## Bài 2: Đạo hàm và vi phân của hàm số (Phần 1) — ⭐⭐⭐

> Bài giảng: TS. Phùng Minh Đức. Đề cương: Bài 2 · Chương 2 · mục 2.1 Đạo hàm, 2.2 Các kỹ thuật tính đạo hàm, 2.3 Các quy tắc tính đạo hàm. Ma trận đề: Lecture 2 (Nhớ).

### Tóm tắt
- Hàm bậc nhất L(x) = mx + b thay đổi với tốc độ **không đổi m**. Hàm phi tuyến có tốc độ thay đổi **phụ thuộc x**, bằng **độ dốc tiếp tuyến**.
- **Tốc độ thay đổi trung bình** = [f(c + h) − f(c)]/h (độ dốc cát tuyến). **Tốc độ thay đổi tức thời** = giới hạn khi h → 0 (độ dốc tiếp tuyến).
- **Đạo hàm f'(x) = lim_{h→0} [f(x + h) − f(x)]/h.** f'(c) vừa là **độ dốc tiếp tuyến** tại (c, f(c)), vừa là **tốc độ thay đổi** của f theo x tại x = c.
- **Ý nghĩa dấu:** f'(c) > 0 thì f **tăng** tại c; f'(c) < 0 thì f **giảm** tại c.
- **Quy tắc cơ bản:** hằng số, lũy thừa (n·xⁿ⁻¹ với mọi số thực n), hằng số nhân, tổng.
- **Tốc độ thay đổi tương đối Q'/Q** và **tốc độ thay đổi phần trăm 100·Q'/Q**.
- **Tích:** (f·g)' = f'·g + f·g'. **Thương:** (f/g)' = (f'·g − f·g')/g².
- **Hàm hợp (quy tắc dây chuyền):** dy/dx = (dy/du)·(du/dx) = f'[g(x)]·g'(x).
- **Đạo hàm cấp hai** f''(x) = (f'(x))' là **tốc độ thay đổi của tốc độ thay đổi**; cấp n: f⁽ⁿ⁾ = (f⁽ⁿ⁻¹⁾)'.
- Phần 1 chưa có khái niệm vi phân df = f'(x)dx (nằm ở Bài 3).

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Tốc độ_tb = [f(c + h) − f(c)]/h**; **Tốc độ_tt = lim_{h→0} [f(c + h) − f(c)]/h**.
- **Định nghĩa đạo hàm:** **df/dx = f'(x) = lim_{h→0} [f(x + h) − f(x)]/h**. f khả vi tại c nếu f'(c) tồn tại.
- **Độ dốc tiếp tuyến** tại (c, f(c)): **m_tt = f'(c)**. **Tốc độ thay đổi** tại x = c: **f'(c)**.
- **Dấu:** **f'(c) > 0 ⇒ f tăng tại c; f'(c) < 0 ⇒ f giảm tại c.**
- **Quy tắc cơ bản:**
  - d/dx (c) = 0
  - **d/dx (xⁿ) = n·xⁿ⁻¹** (mọi số thực n): ví dụ 1/√x = x⁻¹ᐟ², 1/x⁷ = x⁻⁷
  - d/dx [c·f(x)] = c·f'(x)
  - d/dx [f(x) + g(x)] = f'(x) + g'(x)
- **Tốc độ thay đổi tương đối:** **Q'(x)/Q(x)**. **Tốc độ thay đổi phần trăm:** **100·Q'(x)/Q(x)** (%/đơn vị x).
- **Tích:** **(f·g)' = f'·g + f·g'**.
- **Thương:** **(f/g)' = (f'·g − f·g')/g²** (g(x) ≠ 0).
- **Hàm hợp:** y = f(u), u = g(x) ⇒ **dy/dx = (dy/du)·(du/dx) = f'[g(x)]·g'(x)**.
- **Cấp cao:** **f''(x) = (f'(x))'**, ký hiệu f''(x) hoặc d²y/dx²; **f⁽ⁿ⁾(x) = (f⁽ⁿ⁻¹⁾(x))'**, ký hiệu dⁿy/dxⁿ.
- **Các bước bài "tốc độ thay đổi theo thời gian qua biến trung gian" (Ví dụ 8):**
  1. Tính dC/dx và dx/dt.
  2. Ghép dC/dt = (dC/dx)·(dx/dt).
  3. Tính x tại thời điểm t đề cho.
  4. Thay **cả t và x** vào, kết luận tăng/giảm và đơn vị (đơn vị C / đơn vị t).

### 2.1. Tốc độ thay đổi và định nghĩa đạo hàm ⭐⭐⭐
- Hàm tuyến tính có tốc độ thay đổi là hằng số m. Hàm phi tuyến: tốc độ thay đổi tại x = c là độ dốc tiếp tuyến tại P(c, f(c)).
- **Cát tuyến** nối P(c, f(c)) và Q(c + h, f(c + h)), Δx = h, Δy = f(c + h) − f(c), độ dốc = tốc độ thay đổi trung bình. Khi h → 0 cát tuyến tiến tới **tiếp tuyến**.
- **Đạo hàm** f'(x) = lim_{h→0} [f(x + h) − f(x)]/h; quá trình tính đạo hàm gọi là **phép toán vi phân**.
- **Tính đạo hàm bằng định nghĩa:** (1) tính f(x + h); (2) lập f(x + h) − f(x), rút gọn; (3) chia cho h; (4) cho h → 0. Ví dụ 1: P(x) = −400x² + 6,800x − 12,000 ⇒ [P(x + h) − P(x)]/h = −800x − 400h + 6,800 → **P'(x) = −800x + 6,800**.
- **Tốc độ thay đổi (đạo hàm) xấp xỉ thay đổi thực tế** trong một đơn vị tiếp theo. Ví dụ 3: dân số P(x) = x² + 20x + 8,000 ⇒ P'(15) = **50 người/tháng**, thay đổi thực tế trong tháng 16 là P(16) − P(15) = **51 người**.
- **Đơn vị của đạo hàm** = đơn vị của f / đơn vị của x (đô-la mỗi nghìn đơn vị sản phẩm; người/tháng; tỷ đô-la mỗi năm).

### 2.2. Ý nghĩa dấu của đạo hàm ⭐⭐⭐
- f khả vi tại c: **f'(c) > 0 ⇒ f tăng** tại c (đồ thị đi lên); **f'(c) < 0 ⇒ f giảm** tại c (đồ thị đi xuống).
- Ví dụ 1: P'(9) = −800(9) + 6,800 = **−400 < 0** ⇒ lợi nhuận **đang giảm** tại mức 9,000 sản phẩm (x tính bằng nghìn nên x = 9).
- Ví dụ 6: R'(4) = **−14 < 0** ⇒ doanh thu **đang giảm** khoảng 14 trăm đô la (1,400 đô la) mỗi tháng.

### 2.3. Các quy tắc tính đạo hàm: lũy thừa, tổng, tích, thương ⭐⭐⭐
- **Hằng số** → 0; **lũy thừa** n·xⁿ⁻¹ với mọi n thực (đổi căn, phân số sang lũy thừa trước); **hằng số nhân** giữ nguyên; **tổng** đạo hàm từng hạng tử.
- Ví dụ 2: −7/√x = −7x⁻¹ᐟ² ⇒ đạo hàm **(7/2)x⁻³ᐟ²**; 2x⁵ − 3x⁻⁷ + 3 ⇒ **10x⁴ + 21x⁻⁸**.
- **Tích (f·g)' = f'·g + f·g'**; **thương (f/g)' = (f'·g − f·g')/g²**.
- Ví dụ 5: (x − 1)(3x − 2) ⇒ **6x − 5**; (x² − 5x + 7)/(2x) ⇒ **(2x² − 14)/(4x²)** (rút gọn được (x² − 7)/(2x²)).
- **Doanh thu dạng tích theo thời gian:** R(t) = x(t)·p(t) ⇒ R'(t) = x'(t)·p(t) + x(t)·p'(t). Ví dụ 6: x(t) = t² + 3t (trăm đơn vị), p(t) = −2t³ᐟ² + 30 (đô la) ⇒ **R'(4) = −14** (trăm đô la/tháng).

### 2.4. Tốc độ thay đổi tương đối và phần trăm ⭐⭐⭐
- Nhiều khi tốc độ thay đổi **tương đối** quan trọng hơn tốc độ thay đổi. Cùng tăng 500 người/năm: thành phố 5 triệu dân là 500/5,000,000 = 0.0001 (0.01%), thị trấn 2,000 dân là 500/2,000 = 0.25 (25%).
- **Tương đối = Q'(x)/Q(x)**; **phần trăm = 100·Q'(x)/Q(x)**.
- Ví dụ 4: GDP N(t) = t² + 5t + 106 (tỷ đô la, t năm sau 2000) ⇒ N'(10) = **25 tỷ đô-la mỗi năm**; N(10) = 256 ⇒ tốc độ phần trăm = 100·25/256 ≈ **9.77 %/năm**.

### 2.5. Đạo hàm của hàm hợp ⭐⭐⭐
- Dẫn nhập: xe chạy 50 miles/giờ, tiêu hao 0.1 gallon/mile ⇒ (0.1 gallon/mile)(50 miles/giờ) = **5 gallons/giờ**: tốc độ thay đổi là tích các tốc độ thay đổi.
- **Định lý:** y = f(u) khả vi theo u, u = g(x) khả vi theo x ⇒ y = f[g(x)] khả vi và **dy/dx = (dy/du)·(du/dx) = f'[g(x)]·g'(x)**.
- **Cách làm đặt ẩn phụ:** đặt u = biểu thức bên trong, tính dy/du và du/dx, nhân lại, **thay u trở lại theo x**. Ví dụ 7: y = (x² + 2)³ − 3(x² + 2)² + 1, đặt u = x² + 2 ⇒ dy/dx = (3u² − 6u)(2x) = **6x⁵ + 12x³**.
- **Ứng dụng kinh tế:** chi phí theo sản lượng, sản lượng theo thời gian ⇒ tốc độ thay đổi chi phí theo thời gian dC/dt = (dC/dx)(dx/dt). Ví dụ 8: C(x) = (1/3)x² + 4x + 53, x(t) = 0.2t² + 0.03t ⇒ tại t = 4: x = 3.32, dC/dt ≈ **10.13 đô-la mỗi giờ**.

### 2.6. Đạo hàm cấp cao ⭐⭐
- **f''(x) = (f'(x))'** (ký hiệu f''(x), d²y/dx²): **tốc độ thay đổi của tốc độ thay đổi**. Cấp n: f⁽ⁿ⁾(x) = (f⁽ⁿ⁻¹⁾(x))', ký hiệu dⁿy/dxⁿ.
- Ví dụ 9: f(x) = 5x⁴ − 3x² − 3x + 7 ⇒ f'(x) = 20x³ − 6x − 3, **f''(x) = 60x² − 6**.
- **Ứng dụng:** Q(t) là sản lượng ⇒ Q'(t) là **tốc độ sản xuất**, Q''(t) là **tốc độ thay đổi của tốc độ sản xuất**. Ví dụ 10: Q(t) = −t³ + 6t² + 24t, lúc 11 giờ (t = 3) ⇒ Q'(3) = **33 đơn vị/giờ**, Q''(3) = **−6 đơn vị/giờ mỗi giờ**.

### ⚡ Dễ nhầm
- **Tốc độ thay đổi ≠ thay đổi thực tế:** P'(15) = 50 (đạo hàm, xấp xỉ) khác P(16) − P(15) = 51 (thay đổi thực tế trong tháng thứ 16). Đề hỏi "thay đổi thực tế trong tháng thứ 16" thì lấy **P(16) − P(15)**, không lấy P'(16).
- **Tương đối Q'/Q** khác **phần trăm 100·Q'/Q**: đáp án 0.0977 và 9.77% đều có thể là phương án nhiễu.
- **Đổi đơn vị biến:** 9,000 sản phẩm với x tính bằng nghìn là **x = 9**; năm 2010 với t tính từ 2000 là **t = 10**; 11 giờ sáng với t tính từ 8 giờ là **t = 3**; doanh thu (x trăm đơn vị × p đô la) tính bằng **trăm đô la** nên R'(4) = −14 là **−1,400 đô la/tháng**.
- **Quy tắc thương:** tử là **f'·g − f·g'** (thứ tự quan trọng, đảo thì đổi dấu), mẫu là **g²**. Ví dụ 5b mẫu là (2x)² = **4x²**, không phải 2x².
- **Quy tắc tích:** (f·g)' ≠ f'·g'. Ví dụ 5a: f'·g' = 1·3 = 3, sai; đúng là 6x − 5.
- **Lũy thừa âm, phân số:** d/dx(x⁻⁷) = −7x⁻⁸ (số mũ giảm 1 thành −8, không phải −6); d/dx(x⁻¹ᐟ²) = −(1/2)x⁻³ᐟ².
- **Hàm hợp:** quên nhân **du/dx** (đạo hàm phần bên trong); quên thay u trở lại theo x.
- **Ví dụ 8:** phải thay **cả x(4) = 3.32 và t = 4**, không thay x = 4 vào dC/dx.
- **Đạo hàm cấp hai** là tốc độ thay đổi **của tốc độ thay đổi**, đơn vị "đơn vị/giờ mỗi giờ"; Q''(3) = −6 nghĩa là tốc độ sản xuất đang giảm, **không** phải sản lượng đang giảm (Q'(3) = 33 > 0, sản lượng vẫn tăng).
- Slide tr. 7–8 in tiêu đề "Ý NGHĨA DẤU CỦA ĐẠO" (thiếu chữ "HÀM"). Hình Ví dụ 1 vẽ Q tại x = 9 như đỉnh nhưng đỉnh thật ở x = 8.5 (P = 16,900), P(9) = 16,800.

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Định nghĩa đạo hàm bằng giới hạn; tốc độ thay đổi trung bình và tức thời; f'(c) là độ dốc tiếp tuyến.
  - Ý nghĩa dấu: cho f'(c) hoặc cho hàm, hỏi f tăng hay giảm tại c (Ví dụ 1b, 6b).
  - Tính đạo hàm nhanh bằng quy tắc lũy thừa, tổng (Ví dụ 2), tích, thương (Ví dụ 5), hàm hợp (Ví dụ 7), cấp hai (Ví dụ 9).
  - Tính tốc độ thay đổi tại một điểm (Ví dụ 3a, 4a) hoặc tốc độ thay đổi phần trăm (Ví dụ 4b).
  - Phân biệt tốc độ thay đổi và thay đổi thực tế (Ví dụ 3b); tương đối và phần trăm.
- **Tự luận:**
  - Tính đạo hàm bằng định nghĩa rồi xét tăng/giảm: mẫu **Ví dụ 1**.
  - Tốc độ thay đổi, thay đổi thực tế, tốc độ thay đổi phần trăm của đại lượng kinh tế: mẫu **Ví dụ 3, Ví dụ 4**.
  - Lập doanh thu dạng tích theo thời gian, tính tốc độ thay đổi và kết luận tăng/giảm: mẫu **Ví dụ 6**.
  - Tốc độ thay đổi chi phí theo thời gian qua quy tắc hàm hợp: mẫu **Ví dụ 8**.
  - Tốc độ sản xuất và tốc độ thay đổi của tốc độ sản xuất (đạo hàm cấp 1, cấp 2): mẫu **Ví dụ 10**.
  - Kỹ năng đạo hàm của bài này dùng lại trong mọi bài sau (cận biên, tối ưu, co giãn ở Bài 3–5).

---

## Bài 3: Đạo hàm và vi phân của hàm số (Phần 2) — ⭐⭐⭐

> Bài giảng: TS. Lê Thị Anh. Đề cương: Bài 3 · Chương 2 · mục 2.4 (Phân tích cận biên và phép tính xấp xỉ sử dụng số gia), 2.5 (Đạo hàm của hàm ẩn và các tốc độ liên quan). Ma trận đề: Lecture 3 (Hiểu).

### Tóm tắt
- **Chi phí cận biên** MC(x₀) = C'(x₀) xấp xỉ **chi phí tăng thêm** khi tăng sản lượng từ x₀ lên x₀ + 1, tức **chi phí sản xuất đơn vị thứ x₀ + 1**.
- Tương tự: **doanh thu cận biên** R'(x₀) ≈ R(x₀ + 1) − R(x₀), **lợi nhuận cận biên** P'(x₀) ≈ P(x₀ + 1) − P(x₀).
- Dấu của lợi nhuận cận biên cho biết nên **tăng** (P' > 0) hay **giảm** (P' < 0) sản xuất (Ví dụ 2).
- **Xấp xỉ bằng số gia:** Δf ≈ f'(x₀)·Δx khi Δx nhỏ. Dùng để ước lượng mức thay đổi của hàm, hoặc ngược lại tìm Δx cần thiết để hàm tăng một lượng cho trước.
- **Thay đổi tương đối** ΔQ/Q ≈ Q'(x)·Δx/Q(x); **thay đổi phần trăm** = 100 × thay đổi tương đối.
- **Vi phân:** dx = Δx, dy = f'(x)·dx ≈ Δy.
- **Hàm ẩn:** phương trình F(x, y) = 0 xác định y = y(x) nếu mỗi x cho đúng một y. Tính dy/dx bằng cách **đạo hàm hai vế theo x, coi y là hàm của x** (quy tắc hàm hợp), rồi giải ra dy/dx.
- **Ứng dụng kinh tế của hàm ẩn:** giữ sản lượng Q(x, y) = Q₀ không đổi, khi x tăng 1 đơn vị thì y thay đổi Δy ≈ dy/dx (Ví dụ 9).
- **Các tốc độ liên quan:** x, y cùng phụ thuộc thời gian t, liên hệ bởi một phương trình. Đạo hàm hai vế theo t để nối dy/dt với dx/dt.

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Chi phí cận biên:** MC(x₀) = C'(x₀) = lim_{h→0} (C(x₀ + h) − C(x₀))/h.
- **Ý nghĩa cận biên (h = 1, x₀ đủ lớn):**
  - C'(x₀) ≈ C(x₀ + 1) − C(x₀) = chi phí sản xuất **đơn vị thứ x₀ + 1**.
  - R'(x₀) ≈ R(x₀ + 1) − R(x₀) (doanh thu cận biên, MR).
  - P'(x₀) ≈ P(x₀ + 1) − P(x₀) (lợi nhuận cận biên, MP).
- **Doanh thu:** R(x) = x·p(x) (p là giá một đơn vị). **Lợi nhuận** ký hiệu P (không phải giá).
- **Xấp xỉ bằng số gia:** f'(x₀) ≈ (f(x₀ + Δx) − f(x₀))/Δx, tương đương **Δf = f(x₀ + Δx) − f(x₀) ≈ f'(x₀)·Δx**.
- **Thay đổi tương đối:** ΔQ/Q ≈ Q'(x)·Δx/Q(x).
- **Thay đổi phần trăm:** 100·ΔQ/Q ≈ 100·Q'(x)·Δx/Q(x).
- **Vi phân:** dx = Δx; **dy = f'(x)·dx ≈ Δy**.
- **Tính dy/dx của hàm ẩn F(x, y) = 0:**
  1. Lấy đạo hàm hai vế theo x. **y là hàm của x**: (y²)' = 2y·dy/dx, (x²y)' = 2xy + x²·dy/dx, (y³)' = 3y²·dy/dx.
  2. Chuyển các số hạng chứa dy/dx về một vế, giải ra dy/dx theo x và y.
- **Quy trình bài toán các tốc độ liên quan:**
  1. Vẽ hình (nếu có thể), đặt ký hiệu các biến (t là thời gian).
  2. Thiết lập phương trình liên hệ giữa các biến.
  3. Đạo hàm hai vế theo t để có mối liên hệ giữa các tốc độ.
  4. Thay số đã cho (tìm giá trị biến còn thiếu từ phương trình gốc) để ra tốc độ cần tìm.
- **Thể tích hình cầu:** V = (4/3)πR³ (Ví dụ 12).

### 3.1. Phân tích cận biên ⭐⭐⭐
- **Chi phí cận biên** C'(x₀) là độ tăng theo **tiếp tuyến** khi x tăng 1 đơn vị. **Chi phí tăng thêm** C(x₀ + 1) − C(x₀) là độ tăng **thực** trên đường cong. Hai giá trị xấp xỉ nhau khi x₀ đủ lớn.
- **Đơn vị thứ k** ứng với x₀ = k − 1: đơn vị thứ 37 → dùng C'(36), và chi phí thực tế = C(37) − C(36).
- **Ví dụ 1:** C(x) = (1/8)x² + 3x + 98, p(x) = (1/3)(75 − x).
  - C'(x) = (1/4)x + 3; R(x) = (1/3)(75x − x²) nên R'(x) = 25 − (2/3)x.
  - Đơn vị thứ 37: ước tính C'(36) = **12**, thực tế C(37) − C(36) = 12.125 ≈ **12.13**.
  - Doanh thu: ước tính R'(36) = **1**, thực tế R(37) − R(36) = 2/3 ≈ **0.67**.
- **Ví dụ 2:** P(x) = −0.0035x³ + 0.07x² + 25x − 200 (x trăm máy ảnh, P nghìn đô la).
  - P'(x) = −0.0105x² + 0.14x + 25 (nghìn đô la/ trăm chiếc).
  - P'(10) = **25.35** > 0 → nên **tăng** sản xuất. P'(80) = **−31** < 0 → nên **giảm** sản xuất.
- Đơn vị của giá trị cận biên = đơn vị hàm / đơn vị biến (nghìn đô la/ trăm chiếc).

### 3.2. Xấp xỉ bằng số gia, thay đổi phần trăm, vi phân ⭐⭐⭐
- Công thức Δf ≈ f'(x₀)·Δx dùng được **hai chiều**:
  - Biết Δx, tìm Δf (Ví dụ 3).
  - Biết Δf, tìm Δx = Δf / f'(x₀) (Ví dụ 4).
- **Ví dụ 3:** C(q) = 3q² + 5q + 10 (q trăm đơn vị, C nghìn đô la). Từ 4,000 lên 4,050 đơn vị: q₀ = 40, Δq = 0.5. C'(q) = 6q + 5, C'(40) = 245. ΔC ≈ 245 × 0.5 = **122.5 nghìn đô la**.
- **Ví dụ 4:** Q(L) = 900L¹ᐟ³, L₀ = 1,000 giờ, cần ΔQ = 15. Q'(L) = 300L⁻²ᐟ³, Q'(1,000) = 3. ΔL ≈ 15/3 = **5 giờ**.
- **Thay đổi phần trăm** = 100·Q'(x)·Δx/Q(x): chia cho **giá trị hàm tại điểm gốc**.
- **Ví dụ 5:** N(t) = t² + 5t + 200 (t năm sau 2005). Quý 1 năm 2013: t₀ = 8, Δt = 0.25. N'(8) = 21, N(8) = 304. Phần trăm thay đổi ≈ 100 × 21 × 0.25/304 ≈ **1.73%**.
- **Vi phân:** dy = f'(x)dx là độ tăng theo tiếp tuyến, Δy là độ tăng thực của hàm; dy ≈ Δy.
- **Ví dụ 6:** f(x) = x³ − 7x² + 2 → **df = (3x² − 14x)dx**.

### 3.3. Hàm ẩn và đạo hàm của hàm ẩn ⭐⭐⭐
- **Định nghĩa:** phương trình F(x, y) = 0 (∗). Nếu với mỗi x thuộc tập X ⊂ ℝ có **duy nhất** một y thoả (∗) thì (∗) xác định **hàm ẩn** y = y(x).
- Ví dụ phương trình xác định hàm ẩn: x² + y² = 25 với y ≤ 0; eˣ + xy² + 3y = 5.
- **Ví dụ 7:** x²y + y² = x³. Đạo hàm hai vế: 2xy + x²·y' + 2y·y' = 3x² → **dy/dx = (3x² − 2xy)/(x² + 2y)**.
- **Ví dụ 8:** đường tròn x² + y² = 25. Đạo hàm: 2x + 2y·y' = 0 → y' = −x/y. Tại (3, 4): **−3/4**; tại (3, −4): **3/4**. dy/dx là **độ dốc tiếp tuyến**.
- **Ứng dụng kinh tế (Ví dụ 9):** Q = 2x³ + x²y + y³ (x giờ lao động có kỹ năng, y giờ lao động giản đơn), đang dùng (30, 20).
  - Giữ sản lượng: Q(30, 20) = **80,000**, nên 2x³ + x²y + y³ = 80,000 xác định hàm ẩn y = y(x).
  - Δx = 1 → Δy ≈ dy/dx tại (30, 20).
  - 6x² + 2xy + (x² + 3y²)·y' = 0 → y' = −(6x² + 2xy)/(x² + 3y²) = −6,600/2,100 ≈ **−3.14**: giảm khoảng 3.14 giờ lao động giản đơn.

### 3.4. Các tốc độ liên quan ⭐⭐⭐
- x, y là hàm của t; đạo hàm hai vế phương trình liên hệ **theo t** (mỗi biến đều kéo theo đạo hàm theo t của nó: (C²)' = 2C·dC/dt, (q³)' = 3q²·dq/dt).
- Trước khi thay số: **tìm giá trị biến còn lại** từ phương trình gốc, và **đổi đơn vị tốc độ** cho khớp đơn vị biến.
- **Ví dụ 10:** C² − 3q³ = 4,275 (q trăm đơn vị, C nghìn đô la). 1,500 đơn vị → q = 15 → C = 120. 20 đơn vị/tuần → dq/dt = 0.2. 2C·C' − 9q²·q' = 0 → **dC/dt ≈ 1.69 nghìn đô la/ tuần**.
- **Ví dụ 11:** x² − 2x√p − p² = 31 (x nghìn đơn vị cung, p đô la). p = 9 → x = 14. 20 cents/tuần → dp/dt = 0.2. Đạo hàm theo t, thay số → **dx/dt ≈ 0.21 nghìn đơn vị/ tuần**.
- **Ví dụ 12:** quả bóng hình cầu, V = (4/3)πR³, dV/dt = 0.002π mm³/phút, R = 0.005 mm. dV/dt = 4πR²·dR/dt → **dR/dt = 20 mm/phút**.

### ⚡ Dễ nhầm
- ⚡ **Đơn vị thứ 37 ứng với x₀ = 36**, không phải 37: ước tính bằng C'(36), thực tế = C(37) − C(36).
- ⚡ **"Ước tính" và "thực tế" khác nhau:** ước tính dùng đạo hàm (C'(36) = 12), thực tế tính hiệu hai giá trị hàm (12.13). Đề hỏi cả hai thì phải tính cả hai.
- ⚡ **Doanh thu cận biên phải đạo hàm R(x) = x·p(x)**, không đạo hàm giá p(x).
- ⚡ **P trong bài là lợi nhuận**, p là giá (Ví dụ 1 dùng p(x), Ví dụ 2 dùng P(x)).
- ⚡ **Đổi đơn vị trước khi thay số:** 4,000 → 4,050 đơn vị = q từ 40 lên 40.5 (trăm đơn vị), Δq = 0.5; 20 đơn vị/tuần = 0.2 trăm đơn vị/tuần; 20 cents = 0.2 đô la; quý 1 = 0.25 năm; 1,500 đơn vị = q = 15.
- ⚡ **Mốc thời gian:** "t năm sau kể từ năm 2005", năm 2013 → t₀ = 8 (không phải 2013 hay 9).
- ⚡ **Thay đổi phần trăm** phải **chia cho Q(x₀)** và nhân 100; chỉ tính Q'(x₀)·Δx là mới ra thay đổi tuyệt đối.
- ⚡ **Hàm ẩn:** quên nhân dy/dx khi đạo hàm số hạng chứa y (viết (y²)' = 2y là sai). Với tích x²y phải dùng **quy tắc tích**: 2xy + x²·y'.
- ⚡ **Ví dụ 9:** dy/dx âm (−3.14) nghĩa là y **giảm** khoảng 3.14 giờ; đề hỏi "số giờ cần thay đổi" thì trả lời giảm khoảng 3.14 giờ.
- ⚡ **Tốc độ liên quan:** thay số **sau khi** đạo hàm, không thay số rồi mới đạo hàm (hằng số đạo hàm bằng 0). Nghiệm âm của biến kinh tế (x = −8 ở Ví dụ 11) bị loại.
- ⚡ **Ví dụ 11:** √p là hàm của t: (x√p)' = x'·√p + x·(1/(2√p))·p'. Quên hạng tử thứ hai là sai.
- Slide Ví dụ 1c ghi "R(37) − R(36) = 0.67" bằng dấu "=", đúng ra là 2/3 ≈ 0.67; ý b ghi ≈ 12.13 (đúng 12.125). Không phải lỗi nội dung.

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Ý nghĩa của C'(x₀), R'(x₀), P'(x₀) (≈ chi phí/doanh thu/lợi nhuận của đơn vị thứ x₀ + 1).
  - Tính nhanh chi phí cận biên, doanh thu cận biên tại một mức sản lượng; ước tính chi phí đơn vị thứ k.
  - Dựa vào dấu lợi nhuận cận biên để quyết định tăng/giảm sản xuất.
  - Công thức xấp xỉ Δf ≈ f'(x₀)·Δx, thay đổi phần trăm, biểu thức vi phân df = f'(x)dx.
  - Tính dy/dx của hàm ẩn, độ dốc tiếp tuyến của đường cong ẩn tại một điểm.
- **Tự luận:**
  - Phân tích cận biên: tìm hàm MC, MR, ước tính và tính thực tế chi phí/doanh thu đơn vị thứ k (mẫu **Ví dụ 1**); lợi nhuận cận biên và quyết định sản xuất (mẫu **Ví dụ 2**).
  - Ước lượng mức thay đổi bằng số gia (mẫu **Ví dụ 3**), tìm lượng đầu vào cần bổ sung (mẫu **Ví dụ 4**), phần trăm thay đổi (mẫu **Ví dụ 5**).
  - Đạo hàm hàm ẩn (mẫu **Ví dụ 7, 8**); giữ sản lượng không đổi, tìm lượng lao động thay thế (mẫu **Ví dụ 9**).
  - Các tốc độ liên quan: chi phí theo thời gian (mẫu **Ví dụ 10**), cung theo giá (mẫu **Ví dụ 11**), thể tích hình cầu (mẫu **Ví dụ 12**).

---

## Bài 4: Một số ứng dụng của đạo hàm (Phần 1) — ⭐⭐⭐

> Bài giảng: TS. Lê Thị Anh. Đề cương: Bài 4 · Chương 3 · mục 3.1 (Hàm tăng và hàm giảm; cực trị tương đối), 3.2 (Tính lõm và điểm uốn). Ma trận đề: Lecture 4 (Vận dụng), cùng Bài 5.

### Tóm tắt
- **Hàm tăng** trên khoảng: x₂ > x₁ thì f(x₂) > f(x₁). **Hàm giảm:** x₂ > x₁ thì f(x₂) < f(x₁).
- f'(x) > 0 trên khoảng → f **tăng**; f'(x) < 0 → f **giảm**. Xét dấu f' trên các khoảng con giữa các điểm f' = 0 hoặc f' không liên tục.
- **Số tới hạn** c: thuộc tập xác định và f'(c) = 0 hoặc f'(c) không tồn tại. **Điểm tới hạn** là (c, f(c)).
- **Cực trị tương đối chỉ xảy ra tại điểm tới hạn**, nhưng không phải điểm tới hạn nào cũng là cực trị.
- **Kiểm tra bằng đạo hàm cấp một:** f' đổi dấu + → − là cực đại, − → + là cực tiểu, không đổi dấu thì không có cực trị.
- **Tính lõm:** f' tăng (f'' > 0) → bề lõm **hướng lên**, đồ thị nằm trên tiếp tuyến; f' giảm (f'' < 0) → bề lõm **hướng xuống**, đồ thị nằm dưới tiếp tuyến.
- **Điểm uốn:** điểm (c, f(c)) mà f **liên tục** và **đổi hướng lõm**; tìm tại f''(c) = 0 hoặc f''(c) không tồn tại, rồi kiểm tra f'' **đổi dấu**.
- **Kiểm tra cực trị bằng đạo hàm cấp hai:** f'(c) = 0 và f''(c) > 0 → cực tiểu; f''(c) < 0 → cực đại; f''(c) = 0 hoặc không tồn tại → chưa kết luận.
- Ứng dụng kinh tế: tìm thời điểm doanh thu tối đa (Ví dụ 3).

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Quy trình tìm khoảng tăng, giảm của f:**
  1. Tìm tập xác định. Tìm mọi x₀ có f'(x₀) = 0 hoặc f'(x₀) không liên tục; đánh dấu trên trục số, chia thành các khoảng con.
  2. Trên mỗi khoảng con chọn một số c, tính f'(c): f'(c) > 0 → f tăng trên khoảng đó; f'(c) < 0 → f giảm.
- **Kiểm tra cực trị bằng đạo hàm cấp một** (c là số tới hạn):
  - f' > 0 khi x < c và f' < 0 khi x > c → **cực đại tương đối** tại c.
  - f' < 0 khi x < c và f' > 0 khi x > c → **cực tiểu tương đối** tại c.
  - f' cùng dấu hai phía → **không có** cực trị tương đối.
- **Quy trình tìm khoảng lõm:**
  1. Tìm mọi x₀ có f''(x₀) = 0 hoặc f''(x₀) không tồn tại; chia trục số thành các khoảng con.
  2. Chọn c trên mỗi khoảng, tính f''(c): f''(c) > 0 → lõm **hướng lên**; f''(c) < 0 → lõm **hướng xuống**.
- **Quy trình tìm điểm uốn:**
  1. Tính f''(x), tìm mọi c thuộc tập xác định có f''(c) = 0 hoặc f''(c) không tồn tại.
  2. Xét dấu f'' bên trái và bên phải c. f'' **đổi dấu** qua c → (c, f(c)) là điểm uốn.
- **Kiểm tra cực trị bằng đạo hàm cấp hai** (f'' tồn tại quanh c, f'(c) = 0):
  - f''(c) > 0 → **cực tiểu** tương đối.
  - f''(c) < 0 → **cực đại** tương đối.
  - f''(c) = 0 hoặc không tồn tại → **chưa kết luận** (có thể cực đại, cực tiểu hoặc không cực trị); quay lại dùng dấu f'.
- **Quy tắc đạo hàm hay dùng trong bài:** thương (u/v)' = (u'v − uv')/v²; lũy thừa (xⁿ)' = n·xⁿ⁻¹ (kể cả n = 1/3, −2/3).

### 4.1. Hàm tăng, hàm giảm ⭐⭐⭐
- Định nghĩa trên khoảng a < x < b, x₁, x₂ bất kỳ thuộc khoảng: f tăng nếu f(x₂) > f(x₁) với mọi x₂ > x₁; f giảm nếu f(x₂) < f(x₁) với mọi x₂ > x₁.
- Hình học: f' > 0 → các tiếp tuyến có độ dốc dương, đồ thị đi lên; f' < 0 → độ dốc âm, đồ thị đi xuống.
- **Ví dụ 1:** f(x) = x²/(x − 3), D = ℝ\{3}.
  - f'(x) = x(x − 6)/(x − 3)²; f'(x) = 0 ⇔ x = 0, x = 6; thêm điểm chia x = 3 (ngoài tập xác định).
  - f'(−1) = 0.4375 > 0; f'(1) = −1.25 < 0; f'(4) = −8 < 0; f'(7) = 0.4375 > 0.
  - **Tăng** trên (−∞; 0) và (6; +∞); **giảm** trên (0; 3) và (3; 6).

### 4.2. Cực trị tương đối và kiểm tra bằng đạo hàm cấp một ⭐⭐⭐
- **Cực đại tương đối** tại c: f(x) ≤ f(c) với mọi x thuộc một khoảng chứa c. **Cực tiểu tương đối:** f(x) ≥ f(c).
- **Số tới hạn** (giá trị c) khác **điểm tới hạn** (cặp (c, f(c))).
- Minh hoạ: tại điểm f'(c) = 0 (tiếp tuyến nằm ngang) và tại điểm f'(c) không xác định (góc nhọn, tiếp tuyến thẳng đứng) đều có thể là cực đại, cực tiểu hoặc không phải cực trị.
- **Ví dụ 2:** f(x) = 2x⁴ − 4x² + 3, D = ℝ.
  - f'(x) = 8x³ − 8x = 8x(x² − 1) = 0 ⇔ x = 0, x = ±1. Ba điểm tới hạn A(−1, 1), B(0, 3), C(1, 1).
  - f'(−2) = −48 < 0; f'(−1/2) = 3 > 0; f'(1/4) = −15/8 < 0; f'(2) = 48 > 0.
  - **A, C cực tiểu tương đối; B cực đại tương đối.**
- **Ví dụ 3 (ứng dụng):** doanh thu R(t) = (63t − t²)/(t² + 63) triệu đô-la, D = [0; 63].
  - R'(t) = −63(t − 7)(t + 9)/(t² + 63)²; số tới hạn t = 7 (loại t = −9).
  - R'(1) ≃ 0.923 > 0; R'(8) ≃ −0.066 < 0 → R tăng trên (0; 7), giảm trên (7; 63).
  - Doanh thu tối đa sau **7 tuần**, R(7) = **3.5 triệu đô-la**.

### 4.3. Tính lõm và điểm uốn ⭐⭐⭐
- **Bề lõm hướng lên** ("hứng nước"): độ dốc tiếp tuyến tăng dần, đồ thị nằm **trên** tiếp tuyến, f'' > 0.
- **Bề lõm hướng xuống** ("đổ nước"): độ dốc tiếp tuyến giảm dần, đồ thị nằm **dưới** tiếp tuyến, f'' < 0.
- **Điểm uốn:** f liên tục tại c và **đổi hướng lõm**. Điểm nhọn nằm giữa hai đoạn cùng lõm hướng lên **không** phải điểm uốn.
- **Ví dụ 4:** f(x) = 2x⁶ − 5x⁴ + 7x − 3.
  - f'(x) = 12x⁵ − 20x³ + 7; f''(x) = 60x⁴ − 60x² = 60x²(x² − 1) = 0 ⇔ x = 0, ±1.
  - f''(−2) = 720 > 0; f''(−1/2) = −45/4 < 0; f''(1/2) = −45/4 < 0; f''(5) = 36,000 > 0.
  - **Lõm lên** khi x < −1 hoặc x > 1; **lõm xuống** khi −1 < x < 0 hoặc 0 < x < 1.
- **Ví dụ 5a:** f(x) = 3x⁵ − 5x⁴ − 1. f''(x) = 60x³ − 60x² = 60x²(x − 1) = 0 tại x = 0, 1. f''(−1) = −120, f''(0.5) = −7.5, f''(2) = 240. f'' chỉ đổi dấu tại x = 1 → **một điểm uốn (1, −3)**; x = 0 có f'' = 0 nhưng **không** phải điểm uốn.
- **Ví dụ 5b:** g(x) = x¹ᐟ³. g'(x) = (1/3)x⁻²ᐟ³; g''(x) = −(2/9)x⁻⁵ᐟ³, luôn khác 0, không tồn tại tại x = 0. g'' đổi dấu qua 0 → **điểm uốn (0, 0)**.

### 4.4. Kiểm tra cực trị bằng đạo hàm cấp hai ⭐⭐⭐
- Điều kiện: f'(c) = 0 và f'' tồn tại trên khoảng mở chứa c.
- Hình: (a) cực đại f'(c) = 0, f''(c) < 0; (b) cực tiểu f'(c) = 0, f''(c) > 0; (c) f'(c) = 0, f''(c) = 0 không kết luận (đồ thị dạng bậc ba, không cực trị).
- **Ví dụ 6:** f(x) = 2x³ + 3x² − 12x − 7.
  - f'(x) = 6x² + 6x − 12 = 6(x + 2)(x − 1); f''(x) = 12x + 6.
  - Điểm tới hạn (−2, 13) và (1, −14).
  - f''(−2) = −18 < 0 → **(−2, 13) cực đại**; f''(1) = 18 > 0 → **(1, −14) cực tiểu**.

### ⚡ Dễ nhầm
- ⚡ **Số tới hạn phải thuộc tập xác định.** Ví dụ 1: x = 3 ngoài tập xác định, chỉ dùng để chia khoảng, không phải số tới hạn, không phải cực trị.
- ⚡ **Điểm tới hạn chưa chắc là cực trị**: phải kiểm tra f' đổi dấu (hoặc dấu f'').
- ⚡ **f''(c) > 0 là cực TIỂU, f''(c) < 0 là cực ĐẠI** (lõm lên "hứng nước" thì đáy là cực tiểu). Hay nhớ ngược.
- ⚡ **f''(c) = 0 chưa chắc là điểm uốn**: phải xét f'' đổi dấu. Ví dụ 5a: x = 0 có f''(0) = 0 nhưng f'' âm cả hai phía → không phải điểm uốn.
- ⚡ **Điểm uốn có thể ở chỗ f'' không tồn tại** (Ví dụ 5b, g(x) = x¹ᐟ³ tại x = 0).
- ⚡ **f''(c) = 0 thì kiểm tra cấp hai không kết luận được**; khi đó quay lại xét dấu f'.
- ⚡ **Điểm uốn ghi đủ tọa độ** (c, f(c)): (1, −3), (0, 0); khoảng lõm ghi theo x.
- ⚡ **Ví dụ 3:** slide lấy tập xác định D = [0; 63], nên loại t = −9. ⚠️ (bổ sung) Vì R tăng trên (0; 7) và giảm trên (7; 63) nên cực đại tương đối tại t = 7 cũng là giá trị lớn nhất trên [0; 63].
- ⚡ **Slide in nhầm (Ví dụ 2, tr. 12):** slide ghi f'(−2) = −64, đúng là **−48**. Dấu vẫn âm, kết luận không đổi.
- ⚡ **Slide in nhầm (Ví dụ 5b, tr. 21):** slide ghi g''(−1) = −2/9 < 0 và g''(1) = 1/3 > 0. Đúng là **g''(−1) = 2/9 > 0** (lõm lên khi x < 0) và **g''(1) = −2/9 < 0** (lõm xuống khi x > 0). Kết luận điểm uốn (0, 0) không đổi.

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Định nghĩa hàm tăng, giảm; số tới hạn, điểm tới hạn; điều kiện cực đại, cực tiểu theo dấu f' và dấu f''.
  - Cho hàm đa thức hoặc phân thức: chọn khoảng tăng/giảm đúng, số điểm tới hạn, điểm cực đại/cực tiểu.
  - Khoảng lõm hướng lên/xuống, số điểm uốn, tọa độ điểm uốn.
  - Phát biểu đúng/sai: "f''(c) = 0 thì c là điểm uốn", "mọi điểm tới hạn đều là cực trị", "f''(c) > 0 thì cực đại".
- **Tự luận:**
  - Tìm khoảng tăng, giảm của hàm phân thức (mẫu **Ví dụ 1**).
  - Tìm số tới hạn và phân loại cực trị bằng đạo hàm cấp một (mẫu **Ví dụ 2**) hoặc cấp hai (mẫu **Ví dụ 6**).
  - Bài toán ứng dụng: thời điểm doanh thu tối đa, giá trị tối đa (mẫu **Ví dụ 3**); kết hợp với tối ưu hoá Bài 5.
  - Tìm khoảng lõm (mẫu **Ví dụ 4**) và điểm uốn, kể cả điểm f'' không tồn tại (mẫu **Ví dụ 5**).

---

## Bài 5: Một số ứng dụng của đạo hàm (Phần 2) — ⭐⭐⭐

> Bài giảng: TS. Đoàn Trọng Tuyến. Đề cương: Bài 4 · Chương 3 · mục 3.3 (Tối ưu hoá; Độ co giãn của cầu), 3.4 (Các bài toán tối ưu hoá ứng dụng khác). Ma trận đề: Lecture 4 (Vận dụng) + câu tổng hợp "bài toán tối ưu kinh tế một biến".

### Tóm tắt
- **Cực trị tuyệt đối** = giá trị lớn nhất / nhỏ nhất của hàm trên **cả khoảng I**, khác cực trị tương đối (chỉ so với lân cận).
- Hàm **liên tục trên đoạn đóng** [a, b] luôn đạt cực trị tuyệt đối, tại **điểm mút** hoặc tại **số tới hạn** bên trong (tính chất giá trị cực biên).
- Tìm cực trị tuyệt đối trên đoạn đóng: **3 bước** — tìm số tới hạn trong (a, b), tính f tại số tới hạn và hai mút, so sánh.
- Khoảng **không đóng** (ví dụ x > 0): nếu chỉ có **duy nhất một số tới hạn** thì dùng **đạo hàm cấp hai** để kết luận cực trị tuyệt đối.
- **Lợi nhuận tối đa:** **R'(q) = C'(q)** và **R''(q) < C''(q)** (doanh thu cận biên = chi phí cận biên).
- **Chi phí bình quân tối thiểu:** **A(q) = C'(q)** (chi phí bình quân = chi phí cận biên).
- **Độ co giãn của cầu theo giá:** **E(p) = −(p/q)·(dq/dp)** ≈ % giảm của cầu khi giá tăng 1%. So E với **1**: > 1 co giãn, < 1 không co giãn, = 1 co giãn đơn vị.
- **Liên hệ doanh thu:** **R'(p) = q(p)[1 − E(p)]**. Cầu không co giãn thì tăng giá làm **doanh thu tăng**; cầu co giãn thì tăng giá làm **doanh thu giảm**; co giãn đơn vị thì doanh thu **đạt tối đa**.
- Bài toán tối ưu ứng dụng giải theo **5 bước**: đặt tên đại lượng, lập quan hệ, đưa về **một biến** kèm miền giới hạn, tìm số tới hạn và kiểm tra (cả điểm mút), diễn giải kết quả.

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Cực đại tuyệt đối** tại c trên I: f(c) ≥ f(x) với mọi x ∈ I. **Cực tiểu tuyệt đối**: f(c) ≤ f(x) với mọi x ∈ I.
- **Thủ tục tìm cực trị tuyệt đối trên đoạn a ≤ x ≤ b:**
  1. Tìm tất cả số tới hạn của f trong khoảng mở a < x < b (giải f'(x) = 0 hoặc f'(x) không xác định; **loại** số tới hạn nằm ngoài khoảng).
  2. Tính f tại các số tới hạn đó và tại **hai mút** x = a, x = b.
  3. Giá trị **lớn nhất** = cực đại tuyệt đối; giá trị **nhỏ nhất** = cực tiểu tuyệt đối.
- **Kiểm tra cực trị tuyệt đối bằng đạo hàm cấp hai** (f liên tục trên I, c là số tới hạn **duy nhất**, f'(c) = 0):
  - f''(c) > 0 ⟹ f(c) là **cực tiểu tuyệt đối** trên I.
  - f''(c) < 0 ⟹ f(c) là **cực đại tuyệt đối** trên I.
- **Lợi nhuận:** P(q) = R(q) − C(q), R(q) = q·p(q). Tối đa khi **R'(q) = C'(q)** và **R''(q) < C''(q)**.
- **Chi phí bình quân:** A(q) = C(q)/q. Tối thiểu khi **A(q) = C'(q)**.
- **Độ co giãn của cầu theo giá:** **E(p) = −(p/q)·(dq/dp)**, q = D(p).
  - E(p) > 1: **cầu co giãn** (% giảm cầu > % tăng giá).
  - E(p) < 1: **cầu không co giãn** (% giảm cầu < % tăng giá).
  - E(p) = 1: **cầu co giãn đơn vị**.
- **Doanh thu theo giá:** R(p) = p·q(p) ⟹ **R'(p) = q(p) + p·(dq/dp) = q(p)[1 − E(p)]**.
  - E < 1 ⟹ R'(p) > 0: tăng giá thì **R tăng**.
  - E > 1 ⟹ R'(p) < 0: tăng giá thì **R giảm**.
  - E = 1 ⟹ R'(p) = 0: R không đổi với mức tăng giá nhỏ (**đỉnh** của R(p)).
- **5 bước giải bài toán tối ưu hoá:**
  1. Chọn đại lượng cần tối ưu, đặt tên các biến (chữ gợi nhớ: R doanh thu, P ô nhiễm/lợi nhuận…).
  2. Viết quan hệ giữa các biến (phương trình, bất phương trình; có thể vẽ hình).
  3. Biểu diễn đại lượng cần tối ưu theo **một biến**, xác định **miền giới hạn** của biến.
  4. Tính đạo hàm, tìm số tới hạn; dùng định lý giá trị cực biên (so cả **điểm mút**) hoặc đạo hàm cấp hai.
  5. Diễn giải kết quả theo đại lượng kinh tế / hình học / vật lý.

### 5.1. Cực trị tuyệt đối ⭐⭐⭐
- **Định nghĩa** (tr. 4): f xác định trên I chứa c; f(c) là cực đại (cực tiểu) tuyệt đối nếu f(c) ≥ f(x) (≤ f(x)) với mọi x ∈ I. Gọi chung là **cực trị tuyệt đối**.
- **Tính chất giá trị cực biên** (tr. 5): f liên tục trên đoạn đóng a ≤ x ≤ b thì đạt cực trị tuyệt đối **tại một điểm mút** (a hoặc b) **hoặc tại một số tới hạn c** với a < c < b. Bốn hình: cực đại tuyệt đối tại cực đại tương đối / tại mút phải; cực tiểu tuyệt đối tại cực tiểu tương đối / tại mút trái.
- Tr. 20 gọi cùng nội dung này là **"định lý giá trị cực biên"**.
- **Ví dụ 1:** f(x) = 2x³ + 3x² − 12x − 7 trên −3 ≤ x ≤ 0. f'(x) = 6(x + 2)(x − 1), **loại x = 1**. f(−3) = 2, f(−2) = 13, f(0) = −7 ⟹ **max = 13** tại x = −2, **min = −7** tại x = 0 (min nằm ở **điểm mút**).

### 5.2. Bài toán tối ưu tổng quát; kiểm tra bằng đạo hàm cấp hai ⭐⭐
- **Bài toán tối ưu tổng quát** (tr. 8): tìm cực trị tuyệt đối của f liên tục trên khoảng I, **I không nhất thiết đóng**.
- **Chú ý:** trên I, f chỉ có **duy nhất** một số tới hạn c và f có cực đại (cực tiểu) tương đối tại c thì đó cũng là cực đại (cực tiểu) **tuyệt đối**.
- Khoảng không đóng có thể **không có** cực đại hoặc cực tiểu tuyệt đối.
- **Ví dụ 2:** f(x) = x² + 16/x, x > 0. f'(x) = 2x − 16/x² = 0 ⟹ x = 2 (duy nhất). f''(x) = 2 + 32/x³, f''(2) = 6 > 0 ⟹ **f(2) = 12 là cực tiểu tuyệt đối**, **không có cực đại tuyệt đối**.

### 5.3. Hai nguyên lý tổng quát của phân tích cận biên ⭐⭐⭐
- **Lợi nhuận tối đa** (tr. 10): P(q) = R(q) − C(q) tối đa tại q mà **doanh thu cận biên = chi phí cận biên** và **tốc độ thay đổi của chi phí cận biên lớn hơn tốc độ thay đổi của doanh thu cận biên**: R'(q) = C'(q), R''(q) < C''(q).
- **Chi phí bình quân tối thiểu** (tr. 10): A(q) = C(q)/q tối thiểu tại q mà **chi phí bình quân = chi phí cận biên**: A(q) = C'(q).
- **Ví dụ 3** (Adam Goodman): p(q) = 22.2 − 1.2q, C(q) = 0.4q² + 3q + 40 (q nghìn đơn vị, C nghìn đô la).
  - R(q) = −1.2q² + 22.2q; R' = −2.4q + 22.2; C' = 0.8q + 3. R' = C' ⟹ **q = 6** ⟹ **6,000 đơn vị** (R'' = −2.4 < C'' = 0.8).
  - A(q) = 0.4q + 3 + 40/q = C'(q) = 0.8q + 3 ⟹ **q = 10** ⟹ **10,000 đơn vị**.

### 5.4. Độ co giãn của cầu theo giá và doanh thu ⭐⭐⭐
- **Công thức** (tr. 13): q = D(p) khả vi, **E(p) = −(p/q)(dq/dp)** ≈ phần trăm giảm của cầu gây ra bởi 1% tăng giá.
- **Các mức** (tr. 14): E > 1 cầu **co giãn** (nhạy cảm với giá); E < 1 cầu **không co giãn** (tương đối không nhạy cảm); E = 1 **co giãn đơn vị** (% thay đổi cầu ≈ % thay đổi giá).
- **Liên hệ doanh thu** (tr. 17): từ E(p) suy ra p·(dq/dp) = −q(p)·E(p), nên R'(p) = q(p) + p·(dq/dp) = **q(p)[1 − E(p)]**. Đồ thị R(p) dạng parabol úp: nhánh tăng = cầu không co giãn, đỉnh = co giãn đơn vị, nhánh giảm = cầu co giãn.
- **Ví dụ 4** (cửa hàng sách): q = 300 − p², 0 ≤ p ≤ √300.
  - E(p) = 2p²/(300 − p²); **E(5) ≈ 0.18**: giá tăng 1% thì cầu giảm ≈ 0.18%.
  - E = 1 ⟺ **p = 10**; 0 ≤ p < 10: không co giãn (doanh thu tăng); 10 < p ≤ √300: co giãn (doanh thu giảm); p = 10: doanh thu **tối đa**.

### 5.5. Bài toán tối ưu hoá ứng dụng ⭐⭐⭐
- Giải theo **5 bước** (tr. 19–20); bài giảng gộp **B2 & B3**: viết thẳng hàm một biến → Min/Max.
- **Luôn xác định miền của biến** (Ví dụ 5: 1 ≤ x ≤ 14; Ví dụ 6: 0 ≤ x ≤ 15) và **so giá trị tại điểm mút**.
- **Ví dụ 5** (ô nhiễm hai nhà máy): P(x) = 75/x + 300/(15 − x), 1 ≤ x ≤ 14. P'(x) = 0 ⟹ x = 5; P(1) ≈ 96.43, **P(5) = 45**, P(14) ≈ 305.36 ⟹ nhà cách A **5 dặm**, ô nhiễm **45 ppm**.
- **Ví dụ 6** (xe buýt): R(x) = (35 + x)(60 − x), 0 ≤ x ≤ 15. R'(x) = 25 − 2x = 0 ⟹ x = 12.5, **không nguyên** ⟹ xét x = 12, 13: R = **2,256** ⟹ nhóm **47 hoặc 48 người**, doanh thu tối đa **$2,256**.

### ⚡ Dễ nhầm
- ⚡ **Quên điểm mút:** cực trị tuyệt đối trên đoạn đóng có thể nằm ở mút (Ví dụ 1: min = f(0) = −7 ở mút phải).
- ⚡ **Không loại số tới hạn ngoài khoảng:** Ví dụ 1 có x = 1 nhưng không thuộc −3 < x < 0.
- ⚡ **Khoảng mở / nửa vô hạn** có thể **không có** cực đại tuyệt đối (Ví dụ 2). Đạo hàm cấp hai chỉ kết luận được "tuyệt đối" khi số tới hạn là **duy nhất**.
- ⚡ **Đơn vị "nghìn":** Ví dụ 3 q tính bằng **nghìn đơn vị** → đáp số 6,000 và 10,000, không phải 6 và 10.
- ⚡ **Hai tiêu chuẩn cận biên:** lợi nhuận tối đa là **R' = C'** (cận biên = cận biên); chi phí bình quân tối thiểu là **A = C'** (bình quân = cận biên). Đừng đảo.
- ⚡ Điều kiện bậc hai của lợi nhuận là **R'' < C''**, không phải R'' > C''.
- ⚡ **Dấu trừ trong E(p):** bài giảng định nghĩa E(p) = −(p/q)(dq/dp) nên E là **số dương** với cầu giảm; so sánh với **1**, không phải −1.
- ⚡ **Co giãn và doanh thu:** cầu **không co giãn** (E < 1) thì **tăng giá → doanh thu tăng**; cầu **co giãn** (E > 1) thì tăng giá → doanh thu **giảm**. Hay nhầm ngược.
- ⚡ **Biến là "số vượt quá":** Ví dụ 6 x là số người **vượt quá 35** → quy mô nhóm = 35 + x = 47 hoặc 48, không phải 12 hoặc 13.
- ⚡ **Nghiệm không nguyên:** x = 12.5 người không hợp lệ → xét hai số nguyên kề 12 và 13.
- ⚡ Ví dụ 4: tại p = √300 thì q = 0, E(p) không xác định (mẫu 300 − p² = 0); slide vẫn ghi "10 < p ≤ √300". Chi tiết biên, không ảnh hưởng kết luận.

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Tìm cực đại / cực tiểu tuyệt đối của đa thức trên một đoạn (dạng Ví dụ 1); bẫy: quên mút, không loại số tới hạn ngoài khoảng.
  - Hàm trên khoảng x > 0 có cực tiểu / cực đại tuyệt đối không, giá trị bao nhiêu (dạng Ví dụ 2).
  - Điều kiện lợi nhuận tối đa (R' = C', R'' < C''), điều kiện chi phí bình quân tối thiểu (A = C').
  - Tính nhanh q tối đa lợi nhuận / tối thiểu chi phí bình quân khi cho p(q), C(q).
  - Tính E(p) tại một mức giá, phân loại co giãn / không co giãn / đơn vị; tìm mức giá co giãn đơn vị.
  - Tăng giá thì doanh thu tăng hay giảm khi biết E (E < 1 tăng, E > 1 giảm, E = 1 đạt max).
- **Tự luận:**
  - Tối đa lợi nhuận và tối thiểu chi phí bình quân (mẫu: **Ví dụ 3**) — đúng dạng câu tổng hợp "bài toán tối ưu kinh tế một biến".
  - Độ co giãn của cầu: lập E(p), tính tại p cho trước, giải thích ý nghĩa, xác định miền co giãn, liên hệ doanh thu (mẫu: **Ví dụ 4**).
  - Bài toán tối ưu ứng dụng theo 5 bước, nhớ miền biến và điểm mút (mẫu: **Ví dụ 5** ô nhiễm, **Ví dụ 6** doanh thu xe buýt).

---

## Bài 6: Phép toán tích phân (Phần 1) — ⭐⭐⭐

> Bài giảng: TS. Đoàn Trọng Tuyến. Đề cương: Bài 5 · Chương 4 · mục 4.1 (Tích phân bất định và phương trình vi phân), 4.2 (Tính tích phân bằng phương pháp đổi biến), 4.3 (Tích phân xác định và định lý cơ bản của giải tích). Ma trận đề: Lecture 5 (Nhớ). Là nền cho câu tổng hợp ứng dụng tích phân (thặng dư, Gini, giá trị hiện tại/tương lai…).

### Tóm tắt
- **Nguyên hàm** F của f: **F'(x) = f(x)**. Hai nguyên hàm của cùng một hàm chỉ khác nhau **một hằng số C**.
- **Tích phân bất định** ∫ f(x) dx = F(x) + C là **họ tất cả** các nguyên hàm.
- Tính tích phân bất định bằng **6 quy tắc**: hằng, lũy thừa (n ≠ −1), logarit, mũ, nhân với hằng số, tổng/hiệu.
- **Tìm hàm tổng khi biết đạo hàm** (chi phí cận biên → chi phí, tốc độ thay đổi giá → hàm cầu): lấy tích phân rồi dùng **một điều kiện cho trước** để tìm C.
- **Phương pháp đổi biến** (4 bước): đặt u = u(x), tính du, đưa về ∫ g(u) du, tính rồi **thay u lại theo x**.
- **Tích phân xác định** ∫ₐᵇ f(x) dx = giới hạn của **tổng Riemann**; với f ≥ 0 là **diện tích** miền dưới đường cong.
- **Định lý cơ bản của giải tích:** ∫ₐᵇ f(x) dx = **F(b) − F(a)**.
- Tính chất tích phân xác định: nhân hằng số, tổng/hiệu, cận trùng nhau = 0, đổi cận đổi dấu, **phân đoạn**.
- Đổi biến trong tích phân xác định: cách 1 tìm nguyên hàm rồi thay cận theo x; cách 2 **đổi cận** theo u.
- **Thay đổi ròng:** Q(b) − Q(a) = ∫ₐᵇ Q'(x) dx (tổng chi phí tăng thêm, khối lượng thay đổi…).
- ⚠️ Đề cương mục 4.1 có "phương trình vi phân" nhưng bài giảng Bài 6 (Phần 1) **không có nội dung này** (cần xác minh ở bài khác).

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Nguyên hàm:** F'(x) = f(x), ∀x ∈ D. Mọi nguyên hàm có dạng **F(x) + C**. ∫ F'(x) dx = F(x) + C.
- **Quy tắc tích phân bất định:**
  - Hằng: **∫ k dx = kx + C**
  - Lũy thừa: **∫ xⁿ dx = xⁿ⁺¹/(n + 1) + C**, n ≠ −1
  - Logarit: **∫ (1/x) dx = ln|x| + C**, x ≠ 0
  - Mũ: **∫ eᵏˣ dx = eᵏˣ/k + C**, k ≠ 0
  - Nhân với hằng số: ∫ k·f(x) dx = k ∫ f(x) dx
  - Tổng, hiệu: ∫ [f(x) ± g(x)] dx = ∫ f(x) dx ± ∫ g(x) dx
- **Đổi căn, phân thức thành lũy thừa trước khi tích phân:** √x = x¹ᐟ², 1/(x√x) = x⁻³ᐟ², 1/x² = x⁻².
- **Tìm hàm tổng từ đạo hàm:**
  1. F(x) = ∫ F'(x) dx = (nguyên hàm) + C.
  2. Thay điều kiện cho trước (ví dụ C(2) = 900, p(4) = 30) để tìm C.
  3. Viết hàm hoàn chỉnh, thay số theo yêu cầu.
- **Phương pháp đổi biến ∫ f(x) dx:**
  1. Chọn u = u(x) làm hàm lấy tích phân đơn giản hơn.
  2. Tính du = u'(x) dx, viết f(x) dx = g(u) du.
  3. Tính ∫ g(u) du = G(u) + C.
  4. Thay u = u(x): ∫ f(x) dx = G(u(x)) + C.
- **Gợi ý chọn u:** u'(x) là một phần của hàm lấy tích phân; u là biểu thức **dưới dấu căn**, **mẫu thức**, **số mũ** của hàm mũ, **lũy thừa của ngoặc**; không chọn u là toàn bộ hàm lấy tích phân.
- **Tổng Riemann:** Δx = (b − a)/n, **∫ₐᵇ f(x) dx = lim_{n→+∞} [f(x₁) + f(x₂) + ⋯ + f(xₙ)]Δx**.
- **Định lý cơ bản của giải tích:** f liên tục trên [a, b], F là một nguyên hàm ⟹ **∫ₐᵇ f(x) dx = F(x)|ₐᵇ = F(b) − F(a)**.
- **Quy tắc tích phân xác định:**
  - ∫ₐᵇ k·f(x) dx = k ∫ₐᵇ f(x) dx
  - ∫ₐᵇ [f(x) ± g(x)] dx = ∫ₐᵇ f(x) dx ± ∫ₐᵇ g(x) dx
  - **∫ₐᵃ f(x) dx = 0**
  - **∫_b^a f(x) dx = −∫ₐᵇ f(x) dx** (đổi chỗ cận thì đổi dấu)
  - **Phân đoạn:** ∫ₐᵇ f(x) dx = ∫ₐᶜ f(x) dx + ∫_c^b f(x) dx
- **Đổi biến trong tích phân xác định:** cách 1 — tìm nguyên hàm theo x rồi thay cận a, b; cách 2 — đặt u = g(x), **đổi cận** theo u rồi tính luôn theo u.
- **Diện tích dưới đường cong** (f ≥ 0, liên tục trên [a, b]): **S = ∫ₐᵇ f(x) dx**.
- **Thay đổi ròng:** **Q(b) − Q(a) = ∫ₐᵇ Q'(x) dx**.

### 6.1. Nguyên hàm và tích phân bất định ⭐⭐⭐
- **Định nghĩa** (tr. 4): F là nguyên hàm của f trên D nếu F'(x) = f(x) (dF/dx = f(x)) ∀x ∈ D. Đồ thị các nguyên hàm là **họ đường cong song song** (cùng hệ số góc tiếp tuyến tại mỗi x), ví dụ x³, x³ + π, x³ − 5 đều là nguyên hàm của 3x².
- **Định lý** (tr. 6): F là một nguyên hàm của f liên tục ⟹ mọi nguyên hàm có dạng G(x) = F(x) + C.
- **Tích phân bất định** ∫ f(x) dx = F(x) + C. Thành phần: ∫ dấu tích phân; f(x) **hàm lấy tích phân**; x **biến lấy tích phân**; C **hằng số tích phân**.
- **Ví dụ 1:** kiểm tra nguyên hàm bằng cách **lấy đạo hàm**: (x³/3 + x²/2 + x + 2025)' = x² + x + 1; (F(x) + C)' = F'(x) = f(x).
- **Ví dụ 2:** ∫ x¹⁵ dx = x¹⁶/16 + C; ∫ 2/(3x√x) dx = −(4/3)x⁻¹ᐟ² + C; ∫ e⁻⁵ˣ dx = e⁻⁵ˣ/(−5) + C; ∫ (x³ + 2x − 7)/x dx = x³/3 + 2x − 7 ln|x| + C (chia tử cho x trước).

### 6.2. Tìm hàm tổng khi biết hàm cận biên / tốc độ thay đổi ⭐⭐⭐
- Mục tiêu bài học: "giải bài toán tìm hàm tổng nếu biết đạo hàm".
- Hàm cận biên là đạo hàm ⟹ hàm tổng là **tích phân bất định** của hàm cận biên, hằng số C xác định nhờ **một điểm đã biết**.
- **Ví dụ 3:** C'(q) = 3q² − 60q + 400, C(2) = 900 ⟹ C(q) = q³ − 30q² + 400q + 212 ⟹ **C(5) = $1,587**. Slide ký hiệu hằng số là **C̄** để khỏi nhầm với hàm chi phí C(q).
- **Ví dụ 6:** dp/dx = −135x/√(9 + x²), p(4) = 30 (x đo bằng **trăm** đơn vị) ⟹ p(x) = −135√(9 + x²) + 705; p(3) = $132.24; p(0) = $300; p = 20 ⟹ x ≈ 4.09 ⟹ **≈ 409 đơn vị**.

### 6.3. Phương pháp đổi biến ⭐⭐⭐
- **Dẫn nhập** (tr. 10): ∫ x⁷ dx dễ, nhưng ∫ (2x + 3)⁷ dx cần **đổi biến** u = 2x + 3.
- **4 bước** (tr. 11) và **gợi ý chọn u** (tr. 12): xem mục Công thức.
- **Ví dụ 4:** u = 2x + 3, dx = du/2 ⟹ ∫ (2x + 3)⁷ dx = **(2x + 3)⁸/16 + C**.
- **Ví dụ 5:**
  - ∫ √(2x + 7) dx, u = 2x + 7 ⟹ **(1/3)(2x + 7)³ᐟ² + C** (⚡ slide ghi 2/3, in nhầm).
  - ∫ 8x(4x² − 3)⁵ dx, u = 4x² − 3, du = 8x dx ⟹ **(4x² − 3)⁶/6 + C**.
  - ∫ (ln x)²/x dx, u = ln x, du = dx/x ⟹ **(ln x)³/3 + C**.

### 6.4. Tích phân xác định, định lý cơ bản, diện tích ⭐⭐⭐
- **Diện tích bằng giới hạn** (tr. 16): xấp xỉ diện tích dưới y = f(x) bằng các hình chữ nhật; càng nhiều đoạn con càng chính xác (Hình 4.6: 6 và 24 đoạn con).
- **Định nghĩa tích phân xác định** (tr. 17): giới hạn của tổng Riemann khi n → +∞. a, b là **cận dưới, cận trên**.
- **Định lý cơ bản của giải tích** (tr. 18): ∫ₐᵇ f(x) dx = F(b) − F(a).
- **Ví dụ 7:** thửa đất dưới y = x³ + 1, 0 ≤ x ≤ 1 (trăm feet): S = ∫₀¹ (x³ + 1) dx = 5/4 = 1.25 ⟹ **12,500 ft²**.
- **Ví dụ 8:** diện tích dưới y = 2x + 1 trên 1 ≤ x ≤ 3: **S = 10**.
- **Ví dụ 9:** ∫₀¹ (e⁻ˣ + √x) dx = **5/3 − 1/e**; ∫₁⁴ (1/x − x²) dx = **ln 4 − 21 ≈ −19.6137**.
- **Quy tắc tích phân xác định** (tr. 21). **Ví dụ 10:** ∫₋₂⁵ f = 3, ∫₋₂⁵ g = −4, ∫₃⁵ f = 7 ⟹ ∫₋₂⁵ [2f − 3g] = **18**; ∫₋₂³ f = 3 − 7 = **−4**.
- **Đổi biến trong tích phân xác định** (tr. 23), **phải đổi cận** nếu tính theo u. **Ví dụ 11:** ∫₀¹ 8x(x² + 1)³ dx = **15** (cách 1); ∫_{1/4}^{2} (ln x/x) dx = ∫_{ln(1/4)}^{ln 2} u du **≈ −0.721** (cách 2).

### 6.5. Thay đổi ròng ⭐⭐⭐
- **Công thức** (tr. 25): Q' liên tục trên [a, b] ⟹ Q(b) − Q(a) = ∫ₐᵇ Q'(x) dx. Biết tốc độ thay đổi (cận biên) ⟹ tính được **mức thay đổi** mà **không cần tìm hằng số C**.
- **Ví dụ 12:** C'(q) = 3(q − 4)², q từ 6 lên 10 ⟹ C(10) − C(6) = (q − 4)³|₆¹⁰ = **$208**.
- **Ví dụ 13:** dm/dt = −30/(t + 3)², 2 giờ đầu ⟹ m(2) − m(0) = **−4** (giảm 4 g).

### ⚡ Dễ nhầm
- ⚡ **Quên + C** ở tích phân bất định.
- ⚡ **Quy tắc lũy thừa không dùng cho n = −1**: ∫ x⁻¹ dx = ln|x| + C, không phải x⁰/0.
- ⚡ **∫ eᵏˣ dx = eᵏˣ/k**, chia cho k (k âm thì kết quả có dấu âm: ∫ e⁻⁵ˣ dx = −e⁻⁵ˣ/5 + C); hay nhầm thành nhân k (đó là đạo hàm).
- ⚡ **Tích phân của thương ≠ thương các tích phân:** ∫ (x³ + 2x − 7)/x dx phải **chia tử cho x** trước, không lấy ∫ tử / ∫ mẫu.
- ⚡ **Đổi biến quên hệ số du:** u = 2x + 7 ⟹ dx = du/2, kết quả phải nhân 1/2. **Slide Ví dụ 5a in nhầm** (2/3)(2x + 7)³ᐟ² + C; đúng là **(1/3)(2x + 7)³ᐟ² + C** (đạo hàm của bản 2/3 bằng 2√(2x + 7), gấp đôi hàm lấy tích phân). Có thể gặp làm phương án nhiễu.
- ⚡ **Slide Ví dụ 4 in nhầm** bước trung gian "(1/2) ∫ u⁸ du"; đúng là (1/2) ∫ u⁷ du = u⁸/16. Kết quả cuối (2x + 3)⁸/16 + C vẫn đúng.
- ⚡ **Quên thay u lại theo x** ở tích phân bất định.
- ⚡ **Đổi biến trong tích phân xác định theo cách 2 mà không đổi cận** (Ví dụ 11b, Ví dụ 13 phải đổi cận sang u).
- ⚡ **Đổi cận đổi dấu:** ∫_b^a f = −∫ₐᵇ f; **phân đoạn**: ∫₋₂³ f = ∫₋₂⁵ f − ∫₃⁵ f (trừ, không cộng).
- ⚡ **Tích phân xác định có thể âm** (Ví dụ 9b ≈ −19.6137, Ví dụ 11b ≈ −0.721, Ví dụ 13 = −4); chỉ là diện tích khi f ≥ 0.
- ⚡ **Đơn vị:** Ví dụ 6 x đo bằng **trăm** đơn vị (cầu 300 đơn vị ⟹ x = 3; x ≈ 4.09 ⟹ 409 đơn vị); Ví dụ 7 x, y đo bằng **trăm feet** ⟹ nhân 100 × 100.
- ⚡ **Hằng số C̄** ở Ví dụ 3 là hằng số tích phân, khác hàm chi phí C(q). Tìm C̄ từ C(2) = 900, không phải từ C(0).
- ⚡ **Thay đổi ròng** = Q(b) − Q(a), **không phải** Q(b): tính "tổng chi phí tăng bao nhiêu" thì không cần biết chi phí cố định.

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Hàm nào là nguyên hàm của f (lấy đạo hàm kiểm tra); nhận biết các thành phần của ∫ f(x) dx.
  - Tính nhanh tích phân bất định bằng 6 quy tắc: lũy thừa có căn/phân thức, eᵏˣ, 1/x (dạng Ví dụ 2).
  - Đổi biến cơ bản: (ax + b)ⁿ, √(ax + b), u'·uⁿ, (ln x)ⁿ/x (dạng Ví dụ 4, 5); bẫy thiếu hệ số 1/a.
  - Tính tích phân xác định bằng định lý cơ bản (dạng Ví dụ 8, 9, 11); diện tích dưới đường cong.
  - Dùng tính chất tích phân xác định (nhân hằng số, tổng/hiệu, đổi cận, phân đoạn) khi cho sẵn giá trị tích phân (dạng **Ví dụ 10**).
  - Thay đổi ròng: tổng chi phí tăng bao nhiêu khi q tăng từ a đến b (dạng Ví dụ 12).
- **Tự luận:**
  - Tìm hàm tổng chi phí từ chi phí cận biên và một điều kiện, rồi tính chi phí tại mức sản lượng khác (mẫu: **Ví dụ 3**).
  - Tìm hàm cầu từ tốc độ thay đổi giá bằng đổi biến, tính giá tại mức cầu cho trước và cầu tại mức giá cho trước (mẫu: **Ví dụ 6**).
  - Tính diện tích thực tế (đổi đơn vị) bằng tích phân xác định (mẫu: **Ví dụ 7**).
  - Thay đổi ròng của chi phí / đại lượng khi biết tốc độ thay đổi (mẫu: **Ví dụ 12, 13**).

---

## Bài 7: Phép toán tích phân (Phần 2) — Các ứng dụng của tích phân — ⭐⭐⭐

> Bài giảng: TS. Tống Thành Trung. Đề cương: Bài 6 · Chương 4 · mục 4.4 Ứng dụng của tích phân xác định: phân phối thu nhập và giá trị trung bình · 4.5 Các ứng dụng khác của tích phân trong kinh doanh và kinh tế học. Ma trận đề: Lecture 6 (Hiểu); các ứng dụng này cũng là nội dung **câu tổng hợp** (CLO 3.2: thặng dư, Gini, giá trị hiện tại/tương lai, lợi nhuận vượt trội ròng).

### Tóm tắt
- Bài bày **7 ứng dụng** của tích phân xác định, mỗi ứng dụng đều quy về **một tích phân ∫ₐᵇ** rồi thay số.
- **Diện tích giữa hai đường cong:** A = ∫ₐᵇ [f(x) − g(x)] dx, đường **trên** trừ đường **dưới**, cận là **hoành độ giao điểm**.
- **Lợi nhuận vượt trội ròng:** NE = ∫₀ᴺ [P₂'(t) − P₁'(t)] dt, N là lúc hai **tốc độ sinh lợi** bằng nhau.
- **Đường cong Lorenz** L(x) nằm dưới **đường bình đẳng tuyệt đối** y = x; **chỉ số Gini** GI = 2∫₀¹ [x − L(x)] dx, nằm giữa 0 và 1, **càng nhỏ càng công bằng**.
- **Giá trị trung bình** của f trên [a, b]: V = (1/(b − a)) ∫ₐᵇ f(x) dx.
- **Dòng thu nhập** tính lãi gộp liên tục: **FV = ∫₀ᵀ f(t)e^{r(T − t)} dt**, **PV = ∫₀ᵀ f(t)e^{−rt} dt**. Giá trị ròng của dự án = PV − chi phí ban đầu.
- **Mức sẵn lòng chi tiêu** WS = ∫₀^{q₀} D(q) dq (diện tích dưới đường cầu).
- **Thặng dư người tiêu dùng** CS = ∫₀^{q₀} D(q) dq − p₀q₀; **thặng dư nhà sản xuất** PS = p₀q₀ − ∫₀^{q₀} S(q) dq; (q₀, p₀) thường là **điểm cân bằng** S(q) = D(q).

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Diện tích giữa hai đường cong** (f(x) ≥ g(x) trên [a, b]): **A = ∫ₐᵇ [f(x) − g(x)] dx**.
  1. Giải f(x) = g(x) tìm hoành độ giao điểm → cận a, b.
  2. Xác định đường nào nằm trên (thử một điểm giữa a và b).
  3. Tính ∫ₐᵇ [trên − dưới] dx.
- **Lợi nhuận vượt trội ròng** (P₂'(t) ≥ P₁'(t) trên 0 ≤ t ≤ N): E(t) = P₂(t) − P₁(t); **NE = E(N) − E(0) = ∫₀ᴺ [P₂'(t) − P₁'(t)] dt**.
  1. Giải P₂'(t) = P₁'(t) (hoặc bất phương trình P₂'(t) > P₁'(t)) → N, loại nghiệm âm.
  2. Tính ∫₀ᴺ [P₂'(t) − P₁'(t)] dt, giữ đơn vị của đề (ví dụ "trăm đô la").
- **Đường cong Lorenz** y = L(x), 0 ≤ x ≤ 1: đồng biến; 0 ≤ L(x) ≤ 1; L(0) = 0; L(1) = 1; L(x) ≤ x.
- **Chỉ số Gini:** **GI = Diện tích R₁ / Diện tích R₂ = 2∫₀¹ [x − L(x)] dx** (R₂ là tam giác dưới y = x, diện tích 1/2). 0 ≤ GI ≤ 1.
  1. Tính ∫₀¹ [x − L(x)] dx.
  2. Nhân 2.
  3. So sánh: GI nhỏ hơn → phân phối **công bằng hơn**.
- **Giá trị trung bình:** **V = (1/(b − a)) ∫ₐᵇ f(x) dx**.
- **Giá trị tương lai** của dòng thu nhập f(t) trong T năm, lãi suất r gộp liên tục: **FV = ∫₀ᵀ f(t) e^{r(T − t)} dt**.
- **Giá trị hiện tại:** **PV = ∫₀ᵀ f(t) e^{−rt} dt**.
- **Giá trị ròng** của dự án đầu tư trong T năm: **PV − C** (C là chi phí ban đầu). Chọn dự án có giá trị ròng lớn hơn.
- Nguyên hàm hay dùng: ∫ e^{kt} dt = e^{kt}/k + C; ∫₀ᵀ e^{−kt} dt = (1 − e^{−kT})/k.
- **Mức sẵn lòng chi tiêu:** **WS = ∫₀^{q₀} D(q) dq**.
- **Thặng dư của người tiêu dùng:** **CS = ∫₀^{q₀} D(q) dq − p₀q₀** = [sẵn lòng chi] − [chi thực tế].
- **Thặng dư của nhà sản xuất:** **PS = p₀q₀ − ∫₀^{q₀} S(q) dq** = [nhận thực tế] − [sẵn lòng chấp nhận].
  1. Giải S(q) = D(q) → q₀ (loại nghiệm âm).
  2. p₀ = D(q₀) = S(q₀) (thay vào cả hai hàm để kiểm tra).
  3. Tính CS, PS theo công thức; đơn vị = đơn vị của q × đơn vị của p.

### 7.1. Diện tích của miền giữa hai đường cong ⭐⭐
- Nếu f, g liên tục trên [a, b] và f(x) ≥ g(x) với mọi x ∈ [a, b] thì A = ∫ₐᵇ [f(x) − g(x)] dx.
- Hình học: miền R giữa hai đường = R₁ (dưới y = f(x)) − R₂ (dưới y = g(x)).
- Ví dụ 1: y = x³ và y = x² cắt nhau tại x = 0, x = 1; trên [0, 1] đường y = x² nằm trên ⇒ A = ∫₀¹ (x² − x³) dx = **1/12**.

### 7.2. Lợi nhuận vượt trội ròng ⭐⭐⭐
- Hai dự án sinh lợi P₁(t), P₂(t) sau t năm; **tốc độ sinh lợi** P₁'(t), P₂'(t).
- **E(t) = P₂(t) − P₁(t)** là lợi nhuận vượt trội của dự án 2 so với dự án 1 tại thời điểm t.
- **NE = E(N) − E(0) = ∫₀ᴺ [P₂'(t) − P₁'(t)] dt** = diện tích miền giữa y = P₂'(t) (trên) và y = P₁'(t) (dưới) từ 0 đến N; N là điểm hai đường cắt nhau.
- Ví dụ 2: P₁'(t) = 50 + t², P₂'(t) = 200 + 5t (trăm đô la/năm) ⇒ dự án 2 sinh lợi nhanh hơn trong **15 năm**; NE = **1,687.5 trăm đô la = $168,750**.

### 7.3. Đường cong Lorenz và chỉ số Gini ⭐⭐⭐
- **Đường cong Lorenz** L(x), 0 ≤ x ≤ 1: tỷ lệ thu nhập mà **100x% người làm công được trả lương thấp nhất** nhận được trong tổng thu nhập quốc dân hàng năm. Ví dụ: 30% người thu nhập thấp nhất nhận 23% tổng thu nhập ⇒ L(0.3) = 0.23.
- Tính chất (L đồng biến):
  1. 0 ≤ L(x) ≤ 1 (là tỷ lệ phần trăm).
  2. L(0) = 0 (không ai làm thì không có thu nhập từ lương).
  3. L(1) = 1 (100% người làm công tạo ra 100% thu nhập từ lương).
  4. L(x) ≤ x (100x% người lương thấp nhất không thể nhận quá 100x% tổng thu nhập).
- **Đường bình đẳng tuyệt đối** y = x: 100x% người lương thấp nhất nhận đúng 100x% thu nhập. Lorenz luôn nằm **dưới** đường này; **càng gần** y = x thì phân phối **càng công bằng**.
- **Chỉ số Gini** (chỉ số bất bình đẳng thu nhập): R₁ = miền giữa y = x và y = L(x) trên [0, 1]; R₂ = miền dưới y = x trên [0, 1]. **GI = R₁/R₂ = 2∫₀¹ [x − L(x)] dx**.
- Gini luôn trong [0, 1]; **càng nhỏ càng công bằng**; **càng lớn** thì của cải càng tập trung vào một số ít người.
- Ví dụ 3: nha sỹ L₁(x) = x^{1.7} ⇒ GI₁ = **0.2593**; nhà thầu L₂(x) = 0.8x² + 0.2x ⇒ GI₂ = **0.2667** ⇒ thu nhập **nha sỹ công bằng hơn**.

### 7.4. Giá trị trung bình của hàm số ⭐⭐
- f liên tục trên [a, b]: **V = (1/(b − a)) ∫ₐᵇ f(x) dx**.
- Ví dụ 4: doanh số S(t) = 750t/√(4t² + 25) nghìn đô la, 6 tháng đầu ⇒ ∫₀⁶ S(t) dt = 1,500 ⇒ V = **250 nghìn đô la/tháng** (tích phân tính bằng đổi biến u = 4t² + 25, xem Bài 6).

### 7.5. Giá trị tương lai và giá trị hiện tại của dòng thu nhập ⭐⭐⭐
- **Dòng thu nhập (Income stream):** doanh thu từ hoạt động kinh doanh, coi như dòng liên tục, có thể đem đầu tư để tạo thêm thu nhập.
- **Giá trị tương lai** của dòng thu nhập trong một khoảng thời gian = tổng số tiền tích luỹ (tiền chuyển vào tài khoản + tiền lãi) trong khoảng đó.
- **Niên kim (Annuity):** dòng thu nhập đặc biệt, thanh toán (nhận hoặc trả) theo **khoảng thời gian đều đặn** trong một **thời hạn xác định**. Ví dụ: lương hưu, trả góp mua xe hằng tháng, thanh toán thế chấp nhà.
- Tiền chuyển liên tục vào tài khoản với tốc độ f(t) trong 0 ≤ t ≤ T, lãi suất năm r gộp liên tục:
  - **FV = ∫₀ᵀ f(t) e^{r(T − t)} dt**
  - **PV = ∫₀ᵀ f(t) e^{−rt} dt**
- **Giá trị ròng** của dự án trong T năm = PV − chi phí ban đầu (nêu trong lời giải Ví dụ 6).
- Ví dụ 5: niên kim 1,200 đô la/năm, r = 8%, T = 2 ⇒ FV ≈ **2,602.66 đô la**.
- Ví dụ 6: dự án 1 (chi 9,000; f₁ = 3,000e^{0.03t}) giá trị ròng **5,274.39**; dự án 2 (chi 12,000; f₂ = 4,000) giá trị ròng **5,695.94**; r = 5%, T = 5 ⇒ **chọn dự án 2**.

### 7.6. Mức sẵn lòng chi tiêu của người tiêu dùng ⭐⭐
- p = D(q) là hàm cầu. **Tổng mức sẵn lòng chi tiêu để mua đến q₀ đơn vị:** **WS = ∫₀^{q₀} D(q) dq**.
- Hình học: diện tích miền **dưới đường cầu** trên [0; q₀].
- Ví dụ 7: p = 10(25 − q²) đô la/tấn, 3 tấn ⇒ WS = **660 đô la**.

### 7.7. Thặng dư của người tiêu dùng và thặng dư của nhà sản xuất ⭐⭐⭐
- q₀ đơn vị bán với giá p₀; D(q) là hàm cầu, S(q) là hàm cung.
- **CS = ∫₀^{q₀} D(q) dq − p₀q₀** = [tổng tiền người tiêu dùng sẵn lòng chi cho q₀ đơn vị] − [tiền chi trả thực tế]. Hình học: miền giữa đường cầu (trên) và đường p = p₀ (dưới) trên [0; q₀].
- **PS = p₀q₀ − ∫₀^{q₀} S(q) dq** = [tiền nhà sản xuất thực nhận khi cung q₀ đơn vị] − [tiền sẵn lòng chấp nhận]. Hình học: miền giữa đường p = p₀ (trên) và đường cung (dưới) trên [0; q₀].
- Điểm cân bằng: S(q₀) = D(q₀) = p₀.
- Ví dụ 8: D(q) = −0.1q² + 90, S(q) = 0.2q² + q + 50 (q nghìn lốp, p đô la/chiếc) ⇒ q₀ = **10** nghìn lốp, p₀ = **80** đô la; CS ≈ **66.67**, PS ≈ **183.33** nghìn đô la.

### ⚡ Dễ nhầm
- **Thứ tự trừ** trong diện tích: luôn lấy đường **trên** trừ đường **dưới**. Ví dụ 1 trên [0, 1] thì x² ≥ x³ (x² nằm trên), lấy ngược ra −1/12.
- **Đơn vị Ví dụ 2:** 1,687.5 là **trăm đô la** = **$168,750**. Đọc "1,687.5" theo kiểu bài giảng: một nghìn sáu trăm tám mươi bảy phẩy năm.
- **Cận N** của lợi nhuận vượt trội ròng là lúc hai **tốc độ** P₁'(t), P₂'(t) bằng nhau, không phải lúc P₁(t) = P₂(t). Loại nghiệm âm (Ví dụ 2 loại t = −10).
- **Gini quên nhân 2:** ∫₀¹ [x − L(x)] dx chỉ là diện tích R₁; GI = R₁/(1/2) = 2 × tích phân.
- **Gini lớn = bất công hơn.** So sánh hai ngành thì ngành có Gini **nhỏ** hơn là **công bằng hơn**.
- **FV và PV:** FV dùng e^{r(T − t)}, PV dùng e^{−rt}. ⚠️ (nhận xét, không có trong bài giảng) FV = PV·e^{rT}.
- **Gộp mũ ở Ví dụ 6:** e^{0.03t}·e^{−0.05t} = e^{−0.02t}, không phải e^{0.08t} hay e^{−0.08t}.
- **Giá trị ròng** phải trừ chi phí ban đầu; chỉ so PV là chưa đủ.
- **WS và CS:** WS chỉ là ∫₀^{q₀} D(q) dq; CS = WS − p₀q₀. **CS và PS ngược dấu:** CS = tích phân − p₀q₀, PS = p₀q₀ − tích phân.
- **Đơn vị Ví dụ 8:** q tính bằng **nghìn** lốp nên CS, PS tính bằng **nghìn đô la**.
- **Giá trị trung bình** phải **chia cho (b − a)**; Ví dụ 4 quên chia ra 1,500 thay vì 250.
- ⚡ Slide tr. 10: mẫu số của công thức Gini bị chữ che; dùng GI = Diện tích R₁ / Diện tích R₂ = 2∫₀¹ [x − L(x)] dx (khớp lời giải Ví dụ 3).

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Công thức nào là FV / PV / CS / PS / WS / giá trị trung bình / Gini (nhận dạng đúng mũ e, đúng dấu trừ).
  - Tính chất đường cong Lorenz (L(0) = 0, L(1) = 1, L(x) ≤ x, đồng biến); ý nghĩa L(0.3) = 0.23.
  - Gini nằm trong [0, 1]; Gini nhỏ hơn thì công bằng hơn; so sánh hai Gini cho trước.
  - Tính nhanh: diện tích giữa hai đường cong đơn giản (Ví dụ 1), WS với hàm cầu bậc hai (Ví dụ 7), giá trị trung bình, FV của niên kim hằng số (Ví dụ 5).
  - Định nghĩa niên kim, dòng thu nhập, lợi nhuận vượt trội E(t).
- **Tự luận:**
  - Lợi nhuận vượt trội ròng: tìm N rồi tính NE, biểu diễn bằng diện tích (mẫu: Ví dụ 2).
  - Tính Gini của hai phân phối và so sánh (mẫu: Ví dụ 3).
  - Giá trị trung bình của doanh số (mẫu: Ví dụ 4).
  - Giá trị tương lai của niên kim (mẫu: Ví dụ 5); so sánh hai dự án bằng giá trị ròng PV − C (mẫu: Ví dụ 6).
  - Tìm điểm cân bằng, tính CS và PS (mẫu: Ví dụ 8); mức sẵn lòng chi tiêu (mẫu: Ví dụ 7).

---

## Bài 8: Một số chủ đề chọn lọc về tích phân (Phần 1) — ⭐⭐

> Bài giảng: TS. Tống Thành Trung. Đề cương: Bài 7 · Chương 5 · mục 5.1 Tích phân từng phần; bảng tích phân. Ma trận đề: Lecture 7 (Nhớ), chung với Bài 9.

### Tóm tắt
- **Tích phân từng phần** suy ra từ đạo hàm của tích (uv)' = u'v + uv': **∫ u dv = uv − ∫ v du**.
- Phương pháp gồm 3 bước: **chọn u, dv** → **tính du, v** → **áp dụng công thức**, cuối cùng thêm **+ C**.
- Chọn **u** sao cho **du đơn giản hơn u** (ln x, đa thức); chọn **dv** sao cho **∫dv dễ tính** (xⁿ dx, e^{kx} dx, dx).
- Với tích phân xác định: **∫ₐᵇ u dv = uv|ₐᵇ − ∫ₐᵇ v du**.
- Ứng dụng: tính **diện tích** (∫₁ᵉ ln x dx = 1) và **giá trị tương lai** của dòng thu nhập dạng đa thức × mũ (FV ≈ $17,274).
- **Bảng tích phân** (Bảng 5.1) gồm 25 công thức chia 5 nhóm: a + bu; a² + u²; a² − u²; u² − a²; e^{au} và ln u. Cách dùng: biến đổi hàm về đúng dạng, xác định a, b, u rồi thay vào.
- **Phương trình logistic** dQ/dt = kQ(M − Q): mô hình hoá lây lan dịch bệnh, lan truyền tin đồn, tăng trưởng dân số. Giải bằng **tách biến** + **công thức 6** của bảng + **điều kiện ban đầu**.

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Tích phân từng phần (bất định):** **∫ u dv = uv − ∫ v du**.
- **Tích phân từng phần (xác định):** **∫ₐᵇ u dv = uv|ₐᵇ − ∫ₐᵇ v du**, với F(x)|ₐᵇ = F(b) − F(a).
- **Các bước của phương pháp tích phân từng phần:**
  1. Chọn u và dv sao cho f(x)dx = u dv (du đơn giản hơn u; ∫dv dễ tính).
  2. Lập sơ đồ: { u = … ; dv = … } ⟹ { du = u' dx ; v = ∫ dv }.
  3. Áp dụng ∫ f(x) dx = ∫ u dv = uv − ∫ v du; tính ∫ v du và thêm **+ C** (tích phân xác định thì thay cận, không có C).
- **Cách chọn u trong các ví dụ:** u = ln x (Ví dụ 1, 3); u = đa thức (2x + 1 ở Ví dụ 2; 3,000 + 50t ở Ví dụ 4); dv là phần còn lại (x² dx, dx, e^{3x} dx, e^{0.04(5 − t)} dt).
- **Nguyên hàm cần cho v:** ∫ e^{kx} dx = e^{kx}/k; ∫ e^{0.04(5 − t)} dt = e^{0.04(5 − t)}/(−0.04) = −25e^{0.04(5 − t)}.
- **Bảng tích phân hay dùng** (đủ 25 công thức ở mục 8.3):
  - (6) ∫ du/(u(a + bu)) = (1/a) ln|u/(a + bu)| + C
  - (16) ∫ du/(a² − u²) = (1/(2a)) ln|(a + u)/(a − u)| + C
  - (22) ∫ u e^{au} du = (1/a²)(au − 1)e^{au} + C
  - (23) ∫ ln u du = u ln u − u + C
  - (25) ∫ uᵐ ln u du = (u^{m+1}/(m + 1))(ln u − 1/(m + 1)) + C, m ≠ −1
- **Phương trình logistic:** **dQ/dt = kQ(M − Q)** (k, M là hằng số). Các bước giải:
  1. Tách biến: dQ/(Q(M − Q)) = k dt, lấy tích phân hai vế.
  2. Dùng công thức 6 với u = Q, a = M, b = −1: (1/M) ln|Q/(M − Q)| = kt + C₁.
  3. Nhân M, mũ hoá: Q/(M − Q) = Ce^{kMt}.
  4. Rút Q: Q(t) = MCe^{kMt}/(1 + Ce^{kMt}).
  5. Thay điều kiện ban đầu Q(0) tìm C.

### 8.1. Phương pháp tích phân từng phần đối với tích phân bất định ⭐⭐⭐
- Xuất phát: (uv)' = u'v + uv' (1), u = u(x), v = v(x) khả vi. Lấy tích phân hai vế: ∫ (uv)' dx = ∫ u'v dx + ∫ uv' dx, hay uv = ∫ v du + ∫ u dv ⇒ **∫ u dv = uv − ∫ v du** (2).
- 3 bước: chọn u, dv → tính du = u' dx, v = ∫ dv → áp dụng công thức, tính ∫ v du và thêm "+ C".
- Ví dụ 1: ∫ x² ln x dx, chọn u = ln x, dv = x² dx ⇒ **(1/3)x³ ln x − (1/9)x³ + C** (trùng công thức 25 với m = 2).

### 8.2. Phương pháp tích phân từng phần đối với tích phân xác định ⭐⭐⭐
- **∫ₐᵇ u dv = uv|ₐᵇ − ∫ₐᵇ v du**, F(x)|ₐᵇ = F(b) − F(a).
- Ví dụ 2: I = ∫₀¹ (2x + 1)e^{3x} dx, u = 2x + 1, dv = e^{3x} dx ⇒ **I = (7e³ − 1)/9** ≈ 15.51.
- Ví dụ 3 (diện tích): miền giới hạn bởi y = ln x, trục hoành, x = e; ln x ≥ 0 trên [1, e] ⇒ A = ∫₁ᵉ ln x dx, u = ln x, dv = dx ⇒ **A = 1**.
- Ví dụ 4 (ứng dụng kinh tế): FV của dòng thu nhập 3,000 + 50t đô la/năm, r = 4%, T = 5 ⇒ FV = ∫₀⁵ (3,000 + 50t)e^{0.04(5 − t)} dt, u = 3,000 + 50t, dv = e^{0.04(5 − t)} dt ⇒ **FV ≈ 17,274.04** (≈ $17,274). Công thức FV lấy từ Bài 7.

### 8.3. Bảng tích phân (Bảng 5.1) ⭐⭐
- **Nhóm a + bu** (công thức 1–8):
  1. ∫ u du/(a + bu) = (1/b²)[a + bu − a ln|a + bu|] + C
  2. ∫ u² du/(a + bu) = (1/(2b³))[(a + bu)² − 4a(a + bu) + 2a² ln|a + bu|] + C
  3. ∫ u du/(a + bu)² = (1/b²)[a/(a + bu) + ln|a + bu|] + C
  4. ∫ u du/√(a + bu) = (2/(3b²))(bu − 2a)√(a + bu) + C
  5. ∫ du/(u√(a + bu)) = (1/√a) ln|(√(a + bu) − √a)/(√(a + bu) + √a)| + C, a > 0
  6. ∫ du/(u(a + bu)) = (1/a) ln|u/(a + bu)| + C
  7. ∫ du/(u²(a + bu)) = (−1/a)[1/u + (b/a) ln|u/(a + bu)|] + C
  8. ∫ du/(u²(a + bu)²) = (−1/a²)[(a + 2bu)/(u(a + bu)) + (2b/a) ln|u/(a + bu)|] + C
- **Nhóm a² + u²** (9–13):
  9. ∫ √(a² + u²) du = (u/2)√(a² + u²) + (a²/2) ln|u + √(a² + u²)| + C
  10. ∫ du/√(a² + u²) = ln|u + √(a² + u²)| + C
  11. ∫ du/(u√(a² + u²)) = (−1/a) ln|(√(a² + u²) + a)/u| + C
  12. ∫ du/(a² + u²)^{3/2} = u/(a²√(a² + u²)) + C
  13. ∫ u²√(a² + u²) du = (u/8)(a² + 2u²)√(a² + u²) − (a⁴/8) ln|u + √(a² + u²)| + C
- **Nhóm a² − u²** (14–17):
  14. ∫ du/(u√(a² − u²)) = (−1/a) ln|(a + √(a² − u²))/u| + C
  15. ∫ du/(u²√(a² − u²)) = −√(a² − u²)/(a²u) + C
  16. ∫ du/(a² − u²) = (1/(2a)) ln|(a + u)/(a − u)| + C
  17. ∫ (√(a² − u²)/u) du = √(a² − u²) − a ln|(a + √(a² − u²))/u| + C
- **Nhóm u² − a²** (18–21):
  18. ∫ √(u² − a²) du = (u/2)√(u² − a²) − (a²/2) ln|u + √(u² − a²)| + C
  19. ∫ (√(u² − a²)/u²) du = −√(u² − a²)/u + ln|u + √(u² − a²)| + C
  20. ∫ du/√(u² − a²) = ln|u + √(u² − a²)| + C
  21. ∫ du/(u²√(u² − a²)) = √(u² − a²)/(a²u) + C
- **Nhóm e^{au} và ln u** (22–25):
  22. ∫ u e^{au} du = (1/a²)(au − 1)e^{au} + C
  23. ∫ ln u du = u ln u − u + C
  24. ∫ du/(u ln u) = ln|ln u| + C
  25. ∫ uᵐ ln u du = (u^{m+1}/(m + 1))(ln u − 1/(m + 1)) + C, m ≠ −1
- Cách dùng: đưa hàm dưới dấu tích phân về đúng dạng (rút hệ số ra ngoài), nhận ra nhóm, xác định a (b) và u, thay vào.
- Ví dụ 5: 1/(6 − 3x²) = (1/3)·1/(2 − x²), dạng a² − u² với **a = √2**, u = x ⇒ công thức 16 ⇒ ∫ dx/(6 − 3x²) = **(1/3)(1/(2√2)) ln|(√2 + x)/(√2 − x)| + C**.

### 8.4. Phương trình logistic ⭐⭐
- **Phương trình logistic:** phương trình vi phân **dQ/dt = kQ(M − Q)**, k và M là hằng số.
- Đồ thị nghiệm y = Q(t) gọi là **đường cong logistic**.
- Ứng dụng: mô hình hoá **sự lây lan của dịch bệnh**, **sự lan truyền tin đồn**, **tăng trưởng dân số** và nhiều vấn đề khác.
- Ví dụ 6: dN/dt = 0.025N(26 − N), N(0) = 2 ⇒ **N(t) = 26e^{0.65t}/(12 + e^{0.65t})**; N(6) ≈ 21 ⇒ đến trưa còn **5** nhân viên chưa nghe tin đồn.

### ⚡ Dễ nhầm
- **Chọn ngược u và dv:** với ∫ x² ln x dx mà chọn u = x², dv = ln x dx thì phải tính ∫ ln x dx trước, bài toán phức tạp hơn. Có ln x thì chọn **u = ln x**.
- **Quên + C** ở tích phân bất định; tích phân xác định thì **không** có C nhưng phải thay **cả hai cận** cho cả uv và ∫ v du.
- **Sai dấu v** ở Ví dụ 4: v = e^{0.04(5 − t)}/(−0.04) = **−25**e^{0.04(5 − t)} (đạo hàm của 0.04(5 − t) theo t là −0.04).
- **Xác định a trong bảng:** 2 − x² ứng với a² = 2 nên **a = √2**, không phải a = 2. Nhớ hệ số **1/3** rút ra ngoài.
- **Hệ số mũ trong logistic:** sau khi nhân hai vế với M = 26, số mũ là kM = 0.025 × 26 = **0.65**, không phải 0.025.
- **Đọc đúng câu hỏi Ví dụ 6:** hỏi số người **chưa** nghe ⇒ 26 − 21 = **5**, không phải 21. Giữa trưa là **t = 6** (tính từ 6 giờ sáng), không phải t = 12.
- ⚡ Slide tr. 7–8 ghi tiêu đề "Tính tích phân **bất định** bằng phương pháp tích phân từng phần" nhưng nội dung là tích phân **xác định** (tiêu đề giữ nguyên từ slide trước).
- ⚡ Công thức 25 trên slide thiếu "+ C" (thiếu sót trình bày).

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Công thức tích phân từng phần (bất định, xác định); cách chọn u, dv cho một tích phân cho trước.
  - Tính nhanh nguyên hàm dạng xⁿ ln x, ln x, (đa thức)·e^{kx}; nhận ra công thức nào trong bảng tích phân phù hợp (xác định a, b, u).
  - Dạng tổng quát của phương trình logistic; phương trình logistic dùng để mô hình hoá gì.
- **Tự luận:**
  - Tính tích phân bất định bằng từng phần (mẫu: Ví dụ 1); tích phân xác định bằng từng phần (mẫu: Ví dụ 2).
  - Diện tích miền phẳng cần từng phần (mẫu: Ví dụ 3).
  - Giá trị tương lai/hiện tại của dòng thu nhập dạng đa thức (mẫu: Ví dụ 4) — kết hợp với Bài 7.
  - Dùng bảng tích phân (mẫu: Ví dụ 5).
  - Giải phương trình logistic có điều kiện ban đầu và tính giá trị tại một thời điểm (mẫu: Ví dụ 6).

---

## Bài 9: Một số chủ đề tích phân chọn lọc (Phần 2) — ⭐⭐

> Bài giảng: TS. Đặng Huy Ngân (slide bìa: "Một số chủ đề chọn lọc về tích phân"). Đề cương: Bài 7 · Chương 5 · mục 5.2 Tính gần đúng tích phân xác định · 5.3 Tích phân suy rộng (mục 5.1 Tích phân từng phần nằm ở Bài 8). Ma trận đề: Lecture 7 (Nhớ, chung với Bài 8).

### Tóm tắt
- Hai cách **tính gần đúng** ∫ₐᵇ f(x) dx: **quy tắc hình thang** (hệ số 1, 2, 2, …, 2, 1, nhân Δx/2) và **quy tắc Simpson** (hệ số 1, 4, 2, 4, …, 2, 4, 1, nhân Δx/3, **n chẵn**).
- Cả hai đều chia [a, b] thành **n đoạn con bằng nhau**, Δx = (b − a)/n, điểm chia đánh số **x₁ = a, …, xₙ₊₁ = b** (n + 1 điểm).
- Khi chỉ có **số liệu đo** tại các điểm cách đều (không có công thức hàm), dùng quy tắc hình thang trên **bảng số liệu** (Ví dụ 3, bể bơi: **320 feet vuông**).
- **Tích phân suy rộng** = giới hạn của tích phân xác định khi cận chạy ra vô cùng: ∫ₐ^{+∞} = lim_{N→+∞} ∫ₐᴺ, ∫_{−∞}ᵇ = lim_{N→−∞} ∫_Nᵇ.
- Giới hạn tồn tại **hữu hạn** → **hội tụ**; không tồn tại hoặc bằng vô hạn → **phân kỳ**.
- Giới hạn hay dùng: **lim_{N→+∞} Nᵖe^{−kN} = 0** (mọi p thực, k > 0).
- Hai cận vô hạn: tách tại một điểm c, **I = I₁ + I₂**, chỉ hội tụ khi **cả hai** tích phân thành phần hội tụ.
- Ứng dụng: tỷ lệ thiết bị **tồn tại lâu hơn t tháng** = ∫_t^{+∞} 0.008e^{−0.008x} dx; tỷ lệ **hỏng trong vòng không quá T** = 1 − tỷ lệ tồn tại lâu hơn T.

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Độ rộng đoạn con:** Δx = (b − a)/n. Điểm chia: x₁ = a < x₂ < ⋯ < xₙ < xₙ₊₁ = b, xₖ = a + (k − 1)Δx.
- **Quy tắc hình thang** (n nguyên dương bất kỳ):
  - ∫ₐᵇ f(x) dx ≈ Tₙ = (Δx/2)·[f(x₁) + 2f(x₂) + ⋯ + 2f(xₙ) + f(xₙ₊₁)].
  - Hệ số: **hai đầu mút 1, các điểm bên trong 2**.
  - Tₙ là tổng diện tích n hình thang: ½[f(xₖ) + f(xₖ₊₁)]Δx. ∫ₐᵇ f(x) dx = lim_{n→∞} Tₙ.
- **Quy tắc Simpson** (n nguyên dương **chẵn**):
  - ∫ₐᵇ f(x) dx ≈ Sₙ = (Δx/3)·[f(x₁) + 4f(x₂) + 2f(x₃) + 4f(x₄) + ⋯ + 2f(xₙ₋₁) + 4f(xₙ) + f(xₙ₊₁)].
  - Hệ số: **1, 4, 2, 4, 2, …, 2, 4, 1** (hai đầu 1, điểm chỉ số chẵn x₂, x₄, … hệ số 4, điểm chỉ số lẻ bên trong x₃, x₅, … hệ số 2).
  - Sₙ là tổng diện tích dưới n/2 parabol, mỗi parabol qua 3 điểm của một cặp đoạn con: ⅓[f(xₖ) + 4f(xₖ₊₁) + f(xₖ₊₂)]Δx. ∫ₐᵇ f(x) dx = lim_{n→∞} Sₙ.
- **Các bước tính gần đúng:**
  1. Kiểm tra f liên tục trên [a, b].
  2. Tính Δx = (b − a)/n, liệt kê n + 1 điểm chia.
  3. Tính f tại từng điểm chia.
  4. Nhân hệ số (hình thang 1, 2, …, 2, 1; Simpson 1, 4, 2, …, 4, 1), cộng lại, nhân Δx/2 (hình thang) hoặc Δx/3 (Simpson).
- **Tích phân suy rộng cận trên vô hạn:** ∫ₐ^{+∞} f(x) dx = lim_{N→+∞} ∫ₐᴺ f(x) dx.
- **Tích phân suy rộng cận dưới vô hạn:** ∫_{−∞}ᵇ f(x) dx = lim_{N→−∞} ∫_Nᵇ f(x) dx.
- **Hội tụ / phân kỳ:** giới hạn tồn tại hữu hạn → hội tụ; không tồn tại hoặc bằng ∞ → phân kỳ.
- **Ý nghĩa hình học:** nếu f(x) ≥ 0 thì tích phân suy rộng là diện tích hình phẳng (không bị chặn) dưới đường cong f(x).
- **Giới hạn thường dùng:** lim_{N→+∞} Nᵖe^{−kN} = 0 với mọi p thực, k > 0. Hệ quả: lim_{N→+∞} e^{−kN} = 0, lim_{N→−∞} e^{kN} = 0 (k > 0).
- **Các bước tính I = ∫_{−∞}^{+∞} f(x) dx:**
  1. Chọn số c bất kỳ thuộc ℝ (thường c = 0).
  2. Tính tích phân bất định ∫ f(x) dx.
  3. Tính I₁ = ∫_{−∞}^c f(x) dx và I₂ = ∫_c^{+∞} f(x) dx. Nếu **cả hai** hội tụ thì **I = I₁ + I₂**.
- **Ứng dụng (Ví dụ 8):** ∫_t^{+∞} 0.008e^{−0.008x} dx = e^{−0.008t}; "tỷ lệ tồn tại lâu hơn T" + "tỷ lệ hỏng trong vòng không quá T" = 1.
- ⚠️ Bổ sung ngoài bài giảng (hay dùng để kiểm tra nhanh): ∫₁^{+∞} dx/xᵖ hội tụ khi p > 1 (bằng 1/(p − 1)), phân kỳ khi p ≤ 1; ∫₀^{+∞} e^{−kx} dx = 1/k (k > 0).

### 9.1. Tính gần đúng bằng quy tắc hình thang ⭐⭐
- Cho f(x) liên tục trên [a, b]. Với mỗi n nguyên dương, chia [a, b] thành n đoạn con bằng nhau, Δx = (b − a)/n.
- Mỗi dải rộng Δx được thay bằng một **hình thang** có hai đáy f(xₖ) và f(xₖ₊₁). Cộng diện tích các hình thang được Tₙ.
- Mỗi điểm bên trong là đáy chung của 2 hình thang kề nhau nên có **hệ số 2**; hai đầu mút chỉ thuộc 1 hình thang nên **hệ số 1**.
- **Ví dụ 1:** ∫₁² (eˣ/x) dx, n = 5 → Δx = 0.2, điểm chia 1; 1.2; 1.4; 1.6; 1.8; 2 → T₅ ≈ **3.0653** (slide dừng ở dấu "≈", kết quả tính lại).

### 9.2. Tính gần đúng bằng quy tắc Simpson ⭐⭐
- Cho f(x) liên tục trên [a, b], n nguyên dương **chẵn**, Δx = (b − a)/n.
- Xét từng **cặp đoạn con kề nhau** [x₁, x₂] và [x₂, x₃]: có duy nhất một đường cong bậc không quá 2 (parabol hoặc đường thẳng) đi qua A(x₁, f(x₁)), B(x₂, f(x₂)), C(x₃, f(x₃)). Diện tích dưới parabol trên [x₁, x₃] xấp xỉ diện tích dưới f(x).
- n đoạn con tạo thành n/2 cặp, vì vậy **n phải chẵn**.
- **Ví dụ 2:** ∫₁² (eˣ/x) dx, n = 4 → Δx = 0.25, điểm chia 1; 1.25; 1.5; 1.75; 2 → S₄ ≈ **3.059239**.
- ⚠️ (bổ sung) Giá trị đúng ≈ 3.059117: Simpson n = 4 sát hơn hình thang n = 5.

### 9.3. Tính gần đúng tích phân với số liệu thực nghiệm ⭐
- Khi chỉ đo được h(x) tại các điểm **cách đều** nhau, không có công thức hàm, coi diện tích là S = ∫ [f(x) − g(x)] dx = ∫ h(x) dx (f là bờ trên, g là bờ dưới).
- Dùng quy tắc hình thang trực tiếp trên bảng số liệu: Δx = khoảng cách giữa hai lần đo, n = số khoảng.
- **Ví dụ 3 (bể bơi):** đo tại x = 0, 4, …, 36 (Δx = 4, n = 9), h = 0, 9, 10, 8, 7, 10, 12, 13, 11, 0 → S ≈ (4/2)[0 + 2(9 + 10 + 8 + 7 + 10 + 12 + 13 + 11) + 0] = **320 feet vuông**.

### 9.4. Tích phân suy rộng với cận trên vô hạn ⭐⭐⭐
- Cho f(x) liên tục trên x ≥ a: ∫ₐ^{+∞} f(x) dx = lim_{N→+∞} ∫ₐᴺ f(x) dx (∗).
- (∗) hữu hạn → **hội tụ**; (∗) không tồn tại hoặc bằng vô hạn → **phân kỳ**.
- f(x) ≥ 0 trên [a, +∞) → tích phân là diện tích hình phẳng dưới đường cong trên [a, +∞).
- Cách làm: thay +∞ bằng N, tính tích phân xác định từ a đến N theo N, rồi cho N → +∞.
- **Ví dụ 4:** ∫₁^{+∞} (1/x²) dx = lim (1 − 1/N) = **1** → hội tụ.
- **Ví dụ 5:** ∫₀^{+∞} x e^{−2x} dx: tích phân từng phần, dùng lim Ne^{−2N} = 0 → **1/4** → hội tụ.

### 9.5. Tích phân suy rộng với cận dưới vô hạn ⭐⭐
- Cho f(x) liên tục trên x ≤ b: ∫_{−∞}ᵇ f(x) dx = lim_{N→−∞} ∫_Nᵇ f(x) dx (∗∗).
- Hội tụ / phân kỳ và ý nghĩa diện tích giống cận trên vô hạn.
- **Ví dụ 6:** ∫_{−∞}⁰ 3e^{4x} dx = lim_{N→−∞} (3/4 − 3e^{4N}/4) = **3/4** → hội tụ (vì e^{4N} → 0 khi N → −∞).

### 9.6. Tích phân suy rộng với cả hai cận vô hạn ⭐⭐
- Cho f(x) liên tục trên ℝ. Nếu ∫_c^{+∞} f(x) dx và ∫_{−∞}^c f(x) dx **đều hội tụ** với c nào đó thì ∫_{−∞}^{+∞} f(x) dx = ∫_{−∞}^c f(x) dx + ∫_c^{+∞} f(x) dx.
- Làm theo 3 bước: chọn c → tìm nguyên hàm → tính I₁, I₂ rồi cộng.
- **Ví dụ 7:** ∫_{−∞}^{+∞} x e^{−0.1x²} dx, c = 0: nguyên hàm −5e^{−0.1x²}; I₁ = **−5**, I₂ = **5** → I = **0**.

### 9.7. Sử dụng tích phân suy rộng trong các ứng dụng ⭐
- Tỷ lệ thiết bị **tồn tại lâu hơn t tháng**: ∫_t^{+∞} 0.008e^{−0.008x} dx = e^{−0.008t}.
- Tỷ lệ **hỏng trong vòng không quá T** = 1 − tỷ lệ tồn tại lâu hơn T.
- **Ví dụ 8:** đổi năm ra tháng (5 năm = 60 tháng, 10 năm = 120 tháng). Tồn tại lâu hơn 5 năm: e^{−0.48} = **0.6188**. Hỏng trong vòng không quá 10 năm: 1 − e^{−0.96} = **0.6171** (slide ghi 0.6179) < 0.6188 → tỷ lệ tồn tại lâu hơn 5 năm **lớn hơn**.

### ⚡ Dễ nhầm
- **Hệ số nhân:** hình thang nhân **Δx/2**, Simpson nhân **Δx/3**. Nhầm hai hệ số là sai cả bài.
- **Mẫu hệ số:** hình thang 1, 2, 2, …, 2, 1; Simpson 1, 4, 2, 4, …, 2, 4, 1. Với Simpson, hai điểm sát đầu mút (x₂ và xₙ) **luôn có hệ số 4**.
- **Simpson cần n chẵn.** Bể bơi Ví dụ 3 có n = 9 (lẻ) nên chỉ dùng được hình thang (⚠️ nhận xét bổ sung).
- **Số điểm chia = n + 1**, đánh số từ x₁ = a (không phải x₀). n = 5 có 6 điểm, n = 4 có 5 điểm.
- **Δx = (b − a)/n**, không phải (b − a)/(n + 1).
- Slide tr. 11 (Ví dụ 3) dòng công thức ghi "… + 2h(28) + **h(32)** + h(36)": in nhầm, đúng là **2h(32)**. Dòng thay số đã dùng 2(11), kết quả 320 vẫn đúng.
- Ví dụ 1 slide **không ghi kết quả số**; tính lại được T₅ ≈ 3.0653.
- Ví dụ 8 slide ghi 1 − e^{−0.96} = **0.6179** (in nhầm), đúng là **0.6171**. Kết luận không đổi. Đề ở tr. 20 ghi "hỏng trong vòng **dưới** 10 năm", tr. 21–22 ghi "**không quá** 10 năm".
- Ví dụ 8 đơn vị t là **tháng**: phải đổi năm sang tháng trước khi thay số (e^{−0.008·60} = e^{−0.48}, không phải e^{−0.008·5}).
- **Cận dưới vô hạn** cho N → **−∞**: e^{4N} → 0 (không phải → ∞). Ví dụ 7: e^{−0.1N²} → 0 cả khi N → +∞ lẫn N → −∞.
- Tích phân hai cận vô hạn **không được** tính thẳng lim_{N→+∞} ∫_{−N}^{N}: phải tách I₁, I₂ và **cả hai** hội tụ. Ví dụ 7 ra 0 vì I₁ = −5, I₂ = 5 đều hữu hạn.
- Kết quả "bằng ∞" là **phân kỳ**, không phải hội tụ về ∞.
- Slide tr. 17–19 có tiêu đề "Giới hạn thường sử dụng khi tính tích phân suy rộng" nhưng nội dung là tích phân suy rộng **hai cận vô hạn**.

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Công thức quy tắc hình thang / Simpson: hệ số đứng trước (Δx/2 hay Δx/3), mẫu hệ số, điều kiện n chẵn.
  - Tính Δx, số điểm chia, giá trị xₖ khi cho [a, b] và n.
  - Tính nhanh Tₙ từ bảng số liệu (kiểu bể bơi Ví dụ 3).
  - Định nghĩa hội tụ / phân kỳ; tích phân suy rộng nào hội tụ, bằng bao nhiêu (kiểu Ví dụ 4, 5, 6: 1; 1/4; 3/4).
  - Giới hạn lim_{N→+∞} Nᵖe^{−kN}.
  - Điều kiện để ∫_{−∞}^{+∞} hội tụ (cả hai phần hội tụ).
- **Tự luận:**
  - Tính gần đúng tích phân bằng hình thang (mẫu Ví dụ 1) hoặc Simpson (mẫu Ví dụ 2), lập bảng giá trị f(xₖ).
  - Tính diện tích từ số liệu đo (mẫu Ví dụ 3).
  - Xét hội tụ và tính tích phân suy rộng một cận (mẫu Ví dụ 4, 5, 6) hoặc hai cận (mẫu Ví dụ 7).
  - Bài toán tỷ lệ tồn tại / hỏng của thiết bị, so sánh hai tỷ lệ (mẫu Ví dụ 8).

---

## Bài 10: Hàm số nhiều biến và đạo hàm riêng — ⭐⭐⭐

> Bài giảng: TS. Đặng Huy Ngân. Đề cương: Bài 8 · Chương 6 · mục 6.1 Hàm số nhiều biến · 6.2 Đạo hàm riêng. Ma trận đề: Lecture 8 (Hiểu); câu tổng hợp còn dùng **hàng hoá bổ sung/thay thế** của bài này.

### Tóm tắt
- **Hàm hai biến** z = f(x, y) cho mỗi cặp (x, y) thuộc tập D đúng một số thực z. Không chỉ định D thì **tập xác định** là mọi (x, y) làm biểu thức có nghĩa.
- **Đồ thị** là tập các bộ ba (x, y, f(x, y)) trong không gian ba chiều. **Đường mức** tại mức C là tập (x, y) với f(x, y) = C.
- **Hàm sản xuất Cobb-Douglas** Q = A·K^α·L^β (A, α, β > 0, α + β = 1): K, L cùng tăng gấp đôi thì Q tăng gấp đôi.
- Đường mức của hàm sản lượng là **đường đẳng lượng**; của hàm lợi ích là **đường bàng quan**.
- **Đạo hàm riêng** theo x: lấy đạo hàm theo x, **coi y là hằng số** (và ngược lại).
- **Phân tích cận biên:** Q_K là sản lượng cận biên của vốn, Q_L là sản lượng cận biên của lao động; xấp xỉ mức thay đổi của Q khi K (hoặc L) tăng 1 đơn vị.
- **Hàng hoá thay thế / bổ sung** nhận diện bằng dấu của hai đạo hàm riêng chéo ∂D₁/∂p₂ và ∂D₂/∂p₁.
- **Đạo hàm riêng cấp 2:** fₓₓ, f_yy và hai đạo hàm hỗn hợp fₓᵧ, f_yx.
- **Đạo hàm hàm hợp:** z = f(x(t), y(t)) → dz/dt = (∂z/∂x)(dx/dt) + (∂z/∂y)(dy/dt).
- **Xấp xỉ số gia:** Δz ≈ (∂z/∂x)Δx + (∂z/∂y)Δy.

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Tập xác định:** mọi (x, y) làm biểu thức có nghĩa (⚠️ bổ sung: loại các điểm làm mẫu bằng 0, căn bậc chẵn của số âm, ln của số không dương). Ví dụ 1: f = (3x² + 5y)/(x − y) → D = {(x, y) | x ≠ y}.
- **Hàm tổng doanh thu hai mặt hàng:** R(x, y) = x·D₁ + y·D₂ (giá × lượng cầu của từng loại rồi cộng).
- **Đường mức:** f(x, y) = C. Đẳng lượng: Q(x, y) = C. Bàng quan: U(x, y) = C.
- **Cobb-Douglas:** Q(K, L) = A·K^α·L^β, α + β = 1 → Q(2K, 2L) = 2^{α+β}·Q(K, L) = 2Q(K, L).
- **Đạo hàm riêng:**
  - fₓ = ∂z/∂x = lim_{h→0} [f(x + h, y) − f(x, y)]/h (y hằng số).
  - f_y = ∂z/∂y = lim_{h→0} [f(x, y + h) − f(x, y)]/h (x hằng số).
- **Mẫu đạo hàm hay gặp:**
  - (xⁿ)' = n·xⁿ⁻¹; (c/x)' = −c/x²; (aˣ)' = aˣ ln a.
  - Cobb-Douglas: ∂(A·K^α·L^β)/∂K = αA·K^{α−1}L^β; ∂/∂L = βA·K^α L^{β−1}.
  - yˣ: theo x là **hàm mũ** → yˣ ln y; theo y là **hàm luỹ thừa** → x·y^{x−1}.
- **Sản lượng cận biên:** Q_K (của vốn), Q_L (của lao động). Q_K ≈ mức tăng của Q khi K tăng 1 đơn vị, L giữ nguyên.
- **Hàng hoá thay thế / bổ sung** (D₁, D₂ là cầu theo giá p₁, p₂):
  - **Thay thế:** ∂D₁/∂p₂ > 0 **và** ∂D₂/∂p₁ > 0.
  - **Bổ sung:** ∂D₁/∂p₂ < 0 **và** ∂D₂/∂p₁ < 0.
  - Hai đạo hàm chéo **trái dấu** → không phải loại nào.
- **Đạo hàm riêng cấp 2:** fₓₓ = (fₓ)ₓ; f_yy = (f_y)_y; fₓᵧ = (fₓ)_y; f_yx = (f_y)ₓ.
- **Đạo hàm hàm hợp:** z = f(x, y), x = x(t), y = y(t): **dz/dt = (∂z/∂x)(dx/dt) + (∂z/∂y)(dy/dt)**.
  - (∂z/∂x)(dx/dt): tốc độ thay đổi của z theo t khi y cố định; (∂z/∂y)(dy/dt): khi x cố định.
- **Xấp xỉ số gia:** **Δz ≈ (∂z/∂x)·Δx + (∂z/∂y)·Δy**, với Δz = f(x + Δx, y + Δy) − f(x, y).
- **Các bước bài cận biên / hàm hợp / số gia:**
  1. Tính các đạo hàm riêng cấp 1 dưới dạng công thức.
  2. Đổi đơn vị, xác định điểm (x, y) hiện tại (và t, Δx, Δy nếu có).
  3. Thay số vào đạo hàm riêng.
  4. Thay vào công thức (cận biên / hàm hợp / số gia), ghi dấu và đơn vị, kết luận tăng hay giảm.

### 10.1. Khái niệm hàm hai biến ⭐⭐
- Hàm hai biến: quy tắc f cho mỗi cặp có thứ tự (x, y) thuộc D **một và chỉ một** số thực z, ký hiệu z = f(x, y). D là tập xác định.
- Không chỉ định cụ thể thì D là tập tất cả (x, y) làm f(x, y) xác định.
- **Ví dụ 1:** f(x, y) = (3x² + 5y)/(x − y): D = {(x, y) | x ≠ y} (cả mặt phẳng trừ đường thẳng y = x); f(1, 2) = **−13**.
- **Ví dụ 2:** hai loại vợt, giá x và y, cầu D₁ = 300 − 20x + 30y, D₂ = 200 + 40x − 10y → R(x, y) = **−20x² − 10y² + 70xy + 300x + 200y** (đô la).

### 10.2. Đồ thị và đường mức của hàm hai biến ⭐
- **Đồ thị** của f(x, y): tập các bộ ba (x, y, z) với (x, y) thuộc miền xác định và z = f(x, y). Cần hệ toạ độ ba chiều.
- Các mặt minh hoạ: nón z = √(x² + y²), paraboloid z = x² + y², ellipsoid z = √(9 − 3x² − 2y²), mặt yên ngựa z = y² − x².
- **Đường mức** tại mức C: tập (x, y) trong mặt phẳng xy thoả f(x, y) = C. Là hình chiếu xuống mặt phẳng xy của giao tuyến giữa mặt z = f(x, y) và mặt phẳng z = C. Giống **bản đồ địa hình** của một ngọn núi.
- **Ví dụ 3:** đường mức của f = x² + y² là các **đường tròn đồng tâm O** (C = 1, 4, 9 → bán kính 1, 2, 3).

### 10.3. Hàm sản xuất Cobb-Douglas ⭐⭐
- Sản lượng Q là hàm của vốn K và lao động L: **Q(K, L) = A·K^α·L^β**, A, α, β là hằng số dương, **α + β = 1**.
- **Ví dụ 4:** Q = 60K^{1/3}L^{2/3}, K tính theo $1,000. Vốn $512,000 (K = 512), L = 1,000 → Q = 60·8·100 = **48,000**. Tăng gấp đôi cả hai: Q(1,024; 2,000) = **96,000** = 2Q(512; 1,000).

### 10.4. Đường đẳng lượng và đường bàng quan ⭐⭐
- **Đường đẳng lượng:** đường mức Q(x, y) = C của hàm sản lượng; mọi cách kết hợp hai yếu tố sản xuất cho **cùng mức sản lượng**.
- **Hàm lợi ích** U(x, y): mức hài lòng khi có x đơn vị hàng thứ nhất, y đơn vị hàng thứ hai.
- **Đường bàng quan:** đường mức U(x, y) = C; mọi cách kết hợp x, y cho **cùng mức hài lòng**.
- **Ví dụ 5:** U = x^{3/2}y, U(16, 20) = **1,280** → đường bàng quan x^{3/2}y = 1,280 hay y = 1,280x^{−3/2}.
- **Ví dụ 6:** Q = 3x + 2y, Q(10, 20) = **70**; đẳng lượng 3x + 2y = 70; x tăng 2 → y = 17 → **giảm 3** lao động giản đơn.

### 10.5. Đạo hàm riêng cấp 1 ⭐⭐⭐
- ∂z/∂x (fₓ): đạo hàm theo x, coi y là **hằng số**. ∂z/∂y (f_y): đạo hàm theo y, coi x là **hằng số**.
- Định nghĩa bằng giới hạn: fₓ = lim_{h→0} [f(x + h, y) − f(x, y)]/h; f_y = lim_{h→0} [f(x, y + h) − f(x, y)]/h.
- **Ví dụ 7a:** f = x² + 2xy² + 2y/(3x): fₓ = **2x + 2y² − 2y/(3x²)**, f_y = **4xy + 2/(3x)**.
- **Ví dụ 7b:** f = yˣ: ∂z/∂x = **yˣ ln y**, ∂z/∂y = **x·y^{x−1}**.

### 10.6. Phân tích cận biên ⭐⭐⭐
- Dùng đạo hàm riêng để ước lượng thay đổi của hàm khi **một** biến tăng thêm 1 đơn vị, biến kia giữ nguyên.
- Hàm sản xuất Q = Q(K, L): **Q_K** = sản lượng cận biên của vốn, **Q_L** = sản lượng cận biên của lao động.
- **Ví dụ 8:** Q = 50K^{0.4}L^{0.6}: Q_K = 20K^{−0.6}L^{0.6}, Q_L = 30K^{0.4}L^{−0.4}. Tại K = 750, L = 991: Q_K ≈ **23.64**, Q_L ≈ **26.84** → tăng **lao động** làm sản lượng tăng nhiều hơn.
- **Ví dụ 13a, b:** U = (2x + 3)(y + 5): Uₓ = 2(y + 5), U_y = 2x + 3; tại (27, 12): Uₓ = **34**, U_y = **57**.

### 10.7. Hàng hoá thay thế và hàng hoá bổ sung ⭐⭐⭐
- **Thay thế:** cầu hàng này tăng dẫn đến cầu hàng kia giảm (lời slide). Tiêu chí: **∂D₁/∂p₂ > 0 và ∂D₂/∂p₁ > 0** (giá hàng này tăng → cầu hàng kia tăng).
- **Bổ sung:** cầu hàng này giảm dẫn đến cầu hàng kia giảm. Tiêu chí: **∂D₁/∂p₂ < 0 và ∂D₂/∂p₁ < 0** (giá hàng này tăng → cầu hàng kia giảm).
- Hai đạo hàm chéo trái dấu → **không phải loại nào**.
- **Ví dụ 9:** bột mì D₁ = 500 + 10/(p₁ + 2) − 5p₂, bánh mì D₂ = 400 − 2p₁ + 7/(p₂ + 3): ∂D₁/∂p₂ = **−5**, ∂D₂/∂p₁ = **−2** → **bổ sung**.

### 10.8. Đạo hàm riêng cấp 2 ⭐⭐
- fₓₓ = (fₓ)ₓ = ∂²z/∂x²; f_yy = (f_y)_y = ∂²z/∂y².
- Hỗn hợp: fₓᵧ = (fₓ)_y (đạo hàm fₓ theo y); f_yx = (f_y)ₓ (đạo hàm f_y theo x).
- Cách làm: tính fₓ, f_y trước, rồi lấy đạo hàm riêng mỗi cái theo x và theo y (đủ 4 đạo hàm).
- **Ví dụ 10:** f = x³ − 4xy² + 2y³: fₓ = 3x² − 4y², f_y = −8xy + 6y²; fₓₓ = **6x**, fₓᵧ = **−8y**, f_yx = **−8y**, f_yy = **−8x + 12y**.
- ⚠️ (bổ sung) Với các hàm sơ cấp thường gặp, hai đạo hàm hỗn hợp bằng nhau (fₓᵧ = f_yx), dùng để tự kiểm tra; slide không nêu định lý này.

### 10.9. Đạo hàm riêng của hàm hợp ⭐⭐
- z = f(x, y), x = x(t), y = y(t) thì z là hàm một biến t: **dz/dt = (∂z/∂x)(dx/dt) + (∂z/∂y)(dy/dt)**.
- Ý nghĩa: tốc độ thay đổi của z theo thời gian = phần do x thay đổi (y cố định) + phần do y thay đổi (x cố định).
- **Ví dụ 11:** cầu vitamin A Q = 300 − 20x² + 30y, x = 2 + 0.05t, y = 2 + 0.1√t. Tại t = 4: x = y = 2.2, dQ/dt = −4.4 + 0.75 = **−3.65** → cầu **giảm** 3.65 chai mỗi tháng.

### 10.10. Công thức xấp xỉ số gia ⭐⭐⭐
- Δx, Δy là lượng thay đổi nhỏ của x, y. **Δz ≈ (∂z/∂x)·Δx + (∂z/∂y)·Δy**, Δz = f(x + Δx, y + Δy) − f(x, y).
- Δx, Δy **mang dấu**: tăng là dương, giảm là âm.
- **Ví dụ 12:** Q = 60K^{1/2}L^{1/3}, K = 900, L = 1,000, ΔK = 1, ΔL = −2: Q_K = 10, Q_L = 6 → ΔQ ≈ 10 − 12 = **−2** (giảm khoảng 2 đơn vị).
- **Ví dụ 13c:** ΔU ≈ 34(3) + 57(−2) = **−12** (lợi ích giảm khoảng 12 đơn vị).

### ⚡ Dễ nhầm
- **Định nghĩa hàng hoá thay thế trên slide** ghi "cầu đối với hàng hóa này tăng dẫn đến cầu đối với hàng hóa kia giảm", lệch với tiêu chí toán ngay bên dưới. Khi làm bài **dùng dấu đạo hàm chéo**: cùng dương → thay thế; cùng âm → bổ sung; trái dấu → không phải loại nào.
- Xét dấu **đạo hàm chéo** (∂D₁/∂p₂, ∂D₂/∂p₁), **không** xét ∂D₁/∂p₁ hay ∂D₂/∂p₂ (hai đạo hàm này thường âm theo luật cầu).
- **Ký hiệu đạo hàm hỗn hợp trên slide tr. 22** ghép "fₓᵧ = (fₓ)_y hay ∂²z/∂x∂y = ∂/∂x(∂z/∂y)" — phần viết bằng ∂ lại là đạo hàm f_y theo x (thứ tự ngược với phần chỉ số). Học theo cách viết chỉ số: **fₓᵧ = (fₓ)_y**. Ví dụ 10 có fₓᵧ = f_yx nên không ảnh hưởng kết quả.
- **yˣ:** theo x là hàm mũ (yˣ ln y), theo y là hàm luỹ thừa (x·y^{x−1}). Đảo hai công thức là lỗi hay gặp.
- **2y/(3x) theo x:** viết thành (2y/3)·x⁻¹ → −2y/(3x²). Theo y: 2/(3x) (x là hằng số).
- **Đơn vị vốn:** K tính theo **$1,000** → $512,000 là K = 512, $750,000 là K = 750, $900,000 là K = 900, tăng $1,000 là ΔK = 1.
- **Δx, Δy có dấu:** giảm 2 giờ lao động → ΔL = −2; bớt 2 trái phiếu → Δy = −2.
- **Xấp xỉ số gia chỉ là ước lượng:** ⚠️ (bổ sung) Ví dụ 13 thay đổi thực U(30, 10) − U(27, 12) = −24, xấp xỉ cho −12; Ví dụ 12 thay đổi thực ≈ −2.017, xấp xỉ −2. Đề hỏi "tính gần đúng / ước tính" thì dùng công thức số gia, không tính hiệu trực tiếp.
- **Ví dụ 11** slide ghi "(∂Q/∂y)(dy/∂t)": in nhầm, đúng là **dy/dt**. Đạo hàm của 0.1√t là 0.1/(2√t) = 0.05/√t (quên chia 2 là sai).
- Ví dụ 11: ∂Q/∂y = 30 là hằng số nên dQ/dt chỉ cần x tại t = 4 (y = 2.2 không dùng tới).
- **Cobb-Douglas** theo slide cần α + β = 1. Hàm Ví dụ 12 (Q = 60K^{1/2}L^{1/3}, α + β = 5/6) slide không gọi là Cobb-Douglas.
- Ví dụ 6c hỏi **thay đổi** y (giảm 3), không hỏi y mới (17).

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Tập xác định, giá trị hàm tại một điểm (mẫu Ví dụ 1).
  - Định nghĩa đường mức, đường đẳng lượng, đường bàng quan; đường mức của hàm cho trước (mẫu Ví dụ 3).
  - Dạng hàm Cobb-Douglas, điều kiện α + β = 1, tăng gấp đôi K và L thì Q tăng gấp đôi (mẫu Ví dụ 4).
  - Tính nhanh fₓ, f_y hoặc đạo hàm cấp 2 tại một điểm (mẫu Ví dụ 7, 10).
  - Tên gọi Q_K, Q_L (sản lượng cận biên của vốn / lao động).
  - Điều kiện dấu đạo hàm chéo cho hàng hoá thay thế / bổ sung; nhận diện cặp hàng hoá (mẫu Ví dụ 9).
  - Công thức đạo hàm hàm hợp, công thức xấp xỉ số gia.
- **Tự luận:**
  - Lập hàm doanh thu hai mặt hàng (mẫu Ví dụ 2).
  - Cobb-Douglas: tính sản lượng, chứng minh tăng gấp đôi (mẫu Ví dụ 4); sản lượng cận biên và quyết định tăng vốn hay lao động (mẫu Ví dụ 8).
  - Đường bàng quan / đẳng lượng: tính mức, viết phương trình, giữ sản lượng không đổi khi thay đổi một yếu tố (mẫu Ví dụ 5, 6).
  - Nhận diện hàng hoá thay thế / bổ sung (mẫu Ví dụ 9; cũng là dạng câu tổng hợp).
  - Tốc độ thay đổi theo thời gian bằng đạo hàm hàm hợp (mẫu Ví dụ 11).
  - Ước tính thay đổi sản lượng / lợi ích bằng xấp xỉ số gia (mẫu Ví dụ 12, 13).

---

## Bài 11: Cực trị của hàm số nhiều biến (Phần 1) — ⭐⭐⭐

> Bài giảng: ThS. Nguyễn Thị Quý. Đề cương: Bài 9 · Chương 6 · mục 6.3 Tối ưu hoá hàm số hai biến. Ma trận đề: Lecture 9 (Vận dụng).

### Tóm tắt
- **Cực đại tương đối** tại (a, b): f(a, b) ≥ f(x, y) với mọi (x, y) trong **một hình tròn nào đó tâm (a, b)**. **Cực tiểu tương đối**: ngược dấu (≤). Gọi chung là **cực trị tương đối**.
- **Điểm tới hạn**: điểm mà fₓ, f_y tồn tại và **fₓ = 0, f_y = 0**.
- **Điều kiện cần:** nếu fₓ, f_y tồn tại trên miền R thì cực trị tương đối **chỉ có thể xảy ra tại điểm tới hạn**. Điểm tới hạn **chưa chắc** là cực trị.
- **Điểm yên ngựa**: điểm tới hạn mà f đạt cực đại theo một hướng, cực tiểu theo hướng khác (ví dụ (0, 0) của f = y² − x²).
- **Điều kiện đủ:** phân loại điểm tới hạn bằng **D = fₓₓ·f_yy − (fₓ_y)²** và dấu của **fₓₓ**.
- **Bài toán tối ưu ứng dụng:** lập hàm mục tiêu hai biến (lợi nhuận, tổng bình phương khoảng cách), tìm điểm tới hạn, kiểm tra D.
- **Miền đóng, bị chặn:** chứa biên của nó và nằm trong một hình tròn bán kính hữu hạn.
- **Tính chất giá trị cực biên:** f liên tục trên miền đóng, bị chặn R thì **luôn có** cực đại tuyệt đối và cực tiểu tuyệt đối trên R, đạt **trên biên** hoặc **tại điểm tới hạn bên trong R**.
- **Cực trị tuyệt đối trên miền đóng, bị chặn:** tính f tại điểm tới hạn trong R và các điểm ứng viên trên biên, rồi so sánh.

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Điểm tới hạn:** giải hệ **fₓ(x, y) = 0 ; f_y(x, y) = 0**.
- **Hàm phân loại:** **D(x, y) = fₓₓ(x, y)·f_yy(x, y) − [fₓ_y(x, y)]²**.
- **Kiểm tra theo đạo hàm riêng cấp hai (3 bước):**
  1. Tìm tất cả **điểm tới hạn** (a, b).
  2. Với mỗi điểm tới hạn, tính **D(a, b)**.
  3. Kết luận:

     | D(a, b) | fₓₓ(a, b) | Kết luận |
     |---|---|---|
     | < 0 | bất kỳ | **điểm yên ngựa** |
     | > 0 | > 0 | **cực tiểu** tương đối |
     | > 0 | < 0 | **cực đại** tương đối |
     | = 0 | | **không kết luận được** |

- **Cách nhớ:** D > 0 thì có cực trị, **fₓₓ dương → cực tiểu** (lõm lên, như x²), **fₓₓ âm → cực đại**. D < 0 thì yên ngựa.
- **Cực trị tuyệt đối trên miền đóng, bị chặn R (3 bước):**
  1. Tìm các **điểm tới hạn** của f **nằm trong R** (điểm ngoài R thì bỏ).
  2. Tìm các điểm trên **biên** của R nơi cực trị có thể xảy ra: chia biên thành từng đoạn, thay phương trình đoạn vào f được **hàm một biến**, tìm điểm đạo hàm bằng 0 trong đoạn và lấy **hai đầu mút** (Ví dụ 6).
  3. Tính f tại mọi điểm ở Bước 1 và 2. **Lớn nhất = cực đại tuyệt đối, nhỏ nhất = cực tiểu tuyệt đối.**
- **Lợi nhuận hai mặt hàng:** Lợi nhuận = Σ (số lượng bán) × (giá bán − chi phí) (Ví dụ 4).
- **Bình phương khoảng cách** từ W(x, y) đến điểm (a, b): (x − a)² + (y − b)² (Ví dụ 5).

### 11.1. Cực trị tương đối, điểm tới hạn, điểm yên ngựa ⭐⭐⭐
- **Định nghĩa (tr. 4):**
  - f đạt **cực đại tương đối** tại (a, b) trong miền xác định nếu f(a, b) ≥ f(x, y) với mọi (x, y) trong một hình tròn nào đó có tâm (a, b).
  - f đạt **cực tiểu tương đối** tại (c, d) nếu f(c, d) ≤ f(x, y) với mọi (x, y) trong một hình tròn nào đó có tâm (c, d).
  - Hình (tr. 5): cực đại tương đối là **đỉnh nhô lên** của mặt z = f(x, y), cực tiểu tương đối là **điểm trũng xuống**.
- **Điểm tới hạn (tr. 6):** điểm (a, b) trong tập xác định mà fₓ, f_y đều tồn tại và **fₓ(a, b) = 0, f_y(a, b) = 0**.
- **Điểm yên ngựa (tr. 6):** điểm tới hạn mà f đạt cực đại theo một hướng và cực tiểu theo hướng khác.
- **Điều kiện cần (tr. 6):** nếu các đạo hàm riêng cấp một tồn tại tại mọi điểm thuộc miền R thì cực trị tương đối của f trên R **chỉ có thể xảy ra tại các điểm tới hạn**.
- **Ý nghĩa hình học (tr. 7):** tại điểm cực trị, cắt mặt bằng mặt phẳng y = b thì tiếp tuyến **nằm ngang** (độ dốc fₓ(a, b) = 0); cắt bằng x = a thì độ dốc f_y(a, b) = 0.
- **Ví dụ 1:** f = y² − x² → fₓ = −2x = 0, f_y = 2y = 0 → điểm tới hạn duy nhất **(0, 0)**, nhưng (0, 0) là **điểm yên ngựa**.

### 11.2. Điều kiện đủ: kiểm tra theo đạo hàm riêng cấp hai ⭐⭐⭐
- Điều kiện (tr. 9): fₓ, f_y, fₓₓ, f_yy, fₓ_y đều tồn tại. Lập **D(x, y) = fₓₓ·f_yy − (fₓ_y)²**, xét dấu D và fₓₓ tại từng điểm tới hạn (bảng ở trên).
- **Ví dụ 2:** f = y² − x²: fₓₓ = −2, f_yy = 2, fₓ_y = 0 → D = (−2)(2) − 0² = **−4 < 0** → (0, 0) là **điểm yên ngựa**.
- **Ví dụ 3:** f = x³ − y³ − 3xy:
  - Hệ 3x² − 3y = 0, −3y² − 3x = 0 → y = x², x = −y² → x⁴ + x = 0 → x = 0 hoặc x = −1 → hai điểm tới hạn **(0, 0)** và **(−1, 1)**.
  - fₓₓ = 6x, f_yy = −6y, fₓ_y = −3 → **D = −36xy − 9**.
  - D(0, 0) = −9 < 0 → **yên ngựa**. D(−1, 1) = **27** > 0, fₓₓ(−1, 1) = **−6** < 0 → **cực đại tương đối**.
- Khi D là **hằng số** (hàm bậc hai) thì chỉ cần tính D một lần cho mọi điểm (Ví dụ 2, 4, 5). Khi D **chứa x, y** (Ví dụ 3) phải thay từng điểm tới hạn.

### 11.3. Bài toán tối ưu ứng dụng của hàm hai biến ⭐⭐⭐
- Quy trình: **đặt biến → lập hàm mục tiêu f(x, y) → khai triển gọn → giải fₓ = 0, f_y = 0 → tính D, fₓₓ → kết luận theo ngữ cảnh** (đơn vị, ý nghĩa).
- **Ví dụ 4 (định giá hai loại thức ăn cho mèo, tr. 13–14):**
  - f(x, y) = (70 − 5x + 4y)(x − 30) + (80 + 6x − 7y)(y − 40) = −5x² + 10xy − 7y² − 20x + 240y − 5,300.
  - Hệ −10x + 10y − 20 = 0 ; 10x − 14y + 240 = 0 → **(53, 55)**.
  - fₓₓ = −10, f_yy = −14, fₓ_y = 10 → D = 140 − 100 = **40** > 0, fₓₓ < 0 → **cực đại**.
  - Kết luận: giá **53 cents** (nội địa) và **55 cents** (nhập khẩu). ⚡ Slide in nhầm "$53 … và $53".
  - ⚠️ (bổ sung) Tại giá này bán 25 hộp nội địa, 13 hộp nhập khẩu, lợi nhuận tối đa f(53, 55) = 770 cents = $7.70/ngày.
- **Ví dụ 5 (đặt kho hàng, tr. 15–16):**
  - f(x, y) = [(x − 1)² + (y − 5)²] + [x² + y²] + [(x − 8)² + y²] = 3x² + 3y² − 18x − 10y + 90.
  - 6x − 18 = 0, 6y − 10 = 0 → **(3, 5/3)**. D = 36 > 0, fₓₓ = 6 > 0 → **cực tiểu** → đặt kho tại **W(3, 5/3)**.
  - ⚠️ (bổ sung) W là trọng tâm tam giác ABC; tổng bình phương nhỏ nhất = 164/3 ≈ 54.67 mile².
- Bài toán **lợi nhuận** → tìm **cực đại** (cần fₓₓ < 0). Bài toán **khoảng cách, chi phí** → tìm **cực tiểu** (cần fₓₓ > 0).

### 11.4. Cực trị tuyệt đối trên miền đóng và bị chặn ⭐⭐
- **Điểm biên (tr. 17):** điểm (c, d) mà **mọi** hình tròn tâm (c, d) đều chứa cả điểm thuộc R và điểm ngoài R. Tập các điểm biên là **biên** của R.
- **Miền đóng, bị chặn:** R **chứa biên** của nó và R **bị chứa trong một hình tròn bán kính hữu hạn**.
- **Tính chất giá trị cực biên (tr. 18):** f **liên tục** trên miền đóng, bị chặn R thì đạt **cả** cực đại tuyệt đối và cực tiểu tuyệt đối trên R; các giá trị này đạt **trên biên** hoặc **tại điểm tới hạn bên trong R**.
- **Quy trình 3 bước (tr. 19)**: xem mục Công thức.
- **Ví dụ 6 (tr. 20–22):** f = 4xy − x² − 4y + 9 trên tam giác A(0, 0), B(8, 0), C(0, 16):
  - Điểm tới hạn: −2x + 4y = 0, 4x − 4 = 0 → **(1, 1/2)** ∈ R.
  - Biên AB (y = 0): u = −x² + 9; AC (x = 0): v = −4y + 9; BC (y = −2x + 16): w = −9x² + 72x − 55, w' = 0 tại x = 4 → **(4, 8)**.
  - Bảng: f(1, 1/2) = 8, f(0, 0) = 9, f(8, 0) = −55, f(0, 16) = −55, f(4, 8) = 89.
  - **Cực đại tuyệt đối 89 tại (4, 8)**; **cực tiểu tuyệt đối −55 tại (8, 0) và (0, 16)**.
- Cực trị tuyệt đối **không cần** kiểm tra D: chỉ so sánh giá trị f.

### ⚡ Dễ nhầm
- **Điểm tới hạn ≠ điểm cực trị.** f = y² − x² có điểm tới hạn (0, 0) nhưng đó là **yên ngựa**.
- **D < 0 → yên ngựa**, không xét fₓₓ. Chỉ khi **D > 0** mới xét dấu fₓₓ. **D = 0 → không kết luận**, không được nói "không có cực trị".
- Xét dấu **fₓₓ**, không phải f_yy (slide dùng fₓₓ).
- **fₓₓ > 0 là cực tiểu**, fₓₓ < 0 là cực đại (hay đảo ngược).
- D = fₓₓ·f_yy **trừ** (fₓ_y)², bình phương cả đạo hàm hỗn hợp: ví dụ 3 có fₓ_y = −3 → (−3)² = 9, không phải −9.
- D chứa x, y (Ví dụ 3: D = −36xy − 9) thì phải **thay từng điểm**: D(0, 0) = −9 nhưng D(−1, 1) = 27.
- Giải hệ điểm tới hạn phải lấy **đủ nghiệm**: x⁴ + x = 0 ⇔ x(x³ + 1) = 0 → x = 0 **và** x = −1 (đừng chia cho x làm mất nghiệm x = 0).
- **Ví dụ 4:** đơn vị là **cents**, giá nhập khẩu là **55** (slide in nhầm "$53 … $53"). Hằng số −5,300 là năm nghìn ba trăm (dấu phẩy phân cách nghìn).
- **Cực trị tuyệt đối:** phải xét **cả đầu mút** của từng đoạn biên, không chỉ điểm đạo hàm bằng 0. Điểm tới hạn nằm **ngoài** R thì loại.
- **Ví dụ 6, biên BC:** hai đầu mút là (8, 0) và **(0, 16)**; slide ghi "(0,0)" (in nhầm), kết quả không đổi vì (0, 16) đã có từ biên AC.
- Cực trị **tương đối** dùng D; cực trị **tuyệt đối** trên miền đóng dùng **so sánh giá trị**. Đừng trộn hai quy trình.

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Tìm điểm tới hạn của một hàm hai biến đơn giản (giải fₓ = 0, f_y = 0).
  - Cho fₓₓ, f_yy, fₓ_y tại một điểm tới hạn → tính D và kết luận cực đại / cực tiểu / yên ngựa / không kết luận.
  - Định nghĩa: điểm tới hạn, điểm yên ngựa, miền đóng bị chặn, tính chất giá trị cực biên.
  - Đúng/sai nhanh: "điểm tới hạn luôn là cực trị", "D = 0 thì không có cực trị", "D > 0, fₓₓ > 0 là cực đại".
- **Tự luận:**
  - Tìm và phân loại tất cả điểm tới hạn (mẫu: **Ví dụ 3**, hàm bậc ba có hai điểm tới hạn; **Ví dụ 1–2** cho yên ngựa).
  - Bài toán tối ưu kinh tế hai biến: định giá hai sản phẩm để lợi nhuận lớn nhất (mẫu: **Ví dụ 4**), chọn vị trí tối thiểu tổng bình phương khoảng cách (mẫu: **Ví dụ 5**).
  - Cực đại, cực tiểu tuyệt đối trên miền tam giác (mẫu: **Ví dụ 6**).

---

## Bài 12: Cực trị của hàm số nhiều biến (Phần 2) — ⭐⭐⭐

> Bài giảng: ThS. Nguyễn Thị Quý. Đề cương: Bài 9 · Chương 6 · mục 6.4 Cực trị có điều kiện ràng buộc: phương pháp nhân tử Lagrange. Ma trận đề: Lecture 9 (Vận dụng); câu tổng hợp CLO 3.x (tối đa hoá lợi ích, phân bổ nguồn lực).

### Tóm tắt
- **Bài toán cực trị có điều kiện:** tìm cực trị của z = f(x, y) với **ràng buộc g(x, y) = k**. Cực đại có ràng buộc thường **khác** cực đại không ràng buộc (hình tr. 5).
- **Phương pháp nhân tử Lagrange:** giải hệ **fₓ = λgₓ, f_y = λg_y, g = k**; λ là **nhân tử Lagrange**.
- Slide **không dùng điều kiện đủ**: chỉ tính f tại các nghiệm của hệ rồi **so sánh**: lớn nhất là cực đại, nhỏ nhất là cực tiểu.
- **Mẹo giải hệ:** chia hai phương trình đầu cho nhau để **khử λ**, được quan hệ giữa x và y, rồi thay vào ràng buộc.
- **Tối đa hoá lợi ích:** max U(x, y) với ràng buộc ngân sách p₁x + p₂y = I (Ví dụ 4).
- **Phân bổ nguồn lực:** max sản lượng Cobb–Douglas f(x, y) (x vốn, y lao động) với ràng buộc chi phí (Ví dụ 5).
- **Ý nghĩa của λ:** **λ = dM/dk** ≈ lượng thay đổi của giá trị tối ưu M khi k **tăng 1 đơn vị** (Ví dụ 7, 9).
- **Hàm ba biến:** cùng phương pháp, hệ **bốn phương trình** fₓ = λgₓ, f_y = λg_y, f_z = λg_z, g = k (Ví dụ 8).

### Công thức và quy tắc cần thuộc ⭐⭐⭐
- **Phương pháp nhân tử Lagrange, hàm hai biến (3 bước):**
  1. Xác định hàm mục tiêu **f(x, y)**, hàm **g(x, y)** và hằng số **k** từ ràng buộc (đưa ràng buộc về dạng g(x, y) = k).
  2. Tính fₓ, f_y, gₓ, g_y. Giải hệ ba phương trình Lagrange:
     - **fₓ(x, y) = λ·gₓ(x, y)**
     - **f_y(x, y) = λ·g_y(x, y)**
     - **g(x, y) = k**

     → nghiệm (x₀, y₀, λ₀).
  3. Tính f(x₀, y₀) tại mọi nghiệm. **Giá trị lớn nhất (nhỏ nhất) là cực đại (cực tiểu)** của f với điều kiện g = k.
- **Hàm ba biến:** hệ bốn phương trình **fₓ = λgₓ, f_y = λg_y, f_z = λg_z, g(x, y, z) = k** → nghiệm (x₀, y₀, z₀, λ₀); so sánh f(x₀, y₀, z₀).
- **Khử λ:** chia phương trình 1 cho phương trình 2: **fₓ/f_y = gₓ/g_y**.
  - Lợi ích: **Uₓ/U_y = p₁/p₂** (tỷ số lợi ích cận biên = tỷ số giá). ⚠️ (cách gọi kinh tế bổ sung)
  - Sản xuất: **fₓ/f_y = giá vốn/giá lao động**.
- **Đạo hàm hàm Cobb–Douglas:** f = A·x^a·y^b → fₓ = A·a·x^(a−1)·y^b, f_y = A·b·x^a·y^(b−1); chia nhau: **fₓ/f_y = (a/b)·(y/x)**.
- **Ý nghĩa λ:** M là giá trị cực đại (cực tiểu) của f với g = k thì **λ = dM/dk**; **k tăng Δk → M thay đổi ≈ λ·Δk**; **M mới ≈ M + λ·Δk**.
- **Kết quả đáng nhớ:** Ví dụ 4: **x = 18, y = 8**; Ví dụ 5: **x = 160 vốn, y = 24 lao động**, λ ≈ **0.0219**; Ví dụ 6: **100 m × 50 m, 200 m rào**; Ví dụ 8: **x = 6, y = z = 4, λ = 2, C = $288** (slide in $228).

### 12.1. Bài toán cực trị có điều kiện ràng buộc ⭐⭐
- **Đặt vấn đề (tr. 4):** người tiêu dùng chi $600 mua hai hàng hoá giá $20 và $30, lợi ích U(x, y) = 10x^0.6·y^0.4 → tối đa U với ràng buộc **20x + 30y = 600** (giải ở Ví dụ 4).
- **Bài toán (tr. 5):** tìm cực trị của z = f(x, y) với điều kiện ràng buộc g(x, y) = k.
- **Hình (tr. 5):** đỉnh của mặt cong là **cực đại không có ràng buộc**; điểm cao nhất của đường cong trên mặt nằm phía trên **đường ràng buộc** là **cực đại có ràng buộc**.

### 12.2. Phương pháp nhân tử Lagrange (hàm hai biến) ⭐⭐⭐
- Các bước ở mục Công thức (tr. 6). Hệ viết dạng **fₓ = λgₓ, f_y = λg_y, g = k** (slide không lập hàm Lagrange L).
- **Ví dụ 1:** min f = x² − y² với x² + y² = 4: hệ 2x = λ·2x, −2y = λ·2y, x² + y² = 4 → 4 nghiệm (0, ±2, −1), (±2, 0, 1); f(0, ±2) = −4, f(±2, 0) = 4 → **cực tiểu −4 tại (0, ±2)**, cực đại 4 tại (±2, 0).
- **Ví dụ 2:** max f = xy² với x + y² = 1: hệ y² = λ, 2xy = 2λy, x + y² = 1 → (1, 0, 0), (1/2, ±1/√2, 1/2); f(1, 0) = 0, f(1/2, ±1/√2) = 1/4 → **cực đại 1/4 tại (1/2, ±1/√2)**, cực tiểu 0 tại (1, 0).
- **Ví dụ 3:** f = xy với x² + y² = 8: hệ y = 2λx, x = 2λy → x = ±2, y = ±2, λ = ±1/2 → **cực đại 4 tại (2, 2), (−2, −2)**; **cực tiểu −4 tại (−2, 2), (2, −2)**.
- Khi giải hệ dạng x = λx (hoặc y(x − λ) = 0) phải **tách trường hợp** (x = 0 hoặc λ = 1), không chia cho x.

### 12.3. Bài toán tối đa hoá lợi ích và phân bổ nguồn lực ⭐⭐⭐
- **Tối đa hoá lợi ích (Ví dụ 4, tr. 13–14):** U = 10x^0.6·y^0.4, ràng buộc 20x + 30y = 600.
  - Uₓ = 6x^(−0.4)·y^0.4 = 20λ ; U_y = 4x^0.6·y^(−0.6) = 30λ.
  - Chia: 3y/(2x) = 2/3 ⇔ 4x = 9y → thay vào ràng buộc → **x = 18, y = 8**; λ = 0.3·18^(−0.4)·8^0.4.
  - ⚠️ (bổ sung) λ ≈ 0.2169; lợi ích tối đa U(18, 8) ≈ 130.14.
- **Phân bổ nguồn lực (Ví dụ 5, tr. 15–16):** f = 120x^(4/5)·y^(1/5) (x vốn, y lao động), ràng buộc 3,000x + 5,000y = 600,000.
  - fₓ = 96x^(−1/5)·y^(1/5) = 3,000λ ; f_y = 24x^(4/5)·y^(−4/5) = 5,000λ.
  - Chia: 4y/(3x) = 1/5 → **x = 160 đơn vị vốn, y = 24 đơn vị lao động**; λ = 0.032·160^(−1/5)·24^(1/5) ≈ 0.0219.
  - ⚠️ (bổ sung) sản lượng tối đa ≈ 13,138 đơn vị.
- **Bài toán thực tiễn (Ví dụ 6, tr. 17–18):** rào ba mặt khu dừng nghỉ diện tích 5,000 m²: min f = x + 2y với xy = 5,000 → **x = 100 m, y = 50 m**, λ = 1/50, **tối thiểu 200 m rào**.
- ⚠️ (bổ sung) Với Cobb–Douglas, tại điểm tối ưu **phần ngân sách chi cho mỗi đầu vào tỷ lệ với số mũ**: Ví dụ 4: 20·18 = 360 = 0.6·600, 30·8 = 240 = 0.4·600; Ví dụ 5: 3,000·160 = 480,000 = (4/5)·600,000, 5,000·24 = 120,000 = (1/5)·600,000. Dùng để kiểm tra nhanh đáp án.

### 12.4. Ý nghĩa của nhân tử Lagrange ⭐⭐⭐
- **Định lý (tr. 19):** M là giá trị cực đại (cực tiểu) của f(x, y) với g(x, y) = k thì λ là **tốc độ thay đổi của M theo k**: **λ = dM/dk**. Vì vậy **λ ≈ lượng thay đổi của M khi k tăng 1 đơn vị**.
- **Ví dụ 7:** ngân sách Ví dụ 5 tăng từ $600,000 lên $601,000: λ ≈ 0.0219 → thêm $1 thì sản lượng cực đại tăng ≈ 0.0219 đơn vị → thêm $1,000 tăng ≈ (0.0219)(1000) = **21.9 đơn vị**.
- **Ví dụ 9:** thể tích hộp Ví dụ 8 tăng từ 96 lên 97 inch khối: λ = 2 → chi phí tối thiểu tăng ≈ **$2** → ≈ **$290** (slide in $230, theo lỗi $228).
- Ý nghĩa kinh tế ⚠️ (cách gọi bổ sung): bài phân bổ nguồn lực thì λ là **sản lượng cận biên của $1 ngân sách**; bài chi phí thì λ là **chi phí cận biên của 1 đơn vị ràng buộc**; bài lợi ích thì λ là **lợi ích cận biên của $1 thu nhập**.

### 12.5. Cực trị có điều kiện của hàm ba biến ⭐⭐
- **Bài toán (tr. 21):** tìm cực trị của f(x, y, z) với g(x, y, z) = k. Phương pháp: hệ **bốn phương trình** fₓ = λgₓ, f_y = λg_y, f_z = λg_z, g = k; so sánh f tại các nghiệm.
- **Ví dụ 8 (hộp của Mike, tr. 22):** x cao, y dài, z rộng; vật liệu đáy $1, mặt bên $2, nắp $5 mỗi inch vuông; thể tích 96 inch khối.
  - C(x, y, z) = 1(yz) + 2(2xy + 2xz) + 5yz = **6yz + 4xy + 4xz**.
  - Hệ: 4y + 4z = λyz ; 6z + 4x = λxz ; 6y + 4x = λxy ; xyz = 96 → **x = 6, y = 4, z = 4, λ = 2**.
  - Hộp cao **6 inches**, đáy **vuông cạnh 4 inches**; chi phí tối thiểu **C(6, 4, 4) = $288**. ⚡ Slide in "$228".

### ⚡ Dễ nhầm
- Hệ Lagrange có **ba** phương trình (hai biến) / **bốn** phương trình (ba biến): **đừng quên phương trình ràng buộc g = k**.
- Phải đưa ràng buộc về dạng **g(x, y) = k**: ví dụ xy = 5,000 thì g = xy, k = 5,000; gₓ = y, g_y = x.
- Phương trình dạng **x = λx** phải tách **x = 0 hoặc λ = 1**; chia cho x là **mất nghiệm** (Ví dụ 1, 2).
- Nghiệm (0, 0) của hệ hai phương trình đầu **bị loại** nếu không thoả ràng buộc (Ví dụ 1: 0² + 0² ≠ 4; Ví dụ 3).
- Slide **không kiểm tra điều kiện đủ**: chỉ so sánh giá trị f. ⚠️ Ví dụ 2: đường ràng buộc x = 1 − y² không bị chặn, f = y² − y⁴ → −∞, nên "cực tiểu 0 tại (1, 0)" chỉ là cực tiểu địa phương, không phải giá trị nhỏ nhất (slide không nêu).
- **Ví dụ 1:** đề chỉ hỏi cực tiểu nhưng lời giải nêu cả cực đại; cực tiểu = **−4**.
- Đạo hàm lũy thừa thực: (x^0.6)' = 0.6x^(−0.4), (x^(4/5))' = (4/5)x^(−1/5) (số mũ **trừ 1**, ra số mũ âm).
- Chia hai phương trình: **λ triệt tiêu**, vế phải là **tỷ số giá** (20/30 = 2/3; 3,000/5,000 = 3/5). Ví dụ 5 slide viết 4y/(3x) = 1/5 tương đương 4y/x = 3/5.
- **λ = dM/dk**: λ là thay đổi của **giá trị tối ưu M** (sản lượng, chi phí), **không phải** thay đổi của x hay y. Tăng **Δk** thì nhân **λ·Δk** (Ví dụ 7 nhân 1000).
- **Ví dụ 8:** C(6, 4, 4) = 16 + 192 + 80 = **$288** (slide in $228). Kéo theo **Ví dụ 9:** chi phí hộp 97 inch khối ≈ 288 + 2 = **$290** (slide in $230). Phần "tăng ≈ λ = $2" vẫn đúng.
- Ví dụ 8: chi phí mặt bên là **2 cặp mặt**: 2xy + 2xz (hai mặt x·y, hai mặt x·z), nhân giá $2.
- Ví dụ 6: chỉ rào **ba mặt** (một cạnh x dọc đường cao tốc không rào) → f = x + 2y, không phải 2x + 2y.

### 🎯 Đề hỏi gì
- **Trắc nghiệm:**
  - Viết đúng hệ phương trình Lagrange cho f và ràng buộc cho trước (chọn hệ đúng trong 4 phương án).
  - Ý nghĩa của λ: λ = dM/dk; cho λ và Δk → ước tính thay đổi của giá trị tối ưu (λ·Δk).
  - Tính nhanh điểm tối ưu Cobb–Douglas (chia phương trình khử λ, thay vào ràng buộc).
  - Phân biệt cực trị có ràng buộc và không ràng buộc; số phương trình của hệ (3 với hai biến, 4 với ba biến).
- **Tự luận:**
  - Tìm cực đại / cực tiểu của hàm hai biến với ràng buộc (mẫu: **Ví dụ 1, 2, 3**).
  - **Tối đa hoá lợi ích** với ràng buộc ngân sách (mẫu: **Ví dụ 4**) và **phân bổ nguồn lực** vốn – lao động (mẫu: **Ví dụ 5**), thuộc câu tổng hợp CLO 3.x.
  - Bài toán thực tiễn (rào, hộp) lập hàm mục tiêu và ràng buộc (mẫu: **Ví dụ 6**, **Ví dụ 8**).
  - Ước tính tác động khi tăng ngân sách / ràng buộc bằng λ (mẫu: **Ví dụ 7**, **Ví dụ 9**).
