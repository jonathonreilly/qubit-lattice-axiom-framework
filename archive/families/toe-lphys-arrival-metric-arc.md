# Sub-campaign roll-up: the arrival-metric / emergent-isotropy arc (toe-lphys-20260812, 2026-08-17 band, ~#6706–#6792)

A single coherent search: a nearest-neighbour hop-cost on Z³ whose Dijkstra
first-arrival metric is less anisotropic than l¹. Rules: ν (support-drop),
ρ (equal-inward-weight), (0,1,1), μ (corridor-slide). Hosts B6–B24. Full-diff
read of every member (densify 2026-08-31). WARNING: in this band "reverse" =
the diamond/anisotropy-reversal bit and "face" = the face-diagonal comparator
— NOT the family (reverse,face) verdicts; never bin these as sweep rows.

## Load-bearing positives
- #6714: ν reverses the diamond where its own family provably could not
  (t(4,0,0)=10 vs t(2,2,2)=8; var 0.0059 vs l¹ 0.0135).
- #6765/#6770: roundness and reversal are DECOUPLED — exact identity
  t_ρ = 3|v|₂ on axis types makes ρ 7× rounder yet reversal-free.
- #6791/#6792: the 4-clause μ rule restores same-k reverse at k=7 AND keeps
  k=1 — the band's live route at close.

## Forcing negatives
- #6787: the asymptotic kill — t_axis ≈ k+6, t_body ≈ 3k+2, so the reversal
  MUST die at large k (3k² vs 9k²). Complements the arc-brief's Z³-relativity
  no-go: even engineered costs cannot sustain the light-cone reversal.
- #6786/#6788: same-k reverse dies at k=7 and stays dead; #6773/#6776 body
  reverse dies at k=3; #6769/#6774/#6785 face reverse dies at k≥5.
- #6736: reversal is not scale-invariant; #6732/#6768: isochrones never
  spheres, mixing GROWS with t — no continuum-isotropy recovery;
  #6742/#6754: roundness gain flips on two-seed geometry.
- #6706: the in-family derived no-go (N_rev=0 for all 27 cost triples).

## Resolved internal contradiction
#6757's "k=6 face reverse returns" is a ball-wall artifact — refuted on B16 by
#6769/#6772 (corridor site (12,−1,0) flips the bit); mechanism in #6771/#6783.

