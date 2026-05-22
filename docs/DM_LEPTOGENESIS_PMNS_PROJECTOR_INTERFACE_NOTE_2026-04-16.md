# DM Leptogenesis PMNS Projector Interface

**Claim type:** bounded_theorem
**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-16  
**Script:** `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py`  
**Framework convention:** baseline physical framework means `Cl(3)` local algebra on the `Z^3` spatial substrate. Historical axiom-side wording below is lane terminology, not a new repo-wide axiom.

## Status

Exact interface theorem plus diagnostic transplant from the active neutrino /
PMNS lane.

This note does **not** promote a new DM authority value. It identifies the
right imported object from the PMNS lane and quantifies what it would do on the
current exact DM transport branch.

## Question

Does the active neutrino / PMNS lane already contain something useful for the
DM flavored-transport mismatch, or do we need to invent the flavored projector
structure from scratch on the DM branch?

## Bottom line

We should borrow from the PMNS lane, not start from scratch.

The neutrino lane already fixes the correct transport-facing carrier:

- the exact remaining neutrino target is the Hermitian pair `((H_nu,H_e), s)`
- once that pair is supplied, the PMNS matrix is readable
- the flavored transport projector packet is then automatic:

`P_i(alpha) = |U_PMNS(alpha,i)|^2`

So the DM flavored-transport problem is not “invent a new projector family.”
It is “derive the relevant PMNS pair law or projector column.”

## Pair-to-projector interface

The active neutrino lane already proves:

- the lepton supports `E_nu` and `E_e` are fixed
- the remaining full target is `((H_nu,H_e), s)`
- PMNS data are readable from that pair once it is supplied

On the DM branch, this yields the exact interface:

1. diagonalize `H_nu` and `H_e` by their left unitary diagonalizers
2. form `U_PMNS = U_e^dag U_nu`
3. define the flavored transport packet by column magnitudes

`P_i = (|U_{e i}|^2, |U_{mu i}|^2, |U_{tau i}|^2)`

This packet is intrinsic to the Hermitian pair:

- it is phase-insensitive
- it does not require a new support-selection theorem
- it gives exactly the non-democratic flavor weights that the new DM transport
  diagnostic needs

## Canonical `N_nu` sample

On the canonical neutrino-side sample imported from the PMNS lane, the
pair-conditioned packet is

`[[0.502364, 0.158615, 0.339021],
  [0.096835, 0.536381, 0.366784],
  [0.400801, 0.305004, 0.294195]]`

Feeding those three columns into the exact single-source flavored DM transport
diagnostic gives

- `eta/eta_obs = 0.767519440713`
- `eta/eta_obs = 0.725015701233`
- `eta/eta_obs = 0.694205905212`

So the PMNS transplant already gives a large lift over the exact one-flavor
authority value `0.188785929502`.

## Canonical `N_e` sample

On the canonical charged-lepton-side PMNS sample, the pair-conditioned packet
is strongly hierarchical:

`[[0.915868, 0.071267, 0.012865],
  [0.074689, 0.900307, 0.025004],
  [0.009443, 0.028427, 0.962131]]`

Its columnwise flavored DM transport values are

- `eta/eta_obs = 0.820755501975`
- `eta/eta_obs = 0.989512597197`
- `eta/eta_obs = 0.920617013914`

So a PMNS pair law can in principle erase almost the whole exact DM transport
miss without needing a large new `N2` source.

## Consequence

This sharpens the DM last-mile target again.

What the PMNS lane already supplies:

- the right carrier
- the right pair-level interface
- an intrinsic flavored-projector packet once the pair is supplied

What it still does **not** supply:

- the positive axiom-side pair law itself
- a theorem selecting which PMNS column is the physical `N1` transport column

So the remaining DM target is no longer “derive flavored projectors from
nothing.” It is:

- derive the relevant PMNS pair law, or at least the transport-relevant PMNS
  projector column, from `Cl(3)` on `Z^3`

## What this closes

This closes the route-choice question.

The active neutrino lane is directly useful for DM. It is not just background
or analogy. It supplies the exact pair-to-projector interface the DM transport
extension needs.

## What this does not close

This note does **not** promote a new theorem-authority `eta` value, because the
pair law itself is not yet derived on the DM branch.

