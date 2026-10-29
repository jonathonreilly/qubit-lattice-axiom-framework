# Independent hostile review of B2_55

## PRE-STATED — 2026-10-29 06:47:06 UTC

Reviewer: Codex; independent review of the supplied Opus result. No claim of model-family provenance beyond the assignment is used as evidence.

Scope: Theorem B2 and its Schur kernel/norms; STEP55's stationary-lift/Hessian identification and gauge quotient; T3 sharpness; Proposition HL and its claimed independent route to (HC_k); J6/J7; b2_55_1 and the m_Y / ln(2)/4160 erratum. Read only the named sources and at most two additional files. No git commands, no snapshots, no audit ledgers. The sole write target is this file. Arithmetic checks will use exact rational or symbolic reasoning only.

Refutation criteria fixed before derivation:

1. A claimed row/column estimate concerns different kernels, norms, weights, domains, or quantifiers; a dimension, scale, periodic-volume factor, or complexification step is missing.
2. The Hessian identification drops a stationarity or constraint-curvature term, uses unavailable invertibility/positivity, or treats a non-null gauge direction as null.
3. A gauge representative evades the T3 lower bound, or the constant-field normalization yields a different scale factor.
4. The third-derivative bound does not control the stated operator norm uniformly, or the HC_k route silently imports B2, a certificate, induction, or an unavailable domain inclusion.
5. A dependency assertion omits locality, PG transfer, or the identification of the relevant main term; quoted locations no longer support their claims.
6. A numerical value fails an exact enclosure, a minimum is evaluated at an obsolete input, or a check is tautological/vacuous/unsatisfiable and cannot establish its advertised proposition.

Review findings will use CONFIRMED / NOT-VERIFIED / REFUTED. Claim status will use PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. A missing justification is not by itself a counterexample. Each finding will identify its source by current line and locating string. Findings will be appended during the work, followed by a summary table and the precise bankable remainder.

## Read boundary and source convention

`L` below denotes `.claude/science/toe-ruleset-20261021/agents/ym4d-proof`. Named sources read: `L/B2_55.md`, bounded parts of `L/STEP55.md`, the named `b2_55_1` check's script/criteria, and the explicitly required `docs/ai_methodology/SCIENCE_WORKFLOW.md`. The two additional files selected are `docs/ai_methodology/skills/review-loop/SKILL.md` (bounded procedure read) and `L/BFT34_55.md` (bounded prerequisite reads). Only bounded string searches/ranges of `PROOF.md` will be used if needed. Other reviewers' conclusions quoted inside these sources are not independent evidence here. No source-status promotion, source repair, git operation, or delegation is part of this review.

## Findings (appended as established)

### R1 — CONFIRMED: the Schur kernel and sharp scale match, conditionally

**Attaches to:** `L/B2_55.md:132–143`, locating strings `Put k_j(b, y) :=`, `Rows (from BFT-2`, and `Schur`; prerequisite `L/BFT34_55.md:113–126`, `weighted linear estimate` / `Every value of S̃ is cc`.

**Claim status: CONDITIONAL.** Write h = L^{−(k−j)}, D = D_N. In HS coordinates each coordinate-column derivative has norm ≤ C_WD h exp(−μd). Thus the block operator norm k(b,y) is ≤ √D C_WD h exp(−μd). Counting four orientations and h^{−4} sites per coarse volume gives the column sum ≤ 64√D C_WD h^{−3}(1+1/μ)^4. No weighted ℓ² norm has been substituted for the claimed unweighted one.

For the row, holomorphy on the larger ball gives ||Σ_y K(b,y)v_y|| ≤ 2C_0h whenever sup_y||v_y||≤1. For a fixed output unit vector u choose v_y = K(b,y)^*u/||K(b,y)^*u||, omitting zero terms. This proves Σ_y||K(b,y)^*u||≤2C_0h. Summing this inequality over D output basis vectors and using ||K||_op≤Σ_a||K^*e_a|| gives Σ_y k(b,y)≤2DC_0h. This is a valid passage from the vector-valued sup bound to an absolute block-kernel bound; cancellation is not silently discarded.

