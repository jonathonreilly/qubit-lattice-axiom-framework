#!/usr/bin/env python3
"""Verifier for the ambient equivariant heat-trace face note."""
from __future__ import annotations
import itertools
import math
import re
from fractions import Fraction
from pathlib import Path
import numpy as np
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md"
FIXED = ROOT / "docs" / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
RUNNER_NAME = "scripts/acphilambda_ambient_equivariant_heat_trace_face_2026_07_02.py"
PASS = 0
FAIL = 0

def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        line = f"[PASS] {name}"
    else:
        FAIL += 1
        line = f"[FAIL] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return bool(ok)

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def rotate_label(m: tuple[int, int, int], power: int, N: int) -> tuple[int, int, int]:
    a = tuple(x % N for x in m)
    for _ in range(power % 3):
        a = (a[2], a[0], a[1])
    return a

def c4_label(m: tuple[int, int, int], N: int) -> tuple[int, int, int]:
    return (m[1] % N, (-m[0]) % N, m[2] % N)

def diagonal_set(N: int) -> set[tuple[int, int, int]]:
    return {(m, m, m) for m in range(N)}

def fixed_set(N: int, power: int) -> set[tuple[int, int, int]]:
    return {
        m
        for m in itertools.product(range(N), repeat=3)
        if rotate_label(m, power, N) == tuple(x % N for x in m)
    }

def c4_fixed_set(N: int) -> set[tuple[int, int, int]]:
    return {
        m
        for m in itertools.product(range(N), repeat=3)
        if c4_label(m, N) == tuple(x % N for x in m)
    }

def one_dim_character_sum(N: int, diff: int) -> int:
    return N if diff % N == 0 else 0

def character_sum(N: int, m: tuple[int, int, int], power: int) -> int:
    image = rotate_label(m, power, N)
    diffs = [a - b for a, b in zip(m, image)]
    out = 1
    for d in diffs:
        out *= one_dim_character_sum(N, d)
    return out

def positions(N: int) -> list[tuple[int, int, int]]:
    return [(x, y, z) for x in range(N) for y in range(N) for z in range(N)]

def site_index(N: int, p: tuple[int, int, int]) -> int:
    x, y, z = p
    return (x * N + y) * N + z

def rotate_site(p: tuple[int, int, int], power: int, N: int) -> tuple[int, int, int]:
    a = tuple(x % N for x in p)
    for _ in range(power % 3):
        a = (a[2], a[0], a[1])
    return a

def dense_laplacian(N: int) -> np.ndarray:
    n = N**3
    L = np.zeros((n, n), dtype=float)
    for x, y, z in positions(N):
        a = site_index(N, (x, y, z))
        L[a, a] = 6.0
        for dx, dy, dz in (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ):
            b = site_index(N, ((x + dx) % N, (y + dy) % N, (z + dz) % N))
            L[a, b] -= 1.0
    return L

def dense_rotation(N: int, power: int) -> np.ndarray:
    n = N**3
    U = np.zeros((n, n), dtype=float)
    for p in positions(N):
        a = site_index(N, p)
        b = site_index(N, rotate_site(p, power, N))
        U[b, a] = 1.0
    return U

def diagonal_sum(N: int, t: float, wrong: bool = False) -> float:
    if wrong:
        return sum(math.exp(-t * (6.0 - 2.0 * math.cos(2.0 * math.pi * m / N))) for m in range(N))
    return sum(math.exp(-t * (6.0 - 6.0 * math.cos(2.0 * math.pi * m / N))) for m in range(N))

def full_heat_trace(N: int, t: float) -> float:
    total = 0.0
    for m in itertools.product(range(N), repeat=3):
        k = [2.0 * math.pi * a / N for a in m]
        total += math.exp(-t * (6.0 - 2.0 * sum(math.cos(x) for x in k)))
    return total

def axis_amplitude(t: float) -> tuple[int, float]:
    N = math.ceil(12.0 * math.sqrt(t))
    total = sum(math.exp(-t * (6.0 - 6.0 * math.cos(2.0 * math.pi * m / N))) for m in range(N))
    return N, total / N

def source_checks() -> None:
    print("\n-- Source and note pins --")
    note = read(NOTE)
    fixed = read(FIXED)
    axioms = read(AXIOMS)
    fixed_flat = flat(fixed)
    axioms_flat = flat(axioms)
    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor "
        "adjacency, standard translations, and proper cubic rotations."
    )
    check("note exists", NOTE.exists())
    check("fixed-locus source exists", FIXED.exists())
    check("axioms memo exists", AXIOMS.exists())
    check("fixed-locus local density pin exists", "forced and gives local density `2/9`" in fixed)
    check("fixed-locus readout exclusion pin exists", "does **not** supply the physical single-summand readout" in fixed)
    check("axioms lattice sentence exists", lattice_sentence in axioms_flat)
    check("note quotes local density pin", "forced and gives local density `2/9`" in note)
    check("note quotes readout exclusion pin", "does **not**" in note and "supply the physical single-summand readout" in note)
    check("note quotes lattice sentence", lattice_sentence in flat(note))

