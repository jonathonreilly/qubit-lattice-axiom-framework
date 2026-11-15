Reviewer model: claude-opus-5-5

# UIR55 — the trivial-background estimate (UIR^♮) of the coupling flow: explicit Fourier form, n-uniform bound, leading coefficient

Worker file (Opus 5.5, worker role; the binding rules of REVIEW_BRIEF_55 apply). This worker writes only this file and
`checks/ui55_*`. No git. Append-only after the PRE-STATED block. Labels: **PROVEN-HERE** (complete argument written here),
**CONDITIONAL** (implication proven here; inputs named with owner file and owner's status), **ARGUED** (reason given, hole
named), **OPEN**, **IMPORTED-standard** (textbook fact used without re-derivation, named). Statuses quoted from other files are
those files' labels unless this file says it re-derived them. Line numbers drift; citations carry a locating string.

## PRE-STATED (written 2026-10-29T01:25Z UTC, before any derivation, criteria file or script of this file)

*Provenance.* Before this block I read: REVIEW_BRIEF_55 (all); FLOW55.md (all, 616 lines, as on disk at 00:55Z, i.e. through
its §12 "Check provenance"); LINEAR_PACKAGE §0-§5; FLOW.md §0-§5.7, §16-§18, §24, §30, §36-§37, §59-§60, §65-§80, §88-§90,
§96-§99, §107-§108, §110 (bounded `sed` ranges); GSHARP55 §0 (head), §3.4; PLAN_S26 §11 (flow paragraph). CODEX_REVIEW_FLOW55.md
appeared on disk at 01:25Z; I have NOT read it before writing this block. Exploratory reasoning (not written down) preceded
this block: about the K̄-form propagator at U = 1, the chain-rule structure of the IR-term vertices, and which parts of
FLOW's (U-IR) list survive in the K̄ form. **No derivation, criteria file or script of this file existed before this time.**

*Symbol pins (systemic defect 1), fixed now.* n = number of RG steps, ℓ = L^n (FLOW/FLOW55 usage; LINEAR_PACKAGE's "n := L^k"
is a different object and is not used here). β_0^std := 2N·2b_0 = 11N²/(12π²) in u-units (FLOW §0), b_0 = 11N/(48π²). The
brief's phrase "β_0^std = 11N/(48π²)" names b_0, not FLOW's β_0^std; the target identity is read in FLOW's units:
β[G^♮_⊥,n] = −(21/22)β_0^std n log L + O(1). κ = the uniform soft-kernel stiffness of FLOW's stripped tower (Def F-strip),
not Balaban's κ and not the polymer decay κ_p. (TC) below means FLOW55 §4.3's tower-jet convergence, not PLAN_S26 §12's
two-sided window.

**Targets.**
- **U1 (explicit form).** Write, at U = 1 and in Fourier space (fine and level-n momenta, alias blocks): (a) the propagator of
  the K̄ unit ½log det(H^♮ + D_0D_0^*) − ½log det′Δ_{W*}; (b) every class of vertex that enters β[G^♮_⊥,n] (Wilson /
  background-Feynman / ghost vertices with the fine tower as background leg; IR-term vertices from the jets of Ψ_min;
  residual-paired terms; the level group ½log det_⊥(P_⊥𝒞P_⊥)), with the chain-rule formula of the IR-term vertices in terms
  of one-step data; (c) what β extracts, as an integral ∫J^♮_n of a p²-coefficient integrand plus the level group.
- **U2 (prove).** Prove sup_n|β[G^♮_⊥,n] + (21/22)β_0^std n log L| < ∞ (and T-uniformity via infinite-volume definitions),
  or, where I cannot, reduce it to named, precisely stated, n-uniform estimates, each tagged with its status; for every piece
  I claim PROVEN, the constant must be shown independent of n.
- **U3 (leading coefficient).** Re-derive the coefficient of n log L, −(21/22)β_0^std, as the residue of the leading homogeneous
  integrand, and check its arithmetic in exact arithmetic (check ids `ui55_*`, criteria file first); identify where κ enters.
- **U4 (status).** A table: what is PROVEN here, what is CONDITIONAL and on what, what is OPEN; the κ-dependence.

**What would count as a refutation of my own claims (fixed now).**
- R-1 (propagator). If at U = 1 the K̄ unit's propagator is not exactly C^⊥_n ⊕ dΔ^{-2}d^* (C^⊥_n FLOW's Lemma U-T⊥ transverse
  propagator), e.g. a nonzero transverse–longitudinal cross block, or H^♮(1) not annihilating Ran d.
- R-2 (vertex classes). A vertex of D_VH^♮ or D²_VH^♮ at V = 1 that is in none of my classes, or a class I declare to have
  β = 0 whose contribution to the p² coefficient is nonzero for some n (an explicit instance).
- R-3 (any n-uniform bound I claim). A constant in the claimed bound that depends on n (or on T), traced to a specific step;
  or an exact small instance (finite torus, exact arithmetic) violating a claimed inequality.
- R-4 (leading coefficient). The exact residue arithmetic failing (ratio of transverse-group to total ≠ 21/22; the u-unit
  conversion ≠ 2N·2b_0), or a designed-FAIL control in a check that does not fire.
- R-5 (reduction). A remaining item I list as sufficient that is not sufficient (a further term needed), or one I list as needed
  that a proven statement already gives.

**Checks planned (criteria files `checks/ui55_<k>_criteria.md` written before each script; exact rational / symbolic
arithmetic in plain python — `fractions`, `sympy` — no floats in any verdict; nice 10; each with a designed-FAIL control).**
ui55_1: exact identities of the U = 1 K̄ propagator on a small torus (block-diagonality H^♮(1)d = 0, the alias-block Woodbury
form). ui55_2: the leading-coefficient residue (angular averages of the leading homogeneous transverse and ghost integrands;
the 21/22 ratio). Ids may be added; none removed.

---

# FINDINGS (appended from 2026-10-29T01:40Z, after the PRE-STATED block)

## 1. Inputs, and the Codex verdicts used

*Read after the PRE-STATED block:* CODEX_REVIEW_FLOW55.md (339 lines, complete; its last section "Exactly what may be
banked" is finished, items 1-6), FLOW.md §104-§106. I read the Codex file as it is on disk at 01:26Z.

Codex verdicts used, and my position on each (brief rule: explicit, either direction):
- **K̄ (exact averaging) CONFIRMED; H^♮D_0 = 0 only at the partially minimised critical saddle W*(V), not at arbitrary fine
  configurations** (Codex §1.1). **Agree.** Everything below uses H^♮D_0 = 0 only at W*(V), V near 1, and only its
  V-Taylor data at V = 1.
- **For N ≥ 3 the every-background statements need the φ-tower, not FLOW's literal k̃-tower; the trivial-point jets of order
  ≤ 5 agree, so β is unaffected** (Codex §1.2, with an exact SU(3) S4′ example). **Agree**, and this file uses only V = 1
  Taylor data of order ≤ 4 in the fields (one-loop two-point function), so it is unaffected; I write Ψ, 𝔪_n, W_♮ for the
  normalised (φ) objects throughout.
- **Schur/envelope, quotient Jacobian, and the coarse identity det 𝒞·det′(D^*𝒞^{-1}D) = det_⊥(P_⊥𝒞P_⊥)·det′(D^*D) CONFIRMED;
  "this is not a proof that all vertices of H^♮ are independent of that block"** (Codex §1.3). **Agree**; §2.3 below writes
  those vertices out.
- **K̄-tad: β[𝔗′_n] = 0 at every fixed n CONFIRMED with erratum 1; the sentence "the one place where a κ-dependent term could
  have reached the coefficient of n log L" NOT-VERIFIED as exhaustive** (Codex §2.3). **Agree** with both.
- **GH0 CONFIRMED; Corollary K̄-β and (UNIV-1L) ⟺ (UIR^♮) CONFIRMED as a conditional coefficient reduction** (Codex §3.1-§3.2).
  **Agree.** This file takes FLOW55's reduction as its starting point in exactly that conditional sense.
- **KAPPA's "(UIR^♮) bounds (R-a)/(R-b)" REFUTED as a logical implication** (Codex §3.3, by zero-integral perturbations of
  the integrand). **Agree.** This file uses only the valid direction: (R-a)_int + (R-b) + (R-c) + a level-group bound ⇒ (UIR^♮)
  (FLOW Lemma U-res / U-res′); it never infers integrand bounds from (UIR^♮).
- **(G-dec) CONFIRMED with constants that may depend on n** (Codex §2.2). **Agree**; it is used here only at fixed n.

Upstream FLOW items used here, with the status I give them in this file: Lemma U-T⊥ (§24.1) and Proposition U-a1⊥ (§24.3) —
re-derived in §2.2 and §3.3 below; Lemma U-res / U-res′ (§17, §24.3) — re-derived in §3.1 (elementary); Lemma U-Tay + Lemma
CL-V (§18, §95) — used as FLOW's PROVEN-HERE, not re-derived (CL-V not read in full; its role is (R-c) only); VFINE-K/VFINE-L
(§88) — their arithmetic re-checked in §4 (check ui55_2), not their lattice proofs; Lemma Cartan-𝔪, Cartan-T (§104-§105) —
read in full, used in §3.4 for the structure of the root-sector form factors.

## RESUMED 2026-10-29T02:46Z

*Resume provenance.* This run (model claude-opus-5-5 — the same ID as the first line, so no extra model line is added)
read, before this heading: the resume brief (go_UIR55.md); REVIEW_BRIEF_55 (all); this file as on disk (91 lines: the
PRE-STATED block and §1 above); CODEX_REVIEW_FLOW55.md (all 339 lines, "Exactly what may be banked" first; its last section
is finished, items 1-6); FLOW55.md (all 616 lines). The draft above stops after §1; the forward references in §1 to "§2.2,
§2.3, §3.1, §3.3, §3.4, §4" point to sections the stopped run never wrote. I treat §1 as UNREVIEWED: I re-read each Codex
verdict it quotes against CODEX_REVIEW_FLOW55.md and agree that §1 quotes them correctly (items 1.1, 1.2, 1.3, 2.2, 2.3,
3.1-3.3 of the Codex file). Errata to the draft, if any, go in a section "Errata to the stopped draft" below. The
sections below are numbered from §2 and are written by this run.

