---
claim_id: original_local_charge_current_and_finite_time_covariance_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Bounded original charge current, initial charge covariance and a fixed-local-support finite-time covariance remainder for the supplied common generator and minimum-number preparation; no measured charge or detector identification."
upstream_dependencies:
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
  - formation_balance_and_unsaturated_dark_states_bounded_theorem_note_2026-09-24
runner: scripts/original_local_charge_current_and_finite_time_covariance_2026_09_25.py
---

**Type:** bounded_theorem
**Status:** conditional mathematics with selective independent checks; no retained audit status.

# Original local charge current and finite-time covariance

For the supplied common matter/rotor law and the prescribed all-A-plus,
all-B-empty matter preparation, neighboring cubic-lattice charges obey

    Cov(a,b;t) / Var(b;t) -> -1/6 as t -> 0+, for kappa > 0.

This value is calculated before fitting data. The complete proof below gives
an explicit finite-time error bound, uniform in the electric coupling and
finite volume for fixed local support and fixed bounded-interaction strengths.
The initial field may be any compatible normal state; electric moments and a
selected zero-field input are unnecessary. All original later formation
channels and the common matter/field dynamics remain present.

This is a conditional model consequence. It does not yet identify a measurable
charge, justify the starting preparation, calibrate space or time, or derive a
detector coupling. The bound is conservative: at delta=kappa=1 in model rate
units, the displayed sufficient 1/60 ratio-tolerance window on sides16 and20
is only 5/12223805590224 model time units. This is neither physical seconds
nor the time when the actual model departs from its initial behavior. No
experimental agreement or exclusion is inferred.

Part I derives a bounded current from existing operators, exact charge
continuity, and the original charge covariance slope. Its cubic Fourier slope
is 40 kappa sum_i(1-cos(k_i)) per site. Part II controls finite-time local
covariance without differentiating unbounded electric observables. Its volume
uniformity is for fixed local supports; it does not extend the full Fourier
observable uniformly in volume or construct infinite-volume dynamics.

Both resolved original signs and the stipulated unnormalized coherent sum on
each separately recorded edge are covered. Their diagonal initial charge
statistics agree; their states and later recycling maps need not. The full
vacancy gates, integer Gauss fields and unsigned matter algebra are retained.
No field-only postbirth limit or truncation after a first birth is introduced.

The primary agent personally derived both proofs and decisive controls. Two
separate checkers sealed PRE reconstructions before the respective author
release, followed by POST comparisons. Earlier source exposure is disclosed
in each history; these are scoped checks, not universal claims of blindness.
Root reviewed the complete arguments, new checking code, compact results and
failure records and freshly replayed read-only correspondence. POST46 found
one wording error: zero electric field is sufficient, but not necessary, for
vanishing Hamiltonian-current expectation. That exclusivity was removed in a
separately sealed qualified copy; the original note remains unchanged. POST47
found no required mathematical repair within the stated hypotheses.

Additional PRE results retain their own authorship and scope. PRE46 gives
integrated continuity and other charge/current checks. PRE47 gives a local
colored-series remainder containing a formation factor, with a stated
convergence window; it is not the personally proved all-finite-time estimate
in Part II. Its Pearson coefficient uses sqrt(Var(a) Var(b)), whereas the
quotient above uses Var(b). Their equal initial limits do not equate the two
finite-time observables. In PRE47, charge-diagonal in the relevant integral
proof means a bounded function of matter charges, hence an operator commuting
with D. It does not admit arbitrary field-off-diagonal operators.

The PRE47 finite-dimensional control uses a six-vertex tree with two A and
four B sites, which allows two births. It is different from the historical
three-A/three-B six-site fixture that cannot form a second pair. Neither is
a numerical cubic-torus evolution or a physical preparation.

## Part I: current and initial charge statistics

### Original charge current and initial charge-covariance growth

