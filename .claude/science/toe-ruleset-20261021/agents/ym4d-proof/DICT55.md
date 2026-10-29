Reviewer model: claude-opus-5-5

# DICT55 — the proof's single dictionary: every object pinned before estimates are reused (session 26, worker file)

UTC start: 2026-10-29T04:58:39Z
Author role: Opus 5.5 worker (brief: scratchpad/queue/dict.md; shared rules: scratchpad/REVIEW_BRIEF_55.md).
Writes: this file and checks/dc55_* only. No git. Append-only (later sections may correct earlier ones; nothing is deleted).
Source of the commission: CODEX_REVIEW_ASSEMBLY.md, "Corrected ordered OPEN work list", item 3 ("Pin the source dictionaries
and hypotheses before reusing estimates").

## PRE-STATED (written before any derivation or dictionary entry; statements only)

Targets.
- D1. **One canonical name and definition per object** (file + locating string), with every alias found in the lane mapped
  to it (file + locating string), for at least: (a) the three action towers E^br / E^cb / E^min and the per-level functionals
  they are built from; (b) the soft-kernel functional φ (φ̂) versus k̃, and the normalisation of each; (c) κ_j, and every other
  lane object written κ; (d) every gauge slice and orbit norm in use (S_E, Γ, Γ_E, Γ^(T), the NSL slice, BR1's slice, axial,
  Λ_HC, the "per-level covariant slice"); (e) the contour convention (lower-corner versus centred); (f) distance units; (g) the
  coefficient-field norm (sup versus sup-plus-Wilson-Hölder); (h) the gauge-action convention (U^a)^b; (i) the source/field
  norms and weights that banked statements are written in (𝔐, N(S), N_m(S), ‖·‖_inv, the weight triple, m); (j) the domain
  classes (𝒞_glob, the curvature-small class, PD-glob, 𝒮_K).
- D2. **The lane-A linear inputs.** The exact list behind "conditional on the named lane-A linear inputs" in Theorem K^(σ),
  GV-E (and BFT-E), BFT-1/2 and NSL: statement, file, locating string; and for each a status class: **banked cross-family**
  (in PROOF [S26-BANKED] with a Codex scope), **re-verified** (re-derived in a named review file, not cross-family banked),
  or **only stated** (asserted, cited or imported without an on-disk re-derivation I can locate).
- D3. **Banked item × object matrix.** For every [S26-BANKED] bullet: which D1 objects it is stated in. **Flags**: two banked
  items using different objects under one name, or a consumer chaining across a convention change (per-level slice vs S_E;
  lower-corner vs centred contours; E^br vs E^cb vs E^min; φ vs k̃; sup vs ‖·‖_cf; 𝒞_glob vs curvature-small; Z = 1 vs Z ≠ 1;
  m = 0 vs m > 0), each with the precise repair (restatement) or the missing lemma.

What would count as a refutation of an entry in this file (for the Codex checker).
- R1. A locating string that does not occur in the named file, or occurs but denotes a different object than the entry says.
- R2. An alias mapped to a canonical object while the file's own definition differs in normalisation, domain/class, slice or
  gauge convention, norm/weight, quantifier order or units.
- R3. Two objects identified where no bridge lemma on disk identifies them on the domain in question, or kept apart where the
  files define them identically.
- R4. A lane-A input listed with the wrong status class, or an input that one of the four named banked results uses but this
  file omits.
- R5. A flag whose convention change is not real (both sides use the same object), or a missed flag where a banked item or a
  consumer chains across a convention change.
- R6. A numeric check (if any is run) that could not have failed.

Method commitments.
- Large files (PROOF, BFT_B, PLD, BFT_A, HW, FLOW, SF, SQ, HIST) only by grep -n then sed -n ranges; citations by locating
  string (line numbers drift; any line number given is "as read at the time stated" and is secondary).
- Codex review files read as they are on disk now; unfinished tails flagged.
- "Pinned" in this file means: I read the defining text at the cited string myself. Where I only read a quotation of it in
  another file, the entry says "quoted, source not read".
- Any numeric check gets checks/dc55_<id>_criteria.md before its script; exact arithmetic (fractions) only.
- Verdict words per entry: **PINNED** (definition read at source), **MAPPED** (alias read at source and its definition matches the
  canonical one in every listed respect), **DIFFERENT OBJECT** (read at source; differs — named difference), **NOT-VERIFIED**
  (could not settle; says what is missing). Flags carry **CONFIRMED / NOT-VERIFIED / REFUTED** in the shared-rules sense when
  they rest on a mathematical claim.

---

## §0. Read record, provenance, and how to read an entry (appended after the PRE-STATED block)

**Provenance.** Every entry below was written by claude-opus-5-5 (this worker). No entry is a Codex verdict; where an entry
uses a Codex review it says so, and §8 states agreement or disagreement explicitly. Pre-session-24 lane reviews
(REVIEW_BFT_A_S*, REVIEW_BFT_B_S*, REVIEW_S*, the reviews named in LINEAR_PACKAGE's header) record "independent session"
or "independent agent" and **no model**; I report them as "pre-S24 lane review, model not recorded" and never as
cross-family.

**Read (bounded ranges located by string; large files only by grep + sed).** PROOF.md: the header and the whole
[S26-BANKED] block (bullets "(T-UNIF), repaired" through "Node A convexity"), "S1 Lattice"/"S3 Wilson action"/"S4
Averaging", "Decision 4: the RG kernel", "Lemma N2-a" (SU(N) part, E_NA), "Proposition B-NA-red", "Lemma NA-alg", "Setting
N5-bg", "Lemma N5-cov", "Lemma U0", "Lemma BR1", "(MIN_1)", "(BG-unif), precise statement", "(H-C) **in its extended form",
"Lemma TOWER-VAR", "Proposition COMP". BFT_A.md §1, §2 (BA-1…BA-12), §7.1-§7.3, §12.0-§12.2, §26.0-§26.2, §31.0-§31.3.
BFT_B.md §12.2, §13.3, §15.0-§15.1, §27.1-§27.5. LINEAR_PACKAGE.md header, §1.1-§1.5, §3 (Lemmas 3.1, 3.2, 3.2″, Theorem
3.8), §4 (Theorems 4.2, 4.2′). FLOW.md §0, §3.1 incl. "[RFL-fix §3.1", "Def F-strip", §15 "Lemma F-norm". HIST.md §0,
§14.0-§14.2 ("Lemma HF"), the E^♭ / (a5-U) block. RLARGE.md §0. SF.md "(BG-unif) [HYPOTHESIS", "(a5-G♯)", "(a5-U)
[restated". NORMS.md "Conventions" (l.≈99-110). REVIEW_S22.md "Statement (BFT)". ASSEMBLY55 (§1-§7) and
CODEX_REVIEW_ASSEMBLY (all, complete; final checkpoint 04:48:14 UTC). NSL55 §0, §2, §3.0-§3.1, §4.0-§4.4, §5; CODEX_REVIEW_NSL
F3-F10 and "Exactly what may be banked" (complete). KFACTOR_OFF55 §0-§1, §4, §6; CODEX_REVIEW_KOFF §5 and banking list
(complete). GV55 §0-§3.4; CODEX_REVIEW_GV §2, §7 and banking list (complete). BFT4W55 §1, §2.1-§2.2, §4.0-§4.2;
CODEX_REVIEW_BFT4W W3 and banking list (complete). BFT34_55 §0.2, §1.1-§1.3. GSHARP55 §1, §4.2; COFM55 §1; COFUN_CC §1,
§4.1, §5 head, §6.3; SRCAN55 §1, §2.1; CODEX_REVIEW_SRCAN items 4 and 13 and banking list; SRCCD55 §1, §3.1 (𝒮_K),
Lemma V setting; FLOW55 §3.4-§4.2, §9; CODEX_REVIEW_FLOW55 §1.2 and banking list; UIR55 PRE-STATED symbol pins, §3.4,
§3.6; CODEX_REVIEW_UIR provenance and banking list; CODEX_REVIEW_BALX F2, F3, F11 and banking list; ALIGN55 §1, §5.4 head;
HINT55 symbol table, §1.1, §3.1; LCONV55 (β, u_0 lines); REVIEW55_NORMS r55n-F4; SYMBOLS §6 and CODEX_REVIEW_SYMBOLS F9;
the banking sections of every CODEX_REVIEW_* cited in [S26-BANKED] (collected in one pass). Codex files were read as on
disk at 04:58-05:20 UTC; every one cited in [S26-BANKED] ends with a complete banking list or final table except
CODEX_REVIEW_TUNIF2, CODEX_REVIEW_X1, CODEX_REVIEW_P4 and CODEX_REVIEW_KN, which have no section titled "Exactly what may
be banked" (they end with a final verdict / summary table instead; I read their last lines and they are complete).

**Entry format.** Locators are written as FILE: string between white square brackets (U+27E6 … U+27E7) — FILE relative to the lane directory, string an exact one-line
substring of FILE (checked by dc55_1, §6). Verdict words: **PINNED** (definition read at its source), **MAPPED** (alias read
at its source; same object in every listed respect), **DIFFERENT OBJECT** (read at its source; the difference is named),
**NOT-VERIFIED** (what is missing is said). A dictionary entry restates no theorem; it says what a symbol denotes.

---

## §1. Conventions (the frame every later entry is written in)

### C1. Level index, depth, and their direction — PINNED
- **Canonical.** Level 0 = the bare (finest) lattice; level j = after j RG steps; a depth-k composite problem has unknown
  levels 0, …, k−1 and its datum at level k. ⟦BFT_A.md: κ_j ∈ [κ_-, κ_+], depth k ≥ 1, coarse torus side T⟧;
  ⟦FLOW.md: level k = after k RG steps, k = 0 the bare lattice, k = K the unit lattice⟧;
  ⟦RLARGE.md: Level k = after k RG steps; k = 0 bare, k = K the unit lattice⟧. Reference scale = level K (spacing 1):
  ⟦SRCCD55.md: L^r a, level-r spacing; ℓ_K = ℓ_ref = 1⟧. ASSEMBLY55 §2 checked SRCCD55, HINT2_55, FLOW55, RLARGE for this
  (I re-read SRCCD55, FLOW, RLARGE: MAPPED).
- **Depth** (NSL55): ⟦NSL55.md: **j** = depth (1 ≤ j ≤ k); i, l = levels.⟧ — the depth-j problem is the depth-"k := j"
  problem on a torus of coarse side T_j = TL^{k−j}. MAPPED.
- **DIFFERENT OBJECT — PROOF's resolution index runs the other way.** ⟦PROOF.md: in physical units with the resolution-0 spacing equal to 1⟧ and ⟦PROOF.md: resolution K, with spacing ε_K = L^-K⟧: resolution j = level K − j. Codex records the
  same collision against Dimock: ⟦CODEX_REVIEW_BALX.md: Dimock k counts coarse-graining; current PROOF :1376–1378 uses resolution j in the opposite direction⟧. HINT55's m := K − k is a third index (levels below the unit lattice):
  ⟦HINT55.md: m := K − k ≥ 0 (levels below⟧.
- **DIFFERENT OBJECT — "m" as a depth.** ⟦KFACTOR_OFF55.md: m := k − 1 − j)⟧ is a depth offset, not a weight rate; pinned
  as such by ⟦GV55.md: **m** is a weight rate in COFM55 and GSHARP55, but a **depth index m := k − 1 − l** throughout KFACTOR_OFF55⟧. Other files write the same depth offset q := k − 1 − l (GV55, BFT4W55, ALIGN55, GSHARP55).

### C2. Units and distances — PINNED
- **Coarse units** (canonical for every BFT/linear-package norm): one coarse unit = one level-k lattice spacing.
  ⟦BFT_A.md: Level-j 1-form: x^c_j := L^{k-j}x_j. Level-j 2-form: H^c := L^{2(k-j)}H.⟧;
  ⟦BFT_A.md: Level-j plain current: j^c := L^{3(k-j)}j (BNA-F2's convention).⟧;
  ⟦BFT_A.md: Residual of x at level j: r_j(x) := Qx_j - x_{j+1} (linear), coarse r^c_j := L^{k-1-j}r_j.⟧ One own level-l
  step = h_l = ρ_l = L^{−(k−l)} coarse units: ⟦BFT_A.md: ρ_j := L^{-(k-j)} (one level-j step in coarse units)⟧ (aliases
  ⟦BFT4W55.md: h_l := L^{−(k−l)} (one own level-l step in coarse units)⟧, ⟦ALIGN55.md: ρ_l := L^{−(k−l)} (one level-l step in coarse units)⟧ — MAPPED). The plain-current unit π_l(j) := L^{3(k−l)}·sup_own|j| = ‖j^c_l‖_∞ is the same object in
  BFT_B §27.1, KFACTOR_OFF55 §1.1, COFUN_CC §1, BFT34_55 §0.2, BFT4W55 §1 (MAPPED; d = 4 so L^{(d−1)(k−l)} = L^{3(k−l)}).
- **Own units** (FLOW/UIR/HIST "level units"): ⟦FLOW.md: Everything at level k is in level-k units.⟧; at depth k the
  level-k own unit IS the coarse unit, so FLOW's level-n jets and BFT's level-k coarse quantities are in the same length
  unit (used by F23's arrow; see §5 FL9). MAPPED.
- **Physical units** (OS/flow-time/witness files): unit lattice = level K = ℓ_ref = 1; continuum flow time t in these units:
  ⟦HINT55.md: t = continuum flow time (physical units, unit lattice = 1)⟧. A level-j coarse unit of a depth-k problem is
  L^{k−K}·ℓ_ref physical units — the conversion every consumer from the OS side must apply (no banked item applies it
  silently; checked in §4).
- **Distance (weights, decay).** The ℓ¹ torus distance of coarse positions:
  ⟦LINEAR_PACKAGE.md: d(z, z') := the ℓ¹ torus distance between coarse positions (an object at level l sits at L^{l-k}·(its base point)).⟧ (canonical); ⟦COFM55.md: **dist** := ℓ¹ torus distance of coarse positions (never ℓ^∞ unless said)⟧ (MAPPED); BFT's statement uses ⟦REVIEW_S22.md: exponential weights e^{±m d} are in level-k ancestor distance⟧
  (MAPPED: "level-k ancestor" = the coarse position). BFT-3's tree length: ⟦BFT34_55.md: **𝔱** := minimal spanning tree length (BFT's "tree"), **𝔱_S** := minimal Steiner tree length, both in level-k ℓ¹ units⟧ (MAPPED). ℓ^∞ appears in two
  places only, both explicit: Hölder pairs ⟦BFT_A.md: **pointwise** [H]^∞_α := sup over base points z ≠ z', |z - z'|_∞ ≤ 1⟧
  and box radii, converted by ⟦BFT4W55.md: An ℓ^∞ radius a is an ℓ¹ radius ≤ 4a⟧ (d = 4). PINNED.

### C3. Positions and the contour convention — PINNED (Convention C canonical)
- **Canonical: Convention C (centred).** A level-j site sits at the coarse position of its level-0 root (the centre of its
  level-j block); a coarse link sits at the centre of its S4′ contour family:
  ⟦BFT4W55.md: ### 2.1 Positions — Convention C (centred). Load-bearing; see Proposition CORNER (§4.2)⟧,
  ⟦BFT4W55.md: pos(Z) := L^{−k}(L^jZ + ((L^j − 1)/2)𝟙)⟧. Roots are block centres throughout the lane:
  ⟦PROOF.md: and their roots are the block centres c_X (L is⟧, ⟦BFT_B.md: Root convention: block centres (§15.0)⟧.
- **DIFFERENT OBJECT (positions only): Convention K (lower corner).** ⟦LINEAR_PACKAGE.md: d(z, z') := the ℓ¹ torus distance between coarse positions (an object at level l sits at L^{l-k}·(its base point)).⟧ and
  ⟦COFM55.md: coarse position of a level-l object = L^{l−k}·(base⟧. For weights e^{μd} the two differ by < ½ coarse unit in
  ℓ^∞ (a factor ≤ e^{2μ}); **for cutoff multipliers at σ > 0 they are not interchangeable** — the banked Proposition CORNER:
  ⟦BFT4W55.md: **W-mult^σ is false under Convention K for every σ ∈ (0, 1]:**⟧, confirmed in
  ⟦CODEX_REVIEW_BFT4W.md: ### W3. Centred cancellation and the lower-corner obstruction survive the errata⟧. At σ = 0 the
  multiplier bound is convention-blind: ⟦BFT4W55.md: lane B's W-mult (σ = 0) is convention-blind⟧. BA-12's CEN1 is
  Convention C implicitly (its midpoint m_c is the contour centre; BFT4W55 §4.1 makes this explicit).
- **The contour family itself.** S4′ = the order-PAIRED family (same axis order σ at both ends):
  ⟦LINEAR_PACKAGE.md: - **S4' (order-averaged averaging; l.454-481).** For each of the 4! coordinate orders σ, P^σ is the complete-axial⟧. Balaban's (0.4) averages the two families independently — **DIFFERENT OBJECT beyond linear order**:
  ⟦LINEAR_PACKAGE.md: the two operations agree at linear order, which is all this package uses, and differ beyond it⟧.
  Codex's most dangerous item for KN_ADOPT is exactly this identification:
  ⟦CODEX_REVIEW_KN.md: whether the actual decision-4 normalized kernel uses exactly the paired indexed mean quoted in KN_ADOPT⟧ (NOT-VERIFIED there; I did not re-verify it).
- **Orientation.** All S4′ contours run c_X → c_Y: ⟦NSL55.md: (all S4′ contours run c_X → c_Y; PROOF⟧ (PINNED).

### C4. Gauge action, (U^a)^b — PINNED (left action canonical); two right-action passages flagged
- **Canonical (left action).** U^g(b) := g(b^−)U(b)g(b^+)^{−1}, hence **(U^a)^b = U^{ba}**, and the infinitesimal action in
  exponential coordinates is K_0 = −Ξ: ⟦NSL55.md: - **Gauge action** (BFT_A §31.0 convention, K_0 = −Ξ): (x^g)_i(b) := log(g_i(b^−)e^{x_i(b)}g_i(b^+)^{−1}); left action,⟧ and ⟦NSL55.md: (x^g)^{g′} = x^{g′g}.⟧;
  ⟦BFT_A.md: (K_xξ)_j(b) := d/dt|_{t=0}log(e^{tξ_j(b^-)}e^{x_j(b)}e^{-tξ_j(b^+)})⟧, ⟦BFT_A.md: K_0 = -Ξ in this sign convention⟧. Aliases, all MAPPED: ⟦PROOF.md: (gU)_b := g(x)U_bg(x + e_μ)^{-1}⟧ (prefix notation of the same left
  action); ⟦PROOF.md: It is gauge covariant: under a fine gauge transformation g, M̄_c → g(c_X)M̄_cg(c_Y)^{-1}⟧;
  ⟦BFT_B.md: with the convention (U^a)^b = U^{ba} used in 19.13 and 22.12⟧. The covariant generator of ALIGN55/BGT55,
  ⟦ALIGN55.md: (d_Zλ)(b) := Ad_{Z(b)}λ(head b) − λ(tail b)⟧, is the same left action differentiated in the trivialisation
  U → e^AU (PROOF Setting N5-bg's "Left-trivialised coordinates"): δA = λ(tail) − Ad_Z λ(head) = −d_Zλ, i.e. K = −Ξ_Z;
  CODEX_REVIEW_BGT item 4 banks it in either sign ("or with the minus sign for the positive-d Ξ′"). MAPPED.
- **DIFFERENT CONVENTION (right action), two passages.** ⟦BFT_B.md: (a) With V^g(x, y) := g(x)^{-1}V(x, y)g(y), the axial frame is g(x) = hol_V(γ_x)^{-1}⟧ (BFT_B §13.3, Lemma GI-frame): (V^a)^b = V^{ab}; and the (CovLift) cocycle as printed,
  ⟦BFT_B.md: ĥ(h_1h_2, V) = ĥ(h_1, V)ĥ(h_2, V^{h_1})⟧, which is the right-action order (its own [RBB7-fix RS7-8] gives the
  left-action order ĥ(h_2h_1, V) = ĥ(h_2, V^{h_1})ĥ(h_1, V)). The review that confirmed GI-cov wrote its derivation in the
  right action: ⟦REVIEW_BFT_B_S4.md: For the right action, Ad_{g_1g_2} = Ad_{g_2}∘Ad_{g_1}.⟧. **Conversion:** the right
  action by g is the left action by g^{−1}; every statement transfers after g ↦ g^{−1} and reversal of products of gauges.
  Exact check dc55_2 (PASS, all four controls fire) verifies both composition laws and both cocycle orders on non-commuting
  rational matrices. **Consequence for the banked block:** none at present — no [S26-BANKED] bullet uses (CovLift)'s cocycle
  (GZ-SLOT/GZ-FALSE is about (CovLift)(iv)'s g_Z clause, not the cocycle); BFT-4 (b) work (BFT4B55, not banked) must state
  which order it uses (§5 FL12).

### C5. Lie-algebra norms and coordinates — PINNED (Hilbert–Schmidt canonical for the composite functional)
- **Canonical.** |X| = Hilbert–Schmidt norm, |X|² = −tr X², for every BFT/NSL/linear-package statement:
  ⟦PROOF.md: Norms are Hilbert-Schmidt,⟧ (NA-alg); Setting EΠ works "su(N) componentwise in an orthonormal" basis
  (⟦BFT_B.md: Setting LIN of BFT_A §7.1 at the trivial chain (su(N) componentwise in an orthonormal⟧), orthonormal for the
  HS inner product. With S_W's quadratic part ½‖dA‖²_HS (C7) the composite functional's quadratic form is Setting SC's per
  component.
- **DIFFERENT NORMALISATION — FLOW/HIST "normalised Lie coordinates".** ⟦FLOW.md: V_b = exp(Σ_a B^a_b t_a), {t_a} a basis of su(N) orthonormal for ⟨X, Y⟩ := -(1/N)tr(XY)⟧ with ⟦FLOW.md: (so ||t_a||²_HS = N)⟧ and
  ⟦FLOW.md: t_a = i√(2N)T^a⟧; HIST's polydisc is written in them: ⟦HIST.md: 𝔇_α(X) := {|B^a_b| ≤ α_E in normalised Lie coordinates of a local gauge on X}⟧. **Conversion (exact):** an HS-orthonormal coordinate y^a and FLOW's B^a obey
  y^a = √N·B^a; a FLOW polydisc |B^a| ≤ α is an HS-coordinate polydisc |y^a| ≤ √N·α.
- **DIFFERENT NORM — operator norm.** RLARGE's cut and SRCCD55's coarse small-field set are op-norm statements:
  ⟦RLARGE.md: χ_Q := Π_{p⊂int Q}1{||1 - U(p)||_op < ε_1}⟧, ⟦SRCCD55.md: U_K with max_P|log U_{K,P}|_op ≤ ε_0 (BFT's ε_0 at level K)⟧. HIST's bridge ⟦HIST.md: s(U) := 1 - N⁻¹Re tr U; inequality (B): s(U) = ||1 - U||²_HS/(2N) ≥ ||1 - U||²_op/(2N).⟧ relates them. (|X|_op ≤ |X|_HS ≤ √N|X|_op.)

### C6. Coupling normalisation — PINNED (u = 1/g² = β_Wilson canonical)
- **Canonical.** u_k := 1/g_k² is the coefficient of the level-k Wilson density s: u = β_Wilson = 2N/g_std².
  ⟦FLOW.md: s(U) = 1 - N^{-1}Re tr U. So u = β_Wilson = 2N/g_std², where g_std is the coupling of (1/(4g_std²))∫F^aF^a with⟧; ⟦RLARGE.md: u_kΣ_ps(U_p) with **u_k := 1/g_k² = β_Wilson = 2N/g_std²**⟧; the conversion
  proof ⟦FLOW.md: *Claim.* u = 2N/g_std² exactly (at the level of the marginal term).⟧ (Lemma F-norm). Balaban's g_B is
  this g: ⟦FLOW.md: (1/g_B²)Σ[1 - Re tr U] with⟧. Files on the canonical g (MAPPED): HIST, RLARGE, FLOW, FLOW55, UIR55
  (⟦UIR55.md: β_0^std := 2N·2b_0 = 11N²/(12π²) in u-units (FLOW §0), b_0 = 11N/(48π²).⟧), SRCCD55 (Lemma V:
  ⟦SRCCD55.md: Wilson measure ω on a hypercubic torus Λ = (aZ/RZ)⁴ with R/a even, SU(N), N ≥ 2, u_0 = 1/g_0². Here⟧),
  SRCAN55 (⟦SRCAN55.md: the chain's own coupling sequence (RLARGE (F_R)); g_0 = g_bare, u_K = 1/g_ref²⟧), HINT2_55 (the
  banked instanton correction 8π²u → (4π²/N)u is this u), LCONV55 (u_0 = 1/g_0²).
- **DIFFERENT NORMALISATION — the standard g.** ⟦PROOF.md: S_K(U) = β_K Σ_p (1 - N^-1 Re tr U_p), with β_K = 2N/g_K^2.⟧
  (PROOF S3: here g_K = g_std at the UV resolution K, and β_K = u_0 in the canonical notation); SPHERE55's profile
  ⟦SPHERE55.md: beta_Q = 2N/G(a Omega(z_Q))^2: the bare coupling is a fixed function G of the LOCAL PHYSICAL SPACING s = a Omega⟧ (G = g_std); HINT55's free coefficient is written with g_std and converted explicitly:
  ⟦HINT55.md: In FLOW's normalisation u = β_Wilson = 2N/g_std², so A_∞g_std² = 3(N² − 1)·2N/(128π²u).⟧ **Hazard:**
  HINT55's own symbol table uses the canonical g (⟦HINT55.md: u_k := 1/g_k² along the tuned sequence (FLOW Def F-g).⟧)
  while its §3.1 uses g_std; both are explicit, so no error, but g² differs by the factor 2N between the two uses.
- **Not fixed: the "g" of PROOF's Decision-4 kernel.** ⟦PROOF.md: k_c := exp(-(κ/g²)[1 - N^{-1}Re tr(V_c^{-1}M̄_c(U))])⟧
  does not say which g. Read with S3's g_std the kernel stiffness relative to the Wilson density is κ/(2N); read with the
  canonical g it is κ (as in HIST/RLARGE/FLOW). The lane's consumers all read the canonical one (C8); PROOF should say so
  (§5 FL10; bookkeeping).

### C7. Wilson density, Wilson action, bare weight — PINNED
- s(U) := 1 − N⁻¹Re tr U (HIST §0, FLOW §0, RLARGE §0; quoted in C5/C6). **S_W(U) := Σ_p Re tr(1 − U_p) = N·Σ_p s(U_p)**:
  ⟦PROOF.md: with S_W(U) := Σ_pRe tr(1 - U_p) and φ̂ := Nφ⟧ (the composite functional's Wilson term, coefficient 1).
  The bare weight is e^{−u_0Σ_p s(U_p)} = e^{−(u_0/N)S_W(U)}: ⟦RLARGE.md: W(U_0, …, U_K) := e^{-S_0(U_0)}Π_{i<K}K_i(U_{i+1}, U_i)⟧ with ⟦HIST.md: (I_0^E) holds: 𝓔_0 = Σs, E_0 ≡ 0, u_0 = 1/g_0² (the bare action is exactly the main term).⟧. BFT-4's
  S_W is the same object at level k: ⟦BFT34_55.md: S_W(V_k) is the level-k Wilson action with coefficient 1 (β factored out⟧ (MAPPED).

### C8. The RG kernel — PINNED; the φ- and k̃-splittings are two exact rewritings of ONE kernel
- Decision 4's normalised kernel (C6 locator) and RLARGE's ⟦RLARGE.md: k^{(i)}_c(V; M) = e^{-κu_iφ_M(V)}/∫e^{-κu_iφ_M}⟧
  and HIST's ⟦HIST.md: k^{(i)}_c(V, U) = exp(-(κ/g_i²)[1 - N⁻¹Re tr(V⁻¹M̄_c(U))])/𝒩_i(M̄_c(U)) (D4-norm)⟧ are the
  **same kernel** (MAPPED): 1 − N⁻¹Re tr(V⁻¹M) = φ_M(V) + [1 − N⁻¹Re tr(W_0⁻¹M)], and the bracket does not depend on V, so it
  cancels between numerator and normaliser. FLOW's ⟦FLOW.md: -log k_c(V, U) = κu·k̃(V_c, M̄_c(U)) + log 𝒩'(P_c(U))⟧ is a
  third exact rewriting. The kernels agree; **the "tree exponents" read off them do not** (k̃ = φ + d(M), O2 below).

### C9. Hölder seminorms — PINNED (Campanato canonical for 𝔐-type norms)
- Campanato [H]_α (lattice boxes of side between one own step and one coarse unit) and pointwise [H]^∞_α:
  ⟦BFT_A.md: - **Campanato** [H]_α := sup over lattice boxes B (any corner; side ρ an integer multiple of ρ_j with ρ_j ≤ ρ ≤ 1) of⟧ and the pointwise locator in C2. Conversion BL-C: ⟦BFT_A.md: [H]^∞_α ≤ C_C[H]_α + 2·8^α||H||_∞, C_C := 2^α(8·2^α/(2^α - 1) + 32·4^α).⟧; the reverse Osc_2(H; B) ≤ ρ^α[H]^∞_α. NSL55's depth-j norm is pointwise and carries the
  factor ⟦NSL55.md: ‖·‖^C ≤ ‖·‖ ≤ (1 + C_T)‖·‖^C (BFT_B §16 preamble), and⟧ (C_0′ := (1 + C_T)C_0). Which seminorm each norm
  uses is recorded in O10/O11.

### C10. Exponential weights and rate symbols — PINNED
- Weight w(z) := e^{m·d(z, X_0)}: ⟦LINEAR_PACKAGE.md: Weight w(z) := e^{m d(z, X_0)} (m ≥ 0, any coarse site X_0); ||v||_{∞,m} := sup_z w(z)|v^c(z)|.⟧ (canonical; d as in C2). BFT4W55 renames the rate μ (MAPPED):
  ⟦BFT4W55.md: **μ ≥ 0** = the exponential spatial weight rate (BFT34_55's "m"; renamed per Codex BFT34 R2)⟧, and uses the
  base-point form, comparable to COFM55's product form within 1 + 4μe^{4μ} (BFT4W55 §2.2; MAPPED up to that constant).
- **Rates that must not be identified** (each DIFFERENT OBJECT): the weight rate m (≤ m_Y for weighted linear estimates)
  vs BFT-3's locality rate m_0 (derived: μ/4 for x, μ/3 for E, BFT34_55) vs UIR55's jet rate m_0 (any 0 < m_0 < m/3, by
  CODEX_REVIEW_ASSEMBLY R3) vs SRC's CD rate m_c (⟦SRCCD55.md: CD decay rate, in units of 1/ℓ_ref (ROTDEF I4)⟧ — note the
  unit: physical, not coarse) vs LINEAR_PACKAGE's strip m_*, m_*′. Codex keeps them apart explicitly:
  ⟦CODEX_REVIEW_ASSEMBLY.md: UIR's jet radius m_0 versus BFT's decay weight m versus SRC's m_c⟧. m_Y's definition
  (⟦BFT34_55.md: **m_Y** := ln 2/(16L^c), L^c ≥ max(260, 6952C_j)⟧) is COFM55's.

---

## §2. The objects (one canonical name and definition each; aliases mapped)

### O1. The averaging maps: M̄_c, Q_l (= Q_root), Q_str, h_l — PINNED; two collisions
- **M̄_c** (nonlinear, canonical): ⟦PROOF.md: let M̄_c(U) := (d!L^d)^{-1}Σ_σΣ_{y∈B(X)}T^σ_y(U)⟧ — the mean of the order-paired
  S4′ contour transporters (C3); M̄^{(j)}_c is the same map for the level pair (j, j+1) (TOWER-VAR). MAPPED in every S26 file
  that writes M̄ (NSL55 §4.0, KFACTOR_OFF55 §1.1, BFT34_55 §1.3, SRCAN55 §2.1, FLOW55 §4.2).
- **Q_l = Q_root** (its linearisation, canonical "root map"): ⟦LINEAR_PACKAGE.md: the averaged link is Q_rootA(X, μ) := avg_{σ,y}∫_{T^σ_y}A⟧ with the exact identity ⟦LINEAR_PACKAGE.md: the exact identity **Q_root = Q_str - d∘h** holds⟧.
  Setting SC's Q, BFT_A's Q_l, KFACTOR_OFF55's Q_l, NSL55's Q, BFT4W55 §4's Q_l are this operator (MAPPED). Banked size:
  ‖Q^j‖ ≤ 𝔮₀L^j, 𝔮₀ = 11/3 (Theorem NQ-1; (T-UNIF) bullet).
- **Q_str — DIFFERENT OBJECT under one name (REVIEW55_NORMS r55n-F4, CONFIRMED there).** LINEAR_PACKAGE's
  ⟦LINEAR_PACKAGE.md: (Q_strA)(X, μ) := L^{-4}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ)⟧ (support 135 at L = 3, d = 4) versus NORMS's
  ⟦NORMS.md: Q_str B(c) := L^{−(d−1)}Σ_{paths}Σ_{b∈path}σ_bB_b over⟧ (support 81):
  ⟦REVIEW55_NORMS.md: ### r55n-F4 "Q_str is two different operators (NORMS §N1 vs LINEAR_PACKAGE l.71)" — CONFIRMED (exactly reproduced)⟧.
  Both have row sum L and transpose norm L^{1−d}, so NORMS's uses survive; the slice identity Q_root = Q_str − d∘h holds for
  LINEAR_PACKAGE's operator only. **Canonical: LINEAR_PACKAGE's Q_str.**
- **h_l — DIFFERENT OBJECT under one name.** The order-averaged slice functional
  ⟦BFT_A.md: h_l the slice functional of step l (Q_l = Q_{str,l} - d∘h_l)⟧ (canonical) versus BFT_B §27.1's fixed-order
  description ⟦BFT_B.md: (h_l(w)(X) = the average over y ∈ B(X) of the integral of w along the axial path a(c_X → y) in a fixed coordinate order)⟧;
  ⟦COFUN_CC.md: The "fixed coordinate order" description at BFT_B §27.1 l.3589 / §29.2 is of a⟧ different operator; no step of
  RT-cc/FT/RHT-cc depends on which (both are block-interior with |c| ≤ 1; COFUN_CC §1 and §7.2). A third, unrelated h is
  NA-FP's background slice functional h_U (O8). Q_ax (BFT_B §15.0, root-to-root straight map) is a fourth averaging map,
  root-covariant but not Q_root.

### O2. The soft-kernel tree exponent: φ, φ̂, k̃, d(M) — PINNED; the normalisation fixed
- **φ (canonical)** — the exponent of the normalised kernel with the SU(N) maximiser W_0 of Re tr(W^{−1}M):
  ⟦PROOF.md: φ := N^{-1}[Re tr(W_0^{-1}M) - Re tr(V^{-1}M)] satisfies⟧ (NA-alg (b)), φ ≥ 0, φ(W_0) = 0,
  φ = |ρ|²_HS/(2N) up to relative O(y² + |ρ|) (NA-alg (b)), ρ := log(V^{−1}W_0). Aliases, MAPPED (same function of (M, V)):
  E_NA's ⟦PROOF.md: φ_c := N^{-1}[max_{W∈SU(N)}Re tr(W^{-1}M̄_c) - Re tr(V_{i+1,c}^{-1}M̄_c)]⟧; HIST's φ_M
  (⟦HIST.md: Φ_i(U, V) := Σ_cφ_{M̄_c(U)}(V_c) (φ of (3.0); the kernel exponent with⟧); RLARGE's φ_M (C8).
- **φ̂ := Nφ** (the composite functional's normalisation): ⟦BFT_A.md: φ̂ = Nφ with φ of NA-alg (b)⟧, quadratic part
  ½|ρ|²_HS: ⟦PROOF.md: φ̂ = ½|ρ|² + O(ρ⁴) in the ledger's normalisation⟧ (TOWER-VAR (c)); the O(ρ⁴) form holds at M ∈ SU(N)
  (y = 0); in general the remainder is NA-alg (b)'s O(y²|ρ|² + |ρ|³). Argument order: TOWER-VAR writes φ̂_c(M; V), Setting
  N5-bg writes φ̂_c(V; M) — same function (MAPPED).
- **k̃ — DIFFERENT OBJECT (FLOW's exponent):** ⟦FLOW.md: k̃(V, M) := N^{-1}Re tr((1 - V^{-1}W)P) ≥ 0⟧ (M = WP polar, W ∈ U(N)).
  Exact relation ⟦HIST.md: (i) k̃(V, M) = φ_M(V) + d(M) for every V ∈ SU(N), with d(M) := N⁻¹(tr P - Re tr(W_0⁻¹M)) ≥ 0 independent of V;⟧,
  d ≡ 0 for N = 2 on S4′ means, d = O(y⁶) in the contour spreads (Lemma HF (ii)-(iii)). So **k̃ and φ have the same jets of
  order ≤ 5 at the trivial field and differ off it for N ≥ 3**; FLOW itself records that the exact tree exponent is κuφ
  (⟦FLOW.md: [RFL-fix §3.1, per HIST Lemma HF⟧). Banked consequence (FLOW55 bullet): the literal k̃ every-background setting
  is REFUTED for N ≥ 3 by an exact SU(3) S4′ witness (⟦CODEX_REVIEW_FLOW55.md: ### 1.2 Every-background normalization — REFUTED under the literal cited k̃ convention⟧);
  **canonical exponent: φ (or φ̂ in the composite normalisation).**

### O3. κ_j and the κ family — PINNED
- **κ_j (canonical)** := the coefficient of φ̂ for the level pair (j, j+1) in the composite functional, i.e. the soft-kernel
  stiffness RELATIVE to the Wilson density in the s/φ normalisation; κ_j ∈ [κ_−, κ_+], κ̂ := κ_+/κ_−. Sources (MAPPED):
  ⟦BFT_A.md: κ_j ∈ [κ_-, κ_+], depth k ≥ 1, coarse torus side T⟧; Setting SC
  ⟦LINEAR_PACKAGE.md: κ_- ≤ κ_i ≤ κ_+. (The normalisation 𝒩 cancels the shrinkage |M̄| < 1, so only the distance from the polar part is⟧;
  ⟦KFACTOR_OFF55.md: d = 4, L ≥ 3 odd, κ_l ∈ [κ_-, κ_+], κ̂ := κ_+/κ_-⟧; ⟦NORMS.md: κ_j ∈ [κ_-, κ_+], κ̂ := κ_+/κ_-.⟧;
  NSL55 Theorem ID's "κ_l ∈ [κ_−, κ_+]"; level-0 member ⟦PROOF.md: κ_0 ∈ [κ_-, κ_+], g = 1⟧ (Setting N5-bg).
- **κ (uniform), FLOW/HIST/RLARGE/UIR55 — MAPPED to κ_j ≡ κ.** The renormalised stripped tower has the same κ at every level:
  ⟦FLOW.md: The kernel coupling in the stripped tower is the same κ at every level.⟧;
  ⟦UIR55.md: κ = the uniform soft-kernel stiffness of FLOW's stripped tower (Def F-strip),⟧. Proof of the identification:
  the step-0 integrand is exp(−u_0[Σ_p s + κΣ_c φ]) up to the U-dependent kernel normaliser (C7, C8; SRCAN55 §2.1 "Step 0"),
  the renormalised stripped tower keeps the same ratio κ at every level (FLOW Def F-strip), and N[Σ_p s + κΣ_cφ] =
  S_W + κΣ_cφ̂, so the composite coefficient of φ̂ is the same κ (normalisation map NM1, O4). **The per-level variation κ_j ∈ [κ_−, κ_+] of the BFT/linear statements
  contains the uniform case; it is NOT the bare-normalised ratio κu_j/u_0 (which → 0 at coarse levels, FLOW Def F-strip's
  last paragraph).**
- **DIFFERENT NORMALISATION: E_NA's κ_i = N·κ_j (at g = 1).** ⟦PROOF.md: E_NA := S_W(U) + Σ_i(κ_i/g²)Σ_cφ_c⟧ uses φ (not φ̂)
  next to S_W = NΣs, so E_NA(g = 1) = 𝔉_k exactly when κ_i = Nκ_j:
  ⟦BFT_A.md: This is B-NA-red's E_NA (PROOF l.2309, at g = 1 and with the factor N⟧ (absorbed in κ_j). E_NA's display is not
  homogeneous in g (S_W carries no 1/g²); which g PROOF meant is NOT fixed (C6, last item).
- **DIFFERENT OBJECTS written κ_0 / κ_i / κ_j:** the level-0 kernel coefficient κ_0 (above; BR1 runs at
  ⟦PROOF.md: With 𝔠_∞^♯ ([SF7-edit 1]; κ_0 = 1; one class, CS-1)⟧ — this is NSL55 §5.3's "κ_0 the coupling at which BR1 is
  run") versus Theorem CE's ⟦PROOF.md: **κ_0 := 16a ≈ 151.3**⟧ (polymer entropy constant); fine-unit stiffnesses
  ⟦PROOF.md: κ_i = κL^{-2i}⟧ (2D linearised c20 model) and ⟦FLOW.md: κ_j := sL^{2j} (s > 0; f6's κ_1 = 9s at L = 3)⟧ (scalar
  proxy) — both are κ_j expressed in FINE units, not own units; SYMBOLS §6.5's bare-κ family (coupling-ratio bound, polymer
  decay ⟦PROOF.md: **κ > 3κ_0 + 3 ≈ 457**⟧, Balaban's large-field parameter, a group element, a Lie-algebra-valued function —
  ⟦CODEX_REVIEW_SYMBOLS.md: CONFIRMED: ≥5 roles⟧); HIST's polymer decay κ_p
  (⟦HIST.md: Σ_{X∋x}sup_{𝔇_α(X)}|E_k(X; U) - E_k(X; 1)|·e^{κ_pd(X)} ≤ E_0⟧); SRCCD55's cumulants κ_n(·|U_K)
  (⟦SRCCD55.md: conditional joint cumulant of order n⟧). Also κ̂ := κ_+/κ_− versus LINEAR_PACKAGE's
  ⟦LINEAR_PACKAGE.md: κ̂_SC := max_iκ_{k-1}/κ_i (Setting SC⟧ (κ̂_SC ≤ κ̂; either may be used where LINEAR_PACKAGE says so).
  SYMBOLS §6.5 lists three κ_0 values (151.3; 6.15·10⁻⁴; 1) and **misses this fourth κ_0** (the level-0 member of κ_j);
  I record it, no file needs renaming because every use is local to its section.

### O4. The composite functional 𝔉_k and the normalisation map — PINNED (this entry fixes the map ASSEMBLY55 F23 leaves open)
- **Canonical:** ⟦PROOF.md: **𝔉_k(U_0, …, U_{k-1}; V_k) := S_W(U_0) + Σ_{j=0}^{k-1}κ_jΣ_cφ̂_c(M̄^{(j)}_c(U_j); U_{j+1})**⟧
  (TOWER-VAR; U_k := V_k). Aliases, MAPPED: ⟦BFT_A.md: 𝔉_k(U_0, …, U_{k-1}; V_k) := S_W(U_0) + Σ_{j<k}κ_jΣ_cφ̂_c(M̄_c^{(j)}(U_j); U_{j+1}) (TOWER-VAR, PROOF l.6296),⟧;
  ⟦KFACTOR_OFF55.md: F(x) := 𝔉_k∘exp(x; B) (TOWER-VAR; BFT_A §1.1)⟧ (exponential coordinates U_j = e^{x_j}, V_k = e^{B});
  NSL55's 𝔉_j (depth j, same formula); SRCAN55's perturbed ⟦SRCAN55.md: **𝔉_k^{ε̂} := Σ_p(1 + ε̂_0(p))w(F_p) + Σ_{l<k}κ_lΣ_c(1 + ε̂_l(c))φ̂_c(M̄^{(l)}_c(U_l); U_{l+1}).**⟧
  (= 𝔉_k at ε̂ = 0; w(F_p) is the Wilson class function of the plaquette log, i.e. S_W = Σ_p w(F_p)).
- **Quadratic part:** Setting SC per component,
  ⟦LINEAR_PACKAGE.md: **E(B_0, …, B_{k-1}; B_k) = ½||dB_0||² + Σ_{i<k}(κ_i/2)||QB_i - B_{i+1}||²**⟧; with sources
  ⟦BFT_A.md: **E_src(x; B_k) := ½||dx_0||² + Σ_{l<k}(κ_l/2)||r_l(x)||² - Σ_{l<k}[⟨G_l, dx_l⟩ + ⟨j_l, x_l⟩ + ⟨s_l, r_l(x)⟩]**⟧. MAPPED.
- **Same object in a different normalisation: HIST's chain energy** ⟦HIST.md: E(chain) := Σ_ps(U_0(p)) + κΣ_{i<k}Φ_i(U_i, U_{i+1})⟧.
- **The normalisation map NM (derived here from the definitions; exact; no estimate):**
  - **NM1 (coefficients).** κ_j(𝔉_k) = κ(HIST, FLOW, RLARGE, UIR55) when κ_j ≡ κ; κ_j(𝔉_k) = κ_i(E_NA)/N at g = 1 (O3).
  - **NM2 (values).** Since S_W = NΣ_p s exactly and φ̂ = Nφ exactly, **𝔉_k ≡ N·E(chain)** on every configuration
    (κ_j ≡ κ). Hence the composite critical value E^cb_k is N times HIST's chain energy at the same critical chain, and
    min 𝔉_k = N·𝓔_k (O5). Critical points coincide.
  - **NM3 (coordinates and jets).** BFT/NSL coordinates are HS-orthonormal (C5); FLOW/HIST/UIR coordinates are the
    normalised Lie coordinates, y^a = √N·B^a. So the n-th Taylor tensor of a functional F written in y and the n-th Taylor
    tensor of F/N written in B satisfy D^n_y F = N^{1−n/2}·D^n_B(F/N): **quadratic forms coincide** (both are Setting SC per
    colour), cubic tensors differ by N^{−1/2}, quartic by N^{−1}. Every k-, T-uniform kernel bound transfers with an
    N-dependent constant and the same decay rate.
  - **NM4 (coupling).** The bare and the renormalised tree weights are exp(−u·E(chain)) = exp(−(u/N)·𝔉_k); "β factored out"
    (BFT34_55) means the factor u/N = 2/g_std² is stripped from 𝔉_k. FLOW's (J1) normalisation β[𝓔_k] = 1 is the same
    statement as β[E^cb_k] = 1 computed in HS coordinates (NM3, quadratic forms coincide).
  - **NM5 (exponent).** FLOW's stripped tower uses k̃, not φ; jets of order ≤ 5 at the trivial field agree (O2); away from
    it only φ is the exact tree exponent.
  NM is bookkeeping; it is exact algebra from the five definitions cited (S_W, s, φ̂ = Nφ, t_a normalisation, the kernel).
  It discharges the "normalisation map between 𝔉_k's κ_jφ̂ and the stripped φ-tower" that ASSEMBLY55 N16/F23 and
  CODEX_REVIEW_ASSEMBLY R6 leave as a condition, **as a dictionary statement**; it does not discharge (GERM) beyond
  CODEX_REVIEW_ASSEMBLY R6's finite-chain scope, (JET-∞), or (R).

### O5. The towers: E^br, E^cb, E^min, and FLOW's 𝒯_k (a fourth object) — PINNED
- **E^cb_j (composite critical value; canonical for every BFT statement):** ⟦NSL55.md: - **E^cb_j(w)** := 𝔉_j(exp Z_j(w); e^w); **E^cb_0** := S_W;⟧
  with Z_j(w) BFT-E's depth-j point on the FIXED domain ‖w‖_D ≤ ε_u, 𝒞_glob only; origin
  ⟦BFT_A.md: with E_j^{cb}(W) := 𝔉_j(Z_j(W); W) (the composite branch value)⟧. **Aliases written "E_k^br" that denote E^cb
  (MAPPED):** ⟦BFT34_55.md: **E_k^br(B) := 𝔉_k(x(B); B)** (Balaban's convention, BA-9;⟧;
  ⟦BFT4W55.md: - **E_k^br** := 𝔉_k(x(B); B), the **composite critical value** (Balaban's convention; BFT34_55 §1.1; Codex GV item 4).⟧;
  SRCCD55 §5.1's ⟦SRCCD55.md: - **BFT-4** (E_k^br = S_W + R_k, ‖R_k‖_𝒜 := Σ_{X∋0}sup|R_k(X)|e^{m_0|X|} ≤ C_0) is the source-free **classical** part of⟧;
  CODEX_REVIEW_GV item 4's "composite critical value"; BFT34_55's ⟦BFT34_55.md: - **R_k** := E_k^br − S_W(V_k) (REVIEW_S22 l.414)⟧.
- **E^br_j (PROOF's per-level branch): DIFFERENT OBJECT.** ⟦PROOF.md: (U_j critical for F_j(·, U_{j+1}) = E_j^br + κ_jφ̂ without⟧
  (TOWER-VAR (a)); level 1: ⟦PROOF.md: (iv) U(GV) = Ĝ·U(V) for every level-1 gauge G (Lemma U0 (iii)), so E_1^br(V) := F(U(V), V) is gauge invariant;⟧
  with U(V) unique in BR1's sup ball in BR1's slice (O8), on the CURVATURE-small class; levels ≥ 2 by NAH-ind with per-level
  shrinking radii. Bridges: E1 at level 1 on 𝒞_glob(ε_E1) (⟦NSL55.md: BR1's named not-computed inputs C_♭, C_Δ^{BR1}, r_♭ — only finiteness is used). Then **BR1's U(V) is gauge-equivalent under⟧,
  banked conditionally, CODEX_REVIEW_NSL item 4); E-ind on j-dependent balls only (⟦NSL55.md: **Proposition E-ind — PROVEN-HERE as a conditional implication.**⟧).
  **No uniform bridge** (Codex NSL: the most dangerous remaining identification).
- **E^min (global-minimum tower; s-normalised): DIFFERENT OBJECT.**
  ⟦HIST.md: **𝓔_0 := Σ_ps(U_p), 𝓔_{i+1}(V) := min_U[𝓔_i(U) + κΦ_i(U, V)]**⟧; level-1 instance in the composite normalisation
  ⟦PROOF.md: E_1^NA := min_UF = E_1^br on 𝔅_1(ε_br) iff (MIN_1) holds⟧; its local (cone-restricted) version read by SF/HIST
  ⟦HIST.md: **𝓔^♭_k(U) := inf_ψE^♭(ψ; U)**⟧ and the minimiser background ⟦PLD.md: fixes 𝔟(V) := the minimiser of E_k + the kernel term given V⟧.
  Normalisation: min 𝔉_k = N·𝓔_k (NM2). Bridge to E^cb: finite-chain germ only (CODEX_REVIEW_ASSEMBLY R6, banked
  conditional: ⟦CODEX_REVIEW_ASSEMBLY.md: ### R6 — What (GERM) can actually establish; what it cannot⟧); on uniform/local
  domains none ((MIN-cb), ⟦ASSEMBLY55.md: (i) **(MIN-cb)** [OPEN]⟧; PROOF's weaker restricted (MIN_1) option, R7).
- **𝒯_k (FLOW's k̃-min tower): a FOURTH object.** ⟦FLOW.md: **Def F-strip (the tree tower; uniform κ).** 𝒯_0(U) := Σ_ps(U_p); 𝒯_{k+1}(V) := min_U[𝒯_k(U) + κΣ_ck̃(V_c, M̄_c(U))]⟧.
  ⟦HIST.md: Termwise k̃ ≥ φ, so 𝒯_k ≥ 𝓔_k⟧ (equality for N = 2); same jets of order ≤ 5 at V = 1 (O2). ASSEMBLY55 §1.1 counts three
  towers (⟦ASSEMBLY55.md: ## 1.1 There are THREE objects, not two (symbols pinned by file and string; systemic defect 1)⟧) and
  treats 𝒯_k as E^min; that is correct for N = 2 and at the jet level, **not** as functions for N ≥ 3. Canonical E^min := 𝓔_k.
- **Per-level functionals.** F_j := E_j^br + κ_jΣφ̂ (PROOF; REVIEW_S22), F^cb_j := E^cb_j + κ_jΣφ̂ (NSL55 §4.0), BR1's
  F(·, V) = 𝔉_1(·; V) at level 0 (all three agree at j = 0), FLOW's one-step
  ⟦FLOW55.md: Apply Lemma ENV to FLOW §31's one-step problem F_k(U; V) = 𝒯_k(U) + κΣ_ck̃(V_c, M̄_c(U)) on the slice Σ_lin (TOW (2)): with⟧
  (k̃- and s-normalised). Which one a consumer reads is recorded in §4.

### O6. Critical points and backgrounds — PINNED
- **x*(B) / x(B)** (canonical): the unique slice critical point of 𝔉_k∘exp(·; B) in the K^{(σ)}/BFT-E ball, Γ = Γ_E or
  Γ^{(T)}: ⟦GV55.md: 𝔉_k∘exp(·; B) has **exactly one** critical point x* in 𝔅 := {x ∈ Ker Γ : ‖x‖_{(σ)} ≤ C_0s}; it is⟧.
  Z_j(w) (NSL55: "the depth-j point of Theorem BFT-E with datum w") and U^cb_j(v) (⟦NSL55.md: - **U^cb_j(v)** := (Z_{j+1}(v))_j, the level-j component of the depth-(j+1) point (j ≥ 0);⟧) are MAPPED.
- **DIFFERENT OBJECTS:** BR1's ⟦PROOF.md: (ii) **U(V) := e^{A*}U^(0)(V) is a critical point of F(·, V)**⟧ (level 1, BR1 slice,
  curvature-small class); the composite lift ⟦PROOF.md: (b) at the composite lift Z^lift := (U^{(0)}∘⋯∘U^{(k-1)}(V_k), …, U^{(k-1)}(V_k)) every soft fluctuation vanishes, every⟧
  (COMP's centre; excluded as a centre in every decaying norm by BA-2); (CovLift)'s ⟦BFT_B.md: - **(CovLift)** [the new input; named, not proven]: a map V ↦ Z^sm(V), given on every torus by one local formula, with⟧;
  the global minimiser 𝔟(V) (PLD, RLARGE (BG)_k; E^min's argmin); FLOW's ⟦FLOW.md: Φ_{j←n} denotes the tree background map⟧
  (𝒯-minimisers); SF's critical chain ψ^r of E^♭ (⟦SF.md: depth-uniform, such that at every real critical chain ψ^r of E^♭(·; U), U ∈ R_{3ε_1}(Λ_k), in a per-level covariant slice through⟧).
- **Centring.** "Trivial-chain centring" = displacements measured from the trivial chain on 𝒞_glob:
  ⟦BFT_A.md: - (C-glob) *global small gauge class* 𝒞_glob(ε): real V_k = e^{B_k} with ||B_k||_D := max_c|B_k(c)| ≤ ε in one global gauge⟧.

### O7. Composite gauges and the gauge-parameter spaces — PINNED; one live collision (Λ_0)
- **Ξ** (canonical): ⟦KFACTOR_OFF55.md: Ξλ := (dλ, d ev^{(1)}λ, …, d ev^{(k−1)}λ)⟧ (BFT_A §26.0, MAPPED); K_0 = −Ξ (C4).
- **Λ_0 — TWO OBJECTS UNDER ONE NAME.** BFT_A/KFACTOR_OFF55: ⟦BFT_A.md: Λ_0 := level-0 functions that are constant on the level-k roots⟧,
  with ⟦KFACTOR_OFF55.md: **Λ_* := functions vanishing on the level-k roots**⟧; GSHARP55 (with BFT_B §12.0's 𝒢_0 convention, λ vanishing at the level-k sites) and ALIGN55 write Λ_0 for
  the VANISHING space (BFT_B §31 itself uses BFT_A's Λ_0, ⟦BFT_B.md: Λ_0 := level-0 functions that are **constant on the level-k roots** (BFT_A §26.0)⟧): ⟦ALIGN55.md: Λ_0: level-0 su(N)-functions vanishing at the level-k roots.⟧,
  ⟦GSHARP55.md: 𝒢_0 = {Dλ : λ a level-0 function vanishing at the level-k roots}⟧. Pinned already by
  ⟦GV55.md: - **Λ_0 / Λ_***: KFACTOR_OFF55 and BFT_A §31 use Λ_0 = level-0 functions **constant** on level-k roots and Λ_* = those⟧.
  **Canonical: Λ_0 = constant on roots, Λ_* = vanishing (Λ_0/const ≅ Λ_*).** Harmless where only Ξ-images are used
  (Ξ(const) = 0); it matters for "ΓΞ = −1 on …" statements (O8).
- **𝒢^{(j)}, 𝒢^{rt}_j** (NSL55 §0, §4.0): depth-j composite gauges trivial at level j, and their level-j evaluations equal
  to 1 at the level-(j+1) roots. Codex: they are NOT the whole fixed-datum symmetry group (constant conjugations at v = 0):
  ⟦CODEX_REVIEW_NSL.md: ## F5 — new refutation: root-trivial gauges are not the entire fixed-datum symmetry group⟧.
- **(GI)** — the composite gauge invariance of 𝔉_k: ⟦BFT_A.md: - **(GI)** (named hypothesis, the defining property of TOWER-VAR, §1.1): 𝔉_k(U^g) = 𝔉_k(U) for every composite gauge g⟧;
  re-derived in NSL55 In-4 (S4′ covariance + uniqueness of W_0). Composite gauges: ⟦BFT_A.md: Composite gauges: g = (g_0, …, g_{k-1}), g_j a⟧
  level-j gauge with g_j(c_X) = g_{j+1}(X).
- **Three invariances that must not be identified** (CODEX_REVIEW_ASSEMBLY R11): composite-gauge invariance of 𝔉_k
  (above); constant-gauge invariance of BFT-4 (a)'s pieces (BFT4W55); local (independent-endpoint) gauge invariance that
  REVIEW_S22's BFT-4 asks of its polymers. ⟦CODEX_REVIEW_ASSEMBLY.md: ### R11 — Classical versus quantum and constant versus local gauge invariance are real distinctions⟧.

### O8. Gauge slices and the orbit norm — PINNED
- **S_E (canonical slice) = Ker Γ_E, Γ_E = Λ = Λ_E — one object, three names:**
  ⟦BFT_B.md: - Λ(x) := Σ_Xχ^5_Xλ^E_X(x) (each term extended by 0 off N_X); **Π_E x** := the composite gauge transform of x by λ_0 = Λ(x)⟧;
  ⟦BFT_A.md: - **Γ_E.** Γ_E(x) := Λ(x) = Σ_Xχ^5_Xλ^E_X(x) of BFT_B §15.0⟧; ⟦GV55.md: - **Γ_E** = **Λ** of BFT_B §15.0 = "Λ_E" of GSHARP55⟧
  (banked: CODEX_REVIEW_GV item 3). Coarse side T ≥ 5. For T ∈ {3, 4}: Γ^{(T)}
  (⟦BFT_A.md: - **Proposition SM (small tori by periodic lift).** For T ≤ 4 let T' := cT⟧) — MAPPED (same constants, Codex
  GSHARP §2.5, GV item 3). Depth-j versions Λ^{(j)}, S_E^{(j)} (⟦NSL55.md: - **Λ^{(j)}** = the depth-j slice functional⟧) —
  **NOT nested**: a depth-k slice point cut at depth j is not in S_E^{(j)} (banked exact witness, defect −640/19683); NSL
  moves it back (Theorem NSL).
- **Generic Γ (K^{(σ)}'s quantifier):** a linear Γ with ⟦KFACTOR_OFF55.md: Below always **ΓΞλ = −λ for λ ∈ Λ_*** (true for Γ_E,⟧;
  BFT_A's admissibility ⟦BFT_A.md: - **Gauge fixing.** A linear Γ on the chain space such that ΓΞ is a bijection from Λ_0/const onto Ran Γ, and⟧
  (MAPPED: Λ_0/const ≅ Λ_*). Γ_tent / S_tent (⟦BFT_A.md: - **Tent-axial slice (level 0).**⟧): admissible, delivers potentials
  (LR-pot) but not gradients — DIFFERENT OBJECT from S_E for field components.
- **DIFFERENT OBJECTS (per-level slices):** BR1's ⟦PROOF.md: (i) there is a unique A* = A*(V) in {A ∈ ker h_{U^(0)} : ||A||_∞ ≤ r(ε)}⟧
  (axial-type, level 1); NA-FP's background slice ⟦PROOF.md: Π_U := 1 - h_U^T(h_Uh_U^T)^{-1}h_U⟧ (Setting N5-bg; N5's
  covariance); B-NA-red's ⟦PROOF.md: the slice is the per-level covariant slice (h^{(i)}_U = 0 at each⟧ level) and SF's
  (a5-G♯) "per-level covariant slice through ψ^r" (O6 locator); FLOW's Σ_lin (O5 locator); REVIEW_S22's composite slice
  ⟦REVIEW_S22.md: S_k a composite slice at the composite lift Z^lift(V_k).⟧ (centred at Z^lift, unspecified); ALIGN55's
  hierarchical Coulomb-detail gauge ⟦ALIGN55.md: Λ_HCx := λ_0.⟧ (a left inverse with Λ_HCΞ_1 = −1 on ALIGN55's Λ_0 = Λ_*).
- **Orbit norm (canonical gauge-free form):** ⟦GSHARP55.md: ||[x]||_𝔐 := inf_{g∈𝒢_0}||x + g||_𝔐.⟧, equivalent to S_E:
  ⟦GSHARP55.md: ||[x]||_𝔐 ≤ ||Π_Ex||_𝔐 ≤ C_Π||[x]||_𝔐.⟧. Field components are slice-dependent (banked GF-DEP:
  ⟦GSHARP55.md: **Proposition GF-DEP (PROVEN-HERE; exact linear algebra).**⟧, CODEX_REVIEW_GSHARP item 4); ‖x‖_inv and N_res are
  slice-free. ALIGN55's ⟦ALIGN55.md: **[x]_{1,♯}** := inf_{λ∈Λ_0}|||x + Ξ_1λ|||_{1,♯}.⟧ is the same orbit infimum plus
  slice-free residual terms (MAPPED).
- **Feynman vs hard slice.** The Feynman response 𝓛_Γ^{−1}S and the hard-slice response have the same gauge-invariant
  outputs (⟦BFT_A.md: (b) For every source S, the Feynman response 𝓛_E^{-1}S and the hard-slice⟧ response); for cc sources
  they are the same vector (GV55 §1.1, Codex GV item 3). For non-cc sources they differ by Proposition NCR's pairing.

### O9. Source classes: cc, (CC-0), level-wise co-closed — PINNED
- **cc (canonical)** ⟺ D^⊥(S) = 0 ⟺ Ξ^TS = 0 on Λ_0 (constants on roots) ⟺ D(S) supported on level-k roots with total 0:
  ⟦KFACTOR_OFF55.md: **composite-co-closed (cc)** iff D^⊥(S) = 0 (the total ΣD(S) = 0 is automatic); (CC-0) := D(S) = 0 everywhere is⟧;
  ⟦BFT_A.md: composite-co-closed** iff Ξ^TS = 0.⟧; ⟦BFT_B.md: composite co-closedness is D(S) ⟂ Λ_0, i.e. D(S) supported on the level-k roots with total 0.⟧ — MAPPED (equivalent).
- **(CC-0)** = D(S) = 0 everywhere (strictly smaller; refuted at critical points, banked). **Level-wise co-closed** (each
  d*j_l = 0; LIN0's class, BL-7's pair) ⊂ (CC-0) ⊂ cc. Setting LIN^cc = Setting LIN with level-wise co-closedness replaced
  by cc (BFT_B §27.1).

### O10. Field norms — PINNED (four distinct "𝔐"s)
- **𝔐^∇** (BFT_A, σ = 0, residual weight L^{k−1−j}): ⟦BFT_A.md: - **𝔐^∇ (displacements):** ||x||_𝔐 := max_{0≤j<k}[ ||x^c_j||_{∞,m} + ||∇^cx^c_j||_{∞,m} + [∇^cx^c_j]_{α,m} + L^{k-1-j}||r^c_j||_{∞,m} ].⟧
- **𝔐^{(σ)}** (canonical for K^{(σ)}/BFT-E; residual weight L^{(1+σ)(k−1−j)}, θ_w^r = 2 + σ in own units; Campanato):
  ⟦KFACTOR_OFF55.md: - **𝔐^{(σ)}:** ||x||_{(σ)} := max_{0≤j<k}[ ||x^c_j||_∞ + ||∇^cx^c_j||_∞ + [∇^cx^c_j]_α + L^{(1+σ)(k−1−j)}||r^c_j||_∞ ].⟧
  σ = 1 is "𝔐^♯". NSL55's ‖·‖_{(σ),j} is 𝔐^{(σ)} at depth j with the POINTWISE seminorm (C9 factor 1 + C_T).
- **DIFFERENT OBJECTS called "the 𝔐-pair":** ⟦GSHARP55.md: - **"𝔐-pair"** names three different norm pairs:⟧ — RTARGET §33's
  (Y; X_c) (no full gradient), REVIEW_S22's 𝔐 (⟦GSHARP55.md: (P2) REVIEW_S22's 𝔐, which is described but not defined (REVIEW_S22 l.392-399);⟧),
  lane A's (𝔐^∇, 𝒴^∇). ‖x‖_{X_c} + [f_0]_α ≤ 3‖x‖_{𝔐^∇} (GSHARP55 §1).
- **Gauge-invariant norm:** ⟦BFT_A.md: Gauge-invariant configuration norm: **||x||_inv := max_{0≤j<k}[ ||f_j||_∞ + [f_j]_α + L^{k-1-j}||r^c_j||_∞ ]**⟧;
  σ-version ‖x‖_{inv,(σ)} (KFACTOR_OFF55 §1.2). N_res: ⟦BFT_B.md: - **Residual-gradient size.** N_res(x) := Σ_{0≤i≤k-2}||r_i(x)||_{C^{1,α}}⟧.
- **Gauge-function norm** ‖ξ‖_♮ (NSL55: C^{2,α} plus sup, level 0, depth-j coarse units):
  ⟦NSL55.md: - **‖ξ‖_♮** := ‖ξ‖_∞ + ‖∇^cξ‖_∞ + ‖∇^c∇^cξ‖_∞ + [∇^c∇^cξ]^∞_α⟧ — unrelated to FLOW55/UIR55's ♮ (H^♮, (UIR^♮)) and
  HINT2_55's (ID♮) (DIFFERENT OBJECTS sharing the glyph).
- **Weighted versions:** ‖·‖_{(σ),μ,f} (BFT4W55 §2.2, base-point form) and COFM55's product form (C10).

### O11. Source norms — PINNED (three unweighted N's; GV55's pin, re-read and extended)
- **N(S)** (Pc form) ⟦COFUN_CC.md: **N(S)** := ‖G^c_0‖_∞ + [G^c_0]_α + ‖j^c_0‖_∞ + ‖j‖_Pc + ‖G‖_Y + ‖s‖_R (= (CO-fun)'s right side⟧;
  **N_Σ(S)** (level-summed plain slot) ⟦GV55.md: - **N_Σ(S)** := ‖G^c_0‖_∞ + [G^c_0]_α + **|j|_Σ** + ‖G‖_Y + ‖s‖_R⟧ — Codex C2's
  "N" in (C2-COF) is N_Σ (⟦CODEX_REVIEW_C2.md: N := ||G_0^c||_∞+[G_0^c]_α+||G||_Y+||s||_R+J⟧, MAPPED); **N^{(σ)}(S)** (K^{(σ)}'s,
  (R(σ)) slot, no G above level 0) ⟦KFACTOR_OFF55.md: **N^{(σ)}(S) := ||G^c_0||_∞ + [G^c_0]_α + ||s||_{R(σ)} + J(j),⟧.
  **Comparisons (banked, Codex GV items 1-2):** N(S)/N^{(σ)}(S) can be L^{θ(k−1)} (exact witness), and
  N_Σ ≤ max(2, L^{θ₀})N^{(σ)} ≤ L·N^{(σ)} (θ₀ ≤ σ, no G above level 0). So **N(S)-bounds do not feed K^{(σ)}; N_Σ-bounds do.**
- **Weighted:** COFM55's ⟦COFM55.md: **N_m(S) := ||G_0||^L_m + ||j^c_0||_{∞,m} + ||j||_{Pc,m} + ||G||^{sup}_{Y,m} + ||s||_{R,m}**⟧
  (pointwise Hölder on G_0, no Hölder norm on G_l, l ≥ 1; at m = 0 it is ≤ C·N(S) with C from BL-C, so an N_0-bound implies an
  N-bound up to that constant), N_{Σ,m};
  BFT4W55's N^{(σ)}_{μ,f} (pointwise Hölder on G_0, base-point weights); Codex TOPCC's Ñ_Σ (weaker than N_Σ).
- **Slots.** ⟦BFT_A.md: - **(R)** ||s||_R := max_{0≤l<k}ω^R_lL^{k-1-l}||s^c_l||_∞ with **ω^R_l := L^{θ(k-l)} for every 0 ≤ l < k**⟧;
  ⟦BFT_A.md: - **(G)** ||G||_Y := max_lω_l(||G^c_l||_∞ + [G^c_l]_α), ω_0 := 1, ω_l := L^{θ(k-l)};⟧; (R(σ)) := max_l
  L^{(1+σ)(k−1−l)}‖s^c_l‖ with ‖s‖_R ≤ L^θ‖s‖_{R(σ)} for θ ≤ σ.
- **The glyph N** also denotes the colour number (SU(N)), K^{(σ)}'s data map ("H, N: Hessian and data map at x = 0",
  KFACTOR_OFF55 §1.1), NORMS's row-sum norm N_0 and the trilinear norm N3. ALIGN55's N_1, N_Z are infima of N(S) over slot
  representations (flat / covariant).

### O12. Weights and exponents — PINNED
- **θ_w is three objects** (BFT-1 weight pair, [S24-fix 3]): curvature θ_w^c, residual θ_w^r, potential θ_A; delivered
  ⟦KFACTOR_OFF55.md: Lip ≤ ½; its fixed point is the unique critical point of 𝔉_k∘exp in 𝔅; BFT-1 holds with (θ_w^c, θ_w^r, θ_A) = (2, 2 + σ, 1)⟧.
  REVIEW_S22's single ⟦REVIEW_S22.md: - level-j curvature and soft-fluctuation components are weighted by L^{θ_w(k-j)};⟧ is
  the superseded one-parameter version (SYMBOLS §6.3: OWNER-GATED split).
- **θ (class exponent, ω_l = L^{θ(k−l)})** — never θ_w: ⟦GV55.md: - **θ** = the class exponent (ω_l = L^{θ(k−l)}) of N(S), ‖s‖_R, LIN0, CC-INV, RHT-cc; never θ_w.⟧
  (COFUN_CC's θ_c is this θ). **θ₀** := the exponent fed to imported lane-A estimates when σ = 1:
  ⟦CODEX_REVIEW_KOFF.md: use any `θ₀` with `α<θ₀<1`, for example `(α+1)/2`, in those imported⟧ (α < θ₀ ≤ σ, θ₀ < 1).
  **σ** ∈ (0, 1] (KFACTOR_OFF55's residual parameter; θ_R = σ). **α** = Hölder exponent; lane A fixed (α, θ) = (¼, ½) in
  ⟦BFT_A.md: Setting LIN of §7.1, d = 4, L ≥ 3 odd, **α := ¼, θ := ½** (inside 0 < α ≤ θ ≤ 1 - α).⟧ — banked items use the
  windows 0 < α < θ < 1 (C2-COF/TOP-cc/CC-INV) and 0 < α < θ ≤ σ ≤ 1 (K^{(σ)}, BFT-E).

### O13. Data classes and domains — PINNED
- **𝒞_glob(ε)** (canonical for every banked BFT item): O6 locator; ‖B_k‖_D := max_c|B_k(c)| in one global gauge.
  Complex: ⟦BFT34_55.md: 𝒫_ε := {B ∈ (su(N)⊗ℂ)^{links} : max_c|B_c| ≤ ε} is a genuine polydisc in link coordinates (used for Cauchy below).⟧
  (PD-glob). NSL's holomorphy is in the complexified SCALED norm only (CODEX_REVIEW_NSL item 2).
- **Curvature-small class (REVIEW_S22's BFT target): DIFFERENT, strictly larger.**
  ⟦REVIEW_S22.md: level-k field V_k = e^zV_k^r with V_k^r real, max_P|log V^r_{k,P}| ≤ ε ≤ ε_0 and⟧ |z|_∞ ≤ r_ℂε, every torus
  with level-k side ≥ T_0 and every non-wrapping box; BFT-2's polydisc "in curvature-adapted coordinates" (REVIEW_S22
  BFT-4). ⟦BFT34_55.md: components. It is **not** BFT-3 on BFT's full class (curvature-small V on every torus, non-wrapping boxes): 𝒞_glob is a strict⟧ subclass.
- **Op-norm small-field sets (DIFFERENT):** SRCCD55's 𝒮_K (C5; it borrows "BFT's ε_0" for an op-norm CURVATURE bound, while
  K^{(σ)}'s ε_0 bounds ‖B_k‖_D, a link-POTENTIAL sup in one global gauge — §5 FL7); RLARGE's χ_Q (cube interiors, ε_1);
  HIST/SF's R_{2ε_1}(Λ_k), R_{3ε_1}(Λ_k) and 𝔇_α(X) (local, normalised Lie coordinates).
- **Background:** Z = 1 (trivial) for every banked linear item except BGT55's Theorem GA, GA-slice, GA-PG, KER_Z/SF_Z and ALIGN55's
  RED′/R2-glob♯ (Z ≠ 1; conditional or algebraic). Corollary RW♯ is at Z = 1.
  **Weight:** m = 0 except COFM55 (0 ≤ m ≤ m_Y), GV-E_m, BFT34/BFT4W (fixed μ > 0, conditional). **Torus:** coarse side T;
  T ≥ 3 (K^{(σ)}, BFT-E, ID), T ≥ 5 for S_E itself, T ≥ 1 for GF-E/TOP-cc/CC-INV, T_0 (BR1), T ≥ 17 / ≥ 86 (BFT_B frames).

### O14. The coefficient-field norm ‖·‖_cf — PINNED (one collision inside the definition)
- **Canonical (as banked):** the sup of every soft-term coefficient plus the sup and pointwise Hölder seminorm (level-k
  coarse units, separations one fine step to one coarse unit) of the WILSON coefficient only — "the sup-plus-Wilson-Hölder
  coefficient class": ⟦CODEX_REVIEW_SRCAN.md: in the sup-plus-Wilson-Hölder coefficient class on 𝒞_glob⟧ (item 4). SRCAN55's
  printed definition ⟦SRCAN55.md: | ‖ε̂‖_cf | max_l‖ε̂_l‖_∞ + [ε̂_0]^∞_α (pointwise Hölder seminorm in level-k coarse units, separations from one fine step to one coarse unit, Codex KOFF §4.3's convention) | ‖·‖_♮ (FLOW55, GV55) | new name "cf" |⟧
  writes ε̂_0 for BOTH the Wilson coefficient on level-0 plaquettes and the l = 0 soft coefficient:
  ⟦CODEX_REVIEW_SRCAN.md: | ε_W vs ε_{S,l} | SRCAN55:113, 150–153 | Wilson plaquettes vs soft level-(l+1) links; the target uses ε̂₀ for both when l=0 |⟧.
  **Restatement:** ‖ε‖_cf := ‖ε_W‖_∞ + [ε_W]^∞_α + max_{0≤l<k}‖ε_{S,l}‖_∞.
- **DIFFERENT CLASS — the sup-norm ball consumed by SRCCD55:**
  ⟦SRCCD55.md: RLF and (F_R) must therefore hold uniformly over a sup-norm ball of coefficient fields. This is the same "slowly varying⟧;
  SRCAN55 itself: ⟦SRCAN55.md: A sup-norm ball is too large for BFT-1's Hölder clause (Lemma SA-J: exact flux identity; size comparison ARGUED).⟧ (§5 FL8).

### O15. Thresholds and radii — PINNED (the ones banked items are stated with)
- **ε_0 (K^{(σ)} / BFT-E):** a threshold on s = ‖B_k‖_D: ⟦KFACTOR_OFF55.md: *Conclusion.* There are ε_0 > 0 and C_0 < ∞ depending only on (N, L, κ_±, α, θ, σ) and the named constants — **not on k⟧,
  in Codex KOFF §5.3's bookkeeping (C_0 = max(2, 4G), ε_0 below four explicit minima). NSL55's r_u, ε_u, ε_ID, ε_lev, ε_tow,
  r_B, ρ_lev are built from it (⟦NSL55.md: Put **r_u := min(η_*, 1/(8GK), 1/(2C_cc))** and **ε_u := min(ε_0, 1/(4GK), r_u/C_0, r_ℂε_0/2)**.⟧);
  NSL55 warns its ε_u is not the lane's ε_u of TUNIF/NORMS (DIFFERENT OBJECT). E1's radius ε_E1 contains BR1's ε_br and
  𝔠_∞ (finite, not evaluated).
- **DIFFERENT OBJECTS named ε_0:** SRCCD55's "BFT's ε_0 at level K" (op-norm curvature; C5), REVIEW_S22's ε_0 (curvature
  class), BALX's CMP 109 background radius (⟦CODEX_REVIEW_BALX.md: ### F2 — Fixed geometric domains and coupling-dependent integration cuts have been conflated⟧).
  The cut ε_1 is SYMBOLS' six-object family; on the live RLARGE route the cut is the op-norm χ_Q of C5.
- **Fixed regularity radii vs coupling-dependent cuts** (BALX F2, banked as a source distinction): every radius in the banked
  K^{(σ)}/BFT-E/NSL/ID/BFT-3/BFT-4 (a) items (ε_0, r_u, ε_u, r_ℂ, η_*, ε_ID, ε_lev) is FIXED (k-, T-, g-independent); none of them
  uses a coupling-dependent cut p(g_k).

### O16. Observable-side objects used by banked items — PINNED (only what the bullets name)
- **Clover energy density e_a and its smearing** O_a(f) := Σ_x a⁴f(x)e_a(x) (SRCCD55 Lemma V setting, ROTDEF §2.2):
  ⟦SRCCD55.md: O_a(f) = Σ_x a⁴f(x)e_a(x) as in ROTDEF §2.2⟧; Lemma V's Step 0 writes it as Σ_p h(p)s(U_p) — the canonical s
  (C7) and the canonical u_0 = 1/g_0² (C6).
- **Flowed density** ⟦HINT55.md: - E(t,x) = −½tr(G_μνG_μν)(t,x) = ¼G^a_μνG^a_μν (tr T^aT^b = −½δ^{ab}); 𝓔(t,x) := t²E(t,x); f_ω(t) := ω(𝓔(t,0)).⟧
  (continuum) and its lattice version on the BARE links with S_geo (no β): ⟦HINT55.md: ¼G^aG^a on smooth fields [m: Lüscher's construction]. 𝓔(t,x) := t²E_lat(t,x). Properties used: gauge invariant,⟧
  — physical units (C2), standard g in the free coefficient (C6).
- **The R glyph** (CODEX_REVIEW_SRCAN item 13): R_F (flow error constant), R_tor (torus side), R_walk (random-walk box):
  ⟦CODEX_REVIEW_SRCAN.md: Thus the target's “every collision checked” table misses an R collision.⟧ Every flow formula reads R_F.

---

## §3. The lane-A linear inputs — the hidden premise set (target D2)

**Where the phrase comes from.** Four banked results are stated "relative to / conditional on the named lane-A linear
inputs": Theorem K^{(σ)} (⟦CODEX_REVIEW_KOFF.md: K^(σ) of §5.3: relative to the named lane-A linear inputs, one Γ⟧), Proposition
GV-E and Theorem BFT-E (CODEX_REVIEW_GV items 2, 4: "as a named-input implication"), and NSL / Theorem ID
(⟦CODEX_REVIEW_NSL.md: 2. **CONDITIONAL:** NSL's real existence, small-gauge uniqueness, bound C_N=4+3C_Lambda, and Faddeev–Popov inverse, uniformly in k,T,j (and sigma), from the expressly retained uniform elliptic/linear inputs.⟧).
No file lists the set in one place. GV55 §3.2 row 5 lists names only (⟦GV55.md: | 5 | Lane-A linear package (C2-COF), LIN0, W0, GU, FP, BL-4, Prop W, LES-div, LR-pot, Lemma Λ, Q-hold; BA-3, BA-6/F6, CR-1, Corollary WR (a) (named hypothesis) | BFT_A, BFT_B | banked/CONFIRMED at lane level and in the cited Codex reviews, **conditional on their own named inputs** (not re-audited here) |⟧),
and ASSEMBLY55 N24 classifies the whole package "inherited, NOT-VERIFIED at the S26 two-family standard". Below is the
exact set, assembled from the inputs each producer actually invokes (CODEX_REVIEW_KOFF §5.1's list; KFACTOR_OFF55 §4.1-§4.5;
GV55 §1.3 proof steps 1-6 and §3.2; NSL55 §3.0-§3.1; CODEX_REVIEW_C2 §4's dependency sentence; COFUN_CC §6.3), closed
under "input of an input" one level down (the inputs of (C2-COF), TOP-cc, CC-INV and EP-rec, because those four are
themselves inputs).

**Status classes (fixed before classifying).** **B** = banked cross-family: itself listed in PROOF [S26-BANKED] with a Codex
scope. **R2** = re-derived (not merely cited) in a Codex review on disk, and/or in an Opus 5.5 file, but not itself banked.
**R1** = re-derived only in a pre-S24 lane review (model not recorded) — LINEAR_PACKAGE's header review list counts as R1.
**S** = only stated: cited or named as a premise; no on-disk re-derivation located. "Used by": K = Theorem K^{(σ)}; G = GV-E;
E = Theorem BFT-E (BFT-1/2); N = NSL and Theorem ID.

| # | Input (file + locating string) | What it says (as read; not restated beyond its role) | Used by | Class | Evidence (located) |
|---|---|---|---|---|---|
| LA1 | (C2-COF), ⟦CODEX_REVIEW_C2.md: 1. **CONFIRMED — conditional whole-class CO-fun.**⟧ | sup + Hölder bound of f_0 for cc sources in N_Σ, top-response term kept | K (LIN^{(σ)} (2)) | **B** | (CO-fun) bullet; itself conditional on COF's inputs (LA10, LA16, LA20, LA21, LA27-LA34, LA36) and LP Thm 4.2(ii) (LA40) |
| LA2 | Lemma CD (root-pinned) + (GI), ⟦BFT_A.md: - **Lemma CD (exact composite-divergence identity), given (GI).**⟧ | Ξ^T𝔑^0 = −K′^T_x∇(𝔉_k∘exp); cc of the full remainder at critical points | K (CCP (b), (d)) | **B** | (CC-0) bullet ("Lemma CD holds only on root-pinned directions"); Codex KOFF §1 re-derives |
| LA3 | Lemma TOP-cc, CC-FUN (a)-(c), Theorem CC-INV in N(S) and N_Σ form, ⟦CODEX_REVIEW_TOPCC.md: 3. **CONFIRMED — source-only linear estimates, as implications.**⟧ | invariant half and top residual of a cc response bounded by N(S) / N_Σ(S) | G (step 3) | **B** | "Gauge-invariant half of BFT-5 clause (b)" bullet; N_Σ form only in Codex TOPCC item 3, not printed in the PROOF bullet (§5 FL6) |
| LA4 | EP-alg, EP-int, EP-bd, EP-opt, EP-rec, ⟦BFT_B.md: - **Theorem EP-rec (elliptic reconstruction).** For every configuration x (data x_k arbitrary; x_k := 0 for displacements):⟧ | S_E projection algebra; C^{2,α} interior bound of λ^E_X; ‖Π_Ev‖ ≤ C_Π‖v‖; slice optimality; reconstruction from gauge-invariant data | G (steps 1-2), N (Lemma A) | **B** | GF-E bullet ("EP-rec/EP-opt reconstruction"); ⟦CODEX_REVIEW_GSHARP.md: 1. **CONFIRMED — flat unweighted reconstruction and slice identification.**⟧ (independent reconstruction); lane R1 (REVIEW_BFT_B_S5 B.1-B.6) |
| LA5 | GF-E′ data half, ⟦CODEX_REVIEW_GSHARP.md: 3. **CONFIRMED — GF-E′ on S_E.**⟧ | data response in S_E bounded by ‖B_k‖_D | G (step 5) | **B** | GF-E bullet |
| LA6 | Proposition SM (descended slices T = 3, 4), ⟦BFT_A.md: - **Proposition SM (small tori by periodic lift).** For T ≤ 4 let T' := cT⟧ | S_E^{(T)} with the same constants | G, E, N | **B** | GV-E bullet ("slice identities"; Codex GV item 3); Codex GSHARP §2.5 |
| LA7 | Theorem RHT-cc (J-form as displayed), ⟦BFT_B.md: - **Theorem RHT-cc ((Res-Hölder) for composite-co-closed sources, m = 0).**⟧ | N_res of a cc response, plain currents summed (J-form) | G (step 4) | **R2** | lane R1 ⟦REVIEW_BFT_B_S9_S10.md: ## S9-7 Theorem RHT-cc and K_f: **CONFIRMED**⟧; summation re-derived in Codex GSHARP §3.1 and Codex GV §2 |
| LA8 | Lemma RT-cc (c), ⟦BFT_B.md: - **Lemma RT-cc (residual transport for composite-co-closed sources).**⟧ | exact residual transport with funnel-modified currents ĵ_l | K (LIN^{(σ)} (1)), LA7 | **R2** | Codex TR §2 re-derives (c) (⟦CODEX_REVIEW_TR.md: ## 2. RT-cc, TC and FT really give the extra power⟧); REVIEW55_BFTB; banked only inside Lemma TR's scope |
| LA9 | Lemma TC, ⟦BFT_B.md: - **Lemma TC (transported sizes; m := k - 1 - i ≥ 1).**⟧ | transposed straight averages cost L^{−2m} in coarse units (m = depth) | K, LA7 | **R2** | Codex TR §2 ("**CONFIRMED**, without SPD or W2") |
| LA10 | Lemma FT, ⟦BFT_B.md: - **Lemma FT (funnel transpose: size, support, weight).**⟧ | ‖h_l^T‖_{∞→∞} ≤ 1; Σπ_l(ĵ_l) ≤ C_fJ, C_f = 1 + 2d/(1 − L^{−3}) | K, LA7, LA1 | **R2** | Codex TR §2 (FT (ii)); lane R1 ⟦REVIEW_BFT_B_S9_S10.md: ## S9-6 Lemma FT (ii)-(iv): **CONFIRMED**⟧ |
| LA11 | Lemma TS, ⟦BFT_A.md: - **Lemma TS (top source).** If s = s_{k-1} only (residual type at step k - 1), the set of minimisers of E_src(·; B_k) equals⟧ | a top residual source is a data shift δ_b/κ_{k−1} | K (TOP♯), LA3 | **R1** (+ used inside a Codex derivation) | ⟦REVIEW_BFT_A_S3.md: - **Step 3 (TS, W, Λ, LR-pot, FP): CONFIRMED**⟧; Codex KOFF §5.1 uses it in its re-derivation of TOP♯ |
| LA12 | Corollary FP, ⟦BFT_A.md: - **Corollary FP (potential half of (G♯_0-field^∇)_m).** For data and residual-type sources, the minimiser in S_tent obeys⟧ | potentials of the tent-slice data response, weighted | K (TOP♯), LA3 | **R1** | REVIEW_BFT_A_S3 Step 3; Codex KOFF §5.1 names it ("FP bounds the tent representative's potentials"), does not re-derive |
| LA13 | Proposition W, ⟦BFT_A.md: - **Proposition W (weighted data map, gauge-invariant half).**⟧ | weighted BL-4 (0 ≤ m < m′ < m_*′) | LA3, LA1 | **R1** | REVIEW_BFT_A_S3 Step 3; Codex COFM item 4 ("Proposition W as weighted BL-4") — CONFIRMED there as an input |
| LA14 | Lemma Λ, ⟦BFT_A.md: - **Lemma Λ (root-to-root holonomy).**⟧ | root-to-root line integral vs Q^{(0→k)}x_0, C_Λ = 10 | LA4 (EP-rec) | **R1** | REVIEW_BFT_A_S3 Step 3 (C_Λ = 10) |
| LA15 | Lemma LR-pot, ⟦BFT_A.md: - **Lemma LR-pot (potential reconstruction in the tent-axial slice).**⟧ | potentials in S_tent from f_0, B_k, residual sums (C_1 = 775, C_2 = 40, C_3 = 205) | LA4 (EP-rec), K (Γ_tent potentials only) | **R1** | REVIEW_BFT_A_S3 Step 3 |
| LA16 | Corollary LIN0, ⟦BFT_A.md: - **Corollary LIN0 (gauge-invariant (H-lin^∇) on the pair of BL-7, m = 0, trivial background).** For 0 < α < θ < 1 and⟧ | ‖x‖_inv bound for LEVEL-WISE co-closed sources | K (TOP♯'s G,s part), LA1, LA3 | **R1** | ⟦REVIEW_BFT_A_S6.md: scope** (BL-7's pair, level-wise co-closed sources, m = 0, trivial background, 0 < α < θ < 1).⟧ |
| LA17 | Theorem CO-upR + Lemma RH, ⟦BFT_A.md: - **Theorem CO-upR ((CO-up) for rough currents).** For 1 ≤ j < k:⟧ | upper-level curvature from f_0 plus residual sums | K (LIN^{(σ)} (3)) | **R1** | ⟦REVIEW_BFT_A_S5.md: - **CO-0R, RH, CO-upR, CO-B: CONFIRMED** (CO-upR with a Campanato-vs-pointwise remark, fix U5).⟧ |
| LA18 | Proposition BL-4, ⟦BFT_A.md: **Proposition BL-4 (data: the gauge-invariant components).**⟧ | data response's invariant outputs ≤ G_D‖B_k‖_D | K (data), LA3, LA5 | **R1** | ⟦REVIEW_BFT_A_S2.md: (N2-lin, J-str, LES), with one constant to fix (the LES box convention). **BL-5 (a): CONFIRMED** for gauge-invariant⟧ (BL-4 "CONFIRMED given the package") |
| LA19 | Lemma BL-2 (b), (d), ⟦BFT_A.md: **Lemma BL-2 (coarse-unit sizes of the chain maps).**⟧ | Q = Q_str − d∘h sizes; 𝒜^{(0→j)} a probability average | K, LA4 | **R1** | REVIEW_BFT_A_S2 ("BL-2, BL-3, BL-C: CONFIRMED") |
| LA20 | Lemma BL-C, ⟦BFT_A.md: **Lemma BL-C (lattice Campanato ⇒ pointwise Hölder).**⟧ | Campanato ⇒ pointwise Hölder | LA4, LA1, C9 | **R1** | REVIEW_BFT_A_S2 Part 6 |
| LA21 | Theorem BL-5 (a), ⟦BFT_A.md: **Theorem BL-5 (the linear estimate at the trivial background for data and residual-type sources).**⟧ | invariant outputs for data + residual sources, 0 < α ≤ θ | LA1, LA3 | **R1** | REVIEW_BFT_A_S2 ("BL-5 (a): CONFIRMED") |
| LA22 | Lemma FG (ii)-(iii), ⟦BFT_A.md: - **Lemma FG (gauge-fixed responses).**⟧ | for cc S the Γ-response's invariant outputs are Γ-free; 𝓛_Γ^{−1} maps cc sources into Ker Γ | K (CL-0), G (§1.1) | **R2** | REVIEW_BFT_A_S6 ("Lemma FG … CONFIRMED"); Codex KOFF §1 re-derives (iii) "using only surjectivity of ΓΞ" (GV55 §1.1) |
| LA23 | Corollary WR (a) with its named hypothesis, ⟦BFT_A.md: - **Corollary WR (the level-0 Wilson rows).**⟧ | Wilson BCH row q(x): ‖q^c‖ ≤ 9η², Hölder ≤ 8C_qη², given ‖x‖_{𝔐^∇} ≤ η ≤ η_0 with the ∇ leg | K (rows) | **R1** | ⟦REVIEW_BFT_A_S6.md: - **Theorem YH: CONFIRMED.** **Theorem W0: CONFIRMED.** **Corollary WR (a): CONFIRMED-WITH-FIX** (a hypothesis must be⟧ named) |
| LA24 | Lemma BA-3, ⟦BFT_A.md: - **Lemma BA-3 ((CL-3) in 𝔐^∇).**⟧ | ball in 𝔐 ⇒ own plaquette logs ≤ L^{−2(k−j)}(2η + 9η²) (θ_w^c = 2) | K, E (BFT-1) | **R1** | ⟦REVIEW_BFT_A_S1.md: - CONFIRMED: BA-1, BA-3, BA-4 (body), BA-5, BA-7, BA-8 (given G1/G2), BA-9 (implication; one ARGUED step), BA-10, BA-11,⟧ |
| LA25 | Corollary BA-6 / F6, ⟦BFT_A.md: - **Corollary BA-6 (soft-level remainders are irrelevant in 𝔐^∇, marginal in X_c).**⟧ | second-order soft fluctuation ≤ C_6L^{−3(k−l)}η² | K (K_rows' C_6) | **R1** | REVIEW_BFT_A_S1 ("BA-6: sizes CONFIRMED; the 𝒴^∇ bookkeeping has a GAP", repaired as F6) |
| LA26 | Lemma BA-10, ⟦BFT_A.md: - **Lemma BA-10 (holomorphy).**⟧ | uniform contraction on a complex ball ⇒ holomorphic fixed point and value | E (BFT-2) | **R1** | REVIEW_BFT_A_S1 (CONFIRMED list); Codex KOFF §5.3 / GV item 4 use the complexified contraction |
| LA27 | Theorem COF, ⟦BFT_B.md: - **Theorem COF ((CO-fun) under (CC-0)).**⟧ | (CO-fun) for (CC-0) sources | LA1, LA3 | **R2** | ⟦REVIEW_BFT_B_S9_S10.md: ## S10-6 **Corollary COF-crit (§35.6) is WRONG as stated.** Theorem COF is CONFIRMED; its application to the rows is not.⟧; Codex C2 §4 re-runs step (c) on strict plain-only sources |
| LA28 | Lemma DF-cc, ⟦BFT_B.md: - **Lemma DF-cc (funnel-modified dual push-down).**⟧ | d*C(j) = D(S); regrouping of plain currents | LA27, LA3 | **R1** (+ Codex C2 §4 uses the corrected identities) | ⟦REVIEW_BFT_B_S9_S10.md: ## S10-3 Lemma DF-cc (i)-(iii): **CONFIRMED**⟧ |
| LA29 | Proposition COF-size, ⟦BFT_B.md: - **Proposition COF-size.** Under (CC-0) and in the (P0) + (Pl-c) classes⟧ | π_0(C(j)) ≤ C_size(‖j^c_0‖ + ‖j‖_Pc) | LA27, LA3 | **R1** | ⟦REVIEW_BFT_B_S9_S10.md: ## S10-5 Proposition COF-size: **CONFIRMED as an inequality in the (Pl-c) class**⟧ |
| LA30 | Theorem PW-cc's residual estimates, ⟦BFT_B.md: Theorem PW-cc's residual estimates⟧ | residual ℓ¹ bounds of the plaquette response | LA27 | **S** | quoted as an input of COF ("inputs quoted … not re-judged"); not re-derived in REVIEW55_BFTB (⟦REVIEW55_BFTB.md: Lemma LE/BL-C, GU, LIN0, PW-cc's residual ℓ¹ bounds — not re-derived here)⟧); I located no re-derivation |
| LA31 | Theorem YH, ⟦BFT_A.md: - **Theorem YH (level-0 dual bounds).**⟧ | 𝒬_H* ≤ C_YH, 𝒩* ≤ C_YN·n | LA27, LA3 | **R1** | REVIEW_BFT_A_S6 ("Theorem YH: CONFIRMED") |
| LA32 | Theorem W0 (steps 3-5), ⟦BFT_A.md: - **Theorem W0 ((G♯_0-lev0) at m = 0, trivial background, Setting LIN).**⟧ | level-0 divergence-form and plain sources | LA27, LA3 | **R1** | REVIEW_BFT_A_S6 ("Theorem W0: CONFIRMED") |
| LA33 | Theorem GU, ⟦BFT_A.md: - **Theorem GU ((G♯-up) at m = 0, trivial background).**⟧ | divergence-form sources at levels ≥ 1, no Hölder norm of G_l | LA27, LA3 | **R1** | REVIEW_BFT_A_S6 ("Theorem GU: CONFIRMED") |
| LA34 | Lemma TOPD, Lemma LE, ⟦BFT_A.md: - **Lemma TOPD (top-residual duality).**⟧, ⟦BFT_A.md: - **Lemma LE (local energy from the sup).**⟧ | top residual as a pairing with Y^{(b)}; L^∞ → BMO step | LA27, LA3 | **R1** | ⟦REVIEW_BFT_A_S6.md: - **Lemma CS, TOPD, LE: CONFIRMED.**⟧ |
| LA35 | Lemma Q-hold, ⟦BFT_B.md: - **Lemma Q-hold.** For 0 ≤ a < b ≤ k and every level-a 1-form v⟧ | C^{1,α} bound of Q^{(a→b)} | LA4 | **R1** | REVIEW_BFT_B_S5 ("Lemma Q-hold: CONFIRMED") |
| LA36 | LES-div (LINEAR_PACKAGE Lemma 3.2″), ⟦LINEAR_PACKAGE.md: **Lemma 3.2'' (LES-div; l.3271-3284):** for -Δu = Σ_a∂_a^-g_a + h on Q_R, R ≥ 16, the Campanato seminorm of ∇u at scales⟧ | lattice Schauder step C^{0,α} → C^{1,α} | LA4 (EP-int/EP-bd/EP-rec), N (Lemma A), LA32 | **R1** | LINEAR_PACKAGE header review list; Codex GSHARP item 1 names it as an input ("the named LES-div input"), does not re-derive |
| LA37 | LES, J-str, N2-lin (LINEAR_PACKAGE Lemma 3.2, Lemma 3.1 (c), Theorem 3.8), ⟦LINEAR_PACKAGE.md: **Theorem 3.8 (N2-lin, sup forms; l.2502-2516).** For every B_k, uniformly in k ≥ 1 and T:⟧ | the package constants C_R, C_f, C_α under BL-4 | LA18 → K, G | **R1** | LINEAR_PACKAGE header; REVIEW_BFT_A_S2 Part 7 ("CONFIRMED given the package") |
| LA38 | NA-alg (a)-(b), ⟦PROOF.md: - **Lemma NA-alg (explicit su(N) algebra for the normalised soft kernel): PROVEN-HERE.** Norms are Hilbert-Schmidt,⟧ | SU(N) maximiser of an average; soft density ≈ (HS norm of ρ)²/(2N) | K (SG/LA-1′), N (Lemma C) | **R2** | pre-S24 REVIEW_S13_S14 "CONFIRMED-WITH-FIX (domain of (b))" (R1); local uniqueness re-used by Codex NSL F6 and Codex KOFF §4.3 |
| LA39 | Local analytic inputs: (LA-1′) and Codex's completion, ⟦CODEX_REVIEW_KOFF.md: ### 4.3 Independent local analytic completion, with unspecified finite constants⟧; all-orders local constants ⟦CODEX_REVIEW_HIGHER.md: 1. **CONFIRMED — local all-orders inputs.**⟧ | fixed-radius local analytic Taylor bounds (BCH, maximiser, class function); abs(ρ − r) ≤ Cε_l³η² | K (rows, CB), E, N (Lemmas C, D) | **B** | K^{(σ)} bullet ("Printed (LA-1) REFUTED, replaced by (LA-1′)"); TR∞ bullet ("with the corrected higher-order bounds") |
| LA40 | LINEAR_PACKAGE Theorem 4.2(ii) (N2-exp kernels), ⟦LINEAR_PACKAGE.md: **Theorem 4.2 (N2-exp; l.2735-2772).** Let m_* be the minimum over κ ∈ [κ_-, κ_+] of the largest η ≤ 0.1 for which the⟧ | exponential decay of the data kernels | LA1 (via (CO-fun) bullet) | **R1** | LINEAR_PACKAGE header review list; named, not re-derived, in the (CO-fun) bullet |
| LA41 | Lemma A (c) of NSL55 (elliptic constant in the ♮ form), ⟦NSL55.md: - (c) **‖Λ^{(j)}(v)‖_♮ ≤ C_Λ n_0(v)**, C_Λ = C_Λ(α, d, L). (EP-bd's proof: ‖Λ‖_{C^{2,α}} ≤ 16·4C_χ·6C_E·sup_X n_{Ñ_X}(v), and⟧ | only the level-0 C^{1,α} norm of v enters Λ's C^{2,α} norm, plus the sup term | N | **S** for the ♮ form (the C^{2,α} part is inside LA4) | Codex NSL summary table, row "Lemma A elliptic estimate": NOT-VERIFIED independently, ⟦CODEX_REVIEW_NSL.md: Explicit inherited uniform input; algebraic pin/sampling identities rebuilt⟧ |
| LA42 | S4′ covariance of M̄ and uniqueness of W_0 (Decision 4; In-4 of NSL55) | M̄_c(U^g) = g(c_X)M̄_c(U)g(c_Y)^{−1}; φ̂ invariant | N (In-4), K ((GI)) | **R2** | PROOF "Decision 4" (C4 locator); re-derived in NSL55 In-4 (Opus 5.5) and used in Codex FLOW55 §1.1 |
| LA43 | CCP (c)'s Bernoulli constant c_Bern ≤ 59/100 | strict injectivity threshold of M_x | K | **B** | K^{(σ)} bullet ("CCP (a)-(d) CONFIRMED"); Codex KOFF item 7 (ko55_1 exact identities) |

**What the table shows.**
1. **Cross-family coverage of the linear premise set is partial.** Of 43 rows, 8 are **B** (LA1-LA6, LA39, LA43), 8 are **R2**
   (LA7-LA10, LA22, LA27, LA38, LA42 — re-derived by Codex or an Opus 5.5 file but not banked as such), 25 are **R1**
   (pre-S24 lane reviews of unrecorded model only), and 2 are **S** (LA30 PW-cc's residual estimates; LA41's ♮-form elliptic
   constant). Count check: 8 + 8 + 25 + 2 = 43.
2. **The R1 rows are the hidden premise set under [S26-BANKED]'s K^{(σ)}, GV-E, BFT-E, NSL, TOP-cc and (C2-COF) bullets.**
   They are exactly: TS, FP, W, Λ, LR-pot, LIN0, CO-upR/RH, BL-4, BL-2, BL-C, BL-5 (a), WR (a), BA-3, BA-6/F6, BA-10, DF-cc,
   COF-size, YH, W0, GU, TOPD/LE, Q-hold, LES-div, LES/J-str/N2-lin, LP Thm 4.2(ii). None is refuted on disk (several carry recorded fixes: BL-4's LES box constant, BA-6's F6 bookkeeping, WR (a)'s named
   hypothesis); none has a two-family re-derivation on disk that I could locate (Codex reviews name several of them as inputs — FP, LIN0, CO-upR,
   W, LES-div — and explicitly decline to certify them: ⟦CODEX_REVIEW_KOFF.md: All these implications retain the analytic hypotheses of their named⟧
   linear package; they do not independently certify that entire package).
3. **The two S rows are the weakest links in the premise set.** LA30 enters every (C2-COF)/TOP-cc/CC-INV use through
   Theorem COF; LA41 enters every NSL/ID use (Codex NSL marks it NOT-VERIFIED). Each needs a re-derivation, not a citation.
4. ASSEMBLY55 N24's blanket "inherited, NOT-VERIFIED" is **too coarse in one direction**: LA1-LA6, LA39, LA43 are banked
   cross-family and LA7-LA10, LA22, LA27 have Codex re-derivations of the load-bearing step. It is **accurate** for the R1
   and S rows.

---

## §4. Every [S26-BANKED] bullet, and the dictionary objects it is stated in (target D3, first half)

Read: PROOF.md's [S26-BANKED] block as on disk at 04:58 UTC (36 bullets; batch-header lines excluded) and, for each, the
matching Codex banking list (§0). "Stated in" lists the objects of §1-§2 the bullet's banked scope is about; "FL" points to
the flags of §5. A bullet is **convention-clean** if every object it names is the canonical one of §1-§2 or carries its own
explicit conversion.

| # | Bullet (PROOF.md locator) | Stated in (dictionary objects) | FL |
|---|---|---|---|
| B1 | ⟦PROOF.md: (T-UNIF), repaired — CONFIRMED⟧ | D³ of PROOF's E_k^br at V = 1 = D³𝔉_k(1) on the composite linear branch ζ^c (TOWER-VAR (d)); Setting SC (κ_j, O3-O4); Q with ‖Q^j‖ ≤ 𝔮₀L^j (O1); N3 (max row ℓ¹ sum); levels/units C1-C2; Z = 1; d = 4; "uniformly in k and T" | FL1, FL5, FL15 |
| B2 | ⟦PROOF.md: (CO-fun) on the composite-co-closed class — BOTH HALVES CONFIRMED in the (C2-COF) form⟧ | cc sources (O9) of Setting LIN^cc; Codex C2's N = N_Σ (O11); f_0 sup + pointwise Hölder (C9); κ_l ∈ [κ_−, κ_+] (O3); 0 < α < θ < 1 (O12); Z = 1, m = 0, T ≥ 1 (O13); the exact dipole/face-flux algebra (S4′ contours, C3) | FL6 |
| B3 | ⟦PROOF.md: GZ-SLOT / GZ-FALSE — REFUTED⟧ | (CovLift)(iv)'s g_Z clause (O6 Z^sm); TOWER-VAR's 𝔉_k (O4); residual/soft-source formulation; level-0 curvature with ω_0 = 1 (O11) | FL12 |
| B4 | ⟦PROOF.md: (CC-0) at every critical point — REFUTED⟧ | (CC-0) vs cc (O9); Lemma CD root-pinned (LA2); critical points of 𝔉_k (O4, O6) | — (clean) |
| B5 | ⟦PROOF.md: NLOC Theorem NL-3′'s proof step — REFUTED⟧ | NLOC's chain minimiser and sup representative; T = coarse torus side (O13) | — (clean) |
| B6 | ⟦PROOF.md: Gauge-invariant half of BFT-5 clause (b) at the trivial background — CONFIRMED as source-only linear estimates⟧ | Z = 1, weight zero; Setting LIN^cc, B_k = 0 (O9); N(S) — the Pc form (O11); κ_+ (O3); ‖x‖_inv (O10); "uniformly in admissible gauge fixing" = invariant outputs only (O8) | FL6 |
| B7 | ⟦PROOF.md: Lemma TR (level-count factor) — CONFIRMED at the quadratic level⟧ | exact critical points through the trivial chain (O6); BCH₂ rows' plain coarse units π_l (C2); m = DEPTH k−1−l in "L^{−m}" (C1); κ̂ (O3); full-source bound in N_Σ (O11; Codex TR item 4) | FL16 |
| B8 | ⟦PROOF.md: Sphere route — equatorial reflection positivity CONFIRMED⟧ | sphere lattice with β_Q = 2N/G² (standard G, C6); gauge-invariant half-algebras; physical units (C2) | FL10 |
| B9 | ⟦PROOF.md: Smallness hierarchy — strict acyclicity of the encoded graph CONFIRMED⟧ | SMALLNESS_DAG's nodes; thresholds (O15) incl. node C_flat_i = per-level C_♭^{(i)} of E_i^br (O5) | FL14 |
| B10 | ⟦PROOF.md: Theorem K^(σ) (corrected) — CONFIRMED conditionally⟧ | 𝔉_k (O4); 𝒞_glob, trivial centring, m = 0, T ≥ 3 (O13); 𝔐^{(σ)} (O10); N^{(σ)} (O11); Γ with ΓΞ = −1 on Λ_* (O7-O8); cc (O9); weight triple (2, 2+σ, 1) (O12); composite critical point/value (O5-O6); lane-A inputs (§3) | FL6, FL7, FL11, FL22 |
| B11 | ⟦PROOF.md: GF-E and GF-E′ on S_E at m = 0 — CONFIRMED⟧ | S_E / Γ^{(T)} and the orbit norm (O8); 𝔐^∇ (O10); N(S) (O11); GF-DEP; LINEAR_PACKAGE's alias symbol on the strip abs(Im z_ν) ≤ 7/5 | FL2, FL6, FL11 |
| B12 | ⟦PROOF.md: Clause (b) with decay — CONFIRMED⟧ | weight rate m with 0 ≤ m ≤ m_Y / m < m_*′ (C10); N_m, N_{Σ,m} (O11); ‖·‖_{inv,m} (O10); Convention K weights (C3); COF_m under (CC-0) (O9) | FL3, FL16 |
| B13 | ⟦PROOF.md: Rotation reduction — CONFIRMED in part⟧ | finite-torus Ward identity; clover density e_a and normalised torque (O16); CD, SRC-O, SRC-W (source-inserted chain with fixed kernels, C8); physical units (C2) | FL9 |
| B14 | ⟦PROOF.md: Non-freeness comparator — CONFIRMED for a narrower class⟧ | free coefficient 3(N²−1)/(128π²) in the STANDARD continuum normalisation (g_std, standard heat time, C6); quadratic abelian observables; KLM | FL10 |
| B15 | ⟦PROOF.md: RLARGE — W-cb♯ and FI-1 CONFIRMED conditionally⟧ | canonical u_k (C6); chain kernel κu_iφ_M (C8); (F_R) with R = R_F; RLARGE's θ := min{θ_cap, a_A°/a_bad} ("θ-first order") — NOT the class exponent | FL19, FL20 |
| B16 | ⟦PROOF.md: Node A — key reductions CONFIRMED⟧ | (GAUSS); push-down; DOM′'s 1 + 2Rg_K² with R = R_F, canonical g (C6); tilt θ (Chernoff) | FL19, FL20 |
| B17 | ⟦PROOF.md: Full nonlinear COF-crit / NCE (i) / CC-CRIT at critical points (Theorem TR∞, Corollary CC-CRIT∞) — CONFIRMED conditionally⟧ | actual critical point in the 𝔐^∇/data ball (O6, O10); Z = 1, weight 0; Ñ_Σ (O11); 0 < α < θ < 1; admissible Γ (invariant outputs, O8); local constants LA39 | FL6 |
| B18 | ⟦PROOF.md: Proposition GV-E, the corrected slice contraction, the weighted field estimates and slice identities — CONFIRMED as scoped implications⟧ | S_E / Γ^{(T)} (O8); 𝔐^∇, 𝔐^{(σ)} (O10); N_Σ ≤ L·N^{(σ)} (O11); θ₀, σ (O12); depth slices Λ^{(j)} and the −640/19683 witness (O8); GV-E_m in COFM55's weighted norms (C10) | FL6, FL11 |
| B19 | ⟦PROOF.md: Coupling flow — the corrected conditional reduction to (UIR^♮), the fixed-n tadpole/ghost results, the trivial-point Ward identities and the arithmetic — CONFIRMED⟧ | K̄ on the normalised kernel (C8); φ-tower vs k̃ (O2; k̃ literal REFUTED); u-units β_0^std (C6); trivial-point jets (O5) | FL4, FL10, FL13 |
| B20 | ⟦PROOF.md: Node A residual — both counterexamples to the Anderson-type mechanism⟧ | probability models; finite SU(2) Wilson-action patches with S = Σ_P s(U_P) (C7) in the coordinates U = exp(i v·σ), i.e. FLOW's normalised Lie coordinates at N = 2 (C5) — ⟦CODEX_REVIEW_NRES.md: These are the source's conventions.⟧; BL-TILT's hypotheses | — (clean at dictionary level) |
| B21 | ⟦PROOF.md: Proposition T (rotated-lattice universality is controlled by uniform conditional comparisons; the coarse law never enters) — CONFIRMED⟧ | conditional comparisons at fixed volume; the AF envelope in canonical g (C6) | FL10 |
| B22 | ⟦PROOF.md: a_RS has no consumer on the live RLF-step v3 route — CONFIRMED⟧ | RLARGE constants a_RS, a_η, η_q, ε_1 (O15; SYMBOLS families) | — (clean) |
| B23 | ⟦PROOF.md: Theorem GA (perturbative background transfer by alignment) — CONFIRMED with its exact hypotheses⟧ | Z ≠ 1 backgrounds; Λ_0 = VANISHING space (O7); Ξ_Z "positive-d" generator (C4); cc_Z (O9); RW♯ at Z = 1, m = 0 with residual weight L^{(1+θ)(k−1−i)} (θ = class exponent) and N(S) (O11) | FL11 |
| B24 | ⟦PROOF.md: Rotation, flat route (TQ) — reductions CONFIRMED, TQ itself NOT-VERIFIED⟧ | Λ := ‖S′‖_∞ (a fifth Λ, O7/O8 glyph); centred Wilson two-point orbit (O16); physical units | FL9 |
| B25 | ⟦PROOF.md: Source-inserted RG (SRC) — Proposition B and Lemma V CONFIRMED; downstream NOT-VERIFIED⟧ | fixed-kernel chain (C8); Lemma V's g_0 = u_0^{−1/2} canonical (C6), coefficient ≥ 3/2000000 multiplying g_0⁴a⁻⁴; smeared clover density (O16); (F_R) with R_F; downstream SRC consumes 𝒮_K and a sup-norm coefficient ball | FL7, FL8, FL10, FL19 |
| B26 | ⟦PROOF.md: BFT-3 on the global potential-small domain — CONFIRMED conditionally; BFT-4 OPEN⟧ | "E_k^br" := E^cb (O5); 𝒞_glob, PD-glob (O13); weight μ (C10) and rates μ/4, μ/3; 𝔱 in level-k ℓ¹ units (C2); GV-E_m (COFM55 weights, Convention K, C3); funnel constant 121/13 | FL1, FL3, FL5, FL7 |
| B27 | ⟦PROOF.md: Balaban-method reading (BALABAN_EXTRACT) — checked against the open arXiv expositions⟧ | fixed regularity radii vs coupling-dependent cuts (O15); Dimock's k direction (C1); Gaussian composition; hard-source identity | — (clean) |
| B28 | ⟦PROOF.md: (NSL) and BFT-0's per-level identification — CONFIRMED conditionally⟧ | S_E^{(j)}, Λ^{(j)}, 𝒢^{(j)}, 𝒢^{rt}_j (O7-O8); ‖·‖_{(σ),j} pointwise vs Campanato (C9); ‖·‖_♮ (O10); C_N = 4 + 3C_Λ with C_Λ = NSL55 Lemma A (c)'s constant; E^cb vs E^br (O5); BR1 at κ_0 = 1 (O3); 𝒞_glob, m = 0, T ≥ 3; scaled-norm holomorphy (O13) | FL1, FL2, FL17, FL18, FL22 |
| B29 | ⟦PROOF.md: Coupling flow: (UIR^♮) reduced further — CONFIRMED as a conditional implication⟧ | φ objects (O2); jet class 𝔍(m_0, C_J, c_E) with (J1) β[𝒯] = 1 in the s-normalisation and FLOW coordinates (O4 NM3-NM4); β_0^std in u-units (C6); n = number of steps (C1); infinite volume | FL4, FL5, FL10 |
| B30 | ⟦PROOF.md: BFT-4 (a) on 𝒞_glob — CONFIRMED conditionally, with one named premise (R)⟧ | "E_k^br" := E^cb, R_k = E^cb − S_W (O5, C7); Convention C (C3; CORNER); centred cutoffs; PD-glob (O13); pieces invariant under CONSTANT gauges (O7); rate log 2/(16R + 80) with R = random-walk box side | FL3, FL19, FL22, FL23 |
| B31 | ⟦PROOF.md: SRC via analyticity — scoped pieces CONFIRMED⟧ | ‖·‖_cf (O14) on 𝒞_glob; e-source as a Wilson-coefficient shift in the fixed-kernel chain (C8); harmonic-measure exponent 1 − 4arctan(r)/π; (Flow-an), (F_R) with R_F | FL8, FL7, FL19 |
| B32 | ⟦PROOF.md: Non-freeness witness — comparator mathematics CONFIRMED, the identification bridge NOT⟧ | comparator realisation; (4π²/N)u in canonical u (C6); 𝓔 = t²E_pl on bare links (O16); (ID♮) (♮ glyph, O10) | FL10 |
| B33 | ⟦PROOF.md: Sphere route — construction, reflection positivity and Ward algebra CONFIRMED⟧ | β_Q = 2N/G² (standard, C6); geometric units of the sphere; gauge-invariant local half-algebras | FL10, FL19 |
| B34 | ⟦PROOF.md: Background transfer (R2) — alignment reduction CONFIRMED conditionally; S_E obstruction CONFIRMED⟧ | S_E (O8) as reference; Λ_HC with Λ_HCΞ_1 = −1 on the vanishing Λ_0 (O7-O8); exponent (2+θ)k−6−θ with θ = class exponent (O12); C′_b | FL11 |
| B35 | ⟦PROOF.md: Assembly audit — scoped implications CONFIRMED⟧ | DIAG over (a, R) with R = radius; kernel-to-row-sum conversion in ℓ¹ level-lattice units, 0 < m_0 < m/3 (C10); finite-chain germ for the normalised positive-κ φ-chain (O4-O5) | FL1, FL5, FL19 |
| B36 | ⟦PROOF.md: Node A convexity — counterexamples CONFIRMED, the full chain no-go NOT⟧ | bare Wilson action (C7); u_0 = 1/g_0² canonical (C6); stripe amplitude β (NOT β_Wilson); plaquette-cut units | FL21 |

**Bullets that are convention-clean:** B4, B5, B20, B22, B27 (5 of 36). Every other bullet names at least one object whose
glyph or normalisation differs somewhere else in the block or in its consumers; §5 says which of those differences can
cause a wrong chain and which are cosmetic.

---

## §5. Flags: one name for two objects, or a chain across a convention change (target D3, second half)

Each flag: the two objects (§1-§2 ids), where they meet (banked bullet or consumer, located), whether the difference can make
a chained statement false, and the **precise repair** (a restatement) or the **missing lemma** (a new statement, OPEN).
Verdict words apply to the flag's factual claim (that the two objects differ / that the chain crosses them).

**FL1 — "E_k^br" names two objects inside the banked block. CONFIRMED (read at source).**
B1 ((T-UNIF)) bounds D³ of PROOF's per-level branch E^br at V = 1 (TOWER-VAR (d)); B26 (BFT-3) and B30 (BFT-4 (a)) write
"E_k^br" for the composite critical value E^cb (O5 locators); B28 keeps them apart. Chains that cross: FLOW55 uses N1-15 for
D³𝒯_k(1) (⟦FLOW55.md: | cubic tree jet D³𝒯_k(1) k-uniform | Theorem N1-15 (+ NQ-1, + T-UNIF TU-5/TU-6): "N3(D³E_k^br(1)) ≤ 𝔚·L^{(d−4)k} + …", uniform in k and T |⟧);
ASSEMBLY55 F23 feeds BFT3-glob (E) into UIR55's (TC-b)_𝔍. **At trivial-point jets the chain is sound:** (T-UNIF)'s object is,
by TOWER-VAR (d), the cubic vertex D³𝔉_k(1)[ζ^c·, ζ^c·, ζ^c·] of the composite functional on the composite linear branch; any
nondegenerate critical family of 𝔉_k through the trivial chain has this third derivative (envelope identity; FLOW55
"Lemma ENV"; CODEX_REVIEW_ASSEMBLY R6's finite-chain germ statement, banked conditionally), so the bound holds for E^br, E^cb
and E^min alike at fixed (k, T). **Repair (restatement):** state (T-UNIF) as a bound on D³𝔉_k(1)[ζ^c·, ζ^c·, ζ^c·] "for every
nondegenerate critical family of 𝔉_k through the trivial chain", and write E^cb (not E_k^br) in B26/B30. **Beyond jets**
(level-uniform domains) the two objects are not identified (no uniform bridge; CODEX_REVIEW_NSL's most dangerous item): see
FL14. The fourth-order jet is NOT covered by the cubic identity (R6: E″″ = F″″[ζ⁴] − 3⟨c, H⁻¹c⟩), so a quartic chain needs
the full germ identification of R6, not TOWER-VAR (d).

**FL2 — per-level slices versus S_E (field components). CONFIRMED (banked GF-DEP); repair is a restatement.**
Banked statements fix S_E / Γ^{(T)} (B11, B18), any Γ satisfying (GV) (B10), or depth slices S_E^{(j)} (B28). Consumers still
posed in a per-level slice: SF's (a5-G♯) (O6 locator "per-level covariant slice through"), B-NA-red (O8 locator), BR1 / NAH-ind
(E^br's construction). By GF-DEP, field components depend on the slice; ‖x‖_inv and N_res do not. **Repair:** every consumer
that reads only gauge-invariant outputs needs no change; every consumer that reads field components (potentials,
gradients, Hölder of potentials) must be restated in S_E or in the orbit norm (equivalent up to C_Π). **Missing lemma only
if** a consumer genuinely needs the per-level slice: a per-level ↔ S_E transfer (GSHARP55 §5.5: ARGUED, "not consumed"). At
level 1 the BR1 slice and S_E^{(1)} are already bridged by E1 (B28) on 𝒞_glob(ε_E1). N5's fluctuation slice (NA-FP's h_U) is a
gauge fixing of the Gaussian measure, not of the background, and gauge-invariant fluctuation integrals do not depend on it;
it is not interchangeable with S_E for BFT-5's field components.

**FL3 — lower-corner versus centred positions. CONFIRMED (banked CORNER); repair is a convention statement.**
B30 (BFT-4 (a)) is proved in Convention C; B12 (COFM55) and B26's weighted inputs place positions in Convention K (C3
locators). For **weights** the conventions differ by at most e^{2μ} (harmless; B26's chain through COFM55/GV-E_m is sound).
For **cutoff multipliers and commutators at σ > 0** they are not interchangeable (B30's Proposition CORNER). Chains that
would cross: lane B's W-mult^σ / (W-comm)^σ (BFT_B §10, Convention K by default) and BFT34_55's RW-cc-walk (already refuted).
**Repair:** declare Convention C binding for every cutoff multiplier and commutator used at σ > 0 (BFT4W55 §2.1's
definition); positions in weights may stay in K with the factor e^{2μ}. No missing lemma.

**FL4 — φ-tower versus k̃-tower. CONFIRMED (banked FLOW55 item 2).**
B19 refutes the literal k̃ setting for N ≥ 3; B29 works with φ objects. Still on k̃: FLOW's Def F-strip and its consumers
(SF-bg), (SF-g)_k, and FLOW55 §3.4's one-step operator ⟦FLOW55.md: **one-step soft-constrained fluctuation operator** Õ_k(U, V) := slice compression of Hess_U(𝒯_k + κΣ_ck̃(V_c, M̄_c(·)))(U*)⟧,
which is evaluated at a NON-trivial U*. **Repair (restatement):** replace k̃ by φ in Def F-strip and in Õ_k, and move
−κu·d(M̄_c(U)) into the normaliser log 𝒩′ as HIST's [RH2-fix 10] states (it is O(u) per link on the ε_1-domain, not one-loop
sized). Trivial-point coefficient statements (jets of order ≤ 5) are unaffected. No missing lemma.

**FL5 — 𝔉_k's normalisation versus the stripped tower's. CONFIRMED (definitions read); resolved here as NM1-NM5 (O4).**
B26's E-derivatives are of E^cb in HS coordinates, 𝔉-normalised; B29's jet class 𝔍 is for 𝒯_n (stripped, s-normalised,
FLOW coordinates, (J1) β[𝒯] = 1). ASSEMBLY55 lists "the normalisation map between 𝔉_k's κ_jφ̂ and the 'stripped φ-tower'" as a
remaining condition of F23 (⟦ASSEMBLY55.md: the normalisation map between 𝔉_k's κ_jφ̂ and the "stripped φ-tower"⟧) and CODEX_REVIEW_ASSEMBLY
R3/R12 keep it open. **Repair:** NM1-NM5 — κ_j ≡ κ; 𝔉_k = N·E(chain); y = √N·B, so D^n_y E^cb = N^{1−n/2}D^n_B(E^cb/N); (J1) holds
in both normalisations because quadratic forms coincide; k̃-jets = φ-jets to order 5. Rates and k-, T-uniformity transfer
unchanged; constants change by N-powers. **Still open after NM** (not dictionary items): (GERM) beyond R6's finite-chain
scope, (JET-∞), premise (R), and that 𝒯_n is replaced by the φ-tower (FL4).

**FL6 — three source norms N(S), N_Σ(S), N^{(σ)}(S). CONFIRMED (banked mismatch witness and repair, Codex GV items 1-2).**
B6 prints its bound with N(S) (Pc); B11 (GF-E) is in N(S); B10 (K^{(σ)}) needs N^{(σ)}; B2's "N" is N_Σ; B17 uses the weaker Ñ_Σ.
A consumer feeding an N(S)-bound into K^{(σ)} crosses norms (N/N^{(σ)} can be L^{θ(k−1)}). GV-E (B18) is the banked repair; it
uses the N_Σ form of TOP-cc/CC-INV, which Codex TOPCC item 3 confirms (⟦CODEX_REVIEW_TOPCC.md: The bound also holds with N_Σ, and with the explicitly defined weaker⟧ Ñ_Σ)
but **B6's PROOF bullet does not print**. **Repair (restatement of B6):** append "— and with N_Σ(S) in place of N(S) (CODEX_REVIEW_TOPCC
item 3); the N_Σ form is the one GV-E consumes". No missing lemma.

**FL7 — "ε_0" for two different smallness classes; 𝒞_glob versus curvature-small. CONFIRMED (read).**
Every banked BFT bullet (B10, B18, B26, B28, B30, B31) is on 𝒞_glob, ε_0 bounding ‖B_k‖_D = max link potential in one global
gauge (O15 locator). SRCCD55's coarse small-field set uses "BFT's ε_0 at level K" for an OPERATOR-norm bound on PLAQUETTE logs
(C5 locator), REVIEW_S22's target is the curvature-small class (O13 locator), SF (BG-unif) and RLARGE's local regions are
curvature/op-norm classes. On 𝒞_glob, plaquette logs are ≤ 4‖B_k‖_D (the bi-invariant triangle inequality used in NSL55's E1
proof), so 𝒞_glob(ε) ⊂ {curvature ≤ 4ε}; the converse fails on large tori (holonomy; OFFGLOB55 in flight). **The chain
"SRC-κ on 𝒮_K ⇐ BFT" crosses this change.** **Missing lemma (OPEN):** BFT-0…4 on the curvature-small class (and on local
small-field regions with frozen exterior) — ASSEMBLY55 F7 / OFFGLOB55. **Interim repair (restatement):** state 𝒮_K as
𝒞_glob(ε_0) at level K, i.e. "U_K = e^{B_K} in one global gauge with ‖B_K‖_D ≤ ε_0", and record that this is a strict subclass.

**FL8 — coefficient fields: sup-norm ball consumed, ‖·‖_cf produced; and ε̂_0 written for two slots. CONFIRMED (read).**
B31 banks SA-K in the sup-plus-Wilson-Hölder class; SRCCD55 §0 (i) consumes a sup-norm ball (O14 locators); B25's
downstream SRC items inherit SRCCD55's class. That the sup ball is genuinely too large is ARGUED in SRCAN55 ("size comparison
ARGUED"); Codex SRCAN item 7 confirms the flux mechanism and sufficiency of the Hölder class and does not bank necessity.
**Repair (restatement):** state SRC's coefficient class as ‖ε‖_cf := ‖ε_W‖_∞ + [ε_W]^∞_α + max_{0≤l<k}‖ε_{S,l}‖_∞ (Wilson
coefficient ε_W on level-0 plaquettes; soft coefficients ε_{S,l} on level-(l+1) links), with point sources entering only
through shrinking-radius envelopes (ASSEMBLY55 F10/F15). Whether a sup-ball version can hold is OPEN, not refuted.

**FL9 — physical versus coarse units for rates. No defect found; conversion recorded.**
SRCCD55's CD rate m_c is per 1/ℓ_ref (C10 locator); BFT rates (B26: μ/4, μ/3; B30: μ_W) are per coarse unit of a depth-k
problem, i.e. per level-k spacing ℓ_k = L^{k−K}ℓ_ref. The two coincide only when the BFT problem is posed with its datum at the
reference level (depth K). **Rule:** a rate μ per coarse unit of a depth-k problem is μ/ℓ_k per physical unit. I found no
banked bullet that converts silently (B13, B24, B25 state their rates as hypotheses in physical units).

**FL10 — two coupling normalisations among banked items. CONFIRMED (read); no live numerical error found.**
Canonical u = 1/g² = β_Wilson = 2N/g_std² (C6): B15, B16, B19, B25 (Lemma V's g_0), B29 (β_0^std), B32 ((4π²/N)u), B36 (u_0).
Standard g_std: B14 (A_∞ = 3(N²−1)/(128π²) multiplies g_std²), B8/B33 (β_Q = 2N/G²), PROOF S3. Chains that cross: HINT2_55's
H-RED compares Yang–Mills TS bounds in canonical g with the comparator in g_std — HINT55 converts explicitly (C6 locator);
the sphere route's W0 needs FLOW (canonical u) for a profile written in G (u = 2N/G² there). **Repair:** state the
normalisation at each use; in canonical g the leading YM value is f = 2N·A_∞·g² + O(g⁴) = 3N(N²−1)g²/(64π²) + O(g⁴), and
Lemma V's g_0⁴ is (g_std²/(2N))². PROOF's Decision-4 "κ/g²" should be declared canonical (bookkeeping; C6).

**FL11 — Λ_0 is two spaces. CONFIRMED (read); no live error found.**
B10 (K^{(σ)}: ΓΞ = −1 on Λ_*, Λ_0 = constants on roots), B11 (GF-DEP: "ΓD a bijection of Λ_0" with GSHARP55's VANISHING Λ_0),
B23/B34 (BGT55/ALIGN55: vanishing Λ_0; at Z ≠ 1 there is no quotient by constants). Read with the wrong space, the GF-DEP
admissibility "ΓD bijection of Λ_0" is false for every Γ (Ξ kills constants). **Repair (restatement):** write Λ_* wherever the
vanishing space is meant when these statements are quoted together.

**FL12 — left versus right gauge action. CONFIRMED (dc55_2); no banked bullet affected.**
C4: BFT_B §13.3 (GI-frame) and §12.2's printed (CovLift) cocycle are in the right action; everything banked, and BFT4B55's
Lemma AVG (⟦BFT4B55.md: - **𝒢** := SU(N)^{sites} (real level-k gauge group) acting by (V^g)_b := g_x V_b g_y^{-1}, b = (x, y).⟧), is in the left action.
**Repair:** any BFT-4 (b) / (CovLift) use states the cocycle in RS7-8's left form ĥ(h_2h_1, V) = ĥ(h_2, V^{h_1})ĥ(h_1, V), or
converts by g ↦ g^{−1}.

**FL13 — "E^min" is two functions for N ≥ 3. CONFIRMED (Lemma HF; banked FLOW55 item 2).**
ASSEMBLY55 §1.1 lists FLOW's 𝒯_k and HIST's 𝓔_k as one E^min. 𝒯_k ≥ 𝓔_k with equality for N = 2; they share jets of order ≤ 5
at V = 1 and differ off it. FLOW's (SF-bg) reads 𝒯_k on a k-uniform domain; HIST's (I_k^E) reads 𝓔_k. **Repair:** FL4's
restatement (φ everywhere), after which C5b's (MIN-cb) / critical-value alternative applies to one object.

**FL14 — per-level E^br consumers chain into E^cb producers. CONFIRMED distinction (CODEX_REVIEW_ASSEMBLY R7); repair NOT-VERIFIED.**
SF's (BG-unif) and PROOF's (H-C⁺)/(H-ℂ) quantify every level of E^br on a level-uniform class (O5; ASSEMBLY55 C1, C2; B9's DAG
node C_flat_i reads C_♭^{(i)} of E_i^br — an off-route node, a mismatch only if revived). Producers deliver E^cb on 𝒞_glob. **Repair (restatement):** F_j := E^cb_j + κ_jφ̂, tower
:= Theorem ID (I4)'s points, uniqueness := Corollary K-U (fixed radius, modulo 𝒢^{rt}_j). **Missing:** (i) a line-by-line audit
that these consumers use no BR1-specific object at levels ≥ 2 (R7: the cost-free repair is NOT-VERIFIED); (ii) FL7's class lemma.

**FL15 — Q_str is two operators (NORMS versus LINEAR_PACKAGE). CONFIRMED (both formulas read, O1); REVIEW55_NORMS's 108-entry count not re-run here.**
B1 rests on Theorem N1-15, whose NORMS §N1 defines Q_str differently from the package; the uses N1-15 makes survive (row sum
L, transpose norm L^{1−d}), but Lemma N1-4's proof uses NORMS's own (I8). **Repair (restatement):** NORMS §N1's Q_str :=
LINEAR_PACKAGE's (O1). No missing lemma (REVIEW55_NORMS r55n-F4).

**FL16 — "m" is a depth in B7 and a weight rate in B12/B26/B35. CONFIRMED (read).**
B7 prints "π_l ≤ A_Bκ̂L^{−m}" with m = k − 1 − l (CODEX_REVIEW_TR item 3's convention); B12 "0 ≤ m ≤ m_Y" is the weight rate;
B35's "0 < m_0 < m/3" uses BFT's decay weight m. **Repair (restatement of B7):** write q := k − 1 − l: "π_l ≤ A_Bκ̂L^{−q}".

**FL17 — "C_Λ" in B28 is not Lemma Λ's constant. CONFIRMED (read).**
B28 prints "C_N = 4 + 3C_Λ"; there C_Λ is NSL55 Lemma A (c)'s elliptic constant (⟦NSL55.md: C_Λ := the draft's Lemma A (c) constant (**not** Lemma Λ's C_Λ = 10, BFT_A "13.11 Lemma Λ"). C_Δ, η_1, η_2 := the draft's⟧).
Substituting Lemma Λ's C_Λ = 10 (also a banked-at-lane-level constant, LA14) would give a wrong number. **Repair (restatement of
B28):** "C_N = 4 + 3C_Λ^{(A)}, C_Λ^{(A)} := NSL55 Lemma A (c)'s constant (an inherited input, LA41)".

**FL18 — κ_0 in B28 (BR1's coupling) versus Theorem CE's κ_0. CONFIRMED (read); cosmetic.**
E1 runs BR1 "at κ_0", the level-0 kernel coefficient (κ_0 = 1 on PROOF's session-23 class, O3 locator); PROOF also defines
κ_0 := 16 log 12800 ≈ 151.3 (Theorem CE). SYMBOLS §6.5's κ_0 family misses the first. **Repair:** write κ_0^{ker}.

**FL19 — "R" in banked bullets. CONFIRMED (read).**
B30's rate log 2/(16R + 80) has R = the random-walk box side (BFT4W55: "D_W := 16R + 80"); B15, B16, B25, B31's (F_R) has R = R_F;
B35's DIAG and B33's sphere use R for a radius; SRCCD55 uses R for the torus side. **Repair (restatement):** R_W, R_F, R_sph,
R_tor (CODEX_REVIEW_SRCAN item 13 already demands R_F in flow formulas).

**FL20 — "θ" in B15 is RLARGE's large-field fraction, not the class exponent. CONFIRMED (read).**
⟦RLARGE_U55.md: **θ := min{θ_cap, a_A°/a_bad}** (θ_cap the CAP-1 choice), then a_A := min{a_A°, 6θa_bad} ≥ θa_bad, then a = θa_bad.⟧
versus the class exponent θ of B2, B6, B10, B17, B23 and B34's "(2+θ)k−6−θ" (O12), and NODEA55's tilt θ (B16). **Repair:** θ_LF
for RLARGE's. Cosmetic inside each bullet; dangerous only in a cross-bullet comparison, of which I found none.

**FL21 — "β" in B36 is a stripe amplitude. CONFIRMED (read); cosmetic.**
B36's "at β = g_0, u_0β² = 1" uses LCONV55's stripe amplitude β (⟦LCONV55.md: Chart: U_ℓ = exp(i(A_ℓ + v_ℓ)·σ), stripe A_2 = a(x_1 mod 3)σ_3 with **rational** β ∈ {1/5, 1/20}; the second-order expansion of⟧),
not β_Wilson (= u_0), the β-functional β[·], the slopes β_±, or β_0^std. **Repair:** β_str.

**FL22 — four polydiscs. CONFIRMED (read).**
PD-glob 𝒫_ε (link-coordinate polydisc in one global gauge; B10/B26/B30); NSL's complexified SCALED-norm neighbourhood (B28;
Codex NSL item 2: no unweighted fine-link polydisc banked); REVIEW_S22's BFT-2 polydisc "in curvature-adapted coordinates"
(consumed by BFT-4's Cauchy step, O13 locator); HIST's 𝔇_α(X) in normalised Lie coordinates of a local gauge (radius ×√N in HS
coordinates, C5). **Chain that crosses:** REVIEW_S22's "C_♭^{(k)}, (H-G) … level-uniform by Cauchy" needs BFT-4 on the
curvature-adapted polydisc; B30 delivers PD-glob (ASSEMBLY55 F7/N19). **Missing lemma:** FL7's class extension. Inside 𝒞_glob the
chain from B30 to Cauchy bounds on PD-glob is sound.

**FL23 — constant-gauge versus local-gauge invariance of BFT-4's pieces. CONFIRMED distinction (CODEX_REVIEW_ASSEMBLY R11).**
B30 banks pieces "invariant under constant gauges" and explicitly not local gauge invariance; REVIEW_S22's BFT-4 asks for
"gauge-invariant local polymers"; SRCCD55 §5.1/§5.4 consume BFT-4 for per-polymer localisation (whether local invariance
is needed there is exactly BFT4B55's T0 question; I did not settle it). **Missing:** BFT-4 (b) (BFT4B55 + its Codex review,
on disk, not banked) or an audit showing no consumer needs local invariance (BFT4B55's T0).

**FL24 — Campanato versus pointwise Hölder inside banked constants. Note (handled explicitly).** K^{(σ)}'s 𝔐^{(σ)} and
N^{(σ)} are Campanato; NSL/ID use pointwise with C_0′ = (1 + C_T)C_0 (C9); ‖·‖_cf, N^{(σ)}_{μ,f} and COFM55's G_0 norm are
pointwise. Every banked use converts explicitly (BL-C or 1 + C_T). No flag beyond the constants.

**FL25 — h_l is two operators. Note (no step depends on it; COFUN_CC §7.2).**

---

## §6. Addendum: five bullets banked at 05:25:45 UTC (after this file began), and errata to §3 (append-only)

**What changed on disk.** PROOF.md was rewritten at 05:25:45 UTC (stat), after my §4 read (04:58 UTC). Diff of the
[S26-BANKED] block against my saved copy: five new bullets (below, B37-B41) and one amendment to B30 ("[(R) since PROVEN —
RLOC55 + CODEX_REVIEW_RLOC, line below]"). No other bullet changed. Codex banking lists read for all five (complete; each
ends with its "Exactly what may be banked" list).

### 6.1 The five new bullets, and the objects they are stated in

| # | Bullet (PROOF.md locator) | Stated in | FL |
|---|---|---|---|
| B37 | ⟦PROOF.md: BFT-4 (b) — the averaging reduction CONFIRMED; "no consumer" NOT⟧ | left gauge action (C4; BFT4B55's 𝒢 acts by (V^g)_b := g_xV_bg_y^{−1}); an UNCENTRED weighted sup polymer norm and the induction's CENTRED polymer norm D_X := sup_D abs(R_X(W) − R_X(1)) (new, O17); interior charts with radii ε_gl/4, ε_top ≤ Lε_gl/(4C_lift); 81³ anchoring; HIST's (I_k^E)″ polymer class | FL12, FL13, FL23, FL28 |
| B38 | ⟦PROOF.md: Off 𝒞_glob — local components CONFIRMED, Theorem OFF NOT (GAP)⟧ | the data classes 𝔅_k(ε), 𝔅^ℂ_k(ε, r), 𝒞_glob(s), its gauge saturation 𝒞*_glob(s), the frame class 𝔑_k(R, α) (O13 supplement below); s = ‖B_k‖_D versus ε = curvature; d(W, 1) the HS-geodesic distance (C5); hierarchical covariant routing at U | FL7 |
| B39 | ⟦PROOF.md: Large fields — lemmas CONFIRMED, route replacement NOT endorsed⟧ | the normalised fixed-kernel chain (C8); canonical u, g_0 (C6); flow slopes β_− and β_* (u-units; LARGE55's β_* is an upper slope, ⟦LARGE55.md: (iv) if the bare coupling obeys u_0 ≤ u_* + β_*K log L⟧); B_N(ε); n_♯, a_eff, c_B | FL10, FL21 |
| B40 | ⟦PROOF.md: Sphere route — W0 and N5 as conditional implications CONFIRMED⟧ | the SPHERE's W0 (Ward/dilation profile) and N5 (seam transparency) — NOT BFT_A's Theorem W0 (LA32) and NOT PROOF's node N5 (FL26-FL27); u = local inverse coupling in u-units (⟦SEAM55.md: level i (n levels, ℓ_n = ℓ_0); V = U_n the level-n (reference) field; u = local inverse coupling in "u-units"⟧); κ_W := d[u(1 + ϑ_1^p)]/du (a Ward coefficient, NOT κ_j); crossing weights ¼Σ_cβ_c (β_c the sphere's plaquette weights, u-units); Z_e; physical units | FL26, FL27, FL10 |
| B41 | ⟦PROOF.md: The local premise (R) — PROVEN as an implication⟧ | the local finite-word setup; Codex RLOC's R1 cylinder, R4 κ and R7 neighbourhood conventions — R4's κ is the soft coefficient κ_l (O3) with the dependence on κ_+ made explicit (⟦CODEX_REVIEW_RLOC.md: ### R4. HC's κ-independent sup is false, but local holomorphy has a direct repair⟧); K_1 (RLOC's local constant; printed value not certified); Convention C cutoffs (C3) | FL3 |

**Consequences for §4's verdicts.** B30 now reads "loses (R)": its premise list becomes the corrected contraction/linear
package (= §3's table), (GV), (EP) at zero weight, CD, H2W's local-torus inputs, Ward/CCP inputs and W8's prefactor. So §3's
premise set is now the **entire** remaining analytic premise set of BFT-4 (a) on 𝒞_glob, not only of K^{(σ)}/GV-E/BFT-E/NSL.
B37 names the FL13 bridge itself as its most dangerous item ("identifying global critical-value polymers with the
localised-minimiser densities") — that is E^cb versus the local E^min (𝓔^♭_k), in the centred polymer norm.

### 6.2 New objects and supplements to §2

- **O13 supplement — the data classes (PINNED from OFFGLOB55 §1, banked by CODEX_REVIEW_OFFGLOB item 1).**
  ⟦OFFGLOB55.md: 𝔅_k(ε) := {V : level-k links → SU(N) : d(V_P, 1) ≤ ε for every⟧ plaquette P} — REVIEW_S22's curvature-small class
  in the HS-geodesic distance; ⟦OFFGLOB55.md: saturation **𝒞*_glob(s) := ∪_g g·𝒞_glob(s) = {V : ∃ g with d((gV)_c, 1) ≤ s for every level-k link c}**⟧;
  the frame class 𝔑_k(R, α) with the two banked inclusions ⟦OFFGLOB55.md: factor 12(R′ − 1): "curvature-small" = "small in a local frame on every box of bounded size".**⟧;
  and the strictness ⟦OFFGLOB55.md: ### 1.5 Proposition C4 (𝒞*_glob is a strict subclass; the size gap is √ε) — PROVEN-HERE⟧.
  **Canonical reading of every banked "𝒞_glob" statement: on 𝒞*_glob(s)** (each 𝒞_glob theorem transports by a global gauge
  because 𝔉_k is gauge invariant; OFFGLOB55 §1). Relations: 𝒞*_glob(s) ⊂ 𝔅_k(4s) (four links per plaquette, HS triangle
  inequality); SRCCD55's op-norm 𝒮_K(ε) satisfies 𝔅_K(ε) ⊂ 𝒮_K(ε) ⊂ 𝔅_K(√N·ε).
- **O17 — "centred" is two words (DIFFERENT OBJECTS).** Convention C's centred POSITIONS (C3; B30) versus the CENTRED POLYMER
  NORM of HIST's induction, the value at the trivial field subtracted: ⟦CODEX_REVIEW_BFT4B.md: This norm is centered at the trivial field, which is **not fixed** by independent endpoint gauges.⟧
  (B37: averaging costs a factor ≤ 2 there, 1 in the uncentred norm).
- **O18 — W0, W1, W3, N5 name sphere-route items AND lane objects (DIFFERENT OBJECTS).** Sphere: ⟦SEAM55.md: **N5 (seam transparency, separated form).**⟧,
  ⟦SEAM55.md: ### 1.5 Theorem W0 (the Ward profile). CONDITIONAL on LCS-a; implication PROVEN-HERE⟧ (UNIV55/SPHERE55's Ward items
  W0-W3). Lane: BFT_A's Theorem W0 (LA32, ⟦BFT_A.md: - **Theorem W0 ((G♯_0-lev0) at m = 0, trivial background, Setting LIN).**⟧),
  BFT_A's Proposition W (LA13), and PROOF's per-step covariance node N5
  (⟦PROOF.md: Theorem N5-sf0 (N5 at small-field backgrounds for the level-0 fluctuation operator)⟧; ASSEMBLY55 N22, (N5-unif),
  eps_N5_unif). ASSEMBLY55 itself uses both "N5"s (N13 seam, N22 covariance) under one glyph.
- **κ_W** (B40, SEAM55): a Ward-profile coefficient; joins O3's list of κ's that are not κ_j.

### 6.3 New flags

**FL26 — "N5" names two nodes, both now in banked bullets. CONFIRMED (read).** B40's N5 is seam transparency (sphere);
PROOF's N5 is one-step fluctuation-covariance decay (N5-sf0, N5-sf_i, (N5-unif), eps_N5_unif, ε_* "N5 threshold"). A
consumer reading "N5 banked as a conditional implication" (B40) as progress on the covariance node would cross objects.
**Repair:** write N5^seam for the sphere item (SPHERE55/SEAM55/UNIV55/ASSEMBLY55 N13) and keep N5 for PROOF's node.

**FL27 — "W0" names the sphere's Ward profile and lane A's level-0 linear theorem. CONFIRMED (read).** B40's W0 versus LA32
(an input of (C2-COF), TOP-cc and CC-INV through Theorem COF). **Repair:** W0^Ward for the sphere item.

**FL28 — "centred". CONFIRMED (read); cosmetic but load-bearing for constants.** B30's "contour-CENTRED positions" (C3)
versus B37's "induction's centred norm" (O17). A threshold computed in one norm cannot be reused in the other: the averaging
factor is 1 uncentred and ≤ 2 centred (banked). **Repair:** say "Convention C" for positions and "centred polymer norm" for
D_X.

**FL7 update.** The banked inclusions (B38) settle the CLASS relations that FL7 left informal: 𝒞*_glob(s) ⊂ 𝔅_k(4s) and the
√ε gap make 𝒞_glob a strict subclass of BFT's target class 𝔅^ℂ_k at every small ε on large tori. FL7's interim restatement of
SRCCD55's 𝒮_K stands; its missing lemma (BFT off 𝒞*_glob) remains OPEN — B38 banks local components only ("Theorem OFF NOT
(GAP)").

**FL23 update.** B37 banks the averaging reduction (an invariant bounded holomorphic total on an invariant consumer domain can
be replaced by locally invariant pieces) but not the consumer closure (Theorem T0); FL23's missing lemma is now "an
invariant bounded holomorphic representation of the correct total on the correct invariant consumer domain, in the
centred norm" — exactly B37's stated GAP.

### 6.4 Errata to §3 (re-checked after §3 was appended; §3's text is not edited)

Re-reading the Codex reviews for each R1/S row (grep of every CODEX_REVIEW_* for the input's name, then the passage),
twelve classifications in §3 were too low. Each correction names the passage that re-derives (not merely cites) the input:
- **LA11 Lemma TS: R1 → R2.** Codex TOPCC re-derives the identification with the terminal-residual distinction
  (⟦CODEX_REVIEW_TOPCC.md: For a top link β, let Y^β be the zero-datum response to the top residual source δ_β. Lemma TS identifies its unknown components with those of the source-free minimizer y^β having datum δ_β/κ_(k−1). They differ in their last residual:⟧).
- **LA13 Proposition W: R1 → R2**, and **LA18 Proposition BL-4: R1 → R2** (BL-4's displayed bound is W at m = 0):
  ⟦CODEX_REVIEW_COFM.md: **Verdict: CONFIRMED that Proposition W supplies weighted BL-4, including the local Hölder step.**⟧
- **LA23 Corollary WR (a): R1 → R2.** ⟦CODEX_REVIEW_TR.md: writes the plaquette correction as an analytic map `Φ` with `DΦ(0)=0`. Translating the four links and using the ball's gradient bound gives⟧
  (also CODEX_REVIEW_HIGHER, "This extends the argument of `BFT_A.md`, `28.6 Corollary WR (a)`").
- **LA25 BA-6 / F6: R1 → R2.** ⟦CODEX_REVIEW_HIGHER.md: **CONFIRMED — exact quadratic commutator cancellation.**⟧ (CR-1/BA-6), with
  the all-order |ρ − r| bound of Codex HIGHER item 1.
- **LA26 BA-10: R1 → R2.** The holomorphy-by-uniform-analytic-iteration mechanism is re-derived at the K^{(σ)} level
  (⟦CODEX_REVIEW_KOFF.md: fixed local analytic extensions and the complexified fixed linear inverse⟧ give BFT-2) and in
  Codex SRCAN item 4 ("Uniform analytic iteration proves joint holomorphy").
- **LA28 Lemma DF-cc: R1 → R2.** Codex C2 §4 re-derives the corrected DF identities on strict plain-only sources
  (⟦CODEX_REVIEW_C2.md: It suffices to use COF's proof on a **strict plain-only** source. There the corrected DF identities are valid without the SPLIT mistake.⟧).
- **LA30 Theorem PW-cc: S → R1.** It is BFT_A's ⟦BFT_A.md: - **Theorem PW-cc (co-closed half of the dual (PW-i)).**⟧, confirmed by a
  pre-S24 lane review: ⟦REVIEW_BFT_A_S8.md: **S8-4 Theorem PW-cc (38.2, l.3481-3501): CONFIRMED, and uniform in k and T.**⟧. (§3 cited
  only its BFT_B mention.)
- **LA33 Theorem GU: R1 → R2.** Codex COFM item 1 re-derives GU_m's proof (i) for 0 ≤ m ≤ m_Y, which contains m = 0.
- **LA34: split.** Lemma TOPD **R2** (⟦CODEX_REVIEW_TOPCC.md: TOPD is symmetry of the Hessian tested on two actual critical points.⟧);
  Lemma LE stays R1.
- **LA35 Lemma Q-hold: R1 → R2.** ⟦CODEX_REVIEW_GSHARP.md: ### 2.4 Q-hold and the residual sum⟧ ("This proves Q-hold with a
  constant independent of b−a").
- **LA41 NSL55 Lemma A (c): S → R2.** The C^{2,α}-from-local-C^{1,α} control of Λ is re-derived in
  ⟦CODEX_REVIEW_GSHARP.md: Caccioppoli and LES-div thus control λ in `C^(2,α)` on the tent support by the local `C^(1,α)` norm of x_0.⟧;
  the pin/sup step is re-derived in Codex NSL F6 item 1. Codex NSL's own "NOT-VERIFIED independently here" refers to that
  review only.
- **LA15 Lemma LR-pot: stays R1, but leaves the premise set of the banked chain.** Codex GSHARP's independent reconstruction
  of EP-rec does not use it (⟦CODEX_REVIEW_GSHARP.md: This removes LR-pot, its constants `155,8,40`, and all data/residual estimates from this particular step.⟧);
  K^{(σ)} needs LR-pot only for potentials in Γ_tent, which is not the slice of Theorem BFT-E.

**Corrected counts (supersede §3's "What the table shows", items 1 and 3):** B = 8 (LA1-LA6, LA39, LA43); R2 = 18 (LA7-LA11,
LA13, LA18, LA22, LA23, LA25, LA26, LA27, LA28, LA33, LA35, LA38, LA41, LA42); R1 = 17 (LA12, LA14, LA15, LA16, LA17, LA19,
LA20, LA21, LA24, LA29, LA30, LA31, LA32, LA34 [LE part], LA36, LA37, LA40); S = 0. Check: 8 + 18 + 17 = 43. **Item 3 of §3 is
withdrawn: no input is "only stated".** The hidden premise set (inputs with no two-family re-derivation on disk) is the 17
R1 rows: FP, Lemma Λ, LR-pot (now off the banked chain), LIN0, CO-upR/RH, BL-2, BL-C, BL-5 (a), BA-3, COF-size, PW-cc, YH,
W0, LE, LES-div, LES/J-str/N2-lin, LINEAR_PACKAGE Thm 4.2(ii). Each is CONFIRMED in a pre-S24 lane review of unrecorded model;
none is refuted.

---

## §7. Upstream premises checked where a dependent banked estimate uses them (the commission's last clause)

"Verify actual upstream premises where a dependent estimate uses them — do not infer them from a banking label." For each
arrow I read the producer's statement and the consumer's use (both located above) and compare objects, norms, classes,
units and quantifiers. **MATCH** = identical in every respect; **MATCH-cond** = identical after a named conversion or under a
named side condition; **MISMATCH** = different (the flag that repairs it is named). Verdict on my comparison: CONFIRMED
where I read both ends; NOT-VERIFIED where one end was only quoted to me.

| # | Arrow (consumer ← producer) | Comparison | Result | Verdict |
|---|---|---|---|---|
| A1 | GV-E step 3 ← TOP-cc / CC-INV | consumer needs the N_Σ form; Codex TOPCC item 3 banks it ("also holds with N_Σ") | MATCH | CONFIRMED |
| A2 | K^{(σ)}'s TOP♯ ← Corollary FP | consumer: source-free tent-slice minimiser with datum δ_b/κ_{k−1}, weights centred at b, 0 < m_w < m_*′, T ≥ 3; FP: data + residual sources, S_tent, 0 ≤ m < m_*′, every centre X_0, T ≥ 3 through LR-pot; the datum's centred D-norm is 1/κ_{k−1} ≤ 1/κ_− | MATCH (FP itself R1) | CONFIRMED |
| A3 | Theorem BFT-E ← K^{(σ)} + GV-E | K^{(σ)} needs Γ with ΓΞ = −1 on Λ_* and (GV^{(σ)})_Γ in N^{(σ)}; GV-E gives it for Γ_E (T ≥ 5) and Γ^{(T)} (T = 3, 4) via N_Σ ≤ L·N^{(σ)} (θ₀ ≤ σ, no G above level 0) | MATCH | CONFIRMED (Codex GV items 2-4 agree) |
| A4 | NSL / Theorem ID ← BFT-E at every depth | depth-j problem = depth-"k := j" problem on coarse side T_j = TL^{k−j} ≥ 3, datum in one global gauge, same k-, T-free constants; NSL's pointwise norm ↔ BFT-E's Campanato norm via (1 + C_T) (C9) | MATCH-cond (C_0′ = (1 + C_T)C_0) | CONFIRMED |
| A5 | E1 ← BR1 (i)-(ii) | E1 is stated for odd L ≥ 3 inside ID's setting; BR1's proof contains an L = 3 specialisation (Codex NSL F8) and runs at κ_0 = 1 on PROOF's session-23 class with C_♭, C_Δ^{BR1}, r_♭ unevaluated (finiteness only) | MATCH-cond at L = 3 only | CONFIRMED (agrees with Codex NSL F8) |
| A6 | BFT3-glob ((H2)_μ, (H3)_μ) ← GV-E_m, Theorem H3 | (H2)_μ in COFM55's weights (Convention K positions, product form); H3 in BFT4W55's base-point weights with Convention C positions; weights differ by ≤ e^{2μ} and ≤ 1 + 4μe^{4μ}; (H3) is now unconditional on (R) (B41) | MATCH-cond (bounded constant factors, rates unchanged) | CONFIRMED |
| A7 | UIR55 (TC-b)_𝔍 orders 3, 4 ← BFT3-glob (E) at B = 0 (ASSEMBLY55 F23) | units: level-k ℓ¹ = level-lattice units (C2) ✓; rate: any 0 < m_0 < m/3 (Codex ASSEMBLY R3) ✓; normalisation: NM1-NM5 (O4) ✓; κ_j ≡ κ ✓; open: (GERM) beyond R6's finite chains, (JET-∞), and 𝒯_n → φ-tower (FL4) | MATCH-cond | CONFIRMED for the listed items; the open items NOT-VERIFIED |
| A8 | FLOW55's cubic tree jet of 𝒯_k ← (T-UNIF) / N1-15 | object D³𝔉_k(1)[ζ^c·, ζ^c·, ζ^c·] (FL1); NM3 factor N^{1/2} between HS and FLOW coordinates; k̃ and φ agree to order 5; NORMS's Q_str (FL15) does not affect the bound | MATCH-cond | CONFIRMED |
| A9 | SA-K ← K^{(σ)} / BFT-E setting | coefficient fields in ‖·‖_cf (with the ε_W / ε_S split, O14); Codex SRCAN item 4 requires G_cc read as the complex inverse norm | MATCH-cond | CONFIRMED |
| A10 | SRCCD55's SRC-κ on 𝒮_K ← BFT | 𝒮_K is an op-norm curvature class borrowing "BFT's ε_0"; BFT is banked on 𝒞*_glob with ε_0 bounding ‖B_k‖_D (FL7) | MISMATCH | CONFIRMED |
| A11 | HINT2_55's H-RED: Yang–Mills TS bounds ↔ comparator A_∞ | TS bounds in canonical g; A_∞ multiplies g_std² = 2N·g²; HINT55 converts explicitly (FL10) | MATCH-cond | CONFIRMED |
| A12 | REVIEW_S22 BFT-4 consumers (C_♭^{(k)}, (H-G), C_θ by Cauchy) ← BFT-4 (a) | consumed on "the BFT-2 polydisc in curvature-adapted coordinates", curvature-small class; produced on PD-glob, 𝒞*_glob (FL22, FL7) | MISMATCH | CONFIRMED |
| A13 | HIST (I_k^E)″ polymers (centred norm, invariant) ← BFT-4 (b) averaging (B37) | the averaging reduction preserves invariance with factor ≤ 2 in the centred norm; the identification of critical-value polymers with localised-minimiser densities is B37's stated GAP (FL13, FL23, FL28) | MATCH-cond on the reduction; MISMATCH on the identification | CONFIRMED |
| A14 | SF (BG-unif), PROOF (H-C⁺)/(H-ℂ) ← BFT-E / ID | per-level E^br on a level-uniform curvature class ← E^cb on 𝒞*_glob (FL14, FL7) | MISMATCH | CONFIRMED (agrees with Codex ASSEMBLY R7) |

---

## §8. Second errata round (append-only; supersedes §6.4's counts where they differ), one new flag, one precision

### 8.1 Four more §3 rows are banked or re-derived than §6.4 recorded
Re-reading the banked bullets' cited Codex items (not only the bullet text) shows that some lane-A inputs are themselves
inside a banked Codex item. B12 banks "COFM55 + CODEX_REVIEW_COFM items 1-4" — item 1 contains GU_m for 0 ≤ m ≤ m_Y
(⟦CODEX_REVIEW_COFM.md: 1. **CONFIRMED:** Lemma K,⟧ "… and GU_m (i)/(iii)"), item 2 contains COF_m (⟦CODEX_REVIEW_COFM.md: 2. **CONFIRMED:** COF_m under (CC-0), and, after DEC, CC-FUN_m (a), (b) and (c) for every stated composite-co-closed source S with B_k = 0:⟧),
item 4 contains Proposition W (⟦CODEX_REVIEW_COFM.md: 4. **CONFIRMED inputs and bookkeeping:** Lipschitz-weighted QH_m; Proposition W as weighted BL-4;⟧).
Their m = 0 cases are Theorem GU, Theorem COF and (through W at m = 0) Proposition BL-4's displayed bound. Further Codex
re-derivations located: Lemma Λ's root-line-sum content (⟦CODEX_REVIEW_GSHARP.md: Let `H_i(Y,ν)` be the integral of x_0 along the straight fine path between adjacent level-i roots.⟧, inside the banked reconstruction),
and BL-C's mechanism with its constant C_C (⟦CODEX_REVIEW_RLOC.md: Rebuild LBC: two successive dyadic means differ by at most `4 Osc_2` on the larger box in four dimensions.⟧).

**Final classification of §3's 43 rows (supersedes §3 items 1-3 and §6.4's counts):**
- **B = 12:** LA1-LA6, LA13 (W), LA18 (BL-4, as W at m = 0), LA27 (COF), LA33 (GU), LA39, LA43.
- **R2 = 16:** LA7-LA11, LA14 (Lemma Λ), LA20 (BL-C), LA22, LA23, LA25, LA26, LA28, LA35, LA38, LA41, LA42.
- **R1 = 15:** LA12 (FP), LA15 (LR-pot — off the banked chain, §6.4), LA16 (LIN0), LA17 (CO-upR/RH), LA19 (BL-2), LA21 (BL-5 (a)),
  LA24 (BA-3), LA29 (COF-size), LA30 (PW-cc), LA31 (YH), LA32 (W0), LA34 (LE; TOPD is R2), LA36 (LES-div), LA37 (LES/J-str/N2-lin),
  LA40 (LINEAR_PACKAGE Thm 4.2(ii)).
- **S = 0.** Check: 12 + 16 + 15 = 43.
**The hidden premise set** of [S26-BANKED]'s K^{(σ)}, GV-E, BFT-E, NSL, TOP-cc, (C2-COF) — and now also BFT-4 (a), whose only
remaining premises are this package and the items B41 lists — is the 15 R1 rows: inputs CONFIRMED only in pre-S24 lane
reviews of unrecorded model, never re-derived by Codex or by an Opus 5.5 file. Of these, LIN0, FP, BA-3, LES-div, W0, YH,
BL-2, BL-5 (a), COF-size, PW-cc, LE, CO-upR/RH and the LINEAR_PACKAGE items are load-bearing in the banked chain; LR-pot is not
(on the S_E route). None is refuted.

### 8.2 FL29 — the BCH coefficient "9" in BA-3 / BFT-1 (1a) / WR (a) is not certified; two banked bullets disagree. CONFIRMED (arithmetic re-done).
BA-3 bounds the plaquette BCH remainder by 9s_j² with s_j the maximal LINK size (BFT_A §3.3), giving BFT-1's displayed
(1a) bound (⟦KFACTOR_OFF55.md: (1a) own plaquette logs of e^{x_j} ≤ L^{−2(k−j)}(2η + 9η²) (BA-3; θ_w^c = 2, the maximum, NORMS "There is NO slack in the⟧),
reprinted in GV55's Theorem BFT-E display that Codex GV item 4 banks ("the displayed (2,2+σ,1) regularity estimates"). Codex
RLOC R11 (⟦CODEX_REVIEW_RLOC.md: ### R11. The Wilson citation changes the meaning of s and loses a factor sixteen⟧) shows the
cited elementary estimate is in total-word units, so for four links ⟦CODEX_REVIEW_RLOC.md: |q_p|≤9(Σ_{i=1}^4|x_i|)²≤9(4s_j)²=144s_j²⟧,
and B41's banked text records "the cited BCH argument gives 144, not 9". I re-did the arithmetic: (Σ_{i≤4}|x_i|)² ≤ 16s_j², and
9·16 = 144. **So B41 (banked) and B10/B18's displayed BFT-1 constant (banked) disagree.** Consequence: constants only — every
uniformity statement survives (144 is as k-, T-free as 9); no numerical threshold in the banked block uses the 9 (K^{(σ)}'s
ε_0 is not evaluated). **Repair (restatement):** in BA-3, Corollary WR (a) ("‖q^c‖_∞ ≤ 9η²") and every BFT-1 (1a) display,
write C_q′η² with C_q′ := 144 certified by the cited argument (or re-derive 9 on a smaller neighbourhood, which R11 says is
not excluded). Downstream constants that absorbed the 9 (K^{(σ)}'s K_rows, "9 + 4C_q + …") change by a fixed factor.

### 8.3 Precision to ASSEMBLY55 §1.1 ("There are THREE objects, not two")
ASSEMBLY55 lists FLOW's 𝒯_k and HIST's 𝓔_k as instances of one E^min. For N ≥ 3 they are different functions (Lemma HF:
k̃ = φ + d(M), 𝒯_k ≥ 𝓔_k, equality for N = 2; banked FLOW55 item 2), with the same jets of order ≤ 5 at V = 1. ASSEMBLY55's C5a
already records that the k̃-tower "must be the φ-tower for N ≥ 3", so this is a **precision, not a refutation**: read
ASSEMBLY55's E^min as 𝓔_k (φ); FLOW's literal 𝒯_k is a fourth object until FL4's restatement is applied.

### 8.4 Precision to ASSEMBLY55 N24 ("inherited, NOT-VERIFIED at the S26 two-family standard")
For the inputs N24 names, the classification is now: LP Thm 4.2(ii), LES-div, LR-pot, W0, Lemma Λ (R2), BL-5 — not two-family;
**GU, BL-4 (via W) — banked (B12); Q-hold, CR-1 (Codex HIGHER item 3), WR (a) — re-derived by Codex (R2).** So N24's blanket
label is **REFUTED as a blanket statement** (scoped: five of its named items are banked or Codex-re-derived); it remains
correct for the R1 rows of 8.1. N24 is not in [S26-BANKED], so this changes no banked text.

---

## §9. Check record (criteria before scripts; exact arithmetic; no floats)

- **dc55_1 (locator audit).** checks/dc55_1_criteria.md born 05:16:48Z (stat), before the script checks/dc55_1_locators.py
  (born 05:18:46Z). The script extracts every locator of the form FILE: string between white square brackets, writes them
  to checks/dc55_1_locators.tsv, and requires each string to be a substring of one line of its file (UTF-8, exact).
  **Could it fail? Yes, and it did, repeatedly, before each section was appended:** §1's draft failed 24 locators (my own line
  wraps inside locators) plus one malformed bracket; §2's draft failed one (a locator that started mid-line); §5's draft failed
  one twice — the second time because the file writes Ñ as N + U+0303 (combining tilde) while I typed U+00D1; §6's draft failed
  one (a capital letter the file does not have). Each failure was fixed in the scratch draft before appending; nothing in this
  file was appended with a failing locator. Controls: C1 (string + a fixed non-occurring suffix must not be found) fired on
  every row; C3 (a non-existent file must be reported, not passed) fired. **Final run on this file:** see checks/dc55_1_out.txt
  — run at 05:49:36Z on DICT55.md through §8: 367 locators in 61 files, 0 missing, 0 malformed, C1 0 false finds, C3 fired,
  C2 (also present in HANDOFF.md, informational) 0. **VERDICT: PASS.** Sections §9-§12 contain no locators, so that run
  covers every locator in the file. Scope (as pre-registered): PASS shows the strings exist; that each string denotes the
  object claimed is the reading the entries themselves state.
- **dc55_2 (gauge-action composition and cocycle order).** checks/dc55_2_criteria.md born 05:16:48Z, AMENDMENT 1 at 05:17:19Z
  (before any script: the original K3 control used a V-independent ĥ and could not fire; replaced by a non-equivariant
  map X(V) = VMV, which makes ĥ depend on V). Script checks/dc55_2_gauge.py and outputs born 05:17:36Z. Exact Fractions on
  26 random/hand-chosen GL(2, Q) instances: (L) left action (U^g)^{g′} = U^{g′g} on all; (R) right action (U^g)^{g′} = U^{gg′} on
  all; K1 and K2 (the opposite laws) fail somewhere; left-order cocycle holds and the right order fails somewhere (K3a);
  symmetrically for the right model (K3b). **VERDICT: PASS** (checks/dc55_2_out.txt; checks/dc55_2_err.txt empty). Scope: group
  algebra only; it decides C4's composition and cocycle-order claims, nothing about any Yang–Mills estimate.
- **Hand arithmetic used for a verdict (exact):** FL29: (Σ_{i≤4}|x_i|)² ≤ (4s_j)² = 16s_j², 9·16 = 144. FL10: A_∞g_std² =
  A_∞·2N·g² = 3(N²−1)·2N/(128π²)·g² = 3N(N²−1)g²/(64π²). NM3: F = N·(F/N) and y = √N·B give D^n_yF = N·N^{−n/2}D^n_B(F/N) =
  N^{1−n/2}D^n_B(F/N). §8.1 counts: 12 + 16 + 15 = 43.

---

## §10. Codex verdicts used — agree or disagree, explicitly (each read as on disk at 04:58-05:49 UTC; all complete)

- **CODEX_REVIEW_ASSEMBLY** (final checkpoint 04:48:14Z; complete): item 3 of its work list is this commission — agree it is a
  prerequisite. R3 (kernel-to-row-sum, F23 only conditional; the c_T volume counterexample) — agree. R6 (finite-chain germ;
  quartic exchange term −3⟨c, H⁻¹c⟩) — agree; FL1 uses it. R7 (the E^br/E^cb contract distinction is real; the cost-free
  repair is NOT-VERIFIED) — agree; FL14. R11 (constant vs local gauge invariance; classical vs quantum) — agree; FL23. Its
  summary rows F9, F12, F15, F16, F22 ("NOT-VERIFIED cross-file identifications") — agree as of its read; this file supplies
  F9 (C3), F12 (O8/FL2), F15 (O14/FL8) and F22 (O2/FL4) at dictionary level; **F16 (plaquette vs clover witness density) is not
  addressed here**.
- **CODEX_REVIEW_NSL**: F3 (Lemma SC's 84 > 81, repaired), F5 (𝒢^{rt}_j is not the whole fixed-datum symmetry group), F6-F7
  (NSL, K-U, ID conditional), F8 (E1/E-ind conditional; no uniform bridge), F9 (C_Λ, C_Δ, R_0 pins) — agree with all. Its
  summary row "Lemma A elliptic estimate: NOT-VERIFIED independently here" — agree as a statement about that review; the
  estimate is re-derived in CODEX_REVIEW_GSHARP §2.5 (so the input is R2 across reviews, §6.4).
- **CODEX_REVIEW_KOFF**: §5.1's list of named lane-A inputs and "they do not independently certify that entire package" —
  agree; (LA-1) refuted → (LA-1′) — agree (GV55 checked the same); banked items 1-7 — agree.
- **CODEX_REVIEW_GV** items 1-6 — agree (norm witness, GV-E, slice identity and T = 3, 4 sign, BFT-E with E^cb not E^br,
  restriction failure −640/19683, GV-E_m).
- **CODEX_REVIEW_GSHARP** items 1-5 and §2.2, §2.4, §2.5 — agree; the independent reconstruction removing LR-pot is what moves
  LR-pot off the banked chain (§6.4).
- **CODEX_REVIEW_BFT4W** W3 (CORNER) and banking items 1-5 — agree.
- **CODEX_REVIEW_FLOW55** §1.2 and item 2 (literal k̃ refuted for N ≥ 3; φ-tower; jets agree) — agree.
- **CODEX_REVIEW_UIR** symbol pins (β_0^std in u-units ≠ b_0) and banking items — agree.
- **CODEX_REVIEW_SRCAN** items 4, 7, 13 — agree (sup-plus-Wilson-Hölder class; necessity of the Hölder class not banked; the
  R collision and ε_W/ε_S split).
- **CODEX_REVIEW_BALX** F2, F11 — agree (fixed radii vs coupling-dependent cuts; Dimock's k vs PROOF's resolution j).
- **CODEX_REVIEW_C2** item 1 and §4's dependency sentence — agree (C2's N = N_Σ; COF's quoted inputs).
- **CODEX_REVIEW_TOPCC** item 3 (N_Σ form) and its TS/TOPD derivations — agree.
- **CODEX_REVIEW_TR** §2 (RT-cc, TC, FT re-derived) and item 3 (m is the depth) — agree.
- **CODEX_REVIEW_COFM** items 1, 2, 4 and §5 — agree (GU_m, COF_m, Proposition W as weighted BL-4).
- **CODEX_REVIEW_HIGHER** items 1, 3 and the commutator cancellation — agree.
- **CODEX_REVIEW_RLOC** R4 (κ_+ explicit), R5 (LBC rebuilt), R11 (9 → 144 under the cited argument; sharper 9 NOT-VERIFIED) —
  agree; FL29 adds that this contradicts the banked BFT-1 (1a) display.
- **CODEX_REVIEW_OFFGLOB** item 1 (class inclusions, C4's √ε witness) — agree with the statements (I read OFFGLOB55 §1.3, §1.5;
  I did not re-derive C4's witness).
- **CODEX_REVIEW_BFT4B** items 1-2 (uncentred factor 1, centred factor ≤ 2) — agree with the pins (did not re-derive the SU(2)
  counterexample).
- **CODEX_REVIEW_SEAM, CODEX_REVIEW_LARGE, CODEX_REVIEW_NRES, CODEX_REVIEW_KN, CODEX_REVIEW_SYMBOLS, CODEX_REVIEW_X1,
  CODEX_REVIEW_TUNIF2, CODEX_REVIEW_P4, CODEX_REVIEW_DAG, CODEX_REVIEW_ROTDEF, CODEX_REVIEW_HINT, CODEX_REVIEW_HINT2,
  CODEX_REVIEW_SPHERE, CODEX_REVIEW_ALIGN, CODEX_REVIEW_BGT, CODEX_REVIEW_TQ, CODEX_REVIEW_SRCCD, CODEX_REVIEW_BFT34,
  CODEX_REVIEW_UNIV, CODEX_REVIEW_RLU, CODEX_REVIEW_NODEA, CODEX_REVIEW_LCONV**: used only for the objects their banked scopes
  are stated in (§4, §6.1); no disagreement found with any statement used. CODEX_REVIEW_SYMBOLS F9's "κ: ≥ 5 roles" — agree,
  and §2 O3 adds a sixth κ_0 reading (the level-0 kernel coefficient).
- **Disagreements: none.** One qualification: no Codex review pins the HS-vs-normalised-Lie coordinate factor √N or the
  𝔉_k = N·E(chain) normalisation (NM1-NM5); these are supplied here, not checked by Codex.

---

## §11. Summary table — every claim of this file with its verdict

Verdict words: CONFIRMED = read at source (and, where stated, re-derived); NOT-VERIFIED = could not settle (what is missing
is named in the entry); REFUTED = shown wrong (correction given). PINNED/MAPPED/DIFFERENT OBJECT entries are CONFIRMED readings.

| # | Claim (section) | Verdict |
|---|---|---|
| 1 | C1 level index, depth; PROOF's resolution runs the other way; "m" as a depth in KFACTOR_OFF55 | CONFIRMED |
| 2 | C2 coarse/own/physical units; ℓ¹ distance of coarse positions; ℓ^∞ only for Hölder pairs and box radii | CONFIRMED |
| 3 | C3 Convention C canonical; Convention K differs only for cutoffs/commutators at σ > 0 (weights: factor e^{2μ}) | CONFIRMED |
| 4 | C3 S4′ (order-paired) ≠ Balaban's (0.4) beyond linear order | CONFIRMED |
| 5 | C3 KN_ADOPT's paired indexed mean = the live S4′ coarse link (Codex KN's open item) | NOT-VERIFIED (not re-checked here) |
| 6 | C4 left action canonical, (U^a)^b = U^{ba}; two right-action passages in BFT_B (§13.3, §12.2 cocycle print) | CONFIRMED (dc55_2) |
| 7 | C5 HS norm canonical; FLOW coordinates y = √N·B; op-norm classes | CONFIRMED |
| 8 | C6 canonical u = 1/g² = β_Wilson = 2N/g_std²; files on standard g listed | CONFIRMED |
| 9 | C6 which g PROOF's Decision-4 "κ/g²" means | NOT-VERIFIED (unfixed in PROOF; consumers read canonical) |
| 10 | C7 S_W = N·Σ_p s(U_p); bare weight e^{−u_0Σs} | CONFIRMED |
| 11 | C8 Decision-4, RLARGE and FLOW kernels are one kernel | CONFIRMED |
| 12 | C9 Campanato vs pointwise conversions (BL-C; 1 + C_T) | CONFIRMED |
| 13 | C10 weight w = e^{m d}; μ = m; rates m, m_0 (two), m_c, m_*′ distinct | CONFIRMED |
| 14 | O1 Q_root canonical; Q_str two operators; h_l two operators | CONFIRMED (Q_str's 108-entry count is REVIEW55_NORMS's, not re-run) |
| 15 | O2 φ canonical, φ̂ = Nφ, k̃ = φ + d(M) | CONFIRMED |
| 16 | O3 κ_j canonical = uniform κ of HIST/FLOW/RLARGE; E_NA's κ_i = Nκ_j at g = 1; fine-unit κ's; a fourth κ_0 | CONFIRMED |
| 17 | O4 𝔉_k and NM1-NM5 (𝔉_k ≡ N·E(chain); D^n_yF = N^{1−n/2}D^n_B(F/N); coupling u/N; (J1) in both normalisations) | CONFIRMED (derived, exact) |
| 18 | O5 four towers E^br, E^cb, E^min = 𝓔_k, 𝒯_k; aliases "E_k^br" = E^cb in BFT34_55/BFT4W55/SRCCD55; bridges E1, E-ind, R6 | CONFIRMED |
| 19 | O6 critical points and backgrounds | CONFIRMED |
| 20 | O7 Ξ, K_0 = −Ξ; Λ_0 is two spaces; 𝒢^{rt}_j; (GI) | CONFIRMED |
| 21 | O8 S_E = Ker Γ_E (Γ_E = Λ = Λ_E); Γ^{(T)}; depth slices not nested; per-level slices distinct; orbit norm | CONFIRMED |
| 22 | O9 cc ⟺ D^⊥(S) = 0 ⟺ Ξ^TS = 0 on Λ_0; level-wise co-closed ⊂ (CC-0) ⊂ cc | CONFIRMED |
| 23 | O10 𝔐^∇, 𝔐^{(σ)}, three "𝔐-pairs", ‖·‖_inv, ‖·‖_♮ | CONFIRMED |
| 24 | O11 N(S), N_Σ(S), N^{(σ)}(S) (+ weighted); Codex C2's N = N_Σ | CONFIRMED |
| 25 | O12 weight triple (2, 2+σ, 1); θ class exponent; θ₀; σ; α windows | CONFIRMED |
| 26 | O13 + §6.2 data classes 𝒞_glob, 𝒞*_glob, 𝔅_k, 𝔑_k, PD-glob, 𝒮_K, χ_Q; inclusions | CONFIRMED |
| 27 | O14 ‖·‖_cf (sup + Wilson Hölder); ε̂_0 two slots; sup ball consumed by SRCCD55 | CONFIRMED |
| 28 | O15 thresholds ε_0, r_u, ε_u, ε_ID, ε_E1; fixed radii vs coupling-dependent cuts | CONFIRMED |
| 29 | O16 e_a, O_a(f), 𝓔 = t²E; R glyph | CONFIRMED |
| 30 | O17 "centred" (positions vs polymer norm) | CONFIRMED |
| 31 | O18 W0, N5 name sphere items and lane objects | CONFIRMED |
| 32 | D2 final classification of the lane-A inputs (§8.1 + LA44 below): B 12, R2 17, R1 15 | CONFIRMED (classification; the inputs' mathematics is not re-derived here) |
| 33 | §3's first classification (S rows; counts) | WITHDRAWN by this file (§6.4, §8.1) — not counted |
| 34 | ASSEMBLY55 N24's blanket "inherited, NOT-VERIFIED at the S26 two-family standard" | REFUTED as a blanket label (GU, BL-4 via W banked; Q-hold, CR-1, WR (a) Codex-re-derived) |
| 35 | D3 matrix B1-B41: objects each bullet is stated in | CONFIRMED |
| 36 | Convention-clean bullets: B4, B5, B20, B22, B27 | CONFIRMED |
| 37 | FL1 "E_k^br" two objects; jets sound via TOWER-VAR (d) + R6 | CONFIRMED |
| 38 | FL2 per-level slice vs S_E | CONFIRMED |
| 39 | FL3 lower-corner vs centred | CONFIRMED |
| 40 | FL4 φ vs k̃ off the trivial point | CONFIRMED |
| 41 | FL5 𝔉_k vs stripped-tower normalisation (resolved by NM) | CONFIRMED |
| 42 | FL6 N(S) vs N_Σ vs N^{(σ)}; B6 should print the N_Σ form | CONFIRMED |
| 43 | FL7 ε_0 for two classes; SRC on 𝒮_K crosses 𝒞*_glob → curvature class | CONFIRMED |
| 44 | FL8 sup ball vs ‖·‖_cf (difference) | CONFIRMED |
| 45 | FL8 the sup ball is genuinely insufficient | NOT-VERIFIED (ARGUED in SRCAN55; not banked) |
| 46 | FL9 units for rates: no silent conversion found | CONFIRMED |
| 47 | FL10 two coupling normalisations among banked items; no live numeric error | CONFIRMED |
| 48 | FL11 Λ_0 two spaces | CONFIRMED |
| 49 | FL12 left vs right action | CONFIRMED |
| 50 | FL13 E^min two functions for N ≥ 3 | CONFIRMED |
| 51 | FL14 per-level E^br consumers vs E^cb producers (distinction) | CONFIRMED |
| 52 | FL14 the convention repair is cost-free | NOT-VERIFIED (line-by-line consumer audit missing; agrees with Codex ASSEMBLY R7) |
| 53 | FL15 Q_str in NORMS vs LINEAR_PACKAGE | CONFIRMED |
| 54 | FL16 "m" depth in B7 vs weight in B12/B26/B35 | CONFIRMED |
| 55 | FL17 C_Λ in B28 is NSL's Lemma A (c) constant | CONFIRMED |
| 56 | FL18 κ_0 in B28 vs Theorem CE's κ_0 | CONFIRMED |
| 57 | FL19 R glyph (R_W, R_F, radius, torus side) | CONFIRMED |
| 58 | FL20 θ in B15 is RLARGE's large-field fraction | CONFIRMED |
| 59 | FL21 β in B36 is a stripe amplitude | CONFIRMED |
| 60 | FL22 four polydiscs; BFT-4 Cauchy consumers on curvature-adapted coordinates | CONFIRMED |
| 61 | FL23 constant vs local gauge invariance of BFT-4's pieces | CONFIRMED |
| 62 | FL24 Campanato vs pointwise constants handled explicitly | CONFIRMED |
| 63 | FL25 h_l two operators, no dependent step | CONFIRMED |
| 64 | FL26 N5 (seam) vs N5 (covariance node) | CONFIRMED |
| 65 | FL27 W0 (Ward) vs Theorem W0 (lane A) | CONFIRMED |
| 66 | FL28 "centred" positions vs centred polymer norm | CONFIRMED |
| 67 | FL29 BA-3's "|q_p| ≤ 9s_j²" as justified by the cited estimate | REFUTED (the cited estimate gives 144s_j²; agrees with Codex RLOC R11) |
| 68 | FL29 a sharper coefficient 9 on a smaller neighbourhood | NOT-VERIFIED |
| 69-82 | A1-A14 premise comparisons (results: A1, A2, A3 MATCH; A4-A9, A11, A13 (reduction) MATCH-cond; A10, A12, A14, A13 (identification) MISMATCH) | CONFIRMED (14 comparisons) |
| 83 | A7's open items: (GERM) beyond finite chains, (JET-∞), 𝒯_n → φ-tower | NOT-VERIFIED (OPEN) |
| 84 | §8.3 ASSEMBLY55 §1.1's E^min reads as 𝓔_k (precision) | CONFIRMED |
| 85 | dc55_1 locator audit | PASS (367/367; controls fired) |
| 86 | dc55_2 gauge-action composition and cocycle order | PASS (all controls fired) |

**Counts (rows 1-84; rows 69-82 counted as 14):** CONFIRMED **75**, NOT-VERIFIED **7** (rows 5, 9, 45, 52, 68, 83 and — counted
once — none further), REFUTED **2** (rows 34, 67); one self-withdrawal (row 33); two checks PASS.

---

## §12. For the lead (nothing here is banked; the lead edits), and final errata

### 12.1 What should change in PROOF.md's tally and in HANDOFF's critical path
- **Tally: no change.** This file is bookkeeping; it moves none of the 105 items.
- **Restatements of [S26-BANKED] text (bookkeeping, no new mathematics):** B6 — add "and with N_Σ(S) (CODEX_REVIEW_TOPCC
  item 3)" (FL6); B7 — write q := k − 1 − l in "π_l ≤ A_Bκ̂L^{−q}" (FL16); B26, B30 — write E^cb ("composite critical value")
  for "E_k^br" (FL1); B28 — "C_N = 4 + 3C_Λ^{(A)}" with C_Λ^{(A)} := NSL55 Lemma A (c)'s constant (not Lemma Λ's 10), and κ_0^{ker}
  (FL17, FL18); B10/B18's BFT-1 (1a) display versus B41 — replace the BCH coefficient 9 by a certified constant (144 from the
  cited argument) or re-derive 9 (FL29); B30's rate — R_W (walk box), B15/B16/B25/B31 — R_F (FL19); B40 — N5^seam, W0^Ward
  (FL26, FL27); B15 — θ_LF (FL20); B36 — β_str (FL21); B37 — "centred polymer norm" (FL28); and one sentence above the block:
  "every 𝒞_glob statement holds on its gauge saturation 𝒞*_glob(s)" (§6.2).
- **Restatements in consumer files (bookkeeping; each named with its flag):** SF (a5-G♯)/(MIN-reg) and RTARGET (G♯_0-field) in
  S_E or the orbit norm (FL2); Convention C binding for every cutoff multiplier/commutator at σ > 0, lane B §10 included (FL3);
  FLOW Def F-strip and FLOW55 §3.4's Õ_k with φ, and −κu·d(M) moved into log 𝒩′ (FL4); SRCCD55's 𝒮_K stated as 𝒞*_glob(ε_0) at
  level K until BFT holds off 𝒞*_glob (FL7); SRC's coefficient class in ‖·‖_cf with the ε_W/ε_S split (FL8); PROOF Decision 4's
  "g" declared canonical (C6, FL10); Λ_* wherever the vanishing space is meant (FL11); the (CovLift) cocycle in RS7-8's left
  order (FL12); NORMS §N1's Q_str := LINEAR_PACKAGE's (FL15); SF (BG-unif) and PROOF (H-C⁺)/(H-ℂ) in Balaban's convention
  (FL14).
- **Missing lemmas this dictionary exposes (all OPEN; none new to the lane, each now pinned to its objects):** BFT-0…4 off
  𝒞*_glob, on 𝔅_k and on local small-field regions (FL7, FL22; B38's Theorem OFF GAP); (GERM) beyond R6's finite chains and
  (JET-∞) (FL5, A7); (MIN-cb) or the critical-value restatement for 𝓔_k (FL13); BFT-4 (b)'s consumer closure T0 (FL23, B37);
  the line-by-line audit of E^br consumers (FL14).
- **HANDOFF critical path:** item 3 of CODEX_REVIEW_ASSEMBLY's ordered list ("Pin the source dictionaries …") can be marked
  "dictionary written (DICT55); restatements listed in DICT55 §12.1 pending; missing lemmas unchanged". The one dictionary
  finding that changes a banked display is FL29 (constant only). The cheapest step toward a fully two-family BFT chain is a
  re-derivation of the 15 R1 inputs of §8.1 — load-bearing on the S_E route: LIN0, FP, BA-3 (with FL29), LES-div, W0, YH,
  BL-2, BL-5 (a), COF-size, PW-cc, LE, CO-upR/RH and the LINEAR_PACKAGE items (LR-pot is off that route).
- **Single most dangerous dictionary item:** FL7 — every banked BFT statement is about 𝒞*_glob, while SRC, SF, RLARGE, HIST and
  REVIEW_S22's BFT-4 Cauchy consumers read the curvature class 𝔅_k or local regions; the inclusion runs one way only (√ε gap).

### 12.2 Final errata (append-only)
- **E1 (§11 counts).** NOT-VERIFIED is **6**, not 7 (rows 5, 9, 45, 52, 68, 83). Final counts: **CONFIRMED 75, NOT-VERIFIED 6,
  REFUTED 2**, one self-withdrawal, two checks PASS.
- **E2 (§11 row 67 rendering).** The row's claim text contains vertical bars; read it as: "FL29 — BA-3's bound q_p ≤ 9s_j² (in
  norm) as justified by the cited estimate — REFUTED (the cited estimate gives 144s_j²)".
- **E3 (§9 description of §6's failed locator).** The failing KOFF locator began with "The", which sits on the PREVIOUS line of
  CODEX_REVIEW_KOFF (a line break), not a capital letter the file lacks. The fix was the same (start the locator at "fixed").
- **E4 (D2 completeness).** GV55 §3.2 row 5 also names Lemma CR-1 (BFT_A §13.5; the commutator row is residual type). Add
  **LA44 Lemma CR-1 — class R2** (pre-S24 REVIEW_BFT_A_S3; re-derived as the exact quadratic commutator cancellation in
  CODEX_REVIEW_HIGHER, banked context B17). Final D2 counts over 44 rows: **B 12, R2 17, R1 15**.

UTC end: see the last `date -u` of the session record below.
UTC end (date -u): 2026-10-29T05:52:25Z
- **E5 (§9 run time).** checks/dc55_1_out.txt records the final re-run at 05:52:31Z over the complete file (after §12): 367 locators in 61 files, 0 missing, controls fired, PASS — identical counts to the 05:49:36Z run quoted in §9. PROOF.md's [S26-BANKED] block was last modified at 05:25:45Z (44 bullet lines incl. 3 batch headers, i.e. B1-B41) when this file was closed.
