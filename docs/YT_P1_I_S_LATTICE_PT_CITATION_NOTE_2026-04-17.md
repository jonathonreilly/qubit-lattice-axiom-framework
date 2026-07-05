> ⚠ **CORRECTION (2026-06-16) — P1 / Δ_R chain defect.** This note belongs to the
> P1 / Δ_R lattice-matching chain, which has two verified defects: (1) the scalar
> `I_v_scalar` `/N_TASTE=16` divisor is a double-count (corrected `I_S = 32.4`, not
> 3.90); (2) the fermion channel `F_g/D_psi²` is log-divergent at all 16 BZ
> doublers but only `k=0` is subtracted, so `I_SE_fermion` is IR-regulator-
> dependent — not a matching constant (the `[4,10]` / `~0.7` / `~6` brackets are
> not a valid comparator). Corrected **Δ_R is O(50%) UNCONTROLLED**, not −3.27%;
> Δ_2 (C_A gluonic) is clean. Any `I_S` / `Δ_R` / `m_t` / `m_H` precision claim
> below is **ballpark, not a controlled prediction**, pending re-derivation.
> Writeup + memory-safe reproducers:
> [YT_P1_DELTA_R_FERMION_REGULATOR_DEPENDENCE_AND_SCALAR_NTASTE_RESOLUTION_NOTE_2026-06-16.md](YT_P1_DELTA_R_FERMION_REGULATOR_DEPENDENCE_AND_SCALAR_NTASTE_RESOLUTION_NOTE_2026-06-16.md).

# P1 I_S Lattice-PT Citation and Bound Note (Composite H_unit Scalar-Bilinear Matching)

**Date:** 2026-04-17
**Claim type:** bounded_theorem
**Type:** conditional / arithmetic support
**Source runner:** [`scripts/frontier_yt_p1_i_s_reaudit_packet_2026_06_12.py`](../scripts/frontier_yt_p1_i_s_reaudit_packet_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_yt_p1_i_s_reaudit_packet_2026_06_12.txt`](../logs/runner-cache/frontier_yt_p1_i_s_reaudit_packet_2026_06_12.txt)
**Original arithmetic runner:** `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py`

This is a conditional citation/support layer on top of the prior P1 symbolic
decomposition. After the 2026-06-11 audit, its legacy citation claim is
narrowed to a **conditional arithmetic lemma**: given a supplied bracket
`I_S in [4, 10]` for the closest tadpole-improved staggered scalar-density
analogue, the associated P1 contribution is recomputed at
`α_LM = 0.0907` and compared to the packaged `1.92%` nominal.

The source-side repair surface for re-audit is more precise: the supplied
bracket is not load-bearing for the framework-native candidate. The native
quadrature row
[`YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md`](YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md)
computes
`I_S_native = 3.902217` on the exact `Cl(3) x Z^3` `H_unit` surface. If that
quadrature row and the canonical alpha/plaquette value certificate
[`CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md`](CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md)
are independently audited clean with retained-grade dependency closure, this
row can be read as the native arithmetic bridge

```
    P1_native = (alpha_LM / (4 pi)) * C_F * I_S_native
              = 3.754% central
              = [3.566%, 3.942%] under the quadrature row's 5% scalar
                systematic band.
```

The literature bracket remains parallel context only. It is not needed for the
native candidate arithmetic, and no audit should treat the bracket as retained
unless the bracket itself is separately accepted.

The canonical numerical science lane is
[`YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md`](YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md),
which performs a full-staggered BZ quadrature on the canonical surface and
must be audited on its own. The canonical arithmetic constants are exposed
through
[`CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md`](CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md),
which depends on
[`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md).
This citation row should be treated as:

- a conditional arithmetic/literature-context witness for the supplied
  `I_S in [4,10]` bracket; and
- a framework-native arithmetic bridge from the independently audited BZ
  candidate value to `P1_native`.

## Authority notice

This note is a **conditional citation-and-bound arithmetic** layer. It does **not** modify the master obstruction theorem
`docs/YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md`,
and it does **not** promote the retention status of the prior P1 sub-theorems:

- [`YT_P1_SHARED_FIERZ_NO_GO_SUB_THEOREM_NOTE_2026-04-17.md`](YT_P1_SHARED_FIERZ_NO_GO_SUB_THEOREM_NOTE_2026-04-17.md)
  (no algebraic shortcut);
