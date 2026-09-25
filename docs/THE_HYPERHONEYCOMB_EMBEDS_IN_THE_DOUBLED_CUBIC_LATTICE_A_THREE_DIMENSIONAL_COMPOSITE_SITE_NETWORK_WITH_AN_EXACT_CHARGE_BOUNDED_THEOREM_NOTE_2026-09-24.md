---
claim_id: the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: A supplied colored periodic network and finite Majorana-band diagnostics. Supplied constructions and
  explicitly finite diagnostics; no unrestricted minimality, phase, physical particle identification or new premise.
upstream_dependencies:
- composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
- gauging_the_composite_site_charge_the_link_field_dresses_the_yao_lee_bond_and_the_z2_partner_survives_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/three_dimensional_composite_site_network_with_an_exact_charge_2026_09_24.py
---

# A supplied colored periodic network and finite Majorana-band diagnostics

**Type:** bounded_theorem

## Setting and construction

Supply composite vertices 2p with matter sigma and cube partner
2p+(1,1,1) carrying tau, frozen site and bond-color patterns, tensor-product
kinematics, and the real-coupling Hamiltonians below. The frozen pattern
and omission of bonds on recorded sites are extra model choices.
For p=(i,j,z), keep j even at z=0 mod4, i odd at z=1, j odd at z=2,
and i even at z=3. Join kept axial nearest neighbors in p coordinates.
The runner's `flavour` rule alternates x,y along chains, shifted in layers
2,3, with z on interlayer bonds. These explicit definitions, rather than a
name or graph identification, specify the network.

The parity cases show each kept site has two chain neighbors and one
interlayer neighbor, with distinct x,y,z colors. Sum-coordinate parity
gives a bipartition. The rectangular cell 2x2x4 has eight vertices;
translation (1,1,2) preserves the pattern and halves this cell to four.
Finite periodic residue checks verify the stated translation and inversion.
The runner separately checks connectivity on the 4x4x8 torus. Torus
connectivity alone does not prove connectedness of the infinite cover.
The bounded-depth search at the origin gives girth 10 through that origin,
ten length-ten cycles and coordination sequence (3,6,12,24,38).
It does not establish a global classification by these few invariants.

Per doubled 4x4x8 rectangular cell there are 16 composite positions,
eight kept, twelve kept-kept bonds, 24 kept-removed links and twelve
removed-removed links. The sampled pattern test finds stabilizers of order
8 for the vertex set and 2 for its *unoriented* bond colors under the
specified rotations and translations. It omits directed record signs and
the partner displacement (1,1,1): the orbit counts 3 and 12 are not
asserted for the full physical record/partner pattern. Flavor following an
axis defines an equivariant rule but does not produce a chosen pattern.

## Conditional spin algebra

Take bonds J_lambda tau_i^lambda tau_j^lambda (sigma_i dot sigma_j)
and odd paths kappa tau_i^lambda tau_0^nu tau_j^mu (sigma_i dot sigma_j)
for cyclic (lambda,mu,nu). Each commutes with total S=sum sigma/2 by
contraction of the two sigma commutators. Use the fixed-parity
six-Majorana representation described in the composite-site note.
Distinct colors at every vertex are essential for static link variables;
the resulting quadratic parton Hamiltonian requires a supplied gauge sector
and physical projection. The convention S^z=-i c^x c^y/2 makes
(c^x+i c^y)/2 transform with charge +1 but this operator is gauge odd.

For J=(1,.8,.6), kappa=.35, the four-site star's 256 spin levels match
the displayed free comparator. Both hopping signs match: spectra even in
kappa cannot verify that sign or an operator map. ODD_SIGN is explicitly a
choice in the separate band comparator. Pauli-string enumeration checks the
ten origin loops against all 1176 nearby bond/path terms, with a changed
Pauli as a failing control. The code retains the exact support windows;
the bond has a 4x2x2 bounding box up to axis permutation. These checks do
not show that the supplied frozen pattern forms autonomously.

## Band observations, not a phase or exhaustive node theorem

The runner retains its explicit eight-band supercell matrices, grids,
local minimization, symmetry samples and Berry cubes in the chosen u=+1
sector. At isotropic J and kappa=0 it finds near-zero energies; counts
inside a grid-dependent threshold are descriptive, not a proof of nodal
dimension. At kappa=.3 it locates two candidate crossings and computes
opposite Berry fluxes on small cubes with occupied-gap and overlap guards.
This does not exclude additional nodes elsewhere, determine the physical
spin ground-flux sector or prove a charged physical Weyl phase. No cited
flux-selection theorem is imported without its hypotheses.

At kappa=0 and J_z=2.5, a stronger elementary bound is available for this
comparator: the z-colored perfect matching has eigenvalues +/-5 at each
momentum. The x,y matchings each have norm 2. Thus the remaining sum has
norm at most 4, and eigenvalue perturbation bounds give |E|>=1 throughout
the zone. A sampled minimum near 1 is consistent with this bound. No such
bound is asserted at other parameters.

The six-valent comparison supplies six gauge Majoranas and either three
or two matter Majoranas. The connected set of cross bilinears generates
all even Clifford bilinears by commutators, and their associative algebra
is the even Clifford algebra. For nine Majoranas its irreducible complex
algebra is M_16; for eight or six, a fixed chirality block is M_8 or M_4.
The dimensions 256,64,16 and qubit counts 4,3,2 refer to those faithful
irreducible representations, not every possible SU(2) or U(1) model.
The numerical generated-algebra check realizes these representations.

The cubic band section compares two supplied flux patterns with finite
quadrature, threshold counts and a local Berry cube. Its lower sampled
energy among two sectors does not select the unrestricted ground sector;
threshold counts do not prove surfaces, node exhaustion or absence of Weyl
points for a general six-valent construction.

## Validation and residual work

Eight checks preserve the finite geometry, spin, loop, algebra and band
calculations. Extended graph identification, complete physical record
symmetry, global node/flux searches, projection, gauging and physical
realization remain separate work. Original source and its wider conjectures
remain on the preserved PR branch; this note grants no audit status.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

## Construction dependencies

- [9144: scoped construction](COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [9149: scoped construction](GAUGING_THE_COMPOSITE_SITE_CHARGE_THE_LINK_FIELD_DRESSES_THE_YAO_LEE_BOND_AND_THE_Z2_PARTNER_SURVIVES_BOUNDED_THEOREM_NOTE_2026-09-24.md).

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the explicit supplied supports, representations, trajectories and finite experiments above.
- **N2 — Independence:** fresh primary execution is distinct from the independent controls recorded with this review.
- **N3 — Imports:** Hilbert kinematics, models, patterns, clocks and sectors remain supplied rather than framework admissions.
- **N4 — Dependencies:** linked current scoped parents govern; historical titles do not strengthen these claims.
- **N5 — Resolution:** numerical spectra, quadrature, sampled fits and Berry sums are not certified global enclosures.
- **N6 — Residuals:** physical realization, complete classification and larger-system inference require separate evidence.
- **N7 — Counterroutes:** alternative representations, sectors, nonlinear laws and different orders of limits remain available where stated.
- **N8 — Boundary:** this is source review, not an audit verdict or a retained-grade promotion.

## Recovery and falsifiers

An example satisfying a theorem's exact hypotheses but violating its conclusion
refutes that theorem. A failed finite check requires investigation; it is not
silently converted into a different physical interpretation. The original
branch preserves wider proposed claims and all original calculations for
explicit recovery. This source's scope controls its historical identifier.

Original PR #9168, frozen head `8a47c2dff898dd8eb26f567fffe66c3f70455add`.
