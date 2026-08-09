# The landed Cycle-719 substrate hosts a minimal inter-site gate — Cycle 970

Date: 2026-08-09

Authority: none

Audit: unset; independent audit still required

Status: bounded support. The landed deterministic basis-state machinery hosts
a one-gate neighbor-dependent distribution on a two-site finite basis menu.
This is not a full covariant admissibility law on the continuous `M_2(C)`
possibility domain.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle970_inter_site_gate_2026_08_09.py`](../scripts/frontier_cycle970_inter_site_gate_2026_08_09.py)
- [`frontier_cycle970_gate_independent_check_2026_08_09.py`](../scripts/frontier_cycle970_gate_independent_check_2026_08_09.py)

Pinned caches:

- [`frontier_cycle970_inter_site_gate_2026_08_09.txt`](../logs/runner-cache/frontier_cycle970_inter_site_gate_2026_08_09.txt)
- [`frontier_cycle970_gate_independent_check_2026_08_09.txt`](../logs/runner-cache/frontier_cycle970_gate_independent_check_2026_08_09.txt)

Receipts:

- [`inter_site_gate_cycle970_receipt_2026_08_09.json`](../outputs/inter_site_gate_cycle970_receipt_2026_08_09.json)
- [`inter_site_gate_independent_check_cycle970_receipt_2026_08_09.json`](../outputs/inter_site_gate_independent_check_cycle970_receipt_2026_08_09.json)

Constitutional effect: none. No axiom, Qualification, primitive, registry,
policy, audit result, or audit status is edited.

## The load-bearing operational definition

Use the labeled nearest-neighbor patch with sites `0=(0,0,0)` and
`1=(1,0,0)`, and the finite basis menu `{0,1}` accepted by the landed
classical basis-state semantics. For landed gate word `W`, target site `t`,
fixed target input `x`, neighbor bit `n`, and target output `y`, define

```text
D[W,t,x](y | n)
  = 1{ applying W to (target t=x, nearest neighbor=n) outputs t=y }.
