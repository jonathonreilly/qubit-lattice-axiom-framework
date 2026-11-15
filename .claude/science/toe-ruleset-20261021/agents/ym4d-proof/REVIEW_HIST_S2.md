# REVIEW_HIST_S2: hostile review of lane D session 2 (HIST.md §13-§18 and the [RH1-fix] changes in §2-§12)

Reviewer: an independent agent that wrote none of HIST.md or its checks. I edited no other file. No commits, PRs or pushes.

Inputs:
- REVIEW_HIST_S1.md (all; the format and fixes H-1 to H-12).
- HIST.md l.100-1106 (all of §2-§18), diffed against REVIEW_HIST_S1's line references using HIST_LOG.md (all 66 lines).
- FLOW.md §3 (l.109-173, incl. §3.1, Def F-strip, Def F-g, F-Π, F-id), §4 (l.174-195), §5.1-§5.2 (l.196-228, F-tree).
  Read-only.
- LINEAR_PACKAGE.md §1.2-§2 (l.64-162: S4', Q_root = Q_str - d∘h, Setting SC, Lemmas 2.2, 2.4, 2.7 E-low, Theorem 2.6
  N2-E).
- PROOF.md Lemma NA-alg (l.2920-2955) and Lemma A1-NA(1) (l.3968-4030).
- checks/h5_criteria.md, h5_cone_and_dM.py, h5_out.txt, h5_time.txt, h5b_diag.py, h5b_out.txt, h5b_time.txt; mtimes. All
  re-run (below), plus one reviewer side-check.

Scratch work (instrumented copy, wrapper, re-run outputs) is in the scratchpad directory `revhist2/`.

---

## Bottom line

- **All twelve RH1 fixes are applied, and applied correctly.** H-1 is done properly. G_k's U_{k+1}-dependence is now
  global. (H-Mayer^J) is a whole-lattice Mayer expansion of small two-field activities, with an explicit per-cube bound
  and decay. Three nits remain (wording or constants only): N-1 to N-3 below.
- **Lemma HF: CONFIRMED (one wording fix).** I re-derived every constant of (iii). The report to FLOW is right, and it
  understates the point. On the ε_1-domain, κu·d(M) is O(u) per link, not small. So FLOW's Γ_k, which puts Σlog𝒩'_1 in
  the "u-independent" one-loop functional, is mis-assigned for N ≥ 3, not just imprecisely worded. The tree tower has to be
  𝓔_k (φ), as HIST uses, not 𝒯_k (k̃).
- **Lemma E-loc: CONFIRMED.** The cone overlap is exactly ≤ 24 at every depth. Cones are footprints of P's four corner
  blocks: they nest downward but do not grow with depth in level-k units. So Σ_PE_𝒞(P) ≤ 24E(chain), with no
  depth-dependent factor. I re-derived steps (1)-(6). One hypothesis is missing: the torus side must be ≥ 3, so that cones
  do not wrap (A1-NA(1) states the same).
- **Theorem CLS-red: CONFIRMED as CONDITIONAL ⇐ (AE).** Step β is right: ribbons stay in the cone, the NA-alg G-bound holds
  in operator norm, and the KQ dichotomy closes. The large-field part does come "for free". It is a standard ε-regularity
  argument: small aggregate cone energy forces every level of the cone into (AE)'s regime, and large cone energy pays for
  itself through s ≤ 2. So the claim is sound, not an overreach.
  - But (AE) is not a "smaller" (CLS-NA). It is local and pointwise, so logically it is neither weaker nor stronger than the
    global (CLS-NA). Its domain is the perturbative regime, and it contains the whole depth-uniform non-abelian
    linearisation problem (a lattice multiscale Uhlenbeck gauge theorem [inference]).
  - (AE) is also stated with a needlessly strong constant, (1 + C_AEε)·N·C_loc. Any depth-uniform constant suffices (fix
    S2-5).
- **(I_k^E): GAP in the statement (two definitional holes).** It is not yet "precise with every quantifier".
  - (a) The local density 𝓔_{k,x} is defined only when U is small-field on the whole torus, not on Λ_k.
  - (b) The polydisc 𝔇_α(X) is defined in ONE local gauge on X with g-independent radius ~ε_1. For polymers of diameter
    ≳ 4/c it does not contain the ε_1-domain (Stokes forbids it), so the sup bound does not control the actual
    configurations.
  - (d) It also omits the kernel normalisation factor Π_c𝒩(M̄_c(U_k))⁻¹.
  - The consistency items (c1)-(c5) are fine.
  - So target S2 is MET-WITH-FIX, not MET.
- **h5: honest.** B3's FAIL is recorded and stands, and h5b is labelled post hoc. The criteria predate the script by 94 s.
  The re-run reproduces every stored line (below). Two small undisclosed criteria/script mismatches are harmless (A4's 12
  against 24; no Newton/BFGS polishing).
- **Corrected session-2 tally: 2 PROVEN-HERE (HF, E-loc) / 1 CONDITIONAL (CLS-red) / 1 HYPOTHESIS with GAP ((I_k^E)) /
  1 OPEN ((AE)).** That is the claim, except that (I_k^E) carries a GAP. There are 0 GAP or WRONG among counted items.
  The whole-file tally of 7 / 3 / 6 / 3 + 1 HYPOTHESIS stands.

---

## Priority 1. The twelve RH1 fixes

