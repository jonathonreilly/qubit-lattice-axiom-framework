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
