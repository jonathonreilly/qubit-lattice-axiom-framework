# Independent hostile review of LANEA55

## PRE-STATED — 2026-10-29 06:31:59 UTC

Reviewer: Codex, independent cross-family review requested by the owner. Target: `LANEA55.md` and its 17 claimed lane-A inputs to the `[S26-BANKED]` chain. No derivation or target-file inspection preceded this statement. This review makes no claim to have verified a Git revision; Git is forbidden by the task.

Primary falsifiers, declared before calculation:

1. BA-3: an invalid noncommutative quadratic cancellation, an inadequate exact tail bound, or a downstream invocation outside `s <= 1/27` refutes the corresponding coefficient-9 claim or its application.
2. Theorem 4.2: one printed `(eta,r_0)` interval failing its stated condition; a missing quantified kappa minimum; or use of a mass/uniformity hypothesis not implied by Proposition W refutes the stated uniform claim. A finite collection of successful sample points cannot establish a continuous minimum.
3. Other lane-A inputs: reconstruct the operator domains, norms, inverse identities, constants and uniformities. A missing boundary condition, projection, zero-mode exclusion or circular invocation leaves the affected claim unverified; an explicit contradiction refutes it.
4. Bookkeeping: resolve symbols by source and locating string. Check cited locations against their actual current content. Compare maxima with sums quantitatively. A stale symbol, premise, interval or line reference counts as a finding even if repair is easy.
5. Checks `la55_1`–`la55_4`: inspect their predicates and their domain; determine whether they can reject a mathematical error. Self-defined expected answers, vacuity and sample-only generalization do not discharge a theorem.

Accepted premises are only those explicitly attached to each conditional statement. In particular Proposition W, Theorem GU and any unverified nonlinear/physical bridge remain visible dependencies. Status vocabulary: review findings **CONFIRMED / NOT-VERIFIED / REFUTED**; mathematical claims **PROVEN / ARGUED / CONDITIONAL / GAP / OPEN**. A confirmed conditional calculation is not proof of its antecedent or of Yang–Mills existence.

