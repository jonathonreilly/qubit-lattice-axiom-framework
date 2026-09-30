# Original marked rotor process: thermodynamic construction and local energy balance

Constructive discovery theorem candidate, not formal review/audit, retained
status or native-law selection. The contract/source identities are adjacent.
The actual common law, hard-core/integer-rotor carrier, continuous time,
positive K,delta,kappa, Omega and ONE complete original instrument are supplied
inputs. Resolved and coherent alternatives are treated separately throughout.
No microscopic spin-to-rotor error is promoted to a volume-uniform result.

## 1. Result and exact topology

Let H_a=C^2 at A cells. At a B cell let H_b=C^3 tensor the six incoming
l2(Z) rotor factors. For each finite cell set X use A_X=B(H_X), with the
spatial unital embeddings into larger finite regional algebras. Let A_loc
be their union and A its C*-norm closure. This net contains all bounded
operators on a finite region; for infinite-dimensional cells, one must NOT
identify B(H_X) with the norm closure of simple one-site tensors. A normal
finite-region channel extends to larger regions by its spatial normal
amplification. The explicit finite-volume operator construction supplies
these compatible amplifications.

For the original law there is a unique boundary-independent limit T_t(O)
of the canonical finite-volume Heisenberg maps, in OPERATOR NORM for every
O in A_X, uniformly for t in each compact finite time interval. It extends
to a unital completely positive contraction on A. The maps form an algebraic
semigroup. They preserve locally normal states, and the Omega evolution
omega_t=omega_Omega composed with T_t has compatible finite-region density
matrices. Each such density matrix is continuous in trace norm in t.

The semigroup is generally NOT point-norm continuous on A, even on bounded
physical gauge-invariant rotor shifts. No norm-Bochner generator on B(rotor H)
is used. The regularity asserted is finite-region normal-state continuity,
with strong/ultraweak integrals used before the spatial limit.

All local Gauss constraints are preserved. For every finite set F of A
centers, the complete original labels at those centers and their exact
continuous timestamps on [0,T] possess a CP instrument. These instruments
are compatible when more centers are monitored and then forgotten. They
yield a locally finite classical configuration of original marked events
on the countable lattice. Conditioning on events in each finite monitored
region gives compatible locally normal quantum output states. A disintegration
conditioned on the ENTIRE infinite record is not asserted here. There is no
assumed globally ordered first jump or finite global record number.

The limit of the original periodic energy per A center exists and is
finite at every finite time:

    epsilon(t)=lim_(L->infinity) Tr(h_L rho_L(t))/N.

An explicit local energy assignment h_a and finite-range antisymmetric
energy-transfer forms J_(b,a) below obey

    d/dt omega_t(h_a)=omega_t(p_a)+sum_b omega_t(J_(b,a)).

Here p_a is the ORIGINAL full adjoint-dissipator power from center a.
Translation invariance gives epsilon'(t)=omega_t(p_0). Limits of these
unbounded observables use uniform local field moments and uniform
integrability, not trace convergence alone. The separately checked early
power constants give epsilon(t)-epsilon(0)>=61872*kappa*delta*t on their
common positive small-time interval. All later births remain present.

The proof first gives a genuine common-small-time limit with explicit tail
bounds, then constructs all finite times by contraction composition. It
does not postulate thermodynamic existence as an intermediate lemma.

## 2. Prior work, finite approximants and boundary scope

Main and remote main were checked at30a9461ee19a49b99fa6628fe942f08e504e8903.
The complete local-pair source, particularly section4, supplies the local
pair decomposition and identifies the infinite-volume obligations as open:
"These are next questions, not conclusions of (1)." Its preceding paragraph
gives the exact one-step commuting-electric halo, which is retained here.
The complete original local-charge/covariance source supplies a finite-graph
strong-predual/weak-star integral argument and a two-insertion local estimate;
it expressly does not construct an infinite-volume dynamics. The matched
separated-threshold source concerns a bounded infinite pair-configuration
spectral operator, expressly not this full rotor process. Open PR9397 is the
already-read finite-volume autonomous supplier. No separate matching open
thermodynamic proposal was found in the scoped read-only search. This is not
an exhaustive external novelty claim.

