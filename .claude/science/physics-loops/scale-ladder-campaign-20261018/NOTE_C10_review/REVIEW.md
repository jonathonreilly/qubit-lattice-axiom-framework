# Review of the C10 lane note (fresh-context, same model family)

**Provenance.** I am a fresh-context reviewer of the same model family (Claude Opus 5.5) as the C10 worker, its checker and the note writer. I am not independent of that family. I read the note, the runner, `C10_.../FINDINGS.md`, `C10_check/REPORT.md`, the C9 findings (P7 and the common-zero lemma) and the arc-lemma note's "Scope: structure functions" section. I checked the mathematics by hand. My script `rev_c10.py` imports nothing from the runner and tests three things the runner does not test (R1–R3).

**Verdict: approve with changes applied.** I found no mathematical error in any theorem or certificate. I made the following changes:
- one runner fix: two checks had tautological parts, and are now non-tautological; the check count is unchanged;
- one corrected over-strong necessity (the diagonal-coefficient hypothesis, in three places);
- one relabel, with an explicit formula, for the writer's reworded common-zero argument;
- three small precision edits and two provenance or timing lines.

## Files
- Note: `/home/user/wt-lanes/docs/A_ONE_DIMENSIONAL_LATTICE_HAMILTONIAN_CONSTRAINT_WITHOUT_LOCAL_DEGREES_OF_FREEDOM_IS_FIRST_CLASS_BUT_LATTICE_PARAMETRISED_FIELD_THEORY_IS_ANOMALOUS_AND_FIRST_CLASSNESS_IS_LOCAL_ZERO_CURVATURE_BOUNDED_THEOREM_NOTE_2026-10-18.md` (edited in place, not staged)
- Runner: `/home/user/wt-lanes/scripts/lattice_hamiltonian_constraint_first_class_and_zero_curvature_2026_10_18.py` (edited in place, not staged)
- I did not run `git add`, commit, push, or regenerate the graph or manifest.

## Runs (Python 3.13.16, sympy 1.14.0, 2 cores pinned)
- **Default, before my edits:** `TOTAL: PASS=59 FAIL=0`, 126.6 s (`runner_default_pre_review.log`).
- **`--slow`, before my edits:** `TOTAL: PASS=68 FAIL=0`, 639.5 s (`runner_slow_pre_review.log`). Every number the note quotes for `--slow` matches:
  - A3 census: 64 / 240 / 1004 / 1004 non-degenerate components;
  - 48 / 16 / 20 / 20 degenerate first-class pieces;
  - ranks 8, 6 / 7 / 10, 9 / 9;
  - P5m: 126 unknowns, consistent, 256 s;
  - staggered example at L = 8;
  - P6 at (8,1) and (9,2).
- **Default, after my edits:** `TOTAL: PASS=59 FAIL=0`, 119.6 s (`runner_default.log`).
- **`--slow`, after my edits:** `TOTAL: PASS=68 FAIL=0`, 590.7 s (`runner_slow.log`).
- **Mutation test of the rewritten checks:** with the expectation sign-flipped to Λ_n = −λ̂_n (the C9 ruler sign), all six L4b checks and A5-F fail, 0/7 pass. A first draft of my L4b rewrite had a transposed index (D_xz for D_zx) and failed 6/6. This was my bug, fixed before the counted run; it also shows that the new check is sensitive.
- **Reviewer script `rev_c10.py`** (log `rev_c10.log`): 6 PASS, 0 FAIL; the R3 (1,1) case did not complete (killed at my 900 s limit, 18 Gröbner radical-membership calls with explicit rational u-dependence), so it gives no evidence either way.
  - **R1 (common-zero basis change).** Position-space computation at L = 6, forward Δ, circulant M with rational μ. It checks Λ′_n = μ̂₀Λ_n and c̄′(m,n) = μ̂_m μ̂_n c̄(m,n)/μ̂_{m+n} for all (m,n), and that the checker's unscaled "Λ_n unchanged" fails for μ̂₀ ≠ 1. PASS.
  - **R2 (the disclosed post-hoc witness).** With X₄ = 3 the A1-U point has n₃ = 0 (m = [5,16,−1,−18,−2], n = [−3,14,−5,0,−6]), so it is not in U. With X₄ = 8 every m_x, n_x ≠ 0. A hand solution of ℓ = k = 0 (π = −ΔX, P = Δφ, m = 2Δ(φ − X), n = −2Δ(φ + X)) is cross-checked against the definitions. PASS. The disclosure is accurate. The claim is existential and the criterion was unchanged, so the change is harmless.
  - **R3 (P4b by another route).** Explicit u-variables with g = 1 + Δu written out, with no chain rule. Radical membership of every κ is tested by Gröbner(eqs + [1 − tκ]) = [1], instead of relying on the completeness of `sympy.solve`. (1,0): PASS (6 unknowns, 88 equations). (1,1): not completed in 900 s. P4b's (1,1) row therefore rests on the runner's `sympy.solve` result alone.