Read scope: named source files only, with targeted string searches and bounded ranges for large files; no snapshots or audit ledgers. Two discretionary procedural reads are reserved for `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `docs/ai_methodology/skills/review-loop/SKILL.md`. Only this deliverable may be written. Findings will be appended incrementally, followed by a final summary and a precise bankable scope.

## Findings (incremental)

### R1 — CONFIRMED: the sharper BA-3 plaquette coefficient is independently proved

**Attachments:** LANEA55 §14, locating strings “Degree 2 (exact)” and “Degree ≥ 3”; §15 “LA24 — BA-3, extension”; BFT_A.md:122–129, “3.3 BA-3”; BFT_A.md:2496–2507, “28.6 Corollary WR”.

For ordered letters a_1,...,a_4 with ||a_i||_HS <= s, put t=4s and E=e^t. Expanding the product to degree two gives
P_1=sum a_i and P_2=sum a_i^2/2+sum_{i<j}a_i a_j. Thus P_2-P_1^2/2=sum_{i<j}[a_i,a_j]/2, with norm at most 6s^2. This is a cancellation proof, independent of the author's noncommutative script.

For the remaining terms, submultiplicativity gives
f(t)=(E-1-t-t^2/2)+t(E-1-t)+(E-1-t)^2/2+(E-1)^3/[3(2-E)].
The logarithm series is absolutely convergent when E-1<1. Every summand has a nonnegative power series starting at degree >=3: the last uses sum_{j>=0}(E-1)^j. Therefore f(t)/t^2 is increasing throughout this domain; this proves monotonicity at ALL orders, not just the first twelve coefficients checked by la55_2 B3.

Independent exact-rational calculation used
E_lo=sum_{j=0}^{12}t^j/j!,
E_hi=E_lo+(t^13/13!)/(1-t/14).
The tail bound follows because every successive omitted term has ratio <=t/14. It gives the following strict rational enclosures of 6+f(4s)/s^2:

| s | lower | upper |
|---|---:|---:|
| 1/40 | 7.815545 | 7.815546 |
| 1/27 | 8.882077 | 8.882078 |
| 1/24 | 9.335437 | 9.335438 |
| 1/20 | 10.223492 | 10.223493 |

These terminating decimals denote exact rationals. In particular the claimed **9 is PROVEN for every 0<=s<=1/27**, including complex matrices in the HS norm. Failure of this majorant at 1/24 is NOT a counterexample to the actual BCH inequality.

The source requires j<k and L>=3, giving s_j<=eta/3. BFT_A §3.3's sufficient eta<=1/(20p_L) is inside the domain, and WR(b)'s eta<=1/9 gives s_0<=1/27. Thus the actual BA-3/WR consumers inspected are covered. The soft clause is a distinct claim and is not certified by this proof. The old word-size citation still yields 9(4s)^2=144s^2; it is an inadequate justification, not a refutation of 9.

### R2 — REFUTED: LANEA55's asserted factor-two counterexample to FT is invalid in its pinned centred-root setting

**Attachments:** LANEA55 §11 precision P2, “the max form is false by up to a factor 2”; repeated §20 item 5(b). Source: BFT_B.md:3589 (“Root convention: block centres”), :3603 (“Lemma FT”), :3696–3710 (proof).

The printed proof indeed stops at a SUM. It does not follow that the printed MAX bound is false. The actual geometric coefficient is smaller than the proof's crude 1.

For a fixed directed link in coordinate mu, an axial path from the block centre uses it only if its endpoint y_mu lies on the appropriate side of the centre and beyond that edge. At most (L-1)/2 of the L possible y_mu values qualify. All other coordinates have at most L choices. Consequently, for each coordinate order and for their average,
|c(X,b)| <= h_L := (L-1)/(2L) < 1/2.
Only one block contributes to h_l^T at b.

Let A=L^{-theta(k-l)}||j||_Pc, B=L^{-3l}||j_0^c||, and g=(1-L^{-3})^{-1}. The already-derived divergence cascade then gives
pi_l(h_l^T psi_l) <= 2d h_L(g A+B)
<=2d h_L(g+1) max(A,B)
<=2d g max(A,B).
The last inequality uses h_L<=1/2 and g>=1. Adding pi_l(j_l)<=A proves the original FT(iii) MAX bound, with no extra factor.

At L=3,d=4 the sharper sufficient funnel coefficient is
8*(1/3)*(27/26+1)=212/39,
strictly below the printed 8*(27/26)=108/13.
**Correction: no inflation is required; factor 1 suffices in the centred-root setting.** Claim status: PROVEN in that setting. The source's separate assertion of being convention-free has not been proved by this argument; no conclusion about arbitrary off-centre roots is banked. LANEA55 supplied no admissible current/link witness for its stronger falsity claim.

### R3 — CONFIRMED: all five strip pairs; new uniform certificate for the full [1/4,4] interval

**Attachments:** LANEA55 §16 “Check la55_3”, and “minimum over kappa”; LINEAR_PACKAGE.md:211–244; PROOF.md:3079–3122, locating strings “Lemma EXP-strip” and “Define eta_*”.

I independently evaluated the four inequalities, using interval arithmetic throughout, rather than the author's endpoint-specific implementation. pi was enclosed by the alternating-series identity pi=16 atan(1/5)-4 atan(1/239), with 20 and 6 terms respectively; the angle identity follows by the tangent addition formula and the first-quadrant value. This also verifies the script's hard-coded pi bracket. Exponentials used degree 12 with the geometric next-term remainder from R1; cosh used degrees 0,2,...,12 and remainder (eta^14/14!)/(1-eta^2/(15*16)). Square roots were enclosed by integer square roots at denominator 10^20.

The following are rigorous LOWER bounds, rounded down to exact multiples of 10^-6, for S1 through S4 margins:
(1/2-rho_beta), (Psi_U/2-e_Psi), (br_V-[2(1+rho_beta)Gamma]^-1), (3/20-f0cond).

| kappa | khat | eta | r_0 | S1 margin | S2 margin | S3 margin | S4 margin |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | .0111 | .57 | .283687 | .014138 | .005688 | .023892 |
| 1/4 | 1 | .0077 | .37 | .325383 | .020636 | .008913 | .014963 |
| 4 | 1 | .0117 | .65 | .239420 | .004752 | .003463 | .033696 |
| 1/4 | 16 | .0037 | .25 | .354395 | .055344 | .032779 | .054846 |
| 4 | 16 | .0082 | .60 | .264956 | .003288 | .002866 | .062283 |

The control eta=.02,kappa=khat=1,r_0=.57 has S1 positive and S2–S4 strictly negative. These are real discriminating arithmetic checks of the displayed sufficient conditions, not checks of the underlying operator identities.

**New test, not claimed to have been pre-registered:** common eta=37/10000 and r_0=1/4, L=3,khat=16, on all kappa in [1/4,4]. I covered this interval by the 64 closed rational intervals
I_j=[1/4+15j/256, 1/4+15(j+1)/256], j=0,...,63.
Every input occurrence of kappa was replaced by its entire interval, and all operations used outward exact interval bounds (including min/max and square roots). All 64 boxes certify all four conditions. Global lower margins are respectively
**353941/1000000, 423/20000, 24951/1000000, 27423/500000**.
Thus **m_* >= 37/10000 for L=3 and every admissible chain with 1/4<=kappa_i<=4**, using khat=16. This is interval coverage, not endpoint interpolation. LANEA55's per-kappa samples alone did not establish this fact.

For arbitrary fixed 0<kappa_-<=kappa_+<infinity, choose one r_0 in (0,sqrt(6)), e.g. r_0=1/4. At eta=0 the four inequalities have strictly positive margins, continuously in kappa on that compact interval. A finite subcover supplies a common positive eta. This proves an existential uniform rate without tabulating a numerical minimum.

### R4 — REFUTED as an unchanged-scope claim: replacing m_*' by m_* narrows a quantified rate interval

**Attachments:** LANEA55 §16 “Every one of those statements survives with m_* in place of m_*'” and “they are existential in the rate”; BFT_A.md:928 (“For 0 <= m < m' < m_*'”), :1077, :1151–1152; PROOF.md:19 (“TOP-cc_m for 0 <= m < m_*'”).

These statements include universal assertions for every m in a specified interval. Theorem 4.2 alone discharges them for **0<=m<m_***, not for the entire interval **0<=m<m_*'**. A proof at a smaller rate gives no estimate at a larger one. Theorem 4.2' remains NOT-VERIFIED here. The existential decay/contraction chain can use a smaller rate, but the originally printed rate scope has not thereby been independently confirmed.

With m_Y=ln(2)/(16L^c), the correct extra requirement is indeed
L^c >= 6 ln(2)/(16m_*).
Choose c AFTER the interval of kappa and the certified rate; recompute the constants that depend on c and on the kernel bound. This preserves existence and k,T-uniformity. On the interval certified in R3, L^c>=260 suffices:
m_*/6 >=37/60000 >7/41600 >ln(2)/4160.
For a general interval no inference from the five samples is legitimate; the added c-condition is required.

Also relabel the unprimed strip bound M and every derived M_f when replacing Theorem 4.2': LINEAR_PACKAGE.md:219–222 explicitly says the two theorems have their OWN constants M, and :238 adopts the primed one thereafter. The same letter is not proof that the constants agree.

### R5 — CONFIRMED: the unprimed analytic kernel theorem, with an independent uniform-alias argument

**Attachments:** LANEA55 §16 items 1–5; PROOF.md:3028–3145 (“Lemma EXP-id”, “Lemma EXP-real”, “Lemma EXP-strip”, “Theorem N2-exp”); LINEAR_PACKAGE.md:211–217.

The load-bearing cancellations are identities, not numerical tests. Write P_mu=beta_mu/phi, Delta_mu=phi_mu delta_mu, a=kappa product delta, beta_mu=a delta_mu+phi R_mu. Then
D=phi sum_mu Delta_mu/beta_mu=phi Sigma,
a Sigma=sum_mu phi_mu(beta_mu-phi R_mu)/beta_mu=phi Psi.
The constrained Euler equation P_mu r_mu+b_mu=t nu_mu, sum_mu nubar_mu r_mu=0 gives, on exact F=db,
r_mu=-(1/P_mu) sum_nu (1/P_nu)nubar_nu F_{nu mu}/D.
Thus the all-F extension is -a nubar_nu/(beta_mu beta_nu Psi); away from the origin it is also -phi nubar_nu/(beta_mu beta_nu Sigma). This fixes which extension is being proved local.

For f_0's zero alias, substitute the data formula for r. The apparently singular t-term contains
nu_rho^(n) W_sigma nu_sigma/beta_sigma-(rho<->sigma).
Using nu_sigma D_sigma/delta_sigma=nu_sigma^(n) and
1/beta_sigma=1/(a delta_sigma)-phi R_sigma/(a delta_sigma beta_sigma)
cancels the first bracket exactly and supplies the missing phi in the second. The resulting coefficients are analytic near zero.

The real lower bounds follow from delta>=max(4/pi^2,1-x^2/12), phi>=4|x|^2/pi^2 and the zero/nonzero alias split. In particular beta>=min(kappa,24/pi^2) and beta>=phi. The change bounds have the following independent origins: positive Fourier coefficients for delta; the exact cosine/cosh formula for phi and Delta; an affine-in-cosine expression for A; finite Parseval plus Cauchy–Schwarz for the alias numerators; and the quotient rule for beta,Psi,Sigma. On |f|<=rho<1,
Re(1/(1+f))>=1/(1+rho): multiply through by |1+f|^2 and minimize on the circle, or use that inversion maps the disc to a disc with this left endpoint. This validates the P7 denominator argument. R3 verifies the stated sufficient inequalities.

**Uniformity in the number of fine aliases was not assumed from a finite sum.** For K!=0 the denominators obey |phi^(K)(z)|>=lambda phi^(K)(x)>=c|x+2pi K|^2. For |Im z_a|<=eta,
|D_n(z_a+2pi K_a)|<=C_eta/(1+|K_a|),
|nu_rho^(n)|<=C_eta(1+|K|), and the offset phase is <=e^(4eta), since each 0<=u_a/n<1.
The f_0 alias coefficient is therefore bounded by
C_eta product_a(1+|K_a|)^(-1) (1+|K_sigma|)^(-1) (1+|K|)^(-1).
On the shell 2^j<=1+|K|_infinity<2^(j+1), sum the sigma direction with exponent two (bounded), the other three with exponent one (each O(j+1)), and the last factor by 2^-j. The total is at most C (j+1)^3 2^-j, whose series converges. This proves the uniform bound needed here; it does not rely on the order-five derivative estimates left unverified in LANEA55 §17. P's alias sum is still more summable.

The full alias sums are periodic meromorphic functions: shifting p by 2pi reindexes K modulo n, and the fine-offset phase is invariant under that reindexing because u is integral. The locally bounded analytic pieces agree by the displayed identity and extend across removable denominator sets. Contour shifts give the infinite-lattice bound M exp(-m'|X|_1), and absolutely convergent periodisation gives the torus operator.

**Claim status: PROVEN for the unprimed theorem, in the stated trivial-background scalar-component setting.** Constants depend on L,kappa_-,kappa_+ and are not numerically evaluated. A torus pointwise estimate must retain its periodisation sum or absorb its uniform factor in a chosen kernel constant; the weighted row-sum estimate follows directly by summing lifts, without discarding images.

### R6 — REFUTED: “no exponential F-representative is available”; H1 can be discharged without the omitted derivative bookkeeping

**Attachments:** LANEA55 §17, “N2-lin (H1)” and “Here no exponential F-representative is available”; LINEAR_PACKAGE.md:261–286, “Lemma 4.4”; PROOF.md:3791 onward, “F-df_0”. This is a stale-result error: Corollary 4.3 excludes two particular representatives, not all representatives.

Here is an independent reconstruction. Fix a fine offset and output component, and write its analytic periodic data row as B^v(p), bounded by M in the unprimed strip from R5. For exact/gauge data the output curvature vanishes, so sum_v nu_v B^v=0. A closed coarse datum has a zero-energy closed lift (constant part plus a lifted gradient); hence the zero mode is covered as well.

Let E_<a set coordinates 1,...,a-1 to zero, E_a set p_a=0, and T_a g=(g-E_a g)/nu_a. The numerator vanishes at every zero of nu_a=e^(ip_a)-1, by periodicity, so T_a preserves analyticity. Set h_ab=T_a E_<a B^b for a<b and h_ba=-h_ab. Telescoping gives
B^v=sum_{a<v}nu_a h_av+E_<v B^v.
Subtract the Ward identity evaluated with the first v-1 coordinates zero from the one with the first v coordinates zero. After cancelling nu_v, this yields
E_<v B^v=-sum_{b>v}nu_b h_vb.
Therefore B^v=sum_a nu_a h_av and sum_{a<b}h_ab (dB_k)_ab=f_0, for every datum.

For 0<m'<m_*, Cauchy's estimate and |e^(iw)-1|>= (2/pi)e^(-m')|w| on |Re w|<=pi/2 give
|h_ab| <= M_ax := max(2,(pi/2)e^(m')/(m_*-m')) M.
On the rest of a period, |e^(iw)-1|>=1 gives the 2M bound. The resulting periodic kernel satisfies |K_ab(X)|<=M_ax exp(-m'|X|_1). Periodisation and summation over the six planes give
**||f_0||_infinity <= 6 M_ax coth^4(m'/2) ||dB_k||_infinity.**
This proves N2-lin (H1), with a finite k,T,u-independent constant, from the independently checked unprimed theorem. Likewise H2 follows from its all-F residual kernel, with C_R=6M coth^4(m'/2).

**Correction:** the absence claim is false; the printed Coulomb representative's power tail is compatible with an analytic axial representative. LA37's H1 estimate is now **CONFIRMED / PROVEN through this replacement proof**, though the old order-five derivative proof itself remains NOT-VERIFIED here. This does not verify Theorem 4.2' or its larger rate.

### R7 — CONFIRMED: remaining geometric and elliptic inputs, with their actual hypotheses

All references below are to locating strings in BFT_A.md unless otherwise specified. These are independent derivations of the needed implications; “banked” labels were not used as proof.

**BL-2 (LA19), §7.3 / §8.2, lines 491–504 / 598–618 — CONFIRMED / PROVEN.** Summing each contour's two axial legs and middle straight segment gives Q=Q_str-dh and Qd=d ev. Induction gives h^(a->b)=sum_{i=a}^{b-1}ev h_i Q_str^(a->i). The path length bound 2(L-1), summed against L^(i-a), is exactly 2(L^(b-a)-1); one further difference costs 2 and Q_str costs L^(b-a), giving 5 in coarse potential units. Transposition on co-closed currents removes h^T d*; each fine link reads exactly L coarse terms of weight L^-4, giving L^-3 and preserving co-closedness. Stokes on an L by L plaquette gives L^6 pairs of weight L^-6 in coarse curvature units, and its transpose reads L^2 values with weights L^-2. The 4-link curl and 2-value difference give the stated 4 and 2 inverse bounds. No elliptic inverse or gauge-slice theorem enters.

**BL-C (LA20), §8.4, lines 628–635 — CONFIRMED / PROVEN.** For nested boxes of successive size ratio 2, the mean difference is <=sqrt(16) Osc_2=4 Osc_2. Telescoping the dyadic means from a singleton to size in [delta,2delta] gives 4*2^alpha/(2^alpha-1) at each of two endpoints. Enclosing the two terminal boxes in a box four times as wide gives 2*sqrt(4^4)*4^alpha=32*4^alpha. Multiplying by 2^alpha yields exactly the stated C_C. For delta>1/8 the 2*8^alpha sup term suffices. Legal lifted boxes have side <=1<=T; the singleton and I=0 cases are included. Probability averaging commutes with the appropriate coarse translations, so apply this result to f_0 BEFORE pushing it up.

**LES-div (LA36), PROOF “Lemma LES-div”, observed at :3644; LANEA55 §1 — CONFIRMED / PROVEN.** On a box of side r split u=w+v, with w Dirichlet and v harmonic. Testing the equation for w after subtracting the constant mean of g gives ||grad w||_2^2<=C(r^(4+2alpha)[g]^2+r^6 H_0^2). For a harmonic h, repeated difference-Caccioppoli estimates and the four one-dimensional telescoping inequalities give sup|grad h|<=C r^-3||h-mean h||_2 in an interior box. Hence its oscillation decays by (rho/r)^6. Applied to the differences of v and using the minimizing property of means:
psi(rho)<=A(rho/r)^6 psi(r)+B r^(4+2alpha)([g]^2+R^(2-2alpha)H_0^2).
Choose tau<1/4 with A tau^(2-2alpha)<=1/2, iterate at tau^j R/4, sum the geometric series, and fill intermediate radii by monotonicity. Integer-radius termination costs a fixed constant only. Division by rho^4 gives the printed claim. This explicitly requires 0<alpha<1. The scalar LES proof uses ||w||_2<=Cr||grad w||_2 in the same split; it gives the analogous oscillation estimate for F from dF,d*F. J-str follows directly by applying d* to the Euler equations and using injectivity of ev^T; its transport exponent is 3, not a guessed scaling exponent.

**LE (LA34), §18.1 / §28.3, lines 1392–1418 / 2414–2425 — CONFIRMED / PROVEN.** I checked the torus-kernel argument including the omitted zero mode. A dyadic piece of a symbol of order a has kernel bounded by C 2^(j(a-4))(1+2^-j|z|)^-11. Finite-grid periodisation has only 2^j<=M/pi contributing. Splitting 11=6+5 controls nonzero images by a summable four-dimensional fifth-power tail. Summing scales gives C(1+|z|_M)^(a-4) for -2<a<4. For DK_0, a=-1 is strictly inside that interval. Near-field Parseval gives ||K H||_2<=sqrt(2)||H||_2 and hence 192 n^4 sup|F|^2. In the far field there are three input planes per output entry and 16 entries; the Euclidean entry sum costs sqrt(16)=4. The exact count 64t^3+16t<=80t^3 and sum_{t>=n}t^-2<=2/n give 62914560/16807<3744<10^4. The latter tail inequality follows by comparison with 1/[t(t-1)] for n>=2, and by separating t=1 for n=1. Thus C_E=sqrt(192)+10^4 C_K is sufficient. This proves existence of C_K, not its numerical size.

**Lemma Lambda (LA14), §13.11, lines 1109–1121 — CONFIRMED / PROVEN.** The assembled contour and straight root leg differ by a ruled surface of <=2L(L-1)L^(2i) fine plaquettes at step i. Pushing this error through subsequent maps costs <=5L^(k-1-i). The exact sum is
10L(L-1) sum_{i<k}L^(k-1-i)L^(2i)=10L^k(L^k-1)<10n^2.
All surfaces stay in the two indicated top blocks. Telescoping the residuals gives the additional 5 sum||r_i^c|| term. This Lambda constant is **10 for this holonomy lemma**, not NSL's unrelated elliptic Lambda constant.

**LR-pot (LA15), §13.12, lines 1123–1146 — CONFIRMED / PROVEN for T>=3; periodic lifting supplies the small-torus uses.** Product hats sum to one and vanish at other roots, so the constructed gauge is root-pinned. The axial integral transforms by minus the gauge difference; this gives P^2=P. Expanding d(chi lambda) gives a first term of <=3n sup|dx_0|. The derivatives of the hats have total variation <=2/n. Two relevant root paths close with <=4 root segments into a loop of length <=12n inside a radius-n cube, costing <=36n^2 sup|dx_0|. Consequently the level-zero bound is 75||f_0||+8 max|Lambda|, hence 155||f_0||+8||B_k||+40 sum||r_i^c||. Pushing up costs 5 and adding residuals costs another 5, giving **775,40,205**. The local data for the first step lie within coarse l1 distance 12; subsequent composite maps cost <=8, validating e^(20m). A periodic lift from T to 3T commutes with the projection; its gauge difference descends. This is a bound on the tent-slice representative, not on every representative and not a gradient bound.

**FP (LA12), §13.10 / §13.13, lines 1101–1107 / 1148–1153 — CONFIRMED / CONDITIONAL on Proposition W at the selected unprimed rate.** Complete the residual square and set tau_(j+1)=Q_j tau_j+s_j/kappa_j, tau_0=0. The geometric sum gives c_1=5L/((L-1)kappa_-), with the source exponent theta at EVERY level. If alpha<=theta, the curvature and its Campanato loss are summable; weights cost e^(8m) for transport and at most a further e^(4m) for the differences/box. Thus the displayed G_R(m) follows. In LR-pot, sum||r_i^c||<=L/(L-1)||x||_inv<=3||x||_inv/2; **775+205*3/2=2165/2<=1083**. No same-letter c_1 from another section is imported.

**BL-5(a) (LA21), §8.6 — CONFIRMED / CONDITIONAL on the data estimate, now available from R5–R6 and LES.** The same square completion is an affine bijection of the fixed-data problems: x=y-tau, datum of y=B_k+tau_k, f_0(x)=f_0(y), r_i(x)=r_i(y)+s_i/kappa_i. The triangle inequality gives G_R=c_1 G_D+8c_1+1/kappa_- and the residual bound follows from J-str and H2. The weighted version must use its newly selected M,M_f and rate as in R4.

**CO-upR/RH (LA17), §21.2 / §23.8–23.9 and dated U5 at :2356 — CONFIRMED / PROVEN for the configuration identities used in K^(sigma).** For EVERY configuration, d x_(j+1)=Qcal_j d x_j-d r_j. Iteration gives f_j=A f_0-R_j with each A a translation-covariant probability average. Thus ||R_j||<=sum 4L^(2(k-1-i))sup|r_i| and [R_j]_alpha<=sum 4L^(alpha(k-j))L^(2(k-1-i))sup|r_i|. This termwise assertion needs no co-closedness. Apply BL-C to f_0, then average, to obtain the claimed upper-level estimate. The source-specific rough-current corollaries are NOT-VERIFIED here.

### R8 — CONFIRMED: YH, W0 and PW-cc as implications of the checked data package

**Attachments:** LANEA55 §§7,8,12; BFT_A “23.1 Lemma PC”, “23.3 Lemma LD”, “[RBA5-fix] U4'”, “28.4 Theorem YH”, “28.5 Theorem W0”, “38.2 Theorem PW-cc” (observed at :1874, :1900, :2348, :2427, :2465, :3481). Claim status: CONDITIONAL on Proposition W at a rate strictly below the unprimed m_*; its kernel antecedent is supplied in R5.

For the YH decomposition, define omega=Delta^-1(delta_p-h_p), g_0=d*(chi omega). Since d* commutes with the flat Hodge Laplacian,
d*dg_0=d*delta_p-d*(chi h_p-[Delta,chi]omega).
All residuals of the chain g_j=Q^(0->j)g_0 vanish. Completing the translated quadratic functional therefore gives Y^p=g+Z, with datum -Q^(0->k)g_0 and source G'=chi h_p-[Delta,chi]omega. This is an identity on the quotient, not an assumption of the wanted estimate.

For j'=d*G', sum its flux across each coarse face. Summing the fine divergence over a coarse block shows d*J=0 for the resulting face flux J. Straight-transpose interpolation of J is a convex average of n^4 nearby fine links in each orientation, so e=j'-(Q_str^(0->k))^T J obeys |e|<=4n sup|D j'| and is co-closed. Its compact support lies in a cube of side q<=2r+8n+5.

The compact inverse can be built directly. In the first coordinate set G_av=-sum_{t<=z_a} e_v(t,z')+1[z_a>=b] sum_t e_v(t,z'), and put the lower-dimensional inverse of the transverse total flux on the b-slice. Differences give e_v for v!=a; the a-component follows by summing d*e=0 (with the leading minus sign retained). Support is inside the cube. At each dimension the partial sum costs <=q||e||_1, so ||G_e||_1<=3q||e||_1. Thus, from |Dj'|<=C_j r^-6,
||G_e||_1<=48(q/r)^5 C_j L^-c.
For L^c>=260, q/r<=41/20; the EXACT coefficient is
48(41/20)^5=347568603/200000<1738.
Choosing L^c>=max(260,3476 C_j) makes it <=1/2. This gate is satisfiable: C_j depends on the free torus kernel and a fixed smooth cutoff, not on c, YH or the sought response norm. There is no circular requirement of making a constant smaller than its own output. The additional rate condition in R4 can be imposed on the same free c. For a weighted version whose bootstrap requires 1/4, use **6952 C_j**, not 3476 C_j (source U4').

The unscreened dipole is not summable by itself at the curvature level without a subtraction. Here the constant plane value of the test 2-form pairs to zero with dg_0. The remaining near sum is bounded by n^-alpha sum_{t<=n}t^(alpha-1)<=1+1/alpha; the far sum ends at r=L^c n and costs O(c log L), not log n. The potential dipole has l1 norm O(r)=O(L^c n). For the screened part, its data and residual norms are O(n^-2), with constants depending on c and the chosen weight; Proposition W gives curvature O(n^-2) in coarse units, FP gives potential O(n^-2) in coarse units. Multiplying by the fine conversion and counting sites gives respectively n^-2*n^-2*n^4=1 and n^-1*n^-2*n^4=n.

For the lattice sums, in one dimension sum_{z in Z}exp(-a|z/n-t|)<=coth(a/(2n))<=n coth(a/2). The second inequality follows by differentiating u coth u: its derivative has sign sinh(u)cosh(u)-u>=0. Take the fourth power and sum the six plaquette/four link orientations. Periodic sums are bounded by the lifted sums. Thus the screened bounds are uniform in k,T. At fixed k,T the quotient response is a finite linear map, so its seminorm sup is finite before absorption; the <=1/2 term can genuinely be moved to the left. For T<8L^c the whole torus has bounded coarse volume, the uncut free dipole gives the same estimates, and the T<=2 projection use descends from the periodic lift. This establishes YH's two required estimates.

For W0, symmetry of the quadratic form gives
d x_0(p)=<G_0,dY_0^p>+<j_0,Y_0^p>.
Only when d*j_0=0 may the second argument be replaced by Y_0^p+d lambda. YH then gives the sup bound with n^2*n^-3*n=1. Applying d* to the Euler equations shows all residuals are co-closed; their lower-level transport has factor (kappa_top/kappa_i)L^-3(k-1-i). Top-residual reciprocity identifies its response with the source-free datum delta_b/kappa_top, so Proposition W and FP give the printed C_top. For Holder regularity, use B=d*Delta^-1 d x_0 and
-Delta_scalar B=d*G_0+h, ||h||<=n^-3(||j_0^c||+kappa_+||r_top||).
The sign of the scalar/vector Laplacian convention does not change this norm estimate. LES-div and LE supply the estimate at scales <=1/4; larger scales use the sup. All powers cancel as n^(2+alpha)*n^(1-alpha)*n^-3=1. Step 4 needs only a sup bound on h, not co-closedness of its individual summands. Upper-level curvature follows from R7, with the convergent residual sum sum L^-(1-alpha)m. This confirms the two carefully separated uses of co-closedness, not an extension of W0 to arbitrary plain currents.

For PW-cc, expand the pairing by x_l=Q^(0->l)x_0-sum_{i<l}Q^(i+1->l)r_i. A co-closed current pushes down with L^-3l. Top reciprocity yields
||r_top(Y^p)||_1<=4n^-2 G_D(a)S(a)/kappa_-.
Each coarse value under Q_str^T has total fine l1 weight L, so
||r_i(Y^p)||_1<=khat L^(k-1-i)||r_top(Y^p)||_1.
A residual pairing contributes A L^(2i+2-k-3l)||j||. Sum i<l and use k-l>=1 to get A/(L^2-1) times L^(k-3l)||j||. This proves exactly the stated C_cc and both residual estimates used by COF. Finite-dimensional quotient-norm duality follows by minimizing ||x_l+d lambda||_1: its dual constraints are ||j||_infinity<=1 and d*j=0. No gauge choice enters that norm.

### R9 — CONFIRMED: LIN0 and COF-size at their stated source classes; corrected level-zero identity is necessary

**Attachments:** LANEA55 §§10–11; BFT_A “28.8 Corollary LIN0” (:2533); BFT_B “27.1 Definitions” (:3590), “35.3 Lemma DF-cc” / “35.4 Proposition COF-size” (:4040–4070).

**LIN0 (LA16): CONFIRMED / CONDITIONAL on Theorem GU in its stated upper-source scope.** The datum and residual slots use BL-5(a); level-zero divergence and co-closed plain slots use W0; upper divergence slots use GU with alpha<theta. For an upper co-closed current, transposing the telescoping identity gives a co-closed level-zero current and residual sources. Their fine-to-coarse conversions give
sum_{l>=1}||j_l^c|| <= ||j||_Pc/(L^theta-1),
and for fixed i the residual bound is
L (k-1-i) L^(-(1-theta)(k-i)) ||j||_Pc
<= [L/(e(1-theta)ln L)] ||j||_Pc.
Here the discrete supremum is **bounded by**, not identically equal to, the continuous maximum. This is valid for 0<alpha<theta<1. Superposition gives LIN0. Its plain currents are level-wise co-closed; the passage to composite co-closed sources remains the separately named COF/C2-COF construction. I did not re-prove the full GU theorem in this review and do not silently promote it beyond that named antecedent.

**COF-size (LA29): CONFIRMED / PROVEN under (CC-0), with hat j_0=j_0+h_0^T psi_0.** Transpose Q=Q_str-dh, expand the composite and exchange the finite double sum. Its higher-divergence bracket is xi_i. Applying the injective placement ev^T gives xi_i+psi_i=restriction of D(S), hence xi_i=-psi_i under D(S)=0. Therefore
C(j)=sum_l (Q_str^(0->l))^T (j_l+h_l^T psi_l).
The straight transpose contracts in plain coarse units. The divergence cascade gives
pi_l(h_l^T psi_l)<=2d sum_{t<=l}L^-3(l-t) pi_t(j_t).
Sum over l FIRST: the entire funnel sum is <=2d/(1-L^-3) sum_t pi_t(j_t). Thus the simple sufficient bound is
pi_0(C(j)) <= (1+2d/(1-L^-3))[||j_0^c||+||j||_Pc/(L^theta-1)].
This is already below the printed C_C times (||j_0^c||+||j||_Pc). It does not rely on FT's max form at all. The max form itself is valid for centred roots by R2.

**The missing hat j_0 term is real, not merely a suspicion.** Take k=2, an arbitrary level-one link delta j_1 with d*j_1!=0, and j_0=-Q_0^T j_1. Then D(S)=d*j_0+ev^T d*j_1=0 and C(j)=0. The expression using the printed hat j_0=j_0 instead gives
j_0+Q_str,0^T j_1=h_0^T d*j_1,
which is nonzero on an interior axial edge of an endpoint block. Restoring psi_0=-d*j_1 and hat j_0=j_0+h_0^T psi_0 makes it zero exactly. The source's literal convention at :3590 is REFUTED when used in DF-cc (ii); LANEA55's P1 correction is CONFIRMED.

**Two precisions to R2/R8, before final disposition.** R2's final addition pi_l(j_l)<=A is for l>=1. At l=0 the printed hat j_0=j_0 trivially satisfies the displayed FT(iii) bound. If the necessary DF-cc correction is made, pi_0(hat j_0)<=(1+8h_L)B<=8g B in d=4, so that version also satisfies it. As a non-tautological geometry check I enumerated all 24 coordinate orders and all 3^4 endpoints using integer signed edge counts: the averaged h coefficient maximum is exactly 10/81, below the single-order bound 1/3 used in R2. No linear solve or floating point was used.

For R8's screened-data estimate, the direct n-step Q_str has individual fine-link weights <=n^-3. In its nearest tube, sum_{|z-p|<=C n}(1+|z-p|)^-3<=C n (four-dimensional shells); hence ||Q_str g_0||<=C n^-2. Tubes farther away give the same bound from n sup|g_0|<=C n/(distance)^3. The root-map datum differs from this straight datum by a gradient, which the quotient seminorms permit. Also |J|<=6 C_G n^3 r^-5=6C_G L^-5c n^-2. Residual transport gives
||s||_R<=L^theta max_{i<k}L^(-(1-theta)(k-1-i))||J||,
so theta<1 suffices; choose, for example, theta=(1+alpha)/2 in the auxiliary construction. The compact supports add only fixed factors exp(O(a L^c)) in the weighted norms. Thus the O(n^-2) assertions in R8 have explicit scale derivations.

### R10 — CONFIRMED bookkeeping defects: C_C collision, LED typo, and current citation drift

**C_C collision — CONFIRMED.** BFT_A.md:508 / §8.4 defines
C_C^Camp=2^alpha(8*2^alpha/(2^alpha-1)+32*4^alpha).
BFT_B.md:4064 defines
C_C^funnel=(1+2d/(1-L^-3))(1+1/(1-L^-theta)).
Theorem COF's displayed constant list after §35.5(d) lists “C_C” only once although both estimates enter. Both are finite but unequal functions of the parameters. A permissible repair is to keep distinct names, or explicitly use max(C_C^Camp,C_C^funnel); equality or substitution between them is not justified. Similarly c_1 in BL-3 means 5L/((L-1)kappa_-), C_1 in LR-pot means 775, and the two strip theorems' M constants are distinct (R4). No comparison in this review identifies these symbols merely by spelling.

**LED-unif typo — CONFIRMED; the printed identity is REFUTED.** PROOF.md:2855, “Write phi_n/D_g = kappa_(k-1) + u/v”, with u=phi_n-kappa D_g and v=kappa D_g. Algebra gives
phi_n/D_g=(v+u)/D_g=**kappa(1+u/v)**.
The printed coefficient of u/v is 1; the correct coefficient is **kappa**. Equality with the printed expression would require (kappa-1)u=0, which is not its quantified hypothesis. Also it is phi_n and v that share the quadratic Taylor term; u has that term cancelled. The regularity conclusion can survive the correction, but this is not evidence that the old derivative proof has been independently checked.

**Citation drift — CONFIRMED.** String search currently locates the word-size BCH statement at **PROOF.md:4312**, not BFT_A §3.3's “PROOF l.3512”, nor LANEA55's repeated “now ... l.4311”. The latter currently says “Elementary bounds”; 3512 lies in the sector-bound argument. Use the locating string “(BCH) If x_1, ..., x_n ... s := sum|x_i|”. BFT_A W0's “LES-div (PROOF l.3422)” currently lands in the nonlinear implicit-function argument; LES-div is at **PROOF.md:3644**, located by its full lemma name. This independently verifies drift rather than trusting LANEA55's replacement line number.

LINEAR_PACKAGE's own historical “l.N” citations are explicitly to the forbidden frozen session-16 snapshot (lines 9–10 of that package), not to live PROOF.md. I did NOT mark those as drift errors or read the snapshot. I found the corresponding current proofs by string in the permitted PROOF.md. All line numbers here are observations during this review; locating strings remain authoritative if concurrent appends move them.

### R11 — Gate audit: discriminating arithmetic, limited theorem coverage; blanket control claim REFUTED

**Attachments:** LANEA55 §19 “every gate had a designed-FAIL control”; the four named criteria files and scripts under checks/la55_*.

I inspected every predicate and rebuilt the needed arithmetic independently. I did not execute the author's scripts: la55_1 performs a needlessly large 100000-term rational sum, and all four format some outputs through float. The independent computations here used only integers/Fractions, integer square roots and factorials, and wrote no separate check files. A claimed prior PASS log or creation order is not independently authenticated by this review.

| Gate | Can it reject? What does it actually establish? | Review verdict |
|---|---|---|
| la55_1 C1,C2 | Yes: compare independent rational coefficients with 3744,5054,10000. Independently reproduced 62914560/16807 and 84934656/16807. Does not prove the geometric counting premises. | CONFIRMED arithmetic; geometry re-derived in R7 |
| la55_1 C3 | Yes: checks finite integer shells plus explicit binomial coefficients. The all-t result follows from 64t^3+16t<=80t^3 for t>=1. | CONFIRMED |
| la55_1 C4 | Yes on its 200 tested n, but finite samples alone are not the all-n estimate. The telescoping comparison in R7 proves it without a long sum. | CONFIRMED inequality by replacement proof |
| la55_1 C5 | Yes; tightening 1738 to 1737 makes the rational inequality false. Independently reproduced that failure. The final 3476 is 2*1738. | CONFIRMED |
| la55_1 C6 | Yes for arithmetic typos. It compares literal constants, not paths, gauges or weights. The 775/40/205/1083 conclusions require the path reconstruction in R7. | CONFIRMED at arithmetic scope |
| la55_1 C7 | Yes for its finite L,k inputs; the exact geometric-series formula, not the sample loop, establishes uniformity. | CONFIRMED with R7 proof |
| la55_2 B1 and la55_4 E1 | Yes. Rational upper bounds are below 9 at 1/40 and 1/27; rational LOWER bounds exceed 9 at 1/20 and 1/24. These controls reject the chosen majorant, not the underlying matrix inequality. | CONFIRMED, independently reproduced in R1 |
| la55_2 B2 and la55_4 E2 | The reported predicate cannot be false after f_of returns: f_of has already asserted exactly u<1. The assertion itself is a genuine convergence guard and can abort the program. B2/E2 are redundant reports, not an independent second test. | CONFIRMED convergence at tested inputs; no independent gate credit |
| la55_2 B3 | Can detect a negative coefficient among degrees <=12. It cannot decide positivity of all higher coefficients. R1 supplies the missing all-order positive-series proof. | CONFIRMED finite check scope only |
| la55_2 B4 | Yes: expands the ordered product/log and compares the degree-two word coefficients with an independently specified commutator expression. It can detect an order/sign error. R1 also derives this algebra directly. | CONFIRMED |
| la55_3 S1–S4 | Yes at the five rational input tuples. The pi bracket and interval directions are valid; R3 independently reproduced every strict margin. Its control fails S2–S4 and PASSES S1. It has no loop or interval variable covering all kappa. | CONFIRMED five-point scope; uniform certificate is new in R3 |

**REFUTED:** the blanket “every gate had a designed-FAIL control” assertion. la55_1 supplies one control for C5; it does not separately challenge C1–C4,C6,C7. la55_2's control targets B1, not B2–B4. la55_4's targets E1. la55_3's chosen control does not make S1 fail. Passing a harness with one negative control is not a demonstration that every predicate or theorem hypothesis can fail.

None of these scripts tests the field operator, the all-order complex symbol identities, the source-to-slice compatibility, or the consumers' rate quantifiers. Those obligations are handled by the derivations and scope restrictions above, not by relabelling the script outputs.

## Reproduction certificate for the new interval result

This self-contained code reproduces the new 64-box certificate in R3. It uses no files, external packages or floating point. The five point tests use the same function with a singleton k interval and the table's eta,r. The inequalities are the independently derived P1–P7 conditions, so the code certifies arithmetic, not the operator argument in R5.

```python
from fractions import Fraction as F
from math import factorial, isqrt