2026-09-25. Personally derived conditional theorem with separate scoped PRE
and POST checks. No retained audit status or empirical confirmation is claimed.
This targets a bounded charge observable before fitting data. It does not identify
a laboratory preparation, detector, charge unit or lattice/time scale.

Use the three unchanged common-model parents at main60c5f194d940a7bbaf1cdd545296e31d74a02f1a.
Keep h=KD+delta H4, the full vacancy-gated D, H4=-2 sum over unordered
OVERLAPPING A-star pairs S_xy^*S_xy, S_xy=F_yF_xP, and original
L_ab,sigma=sqrt(kappa)Pj_ab,sigma F_aP. The permitted coherent alternative sums
the two signs without normalization at each separately recorded edge. All
integer Gauss fields and unsigned tensor hard-core matter remain present.

The branch identities were previously derived in the personal candidate42.
Their proof is restated below from the three common-model parents; it requires
no additional instrument or physical premise. No root45 result or checker is used.

#### 1. Existing current and exact charge continuity

On the finite physical graph define rho_x=q_x-1_A(x). All rho_x and their
finite test sums R_f=sum_x f_x rho_x are bounded. For link e oriented A to B,
define on the finite q,E basis core the charge current

 J_e = -i[h,E_e]
       -1/2 sum_mu (L_mu^*[E_e,L_mu]+[L_mu^*,E_e]L_mu).

D commutes with E_e. The remaining h and L terms are bounded finite sums of
integer electric translations with bounded matter coefficients. Their
commutators with E_e only multiply each term by its fixed integral shift.
Thus the displayed expression extends to a bounded operator. Its action on P
uses only the original finite local terms involving that link;
it is an expression in existing observables and maps, not a new primitive.
This is minus the formal adjoint-generator action on E_e. It is meaningful as
a bounded current even for normal states lacking an electric first moment.
In that case no time derivative of an undefined mean E_e is asserted.

Every original Hamiltonian term and jump preserves Gauss. On the core,
div E=rho, so L^*rho_x=-sum_e incidence(x,e) J_e. Both sides extend boundedly
and the identity holds on the physical space. It gives

 L^*R_f=sum_(a->b)(f_b-f_a)J_ab,
 L^*sum_x rho_x=0.

The Hamiltonian current and the formation contribution are kept separately
within this one full generator. A nonzero formation count is not net charge
creation. A circulation current can be present without a charge-density change.

#### 2. Initial sector and bounded first derivatives

Supply any normal density in the minimal-number sector N=n=|A|. On P, Gauss
forces all A plus and all B vacant. Its field need not be zero, stationary or
have any electric moment. On this entire sector R_f=0 and h preserves the
sector. Write d_a=|N(a)|. For a mark a->b and outward destination c!=b,

 Delta rho_a=sigma-1, rho_b=-sigma, rho_c=1,
 Delta E=sigma e_ab-e_ac,
 w_f(sigma,c)=f_c-f_a+sigma(f_a-f_b).

The branch injections are isometries into mutually orthogonal matter words
at fixed edge. Hence insertion of a diagonal charge observable between branch
maps gives a scalar times the input-field identity. This remains true for
the coherent sign sum: it does not identify that state with a mixture, but
the present diagonal charge statistics agree. Different edge records are
never coherently added.

For a finite graph, D commutes with R_f and R_f^*R_g. Their Hamiltonian
commutators only use bounded H4 and are bounded. In the interaction picture
of self-adjoint KD, the remaining finite generator is bounded on trace class
and strongly continuous on each trace-class input. A normal state's first
expectation derivative therefore exists by the integral equation and
dominated convergence. No second derivative or uniform norm-continuity of
the conjugated shift operators is assumed.

The initial Hamiltonian and loss anticommutator contributions vanish because
both charge observables annihilate the input sector. The original recycling
term alone gives the initial derivatives below, without turning off any
later channel. At kappa=0 they vanish; no conditioning on a zero-rate mark
is made.

