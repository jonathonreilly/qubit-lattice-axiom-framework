# Lowest transverse level of the ice-rule link model: what is exact at 2x2x2, and where the route stops

Task `J:derive:review-20260929-wall-photon-mode-and-preparation:a1`. Worker: Claude Sonnet 5.5, same family as the source authors. Same-family, unrefereed.

## Plain-language summary
The source wall (T78) asks whether the lowest wave of the ice-rule qubit-link model is light-like. Nothing here settles that. What I did is pin down, exactly, what "the lowest transverse level" is on the one torus where it can be computed exactly (2x2x2, 864-state component), and which wrong readings that rules out.

- The lowest level of the whole Hamiltonian (the gap, 0.969623617 at the RK point) is not the lowest transverse level. It sits in the zero-momentum sector and has exactly zero weight in every k = pi transverse mode.
- The lowest transverse-coupled level at RK is a different number, 1.160865513 (about 20 percent higher). It carries 70.4 percent of the transverse weight.
- Away from RK the same level has certified lower brackets (table in step 10).
- Bigger tori, momentum scaling and any linear-dispersion statement are not reached. That is the first unresolved step.

## What I read (stated as required)
- `docs/MINIMAL_AXIOMS_2026-06-29.md` read in full (main_wt, lines 1-233) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` read in full (lines 1-130). Approved primitives there: `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`.
- Source branch `claude/toe-walls-20260929` at `4bd42747e57c4d604f66a63eed2db099ea38af4e`: fetched; all 8 task source objects re-hashed and match SOURCE_MAP.json (RECOVERY_STATUS.json). Read in full: T78 attack and kill; WALLS.md rows T77-T79 and SUMMARY.md headline. T77/T79 attack and kill files hashed but only their WALLS.md rows were used.
- Current main (`origin/main` 3e1a2dd) notes: the 2026-09-25 energy-only bounds note (all), the 2026-10-01 frozen-components note (all), the 2026-10-01 three-moments note (all), the 2026-09-03 RK note (front matter, result, spectrum lines 195-225). Prior attempts read: `probes/work/derive/deferred-20260926-local-rk-preparation` (ATTEMPT.md, RECOVERY_STATUS.json) and `probes/work/derive/deferred-20260925-ring-limits` (ATTEMPT.md). No attempt exists for the finite-spin tensor task or for this task.

## Premises (what the axioms say, what is supplied, what is proved)
1. READING. The four axioms (Lattice, Qubit, Admissibility, Record) supply no Hamiltonian, no link degrees of freedom, no Gauss law and no transverse readout (`MINIMAL_AXIOMS_2026-06-29.md:114-130`: Admissibility "does not choose a Hamiltonian or transfer operator"). Qubits live on sites in the axioms; the model below puts a two-valued variable on links. Everything below is therefore a conditional statement about a supplied model, as the sources already say.
2. ASSUMED (supplied model, as in main's ring-model notes). Link spins sigma = +-1 on the periodic cubic torus; exact vertex Gauss law (net outward flux 0); plaquette flips of circulating plaquettes (circulation +-4); on a connected flip component H(v) = v*D - A, D = number of flippable plaquettes, A = flip adjacency, 0 <= v <= 1. v = 1 is the Rokhsar-Kivelson (RK) point (H = graph Laplacian), v = 0 the pure ring point. Readout O_b = N^(-1/2) sum over b-links of (-1)^(x_{b+1}) sigma, k = pi, axes cyclic. No other premise; no dynamics claim beyond this H.
3. CHECKED (check.py G1-G3). Independent enumeration on 2x2x2: 9600 Gauss states, 937 flip components, canonical component 864, 16 frozen zero-winding states. Agrees with main's 2026-10-01 note.

## Steps
4. PROVED. For every v in [0,1], H(v) on a connected component has nonpositive off-diagonal entries, so its lowest eigenvalue is simple with a positive eigenvector (Perron-Frobenius). The component's automorphism group contains the translations, so that vector is translation invariant and lies in the trivial momentum sector. (Used in step 10 to place E0.)
5. PROVED + CHECKED (G5, G6). Ground-space treatment. At v = 1 the kernel of H on the full Gauss space is spanned by one uniform vector per component, so it has dimension 937 on 2x2x2 (nullity 937 computed per component). "Lowest excitation above the ground space" must therefore be taken inside one component. O is diagonal in sigma, so it never maps between components; centering O|u_C> by its overlap with u_C removes the whole relevant ground space. CHECKED: for v in {0.9, 0.75, 0.5, 0.25, 0} the global ground state of the full Gauss space is in the canonical component, with a clear margin to every other component. CHECKED (G4, exact rationals): first-order ranking, canonical <N_f> = 8 is the unique maximum of 937 values; runner-up 188/29 (this is the second number the T78 attack quotes for L = 2, so that number is the runner-up component). This holds only on 2x2x2.
6. PROVED (arithmetic) + CHECKED (P2). Rule to reuse where the readout is not diagonal (finite-spin tensor task): if the ground eigenspace G has more than one vector and O connects them, the naive centred weight m0 = <g|O^2|g> - <g|O|g>^2 equals the excited-state weight plus sum over g' in G, g' != g of |<g'|O|g>|^2, while m1 = <g|O(H-E0)O|g> is unchanged. So m1/m0(naive) <= m1/m0(excited only), and the naive ratio need not bound the lowest excited level. Exact 3-level example: ratios 4/13 versus 1 against lowest excited level 1. Not new (it is the rule the task text states); it is the only transfer to the tensor task and no tensor channel is built here.
7. CHECKED exact (T1, T2). Translations of Z_2^3 are automorphisms of the flip graph, and O_b obeys O_b(T_g s) = (-1)^{g_{b+1}} O_b(s) for all 864 states. So O_b|0> lies exactly in the translation-character sector with momentum pi along x_{b+1}.
8. CHECKED exact (T3, S1-S3). Eight character sectors (dimensions 133, 107 x3, 103 x3, 101; orthogonal, complete, H block diagonal). Eigenvalue counts below rational thresholds come from Sylvester inertia, computed from leading principal minors with Python integers (Bareiss):
   - trivial sector at RK: 1 eigenvalue below 0.969623, 3 below 0.969624. So the zero mode and the global-gap doublet 0.969623617 are in the trivial sector.
   - each of the three momentum-pi sectors: 0 below 1.160865 and 2 below 1.160866.
   - the four remaining sectors: 0 below 1.160866.
   Consequence (follows from steps 7 and 8): the global-gap doublet has zero weight in every O_b|0>. The lowest transverse-coupled level is in the momentum-pi sector.
9. CHECKED exact (M1-M9). Moment algebra over Q at RK, independent of the sector route. Exact: m0 = 5/3, m1 = 8/3 (equals the f-sum value 2 u s^2 with u = <N_f>/(3N) = 1/3, s^2 = 4), identical for the three cyclic modes up to moment order 44. The first singular Hankel determinant gives 16 distinct atoms. The minimal polynomial annihilates O_0|u> exactly (all 864 entries, rationals), has 16 simple positive real roots and is irreducible over Q. Lowest root 1.160865513171 lies inside the inertia bracket of step 8 (two independent routes agree). Weights from the exact moments are positive and reproduce m0, m1, m_{-1} = 1.2042482138 to 40 digits (60-digit root finding, so this part is high-precision numerical, not exact). The lowest level carries 1.17367 of 5/3 = 70.4 percent. Chain: 1.1609 <= m0/m_{-1} = 1.3840 <= sqrt(m1/m_{-1}) = 1.4881 <= m1/m0 = 1.6 (exactly 8/5).
10. CHECKED (C1, C2). Away from RK, rational v = p/q. A rigorous lower bracket for the lowest transverse-coupled level is (certified floor of the momentum-pi sector) - (certified upper end of the ground-energy bracket from the trivial sector, justified by step 4). Both ends come from exact inertia. Upper values are floating point (m0/m_{-1}), not certified.

   | v | certified omega_min >= | float coupled level | weight fraction | m0/m_{-1} | m1/m0 |
   |---|---|---|---|---|---|
   | 1 (RK) | 1.160865 (step 8, exact) | 1.160866 | 70.4% (exact moments) | 1.38399 | 1.60000 |
   | 3/4 | 1.47566 | 1.47568 | 74.7% | 1.70474 | 1.91585 |
   | 1/2 | 1.79194 | 1.79196 | 77.5% | 2.02654 | 2.23348 |
   | 1/4 | 2.13191 | 2.13193 | 79.2% | 2.37631 | 2.57888 |
   | 0 | 2.51726 | 2.51728 | 80.3% | 2.77536 | 2.97279 |

   Float cross-check: the lowest level of the momentum-pi sector equals the lowest coupled level to 1e-14 at every v tried. The v = 0 value reproduces the 2.5173 of the earlier ring-limits attempt (rediscovery). The level rises monotonically as v decreases on this grid. That is one size and one momentum; it says nothing about stability of a long-wavelength mode.
11. Static versus dynamic (kept separate).
   - PROVED conditional. ω_min <= m1/m0 = 2 u s^2 / S(k) (Feynman-Cauchy-Schwarz, as in main's 2026-09-25 note). At RK, if the uniform-ice transverse structure factor satisfies S(k) >= S_* > 0 as k -> 0, then ω_min(k) <= (2 u_RK / S_*) s^2 = O(k^2). So a flat static transverse factor at RK excludes a linear mode at RK; this is the tuned point's own scaling. The input S_* > 0 is ASSUMED (Monte Carlo on main, not proved). Only the L = 2 ratio is evaluated (check L2). I do not claim this is new: main's RK note already says the RK point has "special RK scaling".
   - READING. A static quantity (flux stiffness from E_C ≈ -eps <N_f>_C, structure factor, moments) is one half of what a photon speed needs. A lower bound on the lowest level, or on its weight, is a separate input that no moment of order -1, 0, 1 supplies (the earlier ring-limits attempt's exact three-atom counterexample; the 10-01 note bounds weight spreads only). The kill's point that the non-shrinking c_L is close to automatic for a smooth local ensemble is consistent with this separation. I did not rerun the 32^3 sampling.
   - P1 CHECKED exact: a plug-in Rayleigh quotient whose centering is off by delta (f + delta*u) equals m1/(m0 + delta^2) at RK because H u = 0. For delta^2 = m0/2 it is 16/15 = 1.067, below the true lowest coupled level 1.161. So a quotient built from estimated centering is not an upper bound. This restates the task's caution; it is not a new result.

## What is new, and what is not
- Not new: retrieval of sources; the 0.9696 / 1.1609 eigenvalues (they are in main's RK note as the five lowest levels); the three-moment machinery; the ground-space rule (step 6); the v = 0 value 2.517; the conditional O(k^2) bound at RK (step 11); the 937 / 864 / 16 counts.
- New, scoped to 2x2x2 (this is the basis of the HIT line): (i) the exact momentum-sector assignment of the RK spectrum: the gap doublet is in the trivial sector and has exactly zero weight in all k = pi transverse modes; (ii) the lowest transverse-coupled level at RK is 1.160865513171, an algebraic number of degree 16 (irreducible minimal polynomial) with exact weight fraction 70.4 percent, and the two exact routes (sector inertia, Hankel/minimal polynomial) agree; (iii) certified lower brackets at v = 3/4, 1/2, 1/4, 0, with a Perron-Frobenius justification for the ground energy placement. I searched main docs (grep for the numbers 1.16086, 0.96962), the probes work tree and the open-PR list (`gh pr list --search`, which returned nothing) and found no statement of (i)-(iii). The open-PR search is shallow.
- What this does to the source wall: nothing is passed. It shows concretely that P4 of the T78 attack ("lowest level is the photon") must be stated per momentum sector: even at L = 2 the global gap and the lowest transverse-coupled level differ and live in different sectors.

## First unresolved step
Step 12 (not done). A rigorous statement for any torus larger than 2x2x2: a lower bound on the lowest transverse-coupled level, with its size and momentum scaling, and a lower bound on its weight. The exact route used here needs the whole component in rational arithmetic; the next candidate (2x2x4 prism, 1,551,976 states) is beyond it, and a prism is not a cubic torus anyway. Moments alone cannot do it. The static input for the RK statement (step 11) and for any statement away from RK (Coulomb phase, V < K, no ordering) remains supplied.

## Remaining obligations
- Size and momentum scaling of the lowest coupled level, with a weight lower bound uniform in size.
- Dynamic linear dispersion and stability away from the tuned point (nothing proved here; v < 1 rows are one size, one momentum).
- Proof that uniform-ice S(k) stays bounded below (supplied).
- Preparation half of the task (`deferred-20260926-local-rk-preparation`): not advanced; the earlier attempt left a volume-uniform cooler gap and field-phase compatibility open.
- Finite-spin tensor task: only the ground-space rule of step 6 transfers; no tensor channel built.

## Negative claims (N1-N8)
This note makes no negative claim: "the RK point has no linear mode" is stated only as a conditional implication (step 11) and "moments cannot bound the lowest level" is cited from the earlier attempt, not re-proved.

## Reproduce
`python3 check.py` runs in about 70 s, under 0.5 GB, prints `TOTAL: PASS=27 FAIL=0`.
