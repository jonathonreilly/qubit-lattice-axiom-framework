# ROUTE PORTFOLIO — SM g_* matter-content derivation

## Candidate routes

### Route A — full-assembly-now (claim all dof framework-derived)

Source every dof count from framework structure and claim g_* fully derived /
retained.

- **Pro:** maximal claim.
- **Con:** DISHONEST. U(1)_Y (unaudited), single-Higgs-doublet (assumed),
  one-generation matter completion (unaudited/convention), full fermionic-SB
  (unaudited), massless-vector 2-pol (unaudited, emergent-Lorentz under repair)
  are NOT retained. Claiming full derivation violates the no-new-axiom rule and
  the claim-status firewall. **REJECTED.**

### Route B — assemble-retained-core-and-name-residuals (CHOSEN)

Source each dof count from its actual framework authority with its true ledger
status; assemble g_* = 106.75 from the retained core (SU(3), SU(2), n_gen=3,
7/8 ratio, spin-statistics cardinality, hypercharge-value enumeration,
singlet-completion) PLUS explicitly named residuals (U(1)_Y existence,
single-Higgs-doublet, one-gen matter completion + neutral-singlet convention,
full fermionic-SB, massless-vector 2-pol, per-site spin-1/2). Honest claim:
**bounded_theorem**. Retire the monolithic external "declared SM census" import;
replace with framework-internal assembly whose residuals are framework-
derivation targets. Queue residuals for retirement.

- **Pro:** honest; genuinely retires the opaque external census import; moves
  claim state forward (monolithic external import -> framework assembly with
  named internal residuals); each residual becomes a tracked derivation target.
- **Con:** does not fully close g_*; several pieces stay bounded/unaudited.
  This is the correct ceiling per the no-new-axiom rule.
- **MOVES CLAIM STATE HONESTLY. CHOSEN.**

### Route C — derive-one-missing-piece-first (e.g. single-Higgs-doublet)

Spend the cycle deriving one residual (e.g. single-doublet minimality) before
assembling.

- **Pro:** would close one residual.
- **Con:** single-doublet minimality is a hard open problem (the repo has only
  specific two-Higgs-slot no-gos, not a general minimality theorem); attempting
  it as a gating step risks the whole cycle ending in a no-go without the
  import-retirement landing. The import-retirement (Route B) is the
  higher-value, lower-risk move; the single-piece derivations are properly
  queued as follow-on residual-retirement work (HANDOFF.md). **DEFERRED to
  follow-on.**

## Scoring

| Route | claim-state movement | honesty | landability | risk | score |
|---|---|---|---|---|---|
| A full-now | high (if true) | FAILS | low (firewall block) | high | reject |
| B assemble+residuals | medium-high (retires monolithic import) | high | high | low | **CHOSEN** |
| C derive-piece-first | medium (one residual) | high | medium | high (may no-go) | defer |

## Chosen route: B

Assemble g_* = 106.75 from framework structure, sourcing each dof count from its
true-status authority, naming residuals explicitly, claiming bounded_theorem,
retiring the monolithic external SM-census import. Queue residual retirements.

## PROMOTION VALUE GATE (mandatory pre-PR self-review)

This loop's goal is a positive import-retirement (retiring the declared-SM
inventory import). The V1-V5 gate is therefore mandatory. This record is NOT an
audit certificate and does not predict an audit verdict.

| # | Question | Answer |
|---|---|---|
| **V1** | What SPECIFIC obstruction does this close? | The exact text in `sm_relativistic_dof_count_import_note_2026-05-17`: *"The declared Standard Model inventory remains an external physical input. This finite declared-inventory arithmetic certificate is not a framework derivation of which particles nature contains."* and its boundary list item *"a framework derivation of the Standard Model particle inventory"*. This PR retires the **monolithic external** status of that inventory by sourcing each dof count from framework structure (gauge group, generation count, matter content) with named residuals. |
| **V2** | What NEW derivation does this PR contain that the audit lane / existing notes don't already have? | The existing `..._FROM_SUPPLIED_THERMAL_INVENTORY_...note_2026-05-28` (unaudited) does the **arithmetic** proof-walk B1-B13 but holds the **particle inventory itself (its premise P1)** as a *supplied premise*, explicitly NOT deriving the inventory. The NEW content here is the **inventory-sourcing decomposition**: a per-dof "Derived vs residual-input" table that maps the gauge-group content to retained SU(3)/SU(2) + named U(1)_Y residual, the generation count to retained n_gen=3, the matter content to one-generation completion + hypercharge authorities, and the single-Higgs-doublet to a named residual. This converts P1 from a monolithic external premise into a framework-internal assembly with named residuals — the part the existing note explicitly leaves external. The runner makes each *sourcing* check an EXECUTED assert (not prose), per the audit-miss lesson. |
| **V3** | Could the audit lane already complete this from existing retained primitives + standard math? | **No** for the inventory-sourcing claim. Standard math gives the *arithmetic* (24+4=28, 3*30=90, the 7/8 combination) — and indeed the existing note already has that. What standard math does NOT give is the mapping of each dof count to a specific framework authority with its true status and the honest separation of derived-vs-residual. That mapping requires the framework's retained gauge/generation theorems (SU(3) from graph_first_su3, SU(2) from Cl(3) bivectors, n_gen=3 from three-generation observable) and the honest residual identification (U(1)_Y unaudited, single-doublet assumed, etc.). The framework primitives are necessary to assert which pieces are framework-internal vs external. |
| **V4** | Is the marginal content non-trivial? | **Yes.** The non-trivial content is the *retirement of the monolithic external census import*: showing that the inventory is no longer an opaque external SM input but a framework assembly whose residuals are themselves framework-derivation targets. The counterfactual pass (esp. C-c neutrino sector: g_* = 112 if nu_R thermalized Dirac; C-a regime; C-b emergent-Lorentz dependence of the 2-pol count) is genuinely new analysis of which dof choices are load-bearing and which framework results close them. This is not a textbook identity. |
| **V5** | Is this a one-step variant of an already-landed cycle? | **No.** The closest prior note is `..._FROM_SUPPLIED_THERMAL_INVENTORY_...note_2026-05-28`. The structural distinction: that note's load-bearing premise P1 is *"declared SM particle inventory ... declared explicitly ... not derived from the framework here"* — it imports the inventory wholesale. This loop's load-bearing content is *sourcing the inventory itself from framework structure with named residuals*. That is a different load-bearing premise (inventory-sourcing vs inventory-as-premise), not a relabeling of the same arithmetic. The arithmetic (B1-B13) is shared and explicitly cited as prior work; the delta is the inventory decomposition. |

**Gate verdict: PASS all V1-V5.** PR allowed. Honest claim type:
**bounded_theorem** (NOT retained/positive — independent audit owns the verdict;
residuals named and queued).

## Corollary-churn check

Is the output a one-step algebraic corollary of an already-landed cycle? No —
see V5. The arithmetic is shared with the 2026-05-28 note and explicitly cited;
the new load-bearing content is the inventory-sourcing decomposition + the
counterfactual analysis of which framework results close which dof choices. The
runner's dof-sourcing asserts (SU(3) dim 8 -> 16; SU(2) dim 3 -> 6; U(1) 1 -> 2;
massless vector -> 2 pol; per-gen matter -> 30) are NEW executed checks tying
each count to its structural source, not a repeat of the bare arithmetic.