Canonical open restrictions retain every complete magnetic pair/jump word
whose full support is contained in the finite region, and each electric term
whose support is contained there. Unused incoming rotor factors may remain
spectators. Nothing clips the internal F hops of a retained magnetic word.
Large even periodic tori use the exact original finite source law. In a
fundamental-domain embedding, a periodic seam can join distant coordinate
faces; its intrinsic graph still has the same local support cardinality and
incidence bounds. Prefixes inside a growing interior ball coincide with the
infinite-lattice prefixes. This is the relevant boundary comparison, not an
assumption that a periodic seam is short in the ambient coordinate embedding.

The same limit holds for finite-volume variants that agree on growing
interior neighborhoods and have uniform support cardinality/incidence and
bounded non-electric local strengths. Their diagonal electric terms must
commute, be self-adjoint, and have a fixed finite support range. For these
variants replace the numerical support/norm constants below by the common
family bounds; the same proof applies. Canonical open and periodic laws
share the numerical constants displayed here. Arbitrary growing-range or
growing-strength boundary forcing is not covered by that variant statement.
For convergence of total open-boundary energy divided by volume, additionally
require the source-form quadratic electric coefficients and initial local
field moments to have uniform bounds; canonical Omega boundaries satisfy this.
Local bulk energy expectations require only the interior source assignment.

## 3. Electric automorphism and the continuity issue

On the A-occupied ambient tensor carrier write

    D=sum_(a->b) d_ab,   d_ab=(1-n_b)E_ab(E_ab-q_a),
    A=sum_(unordered distance-two A pairs) A_ac,
    A_ac=-2delta (F_c F_a P)^*(F_c F_a P),
    h=K D+A,    L_m=sqrt(kappa)B_m.

The local extensions of these complete words preserve every Gauss projector.
One restricts the resulting state to the physical constraints; a global
Gauss projector is not inserted as a nonlocal tensor interaction. All d_ab
strongly commute and are diagonal. Their finite sums are self-adjoint
multiplication operators on their finite-region Hilbert spaces.

For O in A_X define alpha_t(O) by conjugation with the finite sum of electric
terms touching X. All other electric unitaries commute with O and with those
in this finite sum, and cancel exactly. Thus alpha_t(O) is supported in the
one-step halo X^+, has norm||O||, and is consistent under enlargement of X.
The same cancellation proves alpha_t alpha_s=alpha_(t+s), although blindly
applying a geometric halo twice would overcount the support. Alpha_t extends
isometrically to an automorphism of A for each t.

For a local bounded O, t->alpha_t(O) is strong-* continuous on its finite
support Hilbert space. For every trace-class input rho, multiplication by
these uniformly bounded strong-* continuous operators is continuous in
trace norm: prove it first on finite-rank rho and then approximate rho in
trace norm. These statements give strong measurability in the topologies
actually used below, without asserting norm continuity of O's orbit.

An exact source-physical obstruction to norm continuity illustrates the
point. In the all-plus, empty-B sector, put j units of circulation on one
plaquette. This is a finite-support Gauss field and D=4j^2 on that vector.
The gauge-invariant unit circulation W changes its electric energy by8j+4.
For t_j=pi/[K(8j+4)],

    ||alpha_(t_j)(W)-W||=2,       t_j->0.

For each fixed field vector the change tends to0. This is strong continuity,
not norm continuity. The small-time interaction correction below is O(t) in
operator norm for this fixed-support W, so the full interacting T_t also
fails point-norm continuity along this sequence. This is a regularity fact,
not an obstruction to the locally normal dynamics constructed here.

## 4. Finite-volume normal CP maps without norm-Bochner continuity

For a finite region the interaction-picture bounded coefficients are
A_ac^I(t)=alpha_t(A_ac), L_m^I(t)=alpha_t(L_m). Their finite sum acts on trace
class by bounded commutators, gains and losses. It is strongly continuous on
each trace-class input and bounded uniformly on compact time intervals.
Its trace-class Dyson series consists of genuine Bochner integrals in the
trace-class Banach space, where the required strong continuity DOES hold.
Nested integrands are jointly continuous on fixed trace-class inputs by a
bounded-product telescoping argument. The factorial bound proves convergence.

