# Repo search

READ — Before deriving anything I searched the supplied full repository with
bounded `git grep -n -i -E`, across these local refs:

| Ref | Revision |
|---|---|
| origin/main | 993f5e4f6d11a7e20a1cab9612c5749a53bae073 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Terms: `relative homological|homological analyticity|centre.odd marker|
contractible decorations|\(E17\)`, followed by
`electric.flux|twisted.partition|twist.free.energy|
contractible.*(sum|resum)|homolog.*sector`. The second broad query hit its
75-line cap; it is discovery, not evidence of absence. A follow-up over the
old YM4D folder and `research/ym4d/`, on all five refs, returned six lines.
No fresh fetch or history search was used. The full-repository reads are
the explicit repo-first exception to the task's otherwise local scope.

Let S/ denote `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.

| Relevant hit | Exact content read | Distance from this target |
|---|---|---|
| pr/10114:S/checks/review_massgap_block_literature.md:112–121; also located on pr/10133 | Ito–Seiler's two obligations are flow to strong coupling and a common interpolation parameter for twisted and untwisted partition functions; a local implicit-function argument does not supply global continuation. | Prior warning, no HA or real relative bound. The original paper was not newly read. |
| pr/10114:S/MASS_GAP_LOCAL_BLOCK_ASTRA.md:88–166, found through the November 8 digest | Equation (11): `C_F(a) >= v_N^2 exp[-4 beta(p_B+b)]/(1+v_N/r_f^b) > 0`, uniformly in total spatial volume. | A lower bound for a local one-step witness. It underlies the consumer's rate; it does not suppress winding flux. Credit the Codex source. |
| origin/main:docs/CONFINEMENT_STRING_TENSION_NOTE.md:1–73 | Its support statement explicitly does not derive four-dimensional Yang–Mills confinement; it imports SU(3) confinement and lattice/EFT information. | Different group and conditional support, no supplier. |
| pr/10114:S/EXTCONT.md:455–485; also located on pr/10133 | Its `(E17)` is `sup T(w_{ {v} }) <= C exp(-mu m)`, a jet price for filling a hole. | Equation-label collision, not this (E17). |

The other exact `(E17)` hits are `docs/ENERGY_ADAPTED_REFINEMENT_...`
(`Gamma_E/c0=A`) and `docs/EXCLUDED_WALK_MEMORY_CURRENT_...`
(`||(d/b) cross n-e cross omega||<=r^2`). They are unrelated identities.
Flat-gauge and holonomy hits in S/BFT4B55 and S/CODEX_REVIEW_THETAW
concern different gauge-coordinate estimates; no assertion from them is used.

A later method query, on the same five refs, used
`homologically.trivial.*(resum|decor)|flat.neighbo.*(prob|mass)|
rare.flat.*environment|common.normalizer.*(analytic|twist)`.
Its only hits were pr/10114 and pr/10133:
S/REVIEW_PUSH_A_CYCLE3_ASTRA.md:97. The exact relevant statement is
“TB is a supported analytic fixed point, not a logarithm of an integrated
polymer gas”; the factorized activities and common normalizer remain
missing there. It is a related prior warning, not a supplier for this probe.
No hit in that query supplied the nearly flat event estimate below.

READ — The November 8 digest is about earlier RG/history targets. Its
one-step witness pointer above was followed to the actual source. Local
searches found the following much closer work, which is reused:

- `gap-z2parity-astra.md:246–442`: the marked polynomial, area-order
  zero, HA and HA-to-(E17); the background-uniform HA countertest.
  `gap-z2parity-check-opus.md:15–123` checks these and limits the generic
  shrinking-disc example. Credit Codex GPT-6-astra and Claude Opus 5.5.
- `gap-joint-astra.md:97–183`: (J2)–(J4), a finite exact resummation
  including compatible contractible decorations before absolute values.
  Its `:345–371` states the real, rooted, absolute-surface criterion (J12).
  It is OPEN at order one. Neither identity nor criterion is new here.
- `gap-flat-astra.md:74–151,452–510`: exact grouping (F1)–(F5), and
  existing restricted-shape/strong-coupling estimates. They do not give
  the bound on `I=[43/20,5/2]`.
- `gap-expose-astra.md:575–599`: (E17) is sufficient for (FQ), with
  its fixed consumer rate. No area exponent is required.

Ownership search: `open-registry.md`, `open-core.md`, and `l17c.md`
have no match for HA, homological, centre/center-odd, electric flux,
E17 or decorations. FINISH:948 explicitly assigns this probe to row 871.
The existing algebra and (J12) are covered work; only their missing
order-one averaged estimate, through the requested HA strength decision,
is attacked here. No inspected source already proves it.

# Status and checkpoint

Research text for FINISH row 871, `gap-ha-astra`, by Codex (GPT-6-astra,
configured max effort); completed 2026-11-13.
This is a proof probe, not an audit; it grants no scientific status.
No computation will discharge a proof obligation. Labels used below:
PROVED (written argument here), READ (source and lines), ARGUED, GUIDE,
and OPEN. No sub-agent check has been performed.

- Checkout verified: `6ed5bb723e1efd0d44ef0ce331b03d39a019ae1f`.
  The source account is the supplied on-disk copy at `31a47c543775`.
- First action: checked `library/prior/gap-ha-astra.md`; absent in this
  checkout. No prior-work conclusions have been inferred from that absence.
- READ: `GOAL.md`, in full. Its no-computer-assisted-proof contract applies.
- Completed: a real sufficient replacement, the fully resummed form of HA,
  three proof attempts, a small contribution bound on a specified real
  event, and the U(1), Z2 and frozen-2T tests.
- Open obligation: (C2), the real integrated response estimate, or (D3),
  the equivalent complex HA estimate. Neither is proved or refuted for SU(2).
- Failed routes: positivity after boundary resummation leaves unsuppressed
  class means; real continuation has a volume-sized cost; a thin nearly
  flat event is controlled but its complement is not.
- Next decision: an SU(2)-specific signed estimate for that complement or
  the response in (C2). Another finite rearrangement supplies no such estimate.
- Delivery: this output file only, local and uncommitted. No independent
  check, audit, scientific-status edit, commit, push or outward post.

Credit where used identifies Ethan Sussman and Levent Alpoge (with
Claude and Codex as authors of their account), Tadeusz Balaban, and the
repository authors of the parity reduction and its check. Source summaries
are finding aids, not proof evidence.

## Step 1. Source boundary and exact target

READ — `GOAL.md` and FINISH:64–74,320–351 were read. The sparse checkout
lacks the workflow file. Main's workflow map and its RULES, SETTINGS and
research procedure were read at the revision above. This dispatched,
output-only probe keeps the requested pin and does not start another lane.

Index searches preceded source reads. `sa-index/README.md:1–10` explains
its status labels. Neighbouring rows read: `chunk-01.md:57–74,118–145`,
`chunk-02.md:85–105`, `chunk-04.md:80–93`, and
`obligations.md:17–29,45–53,158–164`. Searches for homological analyticity,
centre-odd, electric flux and E17 found no matching indexed object.
This is a search result, not an account-wide absence theorem.

READ — In Ethan Sussman and Levent Alpoge's outline, authored with Claude
and Codex, the needed source passages are:

| Source lines in `YM4_sketch_500.tex` | Exact scope |
|---|---|
| 565–600 | Polynomial clustering gives no positive mass gap. |
| 2195–2243 | (GL3) gives positive character coefficients and factorial decay. |
| 2313–2335 | (GL8) identifies the positive transfer trace with the torus partition function. |
| 1150–1221,1267–1347 | The connected logarithm and convergence theorem are conditional on the activity criterion: “The estimate on the activities remains a separate analytic task.” |
| 4693–4730 | The normalized zero-free lemma is proved. Its last example shows why an exponential volume bound alone supplies no fixed zero-free radius. |

The CA index's only mass-gap proposition hit is
`10.7:prop-clustering-mass-gap` (CA-III:108223). Reading
CA-III:108209–108260 shows that a positive gap is a **premise** there.
CA-I:2490–2515,2698–2716 explicitly excludes an asserted mass gap.
No result from these passages proves HA. Their proved algebra is credited
and reused, not rederived. `lit-balaban.md:1–155` records Tadeusz
Balaban's background/RG results through quotations and secondary sources;
none is imported as an order-one winding estimate. His papers were not read.
`prior/gap-lit-flux.md` supplies the existing literature map; original
papers behind its conditional criteria were not newly verified.

Use the row-866 notation throughout: time period `a`, spatial periods
`(a,c,d)`, `c,d in {a,2a}`, `a>=3`, `N=6a^2cd<=24a^4`, and
`A=a L_i>=a^2`, `i=3,4`. The crossed spatial twist satisfies `m_2=0`.
Set `g=-(1/2)log eta_*>0`. The desired estimate is

\[
q_{m,i}(a)=\frac{Z^m-Z^{m+v_{1i}}}{2Z^m}
\le C a^p e^{-ga},\qquad \beta\in I=[43/20,5/2].
\tag{E17}
\]

All constants must be uniform in these data. This is fixed-coupling
research; no continuum conclusion follows by changing the meaning of `a`.
Explicitly, `x_p=tr(U_p)/2`, `t_p=tanh(beta x_p)` and
`dnu_ce=prod_p cosh(beta x_p) dU/Z_ce`, where `Z_ce` is that
integral. Write

\[
 \mathcal Z_k(\lambda)=\mathbb E_{\nu_{\rm ce}}
       \prod_p(1+\lambda\eta_{k,p}t_p),\qquad
 F=\log\mathcal Z_m-\log\mathcal Z_{m+v}
\]

as a germ at zero. These are exactly (M)–(M2) of row 866; their
area-order zero `F=O(lambda^A)` is READ input. HA asks for a holomorphic
extension to `|lambda|<r`, `r>1`, with `|F|<=BN`, for uniform
`r,B,a_0` and all admissible `a>=a_0` and beta in I.

## Step 2. The strength decision

**PROVED — restricting the literal HA bound to the real segment is
insufficient. In fact that restriction already holds.** Put
`tau_*=tanh(5/2)` and choose

\[
 R=\frac{1+1/\tau_*}{2}>1,\qquad
 M_R=\log\frac{1+R\tau_*}{1-R\tau_*}<\infty.
\]

For real `|lambda|<=R`, every factor in (M) lies between
`1-R tau_*` and `1+R tau_*`. The centre-even reference measure
is a probability. Therefore, for every twist k,

\[
 (1-R\tau_*)^N\le\mathcal Z_k(\lambda)
 \le(1+R\tau_*)^N,
 \qquad |F_{m,v}(\lambda)|\le N M_R.                 \tag{R0}
\]

The real logarithms are defined on this entire interval. Each finite
volume has a complex neighbourhood of the interval without zeros;
no uniform width is asserted. This proof applies equally to SU(2),
U(1) and Z2 with the same bounded plaquette trace. It uses no area law.
For Z2 at beta 5/2, row 866's proved test gives `q(a)->1/2`.
Thus (R0), even together with the area-order zero, cannot imply (E17).
The complex maximum principle was doing essential work in the HA proof.
The real extensive bound must not be called the real area-law content of HA.

There is an even smaller elementary real bound. Choose v on a single
dual stack, with `K_v=a L_j<=2a^2` faces (`{i,j}={3,4}`). The two
integrands differ only there. Their pointwise ratio lies between
`exp(-K_v M_R)` and `exp(K_v M_R)`. Integrating against either positive
integrand gives `|F(lambda)|<=K_v M_R`. An area-size upper bound on the
real logarithm is therefore also insufficient; the needed quantity
must become small, not merely remain subextensive.

**PROVED — a weaker real averaged sufficient statement.** Define genuine
probability measures and their scores, for `0<=lambda<=1`, by

\[
 d\mu_{k,\lambda}
 =\frac{\prod_p(1+\lambda\eta_{k,p}t_p)}
        {\mathcal Z_k(\lambda)}\,d\nu_{\rm ce},
 \quad S_{k,\lambda}(U)=
       \sum_p\frac{\eta_{k,p}t_p(U)}{1+\lambda\eta_{k,p}t_p(U)},
\]
\[
 \mathcal R_{m,v}(\lambda)
 =\mathbb E_{\mu_{m,\lambda}}S_{m,\lambda}
  -\mathbb E_{\mu_{m+v,\lambda}}S_{m+v,\lambda}.
                                                               \tag{R1}
\]

All factors are bounded away from zero on this real segment. Differentiate
the finite integrals under their bounded integrands. This gives exactly

\[
 F'_{m,v}(\lambda)=\mathcal R_{m,v}(\lambda),\qquad
 F_{m,v}(1)=\int_0^1\mathcal R_{m,v}(\lambda)\,d\lambda.   \tag{R2}
\]

No absolute value has entered either partition integral or the sum over
plaquettes. All contractible decorations are included with their signs.
The two expectations have their **actual** normalizers; they are not
expectations of a conditional logarithm.

The following is the real crux to try, with the same quantifiers as (E17):

\[
 \boxed{\int_0^1|\mathcal R_{m,v}(\lambda)|\,d\lambda
        \le C_R a^{p_R}e^{-ga}.}                         \tag{R}
\]

**OPEN for Wilson SU(2) on I.** If (R) holds, then
`0<=q=(1-exp(-F(1)))/2<=F(1)/2<=C_R a^{p_R}e^{-ga}/2`.
This proves (R) implies (E17). There is no need for a complex disc or
an area exponent. Omitting the outer absolute value makes the criterion
essentially the original endpoint problem; that is not a reduction.
The existing (J12) is another real sufficient criterion, already stated
in the repository. It will not be presented as a new result here.

HA implies (R). Indeed set `s=(1+r)/2`, `d=s-1>0`, and
`c=log(r/s)>0`. Its already proved high-order Schwarz estimate gives
`|F(z)|<=BN(s/r)^A` on `|z|<=s`. Cauchy's derivative formula on
the circle of radius d about any `lambda in [0,1]` then gives

\[
 \int_0^1|\mathcal R(\lambda)|d\lambda
 \le\frac{BN}{d}e^{-cA}
 \le\frac{24B}{d}e^{g^2/(4c)}a^4e^{-ga}.              \tag{R3}
\]

Only this implication uses complex analysis. Criterion (R) itself is
entirely real. It is a statement to prove, not a new confinement input
that has somehow been obtained by writing (R2).

**PROVED — strict loss of complex information in this weakening.** This
test concerns auxiliary polynomials, not Wilson SU(2). For integer `a>=3`,
put `A=a^2`, `epsilon=exp(-ga)`, and

\[
 P_a(\lambda)=1+\lambda^6+\epsilon\lambda^A,\qquad
 Q_a(\lambda)=1+\lambda^6-\epsilon\lambda^A.
                                                               \tag{R4}
\]

They equal one at zero and are positive on `[0,1]`. Their difference
has order A. Put `x(lambda)=epsilon lambda^A/(1+lambda^6)`.
Then `x'>=0` there, because its numerator after differentiation is
`epsilon lambda^{A-1}[A+(A-6)lambda^6]`. Thus