class I:
    def __init__(self, a, b=None):
        self.a, self.b = F(a), F(a if b is None else b)
    def __add__(self, y):
        y = iv(y); return I(self.a+y.a, self.b+y.b)
    __radd__ = __add__
    def __neg__(self): return I(-self.b, -self.a)
    def __sub__(self, y): return self + -iv(y)
    def __rsub__(self, y): return iv(y) + -self
    def __mul__(self, y):
        y = iv(y)
        v = [a*b for a in (self.a,self.b) for b in (y.a,y.b)]
        return I(min(v),max(v))
    __rmul__ = __mul__
    def __truediv__(self, y):
        y = iv(y); assert y.a*y.b > 0
        return self * I(1/y.b,1/y.a)
    def __rtruediv__(self, y): return iv(y)/self
    def __pow__(self, n):
        out = I(1)
        for _ in range(n): out = out*self
        return out
def iv(x): return x if isinstance(x,I) else I(x)
def root(x):
    x=iv(x); D=10**20
    a=isqrt(x.a.numerator*D*D//x.a.denominator)
    b=isqrt(x.b.numerator*D*D//x.b.denominator)+1
    return I(F(a,D),F(b,D))
def atan(x,N):
    p=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(N)),F())
    q=p+(-1)**N*x**(2*N+1)/F(2*N+1)
    return I(min(p,q),max(p,q))
