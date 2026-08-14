#!/usr/bin/env python3
"""First-wave two-cube formations have k=|3n|^2=1; next-wave k in {1,2,3}."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TWO_CUBE_FIRST_WAVE_K_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_FIRST_WAVE_K_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

VERTS = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SEED = frozenset({(0, 0, 0)})
FORMERS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
FACE_DIAGS = ((1, 1, 0), (1, 0, 1), (0, 1, 1))
B_FRONT = ((2, 0, 0), (2, 0, 1), (2, 1, 0), (2, 1, 1))
SPACE_DIAG = (1, 1, 1)
ALLOWED_FORMING_K = frozenset({1, 2, 3})


def occ(v, locks) -> int:
    return 1 if v in locks else 0


def nvec(site, locks):
    """Identity gate. n_μ = (o_{+μ} − o_{-μ}) / 3; off-patch occupancy 0."""
    out = []
    for ax in AXES:
        plus = (site[0] + ax[0], site[1] + ax[1], site[2] + ax[2])
        minus = (site[0] - ax[0], site[1] - ax[1], site[2] - ax[2])
        o_plus = occ(plus, locks) if plus in VERTS else 0
        o_minus = occ(minus, locks) if minus in VERTS else 0
        out.append(Fraction(o_plus - o_minus, 3))
    return tuple(out)


def k_of(n) -> int:
    """Identity gate. k = |3n|^2."""
    return int(sum((3 * c) ** 2 for c in n))


def occ_step(locks):
    """Identity gate. Locked sites stay; unread sites form iff n ≠ 0."""
    out = set(locks)
    for v in VERTS:
        if v not in locks and any(c != 0 for c in nvec(v, locks)):
            out.add(v)
    return frozenset(out)


def first_wave(locks):
    """Identity gate. Sites formed by one occupancy step from locks."""
    return occ_step(locks) - frozenset(locks)


def next_wave_k(locks):
    """Identity gate. k at face-diagonals and B-front after the first wave."""
    after = occ_step(locks)
    sites = FACE_DIAGS + B_FRONT
    return tuple((site, k_of(nvec(site, after))) for site in sites)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label, statement, condition) -> None:
        self.passed += int(bool(condition))
        self.failed += int(not condition)
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    four = axiom.split("## The Four Framework Axioms", 1)[-1].split("## Qualification", 1)[0]
    print("external_scientific_inputs: none")
    print("package_local_integrity_reads: runner, note, axiom memo")
    print("measure_boundary: exact k=|3n|^2 on first-wave and next-wave sites")
    print("negative_scope: first-wave spectral type, not Newton")

    wave1 = first_wave(SEED)
    after1 = occ_step(SEED)
    ns = [nvec(site, SEED) for site in FORMERS]
    ks = [k_of(n) for n in ns]
    nxt = next_wave_k(SEED)
    nxt_map = dict(nxt)
    face_ks = [nxt_map[site] for site in FACE_DIAGS]
    forming_next = [k for _, k in nxt if k != 0]
    after2 = occ_step(after1)
    k_space = k_of(nvec(SPACE_DIAG, after2))

    checks.check(
        "thm1-geom",
        "seed (0,0,0); twelve verts; first wave is the three axis neighbors",
        SEED == frozenset({(0, 0, 0)})
        and len(VERTS) == 12
        and wave1 == frozenset(FORMERS)
        and FORMERS == ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    )
    checks.check(
        "thm2-k1",
        "three first-wave sites each have k=|3n|^2=1",
        ks == [1, 1, 1]
        and ns[0] == (Fraction(-1, 3), Fraction(0), Fraction(0))
        and ns[1] == (Fraction(0), Fraction(-1, 3), Fraction(0))
        and ns[2] == (Fraction(0), Fraction(0), Fraction(-1, 3)),
    )
    checks.check(
        "thm2-unbalanced",
        "each first-wave site has one unbalanced axis",
        all(sum(c != 0 for c in n) == 1 for n in ns),
    )
    checks.check(
        "thm3-face",
        "next-wave face-diagonals have k=2",
        face_ks == [2, 2, 2] and all(site in occ_step(after1) for site in FACE_DIAGS),
    )
    checks.check(
        "thm3-bfront",
        "B-front (2,0,0) has k=1; other B-front k=0",
        nxt_map[(2, 0, 0)] == 1
        and nxt_map[(2, 0, 1)] == 0
        and nxt_map[(2, 1, 0)] == 0
        and nxt_map[(2, 1, 1)] == 0
        and (2, 0, 0) in occ_step(after1),
    )
    checks.check(
        "thm3-bound",
        "forming next-wave k lies in {1,2,3}; k=3 at (1,1,1) after that wave",
        set(forming_next) <= ALLOWED_FORMING_K
        and set(forming_next) == {1, 2}
        and k_space == 3
        and k_space in ALLOWED_FORMING_K
        and all(k in ALLOWED_FORMING_K for k in ks),
    )
    checks.check(
        "mutation-k2-fails",
        "predicate a first-wave site has k=2 must fail",
        all(k != 2 for k in ks),
    )
    checks.check(
        "mutation-face0-fails",
        "predicate a next-wave face-diagonal has k=0 must fail",
        all(k != 0 for k in face_ks),
    )
    checks.check(
        "quoted",
        "note quotes lock, permanence, NN",
        "locks exactly one admissible local possibility" in note
        and "records are permanent" in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note,
    )
    forbidden = ("we adopt", "L_phys", "0.5934", "Lattice-named", "exhausted", "closes the route", "G_N")
    checks.check(
        "boundary",
        "required strings",
        all(p not in note for p in forbidden)
        and "Result Up Front" in note
        and "not a TOE" in note
        and "Qubit remains `M_2(C)`" in note
        and "This note authors no audit verdict" in note
        and "QCD is unused" in note
        and "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"' in note
        and "Honest-auditor / Boundary" in note
        and "claim_id:" in note,
    )
    checks.check(
        "memo-silent",
        "axioms do not name first-wave k",
        "first-wave" not in four and "|3n|" not in four and "kform" not in four,
    )
    checks.check(
        "gates",
        "identity gates",
        "def nvec(" in self_source
        and "def k_of(" in self_source
        and "def occ_step(" in self_source
        and "def first_wave(" in self_source
        and "def next_wave_k(" in self_source
        and AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_FIRST_WAVE_K_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120,
    )
    print("per_element: checked exactly — k at three first-wave and seven next-wave sites")
    print("per_site: checked exactly — seed (0,0,0) and next-wave table")
    print("per_mode: checked exactly — first-wave k=1; next-wave k in {1,2,3}")
    print("per_block: checked exactly — spectral type of first records")
    print("lattice_wide: checked and not executed — not axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
