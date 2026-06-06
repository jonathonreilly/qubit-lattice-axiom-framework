# Formal Assumption-and-Import Audit of the Staggered-Dirac Realization Gate ("The Exercise")

**Date:** 2026-06-06
**Claim type:** meta / methodology-audit (the repo's assumption-import + counterfactual exercise, applied)
**Status:** review-loop source proposal. Adds no axiom, no fitted input, no audit
verdict. Records no audit status.
**Primary runner:**
[`scripts/frontier_staggered_dirac_formal_assumption_import_audit_2026_06_06.py`](../scripts/frontier_staggered_dirac_formal_assumption_import_audit_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_staggered_dirac_formal_assumption_import_audit_2026_06_06.txt`](../logs/runner-cache/frontier_staggered_dirac_formal_assumption_import_audit_2026_06_06.txt)

---

## Role

Runs the repo's formal **Assumption-and-Import Audit + Counterfactual Pass** (the
"exercise":
[`physics-loop/references/assumption-import-audit.md`](ai_methodology/skills/physics-loop/references/assumption-import-audit.md))
on the **staggered-Dirac realization gate**
([STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md),
audited_renaming). This is the systematic version of the earlier ad-hoc pass
(#2956): a full import ledger + a scored counterfactual table over every implicit
framework choice + a synthesis with the allowed-outcome class per row.

## 1. Import ledger (every load-bearing item classified)

| Item | Class | Load-bearing | Disposition / retirement |
|---|---|---|---|
| staggered carrier (1 Grassmann/site) | zero-input structural | yes | **forced** by `{Quantum (dim 2), Locality}` (#2956) |
| fermionic (Grassmann) statistics | framework-derived | yes | substep-1 per-site dim matching (**retained_bounded**) |
| Kähler-Dirac operator equivalence | framework-derived | yes | substep-2 (**retained_bounded**; Becher–Joos comparator) |
| BZ-corner / species reduction | framework-derived | yes | substep-3 (**retained**) |
| AC_λ simultaneous diagonalization | framework-derived | yes | substep-4 (**retained**) |
| species-**label** identification (e/μ/τ) | admitted normalization | yes | `= AC_φλ`; **recordable lens** #2910/#2917/#2923 |
| single-link nearest-neighbour hopping | zero-input structural | yes | Locality axiom |
| continuum Dirac limit | support-only | **no** | **demote** — not supplied/needed (permanent lattice) |

No load-bearing item is an `unsupported import` or a `fitted input`.

## 2. Counterfactual pass (scored, over implicit framework choices)

| Assumption | Concrete alternative | Feasibility | Score | Allowed outcome |
|---|---|---|---|---|
| matter is fermionic (Grassmann) | per-site boson (CCR) | infeasible | 0 | forced finding |
| one Grassmann/site (staggered) | Wilson 4-component spinor | infeasible | 0 | forced finding |
| one Grassmann/site (staggered) | naive 4-comp (+doublers) | infeasible | 0 | forced finding |
| realization is local (single link) | overlap / domain-wall | infeasible | 0 | forced finding |
| matter lives ON the qubit (occupation) | extra dof beyond the qubit | infeasible | 0 | forced finding |
| tastes are the qubit (no extra index) | separate flavor index | infeasible | 0 | forced finding |
| operator is (Kähler-)Dirac | second-order / scalar carrier | live | 1 | derive from retained (substep-2) |
| continuum limit is a required closure | permanent physical lattice (no continuum) | live | 2 | **demote** |

Quantitative anchors (runner): per-site Fock dim — staggered `2¹=2` (= qubit dim,
local), Wilson/naive `2⁴=16` (= four qubits/site), boson `∞`, overlap nonlocal. So
the six carrier/realization counterfactuals are **infeasible against
`{Quantum (one qubit/site, dim 2), Locality}`**.

## 3. Synthesis

The exercise's allowed outcomes (no new axiom invented — the forbidden outcome):

1. **Forced finding (×6).** The carrier and realization choices have **no live
   alternative**: bosonic, Wilson, naive, overlap, extra-dof, and extra-index are
   all infeasible against `{Quantum, Locality}`. The staggered (KS) carrier is
   **fixed, not chosen**.
2. **Derive-from-retained (×1).** The "is it Dirac?" counterfactual resolves into
   the staggered ≅ Kähler-Dirac equivalence — substep-2, now **retained_bounded**.
3. **Demote (×1).** The continuum Dirac limit is **not a required closure**: the
   Locality axiom "does not supply a ... continuum or infrared limit"
   (MINIMAL_AXIOMS_2026-06-05) — the lattice is the physical substrate, so
   continuum recovery is an emergent consistency check, not a gate to close.

Combined with the live ledger (all four substeps now retained/retained_bounded)
and the species-label residual being recordable-lens-addressed
(`= AC_φλ`, #2910/#2917/#2923):

> **The staggered-Dirac realization "gate" is essentially closed.** Its framework
> choices are **forced** (not admitted), its substeps are **retained**, its one
> named irreducible residual (the species-label `AC_φλ`) is **recordable-native**,
> and the continuum residual is **demoted** by the permanent-lattice axiom. No
> new-axiom-free route remains *open* except reproving the (already
> retained_bounded) Kähler-Dirac equivalence deeper.

This corrects the earlier "deep wall, steer away" characterization: the exercise
shows the gate's surrounding choices are genuinely **forced**, and the residual
is in addressed/demoted items — exactly the "forced finding" outcome the protocol
describes (the blocker, if any, is in load-bearing imports, all of which are here
structural/derived/admitted-with-narrow-role).

## Scope and honest residual

- The exercise classifies and scores; it does **not** itself reprove substep-2
  (the Kähler-Dirac equivalence) at greater depth — that is the one remaining
  `live` derive-from-retained route, and it is already retained_bounded.
- The continuum **demotion** is a scope statement (the framework needs no
  continuum), not a continuum-limit theorem.
- No new axiom; the dim counting is representation theory, the locality is the
  Locality axiom, the continuum exclusion is the axiom text.

## Reprove-and-cite ledger

- **Reproven here** (runner): the import-ledger class validity (no unsupported
  import / fitted input); the per-site Fock-dim counting underlying the six
  infeasible counterfactuals; the counterfactual feasibility/score table; the
  synthesis bookkeeping.
- **Cited**: the assumption-import + counterfactual protocol
  (`physics-loop/references/assumption-import-audit.md`); the four substeps and
  the closure synthesis; the carrier-forcing (#2956); the Quantum/Locality axioms
  and the continuum-exclusion text (`MINIMAL_AXIOMS_2026-06-05`); the species-label
  `AC_φλ` recordable-lens treatment (#2910/#2917/#2923); the staggered ≅
  Kähler-Dirac equivalence (Becher–Joos, comparator).

## Audit dependency repair links

- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- [STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md)
- [STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
