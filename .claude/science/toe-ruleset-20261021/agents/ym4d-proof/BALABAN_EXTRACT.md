Reviewer model: claude-opus-5-5

# BALABAN_EXTRACT — T56-1 (Step 1): Balaban's background-field and propagator theorems, read directly

Worker: claude-opus-5-5 (Opus 5.5), effort max, worker role (not reviewer). Brief: scratchpad queue/step1.md +
REVIEW_BRIEF_55.md rules 1-6 and read discipline. Target: RTARGET.md §55 T56-1 (and the wall map of PLAN_S26 §4 Step 2).
Written append-only. No git. This is the only repository file this worker writes.

## PRE-STATED (written 2026-10-28T22:52:11Z, before any source was opened and before any derivation)

**Targets.**
- T-a. For CMP 102 (variational problem / background fields): the exact hypotheses (field domain, small-field
  conditions and their scale in k and g_k), the norms, the constants and what they depend on, and what is
  uniform in k, for existence, uniqueness, regularity and analyticity of the k-fold-constrained minimiser.
- T-b. For CMP 95, 96, 99: the exact statements of the propagator bounds (trivial background and general
  small-field background), the random-walk / multiscale expansion they come from, the decay rate and
  constants and their k-dependence.
- T-c. The mechanism by which constants do not compound across RG steps (what is re-derived at each k from
  scratch vs. carried inductively).
- T-d. Secondary papers CMP 98, 109, 116, 119, 122: what each states that bears on T-a..T-c, and on
  volume-uniform constants, local source insertions, symmetry (rotations / lattice symmetries), infinite volume.
- T-e. The wall map: (GAP-Z), (G♯_0-field), (N-bg)/(H-C), FLOW's H_⊥(U)^{-1}, (SPD)/(W2), the level-count factor
  -> the Balaban result covering each in the hard-constraint scheme, and the step that changes in the soft scheme.
- T-f. BAL-F3: every load-bearing PROOF.md paraphrase of Balaban found, with a verdict.

**Verdict scale for each extracted statement.** READ (statement read in the primary source, page given) /
READ-SECONDARY (read only in a legitimate secondary source such as Dimock's arXiv expositions; source and section
given) / NOT-READ (no legitimate free copy reachable; BAL-F1 recorded, nothing asserted about content).
Model-mediated fetch: the web-fetch tool returns a model-processed rendering of the page; every quotation below
is labelled with how it was obtained, and a quotation obtained only once through that channel is marked as such.

**What counts as a refutation of a PROOF.md paraphrase (BAL-F3).** The paraphrase attributes to Balaban a
hypothesis, norm, constant dependence, uniformity (in k, in volume) or mechanism that the read source does not
state, or states differently in a way the lane's argument uses. A paraphrase about a paper I could not read is
NOT-VERIFIED, never CONFIRMED. A paraphrase that matches the read source in its load-bearing content is CONFIRMED.

**Named failure modes (from RTARGET §55).** BAL-F1: paper not legitimately readable for free -> name it, move on;
never Sci-Hub/LibGen; pay nothing; no PDF saved to disk. BAL-F2: Balaban's k-uniformity depends on the hard
constraint in a way the soft scheme cannot reproduce -> recorded as evidence for Step 3, not as a Step-1 failure.
BAL-F3: as above.

**Criteria before scripts.** No numeric check is planned. If one becomes necessary, its pre-registered
PASS/FAIL criteria are appended to this file before the script is written, and the script lives in the scratchpad
(this worker writes no checks/ file in the repository).

---

# FINDINGS (appended from 2026-10-28T23:22Z, after the reading; everything below was written after the pre-statement)

## 0. Headline

1. **BAL-F1 fires for every Balaban CMP body.** No Balaban paper in the series (CMP 95, 96, 98, 99:75, 99:389,
   102:255, 102:277, 109, 116, 119, 122:175, 122:355) could be read through the permitted channel (WebFetch/WebSearch,
   no PDF on disk). Two independent reasons, each sufficient: (i) every legitimate free copy is a scanned PDF (Deep
   Blue, Project Euclid), and the fetch tool **does not parse PDF** (it returned the raw Flate-compressed stream) and
   **saves the binary to disk** when it fetches one; (ii) the hosts block the tool (Deep Blue: HTTP 403 or an empty
   JavaScript shell; Project Euclid: empty responses, consistent with the Incapsula bot check the lane recorded in
   session 4; Springer: redirect to a sign-in flow and a paywall). No bot check was bypassed, nothing was paid for.
   **So T56-1 as briefed cannot be completed by any worker using this tool; it needs an owner action (§10).**
2. What *could* be read legitimately: abstracts/keywords/reviews (zbMATH Open API), reference lists (Crossref), the
   lane's own direct transcription of CMP 109 (literature/NOTES.md §9, session 6), and open secondary sources: Goswami's
   adaptation of CMP 102 to sigma models (arXiv:2204.08252, AHP 2024), Dimock's arXiv expositions, and one Balaban
   co-authored arXiv paper (BFKT Part 4). §3-§6 extract what these establish, each item graded.
3. **Wall map (§7), in one line each.** (GAP-Z) and FLOW's fine inverse are the subject of CMP 99:389 (background-field
   propagators), but Balaban always inverts the **constrained** operator and gets the coupling flow from the
   **trivial** background via Ward identities, so FLOW's need for H_⊥(U)^{-1} at Nielsen-Olesen-unstable backgrounds has
   no counterpart in his scheme. (G♯_0-field) is the subject of CMP 95/96 (+ CMP 89). (N-bg)/(H-C) are, in his scheme,
   Cauchy-estimate corollaries of **analyticity** of the composite background (CMP 102), not separate theorems.
   (SPD)/(W2) and the level-count factor have **no direct counterpart**: Balaban defines the background by the
   composite constraint and re-evaluates every level's contribution at that one background (CMP 109 (0.21), (1.3)), and
   a hard constraint absorbs sources in Ran Q_k^T exactly (elementary, §7.5), which is precisely what (W2) must
   estimate in the soft scheme.
4. **BAL-F3 (§8): 6 PROOF.md paraphrases REFUTED** (two of them load-bearing for Step 3/Step 6 planning: the coupling
   flow is NOT supplied by any readable Balaban paper, and CMP 102's Theorem 1 is not about CMP 109's average (0.4)),
   plus 2 lead-file paraphrases REFUTED (PLAN_S26 §2e / RTARGET T56-4: Balaban's background threshold does not scale
   with g_k).

## 1. Access record (BAL-F1) — exactly what was tried

| Source tried | Result | Readable? |
|---|---|---|
| Deep Blue PDF URL for CMP 102:277 (bitstream/2027.42/46461/1/220_2005_Article_BF01229381.pdf) | HTTP 200 but only the JavaScript application shell ("Deep Blue Documents"), no content | no |
| Deep Blue item page, handle page, DSpace REST API (bundles) | HTTP 403 each | no |
| Project Euclid (two article URLs in the euclid.cmp/… and journals/… forms; one PDF-download URL) | empty content twice; ECONNRESET once. Consistent with the Incapsula bot check recorded at PROOF.md "[S4]: Project Euclid (CMP back volumes) returned a bot-detection page (Incapsula); not bypassed" | no (not bypassed) |
| link.springer.com/article/10.1007/BF01215753 | 303 redirect to idp.springer.com/authorize (sign-in/cookie flow); publisher copy is paywalled | not followed (pay nothing) |
| Rutgers Esploro records for CMP 95, 96, 102:277 | metadata only; abstract fields empty; the "Open / VoR" link is the DOI, i.e. Springer | metadata only |
| core.ac.uk search | HTTP 403 | no |
| Semantic Scholar API (CMP 102:277) | open-access location = hdl.handle.net/2027.42/46461, i.e. the same Deep Blue PDF | pointer only |
| zbMATH Open API | works. Reviews exist for CMP 109 (Martellini), 119 (no name), 122 I and II (O. M. Boyarkin), ICM 1986 (Itzykson), CMP 89; **for CMP 95, 96, 98, 99:75, 99:389, 102:255, 102:277, 116 only a licensing notice** ("contents unavailable due to conflicting licenses"); keywords are available for all | reviews + keywords |
| Crossref API (CMP 95, 96, 99:389, 102:277) | metadata and reference lists; **no abstracts** | metadata |
| ar5iv (arXiv HTML) | works for Dimock, Goswami, BFKT, Chatterjee; **the converted text is cut at ≈150k characters**, so long papers lose their later sections (1712.10029 stops in §3.2, before its gauge-field Theorem 1) | partly |

**Incident (to the lead; not hidden).** To test whether the fetch tool can read a PDF at all, I fetched one arXiv PDF
(arXiv:1712.10029, Dimock, legitimately free). The tool returned the raw compressed stream and **automatically saved
the binary** to
`/Users/jonBridger/.claude/projects/-Users-jonBridger-Toy-Physics--claude-worktrees-yang-mills-proof-df9972/a931aaa3-5369-4512-9e8d-b8590010706c/tool-results/webfetch-1793228096491-9f3zpe.pdf`
(600,279 bytes). This breaches the brief's "do not save any PDF to disk" by the tool's behaviour, not by choice. The
file is outside the repository, is an arXiv paper, and **was not opened or read**. I did not delete it (deleting files
is outside what I may do unasked); the lead or owner should remove it. **No PDF URL was fetched after this test.**
Consequence for every future worker: WebFetch must never be pointed at a PDF under this lane's rules.

