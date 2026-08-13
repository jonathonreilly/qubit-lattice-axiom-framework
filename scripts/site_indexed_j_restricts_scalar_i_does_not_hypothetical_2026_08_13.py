#!/usr/bin/env python3
"""Exact C1-follow-on checks: J restricts; scalar I does not.

Reconstructs C1 J arithmetic on W={x,y}, U={x}, unit-A locks h10 and h01.
Identity gates call I_W, I_U, J_of, and J_restrict. No Record rewrite, no
sheaf, no pairing, no Newton-π product table, no fifth extra, no C1 adoption.
"""

from __future__ import annotations

import ast
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SITE_INDEXED_J_RESTRICTS_SCALAR_I_DOES_NOT_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

AUDIT_INPUT_PATHS = (
    "docs/SITE_INDEXED_J_RESTRICTS_SCALAR_I_DOES_NOT_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

EMPTY = 0
A = "A"
B = "B"
X = "x"
Y = "y"
W = (X, Y)
U = (X,)
MENU = (A, B)


class History:
    """Site-indexed unit-lock field on W, ordered as (J(x), J(y))."""

    __slots__ = ("name", "locks")

    def __init__(self, name: str, locks: tuple[object, object]) -> None:
        self.name = name
        self.locks = locks


def J_of(history: History) -> tuple[object, object]:
    """Window value of the reconstructed C1 lock field J."""
    return history.locks


def J_restrict(history: History) -> object:
    """Restriction by evaluation: (J|_U)(x) = J(x)."""
    j_w = J_of(history)
    return j_w[W.index(U[0])]


def I_on(history: History, sites: tuple[str, ...]) -> int:
    j_w = J_of(history)
    return sum(1 for site in sites if j_w[W.index(site)] != EMPTY)


def I_W(history: History) -> int:
    return I_on(history, W)


def I_U(history: History) -> int:
    return I_on(history, U)


def i_u_is_function_of_i_w(histories: tuple[History, ...]) -> bool:
    """True iff some f:ℕ→ℕ satisfies f(I_W(h))=I_U(h) on the sample."""
    table: dict[int, int] = {}
    for history in histories:
        key = I_W(history)
        value = I_U(history)
        if key in table and table[key] != value:
            return False
        table[key] = value
    return True


def identity_gate_calls_present(source: str) -> bool:
    tree = ast.parse(source)
    required = {
        ("I_W", "h10"),
        ("I_W", "h01"),
        ("I_U", "h10"),
        ("I_U", "h01"),
        ("J_restrict", "h10"),
        ("J_restrict", "h01"),
        ("J_of", "h10"),
        ("J_of", "h01"),
    }
    seen: set[tuple[str, str]] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
            continue
        if not node.args or not isinstance(node.args[0], ast.Name):
            continue
        seen.add((node.func.id, node.args[0].id))
    return required <= seen


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
    runner_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: axiom memo Record wording only; C1 J arithmetic is reconstructed locally")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: display restriction only; C1, sheaf, pairing, Newton-π, fifth extra, r=1/2, and L_phys are not adopted")

    checks.check(
        "audit-input-paths",
        "declared inputs are the new note and the axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, AXIOM_REL)
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "machine-status-contract",
        "required hypothetical and surface-status strings are present",
        'hypothetical_axiom_status: "C1 follow-on: J restricts to subsites, scalar I does not; not adopted"'
        in note
        and "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "record-quote",
        "current Record names scalar additive I determined by content alone",
        "A readout value is determined by record content" in axiom
        and "scalar readout" in axiom
        and "`I` is additive" in axiom
        and "`I(empty)=0`" in axiom,
    )

    h10 = History("h10", (A, EMPTY))
    h01 = History("h01", (EMPTY, A))

    iw_h10 = I_W(h10)
    iw_h01 = I_W(h01)
    iu_h10 = I_U(h10)
    iu_h01 = I_U(h01)
    jw_h10 = J_of(h10)
    jw_h01 = J_of(h01)
    jr_h10 = J_restrict(h10)
    jr_h01 = J_restrict(h01)

    checks.check(
        "identity-I_W-h10",
        "I_W(h10) is the exact integer 1",
        iw_h10 == 1 and isinstance(iw_h10, int),
    )
    checks.check(
        "identity-I_W-h01",
        "I_W(h01) is the exact integer 1",
        iw_h01 == 1 and isinstance(iw_h01, int),
    )
    checks.check(
        "identity-I_U-h10",
        "I_U(h10) is the exact integer 1",
        iu_h10 == 1 and isinstance(iu_h10, int),
    )
    checks.check(
        "identity-I_U-h01",
        "I_U(h01) is the exact integer 0",
        iu_h01 == 0 and isinstance(iu_h01, int),
    )
    checks.check(
        "theorem1-window-equal",
        "I_W(h10)=I_W(h01)=1",
        iw_h10 == iw_h01 == 1,
    )
    checks.check(
        "theorem1-subsite-split",
        "I_U(h10)=1 ≠ 0=I_U(h01)",
        iu_h10 == 1 and iu_h01 == 0 and iu_h10 != iu_h01,
    )
    checks.check(
        "mutation-I-not-function",
        "predicate I_U is a function of I_W fails",
        i_u_is_function_of_i_w((h10, h01)) is False,
    )
    checks.check(
        "identity-J_restrict-h10",
        "J_W(h10)=(A,0) determines J|_U=A",
        jw_h10 == (A, EMPTY) and jr_h10 == A,
    )
    checks.check(
        "identity-J_restrict-h01",
        "J_W(h01)=(0,A) determines J|_U=0",
        jw_h01 == (EMPTY, A) and jr_h01 == EMPTY,
    )
    checks.check(
        "mutation-J-restrict-unequal",
        "predicate J|_U(h10)=J|_U(h01) fails",
        (jr_h10 == jr_h01) is False,
    )
    checks.check(
        "identity-gate-ast",
        "identity gates call I_W, I_U, J_of, and J_restrict on h10 and h01",
        identity_gate_calls_present(runner_source),
    )
    checks.check(
        "menu-window-subsite",
        "reconstructed objects are W={x,y}, U={x}, M={A,B}",
        W == ("x", "y") and U == ("x",) and MENU == (A, B) and B == "B",
    )
    checks.check(
        "display-only-surface",
        "note displays restriction and refuses C1, sheaf, pairing, Newton-π, fifth extra, r=1/2, and L_phys",
        all(
            phrase in note
            for phrase in (
                "Do not adopt C1",
                "not a sheaf axiom",
                "not a pairing",
                "does not dissolve Newton π",
                "does not name a fifth extra",
                "Do not force `r=1/2`",
                "Do not adopt `L_phys`",
                "Do not adopt a Record rewrite",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "axiom memo is not rewritten to site-indexed J",
        all(
            phrase not in axiom
            for phrase in (
                "J|_U",
                "site-indexed J",
                "C1 follow-on",
                "restriction-stable",
            )
        ),
    )

    print("per_element: two unit-A lock histories on a two-site window")
    print("per_site: restriction is evaluation at the single site of U")
    print("per_mode: occupancy I is a cardinality; no product table is formed")
    print("per_block: Record readout restriction type is the only negative block tested")
    print("lattice_wide: checked and not executed — only W={x,y} is in scope")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
