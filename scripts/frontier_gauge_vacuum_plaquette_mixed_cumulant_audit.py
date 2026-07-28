#!/usr/bin/env python3
"""
Exact mixed-cumulant audit and first nonlinear coefficient for the Wilson
gauge-vacuum plaquette on the accepted 3 spatial + 1 derived-time surface.

What this closes:
  - no nonlocal mixed correction through order beta^4
  - exact classification of every action-face multiplicity pattern through
    order beta^5, including action copies of the observed plaquette
  - an explicit 2+1+1+1 repeated-face scan as an independent rejector
  - equality of the surviving cube-shell connected cumulant and raw moment,
    because every proper shell subset has a private Haar link
  - the per-shell weight computed from the shell geometry rather than inserted:
    the coherent orientation count is solved for, and the color factor comes
    from an explicit index contraction under the exact second Haar moment
    int dU U_ij conj(U)_kl = delta_ik delta_jl / N, whose index classes are
    checked to stand in bijection with the vertices of the closed surface
  - exact first nonlinear coefficient in the full-vacuum reduction law

What this does not close:
  - the full nonperturbative beta-dependent reduction law at beta = 6
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product

import numpy as np


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

DIMS = 4
OBSERVED = ((0, 0, 0, 0), (0, 1))


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def unit(mu: int) -> tuple[int, ...]:
    out = [0] * DIMS
    out[mu] = 1
    return tuple(out)


UNITS = [unit(mu) for mu in range(DIMS)]


def add(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(x, y))


def subtract(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a - b for a, b in zip(x, y))


def plaquette_key(plaquette: tuple[tuple[int, ...], tuple[int, int]]) -> tuple[tuple[int, ...], tuple[int, int]]:
    return plaquette


def canonical_edge(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return (a, b) if a <= b else (b, a)


def plaquettes_on_edge(
    edge: tuple[tuple[int, ...], tuple[int, ...]],
) -> set[tuple[tuple[int, ...], tuple[int, int]]]:
    """The six unit plaquettes incident to a lattice edge in four dimensions."""
    left, right = edge
    changed = [index for index, (a, b) in enumerate(zip(left, right)) if a != b]
    if len(changed) != 1 or abs(left[changed[0]] - right[changed[0]]) != 1:
        raise ValueError(f"not a unit lattice edge: {edge}")
    mu = changed[0]
    lower = tuple(min(a, b) for a, b in zip(left, right))
    out = set()
    for nu in range(DIMS):
        if nu == mu:
            continue
        directions = tuple(sorted((mu, nu)))
        out.add((lower, directions))
        out.add((subtract(lower, UNITS[nu]), directions))
    return out


def oriented_edges(plaquette: tuple[tuple[int, ...], tuple[int, int]]) -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    base, (mu, nu) = plaquette
    v0 = base
    v1 = add(base, UNITS[mu])
    v2 = add(v1, UNITS[nu])
    v3 = add(base, UNITS[nu])
    return ((v0, v1), (v1, v2), (v2, v3), (v3, v0))


def edges_unoriented(plaquette: tuple[tuple[int, ...], tuple[int, int]]) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    return {canonical_edge(a, b) for a, b in oriented_edges(plaquette)}


def edge_charge_map(plaquette: tuple[tuple[int, ...], tuple[int, int]]) -> Counter[tuple[tuple[int, ...], tuple[int, ...]]]:
    out: Counter[tuple[tuple[int, ...], tuple[int, ...]]] = Counter()
    for a, b in oriented_edges(plaquette):
        out[canonical_edge(a, b)] += 1 if a <= b else -1
    return out


OBSERVED_EDGES = tuple(edges_unoriented(OBSERVED))
OBSERVED_EDGE_SET = set(OBSERVED_EDGES)


def shares_exactly_one_observed_edge(plaquette: tuple[tuple[int, ...], tuple[int, int]], edge: tuple[tuple[int, ...], tuple[int, ...]]) -> bool:
    plaquette_edges = edges_unoriented(plaquette)
    return edge in plaquette_edges and len(plaquette_edges & OBSERVED_EDGE_SET) == 1


def per_observed_edge_candidates() -> list[list[tuple[tuple[int, ...], tuple[int, int]]]]:
    out: list[list[tuple[tuple[int, ...], tuple[int, int]]]] = []
    for edge in OBSERVED_EDGES:
        candidates = [
            plaquette
            for plaquette in plaquettes_on_edge(edge)
            if plaquette != OBSERVED
            and shares_exactly_one_observed_edge(plaquette, edge)
        ]
        out.append(sorted(candidates, key=plaquette_key))
    return out


def has_mod3_assignment(copies: tuple[tuple[tuple[int, ...], tuple[int, int]], ...]) -> tuple[bool, tuple[int, ...] | None]:
    maps = [edge_charge_map(plaquette) for plaquette in copies]
    edges = sorted({edge for mapping in maps for edge in mapping})
    for signs in product((1, -1), repeat=len(copies)):
        charges: Counter[tuple[tuple[int, ...], tuple[int, ...]]] = Counter()
        for sign, mapping in zip(signs, maps):
            for edge, value in mapping.items():
                charges[edge] += sign * value
        if all(charges[edge] % 3 == 0 for edge in edges):
            return True, signs
    return False, None


def max_shared_observed_edges() -> int:
    """Largest observed-edge overlap among all faces incident to that boundary."""
    candidates = set().union(*(plaquettes_on_edge(edge) for edge in OBSERVED_EDGES))
    return max(
        len(edges_unoriented(plaquette) & OBSERVED_EDGE_SET)
        for plaquette in candidates
        if plaquette != OBSERVED
    )


def private_edges(
    faces: tuple[tuple[tuple[int, ...], tuple[int, int]], ...],
) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    """Links carried by exactly one distinct face of a support.

    Repeated copies of a face are deliberately collapsed here.  If a face has
    such a link, bi-invariance of that private Haar variable makes the entire
    repeated family of that face independent of the remaining face family, so
    a mixed connected cumulant factorizes to zero.
    """
    counts: Counter[tuple[tuple[int, ...], tuple[int, ...]]] = Counter()
    for face in set(faces):
        counts.update(edges_unoriented(face))
    return {edge for edge, count in counts.items() if count == 1}


def max_pairwise_shared_edges() -> int:
    """Largest link intersection of two distinct unit plaquettes.

    Any intersecting pair is, by translation, represented among the six faces
    incident to one fixed edge.  Nonintersecting pairs have overlap zero.
    """
    incident = plaquettes_on_edge(OBSERVED_EDGES[0])
    return max(
        len(edges_unoriented(left) & edges_unoriented(right))
        for left, right in combinations(incident, 2)
    )


def multiplicity_partitions(total: int) -> list[tuple[int, ...]]:
    """Every multiplicity pattern of `total` action-plaquette insertions."""

    def walk(remaining: int, largest: int) -> list[tuple[int, ...]]:
        if remaining == 0:
            return [()]
        out: list[tuple[int, ...]] = []
        for part in range(min(remaining, largest), 0, -1):
            out.extend((part, *rest) for rest in walk(remaining - part, part))
        return out

    return walk(total, total)


def action_sector_classes_through_five() -> list[tuple[int, tuple[int, ...], bool, int, str]]:
    """Classify all multiplicity patterns and observed-face placements.

    A row is `(order, action multiplicities, observed_in_action,
    total_distinct_faces, disposition)`.  The observable supplies one fixed
    copy of `OBSERVED`.  If the action also contains that face, it does not add
    a distinct support face.  This finite table closes the mixed sectors that
    a non-observed-only overlap count would miss.
    """
    rows = []
    for order in range(1, 6):
        for pattern in multiplicity_partitions(order):
            for observed_in_action in (False, True):
                action_distinct = len(pattern)
                total_distinct = action_distinct + (0 if observed_in_action else 1)
                local = observed_in_action and action_distinct == 1
                disposition = (
                    "local-block"
                    if local
                    else "distinct-six-candidate"
                    if total_distinct == 6
                    else "private-link-factorization"
                )
                rows.append(
                    (order, pattern, observed_in_action, total_distinct, disposition)
                )
    return rows


def five_face_private_link_audit() -> tuple[int, int, int]:
    """Exhaust the only nontrivial at-most-five-distinct support boundary.

    With fewer than five distinct faces, a fixed face can share at most three
    of its four links because two distinct plaquettes share at most one link.
    For five faces, absence of a private observed link forces exactly one
    non-observed face on each observed edge; those 5^4 candidates are searched
    here for a private link anywhere in the support.
    """
    tested = 0
    without_private_link = 0
    minimum_private_links = 10**9
    for choice in product(*per_observed_edge_candidates()):
        if len(set(choice)) < 4:
            continue
        tested += 1
        count = len(private_edges((OBSERVED, *choice)))
        minimum_private_links = min(minimum_private_links, count)
        if count == 0:
            without_private_link += 1
    return tested, without_private_link, minimum_private_links


def order_four_leafless_audit() -> tuple[int, int]:
    per_edge = per_observed_edge_candidates()
    total = 0
    survivors = 0
    for choice in product(*per_edge):
        if len(set(choice)) < 4:
            continue
        total += 1
        ok, _ = has_mod3_assignment((OBSERVED, *choice))
        if ok:
            survivors += 1
    return total, survivors


def candidate_extra_faces(
    support: tuple[tuple[tuple[int, ...], tuple[int, int]], ...]
) -> list[tuple[tuple[int, ...], tuple[int, int]]]:
    used = set(support) | {OBSERVED}
    extras = set().union(
        *(
            plaquettes_on_edge(edge)
            for plaquette in support
            for edge in edges_unoriented(plaquette)
        )
    )
    extras -= used
    return sorted(extras, key=plaquette_key)


def order_five_distinct_survivors() -> tuple[int, dict[tuple[tuple[tuple[int, ...], tuple[int, int]], ...], tuple[int, ...]]]:
    per_edge = per_observed_edge_candidates()
    survivors: dict[tuple[tuple[tuple[int, ...], tuple[int, int]], ...], tuple[int, ...]] = {}
    seen: set[tuple[tuple[tuple[int, ...], tuple[int, int]], ...]] = set()
    tested = 0
    for choice in product(*per_edge):
        if len(set(choice)) < 4:
            continue
        for extra in candidate_extra_faces(choice):
            support = tuple(sorted((*choice, extra), key=plaquette_key))
            if support in seen:
                continue
            seen.add(support)
            tested += 1
            ok, signs = has_mod3_assignment((OBSERVED, *support))
            if ok:
                survivors[support] = signs if signs is not None else ()
    return tested, survivors


def order_five_repeat_sector_survivors() -> tuple[int, int]:
    """Enumerate the four-distinct-plus-one-repeat multiplicity sector 2+1+1+1.

    Each copy of a repeated action face carries its own independent orientation
    sign, so this is a genuinely larger sign space than the order-beta^4 audit.
    """
    per_edge = per_observed_edge_candidates()
    seen: set[tuple[tuple[tuple[int, ...], tuple[int, int]], ...]] = set()
    tested = 0
    survivors = 0
    for choice in product(*per_edge):
        if len(set(choice)) < 4:
            continue
        for doubled in range(len(choice)):
            multiset = tuple(sorted((*choice, choice[doubled]), key=plaquette_key))
            if multiset in seen:
                continue
            seen.add(multiset)
            tested += 1
            ok, _ = has_mod3_assignment((OBSERVED, *multiset))
            if ok:
                survivors += 1
    return tested, survivors


def expected_cube_shells() -> set[tuple[tuple[tuple[int, ...], tuple[int, int]], ...]]:
    out: set[tuple[tuple[tuple[int, ...], tuple[int, int]], ...]] = set()
    for lam in (2, 3):
        for offset in (-1, 0):
            shift = tuple(offset if i == lam else 0 for i in range(DIMS))
            opposite = tuple((1 if offset == 0 else -1) if i == lam else 0 for i in range(DIMS))
            shell = (
                (shift, (0, lam)),
                (add((0, 1, 0, 0), shift), (0, lam)),
                (shift, (1, lam)),
                (add((1, 0, 0, 0), shift), (1, lam)),
                (opposite, (0, 1)),
            )
            out.add(tuple(sorted(shell, key=plaquette_key)))
    return out


def cube_shell_complex(shell):
    """Closed surface formed by the observed plaquette and one surviving shell."""
    faces = tuple(sorted((OBSERVED, *shell), key=plaquette_key))
    vertices = set()
    edge_faces: dict[tuple[tuple[int, ...], tuple[int, ...]], list] = {}
    for face in faces:
        for a, b in oriented_edges(face):
            vertices.add(a)
            vertices.add(b)
            edge_faces.setdefault(canonical_edge(a, b), []).append(face)
    return faces, vertices, edge_faces


def oriented_word(face, sigma):
    """Ordered (link, direction, tail vertex) word of `face` traversed with sign `sigma`."""
    steps = list(oriented_edges(face))
    if sigma < 0:
        steps = [(b, a) for a, b in reversed(steps)]
    return [(canonical_edge(a, b), 1 if a <= b else -1, a) for a, b in steps]


def coherent_orientations(faces):
    """Face orientations for which every shared link is traversed once each way."""
    out = []
    for sigmas in product((1, -1), repeat=len(faces)):
        directions: dict = {}
        ok = True
        for face, sigma in zip(faces, sigmas):
            for link, direction, _ in oriented_word(face, sigma):
                if link in directions and directions[link] + direction != 0:
                    ok = False
                    break
                directions.setdefault(link, direction)
            if not ok:
                break
        if ok:
            out.append(sigmas)
    return out


class IndexClasses:
    """Union-find over the color-index slots of the shell's trace network."""

    def __init__(self) -> None:
        self.parent: dict = {}

    def find(self, item):
        self.parent.setdefault(item, item)
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left, right) -> None:
        a, b = self.find(left), self.find(right)
        if a != b:
            self.parent[a] = b


