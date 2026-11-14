# Repo search

**READ.** FINISH row 802 assigns this fixed-coupling size-recursion target.
The target-specific `prior/gap-size-rec-astra.md` does not exist at
`33a4d3b457825282502b78bdf6746dffa94557ff`.
The lead's `prior/repo-search-2026-11-08.md` concerns row 531's admission
and formation problems. Its hits are not suppliers of this recursion.
Row 802 has no separate “Repo prior work” list.

**READ.** I refreshed `main` and PRs 10114, 10133, 10134 and 10141.
A filename search outside this lane for `twist free energy`,
`thick.vortex`, `Kanazawa`, `Mack.{0,12}Petkova`, and `size.recursion`
found no match on those five refs. This is a bounded vocabulary search,
not an absence theorem. The registry, `open-core.md` and `l17c.md`
have no match for this target or its twist-free-energy names.
Following row 800's more general RG citations also found the older
soft-route MK diagnostic and common-matching warning (exact passages
in section 6). They address a related normalization problem, not the
requested fixed-coupling size estimate.

**READ.** The close prior work is inside this lane: Claude Fable 5.2's
`gap-skeleton-max.md` B3 and E.2–E.3 already identify the entropy cost
in doubling; `gap-skeleton-max-b.md` 1.5 already distinguishes powers
of one transfer operator from enlarging its spatial box. These are
restrictions to retain, not new results of this note. Theorem R in
`gap-means-max.md` and Codex's `gap-kanazawa-astra.md` are the assigned
inputs, to be used only with their stated hypotheses.

# Fixed-coupling recursion for the twist free energy

Proof item, FINISH 802. Author: Codex gpt-6-astra max, 2026-11-12.
Research text, not an audit; no scientific status is granted.
Labels READ, PROVED, ARGUED, GUIDE and OPEN describe this note's use
of a statement. PROVED means a written hand argument here, not an
independent check. No numerical calculation is proof evidence.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for the outline and complete account at `31a47c543775`.
Credit the named lane authors and the literature authors at each use.

## Checkpoint

**OPEN, final checkpoint.** No contracting Wilson recursion was proved
or refuted. Sections 2 and 4 give exact counterexamples to three
proposed inferences, with their limited domains stated. Section 3
proves a conditional propagation theorem and explicit seed threshold.
The remaining obligation is section 6's uniform Wilson estimate,
its seed, and an interpolation estimate if all integer sizes are needed.
Section 5 explains why the comparison phases test a recursion together
with its seed, rather than automatically refuting the upper inequality.
The two sources were each fetched once to
`/tmp/sa-gap-size-rec-astra.m9MhBN/`. No numerical run was made.

## 1. The precise object and the existing doubling obstruction

**READ; definitions.** Fix beta in the compact interval I of
`gap-ext-astra.md:78–129`. On n=(a,a,c,d), c,d in {a,2a}, retain
the original Wilson partition functions and put

\[
 F_{m,v}(n)=-\log\frac{Z^{m+v}(n)}{Z^m(n)},\qquad
 F(a)=\max_{n,m,v,\,\text{required frames}}F_{m,v}(n).
 \tag{1}
\]

The background m is spatial and v temporal in the selected frame.
Then 0<Z^(m+v)/Z^m<=1. The target (V) is
F(a)<=C a^p exp(-sigma a^2), uniformly on the required family.
The weaker fusion consumer (FQ) does not require this area exponent.
Here c,d grow with a. Holding them fixed is a different limit.

**READ.** The old B3 argument already gives the relevant identities.
For a pure twist in plane ij, write q=tanh(F/2). In a direction
inside that plane, let T_+,T_- be the two center-parity restrictions.
For a nonzero positive trace-class operator S and t>=1 write

\[
 H_2(S;t)=\log\frac{(\operatorname{Tr}S^t)^2}
                            {\operatorname{Tr}S^{2t}}.
\]

`gap-skeleton-max.md:258–277`, Lemma 4, gives exactly

\[
 q(2t)=q(t)^2e^{H_2(T_+;t)-H_2(T_-;t)}.                 \tag{2}
\]

