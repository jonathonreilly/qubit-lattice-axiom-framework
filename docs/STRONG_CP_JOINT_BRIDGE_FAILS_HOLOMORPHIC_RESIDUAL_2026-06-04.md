# Strong-CP Joint-Basis Bridge Failure and Holomorphic-Generation Residual

**Date:** 2026-06-04
**Type:** no_go
**Claim type:** no_go (narrow bridge-failure evaluation).
**Claim scope:** the tested joint-basis bridge does not force
`theta_bar = theta_QCD + arg det M` to vanish. The runner verifies that the
gauge reflection and generation conjugation-parity operations act on disjoint
factors, that the tested generation density is odd under pure entrywise
conjugation but even under the reflection-composed generation parity, and that
the anomaly-invariant `theta_bar` is not moved by the separated reality
conditions tested here.

This note does not solve Strong CP, does not prove every route to
`theta_bar = 0` impossible, and does not prove that Strong CP, Koide `Q = 2/3`,
and generation identification are literally the same theorem. It records a
candidate shared residual class: an additional holomorphic/chiral generation
structure may be relevant to all three gates.

**Status authority:** independent audit lane only. This note sets no audit
status and assigns no grade.
**Runner:** [scripts/strong_cp_joint_bridge_holomorphic_residual_2026_06_04.py](../scripts/strong_cp_joint_bridge_holomorphic_residual_2026_06_04.py)
**Runner cache:** [logs/runner-cache/strong_cp_joint_bridge_holomorphic_residual_2026_06_04.txt](../logs/runner-cache/strong_cp_joint_bridge_holomorphic_residual_2026_06_04.txt)

