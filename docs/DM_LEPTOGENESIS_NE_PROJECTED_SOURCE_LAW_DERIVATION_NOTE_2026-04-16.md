# DM Leptogenesis `N_e` Projected-Source-Law Derivation

**Claim type:** bounded_theorem

**Date:** 2026-04-16  
**Script:** `scripts/frontier_dm_leptogenesis_ne_projected_source_law_derivation.py`  
**Framework baseline:** Lattice, Qubit, Admissibility, and Record axioms.

## Status

Conditional finite-fixture reduction from the PMNS microscopic source-response
lane to a labeled DM transport packet.

This note upgrades the flavored-PMNS DM reduction.

The earlier DM reduction said the remaining PMNS-side object was the active
five-real source. That was true if one only used:

- branch/orientation,
- seed averages,
- support pattern,
- and the supplied finite transport functional.

But the PMNS microscopic source-response theorem is stronger than that.

## Question

On the charged-lepton-active branch `N_e`, what is the smallest PMNS-side
object actually needed to derive the transport-relevant flavored DM column?

Do we still need the full active five-real source

`(xi_1, xi_2, eta_1, eta_2, delta)`?

Or, on the supplied simple-spectrum fixture with ascending eigenvalue labels,
is there a smaller source-response object that determines the relevant
column?

## Bottom line

There is a smaller conditional input on that supplied fixture.

On the supplied `N_e` fixture, the selected transport column is derivable from
the charged-lepton projected Hermitian source law together with its explicit
simple-spectrum and ascending-label convention:

`dW_e^H`.

The reduction is algorithmic conditional on the supplied transport fixture:

1. `dW_e^H` reconstructs the active charged-lepton Hermitian block `H_e`
2. for the supplied simple-spectrum `H_e`, ascending eigenvalue labels define
   the three eigenspaces, and the `N_e` packet is `|U_e|^2^T`
3. the supplied finite DM transport functional `F_K` acts on the three packet
   columns
4. therefore the selected flavored transport column is algorithmic for this
   labeled fixture once `dW_e^H` is known

So for the PMNS-assisted DM repair route, we do **not** need the raw active
five-real source as the final target.

We need the projected Hermitian charged-lepton source law.

## Conditional finite-fixture reduction

### 1. Projected Hermitian source pack determines `H_e`

For a `3 x 3` Hermitian block, the nine real linear responses

`X -> Re Tr(X H_e)`

on the standard Hermitian basis determine `H_e` exactly.

So the charged-lepton projected Hermitian source law `dW_e^H` fixes `H_e`
exactly.

### 2. A supplied simple-spectrum, ascending-labeled `H_e` determines the `N_e` packet

On the one-sided charged-lepton-active branch, the passive side is monomial and
contributes only ordering/permutation data already fixed elsewhere.

For the supplied fixture, `H_e` has three separated eigenvalues. Labeling its
one-dimensional eigenspaces in ascending eigenvalue order fixes the columns up
to phases, which disappear after taking absolute squares. Under that explicit
label convention the active packet is

`|U_PMNS|^2 = |U_e|^2^T`.

Thus the supplied simple-spectrum, ascending-labeled `H_e` determines this
`N_e` packet. Degenerate spectra, or relabeling without an external convention,
are outside this claim. The runner's displayed six-decimal reference is checked
entrywise to within half a unit in its final displayed digit.

### 3. The supplied finite transport functional orders the columns

Given the supplied one-source flavored equation, profiles, and finite
quadrature, the branch uses

`F_K(P) = Σ_alpha Psi_K(P_alpha)`.

Applying this to the three columns of the supplied `N_e` packet orders those
three finite columns.

On the supplied labeled `N_e` fixture, the middle column is first under both
the finite functional and the helper's direct ODE computation. This is not a
derivation of a physical yield or readout map.

## Consequence

This changes the last-mile input for the supplied simple-spectrum fixture.

What is not needed as a separate input for this calculation:

- the raw active five-real source law

What replaces it on this fixture:

- the charged-lepton projected Hermitian source law `dW_e^H`

because once `dW_e^H` is known:

- `H_e` is known
- the packet is known for a supplied simple spectrum and ascending-label
  convention
- the finite-fixture transport ordering of those labeled columns is known

So this conditional finite-fixture PMNS contribution is smaller than the
earlier five-real formulation.

## What this finite fixture establishes

For the supplied simple spectrum and ascending labels, the finite `N_e`
calculation can use the projected charged-lepton Hermitian source law instead
of the raw PMNS corner-source coordinates. This does not establish a universal
target reduction for degenerate or differently labeled packets.

## What this does not close

This note does **not** yet evaluate `dW_e^H` from the current four-axiom
framework baseline.

It proves only that once `dW_e^H`, a simple-spectrum/ascending-label convention,
and the supplied transport fixture are available, the finite `N_e` column
ordering is downstream algorithmic.

So the live remaining gap is now:

- derive `dW_e^H` on `E_e` from the current four-axiom framework baseline

not:

- derive the full active five-real PMNS source law.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_ne_projected_source_law_derivation.py
```

## Inputs and related results

Runner inputs:

- `scripts/dm_leptogenesis_exact_common.py` — supplies `exact_package`
  and the source-side normalisation used by the runner.
- `scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py`
  — supplies the conditional finite flavored-column functional and its
  `F_K` action on supplied packet columns.
- `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py`
  — supplies the PMNS-projector interface used by §2 to convert
  `H_e` into the `N_e` packet `|U_PMNS|^2 = |U_e|^2^T`.

Related results:

- [DM_LEPTOGENESIS_EXACT_KERNEL_CLOSURE_NOTE_2026-04-15.md](DM_LEPTOGENESIS_EXACT_KERNEL_CLOSURE_NOTE_2026-04-15.md)
  — supplies the source-side `exact_package` with `gamma`, `E1`, `E2`,
  used as the source-oriented input to the projected-source law.
- [DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md)
  — supplies the conditional integrating-factor identity and finite transport
  functional referenced in §"Bottom line" item 3 and
  §"Conditional finite-fixture reduction" §3;
  it does not derive the transport equations, profiles, packet, or physical
  readout.
- [DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md)
  — supplies the PMNS-projector interface used to bridge from `H_e`
  to the `N_e` packet for the supplied simple-spectrum, ascending-labeled
  fixture (§"Conditional finite-fixture reduction" §2).
- [DM_LEPTOGENESIS_NE_CHARGED_SOURCE_RESPONSE_REDUCTION_NOTE_2026-04-16.md](DM_LEPTOGENESIS_NE_CHARGED_SOURCE_RESPONSE_REDUCTION_NOTE_2026-04-16.md)
  — charged-source response reduction, supplying the
  `dW_e^H -> H_e` reconstruction step in
  §"Conditional finite-fixture reduction" §1.
- [DM_LEPTOGENESIS_NE_ACTIVE_COLUMN_AXIOM_BOUNDARY_NOTE_2026-04-16.md](DM_LEPTOGENESIS_NE_ACTIVE_COLUMN_AXIOM_BOUNDARY_NOTE_2026-04-16.md)
  — finite four-summary ambiguity diagnostic for the `N_e` active-column
  calculation.

## Related context

`DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_TRIPLET_SIGN_THEOREM_NOTE_2026-04-16.md`.
Its runner imports `hermitian_linear_responses` from the present runner as a
sign-orientation companion calculation.

None of these inputs derives `dW_e^H` on `E_e` from the current framework
baseline; that remains outside this finite-fixture calculation.
