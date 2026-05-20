# `S^3` + Anomaly-Forced Time: Transfer-Matrix Bridge Candidate

**Status:** bounded class-A operator construction — once the cited
`PL S^3` topology, anomaly-forced single-clock time `d_t = 1`, and exact
Schur-complement boundary generator `Lambda_R` are imported as upstream
inputs, the one-step Euclidean transfer operator
`T_R := exp(-Lambda_R)` is **defined** by spectral calculus and the
runner verifies its symmetry / positivity / contraction properties.
**Not** a derivation of the upstream inputs and **not** an exact
Einstein/Regge GR dynamics closure on `PL S^3 x R`.
**Date:** 2026-04-14 (audit-narrowing refresh: 2026-05-10)
**Type:** bounded_theorem
**Status authority:** independent audit lane only.
**Authority role:** records, but does not close, a definitional class-A
transfer operator on the boundary-trace space, conditional on three
explicitly named upstream authorities. Names the missing exact
Einstein/Regge dynamics theorem as the single open theorem target for
the route.
**Purpose:** bounded transfer-matrix / discrete-action bridge from the
cited `S^3` + anomaly-forced-time + Schur stack to slice dynamics on
`PL S^3 x R`.
**Primary runner:** [`scripts/frontier_s3_time_transfer_matrix_bridge.py`](../scripts/frontier_s3_time_transfer_matrix_bridge.py) (PASS=9/0 (1 BLOCKED))

## Audit boundary

This note assembles a class-A spectral-calculus construction by
importing three upstream authorities and combining them. It is **not**
a derivation of the upstream inputs and **not** an Einstein/Regge GR
dynamics closure.

**Cited authorities (one-hop deps; cited but not closed in this note):**

- [`S3_GENERAL_R_DERIVATION_NOTE.md`](S3_GENERAL_R_DERIVATION_NOTE.md)
  (`claim_type: positive_theorem`) — supplies the `PL S^3` spatial
  background candidate (cone-capped cubical ball PL homeomorphic to
  `S^3` for `R >= 2`). Imported as the spatial-topology input. Itself
  rests on the PL boundary-link and PL cap-uniqueness theorems cited
  immediately below; both are `audited_conditional`, not retained-grade.
