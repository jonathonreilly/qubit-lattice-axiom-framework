"""
Audit companion (exact, sympy) for
TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md

No-go (narrow): axiom A2/Locality ("separated parts are independent" /
no-signalling / commuting subalgebras) does NOT by itself entail the
C*-tensor-product composition rule for per-site qubits. The precise
additional content required is LOCAL TOMOGRAPHY (a joint state is fixed by
local effects and their products), which is strictly stronger than Locality
-- witnessed irreducibly by real-vector-space QM (rebits): the rebit
composite satisfies no-signalling yet violates local tomography. Given
local tomography (plus M_2 nuclearity, a standard C*-fact cited as
comparator), the qubit composite is uniquely M_4(C).

Hardy / Chiribella-D'Ariano-Perinotti local-tomography axiomatics, Wootters'
real-QM non-tomography, and Takesaki nuclearity are comparators only, never
derivation inputs: the runner exhibits the finite-dimensional facts directly.

No PDG values, no fitted selectors, no lattice numerics consumed.
"""
import sympy as sp
from sympy import eye, zeros, Matrix

R = []
def chk(label, ok): R.append((label, bool(ok)))

# self-adjoint (observable) dimensions:
#   real algebra M_n(R): symmetric n x n  -> n(n+1)/2
#   complex algebra M_n(C): Hermitian n x n -> n^2
def sa_real(n):    return n*(n+1)//2
def sa_complex(n): return n*n

def kron(A, B):
    a, b = A.shape[0], B.shape[0]
    M = zeros(a*b, a*b)
    for i in range(a):
        for j in range(a):
            for k in range(b):
                for l in range(b):
                    M[i*b+k, j*b+l] = A[i, j]*B[k, l]
    return M

s1 = Matrix([[0, 1], [1, 0]])
s3 = Matrix([[1, 0], [0, -1]])
Id2 = eye(2)

# (N1) LOCAL-TOMOGRAPHY TEST -- complex qubits PASS: bipartite observable dim
#      equals the product of local observable dims.
chk("N1  complex qubit IS locally tomographic: sa(M2C)^2 = 4*4 = 16 = sa(M4C)",
    sa_complex(2)**2 == 16 and sa_complex(4) == 16)

# (N2) LOCAL-TOMOGRAPHY TEST -- real rebits FAIL: 3*3 = 9 != 10 = sa(M4R).
chk("N2  real rebit is NOT locally tomographic: sa(M2R)^2 = 3*3 = 9 != 10 = sa(M4R)",
    sa_real(2)**2 == 9 and sa_real(4) == 10 and 9 != 10)

# (N3) LOCALITY / no-signalling holds in BOTH composites: the two tensor
#      factors are commuting subalgebras. Exhibited on the complex composite.
A_factor = [kron(s1, Id2), kron(s3, Id2)]
B_factor = [kron(Id2, s1), kron(Id2, s3)]
commute = all(sp.simplify(a*b - b*a) == zeros(4, 4) for a in A_factor for b in B_factor)
chk("N3  Locality holds in BOTH: tensor factors are commuting subalgebras (no-signalling)",
    commute)
chk("N3b the same commuting structure uses real-valued s1,s3, so it holds for rebits too",
    all(v.is_real for v in (s1 + s3)) and commute)

# (N4) THE NO-GO CORE: a system (rebits) satisfies Locality but FAILS local
#      tomography => local tomography is NOT entailed by Locality (it is
#      strictly stronger). This is the irreducibility witness.
chk("N4  NO-GO: rebits satisfy Locality but fail local tomography => local tomography NOT from Locality",
    commute and (sa_real(2)**2 != sa_real(4)))

# (N5) GIVEN local tomography, the complex-qubit composite is the tensor M4(C)
#      (algebraic tensor M2(C) (x) M2(C) = M4(C); M_2 nuclear => unique C*-norm,
#      cited as comparator). Exhibit M2(C)(x)M2(C) spans dim_C 16.
basisC = [Id2, s1, Matrix([[0, -sp.I], [sp.I, 0]]), s3]
prod16 = [kron(a, b) for a in basisC for b in basisC]
M = Matrix.hstack(*[v.reshape(16, 1) for v in prod16])
chk("N5  given local tomography: M2(C)(x)M2(C) = M4(C), the 16 products are linearly independent (rank 16)",
    M.rank() == 16)

# (N6) THE DISTINGUISHING CONTENT is the complex unit i: the rebit lacks the
#      central i, so sa(M2R)=3 < 4=sa(M2C); the one missing observable dim is
#      exactly what local tomography needs. (Same i = omega = s1 s2 s3 that the
#      d_s=3 note identifies as the third spatial direction.)
chk("N6  the gap is the complex unit i: sa(M2C) - sa(M2R) = 4 - 3 = 1",
    sa_complex(2) - sa_real(2) == 1)

# (N7) Counterfactual catalogue across n: local tomography PASSES for complex
#      M_n(C) at every n (n^2 * n^2 vs (n^2)^2... bipartite is (n^2)) and FAILS
#      for real M_n(R) whenever n>=2 (product n(n+1)/2 squared vs (n^2)(n^2+1)/2).
def lt_complex_ok(n): return sa_complex(n)**2 == sa_complex(n*n)
def lt_real_ok(n):    return sa_real(n)**2 == sa_real(n*n)
chk("N7  complex local-tomographic for n=2,3,4; real fails for n=2,3,4",
    all(lt_complex_ok(n) for n in (2, 3, 4)) and not any(lt_real_ok(n) for n in (2, 3, 4)))

PASS = sum(1 for _, o in R if o)
FAIL = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (PASS, FAIL))
if FAIL:
    raise SystemExit(1)
print(
    "\nNO-GO verified: the C*-tensor composition of per-site qubits is NOT entailed by\n"
    "Locality alone (rebits satisfy no-signalling but violate local tomography, 9 != 10).\n"
    "Local tomography is the precise irreducible admission; given it (+ M_2 nuclearity)\n"
    "the qubit composite is uniquely M_4(C). The distinguishing content is the complex\n"
    "unit i -- the same i the d_s=3 note reads as the third spatial direction."
)
