# Repo search

**ARGUED / source record.** FINISH row 769, 2026-11-12. Author:
Codex gpt-6-astra max. Source checkout `0218f610d1c73eec9976e149f1d04d1b4e38b54d`.
Research text, not an audit; no scientific status is granted.
Here **PROVED** means a complete hand argument supplied by the author,
pending a separate check. **ARGUED**, **GUIDE**, and **OPEN** mean less.
No numerical calculation discharges a statement.

**ARGUED / prior search.** `prior/gap-pag-grow-astra.md` is absent.
The lead's `prior/repo-search-2026-11-08.md` concerns earlier targets.
Its closest hit is the transfer-kernel plaquette correlation in
`pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`.
That is a different conditional law. The search in `prior/gap-lit-block.md`
found no supplier of PA_g. Its closest crossover note supplies an assumed
transfer gap, not a conditional block angle. Current main was fetched at
`a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc`; its workflow, rules, settings,
and research procedure were read. No planning statement supplies science.

**ARGUED / credited inputs.** `gap-crux-exercise-astra.md` §§8.1, 8.4
defines PA_g and its product-box cover. `gap-pag-corner-astra.md` §§1–3, 6
supplies the face pair and the fixed-block obstruction. Its checker,
Claude Opus 5.5 in `gap-pag-corner-check-opus.md`, confirms that argument
with the stated geometry and exterior-neighbourhood corrections. These
are earlier Codex/Astra results, not results reproved here. Searches in
`open-registry.md`, `open-core.md`, and `l17c.md` found no matching owner
for the growing-block estimate. The checked fixed-block result does not
cover this target.

## Contract and checkpoint

**ARGUED / target contract.** Decide PA_g for the nonwrapping product-box covers of
§8.1 with lattice scale $L=\ell$ growing with $\beta$. The degree bound
is 80 and the required angle is at most $1/160$. Keep the exterior
quantifier, including its essential-supremum version, and torus uniformity.
The wider face-corner class has the precise geometry in the Opus check.

**ARGUED / notation.** Write $x(W)=\operatorname{tr}(W)/2$ for SU(2).
The parameter $L=\ell$ is the partition scale used in §8.1. The equal
blocks have actual side $2\lfloor2L/3\rfloor+1$ lattice sites, so every
stated growth rate is also the block-side rate up to a fixed factor.

**PROVED / imported, checked.** At identity exterior the face pair has
quadratic trace correlation at least $1/49$. For each bounded block
size its Wilson correlation exceeds $1/64$ above some $\beta_0(L)$.
That theorem gives no bound on $\beta_0(L)$.

**PROVED / final checkpoint, author only.** The direct factor estimate
in §8 gives a pair angle at least $\beta/(6+19\beta)$, independently of
$L$, on the symmetric equal-interval covers in §5. It defeats every
growth rate in that family once $\beta>2/47$. Twelve explicit bounded
functions suffice when $\beta\ge1/2$. Sections 2–4 also prove the
requested rescaled-moment estimate on an explicit slow-growth regime,
for all §8.1 interval choices.

**OPEN / retained limits.** The unrestricted elementary-trace moment
estimate and covers excluding every symmetric pair are not decided.
The next action is a separate check of the new proof, especially
Lemma R's geometry and Lemma W's sign and integrability. No computation,
audit, registry edit, or public post was used. The proof credits
Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, for the reflection Gram construction it uses.

## 1. Source scope and the new estimate

**ARGUED / source comparison.** The named PR sources were fetched and
read: `MASS_GAP_LOCAL_BLOCK_ASTRA.md:92–164` on #10114 and
`MASS_GAP_CROSSOVER_REDUCTION.md:1–130` on #10133. The first proves a
positive transfer correlation, with an exponentially small local-density
bound. The second explicitly leaves crossover clustering open. Neither
proves the present conditional corner estimate. Main's
`docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145`
uses a specified noncompact law. Its covariance comparison is not a
Wilson moment estimate. These are the closest relevant hits in the
lead's digest; the other digest entries address different RG suppliers.

**ARGUED / source comparison.** The outline and CA-I were downloaded once,
at `31a47c543775`, to `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`.
The SA-index README, chunk-01/02 rows for the scalar gap and free
curvature, chunk-25 rows 28052–28123, their neighbours, and obligations
at 778–779 and 28096–28099 were consulted first. Source reads:
SA 766–779, 1382–1386, 1670–1687, 28050–28123. In GCB48 the measure
is explicitly “still the Gaussian cutoff measure”. Thus GCB47–49 prove
readout estimates on their stated chart and law; they do not supply $M$.
The CA 4.12–4.19 index and neighbouring rows led to CA-I 46064–46075
and 49495–49516. These specify a quadratic fluctuation integral and
retain application conditions. No claim of absence from all CA-I is made.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of that text; the Balaban construction named there is Tadeusz Balaban's.
No Balaban estimate is imported into the proof below.

**PROVED / new scope.** For every §8.1 cover at lattice scale $L\ge12$,
put

\[
 N=32(L+1),\qquad H=2^{16}N^{20}.
 \tag{1}
\]

If $\beta\ge H^{100}$, the three errors in the predecessor's
§4.1 are at most $1/10000$, uniformly in the cover and ambient torus.
Consequently its face-corner Wilson correlation exceeds $1/64$.
Sections 2–4 prove the new quantitative passage. The already checked
quadratic correlation and its conversion (7) are used, not reproved.

