# Sub-campaign roll-up: the exist-opposite window sweep (toe-lphys-20260812, #7142–#7187)

One predicate over a 2-knob readout family (time window × own-letter flag),
10 seeds × 3 frames. Reader re-implemented everything: 38/38 verdict pairs
reproduced; 180-cell grid computed; zero monotonicity violations.

## Conclusions no single PR states
- **A monotone verdict lattice governs the band**: both knobs only enlarge S,
  the predicate is monotone, so verdicts only climb UNDEFINED ≺ fails ≺ HOLD.
  The 17 reverse-HOLDs and 31 face-HOLDs are ONE lemma plus one onset number
  per cell — and at the widest readout 17/18 cells saturate to HOLD/HOLD, so
  later-tick HOLDs mean only "T is past the onset". Onsets computed by the
  reader for every cell (only #7148 measured one).
- **The unique non-saturating cell (#7147)**: perpnn-x — the 1-seed cone is
  all-positive, so reverse fails at the MAXIMAL readout. The band's only
  obstruction surviving every widening, exactly characterised.
- **The exact own-letter HOLD law** (assembled from five members): reverse
  holds through the own channel iff −L(A) ∈ S⁺(B) — NOT "iff seed letters
  are opposite" (#7160 opposite fails; #7181/#7187 identical hold).
- **Plaquette-holonomy no-go (#7151/#7155)**: H is UNDEFINED on the nsopp
  process (three earliest incoming steps at two corners) — an obstruction to
  reading the lock field as a Z³-valued gauge connection, robust to the
  deadline convention.
- **#7163 — the band's only Qubit-axiom contact**: occupancy kernel as Bloch
  vector, H=3n·σ, Tr(ρP+)=2/3, Tr(ρP−)=1/3 at k=1 (ρ posited, not derived).
  Born-adjacent; feeds the selector obligation with that scope caveat.

## Promotion candidates
#7147, #7148 (the T-scan superseding ~20 siblings), #7151+#7155, #7163,
#7150/#7159 (the channel-isolating controlled pair), #7167.

## Defects
- Vacuous HOLDs #7161/#7162: the readout's fail branch is UNREACHABLE
  (verified); headline HOLD/HOLD carries one bit (n≠0); the same data on
  #7163's honest scale reads "some".
- **Name overload hazard**: #7147's runner also computes tick-inequality
  "reverse/face" (both hold) on the same probes where lock-vector reverse
  FAILS — two unrelated predicates share the campaign vocabulary; any
  cross-family (reverse,face) table conflates them unless the readout is
  qualified. (Feeds the family-table caveat.)
- Definitional non-uniformity: MISSING vs NONUNIQUE bookkeeping alone moves
  a verdict; five admitted no-op members. No stubs; arithmetic all confirmed.
