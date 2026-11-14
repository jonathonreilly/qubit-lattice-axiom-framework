# Lane K4MATCH: the Yang–Mills side of the fourth-cumulant witness
**Why.** CUMUL.md and COMBO.md give a witness. It is AF-e together with a nonzero separated fourth cumulant κ4 of e, and it provably excludes F1 ∪ F2 ∪ F3. For free Yang–Mills the leading coefficient of κ4 is PROVEN positive. What is OPEN is the Yang–Mills estimate: |κ4(YM)| ≥ c > 0 uniformly along the common sequence.

**Target.** Prove or reduce the lower-matching statement
κ4^{YM}(f_1..f_4; λ) = κ4^{free}(...)·(1 + o(1)) at short scale λ,
using asymptotic freedom. Work in normalized ratio form, as in CUMUL §normalisation. Model it on WITNESS's E-TS / PL-1L route for the two-point function, and reuse every shared input: LGF (landed), FLOW, source estimates S, and TSE55 Theorem TS machinery. Then:
1. List the exact estimates needed beyond those in the AF-e half. Show which ones are already covered by shared inputs.
2. Check whether a four-insertion source representation is required, compared with the two-insertion one for PL-1L. Name what extra the RG must supply.
3. Do a perturbative sanity check of the O(g²) correction to κ4: its sign and size. The check must show that the correction does not cancel the leading term at the relevant scales. Use exact or rational arithmetic where the conclusion depends on the numbers.

**Deliverable: K4MATCH.md.** It needs a PROVEN, ARGUED or OPEN status for each item, the exact list of YM obligations, and a comparison against PL-1L.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/k4match_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only K4MATCH.md, K4MATCH_LOG.md and checks/k4match_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.
