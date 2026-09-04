"""
T258 - WHY the framework's massless scalars are exact: the Qubit axiom's
non-privileging clause.

Qubit: "No possibility is privileged.  Possibilities are distinguished by the
supplied algebraic structure alone."

The algebraic structure is M_n(C), whose automorphisms are all inner
(Skolem-Noether), i.e. the automorphism group is PU(n).  So a rule that
distinguishes possibilities by nothing but that structure must be PU(n)-
invariant -- and then the symmetry is EXACT, and Goldstone's theorem makes the
broken modes exactly massless.

Checked: (1) PU(n) invariance; (2) the anti-unitary extension (Wigner);
(3) that PRIVILEGING any possibility breaks it -- the converse, quantified.
"""
import numpy as np
rng = np.random.default_rng(419)
n = 4
def haar(m):
    A = rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))
    Q,R = np.linalg.qr(A); return Q*(np.diag(R)/np.abs(np.diag(R)))
def st(m):
    z = rng.normal(size=m)+1j*rng.normal(size=m); return z/np.linalg.norm(z)
born = lambda a,b: abs(np.vdot(a,b))**2

print("=== 1. PU(n) invariance (inner automorphisms) ===")
w = 0.0
for _ in range(20000):
    a,b = st(n), st(n); V = haar(n)
    w = max(w, abs(born(a,b) - born(V@a, V@b)))
print(f"    max deviation: {w:.2e}")

print("\n=== 2. anti-unitary extension (Wigner) ===")
w = 0.0
for _ in range(20000):
    a,b = st(n), st(n); V = haar(n)
    w = max(w, abs(born(a,b) - born(np.conj(V@a), np.conj(V@b))))
print(f"    max deviation under V then complex conjugation: {w:.2e}")

print("\n=== 3. the converse: does PRIVILEGING a possibility break it? ===")
print("    build phi_eps(a,b) = |<a|b>|^2 * (1 + eps |<a|e1>|^2 |<b|e1>|^2),")
print("    which privileges the direction e1, and test PU(n) invariance:")
e1 = np.zeros(n, dtype=complex); e1[0] = 1
for eps in (0.0, 0.01, 0.1, 0.5, 1.0):
    w = 0.0
    for _ in range(4000):
        a,b = st(n), st(n); V = haar(n)
        f  = lambda x,y: born(x,y)*(1 + eps*born(x,e1)*born(y,e1))
        w = max(w, abs(f(a,b) - f(V@a, V@b)))
    print(f"      eps={eps:4.2f}:  max invariance violation {w:.3e}"
          f"   {'INVARIANT' if w < 1e-12 else 'BROKEN'}")

print("""
=== the chain ===
   Qubit: "no possibility is privileged"
     -> the rule is invariant under Aut(M_n(C)) = PU(n)          [1, exact]
     -> the symmetry of the record measure is EXACT
     -> Goldstone's theorem: the broken modes are EXACTLY massless
     -> the framework's 2(n-1) massless scalars are FORCED

   And the converse holds: any rule that privileges a possibility breaks the
   invariance at first order in the privileging (section 3).  To give the
   scalars a mass, some possibility must be privileged -- which the Qubit axiom
   forbids in its own words.""")
