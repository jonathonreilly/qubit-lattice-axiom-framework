# Local original-record supply: a rotor locality bound and a finite scheduled construction

Author construction, 2026-09-30. Conditional supplied-model mathematics,
not an audit, primitive adoption, or autonomous-source claim.

**Result.** There are two useful constructions. (i) Keeping the entire
commuting electric operator while spatially truncating only magnetic terms
makes an original energy-dressed record operator strictly supported in a
finite neighborhood. Its error relative to the exact spectral lift and its
full-energy defect have explicit, rotor-cutoff-independent support-path bounds.
On the supplied sine battery packet these give finite-horizon marked-process
and mean-energy bounds. (ii) After a product-link field cutoff, fresh finite
positive batteries supply center-local collisions of the actual instrument.
Their gates have fixed spatial radius eight and their accumulated error in the
**full original free-energy ledger** is at most a bounded boundary norm times
the sum of their battery approximation errors. This second construction
approximates the actual binned original process under an explicitly supplied
schedule and initial battery phases. It is a finite resource construction,
not a spatially local autonomous reservoir/controller.

No universal locality obstruction is claimed. Strict spatial truncation does
not preserve exact global energy intertwinement in general; an exact source-word
control below detects that defect. Basic interaction-picture rotor locality
and the analogous CAR local-quench method are prior work, not new results here.

## 1. Sources, carrier and frozen law

Main is e75578f7136401d4bd750131671aed9212c06291. Open PR9345 is read at
fe51bf1728b625dc0133256f43e7783afb11f7d8. The actual supplied law on an even
cubic torus, L>=24 and N=L^3/2 A sites, is

    h=KD+A,  A=delta H4=sum_p A_p,
    A_(a,c)=-2 delta S_ac* S_ac,  S_ac=F_c F_a P,
    D=sum_(a->b) (1-n_b) E_ab(E_ab-q_a),
    B_(a,b,sigma)=P j_(a,b,sigma) F_a P.

Keep every P charge sector and every integer field, with div E=q-1_A and total
charge N. The record algebra is the supplied hard-core tensor algebra, not
fermionic. F_a moves its old charge to an empty neighboring B site and shifts
that link by minus the old charge. j fills the vacated A with sigma and an
empty B with -sigma, shifting its link by sigma. The resolved instrument has
12N original edge/sign labels. The coherent instrument has 6N original
unnormalized sums B_(a,b,+)+B_(a,b,-). Choose one instrument, not their union.
All retained flags below preserve that choice and the complete original gains.

The actual-source Schur bounds are

    ||A_p|| <= J=288 delta,
    ||B_resolved||^2<=9,  ||B_coherent||^2<=18,
    ||Gamma_a||=||kappa sum_(m at a) B_m*B_m||<=80 kappa.

Thus g0:=kappa sum_m ||B_m||^2<=108 kappa N, and the sharper loss bound
sum_a ||Gamma_a||<=g:=80 kappa N is available for collision estimates.
D_e are nonnegative, strongly commuting, finite-support multiplication
operators. h is selfadjoint on D(D), with bounded magnetic perturbation.

Use the PR9345 tensor placement: an A charge occupies its site; each B site
contains its charge and all six incident integer links. An original B_m is
supported on the star X_a of radius one. Electric conjugation enlarges a star
to S_a={x:|x-a|_1<=2}. A magnetic pair dressed by D has support S_a union S_c,
|a-c|_1=2, hence diameter at most six. Every such pair has at most 2076
intersecting dressed pairs: 85 even centers lie in a radius-four ball and 1038
unordered distance-two A pairs have at least one endpoint there. The same
counts for one S_a are 1038. These exact geometric overcounts are rechecked.

Imports remain the actual quantum carrier, K,delta,kappa, law, preparation,
readout and compensator. The minimal axioms and approved primitive registry
do not select them. Full source and prior-work distinctions are in SOURCES.md.

