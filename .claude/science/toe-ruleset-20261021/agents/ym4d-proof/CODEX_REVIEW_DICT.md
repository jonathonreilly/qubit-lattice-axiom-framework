# Independent hostile review of DICT55

## PRE-STATED — 2026-10-29T05:53:41Z

This section was written before reading DICT55 or deriving its claims. Target: `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/DICT55.md` and the specifically authorized supporting sources. The sole writable deliverable is this file. No git commands, snapshots, audit ledgers, full PROOF.md read, numerical approximation, or long jobs will be used.

The review will attempt to falsify:

1. The identification and separation of the four energy towers, including BR/CB symbol substitutions and the limited jet agreement between HIST and FLOW.
2. The normalization map for stiffness, energy, and differentiated coordinates. Refutation means an explicit configuration or symbolic derivative with a different factor or order of agreement.
3. Gauge composition, contour location, coupling, metric/norm, slice, and data-class conventions. Refutation means an algebraic counterexample or a missing hypothesis necessary to transport a result.
4. The 44 linear-input classifications and the 29 flag restatements. A banked or re-derived label fails if its supporting statement has a different domain, unresolved premise, wrong constant, or inadequate recorded independent derivation.
5. The two reported refutations and FL7's domain restriction, including downstream consequences for `[S26-BANKED]` statements.
6. The discriminating power of dc55_1 and dc55_2. String presence alone cannot establish semantic agreement; a self-referential or vacuous gate cannot establish the claimed scientific property.

Method: locate claims by strings, record actual current file:line anchors, read bounded ranges, and reconstruct load-bearing mathematics using algebra and (if useful) exact plain-Python arithmetic. A live line reference will not be inferred from an old cited number. Symbol names will be qualified by file and meaning before comparisons. Every gate will be tested against a possible failing case and its actual quantifiers.

Finding verdicts: **CONFIRMED**, **NOT-VERIFIED**, **REFUTED**. Claim statuses: **PROVEN**, **ARGUED**, **CONDITIONAL**, **GAP**, **OPEN**. CONFIRMED applies only to the exact limited proposition reconstructed here, never automatically to its dependencies or an entire proof. Existing author/reviewer labels are evidence to examine, not proof.

Planned end product: incremental findings; a summary table; exactly scoped banking recommendations and corrected restatements for the inspected `[S26-BANKED]` lines. Unread or unreconstructed dependencies will be identified explicitly.

## Findings (appended as established)

### D1 — CONFIRMED: the algebraic normalization map, with a necessary scope boundary

**Anchors:** DICT55.md:308 (`O4. The composite functional`), :320 (`NM2 (values)`), :323 (`NM3 (coordinates and jets)`); PROOF.md:2556 (`E_NA := S_W(U)`), :3242 (`Norms are Hilbert-Schmidt`), :6684 (`𝔉_k(U_0`); HIST.md:835–838 (`𝓔_0 :=`, `E(chain) :=`); FLOW.md:27 (`orthonormal for`).

Reconstruction: write `s(U)=1−Re tr(U)/N`, `S_W=NΣs`, and `φ̂=Nφ`. For **uniform** `κ_j=κ`,

`𝔉_k = N[Σs + κΣφ] = N E_HIST(chain)`.

Multiplication by positive N preserves the set of global minimizers and, wherever differentiable, the critical-point equations. The E_NA display instead puts its stiffness next to φ, so at g=1 it matches precisely when `κ_i(E_NA)=N κ_j(𝔉)`. With an HS-orthonormal basis e_a, FLOW's basis is t_a=√N e_a. Thus y=√N B, and if f(B)=F(√N B)/N, the chain rule gives

`D_y^n F = N^(1−n/2) D_B^n f`.

The factors for orders 2, 3, 4 are respectively 1, N^(−1/2), N^(−1); there is no extra N in κ_j. These are **PROVEN algebraic identities**. They do **not** identify the selected E^cb critical point with a global minimizer or prove β=1. NM4's β claim still needs the tree-Hessian/β result and the applicable germ identification; equality of coordinate-normalized quadratic tensors transfers a value of β already established, not its numerical value by itself. The configuration identity does not include the unequal-coupling bare chain with coefficients κu_i/u_0.

### D2 — REFUTED: the proposed blanket extension to the gauge saturation

**Anchors:** DICT55.md:870 (`Canonical reading of every banked`), :1201 (`every 𝒞_glob statement holds on its gauge saturation`); PROOF.md:18 (`NOT for every gauge representative`), :37 (`holomorphy in the complexified scaled norm only`); DICT55.md:399 (`Gauge slices and the orbit norm`), :693 (`field components depend on the slice`).

The unrestricted restatement is false for the coordinate/slice conclusions that the dictionary itself lists. Start with the identity datum, which belongs to 𝒞_glob(0). Choose a nonconstant site gauge g, taking at two adjacent sites respectively `diag(i,−i,1,…,1)` and 1. Its transformed link is `diag(i,−i,1,…,1)`, whose HS principal-log norm is π/√2, whereas the gauge-saturation parameter is still s=0. All plaquettes are still 1. Therefore a trivial-chart bound by Cs, a fixed linear-slice statement, or a polydisc about the identity cannot hold verbatim for every representative of 𝒞*_glob(s). Gauge invariance of the scalar functional does not imply invariance of these coordinates or of Ker Γ_E.

**Correction:** for each V in 𝒞*_glob(s), choose and retain a real gauge g with g·V in the small global chart. Apply the theorem in that chart; transport its solution, slice, norms and complex neighborhood together. Gauge-invariant numerical conclusions may then be transported. Independence of the chosen chart/branch on overlaps must be proved where a single global branch, value, or polymer representation is required. A chartwise existence statement is **CONDITIONAL**; the unqualified sentence proposed for the banked block must not be used. This does not supply the missing extension from global-potential smallness to curvature smallness.

### D3 — CONFIRMED limitation; NOT-VERIFIED global receipt: dc55_1 checks presence, not meaning or completeness

