# Gauged Fixed-Background Quasilocality of the Reconstructed Log-Transfer Hamiltonian, via Combes-Thomas

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-13
**Claim type:** bounded_theorem (fixed-background, single-particle sector;
Combes-Thomas route)
**Type:** bounded_theorem
**Status:** unaudited candidate. Graph-visible only so the independent audit lane
can decide. Inherits the conditional provenance of the reconstruction authorities
it cites (see Honest status); it does not set or predict an audit outcome.
**Primary runner:**
[`scripts/gauged_log_transfer_quasilocality_combes_thomas_2026_06_13.py`](../scripts/gauged_log_transfer_quasilocality_combes_thomas_2026_06_13.py)
**Cached runner output:**
[`logs/runner-cache/gauged_log_transfer_quasilocality_combes_thomas_2026_06_13.txt`](../logs/runner-cache/gauged_log_transfer_quasilocality_combes_thomas_2026_06_13.txt)

---

## Role

The free (`U = 1`) sector of the microcausality exact-`H` step is closed by
[`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md):
the reconstructed single-particle Hamiltonian `h = -log(T_hat^2)/(2 a_tau)` has a
**sharp** exponential kernel rate `arcsinh(m)`, proved by a Fourier / Paley-Wiener
torus contour shift. That note declares its open frontier verbatim:

> *"the **gauged / interacting** log-transfer locality: fixed-background
> `T_hat^2[U]` is not translation-invariant, the Fourier route does not apply
> verbatim, and the `U`-integrated interacting case is open."*

This note closes the **fixed-background** half of that frontier with the
translation-invariance-free tool: **Combes-Thomas resolvent decay** plus
**holomorphic functional calculus**, on a spectral gap that is **uniform over all
gauge backgrounds**. It does not touch the `U`-integrated dynamical case, which
remains open.

The expansion-route triage
[`MICROCAUSALITY_EXACT_H_EXPANSION_ROUTE_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-09.md`](MICROCAUSALITY_EXACT_H_EXPANSION_ROUTE_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-09.md)
foreclosed the norm-convergent expansion route on the canonical surface and named
spectral/analyticity as the live route; the free note instantiated it via Fourier.
This note shows the spectral route survives the loss of translation invariance.

## The object

On a fixed background `U = {U_mu(x)}` of unitary link variables in any compact
gauge group `G` (here `U(1)` and `SU(2)`), define the covariant shift, covariant
sine, and total hop

```text
    (S_mu psi)(x) = U_mu(x) psi(x + e_mu),   S_mu a contraction (unitary on a block),
    s_mu[U] = (S_mu - S_mu^dag) / (2i),       s_mu = s_mu^dag,
    D[U]   = m^2 I + ( sum_{mu=1}^d s_mu[U] )^2 .                            (1)
```

The reconstructed single-particle Hamiltonian on the fixed background is the
matrix function

```text
    h[U] = arcsinh( sqrt( D[U] ) ),                                          (2)
```

whose eigenvalues are exactly the landed per-config dispersion
`E_j[U] = arcsinh(sqrt(m^2 + lambda_j(U)^2))`, `lambda_j` the eigenvalues of
`sum_mu s_mu`, of
[`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md)
and
[`INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md`](INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md).
Eq. (1) is the **square-of-sum** radicand `m^2 I + (sum_mu s_mu)^2`, which is the
landed gauged form; at `d = 1` it is the exact action-derived free dispersion.

**Carrier note.** The free note's *declared* `d >= 2` carrier is instead the
**sum-of-squares** `D_ss[U] = m^2 I + sum_mu s_mu[U]^2`; it differs from (1) by
flux cross-terms `sum_{mu != nu} s_mu s_nu` and coincides with (1) at `d = 1`.
Both carriers satisfy the Combes-Thomas hypotheses, so the conclusion of this note
is **carrier-robust** (Theorem G9). We take the action-faithful square-of-sum as
primary because it is the operator the landed reconstruction actually produces.

## Statement

Throughout, `m > 0`, `||.||_inf` is the sup metric, and "uniform in `U`" means the
constant is the same for every fixed background of unitary links (every flux /
holonomy) and every volume.

**(G1) Uniform spectral containment.** Each `S_mu` is a contraction
(`||S_mu|| <= 1`), so `s_mu = s_mu^dag` with `||s_mu|| <= 1`, hence
`||sum_mu s_mu|| <= d` and `(sum_mu s_mu)^2 >= 0`. Therefore

```text
    m^2 I  <=  D[U]  <=  (m^2 + d^2) I ,    i.e.  spec(D[U]) subset [m^2, m^2 + d^2],   (3)
```

