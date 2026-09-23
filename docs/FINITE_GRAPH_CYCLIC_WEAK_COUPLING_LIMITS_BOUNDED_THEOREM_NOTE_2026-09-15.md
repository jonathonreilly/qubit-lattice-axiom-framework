---
claim_id: finite_graph_cyclic_weak_coupling_limits_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/cyclic_scaling_check_2026_09_15.py
upstream_dependencies: ["docs/POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14.md", "docs/EXACT_GAUSS_REDUCTION_AND_FIXED_VOLUME_WEAK_COUPLING_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-13.md", "docs/FINITE_INTEGER_LINK_WEAK_COUPLING_PAYLOAD_AND_MONOPOLE_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-13.md"]
claim_scope: "Bounded conditional finite-graph cyclic weak-coupling limits; supplied hypotheses and limit order retained in full proofs."
---

# Finite-graph cyclic weak-coupling limits

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope and actual premises

The complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.

Actual mathematical dependencies:

- [POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14](POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14.md).
- [EXACT_GAUSS_REDUCTION_AND_FIXED_VOLUME_WEAK_COUPLING_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-13](EXACT_GAUSS_REDUCTION_AND_FIXED_VOLUME_WEAK_COUPLING_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-13.md).
- [FINITE_INTEGER_LINK_WEAK_COUPLING_PAYLOAD_AND_MONOPOLE_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-13](FINITE_INTEGER_LINK_WEAK_COUPLING_PAYLOAD_AND_MONOPOLE_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-13.md).

Evidence correction: the separate full-dense corroboration mentioned in the original narrative has no recovered separate source/output. That ancillary narrative is unverified and supplies no numerical evidence here; the analytical proof and identifiable final program remain separately scoped.

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK17_CYCLIC_WEAK_COUPLING_SPECTRAL_LIMITS

