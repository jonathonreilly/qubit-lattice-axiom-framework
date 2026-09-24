#!/usr/bin/env python3
"""Independent referee for deferred-20260924-star-packets a1.

The star is rebuilt from the Gauss sector and the landed operators. The attempt's
script is not imported. The 256-dimensional semigroup is not integrated again.
"""
from __future__ import annotations

import itertools
import sys

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def vanished(matrix) -> bool:
    return sp.expand(matrix) == sp.zeros(*matrix.shape)


states = [q for q in itertools.product((-1, 0, 1), repeat=4) if sum(q) == 1]
index = {q: i for i, q in enumerate(states)}
dimension = len(states)
records = [sum(1 for entry in q if entry) for q in states]
one_record = [i for i in range(dimension) if records[i] == 1]
three_records = [i for i in range(dimension) if records[i] == 3]
occupied = [i for i in three_records if states[i][0] != 0]

left_sector = []


def operator(rule):
    matrix = sp.zeros(dimension)
    for charge in states:
        for amplitude, image in rule(charge):
            if image not in index:
                left_sector.append((charge, image))
                continue
            matrix[index[image], index[charge]] += amplitude
    return matrix


def hop(charge):
    images = []
    if charge[0] != 0:
        for leaf in (1, 2, 3):
            if charge[leaf] == 0:
                moved = list(charge)
                moved[leaf], moved[0] = charge[0], 0
                images.append((1, tuple(moved)))
    return images


def mark(leaf, sign):
    def rule(charge):
        if charge[0] == 0 and charge[leaf] == 0:
            created = list(charge)
            created[0], created[leaf] = sign, -sign
            return [(1, tuple(created))]
        return []

    return rule


transport = operator(hop)
vertex_empty = sp.diag(*[1 if charge[0] == 0 else 0 for charge in states])
leaf_count = sp.diag(*[sum(1 for leaf in (1, 2, 3) if charge[leaf]) for charge in states])
resolved = [operator(mark(leaf, sign)) for leaf in (1, 2, 3) for sign in (1, -1)]
coherent = [operator(mark(leaf, 1)) + operator(mark(leaf, -1)) for leaf in (1, 2, 3)]
vertex = sp.zeros(dimension, 1)
vertex[index[(1, 0, 0, 0)]] = 1
symmetric = transport * vertex / sp.sqrt(3)

eps, lam, coupling, gap, rate = sp.symbols("epsilon lambda K delta kappa", positive=True)
scale = 1 + 3 * eps**2
kinetic = sp.expand((vertex_empty - eps * transport).T * (vertex_empty - eps * transport))
hamiltonian = gap * eps ** (-4) * kinetic + coupling * lam * leaf_count

# ---------------------------------------------------------------- model
model_ok = dimension == 16 and len(one_record) == 4 and len(three_records) == 12 and not left_sector
model_ok &= vanished(kinetic - (vertex_empty - eps * (transport + transport.T) + eps**2 * transport.T * transport))
block = kinetic.extract(three_records, three_records)
model_ok &= vanished(block * block - scale * block) and sp.expand(block.trace() - 3 * scale) == 0
energy = sp.symbols("x")
model_ok &= sp.expand(kinetic.extract(one_record, one_record).charpoly(energy).as_expr() - energy * (energy - 1) ** 2 * (energy - scale)) == 0
for jumps in (resolved, coherent):
    loss = sum((jump.T * jump for jump in jumps), sp.zeros(dimension))
    model_ok &= loss.extract(one_record, one_record) == 4 * vertex_empty.extract(one_record, one_record)
    model_ok &= loss.extract(three_records, three_records) == sp.zeros(12)
    model_ok &= all(vanished(jump * vertex) and vanished(jump[:, three_records]) and vanished(jump[one_record, :]) for jump in jumps)
dressed = vertex + eps * sp.sqrt(3) * symmetric
model_ok &= vanished((vertex_empty - eps * transport) * dressed)
check(
    "E1 model",
    model_ok,
    "16 Gauss states; on N=3, h^2=(1+3 eps^2)h with trace 3(1+3 eps^2); on N=1 the spectrum is {0,1,1,1+3 eps^2}; both instruments lose 4W on N=1 and nothing on N=3; W-eps F kills the dressed input",
)

# ---------------------------------------------------------------- one jump, invariant unborn plane
plane = sp.Matrix.hstack(vertex, symmetric)
invariant = True
resolved_loss = sum((jump.T * jump for jump in resolved), sp.zeros(dimension))
for vector in (vertex, symmetric):
    for matrix in (hamiltonian, resolved_loss):
        image = sp.expand(matrix * vector)
        invariant &= vanished(image - plane * (plane.T * image))
invariant &= all(sp.expand(hamiltonian[i, k]) == 0 for i in one_record for k in three_records)
invariant &= all(sp.expand(hamiltonian[i, k]) == 0 for i in three_records for k in one_record)
ensembles = {}
for name, jumps in (("resolved", resolved), ("coherent", coherent)):
    assembled = sum((jump * symmetric * symmetric.T * jump.T for jump in jumps), sp.zeros(dimension))
    ensembles[name] = assembled
    invariant &= assembled.trace() == 4 and all(entry.is_rational for entry in assembled)