In a direction outside the twist plane it gives

\[
 F(2t)=2F(t)+H_2(T_m;t)-H_2(T_0;t).                    \tag{3}
\]

All other sides are fixed in each identity. The operators change when
a spatial side changes. These formulas are prior work, not this lane's
proof. Their signed entropy terms cannot be dropped. Row 670 already
records the corresponding failure for thermal sums and vacuum energies.

**PROVED, limitation of B3's convexity wording.** Convexity of both
log partition functions does not imply concavity of their difference.
For example take T=diag(1,r,r), 0<r<1, and the commuting involution
C=diag(1,1,-1). Then Z(t)=1+2r^t and Z^v(t)=1 are positive,
and F(t)=log(1+2r^t) has

\[
 F''(t)=\frac{2(\log r)^2r^t}{(1+2r^t)^2}>0.
\]

Both log partition functions are convex. Thus B3's sentence inferring
concavity from their separate convexity is not a usable implication.
This finite operator example is not a Wilson-theory counterexample.
It leaves the exact identities (2)–(3) intact.

## 2. A small twist seed does not bound the transfer entropy

**PROVED, operator-level obstruction.** Fix any integer t>=3 and N>=2.
On N+2 states put r=2^(-1/t), let u be the normalized constant vector,
and set T=rI+(1-r)|u><u|. Let J interchange two states and fix the
others. The kernel has strictly positive entries, T is positive
definite, and its top eigenvector u is simple and even. Also JT=TJ.
Then T_+ has eigenvalues 1 and N copies of r; T_- has one eigenvalue r.
For every positive integer s, its twisted trace is
1+(N-1)2^(-s/t)>0. Directly,

\[
 q(t)=\frac1{N+2},\qquad q(2t)=\frac1{N+4},\qquad
 \frac{q(2t)}{q(t)^2}=\frac{(N+2)^2}{N+4}.             \tag{4}
\]

Hence F(t) can be arbitrarily small while F(2t)/F(t) tends to one.
There is no dimension-independent bound q(2t)<=C q(t)^2 from
positivity, a simple even vacuum, and a small q(t).

More explicitly, for 0<=q<=1/2,
2q<=2 artanh(q)<=4q. Thus
F(2t)>=2/(N+4), whereas F(t)^p<=(4/(N+2))^p for any p>1.
Given C,A,mu>0 and p>1, choose N so that
C(4/(N+2))^p<1/(N+4), then choose t so large that
A exp(-mu t^2)<1/(N+4). This also refutes the proposed
superlinear estimate with that remainder on this operator class.
No enumeration or numerical approximation enters this example.

**ARGUED scope.** It is not a four-dimensional local Wilson model,
and does not refute a conjectured SU(2) recursion. It refutes the
step that tries to deduce the needed entropy bound from the one
twist number and transfer positivity alone. Geometry or a quantitative
Wilson estimate must do additional work.

**READ / PROVED scope of Theorem R.** Its actual hypotheses include
S_ev and the vacuum-energy defect Delta, not F alone
(`gap-means-max.md:146–249`). The theorem supplies no bound on those
inputs in terms of F. The even thermal sum in (4) is already N/2.
More generally, tensoring every sector
operator with the same neutral positive operator B cancels
Tr(B^t) from every twist ratio, while multiplying the normalized
even partition sum by Tr(B^t)/lambda_max(B)^t. This factor can be
arbitrarily large, even with a simple top eigenvalue. This is an
algebraic test, not an enlargement of the allowed Wilson model.
It shows why Theorem R needs information not present in F.

**READ, additional crossed-background problem.** The second cut is
not automatically a positive transfer problem. For m=v_24, v=v_13,
changing time to direction 2 leaves the seam operator
C_4(T_0^t+T_(v_13)^t)/2. It is negative on its nonzero odd subspace.
This is proved in `gap-kanazawa-astra.md:417–456`. Therefore a
derivation of (2) in one admissible frame cannot simply be repeated
in every direction for all the pairs in (1).

## 3. What a successful recursion would actually need

