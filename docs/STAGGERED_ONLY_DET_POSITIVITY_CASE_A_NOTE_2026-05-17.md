# Staggered-Only det(M_KS + m·I) > 0 — Sub-Theorem Note (Case A standalone)

**Date:** 2026-05-17
**Type:** positive_theorem (narrow sub-theorem)
**Loop:** `axiom-first-foundations` (block 25 of the
  2026-05-17 physics-loop campaign)
**Review-loop status:** source-note proposal; independent audit lane owns any audit verdict.
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/staggered_only_det_positivity_case_a_2026-05-17.py`
**Cache:** `logs/runner-cache/staggered_only_det_positivity_case_a_2026-05-17.txt`

## Why this note exists

The parent reflection-positivity note
`docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`
records (post-2026-05-17 narrowing) a load-bearing claim restricted to
two sub-cases:

- **Case A** — staggered-only sector `M = M_KS + m · I` — closed-form on
  the explicit framework baseline via `{ε, M_KS} = 0` plus ±λ paired
  eigenvalues of `γ_5 M`.
- **Case B** — symmetric-canonical Wilson subsurface
  `M = M_KS + r · d · I + m · I` — closed-form, *conditional* on the
  bridge note
  `STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md`
  reaching retained-grade status.

Case B's bridge note carries its own conditional audit status. Case A
is therefore the only currently *unconditional* closed-form route by
which the parent note's combined RP statement is supported. The Case A
derivation in the parent note's §"Step 3a — historical staggered-only
derivation" gets the correct answer but is presented in an abbreviated
form (parent eqs (14a)-(14b)) that:

1. concludes `det(M_KS + m·I) = ∏_pairs λ² ≥ 0` from the ±λ pairing of
   eigenvalues of `γ_5 M`, **without** explicitly reconciling the sign
   that the multiplicativity `det(γ_5 M) = det(γ_5) · det(M)` introduces
   on a balanced lattice (the same sign that eqs (15)-(17) of the bridge
   note carefully tracks for the joint sector);
2. yields `det(M) ≥ 0` (non-negative) without isolating the
   strictly-positive case `m > 0`, which is the load-bearing input that
   the Step 3 combined-sector argument actually uses.

The purpose of this note is therefore to supply a **standalone**,
**self-contained**, **strictly-positive** closed-form proof of
`det(M_KS + m·I) > 0` for `m > 0` on the explicit framework baseline,
with the `det(ε)` sign reconciliation written out in full. The proof
re-uses only inputs that are themselves either closed-form in the physical Cl(3)/Z^3 framework baseline or
verified explicitly by the parent runner's Exhibit E5; in particular
it does **not** depend on the Wilson-sector bridge note.

This sub-theorem strengthens the parent note's Case A path from
"runner-verified plus abbreviated algebraic sketch" to "closed-form
strictly-positive on the explicit framework baseline with the sign
reconciliation written out" — without modifying the parent note's text
and without introducing any new dependency on the bridge note.

## Scope

**In scope.** The bare staggered-Dirac Kogut-Susskind operator with
positive real mass

```text
    M  :=  M_KS  +  m · I,                 m > 0                       (1)
```

on the canonical lattice block `Λ = (Z/L_τ Z) × (Z/L_s Z)^{d_s}` with
**even** total site count `n`, balanced sublattice partition
`n_+ = n_- = n / 2` under the staggered chirality
`ε(x) = (-1)^{x_1 + … + x_d}`, and **arbitrary SU(3) gauge background**
on the links. We prove

```text
    det(M)  >  0                                                       (2)
