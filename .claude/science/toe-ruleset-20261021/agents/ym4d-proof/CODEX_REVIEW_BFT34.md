# PRE-STATED

UTC: 2026-10-29 02:46:51 UTC

Independent hostile review of `BFT34_55.md`. This section is written before any mathematical derivation. Disclosure: two creation attempts failed (`python` unavailable, then a Python string-format brace error); heading discovery and the §0–§1.6 excerpt were returned before this successful write. No verdict or calculation has yet been made. No git commands. Only this deliverable will be written. Bounded reads only; no snapshots, audit ledgers, or whole large files. Exact integer/rational checks in plain Python only.

## Targets and refutation tests

1. **Lemma WD:** rebuild the differentiated critical equation and each Neumann input. Refutation: a non-cc source, inverse-domain mismatch, lost weight, or convergence in an uncontrolled norm.
2. **BFT3-glob / route C:** rebuild (H1)+(H2)_m+(H3)_m ⇒ all-orders U/E locality, uniformly in k,T. Refutation: missing hypothesis, stale quantifier, Cauchy-domain loss, or nonsummable convolution. Explicitly inspect the sigma-weighted residual leg and e^{14m}.
3. **GV-E_m:** locate the positive-decay proposition and the scope of `CODEX_REVIEW_GV.md`. Refutation: a gauge derivative loses decay or an E weight, or constants fail to sum uniformly.
4. **Proposition CX:** test the admissible action class, symmetries, domain, and obstruction. Refutation: the example is outside its stated class or actually satisfies the claimed violated bound.
5. **F4 / RW-cc / CCL and errata:** rebuild divergence, routing, boundary compatibility, and factor 216. Refutation: unroutable charge, incorrect product-rule source, insufficient geometric constant, or lost scale weight.
6. **Route T / b34_1 / b34_1b:** rebuild recurrences, factorials and counts. Refutation: wrong exact coefficient, invalid majorant, circular/vacuous test, or a changed scientific target disguised as a script repair.
7. **Status table:** distinguish proved implications from discharged premises. Refutation: PROVEN for an unestablished premise or a merely argued estimate.

Every symbol comparison will identify the object, file/string and quantifiers. Finding verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. Corrected numbers require derivations. Final output will say exactly what may be banked.

Read budget: files explicitly named by the task, plus `docs/ai_methodology/SCIENCE_WORKFLOW.md` (extra 1) and the corrected b34_1b check script (extra 2). The narrowly scoped owner contract governs this review; no broader workflow, git, landing, or additional reviewer is launched.

# Findings (appended during review)

## R1. Lemma WD: the cc Neumann argument survives, conditionally

**Verdict: CONFIRMED. Claim status: CONDITIONAL.** Target: `BFT34_55.md:109–127`, locating `Lemma WD` and `Every value of S̃ is cc`.

Let A = L_Γ^{-1}D_x S̃ and b_y = L_Γ^{-1}∂_{B_y}S̃. Since D^⊥ is a fixed linear operator and D^⊥S̃ is identically zero, D^⊥D_xS̃[u] = D^⊥∂_{B_y}S̃ = 0. Thus every application of L_Γ^{-1} in A^r b_y has a cc source, regardless of whether the intermediate field A^{r−1}b_y is itself a source. On each finite torus, (H2)_m and (H3)_m give ||A||_{m,f} ≤ 1/2 after the stated threshold reduction. Differentiating the fixed-point equation gives (I−A)x_y = b_y, hence

||x_y||_{m,f} ≤ Σ_{r≥0}2^{−r}||b_y||_{m,f} ≤ 2G_♯(m)e^{c_rm}S_1.

Reading the field sup component gives the claimed L^{−(k−j)}e^{−m dist(b,y)}. This does not prove (H1), (H2)_m, or (H3)_m. In particular the local weighted nonlinear estimate remains a separate premise; cc-ness alone supplies no norm bound. The norm convention for the weighted level-zero source must be made compatible with COFM55's actual product-weighted Hölder norm (see R2 below).

## R2. The residual leg: an actual m collision and a false endpoint summability assertion

**Verdict: REFUTED for the printed summability claim; CONFIRMED for the corrected residual-sup implication below. Claim status: CONDITIONAL.** Targets: `BFT34_55.md:211`, `:488–495`, locating `summable in m`, and `:638–643` (E6); compare `COFM55.md:116`, `:127–135`, `:467–476`; `COFUN_CC.md:415–426`; `BFT_B.md:3682–3684`, `:3702–3706`, `:3748–3751`.

The target's §0 declares bare m to mean only a spatial decay rate, but the resolution paragraph explicitly sets m = k−1−i and then writes e^{14m} and a weighted norm with that same m. E6 repeats the collision. Separate **μ ≥ 0** (fixed spatial rate) from **q = k−1−i** (integer depth). The spatial factor is e^{14μ}, never e^{14q}.

