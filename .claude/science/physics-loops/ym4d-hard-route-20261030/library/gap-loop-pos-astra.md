# Repo search

The lane-specific `prior/gap-loop-pos-astra.md` is absent at
`73d1d443d0ff00cda59439035ff9af3f3bc510ad`. The lead's
`prior/repo-search-2026-11-08.md` concerns older RG targets. Its nearby
hit is PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–165` in the soft
route. I fetched that PR and read lines 1–165. The earlier Codex proof
gives a positive one-step loop correlation; it does not bound a
finite-size plaquette shift. It is not repeated here.

`prior/gap-lit-loops.md` supplies a more pertinent search. I opened its
main-branch hits at `a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc`:
`plaquette-bootstrap-closure-20260503/LITERATURE_BRIDGES.md`, and
`industrial-sdp-bootstrap-20260503/GOAL.md:1–65` with both block
certificates. These are under `.claude/science/physics-loops/`.
They concern numerical moment bounds and an absent loop-equation input.
They supply neither a hand certificate nor this volume comparison.
Their historical standing words are not adopted.

The immediate inputs are Claude Opus 5.5's `gap-loop-eq-opus.md`
and `gap-es1-opus.md`, with Codex's corrections in
`gap-loop-eq-check.md` and `gap-es1-opus-check.md`. Their Ward equations,
integrated-shift identities and Theorem V are reused. In particular,
neither a required radius near a/2 nor a positivity no-go survives
the check. `gap-mid-max.md:81–89` already proposes a local dual
certificate. Merely renaming that proposal would add nothing.

Searches of `open-registry.md`, `open-core.md`, `l17c.md` and
`port-map.md` found no owner of this loop-positivity target. Their
other entries named LOC concern RG label locality, a different object.
The queued electric-flux LOC and ES-1 lanes are not taken over here.

For Section 3, the additional prior input is Claude Fable 5.2's
`gap-seed-sc.md`, Theorem 2. Its nonzero wrapping-tube coefficient
is already proved; it is not recalculated here. I read its statement,
the cancellation argument and Section 4, with the relevant verdicts
in Claude Opus 5.5's `gap-seed-sc-check.md`. That check records its
same-provider limitation. The new use below is a lower bound on
the width allowed by local constraints, not a new tube count.

The outline and CA-I were each downloaded once at `31a47c543775`.
The full-read index was searched first, including chunk files,
`obligations.md` and `ca-4.12-4.19/`. Neighbouring rows read:
chunk 01:60–74, chunk 02:83–112, chunk 03:6–28, obligations:17–28.
The source reads were outline 588–599, 2195–2257, 2313–2336,
2773–2795. The positive one-bond coefficients (GL3), transfer trace
(GL8) and quaternion Gram expansion (AM2) are existing results.
The gap passage explicitly needs an additional spectral estimate.
No matching finite-size loop-positivity bound was located in these
indices. This bounded search is not a whole-account absence claim.
No CA-I theorem is imported.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for that framework. Credit Anderson–Kruczenski and
Kazakov–Zheng for the loop-moment bootstrap, and Makeenko–Migdal,
Chatterjee and Jafarov for the loop-equation methods, as documented
in `prior/gap-lit-loops.md`. No published numerical bracket is an input.

Author: Codex; assigned model and effort: gpt-6-astra max; FINISH row 760.
Research text, not an audit; grants no status. PROVED means a written
argument below, not an independent check. ARGUED, GUIDE and OPEN
retain their literal meanings. No computer-assisted proof is used.

## 1. Fixed conventions and the consumer

Use normalized Haar measure and the weight
`exp(s sum_p x_p)`, where `x_p = tr(U_p)/2`. Its transfer logarithm
is `e_hat(B)=e(B)+6s|B|` in the imported action convention.
The additive term cancels from every deficit. Write `w_L` for the
orientation-averaged plaquette in the infinite-time cylinder of
spatial side L. Do not impose exchange of time with a spatial axis.
For the even torus, use the signed insertion `w_ev^ins` of
`gap-loop-eq-check.md` (3.1), or its seam-free local representative.

**PROVED in the cited inputs.** At a lattice side a,

\[
 \delta=48a^4\int_0^\beta(w_a-w_{2a})\,ds,\qquad
 \log(1+\epsilon)=6a^4\int_0^\beta(w_{\rm ev}^{\rm ins}-w_a)\,ds.
\]

Both integrals are nonnegative. Their integrands have no asserted
pointwise sign. The target tolerances are respectively `10^(-7)`
and `log(1+10^(-7))`. Theorem V does not turn a short-loop lower
bound on a correlation into the required upper thermal-trace bound.

## 2. A finite Ward and positivity certificate

### 2.1 The loop size and the two input moments

**Definition.** Fix length 24 and support radius two, in lattice units.
For a positive oriented link e, read its six incident plaquettes as
`U_e B_i`, where each staple B_i is a path of length three back to
the starting point of e. Put

\[
 H_e=\sum_{i=1}^6 B_i,\quad
 h_e=\tfrac12\operatorname{tr}(U_eH_e),\quad
 u_e=\tfrac12\operatorname{tr}(H_eH_e^*),\quad
 v_e=u_e-h_e^2.
 \tag{2.1}
\]

The quaternion representation gives `0 <= u_e <= 36`,
`|h_e| <= 6`, and `v_e >= 0`. The plaquette orientations cause
no ambiguity because an SU(2) trace equals the trace of its inverse.
Define E to include a uniform average over the four link directions
and the finite torus anchors. On a cylinder, take the finite-time
limit of this average, or use translation invariance at one anchor.
There is no uniform probability measure on infinitely many anchors.
Set

\[
 M=E u_e,\qquad N=E u_e^2,\qquad m=E h_e=6\bar w.
 \tag{2.2}
\]

The last equality counts each plaquette four times among link stars.
It uses no exchange symmetry between time and space.

These are short-loop inputs. In fact

\[
 u_e=6+2\sum_{i<j}W(B_iB_j^{-1}),\qquad W(C)=\tfrac12\operatorname{tr}U_C.
 \tag{2.3}
\]

Thus M needs loops of length at most six. For N, base every loop
at the common endpoint of e and use
`2 W(A) W(B) = W(AB) + W(AB^(-1))`.
It needs loops of length at most twelve. Repeated use of that identity
expresses all certificate terms below as single traces of length at
most 24. All paths stay in the same link star. Length counts repeated
traversals; it is not the diameter of the support.

For `a >= 7`, the radius-two star and its plaquette margin embed in
both target cylinders and the even torus. The word-length ratio is
`24/a`; it is below one if `a >= 25`. The support radius is always
two, independently of a. No claim about the smallest viable seed is made.

For an electric twist, replace `B_i` by `sigma_i B_i` in (2.1).
Equivalently choose a local trivialization with the seam outside the
star. Products in (2.3) then carry the corresponding transported signs.
In the positive even mixture, average these chart moments with the
weights `q_k(s)` of the checked insertion formula. Equation (2.2)
then reads `m=6 w_ev^ins`, not the unsigned fixed-seam mean.

### 2.2 The certificate

**Theorem P (PROVED).** For every real `s >= 0`, in each of these
Wilson states, define

\[
\begin{split}
 L_s(M,N)&=\max\left\{
 0,\ \frac{sM}{4+6s},\ \frac{sM}{4+6s^2},\
 \frac{sM}{4}-\frac{s^3N}{96}\right\},\\
 U_s(M)&=\min\left\{6,\
 \frac{10sM}{20+\sqrt{400+60s^2M}}\right\}.
\end{split}
 \tag{2.4}
\]

Then

\[
             L_s(M,N)\ \le\ 6\bar w\ \le\ U_s(M).
 \tag{2.5}
\]

This holds at order-one coupling, with no smallness hypothesis on s.
The values at zero are zero. The proof uses seven polynomial Ward
tests and local positivity. It does not solve an infinite moment
hierarchy or use a numerical bootstrap.

**Proof.** Temporarily fix e and its exterior. With the checked
generators `t_j=i sigma_j`, the one-link identities are

\[
 \Delta_e h=-3h,\qquad
 \Gamma_e(h,h)=u-h^2=v,\qquad d_j u=0.
 \tag{2.6}
\]

For the second identity, right multiplication by `H/|H|` sends the
unit quaternion U to another unit quaternion. Its scalar coordinate
is `h/|H|`; the squared tangential gradient is `1-h^2/u`.
At `H=0` both sides vanish. This is also the Pauli completeness
identity used in `gap-loop-eq-check.md` Section 1.

Integration by parts applied to the vector field `F(h,u) grad h`
gives the finite polynomial identity

\[
 E\{v\partial_h F-3hF+svF\}=0.
 \tag{2.7}
\]

Equivalently take a polynomial primitive f with `partial_h f=F`
in `E(Delta_e f+s Gamma_e(f,h))=0`. Thus these are loop Ward
equations, including mixed and repeated passages. Linearity permits
averaging over e, orientations, and the positive twist mixture.
Finite-time limits preserve the identities for cylinder ground states.

For `F=v^k` and `F=h v^k`, respectively, (2.7) says

\[
\begin{split}
 (2k+3)E(hv^k)&=sE v^{k+1},\\
 (2k+4)E v^{k+1}+sE(hv^{k+1})&=(2k+3)E(uv^k).
\end{split}
 \tag{2.8}
\]

Only use `F=1,h,v,hv,v^2,uh,uv`. Put
`A_j=E v^j`, `B_1=E(uv)`, `B_2=E(uv^2)`.
The resulting identities are

\[
\begin{split}
 3m&=sA_1,\\
 4A_1+\frac{s^2}{5}A_2&=3M,\\
 6A_2+\frac{s^2}{7}A_3&=5B_1,\\
 4B_1+\frac{s^2}{5}B_2&=3N.
\end{split}
 \tag{2.9}
\]

For example, `F=v^2` gives `7E(hv^2)=sA_3`, and
`F=uv` gives `5E(uhv)=sB_2`. These justify both eliminations.
The largest term is `v^3`, of loop length at most 24.
This list fixes the truncation before any inequality is tested.

The 2-by-2 moment matrix of `1,v` is positive semidefinite, so
`A_2 >= A_1^2`. Equations (2.9) imply

\[
                  3s m^2+20m\le5sM.
 \tag{2.10}
\]

For `s>0`, the first identity gives `m>=0`. The positive root
of (2.10), in its rationalized form, is the second entry of U.
Also `m<=6`. At `s=0`, the first identity directly gives `m=0`.

For the lower bounds, (2.8) with `F=h` gives
`3M=4A_1+sE(hv)`. Since `(6-h)v>=0`,
`3M <= (4+6s)A_1`. This gives the first nonzero entry of L.
Next, nonnegativity in (2.9) gives

\[
 A_2\le\tfrac56 B_1\le30A_1,
 \qquad A_2\le\tfrac56 B_1\le\tfrac58N.
 \tag{2.11}
\]

The middle bound in the first chain is `u<=36`.
Substitution in `3M=4A_1+s^2A_2/5` gives the second entry.
Finally the first two identities of (2.9) give the exact equation

\[
                 m=\frac{sM}{4}-\frac{s^3A_2}{60}.
 \tag{2.12}
\]

Use `A_2<=5N/8` for the final entry of L. This proves (2.5).

All positivity used here has an explicit local origin. In quaternion
coordinates, `v=sum_j(d_jh)^2`,
`36-u=sum_{i<j}|B_i-B_j|^2`, and
`6-h=(1/2)sum_i|U_eB_i-I|^2`.
Hence `(36-u)v`, `(6-h)v`, `v^3` and `uv^2` are sums of
squares of local coordinate polynomials. Their contracted expressions
are the loop polynomials displayed above. Together with the Gram
matrix of `1,v`, these are a finite set of valid moment/localizing
constraints. No positive association of arbitrary plaquette monomials
is assumed. QED.

**PROVED consequence.** Positivity changes the useful bound: retaining
`A_2>=A_1^2` produces (2.10). The absolute row-sum count in the
earlier CR argument does not see that restriction. This does not prove
contraction of the full positive moment system. Temporal reflection
positivity may be added; Theorem P does not need it.

### 2.3 The promised finite-size inequality

**Corollary P-shift (PROVED).** Let `M_X(s),N_X(s)` be the two
moments (2.2) in state X. Write A for the cylinder of spatial side a,
B for the cylinder of spatial side 2a, and E for the even torus a^4.
For every `a>=7` and every finite `beta>=0`,

\[
\begin{split}
 0\le\delta
 &\le8a^4\int_0^\beta
    [U_s(M_A)-L_s(M_B,N_B)]\,ds,\\
 0\le\log(1+\epsilon)
 &\le a^4\int_0^\beta
    [U_s(M_E)-L_s(M_A,N_A)]\,ds.
\end{split}
 \tag{2.13}
\]

Apply (2.5) to the ordered pair in each integrand, then use Section 1.
This proves an upper bound for each seed number in terms of moments
of loops of length at most twelve. Its certificate uses length at
most 24. All constants and factors are displayed. The bound is not
asserted to reach either seed tolerance.

**OPEN, the exact sufficient one-sided tests for this certificate:**

\[
\begin{split}
 \int_0^\beta[U_s(M_A)-L_s(M_B,N_B)]\,ds
       &\le \frac{10^{-7}}{8a^4},\\
 \int_0^\beta[U_s(M_E)-L_s(M_A,N_A)]\,ds
       &\le \frac{\log(1+10^{-7})}{a^4}.
\end{split}
 \tag{P-small}
\]

These are sufficient, not equivalent, to ES. They use the actual
state moments, including twist signs. Replacing those moments by
uncertified numerical estimates would not prove either inequality.

## 3. A positive-width obstruction, with fixed support

### 3.1 Precisely which certificates are excluded

**Definition.** Fix an integer `r>=2` and `s>=0`. Let `K_r(s)` be
the set of all local moment functionals satisfying the following
constraints. The same result holds when any of them are omitted:

1. The SU(2) algebra and trace identities, normalization, and the
   translation, coordinate-reflection and spatial-permutation identities
   shared by the target states.
2. Every polynomial one-link Wilson Ward equation whose entire test
   and action stencil lie in a nonwrapping radius-r patch.
3. Ordinary positive moment matrices and the pointwise compact-group
   localizing inequalities in that patch.
4. Temporal reflection-positive Gram matrices whose complete reflected
   support lies in that patch.

All patch translates use the same local coordinates. Allow any word
length and any matrix order within the fixed support. Thus this list
contains every finite truncation of the listed constraints there.
It carries no volume label or condition saying that a functional
comes from the ground state of a specified spatial torus.
Write `p(omega)` for its orientation-averaged central plaquette.

A *separate-state local certificate* is a measurable integrable
function `b_a(s)` proved to satisfy

\[
 p(\omega)-p(\nu)\le b_a(s)
 \quad\hbox{for every }\omega,\nu\in K_r(s).
 \tag{3.1}
\]

The proposed error may depend on a, but the premises in `K_r(s)`
do not. Both orders of the two functionals are allowed. This is the
class of bounds obtained from two independent copies of the same
local constraints. It is not every use of loop equations.

### 3.2 Actual Wilson witnesses

**Theorem O (PROVED, using the existing Theorem 2).** For every
integer `r>=2` and every real interval `I=[b_0,b_1]` with
`0<=b_0<b_1<infinity`, there is a strictly positive number
`J_r(I)`, independent of a, such that every certificate (3.1) obeys

\[
                       \int_I b_a(s)\,ds\ \ge\ J_r(I)>0.
 \tag{3.2}
\]

In particular this holds for `I=[1,2]`. It is not a small-coupling-only
obstruction. No numerical lower estimate for `J_r([1,2])` is claimed.

**Proof.** Choose the even integer `n=2r+4`. For each real `s>=0`,
let `omega_n(s)` and `omega_2n(s)` be the ordinary Wilson measures
on the four-dimensional tori `n^4` and `(2n)^4`, restricted to the
patch. Both obey every constraint listed above.

Indeed the patch and every retained action stencil embed without
identifications. Haar integration gives its Ward identities. An actual
positive measure gives all ordinary/localizing matrices and SU(2)
identities. The tori have all the required symmetries. Their even
periods also give temporal reflection positivity. For a half-slab
insertion with boundary operator A, the transfer numerator is

\[
 \operatorname{Tr}(A^*T^vAT^u)
       =\|T^{v/2}AT^{u/2}\|_{\rm HS}^2\ge0.
 \tag{3.3}
\]

Use linear combinations of insertions for a Gram matrix. The unused
slabs supply the nonnegative integers u,v; the margin in n keeps
the reflected patch away from the other cut. This is the existing
positive Wilson transfer construction, as used in
`gap-loop-eq-check.md` Section 4. No even projection is needed for
these witnesses. They need not be the target states: they satisfy
exactly the premises which (3.1) is allowed to read.

Let `Z_n(s)` use the Section 1 normalization, and put

\[
 \Phi_n(s)=16\log Z_n(s)-\log Z_{2n}(s),\qquad
 f_n(s)=p(\omega_n(s))-p(\omega_{2n}(s)).
 \tag{3.4}
\]

Finite-volume differentiation gives

\[
                         \Phi_n'(s)=96n^4 f_n(s).
 \tag{3.5}
\]

The constant action terms cancel, so `Phi_n` is exactly the function
in `gap-seed-sc.md`, Theorem 2. Since `n>=5`, that theorem gives

\[
 \Phi_n(s)=192n^3\,4^{-4n}s^{4n}+O(s^{4n+1}),\qquad
 f_n(s)=8\,4^{-4n}s^{4n-1}+O(s^{4n}).
 \tag{3.6}
\]

The O-term here is an analytic remainder at fixed n. Thus
`f_n` is not identically zero. This uses the prior coefficient,
not a numerical estimate of a finite-size correction.

For completeness, analyticity continues along the whole real axis.
The action is bounded on each finite compact configuration space.
The exponential series therefore converges uniformly on every compact
complex s-set and defines an entire partition function. For real s,
its integrand is strictly positive, so `Z_n(s)>0`. At any such s,
continuity gives a complex neighbourhood with no zero. There the
logarithmic derivative is analytic. Consequently `f_n` is real
analytic on the connected real axis.

A nonzero real analytic function cannot vanish on an interval:
an accumulation of zeros forces every Taylor coefficient at an
interior accumulation point to vanish, and analytic continuation
then forces the function to vanish identically. Hence

\[
                       J_r(I):=\int_I|f_n(s)|\,ds>0.
 \tag{3.7}
\]

The integrand is continuous. It is nonzero somewhere inside I,
and stays bounded away from zero in a smaller interval there.
Apply (3.1) to the two witnesses in both orders. This gives
`b_a(s)>=|f_n(s)|`, which proves (3.2). QED.

**PROVED quantitative form near zero.** The fixed-n remainder in
(3.6) supplies some `eta_n>0` such that
`f_n(s)>=4*4^(-4n)*s^(4n-1)` for `0<s<=eta_n`.
Thus, for every `beta>0`,

\[
 J_r([0,\beta])\ge
    \frac1n\left(\frac{\min(\beta,\eta_n)}4\right)^{4n}>0.
 \tag{3.8}
\]

This is an existence-defined constant with a written order of choice.
No uniform estimate of `eta_n` as n grows is supplied.

### 3.3 Exact implication for the ES tolerance

**Corollary O-seed (PROVED).** Fix `r>=2`, `beta>0` and `tau>0`, and set
`J=J_r([0,beta])`. If an upper estimate for delta is obtained by
integrating (3.1) over the whole coupling path, it cannot prove
`delta<=tau` for any integer

\[
             a\ge2r+3,\qquad a>\left(\frac{\tau}{48J}\right)^{1/4}.
 \tag{3.9}
\]

The same method for the even sum cannot prove `epsilon<=tau` if

\[
             a\ge2r+3,\qquad
             a>\left(\frac{\log(1+\tau)}{6J}\right)^{1/4}.
 \tag{3.10}
\]

Proof: Section 1 multiplies the proposed integrals of `b_a` by
`48a^4` or `6a^4`. Theorem O bounds those integrals below by J.
Take `tau=10^(-7)` for the present seed. QED.

**PROVED scope and exclusions.** The quantifier is: *for every fixed
r and beta, all sufficiently large a defeat this certificate class*.
It is not: *for every a, every local certificate fails*. The theorem
allows r to be chosen as a function of a before a finite calculation.
It gives no rate for that choice and no requirement `r about a/2`.
It also allows an arbitrarily long word inside the fixed patch;
increasing moment order there alone does not remove these witnesses.

Volume-specific winding constraints, a joint relation between the two
states, and information selecting their actual global states are outside
(3.1). Signed cancellations along the coupling path also require
information beyond independent pointwise diameter bounds. Theorem O
does not exclude them. It excludes neither a hand certificate at one
chosen seed size nor a growing-support positivity bootstrap.

The correction to VB is therefore strengthened by actual, distinct
Wilson witnesses and a positive integral. No exponential finite-size
ansatz, uniqueness assumption or confinement claim is used.

## 4. U(1) test and what has not been obtained

**PROVED, the group-sensitive step.** For U(1), with the real cosine
trace and the same generator period, `Delta_e h=-h`, not `-3h`.
One still has `Gamma_e(h,h)=u-h^2` for the complex staple sum.
The analogues of (2.8) are therefore

\[
\begin{split}
 (2k+1)E(hv^k)&=sE v^{k+1},\\
 (2k+2)E v^{k+1}+sE(hv^{k+1})&=(2k+1)E(uv^k).
\end{split}
 \tag{4.1}
\]

They do not imply (2.9). In particular `m=sA_1` and
`2A_1+s^2A_2/3=M`, rather than the SU(2) equations.
The SU(2) trace identity alone would not distinguish the groups.
The Casimir and the resulting Ward coefficients do distinguish them.

Here is a hand check that using Theorem P unchanged for U(1) would
actually fail. On any untwisted torus with sides at least seven,
at `s=0` each plaquette angle is Haar. Distinct plaquette cosines
have zero covariance: integrate a link belonging to just one of the
two plaquettes. Thus `M(0)=6` and

\[
 \left.\frac{d}{ds}E_s h\right|_{s=0}
       =6 E_0\cos^2\theta=3.
 \tag{4.2}
\]

In `M(0)=6`, each off-diagonal staple product in (2.3) has a link
which occurs once, so its Haar mean vanishes. Finite-volume analyticity
now gives `m_U(1)(s)=3s+O(s^2)`. But the unmodified SU(2) upper
bound would be `U_s(M(s))=(3/2)s+O(s^2)`. It fails for all
sufficiently small positive s. Hence the SU(2) hypotheses used in
Theorem P are not satisfied by this comparison model.

This is precisely the valid T1–T3 test of `gap-crux-fp.md:270–288`.
A correct U(1) version with (4.1) remains possible. It proves no
seed without its own smallness input. No Coulomb-phase threshold,
photon estimate or numerical phase boundary is needed here.

**PROVED, the obstruction is compatible with the test.** Theorem O
asserts a restriction on a certificate class for actual SU(2), not
a gap. Its analytic argument would apply to any model with two such
positive finite-volume witnesses and a nonzero coefficient. It makes
no claim that an Abelian-compatible tool cannot work. It is fully
consistent with a small-coupling seed proved using growing patches
or explicit volume information.

**ARGUED assessment of the attempts.** The finite Ward system gives
both sides in (2.5); it does not estimate the actual moments in
P-small. Enlarging Gram matrices inside one fixed patch cannot make
the universal comparison arbitrarily precise, by Theorem O. This
does not decide a larger, preselected patch at one a. Using temporal
reflection positivity through `gap-loop-eq-opus.md` Lemma 3.1 gives
a lower bound on the thermal trace. That use supplies no upper bound.
Its proof is not repeated here; no general positivity no-go is inferred.

**OPEN.** Either prove P-small for some specified a and coupling
regime, or replace its local scalar bounds by a sharper hand
certificate with the needed integrated error. That certificate must
state its loop length, support radius, common state constraints and
any extra information relating the two actual volumes. Theorem O
does not supply the necessary radius or the certificate. Uniformity
under a cutoff-dependent effective action is also not proved:
Theorem P uses the exact Wilson drift `s grad h`, and an additional
blocked interaction would contribute an additional Ward term.

## 5. Statement record and final checkpoint

| Statement | Mark | What it establishes |
|---|---|---|
| Corrected integrated-shift formulas; Theorem V | PROVED in the cited prior inputs | Consumer, with normalization and twist signs retained |
| Theorem P and Corollary P-shift | PROVED here; not independently checked | A length-24 certificate bounds each seed number by length-12 moment data |
| Theorem O and O-seed | PROVED here from the existing Theorem 2; not independently checked | Positive integrated width at each fixed radius; only the quantified certificate class is excluded |
| U(1) distinction (4.1)–(4.2) | PROVED here; not independently checked | The SU(2) certificate does not transfer with unchanged coefficients |
| P-small at order-one coupling; ES; a cutoff-uniform physical seed | OPEN | No small upper estimate or mass gap is obtained |

No numerical guide was needed. No script, SDP, finite enumeration,
interval computation or machine proof discharges a statement.
The finite arithmetic in the proofs is displayed. No Balaban formula
is imported. Only this lane's output is changed; no registry, FINISH
row, source proof, audit record or scientific standing is edited.

Sources: assigned commit above; main rules at a527a6fdaeb2;
PR 10114 at f76f6c649cff7dffbab664d8976e680e8f287fe9.
The strongest unproved obligation is P-small or a sharper substitute
at a single admissible physical seed size. A fixed-radius universal
diameter argument cannot be made arbitrarily accurate by increasing
word degree alone. A strategy for arbitrarily large seed sizes needs
size-dependent support or information beyond that certificate class.
At one chosen size, a fixed-support certificate remains unexcluded.
The next decision is to fix that size and patch, then seek a hand
certificate for the displayed integrated tolerance.

Recovery: the requested file is in the supplied checkout. A local
copy is committed on `codex/gap-loop-pos-astra-73d1d443d`, in the
isolated worktree `/tmp/gap-loop-pos-astra.2zbXGu/worktree`.
No remote push or post is made. The author has checked the displayed
Ward eliminations, loop-length ceiling and volume factors; this is
self-checking, not an independent check or a Lean formalization.

RESULT: PROVED here, not independently checked: a radius-two, length-24 Ward/positivity certificate bounds both ES integrals by length-12 staple moments; actual Wilson witnesses give a strictly positive integrated width for every fixed-radius separate-state certificate, including on order-one coupling intervals. No radius proportional to a is required by this obstruction. P-small, ES and the physical mass gap remain OPEN; no scientific status is granted.
