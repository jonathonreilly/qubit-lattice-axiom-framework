# REVIEW_FLOW_S6: hostile review of lane C session 6 (FLOW.md §41-§49 and the [RFL5-fix] edits)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f9*. This file is the only one I edited.
No commits, PRs or pushes.

Inputs (read-only, by offset):
- REVIEW_FLOW_S5.md (all).
- FLOW.md:
  - l.36-40 (normalisation, β_0^std);
  - l.155-186 (F-Π, F-id);
  - l.236-250 (the step functional and its Δ_FP);
  - l.760-841 (§18 with the RFL5 re-split);
  - l.1096-1108 (the covariant slice χ_{U_0} and Δ_FP);
  - l.1255-1268 ((a3));
  - all 19 `[RFL5-fix]` sites;
  - §36 (l.1731-1868);
  - §41-§49 (l.2052-2434) in full.
- FLOW_LOG.md, session-6 entries (l.216-251).
- checks: f9_criteria.md (all), f9_root_sector.py (I/O and structure), f9_out.txt, f9_time.txt. BSD `stat` of all four f9
  files; md5 of f9_root_sector.py = b8f8600f… (it matches FLOW_LOG).

Numerics:
- One NUMERIC LOCK acquisition, 05:39:27-05:39:43 UTC, released once with `rmdir` (no trap).
- Conditions at start: load 2.65, memory free 41%. nice 10, all BLAS threads = 1, PYTHONDONTWRITEBYTECODE=1, plain
  `python3` (no -I), no `timeout`.
- f9 was run unchanged from a scratchpad copy. Output is in
  `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revflow6/`.
- **The output is identical to checks/f9_out.txt, apart from the timestamp and timing lines.** 15.8 s, peak RSS 644 MB.
- No process was left running, and checks/ has no `__pycache__`.

Line numbers are FLOW.md lines as of this review.

---

## Bottom line

- **The [RFL5-fix] edits: all applied (19 tags, as claimed). One substantive leftover:** the redefined J_n (l.830-841)
  uses a propagator that is massless on Ran D_0. That is fine only if the longitudinal block is grouped with the ghosts
  inside the integrand, and this must be stated as part of the definition (fix S6-4).
- **Lemma S-all: CONFIRMED.** The bound γ_n = 1/(2ℓ⁵) is right (crude; the true gap is ~ℓ^{-2}). It holds at every
  background, independent of the torus, and also for Bloch-twisted fields.
