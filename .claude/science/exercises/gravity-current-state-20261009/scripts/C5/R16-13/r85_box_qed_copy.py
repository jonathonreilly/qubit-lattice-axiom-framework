"""R8-5 (C5 round 8): one-loop light cones of a gauge-invariant 'box QED' on Z^3 x R (continuous time).

LAW ("BQ"; every Feynman rule equals continuum Feynman-gauge QED when all lines sit in the box)
  fermion: one 4-component Dirac field per site, separable (axis-only) hopping
      h(k) = sum_j [ S(k_j) alpha_j + W(k_j) beta ] + m beta,
      S = rho k + (1-rho) sin k,  W = r (1-rho)(1-cos k),  rho = C^inf plateau (1 on |k|<=b1, 0 on |k|>=b2)
      -> in the box h = alpha.k + beta m exactly; zone-edge doublers get Wilson mass m + 2r.
  photon: non-compact U(1) links A^std (gauge shift = forward difference). Physical field A_j = G_j A^std_j,
      G_j a smooth translation-invariant 1D convolution with symbol g(q) = (q/2)/sin(q/2) on the plateau
      [c1,c2] -> 1 outside.  Then D_j = grad_j G_j has |Dhat_j(q)|^2 = d(q_j)^2, d = rho_g q + (1-rho_g) 2 sin(q/2):
      Maxwell action with Dhat gives transverse omega^2 = sum_j d(q_j)^2 = |q|^2 exactly in the photon box.
  coupling: Peierls phases of A^std along the (straight, axis) hopping path: gauge invariant, exact Ward identity.
      vertex  V_j(k+q,k) = i e [h_j(k_j) - h_j(k_j+q_j)] / Dhat_j(q)   (= -e alpha_j e^{-iq_j/2} in the box)
      seagull S2_j(p;q,-q) = [h_j(p_j+q_j)+h_j(p_j-q_j)-2h_j(p_j)]/d(q_j)^2   (= 0 in the box)
      A_0 couples on-site to psi^dag psi (vertex i e in Euclidean).

QUANTITIES (per e^2; x16pi^2 printed = units of e^2/16pi^2); Clifford closed forms, k0 integrals in closed form
  photon:  P_E = (1/2)<|d_y n|^2 E^2 ... > via  (|x|^2-(x.n)^2)/(2E^3), x = d h/dk_y   [method w]
           P_E also from the static density response chi_00(q)/d(q)^2                 [method rho, gauge check]
           P_M = [ <-2 y.n> - chi_yy(q xhat) ] / d(q)^2, y = d^2h/dk_y^2                [Ward: P_M*d^2 -> 0 at q=0]
           dc_gamma = (P_M - P_E)/2
  fermion (Feynman gauge, photon mass lam): Sigma(p0,p) = -<sum_n [sum_j D_j P_n D_j/d_j^2 - P_n] s_n/(2W(W+E-i s_n p0))> + tadpole
           A_id = <(sum_j|delta_j|^2/d_j^2 - 1)/(2W(W+E)^2)>,  B_a = d/dp_x [alpha_x part of Sigma(0,p)] ,  dc_e = B_a - A_id
  Delta = (dc_e - dc_gamma) * 16 pi^2.
Validation: with rho=0, r=0, d=2 sin(q/2) the formulas reduce algebraically to F2's naive-QED closed forms
(scratchpad/C4/F2/f2_qed_speeds.py); the run compares numerically against a verbatim copy of F2's functions.
"""
import numpy as np, sys, time

# ---------------------------------------------------------------- smooth plateau
def _phi(t):
    t = np.clip(t, 0.0, 1.0)
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        f0 = np.where(t > 0, np.exp(-1.0 / np.where(t > 0, t, 1.0)), 0.0)
        f1 = np.where(t < 1, np.exp(-1.0 / np.where(t < 1, 1.0 - t, 1.0)), 0.0)
    return f0 / (f0 + f1)

def plateau(k, b1, b2):
    if b1 is None:              # 'off': no box at all (pure lattice functions)
        return np.zeros_like(k)
    return 1.0 - _phi((np.abs(k) - b1) / (b2 - b1))

class Law:
    def __init__(self, b1, b2, r, c1, c2, m, naive_photon=False):
        self.b1, self.b2, self.r, self.c1, self.c2, self.m = b1, b2, r, c1, c2, m
        self.naive_photon = naive_photon
    # 1D fermion functions
    def S(self, k):
        rho = plateau(k, self.b1, self.b2)
        return rho * k + (1 - rho) * np.sin(k)
    def W(self, k):
        rho = plateau(k, self.b1, self.b2)
        return self.r * (1 - rho) * (1 - np.cos(k))
    def d(self, q):
        if self.naive_photon:
            return 2 * np.sin(q / 2)
        rg = plateau(q, self.c1, self.c2)
        return rg * q + (1 - rg) * 2 * np.sin(q / 2)

