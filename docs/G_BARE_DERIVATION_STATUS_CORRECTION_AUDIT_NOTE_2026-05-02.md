# g_bare Derivation Note — Status Correction Audit

**Date:** 2026-05-02 (2026-05-24 packet refresh: missing-runner finding
superseded by the now-present `scripts/frontier_g_bare_derivation.py`;
two 2026-05-03 repair-candidate notes cited as audit-declared dependencies)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Status:** status-correction packet for
[`G_BARE_DERIVATION_NOTE.md`](G_BARE_DERIVATION_NOTE.md). This packet does
not promote or demote the parent on its own; the parent's effective status
is set by the independent audit lane.
**Primary runner:** `scripts/frontier_g_bare_derivation_status_audit.py`
**Authority role:** dep-declaration / status-correction packet for the
g_bare derivation residual on the framework's canonical Cl(3) connection
normalization surface.

## 0. Audit context

The parent note `G_BARE_DERIVATION_NOTE.md` proposes that the canonical
Cl(3) connection normalization is identified with unit gauge coupling
`g_bare = 1`. The audit verdict on this status-correction packet (audit
ledger row `g_bare_derivation_status_correction_audit_note_2026-05-02`,
status `audited_conditional`) recorded:

> *"The status-correction note correctly identifies an open
> normalization/rescaling issue in broad terms, but one of its concrete
> load-bearing premises is stale or false under the provided runner output.
> The cited parent authority is retained_bounded but explicitly says the
> parent theorem remains under an open main gate pending two
> repair-candidate audits and re-audit. Therefore the packet supports a
> conditional/open-gate disposition, not a clean terminal status correction
> on the stated missing-runner basis."*

with re-audit note:

> *"runner_artifact_issue: refresh the status-correction packet against
> the current `scripts/frontier_g_bare_derivation.py` state and include
> the two 2026-05-03 repair-candidate notes or mark them as open
> dependencies."*

The present 2026-05-24 refresh addresses both items:

1. The "missing runner" finding (Section 1 below, original 2026-05-02
   wording) is **superseded**. `scripts/frontier_g_bare_derivation.py`
   now exists and is the primary runner for the parent note plus the two
   2026-05-03 repair-candidate notes (verified at 2026-05-24).
2. The two 2026-05-03 repair-candidate notes are now declared dependencies
   (Section 2), with their current audit-lane status documented inline.

The original three-issue framing (constraint vs. convention ambiguity,
missing primary runner, A → A/g rescaling freedom) is retained for
historical record, with each item annotated against the current state.

## 1. Verification of primary runner (superseded; runner now present)

The original 2026-05-02 status-correction packet flagged a missing
primary runner. As of 2026-05-24, that finding is **superseded**:

```bash
$ ls scripts/frontier_g_bare_derivation.py
scripts/frontier_g_bare_derivation.py
```

The runner is now present and is the declared primary runner for:

- `G_BARE_DERIVATION_NOTE.md` (parent);
- `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`
  (repair candidate #2);
- `G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`
  (repair candidate #3 — itself uses
  `scripts/frontier_g_bare_constraint_surface_check.py` as its declared
  primary runner; the present runner also exercises the
  constraint-vs-convention section algebra).

The runner sections that bear on the original three-issue framing are:

- Section A — Cl(3) → End(V = C^8) chiral representation (axiom A1 input).
- Section B — canonical Tr(T_a T_b) = δ_ab/2 normalization on the
  triplet block (the (CN) surface).
- Section C — Wilson plaquette small-a expansion forces
  `β = 2 N_c / g_bare²` (the (WM) matching identity).
- Section D — rescaling `A → c · A` shifts the matched β by c², not
  g_bare (Wilson-action redistribution of the continuum rescaling
  freedom).
- Section E — constraint-vs-convention disambiguation: at N_c = 3, β = 6
  under (CN), g_bare² = 1 follows by exact Fraction arithmetic.
- Section F — end-to-end no-circular-input integration audit.
- Section G — ledger visibility check for the two 2026-05-03 candidate
  rows.

The audit-packet self-verifier
`scripts/frontier_g_bare_derivation_status_audit.py` is the primary runner
for the present status-correction packet (separate from the parent's
primary runner above).

## 2. Declared audit dependencies (2026-05-24 refresh)

The two 2026-05-03 repair-candidate notes are declared dependencies of the
present packet. Their current audit-lane status (read from the live
audit ledger at 2026-05-24) is:

| Authority | Audit-lane status | Role |
|---|---|---|
| [`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md) | current pipeline-derived effective status `retained` | supplies the class-A algebraic identity that the continuum rescaling `A → c · A` routes itself into β rather than into g_bare on the canonical (CN) surface — repair target #2 of this packet. |
| [`G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`](G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md) | current pipeline-derived effective status `retained_bounded` | supplies the class-A algebraic identity that under (CN), (WM), and the local Wilson surface `β = 6` at `N_c = 3`, the unique compatible `g_bare² = 1` — repair target #3 of this packet. |
| [`G_BARE_DERIVATION_NOTE.md`](G_BARE_DERIVATION_NOTE.md) | current pipeline-derived effective status `retained_bounded` | parent note whose original three-issue framing this packet documents. |

Both repair-candidate dependencies are retained-grade on the live ledger.
The packet therefore no longer needs to mark them as "open dependencies";
the present refresh wires them in directly as one-hop authorities.

## 3. The constraint vs. convention ambiguity (refreshed)

`g_bare = 1` can mean either:

**(a) Structural constraint.** A theorem stating that, given a fixed
upstream normalization surface, `g_bare = 1` is the unique compatible
value, with all other values disallowed by the upstream surface's
algebraic structure.

**(b) Convention choice.** A normalization choice fixing the scale of the
gauge connection field A, with `g_bare = 1` chosen as the canonical
value. Equivalent to a units choice for A.

The original 2026-05-02 framing observed that the parent note conflates
(a) and (b). The 2026-05-03 constraint-vs-convention theorem cited in
Section 2 disambiguates this:

- The honest convention/input layer is **upstream** at the canonical
  Cl(3) connection normalization (CN) and the local Wilson evaluation
  surface `β = 6` at `N_c = 3`.
- With those upstream inputs fixed, `g_bare = 1` is a **derived**
  algebraic constraint on the bounded surface, not a separate
  convention layer.

So reading (a) is correct *relative to the upstream surface*, and reading
(b) is correct *for the upstream surface itself*. The two readings are
not contradictory once the surface boundary is drawn.

## 4. The A → A/g rescaling freedom (refreshed)

The continuum gauge action is invariant under field rescaling `A → A/g`:

```text
S_gauge[A; g] = (1/4 g²) ∫ d⁴x F_μν F^μν
            = (1/4) ∫ d⁴x (∂_μ A'_ν - ∂_ν A'_μ + ...)²    (with A' = g A)
```

The original 2026-05-02 status-correction packet recorded that this
rescaling freedom required a theorem removing it. The 2026-05-03
rescaling-freedom-removal theorem cited in Section 2 supplies this
class-A identity: under the canonical (CN) normalization
`Tr(T_a T_b) = δ_ab/2`, the rescaling `T_a → c · T_a` shifts the matched
Wilson coefficient β by c² rather than altering g_bare. The freedom is
therefore routed into β, not into g_bare, and is removed on the (CN)
surface.

This does not pin the canonical normalization itself; the convention
status of (CN) is the subject of
`G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md` (not a
dependency of this packet).

## 5. Seven retained-proposal certificate criteria (refreshed)

| # | Criterion | Pass? (2026-05-02) | Pass? (2026-05-24 refresh) |
|---|---|---|---|
| 1 | `proposal_allowed: true` | NO | not applicable — this packet is status-correction infrastructure, not a parent-promotion proposal |
| 2 | No open imports | NO | parent's open-gate status documented in Section 2; this packet's own load-bearing inputs are the two retained 2026-05-03 rows |
| 3 | No load-bearing observed/fitted/admitted | conflated | disambiguated by the 2026-05-03 constraint-vs-convention theorem; honest input layer is upstream at (CN) + local Wilson `β = 6` surface |
| 4 | Every dep retained | N/A | both declared deps retained on the live ledger (Section 2) |
| 5 | Runner checks dep classes | NO (runner missing) | YES — `scripts/frontier_g_bare_derivation.py` Sections A–G; `scripts/frontier_g_bare_derivation_status_audit.py` for this packet |
| 6 | Review-loop disposition `pass` | PENDING | PENDING (live: `audited_conditional` pending re-audit) |
| 7 | PR body says independent audit required | YES | YES |

The 2026-05-02 reading "Criteria 1, 2, 3, 5 fail" is **superseded** for
items 3 and 5 (constraint-vs-convention is now disambiguated; runner is
present). Item 6 remains pending the next independent re-audit of this
packet. Item 1 is not applicable to a status-correction packet that does
not itself propose parent promotion.

## 6. Recommended status correction (refreshed)

```yaml
# g_bare_derivation_note (parent)
current_status: retained_bounded on the live ledger
audit-lane status set by independent audit; the parent has retained_bounded
effective status, with its bounded boundary documented on the parent note
and via the 2026-05-03 constraint-vs-convention theorem
proposal_allowed: false (no parent-promotion proposal from this packet)
proposal_allowed_reason: |
  (a) the upstream canonical Cl(3) normalization (CN) remains an admitted
      convention layer, classified by
      G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02
  (b) the local Wilson evaluation surface (β = 6 at N_c = 3) is an
      explicit bounded input of the constraint-vs-convention theorem,
      not derived from the one-qubit operator algebra plus Z^3 spatial
      substrate
  (c) the rescaling-freedom removal class-A identity holds on the (CN)
      surface only; absolute pinning of g_bare = 1 from the framework
      axioms remains a separate Nature-grade target
```

## 7. Path to retention (refreshed)

| Required step | Difficulty | Status (2026-05-24) |
|---|---|---|
| Restore or replace `scripts/frontier_g_bare_derivation.py` | medium | DONE (Section 1) |
| Resolve constraint vs. convention ambiguity in note | medium | DONE via `G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md` (retained_bounded) |
| Supply theorem removing A → A/g rescaling freedom on the (CN) surface | hard | DONE via `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md` (retained) |
| Absolute derivation of (CN) and the local Wilson `β = 6` surface from A1 + A2 | Nature-grade | OPEN |

The three repair targets named in the 2026-05-02 packet are now
addressed (top three rows). The remaining absolute-derivation target
(bottom row) is a strictly stronger Nature-grade objective and is **not**
in scope for this status-correction packet.

## 8. Audit-graph effect

After the present 2026-05-24 refresh:

- The packet's "missing primary runner" finding is superseded; the runner
  is present and exercises the full Cl(3) → End(V) → su(3) → Wilson
  chain in Sections A–F.
- The two 2026-05-03 retained repair-candidate notes are declared
  one-hop dependencies; the citation graph picks them up via the
  markdown links in Section 2.
- The parent `G_BARE_DERIVATION_NOTE.md` remains a documented
  cross-reference; its retained_bounded effective status is set by the
  independent audit lane, not by this packet.
- The packet is itself audit-lane infrastructure with `proposal_allowed:
  false` (Section 6); no parent-promotion is implied by the refresh.

## 9. Cross-references

The declared one-hop dependencies are the rescaling-freedom-removal and
constraint-vs-convention theorems plus the parent note, linked in §2.
The remaining cross-references are reader pointers (plain text, not
load-bearing for the citation graph):

- Parent: `G_BARE_DERIVATION_NOTE.md` — retained_bounded on the live
  ledger.
- Sister G_BARE_* family rows (statuses set by the audit lane, not by
  this packet):
  - `G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18`
  - `G_BARE_RIGIDITY_THEOREM_NOTE`
  - `G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02`
  - `G_BARE_TWO_WARD_CLOSURE_NOTE_2026-04-18`
  - `G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19`
  - `G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19`
  - `G_BARE_DYNAMICAL_FIXATION_OBSTRUCTION_NOTE_2026-04-18`
- Cycle 4 connection: `alpha_s_direct_wilson_loop_derivation_theorem_note_2026-04-30`
  imports `g_bare = 1` as a load-bearing structural input — that cycle
  flagged the same admission and is now serviced via the (CN) + local
  Wilson surface reading documented above.

## 10. Honest scoping summary

This packet is **status-correction infrastructure**, not a parent-
promotion proposal. It refreshes the original 2026-05-02 three-issue
framing against the current ledger state:

- the missing-runner finding is superseded (runner now present);
- the constraint-vs-convention ambiguity is disambiguated by the
  retained_bounded 2026-05-03 constraint-vs-convention theorem;
- the rescaling-freedom finding is addressed by the retained 2026-05-03
  rescaling-freedom-removal theorem on the (CN) surface.

The remaining honest boundary is absolute derivation of the upstream
canonical normalization (CN) and the local Wilson `β = 6` evaluation
surface from the one-qubit operator algebra plus `Z^3` spatial
substrate alone. That is a strictly stronger Nature-grade target and is
outside the scope of this status-correction packet.
