# NQ_DEF.md — what Setting SC's Q actually is, and what 𝔮₀ therefore is (target T55-P)

Owner: the T55-P worker, session 25. Append-only. Anyone may read it; nobody else writes it.
I write only this file and `checks/nd1_*`. I ran no git command, made no commit, no push, no PR.

**Line-number convention, stated once (REVIEW_NQ_S1 F6 asked for this and it is adopted here).** Every PROOF.md,
NORMS.md, LINEAR_PACKAGE.md, NQ_CHECK.md, REVIEW_NQ_S1.md and SESSION25_RESULTS.md line number in this file resolves
in the **live** file as of 2026-10-28 21:48 UTC, not in any snapshot. PROOF.md's numbering has drifted twice this
session, so every PROOF.md citation below is also given as a quoted string, which is the stable locator.

---

## §D0 PRE-STATED (first edit of this file, 2026-10-28 21:48:57 UTC; statements only; cites nothing produced in this session)

This section was written before any derivation, any script, any computation and any conclusion of mine. Nothing below
§D0 existed when §D0 was written. It names its inputs; it quotes no result produced in session 25.

**The question (T55-P).** NORMS.md §N4's named input **(N-Q)**: *‖Q^{j}‖_{∞→∞} ≤ 𝔮₀L^{j} for a constant
𝔮₀ = 𝔮₀(L, d), uniformly in j*, with ‖·‖_{∞→∞} = max_c Σ_b |·(c, b)| (the induced sup→sup operator norm = max row ℓ¹
sum). NORMS.md §N4 calls this *"a question about a DEFINITION, not a theorem"* and says it is *"immediate with
𝔮₀ = 1 for the straight average"*. SESSION25_RESULTS.md's T55-F entry names (N-Q) as **Theorem N1-15's only remaining
input** and asks whether Theorem N1-15 is therefore unconditional. NQ_CHECK.md (session 24) claims (N-Q) PROVEN as
Theorem NQ-1 with **𝔮₀ = 1 + d(L+1)/(2L) = 11/3** at d = 4, L = 3 — not 1 — and REVIEW_NQ_S1.md reviewed that claim.

**Named inputs I will read (naming them is not citing a session-25 result).** PROOF.md (Setting SC; L3g-ob;
L3g(a)-glob; L3g(a)-slice; J-str; IT-str), LINEAR_PACKAGE.md §0–§3, NORMS.md §N1/§N3/§N4/§N6/§N8/§N9/§N10,
NQ_CHECK.md, REVIEW_NQ_S1.md, SQ.md §0.4/§11.0, SESSION25_RESULTS.md's T55-F entry, TUNIF.md.

**Targets.**

- **TD1 (the definition, from the definition).** Locate Setting SC's definition of Q **by string** in the live
  PROOF.md and quote the defining sentence with its live line number. Do not accept any file's description of it.
  Then locate, in LINEAR_PACKAGE.md, the definitions of the three objects that sentence points at (the root map, the
  straight average, the slice functional) and quote them with line numbers. Report which of the three operators is
  Setting SC's Q.
- **TD2 (𝔮₀ from the definition).** Compute ‖Q^j‖_{∞→∞} from that definition. If Q is the straight average, report
  𝔮₀ = 1 and say so. If it is not, give the actual 𝔮₀ and say whether (N-Q) holds with it.
- **TD3 (re-derive, do not cite).** Re-derive Theorem NQ-1's statement from its two claimed inputs (the slice
  identity and root covariance) by my own induction and my own norm computations, and either confirm 𝔮₀ or refute
  it. A banked PROVEN and a banked review are evidence, not certificates.
- **TD4 (reconcile 1 against 11/3).** Decide which of three things the pair (1, 11/3) is: the same operator with two
  bounds, two different operators, or one bound that is not tight. Verify **by file:line** which operator each number
  is about. Report it as an instance of, or a counter-instance to, systemic defect 1.
- **TD5 (does the difference matter).** Determine whether any named consumer needs 𝔮₀ = 1 rather than 𝔮₀ = 11/3 —
  specifically whether 𝔮₀ enters any exponent, any level-ratio that must be < 1 (A_soft), or any smallness threshold.
  If 11/3 suffices everywhere, say the distinction is academic, plainly, rather than manufacture a problem. If some
  consumer needs 1, name it.
- **TD6 (the quantity that is actually load-bearing).** State which property of 𝔮₀ Theorem N1-15 consumes — its
  value, or its independence of j — and what the theorem's conclusion becomes if that property fails.
- **TD7 (consequence for Theorem N1-15).** State exactly what becomes unconditional, in exactly which regime, and
  what does not. The regime caveats (d = 4, trivial background, abelian/linearised) are load-bearing and must travel
  with any claim. Name what is still open.

**Pre-registered failure modes (things that would make my answer wrong, written before I look).**

- **Q-F1.** Setting SC has more than one definition of Q in the live PROOF.md, or the definition points at an object
  that is itself undefined. Then the finding is "a load-bearing operator left undefined" and TD2–TD5 change character.
- **Q-F2.** The operator in (N-Q) is not the operator in Setting SC — e.g. NORMS' Q is a third object, or the Q in
  Lemma N1-11's step (4) is not Setting SC's. (Systemic defect 1, applied to the symbol Q itself.)
- **Q-F3.** 𝔮₀ enters an exponent or a level-ratio and not only a prefactor, so that 11/3 vs 1 is decisive at d = 4.
- **Q-F4.** Theorem NQ-1's bound is stated for composites anchored at level 0 while its consumer needs composites
  anchored at an arbitrary level, and the proof does not deliver that.
- **Q-F5.** My own check is unable to fail (systemic defect 3). Every gate below carries a designed-FAIL control, and
  a control that passes when it should fail voids the gate.
- **Q-F6.** (N-Q) is discharged but Theorem N1-15 has an input I have not enumerated, so "unconditional" is wrong.

**Pre-registered criteria for the one computation I expect to run (check nd1).** Criteria go in
`checks/nd1_criteria.md`, written before the script exists; the constants in them (L = 3, d = 4, L^j = 3, 9) are
Setting SC's own hypotheses, not session-25 outputs. Exact `Fraction`/integer arithmetic, plain python, one process,
no numpy, no BLAS, no numeric lock (brief rule 6).

**Not success.** Declaring (N-Q) settled by citing NQ_CHECK or REVIEW_NQ_S1 rather than re-deriving it; reporting
𝔮₀ = 1 because it is the convenient answer; calling Theorem N1-15 "unconditional" without carrying the regime
caveats; asserting that 11/3 breaks something without naming the consumer and the threshold; running a gate with no
designed-FAIL control.

---
