# Combined adversarial lens — block06 (directional-tilt axis-cone refinement)

Role: hostile referee + independent mathematician. Attempt to REFUTE the note. Report BLOCKER / MAJOR / MINOR with exact sentences/gates attacked and concrete counterexamples or fixes. State survivals explicitly.

Files (read-only):
- docs/MICROCAUSALITY_DIRECTIONAL_TILT_AXIS_CONE_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-07-18.md
- scripts/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.py
- docs/MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md (the sibling whose count is refined)

Attack surfaces (do all, add your own):
1. Height tables: recompute both Delta tables independently. Check both transverse orientations and box stability. Any orientation the note misses?
2. The tilt polynomials, the domination factorization, and the row bound: is using S_par for ALL steps actually valid (walks change type mid-flight)? Verify the backward-recursion factorization argument in the note is airtight for MIXED-type walks.
3. The indicator bound and the offset: exact phi ranges at hyperplanes; the gain >= 2m-2 bookkeeping; the y^2 factor in the display; check the assembled inequality against the sibling's unrolled expansion TERM BY TERM (does the tilt count correctly replace the reach-restricted count, including the base-term factor and the k >= 1 start?).
4. The theorem display: is it really logarithm-free and exact at rational y? Is (4/25)^m right? Does anything hidden depend on d rather than m?
5. The velocity readout and certificates: verify e > 1957/720, ln(5/2) > 312/343 (and that 312/343 really is the two-term atanh partial), the pure-rational final comparison, and the pairwise scan gates. Any is_positive/None hazards?
6. Honest scope: per-axis vs isotropic (is the "both bounds hold" claim right?); scan-best vs optimality; bond class only; d >= 1 handling (does the tilt bound even need d, or only m — and is that stated correctly?).
7. Runner: vacuous gates, manifest, needle fragility, false-greens.

House conventions: axioms supply no dynamics; bounded_theorem notes claim exactly what runners gate; literature comparator-only; N1-N8 with ATTEMPTED markers and Status line; presence needles are not correctness oracles.
