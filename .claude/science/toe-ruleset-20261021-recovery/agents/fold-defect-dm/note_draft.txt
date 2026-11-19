---
claim_id: fold_defects_of_the_two_tiling_tick_are_no_dark_matter_because_the_mass_sign_selects_one_gapped_fold_and_a_supplied_fold_sign_register_is_excluded_by_the_domain_wall_bound_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Single-particle two-tiling ticks of CL-1 (cube hop with face phases -1, even step eps - mu/2, odd step eps + mu/2, eps = 0.3, copy mass M, diagonal metric weights) in Bloch form on the 2^3 cell (k grids 6^3, 8^3), on Lx x 2 x 2 slabs with transverse twists (Lx = 32, 48; 8^2 twists) and on the 10^3 torus. Results: (A) law text: mu = mN with m >= 0 and lapse N > 0, so every species' mass angle has one sign in every cube; mu -> -mu is the (1,1,1) image (spectra equal to 8e-16); at fixed sign the vacuum is unique with gap exactly mu, including with M in [0, 0.25] and random diagonal metrics (gap/mu = 1.000 on 8 samples); the parameter space is contractible, so no fold wall, string or point is topological; the other fold costs ~1.3-1.5 mu^2 per site; a fold offset on the fixed Z^3 has no Burgers charge, and the two tilings admit no three-domain junction. (B) With a supplied mu-sign profile: a sharp wall binds 4 zero modes at zero transverse momentum (2+1D cones of the two copies); a staggered on-site phase D, a second mass direction adding in quadrature (gap 0.13826 at mu = D = 0.1), lets the wall unwind with gap >= 0.11; a closed cubic bubble (side 4) has no zero mode (lowest 0.097); the sharp-wall tension is sigma = c mu^2 per site^2, c = 0.40-0.69; the Fermi-ball binding ratio (12 pi sigma/g)^(1/3)/mu is 2.7-6.4 > 1 at every mu. (C) Estimates: with the supplied unit map, sigma^(1/3) = 8e3 GeV (electron), 0.17 GeV (0.05 eV neutrino), against the domain-wall bound (1 MeV); the passing re-seeds the same fold, so splits make no Kibble-Zurek defects. No dark-matter species from fold defects."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_sign_of_the_mass_angle_picks_one_cube_fold_of_the_two_tiling_tick_and_its_misfolds_are_the_matter_fermions_while_dimer_resonance_and_symmetric_window_rules_leave_the_3d_fold_unselected_bounded_theorem_note_2026-10-22
  - the_copy_sign_is_exact_only_at_rest_and_no_copy_edge_or_split_structure_of_the_candidate_laws_gives_a_stable_cold_link_free_species_bounded_theorem_note_2026-10-22
runner: scripts/fold_defects_of_the_two_tiling_tick_are_no_dark_matter_because_the_mass_sign_selects_one_gapped_fold_and_a_supplied_fold_sign_register_is_excluded_by_the_domain_wall_bound_2026_10_22.py
---

# Fold defects of the two-tiling tick are no dark matter, because the mass sign selects one gapped fold and a supplied fold-sign register is excluded by the domain-wall bound

Claim type: bounded_theorem. The candidate-law register has zero premise weight. Axiom text is unchanged.

## Question

