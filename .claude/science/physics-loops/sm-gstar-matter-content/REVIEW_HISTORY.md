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

## Cycle 2 self-review (review-loop, branch-local) — 2026-05-29

Branch `physics-loop/sm-gstar-retire-fsb-u1y-residuals-2026-05-29`. Deliverable:
`docs/SM_GSTAR_RESIDUAL_RETIREMENT_FSB_U1Y_BOUNDED_NOTE_2026-05-29.md` +
`scripts/frontier_sm_gstar_residual_retirement_fsb_u1y_2026_05_29.py`. Retires
two named census residuals (R-FSB, R-U1Y) to retained-sourced for the g_*
dof-count. Disposition: **pass** (local). Independent audit lane owns the
verdict.

### Findings

1. **Claim-status firewall.** `Claim type: bounded_theorem`; `Status authority:
   independent audit lane only`. No bare `retained`/`promoted` status line. The
   note explicitly states it does NOT claim the full fermionic-SB law or the
   hypercharge values are derived, and does NOT promote/demote any cited
   authority. Runner §6 asserts these. **PASS.**

2. **Honest re-sourcing, not over-claim.** R-FSB: g_* consumes only the
   dimensionless 7/8 ratio, which IS the retained
   `hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor` (R_lat(3)=7/8,
   eta(4)/zeta(4)=7/8). The stronger full fermionic-SB law stays unaudited and
   separately blocked (note §1.3). R-U1Y: g_* consumes only the one-abelian-
   factor RANK, the gl(1) of the retained gl(3)+gl(1) commutant; the hypercharge
   VALUES stay bounded/unaudited and separated (note §2.3). The runner's
   separation check confirms the dof count is invariant under eigenvalue
   rescaling (values not a dof input). **PASS** (re-sourcing for the dof count,
   not a derivation of the stronger statements).

3. **Ledger statuses verified (not from prose).** Read from
   `docs/audit/data/audit_ledger.json` on 2026-05-29:
   `hierarchy_seven_eighths_..._2026-05-10` = retained; `native_gauge_closure_note`
   = retained; `graph_first_su3_integration_note` = retained;
   `axiom_first_fermionic_stefan_boltzmann_..._2026-05-26` = unaudited;
   `standard_model_hypercharge_uniqueness_..._2026-04-24` = unaudited;
   `hypercharge_identification_note` = retained_bounded. Runner §5 cross-checks
   these as executed asserts. **PASS.**

4. **Citation-graph hygiene.** The three retained sources are markdown links
   `[FILE.md](FILE.md)` (load-bearing edges). The separated stronger statements
   (full fermionic-SB, hypercharge uniqueness) are plain-text pointers (no
   markdown link) so the citation-graph builder does not record them as
   load-bearing retained edges. Runner §4 asserts the link/plain-text split.
   **PASS.**

5. **No new repo vocabulary.** `vocab_lint --fix` reports 0 violations. The note
   mirrors the bounded-theorem template (status-authority surface, verification
   section, assumptions-and-imports ledger, independent-audit handoff,
   author-tone-and-boundary closing). No new tags/meta-framings. **PASS.**

6. **No audit-lane data touched.** `git status` shows only the new `docs/*.md`
   note, the new `scripts/*.py` runner, and `.claude/science/physics-loops/...`
   loop-pack updates. No `docs/audit/data/*` or `docs/audit/AUDIT_*.md`. The
   audit pipeline was not run for this PR. **PASS.**

7. **Runner.** `PYTHONPATH=scripts python3
   scripts/frontier_sm_gstar_residual_retirement_fsb_u1y_2026_05_29.py` ->
   `PASS=63 FAIL=0`. All dof / ratio / rank checks are EXECUTED asserts with
   `fractions.Fraction`. **PASS.**

### Local disposition: pass

No local fixes required. The PR may be opened as a bounded_theorem residual-
retirement companion. Independent audit owns the verdict; a first verdict of
`audited_conditional` with `dependency_not_retained` on the still-open R-POL
2-polarization factor is the expected bookkeeping.
