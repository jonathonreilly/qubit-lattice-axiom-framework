# Repo search

Searched `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141` in `/Users/jonreilly/Projects/Physics`, including outside this lane. The completed exact query `crux lemma EXC|Proposition EXP|high.spin.*(excess|odd.sector)|spin.?5/2.*filter|gap-filter-ls|gap-exc-astra` returned no matches (cap 50). Broader bare EXC/E17 and parity-sector queries filled their caps with unrelated material; they establish no absence. A method query for `vortex.free.energy|electric.flux|high.spin|spin-5|sector.*log.derivative|twisted.partition`, restricted in its output to YM4/Yang–Mills paths, located the older small-box electric-flux discussion and the mass-gap literature check on PRs 10114/10133. Exact source reads and dispositions follow below; these discovery hits are not proofs.

READ: `prior/repo-search-2026-11-08.md` in full. It treats earlier RG targets. Its nearest method hit is `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, a positive one-step loop-correlation result, not an EXC estimate. The task supplies no additional “Repo prior work” list. Searches of `open-registry.md`, `open-core.md`, and `l17c.md` for `gap-exc`, `crux.*EXC`, `(E17)`, `spin.?5/2`, `high.spin`, `gap-filter`, and `gap-hs` returned no match. FINISH rows 872–875 distinguish the existing derivation/checks from this assigned probe. No competing EXC owner was located.

The refs read were, respectively, `993f5e4f6d11a7e20a1cab9612c5749a53bae073`, `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `89faef229ff6e6bde42baad15ed8270c2f4087d8`, `1e70c7211a2cdbc39001e619f1dd89db45e25851`, and `c73ad7b177d94f89ff37b77386936e3d52b48b05`. A further completed query, `high.spin.{0,70}(convex|boost|excess)|boost.{0,70}high.spin|commuting quadruple|N_0.?=.?5856`, returned no matches on those refs (cap 35). A preliminary broad boost/spin search hit Lorentz-boost material and is not negative evidence.

Let `S/=.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` and `X/=.claude/science/toe-ruleset-20261021/agents/ym4d-existence/`. Relevant source dispositions:

| Source read | Exact statement used for comparison | Closeness |
|---|---|---|
| `pr/10114:S/MASS_GAP_LOCAL_BLOCK_ASTRA.md:1–166`, existing Codex construction | For b changed edges, `exp(-2 beta b) <= [psi(U)/psi(U')]/[A(U)/A(U')] <= exp(2 beta b)`. Its one-step loop correlation has a positive volume-independent lower bound (11). | Same Wilson kinetic normalization and local comparisons. Neither a winding-sector ratio nor its high-spin response. The stated strong-coupling endpoint has `beta<=1/32`. No re-derivation. |
| `pr/10114:X/EXISTENCE.md:3630–3685` | Twisted flat holonomies produce an argued small-volume electric-flux signal; the text says the route “remains a small-volume statement.” Its SP separates nonzero Hilbert norm from positive-energy spectral weight. | A different volume regime and observable. It supplies no EXC bound. PR 10133 and historical snapshot hits repeat this topic; they are not additional evidence. |
| `pr/10114:S/checks/review_massgap_block_literature.md:112–121` | Its Ito–Seiler reading separates flow to strong coupling from one common interpolation parameter for twisted and untwisted partition functions; local continuation alone does not supply global continuation. | Relevant warning about normalized comparisons. No literature theorem is imported through this secondary record. |
| `pr/10114:S/REALRGB.md:681–689` | Fixed-sector relative/log derivatives are finite algebra; the actual local prefactors and moving-sector boundary derivatives remain open. | RG-fibre sectors, not electric-flux sectors. No EXC result. The REALRGA/check hits concern the same different object. |
| Local `gap-filter-ls-opus.md:128–198`, with `gap-filter-ls-check-astra.md:94–199` | EXP and the corrected relative-response criterion. | Exact prior reduction; reused, not proved again. |
| Local `gap-expose-astra.md:88–153,575–627`; `gap-ext-astra.md:77–128` | Full gauge-invariant transfer, cut parity, admissible aspect ratios, original E17/FQ rate, and the crude extensive comparison E18. | Exact definitions and consumer. E17 is explicitly open. |
| Local `gap-cf-astra.md:163–189`; `gap-z2parity-astra.md:386–442,450–507` | Q8 frozen ratio `3/23`; 2T frozen ratio `1/61`; Z2 odd weight tends to `1/2` at `beta=5/2`; the compact free-Maxwell odd weight is positive and independent of box size. | Existing binding controls. Frozen limits precede the size limit; Maxwell is not a proved Wilson-cosine identification. No new counting proof. |

Index first: read `sa-index/README.md` in full, searched its chunk files and `obligations.md` for high spin, spin 5/2, electric flux, vortex, twist, one-bond convolution, transfer contraction and mass gap. Read neighbouring rows `chunk-02.md:76–112` and `obligations.md:58–74`, then outline `YM4_sketch_500.tex:2195–2257,2313–2381`. GL3–GL4 already give the positive Bessel spectrum and factorial decay; GL8 gives the half-kernel trace; GL10 is a contraction estimate with an additional pointwise-positive inserted kernel. Those proved source steps are credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. They are not EXC. A targeted search of `sa-index/ca-full/` and `port-map.md` for the target/method terms returned no match. This is bounded search coverage, not an absence theorem. No Balaban result is imported. The source folder has no Git metadata, so `31a47c543775` remains the supplied revision, not independently verified provenance.

# EXC proof probe — row 875

