# REVIEW_HISTORY — registrability-bridges-20260610

## Block 01 — Registrable readout additive+even => phase-free (self review, hostile pass)

Reviewer posture: hostile, semantics-first (stress-test the action-level
identification of symbols, not just the algebra — per the firewall).

### Attack 1 — "additivity over disjoint records != additivity over sectors"

Claim attacked: T2's identification of Record's finite additivity over disjoint
record collections with additivity over the central-sector decomposition.

Resolution: the central-sector decomposition NAMED BY THE RECORD AXIOM is a set
of orthogonal central idempotents; orthogonality `e_j e_k = 0` IS pairwise
disjointness of records. So additivity over the sectors is not a new assumption;
it is (Additivity) applied to the family the axiom already names. VERIFIED in
runner T1 (orthogonality/idempotency/partition) and T2 (interference term forced
to 0). **Holds.**

### Attack 2 — "K/CPT does not negate the phase; you imported that"

Claim attacked: T5's use of `arg z -> -arg z` under K/CPT.

Resolution: this is consumed, not imported. The Tier-A K/CPT note
(`TIER_A_KORBIT_..._2026-06-09.md`, line 45) states verbatim "K/CPT conjugation
sends `z` to `conj(z)`, so `arg z` goes to `-arg z`." The note also states the
hostile guard (cos(arg z) is K-invariant, line 65-66) that this theorem threads.
Consuming an existing surface's identification, not a new import. **Holds.**

### Attack 3 — "you overclaim that (a) is closed"

Claim attacked: whether Consequence A overstates reachability.

Resolution: the note says `partially_closes` — it discharges the determinant
**phase** content of the mass-orientation premise ON THE REGISTRABLE SURFACE,
and explicitly names two residuals: strong-CP premise 1 (separate, RP-no-go'd)
and the standing modeling identification (physical readout satisfies Record
registrability constraints).
The TRACE_GATE and CLAIM_STATUS_CERTIFICATE both record `partially_closes` /
`bounded-support`. No bare "retained". **Holds — correctly bounded.**

### Attack 4 — "additivity ⇒ odd needs continuity (Cauchy/Hamel)"

Claim attacked: T4.

Resolution: NO. `g(0) = g(0)+g(0) ⇒ g(0)=0`; `g(x)+g(-x)=g(0)=0 ⇒ g(-x)=-g(x)`.
Pure group algebra, any abelian group, no regularity. The Cauchy/Hamel pathology
concerns whether additive ⇒ LINEAR (needs regularity); the theorem never claims
linearity — only oddness, which is unconditional. VERIFIED symbolically (T4 via
`solve(g(0)=2g(0))`). **Holds — and this is the crux of why the proof is robust.**

### Attack 5 — "the hostile guard is not actually threaded"

Claim attacked: T6 / whether cos(arg z) is properly excluded.

Resolution: the theorem does NOT conclude "K-even ⇒ phase-free". It concludes
"additive ∩ even ⇒ phase-free". cos(arg z) is K-even but fails additivity
(`cos(a1+a2) != cos a1 + cos a2`, verified 6/6 numerically + symbolically), so it
is excluded by the ADDITIVITY premise before evenness is invoked. The guard is
threaded structurally. **Holds.**

### Attack 6 — "R2 should be closable; you're hiding behind 'external math'"

Claim attacked: the R2 bound.

Resolution: R2 is the global geometric identification `Cl(3)/Z^3 -> PL S^3 x R`,
a manifold-topology statement (Perelman/Moise/van Kampen). It is category-
disjoint from "what scalar Record registers". The note's N1 table names 6 routes
including "Record-registrability closes R2" (RULED OUT, category mismatch) and
"unordered-multiset bridge avoids R2" (SUCCEEDS — (b-i) closes independently of
R2). So R2 is correctly isolated as off-layer and import-required, and (b-i) does
not need it. **Holds — bounded honestly, not hidden.**

### Disposition

**pass.** All six hostile attacks resolve with existing-surface grounding and
runner verification. The note is correctly bounded (partially_closes (a); closes
(b-i); bounds (b-ii)), uses author-side status language only, threads the hostile
guard structurally, and names every residual. Independent audit still required.

Severity of any unresolved issue: none load-bearing. No demotion or block
warranted.

### Carried to HANDOFF for later repo-wide integration (NOT done in this run)

- Proposed (audit-lane-owned, NOT enacted): once this theory chain + the
  AC_phi_lambda basis audits land, the AC_phi_lambda residual may be eligible for
  the conventions class (Y0 precedent) per PR #3428 — an owner/audit registry
  decision, recorded only as a future path.
- PR #3511 (GATED theta retirement): its named PENDING gate is blocker (a); this
  PR supplies the det-readout bridge that lifts the mass-orientation portion of
  that gate. The action-form premise (premise 1) remains a distinct gate. Note
  for the #3511 owner in HANDOFF.
