Reviewer model: claude-opus-5-5

# REVIEW55_TUNIF — Opus 5.5 re-review of batch C8: C8, (N-loc), T-uniformity, exponent decoupling

## PRE-STATED (written 2026-10-28T22:13:59Z UTC, before reading any batch file or deriving anything; only the shared brief REVIEW_BRIEF_55.md and the lead's scope message have been read)

Batch files: NLOC.md, TUNIF.md, THETAW.md. Sources by range only: NORMS.md §N4 and §N7; BFT_A.md
(grep "l.396", "RBA2-fix", "BL-5", "BL-6", "W2", "SPD", "l.822"); REVIEW_S22.md l.389-432 (BFT clause
statement). Codex gpt-6-astra/max inputs: CODEX_REVIEW_TUNIF.md, CODEX_REVIEW_THETAW.md (re-read at the
end, since they may still be being written). Check ids: r55u_*. Any numeric check gets
checks/r55u_<id>_criteria.md before its script; exact rational arithmetic only.

Targets (each gets CONFIRMED / NOT-VERIFIED / REFUTED):
U1. NLOC: (N-loc) is bypassed at fixed T; the open half is T-uniformity; the reduction to (N-loc-cell)
    is "one lemma, not a programme".
U2. TUNIF Lemma TU-0: every closed analytic 2-form F^ in the twisted cell complex is D∧b^ with
    |b^| <= 2(1+kappa) L^k |F^| (which kappa, which norm, which L^k).
U3. TUNIF Lemma TU-1: the first obstruction is absorbed by a spread gauge function b^_1 = -mu/L^k.
U4. TUNIF Lemma TU-2: the second obstruction Phi == 0 for every closed F^ at d >= 3 because nu_gamma is
    not a zero divisor.
U5. TUNIF Theorem TU-3: (T-UNIF) PROVEN-HERE, carrying Theorem N1-15 to uniformity in k AND T.
U6. Codex TUNIF: (a) F1 CONFIRMED after an isolated-fibre attack; (b) the TU-6 obligation that
    "admissible as a cell 1-form" gives "admissible as a nested chain reparametrisation fixing all level-k
    roots"; (c) its refutations: mean-subtraction arithmetic (a factor c_0 missing, TUNIF ~l.392), the
    tu1-D "unsatisfiable gate" excuse, the replacement gate's inability to exclude a double pole, the m > 0
    transport inference. And whether (T-UNIF) still stands as PROVEN once these are repaired.
U7. THETAW: decoupling makes the BFT exponent system satisfiable (A = 1/3 data, A = L^{-theta} full);
    "four incompatible windows" = three windows on one job + one requirement on another. Crux: is the
    decoupling faithful, or does it split a symbol the mathematics forces to be one?
U8. THETAW: J6 (theta_A) is a missing clause of BFT-1, consumed twice per cubic vertex.
U9. THETAW: theta <= 1 - alpha is not a proven constraint; the 3/4 ceiling is superseded.
U10. THETAW: sigma > 0 suffices where (W2)/(SPD) is written at exponent 1; Codex THETAW's reported
    "sigma = 1 is already a counterexample" under the original choice.
U11. THETAW: the admissible region is empty at d >= 5 and has zero slack at d = 4.
U12. Every other PROVEN / PROVEN-HERE / REFUTED / FALSE / struck verdict and decision-changing number in
    NLOC / TUNIF / THETAW (enumerated as found; spot-checks labelled as such).

What counts as a refutation (verdict REFUTED):
- R1. An explicit counterexample: e.g. a closed analytic 2-form with no primitive obeying the stated bound
  uniformly in T, or with Phi != 0 at some d >= 3; a cell 1-form admissible in the stated sense that is NOT
  a valid nested chain reparametrisation fixing all level-k roots (if the theorem needs the latter); an
  explicit sigma in (0,1] for which the constants in (W2)/(SPD) are infinite under the stated choice.
- R2. A proof step that is false (identified by file + locating string), with the correct statement.
- R3. An exact recomputation (rational arithmetic / exhaustive enumeration) of a stated number giving a
  different value, with my value and derivation.
- R4. A symbol that, at its file:line definition or in a consuming inequality, is forced to be one object,
  while the claim treats it as two (or vice versa); or a quantifier (k, T, d, L) that is stale.
NOT-VERIFIED when the load-bearing step rests on an object whose definition I cannot locate or settle, or
on a lemma outside the batch that I cannot re-derive here. A file saying PROVEN is not evidence.

---

## R0. Read record and provenance of this review (appended 2026-10-28T22:47:57Z UTC)

**Read in full:** NLOC.md (793 l.), TUNIF.md (679 l.), THETAW.md (716 l.), CODEX_REVIEW_TUNIF.md (207 l.),
CODEX_REVIEW_THETAW.md (read twice: at ~22:20Z it was 198 l. and ended mid-findings at F14 with no summary table —
**unfinished then**; re-read at ~23:00Z it is 237 l. with "Evidence boundaries", "Summary table" and "Short stdout
summary" — **complete now**). CODEX_REVIEW_TUNIF.md was complete at first read ("Review completed: 2026-10-28 22:09:33
UTC" + stdout summary) and unchanged at re-read (mtime 22:09Z).
**Read by range:** NORMS.md §N1 (l.75-144), §N2 (l.145-188), Lemmas N1-2/N1-4..N1-7 (l.228-328), §N4 (l.329-435),
**§N6 Theorem N1-15 and its proof (l.500-600)** — outside the two named sections, read because TU-6's consumer
substitution cannot be checked without it (Codex could not read it, which is why its F6 stayed NOT-VERIFIED) —
and §N7 (l.642-680). BFT_A.md l.34-40, 380-402, 515-562, 797-935, 985-1075, 1240-1300, 1540-1560, 2130-2165,
2355-2362. REVIEW_S22.md l.370-436. RTARGET.md l.575-615. SF.md l.678-682. LINEAR_PACKAGE.md l.60-110, 205-240.
REVIEW_BFT_A_S3.md (grep SPD; l.25-31, 154-170, 243-248). REVIEW_BFT_A_S5.md l.25-45, 194-230.
REVIEW_BFT_B_S9_S10.md l.65-80, 503-548. BFT_B.md l.3729-3736. NBG_B.md l.440-470, 580-600. PROOF.md l.34-46 and
greps for Lemma BR1 / C_♭. HANDOFF.md l.110-140. SESSION25_RESULTS.md l.125-140, 665-815. GREENT.md l.399-420.
EXISTENCE.md (greps; §21.3 l.4766-4800). checks/tu1_*, tu1b_*, tw1_*, tw1b_* (criteria, scripts, outputs).
**No git command was run. Nothing was written except this file and checks/r55u_*.**

## R1. Checks run by this review (criteria written before each script; exact Fractions; plain python, nice 10)

Filesystem birth times (stat %SB, UTC) are recorded so the order can be audited.

| id | criteria born | script born | result | what it decides |
|---|---|---|---|---|
| r55u_1 (checks/r55u_1_nl1ramp.py) | 22:40:03 | after | **A PASS, B PASS, C fired as designed** | NLOC Lemma NL-1's spread-axial representative is NOT bounded by C·sup|B| uniformly in the torus side |
| r55u_2 (checks/r55u_2_tu3poly.py) | before script | after | **R PASS, B PASS, A PASS; C1, C2, C3 fired as designed; C4 reported** | TU-2/TU-3 with z_1, z_2 SYMBOLIC: every pole is removable (exact polynomial divisibility), Φ ≡ 0, D∧b = F |
| r55u_3 (checks/r55u_3_interp.py) | before script | after | **A, B, C, D PASS; E fired as designed** | the admissibility-correction bounds ‖dλ̂‖_∞ ≤ s^{-1}‖d_kμ‖_∞, ‖dλ̂‖_1 ≤ s^{d-1}‖d_kμ‖_1 (sharp), nestedness |

**r55u_1 output (verbatim figures):** half-line staggered field B_1 = (-1)^{y_2}·1[y_1 < R/2], |B|_∞ = 1, |dB|_∞ = 2:
S(R) = max|B − dλ_NL-1 − h^B| = **2, 4, 8, 16 at R = 4, 8, 16, 32 (d = 2)** and **2, 4, 8 at R = 4, 8, 16 (d = 3)**,
i.e. exactly R/2. Control (full-line staggered, curvature uniform along direction 1): S = 1 at every R. Exact
curl and mean preserved in every run (A). Lemma NL-1's own bound is respected (ratio 1/32 resp. 1/48) — NL-1 is
fine; it is the T-free use of it that fails (finding N7 below).
**r55u_2:** 24 random exact instances (d = 3, 4; ℓ = 2, 3; transverse twists in {5/4, 3/7, 7/5, **1**}, the value
1 = resonant): 0 nonzero remainders, Φ ≡ 0, 0 discrepancies in TU-2 (i), in D_βμ = Ω_β and in D∧b = F. With b̂_1
omitted, every instance leaves a nonzero remainder dividing by (Z1 − 1) (16/54/48/243 per instance) — the pole is
real and b̂_1 removes it. d = 2 control F_12 = 1[u_1 = ℓ−1]: Φ = ℓ (= 2, 3) ≠ 0 — the d ≥ 3 clause is load-bearing.
Non-closed perturbation detected in every gate. The concentrated choice b̂_1 = −μ·1[u_1=0] is ALSO an exact
polynomial primitive (0 remainders, 0 discrepancies): it differs from the spread one only in SIZE.
**r55u_3:** sup ratio exactly 1 in all 24 instances; ℓ¹ ratio ≤ 1, equal to 1 for the single-site bump (sharp);
the stronger s^{d-2} bound fails (control fired); s = 9 interpolant = 3∘3 re-interpolation exactly.

**[R1-erratum, own disclosure]** The R1 table's "before script" entries for r55u_2 and r55u_3 were written before I
read the stat. Actual birth times (UTC): r55u_1 criteria 22:40:03 → script 22:40:27; r55u_2 criteria 22:41:06 →
script 22:41:54; **r55u_3 criteria and script both 22:42:35** — they were written by ONE shell command (criteria
heredoc first, then the script heredoc, then the run), so the order is true by construction of that command but is
**not demonstrable from birth times**. I report r55u_3 with that weaker provenance; its criteria were not edited
after the run (modify = birth). The same limitation applies to the worker's tu1b (criteria and script both born
21:32:08), which I hold against tu1b below on exactly the same terms.

