"""HIER-3 R3 (candidate C4, COL-1 class-M cells): how weak a colour coupling can a
truncated link register represent? Plaquette ceilings for Kogut-Susskind truncations
of L^2(SU(3)) on each link. Own code."""
import math, itertools
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")

rng = np.random.default_rng(20261018)
# ---------------- (i) Haar Monte Carlo checks ----------------
def haar_su3(n):
    z = (rng.standard_normal((n, 3, 3)) + 1j * rng.standard_normal((n, 3, 3))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diagonal(r, axis1=1, axis2=2)
    q = q * (d / np.abs(d))[:, None, :]
    det = np.linalg.det(q)
    return q / (det ** (1.0 / 3))[:, None, None]

N = 200000
U = haar_su3(N)
tr = np.trace(U, axis1=1, axis2=2)
def mc(name, samples, exact):
    m = samples.mean(); s = samples.std() / math.sqrt(len(samples))
    ok = abs(m - exact) < 4 * s + 1e-12
    check(f"Haar {name}", ok, f"MC {m.real:+.4f}{m.imag:+.4f}i +- {s:.4f}, exact {exact}")
mc("int |TrU|^2 = 1", np.abs(tr) ** 2, 1.0)
mc("int (TrU)^2 = 0", tr ** 2, 0.0)
mc("int (TrU)^3 = 1", tr ** 3, 1.0)
mc("int |TrU|^2 TrU = 0", np.abs(tr) ** 2 * tr, 0.0)
mc("int U11 U22 U33 = 1/6 (eps.eps/6)", U[:, 0, 0] * U[:, 1, 1] * U[:, 2, 2], 1 / 6)
mc("int |U12|^2 = 1/3", np.abs(U[:, 0, 1]) ** 2, 1 / 3)

eps = np.zeros((3, 3, 3))
for (i, j, k), s in {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}.items():
    eps[i, j, k] = s

# ---------------- (ii) compressed four-link plaquette ----------------
def link_ops(trunc):
    """Compressed multiplication operators A[a][b] = P U_ab P on the truncated link space.
    T10: {0, e_ij}; T19: {0, e_ij, f_ij}; e = sqrt3 U_ij, f = sqrt3 conj(U_ij)."""
    dim = 10 if trunc == "T10" else 19
    E = lambda i, j: 1 + 3 * i + j
    F = lambda i, j: 10 + 3 * i + j
    A = {}
    for a in range(3):
        for b in range(3):
            M = sp.lil_matrix((dim, dim))
            M[E(a, b), 0] = 1 / math.sqrt(3)                  # 0 -> e_ab
            if trunc == "T19":
                M[0, F(a, b)] = 1 / math.sqrt(3)              # f_ab -> 0
                for i in range(3):
                    for k in range(3):
                        if eps[i, a, k] == 0: continue
                        for j in range(3):
                            for l in range(3):
                                if eps[j, b, l] == 0: continue
                                M[F(i, j), E(k, l)] += 0.5 * eps[i, a, k] * eps[j, b, l]  # e -> f
            A[(a, b)] = M.tocsr()
    return A, dim

# MC check of the e->f matrix element <f_ij|U_ab|e_kl> = 3 int U_ij U_ab U_kl = eps_iak eps_jbl / 2
val = 3 * np.mean(U[:, 0, 0] * U[:, 1, 1] * U[:, 2, 2])
check("Haar <f_11|U_22|e_33> = eps eps/2 = 1/2", abs(val - 0.5) < 4 * 3 * (np.abs(U[:, 0, 0] * U[:, 1, 1] * U[:, 2, 2]).std() / math.sqrt(N)),
      f"MC {val.real:.4f}")

def plaquette_ceiling(trunc):
    A, d = link_ops(trunc)
    O = None
    for a, b, c, dd in itertools.product(range(3), repeat=4):
        # Tr(U1 U2 U3^dag U4^dag) = sum U1_ab U2_bc conj(U3_dc) conj(U4_ad)
        term = sp.kron(sp.kron(A[(a, b)], A[(b, c)]), sp.kron(A[(dd, c)].conj().T, A[(a, dd)].conj().T), format='csr')
        O = term if O is None else O + term
    H = (O + O.conj().T) / 6.0        # Re Tr U_p / 3
    H = sp.csr_matrix(H)
    vals = eigsh(H, k=3, which='LA', return_eigenvectors=False, tol=1e-12)
    return max(vals), d ** 4, H.nnz

c10, dim10, nnz10 = plaquette_ceiling("T10")
check("T10 (COL-1 link {1,(3bar,3)}): max <Re Tr U_p>/3 = 1/18", abs(c10 - 1 / 18) < 1e-10,
      f"{c10:.12f} (dim {dim10}, nnz {nnz10})")
c19, dim19, nnz19 = plaquette_ceiling("T19")
print(f"T19 ({{1,(3bar,3),(3,3bar)}}): max <Re Tr U_p>/3 over ALL four-link states = {c19:.6f} (dim {dim19}, nnz {nnz19})")

# ---------------- (iii) isolated gauge-invariant plaquette ceiling c(n) ----------------
def dimpq(p, q): return (p + 1) * (q + 1) * (p + q + 2) // 2
def ceiling_c(reps):
    idx = {r: i for i, r in enumerate(reps)}
    M = np.zeros((len(reps), len(reps)))
    for (p, q), j in idx.items():
        outs = [(p + 1, q), (p - 1, q + 1), (p, q - 1)] + [(p, q + 1), (p + 1, q - 1), (p - 1, q)]
        for r in outs:
            if r[0] >= 0 and r[1] >= 0 and r in idx:
                M[idx[r], j] += 1.0 / 6
    w = np.linalg.eigvalsh((M + M.T) / 2)
    return w[-1]
c_1F = ceiling_c([(0, 0), (1, 0)])
c_1FFb = ceiling_c([(0, 0), (1, 0), (0, 1)])
check("isolated ceiling with {1,F} = 1/6", abs(c_1F - 1 / 6) < 1e-12, f"{c_1F:.6f}")
check("isolated ceiling with {1,F,Fbar} = 1/3", abs(c_1FFb - 1 / 3) < 1e-12, f"{c_1FFb:.6f}")
P_b6 = 0.5934
def P_weak(beta): return 1 - 2 / beta - 1.2208 / beta ** 2   # comparator (two-loop Wilson SU(3))
betas_window = {"W_v centre (Wilson bare)": 6 / 0.1643, "W_v strong edge": 6 / 0.1735, "W_v weak edge": 6 / 0.1560}
print("\n n   ceiling c(n)   1-c      states/link D(n)   qubits/link")
prev = 0; mono = True; table = []
for n in range(0, 41):
    reps = [(p, q) for p in range(n + 1) for q in range(n + 1 - p)]
    c = ceiling_c(reps)
    D = sum(dimpq(p, q) ** 2 for p, q in reps)
    mono &= (c >= prev - 1e-12); prev = c
    table.append((n, c, D))
    if n <= 12 or n % 5 == 0:
        print(f"{n:3d}   {c:.6f}   {1-c:.2e}   {D:14d}   {math.ceil(math.log2(D)):4d}")
check("c(n) non-decreasing in n", mono)
def nmin(target):
    for n, c, D in table:
        if c >= target: return n, D
    return None, None
for lab, tgt in [("Wilson beta=6 plaquette 0.5934", P_b6)] + \
        [(f"{k} beta={b:.1f}: P={P_weak(b):.4f}", P_weak(b)) for k, b in betas_window.items()]:
    n, D = nmin(tgt)
    print(f"  smallest n with ceiling >= {lab}: n = {n}, D = {D}, qubits/link >= "
          f"{math.ceil(math.log2(D)) if D else 'n/a'}")
# fit 1-c(n) ~ C/n^2 tail
ns = np.array([t[0] for t in table[10:]]); cs = np.array([t[1] for t in table[10:]])
C = np.median((1 - cs) * (ns + 3) ** 2)
print(f"  tail: 1 - c(n) ~ {C:.2f}/(n+3)^2 (median over n = 10..40)")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
