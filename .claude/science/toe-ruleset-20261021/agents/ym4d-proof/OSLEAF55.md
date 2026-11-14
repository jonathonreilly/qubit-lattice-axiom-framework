Reviewer model: claude-opus-5-5

# OSLEAF55 — the assembly-level glue leaves ML2 (REC), ML1 (ALG, minus the witness), ML3 (DIAG), ML9 (EXT), ML12 (TRAJ)

**Current reconstruction-consumer scope.** The source corrections recorded in
[rec_consumer_alignment_note.md](checks/rec_consumer_alignment_note.md) apply the reviewed REC_LIB + REC_CONT abstract
contract. They are new authorship pending a different fresh reviewer; the original author record and historical reviews
remain separate. Full four-dimensional Yang–Mills existence **and** a physical continuum mass gap remain OPEN. A scalar
OS theory or a fixed finite Cartesian tensor family is an intermediate construction, not a redefinition of that target.

UTC start: 2026-10-29T04:35:16Z
Author role: Opus 5.5 worker (brief: scratchpad/queue/osleaf.md; shared rules: scratchpad/REVIEW_BRIEF_55.md).
Writes: this file and checks/ol55_* only. No git. Append-only.

## PRE-STATED (written before any derivation; statements only)

Inputs read before this block (reading only, no derivation): the brief; REVIEW_BRIEF_55; ASSEMBLY55 (all of §1-§14);
CODEX_REVIEW_ASSEMBLY as on disk at ≈04:30Z (R1-R5 written, "Review in progress"); NONFREE55 (PRE-STATED only at ≈04:30Z);
HANDOFF; PANEL_P1 §1-§3, §7-§8; SRCCD55 §2.2-§2.3 (OS0 reading, Lemma V).

Targets (each to be closed as a theorem with a complete proof, or reported NOT-VERIFIED with what is missing).
- **T-REC (ML2).** State the reconstruction theorem in the exact form the assembly invokes, for a finite family of real
  gauge-invariant composite scalar/tensor fields whose Schwinger functions are given only as distributions on OS's space of
  test functions vanishing with all derivatives on the coincidence set (^0𝒮), with OS II's linear growth condition (E0′).
  Re-derive here, with complete proofs: (i) the OS form and its positivity on the time-ordered positive-time test algebra,
  noting exactly which test functions the form evaluates; (ii) the quotient/completion Hilbert space and the vacuum;
  (iii) the time-translation contraction semigroup e^{−tH}, H ≥ 0 self-adjoint (including the boundedness step and the
  growth bound it consumes); (iv) the spatial Euclidean unitary representation; (v) the field operators that can be built
  from separated distributions alone, and what (E0′) adds (analytic continuation to tempered Wightman distributions).
  Mark [m] every statement about OS I/OS II (or any other source) I cannot check against a primary or open-access text.
  Prove a lemma: SRC-κ-type bounds (pointwise separated n-point bounds with power singularities δ^{−p_n}, p_n ≤ p·n, and
  factorial growth C_0^n(n!)^p, uniformly in a and R) imply the growth condition in the form stated, with explicit order s
  and exponent β, and the bound passes to subsequential limits. Answer CODEX_REVIEW_ASSEMBLY R1 (the e(f)² example).
- **T-ALG (ML1 minus the witness).** Define one algebra 𝒜 (the OS test algebra over a named finite field family), its
  E(4) action, its positive-half generating set for RP, and a countable determining family for OS0; prove that convergence on
  that family plus uniform bounds determines the state on 𝒜; say whether {e} alone suffices or what larger family is needed;
  make 𝒜 compatible with NONFREE55 as it stands on disk when I write that section.
- **T-DIAG (ML3).** Prove: per-R subsequential limits ω_{a,R} → ω_R and ω_R → ω_∞ on one countable family give one lattice
  sequence (a_j, R_j) with ω_{a_j,R_j} → ω_∞ on that family; state exactly which additional uniformity (if any) is needed for
  convergence on all of 𝒜, and show that Ward/symmetry constants need not be R-uniform (CODEX_REVIEW_SPHERE item 5).
- **T-EXT (ML9).** State and prove the uniform extension estimate that exchanges a → 0 with the Whitney decomposition of a
  fixed flat test function, and state the minimal RG-side input (I expect: a separated bound whose dependence on the
  separation scale λ is a power law, uniformly in a for λ down to a fixed multiple of a, plus the deterministic bound on e_a
  below that scale) — and prove necessity, if true, so that "minimal" is a theorem.
- **T-TRAJ (ML12).** Write the single bare-coupling trajectory (F-tune's g_0(a; g_ref) at ℓ_ref = 1, the condition
  u_K − R > 0 stated, the soft-kernel level couplings fixed by FI-1, the sphere profile rule) and check every input file's
  trajectory assumption against it by locating string; list every conflict.
- Mention any of ML4-ML8, ML10, ML11, ML13 I find easy (no obligation).

What would count as a refutation of what this file will claim.
- ML2: (a) the primary text's growth condition differs from the one I state (norm order, domain of the test functions,
  sequence σ_n), when I claim to have checked it; (b) a step of my reconstruction proof fails — e.g. the contraction bound
  needs a growth estimate that my stated hypotheses do not give; (c) data obeying my SRC-κ-type hypotheses that violate my
  stated growth conclusion; (d) a positive-time test element on which the limiting OS form is not determined by values of the
  Schwinger distributions on ^0𝒮, or lattice RP that fails to pass to the limit form I define.
- ML1: an element needed by OS0-OS3 that is not in 𝒜; an E(4) motion not acting on 𝒜; two different limiting states that
  agree on the claimed determining family and obey the same uniform bounds.
- ML3: data meeting my hypotheses with no convergent diagonal sequence; a uniformity used but not stated.
- ML9: data meeting my stated RG-side input for which S_n^a(F) is not uniformly bounded or does not converge for a flat F;
  or data showing that my "minimal" input is not necessary for the conclusion.
- ML12: a file I record as consistent with the trajectory whose quoted assumption in fact conflicts, or a listed conflict
  that is not one.
- Any check in checks/ol55_*: a gate that could not have failed, or a PASS that is not reproduced.

Method commitments: large files by grep -n then sed -n ranges, located by string; Codex files read as on disk now; any
numeric check gets checks/ol55_<id>_criteria.md before its script, exact rational arithmetic only; [m] for anything about
the literature not checked against a primary or open-access text (at most one sentence quoted per source).

---

### PRE-STATED addendum (2026-10-29T05:12Z; coordinator's message, read before any finding below was written)
The coordinator relayed CODEX_REVIEW_ASSEMBLY (now complete on disk, 237 lines; its last lines are complete). Scope changes
accepted: (1) ML3 (DIAG) is PROVEN by Codex (R2; "Exactly what may be banked" item 1) — cited, not redone (§5 only states the
interface to this file's formulation); (2) Codex's ordered item 1 is the core of this file: ONE OS formulation and observable
algebra (reconstruction theorem, test-function/contact domain, multiplication and RP forms, E(4) action, normalisation and
support maps), the decision "ordinary Euclidean moments or restricted Schwinger distributions", and the positivity/extension
bridge written out; (3) Codex's ordered item 14 (EXT, growth in insertion number, large-distance seminorm control, RP-domain
bridge) is also this file's; (4) PANEL_P1's closure is banked only in its original form (Codex bank item 5) — if the
formulation moves to separated distributions, the closure is re-proved for that formulation here (Theorem CLOSURE-sep).
Additional refutation criterion: a step of CLOSURE-sep that uses a value of a Schwinger functional on a test function not in
^0𝒮, or an "ordinary positivity" form, would refute it.

---

# FINDINGS (appended from 2026-10-29T05:12Z)

## §0. Reading record, literature access, and symbol pins

**Read (by locating string; large files by grep + sed ranges only).** ASSEMBLY55 (all); CODEX_REVIEW_ASSEMBLY (all, as on disk
≈05:00Z); PANEL_P1 §1-§3, §7-§8; SRCCD55 §2.2-§3.5, Proposition E, §11-§14; CODEX_REVIEW_SRCCD §7; CODEX_REVIEW_SRCAN items 3,
6, 10, 11; CODEX_REVIEW_P4 §4.1-§4.3; CODEX_REVIEW_SPHERE Findings 7, 12, 14 and its bank list; SPHERE55 §1.4, §3.4 (W0
lines), §5; SEAM55 §1.4-§1.6 (in flight, read ≈05:05Z); FLOW "Def F-g", "Theorem F-flow", "Theorem F-tune", "Lemma F-ind",
§10, "Lemma F-R"; FLOW55 §1; RLARGE "Flow hypothesis (F_R)", Theorem RLF v1/v3 quantifiers, "(RLF-δ)_k"; RLARGE_U55 §3
(FI-1); CODEX_REVIEW_RLU item 2; CODEX_REVIEW_UNIV §9; HINT2_55 symbol pins and R2.1; ROTDEF §2.2 and its I3 row; SRCAN55
symbol-table rows and SA-F lines; SMALLNESS_DAG symbol notes and "Stage 7"; PROOF §0 "T_OS (the owner's target)", §1 S1-S3,
[S26-BANKED] lines "Source-inserted RG (SRC)" and "Sphere route — construction"; HANDOFF; NONFREE55 (PRE-STATED only, 42
lines, at 05:11Z — nothing to align with beyond its T3).

**Literature.** OS I (CMP 31, 1973) and OS II (CMP 42, 1975) on Project Euclid: the fetch returned an empty page (as
CODEX_REVIEW_SRCCD §7 found: "security/service page"). **The primary texts were not read.** Every statement attributed to
OS I/II below carries **[m-sec]**: checked against two open-access secondary sources, not against the primary text:
- **[KQR]** Kravchuk, Qiao, Rychkov, *Distributions in CFT II. Minkowski space*, arXiv:2104.02090v2 — §2.2 (OS axioms) and §9
  ("Review of Osterwalder-Schrader theorem") read in the text extracted from the arXiv PDF (scratchpad copy only).
- **[AMT]** Adamo, Moriwaki, Tanimoto, *Osterwalder-Schrader axioms for unitary full vertex operator algebras*,
  arXiv:2407.18222v2, §2.5 — read only through the fetch tool's summarising extraction, so it is corroboration of the
  formula's shape, not a verbatim check.
What they say, in my words (one quotation, [KQR] §2.2): (L1) Schwinger functions are distributions on ^0𝒮, Schwartz functions
vanishing with all derivatives at coincident points ([KQR] Remark 2.4); (L2) the OS reflection form uses test functions
supported at positive, strictly ordered times, so that in it all operators "sit at separated positions" ([KQR] §2.2,
after their (2.21)); (L3) OS II's linear growth condition: there are s ∈ ℕ and
σ_n ≤ α(n!)^β with |S_n(f)| ≤ σ_n|f|_{n·s} for all f ∈ ^0𝒮(R^{dn}), |f|_p := max_{|γ|≤p} sup_x (1+|x|²)^{p/2}|∂^γf(x)|
([KQR] (9.14), (9.18); [AMT] §2.5 has the same form, with constants C_1(n!)^{C_2} and norm order sn, on 𝒮_≠ = ^0𝒮);
(L4) the original secondary-source reading attributed the Hilbert space,
semigroup and multi-time analyticity in Re y_k > 0 to hypotheses without linear growth, and used linear growth for the
tempered boundary bound ([KQR] Remark 2.5, §9.1, §9.2.2). This historical attribution is NOT the current proof contract:
REC (e) below uses E0′ for full continuation; only (a)-(d) and single-cut semigroup analyticity are established here without it;
(L5) OS I's Lemma 8.8 is false (counterexample
S_2 = e^{−y_1y_2}); OS II repairs it either by a stronger axiom Ě0 or by the linear growth condition ([KQR] §9.2.1-9.2.2);
(L6) OS I/II and [KQR] §9 treat ONE Hermitian scalar field; [KQR] §2.2 states the axioms for tensor fields and says the
adaptation of OS I/II "should be relatively straightforward" — so the several-field/tensor version of "E0′ ⇒ Wightman" is
**[m-sec] and NOT-VERIFIED** as a literature attribution. The separate in-repository producer now proves the finite
Cartesian tensor implication with its explicit dictionary (REC_LIB §§15,18; REC_CONT; REVIEW2_REC). General O(4)
representation continuation is still unproved here.

**Symbol pins (systemic defect 1).** R = torus side / sphere radius (geometric); **R_F := 2R_0 = FLOW's additive constant in
(F_R)** (FLOW, RLARGE and SRCAN55 write it "R"; HINT2_55 pins it "R_F"); a = bare spacing; level k = 0 (spacing a) … K
(spacing ℓ_ref = L^Ka = 1); **g_bare = FLOW's g_0 = PROOF §1 S3's g_K** (PROOF's resolution index runs the other way: its
"resolution K" is the finest, with "β_K = 2N/g_K²"); **g_ref := FLOW's g_K = g** (the coupling at the reference level);
**γ_0 := FLOW/(RLF-δ)'s coupling-domain threshold** (not N5-sf0's gap, SMALLNESS_DAG "γ_0" note); **g_1 := FLOW's ceiling
(γ^{-2} + R_F)^{-1/2}** (not a level-1 coupling); **g_thr := RLF v3's threshold written "g_K ≤ g_0"** (RLARGE §1.2; ROTDEF's
pin). In this file s, α, β are the E0′ constants (L3) — not the lane's β_±, β_0′, β_K. e_a = ROTDEF §2.2's clover density.
S = a Schwinger functional (not the Wilson action, written S_W). δ(x) := min_{i<j}|x_i − x_j|.

## §1. The OS formulation (CODEX_REVIEW_ASSEMBLY ordered item 1; ML2 + the formulation part of ML1)

### 1.1 The decision: restricted (separated) Schwinger distributions, not ordinary Euclidean moments

