# Extra-Assumptions Audit of the Matter-Attachment Gate No-Gos

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit.
**Primary runner:** [`scripts/frontier_koide_matter_attachment_gate_extra_assumptions_audit.py`](../scripts/frontier_koide_matter_attachment_gate_extra_assumptions_audit.py)

## Context

The companion note
`KOIDE_MATTER_ATTACHMENT_GRADED_STATISTICS_GATE_NARROW_THEOREM_NOTE_2026-06-02`
reduced the charged-lepton matter-attachment pin to a single cross-site
graded-statistics gate, identified with four retained no-gos. This note runs
the extra-assumptions exercise on those four walls -- enumerating the
assumptions each relies on beyond A1 + A2 + retained, and adversarially
testing whether relaxing any opens the matter-attachment. The exercise is
framed to FIND THE ESCAPE, not to confirm the walls.

The four targets (all `retained_no_go` on origin/main):

- **N1** `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25`
- **N2** `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28`
- **N3** `no_per_site_chirality_theorem_note_2026-05-02`
- **N4** `no_per_site_bosonic_ccr_theorem_note_2026-05-02`

## Claim

Each of the four no-gos is airtight AT ITS STATED SCOPE, but all four are
**kinematic / single-site / ungraded** facts, and the escape seam is
**uniform**: it lives in the **graded cross-site / emergent-time dynamics**
arena, which is currently unaudited (not yet retained). The exercise also
surfaced one genuine internal correction (N2's stated reason is superseded by
a sister retained result) and one red flag (an unaudited microcausality note
conflates per-site grading with cross-site anticommutation). None of the four
walls is foreclosed by the kinematic algebra; the productive next paths are
two named promotion targets in the dynamics arena.

### A. The kinematic A1 + A2 frame IS the hard-core boson (N1, N4)

A1 + A2 commit to the ordinary (ungraded) `C*`-tensor product, in which odd
ladders on disjoint sites COMMUTE:

```text
O_0 = sigma_+ (x) I,  O_1 = I (x) sigma_+,   [O_0, O_1] = 0   (hard-core boson),
JW dressing  c_0 = sigma_+ (x) I,  c_1 = sigma_z (x) sigma_+,  {c_0, c_1} = 0   (fermion).
```

So the fermionic frame is a graded relabel = an invertible CHOICE, and every
single-site invariant (number spectrum `{0,1}`, generated algebra,
dimension 2) is identical across the frames. The free-CCR no-go (N4) is a
one-line trace argument (`Tr[a,a^dag] = 0 != Tr I_2 = 2`) that kills only the
free boson `[a,a^dag] = I`; the hard-core boson `b = sigma_+` has
`[b,b^dag] = diag(1,-1) != I` and evades it. **N4's method is single-site and
cannot reach the cross-site fork; the one direction it does point (strict
on-site locality of the elementary field) selects the hard-core boson, not
the fermion.** This is the structural reason the matter-attachment cannot be
forced kinematically.

### B. The dynamics DOES select CAR -- but in the (unaudited) emergent-time arena (N1)

The single-time-slice scope of N1 excludes the mechanism the framework uses
to select statistics. With the standard Pauli mechanism on the
statistics-blind kernel:

```text
Bose-quantizing the -E Dirac mode is unbounded below; CAR is bounded,
CAR on-shell combo  Lu + g0 Lv g0 = 2E g0   (microcausal),
Bose combo  Lu + Lv = 2(E g0 - p.gamma) != 2E g0   (microcausality fails).
```

So energy positivity + microcausality DO distinguish the frames N1 calls
"same algebra." This is not a fresh escape: it is the active
`free_sector_spin_statistics_level1...2026-05-30` (T1/T2) campaign, whose
load-bearing rungs are all **unaudited / audited_conditional** --
`axiom_first_reflection_positivity_theorem` (**unaudited**),
`axiom_first_spectrum_condition_theorem` (**unaudited**), and the
OS->Wightman reconstruction `R`. A1 + A2 contain no time
(`MINIMAL_AXIOMS_2026-05-20.md`: dynamics enters only through named
derivation lanes), so N1 is faithful to the literal kinematic question; the
escape is the dynamics arena, gated on promoting those rungs.

### C. The discrete exchange Z2 exists; the residual is a framing, not pi_1 (N2)

N2's stated reason -- "on a discrete site set `pi_1` is trivial, so the
Finkelstein-Rubinstein rotation->exchange homotopy dies" -- is **superseded**:
`graph_braid_z3_anyon_exclusion_dichotomy_narrow_theorem_note_2026-05-29`
(**retained_bounded**) proves the discrete two-particle CONFIGURATION space
carries a Z2 exchange class (`H_1(UD_2(Z^3)) = Z^b1 (+) Z_2`). The site set's
`pi_1` is trivial, but that is the wrong object; the configuration space's is
not. So N2's stated mechanism is not airtight.