def haar_index_contraction(faces, sigmas, cross_pair: bool = True):
    """Integrate prod_f Tr(W_f) with int dU U_ij conj(U)_kl = delta_ik delta_jl / N.

    Returns (index classes, slot -> vertex) or None when the orientation fails to
    traverse every link once forward and once backward.  With cross_pair=False the
    index pairing of the second moment is deliberately wrong, which is a rejector.
    """
    classes = IndexClasses()
    slot_vertex = {}
    occupancy: dict = {}
    for face, sigma in zip(faces, sigmas):
        word = oriented_word(face, sigma)
        for position, (link, direction, tail) in enumerate(word):
            row = (face, position)
            col = (face, (position + 1) % len(word))
            classes.find(row)
            classes.find(col)
            slot_vertex[row] = tail
            occupancy.setdefault(link, []).append((direction, row, col))
    for entries in occupancy.values():
        if len(entries) != 2:
            return None
        (first_dir, first_row, first_col), (second_dir, second_row, second_col) = entries
        if first_dir + second_dir != 0:
            return None
        forward = (first_row, first_col) if first_dir > 0 else (second_row, second_col)
        backward = (first_row, first_col) if first_dir < 0 else (second_row, second_col)
        if cross_pair:
            classes.union(forward[0], backward[1])
            classes.union(forward[1], backward[0])
        else:
            classes.union(forward[0], backward[0])
            classes.union(forward[1], backward[1])
    members: dict = {}
    for slot in classes.parent:
        members.setdefault(classes.find(slot), []).append(slot)
    return members, slot_vertex


