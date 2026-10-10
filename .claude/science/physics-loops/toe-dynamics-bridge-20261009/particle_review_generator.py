#!/usr/bin/env python3
"""Reviewer-owned small full-state generator controls; no author imports.

Construct Q from labelled one-particle hops and fair labelled pair clocks,
then apply Q to coordinate and squared-norm functions. In particular bracket
traces are computed by Q||p||^2 - 2<p,Qp>, not by the author's event-increment
formula. All arithmetic is exact. The PDE/stopping proofs remain analytic.
"""

from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from math import comb
import sys


MASS, SIDE = F(5, 7), F(7, 3)
SIGMA, GAMMA, KAPPA = F(11, 5), F(13, 17), F(19, 23)
VELOCITIES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0))


def require(condition, explanation):
    if not condition:
        raise AssertionError(explanation)


def compact(d):
    return {k: v for k, v in d.items() if v}


class Generator:
    def __init__(self, m, particles, mutant=None):
        self.m, self.particles, self.mutant = m, particles, mutant
        self.cells = tuple(product(range(m), repeat=3))
        self.cell_index = {x: i for i, x in enumerate(self.cells)}
        self.categories = len(self.cells) * 4
        self.w, self.h = F(1, m ** 3), SIDE / m
        self.a = MASS / (particles * self.w)

    def moved(self, category):
        cell, species = divmod(category, 4)
        position = list(self.cells[cell])
        for axis, component in enumerate(VELOCITIES[species]):
            if component:
                position[axis] = (position[axis] + component) % self.m
        return 4 * self.cell_index[tuple(position)] + species

    def row(self, state):
        """Two generator rows, with diagonals, obtained from labelled clocks."""
        hop, collision = defaultdict(F), defaultdict(F)
        for label, category in enumerate(state):
            target = list(state)
            target[label] = self.moved(category)
            hop[tuple(sorted(target))] += SIGMA / self.h
        coefficient = GAMMA * KAPPA * self.a
        if self.mutant == "collision_volume":
            coefficient *= self.w
        if self.mutant == "collision_mass":
            coefficient /= MASS
        for a, b in combinations(range(self.particles), 2):
            cell_a, species_a = divmod(state[a], 4)
            cell_b, species_b = divmod(state[b], 4)
            if cell_a != cell_b and self.mutant != "cross_cell":
                continue
            pair = {species_a, species_b}
            outputs = (2, 3) if pair == {0, 1} else (0, 1) if pair == {2, 3} else None
            if outputs is None:
                continue
            for sa, sb in (outputs, outputs[::-1]):
                target = list(state)
                target[a], target[b] = 4 * cell_a + sa, 4 * cell_b + sb
                collision[tuple(sorted(target))] += coefficient / 2
        for row in (hop, collision):
            require(state not in row, "unaccounted null event")
            require(all(rate > 0 for rate in row.values()), "negative off-diagonal generator rate")
            row[state] = -sum(row.values(), F(0))
            require(sum(row.values(), F(0)) == 0, "generator row sum")
        return dict(hop), dict(collision)

    def field(self, state):
        return {at: self.a * number for at, number in Counter(state).items()}

    def norm_squared(self, state):
        return self.w * self.a * self.a * sum(number * number for number in Counter(state).values())

    def generator_coordinate_action(self, row):
        out = defaultdict(F)
        for target, rate in row.items():
            for category, number in Counter(target).items():
                out[category] += rate * self.a * number
        return compact(out)

    def carre_du_champ_trace(self, state, row, action):
        p = self.field(state)
        q_norm = sum((rate * self.norm_squared(target) for target, rate in row.items()), F(0))
        pairing = self.w * sum((value * action.get(at, 0) for at, value in p.items()), F(0))
        return q_norm - 2 * pairing

    def continuum_formula_at_grid(self, state):
        """Separate density-field calculation, with neither labels nor Q."""
        p = self.field(state)
        hop, collision = defaultdict(F), defaultdict(F)
        for category, value in p.items():
            flux = SIGMA * value / self.h
            hop[category] -= flux
            hop[self.moved(category)] += flux
        products = F(0)
        for cell in range(len(self.cells)):
            f = [p.get(4 * cell + i, F(0)) for i in range(4)]
            forward, backward = f[0] * f[1], f[2] * f[3]
            flux = GAMMA * KAPPA * (forward - backward)
            for species, sign in ((0, -1), (1, -1), (2, 1), (3, 1)):
                collision[4 * cell + species] += sign * flux
            products += forward + backward
        q_hop = 2 * SIGMA * MASS * sum(p.values(), F(0)) / (self.particles * self.h)
        if self.mutant == "hop_bracket_factor":
            q_hop /= 2
        q_collision = 4 * GAMMA * MASS * KAPPA * products / self.particles
        return compact(hop), compact(collision), q_hop, q_collision

    def moments(self, state):
        values = [F(0)] * 5
        for category in state:
            velocity = VELOCITIES[category % 4]
            moment = (1, *velocity, sum(x * x for x in velocity))
            for k in range(5):
                values[k] += MASS * moment[k] / self.particles
        return tuple(values)


