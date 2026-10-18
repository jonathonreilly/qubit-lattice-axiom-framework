#!/usr/bin/env python3
"""R3 test 2: what the SM's own one-loop Yukawa flow does to generation ratios (comparator RGEs).

Conventions: Yukawa matrices Y_f with mass term  Lbar Y_f R  (left index first).
16 pi^2 dY_u/dt = [ 3/2 (Hu - Hd) + T - Gu ] Y_u,   Hu = Y_u Y_u^dag, Hd = Y_d Y_d^dag
16 pi^2 dY_d/dt = [ 3/2 (Hd - Hu) + T - Gd ] Y_d
16 pi^2 dY_e/dt = [ 3/2  He       + T - Ge ] Y_e
T = Tr(3Hu + 3Hd + He);  Gu = 17/20 g1^2 + 9/4 g2^2 + 8 g3^2; Gd = 1/4 g1^2 + 9/4 g2^2 + 8 g3^2;
Ge = 9/4 g1^2 + 9/4 g2^2  (g1 GUT-normalised);  16 pi^2 dg_i/dt = b_i g_i^3, b = (41/10, -19/6, -7).
Gauge couplings at M_Z are comparator inputs; Yukawa feedback on gauge running is dropped (one loop).

Runs (t = ln mu, from ln M_Pl down to ln M_Z):
 A. hierarchical small Yukawas: are light-generation ratios RG-invariant?
 B. anarchic O(1) complex matrices at M_Pl (several scales s): does the IR flow create or erase hierarchy?
"""
import numpy as np

MZ, MPL = 91.1876, 1.22e19
TZ, TP = np.log(MZ), np.log(MPL)
K = 1.0 / (16 * np.pi ** 2)
B = np.array([41 / 10, -19 / 6, -7.0])
G_MZ = np.array([np.sqrt(5 / 3) * 0.35745, 0.65171, 1.21770])


def gauge(t):
    # exact one-loop solution: 1/g^2(t) = 1/g^2(MZ) - 2 K b (t - tZ)
    inv = 1 / G_MZ ** 2 - 2 * K * B * (t - TZ)
    return 1 / np.sqrt(inv)


def rhs(t, Yu, Yd, Ye):
    g1, g2, g3 = gauge(t)
    Hu, Hd, He = Yu @ Yu.conj().T, Yd @ Yd.conj().T, Ye @ Ye.conj().T
    T = np.real(np.trace(3 * Hu + 3 * Hd + He))
    I = np.eye(3)
    Gu = 17 / 20 * g1 ** 2 + 9 / 4 * g2 ** 2 + 8 * g3 ** 2
    Gd = 1 / 4 * g1 ** 2 + 9 / 4 * g2 ** 2 + 8 * g3 ** 2
    Ge = 9 / 4 * g1 ** 2 + 9 / 4 * g2 ** 2
    dU = K * (1.5 * (Hu - Hd) + (T - Gu) * I) @ Yu
    dD = K * (1.5 * (Hd - Hu) + (T - Gd) * I) @ Yd
    dE = K * (1.5 * He + (T - Ge) * I) @ Ye
    return dU, dD, dE


def run(Yu, Yd, Ye, n=3000):
    h = (TZ - TP) / n
    t = TP
    for _ in range(n):
        k1 = rhs(t, Yu, Yd, Ye)
        k2 = rhs(t + h / 2, *[Y + h / 2 * k for Y, k in zip((Yu, Yd, Ye), k1)])
        k3 = rhs(t + h / 2, *[Y + h / 2 * k for Y, k in zip((Yu, Yd, Ye), k2)])
        k4 = rhs(t + h, *[Y + h * k for Y, k in zip((Yu, Yd, Ye), k3)])
        Yu, Yd, Ye = [Y + h / 6 * (a + 2 * b + 2 * c + d) for Y, a, b, c, d in zip((Yu, Yd, Ye), k1, k2, k3, k4)]
        t += h
    return Yu, Yd, Ye


def sv(Y):
    return np.sort(np.linalg.svd(Y, compute_uv=False))  # ascending: m1, m2, m3


print("gauge couplings at M_Pl:", np.round(gauge(TP), 4), " alpha_s(M_Pl) =", round(gauge(TP)[2] ** 2 / (4 * np.pi), 5))

# ---------- A: hierarchical start ----------
vh = 246.22 / np.sqrt(2)
mGUT = dict(u=0.48e-3, c=0.235, t=74.0, d=1.14e-3, s=0.022, b=1.00, e=0.469652e-3, mu=0.0991466, tau=1.68558)
for label, yt in (("small top (0.3)", 0.3), ("GUT-set top (0.43)", 74.0 / vh), ("large top (1.5)", 1.5)):
    Yu = np.diag([mGUT['u'], mGUT['c'], 0]) / vh; Yu[2, 2] = yt
    Yd = np.diag([mGUT['d'], mGUT['s'], mGUT['b']]) / vh
    Ye = np.diag([mGUT['e'], mGUT['mu'], mGUT['tau']]) / vh
    u0, d0, e0 = sv(Yu), sv(Yd), sv(Ye)
    u1, d1, e1 = [sv(Y) for Y in run(Yu.astype(complex), Yd.astype(complex), Ye.astype(complex))]
    print(f"\nA [{label}] ratio(M_Z)/ratio(M_Pl):")
    for nm, a, b in (("up", u0, u1), ("down", d0, d1), ("lep", e0, e1)):
        r12 = (b[0] / b[1]) / (a[0] / a[1]); r23 = (b[1] / b[2]) / (a[1] / a[2])
        print(f"   {nm:4s}: m1/m2 x{r12:.4f}   m2/m3 x{r23:.4f}   (y3: {a[2]:.3f} -> {b[2]:.3f})")

# ---------- B: anarchic start ----------
rng = np.random.default_rng(20261018)
print("\nB anarchic complex Gaussian matrices at M_Pl, entries s*(N(0,1)+iN(0,1))/sqrt2; 120 samples per s")
print("   reported: median and 10/90% of log10(m1/m3), log10(m2/m3) per sector at M_Pl -> M_Z;")
print("   'spread' = log10(m3/m1); fraction of samples whose spread GREW toward the IR")
for s in (0.1, 0.5, 1.0, 2.0):
    rec = {k: [] for k in ("up", "down", "lep")}
    for _ in range(120):
        Ys = [s * (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / np.sqrt(2) for _ in range(3)]
        Ye_ = [sv(Y) for Y in Ys]
        Yf = [sv(Y) for Y in run(*Ys, n=1500)]
        for k, a, b in zip(("up", "down", "lep"), Ye_, Yf):
            rec[k].append((np.log10(a[0] / a[2]), np.log10(a[1] / a[2]), np.log10(b[0] / b[2]), np.log10(b[1] / b[2]), b[2]))
    print(f"  s = {s}:")
    for k, v in rec.items():
        v = np.array(v)
        q = lambda x: f"{np.median(x):+.2f} [{np.percentile(x,10):+.2f},{np.percentile(x,90):+.2f}]"
        grew = np.mean((v[:, 2] - v[:, 0]) < -1e-9)
        grew_lot = np.mean((v[:, 2] - v[:, 0]) < -0.05)
        print(f"     {k:4s} m1/m3: {q(v[:,0])} -> {q(v[:,2])};  m2/m3: {q(v[:,1])} -> {q(v[:,3])};"
              f"  spread grew: {grew:.2f} (by >0.05 dex: {grew_lot:.2f});  max growth {-(v[:,2]-v[:,0]).min():+.3f} dex; y3(MZ) median {np.median(v[:,4]):.2f}")