\[
 \int_0^1\left|\frac{d}{d\lambda}\log(P_a/Q_a)\right|d\lambda
 =\log\frac{2+\epsilon}{2-\epsilon}
 \le\frac{4\epsilon}{3},                              \tag{R5}
\]

where `log((1+x)/(1-x))<=2x/(1-x^2)` and `x=epsilon/2<=1/2`
prove the inequality by integrating `2/(1-x^2)` from zero.
The endpoint odd fraction is `epsilon/(2+epsilon)>=epsilon/3`.
No fixed positive area exponent can bound that fraction by a polynomial
times `exp(-c a^2)`. So (R) does not force HA even at the endpoint.

There are also actual uncancelled complex zeros near the unit circle.
Let `zeta=exp(i pi/6)` and `delta=sqrt(epsilon)`. On
`|lambda-zeta|=delta`, for sufficiently large a, `delta<=1/20`
and `A delta<=1`. Taylor's finite binomial formula gives

\[
 |1+\lambda^6|\ge6\delta-57\delta^2>3\delta,
 \qquad |\epsilon\lambda^A|\le\epsilon e^{A\delta}
 \le e\delta^2<3\delta.
\]

The six roots of `1+lambda^6` are separated by at least one, so the
delta-disc contains exactly its simple root zeta. Rouché's theorem gives
one zero each of P_a and Q_a inside. They cannot share a zero: their
difference would force `lambda=0`, where both equal one. Any fixed disc
`|lambda|<r`, `r>1`, eventually contains these zeros. The logarithmic
ratio cannot extend there. This is **not** a counterexample to actual
SU(2) HA; it shows exactly what a real sufficient criterion may leave free.

