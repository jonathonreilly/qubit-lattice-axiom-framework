"""Exact checks: the formation law of a product-class nearest-neighbor rule is fixed by the multiset of recorded-neighbour sets of size at least two, with the order census on the 2x3 rectangle and the 2x2x2 cube.

Scope.  Six-projector menu inside M_2(C); covariant positive product rules with
orbit weights (p, q, r) on parallel, antiparallel and orthogonal pairs; the
finite windows path3, P4, star4, cycle4, the 2x3 rectangle and the open 2x2x2
cube.  For every formation order the formation law equals the static weight
divided by a product of one-site normalizers, and that product depends on the
order only through the multiset of recorded-neighbour sets of size at least two
(the in-neighbourhoods of the acyclic orientation the order induces).  Executed:
the census of acyclic orientations, multisets and distinct laws over all orders;
the uniform order mixture against the static law and the monotone-box law; the
class-(P) adjacent-exchange census; the binary Ising-type witness numbers of the
concurrent formation-order-covariance note re-derived along this path.  Exact
integers and rationals throughout.  No order is selected as physical.
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
CLAIM_ID = "admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13"
CLASSIFICATION_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
CLASSIFICATION_FRAGMENT = "FORMATION law of a rule for a formation order"
MONOTONE_CLAIM_ID = "admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07"
MONOTONE_FRAGMENT = "every linear extension of the product partial order"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
    "records are permanent",
)

MUTATION_GATE = {
    "projector_not_idempotent": "B",
    "pair_census_forged": "B",
    "rotation_not_transitive": "B",
    "cube_edge_dropped": "B",
    "acyclic_count_forged": "B",
    "order_orientation_forged": "B",
    "monotone_extension_count_forged": "B",
    "lemma_normalizer_dropped": "C",
    "one_neighbour_normalizer_varies": "C",
    "tree_partition_identity_broken": "C",
    "static_partition_forged": "C",
    "census_key_keeps_singletons": "D",
    "law_count_forged": "D",
    "mixture_weights_uniform_over_multisets": "D",
    "monotone_uses_upper_neighbours": "D",
    "cube_census_forged": "D",
    "spread_zero_claimed": "D",
    "exchange_holds_claimed": "D",
    "constant_rule_defect_claimed": "D",
    "rect_distance_forged": "D",
    "binary_coupling_forged": "E",
    "ends_first_order_forged": "E",
    "opposite_corners_forged": "E",
    "corners_first_forged": "E",
    "binary_law_count_forged": "E",
    "claim_all_orders_same_law": "F",
    "claim_order_selected": "F",
    "claim_mixture_is_law": "F",
    "float_literal_present": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.passed += 1
            print(f"PASS: {label} {detail}".rstrip())
        else:
            self.failed += 1
            self.failed_families.add(label[0])
            print(f"FAIL: {label} {detail}".rstrip())

    def finish(self) -> bool:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed == 0


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def dec(x: Fraction, digits: int = 12) -> str:
    sign = "-" if x < 0 else ""
    x = abs(x)
    whole = x.numerator // x.denominator
    rem = x - whole
    scaled = (rem.numerator * 10 ** digits) // rem.denominator
    return sign + str(whole) + "." + str(scaled).rjust(digits, "0")


def show(x) -> str:
    if isinstance(x, Fraction):
        text = f"{x.numerator}/{x.denominator}"
        return text if len(text) <= 28 else dec(x)
    return str(x)


# ---------------------------------------------------------------- menu (rebuilt)

MENU_VECTORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
M = 6
TRIPLES = ((3, 1, 2), (5, 2, 4))
CONSTANT = (2, 2, 2)
BINARY_PHI = ((4, 1), (1, 4))


def orbit(a: int, b: int) -> int:
    dot = sum(x * y for x, y in zip(MENU_VECTORS[a], MENU_VECTORS[b]))
    return 0 if dot == 1 else (1 if dot == -1 else 2)


def phi_table(triple):
    return tuple(tuple(triple[orbit(a, b)] for b in range(M)) for a in range(M))


def cx(re_part, im_part=0):
    return (Fraction(re_part), Fraction(im_part))


def cadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def cmul(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def cscale(u, s):
    return (u[0] * s, u[1] * s)


def cconj(u):
    return (u[0], -u[1])


def mmul(A, B):
    return tuple(tuple(cadd(cmul(A[i][0], B[0][j]), cmul(A[i][1], B[1][j])) for j in range(2)) for i in range(2))


def madj(A):
    return tuple(tuple(cconj(A[j][i]) for j in range(2)) for i in range(2))


def mtrace(A):
    return cadd(A[0][0], A[1][1])


ZERO = cx(0)
ONE = cx(1)
SIGMA = (
    ((ZERO, ONE), (ONE, ZERO)),
    ((ZERO, cx(0, -1)), (cx(0, 1), ZERO)),
    ((ONE, ZERO), (ZERO, cx(-1))),
)
IDENT = ((ONE, ZERO), (ZERO, ONE))


def projector(k: int, stretch: int = 1):
    axis = k // 2
    sign = 1 if k % 2 == 0 else -1
    half = Fraction(1, 2)
    return tuple(
        tuple(cscale(cadd(IDENT[i][j], cscale(SIGMA[axis][i][j], sign * stretch)), half) for j in range(2))
        for i in range(2)
    )


def signed_permutations():
    rotations = []
    for perm in permutations(range(3)):
        parity = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if perm[i] > perm[j]:
                    parity = -parity
        for signs in product((1, -1), repeat=3):
            det = parity * signs[0] * signs[1] * signs[2]
            if det == 1:
                rotations.append((perm, signs))
    return tuple(rotations)


def rotate_index(rotation, k: int) -> int:
    perm, signs = rotation
    vec = MENU_VECTORS[k]
    image = [0, 0, 0]
    for i in range(3):
        image[perm[i]] = signs[i] * vec[i]
    return MENU_VECTORS.index(tuple(image))


# ---------------------------------------------------------------- windows and orders

def grid_window(shape):
    sites = list(product(*(range(d) for d in shape)))
    index = {site: i for i, site in enumerate(sites)}
    edges = []
    for site in sites:
        for axis in range(len(shape)):
            step = list(site)
            step[axis] += 1
            other = tuple(step)
            if other in index:
                edges.append((index[site], index[other]))
    return len(sites), tuple(edges)


WINDOWS = {
    "path3": (3, ((0, 1), (1, 2))),
    "P4": (4, ((0, 1), (1, 2), (2, 3))),
    "star4": (4, ((0, 1), (0, 2), (0, 3))),
    "cycle4": (4, ((0, 1), (1, 2), (2, 3), (3, 0))),
    "rect": grid_window((2, 3)),
    "cube": grid_window((2, 2, 2)),
}
SMALL = ("path3", "P4", "star4", "cycle4")


def neighbours(n, edges):
    nbhd = [[] for _ in range(n)]
    for x, y in edges:
        nbhd[x].append(y)
        nbhd[y].append(x)
    return tuple(tuple(a) for a in nbhd)


def is_acyclic(n, edges, orientation) -> bool:
    indeg = [0] * n
    out = [[] for _ in range(n)]
    for (x, y), forward in zip(edges, orientation):
        s, t = (x, y) if forward else (y, x)
        out[s].append(t)
        indeg[t] += 1
    stack = [x for x in range(n) if indeg[x] == 0]
    seen = 0
    while stack:
        x = stack.pop()
        seen += 1
        for t in out[x]:
            indeg[t] -= 1
            if indeg[t] == 0:
                stack.append(t)
    return seen == n


def acyclic_orientations(n, edges):
    return frozenset(o for o in product((False, True), repeat=len(edges)) if is_acyclic(n, edges, o))


def orientation_of_order(order, edges):
    pos = {x: k for k, x in enumerate(order)}
    return tuple(pos[x] < pos[y] for x, y in edges)


def in_sets(n, edges, orientation):
    ins = [[] for _ in range(n)]
    for (x, y), forward in zip(edges, orientation):
        s, t = (x, y) if forward else (y, x)
        ins[t].append(s)
    return tuple(tuple(sorted(a)) for a in ins)


def multiset_key(ins, minimum: int = 2):
    return tuple(sorted(a for a in ins if len(a) >= minimum))


def order_census(n, edges, minimum: int = 2):
    """Multiset key -> number of orders; the set of induced orientations; the census of the largest recorded set."""
    keys: Counter = Counter()
    orientations = set()
    largest: Counter = Counter()
    for order in permutations(range(n)):
        o = orientation_of_order(order, edges)
        orientations.add(o)
        ins = in_sets(n, edges, o)
        keys[multiset_key(ins, minimum)] += 1
        largest[max(len(a) for a in ins)] += 1
    return keys, frozenset(orientations), largest


def key_of_order(order, n, edges, minimum: int = 2):
    return multiset_key(in_sets(n, edges, orientation_of_order(order, edges)), minimum)


# ---------------------------------------------------------------- product rules

class ProductRule:
    def __init__(self, phi) -> None:
        self.phi = phi
        self.size = len(phi)
        self.z_one = tuple(sum(phi[s][a] for s in range(self.size)) for a in range(self.size))
        self.tables: dict = {}

    def table(self, k: int) -> dict:
        got = self.tables.get(k)
        if got is None:
            got = {}
            for vals in product(range(self.size), repeat=k):
                total = 0
                for s in range(self.size):
                    w = 1
                    for a in vals:
                        w *= self.phi[s][a]
                    total += w
                got[vals] = total
            self.tables[k] = got
        return got

    def zed(self, values) -> int:
        return self.table(len(values))[values]

    def weight(self, edges, v) -> int:
        w = 1
        for x, y in edges:
            w *= self.phi[v[x]][v[y]]
        return w

    def chain_law(self, n, edges, order, v) -> Fraction:
        """Reference path: the chain of the rule's conditionals along the order, conditioning on records only."""
        nbhd = neighbours(n, edges)
        formed: set = set()
        p = Fraction(1)
        for x in order:
            vals = tuple(v[y] for y in nbhd[x] if y in formed)
            num = 1
            for a in vals:
                num *= self.phi[v[x]][a]
            p *= Fraction(num, self.zed(vals))
            formed.add(x)
        return p

    def compile_key(self, n, edges, key):
        a1 = len(edges) - sum(len(a) for a in key)
        a0 = n - a1 - len(key)
        const = self.size ** a0 * self.z_one[0] ** a1
        return (const, tuple((self.table(len(a)), a) for a in key))

    def evaluate(self, compiled, v) -> int:
        e = compiled[0]
        for table, a in compiled[1]:
            e *= table[tuple(v[y] for y in a)]
        return e

    def denominator(self, n, edges, key, v) -> int:
        return self.evaluate(self.compile_key(n, edges, key), v)

    def law(self, n, edges, key, configs) -> dict:
        compiled = self.compile_key(n, edges, key)
        return {v: Fraction(self.weight(edges, v), self.evaluate(compiled, v)) for v in configs}

    def static_law(self, n, edges, configs) -> dict:
        weights = {v: self.weight(edges, v) for v in configs}
        total = sum(weights.values())
        return {v: Fraction(w, total) for v, w in weights.items()}


