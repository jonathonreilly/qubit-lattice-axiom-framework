# Route A actual common-E composition — 2026-07-25

Authority: none

Audit: unset

## Question and scope

This probe replaces the earlier sum of eleven isolated pair-fixture residuals
by an actually executed common encoding and ordered physical update.  It asks
whether the landed endpoint-carrier ROM, with its existing bounded port-plus-q
controls, implements the Cycle-230 CAR stream on the complete total-`n<=2`
sector of the twelve-cell overlapping-star fixture.

The executable constructs the sparse `59,941 x 2,629` common encoding `E`,
constructs each `59,941 x 59,941` sparse owner operator explicitly, applies all
eleven owners in the declared order, updates the reduced shared q/chart and
carrier rows, and finally applies contact as an actual physical row diagonal.
It starts from `E C` using the independently executed exact physical-coin
equality `C_physical E = E C`; hence the post-coin seam residual is
`(U_seam E - E G_seam) C`, with unchanged Frobenius and operator norms.

No Gram identity, rectangular `P/A`, dense `E U E^dagger` completion, runtime
mode-order query, or host-side branch selector is used as the intertwiner.
Lexicographic cell order is offline sparse-row and logical-basis bookkeeping;
the missing parity implied by that bookkeeping is deliberately not supplied
to the physical ROM.

## First correction: the landed Givens word had a hidden phase

The 24 two-level rotations per cell take every one-particle carrier to its
canonical row with phase `-i`.  The earlier local matrix control also included
a final one-level phase, but that phase was absent from the advertised
24-factor physical ROM.  It does not always cancel: a seam can turn a
doubly-occupied endpoint into two singly-occupied endpoints.

The executable now coefficient-tags the canonical occupation row by the exact
target/source decoder-phase ratio.  After this correction every 79-column
two-cell pair ROM satisfies its intended endpoint-local tensor FSWAP at both
L=5 and held L=6, with maximum residual about `2.71e-15`.  The owner word
remains 97 scheduled factors: 24 left unprepare, 24 right unprepare, one
corrected occupation row, then the two reversed adjoint words.

This correction is local and constructive.  It does not fix the global CAR
sign below.

## Actual common-E result

The physical operators are unitary to randomized residuals near `1.5e-16`,
have no missing target histories, and reproduce the endpoint-local tensor
update on `E` below `1.4e-14` after the full coin/seam/contact composition.
They do **not** reproduce the target CAR update:

- `||U_physical E - E G_target||_F = 30.983866769659...` at L=5 and held L=6;
- raw maximum residual is `0.8740010519307574` after coin composition and the
  operator-norm residual is `2`;
- code leakage is about `2.68e-14`, so this is an in-code sign error, not a
  stale chart, carrier loss, or off-code escape;
- contact neither creates nor removes the defect;
- the one-particle mass fixture is preserved, because the missing sign needs a
  spectator particle.

Before the coin, the exact residual operator is a diagonal signed-permutation
cocycle

`D_e = G_CAR(e)^dagger G_endpoint(e)`.

On the declared `n<=2` sector it is `-1` exactly when one seam endpoint is
occupied and the occupation parity strictly between the two offline mode slots
is odd.  The eleven owner counts of negative input columns are

`60, 36, 24, 24, 12, 12, 36, 24, 24, 12, 12`.

After all eleven owners the missing signed permutation has exactly 240
negative diagonal columns and zero off-diagonal entries.  This is the exact
operator missing from the supplied endpoint ROM.  Supplying it from the
offline linear mode order would be the forbidden parity string/order service,
so that is not accepted as a repair.

## Bounded coefficient-tag audit

The existing physical control alphabet was tested directly: bounded source
and target observations of the owner port shell and q blocks, together with
the fixed transition Pauli.  Seven owners have two observation rows each for
which both required CAR signs occur.  Thus one physical coefficient tag cannot
satisfy every history in those rows.

The per-owner minimum wrong logical columns for any one coefficient choice in
each existing observation row are

`40, 20, 10, 10, 0, 0, 20, 10, 10, 0, 0`.

This is a precise failure of the landed Route-A observation alphabet.  It is
not an impossibility claim against a different bounded gauge or auxiliary
encoding, and it is not shared-substrate or axiom pressure.

## Covariance, translation, and work boundary

The target CAR update passes all 24 proper-cubic frames and the 576 frame
products.  The endpoint-local action induced by the actually executed ROM
fails 23 of 24 proper-cubic frame covariance comparisons, with maximum
residual `2`, exactly as expected when its missing parity cocycle is not
transported.  The frame representation itself has zero group failures.

The physical carrier/chart observations and landed coefficients were replayed
without refit at every torus translation: 125 translations / 1,375 owner
fixtures at L=5 and 216 / 2,376 at held L=6.  They have zero chart ambiguity,
zero invalid qutrit words, zero duplicate-chart failures, and zero coefficient
mismatches.  This shows the local physical ingredients translate; it does not
turn the failed finite program into a recurrent covariant law.

The invariant source/target membership predicate remains true at both ends of
each two-level row, so its comparator work is recomputed to blank.  No
persistent pair label is used.  The executed common-row operator includes the
resulting carrier and shared q/chart target row; explicit comparator bits are
factorized out only after their audited exact return.

## Disposition

Route A's strongest retained result is an exact, bounded physical realization
of every endpoint-local carrier ROM plus contact on the common code space,
including the repaired decoder phase.  It is not a physical compiler for the
coarse CAR stream.  The exact residual is the unsupplied graded parity cocycle,
and the existing bounded observations do not distinguish all of its sign
classes.

This is route-specific negative evidence only.  Authority remains none, audit
remains unset, no axiom language is proposed, and no recurrent volume law is
claimed.

## Reproduction

Run with the Route-B/Route-C dependency scripts on `PYTHONPATH`:

```text
PYTHONPATH=<review-scripts> python3 \
  scripts/frontier_common_e_ordered_physical_rom_composition_2026_07_25.py
```

The terminal marker is
`ROUTE_A_ACTUAL_COMMON_E_COMPOSITION_FALSIFIED_BY_UNSUPPLIED_CAR_PARITY_COCYCLE`.
