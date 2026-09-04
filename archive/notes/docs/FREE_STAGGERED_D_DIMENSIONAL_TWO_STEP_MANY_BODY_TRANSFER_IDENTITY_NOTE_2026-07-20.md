---
claim_id: free_staggered_d_dimensional_two_step_many_body_transfer_identity_note_2026-07-20
claim_type: bounded_theorem
claim_scope: "Free U = 1 staggered surface only, in the d-dimensional dispersion note's own conventions (one Grassmann component per site, d spatial axes, even spatial periods, real m > 0, canonical staggered phases). TWO SEPARATE GRADES, stated in order. (A) DERIVED HERE, unconditionally on the stated surface: the d-dimensional CLASSICAL two-step transfer algebra. (T1) The per-reduced-momentum classical two-step block T_2(k) (dimension 2^{d+1}) is an explicit matrix function of the Hermitian taste-corner matrix S(k) = sum_mu sin(k_mu) Gamma_mu whose square is the SCALAR (sum_mu sin^2 p_mu) I (the dispersion note's 'only dimension-dependent algebraic step'), so it collapses to 2x2 blocks identical to the one-axis recursion with sin^2 p -> sum_mu sin^2 p_mu; det T_2 = 1, tr T_2 = 2^d (2 + 4R), and the separable minimal polynomial T_2^2 - (2 + 4R) T_2 + I = 0 with distinct roots for m > 0 gives diagonalizability, so trace pins the spectrum {e^{+2E_d}, e^{-2E_d}} each of multiplicity 2^d (taste-degenerate), E_d = arcsinh(sqrt(m^2 + sum sin^2 p_mu)). (T2a) For m > 0 the reciprocal pair splits strictly, lambda_- = e^{-2E_d} in (0,1) and lambda_+ = e^{+2E_d} > 1 (REDERIVED here since the dispersion note states no (0,1] interval), and the per-mode Riesz projectors are well-defined and satisfy the projector and eigen-relations. (T2b) The general-period mode count prod_mu (L_mu/2) * 2^d = prod_mu L_mu for even periods L_mu (hypercubic instance (L/2)^d 2^d = L^d; taste corners are spatial-fold bookkeeping, scalar fiber, not extra species). This grade-(A) content is the d-dimensional analogue of the classical monodromy-spectrum-and-projector content of the cited 1+1d construction, and the corner coupling for d >= 2 is genuinely new structure. (B) CONDITIONAL ONLY, on two explicitly supplied inputs and NOT derived here or in any cited source: (T3) the forward-channel SELECTION PRESCRIPTION (supplied: on finite time extent both reciprocal solutions are finite, so no norm on Grassmann histories performs the selection by itself; the prescription declares the forward kernel to be the decaying channel), and (T4) the one-mode exponential coherent-state KERNEL FORM (supplied: the cited 1+1d sentence is itself conditional, 'For a one-mode coherent-state kernel <zbar'|T_2|z> = exp(zbar' lambda_- z)...'). GIVEN both, the kernel exp(zbar' lambda z) induces exactly diag(1, lambda) with vacuum element exp(0) = 1, so a scalar prefactor C != 1 is excluded RELATIVE TO THAT FORM (C = 1 is fixed by the supplied normalized form, NOT derived from the action), the selected one-particle kernel is diagonal so the many-body kernel factorizes over modes, and the landed finite-mode functor theorem then gives, at a_tau = 1 (all displays; no general-a_tau display is claimed): T_hat^2_d = Gamma(t1(2)_d) = tensor_p diag(1, e^{-2E_d(p)}) = B^dag B with B = tensor_p diag(1, e^{-E_d(p)}), H_hat_d = -(1/2) log(T_hat^2_d) = dGamma(E_d) >= 0, and Tr T_hat^2_d = det(1 + t1(2)_d) = prod_p (1 + e^{-2E_d(p)}). CENTRAL NON-CLAIM: this note does NOT supply or discharge the ACTION-TO-FOCK OPERATOR IDENTIFICATION that the landed corner-note names as an unsupplied prerequisite. Specifying the one-mode coherent kernel as exp(zbar' lambda z) IS the coherent-state form of the identification T = diag(1, lambda), so grade (B) RELOCATES that conditional from d = 1 to general d rather than closing it; the two-slice Grassmann/Berezin derivation of the kernel, its residue and normalization, the CAR metric, and the reflected inner product are performed nowhere in this chain, so every grade-(B) display is a statement about the CONSTRUCTED matrix Gamma(diag(e^{-2E_d(p)})) and not about a transfer operator derived from the action. a_tau = 1 is the working convention (the corner note's -1/2 log form); no physical time is selected. ALSO NOT claimed: fixed-gauge-background or U-integrated identification (the corner note names both open; this is the free specialization); interacting/non-quadratic transfers; any locality, kernel-envelope, or Lieb-Robinson content (the dispersion note's C_d/h(z) locality surface is NOT an input here); single-step positivity (fails already at d = 1); species/occupancy interpretation of the taste corners; sharpness; audit verdicts; nothing physical is selected."
upstream_dependencies:
  - minimal_axioms
  - free_staggered_two_step_dispersion_d_dimensional_narrow_theorem_note_2026-06-12
  - axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28
  - microcausality_corner_class_factorization_discharge_bounded_theorem_note_2026-07-18
