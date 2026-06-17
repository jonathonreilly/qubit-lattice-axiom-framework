# The Taste-SUMMED Marginal Lorentz-Violation Is B4-Protected on the OS0 Surface; the Per-Single-Taste Marginal Velocity Is Not (Bounded)

**Date:** 2026-06-13
**Claim type:** bounded_theorem (the B4-orbit / taste-multiplet-*summed* marginal
velocity is Lorentz-isotropic on OS0; the per-single-taste marginal velocity is
*not* — it carries a real `O(0.2)` anisotropy that cancels only across the
B4-covariant taste orbit)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. The `bounded_theorem` label is a
source-side claim-boundary declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_taste_sector_marginal_lv_b4_2026_06_13.py`](../scripts/frontier_taste_sector_marginal_lv_b4_2026_06_13.py)
(`TOTAL: PASS=29 FAIL=0`)

> **Rebuild note (two corrections).** **(1) Scalar-denominator degeneracy.** An
> earlier *scalar-model* version used the scalar fermion denominator
> `sum_mu sin^2(k_mu)`, which is `pi`-periodic, so the taste `pi`-shift `B` left the
> entire self-energy unchanged (`Sigma(B=0) == Sigma(B=(0,1,1,0) pi)` to `~1e-17`)
> — the "taste-changing" test did not actually test taste change. The
> **genuine-Dirac-numerator** rebuild fixes this: the `pi`-shift flips the numerator
> signs and the taste change is genuinely **visible**. **(2) The `W_B`-conjugation
> tautology.** A subsequent "physical observable" version then defined
> `G_phys(p,B) = W_B [ Dinv(p) - Sigma(p,0) ] W_B^{-1}`. This **overclaimed**: it fed
> `Sigma(p,0)` for *every* taste `B` (never reading `Sigma(p,B)`), and conjugating by
> the unitary `W_B` makes `eigvals(W_B X W_B^{-1}) = eigvals(X)`, so the per-taste
> "protection" was a **tautology** — it returned the `B=0` spectrum for every `B` by
> construction. This note documents the **honest observable**
> `G_hon(p,B) = Dinv(p) - Sigma(p,B)` (external `Dinv` fixed, loop genuinely reads
> taste `B`), under which the per-single-taste marginal velocity is *not* protected
> (anisotropy `O(0.2)`) and the protection holds only at the B4-orbit / taste-sum
> level.

---

## Role

The retained B4 radiative-stability theorem
([`EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md))
forbids the marginal (dimension-4) velocity-anisotropy operator
`c_t p_t^2 + c_s (p_x^2 + p_y^2 + p_z^2)`, `c_t != c_s`, on the OS0 (`c_t = c_s`)
discrete-tick surface, and is **representation-blind**.

This note addresses a separate bounded-model question in the **staggered taste
sector**. In the runner's free Dirac/taste model the scalar denominator is
B4-symmetric and taste-blind under Brillouin-zone-corner shifts, while the
Dirac numerator changes sign by direction. Taste is **not** a
gauge-representation factor here; it is carried by the Brillouin-zone-corner
offset `A_mu in {0, pi}` per spacetime direction, which entangles the internal
taste label with the spacetime direction. The unasked question is whether
taste-breaking opens a side door the gauge-singlet B4 argument did not cover:

> Does the interaction-induced **taste-changing** self-energy regenerate a
> **marginal velocity anisotropy that differs between tastes** — a taste-dependent
> `c_t != c_s` — or is the taste-changing marginal velocity coefficient **also**
> B4-protected on OS0?

It consumes the approved `kinetic_isotropy_primitive` (the OS0 kinetic-form
surface, here the `xi = 1` hypercubic-symmetric regulator block) and the approved
`scale_reference_primitive` (`a^-1 = M_Pl`, used only for the dimension-6 size
estimate); it does **not** derive either primitive, does not add a dynamics, and
does not set an audit verdict.

---

## The genuine Dirac numerator (what makes the taste change visible)

The staggered/Wilson Euclidean propagator is

```text
    S(k) = ( m I - i sum_mu g_mu sin k_mu ) / ( m^2 + sum_mu sin^2 k_mu ),
```

