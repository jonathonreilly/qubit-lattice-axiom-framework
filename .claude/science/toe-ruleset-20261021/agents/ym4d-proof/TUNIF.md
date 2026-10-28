# TUNIF.md — T-uniformity (target T55-F)

Owner: the T-uniformity worker, session 25. This file is append-only. It may be read by anyone; nobody else
writes it. Requests for other files are collected in the final section "FOR OTHER FILES (not edited)".

---

## §U0 PRE-STATED (first edit of this file, 2026-10-28T21:27:45Z; statements only; cites nothing produced in this session)

This is the first edit of this file. Nothing below §U0 existed when §U0 was written. §U0 fixes the targets, the
admissible outcomes and the failure modes so that the rest of the file can be read against them.

**Disclosure, in the manner of EXISTENCE §21.0.** Exploratory reading preceded this text and was not written
down: HANDOFF.md, NLOC.md (all), NORMS.md §N2-§N8, GREENT.md §G0, SESSION24_RESULTS.md (the NLOC/GREENT/TGAUGE
entries), RTARGET.md §54, LINEAR_PACKAGE.md §3-§4, PROOF.md l.5835-5858 and l.6110-6135, EXISTENCE.md §21.3, and
greps of the lane for "T-uniform". That reading included the observation that the obstruction NLOC §L7 names is a
twisted-complex division problem and the plan to attack it by the two σ-telescoping identities; it produced no
written derivation and no number. Every number quoted in §U0 is read off a file that existed before this edit.

**On the no-constant rule.** No constant in §U0, and none in any `checks/tu1_*_criteria.md`, is derived by me.
Thresholds are either structural 0/1 verdicts or numbers already in NLOC.md / LINEAR_PACKAGE.md / NORMS.md.

### Scope

This file attacks **T-uniformity** and nothing else. T is the **coarse (level-k) torus side**; the level-j side is
T_j = T·L^{k−j} and the fine side is T·L^k (LINEAR_PACKAGE §1.1 convention, as used by NORMS.md and NLOC.md).
I write **no** other lane file. I do not touch the axioms.

### Targets

- **T-U0 (the statement, with its quantifiers).** Write out what "T-uniformity" means in this lane, with every
  quantifier shown: which object, which norm, over which range of T, jointly with k or separately, and for which
  consumer. The lane uses the phrase for at least two different things (NLOC's (N-loc♯)/Theorem N1-15 constant,
  and BFT_B's "k-, T-uniform" labels); say which is open. **A sharp statement is itself a deliverable.** If a
  quantifier in the recorded statement is weaker or stronger than the consumer needs, say so and give the repaired
  statement.
- **T-U1 (the consumer).** Determine, from the consumers themselves (PROOF.md's Lemma BR1, Theorem NAH1 (b)/δ_Sch,
  Proposition NAH-unif / (H-C); EXISTENCE.md §21.3), whether T-uniformity is needed over all T ≥ T_0, over a
  bounded range, or not at all; and at which exponential weight m the consumer's norm is taken. Report what is
  demanded by a named consumer and what is only asserted.
- **T-U2 (the open half).** NLOC.md §L7 names **(N-loc-cell)** as what is left of (N-loc-b), and says the missing
  step is "the twisted analogue of Lemma NL-10 (b) … one lemma, not a programme". **Attempt that lemma.** If it is
  proven, carry it through to (N-loc♯) and to Theorem N1-15 and state exactly which constants are T-free. If it is
  not, say which step fails.
- **T-U3 (the price without it).** State the T-dependence of Theorem N1-15 that is actually proven today, from
  the files as they stand, and re-derive any step of it I lean on. GREENT.md and NLOC.md are UNREVIEWED; nothing
  from them is to be cited as settled.
- **T-U4 (the (GT-sup) reduction).** REVIEW_BFT_B_S9_S10 marks the reduction of (GT-sup) to (Y-sup^loc)
  NOT-VERIFIED; BFT_B's Proposition GT-loc claims it with an absolute constant 20 and Lemma ΓT-op (d) carries an
  absolute constant. **Check the reduction myself** and give a verdict, inheriting neither.
- **T-U5 (uniformity in L, k, j, N).** State for every item proven here whether the constant depends on j, k, T,
  or on the torus at all, and say where it would fail if it did.

### Admissible outcomes, pre-registered

- **(U-O1)** T-uniformity PROVEN for Theorem N1-15 at its scope (d = 4, trivial background, abelian/linearised),
  with every constant exhibited and T-free, and the consumer clause checked.
- **(U-O2)** A weaker statement proven and checked to suffice for the consumer that actually exists; the stronger
  one withdrawn as unnecessary.
- **(U-O3)** CONDITIONAL on one named new input, named explicitly with its own status.
- **(U-O4)** T-uniformity, or one of its recorded statements, **FALSE as stated**, with the obstruction exhibited
  and the repaired statement given. To be reported as a refutation, not dressed as progress. A no-go must be
  tested by reframing it as a positive claim.
- **(U-O5)** No progress. To be reported plainly.

### Pre-registered failure modes for this session's own work

- **(U-F1) The hidden T.** A constant called absolute that contains the torus side through a cell count, a volume,
  a line length, a smallest nonzero momentum 2π/T, or a periodisation count. Every sum over the torus must be
  exhibited and its T-dependence named.
- **(U-F2) The L^k leak.** A construction that gains the required L^k once but pays it twice (e.g. two nested
  within-cell line integrations), giving L^{2k} or L^{3k} where the budget is L^k. The budget is
  |b|_∞ ≲ L^k|d_0B_0|_∞; any assembly must be counted, not asserted.
- **(U-F3) The wrong leg.** Proving the sup (ℓ^∞) half and calling it the ℓ¹ half. NLOC [NL-corr 1] already has
  the sup half T-free; the open half is the column ℓ¹ mass.
- **(U-F4) Two representatives.** Taking the sup bound from one admissible representative and the ℓ¹ bound from
  another. NORMS Theorem N1-15 needs both from the **same** admissible family (NLOC §L2 (A3), Proposition NL-9).
- **(U-F5) Admissibility dropped.** A gauge that is not in Lemma N1-2's admissible class (nested, trivial at the
  level-k roots). Without it Theorem N1-15's identity is not available and the result is void.
- **(U-F6) Analyticity assumed where only a discrete torus exists.** On the coarse torus the momenta are the
  discrete set (2π/T)Z^d; a division by ν_μ = e^{ip_μ} − 1 at the smallest nonzero momentum costs T unless the
  numerator's vanishing at p_μ = 0 is used together with an analyticity (strip) bound. If I divide, I must say
  which strip and which theorem supplies it.
- **(U-F7) The zero mode swept into a seam.** The chain's constant (harmonic) mode cannot be removed by any gauge.
  It must be exhibited and counted, not absorbed.
- **(U-F8) Quoting an unreviewed file as settled.** GREENT.md, NLOC.md, NORMS.md, NQ_CHECK.md, CONST_T.md,
  STAR_CONST.md are all unreviewed. Any load-bearing step taken from them is to be re-derived here.
- **(U-F9) A gate that cannot decide.** Any check must be able to fail, must have a designed-FAIL control, and the
  control's failure must be reported.

### Not success

Numerics in place of a proof. A statement at fixed T called T-uniform. A log called a constant. A bound whose
constant is not exhibited as a function of (N, L, d, κ_±, m). Declaring (H-C)'s C_♭ clause discharged: Theorem
N1-15 bounds D³E_k^br(**1**), and **(N-bg) is untouched and is the larger wall** (NORMS Remark N6-5, NLOC §L8).
Declaring anything about the nontrivial background.