The exact scalar sum claimed to be summable is

Σ_{q=0}^{k−1}L^{(σ−1)q} = (1−L^{−(1−σ)k})/(1−L^{−(1−σ)}) for σ<1,

and is **k at σ=1** (or **k−1** if only the strictly lower levels q=1,…,k−1 are summed), not bounded independently of k. This is an included endpoint (`0 < α < θ ≤ σ ≤ 1`, target :100). E6 does not fix this quantifier.

The useful repair is not to sum this quantity: the residual output norm is a maximum over i. For the actual KOFF source representations, G_l=0 for l>0 (`GV55.md:134`, locating `G only at level 0`). The exact residual recursion then gives

||r_i^c||_{∞,μ} ≤ κ_-^{-1}[||s_i^c||_{∞,μ}+e^{5μ}L^{−2q}(||ρ_{k−1}||_{∞,μ}+Σ_{l>i}π_{l,μ}(ĵ_l))].

The e^{5μ} is the stated straight-transport reach; using e^{14μ} instead is conservative. Independently summing the funnel convolution,

Σ_lπ_{l,μ}(ĵ_l) ≤ [1+2d e^{2μ}/(1−L^{−3})]J_μ.

Indeed interchange l and l′ in Σ_lΣ_{l′≤l}L^{−3(l−l′)}π_{l′,μ}(j_{l′}); the inner geometric sum is at most (1−L^{−3})^{-1}. At d=4,L=3 the bracket is **1+(108/13)e^{2μ}**, and its μ=0 value is **121/13**. Thus with A_μ = ||ρ_{k−1}||_{∞,μ}+[1+(108/13)e^{2μ}]J_μ,

sup_i L^{(1+σ)q}||r_i^c||_{∞,μ} ≤ κ_-^{-1}[||s||_{R(σ),μ}+e^{5μ}A_μ],  0<σ≤1.

This uses sup_q L^{(σ−1)q}=1, including σ=1. TOP-cc_m controls ρ_top=κ_top r_top−s_top. Using the target's deliberately larger transport factor yields e^{14μ}[1+(108/13)e^{2μ}] on the J term (or (121/13)e^{16μ}); it is a fixed factor, not one multiplied at each level. The route is k-uniform in this residual **sup** norm. It does not supply an additional residual level sum at σ=1.

The omitted positive-level d*G_l terms cannot be dropped for general Setting LIN^cc sources; the repair above applies to the N^(σ) representations actually consumed here. COFM55's source norm uses ||wG_0^c||_∞+[wG_0^c]^∞_α, not an unspecified weighting of an unweighted norm. Locally these can be compared using |w(z)/w(z′)−1| ≤ μe^{μd_1(z,z′)}d_1(z,z′), but the comparison costs a μ-dependent constant and must be included when supplying (H2)_m.

## R3. Route C: valid conditional locality, with its actual domain and repeated-index completion

**Verdict: CONFIRMED as an implication; NOT-VERIFIED as discharged BFT-3. Claim status: CONDITIONAL.** Target: `BFT34_55.md:132–165`, locating `Theorem BFT3-glob`; status table N2 at :600.

For the U/x bound, choose an index y_* maximizing d_1(b,y_i). Apply the (n−1)-variable Cauchy estimate to ∂_{B_{y_*}}x on the embedded coordinate polydisc. A multi-index factorial is at most (n−1)!, and a star through b has length at most n max_i d_1(b,y_i). This proves the displayed rate μ/n. The coordinate radius ε_0(μ)/(2 sqrt(N²−1)) fits about every B in the half ball; the extra factor 2 in the displayed Cauchy bound is conservative.

For E, the envelope identity gives E_y = Ψ_y(x(B),B_y). The top term is a fixed-range analytic density, so its local derivatives are bounded uniformly in k,T on a strictly smaller fixed domain. For y≠y′,

E_{yy′} = D_xΨ_y[x_{y′}],

and WD gives C e^{rμ}e^{−μd_1(y,y′)}. If y=y′, the additional term ∂_{B_y}Ψ_y must be included: the target's proof writes only the distinct-link case, although the theorem allows repetitions. This is a repairable omission, not a counterexample: enlarge C_E by the bounded local direct derivative. Choose a pair of occurrences realizing the maximum separation; Cauchy on the remaining n−2 derivatives and t≤(n−1)max d give μ/(n−1). If every link coincides, t=0 and use the diagonal bound. Thus μ/4 and μ/3 for orders ≤4 are valid. Exponentiation and local coordinate changes preserve locality, with appropriately bounded higher-derivative constants; a first-order dexp statement alone is not a proof of the precise all-orders coordinate-change prefactor.

What this proves concerns the composite components on the stated global potential-small domain, on a fixed slice, **at fixed μ before choosing ε_0(μ)**. It proves neither the per-level tower identification nor curvature-small data outside that domain. Its weighted nonlinear premise (H3)_μ is explicitly only ARGUED at target :213. The source estimate and complex critical-point existence remain named premises. No assertion about a full constructive Yang–Mills theorem follows.

