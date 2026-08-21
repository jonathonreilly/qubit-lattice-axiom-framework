#!/usr/bin/env python3
"""Nnseed formation-tick reverse and face in z and y probe frames.

Finite host: Euclidean ball of radius 3 centered at the origin. Two-site seed
{origin, (0,1,0)} locks +e_1 and +e_2 at tick 0. A 6-NN step is allowed iff it
is perpendicular to the parent lock axis. Newly formed sites lock the incoming
step. Uniqueness is not required: all earliest incoming steps are kept.
"""

from __future__ import annotations

import ast
from collections import deque
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/NNSEED_PROBE_FRAME_ISOTROPY_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/NNSEED_PROBE_FRAME_ISOTROPY_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Point = tuple[int, int, int]
ORIGIN: Point = (0, 0, 0)
E1: Point = (1, 0, 0)
E2: Point = (0, 1, 0)
E3: Point = (0, 0, 1)
NN: tuple[Point, ...] = (
    E1,
    (-1, 0, 0),
    E2,
    (0, -1, 0),
    E3,
    (0, 0, -1),
)
BALL_SQ = 9
A_Z: Point = (0, 0, 1)
B_PT: Point = (1, 1, 1)
C_Z: Point = (0, 0, 2)
D_Z: Point = (0, 1, 1)
A_Y: Point = (0, 1, 0)
C_Y: Point = (0, 2, 0)
D_Y: Point = (1, 1, 0)
A_X: Point = (1, 0, 0)
C_X: Point = (2, 0, 0)
FORBIDDEN_NOTE_TOKENS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "Dijkstra",
    "Gram",
    "s^2 census",
    "L1",
)


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def in_ball(site: Point) -> bool:
    return dot(site, site) <= BALL_SQ


def ball_sites() -> frozenset[Point]:
    return frozenset(
        (x, y, z)
        for x in range(-3, 4)
        for y in range(-3, 4)
        for z in range(-3, 4)
        if in_ball((x, y, z))
    )


def perpendicular(lock: Point, step: Point) -> bool:
    return dot(lock, step) == 0


def assignment_string_tuple(tree: ast.AST, name: str) -> tuple[str, ...] | None:
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                try:
                    value = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    return None
                if isinstance(value, tuple) and all(
                    isinstance(item, str) for item in value
                ):
                    return value
                return None
    return None


