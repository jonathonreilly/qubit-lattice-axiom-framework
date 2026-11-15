# REVIEW_NQ_S1: hostile review of NQ_CHECK.md (session 24) — the (N-Q) decision, Theorem NQ-1, check nq1

Reviewer: an independent agent. I wrote none of NQ_CHECK.md, NORMS.md, PROOF.md, LINEAR_PACKAGE.md, SQ.md or any check in
`checks/`. This file is the only repository file I edited. I ran no git command, made no commit, no push and no PR. I did
not read or write STAR_CONST.md, and I wrote nothing into NORMS.md.

**Inputs** (`TZ=UTC stat`, read 2026-10-28 ~13:45-14:40 UTC):

| file | born | modified | bytes |
|---|---|---|---|
| NQ_CHECK.md | 13:06:50 | 13:16:24 | 28959 |
| NORMS.md | 12:57:22 | 12:57:22 | 81173 |
| checks/nq1_criteria.md | 13:07:22 | 13:07:22 | 4941 |
| checks/nq1_qnorm.py | 13:09:25 | 13:09:38 | 10920 |
| checks/nq1_stage2_out.txt | 13:09:43 | 13:09:44 | 3790 |
| checks/nq1_out.txt / nq1_time.txt | 13:10:15 | 13:10:41 | 4599 / 777 |
| checks/nq1_telescope_posthoc.py | 13:16:04 | 13:16:11 | 3131 |
| checks/nq1_telescope_posthoc_out.txt | 13:16:11 | 13:16:11 | 2207 |
| PROOF_session23_snapshot.md | 12:03:19 | 12:03:19 | 695579 |
| SQ.md / LINEAR_PACKAGE.md | 12:03:19 | 12:03:19 | 190900 / 48089 |
| RTARGET.md | 12:03:19 | 13:29:21 | 94495 |

**What I read.** NQ_CHECK.md in full (366 lines). checks/nq1_criteria.md in full; nq1_qnorm.py and
nq1_telescope_posthoc.py line by line; nq1_out.txt, nq1_stage2_out.txt, nq1_time.txt,
nq1_telescope_posthoc_out.txt in full. NORMS.md §N1 (l.75-141), §N3 Lemmas N1-4 … N1-7 (l.267-325), §N4 in full
(l.329-432), §N6 in full (l.500-638), §N7 (l.642-676), §N8 (l.680-717 scanned), §N10 tally (l.774-827).
LINEAR_PACKAGE.md §0-§3 (l.1-200). PROOF_session23_snapshot.md l.594-602 (S4′), l.1120-1140 (L3g(a)-slice),
l.2055-2098 (Setting SC, J-str), l.2540-2550 (IT-str consequences), and l.3487/3523/3526/5226/5262 (p_L := 5L − 4).
Live PROOF.md l.950-1000, l.1115-1145, l.2050-2110, l.2370-2400, l.2535-2581. SQ.md l.12-18, l.345-365 (§0.4),
l.405-415, l.648-660 (§11.0), l.700-716 (Lemma SHIFT). RTARGET.md l.408-420, l.436. HANDOFF.md (l.30-65) and the
(N-Q) lines of LOG.md / SESSION24_RESULTS.md, to see what has already been propagated.

**Independent re-implementation and probes.** I did **not** re-run nq1_qnorm.py. Instead I rebuilt the whole
computation from the primary definitions, in a deliberately different implementation, so that a shared coding error
cannot cancel: tuple keys instead of bit packing, `fractions.Fraction` throughout instead of integers over a common
denominator, paths built by an explicit coordinate walk, composition by my own recursion, and — for j = 3 — a
streaming sweep in the coordinate-0 direction so that the 4.1M-entry row is never resident. All in plain python
(`python3 -I`, no numpy, no BLAS, single thread, `nice -n 10`). Per brief rule 6 exact rational/integer arithmetic in
plain python does not take the numeric lock; **I did not take the lock.** Load1 was 1.94 at the start and no run
exceeded 60 s.

Scripts and outputs in scratchpad `revnq1/`: `rev_qnorm.py`, `rev_j3.py`, `rev_tele.py`.

| probe | what it does | result | wall | peak RSS |
|---|---|---|---|---|
| R1 `rev_qnorm.py 2` | Q_root, Q_str, h rebuilt from LINEAR_PACKAGE l.67-71; row ℓ¹ at j = 1, 2; my own G1/G2/G3/G5 with a *different* non-linear λ (x₀³ term) | 205/27 and 2021/81, all four directions; 0 mismatches | 1.4 s | 52 MB |
| R2 `rev_j3.py` | j = 3 by a streaming sweep, integers over NC³ | 6115/81 in all four directions | 59.5 s | 482 MB |
| R3 `rev_tele.py` | Step 1 by my own "collapsed-ev" derivation; ev-form vs M-form for h^{(2)}; h∘d = M − ev; the four Step-2 norms | 0 differing entries everywhere; ‖h‖ = 8/3 exactly | 20.8 s | 914 MB |

---

## Bottom line

- **(N-Q) is PROVEN, at the scope NQ_CHECK claims.** I rebuilt Theorem NQ-1 from the two cited identities and could
  not break it. Every step of the telescoping, every one of the four norm inputs, and the assembly arithmetic are
  correct. The brief's two suspicions about the proof (that the identity might hold only on co-closed forms, and that
  ‖d∘G‖ ≤ 2‖G‖ is wrong in d = 4) are both **unfounded**, and I say below exactly why.
- **The identification of Q is not the convenient reading — it is the only reading.** Setting SC's Q is Q_root in the
  definition verbatim (PROOF s23 l.2060), it is named Q_root where the norms are set (RTARGET l.414), and it is
  *forced* by the consumer: NORMS' Lemma N1-11 step (4) uses `B_j = Q^j B_0 − Σ Q^{j−1−i} r_i`, which is an exact
  relation only for Q_root (NORMS' own Lemma N1-4 says the Q_str version holds only "modulo a level-j pure gauge").
  SQ's `Q := Q_str` is an explicitly declared local convention (SQ.md l.655, §0.4), and §0.4's proof is correct.
- **The exact values reproduce, including j = 3.** 205/27, 2021/81, 6115/81 and the support sizes 459 / 47 385 /
  4 113 747, from an independent implementation. ‖h‖ = 8/3 is an **equality**, as the file says in a parenthesis.
- **The NORMS/NQ_CHECK fork goes to NQ_CHECK.** I verified entrywise that the ev-form and the M-form of the composite
  slice functional are the *same object* (0 differing entries at j = 2) and that h∘d = M − ev exactly. So NORMS'
  j-dependence is a bookkeeping loss, not a different quantity, and its named hole ("h applied to a pure gauge") does
  not arise in the ev form, where every h acts on Q_str^{(i)}B_0.
- **The clean gate sweep deserves the scrutiny the brief asked for, and one claim about it is WRONG.** G1 is an
  algebraic near-identity of the script's own construction and has low discriminating power; it does **not**
  "strengthen check c8(f)'s 2e-16 to an entrywise exact identity", because c8(f) tests something G1 assumes. G4 and G5
  cannot fail for this construction; G2 is half tautological. Only G3 has real power. **No gate tests Q_root against an
  independent construction** — my re-implementation supplies that, and it agrees.
- **New finding, not in NQ_CHECK:** NORMS §N1 l.103-104 **misdefines Q_str** (as an average over L^{d−1} straight
  paths of L links; the operator in the identity averages over the L^d block legs). Benign for NORMS' conclusions,
  because only ‖Q_str‖ = L, ‖Q_str^T‖ = L^{−(d−1)} and Q_str∘d = d∘avg are used and those hold for both, but it is a
  third NORMS text item that should have been in NQ_CHECK's FOR-OTHER-FILES list.
- **Two over-reaches.** (i) NQ_CHECK instructs the NORMS owner to move Lemma N1-11 from CONDITIONAL to PROVEN-HERE,
  but it did not review Lemma N1-11's remaining proof; the honest instruction is "its last named condition is
  discharged". (ii) 𝔠_P is still not a number: 𝔮_0 = 11/3 replaces one of four unevaluated constants (C_f, C_R, R_eff
  remain).