Schur now gives ||K||_{2→2}²≤128 D^{3/2}C_0C_WD h^{−2}(1+1/μ)^4, exactly the square of the stated C_B2 L^{k−j}. The torus sum is dominated by the infinite grid by choosing nearest periodic images, independently in each coordinate; 2/(1−e^{−μh})≤2(1+1/(μh)) follows from e^{μh}≥1+μh. Thus neither a T factor nor a scale factor is missing. The radii ε_B2≤r_ℂε_0/2 and ε_B2≤ε_0(μ)/2 provide the required Cauchy margin and WD domain respectively.

The WD implication also checks: the fixed, linear cc annihilator kills derivatives of the identically cc source; the weighted derivative equation is (I−A)ẋ=b with ||A||≤1/2, so ||ẋ||≤2||b||. This does **not** independently establish (H1), the assembled (H2)_μ, or (H3)_μ. The source's promotion of (H3)_μ via RLOC55 is outside this read boundary; retain it as a supplied premise in what this review banks.

### R2 — CONFIRMED: stationary-value Hessian identity; the word “minimising” needs qualification

**Attaches to:** `L/B2_55.md:150–164`, `(E1) Hess E^cb_k` and `(E2) Gauge freedom`; `L/STEP55.md:454–460`, `min over the finer variables`.

**Claim status: CONDITIONAL on full stationarity and the stated gauge invariance; the differentiation itself is PROVEN.** For F(x(B),B), the chain rule gives E″[δ,δ]=F″[(ẋ,δ),(ẋ,δ)]+F_x x″. Full x-stationarity kills the last term directly. Differentiating F_x=0 gives H_xxẋ+H_xBδ=0 and reproduces the same identity. Positivity and finer-level induction are absent from this calculation.

For a gauge action fixing the top data, F_x K_xξ=0 identically. At F_x=0 its differential in an arbitrary joint direction is H[(K_xξ,0),·]=0. The stationary lift and its gauge translates therefore have identical joint-Hessian value. Termwise lower bounds valid for every extension may be evaluated at the bounded slice lift.

This proves an **evaluation at a stationary lift**, not a minimum principle at a general background. Invertibility/stationarity alone would not imply minimization: F(x,B)=−(x−B)² has the unique stationary lift x=B, with H_xx=−2. Therefore the literal identification with STEP55's *minimising* δ* is NOT-VERIFIED without an additional positivity argument. The needed replacement of STEP55's minimum argument by the exact stationary-value identity is valid. At the trivial background the explicitly positive quadratic chain does supply minimization (R3 below).

### R3 — CONFIRMED: T3's scale is sharp for every tangent gauge representative

**Attaches to:** `L/B2_55.md:175–192`, `Proposition SH`; `L/STEP55.md:121–143`, chain energy and `Q∘d = d∘ev`.

**Claim status: PROVEN for the stated quadratic chain.** A constant coarse direction δ=c e_ν has a zero-energy extension y_i=L^{−(k−i)}c e_ν: its curl vanishes and every contour integrates to L times its constant link value. Since κ_i>0 and the chain is a sum of squares, every minimizing extension has d y_0=0 and Qy_i=y_{i+1}. The identity dQ=Q_2d propagates closedness to all levels.

One can establish the needed period statement without citing torus cohomology: d y_i=0 lets a straight ν-loop slide across any transverse plaquette strip without changing its sum. Subtract the constant form whose four periods match y_i; all remaining loop periods vanish, so integration from a base vertex defines a single-valued periodic λ and y_i=h_i+dλ. Each Q contour telescopes on dλ and integrates constants by L, hence preserves the complete ν-period. That period is Tc at every level. There are T_j³ disjoint ν-loops of T_j=TL^{k−j} links each; Cauchy–Schwarz on each gives ||y_j||²≥T_j²T²|c|²=L^{2(k−j)}||δ||². Periodic infinitesimal gauge changes are exact forms and cannot change this. This is a statement about tangent representatives; no claim about arbitrary finite, large gauge transformations is needed.

The displayed weight tolerances follow independently by summing geometric series. With uniform extra exponent a, mismatch is L^{2(1+a)}Σ_{q=0}^{k−1}L^{(2a−σ)q}, certificate error is Σ_{q=1}^kL^{(a−1)q}, and the level-zero spin majorant is L^{2a_0k}. Thus only the level-zero term forbids every strictly positive loss a_0; the others tolerate a<σ/2 and a<1. The source's literal `k-uniform iff a_0 = 0` (`B2_55.md:248`) presupposes the intended **weaker-bound** range a_0≥0; over unrestricted real a_0 the correct condition is a_0≤0. This does not produce an improved possible B2 estimate, because the period argument already excludes exponent below one.