ARGUED decision: pursue (R), or the signed normalized sum behind (J4),
as the consumer-level real target. Do not insist on HA's extra complex
continuation unless a proof produces it at no additional cost.

## Step 3. Attempt A: sum every null-homologous decoration first

READ — `gap-kappa-order.md:35–60` already gives the full homology-class
surface sums (SC), with credit to the Mack–Petkova split and 't Hooft
flux variables. `gap-joint-astra.md:97–183` already resums connected
components and all their compatible decorations. The calculation below
uses SC and changes only how its **finite** sum is grouped. It does not
claim another new surface expansion.

Let `B_2=im(partial_3)` in the torus cell complex over `F_2`, and choose
one cycle `S_h` in each of the 64 homology classes h. Define

\[
 b_h(U,\lambda)=\sum_{b\in B_2}
       \lambda^{|S_h\mathbin\triangle b|}
       \prod_{p\in S_h\mathbin\triangle b}t_p(U),
 \qquad H_h(\lambda)=\mathbb E_{\nu_{\rm ce}}b_h(U,\lambda).
                                                               \tag{D1}
\]

The sum is over distinct boundaries, not over 3-chains with repeated
boundaries. Each closed surface occurs once in its coset. Thus this
already sums every contractible decoration, and also every null-homologous
decoration whose support wraps. “Null-homologous” does not mean that its
support lies inside a contractible box. Keep this enlargement explicit.