**PROVED, propagation lemma.** Let a_n=2^n a_0 and f_n>=0. Suppose
numbers C_n,A_n>=0 and mu>0 are supplied independently of unknown
large-box values, and for every n>=0,

\[
 f_{n+1}\le C_n f_n^4+A_n e^{-\mu a_n^2}.                \tag{5}
\]

Put K_n=max(1,C_n+A_n) and

\[
 B=\sum_{n\ge0}4^{-n-1}\log K_n<\infty,
 \quad g_0=\max(f_0,e^{-\mu a_0^2/4}).
 \tag{6}
\]

If g_0<exp(-B), set gamma=-log(g_0)-B>0. Then

\[
 f_n\le \exp(-\gamma4^n)
       =\exp[-(\gamma/a_0^2)a_n^2].                     \tag{7}
\]

*Proof.* Set b_n=exp(-mu a_n^2/4), g_n=max(f_n,b_n).
Then b_(n+1)=b_n^4, and the error in (5) is A_n b_n^4.
Consequently g_(n+1)<=K_n g_n^4. Iteration gives

\[
 4^{-n}\log g_n
 \le\log g_0+\sum_{j<n}4^{-j-1}\log K_j
 \le-\gamma.
\]

This proves (7). The floor b_n avoids any logarithm of zero. QED.

**PROVED, explicit sufficient seed size.** For constant C,A, let
K=max(1,C+A), B=(log K)/3. It suffices to have

\[
 a_0\ge3,\qquad
 a_0^2\ge\frac{4(1+B)}\mu,\qquad
 F(a_0)\le e^{-1}K^{-1/3}.                              \tag{8}
\]

Choose the next allowed integer, or dyadic size, above this lower bound.
Then (7) holds with gamma>=1, provided (5) is valid on the entire
required family. This is a conditional seed prescription, not a
computed SU(2) seed. Constants uniform on I and a uniform seed on I
give a uniform conclusion on I.

**PROVED, weaker coefficient requirement.** A uniform C is unnecessary.
The summability in (6) suffices. For example log K_n<=D a_n^r,
0<=r<2, gives
B<=D a_0^r/[4(1-2^(r-2))]. A K_n polynomial in a_n also qualifies.
A crude positive surface cost log K_n of order a_n^3 supplies no
finite bound by this test. It must be cancelled or improved.
This observation does not assert that the actual cost has either size.

**PROVED, exponent requirement.** With no remainder, C>0, p>1,
and 0<f_0<C^(-1/(p-1)), the equality f_(n+1)=C f_n^p gives

\[
 f_n=C^{-1/(p-1)}
       \bigl(C^{1/(p-1)}f_0\bigr)^{p^n}.
\]