### R4 — REFUTED: a downward-rounded decimal is printed as an upper bound

**Attaches to:** `L/B2_55.md:264`, `m_Y ≤ ln 2/4160 ≤ 1.666219·10⁻⁴`; `L/checks/b2_55_1_lattice.py`, locating string `m_Y <= mbar = %.6e`; matching printed line in `b2_55_1_out.txt`.

The second inequality is false. An exact rational certificate is obtained from

    a = Σ_{n=1}^{60} 1/(n 2^n),   a < ln 2 < a + 1/(61·2^60) = b.

The remainder bound follows by replacing each 1/n in the tail by 1/61 and summing the geometric tail. Direct Fraction comparisons give

    166621918403833 / 10^18 < a/4160 < ln 2/4160
      < b/4160 < 166621918403834 / 10^18.

Therefore ln 2/4160 is strictly greater than 1.666219·10⁻⁴. A correct upper bound at the printed precision is **1.666220·10⁻⁴**; the append-only erratum's looser **1.6663·10⁻⁴** is also valid. Ordinary nearest-decimal formatting does not preserve an inequality certificate.

The substantive D conclusion survives: exact comparisons with the same a,b give

    36,031,343 < (1 + 4160/ln 2)^2 < 36,031,344.

For the old rounded rate 1.67·10⁻⁴, the corrected exact factor is

    (1 + 10^6/167)^2 = 1000334027889/27889,
    35,868,407 < 1000334027889/27889 < 35,868,408 < 36,000,000.

Thus the self-erratum's criticism of using 1.67·10⁻⁴ is CONFIRMED, and N14's ≥36,000,000 remains CONFIRMED conditional on μ≤m_Y≤ln 2/4160. The error is in the reported decimal upper bound, not in the rational D predicate.

### R5 — CONFIRMED: HL's global-coordinate operator estimate does not need B2

**Attaches to:** `L/B2_55.md:294–305`, `Proposition HL`; `L/BFT34_55.md:146–158`, `Theorem BFT3-glob` / `(E)`; `L/STEP55.md:129–160`, `Theorem LC`.

**Claim status: CONDITIONAL on the complex-domain (H1), (H2)_μ, (H3)_μ and the same-link-completed C_E.** Here is the load-bearing reconstruction, rather than reliance on the cited review verdict.

Full stationarity gives E_y=F_y=Ψ_y. Only the last soft term contains B_y, so Ψ_y depends directly on B_y and on a fixed number (depending on L) of level-(k−1) variables within a bounded coarse distance of y. Its derivatives on the chosen complex domain are bounded. Thus

    E_yy′ = Σ_b (∂Ψ_y/∂x_b) x_{b,y′} + 1_{y=y′} ∂Ψ_y/∂B_y.

WD bounds the first term by C exp(−μd(y,y′)); the second is local and is absorbed by increasing the same C_E. This diagonal completion is essential for arbitrary ℓ² fields and repeated derivative indices. Choose the most separated pair from three derivative indices and differentiate this uniformly bounded holomorphic second derivative by Cauchy. With ϱ=ε_0(μ)/(2√D_N), the component-to-block conversion costs D_N^{3/2} and the stated conservative Cauchy factor is 2/ϱ. Since the three-terminal spanning tree has length at most twice its diameter, the resulting block bound is

    ||E_y1y2y3|| ≤ A_3 exp(−μ t(y1,y2,y3)/2),
    A_3 = C_E(2/ϱ)D_N^{3/2}.

For any three points, t≥diameter and d12+d23≤2 diameter≤2t. This includes repeated links and the torus metric. Therefore contraction with B in ℓ∞ and A,A′ in ℓ² is bounded by A_3||B||∞ times two exponential-kernel sums at rate μ/4: one sum over y1 and one Schur bound over (y2,y3). Each is ≤S=64(1+4/μ)^4. Hence

    |D³E(B″)[B,A,A′]| ≤ A_3 S² ||B||∞ ||A||2 ||A′||2.

