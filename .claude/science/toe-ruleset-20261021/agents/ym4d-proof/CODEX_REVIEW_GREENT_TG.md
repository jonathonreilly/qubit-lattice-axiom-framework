# PRE-STATED — independent hostile review

UTC: 2026-10-28 22:14:18 UTC. Written before reading the target arguments or deriving their claims.

Scope: `GREENT.md`, `TGAUGE_PRICE.md`, and `checks/gt1_*`, `checks/tg1_*`. Only this deliverable will be written. No git commands, numerical quadrature, floating-point experiments, or large-file reads. Extra-read budget: the required `docs/ai_methodology/SCIENCE_WORKFLOW.md` and one applicable procedure, to be identified below.

Pre-stated targets and refutation conditions:

1. Reconstruct the operator, metric, boundary conditions, and quantifiers behind GREENT's Green-function constants. A symbol mismatch, unjustified uniformity step, or explicit counterexample refutes the corresponding claimed implication; failure to reconstruct a proof earns NOT-VERIFIED, not REFUTED.
2. Recompute the cell sum, claimed gain, and ideal-locality comparison with exact arithmetic. A bound obtained at a frozen parameter does not establish a subsequently universal claim. Any incorrect number will be replaced by an exactly derived expression or interval, distinguishing arithmetic from validity of its premises.
3. Decide whether the argument treats only the free level-0 Hodge Laplacian, and whether its kernel estimate actually supplies an R-uniform infinity-norm operator bound. Test the borderline four-dimensional summation and the role of finite support and cancellation.
4. Rebuild the gauge-null-operation and TG-EXCL arguments. Construct candidate measures explicitly; separate mathematical existence, definitional exclusion, and impossibility for the quantified family. Reformulate each negative statement as a positive claim with its assumptions visible.
5. Inspect every cited in-scope check and gate for logical power: could it fail, can it ever pass, does its conclusion follow from its own definitions, and does it test the claimed regime? Trace colliding constants to their defining strings and current lines.
6. Locate citations by strings in permitted files. Citations to files outside the allowed read budget will be explicitly NOT-VERIFIED; line drift will be asserted only when checked.

Verdict vocabulary: CONFIRMED / NOT-VERIFIED / REFUTED for review findings; PROVEN / ARGUED / CONDITIONAL / GAP / OPEN for mathematical claims. Existing status labels carry no evidentiary weight.

## Findings (appended during review)

