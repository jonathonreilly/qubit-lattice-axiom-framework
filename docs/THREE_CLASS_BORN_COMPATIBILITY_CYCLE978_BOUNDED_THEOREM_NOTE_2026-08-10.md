# Fixed-input compatibility with three displayed neighbour-law representatives — Cycle 978

Date: 2026-08-10

Authority: none

Audit: unset; independent audit remains required

Claim type: bounded_theorem

Actual current surface: bounded support. On the reconstructed finite event
space and the exhaustive word-length-at-most-one basis-state gate family
inside a target-centred radius-one star, all five finite event weightings
admit a separate Cycle-974 product extension with each of three displayed
representative truth tables, but none admits one unindexed fixed-`x` kernel
equal to all three representatives pointwise. This does not establish a
class-level stochastic law, construct the axiom-level nearest-neighbour
probability law, cover the full continuous `M_2(C)` possibility domain, or
derive a Born weighting.

Primary runner:

- [`frontier_cycle978_three_class_born_compatibility_2026_08_10.py`](../scripts/frontier_cycle978_three_class_born_compatibility_2026_08_10.py)

Independent refutation checker:

- [`frontier_cycle978_three_class_born_independent_check_2026_08_10.py`](../scripts/frontier_cycle978_three_class_born_independent_check_2026_08_10.py)

Pinned caches:

- [`frontier_cycle978_three_class_born_compatibility_2026_08_10.txt`](../logs/runner-cache/frontier_cycle978_three_class_born_compatibility_2026_08_10.txt)
- [`frontier_cycle978_three_class_born_independent_check_2026_08_10.txt`](../logs/runner-cache/frontier_cycle978_three_class_born_independent_check_2026_08_10.txt)

Receipts and provenance:

- [`three_class_born_compatibility_cycle978_receipt_2026_08_10.json`](../outputs/three_class_born_compatibility_cycle978_receipt_2026_08_10.json)
- [`three_class_born_compatibility_cycle978_independent_check_receipt_2026_08_10.json`](../outputs/three_class_born_compatibility_cycle978_independent_check_receipt_2026_08_10.json)
- [`cycle978_cited_primary_provenance_2026_08_10.json`](../outputs/cycle978_cited_primary_provenance_2026_08_10.json)

Constitutional effect: none. No axiom, primitive, audit result, registry,
policy, or effective-status surface is edited.

## A_REBUILD — independent reconstruction

The primary uses the landed
[`Cycle-719 semantic substrate`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py)
to reconstruct the finite record-write event census. The cited Cycle-878,
Cycle-974, and Cycle-977 note/runner pairs are cached at declared commit/blob
pins, checked as note text and runner AST, and never imported or executed.
They provide provenance and falsifiable scope declarations, not verdicts.

The reconstruction gives 92,260 event atoms in 748 worlds, with 164 formed
worlds. The five weightings are:

| weighting | reconstructed definition | positive events | zero events |
|---|---|---:|---:|
| `M1_COUNTING` | `w(e)=1` | 92,260 | 0 |
| `M2_PER_WORLD_UNIFORM` | world score `a(w)=1`, uniform within each event-bearing world | 92,260 | 0 |
| `M3_OCCUPATION_WEIGHTED` | `a(w)=` clean-dwell occupation count, uniform within world | 19,172 | 73,088 |
| `M4_FORMATION_LIFETIME` | `a(w)=boundaries-formation_moment(w)+1` if formed, otherwise zero, uniform within world | 19,172 | 73,088 |
| `M5_FORMATION_MOMENT` | `a(w)=formation_moment(w)` if formed, otherwise zero, uniform within world | 16,076 | 76,184 |

Every vector is nonnegative and has positive total mass. Normalization
therefore defines a finite event probability `p_i(e)` for each row.

Independently, the primary enumerates every distinct word of length zero or
one over the landed `X`, `CNOT`, and `TOF` constructors, with distinct
operands supported anywhere in the seven-site star:

```text
1 identity + 7 X + 42 ordered CNOT + 105 TOF = 155 words.
```

Both target bits and all 64 neighbour conditions are evaluated, for 19,840
conditioned configurations. Exactly 21 words depend on a neighbour, in three
classes:

| class | representative law | exact witnesses |
|---|---|---|
| CNOT (6) | `y=x XOR n_(+x)` | `CNOT(+x->C)`, `CNOT(-x->C)`, `CNOT(+y->C)`, `CNOT(-y->C)`, `CNOT(+z->C)`, `CNOT(-z->C)` |
| perpendicular-control TOF (12) | `y=x XOR (n_(+x) AND n_(+y))` | `TOF(+x,+y->C)`, `TOF(+x,-y->C)`, `TOF(+x,+z->C)`, `TOF(+x,-z->C)`, `TOF(-x,+y->C)`, `TOF(-x,-y->C)`, `TOF(-x,+z->C)`, `TOF(-x,-z->C)`, `TOF(+y,+z->C)`, `TOF(+y,-z->C)`, `TOF(-y,+z->C)`, `TOF(-y,-z->C)` |
| opposite-control TOF (3) | `y=x XOR (n_(+x) AND n_(-x))` | `TOF(+x,-x->C)`, `TOF(+y,-y->C)`, `TOF(+z,-z->C)` |

The complete family has zero failures in 476,160 proper-rotation semantic
comparisons, 119,040 unit-translation semantic comparisons, and 19,840
landed-core/coordinate bridge comparisons.

## Proof obligation graph

**Exact bounded theorem.** Given the reconstructed finite event vectors, the
declared 155-word basis-state family, uniform full-support
`q(x,n)=1/128`, the three displayed deterministic representatives, and
pointwise equality at fixed `x`, each of the five event weightings admits all
three separate product extensions, while no one unindexed conditional kernel
`K_i(y|x,n)` equals all three representatives.

| obligation | depends on | disposition | evidence |
|---|---|---|---|
| L1 event-vector validity | Cycle-719 finite event rebuild; finite caps | discharged | 92,260 atoms; every numerator nonnegative with positive total |
| L2 155-word/21-witness/3-orbit reconstruction | seven-site star; word length at most one; basis-state semantics | discharged | exhaustive counts and zero covariance/bridge failures in A_REBUILD |
| L3 per-class product marginal identity | L1; uniform full-support `q`; one displayed `L_c` at a time | discharged | exact rational sums reproduce every `p_i(e)` |
| L4 fixed-`x` representative disagreement | L2; displayed CNOT and TOF representatives | discharged | `x=0`, `n=(1,0,0,0,0,0)` gives outputs 1 and 0 |
| L5 no common pointwise `K_i(y|x,n)` | L3; L4; unindexed kernel; pointwise equality | discharged | incompatible delta distributions, independently of `p_i` |
| M1 representative/class-to-axiom bridge | class aggregation; eliminate or interpret `x`; local-to-event lift | **open** | not supplied by this cycle |

The hypotheses are preserved literally: finite caps and horizons, basis-state
words only, the displayed representatives, uniform full-support `q`, fixed
`x`, and pointwise equality. Covered cases are all five weightings (including
their zero-weight events), both target inputs, all 64 neighbour conditions,
all 155 words, and all 21 neighbour-sensitive witnesses. Degenerate identity,
single-`X`, non-target gates, and non-neighbour-sensitive words are included
in the exhaustive family and correctly contribute no witness. The strongest
missing lemma is M1: a justified bridge from representative fixed-`x` kernels
to an axiom-level covariant `K(y|n)`, including class aggregation and the
local-to-event/Born lift.

## B_PER_CLASS_TEST — criterion and 5x3 result

For each class separately, the test uses Cycle 974's product-form criterion
verbatim, with the old single XOR kernel instantiated by the reconstructed
representative kernel `L_c`:

```text
P_i(e,x,n,y) = p_i(e) q(x,n) 1{y=L_c(x,n)},   q(x,n)=1/128.
```

A weighting is excluded only if its weights fail nonnegativity or
normalization, the product fails to reproduce event marginal `p_i`, or an
exact `(witness,x,n,y)` configuration disagrees with the reconstructed
class kernel. Every exclusion must carry the first such witness and
configuration.

| weighting | CNOT | perpendicular-control TOF | opposite-control TOF |
|---|---|---|---|
| `M1_COUNTING` | SURVIVES | SURVIVES | SURVIVES |
| `M2_PER_WORLD_UNIFORM` | SURVIVES | SURVIVES | SURVIVES |
| `M3_OCCUPATION_WEIGHTED` | SURVIVES | SURVIVES | SURVIVES |
| `M4_FORMATION_LIFETIME` | SURVIVES | SURVIVES | SURVIVES |
| `M5_FORMATION_MOMENT` | SURVIVES | SURVIVES | SURVIVES |

Per-class exclusions: none. Therefore there are no disagreeing witnesses to
report.

This is Cycle 974's fixed-input product-extension test, not a derivation of
the full Admissibility probability law. In particular, `x` is auxiliary to
the nearest-neighbour condition `n`; marginalizing the uniform carrier over
`x` makes each displayed XOR-family output marginal uniform. Thus per-class
survival does not by itself establish the axiom's required variation with
nearest-neighbour conditions.

## C_JOINT_TEST — fixed-input common-kernel surrogate

The full-family test keeps one unindexed fixed-input conditional kernel. The
same `K_i(y|x,n)` in one Cycle-974 product extension must equal every
displayed representative kernel pointwise:

```text
P_i(e,x,n,y) = p_i(e) q(x,n) K_i(y|x,n),
K_i(y|x,n) = L_c(y|x,n) for every class c.
```

No class label or carrier is added: gate-word class is not a
nearest-neighbour condition supplied to the substrate rule. Nonnegative event
weights and the event marginal therefore remain necessary but cannot repair
a pointwise disagreement between class kernels.

The first exact disagreement is common to all five weightings:

```text
x=0
n=(+x,-x,+y,-y,+z,-z)=(1,0,0,0,0,0)
CNOT(+x->C):       y=1, distribution [0,1]
TOF(+x,+y->C):    y=0, distribution [1,0]
```

Joint survivors: none. Joint-only exclusions are `M1_COUNTING`,
`M2_PER_WORLD_UNIFORM`, `M3_OCCUPATION_WEIGHTED`,
`M4_FORMATION_LIFETIME`, and `M5_FORMATION_MOMENT`. Each has the exact
disagreeing witness pair and configuration above. The opposite-control
representative `TOF(+x,-x->C)` also gives `y=0` on that configuration, so it
disagrees with the CNOT representative there as well.

This is not an axiom-level class contradiction. Eliminating the auxiliary
target input with the declared `q(x|n)=1/2` gives

```text
K_c(y|n) = sum_x q(x|n) 1{y=x XOR f_c(n)} = [1/2,1/2]
```

for every class and every neighbour condition. The marginalized class
kernels therefore agree, but they do not vary with `n` as Admissibility
requires. The exact joint result is only that the three displayed
deterministic representative truth tables have no common `K(y|x,n)` on the
fixed-input surrogate. It neither proves nor refutes existence of a different
full nearest-neighbour probability law.

## D_ARTIFACT_VERDICT

```text
NULL_WAS_FAMILY_ARTIFACT
survivors/5: 0/5
```

Cycle 974's five-survivor null does not survive the fixed-input common-kernel
test on the enlarged family. The two additional TOF representative truth
tables conflict pointwise with the CNOT representative, so all five
weightings that survive every separate class test are excluded jointly on
that surrogate. This does not select a Born weighting: zero survivors rejects
simultaneous deterministic representative-kernel compatibility rather than
deriving an axiom-level probability law, event-marginal selector, occurrence
rule, or Born rule.

