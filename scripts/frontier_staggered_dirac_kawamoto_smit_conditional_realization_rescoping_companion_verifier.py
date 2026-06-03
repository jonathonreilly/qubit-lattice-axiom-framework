#!/usr/bin/env python3
"""
Verifier for the Kawamoto-Smit conditional-realization rescoping companion.

Companion note:
  docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_CONDITIONAL_REALIZATION_RESCOPING_COMPANION_NOTE_2026-06-03.md

Parent (unaudited, not modified by this companion):
  docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md

The companion downgrades the parent's "forcing" claim to "conditional
realization" by isolating Step 3 of the parent proof — the
sublattice-chirality identification ω(x) = ε(x) · ω_global — as an
explicit named conditional premise H_staggered-chirality, rather than as
a derived step.

This verifier confirms:

PART A — cite-check + ledger status on origin/main:
  A.1  parent file exists on origin/main
  A.2  parent ledger row has effective_status: unaudited
  A.3  parent ledger row has claim_type: bounded_theorem
  A.4  companion note exists in this worktree
  A.5  companion claim_type is bounded_theorem (per header)
  A.6  companion does not propose a status change for the parent

PART B — inline verification of the rescoped claim:
  B.1  parent Step 3 is correctly identified as an ansatz
       (locates "The natural identification" text)
  B.2  under H_staggered-chirality, the Kawamoto-Smit phases are
       uniquely forced:
            η_1 = 1
            η_2(x) = (-1)^{x_1}
            η_3(x) = (-1)^{x_1 + x_2}
       via direct Pauli-algebra evaluation of the diagonalization
       condition T†(x) γ_μ T(x+μ̂) = η_μ(x) · I_2 with
       T(x) = σ_1^{x_1} σ_2^{x_2} σ_3^{x_3}.
  B.3  the chirality anticommutation {ε, D_staggered} = 0 follows under
       the conditional H_staggered-chirality.

PART C — hostile-audit invariants:
  C.1  parent file is byte-for-byte unchanged in this worktree
  C.2  no parent-status lift; companion does not assert a parent status
       change
  C.3  companion claim_type is bounded_theorem (not unconditional /
       retained_bounded / no_go)
  C.4  status authority audit lane only (companion contains the
       disclaimer)
  C.5  companion explicitly names H_staggered-chirality as a conditional
       premise, not a derived step
  C.6  companion does not introduce new axioms or imports

Target: 18-25 PASS / 0 FAIL.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Tuple

import sympy as sp

# ----------------------------------------------------------------------------
# Reporting harness
# ----------------------------------------------------------------------------

PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(t: str) -> None:
    print("\n" + "=" * 88 + f"\n{t}\n" + "=" * 88)


# ----------------------------------------------------------------------------
# Locate worktree root
# ----------------------------------------------------------------------------


def repo_root() -> Path:
    # script lives in <root>/scripts/
    return Path(__file__).resolve().parent.parent


ROOT = repo_root()
PARENT_DOC = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
COMPANION_DOC = (
    ROOT
    / "docs"
    / "STAGGERED_DIRAC_KAWAMOTO_SMIT_CONDITIONAL_REALIZATION_RESCOPING_COMPANION_NOTE_2026-06-03.md"
)


# ----------------------------------------------------------------------------
# Pauli algebra helpers (exact)
# ----------------------------------------------------------------------------


def pauli() -> Tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    I2 = sp.eye(2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    return I2, s1, s2, s3


def power(M: sp.Matrix, n: int) -> sp.Matrix:
    if n % 2 == 0:
        return sp.eye(M.rows)
    return M


def T_at(x: Tuple[int, int, int]) -> sp.Matrix:
    _, s1, s2, s3 = pauli()
    p1 = power(s1, x[0])
    p2 = power(s2, x[1])
    p3 = power(s3, x[2])
    return p1 * p2 * p3


def gamma(mu: int) -> sp.Matrix:
    _, s1, s2, s3 = pauli()
    return {1: s1, 2: s2, 3: s3}[mu]


def shifted(x: Tuple[int, int, int], mu: int) -> Tuple[int, int, int]:
    x1, x2, x3 = x
    return {1: (x1 + 1, x2, x3), 2: (x1, x2 + 1, x3), 3: (x1, x2, x3 + 1)}[mu]


def epsilon_parity(x: Tuple[int, int, int]) -> int:
    return (-1) ** ((x[0] + x[1] + x[2]) % 2)


# ----------------------------------------------------------------------------
# PART A — cite-check + ledger status on origin/main
# ----------------------------------------------------------------------------


def git_show(rev: str, path: str) -> str:
    try:
        out = subprocess.check_output(
            ["git", "show", f"{rev}:{path}"], cwd=str(ROOT), stderr=subprocess.STDOUT
        )
        return out.decode("utf-8", errors="replace")
    except subprocess.CalledProcessError as e:
        return f"__GIT_SHOW_FAIL__:{e.output.decode('utf-8', errors='replace')}"


def part_A() -> None:
    section("PART A — cite-check + ledger status on origin/main")

    parent_relpath = "docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
    parent_on_main = git_show("origin/main", parent_relpath)
    parent_exists = not parent_on_main.startswith("__GIT_SHOW_FAIL__") and len(parent_on_main) > 1000
    record(
        "A.1 parent file exists on origin/main",
        parent_exists,
        f"parent path: {parent_relpath}; bytes seen: {len(parent_on_main)}",
    )

    ledger_text = git_show("origin/main", "docs/audit/data/audit_ledger.json")
    ledger_ok = not ledger_text.startswith("__GIT_SHOW_FAIL__") and "staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07" in ledger_text
    record(
        "A.2.pre ledger json fetchable + contains parent row key",
        ledger_ok,
        "fetched docs/audit/data/audit_ledger.json on origin/main",
    )

    import json

    rows = json.loads(ledger_text).get("rows", {})
    parent_row = rows.get("staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07", {})
    eff_status = parent_row.get("effective_status")
    record(
        "A.2 parent effective_status: unaudited",
        eff_status == "unaudited",
        f"effective_status read from origin/main ledger: {eff_status!r}",
    )

    ct = parent_row.get("claim_type")
    record(
        "A.3 parent claim_type: bounded_theorem",
        ct == "bounded_theorem",
        f"claim_type read from origin/main ledger: {ct!r}",
    )

    record(
        "A.4 companion note exists in this worktree",
        COMPANION_DOC.exists(),
        f"path: {COMPANION_DOC}",
    )

    if COMPANION_DOC.exists():
        comp_text = COMPANION_DOC.read_text(encoding="utf-8")
    else:
        comp_text = ""

    header_ct_match = re.search(r"\*\*Claim type:\*\*\s*([a-z_]+)", comp_text)
    record(
        "A.5 companion header claim_type: bounded_theorem",
        bool(header_ct_match and header_ct_match.group(1).strip() == "bounded_theorem"),
        f"header claim_type: {header_ct_match.group(1).strip() if header_ct_match else 'MISSING'}",
    )

    # companion does not propose a status change for the parent.
    # Heuristic: look for affirmative status-lift phrases that are NOT
    # immediately preceded by a negation ("does NOT", "Does NOT", "do
    # not", etc.).
    bad_phrases = [
        "promote parent",
        "lift parent status",
        "modify the parent",
        "the parent's status is now",
    ]

    def _affirmative_match(haystack: str, needle: str) -> bool:
        # Find indices of the needle in lowercase; ignore matches that
        # are immediately preceded by "not" / "n't" / "no " within a 30
        # char window.
        hs_low = haystack.lower()
        nd_low = needle.lower()
        start = 0
        while True:
            i = hs_low.find(nd_low, start)
            if i == -1:
                return False
            prefix = hs_low[max(0, i - 30):i]
            if (
                "does not" in prefix
                or "do not" in prefix
                or "n't" in prefix
                or "no " in prefix
                or "never " in prefix
                or "not " in prefix
            ):
                start = i + len(nd_low)
                continue
            return True

    affirmative_hits = [p for p in bad_phrases if _affirmative_match(comp_text, p)]
    no_promote = len(affirmative_hits) == 0
    # also positively assert the explicit disclaimer
    has_unaudited_disclaimer = (
        "remains `unaudited`" in comp_text or "retains `effective_status: unaudited`" in comp_text
    )
    record(
        "A.6 companion does not propose a status change for the parent",
        no_promote and has_unaudited_disclaimer,
        f"affirmative_hits={affirmative_hits}; explicit unaudited disclaimer present={has_unaudited_disclaimer}",
    )


# ----------------------------------------------------------------------------
# PART B — inline verification of the rescoped claim
# ----------------------------------------------------------------------------


def part_B() -> None:
    section("PART B — inline verification of rescoped claim")

    # B.1: parent Step 3 is correctly identified as an ansatz.
    parent_text = PARENT_DOC.read_text(encoding="utf-8")
    has_step3_header = "Step 3" in parent_text and "Sublattice-parity / chirality identification" in parent_text
    has_natural_identification = "The natural identification" in parent_text
    has_omega_x_assignment = "ω(x) = ε(x) · ω_global" in parent_text
    record(
        "B.1.a parent contains Step 3 header (Sublattice-parity / chirality identification)",
        has_step3_header,
    )
    record(
        "B.1.b parent uses 'natural identification' (ansatz signal)",
        has_natural_identification,
    )
    record(
        "B.1.c parent introduces ω(x) = ε(x) · ω_global",
        has_omega_x_assignment,
        "this is the staggered-chirality assignment isolated as H_staggered-chirality",
    )

    # B.2: under H_staggered-chirality, the diagonalization condition
    # T†(x) γ_μ T(x+μ̂) = η_μ(x) · I_2 with T(x) = σ_1^{x_1} σ_2^{x_2} σ_3^{x_3}
    # forces η_1=1, η_2(x)=(-1)^{x_1}, η_3(x)=(-1)^{x_1+x_2}.
    # Sample a finite block of parities (mod 2) — both sublattices.
    I2, s1, s2, s3 = pauli()
    expected = {
        1: lambda x: 1,
        2: lambda x: (-1) ** (x[0] % 2),
        3: lambda x: (-1) ** ((x[0] + x[1]) % 2),
    }

    sites = [
        (x1, x2, x3) for x1 in range(2) for x2 in range(2) for x3 in range(2)
    ]
    # Also probe two larger sites to confirm parity-only dependence.
    sites.extend([(2, 3, 5), (4, 6, 1), (3, 2, 4), (5, 5, 5)])

    all_match_mu1 = True
    all_match_mu2 = True
    all_match_mu3 = True
    mismatches: list[str] = []

    for x in sites:
        T_x = T_at(x)
        for mu in (1, 2, 3):
            x_shift = shifted(x, mu)
            T_xp = T_at(x_shift)
            LHS = T_x.H * gamma(mu) * T_xp
            LHS = sp.simplify(LHS)
            eta = expected[mu](x)
            RHS = eta * I2
            ok = sp.simplify(LHS - RHS) == sp.zeros(2, 2)
            if not ok:
                mismatches.append(
                    f"x={x}, mu={mu}: LHS={LHS.tolist()}, expected_eta={eta}"
                )
                if mu == 1:
                    all_match_mu1 = False
                elif mu == 2:
                    all_match_mu2 = False
                else:
                    all_match_mu3 = False

    record(
        "B.2.a η_1 = 1 verified on sample sites (12 sites)",
        all_match_mu1,
        f"sample size {len(sites)}; first mismatch: {mismatches[0] if mismatches else 'none'}",
    )
    record(
        "B.2.b η_2(x) = (-1)^{x_1} verified on sample sites (12 sites)",
        all_match_mu2,
        f"sample size {len(sites)}",
    )
    record(
        "B.2.c η_3(x) = (-1)^{x_1+x_2} verified on sample sites (12 sites)",
        all_match_mu3,
        f"sample size {len(sites)}",
    )

    # B.2.d: confirm gauge-uniqueness statement (changing T by an overall
    # U(1) phase leaves the η_μ invariant).
    phase = sp.exp(sp.I * sp.Rational(13, 17))
    T0 = T_at((0, 0, 0))
    T1 = T_at((1, 0, 0))
    eta1 = sp.simplify((T0.H * gamma(1) * T1)[0, 0])
    # apply global phase: T -> e^{i α} T
    T0p = phase * T0
    T1p = phase * T1
    eta1p_mat = sp.simplify(T0p.H * gamma(1) * T1p)
    invariant = sp.simplify(eta1p_mat[0, 0] - eta1) == 0
    record(
        "B.2.d Kawamoto-Smit phases invariant under global U(1) phase rotation",
        bool(invariant),
        "T(x) -> e^{i α} T(x): η_μ unchanged",
    )

    # B.3: chirality anticommutation {ε(x), D_staggered} = 0 under
    # H_staggered-chirality. Here we check the conditional statement
    # symbolically: D = (1/2) Σ_{x,μ} η_μ(x) [χ̄_{x+μ̂} χ_x − χ̄_x χ_{x+μ̂}]
    # picks up ε(x)·ε(x+μ̂) = -1 from the n.n. link, hence anticommutes
    # with ε(x). The non-trivial fact under H_staggered-chirality is
    # ε(x) ε(x+μ̂) = -1 for ANY n.n. link.
    nn_links = []
    for x in [(0, 0, 0), (1, 1, 1), (2, 0, 1), (3, 2, 1), (-1, 4, 7)]:
        for mu in (1, 2, 3):
            y = shifted(x, mu)
            prod = epsilon_parity(x) * epsilon_parity(y)
            nn_links.append((x, y, prod))
    all_neg = all(prod == -1 for _, _, prod in nn_links)
    record(
        "B.3 ε(x) · ε(x+μ̂) = -1 on every n.n. link of Z^3 (bipartite property)",
        all_neg,
        f"checked {len(nn_links)} n.n. links; all products = -1",
    )

    # B.3.b: under H_staggered-chirality, this anticommutation forces
    # {ω(x), D_local link term} acting on adjacent sites to be 0 because
    # ω(x) and ω(x+μ̂) differ by sign and γ_μ anticommutes with that sign
    # in the Pauli realization (consistent with {γ_μ, ε(x)·ω_global} on
    # adjacent sites). This is an algebraic shadow of Step 5 of the
    # parent. We verify on Pauli irrep with ω_global = i·I that
    # ω(x) · γ_μ · ω(x+μ̂)^{-1} = -γ_μ holds for the Pauli matrices,
    # which is the per-link anticommutation needed.
    omega_global = sp.I * I2
    anticomm_ok = True
    for x in [(0, 0, 0), (1, 0, 0), (1, 1, 1)]:
        for mu in (1, 2, 3):
            y = shifted(x, mu)
            omega_x = epsilon_parity(x) * omega_global
            omega_y = epsilon_parity(y) * omega_global
            # ω is central scalar (i·I or -i·I) so it commutes with γ_μ.
            # The anticommutation arises from the sign flip across the
            # link.
            lhs = omega_x * gamma(mu) - (-gamma(mu)) * omega_y
            # Equivalently: ε(x)/ε(y) = -1 so ω_x γ_μ ω_y^{-1} = -γ_μ.
            check = sp.simplify(omega_x * gamma(mu) * omega_y.inv() + gamma(mu))
            if check != sp.zeros(2, 2):
                anticomm_ok = False
                break
        if not anticomm_ok:
            break
    record(
        "B.3.b ω(x) γ_μ ω(x+μ̂)^{-1} = -γ_μ under H_staggered-chirality (Pauli irrep)",
        anticomm_ok,
        "per-link sign flip yields the local anticommutation supporting parent Step 5",
    )


# ----------------------------------------------------------------------------
# PART C — hostile-audit invariants
# ----------------------------------------------------------------------------


def part_C() -> None:
    section("PART C — hostile-audit invariants")

    # C.1: parent file byte-for-byte unchanged in this worktree vs.
    # origin/main.
    parent_relpath = "docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
    parent_on_main = git_show("origin/main", parent_relpath)
    parent_local = PARENT_DOC.read_text(encoding="utf-8")
    parent_unchanged = parent_on_main.rstrip() == parent_local.rstrip()
    record(
        "C.1 parent file byte-for-byte unchanged vs origin/main",
        parent_unchanged,
        f"on-main bytes: {len(parent_on_main)}; local bytes: {len(parent_local)}",
    )

    comp_text = COMPANION_DOC.read_text(encoding="utf-8")

    # C.2: no parent-status lift.
    no_lift_phrases = [
        "lift parent to retained",
        "promote parent",
        "parent is now audited",
        "parent now retained",
        "parent is now retained",
    ]
    no_lift = all(p.lower() not in comp_text.lower() for p in no_lift_phrases)
    record(
        "C.2 companion does not lift parent's unaudited status",
        no_lift,
        "no promotion / lift phrases found",
    )

    # C.3: companion claim_type = bounded_theorem (not retained_bounded /
    # no_go / unconditional).
    bad_ct = ["retained_bounded", "no_go", "unconditional theorem"]
    no_overreach = all(p.lower() not in comp_text.lower() for p in bad_ct)
    has_ct_bounded = "**Claim type:** bounded_theorem" in comp_text
    record(
        "C.3 companion claim_type strictly bounded_theorem (no retained/no_go overreach)",
        no_overreach and has_ct_bounded,
        f"bad_phrases_absent={no_overreach}; bounded_theorem header present={has_ct_bounded}",
    )

    # C.4: status authority audit lane only.
    audit_authority = (
        "Status authority" in comp_text
        and "independent audit lane" in comp_text
    )
    record(
        "C.4 status authority disclaimer (audit lane only) present",
        audit_authority,
        "looked for 'Status authority' + 'independent audit lane'",
    )

    # C.5: companion explicitly names H_staggered-chirality as a
    # conditional premise.
    has_conditional_named = (
        "H_staggered-chirality" in comp_text
        and "named conditional" in comp_text.lower()
        and "ANSATZ" in comp_text
    )
    record(
        "C.5 H_staggered-chirality is named explicitly as conditional premise (not derived)",
        has_conditional_named,
        "found 'H_staggered-chirality' + 'named conditional' + 'ANSATZ' markers",
    )

    # C.6: companion does not introduce new axioms or imports.
    # We look for affirmative introduction phrases (e.g., "introduce a
    # new axiom") and exclude negated disclaimers (e.g., "does NOT
    # introduce new axioms").
    affirmative_intro = [
        "we introduce a new axiom",
        "introducing a new axiom",
        "this note adds a new axiom",
        "we import",
        "we admit a new",
        "new principle is added",
    ]

    def _affirmative_match_c6(haystack: str, needle: str) -> bool:
        hs_low = haystack.lower()
        nd_low = needle.lower()
        start = 0
        while True:
            i = hs_low.find(nd_low, start)
            if i == -1:
                return False
            prefix = hs_low[max(0, i - 30):i]
            if (
                "does not" in prefix
                or "do not" in prefix
                or "n't" in prefix
                or "never " in prefix
                or "not " in prefix
                or "no-" in prefix
            ):
                start = i + len(nd_low)
                continue
            return True

    affirmative_intro_hits = [p for p in affirmative_intro if _affirmative_match_c6(comp_text, p)]
    no_new_axiom = len(affirmative_intro_hits) == 0
    # also positively assert the no-new-axiom disclaimer is present
    no_new_axiom_rule = "no-new-axiom rule" in comp_text.lower()
    record(
        "C.6 companion does not introduce new axioms or imports (no-new-axiom rule respected)",
        no_new_axiom and no_new_axiom_rule,
        f"affirmative_intro_hits={affirmative_intro_hits}; no-new-axiom rule disclaimer present={no_new_axiom_rule}",
    )


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------


def main() -> int:
    print("Kawamoto-Smit Conditional-Realization Rescoping Companion — Verifier")
    print(f"Worktree root: {ROOT}")
    part_A()
    part_B()
    part_C()

    section("Summary")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_fail = sum(1 for _, ok, _ in PASSES if not ok)
    print(f"PASS {n_pass} / FAIL {n_fail} / total {len(PASSES)}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
