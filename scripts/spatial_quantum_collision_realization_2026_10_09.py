#!/usr/bin/env python3
"""Exact author controls for SPATIAL_QUANTUM_COLLISION_REALIZATION_BOUNDED_THEOREM_NOTE_2026-10-09.md; no repo imports/data.

Fractions are used throughout. The six-dimensional dilation is constructed
directly, not by importing its purported Kraus operators. The labelled jump
enumeration and occupation-product comparator use separate functions.
"""

from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
import sys


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/SPATIAL_QUANTUM_COLLISION_REALIZATION_BOUNDED_THEOREM_NOTE_2026-10-09.md', 'docs/SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md']

def require(condition, message):
    if not condition:
        raise AssertionError(message)


def zero(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    a = zero(n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(s, a):
    return [[s * x for x in row] for row in a]


def matrix_unit(n, i, j):
    a = zero(n)
    a[i][j] = F(1)
    return a


def dissipator(j, rho):
    jt = transpose(j)
    p = multiply(jt, j)
    return add(multiply(multiply(j, rho), jt),
               scale(-F(1, 2), add(multiply(p, rho), multiply(rho, p))))


def joint_unitary(mapping, co, si):
    """Real orthogonal dilation: |s,0> rotates into |mapping[s],1>."""
    w = eye(6)
    for source, target in mapping.items():
        a, b = 2 * source, 2 * target + 1
        w[a][a] = w[b][b] = co
        w[b][a] = si
        w[a][b] = -si
    return w


def reduced_from_unitary(w, rho):
    joint = zero(6)
    for i, j in product(range(3), repeat=2):
        joint[2 * i][2 * j] = rho[i][j]
    output = multiply(multiply(w, joint), transpose(w))
    return [[output[2 * i][2 * j] + output[2 * i + 1][2 * j + 1]
             for j in range(3)] for i in range(3)]


def exact_dilation_controls(mutant):
    co, si = F(3, 5), F(4, 5)
    p = si * si
    checks = 0
    for name, mapping in (("directed", {0: 1}),
                          ("reversible", {0: 1, 1: 0})):
        w = joint_unitary(mapping, co, si)
        require(multiply(transpose(w), w) == eye(6), name + " unitarity")
        k0, k1 = eye(3), zero(3)
        for source, target in mapping.items():
            k0[source][source] = co
            k1[target][source] = si
        require(add(multiply(transpose(k0), k0),
                    multiply(transpose(k1), k1)) == eye(3),
                name + " Kraus completeness")
        for a, b in product(range(3), repeat=2):
            rho = matrix_unit(3, a, b)
            actual = reduced_from_unitary(w, rho)
            kraus = add(multiply(multiply(k0, rho), transpose(k0)),
                        multiply(multiply(k1, rho), transpose(k1)))
            require(actual == kraus, name + " dilation/Kraus disagreement")
            expected_diagonal = [F(int(a == b == i)) for i in range(3)]
            if a == b and a in mapping:
                expected_diagonal[a] -= p
                expected_diagonal[mapping[a]] += p
            require([actual[i][i] for i in range(3)] == expected_diagonal,
                    name + " population/coherence failure")
            checks += 1
        if name == "directed":
            reverse = reduced_from_unitary(w, matrix_unit(3, 1, 1))
            require(reverse[0][0] == 0, "directed gate has a reverse hop")
    print("Exact dilation: two 6x6 unitaries, all 18 system matrix-unit images;")
    print("  Kraus completeness, population closure, and no directed reverse hop.")
    print(f"  cos=3/5, sin=4/5, jump probability={p}.")

    # Different mechanism: a common target with two sources is not injective.
    merged, left, right = zero(3), zero(3), zero(3)
    merged[2][0] = merged[2][1] = F(1)
    left[2][0], right[2][1] = F(1), F(1)
    coherence = matrix_unit(3, 0, 1)
    merged_gain = dissipator(merged, coherence)[2][2]
    separate_gain = add(dissipator(left, coherence),
                        dissipator(right, coherence))[2][2]
    if mutant == "merged_mark":
        require(merged_gain == 0,
                f"merged-mark population closure fails: target derivative={merged_gain}")
    require(merged_gain == 1 and separate_gain == 0,
            "merged-mark discriminator lost its contrast")
    print(f"Merged-source contrast on E_01: target derivative {merged_gain};")
    print(f"  separately marked jumps: {separate_gain} (exact).")
    return checks


def apply_pair_channel(probabilities, a, b, p):
    out = probabilities.copy()
    out[a] = (1 - p) * probabilities[a] + p * probabilities[b]
    out[b] = p * probabilities[a] + (1 - p) * probabilities[b]
    return out


def finite_schedule_nonlumpability():
    p = F(16, 25)
    outputs = []
    for source in (0, 1):
        probabilities = [F(int(source == i)) for i in range(4)]
        for a, b in ((0, 2), (0, 3), (1, 2), (1, 3)):
            probabilities = apply_pair_channel(probabilities, a, b, p)
        outputs.append(probabilities[2] + probabilities[3])
    require(outputs[0] - outputs[1] == -2 * p * p * (1 - p),
            "ordered-schedule contrast formula")
    require(outputs[0] != outputs[1], "false exact finite-step lumpability")
    print("Finite ordered four-mark schedule, same initial occupation:")
    print(f"  input (i,j) gives product-occupation probability {outputs[0]};")
    print(f"  input (j,i) gives product-occupation probability {outputs[1]};")
    print(f"  difference={outputs[0] - outputs[1]}=-2 p^2(1-p).")


VELOCITIES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0))
INPUTS = ((VELOCITIES[0], VELOCITIES[1]),
          (VELOCITIES[1], VELOCITIES[0]))
