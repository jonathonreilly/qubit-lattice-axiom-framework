# Repo search

**READ.** This task starts at `612d615f60e504defbd69c3ed08d328923b851c2`.
`prior/gap-kanazawa-astra.md` is absent. The lead's November 8 digest
concerns ultraviolet suppliers, not this infrared comparison. Row 800 names
no additional outside-lane hit. Row 797 supplies the relevant prior search.
Its common-matching diagnosis and order-one mismatch calculation are reused.

**READ.** I refreshed main and PRs 10114, 10133, 10134 and 10141.
The target-name search (`Kanazawa|Tomboulis|Migdal.Kadanoff`) gives no
outside-lane hits on main, 10134 or 10141. On 10114/10133 it finds the
older soft-route toy and its literature diagnosis. I read
`agents/ym4d-proof/checks/review_massgap_block_literature.md:100–128`
and `PROOF.md:5755–5773`, under `.claude/science/toe-ruleset-20261021/`.
The former already separates bounding flow from common matching; the latter
is explicitly an approximate-map diagnostic. Neither supplies a mismatch
bound. Credit their Codex authors; no toy numerics are used.

**READ.** The local open registry, open-core and l17c searches reveal no
other owner of the Kanazawa mismatch problem. The assigned row is 800.
Rows 789, 793 and 796 concern group algebra and transports; row 797 is the
completed reading, and row 799 checks that reading. Those tasks are not
repeated here. The SA outline index and CA-I 4.12–4.19 index have no entry
under the three target names. Outline 581–602, read through chunk-01 and
obligations, separates a mass gap from scalar clustering. No claim of an
exhaustive absence theorem for CA-I is made.

# The Kanazawa mismatch as a signed twist response

Author: Codex gpt-6-astra max; 2026-11-12; FINISH row 800.
Research text, not an audit; this grants no status. **PROVED** means a hand
argument below, not an independent check. Other labels are **READ**,
**ARGUED**, **GUIDE**, and **OPEN**. No computation discharges a statement.

Credit Takuya Kanazawa for the representation; E. T. Tomboulis for the
interpolation framework; and the named lane authors for the reused results.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, for the indexed outline/account material. No Balaban estimate
is imported.

## Checkpoint

**PROVED / OPEN, final checkpoint.** Equations (K2)–(K7) express the
mismatch through the signed twist response and retain the affine factor
`1+R`. The coarse lemma and inverse theorem (K11)–(K18) extend the
representation to the crossed magnetic pairs, with a controlled endpoint.
They use the named existing polymer and transfer inputs. The fine response
estimate (K-RESP) below is open after the four attempts in §4. No (FQ),
(V), order-one seed, physical mass gap, or continuum assertion is proved.
The next decision is whether a coherent (LC) construction can compare the
*original* Wilson scores (K6)/(K23), beyond the excluded transport classes.
Sources are the pinned checkout, main `bb4ec020d5ada57c630dd89acc98a68397ade423`,
and Kanazawa v3. Downloads live only in the new directory
`/tmp/sa-gap-kanazawa-astra.zx1IR2`.

## 1. What the representation actually asserts