**Verdict, BAL-F1: FIRES** for all twelve Balaban bodies above (and for the ICM 1986 article and Physica 124A, which
exist only as PDF / behind Elsevier). Nothing in §3-§9 asserts the content of a Balaban body except through the
graded channels below.

## 2. What was read, and how much weight each source can bear

Grades (as pre-stated): **READ** (primary text), **READ-SECONDARY** (a legitimate secondary source, read by me), plus
one grade forced by BAL-F1: **LANE-READ** = the lane's own transcription of CMP 109 (literature/NOTES.md §9, written
in session 6 from an owner-supplied scan, key equations from page images). I could not re-verify LANE-READ items: the
owner-supplied PDF is no longer on disk (searched /private/tmp/claude-502 and the home directory by name and by
Spotlight). **Every web read passed through the fetch tool's summarising model**; I asked for verbatim quotations and
repeated the fetch for load-bearing items. That channel made one error that I caught: a search summary attributed
arXiv:2204.08252 to Dybalski-Stottmeister-Tanimoto; the arXiv abstract page gives the sole author as **Abhishek
Goswami** (Ann. Henri Poincaré 25 (2024) 2065-2085). Quotations obtained in one fetch only are marked [1×].

| Id | Source | Grade | Used for |
|---|---|---|---|
| N109 | literature/NOTES.md §9: Balaban, CMP 109 (1987) 249-301 | LANE-READ | statements of CMP 102/99/98/95 as CMP 109 quotes and uses them; CMP 109's own Theorems 1-3, (0.21)-(0.31), (1.2)-(1.22), (2.9), §§4-5 |
| GOS | A. Goswami, arXiv:2204.08252 v3 = AHP 25 (2024) 2065-2085, "The variational problem and background field in the RG method for non-linear sigma models" | READ-SECONDARY | CMP 102's proof architecture, with Goswami's pointers to CMP 102/99/95 equation numbers |
| DIM1 | J. Dimock, arXiv:1108.1335 (RG according to Balaban I; scalar φ⁴₃) | READ-SECONDARY | exact form of the k-step Green's function, its bound, the uniformity convention, the random-walk proof |
| DIMQ | J. Dimock, arXiv:1512.04373 (QED₃ UV regularity), Lemmas 6, 9, 11 | READ-SECONDARY | abelian gauge-field G_k, H_k, C_k bounds (sources cited there as [5], [6], [8]; their identity as CMP 95, 96, 99 is from NOTES §6, not visible in my excerpt) |
| DIMF | J. Dimock, arXiv:1712.10029, §2 (fermions in a gauge background), Lemma 5 | READ-SECONDARY [1×] | a multiscale random-walk bound with an explicit scale-difference factor |
| DIMO | J. Dimock, arXiv:2204.07201 (QED₃ overview) | READ-SECONDARY | hard vs soft constraints in Balaban's method, volume, local perturbations |
| BFKT | Balaban-Feldman-Knörrer-Trubowitz, arXiv:1609.01748 (Part 4: background and critical fields) | READ-SECONDARY (Balaban co-author, different model) | how Balaban states uniformity in a later paper |
| ZB | zbMATH Open API records | READ (reviews/keywords are primary records of the database, secondary about the papers) | subject of each paper; CMP 119/122 main results as reviewed |
| CR | Crossref API | READ (metadata) | dates, reference lists |
| CH | S. Chatterjee, arXiv:1803.01950 §6 | READ-SECONDARY | what "UV stability" did and did not deliver |

## 3. T-a — the k-fold-constrained background field (CMP 102:277-309)

**Primary body: NOT-READ (BAL-F1).** zbMATH keywords (ZB): "lattice gauge theory", "regular gauge field
configurations", "minimal configuration", "background field"; MSC 58E30, 81T08. Crossref: published June 1985; its
reference list cites CMP 95, 96, 98, 99:75, 99:389 and Physica 124A (1984). What is known, by channel:

**3.1 The theorem as CMP 109 quotes it (LANE-READ, N109 §9.4, CMP 109 pp.256, 259-260).**
- Definition (0.21): U_k(V) minimises U ↦ A^η(U) on {U : Ū^k = M^k(U) = V} — **one fine-lattice problem with the
  composite k-fold constraint**, not a tower of one-step problems.
- CMP 109 p.256: "In [15] it was proved that in a space of regular orbits there exists exactly one critical orbit,
  which is a set of minima" ([15] = CMP 102:277). p.260: for V with |V(∂p') - 1| < ε_0' "there exists exactly one
  regular, critical orbit … and it is a minimal orbit". **Uniqueness is among regular orbits (a small-field class),
  modulo gauge — not global.**