Piecewise-constant time approximations are normal Lindblad propagators.
Their Dyson terms converge on every trace-class input to the above series,
by continuity and domination. Hence the limit is trace preserving and CP;
the same argument after tensoring any finite matrix ancilla proves complete
positivity. Its adjoint is a normal unital CP contraction. Dual integrals
are ultraweak, or equivalently strong operator integrals on individual
vectors for each finite local coefficient. They are NOT asserted to be
Bochner integrals in the operator norm of B(H).

The finite physical dynamics is recovered by the electric conjugation at
the final observable. It is the exact original unbounded finite-volume
GKSL law. Equivalently, h is self-adjoint on Dom D by bounded perturbation,
and the finitely many bounded jump terms give the same unique integral
solution. These finite maps, normally amplified by identities outside their
finite support, are the approximants used in the spatial limit.

## 5. Explicit connected-series locality and norm Cauchy convergence

Here are sharper valid bulk strengths, restated rather than imported as an
unexplained infinite-volume lemma. At o occupied B neighbors, F_a has outgoing
incidence6-o and inverse incidence o+1; the Schur bound gives ||F_a||^2<=12.
A fixed resolved edge has forward count5-o and inverse count o+1, giving
||B_res||^2<=9. Orthogonal final A signs give ||B_coh||^2<=18. For either
complete instrument,

    ||Gamma_a||<=80kappa,
    sum_(marks at a)||L_m||^2<=108kappa,
    ||A_ac||<=288delta.

The first bound follows from Gamma_a=2kappa(5-o)F_a^*F_a; its o=0,...,5
bounds are60,80,72,48,20,0 in units kappa. All bounds hold in every later
sector. Define A_a=(1/2)sum_c A_ac. There are18 partners, so

    ||A_a||<=V:=2592delta.

The interaction-picture center generator on observables is

    G_a(t)(O)=i[A_a^I(t),O]+sum_(m at a)L_m^I(t)^* O L_m^I(t)
                                -(1/2){Gamma_a^I(t),O}.

Its norm and every finite-dimensional amplification norm are at most

    lambda=2V+160kappa=5184delta+160kappa.

The gain CP map has norm||Gamma_a|| and the combined loss has norm at most
||Gamma_a||. Its support U_a lies in B_4(a): A_a is in B_3(a), and the exact
electric conjugation adds only one step. A jump's conjugated support lies
in B_2(a). Crucially, G_a(t)(O)=0 whenever U_a misses supp O. Loss must remain
present for this cancellation; gain alone does not even annihilate I.

The ball B_4 has129 cells. At most129 center labels a have U_a containing a
fixed cell. Start an adjoint string on a set Y of x cells. After j terms its
support has at most x+129j cells. The number of potentially nonzero center
strings of length n is therefore bounded by

    product_(j=0)^(n-1)129(x+129j)
       <=16641^n (q)_n,    q=max{1,ceil(x/129)}.         (1)

Every such nested coefficient has norm<=lambda^n||O||. Its time simplex has
volume t^n/n!. Strong/ultraweak integrals have the same norm bound by testing
unit vectors or trace-class duals; norm measurability of the integrand is not
needed for that inequality. Put

    a=16641lambda,
    R_(q,m)(z)=sum_(n=m+1)^infinity binom(n+q-1,n)z^n,
    tau=1/(2a).

For z<1 the full scalar majorant is(1-z)^(-q). For a physical observable on
X, the initial electric conjugate is supported in X^+, with x<=7|X|. Each
subsequent center term can enlarge the metric radius by at most8, since its
radius-four support must touch the current set. If two finite approximants
agree with the original law throughout B_(8m+1)(X), their coefficients through
order m agree EXACTLY. Their high-order tails therefore satisfy

    ||T_t^Lambda(O)-T_t^Lambda'(O)||
       <=2||O|| R_(q,m)(a t),
    q=max{1,ceil(7|X|/129)},       0<=t<=tau.            (2)

For periodic approximants, the agreement is through the rooted interior lift;
seam terms can only occur after a prefix reaches the seam. Their later tails
still satisfy the cardinality/incidence count(1). Exhaustion shape is irrelevant
provided these interior buffers grow. The same proof with uniform family
constants handles the boundary variants specified in section2.

