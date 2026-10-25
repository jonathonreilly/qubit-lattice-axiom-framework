---
claim_id: the_one_family_u1_anomaly_passes_luschers_zero_momentum_tests_on_lattices_to_24_but_its_momentum_space_locality_test_is_scale_limited_at_m0_1p6_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "U(1)_Y covariant anomaly density of the Wilson-kernel overlap (r = 1) for the one-family 16 and a lone L doublet, in axis-restricted factorised backgrounds (U2 = exp(i th2(x1)), U4 = exp(i th4(x3))), on L x T x L x T lattices with L = 6..24 along x1, x3 and T = 24 (16 for L = 24) along x2, x4; exact block sign(H). Exact: block method = full 4D (6e-15), GW per block. Integers (6^4, full dense): indices -(6Y)^2 for 6Y = 1..6, all resolved; the 16's flux integral is 0 from measured integers; lone doublet -18. Finite diagnostics: isotropic small tori are Polyakov-loop dominated for the 16 (holonomy shift flips its sign); at m0 = 1.6 the per-charge kernel and the 16's single-mode coefficient carry a slow scale (finite-size rate ~0.3/site) and the pre-set momentum-space locality criteria P1, P2, P4, P4b, P5 are NOT met at L <= 24 (P3 partly, P6, P7 met); post-hoc at m0 = 1.0 the 16's coefficient is -9e-7 at |p| = 0.39 (7e-5 |gamma_L|) and falls faster than p^2 while the doublet tends to gamma_L. Not covered: the measure construction, non-abelian locality, the gauge-field integral, general (non-axis) backgrounds, momenta below |p| = 0.26."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_u1_hypercharge_anomaly_of_the_one_family_overlap_passes_luschers_zero_momentum_condition_but_finite_range_current_fits_on_4_to_the_4_cannot_test_locality_bounded_theorem_note_2026-10-24
  - the_overlap_chiral_determinant_in_su2_x_u1_backgrounds_cancels_the_family_gauge_anomaly_through_cubic_order_and_in_every_measured_index_but_a_single_doublet_does_not_bounded_theorem_note_2026-10-23
  - the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_bounded_theorem_note_2026-10-23
runner: scripts/the_one_family_u1_anomaly_passes_luschers_zero_momentum_tests_on_lattices_to_24_but_its_momentum_space_locality_test_is_scale_limited_at_m0_1p6_2026_10_24.py
---

# The one-family U(1) anomaly passes Luscher's zero-momentum tests on lattices to 24, but its momentum-space locality test is scale-limited at m0 = 1.6

Claim type: bounded_theorem (exact lattice identities, measured integers, labelled finite diagnostics, two method
findings). Labels: [T] exact, [F] finite diagnostic, [S] reading. Runner: runner.py, TOTAL: PASS=14 FAIL=0, 68 s on
the laptop, peak RSS 131 MB, 5.2 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120, no data files read (the
Mac-mini results are an embedded JSON literal). Tested under a unique filename (scratch luscher_L8_test_run.py,
exit 0). Criteria written before any code (criteria_pre_run.txt), plus one dated set-up addendum written after the
isotropic runs and before any T = 24 run; the PASS criteria were not changed. Pre-set outcomes are reported as MET /
NOT MET; each runner check certifies the stated observation. Axioms unchanged; no rule proposed; no CL edit.

## Question

Route A (wizard w5): the chiral overlap theory with the field-dependent projector P_hat has a gauge-invariant local
measure if the 16's anomaly density is d*j with j a LOCAL gauge-invariant current (Luscher 1998/99, supplied). The
4^4 probe (luscher-local-current) could not test locality with finite-range fits and proposed a momentum-space test
on L >= 8. In momentum space: each charge has q_Y = 2 Y^2 T + d*k_Y; the 16's Fourier kernel must vanish at zero
momentum analytically (like p^2), a lone doublet's must not (it keeps 2 sum m Y^3 /(4 pi^2) = gamma_L).

## Repo check

- No main note does a momentum-space Luscher test (git grep "luscher" on origin/main: only RP / y_t / prompt-log
  hits). Open PRs used: #10049 (overlap-from-walk: P_hat, free-kernel decay exp(-0.72 d)), #10051
  (overlap-nonabelian: kernel, m0 = 1.6, order-4 residual), #10052 (overlap-colour).
- Builds on luscher-local-current (same kernel, conventions, T normalisation) and replaces its proposed method.

## Set-up

- Kernel X = D_W - m0, r = 1, m0 = 1.6 (copied); H = g5 X; q_Y(x) = tr sign H_Y(x,x); A = sum m Y q_Y.
- Axis-restricted factorised backgrounds: U1 = U3 = 1, U2 = exp(i th2(x1)), U4 = exp(i th4(x3)); F12 = F(x1),
  F34 = G(x3). H commutes with x2, x4 translations, so it is EXACTLY block diagonal in (p2, p4); each block is 4L^2
  and sign H is computed by dense eigh per block. This is exact, so the sparse/Zolotarev approximation proposed in
  the earlier note is not needed.