```

configuration-by-configuration on every SU(3) link assignment.

**Out of scope.**

- Any Wilson contribution `M_W ≠ 0`. The Wilson sector is the bridge
  note's territory (Case B), and is explicitly excluded here.
- Site-dependent staggered mass `m · ε(x)`. The mass term is
  `m · I` with `m > 0` real, matching parent eq. (1) and the parent mass-term carrier.
- The reflection-positivity-of-the-full-action statement. The
  parent note is the load-bearing authority for that; this note only
  supplies the Case A determinant input to its Step 3.

## Setup and conventions

Adopt the parent-note conventions verbatim:

- **Framework baseline and parent conventions.** The physical `Cl(3)` local algebra, `Z^3` spatial substrate, and parent reflection-positivity conventions are used as repo-baseline definitions and local setup. The lattice block has even side
  lengths in every direction so `n_+ = n_-`.
- `M_KS` is the canonical Kogut-Susskind staggered Dirac hop with
  staggered phases `η_μ(x) = (-1)^{Σ_{ν<μ} x_ν}` and SU(3) gauge links
  parallel-transporting between nearest neighbours. It is
  **anti-Hermitian**: `M_KS^† = -M_KS`.
- `{ε, M_KS} = 0` (parent Exhibit E5). This is verified by the parent
  runner across `L_t ∈ {4, 6, 8}` and `L_s ∈ {4, 6}` (both even);
  on the canonical surface the anticommutation is structural, not a
  numerical accident — it follows from each staggered hop carrying a
  parity change and the ε grading being the parity.
- Mass term `m · I` with `m > 0` real (parent eq. (1)).
- Gauge background is an SU(3) link configuration `{U_μ(x)}`. The proof
  does not depend on the specific configuration.

## Block decomposition

Order the lattice sites so the `n_+` sites with `ε = +1` come first
and the `n_-` sites with `ε = -1` come second. In this basis,

```text
    ε  =  diag(+I_{n_+}, -I_{n_-}).                                    (3)
```

Since every staggered hop changes ε-parity (each hop is a single
nearest-neighbour step, which flips one Z₂ coordinate sum), `M_KS` is
purely off-diagonal in the ε-sorted basis:

```text
    M_KS  =  [[ 0,    K  ],
              [ -K^†, 0  ]]                                            (4)
```

The block `K` is the `n_+ × n_-` matrix of staggered hops from `+1` to
`-1` sites, including the SU(3) parallel-transport phases. The bottom-
left block being `-K^†` is the explicit content of anti-Hermiticity
`M_KS^† = -M_KS`.

The mass term contributes `m · I` to each diagonal block:

```text
    m · I  =  [[ m · I_{n_+}, 0           ],
                [ 0,            m · I_{n_-} ]]                          (5)
```

Combining (4) and (5),

```text
    M  =  [[ m · I_{n_+},   K           ],
            [ -K^†,           m · I_{n_-} ]]                           (6)
```

## γ₅ M is Hermitian

Identify `γ_5 ≡ ε` on the staggered carrier. Then

```text
    γ_5 M  =  ε M  =  [[ +m · I_{n_+},   +K            ],
                        [ +K^†,            -m · I_{n_-} ]]              (7)
```

This is **Hermitian**: the top-left block is `+m · I` (Hermitian and
real), the bottom-right block is `-m · I` (also Hermitian and real),
and the off-diagonal blocks are conjugate-transpose of each other
(top-right is `+K`, bottom-left is `+K^†`, so the block-Hermitian
condition holds).

Hermiticity of `γ_5 M` is the γ_5-Hermiticity statement
`(γ_5 M)^† = γ_5 M` that the parent note cites and that is the standard
input to the ±λ paired-eigenvalue argument.

## Singular-value decomposition of the off-diagonal block

Let `K = U Σ V^†` be the SVD of the `n_+ × n_-` matrix `K`, where
`Σ = diag(σ_1, …, σ_{n/2})` with `σ_1 ≥ σ_2 ≥ … ≥ σ_{n/2} ≥ 0` the
singular values (both sublattices have size `n/2` on the balanced
lattice), `U` an `n_+ × n_+` unitary, and `V` an `n_- × n_-` unitary.

Conjugating `γ_5 M` by the block-diagonal unitary `W := diag(U, V)`,

```text
    W^† (γ_5 M) W  =  [[ +m · I,   +Σ      ],
                        [ +Σ,        -m · I ]]                          (8)
```

Unitary conjugation preserves both spectrum and determinant. The
right-hand-side block matrix decomposes further via the basis-permutation
that interleaves `(e_i^+, e_i^-)` pairs, giving `n/2` independent
`2 × 2` blocks:

```text
    block_i  =  [[ +m,    +σ_i ],
                  [ +σ_i,  -m   ]]                                     (9)
