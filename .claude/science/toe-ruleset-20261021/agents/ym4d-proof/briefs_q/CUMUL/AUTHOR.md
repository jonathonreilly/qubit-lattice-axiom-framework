# Lane CUMUL: a connected-correlation witness that excludes ALL Gaussian free classes (F2, F3)
**Why.** WITNESS.md showed that AF-e and the time-zero two-scale witness each separate only the finite canonical Wick class F1, or a marked subclass. It also gives PROVEN counterexamples for F2 (all generalised free fields) and F3 (all Gaussian states). The owner wants every variant probed, and the strong standard meaning of "non-trivial" is "not Gaussian". The natural witness for that is a nonzero truncated (connected) correlation.

**Target.** On the separated-e hierarchy A_e of WITNESS.md, or on any other common-algebra field family that works better, use the truncated n-point Schwinger function S_n^T for n = 3 or 4, at fixed separated test functions.
1. **Comparator (prove).** Show that S_n^T = 0 for every state in which the chosen field is a generalised free field or Gaussian (F2 and F3, tensor-valued included). Check that this holds on the reconstructed OS theory, not just on the Euclidean state. Use the landed REC_LIB / REC_CONT.
2. **Witness form.** S_n^T at fixed test functions is a continuous finite-moment functional. Check that this matches N5's finite-moment criterion as consumed by N1F, so that no change to N5 is needed (unlike WITNESS's AF-e route).
3. **Yang–Mills side.** State the estimate needed, |S_n^T(YM)| ≥ c > 0, uniformly along the common sequence.
   - Use asymptotic freedom: at short separations the leading term is the free-Yang–Mills value of the truncated function of the composite e ~ F²/2u. That value is nonzero because F² is quadratic in a Gaussian field. Compute that leading coefficient exactly, and check that it is nonzero.
   - The existence lane's tree-level non-Gaussianity value NG-ax = 0.012827·N(N²−1)g⁴ is a related object. Grep ../ym4d-existence/E/EXISTENCE.md, and relate the two or rebuild it.
   - State the lower-matching estimate that is needed: the analogue of PL-1L for the connected function, at relative error o(1). State the upper and moment inputs too.
   - Compare how hard all of this is against WITNESS's E-TS / PL-1L.
4. **Normalisation.** Since S^T is not invariant under field rescaling, use a scale-free ratio, for example S_3^T / (S_2)^{3/2}, or the corresponding quantity for n = 4. Check that it still excludes every rescaled Gaussian field.

**Deliverable: CUMUL.md.** It must contain:
- the PROVEN comparator theorem;
- the exact leading free-YM coefficient, with an exact finite check pre-registered and using rational or interval arithmetic where the value is load-bearing;
- the exact list of YM obligations;
- a verdict on whether this gives F2/F3 non-triviality with fewer obligations than WITNESS's route.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/cumul_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only CUMUL.md, CUMUL_LOG.md and checks/cumul_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.
