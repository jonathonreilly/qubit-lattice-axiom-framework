---
claim_id: the_rung_ladder_is_a_domain_wall_direction_with_exact_inflow_but_bounded_speed_makes_its_coarse_rungs_a_charged_tower_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For a supplied free tree ladder (1+1D toy: rung j has cells of 2^j fine cells, two modes per cell, a Wilson-type rung tick with copy mass m, each parent exchanging with its two children through the rank-one T = (s_z - i s_y)/2 at kap/sqrt2), (A) one chiral pair forms: a mover on the finest rung and the opposite mover on the top rung; at the tuned wall m = -kap the zero-momentum kernel is exact, and an offset mu pairs the ends into a residual mass falling by mu/kap per rung (fine rate) or mu/(sqrt2 kap) (zoom rate); (B) with Wilson-line dressing the ladder is gauge covariant, flux 2 pi moves q species units and q^2 gauge units from the top rung to rung 0 (inflow along the rungs), the inflow sums to zero for 3-4-5-0 and for the 16, and gauging only the light end either breaks gauge equivalence or, after Gauss projection, cuts the ladder and puts a charged mirror at the cut; (C) at the zoom rate the middle-rung band gaps are 0.707 x 2^-j exactly self-similar, and a Weyl bound gives gap <= 2 ||hop||, so bounded speed forces one charged vector-like band per factor 2 in energy; at the fine rate the gaps are rung-independent but rung j moves 2^j fine cells per tick; (D) estimates: at R = log2(c/(H0 a)) = 200 the zoom ladder puts 17.4 charged three-family copies between m_e and M_Z, about 38 units of extra 1/alpha running against 0.014 known; (E) a full-density layer coordinate inside a role block is the domain-wall slab: no tower, residual mass (mu/kap)^Ls, but the far mirror keeps the full charge, so it gives exact chiral symmetry of a vector-like theory only. Supplied model, finite diagnostic; no rule is adopted."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_rung_ladder_is_a_domain_wall_direction_with_exact_inflow_but_bounded_speed_makes_its_coarse_rungs_a_charged_tower_2026_10_22.py
---

# The rung ladder is a domain-wall direction with exact inflow, but bounded speed makes its coarse rungs a charged tower