```

## Eigenvalues and determinant of each 2 × 2 block

Each `2 × 2` block in (9) is trace-zero with determinant `-m² - σ_i²`.
Its eigenvalues are the roots of

```text
    λ² - (trace) · λ + (det)  =  λ²  -  0  +  (-m² - σ_i²)  =  0       (10)
```

giving `λ = ± √(m² + σ_i²)`. This is the explicit ±λ paired-eigenvalue
structure that the parent note's eq. (14a) invokes but does not write
out in this fully reduced block form. Its determinant is

```text
    det(block_i)  =  -m²  -  σ_i²                                      (11)
```

## Multiplying over blocks

Multiplying (11) over all `n/2` blocks,

```text
    det(γ_5 M)  =  ∏_{i=1}^{n/2}  (-m² - σ_i²)
                =  (-1)^{n/2}  ·  ∏_{i=1}^{n/2}  (m² + σ_i²)           (12)
```

This is the key place where the sign `(-1)^{n/2}` enters explicitly.
The parent note's eq. (14b) writes `det(M_KS + mI) = ∏_pairs λ² ≥ 0`,
which is correct in absolute value but does not reconcile this sign
with the `det(γ_5)` sign that the multiplicativity step below
introduces. The reconciliation is the content of the next step.

## The det(γ₅) = (-1)^{n/2} sign reconciliation

The chirality determinant on the balanced lattice is

```text
    det(γ_5)  =  det(ε)  =  (+1)^{n_+}  ·  (-1)^{n_-}
              =  1^{n/2}  ·  (-1)^{n/2}
              =  (-1)^{n/2}                                            (13)
```

using `n_+ = n_- = n/2`. By multiplicativity of the determinant,

```text
    det(γ_5 M)  =  det(γ_5)  ·  det(M)                                 (14)
```

Substituting (12) and (13) into (14):

```text
    (-1)^{n/2}  ·  ∏ (m² + σ_i²)  =  (-1)^{n/2}  ·  det(M)             (15)
```

The two `(-1)^{n/2}` factors cancel:

```text
    det(M)  =  ∏_{i=1}^{n/2}  ( m²  +  σ_i² )                          (16)
```

## Strict positivity for m > 0

For any `m > 0` and any SU(3) gauge background, every factor satisfies

```text
    m²  +  σ_i²  ≥  m²  >  0                                           (17)
```

(the inequality `m² + σ_i² ≥ m² > 0` uses only `m² > 0` and
`σ_i² ≥ 0`; the strict inequality `m² + σ_i² > 0` is therefore
independent of the value of `σ_i`). Multiplying over `i = 1, …, n/2`,

```text
    det(M)  =  ∏_{i=1}^{n/2}  ( m²  +  σ_i² )  >  0                    (18)
