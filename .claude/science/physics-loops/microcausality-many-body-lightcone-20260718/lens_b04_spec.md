# Combined adversarial lens — block04 (fermionic even-CAR walk-expansion LR bound)

Role: hostile referee + independent mathematician. Attempt to REFUTE the
note before it ships. Report format: BLOCKER / MAJOR / MINOR, each with
the exact sentence or gate attacked and a concrete counterexample or
fix. If a claim survives, say so explicitly.

Files (read-only):
- docs/MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md
- scripts/microcausality_fermionic_even_car_walk_expansion_2026_07_18.py
- docs/MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md (sibling chain being carried over)
- docs/MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md (family class)

Specific attack surfaces (do all, add your own):
1. The graded lemma L-F: is the sign count (-1)^{p*q} right? Is "even commutes with ANY disjoint element" correctly proven and gated (not just even-even)? Does bilinearity extend from monomials correctly?
2. The chain carry-over claim: identify EVERY step of the sibling chain that uses tensor-factor structure rather than only disjoint-commutation, and check L-F actually substitutes. In particular: the boundary reduction, the self-drop, the base-term vanishing, the norm-transport lemma (any hidden tensor assumptions?), unitary invariance, walk combinatorics.
3. The general-parity theorem: the zeroth term ||[A,B]||. Is the displayed bound correct for odd-odd pairs (t = 0 consistency)? Is the claim "||[A,B]|| = 0 whenever A or B is even" exactly L-F? Is anything claimed for odd-odd pairs that the chain does not deliver?
4. The JW representation: is the faithfulness/computational-device framing honest? Do any gates secretly depend on the JW ORDER chosen? The string exhibit: does it prove what the note says (image not supported on the two qubit factors)?
5. n_X, walks, reach, coefficient identity: unchanged Z^3 geometry — is the citation-vs-regate split between this note and the sibling honest and complete per the repo's rebuild directive?
6. Scope hygiene: supplied vs derived (CAR algebra, evenness, no carrier claim); "bridge" naming (two halves, half ii not attempted); non-claims completeness; any sentence that could overclaim spin-statistics, superselection, or physicality.
7. Runner: vacuous gates, instance-vs-universal honesty, is_positive/None hazards, needle fragility, anything false-green.
8. The d >= 1 inheritance: is the sibling's d = 0 exclusion correctly propagated (the fermionic zeroth-term form changes the shape of the necessity argument — does the note handle that honestly)?

House conventions: axioms supply no dynamics and no fermionic carrier; bounded_theorem notes claim exactly what runners gate; literature comparator-only; no new vocabulary; N1-N8 with ATTEMPTED markers and Status line.
