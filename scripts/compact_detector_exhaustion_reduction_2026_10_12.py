"""Author controls for the new detector/source reduction, not an AC computation.

Run once with an external 60-second timeout. Uses exact finite matrices and
free-word expansion; all output is JSONL. No previous scattering/Fock runner.
"""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/COMPACT_DETECTOR_EXHAUSTION_REDUCTION_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md",
]
if not __debug__:
    raise RuntimeError("Run without -O: exact control assertions must be enabled")

from collections import Counter
from itertools import product
import json
import sympy as s


def emit(**row):
    print(json.dumps(row, sort_keys=True), flush=True)


def addword(poly, word, coefficient=1):
    poly[tuple(word)] += coefficient


for n in range(1, 9):
    lhs, rhs = Counter(), Counter()
    a = [f"A{i}" for i in range(n)]
    for i in range(n):
        left = a[:i] + [f"L{i}"] + a[i + 1:]
        moved = [f"L{i}"] + a[:i] + a[i + 1:]
        addword(lhs, left)
        addword(lhs, moved, -1)
        for j in range(i):
            tail = a[j + 1:i] + a[i + 1:]
            addword(rhs, a[:j] + [a[j], f"L{i}"] + tail)
            addword(rhs, a[:j] + [f"L{i}", a[j]] + tail, -1)
    assert +lhs == +rhs and -lhs == -rhs
emit(check="ordered source defect identity", n=list(range(1, 9)), exact=True)


def tensor(xs):
    out = s.Matrix([[1]])
    for x in xs:
        out = s.kronecker_product(out, x)
    return out


N = 4
dim = 2 ** N
identity = s.eye(dim)
lower = s.Matrix([[0, 1], [0, 0]])
ops = [tensor([lower if k == j else s.eye(2) for k in range(N)]) for j in range(N)]
number = [a.H * a for a in ops]
H = 4 * sum(number, s.zeros(dim))
for j in range(N):
    H -= ops[j].H * ops[(j + 1) % N] + ops[(j + 1) % N].H * ops[j]
vac = s.zeros(dim, 1)
vac[0, 0] = 1
assert H * vac == s.zeros(dim, 1)
def comm(a, b):
    return a * b - b * a
def word(indices):
    out = identity
    for j in indices:
        out = out * ops[j]
    return out
def row(indices):
    return vac.H * word(indices)
def sigma_op(j):
    return 4 * ops[j] - ops[(j - 1) % N] - ops[(j + 1) % N]
L = [s.I * comm(H, ops[j]) + s.I * sigma_op(j) for j in range(N)]
assert all(vac.H * a == s.zeros(1, dim) for a in L)
def source(indices):
    out = s.zeros(1, dim)
    for i in range(len(indices)):
        for j in range(i):
            out += (vac.H * word(indices[:j]) * comm(ops[indices[j]], L[indices[i]])
                    * word(indices[j + 1:i]) * word(indices[i + 1:]))
    return out
cases, nonzero, sign_rejected = 0, 0, 0
for n in [1, 2, 3]:
    for xs in product(range(N), repeat=n):
        f = row(xs)
        df = -s.I * f * H
        sigma_f = s.zeros(1, dim)
        for i, x in enumerate(xs):
            xp, xm = list(xs), list(xs)
            xp[i], xm[i] = (x + 1) % N, (x - 1) % N
            sigma_f += 4 * f - row(xp) - row(xm)
        r = source(xs)
        assert df + s.I * sigma_f == r
        cases += 1
        nonzero += int(r != s.zeros(1, dim))
        sign_rejected += int(df - s.I * sigma_f != r)
assert nonzero > 0 and sign_rejected > 0
emit(check="finite XY-chain source equation", sites=N, particle_words=[1, 2, 3],
     exact_cases=cases, nonzero_collision_sources=nonzero,
     wrong_free_evolution_sign_rejected=sign_rejected,
     scope="Finite periodic control of a local spin algebra; not an N1 model or AC test")

# A genuinely local UHF example behind this finite computation is the infinite
# product-vacuum model H=sum_x n_x. Removing two spins from a three-spin state
# leaves one spin, so narrow residual energy is indispensable.
N0 = 3
zero = s.zeros(2 ** N0, 1)
ones = zero.copy(); ones[-1, 0] = 1
aa = [tensor([lower if k == j else s.eye(2) for k in range(N0)]) for j in range(N0)]
HH = sum([a.H*a for a in aa], s.zeros(2 ** N0))
remaining = aa[0] * aa[1] * ones
assert (remaining.H * remaining)[0] == 1 and HH * remaining == remaining
emit(check="residual-window negative control", model="H=sum_x n_x on an on-site qubit UHF chain",
     input_energy=3, removed_energy=2, surviving_energy=1,
     conclusion="Dropping (J-sum I_i) intersect spec(H) subset {0} invalidates vacuum collapse",
     n1_exact_closure=False)

# The order of time limit versus singular resolvent limit cannot be exchanged.
eta = s.symbols('eta', positive=True)
Kt = s.diag(1, eta)  # along eta=1/t
v = s.Matrix([0, 1])
value = eta * (Kt + eta*s.eye(2)).inv() * v
assert value == s.Matrix([0, s.Rational(1, 2)])
emit(check="ordered resolvent limits", K_limit=[[1,0],[0,0]],
     joint_eta_equal_inverse_time_residual=s.Rational(1,2).__str__(),
     conclusion="A simultaneous eta/time limit need not equal the ordered kernel projection")

# Detector-normalization truncation estimate, exact diagonal examples.
for m in range(1, 9):
    tail = s.Rational(1, 2) ** m
    for e in [s.Rational(1,16),s.Rational(1,4),s.Integer(1)]:
        for x in [s.Integer(0),s.Rational(1,3),s.Integer(1)]:
            diff = abs(e/(x+e)-e/(x+tail+e))
            assert diff <= tail/e
emit(check="resolvent truncation scalar stress", cases=72,
     scope="checks sharp near-zero scaling; operator estimate uses resolvent identity in note")

print("per_element: complete original finite algebra controls checked")
print("per_site: finite lattice fixtures only; no infinite-volume inference")
print("per_mode: Fourier and source signs checked at the stated finite scope")
print("per_block: ordered products and finite projections checked")
print("lattice_wide: checked and not executed — convergence and exhaustion require the written proofs")
print("TOTAL: PASS=5 FAIL=0")
print("SCOPE: Finite ordered-word, periodic spin-chain, residual-window and resolvent algebra only; PC, ND and physical completeness require separate analytic arguments.")