Original source identity: `BLOCK17_CYCLIC_WEAK_COUPLING_SPECTRAL_LIMITS.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Cyclic weak-coupling limits and what a small plaquette deficit misses

Personal derivation, 2026-09-15. PROVISIONAL; personal checks and review complete.
No independent review or axiom update. Fixed-volume spectral limits below
are distinct from an infinite-volume photon theorem.

#### 1. Question, parents and exact domain

Main e0ef7cf4633034a8c1e6d57f5812cc4275bf1349 contains three relevant supplied
results, all read in full: the positive cyclic gauge/history construction,
the exact integer Gauss/fixed-volume oscillator construction, and the hard
integer-link weak-coupling payload/monopole-density construction. The latter
two use an OPEN hard flux boundary. The cyclic construction wraps its flux
boundary and has a cosine electric dispersion. Neither feature can be
discarded when the cutoff and weak coupling are taken together.

Fix a connected contractible finite cubical complex with all elementary
plaquettes, at least one plaquette, and no changing volume. Write D for
vertex-link incidence and F for link-plaquette incidence. Choose an integer
rooted tree flow R and fundamental cycle matrix C exactly as in the parent:

 DR=I-e_root 1^T, DC=0, C_chord=I_c, F=C Z.

The columns z_p of Z generate Z^c over the INTEGERS. Positive diagonal
electric and magnetic weights are W_E and W_B. A=Z W_B Z^T and
K=C^T W_E C are positive definite. These hypotheses exclude unhandled
periodic-box harmonic directions and finite-index magnetic sublattices.

There are finitely many charged CAR modes on this graph, opposite species
in the cyclic parent's realization, and bounded fixed matter coefficients.
Let rho_f be the integer charge in occupation state f. Initially impose
total charge zero modulo odd N>=3. Along N->infinity, eventually N exceeds
the maximum possible absolute total charge, so precisely the integer-neutral
matter space M remains. This is a FIXED-GRAPH statement; it is not a claim
that global aliases disappear this way in a growing volume.

For every allowed f, the exact cyclic physical fields are uniquely

 E=rep_N(R rho_f+C n),       n in (Z/NZ)^c.                 (1)

The tree-leaf proof of uniqueness works over Z/NZ without dividing by N.
Thus it is valid also for odd composite N. Unlike hard truncation, the
cyclic physical space in these coordinates is a product M tensor C^(N^c).
It still represents a Gauss-constrained state in the original variables.

A charge-plus hop across a tree edge leaves n unchanged, across chord j
shifts n by e_j; charge-minus hops have the opposite shifts. Plaquette p
shifts n by z_p. CAR signs and the original matter matrices are retained.
The electric and magnetic terms are

 H_E=(g^2 N^2/(2a pi^2)) sum_l w_l
                 sin^2(pi(R rho_f+C n)_l/N),
 H_B=(1/(a g^2)) sum_p w_p [1-Re T_(z_p)].                (2)

Let H_m^0 be the original finite matter Hamiltonian with every link shift
replaced by identity, restricted to M. Any supplied onsite Q^2 term remains
in H_m^0; the notation does not assert that it is a free fermion model.

The scale controlling these limits is

 ell_g=g N.                                             (3)

All other coefficients and the graph stay fixed. Both g->0 and N->infinity
are assumed for the three-limit statement unless fixed N is explicitly named.

#### 2. Finite ell: a periodic Schrödinger operator

If ell_g->ell in(0,infinity), the limiting gauge configuration space is
the c-dimensional torus of side ell, with coordinate x=g n modulo ell.
The limiting operator is

 H_cyc,ell = (1/(2a))[-partial^T A partial
              +(ell/pi)^2 sum_l w_l sin^2(pi(C x)_l/ell)],
 H_limit,ell=H_cyc,ell tensor I + I tensor H_m^0.         (4)

The boundary conditions are PERIODIC. They are not the Dirichlet conditions
of the hard-cutoff parent's polytope, and the potential is not replaced by
its quadratic tangent on the whole finite torus.

Here is a fixed-index eigenvalue/form proof. Embed the discrete amplitudes
as piecewise constants in the unit torus y=n/N, multiplying by N^(c/2).
The magnetic form becomes

 (1/(2a ell_g^2)) sum_p w_p
                  ||N(T_(z_p/N)-I)u||_2^2.             (5)

The electric potential converges uniformly to
ell^2/(2a pi^2) sum_l w_l sin^2(pi(C y)_l), because all R rho_f are bounded
and their offsets divided by N vanish. Bounded matter shifts by e_j/N
converge strongly to identity on bounded-energy interpolants.

For compactness, express each e_j as an integer combination of z_p.
Telescoping the commuting translations bounds its nearest-coordinate
difference quotient by a fixed linear combination of the quotients in(5).
Periodic multilinear interpolants have bounded H^1 norm; their L^2 distance
from the piecewise constant embeddings tends to zero. Rellich compactness
on the fixed torus and weak derivative lower semicontinuity supply the
lower-form bound. Sampling smooth periodic vector functions supplies the
recovery bound. Min-max then gives convergence of every fixed-index
eigenvalue and each isolated spectral cluster to(4). Degenerate clusters
do not supply a preferred eigenvector basis.

#### 3. Infinite ell: the full oscillator is recovered

If ell_g->infinity, center every chord coordinate x_j in[-ell_g/2,ell_g/2).
Since R has zero chord rows and C_chord=I, chord contributions alone give

 H_E >= (2/(a pi^2)) sum_(chords j) w_j x_j^2.           (6)

This follows from sin(pi |x_j|/ell_g)>=2|x_j|/ell_g. Other link terms
remain nonnegative even when Cx wraps across their centered representatives.
Thus low-energy states have a uniform second moment in the centered
chord coordinates. No false global inequality with unwrapped Cx is needed.

On every fixed coordinate ball, the electric potential converges to
x^T K x/(2a), the matter offsets g R rho_f vanish, and discrete derivatives
converge as in(5), now at step g. Apply Rellich on that ball and use(6)
to control the outside norm. The distant torus seam is irrelevant to the
local lower bound; a zero extension across that seam is NOT assumed to have
a global H^1 bound. Compactly supported recovery functions avoid the seam.
Exhaustion and min-max give

 H_limit,infinity=[-partial^T A partial+x^T K x]/(2a)
                         tensor I + I tensor H_m^0.     (7)

This is the same full oscillator as the hard integer parent. The two
regulators agree in this limit even though their finite-ell limits differ.
Its frequencies are sqrt(eig(A^(1/2) K A^(1/2)))/a. All compactness constants
can depend on this fixed graph; no growing-volume spectral conclusion follows.

#### 4. Vanishing ell: finite-energy gauge oscillators disappear

If ell_g->0, the electric operator norm is bounded by

 ||H_E|| <=ell_g^2 sum_l w_l/(2a pi^2).                 (8)

The common invariant vector of all cyclic translations is the uniform
cycle amplitude. Integer generation by z_p makes it the UNIQUE zero vector
sector of H_B. Let P0 project onto this vector tensor all of M. The same
telescoping inequality used for(5), or finite Fourier characters, gives

 Q0 H_B Q0 >= gamma_graph/ell_g^2,
 gamma_graph>0 independent of large odd N.              (9)

For clarity, the character energy is sum_p w_p(1-cos(2pi z_p dot k/N)).
Integer expressions for e_j bound sum_j|exp(2pi i k_j/N)-1|^2 by a constant
times this energy. A nonconstant character has at least one nonzero k_j,
so its latter sum is at least4 sin^2(pi/N)>=16/N^2.

H_m commutes with H_B, since its flux factors are commuting translations
and its matter factors act on the other tensor factor. Its P0 restriction
is exactly H_m^0. If d=dim M, the first d eigenvalues of H_B+H_m are those
of H_m^0 for sufficiently small ell_g; all other levels are bounded below
by gamma_graph/ell_g^2-||H_m||. Adding(8) gives convergence of precisely
these d finite levels and divergence of the remaining gauge excitations.
Resolving the Q0 eigenvector equation also bounds its norm by O(ell_g^4)
for any bounded-energy eigenvector. This estimate uses the large magnetic
gap, not a presumed matter gap.

At fixed odd N the same argument works with its exact finite magnetic gap,
but the matter space is the modular-neutral space M_N and can contain total
charge aliases. Neither version supplies a Maxwell oscillator spectrum.

##### Integer Gauss aliases can persist in this different limit

Take two adjacent plaquettes, no matter, and chord coordinates n1,n2 in
[-S,S], N=2S+1. Orient their circulation so that their shared edge carries
n1-n2 and every other edge carries plus or minus one of n1,n2. Only the
shared field can wrap. The modular field violates integer Gauss law at
the two endpoints of that edge exactly when |n1-n2|>S. In the uniform
magnetic ground vector its probability is

       P_alias=S(S+1)/(2S+1)^2 ->1/4.                 (9a)

This counts both outer triangles of the square of chord labels. The
vanishing-ell ground vector approaches the uniform vector with O(ell_g^4)
norm error by the preceding spectral argument, so(9a) also holds for
the actual pure-gauge ground states as g->0, N->infinity, gN->0.

For a finite positive ell, the limiting two-coordinate pure-gauge operator
has a strictly positive ground function on the connected torus. One direct
reason is that its positive-definite kinetic matrix gives a strictly positive
heat kernel, and bounded real potential multiplies Brownian path weights by
strictly positive factors. Its semigroup is positivity improving. The
open wrapped triangles consequently retain nonzero probability. Their
boundary has measure zero, so spectral/state convergence passes this
indicator expectation to the limit. No numerical lower constant is claimed.

This is precisely outside Block16: that theorem keeps g fixed and uses a
uniform UNRESCALED electric second moment. That moment diverges along the
present weak-coupling sequence. Local removal of modular aliases cannot be
reused after silently exchanging these limits. The vanishing plaquette
deficit and a nonzero integer-alias probability coexist in the same supplied
pure-gauge model; no charged-phase inference is needed for the counterexample.

#### 5. A one-plaquette discriminator and checked normalization

For a=1, unit weights and a single neutral plaquette, C=(1,1,1,1)^T and
A=1. The finite matrix and its finite-ell limit are

 H_(g,N)= (2 g^2 N^2/pi^2) sin^2(pi n/N)
                  +(1/g^2)[1-(T+T^*)/2],
 H_ell=-1/2 d^2/dx^2+(2 ell^2/pi^2)sin^2(pi x/ell),
                         x modulo ell.                (10)

For every finite ell,

                         0<E0(ell)<1.                  (11)

The lower bound is strict because a zero of the sum of the positive kinetic
and potential forms would be both constant and supported where the potential
vanishes. For the upper bound periodize the full oscillator Gaussian:

 Phi_ell(x)=sum_(j in Z) exp[-(x+j ell)^2]>0.

Every summand obeys(-.5 d^2+2(x+j ell)^2)phi_j=phi_j, whereas the periodic
potential in(10) is at most2(x+j ell)^2. Summing the absolutely convergent
derivative series gives H_ell Phi_ell<Phi_ell pointwise. Its Rayleigh
quotient is strictly below1. Thus cyclic finite payload lowers this energy;
the hard Dirichlet truncation raises it. Neither equals the full oscillator.

There is also a state discriminator independent of the energy convention.
Embedding centered cyclic amplitudes into the x line limits their support
to[-ell/2,ell/2] in the finite-ell limit. The full oscillator ground density
sqrt(2/pi) exp(-2x^2) has outside mass erfc(ell/sqrt2). No state with this
finite support can recover its complete electric distribution arbitrarily
accurately. This statement alone is not a photon-phase exclusion.

With z=pi x/ell, equation(10) is the standard Mathieu problem with
q=-ell^4/pi^4. Its exact ground energy is

 E0(ell)=ell^2/pi^2+pi^2 a0(-ell^4/pi^4)/(2 ell^2).      (12)

The standard definition and periodic sector are checked against
[DLMF 28.2](https://dlmf.nist.gov/28.2). The corresponding established
small-parameter and large-parameter expansions give

 E0(ell)=ell^2/pi^2-ell^6/(4pi^6)+O(ell^14), ell->0,
 E0(ell)=1-pi^2/(8ell^2)-pi^4/(64ell^4)+O(ell^-6),
                                                   ell->infinity. (13)

These special-function asymptotics are credited to
[DLMF 28.6.1](https://dlmf.nist.gov/28.6.E1) and
[DLMF 28.8.1](https://dlmf.nist.gov/28.8.E1), not claimed as new mathematics.
The first large-ell correction is independently recovered from
-(2pi^2/(3ell^2))<x^4> in the oscillator vacuum, where <x^4>=3/16.
They describe the limiting differential operator, not a uniform joint
error estimate in finite g,N. Magnetic finite-difference errors also remain
before the continuum limit.

#### 6. Small plaquette deficit is compatible with the wrong spectral limit

Return here to the periodic cubic cyclic model of the positive-history
parent, with V cells and D=(1/V)sum_p w_p<1-Re U_p>. The following bound
is uniform in V and distinct from the fixed-volume theorem above.

Take the uniform amplitude over all divergence-free cyclic electric fields
and the balanced onsite matter minimum from Block16. It is physical.
Every plaquette shift leaves the gauge amplitude invariant, so its magnetic
deficit is EXACTLY zero. Each link lies on an elementary plaquette, whose
shift acts transitively on that link's Z_N values; consequently each link
marginal is uniform. Its electric mean is

 <H_E>trial=ell_g^2 V sum_i w_i/(4a pi^2),               (14)

since the cyclic average of sin^2 is1/2. Its hopping expectation vanishes.
The full matter lower bound is E_on,min-2sum_l||V_l||, where V_l includes
both charged species as in Block16. Comparing the physical ground energy
with this trial and using H_E>=0 proves for EVERY physical ground mixture

 D <=g^2[ell_g^2 sum_i w_i/(4pi^2)
                         +(2a/V)sum_l||V_l||].         (15)

Thus bounded ell_g, including fixed finite N at g->0, already gives an
O(g^2) deficit. For pure gauge it gives O(g^4 N^2). The hard shift-chain
ceiling does not apply to a cyclic unitary plaquette. This is an explicit
different-regulator escape from that narrow necessity statement, not a
contradiction of it. A small plaquette deficit therefore cannot establish
the oscillator/Gaussian limit, let alone a charged Coulomb phase.

#### 7. Remaining obligations and checks

The statements are fixed-volume spectral limits and a separate volume-uniform
one-point ground-state bound. They do not exchange those limits, prove a
massless photon, exclude monopole condensation or pairing, preserve Weyl
matter, or select any of these supplied coefficients from the axioms.
The regulator must grow faster than1/g to recover the declared full Gaussian
finite-volume comparator; this does not prove that every finite-spin model
needs that payload to possess an emergent photon.

The personal checker verifies exact cyclic Gauss coordinates on adjacent
plaquettes at N=3,5,9,15, including composite moduli and full-field N=3
enumeration with neutral and nonzero local charges. The uniform-flow alias
counts agree exactly with(9a), and all seven link marginals are uniform.
For the actual two-plaquette ground state at N=33, g=N^(-3/2), the alias
probability is about.249769 while the magnetic energy is about8.4e-9.
This numerical example illustrates the analytically proved coexistence.

Independent electric-grid and Fourier-continuum constructions check all
three scaling regimes. The coupled two-plaquette continuum includes the
shared-edge potential; it is not two independent rotors. Refined Fourier
levels differ by at most4.2e-12 in those fixtures. Its finite-ell alias
integrals are numerical quadrature diagnostics, not certified lower constants.
The one-plaquette Mathieu comparison differs by at most4.7e-12; oscillator
creation/annihilation matrices recover the two displayed large-ell correction
coefficients exactly. The small-ell first excited gap grows as2pi^2/ell^2.

The charged cycle uses the Block16 independently assembled CAR/Gauss
Hamiltonian. Its projection onto the uniform cycle vector agrees EXACTLY
with the separately assembled70-dimensional matter comparator, including
the supplied Q^2 interaction. All four lowest levels, WITH multiplicities,
approach the continuum sums. At N=33 their maximum errors are about3.27e-5
for ell=2 and.00138 for ell=4. These are finite checks, not a uniform rate.
Actual ground-state plaquette deficits obey the noncubic specialization
of the same variational inequality.

Two initial solver failures are preserved before correction. A nearly
degenerate pure-gauge cluster stalled sparse iteration; direct diagonalization
retained all three levels and the same residual tolerance. The initial
charged sparse run omitted one member of a triply degenerate level while
reporting small residuals. Dense conserved-number blocks, merged WITH
multiplicity, resolve that error; a full dense small matrix independently
confirms the missing level. No physical formula was changed to fit a solver.

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK17_ROUTE_AND_NO_GO_REVIEW

Original source identity: `BLOCK17_ROUTE_AND_NO_GO_REVIEW.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Block17 route and no-go review

