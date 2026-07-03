# Reflection Positivity — Wilson Plaquette Temporal-Gauge Bridge: Sign Repair + a Manifestly-Positive Character-Coefficient Theorem (Repairs the `audited_failed` Bridge)

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

This note **repairs** the `audited_failed` narrow theorem
[`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
(`axiom_first_reflection_positivity_wilson_temporal_gauge_bridge_narrow_theorem_note_2026-06-05`).
That note attempted to supply the **gauge-half norm-square** factor of the
reflection-positivity row's three-factor reduction — the Wilson-plaquette
temporal-gauge application named as `missing_bridge_theorem` by the target row
[`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md).
The independent audit returned **audited_failed** with three blockers (verbatim):

1. **(sign)** "`S_0 = +beta Re` with `exp(-S_0)` gives negative Fourier
   coefficients already for `Z_2`, where the nontrivial coefficient is
   `(e^{-beta} - e^{beta})/2 < 0`."
2. **(note↔runner drift)** "The runner source uses `exp(+S_0)`, not the
   displayed `exp(-S_0)`."
3. **(exactness overclaim)** "its `U(1)` 'exact finite-Haar' check uses a finite
   angular grid on `exp(beta cos theta)`, which is not a bounded-degree
   trigonometric polynomial."

**The audit is correct on all three.** They share **one root**: the wrong sign of
the plane Boltzmann **weight**. This note fixes that root, proves the plane-kernel
positivity by an **exact, group-general** argument (replacing the finite grid),
and in doing so **upgrades** the non-abelian statement from a numeric `SU(2)`
Monte-Carlo sample to an exact theorem for `SU(N)`. Runner: **17 PASS / 0 FAIL**.

## 0. The single root, and the fix

The standard Wilson convention is
`S_W = -(beta/N) \sum_p \mathrm{Re}\,\mathrm{Tr}\,U_p` (plus a constant), so the
partition function carries the **ferromagnetic** Boltzmann weight

```text
    Z = \int \prod dU\; e^{-S_W} = \int \prod dU\; e^{+(beta/N)\sum_p \mathrm{Re}\,\mathrm{Tr}\,U_p}.
```

The straddling reflection-plane weight is therefore

```text
    e^{+beta\,\mathrm{Re}\,\mathrm{Tr}[U_+\,U_-^\dagger]}      (FERROMAGNETIC, beta > 0),
```

equivalently the plane action is `S_0 := -beta\,\mathrm{Re}\,\mathrm{Tr}[U_+U_-^\dagger]`
so that `e^{-S_0}` **is** this ferromagnetic weight. The failed note instead wrote
`S_0 = +beta\,\mathrm{Re}\,\mathrm{Tr}` together with the weight `e^{-S_0}`, i.e.
the **antiferromagnetic** weight `e^{-beta\,\mathrm{Re}\,\mathrm{Tr}}`, whose
character coefficients alternate in sign. Its runner silently used the correct
ferromagnetic `e^{+S_0}` — hence the drift. Aligning both on the ferromagnetic
weight `e^{+beta\,\mathrm{Re}\,\mathrm{Tr}}` (with `S_0 := -beta\,\mathrm{Re}\,\mathrm{Tr}`)
fixes blockers (1) and (2) simultaneously. (Runner Part A.)

## 1. (A) The sign blocker reproduced, then fixed

With the failed note's `e^{-S_0}`, `S_0 = +beta\,\mathrm{Re}\,U`, the `Z_2`
nontrivial character coefficient is

```text
    c_1 = (1/2)\sum_{U=\pm1}\chi_1(U)\,e^{-beta\,\mathrm{Re}\,U}
        = (e^{-beta} - e^{+beta})/2 = -\sinh beta < 0,
```

exactly the audit's number (runner: `c_1 = -0.888106` at `beta=0.8`,
`= -\sinh 0.8`). With the **ferromagnetic** weight `e^{+beta\,\mathrm{Re}\,U}` the
two `Z_2` coefficients are

```text
    (c_0, c_1) = (\cosh beta,\; \sinh beta),\qquad \text{both} > 0.
```

(Runner A1/A2.) The same sign flip repairs every group below.

## 2. (B) Plane-kernel positivity — exact, manifestly positive, group-general

