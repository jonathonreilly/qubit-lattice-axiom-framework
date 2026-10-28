# REVIEW_NORMS_S1: hostile review of NORMS.md (session 24, the N1 norms worker), with the NQ_CHECK adjudication

Reviewer: an independent agent. I wrote none of NORMS.md, NQ_CHECK.md, PROOF.md, LINEAR_PACKAGE.md or any check.
This file is the only repository file I edited. No git command was run; no commit, push or PR.

**Finding ids.** `RN1-k`. NORMS.md's own lemmas are `N1-k`; the prefix `RN1-` is a review finding, never a lemma of the
file under review.

**Inputs** (read 2026-10-28, 13:30–13:55 UTC; `TZ=UTC stat`):
- NORMS.md: born 12:57:22, mod 12:57:22, 81173 B, 918 lines.
- NORMS_LOG.md: born 12:37:51, mod 12:57:30, 4111 B.
- NQ_CHECK.md: born 13:06:50, mod 13:16:24, 28959 B.
- checks/n1_criteria.md 12:38:20 (4282 B); n1_exponents.py 12:38:55; n1_out.txt / n1_err.txt / n1_time.txt 12:38:59.
- checks/nq1_criteria.md 13:07:22; nq1_qnorm.py 13:09:25→13:09:38; nq1_out.txt 13:10:15→13:10:41.

**What I read in full:** NORMS.md (all 918 lines), NORMS_LOG.md, NQ_CHECK.md, checks/n1_criteria.md,
checks/n1_exponents.py line by line, checks/n1_out.txt, checks/n1_time.txt. **In part:** PROOF.md l.6150–6253 (CURV1
assembly, Lemma E3 and its Lipschitz consequence, NAH-unif, (H-K)/(H-C) status, the CURV-F2 diagnosis, c37),
l.6460–6523 (c38 A–D, TOWER-VAR), l.6524–6574 (COMP, COMP-F1, (W1)/(W2)), l.6713–6741 (the BFT clause table);
REVIEW_S22.md l.380–436 (the BFT statement, the norm 𝔐, the anti-circularity clause); LINEAR_PACKAGE.md §1.1–§1.5,
§2, §3, §4 headers (Theorems 2.1, 3.8, 4.2, 4.2′, Lemmas 3.1, 3.4, Propositions 3.3, 3.7, Corollary 4.3, the m_*′
table); HANDOFF.md l.40–75.

**Reviewer probes.** Sixteen exact-rational / float probes in plain python (`python3 -I`, `nice -n 10`, no numpy, no
BLAS, no numeric lock — brief rule 6; wall < 1 s each). Scripts and outputs in scratchpad `rev_norms/`
(`r1.py`, `r2.py`, `r3.py`). Record at the end. No numeric job was run and the lock directory was never touched.

**Added after the lead's note** (REVIEW_NQ_S1.md landed mid-review): Part J2, findings RN1-22…RN1-25, binding fixes
13–15, probes R14–R16. I did **not** read REVIEW_NQ_S1.md (budget); the lead's summary is taken as the statement of its
findings, and I verified its two definitional claims independently from PROOF.md, LINEAR_PACKAGE.md, SQ.md and NORMS.md
before recording them.

---

## Bottom line

- **Theorem N1-15 (A_soft = 1/L = 1/3, uniformly in k): CONFIRMED**, at a scope narrower than the file states (RN1-12).
  I rebuilt the load-bearing "single pullback" step from scratch instead of accepting the TOWER-VAR citation; it is
  **correct, and correct for the third derivative specifically** — the two chain-rule terms that would reintroduce a
  per-level recursion vanish, for a reason the file does not spell out and which I give in RN1-10. The exponent
  arithmetic is right; I re-derived it from the definitions at d = 2…6 (RN1-13).
- **The per-level no-go (Theorem N1-13): NOT ESTABLISHED. This is the review's main finding.** Part (i) is true but
  **vacuous** — it is the anchoring identity L^{θ(k−l)} = 1 at l = k, so the level-k value of the norm is
  weight-independent *by construction* (RN1-2) — and **check n1-D, which the file calls "the proof that N-F2 occurs for
  every per-level route", is a tautology in the arithmetic sense: its code computes x + ((d−4) − x) and would PASS for
  any input whatever** (RN1-3, probe R3). Part (ii) is an **upper** bound on an **estimate**, with no lower-bound input
  exhibited, over a class of norms ("scale-covariant") that **the file never defines** (RN1-1). The file's own
  pre-registered outcome **(O3)** (marginal with zero drive + irrelevant complement) is never tested, although the
  evidence it cites for marginality — c38 C — is precisely (O3)'s signature (RN1-5).
- **The "≈ 10³ gain per level" headline: WRONG as stated** (RN1-7, RN1-8). It is obtained by silently setting
  𝔠_vol = 𝔠_ax = 1. The file's own displayed inequality (l.371) forces **𝔠_ax ≳ 5.46, hence 𝔠_ax² ≳ 29.9**, and
  𝔠_vol is Corollary N1-9's **c_m = coth(m′/2)^d**, which the file defines (l.320), uses (l.451) and never evaluates —
  **≈ 3.7 at the most favourable measured decay rate of 𝒦, ≈ 80 at its measured near-field rate, ≈ 7·10⁶ at the proven
  rate m_*′ = 0.0384**. Carrying the file's own constants gives **A_per ≤ 32–49 (gain ≈ 26–39) at 𝔠_vol = 1 and
  A_per ≤ 2.6·10³ (gain < 1, i.e. no gain) at 𝒦's measured near-field rate** (probes R10, R11). The only quantitative
  support for a large gain is c38's measured R_3, which PROOF.md already records correctly.
- **NQ_CHECK is RIGHT, on both counts** (RN1-17). Theorem NQ-1 is correct — I re-derived the telescoping identity by
  induction myself and it is exact, and I re-derived ‖h‖ = d(L²−1)/(4L) by brute force over the block (probes R7, R8).
  (N-Q) is **PROVEN** (abelian/linearised), 𝔮_0 = 11/3 at d = 4, L = 3. NORMS's polynomial sub-estimate is superseded.
  I also located the *arithmetic* slip in NORMS's bullet, which is slightly different from NQ_CHECK's diagnosis (RN1-18).
- **Constructive: (N-loc) is probably not needed at all** for a k-uniform statement on tori of bounded level-k side
  (RN1-20). Every one of Theorem N1-15's four steps uses locality only to replace a torus volume factor T_k^d by c_m —
  and at the *proven* rate c_m ≈ 7·10⁶ ≫ T_k^d for any T_k ≤ 51, so (N-loc) is a **sharpness** question, not an
  existence question. If this holds, Theorem N1-15 becomes unconditional (given NQ-1) at the trivial background, and
  **HANDOFF's "critical path item 1: (N-loc) … Highest value in the project" is misrouted.**
- **The biggest live wall is (N-bg), not (N-loc)** (verdict (e)). Theorem N1-15 bounds the third Taylor coefficient at
  V_k = 1; every consumer (BR1, CURV1 step (6), δ_Sch) consumes a Lipschitz constant on a class. And NQ-1 — the input
  that made the composite route cheap — is abelian/linearised, with PROOF.md's [R3-fix] recording that its key identity
  **has no nonabelian analogue**.
- **Two definitional slips, both verified independently from the primary files and both benign for the conclusions:**
  NORMS **misdefines Q_str** (l.103-104: `L^{d−1}` paths of L links, **81 entries**, where LINEAR_PACKAGE l.71's object
  is the full block average, **135 entries** — NORMS's support is a strict subset) and **conflates M with ev**
  (l.414-415: `Q_str d = d(·|centres)`, where the truth is `Q_str d = d∘M` and `Q_root d = d∘ev`). Every norm NORMS uses
  agrees for both Q_str's, so nothing numerical moves; but l.103-104 contradicts the file's own import (I8), and the
  M/ev conflation is the **second half** of why its (N-Q) bullet owed "h applied to a pure gauge" (RN1-22, RN1-23).
- **The lead's sharpened L-question, answered: `A_soft = 1/L < 1` at EVERY admissible odd L ≥ 3**, not only at L = 3;
  `𝔮_0 = 1 + d(L+1)/(2L)` *decreases* in L (11/3 → 3) and the `𝔮_0 = p_L/L` coincidence at L = 3 carries nothing
  (RN1-24).
- Statuses: of NORMS.md's 23 tally items (l.778-825) I **confirm 13** (items 1, 2, 3, 4, 6, 7, 10, 11, 13, 16, 18,
  plus 12 and 15 *upgraded* by NQ-1), **narrow 4** (items 5, 9, 14, 19), mark **2 WRONG** (item 8's analytic half and
  item 17), and leave **4 unchanged OPEN** (items 20–23). Separately, check n1-D is a vacuous probe.

---

## Part A. Provenance

**RN1-A1 (criteria before script): CONFIRMED, with a timestamp discrepancy.** The filesystem order is
criteria 12:38:20 → script 12:38:55 → output 12:38:59. The rule is satisfied with 35 s to spare. But both
checks/n1_criteria.md l.3 and NORMS.md l.831 say the criteria were written at **"12:41 UTC"**, and the file was never
modified after **12:38:20**. The quoted time is 2 m 40 s *later* than the truth; the same pattern appears in NQ_CHECK
(claimed 13:08, actual 13:07:22). Harmless to the rule, but the file's own provenance numbers do not match the
filesystem and should be corrected rather than relied on.

**RN1-A2 (PRE-STATED first): NOT-VERIFIED from the filesystem.** NORMS.md has **born = mod = 12:57:22**: the inode
carries no trace of the four edits NORMS_LOG records (12:37:28, then §N1–§N10, then two repairs). The only evidence for
the §N0-only first state is NORMS_LOG's self-reported `stat` (size 5524). By contrast NQ_CHECK.md shows
born 13:06:50 < mod 13:16:24, i.e. genuine appends, and NORMS_LOG.md itself was born 12:37:51, 23 s after the claimed
§N0 edit — which is corroborating but indirect. §N0's *content* is clean (statements only; nothing from this session;
T1–T6 contain no exponent and no constant that later sections derive), and the four pre-registered outcomes O1–O4 and
five failure modes N-F1…N-F5 are genuine commitments that the file is then measured against. I record this as
unverifiable, not as a breach. **The brief's instruction "incremental appends" was not followed physically**, and that
is what cost the verifiability.

**RN1-A3 (no session-derived constant inside the criteria): NOT in breach — and that is not the problem.** Every
*constant* in checks/n1_criteria.md (L, d, p_L, K_p^♯, K_ρ^♯, Z_row, Z_col, the §33 weights) is from PROOF.md,
REVIEW_S21 or RTARGET.md, i.e. prior sessions. The three sister-lane breaches of session 24 are not repeated here.
**The problem is the opposite one:** the criteria embed this session's derivation so tightly that three of the four
verdicts cannot fail (RN1-3, RN1-4). A criterion that cannot fail is not pre-registration; it is decoration.

