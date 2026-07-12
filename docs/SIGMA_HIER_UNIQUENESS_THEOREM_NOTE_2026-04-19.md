# σ_hier Uniqueness Theorem

**Date:** 2026-04-19  
**Status:** **supplied-input S_3 selection table** — conditional on three admitted
external inputs (the pinned chamber point, the NuFit 5.3 NO 3σ magnitude windows, and
the T2K/NOvA `sin(δ_CP) < 0` sign preference), `σ_hier = (2, 1, 0)` is the unique
hierarchy-pairing permutation passing the joint 4-observable PMNS filter at the pinned
chamber point  
**Runner:** `scripts/frontier_sigma_hier_uniqueness_theorem.py` ([scripts/frontier_sigma_hier_uniqueness_theorem.py](../scripts/frontier_sigma_hier_uniqueness_theorem.py))
**Runner result:** `PASS = 33, FAIL = 0`

## What this theorem establishes

At the pinned chamber point `(m_*, δ_*, q_+*) = (0.657061, 0.933806,
0.715042)` (supplied by the P3 PMNS-as-f(H) map), the hierarchy pairing
`σ_hier = (2, 1, 0)` is the **unique** element of S_3 satisfying both:

1. **All 9** `|U_PMNS|_{ij}` entries inside the NuFit 5.3 NO 3σ experimental
   ranges.
2. **sin(δ_CP) < 0**, consistent with the T2K/NOvA experimental preference.

This is a supplied-input selection statement, not an internal derivation.
`σ_hier` is not derivable from the `Cl(3)/Z^3` axiom alone; conditional on the
three admitted external inputs below, the combined 4-observable PMNS constraint
(3 angles + CP-phase sign) uniquely selects it at the pinned chamber point.

## Supplied inputs (admitted, external)

This selection table admits three external inputs. It does not derive any of
them, and it does not elevate `σ_hier` to an internally-derived or
observationally-closed quantity:

1. **The pinned chamber point** `(m_*, δ_*, q_+*) = (0.657061, 0.933806,
   0.715042)` — supplied by the P3 PMNS-as-f(H) map together with the imposed
   branch-choice rule A-BCC. Treated here as an admitted external input.
2. **The NuFit 5.3 NO 3σ magnitude windows** on the 9 `|U_PMNS|_{ij}` entries —
   supplied observational comparators (`PDG_LO`/`PDG_HI` in the runner). An
   admitted external input.
3. **The T2K/NOvA `sin(δ_CP) < 0` sign preference** — the supplied experimental
   sign comparator. An admitted external input.

Conditional on these three admitted external inputs, the table below records
which element of `S_3` the joint 4-observable PMNS filter selects at the pinned
point. Nothing below derives `σ_hier` from the `Cl(3)/Z^3` axiom.

## Proof structure

**Step 1 — Magnitude filter (9/9 NuFit check):**

The eigenvector matrix of H(m_*, δ_*, q_+*) has columns V[:,k] sorted
ascending by eigenvalue. For each of the 6 permutations σ ∈ S_3, the PMNS
matrix is P = V[σ, :]. Evaluating all 9 `|U_{ij}|` entries against the
NuFit 5.3 NO 3σ ranges gives:

| σ | NuFit passes | sin(δ_CP) | status |
|---|---:|---:|---|
| (0,1,2) | 4/9 | +0.966 | excluded (5 failures) |
| (0,2,1) | 4/9 | −0.966 | excluded (5 failures) |
| (1,0,2) | 5/9 | −1.000 | excluded (4 failures) |
| (1,2,0) | 5/9 | +1.000 | excluded (4 failures) |
| **(2,0,1)** | **9/9** | **+0.987** | magnitude passes |
| **(2,1,0)** | **9/9** | **−0.987** | magnitude passes |

The magnitude filter reduces S_3 from 6 to 2 admissible permutations.

**Step 2 — CP-phase discriminator:**

The two magnitude-passing permutations (2,0,1) and (2,1,0) differ by a
μ↔τ row swap. A row swap in the PMNS matrix preserves all `|U|` magnitudes
but reverses the sign of the Jarlskog invariant J, hence reversing
sin(δ_CP):

```
σ = (2,0,1):  sin(δ_CP) = +0.9874   (δ_CP ≈ +81°)
σ = (2,1,0):  sin(δ_CP) = −0.9874   (δ_CP ≈ −81°)
```

T2K (2021, Normal Ordering) measures δ_CP in the 1σ range [−200°, −15°]
(central ≈ −108°). NOvA similarly prefers sin(δ_CP) < 0. Both experiments
exclude sin(δ_CP) = +0.987 at ≥ 2σ. Therefore:

- σ = (2,0,1) is **experimentally disfavored** (sin(δ_CP) = +0.987, excluded
  at ≥ 2σ by T2K/NOvA).
- σ = (2,1,0) is **experimentally preferred** (sin(δ_CP) = −0.987, within
  T2K/NOvA 2σ preferred region).

