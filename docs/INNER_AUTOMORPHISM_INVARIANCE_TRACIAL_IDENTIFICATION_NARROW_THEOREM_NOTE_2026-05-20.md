# Inner-Automorphism Fixed Finite-Region States Are Tracial

**Date:** 2026-05-20; scope repair 2026-05-27
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/frontier_inner_automorphism_invariance_tracial_identification.py`](../scripts/frontier_inner_automorphism_invariance_tracial_identification.py)

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The finite-dimensional algebraic conclusion follows once PRR is granted, but PRR is an admitted external premise and neither cited authority derives or approves it. Removing PRR removes the conclusion."*

with repair: *"missing_bridge_theorem: supply a retained-grade derivation of PRR from accepted inputs or explicit framework approval of PRR, then re-audit any promotion beyond this conditional finite-region bridge."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The finite-dimensional algebraic theorem that the unique density matrix on `M_d(C)` fixed by conjugation with every unitary `U ∈ U(d)` is `I_d/d`, verified by runner on `d = 2, 4, 8, 16`; combined with the one-qubit operator algebra on finite `Z^3` regions, this delivers the conditional implication `PRR ==> ρ_ref|_Λ = I_{2^|Λ|}/2^{|Λ|}`.
- **NON-load-bearing (split off / admitted):** The premise PRR itself — that the pre-record reference state satisfies full inner-unitary invariance on every finite qubit region — is an admitted external premise that is neither derived from the one-qubit operator algebra on the `Z^3` spatial substrate nor approved as a framework rule in any retained authority; removing PRR removes the conclusion entirely, and closing this gap requires a retained-grade derivation or explicit framework approval that is not supplied here.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Honest Scope

The earlier row was audited conditional because it treated PRR, the assertion
that the pre-record reference state is invariant under every finite-region
inner unitary, as an admitted premise. PRR is not derived from accepted inputs
and is not approved as a framework rule.

This repair removes PRR from the binding claim. The row now states only the
finite-dimensional algebra theorem:

```text
If a density matrix on M_d(C) is fixed by every inner unitary automorphism,
then it is I_d/d.
```

That theorem is useful downstream, but it does not identify any specific
framework reference state.

## Setup

By [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md), each finite
qubit region `Lambda subset Z^3` has:

```text
H_Lambda = tensor_{x in Lambda} C^2
A_Lambda = tensor_{x in Lambda} M_2(C) ~= M_{2^|Lambda|}(C)
d = 2^|Lambda|
```

A finite-region state is represented by a density matrix
`rho in M_d(C)`, `rho >= 0`, `Tr(rho)=1`.

## Theorem

Let `rho in M_d(C)` be a density matrix. If

```text
U rho U^dagger = rho
```

for every unitary `U in U(d)`, then

```text
rho = I_d / d.
```

Equivalently, the corresponding state is the normalized trace
`tau_d(X) = Tr(X)/d`.

For qubit finite regions this gives:

```text
inner-unitary fixed state on A_Lambda
  ==> rho_Lambda = I_{2^|Lambda|}/2^|Lambda|.
```

## Proof

The fixed-point condition implies `U rho = rho U` for every unitary `U`.

There are two elementary finite-dimensional proofs:

1. Schur/commutant proof: the commutant of the defining irreducible
   representation of `U(d)` on `C^d` is `C I_d`, so `rho = c I_d`.
2. Entrywise proof: diagonal sign or phase unitaries kill every off-diagonal
   entry of `rho`, and permutation unitaries force all diagonal entries to be
   equal.

The trace condition fixes `c = 1/d`. Positivity is automatic for `I_d/d`.

The finite-region family is restriction-compatible:

```text
Tr_B( I_{d_A d_B}/(d_A d_B) ) = I_{d_A}/d_A.
```

The quasi-local UHF extension is supplied by
[`POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md).

## What This Claims

- A finite-dimensional matrix-algebra theorem on each finite qubit region.
- Compatibility of the maximally mixed finite-region family under partial
  trace.
- A bridge to the existing Powers/UHF uniqueness note for the quasi-local
  tracial state.

## What This Does Not Claim

- It does not derive or approve PRR.
- It does not assert that the pre-record reference state is inner-unitary
  invariant.
- It does not identify the pre-record reference state with the tracial state.
- It does not promote `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20`
  or any Born/measurement row.
- It does not add a new framework axiom, rule, admission, or status verdict.

Plain-text downstream target, not a load-bearing dependency:

- `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20`

## Runner Coverage

The runner checks:

- diagonal sign invariance kills off-diagonal entries;
- permutation invariance forces all diagonal entries equal;
- trace normalization gives `I_d/d` for `d = 2, 4, 8, 16`;
- finite-region maximally mixed states are compatible under partial trace; and
- source-boundary strings prevent this theorem from being presented as a PRR
  approval or pre-record-state identification.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_inner_automorphism_invariance_tracial_identification.py
```

Expected:

```text
TOTAL: PASS=23, FAIL=0
```
