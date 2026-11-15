# REVIEW_FLOW_S3: hostile review of lane C session 3 (FLOW.md §22-§28 and the [RFL-fix] edits)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f6_*. The only file I edited is this one.
No commits, PRs or pushes.

Inputs (read-only, by offset):
- FLOW.md: §0 (l.20-41), §3.1 (l.112-135), §4 (l.186-228), §5.5 (l.301-318), §6 (l.384-406), §16-§18 (l.640-800),
  §21 (l.918-936), and §22-§28 (l.937-1296) in full.
- FLOW_LOG.md, all of it.
- REVIEW_FLOW_S1_S2.md: format, the fix list (l.420-460), FT-1/FN-1/FR-2 texts, and the tally (l.400-421).
- RLARGE.md v2: header and §0 (l.1-40, l.94-104, l.166-178), §8 K1/K4 (l.555-582).
- RLARGE_INTEGRATION_LOG.md l.40-64.
- HIST.md: (3.1) (l.152-162), Proposition CL^J (l.188-262), R1^J (l.290-345), H-pos^J (l.345-360), the ledger (l.767). I also
  grepped every `g_{k+1}` occurrence.
- checks: f6_criteria.md, f6_out.txt, f6_time.txt; f6_iter_chain.py (grep only). BSD `stat` (TZ=UTC) of the f6 files.

Numerics (NUMERIC LOCK acquired and released once, nice 10, 1 thread): one independent brute-force check of the f6
composite-covariance term (§6.3). Script and output are in the scratchpad `revflow3/`. f6 itself was NOT re-run
(2170 s), and ℓ = 21 was NOT run.

Line numbers are FLOW.md lines as of this review.

---

## Bottom line

- **The [RFL-fix] edits are substantially correct. Two items are only partly applied:**
  - FN-1: two stale PROOF pointers are left.
  - The new claim "Theorem UNIV is conditional on (U-IR) alone" (l.1082, l.1281) contradicts FT-1. The session's own
    tally (l.1291-1295) and the §21 note (l.921-925) still need (SF-bg) at orders 3 and 4.
- **The provenance correction CK-1 is honest.** It reports the contradicting filesystem facts against its own earlier
  log, and it downgrades f1 to NOT VERIFIABLE. The f6 provenance checks out: the criteria file was born 01:18:41 with
  birth = mtime; the script was born 01:29:04 and last modified 01:35:39; the run started at 02:08:25.
- **K1 is right.** I re-derived it in FLOW's conventions. The shift changes u_{k+1} by −δβ_k (it lowers u when δβ_k > 0),
  and no bound changes.
- **Lemma F-mono has an index error (WRONG as stated in one clause).** The polynomial clause g_k^{-p} ≤ (g_{k+1}^{-2} + R)^{p/2}
  has its indices swapped. It is also the wrong direction for HIST: two of HIST's four uses need g_{k+1}^{-p} in terms of
  g_k^{-p}. The exponential clause, part (i) and the threshold remark are right.
- **Lemma U-loc' is correct at each n, and that is enough for Corollary U-red.** Corollary U-red is an exact per-n
  identity, and no m_n-dependent constant enters any later bound. Uniformity is needed only inside (U-IR), which is
  stated separately.
- **§24 is correct.** Lemma U-T⊥, Lemma DIR, Lemma H-sym, Lemma U-cov-IR' and Proposition U-a1⊥ all check:
  - one factor ℓ per derivative;
  - the bound ℓ^{-4+|α|}|q|^{-6};
  - every alias sum and power of ℓ.

  Two caveats:
  - U-T⊥'s "on every torus" fails at the q = 0 alias.
  - (a1)-longitudinal and (a4) overlap.