def total_variation(a: dict, b: dict) -> Fraction:
    return sum(abs(a[v] - b[v]) for v in a) / 2


def differing_cells(a: dict, b: dict) -> int:
    return sum(1 for v in a if a[v] != b[v])


def configuration_family(n: int, size: int, draws: int = 300, seed: int = 20260913):
    reference = (0,) * n
    fam = [reference]
    for x in range(n):
        for a in range(1, size):
            v = list(reference)
            v[x] = a
            fam.append(tuple(v))
    for x in range(n):
        for y in range(x + 1, n):
            for a in range(1, size):
                for b in range(1, size):
                    v = list(reference)
                    v[x] = a
                    v[y] = b
                    fam.append(tuple(v))
    state = seed
    for _ in range(draws):
        v = []
        for _ in range(n):
            state = (1103515245 * state + 12345) % 2 ** 31
            v.append((state >> 16) % size)
        fam.append(tuple(v))
    return tuple(dict.fromkeys(fam))


def window_pass(rule: ProductRule, n, edges, keys):
    """All configurations of a window: static weight accumulated by the tuple of every key's denominator, with the largest weight per tuple."""
    compiled = [rule.compile_key(n, edges, k) for k in keys]
    acc: dict = defaultdict(int)
    top: dict = {}
    for v in product(range(rule.size), repeat=n):
        w = rule.weight(edges, v)
        t = tuple(rule.evaluate(c, v) for c in compiled)
        acc[t] += w
        if w > top.get(t, 0):
            top[t] = w
    return acc, top


