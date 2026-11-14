---
claim_id: the_gapped_mirror_keeps_only_a_number_shared_with_light_matter_and_its_lightest_state_is_charged_so_it_gives_no_dark_matter_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For one mirror 16 (two spin components per cell) with the Spin(10) pair square, species-diagonal hops and SM gauging: (A) the species phases that keep every pair-square monomial form exactly U(1)_Y x U(1)_X, with X = 5(B-L) - 4Y = (1,1,-3,-3,1,5) on (Q,u^c,d^c,L,e^c,nu^c) and no discrete remnant (Smith normal form); mode number changes only by 4, and its Z4 = i^N equals exp(i pi X/2), the Spin(10) centre inside U(1)_X; mirror B' and L' are broken, B'-L' is kept; X has no anomaly with SM gauge fields, itself or gravity; with a species-diagonal light-mirror bilinear on all six species only U(1)_Y x U(1)_X(total) survives, so the mirror's number is shared with light B-L; with bilinears on a subset S of the species the group has dimension 8 - |S| (one nu^c bilinear leaves 7), and a mirror-only U(1) or a finite mirror-only group (Z2 to Z6) survives on 23 of the 62 proper subsets. (B) The CL-1 cube tick's one-body commutant is 16-dimensional at K = 0 and the identity at three random K: no mirror, copy or turn number exists for moving states, and the tick, which acts on the cell index alike for every species (supplied model), supplies the bilinear for all six species; an exact one-body mirror number would leave the light sector a lattice theory by itself, vector-like by Nielsen-Ninomiya (1D witness: 20 random bands, net chirality 0). (C) SM singlets: none in the 10, one in the 16 (nu'^c, X = 5), two in the 45, one in the 54 (X = 0); 16 x 16bar = 1 + 45 + 210 and 10 x 10 = 1 + 45 + 54, so in the Spin(10)-symmetric phase nu'^c has zero photon and Z couplings to all orders in the mirror dynamics, while the 10's neutral members have T3 = +-1/2. (D) From the cited one-cell chains: the 10 (spin 0, X = +-2) at 19.07 g lies below the 16 (33.58 g), so the lightest mirror state is SM-charged and nu'^c (Delta_f) is the lightest SM singlet. The so(12) chains are cited from PR #9910 and not rechecked beyond reproducing E0 and the gaps from the cited coefficients; a Casimir term lambda C_Spin(10) with lambda >= 0 keeps the 10 below the 16 (a negative lambda can reverse them). A shared X is not a decay theorem: the absence of a separately conserved mirror label gives no on-shell final state, matrix element or rate (witness: H = [[1,1],[1,1]] does not commute with the label projector diag(1,0), yet its eigenstate (1,-1)/sqrt2 is stationary). Mirror lifetimes are conditional estimates for an open channel nu'^c -> nu^c + graviton with the supplied vertex and width; the lattice decay channel, the band minima and the graviton-coupling normalisation are not computed, so no dark-matter exclusion is claimed. Estimates against measurement use supplied inputs. Supplied model, finite diagnostic."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - spin10_pair_square_gives_unique_gapped_symmetric_mirror_cell_ground_state_bounded_theorem_note_2026-10-21
  - the_copy_sign_is_exact_only_at_rest_and_no_copy_edge_or_split_structure_of_the_candidate_laws_gives_a_stable_cold_link_free_species_bounded_theorem_note_2026-10-22
  - the_mirror_pair_condensate_breaks_the_weak_group_at_its_own_scale_and_its_only_vacuum_angle_runs_to_colour_breaking_bounded_theorem_note_2026-10-22
runner: scripts/the_gapped_mirror_keeps_only_a_number_shared_with_light_matter_and_its_lightest_state_is_charged_so_it_gives_no_dark_matter_2026_10_22.py
---

# With all six species mixed by the tick, the gapped mirror keeps only a number shared with light matter, and its lightest state is charged in the atomic limit; no mirror decay channel is computed

Claim type: bounded_theorem.
Primary runner: `scripts/the_gapped_mirror_keeps_only_a_number_shared_with_light_matter_and_its_lightest_state_is_charged_so_it_gives_no_dark_matter_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its lead chirality route gaps the mirror family symmetrically (SMG) with a cell-local Spin(10)-singlet quartic, the pair square. Measured Higgs data already require that phase rather than the pair-condensed one (mirror-condensate-ew, PR #9974). This note asks whether that one mechanism also gives the dark matter: in an SMG phase every mirror excitation is a gapped composite, and the mirror might carry its own conserved number. The copy-sign note (dark-matter-candidate) found no stable link-free species in CL-1 to CL-3, because the copy sign is exact only at rest and copies share link charges. The question is whether SMG changes that. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

Repo check: origin/main has no note on mirror or SMG dark matter. The SMG hits are the Spin(10) atomic-gap note (2026-09-14) and the chirality endpoint-algebra note. Open PRs used: #9910 (one-cell pair-square spectrum, whose chains are cited here), #9974 (mirror condensate), #9877 and the copy-sign note (dark-matter slot), and #9985 (far-layer N_eff).

## Statement

A. Symmetries of the mirror 16 with the pair square, species-diagonal hops and SM gauging.

1. Exact. Build Spin(10) on 2^5 modes and take M_a = C Gamma_a on the 16. M_a is symmetric, and sum_a M_a x M_a is Spin(10) invariant. The diagonal phases of the 16 weight states that keep all 40 pair-square monomials form U(1)^5, the Spin(10) torus, with no torsion.
2. Exact. SM gauging and species-diagonal hops commute with the six species numbers, U(1)^6. Of these, the pair square keeps exactly U(1)_Y x U(1)_X, with X = 5(B-L) - 4Y taking the values (1, 1, -3, -3, 1, 5) on (Q, u^c, d^c, L, e^c, nu^c). The Smith normal form has no torsion, so no discrete remnant exists beyond these two U(1)s. This answers "which U(1)s survive": one exact mirror number survives, U(1)_X, which at fixed Y is the mirror's B-L.
3. Exact. Mode number changes by 4 only, so Z4 = i^N survives. Every mode has X = 1 mod 4, so i^N = exp(i pi X/2): the Z4 is the Spin(10) centre and lies inside U(1)_X. It is not an independent protection. Mirror B' and L' are broken separately: L' fully, and 3B' only down to the Z3 that colour already contains. B'-L' is exact.
4. Exact. On one 16, the anomalies SU(3)^2 X, SU(2)^2 X, Y^2 X, Y X^2, X^3 and gravity-X all vanish. The mirror's X therefore also survives electroweak instantons.
5. Exact. Add the light family (a left 16) to the mirror (a right 16). Without mixing, the symmetry is U(1)^6 (light species) x U(1)_Y x U(1)_X(mirror), 8 dimensions. With a species-diagonal light-mirror bilinear on all six species, only U(1)_Y x U(1)_X(total) survives, 2 dimensions. The mirror's number is then the same symmetry as light B-L.
6. Exact (all 63 subsets computed; added 2026-11-14). Partial mixing does not give that result. With bilinears on a subset S of the species the group has dimension 8 - |S|, since each bilinear ties one free light phase to the mirror's (Y_s, X_s) rotation. Negative result, explicit witness: a single nu^c light-mirror bilinear leaves dimension 7, and the five unmixed light phases stay free. The mirror's own X is broken by any one bilinear, because X_s is nonzero for every species. The mirror-only subgroup (trivial on every light mode) is U(1)^(2 - r) with r the rank of the mixed species' (Y_s, X_s): a mirror-only U(1) survives on any single species and on {Q, L}, whose charges are parallel (it is 6Y - X on the mirror). Sixteen other partial sets leave a finite mirror-only group (Z2, Z3, Z4 or Z6; for example Z6 for {e^c, nu^c}). Forty sets, the full set among them, leave none. So the statement "any species-diagonal bilinear leaves only U(1)_Y x U(1)_X(total)" is withdrawn; the result needs all six species mixed.

B. The update shares the mirror's number with light matter.

1. Finite diagnostic (rederives the copy-sign note's A5). Take the CL-1 cube tick at (b, mu, M) = (0.3, 0.4, 0.5). The one-body operators commuting with both half-ticks span 16 dimensions at K = 0: copy sign and turn labels are exact at rest. At three random K they span only the identity. No cell-local mirror, copy or turn number exists for moving states. The labels that pick out "the mirror" (the copy the three-fold turn rotates by e^(4 pi i/3), or the copy sign) are rest labels, so the tick is a light-mirror bilinear at nonzero momentum. In the supplied model the tick acts on the cell index alike for every species, so it supplies the bilinear for all six species and A5's full-mixing case applies; a tick that mixed only some species would fall under A6.
2. Theorem (Nielsen-Ninomiya in a sector; 1D witness checked). Suppose an exact one-body mirror number existed. The light sector would then be a local lattice theory by itself, with exact charges, so it would be vector-like. The register also records that the mirror's zone-corner partners are gapped by the chiral generator only through light-mirror mixing. A separately conserved mirror number and a chiral light family therefore exclude each other in the present content.
3. Exact witness (added 2026-11-14): sharing X is not a decay theorem. B1 and A5 constrain symmetries: they show that no conserved number forbids a mirror state from mixing with light states. They integrate no decay channel, so they give no on-shell final state, no nonzero physical matrix element and no rate. The implication "no separately conserved label, so the state decays" is false in general: H = [[1,1],[1,1]] does not commute with the bare-label projector diag(1,0), yet its eigenstate (1,-1)/sqrt2, with weight 1/2 on each label, is stationary for all t (B3). This witness is about the logical step only; it is not a model of the mirror lattice and does not show that a mirror state is stable.

C. Quantum numbers of the gapped spectrum.

1. Exact. SM-singlet content (colour, SU(2)_L and Y all zero):
   - 10: none.
   - 16: one, nu'^c, with X = 5 and B-L = 1.
   - 45: two, the Y and X generators.
   - 54: one, with X = 0.
2. Exact. 16 x 16bar = 1 + 45 + 210 and 10 x 10 = 1 + 45 + 54 (Casimir multiplicities). The 45 occurs once in each. In the Spin(10)-symmetric phase the hops and the pair square commute with Spin(10), so each band is a whole 16 or 10. By Wigner-Eckart, every gauge-current matrix element inside a band is one form factor times the generator's own eigenvalue.
3. Exact, then. nu'^c has T3 = Q = Y = 0. It therefore has zero photon and Z couplings to all orders in the mirror dynamics: no charge radius, magnetic moment or anapole in the Spin(10) limit. These are induced only at O(alpha/4 pi) by the gauge couplings breaking Spin(10). The 10's two neutral members have T3 = +-1/2, which is a vector Z coupling.

D. Which mirror state is lightest (atomic limit; chains cited from #9910).

1. The chains reproduce E0 = -2 sqrt(11088 + 48 sqrt 21081) g. The chain coefficients are cited from PR #9910, whose note was not found on `main` or this branch, and are not rederived here; D1 checks only that they give the stated E0 and gaps. The levels above it are:
   - the 10 (spin 0, X = +-2) at Delta_b = 19.07 g;
   - 16 + 16bar (spin 1/2) at Delta_f = 33.58 g;
   - the 54 at 42.33 g.
2. Finite. Delta_b/Delta_f = 0.568, and 2 Delta_b = 1.136 Delta_f. The lightest mirror excitation is therefore the 10, which is SM-charged (a Y = +-1/2 doublet pair and colour triplets, with no singlet). The lightest SM singlet is nu'^c at Delta_f. It lies below the two-cell 10 x 10 singlets (2 Delta_b, X = 0) and the 54 singlet, both of which carry no conserved number.
3. Finite. Suppose X were exact. Then each (X, mirror fermion parity, SM charge) sector's lightest state is stable. nu'^c cannot reach another 16 member, because Delta X = 4 costs at least 2 Delta_b, and the 10 is the absolute lightest mirror state. A Casimir term lambda C_Spin(10) with lambda >= 0 raises the 16 faster than the 10 (C(16)/C(10) = 1.25), so it cannot lift the 10 above the 16; a negative lambda below -(Delta_f - Delta_b)/(C(16) - C(10)) = -6.45 g per Casimir unit reverses the order (D3 control), which by itself shows no valid stable spectrum or dark-matter model. The 10 also softens toward the pair condensate as hopping grows (toy-qmc, qmc-face-gapped), which keeps it lightest.

## Estimates against measurement

Supplied inputs: the unit map (1 rad/tick = 2.1e18 GeV); the Kolb-Turner freeze-out formula with sigma v = 4 pi kappa/m^2; the copy-changing vertex g >= 0.30 at recoil (from the copy-sign note) times a quasi-particle weight 1/sqrt2 (#9910 E1); the Z cross-section with xenon N/A; the bounds (approximate).

- Mass scale. With the pair square once per tick, #9910's window puts Delta_f near the cell scale. Mirror-condensate-ew needs at least about 1.5 TeV (symmetric phase, decoupled). The mass of nu'^c is Delta_f(1 + O(alpha/4 pi)), and the 10 lies at 0.57 Delta_f.
- Conditional estimate (narrowed 2026-11-14). If the channel nu'^c -> nu^c + graviton is open, with the supplied vertex and the supplied width Gamma = g^2 m^3/(32 pi M_P^2), then tau ~ 3e6 s at 1.5 TeV, 50 s at 56 TeV and 1e-38 s at 1e18 GeV, and the invisible bound (8e18 s) would need m < 0.1 GeV, below the 1.5 TeV floor. The open channel, the on-shell final state, the lattice matrix element and the graviton-coupling normalisation are not computed (Boundary), so this is not an exclusion. The held text said "excluded at every gap" and "every other mirror state decays to light states carrying the same total X (light B-L) at the cell rate"; both are withdrawn. A shared X only removes a conserved number that would forbid such decays (B3); no rate is computed for any mirror state.
- Thermal relic if the mirror number were exact. Strong annihilation gives Omega h^2 = 0.12 at m = 56 TeV (kappa = 1) or 18 TeV (kappa = 0.1). nu' nubar' -> 10 10bar is open, since 2 Delta_b < 2 Delta_f, so the relic is dominated by the stable 10s:
  - charged members (Q = +-1 and colour triplets) are stable CHAMPs or heavy hadrons, excluded;
  - the neutral complex doublet member has sigma_n ~ 6e-40 cm^2 through the Z, against about 1e-46 (m/TeV) cm^2. U(1)_X forbids the real/imaginary splitting that would remove this, so it is excluded below about 6e9 GeV.
  At the law-fixed cell-scale gap, a thermal mirror overcloses (Omega h^2 >~ 4e25 at 1e18 GeV, unitarity-limited).
- nu'^c itself would be a good WIMP-like state: its Z and photon couplings vanish (C3), and its self-interaction is 4 pi/m^3, about 2e-17 cm^2/g at 56 TeV. With a supplied mirror number it is not the lightest stable mirror state in the atomic limit (D2, D3).
- N_eff. A gapped mirror has no massless state, so Delta N_eff = 0 below Delta, unlike the massless far layers (2.25, #9985). The empty-start condition becomes T_RH << Delta if the mirror is stable, and nothing if it decays.

## Verdict

In the supplied model, SMG adds no conserved number of its own to the copy-sign result once the tick mixes all six species. In isolation it does supply one exact, anomaly-free mirror number, U(1)_X, which contains the Z4 of the quartic. But:
- (i) the tick shares X with light B-L, because the mirror label is a rest label (B1) and the tick mixes all six species alike (A5; partial mixing would leave mirror-only groups, A6). So no separately conserved number protects any mirror state. Whether, and how fast, a mirror state decays needs a channel calculation that is not done here (B3); the lifetimes in the estimates are conditional on an open channel and the supplied width;
- (ii) keeping a separate mirror number would make the light sector vector-like (B2) and undo the doubler gapping, so it conflicts with the chirality route that the SMG mirror exists for;
- (iii) even with a supplied mirror number, the lightest stable mirror states in the atomic limit are the SM-charged 10, not the neutral nu'^c.

This note finds no protected neutral mirror state in the present content; it does not show that the mirror gives no dark matter, because the decay channel is open (narrowed 2026-11-14). What SMG does give for free is a neutral composite with exactly zero gauge couplings in the Spin(10) limit (C3).

## Candidate law text (tested, not adopted)

> "Mirror number. The update keeps the mirror's X separately: no term links a light mode to a mirror mode."

Smuggling check.
- Supplied: the rule itself, a new exact symmetry that the tick does not have (B1). It is the copy parity of the copy-sign note, made continuous.
- Forced given the rule: U(1)_X(mirror) exact and anomaly-free, and nu'^c's zero couplings.
- Fails measurement and the chirality route. B2 (light vector-like, corner partners released) and D3 (stable charged 10s, Z-coupled neutral member) both apply.
- What a working version would need: the bosonic 10 above the fermionic 16. That needs a mirror interaction other than the pair square (a Casimir term with lambda >= 0 does not do it, D3), and it does not cure B2.

## Notes used or contradicted

- smg-verify (#9910): its chains and spectrum are cited, and D1 rechecks them. Its Z4 is identified here as the Spin(10) centre inside U(1)_X (A3), and its E1 weight is used.
- dark-matter-candidate (copy sign): A5 is rederived (B1) and its vertex g is cited. Its verdict is extended to the SMG mirror, not contradicted.
- mirror-condensate-ew (#9974): the symmetric-phase requirement and the 1.5 TeV floor are used.
- gk-nogo-check (#9985): narrowed. Its Delta N_eff = 2.25 applies to a massless mirror; a gapped SMG mirror adds nothing below Delta.
- Register lines on the Z4 of mode number ("Z4 is the most that survives") and on the light-mirror mixing that gaps the corner partners: both are consistent. The Z4 sits inside the exact U(1)_X of the mirror alone.

## Boundary

Exact: the representation theory, the lattice and Smith form of the species phases (full and partial mixing), the anomalies, Wigner-Eckart, and the B3 witness that a shared label is not a decay.

Finite: the tick commutant at (0.3, 0.4, 0.5) and three K, and the atomic-limit ordering.

Cited: the so(12) chains (PR #9910) and the copy vertex (the copy-sign note). Sources named only by their campaign names here (smg-verify, dark-matter-candidate, mirror-condensate-ew, gk-nogo-check, toy-qmc, qmc-face-gapped) are recorded only in the consolidation's map ([VACUUM_COSMOLOGY_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md](VACUUM_COSMOLOGY_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md)); no file of these names was found on `main` or this branch.

Supplied: the tick acting on the cell index alike for every species (so it mixes all six).

Not computed:
- any mirror decay channel: on-shell final states, the lattice matrix element and the rate (the lifetimes in the estimates are conditional on an open channel);
- the lattice SMG phase and its band minima (the 10's further softening is cited from the toy QMC);
- the sign of the gauge self-energy splittings inside the 16;
- three-family and cross-family mirror terms (these could reduce per-family X to the diagonal X);
- light Yukawa terms;
- graviton-coupling normalisation.

Literature: Spin(10) branching rules and the GUT X charge are standard. The freeze-out formula and the unitarity scale are standard approximations.

## How to run

```
python3 scripts/the_gapped_mirror_keeps_only_a_number_shared_with_light_matter_and_its_lightest_state_is_charged_so_it_gives_no_dark_matter_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained and declares `AUDIT_TIMEOUT_SEC = 120`. Through runner_cache.execute_runner from an origin/main worktree it ran in about 1.4 s (about 120 MB resident) and printed about 5.8 kB, ending with `TOTAL: PASS=14 FAIL=0` at the held head; the repaired runner ends with `TOTAL: PASS=16 FAIL=0`. Its random draws are seeded. Since 2026-11-14 it exits nonzero when a check fails and adds A6b (partial mixing over all 63 subsets), B3 (the decay-implication witness) and the Casimir-sign control in D3.
