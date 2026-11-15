# Lane WITNESS: freeze a witness contract that actually excludes the required free class
**Why.** This is AUDIT priority 2. It blocks all 10 routes. Several shortcuts are already known to fail:
- ID♮ does not preserve products;
- a scalar GFF satisfies AF-e (NONFREE55 counterexample);
- W_T0 separates marked systems only;
- a single-scale gap is false against unrestricted free normalisations (W_T0).

**Target.** For the two most concrete candidates, (i) separated-e (EI/EM) and (ii) time-zero B (BI/BM), and for each of the three free classes below, decide which witnesses provably separate YM from the whole class. Separation must use only the reconstructed theory's OS data on one common algebra. The free classes:
- (F1) the finite canonical Wick / free YM class;
- (F2) all generalised free fields (any Källén–Lehmann measure, tensor-valued);
- (F3) all Gaussian / quasi-free states on the chosen algebra.

**Steps.**
1. For each witness × free-class pair, give PROVEN separation, a PROVEN counterexample, or OPEN with the exact YM estimate required.
2. Prefer witnesses whose YM-side inputs are fewest and already named, such as F17-WINS-B, MOM2-B and PL-1L.
3. Recommend one (algebra, free class, witness) triple as the target contract, with its full list of YM obligations.

**Deliverable: WITNESS.md**, with an owner-decision summary at the top. This is a recommendation; the owner decides OWN-alg and OWN-free. Read ASSEMBLY55 N0, N5, F1, N6 and N15; W_T0.md; F17.md; NONFREE55 and its review; HINT2_55 R1.9-R1.10; TSE55; LGF.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/witness_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only WITNESS.md, WITNESS_LOG.md and checks/witness_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.