## 2. A quantitative replacement for the compactness step

**PROVED (Lemma G).** Use identity exterior and the interior-vertex
forest slice of the predecessor's §3.1. Let $n$ count its remaining
links and $m=3n$. Write each remaining link as
$U_e=\exp(iA_e\cdot\sigma)$, with $|A_e|\le\pi$, using principal
coordinates outside their measure-zero ambiguity. Let $\mathcal S$
be the sum of $1-x(U_p)$ over touching plaquettes. With (1),

\[
 m\le H,\qquad
 \mathcal S(A)\ge |A|^2/H,
 \qquad |A|^2=\sum_e|A_e|^2.
 \tag{2}
\]

*Hand proof.* The union patch and its collar fit in a box of side
at most $8(L+1)$. Embed that box in an auxiliary $N$-torus.
This preserves every touching plaquette and the conditional law.
It does not restrict the original torus size.

Choose a vertex $r$ whose four coordinates lie outside the patch's
bounding intervals. The exterior graph is connected on boundary
vertices, as proved in the predecessor. Every boundary vertex has
an exterior path to $r$ of length at most $N^4-1$: erase loops
from a path in this graph. Every interior vertex has a forest path
to a boundary root of length at most $N^4-1$.

For a remaining link $e$, join $r$ to its initial vertex using
these paths, traverse $e$, and return to $r$ in the same fashion
from its final vertex. The closed walk has length at most
$4N^4+1\le5N^4=:M$. Its transport in the slice is exactly $U_e$:
every other edge on the walk is exterior or a forest edge.

Sort its signed coordinate steps by coordinate direction. An adjacent
swap of different directions inserts a conjugate of an elementary
plaquette transport or its inverse. There are at most $M^2$ swaps.
Cancel adjacent reverse steps in each one-direction word. Each remaining
word winds an integral number of times around a coordinate circle based
at $r$. It is exterior, because the other three coordinates of $r$
are outside the bounding box. Its transport is $I$.

Telescoping the swaps and using unitary invariance of the operator norm
therefore gives

\[
 \|U_e-I\|\le M^2\max_p\|U_p-I\|
       \le M^2\sqrt{2\mathcal S}.
\]

The maximum may include exterior plaquettes; their defect is zero.
For a principal angle $a\in[0,\pi]$,
$2\sin(a/2)\ge2a/\pi\ge a/2$. Thus
$|A_e|^2\le8M^4\mathcal S$. There are at most $4N^4$ remaining
links, so

\[
 |A|^2\le 8(4N^4)(5N^4)^4\mathcal S
       =20000N^{20}\mathcal S\le H\mathcal S.
\]

Also $m\le12N^4\le H$. This proves (2). The forest change of
variables preserves Haar exactly and fixes the two boundary links $U,V$,
by the checked predecessor. No determinant or orbit volume is inserted.
End proof.

**PROVED (Lemma T).** Let $Q(A)=\tfrac12\|CA\|^2$ be the quadratic
Taylor term in the slice, with three colour copies. Then

\[
 |A|^2/H\le Q(A)\le12|A|^2,\qquad
 |\mathcal S(A)-Q(A)|\le16|A|^3.
 \tag{3}
\]

The first lower bound follows by putting $tA$ into (2), dividing by
$t^2$, and letting $t\to0$. For the upper bound, each plaquette
has at most four terms and each link meets six plaquettes. Cauchy–Schwarz
gives $\|CA\|^2\le24|A|^2$.

For the remainder, differentiate a plaquette's four exponential factors
along $tA$. Their unitary norms are one for real $t$; the third
derivative of the normalized trace is bounded by
$(\sum_{e\in p}|A_e|)^3$. Taylor's integral remainder, followed by
$(\sum_{1}^{4}a_i)^3\le16\sum_1^4a_i^3$, bounds the sum by
$(16\cdot6/6)\sum_e|A_e|^3\le16|A|^3$.
The constant and linear terms vanish. The quadratic term is $Q$,
with the normalization already checked in the predecessor. End proof.

## 3. Uniform normalized moments in a slow-growth regime

**PROVED (Lemma M).** Suppose $\beta\ge H^{100}$. In principal
coordinates put $Y=\sqrt\beta A$, extend the Wilson density by zero
outside the product of balls $|Y_e|<\pi\sqrt\beta$, and omit its
constant Haar factors. The two unnormalized densities are

\[
 w(Y)=e^{-\beta\mathcal S(Y/\sqrt\beta)}j(Y/\sqrt\beta),\quad
 g(Y)=e^{-Q(Y)},\quad
 j(A)=\prod_e\left(\frac{\sin|A_e|}{|A_e|}\right)^2.
\]

Let $\mu_w,\mu_g$ be their normalized measures. For every measurable
function $F$ with $|F(Y)|\le1+|Y|^4$,

\[
 |\mu_w(F)-\mu_g(F)|\le H^{-17}.
 \tag{4}
\]

*Hand proof.* Set $R=\beta^{1/12}$. On $|Y|\le R$, every
$|A_e|\le\beta^{-5/12}\le1$. The elementary estimates
$\sin a/a\ge1-a^2/6$ and
$\log(1-t)\ge-2t$ for $0\le t\le1/2$ imply
$e^{-|A|^2}\le j(A)\le1$. Equation (3) gives

\[
 |\log(w/g)|\le16\beta^{-1/4}+\beta^{-5/6}
                   \le17\beta^{-1/4}.
\]