Author: OpenAI Codex, row 875 dispatch `gpt-6-astra max`, 2026-11-13. Research text only; grants no scientific or audit status. PROVED below means a written author argument, not an independent check. No other model has checked these new arguments. No computation discharges any proof obligation.

## Checkpoint (updated in place)

- Checkout revision verified: `9f1e04272b03270994c98fb4b9716e071924bac4`, branch `lanework`; supplied source-account revision: `31a47c543775` (supplied provenance; the source folder has no Git metadata).
- Prior target inventory: `library/prior/gap-exc-astra.md` is absent (checked before other reads).
- Established in this text: the corrected EXC contract; negative actual response at sufficiently large boost on even-a tori; a negative temporal edge kernel at the natural endpoint throughout the requested window; monotonicity of each sector's total high-spin count; translation accounting; a positive order-length EXC integral in the full electric-only reference.
- Open obligation: the uniform positive net response for the isotropic Wilson transfer at the prescribed bounded boost, with the consumer rate matched. No actual isotropic counterexample was constructed.
- Failed routes: unbounded boosting reverses the response on even-a tori; the proposed positive temporal-edge density fails at the natural endpoint; sector convexity does not order sector responses; the electric comparison's known magnetic continuation estimate loses order a^3 against an order-a gain.
- Next decision: estimate the relative magnetic response displayed at the end. The next session should not repeat EXP, the existing high-free states, frozen group counts, or the electric seed. The final author check and file-delivery record are below.

## Step 1 — initialization

READ: checked the requested prior inventory path; no file exists. Created this running research record before derivation.

## Step 2 — corrected inputs, before derivation

READ: GOAL in full; FINISH 52–74 and 320–351; row 875 at FINISH 952. Main's `SCIENCE_WORKFLOW.md` now points to `RULES.md`, `SETTINGS.md`, and `procedures/research.md`; those were read. This is the expressly assigned pinned-checkout text probe, not a new campaign, review, status edit, or outward post. The repository physics-loop skill supplies the research discipline; the current research procedure and this task control its older mechanics.

READ: `gap-filter-ls-opus.md` 1–445 (Claude Opus 5.5), `gap-filter-ls-check-astra.md` 1–563 (Codex astra), and `gap-hs-check-astra.md` 1–232 (Codex astra), all in full. Existing results used, without re-derivation:

- EXP is the exact finite-time identity for the boost of **half-integer** spins `5/2,7/2,...`. Integer spins above 5/2 are excluded from the counted set.
- Each unnormalized sector trace increases with the boost. The odd fraction and its excess need not increase.
- `Delta=(1-p)(E[N_hi|odd]-E[N_hi|even])`. The two conditional laws must keep their own denominators; unconditional tail bounds do not bound the odd-conditioned law.
- `p(1)=p(s_*) exp(-a integral Delta ds/s)`. EXC is an extra comparison with a modified SU(2) transfer, not an equivalence with every possible proof of E17.
- For the original E17/FQ consumer, a gain `c_0` must match the already supplied rate: `c_0 >= -log(eta_0)/2`, unless a new lower bound for `S_ev` is proved. EXC-W would beat a fixed exponential rate as `L_i>=a` grows.
- Boosting high spins keeps the spatial multiplier fixed. It creates no identification with a finite-group transfer and need not preserve a pointwise positive kernel.
- High-free odd states exist. Their existence gives no lower bound on their normalized weight. No positive multi-time spin history is supplied.
- The earlier operator-order comparison, localization necessity/dichotomy, universal branching fractions, and numerical dressing bounds failed their check. None is used here.

OPEN: the sign and uniformly positive integrated size of the actual Wilson odd-sector excess, including every specified spatial twist and growing box. No GUIDE number is a premise.

## Step 3 — the exact one-slice demand

Use spatial periods `(L_2,L_3,L_4)=(a,c,d)`, `a>=3`, `c,d in {a,2a}`, time `t=a`, and `n=3acd`. For every required spatial twist `m` with `m_2=0` and `i=3,4`, retain the full physical Hilbert space and multiplier `B_m` of (E1). Put

\[
 H_e=\sum_{j\in\{5/2,7/2,\ldots\}}\Pi_{j,e},\quad N=\sum_eH_e,
 \quad L_s=s^{N/2}L_1s^{N/2}.
\]

For a joint edge-spin projection `E_j`, the law is

\[
 \mu_s(\mathbf j)=\frac{\operatorname{Tr}(E_{\mathbf j}L_s^a)}{\operatorname{Tr}L_s^a},
 \qquad O=\mathbf1_{\langle\omega_i,C(\mathbf j)\rangle=1},\quad p_s=\mu_s(O).
\]

READ (EXP and its check): these are nonnegative probabilities. The winding condition refers to one chosen pairing. Write `n_-(s)=E_s[N|O]`, `n_+(s)=E_s[N|1-O]`. Exactly,

\[
 \Delta(s)=(1-p_s)(n_-(s)-n_+(s)),\qquad
 J_{a,m,i}(\beta,S)=\int_1^S\Delta(s)\,\frac{ds}{s}
 =\frac1a\log\frac{p_S}{p_1}.                    \tag{1}
\]

**OPEN — EXC as tested here.** Find a compact interval `I` of nonzero length inside the requested order-one window, one finite endpoint `S>1`, and `c_0>0`, independent of size, twist, and beta in I, with `J>=c_0`. An eventual version may start at one fixed `a_0`. The literal all-size version additionally needs the finitely many smaller sizes. The natural endpoint `S(beta)=r_V^{2T}(beta)/r_{5/2}(beta)` varies with beta; either state that variation explicitly or choose a single endpoint. Continuity makes its supremum finite on compact I, but does not equate its response to that at a fixed endpoint.