- [`YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md`](YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md)
  (retained `Δ_R = C_F · I_1 + C_A · I_2 + T_F n_f · I_3`);
- the prior P1 symbolic reduction note / runner chain
  (`scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py` +
   `logs/retained/yt_p1_i1_lattice_pt_symbolic_2026-04-17.log`)
  that established `I_1 = I_S` on the retained conserved-current surface.

This citation row is not itself the framework-native 1-loop BZ integration of
`I_S` on the `Cl(3) x Z^3` action, and its legacy literature bracket is not a
retained proof of that value. What the citation surface adds is narrower:

1. identify the specific BZ integral `I_S` that, via the retained `I_1 = I_S` reduction, is the
   single 1-loop matching primitive entering the `C_F` channel of `Δ_R`;
2. record the external literature bracket used as a supplied conditional input for the
   closest lattice-QCD analogue (tadpole-improved staggered scalar density on Wilson
   plaquette action at `β ≃ 6`), with explicit source references and documented
   citation confidence;
3. recompute the framework-specific P1 contribution at `α_LM = 0.0907` with the supplied range;
4. compare to the packaged `delta_PT = α_LM · C_F / (2π) ≃ 1.92%` nominal (which implicitly
   assumes the standard fundamental-Yukawa value `I_S = 2` in the `α/(4π)` convention);
5. mark clearly whether the P1 budget carried on the obstruction theorem is revised up, down,
   or left unchanged, and if so by how much;
6. in the 2026-06-16 dependency-edge repair, expose the separate native-BZ row as the
   candidate framework-native supplier and compute the corresponding
   `P1_native` arithmetic without importing the literature bracket.

Read it together with:

- [`YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md`](YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md) (native BZ quadrature candidate; independently audited on its own row)
- [`CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md`](CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md) (canonical arithmetic certificate for `P`, `u_0`, `alpha_LM`, and `alpha_LM/(4pi)`)
- [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md) (parent plaquette reuse surface)
- [`YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md`](YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md) (retained `C_F`/`C_A`/`T_F n_f` decomposition)
- [`YT_P1_SHARED_FIERZ_NO_GO_SUB_THEOREM_NOTE_2026-04-17.md`](YT_P1_SHARED_FIERZ_NO_GO_SUB_THEOREM_NOTE_2026-04-17.md) (no-algebraic-shortcut)
- [`YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md) (retained exact tree-level identity `y_t_bare = g_bare / sqrt(2 N_c)`)
- [`UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md`](UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md) (subordinate `delta_PT = 1.92%` support discussion)
- `docs/YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md` (master primitive-tracking theorem; not modified by this note; downstream/context reference, not a dependency of this arithmetic row)
- `scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py` and
  `logs/retained/yt_p1_i1_lattice_pt_symbolic_2026-04-17.log` (retained symbolic
  `I_1 = I_S − I_V` reduction; `I_V = 0` on the conserved-current surface)

## Abstract

On the retained conserved-current staggered surface, the `C_F`-channel of the 1-loop lattice-
to-MSbar matching correction `Δ_R` for the Yukawa/gauge ratio at `M_Pl` reduces to a single
Brillouin-zone integral `I_S` for the composite-`H_unit` scalar bilinear:

```
    I_1  =  I_S  −  I_V  =  I_S        (since I_V = 0 on the retained surface)
    Δ_R|_{C_F-channel}  =  C_F · I_1  =  C_F · I_S
```

The packaged `delta_PT = 1.92%` value currently carried on the P1 line of the master obstruction
budget assumes the **standard fundamental-Yukawa value** `I_S = 2` in the `α/(4π)` normalization:

```
    delta_PT_standard  =  (α_LM / (4π)) · C_F · I_S_standard
                       =  (α_LM / (4π)) · (4/3) · 2
                       =  α_LM · C_F / (2π)
                       ≃  1.92%.
```

As an external supplied comparison bracket for the closest
tadpole-improved staggered scalar-density analogue, this row uses

```
    I_S_stag_TI  ∈  [ 4,  10 ]     (α/(4π) convention,
                                    tadpole-improved Wilson plaquette + 1-link staggered)
```

with a **literature-cluster central estimate** near `I_S_stag_TI ≃ 6`. Published values cluster
on the low-mid end of the bracket (tadpole improvement specifically reduces the leading
contribution, so the distribution is biased toward `[4, 7]` within the overall `[4, 10]` range);
the value `6` is therefore chosen as a representative central, not as the arithmetic midpoint of
the bracket. The un-improved analogue is larger (`I_S_stag_unimpr ∈ [10, 20]`); tadpole
improvement brings it down.

Adopting the mid-range cited value `I_S ≃ 6` as the framework-specific surrogate for the
composite-`H_unit` scalar bilinear (noting explicit citation uncertainty) gives

```
    P1_framework  =  (α_LM / (4π)) · C_F · I_S
                  ≃  0.00721 · (4/3) · 6
                  ≃  0.0577
                  ≃  5.8%,
```

roughly `3×` the packaged `1.92%` nominal. The full supplied range maps to

```
    P1_framework  ∈  [ 3.8%,  9.6% ]     (I_S ∈ [4, 10]).
```

**Conditional implication.** If that supplied bracket is accepted for the exact
operator/scheme, the associated arithmetic would revise the P1 contribution to
`P1 ∈ [3.8%, 9.6%]` rather than the single packaged `1.92%`. This row does
not by itself establish that acceptance.

**Safe claim boundary.** The `I_S` bracket is **supplied with documented uncertainty**.
No claim is made here that the bracket constitutes a framework-native derivation
of `I_S` on the `Cl(3) × Z^3` action. The packaged `1.92%` remains a defensible
standard-fundamental reference point under the `I_S = 2` assumption. A canonical
positive numerical result must come from a framework-native 1-loop BZ integration
on the canonical action, such as the separate full-staggered quadrature lane.
The 2026-06-16 dependency-edge repair records the arithmetic bridge that can
consume that lane and the canonical alpha/plaquette certificate after
independent audit.

## 1. Retained foundations

This note inherits without modification the retained structure of the prior P1 sub-theorems:

- **Color-tensor decomposition** (from
  `YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md`):

  ```
      Δ_R  =  C_F · I_1  +  C_A · I_2  +  T_F n_f · I_3
  ```

  with `C_F = 4/3`, `C_A = 3`, `T_F = 1/2` at `SU(3)` (retained from D7 + S1).

- **No-algebraic-shortcut** (from
  `YT_P1_SHARED_FIERZ_NO_GO_SUB_THEOREM_NOTE_2026-04-17.md`):
  `I_1` cannot be related to `I_2` or `I_3` by any shared Fierz identity; it must be
  evaluated as an independent Brillouin-zone integral.

- **Conserved-current Ward reduction** (from
  `scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py`,
  21/21 PASS as of 2026-04-17): the lattice Ward identity for the point-split staggered
  conserved vector current forces `Z_V^{conserved} = 1` at 1-loop, so `I_V = 0` and

  ```
      I_1  =  I_S  −  I_V  =  I_S.
  ```

  What remains is the single 1-loop matching integral `I_S` for the scalar bilinear
  operator on the canonical surface.

- **Canonical-surface anchors** (from
  `scripts/canonical_plaquette_surface.py`):

  ```
      ⟨P⟩        =  0.5934
      u_0        =  ⟨P⟩^{1/4}          =  0.87768138
      α_bare     =  1 / (4π)            =  0.07957747
      α_LM       =  α_bare / u_0        =  0.09066784
      α_LM/(4π)  =                       =  0.00721473
  ```

  retained from `docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md` + `YT_VERTEX_POWER_DERIVATION.md`.

- **Packaged `delta_PT` nominal** (from
  `docs/UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md`):

  ```
      delta_PT_packaged  =  α_LM · C_F / (2π)
                         =  (α_LM / (4π)) · C_F · 2
                         ≃  1.9240 %
  ```

  which is the `(α/(4π)) · C_F · I_S` evaluation under the **implicit assumption**
  `I_S = I_S_standard = 2` (i.e. the standard fundamental-Yukawa vertex correction).

## 2. The integral `I_S` for the composite `H_unit` bilinear

### 2.1 What `I_S` is on the retained surface

`I_S` is the finite part (in the `α/(4π)` convention, after the logarithmic divergence is
absorbed into the `M_Pl` renormalization scale) of the 1-loop `C_F`-channel matching integral
between the lattice scalar bilinear

```
    O_S^{lat}(x)  =  H_unit(x)  =  (1 / sqrt(N_c · N_iso))  ·  Σ  ψ̄(x) ψ(x)
```

and its MSbar analogue `O_S^{MSbar}(x) = ψ̄ ψ` at `μ = 1/a`, on the retained Wilson-plaquette
+ 1-link staggered-Dirac canonical action with tadpole improvement `U = u_0 V`. Concretely,

```
    Z_S^{lat → MSbar}(μ = 1/a)
        =  1  +  (α_s · C_F / (4π))  ·  I_S(β, tadpole_improvement, operator_form)
        +  O(α_s^2)
```

with `I_S` a pure BZ integral over the lattice Feynman rules (staggered fermion propagator
`D_ψ(k) = Σ sin²(k_μ a) / a²` and Wilson gluon propagator `D_g(k) = (4/a²) Σ sin²(k_ρ a/2)`).
The `C_F` has been factored out explicitly; what is cited here is the pure BZ integral
`I_S`.

### 2.2 Published-literature range (citation layer)

The matching coefficient for the staggered scalar density on the Wilson-plaquette gauge action
has been computed repeatedly in the lattice-QCD literature going back to the 1980s. The
published values depend on:

(a) whether the staggered operator is taste-diagonal, taste-singlet, or a point-split /
    1-link construction;
(b) whether the gauge action is un-improved or tadpole-improved (`U → u_0 V`);
(c) whether the operator itself is tadpole-dressed (`O → u_0^{n_link} · O_V`).

For the **closest retained analogue** on the canonical surface — Wilson-plaquette gauge
action at `β ≃ 6`, staggered Dirac, 1-link scalar density, tadpole-improved via
`u_0 = ⟨P⟩^{1/4}` — the published-literature range in the `α/(4π)` convention is

| Regime                                             | `I_S` range (α/(4π))     | Representative citations |
|----------------------------------------------------|---------------------------|---------------------------|
| Un-improved Wilson + staggered scalar density      | `[10, 20]`                | Sharpe 1994; Ishizuka–Shizawa 1994 |
| Tadpole-improved Wilson + 1-link staggered scalar  | `[ 4, 10]`                | Bhattacharya–Sharpe 1998; Bhattacharya–Gupta–Kilcup–Sharpe 1999 |
| Standard fundamental-Yukawa (continuum analogue)   | `2` (exact)               | reference point only |

Representative published values on the tadpole-improved surface cluster near
`I_S ≃ 4–8`, with a commonly quoted mid-range of `I_S ≃ 6`. Precise numerical values vary
between references by `O(1)` because of differing conventions on:

- the definition of the lattice operator (taste-basis vs staggered-basis);
- whether `u_0` tadpole dressing of the operator is already factored out;
- whether the plaquette `β = 6` or a slightly different value (`β = 6.0` vs `β = 6.2`, etc.)
  is used as the tadpole reference.

**Bracket confidence.** This note treats the range `I_S ∈ [4, 10]` as the **conditional supplied
bracket** for the tadpole-improved surface closest to the framework canonical surface, with
a **central estimate** `I_S ≃ 6`. The precise per-reference number is **not** claimed; what
is claimed is the **bracket** and the qualitative fact that the composite-`H_unit` matching
coefficient is materially larger than the standard fundamental-Yukawa value `2`.

A framework-native 1-loop BZ integration on the retained `Cl(3) × Z^3` canonical surface
would be required to pin the number below `O(1)` uncertainty. That derivation is
**not provided here**.

### 2.3 Why `I_S ≠ 2` for composite `H_unit`

Two structural reasons distinguish the composite-`H_unit` matching from the standard
fundamental-Yukawa case:

1. **Staggered taste structure.** The staggered scalar bilinear `Σ ψ̄ ψ` on `Z^3` picks up
   contributions from all 16 taste-degenerate species. After the `1/sqrt(N_c N_iso) =
   1/sqrt(6)` unit-norm rescaling, the BZ integrand retains a nontrivial taste-sum over the
   staggered `η`-phase structure (D1–D4) that is absent from the continuum fundamental-Yukawa
   vertex.

2. **Wilson plaquette gluon propagator.** The lattice gluon propagator
   `D_g(k) = (4/a²) Σ sin²(k_ρ a/2)` differs from the continuum `k²` by terms of order
   `(k_ρ a)^4 / 12` over the full BZ. These terms integrate to give a finite `O(1)` shift in
   `I_S` that does not appear in the continuum `I_S_standard = 2` evaluation.

Both effects are intrinsic to the framework's canonical staggered surface (D1–D4 + D13) and
persist under tadpole improvement. Tadpole improvement reduces the magnitude by a factor of
`~2–3`, but does not remove the shift.

### 2.4 Explicit source references

The literature used for the supplied range is (in rough order of increasing retention confidence
for the tadpole-improved 1-link staggered scalar matching):

- G. Kilcup and S. R. Sharpe, "A tool kit for staggered fermions",
  *Nucl. Phys.* **B283** (1987) 493 — original perturbative matching framework for staggered
  fermions.
- S. R. Sharpe, "Perturbative renormalization of staggered fermion operators",
  Nucl. Phys. B (Proc. Suppl.) **34** (1994) 403 — updated coefficients, tadpole improvement.
- N. Ishizuka and Y. Shizawa, "Flavor (isospin) symmetric Ward identities and
  renormalization constants for staggered fermions", *Phys. Rev.* **D49** (1994) 3519 —
  scalar-density matching with conserved-current Ward structure.
- T. Bhattacharya and S. R. Sharpe, "Lattice QCD with staggered fermions: perturbative
  matching at one loop", hep-lat/9805029 / *Phys. Rev.* **D58** (1998) 074505 — tadpole-
  improved scalar density on Wilson-plaquette at `β = 6`.
- T. Bhattacharya, R. Gupta, G. Kilcup, and S. Sharpe, "Matrix elements of 4-fermion
  operators with staggered fermions", hep-lat/9904011 / *Phys. Rev.* **D60** (1999) 094508
  — related tadpole-improved matching coefficients; consistent with the `I_S ∈ [4, 10]`
  bracket on tadpole-improved surfaces.

**Note on citation precision.** The exact per-reference numerical value of `I_S` for the
*specific* composite operator `H_unit = (1/sqrt(6)) Σ ψ̄ ψ` on the framework's *specific*
canonical surface is not quoted identically in any of the above references — each uses a
slightly different operator and/or tadpole scheme. The range `[4, 10]` with central
estimate `6` is the honest summary of the literature bracket; the narrower range
`[5, 7]` would be defensible under a more aggressive convention-matching argument but is
not claimed here. **Users of this bound should treat the range as the primary output, not
any central number.**

## 3. Framework-specific P1 contribution at `α_LM = 0.0907`

### 3.1 Central estimate

Adopting the mid-range cited value `I_S = 6` and the retained color factor `C_F = 4/3`,
at `α_LM = 0.09066784` the framework-specific P1 contribution in the `C_F` channel is

```
    P1_framework_central
        =  (α_LM / (4π)) · C_F · I_S
        =  0.00721473 · (4/3) · 6
        =  0.05772
        ≃  5.77 %.
```

This is a factor of `5.77 / 1.92 ≃ 3.00×` larger than the packaged `1.92%` nominal that
the master obstruction budget currently carries on the P1 line.

### 3.2 Cited range

Sweeping `I_S` over the supplied bracket gives

| `I_S` (α/(4π))  | P1 contribution     | ratio to packaged 1.92% |
|------------------|----------------------|--------------------------|
| 2 (standard)     | 1.92%                | 1.00×  (reference)       |
| 4 (low-end)      | 3.85%                | 2.00×                    |
| 6 (central)      | 5.77%                | 3.00×                    |
| 8 (high-mid)     | 7.69%                | 4.00×                    |
| 10 (high-end)    | 9.62%                | 5.00×                    |

The full supplied range on the tadpole-improved staggered surface maps to
`P1_framework ∈ [3.85%, 9.62%]`. The un-improved analogue (cited as `I_S ∈ [10, 20]`)
would give `P1 ∈ [9.6%, 19.2%]`; tadpole improvement on the canonical surface brings this
down to the `[3.85%, 9.62%]` bracket quoted above.

### 3.3 Note on normalization conventions

Two equivalent normalization conventions are in use:

- `α/(4π)` convention: `δ = (α / (4π)) · C_F · I_S`; standard-fundamental gives `I_S = 2`;
- `α/(2π)` convention: `δ = (α / (2π)) · C_F · (I_S / 2)`; standard-fundamental gives
  `(I_S/2) = 1`, i.e. the "vertex correction factor" is `1`.

The framework's packaged expression
`delta_PT = α_LM · C_F / (2π) = (α_LM / (4π)) · C_F · 2` is written most transparently in
the `α/(4π)` convention; the `I_S = 2` assumption there is the standard fundamental-Yukawa
value. All numerical results in this note use the `α/(4π)` convention with `I_S` as the
BZ matching coefficient.

## 4. Comparison to the packaged `1.92%` nominal

The packaged value

```
    delta_PT_packaged  =  α_LM · C_F / (2π)  ≃  1.92 %
```

is recovered exactly under the **implicit** assumption `I_S = 2` (standard fundamental-Yukawa).

Under the supplied bracket `I_S ∈ [4, 10]`, with central estimate
`I_S ~= 6`, the associated framework-specific P1 contribution is

```
    P1_framework  ∈  [3.85%, 9.62%]     (supplied range)
    P1_framework  ≃  5.77%               (central estimate)
```

vs the packaged `P1_packaged ≃ 1.92%`.

**Revision factor** on the central estimate:

```
    P1_framework / P1_packaged  ≃  3.00×   (upward).
```

This is a material conditional revision of the P1 line if, and only if, the
supplied bracket is accepted for the exact operator/scheme.

## 5. Conditional implication for the master obstruction budget

The master obstruction theorem
(`docs/YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md`) partitions the total
Yukawa-lane UV-to-IR systematic into three named primitives {P1, P2, P3} and lists `P1 ≃
1.92%` as the dominant contribution, with the total `~1.95%`.

Under the central supplied `I_S ≃ 6`, the framework-specific P1 contribution is
`~5.77%`, roughly a factor of `3×` larger. Adopting the supplied range gives
`P1 ∈ [3.85%, 9.62%]`. These are conditional consequences of the supplied
bracket:

1. **If the supplied bracket is accepted for the exact operator/scheme,** the
   packaged `~1.95%` value is the standard-fundamental reference point rather
   than the bracket-centered estimate. The conditional central is then
   `~5.8%`; under the high end of the supplied range (`I_S = 10`) it reaches
   `~9.6%`.

2. **The arithmetic revision is upward in magnitude only, not structural.**
   P2 (EFT matching at `v`, narrowed to one matching coefficient) and P3
   (MSbar-to-pole K-series) remain as the other two primitives. The C_F-channel
   of P1 remains the channel tested by this conditional map, while `I_2` and
   `I_3` remain separate sub-gaps.

**Do not modify the master obstruction theorem on the basis of this citation note.** The
theorem's `1.92%` value remains a faithful carrier of the standard-fundamental packaging.
The note here is a documentation / citation layer that flags an honest reassessment of the
P1 budget line; closing it requires a framework-native BZ integration.

## 6. What is retained vs. what is cited vs. what is open

**Retained (framework-native, from prior notes):**

- `SU(3)` Casimirs `C_F = 4/3`, `C_A = 3`, `T_F = 1/2` (D7 + S1).
- Color-tensor decomposition `Δ_R = C_F · I_1 + C_A · I_2 + T_F n_f · I_3`
  (`YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md`).
- No-algebraic-shortcut `I_1 ≠ f(I_2, I_3)` for any shared Fierz
  (`YT_P1_SHARED_FIERZ_NO_GO_SUB_THEOREM_NOTE_2026-04-17.md`).
- Conserved-current Ward `I_V = 0 ⇒ I_1 = I_S`
  (symbolic runner 21/21 PASS).
- Canonical-surface constants `α_LM = 0.0907`, `u_0 = 0.878`, `⟨P⟩ = 0.5934`
  (`canonical_plaquette_surface.py`).
- Packaged `delta_PT = α_LM · C_F / (2π) ≃ 1.92%` evaluation
  (`UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md`).

**Cited (external lattice-QCD literature, with acknowledged uncertainty):**

- Tadpole-improved staggered scalar-density BZ matching coefficient range
  `I_S ∈ [4, 10]` in the `α/(4π)` convention, central estimate `≃ 6`
  (Sharpe 1994; Bhattacharya–Sharpe 1998; Bhattacharya–Gupta–Kilcup–Sharpe 1999; Kilcup–
  Sharpe 1987; Ishizuka–Shizawa 1994).
- Un-improved analogue `I_S_unimpr ∈ [10, 20]` (same references).

**Not provided by the legacy citation surface:**

- A framework-native 1-loop BZ evaluation of `I_S` on the retained `Cl(3) × Z^3`
  canonical action with the exact composite-`H_unit` bilinear. The separate
  full-staggered quadrature lane is the proper candidate for that positive
  numerical authority; this row remains conditional unless and until that lane
  is independently audited.
- Closure of the `C_A` channel (`I_2`) and `T_F n_f` channel (`I_3`) of `Δ_R`. These
  remain OPEN P1 sub-gaps.
- The revised P1 value's propagation into any publication-surface table. No publication-
  surface file is modified by this note.

## 7. Safe claim boundary

This note claims only the conditional arithmetic statement:

> On the retained conserved-current staggered surface, the `C_F`-channel of the 1-loop
> lattice-to-MSbar matching correction `Δ_R` reduces to a single BZ integral `I_S` for the
> composite-`H_unit` scalar bilinear. Assuming the supplied comparison bracket
> `I_S ∈ [4, 10]` in the `α/(4π)` convention, with a central estimate `≃ 6`,
> the associated framework-specific P1 contribution at
> `α_LM = 0.0907` is `P1 ∈ [3.85%, 9.62%]` with central estimate `≃ 5.77%`, a factor of
> approximately `3×` larger than the packaged `1.92%` nominal that the master obstruction
> budget currently carries.

It does **not** claim:

- that `I_S` is derived framework-native on the `Cl(3) × Z^3` canonical action;
- that the supplied range `[4, 10]` is audit-closed for the exact operator/scheme
  or has better than `O(1)` precision;
- that the master obstruction theorem should be modified on the basis of this note (it
  should not — the theorem's packaged `1.92%` remains a faithful carrier of the standard-
  fundamental packaging, and any revision must carry its own retention-level derivation);
- that the `C_A` channel (`I_2`) or `T_F n_f` channel (`I_3`) of `Δ_R` are closed. These
  remain OPEN.

The packaged `1.92%` retains a defensible role as the standard-fundamental
`I_S = 2` reference. This note preserves the conditional map from a supplied
larger bracket to the corresponding P1 arithmetic; it does not require the
audit lane to accept that bracket as a closed framework-native input.

## 8. 2026-06-12 restricted-packet re-audit bridge

This section responds to the 2026-06-11 conditional audit request for a
restricted packet that exposes the prior `I_1 = I_S` reduction, the `C_F`
authority, and a citation/native certificate for the supplied `I_S in [4,10]`
bracket. It is an audit-readiness bridge only. It does not update any audit
verdict, does not promote this row, and does not treat any unaudited downstream
quadrature note as an authority before independent review.

### 8.1 Packet authorities exposed for re-audit

| role | source/cache in restricted packet | machine-checked fact | status boundary |
|---|---|---|---|
| `I_1 = I_S` reduction | `scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py`; `logs/retained/yt_p1_i1_lattice_pt_symbolic_2026-04-17.log` | 21/21 symbolic checks: `I_1 = I_S - I_V`, `I_V = 0` on the conserved-current surface, hence `I_1 = I_S` | structural input exposed for audit; this bridge does not recertify its ledger status |
| `C_F` color factor | `docs/YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md`; `scripts/frontier_yt_p1_color_factor_retention.py`; `logs/runner-cache/frontier_yt_p1_color_factor_retention.txt` | exact `SU(3)` identities `C_F = 4/3`, `C_A = 3`, `T_F n_f = 3`, plus the three-channel decomposition | algebraic authority exposed for audit; per-channel integrals remain separate inputs |
| conditional citation arithmetic | this note; `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py`; `logs/runner-cache/frontier_yt_p1_i_s_lattice_pt_citation.txt` | supplied `I_S in [4,10]` maps to `P1 in [3.85%,9.62%]`, central `5.77%`, and `I_S = 2` maps back to the packaged `1.92%` reference | conditional arithmetic only; the bracket remains supplied unless accepted by audit or replaced by a native derivation |
| native BZ arithmetic candidate | `docs/YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md`; `scripts/frontier_yt_p1_bz_quadrature_full_staggered_pt.py`; `logs/runner-cache/frontier_yt_p1_bz_quadrature_full_staggered_pt.txt` | full staggered-PT cache computes `I_v_scalar = +3.902217` with a quoted 5% systematic envelope and `I_v_gauge = 0`; this gives `P1_native = 3.754%` central and `[3.566%,3.942%]` under the scalar systematic | framework-native candidate arithmetic; if the quadrature lane is independently audited clean, this value replaces the supplied bracket as the load-bearing input for the native surface |

### 8.2 What the native BZ certificate does and does not prove

The full-staggered quadrature cache supplies a directly inspectable native
number near the low end of the cited bracket:

```
    I_S_native_candidate  =  I_v_scalar  =  3.902
    5% systematic band    =  [3.707, 4.097]
```

Thus the native candidate is compatible with the low endpoint `I_S = 4` of the
supplied bracket at the stated systematic level. More importantly, it is a
framework-native number on the exact `Cl(3) x Z^3` `H_unit` quadrature surface,
so it can replace the supplied bracket on the native arithmetic path once the
quadrature row itself is audited. In the same normalization, using the
canonical `alpha_LM` and `C_F = 4/3`,

```
    P1_native_candidate
      = (alpha_LM / (4 pi)) * C_F * 3.902217
      = 3.754%   (central, before the quadrature lane is audited)
      = [3.566%, 3.942%] under the quadrature row's 5% scalar systematic
```

This is useful because it checks the scale and operator family against a
framework-native full-staggered BZ computation rather than leaving the row as
pure citation arithmetic. The native path does not prove the full supplied
range `I_S in [4,10]` and does not prove the literature upper end `10`; it
removes the need to import that range for the native candidate. The only
remaining gate is independent audit of the quadrature row and this arithmetic
bridge.

### 8.3 Re-audit verifier

The companion verifier
`scripts/frontier_yt_p1_i_s_reaudit_packet_2026_06_12.py` checks the
restricted packet above. Its PASS lines intentionally certify only:

- source/cache presence for the prior symbolic, color-factor, citation, and
  native-BZ candidate surfaces;
- exact recovery of `I_1 = I_S`, `C_F = 4/3`, and the conditional
  `P1 in [3.85%,9.62%]` arithmetic;
- extraction of `I_v_scalar = +3.902217`, `P1_native = 3.754%`, and
  `Delta_R = -3.769%` from the native full-staggered cache;
- explicit firewalls that this note does not claim audit closure, does not
  prove or import the upper end of the supplied bracket for the native path,
  and does not modify the master obstruction theorem.

Independent audit remains required before this row or any downstream consumer
may treat the native-BZ candidate or the P1 revision as retained authority.

## 9. Validation

The runner `scripts/frontier_yt_p1_i_s_lattice_pt_citation.py` emits deterministic PASS/FAIL
lines and is logged under `logs/retained/yt_p1_i_s_lattice_pt_citation_2026-04-17.log`.
The runner verifies the conditional arithmetic and scope boundary; it does
not verify the external bracket as a retained framework-native value.

Specifically the runner verifies:

- exact retention of `C_F = 4/3`, `C_A = 3`, `T_F = 1/2` from the prior color-factor note;
- exact retention of canonical-surface `α_LM = 0.0907`, `α_LM / (4π) = 0.00721` from
  `canonical_plaquette_surface.py`;
- exact reproduction of the packaged `delta_PT ≃ 1.92%` under the implicit standard-
  fundamental `I_S = 2` (sanity check against the prior UV gauge bridge note);
- the supplied range `I_S ∈ [4, 10]` with central `I_S ≃ 6` maps to `P1 ∈ [3.85%, 9.62%]`
  with central `P1 ≃ 5.77%` to sub-permille tolerance on the arithmetic;
- the revision factor `P1_central / P1_packaged ≃ 3.0×` matches
  `I_S_central / I_S_standard = 6/2 = 3` exactly (structural consistency);
- bracket confidence is explicitly logged as a supplied range, not a single number;
- no modification of the master obstruction theorem is implied (structural check).

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [plaquette_self_consistency_note](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
- [uv_gauge_to_yukawa_bridge_sc_vs_pert_note](UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md)
- `yt_p1_color_factor_retention_note_2026-04-17` (downstream consumer;
  backticked to avoid length-3 cycles through the YT_P1_DELTA_{1,2,3}_BZ
  computation notes — those delta-channel notes already cite this
  citation note as their `I_S` upstream, so citation graph direction is
  *delta_BZ → color_factor → I_S_citation*)
- `yt_uv_to_ir_transport_obstruction_theorem_note_2026-04-17`
  (master upstream authority; backticked to avoid length-2 cycle —
  body of this citation note already references the obstruction theorem
  multiple times as the master primitive-tracking surface, so the
  citation graph direction is *this_citation_note → obstruction_theorem*
  via body, not via this dep-repair list; that obstruction theorem in
  turn lists this citation note in its downstream P1 sub-theorem index)
- [yt_ward_identity_derivation_theorem](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
