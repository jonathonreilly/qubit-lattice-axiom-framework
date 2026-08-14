---
claim_id: declared_plaquette_comparison_value_distinct_from_one_plaquette_haar_mean_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the declared Wilson surface beta = 2 N_c / g_bare^2 with N_c = 3 and g_bare = 1, beta = 6 exactly. For the normalized one-plaquette SU(3) Haar integral J(b), the June 10 recurrence and an explicit exponential-tail majorant prove p_1(6) = J'(6)/J(6) < 1/2 < 5934/10000. The last rational is a declared comparison input, historically labeled B1 in the alpha_s source, and is not derived here. This theorem separates that input from the bare one-plaquette object; it does not evaluate the correlated 4D thermodynamic-limit plaquette."
upstream_dependencies:
  - alpha_s_derived_note
  - plaquette_self_consistency_note
  - plaquette_value_derivation_program_specification_and_bracket_reduction_narrow_theorem_note_2026-06-10
runner: scripts/declared_plaquette_comparison_value_distinct_from_one_plaquette_haar_mean_2026_08_13.py
---

# Declared Plaquette Comparison Value Is Distinct from the Bare One-Plaquette Haar Mean

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact Wilson matching arithmetic on a declared surface and a
remainder-controlled bound for one normalized `SU(3)` Haar integral.
**Status authority:** independent audit lane only. This note writes no audit
verdict and predicts none.
**Primary runner:**
[`scripts/declared_plaquette_comparison_value_distinct_from_one_plaquette_haar_mean_2026_08_13.py`](../scripts/declared_plaquette_comparison_value_distinct_from_one_plaquette_haar_mean_2026_08_13.py)

## Result up front

The `alpha_s` forward-computation source
[`ALPHA_S_DERIVED_NOTE.md`](ALPHA_S_DERIVED_NOTE.md) takes
`<P> = 0.5934` as a declared boundary input. Its historical local label for
that input is `B1`; the label is provenance, not the primary name of this
theorem and not a live admission class. The finite-diagnostic source
[`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
does not derive that numeral. Current premise governance supplies no live
admission that could make the numeral an axiom consequence.

On the separately declared Wilson matching
`beta = 2 N_c / g_bare^2`, the point `N_c = 3`, `g_bare = 1` selects
`beta = 6` exactly. The normalized bare one-plaquette Haar mean at that point
satisfies the certified separation

```text
p_1(6) = J'(6)/J(6) < 1/2 < 5934/10000.
```

Thus the matching convention plus the bare one-plaquette Haar measure does
not reproduce the declared comparison value. This is an object-separation
theorem. It neither derives `0.5934` nor evaluates the correlated 4D
thermodynamic-limit plaquette `<P>*` specified by the June 10 source
[`PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`](PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact matching arithmetic and a certified one-plaquette separation are proved; the 4D thermodynamic-limit plaquette value is not evaluated."
trace_class: negative_route_pruning
target_claim_id: alpha_s_derived_note
target_blocker_text: "certify the correlated 4D thermodynamic-limit Wilson plaquette value represented by the declared comparison input 5934/10000"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "evaluate a certified finite-volume three-point ln Z_L bracket or another rigorous 4D Wilson/Haar route"
conditional_surface_status: "exact only on the declared beta = 2 N_c/g_bare^2 matching and the normalized bare one-plaquette SU(3) Haar measure; no 4D value closure"
hypothetical_axiom_status: no edit
admitted_observation_status: "no live admission class is invoked; 5934/10000 is compared only as declared data from the alpha_s source"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and provenance (one hop)

- **M1 (declared matching).** `N_c = 3`, `g_bare = 1`, and
  `beta = 2 N_c/g_bare^2` are stipulated evaluation data on this surface.
  The matching is a convention, not an axiom consequence.
- **M2 (exact single-link engine).** The June 10 source supplies the
  normalized Haar integral
  `J(b) = int_SU(3) exp((b/3) Re Tr U) dHaar U = sum_{n>=0} a_n b^n`,
  the recurrence

  ```text
  6(N+1)(N+4)(N+5) a_{N+1}
    = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2},
  ```

  and seeds `a_0 = 1`, `a_1 = 0`, `a_2 = 1/36`. The paired runner
  recomputes all coefficients used here as exact rationals.
- **M3 (declared comparison datum).** `5934/10000` is read from the
  `alpha_s` source under the finite-diagnostic source's non-derivation
  boundary. It is not an input to `J`, `J'`, the recurrence, or either
  remainder bound.

