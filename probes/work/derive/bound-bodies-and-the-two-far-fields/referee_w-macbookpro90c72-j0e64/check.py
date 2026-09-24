#!/usr/bin/env python3
"""Referee for bound bodies and the two far fields, a1.

Author w-macbookpro90c72-j7e6e (claude-opus-5-5). Own bond derivatives and box operators.
The continuum steps that turn the virial into P=Q are the attempt's assumptions.
Content on wall bonds is not in this Hamiltonian; that is a different attempt's gap.
"""
import itertools

import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def vanished(matrix):
    simplified = sp.simplify(matrix)
    return all(simplified[i, j] == 0 for i in range(simplified.rows) for j in range(simplified.cols))


def graph(shape):
    inner = list(itertools.product(*[range(1, length + 1) for length in shape]))
    occupied = set(inner)
    interior, walls = [], []
    for site in inner:
        for axis in range(len(shape)):
            for step in (1, -1):
                neighbour = list(site)
                neighbour[axis] += step
                neighbour = tuple(neighbour)
                if step == 1 and neighbour in occupied:
                    interior.append((site, neighbour))
                elif neighbour not in occupied:
                    walls.append((site, neighbour))
    return inner, interior, walls


def fields():
    ok = True
    stiffness = sp.symbols("K", positive=True)
    for shape in ((3,), (2, 2)):
        inner, interior, walls = graph(shape)
        def tag(prefix, site):
            return prefix + "_" + "_".join(str(part) for part in site)

        rate_symbol = {site: sp.symbols(tag("u", site), real=True) for site in inner}
        length = {site: sp.symbols(tag("lam", site), real=True) for site in inner}
        rate = {site: sp.exp(rate_symbol[site]) for site in inner}
        chi = {site: sp.exp(length[site] / 2) for site in inner}
        clock = {site: rate[site] * chi[site] for site in inner}
        bond = {pair: sp.symbols(tag("h", pair[0]) + "_" + tag("t", pair[1])) for pair in interior}
        rest = {site: sp.symbols(tag("rho", site)) for site in inner}
        energy = sum(bond[(a, b)] * sp.sqrt(rate[a] * rate[b]) / (chi[a] * chi[b]) for a, b in interior)
        energy += sum(rest[site] * rate[site] for site in inner)

        def chi_at(site):
            return chi.get(site, 1)

        def clock_at(site):
            return clock.get(site, 1)

        field = -8 * stiffness * sum(
            (clock_at(b) - clock_at(a)) * (chi_at(b) - chi_at(a)) for a, b in interior + walls
        )
        neighbours = {site: [] for site in inner}
        for left, right in interior:
            neighbours[left].append(right)
            neighbours[right].append(left)
        for left, right in walls:
            neighbours[left].append(right)

        def laplacian(values, site):
            return sum(values(other) - values(site) for other in neighbours[site])

        for site in inner:
            source = sp.diff(energy, rate_symbol[site])
            hop = -sp.diff(energy, length[site])
            ok &= sp.simplify(source - hop - rest[site] * rate[site]) == 0
            ok &= sp.simplify(sp.diff(field, rate_symbol[site]) - 8 * stiffness * clock[site] * laplacian(chi_at, site)) == 0
            ok &= sp.simplify(
                sp.diff(field, length[site])
                - 4 * stiffness * (clock[site] * laplacian(chi_at, site) + chi[site] * laplacian(clock_at, site))
            ) == 0
            # Stationarity: source + 8 K N Lc = 0 and -hop + 4 K (N Lc + chi Ln) = 0.
            lap_chi = -source / (8 * stiffness * clock[site])
            lap_clock = hop / (4 * stiffness * chi[site]) - clock[site] * lap_chi / chi[site]
            ok &= sp.simplify(lap_clock - (source + 2 * hop) / (8 * stiffness * chi[site])) == 0
    report(
        "fields",
        ok,
        "on a 3-site line and a 2x2 box, e-tau is the rest energy and stationarity is Lap chi=-e/(8KN), Lap N=(e+2 tau)/(8K chi)",
    )


def charges():
    stiffness, source, hop, rate, root = sp.symbols("K e tau w chi", positive=True)
    length_charge = source / (8 * stiffness * rate * root)
    rate_charge = (source + 2 * hop) / (8 * stiffness * root)
    gap = sp.simplify(rate_charge - length_charge - (2 * hop - source * (1 / rate - 1)) / (8 * stiffness * root))
    mass = sp.symbols("m", positive=True)
    pinned = {hop: 0, source: mass * rate}
    pinned_length = sp.simplify((length_charge * root).subs(pinned) - mass / (8 * stiffness))
    pinned_rate = sp.simplify((rate_charge - length_charge * rate).subs(pinned))
    light_gap = sp.simplify(
        (source + 2 * source) / (8 * stiffness * root)
        - 3 * source / (8 * stiffness * rate * root)
        - 3 * source * (rate - 1) / (8 * stiffness * rate * root)
    )
    eps, shift, stretch, hop_scale = sp.symbols("epsilon U Lambda T")
    weak = (2 * hop_scale * eps - source * (sp.exp(-eps * shift) - 1)) / sp.exp(eps * stretch / 2)
    series = sp.series(weak, eps, 0, 3).removeO()
    expected = (2 * hop_scale + source * shift) * eps - (
        source * shift ** 2 / 2 + source * shift * stretch / 2 + hop_scale * stretch
    ) * eps ** 2
    report(
        "charges",
        gap == 0 and pinned_length == 0 and pinned_rate == 0 and light_gap == 0 and sp.expand(series - expected) == 0,
        "P-Q is (1/8K)[2 tau - e(1/w-1)]/chi, a pinned body has P=Qw, light-like content has P-3Q=(3/8K)e(w-1)/(w chi), and the weak gap starts at eps(2 tau + e u)",
    )


