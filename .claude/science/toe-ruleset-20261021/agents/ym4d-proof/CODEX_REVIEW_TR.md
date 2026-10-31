## PRE-STATED

Recorded before reading the target proof or its checks: **2026-10-28 23:39:42 UTC** (UTC clock tool). Prior exposure: the user's target description, including the proposed transport estimate and the two advertised figures; no target proof or check output read yet.

Target: `KFACTOR_O55.md`, Lemma TR (§4), and only the dependencies needed to assess its critical-point curvature SUP conclusion. Here and below paths without a prefix are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.

Pre-stated refutation criteria:

1. An exact stationarity calculation showing that the asserted linear source identification omits or mis-signs a nonzero nonlinear term refutes that identification. A missing derivation alone gives NOT-VERIFIED.
2. An admissible exact chain/source/critical-point example violating TR-1 or its claimed uniform quantifiers refutes TR-1. A hypothesis of RT-cc (c) or TC not established for the proposed source gives NOT-VERIFIED for the deduction; incompatible hypotheses refute the stated application, without automatically disproving every possible transport theorem.
3. A rational exact coefficient calculation contradicting the claimed powers, row bound, level-sum estimate, threshold, or gate result refutes the corresponding assertion. A finite passing computation cannot prove the infinite-level theorem.
4. Any dependence on the number of levels hidden in the source norm, smallness requirement, transport constant, or row estimate prevents confirmation of uniformity. Failure of this proof route is not by itself a counterexample to the desired Yang–Mills result.
5. The check must distinguish testing algebra conditional on TR-1 from testing the actual critical-point transport gate. A mislabeled or vacuous gate does not establish TR-1.

Verdict vocabulary: **CONFIRMED** for the precise checked assertion, **NOT-VERIFIED** for a remaining proof/hypothesis gap, **REFUTED** for an explicit contradiction or counterexample. Each substantive verdict will name a file and locating string. Arithmetic will use integers and exact rational numbers only; symbolic identities and inequalities will be stated with their hypotheses. Off-critical contraction is outside the proven target and will not be promoted.

Operating scope: no git commands; only this report may be written. This is an independent source review, not an audit-status change. A banked lane label will not substitute for reading the lemma and checking its application.

## Disposition

**CONFIRMED: the transport mechanism and its uniform summation, conditional on the stated bounds for the actual source. NOT-VERIFIED: the advertised exact nonlinear critical-point corollary as a consequence of only the banked, proved inputs.** There is no exponent error in TR-1. The unresolved bridge is that Step 0 uses the **full** nonlinear remainder, whereas the bounds substituted in Step 1, and the list of plain currents summed in §4-A, have been established only at second order. The author discloses that higher orders remain ARGUED; that qualification must stay in the theorem and in downstream status claims, not disappear behind “PROVEN as an implication of reviewed source lemmas.” No counterexample to the full nonlinear transport estimate is established here.

| Target and location | Verdict | Exact scope |
|---|---|---|
| `KFACTOR_O55.md`, `Step 0 (criticality is a linear identity` | **CONFIRMED** | Exact for the full source `S*=𝔑^0(x*;B)`, held fixed when varying the linear energy; composite co-closedness only |
| `BFT_B.md`, `29.1 Lemma RT-cc`, `19.2 Lemma TC`, `29.2 Lemma FT` | **CONFIRMED** | These give the displayed transport estimate for an exact admissible source; no individual-current co-closedness, smallness, SPD, W2, SB, or GI is required by these linear steps |
| `KFACTOR_O55.md`, `A-priori sizes on the 𝔐^∇-ball` | **NOT-VERIFIED** for the full nonlinear source | The quoted BA-6/CR-1 bounds cover the quadratic slots. The omitted higher-order slots are not bounded by this proof |
| `KFACTOR_O55.md`, `(TR-2)`, `(TR-3)`, `(TR-4)`, `Step 4 (optional; removes the factor m)` | **CONFIRMED conditionally** | Correct consequences of TR-1 and the stated row/source decomposition; local completion bounds retain their no-wrap proviso |
| `KFACTOR_O55.md`, `Corollary COF-crit♯♯` | **CONFIRMED as an explicitly conditional implication; NOT-VERIFIED as full nonlinear closure** | C2-COF consumes the sum of **all** plain currents. Summing only the BCH₂ currents does not price unproved higher-order currents |
| `checks/kf55_1_criteria.md`, `Part B checks ONLY the algebra`; `checks/kf55_1.py`, `B1`, `B2` | **CONFIRMED** | Honest algebra-only scope; reproduced exact verdicts. The gates can fail, but cannot certify the source identification or source estimates |
| `REVIEW_BFT_B_S9_S10.md`, `S10-6`, `optimal θ` | **REFUTED** as an admissible optimizer for all depths | The advertised `θ*=1/((k−1)ln 3)` is below `α=1/4` for every `k≥5`. The direct old aggregate upper bound has coefficient `(121/13)(k−1)` |

