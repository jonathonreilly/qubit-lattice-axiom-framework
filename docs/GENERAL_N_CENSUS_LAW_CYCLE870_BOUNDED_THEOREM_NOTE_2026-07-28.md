# The general-n census law, the composite-ring table, and the spf selection floor — Cycle 870

Date: 2026-08-03

Authority: none

Audit: unset

Status: bounded worked result (one worker-authored primary and one
independent checker spec'd to refute; owner-directed campaign-5 wave 1;
no axiom surface touched)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle870_general_n_census_2026_07_28.py`](../scripts/frontier_cycle870_general_n_census_2026_07_28.py)
- [`frontier_cycle870_census_independent_check_2026_07_28.py`](../scripts/frontier_cycle870_census_independent_check_2026_07_28.py)

Receipt:

- [`general_n_census_law_cycle870_receipt_2026_07_28.json`](../outputs/general_n_census_law_cycle870_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: the codex worker lane hit its usage ceiling on
2026-08-03, so both runners were authored by a Claude Opus 5 worker
under supervisor spec and reviewed line-by-line by the supervisor
(substitution recorded in the campaign STATE). Checker independence is
therefore cross-context, not cross-model, for this block: the checker
re-derives every number through disjoint machinery (integer-only, no
sympy) and parses the primary as text behind an import firewall, but
both scripts share an authoring model family. Independent audit still
required, as for every block.

## Result up front

- **The law.** `N(n,k) = 4*(n/k)*C(n-k-1,k-1) = 4*n/(n-k)*C(n-k,k)`
  for `n >= 3`, `1 <= k <= floor(n/2)`, with `N(n,0) = 4`. Proved by
  two routes stated as printed proof steps: the transfer matrix
  `T(x) = [[1,x],[1,0]]` whose trace power expands in the Lucas
  polynomial (characteristic-root recurrence residual zero
  symbolically), and an origin-marking double count that cuts the ring
  at a selected site into a path on `n-3` sites. The two closed forms
  simplify to the same expression for symbolic `n, k` (S4), so the
  eigenvalue route and the marking route are one law. Brute-verified
  `n = 3..18`; coefficient-verified symbolically `n = 3..14`; unphased
  totals reproduce the Lucas numbers `L_n` as an independent check.
- **n = 11.** The landed Cycle-857 phased row `44/176/308/220/44` is
  reproduced exactly, from brute enumeration, from both closed forms,
  and from the Cycle-857 literal formula.
- **The composite table (n = 12).** The native k = 2 orbit spectrum is
  `{6:1, 12:4}` over 54 placements. The external math-report
  prediction `{2:1, 3:1, 4:1, 6:2, 12:24}` is **refuted at its
  declared k = 2 scope** and **exact as the k >= 2 spectrum** (309
  placements, 29 orbits) — numbers right, scope label wrong. The
  phased row `4/4/4/8/96` is correct read as orbit multiplicities
  (`x4` free phase label) and false read as orbit sizes. Burnside
  cross-check: `(1/12) * sum_j L_gcd(j,12) = 372/12 = 31` total orbits,
  agreeing with enumeration.
- **The selection floor.** Stabilizer lemma: a subset of `Z_n` fixed by
  the rotation subgroup of orbit index `g` is a union of cosets
  projecting to a subset of `Z_g`, independent iff the projection is
  independent in `C_g`; a nonempty independent fixed set therefore
  forces `g >= 2`. Consequence: **the smallest C_n-covariant selection
  of placements has size `spf(n)`** (smallest prime factor), realised
  by the coset placement `{0, spf, 2*spf, ...}` and its rotations;
  under the full `C_n x Z_4` symmetry the floor is `4*spf(n)`. At
  prime `n` every nonempty orbit is free of size `n` — this is exactly
  where the landed free-C11 selection no-go rides primality — while at
  `n = 12` the floor drops to 2 (evens/odds). A size-1 covariant
  selection is impossible for every `n >= 3`: the only fixed subsets
  are the empty set and `Z_n`, and `Z_n` is not independent. Möbius
  inversion over the divisor lattice reproduces the enumerated
  spectrum exactly and extends the spf law to `n <= 40`.

## Checker design and teeth

Four disjoint routes, integer arithmetic only, primary never imported:
a conditioning DP over paths/rings, an integer-polynomial transfer
matrix, minimal-period canonical forms over bitmasks, and
Burnside/Möbius over the divisor lattice with fixed points read off the
`C_gcd` sub-ring. All sixteen primary claims survived refutation
attempts (R1-R16); all seven deliberately wrong mutants were refuted
(M1-M7: off-by-one row, external-as-k=2, singleton selection,
largest-prime-factor floor, `4^k` phase, plain binomials, all-orbits
free). The checker's no-hardcoded-answer probe fired once mid-block:
the primary's sweep bound `EXTENDED_N_MAX = 36` collided with the
derived value `I(12,5) = 36`; the bound was moved to 40 and the cache
re-pinned — the probe worked as designed and the incident is preserved
in the commit trail.

## Scope and negative-claim discipline

The comparator refutation is a **scope correction, not a value
refutation**: the external numbers are wrong only under their declared
`k = 2` label and exact under `k >= 2`. The selection statement is
scoped to C_n-covariant (and `C_n x Z_4`-covariant) selections of
census placements; within that scope the floor argument is a complete
classification (fixed-set argument), not a search exhaustion. No claim
is made about which `n` the framework selects, and no framework
dynamics are touched.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the free-C_11 selection no-go rides 11's primality (Cycle 857 lineage)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "feed the spf floor into any future selection-rule pricing; the composite table stands as the falsifier for external census predictions"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "general-n law proved by two printed routes with symbolic identity; finite verification ranges declared (brute 3..18, symbolic 3..14, Moebius 3..40); composite table exact at n=12"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the Cycle-857 census object and its landed row (in-stack comparator,
  carried as pinned literals and re-derived, never assumed);
- the external math-report n = 12 prediction (comparator only; scored,
  refuted-as-scoped, confirmed-as-rescoped);
- sympy (primary's symbolic steps only; the checker is integer-only).

### Derived

- the general-n law with two proofs and their symbolic identity;
- the n = 12 orbit spectra at every scope with Burnside cross-check;
- the scope correction of the external prediction;
- the stabilizer lemma, the spf selection floor, the phase-lifted
  floor `4*spf(n)`, and the impossibility of singleton covariant
  selection for all `n >= 3`.

### Open

- a closed-form orbit spectrum (all k) at general composite n — only
  the floor law and the n = 12 table are certified here;
- any physics-side selection consequence: which n the framework
  realises is untouched by this block.

## Verdict

The census law is not an n = 11 accident: it is one two-route theorem
for every ring, and the free-selection no-go's dependence on primality
is now priced exactly — the floor a composite ring buys is its
smallest prime factor, never one. The external composite prediction
survives only after its scope label is corrected, which is precisely
what a falsification table is for. Independent audit still required.
