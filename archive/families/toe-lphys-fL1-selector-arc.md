# Sub-campaign roll-up: the f_L1 selector arc (toe-lphys-20260812, PRs ~#6391–#6474)

> Record-only roll-up: statements aggregate what the member PRs' notes and
> runners reported and, where marked, what the consolidation reader's
> recomputation observed. Nothing here is a repo claim or promotion;
> theorem-grade wording is the archived work's own, quoted. See
> `archive/README.md`.


44-PR research arc on the twelve-vertex two-cube {0,1,2}x{0,1}x{0,1}
(off-patch occupancy 0), asking: does anything select the L1 formation
predicate f_L1 (fire iff some axis is unbalanced)? Written from a full-diff
read of every member (densify 2026-08-31); no single PR states the arc's
conclusion.

## What the members' runners jointly reported (a forcing negative no member states; assembled here)
Three independent selectors were run; NONE picks f_L1:
1. Sparsity picks f_min (support 26 vs f_L1's 56) — and f_min lies OUTSIDE
   F_cut (breaks complement-even). Inside F_cut the sparsest is (1,0,1,0,0)
   at 36, also not L1. (#6400, #6407, #6414)
2. Two-site coverage maximizers are (1,1,1,1,0)/(1,1,1,1,1), both with
   opp2=1 — the exact negation of the balanced-axis-silence motivation for
   L1. (#6431, #6433)
3. Coverage-uniqueness across every seed size is unique only at k=4,6,8 and
   the winner is always f1=(1,1,1,1,1), never L1 — margins 920:924, 494:495.
   Terminal: #6465.
The one PR claiming positive selection of L1 (#6404) is circular by its own
N7 section. Also forcing: #6394/#6398 — under blank-block, N_fill=0 for all
1024 covariant maps; the o=0 vacuum default is REQUIRED and Record does not
supply it.

## Strongest members (promotion candidates)
#6465 (terminal negative), #6407 (f_min closed form; sparsity vs
complement-even select disjoint candidates), #6394/#6398 (vacuum-default
requirement), #6417 (first f_min/f_L1 separator census), #6410 (F_cut fillers
= the subcube (wt1,adj2)=(1,1)), #6426 (lock-count history is not a complete
invariant).

## Defects for the owner's attention (found in the full read)
- Notation collision: (1,0,1,1,0) names two different maps (support 44 inside
  F_cut; support 26 = f_min outside). #6414 prints both adjacently; #6407 and
  #6411 use the name unguarded.
- Mid-series correction never flagged: early notes say f_min/f_L1 "differ on
  mixed3"; they differ on wt5, adj4 AND mixed3 (30 cells). #6417/#6420 fix it
  silently.
- Boundary artifact: every discriminating neighbourhood contains off-patch
  zeros; #6421's stuck corner is manufactured by the o=0 convention (its own
  N7 raises this, unanswered).
- 38 of 44 commit runner-cache files while declaring cache_write: false; in
  #6400 a check named no-cache-write PASSES inside a diff adding the cache.
- #6397's n_mu formula inconsistent with the series definition (harmless).