Review uses the amended target, including §4-A's withdrawal of CC-0 and its final erratum **`A_j=C_f(A_B+A_W)`**. The earlier `C_f max(A_B,A_W)` is not used. The requested off-critical reduction and Remark TOP-crit are not graded as proven.

## 1. Attack on TR-1: the exact identity survives

Sources: `BFT_A.md`, `7.1 Setting LIN`, `26.0` locating `H := the Hessian of E_src's quadratic part`, `31.0 Definitions` locating `Ungauged remainder`, and `28.9 Lemma FG`; `KFACTOR_O55.md`, `Step 0` and `§4-A`.

Let `E_0(x;B)` be the quadratic chain energy. Its gradient is `Hx−NB`. A source in slots `(G,s,j)` represents the linear functional

    <S,u> = Σ_l [<G_l,du_l> + <j_l,u_l> + <s_l,Q_lu_l−u_(l+1)>],  u_k=0.

The affine constant contributed by `s_(k−1)` and the fixed data does not change this derivative. With the **full** definition

    𝔑^0(x;B) = Hx−NB−∇(𝔉_k∘exp)(x;B),

criticality gives `S*=Hx*−NB`. Therefore

    ∇_z E_src(z;B,S*)|_(z=x*) = Hx*−NB−S* = 0.

**CONFIRMED.** No nonlinear term is dropped in this identity. One must freeze `S*`; differentiating `𝔑^0(z;B)` inside the source functional would be a different problem. For each permitted pinned gauge direction, `HΞλ=0` and `<NB,Ξλ>=0`, so `<S*,Ξλ>=0` without GI. This says that the source annihilates the allowed gauge space. It does **not** say that its divergence vanishes at the level-k roots. The amendment withdrawing CC-0 is necessary and sufficient for this part of the repair.

There is a minor signed-decomposition error in the same paragraph. `BFT_A.md`, `3.6 BA-6` and `12.0 Fixed parameters and definitions`, define `κρ^(2)`, `s^C`, and `R^B` as contributions to the **positive nonlinear gradient**. With §31.0's convention they enter `𝔑^0` with the common opposite sign. Thus the literal `s_l = ...; j_l = R^B_l` slot equality in `KFACTOR_O55.md`, `Slots of S*`, is **REFUTED as a signed equality** and should be read with that sign correction. Every norm estimate below is unchanged. This does not refute the exact critical-point identification.

## 2. RT-cc, TC and FT really give the extra power

Sources: `BFT_B.md`, `27.1 Definitions used below`, `27.2` locating `Lemma RT-cc`, `29.1 Lemma RT-cc`, `29.2 Lemma FT`, and `19.2 Lemma TC`; `BFT_A.md`, `8.2 BL-2`; independently corroborated by `REVIEW_BFT_B_S6.md`, `B.2 Lemma TC`.

Write `ρ_l=κ_l r_l−s_l`. The exact Euler–Lagrange equations, for `1≤l≤k−1`, are

    ρ_(l−1) = Q_l^Tρ_l−d*G_l−j_l.

Taking divergence, starting with the level-0 equation, determines `ψ_l=d*ρ_l` from the raw divergences of the plain currents. Substitution of

    Q_l^T = Q_str,l^T−h_l^T d*,    ĵ_l=j_l+h_l^Tψ_l

gives the straight recursion before any iteration. Consequently RT-cc(c) holds for non-co-closed `ĵ_l`. There is no attempt to replace `Q^T` by `Q_str^T` on an arbitrary current without paying the funnel term.

