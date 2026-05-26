#!/usr/bin/env python3
"""Finite cone-cap construction certificate for the PL-topology repair row.

The runner proves only finite combinatorial facts about the declared cubical
ball boundary family. It deliberately does not import or assert PL
Schoenflies, Perelman/Moise, mapping-class-group, van Kampen, or
Kawamoto-Smit homogeneity authority.
"""

from __future__ import annotations

import itertools
from collections import Counter, defaultdict, deque
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


def cubical_ball_cubes(radius: int) -> set[tuple[int, int, int]]:
    sites: set[tuple[int, int, int]] = set()
    for x in range(-radius - 1, radius + 2):
        for y in range(-radius - 1, radius + 2):
            for z in range(-radius - 1, radius + 2):
                if x * x + y * y + z * z <= radius * radius:
                    sites.add((x, y, z))

    cubes: set[tuple[int, int, int]] = set()
    for x, y, z in sites:
        corners = [
            (x + dx, y + dy, z + dz)
            for dx in (0, 1)
            for dy in (0, 1)
            for dz in (0, 1)
        ]
        if all(corner in sites for corner in corners):
            cubes.add((x, y, z))
    return cubes


def cube_faces(cube: tuple[int, int, int]) -> list[tuple[tuple[int, int, int], ...]]:
    x, y, z = cube
    return [
        tuple(sorted(((x, y, z), (x + 1, y, z), (x + 1, y + 1, z), (x, y + 1, z)))),
        tuple(sorted(((x, y, z + 1), (x + 1, y, z + 1), (x + 1, y + 1, z + 1), (x, y + 1, z + 1)))),
        tuple(sorted(((x, y, z), (x + 1, y, z), (x + 1, y, z + 1), (x, y, z + 1)))),
        tuple(sorted(((x, y + 1, z), (x + 1, y + 1, z), (x + 1, y + 1, z + 1), (x, y + 1, z + 1)))),
        tuple(sorted(((x, y, z), (x, y + 1, z), (x, y + 1, z + 1), (x, y, z + 1)))),
        tuple(sorted(((x + 1, y, z), (x + 1, y + 1, z), (x + 1, y + 1, z + 1), (x + 1, y, z + 1)))),
    ]


def boundary_quads(cubes: set[tuple[int, int, int]]) -> list[tuple[tuple[int, int, int], ...]]:
    counts: Counter[tuple[tuple[int, int, int], ...]] = Counter()
    for cube in cubes:
        counts.update(cube_faces(cube))
    return [face for face, count in counts.items() if count == 1]


def quad_cycle(quad: tuple[tuple[int, int, int], ...]) -> list[tuple[int, int, int]]:
    """Return the four vertices in cyclic order around an axis-aligned square."""
    verts = list(quad)
    ranges = [
        (max(v[axis] for v in verts) - min(v[axis] for v in verts), axis)
        for axis in range(3)
    ]
    varying = [axis for width, axis in ranges if width != 0]
    if len(varying) != 2:
        raise ValueError(f"not an axis-aligned square: {quad!r}")
    a, b = varying
    min_a = min(v[a] for v in verts)
    max_a = max(v[a] for v in verts)
    min_b = min(v[b] for v in verts)
    max_b = max(v[b] for v in verts)

    def pick(aa: int, bb: int) -> tuple[int, int, int]:
        matches = [v for v in verts if v[a] == aa and v[b] == bb]
        if len(matches) != 1:
            raise ValueError(f"bad square corner lookup: {quad!r}")
        return matches[0]

    return [pick(min_a, min_b), pick(max_a, min_b), pick(max_a, max_b), pick(min_a, max_b)]


def triangulate_quad(quad: tuple[tuple[int, int, int], ...]) -> list[tuple[tuple[int, int, int], ...]]:
    verts = quad_cycle(quad)
    return [tuple(sorted((verts[0], verts[1], verts[2]))), tuple(sorted((verts[0], verts[2], verts[3])))]


def edges_of(simplex: tuple[int, ...]) -> set[tuple[int, int]]:
    return {tuple(sorted(edge)) for edge in itertools.combinations(simplex, 2)}


def faces_of_tet(tet: tuple[int, int, int, int]) -> set[tuple[int, int, int]]:
    return {tuple(sorted(face)) for face in itertools.combinations(tet, 3)}


