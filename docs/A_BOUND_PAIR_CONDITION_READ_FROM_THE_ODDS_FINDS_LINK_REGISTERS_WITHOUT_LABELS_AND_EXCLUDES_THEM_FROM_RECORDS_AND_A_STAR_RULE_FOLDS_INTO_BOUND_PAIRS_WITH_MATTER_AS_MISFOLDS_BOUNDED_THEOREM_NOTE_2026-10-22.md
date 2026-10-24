---
claim_id: a_bound_pair_condition_read_from_the_odds_finds_link_registers_without_labels_and_excludes_them_from_records_and_a_star_rule_folds_into_bound_pairs_with_matter_as_misfolds_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Finite exact diagnostics on 1D rings and chains (N <= 12, fixed-number sectors), a 3x3 torus and a 12-mode U(1) quantum-link ring (S = 1/2, Gauss sector of dimension 7). A site is called bound when some face-mirror pair of sets (A containing it, A' the mirror of A across a bond, |A| <= 2) has a definite n_A + n_A' while n_A is not definite, and free otherwise. Results: the reading is translation-, reflection- and quarter-turn-covariant (mismatch 1e-15); translation-invariant odds give uniform roles, and the half-filled sea has no bound site; the uniform star rule sum_x P_3/2(x-1, x, x+1) has exactly two zero-phase states on even rings N = 8, 10, 12, the two bound-pair coverings, gapped (0.54, 0.47, 0.43), with every site bound; imaginary-time flow from 20 random starts reaches that manifold (fidelity 1 - 1e-11) but never one sharp covering; an odd ring forces one domain wall whose site is free; at defect density 1/3 the period-3 pair-plus-free-site layout carries 0.92 (N = 9) and 0.89 (N = 12) of the lowest states, not stationary; on L x L tori the runner counts the contractible coverings, 121 (4x4) and 28561 (6x6), lower bounds that omit coverings wrapping the torus (the full pair-covering counts, 272 and 90176, come from the companion fold-selection note, PR #9978, not from this runner); locking a bound site fixes its partner in 20/20 cases; in the quantum-link ground state the condition finds 8/8 rishons and 0/4 matter sites without labels; two-site register ends are found by the set-pair form; with local star gates and the exact fewest-change transport (LP), bound pairs stay exact outside the wall's light cone, and a free site's latest record reproduces the Born marginal for one record per half-tick (max z 2.6) and for records on occupation change (z 2.6, 8x fewer records), but not for records only on role change or once ever (z 52); odds-read graded exclusion keeps recorded values Born (z 3.2) and a configuration-read exclusion biases them (z 25). Toy rules only: the star rule is supplied and is not CL-1's cube tick; no 3D, no gauge-factor sizes, no edge-register dynamics."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_bound_pair_condition_read_from_the_odds_finds_link_registers_without_labels_and_excludes_them_from_records_and_a_star_rule_folds_into_bound_pairs_with_matter_as_misfolds_2026_10_22.py
---

# A bound-pair condition read from the odds finds link registers without labels and excludes them from records, and a star rule folds into bound pairs with matter as misfolds

Claim type: bounded_theorem.

The candidate-law register has zero premise weight. Today it assigns site roles by layout: CL-1 uses nested role blocks to decide which fine sites are matter, rishon or edge-register sites, and CL-2 exempts rishon and edge sites from records by fiat. This note tests whether one covariant condition, read from a site's neighbourhood odds, can do both jobs. Axiom text is quoted from `docs/MINIMAL_AXIOMS_2026-06-29.md` and is not edited. Lattice: "No site is privileged." Record: "When present, a record locks exactly one admissible local possibility." Admissibility reading note (2): the distribution "does not supply the formation site, probability, or rate."

## The condition

A site x is **bound** at a half-tick when the odds hold one or more units shared across a face with x's mirror partner. Concretely, there is a set A containing x on one side of a bond and its mirror image A' across that bond (a pi turn about the bond's face, which is a proper rotation) such that:
- n_A + n_A' is definite, and
- n_A is not definite.

Otherwise x is **free**. A bound site acts as a register site; a free site acts as matter.

Why a bound site carries no record (theorem; C1): if n_A + n_A' is definite, then locking n_x fixes a possibility outside x. For a single-site pair, A' is x's partner. So that record would lock more than one local possibility, which the Record axiom does not allow.

A free site's lock fixes no neighbour. The Gauss cluster is the case to watch: n_m + n_{r-} + n_{r+} is definite, but it is not a mirror pair. So matter stays recordable (C2).

## Results

**Covariance (A1).** The condition is one functional of a site's neighbourhood odds, so it commutes with every lattice symmetry. The test checked translations, the ring reflection and the quarter turn, with mismatch 1e-15.

**Uniform odds give uniform roles (A2).** Translation-invariant odds give every site the same role. The half-filled sea (the 1D analogue of the update's vacuum) has no bound site: c = 0.42 everywhere, and every site is free. So under CL-1 as written, configuration roles make everything matter. A layout needs odds that break translations.

**A fold (B1).** The uniform rule sum_x P_3/2 projects each site's nearest-neighbour star onto total spin 3/2, so it is covariant and acts on stars. Its zero-phase states on even rings are exactly the two bound-pair coverings, which are translates of each other.
- The fold is unique up to translation and gapped.
- Every site in it is bound. The folded vacuum is all register.

**Funnel, and its wall (B2).** Every random start flows into the two-fold manifold. But it lands in a superposition of both coverings, and there no pair sum is definite. The odds do not pick a fold. Records cannot pick one either, because under CL-2 they never condition the odds. So records do not freeze the fold the way folding freezes a protein. Selecting a fold needs symmetry-broken initial odds or an added term.

**Misfolds are particles (B3).** A misfold is a domain wall between the two coverings, and its site is free: that site is matter, carried by the configuration. The wall:
- is a spin-1/2 doublet;
- moves: the lowest 9 states on N = 9 span 1.04;
- appears only in pairs on even rings, because the wall number mod 2 is conserved.

**The familiar layout (B4).** At wall density 1/3, the period-3 layout (bound pair plus a free site, with matter at the block centre) is the dominant domain of the lowest states: 0.92 at N = 9 and 0.89 at N = 12, against 0.036 and 0.006 for a random state. It is not stationary, and the density is supplied.

**2D and 3D (B5).** The zero-phase manifold contains every pair covering. The runner counts the contractible coverings: 121 on the 4x4 torus and 28561 on the 6x6, lower bounds, since coverings that wrap around the torus are omitted. The full pair-covering counts, 272 and 90176, come from the companion fold-selection note, PR #9978, not from this runner. So the manifold carries at least about 0.29 nats per site. The fold is not unique there, so a selection rule is needed.

**Exclusion found without labels (C2, C3).**
- In a U(1) quantum-link ground state, the condition finds the rishons (8/8) and not the matter sites (0/4) with no labels given.
- Two-site register ends (spin-1 type, shared total) are found by the set-pair form, though no single site is bound.

**Dynamics (D1).** Under local star gates, bound pairs stay exactly bound until the wall's light cone reaches them. Roles change only inside the defect's cone.

**Rate (D2).** The actual configuration is moved by the exact fewest-change transport. A free site's latest record reproduces the Born marginal when a record forms either:
- every half-tick (R1), or
- whenever the occupation changes or the site turns free (R3), with about 8 times fewer records.

Records formed only when the role changes (R2), or only once (R0), go stale: z = 52.

In every rule the record count never falls, which is the arrow. R3 needs no record-reading at formation, but an unchanged site then has no fresh record for the next half-tick. So CL-2's read-once clause needs a pointer for it.

**Born needs odds-read exclusion (D3).** Exclusion must be read from the odds, never from the actual configuration. With odds-read graded exclusion, recorded values stay Born (z 3.2). A configuration-read exclusion biases them (z 25).

## Candidate law text (proposal)

> CL-2.4' (records). Each half-tick, every site that is free in the half-tick's odds gets a permanent record of its occupation. A site is bound when some set containing it and that set's mirror across one of its bonds hold a definite total that the set alone does not; a bound site's occupation is part of the actual configuration but gets no record.

This replaces CL-2.5 (the exemption) and the role clause inside CL-2.4. It does not replace CL-1.7 and CL-1.8's role layout: the link and edge constraints still sit on assigned blocks. The fold above makes the layout emerge only in a 1D toy.

Variant R3, if the owner prefers fewer records: "a free site is recorded at the half-tick it turns free and at every half-tick its occupation changes." Same Born readout. It needs a pointer to keep the read-once clause.

## Smuggling review

**Supplied:**
- the star rule;
- the mirror-set form, with |A| <= 2 in the runner;
- the definiteness tolerance (1e-10);
- the wall density in B4;
- the U(1) link model (layout given there, read without labels);
- tau, sizes and seeds.

**Forced, given the reading:** "exactly one local possibility" means the lock fixes no other site. That reading is a choice, and it should be flagged to the owner.

**Not derived:**
- a uniform covariant rule in 3D whose fold is the nested B_f and b_e layout;
- the gauge-factor sizes;
- fold selection;
- edge-register dynamics.

Related work on main, used: `docs/THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (supplied spin-1/2 link role). The non-abelian Gauss-law note on main (zero record patterns in the Gauss kernel) is consistent with excluding entangled link sites. This note narrows `docs/COVARIANT_NN_SUPPORT_RULES_GAUSS_LAW_AS_GLUED_SUPPORT_AND_HOLE_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-14.md` only in giving a role condition; it does not contradict it.
