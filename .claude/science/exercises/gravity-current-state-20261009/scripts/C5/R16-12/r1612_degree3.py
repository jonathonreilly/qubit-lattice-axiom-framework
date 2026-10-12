"""C5 R16-12: degree-3 Killing-sector closure of R12-1's completion with R16-8's Lemma-P placement.

Conventions (fixed once, calibrated by the continuum limit, see report sec. 2):
  {h_ij(x), E_kl(y)} = delta;  C_s[N] = int N R1(h) + int N[E.E - (trE)^2/2] + (1/2)int N h.K h + T00[N] + deg-3 ...
  R1(h)(q) = -s(q).h,  s_ij = q_i q_j - |q|^2 delta_ij;  C_j[xi] = int Kill(xi).E + P^m[xi] + P^g[xi] + deg-3
  G(E) = 2E - trE I  (hdot = G E),  K = linearised Einstein tensor (Edot = -K h), graviton speed 1.
  {C_s[N],C_s[M]} = C_j[M dN - N dM];  {C_j[e_c], C_s[N]} = -C_s[d_c N].
Matter: free one-band separable, Vlasov (leading order in the smearing momentum q, exact for the
  leading homogeneous symbols), eps^2 = m^2 + sum u(k_i), P = d(eps^2/2) = eps v (current-aligned),
  Delta_cb = eps (d_b P_c - delta_bc)  (diagonal for separable bands).
Per matter Fourier mode (q,k), leading order:
  omega = q.v,  delta_c = q.Delta_c / eps,  b_T = i q.Delta_c / (2|q|^2)  (forced by the degree-2 JS jet),
  sigma0 = (eps/2) v v  (forced by the degree-2 strain bracket; the W1 forward stress).
Degree-3 translation charge {P_c^tot, H} (weak: E-coefficient mod L = Im Kill, h-coefficient mod T = Im s):
  E: -i omega B + G A + i delta tau    h: -i omega A - K B + i delta sigma
Degree-3 boost charge {K_b^tot, H} = P_b^tot with K_b^sing = sum E.X f + h.Y f:
  E: -i omega X + G Y - B_b   (mod L)   h: -i omega Y - K X - A_b  (mod T)
"""
import os, sys
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sublum_copy import SymS, SymG, sstep, wrap

