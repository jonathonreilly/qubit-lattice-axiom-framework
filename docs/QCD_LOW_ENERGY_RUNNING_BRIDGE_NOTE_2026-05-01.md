# QCD `v -> M_Z` Running Transfer-Map Kernel Theorem: domain-scoped, boundary-value-free

**Date:** 2026-05-01 (bounded source hint added 2026-05-24; boundary
narrowed 2026-05-25); repaired 2026-06-10 (re-scoped to the transfer-map
kernel theorem; numerical-match structure removed)
**Type:** bounded_theorem
**Claim scope:** A kernel theorem (K1)-(K5), quantified over the whole
admissible domain `D = [0.085, 0.130]`, about the `alpha_s` transfer map
`T : alpha_s(v) -> alpha_s(M_Z)` defined by the declared imports below.
The exact 1-loop map satisfies `1/T_1(a) = 1/a - L` with
`L = (7/2pi) ln(v/m_t) + ((23/3)/2pi) ln(m_t/M_Z) = 1.1746670551`, and
the 2-loop matched map `T_2` is grid-certified across `D` for
well-definedness, strict increase, expansivity, and a center-point inverse
round-trip. **No specific boundary value `alpha_s(v)` appears anywhere in
the claim.** PDG comparisons are confined to a labeled class-D appendix
and are not load-bearing.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:** `scripts/frontier_qcd_low_energy_running_bridge.py`

## Why this note exists

The previous revision of this note verified the standard SM running
transfer at one imported boundary value and checked the result against
the PDG world average. The 2026-05-25 independent review classified that
load-bearing step as a numerical-match case, with the rationale:

> However, the load-bearing result depends on the specific admitted value
> alpha_s(v)=0.103304 and fixed auxiliary boundary inputs, then checks
> agreement with the PDG comparator. Under the rubric tie-breaker,
> dependence on a chosen imported numerical boundary value makes this
> class G rather than a clean first-principles closure.

That criticism is correct: a claim of the form "this particular imported
number runs to the PDG value" is exactly the rubric's worked example of a
class-(G) numerical match, no matter how carefully the running is
implemented. The repair is a re-scope, not a patch. The honest content of
this row was never the boundary value — it is the **transfer map
itself**: the kernel that any accepted `alpha_s(v)` must pass through on
the way to `M_Z`. This revision states and verifies that kernel as a
theorem quantified over an entire domain, with no preferred input value,
and demotes every PDG comparison to a labeled appendix. Downstream rows
(e.g. the `alpha_s` derivation lane) need precisely this kernel; they
supply their own boundary value and own its provenance.

## Declared imports (the boundary of the bounded theorem)

The theorem below is **about the transfer map these imports define**; it
is not a derivation of `alpha_s` from the framework axioms. The imports
are:

1. **Continuum 2-loop SM MSbar RGE coefficients** — the standard
   Machacek-Vaughn (1984) / Arason et al. (1992) two-loop beta functions
   for `(g_1, g_2, g_3, y_t, lambda)`, used as published continuum
   infrastructure. The SU(3) group factors entering the gauge
   coefficient are **recomputed inside the runner** from the Gell-Mann
   generators: `T_F = 1/2` from the trace normalization
   `Tr(T^a T^b) = T_F delta_ab`, `C_A = 3` from the structure-constant
   contraction `f^{acd} f^{bcd} = C_A delta^{ab}` (with `f^{abc}` itself
   computed from commutators and verified totally antisymmetric), and
   `C_F = 4/3` from the fundamental Casimir. Hence the 1-loop coefficient
   `b0(n_f) = (11/3) C_A - (4/3) T_F n_f`, giving `b0(6) = 7` and
   `b0(5) = 23/3`, is **derived within the packet**, not asserted.
2. **Scales** — `v = 246.282818290129 GeV` (framework scale convention),
   `m_t = 172.69 GeV` (PDG top pole mass), `M_Z = 91.1876 GeV` (PDG).
   Only the top threshold lies between `v` and `M_Z`; the lower
   thresholds `m_b`, `m_c` are **not crossed and are not part of this
   note's claim surface** (the previous revision carried unused `m_b/m_c`
   threshold machinery, removed here).
3. **Auxiliary EW tuple** — `g_1(v) = 0.46228`, `g_2(v) = 0.65184`,
   `y_t(v) = 0.93737`, `lambda(v) = 0.13`, fixed declared inputs to the
   2-loop system. Theorem leg (K4) shows this tuple is **not a tuning
   knob**: 5% variations move `T_2` by less than `3.1e-6`, five orders of
   magnitude below the claimed structure.
4. **PDG band** `alpha_s(M_Z) = 0.1180 +/- 0.0009` — comparator only,
   quarantined in the class-D appendix.

