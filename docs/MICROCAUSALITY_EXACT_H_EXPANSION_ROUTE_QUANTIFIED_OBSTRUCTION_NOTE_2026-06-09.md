# Microcausality Exact-H Bridge: Norm-Convergent Expansion Routes are Quantitatively Foreclosed on the Canonical Surface

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-09
**Claim type:** bounded_theorem (route-class obstruction; external thresholds as
comparators only)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary
declaration, not an audit verdict.
**Primary runner:**
[`scripts/microcausality_exact_h_expansion_route_obstruction_2026_06_09.py`](../scripts/microcausality_exact_h_expansion_route_obstruction_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/microcausality_exact_h_expansion_route_obstruction_2026_06_09.txt`](../logs/runner-cache/microcausality_exact_h_expansion_route_obstruction_2026_06_09.txt)

---

## Role

The parent microcausality note
[`AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md)
needs, at its (M2), a **quasilocal reconstructed Hamiltonian**
`H = -log(T)/a_τ`. The action-support bridge note
[`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
supplies the local action-density budget (`J_max = |m| + 78` on the canonical
surface) but leaves the exact-log step open, recording its higher-order
BCH/Trotter control as "the open frontier of this note" (its C4).

This note **triages the route classes** for that open step. There are two known
proof mechanisms for quasilocality of a generator reconstructed from local
layers:

1. **Norm-convergent expansion constructions** — BCH / Magnus / cluster
   expansions / small-step effective-generator constructions, whose
   hypotheses require the per-site layer norms (in units of the step) to lie
   below an `O(1)` convergence threshold;
2. **Spectral/analyticity constructions** — positivity of the transfer symbol
   plus momentum-space analyticity, yielding exponential tails by
   Paley-Wiener; this is the mechanism already instantiated for the free
   surface by
   [`RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md)
   (unaudited candidate; free `U=1` surface).

**Result (quantified): route 1 is foreclosed on the canonical surface.** The
canonical per-site budget exceeds every standard expansion threshold by
**1.28x (matter-only floor vs the exhibited minimal-pair radius) up to 112.5x
(full budget vs the BCH sufficient ball)**, and the failure is not a
vacuously-violated sufficient condition: the runner exhibits actual series
divergence at exactly the canonical norm scales, on a minimal pair whose
convergence radius (`|s*| = 1.8012`) it derives in closed form. The same
runner separates **method from object**: on a layered free chain at a coupling
6.7x beyond the radius, adding BCH orders makes the approximation *worse*
(order-4 error exceeds order-1), while the exact spectral log remains
well-defined and quasilocal (strictly positive Bloch symbol; measured
exponential tails). So nothing here suggests `H` fails to be quasilocal — the
conclusion is that **any proof of the (M2) exact-H step on the canonical
surface must come from the spectral/analyticity class**, as the free-surface
step already does. Runner: **13 PASS / 0 FAIL**.