Since $\beta\ge H^{100}$ and $H\ge2^{16}$, this implies
$|w/g-1|\le H^{-23}=:\epsilon$ on that ball. Use
$e^t-1\le2t$ for $0\le t\le1/2$, and $34\le H^2$.

For the complement, (2) and (3) give $w,g\le e^{-|Y|^2/H}$.
Write $G=\int g$. The upper bound on $Q$ gives
$G\ge(\pi/12)^{m/2}$. For either density, its tail divided by $G$,
weighted by $1+|Y|^4$, is at most

\[
 4H^4(24H)^{m/2}
       \exp[-\beta^{1/6}/(2H)]\le H^{-30}=:\tau.
 \tag{5}
\]

Here the full comparison integral is
$(2\pi H)^{m/2}[1+H^2m(m+2)]$, bounded using $m\le H$.
For the last inequality, the logarithm of its prefactor is at most
$2H^2$, using $\log H\le H$, $\log24<4$, and $H\ge2^{16}$.
The negative exponent is at most $-H^{15}/2$, since
$\beta^{1/6}\ge H^{16}$. Thus the total is at most
$-H^3\le-30\log H$. These deliberately loose integer comparisons
require no numerical integration.

The Gaussian covariance has norm at most $H/2$, by (3).
Consequently $\mu_g(1+|Y|^4)\le4H^4$. The integral difference for
such $F$, divided by $G$, is at most
$4\epsilon H^4+2\tau\le5H^{-19}$.
Also $|\int w/G-1|\le\epsilon+2\tau\le2H^{-23}$.
Dividing by this normalizer bounds the expectation difference by
$26H^{-19}\le H^{-17}$. This proves (4). End proof.

**PROVED (Corollary M1).** For $e=U,V$, define

\[
 q_e=\beta(1-x(U_e)),\qquad q_e^0=|Y_e|^2/2.
\]

The first moments, the two individual second moments, and the joint
second moment of $q_U,q_V$ differ from the corresponding Gaussian
moments of $q_U^0,q_V^0$ by at most $2H^{-17}$.

Indeed $0\le q_e\le|Y_e|^2/2$ and
$|q_e-q_e^0|\le|Y_e|^4/(24\beta)$, by Taylor's formula for cosine.
Both a first readout and a product of two readouts are bounded by
$1+|Y|^4$, so (4) compares their measures. Within the Gaussian law,
the readout error in a product is at most $|Y|^6/(24\beta)$.
The Gaussian fourth and sixth moments are bounded by $3H^4$ and
$15H^6$, respectively: diagonalize its covariance, bound each
eigenvalue by $H/2$, and use the Gaussian norm moments
$m(m+2)$ and $m(m+2)(m+4)$. These moments follow by multiplying
the one-dimensional Gaussian integrals and differentiating their
finite product. The readout error is at most $H^{-94}\le H^{-17}$.

In the checked quadratic law, $1/6\le a,b\le1/2$, so the means of
$q_U^0,q_V^0$ are at most $3/4$. Subtracting the squared means or
the product of means costs at most twice the raw-moment error.
Thus each variance or covariance error is at most

\[
 6H^{-17}\le1/10000.
 \tag{6}
\]

These are exactly the three rescaled moment estimates required in $M$.
The bounds include the full compact Wilson law, with all fields integrated.

## 4. What growing blocks are defeated

**PROVED (Theorem P).** For the §8.1 product-box covers, every
$\beta\ge[2^{16}(32(L+1))^{20}]^{100}$ has an interacting face pair
whose invariant pair angle exceeds $1/64>1/160$, uniformly over the
ambient tori and allowed interval choices. At identity exterior, combine
(6) with the checked predecessor's inequality (7). At each such finite
$\beta,L$, continuity gives an open set of exterior configurations
with the same strict inequality. That set may depend on the pair,
cover, and $\beta$. Its Wilson marginal measure is positive. Hence
both the every-exterior and essential-supremum versions of PA_g fail.

**PROVED / explicit rate.** In particular, take

\[
 L(\beta)=\lfloor\beta^{1/4000}\rfloor,
 \qquad \beta\ge2^{30000}.
 \tag{7}
\]

Then $L\ge12$ and

\[
 H^{100}=2^{11600}(L+1)^{2000}
       \le2^{13600}\beta^{1/2}\le\beta.
\]

The same conclusion holds for every integer $12\le L\le
\beta^{1/4000}$ in that range. This is a quantified growing-block
obstruction, not merely a diagonal selection of unspecified thresholds.
The enormous constants are proof bounds, not predicted transitions.

**OPEN / limitation.** Theorem P does not cover arbitrary growth of $L$
with $\beta$. In particular it supplies no conclusion for exponential
growth in $\beta$, or for the prescribed physical-cutoff trajectory
without its rate satisfying the displayed inequality. It also says
nothing at $\beta=1$ or $\beta=2$. No order-one threshold or
block-size-independent weak-coupling threshold follows from this estimate.

## 5. A direct finite-beta restriction on the actual factor R

**PROVED / geometry of this second result.** Take equal partition
intervals of length $L\ge12$ in the §8.1 cover. Tori of side $12L$,
or larger multiples of $L$, suffice. Put $q=\lfloor2L/3\rfloor$.
After translating the pair, its first two coordinate intervals are

\[
 B=[-L,2q-L]\times[0,2q]\times K\times J,\qquad
 C=[0,2q]\times[-L,2q-L]\times K\times J.
 \tag{8}
\]

