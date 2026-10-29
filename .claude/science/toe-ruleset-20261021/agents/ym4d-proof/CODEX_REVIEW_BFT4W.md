# Independent hostile review of BFT4W55

## PRE-STATED — 2026-10-29 03:46:41 UTC

Recorded before mathematical derivation. Reviewer: the independent Codex session assigned by the owner; no claim about an independently measured model configuration. Target: `BFT4W55.md`, including its §10 and §15 corrections. All lane-relative paths below are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` unless stated otherwise.

Scope: read the named source files by locating strings and bounded ranges; no git, snapshots, ledgers, source edits, or output files other than this deliverable. The two additional files are `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `docs/ai_methodology/skills/review-loop/SKILL.md`, required by the supplied project entry point. Dependencies outside the permitted reading boundary will remain explicitly unverified. Findings will be appended as they are established.

Refutation tests, fixed in advance:

1. **H3 / reading (R):** reconstruct the passage from banked aggregate estimates to individual local densities and their derivatives. Refutation: cancellation, missing local domain hypotheses, dimension-dependent Cauchy loss, or a weighted/multilinear quantifier not supplied by the input.
2. **Centres and corners:** derive the cutoff action from contour averaging, test the proposed lower-corner counterexample against the actual constraint class, and trace which position convention the consumers use. Refutation: an inadmissible counterexample or a convention change that invalidates another required map.
3. **H2W:** reconstruct conjugation, commutator, walk and final projection estimates using only zero-weight local-torus hypotheses. Refutation: an unjustified weighted input, loss depending on k or T, or an incorrect allowable rate.
4. **Nonlinear family:** check the sigma-pair source and energy estimates, clause (d), the placement of Pi_E in every walk piece, and equality with the slice critical point. Refutation: loss of the contraction domain, failure of exact algebra/locality, or missing identification at s=1.
5. **Assembly and prior verdicts:** trace every premise of BFT4a-glob; rederive the L powers and the RW-cc-walk criticism; distinguish a valid conditional implication from discharged premises.
6. **Decisiveness of b4w55_1:** read criteria before implementation/results; inspect whether each gate can fail and whether controls address the claimed operation. Exact rational arithmetic in plain Python only. Finite d=2,3 calculations cannot establish k-uniformity or the d=4 theorem.

Across all six tests: pin each reused constant to its defining object; test whether minima and quantified parameters remain inputs; verify cited line locations against current locating strings. Review verdicts are only CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses are only PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. CONFIRMED means the explicitly scoped statement was independently checked, never that a source's status label was accepted.

## Findings (incremental)

### W1. Reading (R) is an additional premise, not verified source provenance

**Verdict: NOT-VERIFIED. Claim status: CONDITIONAL for H3; GAP in its claimed discharge from the banked package.** Target: `BFT4W55.md:217`, locating `Every bound of ROW^{(σ)} (a)-(b)`; :681, `The reading step (R)`; `PROOF.md`, locating `Theorem K^(σ) (corrected)` in `[S26-BANKED]`.

The permitted banked-summary pointer does not state a bound on arbitrary local constraint balls. The target explicitly acknowledges that (R) is an interpretation. The actual ROW and KOFF local proofs are in files outside this review's allowed additional-file budget; neither their status labels nor the target's paraphrases establish that interpretation. In particular, an aggregate bound alone cannot imply a per-density bound: two local analytic summands `M a^2` and `-M a^2` have zero aggregate and arbitrarily large individual coefficients. This is a counterexample to the inference from aggregate bounds, **not** a counterexample to the actual Yang–Mills densities.

Conditional on genuine local, holomorphic slot bounds with uniform coefficients and summable level profiles, the dimension-free Cauchy construction is sound: normalise each direction by its local seminorm, use distinct scalar parameters of radius `eta_*/(2(p+w))`, and take one derivative in each parameter. The denominator does not count the ambient number of links. For the linear x vertex, its slotwise first derivative at zero must vanish; then Schwarz in the radial parameter supplies the extra factor `eta`. A covector identity by itself would not prove that a chosen redundant slot representation has zero derivative. The displayed slots appear compatible with that cancellation, but the missing local input must establish it slotwise.

The domains also need an explicit boundary convention: `K_D` is described using variables on `supp D`, but Campanato boxes meeting that support and residual contours at its boundary read additional variables. A fixed enlarged patch, or a specified restricted seminorm with an extension theorem, is needed before these are literal balls of the claimed variables. The radius allowance in Lemma FR could accommodate a fixed enlargement; none is defined in (R).

