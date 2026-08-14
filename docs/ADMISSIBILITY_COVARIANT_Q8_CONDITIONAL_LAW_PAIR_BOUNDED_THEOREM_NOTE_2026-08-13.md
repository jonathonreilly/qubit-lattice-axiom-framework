---
claim_id: admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Two separately declared nearest-neighbor conditional probability laws on the one-site M_2(C) possibility domain satisfy the current Admissibility contract. Both use the parity of the number of +I values in the six-site neighbor shell, vary between two shell conditions, and are covariant under translations and proper cubic rotations. The central law has delta outputs at +I and -I, fixed by every internal SU(2) conjugation. The axis law has an odd-parity output uniform on the six quaternion-axis points; a pi/4 internal rotation maps one support point outside that finite support. These are exact finite-support law models, not a selection of the physical law, a gauge-step process, Haar measure, heat kernel, or Record readout."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_covariant_q8_conditional_law_pair_2026_08_13.py
---

# A Covariant Pair Of Finite-Support Admissibility Laws With Distinct Internal Symmetry

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** two explicit nearest-neighbor conditional probability laws with
finite support inside the full one-site possibility domain `M_2(C)`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_covariant_q8_conditional_law_pair_2026_08_13.py`](../scripts/admissibility_covariant_q8_conditional_law_pair_2026_08_13.py)

## Result up front

The current Admissibility axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) requires one
fixed nearest-neighbor rule whose local probability distribution is determined
by, and varies with, the nearest-neighbor conditions. The rule is covariant
under lattice translations and proper cubic rotations.

This note constructs two separate models of that contract. Each rule reads the
same rotation-invariant Boolean from a site's six-neighbor shell. One rule
returns delta measures at the two central matrices `+I` and `-I`. The other
returns `delta_(+I)` for even parity and the uniform measure on the six
quaternion-axis matrices for odd parity. Both rules are fixed, local, varying,
and proper-cubic covariant.

Their internal conjugation behavior differs. The central outputs are fixed by
every `SU(2)` conjugation. A declared `pi/4` rotation about the third axis sends
the axis atom `i sigma_x` to

```text
i (sigma_x + sigma_y) / sqrt(2),
```

which lies outside the six-axis support. This is a positive pair-of-models
witness. It selects neither rule as the framework's physical law.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two finite-support conditional laws, their nearest-neighbor variation, proper-cubic covariance, and distinct internal-conjugation behavior are proved exactly. The physical law, gauge-step identification, process, generator, and continuum extension are not selected."
trace_class: upstream_support
target_claim_id: ad_invariant_gauge_step_measure_derivation
target_blocker_text: "identify a physical internal-conjugation law for a gauge-step process from separately supported dynamics"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "derive a physical map from the local Admissibility distribution to a gauge-step process before using an internal conjugation property in a heat-kernel argument"
conditional_surface_status: "exact for the two declared local laws and their finite supports; no physical law selection, gauge-step process, Haar measure, heat kernel, or continuum theorem"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared mathematical objects

The only scientific dependency is the current four-axiom authority linked
above. In particular, this theorem uses Admissibility's conditional
probability-law clause and the Qubit's full one-site algebraic presentation
`M_2(C)`.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the standard quaternion embedding
  `Q_8={+I,-I,+i sigma_x,-i sigma_x,+i sigma_y,-i sigma_y,+i sigma_z,-i sigma_z}`
  inside `SU(2)` and hence inside `M_2(C)`;
- the 24 proper signed-permutation rotations of the three coordinate axes;
- ordinary finite-support Borel probability measures on `M_2(C)`; and
- one internal `pi/4` rotation about the third axis as an explicit symmetry
  discriminator.

The exact atomic laws below are witness choices. They are not derived values
of the physical Admissibility rule. No observational comparator, literature
constant, Wilson weight, heat-kernel measure, rate, or generator is imported.
No Record functional appears: the construction uses no scalar collection
readout, no finite additivity, and no value assigned to an absent record.

## Exact target and objects

**Target.** Construct two separately declared probability-law models on the
six-neighbor shell that satisfy the current local Admissibility covariance
contract and have explicitly different internal `SU(2)` conjugation behavior.

Let the six nearest-neighbor directions at a site be

```text
D={+e_x,-e_x,+e_y,-e_y,+e_z,-e_z}.
```

For a shell assignment `eta:D->M_2(C)`, define

```text
b(eta) = (# {d in D : eta(d)=+I}) mod 2.
```

Translations carry this same definition from site to site. A proper cubic
rotation permutes the six directions and fixes the central matrix `+I`, so it
preserves `b`.

Define three probability measures on `M_2(C)`:

```text
delta_+  = point mass at +I,
delta_-  = point mass at -I,
nu_axis  = (1/6) sum_{a in {+x,-x,+y,-y,+z,-z}} delta_(i sigma_a),
```

where the sign in the index also changes the sign of the matrix. The two fixed
conditional laws are

```text
P_central(.|eta) = delta_+   if b(eta)=0,
                   delta_-   if b(eta)=1;

P_axis(.|eta)    = delta_+   if b(eta)=0,
                   nu_axis   if b(eta)=1.
```

These are two separate model laws. The theorem does not place both rules into
one physical model, and it does not choose between them.

## Proof-obligation graph

| obligation | exact disposition |
|---|---|
| embed the eight displayed atoms in `M_2(C)` | the standard quaternion matrices lie in `SU(2) subset M_2(C)` |
| normalize each output | each delta has mass one; `nu_axis` has six masses `1/6` |
| establish nearest-neighbor determination | each output is a function only of `b(eta)` |
| exhibit variation with shell condition | the all-`+I` shell has even parity; changing one neighbor to `-I` gives odd parity and a different output |
| establish translation covariance | the same shell formula is used at every translated site |
| establish proper-cubic covariance | rotations permute shell slots, fix `+I`, and permute the six axis atoms |
| establish the central law's internal symmetry | `+I` and `-I` are central under every `SU(2)` conjugation |
| exhibit distinct internal behavior for the axis law | the declared `pi/4` conjugation maps `i sigma_x` outside the six-axis support |
| identify either model as the physical rule | open and not claimed |
| construct a gauge-step process, generator, Haar law, or heat kernel | outside the theorem and not claimed |

Every leaf needed for the stated finite-support target is discharged. The two
last rows are downstream physics questions, not terminal lemmas of this target.

## Theorem 1 — both rules satisfy the local covariance contract

The predicate `eta(d)=+I` is unchanged by internal conjugation, and a proper
cubic rotation only permutes the six directions. Hence

```text
b(R eta)=b(eta)
```

for every proper cubic rotation `R`. The output measures `delta_+` and
`delta_-` are fixed by every such rotation. The measure `nu_axis` is also
fixed because the proper cubic group permutes its six atoms transitively with
equal weights. Therefore

```text
R_* P_central(.|eta) = P_central(.|R eta),
R_* P_axis(.|eta)    = P_axis(.|R eta).
```

The formulas are site-independent, so the same statement holds after a
lattice translation. Both rules depend only on the nearest-neighbor shell.

For variation, compare

```text
eta_even = (+I,+I,+I,+I,+I,+I),
eta_odd  = (-I,+I,+I,+I,+I,+I).
```

They have parity zero and one respectively. Thus `P_central` changes from
`delta_+` to `delta_-`, while `P_axis` changes from `delta_+` to `nu_axis`.
Both conditional distributions are determined by and vary with the shell.

## Theorem 2 — the two rules have distinct internal symmetry

Every `h in SU(2)` satisfies

```text
h (+I) h^{-1}=+I,
h (-I) h^{-1}=-I.
```

Consequently every output of `P_central` is fixed by the full internal
conjugation action.

Now let `h` be the `SU(2)` element whose adjoint action is a `pi/4` rotation
about the third coordinate axis. Then

```text
h (i sigma_x) h^{-1}=i(sigma_x+sigma_y)/sqrt(2).
```

The right side has two nonzero coordinate components, whereas every atom in
the support of `nu_axis` has exactly one. Thus

```text
nu_axis({i sigma_x})=1/6,
nu_axis({h(i sigma_x)h^{-1}})=0,
h_* nu_axis != nu_axis.
```

At odd parity the two local laws therefore display different exact internal
symmetry behavior while satisfying the same spatial covariance contract.

## Boundary and falsifiers

The result is falsified if any of the following finite statements fails:

- the proper cubic rotations fail to permute the six shell directions;
- a rotation changes the parity `b`;
- any displayed output fails probability normalization;
- `nu_axis` fails proper-cubic invariance; or
- the declared internal `pi/4` image remains in the six-axis support.

The theorem does not identify either witness as the physical Admissibility
rule. It supplies no map from a one-site conditional possibility law to a
gauge-link step process, no continuum `SU(2)` measure, no Haar selection, no
Markov generator, no heat kernel, no Wilson action, and no record-formation or
readout dynamics. Those would require separate retained derivations or
explicitly declared downstream inputs.

## Review record

The submitted version used a retired scalar Record functional `I`, finite
additivity, and `I(empty)=0`. The current axiom memo explicitly removes those
structures, and the submitted runner fails its source-premise check on current
`main`. The submission also framed one dummy-sum route as a negative result
without a complete No-Go Discipline packet or the required five-resolution
execution certificate.

This repair removes the Record argument, the `C_3` dummy sum, the heat-kernel
context claims, and the broad negative framing. What remains is the positive
current-axiom-compatible pair of explicit conditional-law models proved above.
The repaired source contains no semantic no-go or wall claim; the original
negative disposition failed N1, N3, N5, N6, and N7 and is not shipped.

## Verification

```bash
python3 scripts/admissibility_covariant_q8_conditional_law_pair_2026_08_13.py
```
