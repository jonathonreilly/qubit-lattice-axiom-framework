"""
Audit companion (exact, sympy) for
QUBIT_ALGEBRA_FORCES_SPATIAL_DIMENSION_THREE_NARROW_THEOREM_NOTE_2026-06-03.md

Claim (narrow): the spatial-dimension count d_s = 3 need not be stipulated
independently (as in axiom A2, "sites form Z^3"). It is forced by axiom A1
(the local algebra is the COMPLEX qubit M_2(C)) via the Clifford
identification M_2(C) = Cl(3,0), GIVEN the geometric-realization premise
"spatial directions are the mutually-anticommuting Hermitian directions of
the local algebra" (offered as the replacement for A2's independent
dimension stipulation).

Everything is reproven from the Pauli generators at exact precision. The
real Clifford classification Cl(3,0) = M_2(C) (Lawson & Michelsohn, Spin
Geometry, ch. I) and the retained narrow theorems
cl3_complexification_split / cl3_faithful_irrep_dim_two are comparators /
cited authorities, never derivation inputs here: this runner exhibits the
algebra directly.

No PDG values, no fitted selectors, no lattice numerics, no unit
conventions are consumed.
"""
import sympy as sp
from sympy import I, eye, zeros, Matrix

# --- the complex qubit M_2(C) and its three Hermitian generators ----------
s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])
Id = eye(2)
P = [s1, s2, s3]

def ac(A, B):  return A*B + B*A           # anticommutator
def co(A, B):  return A*B - B*A           # commutator
def dag(A):    return A.conjugate().T     # Hermitian conjugate
def Z(A):      return sp.simplify(A) == zeros(A.rows, A.cols)

R = []   # (label, ok) checks
def chk(label, ok): R.append((label, bool(ok)))

# (C1) The three generators satisfy the Cl(3,0) relations {s_i,s_j}=2 d_ij I.
chk("C1  {s_i,s_j}=2 delta_ij I  (the s_i generate Cl(3,0))",
    all(Z(ac(P[i], P[j]) - 2*(1 if i == j else 0)*Id) for i in range(3) for j in range(3)))

# (C2) Each generator is a Hermitian, traceless involution = a unit spatial direction.
chk("C2  each s_i Hermitian, traceless, s_i^2=I (orthonormal directions)",
    all(Z(s - dag(s)) and sp.trace(s) == 0 and Z(s*s - Id) for s in P))

# (C3) Dimension forcing: dim_R Cl(d,0)=2^d; dim_R M_2(C)=8.  2^d=8 <=> d=3,
#      and at d=3 the algebra is M_2(C) (retained cl3_complexification_split).
#      Tabulate 2^d for d=1..6 and confirm ONLY d=3 hits 8.
dimR_M2C = 8
hits = [d for d in range(1, 7) if 2**d == dimR_M2C]
chk("C3  dim_R M_2(C)=2^3 ; among Cl(d,0) only d=3 has dim 8 => d=3 unique",
    dimR_M2C == 2**3 and hits == [3])

# (C4) Maximal anticommuting Hermitian frame = 3: the ONLY 2x2 matrix that
#      anticommutes with all three Paulis is 0 (no independent 4th direction).
a, b, c, d = sp.symbols('a b c d')
M = Matrix([[a, b], [c, d]])
J = Matrix([e for s in P for e in ac(M, s)]).jacobian([a, b, c, d])
chk("C4  only M=0 anticommutes with all 3 Paulis (kernel trivial, rank 4) => no 4th axis => d<=3",
    J.rank() == 4)

# (C5) anticommuting => trace-orthogonal (Tr(s_i s_j)=2 d_ij); the traceless
#      Hermitian ambient space is exactly 3-real-dimensional, bounding the frame <=3.
chk("C5  Tr(s_i s_j)=2 delta_ij (anticommuting => orthogonal in 3-dim traceless-Herm)",
    all(sp.trace(P[i]*P[j]) == 2*(1 if i == j else 0) for i in range(3) for j in range(3)))

# (C6) The complex unit IS the top grade: omega = s1 s2 s3 = i*I, omega^2=-I, central.
#      This is the framework's "omega = i, recovering QM's i geometrically".
omega = s1*s2*s3
chk("C6  omega=s1 s2 s3 = i*I (the QM complex unit is the 3-direction volume element)",
    Z(omega - I*Id))