## 2. Retain all electric terms; the local spectral lift then has bounded defect

Fix a center a. Let I_r contain every magnetic pair with at least one endpoint
within lattice distance r of a, and A_r=sum_(p in I_r) A_p. Put

    h_r=KD+A_r,                         B_(m,r)(tau)=exp(-i tau h_r) B_m exp(i tau h_r).

Although h_r contains the global D, its action on B_m is exactly local.
Let S be the union of X_a and the ORIGINAL supports of pairs in I_r.
Every D_e disjoint from S commutes with B_m, with A_r, and with every other
D_f. It therefore commutes with h_r and cancels from the conjugation. Only
D_e meeting S need be retained in a finite local Hamiltonian h_loc,r.
The support of B_(m,r)(tau), for every tau and every integer field, is contained
in S^+, the one-step enlargement of S. It lies in the radius-(r+4) ball.
There is no iteration of electric neighborhoods. This proves support directly;
it is not a finite-field inference.

Use battery energy E_B=-i d/dtau in Fourier convention exp(+i tau E), and
let V_(m,r) be multiplication by B_(m,r)(tau). The exact spectral lift V_m
instead uses full h. Strong unitary-group intertwining gives

    [h_r+E_B,V_(m,r)]=0,
    [h+E_B,V_(m,r)]=[A-A_r,B_(m,r)(tau)]=:D_(m,r)(tau).       (2.1)

The first identity is strong energy intertwinement; it does not assume that
an arbitrary bounded B preserves D(h_r). The second is a bounded commutator:
omitted electric terms cancel exactly. Among omitted magnetic terms, only
those whose original supports meet S^+ contribute. Call this finite set
partial I_r. Every such pair has an endpoint at distance r+1,...,r+5 from a.
Since an A center has 18 distance-two A partners,

    M_r:=|partial I_r| <= 90[4(r+5)^2+2].                    (2.2)

This uses the integer cubic sphere count 4s^2+2 and overcounts orientations.
It also holds on the torus by shortest-displacement counting; if the region
covers the torus the boundary set is empty and the defect is exactly zero.

Dropping arbitrary electric boundary terms instead would leave unbounded
commutators. The exact source control obtains

    ||[D,A_pair/delta] |circulation n>||^2 =512 n^2+128,

on two actual complete overlapping cubic stars. There is no field-independent
operator-norm bound for that alternative difference.

## 3. An explicit support-path bound for the actual rotor operators

Here delta>0; if delta=0, sufficiently enlarged electric dressing is already
exact. Define

    Z=2076,  q=2JZ=1195776 delta,
    T_d(x)=sum_(n>=d) x^n/n!,
    d_r=floor((r-8)/6),   r>=14.

Use the larger exact boundary count if known, or (2.2). Then for u>=0,

    epsilon_r(u)=min{2, (M_r/Z) T_(d_r+1)(q u)},
    gamma_r(u)=2J M_r min{1,T_(d_r)(q u)}.                    (3.1)

For b_m=||B_m||,

    ||B_m(tau)-B_(m,r)(tau)|| <= b_m epsilon_r(|tau|),
    ||D_(m,r)(tau)||          <= b_m gamma_r(|tau|).          (3.2)

Here B_m(tau)=exp(-i tau h)B_m exp(i tau h). These bounds hold on the entire
supplied tensor space, hence on its invariant Gauss sector, without a field
or energy cutoff.

For completeness, the bounded support-path proof has the following explicit
constants. In the D interaction picture every magnetic term has norm <=J and
fixed support S_u union S_v. Remove the homogeneous local commutator in the
usual Jacobi integral recursion. The norm-preserving propagator then bounds a
commutator of an evolved B_X with a probe C_Y by a sum over ordered overlapping
interaction supports. A path of n supports contributes at most

    2 ||B_X|| ||C_Y|| (2J|t|)^n/n!.

