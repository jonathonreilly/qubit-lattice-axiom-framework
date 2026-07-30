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

## Scope stress test and partial narrowing

This note ships one positive finite claim and one bounded completeness
statement, the latter only over the 27 indexed deletions. It ships no no-go,
minimum-content result, wall count, wall-independence theorem, axiom-pressure
claim, or unique-selection result. The items not proved by this note are an
unclassified supplied/open inventory, not a certified wall decomposition.
Because a bounded note still requires hostile scope testing, the N1–N8 record
is explicit below.

### N1 — normalized alternative-route inventory

The linked Cycle 719 parent already attempted six materially distinct
constructive families. They are repeated here rather than compressed into
labels. `ATTEMPTED` means proposal evidence was actually run; none is called
retained authority, and “does not close” means only that its stated terminal
residual remains.

| normalized family | honesty marker | exact attempted evidence | terminal residual and Cycle 732 disposition |
|---|---|---|---|
| token-following semantic bank | `ATTEMPTED` | held 2/5/12 intertwiner exact; 178/756 noncanonical-order changes | autonomous edge schedule, literal source finalizer, and 12-bank physical route remain; this route is live, not ruled out |
| fixed finite physical sweep | `ATTEMPTED` | collision-free forward/inverse nearest-neighbor route; 24/576 covariance checks; zero route failures | source finalizer and sweep order remain supplied; this is partial positive evidence, not an impossibility witness |
| source-local finalization | `ATTEMPTED` | all 4,096 source rows and held 2/5/12 cases exact; three finalizer deletions active | genesis and finite outward/inward order remain supplied |
| one-marker local handshake | `ATTEMPTED` | held 2/5/12 cases exact; all 240 rows across 24 candidate enumerations agree | marker-controlled transitions are not physically synthesized and the one-marker sector is supplied |
| two-rail recurrent controller | `ATTEMPTED` | `H=RQ`; held orbits and inverses exact; literal routes and 24/576 coordinate checks pass | source token, source boundary, finite oriented ring, clean work, and program content remain supplied |
| local dirty-sector refusal | `ATTEMPTED` | 34 physical primitives, 60 routed gates, all 16 truth rows exact, six dirty live-token rows refused, and two active deletions | the refusal is not wrapped around every controlled macro and does not prepare its lawful sector |

The direct-X preparation in this note is an additional live counterroute to
word uniqueness, not a failed route: 27 direct X gates prepare the same
selected target. The accepted data-wire-0 mutation and the explicit
two-rail-parity counterexample similarly defeat broader certificate readings.
These live routes are why the note stops at partial narrowing.

### N2 — relationship audit without an independence claim

The raw list is collapsed first: actual current-parent semantics is closed on
the fixed fixture and is not an open item. The remaining inventory has four
explicitly named groups:

- **fixed-fixture genesis specification:** target, word, ordering, `k`, and
  reference pattern;
- **wider logical certificate:** a domain beyond the exact A-count and 27+23
  censuses;
- **physical realization:** placement, transport, admissibility, and
  nearest-neighbor compilation; and
- **uniform/autonomous formation:** a uniform ring/program family or
  autonomous target, word, state, and Record/occurrence formation.

The entries below say what the cited evidence establishes. “Not established”
is deliberately not “no,” and it is not an independence theorem.

| pair | first automatically closes second? | second automatically closes first? | evidence disposition |
|---|---|---|---|
| fixed-fixture specification / wider logical certificate | not established | not established | one supplied fixture does not widen the certificate domain; a wider checker would not by itself select this fixture |
| fixed-fixture specification / physical realization | not established | not established | a logical specification is not a physical compiler; compiling a supplied word would not derive its selection |
| fixed-fixture specification / uniform-autonomous formation | not established | may retire part of the fixed specification; untested | an autonomous formation rule could remove some supplies, so these headings are not certified independent |
| wider logical certificate / physical realization | not established | not established | broader logical coverage and physical realization are uncomposed here |
| wider logical certificate / uniform-autonomous formation | not established | may widen part of the certificate domain; untested | a uniform family might enlarge the checked domain, but no implication theorem is present |
| physical realization / uniform-autonomous formation | not established | may include the fixed physical compiler; untested | a uniform physical construction could subsume the fixed compiler obligation |

