# Supplied PMNS parity data: conditional sign non-identifiability

**Type:** open_gate
**Status:** conditional algebra; numerical selector and physical selection remain open
**Script:** `scripts/frontier_dm_leptogenesis_pmns_stationary_cp_incompatibility_theorem.py`

## Statement and assumptions

Let x,y be real triples and d a real phase. Supply a domain and constraints invariant under d -> -d. Supply an objective even under that reflection. For

    gamma = x1*y3*sin(d)
    E1 = ((x2²+y2²)-(x3²+y3²)+x2*y1-x1*y3*cos(d))/2
    E2 = x1²+y1²+(x2*y1+x1*y3*cos(d))/2
    cp = (-2*gamma*E1/3, 2*gamma*E2/3)

gamma and cp are odd, while E1,E2 are even. Thus admitted reflected points have identical objective and even data. When cp is nonzero, those data cannot uniquely determine its sign. At cp=0 there are no distinct nonzero CP sheets. This does not exclude a point with the desired sign pattern or require abandoning the family or adding an axiom.

## Matrix and objective scope

For the supplied real cyclic matrix C and Y=diag(x)+diag(y1,y2,y3*exp(i*d))*C, H=YY† obeys H(-d)=conjugate(H(d)). With simple eigenvalues and consistent ordering, conjugating eigenvectors preserves their squared component moduli. At degeneracy an individual eigenvector packet needs a basis convention; no unrestricted packet assertion is made. A real positive-definite seed and positive-definite H make the real trace/log-determinant relative action reflection-even. The supplied information cost has a phase-independent KL part and 1-cos(d), hence is even. Transport is reflection-even only when defined as the same functional of the invariant packet. These premises do not assert a complete bank of all possible selector laws.

## Evidence and unresolved diagnostics

The default runner checks symbolic parity and matrix conjugation identities plus a supplied exact sign-pattern control. It does not construct a stationary point, prove a branch count or certify physical admissibility. Numerical eta equality remains tolerance-based, and finite search is not global extremality.

`python3 scripts/frontier_dm_leptogenesis_pmns_stationary_cp_incompatibility_theorem.py --numerical-diagnostic` is a separate numerical diagnostic with unchanged upstream solver tolerances and nonzero failure. The previous canonical batch's stationary refinement failure and removed-API failure are preserved in the repository-linked failed-execution evidence below; their recovery source is Git commit `5cdc3053ebe202748c218fccee1d9d798ece5c92`. Default algebra success does not erase or replace those failures. Physical CP selection, admissible-domain determination and numerical branch certification remain open.

## Related supplied constructions

These references provide context for the numerical diagnostic; the displayed parity proof is self-contained and does not import their closure or global-selection claims.

- [DM_LEPTOGENESIS_PMNS_MULTISTART_SELECTOR_SUPPORT_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_MULTISTART_SELECTOR_SUPPORT_NOTE_2026-04-16.md) — selector-family construction (`selector` module).
- [DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md) — relative-action stationarity (`stat` module).
- [DM_LEPTOGENESIS_PMNS_BREAKING_TRIPLET_SOURCE_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_BREAKING_TRIPLET_SOURCE_LAW_NOTE_2026-04-16.md) — charged-sector triplet-channel source law (`triplet_channels_from_active_data`).
- [DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md) — minimum-information source-law module (`minlaw`).

## Preserved failed execution evidence

[Historical full-command failure stdout](review_evidence/dm-canonical-failures-2026-10-21/frontier_dm_leptogenesis_pmns_stationary_cp_incompatibility_theorem.log) and [recovery/hash manifest](review_evidence/dm-canonical-failures-2026-10-21/manifest.json) remain evidence of the prior failed command, not the new bounded result.

The optional numerical diagnostic now replays only multistart branch construction. It does not replay the former minimum-information or branch-parity portions, nor does it claim their success.

[Conditional-boundary and alternative-route record](review_evidence/dm-canonical-failures-2026-10-21/NO_GO_DISCIPLINE_CHECKLIST.md): partial narrowing, not a universal no-go or packet PASS.

The wrapper is classified as an open gate for this partial narrowing. The
explicit supplied algebra is preserved, but no complete negative-claim packet
or physical selector conclusion is submitted for certification here.
