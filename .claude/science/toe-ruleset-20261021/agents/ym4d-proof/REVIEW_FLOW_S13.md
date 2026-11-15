# REVIEW_FLOW_S13: hostile review of lane C session 13 (FLOW.md §103-§110, the [RFL12-fix] edits and check f16)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f16*. This file is the only file I edited in
the repo. No commits, PRs or pushes. No git command was run.

Inputs (read-only):
- $L/DRIVE_BRIEF-equivalent process rules; HANDOFF.md (all).
- FLOW.md §103-§110 (l.4541-4851) in full; §98-§102 (l.4440-4539); every [RFL12-fix] site; §30 (l.1444-1578), §37 (C1)-(C3)
  (l.1888-1977), l.1548, l.3003-3012, l.3738-3750, l.3835, l.3954, l.4015, §99 (l.4467-4490).
- REVIEW_FLOW_S12.md (all), REVIEW_FLOW_S9.md (tally and conditional convention).
- PROOF.md l.6600-6660 (the BFT re-pointing and the CROSS-LANE STATUS map).
- FLOW_LOG.md l.562-627 (session 13).
- checks: f16_criteria.md (all), f16_cartan_slice.py (all; Part A map construction, `w_nat`, `closed_forms`, Part B
  accumulators and the B4 closed form read line by line), f16_out.txt (all), f16_time.txt.

Line numbers below are FLOW.md lines as of this review (FLOW.md md5 **ff470b2a32b3523aa90b350393198400**, 539577 B — identical
to the final stat FLOW_LOG records for 11:59:32 UTC).

---

## Bottom line

- **Session 13 IS complete.** The "stopped mid-run" worry does not materialise. §103-§110 is a closed unit: every pre-stated
  item (X1)-(X6) is dispositioned, the f16 verdict arithmetic reconciles exactly (21 pre-stated lines, 19 PASS; 31 lines in
  all, 28 PASS), and every number quoted in §104-§109 matches checks/f16_out.txt — **with two exceptions** (S13-1): one
  misquoted digit, and one pair of numbers quoted from a smoke run that exists in no artifact.
- **Provenance: CLEAN** on everything I can check (sizes and md5s of all four f16 artifacts and of FLOW.md re-verified; the
  §103-first-edit byte accounting reconciles to 3494 B of [RFL12-fix] insertions). **One claim is now unverifiable**: the log
  says the pre-statement bytes can be restored by reverse-applying flow13/fix_s12*.py, but that scratchpad is gone (S13-2).
- **The Cartan restriction is NOT a dodge, and I say so plainly.** c^tot_n is *defined* at a constant Cartan background
  (l.3835), Lemma F-Π (i) supplies the exact colour reduction (l.1548), and §99's (T-a) was already a Cartan-plane-wave
  statement before session 13 (l.3369, 3516, 3786, 3967, 4115, 4263). Session 13 does not report a measure-zero case as
  progress on a general statement. **But §103-§110 never says why Cartan suffices** — a reader of the session alone cannot
  tell (S13-4). The root-sector linearisation does diagonalise exactly what it claims (S13-5).
- **SLICE-U is stronger than the file claims, not weaker.** Its clause (a) — the algebra that removes the d∘h growth from the
  T-split — holds at EVERY U, because FLOW l.3738 already has the gauge covariance "for every U at which 𝔪_n is defined".
  §106 cites only the Cartan case (S13-6).
- **"Pairing at U = 1 grows" does NOT degenerate the decomposition at the trivial field.** I went at this head-on. At ε = 0
  exactly, VC-T0 holds and f16's own diagnostic gives the exact L^{-2} ratio (c_0 = 1.1111e-1, 1.2346e-2). What grows is a
  term in the ε-expansion *about* U = 1 taken with the frozen U = 1 slice — an ε² bookkeeping artefact of a bad slice choice.
  And PROOF.md l.6633's "FLOW BFT-2, 3 at the trivial field" is what FLOW *consumes* from BFT, not a place where SLICE-U must
  hold. **The damaging finding is not there** (S13-7).
- **One real gap in a PROVEN proof.** §105 (c), the chain half of the exact covariance, needs avg_T N_T = avg_T N̄_T, which does
  NOT follow from the pointwise identity it cites. It follows from the maximiser's Lagrange condition, already recorded in
  FLOW at l.3010. Reviewer numerics: at a non-stationary φ the two averages differ by 0.137; at the maximiser they agree.
  The statement is TRUE; the proof is incomplete for N ≥ 3 (S13-8).
- **"PROVEN given (Π-loc)" is labelled in two places out of four.** §110's Outcomes line and FLOW_LOG carry it; §107's HEADING
  and §110's TALLY line do not. The house convention (REVIEW_FLOW_S9 l.371) counts such items but carries the label in the
  tally. There is no "FOR OTHER FILES" section in FLOW.md, so the only propagation path is PROOF.md's cross-lane map, which
  quotes the latest review — this file (S13-10). (Π-loc)'s one-line argument covers its colour clause only (S13-11).
- **§107 (d) over-normalises.** (c) proves the sharp first-order form with λ̃(K)λ̃(K+P), exactly as §99 [S12-4]'s (T-a2)
  specifies. (d) then states the rate only after Ñ_r = N_r², which is λ̃-degree 12 at r = 1 and 30 at r = 2, where degree ≤ 4
  is what the product actually needs. As written, the r = 2 claim permits |K|^{-30} blow-up at small K — and f16 tested no
  small K at all (S13-12, S13-15).
- **B3 and B4 FAILED as pre-registered, and that is reported correctly.** The post-hoc passes are labelled post-hoc, and even
  add1-B4 is reported as a FAIL. The step-size diagnosis is quantitatively right for B4 (δ⁴ to 0.8%), and I verified the
  7.46× field amplification myself. **But the criteria were arithmetically unachievable as written**: the criteria's own
  "error O(δ⁴)" at the pre-stated δ = 0.02 already exceeds the 1e-7 threshold before any amplification. The FAIL was
  determined at pre-registration, not by the physics (S13-13). B3's diagnosis, unlike B4's, has no scaling test (S13-13).
- **The 0.107 shrink is thin and nothing rests on it.** One ratio per order, SU(2) only, on a level-n torus (3,3,1,1) whose
  directions 3 and 4 are a single site — 6 momenta, all with λ̃ ∈ {3, 6}. §107 (b) derives the L^{-i} bound analytically from
  §106 (c) by a Cauchy estimate, which I re-derived; the numerics are corroboration only (S13-15).
- **Corrected tally: 75 PROVEN-HERE (claimed 75); strict 70 (claimed 70) — CONFIRMED**, provided the conditional and scope
  labels of S13-10 are attached.
- **(T-a1) moved, by about half, conditionally.** (T-a2) is closed at the orders needed. See §11.

---

## 0. Numerics (reviewer)

- **No NUMERIC LOCK was taken and f16 was NOT re-run.** Per the handoff's numerics rule ("prefer not to run numerics at all
  this session unless your result genuinely depends on one — eight agents are sharing one slot"), I judged that none of my
  findings depends on re-running a 65 s / 548 MB numpy job. **Consequence, recorded as a limitation:** unlike session 12,
  where the reviewer re-ran f15 and obtained a byte-identical output, **the reproducibility of checks/f16_out.txt is not
  independently confirmed here** (S13-19). I did read f16_cartan_slice.py line by line instead, and I checked that the B4
  comparison is not vacuous (the "closed form" at script l.455-457 is coded independently of the finite-difference operator
  P1 it is compared against) and that `w_nat` for N ≥ 3 (script l.180-193) iterates to the true SU(N) stationary point
  ("anti-hermitian part of V^{-1}M central"), not merely the polar part — which is the map §104/§105 prove about.
