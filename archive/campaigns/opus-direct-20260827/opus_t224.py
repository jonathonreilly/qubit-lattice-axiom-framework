"""
T224 - JOINING R141 AND R133: does the fourth LATTICE direction force the
fourth CLIFFORD direction?

R141: the framework's own rule is relativistic on Z^4 and not on Z^3.
R133: chirality forces the site algebra M2(C) -> M4(C), uniquely and minimally.
R123 asserts these "arrive together" -- an argument, never a derivation.

The chain under test:
   a covariant Dirac operator on Z^d is  D = sum_mu Gamma_mu grad_mu,
   with the Gamma_mu transforming as a d-VECTOR under the hypercubic rotation
   group and mutually anticommuting (so that D^2 = -grad^2).
   T208: M_n(C) admits d mutually anticommuting elements iff 2^floor(d/2) | n.
   d = 3 -> n = 2 (the Paulis)          <- what the Qubit axiom names
   d = 4 -> n = 4                       <- forced the moment the lattice is Z^4

If that holds then Z^4 FORCES M4(C), and gamma5 comes free because M4(C)
carries five anticommuting elements, not four.
"""
import numpy as np, itertools

def hyperoct(d):
    """proper (det=+1) signed permutation matrices in d dimensions"""
    out = []
    for perm in itertools.permutations(range(d)):
        for sg in itertools.product([1,-1], repeat=d):
            R = np.zeros((d,d))
            for i,p in enumerate(perm): R[i,p] = sg[i]
            if abs(np.linalg.det(R)-1) < 1e-12: out.append(R)
    return out

G3, G4 = hyperoct(3), hyperoct(4)
print(f"proper hypercubic rotations: d=3 -> {len(G3)} (expect 24), "
      f"d=4 -> {len(G4)} (expect 192)")

I2 = np.eye(2, dtype=complex)
SX = np.array([[0,1],[1,0]],dtype=complex)
SY = np.array([[0,-1j],[1j,0]],dtype=complex)
SZ = np.array([[1,0],[0,-1]],dtype=complex)
kron = lambda *a: (lambda o: o)(np.array([[1.+0j]])) if not a else \
       (a[0] if len(a)==1 else np.kron(a[0], kron(*a[1:])))

GAM3 = [SX, SY, SZ]                                    # M2(C): 3 anticommuting
GAM4 = [kron(SX,I2), kron(SY,I2), kron(SZ,SX), kron(SZ,SY)]   # M4(C): 4

def check_clifford(G, tag):
    n = G[0].shape[0]; worst = 0.0
    for a in range(len(G)):
        worst = max(worst, np.max(np.abs(G[a]@G[a] - np.eye(n))))
        for b in range(a+1, len(G)):
            worst = max(worst, np.max(np.abs(G[a]@G[b] + G[b]@G[a])))
    print(f"  {tag}: {len(G)} generators in M{n}(C), Clifford relations to {worst:.1e}")
check_clifford(GAM3, "d=3")
check_clifford(GAM4, "d=4")

def spin_rep(Rs, GAM, tag):
    """for each rotation R find U with U Gamma_mu U^-1 = sum_nu R_{nu mu} Gamma_nu."""
    n = GAM[0].shape[0]; d = len(GAM)
    worst_res = 0.0; worst_dim = 0; ok = True
    for R in Rs:
        rows = []
        for mu in range(d):
            tgt = sum(R[nu, mu]*GAM[nu] for nu in range(d))
            # U Gamma_mu - tgt U = 0   ->   (Gamma_mu^T (x) I - I (x) tgt) vec(U)
            rows.append(np.kron(np.eye(n), GAM[mu].T) - np.kron(tgt, np.eye(n)))
        A = np.vstack(rows)
        U_, sv, Vt = np.linalg.svd(A, full_matrices=False)
        tol = max(A.shape)*np.finfo(float).eps*sv.max()
        k = int(np.sum(sv <= tol))
        if k < 1: ok = False; break
        worst_dim = max(worst_dim, k)
        U = Vt[len(Vt)-k].conj().reshape(n, n)
        for mu in range(d):
            tgt = sum(R[nu, mu]*GAM[nu] for nu in range(d))
            worst_res = max(worst_res, np.max(np.abs(U@GAM[mu] - tgt@U)))
    print(f"  {tag}: spin rep exists for all {len(Rs)} rotations: {ok};  "
          f"max residual {worst_res:.1e};  nullspace dim {worst_dim} (U unique up to phase)")
    return ok

print("\n=== do the gammas transform as a vector under the hypercubic group? ===")
spin_rep(G3, GAM3, "Z^3 with M2(C), 3 gammas")
spin_rep(G4, GAM4, "Z^4 with M4(C), 4 gammas")

print("\n=== can M2(C) carry FOUR anticommuting elements (i.e. serve Z^4)? ===")
print("  T208 bound: M_n(C) admits d mutually anticommuting elements iff")
print("  2^floor(d/2) divides n.   d=4 -> 4 | n -> n >= 4.")
from scipy.optimize import minimize
rng = np.random.default_rng(0)
for n in (2, 3, 4):
    best = np.inf
    for _ in range(40):
        x0 = rng.normal(size=2*4*n*n)
        def f(x):
            M = (x[:4*n*n] + 1j*x[4*n*n:]).reshape(4, n, n)
            r = 0.0
            for a in range(4):
                r += np.sum(np.abs(M[a]@M[a] - np.eye(n))**2)
                for b in range(a+1, 4):
                    r += np.sum(np.abs(M[a]@M[b] + M[b]@M[a])**2)
            return r
        best = min(best, minimize(f, x0, method="L-BFGS-B",
                                  options={"maxiter":3000}).fun)
    print(f"    M{n}(C): best residual over 30 restarts = {best:.3e}  "
          f"{'-> SERVES Z^4' if best < 1e-6 else '-> cannot serve Z^4'}")

print("\n=== and chirality comes free at n=4 ===")
g5 = GAM4[0]@GAM4[1]@GAM4[2]@GAM4[3]
anti = max(np.max(np.abs(g5@g - g@g5*-1)) for g in GAM4)
A = np.vstack([np.kron(np.eye(4), g.T) + np.kron(g, np.eye(4)) for g in GAM4])
U_, sv, Vt = np.linalg.svd(A, full_matrices=False)
tol = max(A.shape)*np.finfo(float).eps*sv.max()
print(f"  gamma5 = G1G2G3G4 anticommutes with every gamma: {anti:.1e}")
print(f"  dim of the chirality space {{X : {{X,G}}=0}} = "
      f"{int(np.sum(sv <= tol))}  (1 => gamma5 unique up to scale)")