---

## F-NLOC. Findings on NLOC.md (target U1)

**N1. Lemma NL-0 ("the gauge ambiguity of Setting SC's chain minimiser is exactly Lemma N1-2's admissible class";
NLOC "A structural fact used throughout, PROVEN-HERE (Lemma NL-0)") — CONFIRMED.** Re-derived: E is a quadratic form
≥ 0, so the minimiser set is affine over ker E; d_0δB_0 = 0 and Qδ B_i = δB_{i+1}, QδB_{k−1} = 0 give δB_0 = d_0λ (+
harmonic) and, by root covariance Q∘d_j = d_{j+1}∘ev (imported: LINEAR_PACKAGE §1.2, "Root covariance: Q∘d = d∘ev"),
δB_j = d_j(ev^jλ) with ev^kλ constant. The consequence used everywhere — a representative is fixed by its level-0
gauge, levels j ≥ 1 forced by B_j = Q^jB_0 − Σ_{i<j}Q^{j−1−i}r_i (the r_i are gauge invariant) — is correct.

**N2. §L3 "(N-loc) is invoked exactly twice … to bound the column ℓ¹ mass |ζ^c_jδ_x|_{ℓ¹}"; T enters only through
the T^d level-k cells — CONFIRMED** against the proof itself (NORMS l.507-555, Theorem N1-15 steps (1)-(5)): steps (1)
and (3) use |d_0ζ^c_0δ_x|_{ℓ¹} and |r_j(δ_x)|_{ℓ¹} (gauge-invariant, (I3)+(I4)+(I5)) and the sup legs |ζ^c Y|_∞;
steps (2) and (4) use "(N-loc) and Lemma N1-7 with τ = links … |ζ^c_0δ_x|_{ℓ¹} ≤ dL^{dk}c_m𝔠_PL^{−k}". NORMS's second
(N-loc) display is never used (NLOC (A2) correct). TUNIF §U2.3 reaches the same reading — also CONFIRMED.

**N3. Lemma NL-1 (torus spread-axial gauge, |B − dλ − h^B|_∞ ≤ 4dR|dB|_∞) — CONFIRMED.** Re-derived step by step:
identity (α) (telescoping of the B_ρ terms round the μ-cycle) and (β) (one plaquette); Step 1 makes B_1 ≡ w_1/R; the
1-increments of B_ρ are −(dB)_{ρ1} + [w_1(y_⊥+e_ρ) − w_1(y_⊥)]/R, summing to zero round the cycle, so ≤ R|dB| from the
slice; later rounds use gauges independent of the earlier coordinates and leave earlier components untouched;
component μ accumulates ≤ (μ−1) transports + one spreading deviation ≤ (d−1)R|dB|; Step 4 adds ≤ dR|dB|. The
honest constant is 2dR|dB|_∞ (NLOC says so). Implemented from its text in r55u_1 (curl and mean exact, A PASS).

**N4. Lemma NL-2 (c_j = L^{−(k−j)}c_k) — CONFIRMED,** with the one step Codex F4/F6 says is not supplied now supplied.
Q(const c) = Lc: Q_str(const) = L^{−d}·L^d·L·c; Q_root = Q_str − d∘h (LINEAR_PACKAGE §1.2) and h(const) is a
level-(j+1)-translation-invariant function, so d∘h(const) = 0. **Mean-zero is preserved:** the column sums of Q_str are
constant — for a fine μ-link z, Σ_X Q_str(X; z) = L^{−d}·#{(y, j): y + je_μ = z} = L^{1−d} — so mean(Q_str B) =
L·mean(B) componentwise, and d∘h has zero torus mean; hence mean(QB) = L·mean(B) and the constant and mean-zero sectors
are orthogonal for the chain form. (Codex's two-site counterexample (y_1, y_2) ↦ (y_1, y_1) has non-constant column
sums; Q_str does not.)

**N5. Theorem NL-3 (Lemma N1-11 on the torus, 𝔠_P^tor ∝ T) — CONFIRMED** (steps (1)-(4) re-traced; given (J1) =
Theorem NQ-1 — whose review is REVIEW55_NORMS's, not mine — and N2-lin/J-str). NLOC's correction to NORMS that Lemma
N1-11's R_eff is never fixed, and on the torus the honest constant is ∝ T, is **CONFIRMED** (the box construction
cannot cover a torus with holonomy; the holonomy is exactly the constant mode Lemma NL-2 computes).

**N6. Corollary NL-4 — "(N-loc) bypassed at fixed T", Theorem N1-15 k-uniform at every fixed T ≥ T_0 with a constant
∝ T^{d+2} — CONFIRMED** (given (J1)-(J4)): §L3 (iii)'s cell count T^d replaces c_m, and NL-3 supplies T-dependent
sup legs; the T-power count T^{d+2} in steps (2), (4) and T² in (1), (3) is right. "The open half is T-uniformity" —
CONFIRMED as the correct statement of what remained (and see U5: TUNIF closes it).

**N7. [NL-corr 1] Theorem NL-3′ ("(N-loc-a) holds with 𝔠_P^♭ independent of j, k and T"; NLOC l.379) — REFUTED as
PROVEN-HERE. New finding, not in Codex.** The proof replaces Lemma NL-1's two "R·|dB|_∞" uses by fine line sums of the
curvature and asserts (l.385) *"for the datum Y with |Y|_∞ ≤ 1 and any fine line ℓ in direction ρ,
Σ_{y∈ℓ}|d_0B_0(y)| ≤ … ≤ 2dC_f·c_m^{1/d}·L^{−k}"*. That bound is justified by summing the exponentially decaying kernel
of a SINGLE source along the line ("(sup per cell, summed over cells)"); for a general datum the sup per cell does not
decay along the line, and the line sum is ≤ (number of fine points on the line) × (row sum) ∝ T·L^{−k}. And the
mechanism genuinely fails: Lemma NL-1's representative is linear in B, and for a field whose curvature line sums are
not small it has sup ∝ R. **Exact counterexample (r55u_1, d = 2, 3):** B_1 = (−1)^{y_2}·1[y_1 < R/2], |B|_∞ = 1 —
max|B − dλ_NL-1 − h^B| = **R/2** exactly (the ramp −Σ_{z<y}(dB)_{ρ1} + y_1Φ_ρ/R reaches Φ_ρ/2 = R/2 mid-line), while
the control with uniform-along-the-line curvature stays at 1. At level 0 of the chain (R = TL^k) the same ramp has
height ≍ |Φ_ρ|, and for δ_x data Φ_ρ is the fine image of a nonzero coarse holonomy difference (NLOC's own Prop. NL-7
claims |Φ_ρ| ≍ L^{−k}); summing the ramps of the T data along a row gives a row ℓ¹ mass ∝ T·L^{−k}, i.e. a T-dependent
sup bound for general Y. (That last step inherits NL-7's unproven lower bound, so for k ≥ 1 I state it as ARGUED; the
REFUTATION is of the proof, whose key inequality has no valid justification, and of the mechanism, which r55u_1 shows
exactly.) **Correct statement:** a T-free sup bound (N-loc-a) DOES hold — for TUNIF Corollary TU-4's representative
(row ℓ¹ mass of an exponentially local kernel, U5 below), not for NL-1's. Consequences: NLOC l.397 "T-count drops from
T^{d+2} to T^d (T^d ≈ 2.8·10²⁸)" and FOR OTHER FILES item 1's "recommended edit: replace Lemma N1-11's 𝔠_P by 𝔠_P^♭"
are **unsupported**; replace by TUNIF TU-4/TU-5 (repaired, U6). TUNIF's U-F3 sentence "NLOC [NL-corr 1] already has
the sup half T-free" relies on N7, but TUNIF's own TU-6 takes its sup legs from TU-4, so (T-UNIF) does not inherit N7.

**N8. §L3 (iv) "T⁶ ≈ 4.7·10⁴³" — REFUTED (decision-irrelevant).** T_0 = 1.2932·10⁷: 1.2932² = 1.67236624,
1.2932⁴ = 2.79681…, 1.2932⁶ = 4.6772…, so T_0⁶ = **4.68·10⁴²**; "(N-loc) is worth about 10³⁶–10⁴³" should read
10³⁶–10⁴² (4.68·10⁴²/7.3·10⁶ ≈ 6.4·10³⁵). T_0⁴ = 2.80·10²⁸ (NLOC/TUNIF) is right.