SC gives, without any convergence assumption,

\[
 V_m(\lambda):=\mathcal Z_m(\lambda)
       =\sum_h(-1)^{\langle m,h\rangle}H_h(\lambda),
 \quad O_{m,v}(\lambda)
       =\sum_{h:\langle v,h\rangle=1}
                    (-1)^{\langle m,h\rangle}H_h(\lambda),
 \quad V_{m+v}=V_m-2O_{m,v}.                            \tag{D2}
\]

The sums inside H, and the signed sum defining O, are taken before
absolute values. This is an exact fully averaged object. It includes
overlapping boundary additions by symmetric difference, not by multiplying
independent activities. For example, adding a cube boundary along one
surface face replaces one face by five. Multiplying their separate weights
would count the shared face twice instead of removing it. The old bump
calculations already handle that geometry; a naive product does not.

**OPEN — exact resummed complex crux.** Do there exist `s>1`, `c>0`,
`C<infinity` and `a_0` such that, uniformly in the task's data,

\[
 \boxed{|O_{m,v}(z)|\le C N e^{-cA}|V_m(z)|
       \quad (|z|<s,\ a\ge a_0)?}                    \tag{D3}
\]

Increase `a_0` so that `C N e^{-cA}<=1/4`. This is a genuine relative
estimate after full boundary resummation, not separate bounds on numerator
and denominator. It permits zeros of both partition functions.