- [`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md)
  (`claim_type: bounded_theorem`, `audit_status: audited_clean`,
  `effective_status: retained_bounded`) —
  PL boundary-link disk theorem on `B_R`, one of the two cited PL
  authorities behind the `PL S^3` compactification. (Tier corrected
  2026-05-17: prior wording said `positive_theorem` /
  `audited_conditional`; the 2026-05-17 ledger snapshot has it at
  `bounded_theorem` / `audited_clean` / `retained_bounded`. The
  composite `PL S^3` background still inherits the weakest of the two
  cited PL companions' tiers, which is the cap-uniqueness companion's
  `audited_conditional`.)
- [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md)
  (`claim_type: bounded_theorem`, `audit_status: audited_conditional`) —
  PL cap-uniqueness companion authority for the `PL S^3` compactification.
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md)
  (`claim_type: bounded_theorem`) — anomaly-forced single-time-direction
  result. Imported for the kinematic input `d_t = 1` (one-clock Cauchy
  step).
- [`OH_SCHUR_BOUNDARY_ACTION_NOTE.md`](OH_SCHUR_BOUNDARY_ACTION_NOTE.md)
  (`claim_type: bounded_theorem`, `effective_status: retained_bounded`) —
  exact microscopic Schur-complement boundary action
  `I_R(f ; j) = (1/2) f^T Lambda_R f - j^T f` on the current strong-field
  class. Imported as the slice-Hamiltonian input. Lambda_R is itself
  retained-bounded only on the cited strong-field bridge surface; the
  bridge surface is not the full retained-grade dynamical sector.

**In-note class-A content (what the runner actually verifies, conditional
on the cited inputs):**

Conditional on `Lambda_R` (SPD on the cited surface) and `d_t = 1`
(cited), the one-step Euclidean transfer operator is **defined** by
the standard spectral calculus

> `T_R := exp(-Lambda_R)`,    `H_R := Lambda_R`.

The runner verifies the four properties that follow purely from
linear-algebra / spectral calculus on the imported `Lambda_R`:

- `Lambda_R = Lambda_R^T` to `~3.3e-16` (symmetry of imported generator);
- `Lambda_R > 0` with min eigenvalue `~1.1487` (positivity of imported
  generator on the cited bridge surface);
- `T_R = T_R^T` and `0 < eig(T_R) <= 1` (self-adjoint contraction) by
  spectral calculus from the previous two facts;
- the imported O_h finite-rank bridges are stationary points of the
  same imported `Lambda_R` quadratic form.

These are class-A consequences of the imported facts, not derivations
of `Lambda_R`, of `d_t = 1`, or of any dynamical bridge.

**Admitted-context derivation gap (real, not import-redirect):**

The note **does not** derive any of:

1. an exact `S^3`-to-curvature law on the full retained-grade dynamical
   sector;
2. an exact anomaly-to-Einstein-field-equation derivation on
   `PL S^3 x R`;
3. an exact discrete variational action whose Euler-Lagrange equations
   reproduce the Einstein/Regge metric law from the cited slice
   generator alone.

The runner explicitly records the absence of (1)-(3) as a `[BLOCKED] PASS`
line. This is a **real derivation gap**, not a dependency-citation
issue. No retained, bounded, or proposed theorem on the current atlas
closes (1)-(3) for this route.

## Verdict (scope-bounded)

**Class-A bridge construction; no GR dynamics closure.**

Conditional on the cited upstream authorities, the runner closes the
class-A operator construction:

- exact spatial `PL S^3` background (cited, `audited_conditional` PL
  authorities);
- exact one-clock Cauchy step `d_t = 1` (cited, `bounded_theorem`);
- exact slice generator `Lambda_R` from the cited Schur boundary action
  (cited, `retained_bounded` on the strong-field surface);
- one-step transfer operator `T_R = exp(-Lambda_R)` defined by spectral
  calculus, runner-verified to be a positive self-adjoint contraction.

What is still missing is the theorem that identifies that slice
generator with the full Einstein/Regge metric dynamics. The runner
explicitly records this as the open `BLOCKED` line.

## Exact ingredients already available

### `S^3` compactification

[`S3_GENERAL_R_DERIVATION_NOTE.md`](S3_GENERAL_R_DERIVATION_NOTE.md)
already gives the bounded composite spatial background candidate
(inherits the weakest of the two cited PL companions' tiers, currently
`audited_conditional` via the cap-uniqueness companion):

- the cone-capped cubical ball is PL homeomorphic to `S^3` for all `R >= 2`

### Anomaly-forced time

[`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md)
gives the cited temporal-direction result (`bounded_theorem`,
currently `unaudited`; conditional on admissions (i)-(iv) — see
[F-B framing-fix](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md)):

- anomaly cancellation plus chirality plus the one-clock Cauchy requirement force `d_t = 1`

So the cited kinematic background is:

- `PL S^3 x R` (bounded composite; tier inherited from the upstream
  composite — see "Upstream-tier accounting" remark added below).

### Exact boundary Hamiltonian

[`OH_SCHUR_BOUNDARY_ACTION_NOTE.md`](OH_SCHUR_BOUNDARY_ACTION_NOTE.md)
already gives the exact microscopic boundary action on the current strong-field class:

- `I_R(f ; j) = 1/2 f^T Lambda_R f - j^T f`

with `Lambda_R` the exact Schur-complement Dirichlet-to-Neumann matrix.

The companion Dirichlet principle note shows that the shell trace is the unique
minimum of that exact boundary energy on the current strong-field class.

## Clean bounded bridge candidate

If `d_t = 1` is the exact clock step, the natural one-step Euclidean transfer
operator on the boundary-trace space is

