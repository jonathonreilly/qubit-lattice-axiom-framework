# The general-n census law, the composite-ring table, and the spf floor for invariant subsets — Cycle 870

Date: 2026-08-03

Authority: none

Audit: unset

Status: bounded worked result (one worker-authored primary and one
independent checker spec'd to refute; no axiom surface touched)

Claim type: bounded_theorem

**Primary runner:**
[`frontier_cycle870_general_n_census_2026_07_28.py`](../scripts/frontier_cycle870_general_n_census_2026_07_28.py)

**Independent helper runner:**
[`frontier_cycle870_census_independent_check_2026_07_28.py`](../scripts/frontier_cycle870_census_independent_check_2026_07_28.py)

Receipt:

- [`general_n_census_law_cycle870_receipt_2026_07_28.json`](../outputs/general_n_census_law_cycle870_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: the codex worker lane hit its usage ceiling on
2026-08-03, so both runners were authored by a Claude Opus 5 worker
under supervisor spec and reviewed line-by-line by the supervisor
(substitution disclosed here). Checker independence is therefore
cross-context, not cross-model, for this package: the checker
re-derives every number through disjoint machinery (integer-only, no
sympy) and parses the primary as text behind an import firewall, but
both scripts share an authoring model family. Independent audit still
required, as for every package.

## Result up front

- **The unphased law (derived).** `I(n,k) = (n/k)*C(n-k-1,k-1) =
  n/(n-k)*C(n-k,k)` for `n >= 3`, `1 <= k <= floor(n/2)`, with
  `I(n,0) = 1`, counting the independent `k`-subsets of the labelled
  cycle `C_n` (the stipulated placement object). Proved by two routes
  stated as printed proof steps: the transfer matrix
  `T(x) = [[1,x],[1,0]]` whose trace power expands in the Lucas
  polynomial (characteristic-root recurrence residual zero
  symbolically), and an origin-marking double count that cuts the ring
  at a selected site into a path on `n-3` sites. The two closed forms
  simplify to the same expression for symbolic `n, k` (S4), so the
  eigenvalue route and the marking route are one law. Brute-verified
  `n = 3..18`; coefficient-verified symbolically `n = 3..14`; unphased
  totals reproduce the Lucas numbers `L_n` as an independent check.
- **The phased form (conditional).** Conditional on the supplied phase
  premise — one global four-valued event label attached to the whole
  placement as a free Cartesian `Z_4` factor, independent of the site
  subset; supplied, not derived, and stated as a declared import below —
  `N(n,k) = 4*I(n,k)` with `N(n,0) = 4`. Certificate S5 multiplies both
  sides of the proved unphased identity by the supplied constant: it
  certifies the conditional arithmetic, not the premise. No coupled or
  diagonal phase action is analyzed anywhere in this package.
- **n = 11.** The landed Cycle-857 phased row `176/308/220/44` at its
  declared `k = 2..5` scope is reproduced exactly (conditional on the
  same supplied phase premise) from brute enumeration, from both closed
  forms, and from the Cycle-857 literal formula at that scope. The
  `k = 1` value `N(11,1) = 44` is a new consequence of this package's
  general law — it is not part of the landed Cycle-857 row and is
  reported strictly as new scope.
- **The composite table (n = 12).** The native `k = 2` orbit spectrum is
  `{6:1, 12:4}` over 54 placements. A supplied comparator tuple
  `{2:1, 3:1, 4:1, 6:2, 12:24}`, stipulated in-file with a declared
  `k = 2` scope and no source artifact, does not match the native
  `k = 2` spectrum and matches the native `k >= 2` spectrum (309
  placements, 29 orbits) exactly. This is a local scope observation
  about a stipulated literal; it attributes nothing to any external
  document. The supplied phased row `4/4/4/8/96` equals the
  orbit-multiplicity table under the conditional phase premise and is
  false read as orbit sizes. Burnside cross-check:
  `(1/12) * sum_j L_gcd(j,12) = 372/12 = 31` total orbits, agreeing
  with enumeration.
- **The invariant-subset floor (derived).** Definition: a selection in
  this package means exactly a nonempty `C_n`-invariant subset of the
  finite placement set (a union of rotation orbits). Probabilistic,
  framed, equivariant-map, dynamical, and physical selector notions are
  outside this object and are not excluded by this result. Stabilizer
  lemma: a subset of `Z_n` fixed by the rotation subgroup of orbit
  index `g` is a union of cosets projecting to a subset of `Z_g`,
  independent iff the projection is independent in `C_g`; a nonempty
  independent fixed set therefore forces `g >= 2`. Consequence: within
  the stated definition the smallest selection has size `spf(n)`
  (smallest prime factor), realised by the coset placement
  `{0, spf, 2*spf, ...}` and its rotations. At prime `n` every nonempty
  orbit is free of size `n`; at `n = 12` the floor drops to 2
  (evens/odds). A size-1 invariant subset is impossible for every
  `n >= 3`: the only fixed subsets are the empty set and `Z_n`, and
  `Z_n` is not independent. Conditional on the supplied phase premise
  the floor multiplies to `4*spf(n)`. Möbius inversion over the divisor
  lattice reproduces the enumerated spectrum exactly and extends the
  spf law to `n <= 40`.

## Checker design and teeth

Four disjoint routes, integer arithmetic only, primary never imported:
a conditioning DP over paths/rings, an integer-polynomial transfer
matrix, minimal-period canonical forms over bitmasks, and
Burnside/Möbius over the divisor lattice with fixed points read off the
`C_gcd` sub-ring. All sixteen primary claims survived refutation
attempts (R1-R16); all seven deliberately wrong mutants were refuted
(M1-M7: off-by-one row, comparator-as-k=2, singleton invariant subset,
largest-prime-factor floor, `4^k`-per-source phase with the placement
multiplicity retained — the mutant agrees with the correct model at
`k = 1` and is killed at `k >= 2` — plain binomials, all-orbits free).
The checker's no-hardcoded-answer probe fired once mid-block: the
primary's sweep bound `EXTENDED_N_MAX = 36` collided with the derived
value `I(12,5) = 36`; the bound was moved to 40 and the cache
re-pinned — the probe worked as designed and the incident is preserved
in the commit trail.

## Scope and negative-claim discipline

The comparator finding is a scope observation about an in-file
stipulated literal, not a value or source refutation: the supplied
numbers disagree with their declared `k = 2` label and agree with the
native `k >= 2` spectrum, and no external origin for them is
identified, pinned, or evaluated. The floor statement is scoped to
nonempty `C_n`-invariant subsets of census placements; within that
definition the floor argument is a complete classification (fixed-set
argument), not a search exhaustion, and it excludes nothing outside
that definition. The phase-lifted statements are conditional on the
supplied `Z_4` premise. No claim is made about which `n` the framework
selects, and no framework dynamics are touched.

## Review record (iteration 1)

Sol combined adversarial science review, 2026-08-08, disposition
FIX_THEN_PROCEED. The following demotions were applied and are binding
on every surface of this package:

- the factor-four phased census and the `4*spf(n)` floor are
  **conditional** on the supplied free Cartesian `Z_4` phase premise;
  earlier wording that presented them as derived is retired.
- the comparator tuple's former external-source attribution was
  removed: no source artifact exists in the repository or is cited, so
  only the local comparison against the stipulated in-file literal
  stands. The earlier refutation framing of that comparison must not
  be cited.
- the landed Cycle-857 row is `176/308/220/44` at `k = 2..5`; the
  `k = 1` value is this package's new extension. Earlier wording that
  folded `k = 1` into the landed row must not be cited.
- a selection is now defined as a nonempty `C_n`-invariant subset of
  placements; the earlier broader selection wording (canonical-
  placement impossibility at large, exact pricing of the prior
  free-selection result) is retired and must not be cited as a passed
  no-go gate.
- both runners formerly gated PASS on a hard-coded author branch name;
  that gate is removed and branch/HEAD are provenance-only fields.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the free-C_11 selection no-go rides 11's primality (Cycle 857 lineage)"
source_of_blocker_text: "docs/CENSUS_THEOREM_CYCLE857_BOUNDED_THEOREM_NOTE_2026-07-28.md (provenance-only; that row is unaudited)"
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "feed the invariant-subset spf floor into any future selection-rule analysis; the composite table stands as a comparator for supplied census tuples"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the phased census N(n,k) = 4*I(n,k) and the phase-lifted floor 4*spf(n) are conditional on the supplied free Cartesian Z_4 phase premise (a declared import, not derived)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "unphased general-n law and the invariant-subset spf floor proved by printed routes with declared finite verification ranges (brute 3..18, symbolic 3..14, Moebius 3..40); every factor-four statement conditional on the supplied Z_4 premise; the comparator comparison is local to a stipulated in-file literal"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, conditional, open

### Imports (stipulated definitions and declared scope inputs)

- the placement object: independent `k`-subsets of the labelled
  oriented cycle `C_n` (stipulated formal input object, not a
  consequence of the axioms);
- the selection object: a nonempty `C_n`-invariant subset of the
  placement set (stipulated definition; nothing broader is classified);
- the supplied phase premise: one global four-valued event label
  attached to the whole placement as a free Cartesian `Z_4` factor,
  independent of the site subset (supplied, not derived; every
  factor-four statement in this package is conditional on it);
- the landed Cycle-857 `k = 2..5` phased row `176/308/220/44`, carried
  as a stipulated in-file comparator literal and re-derived natively at
  that scope;
- the supplied `n = 12` comparator tuple `{2:1, 3:1, 4:1, 6:2, 12:24}`
  with declared `k = 2` scope and phased row `4/4/4/8/96`, stipulated
  in-file with no source artifact (local comparison only);
- sympy (primary's symbolic steps only; the checker is integer-only).

### Provenance context (non-load-bearing)

- [`CENSUS_THEOREM_CYCLE857_BOUNDED_THEOREM_NOTE_2026-07-28.md`](CENSUS_THEOREM_CYCLE857_BOUNDED_THEOREM_NOTE_2026-07-28.md)
  — the landed Cycle-857 census note (its ledger row is unaudited),
  which supplies the same one-global-four-valued-label Cartesian phase
  premise at `n = 11` and whose declared `k = 2..5` generator row is
  the comparator literal above. Lineage only: the proofs here load no
  bytes from it and draw no authority from it.
- the `n = 12` comparator tuple arrived without a reviewable source
  artifact; nothing in this package identifies or evaluates its origin.

### Derived

- the unphased general-n law with two proofs and their symbolic
  identity;
- the `n = 12` orbit spectra at every scope with Burnside cross-check;
- the local comparator scope observation (mismatch under the declared
  `k = 2` label; exact match at `k >= 2`) against the stipulated
  literal;
- the stabilizer lemma, the spf floor for nonempty `C_n`-invariant
  subsets, and the impossibility of singleton invariant subsets for
  all `n >= 3`.

### Conditional (on the supplied Z_4 phase premise)

- the phased census `N(n,k) = 4*I(n,k)` and all phased totals;
- the phase-lifted floor `4*spf(n)`;
- the `k = 1` extension `N(11,1) = 44` of the Cycle-857 row (new
  scope, not landed provenance).

### Open

- a closed-form orbit spectrum (all k) at general composite n — only
  the floor law and the n = 12 table are certified here;
- derivation of the phase premise (one global four-valued label with a
  free Cartesian action), and any coupled or diagonal phase action;
- any physics-side selection consequence: which n the framework
  realises is untouched by this package.

## Verdict

The unphased census law is not an n = 11 accident: it is one two-route
theorem for every ring, and within the declared invariant-subset
definition the floor a composite ring buys is its smallest prime
factor, never one, while at prime n the floor is n itself. The
factor-four phased forms and the `4*spf(n)` floor are exactly as strong
as the supplied `Z_4` premise, which is imported, not derived. The
supplied comparator tuple matches the native `k >= 2` spectrum and not
its declared `k = 2` label — a local scope observation about a
stipulated literal, with no external attribution. Independent audit
still required.
