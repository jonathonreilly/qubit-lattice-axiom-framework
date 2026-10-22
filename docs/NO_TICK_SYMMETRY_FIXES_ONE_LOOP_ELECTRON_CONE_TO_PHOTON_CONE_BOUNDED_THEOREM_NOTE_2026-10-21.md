---
claim_id: no_tick_symmetry_fixes_one_loop_electron_cone_to_photon_cone_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "No symmetry of a translation-invariant finite-depth tick on Z^3 can fix the ratio of two species' dressed limiting speeds, and in 3+1 a null-direction tick gives no protection; for the supplied link law the one-loop electron cone sits below the photon cone by kappa alpha with kappa between -0.17 and -1.01 over the copy masses scanned; reading each species' step from its dressed cone is adopted, not derived."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/no_tick_symmetry_fixes_one_loop_electron_cone_to_photon_cone_2026_10_21.py
---

# No tick symmetry fixes the one-loop electron cone to the photon cone

Claim type: bounded_theorem.
Primary runner: `scripts/no_tick_symmetry_fixes_one_loop_electron_cone_to_photon_cone_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its tick law sets a shared step at which the tree-level cones of every species are the null cone of the cube edges, and its photon clause makes the photon's dressed cone the edge cone. This note computes the electron's one-loop cone under the register's link law and asks whether any symmetry of the tick can hold it to the photon's. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the tick nor the link law.

## Statement

1. The one-tick step set (81 displacements, both time senses) is preserved, together with the edge cone, by exactly 96 linear maps for every trial cone speed: the 48 cubic rotations and reflections, each with or without time reversal. All fix the time axis.
2. Any symmetry of a translation-invariant tick maps U to U or U^-1 and K to RK with R orthogonal. Such a map preserves w^2 = c^2 K^2 for every c, so it cannot fix c_e/c_gamma.
3. In 3+1 a tick written on null directions gives no protection: a metric-sign-flipping isometry needs equal inertia, which (1,1) has and (1,3), (3,1) do not.
4. For the register's link law the one-loop electron speed is off the photon's dressed cone by dc/c = kappa alpha, with kappa negative and between -0.17 and -1.01 over the copy masses scanned.

## Derivation

The stay step (one tick, no displacement) is the only step of its norm, so any map preserving the step set sends it to plus or minus itself; hence every such map fixes the time axis. Every step advances exactly one tick, so the Euclidean hypercubic turn t -> x, which the 4D hypercubic radiative-stability argument uses, cannot be a symmetry of any tick. Under the tick law the equality c_t = c_s of the kinetic-isotropy primitive therefore holds at tree level only. The symmetry argument covers the copy-mass CPT-type map, inversion, the 12 tetrahedral turns and the half-tick glide. The edge reading relates updates on different edge sets; it sets the tree-level cone but puts no constraint on how two species are dressed on the same edges.

In 1+1 the step-pi/2 tick dressed by any site phases is a site permutation times phases with displacements of exactly +-2 per tick, which is the 1+1 null-lattice protection. In 3+1 a power of any translation-invariant permutation tick is diagonal with phases linear in K, so its bands are planes and it has no cone. A cone needs interference, and link phases dress interference.

The one-loop computation uses the register's link law: Coulomb gauge, two transverse modes on the partition band, a straight-bond site-phase lift projected off the gauge orbit, and frame-block Coulomb exchange, with second-order Floquet perturbation theory. The Coulomb part runs with the continuum velocity log 2/(3 pi) and the transverse part with the opposite log. Because the tree cones are equal the logs cancel, so kappa is a finite lattice constant.

## Checks

The runner ends with `TOTAL: PASS=15 FAIL=0`. Among its lines:

- `[PASS] A1 real-space 8^3 tick = Bloch tick (M = 0, .5, 1); the copy mass leaves the light speed exactly sin(eps)/sqrt3; the partition (Yee) photon band equals the massless fermion band at every K`.
- `[PASS] A2 THEOREM: the one-tick step set (81 displacements, both time senses) is kept by exactly 96 cone-preserving linear maps for every trial cone speed`.
- `[PASS] A3 THEOREM: an isometry flipping the metric sign needs equal inertia: (1,1) in 1+1 has it ..., (1,3) vs (3,1) in 3+1 does not`.
- `[PASS] A4 bare-mass sensitivity of the light cone at mu = 0: zero without the copy mass ..., O(K^2) relative with it ...: mass and cone conditions are independent`.
- `[PASS] B1` to `[PASS] B4`: the engine matches an exact many-body toy (3.3e-6), a static field on a torus (converging as amplitude^2), a real-space Coulomb sum (2e-15) and the Ward identity (9e-18).
- `[PASS] C1 reference point eps = .3, M = .5: kappa is nonzero, O(1) and negative (electron slower than the photon), isotropic, p-independent, with no helicity splitting (no CPT-odd term)`: kappa = -0.8437 on an axis, -0.8415 on the diagonal, splitting 9e-15.
- `[PASS] C2 the Coulomb part runs with the continuum velocity log 2/(3 pi) per ln(1/p), the transverse part with the opposite log`: slopes +0.2062 and -0.2070.
- `[PASS] C3 continuous-time limit (eps = .05; r = M/eps): kappa(r) stays negative and O(1) for every copy mass, -0.17 when the copies are near-degenerate to -1.0 near r = 3`. kappa is -0.180, -0.217, -0.469, -1.011 and -0.897 at r = 0.1, 0.3, 1, 3, 10, and about -0.85 for a lattice-scale copy mass.
- `[PASS] C4 photon-law variants (eps = .05): at r = 10 every variant stays negative and O(1); at near-degenerate copies (r = .1) bcc Gauss law plus linear photon crosses zero: a one-loop zero can be tuned from supplied choices, not protected`.
- `[PASS] C5 with the photon faster by delta = .1 the electron speed runs towards it ... A = 0.346`.
- `[PASS] D1 a step is not a response variable: the vacuum phase falls monotonically with the step, so no stationarity of the total phase selects it; and the additive mass is unprotected`.
- `[PASS] E1 arithmetic: every kappa excluded by > 1e8 (LEP) and > 1e15 (LHAASO)`.

## Estimates against measurement

Without a fix, dc_e/c is between -7.4e-3 and -1.3e-3, with the photon faster than the electron; photons above 8 to 20 MeV would decay to e+e- in vacuum. This exceeds the LHAASO bound 3e-19 by 4e15 to 2e16 and the LEP bound 1e-11 by 1e8 to 7e8. The flow from the cell scale to the electron mass suppresses the offset only by a factor 0.88, and a tuned one-loop zero still leaves O(alpha^2) ~ 5e-5. With each species' step read from its dressed cone there is no dimension-4 offset by construction; the dimension-6 residual is about 3e-25 at 1.4 PeV, and the electron's bare step comes out 0.13 to 0.74% larger than the edge step. With a fixed bare mass angle, the additive mass would shift m_e by a factor of order 1e19, so the mass angle must also be read as a dressed value or be protected by chirality.

## Boundary

Supplied: the photon law (band, lift, gauge projection, Gauss law, frozen extra site-phase modes, continuous-time photon modes at the half-tick boundaries), the copy mass and step (scanned), the sea branch, one-loop perturbation theory, the photon cone taken from the register's photon clause, a cell size of 5 Planck lengths, and the measured bounds (estimates only). Forced: the symmetry results, the log cancellation, isotropy, the absence of helicity splitting, mass-cone independence, and kappa != 0 at every copy mass scanned for the register's law. Reading each species' step from its dressed cone is adopted to meet measurement, not derived; a vacuum-standard reading reduces to it because the dressing scales with charge squared. The size of kappa depends on the supplied law at O(1). Two loops and the quark and gluon sector were not computed. The cone problem is not the chirality problem: masses could be protected by chirality, but no tick symmetry protects cones.
