---
claim_id: history_actuality_reproduces_the_readable_born_odds_and_which_way_complementarity_but_needs_a_tick_form_the_chiral_weighting_lacks_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Candidate replacement (a supplied proposal with zero premise weight, not adopted) of CL-2's per-half-tick actuality by history actuality: one actual history drawn from the history weighting, a record being the class of a site-local history partition whose decoherence functional D(a,b) = Tr(C_a rho C_b^+) vanishes for a != b (Gell-Mann-Hartle / Griffiths, supplied), selected by least history entropy. Exact on toys (qubit walk on a 4-site ring with a pointer register; two- and three-qubit which-way models): single-time partitions always decohere with D(a,a) = Born; pointer-recorded multi-time partitions decohere exactly and D(a,a) equals CL-2's readable (pointer, mode) joint; the unrecorded fine two-time mode partition of the supplied walk does not decohere, and CL-2's transport joint differs from D(a,a) (TV 0.25) but is unreadable under the read-once clause; which-way |D(L o, R o)| = |<p0|p1>|/4 and visibility V = |<p0|p1>|; readers of one pointer agree with weight-0 disagreeing classes, a record carries exactly H(outcome); after a coherent un-copy of the pointer the specified refinements with a final port projection do not decohere (|D| = 1/4), while the coarser path-only partition, and the path/pointer partition extended by the un-copy without a further projection, still decohere (common-unitary invariance), so the record is not lost in every set; with a two-boundary functional the arrow is the boundary (pure ready pointers at the start give records of the past only, at the end records of the future only); a two-site record (Bell) leaves a continuous U x U* family at least surprise, a three-site redundant record (GHZ) fixes the Z basis. Finite diagnostics (2D U(1) overlap, 4x4 and 6x6, antiperiodic tick): vector-like det(1+V) >= 0; the 3-4-5-0 chiral weight (a supplied candidate weighting, not adopted) in the Narayanan-Neuberger Wigner-Brillouin convention has a small nonzero phase (<= 1.1e-4 at link noise 0.03), its gauge variation is 7x to 610x below a lone charge-5 Weyl's, and the Q = 1 sector has unbalanced zero modes (7 L, 5 R). Not constructed here: a decoherence functional for the chiral weighting (the construction used needs a tick/transfer-matrix form, which this note does not have); not shown: any prediction differing from CL-2's readable statistics, interacting or 3+1D content."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_bounded_theorem_note_2026-10-23
  - admissibility_record_continuation_refinement_conditional_bounded_theorem_note_2026-07-13
runner: scripts/history_actuality_reproduces_the_readable_born_odds_and_which_way_complementarity_but_needs_a_tick_form_the_chiral_weighting_lacks_2026_10_23.py
---

# History actuality reproduces the readable Born odds and which-way complementarity, but needs a tick form the chiral weighting lacks

Claim type: bounded_theorem (exact identities on finite toys plus labelled finite diagnostics; the consistent-histories
rule and lattice-chiral conventions are supplied and cited).
Runner: [scripts/history_actuality_reproduces_the_readable_born_odds_and_which_way_complementarity_but_needs_a_tick_form_the_chiral_weighting_lacks_2026_10_23.py](../scripts/history_actuality_reproduces_the_readable_born_odds_and_which_way_complementarity_but_needs_a_tick_form_the_chiral_weighting_lacks_2026_10_23.py), TOTAL: PASS=23 FAIL=0, about 4 s, about 80 MB peak, about 4.8 k characters of stdout. It exits nonzero on any failed check.
Axioms unchanged; no candidate-law edit.

## Question

CL-2 picks one actual configuration per half-tick by a tick-wise transport, while the candidate chiral matter
weighting supplied by other campaign notes (labelled CL-1 there, a history-level matter weighting; zero premise weight,
not adopted) is over whole space x tick histories, with no tick form known to those notes.
Owner idea (2026-10-23): if matter is weighted over histories, perhaps records are not burned tick by tick but behave
otherwise. Proposal tested: "There is one actual history, drawn from the history weighting; a record registers which
member of a coarse partition of histories was realised, permanently; only records are readable", the partition being
the site-local partitions that decohere, with CL-2's least surprise as selector among them.