### W2. The multilinear sentence of Lemma LD is false as stated

**Verdict: REFUTED. Claim status: GAP in the general lemma; repaired weighted-product rule PROVEN.** Target: `BFT4W55.md:147`, locating `For a p-linear T the factor is`.

On a one-point space take `T(a,b)=ab`, read radius zero, `a=b=1`, the constant 1-Lipschitz function `f=-1`, and `mu=log 2`. Then `w=1/2`. The asserted same-weight inequality has left side `1/2` and right side `1/4`; its claimed factor `exp(p mu rho)=1` fails. For p inputs the ratio is `w^(1-p)`, unbounded under constant downward shifts of f.

The correct rule uses an output exponent F and input exponents F_i with `F <= sum F_i` (and any separate data-distance exponents), each input exponent 1-Lipschitz. Then `exp(mu F(z)) <= exp(p mu rho) product exp(mu F_i(z_i))`. Theorem H3(c)'s displayed compatibility condition supplies the needed correction, provided each F_i is explicitly required to be 1-Lipschitz. Thus this refutes the general lemma's wording, not that properly constrained use in H3(c).

### W3. Centred cancellation and the lower-corner obstruction survive the errata

**Verdict: CONFIRMED at the stated all-chain multiplier scope. Claim status: PROVEN.** Targets: `BFT4W55.md:287`, `Lemma CEN1`; :309, `Proposition CORNER`; :718, `E5`.

For one contour from root c to y, then by L steps in direction mu, then back along the translated root path, the first moment against a direction-constant field is

`L [x_mu v.(y-c) - v_mu x.(y-c)]`.

Its y-average is zero. At a lower-corner coarse-link location the missing centre offset is `((L-1)/2) h_l 1`; a constant direction field therefore leaves the exact affine-cutoff defect `((L-1)/2) h_l (grad phi.1) L x_mu`. This derivation is dimension-independent and applies in d=4, separately from the finite script checks.

The witness `x_j=h_j a` on direction-1 links, zero on other directions, with `x_k=0`, is an admissible displacement chain for WM's quantifier `every complex chain`. Its lower residuals and all gradients vanish; the top residual is a, so its norm is exactly 2. It need not belong to S_E: WM is not restricted to S_E. Scaling by any fixed small positive scalar puts it in an arbitrarily small ball without changing the multiplier ratio.

At l=0 the leading weighted defect divided by that norm is proportional to `L^(sigma(k-1))`. The centred Taylor remainder contributes at most `C_Q L^(-(2+sigma)) L^((sigma-1)k)/(2 ell'^2)` to that ratio. It is bounded for `0<sigma<=1`, and at sigma=1 equals `C_Q L^-3/(2 ell'^2)`, **not a term tending to zero**. Thus §10 E5 is the necessary correction; the unbounded-ratio conclusion survives. The full lower-corner shift at level l is the difference of consecutive offsets, as §10 E4 states; at l=0 the fine offset vanishes exactly.

At d=4,L=3, `p_L=11`, `delta_*=11/2`, hence `C_Q=2 p_L delta_*^2=1331/2`. These constants concern this contour commutator, not any other C_Q in the lane.

### W4. The sigma multiplier and commutator mechanism is valid with centres

**Verdict: CONFIRMED as the explicitly centred estimates. Claim status: PROVEN for the elementary estimates; CONDITIONAL on the stipulated contour map being the linearisation consumed upstream.** Targets: `BFT4W55.md`, `Proposition WM^σ`, `Proposition WC^σ`, `b_l :=`; `BFT_B.md:1238`, `Lemma W-cut`, and :1252, `Lemma W-mult`.

With `q=k-1-l`, a smooth cutoff's centred commutator is bounded by `C_Q h_l^3 (gradient/ell + value/ell^2)`. Converting to the residual norm gives

`L^((2+sigma)q) h_l^3 = L^-3 L^((sigma-1)q) <= L^-3`.

This is a maximum over levels, so sigma=1 is admissible. The field-gradient and Campanato product rules cost only fixed powers of `1/ell`. For the weighted source Hölder term, use the product identity with the second term multiplying **G at the weighted base point**; this justifies the stated `1+d/ell` without moving that weight to a neighbouring G.

Independently expanding the quadratic form gives the four slots printed in WC: `G=[d,psi]u`, `j_W=-[d,psi]^T du`, `s=kappa[Q,psi]u`, `j_S=-kappa[Q,psi]^T r(u)`. No extra coarse-level plain slot is missing: its scalar cutoff factor is included in `r(psi x)=psi r(x)+[Q,psi]x` and cancels in the difference of forms.

