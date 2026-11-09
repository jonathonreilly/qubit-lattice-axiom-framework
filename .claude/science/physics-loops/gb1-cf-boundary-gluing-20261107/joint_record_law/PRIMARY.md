# Joint record probabilities without a stored Bell table

Date: 2026-11-09. Claim type: bounded_theorem; actual status:
conditional-support. This is a conditional construction and applicability
test of standard quantum probability, not an axiom-derived Born rule or a
new Bell theorem. Main: 1e0d3b58dcda7f83152b0bb51729260247454d65;
research parent: c7f096b935e85741ac365341ea550a9d465a37d7.

## 1. Three claims that must remain distinct

We obtain a universal operator rule, independent of which four directions a
CHSH experiment later chooses. A supplied spin-zero preparation gives

    p(a,b | n,m) = (1 - a b n.m)/4,     a,b in {-1,+1}, |n|=|m|=1.

The correlations violate CHSH and reach 2sqrt2, but never exceed that bound
within the stated quantum class. No four-setting probability table or fitted
Bell coefficient is supplied. The comparison values were known beforehand;
this is not a blind prediction.

The rule has a local quantum realization with a shared entangled preparation
and separate instruments depending only on their own setting. That is stronger
than merely checking no-signalling marginals, but imports quantum instruments.

It also has an explicit finite record-only realization by ONE atomic joint
formation event. That event is an irreducible coupling of two distant records,
not a sequence of independently sampled neighborhood births. Its physical
formation mechanism, timing and covariance under physical changes of time
slicing are not supplied. The sequential locality test below exposes exactly
why the two realizations cannot simply be identified.

## 2. What replaces a stored table: a probability rule on effects

Supply the finite composite *-algebra M2(C) tensor M2(C)=M4(C), with its
usual positive cone and the two commuting wing embeddings. This composition
and its physical meaning are extra conditions; one-site M2 alone does not
give them. An effect is a Hermitian E with 0<=E<=I.

For a fixed preparation assume one function f from ALL composite effects to
[0,1], with f(I)=1 and

    f(E+F)=f(E)+f(F) whenever E,F>=0 and E+F<=I.

The same effect must have the same probability in every measurement context.
Identifying physical coarse-graining with operator addition is an extra
measurement assumption, not just ordinary additivity of classical events.
In particular, probabilities on four product-measurement menus alone are
not this hypothesis. This hypothesis applies also to entangled effects.

The Busch/CFMR argument then forces f(E)=Tr(rho E). Here is the complete
finite-dimensional step, following Paul Busch's proof. Partial additivity
gives f(0)=0 and rational homogeneity. Positivity implies monotonicity;
rational lower and upper approximations give f(tE)=t f(E) for 0<=t<=1.
For positive A define L(A)=c f(A/c), c>=||A|| and c>0. Homogeneity makes
this independent of c. Scaling A+B into the effect cone proves additivity
on the positive cone. For H=A-B Hermitian, define L(H)=L(A)-L(B). If also
H=A'-B', then A+B'=A'+B, so the definition is independent of decomposition.
It is real-linear. The nondegenerate finite trace pairing gives a unique
Hermitian rho with L(H)=Tr(rho H). Since every rank-one projector is an
effect, <v|rho|v>>=0 for every v; thus rho>=0. Finally Tr rho=f(I)=1.
This is a proof from the added effect hypotheses, not from Record alone.