with Hermitian Euclidean gammas `{g_mu, g_nu} = 2 delta_{mu nu}`. The taste change
is the BZ-corner offset: the internal line carries `S(k + pi B)`,
`B_mu in {0, 1}`. Because `sin((k + pi B)_mu) = (-1)^{B_mu} sin k_mu`, the
**denominator** `m^2 + sum_mu sin^2 k_mu` is **unchanged** (taste-blind spectrum),
while the **numerator** flips signs,

```text
    numerator of S(k + pi B) = m I - i sum_mu g_mu (-1)^{B_mu} sin k_mu.
```

This is the fix to the rejected degeneracy: the numerator sign-flip makes the
taste `pi`-shift genuinely **visible** in the self-energy. The runner checks
explicitly that `Sigma(B=0) != Sigma(B=(0,1,1,0))` now (`~1.5e-2`, versus the
rejected scalar runner's `~1e-17`).

The one-loop rainbow self-energy is

```text
    Sigma(p, B) = (1/N^4) sum_q [ sum_nu g_nu S(p - q + pi B) g_nu ] D(q),
    D(q) = 1 / gluon_block(q),  gluon_block(q) = sum_mu (2 sin(q_mu / 2))^2.
```

Using the Clifford contraction (**reproven** in the runner numerically and
symbolically)

```text
    sum_nu g_nu g_mu g_nu = (2 - d) g_mu = -2 g_mu   (d = 4),
```

the spin-summed numerator is `4 m I + 2 i sum_mu g_mu (-1)^{B_mu} sin(p-q)_mu`, so

```text
    Sigma(p, B) = A(p) I + i sum_mu g_mu Bc_mu(p, B),
    Bc_mu(p, B) = (1/N^4) sum_q 2 (-1)^{B_mu} sin(p-q)_mu D(q) / den.
```

The coefficient `Bc_mu` carries the explicit `(-1)^{B_mu}`.

---

## The load-bearing distinction: bare sign-flip is a removable taste rotation, but the physical observable reads the taste-B loop

The **bare** velocity coefficient `V_mu(p,B) = Tr[g_mu Sigma(p,B)] / (4 i) = Bc_mu`
picks up `(-1)^{B_mu}` and therefore **flips sign** under the taste shift. The
runner shows this explicitly: at a momentum exciting all four directions, the bare
coefficient flips sign exactly in the `B_mu = 1` directions and is unchanged in the
`B_mu = 0` directions (ratios `-1` and `+1` to machine precision).

This bare sign-flip is a **removable taste rotation**, *not* a physical anisotropy.
The taste `pi`-shift is a **unitary** similarity:

```text
    S(k + pi B) = W_B S(k) W_B^{-1},
    W_B = product over { mu : B_mu = 1 } of (g5 g_mu),
    W_B^{-1} g_mu W_B = (-1)^{B_mu} g_mu   (exact, all 16 B; reproven in the runner),
    W_B^dag W_B = I   (W_B unitary).
```

`W_B` is built from the `gamma_5 gamma_mu` staggered taste generators. The runner
verifies `S(k+pi B) = W_B S(k) W_B^{-1}` to machine precision, that the taste shift
**preserves the propagator eigenvalues**, and that
`Sigma(p, B) = W_B Sigma(p, 0) W_B^{-1}` to machine precision. These facts are
**true** and explain *why* the bare `g_mu` coefficient is not the physical
observable: its sign-flip is exactly the removable `W_B` rotation. They are
**not**, however, used to *define* the physical observable.

### The honest (physical) observable

The physical observable is the **eigenvalue dispersion of the renormalized inverse
propagator** in taste sector `B`, with the **external** inverse propagator left
fixed and the **loop** genuinely read at taste `B`:

```text
    G_hon(p, B) = Dinv(p) - Sigma(p, B),   Dinv(p) = m I + i sum_mu g_mu sin p_mu,
    lambda(p, B) = smallest eigenvalue of G_hon(p,B)^dag G_hon(p,B),
    physical velocity^2 in direction mu = d^2 lambda / d p_mu^2 |_{p=0}.
```

Crucially, `Dinv(p)` is **not** rotated by `W_B`, and the self-energy is `Sigma(p, B)`
(the taste-`B` loop), **not** `Sigma(p, 0)`. So `G_hon(p, B)` is a *genuine* function
of `B` and its eigenvalues *do* depend on `B`. This is the fix to the earlier
overclaim, which used `G_phys(p, B) = W_B [ Dinv(p) - Sigma(p, 0) ] W_B^{-1}`: that
operator (a) fed `Sigma(p, 0)` for every `B` and (b) is a unitary conjugation of the
`B = 0` operator, so `eigvals(W_B X W_B^{-1}) = eigvals(X)` returned the `B = 0`
spectrum for every `B` *by construction* — a tautology that tested nothing about
taste.

The per-taste marginal anisotropy is `delta(B) = (Z_t(B)) - (Z_s(B))` in each taste
sector; the taste-summed (B4-orbit) anisotropy is the orbit average of these.

---

## Result

On the OS0 (`xi = 1`) discrete-tick B4 measure, with the honest observable
`G_hon(p,B) = Dinv(p) - Sigma(p,B)`:

- **Non-degeneracy.** `Sigma(B=0) != Sigma(B=(0,1,1,0))` (`~1.5e-2`); the bare
  `g_mu` coefficient flips sign exactly in the `B_mu = 1` directions (the removable
  taste rotation).
- **Per-single-taste marginal velocity is NOT protected.** With the honest
  observable, each individual taste sector carries a genuine, *nonzero* `O(0.2)`
  marginal anisotropy on OS0. For the representative corner `B = (0,1,1,0)` the
  four direction curvatures are `[1.85, 2.16, 2.16, 1.85]`, i.e.
  `Sigma_t - Sigma_s = -0.206`; the worst per-taste anisotropy over the
  `hw = 1, 2, 3` corners is `~0.31`. **B4 does not protect the marginal velocity
  per single taste.**
- **Taste-summed (B4-orbit) marginal velocity IS protected.** Averaging over the
  `hw = 2` B4-taste orbit, the four curvatures are all `~2.0032` and the
  anisotropy cancels: `Sigma_t - Sigma_s (taste-sum) ~ -2.2e-14` on OS0; full
  four-direction spread `~3.0e-14`; structural across BZ resolutions (`N = 12:
  -1.3e-14`, `N = 16: -2.0e-14`). The explicit contrast is per-taste `O(0.2)`
  versus taste-sum `~1e-14`.
- **Falsification (the orbit zero is genuine B4-covariance, not an averaging
  artifact).** An anisotropic temporal block `xi != 1` regenerates a robustly
  nonzero *orbit-averaged* anisotropy: `xi=0.7: +9.4e-4`, `xi=0.8: +6.7e-4`,
  `xi=1.3: -1.35e-3`, `xi=1.5: -2.56e-3`; the continuous-time block gives
  `+1.8e-3`. The `xi < 1` and `xi > 1` results **straddle in sign**, so OS0
  (`xi = 1`) is an **isolated sign-crossing zero** of the orbit anisotropy
  (magnitudes `~1e-3`), not a degenerate flat region.
- **Survivor.** The physical taste-changing contribution lives in the dimension-6
  B4-invariant cubic harmonic `sum_mu p_mu^4` (axis quartic `-7.55` vs
  body-diagonal `-1.79` differ; the pure cubic harmonic has axis : diagonal
  `= 1 : 1/4` in 4D). With `a^-1 = M_Pl` the surviving taste-LV at `E = 1 GeV` is
  Planck-suppressed, `~ (1/3)(E/M_Pl)^2 ~ 2.2e-39` (the coefficient `c4 = 1/3` is
  an `O(1)` size estimate only, not a derived coefficient).

**Mechanism.** The taste `pi`-shift flips the loop `g_mu` coefficient by
`(-1)^{B_mu}`; with the external `Dinv(p)` *fixed*, this genuinely changes the
renormalized inverse propagator `G_hon(p,B)` in each taste sector, and its
smallest-eigenvalue curvature carries a real per-taste `O(0.2)` anisotropy. The
direction dependence is the gluon block plus loop measure, which on the OS0
(`xi = 1`) B4-covariant regulator are exact axis-relabel images across the four
directions. Summing over the B4 taste orbit, the per-taste anisotropies map into
one another under the axis relabel and cancel — so the *taste-summed* marginal
curvature is isotropic. Breaking the temporal block's B4-covariance (`xi != 1`, or
continuous-time) breaks the axis-relabel and the orbit anisotropy reappears,
straddling zero in sign across `xi = 1`; that is why the OS0 orbit zero is genuine
B4-covariance, not an orbit-averaging wash-out.

