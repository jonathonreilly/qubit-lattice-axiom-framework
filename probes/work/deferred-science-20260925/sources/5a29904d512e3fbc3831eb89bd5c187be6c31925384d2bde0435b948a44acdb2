---
claim_id: dynamics_clause_charges_are_gauss_defects_no_qubit_carries_a_covariant_charge_under_full_soldering_defects_are_bosons_and_record_phases_are_pure_gauge_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting: doubled coordinates with soldered links, as required for a covariant oriented link field (open PR 9066). (i) Under full soldering the stabilizers of the four roles (orders 24, 8, 8, 24) fix no Bloch axis, so no qubit of any role carries a covariant nonconstant charge. (ii) A vertex-link bond is fixed by the four quarter-turns about the link axis. A covariant two-site term on it flips the soldered link only when the vertex is fully soldered too (flip dimensions 0, 0, 0, 2 for the trivial, sign-twist, axis and full vertex actions), and a fully soldered vertex has no covariant charge. So under the landed actions no two-site term transfers charge between a vertex qubit and the field. (iii) With a soft vertex Gauss energy U sum_v (div E_v)^2: one flip from an ice state costs 2U and leaves charges +1 and -1; flipping a link that carries a defect's field onward to a neutral vertex keeps the energy and moves the defect. For hops that are bare single-link flips, as in this supplied model, flips on distinct qubits commute, so the Levin-Wen T-junction relation has phase 1 and the defects exchange as bosons. (iv) The fourth-order ring element on a plaquette is -5/(2U^3) times the product of the four flip amplitudes along the ring, phases included, as checked by exact effective Hamiltonians for random complex transverse fields. Its phase is a lattice curl of the link amplitude phases. A link rephasing, which commutes with the Gauss energy, makes every flip amplitude real, so for purely transverse record fields the phases are pure gauge at every order. (v) With unequal field sizes the fourth-order diagonal energy differs between ice configurations. Finite certificates. The dynamics clause, soldering, the soft Gauss energy and the record fields are supplied, not adopted. No charge assignment, statistics of any Standard Model field or photon phase is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_charges_are_gauss_defects_2026_09_24.py
---

# Charges are Gauss defects

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** supplied models and finite certificates; unaudited.

## Result

Open PR 9066 found that an oriented link field is covariant under full
soldering alone. This note asks where a U(1) charge can then live.
- **Not on a qubit.** Under full soldering, no site of any role has a
  covariant charge. Under the other landed actions, some qubits do have
  one: the sign twist at every role, and axis soldering at link and
  plaquette sites. Theorem 2 then shows those charges cannot reach a
  soldered link field.
- **Not moved by the clause.** No covariant two-site term moves charge
  between a vertex qubit and the field, under any landed vertex action.
- **The covariant charge is a star.** It is `div E_v`, on the six links
  around a vertex.

With a soft Gauss energy, the charges are defects of the Gauss law:
- they cost `U` each;
- they are made in pairs and moved one link at a time by record-field
  flips;
- they exchange as bosons.

The same flip amplitudes build the fourth-order ring, with coefficient
`−5/(2U³)` times their product. Rephasing each link, which commutes with
the Gauss energy, makes every flip amplitude real. So for transverse
record fields the phases are pure gauge at every order, and they create no
background flux for the ring or for the charges. Only the field magnitudes
matter.

## Setting and decision points

- **Roles.** Doubled coordinates as in open PR 9066 (D-roles).
- **Fields.** Links are soldered, with `E_l = s_l · ê_l` (D-sold).
- **Gauss law.** A soft vertex Gauss energy `U Σ_v (div E_v)²` (D-gauss).
- **Dynamics.** The dynamics clause of open PR 9040 (D-dyn). Records act as
  fields and give transverse link fields (open PRs 9041, 9066; D-pattern).

None is adopted. The four landed vertex actions are those of the landed
soldering menu: trivial, sign twist, axis and full.

## Theorem 1 — no qubit carries a covariant charge

Under full soldering, the stabilizers of a vertex, link, plaquette and cube
site have orders 24, 8, 8 and 24.
- No Bloch axis is fixed by the whole stabilizer. At a link or plaquette
  site, the half-turns across the main axis reverse it, and the
  quarter-turns move the others.
- So no one-qubit observable other than a constant is covariant at any
  site.

The covariant charge at a vertex is the star observable
`div E_v = Σ_l s_l · n(v→l)` (open PR 9066). It lives on the vertex's six
link neighbours: the set Admissibility conditions the vertex on.

## Theorem 2 — the clause moves no charge between a qubit and the field

A vertex–link bond is fixed by the four quarter-turns about the link axis.
- A quarter-turn multiplies the soldered link's raising and lowering
  operators by `±i`.
- A covariant two-site term that flips the link needs a vertex operator
  with the opposite phase. Among the landed actions, full soldering alone
  gives such phases:
  - trivial: 1;
  - sign twist: ±1;
  - axis: ±1.
- A fully soldered vertex has no covariant charge (Theorem 1).

So no covariant two-site term changes both a vertex charge and the field
of an adjacent soldered link. The runner finds link-flip dimensions 0, 0,
0 and 2, and charge-transfer norms at machine zero.

## Theorem 3 — soft Gauss defects are bosonic charges

Use `H_0 = U Σ_v (div E_v)²` with `E_l = ±1/2`.
- **Pairs.** Flipping one link of an ice state leaves charges `+1` and `−1`
  at its ends, at cost `2U`.
