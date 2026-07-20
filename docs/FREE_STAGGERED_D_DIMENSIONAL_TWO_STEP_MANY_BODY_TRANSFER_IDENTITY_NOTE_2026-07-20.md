---
claim_id: free_staggered_d_dimensional_two_step_many_body_transfer_identity_note_2026-07-20
claim_type: bounded_theorem
claim_scope: "Free U = 1 staggered surface only, in the d-dimensional dispersion note's own conventions (one Grassmann component per site, d spatial axes, even spatial periods, real m > 0, canonical staggered phases): the ACTION-LEVEL d-dimensional many-body two-step transfer identity, extending the landed 1+1d derivation (RP-positivity note Steps 3b-4) to general d with the SAME bridge status — (T1) the per-reduced-momentum classical two-step block T_2(k) (dimension 2^{d+1}) is an explicit matrix function of the Hermitian taste-corner matrix S(k) = sum_mu sin(k_mu) Gamma_mu whose square is the SCALAR (sum_mu sin^2 p_mu) I (the dispersion note's 'only dimension-dependent algebraic step'), so it collapses to 2x2 blocks identical to the one-axis recursion with sin^2 p -> sum_mu sin^2 p_mu, with spectrum {e^{+2E_d}, e^{-2E_d}} each of multiplicity 2^d (taste-degenerate), E_d = arcsinh(sqrt(m^2 + sum sin^2 p_mu)); (T2) the forward-channel selection at general d: per-mode Riesz projectors (well-defined since m > 0 gives the strict reciprocal split lambda_- < 1 < lambda_+, REDERIVED here since the dispersion note states no (0,1] interval), and the RP note's stable-half-line SELECTION PRESCRIPTION (supplied, not derived: on finite time extent both reciprocal solutions are finite; the prescription — the same one the landed 1+1d identity carries — declares the forward kernel to be the decaying channel, and its sentence is dimension-blind while the d-dim furnishing of the 2x2 blocks is this note's Clifford content) selecting t1(2)_d = diag over the full-momentum modes of e^{-2E_d(p)}; (T3) the per-mode coherent-state -> exterior bridge with C = 1 pinned RELATIVE TO THE SUPPLIED KERNEL FORM: the RP note's one-mode coherent-kernel sentence is CONDITIONAL ('For a one-mode coherent-state kernel <zbar'|T_2|z> = exp(zbar' lambda_- z)...') — the exponential form is supplied there, not derived from the action, and this note inherits exactly that conditional; GIVEN the form, the kernel exp(zbar' lambda z) induces exactly diag(1, lambda) with vacuum element exp(0) = 1, so the Gaussian scalar is excluded relative to the form (a prefactor C != 1 has constant term C != 1), and the many-body kernel factorizes over the S(k)-eigenmodes because the selected one-particle kernel is diagonal — realizing the landed corner-note's canonical-intertwiner vacuum-fixing, the pin that trace + positivity + multiplicativity do NOT supply; the kernel form itself remains an explicit supplied input at every d including the landed d = 1; (T4) the assembly via the landed finite-mode theorem (canonical intertwiner, positive logarithm, trace, direct sums): at a_tau = 1 (all displays; the RP note's a_tau-carrying glyphs are reconciled AT a_tau = 1 and no general-a_tau display is claimed): T_hat^2_d = Gamma(t1(2)_d) = tensor_p diag(1, e^{-2E_d(p)}) = B^dag B with B = tensor_p diag(1, e^{-E_d(p)}), H_hat_d = -(1/2) log(T_hat^2_d) = dGamma(E_d) >= 0 (the d-dimensional two-step reflection-positivity statement), Tr T_hat^2_d = det(1 + t1(2)_d) = prod_p (1 + e^{-2E_d(p)}), and the mode count prod_mu (L_mu/2) * 2^d = prod_mu L_mu for even periods L_mu (hypercubic instance (L/2)^d 2^d = L^d; one decaying forward mode per full momentum; taste corners are spatial-fold bookkeeping, scalar fiber, not extra species) — supplying, at free U = 1 and general d, the OPERATOR IDENTIFICATION the landed corner-note names as an unsupplied prerequisite, with the same three supplied bridge parts as the landed d = 1 case (the stable-half-line selection prescription; the one-mode exponential kernel form; the finite-mode functor) and the only d-dependent input being the Clifford step — 'action-level' throughout MEANS this landed 1+1d bridge status, no more. a_tau = 1 is the working convention (the corner note's -1/2 log form); no physical time is selected. NOT claimed: fixed-gauge-background or U-integrated identification (the corner note names both open; this is the free specialization); interacting/non-quadratic transfers; any locality, kernel-envelope, or Lieb-Robinson content (the dispersion note's C_d/h(z) locality surface is NOT an input here); single-step positivity (fails already at d = 1); species/occupancy interpretation of the taste corners; sharpness; audit verdicts; nothing physical is selected."
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