check(
    "E2 born branch",
    invariant,
    "span{A,s} is invariant, N=1 does not mix with N=3, and both instruments prepare an eps-free ensemble of trace 4",
)

# ---------------------------------------------------------------- lambda = 0, slow no-event root
def bracket(matrix, left, right):
    return sp.expand((left.T * matrix * right)[0])


kinetic_plane = sp.Matrix(2, 2, lambda i, j: bracket(kinetic, (vertex, symmetric)[i], (vertex, symmetric)[j]))
amplitude = -sp.I * gap * eps ** (-4) * kinetic_plane - (2 * rate / eps**2) * sp.diag(0, 1)
rotation = sp.Matrix([[1, sp.sqrt(3) * eps], [sp.sqrt(3) * eps, -1]]) / sp.sqrt(scale)
generator = sp.simplify(rotation.T * amplitude * rotation)
root_shift = sp.symbols("c2")
ansatz = -6 * rate + root_shift * eps**2
residual = sp.expand(sp.together((generator - ansatz * sp.eye(2)).det()) * eps**8)
series = sp.expand(sp.series(residual, eps, 0, 8).removeO())
polynomial = sp.Poly(series, eps)
low_orders = all(sp.expand(polynomial.coeff_monomial(eps**k)) == 0 for k in range(6))
weight = sp.factor(polynomial.coeff_monomial(eps**6) / sp.I)
solved = sp.solve(weight, root_shift)
slow = 18 * rate - 12 * sp.I * rate**2 / gap
high = sp.series((ansatz.subs(root_shift, slow) - generator[0, 0]) / generator[0, 1], eps, 0, 5).removeO()
root_ok = low_orders and solved == [slow] and sp.simplify(high + 2 * sp.sqrt(3) * sp.I * rate / gap * eps**3) == 0
check(
    "E3 no-event root",
    root_ok,
    "z_s = -6 kappa + (18 kappa - 12 i kappa^2/delta) eps^2 + O(eps^4), and the high component is -2 sqrt(3) i (kappa/delta) eps^3 + O(eps^5)",
)

# ---------------------------------------------------------------- lambda > 0 splits the nine occupied states
occupied_gram = (transport.T * transport).extract(occupied, occupied)
eigenspaces = {value: vectors for value, _mult, vectors in occupied_gram.eigenvects()}


def embed(vector):
    full = sp.zeros(dimension, 1)
    for slot, site in enumerate(occupied):
        full[site] = vector[slot]
    return full


null_space = sp.GramSchmidt([embed(vector) for vector in eigenspaces[0]], True)
symmetric_space = sp.GramSchmidt([embed(vector) for vector in eigenspaces[3]], True)
split_ok = len(null_space) == 6 and len(symmetric_space) == 3
split_ok &= all(vanished(hamiltonian * vector - 2 * coupling * lam * vector) for vector in null_space)
pair = sp.Matrix([[3 * eps**2, -sp.sqrt(3) * eps], [-sp.sqrt(3) * eps, 1]]) * gap / eps**4 + coupling * lam * sp.diag(2, 3)
for direction in symmetric_space:
    image = sp.simplify(transport * direction / sp.sqrt(3))
    basis = sp.Matrix.hstack(direction, image)
    split_ok &= sp.simplify(basis.T * basis - sp.eye(2)) == sp.zeros(2)
    split_ok &= sp.simplify(basis.T * hamiltonian * basis - pair) == sp.zeros(2)
shifted = sp.simplify(pair - 2 * coupling * lam * sp.eye(2))
trace = sp.together(shifted.trace())
determinant = sp.together(shifted.det())
claimed_gap = 3 * coupling * lam * eps**2 * (1 - 3 * eps**2)
residual_root = sp.together(claimed_gap**2 - trace * claimed_gap + determinant)
root_error = sp.series(sp.together(residual_root / (trace - 2 * claimed_gap)), eps, 0, 6).removeO()
split_ok &= sp.factor(determinant - 3 * coupling * lam * gap / eps**2) == 0 and root_error == 0
null_projector = sum((vector * vector.T for vector in null_space), sp.zeros(dimension))
symmetric_projector = sum((vector * vector.T for vector in symmetric_space), sp.zeros(dimension))
coherence = {}
preparation = {}
for name in ("resolved", "coherent"):
    density = sp.simplify(ensembles[name] / 4)
    off = sp.simplify(null_projector * density * symmetric_projector)
    singular = []
    for value, multiplicity in (off * off.T).eigenvals().items():
        value = sp.simplify(value)
        if value != 0:
            singular.extend([sp.sqrt(value)] * multiplicity)
    coherence[name] = sp.simplify(2 * sum(singular))
    transported = sp.simplify(density * transport.T)
    nuclear = 0
    for value, multiplicity in (transported * transported.T).eigenvals().items():
        value = sp.simplify(value)
        if value != 0:
            nuclear += multiplicity * sp.sqrt(value)
    preparation[name] = sp.simplify(2 * nuclear)