**Proposition FS (forced for the point-like clover field on tori). PROVEN-HERE (re-derivation of SRCCD55 V-1 with the
trajectory explicit).** Setting of Lemma V (Wilson measure on a hypercubic torus with R/a even, u_0 ≥ u_*(N)), along the
trajectory of §6 (a = L^{-K}, u_0 = 1/g_bare² with F-tune's upper bracket). Let Z(a) > 0 be any normalisation and
O^Z_a(f) := Z(a)^{-1}Σ_x a⁴f(x)e_a(x). Suppose, for all small a,
 (i) Var(O^Z_a(f_0)) ≤ C_1 for one f_0 ∈ C_c^∞, f_0 ≠ 0 (an ordinary second moment, cutoff-uniformly bounded), and
 (ii) |Cov(O^Z_a(g_1), O^Z_a(g_2))| ≥ c_0 > 0 for one pair with dist(supp g_1, supp g_2) > 0 (non-vacuity).
Then |Cov(O_a(g_1), O_a(g_2))| ≥ c·a^{-4}(C + β_+log(1/a))^{-2} → ∞. Hence (i), (ii) and any cutoff-uniform bound on the
separated covariance of e_a (in particular E0 for the limit along this sequence, or SRC-κ (κ-1)) cannot hold together.
*Proof.* Lemma V ([S26-BANKED] "Lemma V … CONFIRMED", scoped): Var(O_a(f_0)) ≥ c_V g_bare⁴a^{-4}(‖f_0‖_2² − O(a)). With (i):
Z² ≥ c_V g_bare⁴a^{-4}‖f_0‖²/(2C_1) for small a. With (ii): |Cov(O_a(g_1),O_a(g_2))| = Z²|Cov(O^Z_a(g_1),O^Z_a(g_2))| ≥ c_0Z².
On the trajectory, F-tune's upper bracket at k = 0 gives u_0 ≤ g_ref^{-2} + β_+K log L + R_F with K log L = log(1/a), so
g_bare⁴ ≥ (C + β_+log(1/a))^{-2}. ∎
**Decision.** With exact Wilson RP, a non-vacuous normalisation and any cutoff-uniform separated bound, the construction for
the point-like clover field **cannot produce ordinary Euclidean moments of smeared e; it can produce only restricted
(separated) Schwinger distributions on ^0𝒮.** This is OS I/II's own formulation (L1-L2). Flowed fields at fixed positive flow
time do have moments but lose exact RP across the reflection plane (PANEL_P1 §3; CODEX_REVIEW_ASSEMBLY R13), so they would
need a different formulation with a localisation limit — not chosen. On the sphere lattice K_a, Lemma V is NOT-VERIFIED (its
Step 1 uses transitivity of translations on plaquettes); the separated formulation is used there too because it is weaker,
not because FS forces it there.

### 1.2 Definitions (the one formulation used everywhere below)
- **D1 (norms)** |F|_k := max_{|γ|≤k} sup_x (1+|x|²)^{k/2}|∂^γF(x)| on R^{4n}, |x|² := Σ_i|x_i|² (L3).
- **D2 (test spaces)** Δ_n := {x : x_i = x_j for some i ≠ j}; ^0𝒮_n := {F ∈ 𝒮(R^{4n}) : ∂^γF = 0 on Δ_n ∀γ} (closed in
  𝒮; Fréchet); 𝒟_n := C_c^∞(R^{4n}\Δ_n) ⊂ ^0𝒮_n; Ω^+_n := {x : 0 < t_1 < t_2 < … < t_n}; 𝒮_{+,n} := {F ∈ 𝒮(R^{4n}) :
  F = 0 off Ω^+_n}; 𝒟_{+,n} := C_c^∞(Ω^+_n). (n = 0: C.) Since R^{4n}\Ω^+_n is a finite union of closed half-spaces
  {t_1 ≤ 0}, {t_i ≥ t_{i+1}}, it is the closure of its interior, so every derivative of F ∈ 𝒮_{+,n} vanishes there; as
  Δ_n ⊂ R^{4n}\Ω^+_n, 𝒮_{+,n} ⊂ ^0𝒮_n.
- **D3 (reflection, conjugation)** θ(t, x⃗) := (−t, x⃗); (ΘF)(x) := F(θx_1, …, θx_n); F^*(x_1, …, x_n) := conj F(x_n, …,
  x_1); ΘF^* := Θ(F^*). (T_sF)(x) := F(x_1 − se_0, …, x_n − se_0).
- **D4 (E(4) action, scalar field)** (g·F)(x) := F(g^{-1}x_1, …, g^{-1}x_n), g ∈ E(4) = O(4) ⋉ R^4.
- **D5 (the observable algebra 𝒜 — ML1's object)** 𝒜 := finite sequences F = (F_n)_{n≥0}, F_n ∈ ^0𝒮_n; 𝒜_𝒟 (F_n ∈
  𝒟_n); positive half 𝒜_+ (F_n ∈ 𝒮_{+,n} for n ≥ 1, F_0 ∈ C) and its dense part 𝒜_{𝒟+} (F_n ∈ 𝒟_{+,n}); local parts
  𝒜(O) := {F ∈ 𝒜_𝒟 : supp F_n ⊂ O^n}.
- **D6 (multiplication: partial, never across a coincidence)** F ⊗ G := (Σ_{k+l=n}F_k ⊗ G_l)_n, defined when every F_k ⊗ G_l
  lies in ^0𝒮_{k+l}. The products used: (ΘF^*, G) with F, G ∈ 𝒜_+ (always defined, Lemma P); (h, T_τG) with h vanishing off
  {0 < t < τ/2}, G ∈ 𝒜_+ (Theorem REC (d)). Not defined in general: f ⊗ f for f ∈ 𝒮(R^4) supported in t > 0 is not flat at
  x_1 = x_2 — **the element "e(f)²" is not in 𝒜** (consistent with FS).
- **D7 (the "state")** S = (S_n)_{n≥0}, S_0 := 1, S_n ∈ (^0𝒮_n)′; S(F) := Σ_n S_n(F_n).
- **D8 (normalisation, support and observable maps; lattice approximants)** Torus Λ_{a,R} := (aZ/RZ)^4, R/a even; Wilson
  measure ω_{a,R} at the bare coupling g_bare(a; g_ref) of §6. Normalisation map: ê_a(x) := Z(a)^{-1}(e_a(x) −
  ω_{a,R}(e_a(x))), Z(a) > 0 R-independent with Z(a) ≥ c_Z a^{q_Z} (the lane's SRC-κ normalisation is Z ≡ 1). Support map:
  ι_R : B_{R/4} → R^4/RZ^4, x ↦ x mod R (injective; torus distance = Euclidean distance on B_{R/4}). Observable map: for F ∈
  𝒜_𝒟 with supp F_n ⊂ (B_{R/4})^n, A_F := Σ_n Σ_{x∈((aZ)^4)^n} a^{4n}F_n(x)Π_i ê_a(ι_Rx_i) (a lattice observable), and
  S^{a,R}(F) := ω_{a,R}(A_F); at a > 0, A_FA_G = A_{F⊗G} for ALL F, G (no coincidence problem on the lattice). Sphere: ι_R
  is replaced by the chart χ_R at the pole S (CODEX_REVIEW_P4 §4.1) and the hypercubic sum by K_a's sites with their volume
  weights; the RP reflections are the four coordinate great spheres through S (banked).
- **D9 (determining family)** D := ∪_n D_n, D_n ⊂ 𝒟_n countable and dense in ^0𝒮_n (exists: 𝒮(R^{4n}) is a separable
  metric space, so is its subset 𝒟_n, and 𝒟_n is dense in ^0𝒮_n by Lemma DENSE), fixed once, independent of a and R
  (SPHERE55's (U-alg)), and closed under a fixed countable dense subgroup G_0 ⊂ E(4) (replace D_n by G_0·D_n).

**Lemma P (the RP form never meets a coincidence). PROVEN-HERE.** For F ∈ 𝒮_{+,n}, G ∈ 𝒮_{+,m} and s ≥ 0, ΘF^* ⊗ T_sG ∈
^0𝒮_{n+m}; for F ∈ 𝒟_{+,n}, G ∈ 𝒟_{+,m}, ΘF^* ⊗ G ∈ 𝒟_{n+m}; and |ΘF^* ⊗ G|_k ≤ |F|_k|G|_k.
*Proof.* ΘF^*(x) = conj F(θx_n, …, θx_1) vanishes with all derivatives off {t_1 < … < t_n < 0}; T_sG vanishes with all
derivatives off {s < t′_1 < … < t′_m}. So the product vanishes with all derivatives off U := {t_1 < … < t_n < 0 < t′_1 <
… < t′_m}; points of U have pairwise distinct times, so Δ_{n+m} ∩ U = ∅ and the product is flat on Δ_{n+m}. For 𝒟_+, supp ⊂
supp(ΘF^*) × supp(G), a compact subset of U. The norm bound: ∂^{(α,β)}(F′ ⊗ G) = ∂^αF′ ⊗ ∂^βG, 1 + |x|² + |y|² ≤
(1+|x|²)(1+|y|²), and Θ, * preserve |·|_k. ∎

**Lemma DENSE. PROVEN-HERE.** 𝒟_n is dense in ^0𝒮_n, and 𝒟_{+,n} is dense in 𝒮_{+,n}.
*Proof.* Fix ψ ∈ C^∞(R), 0 ≤ ψ ≤ 1, ψ = 0 on (−∞, 1], ψ = 1 on [2, ∞), and χ ∈ C_c^∞(R^{4n}) equal to 1 on the unit ball.
(i) χ(·/ρ)F → F in 𝒮 as ρ → ∞ (|(1 − χ(·/ρ))F|_k ≤ C_kρ^{-1}|F|_{k+1}). (ii) Ψ_ε(x) := Π_{i<j}ψ(|x_i − x_j|²/ε²) is
smooth, = 1 where δ(x) ≥ √2ε, = 0 where δ(x) ≤ ε, and |∂^γΨ_ε| ≤ C_γε^{-|γ|}. For F ∈ ^0𝒮_n and δ(x) < √2ε, let y be the
nearest point of the plane {x_i = x_j} realising δ(x) (|x − y| = δ(x)/√2 < ε); all derivatives of F vanish at y, so
Taylor's formula on [y, x] gives |∂^βF(x)| ≤ (2√n·ε)^M/M!·max_{|γ|=|β|+M} sup_{z∈[y,x]}|∂^γF(z)|, and 1 + |x|² ≤
4(1 + |z|²) for ε ≤ 1. Hence |(1 − Ψ_ε)F|_k ≤ C_{k,M}ε^{M−k}|F|_{2k+M} → 0 (M > k). So Ψ_εχ(·/ρ)F ∈ 𝒟_n converges to F.
(iii) For 𝒮_{+,n} use Ψ^+_ε(x) := ψ(t_1/ε)Π_{i<n}ψ((t_{i+1} − t_i)/ε): F ∈ 𝒮_{+,n} is flat on the closed set R^{4n}\Ω^+_n,
Taylor is taken from the nearest point of that set (distance < 2ε where Ψ^+_ε ≠ 1), and Ψ^+_εχ(·/ρ)F ∈ 𝒟_{+,n}. ∎

**Lemma ACT (the E(4) action is continuous). PROVEN-HERE.** For g = (Λ, b): |g·F|_k ≤ 4^k2^{k/2}(1 + n|b|²)^{k/2}|F|_k, g·
maps ^0𝒮_n and 𝒟_n onto themselves, and g ↦ g·F is continuous E(4) → 𝒮(R^{4n}) for each F.
*Proof.* Chain rule: ∂^γ(F∘g^{-1}) is a sum of ≤ 4^{|γ|} terms (∂^{γ′}F)∘g^{-1}, |γ′| = |γ|, with coefficients products of
entries of Λ^{-1} (|entries| ≤ 1); and 1 + |x|² ≤ 2(1 + n|b|²)(1 + |g^{-1}x|²). g^{-1} acts on each point by an isometry, so
Δ_n and compact subsets of its complement are preserved. Continuity: for g′ → g, (∂^{γ′}F)∘g′^{-1} − (∂^{γ′}F)∘g^{-1} is
bounded by sup|∇∂^{γ′}F| on the segment times |g′^{-1}x − g^{-1}x| ≤ C‖g′ − g‖(1 + |x|), which gives |g′·F − g·F|_k ≤
C_{k,g}‖g′ − g‖|F|_{k+2}. ∎

### 1.3 The axioms used ([m-sec] as to OS I/II's wording; checked against [KQR], [AMT])
- **(E0′) linear growth:** ∃ s ∈ ℕ, α, β ≥ 0 with |S_n(F)| ≤ α(n!)^β|F|_{sn} for all n ≥ 1, F ∈ ^0𝒮_n. (Implies E0: S_n
  ∈ (^0𝒮_n)′.)
- **(E1)** S_n(g·F) = S_n(F) for g ∈ E(4) (OS use the proper group [m-sec]; the full group holds here anyway).
- **(E2)** Σ_{n,m}S_{n+m}(ΘF_n^* ⊗ F_m) ≥ 0 for every F ∈ 𝒜_+ (well-defined by Lemma P).
- **(E3)** S_n(F^π) = S_n(F), F^π(x) := F(x_{π(1)}, …, x_{π(n)}); and **(Re)** S_n(F̄) = conj S_n(F).
- **Not used:** ordinary positivity S_{2n}(F̄ ⊗ F) ≥ 0 for unordered same-half F (it is not among E0′-E3, and Theorem REC
  never uses it); E4 (clustering). The abstract reconstruction below asserts no unique vacuum or mass gap; those remain
  separate obligations of the full Yang–Mills target in MASS_GAP_TARGET.md.

### 1.4 Theorem REC — the reconstruction actually invoked (ML2). (a)-(d) proved below; (e) uses REC_LIB + REC_CONT
**Statement.** Let S_0 = 1 and let S satisfy E0 (|S_n(F)| ≤ C_n|F|_{N_n}), E1 for time translations and for E(3) := {g ∈ E(4) fixing the
time axis: g(t, x⃗) = (t, Λ′x⃗ + b⃗)}, and E2. Then:
- **(a) Hilbert space.** ⟨F, G⟩ := Σ_{n,m}S_{n+m}(ΘF_n^* ⊗ G_m) is a positive semidefinite Hermitian form on 𝒜_+; with
  𝒩 := {F : ⟨F, F⟩ = 0}, ℋ := completion of 𝒜_+/𝒩, Ω := [(1, 0, 0, …)], ‖Ω‖ = S_0 = 1.
- **(b) Semigroup.** For s ≥ 0, T_s maps 𝒜_+ into itself and 𝒩 into 𝒩; the induced P_s satisfies ‖P_s‖ ≤ 1, P_s = P_s^* ≥ 0,
  P_sP_{s′} = P_{s+s′}, s ↦ P_s strongly continuous, P_sΩ = Ω. Hence P_s = e^{−sH} with H = H^* ≥ 0, HΩ = 0.
- **(c) Spatial symmetry.** U(g)[F] := [g·F], g ∈ E(3), is a strongly continuous unitary representation commuting with P_s,
  U(g)Ω = Ω.
- **(d) Euclidean field operators from separated distributions.** For τ > 0 and h ∈ 𝒮(R^4) vanishing off {0 < t < τ/2},
  Φ_τ(h)[F] := [h ⊗′ T_τF], (h ⊗′ G)_{n+1} := h ⊗ G_n, is a well-defined, densely defined, closable operator on ℋ (domain
  𝒜_+/𝒩), and ⟨Ω, Φ_{τ_1}(h_1)Φ_{τ_2}(h_2)⋯Φ_{τ_n}(h_n)Ω⟩ = S_n(h_1 ⊗ T_{τ_1}(h_2 ⊗ T_{τ_2}(⋯ ⊗ T_{τ_{n−1}}h_n))): the
  reconstructed Euclidean data read S only at time-ordered, hence separated, configurations. **No coincident-point value of S
  and no ordinary-positivity form enters (a)-(d).**
- **(e) Abstract continuation and reconstruction, with E0′.** Suppose in addition that the SAME hierarchy S obeys E0′ with
  one triple (s, α, β) for ALL n, full E1, E3 and (Re). [REC_LIB](REC_LIB.md) §§6, 18, with the continuation proved in
  [REC_CONT](REC_CONT.md), then supplies holomorphic W_n on the forward tube
  T_n := {z : Im(z_{j+1}−z_j) ∈ V_+ for 1 ≤ j < n}. Here V_+ is the open future cone for metric diag(1,−1,−1,−1), and
  j(t,x⃗) := (it,x⃗); the scalar Wick values satisfy W_n(jx_1,…,jx_n)=S_n(x_1,…,x_n) at ordered separated Euclidean points,
  with S read distributionally. W_0=1 and W_1 is constant; all W_n are invariant under common complex translations.
  Set d_n(y):=min_{j<n}[(y_{j+1}−y_j)^0−|(y_{j+1}−y_j)⃗|] (d_1=1). For each n there are finite C_n,A_n,B_n with
      |W_n(x+iy)| ≤ C_n(1+|x|+|y|)^{B_n}(1+d_n(y)^{-1})^{A_n}.
  The tempered boundary distributions reconstruct Hermitian local fields on a common dense domain of the SAME ℋ as (a),
  a cyclic invariant Ω, proper orthochronous Poincaré covariance and joint translation spectrum in the closed future cone.
  Their time generator is the H of (b). Unitary equivalence of reconstructions does not imply uniqueness of the invariant
  vacuum; neither a nonzero excited sector nor a positive mass threshold follows. Finite Cartesian tensor families use
  the explicit dictionary in §4 below, not an unspecified O(4) representation.
  **E0′ is used in this producer for the continuation itself, not just the boundary estimate.** The older claim of a
  full multi-time continuation without E0′ is an UNPROVED alternative here. E0 alone gives (a)-(d) and the one-cut functions
  ⟨u,e^{−zH}v⟩ for Re z>0 (REC_LIB §5); it does not justify arbitrary products of unbounded continued insertions or glue
  their separate cuts. The completed E0′ route supplies that missing step. REVIEW2_REC.md reviews the abstract producer;
  this consumer alignment is new authorship and requires a separate fresh review.

**Proof of (a).** Lemma P makes each term defined. Antilinearity in F is from the conjugation in F^*. Positivity is E2; a
positive semidefinite sesquilinear form on a complex space is Hermitian (polarisation: ⟨F + λG, F + λG⟩ ∈ R for λ = 1, i).
Cauchy–Schwarz makes 𝒩 = {F : ⟨G, F⟩ = 0 ∀G} a subspace. ∎
**Proof of (b).** *Symmetry.* Let τ_b translate every argument by b. With b := −(s/2)e_0, E1 gives S(ΘF^* ⊗ T_sG) =
S(τ_bΘF^* ⊗ T_{s/2}G), and τ_bΘF^*(x) = conj F(θx_n − (s/2)e_0, …, θx_1 − (s/2)e_0) = Θ(T_{s/2}F)^*(x); so ⟨F, T_sG⟩ =
⟨T_{s/2}F, T_{s/2}G⟩ = ⟨T_sF, G⟩. *Polynomial growth (E0 supplies the large-distance weights).* For G_m with m insertions,
h := (ue_0,…,ue_0) ∈ R^{4m} has |h|²=mu². Thus
  1+|y+h|² ≤ 2(1+mu²)(1+|y|²),    |T_uG_m|_k ≤ 2^{k/2}(1+mu²)^{k/2}|G_m|_k.
For finite F choose N=max N_{n+m} over its nonzero component pairs (C_0=1,N_0=0). Monotonicity of |·|_k and Lemma P give
  |⟨F,T_uF⟩| ≤ Σ_{n,m} C_{n+m}2^{N/2}(1+mu²)^{N/2}|F_n|_N|F_m|_N
               ≤ A_F(1+u)^N ≤ P_F(u),    u≥0,
where A_F:=Σ_{n,m}C_{n+m}2^{N/2}(1+m)^{N/2}|F_n|_N|F_m|_N and P_F(u):=1+A_F(1+u)^N.
This is a polynomial majorant for this F; its constants and degree need not be uniform in insertion number. The factor m
is essential, exactly as in REC_LIB §3. *Contraction.* ‖T_sF‖²=⟨F,T_{2s}F⟩≤‖F‖‖T_{2s}F‖. If ‖F‖=0 this already gives
T_sF∈𝒩. Otherwise iterate k times to get
  ‖T_sF‖ ≤ ‖F‖^{1−2^{−k}}‖T_{2^ks}F‖^{2^{−k}}
           ≤ ‖F‖^{1−2^{−k}}P_F(2^{k+1}s)^{2^{−k−1}} → ‖F‖,
since log P_F(2^{k+1}s)=O(k) for fixed s,F. Hence T_s𝒩⊂𝒩 and ‖P_s‖≤1. *Positivity:*
⟨F, T_sF⟩ = ‖T_{s/2}F‖² ≥ 0. *Strong continuity:* ‖T_sF − F‖² = ⟨F, F⟩ − 2Re⟨F, T_sF⟩ + ⟨F, T_{2s}F⟩ → 0, since
u ↦ ⟨F, T_uF⟩ is continuous (T_uF_m → F_m in 𝒮, S continuous); extend by density and ‖P_s‖ ≤ 1. *Generator:* P_1 is a
positive contraction with trivial kernel (P_1ψ = 0 ⇒ ‖P_{1/2}ψ‖² = 0 ⇒ … ⇒ P_{2^{−k}}ψ = 0 ⇒ ψ = lim P_{2^{−k}}ψ = 0);
H := −log P_1 (spectral theorem) is self-adjoint and ≥ 0; P_q = e^{−qH} for dyadic q by uniqueness of positive square roots,
and for all s ≥ 0 by strong continuity of both sides. T_s(1, 0, …) = (1, 0, …) gives P_sΩ = Ω. ∎
**Proof of (c).** g ∈ E(3) commutes with θ and with T_s and preserves each Ω^+_n, so g·𝒜_+ = 𝒜_+ and ⟨g·F, g·G⟩ =
S(g·(ΘF^* ⊗ G)) = ⟨F, G⟩ by E1. U(g) is isometric on the dense set with inverse U(g^{-1}); strong continuity follows from
Lemma ACT and continuity of S. ∎
**Proof of (d).** h ⊗′ T_τF ∈ 𝒜_+ (the h-point has time < τ/2 < τ < every time of T_τF). *Well-defined.* For G ∈ 𝒜_+,
translate by b := −(τ/2)e_0 (E1): S(ΘG_n^* ⊗ h ⊗ T_τF_m) = S(Θ(T_{τ/2}G_n)^* ⊗ τ_bh ⊗ T_{τ/2}F_m). The first n+1 points
are at negative ordered times (the G-points below −τ/2, the h-point in (−τ/2, 0)), so H := Θ(T_{τ/2}G_n)^* ⊗ τ_bh equals
ΘK^* with K := (ΘH)^* ∈ 𝒮_{+,n+1} (its points: the reflected h-point in (0, τ/2), then the G-points above τ/2). Hence
⟨G, h ⊗′ T_τF⟩ = ⟨K_G, T_{τ/2}F⟩ with K_G := (K(G_n))_n ∈ 𝒜_+. If F ∈ 𝒩 then T_{τ/2}F ∈ 𝒩 by (b), so h ⊗′ T_τF is
orthogonal to all of 𝒜_+, in particular to itself: it lies in 𝒩. *Closable.* ⟨[G], Φ_τ(h)[F]⟩ = ⟨P_{τ/2}[K_G], [F]⟩ is
bounded in [F] for each [G], so Φ_τ(h)^* is densely defined. *Vacuum expectations.* Φ_{τ_n}(h_n)Ω = [h_n] (T_τ fixes the
n = 0 component), and inductively Φ_{τ_1}(h_1)⋯Φ_{τ_n}(h_n)Ω = [h_1 ⊗ T_{τ_1}(h_2 ⊗ ⋯)]; ⟨Ω, [H]⟩ = S_n(H_n). ∎

**Producer-to-consumer contract.** D1 is REC_LIB's one-component Schwartz seminorm; D2/D5 give its flat tests and ordered
positive half, D3 gives reflection with conjugation and reversed positions (and reversed component labels in §4), and D7
supplies S_0=1. CLOSURE-sep (b)-(f), when its all-order, cutoff/volume-uniform hypotheses and R_j→∞ are actually proved,
supplies E0′, full E1, E2, E3 and (Re) on ONE common hierarchy. These are exactly the inputs to REC (e); an E0 estimate with
arbitrary N_n,C_n is sufficient only for (a)-(d) and the one-cut statement above. E0′ must hold on all flat tests, using
continuity/density, with one (s,α,β), not separate constants for each cutoff or degree. No ordinary Euclidean moment
extension, E4, full-field identification or mass-gap estimate is furnished by this abstract implication.

For the pointwise growth route, REC_LIB §16 and GROW below require **unconditional**, all-order (SEP-pt) with constants
uniform in a,R,n and placements. With Z=1, q_X=4 they give s=11, β=b_0+1. The further substitution b_0=p+2 requires the
outer joint-cumulant bound (16.4), INCLUDING singleton blocks and their moments; literal higher conditional SRC-κ bounds
do not supply it. Those Yang–Mills estimates remain OPEN. The larger-q_X formula and the separate smeared EXT route are
stated below; neither is a substitute for proving its input.

### 1.5 Reply to CODEX_REVIEW_ASSEMBLY R1 (F2a) — agree, and the repair
- **Agree** that F2a's replacement is not bookkeeping (Codex R1; summary row F2a "REFUTED repair-as-bookkeeping"). PANEL_P1's
  positive half was "every positive-half polynomial", which contains e(f)² and needs S_4 on (θf)⊗(θf)⊗f⊗f, not flat on the
  same-half collision diagonals.
- **Repair = a different positive half, not an extension.** In OS's formulation the positive half is 𝒜_+ (time-ordered test
  functions, D5); e(f)² is not an element of 𝒜 (D6). Every value the RP form needs is S on ΘF^* ⊗ G with F, G ∈ 𝒜_+, which
  lies in ^0𝒮 (Lemma P) — and, for the lattice-approximable dense part 𝒜_{𝒟+}, in 𝒟 (compact support off Δ). The bridge from
  lattice RP is: exact lattice RP on 𝒜_{𝒟+} (Lemma RP-lat, §2) → limit on 𝒟 → density of 𝒜_{𝒟+} in 𝒜_+ (Lemma DENSE) and
  continuity of the form (E0 + Lemma P). This is the "density/continuity argument on the restricted algebra" Codex asks for;
  it does not use (EXT) for flat tests in place of positivity.
- **Ordinary positivity is not needed.** "ordinary positivity of e(f)^*e(f)" is not among E0′-E3, and Theorem REC (a)-(d)
  never uses it. Codex's contact example (S_2 + cδ(x − y)) is invisible to ^0𝒮 — the two functionals are equal on 𝒜 — in
  line with [KQR] §2.2 (text after their (2.15)), which notes that the OS axioms impose nothing at coincident points, not
  even distributionally (paraphrase).

### 1.6 The intermediate scalar OS formulation and the full target
In this formulation the "state" is S on 𝒜: normalised (S_0=1), E(4)-invariant and positive on the RP cone
{ΘF^*⊗F:F∈𝒜_+}. It is not an ordinary positive state on the partial test algebra. After REC (e), the vacuum is an ordinary
positive state on the Wightman field polynomials, with proper orthochronous Poincaré covariance. This is a construction of
the chosen scalar hierarchy, conditional on all the printed inputs. It does not identify ℋ_e with the full physical
Yang–Mills Hilbert space, establish a common correctly normalized gauge-invariant field hierarchy, give a unique vacuum,
or produce a physical mass threshold. Those requirements of MASS_GAP_TARGET.md remain unchanged and OPEN. The alternatives
of contact-term renormalisation (H-src′-diag) or flowed fields with a localisation limit for RP remain separate unproved
routes; no owner decision shrinking the full target is inferred from this formulation.

## §2. The closure re-proved for separated distributions (Codex bank item 5 does not cover this formulation)

**Lemma RP-lat (the L9a mechanism, site reflection — the case used). PROVEN-HERE (standard; Osterwalder–Seiler [m]).** Wilson
measure on Λ_{a,R}, R/a even; θ : t ↦ −t (mod R) fixes the two site planes t = 0 and t = R/2. Choose the closed temporal
arc Λ_+ := [0,R/2] and let 𝔄_+ consist of bounded complex measurable functions of links GEOMETRICALLY CONTAINED in that
half, keeping distinct periodic geometric edges even when their endpoint names coincide. Thus positive temporal edges
have base 0 ≤ t ≤ R/2−a, while spatial edges at 0 ≤ t ≤ R/2 are included. Inverse orientations denote the same geometric
edge. Set (ΘA)(U) := A(θU). Then ω_{a,R}(Θ(A)^*A) ≥ 0 for every A ∈ 𝔄_+.
*Proof.* Both fixed planes are site planes, so no plaquette straddles one: every plaquette lies in Λ_+ or in Λ_− := θΛ_+, and
plaquettes inside a fixed plane are θ-invariant (s(U^{-1}) = s(U) absorbs orientation). Hence S_W = S_+ + ΘS_+ with S_+ :=
Σ_{p⊂Λ_+, p⊄fixed planes}βs(U_p) + ½Σ_{p⊂fixed planes}βs(U_p). Write U = (U_0, U_+, U_−), U_0 the links inside the fixed planes
(θ-fixed), U_± the remaining links of Λ_±. Then Z·ω(Θ(A)^*A) = ∫dU_0 ∫dU_+dU_− conj(A(θU))e^{−ΘS_+(U)}A(U)e^{−S_+(U)} =
∫dU_0 |∫dU_+ A(U_0, U_+)e^{−S_+(U_0,U_+)}|² ≥ 0, by the Haar-preserving substitution U_− = θU′_+ and reality of S_+. ∎
*Extent-two convention.* Endpoint membership alone is insufficient when R/a=2: it includes both temporal arcs. For the
two distinct positively oriented temporal edges U_0,U_1 at one spatial site, F=Re Tr U_0−Re Tr U_1 then satisfies
F(θU)=−F(U), so ω(Θ(F)^*F)=−ω(F²)<0 under every finite reflection-symmetric Wilson density. The strict sign follows from
full support and F not being identically zero. The geometric half above includes only one arc and excludes this F.
This corrects the original endpoint-only wording; [the second HRP review](REVIEW2_HRP.md) records its discovery. The
paired-half proof and all eventual compact-support continuum uses retain their stated hypotheses.
*Use.* The clover e_a(x) involves only links within distance a of x, and θ maps clover_{μν}(x) onto clover_{μν}(θx), so
Θ(ê_a(x)) = ê_a(θx) (ω(e_a) is θ-invariant). For F ∈ 𝒜_{𝒟+} with supp F_m ⊂ (B_{R/4})^m and a ≤ τ_F := min{t_1 over supp F},
A_F ∈ 𝔄_+, and the change of variables x ↦ θx in the lattice sum gives exactly
  Σ_{n,m}S^{a,R}_{n+m}(ΘF_n^* ⊗ F_m) = ω_{a,R}(Θ(A_F)^*A_F) ≥ 0
(the order reversal in F^* is immaterial because lattice moments are symmetric).
The historical toy check checks/ol55_1 G3 records equality on 200 complex-rational sequences, with a conjugation control
and a non-reversible-chain control. As REVIEW2_REC.md finding 2 explains, commuting scalar moments make this sum invariant
under reversing the insertion tuple. G3 therefore does not validate the order-reversal or label/support convention;
those are fixed by D2/D3, Lemma P and the analytic construction, independently of the toy results.

**Theorem CLOSURE-sep. PROVEN-HERE (implication).** Data: a sequence j ↦ (a_j, R_j), a_j → 0, R_j ≥ R_0 (R_j → ∞, or R_j ≡ R
for the fixed-torus statement), lattice functionals S^{(j)} := S^{a_j,R_j} of D8, the countable family D of D9.
Hypotheses (the whole contract in this formulation):
- **(H_reg-sep)** ∃ s ∈ ℕ, α, β ≥ 0: |S^{(j)}_n(F)| ≤ α(n!)^β|F|_{sn} for all j, n ≥ 1 and F ∈ 𝒟_n with supp F ⊂ (B_{R_j/8})^n.
- **(H_RP-sep)** Lemma RP-lat (exact; no input).
- **(H_Euc-sep)** (only if R_j → ∞) for every g ∈ G_0 and φ ∈ D: S^{(j)}(g·φ) − S^{(j)}(φ) → 0, for EVERY n (all-order; ML7).
Conclusions: there are a subsequence (not relabelled) and S with S_n ∈ (^0𝒮_n)′ such that
- (a) S^{(j)}_n(F) → S_n(F) for every n and F ∈ 𝒟_n (and S_n is the unique continuous extension to ^0𝒮_n);
- (b) E0′ with the same (s, α, β);
- (c) E1 for every g ∈ E(4) (if R_j → ∞ and (H_Euc-sep) holds);
- (d) E2 (RP for θ; with (c), for every affine hyperplane);
- (e) E3 and (Re); (f) S_0 = 1.
Without (H_Euc-sep), (a), (b), (d), (e), (f) hold, together with invariance under the limiting exact lattice symmetries.
*Proof.* (a)-(b) For F ∈ 𝒟_n the support is compact, so supp F ⊂ (B_{R_j/8})^n for j ≥ j_F (or for all j if it fits in the
fixed torus), and |S^{(j)}_n(F)| ≤ α(n!)^β|F|_{sn}. A diagonal extraction over the countable set ∪_nD_n gives a subsequence
converging on every φ ∈ D. For F ∈ 𝒟_n and ε > 0 pick φ ∈ D_n with α(n!)^β|F − φ|_{sn} < ε (D_n dense in |·|_{sn}); then
|S^{(j)}(F) − S^{(k)}(F)| ≤ 2ε + |S^{(j)}(φ) − S^{(k)}(φ)|, so the sequence is Cauchy. The limit obeys the bound on 𝒟_n and
extends uniquely to the closure of 𝒟_n, which is ^0𝒮_n (Lemma DENSE), with the same bound.
(c) For g ∈ G_0 and φ ∈ D: g·φ ∈ 𝒟 (Lemma ACT), so by (a) S(g·φ) − S(φ) = lim_j[S^{(j)}(g·φ) − S^{(j)}(φ)] = 0. For fixed
g ∈ G_0, F ↦ S_n(g·F) − S_n(F) is continuous on ^0𝒮_n (Lemma ACT + (b)) and vanishes on the dense D_n, hence everywhere. For
g ∈ E(4) take g_k ∈ G_0 → g; g_k·F → g·F in ^0𝒮_n (Lemma ACT), so S_n(g·F) = lim S_n(g_k·F) = S_n(F).
(d) For F ∈ 𝒜_{𝒟+}, every ΘF_n^* ⊗ F_m ∈ 𝒟_{n+m} (Lemma P), and for j large the identity after Lemma RP-lat gives
Σ_{n,m}S^{(j)}_{n+m}(ΘF_n^* ⊗ F_m) ≥ 0; by (a) the limit form is ≥ 0. For F ∈ 𝒜_+ take F^{(k)} ∈ 𝒜_{𝒟+} with F^{(k)}_n →
F_n in 𝒮 (Lemma DENSE); (F, G) ↦ ΘF^* ⊗ G is continuous into ^0𝒮 (Lemma P) and S is continuous, so the form at F is a limit of
non-negative numbers. With (c), conjugating θ by E(4) gives RP for every affine hyperplane.
(e) The lattice sum is symmetric under relabelling and the lattice moments are real; both identities are linear and pass to
the limit. (f) by definition. *Lattice symmetries without (H_Euc-sep):* for a_j = L^{-K_j} with K_j ↑, translations by v ∈
L^{-K}Z^4 are exact symmetries of ω_{a_j,R_j} and of the observable map for all j with K_j ≥ K, so S^{(j)}(τ_vF) = S^{(j)}(F)
exactly once supports fit (PANEL_P1's translation mechanism); with (b) and Lemma ACT this gives full translation invariance in
the limit. H(4) is exact (e_a is H(4)-invariant). ∎
*What was NOT used:* any value of S^{(j)} or S on a test function outside ^0𝒮 (in fact outside 𝒟), any ordinary-positivity
form, any moment of a smeared point field. So the refutation criterion of the PRE-STATED addendum is not met.

**Conditional intermediate clover-field contract.** For R_j→∞, CLOSURE-sep with ALL its hypotheses supplies the common
scalar hierarchy meeting REC (e), so REC_LIB + REC_CONT reconstruct that hierarchy. A non-freeness claim additionally needs
an H_int witness and its comparator theorem. This replaces only the clover-field reconstruction interface in PANEL_P1 §3;
it does not replace the full Yang–Mills existence-and-mass-gap target by a scalar-sector target:

- **(H_int-sep) compatibility condition (for NONFREE55).** W(S) := Φ(S_{n_1}(φ_1), …, S_{n_k}(φ_k)) with φ_i ∈ 𝒜_𝒟 (compact
  support off the coincidence set) and Φ continuous. Then W(S^{(j)}) → W(S) along the subsequence of (a), and |W(S^{(j)})| ≥ c
  for all j implies |W(S)| ≥ c. Every such W is determined by the reconstructed Euclidean data (Lemma DET, §4), so contact
  terms (Codex R1's cδ; R13's c‖K_t‖²) cannot move it. Witnesses that need a coincident-point value (variances of smeared e,
  4D-flowed one-point functions) are NOT on 𝒜.

**Corollary CONTRACT-sep (the sphere route's flat limit in separated form — the second half of ML8, which I found easy).
PROVEN-HERE (implication).** For R in a sequence R_k → ∞ let S^R be a continuum sphere functional obtained at FIXED R (by
CLOSURE-sep (a) on K_a through the chart χ_R; Ward constants may depend on R), with chart functionals S^R_n(F), F ∈ 𝒟_n,
supp F ⊂ (B_{ρ(R)})^n, ρ(R) → ∞. Assume:
- **(U-sep)** |S^R_n(F)| ≤ α(n!)^β|F|_{sn} with s, α, β independent of R and n (the separated replacement of SPHERE55's U-mom;
  OPEN, the first half of ML8);
- **(K-inv)** exact local Killing invariance on 𝒟 for every n: S^R_n(F∘ψ^{-1}_{R,v}) = S^R_n(F) for the boost and pole-rotation
  Killing fields v whose flow path keeps supp F inside the chart domain away from the seam, ψ_{R,v} := χ_R^{-1}∘(flow of v)∘χ_R
  (all-order input: ML7; CODEX_REVIEW_SPHERE Finding 7);
- **(RP-pole)** RP for the four coordinate great spheres through S (banked finite-cutoff RP, passed to S^R by CLOSURE-sep (d)).
Then every limit point S^∞ (it exists on D by (U-sep) and compactness) satisfies E0′ (same s, α, β), E1, E2, E3.
*Proof.* Compactness and density as in CLOSURE-sep (a)-(b). Translations: for the boost with c = e/(2R²), ψ_{R,v_c} → (x ↦ x + e)
in every C^k norm on compact sets (CODEX_REVIEW_P4 §4.1; SPHERE55 §5.2; both CONFIRMED there), so F∘ψ^{-1}_{R,v_c} → τ_eF in 𝒮
with supports in a fixed compact set off Δ (ψ acts on all points simultaneously by a diffeomorphism, so it preserves Δ and its
complement), and |S^R(τ_eF) − S^R(F)| = |S^R(τ_eF) − S^R(F∘ψ^{-1}_{R,v_c})| ≤ α(n!)^β|τ_eF − F∘ψ^{-1}_{R,v_c}|_{sn} → 0.
Rotations about S act linearly and exactly in the chart. RP: as in CLOSURE-sep (d) for each θ_μ, then for all hyperplanes
through 0 by SO(4) and all affine ones by translations. E3 as before. ∎
**Consequence.** CODEX_REVIEW_P4 §4.1's sufficient hypothesis (position-uniform unit-ball moments) is unattainable for the
point-like clover field on tori with a non-vacuous normalisation (Proposition FS); CONTRACT-sep is the version the sphere route
must use, with (U-sep) in place of (U-mom). Ward/N5 constants enter only through (K-inv) at fixed R and need not be R-uniform
(agree: CODEX_REVIEW_SPHERE bank item 5 / Finding 14).

## §3. (EXT), growth in insertion number, large-distance control (ML9 + Codex ordered item 14)

Throughout, S^{a,R}_n is D8's lattice functional and Z′ := sup_{0<a≤1} Σ_{y∈(aZ)^4} a^4(1+|y|²)^{-5/2} ≤ 324π² (for w in
the cell y + [0, a]^4, 1 + |w|² ≤ 9(1 + |y|²), and ∫_{R^4}(1 + |w|²)^{-5/2}dw = 2π²·∫_0^∞r³(1+r²)^{-5/2}dr = 4π²/3);
Z_5 := Σ_{c∈Z^4}(1 + |c|²)^{-5/2} ≤ 324π² likewise.

**(X0) Lattice crude bound. PROVEN.** 0 ≤ e_a(x) ≤ 24a^{-4} (ROTDEF §2.2: (4a⁴)^{-1} times 48 terms s(U_p) ∈ [0, 2]; the count
24 unordered / 48 ordered-pair clover plaquettes is checks/ol55_1 G1), so |ê_a(x)| ≤ C_Xa^{-q_X} with C_X := 24/c_Z, q_X :=
4 + q_Z; hence |ω(Π_iê_a(x_i))| ≤ (C_Xa^{-q_X})^n at EVERY lattice configuration, coincident or not.

**(X1) The RG-side input, in its minimal (local, smeared, per-scale) form.** There are A_n, p_n, r_n and c_* ≥ 1 such that for
all a ∈ (0, 1], R ≥ 32, n ≥ 2, λ ∈ [c_*a, 1] and every G ∈ C_c^∞(R^{4n}) supported in (Q_1 × ⋯ × Q_n) ∩ Sh_λ, where the Q_i are
closed cubes of side 2 inside B_{R/4}, Sh_λ := {λ < δ(x) < 4λ} for λ < 1 and Sh_1 := {δ(x) > 1}:
  **|S^{a,R}_n(G)| ≤ A_n λ^{−p_n} ‖G‖_{λ,r_n}**,  ‖G‖_{λ,r} := max_{|γ|≤r} λ^{|γ|}‖∂^γG‖_∞.
In words: separated, smeared bounds that are translation-uniform (unit cubes anywhere), uniform in a and R, and whose
dependence on the separation scale λ is a POWER law all the way down to a fixed multiple of the lattice spacing. Its
**linear-growth form** is A_n ≤ A^n(n!)^b, p_n ≤ pn, r_n ≤ rn.

**Lemma W (partition bounds). PROVEN-HERE.** (a) There is ψ_1 ∈ C^∞(R), ψ_1 = 0 on (−∞, 0], ψ_1 = 1 on [1, ∞), 0 ≤ ψ_1 ≤ 1,
with |ψ_1^{(k)}| ≤ C_G^{k+1}(k!)² for all k. (b) u(y) := ψ_1(|y|² − 1) on R^4 (u = 0 for |y| ≤ 1, = 1 for |y| ≥ √2) obeys
|∂^γu| ≤ C_u^{|γ|+1}(|γ|!)³, C_u := 3C_G. (c) Ψ_λ(x) := Π_{i<j}u((x_i − x_j)/λ) (= 0 where δ ≤ λ, = 1 where δ ≥ √2λ) obeys
max_{|γ|=m}|∂^γΨ_λ| ≤ (C_Wn²)^m(m!)³λ^{−m}, C_W := C_u². (d) With φ(t) := ψ_1(t + 1) − ψ_1(t) (supported in [−1, 1],
Σ_{k∈Z}φ(t − k) = 1) and χ_c(y) := Π_{μ=1}^4φ(y^μ − c^μ), c ∈ Z^4: Σ_cχ_c = 1, supp χ_c ⊂ c + [−1, 1]^4, |∂^γχ_c| ≤
16C_G^{|γ|+4}(|γ|!)².
*Proof.* (a) f(t) := e^{−1/t} (t > 0), 0 (t ≤ 0). For t > 0, Cauchy's estimate on the disc of radius t/2 about t, on which
Re(1/z) ≥ 2/(3t) (its image under z ↦ 1/z is the disc with diameter [2/(3t), 2/t]), gives |f^{(k)}(t)| ≤ k!(2/t)^ke^{−2/(3t)} ≤
k!2^k sup_{w>0}w^ke^{−2w/3} = k!2^k(3k/2)^ke^{−k} ≤ 3^k(k!)² (k^ke^{−k} ≤ k!). For Φ(t) := f(t)f(1 − t), Leibniz gives
|Φ^{(k)}| ≤ Σ_i binom(k,i)3^k(i!)²((k−i)!)² ≤ 3^kk!(k+1)k! ≤ 6^k(k!)²; ψ_1(t) := ∫_{−∞}^tΦ/∫Φ, so |ψ_1^{(k)}| ≤
6^{k−1}((k−1)!)²/∫Φ, and C_G := max(6, 1/∫Φ) works. (b) Faà di Bruno with the quadratic inner function q(y) = |y|² − 1: ∂^γ(ψ_1∘q)
is a sum over partitions of the m := |γ| derivative slots into blocks of size 1 or 2 (≤ m! of them) of ψ_1^{(#blocks)}(q) times
block derivatives of q, each ≤ 2√2 on the region |y| ≤ √2 where u is non-constant; so |∂^γu| ≤ m!·C_G^{m+1}(m!)²(2√2)^m ≤
C_u^{m+1}(m!)³. (c) Leibniz over the M := n(n−1)/2 factors: the multinomial weights sum to M^m ≤ n^{2m}; a factor carrying
k ≥ 1 derivatives contributes ≤ C_u^{k+1}(k!)³λ^{−k} ≤ C_u^{2k}(k!)³λ^{−k} (C_u ≥ 1), and Π(k_p!)³ ≤ (m!)³. (d) Telescoping
and the product of four one-dimensional bounds |φ^{(k)}| ≤ 2C_G^{k+1}(k!)². ∎

**Theorem EXT (the extension estimate: a → 0 exchanged with the Whitney decomposition of a fixed flat test). PROVEN-HERE
(implication).** Assume (X0), (X1). Then for every n ≥ 2, a ∈ (0, 1], R ≥ 32 and F ∈ 𝒟_n with supp F ⊂ (B_{R/8})^n:
 (i) |S^{a,R}_n(F)| ≤ σ′_n|F|_{N_n} + ρ_n(a)|F|_{N′_n}, with N_n := r_n + p_n + 1 + 5n, N′_n := (q_X + 5)n + 1, explicit σ′_n
     (below), and ρ_n(a) ≤ C_n′a → 0 (the sub-lattice remainder);
 (ii) in the linear-growth form of (X1): σ′_n + sup_{a≤1}ρ_n(a) ≤ α′(n!)^{β′} and N_n, N′_n ≤ s′n, with
     **s′ := max(r + p + 7, q_X + 6), β′ := b + 7r + 1** — i.e. (H_reg-sep) holds, so CLOSURE-sep applies and the limit
     satisfies OS II's E0′;
 (iii) (exchange of limits) if moreover S^{a,R}_n(G) converges as a → 0 (along a sequence) for every G in (X1)'s class at each
     fixed λ > 0 ("fixed-separated convergence"), then S^{a,R}_n(F) converges for every flat F: the a → 0 limit commutes with the
     Whitney sum. (Without that extra input, (i) still gives subsequential convergence by compactness, CLOSURE-sep (a).)
*Proof.* *Decomposition.* With Lemma W: F = Σ_{c∈(Z^4)^n}F_c, F_c := FΠ_iχ_{c_i}(x_i) (finitely many c; each F_c is supported in
Π_i(c_i + [−1, 1]^4), cubes of side 2 meeting B_{R/8}, hence inside B_{R/8+4} ⊂ B_{R/4} for R ≥ 32). Let λ_k := 2^{−k},
χ^{sh}_0 := Ψ_1, χ^{sh}_k := Ψ_{λ_k} − Ψ_{2λ_k} (k ≥ 1), supported in {λ_k < δ < 2√2λ_k} ⊂ Sh_{λ_k} (k ≥ 1) and {δ > 1} = Sh_1
(k = 0); Σ_{k=0}^Kχ^{sh}_k = Ψ_{λ_K}. Take K := max{k : λ_k ≥ c_*a}, so λ_K ∈ [c_*a, 2c_*a). Then
  F = Σ_cΣ_{k=0}^K F_cχ^{sh}_k + F(1 − Ψ_{λ_K}).
*Shell pieces.* G := F_cχ^{sh}_k is in (X1)'s class at λ = λ_k. For |γ| ≤ r := r_n, Leibniz splits ∂^γG over (F, cube factor,
shell factor) with multinomial weights summing to 3^{|γ|}. Bounds on supp G: λ_k^{|γ_3|}|∂^{γ_3}χ^{sh}_k| ≤ 2(C_Wn²)^r(r!)³
(Lemma W (c), both scales ≥ λ_k); |∂^{γ_2}Πχ_{c_i}| ≤ (16C_G^4)^nC_G^r(r!)²; and, for k ≥ 1, x ∈ supp G has dist(x, Δ_n) =
δ(x)/√2 < 2λ_k, so Taylor's formula from the nearest point of Δ_n (where all derivatives of F vanish) with M := p_n + 1 gives
|∂^{γ_1}F(x)| ≤ (4√n·λ_k)^M/M!·max_{|γ′|=|γ_1|+M} sup_{z∈[y,x]}|∂^{γ′}F(z)|. For such z, |z_i − c_i| ≤ 2 + 2λ_k ≤ 3, so
1 + |c_i|² ≤ 20(1 + |z_i|²), and (1 + |z|²)^{5n/2} ≥ Π_i(1 + |z_i|²)^{5/2}; hence sup_z|∂^{γ′}F(z)| ≤
20^{5n/2}Π_i(1 + |c_i|²)^{−5/2}|F|_{N_n}. (For k = 0 no Taylor step: the same with (4√nλ_k)^M/M! replaced by 1.) Collecting,
  ‖G‖_{λ_k,r} ≤ D_n·λ_k^M·Π_i(1 + |c_i|²)^{−5/2}|F|_{N_n} (k ≥ 1), D_n := 2·3^r(C_Wn²)^r(r!)^5(16C_G^4)^nC_G^r·20^{5n/2}
  ·(4√n)^{p_n+1}/(p_n + 1)!,
and (X1) gives |S(G)| ≤ A_nD_nλ_k^{M−p_n}Π_i(1+|c_i|²)^{−5/2}|F|_{N_n}; Σ_{k≥1}λ_k^{M−p_n} = Σ_k2^{−k} ≤ 1 and Σ_cΠ_i(1 + |c_i|²)^{−5/2}
≤ Z_5^n. So the shell part is ≤ σ′_n|F|_{N_n} with σ′_n := 2A_nD̄_nZ_5^n, D̄_n := D_n with the last factor replaced by
max(1, (4√n)^{p_n+1}/(p_n+1)!).
*Sub-lattice remainder.* F(1 − Ψ_{λ_K}) is supported in {δ < √2λ_K < 3c_*a}. Lattice points there are either in Δ_n (where F = 0)
or have a ≤ δ(x), dist(x, Δ_n) < 3c_*a ≤ … ; with (X0), Taylor of order M′ := q_Xn + 1 and the same weight argument,
  |S^{a,R}_n(F(1 − Ψ_{λ_K}))| ≤ (C_Xa^{−q_X})^n·(6√n·c_*a)^{M′}/M′!·32^n|F|_{N′_n}·(Z′)^n = ρ_n(a)|F|_{N′_n},
ρ_n(a) ≤ a·(32C_XZ′(6c_*)^{q_X})^n(6c_*)·(√n)^{M′}/M′! → 0.
*(ii)* In linear-growth form: r ≤ rn, p_n ≤ pn; n^{2rn} ≤ e^{2rn}(n!)^{2r}, (rn)! ≤ r^{rn}(n!)^r, (4√n)^{pn+1}/(pn+1)! ≤ C^n and
(√n)^{M′}/M′! ≤ 1; so σ′_n, sup_aρ_n(a) ≤ C^n(n!)^{b+2r+5r} ≤ e^C(n!)^{b+7r+1}; and N_n ≤ (r + p + 7)n, N′_n ≤ (q_X + 6)n.
*(iii)* Each shell piece converges by hypothesis; the shell sum is dominated, uniformly in a, by the summable Σ_k
A_nD_nλ_k^{M−p_n}(…); the remainder → 0. Dominated convergence for series gives convergence of the sum. ∎

**Proposition MIN (minimality: a power-law per-scale bound is NECESSARY). PROVEN-HERE.** Let a_j → 0, let 𝒦 ⊂ R^4 be a closed
ball, and suppose lim_jS^{a_j,R_j}_n(F) exists for every F in ^0𝒟_𝒦 := {F ∈ C^∞(R^{4n}) : supp F ⊂ 𝒦^n, F flat on Δ_n}
(defined for j ≥ j_0, once 𝒦 ⊂ B_{R_j/4}). Then there are C, N (depending on n, 𝒦) with
  |S^{a_j,R_j}_n(G)| ≤ C λ^{−N}‖G‖_{λ,N} for all j ≥ j_0, all λ ∈ (0, 1] and all G ∈ ^0𝒟_𝒦,
in particular for every G of (X1)'s class inside 𝒦^n; by translation invariance of the torus state the same C, N serve every
translate of 𝒦 inside B_{R_j/4}. *Proof.* ^0𝒟_𝒦 is a closed subspace of the Fréchet space C^∞_{𝒦^n}, hence Fréchet; each
S^{a_j,R_j}_n is a finite sum of point evaluations, hence continuous; pointwise convergence implies pointwise boundedness, so by
the Banach–Steinhaus theorem the family is equicontinuous: |S^{a_j,R_j}_n(G)| ≤ C max_{|γ|≤N}‖∂^γG‖_∞ ≤ Cλ^{−N}‖G‖_{λ,N}. ∎
**So (X1) with SOME n-dependent (A_n, p_n, r_n) is necessary and sufficient** for every sequence a → 0 to have a subsequence
converging on the whole flat test space (sufficient: EXT (i) + CLOSURE-sep (a); necessary: MIN). Fixed-separated control
alone is not enough (CODEX_REVIEW_SRCAN item 10's kernel of height a^{−8} on the shell at δ_a ≍ (log 1/a)^{−1/α} gives
|S(G)| ≍ a^{−8}δ_a^4‖G‖_∞ ≫ δ_a^{−N} for every N, violating MIN's necessary bound — agree with Codex's example and diagnosis).
The **linear-growth form** of (X1) is the additional content OS II's E0′ consumes (MIN does not produce it: Banach–Steinhaus
gives some N_n per n, with no control in n).

**Proposition GROW (the pointwise route; matching REC_LIB §16). PROVEN as a quantified implication.** First take Z=1, so
(X0) has q_X=4. Assume **(SEP-pt)**: there are fixed A_0,c_*>0 and b_0,q≥0, independent of a,R,n and placements, such that
for every 0<a≤1, admissible volume R, n≥2 and configuration x∈((aZ)^4∩B_{R/4})^n with δ(x)≥c_*a,
  |ω_{a,R}(Π_iê_a(x_i))| ≤ A_0^n(n!)^{b_0}Π_i w̄(δ_i(x)),    δ_i(x):=min_{j≠i}|x_i−x_j|,
  w̄(r):=min(r,1)^{-4}[log(2+1/min(r,1))]^q.
These are **unconditional moments** with a short-distance weight; no large-distance decay is assumed. Then, uniformly,
  |S^{a,R}_n(F)| ≤ C^n(n!)^{b_0}|F|_{10n+1}
for compact flat tests supported in (B_{R/4})^n. Thus (H_reg-sep) holds with **s=11, β=b_0+1, α=e^C**, enlarged if necessary;
centering gives S_1=0 and S_0=1 is fixed separately. Any common limit inherits E0′ by density.

*Proof and general crude-power dependence.* Suppose more generally |ê_a|≤C_Xa^{-q_X}, taking q_X≥0 without loss on 0<a≤1,
and let Q=ceil(q_X). The weighted lattice sum is bounded uniformly by
  a^{4n}Σ_x Π_i(1+|x_i|²)^{-5/2} ≤ (Z′)^n.
For δ<1 choose a closest pair and project it to its midpoint on Δ_n. The displacement h has |h|=δ/√2 and only eight
nonzero Cartesian coordinates, so ‖h‖_1≤2δ. Flatness and Taylor's formula, with the weight along that segment, give
  |F(x)| ≤ (2δ)^M/M! ·2^{5n/2}|F|_{M+5n}Π_i(1+|x_i|²)^{-5/2}.     (G-Taylor)
The midpoint projection is orthogonal, so |x|²−|z|²≤|h|²<1 along its normal segment; hence
1+|x|²≤2(1+|z|²). Also (1+Σ|x_i|²)^{5n/2}≥Π_i(1+|x_i|²)^{5/2}.
When c_*a≤1 split the sum: for δ≥1 use w̄(δ_i)=(log 3)^q and |F|_{5n}; for c_*a≤δ<1 use
Π_iw̄(δ_i)≤C_q^nδ^{-5n}, C_q:=sup_{0<r≤1}r[log(2+1/r)]^q<∞, and M=5n in (G-Taylor).
The latter region costs at most C^n(n!)^{b_0}|F|_{10n}. For 0<δ<c_*a use (X0) and M=Qn+1:
  a^{-q_Xn}δ^{Qn+1} ≤ c_*^{Qn+1}a^{(Q−q_X)n+1} ≤ c_*^{Qn+1}a.
Its sum costs at most aC^n|F|_{(Q+5)n+1}. At δ=0 flatness makes the summand zero. If c_*a>1, a is bounded below and the
crude bound with |F|_{5n} covers the entire sum. All constants above are to the nth power with fixed q_X,q,c_*; b_0≥0
absorbs the crude term. For Q=4 a safe common order is 10n+1≤11n. In general a safe common integer coefficient is
  **s=max(11,Q+6)**,
since 10n≤sn and (Q+5)n+1≤(Q+6)n. Finally C^n≤e^C n! gives β=b_0+1. This is the actual q_X dependence of the reviewed
pointwise producer; s=11 was not justified for unrestricted q_X by the old near-region estimate. ∎

**The conditional SRC-κ match.** To set b_0=p+2, the total-cumulance route needs, for every partition π of n labels into r
blocks, an outer joint-cumulant bound for its conditional block cumulants of the form
  A^n r! Π_{B∈π}(|B|!)^p Π_iw̄(δ_i),    p≥0,                       (G-outer)
with constants uniform in a,R,n and placements, and with singleton blocks INCLUDED (REC_LIB (16.4)). For each composition
n=k_1+⋯+k_r, ordered partitions number n!/(k_1!⋯k_r!)≤n!; there are 2^{n−1} compositions. Hence Σ_π|π|!≤2^{n−1}n!, so
unconditional cumulants have bound (2A)^n(n!)^{p+1} times the weights. The moment-cumulant sum has at most n! partitions,
Π_B|B|!≤n!, and subset weights are bounded by the corresponding full-configuration weights; explicit singleton bounds
are also needed. It therefore gives b_0=p+2. With Z=1 this yields s=11, β=p+3 **only under (G-outer)**.
Neither (G-outer) nor (SEP-pt) is proved for the actual Yang–Mills hierarchy here. Higher conditional SRC-κ cumulants alone
miss the conditional means and uniform all-order outer-product moments (CODEX_REVIEW_SRCCD §7; REC_LIB §16).
The separate SMEARED route must supply (X1) with its linear-growth, translation-, a- and R-uniform quantifiers before
EXT can supply E0′; integer majorants of any noninteger derivative-order parameters must be used. No numerical check or
status update establishes those estimates, their sphere analogues, or a mass gap.
**Large-distance control (Codex item 14's third clause).** It is exactly two things above: translation-uniformity of the local
input (cubes anywhere, constants independent of position, a and R) and the factorised weight Π_i(1 + |x_i|²)^{−5/2} extracted
from |F|_{sn}; no decay of correlations is used (agree with CODEX_REVIEW_P4 §4.2 and with Codex SRCCD §7's remark that OS0 can
hold without clustering).

## §4. (ALG) — one local algebra (ML1, minus the witness)

**Theorem ALG. PROVEN-HERE (definitions + Lemmas P, DENSE, ACT, RP-lat, DET).** The OS test space 𝒜 of D5, with the partial
product D6, the "state" D7 and the maps D8, carries:
- (i) **an E(4) action** by continuous linear maps (Lemma ACT) preserving 𝒜, 𝒜_𝒟 and flatness on Δ, with g·𝒜(O) = 𝒜(gO)
  (local covariance; isotony 𝒜(O_1) ⊂ 𝒜(O_2) for O_1 ⊂ O_2 is immediate);
- (ii) **a positive-half generating set for RP**: 𝒜_+ with the involution F ↦ ΘF^* and the cone {ΘF^* ⊗ F : F ∈ 𝒜_+} ⊂ 𝒜
  (Lemma P); its dense part 𝒜_{𝒟+} consists of limits of strictly local positive-half lattice observables A_F (D8, Lemma RP-lat);
- (iii) **a countable determining family for OS0**: D of D9. Two functionals obeying E0 that agree on D agree on 𝒜 (density +
  continuity); a sequence of lattice functionals obeying (H_reg-sep) and converging on D converges on 𝒜_𝒟, with limit obeying
  E0′ (CLOSURE-sep (a)-(b)); every sequence obeying (H_reg-sep) has such a subsequence (compactness);
- (iv) **conditional scalar reconstruction:** if the {e} hierarchy satisfies E0′, full E1, E2, E3, (Re) and S_0=1, REC (e)
  reconstructs it on ℋ_e. "Determining" here means determining this S on 𝒜. It does not identify ℋ_e with the full physical
  Yang–Mills Hilbert space; that identification, the full observable hierarchy and the full-target gap remain OPEN.
**Lemma DET (S on 𝒜 is fixed by its time-ordered values; contact data are not part of the reconstructed theory). PROVEN-HERE.**
If S, S′ obey E0, E1 (SO(4)) and E3 and agree on every F ∈ 𝒟_n supported in {x : t_i ≠ t_j ∀i ≠ j}, then S = S′ on 𝒜. Such
values are themselves reconstructed data: for H ∈ C_c^∞ supported in {t_1 < ⋯ < t_n} (after E3), translate to positive times
(E1), H′ := T_τH ∈ 𝒟_{+,n}, and S_n(H) = ⟨Ω, [H′]⟩.
*Proof.* Let F ∈ 𝒟_n with compact support K ⊂ R^{4n}\Δ_n. For x ∈ K the unit vectors e ∈ S³ with e·(x_i − x_j) = 0 for some
pair form a finite union of great 2-spheres, so some e(x) separates all times, and by continuity the same e does so on a
neighbourhood V_x. Cover K by finitely many V_l with rotations Λ_l (Λ_l e(x_l) = e_0); a smooth partition of unity on K
subordinate to {V_l} gives F = Σ_lFφ_l with Fφ_l ∈ 𝒟_n supported in V_l. Then S(Fφ_l) = S(Λ_l·(Fφ_l)) by E1, and
Λ_l·(Fφ_l) is supported where all times are distinct, where S = S′. So S = S′ on 𝒟_n, hence on ^0𝒮_n (density, continuity). ∎
**Consequence for the witness (compatibility with NONFREE55).** NONFREE55 has only its PRE-STATED block on disk (05:11Z); its T3
already asks for a witness "built on the observable algebra on which OS0-OS3 are produced (clover energy density e_a, smeared /
separated Schwinger distributions …)". The condition that makes a witness live on 𝒜 is (H_int-sep) of §2: a continuous
function of finitely many values S_{n_i}(φ_i), φ_i ∈ 𝒜_𝒟 (or a limit of such, with uniform control). By Lemma DET every such
witness is a function of the reconstructed Euclidean data, so it "survives the physical OS quotient" (PANEL_P1 item 4) and is
blind to contact terms (Codex R1, R13). This settles ASSEMBLY55 F1's algebra side for any witness of that form; whether such a
witness separates YM from the free class is NONFREE55's job.
**Larger families: the reviewed finite Cartesian tensor scope.** Fix a finite collection of real bosonic Cartesian
fields with total component space V=⊕_σ(R^4)^{⊗r_σ}, rank r_σ≤r_max<∞ (r_σ=0 permits scalars). Use
^0𝒮_n⊗V^{⊗n}, all mixed words, and the sum seminorm
  ‖F_n‖_{k,1}:=Σ_{a_1,…,a_n} max_{|γ|≤k} sup_x (1+|x|²)^{k/2}|∂^γF_n^{a_1…a_n}(x)|.
For Euclidean rotations D_E(R):=⊕_σR^{⊗r_σ}, tests transform by
  (g·F)_n(x)=[D_E(R^{-1})^T]^{⊗n}F_n(g^{-1}x)=[D_E(R)]^{⊗n}F_n(g^{-1}x).
The star conjugates and reverses BOTH positions and labels; reflection also includes J:=D_E(θ) on every slot. E2 is
positivity of the entire mixed-word form on all finite sequences. Separate positivity of each field species does not
supply it. E0′ must use one (s,α,β) for all n and words in this sum norm. Uniform componentwise scalar estimates give the
same sum-norm bound; a maximum-component norm instead introduces the component-count factor and must be converted.
The real-rotation component factor is bounded by 2^{r_max n}, to be retained in continuity estimates (REC_LIB §15).

The Wick/real-form dictionary is fixed, not guessed: B:=diag(i,1,1,1), C:=⊕_σB^{⊗r_σ}, jx=Bx. REC_LIB §15 and REC_CONT give
  W_n(jx)=C^{⊗n}S_n(x),    J²=1,    bar(C)J=C,
  D_M(Λ)=C D_E(B^{-1}ΛB)C^{-1}=⊕_σΛ^{⊗r_σ}
for proper orthochronous real Lorentz Λ. Minkowski tests transform by D_M(Λ^{-1})^T on each slot. These phases and real
structures are part of the Hermitian-field conclusion. Symmetric or antisymmetric tensor species may be carried as
redundant Cartesian components with their linear identities. An arbitrary abstract O(4) representation without this
complexification, reflection and Wick dictionary has no continuation theorem supplied here; that route remains UNPROVED.

To apply the scalar closure/extension arguments componentwise, the actual lattice fields must also have real components,
the matching reflection law J, finite local support ensuring eventual membership in the geometric half algebra, and the
SAME bare law and sequence. Their mixed-word bounds and all-order E(4) invariance must be proved uniformly. These hypotheses
are not supplied by naming a continuum representation. Under them the finite sum version uses the stated norm and the
reviewed reconstruction; it still does not construct or identify the full Yang–Mills hierarchy. Flowed fields at positive
four-dimensional flow time require a separate support/localisation argument; Lemma RP-lat alone does not include them.

## §5. (DIAG) — cited, not redone (coordinator; CODEX_REVIEW_ASSEMBLY R2 and bank item 1, PROVEN)

I agree with Codex R2's proof (re-read: choose R_j with the outer error < 2^{−j} on φ_1..φ_j, then a cutoff a_j < 1/j from R_j's
convergent subsequence with the inner error < 2^{−j}; joint error < 2^{1−j}; no rate uniform in R). Interface to this file only:
- The countable family is D of D9 (fixed, R-independent, G_0-closed). Enlarging it by countably many further tests (the
  witness tests φ_i, the transported tests g·φ) costs nothing; with D G_0-closed and S^∞ E(4)-invariant (CONTRACT-sep), the
  defects S^{(j)}(g·φ) − S^{(j)}(φ) → 0 along the diagonal, so the diagonal sequence also meets CLOSURE-sep's (H_Euc-sep) on
  D: the sphere route then feeds the flat contract along ONE lattice sequence.
- Convergence along the diagonal on all of 𝒜_𝒟 (not just on D) needs (H_reg-sep) uniformly along the diagonal, i.e. lattice
  bounds uniform in a and R jointly; with only per-R lattice bounds plus (U-sep) for the continuum S^R, the diagonal converges on
  D (and any countable set), which already determines S^∞ (Theorem ALG (iii)). Ward/N5 constants are never used along the
  diagonal (agree: CODEX_REVIEW_SPHERE bank item 5).

## §6. (TRAJ) — the one bare-coupling trajectory, and every input checked against it (ML12)

### 6.1 The trajectory, written once (each clause with its producer and status)
- **TR-0 (units, indices).** ℓ_ref := 1. L ≥ 3 odd. Levels k = 0 (spacing a) … K (spacing L^Ka = 1); so **a = L^{−K} ∈ L^{−ℕ}**
  (F-tune is stated for ε = L^{−K} only). u_k := 1/g_k²; g_bare := g_0 (level 0); g_ref := g_K. (PROOF §1 S1/S3 index
  resolutions the other way; its "g_K" is g_bare — conflict C-T8.)
- **TR-1 (tori).** Hypercubic, side **R ∈ 2ℕ**, R ≥ R_0 (then R/a = RL^K is even, as Lemma V and Lemma RP-lat require, and every
  level-k lattice has RL^{K−k} ∈ ℕ sites per side). The same trajectory for every R (TR-5).
- **TR-2 (kernel couplings; "fixed by FI-1").** Decision 4's soft kernel K_k between levels k and k+1 has stiffness κ·u_k^{ker},
  ONE κ for all levels (FLOW: "the kernel coupling in the stripped tower is the same κ at every level"). A5 ("the chain's own
  sequence", RLARGE §0) is the per-level fixed point u_{k+1}^{ker} = Φ_k(u_{k+1}^{ker}), Φ_k(x) := u_k − b_k − ρ_k(x)
  (RLARGE_U55 §3.1). Existence per level: Theorem FI-1 (CODEX_REVIEW_RLU item 2: CONFIRMED conditionally on (A-unif), (A-cont)
  and its γ condition). **Uniqueness and continuous dependence on g_bare — needed by F-tune's (SF-cont) — require (A-Lip)** (a
  sufficient condition; Codex RLU item 2: continuity alone does not give a continuous selection); OPEN.
- **TR-3 (effective couplings).** u_{k+1} := β[S_{k+1}] in infinite volume (FLOW "Def F-g"; (SF-∞)), along A5.
- **TR-4 (constants, in this order; FLOW "Lemma F-ind" + FI-1).** β_− := β_0′/2, R_F := 2R_0 (from (UNIV-1L) — or from the
  two-sided bracket (B-BR), HINT2_55 L4); then C_ρ; then **γ := min{γ_0, (β_0′log L/(2C_ρ))^{1/2}, γ_FI}**, where γ_FI is
  FI-1's new condition γ^{−2} ≥ max{2R_F, 2/min(1, κ)} + R_F + (3/2)β_0′log L; then **g_1 := (γ^{−2} + R_F)^{−1/2}**.
- **TR-5 (renormalised coupling).** g_ref ∈ (0, g_sink], **g_sink := SMALLNESS_DAG's Stage-7 sink** (below FLOW's g_1, (2R_F)^{−1/2},
  CL^J's min{1, √κ}/√2, RLF v3's threshold g_thr, HIST-sum's, (P5)'s and the existence lane's ceilings), fixed once for all
  a and R (so ℓ_ref is a fixed physical scale).
- **TR-6 (the bare coupling).** **g_bare(a; g_ref) := the smallest g_0 ∈ (0, γ] with u_K(g_0) = g_ref^{−2}** (FLOW "Theorem
  F-tune", conditional on (UNIV-1L), (SF-g), (RLF-δ), (SF-cont), (SF-∞); "γ, g_1, β_±, R do not depend on K or on the torus").
- **TR-7 (what every consumer may use; PROVEN-HERE as arithmetic from TR-4..6).** (F_R) on [0, K]:
  g_ref^{−2} + β_−(K − k)log L − R_F ≤ u_k ≤ g_ref^{−2} + β_+(K − k)log L + R_F; g_k ∈ (0, γ] for all k ≤ K; and
  **u_K − R_F ≥ γ^{−2} > 0** (because g_ref ≤ g_1 ⇔ g_ref^{−2} ≥ γ^{−2} + R_F). Hence the AF envelope of CODEX_REVIEW_UNIV §9,
  g_j² ≤ (g_*^{−2} + B(K − j))^{−1} with **g_*^{−2} := g_ref^{−2} − R_F ≥ γ^{−2}, B := β_−log L**, and Σ_{j≤K}g_j^q ≤
  g_*^q + 2g_*^{q−2}/(B(q − 2)) for q > 2; SRCAN55 SA-F's A := u_K − R_F > 0; g_bare → 0 as a → 0 (u_0 ≥ g_ref^{−2} +
  β_−log(1/a) − R_F); and the bound g_bare⁴ ≥ (C + β_+log(1/a))^{−2} used in Proposition FS.
- **TR-8 (sources).** η-tilted chains keep the η = 0 kernels (CODEX_REVIEW_SRCAN item 11: "leaves every kernel factor and its
  normalization untouched"), so A5 holds only at η = 0; stage estimates are needed OFF the fixed point — exactly FI-1's (A-unif)
  "for every kernel parameter x ∈ X_k". The tilted bare couplings stay in SA-F's polydisc |δu| ≤ r_src ≲ ρ/(2g_ref²) (SRCAN55).
- **TR-9 (sphere profile rule).** β_Q := 2N/G(aΩ(z_Q))² on K_a, G R-independent (U-alg). Three candidates, none of which is
  TR-6 itself, because TR-6 is defined only for L-adic spacings while the local spacing aΩ ranges over [a, 2a]:
  - (G-np/trajectory profile) G^{−2} := log-linear interpolation of TR-6 between consecutive L-adic spacings (SEAM55 §1.6:
    "interpolate linearly in log s, or use a continuous-a line of constant physics"); W0 then needs SEAM55's (LCS-a) AND
    (LCS-b), and the tuning-stability increments Δ_K (PROOF "E7.3 (tuning stability)") enter c_4 (SEAM55 §1.6);
  - (Ward profile, SEAM55 Theorem W0) dT/dlog s = −B_loc(T)/(1 + ϑ^p_1(T)), T(a) := u_traj(a) — needs only (LCS-a) but is a
    DIFFERENT function from TR-6, and its base spacing a must be L-adic for T(a) := u_traj(a) to be defined;
  - (G-pert) the two-loop formula — needs the value statement (UIR^♮ route) in addition (SEAM55 ranking).
  Every sphere RG input (flow, SRC, large fields on K_a) is then needed for the position-dependent profile: ML4 (FLOW-pos).

### 6.2 Every input checked against TR (file, locating string, verdict)
| # | File — locating string | Trajectory assumed | Verdict |
|---|---|---|---|
| T1 | FLOW — "Theorem F-tune" | g ∈ (0, g_1], g_0 ∈ (0, γ], a = L^{−K}, torus-free | defines TR-6; consistent |
| T2 | FLOW — "Def F-g"; "(SF-∞)" | infinite-volume β; torus-independent | = TR-3; consistent |
| T3 | RLARGE — "Flow hypothesis (F_R)" | "(F_R)_{[0,k]} … R ≥ 0 fixed", chain's own sequence | consistent (R ≡ R_F) |
| T4 | RLARGE — Theorem RLF v3 ("g_K ≤ g_0", "max{6θ, 24θ}(1 + 2Rg_K²) < 1") | threshold g_thr on g_ref; R ≡ R_F | consistent given TR-5 (g_thr ≥ g_sink); symbol collision g_0 (C-T8) |
| T5 | RLARGE — "(RLF-δ)_k" | g_0..g_k ∈ (0, γ_0], (F_R) on [0, k] | consistent (γ ≤ γ_0) |
| T6 | RLARGE_U55 — "Theorem FI-1" | kernel x = u_{k+1}^{ker}, window X_k, new γ condition | consistent only if TR-4 includes γ_FI (FLOW's γ alone does not): **C-T2** |
| T7 | FLOW — "(SF-cont)" in F-tune | g_0 ↦ u_{k+1}(g_0) continuous | needs (A-Lip) for the A5 sequence: **C-T3** |
| T8 | SRCCD55 §3.1 — "g_K = g_ref ≤ min(g_thr, γ_0) fixed (ROTDEF I3)"; ROTDEF — I3 row | g_ref ≤ min(g_thr, γ_0) | **C-T1**: γ_0 > γ ≥ g_1; F-tune gives no trajectory for g_ref ∈ (g_1, γ_0]; fix: g_ref ≤ g_sink |
| T9 | SRCCD55 §3.1 — "soft couplings κ_j ∈ [κ_-, κ_+]"; "R/a even and R/ℓ_ref ∈ ℕ" | level-dependent κ_j; even tori | **C-T4** (κ_j vs FLOW's one κ); tori consistent with TR-1 |
| T10 | HINT2_55 R2.1 — "F-tune's tuned sequence at fixed renormalised coupling g ∈ (0, g₁]" | TR-6 with g ≤ g_1; R_F pinned | consistent (TR-5 is stricter) |
| T11 | CODEX_REVIEW_UNIV §9 — "the explicit envelope g_j² ≤ (g_*^{-2} + B(n − j))^{-1}" | AF envelope | holds on TR (TR-7); ASSEMBLY55 N8's "g_ref² < 1/R must be imposed explicitly" is already implied by g_ref ≤ g_1 (see §7 V7) |
| T12 | SRCAN55 — "Under (F_R), u_0 ≥ u_K − R + β_−K log L"; SA-F; CODEX_REVIEW_SRCAN item 3 "A=u_K−R>0" | A > 0; lower propagation needs q_* < 1 | A > 0 holds (TR-7); q_j ≤ 2C_bγ⁴/ρ on TR, so the LOWER bound needs γ⁴ < ρ/(2C_b): **C-T5** (one more one-sided γ condition, only if that lower bound is consumed) |
| T13 | LARGE55 — "(F_R)'s upper bracket between levels 0 and K: u_* = u_K + R" | upper bracket | consistent |
| T14 | FLOW §10 / §19A — EXISTENCE H-Bal-1 "1/g² + β(K − k) log L ≤ 1/g_k² ≤ …" (R = 0 form) | R_F = 0 | form conflict (R_F > 0 in F-tune); FLOW §19A says every EXISTENCE use tolerates R — **NOT-VERIFIED** here (EXISTENCE not read) |
| T15 | SPHERE55 §1.4 — "(G-np) G = the bare coupling of the flat Wilson lattice on a line of constant physics fixed nonperturbatively (for instance by a flat-torus renormalization condition…)" | a G(s) for all s ∈ [a, 2a] | **C-T6**: TR-6 is defined on L^{−ℕ} only and its renormalisation condition is the RG-effective coupling at level K, not "a flat-torus renormalization condition"; an extension (TR-9) is required and W0 then needs LCS-a/LCS-b (SEAM55) |
| T16 | SEAM55 §1.5 — "T(a) := u_traj(a)" | Ward profile | **C-T7**: not TR-6 (different function off the base spacing); the sphere's local line of constant physics equals the flat one only under LCS-b; identifying the sphere limit with a flat Wilson selection (OWN-S4 strict reading) needs that extra input |
| T17 | PROOF §1 — "S1 Lattice … Λ_{j,M} = (L^-j Z / L^M Z)^4"; "S3 … β_K = 2N/g_K^2" | torus side L^M (odd site counts L^{M+K}); g_K = finest-resolution coupling | **C-T8**: L^M odd conflicts with TR-1 (Lemma V's sparse set (2aZ)^4 and the two-site-plane RP-lat need R/a even); and "g_K" there is g_bare, the opposite of FLOW's g_K |
| T18 | UNIV55/Theorem U (rotated lattice) | the comparison theory's own sequence | consistent for rational rotations in infinite volume (Def F-g is infinite-volume and the rotated infinite lattice is isometric); the finite-torus version needs a compatible torus — not checked |

**Conflicts, with fixes (the list ML12 asks for).**
- **C-T1** (SRCCD55/ROTDEF I3 range). Replace "g_ref ≤ min(g_thr, γ_0)" by "g_ref ∈ (0, g_sink]" (TR-5). Not a mathematical
  contradiction once g_thr is read as SMALLNESS_DAG's sink, but the literal γ_0 admits g_ref without an F-tune trajectory.
- **C-T2** (FI-1's γ). FLOW's γ must also obey FI-1's condition; write γ := min{…, γ_FI} (TR-4); SMALLNESS_DAG edges
  R → γ, κ → γ, L → γ (RLARGE_U55 §3.4).
- **C-T3** ((SF-cont) for the A5 sequence). F-tune's continuity hypothesis is not implied by FI-1's existence; add (A-Lip) (or a
  proved continuation argument; RLARGE_U55 §3.3's Browder route is ARGUED only).
- **C-T4** (κ_j). Fix κ_j ≡ κ (TR-2), or carry κ_j-uniformity through (UNIV-1L)'s b_k and FLOW's stripped tower.
- **C-T5** (SA-F lower bound). If the lower propagation bound is consumed, add γ⁴ < ρ/(2C_b) to TR-4.
- **C-T6/C-T7** (sphere). The sphere route does not share TR-6: its profile is an extension (log-linear interpolation, needing
  LCS-a + LCS-b) or SEAM55's Ward profile (LCS-a only, a different function). Either way the sphere's RG inputs need ML4.
- **C-T8** (PROOF §1 conventions). PROOF's L-adic torus sides give odd site counts (incompatible with Lemma V's setting and with
  Lemma RP-lat's two site planes; an odd torus has one site plane and one link plane, whose combined RP is not proved here) and
  PROOF's "g_K" is g_bare. Fix: TR-1's even sides; write g_bare explicitly wherever PROOF §1 is cited.

## §7. Verdicts on inherited claims touched by this file (refutations count as much as positives)
- **V1 — ASSEMBLY55 F2a, "the closure step survives … Bookkeeping for the restatement": REFUTED** (agree CODEX_REVIEW_ASSEMBLY
  R1). Correct statement: the closure survives only after (i) replacing "every positive-half polynomial" by the time-ordered
  positive half 𝒜_+, (ii) dropping ordinary positivity (not an OS axiom; unused by Theorem REC), (iii) proving the lattice-RP →
  limit → density bridge: Theorem CLOSURE-sep.
- **V2 — ASSEMBLY55 N9 / ML2: the ABSTRACT reconstruction producer is now available.** REC_LIB + REC_CONT supply REC (e)
  under E0′ and the exact scalar/finite Cartesian tensor contract above (REVIEW2_REC). The old literature-only MISSING
  description is superseded at that scope. The actual Yang–Mills input hierarchy, all-order uniform growth and singleton
  controls are still OPEN. GROW supplies only the quantified implication: Z=1 and unconditional (SEP-pt) give s=11,
  β=b_0+1; β=p+3 additionally needs (G-outer). This consumer correction is pending fresh independent review.
- **V3 — SRCCD55 §2.2, "OS's axiom E0 places the Schwinger functions in the dual of ^0𝒮 … OS II adds the linear growth
  condition E0′ [m]": CONFIRMED against [KQR] and [AMT] ([m-sec]).**
- **V4 — SRCCD55 §2.2, "So OS0 for the point-like field e needs: (a) pointwise bounds on separated n-point functions …":
  REFUTED as a necessity claim.** Pointwise bounds are sufficient (GROW); the necessary and sufficient input is the smeared,
  per-scale (X1) (MIN + EXT), and E0′ additionally needs (X1)'s linear-growth quantifiers. Its clause "It does not need
  coincident-point counterterms (H-src′-diag)" is CONFIRMED (Lemma P; Theorem REC).
- **V5 — SRCCD55 Proposition E(b), "|S^a_n(F)| ≤ C_2^n(n!)^{p+2}‖F‖_{𝒮,4n+5}": NOT-VERIFIED as printed** (agree CODEX_REVIEW_SRCCD
  §7: exponent and seminorm not established from the stated hypotheses). GROW proves |S| ≤ C^n(n!)^{b_0}|F|_{10n+1} from
  Z=1 and unconditional (SEP-pt) with uniform constants and short-distance weight w̄; for general q_X use GROW's
  s=max(11,ceil(q_X)+6) after taking q_X≥0. The order 4n+5 is not derived or claimed.
- **V6 — SRCCD55 Proposition E(c) (subsequence on a countable dense set, then all F, same bounds): CONFIRMED** given uniform
  bounds (CLOSURE-sep (a)-(b)); agree with Codex SRCCD §7's "CONFIRMED, only as a downstream functional-analytic implication".
- **V7 — ASSEMBLY55 N8, "the envelope … follows from (F_R)'s lower half iff u_K > R … i.e. g_ref² < 1/R must be imposed
  explicitly": the "iff" is CONFIRMED (R = R_F); "must be imposed explicitly" is REFUTED as an extra condition** — it is
  implied by F-tune's own range g_ref ≤ g_1 (u_K − R_F ≥ γ^{−2}, TR-7); it needs stating only where a consumer quotes a weaker
  range (C-T1). Citation: the condition "A = u_K − R > 0" is CODEX_REVIEW_SRCAN **item 3** (SA-F), not item 6 (SA-RW) as
  ASSEMBLY55 N8 and F14 cite (REFUTED as a citation; content agrees).
- **V8 — ASSEMBLY55 N7/F6/ML3, "(DIAG) OPEN, standard, unwritten": superseded** by CODEX_REVIEW_ASSEMBLY R2 (PROVEN; bank item 1)
  — agree; interface in §5.
- **V9 — ASSEMBLY55 ML9's diagnosis (fixed-separated control is not enough): CONFIRMED**, and made precise: (X1) is necessary
  (MIN) and sufficient (EXT); the Codex kernel example violates MIN's necessary bound.
- **V10 — HANDOFF "The architecture": "H_reg — cutoff- and volume-uniform moment bounds for a determining observable family":
  REFUTED as a formulation for the clover field** (Proposition FS on tori). Correct: (H_reg-sep) (§2).
- **V11 — PANEL_P1 §3 "PROVEN — Assembly from this contract": CONFIRMED in its banked scope** (Codex bank item 5) and **not
  applicable** to point-like e, whose "joint observable moments" cannot be cutoff-uniformly bounded with a non-vacuous
  normalisation (FS); CLOSURE-sep replaces it for the separated formulation.
- **V12 — CODEX_REVIEW_P4 §4.1-§4.2 (contraction and local-to-global with unit-ball moments): CONFIRMED as conditional** (agree);
  their moment hypothesis is unattainable for point-like e on tori (FS); CONTRACT-sep is the separated version.
- **V13 — SPHERE55 §5.4 "(U-mom)": incompatible with non-vacuity on tori (FS); NOT-VERIFIED on K_a** (Lemma V not transferred);
  replace by (U-sep) in either case (weaker, and sufficient by CONTRACT-sep).
- **V14 — [S26-BANKED] sphere line, "most dangerous: whether fine-field moment hypotheses and a normalisation keeping separated
  correlations nonzero can hold together" (CODEX_REVIEW_SPHERE F12): answered on tori — they cannot (FS);** on K_a expected
  (Lemma V's mechanism is local) but NOT-VERIFIED. The formulation therefore must be the separated one.
- **V15 — SEAM55 §1.6, "interpolate linearly in log s, or use a continuous-a line of constant physics": CONFIRMED as necessary**
  (TR-6 is defined on L^{−ℕ} only).
- **V16 — ASSEMBLY55 ML12, "the sphere profile rule declared to be (G-np)": REFUTED as sufficient** — declaring (G-np) does not
  produce G from TR-6 (C-T6); SEAM55's Ward profile is a different function (C-T7).
- **V17 — ASSEMBLY55 N8, "torus consumers: MATCH-cond — all read F-tune's g_0(a; g_ref) at ℓ_ref = 1": CONFIRMED**, with the
  quantifier fixes C-T1..C-T5 and C-T8.
- **V18 — HANDOFF Rules, "Wilson reflection positivity on the torus is IMPORTED-AND-REVERIFIED": CONFIRMED for the case used**
  (Lemma RP-lat re-derived for site reflection with two site planes, R/a even); the odd-torus (mixed site/link) case is not
  covered here (C-T8).

## §8. Checks
- **checks/ol55_1** (criteria `ol55_1_criteria.md` written before `ol55_1_conventions.py`; run `python3 -I`, exit 0, empty
  stderr; output `ol55_1_out.txt`): **PASS.** G1: 24 unordered / 48 ordered-pair clover plaquettes per site in Z⁴, max a⁴e_a = 24
  (control X1: Z³ gives 12, fires). G2: (2n)^{5n} ≤ ((5n)!)² for n = 1..100 (control X2: the false (2n)^{5n} ≤ ((2n)!)² fails,
  fires). G3: the OS form equals ⟨Θ(A)^*A⟩, real and ≥ 0, on 200 random complex-rational sequences for a reversible chain
  (controls: dropping the conjugation changes the value — fires; the cyclic chain gives −1/3 < 0 — fires).
  **Historical evidence scope (results and criteria unchanged):** G3 is insensitive to insertion reversal in the commuting
  scalar moment sum, so it checks neither reversal admissibility nor the mixed-label/support convention (REVIEW2_REC finding 2).
  G1 is a conservative termwise bound/count, not a proof that the SU(N) clover upper envelope is attained. These toy results
  supply no Yang–Mills estimate or reconstruction premise. This consumer correction runs no new numerical diagnostic.

## §9. Summary table (every claim of this file and every inherited claim touched)
| # | Claim | Where | Verdict / status |
|---|---|---|---|
| 1 | Proposition FS: ordinary moments of smeared point-like e impossible with non-vacuous normalisation + uniform separated bound (tori) | §1.1 | PROVEN-HERE (⇐ banked Lemma V + F-tune bracket) |
| 2 | Decision: separated Schwinger distributions on ^0𝒮 (OS I/II formulation) | §1.1 | forced on tori by 1; adopted everywhere |
| 3 | Definitions D1-D9: 𝒜, partial product, RP form, E(4) action, normalisation/support/observable maps, determining family | §1.2 | definitions |
| 4 | Lemma P (RP form never meets a coincidence) | §1.2 | PROVEN-HERE |
| 5 | Lemma DENSE (𝒟 dense in ^0𝒮; 𝒟_+ dense in 𝒮_+) | §1.2 | PROVEN-HERE |
| 6 | Lemma ACT (continuous E(4) action) | §1.2 | PROVEN-HERE |
| 7 | Axioms E0′, E1, E2, E3, (Re), S_0=1 as used | §1.3 | Exact REC_LIB contract; historical OS literature attribution [m-sec] |
| 8 | Theorem REC (a) Hilbert space, (b) semigroup, (c) E(3), (d) Euclidean field operators from separated distributions | §1.4 | PROVEN-HERE |
| 9 | Theorem REC (e), including continuation under E0′ | §1.4, §4 | Reviewed abstract REC_LIB + REC_CONT producer for scalars / finite Cartesian tensors; consumer alignment pending fresh review; actual YM inputs OPEN |
| 10 | Reply to Codex R1 (repair = different positive half; ordinary positivity unneeded) | §1.5 | agree with R1; repair = items 4, 8, 12 |
| 11 | Scalar OS formulation versus the full physical target | §1.6 | Intermediate hierarchy only; no owner decision shrinking the full target |
| 12 | Lemma RP-lat (site-reflection RP, R/a even) | §2 | PROVEN-HERE (standard) |
| 13 | Theorem CLOSURE-sep | §2 | PROVEN-HERE (implication) |
| 14 | (H_int-sep) compatibility condition for witnesses | §2 | PROVEN-HERE (passage to the limit) |
| 15 | Corollary CONTRACT-sep (sphere flat limit in separated form; ML8 second half) | §2 | PROVEN-HERE (implication; inputs (U-sep), (K-inv) OPEN) |
| 16 | (X0) clover bound |ê_a| ≤ 24a^{−4}/Z | §3 | PROVEN (+ ol55_1 G1) |
| 17 | Lemma W (Gevrey partitions) | §3 | PROVEN-HERE |
| 18 | Theorem EXT (sufficiency; linear growth s′ = max(r+p+7, q_X+6), β′ = b+7r+1; exchange of limits) | §3 | PROVEN-HERE (implication; input (X1) OPEN) |
| 19 | Proposition MIN ((X1) necessary for convergence on flat tests) | §3 | PROVEN-HERE |
| 20 | GROW: Z=1 gives s=11, β=b_0+1; general q_X gives s=max(11,ceil(q_X)+6) | §3 | Quantified implication; unconditional all-order (SEP-pt) OPEN; β=p+3 also requires (G-outer), including singletons |
| 21 | Theorem ALG (ML1 minus witness) + Lemma DET | §4 | PROVEN-HERE |
| 22 | DIAG interface | §5 | cites Codex R2 (PROVEN) |
| 23 | TR-0..TR-9 (the trajectory) | §6.1 | written; TR-7 arithmetic PROVEN-HERE; TR-2/TR-6 inputs OPEN |
| 24 | Conflicts C-T1..C-T8 | §6.2 | 8 conflicts listed with fixes (T14 NOT-VERIFIED) |
| V1 | ASSEMBLY55 F2a "bookkeeping" | §7 | REFUTED |
| V2 | ASSEMBLY55 N9/ML2 "MISSING" | §7 | Abstract producer available; YM application OPEN under the explicit contract |
| V3 | SRCCD55 §2.2 E0/E0′ recollection | §7 | CONFIRMED [m-sec] |
| V4 | SRCCD55 §2.2 "OS0 … needs pointwise bounds" | §7 | REFUTED (necessity); "no counterterms" CONFIRMED |
| V5 | SRCCD55 Prop. E(b) exponent/seminorm | §7 | NOT-VERIFIED |
| V6 | SRCCD55 Prop. E(c) | §7 | CONFIRMED (given uniform bounds) |
| V7 | ASSEMBLY55 N8 "g_ref² < 1/R must be imposed explicitly"; item-6 citation | §7 | iff CONFIRMED; extra-condition REFUTED; citation REFUTED |
| V8 | ASSEMBLY55 DIAG "OPEN" | §7 | superseded (Codex R2) |
| V9 | ASSEMBLY55 ML9 diagnosis | §7 | CONFIRMED (made precise) |
| V10 | HANDOFF "H_reg — … moment bounds" | §7 | REFUTED (for the clover field) |
| V11 | PANEL_P1 §3 assembly | §7 | CONFIRMED in banked scope; not applicable to separated formulation |
| V12 | CODEX_REVIEW_P4 §4.1-4.2 | §7 | CONFIRMED conditional; hypothesis unattainable on tori |
| V13 | SPHERE55 (U-mom) | §7 | incompatible on tori (FS); NOT-VERIFIED on K_a |
| V14 | banked sphere "most dangerous" item | §7 | answered on tori (FS); NOT-VERIFIED on K_a |
| V15 | SEAM55 §1.6 interpolation remark | §7 | CONFIRMED |
| V16 | ASSEMBLY55 ML12 "(G-np) declared" | §7 | REFUTED as sufficient |
| V17 | ASSEMBLY55 N8 torus MATCH-cond | §7 | CONFIRMED with fixes |
| V18 | HANDOFF torus RP "IMPORTED-AND-REVERIFIED" | §7 | CONFIRMED for the case used |
**Historical counts (original V1-V18 review ledger; not recomputed or promoted by this correction):** CONFIRMED 9 (V3, V6, V9, V11, V12, V15, V17, V18, plus V7's "iff" part counted with V7 below);
REFUTED 5 (V1, V4-necessity, V7-extra-condition + its citation, V10, V16); NOT-VERIFIED 3 (V5, V13-on-K_a, V14-on-K_a);
closed/superseded 2 (V2, V8). (V7 contains one CONFIRMED and two REFUTED parts; V4 one REFUTED and one CONFIRMED part; V13/V14
are refutations on tori and NOT-VERIFIED on K_a.) **New results of this file:** 16 PROVEN-HERE items (1, 4-6, 8, 12-21, 23's
arithmetic), 1 then-IMPORTED [m-sec] (9), 1 then-proposed owner decision (11). Current rows 9 and 11 above supersede those two
historical descriptions; the present source correction claims no new independent review verdict or whole-file certification.

## §10. Codex verdicts used — agree or disagree (each read as on disk at the time stated in §0)
| Codex file, item | Used for | Mine |
|---|---|---|
| ASSEMBLY R1 (F2a not bookkeeping; e(f)² example; contact example) | §1.5, V1 | **agree**; the repair is a different positive half (𝒜_+) plus CLOSURE-sep, not an extension |
| ASSEMBLY R2 + bank item 1 (DIAG PROVEN) | §5, V8 | **agree** (re-read the proof); not redone |
| ASSEMBLY bank item 5 (PANEL_P1 closure only in original form) | §2, V11 | **agree**; CLOSURE-sep is the separated re-proof |
| ASSEMBLY R12 dispositions ML1, ML2, ML3, ML9, ML12 | §1-§6 | **agree** as of its writing; this file updates each |
| ASSEMBLY R13 (flowed one-point statistic not an OS invariant) | §1.1, §4 | **agree**; Lemma DET shows witnesses of the (H_int-sep) form are OS-intrinsic |
| ASSEMBLY ordered items 1, 12, 14 | §1-§3, §6 | addressed (item 1: §1-§2; item 14: §3; item 12: §6) |
| SRCCD item 3 (Lemma V, scoped incompatibility) | Prop. FS | **agree** |
| SRCCD §7 (Prop. E NOT-VERIFIED; downstream CONFIRMED) | §3, V5, V6 | **agree**, incl. the repaired weight w̄; GROW supplies the exponent/seminorm Codex found unestablished |
| SRCAN item 3 (SA-F; A = u_K − R > 0; lower bound needs q_* < 1) | TR-7, C-T5, V7 | **agree** |
| SRCAN item 10 (uniform extension estimate; kernel counterexample; shrinking radii) | §3, V9 | **agree**; MIN makes "uniform extension estimate" a necessary condition |
| SRCAN item 11 (fixed kernels under sources) | TR-8 | **agree** |
| P4 §4.1-§4.3 (contraction; local-to-global; safe order) | CONTRACT-sep, V12 | **agree**; moment hypothesis replaced by (U-sep) |
| SPHERE F7 (pair ⇒ all-order invariance fails) | (K-inv), (H_Euc-sep) | **agree**: all-order inputs are stated |
| SPHERE F12 (moment vs normalisation) | FS, V13, V14 | **agree**; FS settles it on tori |
| SPHERE F14 + bank item 5 (Ward constants per R) | §5, CONTRACT-sep | **agree** |
| RLU item 2 (FI-1 existence; (A-Lip) sufficient, not necessary; continuity alone insufficient) | TR-2, C-T3 | **agree** |
| UNIV §9 (AF envelope as a hypothesis) | TR-7, T11 | **agree**; the envelope holds on the trajectory |
No Codex verdict used here is disputed.

## §11. What should change in PROOF.md's tally / HANDOFF's critical path (the lead edits; nothing here is banked)
1. **Tally: no change** (glue lemmas, pending Codex; no tally item is proved).
2. **Reconstruction interface:** the actual common hierarchy must satisfy uniform (H_reg-sep) on flat tests, S_0=1, (Re),
   symmetry, full all-order E(4) invariance and mixed-word RP. For the scalar clover field, geometric RP-lat supplies its
   eventual compact-support lattice RP step; it supplies neither growth nor full Euclidean invariance. The reviewed abstract
   REC_LIB + REC_CONT implication then applies. The full target of existence and a physical mass gap remains OPEN.
3. **ASSEMBLY55 §9 item 18:** the remaining input is actual cutoff/volume-uniform E0′ for ONE common YM hierarchy: via (X1)
   and EXT with all linear-growth and translation/separation quantifiers, or via unconditional (SEP-pt) and GROW with the
   correct q_X-dependent order. The s=11, β=p+3 specialization uses Z=1 and (G-outer), including singleton/outer-product
   controls. These estimates are OPEN; the abstract reconstruction theorem is available. A separate no-E0′ or arbitrary
   representation route is still unproved, not a substitute for the reviewed contract.
4. **Sphere row**: replace (U-mom) by (U-sep); the flat limit is CONTRACT-sep (pending Codex); the banked "most dangerous" item
   (moment vs normalisation) is answered on tori by FS.
5. **DIAG**: banked (Codex R2); remove it from the open list (agree with Codex's corrected list item 17).
6. **Trajectory**: record TR-0..TR-9 and C-T1..C-T8; in particular g_ref ≤ g_sink (not min(g_thr, γ_0)), FI-1's γ condition in
   γ, (A-Lip) for (SF-cont), one κ, even tori, and the sphere profile as a separate object needing ML4 (+ LCS-a, and LCS-b if
   the interpolated trajectory is used).

## §12. Errata (append-only; each overrides the text it names)
- **E1 (quotations; the only in-place edits of this file).** For the copyright limit (at most one short quotation), two
  sentences were edited in place right after being written (05:2xZ): §0 (L2) now quotes only "sit at separated positions"
  ([KQR] §2.2), and §1.5's second [KQR] quotation was turned into a paraphrase with its correct locator (§2.2, text after
  (2.15), not "Remark 2.4"). No mathematical content changed.
- **E2 (CLOSURE-sep at fixed R).** For R_j ≡ R, read 𝒟_n, ^0𝒮_n and D_n as the subspaces of functions supported in (B̄_{R/8})^n
  (and a countable dense subset of that 𝒟_n); conclusion (a) extends S_n to the closure of that subspace, not to all of ^0𝒮_n;
  (c) is dropped; E0′ in its global form needs R_j → ∞.
- **E3 (Lemma ACT).** |F|_{k+1} suffices in the continuity estimate (|F|_{k+2} was written; true but weaker).
- **E4 (§9 counts).** Clean count over the 21 claim-parts of V1-V18: **CONFIRMED 10** (V3, V4b "no counterterms", V6, V7a "iff",
  V9, V11, V12, V15, V17, V18), **REFUTED 6** (V1, V4a necessity, V7b extra condition, V7c citation, V10, V16), **NOT-VERIFIED 3**
  (V5, V13, V14 — the last two on K_a; their torus analogues are refuted by FS), **superseded/closed 2** (V2, V8). This replaces
  the "Counts" paragraph of §9.

Completed (UTC, from date -u just before this line): see next line.
Completed: 2026-10-29T05:20:26Z

### Errata from a full re-read (append-only; 2026-10-29 ≈05:25Z; each item overrides the text it names)
- **E5 (Theorem EXT, range of a).** The decomposition is used for a ∈ (0, a_0], a_0 := 1/(4c_*) (so K ≥ 1 exists and the
  remainder region lies within distance < 1 of Δ_n, which the weight comparison 1 + |x|² ≤ 4(1 + |z|²) uses). For a ∈ (a_0, 1],
  (X0) alone gives |S^{a,R}_n(F)| ≤ Σ_xa^{4n}|F(x)|(C_Xa^{−q_X})^n ≤ (C_Xa_0^{−q_X}Z′)^n|F|_{5n}, a constant of the form C^n; so
  EXT (i)-(ii) hold for all a ∈ (0, 1] after enlarging α′ by that factor. In the remainder paragraph, the dangling "dist(x,
  Δ_n) < 3c_*a ≤ …" reads "dist(x, Δ_n) = δ(x)/√2 < 3c_*a".
- **E6 (Proposition MIN, translates).** "the same C, N serve every translate of 𝒦" should read: the constants obtained for the
  larger ball 𝒦′ := 𝒦 + B_2 serve every translate of 𝒦 inside B_{R_j/4 − 2} (lattice translations by a_jZ^4 are exact; the
  residual shift, of length ≤ 2a_j ≤ 2, keeps supports inside 𝒦′ and does not change ‖·‖_{λ,N}).
- **E7 (CONTRACT-sep, improper rotations).** E1 for the full E(4) also uses the exact θ_μ-symmetry of K_a and of its radial
  profile (banked "reflection-paired lattice action"), which gives S^R(θ_μ·F) = S^R(F); without it the conclusion is E1 for
  SO(4) ⋉ R^4, which is what OS reconstruction uses [m-sec].
- **E8 (CONTRACT-sep, (RP-pole)).** "passed to S^R by CLOSURE-sep (d)" means CLOSURE-sep (d)'s argument with Lemma RP-lat replaced
  by the banked finite-cutoff RP of K_a for θ_μ (same three ingredients: exact RP on strictly local half-algebra observables,
  Lemma P, Lemma DENSE).
- **E9 (Lemma RP-lat, wording).** "(s(U^{-1}) = s(U) absorbs orientation)" belongs to the temporal plaquettes that θ maps to
  their mirror images (with reversed orientation); the plaquettes inside a fixed plane are fixed pointwise by θ.

Re-read completed (UTC):
2026-10-29T05:22:13Z

---

## §13. The bridge: separated products → a positive OS functional on the full algebra 𝒜 (coordinator's request, 05:26Z)

*Added after reading CODEX_REVIEW_SEAM (complete on disk, 238 lines): Finding 9 ("separated products do not determine the full
observable algebra"; "Single most dangerous unverified bridge: a nontrivial, positivity-compatible observable algebra
extending the separated products") and bank item 6 (the sphere H_Euc assembly is CONDITIONAL on "a precise
positivity/regularity/contact-domain bridge"); bank item 5 (joint diagonal + invariance on the separated domain, PROVEN).
Refutation criteria for this section (stated before the proofs below): an F ∈ ^0𝒮_n not approximable by separated products;
a family obeying the stated separated-product input whose extension to 𝒜 is not continuous or not RP on 𝒜_+; or a step that
uses a value at a coincident configuration.*

**Separated products.** 𝒫_n := span{f_1 ⊗ ⋯ ⊗ f_n : f_i ∈ C_c^∞(R^4; C), supports pairwise disjoint} ⊂ 𝒟_n. For λ > 0,
𝒫_n(λ) := the same with dist(supp f_i, supp f_j) ≥ λ for i ≠ j. On the lattice, S^{a,R}_n(f_1 ⊗ ⋯ ⊗ f_n) =
ω_{a,R}(Π_iÕ_a(f_i)) with Õ_a(f) := Σ_xa⁴f(x)ê_a(x) — exactly SEAM55's family 𝔉 ("finite products … of centred smeared energy
densities with mutually separated supports").

**(SP_λ) — the separated-product input with its separation quantified (the form the RG must deliver).** There are A, b, p, r ≥ 0
and c_SP ≥ 1 such that for all a ∈ (0, 1], R ≥ 32, n ≥ 2, λ ∈ [c_SPa, 1] and all f_1, …, f_n ∈ C_c^∞(R^4; C), each supported in
a cube of side 2 inside B_{R/4}, pairwise at distance ≥ λ:
  |S^{a,R}_n(f_1 ⊗ ⋯ ⊗ f_n)| ≤ A^n(n!)^b λ^{−pn} Π_i ‖f_i‖_{λ,r},  ‖f‖_{λ,r} := max_{|γ|≤r} λ^{|γ|}‖∂^γf‖_∞,
and the same with λ = 1 for separations ≥ 1. These are UNCONDITIONAL moment bounds. The following are sufficient stronger
inputs, not equivalent formulations of (SP_λ):

(a) Fix the actual coarse marginal ν and its conditional law. For every admissible separated family above and EVERY
nonempty block B of its labels, INCLUDING |B|=1, assume the uniform conditional-cumulant bound
  ess sup_V |κ_V(Õ_a(f_i):i∈B)| ≤ A^{|B|}(|B|!)^b λ^{−p|B|} Π_{i∈B}‖f_i‖_{λ,r}.
The essential supremum is with respect to ν. The same A,b,p,r must work for all blocks, cutoffs, volumes, degrees and
placements, with the same λ as the full family; singleton separation is vacuous and the displayed singleton bound is an
explicit extra hypothesis. The conditional moment identity is
  E[Π_iÕ_a(f_i)|V] = Σ_π Π_{B∈π}κ_V(Õ_a(f_i):i∈B).
For each partition, Π_B|B|!≤n!, Σ_B|B|=n and b≥0. There are at most n! partitions, so its absolute value is bounded ν-a.s.
by A^n(n!)^{b+1}λ^{−pn}Π_i‖f_i‖_{λ,r}. Averaging proves (SP_λ) with exponent b+1. Unconditional centering does not bound
the conditional first cumulant; the n≥2 conditional estimates alone do not justify this implication.

(b) The coarse-image moment form sup_V|E_{a,R}[Π_iÕ_a(f_i)|V]|≤the original right side, for every coarse field V where the
chosen conditional law is defined, implies (SP_λ) with exponent b by averaging (|ν(E[F|V])|≤sup_V|E[F|V]|). An essential
supremum suffices as well. This is the shape of SEAM55's (SRC-E′_∞) with the separation and n quantified; it is stronger
than the unconditional bound. Neither (a)'s singleton-inclusive estimate nor (b) is established for Yang–Mills here.

SEAM55's (H2) ("U-sep at the lattice level … for separated supports, with A, b, p independent of R ≥ R_0
and a ≤ a_0(R)") is (SP_λ) only if its seminorm p carries this explicit power of λ uniformly for λ ∈ [c_SPa, 1]; with
separation-dependent but unquantified constants it is NOT enough (CODEX_REVIEW_SRCAN item 10's kernel satisfies every
fixed-separation bound eventually and still diverges on a fixed flat test).

**Lemma TP (tensor-product expansion at scale λ). PROVEN-HERE.** Let λ ∈ (0, 1], μ := λ/16, n ≥ 2, r ≥ 0, M := (r + 4)n + 2,
and G ∈ C_c^∞(R^{4n}) supported in (Q_1 × ⋯ × Q_n) ∩ {δ(x) > λ} (Q_i cubes of side 2). Then
  G = Σ_cΣ_{k∈Z^{4n}} ĝ_c(k)·h^c_{1,k_1} ⊗ ⋯ ⊗ h^c_{n,k_n}   (absolutely and uniformly; also in 𝒮),
where c runs over the ≤ (35/λ)^{4n} points of (μZ^4)^n with Π_i(c_i + [−μ, μ]^4) ∩ supp G ≠ ∅,
h^c_{i,k}(y) := η((y − c_i)/μ)e^{πik·(y−c_i)/(2μ)}, η(z) := Π_{ν=1}^4ψ̃(z^ν) with ψ̃ ∈ C_c^∞((−2, 2)) a Gevrey-2 bump equal to 1
on [−1, 1] (built from Lemma W (a)); for each c the n factors are supported in c_i + [−2μ, 2μ]^4 and are **pairwise at distance
≥ λ/4**; and
  Σ_cΣ_k|ĝ_c(k)|Π_i‖h^c_{i,k_i}‖_{λ/4,r} ≤ C_TP^n(n!)^{(5r/2)+8}λ^{−4n}‖G‖_{λ,M}   (C_TP depends only on r).
*Proof.* (i) *Localisation.* With χ^μ_c(y) := Π_νφ((y^ν − c^ν)/μ) (Lemma W (d) rescaled; Σ_cχ^μ_c = 1, supp ⊂ c + [−μ, μ]^4),
G = Σ_cG_c, G_c := GΠ_iχ^μ_{c_i}(x_i). If G_c ≠ 0 there is x ∈ supp G with |x_i − c_i| ≤ 2μ (half-diagonal of a cube of side
2μ in R^4), so |c_i − c_j| > λ − 4μ = 3λ/4; the enlarged cubes c_i + [−2μ, 2μ]^4 (half-diagonal 4μ) are then pairwise at
distance > 3λ/4 − 8μ = λ/4. Each Q_i contains ≤ (2/μ + 3)^4 ≤ (35/λ)^4 relevant centres. (ii) *Fourier.* G_c vanishes off the
inner box Π_i(c_i + [−μ, μ]^4); its 4μ-periodic extension G_c^per is smooth, and G_c(x) = Π_iη((x_i − c_i)/μ)·G_c^per(x)
for all x (η = 1 on the inner box, η vanishes off the outer box, and G_c^per = 0 on the outer box minus the inner box). Expanding
G_c^per = Σ_kĝ_c(k)e^{πik·(x−c)/(2μ)} gives the displayed separated products. (iii) *Coefficients.* For k ≠ 0 pick ν with
|k_ν| = |k|_∞ and integrate by parts M times in x^ν (periodicity, no boundary terms): |ĝ_c(k)| ≤ (2μ/(π|k|_∞))^M‖∂_ν^MG_c‖_∞ ≤
2^M(1 + |k|_∞)^{−M}max_{|γ|≤M}μ^{|γ|}‖∂^γG_c‖_∞ (also for k = 0); by Leibniz and Lemma W (d), μ^{|γ|}‖∂^γG_c‖_∞ ≤
2^M(16C_G^4)^nC_G^M(M!)²‖G‖_{λ,M} (μ ≤ λ). (iv) *Factors.* (λ/4)^{|γ|}|∂^γh^c_{i,k}| ≤ C_h^{r+1}(r!)²(1 + |k|)^r for |γ| ≤ r
((λ/4)·(π|k|/(2μ)) = 2π|k|; (λ/4)/μ = 4), so Π_i‖h^c_{i,k_i}‖_{λ/4,r} ≤ C_h^{n(r+1)}(r!)^{2n}(2√n)^{rn}(1 + |k|_∞)^{rn}. (v) *Sum.*
Σ_k(1 + |k|_∞)^{rn−M} = Σ_{m≥0}#{|k|_∞ = m}(1 + m)^{−4n−2} ≤ 2^{4n}Σ_m(1 + m)^{−2} ≤ 2^{4n+1}. Multiplying: the bound, with
(M!)² ≤ C^n(n!)^{2r+8} and (2√n)^{rn} ≤ C^n(n!)^{r/2}. Convergence in 𝒮: finitely many c, a fixed compact support, and
coefficients decaying faster than any power. ∎

**Corollary DET-SP (separated products are a determining family for 𝒜). PROVEN-HERE.** 𝒫_n is dense in ^0𝒮_n. Hence an
E0-continuous S on 𝒜 is uniquely determined by its values on separated products, and any identity linear in S that holds on
separated products (E(4) invariance, permutation symmetry) holds on all of 𝒜. *Proof.* 𝒟_n is dense (Lemma DENSE); every
G ∈ 𝒟_n has compact support in some {δ > λ} and is covered by finitely many products of side-2 cubes (partition by Lemma W
(d)); Lemma TP's partial sums are in 𝒫_n and converge to G in 𝒮. ∎

**Theorem BRIDGE (separated products with quantified separation ⇒ a positive OS functional on 𝒜). PROVEN-HERE (implication).**
Assume (SP_λ) and (X0), uniformly along a sequence (a_j, R_j) (a_j → 0; R_j → ∞, or R_j ≡ R). Then:
- (i) (X1) holds in linear-growth form with p_X := p + 4, r_X := r + 6, b_X := b + (5r/2) + 8 and c_* := 4c_SP (apply (SP_λ)
  at separation λ/4 to each separated product of Lemma TP; the factor 4^{pn} goes into A^n);
- (ii) by Theorem EXT, (H_reg-sep) holds with **s = max(p + r + 17, q_X + 6) and β = b + (19r/2) + 51** (EXT (ii) with (i)'s
  parameters; explicit, linear-growth, not optimised);
- (iii) by Theorem CLOSURE-sep, along a subsequence S^{(j)} → S on all of 𝒜_𝒟, S extends uniquely to 𝒜 (Corollary DET-SP)
  and satisfies **E0′** with (s, β) of (ii) and **E2 on 𝒜_+** — the positivity-compatible extension: RP is obtained from exact
  lattice RP on 𝒜_{𝒟+} and density (CLOSURE-sep (d)), never from contact values; plus E3 and (Re);
- (iv) **E1 on all of 𝒜** as soon as invariance holds on separated products for a countable dense subgroup G_0 (all n):
  that is exactly what CODEX_REVIEW_SEAM bank item 5 (joint diagonal, Cartesian enumeration) or CONTRACT-sep (iterated route)
  delivers on the separated domain; Corollary DET-SP and continuity extend it to 𝒜 — no estimate beyond (SP_λ);
- (v) **contact-term domain: empty, by construction.** S_n is defined on ^0𝒮_n only; no value is assigned to a test function
  that is not flat on Δ_n (e.g. f ⊗ f, i.e. "e(f)²"); two families differing by any distribution supported on Δ_n — for
  instance CODEX_REVIEW_SEAM F9's h(x)δ(x − y) with nonconstant h, or its added white noise of covariance hδ — are the SAME
  element of 𝒜′, so they change no value of S, no RP form on 𝒜_+ and no invariance statement on 𝒜. REC (e) needs no contact
  values, but DOES require the whole common-hierarchy contract: E0′ from (ii), E2/E3/(Re) from (iii), full E1 from (iv),
  S_0=1, and the scalar or finite Cartesian tensor dictionary. (SP_λ) alone does not supply the invariance premise of (iv).
  No conclusion here identifies this scalar hierarchy with all YM fields. An ordinary-moment extension to 𝒮(R^{4n}) is not
  supplied; for the clover field on tori with a non-vacuous normalisation none exists as a cutoff-uniform limit (Proposition FS).
*Proof.* (i): for G in (X1)'s class at scale λ ≥ c_*a, Lemma TP gives |S(G)| ≤ Σ_{c,k}|ĝ_c(k)||S(Π_ih^c_{i,k_i})| ≤
A^n(n!)^b(λ/4)^{−pn}Σ_{c,k}|ĝ_c(k)|Π_i‖h^c_{i,k_i}‖_{λ/4,r} ≤ A^n(n!)^b4^{pn}C_TP^n(n!)^{5r/2+8}λ^{−(p+4)n}‖G‖_{λ,(r+4)n+2}
(the interchange is legitimate: S^{a,R}_n is a finite sum of point values and the expansion converges uniformly; complex
factors are allowed in (SP_λ)); (r + 4)n + 2 ≤ (r + 6)n. (ii)-(iv): as stated, by EXT, CLOSURE-sep and DET-SP. (v): ^0𝒮_n
annihilates every distribution supported on Δ_n (each such distribution is a finite sum of derivatives of measures on Δ_n
locally, and every element of ^0𝒮_n vanishes there with all derivatives). ∎
**Necessity (so this is the minimal bridge).** By Proposition MIN, convergence on the whole flat test space forces a power-law
per-scale bound; restricted to separated products this is (SP_λ) with n-dependent constants. So the power-law quantifier on
the separation is unavoidable; the linear-growth form of the constants is what E0′ (hence reconstruction) adds.

**Verdict on CODEX_REVIEW_SEAM Finding 9 and bank item 6.** **Agree** that the separated family together with U-sep as written
and a countable diagonal does not supply contact values or a positivity-compatible extension to an algebra CONTAINING contact
configurations, and that "determining" cannot be asserted without hypotheses. **Add** (not a disagreement with the finding as
scoped): in the scalar formulation fixed in §1, the test algebra is 𝒜 = ⊕_n ^0𝒮_n, which contains no contact configurations;
separated products are dense in it (DET-SP); the positivity-compatible extension is Theorem BRIDGE (iii); its one analytic
input is (SP_λ). In that formulation the clause "including contact configurations among insertions" of CODEX_REVIEW_SPHERE F7's
repair is not needed. So the "precise positivity/regularity/contact-domain bridge" of SEAM bank item 6 is: domain 𝒜, regularity
E0′ via (SP_λ) → TP → EXT, positivity E2 on 𝒜_+ via CLOSURE-sep (d), contact domain empty (BRIDGE (v)). **Agree** with SEAM
bank item 5 (joint diagonal with invariance on the separated domain; same mechanism as ASSEMBLY R2); BRIDGE (iv) is what lifts
that invariance to 𝒜.

**Additions to the summary table (§9).**
| # | Claim | Where | Verdict / status |
|---|---|---|---|
| 25 | (SP_λ): the separated-product input with power-law separation dependence (and its cumulant / coarse-image forms) | §13 | stated; OPEN (RG side) |
| 26 | Lemma TP (tensor-product expansion at scale λ) | §13 | PROVEN-HERE |
| 27 | Corollary DET-SP (separated products dense in ^0𝒮_n; determining for 𝒜) | §13 | PROVEN-HERE |
| 28 | Theorem BRIDGE (i)-(v) | §13 | PROVEN-HERE (implication; input (SP_λ) OPEN) |
| V19 | CODEX_REVIEW_SEAM F9 ("separated products do not determine the full observable algebra") | §13 | agree as scoped (algebra with contacts); for 𝒜 they do (DET-SP) |
| V20 | SEAM55 (H2)/U-sep as written suffices for the bridge | §13 | NOT sufficient without the λ-power quantifier (REFUTED as sufficient) |
| V21 | CODEX_REVIEW_SEAM bank item 5 (joint diagonal on the separated domain) | §13 | agree |

**What should change (adds to §11).** HANDOFF's "most dangerous" bridge (CODEX_REVIEW_SEAM F9 / bank item 6): record Theorem
BRIDGE (pending Codex) with its single analytic input (SP_λ) — the SRC lane's deliverable, in cumulant or coarse-image form, with
the source radius quantified so that the dependence on the separation is a power law (the shrinking-radius route of
CODEX_REVIEW_SRCAN item 10 is one candidate). SEAM55's row 12 ("U-sep + ^0𝒮 contraction lemma") becomes: (SP_λ) uniformly in
R (OPEN) + CONTRACT-sep + BRIDGE (pending Codex).

Section completed (UTC):
2026-10-29T05:27:03Z
- **E10 (BRIDGE (v), justification).** Replace the parenthetical by: a tempered distribution supported in the closed set Δ_n
  is locally of finite order k and annihilates every test function vanishing with its derivatives of order ≤ k on its support
  (Hörmander, ALPDO I, Thm 2.3.3 [m]); elements of ^0𝒮_n vanish there with all derivatives.
- **E11 (historical counts, superseding the original E4).** Over the 24 claim-parts of V1-V21: **CONFIRMED 12** (E4's ten + V19 as scoped + V21),
  **REFUTED 7** (E4's six + V20), **NOT-VERIFIED 3** (V5, V13, V14), **superseded/closed 2** (V2, V8). New results of this file:
  19 PROVEN-HERE items (the 16 of §9 plus Lemma TP, Corollary DET-SP, Theorem BRIDGE), 1 then-IMPORTED [m-sec] (REC (e)), 1
  then-proposed owner decision (OWN-alg). This records the original tally only. Current REC (e)/§1.6 supersede those two
  descriptions without upgrading other claims; this consumer alignment needs fresh review. Historical checks: ol55_1 PASS,
  with the limited scope now printed in §8; no criteria or recorded result has changed.
Final line (UTC):
2026-10-29T05:27:46Z
