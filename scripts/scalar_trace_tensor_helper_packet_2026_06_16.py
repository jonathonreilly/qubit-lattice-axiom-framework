#!/usr/bin/env python3
"""Source/cache packet for the scalar-trace tensor no-go helper imports.

This runner is deliberately small: it makes the three load-bearing helper
sources and cached outputs explicit for the scalar-trace-only tensor no-go.
It does not apply an audit verdict and does not strengthen the physics claim.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "logs" / "runner-cache"


@dataclass(frozen=True)
class Helper:
    label: str
    runner: str
    required_tokens: tuple[str, ...]


HELPERS = (
    Helper(
        "tensorial Einstein/Regge completion probes",
        "scripts/frontier_tensorial_einstein_regge_completion.py",
        ("def probe_family", "def ricci_and_einstein", "def scalar_bridge_action"),
    ),
    Helper(
        "same-source local O_h source family",
        "scripts/frontier_same_source_metric_ansatz_scan.py",
        ("def build_best_phi_grid", "def residual_norm", "def positivity_ok"),
    ),
    Helper(
        "coarse-grained finite-rank exterior law",
        "scripts/frontier_coarse_grained_exterior_law.py",
        ("def build_finite_rank_phi_grid", "def residual_at_radius", "def shell_data"),
    ),
)

PRIMARY_RUNNER = ROOT / "scripts/frontier_scalar_trace_tensor_nogo.py"

CHECKS: list[bool] = []


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def cache_path_for(runner_rel: str) -> Path:
    return CACHE_DIR / f"{Path(runner_rel).stem}.txt"


def header_value(cache_text: str, key: str) -> str:
    m = re.search(rf"^{re.escape(key)}:\s*(.+)$", cache_text, flags=re.MULTILINE)
    return m.group(1).strip() if m else ""


def stdout_text(cache_text: str) -> str:
    marker = "----- stdout -----"
    err = "----- stderr -----"
    if marker not in cache_text:
        return ""
    body = cache_text.split(marker, 1)[1]
    return body.split(err, 1)[0] if err in body else body


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f" -- {detail}" if detail else ""))


def check_cache(helper: Helper, current_sha: str) -> None:
    cache_path = cache_path_for(helper.runner)
    record(f"{helper.label} cache exists", cache_path.exists(), str(cache_path.relative_to(ROOT)))
    if not cache_path.exists():
        return
    text = cache_path.read_text(encoding="utf-8", errors="replace")
    out = stdout_text(text)
    record(
        f"{helper.label} cache names helper runner",
        header_value(text, "runner") == helper.runner,
        header_value(text, "runner"),
    )
    record(
        f"{helper.label} cache is SHA-fresh",
        header_value(text, "runner_sha256") == current_sha,
        header_value(text, "runner_sha256")[:12],
    )
    record(
        f"{helper.label} cache exited cleanly",
        header_value(text, "status") == "ok" and header_value(text, "exit_code") == "0",
        f"status={header_value(text, 'status')} exit={header_value(text, 'exit_code')}",
    )
    if "FAIL=" in out:
        ok = "FAIL=0" in out and "All checks passed." in out
    else:
        ok = "PASS" in out and "Some checks failed." not in out
    record(f"{helper.label} cache output is passing", ok)


def main() -> int:
    print("Scalar-trace tensor helper source/cache packet")
    print("=" * 72)

    primary_text = PRIMARY_RUNNER.read_text(encoding="utf-8")
    for token in (
        "import frontier_tensorial_einstein_regge_completion as tcomp",
        "import frontier_same_source_metric_ansatz_scan as same_source",
        "import frontier_coarse_grained_exterior_law as coarse",
    ):
        record(f"primary no-go runner has static import: {token}", token in primary_text)

    for helper in HELPERS:
        print(f"\n{helper.label}")
        path = ROOT / helper.runner
        record(f"{helper.runner} exists", path.exists())
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        digest = sha256(path)
        record(f"{helper.runner} has substantive source", len(text.splitlines()) >= 100, f"lines={len(text.splitlines())}")
        for token in helper.required_tokens:
            record(f"{helper.runner} exposes `{token}`", token in text)
        print(f"    sha256={digest}")
        check_cache(helper, digest)

    print("\n" + "=" * 72)
    passed = sum(CHECKS)
    total = len(CHECKS)
    failed = total - passed
    print(f"SUMMARY: PASS={passed} FAIL={failed} TOTAL={total}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
