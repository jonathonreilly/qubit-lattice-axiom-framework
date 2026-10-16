"""Exact synthetic controls, not an empirical or global uniqueness proof."""
from pathlib import Path
import hashlib
import json
import sympy as s

P = Path(__file__).resolve().parent
I = s.eye(2)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -s.I], [s.I, 0]])
sz = s.diag(1, -1)
axes = [s.Matrix(v) for v in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
x, y, z = axes
checks = []


def sig(v):
    return v[0] * sx + v[1] * sy + v[2] * sz


def simp(m):
    return m.applyfunc(lambda e: s.simplify(s.expand_trig(e)))


def zero(m):
    return simp(m) == s.zeros(*m.shape)


def check(name, ok, **details):
    assert ok, name
    checks.append({"name": name, "passed": True, **details})


def transport(a, b):
    assert a.dot(a) == b.dot(b) == 1 and a.dot(b) != -1
    return simp((I + sig(b) * sig(a)) / s.sqrt(2 * (1 + a.dot(b))))


def twist(a, b, n, k):
    t = k * a.dot(b.cross(n)) / 2
    return simp(transport(a, b) * (s.cos(t) * I - s.I * s.sin(t) * sig(a)))


def rotate(S, a):
    b = simp(S * sig(a) * S.H)
    return s.Matrix([s.simplify(s.trace(b * q) / 2) for q in [sx, sy, sz]])


a = s.Matrix(s.symbols("a0:3", real=True))
b = s.Matrix(s.symbols("b0:3", real=True))
check("Pauli product with oriented cross sign", zero(sig(b) * sig(a) - b.dot(a) * I + s.I * sig(a.cross(b))))
c = a.dot(b)
M = I + sig(b) * sig(a)
res = simp(M.H * M - 2 * (1 + c) * I)
check("unnormalized norm has only unit-axis residual", zero(res - (a.dot(a) * b.dot(b) - 1) * I))
check("intertwiner algebra before normalization", zero(M * sig(a) - sig(b) * M - (a.dot(a) - 1) * sig(b) + (b.dot(b) - 1) * sig(a)))

h = s.symbols("h", real=True)
U = s.cos(h) * I - s.I * s.sin(h) * sy
bt = s.Matrix([s.sin(2 * h), 0, s.cos(2 * h)])
check("generic orbit unitary", zero(U.H * U - I))
check("generic orbit transports z", zero(U * sz * U.H - sig(bt)))
check("generic orbit determinant one", s.simplify(U.det()) == 1)
kp, km = s.symbols("kp km", complex=True)
K = s.diag(kp, km)
Kb = U * K * U.H
reverse = U.H * Kb
forward_adjoint = (U * K).H
check("reciprocity reduces to Hermitian stabilizer", zero(reverse - forward_adjoint - (K - K.H) * U.H))
check("Hermitian unitary stabilizer signs", all(s.diag(i, j).H == s.diag(i, j) and s.diag(i, j) ** 2 == I for i in [-1, 1] for j in [-1, 1]), scope="Continuity/diagonal identity remove the other signs in prose.")

vectors = axes + [s.Matrix([s.Rational(3, 5), s.Rational(4, 5), 0]), s.Matrix([s.Rational(2, 3), s.Rational(-1, 3), s.Rational(2, 3)])]
S = (2 * I - s.I * sx) / s.sqrt(5)
cases = 0
for a in vectors:
    for b in vectors:
        T = transport(a, b)
        assert zero(T.H * T - I)
        assert zero(T * sig(a) * T.H - sig(b))
        assert zero(transport(b, a) - T.H)
        assert zero(transport(rotate(S, a), rotate(S, b)) - S * T * S.H)
        cases += 1
check("rational axis and rotation controls", True, cases=cases)

L = simp(transport(y, z) * transport(x, y) * transport(z, x))
target = s.diag((1 - s.I) / s.sqrt(2), (1 + s.I) / s.sqrt(2))
check("octant loop phase with chronological order", zero(L - target))
check("closed axis does not erase path", zero(L * sz * L.H - sz) and not zero(L - I))
k = s.symbols("k", real=True)
Lt = simp(twist(y, z, z, k) * twist(x, y, z, k) * twist(z, x, z, k))
target_k = target * (s.cos(k / 2) * I - s.I * s.sin(k / 2) * sz)
check("third-neighbor twist accumulates at initial axis", zero(Lt - target_k))
check("third-neighbor reversal exact", zero(twist(y, x, z, k) - twist(x, y, z, k).H))
check("third-neighbor unitary and axis transport", zero(twist(x, y, z, k).H * twist(x, y, z, k) - I) and zero(twist(x, y, z, k) * sx * twist(x, y, z, k).H - sy))
check("third-neighbor simultaneous covariance", zero(twist(rotate(S, x), rotate(S, y), rotate(S, z), k) - S * twist(x, y, z, k) * S.H))
Lreverse = simp(twist(x, z, z, k) * twist(y, x, z, k) * twist(z, y, z, k))
check("fixed-context reverse echo", zero(Lreverse * Lt - I))
changed = simp(twist(y, z, -z, k) * twist(x, y, -z, k) * twist(z, x, -z, k))
check("context change is observable to coherent comparison", not zero(changed.subs(k, s.pi / 2) - Lt.subs(k, s.pi / 2)))

V = s.exp(s.I * s.pi / 6) * transport(x, y)
check("phase-blind channel misses phase", zero(V * sx * V.H - sy) and zero(V * sz * V.H - transport(x, y) * sz * transport(x, y).H))
check("phase-blind reciprocity counterexample", not zero(s.exp(s.I * s.pi / 6) * transport(y, x) - V.H))

def flat(a, b):
    return simp(transport(z, b) * transport(z, a).H)

Lflat = simp(flat(y, z) * flat(x, y) * flat(z, x))
check("reference-frame flat connection erases loop", zero(Lflat - I))
check("flat connection fails full pair covariance", not zero(flat(rotate(S, x), rotate(S, y)) - S * flat(x, y) * S.H))
diagonal = s.diag(kp, km)
check("antipodal commutant cannot intertwine", not zero(diagonal * sz + sz * diagonal))
check("loop scalar flux examples", s.simplify((1 + s.cos(s.pi / 4)) / 2 - (2 + s.sqrt(2)) / 4) == 0 and s.cos(s.pi / 4 + s.pi / 4) == 0, scope="Supplied comparison junction; no event-probability identification.")

output = {
    "source_sha256": hashlib.sha256((P / "NETWORK_EVOLUTION_BLOCK03_v1.md").read_bytes()).hexdigest(),
    "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "sympy_version": s.__version__,
    "checks": checks,
    "summary": {"passed": len(checks), "failed": 0},
    "scope": "Exact synthetic algebra; no empirical validation or global uniqueness inferred from a finite grid.",
}
text = json.dumps(output, indent=2) + "\n"
(P / "ORIENTATION_TRANSPORT_CONTROLS_v1.json").write_text(text)
print(text, end="")