**Claim type: bounded_theorem (for this bounded model).** The B4-orbit /
taste-multiplet-*summed* marginal velocity is Lorentz-isotropic (B4-protected) on
OS0; the per-*single*-taste marginal velocity carries a real `O(0.2)` anisotropy
that cancels **only** across the B4-covariant taste orbit. The result is reported
from the computed numbers, not asserted.

---

## Honest scope

This is a **single taste-changing one-loop rainbow MODEL kernel** on a **finite
cut block**, in the **marginal sector on OS0 only**, **at the taste-SUM level**. It
does **not** close: the `n`-point functions, the full-staggered-ChPT taste basis
(the complete Lee-Sharpe taste-operator set), the `a -> 0` continuum limit, or the
continuous-time horn (which the falsification control deliberately shows breaks the
orbit isotropy). The **per-single-taste `O(0.2)` anisotropy is the genuine
residual**: whether it constitutes a physical Lorentz violation depends on the
physical interpretation of the taste label (if a single taste corner is a
physically distinguishable particle, the marginal anisotropy is physical; if only
taste-summed observables are physical, it cancels). This note does not settle that
interpretation; it reports the taste-sum protection and the per-taste residual
honestly. It **consumes (does not derive)** the `kinetic_isotropy_primitive` and
the `scale_reference_primitive`. It adds no axiom, primitive, or vocabulary, and
sets no audit status.