This follows by multiplying the recursion by C^(1/(p-1)) and
iterating powers. Thus the decay is exp(-c p^n), up to a constant.
Since a_n=2^n a_0, this is exp(-c'(a_n)^(log_2 p)).
For 1<p<4 this sequence obeys the recursion but fails every positive
area-exponential bound. Thus a contracting map alone does not imply (V).
Quadratic doubling gives exponential decay in a, not in a^2.
For enlargement a->ka, the corresponding threshold is p>=k^2.
An exponential-in-a conclusion might feed (FQ) only with a sufficiently
large decay rate relative to its existing lower bound S_ev>=eta_*^a.

**OPEN, interpolation and family closure.** A dyadic recursion proves
(7) on a_n only. It does not prove (V) at every larger integer size.
One sufficient bridge, with fixed D,h,eta,nu>0, would be

\[
 F(b)\le D a^h\{F(a)^\eta+e^{-\nu a^2}\},
 \qquad a\le b\le2a,                                   \tag{9}
\]

for a on the dyadic hierarchy and all required b-boxes and frames.
Indeed a>=b/2 makes (7) and (9) imply (V), with exponent
min(eta gamma/a_0^2,nu)/4 and a polynomial prefactor.
No such bridge is supplied by separate convexity of partition functions.
Alternatively one could prove (5) for a shell envelope over sizes
[a,2a]; its seed would then concern that entire finite shell.
Neither is silently replaced by a seed at a single torus.

**OPEN, seed at the requested coupling.** No read source bounds the
left side of (8) at an order-one beta. The auxiliary coarse action
in `gap-kanazawa-astra.md` has an area-small endpoint; it is not the
fine Wilson action. Existing strong-coupling expansions apply in their
own small-coupling domain. A finite-box seed is an exact finite Haar
integral inequality and could in principle have a hand proof, with
analytic remainder bounds. No such order-one proof is given here.
Numerical integration, even with a very small answer, would not supply
the seed under this task's rules.

## 4. The other two attempts do not supply (5)

### 4.1 Chessboard gluing and thick containers

**READ.** The outline's AM6, lines 2885–2942, is a proved finite-torus
chessboard inequality for positive slab profiles. Its disseminated
partition functions retain the original torus and shared seam variables.
It is not an identification with independent smaller periodic tori.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors.

**PROVED, obstruction to the proposed product step.** Four small
averages need not have a small fourth-power joint average, even under
reflection positivity in every cut of the four slots. Let a latent bit
H have probability p in (0,1) of being one, and set every slot equal
to H. For a function of one half, reflection gives

\[
 \mathbb E(\overline f\,\vartheta f)
 =(1-p)|f(0,\ldots,0)|^2+p|f(1,\ldots,1)|^2\ge0.
\]

Each slot event has probability p; their intersection also has
probability p, not p^4. Chessboard's disseminated-event bound holds
with equality. This is a finite probability counterexample to the
averaging step, not a Wilson counterexample.

**ARGUED, actual attempt and failure.** Cut a large Wilson torus into
blocks and retain the seam links. Interior integrations then give
conditional boundary kernels. Replacing those kernels by the periodic
small-box ratios would discard their boundary data and their common
normalization. Neither AM6 nor the scalar F(a) controls that replacement.
Even conditional independence of interiors leaves the seam average of
a product, which the preceding example shows cannot be factorized.
The needed next estimate is a bound on the normalized boundary kernels,
or on their correlated gluing error, in the original Wilson law.

**READ, literature scope.** `prior/gap-lit-transport.md`, section B,
records Gerhard Mack and V. B. Petkova's comparison criterion and
Mack's DESY 80/03, section 8, equation (8.6). It uses a maximum
Fourier coefficient for vortex-container partition ratios and supplied
control as container thickness grows. It does not derive that control
from the one periodic number F(a_0). The criterion is a consumer of
thick-vortex estimates. Its proof is not rebuilt here; only the local
reading record is used. No boundary-uniform criterion is silently
identified with (1).

**OPEN.** A valid Wilson gluing estimate with the coefficient budget
(6), or a direct proof of (5), is absent. The surface-cost comparison
already rejected by row 670 does not supply it. A container assumption
strong enough to guarantee the missing factorization would be an extra
input, not a consequence of the seed in (8).

### 4.2 Kanazawa's inverse representation across sizes

**READ.** Takuya Kanazawa's representation, in the crossed-background
extension proved in `gap-kanazawa-astra.md` section 3, supplies

\[
 Q_f(a)=Q_c(a;\alpha)e^{-D_a},\qquad
 Q=(1+e^{-F})/2,\qquad
 D_a=N_a\int_\alpha^{\alpha_a}p'_{c,a}(u)\,du.           \tag{10}
\]

It supplies an area-small coarse endpoint and an O(1/N_a) parameter
shift. The coarse action can be chosen independently of the fine
Wilson action. These are existing results of row 800.

**PROVED consequence, no cross-size estimate from (10).** Fix epsilon>0
and prescribe Q_f(a)=(1+exp(-epsilon))/2 at every size. The prior
scalar inverse construction still solves (10) at every sufficiently
large compatible size, with the same derivative bounds and
O(1/N_a) shifts. Indeed log Q_c-log Q_f lies in [-log 2,log 2],
which is precisely the interval that construction covers. Thus all
those representation bounds coexist with F(a)=epsilon for every a.
Taking C epsilon^3<1/2 and then A exp(-mu a^2)<epsilon/2
contradicts (5) for this scalar data.

This example is not an assertion that a Wilson model realizes those
data. It proves that independent inverse representations, including
their small parameter shifts, do not imply the recursion. The
extensive derivative cancels the inverse-volume shift. Comparing
D_(2a) with D_a requires new fine-measure information. The row-800
response identity already explains what information is missing;
renaming that response as a size correction would close nothing.

## 5. Binding tests and their exact logical scope

**PROVED, qualification of the test.** A nonconfining phase rules out
the recursion *together with a contracting seed*. It need not refute
the upper inequality by itself. For example the constant sequence
f_n=f>0 obeys f_(n+1)<=C f_n^4 whenever f>=C^(-1/3).
Also f(a)=tau a^2 obeys f(2a)<=C f(a)^4 at every sufficiently
large a, although it grows. Thus “group-blind, therefore impossible”
is not valid for a conditional small-seed criterion. Its proof must
either fail in the comparison group or fail to furnish the seed.
No counterexample to SU(2) follows from this logical observation.

### 5.1 U(1)

**READ.** `prior/gap-lit-u1.md` reports Jürg Fröhlich and Thomas
Spencer's large-beta no-area-law result, with the distinction between
the detailed Villain proof and the stated Wilson-cosine extension.
`gap-tu-retry.md:448–508` keeps a specific periodic Wilson-score
passage open. Neither passage proves a sharp asymptotic formula for
every finite twisted Wilson torus. I do not turn them into that claim.

**ARGUED, using the brief's Coulomb scaling as a binding test.** Write
A=L_i L_j for the twist-plane area and B for the transverse area.
The stated density law is F_U(1)/B of order 1/A. On the family
in (1), B/A stays between fixed positive constants. The total F_U(1)
therefore stays of order one in size. It is not of order a^(-2).
If this value lies inside the contracting domain, iteration of (5)
is impossible. If it lies outside, the inequality alone need not fail.
At large beta a classical fixed-flux cost is large, not an exhibited
small seed.

**PROVED conditional contradiction for an algebraic tail.** If, in a
specified limit where that asymptotic is valid, F(a) is asymptotic to
kappa/a^2 with kappa>0, then F(2a)/F(a)->1/4 whereas
C F(a)^4/F(a) and A exp(-mu a^2)/F(a) both tend to zero.
Thus (5) is false in that limit. This argument must not be applied
to the total F on fixed-aspect boxes by replacing it with F/B.
Holding B fixed indefinitely also requires a uniform Coulomb
asymptotic in that different limit; it is not supplied by the brief's
four-dimensional fixed-aspect test or by the two read notes.

**READ / ARGUED, failing step.** Transfer positivity, chessboard
estimates and Kanazawa's representation all survive for U(1). They
do not justify dropping the entropy or normalization terms in
sections 2 and 4. An attempted group-specific use of the prior
small-commutator premise (LC) fails immediately: [A,B]=1 in U(1).
No estimate deriving (5) from (LC) has been obtained for SU(2).

### 5.2 Binary icosahedral group

**READ.** `gap-cf-astra.md:248–264,485–524` and
`gap-kanazawa-astra.md:607–650` already show that local commutator
flattening survives in this finite non-Abelian group. In particular,
the center-odd commutator contraction has norm 1/4, just as in SU(2).
That cannot be the distinguishing step. The positive transfer and
character-kernel arguments also survive with counting Haar measure.

**READ, exact obstruction and its limit.** With
Delta_G=min_(g!=1)(1-tr(g)/2)>0, the rank-four twist has classical
energy at least Delta_G a^2, while its comparison sector has a flat
configuration. The prior note explicitly leaves the normalized
fixed-finite-beta torus phase estimate open: the crude partition
comparison loses a volume entropy. It proves a fixed-box
zero-temperature obstruction, not the large-box weak-coupling
free energy. This lane does not claim to have filled that gap.
The weak-coupling phase stipulated as the binding test must therefore
remain a test input, not a newly proved torus theorem.

**READ, exact failure of the available SU(2)-specific premise.** In
(LC), both generators obey 1-tr(A_M)/2,1-tr(B_M)/2<=pi/(2M).
For M>pi/(2Delta_G), both must equal the identity. Their
commutator cannot have Mth power -1. This fails at discreteness,
whereas U(1) fails at commutativity. The result and proof are already
in `gap-ext-astra.md:474–521`; they are reused, not rederived.

**ARGUED disposition.** No quantitative step in the three size attempts
uses (LC) to control the original Wilson seam measure. Thus none
passes both group tests as a proof that reaches (V). Conversely,
the stipulated growing finite-group twist cost is compatible with
an upper quartic inequality outside its contracting domain, as the
first paragraph proves. It does not by itself refute that inequality.

## 6. Source record and final obligation

**READ, repository provenance.** Main was
`bb4ec020d5ada57c630dd89acc98a68397ade423`; PRs 10114, 10133, 10134,
10141 were respectively `f76f6c649c`, `89faef229f`, `1e70c7211a`,
`fb99b4dddc`. The workflow on main redirects to RULES, SETTINGS and
the research procedure; those were read. Science here stays pinned
to the requested checkout. No audit, status file, registry or queue
was edited.

**READ, additional outside-lane hit.** Following row 800's citations,
I read PR 10114's
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks/review_massgap_block_literature.md:100–128`
and `PROOF.md:5755–5773` in that same directory. The former credits
Ito–Seiler's distinction between strong-coupling flow and common
interpolation matching. The latter labels its Migdal–Kadanoff map an
uncontrolled approximation for the real four-dimensional RG. These
are related diagnostics, not a fixed-Wilson size recursion. Credit
their Codex authors; no toy numerical result is imported.

**READ, index before source.** The SA-index instructions, chunk-02
rows for GL8, chunk-03 rows for AM5–AM7, their neighbours, and
obligations:76–88 led to outline 2313–2355 and 2885–2942.
The former constructs a positive trace-class transfer operator;
the latter proves the finite-torus chessboard inequality used above.
Searches for vortex, Kanazawa, Petkova, twist-free-energy and
size-recursion terminology in the outline index, obligations,
CA-I 4.12–4.19 index and both downloaded sources found no target
supplier. The one source hit, outline 23100, was checked through
chunk-21's neighbouring rows and source 23067–23101: it propagates
an RG source-size constant, a different object. This is a bounded
search record, not a claim about every differently named argument.
No theorem of the account is credited with proving (5).

**PROVED here, not independently checked.** The finite operator
counterexamples invalidate the entropy-free transfer inference;
the four-slot measure invalidates the proposed factorization from
reflection positivity; the scalar inverse example invalidates the
cross-size inference from Kanazawa's representation alone. None is
a counterexample to the actual SU(2) Wilson conjecture.
The propagation lemma gives the explicit sufficient seed (8),
and (6) is the weakest coefficient budget reached in this attempt.

**OPEN, exact missing statement.** At the original Wilson normalization
and one specified order-one beta, prove (5) uniformly for every pair
and frame in (1), with mu>0 and externally bounded C_n,A_n satisfying
(6); prove max(F(a_0),exp(-mu a_0^2/4))<exp(-B).
Equation (8) is an explicit sufficient constant-coefficient case.
A proof using gluing
must retain its conditional seam laws and handle the nonpositive
crossed cuts. For all integer sizes also prove a bridge such as (9),
or formulate and seed a shell version. These conditions suffice;
none of the three attempts supplies the missing Wilson estimate.

**ARGUED stopping decision.** Transfer moments fail at the signed
entropy estimate. Chessboard/container gluing fails at normalized
boundary control. Scalar coarse inversion fails at the relation
between the shifts at different sizes. These are three tested
mechanisms, not three proofs that a recursion cannot exist.
No numerical run was made. No order-one seed, (FQ), (V), mass gap
or continuum conclusion is established. A further equivalent scalar
rewrite would not change this result.

RESULT: OPEN — a quartic size recursion with an explicit seed would imply dyadic (V), as proved here; the required SU(2) Wilson recursion, seed and all-size bridge remain unproved, and the stated positivity, gluing and inverse-representation shortcuts do not supply them.