## Mathematics (checked by hand)
- **Model A brackets and Theorem A1.** Correct.
  - {a,a} = A, {β,β} = −A, hence {ℓ,ℓ} = {m,m} = 0 and {ℓ_x, m_y} = 2A_xy. The Leibniz rule gives ⅛A(ℓ_x m_y + m_x ℓ_y), and the C⁻ line comes from {γ,γ} = +A.
  - With A = 2Δ, the right-hand side Δ_xy((m_y/m_x)C⁺_x + (m_x/m_y)C⁺_y) reproduces ¼Δ_xy(ℓ_x m_y + m_x ℓ_y).
  - Qualifiers: on U, C⁺ = 0 ⟺ ℓ = 0 and C⁻ = 0 ⟺ k = 0. Σ ∩ U is regular, since dC⁺ = ¼m dℓ there and rank(ℓ,k) = 2L. It is coisotropic of dimension 2L in 4L, hence Lagrangian, and the reduced space is 0-dimensional.
  - Winding caveat: on ℓ = k = 0, m = 2Δ(φ − X), so Σm = 0 in the periodic sector. This is correct.
  - Dirac algebra and Fourier constants: {D₀,H_n} ≈ λ̂_n H_n and {H₁,H₋₁} ≈ 2λ̂₋₁D₀ = (λ̂₋₁ − λ̂₁)D₀. Correct.
- **A3 kink rule.** Correct.
  - On a piece, {C⁺_x,C⁺_y} vanishes iff x and y make the same choice. The other term, A m_x ℓ_y, is a product of two factors not identically zero on a non-degenerate piece.
  - {C⁺_x,C⁻_y} = ⅛S(ℓ_x k_y + m_x n_y) vanishes iff (ℓ_x, n_y) or (m_x, k_y). The runner's rule `sp_[i] != sm[j]` encodes exactly this.
  - Central: A connects the cycle, so there are 4 uniform branches. Forward: S_xx ≠ 0 and S_{x,x+1} ≠ 0 force (ℓ,n) and (m,k). The C⁻ kink sign −⅛A n_x k_y is correct.
  - The rule's local argument is general-L. The note conservatively claims only L = 4, 5, where the census decides which pieces are non-degenerate. That is fine.
- **Model P, Theorem P and its hand proof.** Correct.
  - P1 follows from {g_x, Π_y} = Δ_xy. Substituting Π⁺ = −a²/(4g) gives −Δ_xy(a_x g_y − a_y g_x)²/(4g_x g_y).
  - The witness u = φ = 0, π = e_x gives −Δ_xy/4 ≠ 0 for any x ≠ y with Δ_xy ≠ 0, which exists for every antisymmetric Δ ≠ 0. Only antisymmetry is used.
  - One precision: Σ is a graph over the remaining variables only where g^± ≠ 0, which holds near the witness (edit E7).
  - The forward-difference anomaly is shown only at L = 5, by the rational point 3/784. The Answer said it without L (edit E3).
- **L3.** Correct. {K_x,K_y} = ∂_{X_y}h_x − ∂_{X_x}h_y + {h_x,h_y} has no P. Σ is the graph P = −h. A P-free function vanishes on the graph iff it vanishes identically.
  - **Diagonal-coefficient hypothesis.** The note said a local h *needs* a diagonal coefficient. As a necessity this is false: C⁺ = α(Π⁺ + h) with banded α and local h has local h, and first-classness depends only on Σ, so the certificates cover it. What is true is that a diagonal local coefficient *gives* a local h, while C⁺ = αΠ⁺ + β with banded non-diagonal α *generally* gives a quasi-local h = α⁻¹β. Reworded in the claim_scope, the Status line and the L3 bullet (E1, E2, E5).
- **L4 ("if" only).** Correct.
  - {g_x, K_y} = Δ_xy gives the Poisson form.
  - At g = 1: c̄(m,n) = λ̂_n − λ̂_m, Λ_n = λ̂_n, {C₁,C₋₁} = (λ̂₋₁ − λ̂₁)C₀, and Λ₂/Λ₁ = 2cos(2π/L) for central Δ.
  - The converse is correctly disclaimed.
  - The sign note against C9's Λ_n = −λ_n is consistent with C9's P7, {X_a,X_b} = −C_ab^e X_e. The arc-lemma scope section indeed gives Λ_n = −λ_n.
