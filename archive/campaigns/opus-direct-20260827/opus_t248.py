"""
T248 - at rank k, does the framework carry a genuine NON-ABELIAN lattice gauge
field?

R167: a record locking a k-dimensional subspace has a U(k) frame redundancy.
The natural link variable between neighbouring records is

        U_{xy} = Q_x^dag Q_y        (k x k),   Q = the n x k frame

Under an independent frame rotation Q_x -> Q_x V_x this should behave EXACTLY as
a lattice gauge field, U_{xy} -> V_x^dag U_{xy} V_y, making plaquette traces
gauge invariant and Wilson loops well defined.  Checked, along with whether the
Born-type edge weight is the link's norm -- the rank-k generalisation of R158.
"""
import numpy as np
rng = np.random.default_rng(211)

def frame(n,k):
    A = rng.normal(size=(n,k)) + 1j*rng.normal(size=(n,k))
    Q,_ = np.linalg.qr(A); return Q
def haar(k):
    A = rng.normal(size=(k,k)) + 1j*rng.normal(size=(k,k))
    Q,R = np.linalg.qr(A); return Q*(np.diag(R)/np.abs(np.diag(R)))
P = lambda Q: Q @ Q.conj().T
link = lambda Qa, Qb: Qa.conj().T @ Qb

n = 6
print("=== 1. does U_xy transform as a lattice gauge field? ===")
print("    require  U -> V_x^dag U V_y  under independent frame rotations")
for k in (1,2,3):
    w = 0.0
    for _ in range(2000):
        Qa, Qb = frame(n,k), frame(n,k); Va, Vb = haar(k), haar(k)
        lhs = link(Qa@Va, Qb@Vb)
        rhs = Va.conj().T @ link(Qa,Qb) @ Vb
        w = max(w, np.max(np.abs(lhs-rhs)))
    print(f"    k={k}:  max deviation {w:.2e}")

print("\n=== 2. is the plaquette trace gauge invariant? ===")
for k in (1,2,3):
    w = 0.0
    for _ in range(2000):
        Q = [frame(n,k) for _ in range(4)]
        V = [haar(k) for _ in range(4)]
        def plq(Qs):
            return np.trace(link(Qs[0],Qs[1]) @ link(Qs[1],Qs[2])
                            @ link(Qs[2],Qs[3]) @ link(Qs[3],Qs[0]))
        w = max(w, abs(plq(Q) - plq([Q[i]@V[i] for i in range(4)])))
    print(f"    k={k}:  max |tr(plaquette) change| {w:.2e}")

print("\n=== 3. is it actually NON-ABELIAN? ===")
print("    do the link variables commute?  (k=1 must; k>1 must not)")
for k in (1,2,3):
    w = 0.0
    for _ in range(2000):
        Qa,Qb,Qc = frame(n,k), frame(n,k), frame(n,k)
        A, B = link(Qa,Qb), link(Qb,Qc)
        w = max(w, np.max(np.abs(A@B - B@A)))
    print(f"    k={k}:  max |[U1,U2]| = {w:.3e}   "
          f"{'abelian' if w < 1e-12 else 'NON-ABELIAN'}")

print("\n=== 4. is the Born-type edge weight the link's norm? ===")
print("    R158 at rank 1 gave |<psi|psi'>|^2 ; predict Tr(P P') = tr(U^dag U)")
for k in (1,2,3):
    w = 0.0
    for _ in range(2000):
        Qa, Qb = frame(n,k), frame(n,k)
        U = link(Qa,Qb)
        w = max(w, abs(np.trace(P(Qa)@P(Qb)).real - np.trace(U.conj().T@U).real))
    print(f"    k={k}:  max |Tr(P P') - tr(U^dag U)| = {w:.2e}")

print("""
=== reading ===
  At rank k the framework carries a genuine NON-ABELIAN lattice gauge field:
  the link is U_xy = Q_x^dag Q_y, it transforms as V_x^dag U V_y, plaquette
  traces are gauge invariant, the links do not commute for k > 1, and the
  Born-type edge weight is exactly the link's Frobenius norm -- the rank-k
  generalisation of R158's minimal-coupling identity.
  The same heat-trace mechanism that induced Maxwell (R157) would then induce
  YANG-MILLS, since a2 carries tr(F^2) for a non-abelian connection just as it
  carries F^2 for an abelian one.""")