- **Citation hygiene.** Every one of the file's quotations is verbatim and in context, but the PROOF.md line numbers
  resolve in **PROOF_session23_snapshot.md**, not in PROOF.md, while the RTARGET.md number resolves in the live file.
  The convention is undisclosed and mixed.
- Procedural: criteria genuinely precede the script by 2 min 03 s on the filesystem; no constant in the criteria is
  session-derived (I re-anchored p_L = 11 to PROOF's own `p_L := 5L − 4`, and re-derived it as L + d(L−1) at d = 4);
  no `checks/__pycache__`; the FAIL-free sweep is honest, not retuned.

---

# Part A. Provenance and process hygiene

### NQ-1 (provenance of the file and the check): CONFIRMED, two cosmetic notes
NQ_CHECK.md was born 13:06:50 UTC and last modified 13:16:24. §Q0 states "first edit of this file, 2026-10-28
13:06:09 UTC" — 41 s before the file's birth. Cosmetic (a clock read before the write); byte accounting unaffected.
§Q2 states the criteria were written "13:08 UTC"; the filesystem says 13:07:22. Also cosmetic.
The staged run (`nq1_stage2_out.txt`, born 13:09:43) precedes the full run (13:10:15) and the script was not touched
between them (`nq1_qnorm.py` mod 13:09:38), so **the stored script is the one that produced both outputs** — the file's
claim that the staged run used "the identical script and criteria" is verified, not just asserted.
§Q6 (post-hoc) was written at 13:16:04-13:16:11 and the host file's last modification is 13:16:24, consistent with
§Q6 being appended after §Q1-§Q5. No `checks/__pycache__` exists despite the post-hoc script importing `nq1_qnorm`.

### NQ-2 (criteria before script; no session-derived constant): CONFIRMED
`nq1_criteria.md` born = modified = 13:07:22, written in one write; `nq1_qnorm.py` born 13:09:25. Gap 2 min 03 s, so
**criteria-before-script holds on the filesystem**, not only in the prose. Three sister lanes breached the
"no constant derived in the same session" rule in session 24, so I re-anchored every constant in the criteria
independently of session-24 files:
- L = 3, d = 4 — Setting SC, PROOF s23 l.2058. ✓
- d! = 24, L^d = 81 — S4′, PROOF s23 l.596-599 ("for each of the d! coordinate orders σ … L^{-d} Σ_{y∈B(X)}"). ✓
- **p_L = 11** — the criteria route the citation through NORMS.md §N4 / [N1-corr 1], which is a session-24 file. But
  p_L is **defined pre-session** in PROOF: `p_L := 5L - 4` at s23 l.3487 and l.5226, with "L = 3, p_L = 11" spelled out
  at s23 l.3526 (and in the live file at l.3523, l.5262). I also re-derived it from the geometry: the S4′ contour is a
  funnel of ≤ d(L−1)/2 links, a straight leg of L, and a second funnel of ≤ d(L−1)/2, i.e.
  **p_L = L + d(L−1) = 5L − 4 at d = 4** — identically PROOF's formula, for every L. So the threshold p_L/L = 11/3 is
  a genuinely pre-session number and the rule is **not** breached.

### NQ-3 (the j = 1 clause of the BOUNDED criterion was vacuous a priori): NARROWED
The BOUNDED verdict requires "R_j ≤ 11/3 for every j ∈ {1, 2, 3}". At j = 1 this is **forced** by the contour-length
bound that the criteria file itself quotes: 𝔫_1 ≤ p_L = 11, hence R_1 ≤ 11/3, with no computation. One third of the
criterion could not have failed. This does not void anything — the j = 2 and j = 3 clauses had real content (the a
priori bounds there are 13.4 and 49.3) — but it is the project's own "vacuous-probe trap" in miniature and should be
disclosed in the criteria record.

### NQ-4 (resource discipline and the lock exemption): CONFIRMED as permitted, with a nit
The run took 25.7 s and **856 MB peak RSS** (`nq1_time.txt`: 855 851 008 B max RSS) with no numeric lock, on an 8 GB
machine shared with seven other agents. Brief rule 6 does exempt "exact rational/symbolic arithmetic in plain python"
from the lock, on the ground that it "is cheap"; 856 MB stretches that ground. Not a breach as the rule is written, and
the run was `nice -n 10` at load 2.0. For the record, the memory was avoidable: my independent j = 3 sweep
(`rev_j3.py`) gets the same exact value in 482 MB. I disclose that my own `rev_tele.py` peaked at 914 MB.

### NQ-5 (line-number convention): CONFIRMED-WITH-FIX
All five "settle what Q is" citations and all of §Q3's input citations are **verbatim and in context**, but they resolve
in different files:
- "PROOF.md l.2060" (Setting SC) → PROOF_session23_snapshot.md l.2060. In the live PROOF.md that text is at l.2096.
- "PROOF.md l.2093-2094" (J-str) → s23 l.2093-2094. "PROOF.md l.2545" (IT-str consequence) → s23 l.2545 (live l.2581).
  "PROOF.md l.1123-1125" and "l.1127-1131" (L3g(a)-slice, [R3-fix]) → s23. "PROOF.md l.2090" (root covariance) → s23.
  "PROOF.md l.596-600" (S4′) → s23 l.595-600. "PROOF.md l.1134" (h(A+dλ)) → s23 (live l.1170).
- "RTARGET.md l.414" → the **live** RTARGET.md l.414 (verified: "Q = Q_root of S4′").
- SQ.md l.15, l.352-357, l.411, l.655, l.710-711 → the live SQ.md (unmodified today). All verbatim.
Using the session-23 snapshot is defensible while the lead is editing PROOF.md concurrently, but the convention is
undisclosed and is mixed with live-file numbers. **Fix: state the convention once at the head of §Q1.**

---

# Part B. TQ1 — the identification of Q. This is the crux, and I attacked it hardest

### NQ-6 (Setting SC's Q is Q_root): CONFIRMED — and not by a reading of an ambiguity
I read all five locations in context and judge independently. The identification does not rest on a preference between
two readings; it rests on a definition and is then confirmed by the consumer.

1. **PROOF s23 l.2058-2061** is the *definition* of Setting SC and is unambiguous: "*Q is the linearised S4' map from
   level i to level i + 1 (Q_root of L3g(a)-slice, with the S4' order average).*" There is no competing definition of
   Setting SC anywhere; the same sentence appears in every snapshot from session 10 onward and in the live file at
   l.2096.
2. **RTARGET.md l.414** (live) and l.436 both set the section's Setting as "Q = Q_root of S4′" / "Q = Q_root (S4')".
3. **NORMS.md's own convention list, l.102**: "Q: the S4' average (level-j 1-forms → level-(j+1) 1-forms)". So (N-Q)
   is about Q_root inside NORMS too.
4. **The consumer forces it, which is the strongest argument and NQ_CHECK does not make it.** NORMS Lemma N1-11 step
   (4) uses `B_j = Q^j B_0 − Σ_{i<j} Q^{j−1−i} r_i`. That is an *exact* identity only because r_i := QB_i − B_{i+1}
   with Q = Q_root. NORMS' Lemma N1-4 (l.275) writes the Q_str version and explicitly qualifies it:
   "*B_j = Q_str^{j}B_0 − Σ_{i<j}Q_str^{j−1−i}r_i **modulo a level-j pure gauge** … a pure gauge does not change
   d_jB_j, so this step is unconditional for the curvature*". A potential bound cannot use the Q_str version, because
   the discarded pure gauge is exactly the quantity being bounded. So (N-Q) must be about Q_root or it is not the input
   Lemma N1-11 needs. **This closes the question independently of which file one reads first.**

### NQ-7 (the J-str / SHIFT "conflict" is not one): CONFIRMED
- **J-str.** LINEAR_PACKAGE l.170 and PROOF s23 l.2093-2094 say "Q^T = Q_str^T − h^Td*. On co-closed r the funnel
  term h^Td*r vanishes". The co-closedness restriction attaches to the **transpose** statement only, because what has
  to vanish is d*r. This is a statement about Q = Q_root. ✓
- **SHIFT.** SQ.md l.655 (§11.0 Setting, the section containing Lemma SHIFT) declares "*Q := Q_str (§0.4; …)*". The
  parenthesis at l.710-711 is therefore a true statement about SQ's own Q. ✓ And SQ l.411 shows SQ knows the
  distinction: "*B_{j+1} = QB_j − r_j (Q = Q_root) … (dQ = dQ_str)*". ✓
- **The insensitivity claim.** PROOF s23 l.2545: "*Q_root = Q_str − dh at each level and Q_str d = dM, so a composite
  of root maps equals Q_str^{(L^m)} plus a coarse exact form*", whence d∘Q_root^{(m)} = d∘Q_str^{(L^m)} since d∘d = 0.
  SHIFT bounds d(Q^m s), so it cannot see the difference. ✓ CONFIRMED.

### NQ-8 (SQ §0.4's substitution — is it proved, and proved for NQ_CHECK's use?): CONFIRMED, and the file's own
### flagged nuance is right and is in fact stronger than it says
I re-derived §0.4 (SQ.md l.352-357) rather than citing it. With λ_0 := 0, λ_{i+1} := avg(λ_i) + h(B_i),
B'_i := B_i + dλ_i:
  Q_str B'_i = Q_str B_i + Q_str dλ_i = Q_str B_i + d(avg λ_i)   [Q_str∘d = d∘avg]
  B'_{i+1} = B_{i+1} + d(avg λ_i) + d h(B_i)
  ⟹ Q_str B'_i − B'_{i+1} = (Q_str − d∘h)B_i − B_{i+1} = Q_root B_i − B_{i+1}.
So the residuals are *literally equal*, dB'_i = dB_i, and B'_0 = B_0. **§0.4 is correct.** It is proved for exactly what
SQ measures (residuals, curvatures, energies) and for nothing else.

The brief asks whether the gauge-shift nature of §0.4 *undercuts* the identification. It does not — it **supports** it,
and more sharply than NQ_CHECK says. §0.4's accumulated gauge function satisfies λ_{i+1} = avg λ_i + h(B_i), which is
**precisely the M-form recursion for the composite slice functional** h^{(m+1)} = M h^{(m)} + h Q^{(m)} (PROOF s23
l.2787/2980). So §0.4's "the potentials move" is the statement "they move by h^{(i)}", and 𝔮_0 − 1 is a norm of exactly
that object. §Q1's closing paragraph ("𝔮_0 > 1 is a measure of it") is therefore not a hedge but the correct reading,
and the identification survives it intact: §0.4 is unavailable to a potential bound, which is why (N-Q) had to be
proved rather than substituted away.

### NQ-9 (the file did not pick the convenient reading): CONFIRMED
"Not success" in §Q0 pre-registers "silently replacing Setting SC's Q by Q_str because that is the convenient reading".
The convenient reading would have given 𝔮_0 = 1 and a one-line discharge, and NORMS §N4 l.418-419 openly hoped for it
("a one-line check if Setting SC's Q is the straight average (then 𝔮_0 = 1 …)"). The file took the harder reading and
proved the harder statement. I could not find a place where Q_str is substituted for Q_root outside gate G4.

---

# Part C. Theorem NQ-1, rebuilt from scratch

Per the lane's standing rule I rebuilt every load-bearing step rather than checking it against the file.

### NQ-10 (Step 1, the telescoping identity): CONFIRMED as an exact operator identity
Let Q_i = S_i − D_{i+1}H_i (slice identity, level i) and Q_i∘d_i = d_{i+1}∘ev_i (root covariance). Write
S^{(i)} := S_{i-1}⋯S_0, E^{(j-1,i+1)} := ev_{j-1}∘⋯∘ev_{i+1}.

*Claim.* Q^{(j)} = S^{(j)} − D_j Σ_{i=0}^{j-1} E^{(j-1,i+1)} H_i S^{(i)}.
*j = 1:* Q_0 = S_0 − D_1H_0 with both empty products the identity. ✓
*Step:* Q^{(j+1)} = Q_jQ^{(j)} = Q_jS^{(j)} − Q_jD_j Σ_i E^{(j-1,i+1)}H_iS^{(i)}.
  Q_jD_j = D_{j+1}E_j (root covariance, once).
  Q_jS^{(j)} = (S_j − D_{j+1}H_j)S^{(j)} = S^{(j+1)} − D_{j+1}H_jS^{(j)}.
  ⟹ Q^{(j+1)} = S^{(j+1)} − D_{j+1} Σ_{i=0}^{j} E^{(j,i+1)}H_iS^{(i)}, the i = j term having an empty ev-product. ∎

Checked against the brief's four questions:
- **Index range.** i = 0 … j − 1, inclusive. Correct as printed.
- **ev power.** Term i carries ev^{(j−1−i)}, i.e. j − i − 1 factors ev_{j-1}…ev_{i+1}; at i = j − 1 it is empty. Correct.
- **d_j prefactor.** The single d is at level j, the top level, outside the sum. Correct — and it must be outside,
  because that is what makes the whole correction one coarse exact form (PROOF s23 l.2545).
- **Operators or a subspace?** **Operators, on all level-0 1-forms.** The brief's worry that "the slice identity is
  stated for co-closed forms" is misplaced: PROOF s23 l.1127-1128 states the forward identity for *every* A
  ("the linearised average is Q_root A = Q_str A − d h"), and LINEAR_PACKAGE l.72 likewise. Co-closedness enters only
  in J-str's **transpose** equality Q^T = Q_str^T, where h^Td*r = 0 needs d*r = 0. Root covariance is an identity on
  all 0-forms. **So the telescoping is applied on the right space and there is no hidden subspace restriction.**

Two independent confirmations, both mine:
- (R3) I derived a *different* form of the same identity, exploiting that in the root-aligned convention every
  ev-ancestor of the level-j origin is the origin, so h^{(j)} collapses to Σ_{i<j}(h∘Q_str^{(i)}) based at the origin;
  then row(Q^{(j)},(0,μ)) = row(Q_str^{(j)}) − T_{L^je_μ}[h^{(j)}] + h^{(j)}. **0 differing entries at j = 1 and j = 2,
  all four directions**, lhs and rhs both 459 / 47 385 entries.
- The file's own §Q6 post-hoc check uses the same collapse but **imports nq1_qnorm.py's machinery unaltered**, so a
  bug in `pack`/`compose`/`pdelta` would cancel on both sides. My rebuild uses none of that code. See NQ-19.

### NQ-11 (‖S^{(i)}‖_{∞→∞} = L^i exactly): CONFIRMED
One Q_str row (LINEAR_PACKAGE l.71) is non-negative with row sum L^{-d}·L^d·L = L. A product of non-negative matrices
with constant row sums has row sum the product. Measured: 3, 9, 27 exactly, min entry 1/3^{4i} > 0 (R1, R3), and the
j = 3 support 1 043 199 = the support of the direct straight average of side 27, consistent with IT-str
(LINEAR_PACKAGE Lemma 2.4). ✓

### NQ-12 (‖ev^{m}‖_{∞→∞} = 1): CONFIRMED
ev_i λ(X) := λ(c_X) has exactly one entry 1 per row; a composite of restrictions is a restriction. Trivially 1. ✓
(For i = j − 1 the product is empty, norm 1 — the file's "empty products read as the identity" is needed and stated.)

### NQ-13 (‖h‖ ≤ d(L²−1)/(4L), with equality): CONFIRMED, equality verified
h(A)(X) = avg_σ avg_{y∈B(X)} ∫_{P^σ(c_X→y)}A, so the row ℓ¹ mass is at most avg_{σ,y}(path length) = avg_y|y − c_X|_1
= d·L^{-1}·2Σ_{t=1}^{(L-1)/2}t = **d(L²−1)/(4L)** = 8/3 at d = 4, L = 3. ✓ (L odd is used here, and is hypothesised.)
The file's parenthetical that equality holds is right, and I checked the reason: for a link (p,ν), a forward ν-step
only ever occupies p_ν ≥ 0 and a backward ν-step only p_ν ≤ −1, so no two (σ,y) contribute opposite signs to the same
link and |Σ| = Σ|·|. Measured: **row ℓ¹ of h = 8/3 exactly** (R1, R3), 216 nonzero entries.

### NQ-14 (‖D_j∘G‖ ≤ 2‖G‖): CONFIRMED — the brief's d = 4 suspicion does not apply
The brief suspects this because "a lattice exterior derivative on 2-forms generically has operator norm larger than 2
in ℓ^∞". True, but irrelevant here: **H_i maps into level-(i+1) 0-forms**, so D_j acts 0-forms → 1-forms, where
(D_jG)(X,μ;·) = G(X+e_μ;·) − G(X;·) has exactly two terms. ‖D_j‖_{∞→∞} = 2 **exactly**, in every d. The constant 2 is
right, it is not a d-dependent undercount, and 𝔮_0 does not change. (The 2(p+1)-term worry would bite if the
correction were a d of a 1-form; it is not — that is the whole point of the slice identity putting the funnel into a
*coarse exact 1-form*, i.e. d of a 0-form.)

### NQ-15 (Step 3 assembly and 𝔮_0): CONFIRMED, arithmetic re-done
‖Q^{(j)}‖ ≤ L^j + Σ_{i=0}^{j-1} 2·1·(d(L²−1)/(4L))·L^i = L^j + (d(L²−1)/(2L))·(L^j−1)/(L−1)
          = L^j + (d(L+1)/(2L))(L^j − 1) ≤ L^j[1 + d(L+1)/(2L)].
At d = 4, L = 3: d(L+1)/(2L) = 8/3, **𝔮_0 = 11/3**, and the sharp form gives 25/3, 91/3, 289/3 = 8.3333, 30.3333,
96.3333 at j = 1, 2, 3. ✓ All as printed. Submultiplicativity of the max-row-ℓ¹ norm and the triangle inequality are
the only analytic tools and both are valid. 𝔮_0 = 11/3 is the **exact supremum over j** of the proven bound's ratio
1 + (8/3)(1 − L^{-j}), approached and not attained, so it is the honest constant for this route.

### NQ-16 (the torus clause): CONFIRMED, and provable more directly than stated
The file argues via periodisation (torus entries are sums of Z^d entries over the period lattice, and
Σ_b|Σ_per Q(c,b+per)| ≤ Σ_{b'}|Q(c,b')|). That is correct. But the theorem does not need it: every Step-2 input holds
verbatim on a torus — Q_str still has non-negative entries with row sum L even when block legs wrap, ‖ev‖ = 1,
‖h‖ ≤ avg path length, ‖D_j‖ = 2 — so the bound is direct on each torus. Either route is sound; the direct one is
shorter and avoids having to argue that the composite of periodisations is the periodisation of the composite.

### NQ-17 (the statement quantifies over the wrong family for its consumer): CONFIRMED-WITH-FIX
§Q3 states the bound for "Q^j", i.e. Q^{(j)} = Q_{j-1}∘⋯∘Q_0 anchored at level 0. NORMS Lemma N1-11 step (4) also
needs ‖Q^{j−1−i}‖ ≤ 𝔮_0L^{j−1−i} for the **residual transport**, i.e. for composites of m = j−1−i consecutive levels
*starting at level i+1*. The proof delivers that unchanged (nothing in Steps 1-3 uses the starting level, and in own
units every Q_i is the same operator), and m = 0 gives the identity with norm 1 ≤ 𝔮_0. **Fix: one line — state the
theorem for "any composite of m consecutive levels", or note that Q_i is level-independent in own units.** No
mathematical gap; a quantifier gap between the theorem and its consumer.

---

# Part D. TQ2 — the computation, re-run independently

### NQ-18 (the exact values): CONFIRMED, including j = 3
From my own implementation of Q_root (LINEAR_PACKAGE l.67/70, PROOF s23 l.596-597, block B(X) = c_X + {−1,0,1}^4,
c_Y = c_X + Le_μ, same σ at both ends):

| j | my 𝔫_j | NQ_CHECK 𝔫_j | my support | NQ_CHECK support | R_j |
|---|---|---|---|---|---|
| 1 | **205/27** | 205/27 | 459 | 459 | 205/81 = 2.530864 |
| 2 | **2021/81** | 2021/81 | 47 385 | 47 385 | 2021/729 = 2.772291 |
| 3 | **6115/81** | 6115/81 | 4 113 747 | 4 113 747 | 6115/2187 = 2.796068 |

All four link directions agree at every j (my own direction-invariance check). Increments 176/729 = 0.241427 and
52/2187 = 0.023777, ratio 528/52 = 10.154 ("≈ 10.2" as printed). The verdict table's arithmetic is right:
BOUNDED fires, POLYNOMIAL and CRUDE do not, OTHER does not.
The two framing claims are also right: Q^j is level-j translation covariant so max_c reduces to a max over μ; and the
Z⁴ value dominates every torus (NQ-16). The "far from the crude p_L^j/L^j" phrasing is fair at j = 2, 3 (2.77 vs 13.4;
2.80 vs 49.3) and **not** at j = 1 (2.53 vs 3.67, where the crude bound is the one that makes R_1 ≤ 11/3 automatic —
see NQ-3).

### NQ-19 (does the bound dominate, and is there a crossing risk?): CONFIRMED, no risk, and the gap is located
Bound/computed: 25/3 ÷ 205/27 = 225/205 = **1.098**; 91/3 ÷ 2021/81 = 2457/2021 = **1.216**; 289/3 ÷ 6115/81 =
23409/18345 = **1.276**. So +10%, +22%, +28% as printed. Three data points cannot see j → ∞, as the file says; the
**proof** is what carries it, and Part C says the proof carries it. There is no trend that can cross 𝔮_0, because the
bound is unconditional for every j.
I located the slack exactly. The only lossy step is ‖H_iS^{(i)}‖ ≤ ‖h‖·L^i. I measured the true values:
‖h Q_str^{(i)}‖ = 8/3, 56/9, 488/27 for i = 0, 1, 2, i.e. **/L^i = 2.667, 2.074, 2.008** against the bound 8/3. Feeding
these in gives 25/3, 241/9, 2185/27 = 8.333, 26.778, 80.926, i.e. computed/bound = 0.911, 0.932, 0.933 — the slack is
**stable, not growing**, which is the right consistency signature. If one proved ‖hQ_str^{(i)}‖ ≤ (56/27)L^i for
i ≥ 1, the same assembly would give 𝔮_0 ≈ 1 + 2(56/27)/(L−1) ≈ **3.07** instead of 3.667. That is an optional
sharpening, not a defect: it would still not reach the computed ≈ 2.80, and 11/3 is already bounded, which is all
Theorem N1-15 consumes.

### NQ-20 (𝔮_0 = 11/3 = p_L/L at L = 3 is a coincidence): NOTE, worth stating in the file
L·𝔮_0 = L + d(L+1)/2 while p_L = L + d(L−1). At d = 4 these agree **only at L = 3** (both 11); at L = 5 they are 17
vs 21. So at the lane's working L the proven 𝔮_0 is numerically identical to the crude one-level contour bound, and
the entire content of Theorem NQ-1 at L = 3 is that **it does not compound** — exactly as §Q4 says ("off by the factor
(11/3)^{j−1} it claimed per level beyond the first"). Two consequences: the pre-registered BOUNDED threshold and the
proven constant are the same number by accident, which makes the gate look tighter than it is; and at L ≥ 5 Theorem
NQ-1 strictly beats p_L even at one level.

---

# Part E. The gates. The clean sweep does not survive unqualified

### NQ-21 (G1 does not strengthen c8(f)): **WRONG** as claimed; the gate itself PASSES
§Q2 says G1 "re-verifies L3g(a)-slice's identity on our own construction, as exact rationals rather than at 2e-16
(check c8(f))", and FOR-OTHER-FILES item 5(b) asks PROOF.md to record that this "strengthens check c8(f)'s 2e-16 to an
identity". **That is not what G1 does.** In `nq1_qnorm.py`, `q_root_pattern` is built as
(straight leg) + (axial path c_X→y) − (axial path c_Y→y+Le_μ); `h_pattern` is built as (axial path c_X→y); and
`gate_G1` compares them with `translate(hp, Le_μ) − hp`. The two sides are assembled from the *same two primitives by
the same code path*, so G1 can only fail if `pack`/`pdelta`/`translate` is broken. Its residual content is narrow but
real: it does test PROOF s23 l.1130's step ("the last term averages to h(Y) because y ↦ y + Le_μ is a bijection
B(X) → B(Y) and axial paths are translation covariant"), i.e. that the offset is exactly Le_μ and the path
construction is translation covariant.
What c8(f) tested is **strictly more**: it compared the actual (nonlinear) S4/S4′ map on U(1) small fields — where
PROOF s23 l.1131 notes the map is exactly linear — against Q_str − dh. That is a test that the *geometry of the real
contour construction* linearises to Q_root; G1 assumes it. **Binding fix: withdraw the "strengthens c8(f)" claim in
§Q2's G1 bullet and in FOR-OTHER-FILES item 5(b); state G1 as a self-consistency check of the translation step.**
My re-implementation reproduces G1 = 0 residual entries in all four directions from independent code, so the gate's
verdict stands.

### NQ-22 (discriminating power of G2-G5): NARROWED
- **G4** (Q_str returns L^j, all entries ≥ 0) cannot fail: `q_str_pattern` is non-negative by construction with row
  sum L, and products of such matrices have row sum L^j. Zero power. (It is also checked for all four directions only
  at j = 1; `mus = range(D) if j == 1 else (0,)`. Disclosed in the code comment, consistent with the criteria.)
- **G5** (direction invariance) cannot fail: ORDERS is the full permutation group and the block is symmetric, so the
  μ-patterns are coordinate relabellings of one another, and so are the composites. Zero power.
- **G2** (constant reproduction) is half tautological: on a constant 1-form the two funnel integrals of a single
  (σ, y) contour are *individually* equal (both evaluate to Σ_ν o_ν A_ν), so they cancel contour by contour and G2 at
  j = 1 reduces to the straight part. In particular **G2 cannot detect a wrong far-end offset**. At j ≥ 2 it does test
  that the composition preserves the property.
- **G3** (pure-gauge covariance, with a non-linear λ) is the one gate with real power: it pins the contour endpoints
  and orientations, since Q^j(d_0λ) = λ(L^je_μ) − λ(0) holds only if every contour runs from the near root to the far
  root. I re-ran it with a *different* non-linear λ (x₀³ instead of x₀²) and it passes.
- **The gap the suite leaves.** No gate compares Q_root against an **independent construction of the S4′ root map**.
  The dominant risk in this check was never arithmetic; it was implementing the wrong operator, and the suite is blind
  to it. My re-implementation from LINEAR_PACKAGE l.67/70 (different data structures, different arithmetic, different
  composition recursion) closes that gap and agrees entrywise. **This is the single most useful thing in this review:
  the FAIL-free sweep is honest but was under-powered, and it now has the missing independent control.**

### NQ-23 (§Q6's post-hoc check): NARROWED, and the labelling is honest
The post-hoc label is correct (`nq1_telescope_posthoc.py` born 13:16:04, after `nq1_out.txt` at 13:10:15) and the file
attaches no verdict to it. Two limitations the file does not state:
1. It `from nq1_qnorm import …` and reuses `compose`, `pack`, `pdelta`, `unpack`, `q_root_pattern`, `q_str_pattern`,
   `h_pattern` **unaltered**, so it is a self-consistency check: any bug in that machinery appears identically on both
   sides and cancels.
2. It cannot test the ev **exponent** at all. In the root-aligned convention every ev-ancestor of the level-j origin is
   the origin, so ev^{(m)} acts as the identity on origin-based rows for every m; the script never applies ev. Nothing
   load-bearing is lost (‖ev^m‖ = 1 for all m, so the norm bound is exponent-blind), but the check has no power over
   that index.
Both are closed by Part C: I derived the identity symbolically, and R3 verifies it with independent code.

---

# Part F. The fork: who is right about NORMS' sub-estimate

### NQ-24 (adjudication): **NQ_CHECK is right.** NORMS' hole is not a hole
NORMS §N4 l.409-417 expands Q^j = Π(Q_str − dh), estimates the term whose first h sits at level i as
"≲ ‖h‖·L^{j−1−i}·L^{i} = ‖h‖L^{j−1}", sums j such terms, and concludes 𝔮_0 ≤ 1 + 2d‖h‖·j/L — "only POLYNOMIAL in j" —
leaving the hole "*h applied to a pure gauge again produces a controlled gauge function*" (tally item 15, l.809-810).

The mechanism is exactly as NQ_CHECK says, and I verified each link of it:
1. **The M form is self-referential.** With Q_str∘d = d∘M one gets
   Q^{(m+1)} = S_mQ^{(m)} − D_{m+1}hQ^{(m)} = Q_str^{(m+1)} − D_{m+1}[M h^{(m)} + h Q^{(m)}], i.e.
   **h^{(m+1)} = M h^{(m)} + h Q^{(m)}** (PROOF s23 l.2787/2980). The second term feeds h the output of the *root* map
   Q^{(m)} = Q_str^{(m)} − d h^{(m)}, which contains the pure gauge d h^{(m)}. Bounding it therefore needs a bound on
   the very object being bounded; breaking the circle by charging the upward transport the generic factor L^{j−1−i} is
   what produces the j-linear accumulation.
2. **The ev form is not.** From the same two identities,
   **h^{(m+1)} = ev_m h^{(m)} + h Q_str^{(m)}**, so h^{(j)} = Σ_{i<j} ev^{(j−1−i)} h Q_str^{(i)} and every h acts on
   Q_str^{(i)}B_0 — **a straight composite of the input, never a pure gauge.** The hole does not arise.
3. **They are the same object.** The two recursions agree iff h∘d = M − ev on 0-forms, which is PROOF s23 l.1134's
   "h(A + dλ) = h(A) + Q_0λ − λ(c)". I verified both numerically: **h∘d and M − ev agree entrywise (81 entries, 0
   differing)**, and **h^{(2)} computed from the ev recursion and from the M recursion agree entrywise (23 328 entries,
   0 differing)**, and both satisfy Q^{(2)} = Q_str^{(2)} − d h^{(2)} in all four directions.
4. **So the disagreement is a bookkeeping loss, not a disagreement about a quantity.** NORMS' estimate is a *valid*
   upper bound that is simply looser for large j (j‖h‖L^{j−1} versus 2‖h‖L^j/(L−1)); at j ≤ 3 it is actually the
   *smaller* of the two, which is why the fork cannot be settled numerically and had to be settled by the identity.
   NORMS' own text already contained the right mechanism — "which does not grow the gauge function" (l.415) — and then
   charged the transport anyway. That is an internal inconsistency in the heuristic, now resolved.

**Verdict: (N-Q)'s named hole is withdrawn. NORMS tally item 15 should move ARGUED → PROVEN.** One caveat on the
wording NQ_CHECK proposes: NORMS' l.414-415 writes the transport law as "Q_str d_iμ = d_{i+1}(μ|centres)", which
conflates M (block mean) with ev (restriction to centres). Q_str∘d = d∘M and Q_root∘d = d∘ev; both have ℓ^∞ norm 1, so
nothing numerical turns on it, but the amendment NQ_CHECK asks for should fix that clause too.

### NQ-25 (NORMS §N1 misdefines Q_str): **NEW FINDING**, benign, and missing from NQ_CHECK's list
NORMS §N1 l.103-104: "*Q_str: its straight part, Q_str B(c) := L^{−(d−1)}Σ_{paths}Σ_{b∈path}σ_bB_b over the L^{d−1}
straight paths of L links*". That is **not** the Q_str of the slice identity. LINEAR_PACKAGE l.71 and PROOF s23
l.1133 average over the **L^d block sites** y, each contributing the straight leg y → y+Le_μ, i.e. L^d paths with
weight L^{−d}; NORMS' version averages only over the L^{d−1} **transverse** offsets and drops the longitudinal block
average. Both happen to have row ℓ¹ sum L, and my computation shows the operators differ: at L = 3, d = 4 the correct
Q_str row has **135** entries (longitudinal spread 1,2,3,2,1 over 5 positions), NORMS' would have 81.
Q_root = Q_str − d∘h holds for the former only.
*Impact:* benign. NORMS uses Q_str only through ‖Q_str‖ = L, ‖Q_str^T‖_{∞→∞} = L^{−(d−1)} and Q_str∘d = d∘avg, all of
which hold for the correct operator, and (I4) imports the identity from LINEAR_PACKAGE rather than from this
definition. But NORMS l.403-404's "immediate with 𝔮_0 = 1 for the straight average … (a straight composite contour is
L^j fine links; the transverse averaging weights sum to 1)" is reasoning with the wrong object, and the sentence should
be repaired. **This is a third NORMS text item for NQ_CHECK's FOR-OTHER-FILES item 1.**

---

# Part G. Downstream status claims, and scope

### NQ-26 (Theorem N1-15 is CONDITIONAL on (N-loc) alone): CONFIRMED
Checked against NORMS' own structure. Remark N6-1's table (l.565, l.567) marks exactly two rows conditional: the
level-j potential ℓ¹ mass (on (N-Q) **and** (N-loc)) and the level-j potential sup (on (N-Q) alone). With (N-Q)
discharged, the second becomes unconditional and the first retains (N-loc). §N6's steps (1)-(4) use Lemma N1-11 and
(N-loc) and nothing else that is open. Tally item 13's "⇐ (N-Q) and (N-loc)" becomes "⇐ (N-loc)". The conclusion
quoted by §Q4 — N3(D³E_k^br(1)) ≤ 𝔚 + 13.5·𝔖, A_soft = 1/L = 1/3 — is NORMS l.515-517 verbatim. ✓

### NQ-27 (Lemma N1-11 "CONDITIONAL on nothing further"): CONFIRMED-WITH-FIX — an over-reach of scope
NORMS tally item 12 does make Lemma N1-11 conditional on (N-Q) alone, and its proof's other inputs (Lemma N1-5,
Lemma N1-6, (I3), (I4)) are PROVEN or PROVEN-HERE. So *within NORMS' bookkeeping* the status moves. But NQ_CHECK did
not review Lemma N1-11's proof — its scope is "ONE question" — and FOR-OTHER-FILES item 1 nevertheless instructs
"item 12 (Lemma N1-11) CONDITIONAL → **PROVEN-HERE**" flatly. §Q4's hedge "within NORMS.md's own proof" is the honest
form and should be carried into the instruction. **Fix: "its last named condition is discharged; the remaining proof
was not reviewed here."** (I did read Lemma N1-11's proof while checking what (N-Q) is used for, and I note that
step (4) needs the composite bound at arbitrary starting level — see NQ-17 — and that steps (2) and (5) assert that
one fine gauge realises both the pure-gauge and the transported part simultaneously, which is NORMS' reviewer's
business, not mine.)

