#!/usr/bin/env python3
"""B18 check 1: which translation-covariant (anti)unitaries T intertwine the diagonal shift S,
T S T^-1 = w S^{+-1}, for ANY momentum map k -> M k + theta (M in GL(3,Z), theta real), any
continuous V(k), and any constant phase w.  Exhaustive finite enumeration after the exact reduction:
  (i)  V(k) S(k) = w S(Mk+theta) V(k) entrywise forces V_ac = 0 unless f_c = M^T f_a (two distinct
       exponentials vanish only on hyperplanes), so V is monomial and M^T permutes the 12 face diagonals;
  (ii) such M form a group of order 48 (= O_h) [enumerated below over GL(3,Z)];
  (iii) the scalar condition w = sigma_c sigma_{pi c} e^{-i theta.f_{pi c}} for all c forces theta in (pi/2)Z^3;
  (iv) antiunitary and E -> -E versions reduce to M -> -M because S(-k)^* = S(k) and S(k)^-1 = S(-k).
Then: list the momentum images of k* under the allowed maps."""
import time
from chk_model import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

# S(k) structure, read from the Bloch blocks
fvec = {}; sig = {}
for sh, M in blS.items():
    nz = np.argwhere(np.abs(M) > 1e-12)
    assert len(nz) == 1 and nz[0][0] == nz[0][1]
    c = int(nz[0][0]); fvec[c] = np.array(sh); sig[c] = float(M[c, c].real)
check("S(k) = diag(sigma_c e^{i k.f_c}), f_c = the corner's own face diagonal, 12 distinct, sigma = +-1",
      len(fvec) == 12 and all(tuple(fvec[CI[c]]) == FACE[c] for c in CORN) and set(sig.values()) <= {1.0, -1.0})
F12 = [fvec[c] for c in range(12)]; Fset = {tuple(f) for f in F12}

# (ii) all M^T in GL(3,Z) permuting the 12 face diagonals: determined by images of three basis face diagonals
B3 = np.array([[1, 1, 0], [1, -1, 0], [1, 0, 1]]).T   # columns
grp = []
for imgs in itertools.product(F12, repeat=3):
    A = np.array(imgs).T @ np.linalg.inv(B3)          # A B3 = imgs
    if not np.allclose(A, np.round(A)): continue
    A = np.round(A).astype(int)
    if abs(round(np.linalg.det(A))) != 1: continue
    if {tuple(A @ f) for f in F12} == Fset: grp.append(A)
uniq = {tuple(A.ravel()) for A in grp}
signed_perm = all(sorted(np.abs(np.array(a).reshape(3, 3)).sum(0)) == [1, 1, 1] and sorted(np.abs(np.array(a).reshape(3, 3)).sum(1)) == [1, 1, 1] for a in uniq)
check("(ii) the M in GL(3,Z) with M^T permuting the 12 face diagonals are exactly the 48 signed permutations (O_h)",
      len(uniq) == 48 and signed_perm, f"{len(uniq)} matrices")
OH = [np.array(a).reshape(3, 3) for a in sorted(uniq)]

# (iii) enumerate M in O_h, theta in (pi/2) Z^3 (64), test constancy of w over c
def perm_of(M):   # a = pi(c) with M^T f_a = f_c
    out = {}
    for c in range(12):
        a = [a for a in range(12) if tuple(M.T @ F12[a]) == tuple(F12[c])]; assert len(a) == 1; out[c] = a[0]
    return out
allowed = []
for M in OH:
    pi_ = perm_of(M)
    for th in itertools.product(range(4), repeat=3):
        theta = np.array(th) * np.pi / 2
        ws = [sig[c] * sig[pi_[c]] * np.exp(-1j * theta @ F12[pi_[c]]) for c in range(12)]
        if np.allclose(ws, ws[0]): allowed.append((M, theta, ws[0], pi_))
print(f"allowed (M, theta) pairs: {len(allowed)}")
# also confirm theta outside (pi/2)Z^3 never works (random thetas)
rng = np.random.default_rng(3); badrand = 0
for M in OH:
    pi_ = perm_of(M)
    for _ in range(20):
        theta = rng.uniform(0, 2 * np.pi, 3)
        ws = [sig[c] * sig[pi_[c]] * np.exp(-1j * theta @ F12[pi_[c]]) for c in range(12)]
        badrand += np.allclose(ws, ws[0], atol=1e-6)
# numerical cross-check of every allowed pair with an explicit monomial V, and of a sample of forbidden ones via null spaces
def Vmat(pi_):
    V = np.zeros((12, 12), complex)
    for c, a in pi_.items(): V[a, c] = 1.0
    return V