The anisotropy escape is also quantified and closed off by the surface
selection: per-layer norms scale like `a_τ/a_s` at fixed spatial couplings, so
the expansion route's hypotheses are recovered only at
`ξ = a_s/a_τ >= 43.3` (exhibited pair radius) to `>= 112.5` (BCH ball) —
i.e. on the continuous-time horn, **not** on the canonical `ξ = 1` surface
supplied by the approved
[`kinetic_isotropy_primitive`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
and used by the B4 radiative-stability note
([`EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md)).
The two threads point the same way: Lorentz protection selects `ξ = 1`, and at
`ξ = 1` the exact-H bridge is a spectral problem, not an expansion problem.

## Statement

Let the canonical surface be the landed action-density surface of the bridge
note: `d = 4`, hop coefficient `1/2`, `r_W = 1`, `β = 6`, `N_c = 3`, per-site
action-density budget `J_max = |m| + 78`, with matter-only per-site floor
`|m| + d/2` (`= 2.3` at the bridge note's test mass `m = 0.3`).

**(O1) Minimal-pair convergence radius (derived).** For the minimal
non-commuting Euclidean pair `X = s·σ_x`, `Y = s·σ_z`, the BCH object
`Z(s) = log(e^X e^Y)` satisfies (exact arithmetic)

```text
    tr( e^{s σx} e^{s σz} ) / 2  =  cosh² s                                  (1)
```

so the nearest singularity of `Z(s)` — equivalently the convergence radius of
its Taylor/BCH series — sits at `cosh² s* = -1`:

```text
    |s*|  =  sqrt( ln(1+√2)² + (π/2)² )  =  1.80117...                       (2)
```

verified to 40 digits at the singular point and reproduced by a root test on
the series coefficients computed from the closed form.

**(O2) Divergence at the canonical scales.** The series for `Z(s)` converges
to the exact spectral log at `s = 0.3` (inside), and its terms `|c_n s^n|`
grow without bound at `s = 2.3` (the matter-only per-site floor) and at
`s = 78` (the full canonical budget above `|m|`) — by a factor `> 10²` and
`> 10⁶⁰` respectively between orders 20 and 60. The exact log exists at all
three values; it is the **expansion** that fails.

**(O3) Method-vs-object separation.** On a periodic layered free chain
(checkerboard layers, canonical hop coefficient `1/2`, one-particle sector,
`L = 96`):

- inside the convergent regime (`λ = 1`): the order-4 BCH partial sum beats
  order-1 by `~80x` (`err4/err1 = 0.0125`);
- beyond it (`λ = 12`, i.e. `6.7x` past the radius): order-4 is **worse** than
  order-1 (`err4/err1 = 1.23`) — adding orders hurts;
- at both couplings the exact log `H = -log(T_sym)` is well-defined and
  quasilocal **in principle and in practice**: its `2x2` Bloch symbol is
  strictly positive definite over the Brillouin zone (min eigenvalue
  `3.7e-1` at `λ = 1`, `6.1e-6 > 0` at `λ = 12`), which is precisely the
  positivity+analyticity input of the analytic-dispersion mechanism, and the
  measured tails decay exponentially (fit rates `1.46` at `λ = 1`, `0.29` at
  `λ = 4`).

**(O4) Budget-vs-threshold arithmetic and the ξ-line.** Exact gap factors on
the canonical surface:

```text
    matter floor  2.3 / ln 2      =  3.32          2.3 / 1.8012  =  1.28
    full budget   78  / ln 2      =  112.53        78  / 1.8012  =  43.31     (3)
```

Per-layer norms scale `∝ a_τ/a_s` at fixed spatial couplings, so the
expansion hypotheses are recovered only at `ξ >= 43.3` to `>= 112.5`; the
canonical surface has `ξ = 1`. (The bridge note's landed carrier-faithful
bracket extends the budget to `|m| + 78.5` and `|m| + 80` across Wilson
readings; every gap above only widens under those readings, so the
obstruction is reading-independent.)

**Conclusion.** Any quasilocality proof for `H = -log(T)/a_τ` on the
canonical surface lies outside the norm-convergent-expansion class. The
surviving class is the spectral/analyticity route — transfer-symbol
positivity plus dispersion analyticity — whose free-surface instance is
already on the books (2026-06-06 note above). The named open gate is its
gauged/interacting extension; this note does not supply that step.

## Derivation summary

**(O1).** `e^{sσx} = cosh s + sinh s·σx`, `e^{sσz} = cosh s + sinh s·σz`
(grade-2 algebra, exact), so the product trace is `2cosh²s` — eq. (1) is a
two-line exact computation, reproved by the runner in sympy. For `M` in
`SL(2)`, `log M` is analytic in `s` until an eigenvalue of `M(s)` crosses the
negative real axis, which happens exactly when `tr M/2 = cosh θ = -1`; with
eq. (1) this is `cosh² s* = -1`, giving eq. (2). The runner confirms the
radius by a coefficient root test (slow-converging from above; agreement
within 2.5% at order 60).

**(O2).** Series coefficients are computed from the closed form (Cauchy
integrals at 40-digit precision), then summed against the exact spectral log
inside the radius and term-tested outside. No literature input enters.

**(O3).** The chain transfer matrix is symmetrized,
`T_sym = e^{-λA/2} e^{-λB} e^{-λA/2}`, positive definite for every finite
`λ`; the exact log is computed spectrally and compared against explicit
Dynkin partial sums through order 4. The Bloch reduction uses the 2-site unit
cell; symbol positivity over a 4001-point Brillouin grid is the
positivity+analyticity input that guarantees exponential tails by the same
Paley-Wiener mechanism as the free-surface dispersion note (there via
`E(p) = arcsinh sqrt(m² + Σ sin² p_μ)`).

**(O4).** Pure exact arithmetic at 50 digits from the landed budget numbers
and the derived radius.

## Hypothesis set used

- **Landed action budget** —
  `MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`
  (F2): `J_max = |m| + 78` and the per-term composition (`d/2` hops, `|m|`,
  Wilson, `2β·q_face` plaquettes) on the canonical surface. Used as the
  norm scale only; nothing else is read from it.
- **Canonical surface `ξ = 1`** — the approved `kinetic_isotropy_primitive`
  (kinetic-form isotropy; the time-direction graining parallels spatial cubic
  adjacency). Used only to mark the `ξ >= 43-113` regime as off-surface.
- **Free-surface spectral instance** —
  `RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_..._2026-06-06.md`
  (unaudited candidate), cited as the existing member of the surviving route
  class, not as an authority for any claim made here.
- **Minimal-pair closed form, chain construction, all numerics** — derived
  in the runner from explicit matrices and exact arithmetic; no fitted
  parameters, no observed values, no cross-note numerical imports.

**Comparator citations (context only, reproved or replaced in-runner):** the
BCH sufficient convergence ball `‖X‖+‖Y‖ < ln 2` (standard Lie-theory
sufficient condition); the Magnus-expansion `π` criterion
(Magnus 1954; Blanes-Casas-Oteo-Ros, Phys. Rep. 470 (2009) 151); small-step
Floquet/effective-Hamiltonian quasilocality thresholds
(Abanin-De Roeck-Ho-Huveneers, Commun. Math. Phys. 354 (2017) 809). These
motivate the `O(1)`-threshold shape of route 1; the quantitative content used
above (the `1.8012` radius, the divergence exhibits, the gap factors) is
derived in the runner, so no comparator number is load-bearing.

## What this rules out

- Closing the (M2) exact-H step, or the bridge note's C4 BCH frontier, by a
  norm-convergent BCH/Magnus/small-step expansion **on the canonical
  surface**: the hypotheses fail by 1.28x-112.5x and the series demonstrably
  diverges at those scales.
- Rescuing the expansion route via temporal anisotropy without leaving the
  canonical surface: the required `ξ >= 43-113` is the continuous-time horn,
  excluded as non-canonical by the kinetic-isotropy surface selection.

## What this does not claim

- It does **not** claim `H = -log(T)/a_τ` fails to be quasilocal — O3
  exhibits the opposite separation (object healthy where the method dies),
  and the free-surface spectral instance is already on the books.
- It does **not** supply the gauged/interacting spectral step. That is the
  named open gate after this triage: extend transfer-symbol positivity +
  dispersion analyticity to the gauged surface.
- It does **not** modify the parent note's (M2) status, the bridge note's
  scope, or any audit verdict.
- The literature thresholds are not used as derivation inputs; sufficient
  conditions failing is backed by exhibited divergence, not by citation.

## Not in scope

- Non-perturbative gauge-sector spectral analysis (electric/magnetic layer
  structure); only its norm budget enters, via the landed bridge note.
- Continuum (`a -> 0`) statements, OS reconstruction, or Lorentz claims.
- Any change to the `v_LR` numerics of the bridge note.

## Citations

- `AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md` —
  parent (M2) gap this note scopes.
- `MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md` —
  landed budget `J_max = |m| + 78`; C4 frontier.
- `RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md` —
  free-surface instance of the surviving spectral route.
- `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` — canonical `ξ = 1`
  kinetic-form surface (approved primitive).
- `EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md` —
  the surface-selection thread that independently disfavors the
  continuous-time horn.
- Magnus 1954; Blanes-Casas-Oteo-Ros 2009; Abanin-De Roeck-Ho-Huveneers
  2017 — comparator thresholds for route 1 (context only).