uniformly in `U` and volume, with `dist(spec(D[U]), (-inf, 0]) = m^2 > 0`. No
Fourier / translation invariance is used. (For the sum-of-squares carrier the
ceiling tightens to `m^2 + d`.)

**(G2) Finite range, gauge-independent envelope.** Because `S_mu S_mu^dag = I`, the
range-1 piece of `s_mu^2` cancels, so `D[U]` is **exactly range 2** in `||.||_inf`
inside a support envelope that does not depend on `U`. The axial range-2 entries
have gauge-independent magnitude (`|D[x, x+-2 e_mu]| = 1/4`); flux can change or
cancel individual cross-term coefficients inside the envelope.

**(G3) Holomorphic functional calculus, uniform.**
`f(w) = arcsinh(sqrt(w)) = log(sqrt(w) + sqrt(w + 1))` is holomorphic and
single-valued on `C \ (-inf, 0]` (all branch points of `sqrt` and of `arcsinh`
at `w = -1` lie on the cut). Since `spec(D[U])` sits at distance `m^2 > 0` from the
cut for every `U`, the Riesz-Dunford integral

```text
    h[U] = (2 pi i)^{-1} oint_Gamma f(w) (w - D[U])^{-1} dw                  (4)
```

defines `h[U]` on a contour `Gamma` that hugs `[m^2, m^2 + d^2]` at distance
`m^2/2`, staying strictly in `Re w > 0` with finite `sup_Gamma |f|` and finite
length. The gap `m^2 > 0` is load-bearing: a circle of radius `>= m^2 + d^2/2`
would cross the cut and the calculus fails.

**(G4) Combes-Thomas resolvent bound (reproved).** Let `A = A^*` be finite range
`R` in `||.||_inf` with `||A|| <= K`, and `dist(z, spec A) = eta > 0`. Fix a unit
coordinate direction `u` and the diagonal twist `M_lambda = diag e^{lambda <u, x>}`.
By the band decomposition `A = sum_{||r||_inf <= R} A_r` with
`A_r = (2 pi)^{-d} int e^{-i<theta, r>} V_theta A V_theta^* d theta`
(`V_theta = diag e^{i<theta, x>}` unitary), each band obeys `||A_r|| <= ||A|| <= K`,
so

```text
    || M_lambda A M_lambda^{-1} - A ||  <=  K sum_{0 < ||r||_inf <= R} |e^{lambda <u, r>} - 1|
                                        <=  e K lambda * B(R, d)   (lambda R <= 1),     (5)
    B(R, d) = sum_{0 < ||r||_inf <= R} |<u, r>| = (2R+1)^{d-1} R(R+1) ,
```

using `|e^t - 1| <= e |t|` for `|t| <= 1`. The band-count `B(R, d)` is
**dimension-aware** (e.g. `B(2,1) = 6`, `B(2,2) = 30`; enumerated in the runner) —
it is *not* the dimension-blind `2R`. Choosing
`gamma = min(1/R, eta / (2 e K B(R, d)))` gives `||A_gamma - A|| <= eta/2`, so
by Neumann series `||(A_gamma - z)^{-1}|| <= 2/eta`, and undoing the similarity

```text
    | <x| (A - z)^{-1} |y> |  <=  (2/eta) e^{-gamma ||x - y||_inf} ,         (6)
```

with `2/eta` and `gamma` depending **only** on `(R, K, eta, d)`. (We use the rigorous
band-sum / Schur envelope (5), not the non-contraction `(e^{lambda R} - 1)||A||`
form.) The unbounded position ramp `M_lambda = diag e^{lambda <u, x>}` is the
open / infinite-lattice statement; on a finite periodic torus the wrap-around bond
violates (5) literally, but the kernel decay it controls is supplied by the *same*
uniform gap, which is what the runner measures directly on torus kernels (G4, G6,
G7) and on an open chain for the twist bound (G3).

**(G5) Gauged uniform quasilocality (main result).** Combining (G3) and (G4) with
`R = 2`, `K = m^2 + d^2`, and resolvent gap `eta = m^2/2` on `Gamma`,

```text
    || <x| h[U] |y> ||  <=  Const(m, d) e^{-gamma_CT ||x - y||_inf} ,        (7)
    gamma_CT = min(1/2, (m^2/2) / (2 e (m^2 + d^2) B(2, d))) > 0 ,   B(2, d) = 5^{d-1} * 6 ,
```

