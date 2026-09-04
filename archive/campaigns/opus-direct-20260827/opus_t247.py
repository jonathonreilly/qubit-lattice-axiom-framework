"""
T247 - which axiom clause makes the framework's gauge group ABELIAN?

R155: the framework has an exact local U(1), because the Qubit axiom makes
possibilities STATES (rays), so the phase is unphysical.  A ray is a RANK-1
projector.  The Record axiom is what fixes the rank:

   "When present, a record locks exactly ONE admissible local possibility."

If a record instead locked a k-dimensional SUBSPACE, the possibility would be a
rank-k projector P = sum_{i<=k} |psi_i><psi_i|, whose frame {psi_i} is defined
only up to U(k).  The Born-type overlap Tr(P P') depends only on the projectors,
so the frame rotation is a LOCAL redundancy of exactly U(k).

Tested: (1) Tr(P P') is invariant under independent per-site U(k);
        (2) the redundancy has dimension k^2 = dim U(k);
        (3) the edge weight stays affine in each argument, so R136's derivation
            of the rule's form still runs.
"""
import numpy as np
rng = np.random.default_rng(191)

def frame(n, k):
    A = rng.normal(size=(n,k)) + 1j*rng.normal(size=(n,k))
    Q, _ = np.linalg.qr(A)
    return Q                      # n x k, orthonormal columns

def proj(Q):
    return Q @ Q.conj().T

def haar(k):
    A = rng.normal(size=(k,k)) + 1j*rng.normal(size=(k,k))
    Q, R = np.linalg.qr(A)
    return Q * (np.diag(R)/np.abs(np.diag(R)))

n = 6
print("=== 1. is the Born-type overlap Tr(P P') invariant under LOCAL U(k)? ===")
print("    (independent frame rotation at each of the two sites)")
for k in (1, 2, 3):
    worst = 0.0
    for _ in range(2000):
        Q1, Q2 = frame(n,k), frame(n,k)
        a = np.trace(proj(Q1) @ proj(Q2)).real
        b = np.trace(proj(Q1 @ haar(k)) @ proj(Q2 @ haar(k))).real
        worst = max(worst, abs(a-b))
    print(f"    rank k={k}:  max |Tr(PP') - Tr(P'P')| under independent U({k}) "
          f"= {worst:.2e}")

print("\n=== 2. how big is the redundancy? ===")
print("    Stiefel V_k(C^n) real dim = 2nk - k^2 ; Grassmannian Gr(k,n) = 2k(n-k)")
for k in (1,2,3):
    st = 2*n*k - k*k; gr = 2*k*(n-k)
    print(f"    k={k}:  Stiefel {st:3d}  -  Grassmannian {gr:3d}  =  {st-gr:3d}"
          f"   = k^2 = dim U({k}) = {k*k}   {'OK' if st-gr == k*k else 'MISMATCH'}")

print("\n=== 3. is the edge weight still affine in each argument? ===")
print("    (R136's derivation of the rule's FORM needs this)")
for k in (1,2,3):
    worst = 0.0
    for _ in range(1000):
        P1, P2, P3 = proj(frame(n,k)), proj(frame(n,k)), proj(frame(n,k))
        s = rng.uniform(0,1)
        mix = s*P2 + (1-s)*P3
        lhs = np.trace(P1 @ mix).real
        rhs = s*np.trace(P1@P2).real + (1-s)*np.trace(P1@P3).real
        worst = max(worst, abs(lhs-rhs))
    print(f"    rank k={k}:  |Tr(P (s P2 + (1-s) P3)) - mixture| = {worst:.2e}")

print("""
=== what this says ===
  The framework's gauge group is  U(k),  where k is the RANK of the projector a
  record locks.  The Record axiom says a record locks "exactly ONE admissible
  local possibility" -- k = 1 -- and U(1) is abelian.

  >> The abelian-ness of the framework's gauge sector is not a property of the
     Qubit axiom or of M_n(C).  It is the Record axiom's word "one".

  A record locking a k-dimensional subspace would give a NON-ABELIAN U(k), with
  the same Born-type edge weight and the same R136 derivation of the rule's form.
""")
