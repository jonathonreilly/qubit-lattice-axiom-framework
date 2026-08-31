# Sub-campaign roll-up: six readout generations (toe-lphys-20260812, #7188–#7250)

> Record-only roll-up: statements aggregate what the member PRs' notes and
> runners reported and, where marked, what the consolidation reader's
> recomputation observed. Nothing here is a repo claim or promotion;
> theorem-grade wording is the archived work's own, quoted. See
> `archive/README.md`.


Six readout generations (S⁺ union-own-lock, own incoming M, own outgoing O,
two-tick composition, Cl(3,0) plaquette, neighbour-read R) over the fixed
perp-step process. Reader recomputed 31/44 cells number-for-number (all
matching) plus five sweeps (648-cell, 108-config, 26,064-site,
46,656-plaquette, B3–B5).

## Conclusions no single PR states
- **Sign-blindness theorem** (108/108): the process sees only the lock AXIS,
  never its sign → three byte-identical PR pairs titled as independent
  results; "same-lock vs opposite" cells on one axis are the same computation
  unless the flipped seed is a probe/probe-neighbour.
- **The union-own-lock generation is a rename in 11/14 cells** (S⁺==S except
  where A is a seed) — certified by a phrase-inversion `not-leftover` gate
  that PASSES on the numerical identity it claims to exclude.
- **THE PINCER ON THE RECORD CLAUSE** (with f09's #7048/#7058 this is the
  third independent negative on the readout route): (i) reverse is a
  NEIGHBOURHOOD property — own-incoming M fails everywhere S⁺ holds unless
  the probe is a seed (#7205 et al.); (ii) the own record is NOT recoverable
  from neighbours (#7244: R≠M at all four probes). Neither direction
  reproduces the other.
- **M-composition HOLD is a tautology** (M frozen at formation; 26,064
  site-instances, zero exceptions); **O-composition failure is forced**
  (O(τ0) empty at 3 of 4 probes in 648/648 cells); **S⁺-composition HOLD is
  a genuine minority result** (243/648 = 37.5%; the band never shows a
  failing case).
- **Plaquette holonomy, corrected in the useful direction**: #7206's own
  process contains 28 fully-locked unit plaquettes, ALL with palindrome
  words and scalar +1 — trivial holonomy; the published UNDEFINED is a
  probe-anchoring artifact (probes are exactly the multiply-reachable
  sites). Band-wide: 7.4% of plaquettes definable; scalar ±1 in 56%,
  BIVECTOR-valued in 44% (the "hold iff scalar" test ill-posed there).
  RECONCILES f11's #7151/#7155 no-go: that result is about probe-anchored
  cycles under the M2(C)-letter product, not about the field's holonomy.

## Promotion candidates
#7205 (the separation result), #7244 (locality no-go), #7197+#7201 (the
exact axis-confinement obstruction), #7243 (outgoing readouts can never be
formation-time readouts), #7189 (the hold-CHANNEL classifier — the band's one
new instrument), #7212/#7216 (the real composition positives), #7245 (the
sharpest bit-misreading counterexample).

## Disputes and defects
- **FOUR PUBLISHED VERDICTS DISPUTED** (#7234, #7235, #7237, #7247):
  own-tick O-readout HOLD/HOLDs whose own convention forces
  UNDEFINED/UNDEFINED — the printed sets are t+1; their siblings on identical
  cells print O(τ0)={} explicitly. All four sit in the family HOLD table with
  timing "?" — annotated there as disputed.
- 44/44 green gate certifying a false sentence (cache files shipped while
  "no cache is written" PASSes); flat provenance (upstream_dependencies:
  [minimal_axioms] only) breaks the real citation stack; 29.6% of 2,677
  checks are prose greps; six duplicate groups covering 13 members.