### NQ-28 (𝔠_P is still not a number): NARROWED
§Q4 says Lemma N1-11 becomes PROVEN-HERE "with 𝔠_P = 2[c_AX R_eff C_f·𝔮_0 + 𝔮_0·4κ̂C_R L²/(L²−1)] + 2 at 𝔮_0 = 11/3
(an explicit number where a named unknown stood)". Accurate about 𝔮_0, but 𝔠_P still carries **three** unevaluated
quantities: C_f and C_R are "absolute, uncomputed constants of Lemma 3.6" (LINEAR_PACKAGE Thm 3.8, l.197-198), and
R_eff is a free box side. Since the lead's D3 decision is "the constants are the enemy", the file should say that one
of four unknowns became a number, not imply 𝔠_P is now explicit.

### NQ-29 (scope: abelian/linearised, nothing for (N-bg), nothing for (N-loc)): CONFIRMED
§Q3's scope paragraph is correct and is correctly sourced. PROOF s23 l.1123-1125 [R3-fix] is verbatim as quoted: "*the
identity is linearised and abelian only: the nonabelian straight average is not even covariant, so there is no
nonlinear SU(N) analogue*". Input (i) therefore has no background version, so Theorem NQ-1 does not transfer, and
(N-bg) (NORMS tally item 20, Remark N6-5) is untouched. (N-loc) is untouched. §Q4's statement of the (H-C) C_♭ clause
— trivial background on (N-loc), class statement additionally on (N-bg) — matches NORMS tally item 14 and §N8 l.691
exactly. I found no place downstream where NQ-1 is used at a nontrivial background: Theorem N1-15 is explicitly a
trivial-background statement (NORMS l.624), and §N8's table carries the (N-bg) caveat.
§Q4(e)'s claim that no smallness condition moves is consistent with NORMS §N9 l.741.