- **Basis dependence and the reworded common-zero claim.** The claim "rescales Λ_n by the uniform Fourier coefficient and leaves every ratio unchanged" is **right**, and it corrects the checker's "leaves Λ_n unchanged", which holds only when μ̂₀ = 1.
  - Derivation: at a common zero the {C,M} terms vanish. A circulant M acts in Fourier as C′_n = μ̂_n C_n. So c̄′(m,n) = μ̂_m μ̂_n c̄(m,n)/μ̂_{m+n}, and Λ′_n = μ̂₀Λ_n. Invertibility gives μ̂_n ≠ 0, so (S) itself is also invariant, which supports "basis dependence ⟺ moved background".
  - Labelling problem: the text was labelled "checker's argument, not certified" although the rescaling was the writer's correction. Relabelled, with the formula written out and R1 cited as campaign history (E6).
- **P4a.** Correct by hand: F_xy = Δ_xy(−v_x²/4 − v_y²/4 + v_x v_y/2) = −Δ_xy(v_x − v_y)²/4, and g_x g_y F equals the anomaly.
- **Certificates' premises.** Correct.
  - The truncated flatness through order N − 1 involves the c-jets only up to order N: N from the one ∂_u, N − 1 from {h,h}. So it is complete for C^N germs. For a C^N germ, the shift-invariance condition on the Taylor polynomial is exact.
  - The Rabinowitsch normalisation encodes h(a ≡ 1, u = 0) = Σc_rs(0) ≠ 0.
  - Only F_{0,y}, y > 0, is imposed. That suffices by covariance and antisymmetry.
  - Exploration-only rows are labelled as such: the full-1/g g-class rows, the continuum-response (1,2) row and P6 (11,3).
- **Staggered example.** Correct. Odd-site a's commute at distance 2 for central Δ, and the linear response is −A²e/2 (even) or 0 (odd) against −A²e/4. The note correctly says it is 2Z-covariant only and lies outside the certified classes.
- **P6.** The certificate is genuine (linsolve empty). The Sylvester sketch is correctly labelled "checker's argument, not certified".

## Runner review
- **Self-contained and exact.** It imports only itertools, sys, time and sympy. It uses rationals, QQ rings, cyclotomic remainder and Gröbner over QQ. There are no floats.
- **Not tautological.** L1–L3, A-br, A1 (brackets in the ring compared with the cleared-denominator structure functions), A1-U, A3, P1–P3, P-hand, P4a, P4b, P5, G and P6 compute their left-hand sides from the models independently of the claimed formula.
- **Tautological parts found and fixed (runner edit R-E1).**
  - L4b computed `c0` with the very formula it compared to `lam_n - lam_m`.
  - A5-F compared `sum(w^(mr) d(r)) + sum d` with λ̂_m and checked `2 sum w^(-r) d(r)` against λ̂₋₁ − λ̂₁; that is the same symbol formula plus antisymmetry.
  - Both now compute the Fourier coefficient of C_z or H_z from the circulant matrix entries of the L4 Poisson form or the A5 structure functions, at z = 0 and 1. That also tests that the result sits at momentum m + n, and compares it with c̄ω^{(m+n)z}. The (S) and ratio parts are kept.
- **A5 (the position-space Dirac algebra)** is a linear recombination of the A1 structure functions at uniform m and n. It is a weak but legitimate check, not changed.
- **Disclosed post-hoc witness change.** Confirmed by R2 (above).

## Hygiene
- Front matter has the same fields as its siblings. The claim_id equals the lower-cased filename. The upstream dependency's claim_id is exactly the arc-lemma note's, and that note is tracked on this branch.
- Both link targets are tracked: the arc-lemma note (3 links) and `MINIMAL_AXIOMS_2026-06-29.md` (2 links).
- There are no links to PR #9702 material or to `.claude/` files. One plain-text, non-link `.claude/` path is in the Verification section, in the same style as the arc-lemma note.
- The runner path in the front matter exists.

## Edits (old → new)

