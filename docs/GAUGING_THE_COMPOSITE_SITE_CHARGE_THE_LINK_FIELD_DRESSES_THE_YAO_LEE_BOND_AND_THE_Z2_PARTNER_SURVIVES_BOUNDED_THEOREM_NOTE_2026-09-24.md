---
claim_id: gauging_the_composite_site_charge_the_link_field_dresses_the_yao_lee_bond_and_the_z2_partner_survives_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: A gauge-invariant composite bond and a finite plaquette sector. Supplied constructions and explicitly
  finite diagnostics; no unrestricted minimality, phase, physical particle identification or new premise.
upstream_dependencies:
- composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/gauging_the_composite_site_charge_with_the_link_field_2026_09_24.py
---

# A gauge-invariant composite bond and a finite plaquette sector

**Type:** bounded_theorem

## Supplied model

Supply matter sigma at doubled-lattice vertices, partner tau at the cube
2p+(1,1,1), spin-half link fields E=s^z/2, fixed bond colors and background
rho. This body-diagonal pairing differs from the nearest-neighbor dimers
of the composite-site note. Tensor composition and all generators are
supplied. Record constraints alone do not implement the dynamics.
For an oriented edge i->j take n_i=(1+sigma_i^z)/2,
G_i=sum_out E-n_i+rho_i, and
B_ij=J tau_i^lambda tau_j^lambda [sigma_i^z sigma_j^z+
2(sigma_i^+ s_ij^+ sigma_j^-+sigma_i^- s_ij^- sigma_j^+)].

## Exact algebra

Since [E,s^+]=s^+ and [n,sigma^+]=sigma^+, the hop raises outgoing
flux and n_i equally, and lowers outgoing flux and n_j equally at j.
Therefore [G_v,B_ij]=0 at every vertex. The two-link dressed hop has
cancelling increments at its intermediate vertex. A closed oriented ring
has zero divergence, so its raising/lowering product also commutes with G.
The bare hop without link dressing fails these commutators. Total n is
conserved; total S^x generally is not. This proves the stated U(1) symmetry
of this spin model, not fermionic statistics.

On the four-vertex cycle colored x,y,x,y, W=product_i tau_i^z commutes
with every bond: its two anticommutations cancel. It also commutes with
the ring and the supplied path term. The ordered product of the four
partner bond factors is -W. These are plaquette statements, not conserved
individual link variables on an arbitrary six-valent network. Repeated
bond colors at a vertex invalidate the usual static-link argument.

On a closed graph summing G_v=0 gives sum n_v=sum rho_v. A zero background
therefore permits the n=0 sector; it excludes positive total charge for
this one-sign occupation, not all gauge-invariant states. Staggering is a
choice, not uniquely necessary. For the runner's plaquette rho=(0,1,0,1),
there are seven allowed (matter,link) basis patterns and 16 independent
partner patterns, giving dimension 112. They comprise six matter patterns,
with link multiplicities (1,1,1,1,1,2); total n=2. The support condition
n=div E+rho fixes diagonal matter labels from link labels. It does not select
a measurement law. The runner checks invariance and finite spectra at
ring couplings 0 and 1/2, including W sectors.

The odd path term is kappa tau_1^x tau_2^z tau_3^y times the endpoint
sigma^z product plus the two-link dressed hop and its adjoint. In the
specified Z basis all raising matrices are real and the one tau^y is
imaginary. Basis conjugation K fixes bonds/ring and negates this term.
This is a specified antiunitary, not a derived physical time reversal.
The separate transformation (product_all_qubits Y)K flips link E as well
as n->1-n. At fixed background it takes G_v to -G_v+(2rho_v-1);
it need not preserve the chosen sector. It negates each three-ladder
one-link hop and breaks the dressed Hamiltonian's symmetry, as checked.

## Geometry and boundary

The support (two vertices, intervening link, two cube partners) has a
4-by-2-by-2 bounding box in integer coordinates and fits no radius-one
closed star. All candidate centers lie in the finite coordinate window
checked by the runner. The cube partner lattice has six axial neighbors
at distance two. These facts specify a possible bounded support, not a
formation mechanism for its role pattern.

Five runner checks retain the finite matrices, sector enumeration and odd
spectrum. Reported commutator sizes use maximum absolute entries, not an
induced operator norm. An infinite-network gauge reduction, charged
fermion statistics, a fluctuating-link band invariant and a physical phase
remain open; neither this plaquette nor K-oddness proves them.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

## Construction dependencies

- [9144: scoped construction](COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md).

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

Original PR #9149, frozen head `705a0c331e707300a33d2bb6ee599ad9145f84d8`.