```yaml
target_claim_type: no_go
proposed_claim_type: no_go
trace_class: negative_bridge_pruning
reachability_to_target: prunes_joint_basis_bridge
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## 1. Bridge Under Test

The proposed mass-side bridge was that the gauge Osterwalder-Schrader
reflection `Theta_OS` and the generation conjugation-parity `P` form one
forced global antiunitary basis condition. If true, a single K-real basis might
pin the physical anomaly-invariant angle

```text
theta_bar = theta_QCD + arg det M.
```

The runner tests a finite matrix model for that bridge:

1. **Anomaly-invariant bookkeeping.** An axial rotation shifts `arg det M` by
   `+n alpha` while the Fujikawa-side term shifts `theta_QCD` by `-n alpha`,
   leaving `theta_bar` fixed in the runner arithmetic.
2. **Pure-K versus reflection-composed parity.** For
   `G = i(C - C^2)`, entrywise conjugation gives `conj(G) = -G`, while the
   reflection-composed generation parity gives `P conj(G) P = +G`.
3. **Pure-K is not a symmetry of the tested complex-`b` Hermitian circulant.**
   For non-real `b`, `conj(M) != M`; the available relation is the
   reflection-composed one, `P M(b) P = M(conj b)`.
4. **Sector disjointness.** The gauge reflection and generation parity commute
   because they act on different tensor factors. The product can be written,
   but the runner does not derive it as one forced operation.
5. **Residual marker.** A pure-K invariant generation coupling would require
   changing the coupling class. The runner marks this as the open residual; it
   does not prove that such a coupling exists.

The supported conclusion is narrow: the current joint-basis bridge does not
force `theta_bar = 0`.

## 2. Residual Interpretation

The failed bridge points toward a residual involving a holomorphic or chiral
generation-side structure. This is suggestively aligned with:

- the open holomorphic-generation polarization named in
  [KOIDE_EMERGENT_TIME_ETA_CONJUGATION_PARITY_BOUNDED_NOTE_2026-05-30.md](KOIDE_EMERGENT_TIME_ETA_CONJUGATION_PARITY_BOUNDED_NOTE_2026-05-30.md);
- the Koide holomorphic/chiral readout open gate in
  [SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md](SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md);
- the generation-space bridge residual in
  [KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md](KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md).

That alignment is a research lead, not a theorem. A future result could show
that these residuals share one input, or it could split them again.

## 3. Relation To Strong-CP Surfaces

This note is compatible with the existing Strong-CP boundaries:

- [STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
  already warns that a reflection-positive half does not forbid every CP-odd
  imaginary contribution.
- [STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)
  keeps mass orientation as a conditional surface.
- [STRONG_CP_EPSILON_PSEUDOTENSOR_OH_SIGN_BRIDGE_BOUNDED_NOTE_2026-05-26.md](STRONG_CP_EPSILON_PSEUDOTENSOR_OH_SIGN_BRIDGE_BOUNDED_NOTE_2026-05-26.md)
  supplies related sign-bridge context.

The new content is the runner-backed failure of this particular joint-basis
splice to force the anomaly-invariant angle to zero.

## 4. No-Go Discipline Gate

**N1 - Alternative route enumeration.**

| route | result | marker |
|---|---|---|
| Joint `Theta_OS x P` antiunitary bridge | Product exists but is sector-disjoint; not derived as one forced operation. | ATTEMPTED |
| Pure entrywise-K constraint | Would make the tested generation density odd, but is not a symmetry for non-real `b` in the tested Hermitian circulant class. | ATTEMPTED |
| Reflection-composed generation parity | Makes the tested density even, so this parity rule does not force `theta_bar = 0`. | ATTEMPTED |
| Axial-rotation/anomaly bookkeeping | Runner checks `theta_bar` remains invariant under paired shifts; separated reality conditions do not co-move in this model. | ATTEMPTED |
| Real-boundary pure-K escape | Pure-K is available on the real boundary, but that changes away from the non-real coupling class under test and does not close the current bridge. | ATTEMPTED |
| Holomorphic-generation escape | A derived holomorphic/chiral generation structure could change the problem, but this PR does not derive one and does not use its absence as a universal no-go. | ATTEMPTED |

**N2 - Wall independence.** The collapsed wall set for the narrowed claim is
sector disjointness plus absence of pure-K symmetry in the tested non-real
Hermitian circulant class. Reflection-composed parity and anomaly bookkeeping
are evidence for those walls, not extra independent imports. Quark-sector
transport is outside this claim and remains future work.

**N3 - Hidden-wall scan.** "Joint basis", "pure-K", "holomorphic", and
"shared residual" are not used as silent authorities. The first three are
tested or rejected in the finite runner; the shared-residual language is marked
as a lead.

**N4 - Residual matching.** The residual isolated here is a missing
generation-side structure that would make the mass-side reality condition
stronger than reflection-composed parity. That is similar to Koide/generation
holomorphic residuals, but not identical by proof. The note therefore says
"candidate shared residual class", not "same theorem".

**N5 - Rhetoric audit.** "`theta_bar` is not forced" means "not forced by the
tested joint-basis bridge." It is not a universal no-go against all Strong-CP
solutions.

**N6 - Partial-closure scan.** A future holomorphic generation theorem,
quark-sector transport theorem, or anomaly-covariant pure-K construction could
retire this residual without adding an axiom. Approved axioms and primitives
are not bounded-status sources.

**N7 - Steelman.** A hostile reviewer would argue that the finite toy
factorization does not model the full gauge/matter anomaly problem, and that a
quark-sector construction might align the gauge and mass phases in a way this
runner cannot see. That is accepted; the claim remains bridge-specific.

**N8 - Cross-cycle echo.** Previous Strong-CP and Koide cycles repeatedly
overclosed residuals by treating aligned vocabulary as a common theorem. This
note keeps the alignment visible but does not merge the claims.

**Gate result:** PASS for the narrowed bridge-failure claim only.

## 5. What This Does Not Claim

- It does not solve Strong CP.
- It does not prove all `theta_bar = 0` routes impossible.
- It does not prove Koide `Q = 2/3`, generation identification, and Strong CP
  reduce to one theorem.
- It does not add or change an axiom, framework primitive, Tier-A admission, or
  audit verdict.

## 6. Trace Gate

```yaml
trace_class: negative_bridge_pruning
target_blocker_text: "theta_bar not forced by the current joint gauge/mass basis bridge"
source_of_blocker_text: source_note
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "test quark-sector transport and any derived holomorphic/chiral generation coupling before treating the residual as shared."
```