def form(
    seed: dict[Point, Point] | None = None,
) -> tuple[dict[Point, int], dict[Point, set[Point]]]:
    """Earliest formation ticks and possible incoming locks on B_3(0)."""
    if seed is None:
        seed = {ORIGIN: E1, E2: E2}
    ticks: dict[Point, int] = {site: 0 for site in seed}
    locks: dict[Point, set[Point]] = {site: {letter} for site, letter in seed.items()}
    queue: deque[tuple[Point, int]] = deque((site, 0) for site in seed)
    while queue:
        parent, parent_tick = queue.popleft()
        for lock in tuple(locks[parent]):
            for step in NN:
                if not perpendicular(lock, step):
                    continue
                child = add(parent, step)
                if not in_ball(child):
                    continue
                next_tick = parent_tick + 1
                if child not in ticks:
                    ticks[child] = next_tick
                    locks[child] = {step}
                    queue.append((child, next_tick))
                elif ticks[child] == next_tick:
                    locks[child].add(step)
    return ticks, locks


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__).name))
    literal_paths = assignment_string_tuple(tree, "AUDIT_INPUT_PATHS")

    print("nnseed z/y probe-frame reverse/face on Euclidean B_3(0)")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "claim_scope: nnseed formation-tick reverse and face in z and y "
        "probe frames on Euclidean B_3(0) are reported. Displayed, not adopted."
    )

    checks.check(
        "audit-input-paths-literal",
        literal_paths == AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL),
        str(literal_paths),
    )
    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)

    host = ball_sites()
    checks.check("host-is-euclidean-b3", ORIGIN in host and len(host) == 123 and BALL_SQ == 9)
    checks.check("z-probes-in-host", {A_Z, B_PT, C_Z, D_Z} <= host)
    checks.check("y-probes-in-host", {A_Y, B_PT, C_Y, D_Y} <= host)

    ticks, locks = form()
    t_az = ticks.get(A_Z)
    t_b = ticks.get(B_PT)
    t_cz = ticks.get(C_Z)
    t_dz = ticks.get(D_Z)
    t_ay = ticks.get(A_Y)
    t_cy = ticks.get(C_Y)
    t_dy = ticks.get(D_Y)
    t_ax = ticks.get(A_X)
    t_cx = ticks.get(C_X)

    print(
        f"z-probes t(A_z)={t_az} t(B)={t_b} t(C_z)={t_cz} t(D_z)={t_dz} "
        f"locks(B)={sorted(locks.get(B_PT, ()))} locks(C_z)={sorted(locks.get(C_Z, ()))}"
    )
    print(
        f"y-probes t(A_y)={t_ay} t(B)={t_b} t(C_y)={t_cy} t(D_y)={t_dy} "
        f"locks(C_y)={sorted(locks.get(C_Y, ()))}"
    )

    checks.check(
        "theorem1-z-ticks",
        t_az == 1 and t_b == 2 and t_cz == 4 and t_dz == 1,
        f"{t_az},{t_b},{t_cz},{t_dz}",
    )
    checks.check(
        "theorem1-y-ticks",
        t_ay == 0 and t_b == 2 and t_cy == 3 and t_dy == 1,
        f"{t_ay},{t_b},{t_cy},{t_dy}",
    )
    checks.check(
        "theorem1-ay-is-seed-tick-zero",
        t_ay == 0 and locks[A_Y] == {E2} and ticks[ORIGIN] == 0 and locks[ORIGIN] == {E1},
    )
    checks.check(
        "theorem1-uniqueness-not-required",
        t_b is not None
        and len(locks[B_PT]) == 2
        and locks[B_PT] == {E1, E3}
        and len(locks[C_Z]) == 3
        and len(locks[C_Y]) == 4,
        f"B={sorted(locks.get(B_PT, ()))} Cz={sorted(locks.get(C_Z, ()))} Cy={sorted(locks.get(C_Y, ()))}",
    )
    checks.check(
        "theorem1-not-reprint-of-x-bits",
        (t_az, t_b, t_cz, t_dz) != (t_ax, t_b, t_cx, t_dy)
        and A_Z != A_X
        and C_Z != C_X
        and t_az != t_ax,
        f"z=({t_az},{t_b},{t_cz},{t_dz}) x=({t_ax},{t_b},{t_cx},{t_dy})",
    )

    z_reverse_defined = t_az is not None and t_b is not None
    z_face_defined = t_cz is not None and t_dz is not None
    z_reverse_holds = z_reverse_defined and 3 * t_az * t_az > t_b * t_b
    z_face_holds = z_face_defined and t_cz * t_cz > 2 * t_dz * t_dz
    print(
        "z-reverse: "
        f"{'hold' if z_reverse_holds else 'fail' if z_reverse_defined else 'undefined'} "
        f"(3 t(A_z)^2={3 * t_az * t_az if z_reverse_defined else 'undef'} vs "
        f"t(B)^2={t_b * t_b if z_reverse_defined else 'undef'})"
    )
    print(
        "z-face: "
        f"{'hold' if z_face_holds else 'fail' if z_face_defined else 'undefined'} "
        f"(t(C_z)^2={t_cz * t_cz if z_face_defined else 'undef'} vs "
        f"2 t(D_z)^2={2 * t_dz * t_dz if z_face_defined else 'undef'})"
    )
    checks.check(
        "theorem2-z-reverse-defined-and-fails",
        z_reverse_defined and not z_reverse_holds,
        f"3*{t_az}^2 vs {t_b}^2",
    )
    checks.check(
        "theorem2-z-face-defined-and-holds",
        z_face_holds,
        f"{t_cz}^2 vs 2*{t_dz}^2",
    )

    y_reverse_defined = t_ay is not None and t_b is not None
    y_face_defined = t_cy is not None and t_dy is not None
    y_reverse_holds = y_reverse_defined and 3 * t_ay * t_ay > t_b * t_b
    y_face_holds = y_face_defined and t_cy * t_cy > 2 * t_dy * t_dy
    print(
        "y-reverse: "
        f"{'hold' if y_reverse_holds else 'fail' if y_reverse_defined else 'undefined'} "
        f"(3 t(A_y)^2={3 * t_ay * t_ay if y_reverse_defined else 'undef'} vs "
        f"t(B)^2={t_b * t_b if y_reverse_defined else 'undef'})"
    )
    print(
        "y-face: "
        f"{'hold' if y_face_holds else 'fail' if y_face_defined else 'undefined'} "
        f"(t(C_y)^2={t_cy * t_cy if y_face_defined else 'undef'} vs "
        f"2 t(D_y)^2={2 * t_dy * t_dy if y_face_defined else 'undef'})"
    )
    checks.check(
        "theorem3-y-reverse-defined-and-fails",
        y_reverse_defined and not y_reverse_holds,
        f"3*{t_ay}^2 vs {t_b}^2",
    )
    checks.check(
        "theorem3-y-face-defined-and-holds",
        y_face_holds,
        f"{t_cy}^2 vs 2*{t_dy}^2",
    )

    one_site_ticks, _ = form(seed={ORIGIN: E1})
    checks.check(
        "mutation-one-site-seed-changes-z-ticks",
        (
            one_site_ticks.get(A_Z),
            one_site_ticks.get(B_PT),
            one_site_ticks.get(C_Z),
            one_site_ticks.get(D_Z),
        )
        != (t_az, t_b, t_cz, t_dz),
        str(
            (
                one_site_ticks.get(A_Z),
                one_site_ticks.get(B_PT),
                one_site_ticks.get(C_Z),
                one_site_ticks.get(D_Z),
            )
        ),
    )
    checks.check("formation-stays-in-host", set(ticks) <= host)
    checks.check("seed-does-not-reform-ay", ticks[A_Y] == 0)

    claim_scope = (
        "nnseed formation-tick reverse and face in z and y probe frames "
        "on Euclidean B_3(0) are reported. Displayed, not adopted."
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "note-reports-z-and-y-ticks",
        "t(A_z)=t(0,0,1)=1" in note
        and "t(B)=t(1,1,1)=2" in note
        and "t(C_z)=t(0,0,2)=4" in note
        and "t(D_z)=t(0,1,1)=1" in note
        and "t(A_y)=t(0,1,0)=0" in note
        and "t(C_y)=t(0,2,0)=3" in note
        and "t(D_y)=t(1,1,0)=1" in note,
    )
    checks.check(
        "note-z-reverse-fail-face-hold",
        "z-reverse fails" in note and "z-face holds" in note,
    )
    checks.check(
        "note-y-reverse-fail-face-hold",
        "y-reverse fails" in note and "y-face holds" in note,
    )
    checks.check(
        "note-displayed-not-adopted",
        "displayed, not adopted" in note.lower()
        and "not written into Admissibility" in note,
    )
    checks.check(
        "note-forbids-enlargement-and-cache",
        "No larger host is used." in note
        and "B_3(0)" in note
        and "No runner cache is written." in note,
    )
    checks.check(
        "note-not-x-reprint",
        "not a reprint of the x-frame probes" in note,
    )
    checks.check(
        "note-forbidden-tokens-absent",
        all(token not in note for token in FORBIDDEN_NOTE_TOKENS),
    )
    checks.check(
        "axiom-record-sentences-current",
        "Records form." in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "Physical sites are the points of the cubic lattice `Z^3`" in axiom,
    )
    checks.check(
        "note-machine-status-no-axiom-edit",
        "hypothetical_axiom_status: no edit" in note
        and "claim_type: bounded_theorem" in note,
    )
    checks.check(
        "source-audit-paths-are-static-literals",
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/NNSEED_PROBE_FRAME_ISOTROPY_REVERSE_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