There is no need for `Delta(s)>=0` at every s. The integrated positive part must exceed the integrated negative part by at least `c_0`. Equivalently the logarithmic average excess is at least `c_0/log S` **edges per slice**, not a fixed fraction of all `3acd` edges. An integral of order `kappa L_i` would give an area exponent. A very small fixed positive kappa would still suffice eventually; the failed numerical “spectator” estimates cannot exclude that possibility.

For the original consumer retain `g_0=-log(eta_0)/2`: (1) gives `p_1<=exp(-c_0 a)`, and this supplies the already named E17 rate only if `c_0>=g_0` (or if a corresponding stronger `S_ev` lower bound is supplied). This rate condition is prior work from row 873, not a new reduction.

The finite-group comparison does not identify the boosted endpoint's law. READ: `gap-q8test-opus.md:37–58,189–220`, with the arithmetic repairs accepted by row 873. The charged-space norm distinguishes SU(2) from U(1), Q8 and 2T. That distinction alone orders neither `n_-` and `n_+` nor their beta-dependent response.

## Step 4 — endpoint attempt: an actual negative response at large boost

The attempted proof was to make the high channel cheap enough that the odd sector must gain. The following exact calculation shows where that argument fails. It uses the actual spatial Wilson multiplier, not an auxiliary matrix or an assumed positive spin history.

**PROVED here — large-boost sector reversal.** Fix one admissible finite torus, beta>0, a spatial twist, time t=a, and direction i. Let `A_i=acd/L_i` be the number of i-edges crossing the cut, and `epsilon_i=(-1)^{A_i}`. Then

\[
 \max\operatorname{spec}(N|\mathcal H_{\epsilon_i})=n,
 \qquad
 \max\operatorname{spec}(N|\mathcal H_{-\epsilon_i})=n-L_i.       \tag{2}
\]

For `A_i` even this implies

\[
 p_s=C_{a,m,i,\beta}\,s^{-aL_i}(1+O(s^{-1})),\qquad
 \Delta(s)=-L_i+O(s^{-1})\quad(s\to\infty),                    \tag{3}
\]

where `C>0`. In particular Delta is strictly negative for sufficiently large s on every even-a admissible torus. The threshold and the error constants are only fixed-volume constants. They are not uniform in a or asserted to precede the natural endpoint.

*Proof of (2).* The set of all spatial edges is a mod-two cycle, since every vertex has degree six. Its cut pairing is `A_i mod 2`. In any physical spin block the half-integer edges C form a cycle. Thus the integer-spin edges `D=E\C` form a cycle too. If the block has parity opposite to the all-edge cycle, D has odd i-winding. Project D onto the coordinate i-circle. Its image is the nonzero one-cycle, so it contains every one of that circle's `L_i` edges. Consequently D has at least `L_i` distinct edges. Integer-spin edges are never high; hence `N<=n-L_i` in that sector.

Both bounds are attained. Partition E into all the straight coordinate circles, each edge in exactly one circle. The product of their spin-5/2 Wilson characters is a nonzero gauge-invariant function: at the identity every factor equals six. Every edge lies in its spin-5/2 Peter–Weyl block. This gives N=n and parity epsilon_i. Replace the character on one i-circle by the trivial character. That circle's edges now have spin zero, all others remain high, and the cut parity flips. This gives N=n-L_i. These constructions do not assume that the vectors are eigenvectors of L.

*Passage to the actual transfer.* Let `Q_q=1_{N=q}` and `K_q=Q_q K_1`. Within either sector,

\[
 K_s=\sum_{q=0}^{M_\sigma}s^qK_q,\qquad
 Z_\sigma(s)=z^{nt}\operatorname{Tr}_{\mathcal H_\sigma}(K_sB_m)^t,
 \quad M_\sigma=\max\operatorname{spec}(N|\mathcal H_\sigma).
\]

This is a polynomial of degree exactly t M_sigma. Indeed the coefficient of its highest possible power is

\[
 A_\sigma=z^{nt}\operatorname{Tr}_{\mathcal H_\sigma}
       (K_{M_\sigma}^{1/2}B_mK_{M_\sigma}^{1/2})^t>0.             \tag{4}
\]

The operator in (4) is nonzero positive trace class: `K_M` has a nonzero sector range, and `B_m>=exp(-beta|P|)I`. Cyclicity justifies (4); no sign is asserted for the other polynomial coefficients. Hence `Z_sigma(s)=A_sigma s^{tM_sigma}(1+O(s^{-1}))`. Its logarithmic derivative gives `n_sigma(s)=M_sigma+O(s^{-1})`. For `A_i` even, insert `M_+=n`, `M_-=n-L_i` into (1). This proves (3). For `A_i` odd, instead

\[
 1-p_s=(A_+/A_-)s^{-aL_i}(1+O(s^{-1})),\qquad
 \Delta(s)=L_i(A_+/A_-)s^{-aL_i}(1+O(s^{-1})).                   \tag{5}
\]

Thus the large-boost behavior depends on the parity of the transverse area. All steps are finite written algebra.

**What this establishes.** On even-a boxes, `J(beta,S)` tends to minus infinity as S tends to infinity. “Increase the endpoint until EXC holds,” or an assertion `Delta>=0` for every positive boost, is false on the actual Wilson family. An odd wrapping class can eventually contain **fewer** high edges: its integer-spin complement must remove a winding loop from the nearly all-high background. This is a genuine response-sign test, not a counterexample to EXC at one fixed natural endpoint.