### NQ-30 (what has already been propagated): NOTE
HANDOFF.md l.57-62 and SESSION24_RESULTS.md l.735-780 already record "(N-Q) PROVEN, 𝔮_0 = 11/3" and "conditional on
(N-loc) alone", with the abelian/linearised scope warning. HANDOFF l.35 correctly states that none of the session-24
files has been audited. **This review supports those entries**, subject to the binding fixes below.

---

# Binding fixes

**F1 (NQ-21, the only factual error I found).** Withdraw "strengthens check c8(f)'s 2e-16 to an identity" from §Q2's G1
bullet and from FOR-OTHER-FILES item 5(b). G1 compares two expressions assembled from the same two primitives by the
same code; it tests PROOF s23 l.1130's translation step and nothing more. c8(f) tests that the *nonlinear* S4/S4′ map
on U(1) linearises to Q_root, which G1 assumes. Replace with: "G1 is a self-consistency check of the row machinery and
of the Le_μ shift; it does not re-verify c8(f)'s content." If the lead wants an entrywise-exact re-verification of
L3g(a)-slice, it must build the S4′ transporter product and linearise it, not the linear contour average.

**F2 (NQ-22).** Add one paragraph to §Q2 stating the discriminating power of each gate: G1 near-tautological (F1),
G4 and G5 cannot fail for this construction, G2 cannot detect a wrong far-end offset (the funnel terms cancel contour
by contour on constants), G3 is the gate with real power, and **no gate compares Q_root with an independent
construction**. Cite this review's R1/R2/R3 as the independent control, with the three exact values reproduced.

