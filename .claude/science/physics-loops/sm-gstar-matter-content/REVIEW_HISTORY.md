# REVIEW HISTORY — SM g_* matter-content derivation

## Cycle 1 self-review (review-loop, branch-local) — 2026-05-29

Disposition: **pass** (local). Independent audit lane remains the authority on
effective status; this is a branch-local self-review, not an audit verdict.

### Findings

1. **Claim-status firewall.** The note's `Claim type:` is `bounded_theorem`;
   `Status authority:` is "independent audit lane only". No bare
   `retained` / `promoted` in any status line. The note explicitly states it
   "does not claim `g_*` is fully derived, retained, or positive." The runner's
   `check_no_overclaim` asserts the banned status phrases are absent and that
   the firewall sentence is present. **PASS.**

2. **Anti-churn vs `..._FROM_SUPPLIED_THERMAL_INVENTORY_...note_2026-05-28`.**
   The genuine delta — the inventory-sourcing decomposition that converts the
   monolithic external census into a framework assembly with named residuals —
   is explicit in §2 and answered in V2/V5 of the value gate. The shared
   arithmetic (B1-B13) is cited as prior work, not re-sold as the deliverable.
   The runner's dof-sourcing checks are NEW executed asserts tying each factor
   to its structural source. **PASS** (not corollary churn).

3. **Ledger statuses verified.** All sourcing-authority statuses were read from
   `docs/audit/data/audit_ledger.json` on 2026-05-29 (per "verify ledger before
   citing memory"), NOT from source-note prose: SU(3)/SU(2)/n_gen/N_c/
   cardinality/7-8-ratio = retained; hypercharge-enumeration / singlet-
   completion / hypercharge-identification / berezin = retained_bounded;
   per-site-spin-1/2 = audited_conditional; U(1)_Y-uniqueness / matter-closure /
   fermionic-SB / massless-vector-pol / one-Higgs-Yukawa = unaudited. The note's
   labels match. **PASS.**

4. **Counterfactual completeness.** All four required counterfactuals are
   recorded (C-a regime, C-b massless-vector polarization, C-c neutrino sector,
   C-d single Higgs doublet) plus C-e color, C-f generation, C-g 7/8. The
   neutrino caveat (g_* = 112 if nu_R thermalized Dirac) is the most load-bearing
   and is called out explicitly. The runner executes the C-b/C-c/C-d/C-e
   counterfactual arithmetic. **PASS.**

5. **No new repo vocabulary.** The runner's `check_forbidden_imports_and_vocab`
   asserts no new-vocabulary / meta-framing strings. `vocab_lint --fix` reports
   0 violations. The note mirrors the existing bounded-theorem note template
   (status-authority surface, forbidden-imports check, independent-audit
   handoff, author-tone-and-boundary closing). **PASS.**

6. **Citation-graph hygiene.** DERIVED (retained / retained_bounded) authorities
   are cited as markdown links `[FILE.md](FILE.md)` (load-bearing edges, so the
   citation graph sees them and dependency-not-retained bookkeeping is correct).
   RESIDUAL (unaudited / convention-bearing) authorities are cited as plain
   backticked filenames so the citation-graph builder does not parse them as
   load-bearing retained edges (canonical narrow-theorem pattern). No cycle risk
   (this note is new; no cited note cites back to it). **PASS.**

7. **No audit-lane data touched.** `git status` shows only
   `.claude/science/physics-loops/...`, the new `docs/*.md` note, and the new
   `scripts/*.py` runner. No `docs/audit/data/*` or `docs/audit/AUDIT_*.md`. The
   audit pipeline was not run. **PASS.**

8. **Runner.** `PYTHONPATH=scripts python3
   scripts/frontier_sm_gstar_from_framework_structure_2026_05_29.py` -> `PASS=117
   FAIL=0`. The dof-sourcing checks are EXECUTED asserts (not prose), per the
   audit-miss lesson. **PASS.**

### Local disposition: pass

No local fixes required beyond the one runner assertion correction (matching the
import note's wrapped blocker text). The PR may be opened as a bounded_theorem
import-retirement. Independent audit owns the verdict; the first verdict may
correctly be `audited_conditional` with `dependency_not_retained` given the
unaudited sourcing authorities — expected dependency bookkeeping.