PROVISIONAL personal review; independent retention pending.

N1 — Distinct routes. Exact modular Gauss coordinates, discrete-to-periodic
form convergence, growing-torus confinement, a large magnetic-gap reduction,
positive uniform-flow trial and an exact two-face alias count address
different obligations. The hard integer parent remains a different valid
regulator route. None is silently treated as a full phase theorem.

N2 — Independence. The finite-ell periodic spectrum, vanishing-ell loss of
gauge oscillator levels and integer-alias counterexample are consequences
of the declared cyclic scaling. They are not three independent axiom walls.
The small-deficit bound is compatible with all of them and cannot decide
which spectral/state limit occurs.

N3 — Hidden premises. Fixed contractible graph, integer plaquette generation,
positive weights, fixed matter coefficients, bounded orbital count and the
specified g,N scaling are explicit. Integer neutrality eventually follows
from fixed graph and N growth; this argument is not used in growing volume.
Matter Q^2 terms survive in H_m^0. Periodic spatial harmonic directions are
excluded from the theorem rather than assigned an invented gap.

N4 — Matching. The cyclic electric cosine, boundary wrap, CAR signs and
positive magnetic constant are retained. The hard parent's Dirichlet theorem
is not copied onto a torus. The one-plaquette Mathieu normalization and
the two-plaquette shared-edge alias match the actual finite matrices.
The uniform trial is a physical Gauss state, not an unprojected Bloch sea.