The mandated label `NULL_WAS_FAMILY_ARTIFACT` is bookkeeping for the task's
fixed-input surrogate comparison. It is not a causal claim that enlarging the
gate family alone changed the result: both the family and the joint
common-kernel obligation are stronger than Cycle 974's one-representative
test.

## No-Go Discipline Gate

The negative surface governed here is only L5: no common pointwise fixed-`x`
kernel for the three displayed deterministic representatives. It is not a
`no_go` classification for Admissibility or the Born problem.

**N1 — alternative routes.** Five materially different attacks were made:

1. `ATTEMPTED` — change the event weighting. All five reconstructed `p_i`
   were substituted; the representative delta-distribution mismatch is
   independent of the positive event factor ([primary receipt](../outputs/three_class_born_compatibility_cycle978_receipt_2026_08_10.json)).
2. `ATTEMPTED` — choose another witness in the same orbit. Exhausting all 21
   neighbour-dependent words and their proper rotations still contains a
   rotated CNOT/TOF disagreement ([primary cache](../logs/runner-cache/frontier_cycle978_three_class_born_compatibility_2026_08_10.txt)).
3. `ATTEMPTED` — carry a class label and use `K_c`. This constructs three
   context-labelled laws, not the theorem's one unindexed kernel; the rejected
   formulation and narrowing are recorded below under Review record.
4. `ATTEMPTED` — marginalize the auxiliary `x`. The analytic sum gives the
   same `[1/2,1/2]` kernel for all three representatives, but changes the
   fixed-`x` pointwise object and therefore does not refute L5; it instead
   keeps M1 open (C_JOINT_TEST above).
5. `ATTEMPTED` — allow a stochastic common `K` at fixed `x`. Exact equality
   to deterministic representatives requires both incompatible delta masses
   on the displayed disagreement input, so stochastic notation cannot satisfy
   the pointwise-equality hypothesis ([independent checker receipt](../outputs/three_class_born_compatibility_cycle978_independent_check_receipt_2026_08_10.json)).

**N2 — wall independence.** These are promotion walls beyond L5, not
additional premises of the narrow theorem: W1 replaces the fixed-`x`
surrogate by an axiom-level `K(y|n)`; W2 supplies representative-to-class
aggregation/covariance; W3 supplies the local-event-to-substrate/Born lift.
The collapsed pairwise audit is:

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| W1, W2 | no | no | yes |
| W1, W3 | no | no | yes |
| W2, W3 | no | no | yes |

Finite caps, the displayed representatives, and uniform `q` are theorem
hypotheses rather than separately counted promotion walls. Eliminating `x`
is part of W1, so it is not double-counted.

**N3 — hidden-wall scan.** The prescribed phrase scan found no load-bearing
use of “we assume”, “as is standard”, “the framework provides”, “naturally”,
“obviously”, “standard QFT”, “registered”, or “canonical”. Occurrences of
“declared” and construction language name the explicit finite hypotheses
listed in the proof graph; none silently supplies M1. The full continuous
domain, class aggregation, and local-to-event lift are explicit open items.

**N4 — residual matching.** Prior-cycle material is provenance, not an
imported verdict:

| cited artifact | residual it resolves | residual used here | exact match? |
|---|---|---|---|
| Cycle 878 weighting reconstruction (`docs/EVENT_SPACE_GROUNDWORK_CYCLE878_SUPPORT_NOTE_2026-07-28.md:50-64`) | five finite event-vector definitions | L1 definitions only | yes for L1; no support for L5 |
| Cycle 974 compatibility test (`679afcde3234:docs/COVARIANT_LAW_WEIGHT_COMPATIBILITY_CYCLE974_THEOREM_NOTE_2026-08-10.md:107-110,191-194`) | one displayed XOR product extension, separately | three-representative unindexed fixed-`x` L5 | no; provenance/comparator only |
| Cycle 977 family reconstruction (`27ec7c243f61:docs/WITNESS_FAMILY_COMPLETENESS_CYCLE977_BOUNDED_THEOREM_NOTE_2026-08-10.md:61-75,89-113,124-137`) | 155 words, 21 witnesses, three covariant orbits | L2 reconstruction | yes for L2; no support for L5 |
| Cycle 719 executable core (`scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py:80-87,90-133,209-223`) | finite event/controller aliases, program construction, gate semantics, and orbit execution | L1 event data and L2 landed semantic bridge | yes for L1/L2; no support for L5 |