**What remains open.** Nothing in (2)–(5) locates the sign change in `[1,S(beta)]`, where `S(beta) r_{5/2}=r_V^{2T}<1`. Taking a fixed-volume large-s limit does not locate a transition at a volume-independent endpoint. It also says nothing about the required positive net response on a smaller interval. The attempted unbounded-boost proof stops here.

**Binding controls.** The same calculation works for U(1), Q8, 2T and Z2 if the selected high set is a nonempty set of centre-odd irreducibles, is closed under duals, and excludes the trivial representation. Products of a chosen odd representation's characters on the coordinate circles provide the saturating states. The complement-cycle bound is group-blind. For U(1) one can select `|q|>=5`, q odd; for Q8 select V; for 2T select V; for Z2 select the sign representation. These are tests of the algebra, not identifications with the SU(2) filter. Q8 and Z2 have no separate higher odd irrep: selecting their odd irrep also boosts the fundamental carrier. Their s=0 odd sector is then zero, so no logarithm at s=0 is used.

## Step 5 — the positive-kernel proof fails at the proposed endpoint

A second attempt would use conditional link laws or positive surface weights throughout the boost. The actual temporal edge kernel fails the required sign condition already at the natural endpoint in the requested window.

**PROVED here.** For every `beta in [23/10,13/5]`, let `S(beta)=r_V^{2T}/r_{5/2}`. The normalized one-link convolution kernel of `C_lo+S C_hi` is negative at `g=-I`.

Indeed the uniformly convergent character series is

\[
 k_s(g)=\frac{e^{\beta x(g)}}{z}+(s-1)h(g),\qquad
 h(g)=\sum_{j\in\{5/2,7/2,\ldots\}}d_j r_j\chi_j(g).
\]

All selected characters have `chi_j(-I)=-d_j`. Thus

\[
 k_S(-I)=e^{-\beta}/z-(S-1)\sum_{j\ \mathrm{high}}d_j^2r_j
 \le e^{-\beta}/z-36(r_V^{2T}-r_{5/2}).                         \tag{6}
\]

Here are hand bounds with substantial room. GL4 gives

\[
 r_{5/2}\le(\beta/2)^5/720\le(13/10)^5/720<1/180,
\]

since `13^5=371293<400000`. The 2T class data in `gap-q8test-opus.md:30–58` give `E_{2T}x^2=1/4` and a symmetric x-law. Therefore

\[
 r_V^{2T}=\frac{\mathbb E[x\sinh(\beta x)]}{\mathbb E e^{\beta x}}
 \ge\frac{\beta}{4e^\beta}>\frac{23}{1080}>\frac1{48}.
\]

The strict middle bound uses `beta<3` and `e<3`; the latter follows from `n!>=2^{n-1}` for `n>=2`, with a strict inequality in the tail. Also `z>=1` and `e^beta>1+beta`, so `e^{-beta}/z<10/33`. Hence

\[
 k_S(-I)<\frac{10}{33}-36\left(\frac1{48}-\frac1{180}\right)
 =\frac{10}{33}-\frac{11}{20}=-\frac{163}{660}<0.                \tag{7}
\]

There is no numerical approximation or phase input in this proof. The high tail can only make the kernel more negative at -I. Continuity makes the kernel negative on an open set, not merely at one point.

**Scope.** The convolution remains a positive operator: its Peter–Weyl eigenvalues are positive. The full transfer and its one-slice law remain positive in the sense required by EXP. Equation (7) does not assert that every gauge-projected full kernel is negative, nor rule out a different positive representation. It refutes the particular step that treats these temporal edge weights as a positive Gibbs density throughout `[1,S(beta)]`. Row 873 already warned that operator positivity was insufficient; (7) locates an actual failure at the natural endpoint. In particular the s=1 five-staple estimates cannot be transported to this path by the ordinary Wilson conditional-density argument.

**Binding controls.** For any compact group with central -1 and any selected centre-odd irreducible set, the identical formula is `k_s(-1)=k_1(-1)-(s-1)sum_selected d_rho^2 r_rho`. Thus operator positivity and kernel positivity separate also for U(1), Q8 and 2T. For Z2 it reads exactly `k_s(-1)=1-s tanh(beta)`, negative for `s>coth(beta)`. None of the comparison groups acquires the SU(2) charged-space bound. A sign-changing kernel is not itself evidence against EXC.

Repo follow-up before this calculation: the completed query `boosted.kernel|high.spin.{0,70}pointwise|spin.?5/2.{0,70}kernel` on the five refs returned only `pr/10141:research/ym4d/library/ro1.md:364`. Read 354–366: its “boosted kernel” is a positive vector Gram kernel under imaginary spacetime rotations. It concerns a different boost and supplies no kinetic-kernel result. Local gap-file searches found the existing warning, but no endpoint calculation (6)–(7).

## Step 6 — response positivity: what can actually be proved

The third attempted proof uses the increase of high-spin occupation under its own fugacity. That increase does hold for the **total** selected count in each sector, even without positive history weights. It does not compare sectors.

**PROVED here.** Set `x=log s`, `F_sigma(x)=log Tr_sigma L_{e^x}^t`, and `n_sigma=Tr_sigma(N L^t)/Tr_sigma L^t`. Then

\[
 F_\sigma''(x)\ge0,\qquad \frac{d n_\sigma}{dx}\ge0.             \tag{8}
\]

