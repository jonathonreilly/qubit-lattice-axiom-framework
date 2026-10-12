"""C5 R16-12 controls for r1612_degree3.py:
 (A) sign-flip control: with sigma = -(eps/2) v v (wrong sign) the weak translation system must be inconsistent;
 (B) rigidity: null space of the weak boost system has no X_T component (X_T is forced, not a minimal-norm choice);
 (C) strong (undeformed, no constraint-proportional terms) translation system: residual and size of the needed A_T.
"""
import os, sys
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util, io, contextlib
spec = importlib.util.spec_from_file_location("r", os.path.join(os.path.dirname(os.path.abspath(__file__)), "r1612_degree3.py"))
r = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(r)          # rebuilds r1612_degree3.out identically (deterministic seed)
out = []
def pr(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
rng = np.random.default_rng(16121)
law, k = "G(1.4)", np.array([2.6, 0.1, -0.4])
eps, v, P, Delta = r.matter(law, k)

def system(q, c, sig_sign=1.0, strong=False):
    qh = q / np.linalg.norm(q); bas = r.basis(qh)
    om = q @ v; dl = (q @ Delta[c]) / eps
    bT = 1j * (q @ Delta[c]) / (2 * (q @ q)) * np.sqrt(2)
    sigc = r.comps(sig_sign * 0.5 * eps * np.outer(v, v), bas)
    Gm = np.array([[np.sum(bi * r.Gop(bj)) for bj in bas] for bi in bas])
    Km = np.array([[np.sum(bi * r.Kop(bj, q)) for bj in bas] for bi in bas])
    Eidx = list(range(6)) if strong else r.T_IDX + r.TT_IDX
    hidx = list(range(6)) if strong else r.L_IDX + r.TT_IDX
    rows, rhs = [], []
    for i in Eidx:
        z = np.zeros(12, complex); z[i] += -1j * om; z[6:] += Gm[i]; rows.append(z); rhs.append(0.0)
    for i in hidx:
        z = np.zeros(12, complex); z[6 + i] += -1j * om; z[:6] += -Km[i]; rows.append(z); rhs.append(-1j * dl * sigc[i])
    z = np.zeros(12, complex); z[3] = 1.0; rows.append(z); rhs.append(bT)
    return np.array(rows), np.array(rhs, complex), Gm, Km, bas, om, bT

pr("(A) sign-flip control (G(1.4), k = (2.6, 0.1, -0.4), c = 0): relative residual of the weak translation system")
for sgn in (+1.0, -1.0):
    mx = 0
    for _ in range(50):
        qh = rng.normal(size=3); qh /= np.linalg.norm(qh)
        A, b, *_ = system(qh, 0, sgn)
        zz, *_ = np.linalg.lstsq(A, b, rcond=None); mx = max(mx, np.linalg.norm(A @ zz - b) / np.linalg.norm(b))
    pr(f"  sigma = {sgn:+.0f} x (eps/2) v v : max residual {mx:.2e}")

pr("\n(B) rigidity of the boost scalar sector: null space of the weak boost operator (unknowns X(6), Y(6))")
qh = rng.normal(size=3); qh /= np.linalg.norm(qh)
A, b, Gm, Km, bas, om, bT = system(qh, 0)
rows = []
for i in r.T_IDX + r.TT_IDX:
    z = np.zeros(12, complex); z[i] += -1j * om; z[6:] += Gm[i]; rows.append(z)
for i in r.L_IDX + r.TT_IDX:
    z = np.zeros(12, complex); z[6 + i] += -1j * om; z[:6] += -Km[i]; rows.append(z)
Op = np.array(rows); U, s, Vh = np.linalg.svd(Op)
null = Vh[np.sum(s > 1e-10 * s.max()):].conj().T
pr(f"  operator 8 x 12, rank {np.sum(s > 1e-10*s.max())}; null-space dimension {null.shape[1]};"
   f" max |X_T component| over null vectors = {np.max(np.abs(null[3])) if null.size else 0:.1e};"
   f" max |Y_qq component| = {np.max(np.abs(null[6])) if null.size else 0:.1e}")
pr("  (null directions are X_L, Y_T (constraint-proportional) and gauge combinations; X_T and Y_qq are fixed)")

pr("\n(C) strong closure (every component, no constraint-proportional terms), translation sector:")
for c in (0,):
    for t in (1e-1, 1e-2, 1e-3):
        mx, mAT = 0, 0
        for _ in range(50):
            qh = rng.normal(size=3); qh /= np.linalg.norm(qh)
            A, b, Gm, Km, bas, om, bT = system(qh, c, strong=True)
            zz, *_ = np.linalg.lstsq(A, b, rcond=None); mx = max(mx, np.linalg.norm(A @ zz - b) / np.linalg.norm(b))
        # approach qhat.v = 0
        vh = v / np.linalg.norm(v); w = Delta[c] - vh * (vh @ Delta[c]); w /= np.linalg.norm(w)
        qh = np.cos(t) * w + np.sin(t) * vh
        A, b, Gm, Km, bas, om, bT = system(qh, c, strong=True)
        zz, *_ = np.linalg.lstsq(A, b, rcond=None)
        pr(f"  random qhat: max residual {mx:.1e};  at qhat.v = {qh@v:.1e}: |A_T| = {abs(zz[6+3]):.2e}, |B_vL| = {np.max(np.abs(zz[1:3])):.2e}")
pr("  strong closure needs A_T, B_vL ~ 1/(qhat.v): unbounded on the sphere -> only weak closure (with")
pr("  constraint-proportional terms, i.e. matter-dependent structure functions or field-dependent lapse/shift) is in class C.")

with open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w") as f:
    f.write("\n".join(out) + "\n")

pr("\n(D) factorisation Phi_c = delta_c * Xi (Xi independent of c): compare B_c/delta_c, A_c/delta_c for c = 0, 1")
for law, kk in (("S(1.4)", np.array([1.6, 1.6, 0.0])), ("G(1.4)", np.array([2.3, -1.9, 0.7])), ("G(1.4)", np.array([1.6, 1.6, 0.0]))):
    e_, v_, P_, D_ = r.matter(law, kk)
    mx = 0
    for _ in range(50):
        qh = rng.normal(size=3); qh /= np.linalg.norm(qh)
        res = []
        for c in (0, 1):
            Bt, At, rr, om, dl, bT, *_ = r.solve_translation(qh, e_, v_, D_, c)
            res.append((Bt / dl, At / dl))
        mx = max(mx, np.max(np.abs(res[0][0] - res[1][0])) / np.max(np.abs(res[0][0])),
                 np.max(np.abs(res[0][1] - res[1][1])) / np.max(np.abs(res[0][1])))
    pr(f"  {law} k={kk}: max relative difference of Phi_c/delta_c between c=0 and c=1: {mx:.1e}")
pr("  => {P_c^tot, P_d^tot} = 0 at degree 3 (antisymmetric delta_c delta_d cancels), and Phi_c = {P_c^0, W}")
pr("     with W = -i sum E.Xi_E f + h.Xi_h f: (beta) is the first-order canonical relocation of a system with bare P^0.")
with open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w") as f:
    f.write("\n".join(out) + "\n")
