---
claim_id: prepared_flat_sector_with_electric_dynamics_and_formation_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical diagnostics alone do not prove the analytic limits or select physical dynamics."
upstream_dependencies:
  - minimal_axioms
  - exact_fast_spectrum_and_formation_outputs_on_rings_bounded_theorem_note_2026-09-24
  - second_formation_clock_on_the_eight_site_rotor_ring_bounded_theorem_note_2026-09-24
  - finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/prepared_flat_sector_with_electric_dynamics_and_formation_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The source argument below comes from the frozen submission, with the narrow corrections identified in the combined review receipt. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. The Hamiltonians, quantum state spaces, instruments, backgrounds and preparations are supplied model assumptions. Fresh canonical controls are distinguished from archived diagnostics; no numerical scan substitutes for the displayed proofs.

# A prepared post-formation sector retaining electric dynamics and another birth

Primary-author conditional theorem candidate, 2026-09-23. This source is
provisional pending selective independent reconstruction. It closes a proposed
prepared-sector limit in the supplied model; it does not replace the actual
first output by that preparation or assert a native-axiom field theory.

## 1. Precise domain and result

Use the supplied alternating eight-site ring, unit-charge hard-core records,
Gauss background one on A, and integer link spin S normalized by
sqrt(S(S+1)). The sector after a first pair has six records, total charge
four, one minus, and P requires all A sites occupied. The checked finite-spin
target from the third campaign is

    H_S = eta H2_S + delta H4_S,
    H2_S=-A_S^dagger A_S,
    H4_S=(A_S^dagger A_S)^2-Z_S^dagger Z_S/2,
    eta=delta/epsilon^2=K C_S,       C_S=S(S+1),         (1)

where K,delta,kappa are fixed positive constants. A_S=Pi1 T_S P and
Z_S=Pi2 T_S Pi1 T_S P. Formation jumps are sqrt(kappa) B_(e,sigma),S
with B=-P j Pi1 T P, either resolved or combined coherently per edge exactly
as in the parent model. Let Gamma_S be their total loss. Let H2,H4,B,Gamma
denote the unit-rotor versions.

The physical rotor P space is ell^2(Z) tensor C^36. Its integer circulation
is f=E7; Gauss determines every E_e=f+d_e(q), with finitely many bounded
integer offsets d_e(q). Let P0 be the physical flat eigenspace of H2 at -4.
It has twelve internal states per circulation and is defined explicitly below.

For a normalized finite-support vector phi0 in P0, choose S large enough
that its support is physically allowed, and let the exact finite-spin
no-event vector start from this same phi0. Then, uniformly on compact
laboratory intervals 0<=t<=T,

 e^(-4 i eta t) exp[-it(H_S-i Gamma_S/2)] phi0
       -> phi(t)=exp[-it(H_flat-2i kappa)] phi0,        (2)

where

    H_flat = K P0 D2 P0 + delta P0 H4 P0.              (3)

D2 is the leading spin correction to H2, derived below. On this core the
proof gives a nonoptimal norm bound C_(T,phi0) eta^(-1/7). By contraction
and density, (2) extends as strong compact-time convergence to every
normalizable flat-sector input with convergent physical spin embeddings;
the quantitative constant is not uniform over all such inputs.

The limiting no-event survival is exp(-4 kappa t). The full unconditioned
effective density, including the one possible additional formation into the
fully occupied sector, converges as well. The checked microscopic-to-target
bound adds O(epsilon), so the same prepared-sector density limit follows
for the supplied microscopic family under (1).

The initial preparation restriction is essential. The actual normalized
first mark has only one half of its rotor norm in P0. This theorem does not
settle the other half or the full joint-scaling first-output waiting law.

## 2. A compact basis for the embedded flat sector

Write |C,r,f> for a P charge/field configuration: C is the occupied B pair
on the contracted four-site B ring; r=0,...,5 is the minus position in the
ordered occupied charge word starting at A0; f is the circulation. Put
c0(r)=-1 for r=0 and +1 otherwise. The following vectors are orthonormal
as a,b in {0,1}, r and f vary:

    a_(r,f)=(|01,r,f>-|23,r-1,f+c0(r)>)/sqrt(2),
    b_(r,f)=(|12,r,f>-|03,r,f>)/sqrt(2).                (4)

Indices r are modulo six. Distinct pairs in (4) have disjoint support.
The exact two-hop operator has diagonal -4. All its other moves connect
an adjacent B pair to an opposite B pair. The two routes out of each vector
in (4) cancel, including the cut's charge-word and circulation shifts. Thus
H2 a=-4a and H2 b=-4b.