For the soft plain slot, absolute column sum `c_col`, displacement `delta_* h_l`, and the residual bound give

`pi_l(j_S) <= kappa_+ c_col delta_* L^(3(q+1)-(q+1)-(2+sigma)q) ||u||/ell`

`= kappa_+ c_col delta_* L^2 L^(-sigma q) ||u||/ell`.

Its level sum is bounded by `kappa_+ c_col delta_* L^2/(1-L^-sigma)`. Thus the J estimate genuinely uses sigma>0, including sigma=1; it does not claim a summable sigma=0 profile. This reconstruction confirms the exponent mechanism, independently of the script.

The centred convention preserves the consumers that can be checked here: a site and its level-0 root image coincide, so slot-cutoff CCL cancellation is exact; coarse translations still preserve all roots and contours; partition functions still sum to one at every link position; and the box-Coulomb projection reads the same physical roots. Its reach stays below the conservative four coarse units. Switching the positions of norm base points changes exponential weights by a bounded factor, but **does not** license using lower-corner cutoff values in these identities.

### W5. Moving Pi_E inside each piece preserves the walk equation and fixes slice identification

**Verdict: CONFIRMED as algebra with the named kernel/projection and nonlinear Ward inputs. Claim status: CONDITIONAL.** Targets: `BFT4W55.md`, `Proposition RWE`, `Lemma Dcc`, `Lemma UQ`, `Lemma IDcc`; `BFT_B.md:2143`, `Lemma EP-alg`; :2219, `Theorem EP-opt`.

The projection algebra can be reconstructed from the pinned box minimiser: shifting `x` by `D mu` shifts each gauge function by `-mu+mu(root)`. The tents sum to one and interpolate the roots, giving `Lambda D=-I` on root-pinned gauge functions, `Lambda Pi_E=0`, and `Pi_E x-x=D Lambda x`. The quadratic energy has kernel precisely that gauge space: zero energy forces `dx_0=0` and all residuals zero; the constant harmonic one-form is killed by `x_k=0`, leaving a root-pinned gradient. Therefore `H Pi_E=H`.

For each cc local source, `H(Pi_E psi u)=H(psi u)=z_box-R_box z`. Testing this identity against a root-pinned gauge direction proves that **each** remainder piece is cc. Scalar bond weights preserve this property. Summing the Neumann series then yields a field in S_E solving the same equation; it is the S_E inverse, not merely an unspecified representative.

The subsequent multiplication by `eta_Q` means individual cube components need not be in S_E. That does not break identification: at `s=1`, consistency and `sum eta_Q=1` recover the whole projected walk. The three exclusion margins in Dcc are `2R-4`, `R-3`, and `R-6`, all positive for R>=16. The views equal the summed field on the local source/density read regions. Thus the sum A is in S_E and satisfies the projected nonlinear fixed-point equation. Given the quoted Ward identity and CCP bound, `g=P^T(K'_A)^T g` with operator norm at most 1/2 forces `g=grad F(A)=0`; uniqueness on the fixed small ball identifies A with x(B). No nonlinear orbit-coverage claim is required.

One qualification is essential: Dcc's sentence `valid for every source since the box chain applies P_cc first` is **not established by CCL'**, which assumes a cc input to obtain its k-uniform norm bound. The proof is valid on the product space of cc cube sources, which contains every actual iterate and nonlinear source. Restrict that norm claim to this invariant space; projection alone cannot supply the missing general-source estimate.

### W6. H2W repairs the old weighted-domain gap, with a minor geometric correction

**Verdict: CONFIRMED for the corrected named-input implication; REFUTED for the intermediate odd-torus diameter formula. Claim status: CONDITIONAL.** Targets: `BFT4W55.md:445`, `Corollary H2W`; :449, `diam_1 <= 4 floor(T/2)` (mathematical glyphs in source); :707, `E1`; :725, `E8`.

The repaired argument uses an unweighted cc inverse on each fixed-size local torus, not an inverse applied to an exponentially multiplied non-cc source. Localise the input norm to the box read region, bound the full unweighted box chain, and multiply by the ratio of the largest output weight to the smallest input weight. This is legitimate even when the input norm includes a sum of level suprema: the same scalar ratio bounds every level, and the commutator has the explicit summable profile from W4.