## R4. GV-E_m was already reviewed; carry its norm and small-torus correction

**Verdict: CONFIRMED that the prior review covers m>0; CONFIRMED for the explicit conditional interface; NOT-VERIFIED beyond it. Claim status: CONDITIONAL.** Targets: `GV55.md:344–365`, locating `Proposition GV-E_m`; `CODEX_REVIEW_GV.md:340–400`, locating `the weighted field estimate is a valid assembly`; `BFT34_55.md:209–215`, `:470–474`, `:653–657` (`Codex check pending`).

The earlier review explicitly covers GV-E_m, its weighted source norm, its range and its data clause. Therefore the target's pending-review pointers are stale as read in this review. This is not a reason to promote the analytic inputs: the existing verdict is itself a named-input implication.

The assembly's level sum can be rechecked without trusting the verdict. Set a=1−α>0. The plain funnel contribution is

Σ_l L^{−a(k−l)} Σ_{l′≤l} 2d e^{2μ}L^{−3(l−l′)}π_{l′,μ}
≤ [2d e^{2μ}/(1−L^{−(2+α)})] Σ_{l′}L^{−a(k−l′)}π_{l′,μ}
≤ [2d e^{2μ}L^{−a}/(1−L^{−(2+α)})]J_μ.

The residual inverse-estimate sum converges because θ_0>α. TOP-cc_μ bounds the top residual; CC-INV_μ bounds the invariant part; the finite-reach S_E reconstruction then gives the field estimate with a fixed e^{C_*μ}. The norm comparison needed here, when G_l=0 for l>0, is

||s||_{R,μ} ≤ L^{θ_0}||s||_{R(σ),μ},  α<θ_0<1, θ_0≤σ≤1,

so there is no σ=1 divergence in the field assembly. One must use the actual product-weighted G_0 Hölder slot recorded in R2. This verifies the assembly, not the imported analytic reconstruction or CC-INV from first principles.

**Number already refuted by the prior review, independently checked here:** `GV55.md:363–365`, `Small tori (T ≤ 4) ... ≤ 16 cells, factor ≤ e^{4m}`. A four-dimensional T=4 torus has **4⁴=256** coarse cells and ℓ¹ diameter **4·floor(4/2)=8**. The safe uniform comparison for T≤4 is **1≤w≤e^{8μ}**, not e^{4μ}. At opposite sites the exponent 8 is attained. The prior review explicitly supplies this repair. Since GV-E_m leaves C(μ) unspecified, its conditional existence statement survives. Do not silently reuse the incorrect quantitative citation.

## R5. Corrected RW-cc and the 216 routing factor

**Verdict: CONFIRMED for the corrected algebra and routing implication; NOT-VERIFIED for the complete analytic walk. Claim status: CONDITIONAL.** Targets: `BFT34_55.md:308–358`, locating `Proposition RW-cc (exact)` and `Lemma CCL`, with E1/E2 at :401–413. Source representation convention: `BFT_B.md:1032–1045` (`π: Y → X*`, `on Y componentwise`).

There are two distinct multiplications to keep apart: multiplying the G,s,j **representation slots**, and multiplying the resulting raw covector. The lane-B M_χ uses the former. The G and residual slots annihilate gauge gradients even after slotwise multiplication: d*d=0 and r(Dλ)=0. Thus D(M_χy) is determined by the plain currents, as CCL requires. One must not replace M_χπ by πM_χ without a product-rule correction.

For plain currents and a cutoff at link midpoints, each incident midpoint is a half-step from its endpoint. Hence

|d*(χj_l)−χd*j_l| ≤ 2d·[L^{−(k−l)}/(2ℓ)]sup|j_l| = (d/ℓ)L^{−d(k−l)}π_l(j_l).

The χd*j_l terms cancel off the terminal roots because the same scalar cutoff is evaluated at the same physical site at every level. To rederive the HR(v) factor: a centre-root axial routing in one L^d block sends at most M_γ=L^{d−1}(L−1)/2 site charges through an edge. A level-l charge of sup q_0, accumulated at level i≥l, has size at most L^{d(i−l)}q_0. Thus its level-i plain norm is at most

M_γ L^{(d−1)(k−i)}L^{d(i−l)}q_0 = M_γ L^{d(k−l)}L^{−(k−i)}q_0.

Summing i=l,…,k−1 gives M_γ L^{d(k−l)}(1−L^{−(k−l)})/(L−1)·q_0. Insert the cutoff charge and sum l. This proves the displayed bound with dM_γ/((L−1)ℓ), independently of depth. At d=4,L=3,ℓ=1/4, M_γ=27 and the bound is **216**. Including the unchanged source gives **1+216=217**. These numbers are correct. This is the specified hierarchical routing construction, not a general estimate for arbitrary gauge compensation.