Integration over B″=tB yields exactly C_3=A_3S² in the source. This is a genuine ℓ∞-in-background / ℓ²-operator estimate, not a componentwise estimate mislabeled as an operator bound. The same double-sum argument also bounds absolute Hessian row sums; it is stronger than merely pointwise continuity. The domain must be the actual complex domain on which WD and the analytic stationary family hold; the proof cannot use a merely real derivative bound.

For completeness, LC follows by the following independent bookkeeping. Telescoping dB_{i+1}=Q_2dB_i−dr_i gives

    <dB_k,Ξ> = <dB_0,(Q_2*)^kΞ>
               − Σ_i <r_i,(Q*)^{k−1−i}d*Ξ>.

The Q_2 row and column masses are L² and L^{−2}, giving ||Q_2||≤1 in four dimensions. For co-closed sources Q*=Q_str*, whose row/column estimate gives norm ≤L^{−1}. Also ||d*||≤4: the Fourier symbol of d is exterior multiplication by (e^{ip_ν}−1)_ν, whose squared norm is ≤16. Weighted Cauchy–Schwarz against the chain energy gives exactly

    c_co(k) = [2 + 32 Σ_{m=0}^{k−1}L^{−2m}/κ_{k−1−m}]^{−1}.

The trivial composite Taylor expansion is the chain quadratic: each soft term contributes (κ_i/2)||Qy_i−y_{i+1}||² and the Wilson term contributes (1/2)||dy_0||² in the stated HS normalization (also located at `PROOF.md:6695–6706`, `quadratic part of 𝔉_k`). Its stationary lift minimizes this positive quadratic, so Hess E^cb_k(0)[A,A]=2E_k(A). This verifies the factor 2 in HL. Combining LC with the operator estimate gives the stated global-coordinate lower bound. No estimate on ||∂x_j[δ]||2, covariant certificate, or induction has entered.

### R6 — NOT-VERIFIED as literally identified: D_bg in the claimed transfer is not pinned to the consumer's operator

**Attaches to:** `L/B2_55.md:307–309`, `‖dḂ − D_{bg}A‖ ≤ Cε‖A‖` / `That is (HC_k)`; `L/STEP55.md:446`, `(HC_k)`; contrast `L/PROOF.md:3290`, `(D_Uλ)_b := Ad(U_b)λ(y) − λ(x)`.

The explicitly defined D_U in the consumer source is the gauge gradient **0-forms → 1-forms**. The transfer uses D_bg on a **1-form A** and compares its output to the **2-form dḂ**. Neither B2_55 nor STEP55 defines the 1-form → 2-form operator in these displays. This is an actual unpinned symbol/type collision, not evidence that the intended covariant-curl estimate is false. A definition and the identification with the quadratic form entering PG must be supplied; reusing the symbol alone does not supply it.

A precise bankable repair is available without B2. Define P_bg A to be the left-trivialized derivative of each oriented plaquette holonomy along e^{tA}bg. For an oriented plaquette with holonomy U_1U_2U_3^{-1}U_4^{-1}, it is

    P_bg A = A_1 + Ad(U_1)A_2 − Ad(U_1U_2U_3^{-1})A_3
             − Ad(U_1U_2U_3^{-1}U_4^{-1})A_4.

At bg=1 it is dA. Each transport contains at most four background links. For real B, adjoint transport is isometric and ||Ad(e^B)−I||≤2|B|, so each coefficient differs from its zero-background value by at most 8ε. The fixed incidence counts give absolute row sums ≤32ε and column sums ≤48ε; Schur yields ||P_bg A−dA||2≤40ε||A||2, independently of k,T. Also ||S(B)−I||≤ε/(1−3ε), so at ε≤1/100 the difference ||dḂ−P_bg A|| is ≤45ε||A||. This supplies a concrete local comparison for the repaired operator.

Write J(B)=dexp_B and S(B)=J(B)^{−1}. The convergent series J=I+(ad B)/2+O(B²) and its Neumann inverse give S=I−(ad B)/2+O(B²), uniformly on a fixed small HS ball. Along log(e^{tA}e^B), Ḃ=S(B)A, so ||Ḃ−A||2≤Cε||A||2. Moreover B̈=DS(B)[S(B)A]A. The potentially constant term is −[A,A]/2=0; the remaining terms give |B̈_y|≤Cε|A_y|². These statements use convergent local series, not a volume-dependent inverse.

