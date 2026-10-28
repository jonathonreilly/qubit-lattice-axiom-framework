"""Check x2 (criteria: x2_criteria.md, written first).
A: LAP-1 anti-concentration in the 2D open-boundary SU(2) Wilson model (i.i.d. plaquettes).
B: Gaussian two-grid variance of linearised S4' block curvature (exact Fourier symbol).
"""
import math
import numpy as np

ok_all = True

# ---------------- A ----------------
N = 2
alpha = 1.0
n_p = 2
A1 = n_p * 2.0 * math.sqrt(N) * (math.exp(alpha) - 1.0)
Cstar = (4.0 / 3.0) * A1 / alpha**2
dstar = math.exp(-2 * Cstar) / (288 * math.pi**2 * N)
print(f"A: A_1={A1:.4f} C_*={Cstar:.4f} delta_*={dstar:.3e}")


def dens(th, g):
    return np.exp(-(8.0 / g**2) * np.sin(th / 2) ** 2) * np.sin(th) ** 2


def trap(y, x):
    return float(np.sum((y[1:] + y[:-1]) * np.diff(x)) / 2)


def Zg(g, m=2_000_001):
    th = np.linspace(0, math.pi, m)
    return trap(dens(th, g), th)


A_ok = True
for g in [0.05, 0.1, 0.2, 0.3, 0.5]:
    th = np.linspace(0, math.pi, 2_000_001)
    f = dens(th, g)
    Z = trap(f, th)
    E = trap((1 - np.cos(th)) * f, th) / Z
    thc = 2 * math.asin(math.sqrt(dstar * g**2 / 2))
    tt = np.linspace(0, thc, 2001)
    Pc = trap(dens(tt, g), tt) / Z
    a1 = E >= dstar * g**2 / 2
    a2 = Pc <= 0.25
    A_ok &= a1 and a2
    print(f"A g={g}: E[1-P]={E:.6e} E/g^2={E/g**2:.5f} bound={dstar*g**2/2:.3e} A1={a1} "
          f"P(1-P<d*g^2)={Pc:.3e} A2={a2}")
    if g == 0.05:
        a3 = abs(E / g**2 - 0.375) < 0.05
        print(f"A3 (expectation) |E/g^2-3/8|={abs(E/g**2-0.375):.4f} -> {a3}")


def nuS(g, rho, Z):
    # S = {|U-1|_HS < rho}: 4(1-cos th) < rho^2
    thc = math.acos(max(-1.0, 1 - rho**2 / 4))
    tt = np.linspace(0, thc, 200001)
    return trap(dens(tt, g), tt) / Z


def nuTuS(g, rho, s, Z, m):
    a = s / math.sqrt(2)  # quaternion angle of exp(sX), |X|_HS = 1
    beta = 2 * math.asin(rho / (2 * math.sqrt(2)))
    lo, hi = max(0.0, a - beta), min(math.pi, a + beta)
    tt = np.linspace(lo, hi, m)
    c0 = 1 - rho**2 / 4
    with np.errstate(divide="ignore", invalid="ignore"):
        t = (c0 - np.cos(tt) * math.cos(a)) / (np.sin(tt) * math.sin(a))
    t = np.where(np.isfinite(t), t, np.where(np.cos(tt) * math.cos(a) > c0, -1.0, 1.0))
    frac = (1 - np.clip(t, -1, 1)) / 2
    return trap(dens(tt, g) * frac, tt) / Z


for g in [0.1, 0.3]:
    Z = Zg(g)
    for r in [0.05, 0.15]:
        rho = r * g
        nS = nuS(g, rho, Z)
        for s in [g / 4, g / 2, g]:
            v1 = nuTuS(g, rho, s, Z, 200001)
            v2 = nuTuS(g, rho, s, Z, 400001)
            relerr = abs(v1 - v2) / max(v2, 1e-300)
            cs = math.exp(-(4.0 / 3.0) * (A1 / g**2) * s**2 / alpha**2)
            a4 = (v2 >= cs * nS) and relerr < 1e-3
            A_ok &= a4
            print(f"A4 g={g} r={r} s/g={s/g:.2f}: nu(TuS)={v2:.4e} nu(S)={nS:.4e} "
                  f"ratio={v2/nS:.4e} c_s={cs:.3e} relerr={relerr:.1e} -> {a4}")