In a word-twist sector alpha the off-diagonal two-particle matrix has
characteristic polynomial x^2[x^4-8x^2+8-8cos(alpha)]. Its generic kernel
has dimension two, exhausted by (4). The finitely many exceptional angle
fibers have measure zero. Consequently (4) spans the entire normalizable
eigenspace at -4. In particular P0 is a smooth trigonometric matrix in angle
space and a finite-range operator in f, although its energy is embedded
in dispersive spectrum and no uniform gap separates it.

This compact description also shows explicitly that P0 preserves every
weighted circulation space. It is not a spectral cutoff whose derivatives
diverge at the extra crossings.

## 3. The generated electric term and H4 inside this sector

For an integer link value E and shift k=+/-1, the normalized spin amplitude,
extended by zero beyond the physical interval, is

    g_(S,k)(E)=sqrt([1-E(E+k)/C_S]_+).                 (5)

Integer E makes E(E+k)>=0. A two-hop path in H2_S has coefficient
-g_(S,k1)(E1) g_(S,k2)(E2), with E2 evaluated at the actual intermediate
state. If a=E1(E1+k1) and b=E2(E2+k2), its rotor coefficient is -1 and
its D2 coefficient is (a+b)/2. This defines the symmetric finite-range
quadratic field operator D2 without discarding charge or intermediate-state
information.

Compression in (4) gives a diagonal electric operator. Write

    d_a(r,f)=4f^2+A_r f+B_r.

Its coefficients are

| r | A_r | B_r |
|---|---:|---:|
| 0 | -5 | 2 |
| 1 | -3 | 1 |
| 2 | 0 | 0 |
| 3 | 3 | 1 |
| 4 | 5 | 2 |
| 5 | 8 | 4 |

For b states, d_b(0,f)=4f^2-8f+4, and
d_b(r,f)=d_a(r-1,f) for r=1,...,5. These formulas follow directly by
averaging the four backtracking-hop a coefficients in each of the two
configurations in (4). Every nonbacktracking two-hop term maps an adjacent
B pair to an opposite pair and is killed by P0. Thus no off-diagonal electric
matrix element is being omitted from the compression.

The full D2 does not preserve P0. For example, for normalized a_(1,0),
||(1-P0)D2 a_(1,0)||^2=1. This nonzero coupling is retained in the proof
of (2), not replaced by an invariance assumption.

The rotor H4 does preserve P0. Its exact action is

    H4 a_(r,f) =12 a_(r,f)+2 b_(r,f)
                              -2 b_(r-1,f+c0(r)),
    H4 b_(r,f) =12 b_(r,f)+2 a_(r,f)
                              -2 a_(r+1,f-c0(r+1)).    (6)

One way to verify (6) is to use M=-H2, so M^2=16I on (4), and enumerate
Z^dagger Z= P T Pi1 T Pi2 T Pi1 T P. For a_(r,f) this gives
8 a_(r,f)-4 b_(r,f)+4 b_(r-1,f+c0(r)); the b relation is its adjoint.
There are only the displayed two different neighboring compact modes.
The author exact path runner enumerates all intermediate W sequences and
verifies every one of the twelve r/type cases as integer field-shift identities.
The electric coefficients are checked as symbolic polynomials in f, not a
fit to a finite set of fluxes.

Equation (6) is a twelve-site internal cycle with hopping magnitudes two
and circulation translations. Its norm is at most sixteen. Over a full
cycle the net circulation translation is four; its fiber eigenvalues are
12+4cos((4theta+2pi j)/12), j=0,...,11. This is matter motion coupled to
the global ring field. It is not an original four-edge spatial magnetic
plaquette or a three-dimensional photon mode.

The earlier exact second-loss identity Gamma=4 kappa Q_adj implies
Gamma P0=4 kappa P0, for both stipulated channel resolutions. Thus (3)
is selfadjoint on the domain of f^2: its electric diagonal is quadratic
with leading coefficient 4K>0, and its H4 part is bounded. Adding the
no-event loss is precisely the scalar -2i kappa in (2).

## 4. Global weighted bounds for the finite-spin expansion

Put ||psi||_m=||(1+f^2)^(m/2) psi||. Finite charge-dependent Gauss offsets
and finite circulation translations preserve equivalence of these norms.
For x>=0,

    |sqrt([1-x]_+)-1| <= x,
    |sqrt([1-x]_+)-1+x/2| <= x^2/2.                  (7)

For x<=1 the second difference equals
x^2/[2(1+sqrt(1-x))^2]; for x>=1 the stated inequality follows directly.
Using (7) on a product of two amplitudes bounds its remainder after
1-(x+y)/2 by a constant times x^2+y^2. These are global inequalities,
including field values near or beyond the physical spin interval.