```

This is a probability distribution: the deterministic point measure induced
by the landed basis-state semantics, consistent with the
[Admissibility axiom memo](MINIMAL_AXIOMS_2026-06-29.md) reading of
deterministic substrates as boundary realizations. The same local input
`x` is held fixed on the `n=0` and `n=1` branches. That clause is
load-bearing. Averaging over `x` asks a different question and can erase a
conditional dependence.

The exhaustive declared family is all words of length zero or one on two
distinct labeled sites from the classical basis gate kinds accepted by the
Cycle-719 core: identity, `X(0)`, `X(1)`, `CNOT(0->1)`, and `CNOT(1->0)`.
`TOF` is excluded by its three-wire arity. Exhaustiveness is claimed only for
this declared family, not for longer words or the full possibility domain.

## A_INDEPENDENCE_MEASUREMENT

Finding verbatim:

```text
PASS A_INDEPENDENCE_MEASUREMENT :: definition=D[W,t,x](y|n)=indicator that landed deterministic basis-state semantics sends target input x and nearest-neighbor bit n to target output y; the same x is held on the n=0 and n=1 branches; state_resolved_changed=4/20 paired comparisons; changed_pair_configurations=8/40; uniform_self_input_changed=0/10
```

Thus four of the 20 site/local-input/word comparisons change, and eight of 40
conditioned configurations belong to separating pairs. The prior “sites do
not talk” result is reproduced exactly under its uniform-self-input
operationalization,

```text
Dbar[W,t](y|n) = (D[W,t,0](y|n) + D[W,t,1](y|n))/2,
```

for which zero of ten site/word comparisons change. The state-resolved and
uniform-marginal censuses answer distinct conditional questions.

The certificate gates only reconciliation: 20 equals four changed plus 16
unchanged; 40 equals two conditioned configurations per comparison; witness
flags equal recomputed inequalities; and both observed counts lie within
their totals. A zero finding would also be certificate-clean.

## B_GATE_CONSTRUCTION

Finding verbatim:

```text
PASS B_GATE_CONSTRUCTION :: verdict=CONSTRUCTED; word=['CNOT(1->0)']; reads_neighbor_bit=1; D(n=0)=[1, 0]; D(n=1)=[0, 1]; transition_n1=[0, 1]->[1, 1]
```

The minimal construction uses a gate already present in the landed core's
`swap_word` macro:

```text
target site:             0
nearest-neighbor site:   1
fixed target input:      x=0
exact gate word:         [CNOT(1->0)]
neighbor bit read:       bit 1
D(y | n=0):              [1,0]
D(y | n=1):              [0,1]
state at n=0:            (0,0) -> (0,0)
state at n=1:            (0,1) -> (1,1)
```

The `n=1` branch actually mutates the target state. No length-zero word
separates the distributions, so one gate is minimal in the declared family.
The certificate compares the success flag to the measured distribution
inequality, the minimality flag to the zero-length ablation, and mutation
flags to explicit before/after states. It would pass a consistently reported
obstruction.

## C_PRICE

Finding verbatim:

```text
PASS C_PRICE :: price=new gate/coupling/axiom/registered primitive 0/0/0/0; supplied premise=fixed target input x=0; changes=unqualified substrate-wide independence is false while uniform marginal remains 0/10; full covariant M_2(C) law remains open
```

Construction costs no new gate class, coupling, axiom, or registered
primitive. It uses landed CNOT and exactly one disclosed boundary premise:
the target begins in the same supplied local state `x=0` on both neighbor
branches.

Against the four axioms:

- Lattice supplies the nearest-neighbor edge; it is unchanged.
- Qubit supplies the site possibility domain; only its finite basis menu is
  tested, so no full-`M_2(C)` statement is made.
- Admissibility receives one bounded variation witness, not a fixed
  translation- and proper-cubic-covariant law for every site and condition.
- Record is unused; no formation, locking, permanence, or readout claim is
  made.

Against the three registered primitives, the delta is zero for each:
`scale_reference_primitive` and `kinetic_isotropy_primitive` are unused;
`realized_state_primitive` is neither added nor changed, and the two supplied
basis states remain test inputs rather than a derived state-selection law.

What changes is narrow. An unqualified substrate-wide neighbor-independence
claim is false. The `0/10` uniform-self-input independence finding remains
true and is scoped to its averaging prescription. No Cycle-719 controller
certificate is contradicted because CNOT was already landed machinery.

Promoting this bounded witness to the whole axiom remains open: it would
require a fixed translation- and proper-cubic-covariant rule for every site
and nearest-neighbor condition, with measures on the full `M_2(C)` possibility
domain. This cycle does not supply formation site, rate, realized draw, or
record dynamics.

## D_CONTROLS

Finding verbatim:

```text
PASS D_CONTROLS :: sha_pins={"docs/MINIMAL_AXIOMS_2026-06-29.md":"53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39","scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":"0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4"}; BLOCKLIST=['docs/MINIMAL_AXIOMS_2026-06-29.md'] text_only=True; determinism_replay=True; runtime_s=0.000617<1400; stdout_upper_bound_bytes=2667<6000<150000; timeout_s=300<1400
```

Both runners use literal, existing, worktree-relative `AUDIT_INPUT_PATHS`.
The primary SHA-pins and executes only the Cycle-719 substrate while treating
the axiom memo as blocklisted text. The checker blocklists every cited input,
imports neither primary nor core, verifies the landed SWAP/CNOT word from AST,
and recomputes both censuses with an independent XOR interpreter. Both replay
deterministically, declare a 300-second timeout, and stay below the stricter
6 KB house stdout ceiling as well as the requested 150 KB ceiling. Both
caches were written through
`runner_cache.execute_and_write_cache(path, timeout_sec)`.

## Independent refutation outcome

The checker reported:

```text
PASS R0_PINS_BLOCKLIST_AND_LANDED_GATE_AST :: pins_match=4/4; BLOCKLIST_text_AST_only=['scripts/frontier_cycle970_inter_site_gate_2026_08_09.py', 'logs/runner-cache/frontier_cycle970_inter_site_gate_2026_08_09.txt', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py']; blocked_modules_loaded=False; swap_word_cnot_order=[('left', 'right'), ('right', 'left'), ('left', 'right')]
PASS R1_REFUTE_STATE_RESOLVED_CENSUS :: independent_state_resolved_changed=4/20; primary=4/20
PASS R2_REFUTE_UNIFORM_CENSUS :: independent_uniform_self_input_changed=0/10; primary=0/10
PASS R3_REFUTE_GATE_CONSTRUCTION :: independent_verdict=CONSTRUCTED; word=CNOT(1->0); D0=[1, 0]; D1=[0, 1]; transition_n1=[0, 1]->[1, 1]
PASS R4_REFUTE_PRICE_AND_SCOPE :: price_route=successful_landed_construction; delta_gate/coupling/axiom/primitive=[0, 0, 0, 0]; uniform independence scoped, not deleted
PASS R5_CONTROLS :: determinism_replay=True; runtime_s=0.003955<1400; stdout_upper_bound_bytes=2738<6000<150000; timeout_s=300<1400; literal_inputs=['scripts/frontier_cycle970_inter_site_gate_2026_08_09.py', 'logs/runner-cache/frontier_cycle970_inter_site_gate_2026_08_09.txt', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py']
VERDICT: PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT
TOTAL: PASS=6 FAIL=0
```

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "does the landed Cycle-719 controller substrate host any site-local distribution that varies with a nearest-neighbor condition?"
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "independent audit the fixed-local-input operational definition; do not promote this two-site basis-menu witness into a full covariant M_2(C) admissibility law"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "exact on the declared two-site basis-menu family under the fixed-local-input operationalization"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "bounded finite-menu witness only; the full covariant M_2(C) law is not constructed"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Verdict

The landed substrate can host an inter-site gate witness. The one-CNOT word
turns neighbor bit `1` into target possibility `1` while neighbor bit `0`
leaves target possibility `0`, so the conditional point distributions differ.
The prior zero result survives exactly as the uniform-self-input marginal and
cannot be generalized beyond that definition. This settles the bounded
hosting question but does not construct the full Admissibility law.
