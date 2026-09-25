---
claim_id: composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Composite-site spin symmetry, a bare-Majorana obstruction and finite band diagnostics. Supplied constructions
  and explicitly finite diagnostics; no unrestricted minimality, phase, physical particle identification or new
  premise.
upstream_dependencies:
- minimal_axioms
runner: scripts/composite_sites_give_the_carved_majoranas_an_exact_charge_2026_09_24.py
---

# Composite-site spin symmetry, a bare-Majorana obstruction and finite band diagnostics

**Type:** bounded_theorem

## Supplied setting and retained claims

Supply tensor-product qubits, the Pauli algebra, a graph and its bond colors,
real couplings, and a frozen role pattern. At each composite vertex there are
two qubits, tau and sigma. No composite law, role pattern, Hamiltonian,
physical particle or state preparation is derived from the axioms.

### A particular bare generator is unphysical

In the four-Majorana representation of a spin, D_j is the product of its
four Majoranas and physical states obey D_j=1. For distinct sites,
Q=i c_j c_k anticommutes with D_j and D_k. Thus P Q P=0. Since Q^2=1,
(1-P)exp(i theta Q)P=i sin(theta) QP and its operator norm is |sin(theta)|.
This holds for the bare bilinear whether or not the sites are connected.
A supplied dressing u_jk=i b_j^z b_k^z makes i c_j u_jk c_k even at each
endpoint and it survives projection in the checked two-site representation.
This excludes that bare generator, not every one-qubit charge: for example
an XY spin chain conserves total sigma^z. Two qubits are sufficient for the
construction below; no universal minimum is asserted.

### Spin symmetry and finite spectra

The supplied bond is J_lambda tau_i^lambda tau_j^lambda (sigma_i dot sigma_j).
Every bond commutes with S^a=sum_i sigma_i^a/2: the commutators of the two
sigma factors cancel after summing the contracted index. The same argument
applies to kappa tau_1^x tau_0^z tau_2^y (sigma_1 dot sigma_2).
Under the specified antiunitary T=(tensor product of Y on all qubits)K,
each Pauli changes sign; the four-Pauli bond is even and five-Pauli odd
term is odd. This defines the transformation, without identifying a physical
time reversal selected by the framework.

For the four-dimer star and J=(1,0.8,0.6), the runner checks levels
(-3e,-e,e,3e), e=sqrt(2), with multiplicities (32,96,96,32), as well as
spin multiplets. Largest S^z values (1,2,2,1) are multiplet diagnostics,
not a proof of an excitation's charge. With kappa=0.35 the spin spectrum
matches the displayed three-flavor quadratic comparator with multiplicity.
Spectral agreement does not determine the sign of its hopping or establish
an operator equivalence on every graph.

For the usual supplied six-Majorana representation, restrict to a fixed
local parity sector (dimension four). Distinct bond colors at each vertex
are required for conserved link variables. In the convention
S^z=-i c^x c^y/2, f=(c^x+i c^y)/2 obeys [S^z,f]=f and {f,f^dag}=1,
by the Clifford anticommutators. A single c or f is gauge odd: this parton
charge transformation is not by itself a physical, undressed creation
operator or an exchange-statistics derivation.

### Support and the supplied layer

Parallel nearest-neighbor dimers with their centers separated along an
orthogonal axis give four plaquette corners. No radius-one closed lattice
star contains all four: intersecting the possible centers within L1 distance
one of every corner gives the empty set. The 24 proper signed-axis rotations
act freely on an ordered orthogonal oriented axis pair. This is covariance
of a family; a chosen role pattern need not be invariant.

The separate two-band comparator is H=[[d,if],[-if*, -d]], with
f=2(J_x exp(iA)+J_y exp(iB)+J_z),
d=4 kappa(sin A-sin B+sin(B-A)), A=2 pi a, B=2 pi b.
Its energies are +/-sqrt(|f|^2+d^2). At isotropic J=1, the only zeros of f
are (a,b)=(1/3,2/3),(2/3,1/3); d there is +/-6 sqrt(3) kappa.
Hence nonzero kappa gives a positive global band separation on the compact
zone. The sampled minimum |E| printed by the runner is half the band
separation and is not a certified value of the continuous minimum.
The 36-by-36 overlap calculation returns opposite integer-valued discrete
Berry sums at kappa=+/-0.2. It checks nonvanishing overlaps and band gaps.
No edge spectrum, interacting spin phase, physical charged edge mode or
completeness of gauge sectors is established by this finite band calculation.

## Validation and remaining work

The runner retains five checks, including all original finite matrices,
support enumeration, multiplets and band calculations. Numerical agreement
is evidence for these supplied constructions, not an audit verdict.
Physical gauge projection on extended graphs, a realized composite pattern,
and physical charged excitations remain separate work. The original PR
branch preserves the broader interpretations for explicit recovery.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

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

Original PR #9144, frozen head `12645c9624a92743c2a84af8ba1207143cf42a74`.