## Axioms-adjacent sub-thread
#6709/#6713/#6726/#6738: hop-cost as clock vs readiness filter on the 12
perp-mask hosts (ρ: 12 label / 4 filter, survivors exactly "+z occupied AND
−z empty") — touches Admissibility firing, not the arrival metric.

## Promotion candidates
#6787 (asymptotic no-go), #6714, #6765 (decoupling identity), #6791/#6792
(live μ route), #6706.

## Notes
Two wording nuances (#6728 "rounder" only among reversers; #6713 title vs
proved iff); manifest-base drift is a rebase artifact.


## Middle band (~#6793–#6865, fread_06) — the general law and the saturated ladder

Eight new rules (λ, φ, ε, ε2, β, ρ3 ridge-slide, ζ, π). Conclusions no single
PR states:
- **The whole band is two integers per rule**: t(k,0,0)=k+a, t(k,k,k)=3k+b for
  k≥6; reverse ⟺ 6k²+6(b−a)k+(b²−3a²)<0, k* ≈ 1.37·a. Predicts every wall in
  all 38 same-k Dijkstras exactly (ν k*=6.6, μ 12.1, ε/ρ3/ζ/π 13.2).
- **The no-go**: holding reverse to scale k needs axis penalty a ≈ 0.73k — a
  constant that must grow with k. A fixed finite clause set cannot do it.
  (#6787's kill confirmed independently across five rule families.)
- **Ladder saturated**: ν→μ moved the wall 7→13; μ→ρ3 13→14; ρ3→ζ zero.
  Reader-verified: ζ ≡ ρ3 ≡ π on every same-k pair — only THREE distinct
  metrics across the eight rules; ~21/44 PRs re-measure known metrics.
- **The k=1 bar is the discriminator** (both body hops must stay cost 1):
  kills λ (#6794) and ε (#6808); ρ3 survives via the +12/+4 witness-walk
  mechanism (#6816). Blanket 3→3 tax kills reverse (#6809); too-narrow
  clauses buy nothing (#6804 — φ returns μ's identical pair).
- **ρ3 repairs the face channel at k=6,7** (#6822) — overturning the earlier
  "face dies at k≥5" as a rule-CLASS statement — but its k=8 claim is a
  confirmed ball-wall artifact (reader re-ran R=18/20/24: 784<800 fails;
  unreconciled contradiction with #6832 one PR away; machine-asserted PASS on
  the artifact — same class as #6757).
- #6828 (axioms-adjacent promotion candidate): rho3-as-clock 12/12 vs
  readiness-filter 6/12 with a PROVED iff — the dying hosts are exactly the
  rule's own clause predicate. #6796: μ is a reverser AND strictly rounder
  than ν — qualifying the decoupling claim.
- All 44 manifest edits share one base — mutually exclusive as written.

Promotion candidates: #6816, #6817+#6833 (window k≤13, wall k=14), #6800
(closed form), #6809, #6804, #6828, #6796.
Defects: phrase-inversion PASS gates ("small-k-bar-not-killed" green on a
failed rule); false inequality literals written for substring gates; #6796
operator-precedence weak gate; #6830/#6835 lex-first artifact of a degenerate
tie. Integrity positive: AST scan found NO vacuous gates in this band; every
reported integer reproduced under the reader's independent recomputation.


## Late-middle band (~#6866–#6934, fread_07) — the two-law reduction

Thirteen rules across eleven clause families, reduced by the reader (verified
by re-running the diffs' own cost functions on B60) to TWO exact laws:
- t(k,k,k) = 3k+4, INVARIANT under all thirteen rules — nothing touches the
  body diagonal;
- t(m,0,0) = min(3m, m+C), C=12 (ρ3-family) or C=16 (out-face family).
Every clause only raises C; none changes the slope. Hence the sharpened kill:
**reversal survives large k only if the axis slope exceeds s_body/√3 ≈ 1.73,
and every rule keeps slope 1.** The celebrated "restore at k=14" (#6930/#6933)
is a wall relocation 14 → 19, never probed (the band stops at k=16).
Face and same-k reverse TRADE: out-face buys +5 on the same-k wall, pays −2 on
the face wall — no member notices. Six of thirteen rules are "live but idle"
(priced hops no geodesic uses; three sitewise identities re-checked on B30).
The 12/6 clock-vs-filter split is invariant with its exact iff-law living
only in #6874's checker: the filter fires at v iff v does NOT have exactly two
unit coordinates.

Promotion candidates: #6930 (df restores k=14 AND proves df ≡ ω), #6933 (the
C=16 law pinned to k=16 on B48), #6871 (the WALL_ROWS table making the wall
closed-form), #6874 (Admissibility-firing iff), #6902+#6924 (mid-leave clause
provably empty), #6890 (exact idle-clause theorem), #6898/#6906/#6926
(two-seed variance never survives), #6915/#6927 (shells stay mixed under
every rule).

Defects: THREE more ball-wall artifacts asserted as results (#6873, #6912,
#6922 — reader recomputed on B60 and flipped all three; the notes observe the
boundary mechanism and count the bit anyway; recurring class); FOUR fake
mutation gates (#6872/#6895/#6911/#6921 — counterfactual labels over verbatim
restatements, no mutant ever run); THREE dangling premises (#6925 string-
matches its own claimed sentence as a check); three PRs shipped on a provably
empty rule.

## Terminal phase (~#6935–#7033, fread_08) — the program closes itself

The successor rule ρ3 + a two-parameter out-face grow-tax search (floor
m∈{1..4,none} × price c∈{2,3}) + shape variants (ψ, s2), scored on four
comparators. Conclusions no single PR states:
- **Floor and price are invisible in the same-k pair**: nine named rules, ten
  ~102k-site Dijkstras, one identical number pair (30, 46).
- **The complete affine law**: all rules have LOCKED SLOPES (1,3); only
  intercepts move — ρ3 (12,4) k*≈13.2; every out-face variant AND ψ (16,4)
  k*≈18.7; s2 (14,3) k*≈16.8 (the only second intercept move makes the wall
  EARLIER).
- **#7009 (band terminal, promotion candidate): the exact locked-slope
  obstruction** — leading coefficient −6 independent of intercepts, so no
  intercept-only clause restores all-k reversal. #6787's asymptotic kill
  upgraded to an exact theorem.
- **The face comparator alone resolves the floor** (#6969 unique clean k=1..8
  table; #6971 walls it at k=19; #7009 proves it must).
- **The axiom-native object never had the target properties**: unit-l¹
  lock-support fails reverse (#7010: 3<9), fails face (#7012: 4<8), is LESS
  round than the engineered rule (#7013), and native formation-tick gives
  both bits FALSE (#7017) — "occupancy t is not the Record-side cone."
- **The one surviving positive route**: #7024's LOCK-based formation rule
  (not a hop-cost) gets both bits at k=1 and evades #7009's obstruction —
  but note its host-name collision (B_3(0) Euclidean 123 sites vs the
  family's l¹ 25 sites, unflagged).
- #7033: clock ambiguity (perpnn ticks class the axis event timelike; recint
  classes it null).

## Additional defects (methodology dossier)
44/44 cache-write contradictions (cleanest instance of the class);
#6974/#6982 false-green "not-leftover" checks passing by grepping their own
prose while both computations are bit-identical to ρ3; systemic
non-duplication certified by provably-unused hops; #7025 hijacks the
comparator names for a vacuous lettering count; #7014's affine check is
hard-coded arithmetic, and two of its rows are computed by no PR; #6966/76/84
report a vacuous singleton-variance statistic three times.