- The regular class is (1.2) of CMP 109: U_k(ε_0) = {|U(∂p) - 1| < ε_0η² and |J| < ε_0}, η = L^{-k} (fine spacing in
  coarse units), J = D*_U η^{-2} π Im ∂U. **Two clauses**: curvature < ε_0 in coarse units, and a second-order
  (covariant-divergence) clause. ε_0 is a **fixed** small constant, not tied to g_k (p.259: "for ε_0 sufficiently
  small").
- p.260: (1.2) implies |V(∂p') - 1| < 2ε_0 "By Proposition 2 [12]" (CMP 98), and is implied by the condition on V
  "with 2ε_0 replaced by B_3^{-1}ε_0, see Theorem 1 [15]". So CMP 102's Theorem 1 contains a constant **B_3** linking
  coarse regularity of V to fine regularity of U_k(V).
- Also used by CMP 109 from CMP 102 (none re-proved there): Sect. F, local coordinates U_k = exp iηH; Sect. G, the
  multiscale minimisers U_n built on the maximal sequences {Ω_n} of CMP 99:75; **Proposition 9 and (190): exponential
  decay of δH/δB with rate δ_0**; (41), (171), (174), (179), (180), (2): the expansion of the action and the
  Landau-gauge representation; minimal configurations with |∂U_j - 1| < ε_0ξ² lie in the complexified spaces
  U^c_j(X, α_0, α_1, γ_0) of CMP 109 (1.10)-(1.16) (p.263, "via Proposition 9 [15]").

**3.2 Proof architecture, from Goswami's adaptation (READ-SECONDARY, GOS; two fetches agree).** Goswami states that
CMP 102 is his main source and cites it by section and equation:
- minimiser of the linearised problem: H B = G Q*(QGQ*)^{-1}B with G = (Δ + Q*aQ)^{-1} (GOS Eq. 36, citing **CMP 95
  Eq. 1.103** and **CMP 99:389 Eq. 3.126**); bounds |HB| ≤ B_0|B|, |H_1B| ≤ B_1|B| with exponentially decaying
  kernels — GOS Eq. 39: "They also satisfy the bounds (Eqs. 46, 103 [7])" ([7] = CMP 102:277);
- the non-linear constraint is **linearised by a change of variables** (GOS Lemma 5, citing **CMP 102 Sect. C,
  Eqs. 59-62**) and the critical point is a **contraction-mapping fixed point**; positivity of the second variation
  ("since Δ1 is positive definite") gives a minimum;
- **induction on k**: GOS §3.4, "Assuming that Theorem 1 is true for k−1", with U_{k-1}(V_0) as the starting
  configuration at step k; the regularity constant B_3 is **a fixed expression** in B_0, κ, M (GOS Eq. 98, citing
  **CMP 102 Sect. F, Eqs. 162-163**), "provided by the inductive hypothesis on k−1", and the induction closes under
  "B3 e^{-κ(2M)} ⩽ 1/2". **No recursion in B_3: the constant is re-derived from k-uniform propagator bounds, not
  multiplied step by step.** (GOS asserts the closure; the fetch reports it is not proved line by line there.)
- **analyticity**: U_k(V) = e^{iℋ(B)}U_0 is "analytic in the domain |ℋ(B)| < ε2" (GOS §4.1), with ℋ(B) = H_1B + O(B²)
  (GOS Eqs. 101-104, citing **CMP 102 Eqs. 196-197**).
- hypotheses of GOS Theorem 1: 0 < ε_0 ≤ a_0, 0 < ε_1 ≤ a_1, V ∈ 𝔅_k(ε_1), B_3ε_1 ≤ ε_0 (sigma-model version).
- GOS Remark 3 on what does **not** transfer from his model to Balaban's: "Yang Mills theories have an additional
  constraint due to the gauge fixing which further complicates their regularity properties."
- GOS §1 cites Magnen-Rivasseau-Sénéor (CMP 155, 1993) for the remark that Balaban's analysis "is difficult to follow
  and is spread over several papers".

**3.3 How Balaban states uniformity in his own later work (READ-SECONDARY, BFKT, Balaban co-author).** The
background field is a Banach fixed point at fixed scale n built with the **composite** operator Q_n ("the composition
of the averaging operations for all previous steps"); Convention 1.3: "All of the constants K_j, ρ_j are independent of
L and the scale index n."

**3.4 Extraction table for T-a.**

| Item | What is known | Grade |
|---|---|---|
| Existence | exactly one regular critical orbit for |V(∂p') - 1| < ε_0' | LANE-READ (CMP 109's quotation of CMP 102 Thm 1) |
| Uniqueness | among regular orbits, modulo gauge (local, not global) | LANE-READ |
| Regularity | V regular with B_3^{-1}ε_0 ⇒ U_k(V) ∈ U_k(ε_0) (both clauses of (1.2)) | LANE-READ |
| Decay | δH/δB decays exponentially, rate δ_0 (Prop. 9, (190)) | LANE-READ (cited, not quoted) |
| Analyticity | in local coordinates exp iηH; complexified class U^c_j | LANE-READ + READ-SECONDARY (GOS §4.1) |
| Norms | sup-type (|·| per plaquette / link, normalised trace in CMP 109) | LANE-READ (PROOF.md flags the √N conversion) |
| Constants | ε_0, ε_0', B_3 (and B_0, B_1, δ_0); dependence on L, d, G only, as far as visible | NOT-READ (values, exact dependence) |
| k-uniformity | constants independent of k; induction with a non-compounding B_3 | LANE-READ (CMP 109 Thm 3, §5 below) + READ-SECONDARY (GOS, BFKT) |
| Exact hypotheses, the multiscale version (Sect. G), the gauge-fixing interplay | — | **NOT-READ** |

## 4. T-b — propagators (CMP 95, 96, 99:389) and random-walk expansions

**Primary bodies: NOT-READ (BAL-F1).** Subjects, from ZB keywords: CMP 95 — "Lattice gauge theories", "vector field",
"Gaussian action", "renormalization group method", "non-Abelian gauge field"; CMP 96 — "different scales",
"renormalization transformations of different orders"; **CMP 99:389 — "regularity", "decay properties", "propagators",
"renormalization group", "lattice gauge theories", "external gauge field", "back-ground field"**. CR: CMP 99:389 cites
CMP 89 ("Regularity and decay of lattice Green's functions"), 95, 96 and the averaging preprint (CMP 98). So: **95 =
trivial-background (Gaussian) propagators, 96 = their multiscale version, 99:389 = the background-field version.**

**4.1 What CMP 109 takes from them (LANE-READ, N109 §9.4-9.7).** From CMP 99:389: the operators H_{1,j}, Δ_1
("defined in Sect. D [13]"), regular complex configurations and analyticity of the explicit terms ((3.35)-(3.38)),
the quadratic form Δ^{(k)} ((3.127)-(3.128), (3.156)); the fluctuation covariance is **C^{(k)} = (C*Δ^{(k)}C)^{-1} on
the hard-constraint subspace {Q̃B = 0}**, built from (3.156) with δ gauge fixing replaced by the exponential one. From
CMP 95: Δ_j ((1.66)) and the momentum notation ((1.29)-(1.37)). From CMP 99:75: the axial→Landau transformation u_k.
GOS adds CMP 99:389 (3.109)-(3.110), (3.126)-(3.129) (minimiser) and (3.139), (3.147) (projection operator).

**4.2 Exact statements of the analogues (READ-SECONDARY).**
- *Scalar, soft kernel (DIM1).* G_k = (−Δ + μ̄_k + a_kQ_k^TQ_k)^{-1} on the torus of spacing L^{-k} (DIM1 Eq. 49);
  minimiser φ_k = a_kG_kQ_k^TΦ_k (Eq. 50); **a_k = a(1 − L^{-2})/(1 − L^{-2k})** (Eq. 32), obtained from the one-step
  composition a_{k+1} = a_ka/(a_k + aL^{-2}) (Eq. 39) — **composing soft Gaussian steps gives one soft composite
  constraint**. Local bounds (Eqs. 80-81): |(G_k(□̃)f)(x)| ≤ Ce^{−γ_0d(y,y′)}‖f‖_∞, γ_0 = O(L^{-2}), and the same for ∂G_k
  and the Hölder derivative δ_α∂G_k (½ < α < 1); global Lemma 6 (Eq. 85) with rate ½γ_0, hypothesis "If M is
  sufficiently large the series for G_k, ∂G_k, δ_α∂G_k all converge"; Corollary 7 (Eq. 100) sup bounds. **Uniformity:
  DIM1 §2.4, "we employ the convention that C stands for a constant depending on L, but no other parameters"** — so
  independent of k and of the volume; M = L^m is the random-walk cube size ("M is not the same as the volume parameter").
- *Abelian gauge field, hard constraint (DIMQ).* Lemma 6 (Landau-gauge Green's function 𝒢_k), Lemma 9 (minimiser
  ℋ_k = 𝒢_k𝒬_k^T(𝒬_k𝒢_k𝒬_k^T)^{-1}), Lemma 11 (C_k, C_k^{1/2}): |𝒢_kf|, |∂𝒢_kf|, ‖δ_α∂𝒢_kf‖_∞ ≤ C‖f‖_∞, local decay
  Ce^{−γd(y,y′)}, |C_k(Υ,Υ′)| ≤ Ce^{−γd}; hypothesis "convergent for M sufficiently large"; 𝒢_k uses a fixed a > 0 in
  its definition; Lemma 6's proof is "We sketch the proof", with the remark "These bounds can be obtained more simply by
  other methods". **In QED the gauge-field operators are background independent**, so DIMQ is an analogue of CMP 95/96,
  **not** of CMP 99:389 (the lane recorded this at PROOF.md L3g [S5]; confirmed).
- *Multiscale, in a background (DIMF, fermions, [1×]).* Lemma 5: a random-walk expansion S_{k,Ω}(𝒜) = Σ_ω S_{k,Ω,ω}(𝒜)
  for backgrounds 𝒜 in a regular class, with kernel decay in the scaled distance d_Ω(y,y′), **a factor L^{−(k−j′)}** for
  the scale difference, and a Hölder bound with L^{−α(k−j)} (Eqs. 94-95); "C and γ may depend on L"; M "sufficiently
  large (depending on L)".

**4.3 The random-walk mechanism (READ-SECONDARY, DIM1 §2.4; DIMF Lemmas 5-7).** Local inverses on enlarged M-cubes
(Neumann-restricted, or with the cube's block constraint); a parametrix G* = Σ_z h_zG(□̃_z)h_z from a smooth partition
of unity; the commutator of h_z with the operator gains **M^{-1}** (|∂h| ≤ O(1)M^{-1} in block units); paths of n steps
cost (CM^{-1})^n with O(1)^n paths, so the series converges for M large; decay comes from the path length. **The
expansion is written for a generic k, not by induction in k** (DIM1, per both fetches). The base input is the bound
on each local inverse, uniform because every M-cube problem is a fixed finite problem after scaling (Balaban's
"lemma on unit lattice operators", cited at DIMF §2.5).

**4.4 NOT-READ for the non-abelian background case (the lane's actual walls):** the hypotheses on the background U
(which regular class; whether the |J| clause is used), the decay rate and its dependence, the gauge fixing used in
the estimates (Landau via u_k is what CMP 109 reports), analyticity in U, and the treatment of the hard-constraint
subspace. **No open exposition of CMP 99:389 exists** (Dimock's gauge fields are abelian; GOS is a sigma model).

## 5. T-c — why constants do not compound across RG steps

Each mechanism below is stated with its channel. Together they are the answer to (c) as far as it can be given
without the bodies.

- **M1. One-shot composite definitions (LANE-READ + READ-SECONDARY).** Background, propagators and covariances at
  step k are defined from the **k-fold composite** constraint (CMP 109 (0.21); DIM1 Eq. 49 with a_k in closed form;
  BFKT's Q_n), and **bounded directly at that k** with constants depending on L (and M) only (DIM1 convention; BFKT
  Convention 1.3). Nothing is a product of k one-step bounds.
- **M2. Every level is re-evaluated at the one current background (LANE-READ).** CMP 109 (1.3) writes the k-th action
  as −(1/g_k²)A(U_k) + Σ_{j<k}{−β_{j+1}(g_j)A(U_k) + [log Z^{(j)}(U_k) − log Z^{(j)}(1)] + [E^{(j+1)}(g_j,U_k) −
  E^{(j+1)}(g_j,1)]}: every earlier level's contribution is a functional of the **same composite background U_k**.
  There is no tower of per-level backgrounds whose errors could accumulate.
- **M3. Induction with a self-reproducing, not compounding, constant (READ-SECONDARY, GOS; LANE-READ for B_3's
  existence).** Where Balaban does induct (existence of U_k(V)), the constant B_3 is a fixed expression in the
  k-uniform propagator constants and M, closed by e^{-κ(2M)} small (M large) — §3.2.
- **M4. Locality with fixed constants on complex domains (LANE-READ).** CMP 109 (1.18): |E^{(j)}(X, g_{j-1}, U, J)| ≤
  E_0 exp(−κd_j(X)) on the complexified spaces U^c_j, "for M ≥ M(κ), γ sufficiently small" — **E_0 fixed, no power of
  the coupling**; derivatives come from analyticity (Cauchy), not from separate derivative inductions.
- **M5. Irrelevance makes the level sum geometric (LANE-READ).** After the Ward-identity subtraction of the marginal
  part, (0.29): |V^{(j)}(X,U_k)| ≤ O(1)(L^jη)^{4+α}exp(−κd_j(X)), α > 0, hence (0.30): |E_k(U_k)| ≤
  O(1)(1 − L^{-α})^{-1}M^{-4}|T_1^{(k)}| — "This is the essence of the ultraviolet stability concept" (p.259). **Each
  level's contribution carries a power gain (L^jη)^α in the current units; the sum over levels is Σ_j L^{-α(k-j)},
  bounded by (1 − L^{-α})^{-1}.** A level sum of fixed-size terms never occurs.
- **M6. One marginal coupling, extracted at the trivial background (LANE-READ).** Taylor expansion in the local
  coordinates exp iηH to fifth order, Ward identities ((4.9)-(4.45)) fix the lower orders as β_jA^η; Π is
  translation-invariant, permutation- and reflection-covariant, transverse ((5.6)-(5.9)), and (5.37) Π̂_μν(p) =
  β(δ_μνΔ(p) − d̄_μ(p)d_ν(p)) + Π′_μν(p) with Π′ of third order in d, d̄. The coupling recursion is 1/g_k² = 1/g_{k+1}² +
  β_{k+1}(g_k) ((0.20)).
- **M7. Fixed small-field thresholds (LANE-READ).** Background: fixed ε_0 in coarse units ((1.2)). Fluctuations: fixed
  ε_1 per bond ((2.9)), with the alternative "g_k/γ_k ε_1 instead of ε_1, where γ_k = C log(L^kε)^{-1}" — which is
  ≈ (β/C)g_k³·ε_1 along (0.31), not ∝ g_k. **Balaban's k-uniformity in CMP 109 does not come from thresholds that
  shrink with g_k.**
- **M8. The smallness hypothesis on the whole flow (LANE-READ; ZB).** CMP 109 Theorem 3: "There exist positive
  constants κ_0, M(κ), γ, ε_0, ε_1, α_0, α_1 such, that if κ ≥ κ_0, M ≥ M(κ), 0 < g_k ≤ γ for k = 0,1,...,K, then the
  sequence of actions A_k … satisfy all the inductive assumptions" (p.264). The constants are independent of k, K and
  the torus parameter m. The same conditional form is reported for the end of the series (ZB, Boyarkin on CMP 122 II:
  the theorem holds "if the sequence of the effective coupling constants is contained in an interval" ]0,γ]).
- **M9. Large fields (ZB; LANE-READ for the deferral).** In d = 4 the large-field regions need the R operation (CMP
  122 I-II), because, in Boyarkin's summary of CMP 122 I, with the bare coupling ∼ (a + b log ε^{-1})^{-1/2} "the
  Wilson action has the bound which does not give any positive power of ε", which "leads to the impossibility to
  control expressions arising in the large field regions for all steps of the procedure". This is the same diagnosis
  as the lane's Proposition LF-count (consistent; not a proof of it).

## 6. T-d — CMP 98, 109, 116, 119, 122; volume, local sources, symmetry, infinite volume

**6.1 The other papers (bodies NOT-READ except CMP 109 = LANE-READ).**
- **CMP 98 (1985) 17-51, "Averaging operations for lattice gauge theories"** (ZB keywords: renormalization group
  transforms, averaging operations, lattice gauge fields, gauge transformations). CMP 109 calls its average "the
  earlier, non-Euclidean-symmetric average" (p.252) and asserts that "all results of the paper [12] are valid" for its
  new Euclidean-invariant averages (0.4) and (0.12) (p.254) — an assertion, not a proof (N109 §9.2, §9.7).
- **CMP 99:75-102, "Spaces of regular gauge field configurations on a lattice and gauge fixing conditions"** (ZB:
  "lattice gauge field configurations", "gauge invariant regularity"): the spaces U_k(ε_0), maximal sequences {Ω_n},
  regularity conditions (1.7)-(1.10), the axial→Landau transformation u_k, expansions (1.43)-(1.54) (N109 §9.7).
- **CMP 109 (LANE-READ):** small-field only; its inductive Theorem 3 is completed only modulo the localisation and
  cluster expansion of the fluctuation integral (2.13), deferred to "the next paper" (p.298); Theorem 2 (the coupling
  flow, two-sided bounds (0.31) with unspecified 0 < β ≤ β′) is deferred: "A proof of this theorem, based on
  perturbative calculations, will be given in a separate paper" (pp.259-260).
- **CMP 116 (1988) 1-22, "II. Cluster expansions"** (ZB keywords: fluctuation field integral, cluster expansion,
  effective actions, small field approximation) — the deferred localisation of CMP 109.
- **CMP 119 (1988) 243-285, "Convergent renormalization expansions for lattice gauge theories"** (ZB review, opening
  words verbatim: "In this paper we introduce an inductive description of the complete effective densities including
  large field domains,"; the rest, paraphrased by me: the transformations preserve that form, which completes the RG
  analysis for **superrenormalizable** models with convergent expansions). **The review does not mention the coupling
  flow or CMP 109's Theorem 2.**
- **CMP 122:175-202 and 355-392, "Large field renormalization I, II"** (ZB reviews by Boyarkin; §5 M8-M9): Part II's
  main theorem is conditional on the effective couplings lying in ]0,γ]; "As an immediate consequence of this theorem,
  it follows the ultraviolet stability bounds of the same type" (as for superrenormalizable models).

**6.2 Volume.** Balaban's torus is T_ε with side 2L^m (in units of the last RG scale), ε = L^{-K}, m free (N109 §9.2);
the constants of Theorem 3 do not involve m, and the bulk bound (0.30) is **extensive**, |E_k| ≤ C|T_1^{(k)}|. So the
estimates are **volume-uniform per unit volume** and the torus is **not** intrinsically small in last-scale units;
the restriction is that the coupling stay ≤ γ down to the last scale (this confirms PROOF.md's own reading at the
string "torus side in stopping-scale units is arbitrary", against N109). Dimock (DIMO §1, verbatim): "The method works
equally well for any finite volume, not just unit volume." and "But the infinite volume limit would pose new
difficulties." Chatterjee (CH §6): "The existence of a convergent subsequence is known as ultraviolet stability", and
"None of the above techniques, however, help in constructing the continuum limit."
**Bearing on R^4 (panel P4's "what would change my mind", P-a/P-c):** nothing read suggests that large fields force
volume-dependent constants into Balaban's bounds — his bounds are local polymer bounds with fixed constants
(M4) and an extensive sum (M5). But **no Balaban statement read concerns local expectations**; his output is
partition-function-level (UV stability), which panel P3 shows controls no normalised local moment by itself.

**6.3 Local source insertions.** None in the readable record. ZB (Boyarkin, CMP 122 II): "This theorem is the basis
for an analysis of expectation values of physical observables, like loop variables," (and averaged loop variables) —
stated as a basis for later work, not done there. DIMO §1: "The proof should allow one to add local gauge invariant
perturbations to the action", and uniform bounds with analyticity in the sources "would give uniform bounds on
correlation functions" — an expectation. Dimock III (per NOTES §3): "Correlation functions: not proven". **So the
volume-uniform local-source RG that the consensus route needs is not in Balaban's published series as readable; it is
new work, to be modelled on M1-M5.**

**6.4 Symmetry (LANE-READ, N109).** The averages (0.4)/(0.12) and the exponential gauge fixing (0.14) are
**Euclidean-invariant** (lattice symmetries), "unlike the δ-function axial gauge of [9,16]" (p.254); gauge invariance
(1.19) and lattice Euclidean invariance (p.263) are part of the inductive hypotheses; Π is translation-invariant,
permutation- and reflection-covariant and transverse ((5.6)-(5.9)). **The single marginal quadratic term has the
O(4)-covariant transverse form at leading order, β(δ_μνΔ − d̄_μd_ν), and every rotation-non-covariant term is in Π′,
third order in the lattice derivatives, i.e. irrelevant ((5.37)-(5.38)); after renormalisation all remaining local
terms carry the power gain (L^jη)^α of (0.29).** This is the structure a **rotation-defect estimate** would consume:
hypercubic symmetry + gauge invariance leave no rotation-breaking marginal operator, and the irrelevant ones are
suppressed by a power of the scale ratio with k- and volume-uniform constants. Balaban proves this for the effective
actions at small fields; **he states nothing about rotation invariance of limits, observables, or infinite volume.**

## 7. T-e — the wall map (Step 2 input)

Format per wall: **lane object** (file + locating string, as on disk 2026-10-28) · **Balaban's counterpart in the hard
scheme** (with the grade of the pointer) · **what changes in the soft scheme** · **consequence**. "Covered" below means
"is the subject of"; since no body could be read, **no wall is shown to be covered by an exact theorem** — that needs §10.

### 7.1 (GAP-Z)
- **Lane.** BFT_B.md §38.1, string "**(GAP-Z).** The background analogue of the package constant M": a bound, uniform in
  k, T and Z, on the kernel of the gauge-fixed **composite chain** Hessian at a background chain Z — equivalently a k-,
  T-uniform lower bound for 𝓛_Z on the covariant slice S_E^Z, **no decay claimed**.
- **Balaban.** CMP 99:389 (ZB keywords "external gauge field", "back-ground field", "regularity", "decay
  properties"): the quadratic form Δ^{(k)}(U) at a regular background on the hard-constraint subspace {Q̃B = 0}
  ((3.127)-(3.128), (3.156)), whose inverse C^{(k)} = (C*Δ^{(k)}C)^{-1} CMP 109 uses as the fluctuation covariance;
  Landau gauge via u_k (CMP 99:75); the auxiliary G = (Δ + Q*aQ)^{-1} of the minimiser formula (CMP 95 (1.103),
  CMP 99:389 (3.126); GOS Eq. 36). Pointer grade: LANE-READ + READ-SECONDARY. **Balaban's object carries exponential
  decay (more than (GAP-Z) asks).**
- **Soft-scheme change.** (i) The operator: the Hessian of the composite soft functional with every intermediate level
  free and penalised by κ_l (a Schur complement over levels) replaces "fine operator on the single composite constraint
  subspace". At Z = 1 the two coincide in form: integrating out soft Gaussian levels gives one composite soft constraint
  with a_k in closed form (DIM1 Eqs. 32, 39) — the scheme difference is invisible there. At Z ≠ 1 the intermediate maps
  are background-covariant (Q_l^Z), and the Schur complement is no longer a single composite term. (ii) The slice: the
  lane's per-block covariant slice (root value fixed) instead of Landau gauge plus axial-in-blocks. (iii) The class: the
  lane's 𝒦(ε) vs Balaban's (1.2), which also has the |J| clause.
- **Consequence.** (GAP-Z) is CMP 99:389's subject in the hard scheme. If Step 3 chooses the hard scheme, (GAP-Z) becomes
  "import and re-verify CMP 99:389 (+ CMP 99:75 for the gauge)"; in the soft scheme it is a new theorem whose Z = 1 case
  is already the frozen package constant M.

### 7.2 (G♯_0-field)
- **Lane.** PROOF.md string "**(G♯_0-field): not attempted.**": the abelian multi-level **per-level-slice** physical gap
  plus (G♯_0-fine) (Hölder/Campanato field bounds at the trivial background for sources at all levels, uniformly in k,
  T, RTARGET §33 norms).
- **Balaban.** CMP 95 (Gaussian action) and CMP 96 (different scales), with the Hölder/derivative technology of CMP 89;
  abelian exact analogues DIMQ Lemmas 6/9/11 (sup, derivative and Hölder-derivative bounds ≤ C‖f‖_∞, decay e^{−γd},
  M large) and the multiscale form DIMF Lemma 5 (scale-difference factor L^{−(k−j′)}). Pointer grade: READ-SECONDARY for
  the analogues; bodies NOT-READ.
- **Soft-scheme change.** Balaban gauge-fixes on the fine lattice for the **composite** problem; the per-level slice
  (abelian h^{(i)} = 0 + Feynman at every level) and **sources at every level** are features of the lane's chain. In
  Balaban's scheme multi-level sources arise only through the multiscale domains Ω_j, and their bounds carry explicit
  scale-difference factors (DIMF) — a sup over levels, not a sum.
- **Consequence.** The trivial-background content is CMP 95/96's; the per-level-slice formulation is a soft-scheme
  artefact that the composite formulation (BFT) may not need. Not a Balaban-covered wall as stated.

### 7.3 (N-bg) and (H-C) (including the C_♭ clause)
- **Lane.** NORMS.md string "**(N-bg) [OPEN].** D³E_k^br(V) for V in the small-field class, with a constant uniform in
  k"; PROOF.md string "(H-C) (level-uniform Lipschitz constants of Hess E_i^br)"; C_♭ is already a Cauchy constant
  (PROOF.md string "C_♭ := 4S_♭n_1/r_♭", polydisc of radius r_♭/2).
- **Balaban.** No separate third-derivative or Lipschitz theorem: **analyticity** of the background in local
  coordinates (CMP 102 Sect. F; GOS §4.1 "analytic in the domain |ℋ(B)| < ε2", CMP 102 (196)-(197)) and of the
  effective-action terms on complexified spaces with fixed bounds (CMP 109 (1.10)-(1.18), built on CMP 99:389
  (3.35)-(3.38)); all derivatives then follow by Cauchy estimates on k-uniform domains (M4). Pointer grade: LANE-READ +
  READ-SECONDARY.
- **Soft-scheme change.** The soft penalty φ̂ is analytic near the identity, so the same route is available **if** the
  composite soft critical point is constructed by a contraction on complex fields in a k-uniform polydisc (BFT-0 in
  analytic form). (H-C)'s per-level tower E_i^br has no Balaban counterpart: Balaban re-evaluates every level at the
  one composite background (M2).
- **Consequence.** In Balaban's architecture (N-bg)/(H-C) are **corollaries** of an analytic BFT-0, not independent
  walls. This agrees with NBG_ADJ's finding that (N-bg) is downstream (not re-verified here).

### 7.4 FLOW's fine inverse H_⊥(U)^{-1} ((T-a1-M) = (T-b))
- **Lane.** FLOW.md §84 string "H_⊥ := P_⊥H(U)P_⊥ on ker D_U^*" (transverse Hessian of the Wilson action at a
  **critical** background, unconstrained); FLOW.md string "(T-a1-M) needs the fine H_⊥(U)^{-1} expansion and is filed
  with (T-b) (OPEN)"; FLOW.md records that at the constant-flux backgrounds U_f "H_⊥ has the Nielsen-Olesen negative
  mode" and that there "the K_F^{-1} form of X_n must not be used, only V-tel's Woodbury form".
- **Balaban.** CMP 99:389 is about propagators in a background, but **always for the constrained operator** (hard
  constraint or the auxiliary +Q*aQ), which has a gap of order one in block units that dominates O(field strength)
  background effects for regular (small-curvature) backgrounds; and **the coupling flow is extracted at the trivial
  background**: the marginal term comes from the second derivative of E^{(j+1)} at B = 0 plus Ward identities (CMP 109
  (1.20)-(1.22), (4.9)-(4.45), (5.37); M6). No inverse of the unconstrained fine Hessian at a non-trivial critical
  background appears in what CMP 109 uses. Pointer grade: LANE-READ.
- **Soft-scheme change.** None forced: the constrained (Woodbury) form exists in the soft scheme too (FLOW already
  uses it at U_f). The need for H_⊥(U)^{-1} comes from **FLOW's route** (universality via plane-wave and
  constant-Cartan-flux backgrounds, (T-c)), not from the soft kernel.
- **Consequence.** **This wall is route-specific, not a "propagator at a general background" wall.** Balaban's
  route to the β-function (trivial background + Ward identities + analyticity for remainders) avoids it. Step 2 should
  list it separately from (GAP-Z), and the FLOW lane should price adopting the Ward-identity route.

### 7.5 (SPD)/(W2) — BFT_A's (W2), not the other objects called (W2)
- **Lane.** BFT_A.md [RBA2-fix] B4, string "(W2) **(SPD) smooth-part decay**": the Ran Q^T component of a remainder
  row at level l, carried up to level m, has plain coarse size ≲ L^{−(m−l)}η² (OPEN). BFT_A B4 also records that the
  currents of BL-6 (b) "lie entirely in Ran Q^T (j_l = (Q^{(l→k)})^TJ)". (Symbol warning, §8.3: at least three other
  objects in this lane are called (W2).)
- **Balaban.** No counterpart object: in the hard scheme there are no intermediate free fields and no soft residuals
  (the lane's r_j(x) := Qx_j − x_{j+1}, BFT_A §1, is identically zero under a hard constraint). The nearest Balaban
  statements are the multiscale regularity of minimisers (CMP 102 Sect. G; CMP 99:75's {Ω_n}; abelian form in Dimock
  1712.10029 Thm 1, recorded by the lane at PROOF.md L1d [S5] with level weights inside a **sup**) and the
  irrelevance gain (L^jη)^α of (0.29).
- **What changes, precisely (elementary; PROVEN-HERE in one line).** For a hard linear constraint Q_kA = B and any s,
  ⟨Q_k^Ts, A⟩ = ⟨s, Q_kA⟩ = ⟨s, B⟩ is constant on the constraint set, so **adding a source in Ran Q_k^T does not move
  the constrained minimiser at all**. With a soft constraint (κ/2)|Q_kA − B|², the same source is equivalent to the
  data shift B → B − s/κ and moves the minimiser by H_k(s/κ) ≠ 0. In the soft chain, ⟨Q^Tv, x_l⟩ = ⟨v, x_{l+1}⟩ +
  ⟨v, r_l⟩: pushing a Ran Q^T source up one level leaves a residual-type source ⟨v, r_l⟩ behind at every level.
  **(SPD)/(W2) is the soft scheme's quantitative substitute for an identity that is exact in the hard scheme** — for
  the part of a row that reaches the top level. Parts that stay rough at intermediate scales produce a response in
  both schemes ((W1)/(G♯-rough)).
- **Consequence.** BAL-F2 evidence (§9). Whether the hard scheme's exact absorption removes the level-count factor
  depends on how much of each offending row is top-range; that is a Step-4/Step-6 question, not settled here.

### 7.6 The level-count factor ≈ 25(k−1)
- **Lane.** HANDOFF.md item 5 ("≈ 25(k-1)"); BFT_A.md [RBA2-fix] B3, string "the entire level-count loss sits in the
  level-0 image": Σ_l‖j^c_l‖ ≤ (k − 1)η² for an unweighted plain-current family. KFACTOR55.md (Codex, unreviewed)
  locates the rows: κ_l(∂ρ_l^{(2)})^Tr_l (its Eq. (1)) and the BCH₂ current R_l^B(u) = 2κ_l⟨r_l, B_l(x_l,u_l)⟩ —
  **both linear in the soft residual r_l** (checked against BFT_A's definition of r_j).
- **Balaban.** No level sum of fixed-size terms occurs in the readable record: definitions are one-shot composite
  (M1), every level is re-evaluated at the one background (M2), renormalised level contributions carry (L^jη)^α and
  sum geometrically (M5), and the thresholds are **fixed** (ε_0, ε_1), not shrinking with g_k (M7).
- **Soft-scheme change, and a caution against an easy conclusion.** r_l ≡ 0 in the hard scheme, so these rows have no
  literal counterpart. But at a critical point κ_lr_l is the level-l **Lagrange multiplier** (the pulled-back force:
  the Euler-Lagrange equations give κ_{l-1}r_{l-1} = κ_lQ^Tr_l + (non-linear), and ∇S_W(U_0) = κ_0Q^Tr_0 at level 0),
  and the hard scheme has the same "multiplier × second-order averaging remainder" terms through the non-linearity of
  M^k. Balaban handles that non-linearity by **coordinates in which the composite constraint is linear** (CMP 109
  p.267, "The δ(Q̃B′) constraint is linearised by B′ = B − hD(B)" as transcribed in N109 §9.5; CMP 102 Sect. C per GOS)
  and by k-uniform regularity of M^k on regular configurations (CMP 98, 99:75). [Inference, not read:] for a smooth
  background the level-l second-order averaging remainder, measured as a **potential** in coarse units, is
  O(L·L^{−(k−l)}·F) (quadratic in own-unit potentials, which are L^{−(k−l)} smaller at level l) and so sums
  geometrically — the same Σ_iL^{−2i}-type mechanism as the lane's own Corollary A1-NA(k). The lane's factor arises
  when the same terms are measured as **currents** in plain coarse units at level 0. So the factor may be a currency
  effect; KFACTOR55's "least certain point" (a direct uniform estimate the slot-by-slot bounds miss) points the same
  way. Not settled here.
- **Consequence for T56-4.** Balaban's mechanism is **not** a g_k-scaled threshold (M7) and **not** AF running; it is
  the absence of fixed-size per-level terms in the currency his estimates use. The option "absorbed by a level-dependent
  small-field threshold (as Balaban uses, scaling with g_k)" in PLAN_S26 §2e / RTARGET §55 T56-4 rests on a
  misattribution (§8.2).

### 7.7 The map in one table

| Lane wall | Balaban paper (hard scheme) | Pointer grade | Changes in the soft scheme |
|---|---|---|---|
| (GAP-Z) | CMP 99:389 (+ 99:75 gauge, 95 (1.103)) | LANE-READ + SECONDARY | composite Schur complement over soft levels; covariant slice; class without |J| |
| (G♯_0-field) | CMP 95, 96 (+ 89) | SECONDARY (abelian) | per-level slice and all-level sources are chain artefacts |
| (N-bg), (H-C) | CMP 102 analyticity + Cauchy (M4) | LANE-READ + SECONDARY | corollaries of an analytic BFT-0; no per-level tower in Balaban |
| FLOW H_⊥(U)^{-1} | none needed: CMP 109 §§4-5 (trivial background + Ward) | LANE-READ | route-specific; the soft kernel does not force it |
| (SPD)/(W2) | none (no residuals); nearest CMP 102 Sect. G, (0.29) | LANE-READ | replaces an exact hard-scheme identity (§7.5) |
| level-count factor | none (M1, M2, M5, M7) | LANE-READ + SECONDARY | rows ∝ r_l; hard-scheme analogue via the multiplier; currency question |

## 8. T-f — BAL-F3: PROOF.md paraphrases of Balaban, checked

**Coverage.** `grep -n -i balaban PROOF.md` gives 111 lines. I read every hit in context and checked each one that
**asserts content** of a Balaban paper (as opposed to naming him, crediting him, or recording an owner request)
against N109 and the secondary sources. Line numbers are as on disk at 2026-10-28T23:00Z; locate by the quoted
string. **Correction to headline item 4 (§0): the count is 7 REFUTED in PROOF.md, of which 4 are load-bearing and 3
are not; plus 1 lead-file paraphrase REFUTED, occurring in two files.** A paraphrase I can neither confirm nor
contradict from the readable record is NOT-VERIFIED; the global caveat PROOF.md already carries ("Every statement
attributed to Balaban below paraphrases the structure … not read") remains correct.

### 8.1 REFUTED — load-bearing
- **B3-1. PROOF.md l.1000, "CMP 102's Theorem 1 is about the hard constraint (0.4)."** REFUTED. (0.4) is introduced
  **in CMP 109** as a new Euclidean-invariant average, replacing CMP 98's "earlier, non-Euclidean-symmetric average"
  (CMP 109 pp.252-254, N109 §9.2/§9.7); CMP 102 was published in June 1985 (CR), CMP 109 received 23 Sept 1985 (N109).
  **Correct statement:** CMP 102's Theorem 1 concerns the hard constraint built from CMP 98's averaging; CMP 109 uses
  it for (0.4) on the strength of its unproved remark that "all results of the paper [12] are valid" for (0.4)
  (p.254). **Why load-bearing:** Step 3's option (ii) ("run layer 1 in his hard scheme, import-and-reverify") cannot
  import CMP 102 for (0.4) verbatim; it needs CMP 98's results re-proved for (0.4) first — the same obligation the lane
  already records for S4′ (PROOF.md string "Transfer of the CMP 98 results").
- **B3-2. PROOF.md l.6707, "(Balaban's background-field covariances, CMP 95/96/102b [P])".** REFUTED (citation).
  Balaban's background-field propagators are **CMP 99:389-434** (title; ZB keywords "external gauge field",
  "back-ground field"); CMP 95 is the Gaussian (trivial-background) case and CMP 96 the multi-scale one (ZB keywords);
  CMP 109 cites CMP 99:389 Sect. D/(3.156) for the background-dependent operators (N109 §9.7). **Correct:** "CMP
  99:389 (background-field covariances), with CMP 102:277 for the background and CMP 95/96 for the trivial-background
  multiscale propagators." **Why load-bearing:** it is the reading pointer for Step 6's core attack.
- **B3-3. PROOF.md l.1345-1347 (L4a): "β_j → 2 b0 ln L" with "Sources: CMP 109 (1987) 249-301 [v]; CMP 116 …; CMP 119
  …".** REFUTED for CMP 109 by the lane's own read: "no statement β_j → 2b_0 log L appears in CMP 109" (NOTES §9.8);
  CMP 109's Theorem 2 gives only two-sided bounds (0.31) with unspecified 0 < β ≤ β′, and its proof is deferred to "a
  separate paper". NOT-VERIFIED for CMP 116/119 (ZB's review of CMP 119 does not mention it). The lane flags this
  itself at the string "That Balaban's lattice β_k → 2 b0 ln L is part of L4a, not reverified", but the Sources line
  still attributes it. **Correct:** β_j → 2b_0 ln L is one-loop universality, not a Balaban theorem in any readable
  paper. **Why load-bearing:** together with B3-8 below, it means **no readable Balaban paper supplies the coupling
  flow**; L4a-flow must be supplied by the lane in either scheme (this re-prices decision 4: the hard scheme does not
  come with a proven flow).
- **B3-4. PROOF.md l.4367-4368, "Balaban-type per-level thresholds φ_j ~ g_j … This is consistent with Balaban/Dimock,
  who never iterate".** REFUTED as an attribution, on two counts. (a) CMP 109's thresholds are fixed: ε_0 for the
  background ((1.2)) and ε_1 for fluctuations ((2.9)); its stated alternative is "g_k/γ_k ε_1" with γ_k =
  C log(L^kε)^{-1}, of order g_k³ε_1 where the log term of (0.31) dominates — not ∝ g_k. (b) "never iterate" holds for
  Dimock's large-field factors (NOTES §4, Lemma 23; Dimock III Lemma 13 — LANE-READ of Dimock) but not for Balaban's
  background field, which GOS reconstructs as an induction on k with a non-compounding constant B_3 (§3.2). The
  paragraph's **conclusion** (no k-uniform iterated bound for fluctuating fields) is unaffected — with fixed thresholds
  it holds a fortiori. **Why load-bearing:** it is the source of the "threshold scaling with g_k, as Balaban uses"
  framing that PLAN_S26 §2e and RTARGET T56-4 adopted (§8.2).

### 8.2 REFUTED — not load-bearing, and the lead-file item
- **B3-5. PROOF.md l.870 (L1d [R2-fix]), "Balaban's small-field conditions are dimensionless (||1 - U_p|| ≲ p(g_k) g_k
  at each scale …)".** REFUTED as a description of CMP 109 ((1.2): fixed ε_0, with a second |J| clause; (2.9): fixed
  ε_1). "Dimensionless per scale" is right. Already narrowed by the lane's [S6] block for the background domain.
  (The p(g)-type thresholds are Dimock's (p_k = (−log λ_k)^p, DIM1 Eq. 109); whether CMP 116/119/122 use them is
  NOT-VERIFIED.)
- **B3-6. PROOF.md l.752 (S1), "Balaban takes L sufficiently large [m]".** REFUTED (stale) against N109: "L is an odd,
  positive integer > 11" (p.251) is fixed; the parameter taken large in Theorem 3 is **M ≥ M(κ)** (with κ ≥ κ_0). The
  lane corrected this elsewhere (string "Balaban needs \"L odd > 11\""). Low load.
- **B3-7. PROOF.md l.653 and l.894, "Balaban's background small-field condition (1.2) is L1e's hypothesis" / "That is
  L1e's hypothesis F ≤ F_0".** REFUTED as an identity: (1.2) has two clauses, curvature < ε_0 **and** |J| < ε_0 (J =
  D*_Uη^{-2}π Im ∂U); L1e's hypothesis is the first only. The direction used (L1e's domain ⊇ (1.2)) is harmless, and
  l.1004 states both clauses. Low load.
- **Lead files (not PROOF.md), one paraphrase in two places: PLAN_S26.md §2e, "(as Balaban uses, scaling with g_k)",
  and RTARGET.md §55 T56-4 ("by a level-dependent small-field threshold").** REFUTED for the background-field domain
  and for CMP 109's primary fluctuation cut (M7); see B3-4. This bears directly on T56-4's three-way option list.

### 8.3 CONFIRMED against N109 (+ secondary) — not against the bodies
- **B3-9. PROOF.md l.6681, "Alternative: Balaban's convention, *define* the background as the composite critical
  point".** CONFIRMED vs N109: (0.21) defines U_k(V) by the composite constraint, and (1.3) re-evaluates every level at
  U_k (M2). This is the convention BFT's composite route already follows.
- **B3-10. PROOF.md l.6166, "(Balaban's form, CMP 102b)": uniqueness only within the small-field class, a local
  statement.** CONFIRMED in substance vs N109 ("exactly one regular, critical orbit"; uniqueness is among regular
  orbits). Detail NOT-VERIFIED.
- **B3-11. PROOF.md l.3810, "the torus side in stopping-scale units is arbitrary".** CONFIRMED vs N109 ((0.1): side
  2L^m, m free; Theorem 3's constants do not involve m) — §6.2.
- **B3-12. PROOF.md l.4139-4140, "in Balaban's set-up, the small-field conditions are dimensionless per level".**
  CONFIRMED vs N109 ((1.2) in coarse units; (2.9) per bond at each level).
- **PLAN_S26.md §2a** (background = minimiser under the **k-fold** constraint; propagators controlled uniformly in k):
  CONFIRMED in substance vs N109 (0.21), Theorem 3 and the secondary conventions (DIM1, BFKT).
- **PLAN_S26.md §2e, "In Balaban's scheme k-uniformity comes from random-walk expansions with exponential decay":**
  CONFIRMED but **incomplete** — that is the propagator half (M1, §4.3); the effective-action half is the irrelevance
  gain (L^jη)^α after Ward-identity renormalisation (M5-M6), a different mechanism.

### 8.4 NOT-VERIFIED (cannot be settled without the bodies)
- **B3-8. PROOF.md l.5288, "the paper with Theorem 2's proof (CMP 119:243-285 is the likely candidate, [not-read])";
  HANDOFF.md l.213 and LINEAR_PACKAGE.md l.483, "The coupling flow … [cf. CMP 109 Thm 2 and CMP 119]".** NOT-VERIFIED,
  **with contrary evidence**: ZB's review describes CMP 119 as the inductive description of the complete effective
  densities including large-field domains (completing the superrenormalizable case) and does not mention the flow;
  ZB's review of CMP 122 II states the series' main theorem **conditionally** on the effective couplings lying in
  ]0,γ]. An owner request for "the paper with Theorem 2's proof" should not assume it is CMP 119.
- PROOF.md l.977 (L2 statement: unique minimiser near the identity, analytic, exponentially localised) — consistent
  with N109 (quotation of Thm 1; Prop. 9/(190)) and GOS §4.1. NOT-VERIFIED in detail (norms, constants).
- PROOF.md l.1150 (L3g statement, covariance (Δ_{k,A} + aQ_k^†Q_k)^{-1}) — partly consistent: that operator is
  Balaban's **auxiliary** G (CMP 95 (1.103) via GOS; DIMQ's 𝒢_k uses a fixed a > 0); the **fluctuation covariance**
  CMP 109 uses is the hard-constraint C^{(k)} = (C*Δ^{(k)}C)^{-1} on {Q̃B = 0}. The lane's [S6] block records the
  latter. NOT-VERIFIED.
- PROOF.md l.1181, "Whether Balaban's combination has a uniform gap is the content of CMP 99:389" — consistent with
  ZB's keywords for CMP 99:389. NOT-VERIFIED.
- PROOF.md l.1463 (L5: suppression exp(−c p(g_k)²/g_k²) per block) — already flagged by the lane as
  convention-dependent; ZB's review of CMP 122 I supports the **motivation** (the Wilson-action bound gives no usable
  power of ε) that the lane's Proposition LF-count formalises. NOT-VERIFIED.
