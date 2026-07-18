# Reflection Positivity — Wilson Plaquette Temporal-Gauge Bridge: Sign Repair + a Manifestly-Positive Character-Coefficient Theorem (Historical 2026-06-06 Repair Record)

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The `bounded_theorem` label is a source-side
claim-boundary declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_rp_wilson_temporal_gauge_sign_and_positivity_repair_2026_06_06.py`](../scripts/frontier_rp_wilson_temporal_gauge_sign_and_positivity_repair_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_rp_wilson_temporal_gauge_sign_and_positivity_repair_2026_06_06.txt`](../logs/runner-cache/frontier_rp_wilson_temporal_gauge_sign_and_positivity_repair_2026_06_06.txt)

---

## Role

On 2026-06-06 this note responded to the then-`audited_failed` version of the
narrow theorem
[`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
(`axiom_first_reflection_positivity_wilson_temporal_gauge_bridge_narrow_theorem_note_2026-06-05`).
That note attempted to supply the **gauge-half norm-square** factor of the
reflection-positivity row's three-factor reduction — the Wilson-plaquette
temporal-gauge application named as `missing_bridge_theorem` by the target row
[`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md).
The independent audit current on that date had returned **audited_failed** with
three blockers (verbatim):

1. **(sign)** "`S_0 = +beta Re` with `exp(-S_0)` gives negative Fourier
   coefficients already for `Z_2`, where the nontrivial coefficient is
   `(e^{-beta} - e^{beta})/2 < 0`."
2. **(note↔runner drift)** "The runner source uses `exp(+S_0)`, not the
   displayed `exp(-S_0)`."
3. **(exactness overclaim)** "its `U(1)` 'exact finite-Haar' check uses a finite
   angular grid on `exp(beta cos theta)`, which is not a bounded-degree
   trigonometric polynomial."

**The audit is correct on all three.** The sign and note--runner drift blockers
share one root: the wrong sign of the plane Boltzmann weight. The finite-grid
exactness blocker is logically separate. This note fixes the sign and replaces
the grid claim with an exact representation-ring proof. The runner's
FFT/quadrature/Monte-Carlo/truncation values are support for that proof, not the
proof itself. Runner: **17 PASS / 0 FAIL**.

## 0. The single root, and the fix

The standard Wilson convention is
`S_W = -(beta/N) \sum_p \mathrm{Re}\,\mathrm{Tr}\,U_p` (plus a constant), so the
partition function carries the **ferromagnetic** Boltzmann weight

```text
    Z = \int \prod dU\; e^{-S_W} = \int \prod dU\; e^{+(beta/N)\sum_p \mathrm{Re}\,\mathrm{Tr}\,U_p}.
```

Write `alpha := beta/N`. The straddling reflection-plane weight is therefore

```text
    e^{+alpha\,\mathrm{Re}\,\mathrm{Tr}[U_+\,U_-^\dagger]}      (FERROMAGNETIC, alpha >= 0),
```

equivalently the plane action is `S_0 := -alpha\,\mathrm{Re}\,\mathrm{Tr}[U_+U_-^\dagger]`
so that `e^{-S_0}` **is** this ferromagnetic weight. The failed note instead wrote
`S_0 = +alpha\,\mathrm{Re}\,\mathrm{Tr}` together with the weight `e^{-S_0}`, i.e.
the **antiferromagnetic** weight `e^{-alpha\,\mathrm{Re}\,\mathrm{Tr}}`, whose
character coefficients can be negative and whose finite restrictions can be
non-PSD. Its runner silently used the correct
ferromagnetic exponential — hence the drift. Aligning both on the ferromagnetic
weight `e^{+alpha\,\mathrm{Re}\,\mathrm{Tr}}` (with `S_0 := -alpha\,\mathrm{Re}\,\mathrm{Tr}`)
fixes blockers (1) and (2) simultaneously. (Runner Part A.)

## 1. (A) The sign blocker reproduced, then fixed

With the failed note's `e^{-S_0}`, `S_0 = +alpha\,\mathrm{Re}\,U`, the `Z_2`
nontrivial character coefficient is

```text
    c_1 = (1/2)\sum_{U=\pm1}\chi_1(U)\,e^{-alpha\,\mathrm{Re}\,U}
        = (e^{-alpha} - e^{+alpha})/2 = -\sinh alpha < 0,
```

exactly the audit's number (runner: `c_1 = -0.888106` at `alpha=0.8`,
`= -\sinh 0.8`). With the **ferromagnetic** weight `e^{+alpha\,\mathrm{Re}\,U}` the
two `Z_2` coefficients are

```text
    (c_0, c_1) = (\cosh alpha,\; \sinh alpha),\qquad \text{both} \ge 0,
```

(Runner A1/A2.) The same sign flip repairs every group below.