No numeric wall count is inferred from this inventory. In particular, possible
downstream retirement in the last three rows prevents any independence
wording.

### N3 — hidden-condition scan

The all-zero source, target bits, layout, oriented program, ring size, `k`,
word ordering, blank registers, logical interpretation, and selected mutation
domain are all exposed as supplies or scope conditions above. Physical meaning
is not imported through logical gate notation. The registered minimal axioms
do not supply a target-selection, program-synthesis, physical-compiler, or
general-error-detection rule.

### N4 — residual matching

Cycle 731 supplies an A-only counter/comparator with a supplied expected
occupancy and an explicit global-parity nonclaim; that matches only the
fixed-fixture A-count use here. Cycle 730 supplies the local active-station
charge guard; it does not supply target selection or total A+B inventory.
Cycle 719 supplies the held logical program and the six attempted families
listed under N1; it does not supply autonomous genesis or a current physical
Cycle 731 compiler. The minimal axioms identify the state-selection boundary;
they do not synthesize this target or word. No cited residual is reused as
evidence for a different obligation.

### N5 — rhetoric resolution

Deletion completeness is per gate for exactly 27 deletions. Flip coverage is
per named wire for exactly 11 A, 11 reference, and one `h` flip. The result is
not per arbitrary data/B/work/auxiliary wire, per insertion/substitution/
reordering mode, per program, per ring, or lattice-wide. The accepted
data-wire-0 flip and parity mismatch remain active countercontrols against any
broader wording.

### N6 — partial-closure paths

The fixed Boolean identity and finite refusal censuses are theorem content.
The selected target, target interpretation, ordering, and `k` are explicit
imports; an import-retirement theorem could later replace them without adding
an axiom. The approved minimal axioms are premises, not missing walls, but they
also do not grant the absent dynamics. Physical compilation, wider certificate
coverage, and family/autonomous formation remain constructive research routes;
this note requests no new axiom or primitive.

### N7 — strongest steelman

A hostile reviewer can prepare the same supplied target with 27 direct X gates
or many other reversible words, so the selected chain cannot prove uniqueness,
optimality, or axiom-driven selection. The Cycle 719 local-Gauss/charge-sector
and dirty-sector-refusal routes also provide concrete mechanisms by which
currently supplied sector data might later be prepared or enforced. The next
terminal test is to compose such a local sector constructor with the actual
current-parent word while preserving acceptance, exact inverse, clean return,
and the existing countercontrols. The present package does not defeat that
steelman and therefore makes no no-go claim.

### N8 — cross-cycle retirement scan

The repo-wide similar-boundary scan summarized in Cycle 719 N6–N8 was checked
against this narrower genesis package:

| prior surface | earlier supplied/open shape | later retirement mechanism | applicability here |
|---|---|---|---|
| Cycle 713 | a bounded physical endpoint instrument with its consumer supplied | Cycle 719 closes the same-site consumer interface | compose a concrete consumer/compiler before declaring the interface absent |
| Cycle 715 | fixed packet address removed, but direction and bounded controller supplied | Cycle 719 obtains direction from matter and replaces the runtime host sweep with recurrent rails | local control can retire a host-supplied program role |
| Cycles 718/612 | reversible spatial ACK existed without the complete recurrent consumer | Cycle 719 supplies the bounded matter-to-packet controller feeding that interface | reuse a proved interface composition rather than infer a substrate obstruction |
| Cycle 656 | host-stepped fixed ROM | Cycle 719 progressively replaces it with a local handshake and two-rail control | a supplied word/order can be retired incrementally by explicit local dynamics |
| Cycles 332/335 | occurrence and protected recurrence closed only on supplied boundary/selection inputs | bounded constructors retire parts of the process while keeping the remaining supplies explicit | selection/Record extensions remain constructive targets, not axiom-pressure evidence |
| Cycle 703 route carried through Cycle 719 N7 | positive local-Gauss constraint capacity with physical encoder/preparation still open | not yet retired; it remains a concrete live composition test | candidate mechanism for reference/sector preparation and local enforcement |

These repeated partial retirements are evidence against any impossibility,
minimum-content, shared-obstruction, sole-wall, or wall-independence reading.
They leave an honest supplied/open inventory and actionable constructive tests.

Disposition: **partial narrowing** to a fixed logical preparation and exact
enumerated current-parent refusal census. Independent audit is still required.
