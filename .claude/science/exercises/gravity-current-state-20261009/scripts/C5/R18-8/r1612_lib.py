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

