# HOLEPAY — differentiated charges for holes and the remaining matched estimate

**The actual all-history payment in EXTCONT E15 remains OPEN.** A smooth
factor of the original Wilson density pays arbitrary one-step merged holes
with an explicit six-field-derivative bound below. This is a raw allocation,
not yet a bound for an integrated, normalized history activity. The precise
missing inequality is HP14. Boundary estimates are debits against that
allocation; placing a hole weight in a norm moves the required estimate into
the input hypothesis. Neither operation supplies new probability mass.

| Result | Status and scope |
|---|---|
| HP1–HP3 | **PROVEN:** sharper full-root transfer and composition of fixed-mask saturation, for supplied jets. |
| HP4–HP8 | **PROVEN:** smooth original-action factor, all six field derivatives, arbitrary one-step merged holes; source derivatives of this particular factor vanish. |
| HP9–HP11 | **PROVEN:** actual R2 mask geometry, including mergers, and limits of using coarse shadow counts or repeating a birth charge. |
| HP12–HP15 | **PROVEN conditional implication:** a complete local paired-reference/score estimate gives E15 with explicit constants. **OPEN:** its actual history-uniform hypotheses. |
| Boundary and norm alternatives | **PROVEN** scoped comparisons/counterexamples; **OPEN** compatible actual induction. |

PROVEN describes the stated mathematical assertion, including its hypotheses;
ARGUED describes a proposed construction. These labels confer no audit status,
Yang–Mills existence theorem or mass gap. Source identities, execution limits
and fresh review are in [HOLEPAY_LOG.md](HOLEPAY_LOG.md).