## 2. (B) Plane-kernel positivity — exact, manifestly positive, group-general

The plane weight is a class function of `U_+U_-^\dagger`. RP requires its
expansion in irreducible characters to have **nonnegative** coefficients
(a positive Gram kernel). For any compact group equipped with a supplied
finite-dimensional unitary representation `R`, the following proof is exact
and does not use a finite grid. The Wilson application takes `R=F`, the
fundamental representation of `SU(N)`.

> **Lemma (manifest positivity).** For `alpha \ge 0`, the class function
> `e^{alpha\,\mathrm{Re}\,\chi_R(U)}` (`R` finite-dimensional and unitary) expands in
> irreducible characters with nonnegative coefficients:
> `e^{alpha\,\mathrm{Re}\,\chi_R} = \sum_r a_r(alpha)\,\chi_r`, `a_r(alpha) \ge 0`.
>
> *Proof.* `\mathrm{Re}\,\chi_R = \tfrac12(\chi_R + \chi_{\bar R})`, so
> `e^{alpha\,\mathrm{Re}\,\chi_R} = e^{(alpha/2)\chi_R}\,e^{(alpha/2)\chi_{\bar R}}
> = \big[\sum_k \tfrac{(alpha/2)^k}{k!}\chi_R^k\big]\big[\sum_m \tfrac{(alpha/2)^m}{m!}\chi_{\bar R}^m\big]`.
> The tensor powers satisfy `\chi_R^k = \sum_r M^{(k)}_r \chi_r` with
> `M^{(k)}_r \in \mathbb{Z}_{\ge 0}` (tensor-power multiplicities), and products of
> characters decompose with nonnegative fusion (Clebsch–Gordan / Littlewood–Richardson)
> coefficients `N^t_{rs} \ge 0`. Hence each `a_r(alpha)` is a sum of products of
> nonnegative numbers, so `a_r(alpha) \ge 0`. ∎

This is the exact replacement for the finite-grid step, and it is **group-general**.
The runner verifies it concretely:

- **`Z_2`:** coefficients `(\cosh alpha, \sinh alpha) \ge 0`; the odd
  coefficient vanishes at `alpha=0`. (Part A.)
- **`Z_N`:** the exact finite-group Fourier coefficients of
  `e^{alpha\cos(2\pi j/N)}` are all `\ge 0`, and equal
  `\sum_{m\equiv q\ (N)} I_m(alpha)` by Poisson summation — positivity inherited
  from the Bessel positivity below. The runner evaluates these finite sums in
  floating arithmetic for `N\in\{2,3,4,5\}`. (Part B2.)