A conservative geometry avoids relying on the claimed tight `O_box=box^(R+5)`: Pi_E's field support is in `box^(R+4)` and the field norm has read radius at most 3, so use `O_box=box^(R+7)`. The input quantities are in `I_box=box^(2)`. Both are in a box of side less than `4R+14`, hence l1 diameter less than `16R+56`, still below the printed `D_W=16R+80`. The six-per-coordinate overlap count also remains sufficient. Thus

`||R_tilde||_weighted <= exp(mu D_W) epsilon_W`,

`||P_tilde||_weighted <= exp(mu D_W) G_P`.

At `epsilon_W<=1/4` and `mu<=log(2)/D_W`, these give remainder norm at most 1/2 and inverse norm at most `4G_P`. RWE already puts its output in S_E. This proves the implication from zero-weight local bounds, without importing a positive-weight inverse. For the advertised rate with denominator `16R_H+80`, **choose the walk size R=R_H** (or an upward integer rounding, and use that rounded value in the denominator). For a separately chosen larger R, the displayed proof uses `16R+80`; one must not substitute the smaller threshold into its weight-ratio inequality.

The small-torus line's intermediate estimate `diam_1<=4 floor(T/2)` applies to coarse sites, not to all the fine link base points being weighted. For T=5,L=3,k=1, take two parallel level-0 links whose integer bases differ by `(7,7,7,7)` on the side-15 fine torus. Their coarse l1 distance is `4*(7/3)=28/3`, exceeding the printed `8`. For that same-orientation grid the exact diameter is `4 floor(T L^k/2)/L^k`; a universal bound for all base points is **2T**. The following bound `exp(mu(8R+28))` already uses 2T and survives. The T=3,4 bound `exp(8mu)` also survives.

Complex constants must be frozen **after** §10 E8. Write `G_R=G_inv+L C_GV`, `G_C=2G_R`, and `P_C=2(C_Pi+1)`. With `A=n_R(t_N+1) C_c^sigma C_y(1/4)`, the complex walk has `epsilon_W=4 A G_C/R`, `R_W^0=8 A G_C`, and `R_H=16 A G_C`. The cube-family threshold is the distinct function `R_W(bar{s})=16*9^d C_c^sigma G_C C_y(1/4) bar{s}`. The symbols in the original §1/§5 definitions of G_sharp require the identification `G_gv=L C_GV`; otherwise take a common upper bound rather than silently equating constants.

### W7. The direct energy argument has the right sigma summability; the nonlinear source input is still conditional

**Verdict: CONFIRMED for the energy implication and Cauchy argument; NOT-VERIFIED for discharge of the local nonlinear source hypothesis. Claim status: CONDITIONAL.** Targets: `BFT4W55.md:495`, `Lemma F^σ`; :507, `Lemma E2^σ`; :530, `Corollary E3^σ`; :722, `E7`.

For the soft density the real-domain identity `Re tr(rho G)=0` follows from anti-Hermitian traceless rho and `G=H+i theta I` with H Hermitian. Its holomorphic continuation vanishes identically. Removing that linear term therefore leaves the displayed quadratic exponential remainders. The trace inequality and the power series give `|Phi|<=(3 e sqrt(N)/2)|rho|^2` on the stated norm domain.

Assuming the named **complex local** estimate `|rho-r|<=C h_l^3 eta^2`, a level with q=k-1-l contributes at most a fixed multiple of

`|Q| [L^(-2 sigma q) eta^2 + L^-6 L^(-2q) eta^4]`.

Both sums converge uniformly in k for sigma>0. The first is `(1-L^(-2 sigma k))/(1-L^(-2 sigma))` if q=0,...,k-1; the non-top sum actually starts at q=1. At sigma=0 the majorant grows with the number of levels; this does **not** by itself establish that every actual energy does. The Wilson volume factor `L^(4k)` cancels its squared curvature factor `L^(-4k)`. At the top, subtracting D(0;B) yields the required mixed bound `(||x||+||B||)||x||`. These are genuine d=4 power counts, not conclusions drawn from a d=2,3 script.

For the trapezoid defect, if `f(z)=sum D(zu)`, then `f(z)-f(0)-z(f'(0)+f'(z))/2` has zero coefficients through degree two, with cubic coefficient `-f_3/2`. On `|z|=2 rho_E/(3||u||)`, Cauchy in t on radius 1/2 controls both derivative pairings inside the E2 domain. A bound `4 C_E2 rho_E(rho_E+||B||)|Q|` for this circle yields exactly the printed safe coefficient `(27/8) C'_E2 (rho_E+||B||)/rho_E^2` with `C'_E2=4 C_E2`. Thus E7's definition repairs the formerly undefined constant; the larger printed coefficient is safe.