There are at most 1038*Z^(n-1)<=Z^n paths starting at the seed S_a, before
requiring the last support to meet Y. An omitted dressed pair lies at least
r-4 from S_a. Since each traversed support has diameter at most six, a path
with fewer than d_r terms cannot reach it. Dropping further endpoint
restrictions gives 2||B||||C|| T_(d_r)(q|t|); the trivial commutator bound
clips the tail at one. Sum C=A_p over partial I_r to obtain the second bound.
Duhamel comparison of h and h_r integrates that commutator and uses
integral_0^u T_d(qs) ds=T_(d+1)(qu)/q, proving the first. Negative times obey
the same estimates.

The coefficients are strongly continuous with strongly continuous adjoints,
not necessarily norm continuous. To justify this recursion on rotors, freeze
them on a time mesh. All estimates above hold for each bounded piecewise
constant propagator and are independent of mesh and local dimension. For
fixed finite volume, strong coefficient convergence gives trace-norm
convergence on rank-one operators and then all trace class by finite-rank
density. A finite-net argument on the compact exact trajectory plus Duhamel
gives convergence of the propagators. Their duals converge ultraweakly; the
operator norm estimates pass by weak-star lower semicontinuity. This is the
actual topology repair already supplied by the landed Sept24 locality source,
now with explicit pair-only path constants. No unbounded-Hamiltonian LR
theorem with unverified hypotheses is invoked.

## 4. Prepared-battery process and energy bounds, with the phase-flow distinction

This paragraph concerns full-line E_B, not a positive cap. Prepare the
normalized sine packet on [E0,E0+w]. Its Fourier density p0 has, for
U>=sqrt(2) pi/w,

    eta(U):=integral_(|tau|>U) p0(tau) dtau <=32pi/(3w^3 U^3).

Consider the complete GKSL law on system, this one shared battery, and the
original marked history, with free Hamiltonian Q=h+E_B and jumps
sqrt(kappa) V_m, or their local approximants sqrt(kappa) V_(m,r).
Pointwise trace cancellation of every multiplier dissipator gives the exact
UNCONDITIONAL marginal p_t(tau)=p0(tau-t), even after correlations form.
A selected trajectory need not have that marginal.

Along the exact reference, the joint Hilbert-Schmidt error of each jump is
bounded by b_m[epsilon_r(U+T)+2 sqrt(eta(U))]. Gain telescoping and the two
loss terms bound the generator difference by four times this expression
weighted by kappa b_m^2. CPTP Duhamel, including the unchanged mark-append
registers, therefore yields the complete marked-output trace-norm bound

    err_local(T) <=min{2,4g0 T[epsilon_r(U+T)+2sqrt(eta(U))]}. (4.1)

This is a prepared-battery bound, uniform over system/reference inputs. It is
not operator-norm quasi-locality on arbitrary battery inputs: arbitrary phase
translations of the packet can place its Fourier mass arbitrarily far away.

For a finite-second-Q-moment input, (2.1) is a bounded commutator and the
usual quadratic-form energy derivative is justified by domain approximation.
Indeed bounded [Q,V] controls the Q graph norm under jumps; the finite-rate
Dyson expansion propagates that domain on every finite time interval.
The dissipative energy current is

    sum_m kappa (V_(m,r)* D_(m,r)+D_(m,r)* V_(m,r))/2.

It has fiber norm at most g0 gamma_r(|tau|). Hence the actual local full-line
law obeys

    |<Q>_T-<Q>_0| <=g0 T[gamma_r(U+T)+2J M_r eta(U)].        (4.2)

The exact untruncated lift conserves the entire Q distribution. Spatial
truncation generally gives (4.2), not exact conservation. For example choose
U=d_r/(2 e q)-T when positive and above the packet threshold. Then
T_(d_r)(q(U+T))<=2*2^(-d_r), so the central terms decay exponentially; the
energy tail is O(M_r/U^3)=O(r^-1) at fixed w,T, and the trace tail is O(r^-3/2).
These are loose sufficient bounds, with a very large supplied propagation
constant. On a fixed finite torus reaching full support also makes the spatial
error zero. For increasing volumes the energy bound per A site is uniform;
no infinite-volume global energy operator is being defined.