Extra reads used: `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `docs/ai_methodology/skills/no-go-discipline/SKILL.md`. The user's read/write restrictions override that procedure's requests for additional reference files, ledger edits, and commits. Its counter-route, scope, and steelman tests are applied here; no packet approval or landing status is claimed.

Terminology clarification after reading the targets: “candidate measures” in the preserved pre-state means **candidate scalar gauge functions μ**. No probability-measure interpretation is used anywhere in the derivations.

### F1 — REFUTED: the written root-delta has the wrong sign

Attachment: `TGAUGE_PRICE.md:201-204`, compared with `:354-358`.

The definition is `μ_root = −s Φ δ_root`, but the proof later uses `μ_root(root) = +s Φ`. Set `q=n^d>1`, `s=q/(q−1)`, and take `Φ=1` on one block. For a root delta of amplitude `a`, the stated TGAUGE map is `Aμ−μ(root)=(1/q−1)a`. The written `a=−s` therefore produces **+1**, so the new value of Φ is **2**, not 0. The corrected amplitude is **+s**. With the original negative sign, the ledger gives `ΔP=−s𝒯`, `Δ𝒯=+𝒯`, and `ΔM=−(s−1)𝒯`; the absolute price ratio is unchanged. Consequently an absolute-value ratio check alone cannot detect this sign error. The positive-sign construction is viable as a function; whether it is admissible is a separate question addressed below.

Claim status: PROVEN counterexample to the displayed definition's claimed action; the corrected conditional calculation is PROVEN from the displayed map.

### F2 — CONFIRMED, narrowly: GREENT studies the free level-0 operator

Attachment: `GREENT.md:56-57,140-158,204-217`.

Writing `d=Σ ε_μ ∂_μ`, `d*=Σ ε_μ* ∂_μ*`, the exterior anticommutator is `ε_με_ν*+ε_ν*ε_μ=δ_μν`. Commuting the scalar coordinate differences therefore gives `dd*+d*d=Σ ∂_μ*∂_μ`, with symbol `Σ(2−2cos p_μ)` on each component. No background link transport appears. Exact sources have zero componentwise mean by telescoping. This verifies the free, trivial-background, level-0 interpretation and the legitimacy of the mean-zero inverse for such sources. It does **not** derive a covariant SU(N) background bound. The file explicitly declares this restriction, so the restriction is not itself an undisclosed defect.

Claim status: PROVEN for the specified free complex.

### F3 — REFUTED: the periodisation-factor aside

Attachment: `GREENT.md:275-279`, specifically `Ω ≤ 3 once λR ≳ 1`.

For every finite `a=λR>0`, `Ω=1+2/(1−e^(−a)) = 3+2/(e^a−1) > 3`. The corrected statement is `Ω↓3` as `a→∞`; for example `a≥log 3` gives `Ω≤4`. The displayed periodisation inequality can still be true with its actual Ω. This finding does not by itself refute the Green bound.

Claim status: PROVEN correction. The unconditional `Ω≤3` is also repeated at `GREENT.md:582`.

### F4 — NOT-VERIFIED: the four advertised Green constants; REFUTED: their claimed certification

Attachments: `GREENT.md:281-314,583-585,683-689`; `checks/gt1_const.py:87-119`.

The analytic argument defines constants by suprema over **all** `R≥3` and `0≤s≤R/2`. The script instead checks fourteen s-values and four side factors. There is no enclosure of the omitted parameters. Its integral uses the maximum of two endpoint samples and a midpoint, which is not a supremum over an interval; it supplies neither a derivative/error bound nor the positive tail above `10^6 max(s²,1)`. The small-time stub is `t_lo f(t_lo)`, without a proof that this bounds the integral. IEEE doubles have no outward rounding. A finite λ-grid is harmless in the stated direction, but that fact does not repair the other three operations.

Thus **54, 1703, 429, 27250 are NOT-VERIFIED upper bounds**, not numerically disproved here. No corrected universal constants have been established in this review. The file itself concedes at `:686` that its quadrature is “not a proof,” contradicting the theorem/tally's PROVEN status. Exact small-torus measurements cannot fill an unbounded-domain certification gap. The assertion of a monotone profile also conflicts with its own printed sample: `gt1_const_out.txt:13-15` increases from s=1 to 2 for the first derivative and from s=2 to 4 for the second. The printed endpoint values are samples, not certified limits.

Claim status: GAP in explicit, R-uniform certification. Retain the formulas and the analytical kernel reduction separately from their numerical certification.

### F5 — CONFIRMED: logarithmic majorant; REFUTED if used as a uniform infinity-operator bound

Attachments: `GREENT.md:175-176,290-292,400-401,452-469`.

Count a four-dimensional l1 shell by choosing j nonzero coordinates, signs, and a composition of s: `a_4(s)=Σ_{j=1}^4 2^j binom(4,j)binom(s−1,j−1)=(8s³+16s)/3` for integer `s≥1`. Hence

`Σ_{0<|x|_1≤N}|x|_1^(−4) = (8/3) H_N + (16/3) H_N^(3)`.

The first term diverges logarithmically. Norm equivalence gives the same divergence for the Euclidean majorant. On a finite torus the sum is finite; it is not uniformly bounded as its side grows. A pointwise kernel bound is not an infinity-to-infinity operator bound: for scalar convolution its induced infinity norm is `Σ_z |K(z)|` (choose the signs of the input to maximize one output). The **upper** bound `|K(z)|≤C|z|^(−4)` alone does not prove that the actual kernel's norm diverges either; that would require a lower bound or another argument about K. Cancellation against a restricted localized source is a distinct statement.

The later criticism is therefore correct about what GT-2 alone cannot supply, but it would be wrong to say GREENT promises a T-uniform column sum: `:461-469` explicitly denies that. Its localized-source sup leg needs separate scrutiny below. The stronger assertion that the actual composite response's logarithm is “irreducible” (`:459,608-609`) is NOT-VERIFIED: an upper profile is not a lower bound on that response, and higher moment cancellation has not been excluded.

Claim status: PROVEN summability calculation; GAP for a uniform operator bound or an actual-response lower-bound/no-go conclusion.

### F6 — CONFIRMED only as an identity: TG-PRICE does not establish a size obstruction

Attachments: `TGAUGE_PRICE.md:232-279,325-340,407-435,449-455`.

Let `r_X=μ(c_X)` and `a_X=Aμ(X)`. Rebuild the displayed ledger algebraically: `ΔP=n²⟨D,r⟩`, `Δ𝒯=n²⟨D,a−r⟩`, so **`ΔM=n²⟨D,a⟩`**. If r is constant and `ΣD=0`, then `ΔP=0`. If the shift additionally kills Φ on the charged roots, then `Δ𝒯=−𝒯`, and therefore `ΔM=−𝒯`. This proves `ρ=1` **only when `𝒯≠0`** and the elimination condition holds. For `𝒯=0`, the corrected conclusion is `ΔM=0`; `0/0` is undefined. A general admissible μ, such as μ=0 when `𝒯≠0`, does not have `ρ=1`.

This is a valid conditional conservation identity, not evidence that |P| is large or that all estimates after a gauge choice are equally good. Algebraically one can have `P=0`, `M=𝒯≠0`, and after the shift `M_new=0`; the ratio is still 1. The identity alone supplies no lower bound on P in the actual response/source class. Consequently the inference “ρ=1, therefore face (b) is an obstruction / no useful representative remains” is REFUTED **as an implication from this test**. Whether the actual response has the required uniform bound remains OPEN. The file admits it computes no response field at `:449-455`.

The advertised three-way decision cannot return LESS or WORSE while all its own in-domain hypotheses and identities hold. A failure can detect a broken identity or implementation; it cannot decide the actual estimate's sharpness. An inadmissible control tests a different domain. Correct narrow no-go: *no admissible Φ-eliminating shift can make `|ΔM|<|𝒯|` when `𝒯≠0`*. No broader route closure follows.

Claim status: PROVEN implication from the displayed ledger assumptions; GAP in the claimed analytic obstruction and upstream identification.

### F7 — CONFIRMED narrow exclusion; REFUTED exact saving factor; positive reformulation

Attachments: `TGAUGE_PRICE.md:350-370,535,613-614`.

On each block with q=n^d sites, **any** prescribed average a and root value r are realized by

`μ(root)=r`, and `μ(z)=(q a−r)/(q−1)` at its q−1 nonroot sites.

Indeed their sum is `r+(q−1)(q a−r)/(q−1)=q a`. Thus root evaluation and block average are independently surjective coordinates. To eliminate Φ take `a=r−Φ`. Three choices give:

| r | a | μ and effect |
|---|---|---|
| 0 | −Φ | admissible flat-with-hole field; `ΔP=0`, `ΔM=−𝒯` |
| sΦ | (s−1)Φ | **corrected positive-sign** root delta; `ΔP=s𝒯`, `ΔM=(s−1)𝒯` |
| Φ | 0 | `μ=Φδ_root−Φ(1_B−δ_root)/(q−1)`; `ΔP=𝒯`, **`ΔM=0`** |

The last choice kills Φ with exactly zero regrouped-main-term price, is finitely supported for finitely supported Φ, and is different from the root delta. For nonconstant Φ it is excluded by Λ_0; it does not refute the narrow admissible no-go. It establishes positively that the root delta is neither unique nor optimal among excluded functions. Exclusion is **necessary**, not sufficient, for beating the nonzero admissible ratio; many excluded functions do not do so. The word “precisely” at `:367-368` is defensible only as this necessary restriction, not as an equivalence with all excluded functions. No refutation of the corrected narrow TG-EXCL identity is claimed.

For the corrected root delta, its price fraction is exactly `1/(q−1)`. The saving factor relative to |𝒯| is therefore **q−1, not q**: at `(d,k,L)=(4,2,3)`, **6560**, not 6561; the other reported examples give 80 and 728, not 81 and 729. The different ratio `|ΔP|/|ΔM|=q` is correct but is a different comparator. Whether changing this level-0 P changes the full f_0 after its other terms are included is NOT-VERIFIED, not established by this ledger alone.

Claim status: PROVEN constructions and corrections from block arithmetic; CONDITIONAL interpretation through the displayed ledger.

### F8 — REFUTED: exact TV optimality and exact point/flat comparison

Attachments: `TGAUGE_PRICE.md:286-323,342-344,388,534`; independently checked using plain Python integers/Fractions, without running the source scripts.

Take d=4, L=3, k=2, l=1, Φ=1 on one block `[0,9)^4` and zero elsewhere. Its root is `(4,4,4,4)`. Define μ=−1 on that block except on its central `[3,6)^4` subblock; set μ=−81/80 on that subblock's 80 nonroot sites and μ(root)=0. Set μ=0 outside. This is admissible, has `A_k μ=−Φ` **on every block**, and has `A_l μ=−1` on all `3^4` level-l sites in the target block. Therefore

`TV_l=2d·3^(d−1)=216`, and **`ρ_est=8`**.

The original flat field instead has `TV_l=44307/205=216+27/205` and `ρ_est=1641/205=8+1/205`. Both exact averages and TVs were recomputed independently. Thus the advertised flat field is **not** exactly optimal. This construction does not settle the unrestricted infimum or disprove an order-of-magnitude optimality statement.

The displayed TG-TV lower bound is valid when the block averages are prescribed on the two boxes under comparison: on each length-2N line all values differ by at most its TV, so the two averages do too; summing the N^(d−1) lines yields its inequality. It gives **1**, whereas the alleged optimal ratio is near **2d**; the lower bound by itself cannot prove that exact optimum. If (G) is imposed only on a subset 𝒳, it cannot control the oscillation of an arbitrary extension of Φ outside that subset.

The exact ratio between the two *original* constructions is **`L^(k−l)/[s(1+L^(−l)n^(1−d))]`**, not `L^(k−l)`. At d=4,k=2 the corrected ratios are **656/73**, not 9, for l=0, and **1640/547**, not 3, for l=1. The individual displayed flat/point formulas at `:301` are consistent with these corrections.

Claim status: PROVEN counterexample and arithmetic; OPEN exact optimization beyond it.

### F9 — REFUTED geometric steps; CONFIRMED salvage of GT-5

Attachments: `GREENT.md:343-350,379-388`.

The claimed cell separation `|y−z|_1≥(σ−1)L^k` at `:349` is false in d>1. For L^k=3 take y=(2,2,0,0) in cell (0,0,0,0) and z=(3,3,0,0) in cell (1,1,0,0). The coarse distance is 2, but the fine distance is **2**, not at least **3**. For cell displacement a the true minimum is `Σ_i max(0,L^k|a_i|−(L^k−1))`, hence at least `L^k(σ−d)+d` when all d coordinates can contribute; replacing d by 1 is invalid.

**GT-5 itself survives by a different proof, with a better constant.** Put h=L^k. Split the fine-site sum at `|y−z|_1≤h`. Its near part is at most `1+8h≤9h`, since `a_4(s)/s³=8/3+16/(3s²)≤8`. In the far part the kernel is at most h^(−3), and the total source weight is at most `h^4 c_m`. Thus the claimed sum is bounded by **`h(9+c_m)`**, which is stronger than the displayed `h(65+c_m)`. This proof works on the torus by selecting coordinate representatives and overcounting with infinite-lattice shells.

The same geometric error damages the tail proof. At h=3 choose the source cell x=0, y=(6,6,6,6) in cell (2,2,2,2), and z=(5,5,5,5) in cell (1,1,1,1). Then D=8 and D(z)=4 qualify for the “near region,” but the kernel point `y−e_0−z=(0,1,1,1)` has distance **3**, not the claimed `D h/4=6`. A sufficiently large torus avoids any wrap ambiguity. Thus the telescoping path is not everywhere at the asserted distance. Raising cutoffs and changing constants may repair the argument; the advertised GT-4 tail constants are NOT-VERIFIED by this proof. No counterexample to the final tail inequality is claimed.

Claim status: PROVEN geometric counterexamples and replacement GT-5 proof; GAP in GT-4's quantitative tail argument.

### F10 — REFUTED: a constant collision and two price-table counts

Attachments: `GREENT.md:365,410,418,677`; `checks/gt1_price.py:61,74`; `checks/gt1_price_out.txt:7`.

The far-region constant `𝔠_i` is `κ_𝔰 d(d−1)² M C_1^(1)` in the theorem but the pricing script uses `2κ_𝔰 d(d−1) C_1^(1)` after dividing by M. At d=4 the code evaluates **2/3** of the written constant. The corrected normalized coefficient is **`q_i=16/(65+c_m)`**, not the code's `32/[3(65+c_m)]`. The exact same symbol therefore denotes two different objects across theorem and check.

The claimed “l1 ball of radius 52” contribution **8.2·10^7** at `:418` is false. From the shell polynomial, its site count is

`B_4(r)=1+(2/3)r²(r+1)²+(8/3)r(r+1)`.

Thus **`B_4(52)=5,071,041`**, not 82,000,000. Moreover the script's `sat` is the **first unsaturated shell**, as its `next(prof(s)<1)` shows. Its printed 52 means full saturation only through **51**, whose exact contribution is **4,695,809**. The statement that a saturated radius-52 core contributes 82 million is wrong in both radius convention and count.

The metric-conversion aside at `:677` has `d^(d−1)=256`; at d=4 this is **64**. The **second** derivative conversion `d^d` is 256. The formulas at `:292` distinguish them correctly.

Claim status: PROVEN corrections. Recalculation of the actual torus price follows below; all such arithmetic remains conditional on the profile being a valid bound.

### F11 — REFUTED as an equality: the reported torus sum; corrected conditional prices

Attachments: `GREENT.md:399-418,430-450,471-472`; `checks/gt1_price.py:64-93,100-117`.

The definition sums over `(Z/T)^4`, but the script sums **infinite-lattice** shell counts up to 2T. This overcounts once a coordinate reaches the torus half-period. Its exponentially small discarded tails and unbounded-error harmonic approximations also prevent treating the printed value as a certified upper bound. Correcting just the shell domain makes a material difference. Correcting the `𝔠_i` collision in F10 makes a smaller, separately measured difference.

I recomputed the following using exact integer/Fraction interval arithmetic only. Inputs are **frozen exactly as printed**: `T=12,932,000`, `m′=24/625`, `C_1^(1)=429`, `C_2^(1)=27250`, `κ_𝔰=8`. Neither the current validity of the rate/threshold nor the kernel constants is certified by this arithmetic.

| Object | Certified enclosing interval / correction |
|---|---|
| c_m | `[7,362,215.5963, 7,362,215.5964]` |
| c_m^(1) | `[796,157,880.0396, 796,157,880.0397]` |
| q_n | `[7,033,896.9829, 7,033,896.9830]` |
| q_i from the **theorem** | `[0.000002173239, 0.000002173240]`; code used 2/3 of this |
| Infinite-shell envelope, code's q_i | `[251,354,548.67, 251,354,549.82]`; explains the reported `2.51355·10^8` |
| Infinite-shell envelope, theorem's q_i | `[251,356,910.35, 251,356,911.51]` |
| Torus shell correction to the power tail | `[−13,199,142.15, −13,199,142.14]` |
| **S_T as actually defined, with theorem's q_i** | **`[238,157,768.21, 238,157,769.36]`**, approximately **`2.38158·10^8`** |
| T^4 | **`27,968,088,406,917,376,000,000,000,000`** |
| **T^4/S_T** | between **`117,435,129,168,581,803,271`** and **`117,435,129,733,941,332,460`**; approximately **`1.17435·10^20`** |
| **S_T/c_m** | **`[32.348654, 32.348655]`**, replacing **34.14** for the actual torus sum |
| Corrected infinite-shell envelope / c_m | `[34.141476, 34.141477]`; 34.1 remains a reasonable rounded *envelope* comparison |

**Derivation and reproducibility of the enclosure.** Put `w=e^(−24/625)`, `Z=65+c_m`. The coefficients are

`c_m=((1+w)/(1−w))^4`, `c_m^(1)=4c_m[1+2w/(1−w²)]`,

`q_n=(1024·27250/429)c_m^(1)/Z`, `q_ii=1024/Z`, `q_i=16/Z`.

For even T and h=T/2, the **exact** torus shell generating function is

`(1+2x+…+2x^(h−1)+x^h)^4 = ((1+x)/(1−x))^4(1−x^h)^4`.

Consequently `a_T(s)=Σ_{j=0}^4 (−1)^j binom(4,j)a_4(s−jh)`, with `a_4(0)=1` and `a_4(s)=0` for s<0. The first 4000 profile shells were enclosed directly. Their last saturated shell is certified to be 51 and their first unsaturated shell 52. Beyond this cutoff the power tail uses `a_4(s)=(8s³+16s)/3`. Each shifted correction, with b=jh, is

`b^(−4) +(8/3)[H_1−3bH_2+3b²H_3−b³H_4]+(16/3)[H_3−bH_4]`,

where `H_p=Σ_{b<s≤2T}s^(−p)`. Multiply it by `(−1)^j binom(4,j)q_n` and sum j=1,…,4.

No quadrature is used. For any integer a<b and `f(t)=t^(−p)`, convexity gives

`Σ_{a<s≤b} f(s) = ∫_a^b f(t)dt + [f(b)−f(a)]/2 + E`,

`0≤E≤[f′(b)−f′(a)]/8`.

The last bound follows on each unit interval from the exact trapezoid error kernel `(t−a)(a+1−t)/2≤1/8`, then telescopes. The integral is a rational for p>1 and `log(b/a)` for p=1. Logs were enclosed after reduction to `[1,2]` by 60 terms of `2Σ z^(2i+1)/(2i+1)`, `z=(x−1)/(x+1)`, with remainder at most `2z^121/[121(1−z²)]`. The small exponentials were bounded by their 41st/42nd alternating Taylor sums. All interval operations used outward **integer** rounding at denominator `10^45`.

The suffix Xi is evaluated exactly in w from `Σ_{r≥j}r³w^r=w^j[j³/(1−w)+3j²w/(1−w)²+3jw(1+w)/(1−w)³+w(1+4w+w²)/(1−w)^4]` and `Σ_{r≥j}rw^r=w^j[j/(1−w)+w/(1−w)²]`. The omitted exponential profile contribution beyond 4000 was bounded between 0 and 1 using geometric tails for `r^4w^r` and `s^4e^(−3m′s/4)`; an additional exact check bounds it below `10^(−12)`. The profile at shell 4001 lies in `[0.000000027448701,0.000000027448702]`; all three summands decrease thereafter, so removing the min with 1 is justified. This deliberate one-unit enclosure and the convex trapezoid error explain the interval widths. The torus shell formula was also checked independently by exact enumeration at T=2,4,6, with respective totals 16,256,1296.

**Two limitations on the headline.** First, the final inequality at `GREENT.md:447` also contains `(𝔠_P^coul/𝔠_P)^2`. The cell-sum ratio alone is not a certified gain for the full N1-15 constant. Second, “34” is a fixed-T_0 comparison, not a bound for every T≥T_0: `S_T/c_m` grows logarithmically with T when m′ is fixed. Current upstream T_0, rate, and sup constants are NOT-VERIFIED under the read cap.

Claim status: PROVEN enclosed arithmetic for the displayed profile at the stated inputs; GAP in promoting these figures to a proven theorem price.

### F12 — NOT-VERIFIED: Coulomb projection versus one admissible family with both estimates

Attachments: `GREENT.md:140-159,355-389,455-458,695-699`.

The zero-mean curvature inverse is legitimate, but that fact does **not** make `b=d*Δ^(−1)dB` gauge-equivalent to arbitrary B on the torus. Let H project onto constant 1-forms. The componentwise Hodge identity gives

`B = dΔ^(−1)d*B + d*Δ^(−1)dB + HB`.

Thus `B−b=dΔ^(−1)d*B+HB`. A periodic gradient has zero mean. For B a nonzero constant 1-form, b=0 and B−b is not a periodic gradient. The corrected Coulomb representative is **`b+HB`**, unless HB=0 is separately imposed. This refutes the unrestricted statement that this b alone is a gauge choice. The file mentions the harmonic part later, but does not insert it into the displayed b definition and both-leg proof.

There is a second unresolved quantifier change at `:374-377`: GT-3 and GT-5 use an exponentially localized **column source** for Y=δ_x. For arbitrary bounded Y, replacing its amplitude by `sup|d_kY|` does not preserve localization about a single x. A column estimate cannot be promoted to a uniform infinity-operator estimate without a row-sum or cancellation argument. No such argument is supplied there.

Finally, `:366-373` imports the root-restoring gauge and its locality instead of deriving the quantitative tail for the corrected full family. An exponentially local interpolation operator does not by itself turn a nonlocal input gauge function into exponentially decaying data. The required input estimates, harmonic bookkeeping, and same-representative transfer are not available in the allowed files. This is **NOT-VERIFIED**, not a theorem refutation from unread sources. Even a certified free Green estimate would not discharge it.

Claim status: PROVEN harmonic counterexample to the unrestricted gauge identification; GAP in the admissible-family transfer and general-Y sup claim.

### F13 — CONFIRMED positive gauge identities; REFUTED independence claim for the price gate

Attachments: `TGAUGE_PRICE.md:24-27,215-228,488-508`; `checks/tg1_criteria.md:50-60`; `checks/tg1_price.py:95-123,154-193,384-405`.

**Re-derivation, without importing TENTQ.** In the straight average, summing a gradient along each L-link segment telescopes:

`Q_str(df)(X,ν)=L^(−d)Σ_r[f(L(X+e_ν)+r)−f(LX+r)] = d(Af)(X,ν)`.

Every axial path used in h has integral `f(endpoint)−f(root)`, independent of the coordinate order. Averaging its endpoints therefore gives **`h(df)=Af−ev f`**. At k levels, evaluate these identities at successive ancestral roots. The intermediate averages telescope, leaving **`Φ_k(df)=A^(0→k)f−f(c_X)`**. This verifies the sign convention used in F1, the explicit positive constructions in F7, and the use of **A**, rather than ev, for the straight average. The comparison with an unread TENTQ display remains NOT-VERIFIED as a citation, though its quoted mathematical identity can be tested here.

For the price gate, however, the script defines its forward funnel as `Φ=Σ_i E_i h_i Q_str^(0→i)` and defines `Ĉ_def=Σ_i (Q_str^(0→i))* h_i* E_i* D`. These are **transposes by construction**. The `h_fwd` and `h_T` functions even use the same HT table. Therefore `⟨Ĉ_def,v⟩=⟨D,Φv⟩` is an adjoint-consistency identity. The assertion “neither is the other's transpose by construction” at `tg1_criteria.md:56-57` is REFUTED. Distinct forward/scatter implementations can still expose a coding error; they cannot independently establish the response's size or the identification with an upstream COF term. After TG-A and TG-B, C2 is the same identity applied to dμ with a prescribed value of Φ(dμ).

There is also a source mismatch in the original tg1 ledger: `tg1_price.py:348` uses root charges ±1/2 for C, whereas `:422,430` builds unit path currents for D, whose divergences are ±1. That original script does not itself verify one complete same-source M/P/𝒯 ledger. The target says tg1b repairs this; its files are outside the literal permitted `tg1_*` glob and were not read.

**Concrete witness against using the ratio as a size test.** Independently enumerate axial paths at d=4,L=3,k=1 on side 6. Let c=(1,1,1,1), c′=(1,1,4,1), and put C=−1 on the three direction-2 links from c to c′. Then `d*C=δ_c−δ_c′`. Let `u=(1/8)d*δ_p` for the oriented (0,1) plaquette based at p=(2,1,1,1). Its divergence is zero, and it has only direction-0/1 links, so **`P=9⟨C,u⟩=0`**. Averaging all 24 coordinate orders and 81 endpoints gives **`Φ_1(u)(c)=−1/432`**, **`Φ_1(u)(c′)=0`**, hence **`𝒯=−1/48≠0`**. Thus the ledger has M=−1/48 before elimination and M_new=0 afterward, with ρ=1. This is an actual finite cochain witness to the logical distinction, not merely free variables in a ledger. It is **not** claimed to be the physical response Y^p or a counterexample to a worst-case theorem about that response.

Claim status: PROVEN free-complex identities and finite witness; GAP in the gate's advertised power to establish an analytic no-go.

### F14 — NOT-VERIFIED: the purported one-sided residual limitation

Attachments: `TGAUGE_PRICE.md:142-146,430-435,517-518`; compare its `:218-219` and `GREENT.md:143`.

An uncomputed change in a signed residual pairing is not automatically an increase in its absolute value. The displayed f_0 formula subtracts the residual sum (`TGAUGE_PRICE.md:41`); the assertion that any change “can only” worsen a bound has no sign or positivity proof. As a general inference about sums this is REFUTED: a change +a in one contribution and −a in another cancels exactly.

There is a sharper consistency issue. If r_m here is the chain defect implicit in `GREENT.md:143`, namely `r_m=Q_mY_m−Y_(m+1)`, and the **full** Q has the root-evaluation intertwining property asserted at `TGAUGE_PRICE.md:218`, then the displayed composite shift implies

`Δr_m=Q_m d_m ev_(0→m)μ−d_(m+1)ev_(0→m+1)μ=0`.

Under those matching definitions the residual is **inert**, contrary to TP-F5. Their identification across the two settings has not been established in the allowed files, so the actual residual conclusion is NOT-VERIFIED. Either supply a different definition and compute its change, or use the intertwining identity; neither route licenses the present one-sided assertion.

Claim status: GAP in the residual interpretation and sign claim; PROVEN conditional cancellation for the stated chain-defect definition.

## Gate audit — could each check decide its advertised question?

No supplied script was executed: some write output files or run floating-point work. Cached results below are **source records**, not fresh runs. New executed checks in this review were short plain-Python exact-arithmetic constructions/enclosures, recorded in F8–F13.

| Gate and current attachment | What can actually fail; review disposition |
|---|---|
| gt1-A; `gt1_green.py:150-181` | Independent incidence-vs-scalar formulas can fail; the displayed coderivative has the wrong sign (`:115,135`). Its recorded failure is meaningful. CONFIRMED sign defect. |
| gt1b-A, inside permitted `gt1_b.py:79-110` | Corrected signs give a meaningful finite identity check. It runs **3**, not the criteria's **10**, random forms (`gt1_criteria.md:24`, `gt1_b.py:87`). The all-degree identity is re-derived in F2; random agreement alone would not prove it. |
| gt1-B; `gt1_green.py:184-195` | Can reject a bad inverse or normalization. Correctly called solver validation; no implication of R-uniform decay. |
| gt1-C; `gt1_green.py:198-219,287-312` | Finite exact squared maxima can refute too-small constants on the sampled tori. The script **prints maxima but never performs the advertised comparison with C_1,C_2**. A manual comparison is possible; all-R certification is NOT-VERIFIED. |
| gt1-D and gt1b-D; `gt1_criteria.md:44-56`, `gt1_sweep.py:102-159` | The two sources both have zero mean: the “bare” source is δ−mean. What differs is concentration/first-moment control, not the binary zero-mean property. Strict radial monotonicity on finite torus shells does not follow from an upper decay bound. A bounded increasing sequence can still obey that bound. REFUTED advertised theorem-refutation rule. The author's stronger claim that the gate is formally unsatisfiable for every true power law is NOT-VERIFIED; it need only be unjustified to lose that power. |
| gt2-E; `gt1_sweep.py:87-88,160-166` | Endpoint growth at R=8,24 can fail its chosen bracket, but cannot prove uniformity over all R. The code's verdict covers axes, while the criteria at `:64` also names the diagonal. Its own recorded M1 rises from 0.040420 to 0.041791 to 0.042186 (`gt1_sweep_out.txt:65-67`), refuting GREENT `:518`'s “both decrease.” |
| gt2-F; `gt1_criteria.md:70-74`, `gt1_sweep.py:89-101` | Factor-two variation/monotonicity is neither necessary nor sufficient for the stated upper decay estimates. REFUTED inference “failure refutes GT-1/GT-2.” |
| Post-hoc fixed-direction probe; `gt1_b.py:142-195` | Explicitly no gate, and only a few directions/scales. It cannot certify an exponent or universal constant. NOT-VERIFIED as such certification. |
| `gt1_const.py:87-119` | No certified integral/supremum gate; F4. The finite λ-infimum is valid in principle, but does not validate time quadrature or an unbounded parameter sweep. |
| `gt1_price.py:64-93` | No criterion by its own header. Computes an approximate infinite-shell envelope, with a collided coefficient, rather than the displayed torus sum; F10–F11. |
| tg1-Z; `tg1_price.py:341-354,369-370` | Can detect a vacuous residue. It does fail in P1/P3/P4 generic fields, but **does not suppress their subsequent PASS labels** (`tg1_out.txt:194-205,243-246`). The prose later discloses the vacuity. |
| tg1-A/B/G; `tg1_price.py:293-339,356-382` | Averaged paths vs block averages is a meaningful normalization check, with a corrupted-block control. B's code verifies new Φ only on `supp ν`, although the original criteria ask every X. The outside-support conclusion follows from the re-derived local formula, not from that loop alone. |
| tg1-C1/C2; `tg1_price.py:384-407` | Can expose an implementation/adjoint defect. Cannot choose between real in-domain “equal/less/worse” after its algebraic hypotheses hold; F6/F13. Claimed non-transpose independence REFUTED. |
| tg1-D/F; `tg1_price.py:409-470` | D1 checks full-pushdown divergence; D3 then follows from adjointness and zero root values. The outside-domain control is useful for constraint sensitivity, not proof of an obstruction to better estimates. P1/P4 generic controls do not fire. |
| tg1-E; `tg1_price.py:472-520` | Tests only the two selected μ, not an optimum over μ. The upper gate `ρ_est≤2d` is impossible for its selected flat formula at finite n because `s(1+L^(−l)n^(1−d))>1`; it fails in all four models. The repaired exact formula still does not establish optimality; F8 supplies a better μ. |
| tg1-H; `tg1_price.py:522-548` | Can reject four fixed reference values in the displayed toy geometry. Tests k=2, not termination for every k≥2, and never computes Y^p. The cited reference file was not read. |
| tg1b B0–B5, as described at `TGAUGE_PRICE.md:500-508` | Files named `tg1b_*` are **outside** the user's literal `tg1_*` allowance; they were not read or run. NOT-VERIFIED implementation/results. On the descriptions alone: B0 tests non-vacuity; B1 consistency; B2 leaves the admissible domain; B3 compares formulas for selected μ, not an optimum; B4/B5 test block-average identities and multiplicities. None as described tests the actual response bound. |

## Symbol, quantifier, and citation audit

| Symbol | Actual local objects and attachment | Disposition |
|---|---|---|
| `C_1`, `Ĉ_1`, `C_1^(1)` | Euclidean, max-coordinate, and l1 constants respectively; `GREENT.md:288-309`; code `gt1_price.py:47` specifically takes the l1 429 | Kept distinct; no substitution of 54 for 429. Their numerical certification remains F4. |
| `C_2`, `Ĉ_2`, `C_2^(1)` | Corresponding second-derivative constants; `GREENT.md:289-309` | Same distinction; metric typo separately corrected in F10. |
| `𝔠_i` | Theorem `GREENT.md:365` versus code `gt1_price.py:61` | **Collision found**, factor 2/3, F10. |
| `Λ_0` | Fine torus in `GREENT.md:145`; root-constant function space in `TGAUGE_PRICE.md:176` | Different types; no admissibility inference is made from the common notation. |
| `κ` / `κ_𝔰` | Rate setting κ=1 at `GREENT.md:337`; shell constant κ_𝔰=8 at `:346`; root value κ at `TGAUGE_PRICE.md:253` | Three distinct quantities, not comparable constants. |
| `n`, `s`, `T`, `M` | n=k−j in GREENT `:117` versus n=L^k in TGAUGE `:174`; s=max-coordinate in GREENT `:207` versus root-hole normalization in TGAUGE `:175`; T=coarse side versus tilted time at GREENT `:253`; M=locality amplitude at GREENT `:326` versus pairing at TGAUGE `:238` | Type/definition changes explicitly tracked. |
| μ_root | Negative amplitude at `TGAUGE_PRICE.md:202`; positive at `:355`; **positive in the script** `tg1_price.py:343,367` since ν=−Φ | Concrete sign collision, F1. The script did not test the negative displayed definition. |

Quantifier defects: the finite `(s,R)` grid cannot certify all sizes; m′ and T_0 are frozen inputs, not verified current upstream outputs; the “34” comparison is only at T_0; a δ_x column is not arbitrary Y; TG-PRICE needs the Φ-elimination condition and nonzero residue for its ratio; TG-TV needs prescribed averages on the compared boxes; two μ do not exhaust an infinite-dimensional optimization; a statement about a test profile does not establish the actual response's size.

Citation disposition: sources were located by defining strings and inspected with current numbered ranges. No numeric `PROOF.md l.N` citation was found in these two targets; PROOF itself, snapshots, and audit ledgers were not read. The upstream NLOC/NORMS/BFT/TENTQ/YSUP citations therefore remain NOT-VERIFIED, rather than being assigned a fabricated drift finding. One **local dangling reference** is confirmed: `GREENT.md:646` points to “§G2.6,” but the file's section labels do not define §G2.6; the relevant present string is “Theorem GT-4” at `:355`.

## No-go discipline applied to the retained narrow statement

This is a scoped review, not a landing/audit packet. No procedural approval is claimed. The retained statement is exactly: **under the displayed ledger identities, root neutrality, admissibility, and complete residue elimination, `𝒯≠0` implies `|ΔM|/|𝒯|=1`.**

- **N1 — Alternative routes.** Six genuinely different mechanisms were considered: (1) change admissible μ at fixed eliminated Φ — ATTEMPTED, the algebra closes this exact-ratio route; (2) free the root values independently of block averages — ATTEMPTED, zero-price construction exists outside the admissible domain; (3) optimize the level-l TV estimator — ATTEMPTED, explicit admissible improvement in F8; (4) exploit cancellation in the invariant pairing — ATTEMPTED on a finite cochain, P=0 with nonzero residue in F13, while the actual response remains untested; (5) obtain decay from the actual root charges — OPEN, source class not available; (6) prove a restricted representative norm bound directly — OPEN, no such norm is evaluated in the supplied checks. The last two are not falsely labeled ruled out. There is no exhaustive no-go against these broader analytic routes.
- **N2 — Dependencies.** At fixed Φ elimination, ΔP=0 implies ΔM=−𝒯 through one ledger, so these are not independent walls/evidence. Root constancy and neutrality together imply ΔP=0; neither proves the size of P. The TV problem and actual response/source estimates are separate obligations; their independence is not asserted without witnesses. No numerical wall count is claimed.
- **N3 — Hidden premises.** Exposed: the identification of the ledger with the physical source/response, the root-supported divergence, neutrality, the Φ-elimination domain, nonzero residue for division, the full-Q versus straight-Q distinction, and the residual definition. The profile-class size is not inferred from a toy exact cochain.
- **N4 — Residual matching.** The price identity attacks `|ΔM|/|𝒯|`; the obstruction conclusion attacks a uniform bound on P/f_0. These residuals do not match. TG-TV concerns one directional/global variation lower bound; it does not prove exact optimization. The external YSUP/COF claims cannot supply matching proof under this read cap.
- **N5 — Resolution.** Per-site: the independent (a,r) construction works. Per-block: Φ elimination and the TV counterexample are explicit. Per-mode: no covariant/nontrivial-background statement was tested. Finite lattice: the conservation identity is algebraic. All k/T and the actual response: only the stated conditional identities extend; a size obstruction remains OPEN. No untested resolution is promoted.
- **N6 — Positive reframing.** Retain block-average/root-value surjectivity, the admissible conservation identity, and the sufficient norm reduction `|P|≤n²||C||_∞ inf_{μ∈Λ_0}||Y+dμ||_1` when the sup norm covers the pairing's support. These are mathematical statements; no new physical axiom is needed to state or investigate them. The root restriction's cost remains an estimate to prove, not a definitional impossibility.
- **N7 — Steelman against a broad closure.** A gauge-invariant quantity can admit a much better estimate in a chosen representative. The explicit TV improvement already falsifies exact optimality, and the finite cochain witness has nonzero residue but zero P. A real counter-route must now control the actual Y^p and compatible source charges in a useful norm, retaining all residual terms and root constraints. The price gate cannot reject that route because its ratio is fixed regardless of whether P is large, small, or zero. This does not defeat the narrow conservation theorem; it defeats using that theorem as an analytic obstruction certificate.
- **N8 — Cross-cycle evidence.** NOT-VERIFIED under the explicit two-extra-file/read prohibition. No snapshot, audit ledger, or other campaign record was consulted, and no prior verdict is used as evidence.

## Summary table

| Finding | Review verdict | Claim disposition |
|---|---|---|
| F1 root-delta definition/sign | REFUTED | Correct amplitude +sΦ; written negative amplitude doubles Φ. |
| F2 free level-0 Hodge operator | CONFIRMED | PROVEN free-complex statement, no background field. |
| F3 Ω≤3 | REFUTED | Ω=3+2/(e^(λR)−1)>3 at every finite positive λR. |
| F4 explicit R-uniform constants | NOT-VERIFIED; certification claim REFUTED | GAP; 54/1703/429/27250 are not disproved numerically. |
| F5 borderline summability | CONFIRMED | PROVEN logarithmic majorant divergence; no uniform infinity-operator bound follows. Actual-response irreducibility remains OPEN. |
| F6 exact admissible price / broad obstruction | CONFIRMED / REFUTED implication | PROVEN conditional price identity; GAP in size/no-useful-representative inference. |
| F7 excluded μ and saving factor | CONFIRMED narrow exclusion / REFUTED factor | Correct factor q−1; zero-price excluded construction exists. |
| F8 exact TV optimality | REFUTED | PROVEN admissible counterexample; exact global optimum OPEN. |
| F9 cell geometry / GT-5 | REFUTED geometric steps / CONFIRMED lemma | GT-5 repaired with 9+c_m; GT-4 quantitative tail remains GAP. |
| F10 coefficient/core/metric counts | REFUTED | q_i factor 3/2 correction; radius-52 count 5,071,041; saturation through 51; metric factor 64. |
| F11 reported torus price equality | REFUTED | Correct conditional S_T≈2.38158·10^8; gain≈1.17435·10^20; comparison≈32.34865. |
| F12 full admissible-family transfer | NOT-VERIFIED | GAP; harmonic correction and general-Y/locality transfer unresolved. |
| F13 price-gate independence | REFUTED | Adjoint consistency, not an independent analytic obstruction test. Positive gauge identities PROVEN. |
| F14 residual “can only worsen” claim | NOT-VERIFIED; general sign inference REFUTED | GAP; for the matching chain-defect definition Δr=0. |

**Disposition:** retain the free Hodge algebra, the repaired GT-5, the moment generating-function algebra, the constructive gauge identities, and the narrowly quantified price identity. Neither target's headline PROVEN status is justified at its advertised full strength. The nontrivial-background problem is untouched; the actual analytic size problem stays OPEN.

**Single most dangerous unverified step:** `GREENT.md:366-373,695-699` — that the harmonic-completed, root-corrected Coulomb construction yields **one admissible family retaining both a uniform general-Y sup bound and the claimed column decay**. Without that transfer, even a valid free-kernel estimate and correct profile arithmetic do not reach the consumer theorem.

## Source binding and execution record

Current source sizes at end of derivation: GREENT 699 lines; TGAUGE_PRICE 679 lines. SHA-256 (no git used):

```text
GREENT.md          ed0a71f970c813fe154ac9a7fa6232b6ebd0ebf6848682a4f4c620ae6a7a1a55
TGAUGE_PRICE.md    6eb44fbceecd6d839ab67b5cbce05727b8a32ef518851db3caea6194678f67ed
gt1_const.py       8bf77d5706c6adea6b155e3c5987ffc026a465c183b6d49f5c648885ab0f198f
gt1_price.py       d7b73309e34a496bbde4f1b5436e77143aa593aa828d8a05ecd1c7689925ee36
tg1_price.py       9ab48bcd2bafb7e8e2cacad8db44ed5efae6ce402b286dc7a9aad60bbaa3780f
```

Only this deliverable was written. No git, background workers, numerical quadrature, BLAS, or numpy. No claim is made about the author's actual model identity from source labels alone. The review used separate algebra, explicit counterexamples, and exact rational enclosures.

## STDOUT SUMMARY

CONFIRMED: free level-0 operator; logarithmic majorant divergence; repaired GT-5; narrow admissible price identity.
REFUTED: sign/count/coefficient errors, exact TV optimality, purported price-gate independence, and the broad obstruction inference.
NOT-VERIFIED: 54/1703/429/27250 as universal bounds; corrected-family transfer; actual response obstruction and residual claim.
NUMERIC CORRECTIONS: root amplitude −sΦ→+sΦ (written new Φ=2Φ, not 0); Ω≤3→Ω=3+2/(e^(λR)−1)>3; price saving q→q−1 (81→80,729→728,6561→6560); exact point/flat factors 9→656/73 and 3→1640/547; claimed flat optimum 1641/205 is beaten by 8 (TV 44307/205→216); code q_i→(3/2)code q_i=16/(65+c_m); core 8.2·10^7→5,071,041 for radius 52, with full saturation only through 51 giving 4,695,809; d^(d−1) 256→64; actual torus S_T 2.51355·10^8→[238,157,768.21,238,157,769.36], conditional gain 1.113·10^20→1.17435·10^20 and comparison 34.14→[32.348654,32.348655]. Counterexample distances are 2 rather than claimed ≥3, and 3 rather than claimed ≥6. Claimed 10 random forms→3 executed in the scripts. For 𝒯=0, ρ=1→undefined (0/0); for arbitrary non-eliminating μ, ρ need not equal 1.
MOST DANGEROUS UNVERIFIED: one admissible Coulomb family retaining both claimed estimates after harmonic and root corrections.