F^sigma, unlike this power count, still needs the per-density local analytic derivative estimates in W1, including the cutoff plain-current Hölder control. Its global-hypothesis-to-local-hypothesis passage is not discharged by citing CB or by the exact cutoff calculations. The family theorem therefore remains conditional on this input.

### W8. The small-torus fallback does not retain the printed large-torus prefactor

**Verdict: REFUTED for carrying the fixed prefactor into the specified fallback; NOT-VERIFIED for the literal all-torus quantitative assembly. Claim status: GAP in that bound, repairable without changing k/T uniformity.** Targets: `BFT4W55.md:612`, `Small tori`; :620-627, `Theorem BFT4a-glob` and `2e^{m_0}C_R`.

The large-torus argument proves `2 exp(m_0) C_R`. The small-torus paragraph instead puts the entire torus into one polymer and proves a bound containing `exp(m_0 |X|)`. Section 7 then states the **same** large-torus prefactor for every T. That replacement is not harmless when m_0 is an arbitrary input and the local constants have already been fixed.

Here is a counterexample to that prefactor transfer for the prescribed fallback, within SU(2), not an external scalar model. Fix all local analytic/linear constants and sigma>0 before varying m_0, as in the assembly. Set `a=diag(i,-i)` and put `B_c=t a` on direction-1 top links, zero otherwise. The chain `x_j=h_j t a` on direction-1 links has every plaquette product equal to I and every soft residual zero. Indeed, all contour transports commute and equal `exp(L h_j t a)`; their average is that same SU(2) matrix, so its near-identity maximiser W_0 is that matrix. All density gradients vanish and F=0.

The commuting gauge transformation with parameter `Lambda x` is exactly additive in the logarithms. It vanishes at the top roots and sends this chain to `Pi_E x` in S_E without changing the data or energy. Here the box minimiser is explicit in fine coordinates: `lambda_X(z)=-h_0 t (z_1-c_{X,1}) a`, since it makes the box potential zero and is pinned at its root. The fixed quintic tents consequently give a homogeneous field norm bounded by a fixed multiple of |t|, independently of the torus side. For small enough t, the named slice uniqueness therefore identifies the branch value as **E_k^br(B)=0**. The example already works at k=1. Meanwhile `S_W(e^B)=0` and

`E_empty(B)=kappa_{k-1} T^4 * 2(1-cos t)`.

Take `t=epsilon/2` in the Hilbert-Schmidt normalisation (`|a|=sqrt(2)`), so `max|B_c|<=epsilon`. For epsilon<=2, the exact alternating-series bound gives `2(1-cos t)>=11 t^2/12>=2t^2/3`, hence `E_empty>=kappa_- T^4 epsilon^2/6`.

Choose the integer `T=ceil(4R)+2`, which is below `4R+14`. A permitted product partition has two intervals per coordinate, each of length between `M_c=2R` and `2M_c`; hence **|X|=16**. The prescribed single-polymer activity is `R(X)=-E_empty`, so its anchored weighted size is at least

`(kappa_-/6) T^4 epsilon^2 exp(16m_0)`.

Now use the actual printed constants. Write `s_rad=bar{s}=1+K_rad exp(m_0)`, `K_rad=2^42*80e`, and `a_poly(s_rad)=256 mathfrak{c} c_g`, so `c_v r_s=a_poly(s_rad) s_rad^3 epsilon` in d=4. These are distinct from the depth q and nonlinear Lipschitz constant K used elsewhere. Since R>=16 and the only R dependence of mathfrak{c} is the bounded factor `C_M^sigma(R/4)`, a_poly has a fixed upper bound as m_0 grows. Consequently

`2 exp(m_0) C_R = 2^41 C_E2 (4R)^4 epsilon^2 exp(m_0) [a_poly(s_rad)^2 s_rad^6 + a_poly(s_rad) s_rad^3]`

`<= C_pref R^4 epsilon^2 exp(7m_0)`

with C_pref independent of m_0. Since T>=4R, the ratio of the fallback's actual weighted size to this claimed bound grows at least as a positive constant times **exp(9m_0)**. The selected epsilon tends to zero (the `r_s` smallness constraint already forces it), so the small-data qualification is satisfied. All powers are symbolic; no numerical experiment or claimed value of an uncomputed constant is used.

This refutes the **fixed displayed prefactor for that construction**, not existence of a bounded polymer expansion. One could change the small-torus decomposition, or enlarge the prefactor. Retuning C_E2 as an extra function of m_0 after this comparison is also an enlargement, not a proof with the previously fixed local constant.