def analyse_pass(acc, top, keys, counts, index_monotone, factorial):
    """Exact statistics from an accumulated pass: normalization per key, distinct laws, distances of the mixture, monotone and static laws."""
    total = sum(acc.values())
    inv_total = Fraction(1, total)
    tv_static = []
    norms = []
    for i in range(len(keys)):
        by_e: dict = defaultdict(int)
        for t, w in acc.items():
            by_e[t[i]] += w
        norms.append(sum(Fraction(w, e) for e, w in by_e.items()))
        tv_static.append(sum(w * abs(Fraction(1, e) - inv_total) for e, w in by_e.items()) / 2)
    signatures = set()
    tuples = list(acc)
    for i in range(len(keys)):
        signatures.add(tuple(t[i] for t in tuples))
    weights = [Fraction(counts[k], factorial) for k in keys]
    tv_mix_static = Fraction(0)
    tv_mix_mono = Fraction(0)
    gap_mix_static = Fraction(0)
    for t, w in acc.items():
        mix = sum(c / e for c, e in zip(weights, t))
        tv_mix_static += w * abs(mix - inv_total)
        tv_mix_mono += w * abs(mix - Fraction(1, t[index_monotone]))
        gap = top[t] * abs(mix - inv_total)
        if gap > gap_mix_static:
            gap_mix_static = gap
    return {
        "total": total,
        "norms": norms,
        "law_count": len(signatures),
        "tv_static": tv_static,
        "tv_mono_static": tv_static[index_monotone],
        "tv_mix_static": tv_mix_static / 2,
        "tv_mix_mono": tv_mix_mono / 2,
        "gap_mix_static": gap_mix_static,
        "spread": max(tv_static),
    }


def group_keys_on_family(rule: ProductRule, n, edges, keys, fam):
    groups: dict = defaultdict(list)
    for key in keys:
        compiled = rule.compile_key(n, edges, key)
        groups[tuple(rule.evaluate(compiled, v) for v in fam)].append(key)
    return groups


def cube_pass(rule: ProductRule, n, edges, key_forward, key_reverse, ambiguous):
    """One pass over every cube configuration: partition function, static weight by (forward, reverse) denominators, and separation of key groups that coincide on the family."""
    fwd = rule.compile_key(n, edges, key_forward)
    rev = rule.compile_key(n, edges, key_reverse)
    parts = [[(rule.compile_key(n, edges, k), k) for k in group] for group in ambiguous]
    total = 0
    acc: dict = defaultdict(int)
    for v in product(range(rule.size), repeat=n):
        w = rule.weight(edges, v)
        total += w
        acc[(rule.evaluate(fwd, v), rule.evaluate(rev, v))] += w
        if parts:
            refined = []
            for part in parts:
                if len(part) == 1:
                    refined.append(part)
                    continue
                sub: dict = defaultdict(list)
                for item in part:
                    sub[rule.evaluate(item[0], v)].append(item)
                refined.extend(sub.values())
            parts = refined
            if all(len(part) == 1 for part in parts):
                parts = []
    return total, acc, parts


def cube_partition_by_contraction(rule: ProductRule) -> int:
    """Face-by-face contraction: the x = 0 face weight times the trace of the x = 1 face transfer product with the four vertical couplings as site fields."""
    phi = rule.phi
    size = rule.size
    cycle = (0, 1, 3, 2)

    def face_weight(a):
        return phi[a[0]][a[1]] * phi[a[1]][a[3]] * phi[a[3]][a[2]] * phi[a[2]][a[0]]

    def matmul(A, B):
        return [[sum(A[s][u] * B[u][t] for u in range(size)) for t in range(size)] for s in range(size)]

    total = 0
    for a in product(range(size), repeat=4):
        prod_matrix = None
        for i in cycle:
            mtx = [[phi[a[i]][s] * phi[s][t] for t in range(size)] for s in range(size)]
            prod_matrix = mtx if prod_matrix is None else matmul(prod_matrix, mtx)
        total += face_weight(a) * sum(prod_matrix[s][s] for s in range(size))
    return total


def exchange_census(rule: ProductRule, max_background: int = 2):
    """For backgrounds of i and j extra recorded neighbours at two adjacent consecutive sites, count value assignments where Z(eta_x) Z(eta_y + a) differs from Z(eta_y) Z(eta_x + b)."""
    result = {}
    for i in range(max_background + 1):
        for j in range(max_background + 1):
            fails = 0
            total = 0
            for eta_x in product(range(rule.size), repeat=i):
                for eta_y in product(range(rule.size), repeat=j):
                    for a in range(rule.size):
                        for b in range(rule.size):
                            total += 1
                            left = rule.zed(eta_x) * rule.zed(eta_y + (a,))
                            right = rule.zed(eta_y) * rule.zed(eta_x + (b,))
                            if left != right:
                                fails += 1
            result[(i, j)] = (fails, total)
    return result


# ---------------------------------------------------------------- expected values (filled from the first exact run)

