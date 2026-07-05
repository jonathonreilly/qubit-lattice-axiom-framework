# D = 3 Single-Band Orbital-Response Decomposition Bounded Theorem Note

**Date:** 2026-06-13
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_d3_orbital_response_decomposition_2026_06_13.py`
**Runner cache:** `logs/runner-cache/frontier_d3_orbital_response_decomposition_2026_06_13.txt`
**Status:** source proposal; the audit lane grades.
**Native prefactor dependency:**
[`LANDAU_PEIERLS_PREFACTOR_NATIVE_DERIVATION_BOUNDED_THEOREM_NOTE_2026-06-13.md`](LANDAU_PEIERLS_PREFACTOR_NATIVE_DERIVATION_BOUNDED_THEOREM_NOTE_2026-06-13.md)
**Normalization boundary dependency:**
[`D3_LANDAU_PEIERLS_SINGLE_BAND_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md`](D3_LANDAU_PEIERLS_SINGLE_BAND_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md)
**Status authority:** independent audit lane. This source note does not set or
predict an audit outcome and does not edit audit-owned registry, ledger, queue,
or publication-status surfaces.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane owns status.

## Claim

For the free spinless single-band cubic nearest-neighbor model on the
cubic `Z^3` lattice, the finite-torus small-field orbital grand-potential
response for a uniform Peierls field through the xy plaquettes is tracked by
the `d = 3` Landau-Peierls intraband term, with the single-band interband term
equal to zero.

2026-06-18 repair: the Landau-Peierls coefficient used by the runner is no
longer a raw textbook input inside this packet. The runner consumes the exact
rational exported by the source companion
[`LANDAU_PEIERLS_PREFACTOR_NATIVE_DERIVATION_BOUNDED_THEOREM_NOTE_2026-06-13.md`](LANDAU_PEIERLS_PREFACTOR_NATIVE_DERIVATION_BOUNDED_THEOREM_NOTE_2026-06-13.md)
via `scripts/frontier_landau_peierls_prefactor_native_derivation_2026_06_13.py`.
Independent audit still owns whether that companion becomes accepted support;
this note only queues the D3 decomposition for re-audit with the dependency
made explicit.

At the reference point `L=32`, `mu=-2.0`, `T=0.30`, the measured residual is

```text
finite-torus Richardson reference  chi_exact = -3.971713231636e-03
Landau-Peierls 3D BZ integral      chi_LP    = -3.949577202602e-03
single-band interband term         chi_inter = +0.000000000000e+00
decomposition residual             chi_LP + chi_inter - chi_exact
                                             = +2.213602903391e-05
relative residual vs reference                = 5.573420774086e-03
```

Thus this run is bounded finite-lattice evidence for the Landau-Peierls
orbital-response decomposition in this `d = 3` single-band free-fermion
setting. It closes to about `0.557%` at the stated reference point. Across the
sampled `chi(mu)` curve, the worst-case relative residual is about `0.61%` (at
`mu=0.000`, the band center where Euler-Maclaurin discretization error is
largest); see the curve table below.

## Scope

The scope is deliberately narrow:

- cubic periodic lattice, side `L=32`;
- nearest-neighbor hopping `t=1`;
- one orbital and one band, so `chi_inter = 0`;
- spinless normalization with unit charge, hbar, c, and lattice spacing;
- finite temperature `T=0.30`;
- Peierls flux through xy plaquettes, with quantized periodic-torus flux
  `B = 2*pi*p/L^2`;
- grand-potential response density at fixed `mu,T`, computed as
  `(Omega(B) + Omega(-B) - 2 Omega(0)) / B^2`.

No fitted scalar prefactor is used. The Landau-Peierls cell normalization is
the companion runner's derived exact rational `-1/12`, the spinless unit-flux
grand-potential second-derivative normalization. The same normalization
convention is cross-recorded in the D3 normalization boundary note linked
above; the computation below uses the native companion's returned rational.

```text
chi_LP = -1/12 * integral_BZ f'(E(k))
         * [E_xx(k) E_yy(k) - E_xy(k)^2] d^3k/(2*pi)^3
