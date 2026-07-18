# Combined adversarial lens — block05 (finite-range plaquette-class walk-expansion LR bound)

Role: hostile referee + independent mathematician. Attempt to REFUTE
the note before it ships. Report BLOCKER / MAJOR / MINOR with exact
sentences/gates attacked and concrete counterexamples or fixes. State
survivals explicitly.

Files (read-only):
- docs/MICROCAUSALITY_FINITE_RANGE_PLAQUETTE_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md
- scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py
- docs/MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md (sibling chain)
- docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md (the U-integrated open item)

Attack surfaces (do all, add your own):
1. Term-adjacency geometry: independently recompute 6/12/10/20/20/32 (hence 30/52), the diameters, the 804 walk count, and the reach values 2k. Any box-size or orientation dependence? Does the runner's enumeration actually cover all orientations (the fixed representatives claim)?
2. The dilated reach lemma: is k >= ceil(d/2) exactly right at the boundary (odd d)? Is the face-jump exhibit honest (distance-2 in one step)? Does the series-start bookkeeping match the walk definition (k terms, k-1 adjacency steps — check against the sibling's convention and the coefficient identity exponents)?
3. Chain carry-over: any step of the sibling chain that secretly uses BOND structure (two-site supports) rather than general term supports? The per-term reduced generator, the base-term bound 2J||B||, the first-step count n_X — all still correct for four-site terms?
4. The theorem display: coefficient (2J)^k n 52^(k-1), series start ceil(d/2), the mu-form transplant, the 208eJ readout — check every exponent and factor. Is the claim "not on the site dimensions" actually established by the mixed-dim gates?
5. Gauge-shaped coverage: is the edge->endpoint assignment argument airtight (magnetic face-supported, electric bond-supported)? Is anything about the U-integrated item smuggled (measure, kernel, correlations)? Is the Z2 instance faithful to the claim?
6. Scope hygiene: supplied vs derived, d >= 1 inheritance (tensor class — does the sibling's d = 0 counterexample really apply verbatim?), single-site subsumption, longer-range exclusion, non-sharpness language.
7. Runner: vacuous gates, instance-vs-universal honesty, needle fragility, manifest, anything false-green.

House conventions: axioms supply no dynamics; bounded_theorem notes claim exactly what runners gate; literature comparator-only; no new vocabulary; N1-N8 with ATTEMPTED markers and Status line.