*Further reading done by this run before §2 (bounded ranges, by locating string):* FLOW.md §0 ("Conventions fixed for
this file"), §1, §3 ("Def F-strip", "Def F-g", "Lemma F-Π"), §16 ("Lemma U-tad", "Proposition U-dec", "Lemma U-pair",
"Corollary U-red"), §17 ("Lemma U-res"), §18 ("Lemma U-Tay", "Lemma U-cov-IR", the (U-IR) list and its [RFL] fixes), §23
("Lemma BL", "(I1)"-"(I5)", "Lemma U-loc'"), §24 (all), §60, §65-§67, §74-§76 ("Lemma FINE-IR", "Proposition IR-id",
"Theorem UIR-S"), §88 ("Lemma FINE-IR-gen", the [RFL11-fix S11-3] value paragraph), §95 ("Lemma CL-V"), §96-§99, §104-§107,
§110; LINEAR_PACKAGE §1-§4; GSHARP55 §3.4; REVIEW_FLOW_S3 / S11 / S12 verdict lines for U-T⊥, U-a1⊥, FINE-IR-gen, CL-V,
VFINE-K-val (CONFIRMED there; those reviewers' model IDs were not re-checked by me, so I re-derive what I build on).

---

## 2. U1 — the explicit form at U = 1

### 2.1 Conventions and symbols (one colour where colour is trivial; root sectors where it is not)
Fine momenta q ∈ BZ = [−π, π]⁴; a level-n class P ∈ [−π, π]⁴ has the ℓ⁴ fine aliases q_m = (P + 2πm)/ℓ. ŝ_α(q) = e^{iq_α} − 1,
λ̃(q) := |ŝ(q)|² = Σ_α 4 sin²(q_α/2), P_T(q) := 1 − ŝŝ^†/λ̃, g(q) := P_T(q)/λ̃(q). D_ℓ(θ) := ℓ^{-1}Σ_{|j|≤(ℓ−1)/2}e^{iθj}.
𝒞 := 𝒞_n(1), Π := 𝒞^{-1} − 𝒞^{-1}d_c(d_c^*𝒞^{-1}d_c)^+d_c^*𝒞^{-1} = P_⊥(P_⊥𝒞P_⊥)^+P_⊥ (P_⊥ the level transverse projector, d_c the
level derivative; the identity is CONFIRMED in CODEX_REVIEW_FLOW55 §1.3). Q := Q^{(n)} = D𝔪_n(1), the composite S4′ root map,
Q = Q_str − d_c∘h^{(n)} (LINEAR_PACKAGE §1.2, composite form in FLOW §98 (a)); root covariance Q d = d_c ev.

**Finding 2.1 (minor erratum to FLOW §24 (F2); bounds unaffected).** With LINEAR_PACKAGE's definition
(Q_strA)(X, μ) = L^{-4}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ) — y runs over the whole 4D block, including its μ-coordinate — the leg
direction carries TWO Dirichlet factors: the one-step symbol is (phase)·L·D_L(q_μ)·Π_αD_L(q_α) (the μ-direction kernel is the
triangle filter (1/L)(Σ_{y<L}z^y)(Σ_{j<L}z^j)), and the composite of n steps is (phase)·ℓ·D_ℓ(q_μ)·Π_αD_ℓ(q_α) (the triangle
filters telescope: K_L(z)K_L(z^L) = K_{L²}(z) up to the phase). FLOW §24 (F2) writes "𝔪̂_str,μ(q) = e^{iq·v_μ}ℓΠ_αD_ℓ(q_α)", which
is the transverse-FACE average; FLOW §98 (VC-T0, "Q_str has the symbol δ_μνS_μ^{(L)}(k_μ)Π_αD_L(k_α)") has the correct form.
Since |D_ℓ| ≤ 1 and |∂^jD_ℓ| ≤ c_jℓ^j·min(1, π/(ℓ|θ|)) (FLOW Lemma DIR), every bound of FLOW §24 ((F2), U-cov-IR′, U-a1⊥) holds
verbatim with the extra factor. Status: PROVEN-HERE (elementary), exact check ui55_1 Part C.

