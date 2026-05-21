# Finite-Volume Gibbs State Relative to rho_ref: Conditional RP Compatibility Template

**Date:** 2026-05-20
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Purpose:** Salvage the correct finite-volume Radon-Nikodym statement
needed by the reflection-positivity / `rho_ref` compatibility follow-up
without claiming that the Wilson configuration measure has already been
identified with the operator-algebra tracial state.

## Honest Scope

This note does **not** close the RP to `rho_ref` bridge. It records the
standard finite-dimensional Gibbs/tracial Radon-Nikodym template on the
qubit-lattice operator algebra:

```text
omega_H(O) = tau_Lambda(D_H O),    D_H = e^{-H} / tau_Lambda(e^{-H})
```

for a finite-region self-adjoint Hamiltonian/action operator `H` on
`A_Lambda`. The missing bridge is the representation step that turns a
Wilson Euclidean configuration-space measure into such an operator
`H_Wilson,Lambda` on the same carrier as `rho_ref`. That step is not
proved here.

## Claim

Let `Lambda subset Z^3` be finite. By
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md),
the finite-region qubit-lattice algebra is

```text
A_Lambda = tensor_{x in Lambda} M_2(C) ~= M_{2^|Lambda|}(C).
```

Let `tau_Lambda(O) = Tr(O) / 2^|Lambda|` be the normalized trace,
the finite-region restriction of the pre-record reference state from
[`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md).
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

Equivalently, if a Wilson/RP finite-volume sector is independently
represented on the qubit-lattice algebra by a self-adjoint operator
`H_Wilson,Lambda`, then its Gibbs state is absolutely continuous with
respect to `rho_ref|_Lambda` with positive density proportional to
`e^{-H_Wilson,Lambda}`.

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

## Conditional RP Compatibility Reading

The retained reflection-positivity row
`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29` concerns a
Wilson Euclidean configuration/path-integral measure on its narrowed
retained scope. That measure is not automatically a state on the same
operator-algebra carrier as `rho_ref`.

This note therefore supports only the following conditional statement:

```text
If a retained finite-volume Wilson/RP sector is represented by
H_Wilson,Lambda in A_Lambda, then its Gibbs state has
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

## Admitted Inputs

1. **Finite-dimensional Gibbs-state construction** relative to a
   faithful normalized trace.
2. **Standard matrix functional calculus** for `e^{-H}` with
   self-adjoint `H`.
3. **Future/conditional Wilson representation bridge** if this lemma
   is later used for the Wilson/RP compatibility row.

## Risk Classification

This is a `bounded_theorem` candidate. The finite-dimensional
Gibbs/tracial density statement is standard operator-algebraic
background applied to the qubit-lattice finite-region algebra. Any use
as an RP compatibility result remains conditional on a separately
audited carrier-identification bridge.

## Citation-Graph Note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) —
  supplies A1+A2, hence the finite-region qubit algebra.
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) —
  supplies `rho_ref` / `tau_Lambda` as the trace reference.

**Plain-text pointer references** (NOT load-bearing deps):

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