An explicit safe repair is

`C_all = max{2 exp(m_0) C_R, exp(16m_0) C_E2 (4R+14)^4 (C_0+1) C_0 epsilon^2}`,

using at most two intervals per coordinate for small tori (one whole-torus interval when T<M_c). Add the separately stated `C_empty` for the singleton terms of `E_empty-S_W`. These constants are independent of k and T. Also impose `epsilon<=rho_E/C_0` unless a comparison already proves the small-torus solution lies in E2's homogeneous-norm radius. Section 6.6 only explicitly bounds `c_v r_s+epsilon` by rho_E; it does not state the comparison to C_0 epsilon. If upstream C_0 controls the data-inclusive norm, first replace it by a homogeneous-norm bound, at most C_0+1.

### W9. Assembly, smallness and the prior V2b/V4/V7 verdicts

**Verdict: CONFIRMED for the corrected conditional construction and prior arithmetic/domain criticisms; NOT-VERIFIED for closure from already-banked inputs alone. Claim status: CONDITIONAL, with W1 and W8 obligations retained.** Targets: `BFT4W55.md:582`, `Theorem BBcc`; :632, input table; :744, `V2b`; :751, `V4`; :761, `V7`; `BFT34_55.md`, `π_l ≲ L^{3+σ}`, `Corollary RW-cc-walk`, and `at s ≡ 1 the fixed point is CCP (d)`.

The large-torus construction does not have an impossible smallness gate. Freeze the complex constants, R and bar{s} first, and put `a_s=4 mathfrak{c} bar{s}^2 c_g`, so `r_s=a_s epsilon`. The explicitly stated admissible epsilon is the minimum of positive bounds

`c_g/C_N`, `min(eta_*/8,rho_E)/(c_v a_s+1)`,

`1/[2 mathfrak{c} bar{s}^2 C_N c_v (2c_v a_s+1)]`,

`r_u/(t_X 2^d a_s)`, `b_u`, `r_u/C_0`, and `epsilon_0^{BFT-E}`.

There is no self-consistency loop once those inputs are fixed. Since mathfrak{c} depends on R, the function called epsilon_cc(bar{s}) must be evaluated at the selected R, or at the worst allowed lower endpoint before asserting it uniformly over larger R. Apply E8's complex constant replacements before taking the minimum. W8 adds a small-torus energy-domain condition and changes the final prefactor.

Given the local source estimate, the enlarged cube map has contraction factor <=1/2, preserves its support class, and splits when inter-class bonds vanish. Iterating the fundamental theorem of calculus once in each bond produces the connected-bond expansion: a derivative involving two disjoint bond components kills every additive class term. A connected spanning bond set on n cubes has at least n-1 bonds and is among at most `2^(40n)` subsets; Cauchy contributes `(bar{s}-1)^(-|Gamma|)`, while `n<=2^(n-1)`. Thus the displayed **large-torus** bound `2^40 C_E [2^41/(bar{s}-1)]^(n-1)` follows.

For completeness the rooted-set count can also be rebuilt: on a graph of degree <=80, label the root 1 and other vertices 2,...,n. A labelled spanning tree has a length-(n-2) Prüfer code, so there are `n^(n-2)` possibilities; embedding it from a fixed root has at most `80^(n-1)` choices. Each connected set is counted at least `(n-1)!` times. Moreover `log((n-1)!) >= integral_1^n log(t) dt - log n = (n-1)log n-n+1`, so `n^(n-2)/(n-1)! <= exp(n-1)/n <= exp(n-1)`. Thus `(80e)^(n-1)` is sufficient (n=1 separately). The stated geometric series follows. This combinatorial implication cannot supply its own analytic premise.

The prior numerical correction V2b is independently correct: for n=k-l,

`L^(3n) L^2 L^-n L^(-(2+sigma)(n-1)) = L^(4+sigma) L^(-sigma n)`.

Thus the old `L^(3+sigma)` loses one L; at L=3 it is a factor 3. With the same prefactor its sigma=0 sum is `k L^4`, not `k L^3`. This is compatible with WC's separate, sharper column-count bound in W4.

V4 is correctly rejected **as the printed proof/supply**: a stated l-infinity reach `2R+6` alone gives l1 reach `8R+24`, and exponential multiplication need not preserve cc (a plaquette cycle acquires unequal incoming/outgoing weighted currents). A corrected radius is at best `log(1/epsilon_W)/(8R+24)` from that old reach information, before other norm costs. This does not prove every possible inverse violates the old rate; it refutes that inference. W6 supplies a different, valid conditional argument.

