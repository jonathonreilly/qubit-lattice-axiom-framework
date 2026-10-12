"""R9-8 (C5 round 9): box QED with a Lemma-C-allowed, invariant-mass-profiled FRAME ROTATION of the charge,
plus exactly gauge-invariant (symmetrised axis-staircase Peierls) minimal coupling.  One-loop photon and electron speeds.

LAW "BQ-W" (reuses R8-5's BQ fermion symbol h, photon and conventions; r85_box_qed.py copied unchanged next to this file)
  Unrotated symbol h(k) = sum_j S(k_j) alpha_j + M(k) beta,  M = m + sum_j W(k_j)   (R8-5 BQ; box-exact Dirac in the box).
  Frame: psi = W(k) psi',  W(k) = exp( beta alpha.S^ * phi(k)/2 ),  phi = (1 - F(E(k))) theta(k),  tan theta = |S|/M.
     -> h_W(k) = W^dag h W = E [ beta cos(F theta) + alpha.S^ sin(F theta) ]   (still in span{alpha_x,alpha_y,alpha_z,beta}).
     F = C^inf plateau in the band energy E(k) = |h(k)|: F = 1 for E <= E1, 0 for E >= E2.  At zero photon momentum the created
     pair (k,-k) has invariant mass 2E(k), so the profile is the INV form factor F(M^2/4) evaluated on the forward pairs.
     F = 1 (E1 = E2 = inf) is exactly BQ.  F = 0 is the full band (Foldy-Wouthuysen) frame: h_W = E beta, no pair creation.
  Charge: on-site for psi'  (density mu(k',k) = W(k')W(k)^dag in the psi frame; Lemma C rigid: charge 1 at every k).
  Coupling: psi' hops carry Wilson lines along axis staircases, averaged over the 6 axis orders (cubic symmetric, exactly
     gauge invariant for the R8-5 forward-difference photon).  Vertex V_j(p,k) = dbar_j(p,k)/Dhat_j(p-k), with
     dbar_j = [2(h{j}-h{}) + (h{a,j}-h{a}) + (h{b,j}-h{b}) + 2(h{a,b,j}-h{a,b})]/6,   h{B} = h_W at the momentum whose
     components in B are taken from p and the rest from k.  sum_j Dhat_j V_j = h_W(p) - h_W(k) exactly (telescoping).
     For separable h (F = 1) dbar_j = h_j(p_j) - h_j(k_j): R8-5's vertex.
  Seagull (tadpole, photons q,-q on the same axis j): [h(p+q_j e_j) + h(p-q_j e_j) - 2h(p)]/d(q_j)^2, any path order.
  Photon P_M vertex (q = q xhat, polarisation y): V_y = [d_y h(k) + d_y h(k + q xhat)]/2 (x before y in 3 of 6 orders).

QUANTITIES exactly as R8-5 (Clifford closed forms, k0 integrals in closed form, Euclidean Feynman gauge, photon mass lam):
  dc_gamma = (P_M - P_E)/2,  dc_e = B - A,  Delta = (dc_e - dc_gamma)*16 pi^2  (units e^2/16pi^2, one Dirac species).
VALIDATION: F = 1 must reproduce r85_box_qed.py (BQ) to quadrature precision.
"""
import numpy as np, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r85_box_qed import Law, plateau, kgrid1, _phi

U = 16 * np.pi ** 2

class LawW(Law):
    def __init__(self, b1, b2, r, c1, c2, m, E1=None, E2=None):
        super().__init__(b1, b2, r, c1, c2, m)
        self.E1, self.E2 = E1, E2
    def F(self, E):
        if self.E1 is None:
            return np.ones_like(E)
        return 1.0 - _phi((E - self.E1) / (self.E2 - self.E1))
    def hW(self, kx, ky, kz):
        Sx, Sy, Sz = self.S(kx), self.S(ky), self.S(kz)
        M = self.m + self.W(kx) + self.W(ky) + self.W(kz)
        Sx, Sy, Sz, M = np.broadcast_arrays(Sx, Sy, Sz, M)
        S2 = Sx ** 2 + Sy ** 2 + Sz ** 2
        E = np.sqrt(S2 + M ** 2)
        if self.E1 is None:
            return (Sx, Sy, Sz, M)
        Sp = np.sqrt(S2)
        th = np.arctan2(Sp, M)
        th_over_Sp = np.where(Sp > 1e-12, th / np.where(Sp > 1e-12, Sp, 1.0), 1.0 / M)
        F = self.F(E)
        Th = F * th
        c = E * np.sinc(Th / np.pi) * F * th_over_Sp          # = E sin(F th)/|S|
        return (c * Sx, c * Sy, c * Sz, E * np.cos(Th))