The common intervals $K,J$ are the cover's intervals in coordinates
3 and 4. Take the lower face of $K$, and a point strictly inside $J$,
for the predecessor's corner. The reflection
$\theta(x_1,x_2,x_3,x_4)=(x_2,x_1,x_3,x_4)$ interchanges $B,C$ and $U,V$.
All statements below concern this symmetric subclass. They do not assert
that an arbitrary unequal-interval pair has the required symmetry.

**PROVED / all torus sizes.** The witness can also be built for every
side $N_{\rm tor}\ge12L$, without divisibility. Write
$N_{\rm tor}=nL+r$, $n\ge12$, $0\le r<L$. In each coordinate take
$n-1$ partition intervals of length $L$ and one of length $L+r$.
There are at least eleven consecutive length-$L$ intervals. Choose the
two first-coordinate block endpoints and the two second-coordinate
block endpoints with all their three read partition intervals in
that run. Choose the other two blocks there as well. The resulting
pair is exactly (8), up to translation. Its conditional law therefore
has the same reflection. Only this pair, not the full cover, needs
the symmetry. These partitions are among the allowed §8.1 choices.

**PROVED (Lemma R, using the credited reflection construction).** For
this pair at identity exterior, the actual $R_\beta(U,V)$ of the
predecessor's (8) is a continuous positive semidefinite kernel on SU(2).
It is symmetric and invariant under simultaneous conjugation.

The reflection construction is already proved by Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors, at SA 2773–2795,
2820–2832, 2862–2883 (AM2, AM5). The index's chunk-03 neighbouring
rows and obligations for split geometry were read before those lines.
We use their positive Gram expansion; diagonal reflection positivity
itself is not a new result here. The following checks its application
after deleting the three particular plaquettes defining $R$.

Work on the unwrapped finite patch, with all other links fixed to $I$.
A straight periodic torus is not being cut into diagonal halves.
With height $x_1-x_2$, no link joins the two strict halves.
Only (1,2) plaquettes based at height zero meet both strict halves.
Each splits into reflected two-link paths $P_+,P_-$, and its factor is
$\exp[\beta s(P_+)\cdot s(P_-)]$. Here $s$ is the unit quaternion.
AM2 is its convergent Gram expansion with nonnegative coefficients.
The direction-3 and direction-4 links on the mirror are fixed pointwise.

Delete $p,p_U,p_V$. This deletes one crossing factor and a reflected
pair of half factors. The remaining crossing factors retain their Gram
expansions. Conditional on the mirror links, integrate all half variables
except $U,V$. Applying a test function to the two remaining arguments
therefore gives a sum of squares of half integrals. The mirror integral
has positive weight. This is exactly AM5 with these factors deleted;
it proves positive semidefiniteness of the remaining two-link kernel.
Continuity then gives positivity of every finite pointwise Gram matrix,
by testing with Haar approximate point masses.

That kernel equals a positive constant times $R_\beta$: it contains
the eight $U,V$-dependent plaquettes and every plaquette independent
of them, precisely as in the predecessor's definition. Symmetry follows
from $\theta$. Constant conjugation of all free links fixes the
exterior $I$ and gives simultaneous-conjugation invariance. End proof.

**PROVED / immediate consequence.** The predecessor's artificial
factor $e^{-\beta x(UV^{-1})}$ does not have this positive kernel
property for $\beta>0$. For example its quadratic form on a vector
quaternion coordinate is strictly negative, by the calculation below
with Haar marginals. Thus that earlier example correctly tests the
oscillation bound alone, but it cannot replace this actual symmetric $R$.

## 6. A block-size-free finite-beta angle bound

**PROVED (Lemma V).** Under the actual two-link marginal in §5, write

\[
 u=(u_0,u_1,u_2,u_3)=s(U),\quad v=s(V),\qquad
 a_1:=\mathbb E u_1^2=\mathbb E v_1^2\ge\frac1{4+6\beta}.
 \tag{9}
\]

The three vector-coordinate means are zero, by simultaneous conjugation. The
one-link conditional law, with all other links fixed, has density
$Z_\kappa^{-1}e^{\kappa h\cdot u}$ on $S^3$, with $|h|=1$
and $0\le\kappa\le6\beta$. This follows by summing the six staples;
each contributes a unit vector to a linear quaternion functional.

Here is the needed exact bound for that conditional law. Rotate $h$
to the scalar axis, and put

\[
 J_1(\kappa)=\int_{-1}^1e^{\kappa t}(1-t^2)^{1/2}\,dt,\qquad
 J_3(\kappa)=\int_{-1}^1e^{\kappa t}(1-t^2)^{3/2}\,dt.
\]

Two integrations by parts, of
$e^{\kappa t}(1-t^2)^{3/2}$ and
$t e^{\kappa t}(1-t^2)^{3/2}$, give

\[
 J_1'=\kappa J_3/3,\qquad 3J_1=4J_3+\kappa J_3'.
\]

Every transverse second moment equals
$J_3/(3J_1)=1/(4+\kappa b)$, where
$b=J_3'/J_3\in[0,1]$. Positivity of $b$ follows by pairing
$t$ and $-t$ in its integral. The longitudinal second moment is
one minus three transverse moments, hence is no smaller than a
transverse moment. Every coordinate second moment, in every orientation
of $h$, is therefore at least $1/(4+\kappa)$.
At $\kappa=0$ all four moments are $1/4$. Averaging this pointwise
conditional bound proves (9), with $a_1\ge1/(4+6\beta)$. End proof.