**Anchors:** DICT55.md:1032 (`dc55_1 (locator audit)`); checks/dc55_1_locators.py:9 (`re.findall`), :17 (`with open(tsv, "w"`), :33 (`return any(s in line for line in ls)`), :63 (`ok = not missing`); checks/dc55_1_criteria.md:25 (`A PASS shows only`).

The predicate tests a substring, with no comparison between the mathematical assertion outside the locator and the source. Changing, for example, an asserted coefficient, inequality direction, quantifier, or B/R2 status while retaining its locator leaves every test bit unchanged. This proves that a locator PASS cannot verify a dictionary entry's meaning. The author explicitly acknowledges this limited scope; it is not itself a false numerical claim about 367 matches.

There is also no nonempty-inventory or unmatched-delimiter gate: on text with no complete ⟦…⟧ pair, all failure lists are empty and C3 can be true, so the script prints PASS. An unmatched opening bracket is invisible to `findall`; its `MALFORMED` count detects only complete pairs without `: `. These are actual vacuity/completeness holes if this check is used as the dictionary-coverage gate. The synthetic suffix can reject spelling changes but cannot repair either hole.

Both check scripts print their verdict without setting a nonzero process exit status when the computed verdict is FAIL. A caller that tested only successful process exit would therefore not discriminate that failure. No such caller was inspected, so this is a conditional integration risk, not an allegation about an observed run.

I did not run this script: it writes a TSV outside the sole authorized deliverable and reads 61 source files, exceeding this review's read boundary. The historical all-367-found receipt is **NOT-VERIFIED** independently here. Script inspection and targeted source matches are the evidence used. No semantic banking credit is assigned to that receipt.

### D4 — REFUTED: LR-pot is not off the retained premise chain

**Anchors:** DICT55.md:938 (`LA15 Lemma LR-pot: stays R1, but leaves the premise set`), :963 (`A2` / `TOP♯ ← Corollary FP`), :993 (`LR-pot — off the banked chain`), :1000 (`LR-pot is not`); BFT_A.md:934 (`Lemma LR-pot`), :1123 (`13.12 Lemma LR-pot`), :1148 (`13.13 Corollary FP`), :2474 (`Top (Lemma TOPD)`).

DICT's own A2 retains `K^(σ): TOP♯ ← FP`. FP is obtained by inserting LR-pot into the invariant data/residual estimate: LR-pot gives

`max_j ‖(Px)^c_j‖ ≤ e^(20m)[775‖f_0‖ + 40‖B_k‖ + 205Σ_i‖r_i^c‖]`.

Using `Σ_i‖r_i^c‖ ≤ L/(L−1)‖x‖_inv ≤ (3/2)‖x‖_inv` gives `775+205·3/2 = 2165/2 ≤1083`, exactly FP's displayed coefficient. FP then uses Theorem W. Removing LR-pot from **EP-rec's alternative proof** does not remove it from this separate route. BFT_A's W0 top-response step also explicitly uses FP.

**Correction:** retain `LR-pot → FP → TOP♯ → K^(σ)` (and FP in the W0 route) until an alternative potential estimate is actually supplied. LR-pot's reported provenance class remains R1; its **dependency flag changes from excluded to retained**. The 15-row R1 inventory has not lost this row. A top-response norm cannot be recovered just from curvature by choosing an arbitrary gauge: adding dλ leaves curvature unchanged and can make potentials arbitrarily large. This is a real analytic dependency, not a naming issue. Its uniform estimate remains **NOT-VERIFIED** independently here.

### D5 — CONFIRMED cited-argument defect: 9 must become 144; active downstream minima NOT-VERIFIED

**Anchors:** DICT55.md:1003 (`FL29`), :1013 (`write C_q′η²`), :576 (`LA23`); BFT_A.md:121 (`s_j := max|x_j|`), :122 (`|q_p| ≤ 9s_j²`), :2497 (`By BA-3`), :2506 (`η ≤ 1/9`); PROOF.md:4309 (`s := Σ|x_i| ≤ 1/4`), :50 (`the cited BCH argument gives 144, not 9`).

The source estimate really uses **total word length** `s_word=Σ_i|x_i|`, not maximal link size s_j. Rebuild it: exponential multiplication gives `|Y−Σx_i|≤s_word²`, `|Y|≤2s_word≤1/2`; the log series then gives `|log(1+Y)−Y|≤|Y|²/(1−|Y|)≤8s_word²`. Hence `|q|≤9s_word²`. On a four-link plaquette, `s_word≤4s_j`, so the certified conclusion is

`|q_p|≤144 s_j²`, provided `4s_j≤1/4`.

Consequently the corresponding sufficient coarse bound is `|log U_p|≤L^(−2(k−j))(2η+144η²)`. The coefficient 9 in the **claimed application of that argument** is **REFUTED**; the sharper inequality with coefficient 9 as a separate mathematical statement remains **NOT-VERIFIED**, not disproved by the factor-sixteen loss.

There is a concrete auxiliary threshold calculation to update. BFT_A:2506 uses `2+9η≤3` for `η≤1/9`. With the certified replacement, the same prefactor follows from **η≤1/144**. At the old endpoint η=1/9, the new left side is **18**, not ≤3. This refutes the standalone sufficient ceiling 1/9 for the new calculation, **not necessarily the actual admissible minimum**: BA-3 also offers the conservative restriction `η≤1/(20p_L)`, which at L=3, p_L=11 is **1/220 <1/144** and already suffices. Its displayed level-dependent radius `L^(k−j)/(20p_L)` is a different quantity. No active banked radius is declared false here. Either retain an independently sufficient smaller radius, shrink the ceiling, or enlarge the downstream prefactor and propagate it. The complete effective minima remain **NOT-VERIFIED**; k,T-uniform existential statements can survive a fixed shrinkage.

LA23's R2 label must distinguish the re-derived **qualitative Hölder mechanism** from its unsupported numerical sup coefficient 9. The proof at BFT_A:2497 merely imports that sup coefficient from BA-3. A re-derived analytic/Hölder argument does not certify it.

