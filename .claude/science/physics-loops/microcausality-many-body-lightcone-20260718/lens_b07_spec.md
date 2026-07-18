# Combined adversarial lens — block07 (weighted quasilocal-class walk-expansion LR bound)

Role: hostile referee + independent mathematician. Attempt to REFUTE the note. Report BLOCKER / MAJOR / MINOR with exact sentences/gates attacked and concrete counterexamples or fixes. State survivals explicitly. Note: the block's two workhorse workers were Opus-family; you are the independent cross-family check — be maximally skeptical of anything they might have both gotten wrong the same way.

Files (read-only):
- docs/MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md
- scripts/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.py
- docs/MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md (the Duhamel chain consumed)
- docs/EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11.md (the reproducing no-go being dispositioned)
- docs/FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md (the landed pair instance)

Attack surfaces (do all, add your own):
1. The chain lemma and weight split: is sum diam >= d airtight for arbitrary connected supports? Any gap between ambient and intrinsic diameter? Does connectedness actually matter where claimed?
2. The peeling: is the |S|-weight bookkeeping exactly right — could the |S'| inside kappa fail to cover the contact-site multiplicity in some configuration? Is the start factor n_X^w <= |X| kappa right? Check the union-bound slack claims (12/11/10 on bonds).
3. The assembly: verify the 2-powers against the block03 unrolled form; the resummation; the k=1 and t=0 checks; the sharp vs coarse prefactor.
4. THE CENTRAL DISPOSITION: the claim that the exp-decay note's reproducing no-go (ratio >= R+1) does not bind this route. Attack it hard: is there any step where a convolution of pure-exponential weights is implicitly formed? If the disposition fails, the whole note fails.
5. The overlap honesty: does the note actually add over the exp-decay note's polynomial-weight LR bound and the free-bilinear note's W_mu bound, as it claims? Is the "arbitrary |S|" delta real (do the landed notes secretly cover it)? Is anything re-proved that is cited as landed, or vice versa?
6. The consistency reduction (kappa = 12 J e^mu; 6/5) and the instance closed forms (4r^2+2 spheres; kappa_3D = 4 J0 rho(3+rho^2)/(1-rho)^3; the bracket gates). Recompute independently.
7. The fermionic lift: does the graded lemma really cover long-range even terms with no new hypothesis? The odd-odd zeroth-term convention?
8. Scope hygiene: metric declaration, connected supports, set-indexing, d >= 1, directed time, no-dynamics, worker disclosure, non-claims completeness.
9. Runner: gate strength vs descriptions, manifest, needle fragility, vacuous or false-green gates.

House conventions: axioms supply no dynamics; bounded_theorem notes claim exactly what runners gate; literature comparator-only; N1-N8 with ATTEMPTED markers and Status line; presence needles are not correctness oracles.