def shell_index_classes_match_vertices(faces, sigmas, vertices) -> bool:
    """Each index class carries one lattice vertex, bijectively onto the shell's vertices."""
    contraction = haar_index_contraction(faces, sigmas)
    if contraction is None:
        return False
    members, slot_vertex = contraction
    images = set()
    for slots in members.values():
        carried = {slot_vertex[slot] for slot in slots}
        if len(carried) != 1:
            return False
        images |= carried
    return len(members) == len(vertices) and images == vertices


def proper_shell_subset_private_link_audit(faces) -> tuple[int, int]:
    """Count nonempty proper face subsets and those with a private link.

    A proper block moment in the joint moment-cumulant formula vanishes after
    integrating such a link: the selected face holonomy is Haar with zero
    first plaquette moment.  If every proper subset passes, the connected
    cumulant of the full shell equals its raw six-face moment.
    """
    tested = 0
    with_private_link = 0
    for size in range(1, len(faces)):
        for subset in combinations(faces, size):
            tested += 1
            if private_edges(subset):
                with_private_link += 1
    return tested, with_private_link


def per_shell_coefficient(shell) -> Fraction:
    """Weight of one cube shell, with every factor computed from its own geometry."""
    faces, _vertices, edge_faces = cube_shell_complex(shell)
    orientations = coherent_orientations(faces)
    members, _slot_vertex = haar_index_contraction(faces, orientations[0])
    orientation_factor = Fraction(len(orientations), 1)
    face_normalization = Fraction(1, 6) ** len(faces)
    raw_link_integral = Fraction(1, 3) ** (len(edge_faces) - len(members))
    return orientation_factor * face_normalization * raw_link_integral


