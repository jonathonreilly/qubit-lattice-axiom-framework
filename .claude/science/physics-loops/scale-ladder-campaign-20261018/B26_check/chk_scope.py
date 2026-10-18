"""(f) scoping probes: phases in the A0-dual palette map; on-site algebra commutativity; an even-A length-5 word whose
reduction leaves the screened token set {S^+-1, S^+-2, R_L, Rt, o}; monomial (non-unit) generalisation of the theorem."""
import sys, itertools; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from mymodel import *
P = F = 0
def check(n, ok, d=""):
    global P, F; P += bool(ok); F += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}  {d}", flush=True)
A0i = A0m.conj().T; rng = np.random.default_rng(3)
zs = set()
for n, B in PC.items():
    M = A0m @ B @ A0i
    for n2, B2 in PC.items():
        z = np.vdot(B2.ravel(), M.ravel()) / 12
        if abs(abs(z) - 1) < 1e-10 and np.allclose(M, z * B2): zs.add(complex(np.round(z, 6))); break
check("A0 (PC element) A0^-1 = z * (PC element) with z ranging over all four of {1, i, -1, -i} (so 'even-A word = +- old word' needs 'z in {+-1, +-i}' when fills are normalised PC letters)",
      len(zs) == 4, str(sorted(zs, key=lambda c: np.angle(c))))
# (first run expected commutativity -- wrong expectation, kept in chk_scope_firstrun.log). Structure: centre dimension.
basis = np.array([B.ravel() for B in ONB]).T
cen = []
for c in itertools.product(*[[0]] * 0): pass
M = np.vstack([np.kron(np.eye(12), B.T) - np.kron(B, np.eye(12)) for B in ONB])   # vec(X B - B X) row-major
Mc = M @ basis; zdim = basis.shape[1] - np.linalg.matrix_rank(Mc, tol=1e-9)
comm = all(np.allclose(A @ B, B @ A) for A in ONB for B in ONB)
check("symmetric on-site algebra: dim 6, NOT commutative, centre dim 3 (= M1 + M1 + M2(C): D+ and D- are the two multiplicity-1 blocks; an 8-dim multiplicity-2 block carries the noncommutativity)",
      len(ONB) == 6 and not comm and zdim == 3, f"centre dim {zdim}")
okHL = np.allclose(HON0 @ LAM, LAM @ HON0)
print(f"   H_on and Lambda commute: {okHL}  (if False, H*L and L*H fills differ; the PHL palette lists only the H*L order)")
# even-A word of letter length 5: A_2 . S . o1 . A_0 . o2  ->  - S^-3 o1~ o2   (S^-3 is not a screened token)
o1, o2 = PC['L130'], PC['H21']; ok = True
for k in rng.uniform(-np.pi, np.pi, (5, 3)):
    lhs = A0m @ Sk(k, 2) @ Sk(k, 1) @ o1 @ A0m @ o2
    rhs = -Sk(k, -3) @ (A0m @ o1 @ A0i) @ o2
    ok &= np.allclose(lhs, rhs)
check("example: A_2 S o1 A_0 o2 = -S^-3 (A0 o1 A0^-1) o2 : a 5-letter even-A word reducing to an S^3-skeleton outside the screened token set", ok)
# also A_1 S^2 o A_1 o -> - S^-3 o~ S o  (n_eff = -2)
ok2 = True
for k in rng.uniform(-np.pi, np.pi, (5, 3)):
    lhs = A0m @ Sk(k, 1) @ Sk(k, 2) @ o1 @ A0m @ Sk(k, 1) @ o2
    rhs = -Sk(k, -3) @ (A0m @ o1 @ A0i) @ Sk(k, 1) @ o2
    ok2 &= np.allclose(lhs, rhs)
check("example: A_1 S^2 o1 A_1 o2 = -S^-3 o1~ S o2 (merged power |p| = 3 > 2)", ok2)
print(f"\nTOTAL: PASS={P} FAIL={F}")