**Note**
- **E1, claim_scope (L3).** "a local h needs a diagonal coefficient alpha (a banded non-diagonal alpha gives only a quasi-local h, not excluded)" → "h is local when C+ has the diagonal form C+_x = alpha_x(Pi+_x + h_x) with local alpha_x, h_x (solving C+ = alpha Pi+ + beta with a banded non-diagonal alpha generally gives only a quasi-local h = alpha^-1 beta, not excluded)".
- **E2, Status / Conditional.** "\"First class ⟺ local flat h\" needs a C⁺ that is locally solvable for Π⁺ with a diagonal coefficient." → "… is shown for a C⁺ that is locally solvable for Π⁺ with a diagonal coefficient, which makes h local."
- **E3, Answer (Model P).** "…at every L (hand proof), and also for the forward difference." → "…at every L (hand proof). The forward difference is also anomalous (an exact rational point at L = 5)."
- **E4, Answer (certificates).** "(central Δ, local germs at the ruler)" → "(central Δ, local germs at the ruler, the chiral quadratic translation-covariant ansatz with h(a ≡ 1, u = 0) ≠ 0)".
- **E5, L3 bullet.** "A *local* h needs a local, diagonal coefficient: C⁺_x = α_x(Π⁺_x + h_x)." → "A local, diagonal coefficient, C⁺_x = α_x(Π⁺_x + h_x), gives a *local* h."
- **E6, Reading / common zero.** "*Common zero (checker's argument, not certified).* … change by conjugation with M(Φ̄) … A translation-covariant M is then diagonal in momentum, so it rescales Λ_n by the uniform Fourier coefficient of M and leaves every ratio Λ_n/Λ₁ unchanged. …" → "*Common zero (checker's argument, with the rescaling corrected in this consolidation; not certified by the runner).* … transform with M(Φ̄), c̄′ = (M ⊗ M) c̄ M⁻¹, … At a common zero (every gauge flow vanishes at Φ̄) … a circulant, diagonal in momentum with eigenvalues μ̂_n ≠ 0, so c̄′(m, n) = μ̂_m μ̂_n c̄(m, n)/μ̂_{m+n}. Hence Λ′_n = μ̂₀Λ_n: M rescales Λ_n by its uniform Fourier coefficient μ̂₀ and leaves (S) and every ratio Λ_n/Λ₁ unchanged. (The checker's "leaves Λ_n unchanged" holds only for μ̂₀ = 1. A same-family reviewer checked the formula exactly at L = 6 for the forward difference; campaign history, not a repository source.) …"
- **E7, Theorem P proof step 3.** "Σ is a graph over the remaining variables, so it is regular," → "Near the witness (g^± ≠ 0), Σ is a graph over the remaining variables, so it is regular there,".
- **E8, Runner provenance.** Added the bullet "**Review edit (same family).** L4b and A5-F originally recomputed λ̂_n from the same formula they compared against … A sign-flipped expectation (Λ_n = −λ̂_n) now fails them. The check count is unchanged."
- **E9, Verification timings.** "(116 s and 132 s measured;" → "(116 s, 132 s and, after the review edit, 120 s measured;". Also "(608 s measured)" → "(608 s, 640 s and, after the review edit, 591 s measured)".

**Runner**
- **R-E1.** L4b's inner loop: `c0 = sum(w^(n r) v) - sum(w^(m r) v)` compared with `lam_n - lam_m` → the coefficient of C_z in {C_m, C_n}, computed from `circ(L, d)` matrix entries, `sum_y w^(mz+ny) D[z,y] - sum_x w^(mx+nz) D[z,x]`. It is compared with `(lam_n - lam_m) w^((m+n)z)` for z = 0, 1.
- **R-E1.** A5-F: the hand formula `c` and `c11` → coefficients from the matrix of the A5 structure functions, `sum_y w^(my) D[z,y] + w^(mz) sum_x D[x,z]` against `lam_m w^(mz)`, and `w^z sum_y w^(-y) D[z,y] + w^(-z) sum_x w^x D[x,z]` against `lam_-1 - lam_1`, for z = 0, 1. Non-vanishing of λ̂₋₁ − λ̂₁ is checked separately.

## Not changed, and why
- **Title.** "…first-classness is local zero curvature" is unconditioned in the title. The claim_scope, Status and Answer condition it (the diagonal-coefficient form, chiral C⁺). Renaming would change the claim_id and filename, and with them the graph, which is outside my scope. The supervisor may wish to consider "…is local zero curvature for a diagonal Kuchař form", but I do not think it is misleading given claim_scope.
- **"Every kink component is anomalous" / "never" at L = 4, 5 only.** It is conservative (the local rule is general-L), but correct as stated.
- **A5 position-space check.** It is weak (a linear recombination of already-checked structure functions) but honest. Left as is.
- **P4b's reliance on `sympy.solve` completeness.** Left in the runner, and cross-checked by R3 (radical membership by Gröbner) for (1,0) only; R3 (1,1) did not finish in 900 s.
- **Plain-text `.claude/` path in Verification.** It is not a link and follows the arc-lemma note's style. Left as is.
- **Slow numbers.** All match. Nothing changed beyond the timing.
