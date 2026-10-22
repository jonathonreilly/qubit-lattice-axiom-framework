---
claim_id: translation_invariant_terms_give_family_diagonal_mixing_and_a_kept_family_three_cycle_is_excluded_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the register's cube tick (period 2 under translations) read at zoom 3, the three turn-fixed family sectors carry distinct characters of the translations T(2e_i) because gcd(2,3) = 1, so every translation-invariant term or vacuum, at all orders, is family-diagonal and gives permutation mixing matrices with no CP phase; if each quark sector keeps a family three-cycle (any flux or phases), |V| is a permuted circulant, which the measured CKM moduli exclude (estimated at 24 and 184 sigma). Finite diagnostics on a 6^3 torus: the copy-massed tick commutes with T(2e_i), sectors a and -a are isospectral, and a coarse-site vacuum couples the families democratically. Conditional on the supplied zoom-3 family reading; no mass or mixing law is derived."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/translation_invariant_terms_give_family_diagonal_mixing_and_a_kept_family_three_cycle_is_excluded_2026_10_22.py
---

# Translation-invariant terms give family-diagonal mixing, and a kept family three-cycle is excluded

Claim type: bounded_theorem.
Primary runner: `scripts/translation_invariant_terms_give_family_diagonal_mixing_and_a_kept_family_three_cycle_is_excluded_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its family entry reads three families at zoom 3, where the three-fold turn about a site's body diagonal fixes three of the 27 positions of each 3x3x3 block. This note asks what can mix those families, given that the register's update law (CL-1 in the three-law numbering) builds the cube tick from two tilings offset by (1,1,1), and what measured mixing then demands. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the zoom-3 reading nor any vacuum.

## Statement

Supplied model: the update law's cube tick (spin-3/2 edge hop W on 2x2x2 cubes, the two tilings, even cubes exp(-i(eps - mu/2)R) wrapped by the copy-mass factor exp(i(M N/4)(1 - s)R), odd cubes exp(+i(eps + mu/2)R)), one mode per site, single-particle sector, and the zoom-3 family reading in which the families are the turn-fixed sectors (j, j, j), j = 0, 1, 2, of the 27 translation sectors.

1. The tick commutes with T(2e_i) and not with T(e_1) or T(1,1,1). T(2e_1) has character w^(2j) (w = e^(2 pi i/3)) on sector (j, j, j): 1, w^2, w, all distinct because gcd(2, 3) = 1. So every operator commuting with T(2e_i) is block-diagonal in the 27 sectors, and with any translation-invariant term or vacuum, at all orders, each sector's mass matrix is family-diagonal: the quark and lepton mixing matrices are permutations and the Jarlskog invariant is 0. This needs only the update law's translations.
2. Without the copy mass every sector obeys cos w = A S - (cos 2b - cos mu)/2 with S the mean of cos(2 pi a_i/3), A = (cos 2b + cos mu)/2; the family sectors give levels (mu, w1, w1) with w1 -> sqrt3 eps: one light family and a degenerate pair at the cell scale.
3. Sectors a and -a are isospectral for every a (with the copy mass included): the k -> -k symmetry the tick keeps pins family 2 to family 1, so at most two distinct masses per species. A generic T(2e_i)-invariant term splits the pair while keeping every sector closed, so mass splitting and mixing are separate requirements, and mixing needs broken translations.
4. If each quark sector keeps a family three-cycle C_s = D_s C D_s^+ (any family flux or phases D_s), then V = F^+ D_u^+ D_d F up to orderings and |V| is a permuted circulant: every row and column holds the same three moduli.
5. A vacuum term on the zoom-3 coarse sites 3Z^3 breaks the T(2e_i) charge and couples the three families democratically, with |<j,c|V|j',c>| = 1/27 for all j, j', rank one in family space for each corner class c. One such channel per sector gives a rank-one mass (one massive family, two massless). Site plus cube channels on an open spine (x - d, x, x + d, whose ends share no cube) give the texture M = [[0, a, 0], [a, c, b], [0, b, 0]], with det M = 0, so m1 = 0 exactly, m2 m3 = a^2 + b^2 and m3 - m2 = c.

## Derivation

Item 1: sector a is built from the sites 2n + c with the phase w^(-a.n), n running over Z_3^3 (so the zoom-3 block of a 6^3 torus); T(2e_1) shifts n_1 by one and so acts on sector a as a cube root of unity fixed by a_1, which on (j, j, j) is w^(2j) in the runner's convention. The three values are distinct for j = 0, 1, 2 because a period-2 translation generates all of Z_3 (gcd(2, 3) = 1). Anything commuting with all three T(2e_i) preserves the joint character, hence each sector. Item 4: a matrix commuting with a three-cycle is diagonalised by the Fourier matrix F conjugated by D_s, so the two sectors' eigenbases differ by F^+ D_u^+ D_d F, whose moduli form a circulant up to row and column order. Item 5: the coarse-site comb projects equally onto every sector's position basis, giving the democratic 1/27 matrix element; the open-spine texture has zero determinant because its first and third rows are proportional.

## Checks

The runner ends with `TOTAL: PASS=14 FAIL=0` in about 2 s, on a 6^3 torus.

Finite diagnostics:
- The tick at (eps, mu, M N) = (0.03, 0.002, 0.02) is unitary and its commutators with T(2e_1), T(2e_2), T(2e_3) vanish, while those with T(e_1) and T(1,1,1) are 0.0253 and 0.0289.
- The sector leak of the tick at three parameter sets is 2e-16.
- Without the copy mass the closed form matches every sector to 2e-14, with w1/mu = 26.0 at (0.03, 0.002, 0); with the copy mass the family sectors' lowest levels are 0.0020, 0.0363, 0.0363.
- Sectors a and -a agree to 9e-16 at every a and parameter set.
- A random T(2e_i)-averaged term of strength 0.01 splits families 1 and 2 by 1.9e-2 with sector leak 2e-16.
- The coarse-site term has sector leak 9.3e-3 and matrix elements 1/27 to 1e-12, rank one per class.

Exact checks: the three characters are distinct; over 200 random fluxes the row and column moduli of V agree to 6e-14; the open-spine texture with (m2, m3) = (0.3, 7.0) has m1 below 1e-12 and reproduces m2 and m3 to 1e-12.

Stated, not computed by the runner: that a species-blind single channel aligns the heavy family across sectors (V_tb = 1, V_cb = V_ub = 0 at that order), and the zoom-ladder argument that a rung-n cube with the same mass angle has m = mu/N_n with N_n = 2^n N_0.

## Estimates against measurement

Measured inputs: PDG 2024 CKM moduli and errors, quark running masses at M_Z, charged-lepton masses, J = 3.12e-5, NuFIT 6.0 normal ordering.
- Sorted measured rows (0.0037, 0.225, 0.9744) and (0.0086, 0.0411, 0.9991): the smallest moduli differ by 24 sigma and the middle ones by 184 sigma, so every rule that keeps a family three-cycle in both quark sectors is excluded, and a family flux of that type cannot be the source of quark mixing.
- For the site plus cube texture with the measured m2/m3, free angles and phases, and |V_us| held at 0.225, the smallest |V_cb| found by 60 Nelder-Mead starts is 0.0723 (about sqrt(m_s/m_b) - sqrt(m_c/m_t) = 0.137 - 0.060 with an angle factor), against the measured 0.0418 +- 0.0008. This is a float search, so the bound is the best found, not a proved minimum; it indicates that this vacuum needs at least a third channel for the first family.
- A single species-blind channel would make the neutrino mixing share the charged-lepton alignment, against NuFIT |U_mu3| of about 0.68.
- Look-elsewhere: the six adjacent mass ratios read as integer powers of 2 or 3 sit on average 0.18 and 0.28 from integers (p = 0.13 and 0.62 against log-uniform ratios); the best free base, 16.83, has p = 0.46. There is no rung-ratio signal.

## Boundary

Supplied: the tick parameters, the zoom-3 family reading (fine momenta j(1,1,1) or register copies), the coarse-site vacuum and its channels, species couplings per channel, phases, and the measured inputs. Forced, given the update law's tick and the zoom-3 reading: family-diagonal mixing for every translation-invariant term at all orders, at most two distinct masses per species while k -> -k holds, and the permuted-circulant form for any kept family three-cycle. Not claimed: a mass law, a mixing law, a CP phase, a mass hierarchy, or any physical identification of the coarse-site vacuum. What a mass and mixing law must do is read off as requirements: break the tick's translations down to the zoom-3 lattice, break k -> -k in the family sector, keep no family three-cycle in at least one quark sector, and give at least three independent vacuum channels per sector, with neutrinos not sharing the charged-lepton channel. The zoom-ladder reading of masses as 2^-n per rung is not supported here; the open companion result in PR #9883 reports the coarse gap rung-invariant, and that is cited, not rerun.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): unchanged.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's cube tick, copy mass and two tilings, and the zoom-3 family entry. Zero premise weight; results are conditional on them.

## How to run

```
python3 scripts/translation_invariant_terms_give_family_diagonal_mixing_and_a_kept_family_three_cycle_is_excluded_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 2 s, prints about 4.4 kB and ends with `TOTAL: PASS=14 FAIL=0`.