ks = rng.uniform(-np.pi, np.pi, (4, 3))
ok_expl = all(np.allclose(Vmat(p) @ SKc(k), w * SKc(M @ k + th) @ Vmat(p)) for M, th, w, p in allowed for k in ks)
def null_dim(M, th, w):
    I = np.eye(12); A = np.vstack([np.kron(SKc(k).T, I) - w * np.kron(I, SKc(M @ k + th)) for k in ks])
    _, s, Vh = np.linalg.svd(A); s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))])
    nb = [v.conj().reshape(12, 12, order='F') for v in Vh[s < 1e-9]]
    if not nb: return 0.0
    X = sum((rng.normal() + 1j * rng.normal()) * b for b in nb)
    return np.linalg.svd(X, compute_uv=False).min()   # smallest singular value of a generic intertwiner
forb = []
for M in OH[::5]:
    pi_ = perm_of(M)
    for th in [np.array(t) * np.pi / 2 for t in itertools.product(range(4), repeat=3)][::7]:
        if any(np.array_equal(M, a[0]) and np.allclose(th, a[1]) for a in allowed): continue
        cands = {np.round(sig[c] * sig[pi_[c]] * np.exp(-1j * th @ F12[pi_[c]]), 9) for c in range(12)}
        forb.append(max(null_dim(M, th, w) for w in cands))
print('debug: badrand', badrand, 'ok_expl', ok_expl, 'max generic sigma_min over forbidden sample', max(forb))
# which allowed maps are realised by PSG rotations? rotation lifts act as k -> R k + pi s_R
KS = [np.array(t) * 2 * np.pi / L for t in TV]; BK = [Bloch(k) for k in KS]
def kid(k): return [i for i, q in enumerate(KS) if np.allclose(np.exp(1j * (q - k)), 1)][0]
def mom_shift(Mop, R):
    i = kid(np.array([0.5, 0.0, 0.0]) * 2 * np.pi / L * 0 + KS[1]); outs = set()
    for i in range(0, 64, 9):
        w = [np.linalg.norm(BK[j].conj().T @ Mop @ BK[i]) for j in range(64)]; j = int(np.argmax(w))
        outs.add(tuple(np.rint((KS[j] - R @ KS[i]) / np.pi).astype(int) % 2))
    assert len(outs) == 1; return np.array(outs.pop())
sR = [mom_shift(Rm[r], ROTS[r]) for r in range(24)]
# inversion lift: does it commute with S?
inv_comm = [np.allclose(conj(Sr, P, s_), Sr) or np.allclose(conj(Sr, P, s_), Sr.T) for P, s_ in invs]
Sk_inv = [np.allclose(conj(Sr, P, s_), Sr) for P, s_ in invs]
def is_allowed(M, th):
    return any(np.array_equal(M, a[0]) and np.allclose(np.exp(1j * (th - a[1])), 1) for a in allowed)
rot_in = all(is_allowed(ROTS[r], np.pi * sR[r]) for r in range(24))
# images of k* and classification
def cls(k):
    k = wrap(k)
    if np.allclose(np.exp(1j * (k - kst)), 1): return "k*"
    if np.allclose(np.exp(1j * (k + kst)), 1): return "-k*"
    for i in range(3):
        if np.allclose(np.exp(1j * (k - kst - np.pi * np.eye(3)[i])), 1): return f"k*+pi e{i}"
        if np.allclose(np.exp(1j * (k + kst - np.pi * np.eye(3)[i])), 1): return f"-k*+pi e{i}"
    return "other"
imgs = {}
for M, th, w, p in allowed: imgs.setdefault(cls(M @ kst + th), []).append((int(round(np.linalg.det(M))), np.round(th / np.pi, 2)))
print({k: len(v) for k, v in imgs.items()})
proper_shifts = {}
for M, th, w, p in allowed:
    if round(np.linalg.det(M)) == 1: proper_shifts.setdefault(tuple(M.ravel()), []).append(tuple(np.round(th / np.pi * 2).astype(int) % 4))
print("theta (units pi/2) allowed per proper M: counts", sorted({len(v) for v in proper_shifts.values()}))
print("example: M = I allowed theta (pi/2 units):", proper_shifts[tuple(np.eye(3, dtype=int).ravel())])
check("(iii) allowed (M, theta): theta must lie in (pi/2)Z^3 (random theta never works); every allowed pair is realised by an explicit "
      "monomial V; sampled forbidden pairs have no invertible intertwiner at any candidate w (null spaces may be nonzero but singular)",
      badrand == 0 and ok_expl and max(forb) < 1e-9, f"{len(allowed)} allowed of {48*64}; {len(forb)} forbidden sampled")
check("the 24 gauge-dressed rotations (k -> R k + pi s_R) are among the allowed maps (S is PSG-symmetric)", rot_in)
check("NO allowed (anti)unitary momentum map sends k* to a doubler momentum +-k*+pi e_i (images are only k*, -k*)",
      set(imgs) <= {"k*", "-k*"}, f"image classes {sorted(imgs)}")
print("for M = I: thetas", proper_shifts[tuple(np.eye(3, dtype=int).ravel())], "(units of pi/2)")
print("inversion lifts commute with S:", sum(Sk_inv), "of 24")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
