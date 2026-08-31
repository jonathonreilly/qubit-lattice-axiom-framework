# Sub-campaign roll-up: the two-axis-seed frontier (toe-lphys-20260812, #7296–#7385)

The nm2* two-axis grid (2 seeds × 3 frames × 6 readouts) + the five split-
introduction PRs. Reader reimplemented the process; all 44 reproduced exactly.

## Conclusions no single PR states
- **split ≡ cover on the whole two-axis family** (|Axis(M)|=1 at all 24
  probe-instances): five bit-identical twin pairs, one member explicitly
  denying an identity it instantiates. Six readouts collapse to three verdict
  columns (+ constant O-read). The COMPLETE 6-cell anisotropy table is
  assembled here for the first time; the seed sign is invisible except on z.
- **Global freeze lemma** (stronger than any PR states): M never changes;
  O relaxes exactly one tick then freezes forever — verified at every formed
  site for every seed. All composition HOLDs tautological (one steelman
  concedes it).
- **The one dissenting cell is a seed-letter phantom**: the same-lock
  convention injects the partner's letter into O with no formation event
  behind it; removing that single phantom makes the cell identical to its
  opposite-seed twin. (#7360/#7383 name the mechanism; neither concludes.)
- **The chirality probe produces no chirality**: Orient = sgn(m)·ε(axis(m)) —
  a fixed function of the incoming letter, zero information about O
  (consistent with the arc's odd-d chirality = {0}).
- **A clean locality asymmetry**: M is neighbour-readable (20/24 probes,
  60-64/119 sites); O is not (4/24; fail/fail in all six cells).

## Promotion candidates
#7300 (split strictly finer than cover — flips the reverse bit), #7298
(axis-cover is NOT a law), #7299 (three-way predicate independence), #7307
(one seed, three frames, three verdicts), #7361 (the chirality no-go), #7362
(terminal freeze statement), #7360+#7383 (the phantom mechanism).

## Defects (two genuine, one structural)
- **#7357: provenance defect at 65/65 green** — a copy-note describing the
  WRONG experiment (opposite-seed metadata, seed paragraph, obligation table
  and N8 all contradict its own Theorem 2); nothing tests metadata or
  obligation tables; prose-greps pin ~6 sentences.
- **#7297: or-precedence false green** — a 17-term AND (including the
  headline verdicts) never evaluated because a 3-term right disjunct is true.
- Band-wide: ~1/3 of checks are prose greps; template drift in 3 members.

## Second half (#7386–#7429, fread_15) — the observable-status verdict

Reader reimplemented the model; all 44 reproduced exactly. Conclusions no
single PR states:
- **No orientation readout in the band is a lattice observable.** M, O and
  ticks are exactly equivariant under the 24 proper rotations the axioms
  supply; all four Orient conventions are not (their tie-breaks reference the
  fixed frame e1<e2<e3). **Rotating one identical configuration realizes all
  four verdict pairs (hold,hold)...(fail,fail).** The only invariant
  convention (#7425) never produces a sign. An elementary lattice-level form
  of the "odd-d chirality = {0}" wall — the sharpest statement of the
  chirality no-go across these bands.
- **The freeze law is one theorem, 22 members** (M and O exactly constant for
  τ ≥ t+1; 718 site-readouts, 0 violations) — every τ-sweep past t+1 is
  provably vacuous; kills the clock line for this cell family.
- **The seed contrast reduces to the fictitious-parent artifact**: 26/26
  separating witnesses for sim ≠ forall-perp in a 1,500-config random search
  are that convention; with it excluded the two predicates coincide over
  5,659 readouts.
- **The honest locality number**: joint signed (M,O) is neighbour-recoverable
  at 3–7% of sites (signed M 50–54%, signed O 21–23%, unsigned axes ~33%) —
  the four-probe "fails at every probe" is a sample of a 93–97% host-wide
  failure.

Promotion candidates (added): #7419/#7428 (joint-nonrecoverability), the
#7393/#7425/#7427 orientation triad + #7426, #7402/#7408 (the only members
that PROVE the freeze), #7395 (the one tick where anything changes), #7386
(widest cross-readout table).

Defects (added): ACTIVE false green — 26/44 runners' axis_cover lacks an
empty-set guard and returns "hold" at 348 realized site-readouts on this very
host (guarded members correctly fail; no shipped headline hit, but any
off-probe sweep is exposed); contradictory empty-set semantics for
`simultaneous` across members (fail vs UNDEFINED, propagating differently);
fake mutation gates (assert alternative readouts on unmutated data);
neighbor-read 4/4 HOLD headline is a 4-site draw from a ~50% distribution.
