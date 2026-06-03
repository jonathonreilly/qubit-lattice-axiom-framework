# Cluster-Decomposition Parent Discharge via Three Companions — Ledger-Pairing Note

**Date:** 2026-06-03
**Claim type:** meta
**Status authority:** independent audit lane only. This note does not set
or predict an audit outcome for any cited row; later status is generated
by the audit pipeline after independent review.
**Primary runner:** [`scripts/frontier_cluster_decomposition_discharge_via_three_companions_ledger_pairing_verifier.py`](../scripts/frontier_cluster_decomposition_discharge_via_three_companions_ledger_pairing_verifier.py)
**Cache:** [`logs/runner-cache/frontier_cluster_decomposition_discharge_via_three_companions_ledger_pairing_verifier.txt`](../logs/runner-cache/frontier_cluster_decomposition_discharge_via_three_companions_ledger_pairing_verifier.txt)

**Authority role:** ledger-pairing meta-note. Bundles the three
already-on-main companions whose joint content addresses the three named
auditor-conditional items recorded against the parent
[`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
(effective_status `audited_conditional` on `origin/main`). Cross-refs only;
no new science.

---

## §0. Why this note exists

The parent
[`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
is currently `audited_conditional` on `origin/main`. The audit-lane
verdict identifies three named conditional items that, together,
bound the parent's open work:

- **Item (a) — Missing spatial-gap / Lieb-Robinson clustering bridge.**
  The parent's L2 unconditional spatial cluster-decomposition claim is
  not closed. The auditor explicitly asks for a retained spatial
  gap-plus-LR or spatial transfer-matrix bridge, both for the temporal
  slice (gap-input-conditional bridge) and the spatial slice
  (slab-operator bridge plus a finite-Λ spatial gap).

- **Item (b) — Equation (8) Kubo-identity defect.** The parent's Step 4
  sketch cites a Kubo identity in the form
  `⟨A_x B_y⟩_ρ − ⟨A_x⟩_ρ ⟨B_y⟩_ρ = − ∫_0^β dτ ⟨[A_x, B_y(iτ)]⟩_ρ`,
  which is not an algebraic identity for general bounded operators
  (counterexample at H=0). The auditor flagged this as a load-bearing
  defect in the parent's connective tissue between Lieb-Robinson and
  thermal cluster decay.

- **Item (c) — Lieb-Robinson interaction-degree constant.** The
  parent's equation (1) defines `v_LR = 2 e J R_int Z_lat` with
  `J := max_X ‖h_X‖` (per-term operator-norm maximum). The
  Hastings-Koma / Nachtergaele-Sims Lieb-Robinson series requires the
  per-site sum `J* := max_x Σ_{X ∋ x} ‖h_X‖`. The auditor flagged the
  difference as a named-constant arithmetic-loss defect, structurally
  harmless to the (L1) form but quantitatively wrong on the cited
  constant.

THREE companions on `origin/main` jointly address these three items:

1. [`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md)
   — `retained_bounded` on main; supplies the temporal-direction
   bridge slice of item (a).

2. [`CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md)
   (`audited_conditional`) plus
   [`CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02`](CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md)
   (`unaudited`) — together supply the spatial-direction bridge slice
   of item (a) plus the finite-Λ spatial gap input the slab note
   admits as H1+H2.

3. [`CLUSTER_DECOMPOSITION_PARENT_EQ8_REPAIR_NARROW_NOTE_2026-06-02`](CLUSTER_DECOMPOSITION_PARENT_EQ8_REPAIR_NARROW_NOTE_2026-06-02.md)
   — `unaudited` on main; explicitly addresses items (b) eq(8)
   deletion + (c) `J→J*` correction in a single narrow companion.

This note pairs those three companions into a single audit-graph entry
so the audit lane can review them jointly as the proposed discharge
package against the parent's three named conditional items. It does
**not** modify the parent or any companion text; it does **not** lift
any row's status; status authority remains the independent audit lane.

---

## §1. Parent recap (read-only)

The parent
[`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
records, on `A_min`, the axiom-first Lieb-Robinson commutator bound
(L1), the lattice light cone (L3), and a Cl(3)-specific operator-norm
constant (L4). It also states (L2) exponential clustering as
conditional on a temporal transfer-matrix gap `Δ_T > 0` supplied by the
mass-gap bridge note. The unconditional L2 form and the spatial
cluster-decomposition step are explicitly out of the parent's
load-bearing scope.

Ledger metadata snapshot (`origin/main` at writing time):

```
note_id          : axiom_first_cluster_decomposition_theorem_note_2026-04-29
claim_type       : bounded_theorem
effective_status : audited_conditional
audit_status     : audited_conditional
```

Three named auditor-conditional items, restated literally:

> *(a)* missing spatial-gap / Lieb-Robinson clustering bridge: derive
> `Δ_T > 0` on the canonical Cl(3) ⊗ Z³ staggered+Wilson Hamiltonian
> and add a retained spatial cluster-decomposition theorem with
> constants; until then, retain only L1/L3/L4 plus the conditional
> temporal gap-to-clustering support.

> *(b)* parent equation (8) Kubo identity in Step 4 is not an
> identity for general bounded operators; the algebraic chain in the
> parent's Step 4 sketch must be routed through a corrected
> bridge.

> *(c)* parent equation (1) uses the per-term operator-norm
> maximum `J = max_X ‖h_X‖`, whereas the Hastings-Koma /
> Nachtergaele-Sims Lieb-Robinson series demands the per-site sum
> `J* = max_x Σ_{X ∋ x} ‖h_X‖`. The named velocity constant
> underestimates the correct LR speed.

---

## §2. The three companions (cross-refs only)

### §2.1. [`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md) — discharges the temporal slice of item (a)

Ledger snapshot:

```
note_id          : cluster_decomposition_mass_gap_bridge_theorem_note_2026-05-09
claim_type       : bounded_theorem
effective_status : retained_bounded
audit_status     : audited_clean
```

What it proves (theorem (B) of that note, restated for cross-ref only):

> Let `T` be the canonical reflection-positivity-reconstructed
> temporal transfer matrix on `H_phys` (finite-dim on every finite
> block `Λ`), with `M_T := λ_max(T) > 0`, `λ_1` the second
> eigenvalue, and `Δ_T := -log(λ_1 / M_T) ≥ 0`. If `Δ_T > 0` (the
> mass-gap input), then for any two local Cl(3) operators `A_x, B_y`
> separated by `n` lattice units along the temporal direction:
>
>   `| ⟨A_x B_y⟩_0 − ⟨A_x⟩_0 ⟨B_y⟩_0 | ≤ ‖A_x‖ · ‖B_y‖ · exp(-n · Δ_T)`.
>
> The finite-temperature bound at inverse temperature `0 < β < ∞`
> picks up an explicit excited-state thermal-weight correction
> `6 q_β`, with `q_β` the finite-block thermal weight of `P_⊥`.

The bridge proof uses only finite-dimensional spectral decomposition,
Cauchy-Schwarz on the off-diagonal sum, and trace-distance control —
the exact toolkit the parent's Step 4 sketch *should* have used in
place of the (false) eq(8) Kubo identity.

**How this discharges the temporal slice of item (a).** The mass-gap
bridge replaces the parent's eq(8) bridge from Lieb-Robinson to
thermal-correlator decay with a closed-form finite-block spectral
lemma in the temporal direction, conditional on a single named gap
input `Δ_T > 0`. The temporal direction of the parent's open
unconditional L2 is reduced to that one named gap input. The bridge
runner exhibits the gap-required no-gap counterexample (E4 of the
mass-gap note) showing the gap is genuinely required.

The gap input `Δ_T > 0` itself is left open by the bridge; the parent
also wires the finite-Λ temporal-gap support note
[`CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19`](CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md)
as a one-hop candidate dependency on the pure-Wilson surface.

### §2.2. [`CLUSTER_DECOMPOSITION_PARENT_EQ8_REPAIR_NARROW_NOTE_2026-06-02`](CLUSTER_DECOMPOSITION_PARENT_EQ8_REPAIR_NARROW_NOTE_2026-06-02.md) — discharges item (b) and item (c)

Ledger snapshot:

```
note_id          : cluster_decomposition_parent_eq8_repair_narrow_note_2026-06-02
claim_type       : bounded_theorem
effective_status : unaudited
audit_status     : unaudited
```

Two narrow repairs in a single companion (see that note §2 and §3):

- **Repair (R-A): eq(8) Kubo identity deletion.** Lemma R-A.1 of the
  eq8 note proves the parent's eq(8) is not an identity by explicit
  two-qubit counterexample at `H = 0` (LHS = 1, RHS = 0, gap = 1
  exactly). The repair statement deletes eq(8) from the parent's
  Step 4 and routes the conditional L2 statement through the two
  bridge notes already wired as parent dependencies: the temporal
  mass-gap bridge (§2.1 above) and the spatial slab bridge (§2.3
  below). The runner verifies the counterexample arithmetic exactly
  on a finite Hilbert space.

- **Repair (R-B): Nachtergaele-Sims `J → J*` correction.** Lemma R-B.1
  of the eq8 note proves the corrected Lieb-Robinson velocity
  `v_LR* := 2 e J* R_int Z_lat` with the per-site sum
  `J* := max_x Σ_{X ∋ x} ‖h_X‖` is the correct rate constant for the
  iterated commutator series. The strict inequality `J ≤ J*` (with
  equality only when each site is touched by exactly one local term)
  is generic on any cubic lattice with `Z_lat ≥ 2`. The runner
  constructs explicit local Hamiltonians and verifies `J < J*`
  strictly where multiple terms touch one site.

**How this discharges items (b) and (c).** The eq8 repair note ships
the two narrow repairs as a single class-A algebraic-identity check
companion. It does not modify the parent text; it states the corrected
versions of eq(1) and eq(8) as a separate narrow source-note that the
audit lane can review on its own claim-boundary surface.

### §2.3. [`CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md) + [`CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02`](CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md) — together discharge the spatial slice of item (a)

Ledger snapshots:

```
note_id          : cluster_decomposition_spatial_slab_bridge_theorem_note_2026-05-17
claim_type       : bounded_theorem
effective_status : audited_conditional
audit_status     : audited_conditional

note_id          : cluster_decomposition_delta_x_finite_lambda_axis_permutation_narrow_note_2026-06-02
claim_type       : decoration
audit_status     : audited_decoration
```

What the spatial slab bridge note proves (theorem (S), restated for
cross-ref only): on the same finite-block surface as the temporal
mass-gap bridge, conditional on H1 (existence of a positive Hermitian
slab transfer operator `T_x` along one lattice direction `x ∈ {1,2,3}`)
and H2 (a spatial transfer-matrix spectral gap `Δ_x > 0`), the
finite-block spatial connected correlator at slab-separation `d`
satisfies `|⟨A_p · T̃_x^d · B_q⟩_0 − ⟨A_p⟩_0 ⟨B_q⟩_0| ≤ ‖A_p‖ ‖B_q‖ ·
exp(-d · Δ_x)`. The slab-bridge proof is the exact spatial-direction
mirror of the temporal mass-gap bridge: finite-dim spectral
decomposition + Cauchy-Schwarz + trace-distance control. The audited
verdict explicitly recorded a `missing_bridge_theorem` repair-target —
namely a retained one-hop authority constructing the positive Hermitian
spatial slab transfer operator and proving `Δ_x > 0`.

What the axis-permutation companion supplies: on the pure-Wilson
finite-Λ surface, the retained temporal-axis theorem
[`CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19`](CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md)
relabels axis-symmetrically to any of the three spatial axes
`μ ∈ {1,2,3}` of Z³, giving a pure-Wilson finite-Λ spatial transfer
operator `T_W^{(μ)}` with simple top eigenvalue and strict positive
gap `Δ_x^{(μ)} > 0` on the same surface. The relabeling uses only
that the SU(3) heat-kernel positivity, the trace-class property on
`L²(SU(3)^E)`, and the Perron-Jentzsch positivity-improving
compact-operator theorem are *axis-label symmetric* — none of them
encodes a "temporal direction" primitive. (The axis-permutation note
is explicit that this is not a new physical isotropy axiom; the
relabeling lives entirely inside the finite-volume Euclidean Wilson
kernel surface.)

**How this discharges the spatial slice of item (a).** The slab bridge
supplies the conditional spectral lemma from H1+H2 to spatial cluster
decay. The axis-permutation companion supplies H1+H2 on the pure-Wilson
finite-Λ surface by axis-relabeling the retained temporal-axis theorem.
Together, the two notes route the parent's open spatial L2 claim to a
finite-Λ pure-Wilson conditional theorem on the same `A_min` surface
the parent already uses.

**Open residual after this pairing.** The pure-Wilson surface does not
include staggered+Wilson fermions; the axis-permutation note explicitly
records the staggered+Wilson fermion-factor extension as an out-of-row
open input. The pure-Wilson finite-Λ closure is sufficient for the
parent's stated `A_min` scope; promotion of the fermion-extended T_full
surface remains conditional on the named determinant-positivity input
in the strong-CP note (also `audited_conditional` per the parent's
2026-05-19 update).

---

## §3. The joint discharge claim

The proposed audit-lane reading of the parent's three named conditional
items, given the three companions on `origin/main`:

- **Item (a) — spatial-gap / LR clustering bridge.** Discharged by the
  pair §2.1 (temporal slice) + §2.3 (spatial slice). Both directions
  are now closed-form conditional spectral lemmas with explicit named
  gap inputs; the axis-permutation companion further supplies those
  gap inputs on the pure-Wilson finite-Λ surface.

- **Item (b) — eq(8) Kubo identity.** Discharged by §2.2 (R-A): explicit
  counterexample + deletion + routing through the two bridges of §2.1
  and §2.3.

- **Item (c) — Lieb-Robinson `J` per-site-sum constant.** Discharged by
  §2.2 (R-B): named-constant correction `v_LR* = 2 e J* R_int Z_lat`
  with `J* := max_x Σ_{X ∋ x} ‖h_X‖`, runner-verified strict inequality
  `J < J*` where it matters.

The joint claim of this ledger-pairing note is the conjunction:
the three named conditional items are simultaneously addressed by the
three companions, and the audit lane is invited to review them as a
single discharge package against the parent's three named items.

This is a **statement of pairing, not of discharge by this note**.
Whether each individual companion's claim closes its targeted item
remains the audit lane's call on each companion's own claim-boundary
surface.

---

## §4. What this note does NOT do

- **Does not modify the parent text.** The parent
  `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md` is
  untouched by this PR.

- **Does not modify any of the three companion texts.** Each of the
  three companions (mass-gap bridge, eq8 repair, spatial slab bridge,
  axis-permutation) is untouched by this PR.

- **Does not lift the parent's `audited_conditional` status.** Status
  authority lies entirely with the independent audit lane.

- **Does not lift any companion's status.** In particular, this note
  does not promote the `unaudited` eq8 repair or `unaudited`/`decoration`
  axis-permutation companions, and does not relax the
  `audited_conditional` flag on the spatial slab bridge.

- **Does not introduce new axioms, imports, or framework primitives.**
  Every load-bearing input is one of the cited companions on `origin/main`.

- **Does not predict an audit outcome.** This note's `claim_type=meta`
  declaration is a source-side declaration; the audit lane decides
  whether the pairing constitutes a discharge package, on its own
  audit-lane standards.

- **Does not derive new science.** The three companions each carry
  their own load-bearing scope; this note pairs their existing
  scopes against the parent's three named conditional items.

---

## §5. Audit-lane handoff

The audit lane is invited to review the three companions jointly as the
proposed discharge package for the parent
`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`'s three named
conditional items. Suggested review order (least to most disruptive to
the parent text):

1. [`CLUSTER_DECOMPOSITION_PARENT_EQ8_REPAIR_NARROW_NOTE_2026-06-02`](CLUSTER_DECOMPOSITION_PARENT_EQ8_REPAIR_NARROW_NOTE_2026-06-02.md) — narrow algebraic-identity-check companion, two named repairs; touches only the parent's Step 4 sketch and eq(1) constant.

2. [`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md) — `retained_bounded` / `audited_clean`; temporal slice of item (a) (already audited clean on main).

3. [`CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md) + [`CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02`](CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md) — spatial slice of item (a); requires reviewing the slab-bridge's named H1+H2 admissions against the axis-permutation companion's pure-Wilson finite-Λ T_x construction.

If the audit lane judges the joint package discharges all three named
conditional items at the parent's stated `A_min` scope (with the
staggered+Wilson fermion-extended T_full surface explicitly left
out-of-row), the parent row's promotion path is unblocked; if not, the
audit lane records which specific item remains conditional and on which
companion's surface the residual lives. Either outcome is internal to
the audit-lane review of the existing on-main rows; nothing in this
note presupposes which.

---

## §6. Runner pairing

The paired verifier
[`scripts/frontier_cluster_decomposition_discharge_via_three_companions_ledger_pairing_verifier.py`](../scripts/frontier_cluster_decomposition_discharge_via_three_companions_ledger_pairing_verifier.py)
performs the audit-lane-readable cite-checks on the parent and each of
the three companions, verifies the named-item content match of each
companion to the parent's conditional items, and exercises the
hostile-audit invariants (parent text untouched, each companion text
untouched, no status lift, no science change). Cached output at
[`logs/runner-cache/frontier_cluster_decomposition_discharge_via_three_companions_ledger_pairing_verifier.txt`](../logs/runner-cache/frontier_cluster_decomposition_discharge_via_three_companions_ledger_pairing_verifier.txt).

---

## Provenance and discipline

- `claim_type=meta` — pure ledger-pairing source note; no new science.
- All four cited rows verified on `origin/main` with their current
  on-main effective_status snapshot at the time of writing (see ledger
  snapshots above).
- This note creates exactly two new files on `origin/main`: the note
  itself and the paired verifier; plus the cached runner log.
- Branch: `science/cluster-decomposition-discharge-via-three-companions-ledger-pairing-2026-06-03`.