## Selection statement (supplied-input)

**Selection statement (σ_hier, supplied-input).** Conditional on the three
admitted external inputs above, at the pinned chamber point
`(m_*, δ_*, q_+*) = (0.657061, 0.933806, 0.715042)`:

> The unique element σ ∈ S_3 with (1) all 9 `|U_PMNS|_{ij}` inside the
> NuFit 5.3 NO 3σ ranges AND (2) sin(δ_CP) < 0, is σ = (2, 1, 0).

This is a selection among the 6 elements of S_3 under the supplied comparators,
not an internal derivation. It is exact and verified by the dedicated runner.

## What the selection table shows

Conditional on the three admitted external inputs above, the free `σ_hier`
choice at the pinned chamber point is narrowed to a single element of `S_3`:

- σ_hier was previously listed as an "independent conditional — an S_3
  involution (order 2), not derivable from the C_3 order-3 cycle."
- Under the supplied NuFit windows and T2K/NOvA sign comparator, exactly one
  other σ ∈ S_3 survives the magnitude filter, and the CP-phase sign then
  leaves `σ = (2, 1, 0)` as the sole element passing the joint 4-observable
  PMNS filter.
- This is a conditional selection at the live pin, not an internal derivation
  and not an observational-closure claim: `σ_hier` is uniquely **selected**
  there by the supplied comparators, not derived from the framework alone.

## Consequence for the P3 flagship

With `σ_hier` **selected (not closed)** at the pinned point by this table,
conditional on the supplied inputs:

- The P3 flagship closure (PMNS-as-f(H) map + chamber pin) depends on:
  1. The imposed branch-choice rule **A-BCC** (physical sheet = `C_base`)
  2. σ_hier = (2,1,0), **selected** at the live pin conditional on the supplied
     NuFit windows + T2K/NOvA sign (not internally derived, not observationally
     closed)
- **A-BCC remains the single named source-side open input on the pinned
  chamber packet.** Broader chamber-wide / all-basin uniqueness is not
  supplied by this table.

## Falsifiable prediction

The CP-phase prediction sin(δ_CP) = −0.9874 is a forced geometric
consequence of the selected σ_hier under the supplied comparators. It is not a
separately imposed input.

A confirmed >3σ measurement of sin(δ_CP) > +0.5 at DUNE / Hyper-Kamiokande
would exclude the σ = (2, 1, 0) selection at this pin under the supplied
comparators (removing the pin's consistency with the 4-observable PMNS
filter).

## What this theorem does NOT claim

- Does not derive σ_hier from Cl(3)/Z^3 alone (the C_3 generator cannot
  distinguish S_3 involutions from cyclic elements).
- Does not close A-BCC (the physical-sheet identification is treated
  separately; see `ABCC_CP_PHASE_NO_GO_THEOREM_NOTE_2026-04-19.md`).
- Does not pin the absolute neutrino mass scale (different carrier).
- Does not determine the solar gap Δm²_21 (different carrier).
- Does not claim chamber-wide or all-basin uniqueness. Other `H`-parameter
  basins, including the documented Basin N neighborhood, may still support
  other internally consistent PMNS fits. A chamber-wide uniqueness statement
  would require a separate basin analysis.

## 2026-07-12 scope-narrowing (downstream hygiene)

On 2026-07-12 the closure-style language in this note was **narrowed** to match
its audited scope: the note now presents a **supplied-input `S_3` selection
table** conditional on three admitted external inputs (the pinned chamber
point, the NuFit 5.3 windows, and the T2K/NOvA sign preference), and the
earlier observational-closure wording was withdrawn. The physics is unchanged
— `σ = (2, 1, 0)`, the pin, and both proof steps are identical; only the
framing of what the table establishes was narrowed. Editing this note re-enters
the row into the audit queue for an independent re-read; this paragraph records
the narrowing and asserts no audit status of its own.

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_sigma_hier_uniqueness_theorem.py
```

Expected: `PASS = 33, FAIL = 0`.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- `ABCC_CP_PHASE_NO_GO_THEOREM_NOTE_2026-04-19.md` (downstream consumer; backticked to avoid length-2 cycle — citation graph direction is *downstream -> upstream*)
- `DM_SIGMA_HIER_CLOSURE_PACKET_NOTE_2026-04-20.md` (downstream consumer in
  the sigma-hierarchy closure packet; backticked to break cycle-0046
  sigma_hier_uniqueness -> dm_sigma_hier_closure_packet -> dm_pmns_cp_orientation_parity_reduction
  -> dm_sigma_hier_upper_octant_selector -> sigma_hier_uniqueness; the
  load-bearing direction *closure_packet -> sigma_hier_uniqueness* is
  preserved upstream)
- [neutrino_dirac_pmns_retained_lane_packet_2026-04-16](NEUTRINO_DIRAC_PMNS_RETAINED_LANE_PACKET_2026-04-16.md)
