# REVIEW_FLOW_S5: hostile review of lane C session 5 (FLOW.md §35-§40 and the [RFL4-fix] edits)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f8*, f8b*. This file is the only one I
edited. No commits, PRs or pushes.

Inputs (read-only, by offset):
- FLOW.md: l.155-186 (F-Π, F-id), §16 (l.594-684: U-tad, U-dec, U-pair, U-red), §18 (l.752-812), all 22 `[RFL4-fix]`
  sites (l.762, 799, 1274-1285, 1434, 1442, 1452, 1520-1536, 1572, 1602-1608, 1626, 1636-1652, 1665), §35-§40
  (l.1675-1985) in full.
- FLOW_LOG.md, session-5 entries (l.166-215).
- REVIEW_FLOW_S4.md, all of it.
- LINEAR_PACKAGE.md §1.2-§1.3 (l.64-96). PROOF.md l.2142-2150 (the remark on the SU(N) analogue of Q = Q_str − d∘h).
- agents/ym4d-existence/EXISTENCE.md §14.1-§14.2 (l.1925-1968: (R), (IT), GS-1, GS-2).
- checks: f8_criteria.md (with amendment A1), f8_cov_gi.py (model, Part A, chain), f8b_fullbox.py (structure),
  f8_out.txt, f8b_out.txt, f8_time.txt. BSD `stat` (UTC) of all seven f8 files; md5 of f8_cov_gi.py = 3bd34639… (it
  matches FLOW_LOG).

Numerics:
- One NUMERIC LOCK acquisition, 04:49:41-04:51:09 UTC, released once with `rmdir`.
- Conditions at start: load 2.73, memory free 43% (≥ 35%, so full sizes). nice 10, all BLAS threads = 1,
  PYTHONDONTWRITEBYTECODE=1 (so nothing was written into checks/).
- f8 and f8b were run unchanged from scratchpad copies. Outputs are in
  `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revflow5/`.
- **Both outputs are identical to the stored ones, apart from the timestamp and timing lines.** f8: 38.9 s, peak RSS
  1.03 GB. f8b: 49.1 s, peak RSS 1.19 GB.
- No process was left running, and checks/ has no `__pycache__`.

Line numbers are FLOW.md lines as of this review.

---

## Bottom line

- **The [RFL4-fix] edits are correct, with two omissions** (fix S5-1):
  - REVIEW_FLOW_S4 §5 asked for (U-IR-s)(s2) to be restated for (c⊥). It was not. l.811 still states the rate on
    β[Γ^cov_n], and the G-block of Γ^cov_n need not converge.
  - Two "every background near 1" phrases were left without the 𝒰_n qualifier (l.1447-1450, l.1638-1639).
  - There is also a small inconsistency: "+ const" (l.1531) against "no additive constant" (l.1745).
- **Lemma COV-GI: CONFIRMED.** I checked both proofs line by line. It is an exact identity for every 𝒞 > 0, given (S),
  (N), MJ = D and HJ = 0. The ±½log det 𝒞^♭_G cancellation is exact. The 𝒞-dependence goes through P_⊥𝒞P_⊥ only.
  HJ = 0 holds at Wilson-critical backgrounds (constant Cartan curvature included, in all sectors), and in the Cartan
  sector at every Cartan background.
- **Is the critical-background identity enough for β? Yes in principle, with one unproven step.**
  - The alias reading makes β of the sum a fine-lattice β^fine.
  - By Lemma F-id, β^fine is the Hessian at 1 evaluated on 𝓛Φ. That equals twice the f² coefficient of the density
    along U_f = exp(H_1 f a_Φ), and that family is exactly critical.
  - So the non-critical remainder (S5-F1, with its non-local (D^*𝒞^{-1}D)^{-1}) is **not** needed for the one-loop
    coefficient.
  - But the identity has to be used at U_f in infinite volume, or uniformly in T on flux-quantised tori. That needs
    quantitative (N) at U_f, plus a C² per-site density. FLOW proves (S) and (N) only on a torus-dependent neighbourhood
    of 1, which does not contain U_f. Call this missing step **(COV-GI-∞)**. It is OPEN, at session scale (fix S5-2).
    (S) itself is not a problem: it holds at every background, exactly (§2.3).
- **Proposition COV-⊥-C: CONFIRMED, Cartan sector only.**
  - The key fact τd = 0 is correct, and so are the double-geometric sums.
  - The imported structure Q_root = Q_str − d∘h is real for the actual S4' kernel: it follows from the definition
    (LINEAR_PACKAGE §1.2).
  - Scope: at a Cartan background the Cartan sector carries no universal (log ℓ) content. The universal one-loop
    coefficient lives entirely in the root sectors, and those are OPEN. The root sectors are where UNIV for SU(N) is
    decided (§3.3).