Since the finite graph has finitely many legal paths, their input and output
circulations differ by a bounded integer, and each a is O(1+f^2), it follows
that for all vectors in the indicated weighted cores,

 ||(H2_S-H2-D2/C_S)psi|| <= C C_S^-2 ||psi||_4,
 ||(H4_S-H4)psi|| + ||(Gamma_S-Gamma)psi||
                         <= C C_S^-1 ||psi||_2.       (8)

The second bound is the telescoping difference of bounded finite products
of normalized shifts, using the first inequality in (7). The same
C_S^-1 weighted bound holds for each B_S-B. Matter/creation projectors
only remove paths and have norm at most one. Constants here depend on the
fixed graph and fixed coefficients, not on S.

Let A=H2+4I, F=K D2+delta H4-i Gamma/2 and
G_S=H_S+4eta I-i Gamma_S/2. Combining (1) and (8) gives

    G_S=eta A+F+R_S,
    ||R_S psi|| <= C eta^-1 ||psi||_4.                (9)

There is no inference from unweighted strong convergence multiplied by eta.
The fourth moment in (9) is essential. Each extended G_S is bounded for
fixed S and generates a contraction; its physical spin/Gauss subspace is
invariant. This extension lets the comparison use common rotor-space norms
without artificial boundary conditions on the candidate limiting state.

## 5. A cutoff corrector across the dispersive crossings

Fourier transformation makes A a smooth 36-by-36 matrix multiplier. The
complete ring eigenvectors from the independently checked spectral packet
are smooth on the real theta interval, with a harmless permutation at a
circle endpoint. The flat branches vanish identically. Its remaining
twenty-four eigenvalues are, up to a fixed label permutation and sign,

    lambda_j(theta)=2sqrt(2)cos((4theta+2pi j)/24),
    j=0,...,23.                                      (10)

Every zero of a nonflat branch is simple. Consequently, for small h>0,
the union of sets where 0<|lambda_j(theta)|<2h has circle measure at most
C h. The explicit eigenvectors have bounded derivatives of every fixed
order; this statement does not require noncrossing eigenvalues.

Choose a fixed smooth even chi with chi(x)=0 for |x|<=1 and chi(x)=1
for |x|>=2. Define the multiplier

    Q_h = f_h(A),
    f_h(x)=chi(x/h)/x for x!=0,    f_h(0)=0.

Differentiating the explicit eigenvector expansion yields, for m=0,...,4,

    ||Q_h u||_m <= C_m h^(-m-1) ||u||_m.              (11)

Although individual eigenvector labels permute around the circle, Q_h is
periodic because it is a function of the periodic physical matrix A.
Equation (10) and the one-dimensional H^1-to-L-infinity bound also give

    ||[I-chi(A/h)] u|| <= C sqrt(h) ||u||_1            (12)

whenever P0 u=0. Flat branches contribute zero for such u; the additional
zeros at isolated angles do not introduce point mass. Bounds (11)-(12)
replace the unavailable global inverse gap estimate.

Now phi(t) is the proposed evolution in (2) and lies in P0. For finite-support
phi0, its weighted norms through every finite order remain bounded on
0<=t<=T. Indeed its quadratic diagonal commutes with the f weights, while
the bounded, finite-translation operator (6) has a bounded weighted
commutator. Applying Gronwall to the weighted norm establishes these
bounds, first on finite cutoffs and then on their common core. Its time
derivative has the corresponding bounds with two additional moments.

Set u(t)=(I-P0)F phi(t). It has no flat component, and u,u' and the
weighted norms of u through order four are bounded on compact times by
a constant depending on ||phi0||_6 and T. Use the approximate solution

    phi_app(t)=phi(t)-eta^-1 Q_h u(t).                 (13)

Since A phi=0 and A Q_h=chi(A/h), substitution of (13) into the exact
equation gives a residual whose four relevant bounds are

    ||(i d/dt-G_S)phi_app||
       <= C_(T,phi0) [sqrt(h)+eta^-1 h^-3
                              +eta^-1+eta^-2 h^-5].  (14)

The first term is (12). The eta^-1 h^-3 term bounds both the correction's
time derivative and F times the correction, using the second-order nature
of F and (11). Equation (9) on phi and on the correction gives the last
two terms. The initial and final corrector norms are O(eta^-1 h^-1).
All these vectors are in the necessary weighted domains; G_S itself is
bounded, so Duhamel against its contraction applies directly.

Choose h=eta^(-2/7). The first two terms of (14) are eta^(-1/7), the last
is eta^(-4/7), and the endpoint corrections are eta^(-5/7). Integrating
the residual proves (2) on the finite-support flat core with the stated
nonoptimal eta^(-1/7) rate. Approximate a general flat vector by that core
and use contractions on both sides to obtain strong convergence, uniformly
on compact time intervals. Mixed trace-class states follow by finite-rank
approximation. No uniform bound over arbitrarily high field moments is claimed.