The cutoff-source obstruction is real: a current around a single plaquette is divergence-free, whereas multiplying its four edge values by a nonconstant scalar cutoff generally produces nonzero divergence at non-root vertices. Thus cc-only linear estimates cannot simply be used on all raw cutoffs.

For RW-cc, P_ccΣ_□M_χ□y=y on the cc class, and every projected piece is cc. Assuming the stated root-preserving embeddings and kernel identity, solve H_□u_□=y_□ against all test fields. Locality and ψ=1 near the source give, box by box,

H(ψ_□u_□)=y_□+c_□.

Apply Ξ^T: Ξ^TH=0 and Ξ^Ty_□=0, so **Ξ^Tc_□=0 for each box**. This independently proves E2 and shows why arbitrary scalar bond weights preserve cc. The original parenthesis `although the single c_□ are not` is false, but the explicit erratum repairs it. No cancellation between distinct boxes is needed. The Neumann sum, if bounded, produces a representative modulo the gauge kernel; the S_E inverse additionally requires the final projection.

E1's assertion about the older hard-slice walk also needs its compensation to be supported where ψ=1. The algebra is valid under that locality premise; I have not independently reconstructed the old compensation kernel within the read budget. The new cc-localized construction does not need that assertion.

## R6. A missing factor L in the commutator exponent count

**Verdict: REFUTED for the displayed exponent arithmetic; NOT-VERIFIED for the unproved commutator estimate. Claim status: ARGUED.** Target: `BFT34_55.md:363–366`, locating `π_l ≲ L^{3+σ}L^{−σ(k−l)}`.

Put n=k−l. Multiplying the immediately preceding own-unit bound by π_l's conversion factor gives

L^{3n}·L²·L^{−n}·L^{−(2+σ)(n−1)} = **L^{4+σ}L^{−σn}**,

not L^{3+σ}L^{−σn}. Thus the literal exponent count drops one factor **L** (a factor **3** when L=3). For levels l=0,…,k−1 the corrected displayed scalar majorant sums to

L^{4+σ}(1−L^{−σk})/(L^σ−1),  σ>0,

and at σ=0 it is **kL⁴**, not kL³, when carrying the same prefactor from the preceding line. Hidden constants in `≲` may absorb a fixed L; this is a correction to the written arithmetic, not a counterexample to σ>0 summability. The Hölder, centring and multiplication estimates remain ARGUED exactly as the target acknowledges. No numerical C_c^σ can be banked from this calculation.

## R7. RW-cc-walk's advertised weight radius is not proved by its stated premises

**Verdict: REFUTED for the metric conversion; NOT-VERIFIED for the displayed conjugation estimate and the asserted (H2)^Lip supply. Claim status: GAP in the quantitative corollary.** Target: `BFT34_55.md:370–376`, locating `Each step moves supports by ≤ 2R + 6 (coarse ℓ^∞)` and `m_W := log(1/ε_W)/(2R + 6)`; compare :77–79 and :110–112 (coarse ℓ¹ weight).

1. **Metric error.** An ℓ∞ displacement bound a=2R+6 gives an ℓ¹ displacement bound **4a=8R+24**, not a. For a diagonal displacement (a,a,a,a), f(z)=d_1(z,0) is 1-Lipschitz in the required metric and f(a,a,a,a)−f(0)=4a. Therefore the cited support information licenses e^{4μa}, not e^{μa}. The scalar finite-reach convergence threshold obtained from that information is at best

**μ < log(1/ε_W)/(8R+24)**,

before any additional weighted-seminorm or slice-projection constants. This is one quarter of the printed threshold. A sharper radius would require a separate ℓ¹ support argument; none is given. For the product partitions with box sides in [R,2R), the claimed reach 2R+6 itself also needs rechecking: an input in □^(1) and an output in □^(R+3) can have coordinate separation approaching 3R+4. The correction above assumes the target's stated ℓ∞ reach rather than certifying it for those partitions.

2. **Constrained-domain issue.** R̃ has been constructed and bounded on cc sources. Multiplication by e^{−μf} does not preserve cc. For a divergence-free plaquette cycle, its incoming and outgoing weighted currents at a vertex can have unequal factors, giving nonzero divergence. Thus the expression e^{μf}R̃e^{−μf} is not automatically an endomorphism of the same cc space. It can be defined on the transported subspace e^{μf}cc, but then the unweighted cc→cc norm bound alone does not prove its asserted norm. One needs a compatible localized estimate or a box-indexed construction using **scalar** weights on already-cc pieces.

3. **Norm and final slice.** The norms contain derivative/Hölder components, while J is a sum of level sups. Multiplication by a spatial exponential is not merely scalar reweighting of each local seminorm. The target already needs (W-mult)^σ and summable profiles; their weighted versions and the bounded final S_E projection must be supplied in the appropriate norm. The Feynman-free parametrix produces a representative, not automatically the S_E field appearing in (H2)^Lip.

