# EW kappa_EW: Register-Not-Read Registers All Color Sectors

**Date:** 2026-06-09
**Claim type:** no_go
**Type:** route-specific no-go source proposal
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:**
[`scripts/frontier_ew_kappa_registration_color_sector_nogo.py`](../scripts/frontier_ew_kappa_registration_color_sector_nogo.py)
**Runner cache:**
[`logs/runner-cache/frontier_ew_kappa_registration_color_sector_nogo.txt`](../logs/runner-cache/frontier_ew_kappa_registration_color_sector_nogo.txt)

## Scope

This note closes only the register-not-read route named in
[`RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md`](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md):

```text
If register-not-read identifies the I/sqrt(N_c) trace channel as an
unregistered reference, then the registered channel is the traceless adjoint
channel and kappa_EW = 0.
```

The claim here is that the antecedent fails for the supplied color
central-sector decomposition. It does not derive `kappa_EW = 1`, does not derive
`kappa_EW = 0`, and does not close any future non-registration selector.

## Setup

For a color matrix `G in End(C^N_c)`, decompose the operator space into the
trivial and adjoint irreps of the `SU(N_c)` adjoint action:

```text
G = P_1(G) + P_adj(G),
P_1(G) = (Tr G / N_c) I,
P_adj(G) = G - P_1(G),
S = ||P_1(G)||^2 = (1/N_c) |Tr G|^2,
C = ||P_adj(G)||^2.
```

The tested register-not-read channel is the block-dephasing map for a supplied
finite central-sector decomposition,

```text
D(rho) = sum_k P_k rho P_k.
```

This is a channel under test, not a new axiom and not something Record supplies
by itself. Record supplies no decomposition, weighting, normalization,
probability rule, measurement/decoherence dynamics, source/action bridge, or
readout selector.

The physical EW readout family remains

```text
Pi_phys(kappa_EW) = C + kappa_EW S.
```

## Route-Specific No-Go

1. **The singlet is a central sector.** `P_1` is `SU(N_c)`-equivariant:
   `P_1(U G U^dagger) = U P_1(G) U^dagger`. The singlet is the trivial irrep
   of the adjoint action, not inter-sector coherence.
2. **Registration keeps sector populations.** In the two-sector basis, a
   sector-resolved state has the form `rho = [[S, x], [x*, C]]`. The dephasing
   channel gives `D(rho) = diag(S, C)`: it removes the coherence `x` and keeps
   both diagonal populations.
3. **Dropping the singlet is not registration.** The `kappa_EW = 0` route would
   need `rho -> diag(0, C)`, discarding the already-registered singlet
   population `S`. That is not the block-dephasing map.
4. **The partition delivers counts, not the inter-sector weight.** The sector
   count gives the adjoint cardinality fraction `(N_c^2 - 1)/N_c^2`, equal to
   `8/9` for `N_c = 3`. It does not deliver the readout weight `kappa_EW` in
   `C + kappa_EW S`.
5. **The route is directionless.** The same loose slogan can also be pointed in
   the opposite direction: the physical EW bosons are color singlets, so keep
   the singlet and drop the confined adjoint. The supplied partition does not
   choose either direction.

Therefore register-not-read registers all central color sectors in this
decomposition and leaves `kappa_EW` undetermined. It does not supply
`kappa_EW = 0`.

## Relation to Existing Authority

- [`REGISTRATION_REINSTATES_CHIRALITY_NO_GO_NOTE_2026-06-07.md`](REGISTRATION_REINSTATES_CHIRALITY_NO_GO_NOTE_2026-06-07.md)
  supplies the retained no-go pattern: block-dephasing registers central-sector
  content and does not fix the within-block readout dial.
- [`EW_KAPPA_SELF_ENERGY_OBJECT_PIN_MC_UNDECIDABLE_NO_GO_NOTE_2026-06-08.md`](EW_KAPPA_SELF_ENERGY_OBJECT_PIN_MC_UNDECIDABLE_NO_GO_NOTE_2026-06-08.md)
  records that `kappa_EW` is not selected by the Monte Carlo object.
- [`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md)
  and [`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md) record the retained
  matching-rule underdetermination: `kappa_EW = 0` is an extra selector, not a
  consequence of the Fierz/channel-count packet.
- [`REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06.md`](REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06.md)
  is meta context for the directionless-register-not-read failure mode; it is
  not used as retained physics authority.
- [`RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md`](RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md)
  is the open gate this route-specific no-go attacks.

## No-Go Discipline Gate

Status: PASS for the scoped route only.

- **N1 alternatives.** Six routes were considered. Finer central partitions can
  add sectors but do not discard the trivial singlet. The trivial coarsening
  keeps the full trace `S + C`. Treating the singlet as a fixed normalization
  reference fails because `S` is a varying channel population. Making the
  singlet off-diagonal fails because it is the trivial irrep. Identifying
  `kappa_EW` with the `8/9` count fails because `K_EW(kappa_EW)` still depends
  on the separate weight. A future non-registration lattice-current/readout
  theorem is explicitly left open.
- **N2 wall independence.** The no-go has two independent parts: the dephasing
  map keeps the singlet population, and the partition does not deliver the
  inter-sector readout weight.
- **N3 hidden-wall scan.** The supplied inputs are explicit: color carrier,
  singlet/adjoint decomposition, block-dephasing channel, and the established
  `kappa_EW` readout family. No partition-selection or weight-selection rule is
  imported from Record.
- **N4 residual matching.** The residual matches the retained EW matching-rule
  and Monte Carlo no-gos: `kappa_EW` remains an external readout selector.
- **N5 rhetoric audit.** "Registration keeps the singlet" is an irrep-level and
  block-dephasing-level statement. It is not a claim that all possible future
  dynamics keep the singlet or that `kappa_EW` can never be fixed.
- **N6 partial-closure scan.** No convention closes the register-not-read route.
  The only possible closure is a distinct non-registration selector theorem,
  left open.
- **N7 steelman.** A critic could choose a non-central partition that mixes
  singlet and adjoint blocks. That no longer tests the supplied
  `SU(N_c)`-central color decomposition and would be a new admitted readout
  structure, not a register-not-read derivation from the current packet.
- **N8 cross-cycle echo.** This is the same failure pattern as the retained
  chirality no-go and the `r`-dial warnings: a partition can deliver sector
  data and counts while leaving a readout weight free.

## What This Does Not Claim

- It does not derive or force `kappa_EW = 1`.
- It does not derive or force `kappa_EW = 0`.
- It does not close a future retained non-registration selector for
  `kappa_EW`.
- It does not claim Record selects the color partition or supplies the
  block-dephasing dynamics.
- It makes no claim about `sin^2(theta_W)`.

## Verification

```bash
python3 scripts/frontier_ew_kappa_registration_color_sector_nogo.py
```

Expected result: `RUNNER STATUS: PASS (PASS=12 FAIL=0)`.

The runner checks the singlet/adjoint sector decomposition for
`N_c = 2, 3, 4, 5`, the `SU(N_c)`-equivariance of the singlet projector, the
block-dephasing action on sector populations, the failure of the singlet-drop
map to equal registration, the free `kappa_EW` readout weight, the Koide
`r`-dial parallel, and the directionless-sector-drop witness. It imports no
fitted numerical target.