- **Lemma GH: CONFIRMED as an identity for the δ-slice form of Γ^{W0}_n with S = S_0 and Δ_FP = det(Δ')^{1/2}.**
  - J^*J = 𝒮 (Dirichlet principle), S' = ker D_0^*, and Schur gives −½log det 𝒮 − ½log det Δ' = −½log det Δ_0.
  - **But the l.2129-2130 parenthetical is wrong in kind.** A U_0-dependent normalisation of the tower's fixing is not
    "(a3) bookkeeping". It has exactly the size of the ghost group. Dropping the U_0-dependence of Δ_FP = det(Δ')^{1/2}
    would cancel all of β[G_gh], i.e. remove the whole 1/22.
  - So the 1/22 + 21/22 split is valid only once (a3) ≡ 0 at critical backgrounds. That means proving that the tower's
    (h, P_resD^*) fixing with its Δ_FP is an exact FP representation of the G_res quotient (fix S6-1).
- **Lemma G-mag (i)-(v), Proposition GH-log: CONFIRMED.**
  - I re-derived the Poisson-tilt second moment (t²/3)j_1² line by line. c_g = 1/(96π²) is the continuum value.
  - The exact log ℓ comes from the scaling ℓ^{-4}g(qℓ²f) − g(qf).
  - **Normalisation and gauge verdict on 1/22: CORRECT AND CONSISTENT** (§4 below).
    - 1/22 is the share of the background-field Landau-type ghost, ½ of the real FP determinant (once complex per
      root).
    - This is the only IR-safe ghost grouping available here. The Feynman-type grouping (share 1/11) is not IR safe.
    - The share is a convention. Only the total is invariant.
- **Lemma MS, Lemma N-f, Corollary COV-GI-∞: CONFIRMED given (L-loc), with one binding gap.**
  - MS (iii) needs C² kernels (j ≤ 2), but (L-loc) (l.2278-2282) states only first derivatives. Strengthen to (L-loc2)
    (fix S6-2).
  - MS (iv) cites an extension of F-id that is not written out.
  - G-mag (vi) ARGUED: the plan is sound and f9 G2b is consistent, but it is correctly not counted.
- **Transverse group (§46): the required value 21/22 is right.**
  - (V-heat) is precisely stated, and f9 V2 is robust evidence. My refits over 13 window/order choices give R_∞ ∈
    [3.6657, 3.6715] against 11/3 = 3.66667, with a ≈ −1/3.
  - It is provable by a large-t Laplace/Duhamel argument, not by Seeley-DeWitt (§6).
  - (V-IR) is stated as a target, not yet as an operator inequality. It is the crux.
- **f9: CONFIRMED** (re-run byte-identical apart from timing lines; criteria predate the script; 24/24 PASS; both
  controls fail as required).
- **Corrected tally: 37 PROVEN-HERE (claimed 37), with scope annotations** (§8).

---

## 1. Priority 1: the [RFL5-fix] edits

| Fix | Where | Verdict |
|---|---|---|
| S5-1, (s2) → (s2⊥) | l.814-829 | APPLIED. The level-n ⊥ group is written as one group. The 𝒞-independent determinants are assigned to G_gh. |
| S5-1, UNIV re-split | l.830-841 | APPLIED as a binding paragraph. The proof text at l.825-829 is still the old split, so read it with the paragraph. **Leftover:** C_n := (O^♯_n)^{-1} is massless on Ran D_0 (O^♯ = Δ_0 there). The IR grouping (½log det O^♯ − ½log det'Δ_0 together; G_gh exact and outside J_n) must be part of the definition of J_n, not a remark. See fix S6-4. |
| S5-1, J_n redefined | l.835-839 | APPLIED (O^♯_n, Π-vertices). See the previous row. |
| S5-1, 𝒰_n qualifiers | l.1469, l.1663 | APPLIED. |
| S5-1, "+ const" | l.1554-1556 | APPLIED and reconciled correctly. |
| S5-2, (S) at every background | l.1749-1750, §42 | APPLIED, and proven (Lemma S-all). |
| S5-2, (N) at U_f | l.1754-1756 | APPLIED. It now points to Lemma N-f, given (L-loc). |
| S5-2, F-id cited | l.1848-1850 | APPLIED. The "extension via F-Π (ii)" is cited, not written (fix S6-3). |
| S5-2, (COV-GI-∞) recorded | l.1851-1853, l.2026, l.2042 | APPLIED. |
| S5-2/S5-5, IR caution | l.1854-1855, l.1956 | APPLIED. |
| S5-3, all four | l.1761, l.1790, l.1862, l.1928 | APPLIED. |
| S5-4 | l.1975, l.1980, l.1992, l.1998 | APPLIED, wording as asked. |
| S5-5, §37 scope + (R1)-(R4) | l.1950-1959 | APPLIED. |

Tag count: 19 in-text lines, which matches l.2395.

## 2. Priority 2: Lemma S-all (§42, l.2101-2117)

**(i) CONFIRMED.** ⟨X, D_0ρ⟩ = ⟨D_0^*X, ρ⟩ sums only over the support of ρ. The range D_0Λ' is closed by (ii), so the
orthogonal sum holds in infinite volume too.

**(ii) CONFIRMED.**
- Kato: Ad is isometric, so |(D_0ρ)_b| ≥ ||ρ(x)| − |ρ(x+μ)||.
- For odd ℓ the blocks c + {−h_n..h_n}⁴ tile Z⁴ and every torus of side ∈ ℓZ.
- The axial path has length ≤ 4h_n = 2(ℓ−1) < 2ℓ.
- Each edge lies on at most ℓ⁴ paths, so ||u||² ≤ 2ℓ⁵||du||².
- Nothing depends on U_0 or T. Twisted fields are covered, because |ρ| is periodic.
- The constant is crude: the true Dirichlet gap is ~ℓ^{-2}. That is harmless at fixed n.

**(iii) CONFIRMED.**

**Consequence (Jμ = P_{S_0}D_0λ = D_0λ^har_μ): CONFIRMED.**

## 3. Priority 3: Lemma GH (§43, l.2119-2160)

### 3.1 Line-by-line check

- **(i) CONFIRMED.**
  - ||Jμ||² = min_ρ||D_0(λ_μ − ρ)||² = ⟨μ, 𝒮μ⟩.
  - ker 𝒮 = K_0 uses (N) and HJ = 0 exactly as written.
- **(ii) CONFIRMED.** S_0 ∩ D_0Λ is the set of harmonic extensions. D_0Λ = D_0Λ' ⊕ J(Λ_n) orthogonally, so
  S' = (D_0Λ)^⊥ = ker D_0^*.
- **(iii) CONFIRMED as mathematics.**
  - The Gram matrix of (s, ρ) ↦ s + D_0ρ is diag(1, Δ').
  - Δ_FP = det(Δ')^{1/2} in the "Lebesgue on S" normalisation. It equals the δ(E'D_0^*X)·det Δ' convention:
    ∫δ(Δ'ρ)det(Δ')^{1/2}dρ·det Δ' = det(Δ')^{1/2}.
  - The quotient ∫_E/∫_{Λ'} is formal (Q is degenerate on D_0Λ'). It is well defined as the slice integral, which is
    how it is used.
- **(iii), the parenthetical (l.2129-2130): WRONG IN KIND (fix S6-1).**
  - "Every exact FP representation gives the same number" is true, up to U_0-independent constants (for a soft
    't Hooft averaging the normalisation is (2π)^{rank/2}).
  - But "a legitimate fixing differs … by its own U_0-dependent normalisation, which is (a3) bookkeeping" contradicts
    the first clause. It also understates the stakes.
  - Example: a fixing that used Δ_FP(1) instead of Δ_FP(U_0) would add +½log det Δ'(U_f). Δ' is the Dirichlet covariant
    Laplacian on blocks of side ℓ, so its f² coefficient per complex root is ≈ +2c_gq_α²log ℓ + O(1). That cancels
    β[G_gh] entirely.
  - So **(a3) is not bookkeeping. It must be exactly 0 at the critical backgrounds β needs.**
  - The natural proof is short. The tower integrand is G_res-invariant (𝔪_n(U^g) = 𝔪_n(U), Wilson gauge invariant, the
    𝒩' factors depend on composites only). The tower's (h, P_resD^*) fixing with its Δ_FP (l.1100-1103) is then an exact
    FP insertion, so the one-loop quotient is slice-independent.
  - Until that is written, the 1/22 and 21/22 statements are conditional on it. After it, (a3) as defined at
    l.785/l.1262 (against BF-Feynman J_*) is superseded and should be retired, not left "unchanged" (l.2353).
- **(iv) CONFIRMED.**
  - COV-GI (iii) with S = S_0, plus (i)-(iii).
  - (minor) det Δ_0 = det Δ'·det 𝒮 holds whether or not Δ_0 is invertible, since Δ' is invertible. Invertibility is
    needed only for K_0 = 0 and Λ_n^♮ = Λ_n.
- **(v) CONFIRMED.**
  - On Ran D_0, D_0D_0^* is unitarily equivalent to Δ_0 on (ker D_0)^⊥.
  - (H + M^TΠM) kills Ran D_0 at critical U_0.
  - **IR note:** O^♯ is massless on Ran D_0. Only ½log det O^♯ − ½log det'Δ_0 is an IR-safe unit, which is relevant to
    the J_n redefinition (fix S6-4).

### 3.2 Is the regrouping IR safe? (S6-1 "DONE")

- **G_gh:** IR safe, given (vi). Without (vi), limit points lie within 2q²sup|c'| (GH-log (b)).
- **G_⊥'s fine term ½log det_{ker D_0^*}(H + M^TΠM):** IR safe **directly**. This is better than FLOW's "because the
  total is C²" argument (l.2240):
  - in an orthonormal basis of S_0, the Schur complement onto S' of an operator ≥ λ_min(A) is itself ≥ λ_min(A);
  - by Lemma N-f, λ_min(A) ≥ c_n/2;
  - so this term is the density of a gapped covariant operator, C² by Lemma MS.
- **G_⊥'s level-n group ½log det_⊥(P_⊥𝒞_nP_⊥) = ½log det 𝒞_n − ½log det 𝒞^♭_G:**
  - 𝒞^♭_G is gapped (≥ λ_min 𝒞), but it is compressed to the non-local subspace G = Ran D(B). So its density is not of
    MS type.
  - IR safety is plausible: D^*𝒞^{-1}D = c·D^*D + higher order, with a B_4-scalar 𝒞^{-1}(0). But it is not proven.
  - (s2⊥) at l.818-820 needs it. Record it as part of (s2⊥).
- "G_⊥ := left − G_gh" (l.2318) is a definition. The content of COV-GI-∞ for G_⊥ is that the explicit formula holds on the
  dense flux set. The wording at l.2240 and l.2403 should say this.

## 4. Priority 4: Lemma G-mag, Proposition GH-log, and the 1/22 normalisation/gauge verdict

### 4.1 G-mag (i)-(v): CONFIRMED

- **(i).** Feynman-Kac with total jump rate 8. hol(ω) = e^{iφA} by lattice Stokes. The expectation is real by reflection.
- **(ii).** Frullani with ε-regularisation. The integrand is O(t^{-3}) at ∞ and O(φ²t³) at 0.
- **(iii).** I re-derived it independently.
  - E^θ[A] = 2i sin θX_1 and Var^θA = 2cos θX_2.
  - ∫(dθ/2π)e^{−2t(1−cos θ)}sin²θ = j_1/(2t), which gives 2j_1(X_2 − X_1²/t).
  - E^ψ[X_2] = cos ψt² − (4/3)sin²ψt³ and E^ψ[X_1²] = −sin²ψt⁴ + (2/3)cos ψt³, hence (t²/3)(cos ψ − t sin²ψ).
  - Integrating gives (t²/6)j_1, and the product is (t²/3)j_1².
  - Continuum check: for a planar bridge with variance 2 per unit time per coordinate, E[A²] = 4·t²/12 = t²/3.
  - f9 G1 agrees to ≤ 6.1e-8 (finite differences, independent of the tilt).
- **(iv).** Plausible and sufficient as written. The bridge density on [0, t/2] is ≤ 2 against the free walk, plus Doob
  and time reversal.
- **(v).**
  - The split at t_1 = 1/|φ| is correct. The quartic remainder is Cφ⁴(1 + t_1²) = O(φ²), and the tail is O(φ²).
  - m(t) → 1/(48π²), so ψ = (1/(96π²))log(1/φ) + O(1).
  - This matches the continuum: (16π²t²)^{-1}(Bt/sinh Bt) has B²t² coefficient −1/6, so c_g = (1/6)/(16π²).
  - S6-F2 does not occur.
- **(vi) ARGUED, correctly not counted.** The martingale-CLT plan for (x/√t, y/√t, A/t) is the right one. f9 G2b
  increments halve (ratio → 0.51), consistent with c' = c'_0 + O(φ).

### 4.2 Lemma B-flux: CONFIRMED, minor wording fix (fix S6-5)

- Translation and B_4 reflection covariance kill the other planes.
- At linear order, F_n = ℓ²f exactly. The x dy integral is additive over segments, and translated legs give L·Δy = L²
  per step, as in (C2).
- **For N ≥ 3:** the Cartan-sector average acts entrywise on diagonal phases, so B_n's flux is diag(F_n(h_if)) (plus a
  common determinant phase), not F_n(f)H_1, beyond linear order. A root then sees q_αℓ²f + O(f³).
- This is all that GH-log (a) uses. State it per root, as F_{n,α}(f) = q_αℓ²f + O_n(f³).

### 4.3 Proposition GH-log: CONFIRMED

- **(a).** −g(qf) contributes −c_gq²f²log(1/qf), and ℓ^{-4}g(qℓ²f) contributes +c_gq²f²[log(1/qf) − 2log ℓ]. The sum is
  −2c_gq²log ℓ·f².
  - Sign: this is antiscreening, the same sign as the total −β_0^std log ℓ, as the ghost must be.
  - The O_n(f²log) remainder uses ψ' = O(1/φ) times F_n − ℓ²f = O(f³). ✓
- **(b), (c), (e).** CONFIRMED.
- **(d) arithmetic.** 2·(1/48π²)/(11/12π²) = 1/22. ✓
- **Observation (useful, not in FLOW).** UNIV is an O(1)-remainder statement, so for UNIV itself (b) is enough. (vi) is
  needed only for "exactly, no remainder", for the existence of c^⊥_n as a limit, and for the rate statements.

### 4.4 The normalisation and gauge verdict on 1/22 (the priority question)

**Normalisation: consistent end to end.** I checked it independently.
- u = 2N/g_std². With U_p = exp(H_1φ) and (1/N)Σh_i² = 1, Wilson gives uφ²/2 per plaquette, and the continuum
  (1/g²)Σ_{μ<ν}(−tr F²) gives (1/g²)Nφ². So u = 2N/g² ✓, and Δu = 2 × the f² coefficient (consistent with F-id).
- Σ_{α>0}α(H_1)² = ½tr_adj(−ad_{H_1}²) = N·(−tr_F H_1²) = N². ✓
- Per complex root, the one-loop f² coefficient over the scale range ℓ is −R_tot·(2log ℓ)/(16π²)·q_α², with R_tot = 11/3.
  Summing over roots: −(11N²/(24π²))log ℓ, so Δu = −11N²/(12π²)·log ℓ = −β_0^std log ℓ. In standard units this is
  Δ(1/g²) = −2b_0 log ℓ.
- So c_g, Σq² = N² and β_0^std = 11N²/(12π²) are mutually consistent.

**Gauge: the 1/22 matches the grouping actually used.**
- Continuum, per complex root, with heat-trace B²t² coefficients: vector R_V = 10/3 (spin +4, orbital 4·(−1/6)) and
  scalar R_S = −1/6.
- **Background-field Feynman bookkeeping:** Γ = log det_C V − 2 log det_C(−D²), i.e. R_V − 2R_S = 10/3 + 1/3 = 11/3.
  - The ghost share is (1/3)/(11/3) = **1/11**.
  - The folklore "−1/3" is the diamagnetic total, vector orbital −2/3 plus ghost +1/3. It is not the ghost alone.
- **Background-field Landau / orthogonal (δ(D^*a)) bookkeeping:** the δ-function Jacobian det(D^*D)^{-1/2}·det(D^*D)^{+1}
  leaves a net ghost of −½log det_R(D^*D) = −log det_C, so −R_S = +1/6.
  - The transverse part is ½log det_⊥V = ½log det V − ½log det Δ, i.e. R_V − R_S = 7/2.
  - The ghost share is (1/6)/(11/3) = **1/22**, and 7/2 = 21/22 of the total.
- **The lattice G_gh is exactly Landau-type.**
  - Its fine piece is −½log det_R(D_0^*D_0), once complex per root.
  - G_⊥'s fine piece is the operator on ker D_0^* (Landau transverse; in Feynman form, ½log det O^♯ − ½log det'Δ_0,
    i.e. R_12 + R_S = R_V − R_S).
  - So the 1/22 claimed for G_gh and the 21/22 required of G_⊥ are in the same convention, and they add to the
    invariant total.
- **The soft-kernel (Feynman-type) residual slice does not enter.**
  - Lemma GH replaces it by the exact quotient (S_0 Jacobian).
  - That is legitimate only after fix S6-1 ((a3) ≡ 0). If the tower's fixing carried a U_0-dependent normalisation
    mismatch, the shares would move by O(1/22).
- **The Feynman grouping could not be used instead.** It would give "ghost" = ½log det D_n^*D_n − log det D_0^*D_0, with
  f²log(1/f) coefficient c_gq²(1 − 2) ≠ 0. It is not IR safe, so 1/11 never appears as an IR-safe group in this
  construction. The Landau split is forced by IR safety.
- **What to change in the text:** §44 Reading (1) should say "background-field Landau-type (orthogonal-slice)
  bookkeeping; in BF-Feynman bookkeeping the ghost share is 1/11. Only the total is invariant" (fix S6-5).

## 5. Priority 5: Lemma MS, (L-loc), Lemma N-f, Corollary COV-GI-∞

- **MS (i)-(ii): CONFIRMED.** The cocycle composition is right. Combes-Thomas is uniform in f because the phases have
  modulus 1.
- **MS (iii): CONFIRMED as a lemma**, under its own hypothesis |∂_f^jκ_f| ≤ C_Ke^{−m|γ|} for j ≤ 2.
- **MS (iv): CONFIRMED in structure.**
  - Normalised exponential coordinates make U_f = exp(fH_1a^sym) exact, so there is no second-order chart term.
  - The origin-cell trace of log K(U) is gauge invariant, so ρ_0 is a legitimate density.
  - But "F-id, extended to exponentially decaying Hessian kernels by F-Π (ii)" is cited, not proved. F-id's proof uses a
    finite-range Poincaré lemma. The extension needs a moment bound Σ|z|²|Π(z)| < ∞ and a limiting argument (a few
    lines). Write it (fix S6-3).
- **(L-loc): ARGUED, and too weak for its use (fix S6-2).**
  - COV-GI-∞ applies MS (iii) to Ã(U_f), 𝒞_n(U_f) and Δ'(U_f). In the symmetric gauge, ∂_f²κ_f involves second link
    derivatives ∂_c∂_{c'}Ã weighted by a^sym_c·a^sym_{c'}.
  - (L-loc) bounds only the first derivatives.
  - Required: (L-loc2), i.e. (L-loc) plus |∂_c∂_{c'}Ã(U)(b, b')| ≤ C_ne^{−m_n(d(b,c)+d(c,c')+d(c',b'))} on 𝒦_n, and the same for
    𝒞_n.
  - The argument offered for (L-loc) (finite range plus analyticity on 𝒦_n plus Combes-Thomas for 𝒞_n^{-1}) gives this
    equally, so this is a statement fix, not a new obstacle.
- **Lemma N-f: CONFIRMED given (L-loc).**
  - (i) Block diagonality at critical U holds. D_UE'D_U^* on D_UΛ' is similar to Δ' (TV = VΔ'), hence ≥ γ_n.
  - (ii) The Bloch fibres over ℓZ⁴ carry one level-n site per cell. A twisted d_nμ = 0 forces μ = 0, and twisted
    harmonic 1-forms vanish. Compactness gives c_n > 0.
  - (iii) IMS with E_IMS = O(R^{-2}). The ball comparison through U^{(s)} = exp(sfH_1a^{sym,c_j}) ∈ 𝒦_n gives
    C_2|f|(R + 1). R = |f|^{-1/3} gives c_n − C'|f|^{2/3}.
  - The window ε_n is n-dependent. That is harmless for β at fixed n, as FLOW says.
- **Corollary COV-GI-∞: CONFIRMED given (L-loc2) (not (L-loc)) and (vi).**
  - The magnetic Bloch decomposition at q_αℓ²f ∈ 2πQ is fine.
  - The identity ½log det_{S_0}A − log Δ_FP = ½log det Ã − log det Δ' holds (TV = VΔ' gives det = det Δ').
  - The Nielsen-Olesen remark (l.2326-2328) is consistent with Lemma N-f.
- **G-mag (vi) (the area invariance principle): ARGUED, correctly uncounted.**
  - The plan is standard. It still needs the bridge-conditioning step written out: the absolute continuity on
    [0, (1−δ)t] plus the O(δ) last-segment estimate from (iv).
  - Note that (vi) is not needed for UNIV's O(1) bound (§4.3).

## 6. Priority 6: the transverse group G_⊥ and f9 V2

**Required value (l.2332-2340): CORRECT.**
- c^⊥_n = −(21N²/(48π²))log ℓ + O(1), i.e. per complex root −(7/2)(2log ℓ)/(16π²)q².
- R_12 = 2(−1/6) + 4 = 11/3, R_V = R_12 + 2R_S = 10/3, R_12 + R_S = 7/2.
- The 34-components are scalars; f9 V0e checks this to 8.9e-16.

**Precision of the remaining inputs:**

| Input | Precisely stated? | Comment |
|---|---|---|
| (V-heat) | YES | An explicit operator, an explicit limit 11/3, and an O(1/t) rate. |
| (V-IR) | As a target, yes | "|c^⊥_{n,α} + (q²/16π²)∫_1^{ℓ²}(R_12+R_S)dt/t| ≤ A, uniformly in n". As a mechanism, no: "a proper-time cutoff at t ≈ ℓ²" is heuristic. There is no operator inequality for the IR term M^TΠM or for the level-n ⊥ group. It is the crux (it subsumes (R1), (R2), (R3) on G_⊥, and (a2), (a4')). |
| (R1), (R2) | Only by reference to REVIEW_FLOW_S5 §3.3 | FLOW should state them on the root-sector maps T_k(B), with the O(F_k) form claimed. |
| (a3) | **NO; obsolete** | After Lemma GH it should be the statement "(a3) ≡ 0 at critical backgrounds" (exact FP of the tower slice). See fix S6-1. |
| (b), (s1) | Unchanged | Root-sector versions not written. |
| (s2⊥) | Stated (l.818-820) | Missing: IR safety of the level-n ⊥ group in the root sectors (§3.2). |

**f9 V2 extrapolation: robust.**
- The data are 3.4742 … 3.6527 at t = 2 … 24, monotone.
- I refitted the printed 4-digit values with R_∞ + Σ_{j=1}^{k−1}a_j t^{-j}, k = 2, 3, 4, on five windows (t ≥ 3, 4-16, ≥ 6,
  ≥ 8, all). R_∞ ∈ [3.6657, 3.6715] in every case, with a_1 ∈ [−0.39, −0.31], clustering at −1/3.
- The pre-stated competitors 10/3 and 7/2 are excluded by more than 40 times the spread.
- At t = 24 the fit predicts 11/3 − 0.332/24 = 3.6529, against 3.6527 observed.
- **Reading:** strong evidence for (V-heat), and specifically for the lattice spin term. It is not a proof, and it tests
  nothing in (V-IR), as FLOW says (l.2389).

**Is (V-heat) provable by a "lattice Seeley-DeWitt expansion"? Not in that form, but it is provable.**
- Seeley-DeWitt is the small-t (UV) expansion. On the lattice, small t is trivial: the heat trace is entire in t.
- The needed statement is the large-t asymptotic of the f² coefficient. That is an IR/Laplace-method statement.
- Two routes:
  - **(1) Duhamel.** The f² coefficient is an exact BZ integral of trigonometric symbols with e^{−tω(q)} weights. By
    Laplace's method, the large-t limit is fixed by the q → 0 Taylor data of the lattice vertices.
    - Gauge covariance fixes the leading terms: K_F = −D² − 2iqF + (dimension ≥ 6).
    - So R_12^lat → 11/3, with O(1/t) corrections from the dimension-6 terms.
  - **(2) The G-mag tilt with a 2×2 spin-matrix weight on the walk.** This probably gives a closed form in j_0, j_1, j_2,
    which would also explain a = −1/3.
- Estimate: session scale [s]. Route (2) is preferred because it is exact.

## 7. Priority 7: f9 provenance and re-run

| File | Born (UTC) | Size |
|---|---|---|
| f9_criteria.md | 05:27:55 | 6649 |
| f9_root_sector.py | 05:31:45 (md5 b8f8600f…) | 21808 |
| f9_out.txt | 05:32:23 (last modified 05:32:39) | 5397 |
| f9_time.txt | 05:32:44 | 231 |

- The criteria predate the script. The FLOW_LOG stat line was first printed in local time (EDT) and then corrected to UTC.
  That is honest and consistent with BSD stat.
- §42-§46 were written 05:18-05:27, before the criteria. The 05:26 rewrite is logged.
- The smoke test was at reduced size; the script was not changed after it.
- **Re-run:** byte-identical apart from the timing and timestamp lines; 24/24 PASS; both controls fail.
- **Tolerances:**
  - V2a's 2% is loose but discriminating: 7/2 is 4.5% away and 10/3 is 9%.
  - G3a's 2% at Q' = 64 passes at 0.46%, decreasing like φ.
  - G3b (ℓ = 9) is correctly informational.
- **What f9 does not test, as FLOW states:** (V-IR), the actual S4' maps, (L-loc), and (a3).

## 8. Per-item verdicts and corrected tally

| Item | Verdict | Fix |
|---|---|---|
| [RFL5-fix] S5-1..S5-5 (19 tags) | APPLIED; J_n IR grouping leftover | S6-4 |
| Lemma S-all | **CONFIRMED** | — |
| Lemma GH (i)-(v) | **CONFIRMED** (δ-slice S_0 form) | S6-1 (the (iii) parenthetical; (a3) ≡ 0) |
| Lemma B-flux | **CONFIRMED** (per-root wording for N ≥ 3) | S6-5 |
| Lemma G-mag (i)-(v) | **CONFIRMED** ((iii) re-derived independently) | — |
| G-mag (vi) | ARGUED; not counted (correct) | — |
| Prop. GH-log (a), (b), (e); (c), (d) given (vi) | **CONFIRMED**; 1/22 normalisation and gauge consistent (Landau-type) | S6-5 (convention sentence) |
| Lemma MS (i)-(iii); (iv) | CONFIRMED; (iv) uses an unwritten F-id extension | S6-3 |
| (L-loc) | ARGUED; too weak (first derivatives only) for MS (iii) | S6-2 |
| Lemma N-f | **CONFIRMED** given (L-loc) | — |
| Corollary COV-GI-∞ | **CONFIRMED** given (L-loc2), (vi) | S6-2 |
| §43/§44 "G_⊥ IR safe because total C²" | TRUE but circular-sounding; the fine term is directly gapped; the level-n ⊥ group is unproven | S6-4 |
| §46 required value 21/22, (V-heat) statement | **CORRECT** | — |
| (V-IR) | Target precise; mechanism heuristic; OPEN, the crux | S6-6 |
| f9 (re-run identical) | **CONFIRMED** | — |

**Corrected tally: 37 PROVEN-HERE (claimed 37).** That is 29 + 8 (S-all; GH; B-flux; G-mag (i)-(v); GH-log; MS; N-f;
COV-GI-∞), with these scope annotations:
- **GH:** an identity for the δ-slice S_0 form of Γ^{W0}_n. Its use for the tower needs (a3) ≡ 0 (exact FP), OPEN [s].
- **GH-log (c), (d):** given (vi). (a), (b), (e) are unconditional.
- **MS (iv):** given the F-id extension, which is not written [s].
- **N-f:** given (L-loc).
- **COV-GI-∞:** given (L-loc2) and (vi).

**Unchanged:**
- GAP: UNIV-rate.
- WRONG and superseded: as listed at l.2426-2427.
- IMPORTED-AND-REVERIFIED: L4b.

**New OPEN items:**
- (a3) ≡ 0 (exact FP of the tower slice) [s]; it carries a potential ±1/22.
- (L-loc2) [s].
- IR safety of the root-sector level-n ⊥ group [s-P].

## 9. Binding fixes for the next lane-C session

1. **S6-1 ((a3) and the slice).**
   - Delete the parenthetical at l.2129-2130 ("differs … by its own U_0-dependent normalisation, which is (a3)
     bookkeeping"). Replace it with: "a U_0-dependent normalisation mismatch would shift β by O(β[G_gh]); the identity is
     used only for the exact quotient."
   - Prove that the tower's fixing (h, P_resD^*) with Δ_FP(U_0) (l.1100-1103) is an exact FP representation of the
     G_res-invariant integral. Then (a3) ≡ 0 at critical backgrounds.
   - Retire the old (a3) (l.785, l.1262) and l.2353's "unchanged".
   - Until this is done, write "given (a3) ≡ 0" on the 1/22 and 21/22 statements (l.2228, l.2336, l.2408-2413).
2. **S6-2.**
   - Restate (L-loc) as (L-loc2), with second link derivatives and the same for 𝒞_n.
   - Cite (L-loc2) in Corollary COV-GI-∞ (l.2310) and §48-§49.
3. **S6-3.** Write the extension of Lemma F-id to exponentially decaying Hessian kernels (moment bound plus truncation
   limit) that MS (iv) and §36 Reading (b) cite.
4. **S6-4 (IR grouping in J_n and G_⊥).**
   - In the J_n redefinition (l.835-839), take G_gh out of J_n (it is computed exactly). Define J_n^⊥ from G_⊥ only, with
     ½log det O^♯ − ½log det'Δ_0 kept as one unit, since O^♯ is massless on Ran D_0. Then B_n = −β[G_⊥] − β[G_gh]
     exactly.
   - Replace "G_⊥ IR safe because the total is C²" (l.2240, l.2403) with: the fine term is a gapped covariant density (the
     Schur complement is ≥ λ_min(A) ≥ c_n/2); the level-n ⊥ group's IR safety is OPEN and part of (s2⊥).
   - Fix the old UNIV proof text (l.825-829), or mark it as superseded by l.830.
5. **S6-5 (wording).**
   - In §44 Reading (1), add: "background-field Landau-type (orthogonal-slice) bookkeeping; in BF-Feynman bookkeeping the
     ghost share is 1/11, and that grouping is not IR safe here; only the total is invariant."
   - Lemma B-flux: state per root, F_{n,α}(f) = q_αℓ²f + O_n(f³), since for N ≥ 3 the higher orders are not along H_1.
   - Add after GH-log: "(b) suffices for UNIV's O(1) remainder; (vi) is needed only for exactness and the rate."
6. **S6-6.**
   - State (R1) and (R2) in FLOW on the root-sector maps T_k(B).
   - Restate (V-IR) as an operator-level statement on G_⊥: a bound on the f² coefficient of ½log det_{ker D_0^*}(H + M^TΠM) +
     ½log det_⊥(P_⊥𝒞_nP_⊥) against ½log det_{ker D_0^*}(K_F) with a proper-time cutoff, with an n-independent error.

## 10. Next target

1. **(V-heat), exactly.** Use the G-mag tilt with a spin-matrix weight on the walk. Target: a closed form of
   R_12^lat(t) in Bessel ratios, → 11/3 with a_1 = −1/3. This is session scale and closes S6-F5 for good.
2. **S6-1, S6-2, S6-3** (short, but load-bearing for the 1/22).
3. **(V-IR) in a solvable model first.** Take a charged scalar (one root, U(1) charge q) in a constant field with the
   actual S4' root-sector averaging and IR term at n = 1, 2. Prove, or test, that the f² coefficient of the scalar analogue
   of G_⊥ equals −(q²/16π²)∫_1^{ℓ²}R_S^lat dt/t + O(1), uniformly in n.
   - Since the scalar heat trace is exact (G-mag (iii)), this isolates the IR-term/level-⊥ mechanism of (V-IR) from the
     spin term.
   - Suggested check f10: criteria first; 2D and 4D Bloch at rational flux; n = 1, 2.