**F3 (NQ-17).** State Theorem NQ-1 for any composite of m consecutive levels (or note that Q_i is the same operator at
every level in own units), because Lemma N1-11 step (4) consumes ‖Q^{j−1−i}‖ for the residual transport, not only
‖Q^j‖.

**F4 (NQ-27).** In §Q4 and in FOR-OTHER-FILES item 1, say "Lemma N1-11's last named condition is discharged; its
remaining proof was not reviewed in this file" rather than instructing the status change to PROVEN-HERE.

**F5 (NQ-25).** Add to FOR-OTHER-FILES item 1 a third NORMS text item: §N1 l.103-104 misdefines Q_str (L^{d−1}
transverse straight paths instead of the L^d block legs); the slice identity holds for the LINEAR_PACKAGE operator,
and §N4 l.403-404's "𝔮_0 = 1 for the straight average" argument is written against the wrong object. Also note that
NORMS l.414-415's "Q_str d_iμ = d_{i+1}(μ|centres)" conflates M with ev (Q_str∘d = d∘M; Q_root∘d = d∘ev).

**F6 (NQ-5).** Disclose the line-number convention at the head of §Q1: PROOF.md numbers resolve in
PROOF_session23_snapshot.md; RTARGET.md and SQ.md numbers resolve in the live files.

