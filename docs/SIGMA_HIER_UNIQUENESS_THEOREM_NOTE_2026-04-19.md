# σ_hier Uniqueness Theorem

**Date:** 2026-04-19  
**Status:** **supplied-input S3 table theorem on the open DM gate** —
`σ_hier = (2, 1, 0)` is uniquely selected by the registered packet (P-SIG) at
its supplied chamber point  
**Runner:** `scripts/frontier_sigma_hier_uniqueness_theorem.py` ([scripts/frontier_sigma_hier_uniqueness_theorem.py](../scripts/frontier_sigma_hier_uniqueness_theorem.py))
**Runner result:** `PASS = 37, FAIL = 0`

## What this theorem establishes

Given the supplied packet (P-SIG), including its pinned chamber point
`(m_*, δ_*, q_+*) = (0.657061, 0.933806, 0.715042)`, the hierarchy pairing
`σ_hier = (2, 1, 0)` is the **unique** element of S_3 satisfying both:

1. **All 9** `|U_PMNS|_{ij}` entries inside the supplied NuFit 5.3 NO 3σ
   comparator windows.
2. The supplied sign gate **sin(δ_CP) < 0**.

This is an exact finite table-selection statement on supplied inputs. It is
not an observational promotion, does not ratify the pin or comparator
authorities, and does not derive `σ_hier` from the `Cl(3)/Z^3` axiom alone.

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

Packet entry (P-SIG-c) supplies the sign gate `sin(δ_CP) < 0` as comparator
context. This row does not independently ratify its experimental authority.
Applying that supplied gate to the two magnitude-passing rows gives:

- σ = (2,0,1) **fails the supplied sign gate** because
  sin(δ_CP) = +0.987.
- σ = (2,1,0) **passes the supplied sign gate** because
  sin(δ_CP) = −0.987.

## Supplied-Input Registration (P-SIG)

```text
(P-SIG) Supplied-input packet for the S3 table claim (2026-07-11).

(P-SIG-a) Pinned chamber point (supplied, not ratified here):
PIN: m_* = 0.657061 ; delta_* = 0.933806 ; q_+* = 0.715042
(P-SIG-b) Magnitude comparator windows (external observational import,
          comparator context only — never a derivation input): the NuFit 5.3
          NO 3-sigma |U_PMNS| ranges as tabulated below.
WINDOWS:
U_e1: [0.801, 0.845]
U_e2: [0.513, 0.579]
U_e3: [0.143, 0.155]
U_mu1: [0.234, 0.500]
U_mu2: [0.471, 0.689]
U_mu3: [0.637, 0.776]
U_tau1: [0.271, 0.525]
U_tau2: [0.477, 0.694]
U_tau3: [0.613, 0.756]
(P-SIG-c) CP-sign gate (external observational import, comparator context
          only): sin(delta_CP) < 0 per the T2K/NOvA preference.
SIGN-GATE: sin_delta_cp < 0
```

**Status:** supplied-input packet entry. (P-SIG-a) is supplied by the pinned
chamber packet and is not independently ratified by this row; (P-SIG-b) and
(P-SIG-c) are external observational imports carried as comparator context
per registry discipline. None of the three is derived here.

## Theorem statement

**Theorem (S3 table uniqueness on the supplied packet (P-SIG)).** Given
(P-SIG-a)-(P-SIG-c), the unique element σ ∈ S_3 with (1) all 9
`|U_PMNS|_{ij}` inside the supplied windows AND (2) the supplied sign gate,
is σ = (2, 1, 0). Exact finite arithmetic on the supplied inputs; verified by
the runner.

## What this closes

At the supplied pin, `σ_hier` is uniquely selected **by the supplied packet**.
This is a supplied-input selection statement, not an internal derivation and
not a ratified observational closure; the windows remain comparator context.

- σ_hier was previously listed as an "independent conditional — an S_3
  involution (order 2), not derivable from the retained C_3 order-3 cycle."
- On (P-SIG), no other σ ∈ S_3 passes all nine supplied windows and the
  supplied sign gate.
- `σ_hier` is uniquely selected under those registered inputs. It is not
  internally derived from the framework alone, and ratification of the pin,
  windows, and sign authority remains outside this row.

## Consequence for the P3 flagship

With `σ_hier` selected at the supplied pinned point by this theorem:

- The P3 flagship closure (PMNS-as-f(H) map + chamber pin) depends on:
  1. The imposed branch-choice rule **A-BCC** (physical sheet = `C_base`)
  2. `σ_hier = (2,1,0)`: ~~now closed by observational uniqueness~~ →
     **uniquely selected under the supplied packet (P-SIG); ratification of
     the pin and windows remains outside this row**
- This table theorem does not change the source-side status of **A-BCC**, the
  physical-sheet identification, or the supplied chamber pin. Broader
  chamber-wide / all-basin uniqueness is not supplied by this theorem.

## Falsifiable prediction

Conditional on the supplied pin (P-SIG-a), the CP-phase prediction
sin(δ_CP) = −0.9874 is a geometric consequence of the uniquely selected
`σ_hier`. The numerical value is not separately imposed by the sign gate.

A confirmed >3σ measurement of sin(δ_CP) > +0.5 at DUNE / Hyper-Kamiokande
would falsify the P3 closure (ruling out the only physically consistent
chamber pin under the 4-observable PMNS constraint).

## What this theorem does NOT claim

- Does not derive σ_hier from Cl(3)/Z^3 alone (the C_3 generator cannot
  distinguish S_3 involutions from cyclic elements).
- Does not independently ratify the supplied pin, NuFit comparator windows,
  or T2K/NOvA sign-gate authority.
- Does not close A-BCC (the physical-sheet identification is treated
  separately; see `ABCC_CP_PHASE_NO_GO_THEOREM_NOTE_2026-04-19.md`).
- Does not pin the absolute neutrino mass scale (different carrier).
- Does not determine the solar gap Δm²_21 (different carrier).
- Does not claim chamber-wide or all-basin uniqueness. Other `H`-parameter
  basins, including the documented Basin N neighborhood, may still support
  other internally consistent PMNS fits. A chamber-wide uniqueness statement
  would require a separate basin analysis.

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_sigma_hier_uniqueness_theorem.py
```

Expected: `PASS = 37, FAIL = 0`.

## Repair Note (2026-07-11)

**Notes for re-audit (verbatim):**

> missing_dependency_edge: wire and audit the direct
> authorities for the pinned PMNS chamber/A-BCC setup and the exact
> NuFit/T2K/NOvA comparator windows used by the runner, or split this into a
> pure supplied-input S3 table claim.

This repair takes the split arm:

1. (P-SIG-a) registers the chamber point as supplied and not ratified here.
2. (P-SIG-b) and (P-SIG-c) register the exact magnitude windows and sign gate
   as external observational imports used only as comparator context, never
   as derivation inputs.
3. The theorem is narrowed to exact finite S3 table uniqueness on that packet;
   it no longer claims observational promotion or ratified closure.
4. The runner parses the packet, constructs every scan input from it, pins the
   narrowed note surface, and exercises a corrupted-window negative control.

**Note-hash:** supplied pin + comparator-context windows/sign gate → exact
finite S3 table selection only; no internal derivation or ratified
observational closure.

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