- **f6 shows no extra log, and this is now an analytic fact.** In f6's scalar chain the composite-covariance term is
  block-diagonal. It equals **c^cov(L_2) = −(L_2² − 1)²/(576 L_2⁴(L_2² + 1))**:
  - That is −1.3717e-4 at L_2 = 3 and −6.1538e-5 at L_2 = 5, matching f6 to every printed digit.
  - I confirmed it by an independent brute-force path sum (§6.3).
  - It decays like L_2^{-2}, so it contributes nothing to the log coefficient.
  - The failing slope +0.0701 × 1/(48π²) is the finite-difference slope of this rational function.

  But the pre-registered (G6') would also FAIL at ℓ = 21: the exact slope over (15, 21) is ≈ 0.040 > 0.005. The test
  would then have *declared S3-F4 observed*, a false positive. So **do not run ℓ = 21 as pre-registered.**
- **Corrected tally: 24 PROVEN-HERE (claimed 26).** U-res' is a one-line remark on U-res, and F-mono is arithmetic on
  F-flow. Neither is a separate item under this lane's own convention (F-ll and F-R are counted with their parents), and
  F-mono also needs a fix.

---

## 1. Priority 1: the [RFL-fix] edits and the provenance correction

| Fix | Where | Verdict |
|---|---|---|
| FS-1 | l.318 | APPLIED. |
| FI-1, FI-2 (B6) | l.212-221, l.456, l.467 | APPLIED. The requantified (RLF-δ)_k is now consumed. RLARGE v2 l.172-174 carries the matching (RLF-δ)_k item. |
| UC-1 | l.733-734, l.750-755 | APPLIED. The parenthetical is withdrawn. |
| J_n definition; (a1)-(a4) split | l.756-773 | APPLIED. **Residual, see fix S3-6:** l.772-773 still demands the POINTWISE bound \|J^{(a_i)}_n\| ≤ A_iℓ^{-2}\|q\|^{-6}, while §24.3 (l.1162-1166) restates (U-IR)(a) in integrated form. Annotate l.772. |
| (U-IR-s) | l.777-785 | APPLIED. (s2) is separate. |
| UP-1, UP-2 | l.658-661, l.739-742 | APPLIED. |
| FT-1 | l.312-317, l.921-925 | APPLIED, but **contradicted by session-3 text**: see fix S3-1. |
| FR-1 | l.295 | APPLIED. |
| FRR-1, FRR-2, RN-1, RN-2 | l.820, l.837, l.847-848, l.862-866, l.907-910, l.465 | APPLIED. The PLD-fin row is added, RLARGE §7.2 (iv) is named, and the (P2) row uses β_+. |
| UT-1, UT-2 | l.705, l.712 | APPLIED. |
| FR-2 | l.199-211, l.391, l.403-405 | APPLIED. It was first applied in the wrong direction, then corrected and the error disclosed. See §2. |
| CK-1 | FLOW_LOG l.45-63, FLOW l.496 | APPLIED, and honest (see below). |
| CK-2, UR-1, UR-2 | l.883, l.815, l.817, l.890 | APPLIED. |
| **FN-1** | l.39-41 | **PARTLY APPLIED.** l.41 corrects the "l.4089" pointer only. **l.577 still cites "PROOF l.4106-4109"** (now l.4114-4116), **the §19A row at l.850 still cites "l.4091-4102"** (now l.4103-4106), and l.566 cites L4b as l.1159-1170 (the review gave l.1162-1174). §27 (l.1263-1270) says "every binding fix … applied". That is overstated for FN-1. |
| normalisation wording; §3.1 per HIST Lemma HF | l.39-40, l.123-135 | APPLIED. The HF bookkeeping (d(M) = O(y⁶), so no derivative of order ≤ 5 at 1 changes) is consistent with HIST §14.2 as quoted. |

**Provenance (CK-1 and f6).**
- The CK-1 entry (FLOW_LOG l.45-58) does three things:
  - It copies the stat output.
  - It states that the 23:07-23:08 and "23:18" claims of its own session-1 entry are contradicted by the filesystem.
  - It marks f1 NOT VERIFIABLE.

  This is the honest outcome. The session-1 lines are left unedited and the correction is appended. That is right.
- My f6 stat agrees with the log:
  - f6_criteria.md: birth = mtime = 01:18:41, size 5282.
  - f6_iter_chain.py: birth 01:29:04, mtime 01:35:39.
  - f6_out.txt: birth 02:08:25.
- So the criteria predate the script, the criteria were never modified, and the last script edit predates the official
  run. The two POST-HOC lines (V2', V3') are labelled in the script output and in §26.
- The log's claim that the stat was copied "before any f6 script exists" is consistent with these times but not
  independently verifiable (FLOW_LOG.md was rewritten later). Acceptable.
- **(minor)** The FR-2 timestamps "01:0x", "01:3x" (l.199-200) are not times. Give minutes.

## 2. Priority 2: the K1 sign (re-derived independently)

**FLOW's conventions.**
- §0 l.33-35: density e^{-S}; u_{k+1} = β[S_{k+1}] (the marginal coefficient); β_k := u_k − u_{k+1}.

**RLARGE v2 / HIST.**
- RLARGE v2 l.100-101 and HIST l.296: R1 (iii) / R1^J add +δβ_kΣ_ps(U_k(p)) to log Ξ, i.e. to the log of the integrand.

**Derivation.**
- log(e^{-S}) += δβΣs ⇔ S −= δβΣs.
- The shift therefore contributes −δβ_k·β[Σs] to u_{k+1}.
- If Σs is the level-(k+1) Wilson sum, β[Σs] = 1 by c17(A).
- If it is the level-k sum Σ_ps(U_k(p)), as HIST l.296 writes it, it enters S_{k+1} through the tree background, Σs∘Φ.
  β[Σs∘Φ] = β[Σs] = 1 by Lemma F-tree / F-ren (iii), up to O(δβ·g²) loop corrections, which go into ρ_k's E^{≥2} part.
- Either way **β[𝒮^{LF}_k] = −δβ_k**. Hence:
  - u_{k+1} − u_k = −b_k + β[ΣE^{≥2}] − δβ_k;
  - β_k = b_k + ρ_k with **ρ_k = −β[ΣE^{≥2}_k] + δβ_k**.

  This matches l.403-405.
- Every downstream bound uses |ρ_k| ≤ C_ΠE_2g_k² + |δβ_k|. That covers F-rem, F-flow, F-tune, F-R, R, β_± and the e^{aR}
  table of §19A. Neither (RLF-δ)_k nor RLARGE's Σ|δβ_k| bound depends on the sign.

**Verdict: CONFIRMED; no bound changes.**

**Two wording nits (fix S3-7).**
- "the shift LOWERS u_{k+1}" (l.205) is true only for δβ_k > 0. Write "shifts u_{k+1} by −δβ_k".
- l.203-204 should say which field Σs lives on. With HIST's level-k Σs, cite F-ren (iii) for β[Σs∘Φ] = 1.

## 3. Priority 3: Lemma F-mono and HIST's uses of g_k ≤ g_{k+1}

**What F-mono proves.**
- (i): u_k − u_{k+1} ≥ β_- log L − R ≥ −R. This is the lower half of (F_R) at (k, k + 1), and needs g_0, …, g_k ≤ γ.
  **CONFIRMED.** Equivalently: **1/g_{k+1}² ≤ 1/g_k² + R** (⋆).
- (ii), clauses 1 and 2: g_k² ≤ g_{k+1}²/(1 − Rg_{k+1}²) ≤ 2g_{k+1}² for g_{k+1}² ≤ 1/(2R), and
  e^{−a/g_k²} ≤ e^{aR}e^{−a/g_{k+1}²}. Both are (⋆) rearranged. **CONFIRMED.**
- **(ii), clause 3: "g_k^{-p} ≤ (g_{k+1}^{-2} + R)^{p/2}" is WRONG as stated.**
  - It says 1/g_k² ≤ 1/g_{k+1}² + R, i.e. u_k − u_{k+1} ≤ R.
  - The lower half does not give that. The upper half gives only u_k − u_{k+1} ≤ β_+ log L + R.
  - Generically u_k − u_{k+1} ≈ β_0^std log L, which can exceed R.
  - The correct statements are:
    - **g_{k+1}^{-p} ≤ (g_k^{-2} + R)^{p/2} = g_k^{-p}(1 + Rg_k²)^{p/2}** (from (⋆));
    - g_k^{-p} ≤ (g_{k+1}^{-2} + β_+ log L + R)^{p/2} (from the upper half).
- (iii) (exact monotonicity where b_k > C_ργ²; GAP otherwise): **CONFIRMED.**

**HIST's actual uses.** HIST uses g_k ≤ g_{k+1} only in Proposition CL^J. H-pos^J and R1^J inherit it through CL^J; R1^J's
own bounds (l.296-299) are in g_k only.

| # | HIST line | Use | Inequality needed | Covered by F-mono as written? |
|---|---|---|---|---|
| H1 | l.235, CL^J (c) numerator | sup of the C(Y) factors: e c_N^{-1}(κ/g_{k+1}²)^{N²-1} ≤ e c_N^{-1}(κ/g_k²)^{N²-1} | 1/g_{k+1}² ≤ C/g_k² | **NOT covered by (ii) as written** (clause 3 has the swapped indices). Covered by (i)/(⋆): factor (1 + Rg_k²)^{N²-1} ≤ 2^{N²-1} for g_k² ≤ 1/R, per factor. There are ≤ 8\|Y\| factors, so ≤ 2^{8(N²-1)} per cube, which goes into C_J. |
| H2 | l.244-247, CL^J (c) denominator (iii) | exponent (κ/g_{k+1}²)·(3/2)[(1 + A_d)²ε°² + p_L²r²g_k²] ≤ (3κ/2)[(1 + A_d)²ε°²/g_k² + p_L²r²] | 1/g_{k+1}² ≤ 1/g_k² + R | **Covered** by (ii)'s exponential clause (equivalently (⋆)). Extra factor exp(−12κR[(1 + A_d)²(ε^J_loc)² + p_L²r²]) per cube, into C_J. a_J is unchanged. |
| H3 | l.250-254, CL^J (d) | derivative constants: a U_{k+1} or U_{k+2} data link has first derivative ≤ κ/g_{k+1}² ≤ κ/g_k² | 1/g_{k+1}² ≤ C/g_k² | **NOT covered as written** (same index error). Via (⋆): Λ^J_1 → (1 + R)Λ^J_1 (g_k ≤ 1). **Not in the lead's K4 list** ((3.1) and the C(Y) sup only). |
| H4 | l.190, l.349, l.767 (Setting), used at l.237/l.243 | thresholds: (3.1) at g_k needs g_k² ≤ κ; the Haar-cap bound needs rg_k ≤ 1/(4N), i.e. g_k ≤ 1 | g_k ≤ min{1, √κ} from g_{k+1} ≤ min{1, √κ} | **Covered** by the √2 remark (l.1231-1233), with the extra condition g_{k+1}² ≤ 1/(2R). |
| H5 | l.349-353, H-pos^J (i) | "constants independent of k, K, T and g" | — | Covered: after H1-H3 the constants depend on R as well. They remain independent of k, K, T and g. |

**Verdict on F-mono: CONFIRMED-WITH-FIX (S3-2).**
- Replace clause 3 by g_{k+1}^{-p} ≤ g_k^{-p}(1 + Rg_k²)^{p/2}.
- Add the HIST use list H1-H5 to §25, replacing "for HIST's owner to confirm (not checked here)".
- With the fix, all of HIST's uses are of the covered kinds. HIST's owner should still restate CL^J's Setting as
  "g_{k+1}^{-2} ≤ g_k^{-2} + R, g_k, g_{k+1} ≤ min{1, √κ}/√2" and carry the R-dependence of C_J and Λ^J_1.
- F-mono is arithmetic on Theorem F-flow. It is not a separately counted item (F-ll and F-R set the precedent).

## 4. Priority 4: Lemma U-loc', Corollary U-red

**Lemma BL.**
- (i): CONFIRMED. The convexity bound e^{mt} − 1 ≤ (m/m_0)(e^{m_0t} − 1) gives D_m ≤ (m/m_0)N_{m_0}.
- (ii), the infinite-lattice Combes-Thomas: CONFIRMED.
  - The bounded weight f_R makes E bounded.
  - ||EKE^{-1} − K|| ≤ γ/2 gives ||(EKE^{-1})^{-1}|| ≤ 2/γ by Neumann. Symmetry of EKE^{-1} is not needed.
  - The entry bound uses f_R(y_0) = 0.
- (iii)-(v): CONFIRMED. The "compositions → tails" sentence in (v) is a sketch but standard.

**Inputs.**
- (I2): CONFIRMED. a_k = Σ_{j<k}Q_{k−1}⋯Q_{j+1}r_j is right. Cauchy-Schwarz gives |a_k|² ≤ S_nΣ|r_j|², and summing over
  k ≤ n − 1 gives (n − 1)S_n. The Hessian of k̃ at 1 is ½|a_{k+1} − Q_ka_k|² per colour: the O(a²) parts of W and of P enter
  s only at third order. So the gap is correct up to the dropped ½, which is harmless.
- (I3): CONFIRMED (both bounds).
- (I4): CONFIRMED given PG^{(k)} as quoted (upstream, not re-checked). The dense-θ argument is valid for two reasons:
  - Periodised local operators on a side-T torus have exactly the infinite-lattice Bloch fibres at θ ∈ (2π/T)Z⁴.
  - Π^{(n)} has constant rank (h h^T = ||w||²·1), so the restricted infimum is continuous in θ.
- (I5): CONFIRMED (implicit function theorem to order 3).

**The objects.** The order count is right:
- ∂²_rO needs Ψ to fourth order, hence ∇⁴f and the tower to order 3.
- Λ_VV and Γ^W_rr are exactly what the O(r²) remainders need. r(1) = 0, so the Hessian at 1 of a function R(r(v)) with
  R = O(r²) is D²R(0)[Dr·, Dr·].

**Is non-uniformity in n enough?** Yes, for what U-loc' is used for.
- Corollary U-red is an exact identity at each fixed n: B_n = −β[Γ^{W0}_n∘Φ_0] − β[Γ^cov_n].
- Its inputs are:
  - β[Q] = 0, because the symbol is O(p⁴);
  - the O(r²) terms have symbols O(p⁴), so their β is exactly 0;
  - U-dec at the Laplace level, which is exact at one loop.
- β of a functional with an m_n-local Hessian is well defined for every m_n > 0, and an exact zero carries no constant.
- So no m_n-dependent constant reaches Theorem UNIV. All n-uniformity is pushed into (U-IR), which is stated about J_n and
  Γ^cov_n directly.
- **Caveat (fix S3-6):** (U-IR)(a2) concerns the vertices of D𝔪_n^T𝒞_n^{-1}D𝔪_n. A proof of (a2) will need n-uniform
  locality of 𝒞_n and of the composite vertices, i.e. exactly the uniform version that U-loc' does not give. (I3)'s
  gap κ/S_n degrades like q^{-2n}, so the Combes-Thomas rate m_n → 0. Record this as an input (a2) will need: uniform
  locality of 𝒞_n, from N5-triv's per-level rates. U-loc' does not supply it.

**Verdict: Lemma U-loc' CONFIRMED (counted). Corollary U-red now holds without (U-loc): CONFIRMED.**

**But "Theorem UNIV is conditional on (U-IR) only" (l.1082, l.1281) is WRONG as stated (fix S3-1).**
- Theorem UNIV bounds Σ_{k<n}b_k, the per-step numbers of Def F-g and Prop. F-rem, via B_n.
- The identity B_n = Σ_{k<n}b_k is F-tel's second claim. By FT-1 (l.312-317, l.921-925) that needs (SF-bg) at orders 3, 4
  at the trivial point.
- So Theorem UNIV is conditional on (U-IR) and (SF-bg)_{3,4}, or on the FT-1 tower lemma. §28's own OPEN/HYPOTHESES lines
  say so.
- **Cheap upgrade (recommended):** (I5)'s argument applies verbatim to the free-endpoint tree tower Φ_{k←n}: an implicit
  function theorem with the proven-local H_k^{-1} (N2-exp' (ii)) and finite-range vertex tensors. That would prove FT-1's
  "finite-order locality of the tower at 1" at each k and remove (SF-bg) from the one-loop coefficient entirely. This is
  session-scale.

## 5. Priority 5: §24 (the derivative form)

**Lemma U-T⊥: CONFIRMED-WITH-FIX.**
- Step (1): O^{gi} annihilates dΛ, ⟨j, dλ⟩ = 0 for co-closed j, and the zero-mode argument is correct. The FP-ab measure
  equivalence makes the co-closed covariance slice independent.
- Step (2):
  - (dΛ)^⊥ = ker d* ⊕ d𝔐 orthogonally, and ev is bijective on 𝔐.
  - The ν-marginalisation is a Schur complement.
  - The inverse-compression identity is right: 𝒞^{-1} − 𝒞^{-1}P_L(P_L𝒞^{-1}P_L)^+P_L𝒞^{-1} = P_⊥(P_⊥𝒞P_⊥)^+P_⊥.
- Step (3): Woodbury is right, and the bracket is Ĝ_n by F-tree. P_⊥Q_k⋯Q_j = P_⊥Q_kP_T⋯ holds because Q maps
  longitudinal to longitudinal.
- **Fix (S3-5).** "on every torus" fails on an untwisted torus. At the class P = 0 the alias q = 0 has g(0) undefined, and
  the constant 1-forms are in ker d*, carried by the IR term only. This is the same singularity that made f6's (V3)
  unevaluable. Restrict to infinite volume and twisted tori, or treat the q = 0 block separately (there C^⊥ = (Q^TP_⊥(…)^+P_⊥Q)^{-1}
  on constants).

**Lemma DIR, (F1), (F2), Lemma H-sym: CONFIRMED.**
- DIR: Leibniz on sin(ℓθ/2)csc(θ/2) with |θ|^{-1} < ℓ/π gives c_jℓ^jm_ℓ.
- (F2): ℓΠm_ℓ ≤ 2π/|q| from max_α|q_α| ≥ |q|/2 in d = 4. The phase offsets cost ℓ per derivative.
- H-sym:
  - Ĥ ≥ 0 and Ĥ(0) = 0 give ∇Ĥ(0) = 0. The off-diagonal entries are ≤ (H_iiH_jj)^{1/2} = O(|P|²).
  - The Cauchy estimates are on admissible polydiscs: |z| ≤ 3|P|/2 ≤ m'/4 for |P| ≤ m'/8.
  - It is uniform in n given N2-exp' (ii)'s n-uniform bound (upstream, as quoted in N5-loc; not re-checked).

**Lemma U-cov-IR' (i), (ii): CONFIRMED.**
- D_n(q) = −ℓ^{-4}Y^†Ĥ_n(ℓq)Y.
- The ℓ^{|γ|} on Ĥ_n(ℓq) is the one factor ℓ per derivative.
- y² ≤ (2π/|q|)²(π²/(4|q|²))² gives ℓ^{-4+|α|}|q|^{-6}.
- The bound uses sup|∂^γĤ| (not the |P|^{2−|γ|} form), so it is regular at the alias-resonance points. Right.
- "Exactly one factor ℓ" means "at most one". It is an upper bound, and the text should say "at most" (S3-7).
- The comparison with UC-1's suggested |q|^{-6+|α|} is fair. The proven bound is weaker for |q| < 1, and §24.3 shows it
  suffices.

**Lemma U-res' (integrated (R-a)): CONFIRMED.**
- U-res uses (R-a) only in the second piece. The rate form does not use it.
- It is a remark on U-res, **not a separate counted item**.

**Proposition U-a1⊥: CONFIRMED.** Checked line by line:
- (1) The one-Δ terms close on diagonal entries, because J_*'s vertices and g are momentum-diagonal. The envelope ratio is
  (ℓ|q|)^{-4+|β|} ≤ (ℓ|q|)^{-2} for |β| ≤ 2 and ℓ|q| ≥ 1. ∫_{|q|≥1/ℓ}ℓ^{-2}|q|^{-6}d⁴q = π².
- (2) The class measure ℓ^{-4}Σ_{a,b}.
- The derivative costs:
  - On Ĥ_n(P + ℓk): ℓ|P|^{-1}.
  - On Y(q_b + k): ℓ + 2ℓ|P|^{-1}, since |Θ_b| ≥ |P|/2 for all b, using |P| ≤ 2π.
- The alias sums: Σ_{j≠0}(2|j| − 1)^{-2} = π²/4. The K = 0 term gives |P|^{-3}. The restricted a-sum is ≤ c_Yℓ⁵.
- The powers ℓ^{-4−8+2+5+5} = ℓ⁰.
- The P-integrand is O(|P|^{-1}) at 0, which is integrable.
- The constants are n-independent.
- **(minor, S3-7):** in (2), "∫ … dq ≤ A''" must say d⁴q, not §17's dq = d⁴q/(2π)⁴. Otherwise the conversion
  A_{a1⊥} = A' + A''/π² is off by (2π)⁴. It is a constant only.

**§24.4 (a3), (a4): stated exactly enough, but OPEN as labelled.**
- The decomposition C_n = C_n^{ph} ⊕ dT^{-2}d* is orthogonal because span(δ_{c_X}, 1_{B(X)}) ⊥ Λ_res, given Λ_res's two
  block constraints.
- P_TdT^{-2}d*P_T = 0, so the split is consistent with U-T⊥.
- **Overlap (fix S3-6).** (U-IR)(a1) "longitudinal entries OPEN" (l.767, l.1283, l.1292) and (a4) "longitudinal entries
  P_LC^{ph}P_L, P_TC^{ph}P_L" are the same diagrams. Merge them into (a4), or define (a1) as transverse only. Otherwise the
  open list double-counts.

## 6. Priority 6: f6 (the key question)

### 6.1 What failed

- G6, H6 and C6 FAIL, with slopes (9, 15) × 48π² = +0.069-0.070. The (G6) threshold is 0.005.
- The kernel-vertex composite residual Δ^K − c^cov is ≤ 5.2e-6, with slope ≤ 3e-3. That passes the threshold on its own.
- So the whole failure is c^cov. Its values are κ_c-independent:
  - c^cov(9) = −1.3717e-4;
  - c^cov(15) = −6.154e-5.
- These are §26's facts, and the output file agrees.

### 6.2 Analytic form of c^cov in f6's chain (new, exact)

- From the criteria:
  - Γ^cov = log det J_11, with J_11 = κ_1 + κ_2Q1_A^†Q1_A on level-1 fields.
  - κ_1 = 9s and κ_2 = ℓ²s, so κ_2/κ_1 = L_2². This is why c^cov is κ-independent.
- By Sylvester, Γ^cov = const + log det_{level-2}(1 + L_2²Q1_AQ1_A^†).
- Q1_A averages disjoint level-2 blocks, so **Q1_AQ1_A^† is diagonal on level-2 sites**:
  - (Q1Q1^†)(c, c) = L_2^{-4}·N_A(c);
  - N_A(c) := L_2^{-4}Σ_{y∈B_2(c)}|w_A(y, c)|²;
  - w_A = (1/24)Σ_σ exp(iΦ_σ), where Φ_σ is the fine-link flux along axial order σ from y to c.
- Hence **Γ^cov(A) = Σ_c log(1 + L_2^{-2}N_A(c)) + const: a sum of single-block functions.**
- N_0 = 1 and |w| is gauge invariant. To second order in a constant field F:
  - Φ_σ = Φ_0 + Σ_{μ<ν}s_{μν}(σ)·½F_{μν}d_μd_ν, with s = ±1 for the order of μ and ν in σ, and d = y − c in fine units.
  - The cross-pair covariances (= 1/3) multiply Σ_yd_νd_ρ = 0 (ν ≠ ρ).
  - So 1 − |w|² = Σ_{μ<ν}F²_{μν}d_μ²d_ν²/4.
  - Averaging over y: d_μ = 3m_μ, ⟨m²⟩ = (L_2² − 1)/12.
  - Expand log(1 + L_2^{-2}(1 − δ)) and divide by ℓ⁴ = 81L_2⁴ per fine site. The coefficient of ΣF² (c = β/2, as in f5) is

    **c^cov(L_2) = −(L_2² − 1)²/(576 L_2⁴(L_2² + 1)).**

- Values:
  - L_2 = 3: −64/466560 = −1.37174e-4.
  - L_2 = 5: −1/16250 = −6.15385e-5.

  Both agree with f6's −1.3717e-4 and −6.154e-5 to every printed digit.
- Independent confirmation: a brute-force path sum, not using the formula (§6.3).
- Structure: 1/(L_2² + 1) = 9/(9 + ℓ²) is exactly the level-1 noise share that §26 (ii) guessed, and (1 − L_2^{-2})² is
  the discrete flux-variance factor.
- **The log coefficient of c^cov is 0.** c^cov = −1/(576L_2²) + O(L_2^{-4}) → 0.
  - The finite-difference "slope" is (c(5) − c(3))/log(5/3) × 48π² = 0.07014. That is f6's value.
  - The local slope dc/d log ℓ × 48π² tends to ≈ 1.645/L_2² (0.051 at L_2 = 5, 0.0037 at L_2 = 21).
  - The effective power between L_2 = 3 and 5 is 1.57. Exactly: d log|c|/d log L_2 = −2 + 4/(L_2² − 1) + 2/(L_2² + 1),
    which is −1.61 at L_2 = 4 and → −2.

**Answer to the key question: a decaying finite-ℓ correction, not a log.**
- In this family it decays like L_2^{-2}, i.e. like 9/ℓ², with no log term at all.
- It cannot change the one-loop coefficient. Moreover Γ^cov_n is not part of the J_n integral (Corollary U-red), so it
  enters B_n only as the bounded term −β[Γ^cov_n].
- In the real uniform-κ, fixed-L chain the same block-locality argument gives β[Γ^cov_n] → c_cov ≠ 0 geometrically.
  The share of the level-(n − j) noise is ~L^{-2j}, fixed in n. That is (U-IR)(c) with a constant, plus (s2). It is
  bounded, not log-growing, so asymptotic freedom of the soft scheme and UNIV's coefficient are not threatened by this
  term.
- f6's family (L_1 = 3 fixed, L_2 growing) does not test that limit. Its c^cov → 0 is a feature of the family.

### 6.3 Fits under both hypotheses, the third point, and cost

| Hypothesis (two-point fit through ℓ = 9, 15) | Prediction c^cov(21) | Prediction s(15, 21) × 48π² |
|---|---|---|
| A: a + b log ℓ (a genuine log) | −1.172e-5 | +0.0701 |
| B: pure power C ℓ^{-p}, p = 1.57 | −3.63e-5 | ≈ +0.036 |
| C: a + b L_2^{-2} | −4.07e-5 (a = −1.90e-5) | ≈ +0.030 |
| **Exact (§6.2)** | **−3.3319e-5** | **+0.0397** |

**Brute-force confirmation (the reviewer's run).** For L_2 = 3, 5, 7, 9 I summed the 24 axial-order phases on fine links
explicitly: constant F_12, gauge A_2 = εx_1, ε = 1e-3, second difference. I compared the result with the closed form.
Output (copied to the scratchpad file
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revflow3/ccov_out.txt`;
lock taken once, after waiting for another session's job; load 3.3):

| L_2 (ℓ) | brute force | closed form | relative difference |
|---|---|---|---|
| 3 (9) | −1.371733e-4 | −1.371742e-4 | 7e-6 |
| 5 (15) | −6.153376e-5 | −6.153846e-5 | 8e-5 |
| 7 (21) | −3.330854e-5 | −3.331945e-5 | 3e-4 |
| 9 (27) | −2.063326e-5 | −2.065255e-5 | 9e-4 |

- The relative difference grows like the O(ε²d⁴) quartic term of the finite difference. That is consistent with ε = 1e-3
  and |d| up to 3(L_2 − 1)/2; it is not a model discrepancy.
- f6's ℓ = 9 and ℓ = 15 numbers match the closed form better than my brute force does: f6 uses analytic
  k-differentiation.
- Local slopes dc/d log ℓ × 48π² from the closed form: 0.085 (L_2 = 3), 0.051 (5), 0.030 (7), 0.019 (9), 0.013 (11),
  0.0037 (21), 0.0004 (61).
- Two-point slopes: s(9, 15) = 0.07014 and s(15, 21) = 0.03973.

**What a third point would decide.** At ℓ = 21, c^cov separates log (A) from decay (B, C, exact) by a factor ~3 (−1.2e-5
vs −3.3e-5). But the closed form already decides this, so a third point adds nothing for c^cov. What it would test is only
the residual Δ^K − c^cov (≤ 5e-6 at ℓ ≤ 15).

**The pre-registered (G6') would give a FALSE POSITIVE (fix S3-3).**
- At ℓ = 21, s_it^K(15, 21) ≈ s^cov(15, 21) + (single-block kernel part ≈ 0) ≈ 0.040 > 0.005.
- So (G6') would FAIL, and by the reading rule S3-F4 would be "declared OBSERVED", for a term that provably has no log.
- The 0.005 threshold is below the transient's local slope until L_2 ≈ 19 (0.0037 at L_2 = 21), i.e. until ℓ ≈ 57.
- **Do not run ℓ = 21 under the current criteria.**

**Cost.**
- The projected ℓ = 21 time is 6872 s: (1355 + 281) × 4.2, about 1.9 h at nice 10, plus lock waits.
- The smoke test's 1272 ms/class at ℓ = 21 and 575 MB peak are consistent with that.
- It is not worth the time for c^cov, which is known exactly.

**Cheaper discriminating tests (recommended, in order).**
1. **Closed-form criterion (seconds).** Append to f6_criteria.md (append-only) a line: |c^cov_f6(ℓ) − c^cov_closed(L_2)| ≤ 1e-8.
   Re-evaluate the stored ℓ = 9 and 15 values. Replace C6 and the c^cov part of G6/H6 by "slopes of the residual
   c^K − c^cov". This is a pre-registered amendment, not a reinterpretation, and must be labelled as such.
2. **The real chain's Γ^cov (minutes).** For the uniform-κ scalar chain at fixed L = 3 and n = 1, 2, 3, 4 (ℓ = 3, 9, 27, 81),
   𝒞_n(A) = κ^{-1}(1 + Σ_jA_jA_j^†) is again DIAGONAL on level-n sites: the A_j are compositions of disjoint-block averages.
   So β[Γ^cov_n] is a single-block path-variance sum, computable exactly or by brute force up to ℓ = 81. Prediction:
   convergence to c_cov ≠ 0 with an L^{-2}-geometric rate. This tests (U-IR)(c) and (s2) directly. f6 cannot.
3. **The residual Δ^K − c^cov at ℓ = 21** would need the full iterated algebra, which only pays if the residual is under
   suspicion. At ℓ ≤ 15 it is 6e-7 to 5e-6, with slope ≤ 3e-3. Not recommended now.

### 6.4 f6 verdict

- **Validation: PASS as reported.** V2 is a pre-registered FAIL, correctly diagnosed. V3 was NOT EVALUATED. V2' and V3'
  are post-hoc and labelled.
- **Falsification lines:**
  - The FAILs stand as recorded. The reading rule was followed and S3-F4 was correctly not declared.
  - The failing term is now identified exactly: c^cov(L_2) = −(L_2² − 1)²/(576L_2⁴(L_2² + 1)), with zero log
    coefficient.
- **The criteria design was flawed.** (C6) and (G6') test a slope threshold below a known-size transient. They cannot
  PASS before ℓ ≳ 57, and G6' would have produced a false S3-F4.
- §26's post-hoc reading (ii) ("O(L_2^{-2})-type transient … a log would make |c^cov| grow") is **CONFIRMED and
  sharpened.**
- §26 (iii) "f6 neither falsifies nor supports (U-IR)(c)" stands. f6's family has c^cov → 0, which says nothing about
  the uniform chain's c_cov.

## 7. Verdicts per item (session 3)

| Item | Verdict | Fix |
|---|---|---|
| [RFL-fix] set | CONFIRMED except FN-1 (partly applied) and the session-3 claim against FT-1 | S3-1, S3-4 |
| CK-1 provenance correction | CONFIRMED (honest) | — |
| K1 sign (§4 FR-2 block, F-rem, §6.1 (d)) | CONFIRMED | S3-7 (wording) |
| Lemma BL | CONFIRMED (counted with U-loc') | — |
| Lemma U-loc' | CONFIRMED | S3-6 (record the uniform locality (a2) will need) |
| Corollary U-red (now without (U-loc)) | CONFIRMED | — |
| "Theorem UNIV conditional on (U-IR) only" (l.1082, l.1281) | **WRONG as stated**: also (SF-bg)_{3,4} via F-tel/FT-1 | S3-1 |
| Lemma U-T⊥ | CONFIRMED-WITH-FIX (torus q = 0) | S3-5 |
| Lemma DIR, (F1), (F2), Lemma H-sym | CONFIRMED (counted with U-cov-IR') | — |
| Lemma U-cov-IR' | CONFIRMED ("exactly" → "at most") | S3-7 |
| Lemma U-res' | CONFIRMED; a remark, not counted | — |
| Proposition U-a1⊥ | CONFIRMED (d⁴q vs dq constant) | S3-7 |
| §24.4 (a3), (a4) | Statements adequate; OPEN; overlap with (a1)-longitudinal | S3-6 |
| Lemma F-mono | **CONFIRMED-WITH-FIX**: clause 3 has swapped indices, and HIST's H1/H3 need the other direction; not counted | S3-2 |
| f6 | Criteria provenance CONFIRMED; FAILs stand; the cause is identified exactly (a transient with no log); G6' design flaw | S3-3 |

**Corrected tally: 24 PROVEN-HERE (claimed 26).**
- 20 from sessions 1-2.
- 4 from session 3: Lemma U-loc' (with BL), Lemma U-T⊥ (with fix S3-5), Lemma U-cov-IR' (with DIR, H-sym) and
  Proposition U-a1⊥.
- Not counted:
  - U-res' (a remark on U-res);
  - F-mono (arithmetic on F-flow, like F-ll and F-R; and it needs fix S3-2).
- GAP: Corollary UNIV-rate (unchanged).
- WRONG as stated: Lemma F-split (unchanged), and the session-3 sentence "UNIV conditional on (U-IR) only".

## 8. Binding fixes for the next lane-C session

1. **S3-1 (FT-1 consistency).** At l.1082 and l.1281, replace "Theorem UNIV is conditional on (U-IR) only / alone" with
   "conditional on (U-IR) and, for B_n = Σb_k (F-tel), (SF-bg) at orders 3, 4 at the trivial point". Better, discharge
   FT-1 by running §23 (I5)'s implicit-function-theorem argument on the free-endpoint tree tower with N2-exp' (ii).
2. **S3-2 (F-mono).**
   - Replace "g_k^{-p} ≤ (g_{k+1}^{-2} + R)^{p/2}" with "g_{k+1}^{-p} ≤ g_k^{-p}(1 + Rg_k²)^{p/2}". If the other direction is
     wanted, add "g_k^{-p} ≤ (g_{k+1}^{-2} + β_+ log L + R)^{p/2}".
   - Replace the last sentence of §25 with the HIST use table H1-H5 (§3 above). Hand the CL^J Setting restatement and
     the R-dependence of C_J and Λ^J_1 to HIST's owner.
3. **S3-3 (f6 criteria).** Append, never edit, a labelled amendment to f6_criteria.md:
   - the closed-form identity test for c^cov;
   - (G6), (H6), (G6') re-stated on the residual c^K − c^cov.

   Record in §26 that the original (G6') would have produced a false S3-F4. Do not run ℓ = 21 under the original rule.
4. **S3-4 (FN-1 remainder).** Fix l.577 (→ PROOF l.4114-4116), the l.850 row (→ l.4103-4106) and l.566 (L4b → l.1162-1174).
   Narrow §27's "every binding fix applied".
5. **S3-5 (U-T⊥).** Restrict "on every torus" to infinite volume and twisted tori, or add the q = 0 block.
6. **S3-6 (the open list).**
   - Merge (a1)-longitudinal into (a4).
   - Annotate l.772-773 (pointwise → integrated, per §24.3).
   - Record that (a2) needs n-uniform locality of 𝒞_n and the composite vertices, which U-loc' does not give.
7. **S3-7 (wording and constants).**
   - "lowers u" → "shifts u by −δβ_k", and name Σs's level (§4).
   - "exactly one factor ℓ" → "at most one".
   - d⁴q in Proposition U-a1⊥ (2).
   - Give real minutes for the FR-2 timestamps.

## 9. Next target (recommendation)

- **(U-IR)(c) and (s2), the composite-covariance determinant. The reviewer's estimate is session-scale; this is an
  inference, not checked.**
  - In the scalar chain 𝒞_n(A) is block-diagonal on level-n sites.
  - In the gauge chain, *at the linearised level*, 𝒞_n = κ^{-1}(1 + ΣA_jA_j^†) has finite range in level-n units, since
    S4' contours span two adjacent blocks (N5-loc).
  - At a non-trivial background the intermediate Hessian adds curvature terms. Whether they keep the range finite, or
    only exponentially local, is not checked.
  - So β[Γ^cov_n] is a finite sum of single-block path-flux variances weighted by L^{-2j}. Prove |β[Γ^cov_n]| ≤ A_cov and
    |β[Γ^cov_n] − c_cov| ≤ A_sL^{-2n} analytically. f6's closed form is the n = 2 abelian instance with non-uniform κ.
  - Check it with test 2 of §6.3 (seconds to minutes, under the lock).
- **Then FT-1 by §23 (I5)** (session-scale). That removes (SF-bg) from Theorem UNIV.
- (a2) (IR-term vertices) and (a3)/(a4) (the flat δ_{c_X} symbol) remain the paper-scale core of (U-IR)(a). Do not
  report UNIV-1L as close until (a2) has a proof route with n-uniform locality of 𝒞_n.
