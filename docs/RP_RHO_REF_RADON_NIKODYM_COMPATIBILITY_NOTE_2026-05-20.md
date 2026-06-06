# Finite-Volume Gibbs State Relative to the Normalized Trace

**Date:** 2026-05-20
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Runner:** [`scripts/rp_trace_gibbs_radon_nikodym_certificate_2026_06_06.py`](../scripts/rp_trace_gibbs_radon_nikodym_certificate_2026_06_06.py)
**Purpose:** Record the finite-volume Radon-Nikodym density theorem relative to
the normalized trace on the qubit-lattice finite-region algebra, while keeping
all `rho_ref` and Wilson/RP compatibility readings conditional and
non-load-bearing.

## 2026-06-06 audit-scope repair

The 2026-06-06 conditional audit found the finite-dimensional Gibbs-density
identity correct, but blocked the row because the `rho_ref`/Wilson wording made
two separate bridges look load-bearing:

- identifying `rho_ref|_Lambda` with the normalized trace `tau_Lambda`;
- representing a Wilson/RP configuration-space measure by a self-adjoint
  operator `H_Wilson,Lambda in A_Lambda`.

This repair narrows the load-bearing claim to the trace-relative theorem only.
The conditional `rho_ref` and Wilson/RP readings remain as downstream
applications requiring independent bridge theorems.

## Honest Scope

This note does **not** close the RP to `rho_ref` bridge. It records the
finite-dimensional Gibbs/tracial Radon-Nikodym theorem on the qubit-lattice
operator algebra:

```text
omega_H(O) = tau_Lambda(D_H O),    D_H = e^{-H} / tau_Lambda(e^{-H})
```

for a finite-region self-adjoint Hamiltonian/action operator `H` on
`A_Lambda`. No `rho_ref` or Wilson configuration-space measure is a
load-bearing premise of this theorem.

## Claim

Let `Lambda subset Z^3` be finite. By
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md),
the finite-region qubit-lattice algebra is

```text
A_Lambda = tensor_{x in Lambda} M_2(C) ~= M_{2^|Lambda|}(C).
```

Let `tau_Lambda(O) = Tr(O) / 2^|Lambda|` be the normalized trace.
For any self-adjoint finite-region operator `H in A_Lambda`, define

```text
Z_H = tau_Lambda(e^{-H}),        D_H = e^{-H} / Z_H.
```

Then `D_H` is positive, `tau_Lambda(D_H) = 1`, and

```text
omega_H(O) := tau_Lambda(D_H O)
```

is a positive normalized state on `A_Lambda`. In finite dimension,
`omega_H` is normal with respect to `tau_Lambda`, and its
Radon-Nikodym density is exactly `D_H`.

Conditional downstream application: if separate retained bridges identify
`rho_ref|_Lambda = tau_Lambda` and represent a Wilson/RP finite-volume sector
by a self-adjoint `H_Wilson,Lambda in A_Lambda`, then the same formula gives the
Wilson/RP Gibbs density relative to `rho_ref|_Lambda`. Those bridge hypotheses
are not proved or consumed here.

## Proof

Because `H = H^*`, functional calculus gives `e^{-H} > 0`. The trace
state is faithful on the matrix algebra, so `Z_H = tau_Lambda(e^{-H})`
is strictly positive. Hence `D_H = e^{-H} / Z_H` is positive and

```text
tau_Lambda(D_H) = tau_Lambda(e^{-H}) / Z_H = 1.
```

For `O >= 0`, positivity of the Gibbs state follows from the density
matrix form

```text
omega_H(O) = Tr(e^{-H} O) / Tr(e^{-H}).
```

Equivalently, writing `e^{-H} = R^2` with `R = e^{-H/2}`,

```text
Tr(e^{-H} O) = Tr(R O R) >= 0
```

for positive `O`. Normalization is immediate from `omega_H(1)=1`.
Finite dimensionality makes the Radon-Nikodym statement just the
standard density-matrix representation relative to the faithful trace.

## Conditional RP / rho_ref Compatibility Reading

The retained reflection-positivity row
`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29` concerns a
Wilson Euclidean configuration/path-integral measure on its narrowed
retained scope. That measure is not automatically a state on the same
operator-algebra carrier as `rho_ref`.

This note therefore supports only the following conditional downstream
application:

```text
If rho_ref|_Lambda = tau_Lambda and a retained finite-volume Wilson/RP sector
is represented by H_Wilson,Lambda in A_Lambda, then its Gibbs state has
d omega_Wilson / d rho_ref|_Lambda proportional to e^{-H_Wilson,Lambda}.
```

The representation map from the Wilson configuration measure to
`H_Wilson,Lambda` remains a separate bridge. Without that bridge, it is
not correct to say that `mu_Wilson` and `rho_ref` are mutually
absolutely continuous, because they live on different mathematical
carriers.

## What This Can Support After Audit

- The finite-volume Gibbs/tracial density step needed by an eventual
  RP to `rho_ref` compatibility theorem.
- A clean audit target separating the standard Radon-Nikodym template
  from the still-open Wilson-measure-to-operator-algebra bridge.

## What This Does Not Close

- The pending RP to `rho_ref` compatibility follow-up from the qubit
  reframe.
- Mutual absolute continuity between the Wilson Euclidean configuration
  measure and `rho_ref`.
- The representation of the Wilson action as a self-adjoint
  finite-region operator on `A_Lambda`.
- The broader RP scope, full thermodynamic-limit RP retention, or any
  numerical prediction.

## Load-Bearing Inputs

1. **Finite-dimensional Gibbs-state construction** relative to a
   faithful normalized trace.
2. **Standard matrix functional calculus** for `e^{-H}` with
   self-adjoint `H`.
No `rho_ref` identification or Wilson representation bridge is load-bearing for
the theorem stated in this row.

## Risk Classification

This is a `bounded_theorem` candidate for the trace-relative finite theorem.
Any use as an RP or `rho_ref` compatibility result remains conditional on
separately audited carrier-identification bridges.

## Citation-Graph Note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) —
  supplies A1+A2, hence the finite-region qubit algebra.

**Plain-text pointer references** (NOT load-bearing deps):

- `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` —
  downstream/contextual `rho_ref` trace-reference bridge; not consumed as a
  theorem premise here.
- `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29` —
  downstream RP carrier that would need a separate representation
  bridge before this finite-volume density template can be applied.
- `G_BARE_DERIVATION_NOTE.md` and
  `STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md` —
  related Wilson-action gates, not used here.

## What This File Is Not

- Not a closure of the RP to `rho_ref` bridge.
- Not a derivation of a Wilson action operator.
- Not a claim of mutual absolute continuity across different carriers.
- Not a thermodynamic-limit theorem.
- Not a numerical-prediction change.