**PROVED — (D3) is equivalent to HA after shrinking its disc and
increasing its size cutoff.** If (D3) holds, the quotient `O/V_m`
has removable singularities at zeros of `V_m`. Indeed a smaller vanishing
order of O would make its modulus ratio unbounded near that zero.
The quotient is holomorphic and has modulus at most `C N e^{-cA}`.
Consequently

\[
 F=-\log(1-2O/V_m),\qquad |F|\le4 C N e^{-cA}\le4CN
                                                               \tag{D4}
\]

on the disc. The logarithm is its convergent series at zero; (D2)
identifies it with the required germ. Thus HA holds there.

Conversely assume HA on `|z|<r`. Choose `1<s<r` and put
`c=log(r/s)`. The inherited high-order zero gives
`|F(z)|<=BN exp(-cA)` on `|z|<s`. For all sufficiently large a
this is at most `log 2`. The identity
`V_{m+v}=V_m exp(-F)` holds on the whole disc by analytic continuation
from zero, even at common zeros. Therefore
`|O|=|V_m||1-exp(-F)|/2<=BN exp(-cA)|V_m|`.
This is (D3). No estimate of an individual H_h is being demanded.

**Attempted proof of (D3), first stage: obtain a positive resummed vacuum.**
For fixed U define the already known centre-sign polynomial

\[
 \Phi_k(U,\lambda)=2^{-|E|}\sum_{z\in\{\pm1\}^{E}}
        \prod_p\{1+\lambda\eta_{k,p}(\delta z)_p t_p(U)\}.
                                                               \tag{D5}
\]

Link-sign averaging in (J3) gives its closed-surface expansion. Finite
Fourier inversion over the 64 twist classes gives

\[
 b_h=\frac1{64}\sum_k(-1)^{\langle k,h\rangle}\Phi_k.
                                                               \tag{D6}
\]

For real `|lambda|<1/tau_*`, all factors in (D5) are positive.
Thus `b_0>0` and `|b_h|<=b_0`. This proves that the complete
zero-homology sum can serve as a positive real reference, even though
individual surface weights and other class sums can be signed.
The positive reference measure and remaining class means are

\[
 d\rho_{0,\lambda}=\frac{b_0}{H_0}\,d\nu_{\rm ce},
 \quad f_h=b_h/b_0,\quad
 H_h/H_0=\mathbb E_{\rho_{0,\lambda}}f_h,\quad |f_h|\le1.
                                                               \tag{D7}
\]

This is all obtained by finite sums, with no numerical enumeration.
It is the existing flux Fourier identity used as a real vacuum resummation,
not a new positivity theorem for the signed H_h.

**First failing estimate.** Substituting (D7) into (D2) cancels H_0
exactly. It leaves 64 signed class means, each bounded only by one.
No area or perimeter smallness follows. At complex z, (D5) is no
longer positive and b_0 can vanish; (D7) supplies no analytic bound.
Replacing the means by a supremum would reuse the already refuted
environment-uniform route. Summing all boundaries has removed the
extensive vacuum factor algebraically; it has not bounded the relative
weight of different cosets. That is the missing estimate in (D3).

**Binding test, in an actual model.** At beta 5/2 in Z2, row 866's
all-class Peierls bound gives `Z^k/Z^0 -> 0` for every nonzero k.
There are only 63 such k, so (D6), after integration, gives
`H_h/H_0 -> 1` for **every** h. In the untwisted numerator of (D2),
32 classes pair oddly with v, out of 64 in its denominator. Hence
`O/V_0 -> 1/2`, precisely the known Z2 test. Complete boundary
resummation and positivity both survive; the desired suppression does not.
This does not refute the SU(2) estimate. It identifies what the SU(2)
environment average still has to do after the proposed resummation.

Checkpoint: (D3) is HA in a fully resummed form; it remains OPEN.
The finite rearrangement and positive real reference have supplied no
SU(2)-specific cancellation estimate.