The provenance bundle authenticates the exact bytes for the non-main Cycle
974 and Cycle 977 commit/path citations. No nonmatching predecessor verdict is
counted toward the L5 proof; L5 is derived by the primary and independent
checker from the displayed truth tables.

**N5 — rhetoric resolutions.** The landing primary cache contains substantive
`per_element:`, `per_site:`, `per_mode:`, `per_block:`, and `lattice_wide:`
execution lines. Event rows, the target-centred star, and the three displayed
blocks are checked. Continuous modes and a lattice-wide axiom law are
explicitly marked “checked and not executed”; all negative language is
therefore narrowed to the finite fixed-input representative kernel.

**N6 — partial-closure paths.** No claim that a new axiom is required is made.
Marginalizing `x` is an executed reframe that removes the class disagreement
but yields a constant neighbour-conditioned marginal. A nonuniform
`q(x|n)`, a justified stochastic class aggregation, and a local-to-event lift
remain mathematically actionable M1 routes. Existing minimal-axiom language
sets the target boundary but does not silently discharge them.

**N7 — steelman.** A hostile reviewer should reject any axiom-level no-go:
the fixed-`x` input is not itself the nearest-neighbour condition named by
Admissibility, and summing the stipulated uniform `x` makes all three class
marginals identical. A nonuniform `q(x|n)` or a covariant stochastic
aggregation could then restore neighbour variation, provided it is connected
to event probabilities by an explicit lift. That is a concrete unclosed
mechanism with terminal obligation M1. It defeats the broader rhetoric and is
why this note ships only L5; it does not defeat L5 because it changes the
kernel's conditioning and equality obligation.

**N8 — cross-cycle echo.** Cycle 974 itself is the relevant warning: a null on
a declared 20-word family did not test the three-orbit reconstruction later
established by Cycle 977. This cycle therefore preserves exhaustive family
scope and refuses to echo L5 as a full-law result. Repository scans for
“structurally undecidable”, “no retained primitive”, “requires new axiom”,
and “cannot be derived from A_min” yielded no prior residual used as proof of
L5. The same retirement mechanism—narrow the object and expose the missing
bridge—is applied here.

N1–N8 disposition: **PASS for the narrow L5 theorem only**. The convincing
N7 steelman makes any broader Admissibility/Born negative premature and that
broader claim is not shipped.

## E_CONTROLS and independent refutation