Equation(2) is uniform over the ENTIRE norm-one ball of A_X and over the common
small-time interval. It proves norm Cauchy convergence of each local observable,
not just convergence of selected matrix elements. For a rational z and a desired
error there is a finite explicit buffer: with n=m+1 and r=z(n+q)/(n+1)<1,

    R_(q,m)(z)<=binom(n+q-1,n)z^n/(1-r).               (3)

The ratio decreases thereafter. This is a usable finite localization resource,
not an unpriced all-volume enumeration.

## 6. CP, locally normal compatibility, all finite times and Gauss

Local norm limits are consistent with the inclusions A_X subset A_Y. Positivity
at every finite matrix level is closed in norm, so the small-time limit is UCP.
It is a contraction and extends to A. Any initial locally normal state omega
restricted to the finite support of a finite approximant is a normal state;
its evolved restriction to A_X is normal. Equation(2), uniformly over||O||<=1,
gives convergence of these restrictions in functional norm, hence in trace norm
of their density matrices. Normal functionals on B(H_X) are norm closed. The
limit is thus locally normal, and its regional densities are compatible under
partial traces. No global density matrix on an infinite tensor product is
asserted. For Omega, use its consistent normal product densities initially.

The limit extends to every finite time without a hidden norm-continuity premise.
For clarity fix T<infinity and choose M with T/M<=tau. For any t<=T put h=t/M.
A finite local observable can be evolved for one slice h and approximated by
a FINITE-VOLUME CP map using(2)-(3), to any chosen norm error eta_1, uniformly
in h. That approximation remains supported on one finite region and has norm
at most the original norm. Repeat for the next slice, choosing a larger finite
region and error eta_2, and so on through M slices. At every step the bound
is uniform over the unit ball of the current finite regional algebra, so it
applies even though that operator depends on h and need not be norm continuous
in h. All choices of regions are finite and can be made uniformly for0<=t<=T.
Contraction bounds the accumulated error by sum_j eta_j.

The same chain approximates the M-fold evolution of every sufficiently large
finite volume. This proves its uniform-in-t norm Cauchy convergence on [0,T].
The limit equals the M-fold small-step limit, and finite-volume semigroup
identities pass to it by contraction and density of A_loc. It is independent
of the subdivision and obeys T_(s+t)=T_s T_t. This gives all finite times;
it is not a claim of a C0 semigroup in C*-norm. Local normality follows by the
same uniform unit-ball argument. Finite-volume density matrices are continuous
in trace norm; their uniform-on-compact local limits inherit that continuity.
No norm compactness of t->alpha_t(O) was used.

The limit satisfies the original local equation on an explicit bounded
test class. For f smooth with compact support in real electric time, set
O_f=integral f(u)alpha_u(O)du using the finite-support strong integral.
This is still supported in X^+, and the L1 translation identity gives the
bounded local electric derivative

    delta_D(O_f)=-integral f'(u)alpha_u(O)du.

Thus L_local^*(O_f)=delta_D(O_f)+sum_a G_a(0)(O_f) is a finite, bounded,
local expression with the ORIGINAL magnetic and jump coefficients. Every
sufficiently large finite volume has exactly this expression. Its exact
weak-predual integrated GKSL identity passes to the limit uniformly on compact
times: for every locally normal initial state omega,

    omega(T_t(O_f))-omega(O_f)
       =integral_0^t omega(T_s(L_local^*(O_f)))ds.

Local normal-state continuity makes the scalar integrand continuous. One can
approximate any local O strongly-* by such electric smearings, but no norm
density or generator derivative on all of B(H_X) is asserted or required.
This identifies the local law in addition to defining its thermodynamic
channel limit; it does not exchange an unbounded generator with a norm limit.

For a vertex v let P_v be the bounded local spectral projection onto

    div E_v=q_v-1_A(v).

Every electric term and every complete magnetic or original jump word commutes
with P_v. Thus T_t^Lambda(P_v)=P_v whenever the fixed constraint is in the
unaltered interior (also for all t). Taking the norm limit gives T_t(P_v)=P_v.
Omega satisfies every P_v, so omega_t(P_v)=1. Products of any finite collection
of these commuting projections also have expectation1. These are compatible
physical Gauss constraints, not a nonexistent infinite total-charge equation.
For periodic embeddings only eventual interior constraints are compared;
no false identification of a seam's external constraint is needed.

