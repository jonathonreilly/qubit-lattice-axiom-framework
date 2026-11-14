# NLOC.md — (N-loc): exponential locality of the gauge-variant representative

Owner: the (N-loc) worker, session 24. This file is append-only. It may be read by anyone; nobody else writes it.
Requests for other files are collected in the final section "FOR OTHER FILES (not edited)".

---

## §L0 PRE-STATED (first edit of this file, 2026-10-28 13:50:08 UTC; statements only; cites nothing produced in this session)

This is the first edit of this file. Nothing below §L0 existed when §L0 was written. §L0 fixes the targets, the admissible
outcomes and the failure modes so that the rest of the file can be read against them. No constant appearing in §L0 was
derived in this session; the only numbers quoted are from files that existed before this session began (NORMS.md,
NQ_CHECK.md, PROOF.md, LINEAR_PACKAGE.md).

**Scope.** NORMS.md §N4 names two inputs of its Theorem N1-15 (the composite third-derivative bound with soft level-ratio
A_soft = 1/L). NQ_CHECK.md's Theorem NQ-1 discharges one of them, (N-Q). The remaining one is **(N-loc)**, the exponential
locality of the gauge-variant representative ζ^c_{sm,j} selected by Lemma N1-2's reparametrisation freedom. This file
attacks (N-loc) and nothing else. It does not touch the axioms, PROOF.md, NORMS.md, LINEAR_PACKAGE.md or any other lane
file.

**T-L0 (the statement).** Restate (N-loc) precisely in NORMS.md's own notation, with every quantifier shown: which levels,
which uniformity (in k, in j, in the level-k link x, in the torus side T), which gauge, which background, which
linearisation. If NORMS.md's §N4 statement is ambiguous in a way that changes whether it is true or whether it is enough,
say so and give the repaired statement. A sharp statement is itself a deliverable.

**T-L1 (consumption).** Determine what Theorem N1-15 *actually* consumes — the exact inequality, at the exact place in its
proof, that (N-loc) is invoked for. Report whether that is (a) exponential decay, (b) finite support, (c) a bare ℓ¹-mass
bound, or (d) something else. If it is weaker than exponential decay, state the weakest sufficient hypothesis and check it
clause by clause against N1-15's four exponent counts. **This is to be done before any attempt to prove (N-loc), because
it decides what has to be proven.**

**T-L2 (route 2: does Lemma LOC / N2-exp already suffice?).** PROOF.md's Lemma LOC localises background dependence up to
e^{−m_1 D/2} remainders rather than by a support statement, and LINEAR_PACKAGE's N2-exp gives exponentially local kernels
for the gauge-invariant responses B_k ↦ f_0 and B_k ↦ r_{k−1}. Decide whether the gauge-INVARIANT locality already in the
repository, plus the pure-gauge bookkeeping of Lemma N1-6, discharges what T-L1 identifies. If it does, write the argument
out in full; if it does not, name the one step that is missing.

**T-L3 (route 1: glue local axial gauges with the walk expansion).** Theorem RW's walk expansion needs one hypothesis — a
Combes-Thomas bound on box compressions. Check whether the gauge-variant representative's box compressions obey it. If
they do, build the glued representative and report the rate. If they do not, say which compression fails and why.

**T-L4 (route 3: the multi-scale axial gauge).** Only if T-L2 and T-L3 both fail. State what a multi-scale axial gauge
would have to deliver, and whether it is the same object as (CL-1)'s open half.

**T-L5 (rate and uniformity).** State the decay rate m obtained, and prove its uniformity in the level index j and in k, or
say exactly where uniformity fails. A rate that degrades with j or k is worthless to Theorem N1-15 and is to be reported
as a failure, not as a partial success.

**T-L6 (scope).** State the background and the linearisation at which the result holds. A proof at the trivial background
in the abelian/linearised setting (Setting SC's scope) is a real result and is to be reported as exactly that, with the
extension to (N-bg) left where NORMS.md leaves it: OPEN.

**T-L7 (verdict on Theorem N1-15).** After the attack, state whether Theorem N1-15 is unconditional at the scope of T-L6,
and if not, name every remaining input.

**Anti-circularity (binding, adopted from the BFT statement and from NORMS.md §N0).** The route may not use the per-level
covariances C^{(j)} as Newton inverses. (N-loc) must not reintroduce them: in particular, no step may invert a per-level
covariance to construct the representative, and no step may use a per-level Newton iteration whose k-th power appears.

**Admissible outcomes, pre-registered.**
- (L-O1) (N-loc), as restated under T-L0, PROVEN at the trivial background in the linearised setting, uniformly in j, k, T;
  Theorem N1-15 unconditional at that scope.
- (L-O2) A weaker statement proven, and checked to suffice for Theorem N1-15; then (L-O1)'s conclusion holds with the
  weaker statement substituted, and the stronger (N-loc) is withdrawn as unnecessary.
- (L-O3) CONDITIONAL: proven given a named new input, named explicitly and with its own status.
- (L-O4) **(N-loc) FALSE as stated**, with the obstruction exhibited, plus the repaired statement and whether the repaired
  statement suffices for Theorem N1-15. This is an acceptable outcome and is to be reported as a refutation, not dressed
  as progress.
- (L-O5) No progress. To be reported plainly.

**Pre-registered failure modes for this session's own work.**
- (L-F1) **The torus-size leak.** A representative that is exponentially local in level-k distance only after a constant
  that grows with the torus side T, or whose ℓ¹ mass grows with T. Theorem N1-15 needs a thermodynamic-limit-uniform bound,
  so any T-dependence is a failure and must be reported as one, not absorbed into a constant.
- (L-F2) **The Dirac-string artefact.** An axial / tree gauge representative whose value does not decay along the
  integration direction. Any claimed decay must be checked in the longitudinal direction, not only transversally.
- (L-F3) **The power-law tail.** A Hodge/Coulomb-type representative whose kernel decays only polynomially. Any claimed
  exponential decay via a Laplacian inverse must be checked against the degree-0 projector tail that PROOF.md's
  Proposition LED-unif already warns about (COMP-F1 / Π_ex).
- (L-F4) **Rate degradation.** A rate m_j that depends on j or k, or a prefactor that grows geometrically in k. Must be
  reported, not hidden in 𝔠_P.
- (L-F5) **Admissibility.** The reparametrisation used is not in Lemma N1-2's admissible class (the nested family, trivial
  at the coarse centres). The class must be stated and the construction must stay inside it; otherwise Lemma N1-2 does not
  license the representative and Theorem N1-15's identity is not available.
- (L-F6) **Proving the gauge-invariant half and calling it (N-loc).** NORMS.md §N4 already records that the
  gauge-invariant half is PROVEN. Re-proving it is not progress; the deliverable is the gauge-VARIANT representative.
- (L-F7) **Weakening (N-loc) to something Theorem N1-15 cannot use.** Every weakening must be checked against N1-15's four
  exponent counts explicitly, by substitution, not by assertion.

**Not success.** Numerics in place of a proof; a statement at fixed k; a statement for the straight average Q_str only
where Setting SC's Q is used; a bound whose constant is not exhibited as a function of (N, L, d, κ_±, m); citing Theorem RW
or Lemma LOC instead of rebuilding the part used (standing repository rule: load-bearing cited mathematics is REBUILT);
declaring (N-loc) discharged while the step that fails is moved into an unnamed constant.

---

## §L1 Scope, inputs, conventions

**What this file does.** It attacks (N-loc), the last named input of NORMS.md's Theorem N1-15 after NQ_CHECK.md's
Theorem NQ-1. Every item is labelled PROVEN-HERE / PROVEN (imported) / ARGUED / CONDITIONAL / OPEN. It writes no other
file; requests are in "FOR OTHER FILES (not edited)".

**Headline, stated once.**
1. **(N-loc) as written in NORMS.md §N4 is stronger than Theorem N1-15 needs, and is ambiguous in one way that matters
   (uniformity in the torus side).** §L2 restates it; §L3 isolates the exact consumption, **(N-loc♯)**, which is a pair of
   column-ℓ¹ mass bounds and nothing else.
2. **Theorem N1-15 can be made unconditional without (N-loc) at bounded coarse side T** — PROVEN-HERE, §L4, via a torus
   gauge lemma (Lemma NL-1) that I prove from scratch, plus Theorem NQ-1. The price is a factor **T^{d+2}** in the
   constant, i.e. ≈ 10⁴³ at N5-sf0's admissible T, against the ≈ c_m·𝔠_P² of the (N-loc) route. **Finite, uniform in k,
   not uniform in T.**
3. **(N-loc) itself is NOT proven here, and the two obvious constructions provably fail it** (§L5): the global axial /
   tree gauge fails by a Dirac string (failure mode L-F2) and the Hodge/Coulomb representative fails by a power-law tail
   (L-F3). Both failures are a factor of the torus side, i.e. pre-registered failure mode **L-F1 occurs for both**.
4. **A new PROVEN tool for the multi-scale axial gauge** (§L6): the analytic-division lemma, degrees 1 and 2, rebuilt from
   the T_α machinery of LINEAR_PACKAGE Lemma 4.4 and extended from "co-closed vector" to "closed 2-form". It gives an
   exponentially local gauge splitting of the coarse datum (Theorem NL-7) outright, and reduces the fine half of
   (N-loc) to a finite, explicitly named list of cell-flux conditions (§L7). That is where the remaining work is.
5. **Nothing here touches (N-bg)**, and (N-bg) is the larger wall. Theorem N1-15 bounds the third Taylor coefficient at
   V_k = 1; (H-C) names the Lipschitz constant of Hess E_k^br on the small-field class. Everything below is
   abelian/linearised at the trivial background — Setting SC's scope exactly — and does not reach it.

**Conventions.** NORMS.md's, with d ≥ 2 (d = 4 the case of interest), L ≥ 3 odd, levels j = 0, …, k, n := k − j, and
level-j torus side T_j = T·L^{k−j}, T the **coarse** (level-k) side (LINEAR_PACKAGE §1.1). d_j, d_j^*, Δ_j = d_jd_j^* +
d_j^*d_j. Q = the S4′ average, Q_str its straight part, r_j := QB_j − B_{j+1}, ev = restriction to the next level's roots.
𝔠_P, c_AX, c_F, C_f, C_R, κ̂, M, m_*′, c_m = coth(m′/2)^d, p_L, 𝔮_0 as in NORMS.md §N1 and LINEAR_PACKAGE.