### D6 — CONFIRMED: φ versus k̃ at configuration level; REFUTED literal normalizer repair; NOT-VERIFIED strict inequality of the minimized towers

**Anchors:** DICT55.md:258 (`O2`), :360 (`𝒯_k`), :708 (`FL4`), :775 (`FL13`), :1016 (`8.3 Precision`), :1204 (`−κu·d(M) moved into log 𝒩′`); HIST.md:880 (`Lemma HF`), :899 (`Termwise k̃ ≥ φ`), :905 (`Report to the FLOW lane`); FLOW.md:117 (`k̃(V, M) :=`), :124 (`RFL-fix`), :134 (`Def F-strip`).

For M=WP and an SU(N) maximizer W_0, direct subtraction gives

`k̃(V,M)−φ_M(V) = [tr P−Re tr(W_0^−1 M)]/N = d(M) ≥0`.

This term is independent of V but depends on the fine field. Its nonvanishing is not merely hypothetical. Let `z=(1−r²+2ir)/(1+r²)`, r>0 rational, `A=diag(z,z,z^−2)∈SU(3)`, and `M=(2I+A)/3`. Exact expansion gives

`Im det M = 4 sin(t)(1−cos(t))/27 = 16r³/[27(1+r²)²] >0`, where z=e^(it).

At r=1/2, `det M=121/225+i·32/675`; at r=1/100 it is `899940001/900180009+i·1600/2700540027`. The diagonal entries of M are nonzero; its polar factor is therefore not in SU(3). Equality in `Re tr(QP)≤tr P`, P>0, requires Q=I, so the SU(3) maximum is strictly smaller and d(M)>0. This is realizable by S4′ at L=3: for a μ-directed block pair, place A on the μ-links crossing their common boundary for one of the three transverse ν-layers, and put identity on the other links. Each straight leg crosses that boundary once; the within-block axial legs do not. Exactly one third of the y values, for every axis order, yield A. Taking r arbitrarily small keeps the field in a small chart. Embedding the construction with identity extra colors gives the same obstruction for N>3. For SU(2), a nonnegative mean has quaternion form and polar factor in SU(2) whenever invertible, so d=0.

**The necessary normalizer algebra is:** with `a=κu`, `Z_tilde=∫exp(−a k̃)dV`, `Z_phi=∫exp(−aφ)dV`,

`Z_tilde=e^(−ad) Z_phi`,

`a k̃+log Z_tilde = aφ+log Z_phi`,

`log Z_phi = log Z_tilde + ad`.

Thus the φ-based rewriting must **remove the existing −ad from log Z_tilde**, or explicitly add **+ad** when changing that normalizer to log Z_phi. DICT's instruction to replace k̃ by φ and “move −κu·d into log 𝒩′” is not a valid literal substitution: retaining the old normalizer loses ad; additionally inserting −ad loses 2ad. The corrected equations above, not the ambiguous movement instruction, should be banked. The O(u) term cancels at tree level; it must not remain as an O(1) polymer.

For the four towers retain four distinct names: per-level critical E^br; composite critical E^cb; HIST global minimum 𝓔; FLOW literal k̃ minimum 𝒯. Termwise comparison rigorously gives `𝒯≥𝓔`, and equality for SU(2). However **a nonzero d at an arbitrary chain does not prove strict inequality after minimization**. For compact finite chains, equality of the minima holds exactly when some φ-minimizer has d=0 on every soft term: this follows by evaluating a k̃-minimizer and using both nonnegative differences. No inspected source constructs a coarse datum ruling out all such φ-minimizers. DICT's assertion that the minimized functions “differ off it” for N≥3 is therefore **NOT-VERIFIED** here; the inspected HIST consequence gives inequalities, not a strictness witness for minimized values. Keeping separate definitions is essential regardless.

### D7 — CONFIRMED conditional finite-volume jet transport; no uniform or infinite-volume promotion

**Anchors:** DICT55.md:269 (`same jets of order ≤5`), :680 (`At trivial-point jets the chain is sound`), :323 (`NM3`); CODEX_REVIEW_ASSEMBLY.md:65 (`R6`); PROOF.md:6684 (`𝔉_k`), :6695 (`D³E_k^br`).

Rebuild the small-order statement without using a status label. For `M=Σw_a exp(Y_a)` near I, the first-order trace in `tr log M` is zero because tr Y_a=0; its second-order trace is real because the trace of a product of two anti-Hermitian matrices is real. Thus `arg det M=O(‖Y‖³)`. The determinant-corrected polar competitor gives `0≤d≤(arg det M)²/(2N²)=O(‖Y‖⁶)`. Analytic local chain energies therefore differ by terms of total degree at least six.

On a **fixed finite** gauge complement with positive Hessian H, the implicit critical maps are analytic and O(B); their Taylor coefficients through order four coincide, since the stationarity equations first differ in degree five. Their critical values agree through degree five. To call these values the global minima, one additionally uses the finite compact zero-orbit argument: at top identity, zero energy means a flat fine connection with identity cycle holonomies and its compatible blocked chain, hence a single gauge orbit; the compact complement has a positive gap δ_(k,T). This supplies a local minimizing germ for each fixed k,T. No uniform lower bound on that gap or on the radius follows.

For any such critical germ, letting ζ=(−H^−1 F_xB,1), differentiation gives `E'''=F'''[ζ³]`. A second differentiation of the critical equation gives `x''=−H^−1 c`, and `E''''=F''''[ζ⁴]−3⟨c,H^−1c⟩`, with c=F_xzz[ζ,ζ]. Thus the cubic identity alone cannot transport order four; the matched full germ can. Combine this scope with D1's N factors. Claim status: **CONDITIONAL** on the stated finite-chain/slice setup; uniform domains, local-history minima and infinite-volume jet identification remain **OPEN**.

### D8 — CONFIRMED centred-cutoff mechanism; REFUTED unqualified position/weight factor e^(2μ)

