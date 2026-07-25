#!/usr/bin/env python3
"""Exact gates for the common-frame pair-generator exchange-class note.

Every gate is a computation on constructed objects. This runner reads no
markdown and greps no prose: there are no needle gates, so the PASS total is
entirely mathematical. It is still a GATE COUNT, not a count of independent
scientific facts.

Design rules honoured (they are the reason this runner exists rather than the
four 2026-07-14 probes it supersedes):

* exact `sympy` only -- no float appears as an input to any load-bearing
  comparison, and no numeric tolerance is used anywhere;
* every claimed constant is paired with a CONSTRUCTION-mutation probe: the
  probe rebuilds the object from a changed construction and requires the
  constant to move.  Mutating an assertion is not accepted as a probe;
* no vacuous gate: each check can fail on some input, and the negative
  controls (G1e, G2c, G6e, G5g, G8e, G9f, G10c, G10f) exist precisely to show
  the positive gates are not tautologies;
* an ordered label manifest with a drift detector closes the run.

Groups G8-G10 correct limitation L1 of the note.  G2 computes the
independent-onsite collapse for the CONTINUOUS SU(2) and that computation is
unchanged; G8 shows the collapse is a property of that group rather than of
independent-onsite covariance as such, G9 shows the twisted-diagonal commutant
has dimension exactly 2 for EVERY twist (by a symbolic generic-matrix identity,
not by sampling), and G10 shows that "the law is I - SWAP" names an operator
only relative to a frame while the ground-sector separator does not move.
"""

from __future__ import annotations

import functools
import itertools

import sympy as sp

# --------------------------------------------------------------------------
# Gate manifest (ordered).  finish() fails the run on any drift.
# --------------------------------------------------------------------------
EXPECTED_LABELS = [
    "G1a", "G1b", "G1c", "G1d", "G1e", "G1f", "G1g",
    "G2a", "G2b", "G2c", "G2d",
    "G3a", "G3b", "G3c", "G3d", "G3e", "G3f",
    "G4a", "G4b", "G4c", "G4d", "G4e", "G4f",
    "G5a", "G5b", "G5c", "G5d", "G5e", "G5f", "G5g", "G5h",
    "G6a", "G6b", "G6c", "G6d", "G6e", "G6f", "G6g", "G6h", "G6i", "G6j",
    "G7a", "G7b", "G7c", "G7d", "G7e",
    "G8a", "G8b", "G8c", "G8d", "G8e", "G8f", "G8g",
    "G9a", "G9b", "G9c", "G9d", "G9e", "G9f",
    "G10a", "G10b", "G10c", "G10d", "G10e", "G10f",
]


class CheckRunner:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.labels: list[str] = []

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        self.labels.append(label.split()[0])
        suffix = f" :: {detail}" if detail else ""
        if condition:
            self.passed += 1
            print(f"PASS {label}{suffix}")
        else:
            self.failed += 1
            print(f"FAIL {label}{suffix}")

    def finish(self) -> int:
        if self.labels != EXPECTED_LABELS:
            missing = [x for x in EXPECTED_LABELS if x not in self.labels]
            extra = [x for x in self.labels if x not in EXPECTED_LABELS]
            print(
                "FAIL gate-manifest drift: "
                f"ran={self.labels} expected={EXPECTED_LABELS} "
                f"missing={missing} unexpected={extra}"
            )
            self.failed += 1
        print()
        print(f"PASS={self.passed}")
        print(f"FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# --------------------------------------------------------------------------
# Exact primitives
# --------------------------------------------------------------------------
I2 = sp.eye(2)
I4 = sp.eye(4)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
PAULIS = (X, Y, Z)

SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])

# Exact SU(2) samples.  No floats: 3/5 + 4/5 rational rotation, the Hadamard
# with an exact sqrt(2), and a complex-rational element.
SAMPLE_SU2 = (
    sp.Matrix([[sp.Rational(3, 5), sp.Rational(-4, 5)],
               [sp.Rational(4, 5), sp.Rational(3, 5)]]),
    (X + Z) / sp.sqrt(2),
    sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5) * sp.I],
               [sp.Rational(4, 5) * sp.I, sp.Rational(3, 5)]]),
)


def is_zero_matrix(m: sp.Matrix) -> bool:
    return sp.simplify(m) == sp.zeros(*m.shape)


def eq(left: sp.Matrix, right: sp.Matrix) -> bool:
    return is_zero_matrix(sp.Matrix(left) - sp.Matrix(right))


def dag(m: sp.Matrix) -> sp.Matrix:
    return m.conjugate().T


def kron(*mats: sp.Matrix) -> sp.Matrix:
    out = mats[0]
    for m in mats[1:]:
        out = sp.kronecker_product(out, m)
    return out