**The reference in (4.1) is not automatically the original ongoing process.**
Its exact diagonal fiber equation is

    (partial_t+partial_tau) rho_t(tau)
       =-i[h,rho_t(tau)]+kappa sum_m D[B_m(tau)]rho_t(tau).

Set sigma_t(tau)=exp(i tau h)rho_t(tau)exp(-i tau h). Along tau=tau0+t,

    d sigma/dt = kappa sum_m D[B_m]sigma.                   (4.3)

The free matter commutator cancels the derivative of the phase gauge. At an
ideal sharp initial phase zero the resulting map is
Ad(exp(-ith)) composed with exp(t kappa sum D[B_m]), generally different from
exp(t[-i ad_h+kappa sum D[B_m]]). The actual original single-mark covariance
witness in the independently checked supplier packet already detects the
required failure of energy-frequency covariance. The small exact finite
fixture here merely checks the sign and the second-order difference; it does
not replace that source witness.

Replacing every fiber by B_m(tau-t) repairs this algebraically: the co-moving
phase is constant, and each phase fiber carries the original marked generator
conjugated by exp(-i tau0 h). The instantaneous full-energy intertwinement also
survives. This is an explicitly time-programmed law, however. Its time/phase
reference must be supplied; no battery reset or rephasing is free. In its
spatial comparison (4.1)-(4.2), U replaces U+T. This distinction does not apply
to the landed finite-grid autonomous theorem, which already includes its
own interaction-picture history program. It rules out an unjustified reuse
of the unprogrammed full-line lift as that theorem's substitute.

## 5. A fixed-range finite positive supply under a declared schedule

A different construction supplies the actual original process without needing
an unprogrammed shared full-line battery. Its price is a finite fresh battery
for every center collision, a supplied schedule, and supplied initial phases.

### 5.1 Product cutoff preserves local operators

Let P_R^box restrict each link separately to |E|<=R. Compress each local
magnetic term and B_m on those tensor factors and use the resulting loss
sum B_m,R*B_m,R. Never substitute P_R Gamma P_R. The diagonal D and local
Gauss/charge constraints commute with this product projection. Thus this
finite model retains the original interior words, coherent sums and labels,
and retains local tensor supports. It has dimension at most

    d_sys <=6^N(2R+1)^(6N).

The independently checked rotor-process bridge used a radial field cutoff.
Its same proof applies to this product cutoff: it contains every word with
Q_field:=1+sum|E|<=R, a jump changes that weight by at most two, and a magnetic
or loss insertion changes it by at most four. Projections still commute with
Q_field. Hence the exact history coefficients agree whenever 4n+2j<=R;
the weighted tail and boundary estimates of that bridge hold unchanged.
This does not infer convergence from finite dimension. The entire unchanged
weighted-word proof, including later births and the bound j<=N/2, is used.
Unlike the radial cutoff, the product cutoff preserves local tensor factors.
For explicit choice of R, retain the predecessor's conservative constants
G_w=300kappa N, a_w=v+G_w/2, M=N/2, b=1+2M, x=a_w T, y=G_w T and
b_M(y)=(sum_(j=0)^M y^j/j!)^(1/2). Choose an integer ell>=0 and

    R=2M+4ell+8,
    Y_p=b_M(y) sum_(n>=ell+1) (b+4n)^p x^n/n!,
    X_p=b_M(y) sum_(n>=0) (b+4n)^p x^n/n!.

