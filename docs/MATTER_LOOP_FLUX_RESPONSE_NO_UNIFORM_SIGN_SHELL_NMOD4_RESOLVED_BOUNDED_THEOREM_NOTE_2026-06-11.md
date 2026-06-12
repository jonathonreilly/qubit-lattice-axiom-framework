# Matter-Loop Flux Response on Tested Free Rings Has No Uniform Sign: Shell- and N-mod-4-Resolved Curvatures, Open-Shell Cusps, and No Use of the Imported beta Formula

**Date:** 2026-06-11
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** Exact finite free-ring matter-loop response on the tested
instances only: Abelian `U(1)` flux, supplied fillings `K = N/2` and
`K = N/2 - 1`, `N in {8,10,12,14,16}`, masses listed in the runner, and
ground-state response. The result is no uniform curvature sign on that tested
finite shell packet; it is not a continuum, thermodynamic, non-Abelian,
interacting, beta-function, or gauge-self-energy claim.
**Script:** [`scripts/frontier_matter_loop_flux_response_no_uniform_sign_2026_06_11.py`](../scripts/frontier_matter_loop_flux_response_no_uniform_sign_2026_06_11.py)
**Cache:** [`logs/runner-cache/frontier_matter_loop_flux_response_no_uniform_sign_2026_06_11.txt`](../logs/runner-cache/frontier_matter_loop_flux_response_no_uniform_sign_2026_06_11.txt)
**Status:** source proposal; the audit lane grades. Runner `PASS=13 FAIL=0` — exact
dense diagonalization, deterministic, memory trivial. A 4-lens panel returned
unanimous `land_with_edits`; all edits applied — including the panel's own kill-test
result (the `N = 4n+2` class), which is now **in-runner** and sharpens the theorem.

## The question, and what the data did to it — twice

The landed `b₃` note (`retained_bounded`) imports the Peskin–Schroeder β-coefficient
formula as `(X3)`; its narrow attackable face is the **sign structure**. The working
hypothesis — a uniform matter screening sign (`V″(0) > 0` everywhere) — was **refuted
by the first exact data** (even-K rings came out negative). The panel's kill test
then refuted the *replacement* hypothesis too: the clean even/odd parity rule does
**not** extend across `N mod 4`. What survives both refutations is the theorem:

## The findings (runner `PASS=13`; `(X3)` used nowhere; fillings are supplied data)

**(F1) No uniform sign — shell- and `N`-mod-4-resolved.** For the ground-state flux
response `V(φ) = E₀(φ)` at staggered mass `m ∈ {0.4, 1.0}`:

- **`N = 4n` closed shells** (`N ∈ {8,12,16}`): the curvature sign **alternates with
  particle parity** — even `K` paramagnetic (`V″(0) < 0`, all 6), odd `K` diamagnetic
  (`V″(0) > 0`, all 6).
- **`N = 4n+2` closed shells flip**: half-filled *even* `K` gives `V″(0) > 0`
  (`N = 10: +3.1×10⁻²`, `N = 14: +1.3×10⁻²`) — the bare even/odd rule fails across
  `N mod 4`.
- **Open shells are not curvatures at all**: at `N = 4n+2`, `K = N/2 − 1` the
  response has a level-crossing cusp at `φ = 0` (slope jumps `0.32`, `0.21`).

**(F2) The massless half-filled point is a cusp** (Fermi gap `2×10⁻¹⁶`, slope jump
`0.33`), closing at `m = 0.4` to the smooth finite-difference scale — 4 orders of
contrast. Curvature language is never applied to cusp instances.

**(F3) Exact controls.** Twisted spectra match the analytic forms at `m = 0` and the
two-band staggered form `±√(m² + 4t²cos²((2πℓ+φ)/N))` at `m > 0` (`9×10⁻¹⁶`); the
filled band responds **exactly zero** (trace argument); zero-total-flux gauge
transformations are exact invariances; both tested branches decouple monotonically
with mass; Richardson cross-checks carry the disclosed double-precision
second-difference floor (`ε·E₀/h² ≈ 4×10⁻⁶`).

## What this buys, honestly