- The remaining hits (credits, titles, owner requests, comparison-branch bookkeeping) assert no Balaban content and
  need no verdict.

### 8.5 Symbol collisions met in this task (systemic defect 1)
- **η.** Balaban's η = L^{-k} is the fine **lattice spacing** in coarse units ((1.2): |U(∂p) − 1| < ε_0η²). The
  lane's η in BFT_A/KFACTOR55 rows (η², kη) is a **displacement size**. Importing (1.2) into a lane estimate must not
  identify them.
- **(W2).** At least four objects: BFT_A's (W2) = (SPD) smooth-part decay; PROOF.md [S22]'s (W2) = background-covariant
  operators / covariant Hodge (string "(W2) Background-covariant operators"); PROOF.md L5's (W1)/(W2)/(W3) = frozen
  exterior / smooth background / soft constraint (string "Frozen exterior (W1), smooth background (W2)"); FLOW's (W2).
  "(SPD)/(W2)" in the brief is BFT_A's.
- **M.** Balaban's M = L^m (random-walk/polymer cube side); Balaban's torus exponent m; the lane's torus side L^M; the
  frozen package constant M of LINEAR_PACKAGE Thm 4.2′ (the "M half" of (GAP-Z)); GOS uses M for both block geometry
  and lattice size; DIM1 distinguishes M from the volume parameter.