**RN1-A4 (byte accounting): CONFIRMED.** 918 lines / 81173 B matches NORMS_LOG Edit 4 exactly. n1_err.txt is 0 B.
n1_time.txt records 12:38:59 twice (start = end), consistent with a sub-second exact-arithmetic run; no lock was taken
and none was needed.

---

## Part B. The per-level no-go, reframed as a positive claim (the brief's attack 1)

### RN1-1 "A ≥ 1 in every scale-covariant norm family" — the class is UNDEFINED: **WRONG as stated**

`NORMS.md l.86, l.458, l.869` assert the no-go over "every scale-covariant norm family". **The phrase occurs exactly
three times in the file and is never defined** (grep: l.86, l.458, l.869; no definition anywhere). What Theorem
N1-13 (i) actually quantifies over is the **two-parameter family of Definition N^F-1** — the *fixed* leg structure of
Definition N^F-2 (one ℓ¹ divergence-form leg + two ℓ^∞ configuration legs) reweighted by L^{θ_w(k−l)}, L^{θ_A(k−l)}.
That excludes, among others:

- **norms with a Hölder/Campanato leg** — which is what the BFT statement's 𝔐 actually requires
  ("curvature is measured in a Hölder (X_c-type) norm", `REVIEW_S22.md l.394-395`) and what BFT-1 asks for
  ("in Hölder form within each level-k block", `REVIEW_S22.md l.410`). NORMS l.147 claims "The family is 𝔐 restricted
  to what the third-derivative estimate needs. Nothing new is invented" — but the Campanato seminorm of §33's X_f pair
  (`LINEAR_PACKAGE.md l.100`) is dropped, so N^F is a *sub*-family of 𝔐's sup part, not 𝔐 restricted;
- norms with level-dependent **anisotropy** (different weights per direction), non-power weights, ℓ^p legs with
  p ∉ {1, ∞}, and **quotient norms** (e.g. the inf over the admissible gauge class, which is exactly the object Lemma
  N1-2 says is available);
- any norm in which the **estimate itself** changes. This is the decisive omission: the proof of (i) holds the estimate
  of Theorem N1-12 *fixed* and rescales it. A different norm can change which inequality one proves, not merely its
  bookkeeping.

**Honest restatement available on the file's own evidence:** *within the estimate of Theorem N1-12, no choice of the
two level weights delivers A_per < 1.* That is a statement about one estimate, not a no-go over norms.

### RN1-2 Theorem N1-13 (i) is TRUE but VACUOUS: **NARROWED**

I re-derived it (probe R4). With 𝔑^{new}_l = L^{c(k−l)}𝔑^{old}_l, c := (θ_w − 2) + 2(1 − θ_A), the per-level factor
is A^{new} = A^{old}L^{−c} and the level-0 initial condition is scaled by L^{ck}; the product over k levels is
A^{old,k}·M_0, independent of (θ_w, θ_A). I confirm this at 15 pairs including non-integer θ_w = 5/2. **But the reason
is that §33's weights are anchored at level k**: L^{θ(k−l)} = 1 at l = k, so the level-k value of 𝔑 — which is what
the recursion delivers — is weight-independent *by construction* (`NORMS.md l.151-154`, and l.178-182 says it outright:
"the weights CANCEL in 𝔑 … it is the same number organised differently"). (i) therefore says that the answer does not
depend on the bookkeeping used to get it. That is a consistency check on Definition N^F-1, not a no-go ingredient, and
`NORMS.md l.791-793`'s claim that (i) "is what makes the no-go a no-go rather than a failure of imagination" does not
survive.

### RN1-3 Check n1-D is a VACUOUS PROBE: **WRONG** (the file's strongest-labelled computational claim)

`checks/n1_exponents.py` l.86-91:

```
            emis = (F(2) - tw) * 1 + 2 * (tA - F(1)) * (-1)
            emis = -((F(2) - tw) + 2 * (F(1) - tA))      # canonical minus chosen
            total = k * eA + k * (-emis) * 0 + k * 0      # placeholder, replaced below
            # explicit: canonical exponent is d-4; chosen is eA; mismatch per level
            # is (d-4) - eA, and it enters the initial condition k times.
            total = k * eA + k * ((d - 4) - eA)
```

`emis` — the only quantity in the function that is *derived from Definition N^F-1* — is computed twice and then
**discarded**: `total` is overwritten with `k*eA + k*((d−4) − eA) ≡ k(d−4)`, an identity in `eA`. The verdict
`ok &= (F(total,k) == F(d-4))` therefore **cannot fail for any (θ_w, θ_A), any d, any k, or any eA at all**. Probe R3
confirms: the check returns `d−4` for eA ∈ {0, 1, 2, −17, 1/3, 10⁶} at (d,k) = (4,7), (5,7), (3,11). The weight
mismatch is **asserted** as the complement of eA, not computed; the line `# placeholder, replaced below` is the
author's own record that an actual formula was replaced by the tautology.

Consequences: `NORMS.md l.88` ("the weight-invariance half is PROVEN, check n1-D"), l.470-471 ("Checked symbolically in
check n1-D at six pairs … **PASS**"), l.791-793 (tally item 8), l.843-844 (the check record) and l.871 (the request to
PROOF.md) all rest on this. **Only the analytic argument of (i) survives — and RN1-2 shows it is vacuous for a
different reason.** The six pairs establish nothing about all weights; there is no genuine proof of the
weight-invariance half, only the anchoring identity.

### RN1-4 n1-A and n1-B are also non-falsifiable; n1-C has content: **NARROWED**

n1-A reduces to `ok &= (4-4 == 0) and (3-4 == -1) and (5-4 == 1)` (l.31) — three integer identities. n1-B's general-d
clause is `ok &= ((dd-2)-1-1 == dd-4) and ((dd-1)-2-1 == dd-4)` (l.49), again identities. What n1-B and n1-C *do* test
non-trivially is that **two different orderings of the symmetrised vertex, built from two different ingredient lists,
give the same total** — a real (if elementary) consistency check, and it passes. The ingredient exponents themselves are
inputs to the script, never checked by it. The criteria file says as much (`n1_criteria.md l.52-54`), so this is a
labelling problem, not a concealment: but the file's prose (l.476 "the check reproduces the whole power counting")
over-reads it.

### RN1-5 The marginality argument gives the EXPONENT, not the NUMBER — and (O3) is never tested: **WRONG as a no-go**

Marginality fixes only the power of L: `A_per = 𝔠·L^{d−4}·(L²K̄)^a` with `L^{d−4} = 1` at d = 4
(`NORMS.md l.453`, l.474-476). Whether A_per < 1 is then a question about the *pure number* 𝔠·(L²K̄)^a, about which
marginality is silent. Three distinct gaps:

1. **No lower-bound input is exhibited.** Theorem N1-12 proves `M_{i+1} ≤ A_per·M_i`. Theorem N1-13 (ii) concludes
   `A_per ≥ 1`, i.e. that the **bound** is ≥ 1. A no-go needs the **true** per-level factor ≥ 1, i.e. a field, a
   direction or a kernel row realising growth. None is given. The lead applies exactly this standard elsewhere:
   `PROOF.md l.6550-6551`, "read **COMP-F1 occurs [inference, no lower-bound input exhibited]**". The same bracket
   belongs on Theorem N1-13 (ii).
2. **Cancellation between leading terms is not excluded.** A_per is assembled by three separate max-norms
   (𝔎_col and (Z^sm)², l.443) joined by Hölder/triangle steps; the maximising configurations of the three factors need
   not coincide, and 𝔅_p is a signed commutator form. The project has already measured exactly this kind of
   cancellation: `PROOF.md l.6468-6469`, "the absolute counting loses a factor ≈ 22 against the signed kernel at one
   level".
3. **Pre-registered outcome (O3) is never examined.** §N0 l.50-51 registers "(O3) A = 1 (marginality) with zero drive on
   the marginal direction and A_⊥ < 1 on the complement: discharged via a marginal/irrelevant split". The file's own
   cited evidence for marginality is c38 C, whose statement is *verbatim* (O3)'s signature: "**The cubic vertex of E_1^br
   is the Wilson cubic vertex times the quadratic normalisation, both → 1, plus an O(K²) (irrelevant) remainder**"
   (`PROOF.md l.6476-6478`). The file quotes this (l.480-481) only as a *measurement supporting A_per ≥ 1*, and reports
   (O4). (O3) is not established either — `[R22-fix S22-2]` records that c38 C "is silent on the lattice-scale part that
   carries N3" (`PROOF.md l.6480-6481`) — but **neither O3 nor O4 is established, and they have opposite consequences**
   (O3 discharges the clause; O4 kills the route). Reporting O4 is not the honest reading.

### RN1-6 The measured comparator the file quotes but never uses: **CONFIRMED-WITH-FIX (constructive)**

`NORMS.md l.140-141` lists "R_3 ≈ 1.13–1.40" among the measured inputs and then never compares it with A_per. It is the
single most relevant number in the file: c38 B measures the **signed, true, own-units one-level ratio**
N3(T_E)/N3(T_W) = 1.1268 (T = 4), 1.3956 (T = 5), with `R_3(ℤ⁴) ∈ [1.40, ≲ 60]` (`PROOF.md l.6465-6473`). Two
consequences:

- it is **better evidence for A_per ≥ 1 than the marginality argument** — it is a direct measurement of the quantity, and
  it exceeds 1 in every accessible case (though only at the *first* level: `PROOF.md l.6496-6497` records that level 2,
  "whether the irrelevant remainder contracts per level, which is what level-uniformity needs", is NOT shown);
- it **contradicts** the file's own upper bound if 𝔠_vol𝔠_ax² ≈ 1: A_per ≤ 1.38 (l.456) against a measured ℤ⁴ lower
  bound of 1.40. The contradiction is resolved only by 𝔠_vol𝔠_ax² > 1.014 — which RN1-7/RN1-8 show is true by a wide
  margin, and which destroys the gain headline.

---

## Part C. Theorem N1-15's "single pullback" — rebuilt, not accepted (the brief's attack 2)

### RN1-10 The single pullback holds **for the third derivative**: **CONFIRMED (rebuilt)**

`PROOF.md l.6512-6514` states TOWER-VAR (d); its proof (l.6520-6523) is three lines and asserts that "the chain-rule
terms of the third derivative vanish by criticality". The brief is right that this is where a per-level recursion could
hide, so I rebuilt it. Write the fluctuation block (all levels j < k) as A, the data as B, Z(B) := (a(B), B), so
Z′ = (a′, 1), Z″ = (a″, 0), Z‴ = (a‴, 0). Then

  D³(𝔉∘Z) = D³𝔉[Z′, Z′, Z′] + 3·D²𝔉[Z″, Z′] + D𝔉[Z‴].

