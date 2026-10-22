---
claim_id: cube_split_carries_the_half_filled_sea_only_with_half_filled_newborn_modes_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied cube tick without copy mass, the empty and full states have identically zero induced link response while the half-filled sea responds and runs; a mode-number-conserving split with empty newborn modes fills only 4 of 32 fine sea modes per parent; with half-filled newborn modes a nearest sea-to-sea unitary exists, its O(k^2) coarse/fine mismatch is not removable by any finite-range analytic generator, and a strictly local handover keeps the vacuum gap at every K != 0; comparisons with measurement are estimates."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/cube_split_carries_the_half_filled_sea_only_with_half_filled_newborn_modes_2026_10_21.py
---

# A cube split carries the half-filled sea only with half-filled newborn modes

Claim type: bounded_theorem.
Primary runner: `scripts/cube_split_carries_the_half_filled_sea_only_with_half_filled_newborn_modes_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its tick law lets a cube split into its eight children, and main chooses no vacuum. This note asks whether the empty and half-filled vacua differ physically and how a split can carry the half-filled sea. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the tick nor the split. All computations use the cube tick without the copy mass.

## Statement

1. A tick that conserves mode number leaves the empty state with phase exactly 0 under any link field, and the full state's phase is linear in the field. Both have identically zero induced link response. The half-filled sea responds, and its coupling runs, 1/e^2 = kappa[ln(1/m) + C] with kappa = 2/(6 pi^2); the other half gives -1/e^2.
2. A local site relabelling keeps every region's entanglement, and particle-hole conjugation maps empty to full and the sea to the sea, never empty to the sea. The site records distinguish the two vacua.
3. A split that conserves mode number with empty newborn modes fills only 4 of the 32 fine sea modes per parent and changes the charge sum (n - 1/2) by -28 per parent.
4. With half-filled newborn modes, the nearest unitary V* that carries the coarse sea onto the fine sea exists. In the midpoint frame the coarse and fine seas share X0(n) = i sqrt3 [n.C, W] at the Dirac point for every step. The O(k) mismatch is removed by a range-1 analytic unitary; most of the O(k^2) mismatch is removed by no polynomial generator. So any finite-range split leaves excited sea modes at order k^4 per momentum point.
5. A strictly local handover keeps the vacuum gap at every K != 0, so an adiabatic split carries the sea.

## Derivation

Under a link field a mode-number-conserving tick acts on the empty state as the identity, so its phase is 0 at every order. On the full state the phase is the phase of a determinant, which is linear in the field, so its second-order response vanishes. Particle-hole conjugation exchanges the two and maps the half-filled sea to itself. A site relabelling is local and cannot change regional entanglement, so no local relabelling turns the empty state into the sea; the usual reinterpretation of the Dirac sea as empty is a non-local mixing of energy modes. One cube of the sea has entanglement 3.55 nats, record entropy 5.39 nats and occupation count 4 +- 1.04; the empty state has 0 for all three.

The counting follows from the mode numbers: a parent's sea modes pass to the children's corner modes, and the newborn modes start empty, so 28 of the 32 fine sea modes per parent are holes. The earlier heat-free sign map sits inside the fine sea but leaves 7/8 of it empty. Since links attach only to exactly conserved charges, 28 newborn particles per parent are forced.

Filling each child sign pattern with the fine sea at its zone point, the sign blocks are nonsingular on the whole zone (minimum singular value 0.38 to 0.75), so V* exists. An exact Taylor series in k along 324 directions shows the O(k) mismatch is analytic and 98.6% of the O(k^2) mismatch is irreducible: non-analytic quartic angular terms remove it to 7e-13, polynomial generators do not. Mixing in the alias and newborn blocks cannot help, by a block argument. A two-point-function argument, not computed, extends this to non-Gaussian local unitaries.

The handover step applies the children's half-ticks at step s eps_f, eight parent ticks at step (1 - s) eps_c, and the newborn modes' zone-point tick to the power 1 - s. Along this path no quasi-energy crosses 0 or pi at any K != 0.

## Checks

The runner ends with `TOTAL: PASS=12 FAIL=0`. Among its lines:

- `[PASS] A1`: all 8 bands obey the register's band law, the sea projector has rank 4, and the split's alias matrix is unitary to 3e-13.
- `[PASS] A2 THEOREM: in the midpoint frame the massless sea at the Dirac point is X0(n) = i sqrt3 [n.C, W] for every step`.
- `[PASS] B1 THEOREM + exact (8 site)^3 torus: under a link field the empty state keeps phase 0 and the full state's phase is linear (det), so both have zero induced response; the sea and the other half respond oppositely`.
- `[PASS] B2 the sea's link coupling runs: 1/e^2 = kappa[ln(1/m) + C] with slope -> kappa = 2/(6 pi^2) ...; the other half gives -1/e^2 (ghost photon) and empty and full give 0 at every m`: 1/e^2 = 0.0707, 0.0824, 0.0936 at m = 0.5, 0.35, 0.25.
- `[PASS] B3 THEOREM: a site relabelling is local, so it keeps every region's entanglement; particle-hole maps empty <-> full and sea <-> sea`.
- `[PASS] C1`: the earlier corner passing sends about 20% of the coarse sea modes above the fine sea.
- `[PASS] C2 THEOREM (counting): a split that conserves mode number with empty newborn modes fills 4 of the 32 fine sea modes per parent (28 holes)`.
- `[PASS] C3 newborn modes half filled ...: the plain passing still heats, but the sign blocks are nonsingular on the whole zone, so the nearest unitary V* maps the sea onto the sea exactly`.
- `[PASS] C4 exact series at the Dirac point: the O(k) coarse/fine mismatch is removed by a range-1 analytic unitary; the O(k^2) one is mostly irreducible`.
- `[PASS] C5 (10 cell)^3 torus, massless: V*'s kernel falls fast and a re-unitarised range-r truncation removes the heating to 1e-4 (r = 1) and 1e-6 (r = 3)`: the kernel falls by 1e-1, 3e-3, 6e-4, 2e-4 at 1 to 4 cells, and heating is 6.4e-2, 1.3e-4, 7.0e-6, 1.2e-6 at r = 0 to 3.
- `[PASS] C6 a strictly local handover ... keeps the vacuum gap at every K != 0: an adiabatic split carries the sea`; the smallest gap stays at 0.94 of the end values.
- `[PASS] D1 arithmetic: plain-split heating exceeds rho_c by > 1e110; strict range needs > 1e13 cells; handover needs > 1e-25 s`.

