"""SIGN-1 follow-up A: Kramers-class pair {T2 = Theta_1, T1 = (1 x i Gamma^9) T2} for X2's quartic.
Channels: U(1)_c-neutral Hermitian bilinears (U(1)_c = (9,10)-plane rotation of Spin(10)), organised under
SU(2)_spin x Spin(8) x <Z4, Theta>.  SDP: does Q = l1 sum B^dag B + l2 sum (BB + h.c.) decompose into
Theta-even channels with attractive (<= 0) and Theta-odd channels with repulsive (>= 0) coefficients?
"""
import numpy as np, itertools, sys, time, resource
import cvxpy as cp
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from common import *
t0 = time.time()
def P(*a): print(*a); sys.stdout.flush()
def mem(): return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20
rng = np.random.default_rng(91)

G = G9; I16 = np.eye(16)
O2 = antireal(np.kron(E, I16).astype(complex))                 # T2 = (i sigma_y) K
u = 1j * G[8]; OU = realify(np.kron(np.eye(2), u))             # U = 1 x i Gamma^9
O1 = O2 @ OU                                                   # T1 = U T2
P(f"T1^2 = -1: {np.allclose(O1 @ O1, -np.eye(64))}; T2^2 = -1: {np.allclose(O2 @ O2, -np.eye(64))}; "
  f"T1 T2 = -T2 T1: {np.allclose(O1 @ O2, -O2 @ O1)}")

w, Wv = np.linalg.eigh(G[8]); Ws = Wv[:, w > 0]; Wc = Wv[:, w < 0]; Ps = Ws @ Ws.T; Pc = Wc @ Wc.T
SIG = [np.eye(2, dtype=complex), X.astype(complex), SY, Z.astype(complex)]

def a_density(Mh):
    K = density_K(Mh); a = -2j * K; assert np.abs(a.imag).max() < 1e-12; return a.real
def a_pair(Mp, part):
    K = pairing_K(Mp)
    return (4 * K.imag) if part == "Re" else (4 * K.real)

def sym_traceless_basis(n):
    out = []
    for i in range(n):
        for j in range(i, n):
            S = np.zeros((n, n)); S[i, j] = S[j, i] = 1
            out.append(S)
    # remove trace: Gram-Schmidt against identity
    I = np.eye(n) / np.sqrt(n); B = []
    for S in out:
        S = S - np.sum(S * I) * I
        for Bb in B: S = S - np.sum(S * Bb) * Bb
        nr = np.linalg.norm(S)
        if nr > 1e-10: B.append(S / nr)
    assert len(B) == n * (n + 1) // 2 - 1
    return B

fam = {}   # name -> list of real antisymmetric a-matrices
for blk, Pb, Wb in (("s", Ps, Ws), ("c", Pc, Wc)):
    Xs = {"1": [Pb.astype(complex)],
          "28": [1j * Pb @ G[a] @ G[b] @ Pb for a in range(8) for b in range(a + 1, 8)],
          "35": [(Wb @ S @ Wb.T).astype(complex) for S in sym_traceless_basis(8)]}
    for xt, Xl in Xs.items():
        for st, sl in (("sing", [SIG[0]]), ("trip", SIG[1:])):
            fam[f"dens:{st}:{xt}:{blk}"] = [a_density(np.kron(sg, Xm)) for sg in sl for Xm in Xl]
Ys = {"8v": [Ps @ G[a] @ Pc for a in range(8)],
      "56v": [Ps @ G[a] @ G[b] @ G[c] @ Pc for a, b, c in itertools.combinations(range(8), 3)]}
for yt, Yl in Ys.items():
    for st, tl in (("sing", [E.astype(complex)]), ("trip", [E @ SIG[i] for i in (1, 2, 3)])):
        for part in ("Re", "Im"):
            mats = []
            for tau in tl:
                for Y in Yl:
                    Mp = np.kron(tau, Y); Mp = Mp - Mp.T
                    mats.append(a_pair(Mp, part))
            fam[f"pair:{st}:{yt}:{part}"] = mats

# orthonormalise each family (s/c doubled families with the same coefficients); parity and P-commutation checks
def orthonormalise(ms, coef=None):
    A = np.array([m.ravel() for m in ms])
    if coef is None:
        Gm = A @ A.T; L = np.linalg.cholesky(Gm); coef = np.linalg.inv(L)
    B = coef @ A
    return [b.reshape(64, 64) for b in B], coef
famo = {}; info = {}
for nm in fam:
    if nm.endswith(":c") and nm.startswith("dens") and (":1:" in nm or ":28:" in nm):
        continue
    ms, coef = orthonormalise(fam[nm]); famo[nm] = ms
    if nm.startswith("dens") and (":1:" in nm or ":28:" in nm):
        nc = nm[:-1] + "c"
        msc, _ = orthonormalise(fam[nc], coef)
        Gc = np.array([m.ravel() for m in msc]); dev = np.abs(Gc @ Gc.T - np.eye(len(msc))).max()
        assert dev < 1e-10, f"s/c Gram mismatch {nm}: {dev}"
        famo[nc] = msc