with `Const(m, d) = (|Gamma|/2 pi) (sup_Gamma|f|) (2/eta)` finite, and **both
`gamma_CT` and `Const` independent of the background `U` and of the volume**. So
`h[U]` is quasilocal on every fixed background with a single background-independent
rate. `h[U]` is **not** finite-range (the free note proved the same at `U = 1`);
`D[U]` is finite-range, `h[U]` is quasilocal — distinct objects.

**(G6) Gauge covariance of the kernel.** Under
`U_mu(x) -> g(x) U_mu(x) g(x + e_mu)^dag`, `S_mu -> G S_mu G^dag` with `G = diag(g)`
unitary, so `D[U^g] = G D[U] G^dag` and (spectral calculus) `h[U^g] = G h[U] G^dag`
exactly. Hence the kernel block `<x| h[U] |y>` transforms by left/right unitaries
and its **unitarily-invariant block norm `|| <x| h[U] |y> ||` is exactly
gauge-invariant**; for abelian `G` this is the scalar `| <x| h[U] |y> |`. The decay
rate is therefore a gauge-invariant datum.

**(G7) `U = 1` / `d = 1` reduction.** At `U = 1` (or any `d = 1` background) the
symbol of `D` is `m^2 + sin^2 p` and `h` recovers the landed free dispersion
`arcsinh(sqrt(m^2 + sin^2 p))` exactly, with measured kernel rate `arcsinh(m)`. The
runner's `d = 1` rate is extracted by a **joint two-parameter fit** of both the
exponential rate and the prefactor exponent; it recovers the rate to `0.18%` of
`arcsinh(m)` **and** the prefactor exponent `1.56 ~ 3/2` — the square-root
branch-point asymptotic `|h(n)| ~ n^{-3/2} e^{-arcsinh(m) n}` already established by
the free note's T5, here *recovered from the data*, not imported as a tuned input.
The Combes-Thomas lower rate satisfies `gamma_CT <= arcsinh(m)` for all `m > 0`,
consistent with — and never claiming to reproduce — the **sharp** free rate.
`gamma_CT` is a **lower bound** on the true gauged rate and is generically not
sharp; the true gauged rate is background-dependent and can **exceed** `arcsinh(m)`
(measured `~0.9-1.1` on random 2D flux).