def total_nonlocal_beta5_coefficient() -> Fraction:
    return sum(
        (per_shell_coefficient(shell) for shell in sorted(expected_cube_shells())),
        Fraction(0),
    )


def beta_eff_beta5_coefficient() -> Fraction:
    slope = Fraction(1, 18)
    return total_nonlocal_beta5_coefficient() / slope


HAAR_SEED = 20260726
HAAR_DIM = 3
HAAR_BATCH = 100_000


def haar_su3(rng, count):
    """Haar-distributed SU(3) samples from the QR of a complex Ginibre ensemble."""
    ginibre = rng.standard_normal((count, HAAR_DIM, HAAR_DIM)) + 1j * rng.standard_normal(
        (count, HAAR_DIM, HAAR_DIM)
    )
    unitary, upper = np.linalg.qr(ginibre / np.sqrt(2.0))
    phases = np.diagonal(upper, axis1=1, axis2=2)
    unitary = unitary * (phases / np.abs(phases))[:, None, :]
    return unitary / (np.linalg.det(unitary) ** (1.0 / HAAR_DIM))[:, None, None]


def haar_moment_residuals(rng, count):
    """Sampled group-measure residuals against the exact SU(3) first two moments."""
    sample = haar_su3(rng, count)
    dagger = np.conj(np.transpose(sample, (0, 2, 1)))
    unitarity = float(np.max(np.abs(sample @ dagger - np.eye(HAAR_DIM))))
    determinant = float(np.max(np.abs(np.linalg.det(sample) - 1.0)))
    first = float(np.max(np.abs(sample.mean(axis=0))))
    same = float(np.max(np.abs(np.einsum("nij,nkl->ijkl", sample, sample) / count)))
    exact = np.einsum("ik,jl->ijkl", np.eye(HAAR_DIM), np.eye(HAAR_DIM)) / HAAR_DIM
    mixed = float(
        np.max(np.abs(np.einsum("nij,nkl->ijkl", sample, np.conj(sample)) / count - exact))
    )
    return unitarity, determinant, first, same, mixed