E(k) = -2 (cos kx + cos ky + cos kz)
E_xx E_yy - E_xy^2 = 4 cos(kx) cos(ky)
```

## Dependency Boundary

The prior source packet used the standard Landau-Peierls single-band formula
and its `-1/12` spinless unit-flux normalization as explicit theory inputs.
This repair removes the hidden-input role for the scalar: the D3 runner now
imports the companion symbolic derivation, checks its exact rational
`-1/12`, checks the divergence identity residual, and computes the D3
Brillouin-zone integral with that returned value.

This does not audit or promote the companion packet. Until the independent
audit lane accepts the companion native-prefactor theorem, the honest status
of this D3 note remains a source proposal with an explicit source-side
dependency. The D3 normalization boundary note remains a source-side
cross-check for the Peierls convention and the "no new axiom / no fitted
scalar" boundary. The finite-torus Peierls reference remains independent of
the Landau-Peierls formula and still tests the resulting decomposition at the
frozen D3 points.

## Finite-Torus Reference

The runner constructs the real periodic finite-lattice Peierls Hamiltonian with
the boundary seam required for uniform flux on a torus. The exact `d = 3`
spectrum
is obtained by direct diagonalization of the xy Peierls Hamiltonian and exact
addition of the decoupled z spectrum. A small `L=4` full 3D Hamiltonian
diagonalization checks this block decomposition directly.

Measured reference diagnostics:

```text
uniform xy flux p=1 max plaquette error  = 7.112e-16
uniform xy flux p=2 max plaquette error  = 1.342e-15
L=4 full-vs-block spectrum mismatch      = 7.105e-15

B_fine   = 6.135923151543e-03
chi_fine = -3.967221285726e-03
B_coarse = 1.227184630309e-02
chi_coarse = -3.953745447998e-03
chi_richardson = -3.971713231636e-03
step-halving error = 1.347583772820e-05
Richardson correction = 4.491945909400e-06
```

The finite-torus reference is nonzero and stable under the frozen
B-step-halving gate.

## Sign Tracking

The measured chi(mu) curve shows the expected d=3 sign changes across the
band, and the Landau-Peierls integral tracks the exact finite-lattice signs at
all active sampled points:

```text
mu       exact chi             LP chi                residual
-4.500   +6.422959259094e-03   +6.417363451737e-03   -5.595807356714e-06
-3.000   +2.938363909774e-03   +2.935171660751e-03   -3.192249022337e-06
-1.500   -6.975372395063e-03   -6.947962345371e-03   +2.741004969162e-05
+0.000   -9.635406290307e-03   -9.576734049665e-03   +5.867224064285e-05
+1.500   -6.975372398012e-03   -6.947962345371e-03   +2.741005264046e-05
+3.000   +2.938363946634e-03   +2.935171660751e-03   -3.192285882769e-06
+4.500   +6.422959248036e-03   +6.417363451737e-03   -5.595796298580e-06
```

## Gates

The runner declares all tolerances before computing spectra or integrals. Its
load-bearing gates include consumption of the native prefactor companion, the
source-normalization boundary anchors, the finite-torus reference
construction, a sub-`1%` relative residual at the reference point, sign
tracking across the sampled `chi(mu)` curve, and a sub-`1%` active relative
residual across that curve. The passing run reports:

```text
TOTAL: PASS=13 FAIL=0
```

## Re-audit Handoff

The 2026-06-18 source repair targets the audited-conditional blocker that this
note imported the standard Landau-Peierls formula and `-1/12` normalization.
The requested re-audit question is now narrower:

- first grade the companion native-prefactor packet as a source-side bounded
  theorem or identify its remaining import;
- then grade whether this D3 packet cleanly consumes that companion, the
  normalization-boundary note, and its own finite-torus Peierls reference,
  without fitting or hiding a textbook scalar.
