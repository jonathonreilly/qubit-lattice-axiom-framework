---
claim_id: a_fold_is_a_slow_scalar_clock_only_when_the_unfolded_sea_is_critical_on_a_surface_and_the_updates_dirac_sea_makes_it_fast_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For a fold order parameter m that opens a gap in a half-filled sea, with the one-loop (adiabatic) stiffness Z(m) = sum |<n|dH|0>|^2 / (E_n - E_0)^3 and the semiclassical slow-roll dictionary: (A) exact on rings N = 8, 10, 12: the star rule sum P_3/2 is the Majumdar-Ghosh form, with two gapped zero-phase folds; uniform odds (equal amplitudes on every half-filled configuration) are its top, an exact eigenstate at energy 1 per site, which the update's hop moves off within about one tick; the sea's weight on the fold manifold is conserved under the fold rule's unitary and falls with N (0.786, 0.660, 0.541). (B) Theorem: Z = c_d m^(d-3), with d the codimension of the sea's gapless set (c_1 = 1/3, c_2 = 2/3, d = 3 logarithmic), so the unfolded point is at infinite field distance only for d = 1. Lattice ratio check: 1D dimer chain 4.04, 3D nested cubic sea 4.00, 3D Dirac sea 0.91 (4 means pole, 1 means log). (C) 1D toy with the pole (dimer path, exact infinite-chain Wick): V_star falls monotonically from 0.07559 to 0 and z = 1/(24 pi delta^2); slow roll gives n_s = 0.9631-0.9634 at N* = 55 for rungs 0, 2, 4, r = 7e-6 to 2.5e-8, exit at delta = 0.01-0.05; lam = 2^(-2/N) = 0.975; A_s fixes the fold rung near 20 for coupling 1; children born unfolded give q = 1/8 + 7x/8, never a clock. (D) The update's isotropic Dirac band (d = 3, continuum ball cutoff): eta at N* = 55 is -0.88 (flat rung) and -14 (rung 4); n_s = 0.965 needs zeta ~ 50 against zeta <= 1 from the unit map. (E) Plateau energy that leaves the coherent mode sits in misfolds: at most 0.36 walls per site at full conversion. Supplied: the star rule, the dimer path and one-loop stiffness, J a = sqrt 3, M_P a = 1 at the flat rung, the fold rung, coupling gamma = 1, N* = 55, the Dirac cutoff, m_f = 1, semiclassical FRW with Hubble friction, the split carrying the fold order."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_fold_is_a_slow_scalar_clock_only_when_the_unfolded_sea_is_critical_on_a_surface_and_the_updates_dirac_sea_makes_it_fast_2026_10_22.py
---

# A fold is a slow scalar clock only when the unfolded sea is critical on a surface, and the update's Dirac sea makes it fast