**PROVED (Theorem R1).** Let $k_{UV}$ be the maximal correlation
between functions of $U$ and $V$ in this marginal. Uniformly in $L$,

\[
 k_{UV}\ge
 \frac{2t}{(4+6\beta)(e^{2t}+1)},\qquad 0<t\le\beta.
 \tag{10}
\]

This lower-bounds the invariant block-pair angle, since $U,V$ have
boundary endpoints and belong to the two exclusive link sets.

*Hand proof.* Denote the symmetric two-link density by $p(u,v)$,
and its common marginal probability by $m$. By Lemma R,

\[
 K_t(u,v):=e^{-t u\cdot v}p(u,v)
   =Z^{-1}e^{\beta(u_0+v_0)}
       e^{(\beta-t)u\cdot v}R_\beta(u,v)
 \tag{11}
\]

is positive semidefinite. Multiplication by the one-body factors
preserves positivity. The exponential factor has AM2's Gram expansion;
termwise multiplication by $R_\beta$ also preserves positivity.
In particular $p$ itself is positive semidefinite. Therefore, for any
real $h$,

\[
 C(h):=\mathbb E_p h(u)h(v)-m(h)^2\ge0,
 \qquad C(h)\le k_{UV}\operatorname{Var}_m h.
 \tag{12}
\]

The first assertion applies positivity to $h-m(h)$. For a word
$I=(i_1,\ldots,i_n)$ with letters in $\{0,1,2,3\}$, put
$h_I(u)=u_1\prod_{j=1}^n u_{i_j}$. Expand the exponential in the
quadratic form of (11) on $u_1$. Its independent-marginal part is

\[
 J_t=\int u_1v_1e^{-t u\cdot v}\,dm(u)dm(v)
             \le -t e^{-t}a_1^2.
 \tag{13}
\]

To verify the sign and constant, condition on $u_0=a,v_0=b$.
Conjugation invariance makes the vector directions uniform on $S^2$.
Write their lengths as $r,s$, and their dot product as $rsz$.
The random variable $z$ is uniform on $[-1,1]$. Rotation invariance
gives the vector-coordinate integral as

\[
 e^{-tab}\frac{rs}{3}\mathbb E_z[z e^{-trsz}]
 =-e^{-tab}\frac{rs}{3}\mathbb E_z[z\sinh(trsz)]
 \le-\frac{t e^{-t}}9 r^2s^2.
\]

Use $z\sinh(kz)\ge kz^2$, $\mathbb E z^2=1/3$, and
$m(r^2)=3a_1$. This proves (13).

The remaining terms in the expansion are
$\sum_n(-t)^n/n!\sum_{|I|=n}C(h_I)$.
Drop the nonpositive odd terms. By (12), the even terms are bounded by

\[
 k_{UV}\sum_{n\text{ even}}\frac{t^n}{n!}
       \sum_{|I|=n}m(h_I^2)
   =k_{UV}a_1\cosh t,
\]

because $\sum_{|I|=n}h_I(u)^2=u_1^2(\sum_{j=0}^3u_j^2)^n=u_1^2$.
All sums are absolutely integrable: the same identity and Cauchy–Schwarz
bound each summed absolute moment by $a_1$.
Positivity of $K_t$ now gives

\[
 0\le J_t+\sum_n\frac{(-t)^n}{n!}\sum_I C(h_I)
 \le-t e^{-t}a_1^2+k_{UV}a_1\cosh t.
\]

Divide by $a_1>0$, then use (9). This proves (10). End proof.

## 7. An order-one witness for every symmetric block size

**PROVED (Theorem R2).** For every integer $L\ge12$, every
$1/2\le\beta\le4$, and every symmetric pair (8), the invariant
block-pair angle exceeds $1/160$. This holds on a positive-measure
open set of exteriors and is independent of the torus size once the
patch and an exterior collar fit without identifications.

For $1\le\beta\le4$, choose $t=1$ in (10). Since $e<3$,

\[
 k_{UV}>\frac1{5(4+6\beta)}\ge\frac1{140}>\frac1{160}.
\]

For $1/2\le\beta\le1$, choose $t=\beta$. Then
$2\beta/(4+6\beta)\ge1/7$ and $e^{2\beta}+1<10$, giving
$k_{UV}>1/70$. The inequality $e<3$ follows directly from its
series and $n!\ge2^{n-1}$, strictly for $n\ge3$.

**PROVED / finite witness family.** One of the 273 ordered-word
polynomials

\[
 h_I(u)=u_1\prod_{j=1}^{n}u_{i_j},\qquad n\in\{0,2,4\},
 \quad i_j\in\{0,1,2,3\},
 \tag{14}
\]

already has $\operatorname{Corr}(h_I(U),h_I(V))>1/160$.
No eigenfunction or numerical search is required to choose this family.

Suppose otherwise. In the proof of (10), set $t=\min(\beta,1)$.
Bound the even $n=0,2,4$ covariance terms by their assumed $1/160$
times the second moments. Bound every higher even covariance by its
second moment, using Cauchy–Schwarz. Their total is at most

\[
 a_1\left(\frac{37}{3840}+\frac7{4950}\right)
 <\frac{2a_1}{175}<\frac{a_1}{84}.
 \tag{15}
\]