def comps_norm(h):
    E = np.sqrt(h[0] ** 2 + h[1] ** 2 + h[2] ** 2 + h[3] ** 2)
    return tuple(c / E for c in h), E

def dh(law, kx, ky, kz, axis, hstep=1e-3):
    """4th-order central difference of h_W along axis (0,1,2) -> tuple of 4 Clifford comps."""
    def at(s):
        k = [kx, ky, kz]; k[axis] = k[axis] + s
        return law.hW(*k)
    f2, f1, m1, m2 = at(2 * hstep), at(hstep), at(-hstep), at(-2 * hstep)
    return tuple((-f2[i] + 8 * f1[i] - 8 * m1[i] + m2[i]) / (12 * hstep) for i in range(4))

def dot4(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]

# ---------------------------------------------------------------- photon (R8-5 formulas, non-separable vertex)
def photon(law, N, qs=(0.02, 0.04), chunk=8):
    k1 = kgrid1(N)
    KY, KZ = np.meshgrid(k1, k1, indexing="ij")
    acc = dict(PEw=0.0, chiyy0=0.0)
    acc_q = {q: dict(chi00=0.0, chiyy=0.0) for q in qs}
    for i0 in range(0, N, chunk):
        kx = k1[i0:i0 + chunk][:, None, None] + 0 * KY[None]
        ky = KY[None] + 0 * kx; kz = KZ[None] + 0 * kx
        n, E = comps_norm(law.hW(kx, ky, kz))
        x = dh(law, kx, ky, kz, 1)
        xn = dot4(x, n); x2 = dot4(x, x)
        acc["PEw"] += np.sum((x2 - xn ** 2) / (2 * E ** 3))
        acc["chiyy0"] += np.sum(2 * (2 * x2 - 2 * xn ** 2) / (2 * E))
        for q in qs:
            for sgn in (+1, -1):
                n2, E2 = comps_norm(law.hW(kx + sgn * q, ky, kz))
                xq = dh(law, kx + sgn * q, ky, kz, 1)
                X = tuple(0.5 * (x[i] + xq[i]) for i in range(4))     # symmetrised staircase vertex
                nn = dot4(n, n2); X2 = dot4(X, X); Xn = dot4(X, n); Xn2 = dot4(X, n2)
                acc_q[q]["chi00"] += np.sum((1 - nn) / (E + E2))
                acc_q[q]["chiyy"] += np.sum((X2 * (1 + nn) - 2 * Xn * Xn2) / (E + E2))
    V = N ** 3
    PEw = acc["PEw"] / V
    PEr, PM = [], []
    for q in qs:
        dq2 = law.d(np.array(q)) ** 2
        PEr.append(acc_q[q]["chi00"] / V / dq2)
        PM.append((acc["chiyy0"] / V - acc_q[q]["chiyy"] / V) / dq2)
    PEr_x = (4 * PEr[0] - PEr[1]) / 3; PM_x = (4 * PM[0] - PM[1]) / 3
    return dict(PEw=PEw, PEr=PEr_x, PM=PM_x, dcg=(PM_x - PEw) / 2, gauge=PEr_x - PEw)

# ---------------------------------------------------------------- fermion self-energy at p = 0 (Feynman gauge)
def dbar(law, p, kx, ky, kz):
    """symmetrised-staircase h-differences dbar_j(p,k), j = x,y,z; p = (px,0,0); returns list of 3 Clifford tuples."""
    P = (p, 0.0, 0.0); K = (kx, ky, kz)
    cache = {}
    def h(B):
        if B not in cache:
            mom = [P[i] + 0 * K[i] if i in B else K[i] for i in range(3)]
            cache[B] = law.hW(*mom)
        return cache[B]
    out = []
    for j in range(3):
        a, b = [i for i in range(3) if i != j]
        def diff(B):
            hi = h(tuple(sorted(B + (j,)))); lo = h(tuple(sorted(B)))
            return tuple(hi[c] - lo[c] for c in range(4))
        d0, da, db, dab = diff(()), diff((a,)), diff((b,)), diff((a, b))
        out.append(tuple((2 * d0[c] + da[c] + db[c] + 2 * dab[c]) / 6 for c in range(4)))
    return out, h(())