**READ.** Kanazawa, [0805.2742v3](https://arxiv.org/pdf/0805.2742v3),
Theorem 1 and (5)–(13), printed pp. 4–5, takes a positive linear
combination of center sectors. Its proof needs a volume-independent
positive lower bound for that combination divided by the untwisted
partition function. For SU(2), choosing both coefficients equal to `1/2`
gives `Z^+/Z` in `[1/2,1]`. Theorem 3, (38), p. 9, uses precisely this
choice. Dropping the identity sector would remove this supplied lower
bound. The theorem does not provide it for `Z^v/Z` alone.

**READ.** Theorem 1 permits a prescribed small coarse coefficient family;
it needs neither an MK orbit nor the potential-moving inequalities. Fix
its blocking depth and a positive interior coarse parameter. For large
compatible boxes its pressure derivative lets one solve a scalar inverse
problem. The constants and volume threshold can depend on these choices.
They are not stated uniformly as the parameter tends to zero or the
blocking depth grows with the box. Kanazawa's (16)–(19) already identifies
the surviving extensive error. That diagnosis is not new here.

## 2. Exact response and the weakest signed comparison

**PROVED, finite-volume identities.** For each admissible background pair,
let `R_f=Z_(f,m+v)/Z_(f,m)` and define R_c in the same way on the coarse
box. They lie in `(0,1]` by the transfer argument in §3. Write
\(Q_f=(1+R_f)/2\), \(Q_c(u)=(1+R_c(u))/2\), and
\(L_c(u)=\log Z_{c,m}(u)=N p_{c,m}(u)\), where **N counts coarse
plaquettes**. Suppose the positive-average representation holds:

\[
 Q_f=\frac{Z^+_{c,m}(\alpha)}{Z_{c,m}(\alpha_\Lambda)},
 \qquad
 D:=L_c(\alpha_\Lambda)-L_c(\alpha).
 \tag{K1}
\]

Then exactly

\[
 D=\log Q_c(\alpha)-\log Q_f,
 \qquad R_f=(1+R_c(\alpha))e^{-D}-1,
 \qquad
 D=N\int_\alpha^{\alpha_\Lambda}p'_{c,m}(u)\,du.
 \tag{K2}
\]

Insert `Z_c(alpha)` in the ratio in (K1), then take logarithms.
In particular, for `0<=epsilon<1+R_c`,

\[
 R_f\ge R_c-\epsilon
 \quad\Longleftrightarrow\quad
 D\le -\log\!\left(1-\frac{\epsilon}{1+R_c}\right).
 \tag{K3}
\]

Only an upper bound on D is needed. An absolute mismatch bound is stronger.
On an interval containing both parameters with `0<c<=p'_c<=C`, (K3) follows from
\((\alpha_\Lambda-\alpha)_+\le\epsilon/(2NC)\).
Indeed `D_+<=NC(delta_alpha)_+` and
\(-\log(1-\epsilon/(1+R_c))\ge\epsilon/2\).
Conversely (K3) forces
\((\alpha_\Lambda-\alpha)_+\le
[-\log(1-\epsilon/(1+R_c))]/(Nc)\).
Thus the needed scale is `epsilon/N`, rather than merely `1/N`.

**PROVED, exact twist response.** For any differentiable positive action
path, set

\[
 G_m(s)=\partial_s\log Z_m(s)-\partial_s\log Z_m^+(s)
       =-\partial_s\log Q_m(s).
 \tag{K4}
\]

For Tomboulis's coarse interpolation, the definitions of Appendix C are
`A=(partial_s log Z)/B`, `A^+=(partial_s log Z^+)/B`, with the same fixed
bulk constant B. Hence `G=B(A-A^+)`. This identification uses the
Appendix-C definitions read and reconstructed in row 797 §2.1; no new
Tomboulis source was downloaded here. It is a response of a *ratio*.

Use the Wilson coupling s from zero to beta on the fine lattice, and the
coarse coefficient u from zero to alpha. Both ratios equal one at zero.
Integrating (K4) gives the exact expression for the mismatch:

\[
 \boxed{\quad
 D=\int_0^\beta G_{f,m}(s)\,ds
       -\int_0^\alpha G_{c,m}(u)\,du .\quad}
 \tag{K5}
\]

The integrals are signed. Bounding their positive parts separately is
stronger than needed. A bound on `A-A^+` only on the small-coefficient
coarse path cannot control the first integral.

**PROVED, explicit Wilson observable.** Put
`H_m=sum_p eta_(m,p) tr(U_p)/2`,
`Y=sum_(p in Sigma) eta_(m,p) tr(U_p)/2`, and `W=exp(-2sY)`.
Expectations below use the actual normalized fine law at coupling s.
Differentiation under the finite compact integral gives

\[
 G_{f,m}(s)
 =\frac{R_m}{1+R_m}
    \left(\langle H_m\rangle_m
                 -\langle H_{m+v}\rangle_{m+v}\right)
 =\frac{2\langle WY\rangle_m-
                 \operatorname{Cov}_m(W,H_m)}{1+R_m}.
 \tag{K6}
\]

For the second equality use `R_m=<W>_m`,
`R'_m=<-2YW>_m+Cov_m(W,H_m)`, and `G=-R'/(1+R)`.
The action shift `-s N_f` in the lane convention cancels from every ratio.
The covariance with the **whole** action cannot be discarded.

**PROVED, global derivative of the mismatch branch.** If `L'_c>0` on
the inverse interval and alpha is fixed, differentiating (K2) gives

\[
 \frac{d\alpha_\Lambda}{d\beta}
       =\frac{G_{f,m}(\beta)}{N p'_{c,m}(\alpha_\Lambda)}.
 \tag{K7}
\]

At beta zero the branch starts at
`L_c(alpha_Lambda(0))=log Z_c^+(alpha)`, not at `alpha` in general.
The small, negative initial offset records the coarse twist deficit.
Setting it to zero would already change the exact representation.

**PROVED, consumer budgets.** Put `delta_c=1-R_c`. From (K2),

\[
 1-R_f\le\delta_c+2D_+.
 \tag{K8}
\]

For `D>=0` use `1-exp(-D)<=D`; for `D<0` use `R_f>=R_c`.
Here `Q_F=max_(m_2=0,i=3,4)(1-R_(f,m)(v_1i))/2` and S_ev is the
fine even-sector thermal sum; row 793 supplies `S_ev>=eta_*^a`.
Let `e_a=min{1/96,K(a) eta_*^(a/2)/4}`, the scale in row 793 (T2).
The sufficient allocation
`delta_c<=e_a/4`, `D_+<=e_a/8` gives
`1-R_f<=e_a/2`, hence `Q_F<1/192` and
`8Q_F<=K(a) sqrt(S_ev)` for every required pair and shape.
For (V), area-small bounds on `delta_c` and `D_+` imply
`F_f<=2(delta_c+2D_+)` once their sum is at most `1/2`.
These implications reuse row 797's logarithm estimate.

**OPEN, exact weakest scalar statement.** At a chosen coarse action,
insert (K5) into the upper bound (K3), with the allocated comparison error.
This is necessary and sufficient for that one-sided ratio comparison.
It is an exact reformulation, not an estimate that solves it.

## 3. Geometry: the mismatched representation extends to the crossed pairs

### 3.1 The positivity actually needed

**READ input, with its elementary extension.** The lane's magnetic transfer
construction is stated in `gap-means-max.md:146–162`. In a chosen time
frame, for spatial m and a temporal center twist v,

\[
 Z_m=\operatorname{Tr}T_m^t,\qquad
 Z_{m+v}=\operatorname{Tr}(T_m^t C_v),\qquad
 Z_m^+=\operatorname{Tr}\bigl(T_m^t(1+C_v)/2\bigr).
 \tag{K9}
\]

Here `T_m>=0`, and the commuting involution `C_v` has eigenvalues `+1,-1`.
Thus `Z_(m+v)<=Z_m`. The positive integrand gives `Z_(m+v)>0`.
Consequently `1/2<Q_m<=1`. This uses positivity in the selected time
direction, including all spatial m. It does not require positivity in
every coordinate direction.

**PROVED, scope of extension of (K9).** The same construction works for
the coarse plaquette weight

\[
 f_u(g)=1+2u\chi_{1/2}(g),\qquad 0<u<1/4.
 \tag{K10}
\]

It is strictly positive since `|chi_(1/2)|<=2`. Its character
coefficients are nonnegative. In temporal gauge the temporal kernel is
the product of one-link convolution kernels `f_u(UV^{-1})`.
Schur orthogonality makes each convolution positive semidefinite.
The positive spatial weight, including its fixed magnetic signs, enters
as multiplication on both sides. Gauge projection preserves positivity;
all these operations commute with the winding center flips. Splitting
the time seam then gives (K9). This verifies the only extra action
hypothesis needed here; it does not identify (K10) with a Wilson action.

### 3.2 A uniform coarse pressure derivative with the background retained

**READ input, reused rather than rebuilt.** The finite-polymer theorem
of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, is proved at outline 1150–1356. I read those lines after
chunk-01:118–146 and obligations:39–46. It gives a nonvanishing partition
function and a normally convergent connected logarithm under
`sum_(Y incompatible X) |z_Y| exp(a_Y)<=a_X`, with absolute logarithm
bound `sum_X |z_X| exp(a_X)`. Its tree cancellation and convergence proof
are existing inputs. Only the following actual-activity verification and
application to fixed backgrounds are supplied here.

**PROVED, coarse lemma using that input.** On a four-dimensional periodic
box with every side at least eight, let N count plaquettes. For every
closed center cocycle eta, let `Z_eta(u)` use (K10), and
`p_eta=N^(-1) log Z_eta`. There are explicit constants `r,alpha,c_*,C_*>0`,
independent of box and eta, such that

\[
 c_*\le p'_\eta(u)\le C_*
 \quad\text{on }J=[\alpha/2,3\alpha/2],
 \qquad
 |\log Z_\eta(u)-\log Z_{\eta'}(u)|
       \le 2N e^{-\ell^2}\quad(0\le u\le r),
 \tag{K11}
\]

where ell is the shortest side and eta, eta' are any closed cocycles.
The real logarithms are used. The construction and constants follow.

Expand the product of plaquette factors. Join two selected plaquettes
when they share a link. A polymer X is a connected nonempty plaquette
set, with activity

\[
 z_X(\eta,u)=u^{|X|}\int\prod_{p\in X}
                   2\chi_{1/2}(\eta_p U_p)\,dU.
 \tag{K12}
\]

Different components use disjoint links, so this is exactly the finite
hard-core polymer partition function. Activities can have either sign.
The degree of the plaquette adjacency graph is at most twenty.
There are at most `441^k` connected k-sets containing a specified
plaquette: fix a deterministic spanning tree and its depth-first walk;
the walk has `2(k-1)` steps, at most twenty choices at each step, and
its visited set recovers the k-set. Also `|z_X|<=(4|u|)^|X|`.

Choose

\[
 r=(4e^2\cdot441\cdot84)^{-1}.
 \tag{K13}
\]

For `|u|<=r`, the sum of `|z_X| exp(2|X|)` over polymers containing
one plaquette is at most `sum_(k>=1) 84^(-k)=1/83`.
An incompatible polymer meets the closed adjacency neighborhood of X,
which has at most `21|X|` plaquettes. Thus the polymer criterion holds
for the **weighted** activities `|z_X| exp(|X|)`, with `a_X=|X|`,
since `21|X|/83<|X|`. The cited theorem gives

\[
 \sum_{\text{connected lists}}\frac{|\phi|}{n!}
           \prod_i |z_{X_i}|\,e^{\sum_i|X_i|}\le N.
 \tag{K14}
\]

In particular `log Z_eta` is analytic on a neighborhood of `|u|<=r`
and bounded there by N. All estimates retain the original cocycle.

If an edge belongs to an odd number of plaquettes of X, changing that
link to its negative makes (K12) vanish. Every surviving X is therefore
a mod-two 2-cycle. Moreover
`z_X(eta,u)=(prod_(p in X) eta_p) z_X(1,u)`.
A change of closed cocycle can change this sign only if X has nonzero
homology. Such a cycle has at least `ell^2` plaquettes. Indeed, a
nonzero two-dimensional homology coordinate projects to the fundamental
cycle of a coordinate two-torus. Each of its plaquettes must have an
odd number of preimages, so there are at least the product of those
two side lengths. Contractible cycles pair trivially with every closed
cocycle. A cluster which changes sign therefore has total degree at
least `ell^2`. Removing its exponential weight in (K14) proves the
second bound of (K11), including the factor two for the difference.

For the derivative use the existing elementary-cube coefficient from
`gap-tomboulis-read.md` §2.4: no nonempty surface has fewer than six
plaquettes, and the six-plaquette contribution is the cube boundary.
Its weight is `4u^6`, and there are `4V` cubes, where `N=6V`.
Every closed cocycle has product one on these boundaries. Hence

\[
 p_\eta(u)=\tfrac83 u^6+\sum_{k\ge7}b_{k,\eta}u^k,
 \qquad |b_{k,\eta}|\le r^{-k}.
 \tag{K15}
\]

The coefficient bound is Cauchy's inequality applied to the analytic
logarithm just established. For `0<u<=r/2`,

\[
 |p'_\eta(u)-16u^5|
 \le\frac{u^6}{r^7}
          \sum_{j\ge0}(j+7)(u/r)^j
 \le16u^6/r^7.
 \tag{K16}
\]

Take `alpha=r^7/8`. On J we have `u<=r^7/2` and `u<=r/2`.
Thus `8u^5<=p'_eta(u)<=24u^5`. This proves (K11) with
`c_*=8(alpha/2)^5` and `C_*=24(3alpha/2)^5`. These constants are chosen
by inequalities, not by numerical evaluation. The very small alpha
is harmless for this existence result; it is not a physical coupling.

### 3.3 Global inverse construction, including crossed magnetic backgrounds

**PROVED.** Fix any fine Wilson box and its admissible pair `(m,m+v)`.
Let the coarse box carry the same two cohomology classes, with sides at
least eight and `N c_* alpha/2>log 2`. With alpha and J above there is
one `alpha_Lambda in J` such that (K1) holds, and

\[
 |\alpha_\Lambda-\alpha|\le\frac{\log2}{Nc_*}.
 \tag{K17}
\]

This is uniform in the fine Wilson coupling `beta>=0` and in the
spatial background m. At any finite beta the branch is real analytic.

*Proof.* Both positive-average ratios lie in `[1/2,1]` by (K9).
Set `D=log Q_c(alpha)-log Q_f`; then `|D|<=log 2`.
The function `L_c` has derivative at least `N c_*` on J.
Its change between alpha and either endpoint exceeds `log 2`.
The intermediate-value theorem gives a unique solution of
`L_c(alpha_Lambda)=L_c(alpha)+D`. Dividing its exponentiation gives
(K1); the derivative lower bound gives (K17). Analyticity follows
from the analytic finite Wilson integrals and the nonzero inverse
derivative. The interval traps the branch for every beta. QED.

**PROVED, dyadic specialization and endpoint size.** Fix `n>=1`, use
`b=2`, and take `a=2^k` with `k>=n+3`, `c,d in {a,2a}`.
The coarse box has sides `(a,a,c,d)/2^n`; its shortest side is
`ell=a/2^n`. Assign the same cohomology label: use the same coordinate
pair and its closed dual stack on the coarse torus. All prescribed
crossed backgrounds `m_2=0` and `v=v_13,v_14` are included in (K17).
For sufficiently large k its volume condition also holds. By (K11),

\[
 0\le F_{c,m}(v;\alpha)\le2N e^{-a^2/4^n},
 \qquad 1-R_{c,m}(v;\alpha)\le2N e^{-a^2/4^n}.
 \tag{K18}
\]

The fixed n makes this an area-small endpoint. The theorem covers
any sufficiently large compatible integer boxes, but the displayed
dyadic choice is enough to avoid all divisibility questions here.
It supplies no bound for the mismatch as k grows. Taking n to grow
with k would also change the endpoint exponent and is not done.

**ARGUED scope.** This proves the *representation* and a controlled
auxiliary endpoint for the crossed pairs, using Kanazawa's scalar
method. It does not extend Tomboulis's potential-moving inequalities
to those pairs. Neither an MK flow nor the checked small-beta Wilson
seed is needed: the auxiliary action (K10) is chosen directly.
It is not asserted to be an exact block action of the fine Wilson law.
The same fine ratio is encoded in its shifted denominator.

### 3.4 Why all-direction positivity is a different question

**READ.** For `(0,v)` the original `Z^+` reflection construction is
available on compatible dyadic boxes; row 797 §§1, 5.3 reads its proof
in Tomboulis. The scalar inverse proof above does not need that stronger
property. It needs (K9) in the one chosen time frame and (K11).

**PROVED, crossing-operator obstruction to an automatic extension.**
In a cut where both inserted twists are temporal, the sector multiplier
for the average is

\[
 (-1)^{\chi\cdot e_m}\,
           \frac{1+(-1)^{\chi\cdot e_v}}2.
 \tag{K19}
\]

It is negative on any surviving sector with
`chi.e_v=0`, `chi.e_m=1`. Projecting the v parity does not remove an
independent temporal parity of m. When the extra twist becomes spatial
under a change of time, the two spatial transfer operators also differ.
For example take the required pair `m=v_24`, `v=v_13` and use time 2.
Both terms retain the temporal insertion `C_4`; their spatial backgrounds
are 0 and `v_13`. The seam operator is

\[
 C_4\,\frac{T_0^t+T_{v_{13}}^t}{2}.
 \tag{K20}
\]

On its `C_4=-1` subspace its quadratic form is nonpositive, and is
strictly negative on a nonzero such state for the Wilson kernel at
positive coupling. The subspace contains a direction-4 Polyakov trace.
Strictness follows from strictly positive Wilson convolution eigenvalues,
positive invertible spatial multipliers and restriction to gauge-invariant
states. Thus this seam operator is not a positive operator. This is the
specific transfer-crossing form, not a denial of every possible site
reflection construction. A potential-moving proof would need another
valid reflection setup, or additional sector averaging with a new consumer.
The fixed-background inverse construction (K17) needs neither change.

## 4. What trying to bound the response gives

### 4.1 Coarse monotonicity and varying alpha do not supply a fine estimate

**PROVED.** Put `H_f=-log Q_f` and `H_c(u)=-log Q_c(u)`.
Equations (K2) and (K18) give, uniformly for `u in J`,

\[
 D(u)=H_f-H_c(u),\qquad
 0\le H_c(u)\le2N e^{-\ell^2},\qquad
 |D(u)-H_f|\le2N e^{-\ell^2}.
 \tag{K21}
\]

Here `H_c<=F_c`, since `(1+R_c)/2>=R_c`. Hence changing alpha
anywhere within this coarse interval can change D by at most
`2N exp(-ell^2)`. It cannot remove an order-one value of `H_f`.
More generally `partial_alpha D=-G_c=-B(A-A^+)` on the corresponding
coarse path. Integrating this derivative still requires the unknown
fine boundary value. Even a sign for `A-A^+` supplies no such value.

**PROVED, precise limitation of the inverse theorem.** Replace the fine
ratio Q_f by *any* prescribed number q in `[1/2,1]`. The proof of (K17)
works without change. It encodes that q in `alpha_Lambda`.
Thus the existence, compact continuation, and `1/N` bounds in (K17)
place no further restriction on q. This is a statement about the scalar
construction, not a counterexample to the actual Wilson estimate.

**ARGUED, first attempt ends here.** Monotonic coarse pressure and the
controlled coarse response establish the inverse and its conditioning.
They do not estimate the fine response. The new trapping interval proves
global continuation of the *mismatched* branch only. It does not restore
Tomboulis's common-parameter conclusion. By (K21), an exponentially small
mismatch in this construction is equivalent, up to the explicit coarse
error, to an exponentially small fine positive-average deficit.

### 4.2 A Wilson use of (LC) must control the full score

**READ input.** Row 789, `gap-ext-astra.md` §4.2, constructs
`[A_M,B_M]=C_M`, `C_M^M=-I`, with generator trace deficits at most
`pi/(2M)` and total commutator deficit at most `pi^2/(2M)`.
I use M here to distinguish its number of increments from the coarse
plaquette count N. This group construction and its binding tests are
already proved there; they are not new in this note.

**ARGUED, attempted insertion into (K6).** The small commutator cost
can guide control of the sheet term `2<WY>`. It gives no bound for
`Cov(W,H_m)`, whose second observable sums *every* plaquette.
Inserting its generators changes neighboring plaquettes and the
weighted law. Local gauge insertion is an exact dead end: both H_m
and W are gauge invariant, so gauge averaging fixes both observables
and their covariance. It cannot contract (K6).

**READ obstructions, at their actual scope.** Row 793,
`gap-trf-astra.md` §§3–4, proves a full-cost area lower bound for
transports with small final displacement after periodic gauge alignment.
It includes correlated uses of (LC) with word length `q/sqrt(M)->0`.
Row 796, `gap-seam-astra.md` §§2, 5, proves the analogous bound for
a center seam followed by a bounded-range update of one link colour,
including arbitrary correlated mixtures. These are bounds on
`F+D(nu||mu_twisted)`, not bounds on D in (K1).
The standalone D in (K1) is a signed log-normalizer mismatch;
`D(nu||mu)` denotes relative entropy.

**ARGUED, second attempt ends here.** These results exclude using those
transport families to estimate the full score at the requested scale.
They do not contradict (K17), which constructs no transport at all.
Large cumulative changes, successive changes of different colours, or a
direct comparison of the normalized fine responses remain outside their
exclusions. No such comparison follows from the small cost of C_M alone.

### 4.3 Commutator contraction leaves the needed normalizers free

**READ input.** Row 778, `gap-vortex-astra.md` §§4, 6–7, proves
Haar-commutator convolution norm `1/4` on center-odd SU(2) functions,
and its conditional Wilson bound `1-(3/4)exp(-24 beta)`.
Its stronger product-density comparison permits arbitrary nonnegative
endpoint data, but requires a common exterior weight. Its equation (15)
keeps the actual factors

\[
 Z_k=\int d\xi\ C_k(\xi)\prod_x z_{k,x}(\xi).
 \tag{K22}
\]

The common-factorization claim (CF) in that note remains open.
The commutator norm and this normalization identity are reused unchanged.

**PROVED, its exact relation to the response.** On a differentiable
Wilson path, (K22) gives

\[
 \partial_\beta\log Z_k
   =\mathbb E_{\nu_k}\!\left[
       \partial_\beta\log C_k+
                  \sum_x\partial_\beta\log z_{k,x}\right],
 \quad
 d\nu_k=Z_k^{-1}C_k\prod_x z_{k,x}\,d\xi.
 \tag{K23}
\]

This is differentiation of a finite positive integral. Combining the
two sector scores by (K6) gives the required G. The contraction of each
normalized conditional law `f_(k,x)/z_(k,x)` does not compare the
right sides of (K23).

**PROVED logical test; not a change to the Wilson model.** Multiplying
all unnormalized integrands in the twisted sector by `exp(-M beta)`
leaves every normalized conditional law and every commutator contraction
unchanged. It replaces `R_f` by `exp(-M beta)R_f`, still in `(0,1]`,
and changes its integrated response to
`-log[(1+exp(-M beta)R_f)/2]`. For any fixed positive beta this tends
to `log 2` as M tends to infinity. These modified weights are not the
prescribed pure Wilson family. The example proves only that normalized
conditional information, without the original normalizers, cannot imply
the required bound. Passing it through (K17) merely moves the change into
`alpha_Lambda`; nothing cancels it.

**ARGUED, third attempt ends here.** Serial center-odd contraction could
give an area estimate after a common-factor or weighted-score identity.
Neither an identification of that serial carrier nor the comparison of
(K23) is supplied by the existing contraction. The weaker target here
needs only the *integrated* score comparison (K5), not full (CF) for
arbitrary endpoint data. I did not construct even this weaker comparison.

### 4.4 Theorem R is a conditional selection tool

**READ input.** Claude Fable 5.2's R1–R3 and Theorem R,
`gap-means-max.md` §§4.1–4.6, were read with their proofs. They use the
even thermal sum S and the vacuum-energy defect Delta, with
`theta=1-exp(-Delta)(1+S)^(-2)`. They do not estimate these inputs.
The existing test `R_0(v)>64 theta` selects the magnetic light group
under the stated small-theta hypotheses (`gap-ext-astra.md` §3.3).

**PROVED translation of that test, not its supply.** When `64 theta<1`,
the representation would select that alternative if

\[
 D<\log\frac{1+R_c}{1+64\theta}.
 \tag{K24}
\]

This follows directly from (K2). The generic bound
`D<=log(2Q_c)=log(1+R_c)` has no uniform margin sufficient for (K24).
Nor does it prove small S or Delta. The selection theorem therefore
does not supply the exponentially small response needed by (FQ) or (V).
It can consume a future lower twist bound; using that consumption to
prove its own input would be circular.

## 5. Where the two comparison groups fail, and where they do not

**READ / PROVED consequences of the cited (LC).** In U(1) every
commutator equals one. In a fixed binary icosahedral subgroup of SU(2),
let `Delta_G=min_(g!=I)(1-tr(g)/2)>0`. For
`M>pi/(2 Delta_G)`, the (LC) generator bounds force `A_M=B_M=I`.
Their commutator cannot have Mth power `-I`. Thus (LC) fails at an
explicit algebraic step in both groups. Its use must survive into a
*Wilson-weighted* response estimate to distinguish the present target.

**READ / PROVED.** The commutator contraction fails in U(1), where its
operator is the identity on center-odd functions. It does **not** fail
in the binary icosahedral group. Here is a hand check of that latter
point, using the general Schur identity already proved in row 778:

\[
 \mathbb E_{A,B\text{ Haar on }G}\rho([A,B])=d_\rho^{-2}I.
 \tag{K25}
\]

The binary icosahedral group contains the quaternion subgroup generated
by i and j, whose commutator is `-I`. One explicit realization uses
the icosahedron vertices `(0,+/-1,+/-phi)`, `(+/-1,+/-phi,0)`,
`(+/-phi,0,+/-1)`, with `phi=(1+sqrt(5))/2`. Half-turns about the
three coordinate axes preserve that set; their lifts are i, j, k.
Every one-dimensional representation kills commutators, so it sends
`-I` to `+1`. Every center-odd irreducible therefore has dimension at
least two. The defining two-dimensional representation is irreducible:
i has two distinct eigenlines and j exchanges them. Thus (K25) gives
the same center-odd norm `1/4` for this finite group.

**PROVED consequence.** The finite-beta conditional minorization used in
row 778 also holds for normalized counting Haar measure: a bounded
Wilson exponent has the same oscillation bound. Therefore even that
conditional strict contraction does not by itself exclude the binary
icosahedral theory. The absent ingredient is the arbitrarily small
noncommuting deformation (LC) *with a bound on the original scores*.

**ARGUED scope of the tests.** Positivity of `(1+R)/2`, the inverse
calculus, and the coarse polymer argument are not SU(2) confinement
mechanisms. Kanazawa expressly includes U(1); the scalar inverse can
encode any q in `[1/2,1]`. Theorem R is likewise conditional algebra.
No false phase theorem for U(1) or the finite subgroup is inferred here.
A future proof based only on those common properties would still lack
the required group distinction. The specific group premise available
here is (LC), which fails exactly as above; its missing measure estimate
is the same one exposed by (K6) and (K23).

## 6. The remaining statement and source record

**OPEN, a sufficient form with all quantifiers (K-RESP).** Fix a compact
coupling interval `I subset (0,infinity)` and the witness `eta_*` of
row 793. Fix the depth n and the coarse action/alpha from §3 before
taking a large. There should be constants `C_1>0`, `p_1>=0`, `a_0`,
with `K(a)=C_1(1+a)^p_1`, such that, for every dyadic `a>=a_0`, every
`c,d in {a,2a}`, every `beta in I`, and every required crossed pair
`m_2=0`, `v=v_13` or `v_14`,

\[
 \left[\int_0^\beta
    \frac{2\langle W_sY\rangle_{m,s}
       -\operatorname{Cov}_{m,s}(W_s,H_m)}{1+R_m(s)}\,ds
            -\int_0^\alpha G_{c,m}(u)\,du\right]_+
 \le\frac18\min\{1/96,K(a)\eta_*^{a/2}/4\}.
 \tag{K-RESP}
\]

Everything inside the fine integral is at the original Wilson
normalization. This explicit sufficient allocation is slightly stronger
than the exact necessary-and-sufficient bound (K3)/(K5). For (V),
replace its right side by `C a^p exp(-sigma a^2)` and require the
full designated family of twists and frames. Neither form is established.

**PROVED implication.** For this fixed polynomial K, (K18) is eventually
smaller than the allocation `e_a/4`: its negative quadratic exponent
dominates the witness's negative linear exponent and all logarithmic
prefactors. Thus (K-RESP) implies the dyadic (FQ) bounds by (K8). The scalar
representation alone supplies only `|D|<=log 2`. The area-small coarse
error is already accounted for; the unresolved inequality is on the
fine signed response, not on the availability of a coarse parameter.
A theorem for every integer a would require (K-RESP) on those a too;
no propagation from dyadic a to all integers is silently asserted.

**ARGUED stopping point.** The methods tried were coarse inverse/response
control, a weighted use of coherent small commutators, serial conditional
commutator contraction, and the light-group selection inequality.
The first encodes any permitted ratio. The second meets the full action
and covariance term and the existing transport exclusions. The third
leaves (K23) unestimated. The fourth consumes an additional small spectral
input. None bounds (K-RESP). This is an open estimate, not an impossibility
result for other Wilson comparisons.

**READ, reproducible source record.** The fresh remote heads are:

| Ref | Revision |
|---|---|
| main | `bb4ec020d5ada57c630dd89acc98a68397ade423` |
| PR 10114 | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| PR 10133 | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| PR 10134 | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| PR 10141 | `fb99b4dddc7254e6124ac124887d58eeb3a77802` |

The three soft-route primary files named here and in row 797 are
byte-identical on PRs 10114 and 10133; `REVIEW_S2.md:106–125` was also
read. The full bounded search record is `repo-search.json` in the new
scratch directory. Matching historical snapshots were not counted as
independent work. The November 8 digest was read; its unrelated ultraviolet
hits were not imported as premises of this infrared argument.

**READ, source ranges.** The outline and CA-I were each fetched once at
`31a47c543775`. The outline reads used here are 581–602 and 1150–1356,
after their index rows and neighboring rows. CA-I was downloaded as
requested; no CA-I body passage was needed after its indexed target-name
search, and none is claimed as read. Kanazawa v3 was fetched once;
printed pp. 3–9 were read for (2)–(38), with the displayed Theorem 1
formula checked visually. His Appendix A and the original Tomboulis PDF
were not newly read; claims about them are attributed to the fully read
row-797 note. No Balaban paper or estimate was used.

**READ, verification limits.** PDF extraction, source search, hashes and
file bookkeeping are the only computations. `pdftotext` was unavailable;
the installed `pypdf`/PyMuPDF readers supplied text and the formula image.
No numerical run, machine enumeration, formal proof, or independent
checker was used. The arguments in this note need another-provider checking.
Only this output file was written in the checkout; no registry, audit,
queue, prior proof or standing was changed.

RESULT: OPEN — the exact signed-response criterion and a background-uniform mismatched representation with an area-small coarse endpoint are proved from the stated inputs; the missing SU(2) step is (K-RESP), a bound on the original Wilson twist score with all normalizers retained. The existing (LC), commutator contraction and Theorem R do not supply it.
