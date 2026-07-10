# ABJ P-HY Retained-Bounded Supplier Wiring

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Source-side status:** bounded-support source theorem; independent review/audit owns any
effective status movement.
**Trace class:** direct_blocker_closure
**Target blocker:**
`anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
was previously treated as conditional partly because P-HY was treated as a
declared premise edge. This note supplies the narrow P-HY edge needed by the
ABJ B1 left-handed anomaly arithmetic from an existing bounded source.
**Primary runner:** `scripts/frontier_abj_phy_retained_bounded_supplier_wiring_2026_06_18.py`

## Result

For the bounded ABJ bridge's B1 step, P-HY need not be an unsupported
physical-hypercharge import. The exact left-handed arithmetic uses only this
bounded surface:

```text
Q_L : (2,3)_{+1/3},       L_L : (2,1)_{-1}.
```

That surface is supplied by the current supplier chain
[`HYPERCHARGE_IDENTIFICATION_NOTE.md`](HYPERCHARGE_IDENTIFICATION_NOTE.md),
whose current ledger `claim_scope` is quoted here (verbatim up to line
wrapping):

> Bounded LH-doublet chain assembly: from the retained-grade ratio,
> matter-assignment, alpha=1/3 normalization, and GMN readout authorities, the
> commutant U(1) gives Y(Q_L)=+1/3, Y(L_L)=-1 and the derived LH charge table;
> no full-spectrum anomaly, GUT-normalization, or sin^2(theta_W) claim is
> included.

From the ledger scope, the supplier surface used here is:

- LH-doublet chain assembly from the ratio, matter-assignment,
  alpha=1/3 normalization, and GMN readout authorities;
- `Y(Q_L) = +1/3`, `Y(L_L) = -1`, and the derived LH charge table only;
- explicit exclusions for full-spectrum anomaly, GUT-normalization, and
  `sin^2(theta_W)` claims.

Within that supplier chain, the two intermediate authorities named by the
ledger scope are cited here as direct dependency edges. The matter-assignment
authority is
[`LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md`](LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md)
(carried as algebraic decoration under its consolidation parent
`graph_first_su3_integration_note`; consult the pipeline-derived live ledger
for current dependency-chain standing), which splits the
LH-doublet sector into the SU(3)-fundamental `(2,3)` block and SU(3)-singlet
`(2,1)` block used by B1. The alpha=1/3 normalization authority is
[`HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md`](HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md),
whose bounded arithmetic conclusion `alpha = +1/3`, equivalently
`Y(L_L) = -1`, is exactly the normalization this note inherits.

From the source note's own statement (not the ledger scope), the notation
used below: `Y = (1/3)P_sym - P_anti`, with the `(2,3)` block carrying
`Q_L` and the `(2,1)` block carrying `L_L`.

Therefore the ABJ B1 arithmetic may cite bounded P-HY support for the
left-handed `Y` values. The physical statement remains narrow:

- P-HY is supplied only for the bounded left-handed anomaly-trace surface;
- P-ABJ remains the external anomaly-to-inconsistency premise;
- P-COMP remains the opposite-chirality SU(2)-singlet completion
  premise/derivation;
- P-REC remains the anomaly-carrying chirality-reconstruction
  premise/derivation;
- B-AXIS remains outside the ABJ bridge and is needed only by the parent
  theorem's final `d_t = 1` cap.

No new axiom, primitive, Tier-A admission, or additional local hypercharge
normalization is introduced by this wiring note. The edge explicitly inherits
the upstream `alpha=1/3` normalization, including its equivalent
`Y(L_L)=-1` electron-charge convention.

## Theorem

Let the ABJ bridge's B1 step be the left-handed perturbative anomaly-trace
calculation over the graph-first nonabelian `SU(2) x SU(3)` content and a
bounded left-handed abelian generator. Suppose the current authority surface
contains the hypercharge-identification source with the ledger scope quoted
above together with the source note's stated operator form:

```text
Y = (1/3)P_sym - P_anti,
spec(Y on LH doublet surface) = {+1/3 on (2,3), -1 on (2,1)}.
```

Then the B1 input

```text
(2,3)_{+1/3} + (2,1)_{-1}
```

is a bounded supplier edge rather than an unsupported local premise.
The anomaly traces used by B1 are exactly:

```text
Tr[Y]       = 6*(1/3) + 2*(-1)       = 0,
Tr[Y^3]     = 6*(1/3)^3 + 2*(-1)^3   = -16/9,
Tr[SU(3)^2Y]= 2*(1/2)*(1/3)          = 1/3,
Tr[SU(2)^2Y]= 3*(1/2)*(1/3)+(1/2)*(-1)=0,
Tr[SU(3)^3] = 2.
```

The proof is source-edge matching plus exact rational arithmetic. It inherits
the upstream absolute normalization/electron-charge convention; it introduces
no additional normalization at B1. Right-handed completion and a full physical
Standard Model interpretation are not used in this left-handed trace step.

## Boundary

This note does not derive full physical hypercharge from first principles. It
only wires the ABJ bridge's B1 left-handed arithmetic to an already
bounded source.

This note does not close:

- the external ABJ anomaly-to-inconsistency premise P-ABJ/P1;
- the P-COMP completion-shape premise or derivation;
- the P-REC taste-to-Clifford chirality reconstruction premise or derivation;
- the parent theorem's B-AXIS one-clock cap;
- any full-spectrum Standard Model hypercharge or electroweak matching claim
  beyond the hypercharge-identification scope.

**2026-07-10 downstream hygiene.** The supplier-chain inputs are now carried
as direct dependency edges to the L2 matter-assignment and L3 alpha=1/3
normalization authorities (previously reachable only through
[`HYPERCHARGE_IDENTIFICATION_NOTE.md`](HYPERCHARGE_IDENTIFICATION_NOTE.md)),
so upstream drift in either authority re-enters this row for re-audit through
the standard dependency-edge mechanism; this dated line itself moves the note
hash so the row re-enters for re-audit.

## Repair Note

**2026-07-07 scope alignment.** The runner still used the stale
`does not derive` / `full SM spectrum` / `anomaly cancellation` ledger-scope
needle after the 2026-07-04 hypercharge scope repair. This note and runner now
use the current ledger `claim_scope` wording for the LH-doublet surface and
its exclusions. No claim content changed.

**2026-07-10 dependency-edge repair.** The 2026-07-10 re-audit of this row
returned `missing_dependency_edge`: the note named the matter-assignment and
alpha=1/3 normalization authorities in prose but carried no direct dependency
edges to them. The Result section now links both authorities directly, the
Boundary section carries the dated downstream-hygiene line, and the runner
pins both edges and pipeline-derived chain closure. No claim content changed.

## Verification

The runner checks:

- `HYPERCHARGE_IDENTIFICATION_NOTE.md` is cited at its ledger scope in the
  current audit ledger;
- the hypercharge-identification source note contains the bounded `(2,3)` /
  `(2,1)` eigenvalue surface and its explicit exclusions;
- the ABJ bridge now cites this supplier note and no longer presents P-HY as
  an unsupported declared premise for B1;
- the direct L2 matter-assignment and L3 alpha=1/3 normalization dependency
  edges are present in this note, and the pipeline reports chain-satisfying
  dependency closure (for L2, through its consolidation parent);
- the B1 anomaly traces are recomputed exactly over rational numbers;
- branch/file-scope hygiene is enforced by review tooling rather than claimed
  by the science runner.

Expected runner result: `TOTAL: PASS=26 FAIL=0`.