Here $\sum_{n\ge6,\ n\text{ even}}1/n!\le
(1/720)/(1-1/56)=7/4950$; successive even-term ratios are at most
$1/56$. Also $37/3840<1/100$, $7/4950<1/700$, and $168<175$.
For $1\le\beta\le4$, $t e^{-t}a_1>1/84$, by $a_1\ge1/28$.
For $1/2\le\beta\le1$, it exceeds $1/60$, by $a_1\ge1/10$.
Thus (13) and (15) make the positive quadratic form strictly negative.
This contradiction proves the finite witness claim. Each monomial is
nonconstant and has positive variance under the positive marginal density.

**PROVED / gauge and exterior quantifiers.** All functions in (14) are
invariant under the interior gauges in PA_g: both endpoints of $U,V$
are boundary vertices. They are thus admissible without any further repair.
They can also be realized by fully gauge-invariant functions, if required.

Orient the one-free-link plaquette loops with bases $z,w$ so their
holonomies at identity exterior are $U,V$. Write $a_3=\min K$ and
let $t$ be the corner's fourth coordinate. Take three (1,2) plaquettes
based at $(-2,-2,a_3-3,t+3j)$, $j=1,2,3$. They are disjoint and
exterior on the stated tori. Set each first direction-1 link to
$-i\sigma_j$, and every other exterior link to $I$. Reach these bases
from $z,w$ through the exterior layer $x_3=a_3-2$, descending at the
last vertex. These paths avoid the three modified links. Traversing
each plaquette and returning along that path gives the transported
holonomies $H_j^z,H_j^w=-i\sigma_j$.
No changed link belongs to a plaquette touching the patch, so its
conditional law is exactly the law already used above.

Let $F_0=x(W_U)$, $F_j=x(H_j^zW_U)$, where $W_U$ is the based
plaquette holonomy. These are traces of closed loops and equal the four
coordinates $u_j$ at this exterior. The corresponding $G_j$ based
at $w$ equal $v_j$. Products $F_1\prod F_{i_j}$ and
$G_1\prod G_{i_j}$ are fully gauge invariant, and use only $U$ or
$V$, respectively, plus exterior links. This realizes (14) in the
two exclusive algebras with fully gauge-invariant tests.

For each finite $\beta,L$, choose a witness whose correlation is
strictly above the threshold. Its moments and positive variances depend
continuously on the finitely many exterior links read. Therefore the
same strict inequality holds on an open exterior neighbourhood of
positive Wilson marginal measure. No neighbourhood uniform in $\beta,L$
is asserted. This proves both exterior-quantifier versions. End proof.

**OPEN / distinction.** R2 is an obstruction using a finite family of
corner-link polynomials, or their decorated Wilson-loop realizations.
It does not prove that the two elementary traces $x(p_U),x(p_V)$
themselves exceed the threshold at these finite couplings. It also does
not prove R2 for an asymmetric cover that excludes every symmetric pair.

## 8. The direct R estimate extends to every weak-coupling growth rate

**PROVED (Lemma I: the inverse transverse moment).** In the same actual
two-link law, write $b=(u_1,u_2,u_3)$, $r=|b|$, and

\[
 M:=\mathbb E(r^{-2})\le2+6\beta.
 \tag{16}
\]

Values on $r=0$ may be defined arbitrarily; that set has measure zero.
This estimate is uniform in every patch size and exterior configuration.
The coordinate axis defining $r$ is fixed in advance.

*Hand proof.* It suffices to bound the one-link conditional law
$e^{\kappa h\cdot u}/Z_\kappa$, with $\kappa\le6\beta$, as in
Lemma V. The expectation of $1/(1-u_0^2)$ is largest when
$h=\pm e_0$. To prove this without a rearrangement assumption, expand

\[
 (1-u_0^2)^{-1}=\sum_{j\ge0}u_0^{2j},\qquad
 \cosh(\kappa h\cdot u)=\sum_{k\ge0}
                       \frac{\kappa^{2k}(h\cdot u)^{2k}}{(2k)!}.
\]

The odd part of the exponential integrates to zero. Each spherical
moment $\int u_0^{2j}(h\cdot u)^{2k}du$ is a polynomial in $h_0^2$
with nonnegative coefficients. Here is a direct verification. For a
standard four-dimensional Gaussian $G=RU$, polar coordinates make
$R,U$ independent, with $U$ Haar on $S^3$. Its joint generating
function in $G_0,h\cdot G$ is
$\exp(s^2/2)\exp(t^2/2)\exp(h_0st)$.
The coefficient of $s^{2j}t^{2k}$ contains only even powers of $h_0$,
with nonnegative coefficients. Divide the resulting Gaussian moment
by the positive radial moment $\mathbb E R^{2j+2k}$.
Thus every term is maximized at $|h_0|=1$. Monotone convergence
handles both series, and $Z_\kappa$ is independent of the direction
of $h$.

For the aligned direction define
$J_{-1}=\int_{-1}^1e^{\kappa t}(1-t^2)^{-1/2}dt$, with $J_1$
as in §6. Integrating the derivative of
$t\sqrt{1-t^2}e^{\kappa t}$ gives

