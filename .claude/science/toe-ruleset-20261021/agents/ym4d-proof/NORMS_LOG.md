# NORMS_LOG.md — provenance log for NORMS.md (session 24, N1 worker)

## Edit 1 — the PRE-STATED section
- Written: 2026-10-28 12:36:53 UTC (timestamp taken before the edit).
- `stat` immediately after the edit: `NORMS.md size=5524 mtime=Oct 28 08:37:28 2026` (local = UTC-4), i.e. 12:37:28 UTC.
- Content: §N0 only (targets T1–T6, the anti-circularity clause, the admissible outcomes O1–O4, the pre-registered
  failure modes N-F1…N-F5, and the "not success" list). Statements only. No derivation, no constant produced in this
  session, no reference to anything produced in this session.
- This was the first edit of NORMS.md and the first write of any kind by this worker.

## Inputs read before the PRE-STATED section (all read-only)
- scratchpad/DRIVE_BRIEF.md (the binding process rules).
- $L/HANDOFF.md.
- PROOF.md l.5790–5880 (BR1 (iii)/(v), Lemma SC1, Lemma LOC, Theorem NAH1), l.6055–6115 (𝒦, 𝒦_ρ, Lemma CURV-lin,
  Lemma CURV1), l.6160–6250 (Lemma E3, Proposition NAH-unif, (H-K)/(H-C) status, check c37), l.6250–6420 ([S22]: ENV,
  H-fac, HG1, LOC_1, CURV1_1, HG-ind, CURV-F2′, CURV-F2″, NAH-unif′), l.6463–6560 ([S22]: TOWER-VAR, COMP, (CL-1)–(CL-4),
  (CL-cl)/BFT-4, c38), l.6575–6714 ([S23]: the BFT statement, the cross-lane map, the BFT clause table).
- REVIEW_S22.md l.380–445 (the BFT statement in full, including the norm 𝔐 and the anti-circularity clause).
- RTARGET.md §33 (the SF/§33 norm pair: coarse-unit conversions, divergence-form source norm Y, Hölder/Campanato
  seminorm, X_s, X_f, X_c, level weights ω_l = L^{θ(k-l)}, and the targets (G♯_0-soft), (G♯_0-fine), (G♯_0-field)).
- LINEAR_PACKAGE.md §2–§4 (Lemma J-str, Lemma LES, Proposition BG-b-lin, Lemma LED-dual/symb, Lemma WA,
  Proposition LED-unif, **Theorem N2-lin (3.8)**, Theorem N2-exp (4.2) and N2-exp′ (4.2′)).
- SF.md l.70–82 (Corollary SF-thr-k, (BG-unif)), l.2820–2850 (the ε_1-driven rows), HW.md l.1630–1735 (the g²_CRC
  arithmetic).
- A coordinator message (received after the PROOF.md reading, before the PRE-STATED edit) directing the work onto 𝔐 and
  the §33 pair, restating the anti-circularity clause, asking for the θ_w-dependence of A, and asking whether this route
  is an alternative to BFT-4 or a tool inside it. Its four points are T1, the anti-circularity clause, T5 and T4 of §N0.

## Edit 2 — §N1–§N10 and the FOR OTHER FILES section
- Written after §N0, in one pass. Nothing in §N0 was altered.
- Checks: `checks/n1_criteria.md` written before `checks/n1_exponents.py` (see that file's header for the time).
  The check is exact integer/rational arithmetic in plain python, single process, no BLAS, no numeric lock taken
  (permitted by the brief's rule 6 for exact symbolic/rational arithmetic).

## Edit 3 — two typographical repairs inside edit 2's text (no claim changed)
- Lemma N1-1's statement: a garbled ℓ¹-mass expression for M_W ("2·C(2d−2,2)·½·2 = 2(d−1)(2d−3) … M_W ≤ 12") replaced by
  the single correct count **M_W ≤ 6** (four links on a plaquette, C(4,2) = 6 pairs, BCH coefficient ½, commutator
  factor 2; the same in every d). The proof already derived M_W ≤ 6.
- Lemma N1-1's proof (c): one mojibake glyph in "𝔮(X, W)".
- Theorem N1-15's statement: the fragment "A = L^{d−5}·L^{?} → the clean statement:" replaced by the clean sentence it
  was introducing. No constant, exponent or status changed.
- FOR OTHER FILES item 3: one U+FFFD glyph restored to "𝔠_∞".
No other text of edit 2 was altered. §N0 (PRE-STATED) is untouched throughout.

## Edit 4 — cross-reference normalisation (no claim changed)
- "Lemma N1-10" → "Proposition N1-10" (four places); the item is stated as a Proposition in §N4 (b).
- §N1 headline item 3: the soft vertex's first exponent printed as "(d − 1 − n)" corrected to "(n + d − 1)", which is
  what §N6 step (3) derives and what makes the sum (d − 1) − n. Arithmetic typo in the summary line only; §N6, §N7 and
  check n1-C were already correct.
- Final state: NORMS.md 918 lines, 81173 bytes, 12:57 UTC.