def connected_tri_surface(triangles: set[tuple[int, int, int]]) -> bool:
    by_edge: defaultdict[tuple[int, int], list[tuple[int, int, int]]] = defaultdict(list)
    for tri in triangles:
        for edge in edges_of(tri):
            by_edge[edge].append(tri)
    if not triangles:
        return False
    start = next(iter(triangles))
    seen = {start}
    queue: deque[tuple[int, int, int]] = deque([start])
    while queue:
        tri = queue.popleft()
        for edge in edges_of(tri):
            for nb in by_edge[edge]:
                if nb not in seen:
                    seen.add(nb)
                    queue.append(nb)
    return seen == triangles


def finite_certificate(radius: int) -> None:
    print(f"\n=== R={radius} finite cone-cap certificate ===")
    cubes = cubical_ball_cubes(radius)
    quads = boundary_quads(cubes)

    vertex_map: dict[tuple[int, int, int], int] = {}
    for vertex in sorted({v for quad in quads for v in quad}):
        vertex_map[vertex] = len(vertex_map)

    boundary_tris: set[tuple[int, int, int]] = set()
    for quad in quads:
        for tri in triangulate_quad(quad):
            boundary_tris.add(tuple(sorted(vertex_map[v] for v in tri)))

    boundary_edges: Counter[tuple[int, int]] = Counter()
    for tri in boundary_tris:
        boundary_edges.update(edges_of(tri))
    boundary_vertices = {v for tri in boundary_tris for v in tri}
    chi_boundary = len(boundary_vertices) - len(boundary_edges) + len(boundary_tris)

    apex = max(boundary_vertices) + 1
    tets = {tuple(sorted((apex, *tri))) for tri in boundary_tris}
    tet_faces: Counter[tuple[int, int, int]] = Counter()
    tet_edges: set[tuple[int, int]] = set()
    for tet in tets:
        tet_faces.update(faces_of_tet(tet))
        tet_edges.update(edges_of(tet))

    base_faces = {face for face, count in tet_faces.items() if count == 1}
    side_faces = {face for face, count in tet_faces.items() if count == 2}
    stray_faces = {face: count for face, count in tet_faces.items() if count not in (1, 2)}
    cap_vertices = set(boundary_vertices) | {apex}
    chi_cap = len(cap_vertices) - len(tet_edges) + len(tet_faces) - len(tets)
    apex_link = {tuple(sorted(v for v in tet if v != apex)) for tet in tets}

    check(f"R{radius}: nonempty cubical ball", len(cubes) > 0, f"cubes={len(cubes)}")
    check(f"R{radius}: nonempty boundary", len(quads) > 0, f"quads={len(quads)}")
    check(
        f"R{radius}: boundary edge degree two",
        all(count == 2 for count in boundary_edges.values()),
        f"edges={len(boundary_edges)}",
    )
    check(f"R{radius}: boundary connected", connected_tri_surface(boundary_tris))
    check(f"R{radius}: boundary chi equals two", chi_boundary == 2, f"chi={chi_boundary}")
    check(
        f"R{radius}: cone boundary equals base triangulation",
        base_faces == boundary_tris,
        f"base={len(base_faces)} tris={len(boundary_tris)}",
    )
    check(
        f"R{radius}: all non-base cone faces are paired",
        len(side_faces) + len(base_faces) == len(tet_faces) and not stray_faces,
        f"paired={len(side_faces)} stray={len(stray_faces)}",
    )
    check(
        f"R{radius}: apex link is boundary triangulation",
        apex_link == boundary_tris,
        f"link_tris={len(apex_link)}",
    )
    check(f"R{radius}: cone cap chi equals one", chi_cap == 1, f"chi={chi_cap}")


def note_boundary_checks() -> None:
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "This row no longer claims to establish the previous five named external",
        "finite cone-cap construction certificate",
        "No derivation of PL Schoenflies",
        "No proof that every admissible cap is PL-homeomorphic to the cone cap.",
        "No physical closure theorem",
        "No audit verdict and no direct ledger retag.",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)
    forbidden = [
        "PL S^3.",
        "accepted named non-derivation imports usable as one-hop authorities",
        "Kawamoto-Smit homogeneity premise as accepted",
    ]
    for phrase in forbidden:
        check(f"note omits forbidden overclaim: {phrase}", phrase not in text)


def main() -> int:
    note_boundary_checks()
    for radius in (2, 3, 4):
        finite_certificate(radius)
    print("\nPL finite cone-cap certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
