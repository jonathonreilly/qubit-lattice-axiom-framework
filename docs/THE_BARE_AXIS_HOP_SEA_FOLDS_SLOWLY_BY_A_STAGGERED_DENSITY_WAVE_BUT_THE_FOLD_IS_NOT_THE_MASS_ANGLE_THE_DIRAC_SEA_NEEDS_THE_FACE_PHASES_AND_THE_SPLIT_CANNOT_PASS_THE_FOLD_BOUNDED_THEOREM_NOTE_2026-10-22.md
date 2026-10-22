---
claim_id: the_bare_axis_hop_sea_folds_slowly_by_a_staggered_density_wave_but_the_fold_is_not_the_mass_angle_the_dirac_sea_needs_the_face_phases_and_the_split_cannot_pass_the_fold_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Single-particle two-tiling ticks in Bloch form (2^3 cell; eps = 0.3; k grids 6^3 to 24^3), the cube's 4096 sign fields, Hartree mean field for spinless fermions with nearest-neighbour repulsion g on the simple-cubic half-filled sea (elliptic density of states), slow roll on the computed potential and cranking mass, a discrete stationary-phase check of friction, and a 4^3-supercell child sea. Results: (A) every bond lies in exactly one cube of one tiling, so the bare axis hop's two-tiling tick is a split of the 6-NN hop. Its gapless set stays a nested surface (box count 4.5; 4.2 at mu = 0.1), while CL-1's spin-3/2 tick has Dirac points and the same quasi-energies as the Kogut-Susskind pi-flux tick (1e-15). R^2 = 1 holds for exactly the all-minus-face class (128 of 4096 fields). The Dirac sea comes from the face phases, not from the folding; pi flux lowers the half-filled energy from -1.00244 to -1.19380 per site. (B) The staggered density wave at (pi,pi,pi) gaps the nested sea at every g > 0 (ln D* slope -1.168 = -1/(6 rho0)); the Dirac sea needs g > 0.732. It is a Dirac mass of CL-1's tick, but it adds to mu in quadrature (0.1383 = sqrt(0.1^2 + 0.0955^2)), selects no tiling (|Var N_even - Var N_odd| < 1e-14) and leaves every site free. (C) Cranking mass M -> rho0/(12 D^2) and released energy W ~ D^2 ln^2(1/D) give n_s = 0.9631-0.9634 at N* = 55 for g = 0.5 and 1 at rungs 0, 2, 4, with r = 6e-6 to 2e-8 and exit before D*. A_s fixes the rung at 18.6 (g = 0.5) or 20.4 (g = 1). (D) A phase per proper 4-volume gives friction 3H exactly (1.0015 at H tau = 1e-3); a phase per cell gives 27 ln2/14 = 1.34 off. CL-3's 'update's vacuum' (negative quasi-energies filled) is the unfolded sea, so the plateau has zero departure. (E) The parent nesting vector never lifts to the child's, and a passed density wave has zero overlap with the child's fold coordinate and leaves the child gapless: children are born unfolded. Supplied: eps, g, the Hartree reading, J a = sqrt3, M_P a = 1, N* = 55, semiclassical FRW."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_bare_axis_hop_sea_folds_slowly_by_a_staggered_density_wave_but_the_fold_is_not_the_mass_angle_the_dirac_sea_needs_the_face_phases_and_the_split_cannot_pass_the_fold_2026_10_22.py
---

# The bare axis hop's sea folds slowly by a staggered density wave, but the fold is not the mass angle, the Dirac sea needs the face phases, and the split cannot pass the fold

Claim type: bounded_theorem. The candidate-law register has zero premise weight, and the axioms are unchanged.

The fold-inflaton note found that a fold is a Starobinsky-class clock only if the sea before the fold is critical on a whole surface. CL-1's sea is Dirac-point critical, so it rolls fast. This note tests whether a principled rule gives a nested sea before roles exist and the Dirac sea afterwards. It asks four questions:
- (a) Does folding the bare axis hop into cubes give the Dirac band?
- (b) Is the nested sea's (pi,pi,pi) instability the cube fold and the mass angle?
- (c) Does CL-3 supply Hubble friction?
- (d) Can the split pass the fold order to the children?

## Results

### A. The bare axis hop and the Dirac band (question a)

**A1 [T]. The cube tick is a split of the 6-NN hop.**
- A bond along axis i at x lies in a cube of the even tiling exactly when x_i is even, and otherwise in exactly one odd cube.
- So the two-tiling tick of the bare axis hop is a split of the 6-NN hop.
- The opposite sign of CL-1's odd step is the gauge prod_i f(x_i) with f = (1, 1, -1, -1).

**A2 [T]. Cube level.**
- R^2 = 1 holds for exactly the 128 sign fields of the all-minus-face class: Cauchy-Schwarz, as in the main flux-sector note (HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR..., Theorem 1).
- The bare hop has faces +1 and spectrum +-sqrt3, +-1/sqrt3, so it is not a reflection.
- CL-1's spin-3/2-overlap tick has the same quasi-energies as the Kogut-Susskind pi-flux (eta-sign) tick, to 1e-15 at mu = 0 and 0.15. CL-1's R is the staggered pi-flux hop up to gauge.