**N9. Proposition NL-7 (global axial gauge fails (N-loc♯) by a factor T; "PROVEN-HERE") — NOT-VERIFIED.** The
transverse-pure-gauge identity Φ = d_⊥g (sum the Bianchi identity along the 1-line) is CONFIRMED. The failure needs the
lower bound |Φ_ρ(x_⊥)| ≍ L^{−k}, which NLOC itself (FOR OTHER FILES 8 (iii)) calls "an inference … not a theorem".
**N10. Proposition NL-9 (within-cell axial gauge: ℓ¹ on budget, sup off by L^k; "the near/far trade … not available as
stated") — spot-checked: the O(θ) face mismatch computation is right; as a NO-GO for every box-local scheme it is
NOT-VERIFIED** (it prices one construction with one free constant per cell).
**N11. Lemmas NL-10, NL-11, Theorem NL-12 — CONFIRMED (spot re-derivation).** NL-11 is the untwisted analogue of TU-3
(b̂_β = T_1F̂_{1β}, b̂_1 = T_2(−E_1F̂_{12}); the transverse closed V needs E_2V_2 = 0 from a third direction, d ≥ 3);
NL-12's operator symbols are closed column by column (d_k(1 − 𝒲) = 0), so NL-10 (b) applies to the operator symbol,
not to the (non-analytic) symbol of an arbitrary datum.
**N12. §L7: the reduction to (N-loc-cell), "one lemma, not a programme" — CONFIRMED in outcome; one gloss REFUTED.**
TUNIF's Lemma TU-2 + Theorem TU-3 is exactly that one lemma (≈ one page, U2-U4). But (N-loc-cell)'s gloss
"equivalently, the line fluxes of the fine curvature response across a level-k cell, at zero longitudinal coarse
momentum, vanish" (NLOC l.580-584) is false: Ω_β = σ_1(F̂_{1β})|_{p_1=0} is generically NONZERO (r55u_2-C1: removing
b̂_1 leaves a nonzero remainder in every instance; NLOC's own nl1-D "E_1F̂_{1β} ≠ 0 generically"); it is absorbed by
b̂_1, not verified. Only the second-level obstruction Φ vanishes.
**N13. §L7 route-1 negative ("Theorem RW cannot glue gauge representatives") — spot-checked, argument sound (gauge
change is an affine shift, not an orthogonal conjugation); NOT-VERIFIED as a no-go for all gluing schemes.**

---

## F-TUNIF. Findings on TUNIF.md (targets U2-U6)

**U2a. Lemma TU-0 (TUNIF l.265; twisted shift D_μ, line sum σ_μ, partial sum Θ_μ) — CONFIRMED.** Re-derived:
(i) σ_μ(D_μg) = Σ_{i≤ℓ−2}g(i+1) + z_μg(0) − Σ_i g(i) = ν_μ·g|_{u_μ=0}; (ii) D_γ (γ ≠ μ) acts in another coordinate
and its seam factor depends on u_γ only, so it commutes with σ_μ, Θ_μ; (iii) 𝔖_μ = Θ_μ + σ_μ/ν_μ: interior
differences telescope to g, the seam gives z_μσ/ν − σ/ν − Θ(ℓ−1) = σ − Σ_{i<ℓ−1}g(i) = g(ℓ−1); ker D_μ = 0 when ν_μ ≠ 0;
|Θ| ≤ (ℓ−1)|g|, |σ| ≤ ℓ|g|. The coarse-Fourier set-up (fine site = ℓX + u, ℓ = L^k, shift across the seam picks up
e^{ip_μ}) matches LINEAR_PACKAGE l.262's "f̂_0(n·+u) = Σ_v𝔅^v(p;u)b̂_v(p)".

**U2b. Lemma TU-1 (division bound, κ(η,η′) = max(2, (π/2)e^{η′}/(η−η′))) — CONFIRMED.** For |Re w| ≤ π/2,
|Im w| ≤ η′: rotating by e^{−iRe w/2}, Re∫_0^1e^{itw}e^{−iRe w/2}dt ≥ e^{−η′}∫_0^1cos(Re w(t−½))dt ≥ e^{−η′}(2√2/π)
> (2/π)e^{−η′} (Codex F1 reaches the same); Cauchy on the disc of radius η−η′ (only p_μ moves, the others stay in the
strip); for π/2 ≤ |Re w| ≤ π, Re e^{iw} ≤ 0 so |ν_μ| ≥ 1. Removability needs g = 0 on ALL of {p_μ ∈ 2πZ}, i.e.
2π-periodicity, which TU-1 assumes.

**U3. "The first obstruction is absorbed by a SPREAD gauge function b̂_1 = −μ/L^k" — CONFIRMED.** Any b̂_1 with
σ_1(b̂_1) = −μ removes the 1/ν_1 pole, since then σ_1(G_β) = σ_1(F̂_{1β}) − D_βμ = (1 − E_1)σ_1(F̂_{1β}). The spread
choice is the one that keeps the size at one factor ℓ: |b̂_1| = |μ|/ℓ ≤ (1+κ)ℓG and |D_βb̂_1| = |Ω_β|/ℓ ≤ G on the
ORIGINAL strip (D_βμ = Ω_β holds identically, so no second strip loss), giving |G_β| ≤ 2G and |b̂_β| ≤ 2(1+κ)ℓG. The
concentrated choice −μ·1[u_1=0] is also an exact analytic primitive (r55u_2-C4) but has |b̂_1| = |μ| ≍ ℓ²G — the
L^{2k} trap TUNIF names. Note: b̂_1 is a COMPONENT OF A LEVEL-0 1-FORM, not a gauge function of the chain; see U6(c).

**U4. Lemma TU-2: "Φ ≡ 0 for every closed F̂ at d ≥ 3 because ν_γ is not a zero divisor" — CONFIRMED.** Apply σ_1 at
p_1 = 0 to the (1,β,γ) closedness relation: TU-0 (i) kills σ_1(D_1F̂_{βγ}), TU-0 (ii) commutes the rest, so
D_βΩ_γ = D_γΩ_β. Apply σ_2 at p_2 = 0 with β = 2, γ ≥ 3: D_γΦ = 0, so Φ is constant along γ-lines and the seam gives
ν_γΦ = 0 **as an identity between analytic functions of the free variable p_γ** (Φ still depends analytically on
p_3, …, p_d); ν_γ vanishes only on {p_γ ∈ 2πZ}, so Φ = 0 there off a discrete set and everywhere by continuity. This is
an argument about the analytic family, not about one fibre — Codex F1's isolated-fibre attack (a closed non-exact
fibre at all-resonant p, e.g. a constant plaquette) is correctly excluded, and I agree with it. Independently: r55u_2-B
(Φ ≡ 0 as an exact polynomial identity, 24 instances incl. resonant transverse twists) and r55u_2-C2 (d = 2:
F_12 = 1[u_1 = ℓ−1] gives Φ = ℓ ≠ 0, so d ≥ 3 is load-bearing exactly where TUNIF says).

**U5. Theorem TU-3 (|b̂|_{S_η′} ≤ 2(1+κ)ℓ|F̂|_{S_η}; TUNIF l.317) — CONFIRMED, with Codex F10's repair: add "F̂
2π-periodic in each p_α" to the hypotheses.** Steps (1)-(4) re-derived as above; step (3)'s (βγ) equations follow from
D_1(·) = 0 and ker D_1 = 0 off ν_1 = 0, then by continuity. Codex F10's counterexample (a_1 = e^{ip_1/2}, exact,
analytic, not 2π-periodic → the displayed b̂_β has a genuine pole at p_1 = 2π) is valid against the literal text; in the
application the hypothesis holds — LINEAR_PACKAGE l.262-263: the f_0 symbols are "analytic and 2π-periodic on S".
r55u_2-R/A: with z_1, z_2 symbolic, every division by (Z1 − 1), (Z2 − 1) is exact and D∧b̂ = F̂ identically.

