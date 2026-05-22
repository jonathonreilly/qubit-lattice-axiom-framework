# Observable-Principle P1 + P2 from Qubit-Trace Generating Functional

**Date:** 2026-05-20
**Type:** bounded_theorem candidate
**Status:** source-side proposal — independent audit lane owns the verdict
**Supplies (proposed):** bounded qubit-trace support for the P1
scalar-additivity premise and the phase-positive/P2 side condition named in
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` (`audited_conditional`,
load_bearing_score 50.996, 1020 transitive descendants — **#2 most
load-bearing row in the audit ledger**). The observable-principle parent is a
downstream repair target, not an upstream theorem dependency for this row.

## Claim

On the qubit-lattice substrate
([`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md):
A1 = qubit at every site = `M_2(ℂ)`; A2 = `Z^3`), the canonical
**qubit-trace generating functional**

```text
W_qubit[J] := log Tr_A(e^{-(H + J)}) - log Tr_A(e^{-H})                  (1)
```

(for self-adjoint source `J ∈ A_Λ` and Hamiltonian `H ∈ A_Λ`) is a
well-defined real-valued scalar functional that **automatically
satisfies** two premises named by
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`:

- **(P1) Scalar additivity on independent subsystems** — derived
  from trace-tensor factorization on disjoint qubit regions
  (Step 1 below).
- **(P2) CPT-even phase-blindness** — automatic, because `Z[J]` is
  manifestly real-positive for self-adjoint `H + J` (Step 2 below).
  No phase to be sensitive to.

The remaining two premises (P3 continuity, P4 normalization) are
trivially satisfied by log of a positive real plus an additive
constant choice; they are convention, not substantive admission.

**Net:** on the qubit-trace formulation, P1 additivity and the
phase-positive side of P2 are no longer standalone scalar-selection
premises. Transferring that repair back to the observable-principle
parent's `W = log|det(D+J)|` formulation remains gate-conditional
through the admitted Grassmann/Berezin bridge, and this note does not
retag the parent row by itself.

## Setup

By A1+A2, the quasi-local operator algebra is
`A = ⊗_{x ∈ Z^3} M_2(ℂ)`, the UHF C*-algebra of type `2^∞`. For a
finite region `Λ ⊂ Z^3`, `A_Λ = ⊗_{x ∈ Λ} M_2(ℂ)` is a simple
finite-dim C*-algebra acting on `H_Λ = ⊗_x ℂ²` of dimension `2^|Λ|`.

The qubit algebra has a **canonical trace** `Tr_A: A_Λ → ℂ` (the
matrix trace inherited from `M_2(ℂ)` via tensor product). For any
positive operator `B ∈ A_Λ` with `B ≥ 0`, `Tr_A(B) ∈ ℝ_{≥ 0}`.

The qubit-trace partition function for a Hamiltonian `H[J] = H + J`
(`H, J ∈ A_Λ` self-adjoint) is

```text
Z[J] := Tr_A(e^{-(H + J)})                                               (2)
```

Since `H + J` is self-adjoint, `e^{-(H + J)}` is positive (functional
calculus on a positive operator), so `Z[J] > 0` and `W_qubit[J] :=
log Z[J] - log Z[0]` is well-defined and real.

This is the standard Gibbs partition function on the qubit algebra.

## Step 1 — P1 (scalar additivity) from trace-tensor factorization

Let `Λ = Λ_1 ⊔ Λ_2` be a disjoint union, with `A_Λ = A_{Λ_1} ⊗
A_{Λ_2}`. Consider **independent source perturbations** `J_1 ∈ A_{Λ_1}`
and `J_2 ∈ A_{Λ_2}` with the combined source

```text
J_1 ⊕ J_2 := J_1 ⊗ 𝟙_{Λ_2} + 𝟙_{Λ_1} ⊗ J_2                              (3)
```

Independence here is the standard operator-algebraic statement:
`J_1` and `J_2` act on disjoint qubit regions, so
`[J_1 ⊗ 𝟙, 𝟙 ⊗ J_2] = 0`.

Assume the Hamiltonian decomposes correspondingly:
`H = H_1 ⊗ 𝟙 + 𝟙 ⊗ H_2` (no inter-region coupling for the
independent-subsystem premise). Then

```text
H + (J_1 ⊕ J_2) = (H_1 + J_1) ⊗ 𝟙 + 𝟙 ⊗ (H_2 + J_2)                    (4)
```

Both terms commute (disjoint regions, qubit tensor structure).
Exponentiating commuting self-adjoint operators:

```text
e^{-(H + (J_1 ⊕ J_2))} = e^{-(H_1 + J_1) ⊗ 𝟙} · e^{-𝟙 ⊗ (H_2 + J_2)}
                       = e^{-(H_1 + J_1)} ⊗ e^{-(H_2 + J_2)}             (5)