Candidate laws used (conditional, zero premise weight; none is adopted). CL-1 to CL-3 here are the three-law numbering
of the source branches. They are not the clauses of the [candidate-law register](CANDIDATE_LAWS.md) on `main`, whose
CL-1 to CL-3 aliases are other clauses (lossless influence, record removal, conservation). CL-2 here is the actuality
law: one actual configuration, distributed as its odds, moved each half-tick by the support-confined fewest-change,
greatest-entropy transport defined in [the transport note](SUPPORT_CONFINED_RELAY_TRANSPORT_ON_THE_MARGOLUS_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md); every matter mode's
occupation is then recorded, records never condition the odds, and a past record is read only through a pointer
([pointer note](RECORDS_THAT_NEVER_CONDITION_THE_ODDS_GIVE_NO_ZENO_FULL_FRINGES_AND_CHSH_2_SQRT_2_WHILE_BARE_TWO_TIME_RECORDS_NEED_A_POINTER_BOUNDED_THEOREM_NOTE_2026-10-22.md)). CL-1 on those branches is
the update law of the odds; the other campaign notes attach the chiral weighting to it as a history-level matter
weighting.

## Repo check

- On main: [the admissibility/record continuation refinement note](ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md) states that a
  consistent-histories lift would have to prove D(a,b) = 0 for a != b on supplied state and dynamics and supplies no
  decoherence functional. This note supplies that functional on toys; it does not touch that note's order-theoretic theorem.
- Campaign notes used: overlap-from-walk (P_hat is history-level; no positive tick for the chiral overlap),
  overlap-colour / overlap-nonabelian (the candidate chiral weighting), tick-fraction-beta (the static exterior takes the
  source only through its integration constant), and the info-accounting note (B3). None of them is on `main` or on
  this branch; they are named here only, and the frontmatter dependency
  `the_overlap_of_the_cube_walk_euclidean_kernel_..._2026-10-23` is the overlap-from-walk note, which is likewise not in
  this repository. Statements that rest on them (the tick-form premise of D and the source premise of F) are
  conditional on those unrecovered inputs. A search on 2026-10-23 found no consistent-histories construction on main
  or in open PRs.

## Results

A. Born (task 1). Exact.
- A1. A single-time partition always decoheres (Tr(P_a rho P_b) = 0, a != b) with D(a,a) = Born. So CL-2's
  "distributed as its odds" is the single-time content of history actuality, for any state.
- A2, A3. The fine two-time mode partition of the supplied walk, with its sampled state, does not decohere (max |D_offdiag| 0.098; D(a,a) not additive,
  marginal error 0.15). CL-2's transport (LP minimum 2.0 changes, Sinkhorn max-entropy coupling, Born marginals to 2e-15)
  gives a two-time joint that differs from D(a,a) (TV 0.25). Under CL-2 this joint is unreadable (a record is read only
  by the half-tick taking it as input), so nothing measured distinguishes them.
- A4, A5. With a pointer register copying the site, the two-time partition decoheres exactly and D(a,a) = Born of
  (pointer, mode) at the later cut. In CL-2 the copy is a permutation and the walk's support never changes the pointer
  (moved mass 0), so CL-2's readable joint equals D(a,a) exactly. Verdict: YES. Readable statistics coincide exactly
  wherever CL-2's tick picture applies (here vector-like, unitary tick).

B. Read once and complementarity (task 2). Exact.
- B1, B2. For {path t1, port t2} with pointer overlap c = <p0|p1>: |D(L o, R o)| = |c|/4 and V = |c| on 7 couplings
  (deviation 1e-16). Recorded (c = 0): decoheres, V = 0. Unrecorded (c = 1): the path partition is inconsistent
  (|D| = 1/4), and the port-only set keeps V = 1.