The n=2 kernel sum and ∇E(0)=0 give sup_y|E_y(B)|≤Cε. Hence |DE(B)[B̈]|≤Cε²||A||². Combining R5, ||dḂ−P_bg A||≤Cε||A||, and

    ||u+e||² ≥ (1−ε)||u||² − ε^{−1}||e||²   (0<ε<1)

gives Hess^L E^cb_k(bg)[A,A]≥2c_co(1−ε)||P_bg A||²−C′ε||A||²; ε=0 follows directly. **This repaired, explicitly defined plaquette form is CONFIRMED conditionally.** A small local logarithmic-coordinate modification of P_bg has the same estimate. It becomes STEP55's claimed (HC_k) when that file explicitly identifies D_bg with this type of covariant curl; its PG transfer remains a separate obligation.

The 99/97 factor in `B2_55.md:170–172` is also correct **under its stated extra radius restriction** 2max(ε_B2,C_0ε_B2)≤1/50: ||J−I||≤β/[2(1−β)]≤1/98, whence ||J||≤99/98 and ||J^{−1}||≤98/97. If the original ε_B2 is larger, replace the transfer radius by min(ε_B2,1/[100 max(1,C_0)]); the factor is not unconditional on the full original polydisc.

### R7 — CONFIRMED: J6's rejection is justified; the underlying reduction and CX implication are REFUTED

**Attaches to:** `L/B2_55.md:281–289,340–346`, `J6`; `L/STEP55.md:486–505,519`, `(H1) [covariance with decoupling]`, `Each added box raises`, and `here reduced to (HC_k) + (B2)`; `L/PROOF.md:5603–5604`, `(RW1)` / `(RW2)`, and `:5631–5634`, `(v) locality`.

**Claim status: GAP for the displayed reduction; OPEN for a repaired cluster theorem.** Positivity is a spectral lower bound and B2 controls an extension in ℓ². Neither bounds the weighted absolute entries of the one-level Hessian. For example K=I+a(e_p e_q^T+e_q e_p^T), 0<a<1/2, stays uniformly positive while p,q separate; its weighted absolute row sum contains a e^{m d(p,q)}. Thus the separate RW2 requirement cannot be inferred from positivity. The actual RW source also conditions its finite-step geometric locality on finite range of K. Route-C Hessian decay is a suitable additional input, after the correct main-term identification, but an ℓ² extension bound alone is not.

Two independent failures in the written CX proof can be reconstructed without trusting CODEX_REVIEW_STEP:

1. **Parameter locality is not a hypothesis.** Take K=I, so its RW field interpolation is I and all covariance locality requirements are satisfied. Let one singleton interaction be V_{X0}(A;z)=h z_p z_q, independent of A, with |z|<1, h arbitrarily small, and p,q arbitrarily far apart. This satisfies the written field-support and holomorphy/size conditions of H2. Choose the rates as large as required by H4. The normalized integral is exp(−h z_p z_q), whose logarithm has mixed parameter derivative −h. Any claimed locally parameter-dependent polymer representation can contribute to this derivative only through Y with both p,q in Y^♯. Such supports must have tree length tending to infinity with d(p,q). Cauchy and the asserted exponential polymer bound force their total derivative to zero as the separation increases: connected lattice trees of length m can be encoded by a walk of length 2m on a bounded-degree graph, so their count is at most exponential, while H4 can be chosen with arbitrarily larger decay rate. This contradicts the fixed derivative −h. Hence CX's background-local conclusion does not follow even with a finite-range, perfectly local covariance.

2. **Adding one arbitrary box need not cost only 2√d in tree length.** For Y={p}, Z={p,q}, |Z−Y|=1 while d(Z) grows with the separation. In the metric spanning-tree convention the correct single-addition upper bound is t(Y∪{q})≤t(Y)+dist(q,Y), obtained by attaching q to its nearest old vertex; for a singleton Y, the added cost is exactly dist(p,q). There is no universal four-unit replacement cost in d=4. A nonzero long jump makes precisely this term occur. In the two-endpoint compression K=[[1,a],[a,1]], disjoint endpoint neighborhoods have G=(1+τ)^{−1}. The one-walk term from q to p is −a s_q/(1+τ)². Its square-root integral has derivative −a/2, since π^{−1}∫_0^∞τ^{−1/2}(1+τ)^{−2}dτ=1/2 (substitute τ=tan²θ). Thus a single s derivative can connect arbitrarily distant boxes. Even if a is exponentially small in separation, that spatial gain has to be retained in the proof; counting one added box discards it. STEP55's erratum S8 adjusts a fattening factor but does not repair this false geometric inequality.