The plane weight is a class function of `U_+U_-^\dagger`. RP requires its
expansion in irreducible characters to have **nonnegative** coefficients
(a positive Gram kernel). We prove this **exactly** for every compact gauge group,
not by a finite grid.

> **Lemma (manifest positivity).** For `beta \ge 0`, the class function
> `e^{beta\,\mathrm{Re}\,\chi_F(U)}` (`\chi_F` = fundamental character) expands in
> irreducible characters with nonnegative coefficients:
> `e^{beta\,\mathrm{Re}\,\chi_F} = \sum_r a_r(beta)\,\chi_r`, `a_r(beta) \ge 0`.
>
> *Proof.* `\mathrm{Re}\,\chi_F = \tfrac12(\chi_F + \chi_{\bar F})`, so
> `e^{beta\,\mathrm{Re}\,\chi_F} = e^{(beta/2)\chi_F}\,e^{(beta/2)\chi_{\bar F}}
> = \big[\sum_k \tfrac{(beta/2)^k}{k!}\chi_F^k\big]\big[\sum_m \tfrac{(beta/2)^m}{m!}\chi_{\bar F}^m\big]`.
> The tensor powers satisfy `\chi_F^k = \sum_r M^{(k)}_r \chi_r` with
> `M^{(k)}_r \in \mathbb{Z}_{\ge 0}` (tensor-power multiplicities), and products of
> characters decompose with nonnegative fusion (Clebsch–Gordan / Littlewood–Richardson)
> coefficients `N^t_{rs} \ge 0`. Hence each `a_r(beta)` is a sum of products of
> nonnegative numbers, so `a_r(beta) \ge 0`. ∎

This is the exact replacement for the finite-grid step, and it is **group-general**.
The runner verifies it concretely:

- **`Z_2`:** coefficients `(\cosh beta, \sinh beta) > 0`. (Part A.)
- **`Z_N`:** the exact finite-group Fourier coefficients of
  `e^{beta\cos(2\pi j/N)}` are all `> 0`, and equal
  `\sum_{m\equiv q\ (N)} I_m(beta)` by Poisson summation — positivity inherited
  from the Bessel positivity below. (Part B2, exact; `N\in\{2,3,4,5\}`.)
- **`U(1)`:** `c_n = I_n(beta)`, reproven by the **power series**
  `I_n(beta) = \sum_{k\ge0} \tfrac{(beta/2)^{2k+n}}{k!\,(n+k)!}`, which is
  **positive term by term** — exact, no grid. The uniform-grid quadrature is kept
  only as a machine-precision **cross-check** (`max|series-grid| = 7\times10^{-16}`),
  not as the proof. (Part B1/B1'.) This retires the "exact finite-Haar" overclaim
  (blocker 3): the integrand `e^{beta\cos\theta}` is an entire function with
  infinitely many Fourier modes, so a finite grid is spectrally-convergent
  quadrature, **not** an exact evaluation; the power series is the exact statement.
- **`SU(2)`:** the exact character coefficients `a_n` of `e^{beta\chi_{1/2}}`
  (Weyl integration) are all `> 0`, and **equal** the reconstruction from the
  nonnegative-integer tensor-power multiplicities of `\chi_{1/2}^k` (the ballot
  numbers). So `SU(2)` positivity is now an **exact theorem**, not the failed
  note's Monte-Carlo sample. (Part B3/B3'/B3''.)
- **`SU(3)`** (the physically relevant group): the Haar-projected coefficients
  `\langle e^{+beta\,\mathrm{Re}\,\mathrm{Tr}\,U}, \chi_R\rangle` for
  `R\in\{1,3,\bar3,8,6,\bar6,10\}` are all `\ge 0`; the exact reason is the Lemma
  (`e^{beta\,\mathrm{Re}\,\mathrm{Tr}} = e^{(beta/2)\chi_3}e^{(beta/2)\chi_{\bar3}}`
  with nonnegative tensor/fusion multiplicities), exhibited on
  `\chi_3\chi_3 = \chi_6 + \chi_{\bar3}` (nonnegative fusion). (Part B4/B5.)

## 3. (C, D) The integrated three-factor RP Gram is PSD (correct sign)