These are gaps in this claimed quantitative implication, not a proof that a corrected positive-rate walk is impossible. A promising repair is to retain each cc box piece, multiply it only by constant box weights, estimate weight ratios over its full ℓ¹ read/write reach, and then control the final slice projection. Do not use this corollary as an already proved alternative to GV-E_m or as a discharge of route T's input.

## R8. Proposition CX is a valid scalar obstruction, not a Yang–Mills-class counterexample

**Verdict: CONFIRMED for Proposition CX's explicitly stated scalar model and Lemma NC; NOT-VERIFIED for the gauge-theory instance or a no-go inside the specified Yang–Mills branch class. Claim status: PROVEN (scalar theorem), ARGUED (proposed gauge embedding).** Target: `BFT34_55.md:247–287`, locating `Model`, `Lemma NC`, `Gauge-theory instance`; status rows V12/N4 and the sentence `The brief's BFT-4 route is dead` at :658.

For fixed a,h and a specified differentiated site, at most a⁴ translates of the grid contribute. This cancels a^{−4}. The remaining geometric tail is bounded by q^{D_∞}/(1−q), and Σ_{a≥2}2^{−a}=1/2. A star through the n terminals has ℓ¹ length at most 4(n−1)D_∞, giving the stated μ_n=log(1/q)/(4(n−1)); repeated derivatives of one coordinate vanish. Extensivity follows from the same positive summable coefficients. All of these bounds are uniform in the torus size.

Rebuild NC: a distinct-coordinate derivative of R(X) at zero is bounded by ρ^{−n}sup|R(X)|, with **no n!**. It vanishes unless all differentiated sites lie in X^+. Every surviving X meets one of the **3⁴=81** neighboring cubes of the first site, yielding the factor 81. Choosing distinct Q′_i∈X within one ℓ∞ step of each terminal cube, doubling a tree of X gives

MST_∞({Q_i}) ≤ 2(|X|−1)+2(n−1).

This is exactly the claimed N_min lower bound. For the grid, all distinct terminal cubes are at least h/M_c apart, so its MST has length at least (a⁴−1)h/M_c. At zero only the monomial with exactly that site set survives; the torus size condition excludes a second wrapping parametrization. Its coefficient is a^{−4}2^{−a}q^{(a−1)h}. The logarithm of the ratio to NC's permitted bound has h-coefficient

m_0(a⁴−1)/(2M_c)−(a−1)log(1/q).

Choose a so this is positive, equivalently m_0(a³+a²+a+1)>2M_c log(1/q), then let h grow. Shrinking ρ does not repair the contradiction because a is fixed before h→∞. For every sufficiently large T, choose h a multiple of M_c below T/[4(a−1)] and above the contradiction threshold. This proves the advertised uniform-family obstruction.

**Class boundary:** the variables are independent complex scalars at sites. There are no SU(N) links, local gauge transformations, Bianchi constraints, or construction as the critical value of the specified finite-range Wilson-plus-soft functional. Those are extra properties of the actual branch. The proposed replacement by plaquette traces needs an explicit jointly independent local chart and a compatible base point; the target expressly does not provide them. Thus CX refutes the abstract inference from analyticity plus fixed-order derivative locality alone. It does not refute every use of Taylor/cluster methods exploiting the additional Yang–Mills structure, and does not settle BFT-4 for E_k^br. The target's caveat at :249–250 is essential; the broader lead sentence must retain it.

**A further quantifier boundary:** NC assumes a **supremum over all anchor cubes Q_0**, whereas §2.1 prints the norm anchored only at 0. These are interchangeable for a translation-covariant polymer family, which must be stated, or with a uniform-anchor norm. Without either condition, a one-anchor bound is vacuous: on a finite torus with at least three cubes per side, set X equal to all cubes except the anchor cube and put R(X)=E, every other activity zero. Then X is *-connected, X^+ covers the torus, and Σ_{X∋0}sup|R(X)|e^{m_0|X|}=0. Thus the scalar obstruction is banked with NC's **uniform-anchor** quantifier; promotion to the literally weaker one-anchor statement is **NOT-VERIFIED**. This is an additional reason to spell out the activity class rather than rely on the word “local.”

## R9. Route T and the b34_1b test: correct algebra, genuine repair, limited PASS

**Verdict: CONFIRMED for the identities/counts and the multiplicity repair; REFUTED for §1.4’s description of the script as checking all expanded tree counts; NOT-VERIFIED for historical unchanged-criteria/one-line-diff assertions. The explicit disclaimer that the script does not test locality is correct. Claim status: PROVEN (combinatorics), CONDITIONAL (Proposition TREE).** Targets: `BFT34_55.md:167–204`, `:498–513`; `checks/b34_1b_tree.py:63–79`, `:103–153`, `:261–280`.

Independent combinatorics: designate the direct B differentiations W, partition the remaining labeled positions into x-derivative blocks, and remove the single D_xG·∂_[n]x term. Adjoin one distinguished element to W: this is a bijection with partitions of n+1 labels, except the removed term. Thus the root counts are B(n+1)−1 = **1,4,14,51**. The envelope has n−1 remaining differentiations, hence B(n)=**1,2,5,15,52** through order five.

For fully expanded trees, let t(z)=Σ_{n≥1}T(n)z^n/n!. Direct leaves and unordered child subtrees give

t = exp(t+z)−1−t, equivalently t=z+Σ_{r≥2}(t+z)^r/r!.

Solving this formal recurrence with exact rational coefficients through degree four gives **T(1..4)=1,4,32,416**, independently of the script's partition iterator. The sign is correct: G=Lx−S̃ and the inverse line is −(D_xG)^{-1}.

The locality induction is also valid **if** its stronger inputs hold. G_Y(z)=t_S(z∪Y) is 1-Lipschitz; unions of rooted subtrees show Σ_A G_{Y_A}(z)+Σ_{i∈W}d(z,y_i)≥G_Y(z). The multiplicative vertex bound followed by the inverse estimate in that weight closes the induction. Doubling a Steiner tree and deleting the longest edge of the shortcut Hamiltonian cycle gives t≤2(1−1/N_t)t_S. This yields the target's U rates **μ,3μ/4,2μ/3,5μ/8** and E rates **μ,3μ/4,2μ/3**. Repeated terminals only improve the bound. These are implications of the explicitly stronger estimates, not estimates supplied by the tree combinatorics. R7 blocks the advertised automatic supply of (H2)^Lip.

**Actual execution:** ran the corrected script with `python3 -I -B`; each seed 11,23,37 produced 30 U and 62 E comparisons with zero mismatches, the printed Bell counts above, all four controls firing, and `OVERALL: PASS`. No output file was created. Its power-series solution and composition are different algebraic routes from the partition recurrence; the designed omitted/overcounted-vertex controls genuinely distinguish them.

**Independent defect reintroduction, in memory only:** changed the current multilinear routine to iterate distinct variable assignments instead of all factor-copy bijections, leaving every other line unchanged. Each of the same three seeds then gave exactly **28/30 U mismatches and 56/62 E mismatches**, with `OVERALL: FAIL`. For f=x², the missing multiplicity changes D²f(0)[u,v] from 2uv to uv; in general the lost factor is Π_jγ_j!. Thus the described repair fixes a mathematical error and does not change the implicit/envelope identities being tested. The earlier controls still fire against this broken baseline, exactly illustrating why controls alone are insufficient. I did not spend additional file reads on the old script, criteria, or historical output, so I do not certify the historical diff or timestamps.

**A check that cannot decide:** `TU` is printed at script :272–275 as informational. `ok_P3` at :276 checks only cntU/cntE, and the final verdict at :280 does not depend on TU. Replacing TU by any four numbers leaves OVERALL unchanged. Accordingly, the phrase `verifies both formulas and all counts exactly` at target :181–182 is too broad as a description of the gate. The target's §5 does disclose that T(n) is informational; this review banks those counts by the independent generating-function derivation above, not that PASS. No part of this script tests weights, decay, source domains, k/T uniformity, or (H3). The reported b34_2 withdrawal confers no mathematical evidence and no PASS.

## R10. E7's anchoring fix is right; the neighboring-polymer tree geometry still needs a correction

**Verdict: CONFIRMED for E7; REFUTED for the geometric inequality retained in §3.1(iv); CONFIRMED for a repaired all-orders implication with the same rate. Claim status: CONDITIONAL.** Targets: `BFT34_55.md:433–440`, `:644–647` (E7); `BFT_B.md:514–519`, `:538–541`; coordinate conventions at `BFT_B.md:29–37`, `:1037–1040`.

E7 correctly adds an anchoring factor 81: the two free derivative links cost |X^+|²≤81²|X|², while anchoring the fixed link b∈X^+ costs another 81 in the polymer norm. Thus **6·81³**, rather than 6·81², is the safe prefactor multiplying the other factors in the Hessian-Lipschitz estimate. This is a correct disclosed repair.

The separate inequality `|X|−1 ≥ t_S/(4M_c)−n` in §3.1(iv) still treats terminals in X^+ as if their attachment cost were that for X. Exact counterexample: take M_c=2, X the single cube [0,2)^4, and a sufficiently large torus. Its neighbor union contains [-2,4)^4. Let two first-direction links have base points (-2,-2,-2,-2) and (2,3,3,3). Their midpoints are (-3/2,-2,-2,-2) and (5/2,3,3,3), and both links lie in X^+. Their ℓ¹/Steiner distance is **19**. The printed inequality would require

**0 ≥ 19/8−2 = 3/8**, which is false.

A safe repair uses centers of the cubes of X. A *-edge between centers costs at most 4M_c in ℓ¹; a terminal in X^+ is at distance at most 6M_c from a center in X. Joining a tree of centers and attaching all n terminals yields

t_S ≤ 4M_c(|X|−1)+6M_c n,

hence **|X|−1 ≥ t_S/(4M_c)−3n/2**. With the same half-exponential split, a safe derivative prefactor is

**81 n! ((N²−1)^{1/2}/ρ_c)^n e^{3m_0 n/4} C_0**,

instead of the inherited unanchored n!((N²−1)^{1/2}/ρ_c)^n e^{m_0n/2}C_0, before adding the finite-range Wilson contribution. The rate **m_0/(8M_c)** remains valid. Thus the qualitative implication “BFT-4 gives every-order decay at an order-independent rate” survives; its displayed geometric proof and inherited constants do not survive verbatim. This does not affect NC, whose proof explicitly accounts for X^+.

## R11. Status-table adjudication, unreviewed boundaries, and citation checks

**Verdict: REFUTED for an unqualified banked reading of N6's weighted corollary; CONFIRMED for the explicitly conditional readings of N1/N2/N3 and the OPEN BFT-4 status. Claim status: CONDITIONAL / GAP / OPEN as specified below.** Target: `BFT34_55.md:578–608` (`Summary table`), read together with E1–E8.

- **N1 and N2:** their `PROVEN as implication` wording is appropriate after the minor completions in R2–R3. It is not a discharge of (H3)_μ, the analytic inputs, the source-norm interfaces, or the branch-identification premise. The target explicitly labels (H3)_μ ARGUED; that must remain visible.
- **N3:** the formulas/counts are PROVEN by their combinatorial derivation, with the script's restricted scope noted in R9. Proposition TREE is CONDITIONAL on (H2)^Lip and multiplicative (H3)^Lip. It is not discharged by N6.
- **N4:** PROVEN only for the stated scalar CX/NC model. The proposed SU(N) instance remains ARGUED; the strongest no-go wording in the lead summary exceeds this class.
- **N5:** the slice cc-ification identity is valid under X=S⊕Ran Ξ and ΛΞ=−I: y′=y+Λ^TD^⊥y agrees with y on S and annihilates Ξλ because ⟨y,Ξλ⟩+⟨D^⊥y,ΛΞλ⟩=0. This algebra supplies no norm bound for that compensation.
- **N6:** corrected RW-cc algebra and CCL are valid at their stated routing/kernel/locality premises. The commutator and multiplication estimates are only ARGUED, as the table says. The **specific** weighted corollary contains the wrong metric factor and an incomplete norm/domain argument (R7); listing it merely as a proved implication conceals a gap in the implication itself. Its source cc property does not replace weighted analytic estimates.
- **N7:** full BFT-4 remains OPEN. The local gauge-invariant polymers, curvature-small domain, decoupling-family construction and branch identification have not been proved here.
- **N8:** the top-residual observation is valid at separated links. Varying x gives δr_top=δM̄_top at fixed B, so the nonlocal part of E_{yy′} only reads this gauge-invariant response. Same-link derivatives include the direct local term described in R3. This does not bypass the current construction of the background response.

**V7's combinatorial core:** given an analytic splitting family, iterated one-dimensional fundamental-theorem-of-calculus expansions keep only connected bond sets. There are at most 40|X| bonds, hence at most 2^{40|X|} subsets, and |X|≤2^{|X|−1}. Therefore C_R=2^{40}C_E and K=2^{41}/(s̄−1) give |R(X)|≤C_RK^{|X|−1}. The animal count (80e)^{n−1} can be obtained by labeling a canonical spanning tree: at most n^{n−2}80^{n−1} rooted embeddings divided by (n−1)!, bounded by (80e)^{n−1} (n=1,2 separately). Consequently s̄−1≥2^{42}·80e·e^{m_0} implies ||R||_A≤2e^{m_0}C_R. This confirms that combinatorial implication, not the analytic splitting family or its source estimates.

**Other status rows:** V10's numerical consequences require R10's fixes; its near/far and recursion clauses remain NOT-VERIFIED here. The historical priority/provenance, DAG edges and downstream bookkeeping in V1/V13/V14 were not independently re-audited: their source files are outside the read budget. No blanket confirmation of all §7 rows is made.

**Line-drift checks:** strings locate `Lemma TOWER-VAR` at `PROOF.md:6666`, `Proposition COMP` at :6690, and the `(CL-cl)` restatement as BFT-4 at :6744–6755. All are inside the target's cited :6640–6760 range; I found no drift in that particular pointer. `BFT_B.md`'s proved BB-geo/BB-C/BB-IFT occur at :160/:166/:175, and its hard-slice dependency paragraph occurs at :2433. These pointers still match. This is a bounded citation check, not a read of PROOF.md as a whole. The stale quantifiers/statuses actually found are the σ=1 sum, the two meanings of m, the pending GV review labels, and the unqualified weighted-walk supply.

## Evidence boundary and execution record

Review completed UTC: 2026-10-29 03:06:39 UTC.

Files read: `BFT34_55.md`, bounded ranges of `BFT_B.md` and `PROOF.md`, `GV55.md`, `CODEX_REVIEW_GV.md`, `COFUN_CC.md`, `COFM55.md`; the two extra files were `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `checks/b34_1b_tree.py`. No snapshots or audit ledgers. No git commands, subagents, network/literature lookup, source edits, commits, or writes outside this deliverable. No NumPy, BLAS, floating-point numerical experiment, or long job.

