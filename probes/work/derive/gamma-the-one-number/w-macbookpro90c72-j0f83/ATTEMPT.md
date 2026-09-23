# J:derive:gamma-the-one-number:a2: nothing in the clauses of blocks 53–55 fixes γ

**Provenance.**
- Worker `w-macbookpro90c72-j0f83`, model `claude-opus-5-5`, one session. Attempt 2 of 3; there are no prior attempts in the worktree.
- **Related earlier unit.** The same model did `J:derive:kappa-from-the-rule:a2` (issue #8699, unrefereed): block 50's clock with isolated `κ = 1`, and equal pulls giving `log κ = −(γ/6)E_rec`, with nothing fixing `γ`. It is not used as authority here.
- **Sources.**
  - Blocks 53–55 as the task restates them.
  - The scale-reference primitive's text on main (`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`).
  - The claim scopes of blocks 39–55 on their branches, surveyed for forced numbers.
- The statistical postulate is neither assumed nor raised. Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**(a) The point body and its self-consistency (PROVED; CHECKED G.a, G.self, G.sat).**
- **The solution.** For `F = (2/γ)Σ_bonds(φ_x − φ_y)²`, the law is `(12/γ)φ_x(φ_x − avg φ) = −e_x`, with `μ = 0` because the walls are held at the ambient rate. A body of bare rest energy `m` at one site has `e_0 = mφ_0²`. Dividing by `φ_x` makes the law linear, `(12/γ)(φ_x − avg φ) = −mφ_0 δ_{x0}`, so:
  - `φ = 1 − (γ/12)mφ_0 G₀(·, 0)`, with `G₀` the inverse of `1 − avg` with zero walls;
  - `φ_0 = 1/(1 + x)`, with `x = (γ/12)G₀(0)m`;
  - every neighbour of the body sits at exactly `φ_0(1 + γm/12)`, since `G₀(e) = G₀(0) − 1`.
- **Saturation.** The energy seen from afar, `mφ_0`, tends to `12/(γG₀(0))`.
- **Exact values.** `G₀(0) = 1`, `22/17`, `136/99` on boxes of side 1, 3, 5.
- **The proposed self-consistency.** The record's tick ratio from the field is `κ = φ_0²/φ_nbr² = (1 + γm/12)⁻²`.
  - **Reading κ off the field** is an identity: it defines `κ` and carries no condition.
  - **Equating κ with the site's own rate** `w_0 = e^{u_0} = φ_0² = (1 + x)⁻²` requires `γm/12 = x`, i.e. `G₀(0) = 1` or `m = 0`.
  - `G₀(0) = 1` exactly when the body's neighbours are the walls (the side-1 box). There it is an identity for every `γm`.
  - In every larger box `G₀(0) > 1`, and there is **no solution with `m > 0`**.
  - So it is **never a condition that fixes `γm`**.

**(b) The scale reference (PROVED from its text).**
- The primitive declares `a⁻¹ = M_Pl`, "a units conversion", with "zero dimensionless content". It explicitly does **not** assert `a/l_P = 1`: that "self-consistency question … remains a separate open gravity derivation".
- `γ` is a pure number. `γ/(4π)` plays the comparator's constant in lattice units, with energies counted in ambient ticks.
- Reading `γ` from the primitive means taking `G_lattice = G_N` in Planck units, i.e. `G = a²`, i.e. `γ = 4π`. That is exactly the statement `a = l_P`, the open derivation the primitive disclaims.
- **The circle.** The primitive's choice of `M_Pl` as the ruler would be justified by `γ = 4π`, and cannot be its source. By its own declaration it supplies no dimensionless quantity.

**(c) Every forced pure number in blocks 39–55, and why none is `γ` (PROVED, structural).**
- **Survey of the claim scopes.** The forced numbers of order one fall into three kinds:
  1. **Ratios of the clauses' own weights:** block 39's `c₀ = 6/(p + q + 4r)`, and related fractions (`11/12`, `13/12`, `3/10`).
  2. **Geometric and transport coefficients of the record gas:**
     - `4π`, `8π`, `16π` solid-angle factors (blocks 43, 45, 47–49);
     - `9/4` (blocks 48, 49);
     - `2/9`, `2/45` (block 45);
     - `√3/2` (block 47);
     - `√3/16` and `70/2187` (block 51);
     - `1/3` and `√3/6` (block 52).
  3. **Lattice-operator constants:** block 53's `1/6` (the averaging law, and `(p − 1)/6` at second order); block 55's `12` in `12/γ`, the power-mean order `1/2`, and T2(c)'s example energies `5/4`, `3/4`.
- **The argument.** The objects of blocks 39–54 (records, the formation and transport clauses, the rate rule, the walk) contain no field energy `F`. So their forced numbers are independent of how much field energy is booked per unit of stiffness. `γ` is exactly that weight: the relative weight of `F` against `⟨H_w⟩` in block 55's ledger.
- **The consequence.** Identifying `γ` with any of those numbers needs a clause coupling `F`'s normalisation to that object, and no such clause exists. Without one, the identification is numerology.
- **Block 55 itself.** Its law and kept ledger are consistent for every `γ > 0`. CHECKED: the solved field is a stationary point of `m w_0 + (2/γ)Σ(φ_x − φ_y)²` at two unrelated `γ`'s. So `γ` labels a family of consistent (law, ledger) pairs, and nothing in blocks 53–55 selects a member.

**Conclusion.** Nothing in the present clauses fixes `γ`. It stays a declared pure number.

## 2. Steps

**S1 (PROVED; CHECKED G.a). The point body.**
- **Setup.** The box is the interior of side `n` with walls at `φ = 1`. The divided law is linear, with the body row `(12/γ)(φ_0 − avg φ) + mφ_0 = 0` and harmonic rows elsewhere.
- **The solution.** With `(1 − avg)G₀ = δ₀` and `G₀ = 0` on the walls, `φ = 1 − (γm/12)φ_0 G₀`. At the body this gives `φ_0 = 1/(1 + x)`.
- **The neighbours.** The box is symmetric about the body, and `G₀(0) − avg G₀(nbr) = 1`, so `G₀(nbr) = G₀(0) − 1` and `φ_nbr = φ_0 + (γm/12)φ_0`.
- **CHECKED** in exact rationals on sides 1, 3, 5 with two `(γ, m)` pairs each:
  - the solution;
  - the undivided law at every site;
  - the neighbour values;
  - `G₀(0) = 1, 22/17, 136/99`.

**S2 (PROVED; CHECKED G.self).**
- `κ = (1 + γm/12)⁻²` symbolically.
- `κ = φ_0²` reduces to `(1 + γm/12) = (1 + γG₀(0)m/12)`, i.e. `m(G₀(0) − 1) = 0`.
- With `m > 0` there is no solution unless `G₀(0) = 1`, which on the side-1 box holds identically.
- The other root, `1 + γm/12 = −(1 + x)`, has `m < 0`.

**S3 (PROVED; CHECKED G.sat).**
- **Saturation.** `lim_{m→∞} m/(1 + (γ/12)G₀(0)m) = 12/(γG₀(0))`.
- **Stationarity.** `∂/∂φ_i [m φ_0² + (2/γ)Σ_bonds(φ_x − φ_y)²] = 2mφ_0δ_{i0} + (24/γ)(φ_i − avg φ)`, whose zero set is the divided law. CHECKED at `γ = 1` and `9/4` on the side-3 box, with wall bonds counted with multiplicity.

**S4 (PROVED). The scale reference.** As in §1(b), from the primitive's own text.

**S5 (PROVED, structural). Forced numbers.** As in §1(c). The list was read from the blocks' claim scopes; the argument does not depend on its completeness.

## 3. The first failing step

The route "fix `γ` by self-consistency" fails at S2. Equating the record's tick ratio with its own rate is an identity or has no solution with `m > 0`, so it never pins `γm`. The route "read `γ` from the scale reference" fails at S4, by circularity.

## 4. What would finish it

1. **A clause tying `F`'s normalisation to an object with a forced number.** For example: the rate field's stiffness equal to the record gas's own susceptibility (a matching or equipartition clause), or the induced ledger of a sea (block 76's `κ`, a derived stiffness, if the sea were adopted). That would make `γ` derived rather than declared.
2. **A derivation of `a = l_P`** from gravitational self-consistency. It would give `γ = 4π` without circularity.

## 5. Running it

```
python3 probes/work/derive/gamma-the-one-number/w-macbookpro90c72-j0f83/check.py
```

The run takes about 7 s. It prints three exact checks, then the SUMMARY and HIT lines.
