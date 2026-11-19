---
claim_id: record_and_clock_split_triggers_are_fixed_schedules_and_no_memoryless_local_shift_holds_every_stationary_state_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's split trigger and the shift (label motion) under the tied lapse h_00 = -h_kk/3, in linear ADM on flat space with one Fourier mode: a trigger that counts records (one per site per half-tick, ticks global), ticks, proper time or 4-volume per split is a fixed schedule, and no schedule of the form log2 a = t/tau + c tracks a supplied radiation-then-matter expansion history (32.3 octaves from 1 s to today) within the 4-octave window (best miss 14.0 octaves, an estimate); the volume of a block of fixed sites changes only through boundary displacements, so block volume is not displacement-invariant; keeping the tied lapse under x -> x + xi forces d_t xi^0 = div(xi)/3, so a spatial relabelling drags the slicing (symbolic); radiation FRW has Ricci scalar 0 with H != 0, so a curvature invariant cannot trigger splits (symbolic); a uniform trace-free extrinsic curvature is kept static only by beta = K.x + Killing, so no memoryless local shift holds every stationary state (symbolic). Finite diagnostics on seven shift laws (zero, minimal strain, harmonic, strain drivers at eta = 0, 0.5, 5, a static-compatible value driver): all gauge speeds <= 1; zero shift winds the edges linearly around a stationary current; undamped memory drivers tilt the slice linearly around a static source; the value-driver family is stable only for a supplied mu1 < 1/4; damping bounds the tilt but leaves a rotating strain offset 2 eta K/(mu k^2). In a planar shear toy (64 layers) zero shift with one-cube slips at shear 1/2 keeps every cube within shear 1/2. Estimates against measured rotators, a magnetar, Sgr A* and a quasi-static collapse are estimates. Supplied model, finite diagnostic: linear ADM, the dust and current sources, the driver families and their parameters, the expansion history, the measured J, R and ages, the planar toy."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/record_and_clock_split_triggers_are_fixed_schedules_and_no_memoryless_local_shift_holds_every_stationary_state_2026_10_22.py
---

# Record and clock split triggers are fixed schedules, and no memoryless local shift holds every stationary state