## Runner parts (every check an independent computed test)

- **A** — gammas; Clifford `{g,g}=2 delta`; the contraction
  `sum_nu g_nu g_mu g_nu = (2-d) g_mu = -2 g_mu` reproven numerically **and**
  symbolically (sympy, generic `d`); unitary taste rotation
  `W_B = prod (g5 g_mu)` with `W_B^{-1} g_mu W_B = (-1)^{B_mu} g_mu` for all 16
  `B`; propagator similarity `S(k+pi B) = W_B S(k) W_B^{-1}` and eigenvalue
  preservation. **These explain the removable bare `g_mu` sign-flip; they do not
  define the physical observable.**
- **B** — free `D^dag D` spectrum `= m^2 + sum sin^2` (4-fold, taste-blind), B4
  invariant under all 384 signed permutations.
- **C (core, honest observable `G_hon = Dinv - Sigma(p,B)`)** — non-degeneracy
  `Sigma(B=0) != Sigma(B!=0)`; bare `g_mu` sign-flip (removable);
  **(a)** per-single-taste marginal anisotropy genuinely nonzero `O(0.2)` on OS0
  (representative corner and worst-case over `hw = 1, 2, 3`) — B4 does not protect
  per-taste; **(b)** the B4-orbit / taste-SUM marginal anisotropy `~ 1e-14` on OS0,
  full four-direction, structural across `N = 12, 16`; the per-taste `O(0.2)` vs
  taste-sum `~1e-14` contrast.
- **D (falsification)** — `xi != 1` and continuous-time temporal blocks regenerate
  a nonzero *orbit-averaged* anisotropy (`~1e-3`); `xi < 1` / `xi > 1` straddle in
  sign (isolated zero at `xi = 1`).
- **E (survivor)** — the dim-6 cubic-harmonic survivor (axis vs body-diagonal),
  pure-geometry ratio cross-check, Planck-suppressed size (`c4 = 1/3` disclosed as
  a size estimate only).

## Literature (comparator only)

- J. Collins, A. Perez, D. Sudarsky, L. Urrutia, H. Vucetich, *Lorentz invariance
  and quantum gravity: an additional fine-tuning problem?*, Phys. Rev. Lett. **93**
  (2004) 191301 — the marginal-regeneration naturalness target.
- W. Lee, S. Sharpe, Phys. Rev. D **60** (1999) 114503; S. Sharpe,
  hep-lat/0607016 — the staggered taste-breaking operator structure.

These set the comparison context only; every identity used above (the Clifford
contraction, the `W_B` taste rotation, the propagator similarity, the B4 measure
relabel) is reproven in the runner from the lattice, Clifford, and B4 definitions.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — Lattice /
  Quantum / Record baseline (3D + 1; `Z^3` spatial primitive).
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the OS0 kinetic-form surface (`c_t = c_s`, `xi = 1`), consumed here.
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) —
  `a^-1 = M_Pl`, used only for the dimension-6 size estimate.