def exact_reduction_checks() -> None:
    print("\n-- T7-1 exact diagonal-momentum reduction --")
    for N in (3, 4, 5):
        diag = diagonal_set(N)
        f1 = fixed_set(N, 1)
        f2 = fixed_set(N, 2)
        check(f"N={N}: R fixed momenta are diagonal", f1 == diag, f"count={len(f1)}")
        check(f"N={N}: R^2 fixed momenta are diagonal", f2 == diag, f"count={len(f2)}")
        check(f"N={N}: R and R^2 fixed sets coincide", f1 == f2)
    for N in (3, 4):
        for power in (1, 2):
            fixed_m = (1 % N, 1 % N, 1 % N)
            off_m = (1 % N, 0, 0)
            check(f"N={N}, j={power}: fixed character sum is N^3", character_sum(N, fixed_m, power) == N**3)
            check(f"N={N}, j={power}: off-diagonal character sum vanishes", character_sum(N, off_m, power) == 0)
    c4_count = len(c4_fixed_set(4))
    check("C4 discriminator fixed count differs from C3 diagonal count", c4_count != 4, f"C4 count={c4_count}")
    check("C4 discriminator computed exact count", c4_count == 8)
    check("identity component gives full trace, not diagonal sum", abs(full_heat_trace(4, 1.0) - diagonal_sum(4, 1.0)) > 1e-3)

def numeric_trace_checks() -> None:
    print("\n-- T7-1 dense numeric confirmations --")
    for N in (4, 5, 6):
        L = dense_laplacian(N)
        w, V = np.linalg.eigh(L)
        U = dense_rotation(N, 1)
        for t in (0.3, 1.0, 3.0):
            heat = (V * np.exp(-t * w)) @ V.T
            dense = float(np.trace(heat @ U))
            diag = diagonal_sum(N, t)
            check(f"N={N}, t={t}: dense trace equals diagonal sum", abs(dense - diag) < 1e-9, f"err={abs(dense - diag):.3e}")
    check("anchor N=4,t=0.3", abs(diagonal_sum(4, 0.3) - 1.357921498890) < 1e-9)
    check("anchor N=6,t=1.0", abs(diagonal_sum(6, 1.0) - 1.099827100556) < 1e-9)
    check("wrong dispersion breaks N=4,t=0.3", abs(diagonal_sum(4, 0.3, wrong=True) - diagonal_sum(4, 0.3)) > 1e-3)
    check("wrong dispersion breaks N=6,t=1.0", abs(diagonal_sum(6, 1.0, wrong=True) - diagonal_sum(6, 1.0)) > 1e-3)

def continuum_checks() -> None:
    print("\n-- T7-2 continuum bookkeeping --")
    ts = (25.0, 100.0, 400.0)
    data = []
    for t in ts:
        N, A = axis_amplitude(t)
        err = abs(math.sqrt(12.0 * math.pi * t) * A - 1.0)
        lef_err = abs(math.sqrt(4.0 * math.pi * t) * A / math.sqrt(3.0) - (1.0 / 3.0))
        site = math.sqrt(4.0 * math.pi * t) * A
        unit = site / math.sqrt(3.0)
        data.append((t, N, A, err, lef_err, site, unit))
        check(f"t={int(t)}: torus size follows ceil(12 sqrt(t))", N == math.ceil(12.0 * math.sqrt(t)), f"N={N}")
    errs = [x[3] for x in data]
    lef_errs = [x[4] for x in data]
    ratios = [errs[0] / errs[1], errs[1] / errs[2]]
    lef_ratios = [lef_errs[0] / lef_errs[1], lef_errs[1] / lef_errs[2]]
    check("per-site continuum error strictly decreases", errs[0] > errs[1] > errs[2], str(errs))
    check("per-site continuum ratios discriminate", all(2.5 <= r <= 6.0 for r in ratios), str(ratios))
    check("per-length Lefschetz error strictly decreases", lef_errs[0] > lef_errs[1] > lef_errs[2], str(lef_errs))
    check("per-length Lefschetz ratios discriminate", all(2.5 <= r <= 6.0 for r in lef_ratios), str(lef_ratios))
    check("per-unit-length value approaches 1/3", abs(data[-1][6] - (1.0 / 3.0)) < 1e-4, f"value={data[-1][6]:.12f}")
    check("per-site value approaches 1/sqrt(3)", abs(data[-1][5] - (1.0 / math.sqrt(3.0))) < 1e-4, f"value={data[-1][5]:.12f}")
    check("normalization discriminator separates 1/sqrt(3) from 1/3", abs((1.0 / math.sqrt(3.0)) - (1.0 / 3.0)) > 0.24)
    check("only per-unit-length is near 1/3", abs(data[-1][6] - (1.0 / 3.0)) < 1e-4 and abs(data[-1][5] - (1.0 / 3.0)) > 0.1)
    ratio_exact = sp.simplify((1 / sp.sqrt(3)) / sp.Rational(1, 3) - sp.sqrt(3))
    check("exact normalization ratio is sqrt(3)", ratio_exact == 0)