Summing the two signs cancels odd sigma terms. Summing over b and c!=b gives

 d/dt <R_f> at0
   =2 kappa sum_a (d_a-1) sum_(b in N(a)) (f_b-f_a),

 d/dt <R_f^*R_g> at0
   =4 kappa sum_a (d_a-1) sum_(b in N(a))
          conjugate(f_b-f_a) (g_b-g_a).                 (A)

At t=0 every <R_f> is zero, so the same formula gives the derivative of the
connected covariance <R_f^*R_g>-conjugate(<R_f>)<R_g>.
The form on the right is positive semidefinite; constants are in its kernel.
This is the initial covariance slope, not a classical noise process, a
frequency-independent spectrum, a finite-lag correlator or a diffusion law.

For the formation part alone, on this initial sector,

 <J_ab^formation>=2 kappa(d_a-1).

Indeed the sigma link shifts cancel in the sum, and the original outward
hop along ab occurs once for every other mark and both signs, giving
<L_formation^*E_ab>=-2 kappa(d_a-1). A magnetic circulation contribution can
remain for arbitrary field input. For the separately supplied zero-field basis vector, the expectation of
that off-diagonal Hamiltonian current vanishes; it need not vanish for
arbitrary field input. The charge-mean formula (A) needs no such extra field premise.

#### 3. Degree-six cubic Fourier consequence before fitting

On an equal even cubic torus L>=4, let n=L^3/2 and use allowed k_i L in 2pi Z.
For f_x=exp(-ik.x), the six short link lifts give

 d/dt <R_k^*R_k> at0 =80 kappa n sum_i(1-cos(k_i)).     (B)

Normalize by all 2n sites: s(k,t)=<R_k^*R_k>/(2n). Then

 s'(k,0)=40 kappa sum_i(1-cos(k_i)),
 |s'(k,0)-20 kappa |k|^2| <=(5/3) kappa sum_i k_i^4.

The remainder follows from the elementary fourth-order cosine bound and is
geometric, not a continuum dynamical error estimate. The initial covariance
slope is independent of K,delta and the incoming field because R_f annihilates
the entire initial matter sector. Later evolution need not share that independence.

There is a cross-check through the already derived true first-event clock:
rate60 kappa n times the orientation/sign averaged birth structure factor
(4/3)sum_i(1-cos k_i) equals (B). This uses the event only for the derivative;
the direct full-generator derivation above retains every later birth.

The nonzero initial formation link currents point along the oriented bipartite
edges. They do not imply a macroscopic uniform vector current: the six physical
directions at each A cancel. The mean charge redistribution is staggered;
generic long-wavelength Fourier means vanish by lattice translation symmetry.
The covariance grows even where that mean vanishes.

#### 4. Observation obligations

Equation (B) is a conditional charge-density covariance consequence of the
supplied model and initial matter preparation, calculated before any data fit.
It is not yet an observation prediction in SI units. A physical preparation
must justify the minimum-number matter sector; a charge unit, length and time
calibration and a detector coupling must be derived or explicitly supplied.
No charge-density measurement is identified with a photon count or energy
change. An initial slope alone cannot be compared to a measured finite-frequency
noise spectrum without a controlled time/frequency/readout relation.

The next observation task is a controlled local finite-time or finite-lag
charge readout under the full law, with justified physical preparation and
calibration. No experimental exclusion or agreement can be drawn from the
unidentified initial slope alone.

#### 5. Exact controls, chronology and limits

current_noise_controls.py is a new standard-library program. It imports no
earlier author or checker code. It executes the original outward F move and
then j for every primitive mark/destination/sign on the cube, equal L=4,6
cubic tori, a seven-site path and K2,3. The irregular graph bipartition is
specified combinatorially, not inferred from the displayed coordinate labels.
The degree-three cube is never assigned the degree-six Fourier coefficient.
No six-site second-birth calculation is used.