OUTPUTS = ((VELOCITIES[2], VELOCITIES[3]),
           (VELOCITIES[3], VELOCITIES[2]))
GRID_SIDE = 3
N = 4
CELL_WEIGHT = F(1, GRID_SIDE ** 3)
OMEGA = N * CELL_WEIGHT
HOP_RATE = F(7, 5)  # b/ell; positive rational speed/mesh ratio.
COLLISION_MULTIPLIER = F(5, 7)
KAPPA = F(11, 13)
PAIR_COEFFICIENT = COLLISION_MULTIPLIER * KAPPA / OMEGA
GAMMA = PAIR_COEFFICIENT / 2
CELLS = ((0, 0, 0), (1, 0, 0))


def shifted(cell, axis, signed_step):
    out = list(cell)
    out[axis] = (out[axis] + signed_step) % GRID_SIDE
    return tuple(out)


def occupation(z):
    return tuple(sorted(Counter(z).items()))


def changed_occupation(n, removal, addition):
    out = dict(n)
    for state in removal:
        out[state] -= 1
        if out[state] == 0:
            del out[state]
    for state in addition:
        out[state] = out.get(state, 0) + 1
    return tuple(sorted(out.items()))


def microscopically_enumerated_rates(z, mutant=None):
    """Enumerate actual label marks, without using occupation products."""
    hops, collisions = defaultdict(F), defaultdict(F)
    for label, (cell, velocity) in enumerate(z):
        for axis, component in enumerate(velocity):
            if not component:
                continue
            directions = (component, -component) if mutant == "symmetric_hop" else (component,)
            for direction in directions:
                changed = list(z)
                changed[label] = (shifted(cell, axis, direction), velocity)
                hops[occupation(changed)] += HOP_RATE * abs(component)
    targets = OUTPUTS[:1] if mutant == "drop_output" else OUTPUTS
    rate = PAIR_COEFFICIENT if mutant == "gamma" else GAMMA
    for a, b in combinations(range(N), 2):
        ca, va = z[a]
        cb, vb = z[b]
        if ca != cb:
            continue
        for source, target in product(INPUTS, targets):
            current = (va, vb)
            if current == source:
                next_pair = target
            elif current == target:
                next_pair = source
            else:
                continue
            changed = list(z)
            changed[a], changed[b] = (ca, next_pair[0]), (ca, next_pair[1])
            collisions[occupation(changed)] += rate
    return dict(hops), dict(collisions)


def occupation_product_rates(n):
    """Compute the target generator from occupation products only."""
    counts = dict(n)
    hops, collisions = defaultdict(F), defaultdict(F)
    for (cell, velocity), number in n:
        for axis, component in enumerate(velocity):
            if component:
                target = changed_occupation(
                    n, [(cell, velocity)],
                    [(shifted(cell, axis, component), velocity)])
                hops[target] += HOP_RATE * abs(component) * number
    for cell in {state[0] for state in counts}:
        for source, target in ((INPUTS[0], OUTPUTS[0]), (OUTPUTS[0], INPUTS[0])):
            number = counts.get((cell, source[0]), 0) * counts.get((cell, source[1]), 0)
            if number:
                key = changed_occupation(n, [(cell, v) for v in source],
                                         [(cell, v) for v in target])
                collisions[key] += PAIR_COEFFICIENT * number
    return dict(hops), dict(collisions)