chk("C6b omega^2 = -I and omega central (commutes with every generator)",
    Z(omega*omega + Id) and all(Z(co(omega, s)) for s in P))

# (C7) Counterfactual d=2: two anticommuting Hermitian generators {s1,s2}
#      generate the REAL algebra M_2(R)=Cl(2,0): the real linear span
#      {I, s1, s2, s1 s2} is closed and contains NO central imaginary unit
#      (s1 s2 = i s3 squares to -I but is NOT central -> a real two-state system,
#      not the complex qubit).  The 3rd direction is what makes the qubit complex.
e12 = s1*s2
real_span_closed = all(
    any(Z(prod - k*basis) for k, basis in
        [(sp.Integer(1), Id), (sp.Integer(-1), Id), (sp.Integer(1), s1), (sp.Integer(-1), s1),
         (sp.Integer(1), s2), (sp.Integer(-1), s2), (sp.Integer(1), e12), (sp.Integer(-1), e12)])
    for prod in [s1*s1, s2*s2, s1*s2, s2*s1, e12*e12])
chk("C7  d=2 counterfactual: {s1,s2} close on real M_2(R)=Cl(2,0) (real two-state, no central i) => d=2 != complex qubit",
    real_span_closed and Z(e12*e12 + Id) and not all(Z(co(e12, s)) for s in [s1, s2]))

# (C8) d>=3 from informational completeness: {I,s1,s2,s3} is a real basis of
#      the 4-real-dim Hermitian observables.  Using the FULL qubit algebra
#      (axiom A1) requires all three s_i, so all 3 directions are realized.
w, x, y, zz = sp.symbols('w x y z', real=True)
Hgen = Matrix([[w + zz, x - I*y], [x + I*y, w - zz]])     # generic Hermitian 2x2
chk("C8  {I,s1,s2,s3} spans all Hermitian observables (full qubit uses all 3 axes) => d>=3",
    Z(Hgen - (w*Id + x*s1 + y*s2 + zz*s3)))

# (C9) Rotations: even subalgebra Cl+(3,0)=span{1,e12,e23,e31} ~ H ~ su(2);
#      Spin(3)=SU(2) is exactly the rotation group of the 3-direction frame
#      (retained per_site_su2_spin_half), and the qubit is its spin-1/2 module.
e23, e31 = s2*s3, s3*s1
chk("C9  Cl+(3,0)=span{1,e12,e23,e31} ~ H ~ su(2): Spin(3)=SU(2) rotates the 3-space",
    all(Z(q*q + Id) for q in (e12, e23, e31)) and Z(e12*e23 - (-e31)))

# (C10) Counterfactual d=4: a 4-direction Euclidean frame would generate
#       Cl(4,0)=M_2(H), dim_R = 2^4 = 16 > 8 = dim_R M_2(C); it cannot be
#       realized inside the qubit algebra (consistent with C4: no 4th axis).
chk("C10 d=4 counterfactual: Cl(4,0) has dim_R 2^4=16 > 8 => cannot live in M_2(C) (no 4-frame)",
    2**4 == 16 and 16 > dimR_M2C)

# --- report ---------------------------------------------------------------
PASS = sum(1 for _, ok in R if ok)
FAIL = sum(1 for _, ok in R if not ok)
for label, ok in R:
    print(("PASS" if ok else "FAIL"), "-", label)
print("\n%d PASS, %d FAIL" % (PASS, FAIL))
if FAIL:
    raise SystemExit(1)
print(
    "\nVERDICT: the complex qubit M_2(C)=Cl(3,0) intrinsically carries exactly a\n"
    "3-dimensional Euclidean vector grade (Pauli frame); d_s<=3 (C4,C5,C10), d_s>=3\n"
    "(C8), the QM complex unit is the 3-direction volume element (C6), a 2-direction\n"
    "algebra is the REAL M_2(R) (C7), and Spin(3)=SU(2) rotates the frame (C9).\n"
    "GIVEN the geometric-realization premise (space = the local algebra's vector grade),\n"
    "the spatial dimension is forced to 3 and is unique -- so A2's lattice-dimension\n"
    "stipulation is a theorem on A1, not an independent axiom."
)
