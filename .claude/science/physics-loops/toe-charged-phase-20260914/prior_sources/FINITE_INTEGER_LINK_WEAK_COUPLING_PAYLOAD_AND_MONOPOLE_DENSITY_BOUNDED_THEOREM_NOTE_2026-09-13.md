---
claim_id: finite_integer_link_weak_coupling_payload_and_monopole_density_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "For the specified charged hard integer-flux Hamiltonian, derive matching necessary and sufficient cutoff order S=1/g for an O(g squared) weighted plaquette deficit in physical ground states, uniformly in spatial volume. A positive redundant closed-flow trial controls the ground energy, and a compressed principal-angle monopole POVM has an explicit density bound and a qualitative finite-bandwidth floor. The result does not establish a photon, a monopole particle gap, survival of Weyl matter, a common renormalized cone, universal encoding optimality or an axiom update."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/finite_integer_link_weak_coupling_payload_and_monopole_density_2026_09_13.py
---

# A fixed finite-link ground-state bound and its weak-coupling payload

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

## Result and supplied domain

A finite integer-link Hamiltonian with charged four-orbital matter admits a
physical ground-state bound uniform in spatial volume. The local flux cutoff
must grow as 1/g to reach the stated O(g^2) weak-coupling plaquette deficit;
a positive closed-flow trial state proves that the same order is sufficient.
The necessary direction is an exact finite-chain spectral bound. The sufficient
direction handles redundant plaquettes without assuming a product physical
Hilbert space or a free-fermion sea satisfying Gauss law.

The same estimate bounds a specified local magnetic-angle charge statistic.
This is a gauge-invariant POVM quantity obtained by compressing the conventional
principal-plaquette definition. Its interpretation as emergent monopole
particles, and the existence of the charged photon phase, remain unproved.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-chain necessity, positive-flow physical trial sufficiency and ground-state plaquette/monopole-POVM bounds."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Control an actual physical ground-state quantity of a charged finite-link candidate at weak coupling."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Control long-distance correlations or excitation/disorder response in the actual charged model; a small deficit or one-point density does not determine the photon phase."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

The [minimal framework memo](MINIMAL_AXIOMS_2026-06-29.md) is the ontology
reference. The [edge matter construction](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md)
and [current finite integer-link source](THE_FERMION_ON_COMPACT_U1_LINKS_THE_INTEGER_FLUX_SELECTS_THE_STAGGERED_GAUSS_LAW_AND_JOINS_THE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md)
identify conditional comparison domains. The CAR algebra and its physical
encoding, graph, Hamiltonian time, coefficients and cutoff family are supplied.
The complete finite Hamiltonian and trial construction are redeclared here;
no unmerged proposal is used as a theorem premise. No axiom, approved primitive,
state formation law or audit verdict is added.

