# Fixed logical genesis word and enumerated refusal census — Cycle 732

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem candidate

Claim type: bounded_theorem

Runners:

- [`frontier_cycle732_genesis_word_self_verification_2026_07_28.py`](../scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py)
- [`frontier_cycle732_genesis_independent_check_2026_07_28.py`](../scripts/frontier_cycle732_genesis_independent_check_2026_07_28.py)

Load-bearing proposal-only parents and boundary authorities:

- [Cycle 731 A-rail occupancy counter/comparator](TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md)
- [Cycle 730 local charge-row guard](CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md)
- [Cycle 719 recurrent controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
- [Minimal axioms and their explicit state-selection boundary](MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, audit result, or audit status.
The parents above are support-only proposal surfaces, not retained authority.

## Result up front

For one exact supplied ring-11 logical layout, program, target, and expected
A-rail occupancy `k = 1`, a supplied 27-gate chain (one X followed by 26
CNOTs) has the following finite properties:

- it maps the all-zero logical register to the selected 27-one target,
  register by register, and its literal reverse maps the target back to zero;
- the actual current Cycle 731 held word has 11,206 logical gates and accepts
  that target over the 11-step orbit with clean controller return;
- the concatenated 123,293-gate logical word has SHA-256
  `23ad4b292a23095afdffd7337059a4276cf87d2c00a0670f63c4a1269e02194d`,
  produces the expected data transition, returns the controller registers,
  and reverses exactly;
- deleting each genesis gate once gives 27 distinct non-target outputs, with
  Hamming weights 0 through 26, and the current Cycle 731 word refuses all 27;
- flipping each of exactly 11 A wires, 11 reference wires, and the one `h`
  wire gives 23 selected output mutations, and the current Cycle 731 word
  refuses all 23.

The primary and independent runners both execute these claims against the
current parent. The independent runner does not import the Cycle 732 primary;
it rebuilds the genesis chain and uses a separate X/CNOT/TOF integer
evaluator. Both runners declare the full recursive mutable-input closure and
include the paired runner in the other's freshness boundary.

This is a logical fixed-fixture theorem candidate. It is not a physical
transport or nearest-neighbor compilation result.

## Supplied, derived, and excluded

### Supplied conventions and boundary conditions

- ring size 11, two-bank data fixture, oriented program, and logical layout;
- the selected target: 20 data ones, A at station 0, five reference ones,
  `h = 1`, and blank B/work/auxiliary registers;
- the current parent comparator input `k = 1`;
- the 27-gate ordering itself.

The word was synthesized from the selected target. Its exactness therefore
does not derive the target, the one-A interpretation, `k`, or a unique
preparation rule. A different reversible word, including 27 direct X gates,
could prepare the same selected target.

### Derived on the exact supplied fixture

- blank-to-target bit equality and exact literal reverse;
- actual-current-parent target acceptance and clean return;
- the exact 27-deletion census;
- the exact 23 selected A/reference/`h`-flip census;
- the pinned logical gate counts and word digests printed by the runners.

### Not claimed

- total A+B inventory or a global parity behavioral equivalence;
- preparation of the reference pattern or selection of `k`;
- physical placement, transport, admissibility, or nearest-neighbor routing;
- detection of arbitrary preparation errors;
- autonomous state/word selection from Record or occurrence structure;
- a uniform construction for other rings or programs;
- any audit grade or retained status.

A data-wire-0 flip is an explicit countercontrol: the current parent accepts
it with no transient refusal and clean controller return. The 27+23 mutation
result must not be read as a general error-detection theorem. Data, B, work,
and auxiliary flips, plus insertions, substitutions, and reorderings, are
outside the enumerated domain.

The current Cycle 731 global-parity counterexample is also rerun: A occupancy
matches `k = 1`, total two-rail parity does not match `h`, and the actual word
still changes data with clean return. Cycle 732 therefore inherits the
parent's explicit nonclaim, not the superseded parity model.

## No-go discipline and partial narrowing

This note makes a positive finite claim and a bounded completeness statement
only about the 27 indexed deletions. It makes no general impossibility or
unique-selection claim. Because the file names explicit open boundaries, the
following N1–N8 controls are recorded.

1. **N1 — alternative routes.** The selected chain is tested; 27 direct X
   gates are a concrete alternative preparation; actual current-parent
   verification is tested; autonomous target/`k` selection, current physical
   compilation, a general error wrapper, and a uniform family remain separate
   open routes.
2. **N2 — wall independence.** Word/target selection, supplied `k`,
   current-parent semantics, physical compilation, general error coverage,
   and family/Record formation do not imply one another. No one of them is
   presented as the sole remaining wall.
3. **N3 — hidden-wall scan.** Target bits, layout, program, `k`, ordering, and
   logical interpretation are listed above as supplies. Physical meaning is
   not smuggled in through logical gate notation.
4. **N4 — residual matching.** The current Cycle 731 residual is A-only
   counting with supplied expected occupancy and an explicit global-parity
   nonclaim. Cycle 730 supplies a local active-station charge guard, and Cycle
   719 supplies the held logical program. None supplies autonomous genesis
   selection or a current physical Cycle 731 compilation.
5. **N5 — rhetoric granularity.** Resolution is per gate for 27 deletions and
   per named wire for 23 selected flips only. Other mutation modes and all
   family-wide language are excluded.
6. **N6 — partial closure.** The fixed Boolean identity and finite refusal
   censuses remain theorem content. Target interpretation, selection, and
   `k` remain convention/meta inputs; physical and family extensions remain
   separate work.
7. **N7 — strongest steelman.** Many reversible words prepare the same
   supplied target, so this chain cannot establish uniqueness or axiom-driven
   selection. The claim accepts that counterroute and retains only the exact
   behavior of this selected word.
8. **N8 — cross-cycle echo.** The expected-occupancy, total-rail, parity,
   reference-preparation, family, and physical-transport boundaries recorded
   by current Cycle 731 remain open here.

Disposition: **partial narrowing** to a fixed logical preparation and exact
enumerated current-parent refusal census. Independent audit is still required.
