# Diagonal-Connection GATE-CHIRALITY — Selection Deep Dive

**Date:** 2026-06-04
**Type:** deep-dive / selection analysis (Phase 5 of the √2-centered diagonal build)
**Claim type:** meta
**Status authority:** independent audit lane only. This note sets no audit
status, promotes no row, modifies no axiom, and introduces no import. It
records a finite linear-algebra analysis of a *selection* question and reaches
an honest **AVAILABLE-NOT-FORCED** verdict.
**Primary runner:** [`scripts/diagonal_gate_chirality_selection_deep_dive.py`](../scripts/diagonal_gate_chirality_selection_deep_dive.py)
(SUMMARY: PASS=45 FAIL=0).
**Cached log:** [`logs/runner-cache/diagonal_gate_chirality_selection_deep_dive.txt`](../logs/runner-cache/diagonal_gate_chirality_selection_deep_dive.txt)

> **Discipline up front.** This note does **not** claim the retained chirality
> no-go is broken. The no-go
> ([`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md))
> is **correct on its scope**: circulant / `C_3`-equivariant Hermitian
> operators cannot anti-commute with the canonical `Z_3` character grading
> `Γ_χ = (2/3)J − I`. Our finding is narrower and complementary: the operator
> **class** reachable once the lattice admits face-diagonal adjacency is
> **wider** than circulant, so the no-go does not cover all of it — and the
> residual question is **selection**: does any framework-native principle
> *select* the non-circulant (chirality-admitting) operator? The answer
> reached here is **no, not forced**.

## §0. Context and the precise question

The √2-centered diagonal-connection thought experiment
([`DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04`](DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md))
extends the Lattice axiom's adjacency from nearest-neighbor (NN) to include
face-diagonals (Euclidean length `√2`). Its scout **S3** observed that a single
(non-`C_3`-symmetric) face-diagonal coupling `H = pair(0,1)` admits a `Z_2`
grading `Γ` with `Γ² = I`, `{H, Γ} = 0`, while `[H, R] ≠ 0` (`R` = `C_3`
shift) — placing it **outside** the no-go's circulant scope. The scout left
explicitly open:

> Whether dynamics *selects* a single non-circulant coupling versus a symmetric
> combination — which would be circulant again, back inside the no-go — is a
> separate open question.

This note is that deep dive. The crux is the **selection** question. We map the
operator class precisely, re-confirm the no-go on its (circulant) domain,
verify chirality availability on the wider class, surface a **readout
subtlety** that the scout's bare statement hides, and test four explicit
selection principles for whether any **forces** the non-circulant choice.

All objects (`Γ_χ`, the Koide `Q = 2/3` readout, the `C_3` shift `R`, the
hw=1 generation orbit) are framework objects already on `main`; nothing new is
imported.

## §1. Operator-class decomposition (runner Part A)

The generation factor is `R³` (the hw=1 BZ-corner orbit
`{(1,0,0),(0,1,0),(0,0,1)}`,
[`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)).
Hermitian mass operators on it live in `Sym(3, R)`:

| subspace | dimension | role |
|---|---|---|
| `Sym(3, R)` (all real-symmetric) | 6 | full Hermitian mass-operator space |
| circulant-symmetric `aI + b(R+R²)`, real `b` | 2 | **the no-go DOMAIN** |
| Hermitian circulant Brannen `aI + bC + b̄C²`, complex `b` | 3 over `R` | adds the `i(C−C²)` phase direction |
| non-circulant complement | 4 (= 6 − 2) | **where a chirality grading can live** |

The no-go applies to the 2-dim (real-`b`) circulant-symmetric subspace and,
via `Γ_χ`'s circulant membership, to the full circulant algebra `⟨I, R, R²⟩`.
The face-diagonal class adds the **non-circulant** directions: this is the
precise sense in which the class is "wider than the no-go's domain."

## §2. No-go re-confirmation + complementarity (runner Part B)