```

Apply the trace-tensor identity (standard linear algebra):

```text
Tr_{A_1 ⊗ A_2}(B_1 ⊗ B_2) = Tr_{A_1}(B_1) · Tr_{A_2}(B_2)               (6)
```

to get

```text
Z[J_1 ⊕ J_2] = Z_1[J_1] · Z_2[J_2]                                       (7)
```

where `Z_i[J_i] = Tr_{A_{Λ_i}}(e^{-(H_i + J_i)})`. Taking logs:

```text
W_qubit[J_1 ⊕ J_2] = log(Z_1[J_1] · Z_2[J_2])
                   = log Z_1[J_1] + log Z_2[J_2]
                   = W_qubit_1[J_1] + W_qubit_2[J_2]                     (8)
```

(after subtracting the zero-source baseline on each side; the
constants cancel).

**This is the qubit-trace P1 support theorem.** No extra scalar-additivity
premise is admitted once the independent-subsystem scope is fixed; the
additivity follows from (2) + (3) + (6) — all standard linear-algebra /
operator-trace content on the qubit algebra.

The independent-subsystem premise (`H = H_1 ⊗ 𝟙 + 𝟙 ⊗ H_2`,
`[J_1, J_2] = 0` across regions) is the **defining** content of
"independent subsystems" on the qubit lattice. Under A1+A2, this
is tracked by the equal-time locality row
`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`.
That upstream row's audit status is independent of this note.

## Step 2 — P2 (CPT-even phase-blindness) from trace positivity

The observable-principle note's P2 says the scalar generator must
depend only on `|Z|`, not on the phase of `Z`. In the framework's
`log|det(D+J)|` formulation, `det(D+J)` can be complex (the Dirac
operator + source need not be self-adjoint as written), and the
modulus `|·|` is taken to enforce phase-blindness.

In the qubit-trace formulation (1), `Z[J]` is **manifestly real and
positive** because `H + J` is self-adjoint (by construction:
sources to physical Hamiltonians are self-adjoint), so
`e^{-(H + J)}` is positive (functional calculus), so
`Tr_A(positive) > 0`. There is no phase to be sensitive to. P2 is
automatically satisfied.

CPT-even content is inherited from the framework's CPT-lane action
recorded in `AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md`.
That upstream row remains independently audit-scoped. If `Θ` is the
antiunitary CPT operator, `Z[J]` transforms as `Z[J] →
Tr(Θ^{-1} e^{-(H+J)} Θ) = Tr(e^{-Θ^{-1}(H+J)Θ}) = Z[ΘJΘ^{-1}]`
(using Θ-invariance of `H`). So `W_qubit[J]` is CPT-equivariant
on sources. The positive-trace construction supplies the phase-blind
part of P2; any stronger parent-row interpretation remains tied to the
parent's own audit and the bridge back to `log|det|`.

**This is P2.** No phase admission required; the positive-trace
structure of the qubit algebra makes phase-blindness automatic.

## Step 3 — P3 (continuity) and P4 (normalization)

**P3 (continuity / regularity):** `log: ℝ_{>0} → ℝ` is smooth.
`Z[J] > 0` for any self-adjoint `J`. So `W_qubit[J] = log Z[J] -
log Z[0]` is smooth in `J` (in any reasonable topology on the
finite-dim algebra `A_Λ`). P3 is automatically satisfied; no
admission.

**P4 (normalization):** Convention — the subtraction of `log Z[0]`
in (1) fixes the additive constant so `W_qubit[0] = 0`. This is a
choice of zero-source baseline, identical in content to the
observable-principle note's P4 normalization.

## Step 4 — Bridge to `log|det(D+J)|` formulation

The framework's
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`
writes the scalar generator as `W = log|det(D+J)|`. This is the
**fermion partition function log** under the Berezin Gaussian
integration identity:

```text
Z_fermion[J] = ∫ Dψ̄ Dψ exp(-ψ̄ (D+J) ψ) = det(D+J)                       (9)
```

For Grassmann fields `ψ̄, ψ` and Dirac operator `D + J`. The bridge
from the qubit-trace `Z[J] = Tr(e^{-H[J]})` to the fermion-det
`Z_fermion[J] = det(D+J)` requires:
- Grassmann/Berezin Gaussian integration identity (standard)
- Identification of the fermion sector of `H` with the staggered
  Dirac operator `D` (depends on the **staggered-Dirac realization
  gate**, currently open)