With the ferromagnetic weight, the reflected Gram over the `A_+^{(2)}`
observable basis factorizes as in the target row's reduction,

```text
    e^{-S}\,\overline{F_I(c_0)}\,F_J(c_1)
      = \underbrace{e^{+S_+(c_0)}\overline{F_I(c_0)}}_{\text{reflected half}}
        \;\underbrace{e^{+beta\,\mathrm{Re}\,\mathrm{Tr}[U_+U_-^\dagger]}}_{\text{plane positive kernel}}
        \;\underbrace{e^{+S_+(c_1)}F_J(c_1)}_{\text{positive half}},
```

and, inserting the plane-kernel spectral decomposition
`e^{+S_0}=\sum_a \kappa_a\,\phi_a(c_0)\overline{\phi_a(c_1)}` with `\kappa_a\ge0`,

```text
    G_{IJ} = \sum_a \kappa_a\,W_I(a)\,\overline{W_J(a)} \;\Longleftrightarrow\; G = W\,\mathrm{diag}(\kappa)\,W^\dagger \succeq 0.
```

The runner verifies `G\succeq0` exactly for `Z_N`, `N\in\{2,3,4,5\}`,
`beta\in\{0.3,1,2.5\}` (Part C1), and exhibits the manifest factorization
`G = W\,\mathrm{diag}(\kappa)\,W^\dagger` with `\kappa\ge0` to `1.8\times10^{-13}`
(Part D).

## 4. (E) Teeth — the wrong sign genuinely breaks positivity

This was the failed note's hidden danger, and it is now an explicit control. With
the **note-as-written antiferromagnetic** sign `e^{-beta\,\mathrm{Re}\,\mathrm{Tr}}`,
**both** the plane kernel and the integrated Gram are **non-PSD** across
`Z_N` (e.g. `Z_2`: plane-kernel `\min\mathrm{eig} = -1.78`, integrated Gram
`-3.08`). (Part E1.) Independently, dropping `\Theta`'s antilinear conjugation
also gives a non-PSD form (`\min\mathrm{eig} = -0.48`, Part E2). So both the
**sign** of the weight and the **antilinearity** of the reflection are
load-bearing: the failed note's statement was false *as written*, not merely
mislabeled, and the repair is a genuine correction.

## 5. What this note does NOT claim

- It does **not** supply the **fermion-sector** transfer-positivity factor or the
  positive determinant weight (the row's other two, already
  `retained`/`retained_bounded`, factors). This is the **gauge-half (bosonic)**
  factor only.
- It does **not** prove a fully-integrated interacting `SU(N)` RP from scratch on
  a finite carrier; the `SU(N)` statement here is the exact **plane-kernel
  coefficient positivity** (the Lemma) plus the `Z_N`/`U(1)`/`SU(2)` exact Gram
  computations and the `SU(3)` projection. The full multi-slice interacting
  integration is out of scope.
- It does **not** establish continuum / OS-reconstruction RP in the Wightman
  sense; this is a lattice statement.
- It does **not** retag, promote, or set the status of the failed note, the target
  reflection-positivity row, or any upstream row. The audit lane is the only
  status authority; this note makes a **re-audit case** only.
- It introduces **no** new axiom, primitive, repo vocabulary, or class tag, and
  consumes **no** PDG / fitted / measured / lattice-MC / `beta=6` / `g_bare`
  value as a derivation input.

## 6. Re-audit case (no status set here)

The failed note's three blockers are each discharged: **(1)+(2)** the sign root is
fixed (ferromagnetic weight `e^{+beta\,\mathrm{Re}\,\mathrm{Tr}}`,
`S_0 := -beta\,\mathrm{Re}\,\mathrm{Tr}`, note and runner consistent), with the
`Z_2` coefficient now `+\sinh beta > 0`; **(3)** the "exact finite-Haar"
overclaim is replaced by the manifestly-positive power-series / tensor-multiplicity
argument, which is exact and group-general (and the grid is demoted to a
cross-check). The non-abelian case is **upgraded** from a numeric `SU(2)` sample to
an exact `SU(N)` coefficient-positivity theorem. Whether this lifts the
gauge-half bridge out of `audited_failed`, and how that bears on the target RP
row, is for the independent audit lane to decide.

## 7. Bounded-Wall Discipline Gate (N1–N8)

