# Quantum Local Algebra Does Not Force Boost-Action Faith No-Go

**Date:** 2026-06-02
**Claim type:** no_go
**Runner:** `scripts/quantum_local_algebra_boost_action_faith_no_go_2026_06_02.py`

This note separates two facts that can be conflated on the on-site `C^2`
carrier.

Quantum supplies a faithful local operator algebra: the Pauli generators realize
the complex `Cl(3,0) ~= M_2(C)` algebra irreducibly on `C^2`. A scalar-only
rotation module does not realize that local Clifford algebra. That is a
local-algebra fact.

It does not follow that the reconstructed physical boost or mass action must act
faithfully on that same `C^2`. A scalar boost action `S(eta)=exp(eta c) I_2` is
a valid action on the same vector space unless an extra matter-attachment or
kinetic-kernel selector identifies the physical boost with the operator-frame
Pauli triple.

The framework baseline is
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md): Lattice supplies
the lattice carrier, Quantum supplies the one-qubit local algebra, and Record is
irrelevant to this boost-action question. This note does not add a matter
attachment primitive or a Lorentz-action admission.

## Result

The runner verifies three finite algebraic blocks.

First, the Pauli generators satisfy the local Clifford relations, span the full
real Clifford image, and have scalar commutant on `C^2`. This is the faithful
Quantum local algebra.

Second, if the physical boost is assumed to use the same operator-frame Pauli
triple, scalar boost completions fail the Lorentz brackets. The faithful Weyl
choices `K = +/- i sigma/2` are then the surviving two-dimensional completions.
This is a conditional fact: it depends on the antecedent that the physical boost
acts through that operator-frame triple.

Third, the antecedent is not supplied by Quantum alone. The runner exhibits a
scalar boost representation on the same `C^2` vector space and a spin-blind
native-dynamics stand-in that commutes with the operator-frame boost. The
spin-1/2 kinetic kernel does exclude the scalar action, but that is a
matter-attachment / reconstructed-field selector, not a consequence of the local
operator algebra by itself.

## Scope

This is not a no-go against boost-action faithfulness. It is a no-go against the
specific route that tries to derive boost-action faithfulness from Quantum alone.
Once a matter field is independently identified as transforming by the Pauli
spinor action, the runner confirms that scalar boost completions are excluded.

The live residual is the attachment step:

```text
operator-frame Pauli/Clifford action on C^2
        -> physical matter-field boost action on C^2
```

That step needs an owner-approved admission or an independent derivation.

## No-Go Discipline Gate

This gate applies only to the route above: deriving boost-action faithfulness
from the local Quantum algebra without a matter-attachment selector.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Dimension route | Use `dim C^2 = 2` to exclude every scalar action. | Dimension fixes the carrier size; a two-copy scalar boost can still act on the same vector space. |
| Clifford-action route | Use the faithful Pauli/Clifford action to force the physical boost action. | It proves the local operator algebra is faithful; it does not identify that algebra with the physical matter boost. |
| Operator-frame bracket route | Assume `J=sigma/2` and force `K=+/- i sigma/2`. | This works only after the operator-frame antecedent is granted. |
| Native-dynamics route | Let the native single-component dynamics select the boost generator. | The runner's stand-in commutes with the spin operator; it is spin-blind for this question. |
| Kinetic-kernel route | Use the spin-1/2 kernel to exclude scalar covariance. | This does exclude the scalar, but it is the reconstructed-field selector, not Quantum alone. |
| Scalar-boost countermodel | Exhibit `S(eta)=exp(eta c) I_2` on the same vector space. | It remains available until the matter-attachment selector is supplied. |

### N2 - Wall Independence

The collapsed wall is one antecedent: the physical boost must be identified with
the operator-frame Pauli triple. The dimension, Clifford, bracket, dynamics, and
kernel probes all reduce to whether that antecedent has been supplied.

### N3 - Hidden-Wall Scan

"Quantum" means the local `M_2(C) ~= Cl(3,0)` operator algebra. "Boost action"
means a physical Lorentz/mass action on matter fields. The note does not smuggle
in a matter-field transformation law, Poincare covariance, or a kinetic kernel as
part of Quantum.

### N4 - Residual Matching

The residual is the attachment from an operator-frame Clifford action to a
physical matter-field boost action. It is not the faithfulness of the local
Clifford representation, and it is not the conditional bracket fact once the
operator-frame boost has been granted.

### N5 - Rhetoric Audit

"Does not force" is scoped to Quantum alone. The note does not say the faithful
boost is impossible, false, or unavailable. It says the route needs the
attachment selector.

### N6 - Partial-Closure Path Scan

Two closure paths remain open: derive the matter-attachment selector from the
framework, or explicitly approve it as a primitive. After either path, the
operator-frame bracket and kinetic-kernel checks can be reused to exclude scalar
boost action.

### N7 - Steelman

A hostile reviewer can argue that a physical matter field on the qubit carrier is
already a spinor field, so the boost action should be the Pauli/Weyl action by
definition. That is a valid convention or attachment admission. It does not make
the result derivable from Quantum alone; it supplies the antecedent this note
isolates.

### N8 - Cross-Cycle Echo

Other carrier notes separate local qubit structure from cross-site statistics and
from matter-field attachment. This note adds the boost-action version of the same
split: faithful local algebra is not the same thing as a faithful physical boost
action.

**Gate result:** pass for the Quantum-alone boost-action route only.

## Validation

The runner checks finite-matrix facts:

- Pauli matrices satisfy the Clifford relations and give an injective local
  Clifford image;
- the Pauli representation on `C^2` has scalar commutant;
- a scalar-only action does not realize the Quantum local Clifford relations;
- if `J=sigma/2`, scalar boosts fail the Lorentz bracket;
- `K=+/- i sigma/2` give faithful Weyl completions;
- a scalar boost representation exists on the same vector space;
- the spin-1/2 kinetic kernel excludes scalar covariance only after that kernel
  is supplied.