- B3. With a reader copying the pointer, {path, port, pointer, reader} decoheres; disagreeing classes have weight 0
  (two readers of one pointer agree, as CL-2 states); the record carries exactly H(path) = 1 bit, and a second
  reading adds 0. This is the read-once content of the info-accounting note. Verdict: YES.

C. Arrow (task 3).
- C1 (exact). Coarse-graining a decohering set keeps it decohering, so later finer sets contain earlier kept records.
- C2, C3 (exact). {path t1, pointer t1'} decoheres if the history ends at t1'. If the pointer is then coherently
  un-copied, the specified refinements with a final port projection do not decohere: {path t1, port t2},
  {path t1, pointer t1' (Z), port t2} and {pointer t1' (Z or X), port t2} all have |D| = 1/4. The port-only set shows
  the fringe restored (P(port 0) = 1).
- C2b, C2c (exact). Negative result: the earlier statement "after a coherent un-copy no set holding path t1 or
  pointer t1' decoheres" is false. For orthogonal projectors P_a, a later unitary V and the state rho at that cut,
  D(a,b) = Tr(V P_a rho P_b V^+) = Tr(P_a rho P_b) = 0 for a != b; appending one common unitary to every class operator
  leaves the whole decoherence matrix unchanged. Witnesses: after the un-copy the path-only single-time partition
  {path t1} still decoheres with the same matrix as at t1 (difference 1.1e-16), and {path t1, pointer t1'} extended by
  the un-copy without a further projection keeps its matrix (1.1e-16). A class-dependent operator is not a common
  unitary and breaks the identity (|D(0,1)| = 1/2, C2c). So the computed failures are failures of the specified
  refinements, not a loss of the record from every set. These toys do not show that record status is fixed by the
  whole history, do not establish permanence and do not certify the proposed history rule.
- C4 (exact). With the two-boundary functional Tr(rho_f C_a rho_i C_b^+): pure ready pointers at the start give
  records of the past only (I = 1, 0 bit); pure pointers at the end give records of the future only (0, 1 bit).
  Verdict: the arrow is PUT IN by the boundary (pure ready pointers at the start, trace at the end), not derived.
  CL-2 also puts it in, by forming records forward each half-tick.

D. Chiral matter (task 4). Finite diagnostics, 2D U(1) overlap, m0 = 1, antiperiodic in the tick (periodic
   free Weyl determinants vanish at k = 0).
- D1. The vector-like det(1+V) is real and >= 0 (|Im|/|det| 6e-17), and an L x R pair of one charge is real (2e-15),
  so the vector-like history weighting is a positive measure.
- D2, D5. The 3-4-5-0 weight at Q = 0 is complex, with phase up to 3.9e-5 (4x4) and 1.1e-4 (6x6) at link noise 0.03.
  Classes partitioned by a local flux record (sign of one plaquette) have complex weights (|arg| 2.7e-5). Only
  |W|^2 is positive, and that is the theory with the mirror added, i.e. vector-like.
- D3. The gauge variation of the WB phase is 4.6e-3 / 2.5e-4 for a lone charge-5 Weyl against 7.5e-6 / 3.4e-5 for the
  anomaly-free product (ratio 610 on 4x4, 7 on 6x6). The first preset prediction (smaller) passes; a 10x threshold
  set after a scratch diagnostic fails on 6x6 and is reported, not used.
- D4. In the Q = 1 sector the negative-mode counts shift by the charge (-3, -4 for L; +5 for R): 7 L against 5 R zero
  modes, so the weight of every gauge history vanishes without fermion insertions. The weight of a history is then a
  Grassmann correlator, not a number.
- Where it fails. Euclidean weights are a single-copy measure. A decoherence functional pairs a forward with a backward
  amplitude joined at the final cut, which needs the operator (tick / transfer-matrix) form. This note has no
  tick form for the chiral overlap (the overlap-from-walk campaign note, not in this repository, reports none), so the
  decoherence functional used here is not defined for it. A decoherence functional for the chiral weighting was not
  constructed here; this is not a proof that none exists. The weight is also not positive in the sampled backgrounds,
  with a phase whose convention-independent part needs Luscher's measure term (open). Verdict: not constructed here.
  History actuality moves the missing tick form from CL-2's transport to the decoherence functional; it does not
  remove the need.

E. Set selection (Dowker-Kent risk).
- E1 (exact). For a two-site record (Bell state), every U x U* local basis is a decohering finest set at the least
  entropy (H = 1 bit), so least surprise does not fix the set. The axioms privilege no possibility, so no basis is supplied.
- E2 (finite optimisation). For a three-site redundant record (system, pointer, environment; GHZ), every
  least-surprise local basis found (11/12 starts; the others H >= 2) is the Z basis to 3e-8. This is
  tridecompositional uniqueness (Elby-Bub 1994, supplied): redundancy fixes the set.
- E3 (exact). Without site-locality the least-surprise partition is the state itself (H = 0). The Record axiom's
  "locks one admissible local possibility" supplies locality, not the selector.
- Dowker-Kent's general problem (many incompatible consistent sets, retrodiction
  that depends on the set) is not settled by these toys, only narrowed: in the toys the selector works when records
  are redundant (>= 3 sites) and fails for a bare two-site copy.

F. Gravity source (task 5). Conditional on the tick-fraction-beta campaign note (not in this repository): the
   tick-fraction static exterior takes the source only through its integration constant,
   i.e. the expected mass. Under history actuality the expected record or occupation density is the single-time Born
   mean, which is exactly D(a,a) of single-time sets (A1). F1: CL-2 trajectory record counts match it (max z 0.60,
   4000 trajectories, 10 ticks). Change: the source is the expectation, with no per-half-tick record of unmonitored
   matter. The clause "at most one record per free site per half-tick", which CL-2 needed to keep Planck-scale record
   noise out of the source, becomes unnecessary, and the Record axiom's original "a site never carries more than one
   record" can stand. Gravity was not recomputed.

## Proposed CL-2 wording (an unapproved proposal with zero premise weight; conditional; works only where a tick form exists)

Adopting any law is the owner's decision; this wording is a candidate for comparison only.

"There is one actual history, distributed as the history weighting. A record is a class of a site-local partition of
histories whose decoherence functional vanishes off the diagonal over the whole history; among such partitions the
records are those of least history entropy. The actual history fixes each record's class, permanently, at most one
per site. Only records are readable."

## Gate

(1) No measured number chosen: pass. (2) No observed structure by name: pass. (3) A prediction it was not built for:
none found. Its readable statistics equal CL-2's in every toy, so it is UNTESTED as a distinct rule. (4) Axiom bent:
none. It restores the Record axiom's one record per site, and it needs a dynamics in operator form, which the axioms
do not supply.

## Smuggling review

Supplied: the decoherence-functional rule (Gell-Mann-Hartle, Griffiths), exact rather than approximate decoherence,
the least-entropy selector over finest site-local sets, the initial boundary (pure ready pointers), the coin angle and
pointer couplings, m0 = 1, the 3-4-5-0 content, the Wigner-Brillouin phase convention (Narayanan-Neuberger), and
Elby-Bub uniqueness. Forced in the toys: Born at single cuts, complementarity V = |<p0|p1>|, reader agreement, the
failure of the specified port refinements after a coherent un-copy, and the equality of the readable statistics with CL-2's.

## Not covered

3+1D or interacting dynamics; approximate (rather than exact) decoherence and the choice of its threshold; a
transfer-matrix or reflection-positive form of the chiral overlap; Luscher's measure term; the general Dowker-Kent
multiplicity beyond these toys.