Even-sublattice translations intertwine every stabilized local coefficient.
Uniqueness of the limit and the translation-invariant Omega therefore give
translation covariance of the maps and invariance of omega_t. No stationary
state, clustering theorem or global normality is inferred.

## 7. Original finite-region timestamp instruments

Fix a finite set F of A centers. Let M_F contain ALL original marks at those
centers:12|F| resolved labels OR6|F| coherent edge labels. Let J_m(O)=L_m^* O L_m.
The no-M_F-jump finite-volume generator is the full generator with only the
monitored gains sum_(m in M_F)J_m removed. All losses remain. Its propagator
S_t^(F,Lambda) is normal CP and subunital; on states it is trace decreasing.
It includes every unobserved exterior channel and every allowed later birth.
No monitored sign is copied inside a coherent edge record.

The connected proof still applies. The modified center generator has norm
at most lambda: it contains some or none of the gain and the same loss.
Only its monitored-center part fails to annihilate I. Anchor the expansion on

    Y=X^+ union union_(a in F) B_2(a),
    |Y|<=7|X|+25|F|.

Outside this fixed anchor the generators are unital and disjoint terms cancel.
Each insertion at a monitored label also has its interaction-picture support
inside Y. Thus the same count(1) and tail R_(q,m), now with q=ceil(|Y|/129),
construct the infinite-volume no-monitored-jump CP contraction. The all-time
extension works exactly as in section6 with this persistent finite anchor.

For an ordered original-label list m1,...,mn and0<t1<...<tn<T, the finite-volume
Heisenberg instrument density is, in the physical picture,

    S_(t1)^F J_m1 S_(t2-t1)^F ... J_mn S_(T-tn)^F(O).   (4)

This notation is composition from right to left. Each S includes all unobserved
recycling maps and the monitored loss. It is the actual finite source instrument.
For finite-volume time integration use the strong-predual/ultraweak integrals
of section4. Do NOT interpret(4) as a presumed norm-Bochner density on A.

Here is a direct small-time convergence proof for the integrated instruments.
Expand the no-monitored-jump pieces in the electric interaction picture while
keeping all n specified jumps. They have supports inside Y and do not enlarge
the anchor. If l background generator insertions are divided among n+1 time
segments, summing their simplex volumes gives exactly T^l/l!, by the multinomial
identity. The same connected-center bound(1) therefore applies to all background
strings, irrespective of n. Coefficients through l=m stabilize inside B_(8m)(Y).
The difference of two density kernels has norm at most

    2||O|| product_j ||L_mj||^2 R_(q,m)(aT).

This is uniform over ordered timestamps. Define the finite scalar reference
measure nu_F on finite labeled histories by these products times Lebesgue
measure on each ordered simplex, plus the unit atom for no monitored events.
It is only a domination measure, not a replacement Poisson process. With

    r'_F=sum_(m in M_F)||L_m||^2<=108kappa|F|,