**F7 (NQ-3, NQ-20).** Record in §Q2 that the j = 1 clause of the BOUNDED criterion was forced a priori by
𝔫_1 ≤ p_L = 11, and that at d = 4 the proven 𝔮_0 coincides with p_L/L **only at L = 3** (L𝔮_0 = L + d(L+1)/2 vs
p_L = L + d(L−1)); at L ≥ 5 Theorem NQ-1 beats the crude bound even at one level.

**F8 (NQ-19, optional, non-binding).** Record the measured ‖hQ_str^{(i)}‖ = 8/3, 56/9, 488/27 (÷L^i: 2.667, 2.074,
2.008) and note that a proof of ‖hQ_str^{(i)}‖ ≤ (56/27)L^i for i ≥ 1 would give 𝔮_0 ≈ 3.07. Not needed for
Theorem N1-15, which consumes only boundedness.

**F9 (NQ-28).** Say that 𝔮_0 = 11/3 makes one of 𝔠_P's four unknowns explicit; C_f, C_R and R_eff remain.

---

# Independent tally

**PROVEN (I rebuilt the proof and could not break it)**
1. **Theorem NQ-1.** ‖Q^{(m)}‖_{∞→∞} ≤ L^m + (d(L²−1)/(2L))(L^m−1)/(L−1) ≤ (1 + d(L+1)/(2L))L^m for every m ≥ 1, for
   any composite of m consecutive levels, on Z^d and on every torus, for Setting SC's Q = Q_root, d ≥ 2, L ≥ 3 odd,
   abelian/linearised. At d = 4, L = 3: 𝔮_0 = 11/3. **This is (N-Q).**