Claim type: bounded_theorem.
Primary runner: `scripts/a_fold_is_a_slow_scalar_clock_only_when_the_unfolded_sea_is_critical_on_a_surface_and_the_updates_dirac_sea_makes_it_fast_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The split-time cascade note and the record-clock note show that splits and records are self-similar, so neither gives a tilt. The primordial spectrum needs a scalar clock with a per-split factor lam = 2^(n_s - 1) of 0.976 to 0.982, A_s = 2.1e-9, r < 0.036 and an exit.

This note tests an owner idea: the early universe is the grid folding.
- Before roles exist, the odds are unfolded and carry vacuum energy (a plateau).
- Neighbourhoods fold into the bound-pair layout of the neighbourhood-roles note, releasing that energy.
- Misfolds are matter.
- The fold order parameter is the clock.

The potential and the stiffness are computed from the model, not chosen. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. The funnel's ends (exact, rings N = 8, 10, 12, half-filled sector).

1. Each P_3/2 on a three-site star is a rank-4 projector. The star rule sum_x P_3/2(x-1, x, x+1) equals N/2 + (4/3) sum S.S(x, x+1) + (2/3) sum S.S(x, x+2), which is the Majumdar-Ghosh chain (literature, 1969). It has two zero-phase folds, the bound-pair coverings, with gaps 0.539, 0.467 and 0.426.
2. Uniform odds (equal amplitudes on every half-filled configuration) are the funnel's top:
   - every star is spin 3/2, so the energy is 1 per site, the maximum;
   - the state is an exact eigenstate of the star rule and of every SU(2)-blind rule, so a fold never starts from it;
   - the update's hop breaks SU(2) and moves it off the top within about a tick (fidelity 0.83, 0.51, 0.20 at t = 0.25, 0.5, 1).
3. The update's sea (the XX ground state) sits low on the funnel: star energy 0.0645, 0.0685 and 0.0707 per site, tending to 0.0756. The fold manifold's projector commutes with the fold rule, so under that rule's unitary the sea's fold weight (0.786, 0.660, 0.541, about 0.91 per site) never changes. Unitary odds never complete a fold, so an energy sink is needed. Records cannot be the sink, because they never condition the odds (CL-2).

B. What sets the fold's speed (theorem and lattice check).

1. Theorem. Let a fold order parameter m open a gap in a sea of two-band (or Clifford) type. Its adiabatic (one-loop) stiffness is Z(m) = int rho(e) e^2 / (4 (e^2 + m^2)^(5/2)) de. If the gapless set has codimension d, then rho ~ e^(d-1), and Z = c_d m^(d-3):
   - d = 1 (a surface of gapless modes, or a 1D sea): a pole m^-2, with c_1 = 1/3;
   - d = 2: m^-1, with c_2 = 2/3;
   - d = 3 (Dirac points): log(1/m) only, with constant log 2 - 4/3.

   The canonical distance to the unfolded point, int sqrt(Z) dm, diverges only for d = 1.
2. Lattice check, using the ratio [Z(0.1) - Z(0.2)] / [Z(0.2) - Z(0.4)], which is 4 for a pole and 1 for a log:
   - 1D dimer chain: 4.04;
   - 3D half-filled nearest-neighbour cubic sea (a nested Fermi surface; the fold is the staggered gap): 4.00;
   - 3D lattice Dirac sea: 0.91.

C. A 1D toy where the pole exists: the star rule on the dimer path (hops 1 +- delta, with delta = 0 the sea and delta = 1 the fold).

1. Exact infinite-chain values:
   - The Wick reduction gives V_star = 1/2 + (2/3)[(g_s - g_s^2) + (g_w - g_w^2)] + (4/3) g_s g_w from the strong- and weak-bond correlators. It is checked against a 10-site Slater state (1e-12) and a 400-site chain.
   - V_star falls monotonically from V0 = 0.07559 to 0, with V0 - V ~ delta^2 ln^2(1/delta).
   - The stiffness is z = 1/(24 pi delta^2) (0.013263 at delta = 1e-9).
2. Slow roll. Take chi = zeta int sqrt(z) d delta in Planck units, with zeta = (J a)^(-1/2) / (M_P a_r) and M_P a = 1 at the flat rung (unit map). The pole makes V(chi) an exponential plateau: the fold is critically slowed near the sea.
   - n_s at N* = 55 is 0.9631, 0.9633 and 0.9634 at rungs 0, 2 and 4, against 1 - 2/55 = 0.9636. It does not depend on the coupling or the rung.
   - r is 7.0e-6, 4.1e-7 and 2.5e-8, which is about 2 zeta^2 z0 / N^2.
   - eps reaches 1 at delta = 0.05 to 0.01, before the fold completes. This is the graceful exit.
3. Per-split factor: lam = 2^(-2/N), which is 0.9751 at N = 55, inside Planck's range. It is not constant (running -2/N^2 = -6.6e-4). ACT's 0.974 needs N* = 77, as for every exponential plateau (act-tilt).
4. Amplitude. A_s = gamma V0 N^2 2^(-2r) / (pi^2 z0), so A_s fixes the fold rung: r = 19.8 + log2(gamma)/2. Then H/M_P = 2.5e-13 and r = 6e-18.
5. Split re-seeding. If children are born unfolded with share x, the per-split energy factor is q = 1/8 + 7x/8.
   - x = 1 is exact de Sitter with no exit.
   - Constant x < 1 is power-law inflation, with r = 16 eps = 0.28 at q = 0.976 (inflaton-design B1).

   The clock therefore needs the split to carry the fold order to the children.

D. The update's sea.

1. The update's light band is an isotropic Dirac band, a point node, so d = 3 (continuum, ball cutoff of one mode per cell, fold gap m_f = 1). The stiffness is only logarithmic, so eta ~ -sqrt(c2 / (V0 zeta^2 z1 N)) on the log asymptotics:
   - at N* = 55, eta = -0.88 at the flat rung (n_s far below 0.9);
   - eta = -14 at rung 4;
   - n_s = 0.965 would need zeta ~ 50, a cell far below the Planck length, against zeta <= 1 from the unit map.
2. Fold speed. Without the pole, a gapped local fold relaxes in about 1/gap ticks, while a split takes at least ln2/(H a) = 3.6e4 cell times. The fold finishes about 2e4 times within one split. This is the lattice eta problem of inflaton-design C1. In field form eta = M_P^2 V''/V, so the fold coupling cancels and only the stiffness and the cell in Planck units remain.

E. Reheating. The fold rule is >= 0 and vanishes only on folds. Every bit of plateau energy that leaves the coherent mode therefore sits in misfolds: domain walls, whose sites are free, so they are matter in the neighbourhood reading. Full conversion gives at most 2 V0 / gap_pair = 0.36 walls per site, a dense gas at the fold scale, which splits then dilute as matter.

## Derivation

A1: S_a.S_b = swap/2 - 1/4, and P_3/2 = 1/2 + (2/3)(S_a.S_b + S_b.S_c + S_a.S_c); summing the stars counts each nearest-neighbour pair twice and each next-nearest pair once. A2: the uniform state is the M = 0 member of the total-spin N/2 multiplet, in which every triple has spin 3/2. A3: P_fold is a spectral projector of the rule.

B1: per k, |<+|dH|->|^2 = e^2/E^2 for a gap term anticommuting with the kinetic term, and the energy denominator is (2E)^3. Substituting e = m x gives Z = rho0 m^(d-3) int x^(d+1) / (1 + x^2)^(5/2) dx, which converges at large x for d < 3; sympy evaluates the integrals.

C1: Jordan-Wigner on an open chain gives S+_x S-_(x+2) = c+_x (1 - 2 n_(x+1)) c_(x+2). With bipartite hopping at half filling, same-sublattice correlators vanish, so the next-nearest correlation is 2 g_s g_w. The stiffness per site is (1/2) avg sin^2 k / |f|^5 with f = t1 + t2 e^(ik). Near k = pi this gives 1/(24 pi delta^2).

C2: write u = ln delta and W = V0 - V. Then V_chi = -W_u/p, with p = zeta e^u sqrt z, and N = int V p^2 / W_u du. In the pole regime, N = V0 s^2 / (4 c delta^2 L^2) with s^2 = zeta^2 z0, so eta = -1/N and eps = s^2 / (8 N^2): the attractor result. C4 follows from P = V/(24 pi^2 eps M_P^4), with V0/M_P^4 = gamma V0 sqrt3 2^(-4r) and s^2 = z0 2^(-2r)/sqrt3.

D1: W = c2 m^2 and Z = z1 (ln(2 Lambda/m) - 4/3), which give N = zeta^2 V0 z1 L^2 / (4 c2) and eta = -sqrt(c2 / (V0 zeta^2 z1 N)). The quadrature joins these asymptotic forms to within 1e-3.

## Checks

The runner prints 13 checks:
- A1-A3: exact (ED);
- B1: exact (sympy);
- B2, C2, D1: finite diagnostics;
- C1: exact quadrature with two cross-checks;
- C3-C5: exact arithmetic;
- D2, E1: estimates.

## Estimates against measurement

- Index. In the pole case n_s = 1 - 2/N*: 0.963 at N* = 55, -0.4 sigma from Planck and about -3.5 sigma from ACT with DESI, unless N* is about 77. With the update's Dirac sea (no pole), eta is about -0.9 or worse: excluded by orders of magnitude.
- Tensors. r = 2 zeta^2 z0 / N^2 is below 1e-5 at every rung, far under 0.036.
- Amplitude. It needs the fold at about rung 20 (blocks of about 1e6 cells) for coupling 1. That is a supplied number.
- Running. -6.6e-4, against the measured -0.0045 +- 0.0067.

## Boundary

Supplied:
- the star rule (not CL-1's cube tick);
- the dimer path and its one-loop stiffness as the fold's slow manifold and kinetic term;
- J a = sqrt 3;
- M_P a = 1 at the flat rung (unit map);
- the fold rung and the coupling gamma;
- N* = 55;
- the Dirac ball cutoff and m_f = 1;
- semiclassical FRW with Hubble friction acting on the fold mean field (no lattice mechanism for that friction is derived; the split's carriage map would have to provide it);
- the split carrying the parent's fold order.

Forced, given those:
- the Majumdar-Ghosh identity;
- the uniform-odds top as an exact eigenstate;
- conservation of the fold weight;
- Z ~ m^(d-3);
- the pole in 1D and on a nested surface, and its absence at Dirac points;
- n_s = 1 - 2/N with r ~ 2 zeta^2 z0/N^2 in the pole case;
- q = 1/8 + 7x/8;
- the fast roll with the update's Dirac sea.

Not computed:
- a 3D star rule's own potential;
- fold selection among the many 3D coverings;
- quantum diffusion near the top;
- the CL-3 vacuum standard's reading of the plateau (it gravitates only as a departure from the folded vacuum, and between splits it scales like the cell, l^-4, so a log-periodic ripple of period ln 2 is expected);
- reheating dynamics beyond the energy bound.

Not claimed: that a fold cannot be the clock. It can, but only if the sea it folds has a gapless surface. CL-1's sea has only Dirac points.

## Candidate law text (tested, not adopted)

> CL-F (fold). "The first odds are the unfolded sea. Roles are read from the zero-phase states of a uniform star rule acting with coupling gamma on the blocks of rung r_f, and a split carries its parent's fold order to its children."

Verdict: with CL-1's sea as the unfolded state, the fold is fast (D1, D2). With uniform odds as the first odds, the fold rule never starts it, and the hop removes it in about a tick (A2). It works only if the unfolded sea in the fold channel is critical on a surface (B1, C2), and then it is in the exponential-plateau class.

Smuggling check:
- The pole comes from the sea's gapless surface, which is not CL-1's band, so a working version needs a new rule that makes the pre-fold sea nested (for example, a pre-role tick with only axis hops, whose half-filled sea is the nested cubic sea of B2). That rule is untested here and is not law text.
- gamma and r_f are fitted to A_s.
- N* is supplied.

## Dependencies

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [candidate_laws](CANDIDATE_LAWS.md)
- Used:
  - the neighbourhood-roles note (star rule, bound-pair folds, misfolds as free sites);
  - the split-time cascade note (lam = 2^(n_s - 1), self-similar cascades);
  - the record-clock note (records give no clock);
  - inflaton-design B1 and C1 (power law from a fixed per-split fraction; the lattice eta problem);
  - act-tilt, PR #9918 (every exponential plateau gives 1 - 2/N);
  - inflaton A1 (H a < 1.93e-5);
  - the register's unit map (M_P L = 1) and its Dirac light band.
- Narrowed: the owner's fold-as-inflaton idea, to a sea that is critical on a surface.

## How to run

python3 scripts/a_fold_is_a_slow_scalar_clock_only_when_the_unfolded_sea_is_critical_on_a_surface_and_the_updates_dirac_sea_makes_it_fast_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120; about 5 s, peak about 190 MB; ends with TOTAL: PASS=13 FAIL=0.
