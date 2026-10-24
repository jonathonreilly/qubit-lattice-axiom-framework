# Lane 5 Separated-Input Route Inventory and Open Proof Obligation

**Date:** 2026-04-26
**Type:** open_gate
**Claim type:** open_gate
**Status:** conditional route inventory; the former necessity no-go is withdrawn.
**Status authority:** independent audit lane only; this source records no audit verdict.
**Scope:** the supplied expanding constant-density flat-FRW family at fixed
radiation fraction `R`, positive `H_0`, and `0 < L < 1-R`. This note does not
retire any of those premises or derive numerical cosmological inputs.
**Primary runner:** `scripts/frontier_hubble_lane5_cosmic_history_ratio_no_go_source_packet.py`
**Primary runner cache:** `logs/runner-cache/frontier_hubble_lane5_cosmic_history_ratio_no_go_source_packet.txt`

## 0. What is established

The supplied matter bridge gives `H_0 = H_inf/sqrt(L)` with
`L = Omega_Lambda = (H_inf/H_0)^2`. In the family where `H_inf` and `L`
are independently free positive parameters, fixing only one leaves a family
of `H_0` values. This conditional parameter-family result does not prove
independence of these quantities under the framework axioms, nor does it
prove that no physical derivation can impose a joint relation.

The former argument inferred non-derivability of dimensionless scale content
and `L` from a units-only primitive and a list of routes. That inference is
withdrawn. A units convention alone supplies no dimensionless physical law;
this fact does not imply that the other axioms cannot derive such a law.
No framework-wide non-derivability theorem is established here.

## 1. Reviewed separated-input routes

This is a bookkeeping taxonomy of the currently reviewed routes, not a proof
that no other route exists:

- **(C1) absolute-scale route:** separately supply or derive `H_inf` on the
  specified comparison-radius model, including its unresolved physical
  identification and normalization premises.
- **(C2) cosmic-history-ratio retirement:** obtain `L` from the bounded
  matter cascade after resolving its relevant inputs. Partial retirement of
  `eta` or `alpha_GUT` is progress within that cascade, not full `L` closure.
  `T_CMB`, radiation, BBN relations and any supplied `h` retain their own
  premises; this inventory does not retire them.
- **(C3) direct cosmic-`L` derivation:** separately supply or derive `L` by a
  different route. No physical impossibility follows from absence of a
  currently listed construction.

The primitive is a ruler, not the C1 route. It is a units conversion, not
an independently derived dimensionless normalization or cosmological law.
The listed C1 and C2 gate notes identify obligations on their own supplied
surfaces; citing them does not establish their physical completion.

## 2. Conditional family result and its limit

At fixed `L>0`, `H_0` changes linearly with `H_inf`. At fixed `H_inf>0`,
it changes as `L^(-1/2)`. Thus fixing only one independently free input
is insufficient **within this separated-input family**.

A joint relation is a counterexample to a universal two-input requirement:
if a future derivation supplied `H_inf = k sqrt(L)` for a fixed positive
inverse-time scale `k`, then `H_0=k` while `L` could remain free in
`0<L<1-R`. This is an algebraic example, not a derivation of that physical
relation or of `k`. Direct derivations of `H_0` are also not excluded.
The parameter count by itself does not classify all possible constraints.

## 3. Finite Boolean bookkeeping

The runner enumerates all eight assignments of three Boolean flags using
**the stipulated rule** `closure = C1 and (C2 or C3)`; here `C2` means a
complete L-supplying cascade premise, not retirement of just one input.
Exactly three assignments satisfy this rule. The truth table verifies the
rule's implementation, not its physical necessity or sufficiency. It is
not an exhaustive classification of physical routes.

No N1–N8 PASS certificate, QED for framework non-derivability, lattice
calculation, or continuum exhaustion is claimed. Literal source checks
verify documentary consistency only. The former stronger text and its
captures remain recoverable from version history; dated logs are history,
not current authority.

## 4. Open obligations

A genuine non-derivability claim would need a precise axiom-to-observable
map and an independence/underdetermination proof (for example inequivalent
models satisfying those axioms with different outputs). This inventory
provides no such proof. A physical positive closure would instead need a
checked derivation of its particular relation and all supplied bridges.
Both remain open. No listed route is declared impossible by this packet.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [scale_reference_primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
- [cosmology_open_number_reduction_theorem_note_2026-04-26](COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md)
- [omega_lambda_derivation_note](OMEGA_LAMBDA_DERIVATION_NOTE.md)
- [cosmology_scale_identification_and_reduction_note](COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md)
- [omega_lambda_matter_bridge_theorem_note_2026-04-22](OMEGA_LAMBDA_MATTER_BRIDGE_THEOREM_NOTE_2026-04-22.md)
- [planck_scale_lane_status_note_2026-04-23](PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md)
- [hubble_lane5_planck_c1_gate_audit_note_2026-04-26](HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md)
- [hubble_lane5_eta_retirement_gate_audit_note_2026-04-26](HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md)