pi=16*atan(F(1,5),20)-4*atan(F(1,239),6)
def ex(x):
    p=sum((x**j/F(factorial(j)) for j in range(13)),F())
    return I(p,p+x**13/F(factorial(13))/(1-x/14))
def ch(x):
    p=sum((x**(2*j)/F(factorial(2*j)) for j in range(7)),F())
    return I(p,p+x**14/F(factorial(14))/(1-x*x/F(15*16)))
def margins(k,h,t,r):  # L=3
    k=iv(k); E=ex(t); C=ch(t); e=E-1
    R=1+F(h,8)+k/9
    bpi=24/(pi*pi)
    b=I(min(k.a,bpi.a),min(k.b,bpi.b))
    G=pi*pi/4; G=I(max(G.a,R.a),max(G.b,R.b))
    lam=1-4*t*t*C*C/9
    ez=(4*t*t/9+4*t/3)*C
    cz=(e*E**4+4*E**3*e*(1+E)+ez)/(9*lam)
    er=F(h,8)*e+k*cz
    rho=(1+pi*pi*e/4)**5-1+(4*t*t/b+4*t/root(b))*C*(R+er)+er
    PU=k*(1-r*r/6)/(k+r*r*R)
    ep=((4*t*t+4*t*r)*C*(R+er)+r*r*er)/((1-rho)*b)+rho/(1-rho)
    f=(t*t*pi*pi/(r*r)+2*t*pi/r)*C
    br=1/((1+rho)*G)-f/(1-rho)
    rhs=F(1,2)/((1+rho)*G)
    return [I(F(1,2))-rho,PU/2-ep,br-rhs,I(F(3,20))-f]