- M1, order-2 kernel (one charge-1 Weyl): random-phase th2, th4, 4-sign combination, Richardson in eps (0.02,
  0.04); Pi (potential kernel), Q~ = Pi~/((e^{iP1}-1)(e^{iP3}-1)), Q by exact partial sums, Luscher-split currents
  K1, K3 of Q - gamma delta (d*K = Q - gamma delta exactly).
- M2, finite field: single mode F = eps cos(p x1), G = eps cos(k x3), eps = 0.3; R = 4 x (Fourier coefficient at
  (p,k))/eps^2, with the half-site phase removed. Exact zeros at p = pi or k = pi (reflection about a site).
- M3: unit flux (charge unit 1/6) in both planes on 6^4, full dense 5184-dim eigvalsh.
- Mac mini: about 6 h of single-thread jobs (4 at a time, nice 10); peak about 2 GB.

## Results

Exact and integer:
- K1 [T]: block density = full 4D density on 4^4 (6e-15); GW and sign(H)^2 = 1 per block (4e-15).
- P7 [T/F]: on 6^4 the indices for 6Y = 1..6 are -1, -4, -9, -16, -25, -36 (min |gap| 0.43). That includes e^c,
  which 4^4 and 5^4 could not resolve. The 16's flux integral is exactly 0 from MEASURED integers (first time); the
  lone doublet gives -18.

Finite-volume finding (method):
- F1 [F]: on isotropic tori the single-mode backgrounds carry large x2/x4 Polyakov phases (L Y th2, with
  th2 ~ eps/p). On 8^4, a pure holonomy shift th -> th + pi/8 (no field-strength change) moves R16(pi/4, pi/4) from
  -1.12e-3 to +3.03e-3. The isotropic 16 data are therefore finite-volume dominated.
- With T = 24, the same shift changes R16 by 0.25%. At L = 12, T = 16 / 24 / 32 give 7.808 / 7.683 / 7.680 e-4.
- [S] Flag: earlier isotropic 4^4 / 5^4 16-densities (overlap-nonabelian, luscher-local-current) were not checked
  against this artefact. Their eps^4 scaling suggests a modest effect there, but this probe did not test it.

Per-charge order-2 kernel at m0 = 1.6 (T = 24):
- Envelope of |Pi| is exponential, but two scales are present: fitted xi = 0.76, 0.83, 0.91 at L = 10, 12, 16.
- Common momentum (pi/2, pi/2): |Q~_12 - Q~_16| = 1.3e-4 gamma.
- Zero-momentum value sum_ab Q / (2/(4 pi^2)) - 1 = -24.9, -14.4, -8.0, -4.4, -1.2 % for L = 6, 8, 10, 12, 16. This
  is exponential convergence at rate 0.33 per site; the two-point extrapolation gives +0.00%.
- On L = 16 the Luscher-split current kernels are exponentially local: tails 2e-4 gamma, xi(K1) = 0.95.
- The doublet's would-be gauge-invariant current has a NON-decaying tail equal to |gamma_L|(1 + dS): -1.2% at L = 16.
- Doublet single-mode R_L/gamma_L on the diagonal: 0.922 at s = sin^2(p/2) = 0.017 (L = 24), 0.842 at 0.038. The
  linear extrapolation is 0.986.

The 16 at m0 = 1.6 (eps = 0.3, T = 24; L = 24 at T = 16), diagonal p = k:

| s | 0.017 (L24) | 0.038 (L16) | 0.067 (L12) | 0.146 (L16) | 0.25 (L12) | 0.31 (L16) | 0.5 |
|---|---|---|---|---|---|---|---|
| R16 (1e-4) | 3.71 | 6.47 | 7.68 | 6.91 | 4.22 | 3.15 | 1.04 |

- R16 peaks near s = 0.07 (|p| ~ 0.5) and turns down; the local s-exponent rises from 0.30 to 0.69 toward small s.
- Finite size: L = 12 vs 16 at (pi/2, pi/2) differs by 6e-5 of max|R16| (P6 met). L = 8 vs 16 at (pi/4, pi/4)
  differs by 8%.
- eps-scaling exponents 3.77, 3.95 at s = 0.146, 0.5, but 3.43 at s = 0.067.

Post-hoc control at m0 = 1.0 (same everything else, not a pre-set criterion):
- R16 = -9.0e-7 at s = 0.038 (L = 16). That is 7e-5 |gamma_L| and 1.4e-3 of the m0 = 1.6 value.
- R16 = -9.5e-6 at s = 0.067, and -4.5e-5 at s = 0.146 (L = 8 and 16 agree to 4%). It falls faster than p^2
  (|p|-exponent 5.8 between L = 16 n = 1 and 2) and is order eps^4 (exponent 4.28).