- **`U(1)`:** `c_n = I_n(alpha)`, reproven by the **power series**
  `I_n(alpha) = \sum_{k\ge0} \tfrac{(alpha/2)^{2k+n}}{k!\,(n+k)!}`, whose terms
  are **nonnegative** — exact, no grid. For `alpha=0`, all nontrivial modes
  vanish. The uniform-grid quadrature is kept
  only as a machine-precision **cross-check** (`max|series-grid| = 7\times10^{-16}`),
  not as the proof. (Part B1/B1'.) This retires the "exact finite-Haar" overclaim
  (blocker 3): the integrand `e^{alpha\cos\theta}` is an entire function with
  infinitely many Fourier modes, so a finite grid is spectrally-convergent
  quadrature, **not** an exact evaluation; the power series is the exact statement.
- **`SU(2)`:** the representation-ring lemma proves coefficient positivity
  exactly. The runner's Weyl quadrature and order-12 reconstruction from
  nonnegative-integer tensor-power multiplicities are finite numerical support,
  not an all-order reconstruction. (Part B3/B3'/B3''.)
- **`SU(3)`** (the physically relevant group): the Haar-projected coefficients
  `\langle e^{+alpha\,\mathrm{Re}\,\mathrm{Tr}\,U}, \chi_R\rangle` for
  `R\in\{1,3,\bar3,8,6,\bar6,10\}` are all `\ge 0`; the exact reason is the Lemma
  (`e^{alpha\,\mathrm{Re}\,\mathrm{Tr}} = e^{(alpha/2)\chi_3}e^{(alpha/2)\chi_{\bar3}}`
  with nonnegative tensor/fusion multiplicities), exhibited on
  `\chi_3\chi_3 = \chi_6 + \chi_{\bar3}` (nonnegative fusion). (Part B4/B5.)

## 3. (C, D) The integrated three-factor RP Gram is PSD (correct sign)

With the ferromagnetic weight, the reflected Gram over the `A_+^{(2)}`
observable basis factorizes as in the target row's reduction,

```text
    e^{-S}\,\overline{F_I(c_0)}\,F_J(c_1)
      = \underbrace{e^{+S_+(c_0)}\overline{F_I(c_0)}}_{\text{reflected half}}
        \;\underbrace{e^{+alpha\,\mathrm{Re}\,\mathrm{Tr}[U_+U_-^\dagger]}}_{\text{plane positive kernel}}
        \;\underbrace{e^{+S_+(c_1)}F_J(c_1)}_{\text{positive half}},
```

and, inserting the plane-kernel spectral decomposition
`e^{+S_0}=\sum_a \kappa_a\,\phi_a(c_0)\overline{\phi_a(c_1)}` with `\kappa_a\ge0`,

```text
    G_{IJ} = \sum_a \kappa_a\,W_I(a)\,\overline{W_J(a)} \;\Longleftrightarrow\; G = W\,\mathrm{diag}(\kappa)\,W^\dagger \succeq 0.
```

The runner exhausts the finite `Z_N` carrier with floating transcendental
weights for `N\in\{2,3,4,5\}`, `alpha\in\{0.3,1,2.5\}` (Part C1), and checks
the manifest factorization
`G = W\,\mathrm{diag}(\kappa)\,W^\dagger` with `\kappa\ge0` to `1.8\times10^{-13}`
(Part D). These finite residuals support the exact factorization argument above.

## 4. (E) Teeth — the wrong sign genuinely breaks positivity

This was the failed note's hidden danger, and it is now an explicit control. With
the **note-as-written antiferromagnetic** sign `e^{-alpha\,\mathrm{Re}\,\mathrm{Tr}}`,
**both** the plane kernel and the integrated Gram are **non-PSD** across
`Z_N` (e.g. `Z_2`: plane-kernel `\min\mathrm{eig} = -1.78`, integrated Gram
`-3.08`). (Part E1.) Independently, dropping `\Theta`'s antilinear conjugation
also gives a non-PSD form (`\min\mathrm{eig} = -0.48`, Part E2). So both the
**sign** of the weight and the **antilinearity** of the reflection are
load-bearing: the failed note's statement was false *as written*, not merely
mislabeled, and the repair is a genuine correction.

## 5. What this note does NOT claim

- It does **not** supply the **fermion-sector** transfer-positivity factor or the
  positive determinant weight (the row's other separately tracked factors;
  their current standing is audit-lane-owned). This is the **gauge-half (bosonic)**
  factor only.
- It does **not** prove a fully-integrated interacting `SU(N)` RP from scratch on
  a finite carrier; the `SU(N)` statement here is the exact **plane-kernel
  coefficient positivity** (the Lemma) plus finite `Z_N`/`U(1)`/`SU(2)` Gram
  support and the sampled `SU(3)` projection. The full multi-slice interacting
  integration is out of scope.
- It does **not** establish continuum / OS-reconstruction RP in the Wightman
  sense; this is a lattice statement.
- It does **not** retag, promote, or set the status of the historical target
  version, the target reflection-positivity row, or any upstream row. The audit
  lane is the only status authority; this note makes a **re-audit case** only.
- It introduces **no** new axiom, primitive, repo vocabulary, or class tag, and
  consumes **no** PDG / fitted / measured / lattice-MC / `beta=6` / `g_bare`
  value as a derivation input.

## 6. Re-audit case (no status set here)

The three blockers recorded on 2026-06-06 are each discharged: **(1)+(2)** the
sign root is fixed (ferromagnetic weight `e^{+alpha\,\mathrm{Re}\,\mathrm{Tr}}`,
`S_0 := -alpha\,\mathrm{Re}\,\mathrm{Tr}`, note and runner consistent), with the
`Z_2` coefficient now `+\sinh alpha \ge 0` (strict for `alpha>0`); **(3)** the "exact finite-Haar"
overclaim is replaced by the manifestly-positive power-series / tensor-multiplicity
argument, which is exact and group-general (and the grid is demoted to a
cross-check). The non-abelian case is **upgraded** from a numeric `SU(2)` sample to
an exact `SU(N)` coefficient-positivity theorem. This historical packet does
not state the target's current standing or how it bears on the target RP row;
those questions remain for the independent audit lane.

## 7. Historical bounded-wall checklist (not a current N1--N8 record)

This is the dated repair packet's reasoning inventory. It predates the current
N1--N8 artifact schema and does not claim current gate compliance. The current
five-resolution, hostile, and independent records live in the repaired target
note and its primary and independent N7 runners.

- **H1 (routes).** (a) keep the failed sign — *ruled out* (Part E, non-PSD);
  (b) ferromagnetic sign + finite grid — *insufficient* (grid not exact for an
  entire integrand); (c) ferromagnetic sign + power-series/tensor-multiplicity
  positivity — **adopted** (exact, general). (d) full interacting `SU(N)` finite
  reprove — *out of scope*.
- **H2 (wall independence).** Three independent walls, each reproven: the
  reflection split `S_- = \Theta S_+` with plane-symmetric `S_0`; the
  nonnegativity of the plane-kernel character coefficients (the Lemma); the
  spectral PSD of `G = W\,\mathrm{diag}(\kappa)\,W^\dagger`.
- **H3 (hidden-wall scan).** Explicit premises: temporal gauge `U_0 = 1`; the
  antilinear link/time reflection `\Theta`; Haar measure; the `A_+^{(2)}`
  character-degree-`\le2` observable basis; `alpha\ge0` (ferromagnetic). All named.
- **H4 (residual matching).** Repair item ↔ supplied: sign root → Part A; plane
  norm-square → Part B (exact, general); integrated PSD → Parts C/D; sign-teeth →
  Part E. Fermion sector / determinant weight → out of scope (row's other
  factors).
- **H5 (rhetoric).** "Exact" means the source's positive-term power series and
  representation-ring identities, not the runner's FFT, quadrature,
  Monte-Carlo, or truncated reconstruction. "`SU(N)` theorem" means the
  coefficient-positivity lemma, not a full interacting finite computation.
- **H6 (partial-closure).** No new axiom/primitive. Legitimate path: correct the
  sign, prove positivity exactly, leave the fermion factor and full `SU(N)`
  integration to the row's other dependencies.
- **H7 (steelman).** A hostile reviewer could ask for an exact multi-slice
  interacting `SU(3)` Gram. That is out of the bounded scope; the bounded surface
  is the plane-kernel positivity (exact, general) plus finite abelian/`SU(2)`
  Gram support, which displays the mechanism (correct sign + nonnegative
  character kernel + spectral Gram factorization).
- **H8 (cross-cycle echo).** The governance lesson — the target row's history of a
  non-PSD single-step Gram under a wrong reflection convention — is honored here:
  this note pins **both** the antilinear `\Theta` **and** the ferromagnetic sign,
  and exhibits the non-PSD controls for getting either wrong (Part E).

## 8. Reprove-and-cite ledger

- **Exact source algebra:** the `Z_2` sign flip (`-\sinh alpha` versus
  `+\sinh alpha`); `I_n(alpha)\ge0` from its nonnegative-term series (with
  the nontrivial modes zero at `alpha=0`); the all-order
  representation-ring coefficient proof; and the spectral implication
  `G=W\,\mathrm{diag}(\kappa)W^\dagger\succeq0` once `\kappa\ge0`.
- **Runner support:** floating finite-Haar/Poisson reconstruction, SU(2) Weyl
  quadrature and order-12 multiplicities, sampled SU(3) coefficients, finite
  integrated-Gram residuals, and the deterministic antiferromagnetic-sign and
  dropped-conjugation non-PSD controls.
- **Cited** (comparator only, never a derivation input): Osterwalder & Seiler,
  *Ann. Phys.* **110** (1978) 440 (link reflection positivity for the Wilson
  action); Montvay & Münster, *Quantum Fields on a Lattice* (CUP 1994) Sec. 3.4;
  the Jacobi–Anger / modified-Bessel expansion `e^{z\cos t}=\sum_n I_n(z)e^{int}`,
  `I_n(z)\ge0`; the Peter–Weyl character expansion of a positive class function on
  a compact group.

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It
does not promote this note or change any audited claim scope.

- [AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- [REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md)
- [RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md)
- [AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)

### Source-note boundary

**Hypothesis set:** (1) pure-gauge Wilson plaquette action on the two-time-slice
lattice, periodic spatial direction, temporal gauge `U_0 = 1`, **ferromagnetic
Wilson sign** (`S_W = -(beta/N)\mathrm{Re}\,\mathrm{Tr}\,U_p`, `beta\ge0`); (2) the
antilinear link/time reflection `\Theta(F)=\overline{F\circ\theta}`, Haar measure;
(3) the `A_+^{(2)}` observable basis; (4) the retained gauge-half norm-square
hypotheses realized on this data; (5) standard compact-group character
nonnegativity, reproven here by the power-series / tensor-multiplicity Lemma. The
exact source proof is the group-and-representation lemma plus its spectral Gram
factorization. The `Z_N`/`U(1)`/`SU(2)` reconstructions and `SU(3)` projection
are finite numerical support.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class
tag; only standard mathematics ("reflection positivity," "link reflection,"
"temporal gauge," "character," "Haar measure," "Peter–Weyl," "fusion
coefficients") and the repo-canonical "`A_+^{(2)}`," "gauge-half,"
"three-factor reduction." No fitted/observed/PDG/lattice-MC/`beta=6`/`g_bare`
value is consumed.

**No-promotion statement:** this note does **not** promote, demote, or set the
audit status of the failed bridge note, the target reflection-positivity row, or
any upstream row. The audit lane is the only status authority.