The primary declares exactly three worktree-relative `AUDIT_INPUT_PATHS`: the
pinned text/AST provenance bundle, the
[`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md), and the landed Cycle-719
semantic core. All have SHA-256 and git-blob pins. Cited predecessor runners
are blocklisted and never loaded. The deterministic short event replay and
independent family replay agree with the full calculation.

The primary completed in 52.975 seconds with 4,402 stdout bytes:

```text
A_REBUILD PASS
B_PER_CLASS_TEST PASS
C_JOINT_TEST PASS
D_ARTIFACT_VERDICT PASS
E_CONTROLS PASS
TOTAL: PASS=5 FAIL=0
```

The independent checker reads three worktree-relative files, parses the
primary as AST without importing it, and reconstructs the 155-word Boolean
family, 21 witnesses, three classes, and proper-rotation covariance without
Cycle-719. It derives the product-extension verdict algebraically, binds the
primary by a stable source SHA-256 pin, records the dynamic receipt/cache
hashes, semantically binds their source hash, PASS line, table, and headline,
and rejects eight active corruptions:
family size, witness count, class membership, a per-class verdict, joint
survivors, joint disagreeing witness, artifact label, and Born-wall status.

It completed in 0.871 seconds with 1,596 stdout bytes:

```text
R0_PRIMARY_AST_AND_PINS PASS
R1_INDEPENDENT_FAMILY_AND_CLASSES PASS
R2_REFUTE_PER_CLASS_AND_JOINT PASS
R3_RECEIPT_CACHE_BINDING PASS
R4_ACTIVE_CORRUPTION_PROBES PASS
R5_CONTROLS PASS
TOTAL: PASS=6 FAIL=0
```

The certificate gates construction, exhaustive reconciliation, partition
bookkeeping, binding, corruption sensitivity, determinism, and resource
controls. The primary's integrity gates remain outcome-neutral; the
independent checker separately derives and mutation-checks the survivor count,
disagreement, artifact label, and Born-wall line.

## Imports, support, derived, open

- **Executable import:** Cycle 719 supplies the finite event/controller
  substrate used to rebuild the five vectors and the landed gate constructors,
  Boolean semantics, and orbit machinery used for the 155-word bridge.
- **Boundary premise:** `MINIMAL_AXIOMS_2026-06-29.md` supplies the statement
  that the desired distribution is determined by nearest-neighbour conditions;
  it does not supply `K`, `q`, or a lift.
- **Explicit stipulations:** finite caps and horizon, the seven-site star,
  word length at most one, basis-state gates, `q(x,n)=1/128`, fixed `x`, the
  three displayed representatives, and the Cycle-974 product surrogate.
- **Provenance-only support:** Cycle 878 names the five weighting definitions;
  Cycle 974 names the comparator product test; Cycle 977 names the enlarged
  family/class census. Their verdicts are neither imported nor executed.
- **Derived here:** event-vector validity, the 155/21/3 reconstruction,
  separate 5x3 product identities, the exact fixed-input disagreement, and
  the absence of a common pointwise representative kernel.
- **Open:** an axiom-level `K(y|n)`, representative-to-class aggregation and
  covariance, elimination or interpretation of `x`, the full `M_2(C)`
  domain, and a local-to-event/Born lift.

## Review record

Adversarial review rejected an earlier class-indexed carrier because it tested
three labelled laws rather than one rule. The claim was narrowed to the exact
fixed-input representative theorem, and the uniform-`x` marginal counterroute
was made explicit. Raw self-written caches were replaced by authenticated
runner-cache envelopes; receipt/cache hash binding is semantic and only the
stable primary source is hard-pinned.

Restricted-packet co-landing is mandatory. The literal helper mapping is:

```text
"three_class_born_compatibility_cycle978_bounded_theorem_note_2026-08-10": ["scripts/frontier_cycle978_three_class_born_independent_check_2026_08_10.py"]
```

The note, primary, checker, both enveloped caches, both receipts, provenance
bundle, helper mapping, and regenerated citation-graph manifest are hard
co-landing conditions. The generated audit row must expose the checker under
`helper_runner_paths` and its source under `changed_surfaces`; no audit status
or effective-status surface lands in this PR.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "under Cycle 974's fixed-input product-extension surrogate, did its five-survivor null persist only because the 20-word family omitted two induced-law classes?"
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "submit this bounded theorem to independent audit; do not promote it to a full continuous M_2(C) probability law"
```

## Claim boundary

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "finite exact theorem on five event vectors and three displayed fixed-input representative truth tables, with the axiom-level class/lift bridge explicitly open"
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "exact on the reconstructed finite event space, declared 155-word one-step basis-state family, and Cycle-974 fixed-input product-extension surrogate"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "fixed-input surrogate and finite one-step basis-state horizon; no axiom-level nearest-neighbour distribution, full continuous M_2(C) probability law, or Born selector"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/frontier_cycle978_three_class_born_independent_check_2026_08_10.py
```
