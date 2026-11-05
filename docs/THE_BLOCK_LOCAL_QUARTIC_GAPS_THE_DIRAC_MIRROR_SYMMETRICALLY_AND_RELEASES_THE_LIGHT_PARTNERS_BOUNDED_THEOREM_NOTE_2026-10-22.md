---
claim_id: the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the block-local mirror term (on each matter role block, the unique singlet charge-4 term of the block's mirror modes; SU(4) toy with one mode per flavour per block, and its Spin(10) form with two orbitals per flavour) on a real pi-flux Dirac band of the block lattice: (exact) the term is unique (SU(4): 1 with one orbital, 5 with two; Spin(10) on the Weyl 16: 0 with one orbital, exactly 1 with two), is invariant under per-block SU(4) gauge rotations, commutes across blocks, maps to its conjugate under the sublattice particle-hole map, and alone has a unique ground state with gap g; with any real band, including a real light layer mixed to the mirror, the interaction expansion is sign-free (weights det(M)^4, M real). Finite diagnostics (sign-free CT-INT, L = 4, 6 block units, beta = 4, 8 in units 1/g): the Dirac mirror is massless for g/t <= 2, crosses over near g/t ~ 4, and is symmetric and gapped for g/t >= 8 (Dirac-point gap about 0.85-0.95 g, L-independent); no bilinear channel orders at any coupling (site and bond, charge 0 and 2, all Q). With a light layer whose modes are paired to the mirror by w eps_x, the light gap falls from w (g/t <= 4) to 0.54 w (g/t = 8) and 0.22 w (g/t = 16): the symmetric mirror gap releases every light mode the mirror was pairing (exact at the Dirac point once the mirror propagator has a zero). The toy is not Spin(10), the band is not the CL-1 cube tick, no Binder ratio, L <= 6."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_filtered_quartic_toy_with_a_face_gapped_band_is_symmetric_and_gapped_at_moderate_coupling_and_pairs_at_strong_coupling_bounded_theorem_note_2026-10-22
  - the_cube_filtered_quartic_toy_is_sign_free_and_pairs_at_strong_coupling_bounded_theorem_note_2026-10-22
runner: scripts/the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_2026_10_22.py
---

# The block-local quartic gaps the Dirac mirror symmetrically and releases the light partners

Claim type: bounded_theorem.
Primary runner: `scripts/the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) leaves one chirality wall: a mirror term that gaps the mirror family symmetrically. The [face-gapped QMC note](THE_FILTERED_QUARTIC_TOY_WITH_A_FACE_GAPPED_BAND_IS_SYMMETRIC_AND_GAPPED_AT_MODERATE_COUPLING_AND_PAIRS_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-22.md) found two things in sign-free 3D QMC. The overlapping cube-filtered quartic pair-orders at strong coupling. The on-site SU(4) quartic is symmetric and gapped. That run had no Dirac point: its free band had only a quadratic touching. This note asks three questions. Does the non-overlapping, block-local version of the quartic fit the framework? Does it gap a mirror whose free band has a genuine Dirac point? And, the Golterman-Shamir question, does the light family keep its partners gapped while the mirror gaps? The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

## Statement

1. (Framework fit and uniqueness.) CL-1 puts one fermion mode on each site. So a term that acts "on-site" in flavour must live on a non-overlapping block: the matter role block holding one family's modes. The block-local mirror term is the singlet charge-4 operator built from the block's mirror modes.
   - SU(4) toy, one mode per flavour per block: the singlet charge-4 operators span exactly one line, m1 m2 m3 m4. With two orbitals per flavour they span 5, so uniqueness needs one orbital.
   - Spin(10) on the Weyl 16: one orbital per flavour admits no singlet charge-4 operator. Two orbitals admit exactly one, the pair square.
   - In both cases the term is invariant under SU(4) (or Spin(10)) rotations of its own block alone, so it is gauge-invariant per block.
   - Terms on different blocks share no mode and are even, so they commute.
   - Every lattice map of the block tiling permutes the terms. A staggered sign gauge a -> -a multiplies each term by (-1)^4. The sublattice particle-hole map a_x -> eps_x a_x^+ sends the term to its conjugate, so -g sum (Q_b + Q_b^+) is invariant. Mode number is broken to Z4.
   - Alone, -g(Q_b + Q_b^+) has a unique ground state at -g with gap g.
2. (Sign.) Take any real free band, including a light layer mixed to the mirror by a real term, with vertices on the mirror block terms only. Every configuration of n terms and n conjugates has weight g^2n det(M)^4 with M real. A flux through a loop holding two vertex blocks makes the weights complex.
3. (Dirac band.) H = -t sum eta_mu(x)(a_x^+ a_x+mu + h.c.) is the real pi-flux (staggered) band on the block lattice. With periodic boundaries at L = 4 and antiperiodic at L = 6 it has exactly 8 zero modes per flavour (2 tastes x 4 components at k = (pi/2)^3), first levels 2t and sqrt3 t, and it anticommutes with eps_x. The mixing w eps_x (l_x^+ m_x + h.c.) gaps every light and mirror mode by exactly w, because (H +- w eps)^2 = H^2 + w^2. Every real period-2 site pattern tried is either this full mass or not a mass: (1 + eps)/2 leaves 8 zeros with a quadratic touching. So no real, sign-free taste-selective mixing was found.
4. (Mirror alone, finite diagnostics, g = 1.)
   - g/t = 0.5, 1, 2: massless. The Dirac-point midpoint gap is <= 0.02 and is 0.00-0.01 at L = 6.
   - g/t = 4: crossover. The Dirac gap shrinks with L at beta = 8 (cosh band [0.34,0.39] -> [0.27,0.30]), and pair xi/L falls 0.158 -> 0.101.
   - g/t = 8, 16: symmetric and gapped. The Dirac gap is L-independent, [0.87,0.91]; [0.85,0.90] and [0.92,0.99]; [0.87,0.98], approaching the exact g/t = infinity value g.
   - Across all couplings, S/N for each of the 7 bilinear channels falls from L = 4 to 6 by 2.6-3.7, against a volume ratio of 3.375. The channels are site pair (6, charge 2), site adjoint, site singlet density/staggered mass, bond pair (symmetric and antisymmetric), bond adjoint and bond singlet (VBS), each at its peak Q. No order is seen in any channel.
5. (Light release.) A light layer with the same band, paired to the mirror by w eps_x (t = 0.125, w = 0.25, beta = 8, L = 4). The light gap at the Dirac point is 0.249, 0.248, 0.239, 0.135, 0.054 at g/t = 1, 2, 4, 8, 16, against a free value of exactly w = 0.25. At L = 6 and g/t = 8 it is 0.141. Over the same range the mirror gap grows 0.25 -> 1.84. Exact form: at the Dirac point G_l = [i w - w_mix^2 G_m^0(i w)]^-1. Once the symmetric mirror's propagator has a zero (Sigma_m ~ Delta^2 / i w), the light has a pole at w = 0. Every light mode the mirror was gapping is released.

## Derivation

Statement 1. A charge-4 operator on the block is a degree-4 element of the exterior algebra on (flavour x orbital). It is counted on the weight-zero subspace with the restricted Casimir sum_a (X_a P0)^+ (X_a P0), whose kernel is the singlets. The counts are SU(4): 1 (one orbital) and 5 (two). Spin(10), with the 16 as the even Fock space of 5 modes: 0 (one orbital) and 1 (two). The SU(4) result is Lambda^4 of the 4, times Sym^4 of the orbital space. The Spin(10) result is the register's "unique Spin(10) tensor times an algebraic-curvature tensor on the orbitals" (that space has dimension n^2(n^2 - 1)/12: 0, 1 for n = 1, 2). The symmetry and commutation statements are checked on two blocks (8 modes) to 1e-15.

Statement 2 is the toy-QMC sign argument. The light modes enter only the free propagator. The four flavours see the same real M, and vertex reordering gives +1.

Statement 3. {H, eps} = 0 because the hops join opposite sublattices. The zero modes are the 8 momenta with cos k_mu = 0 for all mu, since H^2 = 4t^2 sum cos^2 k_mu.

Statements 4-5 come from continuous-time interaction-expansion Monte Carlo. The moves are global and local pair insertions and removals and vertex shifts. The engine reuses the qmc-face-gapped engine with a translation-by-two table that carries the antiperiodic signs (checked to 1e-7). Observables come from the per-configuration propagator:
- bilinear correlators by Wick per flavour (pair G^2, adjoint (1 - G^T) G, bond forms with link phases);
- Dirac-point propagators Tr(P0 G(tau))/8 on the 8 zero modes, mirror and light;
- gaps from two estimators: the midpoint -(2/beta) ln(2 G(beta/2)/(G(0+) + G(beta-))), which is lower-bound style, and a one-level cosh fit at tau = beta/4, both as mean +- 2 sigma (jackknife, 16 bins).

The release formula follows from integrating out the mirror at quadratic order in the mixing. The light layer is free, so its exact propagator is the free one with self-energy w^2 eps G_m eps, where G_m is the full mirror propagator without the mixing self-energy.

## Checks

- `[PASS] A1` real band with light-mirror mixing: trace = det(M)^4 (4e-16).
- `[PASS] A2` flux: complex weights (|Im w|/|w| up to 0.89).
- `[PASS] A3` uniqueness counts: SU(4) 1, 5; Spin(10) 0, 1.
- `[PASS] A4` per-block SU(4) invariance, commutation across blocks, particle-hole to the conjugate, unique block ground state -g with gap g.
- `[PASS] A5` 8 Dirac zeros at L = 4 (PBC) and 6 (APBC); {H, eps} = 0; the w eps mixing gaps by w; the half mixing gives a quadratic touching.
- `[PASS] A6` release algebra: |G_l(i 1e-3)| is 0.016 free and 941 with an SMG mirror.
- `[PASS] B1` engine vs exact diagonalisation of a mixed 3-orbital cluster: <H_int> and the light G_l(beta/2).
- `[PASS] C1` g/t = 1: Dirac gap 0.016.
- `[PASS] C2` g/t = 8: gap 0.63(6), xi/L 0.05.
- `[PASS] C3` g/t = 8, beta = 4: S/N ratio 3.30, cosh gap 0.684 vs 0.669 (L = 4, 6).
- `[PASS] C4` light gap 0.249 -> 0.144 while the mirror gap is 0.65.

Recorded production values (prod.py, 85 s segments, 171 to 48000 sweeps per point; printed by the runner as recorded, no PASS depends on them). Mirror alone, Dirac-point gap (cosh band, L = 4; L = 6), pair xi/L, and channel S/N ratio:

| beta = 8 | cosh gap | midpoint band | pair xi/L (4 -> 6) | S/N ratio min-max (7 channels) |
|---|---|---|---|---|
| g/t = 0.5 | [0.07,0.08]; [0.01,0.04] | <= 0.01 | 0.082 -> 0.053 | 3.06-3.38 |
| g/t = 1 | [0.07,0.09]; [0.00,0.05] | <= 0.01 | 0.085 -> 0.053 | 3.06-3.38 |
| g/t = 2 | [0.10,0.12]; [0.05,0.09] | <= 0.02 | 0.093 -> 0.058 | 3.05-3.35 |
| g/t = 4 | [0.34,0.39]; [0.27,0.30] | [0.16,0.20]; [0.11,0.13] | 0.158 -> 0.101 | 2.95-3.72 |
| g/t = 8 | [0.87,0.91]; [0.85,0.90] | [0.67,0.72]; [0.60,0.68] | 0.038 -> 0.037 | 2.80-3.41 |
| g/t = 16 | [0.92,0.99]; [0.87,0.98] | [0.75,0.80]; [0.63,0.77] | 0.021 -> 0.008 | 2.61-3.53 |
| g/t = inf | g (exact) | | 0 | |

At beta = 4 the cosh gaps are g/t = 2: [0.16,0.18]; [0.13,0.15], g/t = 4: [0.42,0.43]; [0.40,0.42], g/t = 8: [0.66,0.71]; [0.68,0.71], with S/N ratios 3.07-3.44. The cube-term susceptibility is at most 1.44 in every run and noisy at L = 6. The small nonzero cosh values at weak coupling come from incoherent self-energy decay; the midpoint gap stays at 0.

Light release (t = 0.125, w = 0.25, beta = 8, L = 4; cosh gaps):

| g/t | 1 | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|
| light | 0.249 | 0.248 | 0.239 | 0.135 (L = 6: 0.141) | 0.054 |
| mirror | 0.251 | 0.256 | 0.281 | 0.69 (L = 6: 0.66) | 1.84 |

## Clause count and law text

Proposed replacement for the mirror clause of CL-1's chiral update (law text):

> "Mirror term. On each matter role block the mirror copy's modes carry the one Spin(10)-singlet charge-4 term they admit, the pair square of the block's two orbitals per flavour, with the same coupling on every block; terms of different blocks share no mode."

Effect on the register: one clause replaces one clause, and the cube filter (the supplied form factor prod cos^2(k_i/2)) is removed. That is a simplification. The term is forced by uniqueness once the block and the mirror copy are named.

Smuggling check:
- Supplied: the coupling g (a constant in proper units), the mirror bit, and the role block (already in CL-1).
- Forced: the form of the term (A3), its gauge and lattice covariance (A4), and the Z4.
- The toy evidence is SU(4), not Spin(10). Sign-freedom needs four identical flavours, and the Spin(10) pair square is not of that type, so the Spin(10) phase is unmeasured beyond the register's single-cell result (unique ground state, gap 19.1 g).

Verdict on the register: do NOT adopt this as the chirality fix. The block-local term is exactly the atomic pair square that the register's far-end theorem already excludes, and the QMC now confirms that exclusion in 3D. Gapping the mirror symmetrically is achieved, with no pair order, unlike the cube filter. But it releases every light partner that was gapped through light-mirror mixing, as Golterman and Shamir warn. Adopting it would trade the filter's pair-order failure for the far-end failure. The term is the better mirror-gapping term (unique, no filter, symmetric, gapped). If a separate rule removes the light copy's zone-corner partners WITHOUT routing through the mirror, this term is the natural mirror clause, and it should then replace the cube-filtered pair square.

## Boundary

Supplied:
- the SU(4) toy (not Spin(10)), one mode per flavour per block;
- the real pi-flux Dirac band on the block lattice (a stand-in for the CL-1 cube tick's mirror band), with its boundary conditions;
- the w eps_x mixing as the stand-in for partner gapping through the mirror (no real taste-selective mass was found, so all light modes are paired in the test);
- sizes L = 4, 6, beta = 4, 8 (units 1/g), seeds, and g = 1.

Not computed:
- the Binder ratio, L > 6, and the T -> 0 limit near g/t ~ 4. A narrow intermediate bilinear phase, as Ayyar and Chandrasekharan found in 4E, is neither seen nor excluded.
- the Spin(10) pair square on the Dirac sea;
- a genuinely chiral light-versus-mirror split.

The unpaired-light question is trivial in this model: no light mode is unpaired. Statement 5 and A6 answer the Golterman-Shamir question for the paired ones.
