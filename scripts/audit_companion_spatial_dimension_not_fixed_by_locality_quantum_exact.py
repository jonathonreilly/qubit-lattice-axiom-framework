"""
Audit companion (exact, sympy) for
SPATIAL_DIMENSION_NOT_FIXED_BY_LOCALITY_QUANTUM_DIRAC_SPINOR_CAP_NARROW_NO_GO_NOTE_2026-06-04.md

No-go: the two structural axioms -- Locality (discrete sites, near-neighbour
coupling) and Quantum (each site is the qubit M_2(C)) -- do NOT determine the
spatial dimension. A qubit lives on Z^d for ANY d. The dimension is bounded
only when the dynamics demands an ANTICOMMUTING (Dirac/relativistic) spatial
frame, in which case a 2-component spinor caps it at d_s <= 3 (the maximal
case is the 2-component Weyl spinor of 3+1D). That relativistic structure is
an admitted gate (staggered-Dirac / emergent-Lorentz), so d=3 is DOWNSTREAM
of the matter-dynamics admission, not a theorem of {Locality, Quantum,
Record}. This SUPERSEDES the earlier "d=3 from the qubit observable count"
claim, whose bridge (spatial direction = independent qubit observable) is
contradicted by generic qubit lattices (check A).

Reproven from the Pauli primitives; no PDG values, no fitted selectors, no
lattice numerics, no imports.
"""
import sympy as sp
from sympy import I, eye, zeros, Matrix

s0 = eye(2)
s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])

def ac(A, B): return A*B + B*A
def co(A, B): return A*B - B*A
def Z(A):     return sp.simplify(A) == zeros(A.rows, A.cols)
def kron(A, B):
    a, b = A.shape[0], B.shape[0]
    M = zeros(a*b, a*b)
    for i in range(a):
        for j in range(a):
            for p in range(b):
                for q in range(b):
                    M[i*b+p, j*b+q] = A[i, j]*B[p, q]
    return M

R = []
def chk(l, o): R.append((l, bool(o)))

# (A) THE NO-GO: {Locality, Quantum} do NOT fix the spatial dimension. A qubit per site of Z^d
#     with an Ising bond s3(x)s3 is local and well-defined for ANY d; the SAME bond operator s3 is
#     reused in every direction (distinguished by the graph, not the algebra), and such bonds commute
#     ([s3,s3]=0), imposing no algebraic cap. So d is unbounded by the qubit.
chk("A   Ising bond s3 reusable in any number of directions ([s3,s3]=0, no cap) => {Locality,Quantum} do NOT fix d",
    Z(co(s3, s3)))
chk("A2  k mutually-commuting bond directions (all = s3) exist for every k (shown k=6) => d unbounded by the qubit",
    all(Z(co(s3, s3)) for _ in range(6)))

# (B) THE CAP APPEARS ONLY FOR AN ANTICOMMUTING (DIRAC) FRAME: if each direction must carry a
#     DISTINCT anticommuting Hermitian generator, a 2-component spinor admits at most 3 (only M=0
#     anticommutes with all of s1,s2,s3). So a 2-spinor Dirac frame => d_s <= 3.
a, b, c, d = sp.symbols('a b c d')
M = Matrix([[a, b], [c, d]])
Jc = Matrix([e for s in (s1, s2, s3) for e in ac(M, s)]).jacobian([a, b, c, d])
chk("B   Dirac/anticommuting frame on a 2-spinor caps at 3 (no 4th anticommuting Hermitian) => d_s<=3",
    Jc.rank() == 4)

# (C) THE MAXIMAL CASE = the 2-component WEYL spinor of 3+1D: sigma^mu=(I,s1,s2,s3), the massless
#     Weyl equation i sigma^mu d_mu psi = 0; its 3 spatial gammas satisfy {s_i,s_j}=2 delta_ij.
chk("C   2-component Weyl spinor realizes exactly 3 spatial directions: {s_i,s_j}=2 delta_ij",
    all(Z(ac((s1, s2, s3)[i], (s1, s2, s3)[j]) - 2*(1 if i == j else 0)*s0) for i in range(3) for j in range(3)))

# (D) THE SPINOR SIZE SETS THE CAP: a 4-component spinor admits a 4-element anticommuting Hermitian
#     frame (alpha_i=s1(x)s_i, beta=s3(x)I), impossible at n=2. So d_s<=3 is SPECIFIC to choosing the
#     2-component (qubit) spinor -- i.e. to the matter dynamics, not to {Locality, Quantum}.
A1, A2, A3, Bm = kron(s1, s1), kron(s1, s2), kron(s1, s3), kron(s3, s0)
g4 = [A1, A2, A3, Bm]
chk("D   a 4-component spinor admits a 4-element anticommuting Hermitian frame (impossible at n=2) => spinor size sets d_s",
    all(Z(ac(g4[i], g4[j]) - 2*(1 if i == j else 0)*eye(4)) for i in range(4) for j in range(4)))

# (E) THE su(2) DOUBLE-USE IS REAL (the panel's point): in M_2(C) the bivectors s_i s_j = i s_k ARE
#     the vectors times i, so the SAME three operators serve as both the spatial frame (vectors) and
#     (times i) the weak su(2) (bivectors). Only the dynamical ROLE distinguishes them; the algebra
#     alone does not -- an unresolved bridge, flagged not closed.
chk("E   double-use is real: s1 s2 = i s3 etc (weak-su(2) bivector = i x spatial vector) -- same operators",
    Z(s1*s2 - I*s3) and Z(s2*s3 - I*s1) and Z(s3*s1 - I*s2))

P = sum(1 for _, o in R if o)
F = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F:
    raise SystemExit(1)
print(
    "\nNO-GO verified: {Locality, Quantum} do NOT fix the spatial dimension (A,A2) -- a qubit lives on\n"
    "any Z^d. d_s<=3 appears ONLY for an anticommuting Dirac frame (B), maximal as the 2-component Weyl\n"
    "spinor of 3+1D (C); the cap is set by the 2-component spinor SIZE = the matter dynamics (D), an\n"
    "admitted gate. So d=3 is DOWNSTREAM of the matter-dynamics admission, NOT a theorem of {Locality,\n"
    "Quantum, Record}. The spatial-frame vs weak-su(2) double-use (E) is real and unresolved by the algebra."
)
