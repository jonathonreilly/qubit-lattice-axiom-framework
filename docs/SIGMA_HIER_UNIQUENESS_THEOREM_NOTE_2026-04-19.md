# σ_hier Supplied-Input Selection Replay

**Date:** 2026-04-19  
**Type:** open_gate
**Status:** **supplied-input S_3 selection table** — conditional on three admitted
external inputs (the pinned chamber point, the NuFit 5.3 NO 3σ magnitude windows
without SK-atm, and a supplied `sin(δ_CP) < 0` sign comparator motivated by T2K),
`σ_hier = (2, 1, 0)` is the unique
hierarchy-pairing permutation passing the joint 4-observable PMNS filter at the pinned
chamber point
**Runner:** `scripts/frontier_sigma_hier_uniqueness_theorem.py` ([scripts/frontier_sigma_hier_uniqueness_theorem.py](../scripts/frontier_sigma_hier_uniqueness_theorem.py))
**Runner result:** `PASS = 33, FAIL = 0`

## What this table records

At the pinned chamber point `(m_*, δ_*, q_+*) = (0.657061, 0.933806,
0.715042)` (supplied by the P3 PMNS-as-f(H) map), the hierarchy pairing
`σ_hier = (2, 1, 0)` is the **unique** element of S_3 satisfying both:

1. **All 9** `|U_PMNS|_{ij}` entries inside the NuFit 5.3 NO 3σ experimental
   ranges without SK-atm.
2. **sin(δ_CP) < 0**, used here as a supplied sign comparator.

This is a supplied-input selection statement, not an internal derivation.
`σ_hier` is not derivable from the `Cl(3)/Z^3` axiom alone; conditional on the
three admitted external inputs below, the combined 4-observable PMNS constraint
(3 angles + CP-phase sign) uniquely selects it at the pinned chamber point.

## Supplied inputs (admitted, external)

This selection table admits three external inputs. It does not derive any of
them, and it does not elevate `σ_hier` to an internally-derived or
observationally-closed quantity:

1. **The pinned chamber point** `(m_*, δ_*, q_+*) = (0.657061, 0.933806,
   0.715042)` — supplied by the P3 PMNS-as-f(H) construction, which obtained
   this point under both the imposed branch-choice rule A-BCC and the already
   chosen pairing `σ_hier = (2, 1, 0)`. Treated here as an admitted external
   input. Because the pairing participated in constructing the pin, replaying
   permutations at this fixed point is a conditional consistency table, not
   independent evidence that selects the pairing.
2. **The NuFit 5.3 NO 3σ magnitude windows without SK-atm** on the 9
   `|U_PMNS|_{ij}` entries — supplied observational comparators
   (`PDG_LO`/`PDG_HI` in the runner). An admitted external input.
3. **The `sin(δ_CP) < 0` sign comparator** — supplied rather than derived,
   with the T2K 2021 negative-phase preference as motivation. It is not
   presented as a joint T2K/NOvA preference: the NOvA 2021 normal-ordering
   result instead disfavored the neighborhood of `δ_CP = 3π/2` at about 2σ.

Conditional on these three admitted external inputs, the table below records
which element of `S_3` the joint 4-observable PMNS filter selects at the pinned
point. Nothing below derives `σ_hier` from the `Cl(3)/Z^3` axiom.

## Proof structure

**Step 1 — Magnitude filter (9/9 NuFit 5.3 check, without SK-atm):**

The eigenvector matrix of H(m_*, δ_*, q_+*) has columns V[:,k] sorted
ascending by eigenvalue. For each of the 6 permutations σ ∈ S_3, the PMNS
matrix is P = V[σ, :]. Evaluating all 9 `|U_{ij}|` entries against the
NuFit 5.3 NO 3σ ranges without SK-atm gives:

| σ | NuFit passes | sin(δ_CP) | status |
|---|---:|---:|---|
| (0,1,2) | 4/9 | +0.966 | excluded (5 failures) |
| (0,2,1) | 4/9 | −0.966 | excluded (5 failures) |
| (1,0,2) | 5/9 | −1.000 | excluded (4 failures) |
| (1,2,0) | 5/9 | +1.000 | excluded (4 failures) |
| **(2,0,1)** | **9/9** | **+0.987** | magnitude passes |
| **(2,1,0)** | **9/9** | **−0.987** | magnitude passes |