## The transfer maps (definitions)

Write `a := alpha_s(v)` and `t := ln(mu)`. The 1-loop QCD running of
`1/alpha_s` is linear in `t` with slope `b0(n_f)/(2pi)`:

```text
d(1/alpha_s)/d ln(mu) = b0(n_f) / (2 pi),   b0(n_f) = (11/3) C_A - (4/3) T_F n_f .
```

- **`T_1` (exact 1-loop matched map).** Integrating from `v` down to
  `M_Z` with `n_f = 6` above `m_t` and `n_f = 5` below (leading-order
  continuous matching at `m_t`) gives the exact closed form

  ```text
  1/T_1(a) = 1/a - L ,
  L = (b0(6)/2pi) ln(v/m_t) + (b0(5)/2pi) ln(m_t/M_Z)
    = (7/2pi) ln(v/m_t) + ((23/3)/2pi) ln(m_t/M_Z)
    = 1.1746670551 .
  ```

- **`T_2` (2-loop matched map).** The map obtained by integrating the
  full 2-loop SM RGE for `(g_1, g_2, g_3, y_t, lambda)` from `v` to
  `M_Z`, with the same leading-order matching at `m_t` and the auxiliary
  tuple fixed at its declared values, then reading off
  `alpha_s(M_Z) = g_3(M_Z)^2 / 4pi`.

- **Domain.** `D = [0.085, 0.130]`, a wide window containing every
  physically discussed value of `alpha_s` at the electroweak scale (the
  PDG pullback window of the appendix sits well inside it).

## Kernel theorem (K1-K5)

**Load-bearing statement.** `1/T_1(a) = 1/a - L` with
`L = (7/2pi) ln(v/m_t) + ((23/3)/2pi) ln(m_t/M_Z) = 1.1746670551`
exactly. The 2-loop transfer map `T_2` is independently integrated and
grid-certified on `D = [0.085, 0.130]`: finite and positive at all grid
points, strictly increasing across the grid, expansive on every grid
secant, with a checked center-point inverse round-trip.

- **(K1) Well-definedness (Landau margin).** For all `a` in `D`,
  `1 - L a > 0`: the 1-loop Landau pole sits at `a* = 1/L = 0.8513`, a
  derived factor `(1/L)/a_max = 6.55` above the domain edge. Hence `T_1`
  is finite and positive on all of `D`, and the 2-loop flow integrates
  without singularity at all checked grid points on `[M_Z, v]`. *Proof:*
  exact algebra for `T_1` (the closed form above); grid verification for
  `T_2`.

- **(K2) Exact 1-loop closed form.** The closed form is not a fit: the
  separable 1-loop ODE integrates exactly to `1/T_1 = 1/a - L`. The
  runner confirms the closed form against an independent RK45 integration
  with residual at machine precision (~`6e-16` at the domain center, and
  below `1e-12` at every grid point), and cross-checks the 2-loop
  integrator against a second independent method (RK45 vs DOP853,
  agreement ~`4e-15`).

- **(K3) Monotonicity and expansivity certificate.** `T_1` obeys the
  exact Jacobian identity

  ```text
  dT_1/da = 1/(1 - L a)^2 = (T_1(a)/a)^2 > 1   on D,
  ```

  so `T_1` is strictly increasing and expansive on `D`. `T_2` is
  numerically certified on a uniform 10-point grid: the sampled values
  are strictly increasing, every grid secant slope is `> 1`, the central
  Jacobian is `J_2 = dT_2/da |_(a=0.1075) = 1.328`, and the center-point
  inverse round-trip `T_2^{-1}(T_2(a))` recovers `a` to `< 1e-9`.

- **(K4) Auxiliary-tuple insensitivity (anti-tuning).** Varying any one
  of `(g_1, g_2, y_t, lambda)` by `+/-5%` — or all four jointly — moves
  `T_2` at the domain center by `< 3.1e-6`. The auxiliary tuple is a
  declared import, not a tuning degree of freedom at the checked center
  point: nothing in the theorem is adjusted through it.

- **(K5) Truncation envelope.** At the domain center,
  `T_2 - T_1 = +5.7e-4`: the 2-loop correction to the exact 1-loop
  kernel is positive and bounded, and is quoted as the conservative
  truncation envelope of the kernel (the PDG reference running is
  4-loop; the 1-to-2-loop step bounds the order of the residual).

All five legs are stated on the declared domain `D`. The exact `T_1`
legs are analytic on `D`; the `T_2` legs are evaluated at the domain
center `a = 0.1075` and on the uniform 10-point grid, never at a
preferred imported boundary value.

### Falsifiability structure

Two falsification legs show the theorem has teeth:

- **Sign flip.** The sign-flipped kernel `1/T = 1/a + L` *contracts*
  (`T(a) < a`, Jacobian `< 1`): expansivity is a real property of the
  asymptotically free sign, not a tautology of the map's form.
- **Threshold removal.** Deleting the top threshold (running `n_f = 6`
  throughout) shifts `T_2` by `1.03e-3` — more than `1e4` times the
  two-integrator residual — and the matched map satisfies the **derived
  strict bracket**

  ```text
  T_2[n_f = 6 only]  <  T_2[matched]  <  T_2[n_f = 5 only] ,
  ```

  which follows from `b0(5) = 23/3 > b0(6) = 7 > 0`. (The previous
  revision's threshold "continuity check" compared a quantity to itself
  and was vacuous; this bracket replaces it with a non-trivial,
  sign-definite consequence of the flavor structure.)

## What the runner checks (test -> claim map)

`scripts/frontier_qcd_low_energy_running_bridge.py`, deterministic,
runs in about a second, `SUMMARY: PASS=27 FAIL=0`. Every check is tagged:

| Part | Checks | Class | Claim leg |
|------|--------|-------|-----------|
| 1 | 5 | A | SU(3) group factors `T_F = 1/2`, `f^{abc}` antisymmetric, `C_A = 3`, `C_F = 4/3` computed from Gell-Mann generators; `b0(6) = 7`, `b0(5) = 23/3` derived |
| 2 | 3 | A | (K1) `L` matches declared digits; Landau margin 6.55; `T_1` finite/positive on grid |
| 3 | 3 | A | (K2) closed form vs independent RK45 (center + grid); RK45 vs DOP853 two-integrator independence |
| 4 | 5 | A | (K3) exact `T_1` Jacobian identity; `T_2` grid monotonicity; grid-secanted expansivity with center Jacobian `J_2 = 1.328`; center inverse round-trip |
| 5 | 2 | A | (K4) single-parameter and joint 5% auxiliary variations `< 3.1e-6` |
| 6 | 4 | A | (K5) envelope `+5.7e-4`; derived threshold bracket; threshold-removal and sign-flip falsification legs |
| 7 | 3 | B | note/runner manifest sync (same `L`, same domain, same scales; boundary value confined to appendix) |
| 8 | 2 | D | labeled PDG comparator appendix (below) — **not load-bearing** |

Check-class mix: **A=22, B=3, D=2**. The class-D comparators are a
labeled minority; the previous revision's majority-load-bearing PDG
comparisons (0 C-passes, 8 D-passes) are gone. No class-C
(first-principles-from-axioms) claim is made anywhere: this is a bounded
theorem about declared imports.

## What this rules out

- Treating this row as a numerical match at a tuned input: the claim
  quantifies over all of `D` and contains no preferred boundary value.
- Treating the `-23/3` coefficient or the threshold structure as
  asserted-by-citation: `C_A`, `T_F`, `C_F`, and `b0(n_f)` are computed
  from the generators, and the threshold map is pinned by the derived
  strict bracket rather than a vacuous continuity identity.
- Treating the auxiliary EW tuple as a hidden tuning channel (K4).

## Not in scope (explicit non-claims)

- An analytic proof of global `T_2` monotonicity between grid points. The
  exact global statement is for `T_1`; `T_2` is the bounded
  runner-certified transfer kernel under the declared continuum imports.
- A framework-native derivation of `alpha_s(v)`, of the QCD beta
  function beyond the recomputed SU(3) group factors, of `M_Z`, or of
  `m_t`. These are the declared imports; the upstream plaquette /
  Wilson-loop lanes (`docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md`,
  `docs/ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md`,
  named by file path only — neither is a one-hop authority of this row)
  own the boundary-value problem.
- Any claim about scales below `M_Z`: the `m_b`/`m_c` threshold
  machinery of the previous revision is removed from the claim surface
  (declared unused; those thresholds are never crossed on `[M_Z, v]`).
- Precision beyond the 2-loop truncation envelope (K5).
- Promotion of any downstream `alpha_s(M_Z)` value to framework-derived
  status. A downstream row that feeds a boundary value through this
  kernel must cite its own retained-grade boundary authority.

### Adjacent threshold-kernel extension

`ALPHA_S_HEAVY_THRESHOLD_MATCHING_KERNEL_THEOREM_NOTE_2026-06-18.md`
proves the exact leading-order heavy-threshold continuity kernel on the same
SU(3) one-loop running surface. That extension is intentionally abstract: it
uses arbitrary positive threshold scales and proves the matching/composition
law, while leaving physical threshold placement and higher-loop MSbar
decoupling constants outside scope. This QCD-low bridge therefore remains a
`v -> M_Z` transfer-map theorem, but downstream alpha_s repair work can cite
the 2026-06-18 note for the native threshold-matching kernel instead of
importing that kernel as textbook machinery.