| Fix | Where | Verdict |
|---|---|---|
| H-1 global G_k; (H-Mayer^J) restated | §2 l.120-129 (struck sentence + replacement); §4 Remark l.265-269; §6 l.372-380; §8 l.631-639; §12 l.771-772 | CONFIRMED |
| H-2 (D1-c) broadened; (I_k^E) named; (P4), (H-w)(b) re-based; coupling shift vs 𝓔_k | §6 l.437-450; §7.4 l.538-540; §7.5 l.582-585, l.589-601; §8 l.646-652; §10 l.718-720, l.736-737; §14 | CONFIRMED (the statement it points to has a GAP, see Priority 2) |
| H-3 (SF^J); H-pos^J (iii) wording | §6 l.358-363; §8 l.649-650 | CONFIRMED |
| H-4 RS-joint in-history ARGUED | §7.3 l.521-525 | CONFIRMED |
| H-5 TS_K on Δ^{in}_{*,n}, uncounted | §7.6 l.604-615; §11 l.756 | CONFIRMED |
| H-6 Den^J_B > 0 via U_{k+1} ≡ 1 | §4 l.224-228 | CONFIRMED |
| H-7 F1 line; REVIEW_S18_S19 cited; R1_Λ = G5; collar cost listed | §5 l.308-312, l.322-324, l.335-344; §8 l.643-645 | CONFIRMED-WITH-FIX (N-1) |
| H-8 CF scope | §6 l.407-412; §10 l.714; DAG l.748 | CONFIRMED |
| H-9 "linear" only for ε_1 ≤ 256Nδ_0 | §3 l.152-153, l.183-186; §10 l.712 | CONFIRMED-WITH-FIX (N-2) |
| H-10 relocated, not removed; §10 item ARGUED | §6 l.365-368; §8 l.654-655, l.676; §10 l.706-710 | CONFIRMED |
| H-11 footprint defined; collar-bad sentence; (H-w)(c) fragility | §6 l.418-421; §7.1 l.466-468; §7.4 l.543-546 | CONFIRMED-WITH-FIX (N-3) |
| H-12 tally 5/2/6/3; "new in kind" | §8 l.678-681; §11 l.750-764 | CONFIRMED |