Therefore B2_55 is right to retract its own earlier §4.3 sufficiency sentence. Weighted long-jump and parameter-dependence estimates are necessary parts of a repaired route; this review does not certify any repaired CX theorem.

### R8 — CONFIRMED: J7 correctly leaves the premise list NOT-VERIFIED

**Attaches to:** `L/B2_55.md:220–226,347–350`, `(P2)` / `(P4)` / `J7`; `L/STEP55.md:443–451,773`, `Proposition 1S-k` / `I1 row`; `L/PROOF.md:5748–5759`, `Hessian of E_i^{NA}` and `E_i^{NA} is defined by minimising the lower levels`.

**Claim status: GAP for the advertised complete premise list; OPEN for the missing identification in this review.** Proposition 1S-k itself lists the per-block covariant PG transfer, while the proposed I1 row drops it. More seriously, HL and B2 concern the analytic composite critical value E^cb_k. The actual N5-sf_i consumer concerns a minimum-defined E_i^{NA}. Full stationarity, a slice contraction, and the Hessian identity identify a local branch and its derivatives; they do not exclude a competing minimizing branch or prove equality with the recursive minimum tower. The located source expressly says that N5-sf_i presupposes the minimizer and its regularity/locality.

The bridge is not established by defining E^cb_k to be the main term in a new convention: that changes the object unless the downstream RG construction is also proved to use it. Thus B2 can be removed from the **HC estimate for E^cb_k on a small global chart**, but this does not remove the min-tower/consumer bridge from one-step positivity or establish the full I1 row. This is the most dangerous unverified item: silently transporting the bankable Hessian estimate to a different action would defeat the whole claimed critical-path shortening.

### R9 — CONFIRMED within its arithmetic scope: b2_55_1 discriminates, but cannot certify the analytic inputs or the printed upper bound

**Attaches to:** `L/checks/b2_55_1_criteria.md`, `Gate A`, `Gate D`, `Gate E`, `Overall`; `L/checks/b2_55_1_lattice.py:80–86,94–108,124–147`; `L/B2_55.md:255–271`, `Check record`.

I executed the existing script's predicates in memory under Python 3 after removing output-formatting statements and replacing diagnostic float conversions by Fraction. No predicate, loop range, or rational expression was changed, and no extra file was written. This is a reproduction check, not the independent proof. Result: A=True, A-ctl=True (240 cases, 64 control witnesses), D=True, D-ctl=True, E=True, E-ctl1=True, E-ctl2=True, overall=True. The separate rational comparison of mbar against the printed 1.666219·10⁻⁴ returned False (R4).

Gate audit:

- **A can fail.** It constructs torus distances and finite sums separately from the infinite-grid closed form. Alternating Taylor terms decrease for 0≤x≤1/2; odd/even truncations enclose e^{−x}, outward dyadic rounding preserves the enclosure, and squaring positive interval endpoints preserves it. The interval comparisons are conservative rather than vacuous. The factor-two-dropping control has explicit witnesses; for example at μ=1,h=1,T=5, S=1+2/e+2/e²>2. To certify this without decimals, the exponential series gives e<87/32: the sum through n=6 is 1957/720 and its remaining tail is ≤1/4410, whose sum is <87/32. Then 2/e+2/e²>64/87+2048/7569=7616/7569>1.
- **D can fail.** The rational upper rate is independently compared to 36,000,000, and the obsolete rounded rate fails. But the **printed decimal** is not a predicate anywhere. Altering that output could never affect overall; R4 is exactly a statement this gate cannot decide. Also the implication m_Y≤ln 2/4160 is inherited from the named rate bound, not derived by the script.
- **E1/E2/E3 can fail arithmetically.** They evaluate a j-indexed sum against a reindexed expression, a geometric bound, and the STEP55 exponent-shift ratio. For example at k=1,L=3,σ=1 the true mismatch sum is 9 and the printed STEP55 sum is 1/3, ratio 27=L^{2+σ}. This directly detects the stale exponent. It does not prove a field estimate or identify its constants.
- **E-ctl1** tests the boundary exponent producing kL^{2+σ}; at k=60 its ratios to the sharp-weight bound are exactly 120,240,360,120. **E-ctl2** merely checks growth of the already substituted expression 9^k; 9^6=531441<10^6<4782969=9^7. It is a valid arithmetic control, but is not an independent test of the Wilson spin estimate or an actual background-map derivative. Neither E control can decide whether the analytic hypotheses feeding the exponent model are true.

