#!/usr/bin/env python3
"""Vẽ lại các đồ thị toán học trong ngân hàng câu hỏi môn Toán cho các nhà kinh tế.
Chạy: python3 ve.py  (ghi PNG vào thư mục này)
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 12,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})

def style(ax, xlabel="x", ylabel="y", legend=True, legend_loc="best", legend_fontsize=10):
    ax.axhline(0, color="black", linewidth=0.8, zorder=0)
    ax.axvline(0, color="black", linewidth=0.8, zorder=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel, rotation=0, ha="left", va="bottom")
    ax.yaxis.set_label_coords(0.0, 1.02)
    ax.grid(True, linewidth=0.4, alpha=0.5)
    if legend:
        ax.legend(loc=legend_loc, frameon=False, fontsize=legend_fontsize)

def save(fig, name):
    fig.tight_layout()
    fig.savefig(f"{name}.png", dpi=150)
    plt.close(fig)
    print("saved", name)

def fmt_vnd(n):
    return f"{n:,.0f}".replace(",", ".")

# 1) Bài 1, Ví dụ 6 — cân bằng cung cầu: S(x)=x²+14, D(x)=174-6x, xe=10, pe=114
x = np.linspace(0, 14, 400)
S = x**2 + 14
D = 174 - 6*x
fig, ax = plt.subplots(figsize=(5.8, 4.3))
ax.plot(x, S, label="Cung: p = S(x) = x² + 14", color="#1f77b4")
ax.plot(x, D, label="Cầu: p = D(x) = 174 − 6x", color="#d62728")
ax.plot(10, 114, "ko")
ax.annotate("Cân bằng (10, 114)", (10, 114), textcoords="offset points", xytext=(-95, 12), fontsize=10)
ax.set_xlim(0, 14); ax.set_ylim(0, 185)
style(ax, xlabel="x (đơn vị)", ylabel="p (đô-la)", legend_loc="lower center")
save(fig, "bai1-vd6-can-bang-cung-cau")

# 2) Bài 1, Ví dụ 7 — hoà vốn: R(x)=1500x-3x^2, C(x)=66500+20x, hoà vốn x=50,p=1350; công suất 300
x = np.linspace(0, 300, 400)
R = 1500*x - 3*x**2
C = 66500 + 20*x
fig, ax = plt.subplots(figsize=(5.8, 4.3))
ax.plot(x, R, label="Doanh thu: R(x) = 1.500x − 3x²", color="#1f77b4")
ax.plot(x, C, label="Chi phí: C(x) = 66.500 + 20x", color="#d62728")
x0 = 50
y0 = 1500*x0 - 3*x0**2
ax.plot(x0, y0, "ko")
ax.annotate("Hoà vốn (x = 50)", (x0, y0), textcoords="offset points", xytext=(10, -28), fontsize=10)
ax.fill_between(x, R, C, where=(x < x0), color="#d62728", alpha=0.08)
ax.fill_between(x, R, C, where=(x >= x0), color="#1f77b4", alpha=0.08)
ax.text(10, 95000, "Thua lỗ", color="#d62728", fontsize=10)
ax.text(170, 160000, "Lợi nhuận", color="#1f77b4", fontsize=10)
ax.set_xlim(0, 300); ax.set_ylim(0, 200000)
style(ax, xlabel="x (chiếc ghế)", ylabel="đô-la", legend_loc="lower right")
save(fig, "bai1-vd7-hoa-von")

# 3) Bài 2, Ví dụ 1 — lợi nhuận P(x) = -400x^2+6800x-12000, tiếp tuyến tại x=9 (P'(9)=-400)
x = np.linspace(0.5, 16.5, 400)
P = -400*x**2 + 6800*x - 12000
fig, ax = plt.subplots(figsize=(6.2, 4.3))
ax.plot(x, P, label="Lợi nhuận: P(x) = −400x² + 6.800x − 12.000", color="#1f77b4")
x9, slope9 = 9, -400
P9 = -400*x9**2 + 6800*x9 - 12000
xt = np.linspace(7, 11, 10)
ax.plot(xt, P9 + slope9*(xt - x9), "--", color="#ff7f0e", label="Tiếp tuyến tại x = 9 (độ dốc −400)")
ax.plot(x9, P9, "ko")
ax.annotate(f"(9, {fmt_vnd(P9)})", (x9, P9), textcoords="offset points", xytext=(-75, -28), fontsize=10)
ax.set_xlim(0.5, 16.5); ax.set_ylim(-14000, 19000)
style(ax, xlabel="x (nghìn đơn vị)", ylabel="P (đô-la)", legend_loc="lower center")
save(fig, "bai2-vd1-loi-nhuan")

# 4) Bài 5, Ví dụ 1 — f(x)=2x^3+3x^2-12x-7 trên [-3,0]
x = np.linspace(-3, 0, 400)
f = 2*x**3 + 3*x**2 - 12*x - 7
fig, ax = plt.subplots(figsize=(5.4, 4.6))
ax.plot(x, f, color="#1f77b4")
pts = [(-3, 2, "mút trái\nf(−3) = 2", (10, -28)),
       (-2, 13, "cực đại tuyệt đối\n(−2, 13)", (-15, 10)),
       (0, -7, "cực tiểu tuyệt đối\n(mút phải)\n(0, −7)", (-110, 5))]
for xi, fi, lab, off in pts:
    ax.plot(xi, fi, "ko")
    ax.annotate(lab, (xi, fi), textcoords="offset points", xytext=off, fontsize=9, ha="left")
ax.set_xlim(-3.6, 0.9); ax.set_ylim(-11, 17)
style(ax, xlabel="x", ylabel="f(x)", legend=False)
save(fig, "bai5-vd1-cuc-tri-doan")

# 5) Bài 5, Ví dụ 2 — f(x)=x^2+16/x trên x>0, cực tiểu tuyệt đối tại x=2
x = np.linspace(0.6, 6, 400)
f = x**2 + 16/x
fig, ax = plt.subplots(figsize=(5.4, 4.3))
ax.plot(x, f, color="#1f77b4")
ax.plot(2, 12, "ko")
ax.annotate("cực tiểu tuyệt đối (2, 12)", (2, 12), textcoords="offset points", xytext=(10, 15), fontsize=10)
ax.set_ylim(0, 40)
style(ax, xlabel="x", ylabel="f(x) = x² + 16/x", legend=False)
save(fig, "bai5-vd2-cuc-tri-khoang")

# 6) Bài 5, Ví dụ 4 — doanh thu theo giá R(p) = p(300-p^2) = 300p - p^3, 0<=p<=sqrt300
p = np.linspace(0, np.sqrt(300), 400)
R = 300*p - p**3
p_unit = 10.0  # E(p)=1 tại p=10
fig, ax = plt.subplots(figsize=(5.8, 4.4))
ax.plot(p, R, color="#1f77b4")
mask1 = p <= p_unit
mask2 = p >= p_unit
ax.fill_between(p[mask1], 0, R[mask1], color="#2ca02c", alpha=0.12)
ax.fill_between(p[mask2], 0, R[mask2], color="#d62728", alpha=0.12)
ax.plot(p_unit, 300*p_unit - p_unit**3, "ko")
ax.annotate("p = 10: co giãn đơn vị (E = 1)\nR đạt cực đại", (p_unit, 300*p_unit - p_unit**3),
            textcoords="offset points", xytext=(-15, 12), ha="right", fontsize=9)
ax.text(3.5, 350, "Cầu không co giãn\n(E < 1)\ntăng p, R tăng", color="#2ca02c", fontsize=9)
ax.text(12.5, 350, "Cầu co giãn\n(E > 1)\ntăng p, R giảm", color="#d62728", fontsize=9)
ax.set_xlim(0, np.sqrt(300)); ax.set_ylim(0, 2300)
style(ax, xlabel="p (đô-la)", ylabel="R(p)", legend=False)
save(fig, "bai5-vd4-doanh-thu-gia")

# 7) Bài 6, Ví dụ 7 — y = x^3+1, dien tich tu 0 den 1
x = np.linspace(0, 1, 200)
y = x**3 + 1
fig, ax = plt.subplots(figsize=(5.2, 4.3))
ax.plot(x, y, color="#1f77b4", label="Bờ sông: y = x³ + 1")
ax.fill_between(x, 0, y, color="#1f77b4", alpha=0.15, label="Thửa đất (diện tích cần tính)")
ax.set_xlim(-0.05, 1.3); ax.set_ylim(0, 2.3)
style(ax, xlabel="x (trăm feet)", ylabel="y (trăm feet)", legend_loc="lower right")
save(fig, "bai6-vd7-dien-tich-thua-dat")

# 8) Bài 7, Ví dụ 1 — diện tích giữa y=x^3 và y=x^2 trên [0,1]
x = np.linspace(0, 1, 200)
fig, ax = plt.subplots(figsize=(5, 4.3))
ax.plot(x, x**2, color="#1f77b4", label="y = x²")
ax.plot(x, x**3, color="#d62728", label="y = x³")
ax.fill_between(x, x**3, x**2, color="#2ca02c", alpha=0.25, label="Diện tích A = 1/12")
ax.set_xlim(-0.05, 1.1); ax.set_ylim(-0.05, 1.1)
style(ax, xlabel="x", ylabel="y", legend_loc="upper left")
save(fig, "bai7-vd1-dien-tich-hai-duong")

# 9) Bài 7, Ví dụ 2 — loi nhuan vuot troi rong giua P1'(t)=50+t^2 và P2'(t)=200+5t, 0..15
t = np.linspace(0, 15, 300)
P1 = 50 + t**2
P2 = 200 + 5*t
fig, ax = plt.subplots(figsize=(5.8, 4.4))
ax.plot(t, P2, color="#1f77b4", label="P₂'(t) = 200 + 5t (dự án 2)")
ax.plot(t, P1, color="#d62728", label="P₁'(t) = 50 + t² (dự án 1)")
ax.fill_between(t, P1, P2, color="#2ca02c", alpha=0.2, label="NE = 1.687,5 trăm đô-la")
ax.set_xlim(0, 15); ax.set_ylim(0, 300)
style(ax, xlabel="t (năm)", ylabel="trăm đô-la mỗi năm", legend_loc="lower right")
save(fig, "bai7-vd2-loi-nhuan-vuot-troi")

# 10) Bài 7, Ví dụ 3 — đường Lorenz L1=x^1.7, L2=0.8x^2+0.2x so với y=x
x = np.linspace(0, 1, 200)
fig, ax = plt.subplots(figsize=(5.2, 5.2))
ax.plot(x, x, "k--", linewidth=1, label="y = x (bình đẳng tuyệt đối)")
ax.plot(x, x**1.7, color="#1f77b4", label="L₁(x) = x^1.7 (nha sỹ), GI₁ ≈ 0,26")
ax.plot(x, 0.8*x**2 + 0.2*x, color="#d62728", label="L₂(x) = 0,8x² + 0,2x (nhà thầu), GI₂ ≈ 0,27")
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.set_aspect("equal")
style(ax, xlabel="Tỷ lệ người lao động", ylabel="Tỷ lệ thu nhập",
      legend_loc="lower right", legend_fontsize=9)
save(fig, "bai7-vd3-duong-lorenz")

# 11) Bài 7, Ví dụ 8 — CS/PS: D(q) = -0.1q^2+90, S(q)=0.2q^2+q+50, can bang q=10,p=80
q = np.linspace(0, 20, 300)
Dq = -0.1*q**2 + 90
Sq = 0.2*q**2 + q + 50
fig, ax = plt.subplots(figsize=(5.8, 4.4))
ax.plot(q, Dq, color="#1f77b4", label="Cầu: p = D(q) = −0,1q² + 90")
ax.plot(q, Sq, color="#d62728", label="Cung: p = S(q) = 0,2q² + q + 50")
q0, p0 = 10, 80
qf = np.linspace(0, q0, 100)
ax.fill_between(qf, p0, -0.1*qf**2+90, color="#1f77b4", alpha=0.2, label="CS")
ax.fill_between(qf, 0.2*qf**2+qf+50, p0, color="#d62728", alpha=0.2, label="PS")
ax.plot(q0, p0, "ko")
ax.annotate("(10, 80)", (q0, p0), textcoords="offset points", xytext=(6, -16))
ax.set_xlim(0, 20); ax.set_ylim(0, 110)
style(ax, xlabel="q (nghìn chiếc)", ylabel="p (đô-la)", legend_loc="lower center", legend_fontsize=9)
save(fig, "bai7-vd8-cs-ps")

# 12) Bài 10, Ví dụ 3 — đường mức của f(x,y)=x^2+y^2 (vòng tròn đồng tâm)
fig, ax = plt.subplots(figsize=(4.8, 4.8))
theta = np.linspace(0, 2*np.pi, 200)
for c, r in zip([1, 4, 9], [1, 2, 3]):
    ax.plot(r*np.cos(theta), r*np.sin(theta), label=f"f(x, y) = {c}  (bán kính {r})")
ax.set_xlim(-3.5, 3.5); ax.set_ylim(-3.5, 3.5)
ax.set_aspect("equal")
style(ax, xlabel="x", ylabel="y", legend_loc="lower right", legend_fontsize=9)
save(fig, "bai10-vd3-duong-muc")

# 13) Bài 10, Ví dụ 5 — đường bàng quan x^1.5 y = 1280 qua (16,20)
x = np.linspace(6, 60, 300)
y = 1280/np.power(x, 1.5)
fig, ax = plt.subplots(figsize=(5.2, 4.3))
ax.plot(x, y, color="#1f77b4", label="x^1,5·y = 1.280")
ax.plot(16, 20, "ko")
ax.annotate("(16, 20)", (16, 20), textcoords="offset points", xytext=(8, 8))
ax.set_xlim(0, 62); ax.set_ylim(0, 90)
style(ax, xlabel="x (hàng hoá 1)", ylabel="y (hàng hoá 2)", legend_loc="upper right")
save(fig, "bai10-vd5-duong-bang-quan")

# 14) Bài 11, Ví dụ 6 — miền tam giác R: A(0,0) B(8,0) C(0,16)
fig, ax = plt.subplots(figsize=(4.8, 4.8))
tri_x = [0, 8, 0, 0]
tri_y = [0, 0, 16, 0]
ax.plot(tri_x, tri_y, color="#1f77b4")
ax.fill(tri_x, tri_y, color="#1f77b4", alpha=0.15)
for (xx, yy), lab in zip([(0, 0), (8, 0), (0, 16)], ["A(0, 0)", "B(8, 0)", "C(0, 16)"]):
    ax.plot(xx, yy, "ko")
    ax.annotate(lab, (xx, yy), textcoords="offset points", xytext=(6, 6))
ax.set_xlim(-1.5, 10); ax.set_ylim(-1.5, 18)
style(ax, xlabel="x", ylabel="y", legend=False)
save(fig, "bai11-vd6-mien-tam-giac")

print("Xong.")