print("Pass A:", A_ok)
ok_all &= A_ok

# ---------------- B ----------------
L = 3
B_ok = True
store = {}
for r in [1, 2, 3]:
    ell = L**r
    n = 2 * ell
    x = np.arange(n)
    ind = (x < ell).astype(float)
    tent = np.real(np.fft.ifft(np.fft.fft(ind) * np.fft.fft(ind)))
    tent = np.round(tent)  # integer counts
    k = np.arange(n)
    lam1 = 4 * np.sin(np.pi * k / n) ** 2
    for name, par in [("(1,2) perp-shift", (1, 2)), ("(0,1) in-plane shift", (0, 1))]:
        facs = [np.abs(np.fft.fft(tent if d in par else ind)) ** 2 for d in range(4)]
        S0 = np.zeros(n)
        tot = 0.0
        l1, l2, l3 = np.meshgrid(lam1, lam1, lam1, indexing="ij")
        f123 = facs[1][:, None, None] * facs[2][None, :, None] * facs[3][None, None, :]
        lam_other = [l1, l2, l3]
        for k0 in range(n):
            lam = lam1[k0] + l1 + l2 + l3
            lam_par = sum((lam1[k0] if d == 0 else lam_other[d - 1]) for d in par)
            with np.errstate(divide="ignore", invalid="ignore"):
                w = np.where(lam > 0, lam_par / lam, 0.0)
            ps2 = facs[0][k0] * f123 / ell**8
            S0[k0] = float(np.sum(w * ps2))
            tot += float(np.sum(ps2))
        n4 = float(n) ** 4
        P0 = S0.sum() / n4
        psi2 = tot / n4
        b2 = P0 <= 1 + 1e-12
        B_ok &= b2
        Vs = []
        b1 = True
        for j in range(1, ell):
            mult = 4 * np.sin(np.pi * k * j / n) ** 2
            V = float(np.sum(S0 * mult)) / n4
            Vs.append(V)
            if V > 4 * j / ell + 1e-12:
                b1 = False
        B_ok &= b1
        store[(r, name)] = (P0, Vs)
        print(f"B r={r} {name}: ||psi0||^2={psi2:.5f} ||Pi_ex psi0||^2={P0:.5f} B2={b2} | "
              f"V(1)={Vs[0]:.4e} (4w={4/ell:.3e}) max V/(4w)={max(V/(4*(i+1)/ell) for i,V in enumerate(Vs)):.4f} B1={b1}")
print("Pass B:", B_ok)
ok_all &= B_ok
for name in ["(1,2) perp-shift", "(0,1) in-plane shift"]:
    P0_1, V1 = store[(1, name)]
    a = V1[0] / P0_1 >= 0.1
    b = store[(1, name)][1][0] > store[(2, name)][1][0] > store[(3, name)][1][0]
    v2 = store[(2, name)][1][3 - 1]  # j = 3 at r = 2 (w = 1/3)
    v3 = store[(3, name)][1][9 - 1]  # j = 9 at r = 3 (w = 1/3)
    c = max(v2, v3) / min(v2, v3) <= 1.5
    print(f"B3 {name}: (a) one-step V(1)/Var0={V1[0]/P0_1:.3f} -> {a}; (b) V(j=1) r=1,2,3: "
          f"{store[(1,name)][1][0]:.3e},{store[(2,name)][1][0]:.3e},{store[(3,name)][1][0]:.3e} -> {b}; "
          f"(c) w=1/3: r=2 {v2:.4e}, r=3 {v3:.4e} -> {c}")
print("PASS" if ok_all else "FAIL", "A_ok=", A_ok, "B_ok=", B_ok)
