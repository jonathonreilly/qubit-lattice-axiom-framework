# Lane COMBO: a combined witness that excludes F1 ∪ F2 ∪ F3 together
**Observation (lead).** Two landed lanes each cover part of the free classes:
- **WITNESS.md:** AF-e on the separated e hierarchy excludes F1, the finite canonical Wick polynomials in canonical free fields, which includes the Wick composites. It fails for F2/F3.
- **CUMUL.md:** a nonzero separated fourth cumulant κ4 of e excludes all elementary F2 and all F3. It fails for Wick-composite realizations in free theories, which are F1-type.

So the conjunction W = (AF-e holds) ∧ (κ4 ≠ 0) appears to exclude F1 ∪ F2 ∪ F3.

**Target.**
1. **Union exclusion.** Prove it: each class fails at least one conjunct, on the same algebra A_e with the same normalisation (Z(a) = 1) and the same OS reconstruction (REC_LIB/REC_CONT). Check the edge cases:
   - mixtures;
   - affine shifts;
   - tensor-valued fields;
   - states that are Gaussian on e but Wick-composite in some underlying free theory. Show which conjunct catches them, or give a counterexample to the union claim.
2. **Witness form.** Is W a single continuous finite-moment witness that N5/N1F accept? If not, state the exact restated contract, for example a two-part witness with a finite-moment component and an asymptotic component, and what N5 must say.
3. **Yang–Mills obligations.** List the combined YM obligations: E-ALG, E-SEQ, E-TR, E-TS/PL-1L for AF-e, plus CUMUL's fourth-cumulant lower matching. Identify which inputs they share (the same flowed or separated e, the same source estimates S, the same LGF), so the extra cost of the conjunction is explicit.
4. **Free-class strength.** Compare with the classes the target T_OS must exclude, and say what is still not excluded. For example: arbitrary non-Gaussian free-composite constructions outside F1, or interacting but trivial-in-another-sense theories.

**Deliverable: COMBO.md**, with a PROVEN/ARGUED/OPEN status on each claim. Read WITNESS.md, CUMUL.md and their reviews, ASSEMBLY55 N5/N1F, and NONFREE55.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/combo_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only COMBO.md, COMBO_LOG.md and checks/combo_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.