Every complete charge deviation and electric shift is retained sparsely, with
all six integer charge-test values. All 8480 primitive rows satisfy original
Gauss and hard-core constraints. Each fixed edge's primitive matter words are
distinct, so the same diagonal-charge sums apply to the stipulated coherent
edge mark. This verifies a diagonal statistic; it does not equate recycling
maps or quantum states. Field-independence for arbitrary normal input is proved
by the branch-isometry argument, not inferred from testing zero input flux.

The controls check 180 real polarized covariance entries, including the
real/imaginary components of allowed complex Fourier modes, all charge means,
all link formation currents, their divergence and the actual mark norm/rate
factors. The path has degree-one A sites with no formation, which tests the
zero-rate endpoint. On L4 at k=(pi/2,0,0) the full covariance slope is 2560
in units of kappa and the per-site slope is40. On L6 at k=(pi,0,0) the
corresponding values are17280 and80. Constant tests have exactly zero mean
and covariance slope on every graph.

The primary ran once at09:10:37UTC, exit0, empty stderr, elapsed1.856014958s
externally and1.781567500s internally. A separately written root_readonly_check.py
reconstructed every stored geometry, primitive field/charge row, coverage set,
mark norm, current, mean and covariance without importing or executing the
primary. Its fresh run took.462467417s, exit0 and empty stderr; all seven
observed input files were byte/stat unchanged. All five compact result groups
were read completely. Long raw vectors were checked mechanically, not all
manually read. This is personal verification, not independent evidence.

The current/core argument, arbitrary-normal-state first derivative and all
volume/measurement qualifications are analytic proof obligations not replaced
by the finite controls. No second time derivative, finite-frequency spectrum,
finite-spin stopping/derivative transfer, thermodynamic dynamics, macroscopic
current, physical vacuum instability or experimental fit was computed.

There was no failed scientific execution. The original working argument,
complete program snapshots, streams, receipts and read-only check remain
unchanged. Root had already read the independent42 charge checks and other
earlier campaign results before this derivation; no fresh blindness is claimed.
No independent45 argument was read or used. The exact source pins and author
seal distinguish existing supplied premises from the new conditional observable.

## Part II: local finite-time covariance

### Local charge covariance on a finite observation interval

Personally derived conditional theorem47, 2026-09-25. Separate scoped PRE and
POST checks are complete. It extends the branch compression proved in Part I. This is
a finite-graph conditional statement of the supplied common law, not a physical
preparation, detector, calibrated prediction or infinite-volume construction.

Keep every original formation channel and every later number sector. Use
h=KD+delta H4, the vacancy-gated integer electric D, and the unchanged unsigned
matter tensor algebra. No field-only dynamics or one-birth truncation is used.
The common pair-form parent's commuting-electric support observation motivates
the proof below. Prior45 PRE was read before writing this record, but no45
theorem or code is used. No47 checker evidence had been seen at the author seal.

#### 1. Local operators and strengths

Throughout Part II assume a finite simple bipartite graph of maximum degree
at most six. Work on the tensor product with A restricted to its two occupied signs, B to
its three states, and one integer rotor per edge. The original composed P
operators have local extensions on this tensor product: constraints on the
unchanged external A factors act as identities. They preserve the physical
Gauss subspace, so tensor-product norm bounds restrict to it. This is a device
for bounding the original operators, not a new physical space or dynamics.

An atom is a matter site or an edge rotor. A star(a) has a, its B neighbors,
and its incident rotors. For degree6 it has13 atoms. Let C be the bounded
generator consisting of the full magnetic Hamiltonian and formation dissipator,
so the state generator is -i[KD,.]+C. Decompose C into:

* One Hamiltonian commutator per unordered overlapping A pair {a,c}, with
  support star(a) union star(c), at most25 atoms. Its norm on bounded operators
  or trace class is at most5184 delta, since ||F_c F_a||<=36 and the Hamiltonian
  term is -2delta (F_cF_a)^*(F_cF_a).
