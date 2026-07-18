# Combined adversarial lens — block03 (all-time volume-uniform walk-expansion LR bound)

Role: hostile referee + independent mathematician. Attempt to REFUTE the
note before it ships. Report format: BLOCKER / MAJOR / MINOR items, each
with the exact sentence or gate attacked and a concrete counterexample or
fix. If a claim survives, say so explicitly.

Files (read-only):
- docs/MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md
- scripts/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.py
- docs/MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md (sibling 1, hypotheses class)
- docs/MICROCAUSALITY_VOLUME_UNIFORM_SEQUENCE_COUNT_COEFFICIENT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-07-18.md (sibling 2, named open task)

Specific attack surfaces (do all, add your own):
1. The Duhamel derivation in G1: is f'(t) = i[H~(t), f(t)] - i Σ_b [τ_t(A), [τ_t(h_b), B]] with H~(t) = Σ_{b∩X≠∅} τ_t(h_b) EXACTLY right? Check the per-term Jacobi bookkeeping, the sign conventions, and whether the reduction [H, A] = [H_∂X, A] is applied before or after conjugation consistently.
2. G2: does the norm-transport lemma require anything not declared (self-adjointness of H~(t), differentiability, propagator existence)? Is the W-encoding of the adjoint legitimate (W' = -iWH~ presumes H~ Hermitian — declared?).
3. The iteration step: when A → h_b, the sum must run over b' adjacent to b EXCLUDING b itself. Verify the self-drop is used where claimed and NOT smuggled at the first step (where A is generic and no self-drop exists).
4. Walk bookkeeping: length-k walk = k bonds = k-1 adjacency steps. Check every count (6, 10, 60, 100), the reach lemma k >= d, the transfer from Z^3 to induced E(Λ), and whether n_X should count bonds of E(Λ) or E(Z^3).
5. The assembled series: index start k = d, the (2J)^{k-1} vs (2J)^k bookkeeping (first step has 2||A||, base has 2J||B||), the coefficient identity, and the remainder ρ_K → 0 argument.
6. The tail bound and the large-d certificate arithmetic (3^200·200^800/800! < 10^-40 with e < 3 — check the exponent bookkeeping independently).
7. G7 exhibits: are the sibling comparisons stated fairly (no strawman, no contradiction of their actual claims)?
8. Scope hygiene: any sentence that overclaims (sharpness, physical velocity, dynamics selection, audit verdicts)? Any needle that could go stale?
9. Runner: any gate that is weaker than the note text it certifies (vacuous probes, instance-only gates presented as general)? Any is_positive/is_nonnegative usage that could silently return None and pass?

House conventions that bind this note: axioms supply no dynamics; H is supplied; bounded_theorem notes claim exactly what runners gate; literature is comparator-only; no new vocabulary.