This is not a monotonicity theorem for a single fixed-j density, and not a monotonicity theorem for p.

*Proof.* EXP gives `F_sigma'=t n_sigma` and `L'=(NL+LN)/2`. Differentiating the inserted trace and cycling factors gives, with all traces restricted to the sector,

\[
 F_\sigma''=
 \frac{t}{Z_\sigma}\sum_{k=0}^{t-1}\operatorname{Tr}(N L^k N L^{t-k})
 -t^2 n_\sigma^2.                                             \tag{9}
\]

Choose an orthonormal eigenbasis of positive compact L in that sector. Write its eigenvalues as lambda_r, `N_{rq}=<r,Nq>`, and `w_r=lambda_r^t/Z_sigma`. The diagonal part of (9) is

\[
 t^2\left[\sum_r w_r N_{rr}^2-\left(\sum_r w_r N_{rr}\right)^2\right]\ge0.
\]

The remainder is

\[
 \frac{t}{Z_\sigma}\sum_{r\ne q}|N_{rq}|^2
              \sum_{k=0}^{t-1}\lambda_r^{t-k}\lambda_q^k\ge0.   \tag{10}
\]

All sums are legitimate. N is bounded by n, L is trace class, and Holder bounds each trace term by `n^2 Tr L^t`; alternatively the displayed nonnegative sums converge to those traces. Trace-norm differentiation follows from the bounded exponential congruence. This proves (8).

**Where the proof of EXC stops.** Put `D(x)=n_-(e^x)-n_+(e^x)`. Equation (8) says each summand increases, not that D is positive. More explicitly,

\[
 D(x)=D(0)+\frac1t\int_0^x(F_-''(y)-F_+''(y))\,dy.             \tag{11}
\]

The positive terms (9)–(10) are normalized within different sectors. They give no sign for their difference. In fact Step 4 proves `D(x)->-L_i` on every even-a box. Thus the step “both susceptibilities are positive, so the odd sector gains at least as much” is false on this very operator family. On the bounded natural interval, neither D(0) nor the requisite relative susceptibility estimate has been bounded. Formula (11) is recorded as the exact failing comparison, not offered as a new supplier or as progress on EXC.

**Binding controls.** The proof of (8) uses only positive trace-class L, bounded self-adjoint N, and a commuting sector projection. It holds for the U(1), Q8, 2T and Z2 choices in Step 4. The controls therefore exclude treating (8) itself as a confining input. Their different charged-space spectra must enter a genuine **relative** estimate, which (9) does not provide.

## Step 7 — how many extra edges, and where?

**PROVED here — translation accounting.** For each orientation alpha in `{2,3,4}`, the sector probability `h_{sigma,alpha}(s)=E_s[H_e|sigma]` is independent of the position of e. Put `V=acd` and `d_alpha=h_{-,alpha}-h_{+,alpha}`. Then

\[
 n_--n_+=V\sum_{\alpha=2}^4d_\alpha,\qquad
 \Delta=(1-p_s)V\sum_{\alpha=2}^4d_\alpha.                    \tag{12}
\]

For any **deterministic** region R containing `r_alpha` edges of orientation alpha, its sector excess is exactly

\[
 E_s[N_R|O]-E_s[N_R|1-O]=\sum_\alpha r_\alpha d_\alpha.        \tag{13}
\]

*Proof.* A lattice translation takes a spatial sign cocycle to a cohomologous one. Their quotient is the coboundary of an edge sign assignment. Combining translation with that centre change of variables preserves `B_m`; it also preserves `K_s` up to edge permutation. A translated cut cocycle differs from the old cut by an exact cocycle, whose centre action is a vertex gauge transformation and hence the identity on the physical space. Thus this unitary transformation preserves L_s and both sectors and sends `H_e` to the translated edge projection. Invariance of the trace proves the assertion and its sums. This proof applies also to twisted m and uses no positive classical history.

Consequently a line of `L_i` fixed i-edges has excess `L_i d_i`, while the entire orientation-i family has excess `V d_i`. The ratio is `L_i/V=1/A_i`. For example, **if** the orientation-i contribution is `kappa L_i`, its contribution on a particular fixed line is only `kappa L_i/A_i`, of order `1/a` on these shapes. A randomly located winding carrier can therefore have order-a total excess without producing order-a excess in any preselected thin tube. A claim about a configuration-dependent tube needs the tube-selection law; (13) does not apply to a random R correlated with the spins.

**ARGUED — plausible scale, no asserted sign.** A flux-induced change of local high-spin probability of order `1/a^2`, summed over order `a^3` edges, could produce order-a sector excess. Its contribution to Delta retains the factor `1-p_s`; that factor must not suppress the contributing portion of the boost interval. EXC itself asks for only order-one logarithmically averaged excess, corresponding to a signed mean bias of order `1/a^3` when `1-p_s` stays of order one. These are small differences of extensive populations. A small unconditional high-spin density at s=1 does not rule them out, and supplies neither their sign nor their response at s>1. If an actual flux carrier has a nonzero integrated high-spin excess per unit length, the natural scaling is `J=kappa L_i`; how small kappa is would affect the onset size, not by itself invalidate EXC. Neither the existence of that carrier nor `kappa>0` has been proved.

The topological minimum applies to half-integer edges, not high edges. The already checked high-free winding state prevents a deterministic lower bound `N_hi>=delta L_i` on odd configurations. This existing counterexample is reused, not reconstructed as new work. Equations (12)–(13) also explain why a claim that the excess must first be localized is not justified.

