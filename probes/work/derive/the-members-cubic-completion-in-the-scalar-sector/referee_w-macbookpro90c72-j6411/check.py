#!/usr/bin/env python3
"""Independent count of first-order cubic classes of the member, scalar sector.

Does not import the author's script. Rotation-invariant symbols only.
Cubic-symmetric counts and the exact lattice lift are not rebuilt.
"""
import itertools

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


I3 = sp.eye(3)
w1, w2 = sp.symbols("w1 w2")
zeta, chi = sp.symbols("zeta chi")
RANK = {"n": 0, "N": 1, "h": 2, "zeta": 0, "xi": 1}
PARITY = {"n": 1, "N": -1, "h": 1, "zeta": -1, "xi": 1}
KINDS = ("n", "N", "h")
PAIRS = ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2))


def cross(left, right):
    """Polarisation of 1/4[tr Hd^2 - (tr Hd)^2] + n R1 + R2."""
    def rate(field):
        return field["w"] * field["h"] - field["k"] * field["N"].T - field["N"] * field["k"].T

    def curvature(field):
        return (field["k"].T * field["h"] * field["k"])[0] - (field["k"].dot(field["k"])) * field["h"].trace()

    left_rate, right_rate = rate(left), rate(right)
    kinetic = sp.Rational(1, 2) * ((left_rate * right_rate).trace() - left_rate.trace() * right_rate.trace())
    lapse = left["n"] * curvature(right) + right["n"] * curvature(left)
    dot = (left["k"].dot(right["k"]))
    mixed = (
        -sp.Rational(1, 2) * dot * (left["h"] * right["h"]).trace()
        + ((left["h"] * left["k"]).dot(right["h"] * right["k"]))
        - sp.Rational(1, 2) * ((left["h"] * left["k"]).dot(right["k"]) * right["h"].trace()
                               + (right["h"] * right["k"]).dot(left["k"]) * left["h"].trace())
        + sp.Rational(1, 2) * dot * left["h"].trace() * right["h"].trace()
    )
    return sp.expand(kinetic + lapse + mixed)