- The doublet tends to gamma_L: R_L/gamma_L = 0.919, 0.863, 0.724, with linear intercept 0.985.
- Per-charge zero-momentum value: -1.8% at L = 8 and -0.10% at L = 12 (against -14.4% and -4.4% at m0 = 1.6).

## Against the pre-set criteria

| criterion | outcome |
|-----------|---------|
| P0 exactness/validation | MET |
| P1 xi L-independent within 10% / common momentum <= 1e-3 gamma | NOT MET (18% spread) / MET (1.3e-4) |
| P2 sum Q within 1% for L >= 10 | NOT MET (-8.0, -4.4, -1.2%); converges, extrapolates to +0.00% (post-hoc) |
| P3 current tails < 1e-3 gamma, xi within 15% | PARTLY: tails and K1 met; K3 on the pre-coded range not (construction-forced point) |
| P4 doublet plateau = |gamma_L| within 2% on every L | NOT MET for L <= 12; met at L = 16 (-1.2%); the tail never decays |
| P4b doublet intercept within 3% (pooled cubic fit) | NOT MET (0.905); small-s linear 0.986 (post-hoc) |
| P5 16 intercept and exponent in [1.6, 2.4] | NOT MET at m0 = 1.6 (exponent 0.10; R16 not yet in its p^2 regime) |
| P5b eps^4 within 0.3 | met at s = 0.146, 0.5; not at s = 0.067 |
| P6 16 finite size <= 1e-2 at L = 12 | MET (6e-5) |
| P7 flux integers | MET (all six resolved) |

## Answer

| question | answer |
|----------|--------|
| does the 16's density vanish at zero momentum? | yes, exactly: measured flux integers (6^4) give integral 0, and the per-charge zero-momentum coefficient converges to 2/(4 pi^2), which the 16 cancels (sum m Y^3 = 0) |
| does it vanish like p_mu j_mu with j analytic? | at m0 = 1.6: not demonstrated at L <= 24 (R16 still near its peak at s = 0.017-0.07, turning down); at m0 = 1.0 (post-hoc): yes in the measured range, faster than p^2, to 7e-5 of the doublet's value |
| does the lone doublet fail? | yes: R_L -> gamma_L != 0 (1/p pole of j), non-decaying current tail = |gamma_L|, flux integral -18 |
| why is m0 = 1.6 slow? | [S] finite-size rate ~0.3/site in every m0 = 1.6 quantity, matching the near-doubler Wilson mass 2 - m0 = 0.4 (smallest gap, 0.40 on 4^4); at m0 = 1.0 the same quantities converge in a few sites |

## What this establishes, and what remains

- Establishes [T/F]:
  - the exact block method;
  - six flux integers including e^c, and the 16's measured zero;
  - the Polyakov-loop artefact of isotropic tori (a method negative: isotropic small tori must not be used for the
    16's density);
  - exponential locality of the per-charge kernel and its Luscher-split currents on L = 16;
  - the doublet's non-decaying current tail;
  - at m0 = 1.0, a 16 density at small momentum that is consistent with d* of a local current.
- Does NOT establish:
  - the measure term;
  - the m0 = 1.6 p^2 regime. That would need |p| < 0.2, i.e. L >= 32 at T >= 24 (days of single-thread mini time per
    point), or the m0 = 1.0 kernel;
  - locality in non-axis backgrounds;
  - admissibility (F up to 0.3, above Luscher's proof bound);
  - non-abelian locality (known only to all orders of perturbation theory, supplied);
  - the gauge-field integral.
- Recommendation [S]: run route-A tests with m0 = 1.0, or any m0 well away from 2, where 4^4-12^4 already reach
  the asymptotic regime. m0 = 1.6 is legitimate but has a slow near-doubler scale.

## Smuggling review

- Supplied:
  - U(1)_Y and the 16's hypercharges (test inputs; as rule content they would fail gate criterion 2);
  - the kernel and m0 = 1.6, plus m0 = 1.0 as a post-hoc control;
  - the axis-restricted background class, eps, T = 24 and the fits;
  - Luscher's theorem and the normalisation of T.
- Forced: GW and the index identities, the integers, sum m Y^3 = 0, the exact zero at p = pi, and the
  holonomy-shift result.
- Post-hoc (labelled): the T = 24 addendum (written before T = 24 data), the m0 = 1.0 control, the exponential
  extrapolation, and the small-s linear doublet intercept.
- Gate: N/A (no rule). Route A stays open. Its U(1) zero-momentum premise is now measured with all integers, and
  its locality premise is supported at m0 = 1.0 but not demonstrated at m0 = 1.6.

Uses: luscher-local-current (kernel, conventions, normalisation; its proposed next test, carried out here),
overlap-nonabelian (kernel), overlap-from-walk (P_hat, locality), wizards w5 approach 3.
Narrows: luscher-local-current's "sparse sign(H) needed" (not needed: exact block decomposition). Flags the
isotropic-torus Polyakov-loop artefact for the earlier small-torus 16 densities (untested there).