Gauge-invariant variational states and integer-flow formulations are established
methods; see [Horn and Weinstein](https://www.slac.stanford.edu/pubs/slacpubs/2750/slac-pub-2864.pdf),
sections 2 and 3.2-3.4. The general mechanism is not claimed as a new discovery.
The explicit finite-support positive push-forward and the two-sided cutoff
order are the construction proved below. The compact-cube charge convention
is also established; [Akerlund and de Forcrand](https://arxiv.org/pdf/1505.02666),
section III, state it and distinguish a dilute-monopole phase from an exactly
monopole-free angle-restricted model. Their classical action is not the finite
Fourier cutoff used here.

## Declared family and target

Take a periodic cubic graph with L_i>=3, V cells, 3V oriented links and 3V
positively oriented plaquettes. Each link belongs to four plaquettes and
each plaquette to two cubes. Let a,g>0, r>=0, w_i>0 be fixed supplied
coefficients. Put a hard integer link |n>, -S<=n<=S, with
U_S|n>=|n+1> for n<S and U_S|S>=0. Use four CAR orbitals per cell and

```text
H_S = (r/a) sum_x c_x^dag h_on c_x
    + (r/a) sum_(x,i) [c_x^dag T_i U_(x,i) c_(x+i) + h.c.]
    + (g^2/(2a)) sum_(links i) w_i E_l^2
    + (1/(g^2 a)) sum_(plaquettes normal i) w_i [1-Re W_p,S],
G_x = div(E)_x-(N_x-2),                  Re W=(W+W^dag)/2.
```

The magnetic constant is explicitly chosen so its term is positive. The
claim below concerns the deficit observable itself, so an additive vacuum
energy convention cannot remove it. The onsite Hermitian matrix h_on has
exactly two negative eigenvalues. The T_i have nuclear norms q_i; define
q_sum=sum_i q_i and w_sum=sum_i w_i, w_min=min_i w_i.
The physical space G_x=0 is finite and nonempty.

The concrete mixed carrier has 0<b<pi/2, 1/2<zeta<1 and
0<mu^2<1-zeta^2, with sigma acting on orbital and tau on flavor:

```text
h_on=(2+zeta)sigma3+mu tau_x(sin b sigma1+cos b sigma3),
T_i=(C_i-i S_i)/2,
C_x=-sin b sigma1-cos b sigma3, S_x=tau_z(cos b sigma1-sin b sigma3),
C_y=C_z=-sigma3,                 S_y=sigma2, S_z=0.
```

Here q_i=2 and q_sum=6. In the tau_x basis the onsite eigenvalues are
+/-epsilon_eta, epsilon_eta=sqrt[(eta mu sin b)^2+(2+zeta+eta mu cos b)^2].
Thus two negative onsite orbitals can be filled at each cell. Their product
has exactly N_x=2, even fermion parity per cell and onsite energy E_on,min,
the minimum of the unconstrained onsite many-body Hamiltonian. This local
product is only an auxiliary variational state, not the proposed physical
Weyl ground state. Its hopping expectations vanish.

Define the weighted plaquette deficit in any state rho by

```text
D(rho)=(1/V) sum_(plaquettes normal i) w_i <1-Re W_p,S>_rho.
```

The first target is D=O(g^2), uniformly in V, as g tends to zero with fixed
w_i,r,q_i and a. This is a precise weak-fluctuation target in this specified
integer-link family. It does not define an entire Coulomb phase.

## Exact local cutoff lower bound

For one plaquette write b_p for its oriented integer boundary vector. In
electric-flux space W_p,S shifts E to E+b_p whenever the result stays inside
the box. Its shift orbits are finite disjoint open chains. Any participating
link changes by one per step, so no chain has more than 2S+1 states. The
Hermitian half-adjacency matrix on a chain of n states has eigenvalues
cos(j pi/(n+1)), j=1,...,n. It follows that

```text
lambda_max(Re W_p,S)=cos(pi/(2S+2)),
1-Re W_p,S >= [1-cos(pi/(2S+2))] I.
```

The maximum is attained on the length-2S+1 chain E=m b_p, -S<=m<=S, with all
other fluxes zero. Since div b_p=0, this chain is available even with neutral
matter N_x=2 and exact Gauss law. Simultaneous saturation for all plaquettes
is not asserted. Summing positive operator inequalities gives, for every state,

```text
D(rho)>=w_sum[1-cos(pi/(2S+2))]>=w_sum/[2(S+1)^2].            (1)
```

The last inequality is 1-cos x>=2x^2/pi^2 for |x|<=pi. Consequently, if a
family of states satisfies D<=K g^2 with a fixed finite K>0, then

```text
S+1 >= sqrt[w_sum/(2K)] / g.                                 (2)
```

This necessary cutoff scaling is independent of the matter dynamics and
volume. It applies to the hard unit-amplitude shift family just defined,
not to every finite-spin gauge encoding or every possible infrared phase.

## A positive closed-flow trial state at fixed cutoff

Let B be the link-by-plaquette boundary incidence matrix and D_vertex the
vertex-by-link incidence matrix. Then D_vertex B=0. Introduce auxiliary
integers n_p in [-M,M], M>=0, and the nonnegative path weights

```text
kappa=pi/(2M+2),
f_M(n)=cos(kappa n) for |n|<=M, and 0 otherwise,
F(n)=product_p f_M(n_p).
```

Define the linear push-forward on finitely supported amplitudes by
L|n>=|Bn>, and set psi=L F. This is a finite sum at any finite graph and M.
It is not an isometry, and no bounded-operator assertion about L on an entire
infinite Hilbert space is needed. Redundant plaquette flows add their positive
amplitudes. In particular psi(0)>0, so psi is nonzero; its norm must be taken
after the push-forward, not assumed equal to the product norm of F.

Every supported electric vector obeys div E=0 and |E_l|<=4M, since each link
meets four plaquettes. Thus psi belongs to one finite link cutoff S>=4M,
independently of V. It occupies the zero winding sector, which is sufficient
for a variational upper bound on the full physical ground energy.

On one auxiliary integer line, let t shift n to n+1. The elementary cosine
recurrence and the two outside endpoints give the componentwise identity

```text
(t+t^dag) f_M = 2cos(kappa) f_M + r_M,
r_M>=0, supported at n=+/- (M+1).
```

The map L preserves componentwise positivity and intertwines t_p with the
untruncated rotor plaquette W_p. Therefore, on the finite support involved,

```text
(W_p+W_p^dag) psi >= 2cos(kappa) psi      componentwise.
```

Pairing with the nonnegative psi and normalizing yields

```text
<Re W_p>_psi >= cos(kappa).                                  (3)
```

Compression to S>=4M leaves this expectation unchanged, since psi is already
inside its range. This step handles all linear dependencies among plaquette
boundaries; it does not replace three-dimensional plaquettes by independent
physical rotors. The lower bound can be strict because of redundant flows.

For the normalized trial state, the electric support bound and (3) give

```text
<H_E> <= (V/a) w_sum 8g^2 M^2,
<H_B> <= (V/a) w_sum [1-cos(kappa)]/g^2.                      (4)
```

Tensor psi with the onsite two-particle product described above. This is an
exact physical state of the coupled model, since its electric divergence and
N_x-2 both vanish. It achieves E_on,min in the onsite term and zero hopping
expectation. Neither a free filled Bloch sea nor a gauge-noninvariant product
of charged states is assumed to be physical.

## Matter norm and physical ground-state deficit

The Hermitian bond operator has a sharper bound than twice the norm of its
raising half. On the full rotor, the number-controlled unitary

```text
V_x=sum_n P_(N_x=n) tensor U^n
```

conjugates F+F^dag to F U+F^dag U^dag, where F=c_x^dag T_i c_y.
The one-particle Hermitian off-diagonal block has eigenvalues +/-s_j(T_i).
Its CAR second quantization therefore has norm sum_j s_j(T_i)=q_i.
Compression cannot increase this norm. The comparison unitary is used only
for an ambient operator-norm proof; it is not a proposed physical gate or
state preparation. Hence

```text
H_matter >= E_on,min I -(r/a) V q_sum I.                     (5)
```

Let rho_0 be any physical ground state, including a mixture in a degenerate
ground eigenspace. Variational comparison with (4) and positivity of H_E imply

```text
D(rho_0) <= g^2 B(g,M),
B(g,M)=w_sum[8g^2 M^2+(1-cos(pi/(2M+2)))/g^2]+r q_sum,
S>=4M.                                                       (6)
```

No fermion determinant or assumed gap enters (5)-(6). For 0<g<=1 take
M=ceil(1/g). Since gM<=2 and g(M+1)>=1,

```text
B(g,M)<=B_*=w_sum(32+pi^2/8)+r q_sum.                         (7)
```

Equations (1)-(7) prove matching necessary and sufficient order S=1/g for
the declared O(g^2) plaquette-deficit target: (2) is necessary for any state;
S>=4ceil(1/g) is sufficient for all physical ground states of this family,
uniformly in spatial volume. The coefficient bound is deliberately loose.
The exact expression (6) is stronger. Binary encoding of 2S+1 link states
then uses log2(1/g)+O(1) qubits at this optimal order, within this encoding.
The result is not a lower bound on the payload of every possible theory.

For a Gibbs state on the physical space at inverse temperature beta>0,
U_beta-E_0 <=log(dim H_phys)/beta and
log(dim H_phys)<=V[log16+3log(2S+1)]. The same argument gives

```text
D(rho_beta) <= g^2[B(g,M)+(a/beta)(log16+3log(2S+1))].         (8)
```

This finite-temperature extension remains an energy/deficit estimate. It does
not establish a thermal phase transition or a real-time photon pole.

## A local monopole POVM and its energy inequality

Use the full rotor angle representation with normalized Haar measure. Let
vartheta_p be the principal representative in [-pi,pi) of the oriented
plaquette angle. For each cube c define the integer

```text
Q_c=(1/(2pi)) sum_(outward cube faces) vartheta_p.
```

It is integer almost everywhere because the unwrapped cube curl sums to zero;
principal wrapping changes it by integer multiples of 2pi. Branch surfaces
have Haar measure zero and do not affect the multiplication operators. The
definition is the familiar compact-lattice monopole convention, redeclared
here; it is not an emergent monopole excitation gap.

For finite S define the local positive operators

```text
M_c,S=P_S Q_c^2 P_S,       I_c,S=P_S 1_(Q_c!=0) P_S.
```

These are compressions of functions of the twelve cube-link angles. They
are local and gauge invariant. More explicitly, a finite link has angle POVM
|theta;S><theta;S| dtheta/(2pi), where
|theta;S>=sum_(n=-S)^S exp(-in theta)|n>; its integral is identity. The cube
charge event is a gauge-invariant coarse graining of the product POVM.
Thus M_c,S is its mean square charge statistic, and 0<=I_c,S<=M_c,S.
The exact identity P Q_c^2 P-(P Q_c P)^2=P Q_c(1-P)Q_c P>=0
explains why it is generally false that M_c,S=(P_S Q_c P_S)^2. No sharp conserved
finite-dimensional magnetic charge is silently introduced.

Since 1-cos theta>=2theta^2/pi^2, Cauchy-Schwarz on six faces gives

```text
sum_(faces c) [1-cos vartheta_p] >= (4/3) Q_c^2.
```

Summing over cubes counts each plaquette twice. Multiplication inequalities
remain positive after compression, and P_S W_p P_S=W_p,S. Therefore

```text
sum_c M_c,S <= (3/2) sum_p [1-Re W_p,S]
             <= (3V/(2w_min)) D_operator.                   (9)
```

Here D_operator is the weighted operator whose expectation defines D(rho).
For every physical ground state of (6), the volume-averaged defect statistics
obey

```text
(1/V)sum_c <I_c,S> <= (1/V)sum_c <M_c,S>
                  <= [3g^2/(2w_min)] B(g,M)
                  <= [3g^2/(2w_min)] B_*.                    (10)
```

The last line uses (7). All volumes and all S>=4ceil(1/g) satisfy it. No
translation-invariant ground state is required: the statement is an average.
For a translation-invariant state it bounds the expectation on each cube.
A union bound also controls the probability of any nonzero cube charge in a
fixed finite region when that joint angle POVM is used. Equation (8) gives
the analogous finite-temperature bound with its explicit entropy term.

## Exact-zero defect exclusion has a narrow meaning

At any fixed finite S, the one-cube operator I_c,S is positive definite.
To see this, take a nonzero finite Fourier polynomial on the twelve cube-link
angles. A charge-one event has nonempty open interior: outward raw face
angles (-5pi/3,pi/3,pi/3,pi/3,pi/3,pi/3) sum to zero and lie in the cube
curl range, whose rank is five. Their principal representatives all equal
pi/3. Small variations of the link angles preserve the nonzero charge.
A nonzero finite Fourier polynomial cannot vanish on that open set. Its
integrated squared modulus there is strictly positive. Compactness of the
unit sphere in the finite link space therefore gives

```text
I_c,S >= epsilon_S I,       epsilon_S>0.                     (11)
```

At S=0 even the trivial one-state link has a Haar-distributed angle POVM;
this illustrates why the statistic cannot be identified with a count of
emergent monopole particles without an additional physical argument. The
qualitative constant is local and volume independent; no numerical value
or asymptotic rate for epsilon_S is claimed. Tensoring with other links or
matter and restricting to the physical space preserves the inequality. Thus
this particular finite-bandwidth angle POVM has a nonzero floor for its
unsharp charge statistic at fixed S. Finite-spin Coulomb phases can contain short-distance
virtual defects, so (11) is not a photon or deconfinement no-go. An exactly
restricted classical angle measure, a different encoding or a different
emergent defect observable is outside this statement.

## What remains unproved

The small-deficit and small-defect-density bounds concern actual physical
ground states of the supplied Hamiltonian, which improves on a finite-time
or classical-symbol comparison. They do not give the connected correlations,
helicity response, disorder-operator spectrum or monopole worldline estimates
needed to establish the charged Coulomb phase. They also do not show that
the matter spectrum remains Weyl-like, exclude a Mott or ordered matter
state, protect the common metric, or select these couplings from the axioms.

A density bound alone cannot exclude long-range order. For a simple logical
counterexample, a product of sqrt(1-rho)|0>+sqrt(rho)|1> has arbitrarily small
occupation rho but <b_x^dag b_y>=rho(1-rho) for all distinct sites. Averaging
over the common global phase makes the state number-symmetric while leaving
that correlation unchanged. This is a counterexample to an inference from
density to absence of order, not a proposed model of the monopoles here.
The next phase task must control the relevant correlations or excitations,
not relabel (10) as a photon theorem.

## No-Go Discipline Gate

This is a positive bounded construction with narrow regulator and measurement
statements. The charged Coulomb phase remains an unfinished route. No universal
no-go or axiom deficit is inferred from any count of tested approaches.

**N1 — Actual distinct formulations.**

| Route | Work and actual disposition | Marker |
|---|---|---|
| Finite shift-chain spectral analysis | Gives the exact plaquette ceiling and a necessary S=Omega(1/g) for the specified deficit target. It says nothing about all other encodings. | ATTEMPTED |
| Positive redundant plaquette-flow amplitudes | Gives a physical finite-support trial and sufficient S=O(1/g). This constructive escape defeats a blanket finite-link obstruction. | ATTEMPTED |
| Charged many-body norm/variational comparison | The controlled-shift and CAR singular-value argument extends the deficit bound to actual charged ground states. It does not determine their fermion spectrum. | ATTEMPTED |
| Compact angle geometry and positive compression | The cube inequality bounds the stated monopole POVM. It does not prove a monopole particle gap or a phase. | ATTEMPTED |
| Finite Fourier uniqueness and exact-zero event exclusion | Proves a qualitative floor for this unsharp event statistic. The classical hard-angle restriction in the cited literature is an explicit different-domain escape. | ATTEMPTED |
| Correlation/ordering discriminator | An explicit number-symmetric low-density state retains separated-site order, so a density-only argument cannot close the phase task. A correlation estimate remains live. | ATTEMPTED |

These routes differ in object and terminal obligation. They are not claimed
to exhaust the space of finite-spin or constructive field-theory approaches.
No row labels an untested full-phase route as ruled out by prior authority.

**N2 — Implication audit.** The small weighted deficit D implies a small
mean-square/event statistic M through (9); M is a downstream corollary, not
an independent wall. A small M alone has no stated converse deficit theorem.
The phase task P includes long-distance correlations and charged-spectrum
control, which are not supplied by D or M. No implication P=>this particular
quantitative regulator bound is assumed. A common renormalized cone C is a
stronger target formulated inside the desired phase; it is not added to P
as an independently counted axiom deficit. Relations beyond these stated
implications remain unresolved.

**N3 — Hidden-premise scan.** The graph, a,g,r,w_i, hard unit-amplitude shift,
CAR representation, two negative onsite orbitals, finite nuclear norms and
chosen weak-coupling target are declared. The trial is a finite positive sum,
not an assumed efficient preparation. Its non-isometric normalization is
explicit and challenged. The fixed cutoff is uniform in V at fixed g; it is
not held fixed while demanding vanishing deficit as g tends to zero. The
angle POVM, its coarse graining, and the distinction between compressing a
square and squaring a compression are explicit. No free Bloch sea, gapped
charged state, photon mode or selected metric is hidden in the variational
comparison. The thermal extension supplies its beta and entropy bound.

**N4 — Residual matching.** The current integer-link source identifies exact
finite gauge algebra and the remaining quantum phase distinction. Its
staggered background and code-parity results are not imported into this N-2
carrier. Horn/Weinstein supplies historical variational/flow context, not the
present finite-support estimate or a theorem for this charged quartet.
Akerlund/de Forcrand supplies the principal-angle convention and a classical
hard-angle comparator; its monopole-free action is not a counterexample to
the finite Fourier-POVM statement. No prior no-go is cited as a proof against
the full target.

**N5 — Resolution audit.** Per element: hard-link chain spectra and POVM
normalization are checked. Per site: onsite filling and CAR bond norms are
checked. Per mode: finite chain modes and a declared two-angle Fourier
compression section are checked; no photon spectrum is computed. Per block:
redundant cube-flow amplitudes, exact radical coefficients and charge-one/two
face fixtures are checked. Lattice wide: finite periodic incidence/counting
is checked and the volume-uniform inequalities are proved analytically; a
thermodynamic phase calculation is not executed. The two-angle compression
fixture is not mislabeled as a full twelve-link spectral computation. The
exact-zero exclusion is a statement about the specified measurement effect,
not all notions of magnetic particles or every finite-spin phase.

**N6 — Partial closure and conventions.** The finite physical trial and its
deficit bound close a concrete supplied-model realization task. The scaling
criterion concerns a bounded plaquette observable and cannot be removed by
shifting the zero of energy. It can be changed by changing the regulator or
the requested observable/accuracy target; that is outside this narrow theorem,
not an automatic new axiom. No binary payload bound is asserted for every
encoding. The CAR and state-formation imports are not silently retired.
No proposed primitive is given premise weight, and no approved primitive is
renamed as an independent missing axiom.

**N7 — Strongest counter-route to a universal negative.** A fixed finite-spin
Coulomb phase can tolerate a nonzero local magnetic-angle statistic and still
have a massless transverse sector. The finite-spin route described by
[Hermele, Fisher and Balents](https://arxiv.org/pdf/cond-mat/0305401) makes it
unreasonable to turn the Fourier measurement floor into a photon no-go.
Alternatively, a weak-coupling Hamiltonian argument can use the actual
Gauss-constrained low-energy spectrum and control monopole/disorder
correlations without demanding exact event exclusion. Its terminal task is
an excitation/correlation theorem that persists with the charged matter.
Neither the cutoff lower bound nor the one-point density result closes that
route. The phase campaign remains partial.

**N8 — Cross-cycle echo.** Current-main finite integer-link and cubic-ice
sources were read for the earlier jump from finite algebra, trial curvature
or component data to a quantum photon phase. This note gives an operator
lower bound and a variational upper bound with their exact objects, and keeps
the phase separate. The previous campaign's finite-time cutoff estimate is
context, not an unmerged premise. Its finite-time/ground-state distinction
motivates the present state bound, while the density/correlation distinction
prevents the same overclaim at a new level. No historical convention retirement
is treated as a theorem about the spectrum.

No universal no-go packet PASS is claimed. The narrow necessary regulator
scaling and finite-POVM statements stand on their explicit proofs; the phase
route remains unclosed.

## Reproduction and limits

Run `python3 scripts/finite_integer_link_weak_coupling_payload_and_monopole_density_2026_09_13.py`.
The primary builds periodic incidence matrices, finite shift chains, redundant
cube flows and occupation-basis CAR bonds. Exact rational-radical overlap
coefficients independently challenge floating-point accumulation; analytic
Fourier coefficients are challenged by separate quadrature. Prior versions,
mutation evidence and author corrections are preserved in the branch packet.
Author checks are not independent scientific acceptance.

The result is uniform in spatial volume for its declared deficit and
measurement statistics. It does not exchange weak-coupling, regulator,
thermodynamic and long-time limits to claim a continuum photon. Independent
source review, integrated landing checks and formal audit remain pending.