## Step 4. Attempt B: continue from a controlled real marker

READ — The cluster estimate (J5)–(J9) in
`gap-joint-astra.md:192–274` controls arbitrary signs and deleted
polymers when their absolute activities have its majorant. Its proof
uses the Sussman–Alpoge rooted theorem already read above. It need not
be rederived for this marker: replace every surface weight by
`lambda^{|S|} w(S)`. Then its parameter is
`rho=400 e lambda tanh(beta)`.

At the real value `lambda_0=1/2400`, `rho<1/2`, since `e<3` and
`tanh(beta)<1`. The old pointwise comparison of positive conditional
partitions can therefore be averaged with its actual denominator.
It gives, uniformly on I,

\[
 0\le F_{m,v}(\lambda_0)
 \le \frac{N}{200}\frac{\rho^A}{1-\rho}
 \le\frac{N}{100}2^{-A}.                               \tag{C1}
\]

The nonnegativity uses the same transfer construction as at lambda one:
integer character coefficients are unchanged, half-integer coefficients
are multiplied by nonnegative lambda, and the spatial multiplier is
positive. Thus the temporal centre projection remains positive. This
does not require a probability interpretation of individual surfaces.

**PROVED reduction, with a proved initial value.** It suffices to prove
the real criterion (R) with its integral restricted to `[lambda_0,1]`:

\[
 \int_{\lambda_0}^1|\mathcal R_{m,v}(\lambda)|d\lambda
 \le C_R a^{p_R}e^{-ga}.                               \tag{C2}
\]

Indeed (R2) and (C1) give `F(1)<=N 2^{-A}/100` plus the left
side of (C2). Since
`-(log 2)a^2+ga <= g^2/(4 log 2)`, (C1) is absorbed into a
constant times `a^4 e^{-ga}`. This is a useful restriction of the
unknown interval, not a new closure at order one.

**Attempted continuation estimate.** The exact real scores obey

\[
 |S_{k,\lambda}|\le\frac{N\tau_*}{1-\lambda\tau_*},
 \quad\int_{\lambda_0}^1|\mathcal R|d\lambda
 \le2N\log\frac{1-\lambda_0\tau_*}{1-\tau_*}.           \tag{C3}
\]

This is finite and uniform in beta. It is of volume order and loses
the initial area gain. A Grönwall attempt would need a **relative**
bound on `F'/F`, not the absolute score bound (C3). At a leading term
`F~lambda^A`, even that logarithmic derivative is `A/lambda`;
an automatic order-one bound on it is unjustified. No relative
response estimate at the required coupling follows from the finite
energy bound or the cancellation of the common vacuum sum.

This failure is substantive in the Z2 control. The same (C1) holds
there. At beta 5/2, however, the proved bound of row 866 gives
`F(1)>=log((1-epsilon_a)/epsilon_a)` with
`epsilon_a=(N/80)(80 exp(-5))^{a^2}/(1-80 exp(-5))->0`.
Thus the real continuation from lambda_0 must generate a large response.
Positivity and the controlled initial marker cannot prohibit it.
Neither this test nor (C3) rules out an SU(2)-specific proof of (C2).

Checkpoint: the small-marker endpoint is already supplied by prior work.
The unresolved real obligation is precisely (C2), with the consumer rate g.

## Step 5. Attempt C: average the bad nearly flat environments

READ — Row 866:130–170 already identifies the conditional signed deficit.
Write `D_k(q,lambda)` for its centre-sign sum with the marked plaquette
weight `cosh(beta J)+lambda eta sinh(beta J)`. Its quotient-Haar average
is the full marked partition, up to the common centre-even normalization.
For real `0<=lambda<=1`, put

\[
 d\nu_{m,\lambda}(q)=\frac{D_m(q,\lambda)dq}{\int D_m dq},
 \quad c_{m,v}(q,\lambda)=\frac{1-D_{m+v}(q,\lambda)/D_m(q,\lambda)}2.
\]

Then `q_{m,v}(lambda)=E_{nu_{m,lambda}}c_{m,v}` exactly.
The conditional c can be negative; it is not a conditional probability.
I use the actual measure in this formula throughout.

The pointwise countertest at the identity environment does not alone
refute this average. The following estimate addresses that specific
temptation, with a gauge-invariant event rather than a small neighbourhood
of one gauge representative.

**PROVED — a sufficiently thin, everywhere nearly flat event has a
negligible real contribution.** Put `V=a^2cd`, `K_v=a L_j<=2a^2`,
and choose a fixed positive angle

\[
 \epsilon=\min\left\{\frac1{16},
       \sqrt{\frac{5-\log80}{5}},
       \left(\frac{3\pi e^{-120}}8\right)^{1/3}\right\}.
                                                               \tag{A1}
\]

