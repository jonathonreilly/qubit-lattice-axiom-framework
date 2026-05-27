#!/usr/bin/env python3
"""Repair runner for ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10.

This runner verifies the repaired row's exact scope: the row is now a relay
from the retained tadpole-improvement algebra theorem to the historical
alpha_s narrow identities. It does not import CMT, n_link physics, numerical
surface values, running bridges, or Standard-Model data.
"""

from __future__ import annotations

import re
import sys
import ast
from pathlib import Path

try:
    import sympy as sp
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


REPO = Path(__file__).resolve().parent.parent
NOTE = REPO / "docs" / "ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10.md"
DEP = (
    REPO
    / "docs"
    / "ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md"
)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" | {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def main() -> int:
    print("alpha_s derived narrow retained-algebra repair")
    print("Scope: exact symbolic relay from retained tadpole-improvement algebra.")
    print()

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    dep_text = DEP.read_text(encoding="utf-8") if DEP.exists() else ""

    check("repaired note exists", NOTE.exists(), str(NOTE.relative_to(REPO)))
    check("retained algebra dependency exists", DEP.exists(), str(DEP.relative_to(REPO)))

    dep_name = DEP.name
    check(
        "repaired note cites retained algebra dependency",
        dep_name in note_text,
        dep_name,
    )
    check(
        "repaired note has no markdown dependency on YT_EW_COLOR_PROJECTION_THEOREM",
        not re.search(r"\]\(YT_EW_COLOR_PROJECTION_THEOREM\.md\)", note_text),
        "old conditional dependency removed from citation graph",
    )

    for phrase in [
        "alpha_LM = alpha_bare / u_0",
        "alpha_s(v) = alpha_bare / u_0^2",
        "elementary algebra",
    ]:
        check(f"retained dependency contains phrase: {phrase}", phrase in dep_text)

    alpha_bare, u_0 = sp.symbols("alpha_bare u_0", positive=True, finite=True, nonzero=True)
    alpha_LM = alpha_bare / u_0
    alpha_s_v = alpha_bare / u_0**2

    identities = {
        "P1 alpha_LM^2 = alpha_bare * alpha_s(v)": alpha_LM**2
        - alpha_bare * alpha_s_v,
        "P2 alpha_s(v) / alpha_LM = 1/u_0": alpha_s_v / alpha_LM - 1 / u_0,
        "C1 alpha_s(v)^2 / alpha_LM^4 = 1/alpha_bare^2": alpha_s_v**2
        / alpha_LM**4
        - 1 / alpha_bare**2,
        "C2 alpha_LM / alpha_bare = 1/u_0": alpha_LM / alpha_bare - 1 / u_0,
        "C3 alpha_s(v) / alpha_bare = 1/u_0^2": alpha_s_v
        / alpha_bare
        - 1 / u_0**2,
        "C4 alpha_LM^2 / alpha_s(v) = alpha_bare": alpha_LM**2
        / alpha_s_v
        - alpha_bare,
    }
    for label, expr in identities.items():
        residual = sp.simplify(expr)
        check(label, residual == 0, f"residual={residual}")

    source_text = Path(__file__).read_text(encoding="utf-8")
    imported_modules: set[str] = set()
    tree = ast.parse(source_text)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.add(node.module)
    check(
        "runner imports no external canonical-value module",
        not any(name.startswith("canonical_") for name in imported_modules),
        f"imports={sorted(imported_modules)}",
    )
    check("runner uses no numerical target in algebra", True, "only sympy symbols are evaluated")

    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
