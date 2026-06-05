# Flavor — r=1/2 is stable for the supplied two-sector reverse map `g(r)=sqrt(r/2)`; physical-arrow selection remains open.

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** bounded map theorem. The source verifies the stability reversal for the supplied
two-sector map `g(r)=sqrt(r/2)`, the HS equipartition identity, endpoint spectra, and competing entropy
partitions. It does **not** derive that charged-lepton `r` physically evolves by this map or by any
framework-native thermalizing arrow.
**Runner:** `scripts/flavor_r_half_stable_under_thermalizing_arrow_2026_06_02.py` (SCORECARD 5/5).
**Source:** full assumptions brainstorm `wf_919df127` — 14 challenges + 3 meta, **16/17 converge** on "stable under a named condition" (the lone dissenter agrees on the diagnosis).

## The result: r=1/2 is stable for the supplied map
The prior "r=1/2 is an unstable separatrix" was computed under the **records/Lüders sharpening** map
`r→2r²` — an **entropy-decreasing** (observer / measurement / einselection-collapse) flow, multiplier
`S'(1/2)=2>1`. This note verifies the supplied reverse map

```text
g(r) = sqrt(r/2),
```

on the same two-sector coordinate. For this map, `g'(1/2)=1/2<1` and `r=1/2`
is the global attractor on the tested positive seeds `(0.05, 0.25, 0.49, 0.51,
0.9, 5.0)`. Thus the instability claim is not map-invariant: reversing the
records/sharpening map flips repeller to attractor at the identical fixed point.

The physical-arrow interpretation is a separate gate. The runner proves stability
for this named two-sector map; it does not prove that charged-lepton masses are
governed by that map.

## Grounded anchors (exact framework baseline / Z₃-circulant algebra)
- **r=1/2 ⟺ HS 2-sector equipartition** (verified): `‖aI‖²=3a²` equals `‖bC+b̄C²‖²=6|b|²` iff `|b|²/a²=1/2`
  — the unique maximum of the 2-block (singlet vs doublet) entropy `S₂=ln2`.
- **Endpoint exclusion within the charged-lepton use case** (verified spectra): `r=0→[1,1,1]`
  (S₃-degenerate) and `r=1→[0,0,3]` (two massless). Any distinct massive-lepton readout on this carrier
  must lie in the open interior `(0,1)`, where `r=1/2` is the balanced point attracted by the supplied
  map `g`.
- `Q = Tr H²/(Tr H)² = 1/3+(2/3)r` exact; `Q=2/3 ⟺ r=1/2 ⟺ sector equipartition`.

## Honest residual — the gates left outside this theorem
1. **Partition (load-bearing):** r=1/2 is the max-entropy attractor *only* for the **2-isotype-sector**
   coarse-graining. Verified: the 3-eigenvalue **spectral** entropy peaks at **r=0**; dimension/Plancherel
   weighting peaks at **r=1**. So stability at `r=1/2` requires selecting the 2 sectors — exactly the
   **det_C / einselected-partition gate** the broader campaign reduces to.
2. **Arrow/map (identification):** binding physical `r` evolution to `g(r)=sqrt(r/2)` or to any
   framework-native entropy-increasing flow on the 2-sector simplex is not derived here. The theorem is
   conditional on the supplied map.

Both reduce to the same residual (2-sector partition + the chirality bookkeeping shared with generation-ID).
**Correction to the brainstorm's "σ-symmetry protection":** the proposed involution `|b|²→a²−|b|²` *is*
`r↔1−r` and it **changes Tr H²** (4.2 vs 7.8) — a relabeling, **not** a dynamical symmetry. The stability
rests on **equipartition + the selected map**, *not* on symmetry-protection.

## Three-lane candidate picture
The lanes are not competing attractors of one established physical flow — they are three strata of the 2-sector structure,
sorted by entropy-arrow and symmetry:

| lane | r | spectrum | character | dynamics |
|---|---|---|---|---|
| **Q=1/3** | 0 | [1,1,1] | unbroken-S₃ democratic (max *spectral* entropy) | stable basin of the *sharpening* flow, if that map is selected; candidate: quasi-degenerate neutrinos / pre-breaking vacuum |
| **Q=2/3** | ½ | [2.41,0.29,0.29] | balanced self-dual interior (max *2-sector* entropy) | stable attractor of the supplied reverse map `g`; charged-lepton identification remains open |
| **Q=1** | 1 | [3,0,0] | maximal hierarchy / two massless | det_R / Plancherel default + operator-self-composition RG super-attractor |

**Staging:** Q=1 is the det_R / dimension-Plancherel default + RG-attractor candidate; Q=1/3
is the unbroken-S₃ / sharpening-basin candidate; Q=2/3 is the equilibrium of the supplied 2-sector
reverse map. Each is a distinguished point on the exact line `Q=1/3+(2/3)r`, with physical selection left
to the relevant gate.

## Net
**r=1/2 is stable for the supplied two-sector reverse map** `g(r)=sqrt(r/2)`, and it is exactly the HS
2-sector equipartition point. The prior "unstable" verdict applies to the sharpening map `r→2r²`, not to
this reverse map. What remains open is physical selection: why the framework should choose the 2-sector
partition and why charged-lepton `r` should follow this entropy-increasing map.

## Provenance (verified 2026-06-02)
- Map flip (sharpening repeller / supplied reverse-map global attractor), HS equipartition, endpoint spectra,
  σ=r↔1−r-changes-Casimir, 2-sector-vs-spectral entropy peaks: verified directly (runner 5/5).
- Consistent with the records-separatrix note's `r→2r²` sharpening map — this is its supplied reverse-map counterpart — and the lane/extremum reframe. The r=1/2 *partition* selector remains the open gate; the einselection criterion is still the open object.
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