**Two corrections to NORMS.md's conventions, adopted here (lead note, from REVIEW_NQ_S1).**
- **(C1)** NORMS.md l.103-104 writes Q_str as an average over "the L^{d−1} straight paths of L links". The object used
  below is LINEAR_PACKAGE §1.2's, **(Q_strA)(X, μ) := L^{−d}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ)**, i.e. the average over the
  **L^d block legs** (135 entries at L = 3, d = 4, not 81). Every computation below uses this definition. In particular
  **Q_str(const c) = L·c**, used in Lemma NL-2.
- **(C2)** M (the S4′ contour mean) and ev (restriction to roots) are **distinct**; h∘d = M − ev exactly
  (REVIEW_NQ_S1, verified entrywise). Below, only **ev** is used, and only through the root-covariance identity
  **Q∘d_j = d_{j+1}∘ev** (LINEAR_PACKAGE §1.2, "Q∘d = d∘ev"). No step below uses h or M.

**Imported PROVEN inputs, with the exact statement used.**
- **(J1) Theorem NQ-1** (NQ_CHECK.md): **‖Q^j‖_{∞→∞} ≤ 𝔮_0L^j uniformly in j**, with 𝔮_0 = 1 + d(L+1)/(2L) (= 11/3 at
  L = 3, d = 4; decreasing in L to 3). This is (N-Q) and it is PROVEN. Per the lead's note, the coincidence 𝔮_0 = p_L/L
  is an L = 3 accident and is not used.
- **(J2) Theorem N2-lin** (LINEAR_PACKAGE Thm 3.8, frozen): sup|r_{k−1}| ≤ C_R sup|d_kB_k| and sup|f_0| ≤ C_f sup|d_kB_k|,
  f_0 := L^{2k}d_0B_0, uniformly in k, T.
- **(J3) Lemma J-str (b), (c)** (LINEAR_PACKAGE Lemma 3.1): d^*r_i = 0 at every critical point, and
  sup|r_i| ≤ (κ_{k−1}/κ_i)L^{−(d−1)(k−1−i)}sup|r_{k−1}|.
- **(J4) Theorems N2-exp / N2-exp′ and Corollary N2-exp-b** (LINEAR_PACKAGE Thms 4.2, 4.2′, Cor. 4.3): the coarse
  B_k-symbols of r_{k−1}, r_i, J^c_0 and f_0 are analytic on the strip {|Im p_α| < m_*′} and bounded by M there, uniformly
  in k, T and the fine offset u; every infinite-lattice kernel entry obeys |K(X)| ≤ Me^{−m′|X|_1} for m′ < m_*′, X a
  **coarse** (level-k) displacement.
- **(J5) Lemma 4.4** (LINEAR_PACKAGE, PROVEN, CONFIRMED by REVIEW_S16_S17): the T_α / E_{<α} division machinery, the
  identity **𝔅^v = Σ_μ ν_μh_{μv}** with h_{αβ} = T_αE_{<α}𝔅^β antisymmetric and analytic, and the bound
  |T_αg| ≤ max(2, (π/2)e^{m′}/(m_*′ − m′))·sup_{S}|g| on {|Im p_α| ≤ m′}. §L6 rebuilds the parts it uses.
- **(J6) Lemma TOWER-VAR (d)** and **(J7) Lemma N1-2, Lemma N1-6, Lemma N1-7, Theorem N1-15** (NORMS.md): used as stated
  there. Lemma N1-2's **admissible class** is the one quantity I check at every step: the reparametrisation must be a
  **nested** family (λ̂_j|level-(j+1) roots = λ̂_{j+1}) that is **trivial at the level-k roots**, so that the level-k datum
  is unchanged.

**A structural fact used throughout, PROVEN-HERE (Lemma NL-0).** *The gauge ambiguity of Setting SC's chain minimiser is
exactly Lemma N1-2's admissible class.* Precisely: for fixed B_k, two minimisers (B_0, …, B_{k−1}) and (B′_0, …, B′_{k−1})
of E = ½‖d_0B_0‖² + Σ_{i<k}(κ_i/2)‖QB_i − B_{i+1}‖² differ by a null direction of E, i.e. by (δB_j) with d_0δB_0 = 0 and
QδB_i = δB_{i+1} for i ≤ k − 2 and QδB_{k−1} = 0; on the torus (modulo the harmonic/winding modes, treated separately in
Lemma NL-2) this is δB_0 = d_0λ for a fine λ and then, by root covariance, **δB_j = d_j(ev^jλ) with ev^kλ constant.**
*Proof.* E ≥ 0 is quadratic, so the minimiser set is an affine space over ker E. d_0δB_0 = 0 gives δB_0 = d_0λ + harmonic.
Root covariance Q∘d_j = d_{j+1}∘ev gives Q(d_jev^jλ) = d_{j+1}(ev^{j+1}λ), so the chain conditions hold identically and the
last one, QδB_{k−1} = d_k(ev^kλ) = 0, says ev^kλ is constant. Conversely each such family is null: every residual and
d_0δB_0 vanish. ∎
*Consequence (the one I use).* **A representative is fixed by choosing the level-0 gauge, and the levels j ≥ 1 are then
forced by the chain relation B_j = Q^jB_0 − Σ_{i<j}Q^{j−1−i}r_i.** Independent level-by-level gauge choices are NOT
admissible unless they are the ev-restrictions of one fine λ: that is pre-registered failure mode L-F5, and it is the
reason §L7's per-level division route needs a nesting step.

---

## §L2 (N-loc) restated (T-L0)

NORMS.md §N4 states it as: *"The representative of Lemma N1-11 can be chosen with exponential locality in level-k
ancestor distance: |ζ^c_{sm,j}δ_x(b)| ≤ 𝔠_PL^{−(k−j)}e^{−m d_k(b,x)} and
|ζ^c_{sm,j}Y(b)| ≤ 𝔠_PL^{−(k−j)}sup_{b′}e^{−m d_k(b,b′)}|Y(b′)|."*

**Three ambiguities, and how they are resolved.**
- **(A1) Uniformity in the torus side is not quantified, and it is the whole question.** The displayed inequalities are
  uniform in nothing as written. Theorem N1-15 needs its conclusion uniform in k; its proof needs the ℓ¹ masses of §L3
  uniform in k **and in T**, because the sum they bound runs over the whole torus. An (N-loc) with 𝔠_P or m depending on
  T is not merely weaker — it changes which theorem is true (§L4 proves the T-dependent version; §L5 shows the two
  natural constructions give exactly that). **Resolution: "uniformly in j, k and T" is part of the statement.**
- **(A2) The second display is not a consequence of the first and is not what is used.** The second display asserts a
  pointwise bound on ζ^c_{sm,j}Y(b) in terms of an exponentially weighted sup of Y; Theorem N1-15 never uses it (it uses
  the plain sup bound of Lemma N1-11 for the Y, W legs, and the ℓ¹ mass for the δ_x leg). **Resolution: the second
  display is withdrawn as unnecessary; see §L3.**
- **(A3) "Can be chosen" must mean "by one admissible reparametrisation, simultaneously for all three legs and all
  levels".** Theorem N1-15's identity comes from TOWER-VAR (d) + Lemma N1-2, so the representative must be a single
  nested family trivial at the level-k roots (Lemma NL-0). A per-level choice is not licensed. **Resolution: the
  admissible class is part of the statement.**

**(N-loc) [restated; this is the statement attacked below].** *There is a fine gauge family Λ, admissible in the sense of
Lemma N1-2 (nested, trivial at the level-k roots), such that the resulting representative ζ^c_{sm} of Setting SC's chain
minimiser map satisfies, for constants 𝔠_P < ∞ and m > 0 depending only on (N, L, d, κ_±) — in particular independent of
k, of the level index j, of the level-k link x and of the torus side T:*
  **(N-loc-a)** |ζ^c_{sm,j}Y|_∞ ≤ 𝔠_P L^{−(k−j)}|Y|_∞ for every level-k datum Y and every 0 ≤ j ≤ k;
  **(N-loc-b)** |(ζ^c_{sm,j}δ_x)(b)| ≤ 𝔠_P L^{−(k−j)}e^{−m d_k(b,x)} for every level-j link b, d_k = level-k ℓ¹ distance.
*Scope: abelian/linearised, trivial background (Setting SC).* (N-loc-a) is Lemma N1-11's conclusion and is **PROVEN**
given (N-Q) = Theorem NQ-1, except that NORMS.md's proof of it carries an undischarged box side R_eff (§L5 (c)); §L4
re-proves it on the torus with R_eff replaced by T. **(N-loc-b) is the open half.**

---

## §L3 What Theorem N1-15 actually consumes (T-L1) — and an independent confirmation of RN1-20

I traced every use of locality in Theorem N1-15's proof (NORMS.md l.520-555) before attempting any proof. The result,
PROVEN-HERE as a reading of that proof:

**(i) (N-loc) is invoked exactly twice**, in steps (2) and (4), and in both places for exactly one purpose: to bound the
**column ℓ¹ mass of the potential-slot response**, |ζ^c_jδ_x|_{ℓ¹}, via Lemma N1-7. Steps (1) and (3) use
|d_0ζ^c_0δ_x|_{ℓ¹} and |r_j(δ_x)|_{ℓ¹}, which are the **gauge-invariant** responses; their locality is (J4), PROVEN, and
(N-loc) is not needed for them. The Y, W legs use only the sup bound (N-loc-a).

**(ii) The exact consumption.** Substituting into steps (2) and (4), what the two steps need is

  **(N-loc♯)**  𝔏_j := sup_x Σ_{b ∈ links(level j)} |(ζ^c_{sm,j}δ_x)(b)| ≤ 𝔠_L · L^{(d−1)(k−j)}
  for every 0 ≤ j ≤ k − 1 and j = 0, with 𝔠_L independent of j, k, x and T,

together with (N-loc-a). **Nothing else.** In particular Theorem N1-15 consumes neither exponential decay nor finite
support: it consumes a **bare column-ℓ¹ bound at the budget (volume per level-k cell) × (sup)** = L^{dn}·L^{−n}. So the
honest answer to the brief's route-2 question is: **route 2's premise is right — N1-15 does not need finite range — but
Lemma LOC is not the instrument.** Lemma LOC (PROOF.md l.5853) localises the background dependence of the covariance
C(U, V); it says nothing about a gauge representative of a potential, and it is a statement at level 0 at a background,
not about the chain minimiser's gauge. **Route 2 as the brief frames it (via Lemma LOC) does not apply. Route 2's
weaker-hypothesis half does: (N-loc) is replaceable by (N-loc♯).**