**Result:** PASS for the scoped claim "the gauge-half Wilson-plaquette
temporal-gauge plane weight is, with the correct ferromagnetic sign, a positive
character Gram kernel (exactly, all compact groups), and the integrated
three-factor RP Gram over `A_+^{(2)}` is PSD (`Z_N`/`U(1)` exact)."

- **N1 (routes).** (a) keep the failed sign — *ruled out* (Part E, non-PSD);
  (b) ferromagnetic sign + finite grid — *insufficient* (grid not exact for an
  entire integrand); (c) ferromagnetic sign + power-series/tensor-multiplicity
  positivity — **adopted** (exact, general). (d) full interacting `SU(N)` finite
  reprove — *out of scope*.
- **N2 (wall independence).** Three independent walls, each reproven: the
  reflection split `S_- = \Theta S_+` with plane-symmetric `S_0`; the
  nonnegativity of the plane-kernel character coefficients (the Lemma); the
  spectral PSD of `G = W\,\mathrm{diag}(\kappa)\,W^\dagger`.
- **N3 (hidden-wall scan).** Explicit premises: temporal gauge `U_0 = 1`; the
  antilinear link/time reflection `\Theta`; Haar measure; the `A_+^{(2)}`
  character-degree-`\le2` observable basis; `beta\ge0` (ferromagnetic). All named.
- **N4 (residual matching).** Repair item ↔ supplied: sign root → Part A; plane
  norm-square → Part B (exact, general); integrated PSD → Parts C/D; sign-teeth →
  Part E. Fermion sector / determinant weight → out of scope (row's other
  factors).
- **N5 (rhetoric).** "Exact" now means power-series / finite-group-Fourier /
  Weyl-integration exact, **not** a finite grid. "`SU(N)` theorem" means the
  coefficient-positivity Lemma, not a full interacting finite computation.
- **N6 (partial-closure).** No new axiom/primitive. Legitimate path: correct the
  sign, prove positivity exactly, leave the fermion factor and full `SU(N)`
  integration to the row's other dependencies.
- **N7 (steelman).** A hostile reviewer could ask for an exact multi-slice
  interacting `SU(3)` Gram. That is out of the bounded scope; the bounded surface
  is the plane-kernel positivity (exact, general) + the abelian/`SU(2)` exact
  Gram, which already carries the full mechanism (correct sign + nonnegative
  character kernel + spectral Gram factorization).
- **N8 (cross-cycle echo).** The governance lesson — the target row's history of a
  non-PSD single-step Gram under a wrong reflection convention — is honored here:
  this note pins **both** the antilinear `\Theta` **and** the ferromagnetic sign,
  and exhibits the non-PSD controls for getting either wrong (Part E).

## 8. Reprove-and-cite ledger

- **Reproven here** (runner, exact): the `Z_2` sign flip (`-\sinh beta` vs
  `+\sinh beta`); `I_n(beta) > 0` by the power series; the `Z_N` exact finite-Haar
  coefficient positivity and its Poisson identity with `I_m`; the `SU(2)` exact
  character coefficients and their nonnegative tensor-power-multiplicity
  reconstruction; the `SU(3)` irrep-coefficient nonnegativity and the
  `\chi_3\chi_3=\chi_6+\chi_{\bar3}` fusion exhibit; the ferromagnetic integrated
  Gram PSD and the manifest `G = W\,\mathrm{diag}(\kappa)\,W^\dagger`; the
  antiferromagnetic-sign and dropped-conjugation non-PSD teeth.
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
exact reprove surface is `Z_N`/`U(1)`/`SU(2)` (Gram) and the group-general Lemma
(coefficient positivity), with an `SU(3)` projection exhibit.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class
tag; only standard mathematics ("reflection positivity," "link reflection,"
"temporal gauge," "character," "Haar measure," "Peter–Weyl," "fusion
coefficients") and the repo-canonical "`A_+^{(2)}`," "gauge-half,"
"three-factor reduction." No fitted/observed/PDG/lattice-MC/`beta=6`/`g_bare`
value is consumed.

**No-promotion statement:** this note does **not** promote, demote, or set the
audit status of the failed bridge note, the target reflection-positivity row, or
any upstream row. The audit lane is the only status authority.