2. The exact operator identity Q^{(j)} = Q_str^{(j)} − d_j Σ_{i<j} ev^{(j−1−i)} h Q_str^{(i)}, on all level-0 1-forms
   (no co-closedness), re-derived here by induction and re-verified entrywise by independent code at j = 1, 2.
3. ‖h‖_{∞→∞} = d(L²−1)/(4L) with **equality** (= 8/3); ‖ev^m‖ = 1; ‖Q_str^{(i)}‖ = L^i exactly with non-negative
   entries; ‖d_j‖_{∞→∞} = 2 exactly on 0-forms.
4. h∘d = M − ev on 0-forms, hence the ev-form and M-form composite slice functionals are the same object (verified
   entrywise at j = 2).

**CONFIRMED COMPUTED (exact, reproduced by an independent implementation)**
5. max_cΣ_b|Q^j(c,b)| = 205/27, 2021/81, 6115/81 at j = 1, 2, 3 (L = 3, d = 4), supports 459 / 47 385 / 4 113 747,
   all four directions, R_j = 2.530864, 2.772291, 2.796068.
6. ‖hQ_str^{(i)}‖ = 8/3, 56/9, 488/27 for i = 0, 1, 2 (my measurement; not in NQ_CHECK).

**SETTLED FROM THE FILES (I read all five locations in context and agree)**
7. Setting SC's Q is Q_root. The J-str / SHIFT conflict is not one. SQ §0.4 is correct and is a gauge shift, hence
   unavailable to a potential bound — which is why (N-Q) was a real question.

**CORRECTED HERE**
8. The G1 "strengthens c8(f)" claim is WRONG (F1).
9. NORMS §N1 l.103-104 misdefines Q_str; NORMS l.414-415 conflates M with ev (F5).
10. The Lemma N1-11 status instruction over-reaches NQ_CHECK's own scope (F4); the theorem's quantifier does not cover
    the composite its consumer uses (F3); 𝔠_P is not yet explicit (F9).

**NOT VERIFIED (outside my scope; I say so rather than vouch for it)**
11. Lemma N1-11's proof apart from its use of (N-Q); Theorem N1-15's exponent arithmetic beyond the two rows that
    (N-Q) touches; (N-loc); (N-bg); every other clause of (H-C); check c8(f) itself (I did not re-run it).

**Counted here: nothing.** This is a review, not a ledger.

---

# (c) Verdict on (N-Q)

**(N-Q) is PROVEN, at the following scope, and I could not break it.**