**A3 [D]. Box count of the gapless set** (n = 12 -> 24; a ratio of 4 means a surface, 1 means points).

| Tick | Count | Gapless set |
|---|---|---|
| Bare | 436 -> 1972 | surface |
| Bare, mu = 0.1 | 462 -> 1938 | surface |
| CL-1 | 1 -> 1 | points |

The tick's chiral symmetry (Gamma anticommutes with both steps) keeps the band nested, w -> -w at the nesting vector. The tiling's mass angle does not gap it.

**A4 [T+D]. Answer to (a): no.** Folding the 6-NN sea into 2^3 cubes with even/odd steps keeps the nested surface. The Dirac points come only from the face phase -1 (pi flux), which is what R^2 = 1 forces. The half-filled energy per site (hop 1) is -1.00244 at zero flux and -1.19380 at pi flux. That is Lieb's flux phase, and pi flux is 0.19 lower.

### B. The (pi,pi,pi) instability (question b)

**B1 [T+D]. Gaps.** The staggered phase m (here 0.1 per tick) gives these gaps:
- it gaps the bare tick's nested surface fully (0.0868);
- it is a Dirac mass of CL-1's tick (0.0955);
- with mu = 0.1 the gaps add in quadrature: 0.1383 = sqrt(0.1^2 + 0.0955^2).

So m and mu are two anticommuting masses (a chiral pair), not one.

**B2 [T+D]. No mixing.** The density-wave vacuum binds neither tiling: Var N_even = Var N_odd to 5e-15 at m = 0.2 and 0.6, in both ticks. The mu vacuum has zero staggered density. No site is definite, so in CL-2's bound-pair reading every site is free.

**C2 [T+D]. Instability.** Perfect nesting gives the gap equation 1 = 3g int rho/E a solution at every g > 0, with ln D* = -1/(6 g rho0) + c. The slope is -1.168 against the predicted -1.168, and rho(0) = 0.14267. The pi-flux sea folds only above g_c = 1/(3 <1/eps>) = 0.732.

**Answer to (b): partial.**
- Confirmed: perfect nesting does make any repulsion gap the sea at (pi,pi,pi), and the same operator is a Dirac mass after the flux.
- Refuted: it is not the even/odd cube fold and not the mass angle. It selects no tiling at any computed strength, and it is the chiral partner of mu.

The hoped-for unification of fold selection, copy mass and inflation therefore fails at the identification step.

### C. The 3D nested sea's own potential

The fold is the Hartree Slater state of h + D(-1)^x with spinless nearest-neighbour repulsion g.

**C3 [T+D]. Pole and plateau.**
- The cranking mass M = 2 sum |<n|dH|0>|^2/dE^3 per site has the pole M -> rho0/(12 D^2) (to 1e-7).
- The released energy is W = V0 - V ~ D^2 ln^2(1/D), tending to 3 g rho0^2 D^2 ln^2.
- This is the 1D toy's exponential-plateau class, now computed in 3D.

**C4 [D]. Slow roll.** Take chi = zeta int sqrt(M) dD with zeta = (J a)^-1/2/(M_P a_r), J a = sqrt3, M_P a = 1 at the flat rung, and N* = 55.
- n_s = 0.9631 (rung 0), 0.9633 (rung 2) and 0.9634 (rung 4), for both g = 0.5 and g = 1.
- r = 6e-6, 4e-7 and 2e-8.
- eps reaches 1 at D_end/D* = 0.01-0.08, which is the graceful exit.

**C5 [T+E]. Amplitude.** A_s = 2.1e-9 fixes the rung, given g:

| g | V0 per site | D* | Rung | H/M_P | r |
|---|---|---|---|---|---|
| 0.5 | 0.0145 | 0.64 | 18.6 | 5.7e-13 | 3e-17 |
| 1 | 0.167 | 2.30 | 20.4 | 1.7e-13 | 3e-18 |

### D. Hubble friction (question c)

**D1 [T+D]. Friction needs the 4-volume weight.**
- A fold phase summed per proper 4-volume (weight a^3, as in CL-3's total phase) is stationary only if (a^3 chi')' = -a^3 V'. That is friction of exactly 3H: the discrete terminal velocity is 1.0015 times -V'/3H at H tau = 1e-3.
- A phase per cell, with the cell count rising x8 at each split and fixed in between, damps only at splits. Its cycle-mean drift is 27 ln2/14 = 1.34 times -V'/3H.
- Friction therefore needs the proper-4-volume weight, with edges growing between splits.

**D2 [R]. The vacuum standard blocks the plateau.** CL-3 reads departures from "the update's vacuum", which CL-1 defines as every negative-quasi-energy mode filled. For the bare tick that state is the unfolded nested sea. So the plateau's departure is 0: H = 0, there is no friction and there are no e-folds, and the folded vacuum sits at -V0.

**Answer to (c).** CL-3's phase-per-4-volume form supplies the friction, but only if its vacuum standard is read from the folded (interacting lowest) state. Read as written, it removes the inflation.