**Anchors:** DICT55.md:139 (`For weights e^{μd}`), :700 (`FL3`), :967 (`A6`); LINEAR_PACKAGE.md:98 (`an object at level l sits at`); BFT4W55.md:111 (`pos(Z) :=`), :113 (`A link / plaquette sits at the midpoint / centre`), :120 (`lower-corner`), :124 (`w(z) := e^{μf(z)}`), :287 (`Lemma CEN1`), :309 (`Proposition CORNER`).

The cutoff distinction is real. For an affine cutoff with gradient v and a direction-constant field, the straight leg's first moment is `L x_μ v·(y−c_X)`. Pairing each go-path link with its reversed translate on the return path gives `−L v_μ x·(y−c_X)`. Both average to zero at the block center. Evaluating the coarse multiplier at the lower corner leaves the missing-center term `((L−1)/2)h_l L(v·1)x_μ`. Taking x_l=h_l a gives a residual of order h_l²; the σ-residual weight at l=0 multiplies it to a nonzero multiple of `L^(σ(k−1)−1)`. For fixed σ>0 this diverges with k. For σ=0 it stays bounded. This re-derives the mechanism; no check-script verdict is needed.

However the stated geometric comparison omits that **K places objects at base points while C additionally uses link midpoints and plaquette centers**. Put h_0=L^(−k), h_j=L^(j−k). The actual shifts are

- site: `δ_j=(h_j−h_0)1/2`;
- μ-link: `δ_j+(h_j/2)e_μ`;
- μν-plaquette: `δ_j+(h_j/2)(e_μ+e_ν)`.

For the **same arbitrary 1-Lipschitz f** of BFT4W55 §2.2, the safe two-sided weight-comparison factors are respectively `e^(2μ)`, **e^(5μ/2)**, and **e^(3μ)**. The claimed e^(2μ) for all objects is false as printed. Exact witness: L=3, k=j=2, base point 0, f(z)=d_1(z,0) on a sufficiently large torus. A top link's C position is `(17/18,4/9,4/9,4/9)` (take μ=1), whereas its K position is 0. Their f difference is **41/18 >2**, so their weights have ratio `e^(41μ/18)>e^(2μ)`. A top plaquette similarly has distance **25/9 >2**. Residual sources include top links, so the link issue occurs in the compared norm families.

**A narrower e^(2μ) statement can be repaired:** compare distances to the *corresponding coarse reference site*, translating that site as well by δ_k. The relative shift is then `(h_j−1)1/2+(h_j/2)Σ_{directions}e_ν`; for sites, links and plaquettes its ℓ¹ norm is ≤2. State this recentering explicitly. Alternatively, e^(2μ) is valid if K already assigns cell centers/midpoints and only the root shift changes; that is a different K convention from LINEAR_PACKAGE's printed base-point placement and must be named. For literal base points and an unchanged arbitrary f use e^(3μ) for the mixed family, e^(5μ/2) for links alone. All these are depth-independent; the decay rate is unchanged. This corrects a constant/comparison hypothesis, not the centred-cutoff obstruction.

### D9 — CONFIRMED gauge composition; dc55_2 reproduces its narrow group-algebra claim only

**Anchors:** DICT55.md:152 (`C4`), :1045 (`dc55_2`); BFT_B.md:1638 (`ĥ(h_1h_2, V)` and inline `RS7-8` repair), :1777 (`With V^g(x, y)`); checks/dc55_2_gauge.py:25 (`def left`), :28 (`def right`), :44 (`cocycle models`).

For the canonical action, applying a then b gives

`b_x(a_x U a_y^−1)b_y^−1 = (b_xa_x)U(b_ya_y)^−1`,

hence `(U^a)^b=U^(ba)`. For the right action the same multiplication gives `(U^a)^b=U^(ab)`. Composing covariance twice gives the left cocycle order `ĉ(h_2h_1,V)=ĉ(h_2,V^h_1)ĉ(h_1,V)` when a consistent lift is supplied; covariance without uniqueness gives equality of the transformed configurations, potentially only a gauge-product equality modulo stabilizers. BFT_B's original print is the right order and its inline erratum supplies the left order. GI-frame explicitly uses the right action; convert by inversion of each gauge.

After inspecting the script for writes and prohibited computation, I ran `python3 -I -B checks/dc55_2_gauge.py`. It reported **26 action instances and 26 cocycle instances**, both action laws true, both cocycle laws true, all four wrong-order controls firing, and `VERDICT: PASS`. The code uses Fraction arithmetic and writes only stdout. The universal algebra above is the proof; the finite test is a reproducible implementation check.

The cocycle models are coboundaries `X(hV)X(V)^−1` and `X(V)^−1X(Vh)`, so their positive cocycle identities telescope by construction. Their amended controls really can fail under the wrong convention. This discriminates order in the toy models; it does **not** construct a Yang–Mills CovLift, prove its uniqueness, or check its analytic/locality estimates. The reported pre-script timing is not independently authenticated here.

### D10 — CONFIRMED FL7 domain obstruction; narrowing SRC's set changes its theorem

**Anchors:** DICT55.md:731 (`FL7`), :899 (`FL7 update`), :1205 (`𝒞*_glob(ε_0) at level K`); SRCCD55.md:322 (`Coarse small-field set`), :355 (`every U_K ∈ 𝒮_K`), :623 (`BFT covers 𝒮_K only`); BFT34_55.md:83 (`𝒫_ε`), :106 (`E_k^br(B) := 𝔉_k(x(B); B)`); PROOF.md:36 (`Not banked` / `full curvature-small class`).

If all links in a gauge have HS-geodesic distance ≤s from 1, the bi-invariant triangle inequality gives plaquette distance ≤4s. The converse with a fixed linear loss is false even after arbitrary gauge changes. Here is an independent exact obstruction in SU(2), embedded in SU(N).

Take an even n≥4 torus, H=diag(1,−1,0,…), θ=2π/n², and coordinates x,y mod n. Set

`U_1(x,y)=exp(−iθ yH)`,

`U_2(x,y)=1` for y≠n−1 and `U_2(x,n−1)=exp(iθ nxH)`; other directions are 1.