It is positive because the hand inequality `e^5>1097/12>80`
was proved in row 866. Let `G_epsilon` be the event
`|tr U_p/2|>=cos epsilon` for **every** plaquette. It is invariant
under gauge transformations and centre changes of link lifts.

READ — Lemma FE, `gap-seed-limit.md:124–126`, gives
`mu(|f|)<=exp(12 beta |Gamma|) int |f| dHaar_Gamma` for a
function of links Gamma. The same proof applies to all present real
marked and twisted weights: each plaquette factor is between
`exp(-beta)` and `exp(beta)`, so its log oscillation is at most
`2 beta`. No new finite-energy theorem is claimed.

Choose disjoint 12-plaquettes whose four base coordinates are multiples
of three, stopping at `3(floor(L_mu/3)-1)` in each coordinate.
None wraps. They have disjoint link sets. Their number is

\[
 M=\prod_{\mu=1}^4\lfloor L_\mu/3\rfloor\ge V/625.
                                                               \tag{A2}
\]

For `n=3k+r>=3`, `0<=r<=2`, one has `n<=5k`; this proves
each factor bound used in (A2). Under product Haar measure, the
holonomies of these disjoint plaquettes are independent and Haar.
SU(2)'s Weyl density gives the two-cap probability

\[
 p_\epsilon=\frac4\pi\int_0^\epsilon\sin^2\theta\,d\theta
       \le\frac{4\epsilon^3}{3\pi}.
\]

Apply FE to the event on those `4M` links. The full event is contained
in it. Since `48 beta<=120`, (A1) gives, uniformly on the real segment,

\[
 \nu_{m,\lambda}(G_\epsilon)
 \le(e^{48\beta}p_\epsilon)^M
 \le2^{-M}\le\exp[-(\log2)V/625].                      \tag{A3}
\]

This probability is the push-forward of the full marked Wilson law;
no product law for quotient environments has been assumed.

Flipping v changes only `K_v` plaquette factors. Their real pointwise
ratios lie in `[exp(-2 beta),exp(2 beta)]`, including after the finite
centre sum. Thus `|c_{m,v}|<=exp(2 beta K_v)` everywhere. In particular,

\[
 \left|\int_{G_\epsilon}c_{m,v}\,d\nu_{m,\lambda}\right|
 \le\int_{G_\epsilon}|c_{m,v}|\,d\nu_{m,\lambda}
 \le\exp[10a^2-c_0a^4],\qquad c_0=\frac{\log2}{625}.
                                                               \tag{A4}
\]

For `a>=max{sqrt(20/c_0),(2g/c_0)^{1/3}}`, the last expression
is at most `exp(-ga)`. The two terms `10a^2` and `ga` are then
each at most `c_0 a^4/2`. This is a written real bound on a portion
of the actual average, with no computation or sampling.

The event really includes the old bad conditional environments. Choose
lifts of every link within angle `epsilon/4` of the identity. Products
around a plaquette lie within angle epsilon, so `J_p>=cos epsilon`.
At beta 5/2, the choice (A1) and `cos x>=1-x^2/2` give
`5 cos epsilon>log80`. The earlier Z2 deletion proof applies to
these inhomogeneous conditional couplings, using
`u_p=exp(-5J_p)<=exp(-5 cos epsilon)` in every deleted component.
Its parameter `80 exp(-5 cos epsilon)` is below one. Hence this
conditional odd fraction tends uniformly to 1/2 on that subset.
It lies inside G_epsilon; gauge-transforming it still lies inside
G_epsilon. Estimate (A4) shows why this particular pointwise failure
does not force a failure of the averaged SU(2) bound.

**First failing estimate.** The complementary event is not controlled.
Outside G_epsilon, at least one plaquette has left an extremely thin cap.
This implies neither a density of useful frustration nor suppression of
the signed winding sum. The same pointwise bound used in (A4), on that
complement of probability close to one, is exponentially large in area.
Taking its absolute value cannot prove (E17), (C2), or (D3).
This calculation discards only a narrowly specified set of bad
environments. It is not a typical-environment theorem.

**Model checks for this estimate.** U(1) has cap probability
`2 epsilon/pi`; choosing its cap small enough gives the same argument.
Therefore (A3) is a continuity estimate, not an SU(2)/U(1) separation.
For Z2 every plaquette lies in the cap and its Haar cap probability is
one, so the small-base step fails. For frozen 2T, a cap below the
noncentral separation has Haar probability `2/24=1/12`; at beta 5/2
the FE factor does not make that base small. In the exactly frozen
model every surviving plaquette is central, so G_epsilon has probability
one. No false Z2 or frozen-2T suppression has been deduced.

