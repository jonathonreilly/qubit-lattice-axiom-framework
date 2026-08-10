# The general target-input law for the bounded inter-site gate

Date: 2026-08-10

Authority: none

Audit: unset; independent audit still required

Status: proposed_retained

Boundary: On the declared radius-one, word-length-at-most-one
basis-state family, the target-input simplex has the exact marginal
neighbour-dependence law `TV=|2p-1|`. The unique marginal-invisible input is
the uniform law `p=1/2`, even though both fixed-input rows remain
state-resolved witnesses. This is not a probability law on the full
continuous `M_2(C)` possibility domain and does not fulfill the complete
Admissibility axiom.

Claim type: bounded_theorem

target_claim_type: bounded_theorem

claim_type_reason: exact finite theorem on a declared radius-one,
word-length-at-most-one basis-state family

packet_helper_runner: scripts/frontier_cycle975_input_distribution_independent_check_2026_08_10.py

Primary runner:

- [`frontier_cycle975_input_distribution_dependence_law_2026_08_10.py`](../scripts/frontier_cycle975_input_distribution_dependence_law_2026_08_10.py)

Independent refutation checker:

- [`frontier_cycle975_input_distribution_independent_check_2026_08_10.py`](../scripts/frontier_cycle975_input_distribution_independent_check_2026_08_10.py)

Pinned caches:

- [`frontier_cycle975_input_distribution_dependence_law_2026_08_10.txt`](../logs/runner-cache/frontier_cycle975_input_distribution_dependence_law_2026_08_10.txt)
- [`frontier_cycle975_input_distribution_independent_check_2026_08_10.txt`](../logs/runner-cache/frontier_cycle975_input_distribution_independent_check_2026_08_10.txt)

Receipts:

- [`input_distribution_dependence_law_cycle975_receipt_2026_08_10.json`](../outputs/input_distribution_dependence_law_cycle975_receipt_2026_08_10.json)
- [`input_distribution_dependence_law_cycle975_independent_check_receipt_2026_08_10.json`](../outputs/input_distribution_dependence_law_cycle975_independent_check_receipt_2026_08_10.json)

Constitutional effect: none. No axiom, primitive, registry, policy, audit
result, or effective-status surface is edited.

## Exact gate family, input family, and caps

Fix a target `a` in `Z^3` and its six neighbours `a+d`, where

```text
d in {+e_x,-e_x,+e_y,-e_y,+e_z,-e_z}.
```

The spatial horizon is the seven-site target-centred star. The word-length
cap is one. The gate menu is exactly the identity, `X`, and oriented `CNOT`
as executed by the landed
[`Cycle-719 core`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py).
The distinct word family is

```text
1 identity + 7 X + 12 oriented centre-neighbour CNOT = 20 words.
```

Every target and neighbour coordinate has the basis menu `{0,1}`, and every
one of the `2^6=64` neighbour conditions is enumerated. `TOF` is excluded by
the two-site gate-kind/arity condition. Words of length at least two and
probability measures on the continuous `M_2(C)` domain are outside the cap.

The full target-input family in this note is the entire probability simplex
on the finite target basis:

```text
F = {mu_p = p delta_0 + (1-p) delta_1 : p is real and 0 <= p <= 1}.
```

This parameterization is unique because `p=mu_p({0})`. The same `mu_p` is
held on the two compared `n_d` branches and across spectator contexts. A law
chosen conditionally on `n_d` is excluded because it would insert the tested
neighbour dependence into the input rather than measure the gate's response.
The uncountable family is enumerated exactly by the five algebraically
distinct cells below; the formulas apply pointwise to every member, not just
to the displayed representative values.

## A_INPUT_FAMILY

For each fixed input `x`, an incoming word `CNOT(a+d -> a)` gives

```text
y = x XOR n_d.
```

The full structural census is independent of `p`: 12 of 40 word/input rows
and 384 of 7,680 one-bit edge comparisons are state-resolved dependent.
When only positive-mass inputs are counted, a delta law supports one of the
two rows and a full-support law supports both. The marginal count is six of
20 words and 192 of 3,840 edge comparisons away from the uniform point, and
zero at the uniform point.

| Exact input-family member | Supported state-resolved dependence | Marginal dependence | Per-sensitive-edge TV strength |
|---|---:|---:|---:|
| `p=0` (`delta_1`) | `6/20` rows; `192/3,840` edge pairs | `6/20` words; `192/3,840` edge pairs | `1` |
| `0<p<1/2` | `12/40` rows; `384/7,680` edge pairs | `6/20` words; `192/3,840` edge pairs | `1-2p` |
| `p=1/2` (uniform) | `12/40` rows; `384/7,680` edge pairs | `0/20` words; `0/3,840` edge pairs | `0` |
| `1/2<p<1` | `12/40` rows; `384/7,680` edge pairs | `6/20` words; `192/3,840` edge pairs | `2p-1` |
| `p=1` (`delta_0`) | `6/20` rows; `192/3,840` edge pairs | `6/20` words; `192/3,840` edge pairs | `1` |