This bridge is **admitted as gate-conditional**. Closure of the
Grassmann gate would internalize the bridge; in the meantime,
this note's content (Steps 1–3) is valid for the qubit-trace `W`
formulation, and the |det| formulation inherits additivity P1 and
phase-blindness P2 via the bridge.

## What this can close after audit

- **P1 (scalar additivity)** on
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`: supplied in Step 1 for
  the qubit-trace formulation from trace-tensor factorization on the
  qubit algebra.
- **P2 phase-blindness support** on the same row: supplied in Step 2
  from positivity of qubit-trace partition functions, with CPT
  equivariance tracked separately through the CPT-lane row.

If this row is accepted by the audit lane and the dependency-chain
repair is then applied to the parent, the observable-principle row can
replace its standalone P1/P2 admissions with this bounded qubit-trace
support plus the still-open Grassmann gate bridge to the `|det|`
formulation. P3 and P4 remain convention/regularity conditions of the
parent row.

## What this does not close

- **Bridge from qubit-trace `W` to framework's `log|det(D+J)|`** —
  depends on Grassmann gate closure. Berezin Gaussian identity (9)
  is standard math but the identification of `D` with the framework's
  staggered Dirac operator is gate-dependent.
- **`v` readout from the conditional algebra closure** — explicitly
  out of scope of the parent observable-principle note.
- **The 1020 transitive descendants** are not all automatically
  promoted; they each have their own conditional structure. Closing
  P1+P2 on the parent strengthens the chain head but does not
  lift the chain unilaterally.

## Admitted inputs

1. **Microcausality on the qubit algebra** — tracked via
   `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`.
   Used in Step 1 for `[J_1 ⊗ 𝟙, 𝟙 ⊗ J_2] = 0` on disjoint regions.
2. **Independent-subsystem Hamiltonian decomposition**:
   `H = H_1 ⊗ 𝟙 + 𝟙 ⊗ H_2` for `Λ = Λ_1 ⊔ Λ_2`. This is the
   *defining* content of "independent subsystems" — admitted as
   the operator-algebraic formulation of physical independence
   (standard).
3. **CPT antiunitary action on the qubit algebra** — tracked via
   `AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29`; audit status
   and scope of that upstream row remain independent.
4. **Standard finite-dim linear algebra** (functional calculus on
   positive operators; trace-tensor identity; log smoothness on
   positive reals) — named non-derivation imports.

## Risk classification

This is a `bounded_theorem` candidate. The steps are textbook
operator-algebraic linear algebra (Steps 1, 3) plus separately tracked
framework primitives (microcausality, CPT). The narrow contribution
is the explicit identification that the qubit-trace formulation
(canonically available since the qubit reframe of A1) makes P1 and
P2 derivable rather than admitted.

The qubit reframe of A1 (landed in main as
`MINIMAL_AXIOMS_2026-05-20.md`) is what enables this note: the
canonical trace on `M_2(ℂ)` makes the qubit-trace partition
function `Z[J] = Tr(e^{-H[J]})` the natural starting point,
which is **not** the framework's `log|det|` formulation but is
mathematically equivalent under the Grassmann/Berezin bridge.

Without the qubit reframe, the natural scalar generator was the
fermion-det version `log|det(D+J)|`, for which P1 and P2 had to be
admitted as selection premises. With the qubit reframe, the natural
scalar generator is the qubit-trace `log Z[J]`, for which P1 and P2
are theorems.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links so the citation graph records them as deps):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies A1+A2 (qubit-form local algebra and `Z^3` substrate); the qubit-trace formulation requires the canonical trace on `M_2(ℂ)`
- [`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md) — supplies microcausality for the independent-subsystem premise
- [`AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md`](AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md) — supplies the CPT action used in Step 2 phase-blindness derivation

**Upstream standard-math imports** (named non-derivation; not framework rows):

- Functional calculus on positive self-adjoint operators (e.g. Reed-Simon Vol. I)
- Trace-tensor identity `Tr(A ⊗ B) = Tr A · Tr B` (standard linear algebra)
- Berezin/Grassmann Gaussian integration (Berezin 1966); used in Step 4 bridge to `det` formulation

**Plain-text pointer references** (NOT load-bearing deps):

- `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` — downstream parent row
  whose P1/P2 repair this note may support after independent audit and
  dependency-chain update