The magnitude filter reduces S_3 from 6 to 2 admissible permutations.

**Step 2 — Supplied CP-sign discriminator:**

The two magnitude-passing permutations (2,0,1) and (2,1,0) differ by a
μ↔τ row swap. A row swap in the PMNS matrix preserves all `|U|` magnitudes
but reverses the sign of the Jarlskog invariant J, hence reversing
sin(δ_CP):

```
σ = (2,0,1):  sin(δ_CP) = +0.9874   (δ_CP ≈ +81°)
σ = (2,1,0):  sin(δ_CP) = −0.9874   (δ_CP ≈ −81°)
```

Applying the supplied `sin(δ_CP) < 0` comparator therefore removes
`σ = (2,0,1)` and retains `σ = (2,1,0)`. This is a filter operation on an
admitted comparator, not an experimental-confidence combination and not a
claim that T2K and NOvA share the same 2021 phase preference.

## Selection statement (supplied-input)

**Selection statement (σ_hier, supplied-input).** Conditional on the three
admitted external inputs above, at the pinned chamber point
`(m_*, δ_*, q_+*) = (0.657061, 0.933806, 0.715042)`:

> The unique element σ ∈ S_3 with (1) all 9 `|U_PMNS|_{ij}` inside the
> NuFit 5.3 NO 3σ ranges without SK-atm AND (2) sin(δ_CP) < 0, is
> σ = (2, 1, 0).

This is a replay among the 6 elements of S_3 under the supplied pin and
comparators, not an internal derivation or an independent selector. The finite
table is exact and verified by the dedicated runner.

## What the selection table shows

Conditional on the three admitted external inputs above, the free `σ_hier`
choice at the pinned chamber point is narrowed to a single element of `S_3`:

- σ_hier was previously listed as an "independent conditional — an S_3
  involution (order 2), not derivable from the C_3 order-3 cycle."
- Under the supplied NuFit windows and negative-sign comparator, exactly one
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
     NuFit windows + supplied negative-sign cut (not internally derived, not observationally
     closed)
- **A-BCC and the hierarchy pairing remain the two open inputs of the pinned
  P3 construction.** This replay table does not reduce that input count.
  Broader chamber-wide / all-basin uniqueness is not supplied by this table.

## Conditional consequence

The value sin(δ_CP) = −0.9874 is the geometric consequence of evaluating
the supplied construction with the selected `σ_hier`. It is not a separately
imposed number, but this replay table does not establish it as an independent
prediction because `σ_hier = (2, 1, 0)` participated in the pin's provenance.

A confirmed >3σ measurement of sin(δ_CP) > +0.5 at DUNE / Hyper-Kamiokande
would exclude the σ = (2, 1, 0) selection at this pin under the supplied
comparators (removing the pin's consistency with the 4-observable PMNS
filter).

## What this table does NOT claim

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
- Does not claim that replaying the already pairing-conditioned pin is
  independent evidence for `σ_hier = (2, 1, 0)`.

## 2026-07-12 scope-narrowing (downstream hygiene)

On 2026-07-12 the closure-style language in this note was **narrowed** to match
its audited scope: the note now presents a **supplied-input `S_3` selection
replay** conditional on three admitted external inputs (the pairing-conditioned
pin, the NuFit 5.3 windows without SK-atm, and the supplied negative-sign
comparator), and the earlier observational-closure wording was withdrawn. The
finite outcome is unchanged — `σ = (2, 1, 0)`, the pin, the two magnitude
survivors, and their opposite Jarlskog signs. Review also corrected the imported
NuFit version, removed a false joint T2K/NOvA attribution, and disclosed the
pin's pairing-conditioned provenance. Editing this note re-enters the row into
the audit queue for an independent re-read; this paragraph records the
narrowing and asserts no audit status of its own.

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