EXPECTED = {
    "acyclic": {"path3": 4, "P4": 8, "star4": 8, "cycle4": 14, "rect": 98, "cube": 1862},
    "extensions": {"rect": 5, "cube": 48},
    "equal_orders": {"path3": 4, "P4": 8, "star4": 12, "cycle4": 0},
    "class_sizes": {"path3": (4, 2), "P4": (8, 8, 8), "star4": (12, 6, 2, 2, 2), "cycle4": (8, 8, 4, 4)},
    "e5": {(3, 1, 2): Fraction(899, 2341664), (5, 2, 4): Fraction(3478458125, 23066700436908)},
    "rect_multisets": 28,
    "rect_laws": (28, 28),
    "rect_monotone_orders": 48,
    "rect_tv_mono_static": {(3, 1, 2): Fraction(166597, 6750000), (5, 2, 4): Fraction(18031280990, 1152766563947)},
    "rect_tv_mix_static": {(3, 1, 2): Fraction(372254646387017, 12790481418000000), (5, 2, 4): Fraction(6628058424854510226272127920221, 381356895652498781589963821562900)},
    "rect_tv_mix_mono": {(3, 1, 2): Fraction(44446481797, 2046477026880), (5, 2, 4): Fraction(201171497997761809454557, 14788697255605118189282400)},
    "rect_gap_mix_static": {(3, 1, 2): Fraction(8535587, 105456000000), (5, 2, 4): Fraction(75088901087821671875, 3583863012400439488911216)},
    "rect_spread": {(3, 1, 2): Fraction(16549, 281250), (5, 2, 4): Fraction(125508731, 3410832276)},
    "cube_multisets": 542,
    "cube_laws": {(3, 1, 2): 542, (5, 2, 4): 542},
    "cube_monotone_orders": 120,
    "cube_forward_key": ((1, 2), (1, 4), (2, 4), (3, 5, 6)),
    "cube_reverse_key": ((1, 2, 4), (3, 5), (3, 6), (5, 6)),
    "cube_tv_mono_static": {(3, 1, 2): Fraction(1182193085, 23402354976), (5, 2, 4): Fraction(180429904845630987241, 6061376968596116197338)},
    "cube_tv_mono_reverse": {(3, 1, 2): Fraction(8207, 7830108), (5, 2, 4): Fraction(78076639367, 38683213526034)},
    "cube_gap_mix_static": {(3, 1, 2): Fraction(468324690921, 13849151214080000), (5, 2, 4): Fraction(1083259980382858024033073095703125, 238113505325368709377379573647456927296)},
    "cube_gap_mix_mono": {(3, 1, 2): Fraction(3230469, 511813120000), (5, 2, 4): Fraction(221362490334912109375, 252089923069262577014315712)},
    "binary_cycle_cells": 16,
}

N5_LINES = (
    "per_element: executed — projector, pair, rotation and window checks on the declared menu and windows",
    "per_site: executed — one-site normalizers and recorded-neighbour sets for every site of every window",
    "per_mode: executed — every formation order of every declared window; every acyclic orientation",
    "per_block: executed — census, mixture, monotone-box and exchange results per window and triple",
    "lattice_wide: not claimed — no infinite-volume statement, no rule, order or reading selected",
)


def expect(checks: Checks, label: str, value, target) -> None:
    if target is None:
        checks.check(label, False, f"unset; computed {value!r}")
    else:
        checks.check(label, value == target, show(value))


# ---------------------------------------------------------------- shared exact computations (pure)

def compute_shared() -> dict:
    shared: dict = {"census": {}, "acyclic": {}}
    for name, (n, edges) in WINDOWS.items():
        shared["census"][name] = order_census(n, edges)
        shared["acyclic"][name] = acyclic_orientations(n, edges)
    shared["rules"] = {t: ProductRule(phi_table(t)) for t in TRIPLES}
    shared["constant"] = ProductRule(phi_table(CONSTANT))
    shared["binary"] = ProductRule(BINARY_PHI)
    n_rect, e_rect = WINDOWS["rect"]
    n_cube, e_cube = WINDOWS["cube"]
    shared["rect_forward"] = key_of_order(tuple(range(n_rect)), n_rect, e_rect)
    shared["rect_reverse"] = key_of_order(tuple(reversed(range(n_rect))), n_rect, e_rect)
    shared["cube_forward"] = key_of_order((0, 1, 2, 4, 3, 5, 6, 7), n_cube, e_cube)
    shared["cube_reverse"] = key_of_order((7, 6, 5, 3, 4, 2, 1, 0), n_cube, e_cube)
    shared["family_rect"] = configuration_family(n_rect, M)
    shared["family_cube"] = configuration_family(n_cube, M)
    rect_keys = sorted(shared["census"]["rect"][0])
    shared["rect_keys"] = rect_keys
    shared["rect"] = {}
    for t, rule in shared["rules"].items():
        acc, top = window_pass(rule, n_rect, e_rect, rect_keys)
        shared["rect"][t] = analyse_pass(acc, top, rect_keys, shared["census"]["rect"][0], rect_keys.index(shared["rect_forward"]), 720)
    cube_keys = sorted(shared["census"]["cube"][0])
    shared["cube_keys"] = cube_keys
    shared["cube"] = {}
    for t, rule in shared["rules"].items():
        groups = group_keys_on_family(rule, n_cube, e_cube, cube_keys, shared["family_cube"])
        ambiguous = [g for g in groups.values() if len(g) > 1]
        total, acc, parts = cube_pass(rule, n_cube, e_cube, shared["cube_forward"], shared["cube_reverse"], ambiguous)
        extra = sum(len(part) - 1 for part in parts)
        shared["cube"][t] = {
            "total": total,
            "acc": acc,
            "groups": len(groups),
            "ambiguous": len(ambiguous),
            "unresolved": extra,
            "law_count": len(groups) + sum(len(g) - 1 for g in ambiguous) - extra,
            "contraction": cube_partition_by_contraction(rule),
        }
    return shared


