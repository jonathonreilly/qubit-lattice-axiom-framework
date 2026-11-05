"""Test 3 (pre-set): does the one-cell many-body tick preserve the [[8,3,3]] code space?
PASS iff min over (site labelling x uniform frame) of ||(1-P) G V|| < 1e-10, for the fermionic
second quantisation G of the K = 0 cell block of CL-1 (eps .3, 1.1) or FREEZE, under Jordan-Wigner.
Controls: identity tick (must pass), Haar-random number-conserving cell unitary (baseline)."""
import itertools as it, numpy as np, sys, os
src = open(__import__('pathlib').Path(__file__).with_name('asymmetry_misalignment_part_freeze_tick_rebuild_2026_10_26.py')).read()
ns = {}; exec(compile(src, 'freeze_build.py', 'exec'), ns)
U1, UF = ns['U1'], ns['UF']
n = 8; D = 1 << n
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]], complex); Z = np.diag([1., -1]).astype(complex); Yp = 1j * X @ Z
def kron(ops):
    M = np.array([[1]], complex)
    for o in ops: M = np.kron(M, o)
    return M
P1 = {'I': I2, 'X': X, 'Y': Yp, 'Z': Z}
GOT = "XXXXXXXX ZZZZZZZZ XIXIZYZY XIYZXIYZ XZIYIYXZ".split()
FR = {'id': {'X': 'X', 'Y': 'Y', 'Z': 'Z', 'I': 'I'}, 'XYZ': {'X': 'Y', 'Y': 'Z', 'Z': 'X', 'I': 'I'}, 'ZYX': {'X': 'Z', 'Z': 'Y', 'Y': 'X', 'I': 'I'},
      'H': {'X': 'Z', 'Z': 'X', 'Y': 'Y', 'I': 'I'}, 'S': {'X': 'Y', 'Y': 'X', 'Z': 'Z', 'I': 'I'}, 'HSH': {'X': 'X', 'Y': 'Z', 'Z': 'Y', 'I': 'I'}}
def codeV(frame):
    P = np.eye(D, dtype=complex)
    for g in GOT: P = P @ (np.eye(D) + kron([P1[FR[frame][c]] for c in g])) / 2
    w, v = np.linalg.eigh((P + P.conj().T) / 2); V = v[:, w > .5]
    assert V.shape[1] == 8; return V
# JW annihilators
a = np.array([[0, 1], [0, 0]], complex)
c = [kron([Z] * j + [a] + [I2] * (n - j - 1)) for j in range(n)]
def second_quant(u):
    w, v = np.linalg.eig(u); h = v @ np.diag(np.log(w)) @ np.linalg.inv(v)   # u = exp(h), h anti-Hermitian
    H = sum(h[i, j] * c[i].conj().T @ c[j] for i in range(n) for j in range(n))
    wH, vH = np.linalg.eig(H); G = vH @ np.diag(np.exp(wH)) @ np.linalg.inv(vH)
    # check covariance G c_j^+ G^+ = sum_i u_ij c_i^+
    err = max(np.linalg.norm(G @ c[j].conj().T @ G.conj().T - sum(u[i, j] * c[i].conj().T for i in range(n))) for j in range(n))
    return G, err
idx = np.arange(D); bits = (idx[:, None] >> (n - 1 - np.arange(n))) & 1     # qubit 0 = most significant (kron order)
perms = list(it.permutations(range(n)))
def perm_rows(p):   # basis index map for relabelling qubit j -> p[j]
    nb = np.zeros_like(bits); nb[:, list(p)] = bits
    return (nb * (1 << (n - 1 - np.arange(n)))).sum(1)
PR = [perm_rows(p) for p in perms]
Vs = {f: codeV(f) for f in FR}
RINV = np.array([np.argsort(r) for r in PR])      # Vp = V[RINV[i]] is the code basis under labelling i
def best_leak(G, chunk=4032):
    """min over labellings x frames of ||(1 - Vp Vp^+) G Vp||_2. With G unitary and Vp orthonormal,
    ||(1 - P) G Vp||_2^2 = 1 - sigma_min(Vp^+ G Vp)^2, used to rank all labellings in batches; the minimiser's
    leak is then recomputed directly (the closed form loses precision near 0)."""
    best = (9, None, None); G64 = G.astype(np.complex64)
    for f, V in Vs.items():
        V64 = V.astype(np.complex64)
        for i0 in range(0, len(perms), chunk):
            Vp = V64[RINV[i0:i0 + chunk]]                     # (B, 256, 8), complex64 for ranking only
            B = Vp.shape[0]
            Y = (G64 @ Vp.transpose(1, 0, 2).reshape(D, B * 8)).reshape(D, B, 8).transpose(1, 0, 2)
            M = np.einsum('bik,bil->bkl', Vp.conj(), Y)
            smin = np.linalg.svd(M, compute_uv=False)[:, -1]
            L = np.sqrt(np.clip(1 - smin ** 2, 0, None)); j = int(np.argmin(L))
            if L[j] < best[0]: best = (float(L[j]), (perms[i0 + j], f), V[RINV[i0 + j]])
    Vb = best[2]; W = G @ Vb
    return float(np.linalg.norm(W - Vb @ (Vb.conj().T @ W), 2)), best[1]
rng = np.random.default_rng(7)
q, _ = np.linalg.qr(rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)))
Re = ns['Re']; from numpy.linalg import eigh
def ex(Hm, t): w, v = eigh(Hm); return v @ np.diag(np.exp(-1j*t*w)) @ v.conj().T
kg = np.array([0.37, -1.21, 0.83])
print('||U1(0) - 1|| =', np.linalg.norm(U1(np.zeros(3), .3) - np.eye(8)))
cases = {'identity (control)': np.eye(8, dtype=complex), 'CL-1 eps .3 K=0': U1(np.zeros(3), .3),
         'FREEZE K=0': UF(np.zeros(3)), 'CL-1 intra-cell exp(-i .3 Re)': ex(Re, .3), 'CL-1 intra-cell exp(-i 1.1 Re)': ex(Re, 1.1),
         'CL-1 eps .3 generic K': U1(kg, .3), 'FREEZE generic K': UF(kg), 'random number-conserving (baseline)': q}
res = {}
for name, u in cases.items():
    G, err = second_quant(u); L, arg = best_leak(G); res[name] = L
    print(f"{name:38s} unitarity {np.linalg.norm(u.conj().T@u-np.eye(8)):.1e} covariance {err:.1e}  min leak {L:.3e} at {arg}", flush=True)
ok = res['identity (control)'] < 1e-10
print("controls OK" if ok else "CONTROL FAIL")
for k in [k for k in cases if 'control' not in k and 'baseline' not in k]:
    print(("PASS" if res[k] < 1e-10 else "FAIL"), k, f"{res[k]:.3e}")
