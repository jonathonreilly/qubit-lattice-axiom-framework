# REVIEW_FLOW_S11: hostile review of lane C session 11 (FLOW.md §84-§93 and the [RFL10-fix] edits)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f14*. This file is the only one I edited.
No commits, PRs or pushes.

Inputs (read-only, by offset):
- REVIEW_FLOW_S10.md (all).
- FLOW.md §79-§83 (every [RFL10-fix] site, l.3518-3926), §84-§93 (l.3933-4234) in full, §44 GH-log (l.2247-2275), the
  session-5/6 re-split (l.815-860), the S4' linearisation (l.280, l.735-739, l.1447-1480).
- PROOF.md S4' definition (l.595-600).
- FLOW_LOG.md l.457-506 (session 11).
- checks: f14_criteria.md (all), f14_gp_vlong.py (Parts B, C and the kernels line by line; Part A by function), f14_out.txt,
  f14_time.txt.

BSD stat (UTC):
- f14_criteria.md: born = mtime 10:01:43, 5931 B.
- f14_gp_vlong.py: born 10:04:46, mtime 10:05:00, 19923 B, md5 668777da…, which matches FLOW_LOG.
- f14_out.txt: born 10:05:39, mtime 10:05:53, 13639 B.
- f14_time.txt: 10:05:53, 101 B.
- FLOW_LOG.md: mtime 10:13:48.
- FLOW.md: **born = mtime 10:13:14**, 465413 B. The file was replaced at its last write; at 09:56 it had birth 07:38:40.

All of these agree with FLOW_LOG l.470-506.