`Γ_χ = (2/3)J − I` has spectrum `{+1, −1, −1}` and is **itself circulant**
(`[Γ_χ, R] = 0`). That is exactly *why* a circulant `H` commutes with it, so
`{H, Γ_χ} = 2 H Γ_χ` and anti-commutation forces `H Γ_χ = 0`, hence (by `Z_3`
Fourier invertibility) `H = 0`. The runner re-confirms this two ways:

- **Monte-Carlo:** over 5000 random circulant Hermitian `H`, the minimum of
  `|{H, Γ_χ}| / |H|` is `2.0` (bounded away from 0) — the no-go holds.
- **Exact null space:** the family of Hermitian `H` with `{H, Γ_χ} = 0` is
  **exactly 2-dimensional** (matching the L4 theorem's `Σh = 0` family,
  [`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)),
  and it is **entirely non-circulant** (its overlap with the circulant
  subspace is `< 1e-15`).

**Complementarity.** The no-go ("circulant cannot anti-commute") and L4
("anti-commuting ⇒ `Q = 2/3`") are two faces of **one** fact: the
`Q = 2/3`-producing anti-commuting operators are *exactly* the non-circulant
ones; circulant operators never anti-commute with `Γ_χ`. So chirality, if it is
to give `Q = 2/3` by the L4 mechanism, **must** be carried by a non-circulant
operator.

## §3. Chirality availability on the face-diagonal class (runner Part C)

Re-verifying scout S3: the single face-diagonal coupling `H = pair(0,1)`
- admits the `Z_2` grading `Γ = diag(1, −1, 1)` with `Γ² = I`, `{H, Γ} = 0`;
- is non-`C_3`-equivariant (`|[H, R]| = 2 ≠ 0`);
- is non-circulant.

So a `Z_2` chirality grading **is available** on the wider face-diagonal class.
The scout fact stands. **But it does not yet say which `Q` results, nor which
grading** — and that is where the subtlety lives.

## §4. The readout subtlety — the available grading is **not** `Γ_χ` (runner Part D)

This is the heart of the deep dive, and it sharpens the scout's bare statement.
The grading available on the face-diagonal coupling is `Γ = diag(1, −1, 1)`,
which is **not** the canonical `Γ_χ`:

- `diag(1, −1, 1)` has spectrum `{+1, +1, −1}`; `Γ_χ` has spectrum
  `{+1, −1, −1}`. Different operators, different eigenvalue split.
- The single face-diagonal `H` does **not** anti-commute with the canonical
  `Γ_χ` (`|{H, Γ_χ}| / |H| = 1.76 ≠ 0`).
- The Koide `Q = 2/3` derivation theorem (L4) is **welded to `Γ_χ`** via the
  trace identity `⟨v|Γ_χ|v⟩ = (2/3)(Σv)² − Σv² = 0 ⟺ Q(v) = 2/3`. Against the
  *available* grading `diag(1, −1, 1)`, the nonzero eigenvector of `H` gives
  Koide `Q = 1/2`, **not** `2/3`. (The other eigenvector has `Σv = 0`, so its
  Koide ratio is undefined.)

**Structural obstruction.** The `Γ_χ`-anti-commuting (L4) family has the form
`H = (1/3)(1⊗h + h⊗1)` with `Σh = 0`, whose **diagonal** is `H_ii = 2h_i/3`. A
pure face-diagonal coupling is **off-diagonal**, so it lies in the L4 family
only if `h = 0`, i.e. `H = 0`. Therefore **no nonzero pure face-diagonal
coupling anti-commutes with `Γ_χ`** — the grading that the Koide value requires
is unreachable from face-diagonal couplings alone.

## §5. Two different, incompatible `Q = 2/3` operators (runner Part E)

The foundation reaches `Q = 2/3` in **two** places — and they are **different
operators in mutually exclusive classes**:

| route | operator | relation to `Γ_χ` | `Q = 2/3` source |
|---|---|---|---|
| Brannen `r = 1/2` (scout S4) | circulant `Y = aI + bC + b̄C²`, `r = 1/2` | **commutes** (`comm = 0`) | eigenvalue spectrum `{2.41, 0.29, 0.29}` |
| L4 chirality | non-circulant `H`, `{H, Γ_χ} = 0` | **anti-commutes** (`anti = 0`) | eigenvector expectation `⟨v\|Γ_χ\|v⟩ = 0` |

Crucially, the **Brannen `r = 1/2` operator carries no chirality at all**: it is
circulant and *commutes* with `Γ_χ`; its `Q = 2/3` comes purely from the
`√2`-set eigenvalue ratio (scout S4), with no anti-commutation anywhere. The
two operators cannot be the same object — one commutes and one anti-commutes
with the same `Γ_χ`.

**Consequence for the build's narrative.** The face-diagonal length `√2`
supplies the Brannen `r = 1/2` (circulant) operator — the S4 datum — but that
operator is **not** the chirality-admitting one (S3). S3 and S4 are reached by
*different* operator classes. So "one structural change touches both gates" is
true at the level of the adjacency change, but the **chirality value** and the
**`r = 1/2` value** are not delivered by a single operator; the chirality grading
available on the face-diagonal class does not itself produce `Q = 2/3`.

This is consistent with — and independent corroboration of — the sibling
correction
[`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04`](KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md),
which finds the determinant-modulus / chirality route gives `r = 1` (not
`1/2`), i.e. chirality and the modulus `r` are separate questions.

## §6. The four selection principles + forcing analysis (runner Part F)

For each candidate selection principle we tabulate: circulant? / a
`Z_2`-grading that anti-commutes / the anti-norm against `Γ_χ` / the
eigenvector Koide `Q` / the Brannen eigenvalue Koide `Q`.

| principle | circulant | `Z_2` grading | anti vs `Γ_χ` | eigvec `Q` | eigval `Q` |
|---|---|---|---|---|---|
| **P1** `C_3`-symmetric sum `Σ pair` | yes | none | 2.000 | 1/3 | ∞ |
| **P2** single direction `pair(0,1)` | no | `diag(1,−1,1)` | 1.764 | **1/2** | ∞ |
| **P3** parity-graded `pair(0,1)+pair(1,2)` | no | `diag(1,−1,1)` | 1.886 | 0.343 | ∞ |
| **P4** weak-parity-aligned `ε = (−1)^{x+y+z}` | — | `−I` on orbit (trivial) | — | — | — |
| (ref) **S4** Brannen `r = 1/2` circulant | yes | none | 2.000 | 1/3 | **2/3** |

Reading the table:

- **P1 (`C_3`-symmetric).** The symmetric sum over the three face-diagonals is
  `J − I`, **circulant** — back inside the no-go scope. It **commutes** with
  `Γ_χ` (no chirality), and its eigenvalue Koide is `∞` (degenerate `λ = −1`
  doublet, `λ = 2` singlet). `C_3`-symmetric dynamics selects the
  **chirality-free** operator. ✗
- **P2 (single direction).** Non-circulant, chirality available, but gives the
  **wrong** Koide value (`1/2`) against the wrong grading; does not
  anti-commute with `Γ_χ`. ✗
- **P3 (parity-graded combination).** Non-circulant, admits `diag(1,−1,1)`, but
  again not `Γ_χ`; off-`Γ_χ`. ✗
- **P4 (weak-parity-aligned).** The framework-native parity `ε = (−1)^{x+y+z}`
  is **uniform `−1`** on the hw=1 orbit (all three sites have `x+y+z = 1`,
  odd). Restricted to the generation triplet it is **`−I`** — proportional to
  the identity — so it commutes with everything and **cannot** serve as a
  nontrivial `Z_2` chirality grading on `R³`. The weak-parity grading of
  PR #2685 (one chirality `ε` underlying both weak parity violation and the
  flavor phase) therefore **does not transport** to a generation-factor `Γ`:
  `ε` lives on the spacetime/site factor and acts `C_3`-trivially on the
  generation orbit. ✗

**Is the non-circulant selection forced by any lattice-native principle?**

- The cubic point group `O_h` permutes the **12** face-diagonal directions of
  the unit cube **transitively** — no single face-diagonal is distinguished, so
  the single-direction (P2) selection is a **choice**, not lattice-forced.
- **Body-diagonals** (squared distance 3) do **not** connect the generation
  orbit (all hw=1 pairs are face-diagonal, squared distance 2), so the
  body-diagonal extension adds nothing to this gate.
- The **counting-vs-splitting tension** reappears unchanged: the `C_3` orbit
  that supplies the generation **count** (3) forces any orbit-respecting
  operator to be **circulant** (commuting with `Γ_χ`, `Q = 1`-type), while the
  chirality **splitting** needs a non-circulant, `C_3`-breaking operator. The
  same `C_3` cannot do both.

No framework-native principle examined here **forces** the non-circulant
(chirality-admitting) selection.

## Verdict — **AVAILABLE-NOT-FORCED**

Face-diagonal adjacency **widens** the generation-factor operator class beyond
the no-go's circulant scope, making a `Z_2` chirality grading **available**
(scout S3, re-verified). But:

1. **no framework-native principle forces** the non-circulant selection
   (`O_h` permutes face-diagonals transitively; `C_3`-symmetry selects
   circulant; weak-parity is uniform `−I` on the generation orbit);
2. the grading actually **available** (`diag(1,−1,1)`) is **not** the canonical
   `Γ_χ` the Koide `Q = 2/3` readout requires — its eigenvector gives `Q = 1/2`,
   and no pure face-diagonal coupling can anti-commute with `Γ_χ` (a structural
   diagonal-content obstruction);
3. the operator that **does** give Brannen `Q = 2/3` (`r = 1/2`, scout S4) is
   **circulant**, **commutes** with `Γ_χ`, and carries **no chirality** —
   `r = 1/2` and chirality are reached by different, incompatible operators;
4. the **counting-vs-splitting tension** is unchanged.

The selection gate is the **same `C_3`-orbit-splitting gate** as the prior
attacks (the generation-ID chirality gate), now **precisely relocated** onto
the face-diagonal class — **not** closed. This is the honest stop: face-diagonal
makes chirality *available*, but the *selection* remains the same open gate.

The path this opens (not a closure, a direction): the gate now has a sharp
algebraic shape — find a framework-native, `C_3`-orbit-splitting principle that
(a) prefers a non-circulant generation operator and (b) lands it specifically in
the `Γ_χ`-anti-commuting (diagonal-content-carrying) family, not merely in some
off-circulant direction. Candidate directions left untouched here: a holomorphic
/ Kähler measure on the complex doublet `b` (couples to the phase `δ = arg b`);
a Record/KMS-modular selection on the generation factor; and any mechanism that
supplies the diagonal content `2h/3` from substrate data rather than from a
chosen coupling.

## What this note does NOT do

- It does **not** modify any axiom (`MINIMAL_AXIOMS_2026-06-04.md` untouched).
- It does **not** claim the chirality no-go is broken. The no-go is correct on
  its circulant scope; the finding is the class is wider and the **selection**
  is open.
- It does **not** claim chirality is derived, nor that `Q = 2/3` is closed.
- It does **not** set audit status, promote any row, or introduce any import.
  `Γ_χ`, the Koide readout, `R`, and the hw=1 orbit are all framework objects
  already on `main`.

## Cross-references

- [`DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md`](DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md)
  — the foundation; scouts S1–S4.
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
  — the chirality no-go (circulant scope); correct, not contradicted here.
- [`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)
  — `{H, Γ_χ} = 0 ⇒ Q = 2/3` (welded to `Γ_χ`).
- [`KOIDE_LIGHTCONE_PRIMITIVE_THEOREM_NOTE_2026-05-10.md`](KOIDE_LIGHTCONE_PRIMITIVE_THEOREM_NOTE_2026-05-10.md)
  — circulant-basis lightcone primitive.
- [`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)
  — the hw=1 generation orbit.
- [`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md`](KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md)
  — sibling correction: chirality/modulus route gives `r = 1`, corroborating
  that chirality and `r` are separate.
- PR #2685 (CLOSED) "one chirality grading underlies both weak parity violation
  and the flavor phase" — its `ε = (−1)^{x+y+z}` is the weak-parity grading
  tested in §6 P4; it acts `C_3`-trivially on the generation orbit and does not
  transport to a generation-factor `Γ`.