def vec(m: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(m).reshape(m.rows * m.cols, 1)


def commutant_basis(generators: tuple[sp.Matrix, ...], dim: int):
    """Exact basis of {M : [M, G] = 0 for every supplied generator G}."""
    variables = sp.symbols(f"m0:{dim * dim}")
    candidate = sp.Matrix(dim, dim, variables)
    equations: list[sp.Expr] = []
    for generator in generators:
        equations.extend(candidate * generator - generator * candidate)
    coefficients, _ = sp.linear_eq_to_matrix(equations, variables)
    return [sp.Matrix(dim, dim, tuple(v)) for v in coefficients.nullspace()]


def span_rank(*matrices: sp.Matrix) -> int:
    return sp.Matrix.hstack(*(vec(m) for m in matrices)).rank()


def exact_less(left, right) -> int:
    """Exact three-way comparison of two real algebraic sympy numbers.

    No float is used: the sign of the difference is decided symbolically and
    the helper refuses anything it cannot decide exactly.
    """
    difference = sp.simplify(sp.nsimplify(left) - sp.nsimplify(right))
    if difference == 0:
        return 0
    if difference.is_negative:
        return -1
    if difference.is_positive:
        return 1
    raise AssertionError(f"cannot order {left} against {right} exactly")


ORDER_KEY = functools.cmp_to_key(exact_less)


def exact_spectrum(matrix: sp.Matrix) -> list:
    """Sorted exact eigenvalue list WITH multiplicity; refuses a non-real."""
    out = []
    for value, multiplicity in matrix.eigenvals().items():
        value = sp.nsimplify(sp.simplify(value))
        if not value.is_real:
            raise AssertionError(f"non-real eigenvalue {value}")
        out.extend([value] * int(multiplicity))
    return sorted(out, key=ORDER_KEY)


def same_multiset(left: list, right: list) -> bool:
    if len(left) != len(right):
        return False
    return all(exact_less(a, b) == 0 for a, b in zip(left, right))


def distinct_levels(matrix: sp.Matrix) -> list:
    levels: list = []
    for value in exact_spectrum(matrix):
        if not levels or exact_less(levels[-1], value) != 0:
            levels.append(value)
    return levels


def ground_degeneracy(matrix: sp.Matrix) -> int:
    """Dimension of the lowest-eigenvalue eigenspace, computed from the
    constructed operator (never assumed from a formula)."""
    triples = matrix.eigenvects()
    values = [sp.nsimplify(sp.simplify(t[0])) for t in triples]
    lowest = sorted(values, key=ORDER_KEY)[0]
    total = 0
    for value, _multiplicity, vectors in triples:
        if exact_less(sp.nsimplify(value), lowest) == 0:
            total += len(vectors)
    return total


# --------------------------------------------------------------------------
# G1 -- the common-frame commutant IS span{I, SWAP}
# --------------------------------------------------------------------------
def diagonal_generators() -> tuple[sp.Matrix, ...]:
    """One and the same SU(2) on both sites: J_a = s_a (x) I + I (x) s_a."""
    return tuple(kron(p, I2) + kron(I2, p) for p in PAULIS)


def independent_generators() -> tuple[sp.Matrix, ...]:
    """Separate SU(2) per site: the six single-site generators."""
    return tuple([kron(p, I2) for p in PAULIS] + [kron(I2, p) for p in PAULIS])


def gate_g1(checks: CheckRunner) -> list[sp.Matrix]:
    section("G1  common-frame commutant = span{I, SWAP}")
    basis = commutant_basis(diagonal_generators(), 4)
    checks.check(
        "G1a common-frame (diagonal SU(2)) commutant has complex dimension 2",
        len(basis) == 2,
        f"dim={len(basis)}",
    )

    base_rank = span_rank(*basis)
    checks.check(
        "G1b identity lies in the computed commutant",
        span_rank(*basis, I4) == base_rank,
        f"rank={base_rank}",
    )
    checks.check(
        "G1c SWAP lies in the computed commutant",
        span_rank(*basis, SWAP) == base_rank,
        f"rank={base_rank}",
    )
    checks.check(
        "G1d span{I, SWAP} EQUALS the computed commutant (both containments)",
        span_rank(I4, SWAP) == 2
        and span_rank(*basis, I4, SWAP) == 2
        and base_rank == 2,
    )
    checks.check(
        "G1e MUTATION non-invariant candidate X(x)I is NOT in the commutant "
        "(so G1d is not a tautology)",
        span_rank(*basis, kron(X, I2)) == 3
        and not eq(kron(X, I2) * diagonal_generators()[1],
                   diagonal_generators()[1] * kron(X, I2)),
        f"rank={span_rank(*basis, kron(X, I2))}",
    )
    dot = kron(X, X) + kron(Y, Y) + kron(Z, Z)
    checks.check(
        "G1f exchange identity SWAP = (I + XX + YY + ZZ)/2 is exact",
        eq(SWAP, (I4 + dot) / 2),
    )
    checks.check(
        "G1g finite frame check: (U(x)U) SWAP (U(x)U)^dag = SWAP for exact "
        "SU(2) samples, while X(x)I is moved by the same conjugation",
        all(eq(kron(u, u) * SWAP * dag(kron(u, u)), SWAP) for u in SAMPLE_SU2)
        and any(
            not eq(kron(u, u) * kron(X, I2) * dag(kron(u, u)), kron(X, I2))
            for u in SAMPLE_SU2
        ),
    )
    return basis


# --------------------------------------------------------------------------
# G2 -- the independent-onsite contrast: commutant = scalars only
# --------------------------------------------------------------------------
def gate_g2(checks: CheckRunner) -> None:
    section("G2  MUTATION of the covariance construction: independent onsite")
    basis = commutant_basis(independent_generators(), 4)
    checks.check(
        "G2a MUTATION independent-onsite covariance collapses the commutant "
        "to complex dimension 1",
        len(basis) == 1,
        f"dim={len(basis)}",
    )
    checks.check(
        "G2b the single surviving direction is the scalars span{I}",
        span_rank(basis[0], I4) == 1,
    )
    checks.check(
        "G2c SWAP is NOT in the independent-onsite commutant "
        "(explicit noncommutation with X(x)I)",
        not eq(SWAP * kron(X, I2), kron(X, I2) * SWAP)
        and span_rank(basis[0], SWAP) == 2,
    )
    # Solve the general element directly: every commutant member is c*I, so
    # a pair generator with a nonzero exchange part cannot be invariant.
    a, b = sp.symbols("a b", real=True)
    general = a * I4 + b * SWAP
    residual = general * kron(X, I2) - kron(X, I2) * general
    solutions = sp.solve(list(residual), [b], dict=True)
    checks.check(
        "G2d hence NO nontrivial pair term survives independent-onsite "
        "covariance: a*I + b*SWAP is invariant only for b = 0",
        solutions == [{b: 0}],
        f"solutions={solutions}",
    )


# --------------------------------------------------------------------------
# G3 -- Hermiticity of both candidates and the licensed quotient
# --------------------------------------------------------------------------
def gate_g3(checks: CheckRunner) -> None:
    section("G3  both sign candidates are Hermitian; the licensed quotient")
    a, b = sp.symbols("a b", real=True)
    symbolic = a * I4 + b * SWAP
    checks.check(
        "G3a h = a*I + b*SWAP is Hermitian for symbolic real a, b",
        eq(dag(symbolic), symbolic),
    )
    plus = sp.Rational(2, 7) * I4 + sp.Rational(5, 3) * SWAP
    minus = sp.Rational(2, 7) * I4 - sp.Rational(5, 3) * SWAP
    checks.check(
        "G3b both candidates are Hermitian at exact rational (a, b) and are "
        "genuinely different operators",
        eq(dag(plus), plus) and eq(dag(minus), minus) and not eq(plus, minus),
    )

    # Channel-level quotient, built from the exponential rather than asserted.
    alpha = sp.Rational(3, 2)
    beta = sp.Rational(-7, 5)
    t = sp.Rational(4, 9)
    scaled = alpha * plus + beta * I4
    left = sp.simplify(sp.exp(-sp.I * scaled * (t / alpha)))
    right = sp.simplify(
        sp.exp(-sp.I * beta * t / alpha) * sp.exp(-sp.I * plus * t)
    )
    checks.check(
        "G3c positive clock rescaling + energy shift leaves the generated "
        "channel unchanged up to a global phase (matrix exponentials)",
        eq(left, right),
    )

    both = []
    for value in (sp.Rational(5, 3), sp.Rational(-5, 3)):
        h = sp.Rational(2, 7) * I4 + value * SWAP
        scale = 1 / abs(value)
        shift = -scale * sp.Rational(2, 7)
        reduced = sp.simplify(scale * h + shift * I4)
        both.append(eq(reduced, sp.sign(value) * SWAP))
    checks.check(
        "G3d alpha = 1/|b| > 0 with beta = -alpha*a carries h to "
        "sign(b)*SWAP exactly, for BOTH signs -- a and |b| are removed",
        all(both),
    )

    # The sign is NOT removable: solve the actual two-parameter system.
    alpha_s, beta_s = sp.symbols("alpha beta", real=True)
    target = alpha_s * SWAP + beta_s * I4 - (-SWAP)
    raw = sp.solve(list(target), [alpha_s, beta_s], dict=True)
    positive = [s for s in raw if sp.simplify(s[alpha_s]) > 0]
    checks.check(
        "G3e NO positive rescaling plus energy shift maps +SWAP to -SWAP: "
        "the only solution has alpha = -1",
        raw == [{alpha_s: -1, beta_s: 0}] and positive == [],
        f"solutions={raw} positive={positive}",
    )
    gamma = sp.symbols("gamma", real=True)
    relaxed = sp.solve(
        list(gamma * SWAP + beta_s * I4 - (-SWAP)), [gamma, beta_s], dict=True
    )
    checks.check(
        "G3f MUTATION dropping the positivity constraint on the rescaling "
        "IDENTIFIES the two signs (gamma = -1 solves it), so alpha > 0 is "
        "exactly what makes the sign physical",
        relaxed == [{gamma: -1, beta_s: 0}],
        f"solutions={relaxed}",
    )


# --------------------------------------------------------------------------
# G4 -- the invariant: ground-sector degeneracy 1 vs 3
# --------------------------------------------------------------------------
def gate_g4(checks: CheckRunner) -> None:
    section("G4  ground-sector degeneracy separates the two signs: 1 vs 3")
    eigenvalues = SWAP.eigenvals()
    ket01 = sp.Matrix([0, 1, 0, 0])
    ket10 = sp.Matrix([0, 0, 1, 0])
    checks.check(
        "G4a SWAP is the transposition (it exchanges |01> and |10>) and its "
        "spectrum is {+1 (x3), -1 (x1)}: the multiplicity split the "
        "invariant reads, on the operator G1 pinned",
        eigenvalues == {sp.Integer(1): 3, sp.Integer(-1): 1}
        and eq(SWAP * ket01, ket10)
        and eq(SWAP * ket10, ket01),
        f"spectrum={eigenvalues}",
    )
    a0 = sp.Rational(2, 7)
    plus = a0 * I4 + sp.Rational(5, 3) * SWAP
    minus = a0 * I4 - sp.Rational(5, 3) * SWAP
    deg_plus = ground_degeneracy(plus)
    checks.check(
        "G4b b > 0: ground sector of a*I + b*SWAP is 1-dimensional "
        "(the singlet)",
        deg_plus == 1,
        f"deg={deg_plus}",
    )
    deg_minus = ground_degeneracy(minus)
    checks.check(
        "G4c MUTATION flip the sign IN THE CONSTRUCTION: the ground sector "
        "becomes 3-dimensional (the triplet)",
        deg_minus == 3,
        f"deg={deg_minus}",
    )

    grid_ok = True
    for alpha in (sp.Rational(1, 4), sp.Integer(1), sp.Rational(7, 2)):
        for beta in (sp.Rational(-11, 3), sp.Integer(0), sp.Rational(9, 5)):
            if ground_degeneracy(alpha * plus + beta * I4) != 1:
                grid_ok = False
            if ground_degeneracy(alpha * minus + beta * I4) != 3:
                grid_ok = False
    checks.check(
        "G4d the degeneracies 1 and 3 are invariant across a 3x3 grid of "
        "exact (alpha > 0, beta) -- they survive the whole licensed quotient",
        grid_ok,
    )
    frame_ok = True
    for u in SAMPLE_SU2:
        conj = kron(u, u) * plus * dag(kron(u, u))
        if ground_degeneracy(sp.simplify(conj)) != 1:
            frame_ok = False
    checks.check(
        "G4e the degeneracy is invariant under a common frame change "
        "(U(x)U) h (U(x)U)^dag for exact SU(2) samples",
        frame_ok,
    )
    set_plus = set(SWAP.eigenvals())
    set_minus = set((-SWAP).eigenvals())
    checks.check(
        "G4f +SWAP and -SWAP have the SAME eigenvalue SET {+1, -1}: only the "
        "multiplicities differ, so a set-valued spectral invariant cannot "
        "separate the signs and the DEGENERACY is what does",
        set_plus == set_minus
        and SWAP.eigenvals() != (-SWAP).eigenvals(),
        f"set={set_plus}",
    )


# --------------------------------------------------------------------------
# G5 -- the one-excitation band minimum is NOT a separator on Z^3
# --------------------------------------------------------------------------
def path_graph(n: int):
    return list(range(n)), [(i, i + 1) for i in range(n - 1)]


def cycle_graph(n: int):
    return list(range(n)), [(i, (i + 1) % n) for i in range(n)]


def cube_graph():
    nodes = list(range(8))
    edges = []
    for u in nodes:
        for bit in range(3):
            v = u ^ (1 << bit)
            if u < v:
                edges.append((u, v))
    return nodes, edges


def complete_bipartite(m: int, n: int):
    nodes = list(range(m + n))
    edges = [(i, m + j) for i in range(m) for j in range(n)]
    return nodes, edges


def z3_torus(length: int):
    """Nearest-neighbour Z^3 chunk with even period `length` in each axis."""
    coords = list(itertools.product(range(length), repeat=3))
    index = {c: i for i, c in enumerate(coords)}
    edges = set()
    for c in coords:
        for axis in range(3):
            shifted = list(c)
            shifted[axis] = (c[axis] + 1) % length
            u, v = index[c], index[tuple(shifted)]
            edges.add((min(u, v), max(u, v)))
    return list(range(len(coords))), sorted(edges), coords


def adjacency(nodes, edges) -> sp.Matrix:
    matrix = sp.zeros(len(nodes), len(nodes))
    for u, v in edges:
        matrix[u, v] += 1
        matrix[v, u] += 1
    return matrix


def one_magnon_block(nodes, edges) -> sp.Matrix:
    """Restriction of sum_e SWAP_e to the one-excitation sector, obtained by
    APPLYING each edge permutation to each one-excitation basis label.

    Basis label x = the flipped site.  SWAP_uv maps the flipped site u to v,
    v to u, and fixes every other label.  Nothing about A or the degree is
    assumed; the block is assembled from the permutation action itself.
    """
    size = len(nodes)
    block = sp.zeros(size, size)
    for x in nodes:
        for u, v in edges:
            if x == u:
                image = v
            elif x == v:
                image = u
            else:
                image = x
            block[image, x] += 1
    return block


def full_space_weight_check(nodes, edges) -> bool:
    """On the FULL 2^n space, verify sum_e SWAP_e preserves excitation number
    (so the one-excitation block above is a genuine invariant restriction)."""
    size = len(nodes)
    for basis in range(2 ** size):
        for u, v in edges:
            bu = (basis >> u) & 1
            bv = (basis >> v) & 1
            image = basis
            if bu != bv:
                image = basis ^ (1 << u) ^ (1 << v)
            if bin(image).count("1") != bin(basis).count("1"):
                return False
    return True


def gate_g5(checks: CheckRunner) -> None:
    section("G5  the one-excitation band minimum is NOT a sign separator")

    c4_nodes, c4_edges = cycle_graph(4)
    q3_nodes, q3_edges = cube_graph()
    k33_nodes, k33_edges = complete_bipartite(3, 3)
    z3_nodes, z3_edges, z3_coords = z3_torus(4)
    p3_nodes, p3_edges = path_graph(3)

    regular_family = {
        "C4": (c4_nodes, c4_edges, 2),
        "Q3": (q3_nodes, q3_edges, 3),
        "K3,3": (k33_nodes, k33_edges, 3),
        "Z^3 torus L=4": (z3_nodes, z3_edges, 6),
    }

    derived_ok = True
    detail = []
    for name, (nodes, edges, degree) in regular_family.items():
        block = one_magnon_block(nodes, edges)
        expected = adjacency(nodes, edges) + (len(edges) - degree) * sp.eye(
            len(nodes)
        )
        if not eq(block, expected):
            derived_ok = False
        detail.append(f"{name}: |E|-deg={len(edges) - degree}")
    checks.check(
        "G5a the one-excitation block ASSEMBLED from the edge permutations "
        "equals A + (|E| - deg)*I on every regular instance",
        derived_ok,
        "; ".join(detail),
    )
    checks.check(
        "G5b the exchange sum preserves excitation number on the FULL 2^n "
        "space (C4 and Q3), so the block is an invariant restriction",
        full_space_weight_check(c4_nodes, c4_edges)
        and full_space_weight_check(q3_nodes, q3_edges),
    )

    parity_ok = all(
        (sum(z3_coords[u]) - sum(z3_coords[v])) % 2 == 1 for u, v in z3_edges
    )
    checks.check(
        "G5c Z^3 nearest-neighbour adjacency is bipartite: x + y + z parity "
        "is a proper 2-colouring of every edge (L = 4 chunk, 192 edges)",
        parity_ok,
        f"edges={len(z3_edges)} sites={len(z3_nodes)}",
    )

    def sublattice(coords_or_colour, nodes):
        return sp.diag(*[sp.Integer(-1) ** coords_or_colour[n] for n in nodes])

    colours = {
        "C4": {n: n % 2 for n in c4_nodes},
        "Q3": {n: bin(n).count("1") % 2 for n in q3_nodes},
        "K3,3": {n: (0 if n < 3 else 1) for n in k33_nodes},
        "P3": {n: n % 2 for n in p3_nodes},
        "Z^3 torus L=4": {n: sum(z3_coords[n]) % 2 for n in z3_nodes},
    }
    bipartite_family = dict(regular_family)
    bipartite_family["P3"] = (p3_nodes, p3_edges, None)

    relabel_ok = True
    for name, (nodes, edges, _deg) in bipartite_family.items():
        A = adjacency(nodes, edges)
        D = sublattice(colours[name], nodes)
        if not eq(D * D, sp.eye(len(nodes))) or not eq(D * A * D, -A):
            relabel_ok = False
    checks.check(
        "G5d the sublattice relabeling D = diag((-1)^parity) satisfies "
        "D^2 = I and D A D = -A on every bipartite instance INCLUDING the "
        "Z^3 chunk",
        relabel_ok,
        f"instances={sorted(bipartite_family)}",
    )

    spectra_ok = True
    spec_detail = []
    for name in ("C4", "Q3", "K3,3", "P3"):
        nodes, edges, _deg = bipartite_family[name]
        A = adjacency(nodes, edges)
        spec = exact_spectrum(A)
        neg = sorted((-value for value in spec), key=ORDER_KEY)
        if not same_multiset(spec, neg):
            spectra_ok = False
        spec_detail.append(f"{name}:{spec}")
    checks.check(
        "G5e hence spec(A) = -spec(A) as multisets: A is similar to -A "
        "through D, so the band is sign-symmetric",
        spectra_ok,
        "; ".join(spec_detail),
    )

    band_ok = True
    band_detail = []
    for name in ("C4", "Q3", "K3,3"):
        nodes, edges, degree = regular_family[name]
        A = adjacency(nodes, edges)
        shift = len(edges) - degree
        for coupling in (sp.Integer(1), sp.Integer(-1)):
            block = coupling * one_magnon_block(nodes, edges)
            shifted = block - coupling * shift * sp.eye(len(nodes))
            if not eq(shifted, coupling * A):
                band_ok = False
        plus_band = exact_spectrum(A)
        minus_band = exact_spectrum(-A)
        if not same_multiset(plus_band, minus_band):
            band_ok = False
        if exact_less(plus_band[0], minus_band[0]) != 0:
            band_ok = False
        band_detail.append(f"{name}: band={plus_band}")
    checks.check(
        "G5f consequently the +J and -J one-excitation bands are IDENTICAL "
        "as multisets after the licensed energy shift, so the band minimum "
        "(and the whole band shape) separates NOTHING on a bipartite graph",
        band_ok,
        "; ".join(band_detail),
    )

    tri_nodes, tri_edges = cycle_graph(3)
    tri_A = adjacency(tri_nodes, tri_edges)
    tri_spec = exact_spectrum(tri_A)
    tri_neg = sorted((-value for value in tri_spec), key=ORDER_KEY)
    no_relabel = True
    for signs in itertools.product((1, -1), repeat=3):
        D = sp.diag(*[sp.Integer(s) for s in signs])
        if eq(D * tri_A * D, -tri_A):
            no_relabel = False
    tri_shift = len(tri_edges) - 2
    tri_plus = exact_spectrum(one_magnon_block(tri_nodes, tri_edges)
                              - tri_shift * sp.eye(3))
    tri_minus = exact_spectrum(-one_magnon_block(tri_nodes, tri_edges)
                               + tri_shift * sp.eye(3))
    checks.check(
        "G5g MUTATION swap the bipartite graph for the non-bipartite "
        "triangle: NO diagonal +-1 relabeling gives D A D = -A, spec(A) is "
        "not sign-symmetric, and the shifted +J / -J bands DIFFER -- so the "
        "band minimum DOES separate there and the failure is bipartiteness",
        no_relabel
        and not same_multiset(tri_spec, tri_neg)
        and not same_multiset(tri_plus, tri_minus)
        and exact_less(tri_plus[0], tri_minus[0]) != 0,
        f"spec={tri_spec} +J band={tri_plus} -J band={tri_minus}",
    )

    A = adjacency(q3_nodes, q3_edges)
    base_min = exact_spectrum(A)[0]
    moved_min = exact_spectrum(A + sp.Rational(11, 4) * sp.eye(8))[0]
    checks.check(
        "G5h independently, the band minimum is not even a quotient "
        "invariant: an energy shift beta*I moves it by beta, whereas the "
        "ground-sector degeneracy of G4 does not move at all",
        sp.simplify(moved_min - base_min - sp.Rational(11, 4)) == 0
        and exact_less(moved_min, base_min) != 0,
        f"min={base_min} -> {moved_min}",
    )


# --------------------------------------------------------------------------
# G6 -- L2: the three-site eta defeats "exactly two"
# --------------------------------------------------------------------------
def three_site_swap(site_a: int, site_b: int) -> sp.Matrix:
    """SWAP between two of three qubits, built from the basis-label action."""
    matrix = sp.zeros(8, 8)
    for index in range(8):
        bits = [(index >> (2 - k)) & 1 for k in range(3)]
        bits[site_a], bits[site_b] = bits[site_b], bits[site_a]
        image = (bits[0] << 2) | (bits[1] << 1) | bits[2]
        matrix[image, index] = 1
    return matrix


def three_site_generators() -> tuple[sp.Matrix, ...]:
    return tuple(
        kron(p, I2, I2) + kron(I2, p, I2) + kron(I2, I2, p) for p in PAULIS
    )


def gate_g6(checks: CheckRunner) -> None:
    section("G6  three sites: an independent dimensionless eta survives")
    swap01 = three_site_swap(0, 1)
    swap02 = three_site_swap(0, 2)
    swap12 = three_site_swap(1, 2)
    h1 = swap01 + swap02
    h2 = swap01 * swap02 + swap02 * swap01

    checks.check(
        "G6a H_1 = SWAP_01 + SWAP_02 and H_2 = SWAP_01 SWAP_02 + "
        "SWAP_02 SWAP_01 are both Hermitian",
        eq(dag(h1), h1) and eq(dag(h2), h2),
    )
    checks.check(
        "G6b both are invariant under the neighbour-exchange automorphism "
        "R = SWAP_12 of the three-site star",
        eq(swap12 * h1 * swap12, h1) and eq(swap12 * h2 * swap12, h2),
    )
    generators = three_site_generators()
    checks.check(
        "G6c both COMMUTE with all three diagonal SU(2) generators, i.e. "
        "both are common-frame covariant -- the check the source runners "
        "asserted but never computed",
        all(eq(h1 * g, g * h1) and eq(h2 * g, g * h2) for g in generators),
    )
    frame_ok = True
    for u in SAMPLE_SU2:
        conj = kron(u, u, u)
        if not eq(sp.simplify(conj * h1 * dag(conj)), h1):
            frame_ok = False
        if not eq(sp.simplify(conj * h2 * dag(conj)), h2):
            frame_ok = False
    checks.check(
        "G6d finite frame check: (U(x)U(x)U) H_i (U(x)U(x)U)^dag = H_i for "
        "exact SU(2) samples",
        frame_ok,
    )
    decoy = kron(Z, Z, I2)
    checks.check(
        "G6e MUTATION / negative control: Z_0 Z_1 is Hermitian too, but it "
        "FAILS both the common-frame commutation and the neighbour-exchange "
        "invariance -- so G6b and G6c are not tautologies",
        eq(dag(decoy), decoy)
        and any(not eq(decoy * g, g * decoy) for g in generators)
        and not eq(swap12 * decoy * swap12, decoy),
    )
    checks.check(
        "G6f I, H_1, H_2 are linearly independent, so eta is a genuinely "
        "new coefficient and not a disguised rescaling or energy shift",
        span_rank(sp.eye(8), h1, h2) == 3,
        f"rank={span_rank(sp.eye(8), h1, h2)}",
    )

    def gap_ratio(eta):
        levels = distinct_levels(h1 + eta * h2)
        return sp.simplify(
            (levels[1] - levels[0]) / (levels[2] - levels[1])
        ), levels

    ratio_zero, spec_zero = gap_ratio(sp.Integer(0))
    checks.check(
        "G6g gap ratio (E1 - E0)/(E2 - E1) = 2 at eta = 0",
        ratio_zero == 2,
        f"levels={spec_zero} ratio={ratio_zero}",
    )
    ratio_third, spec_third = gap_ratio(sp.Rational(1, 3))
    checks.check(
        "G6h gap ratio = 1 at eta = 1/3",
        ratio_third == 1,
        f"levels={spec_third} ratio={ratio_third}",
    )
    swept = {}
    for eta in (sp.Rational(-1, 2), sp.Rational(1, 6), sp.Rational(1, 2)):
        swept[eta] = gap_ratio(eta)[0]
    checks.check(
        "G6i MUTATION sweep eta IN THE CONSTRUCTION: the ratio moves at "
        "every sampled value and never returns to a single number, so eta "
        "is not removable and 'exactly two parameters' fails past one edge",
        len(set(list(swept.values()) + [ratio_zero, ratio_third]))
        == len(swept) + 2,
        f"ratios={ {str(k): str(v) for k, v in swept.items()} }",
    )
    invariant_ok = True
    base = h1 + sp.Rational(1, 3) * h2
    for alpha in (sp.Rational(2, 5), sp.Integer(3)):
        for beta in (sp.Rational(-8, 7), sp.Rational(6, 5)):
            levels = distinct_levels(alpha * base + beta * sp.eye(8))
            ratio = sp.simplify(
                (levels[1] - levels[0]) / (levels[2] - levels[1])
            )
            if ratio != ratio_third:
                invariant_ok = False
    checks.check(
        "G6j the gap RATIO is invariant under h -> alpha*h + beta*I for "
        "exact alpha > 0 and beta, so neither clock rescaling nor an "
        "energy-zero choice can remove eta",
        invariant_ok,
    )


# --------------------------------------------------------------------------
# G7 -- L3: the identity term is NOT inert on a record-conditioned edge set
# --------------------------------------------------------------------------
def active_edges(edges, recorded: frozenset[int]):
    """SUPPLIED convention: an edge is active when neither endpoint carries a
    record.  The framework supplies no formation rule; this convention is the
    antecedent of the conditional L3, not a derived law."""
    return [e for e in edges if e[0] not in recorded and e[1] not in recorded]


def gate_g7(checks: CheckRunner) -> None:
    section("G7  the identity term is not inert on a record-conditioned set")
    nodes, edges = path_graph(3)  # sites 0 - 1 - 2, edges (0,1) and (1,2)

    sector_a = frozenset({0})    # one record at an end site
    sector_b = frozenset()       # no record
    n_a = len(active_edges(edges, sector_a))
    n_b = len(active_edges(edges, sector_b))
    checks.check(
        "G7a the active-edge count is COMPUTED from the graph and the record "
        "configuration and differs between the two record sectors",
        (n_a, n_b) == (1, 2),
        f"N_active={n_a} vs {n_b} on edges={edges}",
    )

    beta = sp.Integer(1)
    t = sp.pi / 3
    phase = sp.diag(sp.exp(-sp.I * beta * n_a * t),
                    sp.exp(-sp.I * beta * n_b * t))
    scalar = phase[0, 0] * sp.eye(2)
    checks.check(
        "G7b the sector phase operator built from those counts is NOT a "
        "scalar multiple of the identity",
        not eq(sp.simplify(phase - scalar), sp.zeros(2, 2)),
        f"diag={sp.simplify(phase[0, 0])}, {sp.simplify(phase[1, 1])}",
    )

    superposition = sp.Matrix([1, 1]) / sp.sqrt(2)
    witness = sp.Matrix([[0, 1], [1, 0]])

    def expectation(state: sp.Matrix) -> sp.Expr:
        raw = (dag(state) * witness * state)[0, 0]
        return sp.simplify(sp.expand_complex(sp.expand(raw)))

    before = expectation(superposition)
    evolved = phase * superposition
    after = expectation(evolved)
    checks.check(
        "G7c on a coherent superposition of the two record sectors the "
        "identity term MOVES the interference term, so it is not a removable "
        "global phase",
        sp.simplify(before - 1) == 0
        and sp.simplify(after - sp.Rational(1, 2)) == 0
        and sp.simplify(after - before) != 0,
        f"witness {before} -> {after}",
    )

    sector_c = frozenset({0})
    sector_d = frozenset({2})
    n_c = len(active_edges(edges, sector_c))
    n_d = len(active_edges(edges, sector_d))
    phase_eq = sp.diag(sp.exp(-sp.I * beta * n_c * t),
                       sp.exp(-sp.I * beta * n_d * t))
    after_eq = expectation(phase_eq * superposition)
    checks.check(
        "G7d MUTATION rebuild the record configuration so both sectors carry "
        "EQUAL active-edge counts: the same identity term becomes a genuine "
        "global phase and the interference term stops moving",
        (n_c, n_d) == (1, 1)
        and eq(sp.simplify(phase_eq - phase_eq[0, 0] * sp.eye(2)),
               sp.zeros(2, 2))
        and sp.simplify(after_eq - before) == 0,
        f"N_active={n_c} vs {n_d}, witness {before} -> {after_eq}",
    )

    h = sp.Rational(2, 7) * I4 + sp.Rational(5, 3) * SWAP
    shift = sp.Rational(-7, 5)
    tau = sp.Rational(4, 9)
    checks.check(
        "G7e on a FIXED active-edge set the identity term IS inert: "
        "exp(-i(h + beta*I)t) = exp(-i*beta*t) exp(-i*h*t) exactly, so R2 "
        "holds exactly where it is claimed and L3 is a boundary, not a "
        "contradiction",
        eq(sp.simplify(sp.exp(-sp.I * (h + shift * I4) * tau)),
           sp.simplify(sp.exp(-sp.I * shift * tau)
                       * sp.exp(-sp.I * h * tau))),
    )


# --------------------------------------------------------------------------
# G8 -- the scalars-only collapse is a property of the CONTINUOUS group,
#       not of independent-onsite covariance as such
# --------------------------------------------------------------------------
def herm_commutant_real_dim(generators, dim: int = 4) -> int:
    """Real dimension of the HERMITIAN part of the commutant, solved natively.

    The Hermitian ansatz is built with real symbols, the commutation residual
    is split into its exact real and imaginary parts, and the dimension is
    read off the rank of the resulting exact real linear system.  Nothing is
    assumed from a formula and no float is used.
    """
    entries = sp.symbols(f"h0:{dim * dim}", real=True)
    parts = sp.symbols(f"k0:{dim * dim}", real=True)
    candidate = sp.zeros(dim, dim)
    variables: list[sp.Symbol] = []
    for row in range(dim):
        for col in range(dim):
            if row == col:
                candidate[row, col] = entries[row * dim + col]
                variables.append(entries[row * dim + col])
            elif row < col:
                real_part = entries[row * dim + col]
                imag_part = parts[row * dim + col]
                candidate[row, col] = real_part + sp.I * imag_part
                candidate[col, row] = real_part - sp.I * imag_part
                variables.extend([real_part, imag_part])
    equations: list[sp.Expr] = []
    for generator in generators:
        for residual in sp.expand(candidate * generator - generator * candidate):
            real_part, imag_part = sp.expand(residual).as_real_imag()
            equations.extend([sp.expand(real_part), sp.expand(imag_part)])
    coefficients, _ = sp.linear_eq_to_matrix(equations, variables)
    return len(variables) - coefficients.rank()


def edge_axis_rotation() -> sp.Matrix:
    """Spin lift of the pi/2 lattice rotation about the edge axis.

    This is a FINITE element.  Whether the proper cubic rotations act on
    M_2(C) at all is itself supplied and is not asserted here; the element is
    used only to show which group the scalars-only collapse actually needs.
    """
    zeta = sp.exp(sp.I * sp.pi / 4)
    return sp.Matrix([[zeta ** -1, 0], [0, zeta]])


def gate_g8(checks: CheckRunner) -> None:
    section("G8  the scalars-only collapse needs the CONTINUOUS group")
    rot = edge_axis_rotation()
    checks.check(
        "G8a the edge-axis rotation lift is unitary with u^4 = -I, so u (x) u "
        "generates a group of order exactly 4 on the edge",
        eq(dag(rot) * rot, I2)
        and eq(rot ** 4, -I2)
        and eq(kron(rot, rot) ** 4, I4)
        and not eq(kron(rot, rot) ** 2, I4),
        "order 4",
    )

    common_finite = herm_commutant_real_dim([kron(rot, rot)])
    checks.check(
        "G8b COMMON-frame covariance under that FINITE group leaves Hermitian "
        "real dimension 6, not 2 -- the step down to 2 is bought by the "
        "continuous SU(2)",
        common_finite == 6,
        f"dim_R={common_finite}",
    )

    independent_finite = herm_commutant_real_dim([kron(rot, I2), kron(I2, rot)])
    checks.check(
        "G8c INDEPENDENT-onsite covariance under the SAME finite group leaves "
        "Hermitian real dimension 4: a nontrivial pair law SURVIVES",
        independent_finite == 4,
        f"dim_R={independent_finite}",
    )

    zz = kron(Z, Z)
    checks.check(
        "G8d explicit witness Z(x)Z is Hermitian, commutes with u(x)I and with "
        "I(x)u SEPARATELY, and is not a multiple of I",
        eq(dag(zz), zz)
        and eq(zz * kron(rot, I2), kron(rot, I2) * zz)
        and eq(zz * kron(I2, rot), kron(I2, rot) * zz)
        and span_rank(I4, zz) == 2,
        "nontrivial independent-onsite-invariant pair term",
    )
    checks.check(
        "G8e MUTATION rebuild the same witness against the CONTINUOUS "
        "independent generators: Z(x)Z stops being invariant, so G8c is a "
        "statement about the finite group and does not contradict G2a",
        any(not eq(zz * g, g * zz) for g in independent_generators()),
        "continuous group is what kills it",
    )

    flip_lift = sp.Matrix([[0, -sp.I], [-sp.I, 0]])
    flip = kron(flip_lift, flip_lift) * SWAP
    full_stabiliser = herm_commutant_real_dim([kron(rot, rot), flip])
    checks.check(
        "G8f the endpoint flip is a unitary involution that inverts the "
        "rotation lift, and the FULL order-8 common-frame edge stabiliser "
        "still leaves Hermitian real dimension 5, not 2",
        eq(dag(flip) * flip, I4)
        and eq(flip * flip, I4)
        and eq(flip * kron(rot, rot) * dag(flip), dag(kron(rot, rot)))
        and full_stabiliser == 5,
        f"dim_R={full_stabiliser}",
    )

    bare = herm_commutant_real_dim([SWAP])
    checks.check(
        "G8g and with only the bare endpoint exchange the class is Hermitian "
        "real dimension 10, so the chain 16 -> 10 -> 6 -> 5 -> 2 is monotone "
        "and every step past 5 is supplied",
        bare == 10 and herm_commutant_real_dim(diagonal_generators()) == 2,
        f"bare={bare} continuous_common=2",
    )


# --------------------------------------------------------------------------
# G9 -- the twisted diagonal: dimension exactly 2 for EVERY twist
# --------------------------------------------------------------------------
def twisted_generators(twist: sp.Matrix) -> tuple[sp.Matrix, ...]:
    """Generators of the twisted diagonal {(u, w u w^dag)} on one edge."""
    return tuple(kron(p, I2) + kron(I2, twist * p * dag(twist)) for p in PAULIS)


TWISTS = SAMPLE_SU2 + (
    sp.Matrix([[sp.Rational(1, 2) + sp.Rational(1, 2) * sp.I,
                sp.Rational(1, 2) - sp.Rational(1, 2) * sp.I],
               [-sp.Rational(1, 2) - sp.Rational(1, 2) * sp.I,
                sp.Rational(1, 2) - sp.Rational(1, 2) * sp.I]]),
)


def gate_g9(checks: CheckRunner) -> None:
    section("G9  the twisted diagonal has commutant dimension 2 for EVERY twist")
    symbols = sp.symbols("w0 w1 w2 w3")
    generic = sp.Matrix(2, 2, symbols)
    generic_inverse = generic.adjugate() / generic.det()
    conjugation_ok = all(
        eq(
            kron(I2, generic) * (kron(p, I2) + kron(I2, p)) * kron(I2, generic_inverse),
            kron(p, I2) + kron(I2, sp.simplify(generic * p * generic_inverse)),
        )
        for p in PAULIS
    )
    checks.check(
        "G9a SYMBOLIC, for EVERY invertible W: (I(x)W)(P(x)I + I(x)P)(I(x)W)^-1 "
        "= P(x)I + I(x)(W P W^-1), so the twisted diagonal is exactly the "
        "(I(x)W)-conjugate of the diagonal -- not a sampled claim",
        conjugation_ok,
        "generic 2x2 W with det W != 0",
    )
    checks.check(
        "G9b SYMBOLIC, same W: (I(x)W) SWAP (I(x)W)^-1 = (W^-1 (x) W) SWAP, so "
        "conjugation carries span{I, SWAP} onto span{I, (W^-1(x)W)SWAP} and "
        "the twisted commutant dimension is 2 for EVERY twist",
        eq(kron(I2, generic) * SWAP * kron(I2, generic_inverse),
           kron(generic_inverse, generic) * SWAP),
    )

    dims = []
    equal_spans = []
    for twist in TWISTS:
        basis = commutant_basis(twisted_generators(twist), 4)
        dims.append(len(basis))
        twisted_swap = kron(dag(twist), twist) * SWAP
        equal_spans.append(
            span_rank(I4, twisted_swap) == 2
            and span_rank(*basis, I4, twisted_swap) == 2
        )
    checks.check(
        "G9c NATIVE solve on exact unitary twists confirms the symbolic result: "
        "complex dimension exactly 2 every time",
        all(d == 2 for d in dims),
        f"dims={dims}",
    )
    checks.check(
        "G9d and the solved commutant EQUALS span{I, (w^dag(x)w)SWAP} in both "
        "containments for every sampled twist",
        all(equal_spans),
        f"{equal_spans}",
    )

    degeneracies = []
    for twist in TWISTS:
        twisted_swap = kron(dag(twist), twist) * SWAP
        degeneracies.append((
            ground_degeneracy(sp.Rational(2, 7) * I4 + sp.Rational(5, 3) * twisted_swap),
            ground_degeneracy(sp.Rational(2, 7) * I4 - sp.Rational(5, 3) * twisted_swap),
        ))
    checks.check(
        "G9e the R3 separator is TWIST-INVARIANT: ground-sector degeneracy is 1 "
        "for b > 0 and 3 for b < 0 for every twist, so dropping flatness does "
        "not dissolve the two-point menu",
        all(pair == (1, 3) for pair in degeneracies),
        f"(b>0, b<0) degeneracies={degeneracies}",
    )

    degenerate_twist_dim = len(commutant_basis(tuple(kron(p, I2) for p in PAULIS), 4))
    checks.check(
        "G9f MUTATION rebuild the correlation with the degenerate homomorphism "
        "u -> I instead of an automorphism twist: the dimension MOVES 2 -> 4, "
        "so 'dimension 2' is carried by the twisted-diagonal construction and "
        "is not a tautology",
        degenerate_twist_dim == 4,
        f"dim={degenerate_twist_dim}",
    )


# --------------------------------------------------------------------------
# G10 -- "the law is I - SWAP" is not a frame-invariant sentence, and the
#        twist that moves it carries gauge-invariant holonomy
# --------------------------------------------------------------------------
def gate_g10(checks: CheckRunner) -> None:
    section("G10  the law's NAME is frame-relative; its holonomy is not")
    twist = SAMPLE_SU2[0]
    twisted_swap = kron(dag(twist), twist) * SWAP
    checks.check(
        "G10a (w^dag (x) w) SWAP is Hermitian for every sampled unitary twist, "
        "so it is an admissible pair generator, not a formal object",
        all(eq(dag(kron(dag(t), t) * SWAP), kron(dag(t), t) * SWAP) for t in TWISTS),
    )
    checks.check(
        "G10b but it is NOT in span{I, SWAP}: the span rank rises to 3, so "
        "'the law is I - SWAP' is not a frame-invariant sentence",
        span_rank(I4, SWAP, twisted_swap) == 3,
        f"rank={span_rank(I4, SWAP, twisted_swap)}",
    )
    checks.check(
        "G10c MUTATION rebuild the same construction with a CENTRAL twist "
        "w = -I: the operator lands back inside span{I, SWAP} and the rank "
        "falls to 2, so G10b is carried by the twist and not by the algebra",
        span_rank(I4, SWAP, kron(dag(-I2), -I2) * SWAP) == 2,
        f"rank={span_rank(I4, SWAP, kron(dag(-I2), -I2) * SWAP)}",
    )
    checks.check(
        "G10d yet the ground-sector degeneracy of a*I + b*(w^dag(x)w)SWAP is "
        "still 1 vs 3: what the frame moves is the operator's NAME, not the "
        "separating invariant",
        ground_degeneracy(sp.Rational(2, 7) * I4 + sp.Rational(5, 3) * twisted_swap) == 1
        and ground_degeneracy(sp.Rational(2, 7) * I4 - sp.Rational(5, 3) * twisted_swap) == 3,
    )

    # A twist assignment on a closed 4-cycle of edges.  Per-site re-framing
    # sends w_e -> g_x w_e g_y^dag, so the loop product is conjugated and its
    # trace is invariant.
    holonomy = twist
    checks.check(
        "G10e on a closed 4-cycle the twist assignment (I, I, I, w) has loop "
        "product w with exact trace 6/5, which is neither 2 nor -2, so the "
        "assignment is NOT gauge-equivalent to the flat one",
        sp.simplify(sp.trace(holonomy)) == sp.Rational(6, 5)
        and sp.simplify(sp.trace(holonomy) - 2) != 0
        and sp.simplify(sp.trace(holonomy) + 2) != 0,
        f"trace={sp.simplify(sp.trace(holonomy))}",
    )
    checks.check(
        "G10f MUTATION apply an actual per-site re-framing to the loop product "
        "for every sampled frame: the trace does not move, so no re-framing "
        "flattens it -- dropping flatness ENLARGES the class by a link field "
        "rather than dissolving the two-point menu",
        all(sp.simplify(sp.trace(g * holonomy * dag(g)) - sp.trace(holonomy)) == 0
            for g in SAMPLE_SU2)
        and sp.simplify(sp.trace(I2)) == 2,
        "conjugation-invariant; flat loop product would have trace 2",
    )


def main() -> int:
    checks = CheckRunner()
    gate_g1(checks)
    gate_g2(checks)
    gate_g3(checks)
    gate_g4(checks)
    gate_g5(checks)
    gate_g6(checks)
    gate_g7(checks)
    gate_g8(checks)
    gate_g9(checks)
    gate_g10(checks)
    section("SUMMARY")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