def monte_carlo_shell(rng, faces, sigmas, links, samples):
    """Sampled real part of prod_f Tr(W_f) over independent Haar links."""
    words = [oriented_word(face, sigma) for face, sigma in zip(faces, sigmas)]
    running = 0.0 + 0.0j
    running_square = 0.0
    drawn = 0
    while drawn < samples:
        size = min(HAAR_BATCH, samples - drawn)
        draw = {link: haar_su3(rng, size) for link in links}
        values = np.ones(size, dtype=complex)
        for word in words:
            loop = np.broadcast_to(
                np.eye(HAAR_DIM, dtype=complex), (size, HAAR_DIM, HAAR_DIM)
            ).copy()
            for link, direction, _ in word:
                matrix = draw[link]
                loop = loop @ (
                    matrix if direction > 0 else np.conj(np.transpose(matrix, (0, 2, 1)))
                )
            values = values * np.trace(loop, axis1=1, axis2=2)
        running += complex(values.sum())
        running_square += float((values.real**2).sum())
        drawn += size
    mean = (running / samples).real
    spread = float(np.sqrt(max(running_square / samples - mean**2, 0.0) / samples))
    return mean, spread


def compact(plaquette) -> str:
    base, (mu, nu) = plaquette
    return "".join(f"{c:+d}" for c in base) + f":{mu}{nu}"


