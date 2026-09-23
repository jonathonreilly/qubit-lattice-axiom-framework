# J:derive:what-fixes-gamma-if-not-the-sea:a2

Worker `w-macbookpro90c72-j952b` (claude-opus-5-5). This is attempt 2 of 2. No earlier attempt's files exist on `ai/probes`.

**Overlap, disclosed.** This session's `J:derive:normal-ordering-as-a-rule:a2` (#8761) found that the sea's induced coupling is exactly `12/|c₀|` with the per-site counter-term, and that there is no long-wavelength stiffness with the per-bond one. That result is used here, and recomputed.

Sources: blocks 53–78 (open PRs listed in the unit) and the decision record #8572 (DECISION_RECORD and FORK_PROBE files). Rows cited below are the decision record's.

## (1) Exact statement

### (a) The pure numbers of the rate/length sector, and every relation the clauses produce

| number | enters in | relation produced |
|---|---|---|
| `γ` (coupling) | block 55 (row 10) | pure number by A + C (weight one); block 56's member `(2/γ)Σ(φ_x−φ_y)²`; saturation `12/(γg₀) = 7.9/γ` (row 13); `18/γ` for another admissible member (row 15) |
| `κ` (a record's rate ratio) | block 53 | `log κ = −(γ/6)E/w̄` if records are pulled as amplitudes are (block 55 corollary) |
| order `p` of the clock law's second order | block 53 | fixed to the averaging law for `√w` (`p = 1/2`) by A + C: block 55 T4(d) |
| `c` (kinetic, differences of rates' rates of change) | block 57 (row 17) | none; nothing travels |
| `β`, three numbers of a bond law | block 59 (row 19) | `β = a/(2(ap−b))`; `β = 1/p` for bilinear members (block 60) |
| `K`; `p = 1`, `s = 3`, `c_k = −6K`, `c₀ = 0` (lengths) | block 60 (rows 20–22) | `γ = 1/(4K)` for the curvature member; `p`, `s` and the sign of `c_k` are declared |
| `α`, `β_kin` (kinetic numbers of the frame) | block 62 (row 25) | `α = K/4` puts the ripples at the walker's top speed (not forced); the isotropic stretch has kinetic coefficient `12α + 36β_kin`; a closed lattice with content moves iff `β_kin < −α/3` |
| `α`, `β` (collinear/perpendicular split of block 59's stiffness) | rows 51, 55, 56 | sea-reading thresholds `α + 2β < χ/12 = 0.128`, `β < χ_a/72 = 0.026`; the split itself is not fixed |
| `a₀`, `a` (scalar hop), staggered `m` | block 77 | `a₀` shifts energies; `a` splits the species 1:3:3:1; `m` is a rest term; all free |
| binding scale `c₀ = 6/(p+q+4r)` (record layer) | block 40 | pinned at the neutral value by the likelihood-ratio reading (supplied) |
| the sea's `c₀ = −1.193801121` and stiffness `κ_sea` | block 76 | `κ_sea = |c₀|/12` exactly (#8761); `γ_ind = 12/|c₀|` with the per-site counter-term; no stiffness with the per-bond one |
| units: `w = 1`; the walk's coefficient 1; lattice spacing = natural unit | blocks 53, 54 | the top speed is exactly 1 at `w = 1` (A1); "spacing = natural unit" is an open gate |

### (b) What fixes each number

- **Fixed by a supplied clause:**
  - the member (block 56 T5's principle, or per-tick counting and frame blindness, which fix the curvature member and `p = 1`);
  - `c₀` of the record layer (the likelihood-ratio reading);
  - `β = 1` (the curvature member);
  - `γ = 12/|c₀|`, only under the sea reading with the per-site counter-term. That counter-term is itself supplied, and it gives the half-bending member.
- **Fixed by an identity:**
  - `p = 1/2` in the second-order clock law (A + C);
  - `γ = 1/(4K)` (the curvature member at second order; **A3**);
  - `log κ = −(γ/6)E/w̄` (under the record-pull reading);
  - `κ_sea = |c₀|/12` (#8761).
- **Fixed by nothing:**
  - `γ` itself, in A, B, C;
  - `K`;
  - `α`, `β_kin`;
  - the collinear/perpendicular split;
  - `a₀`, `a`, `m`;
  - the kinetic `c` of block 57.

  The sea does not fix `K`: it gives the clock a `u·u` stiffness, which the curvature member has no term for (block 60 T3(a)). The lengths' stiffness it induces is about 0.003 per `q²` (block 76 W2).

### (c) Comparator only; nothing is adopted

Packets fall at `−∇u` (block 54), and `Δu = γe` (block 55). Read against Newton's `ΔΦ = 4πGρ`, this is `γ = 4πG` in lattice units (`ħ = c = a = 1`), so `a/ℓ_P = √(4π/γ)`:
- `γ = 12/|c₀|` gives `a = 1.118 ℓ_P`;
- block 76's 10.51 gives `1.094 ℓ_P`.

But the half-bending member gives only half the comparator's light bending. For the curvature member, `γ = 1/(4K)` gives `a/ℓ_P = √(16πK)`: of order one iff `K ~ 1/(16π) = 0.0199`. The saturation is `12/(γg₀)`: 0.787 or 0.753.

### (d) Consistency conditions: none fixes `γ` or `K`

- The walker's top speed at `w = 1` is exactly 1: `1 − |∇ε|² = Σ sin⁴k / Σ sin²k` (A1).
- Every travelling speed of a field energy quadratic in its coefficients is a ratio. This includes block 62's ripples, `ω² = Kq²/(4α)`, and the isotropic stretch.
- Scaling `(K, α, β_kin) → λ(K, α, β_kin)` leaves every speed unchanged but sends `γ = 1/(4K)` to `γ/λ`. So matching speeds (ripples at the walker's top speed) fixes `α = K/4`, a ratio, and nothing else (A2).
- The fall law uses `w = 1` only as the unit of rate; `γ` scales it.

Only an inhomogeneous condition can fix the scale: one that ties the field's energy to the content's. The sea's induced energy is one. Nothing else in blocks 53–78 is.

**The unit's HIT condition — a supplied clause other than the sea fixes `γ` or `K` — is not met.**

## (2) Steps

1. **PROVED (A1).** `1 − |∇ε|² = Σ sin⁴k/Σ sin²k ≥ 0`, with the limit 1 along an axis as `k → 0`; sympy.
2. **PROVED (A2).** Homogeneity: sympy checks both dispersion forms under the scaling, and `α = K/4` is the only solution of `ω² = q²`.
3. **CHECKED (A3, exact).** Block 60's per-tick member `Kℓ(4Δλ + 2q)`, with a unit body at rest on a ring of 5, first order in a bookkeeping parameter, with the unit of rate held by a multiplier (block 55 T4(b)). This gives `Δu = (1/(4K))(e − ē)`, which is block 55's law with `γ = 1/(4K)`.
4. **CHECKED (A4, floating point).** `c₀ = −1.193801121` from midpoint sums up to `256³`; `γ = 12/|c₀| = 10.0519`.
5. **CHECKED (A5).** Watson's `g₀` in closed form, and the comparator numbers.
6. **SOURCED (the table).** From the decision record's rows and the block notes as cited. The table is a reading of the notes, not a computation.

### ASSUMED

Only the notes' statements as quoted.

## (3) Where the route fails

**The first failing step is that the scale of the field energy is not fixed.**
- A, B and C, and the per-tick and frame clauses, all leave the field energy's scale free.
- Every consistency condition found in the lane is homogeneous in the field numbers.
- Block 60's identity only trades `γ` for `K`.

The sea reading breaks the homogeneity and fixes `γ`. But it does so in the wrong member, and only under a supplied localisation of the counter-term (per-site, `12/|c₀|`; per-bond gives no stiffness).

## (4) What would finish it

- An inhomogeneous clause tying `F`'s scale to the content's energy. Two candidates: an induced (sea) energy in the curvature member, or a principle like "the field's energy per tick equals the vacuum's energy per tick".
- Or accepting `K` (equivalently the lattice spacing in Planck units) as the lane's one free number: fork 8.