Executed checks: corrected b34_1b; one in-memory multiplicity-defect reintroduction; independent exact-rational exponential-generating-function counts, routing arithmetic, funnel sum factor, small-torus counts, and the X^+ geometric counterexample. The gate outcomes recorded above are actual outputs. Finite checks do not replace the symbolic summations and identities. Original b34_1 criteria/output and all upstream analytic proofs were not read; inherited named hypotheses retain that boundary. Findings apply to the file contents inspected in this session; no repository revision was obtained because git was prohibited.

## Summary table

| Review | Finding verdict | Mathematical disposition | What changes |
|---|---|---|---|
| R1 | CONFIRMED | CONDITIONAL | WD's cc Neumann argument and first-derivative bound survive |
| R2 | REFUTED / CONFIRMED after repair | CONDITIONAL | Separate μ from q; the σ=1 sum is k; use a residual maximum, with a fixed funnel constant |
| R3 | CONFIRMED conditionally | CONDITIONAL | Route C gives μ/4 and μ/3 through order four; include same-link direct term and retain domain/premises |
| R4 | CONFIRMED interface; REFUTED inherited small-torus number | CONDITIONAL | GV-E_m already reviewed; T=4 has 256 cells and needs e^{8μ} for the stated diameter comparison |
| R5 | CONFIRMED corrected identities | CONDITIONAL | Each c_□ is cc; 216 routing and 217 including identity are valid |
| R6 | REFUTED arithmetic | ARGUED | L^{3+σ}→L^{4+σ}; the corresponding σ=0 count is kL⁴ |
| R7 | REFUTED metric inference; NOT-VERIFIED weighted supply | GAP | Denominator 2R+6→8R+24 even assuming the stated reach; weighted cc-domain/norm/projection argument missing |
| R8 | CONFIRMED scalar theorem; NOT-VERIFIED SU(N) extension | PROVEN / ARGUED | CX/NC obstruct the abstract inference only |
| R9 | CONFIRMED identities/repair; REFUTED broad gate coverage | PROVEN / CONDITIONAL | Counts correct; corrected PASS reproduced, original defect's FAIL reproduced; TU is not gated |
| R10 | CONFIRMED E7; REFUTED X^+ geometry | CONDITIONAL after repair | Attachment −n→−3n/2; safe prefactor 81e^{3m_0n/4}; rate m_0/(8M_c) survives |
| R11 | REFUTED unqualified N6 promotion | GAP / OPEN | Keep full BFT-4 OPEN and all undischarged analytic premises explicit |