The universal lattice sum and geometric-series proofs in R1/R3, rather than the finite parameter grid, are what establish the universal arithmetic statements. No gate in this script tests (H1), (H2)_μ, (H3)_μ, full CCP stationarity, the complex Cauchy domain, the min-tower bridge, or PG transfer. The criteria and source disclose most of these limits correctly.

**Check artifacts.** The three full SHA-256 digests reproduce the source's abbreviated hashes:

    criteria  3b0d67c617530f96c2c4923ab1d9745a45b2c5d7905dba79ddba16e84e64bf89
    script    1c7792e7f07d7b9fabfcb15743ac64366841dbeefbba7698d75730745a9b8cda
    output    68f570044b8e794d44fb0941db0dcb79ad6d16d30b9e2e6f43629f2a7cd6135b

The recorded stderr file has length zero. These establish present artifact identity; they do not establish historical pre-registration timing. The recorded chronology is NOT-VERIFIED here.

### R10 — REFUTED literally, repaired by its intended range: the spin “iff” omits a sign restriction

**Attaches to:** `L/B2_55.md:247–249`, `if (B2) were only available with a weight` and `k-uniform iff a_0 = 0`.

For the displayed sequence L^{2a_0k}, with L>1, uniform boundedness in k is equivalent to **a_0≤0**, not a_0=0 over unrestricted real exponents. The exact witness a_0=−1 gives L^{−2k}≤1. If the intended comparison is explicitly restricted to weaker weights a_0≥0, the file's equality condition is correct. This is a missing quantifier, not a counterexample to the sharpness theorem or to the claim that a positive loss at level zero breaks this particular majorant.

### R11 — CONFIRMED bookkeeping; analytic Route 1 remains NOT-VERIFIED

**Attaches to:** `L/B2_55.md:43–58,93–99,199–215`, symbols, rate/radius choices and `The smallness is on ε only`; `L/STEP55.md:103,173–174,492–496`, distinct constants.

| Symbol/object | Pin used in this review | Disposition |
|---|---|---|
| C_0 | B2_55:53,67; BFT34_55:103–104: stationary-ball bound ||x||≤C_0s | Same object in the Cauchy row estimate |
| C_WD | B2_55:54,80; BFT34_55:118: its C_1=2e^{c_rμ}G_♯(μ)S_1 | Same object in the column estimate; distinct from STEP55's curvature constant and CX prefactor |
| C_1^{st}, c_1 | B2_55:203; STEP55:174: PG c_1=1/(3.5·10^6) | Not substituted for C_WD or each other |
| ε_B2, ε_0, ε_0(μ) | B2_55:95 | The minimum uses two distinct radii explicitly; no numerical evaluation at a stale radius was used |
| μ | B2_55:94: 0<μ<min(m_Y,m_*′) | Fixed before the chart radius; positive rate and both range clauses retained |
| κ_j versus CE rates | B2_55:93,206; STEP55:492 | Soft penalties are not the cluster-expansion κ_2 or κ_0^{CE} |
| D_bg versus D_U | R6 | Unresolved type/definition identification; no silent comparison accepted |

With μ fixed, the large constants C_B2 and C_3 are finite and independent of k,T. Choosing the chart radius afterward is a legitimate quantifier order. The mismatch exponent correction is exactly L^{2+σ}, independently verified in R9; it does not create a level-count divergence.

The spin/certificate/PG prefactors are not turned into certified numeric margins by these arithmetic identities. In particular `B2_55.md:205` uses a **plaquette-log** bound 2η+9η², while `PROOF.md`, locating string `The Wilson-row bound is 2η + 144η²`, corrects a **Wilson-row** estimate. These are different objects; this review does not transfer either coefficient to the other on the strength of a matching symbol. The plaquette-log constant and the covariant termwise bounds remain supplied assumptions of Route 1, which the source already labels ARGUED. No explicit positive chart radius for the full one-step operator is banked here.