Claim type: bounded_theorem.
Primary runner: `scripts/record_and_clock_split_triggers_are_fixed_schedules_and_no_memoryless_local_shift_holds_every_stationary_state_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) splits an edge when a trigger fires and ties the lapse to the edges (h_00 = -h_kk/3 in linear form); its actuality law (CL-2) lays one record per site per half-tick. The split trigger must be causal (read only local, already-settled data) and must not need supplied gauge parameters. This note asks what a trigger can read, and which shift (label motion) keeps the trigger causal without parameters. Units: 8 pi G = c = 1 in the linear model; one Fourier mode k = 1 along z. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. What a split trigger can read.

1. One record per site per half-tick with global ticks makes "split after N records" a fixed schedule, as are N ticks and a fixed proper time or 4-volume per split. A schedule log2 a = t/tau + c does not track a supplied expansion history (radiation then matter, t_eq = 5.1e4 yr, t0 = 4.35e17 s) from 1 s to today within the 4-octave window, for any tau in 1e-2 to 1e18 s and the best offset c. This is an estimate against the expansion history; other schedule shapes are not scanned.
2. A block of fixed sites changes volume under a displacement only through its boundary (the flux of xi): interior moves leave it invariant to first order, boundary moves do not. Block volume is not displacement-invariant.
3. Keeping h_00 = -h_kk/3 under x -> x + xi forces d_t xi^0 = div(xi)/3. A spatial relabelling drags the slicing, so the extrinsic curvature (delta K = -lap xi^0), the lapse, proper time and 4-volume at a label all respond at first order; a label-local trigger is causal only if the labels (the shift) are. The consequences after the first equation are stated, not computed.
4. Radiation FRW (a ~ t^1/2) has Ricci scalar 0 with H = 1/(2t); it is conformally flat, so its Weyl tensor vanishes (stated, not computed). Expansion is not local curvature: a trigger must read a congruence (edges or their rate), not a curvature invariant.

B. Causal frames (linear ADM, rho or a stationary transverse current J switched on with consistent data; evolution to T = 400 by exact matrix exponentials).

5. Zero shift: every gauge speed is at most 1 (the runner states the speeds 1, 1/sqrt3, 0 and checks the maximum), the static star stays bounded, but a stationary current winds the edges linearly (h_xz = -2 K_xz t with R_xz = 0, stated).
6. Minimal strain (the shift solved from d_j hdot_ij = 0): bounded for both sources. Its only fault is the instantaneous elliptic solve.
7. A uniform trace-free extrinsic curvature satisfies the momentum constraint and is kept static only by beta = K.x plus a Killing field. A shift that is a local function of the fields at a point is constant where the fields are uniform (stated), so no memoryless local shift unwinds every stationary state.
8. With memory but no damping (harmonic labels, the strain driver at eta = 0) every gauge speed is at most 1 and rotation stays bounded, but around a static source the shift grows linearly: a slice tilt running towards null.
9. Value drivers d_t beta_i = mu1 d_j h_ij + mu2 d_i h have longitudinal speed omega^2 = k^2 (1 + 6(mu1 + mu2))/3. A static tied-lapse source (h_zz = 10U, tr h = 6U) is stationary only if mu2 = -5 mu1/3; then omega^2 = k^2 (1 - 4 mu1)/3, stable only for mu1 < 1/4, a supplied parameter, and only for Psi = Phi.
10. Damping eta > 0 bounds the static tilt (beta = 10 mu U k/eta), but an overdamped driver leaves a rotating strain offset h = 2 eta K/(mu k^2): eta must sit in a window set by each system's size.

C. Slips (planar shear toy, 64 layers, 200000 ticks).

11. Relabelling every site above a layer by one cube when the layer's shear passes 1/2 (where the relabelled cube is less strained) keeps every cube within shear 1/2, with no rate parameter.
12. Simple shear keeps volume (det = 1, stated), so a volume trigger ignores the residual shear; the log-mean-edge trigger moves by at most the listed amount at shear 1/2.

## Derivation

Items 1 and 11-12 are numpy scans: item 1 fits log2 a(t) on 4000 log-spaced times by t/tau + c over 400 log-spaced tau and reports the half-range of the residual; item 11 advances layer displacements and applies the slip rule. Item 2 computes the volume of a 4^3 site block (27 cubes, five tetrahedra each) under random displacements of size 1e-6, interior sites only and all sites. Items 3, 4, 7 and 9 are sympy algebra (the gauge change of h_00 and h_kk; the FRW Ricci scalar; the symmetrised gradient of beta = (y, x, 0); the 5 x 5 longitudinal dispersion determinant factored at mu2 = -5 mu1/3). Items 5-10 build the 18-component linear system (h_ij, K_ij, beta_i, d_t beta_i) for each shift law, read gauge speeds from its eigenvalues, and evolve isotropic static data (rho = 1) and a stationary transverse current (J_x = 1), reporting the maxima of |h| and |beta| over the first and second halves of the run.

## Finite checks

Exact or closed-form checks (the runner asserts each):
- d_t xi^0 = (d_x X1 + d_y X2 + d_z X3)/3 (symbolic).
- Radiation FRW Ricci scalar R = 0 (symbolic).
- beta = (y, x, 0): momentum constraint holds and the symmetrised gradient equals K (symbolic).
- Value-driver dispersion polynomial factors as I omega (k - omega)(k + omega)(4 k^2 mu1 - k^2 + 3 omega^2)/3 at mu2 = -5 mu1/3, with root omega = k sqrt((1 - 4 mu1)/3).

Finite diagnostics (supplied model, finite diagnostic):
- Expansion history: 32.3 octaves needed; best fixed schedule misses by 14.0 octaves (window 4).
- Block volume: dV/eps interior-only 4.9e-07, all sites 4.59.
- Shift laws (max gauge speed; static source h and beta, first half -> second half; rotating h):

| shift law | max speed | growth rate | static h | static beta | rotating h |
|---|---|---|---|---|---|
| zero | 1.000 | 1.1e-16 | 11.0 -> 11.0 | 0.0 -> 0.0 | 400.0 -> 800.0 |
| minimal strain | 1.000 | 2.8e-17 | 1.0 -> 1.0 | 0.0 -> 0.0 | 0.0 -> 0.0 |
| harmonic | 1.000 | 2.8e-17 | 1.0 -> 1.0 | 200.0 -> 400.0 | 2.0 -> 2.0 |
| strain driver, mu1 = 1/3, eta = 0 | 1.000 | 3.4e-09 | 3.0 -> 3.0 | 133.9 -> 267.2 | 3.5 -> 3.5 |
| strain driver, eta = 0.5 | 1.000 | 1.4e-16 | 5.0 -> 5.0 | 4.0 -> 4.0 | 4.3 -> 3.0 |
| strain driver, eta = 5 | 1.000 | 3.2e-16 | 9.2 -> 5.0 | 0.7 -> 0.4 | 30.0 -> 30.0 |
| value driver, mu2 = -5 mu1/3, mu1 = 0.1 | 1.000 | 1.1e-16 | 11.0 -> 11.0 | 0.9 -> 0.9 | 6.3 -> 6.3 |

- Overdamped offset at eta = 5: rotating h -> 30.0, against the predicted 2 eta K/(mu k^2) = 30.
- Planar slips: max shear 0.500 against 9.5 unslipped; 630 slips for a total shear of 600.
- Log-mean edge at shear 1/2: d ln = +0.059.

The runner uses one seeded random draw (seed 1) for the block-volume displacements.

## Estimates against measurement

Estimates with supplied inputs (c = 2.998e8 m/s, G, measured angular momenta, radii and ages; window ln 16 = 2.77):
- Zero-shift winding 3 w_LT x age: Earth (J = 5.86e33, age 1.4e17 s) 1.4e+04; Sun (J = 1.9e41) 3.5e+05; Milky Way disk (J = 1e67, R = 3e20 m) 2.3e-04. Earth and Sun are wound out of the window by about 5e3 and 1e5 window widths (the runner asserts more than 100); the galaxy stays inside.
- Undamped drivers tilt to null in r/(10 mu c |U|): Earth 105 d, Sun 3.8 d, far below the ages.
- The static-compatible value driver (mu1 = 0.1) tilts to null around a magnetar (B = 1e15 G anisotropic stress, Psi - Phi ~ 1.5e-8) in 1.9 h, against ages of 1e3-1e4 yr.
- A constant eta cannot serve both a neutron star (tilt below c needs eta > 1.7e+04 /s) and spinning Sgr A* (offset below ln 16 needs eta < 8.7e-02 /s, spin 0.5 supplied); the linear formulas are applied at the horizon and are indicative only.
- Zero-shift collapse (quasi-static uniform ball, central lapse of the static interior solution): the centre reaches the lapse floor (1/16 to 1/8) when the surface is at 1.16-1.21 r_s. The runner compares this with a surface radius of 2.25 r_s for the event horizon reaching the centre, which it states and does not compute.

## Boundary

Not claimed: a trigger or shift law built on registers (only the linear continuum model is used); schedule shapes other than log2 a linear in t; nonlinear evolution; the slips in any geometry other than planar shear (rings and dislocations are not built here); the statements marked as stated (the speeds 1, 1/sqrt3, 0; h_xz = -2 K_xz t; the Weyl tensor of FRW; the downstream first-order responses of item 3; det = 1 of simple shear; the 2.25 r_s comparison); any physical reading of the driver parameters; the estimates beyond order of magnitude.

## Supplied vs forced

Supplied: linear ADM with dust and current sources; the tied lapse in the linear form h_00 = -h_kk/3; the driver families and their parameters (mu1, mu2, eta); the radiation-then-matter expansion history; the measured J, R and ages; the magnetar stress ratio; Sgr A* spin 0.5; the planar shear toy; the quasi-static collapse. Forced, given those: record, tick, proper-time and 4-volume triggers are fixed schedules; block volume responds to boundary displacements; d_t xi^0 = div(xi)/3; R = 0 for radiation FRW; no memoryless local shift holds a uniform trace-free extrinsic curvature static; the value-driver stability bound mu1 < 1/4 under the static condition; the overdamped offset 2 eta K/(mu k^2); shear at most 1/2 with planar slips.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's split trigger, window and tied lapse; the actuality law's one record per site per half-tick. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/record_and_clock_split_triggers_are_fixed_schedules_and_no_memoryless_local_shift_holds_every_stationary_state_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 60`, runs in about 2 s with about 100 MB resident, prints about 5.7 kB and ends with `TOTAL: PASS=17 FAIL=0`. Two repeated runs gave identical output.