## Reuse rule

Downstream lanes may cite this note as the registered one-hop authority
for the `v -> M_Z` transfer kernel of `alpha_s`. What they inherit is
the kernel theorem (K1)-(K5): the exact 1-loop closed form on
`D = [0.085, 0.130]`, plus the bounded 2-loop grid certificate and
comparator appendix. Provenance of the boundary value is entirely the
consumer's obligation.

## Comparator appendix (class D; not load-bearing)

This appendix records external PDG context for downstream consumers. It
is no part of the kernel theorem and carries exactly two labeled class-D
runner checks.

- **PDG band pullback.** The PDG 2025 world average is
  `alpha_s(M_Z) = 0.1180 +/- 0.0009`. Because `T_2` is a strictly
  increasing bijection (K3), the band pulls back through the kernel to a
  unique boundary window

  ```text
  T_2^{-1}([0.1171, 0.1189]) = [0.10257, 0.10394]   (interior to D).
  ```

  Any future framework derivation of `alpha_s(v)` is PDG-compatible
  if and only if it lands in this window — a sharp, falsifiable target
  produced by the kernel, not a confirmation of any current value.
- **Worked example.** The historical plaquette-lane boundary value
  `alpha_s(v) = 0.103304` (the number whose load-bearing use made the
  previous revision class (G)) maps to `T_2(0.103304) = 0.118067`,
  inside the PDG band. Here it is one labeled example point inside the
  pullback window, nothing more; no load-bearing check evaluates at it.

## Standard infrastructure references

- M. E. Machacek and M. T. Vaughn, "Two-loop renormalization group
  equations in a general quantum field theory," Nucl. Phys. B 222, 83
  (1983); B 236, 221 (1984); B 249, 70 (1985).
- H. Arason, D. J. Castano, B. Kesthelyi, S. Mikaelian, E. J. Piard,
  P. Ramond, B. D. Wright, "Renormalization-group study of the standard
  model and its extensions: The standard model," Phys. Rev. D 46, 3945
  (1992).
- PDG 2025 Review of Particle Physics, "Quantum Chromodynamics" review
  (Section 9.4) — `alpha_s(M_Z) = 0.1180 +/- 0.0009` (comparator
  appendix only).

## Cited authorities (one hop)

None. No repository source note is load-bearing for this kernel theorem:
the theorem needs no boundary value, and all imports are declared
external infrastructure above. The plaquette and Wilson-loop lanes are
named by file path only (see "Not in scope"), preserving the no-back-edge
convention; the shared 2-loop RGE block also appears in
`scripts/frontier_yt_zero_import_chain.py` (file-path reference, not a
note citation).

## Changelog

- **2026-05-01** — original note: bounded numerical transfer of the
  historical boundary value through the standard 2-loop RGE, checked
  against the PDG average.
- **2026-05-24 / 2026-05-25** — bounded source hint added; boundary
  narrowed (plaquette note dropped as one-hop authority).
- **2026-06-10** — kernel-theorem re-scope (this revision), responding
  to the 2026-05-25 numerical-match classification:
  (a) **headline re-scoped** from "the imported value 0.103304 runs to
  the PDG average" (the rubric's worked example of class G) to the
  transfer-map kernel theorem (K1)-(K5), quantified over
  `D = [0.085, 0.130]`, with no specific `alpha_s(v)` anywhere in the
  claim;
  (b) **comparator demotion**: the old runner had 0 C-passes and 8
  load-bearing D-passes; the new mix is A=22, B=3, D=2 with the PDG
  comparators a labeled appendix minority;
  (c) **derived, not asserted**: `C_A = 3` and `T_F = 1/2` are computed
  from the Gell-Mann generators (structure constants + trace
  normalization), so `b0(5) = 23/3` is derived; the vacuous
  threshold-continuity check (which compared `g3(m_t)` to itself) is
  replaced by the derived strict bracket
  `T_2[n_f=6] < T_2[matched] < T_2[n_f=5]`;
  (d) **no preferred evaluation point**: load-bearing checks evaluate at
  the domain center `0.1075` and on a uniform 10-point grid; the
  historical value appears only in the comparator appendix;
  (e) **unused machinery removed**: the `m_b`/`m_c` threshold table is
  off the claim surface (never crossed on `[M_Z, v]`);
  (f) **runner rebuilt**: every check tagged [A]/[B]/[D] with residuals
  printed, two-integrator independence (RK45 vs DOP853), and two
  falsification legs (sign-flipped kernel contracts; threshold removal
  shifts `T_2` by `1.03e-3`, four orders above the integrator residual).
