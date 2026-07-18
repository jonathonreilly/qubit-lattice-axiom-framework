# Gauge-Scalar Temporal Observable Bridge Open Interface

**Date:** 2026-05-03
**Claim type:** open_gate
**Status:** source correction 2026-07-18: the earlier formal no-go proposal
used finite-jet witnesses as if they were full Wilson-packet completions. That
use is withdrawn; the observable-level bridge residual named in
`GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_STRETCH_NOTE_2026-05-02.md` remains
open in this source note.
**Historical runner:** `scripts/frontier_gauge_scalar_temporal_observable_bridge_no_go.py`

## 0. Positive interface and remaining source requirement

The residual is the observable-level bridge

```text
<P>_full = R_O(beta_eff)                                      (BRIDGE)
```

between the full interacting Wilson plaquette expectation and the local
one-plaquette source response evaluated at the completed effective coupling.

This note keeps the stretch note's `A_min` and forbidden-import list fixed.
No fitted `beta_eff`, perturbative beta-function derivation, lattice Monte
Carlo plaquette, or PDG comparator is used as a derivation input.

## 1. Allowed current Wilson packet

The allowed packet is `A_min` plus the current Wilson
plaquette primitives:

- Wilson gauge action at `beta = 6`, `g_bare = 1`.
- [`GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md`](GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md):
  the retained bounded theorem that the accepted Wilson local scalar
  source class has
  `K_O(omega) = 3w(3 + sin^2 omega)` and
  `A_inf / A_2 = 2/sqrt(3)`.
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md):
  the retained bounded onset datum
  `beta_eff(beta) = beta + beta^5 / 26244 + O(beta^6)`.
- [`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md):
  the retained bounded finite Wilson source-sector operator realization.
- [`GAUGE_VACUUM_PLAQUETTE_FRAMEWORK_POINT_UNDERDETERMINATION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_FRAMEWORK_POINT_UNDERDETERMINATION_NOTE.md):
  the positive finite-jet construction of two entire rational polynomials
  with the same coefficients through degree five, exact interval derivative
  lower bounds, and a positive separation at `beta = 6`.
- [`GAUGE_VACUUM_PLAQUETTE_PERRON_JACOBI_UNDERDETERMINATION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_PERRON_JACOBI_UNDERDETERMINATION_NOTE.md):
  the retained no-go theorem that the current source-operator stack does
  not force the beta-6 Perron moments or Jacobi coefficients after the
  local Wilson marked-link factor is fixed.

The finite-jet construction is cited only for its typed polynomial output. It
does not supply a connected-hierarchy realization, compact spectral measure,
finite Wilson reduction law, or completion of the current Wilson packet.

## 2. Lemma 1: BRIDGE pins the missing nonperturbative number

Let `R_O(x)` be the local one-plaquette source response. On the Wilson
one-plaquette block it is strictly increasing in the source coupling:

```text
d R_O / dx = Var_x(P) > 0
```

away from a degenerate zero-variance measure. Therefore `R_O` is injective
on the finite coupling interval used by the displayed polynomial witnesses.

Consequently an exact bridge

```text
<P>_full = R_O(beta_eff)
```

does not merely relate two already-known numbers. It selects the missing
nonperturbative reduction parameter:

```text
beta_eff = R_O^{-1}(<P>_full).
```

If `beta_eff` is defined by this inverse equation, BRIDGE is a definition or
a fit rather than an independent derivation. A positive derivation of BRIDGE
therefore needs an independently sourced theorem selecting the exact beta-6
nonperturbative completion.

## 3. Finite-jet witness pair and its authority boundary

Let

```text
a = 1 / 26244,
c = 10^(-7).
```

Define two analytic, strictly increasing polynomial witnesses on `[0, 6]`:

```text
beta_eff^-(beta) = beta + a beta^5,
beta_eff^+(beta) = beta + a beta^5 + c beta^6.
```

They share the retained onset jet through order `beta^5`:

```text
beta_eff^+(beta) - beta_eff^-(beta) = c beta^6 = O(beta^6).
```

At the framework point:

```text
beta_eff^+(6) - beta_eff^-(6) = c 6^6 = 0.0046656 > 0.
```

Since `R_O` is injective on the displayed positive arguments,

```text
R_O(beta_eff^+(6)) != R_O(beta_eff^-(6)).
```

The two local-block values are strictly ordered. The polynomials have not been
shown to satisfy the connected hierarchy, compact spectral-measure conditions,
or finite Wilson reduction law. They are therefore not two admissible
completions of the current Wilson packet.

## 4. Current positive reduction

The injectivity calculation in section 2 gives a useful positive interface:
any exact bridge theorem that supplies `<P>_full` fixes one corresponding
`beta_eff`, and any independently realized `beta_eff` fixes one local-block
value. The finite-jet pair in section 3 exercises that interface on its stated
mathematical domain. A source theorem connecting either direction to the full
Wilson packet remains the open task.

## 5. Inputs for a future bridge theorem

A future positive bridge theorem may supply one of the following as a
load-bearing derived object:

- the exact beta-6 Wilson plaquette spectral measure;
- the exact beta-6 Perron vector / Jacobi data for the retained source
  operator;
- the exact nonperturbative effective action whose derivative gives
  `<P>_full`;
- an exact independently selected `beta_eff(6)` not fitted to `<P>`.

The source authority for any such object must be stated directly. A fitted
`beta_eff`, perturbative beta-function value, or comparator is not substituted
for that derivation in this note.

## 6. Audit consequence

This source note now declares the bridge residual open. Review-loop does not
apply a verdict, and the independent audit lane owns any later claim-type or
status decision.

```yaml
gate: gauge_scalar_temporal_observable_bridge_stretch_note_2026-05-02
source_disposition: open_gate
positive_bridge_status: not_derived
finite_jet_witness_role: polynomial_surface_only
forbidden_imports_used: false
audit_status_authority: independent audit lane only
```

The downstream parent `gauge_scalar_temporal_completion_theorem_note`
remains scoped to its bounded kernel-level statement: the temporal kernel
completion law is retained, while the full observable plaquette bridge is
not promoted.

## 7. Runner

The historical runner replays the former proposal. It is not current evidence
for a full-Wilson-packet conclusion and is outside the repaired finite-jet
runner package.

Run:

```bash
python3 scripts/frontier_gauge_scalar_temporal_observable_bridge_no_go.py
```

Expected summary:

```text
SUMMARY: THEOREM PASS=9 SUPPORT=4 FAIL=0
```
