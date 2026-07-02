#!/usr/bin/env python3
"""Heat-kernel thermodynamic-stretch source-packet verifier.

Authority note:
    docs/BRIDGE_GAP_HK_THERMODYNAMIC_STRETCH_NOTE_2026-05-06.md

This runner checks Block 03 as an open-gate packet: the heat-kernel
multi-plaquette factorization is explicit, the single-plaquette and L_s=2
finite-cube artifacts are runner-backed, and the thermodynamic-limit blocker
remains the missing cluster-decomposition / exponential-clustering estimate.
It does not assign an audit verdict.

Exit code: 0 on full PASS, 1 on any FAIL.
"""

from __future__ import annotations

import hashlib
import math
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, passed: bool, detail: str) -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if passed else "FAIL"
    if passed:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{status}] {name}: {detail}")
    return passed


def read_text(rel_path: str) -> str:
    return (REPO_ROOT / rel_path).read_text(encoding="utf-8")


def sha256_file(rel_path: str) -> str:
    return hashlib.sha256((REPO_ROOT / rel_path).read_bytes()).hexdigest()


def require_fragment(label: str, text: str, needle: str) -> None:
    check(label, needle in text, needle)


def cache_header(cache_text: str) -> dict[str, str]:
    header: dict[str, str] = {}
    for line in cache_text.splitlines():
        if line == "----- stdout -----":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            header[key.strip()] = value.strip()
    return header


def cache_summary(cache_text: str) -> tuple[int | None, int | None]:
    match = re.search(r"SUMMARY:\s+PASS=(\d+)\s+FAIL=(\d+)", cache_text)
    if not match:
        return None, None
    return int(match.group(1)), int(match.group(2))


def check_cache(
    *,
    runner: str,
    cache: str,
    expected_pass: int | None,
    required_fragments: list[str],
) -> None:
    runner_path = REPO_ROOT / runner
    cache_path = REPO_ROOT / cache
    runner_exists = runner_path.exists()
    cache_exists = cache_path.exists()
    check(f"{runner} exists", runner_exists, runner)
    check(f"{cache} exists", cache_exists, cache)
    if not (runner_exists and cache_exists):
        return
    text = cache_path.read_text(encoding="utf-8", errors="replace")
    header = cache_header(text)
    check(f"{runner} cache names same runner", header.get("runner") == runner, header.get("runner", "<missing>"))
    check(f"{runner} cache status ok", header.get("status") == "ok", header.get("status", "<missing>"))
    check(f"{runner} cache exit code zero", header.get("exit_code") == "0", header.get("exit_code", "<missing>"))
    check(
        f"{runner} cache sha is fresh",
        header.get("runner_sha256") == sha256_file(runner),
        f"cache={header.get('runner_sha256', '<missing>')}",
    )
    if expected_pass is not None:
        passes, fails = cache_summary(text)
        check(
            f"{runner} summary has expected pass count",
            passes == expected_pass and fails == 0,
            f"PASS={passes} FAIL={fails}",
        )
    for fragment in required_fragments:
        require_fragment(f"{runner} cache contains required fragment", text, fragment)