The [existing Busch bridge](../../../../../docs/BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
contains the same mathematics. Its old claim that tensor composition is
axiom content is not imported. Both that note and the existing native Bell
note are currently unaudited; historical labels supply no authority here.

## 3. Preparation selects a state, not a Bell table

Let sigma_i be the three Pauli matrices and

    J_i=(sigma_i tensor I + I tensor sigma_i)/2,
    Pi_triplet=J^2/2=(3I + sum_i sigma_i tensor sigma_i)/4.

Supply a preparation for which f(Pi_triplet)=0: total spin zero. Pi_triplet
is a rank-three projector. Positivity and Tr(rho Pi_triplet)=0 imply rho
has support in its one-dimensional orthogonal complement: writing
Tr(rho Pi_triplet)=||Pi_triplet sqrt(rho)||_HS^2 proves this directly.
Normalization therefore gives the unique singlet density

    rho_s = |psi_minus><psi_minus|
          = (I - sum_i sigma_i tensor sigma_i)/4,
    |psi_minus>=(|01>-|10>)/sqrt2.

Spin-zero preparation is a resource assumption. Rotational symmetry alone
does not select it: I/4 is also invariant and has zero correlations. More
generally rho_eta=eta rho_s+(1-eta)I/4, 0<=eta<=1, gives E=-eta n.m and
S_max=2sqrt2 eta. This exposes preparation quality as an input, not a fit.

A supplied quantum preparation circuit can create the singlet from the
product |01>: apply H on A, CNOT A->B, then Z on A. These gates occur in the
common preparation region BEFORE settings are chosen. Distribution can also
occur before the choices. Their physical realization and preservation of
coherence are conditions, not a native-law derivation. No detector-to-detector
gate is used after the settings. The [native parity construction](../../../../../docs/NATIVE_PARITY_ENTANGLER_AND_CHSH_NOTE_2026-09-08.md)
is another existing conditional resource route, with its own supplied controls;
its full transitive physical implementation is not assumed solved here.

For local direction n let P_a(n)=(I+a n.sigma)/2. The joint event corresponds
to P_a(n) tensor P_b(m). Pauli traces give

    Tr[rho_s (P_a(n) tensor P_b(m))]=(1-a b n.m)/4.

This one equation applies to all unit directions, not a designated four-row
table. It is nonnegative, sums to one, and gives each local outcome probability
1/2, independently of the other direction. E(n,m)=sum_ab ab p=-n.m.

## 4. Quantum bound and an actual no-communication instrument

For the singlet, the CHSH magnitude is at most

    |m0+m1| + |m0-m1| <= 2sqrt2.

The first inequality is Cauchy-Schwarz after grouping the n0,n1 terms.
The two squared lengths sum to 4; their sum is therefore at most 2sqrt2.
Take n0=z,n1=x,m0=(z+x)/sqrt2,m1=(z-x)/sqrt2. The correlators are
(-1,-1,-1,+1)/sqrt2 and the magnitude is 2sqrt2. Choosing settings to
maximize a derived function is not fitting probabilities to observations.

The bound is universal for the supplied quantum class, not just the singlet.
For self-adjoint dichotomic wing observables with all cross-wing commutators
zero, C=A0(B0+B1)+A1(B0-B1) satisfies

    C^2=4I-[A0,A1][B0,B1].

Each commutator has norm at most 2, so ||C||<=2sqrt2. A normalized positive
state bounds |Tr(rho C)| by that norm. General binary POVMs give Hermitian
contractions. Each contraction A has a local dichotomic dilation
[[A,sqrt(I-A^2)],[sqrt(I-A^2),-A]]; using initialized local ancillas preserves
the correlators and cross-wing commutation, giving the same bound.
No change to the output table can exceed it while retaining these hypotheses.

For the explicit implementation add a fresh local two-state pointer on each
side. The local isometry

    V_n: |v> -> sum_a P_a(n)|v> tensor |a>_pointer

satisfies V_n^dagger V_n=I and extends to a unitary on a local system and
initialized pointer. Alice applies V_n and Bob applies V_m, each to disjoint
systems. There is no input from the opposite setting, no shared post-choice
controller and no message channel in this quantum circuit. Reading each
pointer in its fixed basis gives the displayed joint law. Stabilizing the
pointer as a permanent Record is an additional registration condition.

More explicitly, the local instrument is
I_a^n(tau)=(P_a(n) tensor I) tau (P_a(n) tensor I), with an appended label a.
The B instrument has the corresponding other tensor factor. Their branch
maps commute. Summing over b removes Bob's choice from Alice's record law:
sum_b Tr[I_b^m I_a^n(rho)]=Tr[I_a^n(rho)]. This also holds with passive
references and general trace-preserving local instruments. Thus the local
quantum realization proves more than a no-signalling calculation on one table.
It does not prove that the four record axioms supply those quantum systems,
instruments or local formation mechanisms.

## 5. A literal finite atomic record law on Z3

This separate construction tests compatibility with the stated record
ontology. R, the actual configuration of records, is its entire state.
The density matrix above is law-side probability machinery, not an extra
unrecorded state variable. The prepared source tag below has one fixed meaning.

Choose integer L>=6 and targets c_A=(0,0,0), c_B=(0,0,L). Initially each is
blank. For each target c and its own local direction prepare

    T=100I at c+e1 and c+2e1,
    X(n)=2I+n.sigma at c+e2 and c+2e2.

Prepare the source tag 200I at -4e3 and -5e3. This tag declares the supplied
singlet preparation; its existence is not a proof that a laboratory prepared
one. There are ten initial records and at most twelve after the two outputs.
Include all translations, proper cubic rotations, all n,m and all positive-
probability terminal branches in the supplied domain. Every record is one M2
content. The site count is finite; the continuum of ideal setting contents
does not assert finite precision or a finite information alphabet.

Define a TOTAL one-site kernel F on the complete six recorded neighbor slots,
excluding the candidate site itself. Call X a setting content when N=X-2I
satisfies Tr N=0 and N^2=I. If T is present and exactly one setting content
occurs, let F=(delta_I+delta_minus_I)/2. Otherwise use the empirical measure
of all recorded neighbor contents, counting multiplicities, or delta_0 when
there are none. This is Borel, normalized, spatially covariant, defined on
all M2 contents, and varies with neighborhood conditions. It does not read
the remote setting. The prescribed settings are Hermitian; the total fallback
definition makes no unsupported assumption about arbitrary preexisting maps.

The domain's paired arm pattern identifies both target holes intrinsically:
each arm has two collinear equal contents at distances one and two. The false
diagonal hole between the arms fails that two-step pattern. The separate source
tag and the permitted domain identify this one pair. No preferred origin,
external counter or unrecorded frame is used. A spatial symmetry can exchange
the wings without changing the symmetric singlet law.

At a prepared configuration, ONE transition appends aI at c_A and bI at c_B
with the weight computed by the operator rule in section 3. The next state
contains BOTH outputs. There is no state with exactly one of them. At every
terminal state the kernel is the identity. The pair occurrence and its atomic
character are supplied formation choices, not consequences of F.

Each forming site's marginal is exactly its F=1/2 binary menu. After the
jump its same neighbors still support either output. Every metadata record
retains a same-content buddy; its own neighborhood never contains both T and
a setting content, so its empirical fallback keeps it supported. The source
pair is isolated. Patches do not touch for L>=6. No old content is overwritten,
and no absent site is read. The fixed readout maps I to +1 and -I to -1,
and all other contents to fixed metadata labels. Domain membership, the pair,
settings and terminal condition are functions of R.

This is a complete finite compatible atomic model, conditional on the declared
domain and joint formation law. Its source and setting records are supplied;
preparation genesis and repeated-trial composition are not constructed. It
contains no setting relay but DOES contain a distance-spanning joint coupling.
A global sampler can evaluate it; that sampler is not a local physical
implementation. It cannot be called a proved spacelike record mechanism.

### Why the quantum probability assumption matters

The same initial records, local F and atomic domain also allow the universal
alternative p_h(a,b|n,m)=[1-ab h(n.m)]/4, where h(t)=(3t-t^3)/2. This is
not a table either. Its derivative is 3(1-t^2)/2>=0 on [-1,1], and h(+/-1)
=+/-1, so all probabilities are valid. Both local marginals remain 1/2,
the support is the same, and global rotations preserve n.m. At the four
directions above its CHSH magnitude is 5/sqrt2>2sqrt2. Thus eliminating a
stored table and retaining no-signalling local marginals does not select
the quantum cap. This polynomial alternative has no positive, normalized,
context-independent extension to all the declared M4 effects with these
projector identifications: the operator bound proves that contradiction.
It also has no implementation by the local quantum instruments in section 4.
This is a matching-premise record-law comparison, not a physical prediction
or a construction of a separated classical sampler.

## 6. The decisive sequential test

Suppose instead A has already recorded a and B is still blank, with neither
the setting nor the result from A in B's neighborhood. The Born joint law
requires, for every positive A branch,

    p(b | a,n,m)=(1-a b n.m)/2.

For n=m=z, the two A records a=+1 and a=-1 require respectively b=-1 and b=+1
with certainty. B has the IDENTICAL neighborhood in both configurations.
One F of that neighborhood cannot give both required distributions. In the
explicit kernel above it gives 1/2 in each, which yields the wrong joint law.

This contradiction applies to the sequential extension that requires the
one-site distribution conditional on the FULL current R to be fixed by B's
unchanged neighborhood. It does not follow from no-signalling, whose marginal
averages over the unread remote outcome. Quantum conditioning changes that
full conditional without enabling a message. For general local classical
record mechanisms with independent settings and complete causal accounting,
the previous [Bell test](../foundational_bell/RESULT.md) supplies the CHSH<=2
argument, allowing arbitrarily many neighborhood relays before the choices.

The atomic model avoids the contradiction by never admitting those intermediate
states. Ordinary commuting quantum instruments admit both chronological
orders and give the same final law, but their full-state conditional at the
second event has exactly the dependence above. Therefore their implementation
theorem alone does NOT prove conformance with that sequential reading of F.
Changing F to condition only on a detector's locally available history would
be a substantive additional bridge/interpretation; we do not silently make it.

## 7. What has and has not been achieved

The conditional operator law removes the hand-programmed correlation table
and derives the quantum cap from positivity, composition and effect consistency.
The local quantum circuit removes post-choice messages within its own supplied
quantum model. The twelve-record construction proves that an atomic joint law
can preserve the existing record ontology and local formation marginals.
These are three checked implications with different physical obligations.

The current axioms have not selected effect noncontextuality, composite
positivity, the spin-zero preparation, local quantum instruments or atomic
joint occurrence. No new axiom is adopted. A full native explanation remains
open: justify either the atomic formation law physically, or a consistent
sequential probability/causal bridge that handles the intermediate states
above without hiding remote-setting communication. No framework-wide no-go,
forced axiom amendment, empirical test or mass-gap result is claimed.

All added inputs and alternatives are itemized in [ASSUMPTIONS.md](ASSUMPTIONS.md).
The check evidence and exact source scope are indexed in [HANDOFF.md](HANDOFF.md).