M = 0.3
out = []
def pr(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

# ---------------- matter laws (same as R16-8 script A) ----------------
B_IN, B_OUT = 2.0, 3.1
def s_box(k):
    kk = wrap(k); r = 1.0 - sstep((np.abs(kk) - B_IN) / (B_OUT - B_IN))
    return r * kk + (1 - r) * np.sin(kk)
S14, G14 = SymS(1.4), SymG(1.4)
def nd(f, k, h=1e-5):
    return (f(k + h) - f(k - h)) / (2 * h)
LAWS = {
    "S(1.4)": (lambda k: S14.s(k) ** 2, lambda k: 2 * S14.s(k) * S14.ds(k)),
    "G(1.4)": (G14.g, G14.dg),
    "L-box(2.0)": (lambda k: s_box(k) ** 2, lambda k: 2 * s_box(k) * nd(s_box, k)),
}
def matter(law, k):
    u, up = LAWS[law]
    k = np.asarray(k, float)
    eps = np.sqrt(M * M + sum(u(np.array([k[i]]))[0] for i in range(3)))
    P = np.array([0.5 * up(np.array([k[i]]))[0] for i in range(3)])
    dP = np.array([nd(lambda x: 0.5 * up(x), np.array([k[i]]), 1e-4)[0] for i in range(3)])
    v = P / eps
    Delta = np.diag(eps * (dP - 1.0))
    return eps, v, P, Delta

# ---------------- tensor algebra at fixed qhat ----------------
I3 = np.eye(3)
def sym(a, b):
    return np.outer(a, b) + np.outer(b, a)
def frame(qh):
    a = np.array([1.0, 0, 0]) if abs(qh[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = a - qh * (qh @ a); e1 /= np.linalg.norm(e1); e2 = np.cross(qh, e1)
    return e1, e2
def basis(qh):
    """orthonormal basis of symmetric 3x3: [qq, vL1, vL2, T, TT1, TT2]"""
    e1, e2 = frame(qh); Pp = I3 - np.outer(qh, qh)
    return [np.outer(qh, qh), sym(qh, e1) / np.sqrt(2), sym(qh, e2) / np.sqrt(2), Pp / np.sqrt(2),
            (np.outer(e1, e1) - np.outer(e2, e2)) / np.sqrt(2), sym(e1, e2) / np.sqrt(2)]
def comps(Mx, bas):
    return np.array([np.sum(b * Mx) for b in bas])
def Gop(Mx):
    return 2 * Mx - np.trace(Mx) * I3
def Kop(Mx, q):
    """linearised Einstein tensor G1(h)(q):  R_ij = 1/2(-q_k q_i h_kj - q_k q_j h_ki + q_i q_j trh + q^2 h_ij)."""
    q2 = q @ q; tr = np.trace(Mx)
    R = 0.5 * (-np.outer(q, q @ Mx) - np.outer(Mx @ q, q) + np.outer(q, q) * tr + q2 * Mx)
    Rs = -q @ Mx @ q + q2 * tr
    return R - 0.5 * I3 * Rs
def smat(q):
    return np.outer(q, q) - (q @ q) * I3

L_IDX, T_IDX, TT_IDX = [0, 1, 2], [3], [4, 5]

def solve_translation(q, eps, v, Delta, c, tau=None):
    """unknowns: B (6 comps, T fixed) and A (6 comps). Weak equations: E-coef T,TT = 0; h-coef L,TT = 0."""
    qh = q / np.linalg.norm(q); bas = basis(qh)
    om = q @ v; dl = (q @ Delta[c]) / eps
    bT_val = 1j * (q @ Delta[c]) / (2 * (q @ q))       # coefficient on (I - qq)
    bT = bT_val * np.sqrt(2)                           # component on normalised basis vector Pp/sqrt2
    sig = 0.5 * eps * np.outer(v, v)
    tauM = np.zeros((3, 3)) if tau is None else tau
    # linear maps on component vectors (6-dim): build matrices for G and K
    Gm = np.array([[np.sum(bi * Gop(bj)) for bj in bas] for bi in bas])
    Km = np.array([[np.sum(bi * Kop(bj, q)) for bj in bas] for bi in bas])
    sigc, tauc = comps(sig, bas), comps(tauM, bas)
    # unknown vector z = [B(6), A(6)] complex; constraint B_T = bT
    rows, rhs = [], []
    for i in T_IDX + TT_IDX:      # E-coef: -i om B + G A + i dl tau
        r = np.zeros(12, complex); r[i] += -1j * om; r[6:] += Gm[i]
        rows.append(r); rhs.append(-1j * dl * tauc[i])
    for i in L_IDX + TT_IDX:      # h-coef: -i om A - K B + i dl sigma
        r = np.zeros(12, complex); r[6 + i] += -1j * om; r[:6] += -Km[i]
        rows.append(r); rhs.append(-1j * dl * sigc[i])
    r = np.zeros(12, complex); r[3] = 1.0; rows.append(r); rhs.append(bT)   # B_T fixed
    Am, bm = np.array(rows), np.array(rhs)
    z, *_ = np.linalg.lstsq(Am, bm, rcond=None)
    res = np.linalg.norm(Am @ z - bm) / max(np.linalg.norm(bm), 1e-300)
    Bt = sum(z[i] * bas[i] for i in range(6)); At = sum(z[6 + i] * bas[i] for i in range(6))
    return Bt, At, res, om, dl, bT_val, Km, Gm, bas

def solve_boost(q, Bb, Ab, bas, Km, Gm):
    """K_b^sing = E.X + h.Y; weak equations E: (-i om X + G Y) - B = 0 on T,TT;  h: (-i om Y - K X) - A = 0 on L,TT."""
    return None

pr("C5 R16-12 script (r1612_degree3.py): degree-3 Killing-sector closure, d = 3, m =", M)
rng = np.random.default_rng(161200)
KS = [np.array([2.0, 0.3, 0.2]), np.array([2.6, 0.1, -0.4]), np.array([1.6, 1.6, 0.0]), np.array([2.3, -1.9, 0.7])]

pr("\n(1) translation sector {P_c^tot, H} at degree 3, weak, tau = 0, sigma = W1 forward stress (eps/2) v v")
pr("    columns: law, k, c, max residual over 200 random qhat, max |q| |A| (bounded = degree 0), max |q|^2|B|/|q.Delta_c|,")
pr("    JJ check: max | q.A - (1/2)(q.Delta_c) v | / |q|  (A's divergence vs the analytic JJ repair)")
for law in LAWS:
    for k in KS:
        eps, v, P, Delta = matter(law, k)
        if np.max(np.abs(Delta)) < 1e-8:
            continue
        for c in range(3):
            if abs(Delta[c, c]) < 1e-8:
                continue
            mres = mA = mB = mjj = 0.0
            for _ in range(200):
                qh = rng.normal(size=3); qh /= np.linalg.norm(qh); q = 1e-3 * qh
                Bt, At, res, om, dl, bT, Km, Gm, bas = solve_translation(q, eps, v, Delta, c)
                mres = max(mres, res); mA = max(mA, np.max(np.abs(At)))
                mB = max(mB, np.max(np.abs(Bt)) * (q @ q) / max(abs(q @ Delta[c]), 1e-300))
                jj = At @ q - 0.5 * (q @ Delta[c]) * v
                mjj = max(mjj, np.linalg.norm(jj) / np.linalg.norm(q))
            pr(f"  {law:10s} k={np.round(k,2)} c={c}: |v|={np.linalg.norm(v):.4f} resid {mres:.1e}; max|A| {mA:.3f};"
               f" max|q|^2|B|/|q.D| {mB:.3f}; JJ mismatch {mjj:.1e}")

pr("\n(2) TT (helicity-2) denominators: B_TT ~ delta sigma_TT / (|q|^2 - omega^2). min over qhat of 1-(qhat.v)^2")
for law in LAWS:
    for k in KS:
        eps, v, P, Delta = matter(law, k)
        qs = rng.normal(size=(20000, 3)); qs /= np.linalg.norm(qs, axis=1)[:, None]
        den = 1 - (qs @ v) ** 2
        pr(f"  {law:10s} k={np.round(k,2)}: |v| = {np.linalg.norm(v):.4f}, min_qhat (1-(qhat.v)^2) = {den.min():+.4f}"
           f"  ({'no Cherenkov cone' if den.min() > 0 else 'Cherenkov cone: B_TT pole unless tau_TT ~ 1/|q| (non-local H)'})")

pr("\n(2b) TT check at a superluminal L-box edge mode: (beta) solve near the cone qhat.v = 1")
law = "L-box(2.0)"; k = KS[1]; eps, v, P, Delta = matter(law, k)
vh = v / np.linalg.norm(v); e1, e2 = frame(vh); th0 = np.arccos(1 / np.linalg.norm(v))
for dth in (1e-1, 1e-2, 1e-3):
    qh = np.cos(th0 + dth) * vh + np.sin(th0 + dth) * e1; q = 1e-3 * qh
    Bt, At, res, *_ = solve_translation(q, eps, v, Delta, 0)
    pr(f"  angle from cone {dth:.0e}: qhat.v = {qh @ v:.5f}, |q|^2 |B| = {np.max(np.abs(Bt))*(q@q):.3e}, resid {res:.1e}")

pr("\n(3) boost sector {K_b^tot, H} = P_b^tot at degree 3 (scalar/helicity-0 part, rigid):")
pr("    forced: Y_qq = b_T,  X_T = 2 i b_T / omega  ->  |q|^2 |X_T| = |qhat.Delta_b| / |qhat.v|")
pr("    solve the weak equations numerically and approach the plane qhat.v = 0 at fixed qhat.Delta_b != 0")
for law in ("S(1.4)", "G(1.4)"):
    for k in KS[:3]:
        eps, v, P, Delta = matter(law, k)
        b = int(np.argmax(np.abs(np.diag(Delta))))
        if abs(Delta[b, b]) < 1e-8:
            continue
        vh = v / np.linalg.norm(v)
        # a direction in the plane qhat.v = 0 with qhat.Delta_b maximal
        w = Delta[b] - vh * (vh @ Delta[b]); w /= np.linalg.norm(w)
        row = []
        for dth in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5):
            qh = np.cos(dth) * w + np.sin(dth) * vh; q = 1.0 * qh   # leading symbols are homogeneous: |q| = 1 avoids conditioning loss
            Bt, At, res, om, dl, bT, Km, Gm, bas = solve_translation(q, eps, v, Delta, b)
            Bc, Ac = comps(Bt, bas), comps(At, bas)
            # unknowns X(6), Y(6)
            rows, rhs = [], []
            for i in T_IDX + TT_IDX:
                r = np.zeros(12, complex); r[i] += -1j * om; r[6:] += Gm[i]; rows.append(r); rhs.append(Bc[i])
            for i in L_IDX + TT_IDX:
                r = np.zeros(12, complex); r[6 + i] += -1j * om; r[:6] += -Km[i]; rows.append(r); rhs.append(Ac[i])
            Am, bm = np.array(rows), np.array(rhs)
            z, *_ = np.linalg.lstsq(Am, bm, rcond=None)
            r2 = np.linalg.norm(Am @ z - bm) / np.linalg.norm(bm)
            XT = z[3] / np.sqrt(2); pred = 2j * bT / om
            row.append((dth, abs(XT) * (q @ q), abs(XT / pred - 1), r2, abs(q @ Delta[b]) / np.linalg.norm(q)))
        pr(f"  {law} k={np.round(k,2)} b={b}: " + "; ".join(
            f"qhat.v={np.sin(d)*np.linalg.norm(v):.1e}: |q|^2|X_T|={x:.2e} (vs 2ib_T/om: {e:.0e}, resid {r:.0e})"
            for d, x, e, r, _ in row) + f"; |qhat.Delta_b| = {row[-1][4]:.3f}")

pr("\n(4) scalar-sector consistency is an identity: sigma_qq needed = eps omega^2/(2|q|^2) = qhat.sigma0.qhat")
for law in ("S(1.4)", "G(1.4)"):
    eps, v, P, Delta = matter(law, KS[0])
    qh = rng.normal(size=3); qh /= np.linalg.norm(qh)
    need = eps * (qh @ v) ** 2 / 2; have = qh @ (0.5 * np.outer(v, P)) @ qh
    pr(f"  {law}: needed {need:.12f}, W1 forward stress {have:.12f}, difference {need-have:.1e}")

pr("\n(5) finite-q resonances (TT, helicity 2): does |eps(k+q/2)-eps(k-q/2)| reach omega_g(q) = |2 sin(q/2)| anywhere?")
for law in ("S(1.4)", "G(1.4)"):
    u, up = LAWS[law]
    def epsf(K):
        return np.sqrt(M * M + u(K[:, 0]) + u(K[:, 1]) + u(K[:, 2]))
    k = KS[1]
    Q = rng.uniform(-np.pi, np.pi, size=(200000, 3))
    om = np.abs(epsf(k + Q / 2) - epsf(k - Q / 2)); og = np.linalg.norm(2 * np.sin(Q / 2), axis=1)
    ratio = om / og
    pr(f"  {law} k={k}: max |omega_m|/omega_g over 2e5 random q = {ratio.max():.3f}; fraction with ratio>1: {np.mean(ratio>1):.4f};"
       f" small-|q| (<0.3) max ratio {ratio[np.linalg.norm(Q,axis=1)<0.3].max():.3f}")

with open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w") as f:
    f.write("\n".join(out) + "\n")
