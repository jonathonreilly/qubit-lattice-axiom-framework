# Transfer-Matrix Log Quasilocality on the Free Bilinear Sector

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** the single-particle hopping kernel of the exact
reconstructed Hamiltonian `H = -log(T_hat^2)/(2 a_tau)` of the
free staggered two-step transfer matrix obeys the
explicit exponential bound
`|h(z)| <= (1/a_tau) · C_d(eta, m) · e^{-eta·||z||_inf}` for every
`0 < eta < eta* := arcsinh(m)`, with
`C_d(eta, m) = sqrt(m^2 + (d-1) + cosh^2 eta)`; the optimal rate is
exactly `eta* = arcsinh(m)` (proved in `d = 1`, verified to <= 0.3% on
`Z^3` axes); consequently `H` is a quasilocal bilinear support family
with finite per-site overlap weight `W_H = ||h||_l1 < ∞` and
finite-range truncations `H_R` whose per-site tail weights and
single-particle operator-norm errors decay exponentially in `R` at the
same sharp rate. Negative finding on the same sector: the exact `H` is
**not** finite-range (nonzero hops at `l1`-range 4 are exhibited), so
the strict `R <= 2` support-family form of the microcausality bridge
note's (F5) hypothesis is **false** there and must be read in the
quasilocal form proved here. Sector restriction declared: free
(`U = 1`) bilinear staggered two-step sector only; the gauged /
interacting log-transfer locality remains open.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:**
[`scripts/transfer_matrix_log_quasilocality_check_2026_06_10.py`](../scripts/transfer_matrix_log_quasilocality_check_2026_06_10.py)

## Why this note exists