- `D𝔉[Z‴] = ⟨𝔉_A, a‴⟩ = 0`, because Z‴ has no B-component and 𝔉_A = 0 along the critical family.
- `D²𝔉[Z″, Z′] = ⟨a″, 𝔉_{AA}a′ + 𝔉_{AB}⟩ = 0`, because differentiating the identity `𝔉_A(a(B), B) ≡ 0` once in B gives
  `𝔉_{AA}a′ + 𝔉_{AB} = 0`.

So **both** potentially dangerous terms vanish, and the vanishing uses only *first*-order criticality — which is why the
statement is true at third order and not only at first/second. The derivatives of the minimiser map that the brief
worried about **do exist and do appear; they are annihilated, not dropped.** Two caveats I attach:

- the derivation requires the critical family to be **C³ in B** (a″, a‴ must exist to be written down and annihilated);
  that is supplied by Lemma SC1's hypothesis "a real-analytic family of critical points" (`PROOF.md l.6198-6200`), and
  the file should cite it where it uses TOWER-VAR (d) rather than leaving it implicit;
- `𝔉_{AA}` is **not invertible** (it annihilates gauge directions), so a′ is determined only modulo gauge and the
  equation `𝔉_{AA}a′ = −𝔉_{AB}` is solvable only because 𝔉_{AB} is orthogonal to the gauge directions. That is exactly
  Lemma N1-2's freedom, and it is used consistently.

With `𝔉_k`'s quadratic part at the trivial point equal to Setting SC's chain energy (TOWER-VAR (c), `PROOF.md
l.6509-6511`; `LINEAR_PACKAGE.md l.85-89`), `ζ^c = a′(0)` is indeed the **linear composite chain-minimiser map**, so
`D³E_k^br(1) = D³𝔉_k(1)[ζ^c·, ζ^c·, ζ^c·]` is a single pullback by one linear map. **There is no per-level recursion
here, and no per-level covariance.** CONFIRMED.

### RN1-11 Lemma N1-2 and Lemma N1-6: **CONFIRMED-WITH-FIX (one statement is wrong as written; the use is right)**

Lemma N1-2 (l.228-243) is correct: `𝔉_{AA}` annihilates the fluctuation-gauge directions at a critical point (the
second derivative of gauge invariance at fixed data, with 𝔉_A = 0), so `𝔉_{AA}D_UΛ′ = 0` and E3's derivation goes
through verbatim; the admissible class "trivial at the coarse centres of the level whose data is held fixed" is the
right one.

But **Lemma N1-6's parenthesis "(so the family is an admissible reparametrisation in the sense of Lemma N1-2)"
(l.304-305) is false as written.** The interpolant family has `λ̂_k = λ ≠ 0` at the level-k sites, so it is **not**
trivial at the level-k centres; a gauge transformation nontrivial at the top changes the *data*, so it is not a
reparametrisation at fixed data. The *use* in Lemma N1-11 is nevertheless legitimate, for a reason the file does not
give and which I supply: for pure-gauge data `Y = d_kλ` the chain `B_j = d_jλ̂_j` has `r_j = Q d_jλ̂_j − d_{j+1}λ̂_{j+1}
= d_{j+1}(ev λ̂_j) − d_{j+1}λ̂_{j+1} = 0` by nesting and root covariance, and `d_0B_0 = 0`, so it is a **zero-energy,
hence global, minimiser**; and the *difference* between two chains for the same data Y is trivial at level k, i.e. in the
fluctuation gauge group. So `ζ^c_sm − ζ^c` is admissible even though neither summand's gauge is. **Fix:** replace the
parenthesis by that two-line argument.

I also verify that `ζ^c_sm` is a single **linear** map, not a Y-dependent choice (the axial λ(Y), the interpolants
λ̂_j(Y) and the level-0 gauge are each linear in Y) — necessary, because the identity of RN1-10 requires *one*
representative applied to all three legs simultaneously. The file does not state this; it matters and it is true.

### RN1-12 Theorem N1-15: **CONFIRMED, at a narrower scope than stated**

The proof's four steps are correct as exponent statements (RN1-13), the constants are k-independent, and the sum is
dominated by n = 1 (the *top* of the tower), consistent with §N5's own remark at l.494-496. Scope corrections:

- **d = 4 only, not "every d ≥ 2"** (l.509 "general d displayed", l.517 "in every d ≥ 2", l.575 "The result is true for
  every d ≥ 2"). Every imported input is d = 4: `LINEAR_PACKAGE.md l.56` hard-codes the block as
  `B(X) = LX + {0,…,L−1}⁴`; J-str (c)'s decay is written `L^{−3(k−1−i)}` and `‖Q_str^T‖_{∞→∞} = L^{−3}`
  (`LINEAR_PACKAGE.md l.166-171`); Lemma 2.2's constant is `L^{4−d}`. The d-generality is **exponent bookkeeping, not a
  theorem.** NARROWED.
- **abelian/linearised at the trivial background** — correct for ζ^c (the su(N) algebra splits into N²−1 copies around
  the trivial background, `LINEAR_PACKAGE.md l.57-58`), and the vertex is genuinely nonabelian (M_W, M_S carry it). But
  (N-Q)'s proof is abelian-only (NQ_CHECK §Q3 scope paragraph), so nothing here transfers to a background.
- **the constant is not O(1)** (RN1-9).
- **it bounds a different object from the one (H-C) names** (RN1-16).

---

## Part D. The exponent arithmetic (the brief's attack 3)

### RN1-13 **CONFIRMED** by independent re-derivation; §N6/§N7 use the correct form everywhere

Probe R1 recomputes the soft exponent from the definitions — volume `d·n`, residual decay `−(d−1)(n−1)` (J-str (c)),
two potential legs `−n` each — at d = 2, 3, 4, 5, 6 and n = 1, 2, 3, 5:

  `d·n − (d−1)(n−1) − 2n = (d−1) − n`  at every (d, n).

So the residual ℓ¹ mass exponent is `n + (d−1)` (l.543) and the total is `(d−1) − n` (l.546, l.551) — both correct. The
Wilson count `(d−2)k − k − k = (d−4)k` and the swapped ordering `(d−1)k − 2k − k = (d−4)k` (l.529-537) are correct. §N7's
general table (l.650-651) is correct: `(d − θ_w^r − 2θ_A)n + θ_w^r` and `(d − θ_w^c − 2θ_A)k`, reducing to `(d−1) − n`
and `0` at (θ_w^c, θ_w^r, θ_A) = (2, 3, 1). I found **no place in §N6 or §N7 that uses the defective form**, and **no
conclusion depends on it**. The file's disclosure (l.839-842) is accurate as far as it goes.

### RN1-14 The disclosure is INCOMPLETE: the check's *ratio* label is also wrong off d = 4: **CONFIRMED-WITH-FIX**

`n1_exponents.py` l.65-67 computes `ratio = 1/L^{5−d}` and prints "per-level ratio L^(d−5)". The **correct** A_soft is
`L^{−1}` for every d (probe R2: the n-coefficient is `d − (d−1) − 2 = −1`, independent of d). The two agree at d = 4
only. So the script's reading says **A_soft = L⁰ = 1 at d = 5 and L¹ > 1 at d = 6** — directly contradicting the file's
own l.517 ("A_soft = 1/L = 1/3 < 1 in every d ≥ 2") and l.575. §N6 is right and the check is wrong, but the disclosure
at l.839-842 covers only the exponent formula `(d−5)n+3`, not the ratio label. **Fix:** extend the disclosure to the
ratio, and state that the correct per-level ratio is L^{−1} in every d, with `L^{d−5}` an artefact of the hard-coded 3.

---

## Part E. Anti-circularity (the brief's attack 4)

### RN1-15 "SATISFIED by construction" (l.504-505, l.698): **CONFIRMED** — I checked, it is not merely asserted

The clause is `REVIEW_S22.md l.422-423`: "the proof may not use the per-level covariances C^{(j)} as Newton inverses".
I traced every linear input of §N6:

- **Theorem N1-15's proof** cites TOWER-VAR (d), Lemma N1-2, Lemma N1-1, Lemma N1-11, Lemma N1-7, (I3), (I4), (I5),
  (N-loc). It does **not** cite Lemma N1-3, which is the only place `C^0` appears; N1-3 is used in §N5 (Theorem N1-12)
  and in Proposition N1-10 only. CONFIRMED.
- **Lemma N1-11** uses Lemma N1-5, Lemma N1-6, (I3), (I4), (N-Q) — no covariance.
- **(N-Q)/Theorem NQ-1** uses only Q_str, h and ev — no covariance.
- **The imported inputs are composite, not per-level inductions.** This is the step that had to be checked and it holds:
  N2-lin (Thm 3.8) is proved through **Lemma 3.4's single composite dual operator** `P = Σ_m (κ/κ_{k−1−m})
  Q_str^{(L^m)}Q_str^{(L^m)T} + κ Q_str^{(n)}Δ^{−1}Q_str^{(n)T}` (`LINEAR_PACKAGE.md l.186-191`) plus the symbol bounds
  of Lemma 3.6, and J-str's proof is Euler–Lagrange plus an induction on co-closedness (`l.166-171`) — no level-by-level
  inversion anywhere.
- `ζ^c` is itself the inverse of the **composite** Hessian restricted to fluctuations, which is what the clause permits.

One narrowing: `𝔚`, `𝔖` and `𝔠_P` are k-independent, so no per-level constant's k-th power appears (l.591-592 is right).

---

## Part F. The margin "exactly one power of L" (the brief's attack 5)

### RN1-19 **CONFIRMED**, and the fragility is not in L

- `A_soft = L^{−1} < 1` for **every** L ≥ 2 and every d (probe R2), so there is no L = 3 special case; the only
  L-dependence is the prefactor `L^{d−1}/(L−1)` (= 13.5 at d = 4, L = 3), which grows like L^{d−2} and makes the
  *constant* worse at larger L while leaving the ratio untouched. **A_soft < 1 survives at every admissible odd L ≥ 3.**
- The margin is a margin **in the exponent pair**, and there it is exactly zero slack: `d − θ_w^r − 2θ_A = −1` at
  (θ_w^r, θ_A) = (d−1, 1), so any degradation of either exponent by any positive amount gives A_soft ≥ 1. Both are
  delivered exactly: θ_w^r = d−1 = 3 is J-str (c) (PROVEN, frozen), θ_A = 1 is Lemma N1-11 (now PROVEN given NQ-1).
  §N7 l.662-663 and Remark N6-1 l.574-575 state this correctly.
- **Rounding direction.** The conservative roundings are at l.282 (`L^{−3(k−j)} ≤ L^{−2(k−j)}`) and l.398 (the same
  relaxation) — both against the file's interest, correctly. The **favourable** roundings are in Lemma N1-11 step (5),
  l.399: "use θ ≤ 2d|Y|_∞ and |d_kλ|_∞ ≤ 2|Y|_∞; absorb 2d into 𝔠_P's displayed factor 2" — 2d = 8 is absorbed into a
  factor 2, and **`|d_kλ|_∞ ≤ 2|Y|_∞` is false**: `d_kλ = Y − Y′` with `|Y′|_∞ ≤ c_AX R_eff|d_kY|_∞ ≤ 2d c_AX R_eff
  |Y|_∞`, so the true bound is `(1 + 2d c_AX R_eff)|Y|_∞` — 25|Y|_∞ already at R_eff = 1, d = 4, c_AX = 3 (probe R9).
  **Both affect 𝔠_P only, not an exponent**, so Theorem N1-15's conclusion is unaffected; 𝔠_P must gain a term
  `1 + 2d c_AX R_eff`. CONFIRMED-WITH-FIX.
- Lemma N1-4's own arithmetic I re-derived: at d = 4 the i-th term's exponent is `(j−1−i) − 3(k−1−i) = j + 2 − 3k + 2i`,
  the geometric sum with ratio L² is dominated by i = j−1 and equals `4L^{j+2−3k}(L^{2j}−1)/(L²−1) ≤ 4L²/(L²−1)
  L^{−3(k−j)}` — correct as printed (l.279-281), and the independent agreement with SQ's REG-lin (d) constant
  (l.283-285) is a genuine second derivation of the same number.

---

## Part G. The constants the file does not carry — the gain headline (my principal numerical attack)

### RN1-7 `𝔠_ax ≳ 5.46`, from Proposition N1-10's **own** displayed inequality: **WRONG headline**

`NORMS.md l.371` displays

  `|ζ_sm B|_∞ ≤ L^{−1}·[(d−1)·L·|d(ζB)|_∞·L + |B|_∞ + K_ρ|d_1B|_∞] ≤ 𝔠_ax·L^{−1}·(|B|_∞ + |d_1B|_∞)`

with `|d(ζB)| = |𝒦d_1B| ≤ K̄|d_1B|` (Lemma N1-3). Bounding the bracket by `𝔠_ax(|B|_∞ + |d_1B|_∞)` therefore forces

  `𝔠_ax ≥ (d−1)L²K̄ + K_ρ = 5.4644` at (K̄, K_ρ) = (0.1202, 2.219), `= 5.9512` at (0.1236, 2.614), `= 5.0740` at
  (1/9, 2.074)  — probe R10.

So `𝔠_ax² ≳ 25.8–35.4` and `Z^sm ≤ 𝔠_ax/L ≈ 1.69–1.98`. The file's reading at l.375-379 — "**The smooth-sector value
is exactly L^{−1} = 0.333**, against the measured Z_row = 2.849: a factor **8.55** per leg, 73 in the two legs" — is the
value at 𝔠_ax = 1, i.e. with the first and third terms of its own bracket deleted. The honest per-leg gain from the
file's own inequality is `2.849/1.82 ≈ 1.6`, not 8.55; the two legs give ≈ 2.4, not 73. Pre-registered failure mode
**N-F3 is flagged at l.376-377 and then not applied to the headline.**

### RN1-8 `𝔠_vol = c_m = coth(m′/2)^d` is defined, used, and never evaluated: **WRONG headline**

`𝔠_vol` is the max-vs-average slack of Corollary N1-9, i.e. precisely `c_m = (coth(m/2))^d` (l.348-350, l.320, l.451).
It is never given a number. Probe R5:

| m′ | source | `c_m = coth(m′/2)⁴` |
|---|---|---|
| 1.817 | 𝒦's measured **far** step 3.2e-4 → 5.2e-5 (c37 B) | **3.71** |
| 1.036 | the *located, numerically, NOT proven* chain rate (LINEAR_PACKAGE l.245) | **19.5** |
| 0.696 | 𝒦's measured **near-field** step 0.315 → 0.157 (c37 B, the step that carries the mass) | **79.6** |
| 0.0384 | the **proven** rate `m_*′` at κ = 1, L = 3 (Thm 4.2′, LINEAR_PACKAGE l.244) | **7.4·10⁶** |
| 1e-10 | the proven rate for `C^{(i)}` quoted at PROOF.md l.6242 | **1.6·10⁴¹** |

The file *knows* that `coth` of a small rate is astronomical: `NORMS.md l.760` uses `coth⁴(m_1/2) ≈ 5.9·10²⁰`. The same
object is treated as ≈ 10²⁰ in §N9 and as ≈ 1 in §N1/§N5.

**Combining RN1-7 and RN1-8 (probe R11):**

| 𝔠_vol taken at | A_per ≤ | gain over 1266.87 |
|---|---|---|
| 1 (what the headline assumes) | 32.3–48.8 | **26–39** |
| 𝒦's far measured rate (3.71) | 120–181 | 7.0–10.6 |
| 𝒦's near measured rate (79.6) | 2.6·10³–3.9·10³ | **0.33–0.49, i.e. NO GAIN** |
| the proven rate (7.4·10⁶) | 2.4·10⁸–3.6·10⁸ | 4·10⁻⁶ |

against the file's headline `920–1171` (l.84, l.456, l.846, l.872), which probe R12 reproduces exactly as
`1266.87/(L²K̄)^a` — i.e. with 𝔠_vol = 𝔠_ax = 1. **The claim "a gain of ≈ 10³ per level" is not established at any
decay rate the project has, measured or proven.** The *measured* gain, from c38's signed ratio, is
`1266.87/R_3 ∈ [21, 905]` (probe R13) — and `PROOF.md l.6490-6492` already records the sound version of it ("at least
≈ 20 times below E3's 1267. The signed value on ℤ⁴ is not measured").

### RN1-9 The composite constant `𝔚 + 13.5𝔖` is ≳ 10⁷ at proven rates: **NARROWED**

The same `c_m` sits inside `𝔚` and `𝔖` (l.513-514), and (N-loc)'s near/far trade adds `R_eff^d` with
`R_eff ≳ 1/m_*′ ≈ 26` (l.430-432), i.e. `R_eff⁴ ≈ 4.6·10⁵`. So the level-uniform number Theorem N1-15 delivers is
≳ 10⁷ and plausibly ≳ 10¹³, against the measured object `N3(T_E) ≈ 4.2` (T = 5) and `N3^abs ≲ 170` on ℤ⁴
(`PROOF.md l.6472-6473`). Two readings follow, both of which should be recorded:

- the bound is **consistent** with c38 and in no tension with it — but it is ≈ 10⁶ times loose, so it is not a
  sharpness statement about the vertex, only a uniformity statement;
- **§N9's margin claim should be re-checked with that value.** l.900 says "288𝔠_∞³C_♭ ≈ 9.0·10⁹C_♭ far below" the
  binding `288A_in coth⁴(m_1/2)ℓ_θ ≈ 10²⁰–10⁴²`. At C_♭ ≈ 10⁷ the term is ≈ 9·10¹⁶, still below 10²⁰ — so §N9's
  conclusion survives, by about three orders at the session-23 m_1 rather than "far". At C_♭ ≈ 10¹³ it would not.

### RN1-7b "Z_col·Z_row² is a norm artefact" contradicts the file's own §N2: **CONFIRMED-WITH-FIX**

`l.82` ("Z_col·Z_row² ≈ 1.27·10³ is a norm artefact") against `l.178-182` ("at the canonical weights the weights CANCEL
in 𝔑 … the curvature-adapted norm is NOT weaker than the N_0 norm the consumers use, **it is the same number organised
differently**"). I verified the cancellation: at (θ_w, θ_A) = (2, 1), `𝔑_{l,0}(T) = N3(T)/(2(d−1))` exactly. If the
norm is the same number, the 10³ cannot be a norm artefact. It is an **absolute-value-counting artefact** of the
estimate: the gain comes from Lemma N1-1 (one differentiated leg per term) plus Lemma N1-3 (the input is exact), not
from changing the norm. `PROOF.md l.6249-6251` already says exactly this ("absolute-value N_0 norms … count every fine
leg at its sup size, whereas the d = 4 cubic vertex is marginal only after one leg is differentiated"). **Fix the
framing in l.82 and in FOR-OTHER-FILES item 2.**

### RN1-7c The claim that PROOF.md's diagnosis is **wrong**: itself WRONG

`l.361-365` and FOR-OTHER-FILES item 2 (l.866-872) ask PROOF.md to "correct the CURV-F2 diagnosis", on the ground that
"PROOF.md's diagnosis named 'the L^{d−1} = 27 crossing links of one coarse link times the spread'; the correct count is
L^d·K̄ ≈ 9.7 … and the crossing-link count does not appear at all". PROOF.md l.6249 reads "**Z_col ≥** the L^{d−1} = 27
crossing links of one coarse link times the spread". That is a statement about **Z_col**, and it is **true**: for a
coarse delta, `Jδ_c` occupies the L^{d−1} = 27 crossing fine links with value 1 each, so the column ℓ¹ mass is ≥ 27
(measured 156.08). NORMS's own l.365 concedes the mechanism ("the L^{d−1} crossing links are an artefact of the lift J,
which acts only on the potential"). PROOF.md is not wrong about Z_col; NORMS is describing a **different object** (the
column mass of 𝒦 in the field-strength norm). The lead's DRIVE_BRIEF D3 records the diagnosis as "believed correct" —
it is correct. **Fix:** item 2 must be reworded as an *addition*, not a correction. As a correction it would put a false
erratum into the master ledger.

---

## Part H. NQ_CHECK vs NORMS — the fork the lead asked me to settle (the brief's attack 6)

### RN1-17 **NQ_CHECK is RIGHT. (N-Q) is PROVEN.** Theorem NQ-1 rebuilt and confirmed

I did not accept NQ_CHECK's proof either. Rebuilt:

- **Step 1 (the telescoping identity).** With `Q_i = S_i − D_{i+1}H_i` (the slice identity) and `Q_iD_i = D_{i+1}E_i`
  (root covariance), induction on j gives
  `Q^{(j+1)} = Q_jQ^{(j)} = S_jS^{(j)} − (S_j − D_{j+1}H_j)D_jΣ(...) − D_{j+1}H_jS^{(j)}`, and the middle term is
  `−Q_jD_jΣ(...) = −D_{j+1}E_jΣ(...)`, so
  `Q^{(j+1)} = S^{(j+1)} − D_{j+1}Σ_{i≤j}(E_j⋯E_{i+1})H_iS^{(i)}` — **exactly NQ_CHECK §Q3 Step 1.** The induction uses
  root covariance on the **full** Q_j, not on S_j; that is the whole trick and it is sound. NQ_CHECK's own post-hoc
  entrywise check (§Q6, 0 of 459 and 0 of 47 385 entries differing at j = 1, 2) is correctly labelled post-hoc and is
  corroboration, not the proof.
- **Step 2.** `‖S^{(i)}‖_{∞→∞} = L^i` (non-negative entries, constant row sums `L^{−d}·L^d·L = L`) ✓;
  `‖E⋯E‖ = 1` ✓; `‖D_j∘G‖ ≤ 2‖G‖` ✓; and `‖h‖ ≤ avg_{y∈B(X)}|y − c_X|_1 = d(L²−1)/(4L)` — which I re-derived by brute
  force over the whole block (probe R8): exactly 8/3 at (d, L) = (4, 3), 2 at (3, 3), 24/5 at (4, 5), matching the
  closed form in all three cases.
- **Step 3.** `‖Q^{(j)}‖ ≤ L^j + (d(L²−1)/(2L))(L^j−1)/(L−1) ≤ L^j[1 + d(L+1)/(2L)]`, i.e. `𝔮_0 = 11/3` at d = 4,
  L = 3 ✓ (probe R7: the bound is 25/3, 91/3, 289/3 at j = 1, 2, 3, which dominates the computed 205/27, 2021/81,
  6115/81 by 10 %, 22 %, 28 % — the slack is exactly where the triangle inequality was used).
- **Torus:** periodisation merges columns and can only decrease a row ℓ¹ sum ✓.
- **Scope:** abelian/linearised, as §Q3 states, because input (i) has no nonabelian analogue — **`PROOF.md
  l.1159-1161`**, L3g(a)-slice [R3-fix]: "*h depends on A, and the identity is linearised and abelian only: the
  nonabelian straight average is not even covariant, so there is no nonlinear SU(N) analogue*" (NQ_CHECK cites
  l.1123-1125; see RN1-21). Honest and load-bearing — see verdict (e).

So: **NORMS tally item 15 moves ARGUED → PROVEN; item 12 (Lemma N1-11) CONDITIONAL → PROVEN-HERE with 𝔮_0 = 11/3
substituted into 𝔠_P (with RN1-19's 𝔠_P repair); items 13 and 14 become CONDITIONAL on (N-loc) alone.** NQ_CHECK's
FOR-OTHER-FILES item 1 is correct and should be applied verbatim.

### RN1-18 The *cause* of NORMS's polynomial estimate: NQ_CHECK's attribution is approximately right; the actual slip is arithmetic

NQ_CHECK §Q4 says the `j`-dependence "came from organising the expansion so that h had to be applied to a pure gauge at
every level" / "an artefact of expanding Q^j with the block mean M (self-referential)". The file's bullet
(`NORMS.md l.413-417`) reads: "Each term with its first h at level i contributes ≲ ‖h‖·L^{j−1−i}·L^{i} = ‖h‖L^{j−1}
**if the subsequent factors act on it as Q_str does on a pure gauge (Q_str d_iμ = d_{i+1}(μ|centres), which does not
grow the gauge function)**, giving 𝔮_0 ≤ 1 + 2d‖h‖·j/L". That sentence is **internally inconsistent**: it assigns the
post-h factors a growth `L^{j−1−i}` in the same breath as declaring that they do not grow the gauge function. With the
post-h factors correctly at norm 1 (NQ-1's `‖E⋯E‖ = 1`), the sum is the **geometric** `Σ_i L^i = (L^j−1)/(L−1)`,
dominated by i = j−1, giving a bounded 𝔮_0; NORMS's `j·L^{j−1}` double-counts. Both diagnoses reach the same verdict,
and NQ_CHECK's is the more useful one (it names the right covariance, `Q∘d = d∘ev` rather than `Q_str∘d = d∘M`). **The
superseded items in NORMS.md are: the l.415-417 estimate and its named hole, and [N1-corr 1]'s cases 2 and 3
(l.599-604).** Case 1 holds.

One correction to NQ_CHECK's own request: its FOR-OTHER-FILES item 1(a) asks NORMS to withdraw a §N4 bullet quoted as
"*The files are ambiguous about what Q actually is*". **That sentence does not occur in NORMS.md.** The nearest text is
FOR-OTHER-FILES item 1, l.860-862 ("The evidence is mixed in the files"). The substance of the request stands; the quote
is not verbatim and should not be propagated as one.

### RN1-21 NQ_CHECK's PROOF.md line citations are systematically off, and one cited object is absent: **CONFIRMED-WITH-FIX (content sound, citations not)**

I checked every file:line in NQ_CHECK §Q1 and §Q3. **Every quotation's text exists and is accurate**; the line numbers
for PROOF.md are drifted by 30–60 lines, while those for RTARGET.md, SQ.md and LINEAR_PACKAGE.md are right:

| NQ_CHECK cites | actual location | quote verified |
|---|---|---|
| PROOF l.2060 (Setting SC: "Q_root of L3g(a)-slice, with the S4' order average") | **l.2096** | yes |
| PROOF l.2090 (root covariance Q∘d = d∘ev) | **l.2126** ("Hence d*Q^T = ev^Td*") | yes |
| PROOF l.1127-1131 / l.2093-2094 (the slice identity) | **l.1159** (L3g(a)-slice header), l.1121, l.2096 | yes |
| PROOF l.1123-1125 ([R3-fix], no nonabelian analogue) | **l.1159-1161** | yes |
| PROOF l.2545 ("a composite of root maps equals Q_str^{(L^m)} plus a coarse exact form") | **l.2581** | yes |
| PROOF l.1134 ("h(A + dλ) = h(A) + Q_0λ − λ(c)") | **l.1170** | yes |
| RTARGET l.414; SQ l.655, §0.4 l.352-357, l.709-711, l.411; LINEAR_PACKAGE l.70-73, l.166-171 | correct (±1) | yes |
| **PROOF l.2787, l.2980: "h^{(m+1)} = Mh^{(m)} + hQ^{(m)}"** | **not found** — the notation `h^{(m)}` occurs **nowhere** in PROOF.md; l.2787 is Proposition PG and l.2980 is the N6 rate discussion | **no** |

The last row matters for RN1-18: NQ_CHECK's stated *cause* ("an artefact of expanding Q^j with the block mean M …
`h^{(m+1)} = Mh^{(m)} + hQ^{(m)}`, self-referential") rests on an object I cannot locate. The **substantive** mechanism
is however genuinely in PROOF.md, at **l.2581**: "*Q_root = Q_str − dh at each level and **Q_str d = dM**, so a
composite of root maps equals Q_str^{(L^m)} plus a coarse exact form*" — PROOF's own IT-str route does push the exact
form past `Q_str` (covariance `Q_str d = dM`) rather than past the full `Q` (covariance `Q d = d·ev`), which is exactly
the organisation NORMS inherited. And `h∘d = M − ev` follows from l.1170. So NQ_CHECK's diagnosis is **right in
substance, with one unverifiable citation**, and Theorem NQ-1 itself depends on neither: its only two inputs are the
slice identity and root covariance, both of which I verified in place and rebuilt. **Fix:** replace the l.2787/l.2980
citation with l.2581 (+ l.1170), and correct the six drifted PROOF.md line numbers before the lead follows them.

---

## Part I. "An alternative to BFT-4" (the brief's attack 7)

### RN1-16 **NARROWED** — it is an alternative route to one sub-clause of one consequence, and the clause it discharges is not the clause (H-C) names

Remark N8-1 (l.702-719) is honest and I endorse most of it: Theorem N1-15's inputs are TOWER-VAR (d), Lemma N1-1, the
frozen N2-lin / J-str / N2-exp, Lemma AX and the two named inputs, and they genuinely avoid (CovLift), (Mult-Y),
(Pair-loc), (I-id) (`PROOF.md l.6733`). But the scope is three nested restrictions deep:

1. **one clause** — C_♭ — of the **Cauchy corollary** of BFT-4 (`REVIEW_S22.md l.414-418`), not of BFT-4;
2. **third order only**, at the **trivial background**; and route (ii) of (N-bg) *is* BFT-4's own Cauchy argument, in
   which Theorem N1-15 becomes the n = 3 instance of what BFT-4 must prove at every n (l.712-715, correctly stated);
3. `PROOF.md l.6733` records **BFT-4 at k = 1 as already PROVEN** for the gauge-invariant pieces, so the added value is
   k ≥ 2 only.

And the clause is not the clause: **(H-C) names `C_♭^{(i)}`, the N_0-Lipschitz constant of `Hess E_i^br` on the
small-field class** (`PROOF.md l.6206-6210`, l.6220-6221). Theorem N1-15 bounds `N3(D³E_k^br(1))`, the third Taylor
coefficient at `V_k = 1`. There is **no "(H-C) at the trivial background" clause** in NAH-unif, so the phrase "(H-C)'s
C_♭ clause is therefore discharged at the trivial background" (l.584, l.96, l.805) names something that does not exist.
Remark N6-5 (l.622-638) says this correctly and §N8's table row (l.691) says it correctly; the headline and Remark N6-2
do not. **Fix:** say "the third Taylor coefficient of E_k^br at the trivial background is level-uniform; (H-C)'s C_♭
clause is NOT discharged — it is a statement on the class, and (N-bg) is OPEN."

I confirm the two honest negatives, which are the best-written parts of the file: **§N8's "NOT IN SCOPE — untouched" row
for 𝔠_∞, A_in, A_out, c_K, 1/m_1, Z-tails (l.692)**, and **§N9's refusal to claim any improvement in ε_1 or g_K²
(l.741-770, l.897-902)**. §N9's correction of the brief's own premise ("it is the origin of the depth-dependence, not of
the magnitudes", l.752-754) is right and valuable, subject to RN1-9.

Also NARROWED: §N8's BFT-1 row (l.697) claims θ_w^c = 2 and θ_A = 1 are "**SUPPLIED**". They are supplied in **sup**
form; BFT-1 asks for them "in Hölder form within each level-k block" (`REVIEW_S22.md l.410`) and 𝔐 requires a Hölder
(X_c-type) curvature norm (`l.394`). The Hölder half is not supplied.

§N7's load-bearing negative — **with a single common θ_w ∈ (0, 2], `θ_w + 2min(1, θ_w − 1) > 4` has no solution, so
BFT-1 as stated is insufficient and must be stated as the pair (θ_w^c, θ_w^r) = (2, d−1)** — I verified
(l.656-676; at θ_w = 2 the condition reads 4 > 4, and for θ_w < 2 it reads 3θ_w − 2 > 4). **CONFIRMED, and it is the
second most valuable thing in the file.** One addition the file should make: with a single θ_w = 2 one gets A = 1
exactly, hence `C_♭^{(k)} ≲ k` (linear), not divergence — worth recording next to [N1-corr 1]'s k² fallback.

---

## Part J. Constructive: (N-loc) looks unnecessary for bounded-T_k tori

### RN1-20 **ARGUED (reviewer's own sketch, one step to check)** — and it reverses the lead's critical path

Locality enters Theorem N1-15 in exactly one way: to convert a sup bound into an ℓ¹ mass, Lemma N1-7 replaces the
number of level-l objects in the *whole torus* by `n_τ(l)·c_m`. Take instead the torus volume factor directly. With
`T_k` the level-k side (k-**independent** in this RG tower: the level-0 side is `T_kL^k`), the level-j count is
`dT_k^dL^{dn}`, so each of the four steps goes through with `c_m ↦ T_k^d`:

- step (1): `(d(d−1)/2)T_k^dL^{dk}·C_fL^{−2k} = const·L^{(d−2)k}` — uses (I3) only, not (I5);
- step (3): `dT_k^dL^{dn}·κ̂C_RL^{−(d−1)(n−1)} = const·L^{n+(d−1)}` — uses (I3)+(I4) only;
- steps (2), (4): `dT_k^dL^{dn}·𝔠_PL^{−n} = const·L^{(d−1)n}`.

Every exponent is unchanged; `c_m` is replaced by `T_k^d`. And at the **proven** rate `c_m ≈ 7.4·10⁶ = 52⁴`, so
**`T_k^d` is the cheaper constant for any `T_k ≤ 52`.** The one step that genuinely needs replacing is Lemma N1-5: an
axial gauge needs a non-wrapping box. On the torus I would use the Hodge/Coulomb gauge instead: decompose
`B = dλ + d^*G + h`; the flat part `h` needs no gauge and is realised at level j with own-units size `L^{−(k−j)}|h|`
(check: `Q`(constant) = L·(constant), so `r_j = 0` and `d_jB_j = 0`, i.e. `h_j = L^{−(k−j)}h_k` is the exact minimiser);
the exact part is Lemma N1-6; and for the co-exact part `d^*Δ^{−1}dB` the kernel is `|x|^{−(d−1)}`, whose ℓ¹ mass over a
torus of side R is `O(R)` in d = 4 — **the same `c·R·|dB|_∞` that Lemma N1-5 gives axially**, so step (3) of Lemma N1-11
survives with `R_0 = T_kL^k` and still yields `|B_0|_∞ ≲ T_kC_fL^{−k}θ`.

**If that holds, Theorem N1-15 is unconditional at the trivial background** given NQ-1, with `𝔠 ∝ T_k^d` in place of
`c_m`, and **(N-loc) is a sharpness question (the ℤ^d / T_k-uniform statement), not an existence question.** The step to
check is the one I have only sketched: the torus Hodge bound `|B^{coex}|_∞ ≤ c_d·R·|dB|_∞` in d = 4, uniformly in R, and
whether the resulting `T_k`-dependence is acceptable to the consumers (NAH-unif requires `T_j ≥ the level-j sizes`,
`PROOF.md l.6235`, i.e. a lower bound on T_k, not an upper one — so a `T_k`-dependent constant is a real restriction,
but a far weaker one than an open multi-scale axial gauge). **This directly bears on HANDOFF.md l.55-62, which routes
the project's "highest value" at (N-loc).** It should be checked before anyone spends a session on the multi-scale axial
gauge.

---

## Part J2. Addendum after the lead's note (REVIEW_NQ_S1 landed; its three in-scope findings checked here)

I did not read REVIEW_NQ_S1.md (budget); the lead's summary is taken as the statement of its findings, and I verified
each of the two definitional claims **independently, from the primary files**, before recording them. I take the
entrywise ev-form/M-form identity (0 of 23 328 at j = 2; `h∘d = M − ev`, 0 of 81) as settled and did not redo it; it
agrees with my own hand derivation in RN1-17/RN1-18, and I note below where my reading of the *cause* now sharpens.

### RN1-22 NORMS misdefines Q_str — 81 entries where the object has 135: **CONFIRMED (independently), benign, must be corrected**

`NORMS.md l.103-104`: "*Q_str, its straight part, Q_str B(c) := L^{−(d−1)}Σ_{paths}Σ_{b∈path}σ_bB_b over the L^{d−1}
straight paths of L links*". `LINEAR_PACKAGE.md l.71`: "*(Q_strA)(X, μ) := L^{−4}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ)*".
Probe R14 builds both rows entrywise at L = 3, d = 4, μ = 0, X = 0:

- LINEAR_PACKAGE: **135** distinct fine links, weights `m_t/L^d` with multiplicities `m_t = 1, 2, 3, 2, 1` over the
  **2L − 1 = 5** longitudinal offsets (the start point y ranges over the whole block, so the L-link leg from y spills
  one block-length past the coarse link); row sum `27·9/81 = 3 = L`.
- NORMS: **81** distinct fine links, uniform weight `L^{−(d−1)}`, longitudinal extent **L = 3**; row sum `81/27 = 3 = L`.
- NORMS's support is a **strict subset**: 54 entries missing, 0 extra. **They are different operators.**

**Benign for NORMS's conclusions, and I checked why** (probe R15): every property NORMS actually *uses* of `Q_str` holds
for both — `‖Q_str‖_{∞→∞} = L` (non-negative entries, constant row sums), `‖Q_str^T‖_{∞→∞} = L^{−(d−1)}` (LP: L pairs
(y, j) per fine link at weight L^{−d}; NORMS: one path at weight L^{−(d−1)} — same number), and hence
`‖Q_str^{(j)}‖_{∞→∞} = L^j` exactly, which is all that (I4), the (N-Q) bullet and NQ-1's Step 2 consume. **But the file
is internally inconsistent:** its own import (I8) (l.130-133, "`d(Q_str^m s)(p) = L^{−d·m}Σ_y ∮_{∂sq_y}s` over the
`L^{d·m}` squares of side `L^m`", matching `SQ.md l.710-712`) is the **full block average**, i.e. the LINEAR_PACKAGE
operator — the square identity needs all `L^{dm}` starting points and does not hold for the `L^{d−1}`-path object. So
l.103-104 and l.130-133 describe two different operators, and **Lemma N1-4's proof uses (I8)** (l.276-277). Nothing
numerical changes, because Lemma N1-4 only uses (I8) as imported; but the stated definition must be corrected, since any
later worker who recomputes from l.103-104 will build the wrong 81-entry row. The lead's framing is right: this changes
nothing *only if* nothing downstream recomputes from the stated definition.

### RN1-23 NORMS conflates M with ev — and this is the *second* half of why its (N-Q) bullet failed: **CONFIRMED, and it sharpens RN1-18**

`NORMS.md l.414-415` asserts "`Q_str d_iμ = d_{i+1}(μ|centres)`, which does not grow the gauge function". The two true
identities are **`Q_str∘d = d∘M`** (M the block mean — `PROOF.md l.2581`: "*Q_root = Q_str − dh at each level and
**Q_str d = dM***"; `SQ.md l.355`: "*Q_str∘d = d∘avg*") and **`Q_root∘d = d∘ev`** (ev the restriction to roots,
`PROOF.md l.2126`). NORMS attaches **ev's right-hand side to Q_str**. So:

- the bullet applies the **right identity to the wrong operator**. That is precisely why it was then left owing "*h
  applied to a pure gauge*": having pushed the exact form past `Q_str` rather than past the full `Q`, every subsequent
  `−d∘h` factor regenerates an `h`, and the recursion closes only through `h` on a pure gauge. NQ-1 pushes past the full
  `Q_root`, where `Q d = d·ev` is exact and `‖ev‖ = 1`, and the correction terms terminate.
- My RN1-18 located the *arithmetic* loss (the spurious `L^{j−1−i}` on factors simultaneously declared non-growing).
  **Both are present, and they are the two halves of the same mistake.** `|Mμ|_∞ ≤ |μ|_∞` as well as `|ev μ|_∞ ≤
  |μ|_∞`, so the conflation alone does not produce j-linear growth — it produces the *hole*; the `L^{j−1−i}` factor
  produces the *j-linear bound*. With the lead's entrywise result (ev-form and M-form are the **same operator**,
  `h∘d = M − ev`), the conclusion is unambiguous: **NORMS's `𝔮_0 ≤ 1 + 2d‖h‖j/L` is a bookkeeping loss on the same
  quantity, not a different quantity, and its named hole does not arise.** Record it as a **superseded sub-estimate**
  (not merely "amended"), together with [N1-corr 1]'s cases 2 and 3.

I also accept the lead's point 3 and record it so no later reviewer re-walks it: the slice identity
`Q = Q_str − d∘h` is an **unrestricted operator identity** (co-closedness enters only through J-str's *transpose*,
`LINEAR_PACKAGE.md l.166-171`), and `‖D_j∘G‖ ≤ 2‖G‖` is exact because `h` lands in **0-forms**, where `d` has two
terms in every d — the many-term worry would bite only for `d` of a 1-form, which the slice identity never produces.
`‖h‖ = d(L²−1)/(4L) = 8/3` is an **equality** (my probe R8 brute-forced the block mean and got exactly that), and
`𝔮_0 = 11/3` is the exact sup of the proven ratio. **None of these is a live attack vector, in NQ_CHECK or in NORMS.**

### RN1-24 The lead's sharpened L-question, answered explicitly: **A_soft < 1 at EVERY admissible odd L ≥ 3, not only at L = 3**

The NQ review's F7 (`𝔮_0 = p_L/L` only at L = 3) is a statement about a **coincidence of two numbers**, not about a
dependence. `p_L = 11` is the S4′ contour-length bound at L = 3, d = 4; NQ-1's constant is `𝔮_0 = 1 + d(L+1)/(2L)`, and
probe R16 evaluates it: **11/3 = 3.667 (L = 3), 17/5 = 3.400 (L = 5), 23/7 = 3.286 (L = 7), 35/11 = 3.182 (L = 11),
→ 1 + d/2 = 3 as L → ∞.** It is bounded in j for every L and **decreases in L**; that `11/3` also equals `p_L/L` at
L = 3 is arithmetic coincidence and is load-bearing for nothing. Therefore:

> **`A_soft = L^{−1} < 1` holds at every admissible odd `L ≥ 3`** (indeed every `L ≥ 2`). It is **not** an L = 3
> phenomenon. The reason is that `A_soft`'s exponent is `d − θ_w^r − 2θ_A = −1` with `θ_w^r = d−1` from J-str (c)
> (exact for every L) and `θ_A = 1` from Lemma N1-11, whose only L-sensitive input is `𝔮_0`, now proven bounded
> uniformly in both j and L. What *does* degrade with L is the **constant**: the prefactor `L^{d−1}/(L−1)` grows like
> `L^{d−2}` — 13.5, 31.2, 57.2, 133.1 at L = 3, 5, 7, 11 — so larger L buys a better ratio and a worse constant.
> The fragility is in the **exponent pair** `(θ_w^r, θ_A) = (d−1, 1)`, where there is zero slack (RN1-19), and in
> **d**, where the imported inputs are d = 4 only (RN1-12). It is not in L.

### RN1-25 Where I agree and disagree with the NQ review on the wall ordering

**Agree:** "(N-Q) was the small one"; (N-loc) in the form NORMS states it (exponential locality of the *gauge-variant*
representative, uniformly in the torus) **cannot be settled by an identity** — it is the multi-scale axial construction
already OPEN under `(CL-1)` (`PROOF.md l.6558`); NORMS's own near/far trade is "*stated, not carried out*"
(`NORMS.md l.430-432`), and I did not find it carried out anywhere; and **(N-bg) is the structural wall, which NQ-1
provably does not cross** (`PROOF.md l.1159-1161`).

**Disagree, narrowly and constructively (RN1-20):** Theorem N1-15 does not need (N-loc) *in that form*. Locality enters
only to replace a torus volume factor `T_k^d` by `c_m = coth(m′/2)^d`, and at the **proven** rate `c_m ≈ 7.4·10⁶ = 52⁴`,
so `T_k^d` is the *cheaper* constant for every `T_k ≤ 52`. On tori of bounded level-k side the four steps go through
from (I3), (I4) and the volume alone. The one step that must be replaced is Lemma N1-5 (an axial gauge needs a
non-wrapping box); my sketch uses the torus Hodge decomposition instead, and the step I have **not** proven is
`|B^{coex}|_∞ ≤ c_d·R·|dB|_∞` on a d = 4 torus of side R, uniformly in R. **So the two readings are compatible:
(N-loc) is required for the `T_k`-uniform / ℤ⁴ statement and is a genuine multi-scale-gauge problem; it is plausibly
not required for the bounded-`T_k` statement that NAH-unif's hypothesis actually quantifies over
(`PROOF.md l.6235`: "T_j ≥ the level-j sizes" is a *lower* bound on T_k).** That is a one-session check, not a paper,
and it should be done before the multi-scale axial gauge is opened.

**And on the claim to discharge (H-C)'s C_♭ clause, judged against that:** unchanged from RN1-16 and verdict (e). Even
with (N-loc) granted or bypassed, Theorem N1-15 bounds the third Taylor coefficient at `V_k = 1`, while (H-C) names the
N_0-Lipschitz constant of `Hess E_i^br` **on the class** (`PROOF.md l.6206-6210`, l.6220-6221). **Nothing in this
session discharges a clause any consumer consumes.** The correct ledger line is: *the dependency set of the C_♭ clause
has moved off (CovLift)/(Mult-Y) and onto (N-bg), with (N-loc) a sharpness question in between.*

---

## Part K. Binding fixes

In descending order of consequence. Items 1–4 are binding before anything in NORMS.md is propagated further.

1. **Withdraw the no-go.** `NORMS.md l.85-89`, l.458-481, l.490-496, l.869-872, and — most urgently —
   **HANDOFF.md l.44-47**, which already carries it into a "do not relitigate" list: "*the d = 4 cubic vertex is
   marginal, so A ≥ 1 in every scale-covariant norm, and the weight-invariance half is proven*". Neither half is
   proven (RN1-1, RN1-2, RN1-3, RN1-5). The defensible replacement, in full:
   *"Within the field-strength estimate of Theorem N1-12, no choice of the two level weights of Definition N^F-1
   delivers A_per < 1; the estimate's value is `𝔠_vol𝔠_ax²L^{d−4}(L²K̄)` with `L^{d−4} = 1` at d = 4 (marginality) and
   `L²K̄ ≥ 1` measured, not certified. No lower-bound input is exhibited, so A_per ≥ 1 is an INFERENCE, not a no-go
   [the PROOF.md l.6550 standard]. The measured signed one-level ratio is R_3 = 1.13–1.40 (T = 4, 5) and
   R_3(ℤ⁴) ∈ [1.40, ≲ 60], so A_per < 1 is unsupported by measurement either. The pre-registered outcome (O3) —
   marginal with zero drive, irrelevant complement, which is what c38 C's `c_2, c_3 → 1` plus an `O(K²)` remainder
   looks like — is NOT tested and is not excluded."*
   Label Theorem N1-13 (i) **PROVEN but VACUOUS** (the anchoring identity) and (ii) **INFERENCE**, not ARGUED.
2. **Mark check n1-D as a VACUOUS PROBE and strike every claim that rests on it** (l.88, l.470-471, l.791-793,
   l.843-844, l.871). The script's own comment `# placeholder, replaced below` is the record. Nothing needs re-running:
   the honest statement is that no computation was performed.
3. **Delete the gain numbers "920–1171" and "≈ 10³ per level"** from l.84, l.456, l.846 and from FOR-OTHER-FILES item 2
   (l.872). Replace with: *"A_per ≤ 𝔠_vol𝔠_ax²·L^{d−4}(L²K̄) with `𝔠_ax ≳ 5.46` (Proposition N1-10's own bracket) and
   `𝔠_vol = c_m = coth(m′/2)^d` unevaluated (3.7 at 𝒦's far measured rate, ≈ 80 at its near-field rate, ≈ 7·10⁶ at the
   proven rate m_*′): the honest bound is `A_per ≤ 32–49` at `𝔠_vol = 1` and gives no gain at all at 𝒦's near-field
   rate. The only quantitative gain statement the project can make is PROOF.md l.6490's, from c38's signed ratio."*
4. **Reword FOR-OTHER-FILES item 2 as an addition, not a correction** (RN1-7c). PROOF.md l.6249's `Z_col ≥ L^{d−1}×
   spread` is true. And re-label l.82's "norm artefact" as "absolute-value-counting artefact" (RN1-7b), which is what
   PROOF.md l.6249-6251 already says.
5. **Apply NQ_CHECK's status moves** (RN1-17): item 15 → PROVEN; item 12 → PROVEN-HERE at 𝔮_0 = 11/3; items 13, 14 →
   CONDITIONAL on (N-loc) alone; [N1-corr 1] cases 2, 3 moot. Do not propagate NQ_CHECK's non-verbatim quote (RN1-18)
   or its drifted PROOF.md line numbers, and replace its l.2787/l.2980 citation with **l.2581** (RN1-21). Theorem NQ-1
   itself needs no repair.
6. **Repair 𝔠_P** (l.387, l.399): add `1 + 2d·c_AX·R_eff` for the pure-gauge part and stop absorbing `2d` into a factor
   2. Exponents unchanged.
7. **Rewrite Lemma N1-6's admissibility parenthesis** (l.304-305) with the zero-energy-minimiser / difference-is-
   fluctuation-gauge argument of RN1-11, and state that `ζ^c_sm` is one *linear* map.
8. **Extend the n1-C disclosure** to the ratio label `L^{d−5}` (RN1-14), and state A_soft = L^{−1} in every d.
9. **Scope Theorem N1-15 to d = 4** (RN1-12): every imported input is d = 4 (`LINEAR_PACKAGE.md l.56`, l.166-171).
   Strike "the result is true for every d ≥ 2" (l.575) or label it as exponent bookkeeping.
10. **Stop saying "(H-C)'s C_♭ clause discharged"** (l.96, l.584, l.805) — (H-C) is a class statement; use Remark N6-5's
    own wording. And narrow §N8's BFT-1 row to the sup form (the Hölder half is not supplied).
11. **Fix the provenance numbers:** the n1 criteria time is 12:38:20, not 12:41 (l.831); the C_♭ citation at l.107 is
    PROOF.md l.6210, not l.6170-6176.
12. **Add RN1-20 to the open-items list** as a cheap alternative to (N-loc), before anyone starts the multi-scale axial
    gauge.
13. **Correct the Q_str definition** (l.103-104): it must be LINEAR_PACKAGE l.71's full block average,
    `L^{−d}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ)` — **135 entries at L = 3, d = 4, with multiplicities 1, 2, 3, 2, 1 over
    2L−1 = 5 longitudinal offsets** — not `L^{−(d−1)}` over `L^{d−1}` paths of L links (**81 entries, a strict subset,
    54 missing**). Benign for every conclusion (RN1-22), but it contradicts the file's own import (I8) at l.130-133,
    which Lemma N1-4's proof uses, and it is the definition a later worker would recompute from.
14. **Correct `Q_str d_iμ = d_{i+1}(μ|centres)`** (l.414-415) to `Q_str∘d = d∘M` (`PROOF.md l.2581`, `SQ.md l.355`), and
    state `Q_root∘d = d∘ev` (`PROOF.md l.2126`) as the identity that actually closes the bookkeeping. Then mark the
    l.415-417 estimate and its named hole **SUPERSEDED** (not amended) — the lead's entrywise result shows the ev-form
    and M-form composites are the *same operator* and `h∘d = M − ev` exactly, so the j-linear growth was a bookkeeping
    loss on the same quantity (RN1-23).
15. **State the L-uniformity explicitly** (RN1-24): `A_soft = 1/L < 1` at every admissible odd L ≥ 3, with
    `𝔮_0 = 1 + d(L+1)/(2L)` *decreasing* in L; the coincidence `𝔮_0 = p_L/L` at L = 3 is load-bearing for nothing, and
    the L-dependence that does bite is the prefactor `L^{d−1}/(L−1)`.

---

## Part L. My own independent tally of what NORMS.md adds

**Genuinely new and PROVEN (I checked each; d = 4, abelian/linearised, trivial background):**
1. **Lemma N1-1** — the composite cubic vertex carries exactly one coboundary or one residual per term, with M_W ≤ 6.
   I re-derived the Wilson half (`Re tr X³ = 0` for anti-Hermitian X; the cubic part of S_W is `Σ_p⟨(dA)_p, Q_2(A)_p⟩`;
   four links, C(4,2) = 6, BCH ½, commutator 2). This is the real content of the file: it is what makes the
   divergence-form leg available, and it is an identity, not an estimate.
2. **Lemma N1-2** — E3 and TOWER-VAR (d) are invariant under admissible fluctuation-gauge reparametrisation. Correct,
   with `𝔉_{AA}`(gauge) = 0 the only ingredient.
3. **Lemma N1-4** — `sup|d_jB_j| ≤ (C_f + 4κ̂C_RL²/(L²−1))L^{−2(k−j)}θ` on the torus, with an independent agreement
   with SQ's REG-lin (d) constant by a different route on a different geometry. Two independent derivations of one
   constant is worth the ledger line the file asks for (item 5).
4. **Lemma N1-6** — nested multilinear interpolants realise a coarse pure gauge at level j at size `L^{−(k−j)}`; this,
   not a norm, is what replaces `Z_row ≥ 1`. (Statement fix per RN1-11.)
5. **Lemma N1-5, Lemma N1-7, Proposition N1-8, Corollary N1-9** — all correct. N1-8's mass-balance identity
   `ρ_col = [n_τ(i)/n_plaq(i+1)]ρ_row` is clean and is the right way to see where `L^{d−2}` comes from. N1-9 is correct
   with `𝔐_0` the sharp entry sup (needed for `min(R, 𝔐_0e^{−md}) ≤ Re^{−md}`); the file should say so.
6. **Theorem N1-15** — the deliverable. CONFIRMED at the scope of RN1-12, with the single-pullback step rebuilt.
7. **§N7's exponent identity** `A = L^{d−θ_w^r−2θ_A}`, `θ_A = min(1, θ_w^c−1)`, and the consequence that no single
   common `θ_w ∈ (0, 2]` works. CONFIRMED; this is a real and actionable requirement on the BFT-1 statement.
8. **Remark N6-4** — COMP-F1/Π_ex does not occur, because every response used is the response to level-k data (exact,
   not merely closed). Consistent with `LINEAR_PACKAGE.md l.193-195` (Π_ex appears only in the *naive extension*) and
   Corollary 4.3. CONFIRMED.
9. **§N9** — the honest negative: nothing here moves ε_1 or g_K²; what it restores is the legitimacy of their
   k-independence. CONFIRMED subject to RN1-9's C_♭ ≈ 10⁷.

**Not established:** Theorem N1-13 (both halves, RN1-1/2/3/5); the "≈ 10³ gain" (RN1-7/8); "alternative to BFT-4" as a
headline (RN1-16); "every d ≥ 2" (RN1-12); the Hölder half of BFT-1 (RN1-16); "(H-C)'s C_♭ clause discharged" (RN1-16).

**Unchanged OPEN:** (N-bg); the level-uniform form of (H-G); the other (H-C) clauses; CURV-F2′/CURV-F2″ (Remark N8-2 is
a plausible and well-identified ARGUED route — I did not try to break it, and its two named requirements (a) and (b) are
correctly identified as the work).

**Net:** the file's contribution is **Lemma N1-1 + Theorem N1-15 + §N7's exponent pair**, which is substantial and, with
NQ-1, is the strongest result in the session. Its no-go and its headline numbers are not.

---

## Part M. The four explicit verdicts the brief asks for

**(c) Does `A_soft = 1/3` uniformly in k stand, and at what scope? — IT STANDS.** Scope, stated as narrowly as I can
make it and still true:

> For `d = 4`, `L ≥ 3` odd, `κ_j ∈ [κ_−, κ_+]`: the **third Taylor coefficient of `E_k^br` at the trivial background**
> `V_k = 1` satisfies `N3(D³E_k^br(1)) ≤ 𝔚 + (L^{d−1}/(L−1))𝔖` with `𝔚, 𝔖` independent of k, the level-j soft
> contribution decaying by the ratio `A_soft = 1/L = 1/3` per level — on every torus large enough at level k,
> abelian/linearised in the chain response (exact at the trivial background), in one admissible nested gauge
> representative of the composite chain-minimiser map. The `A_soft = 1/L` ratio itself holds for every d ≥ 2 and every
> L ≥ 2; the *theorem* does not, because (I3)/(I4)/(I5) are d = 4. Conditional on **(N-loc)** as written — and, by
> RN1-20 (ARGUED, mine), probably on nothing at all for tori of bounded level-k side. `𝔚 + 13.5𝔖` is **not O(1)**: at
> the proven locality rate it is ≳ 10⁷.

The margin is exactly one power of L in the exponent, zero slack in `(θ_w^r, θ_A) = (d−1, 1)`, and **robust in L: the
lead's sharpened question is answered in RN1-24 — `A_soft = 1/L < 1` at EVERY admissible odd L ≥ 3, not only at L = 3,
because NQ-1's `𝔮_0 = 1 + d(L+1)/(2L)` is bounded in j for every L and decreases in L (11/3, 17/5, 23/7, 35/11 → 3),
and the `𝔮_0 = p_L/L` coincidence at L = 3 carries nothing.** What worsens with L is the constant prefactor
`L^{d−1}/(L−1) ~ L^{d−2}`.

**(d) The per-level no-go — NOT ESTABLISHED; report it as an inference about one estimate.** Part (i) is true and
vacuous (RN1-2); its computational half is a tautology (RN1-3); part (ii) bounds the estimate from above and never
exhibits a lower-bound input (RN1-5); the class of norms is undefined (RN1-1); and the file's own pre-registered (O3)
is untested although the evidence it cites for marginality is (O3)'s signature (RN1-5). **I tried to break it and
partly succeeded: I cannot produce a norm in which A_per < 1, and the measured signed ratio R_3 ≥ 1.13 everywhere it is
measured, so I believe the conclusion is probably true — but "probably true" is not a no-go, and this project's rule is
that no-gos get the same scrutiny as positive theorems.** What I could NOT break: the *reason* a reweighting cannot
help within the given estimate. That part is sound, for the trivial reason of RN1-2.

**(e) The biggest live wall: (N-bg) — not (N-loc).** Three reasons, in order:
1. **Theorem N1-15 bounds an object no consumer consumes.** BR1 (`PROOF.md l.6122`), CURV1 step (6) (l.6180) and
   δ_Sch all consume a Lipschitz constant for `Hess E^br` **on the class**; (H-C) names that constant. The gap is
   (N-bg), and the file's own §N8 table marks every consumer row "needs (N-bg)".
2. **The cheap input that closed (N-Q) does not transfer.** Theorem NQ-1 rests on the slice identity
   `Q_root = Q_str − d∘h`, and `PROOF.md l.1159-1161` [R3-fix] records that **"the identity is linearised and abelian
   only: the nonabelian straight average is not even covariant, so there is no nonlinear SU(N) analogue"**. So (N-bg)
   cannot be had by repeating this session's trick.
3. **(N-loc) is probably not a wall at all** (RN1-20), and even if it is, its cost (`R_eff^d` at `R_eff ≈ 1/m_*′ ≈ 26`)
   is already inside the ≳ 10⁷ constant that the proven locality rate forces anyway.

Within (N-bg), route (i) is BFT-5 / `(G♯_0-field)` / `(a5-G♯)` and route (ii) is BFT-4's own Cauchy estimate — so the
honest reading of the whole file is: **the C_♭ clause's dependency set has moved from (CovLift)/(Mult-Y) to (N-bg), and
(N-bg) routes back into BFT-5 or BFT-4.** That is a genuine reduction for k ≥ 2 at third order, and it is not a closure.

---

## Reviewer probe record

All in scratchpad `rev_norms/`: `r1.py`, `r2.py` and their stdout. Plain python 3 with `-I`, `nice -n 10`, one process,
exact `fractions.Fraction` / integer arithmetic except where a decimal `coth` is printed; no numpy, no BLAS, no numeric
lock taken (brief rule 6), each run < 1 s, peak well under 50 MB. Load average 1.43 at launch. No repository file other
than this review was written; no `__pycache__` was created (`-I` plus `PYTHONDONTWRITEBYTECODE` not needed since the
scripts are run as `__main__` only).

| probe | what it re-derives, independently of the file's script | result |
|---|---|---|
| R1 | the soft exponent from the definitions at d = 2…6, n = 1, 2, 3, 5 | `(d−1) − n` in all 20 cases; the script's `(d−5)n+3` agrees **only** at d = 4 (and at n = 1) |
| R2 | `A_soft` from the definitions, general d | `L^{−1}` for every d; the script's label `L^{d−5}` differs at every d ≠ 4 |
| R3 | n1-D's code with arbitrary `eA` | returns `d−4` for `eA ∈ {0, 1, 2, −17, 1/3, 10⁶}` at three (d, k) — **tautology** |
| R4 | the honest weight-invariance, mismatch *derived* from Definition N^F-1, 15 pairs incl. θ_w = 5/2 | invariant = canonical in all 15; the invariance is the l = k anchoring identity |
| R5 | `c_m = coth(m′/2)⁴` at six rates from the files | 3.71 / 19.5 / 79.6 / 7.4·10⁶ / 1.05·10⁹ / 1.6·10⁴¹ |
| R6 | the "gain" with `𝔠_vol = c_m` carried | 0.49 … 315 depending on rate; never ≈ 10³ |
| R7 | NQ-1's bound, exactly, at (d, L) = (4,3), (4,5), (3,3) | 25/3, 91/3, 289/3 at d = 4, L = 3; dominates the computed 205/27, 2021/81, 6115/81 by 10 / 22 / 28 % |
| R8 | `avg_{y∈B(X)}|y−c_X|_1` by brute force over the block | exactly `d(L²−1)/(4L)` at (4,3), (3,3), (4,5) — NQ-1's `‖h‖` step confirmed |
| R9 | Lemma N1-11 step (5)'s `|d_kλ|_∞ ≤ 2|Y|_∞` | false; the bound is `(1 + 2d·c_AX·R_eff)|Y|_∞` = 25, 121, 625 at R_eff = 1, 5, 26 |
| R10 | `𝔠_ax` forced by Proposition N1-10's own bracket | ≥ 5.4644 / 5.9512 / 5.0740; `𝔠_ax² ≥ 25.8`; `Z^sm ≤ 1.69–1.98` |
| R11 | `A_per` with both constants carried | 32.3–48.8 at `𝔠_vol = 1`; 2.6·10³–3.9·10³ at 𝒦's near measured rate |
| R12 | reproduction of the file's headline gain | exactly `1266.87/(L²K̄)^a` = 920.3, 1171.1 — i.e. `𝔠_vol = 𝔠_ax = 1` |
| R13 | the measured comparator | `1266.87/R_3` = 1124, 908, 905, 21 at R_3 = 1.1268, 1.3956, 1.40, 60 |
| R14 | NORMS l.103-104's Q_str vs LINEAR_PACKAGE l.71's, **entrywise** at L = 3, d = 4 | **135 vs 81** entries; NORMS's support is a strict subset (54 missing, 0 extra); LP multiplicities 1, 2, 3, 2, 1 over 2L−1 = 5 offsets; both row sums = L = 3 |
| R15 | every norm of Q_str that NORMS uses, for both operators | `‖Q_str‖_∞ = L`, `‖Q_str^T‖_∞ = L^{−(d−1)}`, `‖Q_str^{(j)}‖_∞ = L^j`: **all AGREE** — hence benign; but (I8)'s square identity needs the LP operator |
| R16 | `𝔮_0 = 1 + d(L+1)/(2L)` at L = 3, 5, 7, 9, 11, 101 | 11/3, 17/5, 23/7, 29/9, 35/11, 305/101 → 3: **decreasing in L**; prefactor `L^{d−1}/(L−1)` = 13.5, 31.2, 57.2, 91.1, 133.1, 10303 |

Hand rebuilds, not scripted: the TOWER-VAR (d) third-derivative chain rule (RN1-10); NQ-1's telescoping induction
(RN1-17); Lemma N1-1 (a)'s Wilson cubic; Lemma N1-5's axial induction; the `𝔑 = N3/(2(d−1))` weight cancellation
(RN1-7b); `N3 = C_♭` for symmetric T; the zero-energy pure-gauge minimiser (RN1-11); the flat-class response
`h_j = L^{−(k−j)}h_k` (RN1-20).