The terminal residual slot does contribute to the full, unpinned root divergence: `D(S)=D_j+ev_k^T d*s_(k−1)`, as corrected in `CODEX_REVIEW_C2.md`, `4. Whole-class CO-fun`. It vanishes on pinned tests. RT-cc(c) follows directly from the displayed stationarity equations and uses `ψ_l=d*ρ_l`; it does not need the incorrect stronger identification `D(S)=D_j` as full functions. Thus that inherited notation defect does not break the transport argument.

For a straight block average of side `s`, its transpose at a fine link is a sum of exactly `s` current values with coefficient `s^(−4)`. It has ℓ∞ norm `s^(−3)` in own units, for **any** current. Periodic identifications may merge entries; they do not change their total nonnegative weight. Setting `s=L^m` and converting a level-(i+1) 1-form to coarse units multiplies by `L^m`, hence

    L^m L^(−3m) = L^(−2m).

For an intermediate level-l plain current, the same calculation is

    L^m L^(−3(l−i−1)) L^(−3(k−l)) π_l(ĵ_l)
      = L^(−2m) π_l(ĵ_l),       m=k−1−i.

This is the extra power relative to the `L^(−m)` residual bound in the original ball. It is a transpose-column count and a units conversion, not a claim about forward push-up of BCH rows. **CONFIRMED**, without SPD or W2.

FT(ii) uses only the root cascade and `||h_l^T||_(∞→∞)≤1`:

    π_l(ĵ_l) ≤ π_l(j_l)+2d Σ_(a=0)^l L^(−3(l−a))π_a(j_a).

If the actual source has `G_l=0` for `l≥1`,

    ||s_i^c|| ≤ A_s L^(−2m)η²,
    π_l(j_l) ≤ A_Bη² (l≥1),    π_0(j_0) ≤ (A_B+A_W)η²,

then `π_l(ĵ_l)≤A_jη²` with the **corrected** `A_j=C_f(A_B+A_W)`, `C_f=1+2d/(1−L^(−3))`. The norm of the top residual is at most `η`; therefore

    ||ρ_(k−1)|| ≤ κ_+η+A_sη²,
    ||r_i^c|| ≤ κ_-^(−1)L^(−2m)η[κ_++(2A_s+mA_j)η].

This proves TR-1 **under those actual-source hypotheses**. There are exactly `m` positive-level terms above `i`. FT(ii) requires neither a k-uniform Pc norm nor the later conclusion TR-3; there is no circularity in this use of the source class.

The linear lemmas impose no small-field condition. Smallness enters only through the nonlinear slot estimates: the fixed logarithm/polar neighborhood must be respected. `BFT_A.md`, `3.3` locating `in particular for η ≤ 1/(20p_L)`, supplies a k-independent sufficient contour threshold. Its CR-1 size proof also explicitly says `take η ≥ ||B_k||_D`; carry this data convention when quoting its precise `A_s`, or enlarge constants to accommodate `||B_k||_D≤C_Dη`. A k-independent such `C_D` follows from `B_k=Qx_(k−1)−r_(k−1)` and the fixed-length contour bound. None of these steps requires `mη` or `kη` to be small.

## 3. The unproved source hypothesis is material

Sources: `KFACTOR_O55.md`, `Constants, all from the source at second order`, `Slots of S*`, `A-priori sizes`, `Scope, stated plainly`, and `Corollary COF-crit♯♯`; `BFT_A.md`, `31.0` locating `the rows ... are its second-order part`, `3.6 BA-6`, `13.5 Lemma CR-1`, and the `third order` row of §3.9. The targeted later-source search still finds the third-order remainder listed as ARGUED in `BFT_B.md`, the conclusion preceding §31 and the remaining-items list near §33.

The exact source identity in §1 concerns `S_full=𝔑^0(x*;B)`. The cited inequalities bound `S_2`, its quadratic part, and the target itself writes `(+ higher order)` in the slot decomposition. In general

    S_full = S_2+ΔS,
    ∇E_src(x*;B,S_2) = ΔS,

not zero. In particular, the quadratic slots need not separately form a composite-co-closed source at a full nonlinear critical point. Applying RT-cc to the full source and then dropping `ΔS` from its size estimate does not become exact by saying “second order only.” Applying it to `S_2` instead loses the stationarity hypothesis.

An exact scalar illustration of this logical distinction, **not a Yang–Mills counterexample**, is

    F(x)=(x−a)²/2+x³/3+x⁴/4,
    t=1/100,    a=t+t²+t³.