Every 12-plaquette is exp(iθH), including the corner because θn²=2π; the other plaquettes are 1. Thus the maximal HS curvature is `ε_n=2√2π/n²`. A contractible square of side n/2 has holonomy exp(iπH/2) and HS-geodesic distance π/√2 from 1. Its perimeter is 2n. In any gauge, if the largest link distance is s, triangle inequality along this loop yields

`s ≥ π/(2√2 n)`, hence `s/ε_n ≥ n/8`.

This is a √ε obstruction, obtained without numerical approximation and without relying on OFFGLOB's label. It proves that small curvature does not give O(ε) globally small potentials uniformly over torus size. Operator/HS conversion changes only fixed N factors (`|X|_op≤|X|_HS≤√N|X|_op`), not the obstruction.

FL7's warning is **CONFIRMED**. But redefining 𝒮_K as the smaller gauge-saturated global-chart set is **not bookkeeping**: SRC-κ presently quantifies every field in the curvature-defined set. Such a replacement gives a restricted theorem and moves the excluded curvature-small fields into a still-uncontrolled sector. The full SRC/domain extension remains **GAP/OPEN**. This is the single most dangerous unresolved identification.

### D11 — The 44-input census is arithmetically consistent, not a verified 44-theorem status certificate

**Anchors:** DICT55.md:546 (`Status classes`), :591 (`LA38`), :594 (`LA41`), :981 (`8.1`), :1022 (`N24`), :1229 (`LA44`); ASSEMBLY55.md:383 (`N24`); PROOF.md:19 (`Lemma K and GU_m`), :50 (`corrected contraction/linear package`).

The final appended inventory has 44 rows: 12 B, 17 R2, 15 R1. I independently counted the stated ID sets; the arithmetic is correct. It is **NOT-VERIFIED** as a complete classification of all retained quantitative inputs. R2 is defined as a derivation by Codex **and/or** Opus, so it does not itself imply two-family validation; B may bank a conditional implication with open dependencies. The table mixes complete theorems, selected proof mechanisms, local nonlinear inputs, and bundled sublemmas. Counting rows cannot certify their premises.

Targeted status conclusions:

| Input | Review verdict on the dictionary's treatment | Required qualification |
|---|---|---|
| LA15 LR-pot | **REFUTED** exclusion from the banked chain | D4 retains it through FP and through W0; no provenance-count change follows. |
| LA23 WR(a) | **REFUTED** certification of the printed coefficient 9 by the cited argument; **NOT-VERIFIED** for that full quantitative R2 label | Separate the qualitative Hölder derivation from the sup coefficient and downstream radii (D5). |
| LA24 BA-3 | **CONFIRMED** the cited-argument error | Use 144 with the word-length domain; sharper 9 remains NOT-VERIFIED. A historical R1 review is not current certification of its printed number. |
| LA33 GU | **CONFIRMED** recorded banking membership | PROOF's decay bullet explicitly banks GU_m; its m=0 restriction is GU. This is receipt classification, not an independent re-proof of GU. |
| LA13 W / LA18 BL-4 | **NOT-VERIFIED** complete B classification | DICT quotes “CONFIRMED inputs and bookkeeping,” which alone does not decide whether the full quantitative statement was independently re-derived. Their cited review was outside the two-extra-file boundary. |
| LA38 NA-alg | **NOT-VERIFIED** full R2 classification | DICT's evidence says local uniqueness was “re-used”; that is weaker than re-deriving the explicit maximizer and remainder estimates of PROOF:3242. D6–D7 independently establish only the local algebra/analytic mechanisms actually used here. |
| LA41 NSL elliptic input | **NOT-VERIFIED** uniform ♮-norm conclusion | Combining an inherited C^(2,α) estimate with a pinning identity still requires their identical domain, scaling, constants and sup control. The cross-review combination was not rebuilt here. |
| LA36, LA37, LA40 package items; LIN0, FP, W0, YH, BL-2, BL-5(a), COF-size, PW-cc, LE, CO-upR/RH | **NOT-VERIFIED** mathematical estimates at the claimed uniform scope | No imported numerical or provenance label supplies their proofs. Retain these explicit inputs. LP:211 defines its strip via a minimum over κ; this review did not evaluate that minimum or certify positivity uniformly over an output κ-range. |

N24's literal assertion “not re-banked in S26” is refuted already by GU's actual banked pointer. That confirms a **narrow** version of DICT's reported N24 refutation. It does not validate DICT's entire five-item certification or convert the remaining linear package to PROVEN. I do not invent a revised global B/R2/R1 split from this sample; the correction is to qualify/split the affected statements and retain their dependencies.

### D12 — Source alias and norm boundaries; recorded restatements are not substitute lemmas

**Anchors:** DICT55.md:341 (`Aliases written E_k^br`), :496 (`O14`), :450 (`O11`), :399 (`O8`); BFT34_55.md:106 and BFT4W55.md:96 (`E_k^br := 𝔉_k`); SRCCD55.md:609 (`5.1 BFT-3 and BFT-4`), :616 (`E_k^br = S_W + R_k`); PROOF.md:18 (`GF-DEP`), :40 (`sup-plus-Wilson-Hölder coefficient class`).

The BFT34/BFT4W aliases are **CONFIRMED** from their explicit definitions: write them E^cb. The SRCCD passage gives only the older BFT decomposition and cites REVIEW_S22; it does **not** define its action as 𝔉_k evaluated at the composite critical point. DICT's stronger “MAPPED in every listed respect” reading for SRCCD is **NOT-VERIFIED**. Its use needs a consumer restatement and the domain/minimizer/localization bridges; the shared formula `E=S_W+R` identifies no branch by itself.

For coefficients, a correct unambiguous sufficient norm is

`‖ε‖_cf = ‖ε_W‖_∞ + [ε_W]^∞_α + max_l ‖ε_(S,l)‖_∞`,

