# The horizon doubles twice — and one configuration comes clean — Cycle 790

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (HORIZON_CLOSES; the first clean
postimage beyond T = 64; the content-vs-dirt question open in both
directions)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle790_horizon_extension_2026_07_28.py`](../scripts/frontier_cycle790_horizon_extension_2026_07_28.py)
- [`frontier_cycle790_horizon_independent_check_2026_07_28.py`](../scripts/frontier_cycle790_horizon_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 762 found zero clean postimages at horizon T = 64 and
forever-nonzero residual cycles — the finding that made multi-source
residual state a candidate for content rather than dirt. This cycle
doubled the horizon twice:

- **HORIZON_CLOSES**: clean counts T64 = 0 (identity control,
  reproduced exactly), T128 = 0, **T256 = 1** — epoch 3 at positions
  (1, 10) becomes clean **first and exactly at t = 252**. The checker
  verified the event with the LANDED test and its own evolution:
  nonclean at every t < 252, clean at 252, and no other configuration
  clean anywhere through T = 256;
- **the reimplementation is faithful**: the 762 pair was not
  importable in this checkout, so the machinery was rebuilt from the
  sha-anchored source — and the checker verified fidelity against the
  landed test on the full T = 64 census: **all 176 verdicts and 11,440
  residual samples agree** byte-exactly;
- **the cycle census**: period-2 residual cycles on 2 keys, period-3
  on 9 (state-recurrence certified independently; forever-nonzero for
  every certified cycle); **164 keys remain open** through T = 256
  (10/10 spot checks); the period-divisibility table (2 | 130, 2 | 12,
  3 | 12) is printed as data;
- **what changes**: the 762 extrapolation ("forever nonzero") does not
  extend universally — at least one lawful two-source configuration's
  residual is a long transient, not a permanent feature. The
  clean_postimage veto that kills all 638 multi-source exclusions
  (Cycle 787) is horizon-relative for at least one configuration: a
  **horizon-extended postimage law** is now a live, evidenced route to
  multi-source actuality — while the certified period-2/3 cycles show
  other configurations really do cycle forever;
- controls: T = 64 identity exact; determinism byte-identical; the
  anchor certificate verifies the 762 sources byte-exact whether read
  from git lineage or pinned-identical disk copies (never imported —
  the reimplementation basis is preserved).

## Supplied / derived / open

### Supplied

- everything the Cycle-719/736/762 packages declare at their scopes.

### Derived

- the faithful reimplementation (checker-verified against the landed
  test); the T = 128/256 censuses; the t = 252 first-clean event and
  its uniqueness; the certified cycle census and the open-key count;
  the divisibility table.

### Open

- the content-vs-dirt ruling (open in BOTH directions, now with
  evidence on both sides: one transient, eleven certified cycles);
  horizons beyond 256 for the 164 open keys; the horizon-extended
  postimage law as a derivation target.

## Negative-claim discipline

HORIZON_CLOSES states an existence fact (one configuration, one time);
the certified forever-nonzero cycles are scoped to their 11 keys; the
164 open keys are labeled open, not extrapolated.

## Verdict

The census that looked settled at T = 64 had a surprise at t = 252:
one configuration's "permanent" residual was a transient with a long
fuse. The multi-source wall's one law is now known to be
horizon-relative for at least one case — which turns the
horizon-extended postimage law from speculation into the single most
evidenced route to multi-source actuality the campaign has produced.
Independent audit still required.