No axiom memo is a load-bearing premise. No Monte Carlo sample, fitted
selector, 4D transfer matrix, or thermodynamic-limit assumption enters the
proved inequality.

## Exact objects and obligation graph

The bare one-plaquette mean is

```text
p_1(b) := (d/db) ln J(b) = J'(b)/J(b).
```

This is the mean of `(1/3) Re Tr U` under one normalized Haar measure
reweighted by `exp((b/3) Re Tr U)`. It is not the interacting 4D object
`<P>* := 1 + f'(6)`.

| obligation | input | exact check | output |
|---|---|---|---|
| O1 | M1 | `2*3/1^2 = 6` | declared point `beta=6` |
| O2 | M2 | recurrence seeds and coefficients through order 20 | exact `J_N`, `J'_N` |
| O3 | `Re Tr U in [-3/2,3]` from M2 | `0 <= a_n <= 1/n!` | exponential tail majorants |
| O4 | O2, O3 at `N=16` | `J_16 - 2(J'_16+R'_16)>0` | `p_1(6)<1/2` |
| O5 | O4, M3 | `1/2 < 5934/10000` | strict object-value separation |
| O6 | object definitions | bare one-plaquette versus correlated 4D measure | scope boundary retained |

The target is exactly O5. O6 prevents the target from being silently enlarged
to a statement about every method for computing `<P>*`.

## Coefficient and remainder lemmas

The recurrence at `N=2` gives

```text
6*3*6*7*a_3 = 2*3*(1/36) + 1 = 7/6,
a_3 = 1/648.
```

At `N=3` it gives

```text
6*4*7*8*a_4 = 3*4*(1/648) + 2*9*(1/36) = 14/27,
a_4 = 1/2592.
```

Every recurrence coefficient on the right is nonnegative and the denominator
is positive, so induction gives `a_n >= 0`. Since
`|(1/3) Re Tr U| <= 1`, the moment expansion also gives
`a_n <= 1/n!`.

For integer `M>6`, successive terms in the exponential tail have ratio at
most `6/(M+1) < 6/M`, hence

```text
sum_{k=M}^infinity 6^k/k!
  <= (6^M/M!) * sum_{j=0}^infinity (6/M)^j
  =  (6^M/M!) * M/(M-6).
```

For a truncation at order `N`, the valid bounds are therefore

```text
R_N  := (6^(N+1)/(N+1)!) * (N+1)/(N-5),
R'_N := (6^N/N!)         * N/(N-6),

0 <= J(6)-J_N   <= R_N,
0 <= J'(6)-J'_N <= R'_N.
```

The displayed `R_N` is deliberately indexed by its first omitted term
`M=N+1`; this avoids the off-by-one factor present in the submitted draft.
Positivity then gives

```text
J'_N/(J_N+R_N) <= p_1(6) <= (J'_N+R'_N)/J_N.
```

## Theorem — exact separation at the declared point

At `N=16`, exact recurrence arithmetic gives

```text
J_16  = 251763633587 / 73156608000,
J'_16 = 443237359 / 304819200,
R'_16 = 944784 / 4379375,
J'_16 + R'_16 = 259952292959 / 155675520000.
```

The decisive rational is

```text
J_16 - 2(J'_16 + R'_16)
  = 5323057146257 / 52306974720000 > 0.
```

Thus `p_1(6)<1/2`. Only after this bound is closed do we compare M3:

```text
1/2 = 5000/10000 < 5934/10000.
```

Consequently

```text
p_1(6) < 1/2 < 5934/10000.
```

The runner repeats the proof at `N=20`; its certified interval is contained
in `(0.42245, 0.42316)`, far from both `1/2` and the declared datum. That
second truncation is a robustness check, not a new premise.

## No-Go Discipline: narrow exclusion and preserved routes

