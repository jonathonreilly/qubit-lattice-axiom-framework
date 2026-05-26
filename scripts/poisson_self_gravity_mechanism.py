#!/usr/bin/env python3
"""Hard-bar certificate for the Poisson self-gravity mechanism row.

This runner is deliberately a fast certificate over included cached outputs.
It parses the heavy runner caches and recomputes the finite hard-bar summary;
it does not print a prewritten verdict.
"""

from __future__ import annotations

import json
import math
import re
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/POISSON_SELF_GRAVITY_MECHANISM_NOTE.md"
LOOP_CACHE = REPO_ROOT / "logs/runner-cache/poisson_self_gravity_loop.txt"
BORN_CACHE = REPO_ROOT / "logs/runner-cache/poisson_self_gravity_born_audit.txt"
V3_CACHE = REPO_ROOT / "logs/runner-cache/poisson_self_gravity_loop_v3.txt"
LEDGER = REPO_ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = REPO_ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "poisson_self_gravity_mechanism_note"
RUNNER_PATH = "scripts/poisson_self_gravity_mechanism.py"

FLOAT = r"[+-]?(?:\d+\.\d+|\d+)(?:e[+-]?\d+)?"

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


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def f(value: str) -> float:
    return float(value.replace("+", ""))


def slope_loglog(points: list[tuple[float, float]]) -> float:
    xs = [math.log(p[0]) for p in points]
    ys = [math.log(abs(p[1])) for p in points]
    xbar = sum(xs) / len(xs)
    ybar = sum(ys) / len(ys)
    denom = sum((x - xbar) ** 2 for x in xs)
    return sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / denom


def note_boundary_checks() -> None:
    note = text(NOTE)
    normalized = " ".join(note.split())
    required = [
        "Claim type:** no_go",
        "Status:** bounded no-go",
        "do not satisfy the mechanism hard bar",
        "included runner-cache artifacts",
        "Why The Mechanism Bar Fails",
        "does not claim",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in normalized)

    forbidden = [
        "*** Add File:",
        "/Users/jonreilly/Projects/Physics",
        "hard-coded conclusion",
        "strict retained verdict",
        "This is a lightweight report script",
    ]
    for phrase in forbidden:
        check(f"note omits stale artifact phrase: {phrase}", phrase not in note)


def loop_cache_checks() -> None:
    cache = text(LOOP_CACHE)
    print("\n=== main loop cache hard bars ===")
    shift = f(re.search(r"zero-epsilon centroid shift:\s+(%s)" % FLOAT, cache).group(1))
    escape = f(re.search(r"zero-epsilon escape ratio:\s+(%s)" % FLOAT, cache).group(1))
    zero_converged = "zero-epsilon converged:       True" in cache
    check("epsilon=0 centroid identity", abs(shift) <= 1e-12, f"{shift:.3e}")
    check("epsilon=0 escape identity", abs(escape - 1.0) <= 1e-12, f"{escape:.6f}")
    check("epsilon=0 loop converged", zero_converged)

    row_re = re.compile(
        r"^\s+(?P<eps>\d+\.\d+)\s+(?P<s>\d+\.\d+)\s+"
        r"(?P<inst>%s)\s+(?P<loop>%s)\s+(?P<ratio>(?:nan|\d+\.\d+))\s+"
        r"(?P<escape>\d+\.\d+)\s+(?P<born>%s)\s+(?P<iters>\d+)\s+(?P<ok>[Yn])$"
        % (FLOAT, FLOAT, FLOAT),
        re.MULTILINE,
    )
    rows = [
        {
            "eps": f(m.group("eps")),
            "s": f(m.group("s")),
            "inst": f(m.group("inst")),
            "loop": f(m.group("loop")),
            "ratio": math.nan if m.group("ratio") == "nan" else f(m.group("ratio")),
            "born": f(m.group("born")),
            "ok": m.group("ok") == "Y",
        }
        for m in row_re.finditer(cache)
    ]
    nonzero = [r for r in rows if r["eps"] > 0.0]
    by_eps: dict[float, list[dict[str, float | bool]]] = defaultdict(list)
    for row in nonzero:
        by_eps[row["eps"]].append(row)

    check("parsed nonzero loop rows", len(nonzero) == 20, str(len(nonzero)))
    check("frozen-field Born stays below hard bar", max(r["born"] for r in nonzero) <= 1e-10, f"{max(r['born'] for r in nonzero):.3e}")
    check("weak-field TOWARD sign on nonzero rows", all(r["loop"] > 0.0 for r in nonzero), f"{sum(r['loop'] > 0.0 for r in nonzero)}/{len(nonzero)}")
    ratios = [r["ratio"] for r in nonzero]
    check("loop/instantaneous ratios stay bounded", min(ratios) >= 0.85 and max(ratios) <= 1.15, f"{min(ratios):.3f}..{max(ratios):.3f}")
    slopes = {eps: slope_loglog([(float(r["s"]), float(r["loop"])) for r in eps_rows]) for eps, eps_rows in by_eps.items()}
    check("nonzero source-strength scaling stays near linear", all(0.85 <= v <= 1.15 for v in slopes.values()), str({k: round(v, 3) for k, v in slopes.items()}))
    check("nonzero loop rows fail strict convergence", all(not r["ok"] for r in nonzero), f"{sum(r['ok'] for r in nonzero)}/{len(nonzero)} converged", kind="B")