with Wilson plaquettes and soft links kept separate. At mesh h, alternating Wilson values ±δ have sup δ and pointwise seminorm at least `2δ h^(−α)`. Consequently no depth-uniform bound of this norm by a coefficient sup norm exists. This proves the **class distinction**, not necessity of the Hölder norm for every possible SRC method. Replacing a maximum over all sup slots by a sum is an equivalent norm (within factor 2), not exact equality at a previously fixed radius. Retain or shrink radii accordingly.

S_E=Ker Γ_E, per-level gauges, and an orbit norm are different objects. Invariant outputs may survive a change of representative; potentials do not, since dλ can be added with no change to linear curvature. Similarly, Λ_0/const can be represented by functions vanishing on roots, but ΓΞ=−I cannot hold on a space containing nonzero constants when Ξ kills them. Use Λ_* for the vanishing space. Do not merge N(S), N_Σ(S), N^(σ)(S), or the pointwise and Campanato seminorms without their stated embeddings/constants. The exact uniform source-norm inequalities and all slice regularity estimates are **NOT-VERIFIED** anew in this review.

The coupling conversion is **CONFIRMED** independently: `s(exp(ia²F^aT^a))=a⁴Σ_a(F^a)²/(4N)+…`; summing unordered planes gives `u/(8N)∫Σ_(μ,ν),a(F^a_μν)²`. Matching `1/(4g_std²)` yields `u=1/g²=2N/g_std²`, and the coefficient stripped from the HS-normalized 𝔉 is u/N. This does not resolve an unannotated g in another file automatically.

### D13 — CONFIRMED stale citations; current receipts do not freeze historical line numbers

**Anchors:** DICT55.md:293 (quoted `PROOF l.2309`), :310 (quoted `PROOF l.6296`); BFT_A.md:122 (quoted `PROOF l.3512`); DICT55.md:1234 (`44 bullet lines incl. 3 batch headers`).

String relocation and direct reads show these cited line-number attachments have drifted:

| Claimed old PROOF location | What it contains now | Current locating string and line |
|---|---|---|
| 2309 for E_NA | A root-covariance identity in a linear Euler–Lagrange proof | `E_NA := S_W(U)`, **2556** |
| 6296 for 𝔉_k | A BR1 linearization/slice argument | `𝔉_k(U_0, …, U_{k-1}; V_k) :=`, **6684** |
| 3512 for the cited BCH estimate | A complex-symbol denominator estimate | `s := Σ|x_i| ≤ 1/4`, **4309** |

DICT uses exact strings as its primary locators, which avoids attaching its own reading to these old lines. But those surviving numeric references are not live evidence and should not be copied into restated banked lines. The offsets are nonuniform. These are **REFUTED line attachments**, not refutations of the relocated definitions.

I independently extracted **367 complete one-line locator pairs naming 61 files** from DICT by `rg`; I did not open all those files or re-run its presence audit. At the first header read, PROOF additionally contained `OS formulation and reconstruction glue` at line 51 (42 substantive bullets). A later bounded read contained 43 substantive bullets; the final bounded scan, stopped at `[S26-REVIEW]`, returned **44 substantive bullets plus 3 batch headers =47**, rather than DICT's correctly timestamped earlier 41+3=44. The other added titles were `Background transfer, log-chart repair` and `Non-freeness witness on the produced field e`. This is live-source drift, **not** a retroactive refutation of the author's as-of receipt. Any replacement banked block must preserve the separate scopes of newly appended bullets. The quoted source lines in findings are as read; locating strings remain authoritative.

## Disposition of all 29 flags

These verdicts concern this review's reconstruction of each flag or its proposed repair, not an endorsement of every cited theorem.

| Flag | Verdict and disposition |
|---|---|
| FL1 | **CONFIRMED** for the BFT34/BFT4W E^cb aliases; SRCCD identification **NOT-VERIFIED**. Jets retain D7's scope. |
| FL2 | **CONFIRMED** slice/representative distinction. A field estimate needs the specified slice or a separately justified orbit norm. |
| FL3 | **CONFIRMED** centred-cutoff cancellation/obstruction; **REFUTED** unqualified e^(2μ) comparison for base points versus centers with the same arbitrary f. Use D8. |
| FL4 | **CONFIRMED** φ/k̃ distinction; **REFUTED** literal signed-normalizer repair. Use Z_phi=e^(κud)Z_tilde. |
| FL5 | **CONFIRMED** NM1–NM3 algebra. β=1 and uniform/infinite-volume bridges remain conditional. |
| FL6 | **NOT-VERIFIED** full source-norm embeddings anew; preserve three names and the exact version consumed. |
| FL7 | **CONFIRMED** by D10's independent flux witness. Full curvature/local-region transfer remains **GAP**. |
| FL8 | **CONFIRMED** coefficient-class difference and need to separate ε_W/ε_S. Necessity for every SRC method **NOT-VERIFIED**. |
| FL9 | **CONFIRMED** dimensional conversion μ_phys=μ_coarse/ℓ_k; the assertion that every consumer implements it is **NOT-VERIFIED**. |
| FL10 | **CONFIRMED** u=2N/g_std² and HS factors. An unlabelled g still needs an explicit convention. |
| FL11 | **CONFIRMED** constant-on-roots versus vanishing-space algebra. Use Λ_*. |
| FL12 | **CONFIRMED** composition and corrected cocycle order; CovLift existence/estimates **NOT-VERIFIED**. |
| FL13 | **NOT-VERIFIED** strict inequality of minimized functions for some nontrivial datum; distinct definitions, 𝒯≥𝓔, and conditional jets are established. |
| FL14 | **CONFIRMED** ∀j∃r_j does not imply ∃r∀j; complete consumer rewrite **NOT-VERIFIED**. |
| FL15 | **NOT-VERIFIED** NORMS-side operator substitution and claimed harmlessness; that source was outside the read budget. |
| FL16 | **CONFIRMED** q=k−1−l removes the depth/weight collision; no new TR estimate certified. |
| FL17 | **NOT-VERIFIED** uniform NSL elliptic constant; keep C_Λ^(A) separate from the root-line constant 10. Do not assign C_N=34. |
| FL18 | **NOT-VERIFIED** full κ_0 inventory; use κ_0^ker for the specified kernel coefficient, never substitute a polymer entropy parameter. |
| FL19 | **CONFIRMED** R_W is a walk-box side in BFT4W; the complete multi-file R inventory is **NOT-VERIFIED**. Label each imported R. |
| FL20 | **NOT-VERIFIED** RLARGE-wide θ inventory; θ_LF is an appropriate unambiguous name for the quoted fraction. |
| FL21 | **CONFIRMED** the banked stripe amplitude β is not u or the β-functional. Renaming it β_str preserves that pointer's scope. |
| FL22 | **CONFIRMED** identity-chart, scaled-norm and curvature-adapted domains differ; Cauchy cannot cross domains without an extension lemma. |
| FL23 | **CONFIRMED** constant-gauge invariance is weaker than independent-endpoint invariance. For example Re tr U is constant-conjugation invariant but changes under unequal endpoint gauges. Consumer closure remains **GAP**. |
| FL24 | **NOT-VERIFIED** the universal assertion that every banked use converts seminorms correctly; retain explicit conversion factors. |
| FL25 | **NOT-VERIFIED** the universal no-dependent-step assertion for fixed-order versus order-averaged h_l. |
| FL26 | **CONFIRMED** seam N5 and the covariance-node N5 are distinct named propositions; write N5^seam for the former. |
| FL27 | **CONFIRMED** Ward W0 and BFT_A's level-0 linear W0 are distinct; write W0^Ward for the former. |
| FL28 | **CONFIRMED** position centering and subtracting a polymer's value at 1 are distinct. On an invariant domain, averaging a centered difference has norm ≤2 times its original centered bound by the triangle inequality; no factor-1 promotion. |
| FL29 | **CONFIRMED** the argument supports 144 rather than 9 in max-link units. The sharper inequality and all effective downstream minima remain **NOT-VERIFIED**. |

