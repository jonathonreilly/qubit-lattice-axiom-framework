# Declared dynamic check of whole-pair transport

2026-09-21. Written before production dynamic histories or their summaries
exist. This is a finite-size test of the conditional wave construction,
not a numerical proof of its limit or a fitted physical wave speed.

The generator is the full-matching color process of
`DIMER_ROUTED_RECORD_TRANSPORT.md`, gamma=1, k0=11/10, with all six routing
directions and the stated outer factor 1/2. Each nonfixed channel has rate
(22+5 h2)/40, h2=2h in {-4,...,4}. There are exactly 5K nonfixed directed
channels. The uniformization ceiling is 42/40 per channel. At each declared
observation interval, an independent Poisson number with mean
(5K)(42/40) times microscopic elapsed time is sampled, followed by that many
uniform channel attempts. Accept with integer probability (22+5h2)/42.
This samples the exact CTMC observation law without storing event times.

Every pair begins with a distinct immutable integer key and an independently
uniform color among fourteen labels. An accepted event exchanges pair keys,
not their fixed color lookup. Black and white records of that key travel
together as specified in the note. Continuous projector marks are not sampled;
this is the autonomous finite-color projection. Geometry stays fixed.

The declared side lengths are N=16,32,64,128, with respectively 256,128,64,32
independent histories per geometry, for 960 histories total. There are two
fixed geometries at each size:

- maximal winding: each black site pairs with its neighbor in +x;
- randomized columnar: begin with ordinary x-columnar dimers on consecutive
  even/odd x sites, then make exactly 8N^3 uniformly proposed plaquette flips
  with a fixed declared seed. This is a convenient irregular matching, not
  an asserted equilibrium sample. Zero accepted flips is a failed fixture.

The geometry generator, geometry bytes, production seeds, source and binary
hashes will be fixed in a manifest before dispatch. The code will verify each
matching, routing permutation, minimum nontrivial cycle length, and final
key permutation/color counts. A separate deterministic geometric decoder
and small-system stochastic validation precede production. Runtime-only
benchmarks may be used to choose concurrency, not sizes or scientific targets.
If resources prevent the declared run, report the missing histories; do not
silently select a successful subset. A change requires a dated amendment.

Macroscopic observation times are 0,7/16,7/8,21/16,7/4; microscopic time is
N times these values. Record the complex six-component pair Fourier fields
for each positive fundamental axis mode Q=2pi e_i, with K^(-1/2) normalization.
Let E=sqrt(7) X, B=sqrt(7) Y/2, so their initial component variances equal one.
The continuum target speed is c=2/7, hence the phase at these times is
0,pi/4,pi/2,3pi/4,pi. For each mode use the full six-by-six propagation matrix
with static longitudinal projections and the transverse cosine/cross blocks;
do not apply a cosine to all six components.

Prespecified primary quantities at every positive time and in each cell:

1. Mean squared norm of [E(t),B(t)] minus its continuum prediction from the
   same history's initial fields, divided by six. The target in the theorem's
   N->infinity limit is zero. Finite values need not decrease monotonically.
2. Transverse autocovariance, averaged over E/B and both transverse components,
   whose limiting value is cos(c|Q|t).
3. The signed E/B cross covariance contracted with the predicted cross-product
   matrix, whose limiting scalar value is sin(c|Q|t), with Fourier signs
   checked against the exact current matrix before analysis.
4. Longitudinal autocovariance, averaged over E/B, whose limiting value is one.

Also report equal-time E/B component variances, final key/count verification,
attempt/acceptance counts, and wall time. Report the three mode directions
separately and their equal-weight average; do not regard modes in one history
as independent replicates. The maximal-winding geometry can have strongly
anisotropic finite-size damping even when the limiting speed is isotropic.

Use sample means and standard errors across independent whole histories.
Use 10,000 fixed-seed whole-history bootstrap draws for pointwise 95% intervals
of the mode-averaged primary estimates; keep all modes/times from a history
together. No asymptotic exponent, damping formula, phase boundary, comparison
to experimental data, or significance-based selection is planned. The screen
does not verify the projector birth law, first-completion colors, quantum
coherence or a propagating geometric Gauss field.

All original outputs, failures, source identities and commands remain on
disk. A report distinguishes independent checks, complete data authentication,
and any selective replay. Passing this screen cannot replace the separate
proof review.