# ---------------------------------------------------------------- families

def family_a(checks: Checks, note_text: str, axiom_text: str, classification_text: str, monotone_text: str) -> None:
    checks.check("A1 note carries its claim id", CLAIM_ID in note_text)
    axiom_norm = normalize_text(axiom_text)
    missing = [needle for needle in AXIOM_NEEDLES if normalize_text(needle) not in axiom_norm]
    checks.check("A2 axiom sentences quoted verbatim", not missing, f"needles {len(AXIOM_NEEDLES)} missing {len(missing)}")
    classification_norm = normalize_text(classification_text)
    checks.check("A3 classification parent present", CLASSIFICATION_CLAIM_ID in classification_text and CLASSIFICATION_FRAGMENT in classification_norm)
    monotone_norm = normalize_text(monotone_text)
    checks.check("A4 monotone parent present", MONOTONE_CLAIM_ID in monotone_text and MONOTONE_FRAGMENT in monotone_norm)


def family_b(checks: Checks, shared: dict) -> None:
    stretch = 2 if mut("projector_not_idempotent") else 1
    projectors = [projector(k, stretch) for k in range(M)]
    good = True
    for P in projectors:
        idem = mmul(P, P) == P
        herm = madj(P) == P
        good = good and idem and herm and mtrace(P) == ONE
    checks.check("B1 six projectors Hermitian idempotent trace one", good)
    census: Counter = Counter()
    agree = True
    for a in range(M):
        for b in range(M):
            tr = mtrace(mmul(projectors[a], projectors[b]))
            census[tr] += 1
            expected_tr = {0: ONE, 1: ZERO, 2: cx(Fraction(1, 2))}[orbit(a, b)]
            agree = agree and tr == expected_tr
    target = (5, 7, 24) if mut("pair_census_forged") else (6, 6, 24)
    counts = (census[ONE], census[ZERO], census[cx(Fraction(1, 2))])
    checks.check("B2 pair census parallel/antiparallel/orthogonal", counts == target and agree, f"{counts}")
    rotations = signed_permutations()
    if mut("rotation_not_transitive"):
        rotations = tuple(r for r in rotations if r[0] == (0, 1, 2))
    images = {rotate_index(r, 0) for r in rotations}
    preserving = all(orbit(rotate_index(r, a), rotate_index(r, b)) == orbit(a, b) for r in rotations for a in range(M) for b in range(M))
    checks.check("B3 24 proper rotations transitive orbit-preserving", len(rotations) == 24 and len(images) == M and preserving, f"count {len(rotations)} images {len(images)}")
    n_cube, e_cube = grid_window((2, 2, 2))
    if mut("cube_edge_dropped"):
        e_cube = e_cube[:-1]
    degrees = Counter()
    for x, y in e_cube:
        degrees[x] += 1
        degrees[y] += 1
    bitflip = all(bin(x ^ y).count("1") == 1 for x, y in e_cube)
    n_rect, e_rect = grid_window((2, 3))
    rect_ok = n_rect == 6 and set(e_rect) == {(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)}
    checks.check("B4 windows: cube 8 sites 12 bit-flip edges degree 3; rect 6 sites 7 edges", n_cube == 8 and len(e_cube) == 12 and set(degrees.values()) == {3} and bitflip and rect_ok, f"cube edges {len(e_cube)}")
    counts_ok = True
    sets_ok = True
    summary = []
    for name in WINDOWS:
        induced = set(shared["census"][name][1])
        if mut("order_orientation_forged") and name == "cycle4":
            some = next(iter(induced))
            induced.discard(some)
            induced.add(tuple(not b for b in some[:1]) + some[1:])
        acyclic = shared["acyclic"][name]
        sets_ok = sets_ok and induced == set(acyclic)
        target = EXPECTED["acyclic"][name]
        if mut("acyclic_count_forged") and name == "rect" and target is not None:
            target += 1
        counts_ok = counts_ok and target is not None and len(acyclic) == target
        summary.append(f"{name} {len(acyclic)}")
    checks.check("B5 acyclic orientations = order-induced orientations", sets_ok and counts_ok, "; ".join(summary))
    ext = {}
    for name in ("rect", "cube"):
        n, edges = WINDOWS[name]
        forward = tuple(True for _ in edges)
        ext[name] = sum(1 for order in permutations(range(n)) if orientation_of_order(order, edges) == forward)
    target = dict(EXPECTED["extensions"])
    if mut("monotone_extension_count_forged"):
        target["rect"] += 1
    checks.check("B6 linear extensions of the product order", ext == target, f"rect {ext['rect']} cube {ext['cube']}")
    largest = shared["census"]["cube"][2]
    checks.check("B7 every cube order has largest recorded set 3", dict(largest) == {3: 40320}, f"{dict(largest)}")


