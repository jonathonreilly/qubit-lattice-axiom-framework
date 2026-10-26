# Koide gravity-phase probe: conditional scalar-source non-identifiability

**Date:** 2026-05-08; scope correction 2026-10-21
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** finite tensor-product and scalar-source examples; no exhaustive gravity-phase obstruction.
**Status:** source-note proposal. The former five-barrier route exclusion is withdrawn; the gravity-to-flavor identification remains open.
**Authority role:** source proposal; audit verdict and effective status belong to the independent audit lane.
**Primary runner:** [`scripts/cl3_koide_a1_probe_gravity_phase_2026_05_08_probe3.py`](../scripts/cl3_koide_a1_probe_gravity_phase_2026_05_08_probe3.py)

## Question and actual conclusion

Can gravitational dynamics select `|b|²/a²=1/2` for the Hermitian
circulant `H=aI+bU+conj(b)U⁻¹`, where U is the three-cycle? This note
does not answer that general question. It proves a limited
non-identifiability result under an assumed tensor split and flavor-summed
scalar source. It supplies neither a physical gravity-flavor bridge nor a
proof that such a bridge is impossible. Audit labels and ledger absence
are not mathematical obstructions.

## Conditional statement and proof

Assume a product state `Ψ(x,σ)=ψ(x)v(σ)` on `H_space ⊗ C³` and the
specific source `ρ(x)=Σσ |Ψ(x,σ)|²`. Direct multiplication gives
`ρ(x)=|ψ(x)|² ||v||²`. Equal-norm flavor vectors therefore give identical
sources. Any fixed deterministic map F whose only state-dependent input
is ρ gives the same output F(ρ) for both. This includes a linear map but
assumes neither a physical Green function nor its existence. It does not
establish equality of coupled wavefunction evolution with other inputs.

For an orthonormal C3 Fourier basis `(e0,eω,eωbar)`, take

- `vA=e0+(eω+eωbar)/sqrt(2)`;
- `vB=e0/2+sqrt(7/8)(eω+eωbar)`.

Both have norm squared 2, while their Fourier coefficient ratios are
1/2 and 7/2. A rule using only this source cannot distinguish those
ratios. The vectors are examples, not solutions of a gravitational
stationarity problem. Their coefficients are not silently identified
with those of a physical mass operator.

Similarly, `[A⊗I,I⊗H]=0` follows from tensor multiplication for any
finite A and H. This assumes the factorization and flavor-blind action;
it does not derive either from framework axioms. The runner uses an
arbitrary nonidentity 2×2 A and five supplied circulant ratios. A is
neither a Laplacian nor a Green function.

## Corrections to the former barriers

1. Different dimensions do not establish the absence of canonical maps;
   that depends on additional structure. Tensor-product interactions can
   couple factors. The calculation assumes, rather than proves, a
   flavor-blind spatial operator.
2. The original runner used hardcoded ledger counts and true flags,
   without reading a ledger. Its count of four full rows contradicted
   a list of seven. Those assertions are removed without replacement
   claims about current audit statuses.
3. Every homomorphism between `Z2³` and `C3` is trivial: its image order
   divides both 8 and 3. The trivial homomorphism does exist. This does
   not forbid a C3 action on cube corners: coordinate cyclic permutation
   has order three and cycles the weight-one corners. The runner constructs
   this action, which is not a homomorphism from `Z2³` to `C3`.
4. Born probabilities need not be flavor-blind. The norm-only result
   assumes summation with the identity observable. The positive projector
   `P0=|e0><e0|` has normalized expectations 1/2 and 1/8 in vA and vB.
   Both obey the Born rule; probability conservation does not exclude
   flavor-dependent interactions or measurements.
5. Newton's constant has SI dimensions `L³ M⁻¹ T⁻²` and is distinct from
   an inverse Laplacian. With a specified three-dimensional continuum
   integration measure, its Green kernel has dimension `L⁻¹`, while the
   inverse-Laplacian integral operator has dimension `L²`. Lattice versions
   require spacing and measure conventions. Dimensionless combinations
   are possible. Four supplied numbers and their pairwise ratios do not
   exhaust them or establish a flavor-amplitude obstruction.

Thus the former five-barrier exclusion of every gravity-phase route,
including a simultaneous Planck-scale bridge, is withdrawn. No conclusion
about other Koide route notes follows.

## Circulant algebra and physical readout

For real a, `Tr(H)=3a` and `Tr(H²)=3a²+6|b|²`. Coefficient Frobenius
balance is therefore `|b|²/a²=1/2` when a is nonzero. This is imposed
balance, not dynamical selection. For real b the eigenvalues are
`a+2b cos(2πk/3)`. If masses are their squares, the physical Koide
denominator uses the sum of their absolute values. The signed-root trace
identity gives physical Q=2/3 only on a common-sign branch. The supplied
a=1, b=1/sqrt(2) example is positive; phase π/3 gives a mixed-sign
counterexample to unrestricted equivalence. No physical mass assignment
is established here.

## Runtime and verification limits

The runner imports only NumPy and reads no files, ledger, or upstream
runner. Inputs are supplied matrices, Fourier vectors, ratios, a
2-component spatial state, four historical numbers `(-1,1.21,-0.58,ln 2)`,
and mass anchors `(0.5109989461,105.6583745,1776.86)` in common units.
The historical numbers are not refreshed measurements or certified gravity
outputs. They do not enter the conditional theorem. The mass comparison
is printed without a scientific PASS threshold and is not a derivation.

The necessary mathematical premises and proof are stated above. Earlier
repository citations motivated a physical proposal; their correctness,
effective status, and ability to supply a bridge are not certified here.
No `L⁻¹=G0` self-consistency, Newton constant, lattice field solution,
or continuum limit is tested. The runner prints these limitations.

Run `python3 scripts/cl3_koide_a1_probe_gravity_phase_2026_05_08_probe3.py`.
Failures return a nonzero exit code. Passing the finite checks does not
reinstate the withdrawn route exclusion. The physical selection question
remains open.
