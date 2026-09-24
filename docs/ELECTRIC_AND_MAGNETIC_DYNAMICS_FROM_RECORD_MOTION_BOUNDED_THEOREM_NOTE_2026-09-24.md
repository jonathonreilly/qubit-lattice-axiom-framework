---
claim_id: electric_and_magnetic_dynamics_from_record_motion_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated ordered limits; historical numerical tables are author observations, with fresh controls separately identified below."
upstream_dependencies:
  - minimal_axioms
  - uniform_local_ring_dynamics_with_slow_record_formation_bounded_theorem_note_2026-09-24
  - hardcore_record_motion_generates_gauge_rings_bounded_theorem_note_2026-09-24
runner: scripts/electric_and_magnetic_dynamics_from_record_motion_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical construction; unaudited.

The complete source argument below is preserved from the frozen submission. Its dated author-status statements and historical execution tables describe that submission, not an independent audit verdict. Quantum laws, enlarged site/link memories, Hamiltonians, instruments, backgrounds and preparations are supplied mathematical model assumptions. They are not new repository axioms or framework primitives. Fresh execution of the canonical runner checks the stated finite controls; finite tests alone do not establish the general proofs or limits.

# Electric and magnetic dynamics from record motion

Date: 2026-09-22. Status: author conditional construction, exact finite-spin
coefficients, and a proposed uniform local limit using the explicitly
provisional finite circuit lemma in
`UNIFORM_LOCAL_RING_DYNAMICS_WITH_SLOW_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md`.
Independent reconstruction pending. The construction supplies larger link
Hilbert spaces and increasing microscopic energy scales. It is not a derivation
from one native qubit per site, a Coulomb-phase theorem, or a TOE closure.

