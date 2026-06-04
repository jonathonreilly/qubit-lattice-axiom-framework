# Flavor Doublet Complex Structure J Exists on the Generation Factor

**Date:** 2026-06-04
**Claim type:** positive_theorem
**Claim scope:** on the real generation factor `R[Z3]`, the operator
`J = (C - C^T)/sqrt(3)` is a C3-equivariant antisymmetric complex
structure on the two-dimensional doublet, vanishes on the all-ones
singlet, and commutes with every circulant mass operator. This proves
the holomorphic-readout scaffolding exists and is distinct from the
anticommuting grading object. It is not a value derivation, does not
select `Q=2/3`, and does not close a strong-CP theorem.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade. It does not edit, re-cite, or promote any existing row.
**Runner:** `scripts/flavor_split_the_brick_doublet_complex_structure_2026_06_04.py` (SCORECARD 7/7).

## The reframe
A reconnaissance warm-up (assumptions / first-principles / literature / mathematics / semantics, with a
citation-integrity pass) separated a previously conflated phrase,
"chiral/holomorphic grading on the generation `R^3` factor", into
different mathematical jobs. This note proves only the job it can
support: the commuting doublet complex structure exists. The strong-CP
and readout-selector comments below are orientation, not theorem closure.

## The positive theorem — the doublet complex structure exists
On the generation factor `R[Z₃] = ℝ ⊕ ℂ`, define
```
J = (C − Cᵀ)/√3 = (C − C²)/√3 .
```
Verified (runner 7/7):
- `J` is **antisymmetric** (`Jᵀ=−J`) with `eig(J)={0, +i, −i}`;
- `J² = −I` on the **2-dim doublet** and `0` on the **all-ones singlet** — an **almost-contact** structure
  (a genuine complex structure on the doublet distribution; the all-ones vector is the real "Reeb" axis).
  This is the *odd-dim-correct* substitute for the (nonexistent) global `J` on `R³`;
- `J` is **C₃-equivariant** (`[J,C]=0`);
- `J` **commutes** with every circulant mass operator `H = aI + bC + b̄C²` (`[J,H]=0`, `{J,H}≠0`).

So `J` is a **holomorphic-readout** object — *not* an anticommuting chiral grading. It lives entirely
**outside** both obstructions that made "the brick" look hard:
- the **odd-dim wall** (no `J²=−1` on `R³`): `J` lives on the *even-dim* doublet, with the singlet as the
  real Reeb axis — no global-`J`-on-`R³` is needed or claimed;
- the **retained anticommuting no-go**
  [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md):
  that no-go forbids a C3-equivariant anticommuting object; `J`
  commutes with `H`, so the no-go is not the obstruction to this
  commuting complex structure.

## Two objects, not one
The no-go's `Γ_χ = (2/3)J_allones − I` (eig `{1,−1,−1}`, `Γ_χ²=I`) is a **different** object: it too
**commutes** with every circulant `H` (so it never graded `H` chirally), and `Γ_χ ≠ J`. The "brick" framing
**conflated** the commuting holomorphic `J` (which exists) with a (non-existent) anticommuting grading —
importing the worst obstruction onto a problem that does not have it. "Generation chirality" has no lab
referent (e/μ/τ are not L/R partners); the borrowed word, not the physics, created the obstruction.

## Strong-CP Orientation (Not Closed Here)
The strong-CP reality antiunitary is a **spacetime/Dirac ε-grading** object (`εD + Dε = 0` on the
spacetime factor), C₃-trivial on the generation index — **not** a generation-factor structure (the
framework's strong-CP runners and Nelson-Barr / Vecchi-style templates
locate that style of reality structure on spacetime+fields). This note
does not prove a strong-CP result. It only verifies that the generation
factor carries no nonzero circulant operator anticommuting with
`Gamma_chi`, consistent with keeping the strong-CP problem separate from
the commuting doublet `J`.

## The corrected map and the sole residual
The "one brick, three gates" picture is replaced by:
- **strong-CP** = a separate spacetime/field reality-structure problem,
  not closed here;
- **Koide scaffolding / generation-orientation algebra** = the doublet
  `J` proved here;
- **value selection** = a still-open discrete readout choice:
  signed/`det_C` (`r=1/2`, `Q=2/3`) versus unsigned/`det_R`
  (`r=1`, `Q=1`).

**Honest boundary:** `J` is necessary scaffolding but **not sufficient** — it does *not* pin
`|b|²/a² = 1/2`. Both readings sit on the *same* `J`; the value is the one discrete readout bit. So the
prize is no longer "build a chiral grading" (mis-posed, obstructed) — it is the sharp, well-isolated
question: is the Record-compatible additive scalar readout rule
sign-sensitive (signed/`det_C`, `Q=2/3`) or sign-blind
(Born/`det_R`, `Q=1`)? That is a follow-on selector question, not an
axiom change made by this note.

## Literature Context (Non-Load-Bearing)
- Nelson-Barr (arXiv:2203.09002, 2010.02891): θ̄=0 from a spontaneously-broken reality structure with
  calculable `arg det M` — the template for the decoupled strong-CP half.
- Connes NCG SM (hep-th/0705.0489): the chiral grading sits on the L/R qubit factor with generations as a
  trivial 3-fold multiplicity — independently mirrors "γ inert on generations."
- Non-holomorphic modular flavor (arXiv:2406.02527): holomorphy is *optional* (real models fit lepton
  data) — corroborates "signed/`det_C` vs real/`det_R` is a free measure choice," i.e. the residual bit.

## The next paths this opens (not closing)
- **The residual bit:** is the Record-compatible readout rule
  sign-sensitive?
- **Strong-CP:** a native, no-new-fields Nelson-Barr-type reality
  structure on spacetime+fields remains a separate problem.

## Provenance (verified 2026-06-04)
- `J` antisymmetric, `eig(J)={0,±i}`, `J²=−I` on doublet / `0` on singlet, `[J,C]=0`, `[J,H]=0` with
  `{J,H}≠0`; `Γ_χ` commutes with `H` and `Γ_χ≠J`; no circulant anticommutes with `Γ_χ`: verified directly
  (runner 7/7). The retained anchor
  [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
  forbids an anticommuting object; this note uses the commuting-object /
  even-dimensional-doublet escape rather than contradicting that no-go.
- This note sets no audit status; it proves the doublet complex structure, splits the conflated brick into
  separate jobs, and isolates the discrete readout residual.