Credit: Tadeusz Balaban's large-field organization and Jonathan Dimock's
[Large fields](https://arxiv.org/abs/1212.5562) and
[Convergence](https://arxiv.org/abs/1304.0705). Those expositions concern scalar
phi-four in dimension three. They supply attribution, not a gauge-theory
estimate. Every additional lemma used here is proved below; no memory-only
[m] item carries weight.

## 1. Fixed target, law and norms

Use the supplied finite periodic four-dimensional SU(N) model, N>=2, odd
L>=3, normalized Haar, and Decision-4 kernels

    s(U)=1-Re tr(U)/N=||I-U||_HS^2/(2N),
    k_t(V;M)=exp(t Re tr(V* M)/N)/Z_t(M),  t=kappa u,
    R_h(V;J)=int rho_(j,h)(U;J) K_j(V,U)dU,
    Z_A(V)=int chi_A(U)b_j(U)K_j(V,U)dU,
    b_j=exp(-u_j sum_p s(U_p)),  Q_h=R_h/Z_A.

The inherited rho is not b_j. All absences, current completion alternatives,
kernel normalizers and source/vacuum terms remain. Only positive fibres are
divided by; zero fibres stay zero. The original action and kernels are
supplied model data, not new physical axioms.

T is REALRGA RGA3 with total fine-plus-coarse order 6 and source order 4,
or its RGA4 four-label version. Field directions include h_l=sqrt(N/u_l);
source weights are frozen in original units. Observable differentiation
holds every prescribed kernel and coupling fixed. There are mixed words
of total order ten. All retained variables are differentiated; species may
be removed only after integration. The output norm is

    ||K||_(mu,T)=sup_v sum_(X contains v) exp(mu |X|) sup_D T(K_X).

Here D is an open real domain with the prescribed margins and full readers.
Inactive vertices are roots. The graph is declared at each use; a coarse
shadow count is never identified with a count of original reader blocks.
Masks in a fixed-mask theorem are combinatorial parameters. Differentiating
a field-selected mask requires a separate selector-boundary theorem.

For a fixed active set Lambda in a face graph Gamma of degree <=8, let H_X
be all components of Gamma\Lambda meeting or adjacent to connected X, and
let S_X=sum_(H in H_X)|H|. The target is an **actual coefficient identity**
with a factor w_X reading only R_Lambda(X), bare K_X reading X, and

    sup_D T(w_X)<=A exp(-tau S_X),  tau>mu,                 (target)

on the complete summed history family. A raw factor, a bound for each
history separately, or a differently normalized event is insufficient.
FR/SEL, KR, and TC remain named coordinator inputs for domains/selectors,
complete interactions, and original-law charges/tails at their proved scopes.

## 2. Full-root transfer and nested saturation

Let R_Lambda(X) be LIB1's saturation and retain X disjoint from Lambda
unchanged. Under the target hypothesis, the sharper MIXSMALL external-root
argument gives, with delta=tau-mu>0,

    C_hole=A max(1,8 sup_(m>=1 integer) m exp(-delta m)),
    ||K'||_(mu,T)<=C_hole ||K||_(mu,T),
    ||K_inactive+K'||_(mu,T)<=(1+C_hole)||K||_(mu,T),
    C_hole<=A max(1,8/(e delta)).                          (HP1)

**Proof.** Leibniz with the factorial or labelled jet weights gives
T(fg)<=T(f)T(g). Also |R(X)|-|X|<=S_X. Thus each summand costs at most
A exp(-delta S_X) times its original weighted jet. For an active root v,
v in R(X) implies v in X. For an inactive root in H, connected X meeting
Lambda must meet the external face boundary partial_ext H: either an
adjacent vertex of X is there, or a path in X leaving H reaches it.
Every such vertex is active. There are at most 8|H| such vertices.
Root the input sum there and use S_X>=|H|. This proves HP1, including
inactive roots. Inactive input terms cost at most their original norm.
The continuous maximum of s exp(-delta s) is 1/(e delta). At exp(mu)=2,
exp(-tau)=1/4, the discrete maximum m/2^m is 1/2 (at m=1,2), so C_hole=4A.
Empty Lambda leaves the retained inactive family. For full Lambda the
support map is the identity, but every supplied weight w_X remains; the
weighted operator is the identity only when those weights are one.
This transfers existing jets and does not create them.

On a **common graph**, if Lambda subset Omega and X meets Lambda, then

    R_Lambda(R_Omega(X))=R_Lambda(X).                       (HP2)

Every Omega-hole is contained in a Lambda-hole. If the former touches X,
the latter does too, so R_Omega(X) subset R_Lambda(X). A further
Lambda-hole touching that enlarged set either touches X or touches the
same already included Lambda-hole; two distinct components cannot touch.
The reverse inclusion follows from X subset R_Omega(X). This proves HP2.
Finite fibre sums therefore compose, with all terms that lose their last
active vertex retained separately. They do not vanish from the exponent.

For a final, exactly weighted linear representation on that common graph,
with w_H=exp(-Q_H),

    product_(H in H_X) w_H = exp(-sum_(H in H_X) Q_H)       (HP3)

uses each charge Q_H once. HP2 permits a single final saturation estimate;
it does not license multiplying this same weight once per level or per
factor in an overlap product. Nor does HP2 commute a real RG integration
or extraction past saturation. Changing lattices requires the next section's
geometric dictionary, not automatic reuse of HP2.

## 3. An actual original-level differentiated raw payment

Fix the original level and a fixed set F of n>=1 failed bad blocks in RD
R2. A failure in R2 is still a bad block component, whether its reason is
size or completion. Each Q in F has an interior plaquette with
||I-U_p||op>=epsilon(u), where

    u=u_0>=u_*>=1,  epsilon(u)=c u^((d-1)/2),
    0<d<=1,  c>0,  epsilon(u)<=2,  0<theta<1.

This result does not cover an extra chart-failure species with no such
curvature witness. Let P(F) contain **all** interior plaquettes of F,
rather than a field-selected witness. Different blocks have disjoint
interiors. Its count satisfies |P(F)|<=C_P n, C_P=6L^4. Define the globally
smooth factor

    Q_F=theta u sum_(p in P(F)) s(U_p),
    w_F=exp(-Q_F),  a=theta c^2/(2N).                     (HP4)

On the fixed bad sector, Q_F>=a u^d n. This follows from the displayed
trace identity and distinct witnesses. The original density splits exactly
as w_F times the density with those theta fractions removed. Sources are
left in the other factor. All kernels/normalizers stay there too. At zero
source the remaining action is nonnegative; positivity of a source-bearing
remainder does not supply a normalized bound. Fractions spent elsewhere
must be deducted before theta is chosen.

For r>=1, four-factor differentiation of each plaquette gives

    |D_f^r Q_F| <= theta u C_P n (4h_0)^r.

Each ordered derivative chooses one of four unitary occurrences and costs
at most h_0; inverse occurrences have the same bound. Repeated hits keep
their order. Normalized trace is bounded by operator norm. Define
M_0(z)=1 and M_r(z)=sum_(pi partition [r]) z^|pi|. Differentiating exp(-Q)
assigns each derivative position to one block of a set partition, so

    T^(6,4)(w_F)
      <= exp(-Q_F) sum_(r=0)^6 (4h_0)^r M_r(theta u C_P n)/r!
      <= A_6 u^3 n^6 exp(-a u^d n),
    A_6=1+sum_(r=1)^6 (4sqrt(N))^r M_r(theta C_P)/r!.     (HP5)

For the second bound, a degree-k monomial of M_r has k<=r, giving
u^(k-r/2)<=u^(r/2)<=u^3 and n^k<=n^6 for u,n>=1.
The zeroth term is also bounded by u^3 n^6. Coarse/earlier-level fields
other than U_0 and all original sources do not occur in w_F; their
positive-order derivatives are zero. Thus HP5 covers the full indicated
jet of this factor, including the labelled convention, without claiming
that source jets of the other density factors vanish.

Set k=max(6,3/d). For z=u^d n>=1, u^3 n^6<=z^k. Maximizing
z^k exp(-a z/2) gives the explicit, coupling-independent constant

    A_raw=A_6 max(1,(2k/(e a))^k),
    sup_bad T(w_F)<=A_raw exp[-(a/2)u_*^d n].             (HP6)

The sector restriction is on evaluation points only. No derivative of its
indicator is taken: w_F is smooth on the surrounding group manifold.
This distinction is essential when later differentiating a selected integral.

Now H_1=N_1(pi_0 F) in RD R2, with sup-distance collar N_1. Each seed
has at most 3^4=81 neighbours. Assign every original block Q in F to the
unique face component H containing pi_0 Q. Its full N_1 singleton collar
is face-connected, hence belongs to that component. For any collection
of complete components, including all those touching X, let F_X be their
assigned birth blocks. Then

    S_X<=81 |F_X|,
    sup_bad T(w_(F_X))<=A_raw exp(-tau_raw S_X),
    tau_raw=theta c^2 u_*^d/(324N).                       (HP7)

If no component is selected, use w=1. Mergers merely unite the disjoint
birth sets; they do not change A_raw or spend a plaquette twice. In the
current coarse-block labelling, every original field read by this raw
factor is in a parent in H; retain its original argument label. If the
consumer graph counts the original blocks separately, use their actual
cardinality and conversion, not 81 as an asserted full-reader constant.
An explicit sufficient **raw** comparison is

    u_*^d > 324N mu/(theta c^2).                          (HP8)

For example this is a nonempty original-level sector whenever the chosen
cut is below two: putting diag(-1,-1,1,...) on an interior link of each
chosen block and identity elsewhere makes incident interior plaquettes
have distance two. Choose connected components above the size threshold
to make failure independent of the next field. Small product neighbourhoods
retain the strict bad/good tests. All finite Wilson/kernel factors are
positive there. This is an actual raw-density construction, not a
probabilistic tail theorem or a fitted price.

**Limit.** w_(F_X) has been split from the original integrand. It has not
been identified with the w_X of an exact local **integrated** activity.
The remaining density reads these hole variables, may join other supports,
and must still be integrated and divided by Z_A. A small prefactor of a
sector is not a multiplier of every coefficient of its logarithm:
log(p Z)=log p+log Z. Repeating p for each connected activity changes the
state. HP7 therefore proves a raw differentiated payment, not actual E15.

## 4. Growing and merging masks: what the birth count controls

Write F_s for the union of newly failed blocks at stage s. RD's exact rule is

    H_0=empty,  H_(s+1)=N_1(pi_s(H_s union F_s)).

The map A -> N_1(pi_s A) distributes over unions. Evolve the singleton
births separately, including their collars at every subsequent level.
Their union is therefore exactly H_j, including every merger. With compatible
L-block projections, pi(N_w A) subset N_(ceil(w/L))(pi A). In each
coordinate an interval of length w moves its block index by at most
ceil(w/L); periodic identification can only reduce counts. Since
1+ceil(2/L)<=2 for L>=3, induction yields

    H_j subset union_(s<j) N_2(pi_(j-1)...pi_s F_s),
    |H_j| <= 625 sum_(s<j)|F_s|.                         (HP9)

Each singleton cohort is face-connected at every stage. For any collection
of final hole components, assign a birth occurrence to it when its cohort
lies in that collection. A cohort meeting one component lies entirely in
it. The same 625 bound holds for this selected birth set. It counts
**birth occurrences**, not 625 at every level, and not distinct original
plaquettes. No extra merger entropy is charged in this set identity.

To turn HP9 into a physical price, every selected occurrence at s>0 needs
an allocated original-action or genuinely fresh kernel charge, together
with its matching/reference and derivative bill. It is invalid to replace
rho_s by b_s and charge a new Wilson action there. Overlapping ancestral
claims must have fractions omega_(i,p) with

    sum_i omega_(i,p)<=available original fraction at p.  (HP10)

Charges merge by adding these fractions; they do not reset to one. A
matched joint estimate for that merged set, not a product of conditional
probabilities under different laws, is required.

Two explicit limits matter. A nonempty hole with no later births remains
nonempty under the displayed recursion. A fixed finite birth reserve
Q therefore cannot satisfy Q>=tau sum_(j=1)^r |H_j| for every r when
tau>0: the right side is at least tau r. This refutes repeated spending
of that fixed reserve. CHARGE C6's filled towers have a geometric sum of
descendant volumes relative to a much larger original volume, and do not
assert this inequality for a fixed localized reserve.

Also, if supports are filled on the **original** block lattice, rather
than the current graph, a compatible periodic projection has exactly
L^(4j) preimages per level-j block. Hence

    |pi_(0->j)^(-1) H_j|=L^(4j)|H_j|.                    (HP11)

For one fixed finite birth set and no later births, this is unbounded as
the horizon and compatible original torus grow. Thus the proposed bound
|pi^(-1)H_j|<=625 |F_0| fails once L^(4j)>625|F_0|.
Such finite histories are allowed in R2: take an original size failure
as above, and all subsequent fields in identity neighbourhoods so there
are no new active bad blocks. Each finite history has positive mass by
strict positivity of the kernels. This supplies a geometry witness, not
a lower bound on its normalized coefficient as depth grows. Retaining
unsaturated original readers, or supplying a charged ancestor-volume
estimate, remains a possible repair. HP9 does not supply either one.

## 5. The exact differentiated matching bill

Here is a usable sufficient certificate, separating the payment from its
unproved actual realization. Suppose an actual allocated weight admits a
**proved local paired representation** w_F(y)=N_F(y)/D_F(y)>0, with fixed
integration domains and all current selector-boundary/transport terms
already justified. It must equal the required coefficient with its actual
endpoint reference, not a replacement of Z_A. Let n>=1 be its integer
charged count, c_H>0, and S_X<=c_H n, with every reader contained in
R_Lambda(X).
If reference tails extend outside it, they need a supported decomposition
and a full-root tail estimate before using this certificate.

Require the scalar paired estimate and both score bounds

    N_F/D_F <= A_0 exp[-(q-c_ref)n+b_partial |Bdy_F|],
    |Bdy_F|<=c_partial n,
    |D_I log(integrand_N)|, |D_I log(integrand_D)| <= B n
       for every permitted nonempty ordered word |I|<=10.       (HP12)

Require q,c_ref,b_partial,c_partial>=0, A_0>=1 and B>=0, with finite
constants uniform in the stated family and frozen weighted derivative
units. In particular b_partial>=0 is needed to replace the boundary
cardinality by its upper bound. Fixed nonnegative selectors may sit outside
the logarithm. Compact
domination is required. N and D may have different integration spaces,
but each domain must be fixed for differentiation. A global denominator
with volume-sized scores does not meet this local hypothesis just because
it is positive. All local cancellation must be proved before HP12 is used.

For r<=10 define M_r(B) as above, I_0=C_0=1, and

    I_r(B)=sum_(l=1)^r binom(r,l) M_l(B) I_(r-l)(B),
    C_r(B)=sum_(l=0)^r binom(r,l) M_l(B) I_(r-l)(B),
    P(B)=sum_(a+b<=6,c<=4) C_(a+b+c)(B)/(a! b! c!).

For four labelled sources use instead
P_lab(B)=sum_(a+b<=6,c<=4) binom(4,c) C_(a+b+c)(B)/(a!b!),
with the label weights already included in B. Each polynomial has
nonnegative coefficients and degree at most its derivative order.

**Proof of the jet bill.** Partitioning derivatives of exp H bounds
|D_I N|<=N M_|I|(Bn), and similarly for D. Differentiating D D^-1=1
and solving for its highest derivative gives I_r. Leibniz for N/D gives
C_r. Thus the pointwise full Taylor sum is <=w_F P(Bn). Since n>=1,
P(Bn)<=n^10 P(B). Finally n<=2^(n-1) and P(B)>=1 give

    P(Bn)<=exp(d_jet n),  d_jet=10 log 2+log P(B),
    sup_D T(w_F)<=A_0 exp[-q_net n],
    q_net=q-c_ref-b_partial c_partial-d_jet.            (HP13)

Use P_lab for the labelled convention. Zero sectors with a fixed zero
support give the zero function; a disappearing parameter-dependent fibre
is not such a sector and needs SEL. If B depends on u, retain that B(u)
and verify a uniform lower bound for the resulting q_net(u); do not call
the polynomial constant uniform without absorbing it.

The **unevaluated actual inequality** needed for this construction is

    inf_(admitted histories, levels, couplings)
      [q-c_ref-b_partial c_partial-10 log 2-log P(B)]/c_H
          >= tau > mu,                                 (HP14)

together with HP12's exact representation and complete readers. For a
coefficient actually satisfying HP12, HP13 and S_X<=c_H n prove E15 with
A=A_0 and this tau. This applies directly to an already summed coefficient
on one fixed mask only if HP12 is proved for that summed coefficient.

For distinct history masks h, apply HP1 separately, with a common tau and
A_0. Let K_h include the complete bare input family, including inactive
terms, and let M_input be the proposed native input budget. One explicit
sufficient additional envelope is

    sum_h ||K_h||_(mu,T) <= B_hist M_input,
    ||sum_h output_h||_(mu,T)
       <= (1+C_hole) B_hist M_input.                    (HP14h)

Here B_hist is finite and uniform in the claimed volume/depth family and
C_hole is HP1 with A=A_0. The active part alone costs C_hole B_hist.
Triangle inequality proves the second line from the first and HP1, even
when inactive-root maps differ between histories. An envelope
||K_h||<=a_h M_input with sum_h a_h<=B_hist suffices. Neither a per-history
uniform bound nor sup_root of a summed rooted input implies this sum of
norms in general. B_hist has not been evaluated, and is not set to one.
A direct bound for the complete summed representation may avoid this
stronger sufficient envelope, but requires its own proof.

These are PROVEN implications, not assertions that HP12/HP14/HP14h hold.
Their complete matched-jet component is comparable to the original target,
not a weak auxiliary lemma that makes closure automatic.

HP6 already paid the derivatives of one raw charge. When using HP12–HP14,
q denotes the available **scalar** charge before the joint quotient jet
bill. Alternatively, factor HP6 out inside a valid differentiated integral
and estimate only the remaining jets; never charge both derivative bills
as if two independent reserves were obtained. RGA14's regulator
multiplicities and coefficients must be included in that remaining bound.

At zero source, the direct CHARGE cap method applies to a nonnegative
sector numerator, or a complete disjoint history sub-sum, with an actual
original-action charge at least q n. It does not bound an arbitrary signed
connected activity. Choose 0<zeta<=1 with 4zeta strictly below every
retained interior cut in the all-cut denominator. With a local core of n
witnesses in a torus of n_j sites, it leaves the explicit majorant

    log Q_core <= -q n+d_j n_j,
    d_j=48u_j zeta^2+8N^2 log(1+4N/zeta)+16kappa u_j/L^4. (HP15)

For this envelope to supply even a scalar tau-price with S_X=c_H n,
it would need (q-tau c_H)n-d_j n_j>=-log A_0. For d_j>0 and fixed n,
that inequality fails as n_j/n grows. This is a failure of the displayed
upper-bound method, not a lower bound on Q_core. Source-bearing versions
need their additional original-source bill, as in MIXSMALL MS22; HP15
asserts only the source-free specialization. REFMATCH RM7–RM12 provides
a conditional mechanism for cancelling distant volume with complete
derivatives and tail roots. Its MATCH/RM2 premises have not been proved
for every actual inherited history, so it cannot silently replace HP15.

For t=kappa u>=1, fresh gaps provide
q_gap=kappa u a_gap-1-2N^2 log(1+4N kappa u). MIXSMALL MS17–MS18 adds
the derivative cost for fixed event boundaries and q_gap>=0 on its
conditional forward law. For a future weight H the actual law becomes
KH-weighted:
K^H(E)<=K(E) sup H/KH. Taking H=1_E makes K^H(E)=1. Coherent CHARGE C4
means also have zero fresh gap at their maximizing outputs. Thus fresh
gaps pay their assigned branch, not every inherited hole. This leaves
the original-charge/matched-reference branch of HP14 OPEN.

## 6. Boundary prices and norm weights

**Boundary cost, including derivatives.** LFPRICE LF7 uses matching
cluster and prefactor logarithms. If their **full jet** rooted sums are
q_T,b_T, and their coefficients agree off the complete boundary, exactly
the same root sum and triangle inequality give

    sup T(G_boundary)<=2(q_T+b_T)|Bdy|,
    sup T(exp G_boundary)<=exp[2(q_T+b_T)|Bdy|].          (HP16)

Coefficient equality must hold as functions, not just at zero source.
Empty-support source scalars have their own bill. In LF6's finite-halo
geometry, V_w=(2w+1)^4, B_0=16V_w, B_1=32V_w/(L-1), the depth factor is

    c_B^T=32 V_w(q_T+b_T)/log L,

with the separate one-time cost 2(q_T+b_T)B_1(n-1). This is a debit paid
from the creation/continuation reserve. LF7's value estimates alone do
not give q_T,b_T. Actual matching and tail geometry remain required.
Its raw replacement bill (2c_P+4kappa c_K)u can exceed a sublinear
creation price c u^d, d<1: c u^d-Cu becomes negative for C>0 and large u.
That failed envelope does not lower-bound the true matched boundary cost.

**A boundary-only suppression is insufficient for this full norm.** Take
H={1,...,n}^4 in a torus of side >=n+4, Lambda=Gamma\H, and singleton X
at an external face neighbour. Then R(X)=H union X,
|H|=n^4 and |partial_ext H|=8n^3. With the parameter-independent test
weight w=exp(-b|partial_ext H|), b>=0, and K_X=1, the exact norm ratio is

    exp(mu n^4-8b n^3).                                (HP17)

For fixed mu>0 and finite b it is unbounded. Equivalently E15 would need
tau n^4-8b n^3<=log A, which fails for every tau>0. These cube geometries
occur in MIXSMALL MS28's positive-mass one-step histories; the chosen
boundary weight is a test weight, not an asserted actual history amplitude.
This proves only the limitation of boundary-only payment. Volume charges,
different supports and cancellation remain available.

**A norm cannot supply unproved smallness.** A precise candidate with two
labels (core X, actual readers R(X)) is

    ||F||_(mu,tau;Lambda)=sup_x sum_(X contains x, X meets Lambda)
       exp(mu|X|+tau S_X) sup T(F_X).                    (HP18)

The functions F_X may read R(X); HP18 is deliberately a different input
space from RGA7. Dividing each weighted summand by exp(tau S_X) and
repeating HP1 proves saturation into the full output norm with constant
max(1,8 sup_m m exp[-(tau-mu)m]). Thus it works if the actual coefficients
already have finite HP18 norm. For F_{ {v} }=1 next to an arbitrarily
large hole that input norm itself grows as exp(tau|H|).
Giving holes zero weight instead, as LIB1's active norm does, leaves the
unbounded full-norm conversion exp(mu|H|). A regulator exp(aE) likewise
requires the joint moment of RGA14 after integration; overlaps add
multiplicities. None of these definitions proves the required membership,
joint moments, source conversion or next-step regeneration.

## 7. No-Go Discipline Gate — partial construction, no exhaustion claim

N1: The distinct mechanisms examined are original-action allocation
(HP4–HP8), boundary cancellation (HP16/HP17), weighted input spaces
(HP18), fresh conditional-kernel gaps (section 5), and integrating complete
holes/readers before assigning final supports (the REFMATCH/RGA14 route).
The first gives a raw positive result; the next two give conditional
transfers and scoped failures; the fourth prices only its actual branch;
the fifth remains OPEN. These are not five exhausted families. No negative
packet PASS or universal no-go is claimed.

N2: No number of independent walls is asserted. Denote complete matching
by M, full selector/quotient jets by J and charge-to-full-support coverage
by C. A strong differentiated M can contain J (yes, for that representation);
J alone implies M: unresolved. M implies C: unresolved; C implies M:
unresolved. J implies C: unresolved; C implies J: unresolved. HP12–HP14
jointly imply the chosen payment, whereas an E15 weight need not admit
this particular score representation. These are overlapping obligations.

N3: Explicit premises are fixed masks, actual graph units, distinct interior
bad witnesses, unused theta, supplied thresholds, fixed source units,
complete derivative orders, fixed-domain domination, local paired scores,
complete readers and summed history envelopes. No regularity of a hard
selector is inferred from the smooth charge. No coupling flow is derived.

N4: LIB1 L23/MS26 concern unweighted saturation, HP17 a specified boundary
weight, HP11 original-footprint conversion, JMBRB B-MASS repeated positive
mass pricing, and CHARGE C13 the extensive cap majorant. None refutes an
actual matched, charged, differentiated coefficient. The residuals are
kept distinct; no witness is reused as a physical impossibility result.

N5: HP5 is per raw original charge and its full finite jet; HP9 is a
finite-chain set identity; HP17 is a single supported test activity on a
family of four-dimensional graphs. No mode/spectrum/continuum or lattice-wide
all-history derivative estimate follows. Computational coverage is only
what the execution receipt actually records.

N6: Adapted references, carrying unnormalized masses, integrating before
saturating, and a proved compatible norm conversion are mathematical
alternatives requiring no new physical axiom. The registered units,
kinetic-form and realized-state primitives are not analytic price estimates
and are not counted as missing premises.

N7: The strongest counter-route to a broad negative conclusion is to retain
HP4's original reserve, cancel the distant denominator by an actual pinned
reference construction, integrate every shared reader once, and prove a
joint derivative majorant for the resulting full-support coefficients.
REFMATCH RM7–RM12 and REALRGA RGA14 explain a compatible mechanism; its
terminal obligation is HP12/HP14 (or a direct integrated substitute),
including SEL and common history envelopes. This note has not ruled it out.

N8: The inspected prior work already distinguishes filled creation from
localized comparison (CHARGE), complete input jets from mere regrouping
(LIB1/MIXSMALL), and regulator control from probability (REALRGA/REFMATCH).
HP5 adds the local raw-charge derivative calculation; HP9 prevents an
exponential-in-depth overcount of current mask collars. Neither retires
the original-footprint or actual matched-integration obligation.

## 8. Disposition and next decision

**ARGUED next construction:** use the one-step original failed-block family
in section 3, keep its unused charge and original readers, and construct
the local paired integral for the whole merged hole. Test HP12 with one
retained field derivative and four original-source labels before claiming
the full (6,4) bound. This is a diagnostic subcase, not the final target.
If the reference tail leaves R(X), retain it in a supported decomposition
with the full-root reserve of REFMATCH; do not delete the tail. Subsequent
levels need charge ownership for each new birth and the actual consumer's
reader graph. A failed-return or chart-only species without a paid witness
stays explicit in the complement.

The unevaluated same-law inequality HP14, current-selector regularity and
the complete history/root sum remain OPEN. HP8 is an evaluated sufficient
raw threshold, HP15 and HP17 give exact failed inequalities for specified
methods, and HP9 covers growth/mergers without inventing fresh charges.
This is the deliverable's completion boundary; no general hole payment,
uniform RG induction, or physical no-go has been manufactured.

Finite regression criteria are [registered here](checks/holepay_criteria.md).
The resource-gated runner and its actual receipt, followed by the fresh
hostile review and any fixes, are linked from the log. Written proofs carry
the mathematical assertions; finite checks alone cannot close E15.