def complete_generator_check(m, particles, mutant):
    model = Generator(m, particles, mutant)
    states = tuple(combinations_with_replacement(range(model.categories), particles))
    state_set = set(states)
    require(len(states) == comb(model.categories + particles - 1, particles), "state census")
    edges = 0
    seen_reaction = False
    for state in states:
        hop_row, collision_row = model.row(state)
        expected_hop, expected_collision, expected_qhop, expected_qcollision = model.continuum_formula_at_grid(state)
        hop_action = model.generator_coordinate_action(hop_row)
        collision_action = model.generator_coordinate_action(collision_row)
        require(hop_action == expected_hop, f"coordinate streaming mismatch at {state}")
        require(collision_action == expected_collision, f"coordinate collision mismatch at {state}")
        qhop = model.carre_du_champ_trace(state, hop_row, hop_action)
        qcollision = model.carre_du_champ_trace(state, collision_row, collision_action)
        require(qhop == expected_qhop, f"hop bracket mismatch: {qhop} versus {expected_qhop}")
        require(qcollision == expected_qcollision, f"collision bracket mismatch at {state}")
        moment = model.moments(state)
        for row in (hop_row, collision_row):
            for target, rate in row.items():
                require(target in state_set, "generator leaves fixed-count space")
                require(model.moments(target) == moment, "pathwise global conservation")
                if target != state and rate:
                    edges += 1
        seen_reaction |= bool(qcollision)
    require(seen_reaction, "no collision was exercised")
    print(f"Full sparse generator: side cells={m}, N={particles}, states={len(states)}, outgoing edges={edges}.")
    print(f"  h={model.h}, w={model.w}, one-particle density={model.a}.")
    print("  Q on every density coordinate and Q||p||²−2<p,Qp> match the formulas;")
    print("  every target remains in the state space and preserves all five global moments.")
    return model


def exact_initial_law_check(model):
    categories, probabilities = (0, 1, 4), (F(1, 2), F(1, 3), F(1, 6))
    expected_field = {category: MASS * probability / model.w
                      for category, probability in zip(categories, probabilities)}
    second_moment, total_probability = F(0), F(0)
    for choices in product(range(3), repeat=model.particles):
        probability = F(1)
        state = []
        for choice in choices:
            probability *= probabilities[choice]
            state.append(categories[choice])
        field = model.field(tuple(sorted(state)))
        error = model.w * sum((field.get(at, 0) - expected_field[at]) ** 2 for at in categories)
        second_moment += probability * error
        total_probability += probability
    formula = MASS ** 2 / (model.particles * model.w) * (1 - sum(p * p for p in probabilities))
    require(total_probability == 1 and second_moment == formula, "enumerated initial-law covariance")
    print(f"Enumerated independent initial law: N={model.particles}, exact E0={second_moment}.")


def full_reaction_census():
    velocities = tuple(product((-1, 0, 1), repeat=3))
    grouped_pairs = defaultdict(list)
    for i, j in combinations_with_replacement(range(27), 2):
        vi, vj = velocities[i], velocities[j]
        signature = (*[a + b for a, b in zip(vi, vj)],
                     sum(x * x for x in vi) + sum(x * x for x in vj))
        grouped_pairs[signature].append((i, j))
    reactions = [r for group in grouped_pairs.values() for r in combinations(group, 2)]
    require(len(reactions) == 288, "complete reaction census")
    require(all(len(set(left + right)) == 4 for left, right in reactions), "four-species condition")
    print("Full D3Q27 pair-signature census: 288 exchanges, four distinct species in each.")


def overshoot_geometry_check():
    model = Generator(2, 4)
    state = (0, 4, 16, 20)
    changed = list(state)
    changed[0] = model.moved(changed[0])
    pre, post = model.field(state), model.field(tuple(sorted(changed)))
    deterministic_component = MASS / 4
    radius = 3 * model.a / 2
    gap = radius - deterministic_component
    error = model.w * sum((post.get(at, 0) - deterministic_component) ** 2
                          for at in range(model.categories))
    require(max(pre.values()) < radius < max(post.values()), "crossing overshoot missing")
    require(error >= model.w * gap ** 2, "exit threshold geometry")
    print(f"Overshoot witness: pre-max={max(pre.values())}, R={radius}, post-max={max(post.values())};")
    print(f"  actual squared error={error} >= exit threshold {model.w * gap ** 2}.")


def main():
    parser = ArgumentParser()
    parser.add_argument("--mutant", choices=("collision_volume", "collision_mass", "hop_bracket_factor", "cross_cell"))
    args = parser.parse_args()
    print("Reviewer exact generator controls; no imports from author code.")
    print(f"Mass={MASS}, physical torus side={SIDE}, sigma={SIGMA}, gamma={GAMMA}, kappa={KAPPA}.")
    if args.mutant:
        print("ACTIVE MUTANT:", args.mutant)
    full_reaction_census()
    for m, particles in ((3, 2), (2, 3)):
        model = complete_generator_check(m, particles, args.mutant)
        exact_initial_law_check(model)
    overshoot_geometry_check()
    print("REVIEWER EXACT CONTROLS COMPLETE; energy and PDE proofs checked analytically.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print("REVIEWER CONTROL FAILURE:", exc)
        sys.exit(1)