A **non-imported, exact** statement adjacent to the ST3 surface, offered as
**motivational finite-size matter-response evidence** (not running-coupling
derivation): at accessible sizes the matter loop has *no uniform screening sign* —
the sign is a shell-structure and `N`-mod-4 datum. The continuum screening question
that `(X3)` answers must therefore be posed on **parity-averaged or
thermodynamic-limit objects** — the named follow-on. The gauge self-energy side
(antiscreening) remains a **named gap**: it requires the not-yet-derived autonomous
gauge action, consistent with the landed slaving results.

## Scope

Abelian `U(1)` flux on free rings; ground-state response only; `K = N/2` and
`N/2 − 1` are **chosen supplied fillings**, not filling-independent operator facts;
decoupling and cusp-closure statements are scoped to the tested instances. **Not
claimed**: the `b₃` coefficient or any β-function number; non-abelian antiscreening;
the gauge self-energy; the parity-averaged or thermodynamic-limit sign; interacting
matter; `d = 3`; continuum limits. Standard math (method only): twisted
tight-binding spectra; persistent-current parity effects (method context already
present in the repo's flux-threaded rows); Richardson extrapolation; trace
arguments.

No new axiom, primitive, measure, or weight; `r` untouched; discrete throughout.
The audit lane grades.

## No-Go Discipline Gate

This gate applies only to the finite tested-shell negative above. It does not
claim that continuum screening, parity-averaged response, thermodynamic-limit
response, non-Abelian matter, interacting matter, or gauge self-energy has no
uniform sign.

**N1 alternative routes checked.**

| route | outcome on this bounded claim | marker |
|---|---|---|
| Uniform positive matter screening sign on tested rings | Refuted by `N = 4n` even-`K` closed shells with `V''(0) < 0`. | ATTEMPTED |
| Uniform negative sign on tested rings | Refuted by `N = 4n` odd-`K` closed shells and `N = 4n+2` half-filled closed shells with `V''(0) > 0`. | ATTEMPTED |
| Simple even/odd particle-parity rule | Refuted by the `N = 4n+2` half-filled even-`K` closed-shell flip. | ATTEMPTED |
| Treat open shells as curvature data | Rejected: the runner detects level-crossing cusps and excludes them from curvature tables. | ATTEMPTED |
| Import the Peskin-Schroeder beta coefficient formula | Not used; the runner contains only finite free-ring spectra and response checks. | ATTEMPTED |

**N2 wall independence.** The collapsed residual set is: supplied fillings,
finite ring sizes, free matter, Abelian flux, no parity averaging,
no thermodynamic limit, no interacting matter, and no autonomous gauge action.
Closing one residual does not automatically close the others.

**N3 hidden-wall scan.** "Standard math" is method context only. The
load-bearing objects are explicit twisted tight-binding Hamiltonians, finite
eigenvalue sums, finite differences on smooth instances, cusp tests on
open-shell instances, analytic spectrum checks, trace flatness for filled
bands, and zero-total-flux gauge invariance checks.

**N4 residual matching.** The negative attacks only the finite free-ring
uniform-sign residual. It does not use the retained `b3` note as a witness
against continuum screening; that note is mentioned only to mark the imported
formula that is not used here.

**N5 rhetoric audit.** "No uniform sign" means no uniform curvature sign across
the tested finite closed-shell packet. It is not a statement about all fillings,
all `N`, parity-averaged response, thermodynamic response, non-Abelian
response, or gauge self-energy.

**N6 partial-closure path scan.** A parity-averaged observable,
thermodynamic-limit construction, interacting matter model, or autonomous
gauge-action theorem could give a different sign statement. Those are named
follow-ons, not blocked routes.

**N7 steelman.** A hostile reviewer can argue that the continuum screening
question should be asked only after parity averaging and a thermodynamic limit,
and that finite-shell parity effects may disappear or reorganize there. This
is valid against any broader claim, so this note stays finite-shell scoped.

**N8 cross-cycle echo.** Prior imported beta-function/sign surfaces in the
repo are import-bearing or bounded. This note supplies a non-imported finite
matter datum adjacent to that surface, not a replacement beta-function theorem.