Here `F'(t)=0`, the full source is `−t²−t³`, and the linear gradient with the truncated source `−t²` is `−t³=−1/1000000`. The same distinction applies to the full-source/truncated-source inference, irrespective of how small the omitted term is.

More explicitly, let the omitted slots be `(δG,δs,δj)`. The transport estimate has the additional nonnegative error budget `κ_-^(−1)E_i`, where

    E_i = ||δs_i^c||
      + L^(−2m) {||δs_(k−1)^c||
        + Σ_(l=i+1)^(k−1) [π_l(δj_l)
          + 2d Σ_(a=0)^l L^(−3(l−a))π_a(δj_a)
          + 6L^(k−l)||δG_l^c||]}.

This follows from the **full** cascade and triangle inequalities; it does not assume `ΔS` is independently admissible. The target does not bound this budget. Moreover, for the downstream C2-COF application, one must also price `Σ_lπ_l(δj_l)`. Even an `O(η³)` bound per level alone gives `O(kη³)`, which is not uniform at fixed `η`.

One sufficient repair would be an exact decomposition with no positive-level divergence slots, a uniform bound `||δs_i^c||≤C_s^(3)L^(−2m)η³`, and `Σ_lπ_l(δj_l)≤C_j^(3)η³`, together with the level-0 divergence-form bound. Enlarging `A_s,A_j` by fixed multiples of `η_0` would then give the asserted qualitative estimates and the full summable source. This is a sufficient missing estimate, not an assertion that it has been proved or that it is necessary in this particular form.

**NOT-VERIFIED:** full nonlinear TR-1 with the displayed second-order constants, and unconditional full nonlinear removal of the level factor. **CONFIRMED:** the conditional implication once the actual-source estimates above are supplied. No new physical axiom is involved; the missing work is a local nonlinear estimate with the required level dependence.

## 4. Summation and the BCH₂ row conversion are sound

Sources: `KFACTOR_O55.md`, `(★)`, `Step 2`, `Step 3`, `Step 4`; `BFT_A.md`, `12.0` locating `⟨R^B_l, u_l⟩`, and `28.12 Corollary NC`; `BFT_B.md`, `19.4 Corollary RH-inv` and `29.4` locating `Sizes`.

The defining row is linear in the **linear** residual, even at a nonlinear configuration:

    <R^B_l,u_l> = 2κ_l Σ_c <r_l(x)(c),B_c(x_l,u_l)>.

In the notation of the target, its local operator bound gives

    π_l(R^B_l) ≤ c_Bκ_+ L^(3(m+1)) L^(−(m+1))η L^(−m)||r_l^c||
               = c_Bκ_+ L^(m+2)η||r_l^c||.

Substitution of TR-1 produces TR-2 exactly. The old residual bound supplies the first argument `1` in the minimum. For `l=k−1`, where TR-1 was not asserted, the old bound supplies `a_0=1`; the proposed second bound is larger since `κ̂≥1`. Thus including `m=0` in TR-3/TR-4 is legitimate. The case `k=1` has no positive-level sum.

The completion estimate should be applied to the **local pieces** `R_c`, as its proof does. TR-1 controls every `r_l(c)`, so it improves every piece by the same level factor, and the bounded-overlap construction transmits that factor to `V_l`. A generic bound for the norm of a sum of cancelling pieces would not alone justify an inequality for their separately constructed completions. Here the piecewise proof is available, with a fixed local constant. Keep Corollary NC's no-wrap proviso for `V`; the transport and raw-row estimates themselves do not require it. The C2 route can use whole raw rows and does not require this split.

Put `a=1+2A_sη/κ_+`, `b=A_jη/κ_+`. The potentially troublesome corrections are exactly summable:

    Σ_(m≥0) L^(−2m) = L²/(L²−1),
    Σ_(m≥0) m L^(−2m) = L²/(L²−1)²,
    Σ_(m≥0) L^(−m) = L/(L−1),
    Σ_(m≥0) m L^(−m) = L/(L−1)².

At `L=3` these are respectively `9/8`, `9/64`, `3/2`, `3/4`. Hence the polynomial correction in TR-1 cannot restore a level-count loss. For fixed `0<θ<1`,

    sup_(m≥0) L^(−(1−θ)m)(a+bm)
      ≤ a + b/[e(1−θ)ln L],