### E. Passing (question d)

**E1 [T]. Momentum mismatch.**
- The parent nesting vector pi/a_p lifts to pi/a_p or 3pi/a_p modulo the child's 4pi/a_p, and never to the child's 2pi/a_p.
- For every coincident nesting offset, the child staggering (-1)^|y| is constant on the parent sites.
- So a parent density wave passed through parent sites has zero overlap with the child's fold coordinate: the integer overlap on the 4^3 supercell is 0.

**E2 [D]. The child's nested sea** (40^3 sites).

| D | Child's own wave: dE/D^2 | Gap | Passed pattern: dE/D^2 | Gap |
|---|---|---|---|---|
| 0.4 | 0.235 | 0.400 | 0.094 | 0.030 |
| 0.1 | 0.329 | 0.100 | 0.089 | 0.006 |

The child's own wave has the log and the full gap. The passed pattern has no log and leaves the child gapless.

**Answer to (d): no.** CL-1's passing is momentum-preserving: it carries each excitation to the children's lowest excitation of the same momentum. So a cell-scale fold reaches the children as non-nested particle-hole pairs (heat), and the children are born unfolded: x = 1 in fold-inflaton's q = 1/8 + 7x/8, which re-seeds the plateau.

A fold fixed at a comoving rung avoids the mismatch, but its vacuum energy then scales like l^-4: it is not a plateau.

## Verdict

**Positive, conditional:** the bare axis hop's nested sea plus any repulsion is a Starobinsky-class clock. Its numbers are n_s = 1 - 2/N, tiny r and a graceful exit, now with the 3D potential and stiffness computed rather than chosen.

**Negative:**
- (a) The fold does not create the Dirac sea; the face phases do.
- (b) The density wave is not the mass angle.
- (c) The friction works only with a re-read vacuum standard.
- (d) The split cannot pass the fold.

A working ruleset would need three new clauses. None is adopted here.

1. A trigger that turns the face phases on after the fold. The density-wave fold binds no site, so "phases once bound" never fires. Lieb's energy rule would give pi flux from the start, which leaves no nested era.
2. CL-3's vacuum read as the folded lowest state, not the filled-negative-modes state.
3. A channel-matched passing: the parent's fold amplitude written into the child's own nesting channel. This is not momentum-preserving, and it chooses the clock.

## Candidate law text (tested, not recommended)

> CL-1 (pre-role clause). "While no site of a cube is bound, the cube applies the bare axis hop (its edge hops with no overlap phase); a cube applies R only when its sites are bound."
> CL-3 (vacuum clause). "The vacuum is the update's lowest state, including its folds."
> Split (fold passing). "A parent's fold amplitude passes to the children's fold of the same kind at the children's own nesting vector."

Smuggling check:
- Clause 1 gives the nested sea (A3), but nothing then switches on the phases: the density-wave fold binds nothing (B2).
- Clause 3 is not momentum-preserving (E1), and it writes the clock into the passing.
- g and the fold rung are fitted to A_s, and N* = 55 is supplied.

Lopsidedness: none new. The density wave's sign is a spontaneous Z2, broken by the initial odds.

## Smuggling review

Supplied:
- eps = 0.3;
- Hartree (no Fock term) spinless nearest-neighbour repulsion g = 0.5 or 1;
- the staggered phase added per half-tick;
- the eps -> 0 static reading for energies (a tick has no energy);
- J a = sqrt3;
- M_P a = 1 at the flat rung;
- N* = 55;
- semiclassical FRW with H fixed by V0.

Forced, given those:
- the bond split;
- R^2 = 1 if and only if pi flux;
- CL-1's tick being the Kogut-Susskind band;
- the surface versus the points;
- the gap at any g;
- the quadrature of m and mu;
- the absence of tiling selection;
- M ~ 1/D^2;
- n_s = 1 - 2/N;
- 3H friction from the 4-volume weight;
- the Q mismatch.

Not computed: quantum diffusion near the top, the Fock term, the interacting tick (beyond mean field), and the flux as a dynamical register field.

## Dependencies

- Used: fold-inflaton (B1 pole theorem, C5 re-seeding, slow-roll dictionary); fold-selection-3d (two-tiling tick, cube fold by sign of mu); neighbourhood-roles (bound-pair reading).
- On main: HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02 (cube Cauchy-Schwarz; Lieb 1994).
- Narrows: the fold-inflaton smuggling-check suggestion of a pre-role axis-hop tick. It works for the roll, but not for the identification with mu or for the passing.
- Open PR: #9979 (fold-inflaton).

## How to run

python3 scripts/the_bare_axis_hop_sea_folds_slowly_by_a_staggered_density_wave_but_the_fold_is_not_the_mass_angle_the_dirac_sea_needs_the_face_phases_and_the_split_cannot_pass_the_fold_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120. It takes about 5 s, peaks at about 250 MB, prints 5932 characters and ends with TOTAL: PASS=15 FAIL=0. It was checked through scripts/runner_cache.execute_runner from a temporary origin/main worktree (status ok).