class Problem:
    def __init__(self, fields):
        self.fields = fields
        a, b, c = sp.symbols("a b c")
        self.momenta = [a, b, c]
        self.wave = [sp.Matrix([a, 0, 0]), sp.Matrix([b, c, 0]), sp.Matrix([-a - b, -c, 0])]
        self.frequency = [w1, w2, -w1 - w2]
        self.shift = sp.Matrix(sp.symbols("xi0:3"))
        self.leg = []
        for slot in range(3):
            if fields == "scalar":
                lapse, bond, psi, length = sp.symbols(f"n{slot+1} B{slot+1} p{slot+1} E{slot+1}")
                wave = self.wave[slot]
                self.leg.append(dict(
                    n=lapse, N=wave * bond, h=2 * psi * I3 + 2 * wave * wave.T * length,
                    syms=[lapse, bond, psi, length], pot=(lapse, bond, psi, length),
                ))
            else:
                lapse = sp.Symbol(f"n{slot+1}")
                shift = sp.Matrix(sp.symbols(f"N{slot+1}_0:3"))
                strain = sp.symbols(f"h{slot+1}_0:6")
                metric = sp.Matrix(3, 3, lambda i, j: strain[PAIRS.index((min(i, j), max(i, j)))])
                self.leg.append(dict(n=lapse, N=shift, h=metric, syms=[lapse, *shift, *strain]))
        gauge = [zeta, chi] if fields == "scalar" else [zeta, *self.shift]
        self.generators = self.momenta + [w1, w2] + gauge + [symbol for leg in self.leg for symbol in leg["syms"]]

    def pairings(self, indices):
        indices = list(indices)
        if not indices:
            yield []
            return
        first, rest = indices[0], indices[1:]
        for partner in rest:
            others = [index for index in rest if index != partner]
            for tail in self.pairings(others):
                yield [(first, partner)] + tail

    def contract(self, factors, blocks, free=()):
        total = 0
        width = sum(rank for rank, _ in factors)
        for values in itertools.product(range(3), repeat=len(blocks)):
            assign = [None] * (width + len(free))
            ok = True
            for offset, value in enumerate(free):
                assign[width + offset] = value
            for block, value in zip(blocks, values):
                for index in block:
                    if assign[index] not in (None, value):
                        ok = False
                    assign[index] = value
            if not ok:
                continue
            term = 1
            cursor = 0
            for rank, function in factors:
                term *= function(tuple(assign[cursor:cursor + rank]))
                cursor += rank
                if term == 0:
                    break
            total += term
        return total

    def view(self, slot):
        leg = self.leg[slot]
        return dict(n=leg["n"], N=leg["N"], h=leg["h"], k=self.wave[slot], w=self.frequency[slot])

    def field_factor(self, kind, slot, timed, derivatives):
        rank = RANK[kind]
        leg = self.leg[slot]
        wave = self.wave[slot]
        clock = self.frequency[slot] if timed else 1
        reader = {"n": lambda idx: leg["n"], "N": lambda idx: leg["N"][idx[0]], "h": lambda idx: leg["h"][idx[0], idx[1]]}[kind]

        def read(idx):
            value = reader(idx[:rank]) * clock
            for derivative in range(derivatives):
                value *= wave[idx[rank + derivative]]
            return value

        return rank + derivatives, read

    def gauge_factor(self, kind, timed, derivatives):
        wave = self.wave[0]
        clock = self.frequency[0] if timed else 1
        if kind == "zeta":
            return derivatives, lambda idx: zeta * clock * sp.Mul(*[wave[i] for i in idx])
        parameter = wave * chi if self.fields == "scalar" else self.shift
        return 1 + derivatives, lambda idx: parameter[idx[0]] * clock * sp.Mul(*[wave[i] for i in idx[1:]])

    def gauge_on_first(self, expression):
        wave, clock = self.wave[0], self.frequency[0]
        leg = self.leg[0]
        if self.fields == "scalar":
            lapse, bond, psi, length = leg["pot"]
            replacement = {lapse: clock * zeta, bond: clock * chi - zeta, psi: 0, length: chi}
        else:
            shift = clock * self.shift - wave * zeta
            strain = wave * self.shift.T + self.shift * wave.T
            replacement = {leg["n"]: clock * zeta}
            for index in range(3):
                replacement[leg["N"][index]] = shift[index]
            for (row, column), symbol in zip(PAIRS, leg["syms"][4:]):
                replacement[symbol] = strain[row, column]
        return sp.expand(expression.subs(replacement, simultaneous=True))

    def vertices(self):
        found = []
        for kinds in itertools.combinations_with_replacement(KINDS, 3):
            for pattern in itertools.product(((0, 0), (1, 0), (0, 1), (1, 1), (0, 2)), repeat=3):
                if sum(time + space for time, space in pattern) != 2:
                    continue
                if (sum(time for time, _ in pattern) + kinds.count("N")) % 2:
                    continue
                indices = sum(RANK[kind] + space for kind, (_, space) in zip(kinds, pattern))
                if indices % 2:
                    continue
                for pairing in self.pairings(range(indices)):
                    found.append((kinds, pattern, tuple(pairing)))
        return found

    def vertex_symbol(self, monomial):
        kinds, pattern, pairing = monomial
        total = 0
        for order in itertools.permutations(range(3)):
            factors = [self.field_factor(kind, order[slot], time, space)
                       for slot, (kind, (time, space)) in enumerate(zip(kinds, pattern))]
            total += self.contract(factors, list(pairing))
        return sp.expand(total)

    def output_field(self, factors, pairing, kind, wave, clock):
        rank = RANK[kind]
        component = {values: self.contract(factors, list(pairing), free=values)
                     for values in itertools.product(range(3), repeat=rank)}
        field = dict(n=0, N=sp.zeros(3, 1), h=sp.zeros(3), k=wave, w=clock)
        if kind == "n":
            field["n"] = component[()]
        elif kind == "N":
            field["N"] = sp.Matrix([component[(index,)] for index in range(3)])
        else:
            field["h"] = sp.Matrix(3, 3, lambda i, j: (component[(i, j)] + component[(j, i)]) / 2)
        return field

    def deformations(self):
        found = []
        for parameter in ("zeta", "xi"):
            for source in KINDS:
                for place in ("eps", "phi"):
                    for timed, derivatives in ((1, 0), (0, 1)):
                        for target in KINDS:
                            if PARITY[target] != PARITY[parameter] * PARITY[source] * (-1)**timed:
                                continue
                            indices = RANK[parameter] + RANK[source] + derivatives + RANK[target]
                            if indices % 2:
                                continue
                            for pairing in self.pairings(range(indices)):
                                found.append((parameter, source, place, timed, derivatives, target, tuple(pairing)))
        return found

    def deformation_symbol(self, monomial):
        parameter, source, place, timed, derivatives, target, pairing = monomial
        total = 0
        for field_slot, other in ((1, 2), (2, 1)):
            gauge_time, gauge_derivatives = (timed, derivatives) if place == "eps" else (0, 0)
            field_time, field_derivatives = (timed, derivatives) if place == "phi" else (0, 0)
            produced = self.output_field(
                [self.gauge_factor(parameter, gauge_time, gauge_derivatives),
                 self.field_factor(source, field_slot, field_time, field_derivatives)],
                pairing, target, self.wave[0] + self.wave[field_slot], self.frequency[0] + self.frequency[field_slot],
            )
            total += cross(produced, self.view(other))
        return sp.expand(total)

    def redefinitions(self):
        found = []
        for left, right in itertools.combinations_with_replacement(KINDS, 2):
            for target in KINDS:
                if PARITY[target] != PARITY[left] * PARITY[right]:
                    continue
                indices = RANK[left] + RANK[right] + RANK[target]
                if indices % 2:
                    continue
                for pairing in self.pairings(range(indices)):
                    found.append((left, right, target, tuple(pairing)))
        return found

    def redefinition_symbol(self, monomial):
        left, right, target, pairing = monomial
        total = 0
        for omitted in range(3):
            slots = [slot for slot in range(3) if slot != omitted]
            for first, second in (slots, slots[::-1]):
                produced = self.output_field(
                    [self.field_factor(left, first, 0, 0), self.field_factor(right, second, 0, 0)],
                    pairing, target, self.wave[first] + self.wave[second], self.frequency[first] + self.frequency[second],
                )
                total += cross(produced, self.view(omitted))
        return sp.expand(total)

    def matrix(self, expressions):
        polynomials = [sp.Poly(expr, *self.generators).as_dict() if expr != 0 else {} for expr in expressions]
        keys = sorted({key for polynomial in polynomials for key in polynomial})
        index = {key: row for row, key in enumerate(keys)}
        rows = [[QQ(0)] * len(expressions) for _ in keys]
        for column, polynomial in enumerate(polynomials):
            for key, value in polynomial.items():
                rational = sp.Rational(value)
                rows[index[key]][column] = QQ(rational.p, rational.q)
        return DomainMatrix(rows, (len(keys), len(expressions)), QQ)

    def rank(self, expressions):
        return self.matrix(expressions).rank() if expressions else 0

    def classify(self):
        monomials = self.vertices()
        symbols = [self.vertex_symbol(monomial) for monomial in monomials]
        deformations = [self.deformation_symbol(monomial) for monomial in self.deformations()]
        redefinitions = [self.redefinition_symbol(monomial) for monomial in self.redefinitions()]
        _, vertex_pivot = self.matrix(symbols).rref()
        independent = [symbols[index] for index in vertex_pivot]
        _, redefinition_pivot = self.matrix(redefinitions).rref()
        redefinition_basis = [redefinitions[index] for index in redefinition_pivot]
        kernel = self.matrix([self.gauge_on_first(symbol) for symbol in independent] + deformations).nullspace().to_Matrix()
        solutions = []
        for row in range(kernel.rows):
            coefficients = kernel.row(row)[:len(independent)]
            if any(coefficient != 0 for coefficient in coefficients):
                solutions.append(sp.expand(sum(coefficients[index] * independent[index]
                                               for index in range(len(independent)) if coefficients[index] != 0)))
        consistent = self.rank(solutions)
        union = self.rank(solutions + redefinition_basis)
        invariant_kernel = self.matrix([self.gauge_on_first(solution) for solution in solutions]).nullspace().to_Matrix() if solutions else sp.zeros(0)
        invariants = [sp.expand(sum(invariant_kernel[row, index] * solutions[index] for index in range(len(solutions))))
                      for row in range(invariant_kernel.rows)] if solutions else []
        strict = self.rank(invariants + redefinition_basis) - len(redefinition_basis)
        return dict(vertices=len(monomials), independent=len(independent), consistent=consistent,
                    redefinitions=len(redefinition_basis), union=union, classes=union - len(redefinition_basis),
                    strict=strict)


