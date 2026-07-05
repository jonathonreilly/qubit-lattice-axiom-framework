# Hierarchy Dimensional Compression Audited-Scope Narrowing Bounded Note

**Date:** 2026-05-10
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/frontier_hierarchy_dimensional_compression.py`](../scripts/frontier_hierarchy_dimensional_compression.py)

## Why this note exists

The 2026-05-05 audit pass on the parent
`HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md`
returned `audited_numerical_match` (load-bearing-step class G,
criticality `critical`, transitive descendants 265) with the explicit
verdict:

> The runner genuinely computes the condensate-density ratio from its
> finite lattice Dirac operator and then performs the advertised root
> comparisons. However, the load-bearing conclusion is a numerical
> closeness claim at chosen parameters and against the imported
> observed prefactor C_obs, not a first-principles closure of the
> physical determinant-to-VEV map. The note itself caveats that the
> sign, placement, order parameter derivation, and full
> determinant-to-VEV theorem remain open.

with re-audit guidance:

> missing_bridge_theorem: derive the effective-potential-density bridge
> showing exactly how the Lt block normalization enters the physical
> VEV formula, including sign and normalization.

This note narrows the parent's audited scope into the explicit numerical
closeness content that the runner does close, separated from the open
effective-potential-density bridge.

This is a bounded scope-narrowing companion of an existing audited
note. It does not add a new axiom, does not add a new repo-wide theory
class, does not propose a status promotion, and does not modify the
parent note's audit ledger row.

## Prior audit feedback summary (previous revision; not current status)

- Prior verdict label: `audited_numerical_match`
- Prior audit date: 2026-05-05
- Prior chain-closes result: false
- `claim_scope` (audited): "Audited the bounded numerical diagnostic
  that a chosen Lt condensate-density residual, when compressed as a
  dimension-4 density, is closer to the observed v_obs/v_pred prefactor
  than a direct sixteenth-root scale correction."
- `chain_closure_explanation` (audited): "The arithmetic in the runner
  matches the note, but the physical bridge identifying the Lt residual
  as entering a dimension-4 effective potential density with the stated
  sign and placement is explicitly left open. The comparison also
  depends on selected numerical inputs rather than a closed derivation
  from the restricted packet."

The parent note's `Interpretation`, `Practical conclusion`, and `What
is still open` sections already record the same boundary in source
form. This narrowing companion isolates the **within-scope numerical
content** that the prior audit feedback accepted as a numerical match.
The current row remains unaudited until the independent audit lane
reviews this new companion note.

## Narrow within-scope content (what the audited row does close)

Inside the prior bounded numerical-diagnostic scope, the runner
verifies the following arithmetic identities, each of which is
independent of the open effective-potential-density bridge:

| Audited content | Class | Status |
|---|---|---|
| Condensate-density ratio `R = cond(L_t=10) / cond(L_t=2) ~= 1.15469` from the registered finite lattice Dirac operator | computed numerical input | prior parent runner PASS |
| Direct scale-like sixteenth-root compression: `R^(-1/16) ~= 0.99105` | exact arithmetic on `R` | prior parent runner PASS |
| Dimension-4 effective-potential-like fourth-root compression: `R^(-1/4) ~= 0.96468` | exact arithmetic on `R` | prior parent runner PASS |
| Comparison versus imported observed prefactor `C_obs = v_obs / v_pred ~= 0.96692` | comparator arithmetic against external pin | prior numerical-match feedback |
| Dimension-4 fourth-root compression lies in the right few-percent range relative to `C_obs`; sixteenth-root compression is too small | within-scope ordering claim | prior numerical-match feedback |

The within-scope conclusion is a numerical-ordering statement: among
the two compression candidates probed, the dimension-4 fourth-root is
the one in the few-percent range of the imported `C_obs`, while the
direct sixteenth-root is too small. This is a non-trivial computational
diagnostic, but it is **not** a derivation of the dimension-4 bridge
from framework primitives.

## What the narrow scope does **not** close

The prior audit feedback and the parent's own `What is still open`
section already flag these explicitly. This companion note records them
in one place for re-audit traceability:

- the **effective-potential-density bridge** itself: a retained derivation
  showing exactly how the `L_t > 2` block normalization enters the
  physical VEV formula, including the sign and the placement of the
  correction;
- the order-parameter derivation: a retained statement that the
  physical order parameter is a dimension-4 effective-potential density
  rather than a direct scale (the parent note treats this as a
  conditional "if");
- the full `det -> v` theorem: a closed derivation of the determinant-
  to-VEV map carrying the dimension-4 normalization;
- elimination of the dependence on selected numerical inputs (the
  prior audit feedback notes the comparison depends on chosen lattice
  parameters and the imported `C_obs`, not on a closed derivation from
  the restricted packet);
- the sibling bridge theorem **Bridge 2** named in
  [`HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md`](HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md);
- promotion of the row from `bounded` to `retained`.

## What would close the open dependency (Path A future work)

Promoting the parent row from `audited_numerical_match` to a retained
theorem-grade derivation would require, per the prior audit feedback's
repair target:

1. an independent retained theorem deriving the effective-potential-
   density bridge with explicit sign and normalization, so the
   compression exponent (`-1/4` versus `-1/16` versus some derived
   alternative) is forced rather than chosen by which root-best-matches-
   `C_obs`;
2. a retained theorem deriving the physical order parameter as a
   dimension-4 effective-potential density (or equivalent) from
   framework primitives;
3. an updated runner that **tests** the derived compression exponent
   (rejecting if the residual deviates from the derived value) rather
   than **scoring** two candidate exponents against the imported
   observed prefactor.

Until at least (1) is supplied, the row remains a bounded numerical-
diagnostic support note at the audited scope.

## Dependencies

- `HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md`
  for the parent audited bounded numerical-diagnostic note.
- [`HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md`](HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md)
  for the sibling endpoint algebra note (prior 2026-05-05 feedback was
  conditional; the same dimension-4 insertion theorem is its **Bridge 2**).

These are imported authorities for a bounded scope-narrowing companion
note. The row remains unaudited until the independent audit lane
reviews this companion, its dependencies, and the runner.

## Boundaries

This companion note does **not**:

- modify the parent note's audit-ledger row;
- promote any current or prior audit verdict;
- derive the effective-potential-density bridge from framework
  primitives;
- claim the dimension-4 fourth-root compression is forced rather than
  selected by best-match-to-`C_obs`;
- extend the audited scope beyond what the parent already declares.

## 2026-06-15 runner/source drift repair

The live runner and SHA-pinned cache expose seven within-scope PASS gates:
five numerical/algebraic diagnostic gates and two source-firewall gates. A
previous revision of this companion still said "5 pass", and the runner's
source-firewall check read the parent
`HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md` instead of this companion. That
created a real re-audit hygiene defect even though the underlying arithmetic
did not change.

This repair makes the runner inspect this companion note directly while still
checking the parent source boundary, and aligns the expected scorecard with the
cache:

- the D=4 inverse compression `R^(-1/4)` is reproduced by independent `pow`
  and `exp(-log/4)` routes;
- the D=4 and D=16 inverse compressions are quantitatively nondegenerate;
- `1/D = 4/2^D` holds at `D=4`;
- the same identity fails at neighboring tested dimensions;
- no PASS gate imports `v_obs`, `v_pred`, or `C_obs`;
- the parent source preserves conditional-support/open-gate scope and the
  companion source declares bounded numerical-diagnostic scope only;
- both parent and companion source surfaces keep the D=4 readout /
  effective-potential-density bridge open.

This repair does not close the missing effective-potential-density bridge and
does not promote the row. It only aligns the note's verification section with
the current runner/cache so re-audit is not blocked by stale scorecard prose.

**Source-firewall restatement.** This is a bounded numerical-diagnostic support
note, not a derivation of the dimension-4 bridge. It does not derive the
effective-potential-density bridge, does not turn the D=4 root into a forced
framework consequence, and does not remove the fact that the D=4 candidate was
selected by best-match-to-`C_obs` in the numerical diagnostic.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_hierarchy_dimensional_compression.py
```

Expected current runner scorecard:

```text
SCORECARD: 7 pass, 0 fail out of 7
```

The runner is the same one cited by the parent note. This narrowing
companion does not introduce a new runner because the bounded within-
scope numerical content is already exercised. The new content is the
explicit scope-narrowing recording of which arithmetic identities the
prior audit feedback accepted as a within-scope numerical match versus
what remains open as the effective-potential-density bridge.

```yaml
claim_id: hierarchy_dimensional_compression_audited_scope_narrow_bounded_note_2026-05-10
note_path: docs/HIERARCHY_DIMENSIONAL_COMPRESSION_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md
runner_path: scripts/frontier_hierarchy_dimensional_compression.py
proposed_claim_type: bounded_theorem
deps:
  - hierarchy_dimensional_compression_note
  - hierarchy_effective_potential_endpoint_note
audit_authority: independent audit lane only
```
