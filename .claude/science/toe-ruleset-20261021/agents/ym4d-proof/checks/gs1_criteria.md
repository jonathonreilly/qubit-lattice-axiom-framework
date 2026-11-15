# checks/gs1_criteria.md — pre-registered criteria for check `gs1` (target T55-O)

Written **2026-10-28T21:52Z**, after `GESIGN.md` §1 (PRE-STATED) and **before any line of
`gs1_pc.py`**. Contains **no constant derived in this session**: every criterion below is an exact
identity, an exact zero, or a count, and no threshold is numeric.

## What `gs1` tests, and what it cannot test

`gs1` tests **the operator `𝒫` of BFT_A Lemma PC (§23.1) and three elementary claims about
compactly supported co-closed level-0 1-forms**, in exact integer arithmetic, in `d = 4`, on a lift
large enough that no index wraps.

**It does not test** anything about the actual current
`e := d*G' − (Q_str^{(0→k)})^T J` of Lemma LD, because `Q_str^{(0→k)}` and `𝔽^{(0→k)}` are not
implemented here (scope limit §1.5). Statements about the *actual* `e` in `GESIGN.md` are therefore
derivations, and are labelled as such; `gs1` supports only the operator-level and co-closedness-level
claims that those derivations use. A reader must not read a `gs1` PASS as evidence for the actual
`G_e`.

## Conventions fixed before the script (BFT_A §23.1 l.1872)

`(d*G)_ν(z) = Σ_μ [G_{μν}(z − e_μ) − G_{μν}(z)]`, `(d*e)(z) = Σ_μ [e_μ(z − e_μ) − e_μ(z)]`,
`G_{νμ} = −G_{μν}`.

`𝒫` is implemented exactly as BFT_A §23.1 writes it, including the `[RBA5-fix] U2` sign reading
(BFT_A §27): first axis `a`, `b :=` the largest `z_a` carrying a nonzero `e_ν (ν ≠ a)`,
`S_ν(z) := Σ_{t ≤ z_a} e_ν(t, z')`, `W_ν(z') := Σ_t e_ν(t, z')`,
`G_{aν} := −S_ν + 1[z_a ≥ b] W_ν`, and `G_{μν}(z) := δ_{z_a,b} Γ_{μν}(z')` for `μ, ν ≠ a` with `Γ`
the `(d−1)`-dimensional construction applied to `W`.

Generator: `e := d*G_0` for a pseudo-random compactly supported integer 2-form `G_0` (fixed seed,
recorded in the script). This generates co-closed compactly supported `e` by `(d*)² = 0`; it is
**not** claimed to generate every such `e`, and that limitation is stated here before running.

## Clauses and pre-registered verdicts

**A1 (exactness and support of `𝒫`).** For every trial: `d*(𝒫e) = e` exactly (all components, all
sites), and `supp(𝒫e)` lies inside the bounding cube of `supp e`.
→ **PASS** iff exact and inside, in **every** trial. **FAIL** on any single discrepancy.

**A2 (claim ZS: each component of a compactly supported co-closed 1-form has total sum zero).** For
every trial and every `ν`: `Σ_z e_ν(z) = 0` exactly.
→ **PASS** iff zero in every trial and every component. **FAIL** on any nonzero.

**A3 (claim FM: the signed total of a primitive is the first moment of the current).** For every
trial, every `μ < ν`: `Σ_z (𝒫e)_{μν}(z) = Σ_z z_μ e_ν(z)` exactly; and the matrix
`M_{μν} := Σ_z z_μ e_ν(z)` is exactly antisymmetric.
→ **PASS** iff both hold exactly in every trial. **FAIL** on any discrepancy.

**A4 (primitive-independence of the signed total).** For every trial, `𝒫` is run a second time with
the axis order reversed, producing a different primitive `𝒫'e` (checked to be different as a
function in at least one trial, else A4 is reported **VACUOUS**). Then
`Σ_z (𝒫e)_{μν} = Σ_z (𝒫'e)_{μν}` for every `μ < ν`.
→ **PASS** iff equal in every trial **and** `𝒫'e ≠ 𝒫e` pointwise in at least one trial.
→ **VACUOUS** (reported as a failure of the clause to discriminate) if the two primitives coincide
in every trial.

**A5 (sign coherence of `𝒫e`).** Call `𝒫e` *sign-coherent* if for every `μ < ν` the nonzero values
of `(𝒫e)_{μν}` all have the same sign. Report (i) the count of sign-coherent trials out of `N`, and
(ii) whether the single-plaquette input `e := d*δ_q` yields a sign-coherent primitive.
→ **SIGN-MIXED is recorded** iff at least one trial is not sign-coherent (one counterexample
suffices; this clause is designed so that a single trial can settle it).
→ **SIGN-COHERENT-GENERIC is recorded** iff every trial is sign-coherent.
→ (ii) is reported separately and is **not** part of the verdict: it tests only that sign coherence
is *possible*, which bears on whether a general no-go exists.

**A6 (DESIGNED-FAIL CONTROL — must fire).** Three deliberately invalid inputs:
- **A6a** a compactly supported current `ẽ` that is **not** co-closed (a single `+1` on one link).
  A1's exactness clause and A2 must **FAIL** on it.
- **A6b** a 2-form `G̃` that is **not** a primitive of `e` (`𝒫` applied to a *different* current).
  A3's equality must **FAIL** for it.
- **A6c** the matrix `M̃_{μν} := Σ_z z_μ ẽ_ν(z)` for the non-co-closed `ẽ` of A6a must **FAIL**
  antisymmetry.
→ The control **FIRES** iff all three fail as designed. If any of the three passes, `gs1` is
reported as **having no control**, and clauses A1-A3 are downgraded to "not evidence".

## Honest-status commitment

A FAIL in A1-A5 is reported as a FAIL, the script and output kept unaltered, and any re-run given a
new id with these criteria untouched. Any probe added after reading the output is labelled
**post-hoc** in `GESIGN.md`.