its total mass is exp(r'_F T). Thus every Borel history event E obeys

    ||I_E^(F,Lambda)(O)-I_E^(F,Lambda')(O)||
       <=2||O|| nu_F(E) R_(q,m)(aT),     T<=tau.        (5)

This constructs the integrated CP maps by norm limits of actual finite-volume
integrals, without a norm-measurable operator-valued density assumption. The
bound ||I_E^F||<=nu_F(E) proves norm countable additivity in E. The total map
is T_T: pass the finite-volume normalization through the uniformly summable
record-number tail. No gain/loss term is discarded in that passage.

For all finite T, subdivide into intervals <=tau. Use the just-constructed
small-interval instruments and their contraction/localization approximations.
For a fixed finite number of labels, the finite-volume products converge
uniformly in the timestamps by the same finite-region approximation argument
as section6. The global tail in n is uniformly dominated by
sum_(n>n0)(r'_F T)^n/n!, so the limit extends to arbitrary history events.
Finite-volume composition identities make the result independent of the chosen
subdivision. This establishes all finite horizons without a global-jump ansatz.

## 8. Mark compatibility, count bounds and locally normal event states

For F subset F', forgetting labels outside F in the exact finite-volume
instrument gives the F instrument. This identity passes through(5), its
all-time extension and the uniform record-number tails. Time restriction has
the analogous property. After applying omega_Omega, the resulting probabilities
on every finite observed region are consistent. Each regional history space
is standard Borel: a countable disjoint union of finite-label ordered time
simplexes, with the empty history included. The countable-lattice projective
family therefore has a probability measure on its countable product of
one-center history spaces (the ordinary standard-Borel probability extension
theorem). Its hypotheses have now been supplied: positivity, normalization,
countable additivity and all finite-region consistency. This measure theorem
is not a substitute for the preceding quantum construction.

There is an intrinsic local event bound. Let

    Gamma_F=sum_(a in F)Gamma_a,  ||Gamma_F||<=r_F:=80kappa|F|.

In finite volume, integration of the first n monitored events, allowing all
later events after the nth, gives

    Pr[N_F(T)>=n] <= (r_F T)^n/n!,
    E N_F(T) = integral_0^T omega_s(Gamma_F)ds <=r_F T. (6)

The intermediate no-monitored-event pieces are trace contractions, each summed
gain has trace bound r_F, and the final unconditioned propagation preserves
trace. This proves the first inequality directly. Both statements pass to
the spatial limit by the same uniform tails. Hence every finite spatial region
has finitely many marks on every finite time interval almost surely. There is
no explosion locally. No finite global event rate or globally first event is
asserted. Later formation sectors are never truncated by this local bound.

For any E and finite output region X, the positive event functional
omega_Omega composed with I_E^F is dominated by the unconditional omega_T.
Since the latter is normal on B(H_X), the event functional is normal there:
for an increasing bounded positive net its omitted tail is bounded by the
normal unconditional tail. It has a trace-class, positive, subnormalized
regional density matrix. These densities are compatible under partial traces.
For positive-probability E, normalized conditional states are therefore locally
normal; no division by a rare-event probability is used in the convergence
bounds. Original Kraus words commute with the local Gauss projections, so the
same physical constraints hold for these event states. More explicitly,
I_E^F(P_v)=P_v I_E^F(I) on an eventual interior constraint, so its expectation
in Omega equals the event probability. The finite-monitored-region
record/quantum limits retain the original coherent maps, not merely their
diagonal counts. Extending conditional quantum states to almost every entire
infinite history would require an additional measure-valued disintegration;
only the classical history measure and the finite-region quantum instruments
are claimed here.

## 9. Uniform local moments and removal of auxiliary field boxes

Field product boxes are used only to justify unbounded observable estimates.
They are removed at each fixed finite volume BEFORE the thermodynamic limit.
The preceding map construction itself uses the full finite-volume rotors.

For a finite link set S set Q_S=1+sum_(e in S)|E_e|, retaining masked links.
If O shifts Q_S by at most s, its2s+1 integer spectral-difference components
prove

    ||Q_S^u O Q_S^-u||<=b_u(s)||O||,
    b_u(s)=(2s+1)(1+s)^u.

The negative conjugation follows by adjoint. In a finite product box, the
actual compressed jump losses are L_R^*L_R. Applying the adjoint generator to
Q_S^p and sandwiching by Q_S^-p/2 yields the quadratic-form inequality

    L_R^* Q_S^p <= C_p(S) Q_S^p,
    C_p(S)=2b_(p/2)(4)V_S
       +[b_(p/2)(2)^2+b_(p/2)(4)]G_S.                 (7)

Here V_S sums norms of magnetic pairs whose field support meets S; G_S sums
squared jump norms with that property. Disjoint terms cancel, and D commutes
with Q_S exactly after every birth. These constants do not depend on volume
or the product cutoff. If S consists of links ending in a cube of radius r,
explicit overcounts are

    V_S<=18(2r+3)^3*288delta,
    G_S<=(2r+3)^3*108kappa.

Omega has Q_S=1, so finite-box Gronwall gives

    Tr(Q_S^p rho_(Lambda,R)(t))<=exp(C_p(S)t).          (8)

To identify the full unbounded finite-volume law, use W=1+sum_alllinks|E|.
The electric flow commutes with W. Each bounded Hamiltonian/loss insertion has
shift length<=4 and each gain shifts each density leg by<=2. The length-n
interaction-picture density coefficient has both legs within W<=1+4n, and
trace norm at most(C_Lambda T)^n/n! for a finite bounded-perturbation norm
C_Lambda. Multiplying either leg by W^u gives a polynomial factor, still
summable against the factorial at every fixed finite T. Every fixed-order
coefficient stabilizes in the product box once R>=4n+8, including the internal
birth in L_R^*L_R. Dominated convergence gives every needed weighted trace
limit, uniformly on compact times at fixed Lambda. This is the same actual
full-word cutoff mechanism as the checked finite-volume bridge, stated here
with its controlling series. Trace convergence alone is not being substituted.

Thus(8) holds for the full rotor finite volumes. Norm convergence of local
states plus bounded spectral truncations first gives the same moment upper
bounds in the thermodynamic state by monotone convergence. Higher moments
then give uniform integrability and convergence of lower weighted moments.
The order is local cutoff-uniform estimates, fixed-volume cutoff removal,
then thermodynamic local-state convergence with weighted uniform integrability.
No uncontrolled exchange of volume and field cutoff is used.

For explicit use, suppose a local symmetric finite-word operator P satisfies
||P psi||<=C||Q_S^2 psi||. Let P_R^Q be the local spectral projection Q_S<=R.
For any of the states with M4=Tr(Q_S^4 rho) bounded, Cauchy applied to the two
terms in P-P_R^Q P P_R^Q gives

    |Tr(P rho)-Tr(P_R^Q P P_R^Q rho)| <=2 C M4/R^2.    (9)

Indeed the tail probability is <=M4/R^4, while the relevant P^*P forms are
bounded by C^2 Q_S^4, also after sandwiching with P_R^Q. The compressed
observable is bounded. This proves convergence of its actual unbounded-form
expectation from local trace-norm convergence and uniform M4. No self-adjoint
extension of a current is presumed; its finite-word relative form and these
moments define the expectation uniquely. All finite-region fields may be
included in S to make its spectral truncations finite dimensional if desired.

## 10. Local energy balance, transport and density

Assign energy to each A center by

    D_a=sum_(b neighbor a)(1-n_b)E_ab(E_ab-q_a),
    h_a=K D_a + A_a,    A_a=(1/2)sum_c A_ac.

On a periodic torus sum_a h_a=h_L exactly. Its support is in B_3(a), and it
obeys a local Q^2-relative bound. Define the original center dissipator
Diss_a^*(O)=sum_(m at a)L_m^* O L_m-{Gamma_a,O}/2 and

    p_a=Diss_a^*(sum_c h_c),
    J_(b,a)=i[h_b,h_a]+Diss_b^*(h_a)-Diss_a^*(h_b).     (10)

The sum defining p_a is finite: only energy terms meeting the birth star
survive. J_(b,a)=-J_(a,b), and it vanishes when the center separation exceeds6.
These are finite local forms; neither formula subtracts two infinite energies.
Algebraically,

    L^*h_a = p_a+sum_b J_(b,a).                       (11)

The dissipative part of J explicitly accounts for redistribution of the chosen
local energy assignment, in addition to the Hamiltonian transport. P_a is the
actual center source current, not gain without loss or a new observable proxy.

Here are finite sufficient relative bounds showing that (9) applies. Let
G=108kappa, V=2592delta, and V0=264*288delta. The36 electric links and264 pair
terms in p_a give

    ||p_a psi||<=G(316K+2V0)||Q_S^2 psi||=:P0||Q_S^2 psi||.

The number316 is90+1+225 from gain and the two losses, using b2(2)=45 and
b2(4)=225. For a nonzero J_(b,a), choose S containing all links of its radius9
whole-star neighborhood. The two electric/magnetic cross commutators cost
904 K V, the bounded magnetic commutator costs2V^2, and the two dissipative
contributions cost2G(316K+2V). Therefore

    ||J_(b,a)psi||
      <=[904KV+2V^2+2G(316K+2V)]||Q_S^2 psi||.         (12)

To see the first coefficient, D_a<=2Q_S^2 and A_b has bandwidth4, so each
[KD_a,A_b] costs2K(1+b2(4))V=452KV; there are two. The D_a,D_b commutator is
zero even with occupied-B masks. All these estimates survive full-word product
compression. There are at most230 nonzero other A centers within distance6,
so the local sum in(11) is finite with a volume-independent relative bound.

In finite boxes and volumes, integrate the exact finite-matrix identity(11).
Use(8)-(9) and the fixed-volume weighted limit to remove the box, then the
uniform local-state and weighted convergence to remove the volume. Higher
moments ensure uniform integrability on compact time intervals. The local
expectations are continuous there by bounded truncation plus those uniform
tails, so the resulting integrated identity is differentiable:

    d/dt omega_t(h_a)=omega_t(p_a)+sum_b omega_t(J_(b,a)).

Translation invariance and antisymmetry cancel the expectation of the finite
transport sum: displacement b-a pairs with a-b under an even-sublattice
translation. Hence

    epsilon(t):=omega_t(h_a),     epsilon'(t)=omega_t(p_a).          (13)

For periodic volumes, translation invariance gives Tr(h_L rho_L)/N equal to
the local mean exactly, proving the claimed density limit. The normalization
is per A center; per lattice vertex it is epsilon/2. Canonical open restrictions
have only a fixed-thickness boundary discrepancy in their summed assignment;
uniform local moment/energy bounds make it vanish divided by volume along
regular cubes (or any exhaustion with boundary/volume tending to zero).
A full infinite Hamiltonian or finite total energy is not constructed or needed.

## 11. Early positive density gain under the actual full process

The exact landed first-birth source supplies the INITIAL identity

    omega_Omega(p_a)=p0=123744kappa delta,
    epsilon(0)=-618delta.

It is not a claim about only surviving prebirth histories at t>0. The checked
connected-volume argument gives, on the actual full finite-volume ensemble,

    |omega_(L,t)(p_a)-p0|<=240 C_* a t,  a t<=1/2,
    C_*=241920kappa K+12165120kappa delta,
    t0=min{1/(2a),p0/(480 C_* a)}.

For clarity its current cap is
C(s)=5760kappa K(s+2)(s+3)+12165120kappa delta. Apply the connected count with
the conjugated radius-six current support377, and the field-restriction bound
||P_s G_a(t)(O)P_s||<=lambda||P_(s+4)O P_(s+4)||. At order n>=1,
C(4n)<=C_* n^2. The majorant sums to
3z(1+3z)/(1-z)^5<=240z for z<=1/2. Product boxes retain the original source
power for R>=8. This recovers the stated finite-volume estimate with every
later sector and exact loss present. The original855-coefficient initial p0
remains the explicit landed input, not a new enumeration claimed here.

Uniform integrability(9) transfers that estimate to omega_t. Therefore

    epsilon'(t)>=61872kappa delta,
    epsilon(t)-epsilon(0)>=61872kappa delta t,   0<=t<=t0.

No late-time sign is inferred. This is system-energy density within the supplied
model, not heat, work, a reservoir prohibition or an axiom inconsistency.
A supplier consequence would separately need its controller/interaction ledger.

## 12. Executed controls, hypotheses and remaining boundary

The final source-bound standalone check used approximately0.192CPU seconds
and20.0MB (a preceding run also completed below the same resource cap).
It checked144 exact connected-count inequalities, finite geometric tail
certificates,13 timestamp-segment simplex identities, an exact radius-nine
one-step support-envelope expansion,120 original birth Gauss increments, and the physical
plaquette non-norm-continuity counterexample. Omitting loss produces a nonzero
remote identity action60kappa in either original instrument, exposing why
connected cancellation would fail. No full torus or large Hilbert matrix was
formed; the initial30CPU/150MB price and BLAS1 bound were respected.

These are finite discriminators. The all-order scalar majorants, strong-predual
finite maps, normal-state closure, countable instrument additivity, Gauss
identities and uniform integrability carry the theorem's quantifiers. No
numerical extrapolation or norm-continuity assumption supplies them.

At the stated finite-range, supplied-carrier/law, Omega and boundary scope,
this argument leaves no target-equivalent infinite-volume existence lemma
unproved. It requires independent adversarial checking before any source
publication. It does NOT establish point-norm C0 regularity (the counterexample
excludes that stronger claim), an infinite total-energy operator, a globally
normal density matrix, an equilibrium/KMS state, a globally first event,
microscopic finite-qubit approximation uniform in volume, natural preparation,
physical timestamp/energy calibration, autonomous record production, or native
axiom selection. Those are distinct tasks, not tacit premises used here.