The PROOF citations used by B2_55 for RW, N5-sf_i and BG-unif are locating strings, not numeric line claims. They locate the intended statements in the current bounded reads above; no unsupported line-drift finding is asserted.

## Summary table

| Reviewed item | Review verdict | Claim disposition / correction |
|---|---|---|
| B2 Schur kernel, C_B2 and all k,j,T quantifiers | CONFIRMED | CONDITIONAL on the stated analytic/weighted inputs; unchanged constant |
| WD-only constant C′_B2 | CONFIRMED | CONDITIONAL; both sums of the same block kernel give the stated constant |
| E1 stationary-value identity / E2 gauge nullity | CONFIRMED | PROVEN from full stationarity and gauge invariance; no positivity or induction |
| Literal minimizing-extension identification away from zero | NOT-VERIFIED | Stationary evaluation is sufficient; minimization needs an additional argument |
| T3 sharpness in every tangent gauge representative | CONFIRMED | PROVEN for the positive quadratic chain |
| Spin “iff a_0=0” without a_0≥0 | REFUTED | Correct unrestricted condition a_0≤0 |
| 99/97 chart factor | CONFIRMED | CONDITIONAL on 2max(ε,C_0ε)≤1/50 |
| HL, explicit C_3, global-coordinate lower bound | CONFIRMED | CONDITIONAL on the same complex weighted package and completed C_E; independent of B2 |
| Literal identification of D_bg with STEP55's needed operator | NOT-VERIFIED | Define the 1-form→2-form operator; the explicit P_bg repair is verified conditionally |
| J6: reduction to HC_k+B2 / written CX theorem | REFUTED | J6's rejection CONFIRMED; locality and an actual repaired CX theorem remain necessary |
| J7: complete I1 premise list | NOT-VERIFIED | J7's caution CONFIRMED; PG and E^cb↔minimum-action identification are missing |
| b2_55_1 predicates and supplied artifact hashes | CONFIRMED | Reproduced exactly within arithmetic scope; chronology NOT-VERIFIED |
| ln 2/4160≤1.666219·10⁻⁴ | REFUTED | Replace upper endpoint by 1.666220·10⁻⁴, or keep exact ln 2/4160 |
| Erratum on 1.67·10⁻⁴; ≥36,000,000 | CONFIRMED | Old rounded factor =1000334027889/27889<36,000,000; exact-rate factor is between 36,031,343 and 36,031,344 |
| Route 1 term bounds and full one-step positivity | NOT-VERIFIED | ARGUED / CONDITIONAL obligations remain; no unconditional closure |

## Exactly what may be banked

1. **The conditional Theorem B2 exactly with its stated C_B2, ε_B2, ℓ² norms, all k≥1,T≥3,0≤j<k, and μ range; also its WD-only variant.** Retain (H1), the assembled (H2)_μ and the actual (H3)_μ implication as explicit supplied prerequisites. This review does not establish their upstream availability.
2. **The stationary-value Hessian identity and gauge-representative freedom**, under full stationarity/GI, plus **the trivial-background sharpness theorem**, the torus lattice-sum lemma, and the geometric-sum calculations with the stated quantifier correction. The 99/97 transfer factor is bankable on the additionally reduced radius.
3. **HL's conditional ℓ²-operator Lipschitz estimate with the printed C_3 and the global-coordinate lower bound**, with the same-link-completed C_E. Together with the explicit P_bg definition above it also gives a conditional left-chart plaquette-form lower bound, without B2, a nonlinear covariant certificate, or finer-level induction.
4. **The exact arithmetic reproduction and corrected rate enclosure**, and **the negative dependency findings**: positivity/B2 do not supply CX locality; the written CX implication fails; PG and the minimum-tower identification remain separate obligations.

**Do not bank an unconditional (HC_k) consumer identification, full level-≥1 one-step positivity, a repaired cluster expansion, an off-global-chart extension, or E^cb_k=E_i^{NA}. The single most dangerous unverified step is the last identification: every verified Hessian estimate here concerns E^cb_k, while the downstream minimum-defined action has not been proved to be that object.**