runner: scripts/free_staggered_d_dimensional_two_step_many_body_transfer_2026_07_20.py
---

# Free Staggered d-Dimensional Two-Step Many-Body Transfer Identity

**Date:** 2026-07-20
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** free `U = 1` staggered surface, general spatial dimension
`d`, even periods, `m > 0`; the axioms supply no dynamics.
**Audit-status authority:** independent audit lane only. This note
sets no audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited,
or enlarged here.
**Primary runner:**
[`scripts/free_staggered_d_dimensional_two_step_many_body_transfer_2026_07_20.py`](../scripts/free_staggered_d_dimensional_two_step_many_body_transfer_2026_07_20.py)
**Runner cache:**
[`logs/runner-cache/free_staggered_d_dimensional_two_step_many_body_transfer_2026_07_20.txt`](../logs/runner-cache/free_staggered_d_dimensional_two_step_many_body_transfer_2026_07_20.txt)

## Purpose

Three landed notes bound this note's target. The corner-note
[`MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md)
proves the finite-mode second-quantization theorem but "does not
infer a many-body transfer operator from a one-particle kernel", and
names the operator identification as an unsupplied prerequisite for
any locality feed. The RP-positivity note
[`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
assembles the many-body two-step identity at `1+1d` only, and it
does so on the same supplied coherent-kernel form — its own
one-mode sentence is explicitly conditional. The dispersion note
[`FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md)
derives the d-dimensional classical two-step structure but is
one-particle-only by its own boundary: it states no `(0,1]`
interval, builds no projectors, no coherent kernel, no `Γ`, no
`B†B` (its runner builds none of them; the channel selection is
deferred "as in the one-axis construction").

This note therefore ships **two grades, kept separate throughout**.
Grade (A), derived here: the d-dimensional **classical** two-step
transfer algebra — the block form, the scalar Clifford square, the
2×2 collapse, `det`/`tr`, the spectrum and its `2^d` multiplicities,
the strict reciprocal split, the Riesz projectors, and the
general-period mode count. The corner coupling at `d ≥ 2` is
genuinely new structure and the scalar square is what tames it.
Grade (B), conditional only: the passage from that classical
algebra to a Fock-space operator, which rests on two explicitly
supplied inputs — the stable-half-line selection prescription and
the one-mode exponential coherent-kernel form. Relative to the
supplied form the normalization is `C = 1`; the form itself is not
derived from the action here or at `d = 1`.

**What this note does not do.** It does not discharge the
corner-note's operator-identification prerequisite. Specifying the
one-mode coherent kernel as `exp(z̄'λz)` *is* the coherent-state
form of the identification `T = diag(1, λ)`, so grade (B) carries
that conditional from `d = 1` to general `d` rather than closing
it. The named open obligation, unchanged by this note, is the
two-slice Grassmann/Berezin derivation of the kernel — its residue
and normalization, the CAR metric, and the reflected inner product
— from the stated action.

## Hypotheses (all supplied, none derived here)

(i) The dispersion note's surface and conventions, verbatim: free
`U = 1`, one Grassmann component per site, `d` spatial axes, even
spatial periods, real `m > 0`; phases `η_0 = 1`,
`η_μ(t,x) = (−1)^{t + x_1 + … + x_{μ−1}}`; the mode equation
`ψ_{t+1} = −2(mI + (−1)^t H_hop)ψ_t + ψ_{t−1}`; the fold to reduced
momenta `k ∈ (−π/2, π/2]^d` with taste corners `r ∈ {0,1}^d`
(`p_r = k + πr`); the corner operators
`Γ_μ|r⟩ = (−1)^{r_μ}|r xor s_μ⟩` with `Γ_μ² = I`, anticommuting,
and `H_hop(k)² = −(Σ_μ sin² k_μ)I` — its "only dimension-dependent
algebraic step" (all needled; the corner algebra REBUILT and gated
natively). "Taste corner" in this note always means the dispersion
note's `r` — never the corner-note's generation channels. (ii) The
RP note's Step-3b/4 structure as the `1+1d` template (projector
display, finite-norm selection sentence, one-mode coherent kernel,
defining intertwiner — needled; every d-dim instance re-derived and
gated natively). (iii) The landed corner-note's finite-mode theorem:
canonical intertwiner (vacuum-fixing), positive logarithm, trace
identity, direct sums — and its pin statement (trace + positivity +
multiplicativity do not identify the functor; the intertwiner does),
whose counterexample is rebuilt here as a discrimination gate.
(iv) `a_τ` carried explicitly, `a_τ = 1` as the convention
reconciling the sources (the RP note's `−log/(2a_τ)` equals the
corner-note's `−(1/2)log` at `a_τ = 1`); no physical time selected.
Workhorse disclosure: two Opus 4.8 max workers executed bounded
pieces (source extraction; derivation drafting) under supervisor
ground truth recorded first in the loop pack; every load-bearing
fact below is gated natively by the runner.

## Results

**The per-k classical block (action side).** Substituting
`H_hop(k) = iS(k)`, `S(k) := Σ_μ sin(k_μ)Γ_μ` Hermitian, into the
dispersion note's single-step matrices and multiplying blocks:

> `T_2(k) = [[ (4m² + 1)I + 4S(k)² , −2(mI − iS(k)) ],`
> `          [ −2(mI + iS(k)) ,              I      ]]`,

a `2^{d+1}`-dimensional matrix function of `S(k)`. The Clifford
relations give the **scalar** square
`S(k)² = (Σ_μ sin² k_μ)I = (Σ_μ sin² p_μ)I` — all `2^d` diagonal
entries equal, which is stronger than diagonality and is the entire
collapse mechanism: on each `S(k)`-eigenline (`S(k)w = σw`,
`σ = ±λ`, `λ² = Σ sin² k_μ`; the two signs occur with multiplicity
`2^{d−1}` each because every `Γ_μ` is traceless — for `d ≥ 2`,
`Γ_μ = −Γ_ν Γ_μ Γ_ν` for any `ν ≠ μ` and the trace is cyclic — but
nothing below depends on that split)
the block restricts to exactly the one-axis two-step matrix with
`sin p → σ` (for `λ > 0`; at `λ = 0` the two sign-eigenspaces merge
into the full `2^d` corner space with `σ = 0`, and the same 2×2
conclusion holds there):

> `T_2(σ) = [[4|a|² + 1, −2ā],[−2a, 1]]`, `a = m + iσ`,
> `det = 1`, `tr = 2 + 4R`, `R = m² + σ²`,
> `spec = {e^{+2E_d}, e^{−2E_d}}`,
> `E_d = arcsinh(√R) = arcsinh(sqrt(m² + Σ_μ sin² p_μ))`.

Since `R` depends on `σ` only through `σ² = λ²`, and
`sin²(k_μ + πr_μ) = sin² k_μ`, all `2^d` corner-eigenmodes at fixed
`k` share one `E_d`. The multiplicity conclusion does **not** rest
on the `±λ` sign split above: the full `2^{d+1}`-dimensional block
satisfies the separable quadratic `T_2² − (2+4R)T_2 + I = 0`, whose
roots are distinct for `m > 0`, so `T_2` is diagonalizable with
spectrum in `{e^{+2E_d}, e^{−2E_d}}`; the full-block trace
`tr T_2 = 2^d(2 + 4R) = 2^d(λ_+ + λ_−)` then forces the full block
spectrum to be `e^{+2E_d}` and `e^{−2E_d}`, **each with
multiplicity `2^d`**. (This minimal-polynomial + trace route is what
the runner gates, and it needs neither `tr S = 0` nor a symbolic
eigendecomposition.) For `d ≥ 2` the corners genuinely couple
(`Γ_μ` is off-diagonal for `μ ≥ 2`); at `d = 1` they never do — the
coupling is the new feature, and the scalar square is what tames it.

**Forward-channel selection at general d.** For `m > 0`,
`E_d(p) ≥ arcsinh(m) > 0`, so the reciprocal pair splits strictly:
`λ_−(p) = e^{−2E_d(p)} ∈ (0,1)` and `λ_+(p) = e^{+2E_d(p)} > 1`
(rederived here — the dispersion note states no interval; gated via
`R(1+R) − R² = R > 0`). The per-mode Riesz projectors

> `P_∓(k,α) = (T_2(σ_α) − λ_± I)/(λ_∓ − λ_±)`

are well-defined (denominators nonzero) and satisfy the projector
identities and eigen-relations (gated symbolically). The selection
is the RP note's **stable-half-line prescription, supplied and
inherited as such**: on a finite time extent both reciprocal
solutions are finite, and no norm on Grassmann histories performs
the selection by itself — the prescription (the landed note's "a
forward solution with any `P_+` component grows like `λ_+^N` over
`N` two-step blocks, so finite-action/finite-norm positive-time
propagation sets that coefficient to zero") declares the forward
kernel to be the decaying channel, exactly as at `d = 1`. The
prescription's sentence is **dimension-blind**; what is d-dependent
is only the **furnishing** of the 2×2 blocks it acts on — the
Clifford step above. Collecting survivors over all modes:

> `t1⁽²⁾_d = diag over full momenta p of e^{−2E_d(p)}`,
> `L^d` entries.

**The coherent-state → exterior bridge, with C = 1 pinned relative
to the supplied kernel form.** The RP note's one-mode sentence is
conditional — "For a one-mode coherent-state kernel
`<z̄'|T_2|z> = exp(z̄' λ_− z)`…" — and this note inherits exactly
that conditional: **the exponential kernel form is a supplied
input, not derived from the action, at every `d` including the
landed `d = 1`**. Given the form: a number-conserving one-mode
operator `T = T_0(1−n) + T_1 n` has coherent kernel
`T_0 + T_1 z̄'z`; matching to `exp(z̄'λz) = 1 + λz̄'z` (the series
truncates) forces `T_0 = 1, T_1 = λ` — the induced operator is
**exactly** `diag(1, λ)` with vacuum element `exp(0) = 1`, and a
scalar prefactor `C ≠ 1` has constant term `C ≠ 1`, so the Gaussian
scalar is excluded **relative to the form**. The selected
one-particle kernel is diagonal in the `S(k)`-eigenmode basis, so
the many-body coherent kernel has no cross terms and factorizes
over modes; the vacuum→vacuum amplitude is `Π 1 = 1`. This matches
the corner-note's canonical-intertwiner vacuum-fixing — the pin
that trace, positivity, and multiplicativity do **not** supply (its
`W`-conjugate counterexample is rebuilt here as a gate on a
non-degenerate kernel, where it genuinely discriminates; on fully
degenerate instances it cannot, and the runner says so honestly).
Note the logical direction: this paragraph *computes the operator
determined by a supplied kernel form*. It does not derive that form,
so it does not derive the operator identification either — see the
boundary statement after the assembly below.

**Conditional assembly (grade B).** On the stated surface, at
`a_τ = 1` (all displays; the RP note's `a_τ`-carrying glyphs
reconcile with the corner-note's `−(1/2)log` form exactly at
`a_τ = 1`, and no general-`a_τ` display is claimed), **given the
two supplied inputs above** (the stable-half-line selection
prescription and the one-mode exponential kernel form):

> `T̂²_d = Γ(t1⁽²⁾_d) = ⊗_p diag(1, e^{−2E_d(p)}) = B†B`,
> `B = ⊗_p diag(1, e^{−E_d(p)})`,
>
> `Ĥ_d = −(1/2) log(T̂²_d) = dΓ(E_d) ≥ 0`,
>
> `Tr T̂²_d = det(1 + t1⁽²⁾_d) = Π_p (1 + e^{−2E_d(p)})`,
>
> mode count `Π_μ (L_μ/2) · 2^d = Π_μ L_μ` for even periods
> `L_μ` (hypercubic instance `(L/2)^d · 2^d = L^d`),

by the landed finite-mode theorem (direct sums for the tensor
factorization; positive logarithm for `Ĥ_d`; trace identity; the
canonical intertwiner
`Γ(t1⁽²⁾_d)a_p† = e^{−2E_d(p)} a_p† Γ(t1⁽²⁾_d)` displayed and
gated), with `C = 1` fixed by the supplied normalized kernel form.

**What this assembly is and is not.** It is the d-dimensional
two-step reflection-positivity statement *for the constructed
matrix* `Γ(diag(e^{−2E_d(p)}))`. It is **not** a discharge of the
corner-note's action-to-Fock operator identification, and this note
does not claim one. The reason is structural, not rhetorical:
specifying the one-mode coherent kernel as `exp(z̄'λz)` *is* the
coherent-state form of the identification `T = diag(1, λ)`, so
supplying that form mode-by-mode, together with factorization,
supplies the identification rather than deriving it. What this note
establishes is that the *classical* d-dimensional algebra (grade A)
exists and has the stated spectrum, projectors, and mode count, and
that **given** the same two supplied inputs the landed `1+1d`
assembly goes through verbatim at general `d` — **parity with the
landed `d = 1` case**, not a stronger from-scratch construction and
not a closure. The named open obligation, unchanged at every `d`
including `d = 1`, is the two-slice Grassmann/Berezin derivation of
the kernel — residue, normalization, CAR metric, and reflected
inner product — from the stated action; until that exists, no
sentence here licenses treating `T̂²_d` as an action-derived
transfer operator. The taste corners are spatial-fold bookkeeping (one
Grassmann component per site; scalar fiber; `2^d`-fold degeneracy
per reduced momentum is the standard staggered doubling); no
species or occupancy interpretation is claimed.

## No-Go Discipline Gate

- **N1 route inventory — ATTEMPTED.** (1) "cite the 1+1d identity
  and assert the d-dim case is analogous" — REJECTED: the repo
  discipline requires the algebra rebuilt, and the d-dim corner
  coupling (`d ≥ 2`) is genuinely new structure; (2) "derive via
  trace/determinant matching" — REJECTED by the landed pin
  (trace + positivity + multiplicativity do not identify the
  functor; the counterexample is a gate here); (3) "treat the
  taste corners as a fiber and reuse the matrix-fiber machinery" —
  REJECTED: in position space the surface has one Grassmann
  component per site (scalar fiber); corners are momentum
  bookkeeping; (4) "claim the gauged case too" — REJECTED: the
  corner-note names fixed-background identification open; this is
  the free specialization, stated; (5) executed route: rebuild the
  RP note's Steps 3b–4 at general `d` on the dispersion note's
  surface.
- **N2 hypothesis independence (pairwise) — ATTEMPTED.** `m > 0`
  enters the strict channel split and the positive logarithm only;
  even periods enter the fold/mode-count only; the phase convention
  enters the Clifford step only; `a_τ` enters the generator
  normalization only (convention, fixed to 1 in all displays); the
  intertwiner pin enters uniqueness only; the supplied kernel form
  enters the bridge only. (The mutation battery referenced here is
  the loop-pack's supervisor-run probe set — scratchpad copies of
  the runner, one assertion flipped each — not an in-runner
  hypothesis sweep; the runner itself contains no odd-period,
  `m = 0`, or phase-flip executions, which are excluded by the
  stated hypotheses.)
- **N3 hidden-wall scan — ATTEMPTED.** Surfaced and stated: **the
  supplied-kernel-form wall** (the exponential coherent kernel is a
  conditional input at every `d`, including the landed `d = 1` —
  review-found in this note's first draft, which had claimed it
  came from the action; `C = 1` is pinned relative to the form
  only); **the selection-prescription wall** (finite time extent
  gives both reciprocal solutions finite norm; the stable-half-line
  prescription is supplied, same as at `d = 1`); the
  degenerate-gate insufficiency (fully degenerate Fock instances
  cannot discriminate the canonical pin — the `W`-conjugate
  coincides there; hence the non-degenerate Gate G9); the
  diagonal-kernel intertwiner is sign-convention-blind (both sides
  carry the same JW sign; the separate CAR gate verifies that the
  runner's chosen Jordan-Wigner matrices satisfy the CAR — it does
  **not** derive or pin the physical fermionic structure of the
  staggered action, which is part of the named open Berezin/CAR
  obligation); the coherent-state
  sign convention (routed through the `n`/`1−n` kernels,
  sign-unambiguous; inert since `λ > 0`); `m = 0` degeneracy and
  the `λ = 0` sign-eigenspace merge (stated; conclusions
  unaffected); odd periods break the fold (excluded); the
  `2^{d+1}` block dimension and multiplicities are this note's
  assembly (gate-verified, not quoted from the dispersion note).
- **N4 dependency roles, per citation — ATTEMPTED.**
  - [`FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md):
    the d-dim action surface, phases, fold, Clifford step, and
    dispersion (all needled; corner algebra rebuilt natively);
    its locality content (`C_d`, `h(z)`, rates) is NOT an input.
  - [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md):
    the `1+1d` template being extended (Steps 3b–4 needled; its
    `1+1d`-only scope sentence needled); unmodified.
  - [`MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    the finite-mode functor theorem consumed (intertwiner, positive
    log, trace, direct sums — needled); its pin counterexample
    rebuilt as Gate G9; the "does not infer" and
    operator-identification-open sentences needled — **that
    prerequisite is NOT discharged here**; this note carries it to
    general `d` in the same conditional form.
  - [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):
    no-dynamics boundary needle only.
  - Loop-pack worker reports: disclosed scaffolding, graded against
    pre-recorded ground truth; not executed by the runner.
- **N5 rhetoric audit — ATTEMPTED.** The word "action-level" has
  been REMOVED from this note's live claim language: a second review
  round judged that its ordinary meaning is exactly what the note
  does not establish, so no definitional gloss can rescue it. Three
  earlier over-claims are retracted in place and named here so the
  retraction is auditable: "C = 1 derived rather than conventional"
  and "kernel form supplied by the quadratic action" (first draft),
  and "supplies the operator identification the corner-note names as
  an unsupplied prerequisite" (second draft, caught in the second
  review round). The corrected statements are "C = 1 fixed by the
  supplied normalized kernel form" and "grade (B) relocates the
  identification conditional to general `d` rather than closing it".
  Nothing is called sharp; the corner-coupling novelty is stated
  without superlatives.
- **N6 partial-closure scan — ATTEMPTED.** Derived here: the free
  `U = 1` d-dimensional CLASSICAL two-step algebra (block form,
  spectrum with `2^d` multiplicities, strict split, projectors,
  mode count). Conditional only: the Fock assembly, given the two
  supplied inputs. Still open, named: the action-to-Fock operator
  identification itself (the two-slice Grassmann/Berezin kernel,
  its residue and normalization, the CAR metric, the reflected
  inner product) at every `d` including `d = 1`;
  fixed-gauge-background identification (`Γ(t[U])`), `U`-integrated
  measure, interacting transfers, locality feeds, sharp anisotropic
  rates.
- **N7 steelman (strongest counterarguments) — ATTEMPTED, and one
  of them is CONCEDED as unclosed.** (a) "The forward-channel
  selection is a prescription, not a theorem." CORRECT and stated
  as such throughout. (b) "`C = 1` is conditional because the
  coherent kernel form is itself supplied." CORRECT and adopted.
  (b′) **"Supplying that kernel form IS the operator identification,
  so the note relocates the conditional rather than discharging
  it." CORRECT and CONCEDED — this objection is not answered, it is
  adopted as the note's boundary.** The claim was demoted
  accordingly: grade (A) derived, grade (B) conditional, prerequisite
  explicitly NOT discharged. (c) "Degenerate gates prove nothing
  about the pin." Correct, and stated: Gate G9 runs the
  discrimination on a non-degenerate kernel. (d) "At `L = 2` the hop
  vanishes and the instances are trivial." True, and the gate labels
  now say so: the `L = 2` gates are support-only exterior-algebra
  bookkeeping and carry no `d`-dimensional content; the
  corner-coupling content is gated only at `L = 4` (position-space
  faithfulness) and symbolically at `k = (π/2, π/2)`. (e) "The taste
  corners might secretly be a matrix fiber." In position space
  there is one Grassmann component per site; the corners arise
  from the momentum fold; the mode count closes exactly.
- **N8 prior-wall echo — ATTEMPTED.** The corner-note's refusal to
  infer many-body from one-particle is respected by NOT claiming to
  have overcome it: grade (A) is classical and does not touch it,
  and grade (B) is explicitly conditional on the supplied kernel
  form, which is the same refusal restated at general `d`. The
  single-step non-positivity (landed at `1+1d`) is not contradicted
  (nothing single-step is claimed); the dispersion note's
  one-particle boundary is respected (its content is consumed as
  one-particle input); no landed no-go concerns the free two-step
  surface.

**Status: no closure is claimed and no `PASS` is asserted.** The
eight items are answered as an honesty exercise, not as a
certificate: item N7(b′) is a conceded, unclosed objection, and the
action-to-Fock operator identification remains an open obligation at
every `d`. What survives is grade (A) — the classical d-dimensional
transfer algebra — plus the conditional grade-(B) assembly.

## Non-Claims

- Does **not** claim a fixed-gauge-background identification
  (`Γ(t[U])`) or the `U`-integrated measure statement (both named
  open by the corner-note; this is the free specialization).
- Does **not** claim any locality, kernel-envelope, or
  Lieb-Robinson content (the dispersion note's locality surface is
  not an input; feeds built on this identification are other
  notes' content).
- Does **not** claim the one-mode exponential kernel form or the
  stable-half-line selection are action-derived (both are supplied
  inputs, at every `d` including the landed `d = 1`; `C = 1` is
  fixed by the supplied normalized form).
- Does **not** supply or discharge the corner-note's action-to-Fock
  **operator identification**. Specifying the one-mode coherent
  kernel as `exp(z̄'λz)` is the coherent-state form of that very
  identification, so grade (B) relocates the conditional from
  `d = 1` to general `d`. The two-slice Grassmann/Berezin derivation
  of the kernel — residue, normalization, CAR metric, reflected
  inner product — is performed nowhere in this chain and remains the
  named open obligation.
- Does **not** claim any grade-(B) display is a statement about an
  action-derived transfer operator; they are statements about the
  constructed matrix `Γ(diag(e^{−2E_d(p)}))`.
- Does **not** claim single-step positivity (fails already at
  `d = 1`), a from-scratch bridge stronger than the landed `1+1d`
  status, or sharp constants.
- Does **not** interpret the taste corners as species or select
  occupancy; no physical time is selected (`a_τ` conventional).
- Does **not** modify the three cited notes.
- Does **not** set an audit verdict; independent audit remains
  required.

## Verification

Primary runner:
[`scripts/free_staggered_d_dimensional_two_step_many_body_transfer_2026_07_20.py`](../scripts/free_staggered_d_dimensional_two_step_many_body_transfer_2026_07_20.py)
— sympy-exact throughout (no floats as inputs; no numeric
tolerances). **What each gate does and does not cover, stated
plainly, because the coverage is uneven:**

*Gates that test the grade-(A) d-dimensional classical algebra.*
`G1` rebuilds the Clifford/corner algebra from the fold rule at
`d = 2, 3` with symbolic `s_μ` and establishes the scalar square
`S(k)² = (Σ s_μ²)I`, plus the general-period mode count. `G3` is
the only position-space gate in which the staggered phases do any
work: at `d = 2, L = 4` it exhibits `charpoly(H_hop²) =
λ⁴(λ+1)⁸(λ+2)⁴`, matching the independent momentum count
`{0×4, −1×8, −2×4}`. `G4` exercises genuine corner coupling
symbolically at `k = (π/2, π/2)` (`S = Γ_1 + Γ_2`, `S² = 2I`) and
at `k = (π/2, 0)`, pinning the `2^d` multiplicities by minimal
polynomial + trace. `G5` gates the projector identities and the
strict reciprocal split via `R(1+R) − R² = R > 0`.

*Support-only gates, carrying NO d-dimensional content.* `G2` runs
at `L = 2`, where `H_hop = 0` identically; it therefore tests a
mass-only repeated recurrence and nothing about the phases, `S(k)`,
or `E_d`. `G7` (four modes) and `G8` (eight modes) are generic
exterior-algebra / Jordan-Wigner bookkeeping in a free symbolic
scalar `t`; their `d = 2` and `d = 3` labels record only which mode
count they instantiate, not any dimensional content. **No gate
composes the grade-(A) classical algebra with the Fock
construction** — that composition is grade (B), and it runs through
the supplied kernel form, which no gate can validate.

*Gate-strength caveats, stated rather than glossed.* In `G6` the
`C ≠ 1` conjunct is a symbolic constant-term residual `C − 1` whose
zero set is `C = 1`; it is a bookkeeping statement, not an
independent discrimination. In `G9` the multiplicativity conjunct
is true by construction of the instance and is not an independent
oracle — the abstract conjugation argument is the corner-note's;
the intertwiner and log-identity failures in `G9` are genuine
discriminations. In `G7` the CAR anticommutator gates
`{a_i, a†_j} = δ_ij`, `{a†_i, a†_j} = 0` do discriminate a
sign-stripping mutation, but only for the runner's own
Jordan-Wigner matrices: they verify that a chosen Fock
representation satisfies the CAR; they do **not** derive the
physical CAR metric, the reflected inner product, or the
action-to-Fock identification. The diagonal-kernel intertwiner is
sign-convention-blind (both sides carry the same JW sign).

*Needles* (`N1`–`N5`) are presence checks on the cited notes'
displays and boundary sentences — not correctness oracles — plus
target-note self-pins, which are not evidence either. Presence
checks alone cannot detect a restored over-claim, since adding a
retracted sentence does not remove the corrected ones, so `N6` is
an **absence** gate: it fails if any of the eight phrases retracted
in review — enumerated in the runner's `RETRACTED_PHRASES`, and
quoted in this note only inside the N5 rhetoric-audit bullet —
reappears anywhere on this note's live claim surface, meaning the
YAML `claim_scope` plus every body section other than that one
bullet. The exclusion ends at the next list item or heading, so a
live claim cannot be hidden by appending it after the historical
text; the gate was mutation-probed both ways. The gate sequence is
enforced against an ordered label manifest; one `PASS`/`FAIL` line
per gate and a final total; the cached transcript is committed at
the header path at landing time.