**(iii) Where the T enters, and why.** Lemma N1-7's proof groups the level-j objects by the level-k cell containing them
and then sums e^{−m′|X|_1} over X ∈ Z^d, getting c_m = coth(m′/2)^d. **Without any decay the same sum runs over the
T^d level-k cells of the torus and gives T^d in place of c_m.** Hence, with (N-loc-a) alone,
  𝔏_j ≤ d·T^d·L^{dn}·𝔠_PL^{−n} = d𝔠_P·**T^d**·L^{(d−1)n},
which is (N-loc♯) with 𝔠_L = d𝔠_PT^d. **This independently confirms REVIEW_NORMS_S1's finding RN1-20: locality enters
Theorem N1-15 in exactly one place and for exactly one purpose, to replace a torus volume T^d by c_m.** I reached the
same conclusion from N1-15's proof before being told of RN1-20, and I confirm its substance and its location.

**(iv) The price of the trade, stated honestly.** The replacement is not free. Collecting the T-powers through N1-15's
four steps, with 𝔠_P^{tor} ∝ T from §L4:
  step (1): T² (two potential sup legs) · step (2): T^{d+1}(ℓ¹) · T(sup) = **T^{d+2}** ·
  step (3): T² · step (4): T^{d+1}·T = **T^{d+2}**.
So **the T-free route costs a factor ≈ T^{d+2} = T⁶ at d = 4** relative to an (N-loc) with the proven rate, against
c_m·𝔠_P² for the (N-loc) route. At N5-sf0's admissible coarse side T ≥ T_0 = 1.2932·10⁷ (PROOF.md, [SF7-edit 4]) that is
T⁶ ≈ 4.7·10⁴³. For comparison c_m ≈ (2/m_*′)^d ≈ 52⁴ ≈ 7.3·10⁶ at m_*′ = 0.0384 (κ = 1, L = 3). **So (N-loc) is worth
about 10³⁶–10⁴³ in the constant and nothing in the structure.** Per REVIEW_NORMS_S1, N1-15's constant is already ≳ 10⁷
at the proven rate, so this is a constant-quality question, not an existence question. Recorded because it is the honest
scoring of RN1-20: it closes the input, it does not improve the constant.

---

## §L4 The torus route: Theorem N1-15 without (N-loc), at bounded coarse side (T-L2, reordered per the lead's note)

The lead's note asks for the torus gauge bound first. I prove it, in the form the application needs, and then assemble.

### Lemma NL-1 (torus spread-axial gauge): PROVEN-HERE (abelian / linearised)

*Statement.* Let Λ = (Z/R)^d, R ≥ 2, and let B be a 1-form on Λ (one real component; su(N)-valued componentwise in the
linearisation). Let h^B be the constant 1-form h^B_μ := R^{−d}Σ_{y∈Λ}B_μ(y). Then there is λ: Λ → R with
  **|B − dλ − h^B|_∞ ≤ 4d·R·|dB|_∞.**
*No non-wrapping hypothesis is needed; this is the torus statement, where Lemma N1-5's box construction does not apply.*

*Proof.* Write w_μ(y_⊥) := Σ_{y_μ ∈ Z/R}B_μ(y) for the holonomy of B around the μ-cycle through the transverse position
y_⊥, and note the two exact identities used repeatedly:
  **(α)** for ρ ≠ μ, **w_μ(y_⊥) − w_μ(y_⊥ + e_ρ) = Σ_{y_μ}(dB)_{μρ}(y)**, hence |w_μ(y_⊥) − w_μ(y_⊥ + e_ρ)| ≤ R|dB|_∞.
  *(Sum (dB)_{μρ}(y) = B_μ(y) + B_ρ(y + e_μ) − B_μ(y + e_ρ) − B_ρ(y) over the μ-cycle; the two B_ρ terms telescope to 0
  around the cycle.)*
  **(β)** **B_μ(y + e_ρ) − B_μ(y) = −(dB)_{μρ}(y) + [B_ρ(y + e_μ) − B_ρ(y)]**, from the same plaquette.

*Step 1 (spread the μ = 1 holonomy).* Define λ^{(1)}(y_1, y_⊥) := Σ_{0≤i<y_1}[B_1(i, y_⊥) − w_1(y_⊥)/R] for
y_1 = 0, …, R − 1. The total increment around the cycle is w_1 − R·(w_1/R) = 0, so λ^{(1)} is well defined on Λ, and
B^{(1)} := B − dλ^{(1)} has **B^{(1)}_1(y) = w_1(y_⊥)/R** exactly, with dB^{(1)} = dB. By (α), w_1/R changes by at most
|dB|_∞ per transverse step, so travelling the short way round in each of the d − 1 transverse directions,
  |B^{(1)}_1(y) − w̄_1/R| ≤ (d − 1)(R/2)|dB|_∞,  w̄_1 := R^{−(d−1)}Σ_{y_⊥}w_1(y_⊥).
*Step 2 (transport the remaining components to a slice).* For ρ ≠ 1, apply (β) with μ = ρ, ρ = 1 to B^{(1)}:
B^{(1)}_ρ(y + e_1) − B^{(1)}_ρ(y) = −(dB)_{ρ1}(y) + [B^{(1)}_1(y + e_ρ) − B^{(1)}_1(y)], and the bracket is
[w_1(y_⊥ + e_ρ) − w_1(y_⊥)]/R, which is ≤ |dB|_∞ by (α). Hence the 1-increments of B^{(1)}_ρ are ≤ 2|dB|_∞, and
travelling the short way round the 1-cycle,
  **|B^{(1)}_ρ(y) − B^{(1)}_ρ(0, y_⊥)| ≤ 2·(R/2)·|dB|_∞ = R|dB|_∞** for every ρ ≠ 1.
(The increments sum to zero around the cycle — by (α) the two contributions cancel exactly — so the two ways round agree
and the bound is consistent.)
*Step 3 (induct).* The residual gauge freedom after Step 1 is λ′ independent of y_1, which leaves B^{(1)}_1 unchanged.
Use it to run Steps 1-2 for direction 2 **inside the slice {y_1 = 0}**, a (d − 1)-torus of the same side R, with
d(B^{(1)}|slice) controlled by |dB|_∞. After d − 1 such rounds every component has been spread and transported, and
component μ has accumulated at most (μ − 1) transports of 2·(R/2)|dB|_∞ each (Step 2, once per previous direction) plus
one spreading deviation of (d − μ)(R/2)|dB|_∞ (Step 1 in the remaining transverse torus):
  |B_μ − dλ_μ − c_μ| ≤ [(μ − 1) + (d − μ)/2]·R|dB|_∞ ≤ d·R·|dB|_∞ for some constant 1-form c.
*Step 4 (identify the constant).* Taking the Λ-mean of B − dλ − c and using that the mean of dλ vanishes on the torus,
|c − h^B|_∞ ≤ dR|dB|_∞. Hence |B − dλ − h^B|_∞ ≤ 2dR|dB|_∞ ≤ 4dR|dB|_∞. ∎
*(The constant 4d is a conservative upper bound, not optimised; d = 4 gives 16. Nothing below is sensitive to it.)*

*Reading.* This is the torus replacement for NORMS.md's Lemma N1-5, with the box side R_eff replaced by the **torus
side** and the holonomy carried by an explicitly identified constant 1-form rather than left in a seam. It is exactly the
"torus Hodge bound |B^{coex}|_∞ ≤ c_d R|dB|_∞" that REVIEW_NORMS_S1 asked for, in the ∃-gauge form the application
needs: a bound on a gauge-fixed representative, not on the d^*-free Hodge representative (which is a different field, and
whose sup is not bounded by another representative's sup).

### Lemma NL-2 (the harmonic mode of the chain is exactly L^{−(k−j)}): PROVEN-HERE

*Statement.* Let (B_0, …, B_{k−1}) minimise Setting SC's chain energy for level-k datum Y on the torus. Let
c_j := (the Λ_j-mean of B_j), a constant 1-form. Then **c_j = L^{−(k−j)}c_k**, c_k = the mean of Y; in particular
|c_j|_∞ ≤ L^{−(k−j)}|Y|_∞.
*Proof.* (1) **Q_str(const c) = L·c**: by convention (C1), Q_strA(X, μ) = L^{−d}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ), and for
A ≡ c this is L^{−d}·L^d·L·c = Lc. For the full S4′ average the same holds, because Q and Q_str differ by d∘h
(LINEAR_PACKAGE §1.2) and d annihilates nothing here: on a constant 1-form the slice functional h is constant, so
d∘h = 0. Hence **Q(const c) = Lc.** (2) The constant 1-forms and the mean-zero 1-forms are **orthogonal with respect to
the chain form**: ⟨d_0B_0^{const}, d_0B_0^{mz}⟩ = 0 since d annihilates constants; and ⟨QB_i^{const} − B_{i+1}^{const},
QB_i^{mz} − B_{i+1}^{mz}⟩ = (const)·(mean of a mean-zero field) = 0, using that Q preserves mean-zero by (1) applied to
the mean. (3) Therefore the minimiser splits, and on the constant sector the energy is Σ_i(κ_i/2)|Λ_{i+1}|·|Lc_i −
c_{i+1}|², minimised at c_{i+1} = Lc_i with all residuals zero. ∎

### Theorem NL-3 (Lemma N1-11 on the torus, with no box, no R_eff and no (N-loc)): PROVEN-HERE given (J1)

*Statement.* Let Y be level-k data on the torus of coarse side T, θ := sup|d_kY|. There is an **admissible** (Lemma N1-2:
nested, trivial at the level-k roots) representative ζ^c_{sm} of the chain-minimiser map with, for every 0 ≤ j ≤ k,
  **|ζ^c_{sm,j}Y|_∞ ≤ 𝔠_P^{tor}·L^{−(k−j)}·|Y|_∞,**
  **𝔠_P^{tor} := (1 + 𝔮_0)[8d²C_f·T + 1] + 𝔮_0·8dκ̂C_R·L²/(L² − 1) + 2 ,**