**Binding controls.** Translation accounting and the count scalings hold for U(1), Q8, 2T and Z2 on the same periodic graphs and centre twists. They select no theory. For the Coulomb control, the existing Maxwell calculation gives order-one p rather than a scale-growing exponent; for Z2 the existing fixed-beta bound gives `p->1/2`. A proof must compare the actual conditional high-spin laws, not infer their difference from homology, symmetry, or these scalings alone.

## Step 8a — a controlled positive comparison, with the existing electric result credited

READ: `gap-crux-skeleton-max.md:137–175` already treats zero spatial coupling at arbitrary temporal beta. Lemma A1 bounds the electric odd-sector norm by `r_{1/2}^{L_i}`; Lemma A2 controls its full gauge-projected trace. The subsequent continuation to the isotropic model stops at a missing normalized response estimate. That electric seed and failed continuation are prior work. I do not reopen either. What is not supplied there is the **relative high-spin boost** in (1). The calculation below addresses only that comparison; it will not be called a Wilson-isotropic EXC proof.

First a useful strict comparison can be proved without the earlier GUIDE decimals.

**PROVED here.** For every beta>0,

\[
 r_V^{2T}(\beta)>r_{1/2}^{SU(2)}(\beta).                        \tag{14}
\]

The already read class data give `z_T=(2 cosh beta+6+16 cosh(beta/2))/24`. GL3's Bessel series gives `z_U=2I_1(beta)/beta=sum_{n>=0} b_n beta^{2n}`, with `b_n=1/(4^n n!(n+1)!)`. Write `z_T=sum a_n b_n beta^{2n}`. Then

\[
 a_0=1,\qquad a_n=\frac{4^n+8}{12\,\mathrm{Cat}_n}\quad(n\ge1),
 \qquad \mathrm{Cat}_n=\frac{(2n)!}{n!(n+1)!}.
\]

In particular `a_0=a_1=a_2=1` and `a_3=6/5`. The factorial formula gives `Cat_{n+1}/Cat_n=(4n+2)/(n+2)`. For n>=1 the sign of `a_{n+1}-a_n` is the sign of

\[
 (4^{n+1}+8)(n+2)-(4^n+8)(4n+2)=6(4^n-4n)\ge0.
\]

The last inequality holds at n=1 and propagates by multiplication by four; it is strict for n>=2. Therefore a_n is nondecreasing and not constant. With probabilities `w_n=b_n beta^{2n}/z_U`, differentiation of the absolutely convergent series gives

\[
 \beta\frac{d}{d\beta}\frac{z_T}{z_U}
 =\operatorname{Cov}_{w}(a_n,2n)
 =\frac12\sum_{n,m}w_nw_m(a_n-a_m)(2n-2m)>0.                   \tag{15}
\]

Strictness follows, for example, from the n=2, m=3 terms. The logarithmic derivatives of z_T and z_U are their fundamental eigenvalues (`gap-q8test-opus.md:60–63`). This proves (14). Also `r_V^{2T}<1`, since the finite-beta class measure gives positive weight to x<1.

The beta^5 asymptotic difference was already proved at `gap-q8test-opus.md:241`; (14) uses its exact class data to extend the sign to every positive beta. The completed five-ref query `Catalan.{0,60}tetrahedral|tetrahedral.{0,60}Catalan|fundamental.{0,50}2T|2T.{0,50}fundamental|electric.only.{0,50}(boost|high.spin)` returned no matches. The local filter/assumptions search found the existing moment data and small-beta expansion, not (14) or the following relative trace comparison. No global novelty claim is made.

## Step 8b — EXC holds in the electric reference, with the full trace retained

**PROVED here, reference-model scope only.** Replace the spatial multiplier by `B=1`, retain the actual gauge-invariant SU(2) Hilbert space on the three-dimensional torus, and keep temporal beta in any fixed compact `I` inside `(0,infinity)`. Denote this reference's odd fraction by `p_s^{el}`. At the natural endpoint `S(beta)=r_V^{2T}/r_{5/2}`,

\[
 \frac1{aL_i}\log\frac{p_{S(\beta)}^{el}}{p_1^{el}}
 \longrightarrow \gamma(\beta):=
       \log\frac{r_V^{2T}(\beta)}{r_{1/2}(\beta)}>0              \tag{16}
\]

uniformly in beta and the admissible aspect ratios. Thus this reference has `J^{el}>=(min_I gamma)L_i/2` for all sufficiently large a. This is a comparison of complete normalized traces, not two isolated flat-plane terms.

*Proof.* At either endpoint let `w_j` be the one-link eigenvalue. At s=1 its largest nontrivial and largest odd eigenvalue is `q_1=r_{1/2}`. At s=S these two maxima are `q_S=r_V^{2T}`, attained at spin 5/2, by (14) and the inherited strict decrease of r_j in j. Both q's are below one. Set

\[
 \epsilon_s(a)=\sum_{j>0}d_j^2w_j^a,\qquad
 u_s(a)=\sum_{j\ \mathrm{half\!\!\!-integer}}d_j^2w_j^a.
\]

Uniform factorial decay and compactness provide `C>=1` and `q<1` such that at both endpoints

\[
 \epsilon_s(a)\le C q_s^a\le Cq^a,\qquad u_s(a)\le Cq_s^a.     \tag{17}
\]

For clarity, `epsilon_s(a)<=q_s^{a-1}sum_{j>0}d_j^2w_j`; the sum is uniformly bounded, and the endpoint q's have a positive minimum. This proves the asserted uniform constants, without calculating them.

Remove the common scalar `z^{na}` from all traces. The constant state gives the full gauge-projected trace at least one, while dropping gauge projection gives