## Summary table

| Finding | Verdict | Consequence |
|---|---|---|
| D1 normalization | **CONFIRMED** algebra; **CONDITIONAL** analytic uses | Same κ, E_NA stiffness Nκ, energy factor N, nth-jet factor N^(1−n/2). |
| D2 gauge saturation | **REFUTED** verbatim blanket transport | Retain the chosen gauge, chart, slice and transported norms. |
| D3 locator gate | **CONFIRMED** limited predicate; complete receipt **NOT-VERIFIED** | 367/61 inventory checked; semantics, unmatched brackets and nonvacuity not certified by PASS. |
| D4 LR-pot | **REFUTED** exclusion | Restore LR-pot→FP→TOP♯ and the W0 dependency. |
| D5 BCH | **CONFIRMED** cited-argument refutation | 9→144; standalone auxiliary ceiling 1/9→1/144, with actual smaller minima checked separately. |
| D6 tower/normalizer | **CONFIRMED** configuration distinction; **REFUTED** literal sign repair; strict minimized inequality **NOT-VERIFIED** | Add +κud to log Z_tilde when replacing k̃ by φ. |
| D7 jets | **CONFIRMED** finite-chain implication | Order-five agreement is conditional on a matched smooth minimizing germ; no uniform/infinite-volume promotion. |
| D8 weights/cutoffs | **CONFIRMED** centering mechanism; **REFUTED** unconditional factor e^(2μ) | Same-f factors e^(5μ/2) for links, e^(3μ) mixed; e^(2μ) needs corresponding reference-site recentering. |
| D9 gauge script | **CONFIRMED** algebra and reproduced narrow test | 26+26 instances and four wrong-order controls; no Yang–Mills CovLift established. |
| D10 FL7 | **CONFIRMED** independent √ε obstruction | Restricting SRC's domain is a restricted theorem, not a closure of the original one. |
| D11 classifications | **NOT-VERIFIED** full 44-input certificate; narrow N24 refutation **CONFIRMED** | 12/17/15 is correct accounting; repair LR-pot/WR(a) and retain conditional inputs. |
| D12 aliases/norms | **CONFIRMED** two explicit aliases and norm-class distinctions; SRCCD mapping **NOT-VERIFIED** | E^cb naming alone supplies no consumer bridge. |
| D13 citations | **CONFIRMED** drift / **REFUTED** stale line attachments | Use locating strings and record time; do not copy historical line numbers. |

## Review boundary and check record

The procedural reads were SCIENCE_WORKFLOW.md (explicitly required by the supplied entry point) and the selected repository review-loop/SKILL.md. The two discretionary files beyond the named scientific sources were that review skill and BFT_A.md. Other scientific reads were restricted to the named DICT55, PROOF, HIST, FLOW, LINEAR_PACKAGE, BFT_B, BFT34_55, BFT4W55, SRCCD55, ASSEMBLY55, CODEX_REVIEW_ASSEMBLY and the explicitly requested dc55_1/dc55_2 scripts/criteria. Supporting reviews mentioned only inside DICT were not silently opened or treated as independently checked proofs. All large source reads used locating searches and bounded sed ranges. No snapshots, audit ledgers, git commands, subagents, network queries, heavy numerical libraries or output files other than this deliverable were used.

Executed checks: read-only dc55_2 with exact Fractions; independent rational SU(3) determinant arithmetic; exact BCH factor and auxiliary-threshold arithmetic; disjoint/complete 44-row ID-set accounting; locator-pair inventory with rg; bounded live-header inventory; direct relocation of stale citations. The dc55_1 script was inspected but not executed. No script PASS is used as a substitute for the derivations above.

## Exactly what may be banked, and corrected [S26-BANKED] restatements

**Newly bankable from this review, at exactly these scopes:**