V7's NOT-VERIFIED status was appropriate for the old unprojected family: criticality without a slice does not identify the named slice solution. W5 repairs this algebraically. It does not establish nonlinear gauge-orbit coverage, nor require it.

The remaining key failure of the claimed banked-input closure is W1: the local analytic input (R) is explicitly extra in item 11 of the target's own table. Its source proof was not available within this review's permitted files. Neither the global summary nor the finite script verifies it. BFT4a-glob can be banked here only as a **corrected conditional theorem with (R)/F^sigma and the named zero-weight linear, projection, Ward and local analytic estimates explicit**, not as a newly closed consequence whose every input has been independently discharged.

### W10. b4w55_1 is a reproducible finite algebra check, not an analytic gate

**Verdict: CONFIRMED at its disclosed finite scope. Claim status: PROVEN only for the enumerated exact identities/check instances; the infinite-family claims retain their separate proofs/premises.** Targets: `checks/b4w55_1_criteria.md:20-50`, P1-P5 and K1-K4; `checks/b4w55_1_cen1.py:97`, :137, :153, :206-221; `BFT4W55.md:691`, `Check record`.

I read the criteria before the implementation and saved results. Filesystem birth and modification times support the corrected chronology: criteria **2026-10-29 03:17:34 UTC**, script **03:18:48 UTC**, output created **03:19:13 UTC** and last modified **03:19:25 UTC**. This supports criteria-before-script; it cannot independently certify that no unrecorded earlier experiment occurred. Section 15 explicitly retracts the guessed section-heading times, so those guesses are not used as evidence.

I replayed the script once with `python3 -I -B`, in memory and without writing another file. Its sole `float(worst)` **informational formatting** was replaced in memory by exact Fraction formatting; no gate, seed, coefficient or control was changed. Actual output: **OVERALL: PASS**, all P1-P5 pass for d=2,3 and all four controls fire in both dimensions.

| Exact measurement | d=2 | d=3 |
|---|---:|---:|
| Nonzero P1 moments / tested entries | 0 / 128 | 0 / 1728 |
| Maximum absolute row sum | 43/9 | 499/81 |
| Maximum absolute column sum | 1 | 1 |
| Maximum l1 displacement | 3 | 4 |
| P2 largest exact ratio | 347356279471/32355600076800 | 215450784104629/47442608309096000 |

Decisiveness, gate by gate:

- **P1:** compares geometric moments to zero. K1, K2 and K4 actually make this check fail; the overall conjunction requires those failures. It is neither vacuous nor an unsatisfiable acceptance gate.
- **P2:** the criterion explicitly discloses that the bound follows from P1 and the triangle inequality. Its implementation uses the Taylor decomposition to compute the left side and a termwise majorant for the right. It tests that finite implementation; it cannot independently validate the Taylor argument, a sigma norm, or a k-uniform estimate. There is no separate P2 negative control. The small observed ratios are not a sharpness certificate.
- **P3:** compares direct evaluation of two bilinear energies with an independently assembled four-slot pairing. Omitting j_S makes it fail for every tested seed (K3 requires this). The algebra is valid for **any** Q matrix with the matching residual definition, so P3 cannot decide whether the chosen Q is the right S4' linearisation or whether its norm bounds hold.
- **P4:** compares the summed corner moment to the separate geometric formula and also requires a nonzero value. It can detect a wrong offset or constant response; it is not a test of the whole k-dependent CORNER witness. That witness was derived in W3.
- **P5:** compares measured row/column/reach quantities to explicit independent bounds. These can fail for wrong normalisation or longer contours; no false claim of a d=4 enumeration is made. W4 gives the separate dimension-independent counting argument.

The final `ok` includes all five gates and all four controls. No check establishes (R), complex analyticity, H2W, slice uniqueness, k-uniformity, or the small-torus prefactor. Calling this finite PASS evidence for those conclusions would be an invalid promotion; the criteria themselves make that boundary explicit.

## Evidence and citation boundary

Only the assigned deliverable was written. No git commands, snapshots, ledgers, subagents, network lookups, source edits, commits, NumPy, BLAS or floating-point scientific calculations were used. Read files: BFT4W55.md; bounded ranges/search matches of BFT_B.md, PROOF.md, BFT34_55.md and CODEX_REVIEW_BFT34.md; the named b4w55_1 criteria/script/output/error bundle; and the two methodology files identified in PRE-STATED. The check replay and the independent rational arithmetic printed to stdout only.

