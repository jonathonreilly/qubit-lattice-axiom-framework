# Sub-campaign roll-up: the chirality/light-cone arc (toe-lphys-20260812, ~#6623–#6704)

> Record-only roll-up: statements aggregate what the member PRs' notes and
> runners reported and, where marked, what the consolidation reader's
> recomputation observed. Nothing here is a repo claim or promotion;
> theorem-grade wording is the archived work's own, quoted. See
> `archive/README.md`.


One continuous 39-PR argument plus a 5-PR F_cut selector census; written from a
full-diff read of every member (densify 2026-08-31). No (reverse,face) verdicts
exist in this band — the earlier family roll-up must not count these members.

## Arc A — F_cut selector census (#6623–#6628)
All 32 cube-covariant cut maps scored at k=3..11: cov_k>0 never EQUALS
Q8 = wt1∨adj2∨opp2∨vertex3, but positivity always implies it; on the Q6-false
subclass cov9>0 ⟺ opp2∧mixed3 exactly (unique positive (0,1,0,0,1)).

## Arc B — light cone and chirality on the seed-grown front
- Minkowski forcing negatives: every cube-covariant 6-NN hop cost is CONSTANT
  (#6631; single G+ orbit) forcing t = w0·|v|_1 — extended to all 1024
  occupancy-dependent (#6684) and all 256 two-end costs (#6692).
- THEN THE BREAK (#6701): a local-in-weights rule (cost 3 iff equal inward
  weight or seed-exit) DOES reverse the diamond on B4 — the no-go was an
  artifact of the {1,2} cost alphabet. Reversal does not survive to B6, but
  isotropy variance drops ~20-30x below l^1 (#6702: 0.00068 vs 0.01350; #6704).
- Chirality chain: alphabet derived from the axioms (M2(C) => k=3 exactly,
  #6637); the July-3 chiral pair has empty support on any seed-grown front
  (#6636/#6639, true requirement = 4 occupied neighbours); radius-2 stars can
  present 4 (#6640) and the pair fires (#6645); but over all 15 weight-4 masks
  N_stab_ok = 0 — NO NN-determined G+-equivariant chiral labeling exists on
  any 4-occupied star (#6668); lock-ticks are no repair across all 763,608
  equal-radius three-ball stars (#6671); the escape is UNEQUAL RADII, reduced
  to exactly ONE age bit (#6675/#6681), fired by a canonical orientation
  section on all 12 masks (#6690) — and priced: the bit is NOT recoverable
  from occupancy (k=t on only 27 of 2000 stars, #6682).

## Promotion candidates
#6668 (the chiral-labeling no-go), #6682 (the age-bit price), #6701 (the
alphabet-artifact break), #6702/#6704 (isotropy-variance drop), #6631 (constant
hop-cost theorem), #6637 (alphabet from axioms).

## Defects for the owner's attention
- #6632: BROKEN CHECKER — runner implements Hamming-nonzero (63 formers), the
  exact predicate #6630 proves is NOT f_L1 (56); the check passes by grepping
  prose strings that the implemented function contradicts; corrupted text
  substitutions in the note.
- #6642/#6643 generalize from the lex-first witness; #6644 refutes (2 of 4
  sites admit unique-axis agreement).
- #6636/#6637 say "six occupied neighbours"; the true count is four (#6639).
- #6675's "24/24 covariant" is a set-membership tautology (|Stab|=1).
- #6667 near-vacuous: gates a search that never executes (search_ran=False).