**H-1 in detail (the review's priority).** The restated (H-Mayer^J)_k (l.631-639) has all the required parts:
- ρ_x := every stage-(k-1) remainder ℛ^J_x and every re-extracted polymer of (W1-ret'^J)_{k-1} that reads level-(k+1)
  links, at every cube;
- two-field activities in (U_k, U_{k+1}) (after (SF^J)_{k-1});
- the bound (Ce^{-a''_J/g_{k-1}²})^{#cubes}e^{-κ'd} with κ' > 3κ_0 + 3;
- a Mayer expansion over the whole lattice, jointly with CL^J's clusters;
- CL^J (c)-(e) kept up to 1 + O(e^{-a''/g²}) per cube.

The last item is where the joint activity (a Mayer polymer overlapping int(B) sits inside the int(B) integral) is
absorbed. It is stated as part of the hypothesis, which is the honest place for it. CL^J (a)'s hypothesis "explicit near
B" is now defined (l.127) and correctly flagged as failing after stage k - 1 (l.127-129, l.771-772).

**R1_Λ as G5's R1-loc (l.335-339): CONFIRMED.** The sample-dependent Λ' argument is the one REVIEW_HIST_S1 gave. The
added clause, "the (H-ch)^J indicator is constant on the chart ball by the C^J_♮ line", is right: C^J_♮ is chosen so that
the whole chart ball satisfies the hypotheses.

**Nits (binding, wording or constants only).**
- **N-1 (l.341, l.580).** The missing-shift cost is |δβ|·Σs, and s ≤ 2. So the factor is 12L⁸ per cube, not 6L⁸. That is
  the review's (2w_* + 1)⁴·12L⁸|δβ^J_k|. (c4) at l.921 already uses 12L⁸. Make l.341 and (P2) l.580 agree.
- **N-2 (l.168).** The Lemma RS-lin title still says "with a LINEAR threshold". Add "(linear for ε_1 ≤ 256Nδ_0)".
- **N-3 (l.420-421).** "Equivalently the union over levels i < k of the level-i regions W_P^{(i)}" mixes levels. Say "the
  level-0 descendants of W_P^{(i)} (all equal to W_P^{(0)})", or drop the "equivalently".

---

## Priority 2. (I_k^E) (§14.1, l.842-869): GAP (statement), consistency items CONFIRMED

### What is right
- The main term is u_k·𝓔_k with u_k FLOW's β-functional coupling. The coupling is not silently changed: β[𝓔_k] = 1 =
  β[𝒯_k] (see Priority 3), so Def F-g's u_k is the coefficient of either tower.
- The polymers carry the right content. They have β = 0, a per-cube bound E_0 that is O(1), g-independent and not small
  (accumulated one-loop remainders), O(g²) higher loops and O(e^{-a/g²}) returned terms. There is no marginal part.
- The two-field form (d) is the (SF^J) interface H-3 asked for.
- (I_0^E) holds trivially.
- This is consistent with F-tree. F-tree is a statement about the Hessian H_k, and 𝓔_k has the same Hessian (d = O(y⁶)).

### GAP S2-1: the localised main term (a) is not defined on Λ_k (l.848-851)
- 𝓔_{k,x} is "the energy terms of the tree minimiser chain Φ_{·←k}(U) lying over x, defined on the small-field domain by
  (SF-bg) … so that Σ_x𝓔_{k,x} = 𝓔_k whenever U is small-field on the whole torus".
- The tower minimiser is a global object. On a configuration that is small-field only on Λ_k (large fields on Ω^c_k) it
  reads U on Ω^c_k, where (SF-bg) gives neither uniqueness nor analyticity. So 𝓔_{k,x}, x ∈ Λ_k, is undefined exactly in
  the case (I_k^E) is for.
- The assignment of terms that straddle cubes is also unspecified.
- **Fix.** Define the main term through a localised tower. One option is the minimiser on Λ_k with the Ω^c_k-side data
  frozen (or replaced by a reference), as Balaban's localised background fields do. Then put the difference from the
  global tower into the polymers, with its decay e^{-κ_p dist(x, Ω^c)} from (SF-bg)'s exponential locality. State the
  assignment rule (e.g. each term to the level-k cube containing its lexicographically first vertex ancestor).
- (c4)'s per-cube constant C_𝓔 and (c5)'s self-reproduction both inherit this. (c5) is exact only for the global tower.

### GAP S2-2: the analyticity domain (b) does not contain the ε_1-domain (l.852-856)
- 𝔇_α(X) := {|B^a_b| ≤ α_E in normalised Lie coordinates of a local gauge on X}, with α_E ≥ cε_1, and the bound is a sup
  over 𝔇_α(X).
- Take a constant-curvature field (Proposition CF's type) with every level-k plaquette of angle ~ε_1, on a polymer X that
  contains an m × m square. Stokes gives |flux| ≈ m²ε_1 ≤ (perimeter)·max|B| = 4mα_E. So in ANY gauge on X the links
  reach ≳ mε_1/4.
- For m > 4α_E/ε_1 (≥ 4c) the configuration lies in the ε_1-domain but in no 𝔇_α(X). So the bound (b) says nothing about
  E_k(X; U) at actual small-field configurations on large polymers. This is HIST's own (CS-F2) phenomenon (§15.5),
  reappearing in (I_k^E).
- FLOW's F-Π uses the same polydisc (FLOW l.143-145, "other links at 1"). That is fine for Taylor coefficients at V = 1
  (β), but not for a sup on the ε_1-domain.
- **Fix.** Make the domain gauge-covariant and local. For example: "U ∈ 𝔇_α(X) iff for every level-k cube z ⊂ X there is a
  gauge on the bounded neighbourhood N_R(z) in which every link of N_R(z) is within α_E of 1 (complexified)". Charts
  would overlap, with the polymer an analytic function on each chart. Alternatively, state analyticity in plaquette and
  residual variables. Either way the per-cube bound then has to be proven chart by chart, which is what Balaban's
  small-field gauge fixing does [inference; CMP 95-99 not read here].
- The same remark applies to (SF-bg) as HIST consumes it. FLOW §4 states (SF-bg) on "a complex neighbourhood of the
  trivial field (in normalised Lie coordinates)", which is not the ε_1-domain on large regions. So (I_k^E)(a)'s appeal to
  (SF-bg) on the small-field domain needs the same local-gauge form.

### GAP S2-3 (minor): (d) omits the kernel normalisation (l.861-865)
- K_k = Π_ce^{-κu_kφ}/∫e^{-κu_kφ_{M̄_c(U_k)}} ((3.0)). The denominator is a field-dependent function of U_k: O(1) per link,
  with a quadratic part.
- It is neither in the main term nor among the listed polymers of (d). It must be listed: it feeds Γ_k's 𝒩'_1 term and
  hence u_{k+1} in (c5).
- **Fix:** add "-Σ_clog∫e^{-κu_kφ_{M̄_c(U_k)}} (a function of U_k, (b)-class with E_0; not β-free)" to (d).

### Consistency items
- **(c1): CONFIRMED** (Priority 3).
- **(c2): CONFIRMED.** The quadratic part of Σs is ½||dB_k||², and that of 𝓔_k is Setting SC's E_k. This gives
  [2c_E, 2C_E(1 + κ)] = [0.0081, 4.8·10⁸] (c_E = 0.004069, C_E = 1.2·10⁸, LINEAR_PACKAGE l.148, l.154). Checked.
- **(c3): CONFIRMED as ARGUED.** "FLOW's renormalised remainder and (D1-c) agree: the β = 0 tree part must stay in the
  main term" is the right synthesis.
- **(c4): CONFIRMED-WITH-FIX.**
  - The arithmetic is right (12L⁸ + L⁴C_𝓔).
  - Sign: adding +δβΣs to log e^{-S} is u_k → u_k - δβ, not "+δβ" (l.920). This is cosmetic.
  - C_𝓔 needs GAP S2-1's localisation.
- **(c5): CONFIRMED** (elementary identity). The "Laplace method gives u_k𝓔_{k+1} + Γ_k + …" part is ARGUED and inherits
  S2-1 and S2-3.

**Verdict on target S2:** MET-WITH-FIX. The statement is right in content, and the five consistency items are each
correctly labelled. But its domain (b) and its main term (a) are not yet defined on the configurations it must cover.
The pre-stated "Not success" clause ("polymer bound not per-cube g-independent on the ε_1-domain") is formally avoided,
but substantively it is met until S2-2 is fixed, because the per-cube bound is over a set that misses most of the
ε_1-domain on large polymers.

---

## Priority 3. Lemma HF (l.873-890): CONFIRMED-WITH-FIX (wording); FLOW report CONFIRMED and strengthened

- **(i).** k̃ = N⁻¹[tr P - Re tr(V⁻¹M)] (since V⁻¹WP = V⁻¹M), and φ = N⁻¹[Re tr(W_0⁻¹M) - Re tr(V⁻¹M)] ((3.0), l.134). The
  difference is d(M). d ≥ 0 by von Neumann (|Re tr(YP)| ≤ tr P for unitary Y). Checked.
- **(ii).**
  - W_1 = We^{-iα/N} has det 1, and Re tr(W_1⁻¹M) = cos(α/N)tr P ≤ Re tr(W_0⁻¹M).
  - tr P ≤ N because ||M|| ≤ 1, and 1 - cos t ≤ t²/2.
  - The bound holds for any branch of α. The stated (-π, π] is the best choice.
  - **Fix (wording, l.878, l.883-884):** "d ≡ 0 for N = 2" holds for M a non-negative combination of SU(2) elements, which
    are real multiples of SU(2) elements (quaternions). That is the case for every M̄_c. It is false for a general 2 × 2
    contraction. The proof says this; the statement should too.
- **(iii).** Re-derived against NA-alg (a) (PROOF l.2922-2949).
  - G = H + iθ1, and α = Σarg(h_j + iθ) with |arg| ≤ |θ|/(1 - 18.4y²) ≤ 1.05|θ| (y ≤ 1/20).
  - Im tr R_X: only odd m ≥ 3 contribute (tr X^m is real for even m, imaginary for odd m, X anti-Hermitian). The bound is
    √N(sinh|X| - |X|) ≤ 1.01√N(3y)³/6 = 4.55√Ny³.
  - |Im tr E| ≤ √N(sinh y - y) ≤ 0.17√Ny³.
  - Im tr(XȲ) = 0, so the cross term is ≤ 5.23y²·1.03y + 3y·0.53y² = 6.98y³.
  - Total (4.8√N + 7)y³. At N = 3: [1.05·15.31]²/18 = 14.36 ≤ 14.4. All checked.
  - The bound is very loose: h5b measures |α|/y³ ≤ 0.010 against 16.1.
- **Consequence (l.891-896): CONFIRMED given F-tree.**
  - k̃ ≥ φ termwise, so 𝒯_k ≥ 𝓔_k.
  - The upper bound evaluates 𝒯_k's defining minimum at 𝓔_k's minimiser chain.
  - The Hessians at 1 are equal (d is sextic), and F-tree is a Hessian statement (FLOW l.122-125, l.210-225). So
    β[𝓔_k] = 1.
- **The FLOW report (l.897-905): CONFIRMED, and stronger than HIST says.**
  - FLOW §3.1 (l.115) writes 𝒩'(P) := ∫exp(-κuN⁻¹Re tr((1 - X)P))dX with X := W⁻¹V "Haar". For det W ≠ 1, X ranges over the
    coset W⁻¹SU(N). So 𝒩' depends on W (through det W), not only on P, and Lemma HF (i) gives log 𝒩' = -κu·d(M) +
    log∫e^{-κuφ}. The "no power of u" sentence (l.118) is false for N ≥ 3.
  - **Strengthening.** HIST calls this harmless because d has β = 0. That is true for the coupling and the tree lemmas
    (F-tree, F-bg, F-ren). But FLOW §5.1 (l.199-203) puts Π_c𝒩'(P_c(U))⁻¹ into the U-integrand as an O(1) factor, and puts
    Σ_clog𝒩'_1 into Γ_k as "the u-independent factor". For N ≥ 3 that factor contains e^{+κu·d(M̄_c(U))}, a function of
    the integration variable with coefficient u.
    - On the ε_1-domain contour spreads are up to A_dε_1, and d is up to α²/(2N²) = O(1). So the term is O(u) per link:
      not one-loop-sized, and not per-cube bounded.
    - It shifts the tree minimiser, from 𝒯's to 𝓔's.
    - This is exactly the (c3) phenomenon. A β = 0 tree term must stay in the main term. So FLOW's tower must be 𝓔_k (φ,
      SU(N) maximiser) wherever per-cube polymer bounds ((SF-g)) are claimed. HIST's choice of 𝓔_k is the right one, and
      this should be part of the report.
  - **Report text (for the lead to pass on; FLOW.md not edited here):** "§3.1: 𝒩' depends on det W; log 𝒩' = -κu·d(M) +
    log∫e^{-κuφ}. Replace k̃ by φ in Def F-strip and §5.1 (or move κu·d into the tower). β, F-tree, F-bg and F-ren are
    unchanged, since d = O(y⁶)."

---

## Priority 4. Cones and Lemma E-loc (§15.1-§15.2, l.940-983): CONFIRMED (one hypothesis to add)

### Cone geometry
- **Nesting (l.948-949).** A level-i site in W_P^{(i)} has its level-k ancestor among P's corners, and so do all its
  descendants. So W_p^{(j)} ⊂ W_P^{(j)} and 𝒞(p) ⊂ 𝒞(P). Correct.
- **Overlap (l.950-951): the depth question.**
  - Every cone is the set of terms whose vertices have level-k ancestors among P's four corners. Its "size" is always four
    level-k blocks, at every depth. Cones grow downward (L^{4(k-i)} level-i sites per block), but they do not spread
    sideways in level-k units.
  - A term with ancestor set A lies in 𝒞(P) only if one fixed element a ∈ A is a corner of P. A d = 4 site is a corner of
    exactly 24 plaquettes (6 planes × 4 positions).
  - So **every term at every level is in ≤ 24 cones, independent of k**, and Σ_PE_𝒞(P) ≤ 24E(chain). No depth-dependent
    factor appears.
  - Terms whose ancestor set is not inside one plaquette's corner set (e.g. a fine plaquette straddling three level-k
    blocks in a non-planar way) are in NO cone. That only helps the inequality direction used.
- **Missing hypothesis.** On a level-k torus of side ≤ 2, the four corner blocks are not distinct (or the cone wraps).
  Then W_P is not a box, the overlap count changes, and in the non-abelian use (§15.4) flat non-trivial holonomies could
  live in the cone.
  - **Fix S2-4:** assume level-k torus side ≥ 3, as A1-NA(1) does ([R56-fix], PROOF l.3974-3975). HIST's "uniformly in
    T" should read "for every torus of side ≥ 3".
  - The coarse-torus top level K is where this bites.

### Lemma E-loc, line by line
- **(1).**
  - d∘Q = d∘Q_str follows from Q = Q_str - d∘h (LINEAR_PACKAGE l.72).
  - Q_str∘d = d∘avg: the leg sum of a gradient telescopes, and B(X + e_μ) = B(X) + Le_μ.
  - Hence Q_str∘Q = Q_str∘Q_str - d∘avg∘h, and by induction d∘Q^m = d∘Q_str^m = d∘Q_str^{(L^m)} (Lemma 2.4).
  - The residual representation B_k = Q^kB_0 - ΣQ^{k-1-i}r_i follows from B_{i+1} = QB_i - r_i. Correct.
- **(2).** This is the m-step version of Lemma 2.2 (i) (LINEAR_PACKAGE l.125), via (1). Checked numerically (h5 A1).
- **(3).**
  - |∮_{∂sq_y}B_0|² ≤ n²Σ_{sq_y}|dB_0|².
  - A plaquette of P's plane lies in ≤ n·n squares (its transverse coordinates are fixed by y's).
  - |Σ_y∮_y|² ≤ n⁴Σ_y|∮_y|².
  - Together these give |d(Q^kB_0)(P)|² ≤ Σ_{R_0(P)}|dB_0|². The constant is exactly 1.
  - The vertices of sq_y lie in the four corner blocks: the blocks are contiguous along μ and ν, and transverse coordinates
    are those of y. Correct.
- **(4).**
  - A boundary circulation of 4n links has |∮|² ≤ 4nΣ.
  - A link lies on ∂sq_y for ≤ 2n values of y. This is generous by 2; h5 A2 measures n.
  - n^{-4}·8n² = 8L^{-2m}. Correct.
  - The decay is real: a link-level source's flux through a big square is a boundary term spread over n⁴ positions.
- **(5).** Cauchy-Schwarz with weights (1, L^{-m}) gives (1 + L/(L - 1)) = (2L - 1)/(L - 1), and
  8L^{-m}ρ_m² ≤ (16/κ_-)(κ_i/2)ρ_m². So C_loc = (5/2)·16 = 40 at L = 3, κ ≡ 1. Correct.
- **(6).** Overlap 24 gives E_k ≥ ||dB_k||²/960. This is weaker than E-low's c_E = 0.004069 but independent of it, and
  consistent with it. Correct.
- **Verdict: CONFIRMED (PROVEN-HERE, counted), with S2-4.** The "sup form", in which every coarse plaquette is controlled
  by its own cone's energy at every depth, is genuinely new relative to the Fourier proof. It is the right input for
  ε-regularity.

---

## Priority 5. (AE) and Theorem CLS-red (§15.3-§15.5, l.985-1050)

### Theorem CLS-red, line by line: CONFIRMED as CONDITIONAL ⇐ (AE)
- **Base i = 0.**
  - 𝒞(p) = {p} for a level-0 plaquette, and |1 - U|²_HS = 2Ns.
  - ||1 - U||_op ≤ √(2Nη_E) ≤ ½ gives max angle ≤ 2arcsin(¼).
  - Then |X|² ≤ (1 + φ²/6)·2Ns (A1-NA(1) step 6, PROOF l.4017-4021) ≤ C_* = 80N. Correct.
- **(α).** Nesting gives E_𝒞(p) ≤ E_𝒞(P) < η_E, and the induction hypothesis (all chains, all lower levels) gives
  |log U_i(p)|²_HS ≤ C_*η_E ≤ ε². Correct.
- **(β), the step the brief flags.**
  - *Ribbons stay in the cone.* For c with both endpoints in W_P^{(i+1)}, its two level-i endpoint blocks are in W_P^{(i)}.
    Its S4' contours T^σ_y = P^σ(c_X→y)S_yP^σ(c_Y→y+Le_μ)^† (LINEAR_PACKAGE l.66-67) use axial moves inside one block and
    one straight leg between the two blocks, and S_c is straight between the centres. The union of the two blocks is a
    coordinate box, and the RS (R1) ribbon (1 × L rectangles at the off-axis steps) stays in it. So every ribbon plaquette
    has its vertices in W_P^{(i)} and is covered by (α).
    - Add this one sentence (fix S2-6). HIST's parenthesis "c's two endpoint blocks lie in W_P^{(i)}" is the conclusion,
      not the argument.
  - *Lasso.* ||1 - Π_jg_jh_jg_j⁻¹|| ≤ Σ_j||1 - h_j||, and ||1 - U_p||_op ≤ |log U_p|_op ≤ ε. So ||1 - T_1⁻¹T_j||_op ≤ A'ε
    with A' = 2A_d (two ribbons). Correct.
  - *Op-to-HS log.* |1 - g|_HS ≤ √N·A'ε ≤ ½ (implied by c'A'ε ≤ 1/20), so |log|_HS ≤ 4arcsin(¼)√N·A'ε = c'A'ε. Correct.
  - *NA-alg.* M̄_c = avg_jT_j, so T_1⁻¹M̄_c = avg_je^{Y_j}, and W_0 is left-covariant. NA-alg's proof gives
    ||G - 1|| ≤ |Ȳ - X_0| + |K(X_0)| ≤ 18.4y² in HS (PROOF l.2949), hence also in operator norm. **This bound includes θ**
    (it bounds G - 1, not only H - 1), which is what step β needs. Correct.
  - *KQ dichotomy.* φ_c ≥ x²/(2N) - 18.4y²x (KQ lower, l.157). Either x ≤ 73.6Ny² ≤ ε, or φ_c ≥ x²/(4N), and then
    κφ_c < η_E gives x ≤ √(4Nη_E/κ) ≤ ε. Correct.
- **(γ), (δ).** (AE) with C_AEε ≤ 1 gives ≤ 2NC_locE_𝒞 = C_*E_𝒞, which closes the induction with the SAME C_*. So no
  per-level constant is iterated: (CS-F1) is avoided, given (AE). s ≤ |log|²/(2N) ≤ C_locE_𝒞; otherwise s ≤ 2 ≤
  (2/η_E)E_𝒞. The overlap 24 then gives c_cl. Correct.
- **Constants.** The four conditions on ε are compatible: each is satisfied for η_E small, since ε ∝ √η_E and the last
  condition is ε ≤ 1/(73.6Nc'²A'²). η_E depends only on (N, L, κ, C_AE, ε_AE, A_d). Uniform in k. Correct.

### Does it really give the full classical (CLS-NA), large fields included? Yes, given (AE). Not an overreach.
- The mechanism is ε-regularity (as in Uhlenbeck's and Sacks-Uhlenbeck's small-energy regularity) [inference; not read for
  this review].
  - Small cone energy forces every plaquette and residual at every level of the cone to be small (α, β, by induction on
    the level).
  - Large cone energy is charged against s ≤ 2.
- The large-field configurations never need a large-field estimate, because the inequality is per-cone and the cone
  energy is an aggregate (≳ L^{4(k-i)} terms per level). This is exactly the class of bounds REVIEW_HIST_S1's H-8 said
  Proposition CF does not exclude, and CF is consistent with it (Remark (1), l.1019-1021).
- REVIEW_HIST_S1 advised against *attacking* full (CLS-NA) on cost and main-path grounds. It did not say the large-field
  case was mathematically harder. HIST §17's "revises REVIEW_HIST_S1's strategic reading" (l.1089-1092) is fair for the
  classical statement.
  - (D1-b) still needs the large-field fluctuation bound (HP-F3), as HIST says (Remark (3)).
  - (CLS-NA) stays off the main path. CLS-sf (on path, via (PLD-q)) is reduced to the same (AE), so nothing on the path got
    cheaper than (AE).

### Is (AE) precisely stated? Nearly. Three fixes.
- **S2-5 (weaken the constant; recommended, makes (AE) strictly weaker).** CLS-red needs only some depth-uniform constant,
  not (1 + C_AEε)·N·C_loc.
  - Restate: "there are ε_AE > 0 and C'_AE < ∞ (independent of k, K, T) such that (i)-(ii) with ε ≤ ε_AE imply
    s(U_k(P)) ≤ |log U_k(P)|²_HS/(2N) ≤ C'_AE·E_𝒞(P)".
  - In CLS-red put C_* := max{2NC'_AE, 2N(1 + φ²/6)} and choose η_E after C_*.
  - The proof is unchanged. The present form ties the non-abelian statement to the linear constant 40, which is a
    non-sharp upper bound (measured ≤ 3.81), for no gain.
- **S2-6.** The ribbon-in-cone sentence above.
- **S2-7 (principal log).** "|log U_k(P)|_HS" is undefined if U_k(P) has an eigenvalue -1, and (AE)'s hypotheses do not
  include P itself. State the conclusion as "U_k(P) = e^X with |X|²_HS ≤ …" (or bound s(U_k(P)) directly). Together with
  S2-4 (torus side ≥ 3), this is what makes "flat cone ⇒ U_k(P) = 1" true.
  - That is a necessary consistency of (AE), and it holds: a flat box is pure gauge, and the S4' averages of pure gauge are
    pure gauge.

### Is (AE) genuinely smaller than (CLS-NA)? In domain yes; logically no; in difficulty it is the core.
- **Logic.** (AE) ⇒ (CLS-NA) (CLS-red), but (CLS-NA) ⇏ (AE): a global sum bound does not give a per-cone pointwise bound.
  So (AE) is a *local strengthening restricted to the perturbative regime*. It is not a weakening of (CLS-NA). §17 and
  §18 should say "reduced to a local small-field statement", not suggest that (AE) is a smaller instance of (CLS-NA).
- **Difficulty.** (AE) is the whole depth-uniform non-abelian linearisation.
  - Its linear case is E-loc (proven).
  - Its non-abelian content is that the composite S4' average of a k-level chain, all of whose levels are ε-small, has a
    top plaquette controlled by the cone's ℓ² energy, uniformly in k.
  - §15.5 locates the wall correctly: the gauge on a cone of side ~2L^k. Axial gauge accumulates link sizes over levels
    (A1-NA(1) step 2's C_1 = 2c(d - 1)L grows with the box), and the per-step route needs Σφ_j < ∞ (CS-F3). Both
    diagnoses are right.
  - (MSG) + (MS-Sob) is the lattice multiscale analogue of Uhlenbeck's gauge theorem: small ||F||_{L²} on a 4-ball (scale
    invariant in d = 4) gives a Coulomb gauge with ||A||_{L⁴} ≲ ||F||_{L²}. That is a known, hard but finite theorem in
    the continuum. The lattice multiscale version is Balaban's small-field gauge fixing [inference; neither paper read for
    this review].
  - (AE) is therefore a well-posed and plausible wall, not a disguised restatement.
- **Synergy (the strategic point).** The same gauge object is needed in three places:
  - (AE) (§15.5);
  - (I_k^E)(b)'s analyticity domain (GAP S2-2);
  - (I_k^E)(a)'s localised tower via (SF-bg) on the ε_1-domain (GAP S2-1).
  One theorem, "(MSG): a depth-uniform local small-field gauge on cones / localisation domains, with link sizes controlled
  by local plaquette and residual sizes", would discharge the gauge part of all three.

---

## Priority 6. Checks h5, h5b (re-run)

### Procedure and honesty
- **Criteria predate the script.** mtimes (local EDT = UTC-4): h5_criteria.md 20:08:33, h5_cone_and_dM.py 20:10:07 (94 s
  later), h5_out.txt 20:21:41, h5_time.txt 20:22:57. The script was not touched after the run.
- **h5b is post hoc.** h5b_diag.py (20:22:57) was written after h5_out (20:21:41). It is labelled post hoc in its
  docstring, HIST §16 and HIST_LOG, and it does not change B3.
- **B3 FAIL recorded honestly.** The cause is a design flaw of the criterion (the smallest y sits at the rounding floor:
  |α| ≈ 0.01y³ ≈ 8·10⁻⁸ at y = 0.02, so d ≈ α²/18 ≈ 4·10⁻¹⁶). It is not a failure of Lemma HF. The FAIL stands as
  recorded.
- The order inside HIST (§13 at 00:07 UTC before §14) cannot be verified from mtimes. It is recorded, not checked.
- **Undisclosed criteria/script mismatches (harmless).**
  - (i) Criteria A4 compares with "12·C_loc = 480", while the proof's overlap is 24 (so 960). A4 is informational and
    measures 1.99.
  - (ii) The criteria say W_0 is found by "fixed-point iteration … followed by Newton/BFGS polishing". The script does the
    fixed-point iteration only (residual ≤ 1e-15).
  - Disclose both in HIST_LOG.
- **Scope notes.**
  - A3 tests the stronger inequality with E restricted to R_0 ∪ R'_i, a subset of the cone. That is good.
  - It uses Q_str chains. That is legitimate: with the same r_i, the Q_root and Q_str chains differ by gradients
    (Q = Q_str - d∘h) and have identical dB_k and identical cone energy.
  - h5b's y = 0.32 points are outside HF (iii)'s range y ≤ 1/20 (diagnostic only).

### Re-run
Setup:
- The numeric lock was taken by `until mkdir …/locks/numeric; do sleep 20; done`. I waited about 4 minutes for another
  holder. The lock was taken at 00:44:11 UTC and released by a single `rmdir` at the end of the wrapper (00:44:15 UTC; no
  trap, no second release).
- Load 3.45 (< 8, checked inside the lock before running), 35% free memory, nice 10, OPENBLAS/OMP/MKL/vecLib threads 1,
  PYTHONDONTWRITEBYTECODE = 1, python3 without -I, no `timeout`, sequential.

| Run | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| h5_cone_and_dM.py | OVERALL FAIL (B3 5.367); A1-A3, B1, B2, B4 PASS | 1.8 s | 134 MB | identical except timing (`diff`) |
| h5b_diag.py | α slope 3.000; d slope 5.993 / 6.000 | 0.0 s | 56 MB | identical except timing |
| reviewer copy (h5 + B5 recheck) | reproduces h5's B lines exactly (same RNG stream) | 1.5 s | 148 MB | — |

**Reviewer side-check (B5 outliers; scratch only, not a check of the file).**
- HIST (l.1069-1070) says the B5 ratios above 1 (max 1.0187) "can only be numerical [inference]". I tested this. For the
  five largest float ratios and the smallest, I recomputed W_0, tr P and α at 50 digits (fixed-point residual ≤ 10⁻⁴⁵).
- Result: d/[(tr P/N)(1 - cos(α/N))] = 1.0000000 (to 8 digits) for all six. The float value 1.0187 is rounding at
  d ≈ 5.5·10⁻¹⁵, α ≈ 3·10⁻⁷.
- So the inference is right. Moreover, **Lemma HF (ii) is an equality to 8 digits in this regime**: the maximiser is
  W_1 = We^{-iα/N} up to higher order.
- The min ratio 0.0000 is also rounding: mp ratio 0.99999998 at d = 1.4·10⁻¹⁷.

---

## Corrected tally (session 2)

| Item | Claimed | Verdict |
|---|---|---|
| Lemma HF | PROVEN-HERE, counted | CONFIRMED-WITH-FIX (N = 2 wording) |
| Lemma E-loc | PROVEN-HERE, counted | CONFIRMED (add S2-4, torus side ≥ 3) |
| Theorem CLS-red | CONDITIONAL ⇐ (AE) | CONFIRMED as CONDITIONAL (S2-4 to S2-7) |
| (I_k^E) | HYPOTHESIS | GAP (statement): S2-1, S2-2, S2-3 |
| (AE) | OPEN | OPEN, precisely named up to S2-5 to S2-7 |
| tower identity §14.0; β[𝓔_k] = 1; (c4); (c5) | PROVEN-HERE, uncounted | CONFIRMED ((c4): sign, and C_𝓔 needs S2-1) |
| (c2) | PROVEN (ledger) | CONFIRMED |
| (c3) | ARGUED | CONFIRMED as ARGUED |
| FLOW §3.1 report | imprecision, harmless | CONFIRMED; stronger: mis-assigned O(u) term for per-cube bounds |
| §15.5 (MSG), (MS-Sob) | inference | fair, labelled |

- **Session 2: 2 PROVEN-HERE / 1 CONDITIONAL / 1 HYPOTHESIS (with GAP) / 1 OPEN.** 0 GAP or WRONG among counted items.
- **Whole file: 7 PROVEN-HERE / 3 CONDITIONAL / 6 ARGUED / 3 OPEN + 1 HYPOTHESIS.** This stands. (CLS-NA) is CONDITIONAL
  ⇐ (AE) via CLS-red, and the OPEN walls are (AE), (D1-b), (H-w).
- Target S2: **MET-WITH-FIX** (claimed MET).
- Target S3: **MET in the alternative form**, as claimed: a proven reduction, the wall's linear case proven, the gauge
  identified.
- If the lead places items in PROOF.md, the main-path count from session 2 is +2 (HF, E-loc), neither on the critical path
  by itself.

## Binding fixes (next lane-D session)
1. **S2-1.** Define 𝓔_{k,x} on Λ_k by a localised tower (Ω^c_k data frozen or referenced), with the difference from the
   global tower put into the polymers. State the term-to-cube assignment rule. Re-check (c4) and (c5) against it.
2. **S2-2.** Replace the single-gauge polydisc 𝔇_α(X) by a gauge-covariant local domain (overlapping per-cube charts, or
   plaquette and residual variables). Note that FLOW's (SF-bg) needs the same form to be consumed on the ε_1-domain.
3. **S2-3.** List the kernel normalisation -Σ_clog∫e^{-κu_kφ_{M̄_c(U_k)}} in (I_k^E)(d) (field-dependent, not β-free; feeds
   Γ_k).
4. **S2-4.** Add "level-k torus side ≥ 3" to §15.1, Lemma E-loc and CLS-red ("uniformly in T" → "for every T with side
   ≥ 3").
5. **S2-5.** Weaken (AE) to an arbitrary depth-uniform constant C'_AE, and set C_* from it in CLS-red.
6. **S2-6.** One sentence in CLS-red step β: the S4' contours and the RS ribbons of c lie in the box formed by c's two
   endpoint blocks, hence in the cone.
7. **S2-7.** State (AE)'s conclusion via U_k(P) = e^X, |X|² ≤ …, or via s(U_k(P)), not via the principal log.
8. **HF wording.** "d ≡ 0 for N = 2" applies to non-negative combinations of SU(2) elements.
9. **(c4) sign.** Adding +δβΣs is u_k → u_k - δβ.
10. **FLOW report.** Add the strengthening of Priority 3: the u·d term is O(u) per link on the ε_1-domain, so FLOW's tower
    must be φ-based wherever per-cube bounds are claimed.
11. **§17-§18 wording.** "(CLS-NA) reduced to the LOCAL small-field statement (AE)". (AE) is not a weakening of (CLS-NA).
12. **Nits N-1 to N-3** (12L⁸ at l.341 and l.580; the RS-lin title; the footprint "equivalently").
13. **HIST_LOG.** Disclose the two h5 criteria/script mismatches (A4's 12 against 24; no Newton/BFGS polishing).

---

## Strategic verdict on (AE)

- **(AE) is the right wall, and it is worth attacking. It is no longer optional, because it is shared.**
  - It is precisely posable (after S2-5 to S2-7), its linear case is proven (E-loc), and the reduction to it is
    depth-uniform.
  - The gauge object it needs is exactly what (I_k^E) is missing (S2-1, S2-2). So the next real step for the main path is
    the same theorem: **(MSG), a depth-uniform local small-field gauge on cones and localisation domains**. It is not two
    separate efforts.
- **Order:**
  1. Fixes 1-13. About half a session; S2-1 and S2-2 are restatements, not proofs.
  2. **Read before deriving.** Balaban's small-field gauge fixing (CMP 95-99; axial/Landau gauges on multiscale
     localisation domains) and Uhlenbeck (CMP 83 (1982)) for the continuum ε-regularity template. The repo rule "derive
     independently, then compare" applies; do not import the constants.
  3. **The first target is the one-cone (MSG) at depth 2 with explicit constants.** In one level of the interpolation
     gauge, show |a_i - I(a_{i+1})| ≤ C_M·(local sizes) with |I(a)| ≤ (C_I/L)|a| and C_I² < L. A depth-2 check (h-type,
     SU(2), L = 3) of the non-abelian cone ratio |log U_2(P)|²/E_𝒞(P) on random ε-small chains, against the linear 3.81,
     would show whether a depth-uniform C'_AE is plausible before the multi-level induction is written.
  4. (MS-Sob) after (MSG). It is where the marginal level-0 BCH errors are controlled, and it is the delicate,
     d = 4-critical step.
- **Do not:** attack (D1-b) or the large-field fluctuation bound (HP-F3). CLS-red already took the classical large-field
  part off the table, and (D1-b) is still not consumed by RLF-step^J.