```

configuration-by-configuration on every SU(3) link assignment.

This is the strictly-positive closed-form determinant input that the
parent note's Step 3 combined-sector RP argument uses on the Case A
sub-surface. ∎

## What this proves

1. `det(M_KS + m·I) > 0` configuration-by-configuration on every SU(3)
   gauge background, for any `m > 0`, on the balanced canonical
   lattice block. (Equation (18).)

2. The factorisation formula
   `det(M_KS + m·I) = ∏_{i=1}^{n/2} ( m² + σ_i² )`. (Equation (16).)

3. The full sign reconciliation between `det(γ_5 M)` and
   `det(γ_5) · det(M)`. (Equations (12)-(15).)

## What this does *not* prove

- Anything about `M_W ≠ 0`. The Wilson sector is the bridge note's
  territory (Case B). If the bridge note's symmetric-canonical
  closure is not retained on independent audit, this Case A
  sub-theorem is still unaffected: it stands or falls on its own
  staggered-only inputs.

- Reflection positivity of the full canonical action. That
  remains the parent note's load-bearing claim; this note supplies a
  cleaner determinant input to its Case A path.

- Anything about staggered mass `m · ε(x)` (where the mass term picks
  up a sign across sublattices). That would change `m · I` in (5)
  to `m · ε`, breaking the calculation at (7); the parent note's
  Case A explicitly uses real mass `m · I`.

## Inputs

| Input | Source | Audit status |
|---|---|---|
| `M_KS` anti-Hermitian | Definition of canonical Kogut-Susskind hop (parent §"Setup", parent eq. (1)) | closed-form (definitional) |
| `{ε, M_KS} = 0` (parent E5) | Parent Exhibit E5, verified on `L_t ∈ {4,6,8}`, `L_s ∈ {4,6}` | runner-verified + structural |
| Balanced sublattice `n_+ = n_- = n/2` | Even side lengths in every direction (parent setup) | closed-form (definitional) |
| Mass term `m · I`, `m > 0` real | Parent eq. (1), parent mass-term carrier | closed-form (definitional) |
| SVD of arbitrary complex matrix `K` | Standard linear algebra | closed-form (theorem of linear algebra) |
| Block-determinant arithmetic | Standard `2 × 2` determinant identity | closed-form (algebra) |
| `det(γ_5) = (-1)^{n/2}` on balanced lattice | Equation (13), counting +1 and -1 entries on the ε-diagonal | closed-form (algebra) |

No imports from the forbidden list. No imports from the Wilson-sector
bridge note. No numerical, observed, or fitted inputs.

## Cross-check against the bridge note

This Case A sub-theorem is the `M_W = 0` specialisation of the bridge
note's symmetric-canonical theorem, with `α := m` in place of
`α := r · d + m`. Specifically:

- Bridge eq. (9) becomes (16) with `α → m`.
- Bridge eq. (15) becomes (12) with `α → m`.
- Bridge eq. (16) is identical to (13).
- Bridge eq. (17) becomes (15)-(16) with `α → m`.

The point is that with `M_W = 0` the symmetric-canonical assumption
`A = B = α · I` of the bridge becomes *unconditional* — there is no
Wilson term to constrain, so the bridge's load-bearing assumption (D4)
holds trivially. The Case A sub-theorem is therefore the bridge note's
content **specialised to a regime where it requires no extra
hypothesis**.

Consequence: the Case A sub-theorem is not contingent on whether the
bridge note retains its `audited_conditional` or upgrades to retained;
its own audit can therefore proceed independently.

## Corollaries (downstream)

C1. *Parent note Case A path is closed-form and strictly positive on
the explicit framework baseline.* The parent note's §"Step 3a —
historical staggered-only derivation" can be cited together with this
sub-theorem to upgrade its Case A determinant input from "abbreviated
algebraic sketch" to "explicit closed-form".

C2. *Worst-case gauge background.* Equation (16) shows that the
determinant is **bounded below by `m^n` on every SU(3) gauge
background** (set all `σ_i = 0` to minimise). The strictly-positive
lower bound `m^n > 0` is uniform in the link configuration. This
makes the Case A path *manifestly gauge-uniform*: there is no
sign-problem regime hidden in the SU(3) measure.

C3. *Compatibility with γ_5-Hermiticity.* Equation (14) is the
multiplicativity of the determinant under multiplication by `γ_5`. It
is the same fact that supports the strong-CP / `θ_eff = 0` row of
`docs/ASSUMPTION_DERIVATION_LEDGER.md` on the staggered-only sector.

## Honest status

**Branch-local closed-form sub-theorem on the explicit framework
baseline.** Independent audit is required before any retained-grade
elevation. The runner numerically verifies the factorisation formula
(16) and the strict-positivity bound (18) across a representative
parameter scan; the runner is a verification of the load-bearing
identity, not a substitute for the closed-form derivation above.

This note is strictly additive on the parent note. It does **not**:

- modify the parent note's text;
- add or remove any parent note dependency;
- claim to extend RP outside the parent note's narrowed scope;
- claim retained-grade status for itself.

It only **supplies a cleaner, fully self-contained derivation** of the
parent's Case A determinant input.

## Citations

- Explicit framework baseline: `docs/MINIMAL_AXIOMS_2026-04-11.md`
- Parent reflection-positivity note (consumes this Case A input):
  `docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`
- Sister bridge note for Case B (independent of this note):
  `docs/STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md`
- Parent runner (verifies inputs E5, E6):
  `scripts/axiom_first_reflection_positivity_check.py`
- Assumption / derivation ledger:
  `docs/ASSUMPTION_DERIVATION_LEDGER.md`