The microcausality bridge note
[`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
proves a
Lieb-Robinson lemma in-note and applies it unconditionally to the
finite-range hopping-bilinear Hamiltonian, but quarantines as its
explicit open hypothesis (F5) the claim that the exact reconstructed
Hamiltonian `H = -log(T)/a_tau` "admits a support-family decomposition
with `q <= 4`, `R <= 2`, and `W <= |m| + 300`", noting that BCH
commutators can enlarge range. The expansion-route triage note
(`MICROCAUSALITY_EXACT_H_EXPANSION_ROUTE_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-09.md`,
unaudited) closed the canonical one-step norm-convergent expansion
route on the canonical surface and named spectral/analyticity as the
live route; the free-surface dispersion note
(`RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`,
unaudited) instantiated that route qualitatively (analyticity ⟹ some
exponential tail, fitted rate within ~2x).

This note executes the spectral/analyticity route **quantitatively and
self-containedly** on the framework's actual bilinear transfer matrix:

1. it derives the decay **rate** exactly (`eta* = arcsinh(m)`, sharp:
   matching upper bound and branch-point lower-bound obstruction, not a
   fitted value);
2. it derives an **explicit, closed-form prefactor**
   `C_d(eta, m) = sqrt(m^2 + (d-1) + cosh^2 eta)`, so the bound is
   fully quantitative at every `(m, eta, d)`;
3. it translates the result into the bridge note's own support-family
   vocabulary `(q, R, W)` — finite total per-site overlap weight
   `W_H = ||h||_l1`, truncations `H_R` with exponentially small tail
   weights `W_tail(R)`, and single-particle truncation error
   `||h - h_R||_op <= W_tail(R)` — i.e. exactly the
   commutator-relevant quasilocality input the (F5) step needs;
4. it proves the honest **negative** counterpart: the exact `H` on this
   sector is *not* finite-range (its hopping coefficients at
   `l1`-distance 4 are nonzero, far above any numerical floor), so the
   strict `R <= 2` reading of (F5) is false on the bilinear sector and
   only the quasilocal reading can survive.

## Setup and conventions

### The object (one-hop authorities)

- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  — supplies the free staggered two-step blocked
  transfer matrix `T_hat^2` derived in-repo from the staggered action
  (`U = 1`, one Grassmann component per site, `1+1d`, `m > 0`), with
  single-particle kernel `t1^(2)(p) = e^{-2E(p)}`,
  `E(p) = arcsinh(sqrt(m^2 + sin^2 p))` the exact action-derived
  dispersion, and `H_hat = -log(T_hat^2)/(2 a_tau) = Σ_p E(p) a_p† a_p
  >= 0` on the free Fock space. This is the load-bearing object of this
  note.
- [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
  — the blocked-time normalization
  `H := -(1/(2 a_tau)) log(T)` for `T := T_hat^2` (the two-step block
  advances two lattice time steps) and self-adjointness/boundedness
  below of the reconstructed `H`. Only the normalization convention and
  well-definedness are consumed.
- [`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`](HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md)
  — the
  per-site commuting tensor-product mode convention and the two-site
  swap structure giving the exact pair-term operator norm
  `||c·(a_x† a_y + a_y† a_x)||_op = |c|` used in the support-family
  translation (Q3). This is the same convention the bridge note's (F4)
  and (F5) use.
- Parent RP context:
  [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
  — what `T` is and what RP licenses (staggered-only
  2-step blocked surface). Context for the object's provenance; no
  additional content consumed.

### Symbol, kernel, and the declared `d = 3` carrier (explicit boundary)

On the `d`-dimensional spatial torus the two-step single-particle
log-transfer symbol is

```text
    E_d(p) = arcsinh( sqrt( m^2 + Σ_{μ=1}^{d} sin^2 p_μ ) ),   m > 0,      (1)
```

and the exact reconstructed bilinear Hamiltonian is, in position space,

```text
    H = Σ_{x,y} h(x-y) a_x† a_y,
    h(z) = (1/a_tau) (2π)^{-d} ∫_{T^d} E_d(p) e^{i p·z} d^d p.             (2)
```

`E_d` is real and even in each `p_μ`, so `h` is real and even. On a
finite periodic block the DFT kernel is the periodization
`h_L(z) = Σ_k h(z + L k)`, which inherits every bound below.

**Carrier declaration (explicit boundary).** The in-repo
two-step authority derives (1) in-repo for `d = 1`; that case is the
proved anchor (and the runner re-verifies the action-derived
`T_odd·T_even` decaying eigenvalue equals `e^{-2E_1(p)}`, check T1).
The `d = 3` symbol in (1) is **declared in this note** as the
`Z^3`-spatial carrier of the same construction (the standard free
staggered dispersion with one `sin^2 p_μ` per spatial axis, matching
the framework's `Z^3` lattice baseline and the display already used by
the 2026-06-06 and 2026-06-09 microcausality notes). All proofs below
are written for general `d >= 1` from symbol (1) alone; nothing else
about `d = 3` is assumed.

Throughout `eta* := arcsinh(m) = log(m + sqrt(1 + m^2)) > 0` and
`||z||_inf := max_μ |z_μ|`, `||z||_1 := Σ_μ |z_μ|`. `a_tau` enters (2)
only as the overall `1/a_tau` scale; all rates are in lattice units and
`a_tau`-independent (check T14).

## Statement

**(Q1) Explicit exponential kernel bound (quasilocality).** For every
`0 < eta < eta*` and every `z ∈ Z^d`,

```text
    |h(z)|  <=  (1/a_tau) · C_d(eta, m) · e^{-eta·||z||_inf},
    C_d(eta, m)  :=  sqrt( m^2 + (d-1) + cosh^2 eta ).                     (3)
```

(Hence also `|h(z)| <= (C_d/a_tau) e^{-(eta/d)·||z||_1}`.)

**(Q2) Sharpness: the optimal rate is exactly `eta* = arcsinh(m)`.**
In `d = 1`: if `|h(n)| <= C e^{-eta'·|n|}` held for some `eta' > eta*`,
the Fourier series of `E_1` would converge in a strip wider than
`eta*`, analytically extending `E_1` past the point
`p* = i·arcsinh(m)`; but `E_1'(p)` diverges as `p -> p*` along the
imaginary axis (closed form, eq. (8)), so `p*` is a genuine branch
point and no such `eta'` exists. Combined with (Q1) the decay rate is
exactly `eta*`. In `d = 3` the upper bound (Q1) is proved and the same
branch point sits at the transverse minimum `p_⊥ = 0`; the axis rate is
verified numerically to `<= 0.3%` (checks T8), while the `d = 3`
lower-bound argument is not separately formalized (declared boundary).

**(Q3) Support-family (commutator-relevant) form.** In the per-site
commuting-mode convention of the hopping-bilinear authority:

- (a) `H = Σ_x h(0) n̂_x + Σ_{unordered pairs {x,y}} h(x-y)(a_x† a_y +
  a_y† a_x)` is a support family with `q = 2` and exact term norms
  `|h(x-y)|`; its per-site overlap weight is
  `W_H = |h(0)| + Σ_{z≠0} |h(z)| = ||h||_l1 < ∞`
  (value at `m = 0.3`, `d = 3`, `a_tau = 1`: `W_H = 1.757278…`).
- (b) For each `R`, the truncation `H_R` (keep `||z||_inf <= R`) is a
  bona fide finite-range support family (`q = 2`,
  `diam_l1 <= d·R`, `W <= ||h||_l1`), and the remainder `H - H_R` is a
  support family with per-site overlap weight

  ```text
      W_tail(R) = Σ_{||z||_inf > R} |h(z)|
                <= (C_d(eta,m)/a_tau) Σ_{r > R} [(2r+1)^d - (2r-1)^d] e^{-eta r}
                =  O( (1+R)^{d-1} e^{-eta R} ),                            (4)
  ```

  for every `eta < eta*`; the measured tail-weight slope equals `eta*`
  (check T12). On any finite block `Λ`,
  `||H - H_R||_op <= |Λ| · W_tail(R)`, and at the single-particle level
  `||h - h_R||_op <= W_tail(R)` exactly (circulant symbol bound; check
  T13). This is the standard quantitative input for quasilocal
  Lieb-Robinson bounds.
- (c) **Negative finding (strict (F5) form fails on this sector).** The
  symbol (1) is `π`-periodic in each `p_μ`, so `h(z) = 0` unless every
  `z_μ` is even (the blocked `H` hops on the even sublattice; check
  T9) — and the surviving even-offset coefficients are *not* compactly
  supported: `|h(4,0,0)| = 5.56e-3`, `|h(2,2,0)| = 1.04e-2` at
  `m = 0.3` (`a_tau = 1`), nine orders of magnitude above the numeric
  floor (check T10). By the matrix-element lemma (Step 4), **no**
  support-family decomposition of the exact `H` with all support
  diameters `<= 2` exists. Hence the bridge note's (F5) hypothesis in
  its literal strict form (`R <= 2`) is false on the bilinear sector;
  the true statement is the quasilocal form (Q1)+(Q3a,b).

**(Q4) Gap dependence (boundary of validity).** At `m = 0` the strip
closes (`eta* = 0`) and the kernel is a genuine power law
(`|h(n)| ~ n^{-2}` in `d = 1`, fit `R^2 > 0.999`); quasilocality is
supplied specifically by `m > 0` (check T15).

## Proof

### Step 1 — strip analyticity and the explicit bound (proves Q1)

Fix `z ≠ 0` and let `μ*` attain `||z||_inf`; write `p = (p_{μ*}, p_⊥)`
and fix `p_⊥` real. Complexify `p_{μ*} = a + ib` with `|b| <= eta <
eta*`. Using `sin(a+ib) = sin a cosh b + i cos a sinh b`:

```text
    Re sin^2(a+ib) = sin^2 a cosh^2 b - cos^2 a sinh^2 b  >=  -sinh^2 eta,
    |sin^2(a+ib)|  =  sin^2 a + sinh^2 b                  <=  cosh^2 eta.  (5)
```

Hence the radicand `w(p) = m^2 + Σ_μ sin^2 p_μ` satisfies, on the
strip,

```text
    Re w  >=  m^2 - sinh^2 eta  >  0,
    |w|   <=  m^2 + (d-1) + cosh^2 eta.                                    (6)
```

(check T2 verifies (6) numerically on dense strip grids, including at
`0.99·eta*` where the floor `m^2 - sinh^2 eta` is `1.8e-3`.) Since
`Re w > 0`, `w` avoids the cut `(-∞, 0]`, the principal `s = sqrt(w)`
is analytic with `arg s ∈ (-π/4, π/4)` (so `Re s > 0`, off the
`arcsinh` cuts `±i[1, ∞)`), and `E = arcsinh(s)` is analytic on the
closed strip.

**Bound on `|E|`.** For `Re w > 0`, integrate
`arcsinh(s) = ∫_0^1 s·du / sqrt(1 + u^2 s^2)` along the straight
segment: `Re(1 + u^2 w) >= 1`, so `|sqrt(1 + u^2 s^2)| >= 1` and

```text
    |E|  =  |arcsinh(sqrt w)|  <=  |sqrt w|  <=  sqrt(m^2 + (d-1) + cosh^2 eta)
         =  C_d(eta, m).                                                   (7)
```

(check T3.) Now shift the `p_{μ*}` contour in (2) from the real
interval `[-π, π]` to `Im p_{μ*} = +eta·sgn(z_{μ*})`: the integrand is
analytic in the closed strip and `2π`-periodic in `Re p_{μ*}`, so the
two vertical sides of the rectangle cancel and the integral is
unchanged. The `+` orientation is the decaying one for the `e^{+i p·z}`
convention of (2): writing `p_{μ*} = a + i·eta·sgn(z_{μ*})`,
`|e^{i p_{μ*} z_{μ*}}| = e^{-eta·sgn(z_{μ*})·z_{μ*}} =
e^{-eta·|z_{μ*}|} = e^{-eta·||z||_inf}` (the opposite shift
`Im p_{μ*} = -eta·sgn(z_{μ*})` carries `e^{+eta·|z_{μ*}|}`, growth, and
cannot produce (3); orientation witnessed numerically, check T17).
Bounding the integrand by (7) and the normalized measure by 1
gives (3). ∎ (Q1)

### Step 2 — sharpness via the branch point (proves Q2, `d = 1`)

Suppose `|h(n)| <= C e^{-eta'·n}` (`n >= 0`, `h` even) for some
`eta' > eta*`. The Fourier series
`E_1(p) = a_tau Σ_n h(n) e^{-i p n}` then converges uniformly on every
closed strip `|Im p| <= eta''` with `eta* < eta'' < eta'`, defining an
analytic function on `|Im p| < eta'` that agrees with `E_1` on the
real axis, hence (uniqueness of analytic continuation) extends `E_1`
analytically to a neighborhood of `p* = i·eta*`. But along the
imaginary axis `p = iθ`, `θ ↑ eta*`:

```text
    E_1'(iθ)  =  i · sinh θ cosh θ / ( sqrt(m^2 - sinh^2 θ) ·
                                       sqrt(1 + m^2 - sinh^2 θ) ),
    |E_1'(iθ)|  ~  m·sqrt(1+m^2) / sqrt(m^2 - sinh^2 θ)  ->  ∞,            (8)
```

(numerator `-> m·sqrt(1+m^2) ≠ 0`, second factor `-> 1`; check T6
verifies (8) against finite differences and exhibits the divergence),
contradicting boundedness of the derivative of an analytic function
near `p*`. So no rate `eta' > eta*` is possible; with (Q1) the optimal
rate is exactly `eta* = arcsinh(m)`. ∎ (Q2, `d = 1`)

The measured rates confirm sharpness: `d = 1` log-prefactor fits land
within `0.7%` of `arcsinh(m)` across `m ∈ {0.1, 0.3, 0.5, 1.0}` with
the branch-point-predicted `n^{-3/2}` prefactor (fitted exponents
`1.56–1.73`; check T5); `Z^3` axis fits land within `0.3%` (check T8).

### Step 3 — support-family translation (proves Q3a, Q3b)

`h` real and even gives the unordered-pair regrouping in (Q3a); the
pair-term operator norm `|h(z)|` and on-site norm `|h(0)|` are exact in
the commuting-mode convention (two-site swap structure of the
hopping-bilinear authority, B6). A fixed site `x` belongs to its own
on-site term plus exactly one unordered pair `{x, x+z}` per `z ≠ 0`, so
the per-site overlap weight in the bridge note's sense (its eq. (6)) is
`W_H = |h(0)| + Σ_{z≠0}|h(z)| = ||h||_l1`, finite by (Q1) (geometric
shell sums; partial sums verified Cauchy, check T11). The tail-weight
bound (4) is (Q1) summed over `l_inf` shells of cardinality
`(2r+1)^d - (2r-1)^d` (check T12 verifies the measured tails sit below
the derived shell sums and decay at slope `eta*`). At the
single-particle level `h - h_R` is a circulant (Toeplitz) operator with
symbol `Σ_{||z||_inf > R} h(z) e^{-ip·z}`, so
`||h - h_R||_op = sup_p |symbol| <= W_tail(R)` (check T13). ∎ (Q3a,b)

### Step 4 — the exact `H` is not finite-range (proves Q3c)

**Matrix-element lemma.** In the per-site tensor-product convention,
suppose `H = Σ_Z h_Z` with every `diam_l1(Z) <= 2`, and let
`d(x, y) >= 3`. Each `h_Z` fails to contain at least one of `x, y` in
its support and therefore acts as the identity on that factor; its
matrix element between two product states that *differ at both* `x`
and `y` vanishes. Summing, every matrix element of `H` between states
differing at both `x` and `y` (and agreeing elsewhere) is zero. For the
exact bilinear `H` the element
`⟨1_x 0_y | H | 0_x 1_y⟩ = h(x - y)`, which is nonzero at
`x - y = (4,0,0)` and `(2,2,0)` (`l1`-distance 4; measured
`5.56e-3` and `1.04e-2` at `m = 0.3`, nine orders above the `1e-13`
floor, check T10; these offsets are on the even sublattice consistent
with the `π`-periodicity parity, check T9). Contradiction; no
diameter-`<= 2` support-family decomposition of the exact `H` exists on
this sector. ∎ (Q3c)

### Step 5 — gap dependence (proves Q4)

At `m = 0`, `w(p) = Σ sin^2 p_μ` vanishes at `p = 0` on the real
torus: the strip closes, (Q1) holds for no `eta > 0`, and in `d = 1`
the kernel of `arcsinh|sin p|` is a measured pure power law
(`exponent -1.998`, `R^2 = 1.00000`, exponential-rate fit `0.0000`;
the `eta = 0.05` exponential bound is violated by `1.9e3`; check T15).
Quasilocality on this sector is supplied exactly by the mass gap
`m > 0`. ∎ (Q4)

## What this supplies to the (F5) step (and what it does not)

The bridge note's (F5) hypothesis, restricted to the **bilinear free
two-step sector**, should be replaced by the following proved
statements:

1. **Strict form false.** The exact `H = -log(T_hat^2)/(2 a_tau)` does
   **not** admit a `(q <= 4, R <= 2, W <= |m| + 300)` support-family
   decomposition: it has nonzero hopping coefficients at `l1`-range 4
   (Q3c). The (F5) implication remains valid (its hypothesis is simply
   not satisfied by the exact `H` on this sector); what is false is any
   hope of discharging the hypothesis as literally stated.
2. **Quasilocal form true with explicit constants.** The exact `H` is
   a `q = 2` quasilocal family with total per-site weight
   `W_H = ||h||_l1 < ∞`, truncations `H_R` satisfying the bridge
   note's lemma hypotheses at every finite `R`
   (`q = 2`, `diam_l1 <= d·R`, `W <= W_H`), and remainder per-site
   weight `W_tail(R) <= O((1+R)^{d-1} e^{-eta R})` for every
   `eta < arcsinh(m)` — with the rate sharp at `arcsinh(m)`.
3. **Named remaining step (not claimed here).** Composing the bridge
   note's finite-range Lieb-Robinson lemma applied to `H_R` with a
   Duhamel/interpolation control of the exponentially small tail
   `H - H_R` (the standard quasilocal-LR argument, optimizing `R`
   against distance) would yield an exponential lightcone for the exact
   `H` on this sector. That composition is a separate one-step theorem
   and is **not** proved in this note; this note supplies exactly its
   quantitative inputs.

The microcausality bridge note could therefore cite this note at its
(F5) paragraph as: *"on the free bilinear two-step sector the (F5)
hypothesis is false as stated but holds in quasilocal form with sharp
rate `arcsinh(m)` and explicit constants
(`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10`);
the gauged/interacting sector remains open."* This note does not edit
the bridge note; that decision belongs to its owning lane.

## No-Go Discipline Gate for the strict finite-range finding

**Status: PASS for the scoped negative only.** The negative claim is not that
log-transfer locality fails. It is only that, on the free bilinear two-step
sector, the exact log Hamiltonian is not a diameter-`<= 2` finite-range
support family; the quasilocal replacement is proved above.

- **N1 alternative routes.** Literal diameter-`<= 2` finite range was tested
  and fails by explicit nonzero matrix elements at range 4. Larger finite
  range is not claimed and is not supported by the nonzero tail evidence.
  Quasilocal exponential tails are proved and are the positive route.
  Gauged/interacting locality remains open. A quasilocal Lieb-Robinson
  composition remains a separate theorem.
- **N2 wall independence.** There is one scoped wall: strict finite range of
  the exact free bilinear log. The gauged/interacting and quasilocal-LR
  composition problems are separate open tasks, not additional walls claimed
  here.
- **N3 hidden-wall scan.** The `d = 3` carrier is declared, not imported as a
  retained theorem. Standard complex-analysis steps are proved in-note by
  the contour-shift inequalities and checked by the runner.
- **N4 residual matching.** The residual matched here is the bridge note's
  finite-range support-family hypothesis on the exact reconstructed
  Hamiltonian, restricted to the free bilinear sector. It is not a claim
  about interacting `T_hat^2[U]`.
- **N5 rhetoric audit.** "False" means "the strict `R <= 2` support-family
  form is false on this sector." It does not mean the bridge program fails;
  the note supplies a quasilocal replacement.
- **N6 partial-closure path.** The closure path is a theorem-level reframe
  from strict finite range to quasilocal exponential tails. No new axiom,
  primitive, or Tier-A admission is requested.
- **N7 steelman.** A hostile reviewer should say the result is only for the
  free bilinear translation-invariant symbol and does not prove the
  interacting/gauged log-transfer locality or the quasilocal-LR composition.
  This note accepts that steelman and declares both as open.
- **N8 cross-cycle echo.** Prior exact-log concerns came from BCH
  range-growth. This note confirms the range growth but replaces it with a
  quantitative exponential-tail statement on the free bilinear sector, so
  the old wall is narrowed rather than promoted to a new foundational
  premise.

## Hypothesis set used

- **Two-step transfer object** — symbol
  `e^{-2E_1(p)}` and `H = -log(T_hat^2)/(2 a_tau)` from the two-step
  positivity note; blocked-time normalization from
  the spectrum-condition note. The runner
  re-derives the `d = 1` symbol from the action-derived
  `T_odd·T_even` monodromy (T1) rather than trusting the citation.
- **Declared `d = 3` carrier** — symbol (1) at `d = 3` (explicit
  boundary; see Setup). No retained note currently displays the `Z^3`
  dispersion; the proofs are symbol-generic in `d`.
- **Per-site commuting-mode convention and pair norms** — the
  hopping-bilinear authority, same
  convention as the bridge note's (F4)/(F5).
- **Standard complex analysis on the torus** — contour shift /
  Paley-Wiener mechanism, principal-branch composition, uniqueness of
  analytic continuation; all inequalities ((5)-(8)) are derived in-note
  and re-verified numerically by the runner. No literature constant is
  imported.
- **No fitted parameters, no observed values, no empirical
  comparators.** The only inputs are `m`, `a_tau`, and `d`.

## Honest status

**Narrow theorem on the free bilinear two-step sector.** What is
proved: (Q1) explicit exponential kernel bound for every
`eta < arcsinh(m)` with closed-form prefactor; (Q2) exact sharpness in
`d = 1` (branch-point obstruction) with `Z^3`-axis numerical
confirmation; (Q3) the support-family/overlap-weight translation with
finite `W_H`, exponentially decaying tail weights, and single-particle
truncation control; (Q3c) the exact `H` is not finite-range, so the
strict (F5) reading fails on this sector; (Q4) `m > 0` is load-bearing.

**What this rules out.**

- Treating the exact-log quasilocality on the bilinear sector as open,
  unquantified, or rate-unknown: the rate is `arcsinh(m)` exactly and
  the constants are explicit.
- Discharging (F5) **as literally stated** (`R <= 2`) on the bilinear
  sector: the exact `H` has genuine range-4 hops. Any
  consumer of (F5) must use the quasilocal form.
- The worry that "BCH commutators enlarge range" silently destroys
  locality of the exact log on this sector: they enlarge range from 2
  to infinity, but with tails dying at the sharp exponential rate
  `arcsinh(m)`.

**Not in scope (declared boundaries).**

- The **gauged / interacting** log-transfer locality: fixed-background
  `T_hat^2[U]` is not
  translation-invariant, the Fourier route does not apply verbatim, and
  the `U`-integrated interacting case is open. This is the named open
  frontier left by this note.
- A formalized `d = 3` sharpness **lower bound** (the upper bound (Q1)
  is proved for all `d`; sharpness is proved in `d = 1` and verified
  numerically on `Z^3` axes).
- The quasilocal Lieb-Robinson **composition** step (item 3 above).
- The `m = 0` massless sector (power-law tails, (Q4)); continuum
  limits; OS reconstruction; any audit status or promotion.

## Runner and cache

```bash
python3 scripts/transfer_matrix_log_quasilocality_check_2026_06_10.py
```

Deterministic (no random input), runtime under 5 minutes. The runner checks
the symbol anchor, strip inequalities, `d = 1` and `Z^3` kernel bounds,
sharp-rate fits, branch-point obstruction, even-sublattice support,
not-finite-range exhibit, overlap weights, truncation tails, `a_tau` scaling,
two falsification legs (the gapless boundary and a positive, gapped,
long-range-perturbed comparator symbol that violates the derived bound),
and the Step 1 contour-shift orientation witness (shifted-contour
identity at `Im p = +eta·sgn(z)`; growth on the opposite orientation).

Runner cache: [`logs/runner-cache/transfer_matrix_log_quasilocality_check_2026_06_10.txt`](../logs/runner-cache/transfer_matrix_log_quasilocality_check_2026_06_10.txt) (PASS=19, FAIL=0).

## Citations

- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  — the load-bearing object (`T_hat^2`, symbol,
  `H = -log(T_hat^2)/(2 a_tau)`), `d = 1` free case.
- [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
  — blocked-time normalization and
  well-definedness of the reconstructed `H`.
- [`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`](HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md)
  — per-site mode convention and exact pair norms.
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
  — provenance of `T` (context).
- `MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`
  — defines the (F5) hypothesis and the
  support-family vocabulary `(q, R, W)` this note answers in. Cited as
  the target gap, not as an authority for any claim here (plain-text
  filename: downstream target, not an upstream premise).
- `RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`
  — unaudited; prior qualitative free-surface instance of the same
  spectral route (analyticity ⟹ some exponential tail, fitted rate
  within ~2x). Context only; this note is self-contained, derives the
  sharp rate and explicit constants, and adds the support-family
  translation and the strict-(F5)-falsity finding.
- `MICROCAUSALITY_EXACT_H_EXPANSION_ROUTE_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-09.md`
  — unaudited; route triage that closed the one-step expansion route
  and named the spectral route live. Context only.
- Proof-technique provenance (no bound or constant imported):
  Paley-Wiener / torus contour-shift exponential-decay mechanism
  (standard complex analysis; reproved in-note as Step 1).

## Changelog

- **2026-06-10** — initial note. Narrow theorem: explicit exponential
  quasilocality bound (3) with closed-form prefactor
  `C_d(eta, m) = sqrt(m^2 + (d-1) + cosh^2 eta)` for the exact
  log-transfer Hamiltonian of the free staggered
  two-step transfer matrix; sharp rate `arcsinh(m)` (proved `d = 1`,
  verified `<= 0.3%` on `Z^3` axes); support-family translation
  (finite `W_H = ||h||_l1`, exponential tail weights, truncation
  control); negative finding that the exact `H` is not finite-range,
  so the strict `R <= 2` reading of the bridge note's (F5) fails on
  the bilinear sector and only the quasilocal reading survives.
  Falsification legs: `m = 0` power-law boundary; long-range-perturbed
  positive comparator symbol violating the derived bound. Runner
  `PASS=16 FAIL=0`. Sector restriction: free (`U = 1`) bilinear
  two-step sector; gauged/interacting log-transfer locality open.
- **2026-07-01** — repair: Step 1 contour-shift orientation corrected
  from `Im p_{μ*} = -eta·sgn(z_{μ*})` to `+eta·sgn(z_{μ*})`, the
  decaying orientation for the `e^{+i p·z}` convention of (2). No other
  step, constant, rate, or claim changed; the displayed estimate
  `|e^{i p_{μ*} z_{μ*}}| = e^{-eta·|z_{μ*}|}` was already the
  `+`-orientation value. New check T17 (a/b/c) witnesses the
  shifted-contour identity, the decay factor on the `+` orientation,
  and the growth factor on the pre-repair `-` orientation. Runner
  `PASS=19 FAIL=0`.