## Estimates against measurement

An empty vacuum has no Uehling term: the muonic-hydrogen vacuum-polarisation term is 205.0 meV against a measured 202.3706(23) meV. It also gives no running of alpha, against 1/alpha going from 137.036 to 127.95 at M_Z. By these estimates the vacuum must be the half-filled sea.

A split with empty newborn modes injects about 72 hbar c/l_f per parent; plain passing with half-filled newborns about 18.7, a density near 5e72 GeV^4 per split, which exceeds today's critical density by about 1e119. A finite-range split leaves rho = N_s F r^-8/(8 pi^2 l_c^4) with F = 3.6e-5 and N_s = 12, which needs r of about 1e14 to 1e15 cells from the critical density and the Fermi cascade bound. The exact V* kernel falls roughly as r^-4. A handover must last more than about 1e-21 s; today's doubling time is about 3e17 s.

## Boundary

Supplied: the tick without copy mass, the negative-quasi-energy branch, site-phase links, the register's corner passing and midpoint frame, the newborn zone-point state, the nearest-unitary criterion, the handover path, the grids and tori, the unit map l_f = 2 sqrt(8 pi) l_P, the species count and the measured numbers. The result with one light copy was not computed. The exact split breaks the strict light cone at amplitude about (l/r)^4; the handover keeps the light cone but turns the split into a process, and how it fits the register's fixed 4-volume per record is not settled. Since the sea is forced, the register's gravitational-source clause must exclude sea modes, or the frozen sea adds Planck-scale noise to the source. This narrows the main note that leaves the vacuum as one free coefficient of the law: there, measurement decides. No split rule is adopted here.
