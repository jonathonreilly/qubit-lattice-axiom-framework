# C3 lane F: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

## VERDICT: CONFIRMED WITH CORRECTIONS

The fixed reading supports a **bounded FAIL**, not a universal no-go for label-free, order-only growth.

### Findings

1. **Theorem L is correct after fixing the definition of \(D\).** The proof through \(J(a)-J(a-1)\), concavity, the compensator, and the tail bound closes ([C3_F_report.md:191](C3_F_report.md:191)). However, \(D\) must be called an exchangeable **generating/selected ancestor set**, not the actual direct-ancestor or cover set. Ordinary CSG samples such a subset with probability proportional to \(t_{|D|}\) and then takes transitive closure ([contlim.txt:134](work/lit/bg2010/contlim.txt:134)). Its actual covers are not generally exchangeable. With that correction, single-era \(P(t)\) CSG—including zero individual \(t_k\), \(t_0=0\), mixtures, and stage/history-dependent exchangeable size laws—satisfies the theorem. Stage-dependent laws need not themselves be DGC/CSG.

2. **The bound is sound and slightly stronger than reported.** One has
   \[
   \mathbb E X_i\le \mathbb E H_{|\uparrow i|},\qquad
   \mathbb E[L]/N\le H_{N-1}<1+\ln N.
   \]
   My exact-enumeration reruns reproduced all reported cases and the nonexchangeable counterexamples. But “for every \(N\ge300\)” is not exact from the supplied evidence: the theorem is exact, while the 4D comparison is Monte Carlo at selected \(N\). The defensible finite statement is for the tested sizes, including \(N=300,500,1000,2000,4000,8000\) ([C3_F_report.md:142](C3_F_report.md:142)).

3. **The frontier lemma is exact.** Selecting only current maximal elements makes the selected elements covers; after its first selection an element ceases permanently to be maximal, so it can acquire no second future cover. Hence \(L\le N-1\), independently of probabilities or label invariance ([C3_F_report.md:220](C3_F_report.md:220)).

4. **The BG result and tower extension work, with the checker’s correction.** BG Theorem 1.5 is uniform in \(t\) and gives closeness in expected normalized pair-edit distance—not literal equality to a semiorder ([contlim.txt:175](work/lit/bg2010/contlim.txt:175)). VR establishes ordinally stacked turtles, with all later-turtle elements above prior turtles ([vr.txt:710](work/lit/vr2006/vr.txt:710)). Ordinal sums preserve semiorders, and short eras cost at most \(Nn_0/2\) edits. Thus \(\Delta\le1.5\epsilon N^2\) implies an asymptotic forbidden-density bound of \(18\epsilon\), not \(12\epsilon\). The corresponding numerical choice is approximately \(\epsilon<2.6\times10^{-4}\). Since \(n_0(\epsilon)\) is not explicit, this gives no accessible-size bound for the full tower class.

5. **The tower counterexample is valid and important.** Re-running the supplied independent implementation reproduced the dust\((48)\oplus\mathrm{TP}(952)\) result: \(r=0.0985\), \(L/N=17.32\), \(H=10.7\). It evades Theorem L and matches the principal link target, but fails \(n_{\min}/N\), \(n_1/n_0\), and both forbidden four-point densities ([C3_F_report.md:299](C3_F_report.md:299)). Therefore Theorem L is not a finite-\(N\) theorem for the full DGC+Bell class.

6. **The principal numerics check out, with minor qualifications.** Stored data reproduce \(L/N=17.746\pm0.105\) SE at \(N=1000\), and the reported combined-SE z-scores through \(1355.8\). An independent direct sampler gave four-point probabilities \(0.004849\pm0.000040\) for \(2+2\) and \(0.004939\pm0.000040\) for \(3+1\), consistent with the report ([C3_F_report.md:163](C3_F_report.md:163)). The expected four-point law is exactly \(N\)-independent; the displayed decimal values are Monte Carlo estimates. Minor numerical caveats are that the OP sampler approximates the earliest zero-truncated binomials ([fcore.py:140](work/scripts/fcore.py:140)), and the four-point reference count is hard-coded from an earlier run ([F3_fourpoint.py:13](work/scripts/F3_fourpoint.py:13)). Neither affects the conclusion. The CSGMIX optimization did not actually match both targets; its class-wide exclusion comes from Theorem L, not the sparse grid search.

The fixed reading expressly permits “a no-go under stated hypotheses” ([TESTS.md:528](TESTS.md:528)), so the bounded FAIL is admissible. But “Markovian label-invariant” is broader than CSG: Bell causality is an additional hypothesis, and structure-aware order-invariant kernels remain open.

### Strongest correct statement

A label-free rule is **not ruled out in general**. What is established is:

- conditionally exchangeable generating-subset growth cannot reproduce the tested 4D link means;
- frontier-only growth has \(L\le N-1\);
- every classical DGC+Bell dynamics, including VR turtle towers, is asymptotically incompatible with 4D sprinkling because its \(2+2\) and \(3+1\) densities vanish while the 4D values remain positive.

Thus “records forming cannot produce the event set” is not established. The strongest conclusion is that records cannot do so through these exchangeable, frontier-only, or classical DGC+Bell mechanisms. A surviving rule must use order structure nonexchangeably—or leave the Markovian/classical/Bell-causal scope—and must still match all prescribed observables.