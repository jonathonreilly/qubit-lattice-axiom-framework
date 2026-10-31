# Lane MIXGFF: can the witness be extended to mixtures of GFFs and to Wick composites of GFFs?
**Why.** COMBO.md has PROVEN counterexamples. AF-e ∧ κ4≠0 does not exclude finite mixtures of elementary generalised free fields. It also does not exclude Wick composites of arbitrary generalised free fields. The owner wants every direction probed, so this lane tests stronger non-triviality.

**Target.** Find a witness, or a combination of witnesses, on the same separated-e algebra and with the same OS reconstruction, that excludes these classes too. Candidates:
- (a) Cumulant-ratio rigidity. Mixtures of Gaussians have specific moment and cumulant relations; one example is the positivity structure of κ4 for scale mixtures. YM may violate those relations at short distance, and this can be checked against the free-YM leading values.
- (b) A short-distance operator-product / scaling witness. Composites of GFFs have exact scaling dimensions with no logarithms. YM has asymptotic-freedom logarithms, the anomalous scaling of tr F² through the β-function. This is the AF-e idea extended to composites of *arbitrary* GFFs.
- (c) Cluster or extremality arguments. A mixture is not extremal, so if the YM state is shown to be extremal (clustering, at least partial), mixtures are excluded. This is a weaker infrared input than a mass gap. Estimate what it needs.

For each candidate give PROVEN separation or a counterexample, plus the YM obligations it requires.

**Deliverable: MIXGFF.md**, recommending the strongest free class that is reachable with the fewest new YM obligations.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/mixgff_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only MIXGFF.md, MIXGFF_LOG.md and checks/mixgff_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.