\[
 J_{-1}=2J_1+\kappa J_1',\qquad
 \frac{J_{-1}}{J_1}=2+\kappa\frac{J_1'}{J_1}\le2+\kappa.
\]

The integrals converge at both endpoints, and $|J_1'/J_1|\le1$.
Averaging over the other links proves (16). End proof.

**PROVED (Lemma W: angular identity with a sign).** Put
$c=(v_1,v_2,v_3)$, $s=|c|$, $n=b/r$, $n'=c/s$. Then

\[
 \mathbb E\frac{b\cdot c}{r^2s^2}
       \ge\frac\beta2\mathbb E[1-(n\cdot n')^2].
 \tag{17}
\]

*Hand proof.* Let $L_1,L_2,L_3$ generate the usual rotations of the
three vector coordinates, fixing $u_0$, and let
$\Delta=\sum_iL_i^2$. Simultaneous-conjugation invariance of the
actual $R_\beta$ gives

\[
 -\Delta_uR_\beta=\sum_i L_i^uL_i^vR_\beta.
 \tag{18}
\]

The kernel on the right is positive semidefinite. Indeed the mixed
derivative for one generator is the limit of the positive Gram kernels
formed from simultaneous difference quotients in both arguments of
$R_\beta$. Explicitly use coefficients $a_j/\delta,-a_j/\delta$
at the rotated and original arguments, respectively. Smoothness of the
finite compact integral defining $R_\beta$ justifies the limit.
Summing over the three generators preserves positivity.

Multiply (18) pointwise by the positive Gram kernel
$e^{\beta u\cdot v}$. AM2, or its finite partial sums and their
limit, shows that this product is positive semidefinite. For any bounded
real radial $f=f(u_0)$, its quadratic form on $e^{\beta u_0}f(u_0)$
is therefore nonnegative. Integrate by parts in $u$ with Haar measure.
The radial factors are annihilated by every $L_i$, and

\[
 \Delta_u(b\cdot c)=-2b\cdot c,\qquad
 \sum_i[L_i^u(b\cdot c)]^2=r^2s^2-(b\cdot c)^2.
\]

It follows, after dividing by the positive two-link normalizer, that

\[
 2\beta\mathbb E[f(u_0)f(v_0)b\cdot c]
 \ge\beta^2\mathbb E[f(u_0)f(v_0)
                         (r^2s^2-(b\cdot c)^2)].
\]

Choose $f=(r^2+\epsilon)^{-1}$ and let $\epsilon\downarrow0$.
The right integrand is bounded by one after removing its $\beta^2$.
The left is bounded by $1/(rs)\le(r^{-2}+s^{-2})/2$, integrable
by (16). Dominated convergence proves (17). No differentiation of a
singular radial function was used. End proof.

**PROVED (Theorem R3: a threshold uniform in block size).** On the
symmetric cover family (8), for every $\beta>0$ and every $L\ge12$,

\[
 k_{UV}\ge\frac{\beta}{6+19\beta}.
 \tag{19}
\]

In particular PA_g fails whenever $\beta>2/47$, uniformly in $L$.
For $\beta\ge1/2$, a fixed family of twelve bounded continuous
corner functions, specified below, has a member with correlation
greater than $1/32>1/160$.

*Hand proof.* Define three $L^2$ functions $A_i=b_i/r^2$ and nine
bounded functions $B_{ij}=n_i n_j$. The common marginal is conjugation
invariant. Consequently

\[
 m(A_i)=0,\quad \sum_i\operatorname{Var}_m A_i=M,\qquad
 m(B_{ij})=\delta_{ij}/3,\quad
 \sum_{i,j}\operatorname{Var}_m B_{ij}=2/3.
\]

For any upper bound $k$ on their twelve same-function correlations,
the definition of correlation gives

\[
 \mathbb E\frac{b\cdot c}{r^2s^2}\le kM,\qquad
 \mathbb E(n\cdot n')^2\le\frac13+\frac{2k}{3}.
\]

Equation (17) implies $kM\ge\beta(1-k)/3$. Hence

\[
 k\ge\frac{\beta}{3M+\beta}\ge\frac{\beta}{6+19\beta}.
\]

This proves more than (19): one of those twelve functions attains at
least the displayed bound. Their variances are positive. For $A_i$
they equal $M/3\ge1/3$. For $B_{ij}$ they equal $1/15$ off the
diagonal and $4/45$ on it. The latter numbers follow by integrating
uniform directions on $S^2$: $m(n_i^4)=1/5$ and
$m(n_i^2n_j^2)=1/15$ for $i\ne j$.
The first is the integral of $t^4$ under the uniform law on $[-1,1]$;
the second follows by expanding $(n_1^2+n_2^2+n_3^2)^2=1$.
Finally $160\beta>6+19\beta$ is exactly $\beta>2/47$.
End proof of the norm bound.

**PROVED / bounded witness and uniform approximation.** For
$\beta\ge1/2$, set

\[
 \epsilon=2^{-160}e^{-48\beta}(1+\beta)^{-8},\qquad
 A_i^\epsilon=\frac{b_i}{r^2+\epsilon},\qquad
 B_{ij}^\epsilon=\frac{b_i b_j}{r^2+\epsilon}.
 \tag{20}
\]

At least one of these twelve functions has pair correlation $>1/32$,
uniformly in $L$. The following bounds justify that statement with an
explicit $\epsilon$, rather than an unquantified truncation.

A one-link conditional density relative to Haar is at most $e^{12\beta}$,
by the six-plaquette oscillation bound. Its marginal has the same upper
bound. The squared Haar $L^2$ error for each function in (20), against
its unregularized version, is at most $8\sqrt\epsilon$. For $A_i$
bound the squared integrand by

\[
 \frac{\epsilon^2}{r^2(r^2+\epsilon)^2}.
\]

Haar's angle density is $(2/\pi)\sin^2\theta\,d\theta$.
Reflect about $\pi/2$, use $\sin\theta\ge\theta/2$, and then put
$\theta=2\sqrt\epsilon t$. The remaining integral of
$(1+t^2)^{-2}$ over $[0,\infty)$ is at most two, by splitting
at one. This gives $8\sqrt\epsilon$. For $B_{ij}$ the same
bound holds since its error squared is no larger than that integrand.
Thus each marginal $L^2$ error is at most

\[
 \delta=3e^{6\beta}\epsilon^{1/4}<2^{-38}.
\]

Centering is an orthogonal projection, so it does not increase this
error. If two nonzero centered functions differ by at most $\delta$,
their normalized vectors differ by at most $2\delta/\sigma$, where
$\sigma$ is the first norm. Here $\sigma\ge1/\sqrt{15}$.
Consequently their same-function pair correlations differ by less than
$16\delta<2^{-34}$. Equation (19) is at least $1/31$ for
$\beta\ge1/2$, and $1/31-2^{-34}>1/32$. This proves the claim.

**PROVED / fully invariant realization and exterior measure.** Replace
the quaternion coordinates in (20) by the four decorated loop traces
constructed in §7. Their denominators stay positive. They are bounded,
continuous and fully gauge invariant, with $U$-only or $V$-only free
dependence. They agree with (20) at the specified exterior, which leaves
the conditional action unchanged. The strict margin $>1/32$ persists
on a positive-measure open exterior neighbourhood for each $\beta,L$.
For $2/47<\beta<1/2$, the same conclusion above $1/160$ follows by
taking a sufficiently small $\epsilon$; no uniform choice is needed
there. This establishes both versions of the exterior quantifier.
Letting the approximation error tend to zero also bounds the essential
supremum of the fibre angles below by (19). No single exterior
neighbourhood attaining that exact bound is required.

## 9. Rates, scope, and final checkpoint

**PROVED / growing-block decision for the witness class.** Let $L(\beta)$
be any integer-valued function with $L(\beta)\ge12$, with no upper
growth restriction. For each $\beta$, use the equal-interval §8.1
cover on a torus of side $12L(\beta)$, or a larger multiple of
$L(\beta)$. Alternatively, the one-remainder construction in §5 gives
the same symmetric witness on every torus side at least $12L(\beta)$.
These are admitted tori and covers. Theorem R3 defeats
PA_g for every $\beta>2/47$. This includes polynomial, exponential,
and faster growing block sizes. For a concrete exponential rate
take $L(\beta)=\lceil e^{\beta}\rceil$ once it is at least twelve;
the same bound holds for $\lceil e^{c\beta}\rceil$ with any fixed
$c>0$. A prescribed trajectory with $\beta_h\to\infty$ and arbitrary
$L_h=\lceil R/h\rceil\to\infty$ is also defeated on this cover family.
No asymptotic-freedom relation is needed to make this last deduction.

**PROVED / quantifier boundary.** This is a witness for every growth
rate within the symmetric product-box family (8). It refutes a PA_g
claim uniform over the entire §8.1 class, since that class includes
these covers. It does not prove that every possible unequal-interval
cover fails at large $L$. A proposal that deliberately excludes
every symmetric pair, changes link assignment, changes boundary gauge
invariance, or uses larger groups of blocks is not refuted by R3.
Such a proposal needs a new estimate; its validity is OPEN here.

**PROVED / what each requested obligation yielded.** (M) now has the
explicit uniform slow-growth estimate (1)–(7), on all §8.1 interval
choices. The unrestricted version of that rescaled-moment estimate
remains OPEN. (R) has the actual-kernel positivity and angular estimate
(16)–(19), with no small-field truncation and no dependence on $L$,
on the symmetric family. This second route supplies the growing-block
witness even when the first route's size bound fails.

**ARGUED / failed routes retained.** Unquantified fixed-patch Laplace
convergence did not permit growing $L$; §§2–4 replace that step only
in the stated slow regime. The scalar oscillation bound on $R$ did
not control its sign; §5 uses its actual reflection Gram structure.
The unweighted inverse-kernel bound (10) decays at large $\beta$;
the inverse transverse moment and radial weighting in §8 remove that
loss. No Wilson association or monotonicity inequality was assumed.

**ARGUED / check request and provenance.** Check Lemmas G, M, R, I, W
and Theorem R3, especially the deleted-plaquette reflection geometry,
the sign in (18), the singular-weight limit in (17), and the exact
cover quantifier. The fixed-beta polynomial argument in §§6–7 supplies
a separate hand calculation at order-one coupling, but is not an
independent review. No numerical run was used. The elementary trace
correlation at unrestricted growth remains OPEN; the proved witness is
the larger admissible corner function family. No mass gap is proved
or refuted, no audit was run, and no scientific status is granted.

RESULT: PROVED by hand, pending independent check: PA_g fails for the equal-interval symmetric product-box covers at every growth rate L(beta), with invariant pair angle at least beta/(6+19 beta), above 1/160 for beta>2/47; an explicit bounded fully gauge-invariant witness family works for beta>=1/2. The rescaled-moment obligation is also proved when beta>=[2^16(32(L+1))^20]^100. OPEN: unrestricted elementary-trace moments and cover classes excluding every symmetric pair.