- **γ.** Balaban's coupling bound γ (]0,γ]); his γ_k = C log(L^kε)^{-1} in (2.9); Dimock's decay rate γ (γ_0).
- **κ.** Balaban's polymer decay rate κ (κ ≥ κ_0); the lane's soft-penalty strengths κ_l; GOS's propagator decay κ.
- **ε_0, ε_1.** Balaban's ε_0 (background, (1.2)) and ε_1 (fluctuation cut, (2.9)) are two further objects beside the
  lane's six ε_1.
- **B_3.** Balaban's constant in CMP 102 Thm 1 (as cited by CMP 109 p.260) and GOS's B_3 (his Eq. 98) are analogues in
  different models, not the same number.

## 9. BAL-F2 — does Balaban's k-uniformity depend on the hard constraint? (evidence for Step 3)

**Verdict: NOT decided; the evidence localises the question.**
- **Hardness is NOT what makes the propagators k-uniform.** Balaban's own scalar RG is soft (Gaussian kernels), and
  composing soft steps gives one composite soft constraint with a_k in closed form, bounded uniformly (DIM1 Eqs. 32,
  39, 49; convention "C … depending on L, but no other parameters"). Random-walk expansions (§4.3), irrelevance gains
  (M5), analyticity (M4) and fixed thresholds (M7) do not use hardness.