def face_wiring_checks() -> None:
    print("\n-- T7-3 exact face wiring --")
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    core = sp.simplify((omega - 1) * (omega**2 - 1))
    check("omega core identity equals 3", core == 3, str(core))
    factors = [
        sp.nsimplify(sp.simplify(1 / ((omega**j - 1) * sp.conjugate(omega**j - 1))))
        for j in (1, 2)
    ]
    check("j=1 transverse factor derives to 1/3", factors[0] == sp.Rational(1, 3), str(factors[0]))
    check("j=2 transverse factor derives to 1/3", factors[1] == sp.Rational(1, 3), str(factors[1]))
    s_sum = sp.nsimplify(factors[0] + factors[1])
    l3 = sp.nsimplify(s_sum / 3)
    check("unaveraged nontrivial-sector sum derives to 2/3", s_sum == sp.Rational(2, 3))
    check("C3 group average derives to 2/9 (fixed-locus value)", l3 == sp.Rational(2, 9))
    check("wrong-member rejector L3 != 1/9", l3 != sp.Rational(1, 9))
    check(
        "wrong-weight rejector: (1,1)-pair per-mode factor is not real-positive 1/3",
        sp.simplify(1 / (omega - 1) ** 2 - sp.Rational(1, 3)) != 0,
    )
    lam = sp.symbols("lambda_unit", positive=True)
    a_site = sp.symbols("a_site", positive=True)
    per_length = a_site / (sp.sqrt(3) * lam)
    check(
        "PR #4783 rescale obstruction persists on the ambient normalization",
        sp.simplify(per_length.subs(lam, 2 * lam) - per_length / 2) == 0
        and sp.simplify(a_site / (sp.sqrt(3) * 1) / a_site - 1 / sp.sqrt(3)) == 0,
    )

def note_discipline_checks() -> None:
    print("\n-- Note discipline --")
    note = read(NOTE)
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note)
    md_links = [x for x in links if x.endswith(".md")]
    runner_links = [x for x in links if x.endswith(".py")]
    verbatim = [
        "the fixed-locus density acquires its ambient face: the nontrivial-sector group average of the per-unit-`[111]`-length equivariant heat-trace amplitudes of the `Z^3` lattice",
        "the unit junction persists verbatim in ambient coordinates: per-site versus per-unit-length is a `sqrt(3)` rescale of the density normalization",
        "nothing here derives the physical normalization or the phase value",
        "not a terminal no-go",
    ]
    forbidden = [
        "only " + "route",
        "last " + "route",
        "exhausted",
        "closes the " + "route",
        "P" + "DG",
        "new " + "wall",
    ]
    leaks = [
        "Acceptance " + "contract",
        "PRESERVE " + "VERBATIM",
        "MUST BE " + "ABSENT",
        "Files to " + "produce",
        "ANTI-" + "FABRICATION",
        "Spec " + "AMBIENT",
        "execute it " + "exactly",
    ]
    allowed_walls = {"W_cycle_holonomy_value", "W_defect_identity_unit", "W_defect_readout_selection"}
    walls = set(re.findall(r"\bW_[A-Za-z0-9_]+\b", note))
    check("three required ambient-face sentences and no-go sentence appear", all(s in note for s in verbatim))
    check("N1 through N8 headers appear", all(f"### N{i}" in note for i in range(1, 9)))
    check("forbidden route/status phrases absent", not any(s in note for s in forbidden))
    check("wall labels are whitelisted", walls <= allowed_walls, str(sorted(walls)))
    check("status-authority header is present", "**Status authority:** independent audit lane only." in note)
    check("exactly two markdown links appear", len(links) == 2, str(links))
    check("exactly one markdown dependency target appears", len(md_links) == 1 and Path(md_links[0]).name == FIXED.name, str(md_links))
    check("runner link is present", len(runner_links) == 1 and RUNNER_NAME in runner_links[0], str(runner_links))
    check("axioms memo is inline text, not a link", "MINIMAL_AXIOMS_2026-06-29.md" in note and all("MINIMAL_AXIOMS" not in x for x in links))
    check("in-flight PR identifiers are backticked", all(f"`PR #{n}" in note for n in (4783, 4788, 4789, 4790, 4794, 4798)))
    check("in-flight PR identifiers are not link targets", not any("ACPHILAMBDA_" in x for x in links))
    check("spec leakage phrases absent from note", not any(s in note for s in leaks))
    check("audit-grade authorship phrases absent", "retained_bounded" not in note and "audit-retained" not in note)
    check("verification command is recorded", f"python3 {RUNNER_NAME}" in note)
    check("verification close is recorded", "TOTAL: PASS=" in note and "FAIL=0" in note)

def main() -> int:
    source_checks()
    exact_reduction_checks()
    numeric_trace_checks()
    continuum_checks()
    face_wiring_checks()
    note_discipline_checks()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 and PASS >= 55 else 1

if __name__ == "__main__":
    raise SystemExit(main())
