#!/usr/bin/env python3
"""Referee for moving kernel with vacancies, a2.

Author w-jonathonsmac4f50-j5c79 (claude-opus-5). Own subset and Ising enumerations.
GKS-II is checked on three graphs, not proved for every graph.
The sphere menu is not covered: there is no GKS-II for O(3) in this argument.
"""
import itertools
from fractions import Fraction as Fr

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def ring(n):
    sites = list(range(n))
    bonds = [(i, (i + 1) % n) for i in sites]
    return sites, bonds


def torus(side):
    sites = [(i, j) for i in range(side) for j in range(side)]
    bonds = []
    for i, j in sites:
        bonds.append(((i, j), ((i + 1) % side, j)))
        bonds.append(((i, j), (i, (j + 1) % side)))
    return sites, bonds


def induced(occupied, bonds):
    present = set(occupied)
    return {edge for edge in bonds if edge[0] in present and edge[1] in present}


def subsets(sites):
    out = []
    for mask in range(1 << len(sites)):
        out.append(frozenset(sites[i] for i in range(len(sites)) if mask >> i & 1))
    return out


def combinatorics():
    ok = True
    for sites, bonds in (ring(6), torus(3)):
        pieces = subsets(sites)
        for left in pieces:
            for right in pieces:
                ok &= len(left | right) + len(left & right) == len(left) + len(right)
                edges_left, edges_right = induced(left, bonds), induced(right, bonds)
                ok &= induced(left & right, bonds) == edges_left & edges_right
                ok &= edges_left | edges_right <= induced(left | right, bonds)
    sites, bonds = ring(4)
    strict = False
    for left in subsets(sites):
        for right in subsets(sites):
            union = induced(left | right, bonds)
            separate = induced(left, bonds) | induced(right, bonds)
            if len(union) == 4 and len(separate) == 2:
                strict = True
    report(
        "sets",
        ok and strict,
        "on a ring of 6 and a 3x3 torus every pair is modular and the induced edges are supermodular; a ring of 4 has a strict union, 4 edges against 2",
    )


def couplings():
    ok = True
    for sites, bonds in (ring(6), torus(3)):
        for left in subsets(sites):
            for right in subsets(sites):
                meet = induced(left & right, bonds)
                join = induced(left | right, bonds)
                left_edges, right_edges = induced(left, bonds), induced(right, bonds)
                ok &= meet == left_edges & right_edges
                ok &= left_edges | right_edges <= join
    report(
        "couplings",
        ok,
        "J(A cap B) is the componentwise minimum and J(A cup B) dominates the componentwise maximum, because J is the indicator of the induced edges",
    )


def ising_moments(sites, bonds, weight):
    index = {site: i for i, site in enumerate(sites)}
    partition = Fr(0)
    one = {edge: Fr(0) for edge in bonds}
    two = {(left, right): Fr(0) for left in bonds for right in bonds}
    for spins in itertools.product((1, -1), repeat=len(sites)):
        factor = Fr(1)
        sign = {}
        for edge in bonds:
            agree = spins[index[edge[0]]] * spins[index[edge[1]]]
            sign[edge] = agree
            factor *= weight if agree == 1 else 1 / weight
        partition += factor
        for edge in bonds:
            one[edge] += factor * sign[edge]
            for other in bonds:
                two[(edge, other)] += factor * sign[edge] * sign[other]
    return partition, one, two


def griffiths():
    ok = True
    for sites, bonds, weight in ((ring(5)[0], ring(5)[1], Fr(2)), (ring(6)[0], ring(6)[1], Fr(3)), (torus(2)[0], torus(2)[1], Fr(2))):
        partition, one, two = ising_moments(sites, bonds, weight)
        for edge in bonds:
            ok &= one[edge] >= 0
            for other in bonds:
                ok &= two[(edge, other)] * partition - one[edge] * one[other] >= 0
    report(
        "griffiths",
        ok,
        "on a ring of 5 at w=2, a ring of 6 at w=3, and a 2x2 torus at w=2, every edge mean is non-negative and every edge-pair covariance is non-negative",
    )


def lattice():
    sites, bonds = ring(5)
    fugacity, weight = Fr(3, 2), Fr(2)
    marginal = {}
    for mask in range(1 << len(sites)):
        occupied = [sites[i] for i in range(len(sites)) if mask >> i & 1]
        place = {site: i for i, site in enumerate(occupied)}
        total = Fr(0)
        inside = induced(occupied, bonds)
        for spins in itertools.product((1, -1), repeat=len(occupied)):
            factor = Fr(1)
            for edge in inside:
                factor *= weight if spins[place[edge[0]]] == spins[place[edge[1]]] else 1 / weight
            total += factor
        marginal[mask] = fugacity ** len(occupied) * total
    bad = 0
    width = 1 << len(sites)
    for left in range(width):
        for right in range(width):
            if marginal[left | right] * marginal[left & right] < marginal[left] * marginal[right]:
                bad += 1
    report(
        "lattice",
        bad == 0,
        "ring of 5 at z=3/2 and w=2: all 1024 ordered pairs satisfy mu(A cup B) mu(A cap B) >= mu(A) mu(B)",
    )


def potts():
    sites, bonds = ring(5)
    index = {site: i for i, site in enumerate(sites)}
    weight = Fr(2)
    ok = True
    for states in (2, 3, 4, 6):
        partition = Fr(0)
        one = {edge: Fr(0) for edge in bonds}
        two = {(left, right): Fr(0) for left in bonds for right in bonds}
        centre = Fr(1, states)
        for config in itertools.product(range(states), repeat=len(sites)):
            factor = Fr(1)
            sign = {}
            for edge in bonds:
                agree = config[index[edge[0]]] == config[index[edge[1]]]
                sign[edge] = (1 if agree else 0) - centre
                factor *= weight if agree else 1
            partition += factor
            for edge in bonds:
                one[edge] += factor * sign[edge]
                for other in bonds:
                    two[(edge, other)] += factor * sign[edge] * sign[other]
        for edge in bonds:
            for other in bonds:
                ok &= two[(edge, other)] * partition - one[edge] * one[other] >= 0
    report(
        "potts",
        ok,
        "on a ring of 5, centred agreement covariances are non-negative at q=2, 3, 4 and 6",
    )


def main():
    combinatorics()
    couplings()
    griffiths()
    lattice()
    potts()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - for the two-valued menu the site count is modular and induced edges are supermodular, "
        "so the lattice condition reduces to Griffiths' second inequality. That inequality holds on the three checked graphs, "
        "and the occupation marginal on a ring of 5 satisfies it at z=3/2, w=2. "
        "Finite-q agreement weights stay non-negative through q=6. The sphere menu is not covered."
    )
    print(
        "SUMMARY: confirmed the set identities, the coupling comparison, the Ising covariances, the ring-of-5 lattice condition, "
        "and the finite-q checks. GKS-II is not proved for every graph, and there is no O(3) substitute here."
    )


if __name__ == "__main__":
    main()
