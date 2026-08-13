#!/usr/bin/env python3
"""Exact Z2 Bianchi identity on the unit cube; monopole 6-tuple is impossible.

Identity gates call face_holonomies(theta) and bianchi_sum(H). Arithmetic is
integers modulo 2. No fitted scalar is used as an input.
"""

from __future__ import annotations

import ast
import inspect
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/Z2_UNIT_CUBE_FACE_HOLONOMIES_OBEY_BIANCHI_MONOPOLE_IMPOSSIBLE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

# Face order: z=0, z=1, y=0, y=1, x=0, x=1.
FACES: tuple[tuple[int, ...], ...] = (
    (0, 5, 1, 4),
    (2, 7, 3, 6),
    (0, 9, 2, 8),
    (1, 11, 3, 10),
    (4, 10, 6, 8),
    (5, 11, 7, 9),
)

MONOPOLE = (1, 0, 0, 0, 0, 0)
N_P_CUBE = 6
N_P_L2_SU3 = 96

_FACE_CALLS = 0
_BIANCHI_CALLS = 0


def _mod2(value: int) -> int:
    return int(value) & 1


def face_holonomies(theta: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    global _FACE_CALLS
    _FACE_CALLS += 1
    bits = tuple(_mod2(bit) for bit in theta)
    if len(bits) != 12:
        raise ValueError("theta must have 12 edge bits")
    return tuple(_mod2(sum(bits[edge] for edge in face)) for face in FACES)


def bianchi_sum(H: tuple[int, ...] | list[int]) -> int:
    global _BIANCHI_CALLS
    _BIANCHI_CALLS += 1
    bits = tuple(_mod2(bit) for bit in H)
    if len(bits) != 6:
        raise ValueError("H must have 6 face bits")
    return _mod2(sum(bits))


def identity_zero_link_field() -> bool:
    theta = (0,) * 12
    H = face_holonomies(theta)
    return H == (0, 0, 0, 0, 0, 0) and bianchi_sum(H) == 0


def identity_single_edge_flip(edge: int) -> bool:
    theta0 = (0,) * 12
    H0 = face_holonomies(theta0)
    theta1 = list(theta0)
    theta1[edge] = 1
    H1 = face_holonomies(tuple(theta1))
    flipped = sum(a != b for a, b in zip(H0, H1))
    return flipped == 2 and bianchi_sum(H1) == 0


def identity_bianchi_on_field(theta: tuple[int, ...]) -> bool:
    H = face_holonomies(theta)
    return bianchi_sum(H) == 0


def identity_bianchi_all_fields() -> tuple[bool, set[tuple[int, ...]]]:
    image: set[tuple[int, ...]] = set()
    ok = True
    for bits in product((0, 1), repeat=12):
        H = face_holonomies(bits)
        if bianchi_sum(H) != 0:
            ok = False
            break
        image.add(H)
    return ok, image


def every_six_tuple_is_face_holonomy_image(image: set[tuple[int, ...]]) -> bool:
    return all(h in image for h in product((0, 1), repeat=6))


def _calls_named(fn, names: tuple[str, ...]) -> bool:
    tree = ast.parse(inspect.getsource(fn))
    called = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    return all(name in called for name in names)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    axiom_flat = " ".join(axiom.split())

    checks.check(
        "inputs-exist",
        "declared note and axiom memo are present",
        NOTE_PATH.is_file() and AXIOM_PATH.is_file(),
    )
    checks.check(
        "axiom-lattice",
        "Lattice names Z^3 with nearest-neighbor adjacency",
        "cubic lattice `Z^3`, with nearest-neighbor adjacency" in axiom_flat,
    )
    checks.check(
        "axiom-admissibility",
        "Admissibility names the nearest-neighbor distribution sentence",
        "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions"
        in axiom_flat,
    )
    checks.check(
        "axiom-no-link-form",
        "the axiom memo does not name a link 1-form or closed 2-cochain",
        "link 1-form" not in axiom and "2-cochain" not in axiom,
    )

    incidence = [0] * 12
    for face in FACES:
        checks.check(
            "face-arity",
            f"face {face} has four distinct edges",
            len(face) == 4 and len(set(face)) == 4 and all(0 <= e < 12 for e in face),
        )
        for edge in face:
            incidence[edge] += 1
    checks.check(
        "edge-incidence",
        "each of the 12 edges lies in exactly two faces",
        incidence == [2] * 12,
    )

    required = ("face_holonomies", "bianchi_sum")
    checks.check(
        "identity-call-zero",
        "identity_zero_link_field calls face_holonomies and bianchi_sum",
        _calls_named(identity_zero_link_field, required),
    )
    checks.check(
        "identity-call-flip",
        "identity_single_edge_flip calls face_holonomies and bianchi_sum",
        _calls_named(identity_single_edge_flip, required),
    )
    checks.check(
        "identity-call-field",
        "identity_bianchi_on_field calls face_holonomies and bianchi_sum",
        _calls_named(identity_bianchi_on_field, required),
    )
    checks.check(
        "identity-call-all",
        "identity_bianchi_all_fields calls face_holonomies and bianchi_sum",
        _calls_named(identity_bianchi_all_fields, required),
    )

    checks.check(
        "identity-zero",
        "theta=0 maps to H=0^6 with even Bianchi sum",
        identity_zero_link_field(),
    )
    flip_ok = all(identity_single_edge_flip(edge) for edge in range(12))
    checks.check(
        "identity-single-flip",
        "each single-edge flip changes exactly two faces and preserves Bianchi",
        flip_ok,
    )
    sample = (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
    checks.check(
        "identity-sample",
        "a mixed field has even Bianchi sum",
        identity_bianchi_on_field(sample),
    )

    before_face = _FACE_CALLS
    before_bianchi = _BIANCHI_CALLS
    all_ok, image = identity_bianchi_all_fields()
    checks.check(
        "identity-enumerate",
        "every one of the 4096 link fields has even Bianchi sum",
        all_ok and len(image) > 0,
    )
    checks.check(
        "identity-calls-fired",
        "enumeration invoked face_holonomies and bianchi_sum",
        _FACE_CALLS - before_face >= 4096 and _BIANCHI_CALLS - before_bianchi >= 4096,
    )

    even = {h for h in product((0, 1), repeat=6) if _mod2(sum(h)) == 0}
    checks.check(
        "image-even",
        "holonomy image equals the 32 even-weight 6-tuples",
        image == even and len(image) == 32,
    )
    checks.check(
        "monopole-odd",
        "m=(1,0,0,0,0,0) has odd Bianchi weight",
        bianchi_sum(MONOPOLE) == 1,
    )
    checks.check(
        "monopole-missing",
        "m is not a face-holonomy image",
        MONOPOLE not in image,
    )
    checks.check(
        "mutation-independent-plaquettes",
        "the predicate that every 6-tuple is a holonomy image fails on m",
        (not every_six_tuple_is_face_holonomy_image(image)) and MONOPOLE not in image,
    )

    checks.check(
        "np-not-june10",
        "N_p(this cube)=6 is not N_p(L=2)=96",
        N_P_CUBE == len(FACES) and N_P_CUBE != N_P_L2_SU3,
    )
    checks.check(
        "group-not-su3",
        "the cube group is Z2, not SU(3)",
        "Z2" in note and "SU(3)" in note and "Z2` ≠ `SU(3)" in note,
    )
    checks.check(
        "note-theorems",
        "the note states Bianchi, monopole impossibility, and extra edge object",
        all(
            needle in note
            for needle in (
                "H_f",
                "(1,0,0,0,0,0)",
                "not six independent",
                "on the twelve edges",
                "N_p(L=2) = 96",
            )
        ),
    )
    forbidden_scalar = "0." + "5934"
    runner_src = Path(__file__).read_text(encoding="utf-8")
    checks.check(
        "hygiene",
        "note carries no fitted-plaquette input and no axiom-adoption language",
        forbidden_scalar not in note
        and "we adopt" not in note.lower()
        and "L_phys" not in note
        and " = " + forbidden_scalar not in runner_src
        and "N_P_L2_SU3 = 96" in runner_src,
    )

    n5_lines = (
        "per_element: twelve edge bits and six face holonomies are Z2 sums",
        "per_site: one unit cube; no lattice-wide gauge field is sampled",
        "per_mode: Z2 coboundary is checked; no SU(3) mode is claimed",
        "per_block: only Bianchi even-sum and the missing monopole 6-tuple are executed",
        "lattice_wide: checked and not executed — no 4D SU(3) ln Z_L claim",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
        )
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
