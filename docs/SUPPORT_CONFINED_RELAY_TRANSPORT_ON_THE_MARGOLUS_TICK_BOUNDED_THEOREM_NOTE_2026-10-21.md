---
claim_id: support_confined_relay_transport_on_the_margolus_tick_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "In supplied models on the spin-3/2 Margolus tick (one relay on 12^3 and 8^3 tori, two entangled fermion relays on 4^3, a three-block ring with relay number free, and two-block CHSH and reader models), a transport of the configuration distribution that uses only nonzero elements of each half-tick, moves the fewest modes and is of maximal entropy among those keeps Born statistics exactly, gives agreeing readers and CHSH 2 sqrt 2, and is unique, label-equivariant and separable; it also splits some plane waves into sublattice streams of different velocity and revisits burnt sites. No physical identification or adoption is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/support_confined_relay_transport_on_the_margolus_tick_2026_10_21.py
---

# Support-confined relay transport on the Margolus tick

Claim type: bounded_theorem.

The register's switching rule (proportional shortfall switching among connected targets) does not keep Born statistics on one Margolus block: the worst inflow error is 0.317. A transport that uses only nonzero elements of the half-tick always exists. For any target set S, P_S U = P_S U P_{N^-1(S)}, so with U unitary ||P_S U psi||^2 <= ||P_{N^-1(S)} psi||^2. That is the supply-demand (Hall) condition, and max-flow/min-cut then gives a plan. Its largest excess over all 254 sets is 5.6e-16. The earlier "minimal switching" of the straight-pairing picture also keeps Born, but only by sending 32 to 100 per cent (mean 68 per cent) of each half-tick's switched mass along zero elements of W.

The law tested here: the configuration moves by the plan that (i) uses only nonzero elements, staying included, (ii) has row sums equal to the old odds and column sums equal to the new odds, (iii) changes the fewest mode occupations on average, and (iv) has the largest entropy among such plans.

Clause (iii) alone never gives a single plan. The optimal face has dimension 10 for every state at mu = 0, where no stays are allowed, and dimension at least 1 at mu = 0.3. An LP vertex depends on the labels (95 per cent of cases). Clause (iv) gives one plan. It is equivariant under relabelling (to 1.7e-16) and under translation, and it is continuous (|dJ|/|dpsi| <= 0.72). Least squares is also unique and equivariant, but it couples unentangled relays (5.4e-3), while max entropy does not (1.9e-15). Counting the whole configuration as staying, rather than counting modes, also couples unentangled relays (0.077).

Results. Over 16 half-ticks the distribution stays the odds to 1.8e-17 for one relay and to 3.4e-16 in total variation for two entangled relays. With relay number free, relays begin and end in pairs, the total variation stays at 7.4e-11, and no block value is violated. Moving each relay by its own marginal fails, with total variation 0.343. CHSH reaches 2.83, and two readers never disagree, against 0.418 when each pointer moves by its own marginal. A step acting only on A never moves B. For plane waves the mean drift equals the group velocity to 1e-10, for any block-confined transport.

Relays jump on 53 to 100 per cent of half-ticks and zigzag. In 5 of 8 (K along x) and 4 of 8 (K along xy) mu = 0.3 plane waves, the per-tick chain splits into two sublattice streams that never mix, for example at 1.507 and 0.513 site/tick against a group velocity of 0.839. Relays land on sites they have already burnt on 44.5 per cent of half-ticks at mu = 0.3 and 2.3 per cent at mu = 0. One transport per half-tick differs from two block-by-block transports of the same unitary: slicing moves 0.37 to 0.67 more modes.

Supplied: the configuration space, the cost (modes moved), the max-entropy tie-break, the half-tick as the transport step, the basis rotations, the pointer couplings, the coins and pulse, and the states.