Numerics. Scratchpad: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revflow11/`.

Lock and run conditions:
- ONE lock acquisition, 10:22:33-10:22:48 UTC, released once with `rmdir` (no trap).
- Load 2.27 (1-min) and memory free 41%, both checked inside the lock before starting.
- nice 10, all BLAS threads = 1, plain `python3`, no `timeout`, `PYTHONDONTWRITEBYTECODE=1`.
- Afterwards: no process left, the lock directory is empty, and nothing was written to checks/.

Runs:
- **f14 re-run** from byte-identical copies (f14 md5 668777da…, f12 md5 fea3107e…): 15.3 s, peak RSS 561 MB. **35/37 PASS
  (B3 n = 3 and X0 FAIL), output IDENTICAL to checks/f14_out.txt once the timing fields are stripped (strict `diff`).**
- **`sp_s4.py`** (reviewer): the 11-symbol of X_n(1) and Y_n(1) at U = 1, by proper-time factorised alias sums (n = 1..7,
  K_a and K_b), for two maps:
  - (i) f14's single straight path;
  - (ii) the block-averaged straight legs, i.e. Q_str, the linearised S4' with the d∘h correction omitted.

  0.12 s, 83 MB. Step control 5e-14. Validation: X11_str reproduces f14 B (1.771397, 7.792197, 21.4264, 185.1699), and
  X11_str − Y11_str = |D̂_ℓ1|²g2_n to rounding (n = 6: 0.8171 vs 0.8160 from f14's printed g2). This is an independent numerical
  check of Lemma GP-L (a) at U = 1.

Line numbers are FLOW.md lines as of this review.

---

## Bottom line

- **Provenance: CLEAN, with one disclosure.** The order was pre-statement (09:56:30) → [RFL10-fix] (09:57-10:01) →
  criteria (10:01:43) → script (10:04:46/10:05:00) → smoke (10:05:10) → official run (10:05:39-53) → proofs (10:08-10:13).
  Every statement change after §84 is logged. One deviation is not logged: **the criteria test the 11-symbol of the Feynman
  X_n for SP-div, while (U7) states Y_n** (S11-2).
- **[RFL10-fix] S10-1..S10-6: all APPLIED and correct.** There are 13 tag lines at the fix sites (l.3518-3926), as claimed.
- **Lemma GP-L: CONFIRMED** ((a)-(d) re-derived; (a) also checked numerically at U = 1).
- **Proposition G2-log: CONFIRMED.** (VC-V) as formulated is FALSE at U = 1 for every covariant block map. This is a narrow
  negative, Feynman form only. Two proof-wording points (S11-4). REVIEW_FLOW_S10 §6's "(VC-V): moderate" was wrong.
- **THE DECISIVE QUESTION: the −½c_gq_α²log log ℓ drift is (a), an ARTEFACT of the Feynman split. It is NOT a contribution
  to β.**
  - At every critical background the total, hence c^tot_n, has an exact G2-free representation: GP-L (c), L-tel, and
    independently the session-5/6 form G_⊥,n + G_gh,n (l.839).
  - The object that carries the drift, [f²]½log det(1 + G2Z), enters γ_n and ½Σφ^V_k with opposite signs and cancels
    identically.
  - L-tel settles the question for THIS mechanism. It does not by itself exclude every other non-standard term in c^tot_n;
    that is exactly the content of the Landau items (VC-L), (GP-L) and the exchange.
  - The heat-kernel universality results (11/3; 1/22 + 21/22) fix only the log ℓ coefficient. They neither produce nor
    exclude a log log ℓ.
  - Details in §3.
- **(GP) expected-failure argument: SOUND as ARGUED.** Q_n is suppressed by ḡ^{-1/2} at the crossover, as needed.
  - The "0.05%" agreement is specific to K_a; at K_b the ratio is 1.02-1.03.
  - The K-free test (1/D_n − 1/D_{n−1})·c_g = 0.54, 0.93, 0.98 → 1 confirms D_n ≈ c_g/(n + n_0) (S11-5).
- **L-tel: CONFIRMED. VFINE-gh: CONFIRMED. FINE-IR-gen: CONFIRMED** under (G1)-(G4).
  - The hypotheses added mid-proof are harmless: **(G4) is automatic** (the backgrounds (p, ϑ) and (−p, −ϑ) are the same
    field), and **(G1′) follows from charge conjugation and hermiticity**.
  - Neither is a property of the soft chain.
  - Minor gap in step (iii): the omitted |q|^{-3} term (S11-6).
- **VFINE-K: value −20q_α²c_g CONFIRMED by a direct derivation** (orbital 4·c_g; orbital × spin cross terms vanish because
  tr A = 0; spin bubble −24·c_g). It can be promoted to "given (CL-V)" once written (S11-3).
- **SP-div: CONFIRMED.** The f14 B3 n = 3 FAIL is an artefact of measuring X instead of Y: Y_11 itself gives ρ_3/L = 0.945
  (S11-2).
  - **Our S4' map DOES average transversely**: Q_str is the block average of straight legs, with symbol Π_α(1D Dirichlet),
    FLOW l.280, 737-739.
  - Reviewer numerics: with Q_str the 11-symbols of X and Y CONVERGE geometrically, with differences shrinking by L^{-2} = 0.111.
  - Not yet checked: the d∘h part of the covariant Q_root (S11-7).
- **New UNIV list: correct in substance, neither minimal nor complete.**
  - (G1′) and (G4) drop.
  - The value of C_{K_F} needs no ARGUED.
  - (GP-L) is part of (VC-L) when (VC-L) is stated for D_ℓ^*Y^{-1}D_ℓ.
  - The plane-wave form factor of 𝔪_n (W_♮) must be re-listed under the exchange item (S11-7).
- **Corrected tally: 65 PROVEN-HERE (claimed 65).** Under the strict convention (S10's 57 base; VFINE-gh folded into
  FINE-IR) it is 62.

---

## 1. Priority 1: provenance and the [RFL10-fix] edits

### 1.1 Provenance

| Event | Time (UTC) | Evidence | Verdict |
|---|---|---|---|
| §84 pre-statement | 09:56:30, 432192 B, md5 ddaacdca… | FLOW_LOG l.462-468 | not re-verifiable (FLOW.md replaced since); consistent |
| [RFL10-fix] | 09:57-10:01 | FLOW_LOG l.469-476; tags | consistent |
| f14_criteria.md | 10:01:43 | BSD stat | ✓ before the script |
| f14_gp_vlong.py | 10:04:46 / 10:05:00, md5 668777da… | BSD stat, md5 | ✓ |
| smoke | 10:05:10 | FLOW_LOG l.484-485 | after the last script edit ✓ |
| official run | 10:05:39-10:05:53 | f14_out.txt birth/mtime | ✓ |
| §85-§93 | 10:08-10:13 | FLOW.md mtime 10:13:14 | after the run ✓ |

- **Logged statement changes:**
  - (U1) (b): "Z invertible" is added, and log|det| is used where an operator may be indefinite. Both honest and necessary.
  - (U2): strengthened to uniform convergence on all of [−π, π]⁴ (S11-4: needs one more line).
  - (U6): (G1′) and (G4) added. Weakening, honest, and in fact vacuous (S11-3).
  - The value of C_{K_F} is downgraded to ARGUED. Honest, though more cautious than needed.
- **Not logged (S11-2).**
  - (U7) and the §84 check plan (b) say "the transverse diagonal symbol of Y_n(1)".
  - The criteria file (B2, B3) instead defines x_{n,μμ} = ℓ^{-4}Σ_m|S_μ|²/λ, which is the FEYNMAN X_n (1/λ, no P_T).
  - §89 bridges the gap by inference ("X − Y grows only like log ℓ"). The inference is correct, but the deviation from the
    pre-statement should be recorded.
- **FLOW.md's birth time is now 10:13:14.** The file was replaced at its last write, so birth-time evidence for FLOW.md is
  gone for this session. The order rests on the checks/ stats and the log, and these are consistent.
- **X0 FAIL diagnosis.**
  - The relative difference is maximal at a kernel value of 1.4e-303 (e^{−T·min} at the double underflow edge). That is
    plausible: the comparison divides by max(|f|, 1e-300).
  - The independent evidence for the extended kernels is C1 (brute force, 8e-8 and 1e-8).
  - Reporting X0 as FAIL rather than re-thresholding is correct. ✓
- **B3 FAIL** (n = 3) is reported as such. ✓ See S11-2: the pre-stated object passes.

### 1.2 [RFL10-fix]

| Fix | Where | Verdict |
|---|---|---|
| S10-1 (Ê_2; 𝔮_0; "−i × average") | l.3518, 3792-3801, 3812-3819, 3912 | APPLIED, correct (Ê_2 formula and the 4𝔮_0 + 4𝔮_1 + 16sin²𝔮_2 normalisation as in REVIEW_FLOW_S10 §4) |
| S10-2 ((DEF) retired → (GP)/(DEF-F); E ≡ 0 on U_f; X ≥ 𝒞 fails at U_f) | l.3834-3843, 3860, 3912, 3926 | APPLIED |
| S10-3 (per-j bound; half-radius polydisc; soft points) | l.3639-3642, 3661-3666 | APPLIED |
| S10-4 (b_n, w_n disclosure) | l.3601-3605, 3720-3722, 3890 | APPLIED; now discharged by f14 A |
| S10-5 (C1, C2, C6 are linear algebra; "off-shell included" struck) | l.3747-3751, 3890-3895 | APPLIED |
| S10-6 (level ghost → (GP); vector IR-id via det A) | l.3860-3868 | APPLIED, then superseded by §86-§87 |

Residue (acceptable): §79 (b)'s first paragraph still says "E_U = εp̂²Ê + O(ε³)" (l.3803). The tagged further correction
directly below supersedes it.

## 2. Priority 2: Lemma GP-L and Proposition G2-log

### 2.1 Lemma GP-L (§85): CONFIRMED

- (a) Critical U means E = HD = 0. H is symmetric, so H vanishes on Ran D and maps into ker D^*. Hence K_F = H_⊥ ⊕ DD^*|_{Ran D}.
  ✓
  - (DD^*)(DΔ^{-2}D^*) = DΔ^{-1}D^*, which is the projector onto Ran D. ✓
  - Covariance M_UD_U = D_ℓι^* gives MDΔ^{-2}D^*M^T = D_ℓG2D_ℓ^*. ✓
  - Reviewer numerics at U = 1 (straight path, covariant at U = 1): X_11 − Y_11 = |D̂_ℓ1|²g2_n to rounding. ✓
- (b) Woodbury: D_ℓ^*X^{-1}D_ℓ = Z − Z(G2^{-1} + Z)^{-1}Z = Z(1 + G2Z)^{-1} = (Z^{-1} + G2)^{-1}. ✓ The extra hypothesis "Z
  invertible" is used only in the last form. ✓
- (c) det X = det Y·det(1 + G2Z) (Sylvester), and log det(D^*X^{-1}D) = log det Z − log det(1 + G2Z). ✓
- (d) D_ℓ = VR, so log det(D^*X^{-1}D) = log det(D^*D) + log det(V^*X^{-1}V). With G_gh,n = ½log det D^*D − ½log det Δ this gives
  the stated identity. ✓
- Consequence γ_n = −2c_gq²log ℓ + γ'_n. This is exact because GH-log (c) gives [f²]G_gh,n = −2c_gq_α²log ℓ with no remainder
  (l.2253-2254). ✓
- Reading (1), "Γ^crit is not a ghost-only pair", is right. It corrects REVIEW_FLOW_S10 §5.3, which described (GP) as
  "the fine-ghost/level-ghost pair".

### 2.2 Proposition G2-log (§86): CONFIRMED (two wording points, S11-4)

- (a) Sampling symbol ℓ^{-4}Σ_mÂ(k_m), and ℓ^{-4}λ(k_m)^{-2} = λ̃(x_m)^{-2}. ✓
- (b) ∫_{1/ℓ<|k|<1}|k|^{-4}d⁴k/(2π)⁴ = 2π²log ℓ/(2π)⁴ = (log ℓ)/(8π²). ✓
  - The f_s Riemann-sum error is O(ℓ^{-2}log ℓ). The near-cell count ℓ^{-4}Σℓ²/|x_m|² ≤ CM²ℓ^{-2} is right.
  - **Wording:** the samples sit at k_m = (K + 2πm)/ℓ, offset by K/ℓ from the cell centres. So this is not a "midpoint-type"
    sum. The O(h) term cancels because f_s is even and the removed cell is centred at 0. Say so.
  - **Strengthened uniformity (all of [−π, π]⁴):** when some |K_μ| → π, a neighbouring alias cell touches x = 0. The
    second-order Taylor comparison then fails there, and so does the term "−∫_{C_0∖B_π}|x|^{-4} + …" written for the
    complement of C_0. The claim is still true (ḡ_n is continuous and the alias set is the same for K and K − 2πe_μ). Fix:
    treat the ≤ 2⁴ aliases with |x_m| < 2π explicitly (bounded and continuous) and apply the cell comparison to the rest.
- (c) x_n = y_n + D̂_ℓg2D̂_ℓ^† with y_n ≥ 0. Hence ⟨D̂, xD̂⟩ ≥ |D̂|⁴g2_n, which is unbounded at every K ≠ 0. ✓
- f14 B1: the slope is log L/(8π²) to 1e-6 at n = 7, at both K. ✓
- **Verdict on the reading.** "(VC-V) as formulated (n-uniform level-unit vertex data of the Feynman X_n) is FALSE at U = 1,
  for every covariant block map" is CORRECT. The cause is covariance-forced sampling of the log-correlated Feynman gauge
  parameter (covariance Δ^{-2}). It is narrow: it concerns the Feynman X-telescoping, not the total.
  - REVIEW_FLOW_S10 §6 rated (VC-V) "moderate". That rating was wrong: the zeroth-order symbol already diverges.

## 3. Priority 3 (DECISIVE): is the log log ℓ drift a defect of β?

### 3.1 Verdict: (a). The drift is an artefact of the gauge-dependent (Feynman) split, and it cancels exactly in the total

**(i) The exact cancellation.** At U_f (critical), with Z := D_ℓ^*Y^{-1}D_ℓ, the exact identities give the following.

From GP-L (b), (c):
  Γ^crit_n = Γ^L_n − ½log det Δ_U − ½log det(1 + G2_UZ_U).

From V-tel, L-tel and GP-L (c) (§87 Reading (3), re-derived):
  ½Σ_{k<n}(Φ^V_k − Φ^L_k) = ½log det X_n − ½log det Y_n + ½log det Δ_U = +½log det(1 + G2_UZ_U) + ½log det Δ_U.

Hence, exactly at each n,
  c^tot_n = ½Σφ^V_k + γ_n = ½Σφ^L_k + γ^L_n.
The whole G2 content, 𝒦_n := [f²]½log det(1 + G2Z)(U_f), enters the Feynman steps as +𝒦_n and the Feynman remainder γ_n as
−𝒦_n.
- §86's mechanism places the drift in the G2 parts: P_n = −log det Δ − ½log det G2, where log det(1 + ḡλ̃²) produces
  c_g log ḡ_n.
- So the −½c_gq_α²log log ℓ of γ'_n and the +½c_gq_α²log n of the Feynman steps are the two signs of one quantity −𝒦_n / +𝒦_n
  (up to the ARGUED Q_n remainder). They cancel identically.

**(ii) Independent confirmation.** The session-5/6 binding re-split (l.836-841) writes the same total as G_⊥,n + G_gh,n.
- G_⊥,n = ½log det_{ker D_0^*}(H + M^TΠM) + ½log det_⊥(P_⊥𝒞_nP_⊥) is a transverse (Landau) determinant with the block mass term.
- It contains no G2: Δ^{-2} never appears.
- G_gh,n is exactly −2c_gq²log ℓ (GH-log (c)).
- So the gauge-invariant total has a manifestly G2-free form, and the log-correlated object Δ^{-2} cannot reach c^tot_n.
- (Gauge-fixing independence, COV-GI at critical backgrounds, is what makes the Feynman and Landau forms equal. Here it is
  realised as an explicit algebraic identity, with no Nielsen-type argument needed.)

**(iii) Physical reading.**
- ℓ^{-4}Σ_m λ̃^{-2} ≈ (log ℓ)/(8π²) is the log-correlated variance of the level-site samples of the Feynman-gauge gauge
  parameter, whose covariance is Δ^{-2} in 4D.
- It is a pure-gauge quantity. The Feynman split routes it through every step X_k and makes the step coefficients converge
  like 1/k instead of geometrically.
- So the Feynman form is not a uniformly local RG decomposition. That is a defect of the bookkeeping, not of the scheme.
- The Landau steps (L-tel) never contain it: Y^{(0)} = P_T/λ annihilates the covariance-forced component, and every
  Y^{(k)} = 𝒞-terms + M^{(k)}H_⊥^{-1}P_⊥M^{(k)T} at critical U.
- Reviewer numerics: for the decision-4 map's Q_str part, the Landau 11-symbol Y_11 converges with differences
  −7.7e-4, −8.5e-5, −9.5e-6, −1.05e-6 (ratio 0.111 = L^{-2}). There is no log ℓ and no log log ℓ.

### 3.2 What is and is not settled

- **SETTLED (exact, conditional only on the invertibility hypotheses of GP-L at U_f):** the specific drift predicted by §86 is
  not in c^tot_n. It is not a contribution to β and does not threaten the standard one-loop running.
- **Does L-tel settle the whole question? Partly.** It shows that G2 drops out of every term of the Landau split. It does
  not show that the Landau pieces have no non-standard n-dependence of their own. That is (VC-L) for the steps, (GP-L)
  for w_n, and the Landau exchange at U_f.
  - No mechanism for such a term is known: the Landau objects carry no log-correlated input.
  - The scalar template (UIR-S, θ = L^{-2}) and the reviewer's Y_11 numerics point to geometric convergence.
- **The heat-kernel results (V-heat 11/3; ghost 1/22 + transverse 21/22, which match ½(−20) − ½(1) = −21/2 and −½ in c_g
  units) fix the coefficient of log ℓ only.** A log log ℓ is invisible to them. Neither the existence nor the absence of a
  log log can be argued from universality of the log coefficient. Only the exact G2-free representation does it.
- Consequence for UNIV: unaffected. The Feynman route must be abandoned for the steps (as §90 does), not because β is
  wrong but because the Feynman steps are not n-uniformly convergent.

### 3.3 The (GP) expected-failure argument itself (§86 l.4062-4076): SOUND as ARGUED

- The factorisation is right: log(1 + ḡλ̃²) = log ḡ + log(λ̃ + iḡ^{-1/2}) + log(λ̃ − iḡ^{-1/2}). Two pieces of |mass²| = ḡ^{-1/2}
  give c_g log ḡ in x-units, and x-units equal f²-units (c = x, from 2c = ĥ(0) and (p²/2)x = ĥp²/4).
- Q_n is suppressed in both regimes (the claim is right, and I checked the crossover the text skips):
  - For λ̃ ~ 1: G2^{-1}Z^{-1} ≲ 1/(κḡ).
  - At the crossover λ̃ ~ ḡ^{-1/2}: G2^{-1}Z^{-1} ~ y_L/(2√ḡ) → 0.
- f14 C:
  - C1 brute force confirms the level formula (8e-8, 1e-8).
  - The classification is "slow" (r_6 = 0.842).
  - Re-run identical.
  - **But the "0.05%" (l.4074-4075) is K_a-specific.** The same post-run ratio at K_b is 1.019, 1.031, 1.029. The K-free form
    (1/D_n − 1/D_{n−1})·c_g = 0.538, 0.927, 0.984 (n = 4, 5, 6; 1/c_g = 96π²) confirms D_n ≈ c_g/(n + n_0), coefficient c_g, at the
    few-% level. Report that form (S11-5).
- It remains a plane-wave, scalar-model test of P_n only; γ'_n is not computed. The text says so. ✓
- Lemma DEF-red (remark): the bookkeeping is correct; it is not counted. ✓

## 4. Priority 4: L-tel, VFINE-gh, FINE-IR-gen, VFINE-K, SP-div

### 4.1 Lemma L-tel (§87): CONFIRMED

- Subtracting T_kD^{(k)}G2^{(k)}D^{(k)*}T_k^T = D^{(k+1)}G2^{(k+1)}D^{(k+1)*} (one-step covariance, plus ι_k^*G2^{(k)}ι_k = G2^{(k+1)}) gives the
  Y-recursion for every U. ✓
  - The one-step covariance needs 𝔪_{k+1} = (one step)∘𝔪_k with T_k its derivative. That holds for the composite polar
    averages (l.1447, 1456). ✓
- Telescoping: Σ_{k<n}Φ^L_k = log det K_F − log det Δ + log det Y_n, so total_n = ½ΣΦ^L_k − ½log det Δ + ½log det Z = ½ΣΦ^L + Γ^L_n. ✓
- Φ^L_0: the block upper-triangular determinant is right: the Ran D column has the identity on its diagonal block. ✓
- U = 1: K_F(1) = d^*d + dd^* = λ·1 and D̂D̂^† = λP_L, so Y^{(0)} = P_T/λ. ✓
- Reading (3): Φ^L_0 − Φ^V_0 = log det(D^*(H^V_0)^{-1}D) − log det Δ (Jacobi). This is an n-independent one-step fine object. ✓

### 4.2 Corollary VFINE-gh (§88): CONFIRMED

The root component carries the U(1) phase e^{∓iq_αa}, so §74 applies with ε → q_αε. It is a corollary; see the strict tally.

### 4.3 Lemma FINE-IR-gen: CONFIRMED; the added hypotheses are automatic (S11-3)

**(G4) is vacuous.** The plane wave ε cos(px_2 + ϑ) with (p, ϑ) is the same field as with (−p, −ϑ). So any family built on
it satisfies (G4).
- More precisely, f(k, −p) = f(k, p) pointwise: under p → −p the ± bubble terms swap, since V_+^{(−p)} = V_−^{(p)} as
  momentum-transfer parts, and the explicit p-factors of the spin vertex transform consistently.

**(G1′) follows from charge conjugation and hermiticity.**
- Complex conjugation maps the root-α operator at background a to the root-(−α) operator, i.e. charge −q_α, equivalently
  ε → −ε, and maps k ↦ −k.
- f is the ε² coefficient, hence even in ε.
- f is real pointwise: tr(O_0^{-1}Ô_2) is a trace of a product of two hermitian matrices, and the bubble is
  tr(A V_+^† B V_+) with A, B > 0.
- Hence f(−k, p) = f(k, p), and with (G4), f(−k, −p) = f(k, p).
- This holds for Δ_U and for K_F = H + DD^* (Wilson action and DD^* are C-covariant; E_α^† = E_{−α}).

**Are they properties of the soft chain?** No. FINE-IR-gen concerns fine operators only. The chain enters at (VC-L), where
the analogous requirement is reflection and C-covariance of the block form factors. S4' has both: it is B_4-symmetric
(D4-norm (1), FLOW l.136, 406) and C-even (l.1923).

**Proof check.**
- (i) ✓. (ii) The relative-order-r correction is odd jointly and integrates to zero. ✓
- (iii) **Minor gap (S11-6):** f_c(q, e_2) − f_c(q, 0) has a FIRST-order term c_1(q̂)|q|^{-3}, not only h|q|^{-4} + c_3|q|^{-5}.
  - c_1 is odd: joint parity gives ∂_pf_c(−q, 0) = −∂_pf_c(q, 0). So ∫_{S³}c_1 = 0, but it must be listed, because pointwise
    it is the largest term.
  - With that, x^O = 2C_O log(1/p) + a^O + o(1). ✓

### 4.4 (VFINE-K): the value −20q_α²c_g is DERIVABLE, not just ARGUED (S11-3)

Direct continuum derivation, with O^c = (−i∂ − qa)²δ_{μν} + 2iqF_{μν}, a = ε cos(px_2)e_1, in the same tr-log convention for the
scalar and the vector, so that only the ratio matters:
- **Orbital and diamagnetic:** O^c's orbital part is diagonal in μν, so it gives exactly 4 × the scalar result, i.e. 4c_g.
- **Cross terms orbital × spin:** the orbital vertex is ∝ δ_{μν}, the spin vertex is ∝ A := E_{21} − E_{12}, and tr A = 0. They
  vanish.
- **Spin × spin:** for an abelian background F is linear in a, so there is no second-order spin vertex. The e^{±ipx_2} parts
  of 2iqF are ∓εpA (as hermitian partners), and tr(−A²) = 2.
  - Spin ε² density: −p²Σ_±∫d⁴k/(2π)⁴ [k²|k ± pe_2|²]^{-1}. Its log(1/p) coefficient is −p²·2/(8π²).
  - So x_spin = −(1/(2π²))log(1/p), i.e. C_spin = −1/(4π²) = −24c_g.
- **Total:** C_{K_F} = 4c_g − 24c_g = −20c_g. This agrees with the heat-trace ratio (10/3)/(−1/6), and the heat-trace arithmetic
  4·(−1/6) + 4 = 10/3 is also right.
- Cross-check: ½(−20) − 1 = −11 is the Feynman-form 11/3. ½(−20) − ½ = −21/2 and −½ give the 21/22 + 1/22 split of GH-log. ✓

So, after these five lines are written in, (VFINE-K) is PROVEN given (CL-V) alone, value included. (CL-V), the explicit
second-order plane-wave vertices of the lattice Wilson Hessian, stays OPEN. It is a computation, checkable against a
finite-difference Hessian as f13 Part C did.

### 4.5 Proposition SP-div (§89): CONFIRMED; B3's FAIL is an X-versus-Y artefact (S11-2); S4' averages transversely

- **Proof.**
  - Lower bound: m_1 = 0, 1 ≤ |m_⊥| ≤ ℓ/4, with |S_1|² ≥ cℓ², (P_T)_{11} ≥ ½ and λ ≤ C|m_⊥|²/ℓ². The 3D sum of |m_⊥|^{-2} is ≍ ℓ. ✓
  - Upper bound by the same count. ✓
  - Physically this is the linear (perimeter) self-energy of a single Wilson line: the variance of Σ_{j<ℓ}a with ⟨aa⟩ ~ r^{-2}
    is ≍ ℓ·Σd^{-2}.
  - Wording: "fibre row ℓ^{-2}S_μ" (l.4146) does not match the formula Y = 𝒞 + Σℓ^{-4}SP_TS^†/λ used one line later, nor f14.
    The row is S_μ, and ℓ^{-4} is the Poisson factor.
- **f14 B3 measured X_11, not Y_11.** Reviewer Y_11 (straight path, K_a), ratios ρ_n/L:

  | n | 2 | 3 | 4 | 5 | 6 | 7 |
  |---|---|---|---|---|---|---|
  | ρ_n/L | 0.838 | **0.945** | 0.983 | 0.995 | 0.998 | 0.9996 |

  **The pre-stated (U7) prediction (within 10% of L at n ≥ 3) HOLDS for the pre-stated object Y.** The X FAIL at n = 3 comes
  from X's extra m = 0 and log ℓ pieces. The FAIL line stays as recorded, because the criteria fixed X.
- **Does the S4' soft kernel average transversely? YES.**
  - S4' averages the transported straight legs over ALL L^d starting points y ∈ B(X) (PROOF.md l.595-600).
  - Its U = 1 linearisation is Q_root = Q_str − d∘h. Q_str has symbol S_μ(k_μ)·Π_α D_ℓ(k_α), a product of 1D Dirichlet factors
    in all four directions, with |D_ℓ(θ)| ≤ min(1, π/(ℓ|θ|)) (FLOW l.280, 737-739).
  - The transverse factors give alias weights ~Π_{α≠μ}m_α^{-2}, which turn the divergent Σ|m_⊥|^{-2} into a convergent sum.
  - Reviewer numerics (Q_str, K_a): X11_blk = 1.15523, 1.15348, 1.15329, 1.15327, 1.153262, 1.153262 (n = 2..7) and Y11_blk = 0.42986 …
    0.4290003. Successive differences shrink by 0.111 = L^{-2}, and the same holds at K_b.
- **Caveat.** Q_str alone is not covariant (Q_str∘d = d∘(ev + h∘d)). The covariant Q_root adds the level-gradient term −d∘h.
  - That term is NOT killed by the fine P_T: it acts on the level side.
  - It is what carries the forced log ℓ into X, by G2-log.
  - Its effect on Y (and on W_n = V^*Y^{-1}V) is not tested here. That is the first concrete item of (VC-L).

## 5. Priority 5: the new UNIV list (§90 l.4165-4178): precise and minimal?

Correct in substance; (DEF), (GP) and Feynman (VC-V) are correctly retired. Corrections:
1. **Drop (G1′) and (G4)** (S11-3: automatic).
2. **(VFINE-K) value:** PROVEN given (CL-V) once §4.4 is written. Then (VFINE-L) = (VFINE-K) − ½(VFINE-gh) is PROVEN given
   (CL-V), value included.
3. **Merge (GP-L) into (VC-L).** State (VC-L) for the steps Φ^L_k AND for D_ℓ^*Y_n^{-1}D_ℓ. log det W_n = log det(D_ℓ^*Y^{-1}D_ℓ) −
   log det(D_ℓ^*D_ℓ), and the last term is exact by GH-log (l.4162-4163), so (GP-L) is then a corollary and not an
   independent wall.
4. **Admissible map: say that the decision-4 map qualifies at the Q_str level.** The open part is the −d∘h (GS-1) term of
   Q_root, plus Lemma A-type product decay for the tensor form factors of T_k, Π_k. "A transversely averaging block map is
   needed" should not read as if a new map were needed.
5. **Re-list the plane-wave form factor of 𝔪_n (W_♮)** (REVIEW_FLOW_S10 §11 item 3). It disappeared from the list. It belongs
   in the exchange item, together with the Nielsen-Olesen mode handled by the Woodbury forms.
6. Unchanged and still required: (L-loc2); (s1), (s2⊥) (rate); the rate of c'(φ) → c'_0; (COV-GI) at non-critical
   backgrounds (not needed on the critical-background route); FI-1; HIST's restatement of CL^J's Setting.

**Minimal list for the vector (UIR)/(V-IR):**
- (L-loc2);
- (CL-V);
- (VC-L) (Landau steps + D_ℓ^*Y^{-1}D_ℓ, for Q_root including d∘h, with the Landau vector IR-id);
- the Landau plane-wave/constant-field exchange at U_f (including the 𝔪_n form factor and the NO mode).

## 6. Priority 6: f14

- **Re-run: 35/37, identical** (§0).
- **Part A: confirmed.**
  - A1 ≤ 7.1e-14 against f12's integrand, and A2 ≤ 2.2e-8.
  - The control fails at 0.41.
  - A real test of §75's b_n, w_n, including the K − P fibre and the Ward normalisations. S10-4 is discharged. ✓
- **Part B.**
  - B1 confirms the G2-log constant to 1e-6. ✓
  - B2 passes (margin 0.29), but it is weak: the inequality holds termwise.
  - B3: see S11-2.
- **Part C.**
  - Formulas re-derived: b2 = −Σ Σ_m[λ^{-2}λ_+^{-1} + λ^{-1}λ_+^{-2}] is the first variation of Δ^{-2}.
  - C1 is an independent brute-force LU test. ✓
  - C2 step control ≤ 7.5e-6. ✓
  - The classification is "slow". ✓
  - The drift magnitude comparison was made post-run, and it is K_a-tuned (S11-5).
- **FAIL honesty: B3 and X0 are reported as FAIL, with diagnosis and no threshold change. ✓**

## 7. Per-item verdicts

| Item | Verdict | Fix |
|---|---|---|
| Provenance | **CLEAN**; criteria deviate from (U7) (X vs Y), unlogged; FLOW.md birth reset | S11-2, S11-8 |
| [RFL10-fix] S10-1..S10-6, 13 tag lines | **APPLIED**, correct | — |
| (U1) Lemma GP-L | **CONFIRMED** (+ numeric (a) at U = 1) | — |
| (U2) Proposition G2-log | **CONFIRMED**; (VC-V) Feynman form FALSE at U = 1 | S11-4 (offset Riemann sum; boundary cells) |
| (U4) (GP) expected failure | **SOUND as ARGUED**; drift is a split artefact (§3) | S11-1, S11-5 |
| Lemma DEF-red (remark) | correct bookkeeping; not counted | — |
| (U3) Lemma L-tel | **CONFIRMED** | — |
| (U5) VFINE-gh | **CONFIRMED** (corollary) | — |
| (U6) FINE-IR-gen | **CONFIRMED** under (G1)-(G4); (G1′), (G4) automatic | S11-3, S11-6 |
| (VFINE-K) | existence **CONFIRMED given (CL-V)**; value derivable (−20 confirmed) | S11-3 |
| (U7) SP-div | **CONFIRMED**; S4' averages transversely | S11-2, S11-7 |
| (VC-L) | **OPEN**; Q_str part numerically geometric (reviewer) | S11-7 |
| (U8) / §90 list | **CORRECT** in substance, not minimal | S11-7 |
| f14 | **CONFIRMED**; re-run identical 35/37 | S11-2, S11-5 |

## 8. Corrected tally

**65 PROVEN-HERE (claimed 65)** = 59 + GP-L + G2-log + L-tel + VFINE-gh + FINE-IR-gen + SP-div.
- Strict convention (REVIEW_FLOW_S10's 57 base, with VFINE-gh folded into FINE-IR as a corollary): **62**.
- Scope:
  - FINE-IR-gen is stated under (G1)-(G4), where (G1′) and (G4) are automatic.
  - SP-div concerns a test map, not the adopted one.
  - G2-log's strengthened uniformity needs the S11-4 line.
- IMPORTED-AND-REVERIFIED: L4b; the Lévy-process functional CLT. No new import. ✓
- ARGUED, not counted:
  - (L-loc2);
  - the (GP) failure mechanism;
  - the value C_{K_F}, until §4.4 is written in;
  - DEF-red.
- OPEN:
  - (V-IR) on G_⊥, reduced to the §5 minimal list;
  - (CL-V);
  - (VC-L) (with (GP-L) merged);
  - the Landau exchange at U_f;
  - the cross-lane and rate items.

## 9. Binding fixes for the next lane-C session

1. **S11-1 (decisive; §86 l.4068-4071, §90 l.4175-4176, §92 l.4213-4214, §93 l.4227).**
   - Add: "The log log ℓ is NOT in c^tot_n. Exactly, ½Σ_{k<n}(φ^V_k − φ^L_k) = +𝒦_n + [f²]½log det Δ_U and γ_n − γ^L_n = −𝒦_n −
     [f²]½log det Δ_U, with 𝒦_n := [f²]½log det(1 + G2_UZ_U)(U_f). The G2 log-correlation cancels identically; the total is also
     G2-free in the l.839 form G_⊥,n + G_gh,n. It is not a contribution to β."
   - Add that the heat-kernel universality fixes only the log ℓ coefficient, and that the absence of any other
     non-standard term is (VC-L) + exchange.
   - Retitle "(GP) expected to FAIL" so that it cannot be read as a defect of the scheme: "(GP), a Feynman-split
     statement, expected false; irrelevant to c^tot_n".
2. **S11-2 (§89 l.4151-4154, §91 l.4191-4192, FLOW_LOG).**
   - Log that f14 B2/B3 (criteria) use the Feynman X_n symbol, while (U7) states Y_n.
   - Report the reviewer's Y_11 ratios (ρ_3/L = 0.945; 0.983, 0.995, 0.998). Keep the B3 FAIL line as recorded.
   - Fix "fibre row ℓ^{-2}S_μ" → "row S_μ, Poisson factor ℓ^{-4}".
3. **S11-3 (§88 l.4118-4121, 4135-4142; §90; §92; §93).**
   - Replace the two hypotheses by their proofs: (G4) is automatic, and (G1′) follows from C + hermiticity.
   - Write the §4.4 derivation of C_{K_F} = −20q_α²c_g (orbital 4, cross 0, spin −24).
   - Then state (VFINE-K) and (VFINE-L) as PROVEN given (CL-V), value included.
4. **S11-4 (§86 l.4038, l.4044-4050).**
   - "midpoint-type" → offset Riemann sum, whose O(h) term cancels by the evenness of f_s and the centred removed cell.
   - For uniformity on all of [−π, π]⁴, treat the aliases with |x_m| < 2π separately.
5. **S11-5 (§86 l.4074-4076, §91 Reading (3)).**
   - State that 0.977/0.996/0.9995 is at K_a, with 1.019/1.031/1.029 at K_b.
   - Add the K-free (1/D_n − 1/D_{n−1})·c_g = 0.538, 0.927, 0.984 → 1.
   - Keep "post-run".
6. **S11-6 (§88 step (iii), l.4131-4132).** Add the odd first-order term c_1(q̂)|q|^{-3}, with ∫_{S³}c_1 = 0.
7. **S11-7 (§89 l.4154-4163, §90 l.4176-4178).**
   - Our S4' averages transversely: Q_str has the product Dirichlet symbol (l.280, 737-739). The admissible-map requirement
     reduces to the d∘h term of Q_root and the Lemma A product decay of T_k, Π_k.
   - Merge (GP-L) into (VC-L).
   - Re-list the plane-wave form factor of 𝔪_n (W_♮) under the exchange item.
   - Drop (G1′) and (G4).
8. **S11-8 (provenance).** Record in FLOW_LOG that FLOW.md was replaced at 10:13:14 (birth reset), so its birth time is no
   longer evidence.

## 10. Next target

1. Apply S11-1..S11-8. The two that change status are S11-3 ((VFINE-K) value) and S11-1 (the drift verdict).
2. **(CL-V):** write the explicit second-order plane-wave vertices of the lattice Wilson Hessian in root sector α,
   including the spin (plaquette) vertex. Show that their small-(k, p) parts are those of O^c. Check against the
   finite-difference Hessian (f13 Part C machinery) to ~1e-10.
3. **(VC-L) for the actual map at U = 1:**
   - Q_root = Q_str − d∘h (GS-1 gives d∘λ_m). Compute the Landau level symbols Y_n and D_ℓ^*Y_n^{-1}D_ℓ and the level-unit
     polarisation x^L_n(P) by alias sums.
   - Prove the Lemma A product decay for the transverse factors.
   - Prove the n-independence of the degree-4 numerator.
   - Suggested check f15, pre-stated:
     - geometric L^{-2} convergence of x^L_n(P), uniformly down to P = 0.05;
     - a control with the straight single path, which must diverge;
     - a test that the d∘h term does not reintroduce a log ℓ into Y or into D_ℓ^*Y^{-1}D_ℓ.

     Jobs < 20 min and < 1 GB, under the lock.
4. Then the Landau exchange at U_f (NO mode via Woodbury; 𝔪_n form factor), and (L-loc2).