The wall's SUBSTANCE survives, relocated. The `2 pi = -1` spinor sign on one
particle is the central `-I_2 (x) I = -I_4`, a GLOBAL phase:

```text
(-I_2) (x) I = -I_4,   [-I_4, SWAP] = 0   (commutes with exchange),
a NON-central spin op:  SWAP (i sigma_z (x) I) SWAP = I (x) i sigma_z != original.
```

So the existing graph-braid Z2 is purely positional and the on-site `2O`
spin sign decouples by CENTRALITY (not by factor-separation). Coupling them
needs a discrete framing / ribbon structure on the configuration space -- a
1-complex has no transverse plane to frame -- which is an import (user
approval) unless derived. **Recommended internal correction (for the audit
lane, not edited here): N2's F2 should target the missing framing, not
"pi_1 trivial."**

### D. Multi-site chirality exists but sits on the wrong factor (N3)

N3 (no single-site `gamma_5`, because `omega = sigma_1 sigma_2 sigma_3 = iI`
is central for odd `n = 3`) is airtight but single-site, and explicitly
scopes out multi-site / emergent-spacetime chirality. Those DO exist and are
retained-derivable: the corner chirality `eps = (-1)^{Hamming}` on `(Z_2)^3`
anticommutes with the cross-site Dirac operator (`{eps, D} = 0`), and the
even-dimension volume element gives `gamma_5` on `Cl(3,1)`
(`clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10`,
**retained**). But `eps` restricted to the `hw = 1` generation triplet is
`-I_3` (a uniform scalar), so it does not split generation from generation --
matching `parity_violation_does_not_reach_generation_triplet...` (retained_bounded).
The real generation-chirality wall is a different theorem,
`koide_z3_equivariant_anticommuting_no_go_note_2026-05-16`
(**retained_bounded**); the unbuilt bridge is the transport
`eps(position) -> Gamma_chi(generation)`.

## Disposition

All four no-gos are airtight at their stated scope; none is foreclosed by the
kinematic algebra. The escape is uniform -- the graded cross-site /
emergent-time dynamics arena -- and resolves to two named promotion targets
plus one correction and one flag.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | retained_no_go |
| `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28` | retained_no_go |
| `no_per_site_chirality_theorem_note_2026-05-02` | retained_no_go |
| `no_per_site_bosonic_ccr_theorem_note_2026-05-02` | retained_no_go |
| `graph_braid_z3_anyon_exclusion_dichotomy_narrow_theorem_note_2026-05-29` | retained_bounded |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | retained_bounded |
| `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10` | retained |
| `parity_violation_does_not_reach_generation_triplet_narrow_theorem_note_2026-05-23` | retained_bounded |
| `free_sector_spin_statistics_level1_mechanism_and_reconstruction_reduction_bounded_note_2026-05-30` | unaudited |
| `axiom_first_reflection_positivity_theorem_note_2026-04-29` | unaudited |
| `axiom_first_spectrum_condition_theorem_note_2026-04-29` | unaudited |
| `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01` | unaudited |

## Red flag (for the audit lane)

The **unaudited** `axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01`
asserts the per-site `Cl(3)` grading propagates to a vanishing cross-site
graded commutator automatically. Section A shows this is false in the ordinary
tensor product A1 + A2 commit to: disjoint-site odd elements COMMUTE, they do
not anticommute. This is exactly the conflation the retained N1 was written to
refute. The note is unaudited, hence not load-bearing, but if ever cited to
derive the graded structure it would smuggle in the fermionic frame.

## Non-circularity

The forward checks are tier verification and direct computation (the ordinary
tensor product, the on-shell projector identity, the centrality of `-I`, the
corner-grading anticommutation), none of which uses CAR, the faithful
representation, or `Q = 2/3`.

## Next paths this opens

- Promote `axiom_first_reflection_positivity_theorem` and
  `axiom_first_spectrum_condition_theorem` toward retained; the free_sector
  T1/T2 reduction then makes CAR (and the matter-attachment) a derived
  consequence of A1 + A2 + emergent time, via the dynamics arena rather than
  the kinematic algebra.
- Construct (or show the obstruction to) a discrete framing / ribbon map on
  `UD_2(Z^3)` carrying the graph-braid exchange Z2 onto the on-site `2O` spin
  Z2 -- the precise discrete spin-statistics map. If derivable from retained,
  it couples statistics to the spin sign without the continuum.
- Build the transport `eps(position) -> Gamma_chi(generation)`: whether the
  corner chirality (which anticommutes with the spatial Dirac operator) can be
  coupled to the `hw = 1` internal index. This is the bridge shared with the
  generation-identification gate.

This audit sharpens the gate from a wall into a uniform, named dynamics
target; it is a localization, not an enumeration.
