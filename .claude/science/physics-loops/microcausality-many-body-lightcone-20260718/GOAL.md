# Goal — microcausality many-body lightcone lane (block01 anchor, 2026-07-18)

Target: the named open task of the landed microcausality surface.
V1 quote (from
`GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`,
its N2/N3 gate): "The `U`-integrated, many-body, and sharp-rate problems
are separate open tasks, not walls claimed here." This block takes the
**many-body** slice at bounded level. Prior-art verified 2026-07-18: the
2026-05-09 `MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE`
is one-particle/free-sector (and falsified `H = -log(T)/a_tau` on the
free bilinear two-step sector); no repo note carries a many-body
commutator lightcone; no open PR collides (checked).

Block01 theorem set (all bridge-conditional on a SUPPLIED finite-range
Hamiltonian class — the axiom memo's "Admissibility is not a dynamics
axiom ... It does not choose a Hamiltonian" sentence is the honesty
needle; no physical velocity claim; kinetic-isotropy primitive NOT used):

- L1 (support growth, exact): for supplied nearest-neighbor bond
  Hamiltonians H = sum_b h_b on the qubit lattice, supp(ad_H A) is
  contained in the 1-neighborhood of supp A ([h_b, A] = 0 for bonds not
  touching supp A). General finite-algebra proof note-carried;
  instance-gated.
- T1 (below-cone Taylor vanishing, exact): iterating L1,
  supp(ad_H^k A) is within the k-neighborhood, so for graph distance
  d(X, Y) > k every Taylor coefficient of [A_X(t), B_Y] at t = 0 through
  order k vanishes identically — the commutator vanishes to order
  d(X,Y). PRE-VERIFIED exactly on the 3-site chain: H = X1X2 + Z2Z3,
  A = Z1, B = X3: k = 0, 1 commutators zero, k = 2 (= d) nonzero.
- T2 (upper-bound-not-equality exhibit, exact): for the commuting chain
  H = X1X2 + X2X3 the cone is NEVER reached (k = 2, 3 still zero —
  pre-verified): site-2 factors commute, propagation stalls. So T1's
  vanishing is universal while cone-saturation is Hamiltonian-dependent
  — an honest two-sided pair, no genericity claim.
- T3 (LR-form series bound, bounded): ||[A_X(t), B_Y]|| bounded by
  2||A||||B|| sum_{k >= d} (c_k t^k / k!) with c_k from local bond-norm
  and neighborhood-count bounds (coarse, exact); tail domination by the
  exact inequality sum_{k>=d} x^k/k! <= (x^d/d!) e^x (proof:
  d!/k! <= 1/(k-d)! iff binomial(k,d) >= 1 — pre-verified). Velocity is
  class-relative bookkeeping, not a physical c; sharp-rate stays the
  named open task per the CT note.

Runner design (~16 gates, supervisor-authored per the demotion-era
discipline): the two 3-site exhibit families (8x8 exact); far-bond
commutation; ad-support gates; the factorial-domination formal gate; a
commutator-norm instance; needles (CT open-task sentence; the axiom
no-dynamics sentences; the 2026-05-09 note's one-particle scoping line;
own claim_id/labels). Mutations: one per family (flip a bond to touching;
perturb the binomial bound; swap the generic/commuting Hamiltonians —
the swapped generic-exhibit gate must fail; needle perturbation).

Lessons standing (from this session's five review rounds): quantifier
placement stated per theorem; codomains declared; axiom sentences
quantify over realized objects — T1 here is pure operator algebra on the
supplied class, no axiom-lift is attempted; "upper bound, not equality"
stated via the T2 exhibit rather than rhetoric. New lane, new family:
PR #1, no cluster cap. Same landing discipline: quote audit both
directions, mutation battery, SHA-pinned cache, one combined adversarial
lens, pipeline with origin/main-relative restore + manifest staging,
stacked-nothing (base main).
