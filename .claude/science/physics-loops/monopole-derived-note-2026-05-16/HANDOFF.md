# Handoff — monopole-derived-note 2026-05-16

## What was done (iter35)

Closed the missing-derivation work for `docs/MONOPOLE_DERIVED_NOTE.md`
flagged by the 2026-05-15 audit (verdict: `audited_numerical_match`).

### Changes

1. `docs/MONOPOLE_DERIVED_NOTE.md` rewritten to:
   - Re-title to "Magnetic Monopole Mass: Bounded Lattice Derivation".
   - State `Claim type: bounded_theorem` and `Status: Bounded` up front.
   - Distinguish the **derived c_lat = 0.2527** from the **imported
     beta = 1/(4*pi*alpha_EM(M_Pl)) ~ 5.738** and the **pinned
     a^(-1) = M_Pl**.
   - Present `M_mono = 1.43 M_Pl` as a **conditional numerical prefactor**
     and `M_mono ~ M_Planck` as the **import-robust** order-of-magnitude
     headline (across `alpha^-1` in [30, 60] gives M in [0.60, 1.21] M_Pl).
   - Re-scope Step 4 from "direct numerical self-energy" to a **topology
     check**. Explain that the bare Wilson action of the constructed Wu-Yang
     field is dominated by Dirac-string artifacts, so the reported
     `Delta S` is not a self-energy of the monopole core. The
     load-bearing Step 4 facts are now: (a) every plaquette charge is
     integer, (b) total charge is zero, both at every L in {6, 8, 10, 12}.
   - Add an "Assumptions and Imports (Explicit Ledger)" section that
     names every import, its role, and what it leaves underived.
   - Add a "Reconciliation Note (2026-05-16)" that summarizes the audit
     verdict and the corrective response (1:1).

2. `scripts/frontier_monopole_derived.py` updated to:
   - Module docstring rewritten to be honest about which steps are derived
     and which are bounded by named imports.
   - Step 3 prints now label `alpha_EM(M_Pl)` as a **named non-derivation
     import** and announce the conditional vs. import-robust split.
   - Step 4 renamed to `step4_topology_check` (with a backwards-compat
     alias `step4_numerical_self_energy` that routes to the new function);
     output explicitly labels the bare action as a diagnostic, not a
     self-energy measurement, and provides a per-L topology pass/fail.
   - Synthesis scorecard rewritten to match: each row carries a class
     label (DERIVED / BOUNDED / ROBUST / NOT DONE / PASS / VERIFIED), and
     the bottom of the synthesis lists the named imports and the
     not-derived items.

### Verification

- Runner runs end-to-end with exit code 0 in ~0.5s (`python3
  scripts/frontier_monopole_derived.py`).
- `G_lat(0)` at L=64 prints 0.2492, within 1.5% of the infinite-volume
  BKM value 0.2527 (finite-volume correction).
- Step 4 topology check passes at L in {6, 8, 10, 12}: all charges
  integer, sum of charges = 0 on every L.
- Step 3 conditional prefactor reproduces `1.43 M_Pl` as before.

## What did NOT change

- The framework axioms.
- The publication disposition ("bounded companion only" in
  `docs/publication/ci3_z3/FULL_CLAIM_LEDGER.md`).
- The Step 1, Step 2, Step 5 derivations.
- The numerical value `c_lat ~ 0.2527` (only its derivation status was
  always derived; this iteration just made the labeling consistent).

## What was deliberately NOT attempted (out of 60-min scope)

- A first-principles derivation of `alpha_EM(M_Pl)` from the lattice
  axiom packet. That would retire the load-bearing import but is its own
  multi-day project and is out of scope.
- Implementing a correct numerical self-energy measurement (Monte Carlo
  free-energy or DeGrand-Toussaint dual-lattice string subtraction). The
  note now explains what would be required.
- A two-loop / threshold-matching `alpha_EM(M_Pl)` extrapolation. The
  one-loop value remains; the note flags the residual uncertainty.

## Next exact action

Push the branch and open the PR for re-audit. After audit, the next
possible work in this lane (if accepted as `audited_clean` at
bounded-support grade):

- Implement a Monte Carlo free-energy measurement of `c_lat` on the same
  compact U(1) action to make Step 4 a genuine cross-check (tightens the
  derived part).
- Survey the existing repo for an axiom-native definition of the monopole
  mass that does not require the gauge coupling as an import (would
  retire the load-bearing import).