tot = 0
for nm, ms in famo.items():
    par = set(); com = set()
    for a in ms:
        t = O2.T @ a @ O2
        par.add("even" if np.allclose(t, -a) else ("odd" if np.allclose(t, a) else "mixed"))
        com.add(np.allclose(OU.T @ a @ OU, a))
        t1 = O1.T @ a @ O1
        par.add("T1even" if np.allclose(t1, -a) else ("T1odd" if np.allclose(t1, a) else "T1mixed"))
    info[nm] = (len(ms), par, com); tot += len(ms)
    P(f"  {nm:26s} dim {len(ms):4d}  parity {sorted(par)}  commutes with U: {com}")
P(f"total channel dimension {tot} (expected 1024)")
del fam
A_all = np.array([a.ravel() for ms in famo.values() for a in ms])
P(f"orthonormal across families: max |Gram - 1| = {np.abs(A_all @ A_all.T - np.eye(len(A_all))).max():.1e}")
del A_all

# samples and 4-forms
n = 64; S = 3000
quads = np.array(sorted({tuple(sorted(rng.choice(n, 4, replace=False))) for _ in range(S + 400)}))[:S]
Kb = vertex_B()
q1 = sum(alt_s(-Kb[a].conj(), Kb[a], quads) for a in range(10)).real
q2 = sum(2 * alt_s(Kb[a], Kb[a], quads).real for a in range(10))
for R, nm, anti in ((O1, "T1", True), (OU, "U", False)):
    Kt = [R.T @ Kk @ R for Kk in Kb]
    if anti: Kt = [Kk.conj() for Kk in Kt]
    q1t = sum(alt_s(-Kt[a].conj(), Kt[a], quads) for a in range(10)).real
    q2t = sum(2 * alt_s(Kt[a], Kt[a], quads).real for a in range(10))
    P(f"Q invariant under {nm}: {np.allclose(q1t, q1) and np.allclose(q2t, q2)}")

cols = {}; kinds = []
for nm, ms in famo.items():
    cols[nm] = sum(alt_s(a, a, quads) for a in ms)
doubled = sorted({nm[:-2] for nm in famo if nm.startswith("dens") and (":1:" in nm or ":28:" in nm)})
for d in doubled:
    cols[d + ":sc"] = sum(alt_s(a, b, quads) for a, b in zip(famo[d + ":s"], famo[d + ":c"]))
singles = [nm for nm in famo if not any(nm.startswith(d + ":") for d in doubled)]
Mall = np.array([cols[k] for k in cols]).T * (-0.25)
for nm_, qq in (("q1", q1), ("q2", q2)):
    g, *_ = np.linalg.lstsq(Mall, qq, rcond=None)
    P(f"unconstrained fit of {nm_}: relative residual {np.linalg.norm(Mall @ g - qq) / np.linalg.norm(qq):.2e}")
P(f"rank of channel 4-forms on sample: {np.linalg.matrix_rank(Mall, tol=1e-9)}")

def parity(nm):
    pr = info[nm][1]; assert ("even" in pr) != ("odd" in pr)
    return "even" if "even" in pr else "odd"
def solve(l1, l2, verbose=False):
    c = l1 * q1 + l2 * q2
    gs = {nm: cp.Variable() for nm in singles}
    Gd = {d: cp.Variable((2, 2), symmetric=True) for d in doubled}
    cons = []
    expr = 0
    for nm in singles:
        cons.append(gs[nm] <= 0 if parity(nm) == "even" else gs[nm] >= 0)
        expr = expr + gs[nm] * cols[nm]
    for d in doubled:
        assert parity(d + ":s") == parity(d + ":c")
        cons.append(Gd[d] << 0 if parity(d + ":s") == "even" else Gd[d] >> 0)
        expr = expr + Gd[d][0, 0] * cols[d + ":s"] + Gd[d][1, 1] * cols[d + ":c"] + 2 * Gd[d][0, 1] * cols[d + ":sc"]
    res = -0.25 * expr - c
    prob = cp.Problem(cp.Minimize(cp.norm1(res)), cons)
    prob.solve(solver="CLARABEL")
    val = prob.value / np.abs(c).sum()
    sol = {nm: float(gs[nm].value) for nm in singles}; sol.update({d: np.array(Gd[d].value) for d in doubled})
    return val, sol, prob.status

P("\nangle  lam1   lam2   min L1 residual/|q|_1 (Kramers class with U(1)_c)   status")
rows = []
for th in np.arange(0, 360, 10.0):
    l1, l2 = np.cos(np.radians(th)), np.sin(np.radians(th))
    val, sol, st = solve(l1, l2)
    rows.append((th, val, sol))
    P(f" {th:5.0f} {l1:+.3f} {l2:+.3f}   {val:.3e}   {st}" + ("   FEASIBLE" if val < 1e-7 else ""))
feas = [r for r in rows if r[1] < 1e-7]
P(f"feasible angles: {[r[0] for r in feas]}")
for th, val, sol in feas[:3]:
    P(f"  decomposition at {th:.0f} deg (nonzero coefficients):")
    for k, v in sol.items():
        vv = np.atleast_1d(v)
        if np.abs(vv).max() > 1e-6: P(f"     {k:26s} {np.round(v, 5).tolist()}  ({parity(k if k in info else k + ':s')})")
P(f"total {time.time() - t0:.0f}s, peak RSS {mem():.0f} MB")