uniformly in j, k, T. This is (N-loc-a) with 𝔠_P = 𝔠_P^{tor} ∝ T.
*Proof.* (1) **Level 0.** Apply Lemma NL-1 at level 0, where the torus side is R_0 = T·L^k: there is a fine λ_0 with
|B_0 − d_0λ_0 − h|_∞ ≤ 4d·TL^k·sup|d_0B_0|, h the mean of B_0. By (J2), sup|d_0B_0| = L^{−2k}sup|f_0| ≤ C_fL^{−2k}θ, so
the first term is ≤ 4dTC_f·L^{−k}θ ≤ 8d²TC_f·L^{−k}|Y|_∞ (θ ≤ 2d|Y|_∞); by Lemma NL-2, |h| ≤ L^{−k}|Y|_∞. Hence
  **|b^{(0)}|_∞ ≤ 𝔞·L^{−k}|Y|_∞,  b^{(0)} := B_0 − d_0λ_0,  𝔞 := 8d²C_fT + 1.**
(2) **Levels j ≥ 1, forced by the chain.** By Lemma NL-0 the representative is determined by the level-0 gauge:
b^{(j)} := Q^jb^{(0)} − Σ_{i<j}Q^{j−1−i}r_i. By (J1) ‖Q^j‖_{∞→∞} ≤ 𝔮_0L^j and by (J2)+(J3)
sup|r_i| ≤ κ̂C_RL^{−(d−1)(k−1−i)}θ, so, exactly as in Lemma N1-11's step (4),
  |b^{(j)}|_∞ ≤ 𝔮_0L^j𝔞L^{−k}|Y|_∞ + 𝔮_0·4κ̂C_RL²/(L² − 1)·L^{−(k−j)}θ
            ≤ [𝔮_0𝔞 + 𝔮_0·8dκ̂C_RL²/(L² − 1)]·L^{−(k−j)}|Y|_∞.
(3) **Admissibility correction.** The family (b^{(j)}) is the chain minimiser for the datum
Y − d_k(ev^kλ_0) =: Y − d_kμ, not for Y, so it is not yet admissible (pre-registered failure mode L-F5). Correct it by
Lemma N1-6: let λ̂ be the nested multilinear interpolant of μ from level k down to level 0 (λ̂_k = μ, λ̂_j|level-(j+1)
roots = λ̂_{j+1}) and set **ζ^c_{sm,j}Y := b^{(j)} + d_j(ev^jλ̂)**. Then the level-k component is
Y − d_kμ + d_kμ = Y, the family is nested and its level-k reparametrisation is trivial, so it **is** admissible, and it
is the chain minimiser for Y (adding a null direction of E to a minimiser of E, Lemma NL-0). Its size: by Lemma N1-6
|d_j(ev^jλ̂)|_∞ ≤ L^{−(k−j)}|d_kμ|_∞, and
  |d_kμ|_∞ = |Y − (level-k component of b^{(·)})|_∞ ≤ |Y|_∞ + 𝔮_0𝔞|Y|_∞ + 𝔮_0·8dκ̂C_RL²/(L² − 1)|Y|_∞
by step (2) at j = k. (4) Adding (2) and (3) gives the displayed 𝔠_P^{tor}. ∎

*What this fixes in NORMS.md.* Lemma N1-11's proof carries a box of side R_eff that is **never fixed**: 𝔠_P contains
c_AXR_eff, and the construction is valid only on a non-wrapping box of that side, so as stated it is not a statement
about the torus Theorem N1-15 is proven on. Theorem NL-3 removes the box: on the torus the only admissible "R" is T, and
the holonomy that the box construction never sees is the constant mode, which Lemma NL-2 computes exactly. **So the
honest reading of Lemma N1-11 is 𝔠_P ∝ T, not 𝔠_P = O(1).** That is a correction to NORMS.md, not an improvement of it
(item 1 of FOR OTHER FILES).

### Corollary NL-4 (Theorem N1-15 at bounded coarse side, with no (N-loc)): PROVEN-HERE given (J1)-(J4)

*Statement.* At d = 4 (the scope REVIEW_NORMS_S1 confirms for N1-15), for every k ≥ 1 and every coarse side
T_0 ≤ T < ∞,
  **N3(D³E_k^br(1)) ≤ 𝔚^tor + (L^{d−1}/(L − 1))·𝔖^tor,  uniformly in k,**
with 𝔚^tor, 𝔖^tor obtained from NORMS.md's 𝔚, 𝔖 by the substitutions **c_m ↦ T^d** in the two potential-slot ℓ¹ masses
and **𝔠_P ↦ 𝔠_P^{tor}**, i.e. 𝔚^tor + 13.5𝔖^tor ≤ (𝔚 + 13.5𝔖)·(T^d/c_m)·(𝔠_P^{tor}/𝔠_P)² at the same m′. The soft
level-ratio is unchanged: **A_soft = 1/L**, and the whole exponent bookkeeping of §N6/§N7 is untouched.
*Proof.* Theorem N1-15's steps (1) and (3) use only the gauge-invariant ℓ¹ masses, bounded by Lemma N1-7 with (J4)'s
PROVEN exponential kernels; they are unchanged. Steps (2) and (4) use |ζ^c_jδ_x|_{ℓ¹}, for which §L3 (iii) gives
𝔏_j ≤ d𝔠_P^{tor}T^dL^{(d−1)n} from Theorem NL-3 alone, with no decay input — the sum over level-k cells is finite because
the torus has T^d of them. The Y, W legs use Theorem NL-3's sup bound. Summation (step (5)) is unchanged. ∎

*Status of Theorem N1-15 after this.* **Unconditional at d = 4, at the trivial background, in the abelian/linearised
setting, for every fixed coarse side T ≥ T_0 — with a constant that grows like T^{d+2}.** Its inputs (N-Q) and (N-loc)
are both discharged on that class: (N-Q) by Theorem NQ-1, (N-loc) by not being needed. **It is not uniform in T**, so it
does not survive the thermodynamic limit, and (N-bg) is untouched.

### Remark NL-5 (does the class match the consumer? — T-L2 item 2)

**Partly, and the part that fails is the thermodynamic limit, not the UV limit.**
- Proposition NAH-unif (PROOF.md l.6220) quantifies over "every k, every torus **large enough at each level** (T_j ≥ the
  level-j sizes, uniform by (H-C))", and its ε_unif := inf_i min{…} is an infimum over **levels**, at a fixed torus. So
  the hypothesis it needs from (H-C) is level-uniformity, and a T-dependent C_♭^{(i)} is admissible for it **provided T
  is fixed**. N5-sf0 likewise imposes only a **lower** bound, T ≥ T_0 = 1.2932·10⁷.
- The RG chain has T_i = T·L^{k−i} with T the coarse side, so **k → ∞ at fixed T is exactly the UV limit at fixed
  physical volume**. Corollary NL-4 is therefore a genuine layer-1 statement: UV stability at fixed volume, uniformly in
  the depth.
- **What it does not give:** any statement uniform in T. Layer 2 (the OS axioms, the thermodynamic limit, the cluster
  expansion) needs T-uniform constants, and Corollary NL-4's T^{d+2} is fatal there. **So (N-loc) is not retired by
  Corollary NL-4; it is retired only for the fixed-volume UV statement.** This is the honest scoring and it is the answer
  to the lead's item 2: the Hodge route finishes the job for one consumer and not for the other.

---

## §L5 The two halves separate: the sup bound is T-free, the ℓ¹ mass is not (T-L3 partial, T-L5)

### [NL-corr 1] Theorem NL-3's factor T is removable from the sup bound: PROVEN-HERE

*Theorem NL-3′.* **(N-loc-a) holds with 𝔠_P = 𝔠_P^♭ independent of j, k and T:**
  **𝔠_P^♭ := (1 + 𝔮_0)[2d(2d + 1)C_f·c_m + 1] + 𝔮_0·8dκ̂C_RL²/(L² − 1) + 2.**
*Proof.* Only Theorem NL-3's step (1) used the torus side, and only through Lemma NL-1's two uses of the crude bound
"(length of a lattice line) × |dB|_∞". Both are line sums of the **fine curvature**, and by (J4) the fine curvature
response to level-k data has exponentially local coarse kernels: for the datum Y with |Y|_∞ ≤ 1 and any fine line ℓ in
direction ρ,
  Σ_{y∈ℓ}|d_0B_0(y)| ≤ (number of level-0 links per level-k cell on ℓ)·(sup per cell, summed over cells)
                     ≤ L^k·C_fL^{−2k}·coth(m′/2)·(2d) ≤ 2dC_f·c_m^{1/d}·L^{−k},
the cell sum being a one-dimensional geometric sum of e^{−m′D}. Substituting this for "R|dB|_∞" in Lemma NL-1 steps (1)
and (2) — identity (α) gives the transverse variation of the holonomy as exactly a line sum of the curvature, and step 2
transports by line sums of the curvature — gives |b^{(0)}|_∞ ≤ [2d(2d+1)C_fc_m + 1]L^{−k}|Y|_∞ with no T. Steps (2)-(4)
of Theorem NL-3 are unchanged. ∎
*Reading.* **The exponential locality that the sup half of (N-loc) needs is the gauge-INVARIANT locality, which is
PROVEN (J4).** The gauge-variant locality (N-loc-b) is needed **only** for the ℓ¹ masses. This is the sharpest statement
of where (N-loc) bites, and it is why pre-registered failure mode L-F6 matters: proving the gauge-invariant half is not
progress on (N-loc-b), but it **is** what makes (N-loc-a) T-free.
*Consequence for Corollary NL-4:* its T-count drops from T^{d+2} to **T^d** (the cell sum in steps (2) and (4) only);
T^d ≈ 2.8·10²⁸ at T = T_0.

### Proposition NL-7 (the global axial / tree gauge FAILS (N-loc♯) by a factor T): PROVEN-HERE

*Statement.* Let λ_ax be the gauge of Lemma NL-1 / Lemma N1-5 run globally in direction 1, and b := B_0 − dλ_ax the
level-0 representative of the response to Y = δ_x. Then for every y with y_⊥ = x_⊥ and y_1 on the far side of x,
  **b_ρ(y) → Φ_ρ(y_⊥) := Σ_{z_1}(d_0B_0)_{1ρ}(z_1, y_⊥)  as the line is traversed,**
and |Φ_ρ(x_⊥)| ≍ L^{−k} generically, so b does not decay along direction 1 and
  **𝔏_0 ≥ c·T·L^{(d−1)k},** a factor T above (N-loc♯)'s budget. Pre-registered failure modes **L-F1 and L-F2 both occur.**