# gauge invariance of the quadratic member, for a generic field
wave = sp.Matrix(sp.symbols("q1:4"))
clock = sp.Symbol("om")
amplitude = sp.symbols("y0:10")
generic = dict(
    n=amplitude[0], N=sp.Matrix(amplitude[1:4]),
    h=sp.Matrix(3, 3, lambda i, j: amplitude[4 + PAIRS.index((min(i, j), max(i, j)))]),
    k=-wave, w=-clock,
)
time_shift = sp.Symbol("z")
space_shift = sp.Matrix(sp.symbols("x1:4"))
check(
    "time relabelling",
    cross(dict(n=clock * time_shift, N=-wave * time_shift, h=sp.zeros(3), k=wave, w=clock), generic) == 0,
    "the member is invariant under dn = d zeta and dN = -grad zeta",
)
check(
    "space relabelling",
    cross(dict(n=0, N=clock * space_shift, h=wave * space_shift.T + space_shift * wave.T, k=wave, w=clock), generic) == 0,
    "the member is invariant under dh = d xi + d xi^T and dN = xi-dot",
)

# scalar reduction
probe = Problem("scalar")
momentum = probe.wave[0]
metric = probe.leg[0]["h"]
psi = probe.leg[0]["pot"][2]
check(
    "scalar reduction",
    sp.simplify(metric * momentum - momentum * metric.trace() + 4 * momentum * psi) == sp.zeros(3, 1),
    "on h = 2 psi I + 2 k k^T E, k_i h_ij - k_j tr h = -4 k_j psi",
)
reduced = sp.expand(probe.leg[0]["n"] * (metric * momentum - momentum * metric.trace()).dot(
    metric * momentum - momentum * metric.trace()))