The useful change from the spin-half construction is that both the electric
quadratic energy and magnetic plaquette motion now arise from the same
record hopping. The electric mechanism is established quantum-link machinery:
[Zohar, Cirac and Reznik, arXiv:1303.5040v3, section VII.A, equations 97-101](https://arxiv.org/pdf/1303.5040v3)
already derive the nonunitary-link electric correction. Their auxiliary matter
and parameter scheme differ. The coefficients, hard-core counting, joint
scaling and live-record comparison below are checked for this declared model;
the general mechanism is not claimed as new physics.

## 1. Supplied model and the joint scaling

Use a d-dimensional cubic torus, d>=2, all periods even and at least six.
Matter is the same bosonic qutrit 0,+,- with at most one record per vertex.
Initially every A vertex carries plus and every B vertex is vacant. The
selected constraint is

    div E_x + 1_A(x) - q_x = 0.                         (1)

Replace each spin-half link by an integer spin S>=1. Put C_S=S(S+1) and

    E=S_z,
    U_S=S_+/sqrt(C_S),
    U_S|m> = sqrt(1-m(m+1)/C_S)|m+1>,
    ||U_S||=1.                                         (2)

The shift is zero at the endpoint; it is not a cyclic wrap. Hopping transfers
a record with its charge unchanged to a vacant neighbor and changes E by the
required unit using U_S or U_S^dag. Write T_S for minus the sum of those
unit-coefficient weighted hops. The microscopic Hamiltonian is either

    H_s=Delta N_B+t T_S,
    H_f=(Delta/2)sum_x(div E_x)^2+t T_S.                 (3)

There is no separate bare sum E_e^2 term in (3). On the selected physical
sector the field-star penalty still equals N_(A,-)+N_(B,+), exactly as in
the preceding local-limit note; this identity does not depend on link spin.
Before births the two Hamiltonians agree on the initial-number sector.

One possible formation instrument uses the two resolved opposite-charge pair
jumps, each accompanied by the appropriate U_S or U_S^dag. Their coefficients
are sqrt(beta). The loss per edge is now

    beta P_vac (U_S^dag U_S+U_S U_S^dag)
        = 2 beta P_vac (1-E^2/C_S).                    (4)

Both charge orientations can be available. The earlier spin-half constant
vacant-edge clock must not be imported here. One coherent sum gives the same
loss with a different CP map. Each resolved normalized jump has norm at most
one; the coherent sum has norm at most sqrt(2). They preserve (1) and total
signed charge, and each event adds two records. More generally the local-limit
argument below admits a bounded number of gauge-preserving, number-raising
local jump operators of uniformly bounded norm that annihilate the initial
matter code.

Fix finite positive K and J. Along integer S tending to infinity choose

    epsilon_S^2 = J/[2K C_S],
    h_S=t_S^2/Delta_S=K C_S,
    Delta_S=2K^2 C_S^2/J,
    t_S=sqrt(2) K^(3/2) C_S^(3/2)/sqrt(J),
    beta_S=beta_0 epsilon_S^(2d), beta_0>=0.             (5)

Thus 2t_S^4/Delta_S^3=J, t_S/Delta_S=epsilon_S tends to zero, and h_S/C_S=K.
The link dimension grows like epsilon_S^(-1), Delta like S^4, hopping like S^3,
and the formation coefficient like S^(-2d). These resource scalings are part
of the construction.

The candidate target is the standard compact rotor Hamiltonian on integer
electric fields, with unit shift U|m>=|m+1>,

    H_rot = K sum_e E_e^2 - J sum_p(W_p+W_p^dag),
    div E=0.                                           (6)

In particular the electric coefficient stays nonzero in the joint limit.
Taking S to infinity first at fixed t,Delta would erase that coefficient.

## 2. Complete second- and fourth-order coefficients

Let P be the low matter/ice projector in the fixed initial-number sector.
For an edge in its stored positive-axis orientation, define sigma_e=+1 if
its source is A and sigma_e=-1 otherwise. The allowed A-to-B hop shifts the
stored E by -sigma_e. Its squared amplitude is

    F_e = 1-(E_e^2-sigma_e E_e)/C_S.                    (7)

F_e is nonnegative on the link Hilbert space, including its zero-amplitude
endpoints. Each initial hop costs Delta. All two-hop returns use the same
edge, so the full second-order block is

    H_2 = -(t^2/Delta) sum_e F_e
        = -(t^2/Delta)dV I
                  +[t^2/(Delta C_S)]sum_e E_e^2.      (8)

Here `sum_e sigma_e E_e=sum_(x in A)div E_x=0` on ice. There are dV edges.
Unlike for spin-half links, E^2 is not a constant. Equation (8) is a positive
electric energy generated by virtual record motion, without adding it to (3).

For completeness the canonical orthonormal low block through fourth order is

    H_eff = -(t^2/Delta)sum_e F_e
        +(t^4/Delta^3){
           sum_e F_e^2
             +2 sum_(unordered distinct adjacent e,f) F_e F_f
             -2 sum_p(W_(p,S)+W_(p,S)^dag)}
        +O_V(t^6/Delta^5).                             (9)

The pair sum means that the two edges share one endpoint. The periods exclude
parallel-edge and four-step winding ambiguities. W_(p,S) contains the four
appropriate normalized spin shifts. The remainder is a fixed-volume operator
bound uniform in S, since all hop norms are uniformly bounded and the matter
penalty gap is Delta; a separate local argument appears below.

**Counting including folded normalization.** A second outward hop must use
an edge with different A and B endpoints. Its intermediate energy is 2Delta.
For each unordered disjoint pair e,f, the two outward orders and two return
orders give diagonal contribution `-2 F_e F_f` in fourth-order units. The
normalization/folded term is `(sum_e F_e)^2`: both the second-order excursion
and its squared-denominator partner are the same diagonal sum at unit Delta.
Subtracting disjoint pairs leaves exactly the diagonal expression in (9).
The alternative low endpoint swaps two identical plus records around a
square. Its four paths have denominators 1,2,1 and the same product of four
link amplitudes, giving -2 W_(p,S) and its adjoint. There are no other
four-hop low endpoints under the geometry assumptions.

As U_S approaches the unit rotor shift on finite electric states, every F_e
approaches one. Each edge has 4d-2 adjacent distinct edges. The diagonal
constant in (9) tends to

    c_d V = dV(4d-1).                                  (10)

The nonconstant diagonal corrections are explicitly visible. Put
f_e=(E_e^2-sigma_e E_e)/C_S. After subtracting (10), the diagonal in braces is

    -[2(4d-1)/C_S]sum_e E_e^2
       +sum_e f_e^2+2 sum_(adjacent e,f) f_e f_f.        (11)

These corrections must not be dropped at a fixed small S. They vanish on
finite-electric-field states in the joint limit (5). In physical units the
fourth-order correction to the quadratic coefficient is -J(4d-1)/C_S.

On a single cyclic square the code states are uniform flux m=-S,...,S. The
complete coefficients in dimensionless second/fourth-order units are

    (H_2)_mm = -4+4m^2/C_S,
    (H_4)_mm = 12(1-m^2/C_S)^2-4m^2/C_S^2,
    (H_4)_(m+1,m) = -2[1-m(m+1)/C_S]^2.                (12)

All other off-diagonal elements vanish. This is a local control, not an
allowed d=1 period-four instance of the general torus theorem.

## 3. Conditional uniform local rotor limit

The finite circuit normal-form lemma in the preceding note is an explicit
open dependency pending its independent check. Under that lemma, the following
argument supplies the additional large-spin and unbounded-electric-field steps.

For each finite torus take any ice density rho_0^(S) supported on the spin-S
link intervals and satisfying a uniform per-link fourth-moment bound

    sup_(S,V,e) Tr[rho_0^(S)(1+E_e^2)^2] <= B < infinity. (13)

Correlations and coherences are arbitrary. A common finite-electric-support
family is one sufficient example. Let Y_(epsilon,S) be the local circuit from
that lemma, using n=2d+6 and a fixed structural term decomposition and coloring
across S. Prepare

    rho_(micro,S)(0)=Y^dag(P_m tensor rho_0^(S))Y.       (14)

For every bounded local field operator O_X on rotor links, interpret its
microscopic observable by compression to the spin-S intervals. Then for each
fixed finite T_* there are constants independent of S,V,rho_0^(S) such that

    sup_(0<=tau<=T_*) |
      Tr[O_X rho_(micro,S)(tau)]
        -Tr[O_X exp(-i tau H_rot)rho_0^(S)exp(i tau H_rot)]|
       <= C_(X,T_*,K,J,beta_0,d,B) ||O_X|| epsilon_S.    (15)

The target initial state is the same embedded rho_0^(S); (15) does not assume
that an arbitrary S-dependent family has a limiting state. A thermodynamic
state construction is a further question. Unbounded observables such as E
itself are not included in this operator-norm statement.

### 3.1 Uniform microscopic normal form and birth comparison

Every input hop has norm bounded independently of S. The penalty used in the
normal-form inverse is an onsite integer matter projector, not the electric
energy. Its inverse-on-nonzero-grades integral norm is pi/2 independently of
the link dimension. Consequently all fixed-order generator norms, circuit
ranges, depths, local Taylor constants and parity statements can be chosen
uniformly in S. Coefficient terms are finite sums of words in U_S,U_S^dag and
matter matrices, with scalar coefficients independent of S.

The transformed Hamiltonian is Delta N+D+R with

    ||D||_loc <= C h_S,
    ||R||_loc <= C Delta_S epsilon_S^(n+1).

The finite-range transformed jumps have norm bounded by a constant and satisfy
`||Y j Y^dag P|| <= C epsilon_S`. Thus their full dissipators on a code state,
including no-event terms, have trace norm O(epsilon_S). The previous proof's
polynomial light-cone sum and beta_S in (5) apply unchanged up to constants.
It compares the exact microscopic open dynamics to the closed code block
with local error O(epsilon_S), uniformly in S,V, on fixed time intervals.
The state-dependent loss (4) is allowed; constancy of the vacant-edge clock
was not needed for this comparison.

### 3.2 The code Hamiltonian and its electric extension

After taking the product matter matrix element, the second-order code term
is exactly (8). Remove its scalar. The rest is finite-range bounded field
interactions with local strength O(J), plus terms of order six and higher
with strength O(J epsilon_S^2). There can be a change of fourth-order
Schrieffer-Wolff gauge between (9) and the finite circuit. We do not set it
to zero at finite S: use the actual finite circuit coefficient D_(4,S).

Replace its shifts by unit rotor shifts to define D_(4,infinity). In this
unitary-link limit the second-order block is scalar, so the first non-scalar
fourth-order block is invariant under a near-identity analytic block change.
The counting above therefore gives

    D_(4,infinity)=c_d V I-2 sum_p(W_p+W_p^dag).         (16)

This step avoids importing the scalar-second-order argument into a finite-S
block whose second order is nonconstant.

Embed spin-S link spaces in ell^2(Z). Extend U_S to be zero on transitions
outside [-S,S]. All bounded field words extend to bounded operators with the
same norm control. Extend the second-order term by the exact onsite operator
K sum E_e^2. It agrees with the physical code Hamiltonian on its invariant
finite-S sector. After removing all displayed scalar terms, this extension is

    H_(code,S)=K sum E_e^2+(J/2)[D_(4,S)-c_d V I]
                         +E_(>=6,S),
    ||E_(>=6,S)||_loc <= C J epsilon_S^2.               (17)

All nonscalar interactions other than the onsite electric term have uniformly
bounded norms and ranges. This remains true at the spin cutoff.

### 3.3 Weighted comparison of spin and rotor shifts

For integer m, directly from (2), including both cutoff endpoints and the
exterior extension,

    ||(U_S-U)(1+E^2)^(-1)|| <= 2/C_S,                  (18)

and the same bound holds with adjoints up to another fixed constant.
Inside the interval use `1-sqrt(1-x)<=x` for x in [0,1] and
`|m(m+1)|<=2(1+m^2)`; at and outside the cutoff the right weight is already
of order C_S. Shifting E by any fixed integer changes 1+E^2 by at most a
fixed multiplicative factor. Telescoping any fixed-length field word then
gives, for its difference applied to a density with bounded local fourth
moments, a trace-norm source bound C/C_S. The constant depends on the word
length and moment bound, not the dimension of the local Hilbert space.

This applies term by term to D_(4,S)-D_(4,infinity), because its normal-form
coefficients are the same finite words with different link shifts. It is a
weighted state estimate, not uniform operator-norm convergence of U_S to U.
The latter is false: a cutoff state retains an order-one shift discrepancy.

### 3.4 Moment and locality estimates for the target rotor dynamics

The required moments remain controlled under (6). Put w_e=(1+E_e^2)^2.
The onsite electric Hamiltonian commutes with w_e. A plaquette containing e
changes E_e by one. For either sign,

    w(m+1)/w(m) <= 9,     w(m)/w(m+1) <= 9,
    ||w_e^(-1/2)[w_e,W_p]w_e^(-1/2)|| <= 6.             (19)

There are 2(d-1) plaquettes containing e. The two shift orientations and
weighted Cauchy-Schwarz give the sufficient scalar inequality

    |d Tr[rho_rot(tau) w_e]/d tau|
       <= 24J(d-1) Tr[rho_rot(tau) w_e].                (20)

Hence the moment is bounded by B exp(24J(d-1)T_*). One may first replace
w by min(w,L); its neighboring-value ratio obeys the same bound. The bounded
commutator calculation then holds on the full density domain, and monotone
convergence supplies (20) for finite initial moments. No finite electric
cutoff is assumed during target evolution.

The unbounded onsite term also causes no spatial propagation. In each finite
volume move K sum E^2 into an interaction picture. The remaining finite-range
interactions are bounded and strongly continuous, with time-uniform norms.
Their vector Dyson series converges using the usual factorial bounds. The
finite-range commutator Picard iteration uses only these bounds, disjoint
support commutation and unitary norm preservation; it does not use a finite
local matrix dimension or operator-norm continuity of the onsite conjugation.
It therefore gives the same exponential spatial bound with speed C J for
(17) and (6). This is the needed extension of the finite-dimensional locality
argument, stated here explicitly. It is not attributed to a source theorem
with mismatched hypotheses.

Compare (17) to (6) with the target rotor density on the source side of
Duhamel. Equations (18)-(20) bound a local fourth-order difference source by
C/C_S near the observation cone. Far from that cone use its bounded operator
norm and the locality estimate. Splitting the sum at distance proportional
to J T_*+log C_S gives

    local code-to-rotor error
       <= C_(X,T_*,K,J,d,B) ||O_X||
           [epsilon_S^2+C_S^(-1)(1+log C_S)^d].         (21)

The sixth-and-higher remainder in (17) needs no moment bound and contributes
the first term. Since C_S^(-1)=2K epsilon_S^2/J, (21) is o(epsilon_S).
Add the microscopic comparison of 3.1 and the O(epsilon_S) local observable
change from the preparation circuit. This proves the conditional statement
(15), subject to its named normal-form dependency.

## 4. Complete finite checks

`large_spin_record_electric_ring_check.py` enumerates every allowed plus-record
and electric-field state of a square directly from Gauss. Exact matrix
products, with all intermediate states retained, give (12) at spins
1/2,1,2,3 in physical dimensions 7,13,25,37. The normalized spin-half hopping
amplitude is 2/sqrt(3), so it agrees with the earlier unit-link result after
that explicit hopping normalization; no coefficient is transferred silently.

The same runner diagonalizes the full finite-square microscopic Hamiltonian
at K=.3,J=1 and S=16,32,64,128. Removing the predicted scalar -4h_S+6J,
the largest error of its six lowest energies against the rotor square falls
through approximately .601508, .162376, .0417403, .0105500. Dividing by
epsilon_S^2 gives 98.17,102.88,104.18,104.52. The spin-128 matrix has dimension
1537; the largest reported eigenpair residual is about 1.13e-7. Its ground
state has code weight .9995966. Rotor cutoffs 12 and 24 agree for those six
energies within the declared numerical tolerance. These are converged finite
numerical controls, not exact spectral enclosures or a large-volume simulation.

The weighted-shift, moment and normal-form arguments in section 3 are analytic
obligations; these square spectra cannot substitute for them. No many-body
Coulomb phase or particular long-wavelength state is inferred from the energy
agreement.

`large_spin_live_birth_and_weight_check.py` also constructs the complete live
physical square sectors at S=1,2,3, of dimensions 19,39,59. It checks the
state-dependent loss (4), count increments, annihilation of the initial code,
the exact onsite form of the star potential, and the unit changes of either
penalty under hopping. A separate exact rational screen covers 7,440 shift
inequalities through S=40, and a symbolic quadratic identity verifies the
all-real neighboring-moment inequality used in (19). The general cutoff case
argument remains explicit in section 3, rather than inferred from that screen.

## 5. What this buys and what it still supplies

Within the declared model, electric restoring energy and magnetic loop motion
can share a microscopic hopping origin. The joint scaling prevents the
electric coefficient from disappearing when the link becomes rotor-like,
and the local argument allows formation to remain enabled at every finite
parameter value. A positive limiting production density is not established.

The growing link memory is material. Any unconstrained binary encoding needs
at least ceil(log2(2S+1)) qubits per link; implementing the required spin shifts
and local preparation gates within native lattice interactions is additional
work. A finite spatial circuit depth does not imply bounded native gate cost
as S grows. The checkerboard sector, coherent hopping law, energy/time scales,
state preparation and birth reservoir also remain supplied.

The compact rotor target (6) is a standard lattice gauge theory, not by itself
observed electromagnetism. A Gaussian expansion about small plaquette angles
suggests transverse waves, but establishing a deconfined thermodynamic regime,
its relation to the prepared states, native finite-resource realization, and
the other forces and empirical parameters remains separate work.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** only the model, graph, sector, preparation, observables and order of limits explicitly specified above.
- **N2 — Alternatives:** other instruments, Hamiltonians, states and scaling paths are not excluded.
- **N3 — Imports:** supplied quantum and probabilistic structures are model assumptions; the native axioms do not select them.
- **N4 — Dependencies:** named companion arguments are used within their stated scope; no audit grade is inherited.
- **N5 — Evidence:** exact finite algebra and numerical stability controls corroborate the displayed proofs. Floating spectra and propagations are not interval enclosures. Historical tables are not independently certified by their presence here.
- **N6 — Resolution:** fixed-volume, uniform-volume and ordered-limit statements keep their distinct hypotheses; no exchange of limits is inferred.
- **N7 — Remaining work:** native selection, physical implementation, energy supply, preparation and empirical identification remain separate obligations except for explicitly proved model-specific results.
- **N8 — Authority:** this source applies no audit verdict, retained grade or assembly decision.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary only; it does not derive the supplied model.
- [uniform_local_ring_dynamics_with_slow_record_formation_bounded_theorem_note_2026-09-24](UNIFORM_LOCAL_RING_DYNAMICS_WITH_SLOW_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional argument only within its explicit hypotheses.
- [hardcore_record_motion_generates_gauge_rings_bounded_theorem_note_2026-09-24](HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional argument only within its explicit hypotheses.

Finite-dimensional linear algebra, operator calculus and the explicit inequalities above are mathematical tools. Referenced literature is attribution or context unless its actual assumptions and use are stated in the argument.

## Source and verification

Source PR #8650, frozen head `1ca7b4c2ee69d0840bd9196766e3b77c4251bcc0`. The primary review session uses no subagents; no separate fix reviewer or formal audit is claimed. Original auxiliary packets, failed attempts and historical seals remain recoverable on the original PR branch. The combined receipt records each original path disposition.

```bash
python3 scripts/electric_and_magnetic_dynamics_from_record_motion_2026_09_24.py
```

The canonical wrapper executes the selected scientific controls in a fresh temporary directory, retains their generated result JSON in its stdout, and ends with TOTAL. It does not execute historical sealing or approval instructions.