Thus every nonuniform input distribution makes marginal neighbour dependence
nonzero. Its sum over all 192 sensitive edge pairs is
`192|2p-1|`; its average over all 3,840 declared marginal edge comparisons is
`|2p-1|/20`.

## B_BOUNDARY

The boundary is derived by exhaustive finite Boolean truth-table evaluation
followed by exact affine-polynomial elimination over the real parameter `p`.
For an incoming CNOT, the two neighbour branches have

```text
P_p(Y=0 | n_d=0) = p,       P_p(Y=1 | n_d=0) = 1-p,
P_p(Y=0 | n_d=1) = 1-p,     P_p(Y=1 | n_d=1) = p.
```

Their signed difference polynomials have coefficient pairs

```text
(-1 + 2p, 1 - 2p),
```

so

```text
TV(P_p(.|n_d=0), P_p(.|n_d=1)) = |2p-1|.
```

The primary derives these coefficients from the landed truth rows on all
3,840 word/direction/spectator comparisons. Exactly 192 comparison
polynomials are nonzero and all have the same sole root in `[0,1]`; the other
3,648 are identically zero. Therefore the exact set where state-resolved
dependence is nonzero but marginal dependence is zero is

```text
B = {mu_(1/2)}.
```

The boundary is not empty. It is the singleton uniform distribution. The
marginal-visible set is `F \ B`, so yes: not merely one but every nonuniform
input distribution makes marginal dependence nonzero.

Integrity gates do not demand this nonempty finding. The `B_BOUNDARY`
certificate checks polynomial/count/root reconciliation and would pass with
an honestly derived null boundary.

## C_PREMISE_PRICE

Cycle 970 fixed `x=0` on both neighbour branches. For its representative
incoming CNOT this produced the ordered point-mass pair

```text
n_d=0: [1,0],   n_d=1: [0,1].
```

That premise bought a delta input law, hence no cancellation between the two
XOR rows. The particular choice `x=0` was sufficient, not necessary, and
merely convenient:

- both fixed inputs (`2/2`) are state-resolved witnesses with unit TV;
- `x=1` produces the reversed ordered pair `[0,1]`, `[1,0]`;
- only `x=0` reproduces Cycle 970's exact ordered pair;
- both delta laws `p in {0,1}` reproduce its maximal strength;
- the whole uncountable family `p != 1/2` reproduces nonzero marginal
  dependence, with strength `|2p-1|`.

The general theorem therefore requires zero supplied fixed-input premises.
Its delta is zero new gate classes, couplings, axioms, and registered
primitives.

## D_CONTROLS

The primary reads Cycle 970 and Cycle 972 only as pinned provenance. Runner
blobs are parsed as AST and never executed; note blobs are read as text. The
Cycle-719 core is the sole executable science substrate. The
[`minimal-axiom memo`](MINIMAL_AXIOMS_2026-06-29.md) is text-only cited
authority. The explicit source/provenance read ledger contains exactly six
files:

1. Cycle-970 primary runner at commit `6fd0de0a288d212a4a6ce3fdd4dc9019f30dbbad`;
2. Cycle-970 theorem note at the same commit;
3. Cycle-972 primary runner at commit `3826925e019c0e1966a9b85110a397db2c61d33f`;
4. Cycle-972 theorem note at the same commit;
5. landed Cycle-719 two-rail recurrent controller core;
6. current minimal-axiom memo.

The primary replays deterministically, uses exact `Fraction` arithmetic for
all polynomial coefficients and roots, enforces a 300-second timeout contract,
and remains below the stricter 6 KB stdout ceiling. Its receipt pins its
source, live inputs, and provenance blobs; the canonical runner-cache header
independently pins the primary source and declared-input fingerprint.

The independent checker imports neither primary nor core. It parses the
primary as AST, reconstructs the 20 Boolean maps and every affine comparison,
validates the source/cache/receipt bindings, and carries an explicit falsifier
for every requested certificate. Five active corruptions—erased boundary,
erased affine signal, false uniform visibility, false necessity of `x=0`, and
a changed symbolic count—were all rejected.

