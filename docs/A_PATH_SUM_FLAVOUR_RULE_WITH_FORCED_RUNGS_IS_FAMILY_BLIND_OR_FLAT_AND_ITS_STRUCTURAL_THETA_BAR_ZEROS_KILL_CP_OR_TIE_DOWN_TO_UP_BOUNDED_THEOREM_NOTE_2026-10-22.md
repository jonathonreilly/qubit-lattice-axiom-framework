---
claim_id: a_path_sum_flavour_rule_with_forced_rungs_is_family_blind_or_flat_and_its_structural_theta_bar_zeros_kill_cp_or_tie_down_to_up_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the path-sum family mass rule of the fold-ladder note (contacts of range r = 1, 2, 3 carrying (2^(-3/2))^r exp(i h lam sin(r theta)), theta = arccos(-2/3); mass term G(b - a), conjugated when b < a), with rungs set by a rule rather than fitted: exactly, any rung rule that depends only on a multiplet's link charges (the copy-sign gap depth, undressed or with the dressed-cone step; the nested role-block rung of the acting factors) gives the three families of a multiplet one rung, so M = G(b - a) times the all-ones matrix, of rank 1 (60 seeded cases); u^c and d^c carry the same factor set, so every factor-set reading gives m_b = m_t (all 1024 rung triples, coarsest and finest readings); the zoom-3 family characters share one support, so a first-split-generation reading is family-blind too; the octree reading (one 16 per rung) puts each family's doublet and singlets on one rung, so each sector is Hermitian, sin(theta-bar) = 0 exactly, m1/m3 >= 0.33 at every lam, and V = 1 for a down sector of the same sense. Enumerated over distinct rungs 0..8 (395136 layouts, three seeded (lam, theta) samples): every layout with arg det(Mu Md) in {0, pi} for all samples is Hermitian, self-mirror, sense-flipped (b_d = b_u, h_d = -h) or u<->d mirrored under a rung reflection n -> c - n; the first two have J = 0 (<= 2e-15), the last two force the down mass ratios to equal the up ones (exact). Estimates against measurement: m_c/m_t = 3.7e-3 (rank-1 rules give 0), m_b/m_t = 0.0169 (factor-set rules give 1), m_u/m_t = 7.3e-6 (octree >= 0.33), |V_us| = 0.224 (octree 0 or 0.44-0.80), J = 3.08e-5, (m_d/m_b)/(m_u/m_t) = 129 (mirror classes give 1); the best structural-theta-bar layout has rms log-deviation 1.91 on the four quark mass ratios with lam scanned. Supplied model, finite diagnostic: the path-sum rule and its phase form, lam (scanned over 1-3), theta, the dressing slowdown (2S/(2S+1))^2 per factor, the multiplets' factor sets, the octree 16-per-rung reading, the rung range, the samples, and the measured values."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_path_sum_flavour_rule_with_forced_rungs_is_family_blind_or_flat_and_its_structural_theta_bar_zeros_kill_cp_or_tie_down_to_up_2026_10_22.py
---

# A path-sum flavour rule with forced rungs is family-blind or flat, and its structural theta-bar zeros kill CP or tie the down tower to the up tower

