# Referee report: J:derive:gamma-the-one-number:a2

- **Author:** `w-macbookpro90c72-j0f83` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j92a2` (`grok-4.6`). Different model family.
- **Material:** the attempt's `ATTEMPT.md` and `check.py`, and `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` in this checkout.

`check.py` here re-solves the walled cube in exact rationals and reduces the side-3 Green function on four orbits. It does not call the author's script.

## The statement

The task asks whether anything in the clauses of blocks 53–55 fixes the pure number `γ`: a point-body self-consistency, the scale-reference primitive, or a pure number already forced in blocks 39–55. A conclusion that nothing fixes `γ` is a result the task allows.

The attempt says exactly that. The finite part is the point body and the failed self-consistency. The scale reference is read off its own text. The survey of other numbers is structural: `γ` is the weight of the field energy, and those numbers are fixed without it.

## Step by step

**R1 (Green function): holds.** With walls at zero for `G` and `(1 − avg)G = δ` at the centre, `G(0) = 1`, `22/17`, `136/99` on sides 1, 3, 5. The side-3 value is also the solution of the four orbit equations (centre, face, edge, corner), so it does not depend on the site ordering of the full solve.

**R2 (the point body): holds.** Dividing `(12/γ) φ(φ − avg) = −e` by `φ` linearises it. Re-solving that linear system at two `(γ, m)` pairs on each box gives `φ_0 = 1/(1+x)`, `x = (γ/12) G(0) m`, the undivided law at every site, and every neighbour, or the wall, at `φ_0(1 + γm/12)`. The neighbour formula is `G(0) − 1` at each of the six symmetric neighbours, and it does not otherwise depend on `G(0)`.

**R3 (self-consistency): holds, and it fixes nothing.** The tick ratio is `κ = φ_0²/φ_nbr² = (1 + γm/12)⁻²` for every `γ` and `m`. Setting that equal to the site rate `w_0 = φ_0²` is `(1 + γm/12)² = (1 + x)²`. The roots are `m = 0` and `m = −24/(γ(1+G(0)))`. For `m > 0` one needs `G(0) = 1`, which is the side-1 box, and there the equation is an identity for every `γm`. No value of `γm` is selected. The author's sympy check hides the negative root by declaring `m` positive and treats an empty positive solution set as success; the roots above are the full real solution, and they agree with the attempt's prose.

**R4 (the ledger does not select `γ`): holds.** `m φ_0 → 12/(γ G(0))` as `m → ∞`. The gradient of `m φ_0² + (2/γ) Σ (φ_x − φ_y)²` is `(4/γ)` times the sum of bond differences, plus `2m φ_0` at the body. It vanishes on the solved field at unrelated values (`γ = 1` and `9/4` on side 3, `γ = 2` on side 5). The pair (law, ledger) is consistent for every `γ > 0`.

**R5 (the scale reference): holds as a reading of the note.** The primitive says `a^{-1} = M_Pl`, calls that a units conversion with zero dimensionless content, and says it does not assert `a/l_P = 1`; that equality "remains a separate open gravity derivation." The task's own sentence is that `γ/(4π)` plays the comparator's constant in lattice units. Setting that constant to the Planck value is `γ = 4π`, which is `a = l_P`. The primitive disclaims that statement, so it cannot be the source of `γ`. Using it as the source would be circular.

The list of other pure numbers was not re-derived from every block branch. It is not needed. None of the routes the task names — the point-body clock, the scale reference, or the consistency of block 55 — produces a condition on `γ`. A number forced by a clause that does not contain the weight of `F` becomes `γ` only by an extra identification, which is the numerology the task excludes.

## Verdict

The partial result survives. Nothing checked here fixes `γ`.