check(
    "scalar Vn",
    sp.expand(reduced - 16 * probe.leg[0]["n"] * psi**2 * momentum.dot(momentum)) == 0,
    "n |k_i h_ij - k_j tr h|^2 = 16 n psi^2 k^2 on a scalar configuration",
)

print("counting scalar rotation-invariant classes", flush=True)
scalar = probe.classify()
print(scalar, flush=True)
check(
    "scalar classes",
    scalar["union"] == scalar["consistent"] and scalar["classes"] == 4 and scalar["strict"] == 0,
    f"consistent {scalar['consistent']}, redefinitions {scalar['redefinitions']}, classes {scalar['classes']}, strict {scalar['strict']}",
)

print("counting full rotation-invariant classes", flush=True)
full = Problem("full").classify()
print(full, flush=True)
check(
    "full classes",
    full["union"] == full["consistent"] and full["classes"] == 1 and full["strict"] == 0,
    f"consistent {full['consistent']}, redefinitions {full['redefinitions']}, classes {full['classes']}, strict {full['strict']}",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL in the rotation-invariant scalar sector the first-order problem has 4 classes and none is strictly invariant. "
        "On a scalar configuration k_i h_ij - k_j tr h = -4 k_j psi, so n times that square is 16 n psi^2 k^2. "
        "With all configurations allowed there is exactly 1 class. "
        "The cubic-symmetric counts, the identification of that class with the comparator, and the lattice lift were not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - the scalar-sector restriction is not selective. "
        "It has 4 rotation-invariant first-order classes, while the unrestricted rotation-invariant problem has 1.",
        flush=True,
    )