Final mathematical review checkpoint: **2026-10-29 04:13:03 UTC**. Findings concern the inspected file contents and locating strings; no repository revision was obtained because git was prohibited.

Locating strings were used before citing lines. The target's sole numbered PROOF read pointer, `PROOF.md l.1-40`, still contains the claimed `[S26-BANKED]` batches, including the K, GV, GSHARP and BFT34 scope statements. The sampled BFT_B pointers for Setting W, the cutoff proof, the walk, and the elliptic slice match their named sections. No drift was found in these inspected pointers. Pointers into the unread KOFF/GV/GSHARP/BFT_A source files are **NOT-VERIFIED**, not silently certified. Section 10's R_W/R_H, remainder and complex-constant corrections were applied before evaluating conclusions.

The weight-rate mu is also reused as a contour direction index in §4; the context distinguishes these occurrences, and no erroneous comparison was found from that reuse. In contrast, R_H versus R_W(bar{s}) and real versus complex G_sharp change actual thresholds and must stay separated as in W6. The local constants must be fixed before the smallness minimum and before testing the all-m_0 prefactor claim.

## Summary table

| Finding | Verdict | Claim status / banking consequence |
|---|---|---|
| W1: (R), local balls and source provenance | NOT-VERIFIED | H3/F^sigma remain CONDITIONAL on a genuine local analytic input |
| W2: same-weight multilinear LD | REFUTED | Use compatible output/input exponents; H3(c)'s intended repair survives |
| W3: CEN1 and CORNER, after E4/E5 | CONFIRMED | PROVEN for the specified contour map and all-chain multiplier class |
| W4: centred WM/WC and summable J profile | CONFIRMED | Elementary estimates PROVEN; map identification remains an explicit input |
| W5: Pi_E walk, cc pieces, clause (d), slice identification | CONFIRMED | CONDITIONAL on named kernel/linear/Ward bounds; use cc source space |
| W6: H2W | CONFIRMED | CONDITIONAL; zero-weight local estimates suffice; freeze corrected constants and actual R |
| W6: odd-T diameter `4 floor(T/2)` | REFUTED | Fine-grid witness 28/3>8; use 2T; final small-torus weight bound survives |
| W7: E2/E3 power count and complex Cauchy argument | CONFIRMED | CONDITIONAL on local complex density estimates; F^sigma still uses W1 |
| W8: unchanged all-torus prefactor | REFUTED for prescribed fallback | GAP repaired by C_all and an explicit small-torus energy-domain margin |
| W9: V2b and V4 criticisms; V7 boundary | CONFIRMED | Old power/rate inferences REFUTED; old slice identification NOT-VERIFIED |
| W9: BFT4a closure from already-banked inputs | NOT-VERIFIED | Corrected theorem is CONDITIONAL; do not mark every premise discharged |
| W10: b4w55_1 record and replay | CONFIRMED | Exact finite PASS, four controls fired; no analytic or k-uniform promotion |

## Exactly what may be banked

1. **PROVEN:** the centred first-moment cancellation, the lower-corner all-chain multiplier obstruction with its bounded E5 error, and the centred cutoff/commutator estimates for the explicitly specified contour map. The J profile is summable for every sigma>0; sigma=1 requires no residual-level sum.
2. **CONDITIONAL:** the projected cc walk and H2W from the stated zero-weight local-torus response and projection bounds, with actual walk size R, rate `log(2)/(16R+80)`, and all E8 complex replacements. The new algebra repairs the old constrained-domain and final-slice gaps.
3. **CONDITIONAL:** clause (d), slice identification, the sigma energy bound, the analytic family and connected-polymer construction, **with (R)/F^sigma and the local complex density, linear and Ward estimates named as premises**. Use W8's corrected all-torus prefactor/domain. This review does not independently discharge (R).
4. **CONFIRMED finite evidence:** the exact b4w55_1 measurements and firing controls at d=2,3,L=3,T_c=4. The dimension-independent algebra in this review, not that enumeration, supports its d=4 elementary conclusions.
5. **Do not bank:** the false general multilinear LD sentence, the coarse-site diameter formula for fine positions, the unchanged small-torus prefactor, a claim that all H3/F^sigma inputs have been verified, per-level branch identification, local gauge invariance of the pieces, or extension off the global potential-small domain.

**Single most dangerous unverified input:** (R)'s per-density/per-pair holomorphic estimates on properly defined local constraint sets, including the plain-current Hölder/routing bounds. Promoting aggregate banked estimates to those local estimates would silently certify H3, the nonlinear decoupling family, and both locality routes without the needed premise.