The fold-selection note (PR #9978) found that the sign of the mass angle mu picks the odd-cube fold, that point misfolds are the matter fermions, and that walls across which mu flips carry gapless 2+1D fermions. This note asks whether any fold defect the laws already make is a dark-matter species without a hand-added parity:
- (a) closed mu-sign wall bubbles: a conserved index from their bound fermions, their mass against radius, whether they are link-blind;
- (b) wall junctions;
- (c) translation defects (dislocations) of the fold crystal;
- (d) abundance from the split cascade (Kibble-Zurek), against the domain-wall, cosmic-string and CMB bounds.

The measured dark matter is cold, stable, link-blind, with Omega_c h^2 = 0.120.

## Results

### A. The fold's vacuum manifold under the laws

**A1 [T].** Law text: a species of mass m applies its tick with mass angle mu = mN, and the lapse N = sin(eps0)/(sqrt3 rms sqrt(gamma^ii)) is positive in every cube and half-tick. So mu has one sign in every cube for every species. The other fold is the vacuum of -mu, the (1,1,1) image (equal spectra to 8e-16), which the update does not contain at fixed sign. At fixed sign the vacuum is unique with gap exactly |mu|. The fold is explicitly selected, not spontaneously chosen.

**A2 [D+T].** Over the parameters CL-1 lets vary in space (mu > 0, the copy mass M, diagonal metric weights) the tick stays gapped, with gap/mu = 1.000 on 8 random samples. That parameter space is a product of intervals and the convex cone PD(3) (dark-matter-candidate D1), so it is contractible. Any register texture deforms to the uniform vacuum without closing the gap: pi_0 = pi_1 = pi_2 = 0. No fold wall, string or point is topological.

**A3 [D].** The other fold is not a second vacuum. Under the +mu tick the -mu vacuum costs 1.54, 1.47, 1.33 mu^2 per site (mu = 0.05, 0.1, 0.2). A wrong-fold region is an excited state with a volume cost. Both the volume cost and the wall cost (B4, about 0.6 mu^2 per site^2) are positive, and the volume term dominates beyond about 0.4 sites, so a wrong-fold bubble shrinks at every size.

**A4 [T].** A fold offset is a single-valued function on the fixed Z^3 sites, so its jumps sum to zero around every loop (checked: 0 nonzero plaquette sums for 2- and 8-offset fields). The fold has no Burgers charge. A dislocation of the fold would need a dislocated lattice, which the Lattice axiom forbids. CL-1 has two tilings, so no three-domain junction exists (0 junction plaquettes). Even a fold read from neighbourhoods with all 8 offsets (owner scope) has junction lines only where walls meet (198 on a random 6^3 field), never free strings. So (b) and (c) reduce to walls.

### B. If the mass sign were a register (supplied profiles)

These checks take a sharp mu-sign profile that no law produces, to see what such a rule would give.

**B1 [D].** A sharp wall (M = 0, mu = +-0.2, Lx = 32) binds 4 zero modes per wall at zero transverse momentum. They disperse linearly (|w| = 0.0065 and 0.0130 at twists 0.05 and 0.1): two 2+1D Dirac cones, one per copy. This is the Jackiw-Rebbi structure that fold-selection C8 saw.

**B2 [D].** The index is not protected. A staggered on-site phase D (-1)^(x+y+z) is a second Dirac-mass direction adding in quadrature (gap 0.13826 at mu = D = 0.1, i.e. sqrt(0.1^2 + 0.0955^2), matching nested-prefold-sea B). A wall that rotates (mu, D) from (m, 0) to (-m, 0) keeps the gap at 0.114 (width 4) and 0.150 (width 8), against 0 for the sharp flip. The bound modes leave.

**B3 [D].** A closed cubic bubble of -0.3 inside +0.3 (side 4, 10^3 torus) has no zero mode. Its lowest level is 0.097, with 56 in-gap states. The 2+1D Dirac index on a closed wall without link flux is zero. So bound fermion number is not a defect number. It is the species' own mode number, carrying the species' link charges (q times number commutes with the hops), so a bubble is link-blind only for a link-free species.

**B4 [D].** The sharp-wall tension is sigma = c mu^2 per site^2, with c = 0.693, 0.597, 0.510, 0.398 at mu = 0.05, 0.1, 0.2, 0.4. c rises slowly as mu -> 0 (about +0.1 per halving). The thin wall is UV-sensitive, sigma ~ m^2/a rather than m^3.

**B5 [T+D].** Fermi-ball test (the literature's wall-bubble stabilised by trapped fermions). N massless wall fermions in g = 2 cones on a sphere of radius R give E = 4 pi sigma R^2 + (2/3) N^(3/2) / (sqrt(g) R). The minimum is E/N = (12 pi sigma/g)^(1/3). They stay bound only if E/N < |mu|. The ratio is 6.39, 4.83, 3.64, 2.66 at the four mu: it fails everywhere. It would need mu > 12 pi c/g ~ 5, beyond the tick's 2 eps = 0.6. The fermions escape into the bulk, and an uncharged bubble shrinks at the speed of light.

### C. Abundance against measurement (estimates)

**C1 [law text].** The passing carries the update's vacuum onto the children's update's vacuum, and each excitation onto the lowest excitation of the same charges. So a split re-seeds the same fold, and the split cascade makes no fold defects. The Kibble-Zurek density is zero, because no symmetric choice is made in causally separate regions.

**C2 [E].** Suppose a fold-sign register were supplied. Use the unit map (1 rad per tick = 2.1e18 GeV, 1/a = 2.43e18 GeV) and c = 0.69. Then sigma^(1/3) = 8.0e3 GeV for the electron, 0.17 GeV for a 0.05 eV neutrino, and 3.9e7 GeV for the top quark. The domain-wall (Zel'dovich-Kobzarev-Okun) and CMB bound is sigma < (1 MeV)^3, which these exceed by 5e20 and 5e6 respectively. A scaling network would have Omega_w ~ 8 pi sigma/(3 M_P^2 H0) = 2e16 and 2e2. Walls have w = -2/3, so they are not cold matter at any abundance. The cosmic-string bounds (G mu_s < 1e-7 to 1e-11) are not reached, because no free strings exist (A2, A4).

## Verdict

**No.** The rules make no fold defect that is a dark-matter species:
- The mass sign is not a register, so the fold has one gapped vacuum over every edge and copy-mass texture. Nothing is topologically stable except what the laws already conserve. The fold's only localized excitations are the matter particles (fold-selection C7), which carry their species' link charges.
- Supplying a fold-sign register would make walls, but their index unwinds through a second mass direction. Closed bubbles bind nothing topologically, Fermi balls never bind, and the tension overshoots the domain-wall bound by at least 6 orders for every massive species.

This narrows fold-selection C8: its wall misfolds are configurations of a supplied mass profile, not states of the update. It extends dark-matter-candidate D (geometry and split defects) to the fold's own defects.

## Candidate law text

None is proposed for adoption. A derived consequence line for the register:

> Fold defects. With every mass angle of one sign, the fold has one vacuum, joined to every edge and copy-mass value without closing its gap, so the laws make no stable fold wall, string or point beyond the matter particles, and the passing re-seeds the same fold.

The replacement rule that would make walls, a fold-sign register, is excluded by the domain-wall bound. The rule-level route to dark matter stays the link-free species with a conserved number (#9877, #9946). Every route found so far still supplies that number.

## Smuggling review

**Supplied:**
- eps = 0.3, the mu values, M and the metric samples;
- the sharp and rotating mu-sign profiles (no law produces them);
- the staggered phase D (on-site and admissible, but in no law; nested-prefold-sea gets it from a supplied repulsion);
- the principal-branch Floquet energy used for tensions and costs;
- the cubic bubble shape;
- the thin-wall Fermi gas and g = 2;
- the unit map, M_P, H0 and the measured bounds.

**Forced, given these:**
- one sign of mu per species (law text);
- a unique gapped vacuum over a contractible parameter space;
- no Burgers charge on a fixed lattice;
- no three-domain junction with two tilings;
- an unprotected wall index once any second mass direction exists;
- a zero index on closed walls;
- sigma ~ c mu^2;
- Fermi-ball failure;
- zero defect density from the passing.

**Not derived:**
- the analytic form of c(mu) (logarithm or not);
- the closed-bubble level against radius beyond side 4;
- bubbles threaded by link flux (a monopole inside would bind zero modes, but the object would then be the magnetic relic of #9946, not dark);
- the zero-mode count with the copy mass. At M = 0.5 the k = 0 zero modes lift to 0.037, and lower minima appear at nonzero twist (0.0009 at Lx = 48), probably a displaced light-copy cone. This was not resolved and is not used.

**Lopsidedness:** none added. The selector is the sign of the mass, already in CL-1.

## Dependencies

- Minimal axioms (Lattice, one qubit per site, admissibility, records), unchanged.
- Candidate-law register: CL-1's tick, mass angle, lapse, copy mass and split passing. Zero premise weight.
- Fold-selection note (PR #9978): the selector, the misfolds and the wall modes, narrowed here.
- Dark-matter-candidate note: the PD(3) convexity and the unit map, cited.
- Mirror-dark-matter note (PR #9988) and #9877, #9946: the remaining link-free-species slot.
- Nested-prefold-sea note (PR #9982): the staggered-phase mass direction.

## How to run

```
python3 scripts/fold_defects_of_the_two_tiling_tick_are_no_dark_matter_because_the_mass_sign_selects_one_gapped_fold_and_a_supplied_fold_sign_register_is_excluded_by_the_domain_wall_bound_2026_10_22.py
```

Needs numpy and scipy. It is self-contained and declares `AUDIT_TIMEOUT_SEC = 120`. It runs in about 15 s with about 206 MB resident, prints about 4.3 kB and ends with `TOTAL: PASS=10 FAIL=0`. Its random draws are seeded, and two runs (direct, and via `scripts/runner_cache.execute_runner` on an origin/main worktree) gave identical output.