Claim type: bounded_theorem.
Primary runner: `scripts/the_rung_ladder_is_a_domain_wall_direction_with_exact_inflow_but_bounded_speed_makes_its_coarse_rungs_a_charged_tower_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its chirality item says no finite-range update gives net chirality at any rung, and that the update law's light content is vector-like. Domain-wall fermions get exact lattice chirality from an extra coordinate, with the light Weyl field on one boundary and its mirror on the other. This note asks whether a coordinate the framework already has can play that role without a literal Z^4. The candidates are the rung index of the nested blocks (the split cascade's levels) and the tick. Where the rung reading fails, the note tests one new rule, a layer coordinate inside a role block. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the model inputs.

Build on and narrow: the octree-ladder note (PR #9908) proved, for the 3D fine-rate ladder, the one fine chirality, the top-rung mirror, the per-rung residual-mass law and the unbounded range (an Eilenberg swindle). The campaign files hybrid-wall and ladder-wall cover the zoom-rate ladder, the top-rung pair square and the cut-rung flow. This note adds the following: the inflow along the rungs as an exact spectral-flow statement; anomaly-free versus anomalous content; the bounded-speed theorem behind the tower; the estimate at the rung count the horizon sets; and the full-density layer comparison.

## Statement

A. Free ladder (1+1D toy).
1. Exact. H_zoom = S H_fine S with S = 2^(-j/2), so the two rates have equal inertia at every Bloch momentum, and the zero-momentum kernel has dimension 2 at both rates (A1).
2. One chiral pair. On rung 0 a mover has velocity -1. On the top rung the opposite mover has velocity 2^R (fine rate) or 1 (zoom rate) (A2).
3. The ends' residual mass is mu (mu/kap)^R at the fine rate, with a ratio of 0.1994 to 0.2000 at mu = 0.2 kap. At the zoom rate (in fine units) the ratio is mu/(sqrt2 kap). At the tuned wall the mass is exactly zero (A3). At fixed physical momentum, the light state's weight on the top rung falls from 2.5e-14 (R = 2) to 1.2e-27 (R = 6) (A4).

B. Gauge.
1. Exact. With Wilson-line dressing (every hop carries exp(i q A dx), and every parent is anchored at its first child), the ladder at flux theta is the twisted ladder at Bloch Q_n = (q theta + 2 pi n)/N_top, with a residual of 3e-15 (B1).
2. Index. Each Bloch turn has one zero crossing on the light end and the opposite one on the top rung, at both rates and for both handednesses. Flux 2 pi therefore moves q units of species number and q^2 units of gauge charge between the ends. This is Callan-Harvey inflow along the rung direction through the gapped middle rungs (B2).
3. For 3-4-5-0 the gauge inflow is sum chi q^2 = 9 + 16 - 25 - 0 = 0, while the species numbers (3, 4, -5, 0) still flow. For one family's 16, the coefficients Y^3, Y, SU(2)^2 Y and SU(3)^2 Y all vanish. So anomaly freedom makes the light end alone gauge-consistent, but it does not decouple the mirror (B3).
4. Gauging only the light end. If the cut is left undressed, the hops across it break gauge equivalence (the spectra of H(2 pi) and H(0) differ by 0.38). If Gauss's law projects those hops out, the ladder is cut. Crossings by rung are then [-1, 0, +1, -1, 0, +1]: the gauged piece carries its own charged mirror on rung J - 1 (B4).

C. Rates.
1. The middle-rung band gaps are 0.74 on every rung at the fine rate. At the zoom rate they are exactly 0.707 x 2^-j (C1).
2. Weyl bound (theorem). Suppose the smallest on-site |level| exceeds ||H_hop||. Then the path from the on-site Hamiltonian to H stays gapped, so the index is 0. A wall therefore needs bulk gap <= 2 ||H_hop||. In the scan, the largest ratio at indexed points is 0.52 (C2). By Lieb-Robinson, bounded speed v with hop range 2^j caps rung-j hops at about v 2^-j. So at bounded speed, gap_j <= 2 v 2^-j. Bounded speed makes the zoom rate the fastest rate allowed, and with it the tower of bands.

D. Estimates against measurement.
1. Diagnostic. A unit-charge 3D Wilson-Dirac band gives Delta(1/e^2) = chi(q)/q^2 = 0.035, 0.022 and 0.014 at m0 = 0.2, 0.354 and 0.6. These are within a factor 2 of the continuum value ln(Lambda^2/m^2)/(12 pi^2) (D1).
2. With a = sqrt(8 pi) l_P, the horizon sets R_H = log2(c/(H0 a)) = 200.1. At the zoom rate, a gauge-covariant ladder puts log2(M_Z/m_e) = 17.4 rungs between m_e and M_Z. Each is a vector-like three-family copy with sum Q^2 = 8. Together they add 17.4 x 4 pi x 0.022 x 8 = 38 to the running of 1/alpha, against an uncertainty of 0.014 (Delta alpha_had). This is excluded unless c1 < 2.4e-5 (D2).
3. At the fine rate there is no tower, and the mirror has essentially no states below 1 TeV per horizon volume. The residual mass is at most 1e-42 GeV for mu/kap = 1/2. The price is that rung j crosses 2^j sites per tick, the swindle of PR #9908, which goes against nearest-neighbour admissibility (D3).
4. Any cut, or any finite top rung with E_R above M_Z, leaves a massless charged mirror. The mirror e^c' alone adds 35.5 MeV per family to Gamma_Z (ladder-wall E3), against sigma = 2.3 MeV (D4).

E. A full-density layer coordinate, the rule proposed when the scope was widened.
1. Each matter cell holds 2 Ls one-mode sites (layer s, component). The layer hop T acts inside the cell, and the cell-to-cell hop K acts at equal layer. This is the domain-wall slab. The layer gap is the same on every layer (1.0, so no tower), the residual mass falls by (mu/kap) per layer (0.04 per two layers), and the flow is (-1 near, +1 far): the far mirror carries the full charge (E1).
2. Theorem (from B1 and B2). Any gauge-covariant reading of the far layers keeps their crossing under flux 2 pi. The mirror therefore couples to the holonomy with charge q. The slab gives exact chiral symmetry of a vector-like theory, not chiral gauge couplings.
3. Estimate of the cost. One family needs 16 Weyl x 4 components x Ls sites per cell. Three families at Ls = 8 use 1536 of the 1728 sites of a 12^3 role block. The cell-to-cell hops span the block, which gives a uniform slowdown and no tower.

F. The tick (counting theorem). A domain wall bounds a bulk with one more dimension, and its boundary is the whole 3+1 world, tick included. So the tick cannot be the wall direction. The B4 transfer matrix is the world's own time step: euclidean-b4 B4 shows it projects onto the vacuum and cannot carry CL-2. Neuberger's overlap sign(H_W) is the infinite-layer limit of a fifth-direction transfer matrix, that is, of E's layer coordinate.

## Candidate law text (not adopted)

Rung reading, as tested here (fails measurement, D2/D4):
> "Each block's mode exchanges with the same mode of its children through T = W(1 - g5)/2, at the block's own rate, with the copy mass the wall height."

Layer rule, proposed (exact free chirality; vector-like as it stands):
> "Each matter cell is a role block whose matter sites, in a fixed order, are layers 0..Ls-1. Each half-tick hops every layer's modes to its neighbour layer through W(1 - g5)/2 and to the same layer of the neighbour cell through the cube tick; matter is read at layer 0."

To make the gauge couplings chiral, the layer rule needs one more clause. Either the far layers are gapped symmetrically (pair-square route; toy-qmc found pair order in the extended zone), or the far layers' hops read a smoothed field that keeps the holonomy (the Grabowska-Kaplan route, not tested here). The smoothed-field clause has an open risk: the holonomy and the topology stay coupled (E2).

## Smuggling check

Supplied: the tree and its isometric exchange, the rank-one T with its handedness sign, m = -kap (tuned), mu, both rates, Wilson-line dressing and parent anchoring, the cut, N_top, the Q grid, the 3D Wilson band (m0, grid N = 20, q = 0.08), Ls, a = sqrt(8 pi) l_P, H0, and the PDG inputs. Forced given those: the congruence, the kernel count, the chiral pair, the residual-mass ratios, the gauge covariance, the spectral flow, the zero inflow sums, the charged mirror at a cut, the self-similar tower, the Weyl bound, and the far-layer charge. Not derived: that coarse cells carry modes. That needs either extra sites (the Lattice and Qubit axioms) or the role-assigned sites of CL-1, which is an owner-pending departure. The rung count R_H = 200 is an estimate tied to the horizon. The per-rung polarisation c1 comes from a stand-alone Wilson band, not from the ladder's own rung band; the exclusion holds for any c1 above 2.4e-5.

## Boundary

The toys are 1+1D, plus a 3D band integral. The 3+1D statements are cited (PR #9908, hybrid-wall) or argued by scaling (self-similarity, power counting). No interacting mirror, smoothed-field clause or adopted rule is established. Clause count: the rung reading adds one clause (the exchange) and gives one generation. The layer rule adds the layer clause plus a decoupling clause, and it removes none unless the decoupling clause can replace the register's mirror term.