* One formation dissipator group per A star, including all six edge records
  and both original signs, or the six stipulated unnormalized coherent edge
  sums. Its norm is at most600 kappa. For resolved marks ||B||<=5, giving
  12 times2 times25 kappa. Coherent sign outputs on an edge are orthogonal,
  so ||B_++B_-||<=sqrt(50); six times2 times50 gives the same bound. Recycling
  maps are not identified with each other.

For an atom set X define J(X) as the sum of these local norm bounds for groups
whose support intersects X. For O supported in X, locality gives
||C^*O||<=J(X)||O||. It vanishes for each disjoint group. Let X1(X) be X union
all supports of those intersecting groups. Thus C^*O is supported in X1(X).

Write D=sum_e D_e, D_e=(1-n_b)E_e(E_e-q_a), with support {a,b,e}. These are
strongly commuting diagonal self-adjoint operators. If B has support Y, then
alpha_v(B)=exp(ivKD) B exp(-ivKD) has support in

 Y^D=Y union union_{e: {a,b,e} intersects Y} {a,b,e}.

Only those finitely many diagonal terms enter the conjugation. A disjoint term
commutes both with B and every other diagonal unitary, so no iterative halo is
needed. Its operator norm is unchanged, without assuming norm continuity in v.
Set X2(X)=X1(X)^D.

Consequently for every real s,u and every K,

 ||alpha_u C^* alpha_(s-u) C^* O||
       <= J(X2(X)) J(X) ||O||.                         (1)

These bounds involve all sectors and no electric moment assumption.

#### 2. Two exact integral identities

For each fixed finite graph the bounded perturbation of the self-adjoint KD
evolution gives the trace-preserving CP propagator. In the interaction picture
its generator is C_t=alpha_t C alpha_-t on trace class, and its dual is
C_t^*=alpha_t C^* alpha_-t. It is strongly continuous on each trace-class input
and uniformly bounded for that graph. Let T(t,0) be its state propagator.
Dual integrals may be interpreted weak-star by pairing with trace class;
no Bochner norm continuity of conjugated rotor shifts is required.
The double integrands are jointly weak-star measurable: after pairing with a
normal state, continuity of C_u on trace class and weak-star continuity of
C_s^*O, together with their uniform bounds, justify the iterated integrals.
This also gives the stated scalar norm estimates by duality.

The dual Duhamel equation reads

 T(t,0)^* O = O + integral_0^t T(s,0)^* C_s^* O ds.

For each fixed s insert the same equation for B_s=C_s^*O:

 T(s,0)^* B_s = B_s
       + integral_0^s T(u,0)^* C_u^* B_s du.             (2)

Contractivity of the dual and (1) control the double integral. These identities
are finite-graph identities of the full propagator, not a Dyson truncation
defined by discarding trajectories with later births.

#### 3. Scalar first term for arbitrary normal initial field

Supply an arbitrary normal density in the minimum-number matter sector Pmin:
all A plus, all B empty, any compatible normal rotor field. No electric
moment is imposed. Let R_f=sum_x f_x(q_x-1_A(x)), for a finitely supported test
f. It is bounded, supported in the site set Sf, and commutes with D. Put
b_f=2sum_A|f_x|+sum_B|f_x|, so ||R_f||<=b_f.

For O=R_f or R_f^*R_g, one has O Pmin=0. Candidate46's branch-isometry argument,
restated here, gives a scalar compression of C^*O: for a mark(a,b,sigma) and
outward destination c!=b the original charge increment is

 w_f=f_c-f_a+sigma(f_a-f_b).

Its branch map is a rotor translation with distinct outgoing matter word.
For diagonal charge O all off-diagonal branch matrix elements vanish, including
between the two coherent signs. Summing both signs and all b,c gives

 Pmin C^*R_f Pmin = m_f Pmin,
 m_f=2kappa sum_a(d_a-1)sum_{b~a}(f_b-f_a),

 Pmin C^*(R_f^*R_g) Pmin = N_fg Pmin,
 N_fg=4kappa sum_a(d_a-1)sum_{b~a}conj(f_b-f_a)(g_b-g_a). (3)