**U6. Corollaries TU-4, TU-5 and Theorem TU-6 ((T-UNIF), "PROVEN-HERE given (I-A)-(I-E)") — CONFIRMED as a
conditional theorem (on (N-Q) = Theorem NQ-1 and the frozen LINEAR_PACKAGE imports), after the repairs (R1)-(R7) below;
the DISPLAYED constant 𝔠_L is REFUTED.** Load-bearing steps, each re-derived:
(a) *TU-4.* The import is quoted correctly: LINEAR_PACKAGE Theorem 4.2′ (l.219, with 4.2 (i)-(ii) at l.211-217):
"uniformly in k ≥ 1, T and the fine offset u … B_k ↦ f_0 extend analytically to the strip … bounded there by M; …
torus kernels are the periodisations". With F̂ = L^{−2k}𝔅^v(·;u) (closed: fine Bianchi ↔ twisted closedness),
TU-3 gives |b̂| ≤ 𝔠_0L^{−k} on S_η′ and the contour shift gives |K(X;u)| ≤ 𝔠_0L^{−k}e^{−η′|X|_1}. Periodisation
commutes with d_0, so d_0b^per = d_0B_0^torus; b^per − B_0^torus is closed, and after subtracting means it is exact,
b′ := b^per − mean(b^per) + c_0 = B_0 − d_0λ (closed + zero mean ⇒ exact on the lattice torus).
(b) *TU-5, level 0.* ℓ¹ ≤ d𝔠_0c_η′L^{(d−1)k} (Lemma N1-7 grouping) + harmonic mode L^{(d−1)k} (one orientation; TUNIF's
dL^{(d−1)k} is an upper bound, Codex F4 right) + the mean of b^per, whose ℓ¹ contribution is
dT^dL^{dk}·𝔠_0c_η′L^{−k}T^{−d} = **d𝔠_0c_η′L^{(d−1)k}** — TUNIF l.392 writes **dc_η′L^{(d−1)n}, dropping the whole
factor 𝔠_0** (Codex F4: I agree, re-derived). T-free either way.
(c) *TU-6's admissibility step — "admissible as a cell 1-form" does NOT give "admissible as a nested chain
reparametrisation fixing all level-k roots"; it is a separate obligation, and it is DISCHARGED.* TU-3's output is just
a level-0 field with the right curl. Two further facts are needed and both hold: (i) by (a), b′ = B_0 − d_0λ for a
fine λ, and the levels j ≥ 1 are then forced and equal B_j − d_j(ev^jλ) (Lemma NL-0, root covariance) — nested
automatically; (ii) μ_x := ev^kλ is generally NOT constant, so the family is the minimiser for Y − d_kμ_x; adding
d_j(ev^jλ̂) with λ̂ the nested multilinear interpolant of μ_x (NORMS Lemma N1-6) makes the gauge λ − λ̂ vanish at
every level-k root. Its cost is controlled by h := d_kμ_x = Y − b^{(k)} through ‖H_jh‖_∞ ≤ s^{−1}‖h‖_∞ and
‖H_jh‖_1 ≤ s^{d−1}‖h‖_1, s = L^{k−j} (Codex F6's estimate; I re-derived it — the fine α-difference of a multilinear
interpolant is s^{−1} times a transverse convex combination of coarse α-differences, and the transverse hat weights sum
to s per direction — and r55u_3 checks it exactly, sharp). With ‖h‖_1 ≤ 1 + 𝔏_k and ‖h‖_∞ ≤ 1 + sup|b^{(k)}|, both legs
stay in budget and T-free. TUNIF asserted this in one line ("a difference of exponentially localised objects") and
left it out of 𝔠_L; the substance is right, the budget is incomplete.
(d) *TU-5, levels j ≥ 1.* Per-cell sup of Q^jb′ ≤ 𝔮_0L^j × (sup of b′ over the cells Q^j reads), times dL^{d(k−j)}
links per cell, summed against e^{−η′|X|_1}: ≤ d𝔮_0e^{O(dη′)}(𝔠_0c_η′ + mean + harmonic)L^{(d−1)(k−j)}. The e^{O(dη′)}
is TU-prec 1's finite range of Q^j (S4′ contours use B(X) ∪ B(X+e_μ), so the range is ≤ about two cells; the exact
factor is a constant). The residual terms need exponential locality of B_k ↦ r_i for all i: TUNIF's (I-A) lists only
r_{k−1}, but the import exists — LINEAR_PACKAGE l.235-236 "By Lemma 3.1 (c) the kernels B_k ↦ r_i … are exponential
too (Corollary N2-exp-b)", with r_{i−1} = (κ_i/κ_{i−1})Q_str^Tr_i (NORMS (I4)) — and the sum is the one of NORMS
Lemma N1-4/N1-11, ≲ L^{−3(k−j)} ≤ L^{−(k−j)} per cell at d = 4.
(e) *Consumer substitution.* With NORMS §N6 read: steps (2), (4) consume exactly 𝔏_j (TU-5); the sup legs of steps
(1)-(4) are the row ℓ¹ masses of the SAME linear representative (b^per part ≤ d𝔠_0c_η′L^{−k}; mean part ≤
d𝔠_0c_η′L^{−k}; c_0 part ≤ dL^{−k}; interpolant part ≤ L^{−k}·2^{d−1}·(1 + row sum of b^{(k)})) — all T-free; the four
exponent counts and step (5) are untouched. One representative carries both legs (no U-F4).
**Repairs (R1)-(R7), none touching T-uniformity:** (R1) TU-2/TU-3: state 2π-periodicity. (R2) TU-5: mean-of-b term
d𝔠_0c_η′(·𝔮_0 at j ≥ 1), not dc_η′. (R3) harmonic term L^{(d−1)n} (≤ the stated dL^{(d−1)n}). (R4) put the
admissibility-correction contribution (via H_j) into both 𝔠_L and the sup constant. (R5) the e^{O(dη′)} range factor
(TU-prec 1). (R6) list Corollary N2-exp-b / J-str (c) among the imports. (R7) "13.5" is L³/(L−1) at L = 3 only (Codex
F8 right; 125/4 at L = 5). **After (R1)-(R7), (T-UNIF) stands as PROVEN, CONDITIONAL on (N-Q) = Theorem NQ-1 and the
frozen imports, at d = 4, trivial background, abelian/linearised** (TU-2 needs d ≥ 3; N1-15's imports are d = 4).
Status line for N1-15: "CONDITIONAL on (N-Q); uniform in k and T" — TUNIF's FOR OTHER FILES item 4 is right in
substance, with 𝔠_L recomputed. Its item 7 ("if Setting SC's Q is the straight average, 𝔮_0 = 1 and N1-15 is
unconditional") is counterfactual: LINEAR_PACKAGE §1.2 defines Setting SC's Q as the S4′ linearisation Q_root =
Q_str − d∘h, so N1-15 stays conditional on NQ-1 (that theorem is REVIEW55_NORMS's).

**U6′. Remaining TUNIF items.**
- **(Q3) "At any m > 0 the T-dependence … disappears for free … it needs nothing but the T-free sup bound" (l.183,
  l.208) — REFUTED (agree Codex F3).** Decay of the INPUT (|Y(b)| ≤ e^{−md(b,x)}) is not decay of the RESPONSE at the
  vertex: an ∞→∞ bound does not transport weights (Codex's rank-one map (RY)(p) = Y(x) has norm 1 and gives T^d).
  The spare factor needs a weighted response bound — NORMS's second (N-loc) display — which TU-4's local kernel would
  supply for m < η′, but "nothing but the sup bound" is false. **"The consumer's norm is the m = 0 one" — CONFIRMED**
  (N_0 = sup over global sign patterns; BR1 consumes N_0).
- **[TU-corr 4] (N-loc-b) as literally stated is not what is delivered; (N-loc-b′) = decay + the explicit constant mode
  is, and is exactly what (N-loc♯) needs — CONFIRMED** (agree Codex F6's rank-one remark; the constant T^{−d} tail is
  ineliminable by gauge).
- **[TU-corr 1], [TU-corr 2] — CONFIRMED** given U6 ((N-loc-cell) discharged; "T-uniformity open" superseded for the
  (N-loc) route, conditional on (N-Q)). **[TU-corr 3] / §U6 (i) — arithmetic CONFIRMED** (2M_n/n = 16 + 4/n ≤ 20;
  148/9 = 16.44 at n = 9); §U6 (ii)-(iv) are BFT_B-lane readings, spot-checked only.
- **tu1-D's excuse "the criterion was unsatisfiable by the truth" (TUNIF l.543-546; tu1b_criteria.md) — REFUTED (agree
  Codex F2).** Hand-verified Codex's exact input (ℓ = 3, d = 4, a_1 = 1[u_1 = 2], twists (5/4, 3/7, 7/5)): Ω_β =
  −ν_β1[u_β=2], μ = −1, b̂_1 = 1/3, b̂_β = (u_1/3)ν_β1[u_β=2], corrected max|b| = 8/21; without b̂_1, max|b| = 4/(7ε),
  growth exactly 1000 over ε = 10^{−1}…10^{−4} — the "≥ 10³" gate PASSES. The seed-777 FAIL is genuine (regular part +9:
  Codex's 1137/(70ε) + 9 reproduces TUNIF's printed 171.4, 1633…). **The tu1b replacement gate cannot exclude a double
  pole (agree Codex F2):** tu1b_pole.py tests only lower bounds (ratios ≥ 9, last ≥ 9.9), and a double pole gives 100;
  it also decides on floats (`float(on["maxb"])`). "Six decades" = five (agree Codex F7).
- **tu1-E "this is the clause that would have caught [U-F2]" (l.537) — REFUTED in logic (agree Codex F5):** a ≤ 100·ℓ
  bracket at ℓ ≤ 9 cannot separate one factor of ℓ from two; r55u_2-C4 shows the concentrated choice is a valid exact
  primitive, so only its SIZE differs. I did not re-run Codex's specific rationals (48/215, 629/3780, 253/1401).
- **Pre-registration chronology of tu1 (Codex F7: NOT-VERIFIED) — RESOLVED, I partly disagree:** birth times
  tu1_criteria.md 21:29:53 < tu1_twisted.py 21:31:27 < tu1_out.txt 21:31:33, criteria never modified — tu1 WAS
  pre-registered; the header "Written 21:33Z" is simply a wrong clock time. tu1b: criteria and script both born
  21:32:08 (header says 21:36Z) — order not demonstrable, and tu1b is post-hoc by its own text.
- **§U4.7 "scored at any T above ≈ 10⁹ it is cheaper [than GREENT]" (l.426-427) — REFUTED (decision-irrelevant).**
  GREENT's own table (GREENT l.416, unreviewed) gives 𝒮_T/log(2T) = 1.55·10⁷ at T = 10⁹; since e^{22} > 2·10⁹,
  𝒮_T(10⁹) < 1.55·10⁷·22 < 3.5·10⁸ < 7.9·10⁹. With logarithmic growth the crossover is near log(2T) ≈ 7.9·10⁹/1.6·10⁷
  ≈ 490, i.e. T ~ 10^{2xx}, not 10⁹. The table's other figures (κ = 83.4/168.4/423.4; c_η′ = 1.18·10⁸/2.33·10⁷/1.12·10⁷;
  7.88·10⁹; ×31 at T_0; ×1.07·10³ over c_{m_*′} = 7.36·10⁶) were spot-checked approximately and agree; none decides
  anything.
- **§U3 "'Volume-uniform' occurs 162 times in EXISTENCE.md" (l.226-227) — REFUTED as a count:** grep -ci gives 23
  (lines containing "volume" = 162). The substance — §21.3 demands level-uniform thresholds and never attaches volume
  uniformity to C_♭ / N1-15's constant — spot-checked consistent (§21.3 l.4766-4800).
- **§U3 PROOF citations l.5842 and l.5835-5840 — drifted** (BR1 "Let T ≥ T_0" now l.5896; C_♭ := 4S_♭n_1/r_♭ now
  l.5889; Codex's 5892/5885-5890 have drifted again). Content as cited.

---

## F-THETAW. Findings on THETAW.md (targets U7-U11)

**W1. The job inventory (six jobs; REVIEW_S22 writes three of them with one θ_w) — CONFIRMED** against REVIEW_S22
l.392-399 and l.409-410: l.393 "level-j curvature and soft-fluctuation components are weighted by L^{θ_w(k-j)}";
l.394-395 "nonlinear sources in a divergence-form norm Y (SF/RTARGET §33's pair with ω_l = L^{θ_w(k-l)})"; l.399
"there exist … θ_w ∈ (0, 2]"; BFT-1 (l.409-410) one rate for plaquette logs and ρ(U_j, U_{j+1}), no potential clause.

**W2. The crux — is the decoupling faithful, or does it split a symbol the mathematics forces to be one? — FAITHFUL
(CONFIRMED).** (i) Curvature vs residual weight: different objects with different delivered decay (2 by NORMS Lemma
N1-4, d−1 by J-str (c)); nothing identifies them. (ii) Displacement weights vs source weight: in the pair REVIEW_S22
itself cites, RTARGET §33 l.580-598, the output norms carry FIXED coarse-unit weights (H^c = L^{2(k−l)}H,
r^c = L^{k−1−i}r) and the source weight ω_l = L^{θ(k−l)}, θ ∈ (0, 1], is a SEPARATE parameter (also BFT_A l.36:
ω_l := L^{θ(k−l)}, θ ∈ [0, 1); SF l.680: θ ∈ (0, 1]) — REVIEW_S22 l.394 merged them by writing θ_w. In the fixed-point
argument the source and displacement weights interact only through INEQUALITIES ((C2) θ_w^r ≤ 2 + θ, (C3) α < θ, the
F3/SPD/COF conditions), never an identity. (iii) The one identity that IS forced — BFT-1's decay rate equals 𝔐's
weight on the same component, because BFT-1 is the reading of BFT-0's 𝔐-ball — is preserved by THETAW (θ_w^c both
places; θ_w^r both places). (iv) θ_A is genuinely not free (see W8), and THETAW keeps it bound. I agree with Codex F11
("No algebra in these vertices forces c = r = θ").

**W3. The decoupled exponent system is SATISFIABLE — CONFIRMED (as a formal exponent system).** Witness (agrees with
Codex F11): (θ_w^c, θ_A, θ_w^r, θ, α) = (2, 1, 5/2, 1/2, 1/4): Wilson 2 + 2 ≥ 4; soft 5/2 + 2 > 4; θ_w^r ≤ 2 + θ;
0 < α < θ < 1; even θ ≤ 1 − α. A = L^{4 − 5/2 − 2} = L^{−1/2}. This is a statement about parameters, not about the
open estimates (THETAW §T4.4 says so; Codex's "full-target satisfiability NOT-VERIFIED" is the same caveat).

**W4. "A = 1/3 data" — CONFIRMED** (A = L^{d−θ_w^r−2θ_A} = L^{4−3−2} at θ_w^r = d−1 = 3, θ_A = 1; this is N1-15's
data-only A_soft). **"R_lin — level-k data, divergence-form sources, residual-type sources … θ_w^r = 3" (THETAW l.305)
— REFUTED (agree Codex F5):** THETAW's own (C2) (from BFT_A l.1551: Σ_iL^{k−1−i}‖σ^c_i‖ ≤ Σ_iL^{−θ(k−i)}‖s‖_R/κ_-)
caps the residual exponent at 2 + θ < 3 as soon as residual-type sources are in the class; R_lin with θ_w^r = 3 is
the DATA-ONLY region. **"A = L^{−θ} full; 1/3 is an unattained infimum" (l.322-336, F6 item 2) — NOT-VERIFIED.** It is
a formal exponent count for a nonlinear-source contraction that has not been set up; Codex F10's endpoint objection is
correct (with HX's Σ-aggregation the strengthened leg needs δ := θ_w^r − 2 < θ strictly, the endpoint costs k); and
there is a symbol collision — N1-15's A_soft (data-only third derivative, exactly 1/L) is a different object from
this formal ratio, so nothing here revises NORMS/PROOF's A_soft = 1/3 for Theorem N1-15.

**W5. "The four incompatible windows were three windows on one job plus one requirement on another" — CONFIRMED in
substance, with one sentence REFUTED.** Located: lane A's α ≤ θ ≤ 1 − α (BFT_A l.396, l.827), SF's θ ∈ (0, 1]
(SF l.680, inside (a5-G♯) "in RTARGET §33's pair"), RTARGET's θ ∈ (0, 1] (l.587-588) are all windows on the SOURCE
weight; the fourth (NBG_B l.452 / PROOF [S25-fix 3]) is the composite contraction's residual exponent. Two
corrections: (a) the residual REQUIREMENT is θ_w^r > d − 2θ_A = 2 strictly (NORMS l.651-662); "= 3" is the data-only
SUPPLY — that is why the decoupled system is satisfiable at all; (b) **"Once the letters are separated they are
constraints on different variables and cannot clash" (l.205, l.522) — REFUTED as stated (agree Codex F11):** (C2)
couples J2 to J3, and the four windows as NBG_B listed them (requirement "θ_w^r = 3" together with θ < 1 and
residual-type sources) DO clash through (C2); they stop clashing only after (a).

**W6. "J6 (θ_A) is a missing clause of BFT-1, consumed twice per cubic vertex" — CONFIRMED as to consumption and as a
fact about REVIEW_S22's text; the proposed clause (1c) is REFUTED at its literal reading.** Consumption: NORMS §N6
steps (1)-(4) each carry exactly two potential legs (|ζ^c_0Y||ζ^c_0W|; |ζ^c_0δ_x|_{ℓ¹}|ζ^c_0W|; two legs at levels
j, j+1; |ζ^c_jδ_x|_{ℓ¹}|ζ^c_{j+1}W|) — I read the proof (Codex could not, its F12 left this NOT-VERIFIED). BFT-1 states
no potential bound (REVIEW_S22 l.409-410); the potential leg is carried only implicitly by 𝔐's "X_c-type" norm in
coarse units (BFT_A l.38 ‖x^c_j‖; RTARGET X_c), as THETAW itself notes. But (1c), *"There is an admissible gauge
representative with own-units potentials ≤ C_0L^{−(k−j)}ε"* (THETAW l.607-610), bounds the BACKGROUND's potentials by
the CURVATURE size ε, and that is false on a torus with holonomy — Codex F13's example, which I checked against BFT's
data hypotheses: a commuting diagonal link exp(iφH/T) in one direction has every plaquette = 1 (so
max_P|log V_P| = 0 ≤ ε, z = 0) and cycle holonomy exp(iφH) ≠ 1, while (1c) would force the holonomy within C_0Tε of
1 for every gauge (holonomy is gauge invariant), false as ε → 0 at fixed T. Correct object: the displacement X
relative to Z^lift (which carries the holonomy), in 𝔐's coarse units, or the linear response's potential bounded by
the data's size (as N1-15 actually consumes: |ζ^c_jY| ≤ 𝔠L^{−(k−j)}|Y|_∞). Note NORMS §N7 l.644-646 writes θ_A with
"≤ CL^{−θ_A(k−j)}ε" too — the same loose ε; harmless there (data-only linear statement), not harmless in BFT-1.

**W7. "θ ≤ 1 − α is NOT a proven constraint" — CONFIRMED; "the ¾ ceiling is superseded" (l.200-201, §T7.1 item 2,
F5) — REFUTED (agree Codex F4).** BL-7 (f) (BFT_A l.560-561) "θ ≤ 1 − α enters only through the repaired plain slot
(BL-6 (c)), ARGUED" and [RBA2-fix] B4's proven list (l.834: θ > 0, θ < 1, α ≤ θ) both confirm "not proven". But B4
(l.826-827) RESTATES the window, "**0 < α ≤ θ ≤ 1 − α (so α ≤ ½), e.g. α = ¼, θ ∈ [¼, ¾]**", attached to (W1), (W2);
l.396-397 contains no ¾ (only "α ≤ θ ≤ 1 − α (so α ≤ ½)"); the ¾ is B4's own example value at α = ¼, quoted as a
ceiling by NBG_B/PROOF [S25-fix 3]; and REVIEW_BFT_A_S5 l.199 still records "the package window is 0 < α ≤ θ ≤ 1 − α".
**Correct statement:** lane A's recorded window keeps θ ≤ 1 − α as an ARGUED condition of its route; it was never a ¾
ceiling (sup over α is 1, unattained) and it does not empty the region (W3's witness satisfies it).

*(Erratum to W5: the NBG_B row "what the composite contraction REQUIRES … θ_w^r = 3" is at NBG_B l.451, not l.452.)*

**W8. θ_A pinned at 1 and θ_w^c's floor of 2 — CONFIRMED, and slightly stronger than THETAW states.** θ_A ≤ 1 is a
hard cap for EVERY admissible representative: for pure-gauge data d_kλ, any admissible level-j gauge agrees with λ at
the level-k roots, so along the L^{k−j} level-j links joining two adjacent roots the potentials sum to (d_kλ), and the
largest is ≥ L^{−(k−j)}|d_kλ| (pigeonhole; Codex F12 agrees). Then the Wilson condition θ_w^c + 2θ_A ≥ 4 forces
θ_w^c ≥ 2 from the cap alone, without THETAW's formula θ_A = min(1, θ_w^c − 1). The ceiling θ_w^c ≤ 2 remains ARGUED
(NORMS l.660; THETAW labels it so). I checked that a flux argument does not upgrade it: d_kB_k = d_k(Q_str^kB_0) −
Σ_i d_k(Q_str^{k−1−i}r_i), and the i = k−1 residual term is O(sup|d_kY|), so the coarse curvature can in principle be
carried by r_{k−1}; the one-level transfer K_p^♯ is what decides it, as NORMS says.

**W9. σ > 0 suffices where (W2)/(SPD) is written at exponent 1 (THETAW §T4.3 l.355-373, F7 l.705-713) — REFUTED as
stated, derived and used. The bare exponent fact survives by a different derivation but has no live consumer.**
(a) *The derivation is invalid (agree Codex F1).* (W2) as defined (BFT_A l.830-831) bounds "the Ran Q^T component of a
remainder row at level l, CARRIED UP TO LEVEL m" by L^{−(m−l)}η² — decay in TRANSPORT distance. THETAW l.361 instead
posits "decay σ relative to the top, so a row born at level l has plain coarse size ≲ L^{−σ(k−l)}η²" and weights the
row AT BIRTH by ω_l. Codex's scalar countermodel a_{m,l} = L^{−σ(m−l)}η² satisfies (W2) with constant 1 while
ω_la_{l,l} = L^{θ(k−l)}η² is unbounded — so (W2) does not imply THETAW's hypothesis, and the "iff θ ≤ σ" condition is
about a different statement. Moreover the actual rows do not decay at birth at all (BFT_A [RBA2-fix] B3 l.819-824;
BFT_B l.3735 "π_l(V_l) ≤ 2C_NCC_bchκ_+L²η², uniform in l").
(b) *The witness fails at the original exponent (agree Codex F8; immaterial).* α := σ/2, θ := σ gives θ = 1 at σ = 1,
excluded (C_P = L/(e(1−θ)ln L) diverges); with θ ≤ 1 − α kept it fails for σ > 2/3. θ := min(σ/2, ½), α := θ/2 works
for every σ > 0. So "under the original choice the constants are not finite for every σ > 0: σ = 1 is already a
counterexample" is TRUE of THETAW's displayed formula — and it refutes only the formula, not the existence of a witness.
(c) *What the consumer of (W2) actually needs — my re-derivation.* The only place lane A consumed (W2)-type decay is
§13.7's implication "(G♯-rough) + (SB) ⇒ H-lin_inv" (BFT_A l.1050-1061; [RBA3-fix] B2′ l.1329-1331: "(W2) ⟸ SPD +
(SB)"). Replace its decay L^{−(m−l)} by L^{−σ(m−l)}: the residual sources obey ω^R_iL^{k−1−i}‖s^c_i‖ ≤
C_BL·L^{−(1−θ)(k−i)}Σ_{l≤i<m}L^{−σ(m−l)}η² ≤ C_BL·L^{−σ}(1 − L^{−σ})^{−2}η²; the rough pieces' responses are
≤ CC_BL^{−(1−θ)(k−m)}L^{−σ(m−l)}η², summable over all l ≤ m < k for θ < 1, σ > 0; the top pieces V^{(l)}_k are data
shifts (Lemma TS) summing to ≤ C/(L^σ − 1). So **any σ > 0 suffices there, with NO coupling θ ≤ σ** — THETAW's
conclusion is true in that consumer, its condition is spurious, and its claim that the weakening "buys the entire
feasible region" is empty: the exponent of (W2) never constrained (α, θ) in the first place.
(d) *But (W2) is off lane A's critical path — THETAW's premise is STALE (systemic defect 2).* SPD itself, the carrier
bound |Q_str^{(l→m)}R^B_l| ≤ C_SPDκ_lL^{−3(k−l)}η² (= carried current ≤ C_SPDκ_lL^{−(m−l)}η², i.e. EXPONENT 1), is
PROVEN (BFT_A §13.6) and CONFIRMED (REVIEW_BFT_A_S3 l.25: "SPD: CONFIRMED as a bound on the carrier … It is not
(W2)"); and lane A's later route uses SPD only as a carrier bound and needs neither (W2) nor (SB) (BFT_A l.1546 "No
(SB), no (G♯-rough), no (W2)"; Theorem XB, Theorem CO-B, Corollary HL — REVIEW_BFT_A_S5 l.34 "Corollary HL: CONFIRMED
in its stated scope … It avoids (SB) entirely", l.212 "This bypasses 13.7's Gap 2 (SB) entirely"). The level sum there
is Σ_l(k−l+1)²L^{−(1−α)(k−l)} < ∞ — no factor k.
(e) *Where a level-count factor k does remain* is BFT_B's Corollary COF-crit (REVIEW_BFT_B_S9_S10 S10-6, l.503-548),
for the non-level-wise-co-closed part V_l of the BCH₂ rows (BFT_B l.3729-3736), outside lane A's HL scope. S10-6 states
"There is no choice of θ in (α, 1) that removes the factor"; what it needs is a level-decay input for V_l consumable by
Theorem COF (its class norm max_lL^{θ(k−l)}π_l(j_l) weights rows at birth — the one setting where THETAW's
"θ ≤ σ" form would be the right condition, but for a decay hypothesis on V_l that is not (W2) and that V_l does not
satisfy). That is a route question (a carrier-class version of COF, as lane A built CO-B), not an exponent question.
**Verdict for the lead: do not redirect the lane's main effort to "(W2) at some positive power".** For the BCH₂
carrier the exponent-1 estimate is already proven; lane A's live route does not use (W2); and the open k-factor is
not removed by any exponent choice.

**W10. "(W1)/(G♯-rough) does NOT soften: an irreducible ¼-per-level deficit remains at α = 0⁺" (l.375-383, F7) —
REFUTED (agree Codex F2), and stale.** BR-2 (iii) (BFT_A l.991) gives ‖J^c‖_∞ = L^{(1−α−θ)(k−l)}N against the target
CL^{−α(k−l)}N: the deficit is (1 − α − θ) + α = **1 − θ**, independent of α; the "¼" is 1 − α − θ evaluated at
(¼, ½) and then frozen while α varies. Its infimum over the window is 0. And (G♯-rough) is PROVEN anyway: Corollary
G♯R (= Theorem G♯-rough, all gauge-invariant outputs, m = 0) CONFIRMED on 0 < α < θ ≤ 1 − α (REVIEW_BFT_A_S5 l.31,
l.196) — which THETAW itself cites as PROVEN in its J3 row (l.188-190), contradicting its §T4.3.

**W11. "The θ question and the k-factor question are ONE question: a positive source weight is exactly what turns the
(k − 1) sum into a geometric one" (l.351-353) — REFUTED.** A positive source weight makes the class norm of
non-decaying rows LARGER (L^{θ(k−1)}, S10-6), it does not make their level sum geometric; S10-6 (CONFIRMED there)
optimises over θ and still gets ≈ 25(k−1). The level sum becomes geometric only through DECAY of what is summed (as in
CO-B via SPD), independent of θ. SESSION25_RESULTS's "CONVERGENCE: three independent lines now name (SPD)/(W2) as the
upstream item" rests on this sentence for its THETAW leg.

**W12. "The region is non-empty at d = 4 and EMPTY at every d ≥ 5; zero Wilson slack at d = 4" (§T5) — CONFIRMED
given the caps** (θ_A ≤ 1 hard, W8; θ_w^c ≤ 2 ARGUED): Wilson slack 4 − d. Agree with Codex F11's two qualifications:
the soft clause alone reads d < 4 + θ (so d ≤ 4 only for integer d); and "a restatement that gave the Wilson clause
slack at d = 4 … would be feasible at d = 5 as well" (l.425-427) is false as stated — slack s at d = 4 reaches d = 5 only
if s ≥ 1 (and the soft clause, r ≤ 2 + θ < 3, fails at d = 5 regardless).

**W13. Remaining THETAW items.**
- **Replacement text's "ω_l = L^{θ(k−l)} (l ≥ 1; ω_0 = 1)" (l.569) — REFUTED (agree Codex F3):** BFT_A BL-5 (c)
  (l.524-528) and [RBA2-fix] B6 (i) (l.844): "the (R) weight at l = 0 is ω^R_0 = L^{θk}, not 1" — with ω_0 = 1 the
  residual slot fails for every α > 0. The restatement needs slot-specific level-0 weights.
- **"One provably empty slot" (§T4.1, §T7.1) — REFUTED as "provably" (agree Codex F9):** [RBA2-fix] B2 (l.814-817)
  relabels BL-6 (b) "PROVEN on the linear side only"; the remainder side is "ARGUED (power count only)".
- **θ > 0 floor attributed to C_P (§T5 table, tw1_criteria) — REFUTED (agree Codex F14):** C_P(0) = L/(e ln L) is
  finite; the θ > 0 obstruction is Ω ≤ 1 + 1/(L^θ − 1).
- **"SF.md l.680 and RTARGET §33 l.588 should both read (0, 1)" (F2) — NOT-VERIFIED:** θ < 1 is consumed by lane A's
  route (C_P, BA-6); THETAW does not show that SF's or RTARGET's own routes consume it.
- **J5 (m_0 doing three jobs) — spot-checked:** REVIEW_S22 l.396 writes the norm weight as bare "m", l.399 quantifies
  "m_0", BFT-3/4 use m_0; flagged, not decided, as THETAW says.
- **Checks tw1 (agree Codex F6, F7, F14):** tw1-A's EMPTY is right (a common t ≤ 2 gives t + 2min(1, t−1) ≤ 4);
  tw1-B's 440 = Σ_{j=2}^{11} j(j−1) points, of which only 55 = Σ(j−1) sit on the cap tr = 2 + θ where the exponent is
  −θ (re-counted by hand); tw1-C cannot test the θ > 0 floor (at θ = 0, 0 < α < θ is already empty — tw1_feas.py
  l.84-92); tw1-D's EMPTY at d = 5 is over-determined (both Wilson and soft fail); tw1-G aborted on a float/Fraction
  mix; the boundary row "tr = 2: A = 1" that THETAW l.177-178 cites IS in tw1b_out.txt (Codex could not open tw1b),
  as is the false bracket "3^-1 > A > 3^-3/2" THETAW disclosed. tw1 criteria (born 21:40:33) preceded tw1_feas.py
  (21:41:25).

*(Errata to W9-W13 line references, checked by grep after writing: REVIEW_BFT_A_S5 "This bypasses 13.7's Gap 2 (SB)
entirely" is at l.215 (not l.212); THETAW's J3 row citing "Corollary G♯R is PROVEN at 0 < α < θ" is at l.191 (also
l.231), not l.188-190; tw1_feas.py's θ filter and α < θ test are at l.83 and l.90; BFT_A §13.7 runs l.1050-1066.)*

---

## C. Codex verdicts I used — agree / disagree, explicitly

**CODEX_REVIEW_TUNIF.md** (complete; "Review completed: 2026-10-28 22:09:33 UTC").
- F1 (TU-0/1/2 and periodic TU-3 CONFIRMED after the isolated-fibre attack) — **AGREE**; re-derived (U2-U5) and
  independently checked with symbolic twists (r55u_2).
- F10 (TU-3 needs explicit 2π-periodicity; exact non-periodic counterexample) — **AGREE**; the application satisfies
  it (LINEAR_PACKAGE l.263).
- F2 (tu1-D "unsatisfiable" excuse REFUTED; replacement gate cannot exclude a double pole) — **AGREE**; Codex's exact
  example hand-verified (8/21; 4/(7ε); growth 1000).
- F3 (m = 0 is the consumer's norm CONFIRMED; m > 0 "from the sup bound alone" REFUTED) — **AGREE**.
- F4 (mean-subtraction loses the whole factor 𝔠_0 at TUNIF l.392; harmonic mass L^{(d−1)n} not dL^{(d−1)n}) — **AGREE**.
- F5 (tu1-E cannot catch the concentrated correction) — **AGREE in logic**; the specific rationals were not re-run.
- F6 (TU-5/TU-6 NOT-VERIFIED; chain bridge a GAP) — **AGREE on every individual point, DISAGREE with the overall
  verdict**: the four items it left open are settled here — mean preservation (Q_str's column sums are constant,
  L^{1−d}; d∘h is exact: N4), the r_i locality import (LINEAR_PACKAGE l.235-236, Corollary N2-exp-b; U6(d)), the
  admissibility estimate (its own H_j bounds, re-derived and checked exactly: r55u_3), and the consumer substitution
  (NORMS §N6, which Codex was not permitted to read: U6(e)). Hence (T-UNIF) CONFIRMED-with-repairs, not NOT-VERIFIED.
- F7 (pre-registration chronology NOT-VERIFIED) — **PARTLY DISAGREE**: filesystem birth times settle tu1 (criteria
  precede script); tu1b is not demonstrable either way. **AGREE** on "six decades" = five and on floats in the D gates.
- F8 (PROOF citations drifted; 13.5 only at L = 3) — **AGREE** (they have drifted a further +4 since).
- F9 (symbol register: κ(η,η′) vs κ_±; two different μ's; T as torus side and as a trilinear form) — **AGREE**.

**CODEX_REVIEW_THETAW.md** (complete at re-read, 237 l.; unfinished at first read).
- F1 (σ > 0 derivation substitutes transport distance m − l by distance to the top k − l) — **AGREE** (W9 (a)). Its
  "most dangerous unverified point" (does L^{−σ(m−l)} decay for any σ > 0 yield a k-uniform estimate?) I answer: yes
  inside §13.7's implication, with no θ-coupling (W9 (c)) — but that implication is no longer on lane A's path (W9 (d)).
- F2 (the "irreducible ¼" is a stale evaluation; deficit is 1 − θ) — **AGREE**, and add: (G♯-rough) is PROVEN (W10).
- F3 (ω_0 = 1 in the residual slot) — **AGREE**.
- F4 (B4 retains θ ≤ 1 − α; ¾ is only the α = ¼ example; l.396-397 has no ¾) — **AGREE**.
- F5 (R_lin with residual-type sources at θ_w^r = 3 contradicts (C2)) — **AGREE**.
- F6 (only 55 of the 440 points have exponent −θ) — **AGREE**, counts re-derived by hand.
- F7 (controls tw1-C, tw1-D redundant; grid ≠ decision procedure) — **AGREE**.
- F8 (witness α = σ/2, θ = σ fails at σ ≥ 1 — "σ = 1 is already a counterexample") — **AGREE**, and it is immaterial to
  the existence of a witness (θ = min(σ/2, ½), α = θ/2 works); the substantive objection is F1 plus staleness (W9).
- F9 ("provably empty" overstates an upper-bound power count) — **AGREE**.
- F10 (strengthened residual leg not delivered; Σ-endpoint needs δ < θ) — **AGREE** (NOT-VERIFIED).
- F11 (reduced algebra CONFIRMED; "cannot clash" false; d < 4 + θ; slack ≠ d = 5) — **AGREE**.
- F12 (J6's two potential factors CONFIRMED; inventory NOT-VERIFIED) — **AGREE, and I close its NOT-VERIFIED part**
  by reading NORMS §N6 (W6).
- F13 (flat-holonomy counterexample to a global reading of (1c); verdict NOT-VERIFIED) — **AGREE with the
  counterexample; I go one step further**: (1c) as literally written (background potentials bounded by the curvature
  size ε) is REFUTED; only a reformulation on the displacement is viable (W6).
- F14 (abort, false bracket, C_P(0) finite) — **AGREE**; the tw1b output Codex could not open does contain the cited
  boundary row.

---

## S. Summary table — every claim reviewed in batch C8

| # | file / locating string | claim | verdict |
|---|---|---|---|
| 1 | NLOC "Lemma NL-0" | gauge ambiguity = admissible class; levels forced by level-0 gauge | CONFIRMED |
| 2 | NLOC §L3 | (N-loc) enters N1-15 only via the column ℓ¹ mass, T only via T^d cells | CONFIRMED |
| 3 | NLOC "Lemma NL-1" | torus spread-axial gauge, ≤ 4dR|dB| (2dR suffices) | CONFIRMED |
| 4 | NLOC "Lemma NL-2" | chain's constant mode c_j = L^{−(k−j)}c_k | CONFIRMED |
| 5 | NLOC "Theorem NL-3" (+ R_eff correction to NORMS N1-11) | 𝔠_P^tor ∝ T on the torus | CONFIRMED |
| 6 | NLOC "Corollary NL-4" | (N-loc) bypassed at fixed T (price T^{d+2}); open half = T-uniformity | CONFIRMED (given NQ-1) |
| 7 | NLOC "[NL-corr 1] Theorem NL-3′" | T-free 𝔠_P^♭ via NL-1 + line sums; NL-4 drops to T^d | **REFUTED** (proof invalid; r55u_1) |
| 8 | NLOC l.242 "T⁶ ≈ 4.7·10⁴³" | number | **REFUTED** (4.68·10⁴²) |
| 9 | NLOC "Proposition NL-7" | global axial gauge fails by a factor T | NOT-VERIFIED (lower bound on Φ unproven) |
| 10 | NLOC "Proposition NL-9" | near/far trade not available (as a no-go) | NOT-VERIFIED (one construction priced) |
| 11 | NLOC "Lemma NL-10/NL-11", "Theorem NL-12" | untwisted divisions; local gauge splitting | CONFIRMED (spot re-derivation) |
| 12 | NLOC l.590 | what is left is "one lemma, not a programme" | CONFIRMED (TU-2/TU-3 is it) |
| 13 | NLOC l.580-584 | (N-loc-cell) ⇔ "the line fluxes … vanish" | **REFUTED** (Ω ≠ 0; absorbed, not verified) |
| 14 | NLOC §L7 route 1 | Theorem RW cannot glue representatives | NOT-VERIFIED (sound argument, not a no-go) |
| 15 | TUNIF "Lemma TU-0" | three twisted identities | CONFIRMED |
| 16 | TUNIF "Lemma TU-1" | division bound κ(η,η′) | CONFIRMED |
| 17 | TUNIF §U4.4 | first obstruction absorbed by spread b̂_1 = −μ/L^k | CONFIRMED |
| 18 | TUNIF "Lemma TU-2" | Φ ≡ 0 for every closed F̂, d ≥ 3, ν_γ not a zero divisor | CONFIRMED (r55u_2) |
| 19 | TUNIF "Theorem TU-3" | closed ⇒ D∧b̂, |b̂| ≤ 2(1+κ)L^k|F̂| | CONFIRMED with periodicity added (Codex F10) |
| 20 | TUNIF "Corollary TU-4" | (N-loc-b′) at level 0, rate η′ < m_*′ | CONFIRMED (import quoted correctly) |
| 21 | TUNIF "Corollary TU-5" | (N-loc♯) with 𝔠_L free of j, k, x, T | CONFIRMED (T-freeness) |
| 22 | TUNIF l.377-392 | the displayed 𝔠_L (mean term dc_η′ etc.) | **REFUTED** (missing 𝔠_0; unbudgeted correction) |
| 23 | TUNIF "Theorem TU-6" | (T-UNIF): N1-15 uniform in k AND T | **CONFIRMED** (conditional on (N-Q); after R1-R7) |
| 24 | TUNIF TU-6 / Codex TU-6 obligation | cell-1-form admissibility ⇒ chain admissibility | not automatic; separate step, DISCHARGED — CONFIRMED |
| 25 | TUNIF l.183, l.208 | m > 0 T-free "from nothing but the sup bound" | **REFUTED** (Codex F3) |
| 26 | TUNIF (Q3) | the consumer's norm is m = 0 | CONFIRMED |
| 27 | TUNIF [TU-corr 4] | (N-loc-b) literal not delivered; (N-loc-b′) is what's consumed | CONFIRMED |
| 28 | TUNIF [TU-corr 1], [TU-corr 2] | (N-loc-cell) discharged; "T-uniformity open" superseded | CONFIRMED (given N-Q) |
| 29 | TUNIF §U6 (i) | 2M_n/n = 16 + 4/n ≤ 20 | CONFIRMED (arithmetic) |
| 30 | TUNIF l.543-546 | tu1-D "unsatisfiable by the truth" | **REFUTED** (Codex F2) |
| 31 | tu1b_criteria / TUNIF §U7 | tu1b-D certifies a simple pole | **REFUTED** (double pole passes; floats) |
| 32 | TUNIF l.537 | tu1-E "would have caught" U-F2 | **REFUTED** (Codex F5) |
| 33 | tu1_criteria "Written … before" | tu1 pre-registered | CONFIRMED (birth times; header clock wrong) |
| 34 | TUNIF l.426-427 | cheaper than GREENT "at any T above ≈ 10⁹" | **REFUTED** (crossover ~10^{2xx}) |
| 35 | TUNIF l.226-227 | "'Volume-uniform' occurs 162 times" | **REFUTED** (23) |
| 36 | THETAW §T1 | six jobs; three written as one θ_w | CONFIRMED |
| 37 | THETAW §T2/§T7.1 | the decoupling is faithful (no forced identity) | CONFIRMED |
| 38 | THETAW §T4.1 | decoupled system satisfiable | CONFIRMED (formal; witness (2,1,5/2,½,¼)) |
| 39 | THETAW §T4.2 | A = 1/3 on data | CONFIRMED |
| 40 | THETAW l.305 | R_lin incl. residual-type sources at θ_w^r = 3 | **REFUTED** (Codex F5) |
| 41 | THETAW l.322-336, F6.2 | A = L^{−θ} full; 1/3 an unattained infimum | NOT-VERIFIED (ARGUED; endpoint; symbol collision) |
| 42 | THETAW l.203-206 | four windows = three on J3 + one on J2 | CONFIRMED (J2 requirement is > 2, not = 3) |
| 43 | THETAW l.205, l.522 | "constraints on different variables … cannot clash" | **REFUTED** ((C2) couples them) |
| 44 | THETAW §T1, J6 | θ_A consumed twice per cubic vertex; missing from BFT-1's text | CONFIRMED |
| 45 | THETAW F1 "(1c)" | admissible representative with potentials ≤ C_0L^{−(k−j)}ε | **REFUTED** (flat holonomy) |
| 46 | THETAW J3 | θ ≤ 1 − α is not a proven constraint | CONFIRMED |
| 47 | THETAW l.200-201, F5 | the ¾ ceiling is superseded by B4 | **REFUTED** (Codex F4) |
| 48 | THETAW J1, J6 | θ_A ≤ 1 hard; θ_w^c ≥ 2 forced at d = 4 | CONFIRMED |
| 49 | THETAW §T4.3, F7 | σ > 0 suffices for (W2)/(SPD); it is the open target | **REFUTED** as stated/derived/used (W9) |
| 50 | THETAW l.380, l.715 | irreducible ¼-per-level deficit for (W1) | **REFUTED** (deficit 1 − θ; G♯R proven) |
| 51 | THETAW l.351 | θ question = k-factor question | **REFUTED** (S10-6) |
| 52 | THETAW §T5 | empty at d ≥ 5; zero Wilson slack at d = 4 | CONFIRMED (given the caps) |
| 53 | THETAW l.425-427 | Wilson slack at d = 4 would make d = 5 feasible | **REFUTED** (needs slack ≥ 1) |
| 54 | THETAW l.569 | ω_0 = 1 in the replacement | **REFUTED** (Codex F3) |
| 55 | THETAW §T4.1/§T7.1 | one PROVABLY empty slot | **REFUTED** (remainder side ARGUED) |
| 56 | THETAW §T5, tw1_criteria | θ > 0 floor from C_P | **REFUTED** (C_P(0) finite) |
| 57 | THETAW F2 | SF l.680, RTARGET l.588 should read (0, 1) | NOT-VERIFIED |
| 58 | THETAW §T6 | tw1-B exponent = −θ; tw1-C/D controls certify their claims | **REFUTED** (55/440; redundant controls) |
| 59 | tw1_criteria born 21:40:33 | tw1 pre-registered | CONFIRMED |

**Counts: CONFIRMED 32 · NOT-VERIFIED 5 · REFUTED 22.** Of the 22 REFUTED, the load-bearing ones are #7, #13, #22,
#40, #43, #45, #47, #49, #50, #51, #54; the rest are numbers, check records and wording.
Spot-checked only (not counted as re-derived): #10, #11, #14, #29's surroundings (§U6 (ii)-(iv)), the §U4.7 constants.

---

## L. For the lead: what this changes in PROOF.md's tally and HANDOFF's critical path (written 2026-10-28T22:53:28Z UTC)

1. **Theorem N1-15 is uniform in k AND T at its scope — (T-UNIF) CONFIRMED, conditional on (N-Q) = Theorem NQ-1.**
   Ledger row: "CONDITIONAL on (N-Q) only; uniform in k and T; d = 4, trivial background, abelian/linearised", with
   𝔠_L recomputed per (R1)-(R7) (U6). (N-loc), (N-loc-b), (N-loc-cell) may be closed with a pointer to TUNIF §U4 + this
   review, (N-loc-b) restated as (N-loc-b′) (decay + the explicit constant mode). HANDOFF's item "what is actually open
   is uniformity in T" is superseded for the (N-loc) route. If REVIEW55_NORMS refutes NQ-1, N1-15 reverts to
   "CONDITIONAL on (N-Q)" — TU-5's levels j ≥ 1 use ‖Q^j‖ ≤ 𝔮_0L^j; nothing else here changes.
2. **Do NOT land NLOC's FOR OTHER FILES item 1 ("replace Lemma N1-11's 𝔠_P by 𝔠_P^♭ of Theorem NL-3′").** NL-3′ is
   REFUTED as proven (N7). The T-free sup bound comes from TUNIF TU-4/TU-5 instead. Any record of "N1-15 at fixed T
   costs T^d ≈ 2.8·10²⁸ (via NL-3′)" should read T^{d+2} (NL-3) — or, better, T-free (item 1).
3. **Do NOT redirect the lane's main effort to "(W2)/(SPD) at some positive power".** THETAW's σ > 0 claim is REFUTED
   as stated, derived and used (W9): wrong hypothesis (Codex F1), witness fails at the original σ = 1 (Codex F8), and
   STALE — SPD at exponent 1 is PROVEN and CONFIRMED in carrier form (BFT_A §13.6; REVIEW_BFT_A_S3 l.25), (W2) = SPD +
   (SB), and lane A's live route (Theorem XB, Theorem CO-B, Corollary HL; CONFIRMED in REVIEW_BFT_A_S5) needs neither
   (W2) nor (SB). **HANDOFF critical-path item 5's sentence "The missing input is lane A's (SPD)/(W2), OPEN" is
   mislabelled:** what COF-crit (REVIEW_BFT_B_S9_S10 S10-6) lacks is a level-decay / carrier-type input for the
   non-level-wise-co-closed part V_l of the BCH₂ rows that Theorem COF can consume — a route question (cf. how CO-B
   consumed SPD), not an exponent question; S10-6 itself shows no θ removes the factor. SESSION25_RESULTS's
   "CONVERGENCE: three independent lines now name (SPD)/(W2)" rests, on its THETAW leg, on the refuted W11 sentence.
4. **THETAW's append-ready BFT restatement (its F1) must not be landed as written:** (1c) is false at its literal
   reading (flat torus holonomy, W6) and must be stated for the displacement X relative to Z^lift; ω_0 must be
   slot-specific (ω^R_0 = L^{θk}, W13); R_lin is data-only (W4); keep "θ ≤ 1 − α (ARGUED, lane A's route)" in the
   window rather than dropping it (W7); the "A = L^{−θ}" sentence is ARGUED with an endpoint caveat (W4). What CAN be
   landed: the decoupling itself (θ_w^c, θ_w^r, θ_A and the source weight θ as separate symbols) — faithful (W2) and
   satisfiable (W3) — and "exponents pinned in the data, constants existential".
5. **PROOF.md [S25-fix 3] / NBG_B NB7: "α ≤ θ ≤ 1 − α ≤ ¾" misquotes BFT_A** (the ¾ is B4's example at α = ¼; the
   ceiling is 1 − α, sup 1). [S25-fix 3]'s own conclusion — decouple the four exponents — stands.
6. **N1-15's A_soft = 1/3 is unaffected** by THETAW's "A = L^{−θ}" re-reading (different object; W4).

(T-UNIF): CONFIRMED
σ > 0 suffices for (W2)/(SPD): REFUTED — as THETAW states, derives and uses it (transport distance m−l replaced by
distance to the top k−l; witness fails at the original σ = 1; premise stale). The bare exponent fact — in the one
consumer that ever used (W2)-type decay (BFT_A §13.7), any σ > 0 suffices with no θ-coupling — is true by my
re-derivation (W9 (c)) but has no live consumer, so it is no ground to redirect effort.

**Cross-reference (appended 2026-10-28T22:54:13Z UTC, after the two verdict lines; it changes neither).** REVIEW55_NORMS.md, being
written concurrently, records r55n-E1 "Theorem NQ-1 … CONFIRMED (re-derived)" and r55n-A4 "Theorem N1-15 … CONFIRMED as
a CONDITIONAL theorem". If both stand, the one condition on (T-UNIF) above is met: Theorem N1-15 (sup-form N3, d = 4,
trivial background, abelian/linearised) is uniform in k and T with no open named input inside that scope, (N-bg) and
(H-C)'s C_♭ clause on the small-field class remaining untouched. Its r55n-A5 (THETAW's A = L^{−θ} REFUTED as a statement
about N1-15's A_soft) and r55n-D1 (the requirement is θ_w^r > 2, not = 3) agree with my W4 and W5 (a).