\[
 1\le Z_s^{el}\le(1+\epsilon_s(a))^n.                          \tag{18}
\]

Reuse A1's crossing argument: an odd spin assignment has at least L_i half-integer edges. For each subset of L_i edges, dropping the gauge projection bounds its trace by `u_s(a)^{L_i}(1+epsilon_s(a))^{n-L_i}`. Sum over those subsets. Conversely the unit character on one simple winding line, in spin 1/2 at s=1 or spin 5/2 at s=S, is an odd eigenvector of K_s with eigenvalue `q_s^{L_i}`. Hence

\[
 \frac{q_s^{aL_i}}{(1+\epsilon_s(a))^n}
 \le p_s^{el}
 \le {n\choose L_i}(Cq_s^a)^{L_i}(1+\epsilon_s(a))^n.           \tag{19}
\]

Every trace in this step is diagonal in spins; its multiplicity on the physical subspace is at most the full Peter–Weyl multiplicity. No sign of a multi-time spin expansion is needed.

Take logarithms of (19), use `binom(n,L_i)<=n^{L_i}` and `log(1+epsilon)<=epsilon`, and subtract the endpoint bounds. Since `a<=L_i<=2a` and `n<=12a^3`,

\[
 \left|\frac{1}{aL_i}\log\frac{p_S^{el}}{p_1^{el}}-
       \log\frac{q_S}{q_1}\right|
 \le \frac{\log(12Ca^3)}a+24Ca q^a\longrightarrow0.             \tag{20}
\]

The convergence is uniform. The first term vanishes, for example using `log a<=sqrt(a)` for a>=4 and then division by a. For the second, the ratio of consecutive terms `a q^a` tends to q<1, so its tail is bounded by a geometric sequence. Finally continuity and (14) give `min_I gamma>0`. This proves (16) and its lower bound.

For the literal single-endpoint quantifier, choose any beta_0 inside the requested window and fix `S=S(beta_0)`. The strict inequalities `r_{1/2}(beta)<S r_{5/2}(beta)<1` persist on a sufficiently small compact interval of positive length around beta_0. The identical proof gives (16) there with `gamma=log(S r_{5/2}/r_{1/2})`. Thus the positive reference test is not an artifact of allowing S to depend on beta.

**Why this does not prove the requested EXC.** Restoring the spatial multiplier is exactly the nontrivial step. The existing spectral comparison behind E18, applied in both directions at either endpoint, gives only

\[
 |\log p_{s,b}-\log p_s^{el}|\le2bn a,
 \qquad |J_b-J^{el}|\le4bn,                                  \tag{21}
\]

where `B_b=exp(b sum_p eta_p x(U_p))` and b is the spatial coupling. The reference gain is order L_i, while this comparison costs order `b a^3`. With this estimate one reaches only b of order `a^{-2}`, not the isotropic b=beta. Equation (21) is a reuse of the already proved crude comparison, not a new volume-loss no-go. The older electric-reference continuation also stopped at the normalized magnetic response. No argument here bounds its effect on (16) at b=beta.

**Binding controls.** The argument (17)–(20) uses the minimum winding length, positive spectral coefficients, finite one-link trace and an increase of the maximal odd kinetic eigenvalue while all nontrivial eigenvalues remain below one. It applies equally to an electric-only U(1), Q8, 2T or Z2 reference when those inequalities hold. In Q8 and Z2 the boost changes their sole odd carrier. For 2T it can change V; for U(1) it can make a selected odd charge the largest odd coefficient. There is no Coulomb or finite-group freezing conclusion for these references. Their full spatial interactions are precisely what this calculation omits. Therefore (16) is a positive consistency test for the proposed response scale, not an SU(2)-selective confinement argument.

## Step 9 — the remaining comparison and the binding tests

The exact next comparison can be stated without identifying the wrong one-slice law. Fix temporal beta and its endpoint S. Write `M(U)=sum_spatial_p eta_{m,p} x(U_p)` and use the isospectral transfer

\[
 A_{s,b}=z^n e^{bM/2}K_s e^{bM/2},\qquad
 d^{\mathrm{mag}}_{s,b}=
 \frac{\operatorname{Tr}(P_- M A_{s,b}^a)}{\operatorname{Tr}(P_- A_{s,b}^a)}
 -\frac{\operatorname{Tr}(M A_{s,b}^a)}{\operatorname{Tr}A_{s,b}^a}.
\]

**PROVED identity; not a closure.** `A_{s,b}` and `L_{s,b}` have the same nonzero sector spectra: write them as `XX*` and `X*X`, with `X=z^{n/2}e^{bM/2}K_s^{1/2}`. Differentiation gives `partial_b A=(MA+AM)/2`. Cycling the trace of its integer power therefore gives `partial_b log p_{s,b}=a d^{mag}_{s,b}`. Consequently

\[
 J_{\beta}=J^{el}+
       \int_0^\beta(d^{\mathrm{mag}}_{S,b}-d^{\mathrm{mag}}_{1,b})\,db. \tag{22}
\]

The expectation in this formula is at the **magnetic cut** A; it is not the spin-law expectation of N at the kinetic cut L. In particular it is not obtained by applying an s=1 Wilson conditional-density formula at s=S. All derivatives are trace-norm valid because M is bounded on this finite torus.

**OPEN.** At isotropic b=beta, prove that the integral in (22) does not erase the positive reference gain, or prove EXC directly without this path. A sufficient quantified margin would be