It is an interface theorem plus a diagnostic transplant.

## Conditional structure (explicit)

This note's content factors into one closed algebraic step plus two named open
dependencies. The runner's Parts 1 and 4 make this structure executable, so the
conditional shape is legible from the runner output rather than masked by
unconditional bottom-line assertions.

- **Closed (algebraic):** given any positive-definite Hermitian pair
  `(H_nu, H_e)`, the flavored transport packet
  `P_i(alpha) = |U_PMNS(alpha,i)|^2` is doubly stochastic, phase-insensitive,
  and pair-readable. The runner's Part 1 verifies this on the canonical pair
  plus eight deterministic random Hermitian pairs (72 rephasing samples in
  total) at numerical-zero accuracy.
- **Open (carrier authority):** the active neutrino lane fixes the Hermitian
  pair `((H_nu,H_e), s)` as the remaining full target carrier. The positive
  PMNS pair law from `Cl(3)` on `Z^3` is not derived in this note. The
  runner's Part 4 leaves this dependency explicitly unresolved (its
  resolution string begins with `open:`).
- **Open (physical column authority):** a theorem on the active neutrino
  lane selecting which PMNS column is the physical `N1` transport column.
  This selection is not derived in this note. The runner's Part 4 leaves
  this dependency explicitly unresolved (its resolution string begins with
  `open:`).

The diagnostic `eta/eta_obs` values reported in Parts 2 and 3 are columnwise
readouts of the algebraic interface on two canonical sample pairs; they do
not load-bear on the open dependencies.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_projector_interface.py
```

## 2026-05-19 audit-conditional repair

This block makes the retained scope and the imported admissions explicit, so the
note's `bounded_theorem` claim type maps cleanly onto only what the paired
runner actually verifies.

**Retained scope (class-A facts the runner verifies at numerical-zero):**

- For any positive-definite Hermitian pair `(H_nu, H_e)` and the induced
  `U_PMNS = U_e^dag U_nu`, the matrix `U_PMNS` is unitary. Verified by the
  runner on the canonical pair plus eight deterministic random Hermitian
  pairs (`max ||U U^dag - I||` at numerical-zero accuracy in Part 1).
- The flavored transport packet `P_i(alpha) = |U_PMNS(alpha,i)|^2` is doubly
  stochastic (rows and columns each sum to 1) on every sampled pair. Verified
  by the runner in Part 1.
- `|U_PMNS|^2` is invariant under independent left-eigenvector rephasings
  (diagonal unitaries on the left of `u_nu` and `u_e`). Verified by the
  runner on 72 rephasing samples (9 Hermitian pairs * 8 rephasings each) in
  Part 1, at numerical-zero accuracy.
- Therefore the pair-conditioned packet
  `P_i(alpha) = |U_PMNS(alpha,i)|^2` is pair-readable and phase-insensitive
  as a function of `(H_nu, H_e)`, conditional on the carrier being supplied.

The columnwise `eta/eta_obs` diagnostic readouts in Parts 2 and 3 of the
runner are conditional numerical evaluations of this algebraic interface on
two canonical sample pairs. They are not retained-scope content of this note
and do not load-bear on any authority promotion.

**Admitted context (explicit imports, NOT derived in this note or runner):**

- **Carrier authority.** That the remaining full target carrier on the active
  neutrino lane is the Hermitian pair `((H_nu, H_e), s)` rather than some
  other object is imported from the active neutrino / PMNS lane. This note
  does not derive carrier authority from `Cl(3)` on `Z^3` from the sole
  axiom. The paired runner's Part 4 carries this as an explicit admission
  with resolution string beginning `open:`.
- **Physical-column selection.** That a particular column of `|U_PMNS|^2`
  is the physical `N1` transport column is imported. No theorem selecting
  the transport-physical column on the active neutrino lane is derived in
  this note. The paired runner's Part 4 carries this as a second explicit
  admission with resolution string beginning `open:`.

**Audit-conditional status.** The note is retained at `bounded_theorem`
strictly for the class-A facts above. The two admissions are required to
turn any columnwise `eta/eta_obs` readout in Parts 2 and 3 of the runner
into a physical leptogenesis statement; they are out of retained scope
here. No new repo-wide authority is promoted by this repair.