- `STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md` — Grassmann gate closure target; the gate-conditional bridge in Step 4 depends on this gate closing

## Runner companion

Primary runner:
[`scripts/audit_companion_observable_principle_p1_p2_qubit_trace_2026_05_22.py`](../scripts/audit_companion_observable_principle_p1_p2_qubit_trace_2026_05_22.py)
verifies Step 1 and Step 2 of this note at exact sympy precision on small
qubit blocks plus randomized numeric checks on 2-site and 3-site qubit
registers:

- **T1**: Symbolic 1-qubit factorization
  `exp(-(H_A ⊗ I + I ⊗ H_B + J_A ⊗ I + I ⊗ J_B))
  = exp(-(H_A + J_A)) ⊗ exp(-(H_B + J_B))` at exact sympy precision on
  diagonal Hermitian inputs, plus the trace identity (Eq. 6 of the note).
- **T2**: log-additivity follow-through
  `W_qubit[J_A ⊕ J_B] = W_qubit[J_A] + W_qubit[J_B]` at high-precision
  rational sympy evaluation (50-digit) on three independent substitutions
  (Eq. 8 of the note).
- **T3**: Trace-tensor identity `Tr(B_A ⊗ B_B) = Tr(B_A) · Tr(B_B)` on
  10 random rational 2x2 pairs (the linear-algebra input used in Step 1,
  Eq. 6).
- **T4**: Boundary normalization `W_qubit[0] = 0` (Step 3 / P4)
  symbolically and on a numeric 4x4 Hermitian sample.
- **T5**: 2-site numeric factorization on 25 random Hermitian
  (`H_A, H_B, J_A, J_B`) 2x2 samples, residual `< 1e-12`.
- **T6**: 3-site (8x8) numeric factorization on 15 random Hermitian
  (`H_A` 2x2, `H_B` 4x4, `J_A` 2x2, `J_B` 4x4) samples, residual
  `< 1e-10`. (Sympy `Matrix.exp` on 8x8 symbolic Hermitian times out
  > 60 s; exact-symbolic verification is done at T1 / T2 on the
  smaller 4x4 case, numeric at T6 confirms the same identity at
  higher dimension.)
- **T7**: Positivity (Step 2 / P2 side condition).  Generic 2x2 Hermitian
  `M` parameterized by 4 real symbols `(x, y, z, w)`; verify the
  eigenvalue discriminant `(x-y)^2 + 4(z^2 + w^2)` is a manifest sum
  of real squares so eigenvalues are real; verify `Tr(exp(-M)) > 0`
  on a symbolic substitution and on 100 random Hermitian samples
  (d in {2, 4}, 50 each).
- **T8**: CPT-equivariance shape check
  `Tr((exp(-(H+J)))^*) = Tr(exp(-(H + J^*)))` for real `H` and
  Hermitian `J` (Step 2 CPT footnote), numeric on a 4x4 instance, plus
  modulus equivariance `|Z[J]| = |Z[ΘJΘ^{-1}]|`.
- **T9**: Source-note boundary check — required strings
  (`bounded_theorem candidate`, `independent audit lane owns the verdict`,
  `gate-conditional`, `audited_conditional`) present and forbidden
  overclaim phrases absent.
- **T10**: Independence (microcausality input, Eq. §1 of "Admitted
  inputs") — `[J_A ⊗ I, I ⊗ J_B] = 0` for arbitrary 2x2 Hermitian
  `J_A, J_B` at exact symbolic precision.

Reproduction:

```bash
python3 scripts/audit_companion_observable_principle_p1_p2_qubit_trace_2026_05_22.py
```

Expected scorecard: PASS=23 FAIL=0 at exact sympy precision plus the
named numeric tolerances on randomized samples.  A passing run supplies
the bounded structural content for Steps 1 + 2 + 4 of the note above;
it does not retag the broad parent row `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`
and does not internalize the Grassmann/Berezin bridge to the `det` form
(which remains gate-conditional on
`STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md`).

`runner_path: scripts/audit_companion_observable_principle_p1_p2_qubit_trace_2026_05_22.py`

## What this file is not

- Not a derivation of the Grassmann/Berezin bridge to the |det| formulation (admitted, gate-conditional).
- Not a closure of the observable-principle parent note itself (closes 2 of 4 premises; bridge remains).
- Not an automatic promotion of the 1020 transitive descendants.
- Not a numerical-prediction change.
- Not a unilateral retagging. The bounded-theorem candidacy depends on independent audit acceptance of the qubit-trace formulation, the Step 1 trace-tensor argument, and the Step 2 CPT-action argument.
