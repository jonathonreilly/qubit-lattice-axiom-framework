# Observable-Principle P1 NU License Narrowing No-Go

**Date:** 2026-06-10
**Type:** no_go
**Claim type:** no_go
**Claim scope note:** narrow source note for the P1 exponent-selector
license. The conditional selector target uses the `(NU)` premise: global
constant-sign nonzero curvature plus finite `nu[W] = sup W'(z)^2/|W''(z)|`
on `R_{>0}`. This note proves that `(NU)` implies a weaker single response
clause `(BR): sup_{z>0} |z W'(z)| < infinity`, proves `(BR)` alone selects
the logarithmic exponent on the tested exponent family, and shows that the
linked current supplier candidates do not supply `(NU)` or `(BR)`.
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/observable_principle_p1_nu_license_check_2026_06_10.py`](../scripts/observable_principle_p1_nu_license_check_2026_06_10.py)
(`TOTAL: PASS=38 FAIL=0`).
**Runner cache:**
[`logs/runner-cache/observable_principle_p1_nu_license_check_2026_06_10.txt`](../logs/runner-cache/observable_principle_p1_nu_license_check_2026_06_10.txt).

---

## Question

The target theorem
[`OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md`](OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md)
is conditional on a readout regularity premise:

```text
(NU)
  W'' exists, is nonzero, and has constant sign on all of R_{>0};
  nu[W] := sup_{z>0} W'(z)^2 / |W''(z)| < infinity.