def family_c(checks: Checks, shared: dict) -> None:
    ok = True
    detail = []
    for t, rule in shared["rules"].items():
        z_one = list(rule.z_one)
        if mut("one_neighbour_normalizer_varies"):
            z_one[3] += 1
        ok = ok and set(z_one) == {t[0] + t[1] + 4 * t[2]}
        detail.append(f"{t}:{z_one[0]}")
    ok = ok and set(shared["binary"].z_one) == {5}
    checks.check("C1 one-neighbour normalizer constant p+q+4r; binary 5", ok, " ".join(detail))
    mismatches = 0
    evaluated = 0
    for name in SMALL:
        n, edges = WINDOWS[name]
        configs = list(product(range(M), repeat=n))
        for rule in shared["rules"].values():
            for order in permutations(range(n)):
                key = key_of_order(order, n, edges)
                if mut("lemma_normalizer_dropped"):
                    key = ()
                law = rule.law(n, edges, key, configs)
                for v in configs:
                    evaluated += 1
                    if rule.chain_law(n, edges, order, v) != law[v]:
                        mismatches += 1
    n_rect, e_rect = WINDOWS["rect"]
    small_family = configuration_family(n_rect, M, draws=100)[:1 + 30 + 100]
    for rule in shared["rules"].values():
        for order in permutations(range(n_rect)):
            key = key_of_order(order, n_rect, e_rect)
            compiled = rule.compile_key(n_rect, e_rect, key)
            for v in small_family:
                evaluated += 1
                if rule.chain_law(n_rect, e_rect, order, v) != Fraction(rule.weight(e_rect, v), rule.evaluate(compiled, v)):
                    mismatches += 1
    binary = shared["binary"]
    for name in ("cycle4", "rect"):
        n, edges = WINDOWS[name]
        configs = list(product(range(2), repeat=n))
        for order in permutations(range(n)):
            law = binary.law(n, edges, key_of_order(order, n, edges), configs)
            for v in configs:
                evaluated += 1
                if binary.chain_law(n, edges, order, v) != law[v]:
                    mismatches += 1
    checks.check("C2 chain law = static weight / multiset denominator", mismatches == 0, f"evaluated {evaluated} mismatches {mismatches}")
    norm_ok = True
    for name in SMALL:
        n, edges = WINDOWS[name]
        configs = list(product(range(M), repeat=n))
        for rule in shared["rules"].values():
            for key in shared["census"][name][0]:
                norm_ok = norm_ok and sum(rule.law(n, edges, key, configs).values()) == 1
    for t in TRIPLES:
        norm_ok = norm_ok and all(x == 1 for x in shared["rect"][t]["norms"])
    checks.check("C3 every multiset law sums to one (small windows, rect)", norm_ok)
    tree_ok = True
    equal_ok = True
    detail = []
    for name in SMALL:
        n, edges = WINDOWS[name]
        configs = list(product(range(M), repeat=n))
        for rule in shared["rules"].values():
            total = sum(rule.weight(edges, v) for v in configs)
            if name != "cycle4":
                target = M * rule.z_one[0] ** (n - 1 + (1 if mut("tree_partition_identity_broken") else 0))
                tree_ok = tree_ok and total == target
        equal = shared["census"][name][0].get((), 0)
        equal_ok = equal_ok and equal == EXPECTED["equal_orders"][name]
        detail.append(f"{name} {equal}")
    checks.check("C4 tree partition function M*Z1^(n-1); orders equal to static", tree_ok and equal_ok, "; ".join(detail))
    contraction_ok = True
    for t in TRIPLES:
        block = shared["cube"][t]
        forged = 1 if mut("static_partition_forged") else 0
        contraction_ok = contraction_ok and block["contraction"] + forged == block["total"]
    checks.check("C5 cube partition function: contraction = full pass", contraction_ok, f"Z(3,1,2)={shared['cube'][(3, 1, 2)]['total']}")