- `T_R := exp(-Lambda_R)`

with the associated one-slice quadratic generator

- `H_R := Lambda_R`.

This is the cleanest slice-to-slice candidate the retained stack supports
without inventing a new dynamical postulate.

Why it is the right bounded candidate:

1. `Lambda_R` is exact on the current bridge surface.
2. `Lambda_R` is symmetric positive definite on the audited source classes.
3. `exp(-Lambda_R)` is therefore a positive self-adjoint contraction.
4. The anomaly theorem supplies the unique clock direction, so the step
   size is fixed by the route-2 background rather than by an extra ad hoc
   time choice.

So Route 2 yields a well-defined discrete transfer-matrix bridge,
conditional on the cited upstream tiers (`audited_conditional` for the
`PL S^3` composite, `unaudited` for `ANOMALY_FORCES_TIME_THEOREM`,
`retained_bounded` for `OH_SCHUR_BOUNDARY_ACTION_NOTE`):

> cited spatial slice + cited one-clock time + bounded boundary Hamiltonian
>  => bounded slice transfer operator on `PL S^3 x R`

(Phrasing corrected 2026-05-17: prior wording "exact spatial slice +
exact one-clock time + exact boundary Hamiltonian" overstated each of
the three upstreams' tiers.)

## What this bridge does

The transfer matrix candidate is strong enough to say:

- the route has a canonical slice evolution operator
- the exact shell action can be propagated slice-by-slice
- the current `PL S^3 x R` background is not just a kinematic label; it
  supports a real transfer operator on the current strong-field class

That is enough to make Route 2 a genuine discrete-action bridge candidate,
not just a background theorem.

## What this bridge does not do

This candidate still does **not** prove:

1. a full pointwise Einstein/Regge dynamics theorem
2. an exact lapse/shift or kinetic term on `PL S^3 x R`
3. a unique metric law forced by the retained stack alone

So the bridge is bounded, not closed.

## Sharp blocker

The atlas still lacks an exact theorem that turns the exact slice generator
`Lambda_R` into a full dynamics bridge:

> there is no exact derivation of the Einstein metric law from the retained
> `PL S^3 x R` slice generator alone

Equivalently:

- the retained stack gives the exact slice Hamiltonian
- it does not yet give the exact time-coupling / curvature law that makes
  the bridge theorem-grade

## Runnable summary

The companion runner checks:

- `S^3` topology composite at the cited tier (`audited_conditional`
  composite via the cap-uniqueness companion);
- anomaly-forced time at the cited tier (`bounded_theorem`, currently
  `unaudited` per the 2026-05-17 ledger; admissions (i)-(iv) per the
  upstream [F-B framing-fix](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md));
- the Schur boundary generator is symmetric positive definite
  (`OH_SCHUR_BOUNDARY_ACTION_NOTE` at `retained_bounded` on the
  strong-field bridge surface only);
- the induced transfer operator `T_R = exp(-Lambda_R)` is a positive
  contraction on the current bridge surface;
- the atlas still does not contain an exact GR dynamics bridge.

(Tier-accuracy corrected 2026-05-17: prior wording "`S^3` topology is
exact / anomaly-forced time is exact" did not match the cited
upstreams' actual tiers.)

## Bottom line (scope-bounded)

Conditional on the cited upstream authorities (PL `S^3` topology, the
`bounded_theorem` anomaly-forced-time result, and the `retained_bounded`
Schur boundary generator), this note records a class-A spectral-calculus
construction:

- imported background: `PL S^3 x R`;
- imported slice generator: `Lambda_R` (SPD on the cited strong-field
  bridge surface);
- defined one-step transfer operator: `T_R = exp(-Lambda_R)`, runner-
  verified to be a positive self-adjoint contraction.

That is a real discrete-action bridge construction on the cited
strong-field bridge surface, conditional on the cited authorities. It
is **not** an exact Einstein/Regge GR closure theorem and **not** a
derivation of the upstream inputs themselves.

## Upstream-tier accounting (2026-05-17)

Per the 2026-05-17 ledger snapshot, the cited upstreams sit at:

| Upstream | `claim_type` | `audit_status` | `effective_status` |
|---|---|---|---|
| `s3_boundary_link_theorem_note` | `bounded_theorem` | `audited_clean` | `retained_bounded` |
| `s3_cap_uniqueness_note` | `bounded_theorem` | `audited_conditional` | `audited_conditional` |
| `anomaly_forces_time_theorem` | `bounded_theorem` | `unaudited` | `unaudited` |
| `oh_schur_boundary_action_note` | `bounded_theorem` | (per ledger) | `retained_bounded` |
| `s3_general_r_derivation_note` | `positive_theorem` | (per ledger) | (per ledger) |

**Tier accounting:** the composite `PL S^3` background inherits the
weakest of the two cited PL companions' tiers, currently
`audited_conditional` (via cap-uniqueness). The combined `PL S^3 x R`
background further inherits from `ANOMALY_FORCES_TIME_THEOREM` (currently
`unaudited`). The slice generator `Lambda_R` from
`OH_SCHUR_BOUNDARY_ACTION_NOTE` is `retained_bounded` on the
strong-field bridge surface only — not on the full retained-grade
dynamical sector. The composite bridge is therefore bounded at the
weakest upstream tier; earlier body wording that called any of these
"exact" or the composite "retained" was tier-loose and has been
corrected inline.

**Admission inheritance from `ANOMALY_FORCES_TIME_THEOREM`:** the bridge
imports the `d_t = 1` conclusion as the one-clock Cauchy step. Per the
upstream parent's recent
[F-B framing-fix](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md),
`d_t = 1` decomposes into a derived part (Step 3 of the parent:
`d_t ∈ {1, 3, 5, ...}`) and an inherited part (admission (iv) excludes
`d_t > 1`). Any future revision to admission (iv) propagates directly
into this bridge's one-clock-step input. The `T_R = exp(-Lambda_R)`
construction itself is unaffected by the parent's admission structure;
only the kinematic time-direction input inherits.

## Fix record (2026-05-17, downstream surgical-fix wave)

Three hostile-audit-grade issues patched on this note:

- **F-A (over-claim "exact"/"retained" in body):** §("Exact ingredients
  already available"), §("Clean bounded bridge candidate" closing line),
  §("Runnable summary"), and §("Sharp blocker") used "exact" / "retained"
  for the upstream composite. Per the 2026-05-17 ledger, the composite
  is at best `audited_conditional` (cap-uniqueness) / `unaudited`
  (anomaly-forced time). Corrected inline to "cited / bounded
  composite" wording with explicit tier qualifiers.
- **F-B (admission-inheritance disclosure):** the new
  "Upstream-tier accounting (2026-05-17)" section now records the
  parent's admission structure and links to the upstream F-B
  framing-fix. The bridge's `T_R = exp(-Lambda_R)` construction itself
  is unaffected; only the `d_t = 1` kinematic input inherits.
- **F-C-like (stale s3_boundary_link tier in cited-authorities
  block):** the boundary-link companion was cited as `positive_theorem`
  / `audited_conditional`; the 2026-05-17 ledger has it at
  `bounded_theorem` / `audited_clean` / `retained_bounded`. Corrected
  inline (mirrors the upstream fix landed in
  [PR #1507](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1507)).

See companion fix-record:
[`S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE_2026-05-17.md`](S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE_2026-05-17.md).

Paired verifier:
`scripts/frontier_s3_time_transfer_matrix_bridge_downstream_fix.py`.

None of these edits change the `T_R = exp(-Lambda_R)` definition, the
runner-verified spectral-calculus properties (symmetry, positivity,
contraction), the "Sharp blocker" wording about Einstein/Regge dynamics,
or any other in-note claim about the bridge itself.