def main() -> int:
    per_edge = per_observed_edge_candidates()
    max_shared = max_shared_observed_edges()
    max_pair_shared = max_pairwise_shared_edges()
    patterns = multiplicity_partitions(5)
    sector_classes = action_sector_classes_through_five()
    six_face_candidates = [
        row for row in sector_classes if row[-1] == "distinct-six-candidate"
    ]
    private_tested, private_survivors, minimum_private = five_face_private_link_audit()
    order4_tested, order4_survivors = order_four_leafless_audit()
    order5_tested, order5_survivors = order_five_distinct_survivors()
    repeat_tested, repeat_survivors = order_five_repeat_sector_survivors()
    expected_shells = expected_cube_shells()
    ordered_shells = sorted(expected_shells)

    geometry = {}
    subset_audits = {}
    for shell in ordered_shells:
        faces, vertices, edge_faces = cube_shell_complex(shell)
        orientations = coherent_orientations(faces)
        members, _slot_vertex = haar_index_contraction(faces, orientations[0])
        geometry[shell] = (faces, vertices, edge_faces, orientations, members)
        subset_audits[shell] = proper_shell_subset_private_link_audit(faces)

    per_shell_values = {shell: per_shell_coefficient(shell) for shell in ordered_shells}
    per_shell = per_shell_values[ordered_shells[0]]
    total_coeff = total_nonlocal_beta5_coefficient()
    beta_eff_coeff = beta_eff_beta5_coefficient()

    faces0, vertices0, edge_faces0, orientations0, members0 = geometry[ordered_shells[0]]
    reference = orientations0[0]
    flips_defined = sum(
        haar_index_contraction(
            faces0,
            tuple(-s if i == position else s for i, s in enumerate(reference)),
        )
        is not None
        for position in range(len(faces0))
    )
    wrong_classes = len(haar_index_contraction(faces0, reference, cross_pair=False)[0])

    rng = np.random.default_rng(HAAR_SEED)
    unitarity, determinant, first, same, mixed = haar_moment_residuals(rng, 200_000)
    links0 = sorted(edge_faces0)
    mc_mean, mc_spread = monte_carlo_shell(rng, faces0, reference, links0, 600_000)
    flipped = (-reference[0], *reference[1:])
    flip_mean, flip_spread = monte_carlo_shell(rng, faces0, flipped, links0, 400_000)
    exact_shell = 1.0 / 81.0

    print("=" * 78)
    print("GAUGE-VACUUM PLAQUETTE MIXED-CUMULANT AUDIT")
    print("=" * 78)
    print()
    print("Observed-edge local combinatorics")
    print(f"  candidates per observed edge          = {[len(c) for c in per_edge]}")
    print(f"  max observed edges on one other face  = {max_shared}")
    print(f"  max links shared by two distinct faces = {max_pair_shared}")
    print(f"  five-face supports with no private link = {private_survivors} of {private_tested}")
    print(f"  minimum private links in that audit    = {minimum_private}")
    print(f"  order-beta^4 supports tested          = {order4_tested}")
    print(f"  order-beta^4 survivors                = {order4_survivors}")
    print()
    print("Order-beta^5 multiplicity sectors")
    print(f"  multiplicity patterns of five         = {len(patterns)}")
    print(f"  structural classes through beta^5     = {len(sector_classes)}")
    print(f"  classes reaching six distinct faces   = {len(six_face_candidates)}")
    print(
        "  sole six-face class                   = "
        f"order={six_face_candidates[0][0]} pattern={six_face_candidates[0][1]} "
        f"observed-in-action={six_face_candidates[0][2]}"
    )
    print(f"  sector 1+1+1+1+1 tested / survivors   = {order5_tested} / {len(order5_survivors)}")
    print(f"  sector 2+1+1+1   tested / survivors   = {repeat_tested} / {repeat_survivors}")
    for index, support in enumerate(sorted(order5_survivors)):
        print(f"  shell {index} = {' '.join(compact(p) for p in support)}")
    print()
    print("Cube-shell Haar contraction from the shell geometry")
    for index, shell in enumerate(ordered_shells):
        faces, vertices, edge_faces, orientations, members = geometry[shell]
        euler = len(vertices) - len(edge_faces) + len(faces)
        print(
            f"  shell {index}: F={len(faces)} V={len(vertices)} E={len(edge_faces)} "
            f"Euler={euler} orientations={len(orientations)} classes={len(members)} "
            f"N^({len(members)}-{len(edge_faces)}) weight={per_shell_values[shell]} "
            f"proper-subsets={subset_audits[shell][1]}/{subset_audits[shell][0]}"
        )
    print(f"  rejector, single-face flips still coherent = {flips_defined} of {len(faces0)}")
    print(f"  rejector, wrong index pairing classes      = {wrong_classes} vs {len(members0)}")
    print()
    print("Monte-Carlo SU(3) cross-check")
    print(f"  measure residuals |UU*-I| / |det-1|   = {unitarity:.2e} / {determinant:.2e}")
    print(f"  moment residuals E[U] / E[UU] / E[UU*] = {first:.2e} / {same:.2e} / {mixed:.2e}")
    print(f"  coherent shell    = {mc_mean:+.6f} +- {mc_spread:.6f}   exact 1/81 = {exact_shell:.6f}")
    print(f"  one face flipped  = {flip_mean:+.6f} +- {flip_spread:.6f}   exact 0")
    print()
    print("First nonlinear coefficient")
    print(f"  per-cube-shell coefficient               = {per_shell} = {float(per_shell):.15e}")
    print(f"  total nonlocal beta^5 coefficient        = {total_coeff} = {float(total_coeff):.15e}")
    print(f"  beta_eff beta^5 coefficient              = {beta_eff_coeff} = {float(beta_eff_coeff):.15e}")
    print()

    check(
        "each observed edge has exactly five distinct one-edge-sharing local action plaquettes",
        all(len(candidates) == 5 for candidates in per_edge),
        detail=f"candidate counts = {[len(candidates) for candidates in per_edge]}",
    )
    check(
        "no distinct non-observed local plaquette carries more than one observed edge",
        max_shared == 1,
        detail=f"largest observed-edge overlap = {max_shared}",
    )
    check(
        "every support with at most five distinct faces has a private Haar link",
        max_pair_shared == 1
        and private_tested == 625
        and private_survivors == 0
        and minimum_private > 0,
        detail=(
            "fewer than five faces are forced by pairwise overlap; "
            f"all {private_tested} five-face boundary candidates have at least "
            f"{minimum_private} private links"
        ),
    )
    check(
        "all mixed action multiplicities through beta^5, including observed-face copies, are classified",
        len(patterns) == 7
        and len(sector_classes) == 36
        and six_face_candidates
        == [(5, (1, 1, 1, 1, 1), False, 6, "distinct-six-candidate")]
        and all(
            row[-1] in {"local-block", "private-link-factorization"}
            for row in sector_classes
            if row not in six_face_candidates
        ),
        detail=(
            "only five distinct non-observed action faces reach six distinct "
            "total faces; every repeated or observed-copy mixed class has at "
            "most five"
        ),
    )
    check(
        "no nonlocal connected cumulant survives through order beta^4",
        order4_tested == 625 and order4_survivors == 0,
        detail=(
            f"private-link factorization covers every multiplicity; the "
            f"{order4_tested} maximal distinct supports also have "
            f"{order4_survivors} center-balanced survivors"
        ),
    )
    check(
        "the only distinct order-beta^5 survivors are the four elementary cube shells through the observed plaquette",
        set(order5_survivors) == expected_shells,
        detail=f"tested {order5_tested} supports and found {len(order5_survivors)} survivors",
    )
    check(
        "no four-distinct-plus-one-repeat order-beta^5 support survives the exact link-balance condition",
        repeat_tested == 2500 and repeat_survivors == 0,
        detail=f"tested {repeat_tested} distinct 2+1+1+1 multisets and found {repeat_survivors} survivors",
    )
    check(
        "every proper cube-shell block moment vanishes, so its connected cumulant equals its raw moment",
        all(tested == 62 and passed == tested for tested, passed in subset_audits.values()),
        detail="all 2^6 - 2 = 62 nonempty proper face subsets have a private Haar link on every shell",
    )
    check(
        "each surviving shell closes: V - E + F = 2 with every link shared by exactly two faces",
        all(
            len(v) - len(e) + len(f) == 2 and all(len(owners) == 2 for owners in e.values())
            for f, v, e, _o, _m in geometry.values()
        ),
        detail=f"F={len(faces0)} V={len(vertices0)} E={len(edge_faces0)} on every shell",
    )
    check(
        "exactly two global face orientations traverse every shared link once in each direction",
        all(len(o) == 2 for _f, _v, _e, o, _m in geometry.values()),
        detail=f"coherent orientations per shell = {sorted({len(o) for _f, _v, _e, o, _m in geometry.values()})}",
    )
    check(
        "the exact second Haar moment leaves one free color index class per shell vertex",
        all(len(m) == len(v) for _f, v, _e, _o, m in geometry.values()),
        detail=f"index classes = {len(members0)} for V = {len(vertices0)} on every shell",
    )
    check(
        "each index class carries a single lattice vertex, bijectively onto the shell vertices",
        all(
            shell_index_classes_match_vertices(f, o[0], v)
            for f, v, _e, o, _m in geometry.values()
        ),
        detail="slot -> vertex is constant on classes and onto the eight cube vertices",
    )
    check(
        "the contraction is rejected by a mis-oriented face and by the wrong second-moment pairing",
        flips_defined == 0 and wrong_classes != len(members0),
        detail=f"{flips_defined} of {len(faces0)} single-face flips stay coherent; wrong pairing gives {wrong_classes} classes",
    )
    check(
        "each cube shell contributes exactly 1/18^5",
        all(value == Fraction(1, 18**5) for value in per_shell_values.values()),
        detail=f"per-shell coefficient = {per_shell}",
    )
    check(
        "the first nonlocal numerator correction is exactly 4/18^5 * beta^5",
        total_coeff == Fraction(4, 18**5),
        detail=f"total coefficient = {total_coeff}",
    )
    check(
        "the full-vacuum reduction law therefore begins beta_eff(beta)=beta + beta^5/26244 + O(beta^6)",
        beta_eff_coeff == Fraction(1, 26244),
        detail=f"beta_eff coefficient = {beta_eff_coeff}",
    )

    check(
        "the sampled group measure reproduces the exact SU(3) first and second moments",
        unitarity < 1e-12
        and determinant < 1e-12
        and first < 0.01
        and same < 0.01
        and mixed < 0.01,
        detail=f"E[U]={first:.2e} E[UU]={same:.2e} E[UU*]-dd/N={mixed:.2e}",
        bucket="SUPPORT",
    )
    check(
        "independent Haar sampling reproduces 1/81 for the coherent shell and rejects 1/27, 1/243 and 0",
        abs(mc_mean - exact_shell) < 4 * mc_spread
        and abs(mc_mean - 1.0 / 27.0) > 4 * mc_spread
        and abs(mc_mean - 1.0 / 243.0) > 4 * mc_spread
        and abs(mc_mean) > 4 * mc_spread
        and abs(flip_mean) < 4 * flip_spread
        and abs(flip_mean - exact_shell) > 4 * flip_spread,
        detail=f"coherent {mc_mean:+.6f}+-{mc_spread:.6f}, flipped {flip_mean:+.6f}+-{flip_spread:.6f}",
        bucket="SUPPORT",
    )

    print()
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
