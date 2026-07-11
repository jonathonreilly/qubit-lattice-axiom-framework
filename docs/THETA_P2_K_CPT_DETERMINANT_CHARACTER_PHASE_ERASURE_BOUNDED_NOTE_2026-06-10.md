# Theta P2 K/CPT Determinant-Character Phase Erasure: Bounded Candidate Route

**Current premise authority (2026-07-11):** every Tier-A/admission/registry
reference below is superseded historical context. It supplies no premise and
makes no dependency ready; the scientific conditions remain conditional/open.

**Date:** 2026-06-10 (split from
`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`
so the strong-CP mass-orientation route stands on the theta surface alone,
with no dependency on the `AC_phi_lambda` staggered gate) (2026-06-12: the
determinant-readout bridge named open here is now cited from
`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`
and from the dedicated mass-determinant-channel bridge
`STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md`;
both are wired below as load-bearing dependencies)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit the audit-lane-owned Tier-A registry.
**Primary runner:** [`scripts/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.py`](../scripts/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.py)
**Runner cache:** [`logs/runner-cache/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.txt`](../logs/runner-cache/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.txt)

## Boundary

This note proves one bounded fact:

1. In a supplied determinant-class readout whose scalar readouts are the
   standard continuous multiplicative determinant characters
   `|z|^s exp(i k arg z)`, K/CPT invariance kills the determinant phase
   character: `k = 0`.

It does not discharge the strong-CP mass-orientation premise by itself,
derive the strong-CP action-form premise, or change
`docs/audit/data/premise_decision_history.json`. Those moves require later
registry/audit handling and the determinant-readout bridge cited below, whose
audit status is owned by the independent audit lane.

## Determinant Readout Lemma

The Record axiom supplies durable realized-outcome readout only after a
readout context, finite central-sector decomposition, and fixed K/CPT
conjugation are already supplied. It does not supply the determinant readout
context.

Given such a supplied determinant-class context, the standard multiplicative
determinant character family has phase part

```text
chi_k(z) = exp(i k arg z).
```

K/CPT conjugation sends `z` to `conj(z)`, so `arg z` goes to `-arg z`.
Requiring the character to be invariant under that conjugation gives

```text
exp(i k phi) = exp(-i k phi) for all phi,
```

hence `sin(k phi) = 0` for all `phi`, so `k = 0`. Therefore the invariant
members of this determinant-character family are phase-free functions of
`|det|`.

The hostile guard is important: K/CPT orbit invariance alone gives evenness, not phase erasure.
For example `cos(arg z)` is K-invariant and still depends on the phase. The
phase-erasure conclusion applies only inside the supplied multiplicative
determinant-character class.

## The Determinant-Readout Bridge (cited dependency)

This lemma is a candidate route for the mass-orientation part of the strong-CP
surface, not a completed discharge by itself. To discharge that premise, a
later retained bridge must show that the physical `arg det(M_u M_d)`
contribution used by
[`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) is exhausted by
this determinant-class registrable readout, and that no phase-sensitive
non-multiplicative or action-level datum remains relevant to that premise.
The broad Record-registrability source theorem is cited here as the candidate
bridge:
[`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
(Consequence A there): a Record-registrable scalar readout is finitely
additive over pairwise-disjoint records and constant on `K`/CPT orbits;
additivity forces its per-sector phase functional to be odd, orbit-constancy
forces it to be even, and odd-and-even forces it to vanish identically. Hence
the registrable content of `arg det(M_u M_d)` is exhausted by the phase-free
`k = 0` (modulus) class: phase-sensitive non-multiplicative functionals (for
example `cos(arg z)`, this note's hostile guard) are excluded by additivity,
cross-sector interference data are excluded by additivity, and the
action-level bare-`theta` slot is strong-CP premise 1 — a separate
action-surface premise tracked by the per-plaquette license route, not part of
the mass-orientation premise.

The dedicated mass-determinant-channel specialization is
[`STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md`](STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md):
under a supplied determinant-channel interface with independent-block
determinant multiplication and K/CPT orbit registration, the only registered
continuous determinant phase character is `k = 0`; K-even nonmultiplicative
phase probes such as `cos(arg det)` are outside that determinant-channel block
law.

This wiring does not set `theta_gauge = 0`, does not derive the real-positive
Wilson action surface, and does not eliminate action-level or gauge-theta
residuals.

What remains conditional, exactly as named in the bridge note: the standing
modeling premise that the physical mass-surface readout context satisfies the
Record registrability constraints remains an explicit condition of the
strong-CP selected surface (the bridge removes phase freedom within the
Record-registrable class; it does not prove the physical readout must be in
that class), and the bridge note's audit status is owned by the independent
audit lane and is not asserted here.

## Registry Consequence

The only supported consequence is a candidate route for future Tier-A
registry review: the determinant lemma composed with the determinant-readout
bridges cited above may help remove the positive-real mass-orientation
condition of the strong-CP selected surface only after independent review/audit
accepts the determinant-readout bridge surface being used; registry handling
stays with the audit lane.

No new axiom, primitive, admission, normalization, probability rule,
comparator, or audit verdict is introduced here.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) for the
  narrow Record axiom boundary.
- [`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) for the
  selected-surface strong-CP premise whose mass-orientation part is the
  candidate target here.
- [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
  for the determinant-readout bridge candidate (its Consequence A):
  registrable readouts are additive plus `K`/CPT-orbit-constant, hence
  phase-free, so the multiplicative determinant-character family exhausts the
  registrable `arg det(M_u M_d)` content.
- [`STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md`](STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the dedicated mass-determinant-channel bridge under independent-block
  determinant multiplication and K/CPT orbit registration.

The `AC_phi_lambda` orientation lemma that previously shared a note with
this lemma remains in
`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`
(context, not load-bearing here: this lemma uses nothing from the staggered
gate surface).

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only
status authority.