```

That premise point-selects the logarithmic member of the normalized exponent
family, but it was left as an unlicensed input. This note asks two narrower
questions:

1. Can the license demand be reduced to a smaller clause?
2. Do the linked current supplier candidates already provide that smaller
   clause?

## Result

The demand reduces cleanly:

```text
(NU)  =>  (BR): sup_{z>0} |z W'(z)| < infinity.
```

`(BR)` is strictly weaker than `(NU)`, but it is still strong enough for the
tested selector. On the family

```text
g_p(z) = (z^p - 1) / p,       p != 0,
g_0(z) = log z,
```

the log-scale response is

```text
z (s g_p)'(z) = s z^p.
```

That response is bounded on `R_{>0}` exactly when `p = 0`. Thus a future
license for `(BR)` would already close the exponent selection in this
neighborhood.

The no-go part is also narrow: the linked supplier candidates do not provide
`(NU)` or `(BR)`. The runner supplies two independent witnesses:

- `W_G(z) = log z + (log z)^3` satisfies the formalized readout-side
  constraints tested here, but its curvature changes sign. It kills any
  supplier claim for `(NU)`'s constant-sign curvature clause.
- `W_Q(z) = (z^2 - 1)/2` has constant-sign curvature, but
  `W'(z)^2 / |W''(z)| = z^2` and `z W'(z) = z^2` are unbounded. It kills
  any supplier claim for finite `nu` or `(BR)`.

Therefore this note does not retire P1 and does not ratify `(NU)` or `(BR)`.
It replaces a two-clause barrier regularity residual with one named missing
response-bound residual.

## Lemma N: `(NU) => (BR)`

Let `u = log z`, `h(u) = W(e^u)`, and `g(u) = h'(u) = z W'(z)`. Then

```text
h''(u) - h'(u) = z^2 W''(z).
```

If `z^2 W''(z) < 0`, the finite-`nu` clause gives

```text
g' <= g - g^2/nu.
```

If `z^2 W''(z) > 0`, it gives

```text
g' >= g + g^2/nu.
```

The runner checks the logistic and super-logistic comparison solutions and
their finite blow-up times exactly. On the negative-curvature branch,
values `g > nu` blow up backward and values `g < 0` blow up forward, so
`0 <= g <= nu`. On the positive-curvature branch, the reflected argument
gives `-nu <= g <= 0`. In both cases

```text
sup |z W'(z)| = sup |g(u)| <= nu[W].
```

The full `R_{>0}` domain is load-bearing; on compact domains the response
bound collapses and does not select.

## Strictness And Selector Value

The ladder is strict:

```text
Additivity + continuity  =>  (NU)  =>  (BR).
```

The runner verifies:

- `s log z` satisfies `(NU)` and `(BR)` sharply.
- A bounded oscillatory readout gives `(NU)` without additivity.
- The Fisher chart readout
  `W_F(z) = log((z + 1/z)/2)` gives `(BR)` without `(NU)`.
- The sine/cosine witness family passes `(BR)` while violating the additive
  identity at nondegenerate pairs, so `(BR)` remains outside the extended
  irreducible additive class used by the target theorem.

This is the positive value of the note: the missing license is smaller than
the target theorem's original premise.

## Supplier Hunt

The linked amplitude-side rows are readout-blind for this question. The
runner recomputes an exact positive-determinant/Neumann family and verifies
that `log`, `W_G`, and `W_Q` all compose with the same positive amplitude
branch. Those amplitude facts do not inspect the curvature or log-scale
response of the readout.

The Fisher route is the strongest readout-side candidate. Even if one grants
the two bridges it would need but does not itself supply, a probability path
on records and the exponential amplitude coordinate `z = e^h`, the row's own
canonical two-outcome chart yields

```text
W_F(z) = log((z + 1/z)/2).
```

That readout has sign-changing curvature and infinite `nu`, while still
having bounded response. It is a strictness witness for `(BR) < (NU)`, not a
supplier of `(NU)`.

The Record/probability firewalls remain respected: this note does not create
a probability law for records, does not identify a branch-to-scalar map, and
does not infer a readout regularity law from finite records.

The runner also performs a current parser scan for curvature, barrier,
response-bound, log-scale, readout-regularity, and bounded-resolution
vocabulary among retained-grade rows. It finds no supplier row. That scan is
diagnostic support for the route review; the load-bearing no-go is the
structural witness pair above plus the supplier-route analysis.

## Boundaries

- `(BR)` is a local clause name in this note, not a new axiom, primitive,
  registry entry, or accepted premise.
- The note uses the T1-d style full positive-amplitude domain as the domain
  on which the target theorem is formulated. It does not derive that domain.
- Compact images, including the tested Neumann image, do not select:
  every exponent has finite response on compact positive intervals.
- The note supplies no probability rule, normalization rule, weighting rule,
  record-count law, branch-to-scalar map, empirical input, or audit verdict.
- The next live target is a genuine license for `(BR)`: a structure forcing
  uniformly bounded response per e-fold of amplitude.

## No-Go Discipline Gate

- **N1 alternative routes:** amplitude-side determinant/RP/quasilocality rows
  were tested and are readout-blind; Fisher tangent geometry was steelmanned
  and gives the wrong readout regularity; Record/probability routes are
  blocked by the linked firewalls; compact-domain/domain routes were tested
  and collapse selection; direct supplier vocabulary scan found no current
  retained-grade supplier; additivity/irreducibility routes are escaped by
  the sine/cosine witnesses.
- **N2 wall independence:** the original `(NU)` curvature and finite-`nu`
  walls collapse to the weaker missing `(BR)` response-bound wall for this
  selector. The full-domain assumption remains separate and is not derived
  here.
- **N3 hidden-wall scan:** the readout function, full `R_{>0}` domain,
  smoothness, supplier-row scope, and the two Fisher bridges are named
  explicitly. None is smuggled as an axiom or primitive.
- **N4 residual matching:** the residual is exactly the target theorem's
  unlicensed readout-regularity premise, narrowed to `(BR)`. No claim is made
  about unrelated P1 routes.
- **N5 rhetoric audit:** "no supplier" means no supplier among the linked
  current candidates under the stated readout and domain. It does not mean a
  future record-capacity or finite-resolution theorem cannot supply `(BR)`.
- **N6 partial-closure scan:** the natural partial-closure path is a future
  theorem deriving bounded log-scale response from record capacity, finite
  resolution, or another readout-side structure. This would be an import
  retirement path, not a new axiom by default.
- **N7 steelman:** a hostile reviewer would argue that finite records should
  cap response per e-fold. That is plausible as a next theorem, but it is
  exactly `(BR)` and is not supplied by the current linked rows.
- **N8 cross-cycle echo:** this matches prior route-narrowing work: a broad
  admitted/conditional premise is split, tested clause by clause, and the
  surviving wall is named more precisely rather than declared solved.

## Runner Checks

The runner checks:

- exponent-family normalization and the `p -> 0` logarithmic limit;
- `(BR)` point-selection on `{s g_p}`;
- the log-coordinate identities and comparison-solution blow-up times for
  Lemma N;
- sine/cosine witnesses showing `(BR)` escapes the extended irreducible
  additive class;
- `W_G`, `W_Q`, and `W_F` witness calculations;
- exact determinant/Neumann amplitude examples demonstrating readout
  blindness;
- compact-domain collapse;
- current supplier-row presence/status diagnostics;
- honest-scope and firewall-compliance strings.

## Dependencies

- [OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md](OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md)
  is the conditional target whose `(NU)` premise is narrowed.
- [OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md](OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md)
  supplies the extended irreducible-class target escaped by `(NU)` and `(BR)`.
- [REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md](REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md)
  supplies the determinant/Neumann amplitude-side surface recomputed by the
  runner.
- [SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md](SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md)
  is the tested Fisher candidate.
- [REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md)
  is an amplitude-side positivity candidate.
- [POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md](POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md)
  and
  [OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md](OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md)
  supply the record/probability firewall boundaries.
- [OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  is cited only for the legacy T1-d style readout-domain boundary, not as an
  axiom-premise node.

## Command

```bash
python3 scripts/observable_principle_p1_nu_license_check_2026_06_10.py
```

Expected deterministic summary:

```text
TOTAL: PASS=38 FAIL=0
```

## Honest Status

```yaml
claim_type_author_hint: no_go
claim_scope: "Narrow P1 readout-license route note. Proves NU implies BR, proves BR alone selects the logarithmic exponent on the tested exponent family, and shows the linked current supplier candidates do not supply NU or BR. Does not retire P1 or ratify BR."
upstream_dependencies:
  - observable_principle_p1_exponent_barrier_parameter_selector_narrow_theorem_note_2026-06-10
  - observable_principle_p1_exponent_fixing_irreducibility_narrow_note_2026-05-31
  - real_diagonal_source_det_positivity_and_log_readout_lemma_note_2026-06-08
  - sharp_record_fisher_tangent_space_narrow_theorem_note_2026-06-06
  - reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10
  - post_record_count_probability_firewall_2026-06-06
  - observable_principle_record_scalar_map_no_go_note_2026-06-05
  - observable_principle_from_axiom_note
admitted_context_inputs: []
source_sets_audit_outcome: false
```