### 2.2 Lemma P♮ (the K̄ propagator at U = 1): PROVEN-HERE (exact check ui55_1 Parts A, B)
*Claim.* O^♮_n(1) := H^♮(1) + dd^* = d^*d + dd^* + Q^*ΠQ (FLOW55 Prop. K̄-1L (c); Codex §1.3: "At V = 1, eliminating h in
the quadratic form gives exactly H♮ = d*d + Q*ΠQ") is block diagonal for ker d^* ⊕ Ran d, with
  O^♮_n(1) = [d^*d + Q_str^*ΠQ_str]|_{ker d*} ⊕ [dd^*]|_{Ran d},   (O^♮_n(1))^{-1} = C^⊥_n ⊕ dΔ_0^{-2}d^*,
C^⊥_n := ([d^*d + Q_str^*ΠQ_str]|_{ker d*})^{-1}P_T, and per class P (infinite volume or twisted torus; FLOW's [RFL3-fix S3-5]
q = 0 caveat on periodic tori) the alias-block Woodbury form
  C^⊥_n(q_a, q_b) = δ_{ab}g(q_a) − ℓ^{-4}Y(q_a)^†Ĥ_n(P)Y(q_b),  Y(q) := 𝔪̂_str(q)g(q),  Ĥ_n = (P_⊥(𝒞 + Q_strgQ_str^*)P_⊥|_⊥)^{-1},
Ĥ_n the symbol of the level-n tree Hessian D²𝒯_n(1). **There is no transverse–longitudinal cross block, and the longitudinal
propagator is EXACTLY the massless background-Feynman one, dΔ_0^{-2}d^*.** (Refutation R-1 of the PRE-STATED block does not occur.)
*Proof.* (1) Π d_c = 0 and Q d = d_c ev give Q^*ΠQ d = 0; Q^*ΠQ is symmetric, so it maps into (Ran d)^⊥ = ker d^*. d^*d vanishes on
Ran d and preserves ker d^*; dd^* vanishes on ker d^* and preserves Ran d. Hence block diagonality. (2) On ker d^*:
⟨A, Q^*ΠQA⟩ = ⟨Q_strA − d_c hA, Π(Q_strA − d_c hA)⟩ = ⟨Q_strA, ΠQ_strA⟩ since Π d_c = 0 (the S4′ slice part d_c∘h drops out
exactly; this is FLOW's Lemma U-T⊥, here obtained in one line because the K̄ form has Π, not 𝒞^{-1}). (3) On Ran d,
dd^*·dΔ_0^{-2}d^* = dΔ_0^{-1}d^* = the orthogonal projector onto Ran d. (4) Woodbury on the transverse ranges:
(g^{-1} + Q_str^*P_⊥S^{-1}P_⊥Q_str)^{-1} = g − gQ_str^*P_⊥(S + P_⊥Q_strgQ_str^*P_⊥)^{-1}P_⊥Q_strg, S := P_⊥𝒞P_⊥; the bracket is the
level transverse tree propagator (FLOW Lemma U-T⊥ step (3); equivalently §3.2 below at V = 1), whose inverse is Ĥ_n|_⊥. ∎
*Reading.* FLOW's (a3) (slice) and (a4) (longitudinal / coarse-gauge / cross entries) do not exist in the K̄ form: the
coarse-gauge block that grows like n/κ (FLOW Lemma COV-str (iv), Prop. LONG-n) never enters a propagator. The only
n-dependent propagator piece is the transverse correction Δ^⊥_n = C^⊥_n − g, controlled n-uniformly by FLOW's U-cov-IR′ and
U-a1⊥ (CONFIRMED in REVIEW_FLOW_S3; I re-checked their degree count against Finding 2.1 and it is unchanged).

### 2.3 The vertices that enter β[G^♮_⊥,n] (U1 (b))
β is the transverse P² coefficient of the V-Hessian at V = 1 (FLOW Def F-g; a directional limit, Codex §2.3). By Lemma U-tad
(i) every term containing D²W*(1) or D²ρ*(1) vanishes (first derivative of a global-colour-invariant function at the trivial
point). The Hessian of G^♮_⊥,n(V) = ½log det_{ker D_0^*}H^♮(V) + ½log det_{ker D_V^*}(P_⊥𝒞(W*)P_⊥) is therefore built from the
propagator of §2.2 and the following first- and second-order V-derivatives at 1 (in the equivariant chart, FLOW U-tad fix):
- **(V-W) Wilson / background-Feynman / ghost vertices** with the fine tower DW*(1)v as background leg: ∇³𝒯_0(1), ∇⁴𝒯_0(1)
  contracted with DW*v, the derivatives of D_{W*}D_{W*}^* and of Δ_{W*}; at a Cartan plane wave these are FLOW Lemma CL-V's
  (CONFIRMED, REVIEW_FLOW_S12) explicit root-sector symbols, with the continuum limit O^c = −D²δ_μν − 2iq_αF_μν.
- **(V-M) IR-term vertices from the composite map:** with B(U) := D𝔪(U)^*Π_{𝔪(U)}D𝔪(U), the background derivatives of D𝔪(U).
  Chain rule (composite of the one-step φ-maps 𝔪^{(k)}, Q^{(k)} := Q_{k−1}⋯Q_0, Q^{(n←k+1)} := Q_{n−1}⋯Q_{k+1}):
    D²𝔪_n(1)[a, b] = Σ_{k<n} Q^{(n←k+1)}·D²𝔪^{(k)}(1)[Q^{(k)}a, Q^{(k)}b],
  and at a Cartan background the one-step root-sector linearisation is FLOW Lemma Cartan-T (d): z = avg_Tξ_T + (iq/2)Cov_T(θ_T, ξ_T)
  + O(a²) (θ_T the background line sum, ξ_T the transported fluctuation sum along the S4′ contour T). So [ε]Q^{(n)} =
  Σ_kQ^{(n←k+1)}[ε]Q_kQ^{(k)}: a level sum of one-step data, each a fixed local map in level-k units.
- **(V-Π) IR-term vertices from Π_{𝔪(U)}:** the background dependence of 𝒞(U) (FLOW Prop. VC-T1: Σ_i s_i with ||[ε^r]s_i|| ≤ C_rL^{-2i},
  given (Π-loc)) and of the level projector P_⊥(U) = 1 − D(D^*D)^{-1}D^* (FLOW Lemma P-poles: first-order massless poles at the
  loop momenta K and K + P, λ̃-normalised). **These vertices are not local**: Π's symbol contains the level transverse projector
  P_⊥(P), non-analytic at P = 0, and the h-elimination brings the massless level Green function (D^*𝒞^{-1}D)^{-1} (the Schur
  complement H^♮ = B − EA^{-1}E^* of Codex §1.3 has A = 𝔊_0 + R massless at level n).
- **(V-ρ) residual-paired vertices:** terms linear or quadratic in Dρ*(1)v, where Π̂ρ̂* = Ĥ_n(P)v̂ (stationarity, FLOW55 §5.3 step (1))
  and D^*𝒞^{-1}ρ* = 0 (h-stationarity), hence ρ̂* = 𝒞̂Ĥ_nv̂ + O(v̂²): ρ* is proportional to the tree equation of motion ∇𝒯_n(V).
- **(V-L) the level group** ½log det_{ker D_V^*}(P_⊥𝒞(W*)P_⊥) = ½log det𝒞 + ½log det′(D_V^*𝒞^{-1}D_V) − ½log det′Δ_V (Codex §1.3 identity;
  𝒞 fixed at 𝒞(W*)): two massless level-n scalar loops plus a local term.

### 2.4 What β extracts, and why a termwise residue-lemma attack has to group terms (U1 (c))
FLOW55 §5.5 writes β[G^♮_⊥,n] = ∫_{BZ}J^♮_n + β[level group], J^♮_n the p²-integrand of the fine unit with propagator §2.2 and the
vertices (V-W), (V-M), (V-Π), (V-ρ); via FLOW Lemma U-res′, (UIR^♮) would follow from n-uniform (R-a_int), (R-b) for J^♮_n plus an
n-uniform bound on the level group. Writing J^♮_n = J_*^⊥ + J^{(a1⊥)}_n + J^{(IR)}_n (J_*^⊥ the massless BF integrand of the
transverse group, J^{(a1⊥)}_n the Wilson-vertex diagrams with Δ^⊥_n insertions — FLOW's U-a1⊥ — and J^{(IR)}_n every diagram
with ≥ 1 vertex of type (V-M), (V-Π), (V-ρ)): **ARGUED (not used below):** neither J^{(IR)}_n nor the level group is separately
n-uniformly bounded in the region |q| ≲ 1/ℓ, because the (V-Π) and (V-L) pieces carry massless LEVEL-n loops whose log(1/P)
must cancel the fine massless pieces' log(ℓ/P) (the GH0 mechanism, FLOW55 §5.4); and J^{(a1⊥)}_n's (R-b) on |q| < 1/ℓ is not
written by FLOW. The exact regrouping in §3 avoids this bookkeeping altogether.

**Check ui55_1 (run 2026-10-29T03:31Z; criteria checks/ui55_1_criteria.md written 03:29Z, before the script; md5 ui55_1.py
0f5c91a94fcbf60b25e8042b1b073715; one run, output unaltered in checks/ui55_1_out.txt): 20/20 PASS, the three designed-FAIL
controls fire (3.3 s, 23 MB).** Part A: the abstract split algebra of §3.1 below (A0-A6), exact on random rational data;
controls: FLOW's pre-K̄ IR term M^T𝒞^{-1}M is not transverse (Ac1), the split fails without the level group (Ac2), the
Feynman form fails for a non-transverse A (Ac3). Part B: Lemma P♮ on a 2D torus with the actual S2′ order-averaged contour
map (side 6, L = 3): Q d = d_c ev, Q = Q_str − d_c h, Q^*ΠQ d = 0, no cross block, O^{-1} = C^⊥ ⊕ dΔ^{-2}d^*; control: with
𝒞^{-1} in place of Π the cross block is nonzero (Bc fires). Part C: Finding 2.1 (leg-direction weights 1/3, 2/3, 1, 2/3, 1/3 —
two Dirichlet factors; the single-box reading fails, Cc fires). What it cannot decide: anything n-uniform or analytic.

---

## 3. U2 — the exact fine/level split of the K̄ transverse group, and what it does to (UIR^♮)

Setting for §3 (fixed n ≥ 1): FLOW's one-loop (Laplace) level, the normalised φ-objects (Codex §1.2), the K̄ tower
representative W* = W*(V) with h* = 1 (Codex §1.2 last paragraph), root sector α of a Cartan colour direction (Lemma F-Π (i);
the Cartan sector does not feel a Cartan background), on antiperiodic tori of side Nℓ (all covariant Laplacians and the
massless transverse operator d^*d|_{ker d^*} invertible; FLOW §75 (b)'s device) and then N → ∞ (per-site densities).
Notation: m := 𝔪(W*) (the composite φ-map of the tower), ρ* := log(m^{-1}V) (linkwise), D_0 := D_{W*}, D_m := level covariant
derivative at m, E_0 := ker D_0^*, E_m := ker D_m^*, P_m := the projector onto E_m, 𝒞 := 𝒞(W*), S := P_m𝒞P_m|_{E_m},
Π_m := P_mS^{-1}P_m, M := D𝔪(W*), B := M^*Π_mM, A := H^♮ − B, A_0 := A|_{E_0}, 𝕄 := P_mMP_{E_0}.

### 3.1 Lemma SPLIT (exact; every V near 1): PROVEN-HERE (algebra checked exactly in ui55_1 Part A)
(i) BD_0 = 0 and AD_0 = 0: **both parts of H^♮ are exactly transverse.**
(ii) ½log det_{E_0}H^♮ + ½log det_{E_m}S = ½log det_{E_0}A_0 + ½log det_{E_m}(S + 𝕄A_0^{-1}𝕄^*).
(iii) 𝔅 := P_m(S + 𝕄A_0^{-1}𝕄^*)^{-1}P_m satisfies 𝔅D_m = 0, and
  G^♮_⊥,n(V) = 𝔉(V) + 𝔏(V) + 𝔐(V),
  𝔉 := ½log det(A + D_0D_0^*) − ½log det′Δ_{W*},   𝔏 := −[½log det(𝔅 + D_mD_m^*) − ½log det′Δ_m],
  𝔐 := ½log det_{ker D_V^*}(P_V𝒞P_V) − ½log det_{E_m}(P_m𝒞P_m)   (the level group moved from m to V = me^{ρ*}).
*Proof.* (i) Fine gauge covariance of the composite map, 𝔪(U^g) = 𝔪(U)^{g|_n}, differentiated at g = 1, gives MD_0λ = D_m(evλ);
Π_mD_m = 0 (Codex §1.3's Π identity at the background m), so BD_0 = 0. H^♮D_0 = 0 at the critical saddle W* (Codex §1.1).
Hence AD_0 = 0. (ii) B and A vanish on Ran D_0 and are symmetric, so both map E_0 → E_0, and H^♮|_{E_0} = A_0 + 𝕄^*S^{-1}𝕄. With A_0
invertible (at V = 1, A_0 = d^*d|_{ker d^*}, invertible on the antiperiodic torus; by continuity near 1), Sylvester's identity
det(A_0 + 𝕄^*S^{-1}𝕄) = det A_0·det(1 + S^{-1}𝕄A_0^{-1}𝕄^*) = det A_0·det(S + 𝕄A_0^{-1}𝕄^*)/det S. (iii) 𝔅 is P_m-compressed, so 𝔅D_m = 0.
For an exactly transverse symmetric X (XD = 0), X + DD^* is block diagonal for ker D^* ⊕ Ran D and DD^*|_{Ran D} ≅ D^*D|_{(ker D)^⊥},
so ½log det(X + DD^*) = ½log det_{ker D^*}X + ½log det′(D^*D). Apply it to A (fine) and to 𝔅 (level, with
log det_{E_m}𝔅 = −log det_{E_m}(S + 𝕄A_0^{-1}𝕄^*)); add the level-group difference 𝔐. ∎
*Reading.* FLOW55 §5.5 said that FLOW's Woodbury split "is not available off-shell without re-introducing the defect". It is
available: split H^♮ as (exactly transverse IR part B) + (remainder A); A is then exactly transverse too, and the Wilson
off-shell defect H_W(W*)D_0 ≠ 0 is compensated exactly inside A by the residual part of the IR Hessian (Lemma ENV-𝒯 below).
The level group is no longer a separate object: it completes the Sylvester identity.

### 3.2 Lemma ENV-𝒯 (the two pieces are the fine Wilson group and the level tree group, up to equation-of-motion terms):
### PROVEN-HERE
Write Ψ_min(U; V) = ψ(U, r), r := log(𝔪(U)^{-1}V), with ψ(U, 0) = 0, ∂_rψ(U, 0) = 0, ∂²_rψ(U, 0) = Π_{𝔪(U)} (the h-Schur
complement of 𝒞(U)^{-1}; FLOW U-dec (i) and Codex §1.3). Put F(U, V) := 𝒯_0(U) + Ψ_min(U; V), so 𝒯_n(V) = F(W*(V), V) (the min over h is
trivial because min_U[𝒯_0 + Ψ(U; ·)] is already level-gauge invariant). Define the residual parts
  R_UU := H^♮ − H_W(W*) − B,   R_UV := ∂_U∂_VF + M^*Π_m,   R_VV := ∂²_VF − Π_m   (all at (W*, V)).
Then: (a) R_UU, R_UV, R_VV are smooth in (W*, ρ*) and vanish at ρ* = 0; A = H_W(W*) + R_UU.
(b) Hess_V𝒯_n(V) = 𝔅 + 𝒪, 𝒪 := R_VV + Π_m M(H^♮|_{E_0})^{-1}R_UV + R_VU(H^♮|_{E_0})^{-1}M^*Π_m − R_VU(H^♮|_{E_0})^{-1}R_UV.
(c) At linear order ρ* is proportional to the tree equation of motion: Π_mρ* = ∇𝒯_n(V) + O(|v|²) and D_m^*𝒞^{-1}ρ* = 0, hence
ρ* = 𝒞Π_mρ* = 𝒞∇𝒯_n(V) + O(|v|²); in symbols Dρ̂*(1)(P) = 𝒞̂(P)Ĥ_n(P) (FLOW55 §5.3 step (1) is the first half). In particular
ρ* = 0 whenever ∇𝒯_n(V) = 0 (near 1: V flat), and then 𝒪 = 0, A = H_W(W*), 𝔐 = 0.
*Proof.* (a) At ρ* = 0 the residual vanishes, so the Hessian of ψ(U, r(U, V)) is the Gauss–Newton form r_U^*Π r_U = M^*Π_mM (the terms
∂_rψ·r_UU and ∂_Uψ-terms vanish with r); likewise ∂_U∂_VF = −M^*Π_m and ∂²_VF = Π_m there. (b) Envelope theorem for the critical
family W*(V): Hess𝒯_n = F_VV − F_VU(F_UU|_{E_0})^{-1}F_UV, legitimate because F_UV maps into E_0 (differentiate ∂_UF(U, V)[D_Uλ] ≡ 0,
fine gauge invariance of F(·, V), in V) and F_UU = H^♮. Insert F_VV = Π_m + R_VV, F_UV = −M^*Π_m + R_UV, F_UU|_{E_0} = A_0 + 𝕄^*S^{-1}𝕄 and use
Woodbury: Π_m − Π_mM(A_0 + 𝕄^*S^{-1}𝕄)^{-1}M^*Π_m = P_m(S + 𝕄A_0^{-1}𝕄^*)^{-1}P_m = 𝔅 (ui55_1 A4 checks this algebra exactly).
(c) ∇𝒯_n(V) = ∂_VF(W*, V) = ∂_rψ(W*, ρ*)·r_V = Π_mρ* + O(ρ*²); h-stationarity at h* = 1 is D_m^*∇_rψ-type, linearised
D_m^*𝒞^{-1}ρ* = 0; then 𝒞Π_mρ* = ρ* − D_m𝔊_0^{-1}D_m^*𝒞^{-1}ρ* = ρ*. If ∇𝒯_n(V) = 0, then Π_mρ* = O(ρ*²) and ρ* = 𝒞Π_mρ* + O(ρ*²) = O(ρ*²), so
ρ* = 0 for V near 1. ∎

### 3.3 Theorem TEL (exact telescoping of the transverse group): PROVEN-HERE, given the inputs named in the proof
*Definitions.* (1) For a translation-invariant, gauge-invariant, B_4- and C-covariant functional F on a lattice (fine or
level), β_F(P) (0 < |P| < π) := the ϑ-averaged ε²-density per site of F at the Cartan plane wave a_{x,1} = εcos(Px_2 + ϑ)H, divided by
the same density of the Wilson action Σ_ps(U_p) on that lattice. If F has an exponentially decaying Hessian, β_F(P) → β[F] (L4a-Π,
FLOW Def F-g); for the massless functionals below, β_F(P) is finite for P ≠ 0 and diverges logarithmically as P → 0. β[G] for
G^♮_⊥,n, G_gh,n is the directional limit lim_{P→0}β_G(P) (Codex §2.3, §3.1).
(2) The fine Wilson transverse group 𝒲^⊥(U) := ½log det(H_W(U) + D_UD_U^*) − ½log det′Δ_U, and, for a level tree action 𝒯
(any functional as in Lemma FP below), the level transverse group 𝒱^⊥[𝒯](V) := ½log det(Hess_X𝒯(Ve^X)|_{X=0} + D_VD_V^*) −
½log det′Δ_V. 𝒱^⊥[𝒯_0] is 𝒲^⊥ (same lattice functional).
(3) σ_⊥ := −(21/22)β_0^std (u-units, per unit log; VFINE-K/VFINE-L value, Codex §5.2 arithmetic; re-derived in ui55_2).
(4) a^⊥(𝒯) := lim_{P→0}[β_{𝒱^⊥[𝒯]}(P) − σ_⊥log(1/P)] (exists: Lemma FP (i)). J_n := (D², D³, D⁴)𝒯_n(1); a^⊥(J_n) := a^⊥(𝒯_n).
(5) The equation-of-motion remainder Δ_n(V) := G^♮_⊥,n(V) − 𝒲^⊥(W*(V)) + 𝒱^⊥[𝒯_n](V), and Ρ_n := lim_{P→0}β_{Δ_n}(P).
*Claim.* For every n ≥ 1, Ρ_n exists (finite) and
  **β[G^♮_⊥,n] + (21/22)β_0^std·n log L = a^⊥(J_0) − a^⊥(J_n) + Ρ_n,**
  **B_n − β_0^std·n log L = a^⊥(J_n) − a^⊥(J_0) − Ρ_n** (with FLOW55's Corollary K̄-β and Lemma GH0).
Moreover Δ_n is an equation-of-motion term: its second variation at V = 1 consists only of terms containing Dρ*(1)v =
𝒞̂Ĥ_n(P)v̂ (Lemma ENV-𝒯 (c)) — no term of Δ_n's Hessian is free of the factor Ĥ_n(P) = O(P²).
*Proof.* (α) *Fine piece through the tower (Lemma TT).* 𝒲^⊥ is Z⁴-translation invariant, so its Hessian at 1 is diagonal in fine
momentum and transverse. The fine tower DW*(1)v at level momentum P has the smooth component (v̂/ℓ)(1 + O(P)) at fine momentum P/ℓ and
aliases O(P³) (F-bg; Codex §3.1 confirms these orders in the GH0 setting). So per level site β_{𝒲^⊥∘W*}(P) = β_{𝒲^⊥}(P/ℓ)(1 + O(P)) +
O(P⁴)·(alias sum) (the factors ℓ⁴·ℓ^{-2}·ℓ^{-2} cancel, marginal scaling; ℓ²·sin²(P/2ℓ)/sin²(P/2) = 1 + O(P²)). By VFINE-K and VFINE-gh
(FLOW §88/§95, CONFIRMED REVIEW_FLOW_S11/S12; finite parts exist) β_{𝒲^⊥}(k) = σ_⊥log(1/k) + a^⊥(J_0) + o(1), hence
β_{𝒲^⊥∘W*}(P) = σ_⊥log(ℓ/P) + a^⊥(J_0) + o(1) as P → 0 (the O(P)·log(ℓ/P) correction is o(1)).
(β) *Level piece.* By definition and Lemma FP (i), β_{𝒱^⊥[𝒯_n]}(P) = σ_⊥log(1/P) + a^⊥(J_n) + o(1).
(γ) *Total.* β[G^♮_⊥,n] exists at fixed n (FLOW55 Cor. K̄-β with B_n finite). So β_{Δ_n}(P) = β_{G^♮}(P) − β_{𝒲^⊥∘W*}(P) + β_{𝒱^⊥[𝒯_n]}(P)
has the limit Ρ_n = β[G^♮_⊥,n] − σ_⊥ log ℓ − a^⊥(J_0) + a^⊥(J_n): the log(1/P) terms cancel because the two coefficients are the same σ_⊥.
With log ℓ = n log L this is the first display; the second follows from B_n = −β[G^♮_⊥,n] + (1/22)β_0^std n log L.
(δ) *EOM structure.* By Lemma SPLIT, Δ_n = (𝔉 − 𝒲^⊥∘W*) + (𝔏 + 𝒱^⊥[𝒯_n]) + 𝔐. By Lemma ENV-𝒯 (a), 𝔉 − 𝒲^⊥∘W* is a function of
(W*, ρ*) vanishing at ρ* = 0 (A − H_W(W*) = R_UU); by (b), 𝔏 + 𝒱^⊥[𝒯_n] is a function vanishing at ρ* = 0 (𝔅 − Hess𝒯_n = −𝒪, and
m = V there); 𝔐 vanishes at ρ* = 0. The second variation at V = 1 of a function Φ(W*(V), ρ*(V)) with Φ(·, 0) ≡ 0 is
2∂_U∂_ρΦ[DW*v, Dρ*v] + ∂²_ρΦ[Dρ*v, Dρ*v] + ∂_ρΦ[D²ρ*(v, v)], and the last term vanishes (∂_ρΦ(1, 0) is an Ad-invariant linear form,
Lemma U-tad (i)). ∎
*What the theorem says.* The whole n-dependence of the transverse group beyond its universal slope sits in (i) a^⊥(J_n), the
finite part of the ONE-SCALE level-n polarisation of the tree action — a functional of the tree jets J_n only, in level units,
with no alias sums and no IR term; and (ii) Ρ_n, the β of an equation-of-motion term. **The remainder telescopes exactly: no
mechanism can make it accumulate linearly in n, unless a^⊥(J_n) or Ρ_n themselves grow.** The universal slope comes entirely
from the n-INDEPENDENT fine Wilson functional evaluated at the scale ratio ℓ (the GH0 mechanism of FLOW55 §5.4, now for the
whole transverse group).

**Correction to §3.3 step (δ) (appended immediately after writing it; content of the claim unchanged).** For 𝔉 and 𝔐 the
phrase "a function of (W*, ρ*) vanishing at ρ* = 0" is literally right (R_UU(U, ρ) := Hess_{U′}Ψ_min(U′; 𝔪(U)e^ρ)|_{U′=U} − B(U) is
defined for independent (U, ρ) and vanishes at ρ = 0). For 𝔏 + 𝒱^⊥[𝒯_n] it is not: Hess𝒯_n(𝔪(U)) involves the tower of 𝔪(U), which is
not U off the family, so the two pieces need not cancel at (U, 0) for U off the tower family. Use instead the V-parametrised
interpolation: with m_s := Ve^{−sρ*(V)} and φ(V, s) := −[½log det(Hess𝒯_n(V) − s𝒪(V) + D_{m_s}D_{m_s}^*) − ½log det′Δ_{m_s}], one has
𝔏(V) + 𝒱^⊥[𝒯_n](V) = φ(V, 1) − φ(V, 0) = ∫_0^1∂_sφ(V, s)ds, and ∂_sφ is linear in (𝒪(V), ρ*(V)); since 𝒪(V) = 𝒪̃(W*(V), ρ*(V)) with
𝒪̃(U, 0) ≡ 0 (Lemma ENV-𝒯 (a)-(b): R_VV, R_UV vanish at ρ = 0 for every U), 𝔏 + 𝒱^⊥ = ⟨Ξ_L(V), ρ*(V)⟩ + O(|ρ*|²) with Ξ_L smooth and
level-gauge covariant; likewise 𝔉 − 𝒲^⊥∘W* = ∫_0^1½tr[(H_W(W*) + sR_UU + D_0D_0^*)^{-1}R_UU]ds = ⟨Ξ_F(V), ρ*⟩ + O(|ρ*|²). Then
D²Δ_n(1)[v, v] = 2⟨DΞ(1)v, Dρ*(1)v⟩ + ⟨Ξ(1), D²ρ*(1)[v, v]⟩ + O(|Dρ*(1)v|²), Ξ := Ξ_F + Ξ_L + Ξ_M, and Ξ(1) = 0 (Ad-invariance, Lemma
U-tad (i)). This is the statement used in §3.5.

### 3.4 Lemma FP (the finite part of the level polarisation is bounded and Lipschitz on tree-jet classes): PROVEN-HERE
*Jet class 𝔍(m_0, C_J, c_E).* A level functional 𝒯 (Z⁴-translation invariant in level units, gauge invariant, B_4- and C-covariant,
real-analytic near 1) is in 𝔍 if (J1) β[𝒯] = 1; (J2) its Taylor kernels at 1 of orders 2, 3, 4 (exponential chart) have
|||·|||_{m_0} ≤ C_J (FLOW55 §4.3's exponentially weighted row-sum norm, so all their plane-wave symbols are analytic on
|Im| < m_0 with bounds depending on (m_0, C_J)); (J3) D²𝒯(1) ≥ c_E·d^*d on level 1-forms. (The Wilson action 𝒯_0 is in 𝔍 for
m_0 ≤ 1, C_J ≥ C_W, c_E ≤ 1.) For 𝒯, 𝒯′ ∈ 𝔍 put δ(𝒯, 𝒯′) := max_{r=2,3,4}|||D^r𝒯(1) − D^r𝒯′(1)|||_{m_0}.
*Claim.* With constants depending only on (m_0, C_J, c_E, N): (i) β_{𝒱^⊥[𝒯]}(P) = σ_⊥log(1/P) + a^⊥(𝒯) + o(1) as P → 0;
(ii) |a^⊥(𝒯) − a^⊥(𝒯_0)| ≤ C_FP; (iii) |a^⊥(𝒯) − a^⊥(𝒯′)| ≤ C′_FP·δ(𝒯, 𝒯′).
*Proof.* (1) *Fibre formula* (FLOW §88, FINE-IR-gen's proof, CONFIRMED REVIEW_FLOW_S11; it uses only translation invariance and
the analytic-symbol structure, so it holds verbatim for exponentially local Hessians): for 0 < |P| < π the ϑ-averaged ε²-density
of 𝒱^⊥[𝒯] in the root sector is ∫_{BZ}f_𝒯(K, P)dK/(2π)⁴ with f_𝒯 = c_v[tr(O_0^{-1}Ô_2) − ¼Σ_±tr(O_0(K)^{-1}V_∓O_0(K ± Pe_2)^{-1}V_±)] −
(ghost part), c_v a convention constant, O_0 = Ĥ + d̂d̂^† (Ĥ the symbol of D²𝒯(1)), V_± and Ô_2 the momentum-transfer ±Pe_2 and ϑ-free
second-order plane-wave vertices of Hess_X𝒯(Ve^X)|_0 + D_VD_V^* (the ±2P parts vanish per site). The ghost part does not depend on 𝒯.
(2) *Symbol bounds.* Ĥ = (λ̃ − ŝŝ^†) + E with E analytic, E = O(K⁴), Eŝ = 0 (L4a-Π with (J1)); so O_0 = λ̃·1 + E and, by (J3),
O_0 ≥ min(c_E, 1)λ̃. On |K| ≤ r_0 := m_0/4: |∂^αO_0^{-1}| ≤ C|K|^{-2−|α|}, |∂^α(O_0^{-1} − O_0′^{-1})| = |∂^α[O_0^{-1}(E′ − E)O_0′^{-1}]| ≤
Cδ|K|^{-|α|} (|α| ≤ 2). The vertices are fixed algebraic combinations of the plane-wave symbols of D²𝒯, D³𝒯, D⁴𝒯 (the exponential-chart
BCH corrections included) and of the gauge-fixing vertices (trigonometric polynomials, 𝒯-independent). By Proposition JET-MARG
(FLOW55 §3.3; CONFIRMED Codex §4.2: "all dimension-four Taylor pieces at orders 2–4 are fixed by β") and (J1), their marginal parts —
degree 1 for V_±, degree 0 for Ô_2 — are those of the Wilson action; parity removes the next degree. Cauchy estimates on the polydisc
of radius 2r_0 give, with r := |(K, P)| ≤ r_0 and δX := X_𝒯 − X_{𝒯′}: |∂^γV_±| ≤ Cr^{1−|γ|}, |∂^γδV_±| ≤ Cδr^{3−|γ|}, |∂^γÔ_2| ≤ C,
|∂^γδÔ_2| ≤ Cδr^{2−|γ|} (|γ| ≤ 2). Away from the origin (|K| ≥ r_0/2) all symbols are smooth, bounded with derivatives, O_0 ≥ c > 0.
(3) *Ward identity at P = 0* (FLOW §95 (G2)'s argument, which uses only gauge covariance): at P = 0 the constant Cartan field is
pure gauge on the infinite lattice, the operator is conjugated by a phase, its symbol is shifted K_1 → K_1 + qεcosϑ, and f_𝒯(K, 0) =
c·∂_{K_1}tr(O_0^{-1}∂_{K_1}O_0) − (ghost analogue): a K_1-derivative of a periodic function that is O(|K|^{-1}) with derivative in L¹,
so ∫_{BZ}f_𝒯(K, 0)dK = 0.
(4) *Parity:* f_𝒯(−K, −P) = f_𝒯(K, P) (automatic, FLOW [RFL11-fix S11-3]).
(5) *Estimate* (the template of FLOW Theorem UIR-S step (4), with real-variable symbol bounds in place of Cauchy estimates at 0,
because O_0^{-1} is not λ̃^{-1} times an analytic function — the [S10-corr] phenomenon, here for the vector). D := f_𝒯 − f_{𝒯′} is a sum
of terms each with exactly one δ-factor (telescoping), and by (2), for r ≤ r_0:
  |D(K, P)| ≤ Cδ[1 + r²(|K|^{-2} + |K + P|^{-2} + |K − P|^{-2}) + r⁴|K|^{-2}(|K + P|^{-2} + |K − P|^{-2})];
on {2|P| ≤ |K| ≤ r_0}, |∂^j_{P_2}D(K, tP)| ≤ Cδ|K|^{-j}, j ≤ 2, |t| ≤ 1 (there |K ± tP| ≥ |K|/2 and r ≤ 2|K|). Hence:
∫_{|K|<2|P|}|D(K, P)|dK ≤ CδP⁴ (scaling; separated integrable singularities); ∫_{|K|≥2|P|}D(K, 0)dK = −∫_{|K|<2|P|}D(K, 0)dK = O(δP⁴) by
(3) for 𝒯 and 𝒯′; ∫_{|K|≥2|P|}∂_{P_2}D(K, 0)dK = 0 by (4) (odd integrand, symmetric region, |∂_{P_2}D(K, 0)| ≤ Cδ|K|^{-1}); and the Taylor
remainder gives ∫_{|K|≥2|P|}[D(K, P) − D(K, 0) − P∂_{P_2}D(K, 0)]dK = (P²/2)∫_{BZ}∂²_{P_2}D(K, 0)dK + o(P²) by dominated convergence
(dominant Cδ|K|^{-2} ∈ L¹). Dividing by the Wilson density ∝ |ŝ_2(P)|² = P²(1 + O(P²)): β_{𝒱^⊥[𝒯]}(P) − β_{𝒱^⊥[𝒯′]}(P) → c∫_{BZ}∂²_{P_2}D(K, 0)dK,
|·| ≤ cCδ(∫_{|K|≤r_0}|K|^{-2}dK + (2π)⁴) =: C′_FPδ. That is (iii); (ii) is (iii) with 𝒯′ = 𝒯_0 and δ ≤ C_J + C_W; (i) follows from (ii)'s limit
and VFINE-K/VFINE-gh for 𝒯_0 (𝒱^⊥[𝒯_0] = 𝒲^⊥). ∎
*Reading.* The leading (degree −4) homogeneous part of the p²-integrand — the only part that can produce a log — is the same for every
𝒯 ∈ 𝔍: it is fixed by the marginal jets, which JET-MARG ties to β[𝒯] = 1. So the irrelevant parts of the tree jets move only the
finite part, by an amount controlled by their size. This is the vector form of FLOW Lemma VC (ii) ("the leading minimal-coupling
structure is n-independent") without the explicit alias sums: the alias structure of the fine lattice is invisible in level units.

### 3.5 (ρ-null) — the equation-of-motion term has no β: ARGUED (not proven)
*Statement.* Ρ_n = 0 for every n.
*What is proven.* By §3.3 (δ) and its correction, β_{Δ_n}(P)·(Wilson density) = 2⟨D̂Ξ(1)(P)v̂, 𝒞̂(P)Ĥ_n(P)v̂⟩ + (a term quadratic in
𝒞̂Ĥ_nv̂ = O(P²), with at most a massless-bubble kernel O(log(1/P))), for the transverse unit v̂ of the plane wave; and 𝒞̂(P)Ĥ_n(P)v̂ =
c_𝒞|ŝ(P)|²v̂ + O(P⁴) (𝒞̂ analytic, 𝒞̂(0) = c_𝒞·1 by B_4; Ĥ_nv̂ = |ŝ|²v̂ + O(P⁴) by F-tree). So Ρ_n = 2c_𝒞·lim_{P→0}⟨D̂Ξ(1)(P)v̂, v̂⟩ whenever the
limit exists. Gauge covariance (Ξ(V^h) = Ad_hΞ(V), Ξ(1) = 0) gives D̂Ξ(1)(P)ŝ(P) = 0 for all P. **If D̂Ξ(1) is continuous at P = 0 as a
matrix-valued function, then D̂Ξ(1)(0) = 0** (for every unit ê, D̂Ξ(1)(0)ê = lim_{t→0}D̂Ξ(1)(tê)ŝ(tê)/|ŝ(tê)| up to a phase = 0), **and
Ρ_n = 0.** This is the K̄-tad mechanism (FLOW55 §5.3, CONFIRMED Codex §2.3), where continuity came from an ℓ¹ kernel.
*Why continuity is expected (the ARGUED part).* DΞ(1) is a finite sum of fixed-n one-loop expressions: fine loops with the massless
fine Feynman propagator (Ξ_F), level loops with the massless level propagator (H_n + dd^*)^{-1} (Ξ_L), and the level-group Hessian
(Ξ_M). Their external couplings are local: the residual leg enters only through Π_mρ* = ∇𝒯_n (the Gauss–Newton term), through
𝒞Π_mρ* = ρ* (by ENV applied to the h-minimisation, ψ's cubic r-jet is ψ_3[𝒞Π_m·, 𝒞Π_m·, 𝒞Π_m·], because the linear h-tower is
1 + D_mDh* = 𝒞Π_m), or through BCH commutators [·, ρ*]; Π_m, P_⊥ and the massless h-Green function act only on internal loop momenta,
where they are integrated. The background leg enters through vertices with at least one momentum factor (Wilson, D³𝒯_n, gauge
fixing) or through local IR-term vertices. At fixed n every integrand is then dominated near K = 0 and K = −P by C|K|^{-a}|K + P|^{-b},
a + b ≤ 3, uniformly for small P; dominated convergence gives continuity. For Ξ_M separately: Hess L(1) is the difference of two massless
level scalar loops (½log det′(D^*𝒞^{-1}D) − ½log det′(D^*D)) with the same leading symbol up to the constant c_𝒞^{-1}, so it is O(P²) and
contributes O(P⁴).
*What would refute (ρ-null).* A term of DΞ(1) whose dependence on the EXTERNAL momentum is a bare level transverse projector P_⊥(P)
(or Π̂_m(P)) acting on the external leg: m·P_⊥(P) satisfies the gauge covariance and contributes 2c_𝒞m to Ρ_n. I found none in the
structure above, but **a term-by-term enumeration of DΞ(1) with its domination bounds is not written** — hence ARGUED. (ρ-null) is a
fixed-n statement: it needs no uniformity in n.

### 3.6 Theorem UIR-T (the n-uniform bound, conditional): PROVEN-HERE as an implication
*Hypothesis (TC-b)_𝔍.* There are m_0 > 0 and C_J such that 𝒯_n ∈ 𝔍(m_0, C_J, c_E) for every n ≥ 0, i.e. (J2) holds n-uniformly. Status:
(J1) β[𝒯_n] = 1 — FLOW Lemma F-tree (CONFIRMED upstream); (J3) with c_E = 2κ/(π²(κ + 4π²R̄)) uniformly in n — LINEAR_PACKAGE Lemma 2.7
(E-low; CONFIRMED upstream); (J2) at order 2 uniformly in n — FLOW Lemma H-sym (from N2-exp′ (ii), CONFIRMED REVIEW_FLOW_S3);
**(J2) at orders 3 and 4: OPEN** (order 3: Theorem N1-15 gives an n-uniform bound in the UNWEIGHTED N3 norm, CONDITIONAL; order 4:
nothing). This is FLOW55's (TC-b), without (TC-c).
*Claim.* Given (TC-b)_𝔍: for every n ≥ 1, |β[G^♮_⊥,n] + (21/22)β_0^std·n log L − Ρ_n| ≤ C_FP + C_FP (= 2C_FP, from Lemma FP (ii) at 𝒯_n
and 𝒯_0 = Wilson's a^⊥ itself is a^⊥(J_0)). Hence **(ρ-null) + (TC-b)_𝔍 ⇒ (UIR^♮) ⇔ (UNIV-1L)**, with the explicit additive constant
R ≤ 2C_FP(m_0, C_J, c_E, N), uniformly in n and in the volume.
*Rate form.* If moreover (TC-c): δ(𝒯_{n+1}, 𝒯_n) ≤ C_Tθ^n, then by Lemma FP (iii), given (ρ-null),
|β[G^♮_⊥,n+1] − β[G^♮_⊥,n] + (21/22)β_0^std log L| ≤ C′_FPC_Tθ^n, and β[G^♮_⊥,n] + (21/22)β_0^std n log L converges (to a^⊥(J_0) − a^⊥(J_∞)).
*Proof.* Theorem TEL and Lemma FP. ∎
*Corollary (the value of b_∞).* Given (ρ-null), B_{n+1} − B_n = β_0^std log L + a^⊥(J_{n+1}) − a^⊥(J_n). If the tree-jet recursion
J_{k+1} = 𝔗(J_k; K) of FLOW55 §4.2 converges in 𝔍 to a fixed point J_∞, the per-step coefficient tends to β_0^std log L. **This answers
FLOW55 Proposition PS's open point ("with NO statement about the value of b_∞"): (TC) together with (ρ-null) fixes b_∞ = β_0^std log L.**
FLOW55's sentence "no single one-step Gaussian integral at fixed L delivers it" stays true: the value is carried by the n-independent
FINE Wilson functional 𝒲^⊥ evaluated at the scale ratio ℓ (a multi-scale object), not by the one-step integral.

### 3.7 What the split changes, κ, the volume, and where the analytic-strip and alias data enter
- **Absorbed (no longer needed for (UIR^♮)):** FLOW's (a2) (IR-term vertices) and (c)/(s2⊥) (the level group): Lemma SPLIT combines
  them exactly into the level tree group; the residue-lemma inputs (R-a_int), (R-b) for the K̄ integrand: not used; FLOW's T-split items
  (T-a1), (T-a1-M), (T-a3), (T-b): replaced by (TC-b)_𝔍 at orders 3, 4 (tree level) + JET-MARG (proven) + Theorem TEL (proven given its
  inputs); (T-c): not needed (U = 1 throughout, as FLOW55 intended).
- **Remaining for (UIR^♮):** (TC-b)_𝔍 at orders 3 and 4 (a tree-level, classical statement about the stripped tower) and (ρ-null) (a
  fixed-n statement). Nothing n-uniform at one loop is left.
- **The massless fine inverse.** H_W(1)^{-1} (the unconstrained, massless fine Wilson propagator) DOES appear — but only inside the
  n-independent fine functional 𝒲^⊥, whose asymptotics are VFINE-K (CONFIRMED). This revises FLOW55 §8 ("the only fine inverse left is
  the gapped (H^♮_⊥(1))^{-1}") as a recommendation: quarantining the massless inverse in an n-independent object is what makes the
  n-uniform problem one-scale.
- **κ.** κ enters J_n and the class constants (m_0, C_J, c_E(κ)), and Ρ_n; the slope σ_⊥ comes from 𝒲^⊥, which contains no κ. So κ
  enters only the O(1) constant (FLOW55 Proposition KAPPA's conclusion), now with an explicit n-uniform constant 2C_FP in terms of tree
  data. No uniformity as κ → 0 (c_E → 0) or κ → ∞ is claimed.
- **Volume.** All objects are infinite-volume densities; the antiperiodic tori are a device (FLOW §75 (b)); T-uniform by construction.
- **Analytic strip and aliases.** In this organisation the alias structure (Dirichlet factors, the strip of GSHARP55 §3.4 for the K ≠ 0
  alias denominators, |Im p_α| ≤ 1.4) enters only through the proof of (TC-b)_𝔍: D³𝒯_n, D⁴𝒯_n are, by Lemma ENV (FLOW55 §4.1),
  D³F[ζ³] and D⁴F[ζ⁴] − 3c^*(H^♮|_{E_0})^{-1}c with the linear tower ζ, whose level-unit kernels are exponentially local uniformly in n
  (LINEAR_PACKAGE Theorem 4.2′, rate m_*′ = 0.0384 at κ = 1, L = 3 — the binding strip is the K = 0 screened one, not GSHARP55's 1.4);
  so one expects m_0 ≲ m_*′. The (TC-b) proof itself is not attempted here.

**Correction to §3.6 (appended at once; the stated bound was true but loose and its justification garbled).** By Theorem TEL,
β[G^♮_⊥,n] + (21/22)β_0^std n log L − Ρ_n = a^⊥(J_0) − a^⊥(J_n) = a^⊥(𝒯_0) − a^⊥(𝒯_n), and Lemma FP (ii) bounds this by C_FP directly.
Read "≤ C_FP + C_FP (= 2C_FP, …)" as "≤ C_FP", and "R ≤ 2C_FP" as "R ≤ C_FP".

### 2.5 Addendum to §2 (explicit level-unit symbols at U = 1; written after §3, append-only)
In level units (level momentum K, fine aliases x_m := K + 2πm with representatives |x_{m,α}| ≤ πℓ, s_ℓ(x) := ℓ sin(x/2ℓ)), FLOW's Prop.
VC-T0 (CONFIRMED, REVIEW_FLOW_S12) gives the two transverse level symbols that build Ĥ_n:
- the soft-kernel (noise) part: P_⊥𝒞̂_nP_⊥ = κ^{-1}P_{T,ℓ}(K)[Σ_{i<n}s_i(K)]P_{T,ℓ}(K), s_i the i-step straight-average Gram symbol, ||s_i|| ≤ L^{-2i}
  (the d∘h part of S4′ drops out exactly because P_⊥A_j = P_⊥Q_str^{(L^i)});
- the block-averaged massless fine propagator: P_⊥Q_strgQ_str^*P_⊥ = P_{T,ℓ}diag(x^{blk}_{n,μ}(K))P_{T,ℓ},
  x^{blk}_{n,μ}(K) = Σ_m ℓ^{-4}|S_μ(x_{m,μ}/ℓ)|²Π_αD_ℓ(x_{m,α}/ℓ)²/λ(x_m/ℓ) (two Dirichlet factors in the leg direction, consistent with
  Finding 2.1), converging at rate ℓ^{-2} to Σ_{m∈Z⁴}|e^{ix_μ} − 1|²x_μ^{-2}Π_α(sin(x_α/2)/(x_α/2))²/|x|².
Then Ĥ_n|_⊥ = (κ^{-1}P_{T,ℓ}Σ_{i<n}s_iP_{T,ℓ} + P_{T,ℓ}diag(x^{blk}_n)P_{T,ℓ})^{-1} on the transverse range: the κ-dependence of the K̄ unit at
U = 1 is entirely in the first bracket, and both brackets converge geometrically in n (VC-T0). β extracts, in §3's organisation,
the finite part of the one-scale polarisation built from Ĥ_n and the plane-wave symbols of D³𝒯_n(1), D⁴𝒯_n(1) (Lemma FP), plus the
fine Wilson log of §4.

---

## 4. U3 — the leading coefficient

### 4.1 Where it comes from (PROVEN-HERE as a consequence of Theorem TEL, given VFINE-K/VFINE-gh)
By Theorem TEL, the coefficient of n log L in β[G^♮_⊥,n] is the log coefficient σ_⊥ of the n-INDEPENDENT fine Wilson transverse group
𝒲^⊥ = ½log det(H_W + DD^*) − ½log det′Δ (vector minus half ghost), evaluated at the scale ratio ℓ = L^n. The level piece has the same
log coefficient (Lemma FP (i): the degree −4 part of its integrand is fixed by the marginal jets, which JET-MARG ties to β[𝒯_n] = 1), so
it contributes no n log L. Hence the coefficient is κ-independent and scheme-independent in the sense of FLOW Lemma U-res Remark (1):
only the leading homogeneous continuum integrand of 𝒲^⊥ enters. Its value (FLOW §88/§95 VFINE-K-val, CONFIRMED REVIEW_FLOW_S11/S12;
Codex §5.2 for the arithmetic): per positive root of charge q (one complex field), vector C_{K_F} = −20q²c_g, ghost +q²c_g, so the
transverse group is −21q²c_g and the full group −22q²c_g per unit P²log; with the Wilson-wave normalisation P²/4 and Σ_{α>0}q_α² = N²:
**σ_⊥ = −84N²c_g = −7N²/(8π²) = −(21/22)β_0^std**, the ghost group −4N²c_g = −(1/22)β_0^std, total −β_0^std, β_0^std = 2N·2b_0 = 11N²/(12π²).
(The brief's "β_0^std = 11N/(48π²)" is b_0; see the PRE-STATED symbol pins.)

### 4.2 Exact control ui55_2 (criteria checks/ui55_2_criteria.md, written 03:40Z before any ui55_2 script)
Independent of fl55_1's heat-kernel route: the vertices are derived symbolically from the continuum operator
O_c = (−i∂ − qa e_1)²·1 + s·iqF (s = 2) acting on u·e^{ik·x} at the plane wave a = εcos(px_2 + ϑ) — giving V_± = −qk_1·1 ± (s/2)qp(E_12 − E_21),
Ô_2 = (q²/2)·1 — the ε²-integrand f(k, p) is expanded at large |k| = R with |n| = 1, and the R^{-4} coefficient h(n) is averaged over S³ with
exact moments (Gaussian-moment formula, cross-checked by direct sympy integration in hyperspherical coordinates). Results (run 2):
h_S(n) = n_1² − 4n_1²n_2², ⟨h_S⟩ = 1/12, so C_S = q²/(96π²) = q²c_g; h_V(n) = 4h_S(n) − 2 (orbital ×4, spin −s²/2), ⟨h_V⟩ = −5/3, ratio −20;
the R^{-3} terms vanish identically; transverse/full = 21/22; Σ_{i<j}(h_i − h_j)² = NΣh_i² − (Σh_i)² identically (N = 2, 3, 4); u-unit slopes
−84N²c_g = −(21/22)β_0^std and −4N²c_g = −(1/22)β_0^std, summing to −β_0^std = −11N²/(12π²). Controls fire: spin coupling 1 gives ratio −2;
the product-of-marginals moment 1/16 gives ⟨h_S⟩ = 0; the FN-1 slip 2N·b_0 ≠ 88N²c_g.
**Run record (honest).** Run 1 (03:42Z, md5 963bbc81fbd2630f9c7d10815fbc21fe, script kept as checks/ui55_2_run1.py, output kept unaltered as
checks/ui55_2_out.txt): **9/11 — L1 and L3 FAIL** because of a script defect: h was computed with the charge q symbolic and the
criteria's C = q²⟨h⟩/(8π²) then applied q² a second time (L3), and L1 compared ⟨h_S⟩ = q²/12 with 1/12. The printed run-1 values
(⟨h_S⟩ = q²/12, ⟨h_V⟩ = −5q²/3, ratio −20) are the pre-registered ones at unit charge. Fix (one line, q := 1 inside h before
averaging, as the criteria define ⟨h⟩; criteria unchanged): run 2 (03:44Z, md5 20528e40d904b5cf84ef9505e8ff7bb2, output
checks/ui55_2_run2_out.txt): **11/11 PASS, three controls fire** (0.5 s, 65 MB). The verdict I use is run 2's; run 1 is a defect of
the script, not of the mathematics, and is recorded so that it can be checked.
*Scope.* Continuum leading integrands only; the lattice → continuum step is FLOW Lemma U-Tay / FINE-IR-gen / CL-V (CONFIRMED
upstream, not re-tested). **No small-n lattice control of β[G^♮_⊥,n] itself is given:** in §3's organisation it equals
σ_⊥ n log L + a^⊥(J_0) − a^⊥(J_n) (given (ρ-null)), and a rigorous-interval evaluation of a^⊥(J_n) for n ≥ 1 needs the tree jets D³𝒯_n(1),
D⁴𝒯_n(1), which are not available in closed form; FLOW's float checks f2/f3/f5 are consistent but are not verdicts under this brief.
*Timestamp correction to §4.2 (from `ls -T`, local clock UTC−4h):* ui55_2_criteria.md 03:40:28Z; run 1 output 03:42:36Z; run 2 output
03:42:55Z (not "03:44Z"). The ui55_2 script was rewritten once BEFORE its first run (the first draft extracted vertices by substituting
exponentials, which sympy can merge; it was never executed); run 1 used the rewritten script (md5 963bbc81…), run 2 the one-line fix.
ui55_1: criteria 03:29:49Z, script 03:31:16Z, single run 03:31:33Z.

---

## 5. U4 — what is PROVEN, what is CONDITIONAL, what is OPEN

| item | statement | status here |
|---|---|---|
| Lemma P♮ (§2.2) | K̄ propagator at U = 1 = C^⊥_n ⊕ dΔ_0^{-2}d^*, no cross block; longitudinal part exactly massless Feynman; alias-block Woodbury form | PROVEN-HERE; exact check ui55_1 B |
| Finding 2.1 | composite straight average has two Dirichlet factors in the leg direction; FLOW §24 (F2)'s formula is the face average; bounds unaffected | PROVEN-HERE; ui55_1 C |
| Lemma SPLIT (§3.1) | G^♮_⊥,n = 𝔉 + 𝔏 + 𝔐 exactly at every V near 1, both parts of H^♮ exactly transverse | PROVEN-HERE (one-loop level of FLOW/FLOW55); algebra ui55_1 A |
| Lemma ENV-𝒯 (§3.2) | 𝔅 = Hess𝒯_n − 𝒪, A = H_W(W*) + R_UU, 𝒪, R vanish at ρ* = 0; ρ* = 𝒞∇𝒯_n at linear order | PROVEN-HERE |
| Theorem TEL (§3.3) | β[G^♮_⊥,n] + (21/22)β_0^std n log L = a^⊥(J_0) − a^⊥(J_n) + Ρ_n, Ρ_n the β of an equation-of-motion term | PROVEN-HERE given VFINE-K/VFINE-gh, F-bg, F-tree, FLOW55 K̄-β (upstream CONFIRMED) and Lemma FP |
| Lemma FP (§3.4) | finite part a^⊥ of the one-scale level polarisation is bounded and Lipschitz on tree-jet classes 𝔍(m_0, C_J, c_E) | PROVEN-HERE |
| (ρ-null) (§3.5) | Ρ_n = 0 for each n | ARGUED (criterion and mechanism stated; term-by-term domination not written) |
| (TC-b)_𝔍 orders 2 | n-uniform exponential locality and gap of D²𝒯_n(1); β[𝒯_n] = 1 | PROVEN upstream (H-sym, E-low, F-tree) |
| (TC-b)_𝔍 orders 3, 4 | n-uniform exponentially weighted bounds on D³𝒯_n(1), D⁴𝒯_n(1) | **OPEN** (order 3: N1-15 unweighted, CONDITIONAL; order 4: nothing) |
| Theorem UIR-T (§3.6) | (TC-b)_𝔍 + (ρ-null) ⇒ (UIR^♮) ⇔ (UNIV-1L), R ≤ C_FP; (TC-c) ⇒ geometric per-level convergence | PROVEN-HERE as an implication |
| Corollary b_∞ | (TC) + (ρ-null) ⇒ b_∞ = β_0^std log L | PROVEN-HERE as an implication |
| §4.1 | the n log L coefficient comes only from the n-independent fine Wilson group; value −(21/22)β_0^std | PROVEN-HERE given TEL; value CONFIRMED upstream and re-derived exactly in ui55_2 |
| **(UIR^♮)** | sup_n|β[G^♮_⊥,n] + (21/22)β_0^std n log L| < ∞ | **OPEN — reduced to (TC-b)_𝔍 at orders 3, 4 (tree level) and (ρ-null) (fixed n)** |
| κ-dependence | κ only in the O(1) constant (through J_n, the class constants and Ρ_n); slope κ-free | PROVEN-HERE given the above (no uniformity as κ → 0, ∞) |
| volume | everything in infinite volume; T-uniform | PROVEN-HERE (definitions) |

**Scope remark (Cartan sector; appended for completeness).** §3 was written in a root sector α. At a Cartan background the Cartan
sector also feels the background at second order (Wilson: cos F_P in the abelian plaquette; the kernel: the polar positive part P of the
contour average), but only through vertices of total degree ≥ 4 in (K, P) (e.g. F_b²(dX)² ~ P²K²); its contribution to every
β_F(P) has no log and its plane-wave integrand is dominated as in Lemma FP (5). Lemma SPLIT holds fibrewise in infinite volume for
a.e. level momentum K (each class is finite-dimensional; the plane wave couples finitely many classes at each order in ε), which
covers the Cartan sector without twisted tori. So Theorem TEL and Lemma FP hold with all sectors included; a^⊥ includes the finite
Cartan-sector contribution.

**Notation collisions met in this file (systemic defect 1).** (a) Codex §1.3's A = Hess_hΨ and B (blocks of the joint Hessian) are NOT
§3's A := H^♮ − B and B := M^*Π_mM. (b) Δ_n (no other subscript) in §3.3-§3.6 is the equation-of-motion remainder functional; Δ_0, Δ_{W*},
Δ_m, Δ_V are Laplacians; FLOW's Δ^⊥_n is the transverse propagator correction. (c) R in §3.6 ("R ≤ C_FP") is FLOW's additive constant
of (F_R)/(UNIV-1L); R_UU, R_UV, R_VV are §3.2's residual blocks; FLOW55's R is Hess_hΨ − 𝔊_0. (d) c_E in (J3) is any constant with
D²𝒯_n(1) ≥ c_E d^*d; LINEAR_PACKAGE's c_E (Lemma 2.7) gives H_n ≥ 2c_E^{LP}d^*d, so (J3) holds with c_E := c_E^{LP} (with room 2).
(e) M is FLOW55's M_U = D𝔪_n(U) at U = W*, not FLOW's M-cubes nor LINEAR_PACKAGE's constant M. (f) σ_⊥ is FLOW U-res's σ_h for the
transverse group (per unit log, u-units). (g) β[·] (the functional), β_F(P) (the plane-wave ratio), β_0^std, β_k (coupling shift) are
distinct. Stale-quantifier check (defect 2): the only numbers quoted are m_*′ = 0.0384 (κ = 1, L = 3, LINEAR_PACKAGE Theorem 4.2′) and
the strip 1.4 (GSHARP55, K ≠ 0 alias denominators only, n ≥ 3), each with its parameters; no inequality here is evaluated at a constant
that later became an output. Decidability (defect 3): ui55_1's controls show that FLOW's pre-K̄ IR term fails the identities, that the
split fails without the level group, and that a non-transverse A fails the Feynman form; ui55_2's controls show that the wrong spin
coupling, the product-of-marginals moment and the FN-1 slip each change the verdict. Neither check can decide anything n-uniform, and
none is used as evidence for (UIR^♮).

## 6. Codex verdicts used (agree / disagree), errata to the stopped draft, findings against other files

**Codex verdicts (CODEX_REVIEW_FLOW55.md, read in full as on disk 02:45Z; complete).** I agree with each verdict I use:
§1.1 (K̄ exact; H^♮D_0 = 0 only at the critical saddle) — AGREE, used in Lemma SPLIT (i) exactly in that form; §1.2 (φ-tower, not
k̃, for N ≥ 3; trivial-point jets of order ≤ 5 agree) — AGREE, §3 uses the normalised φ-objects and only order ≤ 4 Taylor data at 1;
§1.3 (Schur/envelope, quotient factors, the Π identity and the coarse determinant identity) — AGREE, used in Lemma P♮, SPLIT, ENV-𝒯;
§2.3 (K̄-tad at fixed n; the "one place" sentence NOT-VERIFIED as exhaustive) — AGREE; §3's equation-of-motion terms are exactly the kind
of further κ-dependent fixed-n terms the Codex said were not excluded, and (ρ-null) is where they are now isolated; §3.1-§3.2 (GH0;
K̄-β as a conditional coefficient reduction) — AGREE, used in Theorem TEL; §3.3 ((UIR^♮) does not imply (R-a)/(R-b)) — AGREE, and §3
does not use the residue lemma at all; §4.2 (JET-MARG; the symmetric-channel sentence REFUTED) — AGREE, used in Lemma FP (2);
§5.2 (arithmetic 11 = 12 − 1, 2N·2b_0, 21/22) — AGREE, independently re-derived in ui55_2.

**Errata to the stopped draft (§1 above; not edited).** E-1: the forward references in §1's last paragraph ("re-derived in §2.2
and §3.3 below", "§3.1", "§3.4") name sections of the stopped run's plan. In this file: Lemma U-T⊥ is re-derived in §2.2 (Lemma P♮);
Proposition U-a1⊥ is NOT re-derived (§3's route does not use it; only its degree count was re-checked against Finding 2.1); Lemma
U-res/U-res′ are not used; VFINE-K/VFINE-L's arithmetic is re-checked in §4 (ui55_2) as promised; Lemma Cartan-𝔪/Cartan-T enter §2.3
(V-M). No mathematical error was found in §1; its quotations of the Codex verdicts are accurate.

**Findings against other files (none applied; this worker writes only UIR55.md and checks/ui55_*).**
- FLOW §24 (F2): the composite straight-average symbol has an extra factor D_ℓ(q_μ) (Finding 2.1). REFUTED as a literal formula;
  every bound built on it stands (|D_ℓ| ≤ 1, Lemma DIR).
- FLOW55 §5.5, "FLOW's Woodbury split … is not available off-shell without re-introducing the defect": REFUTED as stated — the split
  exists exactly at every V (Lemma SPLIT), with both parts exactly transverse; what survives of the concern is the equation-of-motion
  item (ρ-null), a fixed-n statement.
- FLOW55 §8, "the only fine inverse left is the gapped (H^♮_⊥(1))^{-1}": true of the unsplit K̄ form, but as a route recommendation it is
  superseded: the massless H_W(1)^{-1} is harmless once quarantined in the n-independent 𝒲^⊥ (VFINE-K), and that is what makes the
  n-uniform problem one-scale.
- FLOW55 Proposition PS, "with NO statement about the value of b_∞": given (ρ-null), (TC) fixes b_∞ = β_0^std log L (Corollary b_∞).

### 3.5′ Erratum to §3.5 and the refined criterion for (ρ-null) (appended after re-reading §3.5; (ρ-null) stays ARGUED)
**Erratum.** §3.5's paragraph "Why continuity is expected" is wrong as written: it lists "Π_mρ* = ∇𝒯_n (the Gauss–Newton term)" among
the external couplings and then claims D̂Ξ(1) is continuous at P = 0. But in that term Π_m acts on the residual leg AT THE EXTERNAL
MOMENTUM, so D̂Ξ(1)(P) contains the factor Π̂_m(P) on its ρ-slot and is not continuous at P = 0 (its longitudinal part is direction
dependent). The sufficient condition "D̂Ξ(1) continuous" therefore FAILS for the actual Ξ, and §3.5's argument does not establish Ρ_n = 0.
**Why this matters (the precise failure mode).** A covariant coefficient of the form Ξ[w] = y⟨Π_m(V)·log V, w⟩ satisfies
D̂Ξ(1)(P)ŝ(P) = yΠ̂_m(P)ŝ(P) = 0 (gauge covariance holds) and pairs with ρ* to y⟨v, Π_mρ*⟩ = y⟨v, ∇𝒯_n(v)⟩ = 2y𝒯_n^{(2)}(v): a pure
coupling shift, Ρ_n = 2y ≠ 0. So gauge covariance of Ξ alone does NOT force Ρ_n = 0; an equation-of-motion term with a non-local
(transverse-projected) coefficient can renormalise β.
**Refined criterion (sufficient).** Suppose Ξ admits a decomposition Ξ(V)[w] = Σ_j⟨𝔱_j(V), 𝒦_j(V)w⟩ in which (a) each 𝔱_j is a
level-gauge-covariant functional (𝔱_j(V^h) = Ad_h𝔱_j(V)) with 𝔱_j(1) = 0 and a derivative symbol Y_j(P) := D̂𝔱_j(1)(P) continuous at
P = 0; (b) each pairing map 𝒦_j(V) is fixed linear algebra (𝒦_j ∈ {Π_m, 𝒞Π_m, 1, commutators [·, ·]}) with 𝒦̂_j(P)𝒞̂(P)Ĥ_n(P)v̂ = O(P²)
for transverse v̂. Then Ρ_n = 0: D²Δ_n(1)[v, v] = 2Σ_j⟨Y_j(P)v̂, 𝒦̂_j(P)𝒞̂Ĥ_nv̂⟩ + o(P²) (the term ⟨𝔱_j(1), D𝒦_j[v]w⟩ vanishes), covariance of 𝔱_j
gives Y_j(P)ŝ(P) = 0, continuity gives Y_j(0) = 0, so each term is o(P²). (Here the discontinuous Π̂_m(P) sits in 𝒦̂_j, where it acts on
𝒞̂Ĥ_nv̂ and returns Ĥ_nv̂, which is analytic.)
**Why (a)-(b) are expected for the actual Ξ (ARGUED).** The residual enters H^♮, 𝔅 and the level group only through the expansion of
ψ(U, r) at r = ρ*: as ψ_r = Π_mρ* + ψ_3[·, ·, 𝒞Π_mρ*]-terms (pairing map Π_m or 𝒞Π_m), as ψ_rr(ρ*) − Π_m = ψ_3[𝒞Π_m·, 𝒞Π_m·, 𝒞Π_mρ*]
(pairing 𝒞Π_m, by ENV for the h-minimisation: the linear h-tower is 1 + D_mDh* = 𝒞Π_m), and through BCH commutators with ρ* = 𝒞Π_mρ*.
In each case the coefficient 𝔱_j is a one-loop trace built from covariant objects (fine massless G_W, level massless (Hess𝒯_n +
D_VD_V^*)^{-1}, the gapped K̄ fine propagator, D𝔪, D²𝔪, 𝒞, internal Π_m and internal h-Green functions), hence covariant, and its
derivative symbol is a loop integral whose integrand is dominated near the internal singular points by C|K|^{-a}|K + P|^{-b}, a + b ≤ 3
(at least one momentum factor at each massless vertex), uniformly for small P; P-poles-type internal factors (FLOW Lemma P-poles:
first-order numerators λ̃(K)λ̃(K + P)[ε]P = O(|K||K + P|)) keep the singularities at |K|^{-1}. **The one thing that would refute (ρ-null):**
a term in which a background-dependent Π_m(V) multiplies a quantity that is first order in v and is NOT itself paired with ρ* through
a covariant functional — i.e. a 𝔱_j of the form Π_m(V)f(V) with f(1) = 0 but f not covariant. I found no such term, but the enumeration
is not written. (ρ-null) remains ARGUED; it is the single fixed-n item between Theorem TEL and an unconditional reduction of
(UIR^♮) to (TC-b)_𝔍.

## 7. FOR OTHER FILES (demands raised here; none applied)
- **FLOW / FLOW55 (lane C).** After an independent review of §3: adopt Lemma SPLIT → Lemma ENV-𝒯 → Theorem TEL → Lemma FP, and restate the
  coupling-flow wall as **(TC-b)_𝔍 at orders 3, 4 (tree level) + (ρ-null) (fixed n)**. For this route the following are no longer
  needed: FLOW's (a2), (c)/(s2⊥), (R-b), (T-a1), (T-a1-M), (T-a3), (T-b), (T-c), (L-loc2), and the residue-lemma decomposition of the K̄
  integrand. Correct FLOW §24 (F2)'s symbol (Finding 2.1; bounds unchanged). Withdraw FLOW55 §5.5's sentence that the Woodbury split is
  unavailable off-shell; keep its caution in the form (ρ-null).
- **Layer 1 (lane A / NORMS / T-UNIF).** The (TC-b) items FLOW55 §9 already requested — an exponentially weighted version of Theorem
  N1-15 (order 3) and its quartic analogue including the tree exchange term −3c^*(H^♮|_{E_0})^{-1}c — now deliver (UIR^♮) (given (ρ-null)),
  not only (F-1) with an unknown slope. Convergence (TC-c) is not needed for (UIR^♮); it gives the geometric per-level rate.
- **HANDOFF, critical-path item 6** (after review): "FLOW: (UIR^♮) ⟸ (TC-b)_𝔍 at orders 3, 4 (n-uniform exponentially weighted bounds on
  D³𝒯_n(1), D⁴𝒯_n(1) of the stripped φ-tower) + (ρ-null) (a fixed-n equation-of-motion statement, ARGUED). The n-uniform one-loop
  estimate is no longer a separate wall: the transverse group telescopes exactly into the n-independent fine Wilson group at scale ratio
  ℓ minus the one-scale level-n group of the tree action (UIR55 §3)."
- **PROOF.md tally.** No item moves to PROVEN: (UIR^♮) ⇔ (UNIV-1L) stays OPEN. New unreviewed PROVEN-HERE items of this file: Lemma P♮,
  Finding 2.1, Lemma SPLIT, Lemma ENV-𝒯, Theorem TEL (given its named inputs), Lemma FP, Theorem UIR-T and Corollary b_∞ (as implications).
- **For the Codex reviewer, the load-bearing steps to attack:** (1) Lemma SPLIT (i)-(iii), in particular that B is built with Π at
  m = 𝔪(W*) (so BD_0 = 0) while FLOW55's level group sits at V (the 𝔐 term); (2) Theorem TEL step (α), the tower transfer for the massless
  fine functional 𝒲^⊥ (diagonality in fine momentum, alias orders, the o(1) error with a log); (3) Lemma FP step (5), the bounds near the
  merging singularities K = 0, ∓P and the use of JET-MARG for the vertex differences; (4) §3.5′, whether any coefficient 𝔱_j of the form
  Π_m(V)f(V) with non-covariant f occurs (that is the only way (ρ-null) can fail).

## 8. Summary table (claims of this file) and counts

| # | claim (locating string) | status |
|---|---|---|
| 1 | Finding 2.1 ("Finding 2.1 (minor erratum to FLOW §24 (F2)") | PROVEN-HERE; ui55_1 C |
| 2 | Lemma P♮ ("### 2.2 Lemma P♮") | PROVEN-HERE; ui55_1 B |
| 3 | §2.3 vertex classes; (V-Π) vertices non-local (P_⊥(P), massless h-Green function) | PROVEN-HERE (structure) |
| 4 | §2.4 a termwise residue-lemma attack has to group IR-term and level-group pieces | ARGUED, not used |
| 5 | Lemma SPLIT ("### 3.1 Lemma SPLIT") | PROVEN-HERE; algebra ui55_1 A |
| 6 | Lemma ENV-𝒯 ("### 3.2 Lemma ENV-𝒯") | PROVEN-HERE |
| 7 | Theorem TEL ("### 3.3 Theorem TEL"), with its (δ) correction | PROVEN-HERE given VFINE-K/gh, F-bg, F-tree, K̄-β (upstream CONFIRMED) and Lemma FP |
| 8 | Lemma FP ("### 3.4 Lemma FP") | PROVEN-HERE (class 𝔍) |
| 9 | (ρ-null) ("### 3.5", "### 3.5′") — §3.5's continuity argument withdrawn, refined criterion stated | ARGUED |
| 10 | Theorem UIR-T ("### 3.6"), bound C_FP (correction appended) | PROVEN-HERE as an implication: (TC-b)_𝔍 + (ρ-null) ⇒ (UIR^♮) |
| 11 | Corollary b_∞ ("*Corollary (the value of b_∞).*") | PROVEN-HERE as an implication |
| 12 | §3.7 / §5 κ only in the O(1) constant; T-uniform | PROVEN-HERE given 7-10 |
| 13 | §4.1 the n log L coefficient = −(21/22)β_0^std, from the n-independent fine Wilson group only | PROVEN-HERE given TEL; value CONFIRMED upstream; ui55_2 |
| 14 | ui55_1 (exact identities) | 20/20 PASS, 3/3 controls fire |
| 15 | ui55_2 (leading-coefficient control) | run 1: 9/11 (script defect, recorded); run 2: 11/11 PASS, 3/3 controls fire |
| 16 | (TC-b)_𝔍 at orders 3, 4 | OPEN (not attempted) |
| 17 | **(UIR^♮)** | **OPEN, reduced to 16 + 9** |

**Counts.** Results of this file: PROVEN-HERE 10 (items 1, 2, 3, 5, 6, 7, 8, 10, 11, 13; item 12 is a corollary and not counted
separately), ARGUED 2 (items 4, 9), OPEN 2 (16, 17). Upstream claims I re-derived or tested: CONFIRMED — Lemma U-T⊥ (via Lemma P♮),
FLOW55 K̄-1L (c) (used), the VFINE-K/VFINE-L/GH0 arithmetic (ui55_2); REFUTED — FLOW §24 (F2)'s literal symbol (correction: an extra
factor D_ℓ(q_μ); all bounds stand) and FLOW55 §5.5's "the Woodbury split is not available off-shell without re-introducing the defect"
(correction: Lemma SPLIT); NOT-VERIFIED — Proposition U-a1⊥ (degree count re-checked only; not used). Codex verdicts used: 8, all AGREE
(§6). Errata to the stopped draft: 1 (E-1, forward references). Errata to this run's own text, appended: 4 (§3.3 (δ), §3.6 bound,
§4.2 timestamps, §3.5 continuity argument).

**Bottom line for the lead.** (UIR^♮) is still OPEN, but it is no longer a one-loop multi-scale estimate. Exactly (Theorem TEL),
β[G^♮_⊥,n] + (21/22)β_0^std n log L = a^⊥(J_0) − a^⊥(J_n) + Ρ_n: the universal slope comes only from the n-independent fine Wilson
transverse group evaluated at the scale ratio ℓ, the remainder telescopes (it cannot accumulate linearly in n), a^⊥(J_n) is the finite
part of a one-scale level-n polarisation of the tree action and is bounded by Lemma FP as soon as the tree jets are n-uniformly
exponentially local ((TC-b)_𝔍 at orders 3, 4, OPEN, tree level), and Ρ_n is the β of an equation-of-motion term, argued to vanish at
each n ((ρ-null), ARGUED, with the one possible failure mode named). κ enters only the O(1) constant.

**End of UIR55 (worker claude-opus-5-5, resumed run).**

**Late erratum E-2 (to this run's own §3 Setting; found on the final re-read).** The parenthetical "(Lemma F-Π (i); the Cartan
sector does not feel a Cartan background)" is FALSE at second order: at a Cartan background the Cartan-sector fluctuations see the
background through cos F_P in the abelian Wilson plaquette and through the polar positive part P of the S4′ contour average. As the §5
scope remark states, these couplings have total degree ≥ 4 in (K, P), give no log, are dominated as in Lemma FP (5), and are included
in a^⊥; Lemma SPLIT holds fibrewise in infinite volume for a.e. K, which covers this sector. No conclusion of §3-§4 changes. With E-2,
the errata to this run's own text number 5 (§3.3 (δ), §3.6 bound, §4.2 timestamps, §3.5 continuity argument, §3 Setting), not 4.
