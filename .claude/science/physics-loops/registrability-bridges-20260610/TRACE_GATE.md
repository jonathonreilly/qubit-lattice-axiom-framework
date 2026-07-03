# TRACE_GATE — registrability-bridges-20260610

## Block 01 — shared-core registrability theorem (additive + K/CPT-even => phase-free)

```yaml
trace_class: direct_blocker_closure
target_claim_id:
  - tier_a_korbit_determinant_and_orientation_invariance_bounded_note_2026-06-09  # source of both blockers
  - strong_cp_theta_zero_note            # consumer of blocker (a)
  - staggered_dirac_realization_gate_note_2026-05-03  # AC_phi_lambda Tier-A carrier (blocker b)
target_blocker_text:
  blocker_a: >
    "To discharge that premise, a later retained bridge must show that the
    physical `arg det(M_u M_d)` contribution used by STRONG_CP_THETA_ZERO_NOTE.md
    is exhausted by this determinant-class registrable readout, and that no
    phase-sensitive non-multiplicative or action-level datum remains relevant to
    that premise. Until that bridge exists, the positive-real mass orientation
    remains an explicit condition of the strong-CP selected surface."
  blocker_b_i: >
    "the orientation lemma may help reduce the admission to a magnitude-only atom
    only after the unordered-multiset registrability bridge is retained or
    confirmed as already supplied by existing audited surfaces."
source_of_blocker_text: handoff   # the TIER_A_KORBIT bounded note's own named-bridge text + PR #3428 owner review
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: >
  Deliver the registrable-readout theorem note + runner; it closes the
  det-class-exhaustiveness ask (a) and the unordered-multiset registrability ask
  (b-i) on the Record layer. It does NOT close strong-CP premise 1 (separate
  action-surface premise) or R2 (b-ii, external-math LIVE).
```

### Exactly how the artifact retires each quoted blocker

**Blocker (a) — det-readout exhaustiveness.** The artifact proves: a
Record-registrable scalar is additive over the disjoint central-sector
decomposition (forced by Record's finite additivity over disjoint records,
applied to orthogonal central idempotents) AND K/CPT-even (forced by Record's
realized-outcome = K/CPT orbit). The determinant phase = additive sector-phase
sum; an additive phase functional is odd; the even part of an odd functional is
zero. Hence on the registrable surface the *only* surviving determinant-class
datum is modulus-type (phase character k=0): the multiplicative determinant
character class is exhaustive for the registrable phase readout, and `arg
det(M_u M_d)` carries no separately-registrable non-multiplicative datum. The
hostile guard is threaded: the proof does NOT use evenness alone (which would
falsely admit `cos(arg z)`); it uses additivity AND evenness, and shows
`cos(arg z)` is excluded by *additivity*.

This `partially_closes` blocker (a): it discharges the determinant-PHASE part
of the mass-orientation premise on the registrable surface. It leaves explicit
(does not claim to close) (i) strong-CP premise 1 ("no bare theta slot",
already RP-no-go'd as a distinct premise), and (ii) the standing modeling
identification that the physical mass-surface readout context IS the
constrained one. Both are stated as the note's boundary.

**Blocker (b-i) — unordered-multiset registrability.** The artifact proves: for
the AC_phi_lambda Hermitian circulant `H(delta)`, `conj(H(delta)) = H(-delta)`,
so the `delta -> -delta` sign flip IS the K/CPT conjugation. The registrable
readout is K/CPT-even, so it cannot carry the sign; the elementary symmetric
polynomials (e1,e2,e3) are all even in `delta` (verified: e3 ~ cos 3delta), and
the sign lives only in the K/CPT-ODD `sin(3 delta)` line (the orientation-odd
`u - v` invariant), which is unregistrable by the same additive+even argument.
Hence the registrable species surface is exactly the unordered multiset
(symmetric functions), reducing AC_phi_lambda to the magnitude-only atom
`|delta|`. This `closes` the unordered-multiset registrability bridge named in
the Registry Consequence.

**Blocker (b-ii) — R2 PL/ABSS global bridge.** NOT on this layer. R2 is the
global geometric identification `Cl(3)/Z^3 -> PL S^3 x R` (manifold topology;
Perelman / Moise / van Kampen), needed for the equivariant eta-invariant /
single-summand readout and the |delta| MAGNITUDE value, not for the
sign-removal registrability question. Honestly bounded as external-math LIVE
(import-required wall), recorded via N1-N8. `negative_route_pruning` on the
claim that R2 blocks the registrability reduction: it does not; (b-i) closes
independently of R2.

## Reachability summary

| blocker | reachability | residual |
|---|---|---|
| (a) det-readout exhaustiveness | partially_closes | premise 1 (separate); standing readout-context identification |
| (b-i) unordered-multiset registrability | closes | the |delta| magnitude still needs R-eta + R2 |
| (b-ii) R2 PL/ABSS global | bounds (external-math LIVE) | Perelman/Moise/van Kampen on framework surface |