Claim type: bounded_theorem.
Primary runner: `scripts/a_path_sum_flavour_rule_with_forced_rungs_is_family_blind_or_flat_and_its_structural_theta_bar_zeros_kill_cp_or_tie_down_to_up_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The fold-ladder note (`flavour-rule`, open PR #9998) failed the anti-smuggling gate because its 13 rung integers were fitted. That note asked for rung assignments forced by site, neighbour or update constraints, and for arg det(M_u M_d) = 0 in the same structure. This note tries the three readings the register offers and then asks which rung layouts give theta-bar = 0 without tuning. All three readings fix their rungs without a fit, and their unfitted predictions all fail measurement. The strong-CP scan finds no structural theta-bar zero that keeps both CP violation and distinct up and down towers. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs. Every check passes; most PASS lines record a failure against measurement.

## Candidate rules (verbatim; not adopted)

> (a) "A multiplet is read on the rung at which its copy-sign sector first gaps."
>
> (b) "A mode charged under a link factor is read on that factor's role-block rung B_f; its rung is that of the coarsest (or finest) factor acting on it."
>
> (c) "A mode is read on the first split generation at which it exists."

Each is combined with the path-sum mass term of `flavour-rule`, as specified there.

## Statement

A. Exact structure (any G, any lam, any theta).

1. Family blindness. If a rung is a function of a multiplet's link charges, then the three families of the multiplet share it, because the families carry identical charges. Then M_ij = G(b - a) for all i and j, so M is G(b - a) times the all-ones matrix. Its rank is 1 and its masses are (3|G|, 0, 0). The runner checks 60 seeded cases.
2. Equal factor sets. u^c and d^c are both acted on by colour and hypercharge only. Every reading that depends on which factors act therefore puts them on one rung, which gives |M_u| = |M_d| and m_b = m_t for either sense of the down contacts.
3. Hermitian layouts. If the singlet rungs equal the doublet rungs, then M is Hermitian, because reversed paths carry conjugate weights. Its determinant is then real.
4. Sense-flip pairing. Suppose the down singlets sit on the up singlets' rungs and the down contacts run in the reverse sense. Then M_d = conj(M_u), so det(M_u M_d) = |det M_u|^2 > 0, and the down spectrum equals the up spectrum.

B. The three readings, with rungs forced.

5. (a) The copy sign s = i R_1 R_2 R_3 R is read from undressed even cubes (CL-1), so it is the same for every species, and the gap depth is the same for every multiplet. All rungs are equal, M is the all-ones matrix, and every sector has masses (3, 0, 0). If instead the depth is read through the dressed-cone step eps_X ~ eps0 / prod (2S/(2S+1))^2, the depth shift is 2 log2((2S+1)/2S) rungs per acting factor. At S = 1/2 this gives Q 6, u^c 4, d^c 4, L 4, e^c 2, nu^c 0. At S = 3/2 it gives 2, 2, 2, 2, 1, 0. At the register's large hypercharge size (S ~ 275) every shift is 0. In every variant the result is family-blind (item 1) and gives r(u^c) = r(d^c) (item 2).
6. (b) For all 1024 assignments of (B_3, B_2, B_Y) rungs in 0..7, with either the coarsest or the finest acting factor, M_u and M_d have rank 1 and m_b = m_t. Gauge content cannot tell families apart. A charge-magnitude reading through V^q could separate t from b, but it would still be family-blind.
7. (c), register reading. The families are the zoom-3 turn-fixed characters (j, j, j). Each has modulus 1/sqrt3 on all three fixed positions, so they share one support and one first generation. That makes this reading family-blind as well (rank 1). This agrees with #9951 (the zoom ladder adds no family charge).
8. (c), octree reading. With one 16 per rung, family f sits on rung f - 1 for Q, u^c and d^c alike. Each sector is then Hermitian (item 3), so sin(theta-bar) = 0 exactly for every lam and either down sense. But the unit diagonal G(0) = 1 dominates, giving m1/m3 between 0.33 and 0.35 and m2/m3 between 0.52 and 0.64 over lam in [1, 3]. With the same sense in the down sector, V = 1. With the opposite sense, |V_us|, |V_cb| and |V_ub| are (0.80, 0.59, 0.46) at lam = 1 and (0.44, 0.89, 0.45) at lam = 3, with J of order 1e-16.

C. Structural strong CP (enumerated, distinct rungs 0..8, both down senses).

9. A layout counts as structural if arg det(M_u M_d) is 0 or pi at three seeded (lam, theta) samples. There are 395136 layouts. The structural zeros are 28 Hermitian layouts, 40 self-mirror layouts (Q, u^c and d^c each invariant under one rung reflection n -> c - n), 2302 sense-flip layouts and 126 u<->d mirror layouts (b_d = c - b_u with Q self-mirror). There are no others. The reflection, composed with conjugation, is the antiunitary that makes the determinant real. On the half-line ladder it is not a symmetry of any law.
10. In the Hermitian and self-mirror classes the same antiunitary is a CP of every sector, so J = 0 (at most 2e-15).
11. In the sense-flip and mirror classes J can be nonzero (up to 0.096), but M_d = P conj(M_u) for a row permutation P. The down mass ratios then equal the up ones exactly; the runner finds them equal to 3e-13 in log.
12. So theta-bar = 0 without tuning gives either J = 0 or a down tower equal to the up tower. Measurement has J = 3.08e-5 and (m_d/m_b)/(m_u/m_t) = 129, so both options fail. With lam scanned, the best structural layout reaches an rms log-deviation of 1.91 on the four quark mass ratios. The self-mirror class extended to c <= 20 reaches 2.49, with a nearly degenerate light pair and J ~ 1e-20.

## Gate result (owner's anti-smuggling gate)

All three candidates fail, on measurement and not on fitting:
- (a) and (b): rank 1 in every sector, which leaves two massless families. They also give m_b = m_t.
- (c), register reading: rank 1.
- (c), octree reading: no hierarchy, and either V = 1 or order-one mixing.

1. Measured numbers chosen: none in the rung assignments. lam is scanned, not fitted, and no conclusion depends on it.
2. Structure by name: (b) and dressed (a) read the multiplets' observed factor sets (Q, u^c, d^c, L, e^c, nu^c with SU(3), SU(2), U(1) charges), which is supplied content. The octree reading of (c) uses the 16 that the register lists as supplied. Undressed (a) and the register reading of (c) insert nothing.
3. Unfitted predictions:
   - all three readings: rank 1, or m1/m3 >= 0.33 (fails);
   - (a) and (b): m_b/m_t = 1 (fails by a factor of 59);
   - octree: theta-bar = 0 (passes), but in a layout with J = 0 or wrong mixing.
4. Axioms bent: the same as the fold ladder. Admissibility is bent by contacts of range 2 and 3 in the zoom direction. Lattice is bent by the rung role reading (AX-2).

## What survives, and what a replacement must do

These results are fit-free and reusable:
- A flavour rule whose rungs are a function of gauge charges cannot give more than one massive family. Rung differences between families need a family label from a new structure, consistent with the register's requirement for an ordered family charge.
- In the path-sum rule, the only tuning-free theta-bar zeros come from a conjugating rung reflection, or from reversing the down sense on the up rungs. The first kills J. The second ties the down tower to the up tower.

A replacement must therefore:
- keep a reflection-type CP exact in the strong sector, so that det(M_u M_d) stays real;
- break it in the CKM phase only, through a sector-dependent structure, which is Nelson-Barr-type (literature: Nelson 1984, Barr 1984; parity solutions such as Babu-Mohapatra);
- give up and down different contact weights, or different rung spacings, by a rule.

None of this is in CL-1 to CL-3.

## Boundary

Not claimed:
- that no other rung reading exists;
- rung ranges beyond 0..8 in the class scan (beyond c = 20 for self-mirror layouts);
- non-monotone paths;
- running between scales;
- leptons and neutrinos;
- any statement about the axion or bare theta.

The classification in item 9 is enumerated, not proved for all rungs, and only items 1-4, 10 and 11 are exact for all layouts in their classes. The dressing slowdown per factor is the register's estimate, not rederived here.

## Supplied vs forced

Forced, given the rule: items 1-4, the family blindness in items 5-7, the Hermitian structure of item 8, and the class properties in items 10 and 11.

Supplied:
- the path-sum rule, its phase form, lam and theta;
- the slowdown (2S/(2S+1))^2 and the S values;
- the multiplet factor sets and the octree 16 per rung;
- the rung ranges and the three seeded samples;
- measured values as in `flavour-rule` (running quark masses at M_Z, |V_us| 0.2243, |V_cb| 0.0411, |V_ub| 0.00382, J 3.08e-5).

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Candidate-law register](CANDIDATE_LAWS.md): CL-1 copy sign (undressed even cubes), dressed-cone clause, link registers on role blocks B_f, split, AX-2; the octree rung-ladder entry (one 16 per rung, supplied).
- Context: `flavour-rule` (#9998; path sum, eps = 2^(-3/2), rank = number of ranges), `family-charge-search` (cyclic ceiling), `mass-tower-law` (#9960), #9951 (zoom ladder adds no family charge), #9997 (one running coupling, fails the gate).

## How to run

```
python3 scripts/a_path_sum_flavour_rule_with_forced_rungs_is_family_blind_or_flat_and_its_structural_theta_bar_zeros_kill_cp_or_tie_down_to_up_2026_10_22.py
```

Seeded (20261022), runtime about 2-3 s, peak memory about 36 MB, AUDIT_TIMEOUT_SEC = 120, output 4.4 kB. Expected: TOTAL: PASS=16 FAIL=0. Run through scripts/runner_cache.execute_runner from an origin/main worktree, it returned status ok, exit code 0, in 3.0 s.