certified=[F(353941,10**6),F(423,20000),
           F(24951,10**6),F(27423,500000)]
for j in range(64):
    K=I(F(1,4)+F(15*j,256),F(1,4)+F(15*(j+1),256))
    for q,c in zip(margins(K,16,F(37,10000),F(1,4)),certified):
        assert q.a >= c > 0
print("64 exhaustive rational intervals certified")
```

## Summary table

“CONFIRMED” below always refers to the statement in the Scope column. It does not overwrite the refuted auxiliary assertions R2,R4,R6,R10,R11.

| Target | Review verdict | Claim status and precise scope |
|---|---|---|
| LA36 LES-div | CONFIRMED | PROVEN; 0<alpha<1, local divergence-form estimate |
| LA19 BL-2 | CONFIRMED | PROVEN; centred roots, stated coarse units and transpose domains |
| LA20 BL-C | CONFIRMED | PROVEN; its own C_C^Camp |
| LA34 LE | CONFIRMED | PROVEN; finite uncomputed C_K, every required centre |
| LA14 Lemma Lambda | CONFIRMED | PROVEN; holonomy C_Lambda=10, not NSL's constant |
| LA15 LR-pot | CONFIRMED | PROVEN; tent slice, constants 775/40/205, weight cost e^(20m) |
| LA12 FP | CONFIRMED | CONDITIONAL on Proposition W at 0<=m<m_*; 1083 is sufficient |
| LA31 YH | CONFIRMED | CONDITIONAL on that data package; bootstrap c chosen after its inputs |
| LA32 W0 | CONFIRMED | CONDITIONAL on YH/data package; plain level-zero current co-closed |
| LA21 BL-5(a) | CONFIRMED | CONDITIONAL on checked data estimate; alpha<=theta |
| LA16 LIN0 | CONFIRMED | CONDITIONAL on the named GU input; 0<alpha<theta<1, level-wise co-closed plain sources |
| LA29 COF-size | CONFIRMED | PROVEN under CC-0; use corrected hat j_0; no factor-two inflation |
| LA30 PW-cc | CONFIRMED | CONDITIONAL on YH/data package; includes both exact residual l1 estimates |
| LA17 CO-upR/RH | CONFIRMED | PROVEN for configuration-level identities/bounds; rough-source corollaries NOT-VERIFIED |
| LA24 BA-3 plaquette clause | CONFIRMED | PROVEN with 9 for s_j<=1/27, including complex HS matrices; soft clause NOT-VERIFIED |
| LA37 LES, J-str, H1, H2 | CONFIRMED | PROVEN estimates; H1 uses R6's new proof, not the omitted derivative bookkeeping |
| LA40 Theorem 4.2(i)–(ii) | CONFIRMED | PROVEN unprimed kernel theorem and five pairs; new interval bound m_*>=37/10000 for L=3,[1/4,4] |
| Theorem 4.2' / original full primed weighted range | NOT-VERIFIED | GAP in this review; unprimed verification does not establish the larger quantified range |
| FT “false by factor 2” diagnosis | REFUTED | Centred-root max bound is PROVEN without inflation; sufficient coefficient 212/39<108/13 at L=3,d=4 |
| “No exponential F-representative” | REFUTED | R6 gives one and proves H1 |
| “Every gate had a designed-FAIL control” | REFUTED | Controls cover selected predicates only |
| hat j_0=j_0 in DF-cc / LED ratio / live line pointers | REFUTED as printed | Corrections proved in R9–R10 |
| C_C collision | CONFIRMED | Distinct constants must stay distinct or be explicitly maximized |

There are **17 confirmed target estimates at these scopes**, including conditional implications with their named antecedents. There is **no blanket confirmation of LANEA55 as written**: its rate-quantifier claim, false-FT diagnosis, no-representative claim and control-coverage claim are refuted. The rate restriction is material to the original quantified banked text; the other corrections do not destroy the required k,T-uniform estimates.

## Exactly what may be banked

1. **Coefficient 9 is now independently bankable.** The direct proof discharges the sharper plaquette input and WR's 2+9eta<=3 step for eta<=1/9, because j<k,L>=3 imply s_j<=1/27. The old cited proof still gives 144. Consequently CODEX_REVIEW_DICT D5's recommendation to use 144 is no longer necessary for these consumers; its historical diagnosis of the citation remains correct. PROOF.md:54's mandatory “not 9” replacement is superseded at this specifically verified scope. Keep all other smallness minima in force; this does not justify enlarging a final nonlinear radius without checking its other entries.

2. **The 17-item hidden-input set is discharged in the precise forms above.** This includes LR-pot through FP and the W0/top-response chain, and the unprimed analytic kernel root of Proposition W. The H1 estimate no longer needs to remain an unverified side branch: R6 supplies an independent route. Constants remain finite, possibly very large, and generally uncomputed. The scalar-component linear estimates transfer to fixed SU(N) HS-valued fields with the relevant finite component-norm factors; no dimension-independent constant is inferred.

3. **A lower-rate version of the weighted chain may be banked.** Replace the primed rate by a certified unprimed rate, relabel/recompute M,M_f and downstream constants, choose the auxiliary kernel rate strictly larger than the norm weight, and impose L^c>=6 ln(2)/(16m_*). On L=3,1/4<=kappa_i<=4 the verified bound m_*>=.0037 makes L^c>=260 sufficient for this last inequality. On an arbitrary fixed positive compact kappa interval the rate exists, but no numerical lower bound from the five points is asserted. **Do not mark the original “every m<m_*'” statement as discharged.**

The following table identifies the affected [S26-BANKED] pointers in the permitted PROOF.md. These are premise discharges for already stated implications, not a fresh review of their consumer files, which were outside this read scope.

| PROOF.md pointer (line observed; locating string) | What this review discharges | What is retained |
|---|---|---|
| :8 “(CO-fun) ... (C2-COF)” | Reviewed YH,W0,LIN0,COF-size,PW-cc,LES-div,LE,BL-C and Theorem 4.2(ii) inputs | The named GU antecedent and the consumer's composite-co-closed/top-response construction; no replacement of CC by CC-0 |
| :12 “Gauge-invariant half of BFT-5 clause (b)” / TOP-cc | Same source-only linear estimates and their top-residual bounds at m=0 | Its exact norm/source class, trivial background and stated quotient/slice scope |
| :17 “Theorem K^(sigma) (corrected)” | FP/LR-pot, BL-5(a), LIN0, CO-upR/RH configuration estimates, BA-3's 9 | GV, corrected LA-1', nonlinear/analytic hypotheses and chosen small global chart |
| :18 “GF-E and GF-E' on S_E at m=0” | LES-div, BL-2/BL-C, source estimates and reconstruction inputs reviewed here | The EP reconstruction argument and its named slice/orbit meaning |
| :19 “Clause (b) with decay” | Data kernel root and reviewed inputs for the version restricted to 0<=m<m_* and the chosen m_Y | GU_m/COF_m/CC-FUN_m producer implications; original TOP-cc_m range m<m_*' NOT-VERIFIED |
| :26 “Proposition GV-E” | This review's linear/elliptic inputs and corrected BCH coefficient | Norm choices, slice identities, the source-sum formulation and nonlinear hypotheses |
| :35 “BFT-3 on the global potential-small domain” | Only the reviewed flat linear package feeding its conditional inverse interface | H1/H2/locality hypotheses of that consumer (these labels are NOT N2-lin H1/H2), and all stated scope exclusions |
| :37 “(NSL) and BFT-0's per-level identification” | Reviewed uniform local elliptic/reconstruction inputs and BA-3 coefficient | NSL-specific elliptic constants, gauge/tower hypotheses, m=0,T>=3 and stated complex restrictions |
| :39 “BFT-4(a) on C_glob”, :50 “The local premise (R)” | Reviewed flat contraction/linear-package inputs and the sharper Wilson coefficient | All remaining GV,EP,CD,local-torus,Ward/CCP,chart and prefactor conditions of those implications |
| :54 “DICTIONARY CORRECTIONS” (names BFT-E explicitly) | Its 17-item lane-A premise subset, including LR-pot; the mandatory 144 prescription may be replaced by 9 at R1's scope | All other dictionary corrections, all unreviewed named premises, and the restricted lower-rate interpretation above |

BFT-1/2 through K^(sigma), BFT-E/GV-E, NSL, and BFT-3/4(a) therefore lose **this reviewed subset** of unnamed old-model lane-A premises. They do not become unconditional Yang–Mills theorems. No conclusion about nontrivial backgrounds, unrestricted curvature-small data, local boxes, independent BR1-action identification or a continuum construction follows from these linear estimates.

**Single most dangerous unverified item:** the uniform weighted package on the **original full primed interval 0<=m<m_*'**. It sits upstream of FP/YH/W0/top responses and many banked implications. The verified smaller-rate construction suffices for existential decay after the explicit c adjustment, but using it to certify every original primed weight would silently change a quantifier.

## Final stdout-equivalent summary

Completion record: 2026-10-29 06:58:02 UTC. The exact code embedded above was executed from this deliverable and printed “64 exhaustive rational intervals certified”. No Git command, snapshot read, audit-ledger read or write to another deliverable/check file was performed.

- **CONFIRMED:** all 17 requested estimates at the scoped statements in the table; BA-3 coefficient **9** for s<=1/27; the five strip pairs; a new uniform **m_*>=37/10000** on L=3,kappa_i in [1/4,4]; H1 by an analytic F-representative.
- **REFUTED:** FT's alleged necessary inflation **2 -> 1** for centred roots (sufficient funnel coefficient **212/39 < 108/13**); the unchanged primed-rate claim; “no exponential F-representative”; “every gate had a failing control”; the literal missing level-zero funnel; LED's coefficient of u/v **1 -> kappa**; BCH live pointers **3512 / 4311 -> 4312**, and LES-div live pointer **3422 -> 3644** at inspection.
- **Citation versus sharp bound:** **144** remains what the old cited word-size proof gives; the independently proved consumer coefficient is **9**, so the WR auxiliary ceiling **1/144 may return to 1/9 for that step only**. Neither 144 as an upper bound nor the old smaller ceiling is mathematically false.
- **NOT-VERIFIED:** Theorem 4.2', the full original primed weighted interval, the omitted historical derivative proof, off-scope BA-3 soft/rough-current clauses, and the full GU antecedent as an independent theorem in this review.
- **Most dangerous:** silently banking the original full primed weighted interval from the smaller unprimed proof.