def conserved_moments(n):
    return (sum(number for _, number in n),
            *(sum(number * velocity[d] for (_, velocity), number in n)
              for d in range(3)),
            sum(number * sum(t * t for t in velocity)
                for (_, velocity), number in n))


def exact_labelled_count_control(mutant):
    particle_states = tuple(product(CELLS, VELOCITIES))
    fibers, configurations, edges = set(), 0, 0
    for z in product(particle_states, repeat=N):
        n = occupation(z)
        fibers.add(n)
        actual = microscopically_enumerated_rates(z, mutant)
        expected = occupation_product_rates(n)
        require(actual[0] == expected[0], f"streaming normalization/direction mismatch at {z}")
        require(actual[1] == expected[1], f"collision normalization/output mismatch at {z}")
        moment = conserved_moments(n)
        for rates in actual:
            for target, rate in rates.items():
                require(rate > 0, "nonpositive generated rate")
                require(conserved_moments(target) == moment, "lost conserved moment")
                edges += 1
        configurations += 1
    require(len(fibers) == comb(len(particle_states) + N - 1, N),
            "occupation-fiber census incomplete")
    require(configurations == len(particle_states) ** N,
            "labelled census incomplete")
    print("Exact labelled-to-occupation generator comparison:")
    print(f"  {configurations} configurations; {len(fibers)} fibers; {edges} outgoing targets.")
    print("  Two occupied cells inside a 3x3x3 torus, four velocities, N=4;")
    print("  all streaming targets are kept in the full torus.")
    print(f"  w={CELL_WEIGHT}, Omega={OMEGA}, b/ell={HOP_RATE},")
    print(f"  c={COLLISION_MULTIPLIER}, kappa={KAPPA}, gamma={GAMMA}.")

    colocated = ((CELLS[0], VELOCITIES[0]),) * 2 + ((CELLS[0], VELOCITIES[1]),) * 2
    separated = ((CELLS[0], VELOCITIES[0]),) * 2 + ((CELLS[1], VELOCITIES[1]),) * 2
    colocated_rate = sum(microscopically_enumerated_rates(colocated)[1].values(), F(0))
    separated_rate = sum(microscopically_enumerated_rates(separated)[1].values(), F(0))
    require(colocated_rate == 4 * PAIR_COEFFICIENT, "n_i=n_j=2 factor")
    require(separated_rate == 0, "spurious non-colocated reaction")
    print(f"  n_i=n_j=2 at one cell: total forward rate={colocated_rate};")
    print(f"  species separated between cells: total collision rate={separated_rate}.")
    return configurations, len(fibers)


def full_velocity_hop_and_reaction_census():
    velocities = tuple(product((-1, 0, 1), repeat=3))
    directed_hops = sum(abs(component) for v in velocities for component in v)
    require(directed_hops == 54, "D3Q27 hop mark count")
    pair_groups = defaultdict(list)
    for a in range(len(velocities)):
        for b in range(a, len(velocities)):
            va, vb = velocities[a], velocities[b]
            key = (tuple(x + y for x, y in zip(va, vb)),
                   sum(x * x for x in va) + sum(y * y for y in vb))
            pair_groups[key].append((a, b))
    reactions = [pair for group in pair_groups.values() for pair in combinations(group, 2)]
    require(len(reactions) == 288, "D3Q27 reaction count")
    require(all(len({*left, *right}) == 4 for left, right in reactions),
            "repeated species in a nontrivial reaction")
    print(f"Full D3Q27 pair-group census: {len(reactions)} reversible reactions;")
    print(f"  four distinct species each; {directed_hops} directed hop marks per label/cell.")


def main():
    parser = ArgumentParser()
    parser.add_argument("--mutant", choices=("gamma", "drop_output", "symmetric_hop", "merged_mark"))
    args = parser.parse_args()
    print("Author exact discriminator; Python standard library, rational arithmetic.")
    if args.mutant:
        print("ACTIVE MUTANT:", args.mutant)
    exact_dilation_controls(args.mutant)
    finite_schedule_nonlumpability()
    full_velocity_hop_and_reaction_census()
    exact_labelled_count_control(args.mutant)
    print("AUTHOR CHECKS COMPLETE: exact identities and declared contrasts verified.")
    print("Not independent review; no numerical or all-size proof claim from this census.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print("DISCRIMINATOR FAILURE:", exc)
        sys.exit(1)