- **What I did run:** one plain-python script (`math`, `cmath`, `random` only — no numpy, no BLAS, < 1 s, trivial memory), in
  my own scratchpad `revflow13/chk.py`. Under the rule "exact rational/symbolic arithmetic in plain python (no BLAS) is cheap
  and does not need the lock". Results used below:
  - ε_n/ε = sin(P/2)/sin(P/2ℓ) at L = 3, n = 2, P = 2π/3 = **7.4598** (§109's "≈ 7.5"); field step at δ = 0.02 = **0.1492**
    (§109's "0.15"); ε_n/(εℓ) = 0.828862 against sin(P/2)/(P/2) = 0.826993 (the (X2) (c) 1 + O(P²/ℓ²) claim).
  - max over P ∈ (0, π], i ≤ 5 of ρ_i/((π/2)L^{-i}) = **0.9995** — the §104 bound ρ_i ≤ (π/2)L^{-i} holds and is tight.
  - δ-scaling of B4: 0.02 → 0.002 gives the factor **1.008e4** against δ⁴'s 1e4; 0.002 → 0.0005 gives **146.7** against 256.
    The δ required for < 1e-7 from the observed coefficient is **0.0019**.
  - The stationarity question of S13-8, on a seeded SU(3) toy (h = (0.7, −0.2, −0.5), 40 random contour angles): at the
    maximiser, Im r_k = (−1.78160e-4, −1.78231e-4, −1.78145e-4) (equal to my optimiser's floor) and |avg N − avg N̄| = 1.4e-7;
    at a φ perturbed off the maximiser by (0.05, −0.02), |avg N − avg N̄| = **0.137**.
- Nothing was written to checks/. No lock directory was created or removed. No process left running.

---

## 1. Priority 1: completeness, provenance, [RFL12-fix]

### 1.1 Is session 13 complete and internally consistent? (S13-1) — **CONFIRMED-WITH-FIX**

HANDOFF.md l.92-96 says FLOW session 13 was stopped during its f16 smoke run and that everything after the [RFL12-fix]
entries is unfinished; l.124-133 supersedes that. I checked the supersession rather than trusting it.

| Completeness test | Result |
|---|---|
| Every pre-stated item (X1)-(X6) dispositioned in §110 | ✓ (X1) DONE, (X2)-(X5) PROVEN with scope, (X6) = the remaining list |
| Every §103 failure mode S13-F1..F6 adjudicated | ✓ §109 Reading (1): F1-F4 do not occur; F5, F6 FAIL as recorded |
| Pre-stated verdict count | ✓ Part A 16 (SU(2) 6 + SU(3) (1,2) 6 + SU(3) (1,3) 4) + Part B 5 = **21**; 19 PASS |
| Total verdict lines | ✓ 21 + add1 5 + add2 5 = **31**; 28 PASS, matching f16_out.txt's own SUMMARY |
| Forward references to unwritten results | ✓ none left: the three [RFL12-fix] forward tags (l.4416, 4487, 4515) point at §108, which exists |
| Dangling section references | ✓ §98 (a), (b), §97, §104 (b), (c), §106 (a), (c), §107, §30, §37, LINEAR_PACKAGE §1.2, BFT_B §15 all exist — one is mis-numbered, see S13-9 |
| Artifacts named in §109 all present | ✓ f16_criteria.md, f16_cartan_slice.py, f16_out.txt, f16_time.txt |
| Claims an output the check did not produce | **two defects, below** |

**Defect (i), a misquoted number.** §106 Reading (4) (l.4730-4731): "With the U = 1 pairing, the data [ε]A^{(i)} = [ε]Q'^{(i)} do
not decay (**2.92** → 2.95)." f16_out.txt prints `||[e]A^(1)|| = 2.8916e+00, ||[e]A^(2)|| = 2.9528e+00`. The first figure is
**2.89**, not 2.92. The conclusion (no decay) is unaffected.

**Defect (ii), an orphaned pair of numbers.** The logged statement change at l.4719-4722 says: "f16 does not show L^{-i} decay
at i ≤ 2: on the official torus the piece vanishes (8e-16, 2e-14), and on the **(3, 3, 2, 1) smoke torus it is 1.99e-2 →
2.46e-3 (ratio 0.12)**." The first pair is in f16_out.txt (8.2418e-16, 2.3932e-14 ✓). The second pair is from smoke 3, whose
output is **in no committed artifact and is not recorded in FLOW_LOG** (FLOW_LOG l.600-603 records smoke 3's B1-B4 verdicts and
its 1.03 GB peak, but not these two numbers). This is the one place in §103-§110 that quotes a result the committed check did
not produce. It is used to justify a WITHDRAWAL, i.e. in the conservative direction, and the quoted ratio 0.1236 is ≈ L^{-2},
i.e. *faster* decay than the withdrawn clause claimed — so the withdrawal is right either way. It still has to be fixed.

Note on the withdrawal itself: it is correctly handled. The clause is struck in place with a "**Statement change (logged)**"
block, the reason is given, the log records it as the only statement change after §103, and the honest reading ("only an
upper bound is proved") is stated. ✓

### 1.2 Provenance (S13-2) — **CONFIRMED**, with one unverifiable claim

| Event | Claimed (FLOW_LOG) | My check | Verdict |
|---|---|---|---|
| §103 = first edit | 11:35:42 UTC, FLOW.md 517091 B, md5 0acac88f…; `ls checks \| grep -c '^f16'` = 0 at 11:34:38 | byte accounting below | ✓ consistent |
| [RFL12-fix] after §103 | 11:36:52, 11:37:08 (16 + 8 replacements) | 24 `RFL12-fix` sites present, all 9 fixes (§1.3) | ✓ |
| f16_criteria.md before any script | born = mtime 11:39:15, 4580 B | `stat` 4580 B ✓; md5 088a6b1d… | ✓ |
| f16_cartan_slice.py | born = mtime 11:54:59, 25561 B, md5 7c81a91bfff45189e025be6b22547cca | `stat` 25561 ✓; `md5` **7c81a91bfff45189e025be6b22547cca** ✓ | ✓ |
| official run | 11:55:17-11:56:22, load 3.03, mem free 38%, nice 10, 1 thread, 65.35 s, 548 MB | f16_time.txt = `65.35 real … 548126720 maximum resident set size` ✓; f16_out.txt 6137 B ✓ | ✓ |
| §104-§110 | 11:59:32, FLOW.md 539577 B, md5 ff470b2a… | `stat` 539577 ✓; `md5` **ff470b2a32b3523aa90b350393198400** ✓ | ✓ |

**Byte accounting for the first-edit claim.** In the current file §103 runs from byte 510290 (start of l.4541) to byte 520585
(end of l.4629). FLOW_LOG records 517091 B at 11:35:42, immediately after the §103 append. The difference is **3494 B**, which
must be exactly the net bytes the [RFL12-fix] edits added *before* §103. The 24 bracketed tags total 3153 UTF-8 bytes, one of
which (l.4775) sits in §108 and so does not count, and the S12-1 sign correction plus the eight fix_s12b rewordings add the
rest. 3494 against ~3100 of tag text plus rewordings is consistent. The ordering claim — §103 first, then the fixes, then the
criteria, then the script, then the run, then the proofs — is therefore corroborated and nothing contradicts it.

**What I could NOT verify (NOT-VERIFIED).** FLOW_LOG l.584 asserts: "Reconstruction: reverse-applying fix_s12b.py then
fix_s12.py to FLOW.md restores the 11:35:42 bytes." REVIEW_FLOW_S12 performed exactly that reconstruction for §94 and got the
recorded md5, because flow12/ still existed. **flow13/ no longer exists on this machine** (I looked under every
`/private/tmp/claude-50*/*/*/scratchpad/`), so the §103 pre-statement cannot be byte-reconstructed by any reviewer, now or
later. This is not an accusation — the stat chain is consistent — but the session asserts a reproducibility that is no longer
reproducible. Recommend the lead require the replacement scripts, or at least their md5s and pair counts, in the lane dir.

### 1.3 [RFL12-fix] S12-1..S12-9 (S13-3) — **CONFIRMED**, one formula slip in a tag

| Fix | Sites found | Content check | Verdict |
|---|---|---|---|
| S12-1 (sign of Φ^T_k − Φ^L_k) | l.4394 | "both signs corrected (they were reversed); by Jacobi log det_⊥Ỹ = log det Y + …" | APPLIED, correct |
| S12-2 (FALSE for Y_n only; Schur; soft-chain named) | l.4280, 4416, 4487, 4515, 4537 (+ the §108 title l.4775) | all three sub-requirements present at l.4280, including "read 'every block map in the soft chain of COV-str'" | APPLIED; **formula slip**, below |
| S12-3 (l.839's Π and P_⊥) | l.4400 | "read Π := P_n(P_n𝒞_nP_n)^{-1}P_n, and l.839's 'P_⊥' as the LEVEL transverse projector P_n" | APPLIED, correct |
| S12-4 ((b) is a U = 1 identity; (T-a) → (T-a1) + (T-a2)) | l.4447 (§98 Reading (1)), l.4473 (§99) | both halves present, with the λ̃(K)λ̃(K+P) normalisation and the P_{T,ℓ} non-analyticity | APPLIED, correct |
| S12-5 (uniformity is of the difference) | l.4446 | "applies to the DIFFERENCE Ỹ̂_n − Ỹ̂_∞; the symbol itself is ~\|K\|^{-2}" | APPLIED, correct |
| S12-6 (q → −q with D and F both flipping) | l.3976, 4265, 4365 | the §84 (U6) site l.3976 tagged "superseded by −2iq_αF_{μν} with D = ∂ + iq_αa" | APPLIED, correct |
| S12-7 (A1c is a weak control) | l.4371, 4497 | "a WEAK control: at this background the spin term is ≈ 1% of the Hessian" at both sites | APPLIED, correct |
| S12-8 (forward refs; log the factor-2 slip) | l.4082, 4156; FLOW_LOG l.585-586 | both re-tagged "(forward reference, written … before those proofs: see §96, §98)"; the log carries the separate `[RFL12-fix S12-8] (record)` entry calling the extra factor 2 "a mathematical slip in the proof draft, not a wording correction" | APPLIED, correct |
| S12-9 (𝔪_n form factor off the wall list) | l.4476-4477 | "it is Lemma Cartan-𝔪 (§103 (X2), pre-stated; proof follows), exact for 𝔪^{S4'} and through second order for the chain map" | APPLIED, correct |

**The slip.** The S12-2 tag at l.4281-4282 writes the Schur bound as `W_n(K) ≤ 1/(κ^{-1}[1 + (n − 1)λ̃(K)/8] − C(K))`. §108
(l.4782) writes `… − κC(K)²`, which is the correct one: Y_VTY_TT^{-1}Y_TV ≤ ‖Y_TT^{-1}‖·|Y_VT|² ≤ κC(K)². The tag's version
drops both the κ and the square. Harmless (§108 governs), but the tag is the text a later reader meets first.

---

## 2. Priority 2: the Cartan restriction — how much of (T-a1) actually moved

### 2.1 Is the Cartan case a genuine reduction? (S13-4) — **CONFIRMED as a reduction; NARROWED by a missing citation**

I expected to find a measure-zero special case reported as progress on a general statement. It is not that, and I will not
manufacture the objection. Three independent facts, all upstream of session 13:

1. **The target is defined at a Cartan background.** l.3835: "U_f (constant Cartan flux) that **DEFINES** c^tot_n :=
   [f²]total_n(U_f)". The quantity the coupling flow needs is the f² coefficient at a constant Cartan curvature, not a
   quantity at a generic SU(N) configuration.
2. **The colour reduction is exact and proven.** l.1548: "Colour reduction (exact): by Lemma F-Π (i) β can be read along one
   Cartan direction; for a Cartan-valued U_0 every B_k is Cartan valued (M̄ of commuting transports is in the torus, and W_♮ of
   a torus element is in the torus by uniqueness)". Lemma F-Π is counted PROVEN-HERE at l.521.
3. **(T-a) was already a Cartan-plane-wave statement before session 13.** The lane's plane wave is H_1 ε cos(px_2 + ϑ) on the
   1-links throughout: l.3369, 3516, 3786, 3967, 4115, 4263. §99's (T-a) "plane-wave vertex symbols" (l.4470-4477) inherits
   that convention, and [RFL12-fix S12-4]'s (T-a1)/(T-a2) keep it.

So the answer to the hostile question is: **(T-a1) is a Cartan-plane-wave statement by construction, and session 13 proves
part of it at exactly that background. No over-claim on this axis.**

What IS wrong: §103-§110 never states any of this. §103's notation block (l.4548-4549) merely *defines* a Cartan
configuration; §110 never says why the Cartan restriction is adequate. A hostile reader of the session in isolation — which
is how the next reviewer and PROOF.md's map will meet it — has no way to tell a reduction from a dodge. **Fix:** one sentence
in §110 citing Lemma F-Π (i) (l.1548) and the c^tot_n definition (l.3835).

There is one real residue, and the file does not mention it either: the reduction is to **a constant Cartan flux**, not to a
Cartan plane wave. Getting from one to the other is (T-c), which is OPEN. Until (T-c), nothing proved in §107 reaches c^tot_n.
I return to this in §12.

### 2.2 Does the root-sector linearisation diagonalise what it claims? (S13-5) — **CONFIRMED**

At a Cartan U, Ad(exp(cH_1)) acts on e_{ij} by e^{iqc} (§105 proof, l.4667). The torus action therefore assigns distinct
weights to the Cartan subalgebra (weight 0), to each root pair, and to φ versus φ̄ within a pair. Any torus-equivariant
real-linear map — and T(U) is one, since 𝔪 commutes with the torus action on Cartan arguments — preserves each of these.
Hence:
- the root sectors do not mix with each other or with the Cartan sector: correct, and §105 (a) says so ("the root sectors
  decouple by torus equivariance", l.4670);
- T(U) acts **complex**-linearly on φ (no φ̄ term): correct, and used implicitly throughout without comment;
- f16 A2 tests the closed forms against central differences of the **full nonlinear maps** with random complex φ on all fine
  links, at SU(3) with two roots having h̄ ≠ 0 (q = 0.9, h̄ = 0.25 and q = 1.2, h̄ = 0.1). Sector mixing would show there. It
  does not: 2.37e-10 / 2.66e-10 / 2.78e-10 (chain), 6.95e-10 / 7.62e-10 / 7.69e-10 (S4'), against a 1e-7 threshold, with the
  naive-average control failing at 7.2e-2 … 8.95e-2.

**Are the non-Cartan directions "controlled or simply absent"?** Absent — correctly. The *background* is Cartan by the §2.1
reduction, so there are no non-Cartan background directions to control. The *fluctuations* do cover every direction, and here
there is a real omission: §103-§110 treats one root sector and never mentions the **Cartan-sector fluctuations** at the same
background. That omission is justified upstream (§37 [RFL5-fix S5-5] l.1968: at a Cartan background the Cartan-sector
fluctuations are neutral and carry no universal log ℓ; §44 (e) l.2256: "the Cartan sector contributes nothing") but is not
cited in §103-§110. Same fix as §2.1.

---

## 3. Priority 3: Lemma Cartan-𝔪 (§104) and Lemma Cartan-T (§105)

### 3.1 Lemma Cartan-𝔪 (S13-20) — **CONFIRMED**, with a mis-citation

I re-derived (a), (b), (c).

- **(a)** At Cartan U, S_c^{-1}T = exp(δ_TH_1) with eigenvalues e^{ih_kδ_T}; on D′ the principal log is δ_TH_1, so the S4'
  average is δ̄H_1 and U′ = exp((avg_Tθ_T)H_1) with avg_Tθ_T = (Q_root a). Exact and inductive. ✓
- **(b)** The equivariance step is right: W_♮(tMt^{-1}) = tW_♮(M)t^{-1} for the *unique* local maximiser; M̄ = diag(m_k) is fixed
  by the full diagonal torus 𝕋, so W_♮(M̄) ∈ Z_{SU(N)}(𝕋) = 𝕋. ✓ Uniqueness is carried by (X2)'s domain hypothesis ("the
  neighbourhood of 1 on which W_♮ is the analytic local maximiser") ✓. Oddness: a ↦ −a sends the diagonal U to Ū and M̄ to
  conj(M̄); with W_♮(conj M) = conj(W_♮(M)) this gives φ ↦ −φ, killing the quadratic term. ✓ The induction (l.4647-4648) is
  correct: Q_root(c_j) = O(|a|³) and the one-step O(|α|³) pulls back to O(|a|³).
  **Note the care taken here and credit it:** §103 (X2) (b) and the Reading (l.4657-4659) both state, unprompted, that
  REVIEW_FLOW_S12 §5 (1)'s "exact" form factor is exact for 𝔪^{S4'} but only second-order-exact for the chain map 𝔪 = W_♮∘M̄
  that FLOW actually uses. That distinction was not in the review; the session found it and reported it against its own
  interest. It is also the distinction that makes §107 (a)'s "no quadratic part" argument work.
- **(c)** Q_str on A_1(x) = e^{ipx_2} gives the factor sin(Lp/2)/sin(p/2) ✓; the slice functional vanishes for this
  polarisation by the stated y_1-average argument ✓; the telescoping Π_{j<m}sin(L^{j+1}p/2)/sin(L^jp/2) = sin(L^mp/2)/sin(p/2)
  and Σ_jL^jpr = p(L^m − 1)/2 ✓. The bound ρ_i ≤ (π/2)L^{-i} from |sin x| ≤ |x| and |sin(P/2)| ≥ |P|/π ✓ — **numerically
  verified tight (0.9995) by me**. ε_n/(εℓ) = sin(P/2)/(ℓ sin(P/2ℓ)) = (sin(P/2)/(P/2))(1 + O(P²/ℓ²)) ✓ — **verified
  (0.828862 against 0.826993 at L = 3, n = 2, P = 2π/3)**.

**(S13-9) WRONG pointer.** l.4645 cites "(FLOW **§30** (C3))" for W_♮(M̄‾) = conj(W_♮(M̄)). (C1)-(C3) are in **§37**
(l.1910-1923; §30 is l.1444-1578), and the rest of FLOW cites them as "§37 (C1)-(C3)" (l.2186, 2261, 2494). The content at
l.1923 is the right content. Pointer only.

f16 A1 corroborates: 𝔪^{S4'} = exp(Q_root aH_1) to 4.37e-15 (SU(2)) / 5.04e-15 (SU(3)), tower formula 7.55e-15; chain map
off-diagonal and oddness **exactly 0.0**; deviation-from-linear ratios 8.063, 8.094 against the pre-stated window [7, 9]
(cubic predicts 8). The Part B diagnostic `level n-1 |a - linear|` = 2.60e-8 at ε = 0.04, 2.60e-11 at 0.004, 4.07e-13 at
0.001 — ratios 1000 and 63.9 against ε³'s 1000 and 64. Clean.

### 3.2 Lemma Cartan-T (S13-8) — **CONFIRMED-WITH-FIX**: one step of (c) is missing for N ≥ 3

I re-derived every clause.

- **(a)** The stationarity computation is correct. Writing out l.4671-4673: e^{−iφ_i}E_{ij} − e^{iφ_j}Ē_{ji} = avg_T N_Tξ_T
  (using ψ_i = h_iθ − φ_i, ψ_j = h_jθ − φ_j and E_{ji} = −avg e^{ih_jθ}ξ̄_T), while r_j + r̄_i = avg_T N̄_T. So
  z·avg_TN̄_T = avg_TN_Tξ_T ✓. The SU(2) specialisation is correct and I checked it in full: N_T = 2e^{i(qθ/2−φ_1)},
  N̄_T = 2e^{−i(qθ/2−φ_1)}, and with e^{iφ_1} = m_1/|m_1| and avg e^{−iqθ/2} = conj(m_1) the phases cancel exactly to
  z = avg[e^{iqθ/2}ξ]/avg[e^{iqθ/2}] ✓.
- **(b)** Exact and elegant. ξ_T − e^{−iqδ_T}ξ_c = −(1 − e^{−iqδ_T})ω(c_Y) ✓ (the ω_X terms cancel because
  δ_T + θ_{S_c} = θ_T); then g(iqδ_T)·(−(1 − e^{−iqδ_T})ω_Y) = −iqδ_Tω_Y, whose average is −iqδ̄ω_Y **exactly, for every
  background in the domain** — the g-weight is precisely what makes the average collapse ✓; then f(iqδ̄)(−iqδ̄ω_Y) =
  −(1 − e^{−iqδ̄})ω_Y and adding e^{−iqδ̄}ξ_c gives e^{−iq(θ_{S_c}+δ̄)}ω(c_X) − ω(c_Y) ✓. The S4' half of (c) is complete.
- **(c), chain half: THE GAP.** l.4680-4681 proves the pointwise identity N_Te^{−iqθ_T} = e^{−i(φ_i − φ_j)}N̄_T (I verified it:
  ψ_i − qθ = ψ_j + φ_j − φ_i and −ψ_j − qθ = −ψ_i − φ_i + φ_j) and then writes "**So** z = e^{−i(φ_i − φ_j)}ω(c_X) − ω(c_Y)".
  That does not follow. Substituting ξ_T(D_Uω) = e^{−iqθ_T}ω(c_X) − ω(c_Y) into z = avg[N_Tξ_T]/avg[N̄_T] gives

      z = e^{−i(φ_i − φ_j)}ω(c_X) − (avg_T N_T / avg_T N̄_T)·ω(c_Y),

  so the covariance needs **avg_T N_T = avg_T N̄_T**, which the pointwise identity does not give (N_T and N̄_T are complex
  conjugates; their averages agree only if avg_T N_T is real).

  **The step is true and the fix is one line.** avg_Te^{iψ_k} = e^{−iφ_k}m_k = r_k, so avg N − avg N̄ = 2i(Im r_i − Im r_j). The
  maximiser's Lagrange condition for Σ_k|m_k|cos(φ_k − arg m_k) under Σφ_k = 0 is |m_k|sin(φ_k − arg m_k) = const, i.e.
  **Im r_k is the same for every k** — which FLOW already records, at l.3010, inside [RFL8-fix S8-3]: "(Lagrange:
  r_isin(arg m_i − ψ_i) must be the same for every i)". Hence avg N = avg N̄ and (c) holds.

  **Reviewer numerics (§0):** at a φ perturbed off the maximiser, |avg N − avg N̄| = 0.137 — so the step is genuinely needed,
  not a triviality. At the maximiser, Im r_k agree to 1e-10 and the difference vanishes.

  **Scope of the gap:** for SU(2), r_1 = r_2 = |m_1| is real (m_2 = conj(m_1), φ_2 = −φ_1), so the step is automatic. The gap
  bites only for N ≥ 3, i.e. exactly where §104 (b) also needed the maximiser rather than the polar part. f16 A3a tested
  SU(3) roots (1,2) and (1,3) and got 2.54e-14 / 2.56e-14, so the *statement* is not in doubt.

  **Verdict: CONFIRMED-WITH-FIX.** Cartan-T stays counted; the proof must cite l.3010.
- **(d)** Correct. N_T = 2 + iq(θ_T − θ̄) + O(a²), avg N̄ = 2 + O(a²) (since avg(θ_T − θ̄) = 0), giving
  z = avg ξ + (iq/2)Cov_T(θ, ξ) + O(a²) ✓; shift-invariance of the covariance gives Cov(δ, ξ) = Cov(θ, ξ) ✓.
  f16 A3b: chain/S4′ difference ratios 3.972, 4.026, 3.984 against the pre-stated [3, 5] (second order predicts 4) ✓.

---

## 4. Priority 4: Proposition SLICE-U (§106), the withdrawn clause, and "pairing at U = 1 grows"

### 4.1 (a): correct, and **stronger than stated** (S13-6) — **CONFIRMED-WITH-FIX**

I verified the induction term by term. With Q_m := T_m + D^{(m+1)}h_m and Q_mD^{(m)} = D^{(m+1)}(ev + h_mD^{(m)}):

    A^{(m+1←j)} = (Q_m − D^{(m+1)}h_m)(Q^{(m)} − D^{(m)}h^{(m)})
                = Q_mQ^{(m)} − D^{(m+1)}[ev h^{(m)} + h_mD^{(m)}h^{(m)} + h_mQ^{(m)} − h_mD^{(m)}h^{(m)}]
                = Q_mQ^{(m)} − D^{(m+1)}[ev h^{(m)} + h_mQ^{(m)}]  ✓

matching l.4695-4697 exactly, with the h^{(m)}D^{(m)}h^{(m)} cross terms cancelling as claimed. P_nD^{(n)} = 0 then gives
P_nA_j = P_nQ^{(n←j)} and the projected identity ✓.

**The strengthening the file misses.** §106 states the hypothesis as "one-step covariance T_kD^{(k)} = D^{(k+1)}ev at U (true
at Cartan U by (X3) (c))" (l.4578-4579). But FLOW already has the composite version at **every** U, at l.3738: "M_UD_U =
D_ℓ^{𝔪(U)}∘ι^* (**for every U at which 𝔪_n is defined**; the S4'/W_♮ constructions are covariant by construction)", used that
way at l.3954 and l.4015 ("for EVERY block map with M_UD_U = D_ℓι^*"). The one-step statement is the same argument with n = 1:
it is just the statement that a gauge-covariant block map intertwines infinitesimal gauge transformations. So **SLICE-U (a) —
the algebraic core, i.e. "the d∘h analogue drops out of the whole T-split at every U" — is unconditionally general, not
Cartan-restricted.** Clauses (b) and (c) are Cartan-plane-wave specific (the slice uses the abelian transport phase e^{iqθ_P}
and the root charge q; the norm bound uses the SU(2) denominator and the plane-wave amplitude ladder). **Fix:** cite §77 (b)
/ l.3738 in §106 (a) and drop "(true at Cartan U by (X3) (c))" to a parenthesis. This is the one place where the session
under-claims.

### 4.2 (b), (c): correct (S13-21) — **CONFIRMED**

- (b): the paths P^σ(c_X → y) lie in c_X + [−1, 1]⁴, so locality ✓; coefficients are exponentials of line sums, so
  analyticity ✓; at U = 1 the coefficients are ±1 with the orientation, so h_{1,k} = −h and, with D_{U'}(1) = −d,
  Q_k(1) = Q_root + dh = Q_str by LINEAR_PACKAGE §1.2 ✓.
- (c): the ≤ 11-step contour count is right (≤ 4 steps centre→corner, 3 along the coarse link, ≤ 4 back), so the SU(2)
  denominator avg e^{iqθ_T/2} can be held ≥ 1/2 on a polydisc ✓. The several-variable Schwarz bound C_2η ✓, the Schur test
  with row/column sums ≤ 648 = 81 sites × 4 directions × 2 orientations ✓, ‖Q_str,L‖ ≤ L^{-1} from §98 ✓. The final
  packaging L^{-1} + x ≤ L^{-1}e^{Lx} is correct (it is 1 + Lx ≤ e^{Lx}) ✓. For complex ε_n, |a_b| ≤ |ε_nρ_{n−k}| because cos
  has a real argument ✓, and ρ_t ≤ 1, so all levels stay in the domain when ε_n does ✓.
  f16 B1 corroborates (a): A^{(2)} = Q^{(2)} − Dh^{(2)} to 1.8e-14, P(A^{(i)} − Q^{(i)}) ≤ 9.5e-15, covariance 2.1e-14.

### 4.3 "Pairing at U = 1 grows": does SLICE-U fail at the trivial field? (S13-7) — **CONFIRMED (no damage)**

This was the most damaging finding on offer, and I went after it directly. It is not there.

1. **At U = 1 exactly, the decomposition does not degenerate; it is the proven case.** §106 (a) says so in its own statement
   (l.4582: "at U = 1 with h_k = −h this is §98 (b)"), and §98/VC-T0 is CONFIRMED at U = 1 by REVIEW_FLOW_S12. f16's own
   diagnostic settles it numerically: at ε = 0, c_0(i) = **1.1111e-01, 1.2346e-02**, a ratio of exactly L^{-2} = 1/9. The
   transverse coefficients at the trivial field decay at the full rate.
2. **What grows is not SLICE-U at U = 1; it is the ε-expansion *about* U = 1 with the frozen slice.** ℒ_n is defined at
   l.4588-4590 as `[ε]P_n·(1 − P_n^0)𝒞_n^0(1 − P_n^0)·[ε]P_n` — a term carrying **two** factors of [ε]P_n, i.e. an ε² term in
   the expansion away from U = 1, assembled with U = 1 projectors. §106 (d)'s mechanism is then: differentiating
   P_n(U)D^{(n)}(U) = 0 gives [ε]P_n·D_0 = −P_n^0D_1, and with 1 − P_n^0 = D_0Δ_0^+D_0^* this converts ℒ_n into
   P_n^0D_1G_nD_1^*P_n^0 with G_n ≥ κ^{-1}(n − 1)/8 by LONG-n. I checked each step, including the explicit
   P^0(K)D_1(K ← K∓P) = β_∓P_{T,ℓ}(K)e_1 with |β_∓| = |q|·|[ε]ε_n|/2 and the diagonal value
   κ^{-1}((n−1)/8)(q²|[ε]ε_n|²/2)(1 − |D̂_ℓ(K)_1|²/λ̃(K)) ✓.
   So "pairing at U = 1 grows" means: *if you keep the U = 1 slice while moving off U = 1, the first-order slice data stop
   being L^{-i}-summable.* f16 measures exactly that, and the measurement is unambiguous: with the U = 1 pairing
   ‖[ε]A^{(i)}‖ = 2.8916 → 2.9528 (no decay); with the pairing at U, ‖[ε]Q^{(i)}‖ = 1.1604 → 0.38739 (ratio 0.3338 ≈ L^{-1}).
   That is a statement about slice choice, not about the trivial background.
3. **PROOF.md's "FLOW BFT-2, 3 at the trivial field" is a different thing entirely.** l.6633 lists *who needs which part of
   BFT*: "FLOW BFT-2, 3 at the trivial field", and the FLOW row of the cross-lane map (l.6637-6642) spells it out: "Needs from
   PROOF/BFT: (SF-bg) = BFT-2, 3 at the trivial field". That is an **input FLOW consumes** — holomorphy and locality of the
   composite tower at V_k = 1 — not a background at which FLOW's own covariant decomposition has to be non-degenerate. The
   two "trivial field"s are unrelated.

**Verdict: no damage.** SLICE-U gives FLOW the U = 1 case as the already-proven special case, and the growth is a diagnosis of
why the U = 1 slice must be replaced away from U = 1 — which is the whole content of [RFL12-fix S12-4] and the reason the
session was asked for SLICE-U in the first place.

**One presentational defect (S13-22).** §106 (d)'s *proof* ends, before the ∎ (l.4717-4718), with "By §107 the full
second-order transverse coefficient converges, so ℒ_n is cancelled by the cross terms of the termwise expansion." A forward
reference inside a proof. It is **not circular** — §107 uses only §106 (a) and (c), never (d) — and at the Π_j = 1 of (X4) (d)
§107 carries no (Π-loc) conditionality, so the sentence is sound. But it belongs in the Reading, not inside the proof.

---

## 5. Priority 5: VC-T1 and P-poles (§107), and the "PROVEN given (Π-loc)" labelling

### 5.1 The mathematics (S13-23) — **CONFIRMED**

- **(a) n-independence.** Correct, and the argument is subtler than it looks: for r ≤ 2 the coefficients see only the linear
  part of each level background *because* §104 (b) kills the quadratic part (the ε³ term cannot reach an ε² Taylor
  coefficient). With §104 (c) the level-(n−i) background depends only on (i, ε_n, P, ϑ_n), the level-(n−i) torus has side
  L^iT, and the one-step maps are level-uniform; so s_i and P are n-independent and 𝒞_n is the sum over i = 0..n−1 ✓.
- **(b) the decay.** ‖Q^{(i)}‖ ≤ L^{-i}exp(LC_3RΣ_{t≥1}ρ_t) ≤ L^{-i}exp(LC_3Rπ/(2(L−1))) ✓ — I checked Σ_{t≥1}ρ_t ≤
  (π/2)Σ L^{-t} = (π/2)/(L−1). The holomorphy trick is correct and worth noting: Q^{(i)}(ε̄)^* has the Taylor coefficients
  q_k^* and so is **holomorphic** in ε, agreeing with Q^{(i)*} on the real axis, which is what makes a one-variable Cauchy
  estimate legitimate on ‖QΠ^{-1}Q^*‖ ✓. Hence ‖[ε^r]Q^{(i)}‖ ≤ C'_rL^{-i} and ‖[ε^r](QΠ^{-1}Q^*)‖ ≤ C''_rL^{-2i} ✓.
  Minor: "Π^{-1} is bounded and analytic, by (Π-loc)" skips that R may have to shrink to keep Π(ε) invertible.
- **(c) P-poles.** The sector {K + tP} is finite on the torus, so μ_K = min_tλ̃(K + tP) > 0 ✓; [ε^r]Δ^{-1} is a sum of products
  with ≤ r + 1 diagonal factors 1/λ̃(K + tP), |t| ≤ r, so N_r = Π_{|t|≤r}λ̃(K+tP)^{r+1} clears every denominator and N_r[ε^r]P
  is a trigonometric polynomial ✓ — this is an *algebraic* cancellation, strictly better than a Cauchy estimate whose radius
  would degenerate as μ_K → 0, and it is the right way to do it. The explicit first-order closed form at l.4756-4757 is
  correct and matches the script's independent implementation character for character. "P_{T,ℓ} itself (r = 0) is bounded but
  non-analytic at K = 0" is correctly flagged ✓.
- **(d).** The divisibility claim holds for r ≤ 2: each [ε^{r_i}]P factor contributes λ̃-powers only at momenta K + vP with
  |v| ≤ r, to total power ≤ r + 2 ≤ 2(r + 1), so the normalisations divide Ñ_r = N_r² ✓. Σ_{i≥n}C_rL^{-2i} = C_rL^{-2n}/(1 −
  L^{-2}) ✓.

### 5.2 (d)'s normalisation is far heavier than (T-a2)'s (S13-12) — **NARROWED**

(c) delivers the **sharp** first-order statement with normalisation λ̃(K)λ̃(K+P), λ̃-degree 2 — precisely what §99 [RFL12-fix
S12-4] (l.4474-4476) specifies for (T-a2). (d) then states the L^{-2n} rate only after Ñ_r = N_r², i.e.
Π_{|t|≤r}λ̃(K+tP)^{2(r+1)}:

| order r | Ñ_r | total λ̃-degree | degree the product actually needs |
|---|---|---|---|
| 1 | Π_{\|t\|≤1}λ̃^4 | **12** | ≤ 4 (each term of [ε](Ps_iP) carries at most one [ε]P factor; the P^0 factors need none) |
| 2 | Π_{\|t\|≤2}λ̃^6 | **30** | ≤ 8 by the same count |

So (d) over-normalises by roughly a factor 3-4 in λ̃-degree. As written, the r = 2 clause permits the difference from the
limit to blow up like |K|^{-30} as K → 0. Whether a bound that weak suffices for the Lemma-VC-type pole absorption that (T-b)
and (T-c) will need is **not established anywhere**, and §99's (T-a) does not pin the degree. Compounding this: f16 tested no
small K at all (§7.3), so the one regime where the normalisation matters is untouched by both proof optimisation and
measurement. **Fix:** state (d) with the sharp normalisation, or say explicitly that the degree is not optimised and name the
degree the downstream use needs.

### 5.3 "PROVEN given (Π-loc)" (S13-10) — **CONFIRMED-WITH-FIX**

Where the conditionality is stated and where it is not:

| Site | Carries "given (Π-loc)"? |
|---|---|
| §103 (X5) hypotheses, l.4595 | ✓ named as a hypothesis |
| §107 heading, l.4733 | ✗ **"PROVEN-HERE", unqualified** |
| §107 l.4735, immediately below | ✓ "(Π-loc) is a named hypothesis, ARGUED" |
| §110 Outcomes, l.4831 | ✓ "PROVEN, for the 𝒞-part, orders ≤ 2, given (Π-loc)" |
| §110 **Tally**, l.4847 | ✗ **"PROVEN-HERE: 70 + 5 = 75: Cartan-𝔪, Cartan-T, SLICE-U, VC-T1, P-poles"** |
| §110 ARGUED list, l.4850 | ✓ (Π-loc) listed as ARGUED, not counted |
| FLOW_LOG l.619-620 | ✓ "PROVEN for the 𝒞-part, orders ≤ 2, given (Π-loc) ARGUED" |
| "FOR OTHER FILES" note | n/a — **FLOW.md has no such section**; I grepped |

**The count is not wrong under this lane's convention.** REVIEW_FLOW_S9 l.371 sets it: "Corrected tally: 50 PROVEN-HERE
(claimed 50) = 46 + S-2pt + S-tel + S-fix + **V-2pt (given (L-loc2))**". An item proven from a named ARGUED input is counted,
with the label attached *in the tally line*. Session 13 keeps the count and drops the label in exactly the two places a later
reader will quote: the section heading and the tally. Since PROOF.md's cross-lane map quotes the latest review's statuses
verbatim (l.6637ff), the fix has to land before this propagates into the master ledger.

**Fix:** §107's heading and §110's tally line must read "VC-T1, P-poles (given (Π-loc), ARGUED; 𝒞-part only; orders r ≤ 2; at
the Cartan plane wave)".

### 5.4 (Π-loc)'s own argument covers only part of it (S13-11) — **CONFIRMED**

(X5) states (Π-loc) as three things: Π_{k+1}(U) = Π(M̄_c(B_k)) is (i) a **per-link multiplication operator** in the root
sector, (ii) **analytic in the background**, (iii) Π(1) = 1. §107's justification (l.4735-4736) is one clause: "at diagonal
M̄, Π(M̄) is torus-invariant, hence diagonal in the roots." That argues the **colour** structure only. Position-space locality
— the substantive part, and the part a cluster expansion would have to supply — is not argued at all, and neither is the
analyticity. ARGUED is the right status; the argument given does not reach as far as the statement.

**Constructive note, and the cheapest route to an unconditional item.** At Π_j = 1 — the soft-chain normalisation of COV-str
(ii) used by LONG-n (l.4277), by §98 and by f16 Part B itself — (Π-loc) is not needed: §107 (b) only ever uses Π^{-1} through
"bounded and analytic", which is trivial at 1. So **VC-T1 at Π_j = 1 is unconditional**, and splitting (X5) into a Π = 1
clause and a general-Π clause would make one of the two new items unconditional at no cost. The session does not make that
split.

---

## 6. Priority 6: §108, the W_n half of LONG-n (S13-16) — **CONFIRMED-WITH-FIX**

This is the discharge of [RFL12-fix S12-2], and it does discharge it. I re-derived it:

- (Y^{-1})_{VV} = 1/(Y_VV − Y_VTY_TT^{-1}Y_TV) in the frame (V, ker D̂^†), with V = D̂/|D̂| spanning Ran D̂ ✓.
- Y_TT = Ỹ_n ≥ κ^{-1}P_n from the j = n term of 𝒞_n (A_n = 1, Π_n = 1) plus the positive M-part, so ‖Y_TT^{-1}‖ ≤ κ ✓.
- Y_VT's j-terms: A_j^*P_n = Q_str^{(L^i)*}P_n by the same projected identity, so the j-term is
  V^*(Q_str^{(L^i)} − d_n∘h^{(i)})Q_str^{(L^i)*}P_n with norm ≤ L^{-2i} + ‖h^{(i)}‖L^{-i}, summable; the M-term is finite at
  fixed K ✓. So |Y_VT| ≤ C(K).
- W_n(K) ≤ 1/(κ^{-1}[1 + (n − 1)λ̃(K)/8] − κC(K)²) → 0, log W_n(K) ≤ −log n + O_K(1) ✓. That is the upper bound the FALSE
  verdict needs, and S12-2 is satisfied.

**Two loose points.**
1. The closing sentence (l.4783) — "Together with W_n ≥ 1/⟨V, YV⟩ this proves the W_n half" — does no work. W_n ≥ 1/⟨V, YV⟩
   combined with LONG-n's *lower* bound on ⟨V, YV⟩ gives nothing; a matching log W_n ≥ −log n − O(1) would need
   ⟨V, YV⟩ = O(n), which is plausible (each j-term is O(1) on the longitudinal direction) but is not proved here. The FALSE
   verdict needs only the upper bound, so: either drop the sentence or prove the O(n).
2. **§108 is missing from §110's Outcomes list** (l.4826-4831 lists (X1)-(X5) only). Counting it with LONG-n rather than as a
   new item is right; omitting it from the outcomes is not. It belongs under (X1), since S12-2 is one of the nine fixes.

---

## 7. Priority 7: check f16

### 7.1 B3 and B4 (S13-13) — **CONFIRMED-WITH-FIX**: honest FAILs, correct diagnosis, self-inconsistent criteria

**Honesty first, because it is the part that matters and it is right.**
- δ = 0.02 and 0.04 WERE pre-registered: f16_criteria.md Part B, "Coefficients [ε], [ε²] from central differences at δ = 0.02
  and 0.04, Richardson-combined (error O(δ⁴))". So the two FAILs are real pre-registered FAILs on a pre-registered step.
- Both are printed as `[FAIL]` in f16_out.txt, carried into §109 as FAILs, and listed in §109 Reading (1) as "the pre-stated
  F5 (B3) and F6 (B4) lines FAIL as recorded".
- The rescue runs are labelled "ADDENDUM (NOT pre-stated; added after the smoke runs)" in the output itself, in FLOW_LOG and
  in §109, and the thresholds were not changed.
- **add1-B4 is reported as a FAIL** (1.21e-7 against 1e-7). A session inflating its result would have quietly folded that into
  the δ = 0.0005 pass. It did not.

**Is "too coarse a step" a credible diagnosis or a rationalisation? For B4: credible, and I verified it quantitatively.**

| δ | B4 residual | ratio to previous | δ⁴ prediction |
|---|---|---|---|
| 0.02 | 1.22e-3 | — | — |
| 0.002 | 1.21e-7 | **1.008e4** | 1e4 |
| 0.0005 | 8.25e-10 | 146.7 | 256 |

The first step is δ⁴ to within 0.8%. The second falls short of δ⁴ by a factor 1.7, which is the expected signature of the
roundoff floor of a Richardson-extrapolated central difference at δ = 5e-4 (the cancellation error grows as δ decreases, so
the observed decay being *slower* than δ⁴ is the right direction). Diagnosis accepted.

**But the criteria were arithmetically unachievable as written, and that was knowable before the run.**
- The criteria state their own error model: "Richardson-combined (**error O(δ⁴)**)". At the pre-stated δ = 0.02 that is
  1.6e-7 with coefficient 1 — **already above the 1e-7 threshold** before anything else is counted.
- And the expansion variable is not the field. §109 says "the level-n field is ≈ 7.5ε"; I recomputed it exactly:
  ε_n/ε = sin(P/2)/sin(P/2ℓ) = **7.4598** at L = 3, n = 2, P = 2π/3, so the step in the field is **0.1492** and
  δ_field⁴ = 4.9e-4 — within a factor 2.5 of the observed 1.22e-3.
- The δ that meets the threshold is **0.0019**, i.e. the pre-stated step was ~10× too coarse.

So the B4 FAIL carries no information about Lemma P-poles; it was determined at pre-registration by the criteria's own error
model. The same holds for B3, whose −1e-10 tolerance is orders below the finite-difference error in ℒ at δ = 0.02. **Fix:**
§109 should say that the pre-stated (δ, threshold) pair was internally inconsistent, not merely that δ "was too coarse" —
the distinction matters for whether the next criteria file repeats it.

**One over-reach in the B3 diagnosis.** §109 says "the δ⁴ scaling identifies the residual as truncation" under a bullet list
covering both failures. There is no scaling test for B3. Its two data points are λ_min = −2.91e-9 / −3.30e-9 at δ = 0.02 and
≈ −3e-16 at δ ≤ 0.002 — a factor ~1e7 for δ/10, which is **not** δ⁴ (1e4); −3e-16 is the roundoff floor, so the scaling is
untestable, not verified. The direction is right and the conclusion is almost certainly right, but it is demonstrated for B4
only. Also, §109 quotes B3's λ_min as "−2.9e-9" where the output gives −2.91e-9 **and −3.30e-9**; quote the worse one.

**No verdict depends on the post-hoc runs.** B3's non-decay half (ratio 0.9661) passes at every δ, and B2 — the only f16
result §107 actually cites — is identical to four digits at δ = 0.02, 0.002 and 0.0005. Good.

### 7.2 §103 vs the criteria file: an unlogged threshold relaxation (S13-14) — **CONFIRMED-WITH-FIX**

§103 (B2), l.4622-4623: "‖[ε^r]Q^{(2)}‖/‖[ε^r]Q^{(1)}‖ ≤ **0.5**".
f16_criteria.md Part B, B2: "q_r(2)/q_r(1) ≤ **0.6** for r = 1, 2".

§103 is the binding pre-statement (11:35:42); the criteria file (11:39:15) relaxed one of its thresholds by 20%, and
FLOW_LOG's "Statement changes after §103" list (l.621-623) records only the withdrawn (X4) (d) clause, the torus and the
addendum. **No verdict turns on it** — the measured ratios are 0.3338 and 0.4182, which pass 0.5 as well — but a pre-stated
number must either govern or be logged as changed.

### 7.3 The 0.107 shrink against L^{-2} = 0.111 (S13-15) — **NARROWED; nothing is load-bearing on it**

The data (one ratio per order):

| r | c_r(i = 1) | c_r(i = 2) | ratio | L^{-2} |
|---|---|---|---|---|
| 1 | 1.7789e-01 | 1.8817e-02 | 0.1058 | 0.1111 |
| 2 | 6.2776e-01 | 6.7840e-02 | 0.1081 | 0.1111 |

**What it supports.** At this one background, the first- and second-order transverse 𝒞 coefficients shrink by roughly L^{-2}
over one level, and the U = 1 bookkeeping term does not shrink (ratio 0.9661). Together with the decomposition algebra
passing at 1e-14, that is a real, non-vacuous corroboration of the mechanism, and the U = 1 control is the sharp contrast
S12 §10.3 (iii) asked for in spirit.

**What it does not support, stated plainly.**
- i ranges over {1, 2}, so there is exactly **one ratio per order**. One ratio cannot distinguish L^{-2} from L^{-2}(1 + O(ρ))
  from a background-specific 0.106. The criteria themselves only asked for ≤ 0.25, which is a factor-2.4 margin.
- The level-n torus is **(3, 3, 1, 1)**, not the pre-stated (3, 3, 2, 2). Directions 3 and 4 have a single site, so
  K_3 = K_4 = 0 identically and the sector condition (K_1, K_3, K_4) ≠ 0 collapses to K_1 ≠ 0. **Six momenta are tested**
  (f16_out.txt: "over 6 K"), and the level-n momentum content is effectively two-dimensional. No 4D sector structure is
  probed.
- At those six momenta λ̃(K) = |1 − e^{iK_1}|² + |1 − e^{iK_2}|² ∈ {3, 6}. **There is no small K anywhere in Part B**, so the
  λ̃-normalisation of S13-12 — where Ñ_1 at λ̃ = 3 is already a factor 5.3e5 — is never exercised. REVIEW_FLOW_S12 §10.3 (ii)
  (l.428-429) explicitly asked for "three K including a small one". That probe was not run, and the reason is the memory
  ceiling (§7.4), not a judgement that it was unnecessary.
- SU(2) only in Part B; no N ≥ 3 anywhere in the composite setting.
§109 Reading (3) discloses the first three of these honestly.

**Load-bearing check — the answer is no.** §107 (b) derives ‖[ε^r]Q^{(i)}‖ ≤ C'_rL^{-i} analytically, by Cauchy's estimate on
§106 (c)'s ‖Q_k‖ ≤ L^{-1}exp(C_3L|ε_nρ|). I re-derived both steps (§4.2, §5.1). **No statement in §104-§108 rests on the
0.107.** It is corroboration, and §107 Reading (4) presents it as such ("against L^{-2} = 0.111"), not as evidence for the
bound.

### 7.4 The 1.03 GB smoke run (S13-17) — **CONFIRMED: a disclosed breach of the process rules**

The handoff rule is "keep each job under 20 min and **under 1 GB**". Smoke 3 (11:53:49-11:54:36, torus (3,3,2,1)) peaked at
**1.03 GB**, ~3% over. FLOW_LOG l.602-603 records it explicitly as "this smoke run EXCEEDED the 1 GB job limit (by ~3%);
recorded as a violation", and §109 repeats it. Disclosure is exemplary; it is still a breach, and it should be counted as one.

Everything else is inside the envelope: the official run took one lock acquisition (11:55:17-11:56:22), released once with
`rmdir`, load 3.03 < 8, memory free 38% ≥ 35%, nice 10, one thread, 65.35 s < 20 min, 548 MB < 1 GB. Five lock acquisitions in
all, each released. Nothing left running.

**The consequence is the thing to notice.** The breach is *why* the pre-stated (3, 3, 2, 2) torus was abandoned for
(3, 3, 1, 1) — "extrapolated ~2 GB from 1.03 GB at (3, 3, 2, 1)" (FLOW_LOG l.604-606). That substitution is the single
largest weakening of the numeric evidence in this session: it is what removed the second site in two directions and, with it,
any small-K sector. A memory-lighter implementation (sector-by-sector assembly rather than dense level-n operators) would
restore the probe S12 asked for.

---

## 8. Per-item verdicts

| Item | Verdict | Finding / fix |
|---|---|---|
| Session complete, no orphans | **CONFIRMED-WITH-FIX** | S13-1 (misquoted 2.92; the (3,3,2,1) smoke numbers are unsourced) |
| Provenance chain | **CONFIRMED** | S13-2 (the reconstruction claim is now unverifiable) |
| [RFL12-fix] S12-1..S12-9 | **APPLIED, all nine, correct** | S13-3 (formula slip in the l.4280 tag) |
| The Cartan restriction | **CONFIRMED as a genuine, upstream-proven reduction** | S13-4 (cite F-Π (i), l.3835, §37 S5-5) |
| Root-sector diagonalisation | **CONFIRMED** | S13-5 |
| Lemma Cartan-𝔪 (X2) | **CONFIRMED** | S13-9 (§30 → §37 for (C3)) |
| Lemma Cartan-T (X3) (a), (b), (d) | **CONFIRMED** | — |
| Lemma Cartan-T (X3) (c), chain half | **CONFIRMED-WITH-FIX** | S13-8 (needs avg N = avg N̄; cite l.3010's Lagrange condition; N ≥ 3 only) |
| Prop SLICE-U (a) | **CONFIRMED, and stronger than claimed** | S13-6 (holds at every U by l.3738) |
| Prop SLICE-U (b), (c) | **CONFIRMED** (Cartan plane wave only) | — |
| Prop SLICE-U (d) | **CONFIRMED**; the L^{-i} clause correctly WITHDRAWN | S13-22 (forward reference inside the proof) |
| "Pairing at U = 1 grows" ⇒ failure at the trivial field | **the claim does not hold; no damage** | S13-7 |
| Prop VC-T1 (X5) (a)-(c) | **CONFIRMED** given (Π-loc) | S13-10 (labelling) |
| Prop VC-T1 (X5) (d) | **NARROWED** | S13-12 (Ñ_r is λ̃-degree 12 / 30 where ≤ 4 / 8 is needed) |
| Lemma P-poles (X5) (c) | **CONFIRMED**, sharp at first order | — |
| (Π-loc) as ARGUED | **CONFIRMED**; the argument covers the colour clause only | S13-11 (unconditional at Π_j = 1) |
| §108 W_n half | **CONFIRMED-WITH-FIX** | S13-16 (dead final sentence; missing from §110 Outcomes) |
| f16 B3, B4 FAILs and their diagnosis | **CONFIRMED-WITH-FIX** | S13-13 (criteria self-inconsistent; B3 has no scaling test) |
| §103 vs criteria B2 threshold | **CONFIRMED-WITH-FIX** | S13-14 (0.5 → 0.6, unlogged; no verdict affected) |
| The 0.107 shrink | **NARROWED**; corroboration only | S13-15 |
| 1.03 GB smoke run | **CONFIRMED breach**, disclosed | S13-17 |
| §110 "P_k at orders 1, 2 off the list" | **NARROWED** (minor) | S13-18: §107 (c) proves it for P_n; every k follows by the level-uniformity of §107 (a), unstated |
| f16 reproducibility | **NOT-VERIFIED** | S13-19: not re-run, by choice, under the numerics rule |

---

## 9. Corrected tally

**75 PROVEN-HERE (claimed 75) = 70 (REVIEW_FLOW_S12) + Cartan-𝔪 + Cartan-T + SLICE-U + VC-T1 + P-poles — CONFIRMED.**
- **Strict: 70 (claimed 70)**, with P-poles folded into VC-T1.
- **Counted with these labels, which must travel with the items:**
  - Cartan-𝔪: at Cartan configurations, any N; exact for 𝔪^{S4'}, exact through second order for the chain map 𝔪.
  - Cartan-T: at Cartan configurations, any N; **(c)'s chain half needs the one-line Lagrange step of S13-8**.
  - SLICE-U: (a) at **every** U (S13-6); (b), (c) at the Cartan plane wave; (d) with its L^{-i} clause withdrawn.
  - VC-T1: **given (Π-loc) (ARGUED)**; 𝒞-part only; orders r ≤ 2; at the Cartan plane wave; uniformity in K only after the
    heavy Ñ_r of S13-12. Unconditional at Π_j = 1.
  - P-poles: unconditional ((Π-loc) is not used); orders r ≤ 2; sharp at first order.
- **IMPORTED-AND-REVERIFIED:** unchanged (L4b; the Lévy functional CLT). No new import. ✓
- **ARGUED, not counted:** (L-loc2); (W6); **(Π-loc) (new this session)**; the flux-type bound for the covariant slice at U_f;
  DEF-red.
- **OPEN:** (T-a1-M) [filed with (T-b)]; **(T-a3) (newly named)**; (T-b); (T-c); (L-loc2); the rate items (s1), (s2⊥), the
  rate of c'(φ) → c'_0; (COV-GI) at non-critical backgrounds; FI-1; HIST's restatement of CL^J's Setting.
- **Honest accounting of the net move.** (T-a2) comes off the list at the orders needed. (T-a1) does not: it is split into a
  conditional 𝒞-part (done) and (T-a1-M) (open), and (T-a3) is carved out of what (T-a) also demanded. So where §102 had one
  OPEN name, §110 has two OPEN names plus one new ARGUED hypothesis. That is refinement in the right direction, but the wall
  shrank by less than "(T-a1) + (T-a2) done" would suggest, and §110's "Theorem UNIV for SU(N) does NOT yet rest only on
  (L-loc2)" (l.4844) remains the correct headline. The session states it.

---

## 10. Binding fixes for the next lane-C session

1. **S13-1 (§106 l.4730-4731; §106 l.4721-4722).** Correct "2.92" to **2.89** (f16_out.txt: 2.8916e+00). Either drop the
   "(3, 3, 2, 1) smoke torus … 1.99e-2 → 2.46e-3 (ratio 0.12)" figures or record them in FLOW_LOG as smoke-3 output, since no
   committed artifact contains them. Note while doing so that 0.1236 ≈ L^{-2}, i.e. the smoke showed *faster* decay than the
   withdrawn clause claimed.
2. **S13-8 (§105 (c), l.4680-4681). The one substantive mathematical fix.** Insert the missing step: z =
   e^{−i(φ_i−φ_j)}ω(c_X) − (avg_TN_T/avg_TN̄_T)ω(c_Y), and avg_TN_T = avg_TN̄_T because avg_Te^{iψ_k} = r_k and the maximiser's
   Lagrange condition makes Im r_k independent of k — cite **l.3010, [RFL8-fix S8-3]**. State that for SU(2) it is automatic
   (r_1 = r_2 = |m_1| real).
3. **S13-10 (§107 heading l.4733; §110 tally l.4847).** Add the conditional and scope label: "VC-T1, P-poles (given (Π-loc),
   ARGUED; 𝒞-part only; orders r ≤ 2; at the Cartan plane wave)", following REVIEW_FLOW_S9 l.371's convention. Also split
   (X5) so that the Π_j = 1 case is stated unconditionally (S13-11), and note that P-poles alone never uses (Π-loc).
4. **S13-4 (§110).** One sentence saying why Cartan suffices: c^tot_n is defined at a constant Cartan flux (l.3835), Lemma
   F-Π (i) gives the exact colour reduction (l.1548), and the Cartan-sector fluctuations carry no universal content (§37
   [RFL5-fix S5-5], §44 (e)). Say in the same sentence that the remaining step from the Cartan plane wave to U_f is (T-c),
   OPEN.
5. **S13-6 (§106 (a), l.4578-4579).** Cite §77 (b) / l.3738 ("for every U at which 𝔪_n is defined") so that (a)'s covariance
   hypothesis is seen to hold at every U, not only at Cartan. This strengthens the result; it is the one place the session
   under-claims.
6. **S13-12 (§107 (d), l.4759-4763; (X5) (d)).** State (d) with the sharp normalisation, or record explicitly that Ñ_r is
   λ̃-degree 12 (r = 1) and 30 (r = 2) where the product needs ≤ 4 and ≤ 8, that the degree is not optimised, and that no
   small-K data bear on it.
7. **S13-13 (§109).** Say that the pre-stated (δ, threshold) pairs were internally inconsistent — the criteria's own
   "error O(δ⁴)" gives 1.6e-7 at δ = 0.02, already above B4's 1e-7, before the 7.46× field amplification — so the FAILs were
   fixed at pre-registration. Restrict "the δ⁴ scaling identifies the residual as truncation" to **B4**; for B3 say that the
   smaller-δ value is at the roundoff floor and no scaling test exists. Quote B3's worse eigenvalue (−3.30e-9).
8. **S13-14 (FLOW_LOG).** Log the §103 → f16_criteria.md B2 threshold change (0.5 → 0.6). Pre-stated numbers govern unless the
   change is logged.
9. **S13-9 (§104 (b), l.4645); S13-3 (l.4281-4282); S13-16 (§108 l.4783, §110 l.4826-4831); S13-22 (§106 (d) l.4717-4718).**
   (C3) is in **§37**, not §30. The S12-2 tag's Schur bound should read "− κC(K)²". Drop §108's dead last sentence (or prove
   ⟨V, Y_nV⟩ = O(n)) and list §108 in §110's Outcomes under (X1). Move §106 (d)'s "By §107 …" out of the proof into the
   Reading.
10. **S13-2 (process, for the lead).** Keep the in-place replacement scripts, or their md5s and pair counts, in the lane dir.
    Session 12's provenance was byte-reconstructible because flow12/ survived; session 13's is not, because flow13/ is gone.
11. **S13-15 / S13-17 (next check).** The missing probe is small K. Re-run Part B with a level-n torus that has at least two
    sites in a third direction and at least one small-|K| sector, under a sector-by-sector assembly that fits in 1 GB. Also
    extend to i = 3 so that there are two ratios per order rather than one, and to SU(3) in Part B.

---

## 11. How much of (T-a1)/(T-a2) is in hand, and at which backgrounds

**In hand.**

| Statement | Status | Background | Scope |
|---|---|---|---|
| **(T-a2)**: ε-expansion of the level projector, poles absorbed | **PROVEN, unconditional** (no (Π-loc)) | Cartan plane wave of (X2) (c), one Cartan direction H_1, one root α, any N | orders r = 1 and 2; momentum sectors {K + tP} avoiding 2πZ⁴; **sharp** first-order normalisation λ̃(K)λ̃(K+P), exactly as §99 [S12-4] specifies; stated for P_n (every k follows by level-uniformity, unstated — S13-18) |
| **(T-a1), 𝒞-part**: the level-transverse 𝒞 symbols converge at L^{-2n} | **PROVEN GIVEN (Π-loc) (ARGUED)**; unconditional at Π_j = 1 | same | orders r ≤ 2; one root sector; uniformity in K only after Ñ_r (λ̃-degree 12 / 30 — S13-12) |
| **The slice algebra** P_n(U)A_jΠ^{-1}A_j^*P_n(U) = P_n(U)Q^{(n←j)}Π^{-1}Q^{(n←j)*}P_n(U) | **PROVEN** | **every U** (S13-6) | any slice family h_k; this is what removes the d∘h / LONG-n growth from the T-split |
| **The plane-wave form factor of 𝔪_n** (S12-9's item) | **PROVEN** | every Cartan configuration, any N | exact for 𝔪^{S4'}; exact through second order for the chain map 𝔪 — which is all orders r ≤ 2 use |

**Not in hand.**
- **(T-a1-M)**, the M-part P_nQ^{(n←0)}H_⊥(U)^{-1}P_⊥Q^{(n←0)*}P_n. OPEN, filed with (T-b). This is the half carrying the
  x^blk ~ |K|^{-2} infrared content ([RFL12-fix S12-5], l.4446). At U = 1 both halves were done in §98; at U ≠ 1 only the
  𝒞-half is. The half that moved is the half whose U = 1 structure was already understood.
- **(T-a3)**, the n-independent leading degree-4 numerator that §99's (T-a) explicitly demands. OPEN, newly named (§107
  Reading (3), l.4769).
- Orders r ≥ 3 — not claimed, and (T-a) does not need them.
- Any non-Cartan background; any Cartan-**sector** fluctuation; any N ≥ 3 in the composite setting; any small K.
- **The exchange from the Cartan plane wave to the constant Cartan flux U_f that defines c^tot_n.** That is **(T-c)**, OPEN.

**One-line answer.** (T-a2) is closed at the orders the programme needs. (T-a1) is about half closed and conditionally so:
the 𝒞-part at the Cartan plane wave, orders ≤ 2, given (Π-loc), with a normalisation heavier than specified; the M-part and
the degree-4 numerator are open. (T-a1) did move — this is not a measure-zero case dressed up — but it did not close, and
§110 says so.

---

## 12. The biggest live wall in FLOW

**The fine, background-dependent inverse H_⊥(U)^{-1} — i.e. (T-a1-M) together with (T-b).**

Why this and not something else:
- It is the half of (T-a1) that session 13 left open, and §107 Reading (2) (l.4767-4768) names the obstruction precisely: the
  M-part "needs the fine H_⊥(U)^{-1} expansion". Everything session 13 proved lives at the *level* lattice, where the
  composites are explicit abelian products; H_⊥(U)^{-1} is a resolvent on the **fine** lattice at a non-trivial background,
  a genuinely new analytic object for this lane.
- (T-b) needs the same object from the other side: "the plane-wave density of the gapped fine operator
  H_⊥ + M̃^T(P_n𝒞_nP_n)^{-1}M̃" (§99, l.4478-4480). The two are one wall, which is why §107 files (T-a1-M) with (T-b).
- It carries the infrared content. [RFL12-fix S12-5] records that the symbol itself is ~|K|^{-2} and only the *difference*
  is uniform; that |K|^{-2} lives in the M-part's x^blk. The 𝒞-part that session 13 convergence-proved is the benign half.
- REVIEW_FLOW_S12 §5 identified "the background linearisation T_k(U) … together with the poles of P_k(U)" as the hard part of
  (T-a). Session 13 did both of those. The next hard thing is this.

**Runner-up, and the one that decides whether any of it reaches the target: (T-c).** c^tot_n is defined at a constant Cartan
flux (l.3835). Everything §104-§107 proves is at a Cartan *plane wave*. Without the plane-wave ↔ constant-field exchange,
the entire §107 result is a statement about a probe background that never reaches the coupling flow. Nothing in §103-§110
narrows (T-c), and §110 does not claim otherwise — but the dependency should be stated where the Cartan justification of
S13-4 is added, so that no later reader mistakes "the T-split vertex data converge" for "c^tot_n converges".

**(L-loc2)** remains ARGUED, as it has been since session 9, and is not displaced by anything here.