This note excludes only the route “identify the declared comparison value
with the bare one-plaquette Haar mean at the declared matching point.” It
does not issue a general no-go for deriving `<P>*`.

### N1 — materially distinct route scan

| route | marker | outcome relative to this theorem |
|---|---|---|
| replace the matching by `2N_c g_bare^2` | **ATTEMPTED** | exact gates at `(3,1),(3,2),(2,1)` reject it as the declared matching |
| omit the factor two in the matching | **ATTEMPTED** | the same exact gates reject it |
| identify `5934/10000` with the bare Haar mean | **ATTEMPTED** | the certified half-ceiling rejects equality |
| use the correlated 4D Wilson/Haar measure | **ATTEMPTED** | changes the measure and is therefore outside, but remains a live route to `<P>*` |
| use a supplied effective plaquette environment | **ATTEMPTED** | changes the single-plaquette object and remains a live conditional route |
| use finite-volume `ln Z_L` enclosures and a thermodynamic-limit rate | **ATTEMPTED** | outside the bare integral; preserved as the June 10 certification route |
| use a convergent reorganization, transfer operator, or tensor method | **ATTEMPTED** | not decided by the present calculation and remains open |

### N2 — wall independence

No conjunction of walls is claimed. The exact rational separation is one
object-specific wall. The finite-volume bracket, mass-gap sharpening, and
4D evaluation tasks are alternative or composable methods, not asserted
independent impossibility certificates.

### N3 — hidden-wall scan

The proof depends on the stipulated matching, normalized `SU(3)` Haar
measure, June 10 recurrence, and exact declared comparator. It does not
silently assume an infinite-volume limit, differentiability of `f` at six,
a mass gap, a finite-size scaling ansatz, a chosen 4D environment, or an
axiom-derived coupling.

### N4 — residual matching

The June 10 residual is certification of the correlated 4D object, while
the present residual is explicitly the same: compute `<P>*`, not `p_1`.
The `alpha_s` source identifies the numeral as a declared input and the
finite diagnostic withholds its derivation. No stronger prior no-go is
borrowed.

### N5 — certificate granularity

```text
per-element: executed — exact recurrence coefficient arithmetic
per-site: not applicable — the proved object has no lattice sites
per-mode: not applicable — no mode decomposition is used
per-block: executed — the one-plaquette Haar block is fully bounded
lattice-wide: not executed — no correlated 4D lattice is evaluated
```

### N6 — partial-closure paths

The June 10 three-point `ln Z_L` bracket is preserved. A stronger finite-size
rate, a certified 4D Monte Carlo enclosure, or a rigorous transfer/tensor
evaluation could also supply useful 4D progress without altering the present
theorem or any axiom.

### N7 — steelman

The strongest objection is that the bare one-plaquette measure is not the
physical comparator: 4D correlations can change the mean, so its failure to
equal `0.5934` says little about the full Wilson theory. The objection is
correct. The theorem is retained only as a precise route-pruning and
object-separation result.

### N8 — cross-cycle echo

The June 10 source already distinguishes `J(6)` from `<P>*` and keeps the
finite-volume bracket open. The finite 4D diagnostic likewise withholds an
infinite-volume value certificate. This note agrees with those boundaries;
it does not convert earlier one-plaquette failures into a universal closure.

## Boundaries and explicit non-claims

- `0.5934` is declared comparison data, not a derived or admitted theorem.
- The result is coupling-specific at the declared `beta=6` point; it is not
  a coupling-independent ceiling.
- No 4D `<P>*` evaluation, Monte Carlo certificate, cluster-convergence
  radius, mass-gap rate, or differentiability result is claimed.
- No axiom edit, axiom necessity, or new primitive is proposed.
- Changing the measure, action, matching, or environment defines a different
  object and is not excluded as a route to the 4D target.

## Verification

Run:

```bash
python3 scripts/declared_plaquette_comparison_value_distinct_from_one_plaquette_haar_mean_2026_08_13.py
```

The runner uses exact `Fraction` arithmetic for the recurrence, tail bounds,
matching identities, and comparator. It declares every repository file it
reads for cache fingerprinting, includes family-specific mutation gates, and
writes no audit verdict. Expected summary:

```text
TOTAL: PASS>=30 FAIL=0
```