N5 — Rhetoric. Full Gaussian fixed-volume recovery requires gN->infinity
in this declared regulator comparison. It is not a universal lower bound
on the qubits needed for every emergent photon. A converged one-point
deficit is explicitly separated from phase identification. Two numerical
failures are preserved; small residuals did not certify ordered eigenvalue
multiplicity, and that error was corrected before acceptance.

N6 — Partial closure. The three scaling regimes and a charged fixed-volume
comparator are supplied. One may use gN->infinity, use the different hard
integer regulator, or investigate a finite-spin phase without demanding
this full Gaussian comparator. No such route is declared closed by the
small-payload example. Thermodynamic excitation/control remains missing.

N7 — Steelman. A fixed finite cyclic model can have exactly flat magnetic
trial states and O(g^2) ground deficits without taking N of order1/g.
This explicit escape defeats a universal version of the hard shift-chain
payload claim. Conversely, choosing gN->infinity recovers the fixed-volume
oscillator within the very same positive cyclic family. No new axiom is
needed for that escape.

N8 — Cross-cycle echo. Earlier campaigns warned that one-point defect
density is not a photon proof. Here an exact spectral and integer-Gauss
counterexample makes the analogous deficit gap concrete. Block16's fixed-g
state theorem remains valid; its divergent weak-coupling constants are
not ignored when changing the order of limits. Special-function facts are
credited to DLMF and not counted as newly discovered mathematics.

Disposition: provisional regulator-specific theorem and explicit
counterexample to a deficit-only inference. Broad axiom no-go FAIL/not claimed.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: cyclic_scaling_check_2026_09_15](../scripts/cyclic_scaling_check_2026_09_15.py); [current cache](../logs/runner-cache/cyclic_scaling_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).