- **Hops.** A defect with charge `+1` has four outgoing links. Flipping one
  whose far end is neutral moves the defect across it and leaves the energy
  unchanged. The hop is first order in the record field, with amplitude
  equal to the flip amplitude.
- **Statistics.** In this supplied model the hops are bare single-link
  flips. Flips on distinct qubits commute, so the Levin–Wen T-junction
  relation `t₁ t₂† t₃ = t₃ t₂† t₁` holds with phase 1: the defects exchange
  as bosons.
  - The independent checker built an explicit T-junction with two `+1`
    defects on the L = 6 torus. Every intermediate energy was `4U`, and
    the two orders agreed with amplitude ratio 1.
  - Hops dressed with string operators, which this model does not have,
    could make charges fermions.

## Theorem 4 — record phases are pure gauge

Let `t_l` be the amplitude with which link `l`'s record field flips it
from its value in one flippable configuration to its value in the other.
Through fourth order the ring element is

    ⟨b|H_eff|a⟩ = −(5 / (2U³)) · t_b t_r t_t t_l ,

phases included. The energy denominators of open PR 9066 do not depend on
the field.
- Pair creation, carrying one member around the plaquette and annihilation
  apply the same four flips, so a defect's loop amplitude carries the same
  product.
- Let `τ_l` be each link's `+ → −` amplitude. The product is
  `τ_b τ_r τ̄_t τ̄_l`, and its phase is the lattice curl of the link
  phases `arg τ_l`. It sums to zero over the faces of every cube, and
  rephasing each link's field basis removes it.
- So every ring element is negative real in that gauge: the ring is
  unfrustrated and charges see no background flux.
- The rephasing commutes with the Gauss energy and makes every transverse
  flip amplitude real. So the phases are removable exactly, at every
  order, not only at fourth.

What remains of the record fields is their magnitudes:
- unequal magnitudes give plaquette-dependent ring strengths;
- they also give a configuration-dependent diagonal energy (check 6), so
  equal magnitudes are what give `V = 0` in open PR 9066.

## What this means for the lanes

- **Charged matter.** In this supplied setting (a soft Gauss energy `U` and
  transverse record fields, both decision points), U(1) charge is a
  collective star observable. It is conserved in the emergent low-energy
  sense, since a single flip makes a pair. Its quanta are Gauss defects:
  - gapped, at `U` per unit charge squared;
  - hopping at first order in the record fields;
  - bosons, for bare single-link flips.
- **The photon lane.** Its supplied three-site hops of permanent records
  (the landed
  `HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md`)
  move charges carried by vertex states. There they are a supplied
  three-state vertex memory. Theorem 2 shows that for qubit vertices, no
  covariant two-site term moves such charges under any landed action. In
  the soft-Gauss setting, the defects are the charges.
- **Fermions.** Charged fermions are not generated in this supplied model:
  with bare single-link-flip hops the charges are bosons. The fermions the campaign found are the Z2-charged Majoranas of
  the carved Kitaev networks (open PRs 9048, 9054). Making charged
  fermions needs more than the soft Gauss law and single-link flips.

## Checks

The runner has 6 checks and all pass in about 1 s.

| Check | Result |
|---|---|
| No qubit charge | Stabilizer orders 24, 8, 8, 24; fixed Bloch axes 0, 0, 0, 0. |
| No charge transfer | Bond stabilizer of order 4. Link-flip dimensions 0, 0, 0, 2. Charge-transfer norms 5e-16 and 3e-16 for the trivial and sign-twist axes. |
| Defects | On the L = 6 torus a pair costs 2U. All 3 available hops of the `+1` defect keep 2U and move it. |
| Bosons | Bare single-link flips on distinct qubits commute: Levin–Wen relation holds to 8e-17. |
| Pure gauge | One random field set, scaled by h. Exact des Cloizeaux ring element / prediction = 0.99976 and 0.99994 at h/U = 0.03 and 0.015: the deviation falls by 4, as (h/U)². Phase error 4e-8 rad. Largest cube sum of ring phases 4e-15. |
| Magnitudes | Shared-vertex fourth-order part: spread 1e-14 with equal sizes and 0.52 h⁴/U³ with unequal sizes. |

## Independent check

A separate checker wrote its own code without reading this runner. Every
claim passes:
- the stabilizer orders and fixed axes;
- the vertex–link flip dimensions 0, 0, 0, 2, with charge-transfer norms at
  machine zero on the x, y and z axes and 5 random axes;
- 120 random ice states on L = 3, 4 and 6 tori, with no failure;
- an explicit T-junction;
- the ring ratios, with deviations scaling as (h/U)² on each field set;
- pure gauge, with all 192 ring elements on the L = 4 torus negative real
  after rephasing;
- the diagonal energy, matched exactly on a 7-link cluster.

It flagged scope, now corrected:
- the title's soldering is full soldering;
- the soft Gauss energy and record fields are decision points;
- the boson statement holds for bare single-link flips;
- the phases are pure gauge at every order, not only the fourth.

## What this does not do

- It adopts no soldering, Gauss energy or record pattern.
- It assigns no Standard Model charge, and it claims nothing about
  fermionic charges or dyons.
- It does not treat role-dependent actions beyond the vertex–link bond, or
  record fields with longitudinal parts.
- It does not treat orders beyond the fourth.
- It derives no photon phase.