Three landed notes triangulate a missing object. The corner-note
[`MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md)
proves the finite-mode second-quantization theorem but "does not
infer a many-body transfer operator from a one-particle kernel", and
names the operator identification as an unsupplied prerequisite for
any locality feed. The RP-positivity note
[`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
derives the full many-body two-step identity from the staggered
action — at `1+1d` only. The dispersion note
[`FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md)
derives the d-dimensional classical two-step structure but is
one-particle-only by its own boundary: it states no `(0,1]`
interval, builds no projectors, no coherent kernel, no `Γ`, no
`B†B` (its runner builds none of them; the channel selection is
deferred "as in the one-axis construction"). This note builds the
un-built bridge: the RP note's Steps 3b–4, executed at general `d`
on the dispersion note's own surface, with the same bridge status —
the only genuinely d-dependent input is the dispersion note's
Clifford step, and everything downstream is dimension-blind. The
result is the d-dimensional many-body identity at the landed
`1+1d` bridge status, with the normalization `C = 1` pinned
relative to the supplied one-mode kernel form (given the form, the
Gaussian scalar is excluded; the form itself stays a supplied
input, exactly as at `d = 1`).

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
`σ = ±λ`, `λ² = Σ sin² k_μ`, each sign with multiplicity `2^{d−1}`)
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
`k` share one `E_d`: the full block spectrum is `e^{+2E_d}` and
`e^{−2E_d}`, **each with multiplicity `2^d`** (gated by minimal
polynomial + trace, which pin the multiplicities without a symbolic
eigendecomposition). For `d ≥ 2` the corners genuinely couple
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
over modes; the vacuum→vacuum amplitude is `Π 1 = 1`. This realizes
the corner-note's canonical-intertwiner vacuum-fixing — the pin
that trace, positivity, and multiplicativity do **not** supply (its
`W`-conjugate counterexample is rebuilt here as a gate on a
non-degenerate kernel, where it genuinely discriminates; on fully
degenerate instances it cannot, and the runner says so honestly).

**Theorem (the d-dimensional identity).** On the stated surface,
at `a_τ = 1` (all displays; the RP note's `a_τ`-carrying glyphs
reconcile with the corner-note's `−(1/2)log` form exactly at
`a_τ = 1`, and no general-`a_τ` display is claimed):

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
gated). This is the d-dimensional two-step reflection-positivity
statement and the **operator identification the corner-note names
as an unsupplied prerequisite**, supplied at free `U = 1` and
general `d`, with `C = 1` derived. Honest bridge status, stated
plainly: exactly as in the landed `1+1d` derivation, the passage
from the classical monodromy to the quantum kernel has three
supplied parts — the stable-half-line selection prescription, the
one-mode exponential kernel form, and the finite-mode functor — and
this note's claim is **parity with the landed `d = 1` case**, not a
stronger from-scratch construction; the only d-dependent input is
the Clifford step, and "action-level" throughout means exactly this
landed bridge status. The taste corners are spatial-fold bookkeeping (one
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
  carry the same JW sign — the fermionic structure is pinned by the
  separate CAR gate, not by the intertwiner); the coherent-state
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
    rebuilt as Gate F; the "does not infer" and
    operator-identification-open sentences needled (the prerequisite
    supplied here).
  - [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):
    no-dynamics boundary needle only.
  - Loop-pack worker reports: disclosed scaffolding, graded against
    pre-recorded ground truth; not executed by the runner.
- **N5 rhetoric audit — ATTEMPTED.** "Action-level" is DEFINED in
  the claim scope as the landed `1+1d` bridge status (three
  supplied parts: selection prescription, kernel form, functor) —
  the first draft's "C = 1 derived rather than conventional" and
  "kernel form supplied by the quadratic action" were review-caught
  over-claims, retracted in place; "pinned relative to the supplied
  form" is the corrected statement everywhere; "supplies the
  prerequisite" refers to the operator identification at free
  `U = 1` only (the boundary-convention prerequisite is a separate
  lane's content); nothing is called sharp; the corner-coupling
  novelty is stated without superlatives.
- **N6 partial-closure scan — ATTEMPTED.** Supplied here: the free
  `U = 1` operator identification at general `d` (with positivity,
  trace, log-generator, and mode bookkeeping). Still open, named:
  fixed-gauge-background identification (`Γ(t[U])`), `U`-integrated
  measure, interacting transfers, locality feeds built on this
  identification, sharp anisotropic rates.
- **N7 steelman (strongest counterarguments, answered) —
  ATTEMPTED.** (a) "The forward-channel selection is a
  prescription, not a theorem." CORRECT and now stated as such: it
  is the RP note's supplied stable-half-line prescription, applied
  per 2×2 block; the note claims parity with that landed status,
  no more. (b) "`C = 1` is still conditional because the coherent
  kernel form is itself supplied." CORRECT and adopted (review
  round): the form is a supplied input at every `d` including
  `d = 1`; given the form, the constant term forces `C = 1` — the
  gate exhibits that `C·diag(1,λ)` fails the form. The note's
  value is that the d-dim identity now exists at exactly the
  landed conditional status, no weaker.
  (c) "Degenerate gates prove nothing about the pin." Correct, and
  stated: Gate F runs the discrimination on a non-degenerate
  kernel, where the `W`-conjugate genuinely breaks the intertwiner
  while preserving trace/positivity/multiplicativity. (d) "At
  `L = 2` the hop vanishes and the instances are trivial." True and
  used honestly: `L = 2` gates anchor the Fock assembly (all modes
  at `E = arcsinh(m)`); the corner-coupling content is gated at
  `L = 4` (position-space faithfulness) and symbolically at
  `k = (π/2, π/2)` where `S(k) = Γ_1 + Γ_2 ≠ 0`. (e) "The taste
  corners might secretly be a matrix fiber." In position space
  there is one Grassmann component per site; the corners arise
  from the momentum fold; the mode count closes exactly.
- **N8 prior-wall echo — ATTEMPTED.** The corner-note's refusal to
  infer many-body from one-particle is respected: this note does
  not infer — it derives, on the action surface where the RP note's
  bridge is available, and only there; the single-step
  non-positivity (landed at `1+1d`) is not contradicted (nothing
  single-step is claimed); the dispersion note's one-particle
  boundary is respected (its content is consumed as one-particle
  input; the many-body object is this note's construction); no
  landed no-go concerns the free two-step surface.

**Status: PASS** (all eight items answered; the honest weaknesses —
bridge parity rather than from-scratch derivation, and the
degenerate-gate limitation — are steelman subjects (a)/(c)/(d),
stated in the Results and Verification).

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
  pinned relative to the form).
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
tolerances). Gate kinds, honestly distinguished: **symbolic
identity gates** (the Clifford/corner algebra rebuilt from the
fold rule at `d = 2, 3` with `S(k)² = (Σ sin²)I`; the 2×2 collapse
displays; projector identities with the strict-split positivity
via `R(1+R) − R² = R`; the Grassmann bridge with the `C ≠ 1`
rejector; minimal-polynomial + trace multiplicity pins), **exact
instance gates** (position-space action rebuild at `d = 2, 3`,
`L = 2` — where the hop vanishes identically, stated honestly, and
the doubled classical block still carries `e^{±2 arcsinh m}` with
multiplicity `2^d`; the `d = 2, L = 4` position-space
`H_hop²` spectrum `{0×4, −1×8, −2×4}` — the faithfulness gate that
genuinely exercises the phases; the symbolic corner-coupled block
at `k = (π/2, π/2)`; the full-Fock `d = 2, L = 2` dense assembly
(16-dim: occupation `Γ`, the intertwiner for every mode — which for
a DIAGONAL kernel is sign-convention-blind, both sides carrying the
same JW sign, stated honestly — plus the separate CAR
anticommutator gates `{a_i, a†_j} = δ_ij`, `{a†_i, a†_j} = 0`,
which DO discriminate the JW signs and pin the fermionic structure;
per-entry log identity, trace = det, `B†B`); the structured
`d = 3, L = 2` assembly (256-dim: NO dense matrix — subset-indexed
scalars, target/scalar bookkeeping via action on basis vectors;
sign discrimination lives in the dense CAR gate); the
non-degenerate pin discrimination (Gate G9: the `W`-conjugate
preserves trace and inherits multiplicativity by conjugation —
instance-checked, the abstract argument being the corner-note's —
and BREAKS the intertwiner and the log identity)), and **needles** (presence
checks on the three cited notes' displays and boundary sentences —
not correctness oracles; target-note self-pins against drift, not
evidence). The gate sequence is enforced against an ordered label
manifest; one `PASS`/`FAIL` line per gate and a final total; the
cached transcript is committed at the header path at landing time.