*Proof.* The axial formula is b_ρ(y) = Σ_{z_1 < y_1}(d_0B_0)_{1ρ}(z_1, y_⊥) (Lemma N1-5's step), whose limit along the
line is the full line flux Φ_ρ; the line flux is a sum of L^k terms of size ≍ C_fL^{−2k} with a definite sign near x
(the response to a single coarse link is not sign-alternating along the line through it), so |Φ_ρ| ≍ L^{−k}. The tube of
transverse cross-section O(1) level-k cells and longitudinal extent T level-k cells contains ≍ T·L^{dk} level-0 links,
each carrying ≍ L^{−k}. ∎
*The constructive half of this negative.* The string is **not** arbitrary: by closedness,
  **Σ_{z_1}(d_0B_0)_{1ρ} = Φ_ρ with d_⊥Φ = 0, i.e. Φ = d_⊥g transversally** —
sum the Bianchi relation d_1F_{ρσ} − d_ρF_{1σ} + d_σF_{1ρ} = 0 along the 1-line; the first term telescopes to 0, leaving
d_ρΦ_σ = d_σΦ_ρ. So **the Dirac string of the axial gauge is a transverse pure gauge**, and removing it is a
(d − 1)-dimensional instance of the same division problem. That is exactly the step a multi-scale axial construction has
to perform, and it is the entry point for §L6.

### Proposition NL-8 (the Hodge / Coulomb representative: a |x|^{−d} tail, ℓ¹ mass ∝ log T): ARGUED

*Statement.* Let b := d_0^*Δ_0^{−1}(d_0B_0) be the Coulomb representative (d_0^*b = 0, d_0b = d_0B_0). Then
  (i) the leading |x|^{−(d−1)} tail **cancels**, because the total flux of the curvature response vanishes;
  (ii) the residual tail is |x|^{−d} (the degree-0 projector Π_ex of LINEAR_PACKAGE Proposition 3.7, whose |x|^{−4} is
      exactly |x|^{−d} at d = 4), giving **𝔏_j ≤ 𝔠·(log T)·L^{(d−1)(k−j)}**, k-uniform but not T-uniform.
*Argument.* (i) In the coarse symbol, b̂ = \bar{ν}F̂/|ν|² with |ν|² = Σ_α|e^{ip_α} − 1|², and b̂ is bounded at p = 0 iff
F̂(0) = 0. **F̂(0) = 0 is PROVEN:** by (J5) the curvature response symbol satisfies 𝔅^v = Σ_μν_μh_{μv} with h analytic, so
𝔅^v(0) = 0 — the response to a constant coarse potential is flat, as it must be. Spatially this says the total flux
Σ_z(d_0B_0)(z) of the response vanishes, which is precisely the obstruction to a summable potential. (ii) With F̂(0) = 0
the symbol b̂ is bounded but homogeneous of degree 0 and **not** smooth at p = 0 (a ratio of a quadratic to |p|²), so its
kernel decays like |x|^{−d} and no better; the mass is then L^{(d−1)k}·Σ_{D=1}^{T}D^{−1} ≈ L^{(d−1)k}log T, the inner
region D ≤ 1 being covered by Theorem NL-3′'s sup bound.
*What is missing (why this is ARGUED, not PROVEN).* An explicit lattice bound |d_0^*Δ_0^{−1}(x)| ≤ C_d|x|^{−(d−1)} on the
torus with C_d explicit, and the first-moment cancellation made quantitative (the step from |x|^{−(d−1)} to |x|^{−d}
uses F̂(0) = 0 plus a derivative bound on F̂, i.e. (J4)'s strip, which is available). Both are classical lattice potential
theory; neither is written in this repository. **This is the cheapest remaining improvement in the lane: it would take
Corollary NL-4's T^d ≈ 10²⁸ down to log T ≈ 16.** Pre-registered failure mode **L-F3 occurs, but mildly** — the tail is
one power better than the naive expectation because of the flux cancellation.

### Proposition NL-9 (the within-cell axial gauge meets the ℓ¹ budget and FAILS the sup budget): PROVEN-HERE

*Statement.* Fix the axial gauge of Lemma N1-5 **separately inside each level-k cell** (box of side L^k, non-wrapping, so
Lemma N1-5 applies) and let the per-cell constants be chosen arbitrarily. The resulting field is
(a) ≤ c_AXL^{−k}C_fθ on the links **interior** to a cell, with support exponentially localised in level-k distance by
(J4), hence of ℓ¹ mass ≤ 𝔠L^{(d−1)k}, i.e. **it meets (N-loc♯)**; but
(b) on the **cell-crossing** links the value cannot be made smaller than ≍ θ for all of them: the crossing-link value
varies across one face of a cell by
  **|β_μ(y) − β_μ(y + e_ρ)| ≤ |d_0B_0|_∞ + 2 max|B̃|,** summed over the L^k steps of the face ⟹ variation ≍ 2(d − 1)c_AXC_fθ,
which is O(θ), not O(L^{−k}θ); and only one free constant per cell is available to absorb it. Hence the glued field has
≍ θ on a set of d·L^{(d−1)k} links per cell: **sup ≍ θ, failing (N-loc-a) by a factor L^k**, while its ℓ¹ contribution is
d·L^{(d−1)k}·θ, which is **exactly on budget**.
*Proof of (b).* With B̃^{(X)} := B_0 − d_0λ^{(X)} the within-cell field, the plaquette identity (β) of Lemma NL-1 gives
β_μ(y) − β_μ(y + e_ρ) = −(d_0B_0)_{μρ}(y) + B̃^{(X)}(y, ρ) − B̃^{(X+e_μ)}(y + e_μ, ρ); the two B̃ terms are the within-cell
fields, of size c_AXL^{−k}C_fθ, and there are L^k steps across a face, so the accumulated variation is
≤ L^k(L^{−2k}C_fθ + 2c_AXL^{−k}C_fθ) = (L^{−k} + 2c_AX)C_fθ. A single per-cell constant removes only the mean. ∎
*Reading.* **This is the precise sense in which NORMS.md's "near/far split" trade is not available as stated.** NORMS.md
§N4 says (N-loc) "can be traded for an explicit near/far split" with "a factor R_eff^d and an additive Me^{−m′R_eff} far
term". Proposition NL-9 shows what such a split actually costs: a box-local gauge delivers the ℓ¹ budget but breaks the
sup bound by L^k, and the two legs of Theorem N1-15 need **both** bounds from the **same** representative (§L2 (A3)).
The trade as stated is therefore not a trade; REVIEW_NQ_S1's verdict that it is "stated, not carried out" is confirmed,
and strengthened: carried out naively, it fails.

---

## §L6 The analytic-division lemma (the tool the multi-scale axial gauge needs): PROVEN-HERE

Per the standing repository rule, the cited mathematics is rebuilt, not cited: Lemma NL-10 (a) is LINEAR_PACKAGE Lemma
4.4's step (1) re-proved; (b) and Lemma NL-11 are new (Lemma 4.4 solves the **contraction** complex at degree 1 — "a
co-closed vector is a divergence" — whereas a gauge representative needs the **exterior** complex at degree 2, "a closed
2-form is a coboundary").

**Setting.** S_η := {p ∈ (C/2πZ)^d : |Im p_α| < η}; 𝒪(η) := the analytic, 2π-periodic functions on S_η;
ν_α(p) := e^{ip_α} − 1; E_αg := g|_{p_α=0}; for 0 < η′ < η put
  **κ(η, η′) := max(2, (π/2)e^{η′}/(η − η′)).**
A symbol bounded on S_η by G has a kernel obeying |K(X)| ≤ Ge^{−η′|X|_1} on Z^d for every η′ < η (Paley-Wiener /
Poisson, as in Theorem 4.2), and its ℓ¹ mass over Z^d is ≤ G·coth(η′/2)^d. **Division is in the COARSE momentum p; that
is the whole point, because (J4) gives O(1) strip width in p and strip width is what the bound is proportional to.**

### Lemma NL-10 (one-variable division and the degree-1 complex): PROVEN-HERE
*(a)* For g ∈ 𝒪(η) with |g| ≤ G on S_η, **T_αg := (g − E_αg)/ν_α ∈ 𝒪(η)** and sup_{S_{η′}}|T_αg| ≤ κ(η, η′)·G.
*Proof.* ν_α has simple zeros exactly at p_α ∈ 2πZ; by 2π-periodicity g − E_αg vanishes there, so the quotient is
analytic and periodic. On |Im p_α| ≤ η′: if |Re p_α| ∈ [π/2, π] then Re e^{ip_α} ≤ 0, so |ν_α| ≥ 1 and |T_αg| ≤ 2G. If
|Re p_α| ≤ π/2, write w := p_α; g(w) − g(0) = w∫_0^1g′(tw)dt with |g′| ≤ G/(η − η′) (Cauchy on the disc of radius
η − η′ about w, which stays in S_η), and |ν_α(w)| = |w|·|∫_0^1e^{itw}dt| ≥ (2/π)e^{−η′}|w|. ∎
*(b)* Let d ≥ 2 and let ĉ_ν ∈ 𝒪(η), |ĉ| ≤ G, be **closed**: ν_αĉ_β = ν_βĉ_α for all α, β. Then
**μ̂ := T_1ĉ_1 ∈ 𝒪(η)** satisfies **ν_νμ̂ = ĉ_ν for every ν**, with sup_{S_{η′}}|μ̂| ≤ κ(η, η′)G.
*Proof.* Apply E_1 to ν_1ĉ_β = ν_βĉ_1: the left side vanishes (ν_1|_{p_1=0} = 0), so ν_βE_1ĉ_1 = 0 for every β ≠ 1.
ν_β is not a zero divisor in 𝒪(η) (if ν_βA ≡ 0 with A analytic then A = 0 off the zero set of ν_β, hence everywhere by
continuity), so **E_1ĉ_1 = 0** and ν_1μ̂ = ĉ_1 − E_1ĉ_1 = ĉ_1. For ν ≠ 1: ν_1(ν_νμ̂) = ν_ν(ν_1μ̂) = ν_νĉ_1 = ν_1ĉ_ν, and
dividing by the non-zero-divisor ν_1 gives ν_νμ̂ = ĉ_ν. ∎

### Lemma NL-11 (degree-2 analytic division: a closed 2-form symbol is an analytic coboundary): PROVEN-HERE, d ≥ 3
*Statement.* Let d ≥ 3 and let F̂_{αβ} = −F̂_{βα} ∈ 𝒪(η) with |F̂| ≤ G on S_η be **closed**:
  ν_αF̂_{βγ} − ν_βF̂_{αγ} + ν_γF̂_{αβ} = 0 for all α, β, γ.
Then **b̂_β := T_1F̂_{1β} (β ≥ 2),  b̂_1 := T_2(−E_1F̂_{12})** lie in 𝒪(η), satisfy
  **ν_αb̂_β − ν_βb̂_α = F̂_{αβ} for all α, β,**
and sup_{S_{η′}}|b̂| ≤ κ(η, η′)·G. *No induction and no extra hypothesis are needed.*
*Proof.* (0) **F̂(0) = 0 is automatic for d ≥ 3**: expanding closedness to first order at p = 0 with ν_α = ip_α + O(p²)
gives p_αF̂_{βγ}(0) − p_βF̂_{αγ}(0) + p_γF̂_{αβ}(0) = 0 for all p, and matching the coefficient of p_α (α ∉ {β, γ}, which
exists iff d ≥ 3) gives F̂_{βγ}(0) = 0. (Not needed below, but it is the spatial statement "the total flux vanishes",
used in Proposition NL-8.)
(1) **The (βγ) equations, β, γ ≥ 2.** ν_β and ν_γ do not depend on p_1, so E_1(ν_βg) = ν_βE_1g and therefore T_1
commutes with multiplication by them; also T_1(ν_1g) = g, since E_1(ν_1g) = 0. Hence
  ν_βb̂_γ − ν_γb̂_β = T_1(ν_βF̂_{1γ} − ν_γF̂_{1β}) = T_1(ν_1F̂_{βγ}) = F̂_{βγ},
the middle step being closedness for the triple (1, β, γ).
(2) **The transverse vector is closed.** Put V_β := −E_1F̂_{1β} (β ≥ 2). Applying E_1 to closedness for (1, β, γ) kills
the ν_1 term and leaves ν_βE_1F̂_{1γ} = ν_γE_1F̂_{1β}, i.e. ν_βV_γ = ν_γV_β: V is a closed 1-form symbol in the d − 1 ≥ 2
transverse variables. By Lemma NL-10 (b) applied in those variables, **ν_βb̂_1 = V_β for every β ≥ 2** with
b̂_1 = T_2V_2 ∈ 𝒪(η) and |b̂_1| ≤ κG.
(3) **The (1β) equations.** ν_1b̂_β − ν_βb̂_1 = (F̂_{1β} − E_1F̂_{1β}) − V_β = F̂_{1β}. ∎
*(d = 2 is genuinely different: there is no transverse pair, Lemma NL-10 (b) is unavailable, and the construction needs
F̂(0) = 0 as a hypothesis — then b̂_2 := T_1F̂_{12}, b̂_1 := −T_2E_1F̂_{12} works by the same two lines. d = 4 is the case
of interest and is covered by the lemma as stated.)*
*What it is.* **An exponentially local, translation-covariant, analytic gauge-fixing operator at one level, with the
constant κ(η, η′)·(strip width)^{−1} and no box, no string and no power-law tail.** It is the symbol-space form of the
"multi-scale axial gauge": T_1 is an axial gauge in direction 1 with the p_1 = 0 (string) part removed and re-expressed
through the transverse division of step (2) — which is exactly the identity Φ = d_⊥g that Proposition NL-7 exhibits
spatially. *What it is not:* a bounded operator on ℓ^∞ with an O(1) mass — κ(η, η′) ∝ 1/(η − η′) and the input's strip
width is what pays for the gain; see §L7.

### Theorem NL-12 (exponentially local gauge splitting of the level-k datum): PROVEN-HERE, d ≥ 3
*Statement.* There are coarse-translation-covariant operators 𝒲 (coarse 1-forms → coarse 1-forms) and ℳ (coarse 1-forms
→ coarse functions), with kernels obeying |K(X)| ≤ κ(η, η′)·2d·e^{−η′|X|_1} for every η′ < η < π/2 and ℓ¹ masses
≤ κ·2d·coth(η′/2)^d, such that for every level-k datum Y
  **Y = 𝒲Y + d_k(ℳY),  d_k(𝒲Y) = d_kY,  |𝒲Y|_∞ ≤ 𝔡·|d_kY|_∞,  |ℳY|_∞ ≤ 𝔡·|Y|_∞,**
with 𝔡 := κ(η, η′)coth(η′/2)^d·2d. *(η may be taken any value < π/2: the kernel of d_k is a two-term difference, whose
symbol ν_α(p) is entire.)*
*Proof.* Apply Lemma NL-11 to F̂ := (d_kY)^ = ν∧Ŷ, which is closed (ν∧ν∧ = 0) and analytic wherever Ŷ is; the operator
𝒲 := (the NL-11 division) ∘ d_k is built from T_1, T_2, E_1 and d_k alone, so it is a fixed coarse-translation-covariant
operator with the stated kernel bound, and d_k𝒲 = d_k by construction. Then Ŷ − 𝒲Ŷ is closed, so Lemma NL-10 (b) gives
ℳ := T_1(1 − 𝒲)_1, again a fixed operator, with d_kℳY = Y − 𝒲Y. The sup bounds are the ℓ¹ masses of the kernels. ∎
*Consequence (the pure-gauge half of (N-loc-b) is PROVEN).* Theorem NL-3's admissibility correction and Lemma N1-11's
steps (1)-(2) both act on the pure-gauge part of the datum. With Theorem NL-12 in place of the box axial gauge of
Lemma N1-5, that part is **d_j(ev^jλ̂(ℳY))** with λ̂ Lemma N1-6's nested interpolant: ℳ is exponentially local, and ev,
the interpolant and d_j are cell-local, so **this contribution satisfies both (N-loc-a) (size L^{−(k−j)}𝔡|Y|_∞,
Lemma N1-6) and (N-loc-b) (rate η′ in level-k distance), with no box, no R_eff, no string and no T.** Pre-registered
failure modes L-F1, L-F2, L-F3 do not occur for this half.
**So (N-loc-b) is now reduced to a single class: the response to a datum already in the form 𝒲Y.** That is the
"curvature half", and it is what §L7 is about.

---

## §L7 The residual: the fine half, and why it is the multi-scale axial gauge (T-L3, T-L4)

**The obstruction, stated exactly.** Theorem N1-15's steps (2) and (4) need the ℓ¹ mass of **ζ^c_jδ_x at levels
j < k**, and by Lemma NL-0 the level-0 gauge choice determines all of them. So the one remaining object is the level-0
representative b^{(0)} with d_0b^{(0)} = d_0B_0. Lemma NL-11 cannot be applied to it directly, and the reason is
structural, not technical:

**The level-0 field is not level-0-translation-covariant.** The chain operator Q blocks the lattice, so the map
Y ↦ B_0 is covariant only under **level-k** translations; (J4) is stated exactly that way ("uniformly in k, T and the
fine offset u"). Consequently:
- a division in **fine** momentum is unavailable (no fine symbol); and in any case a fine-local division cannot work,
  because an exact right inverse of d_0 with O(1) ℓ¹ mass would give |B_0|_∞ ≲ |d_0B_0|_∞, contradicting the elementary
  coherence bound |B|_∞ ≳ R|dB|_∞ for a curvature of one sign on a region of side R. **The gain of L^k must come from an
  integration over a length L^k, so the division kernel must be spread over exactly one level-k cell.** This is the
  honest reason the problem is a *multi-scale* one.
- a division in **coarse** momentum is available but the complex is twisted: decomposing level-0 fields by coarse
  momentum p writes the level-0 de Rham complex as the Koszul complex of the d commuting operators
  **D_μ := (twisted fine shift in direction μ) − 1** on V := functions on the cell 𝒞 = (Z/L^k)^d with holonomy e^{ip_μ}
  around the μ-th cycle, i.e. as the cochain complex of the discrete d-torus with the flat line bundle ℒ_p.

**What is settled about that complex (PROVEN-HERE as a reading of the standard facts, re-derived):**
1. **For p ≠ 0, H^•(𝒞; ℒ_p) = 0 in every degree** (Künneth over the d circle factors; the circle complex
   0 → R^{L^k} →^{D_p} R^{L^k} → 0 has vanishing cohomology iff e^{ip_μ} ≠ 1). So d_0b = F is solvable at every p ≠ 0,
   uniquely modulo the gauge image — which is Lemma NL-0's statement, recovered.
2. **The only possible singularity of the solution is at p = 0**, where H^1 ≅ R^d and H^2 ≅ R^{d(d−1)/2} jump.
3. **The one-direction division has exactly one singular part, and it is the cell-flux functional.** Solving D_μψ = g on
   one μ-line of 𝒞 gives
     **ψ = Θ_μ(g) + ν_μ^{−1}·σ_μ(g)·(seam vector),  σ_μ(g) := Σ_{y_μ ∈ Z/L^k} g(y),**
   where Θ_μ is the telescoping partial sum along the line. **Θ_μ carries ℓ^∞ norm ≤ L^k|g|_∞ — that is precisely the
   L^k gain, and it is cell-local** — and the entire obstruction to analyticity is the single term ν_μ^{−1}σ_μ(g), which
   by Lemma NL-10 (a) is analytic **iff σ_μ(g) vanishes on {p_μ = 0}**.
4. **The leading cell-flux condition holds.** Summing over the offsets, σ(F̂)|_{p=0} = Σ_{y∈𝒞}F̂(y)|_{p=0} = Σ_u𝔅^u(0),
   and 𝔅^u(0) = 0 for every offset u by (J5)'s identity 𝔅^v = Σ_μν_μh_{μv}. **PROVEN.** (This is the same fact that
   makes Proposition NL-8's leading tail cancel.)

**What is NOT settled, named precisely.** The construction of §L6 run on the twisted complex produces, at each of its
two steps, one cell-flux condition, and item 4 discharges only the p = 0 value of the last one. The residual statement is:

  **(N-loc-cell) [OPEN; this is what is left of (N-loc)].** For the curvature response F̂ = 𝔅 of (J4) and the
  construction of Lemma NL-11 transcribed to the twisted complex, each of the functionals
  σ_1(F̂_{1β})|_{p_1=0} (β ≥ 2) and σ_2(E_1F̂_{12})|_{p_2=0} is divisible by the corresponding ν analytically — equivalently,
  the line fluxes of the fine curvature response across a level-k cell, at zero longitudinal coarse momentum, vanish.

Status: **ARGUED for the structure, OPEN for (N-loc-cell).** Two remarks that bound how hard it is:
- It is the Fourier form of Proposition NL-7's identity Φ = d_⊥g: the line flux is transversally closed, so it is a
  transverse pure gauge, and item 3's second step is exactly the transverse division that removes it. So the conditions
  are not independent of each other — they are a chain, as in Lemma NL-11's steps (1)-(3), and what is missing is the
  **twisted** analogue of Lemma NL-10 (b): that a transversally closed V with values in V(𝒞) is ν_β times something
  analytic. That is one lemma, not a programme.
- **(N-loc-cell) is exactly (CL-1)'s open half.** PROOF.md l.6556-6558 records under (CL-1) that "the background
  dependence of 𝔊_k … needs a composite LOC with multi-scale axial gauges: OPEN", and NORMS.md §N4 names the same
  object. The twisted-Koszul formulation above is, as far as I can tell, the first statement of it as a finite list of
  scalar conditions on an **already-PROVEN symbol** (J4)/(J5) rather than as a gauge construction to be invented.
  That is the deliverable of this section.

**Route 1 of the brief (glue local axial gauges with the walk expansion) — checked, and it does not transfer.** Theorem
RW (PROOF.md l.5410) needs one hypothesis of its operator K: (RW1), a Combes-Thomas bound on the Dirichlet compressions
K_{Ω_□}. Theorem N5-sf0 glues box-local gauges with it, and the reason that works is that its gauge-variant object is an
**operator**: Lemma N5-cov gives K_{Ω_□} = R_g^{−1}(Õ(gU, gV))_{Ω_□}R_g with R_g **block-diagonal orthogonal**, so
conjugating by a box-local gauge changes neither the block norms nor the distances, and each box's bound transfers
verbatim. **A potential representative has no such covariance:** a gauge change sends B ↦ B − dλ, an affine shift, not an
orthogonal conjugation, so there is nothing for the walk expansion to glue — the box-local bounds do not transfer, and
what has to be glued is the gauge functions themselves. Concretely, Proposition NL-9 computes the price of gluing them
naively. **So "the box compressions obey a Combes-Thomas bound" is not the relevant question for (N-loc): Theorem RW is
a tool for inverting operators, and (N-loc) is not an operator-inversion problem.** This is a negative answer to the
brief's route 1, with the reason named.

---

## §L8 Rate, uniformity, scope, verdict (T-L5, T-L6, T-L7)

**Rate (T-L5).** Every rate obtained here is stated in **level-k (coarse) ℓ¹ distance**, which is the variable (N-loc-b)
asks for.
- The pure-gauge half (Theorem NL-12): rate **any η′ < η < π/2**, with constant κ(η, η′)·coth(η′/2)^d, **independent of
  j, k and T**. The kernel is built from T_1, T_2, E_1 and d_k, whose symbols are entire except for the ν-divisions, so
  no analyticity input from the chain is consumed and the rate does not degrade.
- The gauge-invariant inputs: rate **any m′ < m_*′**, uniformly in j, k, T, by (J4). At κ = 1, L = 3 the proven
  m_*′ = 0.0384, so c_m = coth(m_*′/2)^4 ≈ 52⁴ ≈ 7.3·10⁶; the located (not proven) rate is ≈ 1.0, which would give
  c_m ≈ 2.1²·… ≈ 25. **Every constant below inherits that 25-vs-7·10⁶ gap; it is a rate-quality problem, not a
  structural one.**
- The curvature half of (N-loc-b): **no rate is obtained.** Pre-registered failure mode L-F4 does not occur in the
  halves that are proven (no j- or k-dependence anywhere above), but that is because the open half is open, not because
  it was checked.
- Uniformity in L: Theorem NQ-1's 𝔮_0 = 1 + d(L+1)/(2L) is used only through its boundedness, so every statement above
  holds at every admissible odd L ≥ 3. **No statement here uses p_L or the L = 3 coincidence 𝔮_0 = p_L/L** (lead note,
  REVIEW_NQ_S1 F7). Lemma NL-11 needs **d ≥ 3**; Corollary NL-4 is at **d = 4** only, matching the scope
  REVIEW_NORMS_S1 confirms for Theorem N1-15 (every imported input is d = 4).

**Scope (T-L6).** Everything in §L4-§L7 is:
- **abelian / linearised** — Setting SC, one real component, the chain energy ½‖d_0B_0‖² + Σ(κ_i/2)‖QB_i − B_{i+1}‖².
  Lemma NL-0, Lemma NL-1, Lemma NL-2 and the division lemmas are all statements about that quadratic problem.
- **at the trivial background** (V_k = 1): the third-derivative identity used by Theorem N1-15 is TOWER-VAR (d) at the
  trivial point, and the linear inputs (J2)-(J4) are the trivial-background chain's.
- **and it does not reach (N-bg).** Theorem N1-15, with or without (N-loc), bounds **D³E_k^br(1)** — one Taylor
  coefficient at one point. (H-C)'s C_♭ clause, as Lemma BR1 and δ_Sch consume it, is the **Lipschitz constant of
  Hess E_k^br on the small-field class**, i.e. a bound on D³E_k^br(V) for every V in the class. These are different
  statements (NORMS.md's own Remark N6-5, pre-registered failure mode N-F4 there). **Nothing in this file bears on
  (N-bg)**, and Theorem NQ-1 provably does not cross it either: its slice identity is abelian and has no nonlinear
  SU(N) analogue (PROOF.md l.1159-1161, per the lead's note). **So the honest statement is: (H-C)'s C_♭ clause is NOT
  discharged by this work. One named input of one trivial-background theorem is.**

**Verdict on Theorem N1-15 (T-L7).**
| scope | status of Theorem N1-15 | remaining inputs |
|---|---|---|
| d = 4, trivial background, linearised, **fixed coarse side T ≥ T_0** | **unconditional** (PROVEN-HERE, Corollary NL-4 + [NL-corr 1] + Theorem NQ-1) | none at this scope; constant carries T^d |
| same, **uniform in T** (what layer 2 needs) | **CONDITIONAL on (N-loc-b)**, reduced to (N-loc-cell) | (N-loc-cell) [OPEN]; or Proposition NL-8's lattice tail bound, which would leave only a factor log T |
| the Lipschitz statement on the small-field class, any T | **CONDITIONAL on (N-bg)** | (N-bg) [OPEN], the larger wall |

**Pre-registered outcome reached: (L-O2) at fixed T, (L-O4) in part, (L-O3) in general.** Specifically: (N-loc) as
written is **replaced** by the weaker (N-loc♯) (L-O2's mechanism, §L3), (N-loc) is shown **false for the two natural
constructions** with the obstruction exhibited (L-O4's mechanism, §L5), and what remains is CONDITIONAL on the newly
named (N-loc-cell) (L-O3). **(N-loc) itself is not proven.**

---

## §L9 Tally, and the record of checks nl1 and nl2

**PROVEN-HERE (complete proofs written out above, from stated hypotheses; abelian/linearised, trivial background)**
1. **Lemma NL-0** — the gauge ambiguity of Setting SC's chain minimiser is exactly Lemma N1-2's admissible class
   (nested, trivial at the level-k roots); consequently a representative is fixed by the level-0 gauge alone and the
   levels j ≥ 1 are forced by the chain relation. (This is what makes per-level gauge choices inadmissible, L-F5.)
2. **§L3 (i)-(iii)** — the exact consumption of Theorem N1-15: (N-loc) enters exactly twice, only through the
   column-ℓ¹ masses, and only to replace a torus cell count T^d by c_m. **Independent confirmation of
   REVIEW_NORMS_S1's RN1-20**, reached from N1-15's proof before being told of it.
3. **Lemma NL-1** — the torus spread-axial gauge: ∃λ with |B − dλ − h^B|_∞ ≤ 4dR|dB|_∞ on (Z/R)^d, h^B the mean.
   This is the torus Hodge bound the lead asked for, in the ∃-gauge form.
4. **Lemma NL-2** — the chain's constant mode is exactly c_j = L^{−(k−j)}c_k (via Q(const c) = Lc and the orthogonality
   of the constant and mean-zero sectors under the chain form).
5. **Theorem NL-3 / [NL-corr 1] Theorem NL-3′** — Lemma N1-11's conclusion (N-loc-a) on the torus, with the box and
   R_eff removed and with **𝔠_P^♭ independent of j, k and T**. Given Theorem NQ-1.
6. **Corollary NL-4** — Theorem N1-15 **unconditional at d = 4 at fixed coarse side T**, with no (N-loc), at the price
   of T^d in the constant (T^d ≈ 2.8·10²⁸ at T = T_0 = 1.2932·10⁷, against c_m ≈ 7.3·10⁶).
7. **Proposition NL-7** — the global axial/tree gauge fails (N-loc♯) by a factor T (the Dirac string), together with the
   identity that the string is a **transverse pure gauge** (Φ = d_⊥g).
8. **Proposition NL-9** — the within-cell axial gauge meets the ℓ¹ budget and fails the sup budget by L^k, with the
   explicit O(θ) inter-cell mismatch. **NORMS.md's near/far trade, carried out naively, fails.**
9. **Lemma NL-10** (a), (b) — the T_α division bound (Lemma 4.4's step rebuilt) and the degree-1 complex: a closed
   1-form symbol is ν times an analytic function, with E_1ĉ_1 = 0 derived. (Checked exactly: nl1b-A, nl1b-B **PASS**.)
10. **Lemma NL-11** — **degree-2 analytic division**: a closed 2-form symbol is ν∧b̂ with b̂ analytic and
    |b̂| ≤ κ(η, η′)|F̂|, by the one-step formula b̂_β = T_1F̂_{1β}, b̂_1 = T_2(−E_1F̂_{12}), for every d ≥ 3; and
    F̂(0) = 0 is automatic for d ≥ 3. (Checked exactly on 200 random closed inputs: nl1-A **PASS**, with a designed-FAIL
    control nl1-C **PASS**.) This is the new tool.
11. **Theorem NL-12** — an exponentially local, translation-covariant gauge splitting Y = 𝒲Y + d_k(ℳY) of the level-k
    datum, hence **the pure-gauge half of (N-loc-b) outright**, with no box, no string, no power tail and no T.
12. **§L7's route-1 finding** — Theorem RW cannot glue gauge representatives: N5-sf0's gluing works because R_g is
    block-diagonal orthogonal and the object is an operator; a potential transforms affinely, so there is nothing to
    conjugate. The brief's route 1 is answered negatively, with the reason named.

**ARGUED (convincing, with an identified hole)**
13. **Proposition NL-8** — the Hodge/Coulomb representative has a |x|^{−d} tail (the Π_ex tail), giving (N-loc♯) with a
    factor **log T** instead of T^d. Hole: an explicit lattice bound |d_0^*Δ_0^{−1}(x)| ≤ C_d|x|^{−(d−1)} on the torus
    and the quantitative first-moment cancellation. **This is the cheapest remaining improvement in the lane.**
14. **§L7 items 1-4** — the twisted-Koszul reduction of the fine half: pointwise solvability for p ≠ 0, the singularity
    confined to p = 0, the one-direction division's L^k gain from the telescoping sum Θ_μ, and the leading cell-flux
    condition PROVEN from (J5). Hole: the twisted analogue of Lemma NL-10 (b).

**OPEN**
15. **(N-loc-cell)** — the remaining content of (N-loc-b), stated in §L7 as a finite list of cell-flux divisibility
    conditions on the already-PROVEN symbol of (J4)/(J5). **This is (CL-1)'s open half, now in scalar form.**
16. **(N-bg)** — untouched, and the larger wall (§L8).
17. **(N-loc-b) at d = 2** — Lemma NL-11 needs d ≥ 3; not pursued (d = 4 is the case of interest).

**Counted here: nothing.** This file is not a ledger. No item above is to be added to PROOF.md's tally by this worker.

### Record of check nl1 — one clause **FAILED**, reported as a FAIL
Criteria written first: `checks/nl1_criteria.md`, before `checks/nl1_division.py` existed. Exact integer polynomial
arithmetic (Laurent monomials in z_α = e^{ip_α}), plain python, single process, no BLAS, **no numeric lock taken**
(permitted by the brief's rule 6). Output: `checks/nl1_out.txt`, kept unaltered.
- **nl1-A PASS.** 0 / 200 random closed inputs gave a nonzero residual: Lemma NL-11's formula solves ν∧b̂ = F̂ exactly.
- **nl1-B PASS.** 183 / 200 cases returned b̂ ≠ the input 1-form, so the check is not testing that the input is echoed.
- **nl1-C PASS** (designed-FAIL control). 20 / 20 non-closed inputs were detected, so nl1-A is not vacuous.
- **nl1-D FAIL.** 199 / 200 cases reported an inexact T_α division, against the pre-registered verdict of 0.
  *Reported as a FAIL. The script and output are unaltered and the criteria are untouched.*
  **Post-hoc diagnosis (labelled post-hoc):** the helper `T(p, a)` performs synthetic division of p by (z_α − 1) and
  returns (quotient, remainder) without subtracting E_α p first, so its remainder **is** E_α p and the clause tested a
  property Lemma NL-11 never claims; the quotient it returns is nevertheless (p − E_α p)/ν_α, i.e. the lemma's T_α p,
  which is why nl1-A passes. The 199/200 is also, post-hoc, a confirmation that E_1F̂_{1β} ≠ 0 generically — the
  Dirac-string term of Proposition NL-7.
  *Re-run under a new id with the nl1 criteria untouched:* `checks/nl1_b_criteria.md`, `checks/nl1_b_exactness.py`,
  `checks/nl1_b_out.txt`.
- **nl1b-A PASS** (0 / 800 nonzero remainders dividing g − E_αg by z_α − 1), **nl1b-B PASS** (0 / 3200 failures of
  T_α(ν_αg) = g and T_α(ν_βg) = ν_βT_α g — the two commutation steps of Lemma NL-11's step (1)), **nl1b-C PASS**
  (800 / 800 control: dividing g itself leaves a remainder, so nl1b-A's subtraction is load-bearing).
- No other probe was run after seeing a result; the only post-hoc item is the nl1-D diagnosis above, labelled as such.
- No numeric lock was taken and no float arithmetic was used anywhere in this file.

---

## FOR OTHER FILES (not edited)

Nothing below has been written into any other file. Each item names the file, the precise change, and why.

**1. NORMS.md — Lemma N1-11's box side R_eff is undischarged, and on the torus the honest constant is T (or, with
[NL-corr 1], T-free).** Lemma N1-11's proof applies Lemma N1-5 on "a box of side R_eff ≥ 1" and carries c_AXR_eff into
𝔠_P, but R_eff is never fixed and the construction is valid only on a **non-wrapping** box, whereas Theorem N1-15 is
proven on the torus. Two repairs, both in this file: **Lemma NL-1** (torus spread-axial gauge, PROVEN-HERE) replaces
Lemma N1-5 with R = the torus side and identifies the holonomy as a constant 1-form, which **Lemma NL-2** then computes
exactly (c_j = L^{−(k−j)}c_k); and **Theorem NL-3′** removes the T altogether by using (J4)'s PROVEN gauge-invariant
locality in the two line sums. Recommended edit: replace Lemma N1-11's 𝔠_P by 𝔠_P^♭ of Theorem NL-3′ and drop R_eff.

**2. NORMS.md — (N-loc) is stronger than Theorem N1-15 needs; the hypothesis should be restated as (N-loc♯).** §L3 shows
that N1-15 consumes only the two column-ℓ¹ bounds 𝔏_j ≤ 𝔠_LL^{(d−1)(k−j)} (uniformly in j, k, x and T), plus the sup
bound (N-loc-a) which is separately PROVEN. The second display of §N4's (N-loc) ("|ζ^c_{sm,j}Y(b)| ≤ …") is never used
and should be withdrawn. **And "uniformly in T" must be written into the hypothesis**: it is the entire content of the
open half, and as stated the hypothesis does not say it.

**3. NORMS.md — the near/far trade of §N4 is not available as stated, and Proposition NL-9 says why.** §N4 says (N-loc)
"can be traded for an explicit near/far split … with 𝔠 carrying a factor R_eff^d and an additive Me^{−m′R_eff} far
term". Carried out, a box-local gauge delivers the ℓ¹ budget and **breaks the sup bound by L^k** (the inter-cell
mismatch is O(θ), not O(L^{−k}θ)), and Theorem N1-15 needs both bounds from the same representative. REVIEW_NQ_S1's
"stated, not carried out" is confirmed and strengthened.

**4. PROOF.md — (CL-1)'s open half now has a scalar formulation, and it should be recorded as the named target.** The
"composite LOC with multi-scale axial gauges: OPEN" of l.6556-6558 reduces, at the trivial background in the linearised
setting, to **(N-loc-cell)** of §L7: a finite list of divisibility conditions for the cell-flux functionals
σ_μ(F̂)|_{p_μ=0} of the **already-PROVEN** curvature symbol of LINEAR_PACKAGE Theorem 4.2′ / Lemma 4.4. The missing
lemma is the twisted analogue of Lemma NL-10 (b). The leading condition is PROVEN (from Lemma 4.4's identity
𝔅^v = Σν_μh_{μv}, which gives 𝔅^v(0) = 0). Recommended: promote (N-loc-cell) to a named target under (CL-1) with this
formulation, replacing "a gauge construction to be invented".

**5. LINEAR_PACKAGE.md (errata-only; this is an addition, so for its owner to route) — Lemma NL-11 is the degree-2
companion of Lemma 4.4 and belongs beside it.** Lemma 4.4 solves the **contraction** complex at degree 1 (a co-closed
vector is a divergence, with the T_α/E_{<α} machinery). Lemma NL-11 here solves the **exterior** complex at degree 2 (a
closed 2-form symbol is an analytic coboundary) with the **same** constant κ(η, η′) and in one step, for every d ≥ 3,
and notes that F̂(0) = 0 is automatic for d ≥ 3. It is the gauge-fixing counterpart of Lemma 4.4's curvature
representative and is what a multi-scale axial gauge needs. Checked exactly (nl1-A, nl1b-A, nl1b-B PASS, with controls).

**6. PROOF.md / SF.md — the fixed-volume statement should be recorded as such, and the thermodynamic limit as the thing
it does not give.** Corollary NL-4 makes Theorem N1-15 unconditional at d = 4 at **fixed coarse side T ≥ T_0**, i.e.
UV stability at fixed physical volume, uniformly in the depth — which is what Proposition NAH-unif's quantifier ("every
torus large enough at each level", with ε_unif an infimum over **levels**) accepts. It gives nothing uniform in T, so
layer 2's cluster expansion and thermodynamic limit still need (N-loc-b). **If anyone records that (N-loc) is
discharged, that is false**: it is discharged for one consumer and one scope.

**7. Whoever owns the next numeric slot — the cheapest high-value piece in this lane.** Proposition NL-8 would reduce
Corollary NL-4's T^d ≈ 2.8·10²⁸ to **log T ≈ 16** and is ARGUED, missing only a classical lattice estimate: an explicit
bound |d_0^*Δ_0^{−1}(x)| ≤ C_d|x|^{−(d−1)} on the torus (Z/R)^d with C_d explicit, plus the first-moment cancellation
that upgrades it to |x|^{−d} given F̂(0) = 0 (which is PROVEN here). A useful precursor, exact-rational and seconds
long: tabulate Σ_{x ∈ (Z/R)^4}|d^*Δ^{−1}(x)| for R = 4, 6, 8, 12 and check it grows like R (and like log R after the
total flux is projected out). **This is an estimate, not an invention, and it is worth more to the constants than the
whole of (N-loc-cell).**

**8. The lead — two claims of mine that a hostile reviewer should attack first.** (i) Lemma NL-1's constant 4d is a
conservative bookkeeping bound and its Step 3 induction is written compactly; a reviewer should re-derive the per-
direction accounting. (ii) §L7's twisted-cohomology items 1-2 are standard but are **stated** here, not proved
entrywise; the load-bearing one is item 3 (the one-direction division's split into Θ_μ plus ν_μ^{−1}σ_μ), which is
elementary and is where a reviewer should check me. (iii) Proposition NL-7's "|Φ_ρ| ≍ L^{−k} generically" uses that the
curvature response to one coarse link does not sign-alternate along the line through it; that is an inference from the
smooth-sector shape of the response, not a theorem, and it is the one place in §L5 where a hostile reading could save
the global axial gauge.

---