def born_cache_checks() -> None:
    cache = text(BORN_CACHE)
    print("\n=== Born audit cache split ===")
    match = re.search(
        r"^\s+0\.05\s+0\.0040\s+(?P<step>%s)\s+(?P<end>%s)\s+"
        r"(?P<step_conv>True|False)\s+(?P<end_conv>True|False)"
        % (FLOAT, FLOAT),
        cache,
        re.MULTILINE,
    )
    check("Born audit representative row parsed", match is not None)
    if not match:
        return
    step_born = f(match.group("step"))
    end_born = f(match.group("end"))
    step_conv = match.group("step_conv") == "True"
    end_conv = match.group("end_conv") == "True"
    check("step-local Born is machine clean", step_born <= 1e-10, f"{step_born:.3e}")
    check("end-to-end Born is not machine clean", end_born > 1e-10, f"{end_born:.3e}", kind="B")
    check("step-local row is not a converged-loop theorem", not step_conv, str(step_conv), kind="B")
    check("end-to-end row is not converged", not end_conv, str(end_conv), kind="B")


def v3_cache_checks() -> None:
    cache = text(V3_CACHE)
    print("\n=== V3 matched-null cache ===")
    zero_shift = f(re.search(r"zero-epsilon centroid shift:\s+(%s)" % FLOAT, cache).group(1))
    zero_slope = f(re.search(r"zero-epsilon phase slope:\s+(%s)" % FLOAT, cache).group(1))
    zero_span = f(re.search(r"zero-epsilon phase span:\s+(%s)" % FLOAT, cache).group(1))
    check("V3 epsilon=0 centroid identity", abs(zero_shift) <= 1e-12, f"{zero_shift:.3e}")
    check("V3 epsilon=0 phase slope identity", abs(zero_slope) <= 1e-12, f"{zero_slope:.3e}")
    check("V3 epsilon=0 phase span identity", abs(zero_span) <= 1e-12, f"{zero_span:.3e}")

    summary_re = re.compile(
        r"eps=(?P<eps>\d+\.\d+) summary: mean delta=(?P<delta>%s) "
        r"mean phase slope=(?P<slope>%s) mean span=(?P<span>%s) "
        r"mean escape=(?P<escape>\d+\.\d+) toward=(?P<toward>\d+)/(?P<total>\d+) "
        r"resid=(?P<resid>%s) converged=(?P<conv>\d+)/(?P<conv_total>\d+)"
        % (FLOAT, FLOAT, FLOAT, FLOAT),
        re.MULTILINE,
    )
    summaries = [
        {
            "eps": f(m.group("eps")),
            "delta": f(m.group("delta")),
            "slope": f(m.group("slope")),
            "span": f(m.group("span")),
            "toward": int(m.group("toward")),
            "total": int(m.group("total")),
            "conv": int(m.group("conv")),
            "conv_total": int(m.group("conv_total")),
        }
        for m in summary_re.finditer(cache)
    ]
    nonzero = [s for s in summaries if s["eps"] > 0.0]
    check("parsed V3 nonzero summaries", len(nonzero) == 3, str(len(nonzero)))
    check("V3 nonzero matched-null direction is TOWARD", all(s["toward"] == s["total"] for s in nonzero), str([(s["toward"], s["total"]) for s in nonzero]))
    check("V3 nonzero rows fail strict convergence", all(s["conv"] == 0 for s in nonzero), str([(s["conv"], s["conv_total"]) for s in nonzero]), kind="B")
    check("V3 matched-null effect remains tiny", max(abs(s["delta"]) for s in nonzero) < 0.05, f"{max(abs(s['delta']) for s in nonzero):.3e}", kind="B")
    check("V3 phase-span effect remains bounded", max(abs(s["span"]) for s in nonzero) < 0.30, f"{max(abs(s['span']) for s in nonzero):.3e}", kind="B")


def audit_metadata_checks() -> None:
    if not LEDGER.exists() or not QUEUE.exists():
        print("\n=== audit metadata unavailable before pipeline ===")
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next(e for e in queue if e["claim_id"] == CLAIM_ID)

    print("\n=== regenerated audit metadata ===")
    check("ledger claim_type is no_go", row.get("claim_type") == "no_go")
    check("ledger audit_status reset to unaudited", row.get("audit_status") == "unaudited")
    check("ledger effective_status reset to unaudited", row.get("effective_status") == "unaudited")
    check("ledger runner_path registered", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("ledger has no direct deps", row.get("deps") == [], str(row.get("deps")))
    check("no open dependency paths remain", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))
    check("queue marks row ready", queue_entry.get("ready") is True, str(queue_entry.get("ready")))
    check("descendant chain remains material", int(row.get("transitive_descendants") or 0) >= 100, str(row.get("transitive_descendants")), kind="B")


def main() -> int:
    note_boundary_checks()
    loop_cache_checks()
    born_cache_checks()
    v3_cache_checks()
    audit_metadata_checks()
    print("\nPoisson self-gravity mechanism hard-bar certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