Then eta_rot<=min(2,4Y_0), E_rot=4(2KX_2+v)Y_0, and the other three
energy/current errors are exactly (17)-(18) in the accepted bridge, with G_w
in its current constants. These tails vanish at fixed N,T as ell grows.
They remain valid uniformly for passive history reads at fixed grid times;
arbitrary energy-injecting interventions are not covered.
Its finite norm bound may safely be taken as

    v=2592 delta N, Qmax=1+6NR,
    0<=h_R+vI,  ||h_R+vI||<=hbar=2K Qmax^2+2v.             (5.1)

The accepted bridge's error quantities eta_rot, E_rot (energy mean), E_rot,2,
and current-moment errors are carried with this larger finite norm when
composing apparatus errors. This product-cut extension is new author work
here; the earlier independent check did not separately check these paragraphs.

### 5.2 Original center collisions and marked approximation

At each center a, with tau*80kappa<=1/2, form the local column

    K_(a,0)=sqrt(I-tau Gamma_a),
    K_(a,m)=sqrt(tau kappa) B_(a,m,R).

It is an isometry into a blank local mark flag of dimension 13 (resolved) or
7 (coherent). Complete it to a unitary U_a on that star and flag. Its extension
on other flag inputs is supplied, but it is local and input-independent.
Gauss constraints can be preserved by completing separately in their joint
blocks, since every column intertwines those local diagonal constraints.

One bin applies all N center collisions in a fixed declared order, then free
exp(-i tau h_R); all marks are retained in their order within that bin. With
n=T/tau bins, m=Nn collisions, the comparison with the exact original binned
history satisfies

    err_sweep <=T tau c,  c=7g^2+4hbar g,  g=80kappa N.     (5.2)

One may prove this on the history-appending space. A single center's collision
remainder is <=7tau^2 g_a^2. The Lie product splitting contributes at most
4tau^2 sum_(a<b) g_a g_b, and free-Hamiltonian splitting at most
4tau^2 hbar g. These fit inside (5.2). This argument includes actual zero,
one, and multiple-event maps and later births; there is no scalar Poisson
replacement. Exact continuous timestamps are coarsened to bins, as in the
landed grid theorem. Normalized rare-event errors are not bounded uniformly.

### 5.3 Local finite batteries and the full-energy ledger

For each U_a choose r=4 in section 2. Then S^+ has at most 833 site factors
and radius eight. Define its finite h_loc using all retained magnetic terms
and all electric terms touching their original support. Both U_a and this
Hamiltonian act in that neighborhood. Apply the landed finite energy-supply
block construction to U_a with this h_loc and a FRESH finite battery.
If h_loc has s distinct positive excitation energies E_i above its ground,

    s<=d_loc-1, d_loc <=[3(2R+1)^6]^833,
    H_bat=sum_(i=1)^s E_i N_i,   N_i=0,...,L_b+1,
    dim(battery)=(L_b+2)^s,
    <H_bat>_initial=(L_b+1)/2 sum_i E_i,
    eta_b<=4pi/(L_b+1).                                  (5.3)

These E_i are excitation energies from the ground, not all pairwise Bohr
energy differences. Degenerate and incommensurate energies are allowed.
The implemented full finite unitary V_a exactly conserves h_loc+H_bat and
approximates U_a on arbitrary system/reference inputs with the fixed sine
product battery, retaining the battery and original flag in the output, by
trace norm <=eta_b. There is no cap refusal or wrapped shift. Incomplete
joint energy-label blocks receive the identity unitary.

There is also an explicit energy ceiling. The local spectral width is bounded
by W_loc=6*833 K R(R+1)+2J*1038; hence sum_i E_i<=s W_loc and the maximum
battery energy is at most (L_b+1)s W_loc. These are finite symbolic resources;
no matrix of dimension d_loc has been computed or hidden in a claimed run.