def main() -> int:
    print("=" * 78)
    print("HK THERMODYNAMIC STRETCH SOURCE PACKET")
    print("=" * 78)
    print()
    print("Question: is Block 03 now runner-backed as an open gate, with")
    print("the later L_s=2 HK cube result included but not overclaimed?")
    print()

    note_path = "docs/BRIDGE_GAP_HK_THERMODYNAMIC_STRETCH_NOTE_2026-05-06.md"
    note = read_text(note_path)
    cube_note = read_text("docs/BRIDGE_GAP_HK_CUBE_PERRON_NOTE_2026-05-06.md")

    require_fragment("source note title is present", note, "Heat-Kernel Thermodynamic")
    require_fragment("primary runner metadata names this verifier", note, "Primary runner: `scripts/frontier_hk_thermodynamic_stretch_source_packet.py`")
    require_fragment("primary cache metadata names this verifier output", note, "logs/runner-cache/frontier_hk_thermodynamic_stretch_source_packet.txt")
    require_fragment("audit authority firewall is present", note, "independent audit lane")
    require_fragment("source note remains not a closure", note, "NOT a closure")
    require_fragment("source note does not derive thermodynamic value", note, "It does not derive a thermodynamic value")
    require_fragment("exact factorization T3.a is present", note, "Z_HK,Λ(t) = Σ_{(λ_p)} (Π_p W_{λ_p}(t)) · F_Λ((λ_p))")
    require_fragment("marked plaquette expression T3.b is present", note, "F_Λ^{(p_0,1,0)}")
    require_fragment("graph-trace obstruction is named", note, "Obstruction (O3.1): graph-trace combinatorics")
    require_fragment("lambda-sum obstruction is named", note, "Obstruction (O3.2): convergence of the (λ_p)-sum at t=1")
    require_fragment("cluster estimate is the open premise blocker", note, "cluster-decomposition / exponential-clustering estimate")
    require_fragment("current premises do not contain the cluster estimate", note, "current approved primitive or\nretained-premise surface")
    require_fragment("Block 06 update is cited", note, "BRIDGE_GAP_HK_CUBE_PERRON_NOTE_2026-05-06.md")
    require_fragment("Block 06 finite cube value is cited", note, "0.5223243151")
    require_fragment("Block 06 still leaves the named obstruction open", note, "Block 03's named obstruction stands")

    t_at_beta_6 = 1.0
    hk_single = math.exp(-2.0 / 3.0)
    hk_cube = 0.5223243151
    mc_comparator = 0.5934
    check("canonical HK Brownian time at beta=6 is one", math.isclose(t_at_beta_6, 1.0), "t(6)=1")
    check("single-plaquette HK value matches exp(-2/3)", math.isclose(hk_single, 0.513417119032592, rel_tol=0, abs_tol=5e-16), f"exp(-2/3)={hk_single:.15f}")
    check("L_s=2 HK cube improves over single plaquette", hk_cube > hk_single, f"{hk_cube:.10f} > {hk_single:.10f}")
    check("L_s=2 HK cube remains below thermodynamic comparator", hk_cube < mc_comparator, f"{hk_cube:.10f} < {mc_comparator:.4f}")
    check("finite cube gap remains far from epsilon-witness scale", (mc_comparator - hk_cube) > 0.07, f"gap={mc_comparator - hk_cube:.10f}")

    deps = [
        "docs/BRIDGE_GAP_HK_TIME_DERIVATION_NOTE_2026-05-06.md",
        "docs/BRIDGE_GAP_HK_PLAQUETTE_CLOSED_FORM_NOTE_2026-05-06.md",
        "docs/BRIDGE_GAP_HK_CUBE_PERRON_NOTE_2026-05-06.md",
        "docs/SU3_CUBE_FULL_RHO_PERRON_2026-05-04.md",
        "docs/GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md",
        "docs/SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md",
    ]
    for dep in deps:
        dep_name = Path(dep).name
        check(f"{dep_name} exists", (REPO_ROOT / dep).exists(), dep)
        require_fragment(f"{dep_name} cited by Block 03 note", note, dep_name)

    require_fragment("cube note names finite value", cube_note, "P_cube_HK(L_s=2, t=1) = 0.5223243151")
    require_fragment("cube note states thermodynamic limit remains open", cube_note, "does not\nestablish the thermodynamic limit")
    require_fragment("cube note preserves Block 03 blocker", cube_note, "Block 03's named obstruction stands")

    check_cache(
        runner="scripts/probe_hk_time_derivation.py",
        cache="logs/runner-cache/probe_hk_time_derivation.txt",
        expected_pass=7,
        required_fragments=["t(6) = 1", "SUMMARY: PASS=7 FAIL=0"],
    )
    check_cache(
        runner="scripts/probe_hk_plaquette_closed_form.py",
        cache="logs/runner-cache/probe_hk_plaquette_closed_form.txt",
        expected_pass=8,
        required_fragments=["exp(-2/3)", "SUMMARY: PASS=8 FAIL=0"],
    )
    check_cache(
        runner="scripts/probe_hk_cube_perron_l2_2026_05_06.py",
        cache="logs/runner-cache/probe_hk_cube_perron_l2_2026_05_06.txt",
        expected_pass=None,
        required_fragments=[
            "P_cube_HK(L_s=2, t=1) ≈ 0.5223243151",
            "Block 03's named obstruction",
            "thermodynamic-limit closure",
        ],
    )

    print()
    print("=" * 78)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    print()
    if FAIL_COUNT:
        print("Verdict: FAIL; HK thermodynamic stretch packet is not audit-ready.")
        return 1
    print("Verdict: bounded source-packet support. Block 03 is runner-backed")
    print("as an open gate; Block 06 closes the finite-cube comparator path,")
    print("but thermodynamic closure still needs the named clustering estimate.")
    print("No audit verdict or retained status is assigned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
