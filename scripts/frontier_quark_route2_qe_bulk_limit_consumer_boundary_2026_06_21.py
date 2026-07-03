#!/usr/bin/env python3
"""Route-2 q_E bulk-limit consumer boundary.

This runner is intentionally cache-first for the heavy box-size scan. It checks
that the existing SHA-pinned scan output is fresh, then verifies the downstream
consumer conclusion:

* the measured-calibration bulk-limit route to q_E=15/8 is pruned;
* the S3 primitive-chain gate remains a fixed-carrier readout selector problem;
* no endpoint closure, audit verdict, or retained-status movement is claimed.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CACHE = ROOT / "logs" / "runner-cache"

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)
    return ok


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def contains_all(text: str, phrases: list[str]) -> bool:
    return all(phrase in text for phrase in phrases)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_cache_header(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for key in ("runner", "runner_sha256", "exit_code", "status"):
        m = re.search(rf"^{key}:\s*(.+?)\s*$", text, flags=re.MULTILINE)
        if m:
            out[key] = m.group(1)
    return out


def parse_box_rows(cache_text: str) -> dict[int, tuple[float, float]]:
    rows: dict[int, tuple[float, float]] = {}
    row_re = re.compile(
        r"^\s*(\d+)\s+"
        r"[-+0-9.eE]+\s+[-+0-9.eE]+\s+"
        r"[-+0-9.eE]+\s+[-+0-9.eE]+\s+"
        r"[-+0-9.eE]+\s+[-+0-9.eE]+\s+"
        r"([-+0-9.]+)\s+([-+0-9.]+)\s*$",
        flags=re.MULTILINE,
    )
    for m in row_re.finditer(cache_text):
        rows[int(m.group(1))] = (float(m.group(2)), float(m.group(3)))
    return rows


def main() -> int:
    print("ROUTE-2 q_E BULK-LIMIT CONSUMER BOUNDARY")
    print("=" * 78)

    paths = {
        "new_note": DOCS / "QUARK_ROUTE2_QE_BULK_LIMIT_CONSUMER_BOUNDARY_NOTE_2026-06-21.md",
        "primitive": DOCS / "S3_TIME_PRIMITIVE_CHAIN_NOTE.md",
        "theta_slice": DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        "measured": DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
        "box_note": DOCS / "QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md",
        "naturality": DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        "readout": DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        "box_runner": ROOT / "scripts" / "frontier_quark_route2_qe_box_size_scan_2026_06_10.py",
        "box_cache": CACHE / "frontier_quark_route2_qe_box_size_scan_2026_06_10.txt",
    }

    print()
    print("A. Source surfaces")
    print("-" * 78)
    for label, path in paths.items():
        check(f"{label} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(paths["new_note"])
    primitive = read(paths["primitive"])
    theta_slice = read(paths["theta_slice"])
    measured = read(paths["measured"])
    box_note = read(paths["box_note"])
    naturality = read(paths["naturality"])
    readout = read(paths["readout"])
    cache_text = read(paths["box_cache"])

    print()
    print("B. Existing owner-row and direct-consumer boundaries")
    print("-" * 78)
    check(
        "primitive-chain note names beta_E/alpha_E=21/4 as the open entry",
        "beta_E / alpha_E = 21/4" in primitive
        and "open primitive" in primitive
        and "new E-center/source/readout primitive" in primitive,
    )
    check(
        "theta-to-slice consumer remains blocked by the endpoint triple",
        "endpoint triple" in theta_slice
        and "not yet derived" in theta_slice
        and "unique exact `Theta_R -> Lambda_R` coupling theorem" in theta_slice,
    )
    check(
        "readout note localizes the missing map entry",
        "beta_E / alpha_E = 21/4" in readout
        and "exact missing-map obstruction" in readout
        and "restricted carrier class" in readout,
    )
    check(
        "naturality no-go states rho_E remains free without extra structure",
        "remains a free parameter" in naturality
        and "additional E-center endpoint ratio" in naturality
        and (
            "stronger readout primitive" in naturality
            or "readout-map primitive" in naturality
        ),
    )

    print()
    print("C. Box-size cache freshness and scan facts")
    print("-" * 78)
    header = parse_cache_header(cache_text)
    current_sha = sha256(paths["box_runner"])
    check(
        "box-size scan cache is SHA-fresh",
        header.get("runner_sha256") == current_sha,
        f"cache={header.get('runner_sha256', '')[:16]} current={current_sha[:16]}",
    )
    check(
        "box-size scan cache is successful",
        header.get("status") == "ok" and header.get("exit_code") == "0",
        f"status={header.get('status')} exit_code={header.get('exit_code')}",
    )
    check(
        "box-size scan reported PASS=7 FAIL=0",
        "TOTAL: PASS=7 FAIL=0" in cache_text,
    )

    rows = parse_box_rows(cache_text)
    check(
        "box-size scan table parses the expected N values",
        {11, 13, 15, 17, 19, 21, 25, 29}.issubset(rows),
        f"N={sorted(rows)}",
    )
    q_t_15, q_e_15 = rows[15]
    check(
        "N=15 reproduces the finite-box target neighborhood",
        abs(q_t_15 - float(Fraction(5, 6))) < 1e-4
        and abs(q_e_15 - float(Fraction(15, 8))) < 2e-3,
        f"q_T(15)={q_t_15:.6f}, q_E(15)={q_e_15:.6f}",
    )
    check(
        "fixed-radius q_T sign-flips after N=15",
        rows[15][0] > 0 and rows[17][0] < 0,
        f"q_T(15)={rows[15][0]:+.5f}, q_T(17)={rows[17][0]:+.5f}",
    )
    check(
        "fixed-radius q_E runs large-negative for larger boxes",
        all(rows[n][1] < -3.0 for n in (17, 19, 21, 25, 29)),
        ", ".join(f"N{n}={rows[n][1]:+.2f}" for n in (17, 19, 21, 25, 29)),
    )
    check(
        "box-proportional limit line records convergence toward 1 rather than 15/8",
        "box-proportional q_E ->" in cache_text
        and "target 1" in cache_text
        and "not 15/8, not 5/6" in cache_text,
    )
    check(
        "one-box excursion mechanism is recorded",
        "isolated one-box NUMERATOR excursion" in cache_text
        and "N15" in cache_text
        and "NEG" in cache_text
        and "N13/N17 interp at N15" in cache_text,
    )

    print()
    print("D. Prior notes support the two-layer consumer boundary")
    print("-" * 78)
    check(
        "measured-calibration note named the box-size discriminator and warned it could fail",
        "box-size scan" in measured
        and "could" in measured
        and "fail" in measured
        and "a derivation of `21/4`" in measured,
    )
    check(
        "box-size note prunes only the bulk-limit route",
        "fixed-`N=15` exact-readout coincidence" in box_note
        and "closes the \"maybe it converges to" in box_note
        and "does NOT sharpen the standing naturality no-go" in box_note,
    )
    check(
        "box-size note says it supplies no selecting primitive",
        "supplies **no** selecting" in box_note
        and "primitive" in box_note
        and "only rules out" in box_note
        and "bulk-limit" in box_note
        and "promotion" in box_note,
    )
    check(
        "new note states bulk-limit route is pruned",
        "bulk-limit route is pruned" in note
        and "does not supply the missing Route-2 primitive" in note,
    )
    check(
        "new note keeps fixed-carrier structural-selection gap open",
        "fixed-carrier" in note
        and "structural-selection" in note
        and "independent E-center endpoint ratio" in note
        and "stronger" in note
        and "readout-map primitive" in note,
    )

    print()
    print("E. Exact target rewrites are algebra, not selection")
    print("-" * 78)
    rho_t = Fraction(-1, 1)
    q_t = Fraction(1, 1) + rho_t / 6
    rho_e = Fraction(21, 4)
    q_e = Fraction(1, 1) + rho_e / 6
    shell_te = Fraction(-2, 1)
    c_te = shell_te * q_t / q_e
    check("rho_T=-1 gives q_T=5/6", q_t == Fraction(5, 6), str(q_t))
    check("rho_E=21/4 gives q_E=15/8", q_e == Fraction(15, 8), str(q_e))
    check("q_E=(9/4)q_T is equivalent to q_E=15/8 under q_T=5/6", Fraction(9, 4) * q_t == q_e)
    check("shell T/E=-2 plus target quotients gives c_TE=-8/9", c_te == Fraction(-8, 9), str(c_te))
    check(
        "new note treats the equivalences as target rewrites only",
        "This note does not derive any member of that chain" in note
        and "target rewrite only" in note,
    )

    print()
    print("F. Claim-status firewall")
    print("-" * 78)
    check(
        "new note declares no_go / negative route pruning scope",
        "**Claim scope:** no_go / negative route pruning" in note
        and "**Trace class:** negative_route_pruning" in note,
    )
    check(
        "new note explicitly denies endpoint and time-coupling closure",
        "No derivation of `rho_E = 21/4`" in note
        and "No derivation of the endpoint triple" in note
        and "No unique exact `Theta_R -> Lambda_R` coupling theorem" in note,
    )
    check(
        "new note denies audit verdict or ledger/status change",
        "does not update any audit verdict" in note
        and "No audit verdict or ledger/status change" in note,
    )
    check(
        "new note forbids downstream promotion",
        "do not cite this packet as a derivation of `beta_E / alpha_E = 21/4`" in note
        and "do not cite it as closure of the Route-2 readout endpoint triple" in note
        and "do not use it as an all-routes no-go" in note,
    )
    check(
        "new note has no forbidden retained-status wording",
        not any(
            bad in note
            for bad in (
                "retained " "branch-local",
                "would " "become retained",
                "promoted " "to retained",
                "retained on " "the actual surface",
                "endpoint triple " "derived",
                "unique exact Theta_R -> Lambda_R theorem " "is closed",
            )
        ),
    )

    print()
    print("Summary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bulk-limit promotion is pruned; fixed-carrier readout "
            "selection remains open."
        )
        return 0
    print("VERDICT: consumer-boundary checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