Let A_partial be the omitted magnetic terms meeting S^+. Omitted electric
terms commute strongly with h_loc and U_a, hence with V_a's entire spectral
block construction. Other omitted magnetic terms are disjoint from V_a.
Furthermore [A_partial,U_a]=0, because every magnetic pair meeting the bare
star was retained. Therefore on every input with this fresh battery,

    |Delta <h_R+sum H_bat>| = |Delta <A_partial>|
       <=B_partial eta_b,
    B_partial=J M_4 <=8449920 delta.                       (5.4)

The equality uses exact local conservation; the inequality compares V_a's
joint output to U_a's and uses ||A_partial||<=B_partial. This is why an
unbounded omitted electric operator cannot be tolerated in the construction.
It is also why no large ||D|| appears in (5.4). It does NOT assert a small
unrestricted commutator norm on arbitrary battery inputs or exact conservation
of the full global energy distribution.

A fresh battery remains product with the current system even when the system
is correlated with earlier, retained batteries. Thus the fixed-input theorem
applies at every gate without resetting anything. Free evolution preserves
the full free energy. At the scheduled gate time t_j, use the packet beta_j
whose initial phase is exp(+i H_bat,j t_j) beta_sine. Its own free evolution
then brings it to beta_sine at that gate. All these phases and the schedule are
explicit supplied preparation/control data; their selection is not derived,
and their precision has not been declared free. Old batteries and mark flags
are retained, not recycled or silently reset.

The complete scheduled process and mean ledger obey

    nu:=m eta_b+T tau c,
    err(original binned process)<=eta_rot+nu,
    |Delta <h_R+sum H_bat>|<=m B_partial eta_b.             (5.5)

The error in mean energy drawn from these batteries relative to the original
unbounded process is at most

    E_rot+hbar nu+m B_partial eta_b.                       (5.6)

Its target is the original process's energy increase, equivalently its
integrated source-current mean where the accepted bridge justifies that
identity. At grid times the original energy and source-current first/second
moment comparisons add hbar nu,hbar^2 nu,pbar nu,pbar^2 nu to the accepted
rotor errors, with pbar=300 kappa N[316K Qmax^2+2v], a conservative product-cut
current bound from the same field-word estimate. Equation (5.6) does not
identify a microscopic instantaneous battery current with that source current,
or establish a work-distribution/second-work-moment equality.

For a desired apparatus trace tolerance eps and mean-ledger tolerance eps_E,
choose n with n>=2Tg and T^2 c/n<=eps/2, then choose

    eta_b<=min{eps/(2m), eps_E/(m B_partial)},
    L_b+1>=4pi/eta_b.                                    (5.7)

This explicitly prices m fresh coherent batteries and m blank original-mark
flags. Larger rotor R chosen from the accepted bridge prices the unbounded
model approximation. An independently checked finite-cut R=100 example in
results.json gives finite, very large n and L_b; it makes no claim that R=100
approximates the full rotor law. This illustrates apparatus inequalities,
not efficient resources or a physical source selected by the axioms.

## 6. What is and is not implemented in time

Section 5 is a finite sequence of finite-support unitary operations under a
supplied external schedule. All neighborhoods have fixed radius eight; the
original free h_R is itself finite range. This is more local than the full
system spectral battery lift, but the local spectral gates may be arbitrary
many-body operations within those 833 factors. Nearest-neighbor synthesis,
controller locality, preparation machinery, irreversible flag permanence and
controller energy are not absorbed into (5.3).

Finite pulse strengths can be priced for the declared scheduled circuit,
without asserting an autonomous implementation. For each V_j take a local
Hermitian logarithm G_j with exp(-iG_j)=V_j and ||G_j||<=pi. A pulse of duration
s driven by G_j/s has coupling <=pi/s. Put
E_*:=hbar+sum_j (L_b+1)s_j W_loc, an upper bound on positive Q_free. Duhamel and
a triangle inequality give

    ||exp[-is(Q_free+G_j/s)]-exp(-isQ_free)V_j||<=2s E_*.