1. **PROVEN:** the configuration normalization identities and coordinate-chain-rule factors in D1; the coupling conversion in D12. These do not independently establish β=1 or a minimizer bridge.
2. **PROVEN:** k̃=φ+d, d≥0; the exact normalized-kernel cancellation with `Z_phi=e^(κud)Z_tilde`; the rational S4′ SU(3) configuration witness to d>0 (and its SU(N), N>3 embedding); d=0 for SU(2) means. Strict inequality of globally minimized towers is not banked.
3. **CONDITIONAL:** finite-(k,T) minimizing-germ/critical-germ identification for the matched positive-κ φ-chain with fixed identity top, compatible periodic blocking and a nondegenerate gauge complement; consequent φ/k̃ value jets through order five. No uniform radius or infinite-volume conclusion.
4. **PROVEN:** both gauge-action composition laws and the order required of a consistent cocycle; the centred first-moment identity, its affine lower-corner obstruction, and D8's explicitly qualified weight comparison.
5. **PROVEN:** the cited BCH estimate yields 144 in max-link units, with total word size ≤1/4; preserving `2+144η≤3` is justified by η≤1/144 (or a smaller existing minimum). No counterexample to an independently proved sharper coefficient 9 is claimed.
6. **PROVEN:** D10's torus flux witness shows a √ε lower bound on the best global potential gauge and rules out a uniform O(ε) conversion. The coefficient sup/Hölder norm distinction is also proven. Neither is a universal no-go for another construction.
7. **CONFIRMED review findings only:** the LR-pot dependency omission, the two explicit E^cb aliases, the stale line attachments, the 44-row arithmetic, the locator gate's limited scope, and the reproduced dc55_2 output. These are not proofs of the inherited analytic package.

**Do not bank** an unconditional 12/17/15 scientific-status certificate, all 29 repairs as automatic bookkeeping, automatic fixed-slice transport to every gauge representative, the SRCCD branch identification, a curvature-class BFT/SRC theorem, a strict off-origin inequality of minimized towers, or any missing uniform elliptic/infinite-volume estimate.

The following are precise replacement/additional wording for the affected existing pointers. Preserve all unrelated existing qualifications and newly added bullets; only the owner of PROOF should apply these edits.

- **Scope sentence above the block:** “Every global-potential-small estimate is stated in a chosen small global gauge and its specified slice, norms and complex chart. Gauge transport carries those choices with it. This does not establish the curvature-small or local-region extension, or independence of local branch choices on arbitrary chart overlaps.” Do **not** insert DICT's unqualified “every 𝒞_glob statement holds on its gauge saturation” sentence.
- **(T-UNIF) / coupling-flow / assembly jet pointers (B1, B19, B29, B35):** “Use the matched positive-κ **φ-chain**. For κ_j≡κ, 𝔉_k=N E_HIST(chain), y=√N B, and D_y^n𝔉=N^(1−n/2)D_B^n E_HIST. T-UNIF controls the cubic composite vertex on the linear critical branch. Transfer to a minimum tower is through the stated finite-chain germ implication; order four includes the envelope exchange term. Uniform-radius and infinite-volume identifications remain separate hypotheses.” For the kernel repair add: “`k̃=φ+d`, `log Z_phi=log Z_tilde+κud`, so `−log k=κuφ+log Z_phi`.”
- **K^(σ), GV-E/BFT-E, NSL and BFT-4(a) (B10, B18, B28, B30):** “All original named linear/elliptic hypotheses are retained, including **LR-pot through FP and the W0/top-response route** unless explicitly replaced by an independently justified estimate. The quantitative Wilson-row statement uses the certified bound `2η+144η²`; coefficient 9 is not certified by its cited argument. Recompute affected prefactors and use an effective radius satisfying the corrected inequalities.” This does not revoke the independently banked qualitative local-(R) implication.
- **BFT-3 and BFT-4(a) (B26, B30):** “The action denoted here is `E^cb_k(B):=𝔉_k(x*(B);B)`, the composite critical value in the named small-field chart. No uniform identification with prescribed per-level BR1 actions or global/localized minimum towers is included.” For the weighted interface: “Use Convention C for cutoffs. The K/C weight factor is e^(2μ) for corresponding coarse-reference-site distance weights; for an unchanged arbitrary Lipschitz f use e^(3μ) for the mixed object family (e^(5μ/2) for links). Decay rates are unchanged.” Write `R_W` in `log 2/(16R_W+80)`.
- **BFT-5 source-only bound and TR (B6, B7):** “Keep N(S), N_Σ(S), N^(σ)(S) distinct. The version required by GV-E is the **N_Σ** version with its original named-input hypotheses; the N(S) display alone does not supply it.” The reported existing N_Σ review scope was not independently re-proved here. In TR write `q:=k−1−l`, `π_l≤A_B κ̂ L^(−q)`, and retain the existing critical-family and full-source hypotheses.
- **NSL constant names (B28):** “`C_N=4+3C_Λ^(A)`, where C_Λ^(A) is the retained NSL Lemma A(c) elliptic constant, not Lemma Λ's 10; `κ_0^ker` is the BR1 kernel coefficient.” Keep scaled-norm holomorphy and small-gauge uniqueness exactly as scoped.
- **SRC pointers (B25, B31):** “The available tree-level result uses the chosen global-potential-small chart and `‖ε‖_cf=‖ε_W‖_∞+[ε_W]^∞_α+max_l‖ε_(S,l)‖_∞`. It does not establish the asserted SRC bounds uniformly on the curvature-defined 𝒮_K or on a pure sup-norm coefficient ball. Restricting the domain gives only a restricted theorem; the excluded configurations and original SRC closure remain OPEN.”
- **Remaining names and invariance (B15/B16/B25/B31, B36/B37/B40):** use `R_F` for the flow-error constant, `θ_LF` for the large-field fraction, `β_str` for the stripe amplitude, and `W0^Ward` / `N5^seam` for the sphere propositions. In B37 say **“centered polymer norm: averaging costs ≤2 on the invariant domain”**; constant-gauge invariance of B30's pieces does not itself supply local gauge invariance or consumer closure.

These restatements bank precisely the identities, restricted implications and counterexamples above. The original curvature-class BFT/SRC bridge, uniform/infinite-volume identifications and unverified analytic inputs remain **GAP/OPEN**.