- **Gauge fields: Balaban and Dimock both use the hard constraint** (CMP 109 (0.17), δ(Ū(c)V^{-1}(c)), N109; DIMO Eqs.
  10, 52, δ(A_{k+1} − 𝒬A_k)). The only reason given in the readable record for a soft kernel is Grassmann-specific
  (DIMO: "We have avoided using a delta function for the fermion fields (which would not work for Grassmann
  elements)"). No readable source says why hardness was chosen for gauge fields.
- **Where hardness does work in the background-field problem (three places):** (a) sources in Ran Q_k^T are absorbed
  exactly (§7.5) — the soft scheme must estimate this ((SPD)/(W2)); (b) there are no intermediate free fields, so no
  residual-dependent rows (§7.6) — but the multiplier carries the same information, so this alone does not remove the
  level count; (c) the composite constraint can be linearised by one change of coordinates (CMP 109 p.267; CMP 102
  Sect. C via GOS) — the soft analogue (coordinates making every level's penalty exactly quadratic) has not been tried
  in this lane.
- **For Step 3:** these are exactly the two open soft-scheme items (SPD)/(W2) and the level-count factor. Choosing the
  hard scheme would turn (a) into an identity, but (i) CMP 102 would still have to be re-proved for (0.4) or (0.4)
  replaced by CMP 98's averaging (B3-1), (ii) the coupling flow is not supplied either way (B3-3, B3-8), and (iii) the
  lane's soft-scheme layer-2 benefits (Markov kernel, RP) would need re-deriving. Recorded as evidence, not as a
  recommendation.

## 10. What would complete T56-1 (owner action needed)

**The permitted channel cannot do it (§1).** Two legitimate ways forward, both owner decisions:
- **(A) Local copies, as for CMP 109.** The owner obtains the legitimately free copies in a normal browser — Deep Blue
  (hdl.handle.net/2027.42/46461 for CMP 102:277) and the open-access CMP back volumes on Project Euclid — and places
  them in a folder **outside the repository**; a worker then reads them locally (text plus page images for formulas,
  the NOTES §9 procedure). Nothing enters the repository but short quotations with page numbers.
- **(B) The in-app browser.** Authorise a worker to display those PDFs in the browser pane (viewing only; stop at any
  bot check). The browser may cache the file on disk; the owner should decide whether that is acceptable under "no
  PDF on disk".

**Reading plan, in order of leverage (targets taken from CMP 109's citations, N109 §9.7, and GOS):**
1. **CMP 102:277-309** — Theorem 1 (exact hypotheses; ε_0′, B_3), Sect. C (Eqs. 59-62), Sect. E (Prop. 8), Sect. F
   (Eqs. 162-163; local coordinates exp iηH), Sect. G (multiscale minimisers), Prop. 9 and (190) (rate δ_0), Eqs. (41),
   (46), (103), (171), (174), (179)-(180), (196)-(197). Settles T-a exactly; shows whether the existence proof inducts
   (as GOS does) and how the constraint's non-linearity is summed over levels — the hard-scheme version of §7.6.
2. **CMP 99:389-434** — Sect. D (H_{1,j}, Δ_1), (3.35)-(3.38), (3.109)-(3.110), (3.126)-(3.129), (3.139), (3.147),
   (3.156): the background class, the decay rate, the constants. Settles (GAP-Z) and the FLOW question.
3. **CMP 99:75-102** — (1.3)-(1.10), (1.17), (1.29), (1.43)-(1.54), (1.66), (1.80), Lemma 1, Prop. 5, the map u_k.
4. **CMP 95** ((1.29)-(1.37), (1.66), (1.103)) and **CMP 96** — (G♯_0-field).
5. **CMP 98** — Prop. 2; (32)-(41), (77), (97), (106).
6. **CMP 116, CMP 119 Sect. 2, CMP 122 I-II** — cluster expansion, the full inductive hypotheses, the R operation.
7. **The coupling flow.** Identify the "separate paper" promised at CMP 109 pp.259-260; none was found. Balaban's ICM
   1986 lecture (free PDF on the IMU site) may say where.

## 11. Errata to the sections above (append-only)
- **§5 M7:** "≈ (β/C)g_k³·ε_1" should read: between (β/C)g_k³ε_1 and (β′/C)g_k³ε_1 where the log term of (0.31)
  dominates (from γ_k = C log(L^kε)^{-1} and (0.31)); in all cases not ∝ g_k.
- **§7.6:** with r_j := Qx_j − x_{j+1} and the quadratic part of the penalty, the level-0 equation is ∇S_W(U_0) +
  κ_0Q^Tr_0 = 0 (sign), and κ_{l-1}r_{l-1} = κ_lQ^Tr_l for 0 < l < k at linear order.
- **§7.4:** "a gap of order one in block units that dominates O(field strength) background effects for regular
  backgrounds" is **my inference** from the constrained structure (a_kQ_k^TQ_k, or restriction to ker Q_k, with
  curvature < ε_0 in block units), not a statement read in CMP 99:389.
- **§0 item 4:** superseded by §8's count (7 REFUTED in PROOF.md, 4 load-bearing; 1 lead-file paraphrase in 2 places).

## 12. Summary table

**Extraction (T-a … T-d):** primary bodies READ: 0 of 12. LANE-READ items used: CMP 109 statements in §3.1, §4.1,
§5 M2/M4-M9, §6. READ-SECONDARY: GOS, DIM1, DIMQ, DIMF [1×], DIMO, BFKT, CH. Metadata READ: ZB (all twelve), CR (four).

| # | Item | Verdict |
|---|---|---|
| A-1 | Access to every Balaban CMP body through WebFetch/WebSearch | **BAL-F1 FIRES** (§1) |
| A-2 | PDF-on-disk incident (tool auto-save of one arXiv PDF; not read; path in §1) | reported |
| T-a | CMP 102: existence/uniqueness/regularity/analyticity | LANE-READ (as CMP 109 quotes it) + READ-SECONDARY (GOS); exact constants NOT-READ |
| T-b | CMP 95/96/99:389 propagators and random walks | scalar/abelian analogues READ-SECONDARY; non-abelian background version NOT-READ |
| T-c | Why constants do not compound (M1-M9) | LANE-READ + READ-SECONDARY |
| T-d | CMP 98/109/116/119/122; volume; sources; symmetry | ZB + LANE-READ; no Balaban statement on observables, rotation invariance of limits, or infinite volume |
| T-e | Wall map, six walls | §7.7; FLOW's H_⊥^{-1} is route-specific; (N-bg)/(H-C) corollaries of analyticity; (SPD)/(W2) and the k-factor have no direct counterpart |
| §7.5 | Hard constraint absorbs Ran Q_k^T sources exactly; soft constraint shifts data by s/κ | PROVEN-HERE (elementary; needs the cross-family check before banking) |
| B3-1 | PROOF l.1000: CMP 102 Thm 1 "about (0.4)" | **REFUTED** (load-bearing) |
| B3-2 | PROOF l.6707: background-field covariances = CMP 95/96/102b | **REFUTED** (load-bearing; it is CMP 99:389) |
| B3-3 | PROOF l.1345-1347: β_j → 2b0 ln L sourced to CMP 109 | **REFUTED** for CMP 109 (load-bearing) |
| B3-4 | PROOF l.4367-4368: thresholds φ_j ~ g_j; "never iterate" | **REFUTED** as attribution (load-bearing for T56-4 framing) |
| B3-5 | PROOF l.870: thresholds ≲ p(g_k)g_k | **REFUTED** for CMP 109 (not load-bearing; already narrowed) |
| B3-6 | PROOF l.752: "L sufficiently large" | **REFUTED** (stale; not load-bearing) |
| B3-7 | PROOF l.653/l.894: "(1.2) is L1e's hypothesis" | **REFUTED** as identity (|J| clause; not load-bearing) |
| B3-L | PLAN_S26 §2e + RTARGET §55 T56-4: "threshold scaling with g_k, as Balaban uses" | **REFUTED** |
| B3-8 | PROOF l.5288, HANDOFF l.213, LINEAR_PACKAGE l.483: coupling flow in CMP 119 | NOT-VERIFIED (contrary evidence) |
| B3-9 | PROOF l.6681: Balaban's convention = composite critical point | CONFIRMED vs N109 |
| B3-10 | PROOF l.6166: CMP 102b uniqueness is local (small-field class) | CONFIRMED vs N109 |
| B3-11 | PROOF l.3810: torus side arbitrary in stopping-scale units | CONFIRMED vs N109 |
| B3-12 | PROOF l.4139-4140: thresholds dimensionless per level | CONFIRMED vs N109 |
| P-2a | PLAN_S26 §2a: k-fold background, k-uniform propagators | CONFIRMED vs N109 + secondary |
| P-2e | PLAN_S26 §2e: k-uniformity "from random-walk expansions" | CONFIRMED, incomplete (misses M5) |
| N-1..4 | PROOF l.977 (L2), l.1150 (L3g), l.1181, l.1463 (L5) | NOT-VERIFIED (consistent where checkable) |
| BAL-F2 | Does k-uniformity need the hard constraint? | NOT decided; localised to (SPD)/(W2) and the level count (§9) |

**Counts (paraphrase verdicts): CONFIRMED 6 (all against N109/secondary, none against a body), NOT-VERIFIED 5,
REFUTED 8 (7 in PROOF.md, 4 of them load-bearing; 1 in PLAN_S26 + RTARGET).** No PROOF.md item changes status
category: every affected item was already IMPORTED-NOT-YET-REVERIFIED or OPEN and stays so.

**Codex input used: KFACTOR55.md (gpt-6-astra/max, unreviewed).** I agree that its two rows are linear in the soft
residual r_l (checked against BFT_A's definition r_j(x) := Qx_j − x_{j+1}); I agree that a level count times a
fixed-size quantity is the source-level diagnosis (KF-F2) and that it is not Balaban's mechanism to absorb it by AF
or g_k-thresholds; I add (§7.6) that the rows have a hard-scheme analogue through the Lagrange multiplier, so the factor
is not automatically a soft-scheme artefact, and that it may be a currency effect — which is KFACTOR55's own "least
certain point". I did not re-derive its Eq. (1) or its constant 121/13.

## 13. Second errata block (self-review of §0-§12, appended 2026-10-28T23:30:49Z)
- **§1 table, zbMATH row:** "keywords are available for all" overstates what I fetched. ZB records (review or licensing
  notice) were read for all twelve papers; **keywords were fetched for ten** (CMP 95, 96, 98, 99:75, 99:389, 102:277,
  116, 119, 122 I, 122 II), not for CMP 102:255 or CMP 109. §12's "ZB (all twelve)" means records, not keywords.
- **§0 item 3 and §7.4, "always for the constrained operator":** read "in every use recorded in CMP 109 (N109 §9.4-9.7)
  and in Dimock's analogues" — the body of CMP 99:389 was not read, so "always" is not established.
- **§7.3, last sentence:** delete the support from NBG_ADJ. PROOF.md's header marks the [S25-fix 5] obstruction counts
  as REVERTED (REVIEW55_LEAD H14c, "the count of two is not established"). My statement that (N-bg)/(H-C) are
  corollaries of an analytic BFT-0 rests only on Balaban's architecture (M4), not on NBG_ADJ.
- **§7.5:** "Symbol warning, §8.3" should read §8.5. "moves the minimiser by H_k(s/κ) ≠ 0" should read "moves it by
  −H_κ(s/κ), H_κ the soft-constrained minimiser operator, which is non-zero for s ≠ 0". The data-shift identity:
  (κ/2)|QA − B|² + ⟨s, QA⟩ = (κ/2)|QA − (B − s/κ)|² + ⟨s, B⟩ − |s|²/(2κ).
- **§6.4:** "every rotation-non-covariant term is in Π′" is too strong. Correct: every rotation-non-covariant
  contribution to the quadratic marginal term is of higher order in p — either in Π′ (third order in d, d̄) or in the
  lattice corrections of the transverse form itself (Δ(p) = Σ_μ 4 sin²(p_μ/2) = p² − (1/12)Σ_μ p_μ⁴ + …); both are
  irrelevant. The O(4)-covariance statement is about the O(p²) part only.
- **§5 M4:** "derivatives come from analyticity (Cauchy)" is my reading of the structure that N109 records (analytic
  extensions (3.1)-(3.17), Lemma 4 (3.53), the fifth-order Taylor remainder (3.34)-(3.35), bounds on complexified
  spaces); CMP 109's text, as transcribed, does not use the word "Cauchy".
- **§4.2 DIMQ:** from a single fetch [1×]; it agrees with the lane's independent session-5 reading (NOTES §6).
- **§8.1 B3-1, "Correct statement":** the averaging CMP 102 actually uses is **inferred** (dates; CMP 102's reference
  list contains CMP 98; CMP 109 p.252-254 presents (0.4) as new and contrasts it with CMP 98's). The refutation of
  "about (0.4)" rests on CMP 109 introducing (0.4) as its own new definition; which averaging CMP 102 uses is
  NOT-VERIFIED until its body is read.

**End of BALABAN_EXTRACT (worker: claude-opus-5-5; last append 2026-10-28T23:30:49Z).**