> For d ≥ 2, L ≥ 3 odd, Setting SC's averaging operator Q = Q_root (the linearised S4′ order-averaged root map), on Z^d
> or any level-j torus, **abelian / linearised only** (one real component around the trivial SU(N) background):
> ‖Q^{(m)}‖_{∞→∞} ≤ 𝔮_0 L^m uniformly in m, with 𝔮_0 = 1 + d(L+1)/(2L) = 11/3 at d = 4, L = 3; and the true constant
> is ≈ 2.80, with exact values 205/27, 2021/81, 6115/81 at m = 1, 2, 3.

Three things make me willing to sign this despite the project's record of reversed verdicts:
1. The proof uses **only two inputs**, both of which I rebuilt rather than cited (the slice identity's own one-line
   proof, and root covariance's one-line proof), and four elementary norm facts, all four of which I verified
   numerically as well as analytically.
2. The one step that could have been a subspace restriction is not one: the forward slice identity is unconditional,
   and the co-closedness in J-str attaches to the transpose. I checked the primary statement, not the file's gloss.
3. The computed values reproduce under an implementation that shares no code with the author's, including at j = 3.

Scope limits I insist on being carried with the statement: it is **not** a statement about Q_str (which is trivial), it
does **nothing** for (N-bg) because input (i) has no nonabelian analogue, and it does **nothing** for (N-loc).

# (d) Adjudication of the NORMS / NQ_CHECK fork

**NQ_CHECK is right; NORMS' hole was not a hole.** The precise reason: NORMS expanded the composite with the block mean
M, which gives h^{(m+1)} = M h^{(m)} + h Q^{(m)} — self-referential, because Q^{(m)} = Q_str^{(m)} − d h^{(m)} contains
the object being bounded, so h really is applied to a pure gauge and the circle has to be broken by charging the
upward transport the generic factor L^{j−1−i}, which is where the j-linear growth comes from. Expanding with the root
restriction ev instead gives h^{(m+1)} = ev h^{(m)} + h Q_str^{(m)}, in which **every h acts on Q_str^{(i)}B_0 and
never on a pure gauge**, and the upward transport of a pure gauge costs nothing because ev has norm 1 and the single
d at the top costs 2. I verified that the two expansions describe the *same* operator (0 differing entries at j = 2),
so this is a strictly sharper bound on the same quantity, not a different claim. NORMS' polynomial estimate remains a
valid but loose upper bound; [N1-corr 1]'s case 1 is the case that holds, and cases 2 and 3 are moot for this route.
NORMS tally item 15 should move ARGUED → PROVEN, with the two text withdrawals NQ_CHECK asks for plus F5.

# (e) The biggest live wall

**(N-loc), and behind it (N-bg) — and the honest reading is that (N-Q) was the small one.**

Theorem N1-15 now waits on a single named input, and that input is the one NORMS itself rates ARGUED with the harder
hole: the **gauge-variant** representative's exponential locality (NORMS l.422-432). Lemma N1-5's axial construction is
anchored at a box corner, not at x, and the object that would fix it — a multi-scale axial gauge — is already recorded
OPEN in PROOF under (CL-1). NORMS offers a trade (a near/far box truncation with a factor R_eff^d and an additive
Me^{−m′R_eff}), and that trade is "stated, not carried out" (l.432). **Carrying out that trade is the cheapest
remaining step on this whole route**, and unlike (N-Q) it cannot be settled by an identity: it needs a construction.

Beyond it, the structural wall is unchanged and is *not* a constant: (H-C)'s C_♭ clause is what BR1 and δ_Sch consume
as a Lipschitz bound on the small-field class, and Theorem N1-15 bounds only the trivial-background Taylor
coefficient. The gap is (N-bg), Theorem NQ-1 provably does not cross it (input (i) is abelian-only by PROOF's own
[R3-fix]), and both of NORMS' routes to (N-bg) run back into BFT-4/BFT-5. Three notes for the lead, in order of value:
1. **Do not let 𝔮_0 = 11/3 be read as a constants win.** §Q4(e) is right that no smallness condition moves. Against
   the lead's D3 ("the constants are the enemy"), this result removes a *depth dependence*, not a factor; 𝔠_P still
   carries C_f, C_R and R_eff.
2. The ev-form identity in finding 2 above is worth landing in LINEAR_PACKAGE next to Lemma 2.4 as NQ_CHECK's
   FOR-OTHER-FILES item 3 asks, because it is the non-self-referential form of PROOF's h^{(m+1)} recursion and any
   future *potential* bound (as opposed to curvature or residual) must go through it.
3. SQ's §0.4 deserves the one sentence NQ_CHECK asks for ("curvatures and residuals only; the potentials move by the
   accumulated funnel gauge"), because λ_{i+1} = avg λ_i + h(B_i) **is** the composite slice functional, and any
   consumer that reads §0.4 as licence to work with Q_str while bounding a potential will repeat exactly the error
   that (N-Q) was created to settle.

---

## Re-run record and reviewer probes

Scripts and outputs in scratchpad `revnq1/`: `rev_qnorm.py`, `rev_j3.py`, `rev_tele.py`.
I re-ran none of the author's scripts; all three probes are independent re-implementations from the primary
definitions (LINEAR_PACKAGE l.67/70/71, PROOF s23 l.596-597, l.1127-1131).

| probe | result | wall | peak RSS |
|---|---|---|---|
| R1 `rev_qnorm.py 2` | ‖h‖ = 8/3 exactly (216 entries); my G1 = 0 residual entries ×4; 𝔫_1 = 205/27, 𝔫_2 = 2021/81 ×4 directions; direction sums (L^j, 0, 0, 0); Q^j(dλ) = λ(far) − λ(0) for a λ with an x₀³ term; Q_str control 3, 9 with min entry > 0 | 1.4 s | 52 MB |
| R2 `rev_j3.py` | 𝔫_3 = 6115/81 in all four directions, by a streaming coordinate-0 sweep (peak window 776 385 of 4 113 747 entries) | 59.5 s | 482 MB |
| R3 `rev_tele.py` | Step 1 via my collapsed-ev derivation: 0 differing entries at j = 1, 2 ×4; h²_ev vs h²_M: 0 differing of 23 328; Q^{(2)} = Q_str^{(2)} − d h^{(2)} ×4: 0; h∘d vs M − ev: 0 differing of 81; ‖Q_str^{(1,2,3)}‖ = 3, 9, 27; ‖M‖ = 1; ‖hQ_str^{(1)}‖ = 56/9, ‖hQ_str^{(2)}‖ = 488/27 | 20.8 s | 914 MB |

- Exact `Fraction` / integer arithmetic in plain python, `python3 -I`, no numpy, no BLAS, one process, single thread,
  `nice -n 10`. **No numeric lock taken** (brief rule 6's exemption for exact rational/symbolic arithmetic). Load1
  1.94 at start. R3's 914 MB peak is disclosed; it is the largest single allocation I made and it was a one-off.
- No `checks/__pycache__` was created and no file under `checks/` was modified. No repository file other than this
  review was written. No git command was run.

## FOR OTHER FILES (not edited)

Nothing below has been written into any other file. The binding fixes F1-F9 above are addressed to the NQ_CHECK owner.
For the NORMS owner, via NQ_CHECK's FOR-OTHER-FILES item 1: in addition to the two withdrawals NQ_CHECK already asks
for, §N1 l.103-104's definition of Q_str is wrong and l.414-415 conflates M with ev (F5). For the lead: HANDOFF.md
l.57-62 and SESSION24_RESULTS.md l.735-780 are supported by this review, subject to F1 (the c8(f) strengthening claim
should not be propagated to PROOF.md) and F4 (Lemma N1-11's status wording).