The magnetic and loss anticommutator terms vanish in this compression because
O annihilates Pmin and the Hamiltonian preserves it. Pmin commutes with D.
Therefore Pmin C_s^*O Pmin equals exactly the same scalar for every s, despite
the actual prebirth field evolution and arbitrary input electric tails.

Since O commutes with D, its Schrödinger expectation equals its interaction-
picture expectation. Equations(1)-(3) and normality give, with X=Sf union Sg,

 |<R_f^*R_g>_t - t N_fg|
       <= (t^2/2) J(X) J(X2(X)) b_f b_g.                (4)

The one-integral equation also gives
|<R_f>_t|<=t J(Sf)b_f, because its initial expectation is zero. Hence the
connected covariance Cov_fg=<R_f^*R_g>-conj(<R_f>)<R_g> obeys

 |Cov_fg(t)-t N_fg| <= t^2 M_fg,
 M_fg=b_f b_g [J(X)J(X2(X))/2 + J(Sf)J(Sg)].           (5)

This is a finite-time, arbitrary-normal-field remainder, independent of K.
No second time derivative, uniform norm-continuity or electric moments were
used. Coarse M may be large. The initial scalar N is independent of delta and
K; the finite-time bound retains delta through the local magnetic strength.

#### 4. Uniformity of the local estimate and its meaning

At degree at most6, each A has at most30 overlapping partners. An atom lies
in at most6 formation stars and at most180 magnetic-pair supports. Thus
J(X)<=j|X| with j=933120delta+3600kappa. At most186 local groups meet any atom;
each has at most25 atoms. Therefore |X1(X)|<=4651|X|. Each atom belongs to at
most6 D terms of at most3 atoms, so |X2(X)|<=19|X1(X)|<=88369|X|.
These intentionally loose constants prove that (5) can be uniform over finite
volumes for fixed local support and fixed delta,kappa. Exact support counting
should be used for numerical readout windows. The result supplies a bound on
each finite graph; it does not construct or identify an infinite-volume state
or semigroup, prove boundary convergence, or transfer microscopic errors.

A full Fourier test has support proportional to volume, so these local bounds
do not establish a volume-uniform normalized Fourier covariance remainder.
This limitation is not bypassed by dividing (5) by the number of sites.

#### 5. A dimensionless, before-fit local consequence

On a degree6 simple torus, take an adjacent A site a and B site b. Their
relative charges have initial means -60kappa t and +60kappa t, respectively,
to first order. Equation(3) gives

 N_aa=N_bb=120kappa, N_ab=-20kappa.

At any t>0 with t M_bb<120kappa, (5) guarantees a positive Var_b and

 |Cov_ab(t)/Var_b(t)+1/6|
   <= t (M_ab+M_bb/6)/(120kappa-t M_bb).                (6)

This ratio cancels the charge unit and the amplitude kappa in its leading
value. It is calculated before fitting data, for this supplied initial matter
preparation and site-resolved readout. The error bound still depends on model
time and couplings. For kappa=0 its denominator premise fails; no ratio law is
asserted there. Sites not connected by an edge have N_xy=0; this first-order
fact is not permanent absence of correlations.

To compare (6) with observation still requires a justified identification of
the A/B charges with measurable quantities, access to the prescribed preparation
and spatial smearing/readout, and a time interval satisfying the bound in
physical units. No actual detector or natural vacuum has been derived. The
result does not predict photon absorption, heat, a noise spectrum or an observed
particle mass. It closes a particular time-error obligation inside the supplied
model rather than establishing experimental agreement.

#### 6. Exact controls and their limits

The personally authored standard-library local_support_controls.py checks the
support sets and all rational bound arithmetic on sides4,6,8,12,16,20. It runs
no earlier program and simulates no time evolution. The local enumeration is
compared with a separate exhaustive all-A-pair search on sides4,6,8. Complete
sets X1,X2 and both local group lists are saved for A, B and adjacent AB tests.
The initial two-site means and covariance are also checked explicitly.