**Single most dangerous unverified step:** treating the cc-localized walk as an already proved source of (H2)^Lip, despite the missing weighted-domain/norm argument and the incorrect reach-to-rate conversion. This is the step that can silently turn conditional tree locality into an asserted theorem.

## Exactly what may be banked

1. **Conditional WD and route-C locality** for the composite critical point on the global potential-small domain, with fixed μ, explicit (H1)/(H2)_μ/(H3)_μ, the correct representation norms, and the same-link E completion. Rates through order four: μ/4 for x/U and μ/3 for E. Neither the original per-level tower identification nor the full curvature-small class is banked.
2. **The repaired residual-sup assembly**, including σ=1, and the explicit GV-E_m interface as a named-input implication. The funnel convolution is k-uniform; at d=4,L=3 its unweighted constant is 121/13. The inherited small-torus quantitative citation must use the corrected bound.
3. **Corrected RW-cc algebra, the slice cc-ification identity, and CCL's 216 bound** for the specified hierarchical routing; every commutator piece in the new construction is cc. No quantitative weighted inverse or complete decoupling family is banked from those identities.
4. **The tree derivative identities and exact counts**, plus Proposition TREE only under its explicit stronger weighted/vertex hypotheses. b34_1b's algebraic PASS and the genuine multiplicity repair are bankable at that scope. The printed walk is not a verified supplier of those hypotheses.
5. **CX and NC in their scalar model with the uniform-anchor norm (or translation-covariant activities)**, the connected-bond combinatorial bound given an analytic splitting family, and the repaired Cauchy consequences given BFT-4 (including 81³ anchoring and the corrected X^+ attachment cost). No SU(N)-class no-go, analytic polymer construction, or full BFT-4 theorem is banked.