This is the cutoff-corrector strategy familiar from gapless adiabatic
arguments; see [Avron and Elgart, arXiv:math-ph/9805022](https://arxiv.org/abs/math-ph/9805022),
especially their commutator-equation discussion and Lemma 1. That theorem
is not imported here: P0 has infinite physical rank and F contains an
unbounded electric operator. Equations (7)-(14) verify the hypotheses and
estimates actually needed in this specific ring problem.

## 6. Another formation and microscopic transfer

Starting in this six-record sector, one additional pair fills all sites.
Hopping and further formation then vanish, so the fully occupied target
sector has zero Hamiltonian and zero loss. For a pure flat input the proposed
limiting unconditioned density is explicitly

    rho6(t)=|phi(t)><phi(t)|,
    rho8(t)=kappa sum_mu integral_0^t
                    B_mu |phi(s)><phi(s)| B_mu^dagger ds.      (15)

Use resolved B_mu or the stipulated coherent sums consistently. The total
loss identity gives Tr rho6=e^(-4 kappa t) and Tr rho8=1-e^(-4 kappa t).
This also verifies conservation of total probability. Equation (2), bounded
jump norms and the weighted/strong B_S convergence give trace-norm
convergence of the finite-spin version of (15) on compact intervals.
The removed common fast phase cancels inside each jump density.

The checked parent fixed-graph theorem approximates the microscopic density
by this finite-spin target with O(epsilon) error, uniformly in integer S.
Composition under (1) therefore yields the prepared microscopic density
limit and fixed-time number probabilities. This does not assert a new
uniform convergence theorem for microscopic histories conditioned on a
random first mark.

## 7. Checks and limits of the claim

The exact author controls verify the compact P0 vectors, symbolic electric
coefficients, nonzero D2 leakage and every term of (6). Separate controls
construct the full Gauss-compatible finite-spin sectors and all effective
jump matrices before propagating two prepared flat vectors at S=4,8,12,16,24,32.
Those are the complete physical finite-spin field intervals, not chosen field
cutoffs. The reference flat evolution has a declared circulation cutoff and
a Dyson-series bound for its omitted paths. Source identities, timings,
complete results and all failures/corrections are retained. The finite-size
agreement is corroboration; the convergence assertion rests on (7)-(14).

An actual first ring mark has flat weight one half. A measurement projecting
onto P0, or another preparation of (4), is an additional physical operation
whose selection/local implementation is not established here. This result
establishes neither the full unprepared post-event dynamics nor an indefinite
stream of new records. The eight-site system is full after the next event,
and its field then stops evolving in this target. The graph is fixed, its
field is a global circulation, and the quantum law/background/instrument
remain supplied. A spatial field phase, increasing volume, finite-resource
operation, native selection and empirical or TOE identification remain open.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** only the stated graph, sector, preparation, observation topology and order of limits.
- **N2 — Alternatives:** other laws, preparations, graphs and scaling paths are not excluded.
- **N3 — Imports:** supplied quantum and probability structures are mathematical assumptions, not repository axioms.
- **N4 — Dependencies:** companion arguments retain their explicit hypotheses and confer no audit grade.
- **N5 — Evidence:** exact finite controls and fresh numerical diagnostics corroborate proofs; floating computations are not interval enclosures. Archived diagnostic tables remain historical observations.
- **N6 — Resolution:** fixed-time, shrinking-time, fixed-index, growing-index and volume statements must not be interchanged.
- **N7 — Remaining work:** native model selection, physical implementation and empirical identification remain separate obligations.
- **N8 — Authority:** this source applies no audit verdict or retained grade.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary; it does not derive the supplied quantum model.
- [exact_fast_spectrum_and_formation_outputs_on_rings_bounded_theorem_note_2026-09-24](EXACT_FAST_SPECTRUM_AND_FORMATION_OUTPUTS_ON_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion argument within its stated hypotheses.
- [second_formation_clock_on_the_eight_site_rotor_ring_bounded_theorem_note_2026-09-24](SECOND_FORMATION_CLOCK_ON_THE_EIGHT_SITE_ROTOR_RING_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion argument within its stated hypotheses.
- [finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24](FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion argument within its stated hypotheses.

## Source and verification

Source PR #8832, frozen head `7013db3809221268780ffff04b716075d1e53626`. Complete original path dispositions and recovery branches are retained in the combined receipt. Review and affected-fix confirmation use the same primary session without subagents; no formal audit is claimed.

```bash
python3 scripts/prepared_flat_sector_with_electric_dynamics_and_formation_2026_09_24.py
```

The runner executes selected controls in a fresh temporary directory and includes generated result JSON in its authenticated stdout. Source history and deferred diagnostics remain recoverable from the original branch.