def deriv(f, k, n=1, h=1e-3):
    """4th-order central differences of a 1D function (n = 1 or 2)."""
    if n == 1:
        return (-f(k + 2 * h) + 8 * f(k + h) - 8 * f(k - h) + f(k - 2 * h)) / (12 * h)
    return (-f(k + 2 * h) + 16 * f(k + h) - 30 * f(k) + 16 * f(k - h) - f(k - 2 * h)) / (12 * h * h)

def kgrid1(N):
    return (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi

def hvec(law, kx, ky, kz):
    """Clifford components (alpha_x, alpha_y, alpha_z, beta) of h(k) on a broadcast grid."""
    return (law.S(kx), law.S(ky), law.S(kz), law.m + law.W(kx) + law.W(ky) + law.W(kz))

# ---------------------------------------------------------------- photon
def photon(law, N, qs=(0.02, 0.04), chunk=16):
    k1 = kgrid1(N)
    KY, KZ = np.meshgrid(k1, k1, indexing="ij")
    Sy, Wy = law.S(KY), law.W(KY)
    Sz, Wz = law.S(KZ), law.W(KZ)
    xy = deriv(law.S, KY); xb = deriv(law.W, KY)          # x = d h / dk_y : (0, S'(ky), 0, W'(ky))
    yy = deriv(law.S, KY, 2); yb = deriv(law.W, KY, 2)    # y = d2h/dk_y2
    acc = dict(PEw=0.0, dia=0.0, chiyy0=0.0)
    acc_q = {q: dict(chi00=0.0, chiyy=0.0) for q in qs}
    for i0 in range(0, N, chunk):
        kx = k1[i0:i0 + chunk][:, None, None]
        def nE(kxv):
            Sx = law.S(kxv); Wx = law.W(kxv)
            hx, hy, hz, hb = Sx + 0 * KY, Sy[None] + 0 * kxv, Sz[None] + 0 * kxv, law.m + Wx + Wy[None] + Wz[None]
            E = np.sqrt(hx ** 2 + hy ** 2 + hz ** 2 + hb ** 2)
            return (hx / E, hy / E, hz / E, hb / E), E
        n, E = nE(kx)
        xn = xy[None] * n[1] + xb[None] * n[3]
        x2 = xy[None] ** 2 + xb[None] ** 2
        acc["PEw"] += np.sum((x2 - xn ** 2) / (2 * E ** 3))
        acc["dia"] += np.sum(-2 * (yy[None] * n[1] + yb[None] * n[3]))
        # q = 0 paramagnetic (Ward identity check): Tr[X P+ X P-]/(2E) * 2 orderings
        acc["chiyy0"] += np.sum(2 * (2 * x2 - 2 * xn ** 2) / (2 * E))
        for q in qs:
            for sgn in (+1, -1):
                n2, E2 = nE(kx + sgn * q)
                nn = n[0] * n2[0] + n[1] * n2[1] + n[2] * n2[2] + n[3] * n2[3]
                xn2 = xy[None] * n2[1] + xb[None] * n2[3]
                acc_q[q]["chi00"] += np.sum((1 - nn) / (E + E2))
                acc_q[q]["chiyy"] += np.sum((x2 * (1 + nn) - 2 * xn * xn2) / (E + E2))
    V = N ** 3
    PEw = acc["PEw"] / V; dia = acc["dia"] / V; wi = dia - acc["chiyy0"] / V
    PEr, PM = [], []
    for q in qs:
        dq2 = law.d(np.array(q)) ** 2
        PEr.append(acc_q[q]["chi00"] / V / dq2)
        # Ward-subtracted: the f-sum rule dia = chi_yy(0) is an exact BZ identity; using chi_yy(0) from the
        # same grid removes its quadrature error (reported separately as 'Ward').
        PM.append((acc["chiyy0"] / V - acc_q[q]["chiyy"] / V) / dq2)
    # Richardson in q^2 (qs = h, 2h)
    PEr_x = (4 * PEr[0] - PEr[1]) / 3; PM_x = (4 * PM[0] - PM[1]) / 3
    # same-q estimator: in a Lorentz-invariant theory the static P_E(q) and P_M(q) are the same function of q^2,
    # so (P_M(q) - P_E^rho(q))/2 cancels the (continuum, LI) IR region identically even when q ~ m.
    dsq = [(PM[i] - PEr[i]) / 2 for i in range(len(qs))]
    dcg_sq = (4 * dsq[0] - dsq[1]) / 3
    return dict(PEw=PEw, PEr=PEr_x, PM=PM_x, wi=wi, dcg=(PM_x - PEw) / 2, gauge=(PEr_x - PEw), dcg_sq=dcg_sq)

# ---------------------------------------------------------------- fermion self-energy at p = 0
def fermion(law, N, lam, hp=(1e-3, 2e-3), chunk=16):
    q1 = kgrid1(N)
    QY, QZ = np.meshgrid(q1, q1, indexing="ij")
    dqy2, dqz2 = law.d(QY) ** 2, law.d(QZ) ** 2
    # y,z parts at p_y = p_z = 0: fermion k_j = -q_j ; delta_j = h_j(0) - h_j(-q_j)
    Sy, Wy, Sz, Wz = law.S(-QY), law.W(-QY), law.S(-QZ), law.W(-QZ)
    dly = (0 - Sy, law.W(np.array(0.0)) - Wy)   # (alpha_y comp, beta comp)
    dlz = (0 - Sz, law.W(np.array(0.0)) - Wz)
    A_id = 0.0; tadd = 0.0
    sun = {p: 0.0 for p in [s * h for h in hp for s in (+1, -1)]}
    S0p = deriv(law.S, np.array(0.0))
    for i0 in range(0, N, chunk):
        qx = q1[i0:i0 + chunk][:, None, None]
        dqx2 = law.d(qx) ** 2
        Om = np.sqrt(dqx2 + dqy2[None] + dqz2[None] + lam ** 2)
        # tadpole derivative (alpha_x comp): <(S'(q_x) - S'(0)) / (2 Om d(q_x)^2)>
        tadd += np.sum((deriv(law.S, qx) - S0p) / (2 * Om * dqx2) + 0 * Om)
        for p in list(sun.keys()) + [0.0]:
            kx = p - qx
            hx = law.S(kx) + 0 * Om
            hy = Sy[None] + 0 * Om; hz = Sz[None] + 0 * Om
            hb = law.m + law.W(kx) + Wy[None] + Wz[None]
            E = np.sqrt(hx ** 2 + hy ** 2 + hz ** 2 + hb ** 2)
            n = (hx / E, hy / E, hz / E, hb / E)
            # delta_x = h_x(p) - h_x(p - q_x): components (alpha_x, beta)
            dxa = law.S(np.array(p)) - law.S(kx); dxb = law.W(np.array(p)) - law.W(kx)
            if p == 0.0:
                s2 = (dxa ** 2 + dxb ** 2) / dqx2 + (dly[0] ** 2 + dly[1] ** 2)[None] / dqy2[None] \
                     + (dlz[0] ** 2 + dlz[1] ** 2)[None] / dqz2[None]
                A_id += np.sum((s2 - 1) / (2 * Om * (Om + E) ** 2))
                continue
            # alpha_x component of  sum_j (2 (d_j.n) d_j - |d_j|^2 n)/d_j^2 - n
            dn_x = dxa * n[0] + dxb * n[3]
            comp = (2 * dn_x * dxa - (dxa ** 2 + dxb ** 2) * n[0]) / dqx2
            dn_y = dly[0][None] * n[1] + dly[1][None] * n[3]
            comp += (-(dly[0] ** 2 + dly[1] ** 2)[None] * n[0]) / dqy2[None]   # (d_y.n) d_y has no alpha_x part
            comp += (-(dlz[0] ** 2 + dlz[1] ** 2)[None] * n[0]) / dqz2[None]
            comp -= n[0]
            sun[p] += np.sum(-comp / (2 * Om * (Om + E)))
    V = N ** 3
    A_id /= V; tadd /= V
    for p in sun: sun[p] /= V
    h1, h2 = hp
    D1 = (sun[h1] - sun[-h1]) / (2 * h1); D2 = (sun[h2] - sun[-h2]) / (2 * h2)
    sund = (4 * D1 - D2) / 3
    B = sund + tadd
    return dict(A_id=A_id, B=B, sun=sund, tad=tadd, dce=B - A_id)

# ---------------------------------------------------------------- F2 verbatim reference (naive QED)
def f2_grid(L):
    k = (np.arange(L) + 0.5) * 2 * np.pi / L - np.pi
    return np.meshgrid(k, k, k, indexing="ij")

def f2_fermion_coeffs(L, m, lam, h=1e-4):
    KX, KY, KZ = f2_grid(L)
    khat2 = 4 * (np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2)
    w = np.sqrt(khat2 + lam ** 2)
    E = np.sqrt(np.sin(KX) ** 2 + np.sin(KY) ** 2 + np.sin(KZ) ** 2 + m ** 2)
    C0 = np.cos(KX / 2) ** 2 + np.cos(KY / 2) ** 2 + np.cos(KZ / 2) ** 2
    a0 = -np.mean((1 - C0) / (2 * w * (E + w) ** 2))
    A2 = np.mean(1 / (2 * w))
    def I(px):
        Eq = np.sqrt(np.sin(px - KX) ** 2 + np.sin(KY) ** 2 + np.sin(KZ) ** 2 + m ** 2)
        C = 1 + np.cos(px - KX / 2) ** 2 + np.cos(KY / 2) ** 2 + np.cos(KZ / 2) ** 2
        F = np.sin(px - KX) * (2 * np.cos(px - KX / 2) ** 2 - C) / (2 * Eq * w * (Eq + w))
        return np.mean(F)
    dI = (I(h) - I(-h)) / (2 * h)
    a1 = -0.5 * A2 - dI
    return dict(a0=a0, a1=a1, dcf=a1 - a0)

def f2_photon_coeffs(L, m, kxs=(0.02, 0.04)):
    QX, QY, QZ = f2_grid(L)
    sx, sy, sz = np.sin(QX), np.sin(QY), np.sin(QZ)
    E2 = sx ** 2 + sy ** 2 + sz ** 2 + m ** 2
    E = np.sqrt(E2)
    aE = 0.5 * np.mean(np.cos(QX) ** 2 * (E2 - sx ** 2) / E ** 5)
    tad_yy = 2 * np.mean(sy ** 2 / E)
    vals = []
    for kx in kxs:
        sxp = np.sin(QX + kx)
        Ep = np.sqrt(sxp ** 2 + sy ** 2 + sz ** 2 + m ** 2)
        Y = sx * sxp - sy ** 2 + sz ** 2 + m ** 2
        bub = -4 * np.mean(np.cos(QY) ** 2 * (E * Ep + Y) / (2 * E * Ep * (E + Ep)))
        vals.append((bub + tad_yy) / (4 * np.sin(kx / 2) ** 2))
    aB = (4 * vals[0] - vals[1]) / 3
    return dict(aE=aE, aB=aB, dcg=(aB - aE) / 2)

U = 16 * np.pi ** 2

if __name__ == "__main__":
    t0 = time.time()
    mode = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if mode == "validate":
        print("== VALIDATION: general Clifford code with box OFF (naive fermion, r=0, naive photon) vs F2 verbatim")
        for (L, m, lam) in [(48, 0.2, 0.2), (64, 0.1, 0.1)]:
            law = Law(None, None, 0.0, None, None, m, naive_photon=True)
            ph = photon(law, L); fe = fermion(law, L, lam, hp=(1e-4, 2e-4))
            f2p = f2_photon_coeffs(L, m); f2f = f2_fermion_coeffs(L, m, lam)
            print(f" L={L} m={m} lam={lam}")
            print(f"   photon  P_E(w)={ph['PEw']:.10f} F2 aE={f2p['aE']:.10f} | P_M={ph['PM']:.10f} F2 aB={f2p['aB']:.10f}"
                  f" | P_E(rho)-P_E(w)={ph['gauge']:+.2e} | Ward P_M*d^2(q=0)={ph['wi']:+.2e}")
            print(f"   fermion A_id={fe['A_id']:.10f} F2 a0={f2f['a0']:.10f} | B={fe['B']:.10f} F2 a1={f2f['a1']:.10f}"
                  f" (F2 uses h=1e-4 single diff)")
            print(f"   dc_gamma*16pi^2 here {U*ph['dcg']:+.5f}  F2 {U*f2p['dcg']:+.5f}   dc_e*16pi^2 here {U*fe['dce']:+.5f}  F2 {U*f2f['dcf']:+.5f}", flush=True)
    else:
        # box runs: mode = "box b1 b2 r c1 c2 N m lam"
        b1, b2, r, c1, c2 = [float(x) for x in sys.argv[2:7]]
        N = int(sys.argv[7]); m = float(sys.argv[8]); lam = float(sys.argv[9])
        if b1 < 0: b1 = b2 = None            # no fermion box: plain Wilson-naive lattice functions
        if c1 < 0: c1 = c2 = None            # no photon box: d(q) = 2 sin(q/2)
        law = Law(b1, b2, r, c1, c2, m)
        ph = photon(law, N); fe = fermion(law, N, lam)
        D = U * (fe["dce"] - ph["dcg"])
        print(f"b1={b1} b2={b2} r={r} c=({c1},{c2}) N={N} m={m} lam={lam} | P_E(w)*U={U*ph['PEw']:.4f} P_M*U={U*ph['PM']:.4f}"
              f" gauge P_E(rho)-P_E(w)={ph['gauge']:+.1e} Ward={ph['wi']:+.1e} | dc_g*U={U*ph['dcg']:+.4f}"
              f" [same-q {U*ph['dcg_sq']:+.4f}] | A*U={U*fe['A_id']:+.4f} B*U={U*fe['B']:+.4f} [tad {U*fe['tad']:+.4f}] dc_e*U={U*fe['dce']:+.4f}"
              f" | DELTA={D:+.4f}", flush=True)
    print(f"elapsed {time.time()-t0:.1f}s")