**(G9) Carrier robustness.** The sum-of-squares carrier
`D_ss = m^2 I + sum_mu s_mu^2` (the free note's declared `d >= 2` carrier) is also
range 2 with `spec(D_ss) subset [m^2, m^2 + d]` and gap `m^2`, so (G4)-(G5) give
the same quasilocality conclusion. Thus the gauged-quasilocality result does not
depend on the `d >= 2` carrier choice; only the constants (`d^2` vs `d` ceiling)
and the parity structure differ.

## Parity Boundary

In `d = 1` (both carriers) and for the sum-of-squares carrier in any `d`, `D` and
hence `h` hop on the **even sublattice** (`h(z) = 0` unless every component of `z`
is even), preserved on every background — flux changes coefficients, not the parity
support. The **action-faithful square-of-sum** carrier does **not** have strict
even-sublattice parity as a universal carrier identity in `d >= 2`: the cross-terms
`s_mu s_nu` (`mu != nu`) open nearest diagonal channels at offsets
`(+-1, +-1, ...)` (measured magnitude `~5e-1` on the tested background, far above
any floor). This is stated, not hidden; it does not affect (G5), which only uses
range and gap.

## Proof sketch

(G1) operator monotonicity from `0 <= s_mu^2 <= I` and `(sum s_mu)^2 >= 0`, summed
over `d` directions; (G2) the cancellation `s_mu^2 = -(S_mu^2 - 2I + S_mu^{dag 2})/4`
removes the range-1 part, leaving offsets `{0, +-2 e_mu}` (plus `{+-e_mu +- e_nu}`
cross-terms for the square-of-sum, still `||.||_inf`-range 2); (G3) principal-branch
composition and the contour-distance bound; (G4) the band-decomposition Combes-Thomas
estimate with the dimension-aware band constant `B(R, d) = (2R+1)^{d-1} R(R+1)`
(eq. (5)); (G5) assembling (4) with (6) and bounding `|f|`, `|Gamma|`, `2/eta`;
(G6) direct conjugation through the spectral calculus; (G7) the `d = 1` symbol
identity and `gamma_CT <= arcsinh(m)`.

**What the runner does (and does not) reprove.** The runner reproves a *numerical*
Schur row-sum twist bound on an explicit open chain (G3, `alpha* ~ 0.022`) and
verifies the closed-form band constant `B(R, d)` by enumeration; it confirms that
the closed-form `gamma_CT` of (7) is a valid *conservative lower bound* on the
independently measured resolvent and kernel decay rates (it is not sharp). It also
verifies the Riesz-Dunford contour integral reproduces `h[U]` (G2), the uniform gap
floor `m^2` and ceiling `m^2 + d^2` (G1), the `arcsinh(m)` reduction (G7), and the
exact gauge-invariance (G5) to machine precision. It does **not** symbolically
reprove the closed-form CT envelope (5)-(7); that is the in-note analytic step, and
(5) is corrected here to the dimension-aware form.

## Hypothesis set used

- **Compact gauge group / unitary links** — `S_mu` a contraction
  (`||S_mu|| <= 1`); load-bearing for (G1) `||s_mu|| <= 1` and the uniform gap.
  Reproved in-runner from `S_mu S_mu^dag = I` (eigenvalues on the unit circle =>
  `Im in [-1, 1]`); not asserted.
- **Mass gap `m > 0`** — load-bearing for the gap `m^2` to the holomorphy cut;
  at `m = 0` the kernel is a power law (F1).
- **The reconstruction object** — that `h[U] = arcsinh(sqrt(D[U]))` with the
  square-of-sum radicand (1) is the per-config reconstructed single-particle
  Hamiltonian: cited from `RP_P2_GAUGE_EXTENSION...2026-05-28` and
  `INTERACTING_TRANSFER_MATTER_GAP...2026-05-30` (both `audited_conditional`),
  whose `E_j[U] = arcsinh(sqrt(m^2 + lambda_j^2))` this note covariantizes
  operatorially. The `d >= 2` carrier choice is declared (square-of-sum primary,
  sum-of-squares robustness), exactly as the free note declares its `d >= 2`
  carrier.
- **Per-site commuting-mode / block-kernel convention** — from
  `HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02` (same convention as the
  free note); blocked-time normalization from
  `AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29` (unaudited; inherited
  conditionality).
- **Proof-technique provenance (cited as method, reproved in-note, NOT a
  derivation input):** Combes-Thomas resolvent decay (Combes-Thomas 1973) and
  Riesz-Dunford holomorphic functional calculus. The repo's own
  `OBSERVABLE_PRINCIPLE_P1_BRIDGE_LOCALITY_OF_SOURCE_DERIVATIVES_NARROW_NOTE_2026-05-21`
  already records that "Combes-Thomas does not derive locality as a primitive; it
  characterizes the resolvent decay rate" — the same discipline applies here.
- **No fitted parameters, no observed values, no empirical comparators.** Inputs
  are `m`, `d`, and the fixed background `U`.

## No-Go Discipline Gate (parity boundary only)

**Status: PASS for the scoped parity boundary only.** The negative is not that
gauged log-transfer locality fails — it is proved (G5). It is only that strict
component-even sublattice parity is not a universal identity of the
action-faithful square-of-sum carrier in `d >= 2`.

- **N1 alternative routes.** Five distinct rescue routes were checked or scoped
  away. (1) `d = 1` preserves strict even parity, but that is outside the `d >= 2`
  square-of-sum boundary. (2) The sum-of-squares carrier preserves strict even
  parity, but it is a different carrier; G9 keeps locality carrier-robust while
  not transferring parity. (3) Gauge transformation cannot remove a nonzero odd
  block norm because G6 gives unitary covariance of the kernel blocks. (4) Flux
  cancellation can erase individual cross-term coefficients, so the claim is not
  phrased as "every background breaks parity"; it is only that strict parity is not
  a universal carrier identity. (5) Replacing strict component-even parity with a
  different parity notion, such as checkerboard parity, changes the predicate and
  is not the free/sum-of-squares parity statement compared here.
- **N2 wall independence.** One scoped boundary: strict component-even parity for
  the square-of-sum carrier in `d >= 2`. The `U`-integrated, many-body, and
  sharp-rate problems are separate open tasks, not walls claimed here.
- **N3 hidden-wall scan.** The `d >= 2` carrier is declared (both forms), not
  imported as a retained theorem; the CT and contour steps are reproved in-note.
  "Background" means a supplied fixed unitary-link configuration, not a hidden
  gauge-measure or dynamical gauge-field claim.
- **N4 residual matching.** No prior no-go witness is used for the parity boundary.
  The free note's named residual is fixed-background gauged quasilocality, which
  this note addresses by (G5), not by the parity boundary.
- **N5 rhetoric audit.** The only negative predicate is strict component-even
  sublattice parity of the square-of-sum carrier. The note does not claim failure
  of all parity notions, finite-range locality, quasilocality, gauge covariance, or
  sum-of-squares parity.
- **N6 partial-closure path.** Parity can be restored by choosing the
  sum-of-squares carrier or by changing the parity predicate, but those are
  carrier/predicate changes, not derivations of strict parity for the
  action-faithful square-of-sum carrier. No new axiom, primitive, or Tier-A
  admission is requested.
- **N7 steelman.** A hostile reviewer can object that a different parity notion or
  the sum-of-squares carrier remains useful. This is correct and is why the note
  isolates parity as a carrier-dependent boundary while keeping the quasilocality
  theorem carrier-robust.
- **N8 cross-cycle echo.** Similar prior overclaims confused finite range, exact
  parity, and quasilocal tails. This note separates them: `D[U]` is finite-range,
  `h[U]` is quasilocal, and strict component-even parity is carrier-dependent.

## What this rules out / does not claim

**Shows (not open at the fixed-background single-particle level).** Fixed-background
gauged log-transfer locality is not rate-unknown: `h[U]` is quasilocal with a
background-independent exponential rate `gamma_CT > 0`, and the kernel block norm is
exactly gauge-invariant. The "BCH commutators destroy locality" worry is answered on
every fixed background, not just `U = 1`. (This note carries Status = unaudited
candidate; "shows" is a source-side claim, not an audit-ratified closure.)

**Does not claim.** (i) The `U`-integrated / dynamical gauge-measure case — the
fixed-`U` resolvent bound does not control gauge-field correlations; **open**.
(ii) A **sharp** gauged rate — `gamma_CT` is a lower bound only. (iii) The full
**many-body fermionic** transfer-matrix locality or a **Lieb-Robinson lightcone** —
that needs the separate quasilocal-LR composition step (the free note's item 3),
still a separate theorem. (iv) Continuum limit, OS reconstruction, or any audit
status. (v) Retained-grade status: the reconstruction authorities cited are
`audited_conditional` / unaudited, so this note inherits conditional status.

## Runner and cache

```bash
python3 scripts/gauged_log_transfer_quasilocality_combes_thomas_2026_06_13.py
```

Deterministic (seeded `U(1)` and `SU(2)` backgrounds), runtime a few minutes.
Checks: object sanity (G0), uniform gap (G1), contour (G2), Combes-Thomas
reproved + measured (G3), kernel quasilocality 1D/2D (G4), abelian and non-abelian
gauge-invariance (G5), uniform rate over a `U(1)+SU(2)` ensemble (G6), `d = 1`
reduction to `arcsinh(m)` (G7), parity (G8), carrier robustness (G9), and
falsification legs `m = 0` (gap) and long-range (finite range). Runner cache:
[`logs/runner-cache/gauged_log_transfer_quasilocality_combes_thomas_2026_06_13.txt`](../logs/runner-cache/gauged_log_transfer_quasilocality_combes_thomas_2026_06_13.txt)
(PASS=36, FAIL=0).

## Citations

- [`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md)
  — the free (`U = 1`) anchor this note extends, and its named open frontier
  (context/target, not an upstream premise).
- [`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md)
  (`audited_conditional`) — per-config dispersion
  `E_j[U] = arcsinh(sqrt(m^2 + lambda_j^2))`; the object (1)-(2) covariantizes this.
- [`INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md`](INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md)
  (`audited_conditional`) — the uniform matter-gap floor `arcsinh(m)`; the floor
  this note's gap `m^2` is consistent with.
- [`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`](HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md)
  — per-site mode / block-kernel convention.
- [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
  — blocked-time normalization (unaudited; inherited conditionality).
- [`MICROCAUSALITY_EXACT_H_EXPANSION_ROUTE_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-09.md`](MICROCAUSALITY_EXACT_H_EXPANSION_ROUTE_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-09.md)
  — route triage naming spectral/analyticity live (context only).
- Proof-technique provenance (no constant imported): Combes-Thomas (1973);
  Riesz-Dunford holomorphic functional calculus. Reproved in-note (G4/G3).

## Changelog

- **2026-06-13** — initial note. Closes the fixed-background half of the free
  note's named gauged open frontier: on any fixed compact-group background `U`,
  the reconstructed single-particle `h[U] = arcsinh(sqrt(m^2 I + (sum_mu s_mu)^2))`
  is quasilocal with a background- and volume-independent exponential rate
  `gamma_CT > 0` (Combes-Thomas on the uniform gap `m^2`, finite range 2), the
  kernel block norm exactly gauge-invariant, reducing to the landed sharp free rate
  `arcsinh(m)` at `d = 1`. Carrier-robust across the square-of-sum (action-faithful)
  and sum-of-squares (declared) radicands. Open: `U`-integrated/dynamical case,
  sharp gauged rate, many-body Lieb-Robinson lightcone, continuum. Runner
  `PASS=36 FAIL=0`.
