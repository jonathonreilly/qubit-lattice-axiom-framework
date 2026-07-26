# Cycle 709 — BACKLOGGED (eighth). Two of my claims were wrong.

Branch: `physics-loop/a2-bridge-identification-20260726`
Commits: `344e2a600c` (science), `3a35b608d2` (receipt + gate)
Runner: 8 PASS / 0 FAIL, cold-run, PIN MATCH. Step 11: clean.
Cluster-cap evaluator: **BACKLOG**. Objections accepted.

## Error 1 — the no-go was invalid (mine)

I claimed A2 carries an energy origin that is unobservable in the matter
dynamics into the observable force range. The evaluator:

> "the invariant resolvent quantity is `H - E`: an energy-origin change shifts
> both `mu` and `E`, leaving `mu - E` and hence `A` unchanged. Holding `E = 0`
> while shifting only `H` changes `G_0`; it makes the chosen origin part of the
> coupling rather than deriving a contradiction."

This is right. A consistent energy-origin shift moves `mu` **and** `E` together,
so `A = mu - 6 - E` is invariant and there is no pathology. I applied the shift
to one side of the identity and not the other, then read the resulting mismatch
as a contradiction. Failure class: an inconsistent transformation, which the
`Shown vs claimed` column would have caught had I asked "what exactly
transforms?" — I did not.

The fact that survives is the opposite of a no-go and is useful: **`A` is
invariant under consistent energy-origin shifts**, so `A` is genuine physical
content rather than a parametrization artifact.

## Error 2 — the central identification was wrong (mine)

I claimed "the bridge theorem is exactly derive `mu = 6`". But the root source
fixes `H = -Delta_lat` **before** stating A2, so `mu = 6` is part of the
supplied matter operator, not the gap. The gap is the **cross-sector**
identification of the field operator with the matter operator. Deriving `mu = 6`
establishes nothing about it.

## What survives, and it is worth keeping

The evaluator's own sharpening: the missing theorem must "select both `A = 0`
and `B = -1` for `L`". Inside the supplied range-1 covariant family
`L = A*I + B*Delta`, with `H = -Delta` supplied, A2 holds iff `(A, B) = (0, -1)`.
`B` is an overall normalization absorbable into `rho`. So:

> **Inside the supplied family, A2 is not a cross-sector identity at all. It is
> two conditions on `L` alone: masslessness (`A = 0`) and a normalization
> (`B = -1`). The cross-sector character evaporates because `H` is supplied and
> the family is two-dimensional.**

And therefore: **A2's `missing_bridge_theorem` and the `A/B` gap are the same
gap.** Two separately-tracked obligations are one obligation. The five-mechanism
`A/B` scoreboard in `HANDOFF.md` (scale primitive, covariance,
source-restriction, RG, positivity — all negative) applies directly to A2.

That is the honest deliverable and it is much smaller than what was submitted.

## Error 3 — two evidentiary defects shipped

- **R2 hardcoded a truth**: `a2_is_zero = (Fraction(6) - COORD - Fraction(0)) == 0`
  computes `6 - 6 - 0 == 0`. It cannot fail. Same class as the
  `pinv_annihilates_const = True` defect caught in 708 — caught there, shipped
  here.
- **R8's enumeration was domain-mismatched**: it enumerated 4-component sources
  while its `L = 2` torus has 8 sites, so "exhaustive over non-negative
  sources" was false.
- Ledger tagging: `N3` and `N8` carry `[satisfied]` on premises that are
  `[supplied]`.

## The step-11 finding, and the fix

Most damaging:

> "most importantly, the central route no-go has no ledger row or genuine
> falsifier."

The ledger had eight rows about the *components* and **no row for the headline
claim**. The linter enforces that rows are complete; it never checks that the
note's claims are *covered* by rows. So a note can pass with a complete ledger
that omits its own thesis.

Third layer added (`COVERAGE`): every claim-position sentence must be covered by
some ledger row, not merely the necessity-worded ones. Derived from this
failure, same as `TAG`/`HEADLINE` were derived from 708's.

## Trajectory, stated plainly

Eight rejections. The objections have moved steadily inward:

| cycles | objection class |
|---|---|
| 700–705 | inference from the arithmetic overreaches |
| 707 | cited theorem's hypothesis dropped |
| 708 | hypothesis recorded, then ignored by the headline |
| 709 | headline claim absent from the ledger; a transformation applied to one side only |

Each is narrower and caught one layer earlier. None of that is a derivation of
A2, and I have not produced one.

## Named successor

The one route the evaluator left standing is worth stating precisely, because
it reframes the whole lane:

`G_0 = H^{-1}` is the resolvent at zero energy. For a **quantum** propagator the
natural object is `e^{-iHt}`, not `H^{-1}`; `H^{-1}` is the Green's function of a
**Markov** generator — for `Q = Delta`, `-Delta^{-1}` is the expected occupation
time of the random walk. In `d >= 3` that walk is transient, so its Green's
function is finite and behaves as `1/r`; in `d = 2` it is recurrent and gives a
log, which is what the lane's own dimensional table reports.

**Conjecture to test:** the `1/r` law in this lane is the transience of the
random walk on `Z^3`, and A2 is the statement that the field's Green's function
is the walk's Green's function. If so, `A = 0` is automatic (a Markov generator
annihilates constants) and the gap moves to justifying a stochastic reading
against admission (b)'s `rho = |psi|^2`, which is quantum.

The evaluator has already pre-empted the cheap version of this: X1 "supplies the
unit-hopping Markov ansatz and an identification of record formation with
`Q = -H`, while still not deriving `L^{-1} = G_0`". So the successor must derive
the stochastic reading, not assume it. Do not open a cycle on this without that.
