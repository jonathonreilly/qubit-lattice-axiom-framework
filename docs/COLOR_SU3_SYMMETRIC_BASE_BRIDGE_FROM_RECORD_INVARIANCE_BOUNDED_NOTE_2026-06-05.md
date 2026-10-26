# Supplied symmetric-base SU(3) action and record-invariance limits

**Type:** bounded_theorem
**Primary runner:** `scripts/frontier_color_su3_bridge_from_record_2026_06_05.py`

## Carrier and additional action

Choose C⁸=(C²⊗C²)_base⊗C²_fiber, with the base split into its symmetric
three-space and antisymmetric line. Sym²(C²) has dimension three. The
inherited diagonal SU(2) action is its spin-one representation; it is not
the fundamental representation of SU(3). One can separately choose the
fundamental SU(3) action on this three-dimensional vector space, extended
trivially over the antisymmetric line and fiber. That choice is the matrix
construction here, not a consequence of taking a symmetric square.
Physical color and weak-isospin labels remain proposed interpretations.

On this supplied carrier, the base SU(3) commutant in End(C⁸) has complex
dimension 8: (C⊕C)⊗M₂(C). The separately supplied fiber SU(2) commutant
has dimension 16: M₄(C)⊗I₂. These follow from the distinct irreducible
base summands and the irreducible fiber action, and are checked by numerical
SVD. They distinguish these representations' invariant operator algebras.
They do not reconstruct a unique gauge group from selected observables.

## Singlets and the failed converse

In the separately chosen defining three, the meson tensor Σ_i e_i⊗ebar_i
and baryon alternating tensor ε are fixed by SU(3). Their invariant
subspaces in 3⊗3bar and 3⊗3⊗3 are one-dimensional. Their rank-one projectors
therefore commute with the diagonal group actions. These projectors live
in End(C⁹) and End(C²⁷), not literally in End(C⁸).

The former inference from projector invariance to a unique SU(3) gauge
group was unjustified. A scalar U(3) phase zI fixes the meson tensor and
sends ε to z³ε; it leaves both projectors invariant even for z³≠1.
Thus these projector tests cannot exclude U(3), and do not compare fiber
SU(2) on a fully specified common tensor carrier. If one instead requires
unitary maps on C³ to fix ε itself, det U=1 selects SU(3) within U(3).
That is an additional tensor-preservation hypothesis, not the old
projector test or a deduction from a Record axiom.

## Link diagnostic and remaining obligations

The runner additionally constructs two supplied finite models: four qubits
with endpoint SU(2) generators, and a matched C³⊗C³bar endpoint with SU(3)
generators. A bare operator fails an endpoint-invariance test while the
specified singlet projector passes. These examples show the tested profile
exists for these choices. They do not exhaust theories allowed by locality
or prove that no additional axiom can select a gauge group.

Assigning physical quarks, color links, records and dynamics remains open.
No gauge-group reconstruction theorem, physical SU(3) derivation, or general
no-go is claimed. The primary mixes exact symbolic checks with numerical
matrix residual/SVD checks; the latter are not exact arithmetic proofs.
No repository scientific premise is required for these supplied finite
matrices; #2667, #2711 and other color/two-endpoint notes are historical
motivation. Baseline recovery is f24d17d97d372df977476e4a69674577f31af575
at this note and runner's paths.

## Documentary antecedent boundary

Even given the antecedent that the physical records are the color singlets,
the projector test does not reconstruct a unique gauge group. This calculation
does not force the antecedent; matter realization remains a separate input.
The selector that fixes the antecedent — which subsystem the quarks occupy and which symmetry index the link connection carries — is a separate input.