## Assumptions and imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---:|---:|---|---|
| `Z^3` nearest-neighbour star | Spatial domain | zero-input structural | minimal axiom memo | yes | yes | none inside bounded theorem | framework supplied |
| `{0,1}` target/neighbor basis menu | Finite possibility-domain selector | explicit normalization/boundary condition | declared theorem cap; not selected by the Qubit axiom | yes | yes | extend the law to measures on the full `M_2(C)` domain | bounded selector |
| `X`, oriented `CNOT`, `apply_semantic` | Finite truth rows | one computed lattice input | landed Cycle-719 core | yes | yes | independent Boolean reconstruction | cross-checked |
| Cycle-970 fixed-input witness | Historical residual and exact premise price | support-only provenance | pinned runner AST and note text | no | no | re-derived from Cycle 719 | not executed |
| Cycle-972 XOR/covariance result | Historical residual and family choice | support-only provenance | pinned runner AST and note text | no | no | re-derived from Cycle 719 | not executed |
| Common target law `mu_p` on compared branches | Controlled intervention family | explicit normalization/boundary condition | exact family declaration in this note | yes | yes | enlarge to condition-dependent joint inputs in a separate theorem | scoped explicitly |
| Continuous `M_2(C)` probability law | Full Admissibility target | unsupported import if extrapolated | absent | no for bounded theorem | yes for Nature-grade closure | derive a full-domain covariant measure-valued law | remains open |

No observational values, fitted selectors, literature values, or registered
primitive edits enter the proof.

## No-Go Discipline Gate

The singleton zero set is a negative boundary only inside the declared
family. It is not an exhaustion result for other input interventions, longer
gate words, larger gate kinds, or the full possibility domain.

- **N1 — alternative routes:** five distinct enlargements remain live and
  untested by the negative boundary: (1) length-two or longer words; (2) a
  target law chosen conditionally on the compared neighbour bit; (3) a joint
  target-neighbour input with correlations; (4) additional landed gate kinds,
  including larger-arity words; and (5) probability measures and channels on
  the full continuous `M_2(C)` domain. The theorem excludes rather than
  refutes every route in this list.
- **N2 — wall independence:** no collection of independent derivation walls
  is claimed. Radius one, word length at most one, the `{0,1}` basis, and a
  common branch-independent `mu_p` are declared scope coordinates, not an
  exhaustion theorem.
- **N3 — hidden-wall scan:** the finite basis selector and common-law
  intervention are load-bearing and are listed separately in the import
  table. No observation, fitted value, or primitive registration is hidden.
- **N4 — residual matching:** the zero-set statement answers only the user
  residual “which common target-bit input laws erase the incoming-CNOT XOR
  after marginalization?” Cycle 970 and Cycle 972 are provenance, not
  negative-premise imports.
- **N5 — resolution rhetoric:** the primary cache lands the following
  execution certificate verbatim:

```text
per_element: checked and executed -- both target basis inputs and outcomes were enumerated for every declared word
per_site: checked and executed -- the target and all six radius-one neighbour coordinates were enumerated
per_mode: checked and not executed -- no Fourier or mode decomposition is claimed by this finite basis theorem
per_block: checked and executed -- every word/input/neighbour/spectator comparison block was enumerated
lattice_wide: checked and not executed -- this runner claims one target-centred star, not a new lattice-wide computation
```

- **N6 — partial-closure routes:** the present affine law is complete on its
  declared family. Any broader route requires a separately declared theorem
  family; it does not require or justify a new axiom merely to be investigated.
- **N7 — steelman:** a condition-dependent intervention with
  `P(X=0|n_d=0)=p_0` and `P(X=0|n_d=1)=p_1` has equal output marginals when
  `p_0=1-p_1`, a different one-parameter zero set. Likewise, an excluded
  length-two word can send the target to `y=n_d`, making uniform averaging
  visible. These are genuine counter-routes to any broader claim and are why
  the common-law and word-length caps are explicit.
- **N8 — cross-cycle echo:** Cycle 970 supplied the delta endpoint `p=1` and
  Cycle 972 supplied the uniform midpoint `p=1/2`; this result interpolates
  between them by exact affine algebra. It does not repeat their bounded
  conclusions as evidence for an all-domain no-go.

Disposition: PASS for the narrowly scoped negative boundary. No route outside
the declared family is ruled out.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "characterize neighbour dependence over every target-coordinate input distribution, including the exact marginal-visible/invisible boundary and the price of Cycle 970's fixed x=0 premise"
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "independently audit the bounded theorem; do not extrapolate it to longer words, condition-dependent input laws, or the full continuous M_2(C) domain"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
author_status: proposed_retained
target_claim_type: bounded_theorem
claim_type_reason: "exact finite theorem on a declared radius-one, word-length-at-most-one basis-state family"
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "exact on the declared 20-word, radius-one, basis-state target-input simplex"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
audit_status_authority: "independent audit lane only"
```

## Verdict

On the declared family, marginal neighbour dependence is visible for exactly
the nonuniform target-input laws and varies continuously from zero to unit
strength as `|2p-1|`. The only coexistence point—nonzero state-resolved
dependence with zero marginal dependence—is the uniform input. Cycle 970's
`x=0` choice selected one maximally visible endpoint but was not necessary.
The declared-family input-distribution calculation is complete; the full
continuous-domain Admissibility law remains open.
