"""Family construction for the Kramers-class pair {T2 = Theta_1, T1 = (1 x i Gamma^9) T2} (no cvxpy here)."""
import numpy as np, itertools, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from common import *
def P(*a): print(*a); sys.stdout.flush()
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
_worst = 0.0
_names = list(famo)
for _i, _a in enumerate(_names):
    _A = np.array([m.ravel() for m in famo[_a]])
    for _b in _names[_i:]:
        _B = np.array([m.ravel() for m in famo[_b]])
        _Gm = _A @ _B.T
        if _a == _b: _Gm = _Gm - np.eye(len(_A))
        _worst = max(_worst, np.abs(_Gm).max())
P(f"orthonormal across families: max |Gram - 1| = {_worst:.1e}")
del _A, _B, _Gm


def parity(nm):
    pr = info[nm if nm in info else nm + ":s"][1]; assert ("even" in pr) != ("odd" in pr)
    return "even" if "even" in pr else "odd"
doubled = sorted({nm[:-2] for nm in famo if nm.startswith("dens") and (":1:" in nm or ":28:" in nm)})
singles = [nm for nm in famo if not any(nm.startswith(d + ":") for d in doubled)]
def channels(sol):
    """(coefficient, a-matrix) list from an SDP solution dict; blocks diagonalised."""
    out = []
    for nm in singles:
        for a in famo[nm]: out.append((sol[nm], a))
    for d in doubled:
        mu, V = np.linalg.eigh(sol[d])
        for i in range(2):
            for a_s, a_c in zip(famo[d + ":s"], famo[d + ":c"]):
                out.append((mu[i], V[0, i] * a_s + V[1, i] * a_c))
    return out