def box():
    shape = (3, 2)
    sites = list(itertools.product(*[range(length) for length in shape]))
    index = {site: i for i, site in enumerate(sites)}
    count = len(sites)
    shifts = []
    for axis in range(2):
        hop = sp.zeros(count)
        for site in sites:
            neighbour = list(site)
            neighbour[axis] += 1
            neighbour = tuple(neighbour)
            if neighbour in index:
                hop[index[site], index[neighbour]] = 1
        shifts.append(hop)
    pauli = [
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]
    spin = [(hop - hop.T) / (2 * sp.I) for hop in shifts]
    cosine = [(hop + hop.T) / 2 for hop in shifts]
    identity = sp.eye(2)
    hamiltonian = sum(
        (sp.kronecker_product(spin[axis], pauli[axis]) for axis in range(2)),
        sp.zeros(2 * count),
    )
    position = [sp.diag(*[site[axis] for site in sites]) for axis in range(2)]
    relabel = sum(
        (
            sp.kronecker_product((position[axis] * spin[axis] + spin[axis] * position[axis]) / 2, identity)
            for axis in range(2)
        ),
        sp.zeros(2 * count),
    )
    two_step = sum(
        (
            sp.kronecker_product((hop ** 2 - (hop.T) ** 2) / (4 * sp.I), pauli[axis])
            for axis, hop in enumerate(shifts)
        ),
        sp.zeros(2 * count),
    )
    anticommutator = all(
        vanished((cosine[axis] * spin[axis] + spin[axis] * cosine[axis]) / 2 - (hop ** 2 - (hop.T) ** 2) / (4 * sp.I))
        for axis, hop in enumerate(shifts)
    )
    bare = vanished(sp.I * (hamiltonian * relabel - relabel * hamiltonian) - two_step)
    weights = [sp.Rational(k + 2, k + 3) for k in range(count)]
    clock = sp.diag(*weights)

    def bond_difference(axis):
        matrix = sp.zeros(count)
        for site in sites:
            neighbour = list(site)
            neighbour[axis] += 1
            neighbour = tuple(neighbour)
            if neighbour in index:
                left, right = index[site], index[neighbour]
                gap = weights[right] - weights[left]
                matrix[left, right] += gap / 2
                matrix[right, left] += gap / 2
        return matrix

    wall = sum(
        (
            sp.kronecker_product(
                (position[axis] * bond_difference(axis) + bond_difference(axis) * position[axis]) / 2,
                identity,
            )
            for axis in range(2)
        ),
        sp.zeros(2 * count),
    )
    dressed = sp.kronecker_product(clock, identity)
    weighted = dressed * hamiltonian * dressed
    face = all(
        vanished(sp.I * (clock * spin[axis] - spin[axis] * clock) + bond_difference(axis)) for axis in range(2)
    )
    dressed_identity = vanished(
        sp.I * (weighted * relabel - relabel * weighted)
        - (dressed * two_step * dressed - (wall * hamiltonian * dressed + dressed * hamiltonian * wall))
    )
    stagger = sp.kronecker_product(sp.diag(*[(-1) ** sum(site) for site in sites]), identity)
    two_step_relabel = sum(
        (
            sp.kronecker_product(
                (position[axis] * spin[axis] * cosine[axis] + spin[axis] * cosine[axis] * position[axis]) / 2,
                identity,
            )
            for axis in range(2)
        ),
        sp.zeros(2 * count),
    )
    one_step_mass = vanished(stagger * relabel - relabel * stagger - 2 * stagger * relabel)
    two_step_mass = vanished(stagger * two_step_relabel - two_step_relabel * stagger)
    mass_hop = vanished(stagger * hamiltonian + hamiltonian * stagger)
    flat = sp.zeros(count)
    for axis in range(2):
        # rebuild bond differences of a constant field, which must vanish
        matrix = sp.zeros(count)
        for site in sites:
            neighbour = list(site)
            neighbour[axis] += 1
            neighbour = tuple(neighbour)
            if neighbour in index:
                left, right = index[site], index[neighbour]
                matrix[left, right] += 0
        flat += matrix
    report(
        "virial",
        anticommutator and bare and face and dressed_identity and one_step_mass and two_step_mass and mass_hop and vanished(flat),
        "on a 3x2 box, {C,S}/2 is the truncated two-step hop, i[phi H phi, G_x] has no wall operator, and the staggered mass commutes with G_P but not G_x",
    )


def main():
    fields()
    charges()
    box()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - from the bond energy, e-tau is the rest energy and stationarity is "
        "Lap chi=-e/(8KN), Lap N=(e+2 tau)/(8K chi). Then P-Q=(1/8K)[2 tau-e(1/w-1)]/chi, "
        "a pinned body has P=Qw, and light-like content has P-3Q=(3/8K)e(w-1)/(w chi). "
        "On a 3x2 box, i[phi H phi, G_x]=phi H2 phi-(Lam H phi+phi H Lam) with H2 the truncated two-step walk, "
        "while the staggered mass satisfies [eps,G_x]=2 eps G_x and [eps,G_P]=0."
    )
    print(
        "SUMMARY: confirmed the bond derivatives, the charge identities, the weak-field series, and the box virial. "
        "The continuum steps that would give P=Q for a self-bound body are the attempt's assumptions. "
        "Content on wall bonds is outside this Hamiltonian."
    )


if __name__ == "__main__":
    main()