\[
 \int_0^\beta(d^{\mathrm{mag}}_{S,b}-d^{\mathrm{mag}}_{1,b})\,db
 \ge -J^{el}+c_0
\]

uniformly over the original I, sizes and twists, with the original rate condition. This is explicitly an equivalent residual of this continuation, not a weaker lemma advertised as progress. The available absolute estimate is only `4 beta n`; sector convexity supplies no sign, and the natural endpoint prevents the attempted positive-edge-law proof. No bound of the required order has been obtained. The large-boost sign reversal is not a counterexample on this bounded path.

The binding controls retain their distinct logical force:

| Control | Established test and exact source | Consequence here |
|---|---|---|
| U(1) Coulomb | READ `gap-z2parity-astra.md:485–501`: compact free Maxwell has odd fraction `sum_odd exp(-e^2 n^2/2)/sum_all exp(-e^2 n^2/2)>0`, independent of size. Wilson-cosine matching is not proved there. | A corresponding positive-transfer boost cannot have a uniform EXC integral on this Maxwell family, by EXP's endpoint bound. Failure for the actual Wilson U(1) Coulomb family remains ARGUED pending that matching. The Sym^5 V norm hypothesis already fails for U(1); it is not a counterexample to the SU(2) filter. |
| Q8 | READ `gap-cf-astra.md:163–189`: frozen `Z^v/Z^0=3/23`, hence odd fraction `10/23`, with beta sent to infinity at each fixed torus first. | The frozen family excludes EXC for any admissible positive boost. It supplies no fixed-beta result near 2.3. The carrier V is also the sole odd irrep; it cannot be held fixed while selecting a distinct high V-copy in the finite-group regular representation. |
| 2T | READ `gap-z2parity-astra.md:450–483`: frozen ratio `1/61`, odd fraction `30/61`, with the same order of limits. | Same restriction. Equation (14) is a coefficient comparison, not a comparison of full Gibbs laws. Making one SU(2) eigenvalue equal to this finite-group coefficient does not produce its frozen law. |
| Z2 | READ `gap-z2parity-astra.md:386–442`: at beta=5/2, `p_1(a)->1/2` on the actual admissible growing tori. | For **any fixed finite positive boost** of the odd block, EXP gives `J<=log(1/p_1)/a->0`. This is a fixed-coupling test. On Sym^5 V, Z2's kernel acts as `tanh(beta)`, so it also fails the SU(2) filter bound in this window. |

The last charged-space statement has a direct hand check. Under Z2, -I acts as minus the identity on all of Sym^5 V. Thus its normalized convolution is `tanh(beta) I`. In this window `e^{2 beta}>1+2 beta>3`, so `tanh(beta)>1/2`, whereas the SU(2) factorial filter bound is below `1/180`. No Z2 conclusion is silently transferred to SU(2).

For the p-bounded-below cases, the used inequality is exactly row 872's checked `J<=log(1/p_min)/a`; no new proof of the phases or of the flat counts is claimed. The positive electric reference passes all four tests because their spatial interactions are absent there. The large-boost and convexity lemmas also pass them because they claim no confinement.

## Step 10 — assessment and delivery record

**ARGUED.** EXC is plausible as an additional dynamical statement at order one; it is not supported by a proved sign estimate for the isotropic one-slice law. Its scale is coherent: order-one integrated excess is enough for a bare exponential bound, and order-length excess occurs in the complete electric reference at the natural endpoint. For the actual Wilson model, the answer to “does the odd sector carry extra high-spin edges?” is still unknown on the specified boost interval. Topology alone permits none; sufficiently large boosts actually give a deficit on even-a tori. There is no justified numerical estimate of the excess in a wrapping region. A fixed tube's count must also respect (13).

**PROVED here, subject to an independent check:** (2)–(5), the actual fixed-volume large-boost behavior; (6)–(7), a sign-changing temporal edge kernel at the natural endpoint for beta in [2.3,2.6]; (8)–(10), within-sector monotonicity of the total high count; (12)–(13), translation accounting; (14), the strict fundamental coefficient ordering; (16)–(20), a full-trace positive EXC comparison with zero spatial coupling; and (22), the exact location of the missing relative magnetic response. None proves isotropic EXC or E17.

**READ:** existing EXP, parity, rate correction, avoidance support and convolution results, with the sources and lines above. **GUIDE:** no numerical guide was run or used as a premise. The earlier measured high-spin densities and recalled tensions were deliberately not used to assign a sign or a bound. **OPEN:** isotropic EXC, its original E17/FQ rate, and the relative response needed to restore the spatial multiplier.

Only `library/gap-exc-astra.md` is a deliverable. The requested pinned checkout is retained. No source, registry, FINISH row, ledger or audit record was changed. No subagent, simulation, machine enumeration, external post, commit or push was performed. The new arguments are an author proof probe, not an independent check. Work remains local and uncommitted in this file.

Final author check: read the completed note in bounded ranges and checked the sector polynomial's leading term, both trace derivatives, the rational endpoint bounds, and the two-sided normalized electric trace estimate by hand. Corrected a formula delimiter and replaced wording that could have asserted an unproved magnetic-response obstruction. This is self-review only; no independent verification was performed. File-status checks found this note as the sole new path and no tracked-file changes.

RESULT: OPEN — isotropic EXC and its E17/FQ consumer are neither proved nor refuted; the full electric-only reference has a positive order-length boost response, but no bound for the relative magnetic response at the required scale was obtained, while actual large boosts reverse the sign on even-a tori and the natural endpoint has a negative single-link kernel. Written proofs only; no scientific or audit status granted.