def family_d(checks: Checks, shared: dict) -> None:
    minimum = 1 if mut("census_key_keeps_singletons") else 2
    class_ok = True
    detail = []
    for name in SMALL:
        n, edges = WINDOWS[name]
        configs = list(product(range(M), repeat=n))
        keys, _, _ = order_census(n, edges, minimum)
        for rule in shared["rules"].values():
            laws: dict = defaultdict(int)
            for key, count in keys.items():
                laws[tuple(sorted(rule.law(n, edges, key, configs).items()))] += count
            sizes = tuple(sorted(laws.values(), reverse=True))
            class_ok = class_ok and sizes == EXPECTED["class_sizes"][name] and len(laws) == len(keys)
        detail.append(f"{name} {len(keys)}")
    checks.check("D1 census on path3/P4/star4/cycle4 = (4,2) (8,8,8) (12,6,2,2,2) (8,8,4,4)", class_ok, "; ".join(detail))
    n4, e4 = WINDOWS["cycle4"]
    configs4 = list(product(range(M), repeat=n4))
    keys4, _, _ = order_census(n4, e4, minimum)
    e5_ok = True
    detail = []
    for t, rule in shared["rules"].items():
        static = rule.static_law(n4, e4, configs4)
        mixture = {v: Fraction(0) for v in configs4}
        for key, count in keys4.items():
            weight = Fraction(1, len(keys4)) if mut("mixture_weights_uniform_over_multisets") else Fraction(count, 24)
            law = rule.law(n4, e4, key, configs4)
            for v in configs4:
                mixture[v] += weight * law[v]
        gap = max(abs(mixture[v] - static[v]) for v in configs4)
        e5_ok = e5_ok and gap == EXPECTED["e5"][t]
        detail.append(show(gap))
    checks.check("D2 cycle4 uniform order mixture gap reproduces E5", e5_ok, " ".join(detail))
    n_rect, e_rect = WINDOWS["rect"]
    rect_keys, _, _ = order_census(n_rect, e_rect, minimum)
    rect_counts = shared["census"]["rect"][0]
    forward = shared["rect_forward"]
    expect(checks, "D3 rect: multisets over 720 orders", len(rect_keys), EXPECTED["rect_multisets"])
    law_counts = tuple(shared["rect"][t]["law_count"] for t in TRIPLES)
    target = EXPECTED["rect_laws"]
    if mut("law_count_forged") and target is not None:
        target = tuple(x + 1 for x in target)
    expect(checks, "D4 rect: distinct laws at (3,1,2),(5,2,4) = multisets", law_counts, target)
    checks.check("D5 rect: forward and reverse orders share a multiset", forward == shared["rect_reverse"] and len(rect_keys) == law_counts[0] == law_counts[1], f"{forward}")
    expect(checks, "D6 rect: orders in the monotone-box class", rect_counts[forward], EXPECTED["rect_monotone_orders"])
    for t in TRIPLES:
        block = shared["rect"][t]
        tv = block["tv_mono_static"]
        target = EXPECTED["rect_tv_mono_static"][t]
        if mut("rect_distance_forged") and target is not None:
            target = target + 1
        expect(checks, f"D7 rect TV(mono,static) {t}", tv, target)
        expect(checks, f"D8 rect TV(mix,static) {t}", block["tv_mix_static"], EXPECTED["rect_tv_mix_static"][t])
        expect(checks, f"D9 rect TV(mix,mono) {t}", block["tv_mix_mono"], EXPECTED["rect_tv_mix_mono"][t])
        expect(checks, f"D10 rect max|mix-static| {t}", block["gap_mix_static"], EXPECTED["rect_gap_mix_static"][t])
        spread = block["spread"]
        spread_ok = spread == 0 if mut("spread_zero_claimed") else spread > 0
        expect(checks, f"D11 rect spread max_m TV(m,static) {t}", spread if spread_ok else None, EXPECTED["rect_spread"][t])
    constant = shared["constant"]
    const_ok = all(len(set(constant.table(k).values())) == 1 for k in (1, 2, 3))
    const_groups = group_keys_on_family(constant, n_rect, e_rect, sorted(rect_keys), shared["family_rect"])
    const_laws = 2 if mut("constant_rule_defect_claimed") else 1
    checks.check("D12 constant rule: normalizer tables constant, one law on rect and cube", const_ok and len(const_groups) == const_laws, f"groups {len(const_groups)}")
    n_cube, e_cube = WINDOWS["cube"]
    cube_keys, _, _ = order_census(n_cube, e_cube, minimum)
    cube_counts = shared["census"]["cube"][0]
    target = EXPECTED["cube_multisets"]
    if mut("cube_census_forged") and target is not None:
        target += 1
    expect(checks, "D13 cube: multisets over 40320 orders", len(cube_keys), target)
    cube_laws = tuple(shared["cube"][t]["law_count"] for t in TRIPLES)
    unresolved = sum(shared["cube"][t]["unresolved"] for t in TRIPLES)
    ambiguous = tuple(shared["cube"][t]["ambiguous"] for t in TRIPLES)
    expect(checks, "D14 cube: distinct laws at (3,1,2),(5,2,4)", cube_laws if unresolved == 0 else None, tuple(EXPECTED["cube_laws"][t] for t in TRIPLES))
    checks.check("D15 cube: family separates the multisets (groups needing the full pass)", unresolved == 0 and cube_laws == (len(cube_keys), len(cube_keys)), f"ambiguous {ambiguous}")
    fwd = shared["cube_reverse"] if mut("monotone_uses_upper_neighbours") else shared["cube_forward"]
    checks.check("D16 cube: monotone and reversed multisets as declared, distinct", fwd == EXPECTED["cube_forward_key"] and shared["cube_reverse"] == EXPECTED["cube_reverse_key"] and fwd != shared["cube_reverse"])
    expect(checks, "D17 cube: orders in the monotone-box class", cube_counts[shared["cube_forward"]], EXPECTED["cube_monotone_orders"])
    fam = shared["family_cube"]
    for t, rule in shared["rules"].items():
        block = shared["cube"][t]
        total = block["total"]
        inv_total = Fraction(1, total)
        tv_fs = Fraction(0)
        tv_rs = Fraction(0)
        tv_fr = Fraction(0)
        for (ef, er), w in block["acc"].items():
            tv_fs += w * abs(Fraction(1, ef) - inv_total)
            tv_rs += w * abs(Fraction(1, er) - inv_total)
            tv_fr += w * abs(Fraction(1, ef) - Fraction(1, er))
        tv_fs /= 2
        tv_rs /= 2
        tv_fr /= 2
        expect(checks, f"D18 cube TV(mono,static)=TV(rev,static) {t}", tv_fs if tv_fs == tv_rs and tv_fs > 0 else None, EXPECTED["cube_tv_mono_static"][t])
        expect(checks, f"D19 cube TV(mono,rev) {t}", tv_fr, EXPECTED["cube_tv_mono_reverse"][t])
        compiled = {key: rule.compile_key(n_cube, e_cube, key) for key in cube_counts}
        fwd_c = rule.compile_key(n_cube, e_cube, shared["cube_forward"])
        gap_static = Fraction(0)
        gap_mono = Fraction(0)
        for v in fam:
            w = rule.weight(e_cube, v)
            if mut("mixture_weights_uniform_over_multisets"):
                mix = sum(Fraction(1, len(cube_counts) * rule.evaluate(c, v)) for c in compiled.values())
            else:
                mix = sum(Fraction(cube_counts[key], 40320 * rule.evaluate(c, v)) for key, c in compiled.items())
            gap_static = max(gap_static, w * abs(mix - inv_total))
            gap_mono = max(gap_mono, w * abs(mix - Fraction(1, rule.evaluate(fwd_c, v))))
        expect(checks, f"D20 cube family max|mix-static| {t}", gap_static, EXPECTED["cube_gap_mix_static"][t])
        expect(checks, f"D21 cube family max|mix-mono| {t}", gap_mono, EXPECTED["cube_gap_mix_mono"][t])
    exch_ok = True
    detail = []
    for t, rule in shared["rules"].items():
        census = exchange_census(rule)
        if mut("exchange_holds_claimed"):
            exch_ok = exch_ok and all(census[b][0] == 0 for b in census)
        else:
            exch_ok = exch_ok and census[(0, 0)][0] == 0 and all(census[b][0] > 0 for b in census if b != (0, 0))
        detail.append(f"{t} (0,1):{census[(0, 1)][0]}/{census[(0, 1)][1]}")
    const_census = exchange_census(constant)
    exch_ok = exch_ok and all(f == 0 for f, _ in const_census.values())
    checks.check("D22 exchange identity holds only at empty backgrounds; constant rule everywhere", exch_ok, " ".join(detail))


