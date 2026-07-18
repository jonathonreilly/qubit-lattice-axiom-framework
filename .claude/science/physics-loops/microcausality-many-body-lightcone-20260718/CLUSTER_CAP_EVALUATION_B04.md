# Cluster-cap evaluation — microcausality family, PR #4 (block04, fermionic)

Date: 2026-07-18. Trigger: house rule — evaluator required from the
third PR in a family onward, recorded before the PR is opened. This
evaluation must also answer block03's own evaluation, which stated:
"The natural stopping point: the remaining named items (sharp rate,
U-integrated/tick-level, fermionic transfer bridge) are each a
different surface, not incremental slices of this one. No fourth
same-surface PR is planned; any follow-on would re-run this evaluator."

Family to date:
1. Block01 (#5508): qubit nested-commutator lightcone (Taylor level).
2. Block02 (#5511): qubit coefficient-level volume-uniform bounds +
   finite window.
3. Block03 (#5512): qubit Duhamel walk expansion — all-time
   volume-uniform LR bound.
4. Block04 (this PR): the CAR half of the fermionic transfer bridge.

Criteria:

- **Same-surface test (the block03 stopping-point statement).** PASSED
  AS A DIFFERENT SURFACE, exactly as block03's evaluation anticipated:
  the algebra changes (CAR, graded), the load-bearing lemma is new
  (graded locality from the CAR relations — absent from all three
  siblings), the observable class changes (arbitrary parity, with a
  genuinely different theorem shape: the explicit odd-odd zeroth
  term), and the motivating obstruction (JW strings breaking
  bond-locality) does not exist in the qubit family. This is the named
  "fermionic transfer bridge" item, not a fourth cut of the qubit
  surface.
- **Marginal value.** HIGH. The framework's supplied matter surfaces
  are fermionic; a locality family that stops at qubits does not reach
  them. Block04 carries the family's strongest result to the algebra
  the matter actually lives in, and isolates precisely what remains
  (the transfer-operator identification).
- **Mechanism novelty.** GENUINE but deliberately minimal: one new
  lemma (L-F) plus a motivation exhibit; everything else is cited to
  the sibling where natively gated, with algebra-adjacent instances
  re-gated fermionically. The note names the cite-vs-regate split
  step-by-step.
- **Independent reviewability.** YES: the lemma is rebuilt from the
  CAR relations in the note; the runner is standalone (JW
  representation built from scratch); sibling dependencies are
  needle-pinned.
- **Churn risk.** LOW-MODERATE, managed: the risk is "family sprawl"
  (a fifth block). Mitigation recorded here: the remaining named items
  (transfer identification, sharp rate, U-integrated) each require
  genuinely new inputs (Berezin/log-transfer machinery; optimization;
  gauge-measure structure) — none is reachable by the current
  machinery plus one lemma, so no fifth block is planned from this
  session's toolkit. Any future attempt re-runs this evaluator against
  that statement.

Verdict: PROCEED — block04 is the family's reach into the supplied
matter algebra via one new rebuilt lemma, anticipated as a separate
surface by the previous evaluation. Recorded before PR creation.