because the continuous maximum of `t exp(−ct)` is `1/(ec)` for `c>0`. This confirms the displayed `K_Pc`. Alternatively, with `q=L^θ`, the elementary geometric-series bound `sup_m m(q/L)^m≤(q/L)/(1−q/L)²` avoids transcendental constants entirely. Replace `η` by `η_0` in all coefficient bounds to obtain constants fixed for the whole ball. Constants may diverge as `θ→1`; uniformity in **θ** is not asserted or proved.

Thus TR-3 and TR-4 are **CONFIRMED conditional consequences** of TR-1. Before the feedback step, the bound is `L^(−m)(a+bm)η²`; it is not literally a pure `L^(−m)` bound with an m-independent coefficient. Step 4 removes that distinction under the stated exact row decomposition: FT's nonnegative convolution satisfies

    Σ_lπ_l(ĵ_l) ≤ C_f Σ_lπ_l(j_l).

Sum the already obtained BCH₂ bounds and add the level-0 Wilson term; the right side is k-independent. Feed it back into RT-cc to obtain

    ||r_i^c|| ≤ κ_-^(−1)L^(−2m)η(κ_++c'η),
    π_l(R^B_l) ≤ A_Bκ̂ L^(−m)(1+c'η/κ_+)η²,

with `c'` independent of `m,k,T`. This bootstrap needs no absorption or smallness of `kη`. It also needs all currents in the source sum to have been priced; §3 explains why omitted higher orders cannot silently be included.

## 5. What C2-COF does and does not close

Sources: `KFACTOR_O55.md`, `§4-A`, `Corollary COF-crit♯♯`, `Remark TOP-crit`; `CODEX_REVIEW_C2.md`, `4. Whole-class CO-fun` locating `(C2-COF)`, and `Exactly what may be banked`; `BFT_A.md`, `28.6 Corollary WR`.

The amended response is correctly defined:

    x_rows=x*−x(B_k),    Hx_rows=S*,    (x_rows)_k=0,

where `x(B_k)` solves the source-free linear chain with the same data. **CONFIRMED.** C2-COF bounds its curvature, not the entire critical field's data contribution. Adding the latter generally adds a linear-in-data term; it cannot simply be called `O(η²)`.

Treating the named lane-A inputs of C2-COF as supplied conditional inputs, its sup bound is `||f_0(x_rows)||∞≤C N(S*)`, with

    N(S*)=||G_0^c||∞+[G_0^c]_α+||G||_Y+||s||_R+Σ_lπ_l(j_l).

No CC-0 assumption or top-response term is needed in this **sup** bound. With actual-source TR and the full slot estimates, it yields the desired uniform sup conclusion without SPD/W2/SB/GI. Its Hölder estimate still has `κ_+||r_(k−1)^c(x_rows)||∞`; that term is retained here. TOP-crit and the off-critical contraction remain unproved by this review.

The author's citation to §3.9 leaves Wilson Hölder regularity labelled ARGUED, but there is a later proof: `BFT_A.md`, `28.6 Corollary WR (a)`, writes the plaquette correction as an analytic map `Φ` with `DΦ(0)=0`. Translating the four links and using the ball's gradient bound gives

    |q^c(p)−q^c(p')| ≤ 4C_qη²δ ≤ 4C_qη²δ^α,

for coarse separation `δ≤1`. Thus `[q^c]_α≤4C_qη²` in the fixed analytic neighborhood. **CONFIRMED:** this particular missing-looking input is available in the cited lane. It is not the reason for withholding nonlinear closure.

The remaining issue is `S*`'s full soft remainder and full plain-current sum. C2-COF is a linear source theorem; it cannot supply those nonlinear bounds. Consequently §4-A is a valid composition **conditional on them**, and not a proof that they follow from the quadratic rows alone.

## 6. Exact checks, discrimination, and the old figure

Sources: `checks/kf55_1.py`, `checks/kf55_1_criteria.md`, `checks/kf55_1_out.txt`, `checks/kf55_1_err.txt`; `KFACTOR_O55.md`, `§7. Check record`; `REVIEW_BFT_B_S9_S10.md`, `S10-6`.

### Reproduction and independent checks

The checker was executed in memory with all expression statements calling `say(...)` suppressed by an AST transformation. Those are display statements, including all floating-point approximations. The verdict expressions, parameter grid, loops and constants were left unchanged. No output file or bytecode was written. Results actually returned:

    A1=True, A2=True, B1=True, B2=True, B3=True, B4=True, overall=True
    Cf=121/13
    minimum old/new class ratio >= 2*10^49: True
    minimum old/new sum ratio >= 75: True
    B2 failure: None

The archived checker uses floats only for display; its verdicts use exact integers/Fractions. Its printed identical rounded endpoints are not exact singleton enclosures. This review did not use those decimal displays as evidence.

Independent integer/Fraction checks, rather than the author's expression on both sides, gave:

- A direct transpose-column enumeration for block sides `s∈{3,9,27,81}`, coarse tori `T∈{1,2,3}`, and every longitudinal offset: **720 cases passed**, row sum exactly `s^(−3)` and coarse sum exactly `s^(−2)`. Arbitrary signed currents also obeyed the bound. This is a finite check of the kernel count; the proof in §2 supplies all depths.
- Exact maxima of `m(q/3)^m`: for `q=4/3`, maximum `4/9` at `m=1`; for `q=2`, maximum `8/9` at `m=2,3`; for `q=5/2`, maximum `15625/7776` at `m=5,6`. The ratio `q(m+1)/(3m)` decreases with `m≥1`, proving that no later maximum was missed.
- `C_f=121/13` exactly, and a factorial series through order 12 with tail at most `2/13!` gives `253/10 < 121e/13 < 2531/100`.
- The all-depth optimizer-window test follows from rational bounds on `ln 3`, given below.

### Can the gates fail?

**CONFIRMED:** they can fail on the algebra they actually test. In-memory mutations used the restricted grid `κ_+=1`, `η=1/100`, `A_s=A_j=1`, `L^θ=2`, `KMAX=4`; only B1/B2 were judged in these controls. Actual results:

| In-memory variant | B1 | B2 |
|---|---|---|
| Restricted baseline | True | True |
| Change only `P`'s exponent from `m+2` to `m+3` | False | True |
| Change only `BS`'s factor `L/(L−1)` to `1` | True | False |
| Change transport from `L^(−2m)` to `L^(−m)` and change the compared row factor from `L^(−m)` to `1` | True | True |

The first mutant fails already at `m=1` by a factor of `3`. For the second, at `k=4` the exact sum is `1313/900`, exceeding the mutated bound `411/400`. The matched corruption survives because B1 compares two formulas that share the asserted transport, while B2 separately builds its own `a_m`; the script never solves a chain or checks a nonlinear critical point. This is a limitation explicitly disclosed by the author, not concealed evidence of TR-1.

One further scope distinction: B2 uses the **discrete** maximum `M` on its rational parameter choices. It does not execute the target's exact displayed formula `1/[e(1−θ)ln L]` for `K_Pc`. That latter inequality is justified by the elementary proof in §4, not by calling B2 an independent test of it. No finite sweep establishes uniformity in arbitrary k; the geometric-series argument does.

### The advertised optimizer and the honest old bound

From `ln 3=2 Σ_(j≥0) (1/2)^(2j+1)/(2j+1)`, the first two terms give `ln 3>13/12`; bounding every remaining denominator by 3 gives `ln 3<10/9`. In particular

    1 < ln 3 < 4/3,
    3 ln 3 < 4 < 4 ln 3.

Therefore the advertised `θ*=1/((k−1)ln 3)` lies above `1/4` for `2≤k≤4` and below `1/4` for **every** `k≥5`, not merely up to the checker's `10000`. For `k=2` it is also below 1. This is an exact proof using rational bounds.

**REFUTED:** S10-6's use of that advertised optimum as an admissible choice in the fixed window `1/4<θ<1` for all k. **CONFIRMED:** `121e/13` is the leading coefficient of its stated approximate unconstrained optimization. Neither file's approximate objective should be relabelled the exact finite-k optimizer of COF's full constant.

The direct old route bypasses the weighted maximum. If each of `k−1` positive-level currents is bounded by `Mη²`, then FT gives

    Σ_lπ_l(ĵ_l) ≤ (121/13)(k−1)Mη²

for that positive-level collection, with the level-0 contribution added separately. This is the honest **upper-bound coefficient** before the transport repair. It is neither an attained nonlinear lower bound nor a proof that the physical response grows with k. “Only given SPD” is not an established necessity theorem; the conditional transport mechanism provides a different sufficient route.

## Source identity and execution record

Review completed: **2026-10-28 23:51:15 UTC** (UTC clock tool). Final checks found the target, checker script, and C2 input hashes unchanged from the receipts below.

No git commands, source changes, worker launches, audit-status changes, or writes outside this report. Large BFT files were inspected by `rg` and bounded `sed` ranges. The review is of this local candidate, not a verified origin/main snapshot. SHA-256 receipts for the target and checker packet:

    KFACTOR_O55.md
      24ff96d127a4298805377fd450d1905729064f8599385e2b41e508f206ce6881
    checks/kf55_1.py
      a145a88745e5474d48e394acc87448f1571d114563032baceacc832f185b5a09
    checks/kf55_1_criteria.md
      e5aed95affed95a0a9464f4227bd51fe3b2480680a02b5fc1c6cc5f7481b4851
    checks/kf55_1_out.txt
      91e49c1a345d193ca9e99bfe44cb436e7ea17396618f2499272a4ba13367af3f
    checks/kf55_1_err.txt (empty)
      e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    CODEX_REVIEW_C2.md
      36180292c9324dfd526404e91b76ef1ee9651db27e91cfabab4a418ded6dcddb

## Exactly what may be banked

1. **CONFIRMED — exact conditional transport theorem.** At the trivial linear background, weight parameter zero, fixed `d=4`, odd `L≥3`, and `0<κ_-≤κ_l≤κ_+`, let `x` be an actual critical point of `E_src` with `||x||_𝔐≤η`. If its **actual** source has `G_l=0` for `l≥1` and the residual/plain slot bounds stated in §2, then TR-1 holds with `A_j=C_f(A_B+A_W)`. This is uniform in k and T and uses no SPD/W2/SB/GI. A nonlinear critical point with its full `𝔑^0` satisfies the exact linear stationarity and composite-co-closedness hypotheses; the source size hypotheses remain separately required.

2. **CONFIRMED — conditional BCH₂ decay and aggregation.** TR-1 and the local BCH₂ bilinear bound imply TR-2, Pc boundedness for each fixed `0<θ<1`, and a k-independent level sum. Local completions inherit these conclusions on their stated no-wrap domain. If the **full** positive-level plain source consists of those rows (or has separately summable additional terms), the feedback step gives pure `L^(−(k−1−l))η²` decay with a fixed coefficient.

3. **CONFIRMED — a strictly perturbative version without discarding an exact remainder.** Along any twice differentiable family of exact critical points through the trivial chain, write `x(t)=t x_1+O(t²)`, `B(t)=tB_1+O(t²)`, with `||x_1||_𝔐≤1` and the corresponding small-data convention. Differentiated stationarity gives `Hx_1=NB_1`. Source-free transport then gives `||r_l^c(x_1)||≤κ̂L^(−2m)`. The quadratic Taylor coefficient `R^B_l(x_1)` therefore obeys `π_l≤A_Bκ̂L^(−m)`, and its level sum is at most `A_Bκ̂ L/(L−1)`. This banks the quadratic coefficient, conditional on such a family; it is not an exact finite-field theorem or a construction of that family.

4. **CONFIRMED — the conditional C2-COF consequence.** With the named C2-COF lane-A inputs and full-source bounds `||G_0^c||+[G_0^c]_α+||G||_Y+||s||_R+Σ_lπ_l(j_l)≤Cη²`, bank `||f_0(x*−x(B_k))||∞≤C'η²`, k- and T-uniformly. Keep the top-response term in the Hölder estimate. The Wilson regularity input is available in BFT_A §28.6(a).

5. **NOT-VERIFIED — promotion to full nonlinear COF-crit/NCE(i) from the present packet alone.** Retain the higher-order exact-source obligation. Do not mark “the k-factor is removed at every nonlinear critical point” as proved solely by the quadratic source lemmas and `kf55_1`. Do not promote the off-critical contraction or TOP-crit. This review supplies no counterexample to a completed nonlinear repair and no necessity claim for SPD/W2.

6. **CONFIRMED/REFUTED — numerical bookkeeping in its exact scope.** Bank the algebra-only reproduction and its disclosed limitations; bank `C_f=121/13`, the direct pre-repair coefficient `(121/13)(k−1)`, and the all-k optimizer-window threshold. Withdraw the advertised `θ*` as an admissible optimizer for `k≥5` at `α=1/4`.