def family_e(checks: Checks, shared: dict) -> None:
    rule = ProductRule(((3, 1), (1, 3)) if mut("binary_coupling_forged") else BINARY_PHI)
    n3, e3 = WINDOWS["path3"]
    configs3 = list(product(range(2), repeat=n3))
    chain = rule.law(n3, e3, key_of_order((0, 1, 2), n3, e3), configs3)
    ends = rule.law(n3, e3, key_of_order((1, 0, 2) if mut("ends_first_order_forged") else (0, 2, 1), n3, e3), configs3)
    tv = total_variation(chain, ends)
    checks.check("E1 binary path3 chain vs ends-first: TV 9/50, masses 8/25 vs 4/17, 8 cells", tv == Fraction(9, 50) and chain[(0, 0, 0)] == Fraction(8, 25) and ends[(0, 0, 0)] == Fraction(4, 17) and differing_cells(chain, ends) == 8, show(tv))
    n4, e4 = WINDOWS["cycle4"]
    configs4 = list(product(range(2), repeat=n4))
    laws: dict = defaultdict(int)
    for order in permutations(range(n4)):
        laws[tuple(sorted(rule.law(n4, e4, key_of_order(order, n4, e4), configs4).items()))] += 1
    cyclic = rule.law(n4, e4, key_of_order((0, 1, 2, 3), n4, e4), configs4)
    opposite = rule.law(n4, e4, key_of_order((0, 1, 2, 3) if mut("opposite_corners_forged") else (0, 2, 1, 3), n4, e4), configs4)
    tv = total_variation(cyclic, opposite)
    cells = differing_cells(cyclic, opposite)
    sizes = tuple(sorted(laws.values(), reverse=True))
    expect(checks, "E2 binary cycle4: laws (8,8,4,4); cyclic vs opposite TV 9/50; cells", cells if sizes == (8, 8, 4, 4) and tv == Fraction(9, 50) else None, EXPECTED["binary_cycle_cells"])
    n6, e6 = WINDOWS["rect"]
    configs6 = list(product(range(2), repeat=n6))
    laws = defaultdict(int)
    for order in permutations(range(n6)):
        laws[tuple(sorted(rule.law(n6, e6, key_of_order(order, n6, e6), configs6).items()))] += 1
    row_major = rule.law(n6, e6, key_of_order((0, 1, 2, 3, 4, 5), n6, e6), configs6)
    corners_order = (0, 1, 2, 3, 4, 5) if mut("corners_first_forged") else (0, 2, 3, 5, 1, 4)
    corners = rule.law(n6, e6, key_of_order(corners_order, n6, e6), configs6)
    reverse_key = key_of_order((5, 4, 3, 2, 1, 0), n6, e6)
    target = 27 if mut("binary_law_count_forged") else 28
    checks.check("E3 binary rect: 28 laws; row-major = reverse; corners vs row-major 44/64 cells TV 135/578", len(laws) == target and reverse_key == key_of_order((0, 1, 2, 3, 4, 5), n6, e6) and differing_cells(corners, row_major) == 44 and total_variation(corners, row_major) == Fraction(135, 578), f"laws {len(laws)}")
    constant = ProductRule(((2, 2), (2, 2)))
    laws = defaultdict(int)
    for order in permutations(range(n6)):
        laws[tuple(sorted(constant.law(n6, e6, key_of_order(order, n6, e6), configs6).items()))] += 1
    checks.check("E4 binary constant rule: one law over all 720 orders", len(laws) == 1, f"laws {len(laws)}")


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    if mut("claim_all_orders_same_law"):
        text += " only route"
    if mut("claim_order_selected"):
        text += " the physical order is selected"
    if mut("claim_mixture_is_law"):
        text = text.replace("witness-generating device", "law")
    lowered = text.lower()
    fences = ("No order is selected as physical", "witness-generating device", CLAIM_ID)
    banned = ("only route", "last route", "closes the route", "exhaust", "the physical order is selected")
    checks.check("F1 note carries the fence sentences", all(f in text for f in fences))
    checks.check("F2 note avoids closing and selecting language", not any(b in lowered for b in banned))
    source = Path(__file__).read_text(encoding="utf-8")
    scan = "\n".join(line for line in source.splitlines() if "float-scan-marker-line" not in line)
    if mut("float_literal_present"):
        scan += " " + "0" + "." + "5"
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")  # float-scan-marker-line
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    hits = float_literal.findall(scan)
    clean = not hits and conversion not in scan and evalf not in scan and numeric not in scan
    checks.check("F3 runner source carries no floating-point literal or conversion", clean and len(scan) > 300, f"hits {len(hits)}")


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1 resolution certificate printed", len(N5_LINES) == 5 and all(len(line) >= 40 for line in N5_LINES))


def read_if_present(rel: str) -> str:
    path = ROOT / rel
    return path.read_text(encoding="utf-8") if path.exists() else ""


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        name = argv[argv.index("--mutation") + 1]
        if name not in MUTATION_GATE:
            print(f"unknown mutation {name}")
            return 2
        ACTIVE_MUTATION = name
    print("AUDIT_INPUT_PATHS:")
    for rel in AUDIT_INPUT_PATHS:
        print(f"  {rel}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: six-projector menu; product rules (3,1,2),(5,2,4), constant (2,2,2), binary Ising-type e^J=2; windows path3, P4, star4, cycle4, 2x3 rectangle, 2x2x2 cube; every order")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    checks = Checks()
    note_text = read_if_present(AUDIT_INPUT_PATHS[0])
    axiom_text = read_if_present(AUDIT_INPUT_PATHS[1])
    classification_text = read_if_present(AUDIT_INPUT_PATHS[2])
    monotone_text = read_if_present(AUDIT_INPUT_PATHS[3])
    shared = compute_shared()
    family_a(checks, note_text, axiom_text, classification_text, monotone_text)
    family_b(checks, shared)
    family_c(checks, shared)
    family_d(checks, shared)
    family_e(checks, shared)
    family_f(checks, note_text)
    family_g(checks)
    ok = checks.finish()
    if ACTIVE_MUTATION is not None:
        observed = "".join(sorted(checks.failed_families)) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