def fermion(law, N, lam, hp=(1e-3, 2e-3), chunk=8):
    q1 = kgrid1(N)
    QY, QZ = np.meshgrid(q1, q1, indexing="ij")
    dqy2, dqz2 = law.d(QY) ** 2, law.d(QZ) ** 2
    A_id = 0.0; tadd = 0.0
    sun = {p: 0.0 for p in [s * h for h in hp for s in (+1, -1)]}
    for i0 in range(0, N, chunk):
        qx = q1[i0:i0 + chunk][:, None, None] + 0 * QY[None]
        qy = QY[None] + 0 * qx; qz = QZ[None] + 0 * qx
        d2 = (law.d(qx) ** 2, dqy2[None] + 0 * qx, dqz2[None] + 0 * qx)
        Om = np.sqrt(d2[0] + d2[1] + d2[2] + lam ** 2)
        # tadpole: (1/2) sum_j < d/dp_x [h(p+q_j e_j)+h(p-q_j e_j)-2h(p)]_{alpha_x} / (2 Om d_j^2) >  at p = 0
        h1 = hp[0]
        tsum = 0.0
        for j, qj in enumerate((qx, qy, qz)):
            vals = {}
            for s in (+1, -1):
                pv = s * h1
                base = [pv + 0 * qx, 0 * qx, 0 * qx]
                up = list(base); up[j] = up[j] + qj
                dn = list(base); dn[j] = dn[j] - qj
                hu, hd, h0 = law.hW(*up), law.hW(*dn), law.hW(*base)
                vals[s] = hu[0] + hd[0] - 2 * h0[0]
            tsum = tsum + (vals[1] - vals[-1]) / (2 * h1) / (2 * Om * d2[j])
        tadd += 0.5 * np.sum(tsum)
        for p in list(sun.keys()) + [0.0]:
            db, hk = dbar(law, p, p - qx, -qy, -qz)
            n, E = comps_norm(hk)
            if p == 0.0:
                s2 = sum(dot4(db[j], db[j]) / d2[j] for j in range(3))
                A_id += np.sum((s2 - 1) / (2 * Om * (Om + E) ** 2))
                continue
            # alpha_x component of sum_j (2 (d_j.n) d_j - |d_j|^2 n)/d_j^2 - n
            comp = -n[0]
            for j in range(3):
                dn_ = dot4(db[j], n)
                comp = comp + (2 * dn_ * db[j][0] - dot4(db[j], db[j]) * n[0]) / d2[j]
            sun[p] += np.sum(-comp / (2 * Om * (Om + E)))
    V = N ** 3
    A_id /= V; tadd /= V
    for p in sun: sun[p] /= V
    h1, h2 = hp
    D1 = (sun[h1] - sun[-h1]) / (2 * h1); D2 = (sun[h2] - sun[-h2]) / (2 * h2)
    sund = (4 * D1 - D2) / 3
    B = sund + tadd
    return dict(A_id=A_id, B=B, sun=sund, tad=tadd, dce=B - A_id)

if __name__ == "__main__":
    t0 = time.time()
    # args: b1 b2 r c1 c2 N m lam E1 E2   (E1 < 0 -> no frame rotation, i.e. BQ)
    b1, b2, r, c1, c2 = [float(x) for x in sys.argv[1:6]]
    N = int(sys.argv[6]); m = float(sys.argv[7]); lam = float(sys.argv[8])
    E1, E2 = float(sys.argv[9]), float(sys.argv[10])
    if E1 < 0: E1 = E2 = None
    law = LawW(b1, b2, r, c1, c2, m, E1, E2)
    ph = photon(law, N); fe = fermion(law, N, lam)
    D = U * (fe["dce"] - ph["dcg"])
    print(f"BQ-W b=({b1},{b2}) r={r} c=({c1},{c2}) E=({E1},{E2}) N={N} m={m} lam={lam} | P_E(w)*U={U*ph['PEw']:.4f}"
          f" P_E(rho)-P_E(w)={ph['gauge']:+.1e} P_M*U={U*ph['PM']:.4f} | dc_g*U={U*ph['dcg']:+.4f} | A*U={U*fe['A_id']:+.4f}"
          f" B*U={U*fe['B']:+.4f} [tad {U*fe['tad']:+.4f}] dc_e*U={U*fe['dce']:+.4f} | DELTA={D:+.4f}  ({time.time()-t0:.0f}s)", flush=True)
