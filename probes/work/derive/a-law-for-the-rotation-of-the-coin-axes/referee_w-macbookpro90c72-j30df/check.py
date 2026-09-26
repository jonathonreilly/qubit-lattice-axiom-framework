#!/usr/bin/env python3
"""Independent referee for the coin-axis rotation law, attempt 2.

Bond matrices and the torque identity are rebuilt in exact arithmetic.
The attempt's script is not imported.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
EYE = sp.eye(2)


def pauli(vector):
    return vector[0] * SIGMA[0] + vector[1] * SIGMA[1] + vector[2] * SIGMA[2]


def quaternion_matrix(scalar, vector):
    return scalar * EYE - sp.I * pauli(vector)


def cayley(vector):
    square = sum(component * component for component in vector)
    scale = 1 + square
    return quaternion_matrix((1 - square) / scale, [2 * component / scale for component in vector])


def vanished(matrix):
    return all(sp.expand(entry) == 0 for entry in matrix)


def rotation(group):
    matrix = sp.zeros(3)
    for column in range(3):
        conjugated = group * SIGMA[column] * group.H
        for row in range(3):
            matrix[row, column] = sp.expand((conjugated * SIGMA[row]).trace() / 2)
    return matrix


def bond(left, right, link):
    return (pauli(left) * link + link * pauli(right)) / 2


left_group = cayley([F(1, 2), F(-1, 3), F(1, 4)])
right_group = cayley([F(-2, 3), F(1, 5), F(3, 2)])
left_frame = sp.Matrix([F(2, 3), F(-1, 2), F(4, 5)])
right_frame = sp.Matrix([F(1, 7), F(3, 2), F(-2, 5)])
average = (left_frame + right_frame) / 2
left_rotation = rotation(left_group)
right_rotation = rotation(right_group)
conjugated = left_group * pauli(average) * right_group.H
rotated = pauli((left_rotation * left_frame + right_rotation * right_frame) / 2)
mismatch = (
    left_group * pauli(left_frame) * (right_group.H - left_group.H)
    + (left_group - right_group) * pauli(right_frame) * right_group.H
) / 2
scalar = sp.expand(conjugated.trace())
check(
    "bond mismatch",
    vanished(left_group * left_group.H - EYE)
    and vanished(right_group * right_group.H - EYE)
    and sp.expand(left_group.det() - 1) == 0
    and vanished(conjugated - rotated - mismatch)
    and scalar != 0
    and vanished(pauli(left_frame).trace() * EYE),
    f"the conjugated bond differs from every frame bond by the stated twist, trace {scalar}",
)

epsilon = sp.symbols("epsilon", real=True)
left_angle = sp.Matrix(sp.symbols("a1:4", real=True))
right_angle = sp.Matrix(sp.symbols("b1:4", real=True))
left_small = EYE - sp.I * epsilon * pauli(left_angle) / 2
right_small = EYE - sp.I * epsilon * pauli(right_angle) / 2
series_ok = True
for axis in range(3):
    expanded = (left_small * SIGMA[axis] * right_small.H).applyfunc(lambda entry: sp.series(sp.expand(entry), epsilon, 0, 2).removeO())
    constant = expanded.subs(epsilon, 0)
    linear = expanded.diff(epsilon).subs(epsilon, 0)
    axis_vector = sp.Matrix([1 if index == axis else 0 for index in range(3)])
    predicted = pauli(((left_angle + right_angle) / 2).cross(axis_vector)) + sp.I * (right_angle[axis] - left_angle[axis]) / 2 * EYE
    series_ok = series_ok and vanished(constant - SIGMA[axis]) and vanished(linear - predicted)
check(
    "first order",
    series_ok,
    "U_x sigma_j U_y^dag = sigma_j + (((theta_x+theta_y)/2) cross e_j).sigma + (i/2)(theta_y-theta_x)_j + O(theta^2)",
)

link = cayley([F(1, 3), F(1, 4), F(-1, 5)])
covariant = bond(left_rotation * left_frame, right_rotation * right_frame, left_group * link * right_group.H)
pulled = left_group * bond(left_frame, right_frame, link) * right_group.H
bare = bond(left_frame, right_frame, EYE)
stretch_left = sp.diag(F(2), F(3), F(4))
stretch_right = sp.diag(F(3, 2), F(5, 2), F(7, 2))
flat_ok = True
for axis in range(3):
    flat_bond = bond(
        left_rotation * stretch_left[:, axis],
        right_rotation * stretch_right[:, axis],
        left_group * right_group.H,
    )
    reduced = left_group * bond(stretch_left[:, axis], stretch_right[:, axis], EYE) * right_group.H
    flat_ok = flat_ok and vanished(flat_bond - reduced)
minus = -left_group
check(
    "links",
    vanished(covariant - pulled)
    and vanished(bare - pauli((left_frame + right_frame) / 2))
    and flat_ok
    and vanished(rotation(minus) - left_rotation)
    and vanished(bond(left_frame, right_frame, minus * link) + bond(left_frame, right_frame, left_group * link)),
    "the link bond is covariant, flat links see only the stretch, and a site sign flips the link but not the rotation",
)


def neighbours(side, site, axis, step=1):
    moved = list(site)
    moved[axis] = (moved[axis] + step) % side
    return tuple(moved)


def apply_generator(side, frames, links, state):
    sites = list(itertools.product(range(side), repeat=3))
    image = {}
    for site in sites:
        value = sp.zeros(2, 1)
        for axis in range(3):
            forward = neighbours(side, site, axis, 1)
            backward = neighbours(side, site, axis, -1)
            value += bond(frames[site][:, axis], frames[forward][:, axis], links[(site, axis)]) * state[forward] / (2 * sp.I)
            value += bond(frames[backward][:, axis], frames[site][:, axis], links[(backward, axis)]).H * state[backward] / (-2 * sp.I)
        image[site] = value.applyfunc(sp.expand)
    return sites, image


def real_part(expression):
    return sp.expand(sp.re(sp.expand(expression)))


def torque(side, frames, links, state):
    sites, image = apply_generator(side, frames, links, state)
    rows = {}
    for site in sites:
        for axis in range(3):
            direction = sp.Matrix([1 if index == axis else 0 for index in range(3)])
            frame_part = 0
            link_part = 0
            for bond_axis in range(3):
                forward = neighbours(side, site, bond_axis, 1)
                backward = neighbours(side, site, bond_axis, -1)
                turned = direction.cross(frames[site][:, bond_axis])
                outgoing = pauli(turned) * links[(site, bond_axis)] / 2
                incoming = links[(backward, bond_axis)] * pauli(turned) / 2
                frame_part += 2 * real_part((state[site].H * outgoing * state[forward])[0] / (2 * sp.I))
                frame_part += 2 * real_part((state[backward].H * incoming * state[site])[0] / (2 * sp.I))
                left_link = -sp.I * SIGMA[axis] * links[(site, bond_axis)] / 2
                right_link = sp.I * links[(backward, bond_axis)] * SIGMA[axis] / 2
                link_part += 2 * real_part(
                    (state[site].H * bond(frames[site][:, bond_axis], frames[forward][:, bond_axis], left_link) * state[forward])[0] / (2 * sp.I)
                )
                link_part += 2 * real_part(
                    (state[backward].H * bond(frames[backward][:, bond_axis], frames[site][:, bond_axis], right_link) * state[site])[0] / (2 * sp.I)
                )
            spin_rate = -sp.im(sp.expand((image[site].H * SIGMA[axis] * state[site])[0]))
            rows[(site, axis)] = (sp.expand(frame_part), sp.expand(link_part), sp.expand(spin_rate))
    return rows


def rational_frame(seed):
    return sp.Matrix(3, 3, lambda row, column: F((seed + 3 * row + 5 * column) % 5 - 2, 2) + (2 if row == column else 0))


def rational_state(seed):
    return sp.Matrix([F(seed % 3 - 1, 2) + sp.I * F((seed + 1) % 3 - 1, 3), F((seed + 2) % 4 - 1, 2) + sp.I * F(seed % 2, 5)])


side_three = 3
sites_three = list(itertools.product(range(side_three), repeat=3))
frames_three = {site: rational_frame(sum(site) + 1) for site in sites_three}
links_three = {
    (site, axis): cayley([F((sum(site) + axis) % 3 - 1, 2), F(axis - 1, 3), F(1, 4)])
    for site in sites_three
    for axis in range(3)
}
state_three = {site: rational_state(sum(site) + 2) for site in sites_three}
balance = torque(side_three, frames_three, links_three, state_three)
active = sum(1 for frame_part, link_part, spin_rate in balance.values() if frame_part != 0 and link_part != 0 and spin_rate != 0)
check(
    "torque identity",
    all(sp.expand(frame_part + link_part - spin_rate) == 0 for frame_part, link_part, spin_rate in balance.values()) and active > 60,
    f"{len(balance)} identities on the 3-torus, {active} with every term nonzero",
)

side_four = 4
sites_four = list(itertools.product(range(side_four), repeat=3))
coins = (sp.Matrix([1, 1]), sp.Matrix([1, sp.I]), sp.Matrix([1, 0]))
plane_wave = {site: sum((sp.I ** site[axis] * coins[axis] for axis in range(3)), sp.zeros(2, 1)) for site in sites_four}
identity_frame = {site: sp.eye(3) for site in sites_four}
bare_links = {(site, axis): EYE for site in sites_four for axis in range(3)}
_, bare_image = apply_generator(side_four, identity_frame, bare_links, plane_wave)
bare_balance = torque(side_four, identity_frame, bare_links, plane_wave)
nonzero_frame = sum(1 for frame_part, _link_part, _spin_rate in bare_balance.values() if frame_part != 0)
check(
    "bare stationary state",
    all(vanished(bare_image[site] - plane_wave[site]) for site in sites_four)
    and all(spin_rate == 0 and sp.expand(frame_part + link_part) == 0 for frame_part, link_part, spin_rate in bare_balance.values())
    and nonzero_frame == 136,
    f"energy +1, spin stationary, frame torque nonzero at {nonzero_frame} of {len(bare_balance)} pairs and equal to minus the link part",
)

lifts = {site: cayley([F(site[0] - 1, 2), F(site[1] - 2, 3), F(site[2] - 1, 4)]) for site in sites_four}
rotated_frames = {site: rotation(lifts[site]) for site in sites_four}
flat_links = {
    (site, axis): lifts[site] * lifts[neighbours(side_four, site, axis)].H for site in sites_four for axis in range(3)
}
rotated_state = {site: (lifts[site] * plane_wave[site]).applyfunc(sp.expand) for site in sites_four}
_, rotated_image = apply_generator(side_four, rotated_frames, flat_links, rotated_state)
rotated_balance = torque(side_four, rotated_frames, flat_links, rotated_state)
rotated_nonzero = sum(1 for frame_part, _link_part, _spin_rate in rotated_balance.values() if frame_part != 0)
check(
    "flat links",
    all(vanished(rotated_image[site] - rotated_state[site]) for site in sites_four)
    and all(spin_rate == 0 and sp.expand(frame_part + link_part) == 0 for frame_part, link_part, spin_rate in rotated_balance.values())
    and rotated_nonzero > 0,
    f"the dressed plane wave remains an energy +1 state, total torque vanishes, and the frame part is nonzero at {rotated_nonzero} pairs",
)


def plaquette_sum(side, links):
    total = 0
    for site in itertools.product(range(side), repeat=3):
        for first, second in ((0, 1), (0, 2), (1, 2)):
            loop = (
                links[(site, first)]
                * links[(neighbours(side, site, first), second)]
                * links[(neighbours(side, site, second), first)].H
                * links[(site, second)].H
            )
            total += sp.re(sp.expand(loop.trace()))
    return sp.expand(total)


gauge = {site: cayley([F(1, 2), F(site[0] - site[1], 3), F(site[2], 4)]) for site in sites_three}
gauged = {
    (site, axis): gauge[site] * links_three[(site, axis)] * gauge[neighbours(side_three, site, axis)].H
    for site in sites_three
    for axis in range(3)
}
before, after = plaquette_sum(side_three, links_three), plaquette_sum(side_three, gauged)
check(
    "plaquette",
    sp.expand(before - after) == 0 and before != 0,
    "Re tr of every face holonomy is unchanged by a finite link gauge transformation",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. A site-dependent coin rotation replaces the bond matrix by U_x (Ebar.sigma) U_y^dag. "
    "The difference from the rotated frame is the stated twist and has a nonzero coin scalar, so it is not a frame generator. "
    "At first order that twist is (i/2)(theta_y - theta_x)_j. The bond (1/2)(E_x.sigma W + W E_y.sigma) is covariant, "
    "and flat links built from the frame's rotation leave only the stretch. On a 3-torus, frame torque plus the link response "
    "equals (1/2) d<sigma_c>/dt at every site and axis. On the stationary 4-torus plane wave the bare frame torque is nonzero "
    f"at {nonzero_frame} of 192 pairs and cancels the link part. With flat links the dressed state stays at energy +1 and the "
    "total torque vanishes. A plaquette energy is gauge invariant. Link dynamics and a torsion-free rule for the stretches were not constructed.",
    flush=True,
)
print(
    "HIT: confirmed - covariant SU(2) links make local coin rotations a symmetry to all orders, flat links leave only the stretch, "
    "and the frame torque on a stationary state vanishes exactly when the link response does",
    flush=True,
)