Ownership: FINISH:944 assigns row 867 a different one-slice, local-spin
separation probe. This spacetime estimate does not prove such a separation
and does not take over that task. The targeted search found no existing
estimate for this particular nearly flat event; its FE input is reused.

## Step 6. Binding tests and disposition

READ — The controls used here are precisely those proved in
`gap-z2parity-astra.md:386–503` and checked in
`gap-z2parity-check-opus.md:63–110`:

- Z2 at beta 5/2: the odd fraction tends to `1/2` on the admissible
  large tori. This is a finite-coupling theorem from the Peierls bound.
- Frozen 2T: the exact flat counts are `N_0=5856`, `N_v=96`, giving
  `Z^v/Z^0=1/61` and `q=30/61`. Freezing is first at each fixed torus.
  No finite-coupling freezing threshold or exchange of limits is used.
- Compact free Maxwell: the holonomy-mode odd fraction is
  `sum_{n odd} exp(-e^2 n^2/2) / sum_n exp(-e^2 n^2/2)>0`,
  independent of the cubic side. Its identification with the finite-torus
  Wilson-cosine U(1) Coulomb phase is not proved in the sources read here.

| Step | U(1) Coulomb check | Z2 at beta 5/2 | Frozen 2T check |
|---|---|---|---|
| Real positivity and (R0), including its area-size version | Holds for the Wilson marker; cannot force suppression | Holds despite `q->1/2` | Positivity survives; no uniform frozen-beta constant is claimed for (R0) |
| (R1)–(R2) and the sufficient criteria (R), (C2) | Finite-coupling identities hold. A successful bound would require vanishing odd flux, incompatible with the Maxwell control if the Coulomb matching is supplied (ARGUED for Wilson U(1)) | The final bound fails; the real integrated response cannot be small | On the frozen family, the endpoint is `F(1)=log61`, so a vanishing continuation bound cannot hold |
| (D1)–(D7), complete boundary resummation | Centre quotient and finite Fourier identities still hold; no integer-flux suppression follows | Fully resummed class means tend to one | Finite Fourier identities persist in the frozen limit; they do not change its counts |
| (D3) equivalent to HA; the area-order argument | Same implication, no group selection | False by its real endpoint consequence | False for the frozen family by its real endpoint consequence |
| Controlled marker (C1) and crude continuation (C3) | Same small-marker proof; no continuation through a Coulomb phase is obtained | Initial smallness holds and is lost before lambda one | The small-marker comparison has no bearing on the non-small frozen endpoint |
| Nearly flat event (A3)–(A4) | Also works after choosing the U(1) cap small enough; not a separating input | The small Haar-cap premise fails | The small Haar-cap premise fails; frozen plaquettes are central |
| Auxiliary zeros (R4) | No identification with a gauge theory | No identification with a gauge theory | No identification with a gauge theory |

**ARGUED route decision.** HA is an unnecessary strengthening of the
consumer. The useful real alternative is (C2), which retains the prescribed
rate g and starts after the proved small-marker point. Proving only a
real extensive bound, even on an interval extending past one, would prove
nothing new: (R0) already supplies it. The strict weakening is established
for the class of normalized marked polynomials; no equivalence or
inequivalence theorem within the Wilson SU(2) family is asserted.

**OPEN outcome of the proof probe.** Complete null-homology resummation
leads to (D3), which is equivalent to HA after harmless changes of radius
and size cutoff. The finite algebra does not prove its inequality.
The only new smallness estimate obtained, (A4), bounds a specified thin
event in the real ensemble. Its complement can carry the whole winding
fraction. No numerical string tension, local typical value, or numerical
zero-free radius has entered any proof. The recalled numbers in row 870
remain GUIDE and were not needed here.

An actual complex refutation would need uncancelled zeros of the two
SU(2) marked polynomials inside every proposed uniform disc, on an
unbounded sequence of admissible sizes (or another violation of HA's
uniform logarithm bound). Exponentially close but unequal zeros would
suffice; approximate cancellation of contractible free energies would not.
The auxiliary polynomials (R4) exhibit that distinction, but no such
SU(2) zeros have been established. A finite-size zero alone would not
exclude HA's freedom to increase `a_0`.

Source hashes (bookkeeping only): outline
`d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`;
CA-I `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`;
CA-III `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d`.
The first two match the prior parity note's source hashes. CA-II was not
needed and was not read. No numerical experiment, enumeration, automated
proof, fresh literature fetch or subagent was used. The arguments above
are author proofs and conditional implications, not independently checked
results or granted repository standing.

RESULT: OPEN — a weaker real averaged response bound suffices for (E17), and a thin nearly flat contribution is proved negligible; full boundary resummation leaves the SU(2) relative estimate unproved, and no SU(2) complex counterexample to HA is established.