Thus m actual pulses differ from ideal instantaneous gates followed by their
full free waits by joint trace norm <=4ms E_*. Set each bin's remaining free
wait to tau-Ns, requiring Ns<=tau. The actual physical horizon is exactly T.
In the ideal comparator every battery still experiences the full elapsed free
time, so the initial phase prescription in section 5.3 remains valid at every
pulse start. After the m eta_b hybrid replaces lifted gates by their bare U_j,
battery free evolution commutes with those bare gates. Moving all system free
segments to the end of each bin costs at most 4ms hbar: remove those segments
and reinsert their combined length, using unitary telescoping. Consequently
an additional 4ms(E_*+hbar) bounds the process error at the unchanged bin
boundaries. Ledger comparison to the ideal lifted schedule costs at most
4ms E_*^2 in endpoint energy; that ideal schedule still obeys (5.4) at each
gate and preserves Q_free in every free interval. Choosing a smaller positive
s makes these errors arbitrarily small with finite coupling pi/s. A scalar
shift of each G_j changes only phase and can make each pulse Hamiltonian
positive. This explicit but very loose pulse construction still uses external
switching and phase preparation; its controller's energy is not included.

An existing finite-grid history clock can globally program finite operations,
but its clock-to-payload interactions have not been shown geometrically local
when these separated center gates are used. Quoting it would not close this
residual. An actual spatial autonomous supplier must transport timing/control
information and account for its coherent energy, fresh preparation and readout.
That is a **target-equivalent missing construction**, not a small omitted
technical estimate. Exact global energy intertwinement for strictly local gates
is likewise not obtained by (5.4); only its stated state-class mean defect is.
The LR construction in sections 2-4 supplies a separate controlled tail route,
not a proof that this final autonomous step is impossible.

## 7. Executed controls and frozen scope

The standard-library control job was run with maximum one concurrent job.
The first successful run took 1.03 seconds; the final run adding the explicit
coherent-sum control took 27.05 seconds of wall time, exceeding the estimated
15-second budget. No further compute job was launched. BLAS/OpenMP threads were capped at one.
No torus Hilbert matrix or apparatus matrix was built. Six groups pass:

* Exact overlap inventory 85,1038,2076 and support/boundary counts at r=2,4,6.
  At r=4 there are 1038 retained pairs, 833 support sites and 4284 actually
  intersecting omitted pairs, below the conservative 29340 boundary bound.
* Literal unsigned F,j source words on two FULL degree-six cubic stars:
  [A_pair/delta,B_minus]Omega has 140 nonzero words and norm squared 16984;
  the plus case has 75 words and norm squared 10808; the original coherent
  sum has 215 words and norm squared 27792. A local energy lift
  omitting this live pair does not exactly conserve global energy.
* Actual Gauss-compatible circulation words n=1,2,3,10 verify the electric
  commutator formula 512n^2+128, detecting an unbounded naive boundary.
* A separately labelled two-level exact rational fixture checks (4.3)'s
  product-versus-simultaneous-generator discrepancy at second order.
* Exact rational integer-resource inequalities for a finite-cut apparatus.
* Source/scope controls retain actual sign coherence and original support;
  no CAR, oscillator, first-event-only or scalar-rate substitute is used.

The first attempt at the small phase-flow fixture chose an input for which
that particular second-order commutator vanished. Its assertion failed before
any result artifact was written. The corrected positive density |0><0| detects
the intended nonzero coefficient; the source-word controls were unchanged.
The final successful run supersedes the earlier output and is preserved; this
is not an independent check of the new
analytic lemmas. Parent is expected to arrange that before reuse.

Frozen conclusions: explicit actual-rotor dressed-operation locality and energy
defect; prepared-battery marked comparison of the stated full-line laws; a
finite fixed-range scheduled original-process supplier with all fresh batteries
and flags priced; exact identification of the uncontrolled phase-flow issue.
The external control and final local autonomous source remain unresolved.