- **f8: CONFIRMED as recorded** (re-run byte-identical).
  - Part A is a genuine test of the exact algebraic form of (iii), including the absence of a constant.
  - It is not a test of criticality: in U(1), HJ = d^TCd·dλ = 0 and MJ = D are algebraic tautologies.
  - The "B1 FAIL ⇒ structure load-bearing" reading is right in kind. But "NOT n-uniformly bounded" (l.1927) and
    "undamped" (l.1944-1945) overclaim from n ≤ 3 (fix S5-4).
- **Corrected tally: 29 PROVEN-HERE (claimed 29).** Unchanged, with scope annotations: COV-GI is a per-torus identity
  whose β-use needs (COV-GI-∞); COV-⊥-C is the Cartan sector only.

---

## 1. Priority 1: the [RFL4-fix] edits

| Fix | Where | Verdict |
|---|---|---|
| S4-1 | l.1274 | CORRECT. From 1/g_k² ≥ 1/g_{k+1}² − R: g_{k+1}^{-2} ≤ g_k^{-2}(1 + Rg_k²), hence g_{k+1}^{-p} ≤ g_k^{-p}(1 + Rg_k²)^{p/2}. |
| S4-1, √2 note and H4 row | l.1276, l.1285 | CORRECT. They say honestly that the case HIST is in is not checked. |
| S4-2a | l.1434 | APPLIED (N ≥ 3 κd(M̄) terms, O(\|bg\|⁴), outside the chain form). |
| S4-2b | l.1442 | APPLIED in the proof of (iii). **Leftover:** the §30 Reading (l.1447-1450, "the range stays finite at every background near 1") and §33 (l.1638-1639, "uniformly in n at every background near 1") still lack the 𝒰_n qualifier. |
| S4-3 | l.1572, l.1602 | APPLIED ("only on"; no per-step constants of TOW). |
| S4-4, §30 Reading | l.1452 | APPLIED. |
| S4-4, (COV-NA) and its bracket | l.1520-1530 | APPLIED: struck and kept for the record, as asked. |
| S4-4, replacement statement | l.1531-1536 | APPLIED. It writes "+ const", while §36 (iii) (l.1745) says "with no additive constant". Reconcile: the constants are the U_0- and 𝒞-independent normalisations dropped in §36's Setting (l.1720). |
| S4-4, §18 restatement | l.799-805 | APPLIED for (a2), (a4') and (c⊥). |
| S4-4, §31, §32, §33, §34 | l.1606, 1626, 1636-1652, 1665 | APPLIED. |
| S4-4, (s2) restatement | l.811 | **NOT APPLIED.** REVIEW_FLOW_S4 §5 asked for "(U-IR-s)(s1), and (s2) restated for (c⊥)". l.811 still asks for \|β[Γ^cov_n] − c_cov\| ≤ A_sθ^n. After COV-GI, β[Γ^cov_n] alone contains +½log det 𝒞^♭_G, whose n-behaviour is uncontrolled: λ_max(𝒞^♭_G) grows linearly in both f8 models. (s2) must be stated on ½log det_⊥(P_⊥𝒞_nP_⊥). See fix S5-1, which also covers the UNIV proof split at l.819. |

**Tag count:** 20 in-text tags plus 2 in §35 and §39 = 22 occurrences. This matches §39's "(20 tags)".

## 2. Priority 2: Lemma COV-GI (l.1708-1830)

### 2.1 Line-by-line check of the statement and both proofs

- **(1) MJ = D at every background.** CONFIRMED. Differentiate 𝔪_n((U_0e^X)^{g_t}) = 𝔪_n(U_0e^X)^{ev g_t} at
  t = 0, X = 0, in the equivariant charts. No criticality enters.
- **(2) The lift J.** CONFIRMED.
  - It is well defined because S ∩ D_0Λ' = {0}, and independent of the choice of λ because λ' − λ ∈ Λ'.
  - MJ = D because ev ρ = 0.
  - J is injective on K_0^⊥.
  - **(minor)** "(ρ := ρ')" is garbled. Only D_0ρ is needed, so injectivity of D_0 on Λ' is not used. It does hold
    (§2.3).
- **(3) HJ = 0 at critical points.** CONFIRMED. The gauge-invariance identity Df(X)[V_λ(X)] = 0 is differentiated once,
  and Df(0) = 0 kills the second term. So H·D_0λ = 0 for every λ ∈ Λ, as a form on all of E.
  - Constant Cartan curvature is critical: the root components of the gradient vanish by torus invariance, and the
    Cartan components are ∝ d^T(constant 2-form) = 0. ✓
- **(4) Cartan backgrounds, Cartan sector.** CONFIRMED.
  - For Cartan λ and Cartan X, V_λ(X) = dλ, so DV_λ(0)Y = 0 for Cartan Y.
  - Root Y is orthogonal to Cartan by torus invariance of the Hessian at a torus-fixed U_0.
  - With a torus-equivariant S, ρ is Cartan, so Jμ ∈ Cartan.
- **(5)-(9), the Gaussian proof.** CONFIRMED.
  - Gram factor det(J^*J)^{1/2}: the Gram matrix of (μ, X') ↦ Jμ + X' is diag(J^*J, 1), because S' ⊥ Ran J.
  - Quotient marginal: q(y) = det(D^*D)^{-1/2}p^⊥(P_⊥y). Translation in G, then Fubini over ker D^* ⊕ G.
  - Π = 𝒞^{-1/2}(1 − R)𝒞^{-1/2}; ΠD = 0; Π𝒞w = w on ker D^*; and ΠP_G = 0. Hence Π = P_⊥𝒞_⊥^{-1}P_⊥.
  - The powers of 2π match: (dim S − m)/2 on both sides.
  - Positivity of (H + M^TΠM)|_{S'} comes as the Schur complement of T^*AT > 0. The cross block vanishes by HJ = 0.
  - The kernel of (H + M^TΠM)|_S is exactly J(Λ_n^♮).
- **(10), the algebraic proof.** CONFIRMED.
  - det 𝒞 = det 𝒞_⊥·det 𝒞^♭_G (Schur).
  - det(D^*𝒞^{-1}D) = det(D^*D)/det 𝒞^♭_G (polar decomposition).
  - det(T^*AT) = det(J^*J)·det_SA = det(D^*𝒞^{-1}D)·det_{S'}(Schur).
  - The two displays of (iv) follow, and they add to (iii).
  - This second proof is independent of the first: it needs only finite-dimensional block determinants.
- **The Feynman-form bullet (l.1729-1732).** CONFIRMED when HD_0Λ_res = 0, which is true at critical points.
  - The conversion factor is 𝒞-independent but **f-dependent**. It is part of (a3), and it must be kept in β.
  - Its wording "differs by a 𝒞-independent factor" is correct, but this should be said.
- **The S5-F1 remainder (l.1821-1830).** CORRECT as an identity (multiplicativity of det). It needs A_♮ > 0, which is not
  stated: add "provided A_♮ > 0".
  - The diagnosis is right. The remainder involves (D^*𝒞^{-1}D)^{-1}, which is non-local, so U-pair (e) is not
    available for it as written.
  - That retracts the suggestion in my S4 review §2 (5)(b) (treat it as a U-pair pairing). The retraction is correct.

### 2.2 Does HJ = 0 at the critical backgrounds suffice for β? (This decides the route to UNIV for SU(N).)

**The chain of reductions is sound:**
1. Corollary U-red with the alias reading: B_n = −β^fine[F̄], with F := Γ^{W0}_n + ½log det 𝒞_n as a gauge-invariant fine
   functional of U_0 (l.674-684). The tower point Φ_0(V) has already been eliminated at this step. That is why HJ ≠ 0
   there (l.1818) is irrelevant.
2. β^fine of a gauge-invariant functional is fixed by its Hessian at 1. By Lemma F-id (l.180-182), β = c with
   H(𝓛Φ, 𝓛Φ) = cφ² per site, where 𝓛Φ is the linear constant-curvature field.
3. Along the one-parameter family U_f := exp(H_1 f a_Φ) we have d²/df² F(U_f)|_0 = D²F(1)[H_1a_Φ, H_1a_Φ], since
   DF(1) = 0. So β^fine = 2 × (the f² coefficient of the density of F(U_f)).
4. **U_f is exactly critical for every f.** It is the Cartan constant-curvature field. So COV-GI (ii)(a) applies along the
   whole family, in all sectors. The f² coefficient of F(U_f) is then the f² coefficient of COV-GI's right side.

Hence the remainder ½log det(1 + A_♮^{-1}(H − H_♮)) is **not needed for the one-loop coefficient**. This holds because
the one-parameter family that computes β can be chosen inside the critical set. It is not an approximation.

**The one unproven step: (COV-GI-∞).** Items 3-4 need COV-GI at U_f either in infinite volume (per-site densities) or on
flux-quantised tori f = 2πm/T² uniformly in T, with T → ∞. FLOW proves (S) and (N) only "at 1 and on a torus-dependent
neighbourhood of 1 by continuity" (l.1722-1728). In infinite volume, U_f is not near 1 in link variables: the potential
grows linearly. On a torus, nothing shows that U_{2πm/T²} lies in that neighbourhood.

What is needed:
- **(S) at U_f.** This holds at **every** background, exactly. If ρ ∈ Λ' and D_0ρ = 0, then |ρ| is constant along links
  (unitary transport), and ρ vanishes at the level-n sites, so ρ = 0. A T-uniform Dirichlet gap follows from Kato's
  inequality. One line.
- **(N) at U_f with a T-uniform gap.** This is not automatic.
  - In the root sectors the Wilson Hessian at constant Cartan curvature has negative (Nielsen-Olesen-type) modes of size
    ∼ |f|. Only the IR term M^T𝒞^{-1}M lifts them.
  - What is needed is a quantitative gap A(1) ≥ c_n > 0 on S, uniform in T (c_n ∼ ℓ^{-2} is expected), together with a
    gauge-covariant perturbation bound at U_f for |f| ≤ ε_0c_n.
  - FLOW proves (N) at 1 by a kernel argument with no gap, so this is OPEN.
- **The per-site density of F(U_f) is C² in f near 0, with Lemma F-id extended from finite support to F's exponentially
  decaying (at fixed n) Hessian kernel.** Lemma F-Π (ii)'s moment bound is the needed input.
- §36 Reading (b) (l.1814-1817) cites "Lemma F-Π (i)" for the identification of β with the constant-curvature
  coefficient. The identification is Lemma F-id. F-Π (i) only reduces to one colour direction.

**Verdict.** COV-GI is PROVEN as stated: per torus, given (S), (N), HJ = 0. The claim "this is what β needs; there it
holds in all sectors" (l.1816-1817, l.1954-1956) is correct as a reduction. It is conditional on (COV-GI-∞), which is
session-scale. With (COV-GI-∞), the 𝒞_n-dependence of B_n is through P_⊥𝒞_nP_⊥ only, for SU(N), in all sectors.

**A caution that FLOW does not state.** In the root sectors the individual right-side terms of (COV-GI) at U_f need not
have an f² coefficient at all.
- ½log det(D_B^*D_B) is the determinant of a massless charged level-n Laplacian. In 4D its density at constant field is
  of the F² log F type, so it is non-analytic at f = 0.
- The left side is analytic, because A is gapped. So the infrared singularities must cancel between groups of right-side
  terms:
  - ½log det(D^*D) against ½log det(J^*J). J^*J is the fine harmonic-extension energy, ≈ c·D^*D at low momentum.
  - ½log det_⊥(P_⊥𝒞P_⊥) = ½log det 𝒞 − ½log det 𝒞^♭_G, with det 𝒞^♭_G = det(D^*D)/det(D^*𝒞^{-1}D). Both D^*D and
    D^*𝒞^{-1}D are massless charged.
  - det'_S(H + M^TΠM), on the non-local complement S' = S ⊖ J(Λ_n^♮).
- So in the root sectors (COV-⊥) as stated ("β of ½log det_⊥(P_⊥𝒞_nP_⊥) bounded uniformly in n") must be stated for
  IR-safe groups, not term by term. An IR-safe group is, for example, ½log det 𝒞_n − ½log det(D^*D) + ½log det(D^*𝒞_n^{-1}D),
  where the leading low-momentum parts of the last two are proportional.
- In the Cartan sector this caution does not apply, because D = d is f-independent there.

## 3. Priority 3: Proposition COV-⊥-C (l.1832-1910)

### 3.1 Checks

- **Imports.** GS-1 (EXISTENCE l.1944-1949) and GS-2 (e) (l.1951-1966) are as quoted. ||Q_str^m|| ≤ L^{-m} follows from
  GS-2 (e) with σ = 1. The FLOW chain's Q (the S4' root map at 1, in level units) is LINEAR_PACKAGE's Q_root. Its
  structure Q_root = Q_str − d∘h holds **by the definition of S4'**:
  - y runs over the full block B(X), including the μ-direction.
  - The leg c_Y → y + Le_μ is the L e_μ-translate of c_X → y.
  - So both legs average to the same μ-independent h, at X and at Y.
  - This is LINEAR_PACKAGE l.70-73 (PROOF l.982-990; c8(f) ≤ 2e-16).
- **(C1).** CONFIRMED. T_k(B)d = d ev at every Cartan B_k, by covariance with D_B = d. So
  P_⊥^{(k+1)}T_kP_G^{(k)} = 0, and P_⊥A_j factorises into one-step compressions.
- **(C2).** CONFIRMED. The Cartan-sector map depends only on closed-loop fluxes, F_k is constant per orientation by
  translation and reflection covariance, and 𝒯 does not depend on k (uniform chain). τd = 0 follows coefficient-wise
  from 𝒯(φ)d = d ev.
- **(C3).** CONFIRMED. Conjugation is −1 on 𝔥 and commutes with W_♮ and the transports, so 𝒯 and 𝒫 are even.
- **(a).** CONFIRMED.
  - P_⊥Q^m = P_⊥Q_str^m.
  - The m = 0 term gives the lower bound κ^{-1}P_⊥.
  - Σ_mL^{-2m} gives the upper bound.
  - The one-level extension adds exactly the m = n term.
  - f8b confirms all of this numerically in a model with the same structure, with the bound attained: spectra up to
    1 + L^{-2} + L^{-4} = 1.123457.
- **(b).** CONFIRMED.
  - ||P_⊥T_kP_⊥|| ≤ L^{-1} + c_TF_k².
  - Σ_{k<n}F_k² ≤ 4ε_0²/(L⁴ − 1). FLOW writes 8ε_0²/(L⁴ − 1), which is conservative and harmless.
  - The lower bound comes from the j = n term.
- **(c).** CONFIRMED.
  - Index bookkeeping: k = n − 1 − a gives L^{4k−4n} = L^{-4-4a}; the constraint j ≥ 1 gives a + b ≤ n − 2; the
    π-term has L^{4(j−1)−4n} = L^{-4-4i}.
  - Norms: ||X_{a,b}|| ≤ ||τ||L^{-2a-2b-1}, so the terms are L^{-5-6a-2b}.
  - The tail is dominated by (a, b) = (0, n − 1), giving L^{-3-2n}, so the rate is L^{-2n}.
  - ||K_n − K_∞|| ≤ κL^{-2n}/(1 − L^{-2}).
  - **(minor)** "|tr_sZ| ≤ 4r||Z||" needs Z to commute with level-n translations. It does here, because the Cartan-sector
    maps depend only on the translation-invariant fluxes. Say so.

### 3.2 Scope: what COV-⊥-C does and does not buy

At a Cartan background, the Cartan-sector fluctuations are neutral. In the continuum their determinant is f-independent,
and on the lattice the f-dependence is O(f²) and local: the cos-weights of H and the |m|-weights of Π. So the Cartan sector
contributes a non-universal constant and no log ℓ.

COV-⊥-C is necessary bookkeeping, and it is now proven. But **none of the universal one-loop coefficient is in it.** All
of the universal coefficient (11N/3 in the standard normalisation; FLOW's normalisation is not re-derived here) comes from
the root sectors ±α, where the fluctuations carry charge
α(H_1).

"(s2) is now discharged in the Cartan sector" (l.1968) is true for the Cartan block of ½log det_⊥, once (s2) is restated
(fix S5-1).

### 3.3 Root sectors: how hard is the extension?

**What carries over unchanged:**
- covariance A_j(B)D_{B_j} = D_{B_n}ev at every background, hence P_⊥(B_{k+1})T_kP_G(B_k) = 0 exactly, and the
  factorisation of P_⊥A_j;
- the finite range (COV-str (iii));
- COV-GI itself, at U_f, given (COV-GI-∞).

**What is new and hard, in increasing order:**

**(R1) The GS-1 analogue at a Cartan background, in a root sector.**
- The linearisation at fixed B is linear in X. Each contour still splits into leg + straight + leg, with covariant
  (background-transported) legs.
- But the "straight" part is transported to c_X along a (σ, y)-dependent leg, and the polar-part derivative at a
  non-unitary mean adds Re(e^{iΦ}m̄)/|m|²-type weights.
- Whether T_k(B) = Q^B_str − D_{B'}∘h_B holds exactly, up to O(F_k) corrections that annihilate D_B, is not known.
- PROOF l.2146-2150 records that there is **no nonlinear SU(N) analogue of Q = Q_str − d∘h as an identity**, only an
  estimate with Ad-transports 1 + O(|a|).
- In a root sector there is no evenness within a single sector (conjugation exchanges α and −α), so the corrections are
  O(F_k), not O(F_k²).
- Session-scale to decide.

**(R2) Damping.**
- For the straight part, entrywise domination |Q^B_str| ≤ Q_str(0) gives ||Q^B_str^m|| ≤ L^{-m} for any unitary
  background (diamagnetic). That is easy.
- O(F_k) corrections still give n-uniform operator bounds, since Σ_kF_k ≲ ε_0 for |f| ≤ ε_0L^{-2n}.
- For the f² coefficient, two first-order insertions at levels k and k' give weights L^{2(k−n)}L^{2(k'−n)} times the
  damping between them. These sums should converge, but they must be done.

**(R3) The real obstacle: non-local, background-dependent P_⊥(B), and IR safety.**
- P_⊥(B) = 1 − D_B(D_B^*D_B)^{-1}D_B^* involves the massless charged level-n Laplacian.
- At constant curvature the background is not a bounded or translation-invariant perturbation. The potential grows
  linearly, and only magnetic translations survive.
- So the f-expansion needs a magnetic (twisted-convolution) symbol calculus on the lattice, instead of the ordinary
  symbols used in all of §17-§37.
- On top of that, the right-side terms must be grouped so that each group's f² coefficient exists (§2.2 caution).
- This is where the log ℓ of β_0 actually sits. The 𝒞-independent determinants ½log det(D^*D) − ½log det(J^*J) and the
  FP and residual-slice factors are **not only IR bookkeeping. They carry part of the universal coefficient** (in the
  continuum, the ghost-like charged-scalar determinants contribute to 11N/3).
- Estimate: several sessions. **This is the crux of UNIV for SU(N).**

**(R4)** Then (a2) in transverse form (vertices of M^TΠM, non-local through P_⊥(B)), (a3) and (a4') cross entries, and (b),
all in the root sectors, with the UNIV proof's J_n rebuilt for the regrouped operator (fix S5-1).

## 4. Priority 4: f8, f8b and their reading

### 4.1 Provenance

The provenance is consistent and the criteria predate both scripts.

| File | Born (UTC) | Last modified (UTC) | Size |
|---|---|---|---|
| f8_criteria.md | 04:31:31 | 04:37:52 (amendment A1 append) | 7766 |
| f8_cov_gi.py | 04:34:13 | 04:34:57 | 15508 |
| f8_out.txt | 04:36:21 | 04:37:00 | 5089 |
| f8b_fullbox.py | 04:38:40 | 04:38:40 | 7248 |
| f8b_out.txt | 04:38:55 | 04:39:44 | 5060 |

- The A1 append is labelled POST-HOC and came after the official run (04:37:00).
- f8b was born after A1.
- The FLOW_LOG ordering quirk (an entry headed "04:38" placed before the 04:37:52 entry) is corrected in the log itself.
  It is honest.

### 4.2 Part A (and A')

- All PASS, and the control fails as required, in both models (re-run identical).
- Residuals: ≤ 5.7e-13 in f8 and ≤ 4.5e-13 in f8b.
- Kernel of H + M^TΠM: ≤ 3.7e-15 relative, with the next eigenvalue ≥ 1.6e-3.

**What it tests:**
- The exact form of (iii): Gram factor, det(D^*D), the absence of a constant, both forms of Π. This is real and
  valuable. A wrong Jacobian would have shown up at O(1).
- "𝒞-dependence only via P_⊥𝒞P_⊥", through two different completions (𝒞' and 𝒞'').

**What it does not test:**
- In U(1), H = d^TCd, so HJ = d^TCd·dλ = 0, and T_kd = d ev holds by construction (root-to-root paths, Σω = 1). A0 is
  therefore a tautology.
- The "f ≠ 0" cases are cos-weighted Hessians and phase-weighted maps, not actual torus configurations: f = 0.03 is not
  flux-quantised on these tori. They test the f-dependent algebra only.
- Nothing about (ii)(a) (non-abelian criticality), root sectors, (N) at U_f, or the Feynman-to-δ-slice conversion is
  tested.
- §38 Reading (1) (l.1940-1941) is accurate on this, except that "in d = 2, 3, 4" should add "(U(1); HJ = 0 holds
  identically there)".

### 4.3 Part B: is "Q = Q_str − d∘h is load-bearing for (COV-⊥)" the right reading?

**Right in kind, overstated in degree.**

**The B1 diagnosis is correct.**
- Model 1's paths average over t ⊥ μ, a μ-dependent set. So Q_staple = Q_tr − (∂_μh_μ)_μ, with a different 0-form h_μ
  for each μ. That is not exact, so P_⊥ does not remove it.
- The criteria's prediction was otherwise self-consistent: for the transverse-box Q_tr in d = 4, Q_tr^mQ_tr^{mT} = L^{-2m}·1
  exactly (disjoint supports). So the leg structure is the only error. B1 FAIL stands.

**The overclaim.**
- FLOW says the model-1 transverse block "is NOT n-uniformly bounded" (l.1927) and that a covariant map without the
  structure "can have an undamped transverse block" (l.1944-1945).
- The data are 1, 2.397, 3.524 at n = 1, 2, 3 (T = 2). The increments are 1.397 and 1.127, a ratio of 0.81.
- That is equally consistent with a bounded block converging slowly (limit ≈ 8 if the ratio held), as with growth.
- T-dependence is visible too: 2.075 at T = 3, n = 2.
- Correct reading: "the GS-2 bound (1 − L^{-2})^{-1} fails in model 1 by a factor > 3 at n = 3, and the
  increments are not L^{-2}-damped (ratio 0.81 vs 0.11). Whether the block is n-uniformly bounded is not decided by
  n ≤ 3" (fix S5-4).
- What is load-bearing for **this proof** of COV-⊥-C is GS-1's exactness. In general, the requirement is that P_⊥QP_⊥ be
  contracting with summable powers (Q = Q_0 − d∘h with Q_0 damping is one way).

**Side observation.** B4 PASSES in model 1, which is the model where B1 fails (increment ratio 0.179). So the three-point
geometric test of c^⊥_n is not diagnostic of n-uniform damping. Do not cite B4-type passes as evidence for (COV-⊥) without
the operator bound.

**Does the actual soft kernel have the structure? Yes, at the trivial background, exactly.**
- LINEAR_PACKAGE §1.2 l.70-73: Q_root = Q_str − d∘h, from the full-box definition of S4' (l.65-68). PROOF l.982-990;
  check c8(f) ≤ 2e-16 (no criteria file, as LINEAR_PACKAGE l.403 notes).
- EXISTENCE §14.1 imports it as (R).
- At Cartan backgrounds, in the Cartan sector, COV-⊥-C needs only (C1)-(C3) beyond it.
- In the root sectors it holds only as an estimate (PROOF l.2146-2150). That is (R1) above.

### 4.4 B1'b (POST-HOC)

- FAIL as pre-stated, by λ_max − L^{-4} = +5.8e-14 (4.7e-12 relative, against a 1e-12 tolerance).
- **The round-off reading is well supported.** By the GS-1 analogue (B1'a, ≤ 6.2e-16), P_⊥(𝒞_3 − 𝒞_2)P_⊥ is
  P_⊥Q_box²Q_box^{2T}P_⊥ in level units. That same operator was computed directly in B1'b's first part, with norm
  0.012345679012 = L^{-4} to 12 digits, passing at 1 + 1e-12.
- The increment is a difference of two matrices whose G-block is ≈ 12. 5.8e-14 is about 20ε·||𝒞||.
- FLOW's wording (l.1934-1938) is accurate.

## 5. Verdicts per item (session 5)

| Item | Verdict | Fix |
|---|---|---|
| [RFL4-fix] S4-1..S4-4 | CONFIRMED except: (s2) not restated; two 𝒰_n leftovers; the "+ const" vs "no additive constant" mismatch | S5-1 |
| (S), (N) bullets (l.1722-1728) | CORRECT near 1 per torus; (S) in fact holds at every background; (N) at U_f, uniformly in T: OPEN | S5-2 |
| Lemma COV-GI (i)-(iv), both proofs | **CONFIRMED** | S5-3 (minor wording) |
| Reading (b): "β needs exactly the critical case" (l.1814-1817) | CORRECT as a reduction; conditional on (COV-GI-∞); cite F-id, not F-Π (i) | S5-2 |
| S5-F1 remainder (l.1821-1830) | CORRECT (add "A_♮ > 0"); correctly not needed for β | S5-3 |
| Proposition COV-⊥-C (a)-(c) | **CONFIRMED** (Cartan sector; imports as labelled) | S5-3 (tr_s translation note) |
| COV-⊥-C Reading (l.1902-1910) | CORRECT, but it should state that the Cartan sector carries no universal content | S5-5 |
| f8 A0-A4, A-ctl (re-run identical) | CONFIRMED; A0 is tautological in U(1) | S5-4 (wording) |
| f8 B1 FAIL, diagnosis | CONFIRMED | — |
| "NOT n-uniformly bounded" / "undamped" (l.1927, l.1944-1945) | OVERCLAIM from n ≤ 3 | S5-4 |
| f8b A', B1'a, B4' PASS; B1'b FAIL | CONFIRMED; the round-off reading is supported by B1'b's own first part | — |
| §39 "UNIV now" (l.1966-1970) | Must add (COV-GI-∞), (s2⊥), the IR-safe grouping, and the UNIV proof's re-split | S5-1, S5-5 |

**Corrected tally: 29 PROVEN-HERE (claimed 29).** That is 27 + Lemma COV-GI (per torus, given (S), (N), HJ = 0) +
Proposition COV-⊥-C (Cartan sector; GS-1 and GS-2 (e) imported). Otherwise unchanged:
- GAP: UNIV-rate.
- WRONG and superseded: F-split, the session-3 sentence, F-mono clause 3; (COV-NA) as a target.
- IMPORTED-AND-REVERIFIED: L4b.
- **New OPEN items:** (COV-GI-∞) [s]; (s2⊥) for SU(N) root sectors; the IR-safe grouping of COV-GI's root-sector right
  side [s-P].

## 6. Binding fixes for the next lane-C session

1. **S5-1.**
   - Restate (U-IR-s)(s2) at l.811 as (s2⊥): |β[½log det_⊥(P_⊥𝒞_nP_⊥)] − c_⊥| ≤ A_sθ^n, with the 𝒞-independent COV-GI
     determinants assigned explicitly to the J_n side or to (a4').
   - Re-split the UNIV proof (l.819: "B_n = −∫J_n − β[Γ^cov_n]") for the regrouped functional, and redefine J_n
     (l.770-776) with the operator H + M^TΠM in place of H + D𝔪^T𝒞^{-1}D𝔪.
   - Add 𝒰_n to l.1447-1450 and l.1638-1639.
   - Reconcile "+ const" (l.1531) with l.1745.
2. **S5-2.**
   - Add (COV-GI-∞) as an explicit hypothesis of §36 Reading (b), §39 S5-1 and §40.
   - Prove (S) at every background (one line: unitary transport plus vanishing at the level-n sites; Kato for a
     T-uniform gap).
   - State (N) at U_f, |f| ≤ ε_0c_n, uniformly in T, as OPEN.
   - Cite Lemma F-id (extended to exponentially decaying kernels via F-Π (ii)) for the identification of β with the
     f² coefficient at constant curvature.
3. **S5-3 (minor).**
   - In §36 (2), fix "(ρ := ρ')".
   - In the remainder formula, add "provided A_♮ > 0".
   - In the Feynman bullet, add "𝒞-independent but U_0-dependent (part of (a3))".
   - In COV-⊥-C (c), note that the X_{a,b} and Y_i commute with level-n translations.
4. **S5-4.**
   - At l.1927 and l.1944-1945, replace "NOT n-uniformly bounded" and "undamped" with the bounded/unbounded-undecided
     wording of §4.3.
   - At l.1940, add "(U(1): HJ = 0 and MJ = D hold identically, so A0 is structural)".
   - Do not cite B4-type passes as evidence of damping.
5. **S5-5.**
   - In §37 Reading and §39, state that the Cartan sector carries no universal log ℓ content.
   - List the root-sector programme (R1)-(R4) of §3.3 as what UNIV for SU(N) still needs.
   - Add the §2.2 caution: in the root sectors the COV-GI right-side terms are individually IR-singular at f = 0, and
     (COV-⊥) must be stated for IR-safe groups.

## 7. What UNIV for SU(N) still needs (verdict)

After session 5, the coarse-gauge sector is **settled in principle**:
- COV-GI removes it exactly, at the only backgrounds β needs, once (COV-GI-∞) is supplied (session scale).
- The Cartan sector of the transverse determinant is done.

**What remains carries all of the universal coefficient.** In order:
1. (COV-GI-∞).
2. The root-sector GS-1 analogue (R1). It is an estimate, not an identity, per PROOF l.2146-2150.
3. Diamagnetic damping (R2). Easy.
4. A magnetic symbol calculus for P_⊥(B), with an IR-safe regrouping of ½log det(D^*D) − ½log det(J^*J), the FP and
   residual-slice factors, ½log det_⊥ and det'(H + M^TΠM) (R3). Multi-session; the crux.
5. (a2) in the transverse form, (a3), (a4'), (b), and (s1)/(s2⊥), with the UNIV proof rebuilt for the regrouped operator
   (R4).

**Recommended next target:** (COV-GI-∞) together with (R1) at the linearised level, at a constant Cartan background in a
single root sector, for SU(2) (one root pair).

Recommended check: the f8 harness extended to a charged root sector, with transports e^{iα(H_1)Φ}, on flux-quantised tori.
- (A) COV-GI with D = D_B (background-dependent), including the IR-safe grouped f² coefficient as T grows.
- (B) Whether P_⊥(B)T_kP_G(B) = 0 holds to round-off, and whether P_⊥(B)(T_k − Q^B_str)P_⊥(B) is O(F_k) or O(F_k²).