split_ok &= sp.simplify(coherence["resolved"] - 2 * sp.sqrt(2) / 9) == 0
split_ok &= sp.simplify(coherence["coherent"] - 4 * sp.sqrt(2) / 9) == 0
split_ok &= sp.simplify(preparation["resolved"] - (1 + sp.sqrt(6) / 3)) == 0
split_ok &= sp.simplify(preparation["coherent"] - (sp.sqrt(3) / 3 + 2 * sp.sqrt(6) / 3)) == 0
check(
    "E4 split",
    split_ok,
    "six occupied states sit at 2 K lambda; three blocks give mu_- - 2 K lambda = 3 K lambda eps^2 (1-3 eps^2) + O(eps^6); the ensemble coherences are 2 sqrt(2)/9 and 4 sqrt(2)/9",
)

# ---------------------------------------------------------------- one prepared output versus the occurrence
weights = []
for jump in resolved + coherent:
    image = sp.expand(jump * symmetric)
    norm = sp.simplify((image.T * image)[0])
    state = image / sp.sqrt(norm)
    population = sp.factor(sp.simplify((state.T * kinetic * state)[0] / scale))
    weights.append(population)
expected = {2 * eps**2 / scale, eps**2 / scale, sp.Rational(3, 2) * eps**2 / scale}
leading_ok = set(weights) == expected
for population, constant in (
    (2 * eps**2 / scale, sp.sqrt(2)),
    (eps**2 / scale, 1),
    (sp.Rational(3, 2) * eps**2 / scale, sp.sqrt(sp.Rational(3, 2))),
):
    gap_series = sp.series(2 * sp.sqrt(population * (1 - population)) - 2 * constant * eps, eps, 0, 3).removeO()
    leading_ok &= gap_series == 0
check(
    "C outputs",
    leading_ok,
    "a prepared output has spectral weight c eps^2/(1+3 eps^2) for c in {2,1,3/2}, so its stationary-supply cost is 2 sqrt(c) eps + O(eps^3)",
)

# The dressed input at lambda > 0 lives in span{A,s}. Its coherence is the two-level value.
plane_hamiltonian = sp.Matrix(2, 2, lambda i, j: bracket(hamiltonian, (vertex, symmetric)[i], (vertex, symmetric)[j]))
dressed_coordinates = sp.Matrix([1, sp.sqrt(3) * eps]) / sp.sqrt(scale)
excited_population = None
for _value, _mult, vectors in plane_hamiltonian.eigenvects():
    vector = sp.simplify(vectors[0])
    vector = vector / sp.sqrt(sp.simplify((vector.T * vector)[0]))
    overlap = sp.series(sp.simplify((vector.T * dressed_coordinates)[0] ** 2), eps, 0, 4).removeO()
    if overlap == 0:
        excited_population = sp.simplify((vector.T * dressed_coordinates)[0] ** 2)
input_coherence = sp.series(2 * sp.sqrt(sp.simplify(excited_population * (1 - excited_population))), eps, 0, 7).removeO()
input_ok = sp.simplify(input_coherence - 2 * sp.sqrt(3) * coupling * lam / gap * eps**5) == 0
check(
    "C input",
    input_ok,
    "the dressed input's own energy coherence is 2 sqrt(3) (K lambda/delta) eps^5 + O(eps^7), smaller than the born obstruction",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. The born branch is the eps-free prepared ensemble evolved from an unrecorded birth time. "
    "At lambda = 0 the best energy-stationary trace error is the unborn coherence 4 sqrt(3) (kappa/delta) eps^3 e^{-12 kappa t} "
    "(1+O(eps^2)), while one prepared output costs 2 sqrt(c) eps + O(eps^3) with c in {2,1,3/2}. For every lambda in (0,1] "
    "the electric term splits the zero cluster by 3 K lambda eps^2 (1-3 eps^2)+O(eps^6), and the ensemble coherence across "
    "that split is exactly 2 sqrt(2)/9 (resolved) or 4 sqrt(2)/9 (coherent). The dressed input's own coherence is "
    "2 sqrt(3) (K lambda/delta) eps^5 + O(eps^7). The 256-dimensional semigroup was not integrated again; the birth weight's "
    "uniform limit 1-e^{-12 kappa t} is the landed Duhamel estimate.",
    flush=True,
)
print(
    "HIT: confirmed - at lambda = 0 an energy-stationary supply matches the star's occurrence up to an O(eps^3) coherence, "
    "far below the O(eps) cost of one prepared output; for every lambda in (0,1] the cluster split leaves an ensemble "
    "coherence 2 sqrt(2)/9 (resolved) or 4 sqrt(2)/9 (coherent), so with the landed birth weight the miss tends to "
    "(1 - e^{-12 kappa t}) times that constant",
    flush=True,
)
