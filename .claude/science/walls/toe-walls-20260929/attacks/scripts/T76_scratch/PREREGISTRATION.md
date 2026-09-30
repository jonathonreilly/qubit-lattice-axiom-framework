# T76 pre-registration (written BEFORE any script was run)

Author: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family check).
Date: 2026-09-29.

## Question under test
Wall T76 (L15-W8 / L01-W13): "with the simple count-threshold formation rules the number of
possible frozen boxes is either one or grows with volume" (probe 19, PR #9363, sol round 5),
plus the unanalysed rule E (2D, A = {0,2,3,4}, N = 1,7,13,27 for L = 2..5).
Sharp version of what I test: is the dichotomy {one state} OR {volume law} COMPLETE over ALL
count-threshold rules A subset {0..2d} (d = 2, 3), and if a rule escapes, does its exact flat
count scale like the boundary?

Rule (same as probe 19): sealed L^d box, outside counts as unrecorded, one record per site,
permanent; empty site may form iff its number k of recorded neighbours is in A; frozen = no
empty site has k in A; N = number of distinct frozen occupation sets reachable from the empty
box (flat count).

## Test T76-A: sealed-gadget classification of every count-threshold rule
A "sealed gadget" is a window W (a box a x b (x c) of sites) with two distinct occupation
patterns P1 != P2 such that each Pi (i) is peelable inside W with the outside empty
(there is an order of adding its sites, each having k in A when added), and (ii) is sealed:
every empty site v of W has k_in(v) + j not in A for every j = 0..o(v), o(v) = number of
lattice neighbours of v outside W.  Lemma (suggested, proof skeleton in the report): if a
gadget with g >= 2 patterns exists then N_L >= g^(floor((L+1)/(b+1))^d), a volume law, exactly
as in the probe's block lemma C but for arbitrary A.
- Windows: 2D all a x b with a,b <= 5; 3D all a x b x c with a*b*c <= 18, plus 3x3x3 for
  rules still unresolved.
- Sanity: for the crowding rules A = {0..m} the search must find a gadget for every
  m <= 2d-1 (probe's lemma C) and none for upward-closed rules.

PASS-A (the dichotomy fails; route "boundary-rigid rules" lives): some rule with 0 in A and A
not upward-closed has NO gadget in the window range.
FAIL-A (the dichotomy is complete on the searched windows): every rule with 0 in A is either
upward-closed (one state) or has a gadget (volume law).

## Test T76-B: exact flat counts for the gadget-free rules (if any), extended past L = 5
Exact count of frozen states by row/layer dynamic programming (frozen only), and of REACHABLE
frozen states by explicit enumeration + reverse-peeling search, for L up to as large as
feasible (target: 2D L <= 12, 3D L <= 5).  First reproduce the probe's pinned counts
(2D m=0: 2,10,42,358; rule E: 1,7,13,27) with my own code.
Reading rules (fixed now):
- BOUNDARY-LAW-LIKE if ln N(L)/L^(d-1) is within +-25% of its L_max value over the last three
  sizes AND ln N(L)/L^d decreases monotonically over the last three sizes.
- VOLUME-LIKE if ln N(L)/L^d is non-decreasing or within +-10% over the last three sizes.
- Finite fits never prove scaling (sol round 1 on probe 19).  A boundary law counts as
  PASS-B-STRONG only with an upper-bound argument ln N <= C L^(d-1); a fit alone is
  PASS-B-WEAK (suggestive).

## What each outcome would change
- PASS-A + PASS-B-STRONG: the wall's plain sentence ("one or volume") is false, and a
  supplied count-threshold rule with boundary-scaled flat count exists (in that d).  Wall moves
  from "no rule found" to "rule found, coefficient and 3D scaling still open".
- PASS-A only: dichotomy fails on the searched windows but growth unknown -> wall unchanged
  except the sentence is corrected.
- FAIL-A: the dichotomy is proved complete for count-threshold rules on the searched windows;
  the wall sharpens to "an area law needs a rule outside the count-threshold class".