For sides16 and20, the B test has6 formation groups and93 magnetic groups.
X1 has393 atoms, X2 has741, and the latter meets146 formation and1713 magnetic
groups. On side12 the last magnetic count is1710, so mere agreement of the
support sizes is not enough to assume all counted interactions have stabilized.
On side4, wrapping changes these counts to32 and240; the actual geometry is
used. No infinite-volume convergence theorem is inferred from these samples.

At sides16 and20 the computed conservative covariance constants are

 M_bb=2373055543296 delta^2+40572057600 delta kappa+170640000 kappa^2,
 M_ab=4371220795392 delta^2+75452083200 delta kappa+319680000 kappa^2.

For the purely illustrative delta=kappa=1 in model rate units, the rational
sufficient interval for the error in (6) to be at most1/60 reaches
t=5/12223805590224, approximately4.09038e-13 in the corresponding model time
unit. This is not seconds, a fitted scale, a useful experimental window, or a
claim that the actual dynamics departs from its initial law at that time.
These deliberately loose operator bounds are sufficient rather than optimal.

The primary ran once on2026-09-25 at09:41:24.985561UTC, exit0, empty stderr,
elapsed0.164348542s. Its complete raw output is bound by its execution receipt.
A separately authored root_readonly_check.py then enumerated every global
formation star and every distance-two A pair using closed coordinate offsets
on all six volumes, including36000 magnetic pairs and24000 electric terms
on side20. It rebuilt every saved support set, proved completeness of every
saved local group list by that enumeration, and checked all rational covariance
constants and ratio denominators. It imported or executed no primary code.
The fresh read-only run took0.724004959s, exit0, empty stderr; all eight observed
inputs retained their bytes and file metadata. All six compact result groups
were read completely. Large raw set lists were checked mechanically rather
than all manually read. This is root verification, not independent evidence.

No scientific execution failed. The original working argument, pre-control
copy, programs, snapshots, streams and exact source pins remain preserved.
The integral/domain proof and physical identification obligations are not
replaced by the finite geometric controls. The candidate46 branch compression is proved in Part I and its separate
independent checks have been reviewed. No laboratory
data or observed target was used to obtain the coefficient or the ratio.

#### 7. Remaining observation decisions

The next bridge obligations are a justified physical preparation and local
charge/readout identification, calibrated length/time, and sharper usable
errors if the available measurement interval needs them. A possible further
bound could exploit that all purely magnetic histories preserve the initial
matter sector, to replace the coarse delta-squared error by one containing a
formation factor. That improvement was unproved in the sealed personal author record and is
not part of this personal result. PRE47 separately supplies a colored-series
estimate with its own convergence window; the distinction is recorded above. Fourier-volume control, finite-frequency noise and microscopic
transfer still require separate derivations. Do not promote (6) into a test
of nature until its preparation and measurement dictionary are supplied or
derived and independently assessed.

## Reproduction and next observation obligation

The canonical runner executes exact copies of the two personally sealed
standard-library programs. The first reconstructs 8480 primitive Gauss-law
births and 180 covariance entries on five graphs. The second checks18 local
support sets and exact rational error arithmetic on six cubic sizes. These
are finite exact controls, not numerical finite-time propagation or proofs
of the analytic integral identities. The sealed PRE/POST packets and their
fresh root replay receipts preserve the distinct evidence coverage.

The next bridge requires physical preparation, spatial charge/readout
identification and calibrated time, then a measurement interval with justified
errors. No laboratory data have been fitted or compared in this unit. No
finite-frequency noise, photon absorption, heat, measured mass, natural vacuum,
microscopic joint time transfer or TOE completion follows. This publication
requests review; it requests no merge or audit disposition.

Direct conditional parents:

- [LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24](FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md).
