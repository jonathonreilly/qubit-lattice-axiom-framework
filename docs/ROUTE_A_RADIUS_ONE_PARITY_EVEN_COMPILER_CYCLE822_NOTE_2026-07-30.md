# Cycle 822 Route A: superseded radius-one parity-even compiler diagnostic

> **Superseded framework typing.** This first probe incorrectly treated every
> routed/token coordinate as charged under product-Z parity. Cycle 821 protects
> matter plus carrier only; companion, syndrome, token, and neutral-work modes
> are neutral. Its 328-factor physical claim is therefore demoted. The exact
> failure census and corrected fixed-atlas construction are in
> [`ROUTE_A_FIXED_TYPE_ATLAS_CORRECTION_CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-30.md`](ROUTE_A_FIXED_TYPE_ATLAS_CORRECTION_CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-30.md).

**Type:** meta

**Authority:** none

**Audit:** unset

**Baseline:** `c04e711ea660d655eff907a40f96fd345259b53f`

**Status:** superseded-invalid historical route; not a live theorem or
framework compiler claim

**Declared dependencies:**
[Cycle 720](RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md),
[Cycle 789](THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md),
[Cycle 794](LITERAL_THREE_BANK_PREFIX_RECURRENT_G_ACTUAL_SHEAR_CYCLE794_BOUNDED_THEOREM_NOTE_2026-07-30.md),
and [Cycle 821](LOCAL_PARITY_EXCHANGE_CARRIER_RECURRENT_BELL_CYCLE821_BOUNDED_THEOREM_NOTE_2026-07-30.md).

## Rejected trial construction

The runner
`scripts/frontier_cycle822_route_a_radius_one_parity_even_compiler_2026_07_30.py`
records an internally consistent all-coordinates-charged product-Z experiment
for two target surfaces:

1. every Cycle-821 controlled two-target pair atom, including all
   `XX`, `XY`, `YX`, and `YY` targets and either choice of pivot; and
2. every landed recurrent Cycle-720 seam factor
   `exp(-i pi P/4)`, including the factors of support 17 M2 and physical
   Manhattan diameter 24.

There is no semantic multi-site rotation in either output word. The elementary
palette is nearest-neighbour FSWAP, nearest-neighbour CZ, the Cycle-821
two-mode even rotation `U` or `U_dagger`, a radius-one three-mode Fredkin star,
and a one-mode diagonal phase. Every route and the dual-rail token are returned.

This is not a Cycle-821 physical compiler: its grading is wrong for companion,
syndrome, token, and neutral-work coordinates. The algebra and controls below
are retained only to make the rejected route reproducible. The corrected
fixed-type-atlas note is the sole positive Route-A theorem.

## Exact tensor-frame route hop

The landed Cycle-821 targets use a fixed tensor-product Pauli frame. Moving a
label with a bare fermionic swap would change that frame by the graded
occupation sign. Each routed tensor-label transposition is therefore factored
as

\[
T_{j,j+1}=\operatorname{CZ}_{j,j+1}\operatorname{FSWAP}_{j,j+1}
=\operatorname{SWAP}_{j,j+1}.
\]

The circuit applies FSWAP and then CZ chronologically, so its state operator is
the product displayed above. Both factors separately commute with the local
two-mode parity. A forward sequence of these hops brings a named operand to
the local gate; the identical hops in reverse order restore every label and
spectator. The compiler checks the active operands at the gate and checks the
complete label permutation after every macro.

This factorization is not cosmetic. Replacing the FSWAP factor by ordinary
SWAP while retaining the sign-firewall CZ leaves a bare FSWAP route and gives
minimum dense residual `5.65685424949238`. Deleting one return hop leaves two
label mismatches and has dense residual `5.656854249492381`.

## Controlled two-target atom

For an even target `A=A_first A_second`, choose either target as pivot. In the
pivot-first notation Cycle 821 supplies

\[
K=\begin{cases}
Y_{\rm first}A_{\rm second},&A_{\rm first}=X,\\
-X_{\rm first}A_{\rm second},&A_{\rm first}=Y,
\end{cases}
\qquad
U=\exp(-i\pi K/4),
\]

with `U Z_first U_dagger=A`. The literal word is:

1. returned-route the pivot beside its partner, apply `U_dagger`, and return;
2. returned-route the control beside the pivot, apply CZ, and return; and
3. returned-route the pivot beside its partner, apply `U`, and return.

Thus the chronological circuit has operator `U CZ U_dagger`, exactly the
controlled-`A` atom. Across all eight letter/pivot cases the maximum dense
matrix residual is `1.2624328845283428e-15`. The maximum elementary and
Cycle-821 `U Z U_dagger` conjugacy residual is
`4.463374267214424e-16`; the maximum elementary and cumulative-prefix
commutators with extended product-Z parity are both zero.

## Dual-rail seam accumulator

Write a Hermitian seam row in the repository encoding as
`P=i^phase X^x Z^z`. Pair the even number of `X/Y` sites. For every ordered pair
use the Cycle-821 diagonalizer above, so a pivot Z is mapped to the ordinary
letter-pair matrix. All remaining supported sites are Z singletons. If
`n_Y=(x&z).bit_count()`, the repository row differs from the ordinary letter
product by

\[
s=i^{\mathrm{phase}-n_Y}\in\{+1,-1\}.
\]

This sign is essential for the phase-zero `XYZXY` seam family.

Supply token rails `(a,b)` in the one-excitation state `|10>`. After the pair
`U_dagger` macros, returned-route each pivot and Z singleton to a fixed local
star and apply Fredkin controlled by that data mode. The token is swapped once
for every occupied control. Consequently `Z_a=-Q`, where `Q` is the product of
the diagonalized control Zs. Apply the one-mode phase

\[
\exp(+i s\pi Z_a/4)=\exp(-i s\pi Q/4),
\]

reverse all Fredkins, and apply the returned `U` macros in reverse pair order.
The result is exactly `exp(-i pi P/4)`, and the token returns to `|10>`.

Fredkins with different controls commute on the token because each contributes
one application of the same rail swap. Both forward and reverse control orders
are executed. Both choices of pivot in every X/Y pair are also executed.

## Rejected product-Z parity calculation

The rejected experiment defines a trial product Z on every data, token, and
route-workspace M2. This trial observable is not the landed Cycle-821
`P_ext`. Within that rejected grading each elementary factor commutes with its
support parity:

- FSWAP and Fredkin preserve occupation number;
- CZ and the token phase are diagonal;
- the Cycle-821 `U` and `U_dagger` have even two-mode generator `K`.

Tensoring the support identity proves commutation with that trial product-Z
observable. The runner's zero prefix residuals therefore characterize the
rejected model only; they do not certify Cycle-821 parity. The correction
runner replays these words under the actual fixed grading and finds 10,112
elementary failures and 1,445 charged/neutral coordinate conflicts.

Every two-mode factor acts on nearest neighbours. Fredkin acts on the center
and its two opposite token neighbours, a three-site support of diameter two
contained in the radius-one ball about the center. The phase is one-site.
There are zero radius-one failures and zero remaining semantic multi-site
rotation primitives.

## Executed surfaces and residuals

The literal held shapes are `(2,1,1)`, `(3,1,1)`, `(3,2,2)`, and `(5,3,2)`.
They contain 328 landed seam factors. Translation reduces them to seven
operator templates: one `Z` template and the two phase-distinct families at
each of weights 5, 11, and 17. For every template, every computational-basis
operator column is executed for both pivot choices and both accumulator
orders. This is an exhaustive sparse-column representation of the full dense
operator, not random-state sampling.

The maximum seam operator residual is
`3.1401849173675503e-16`. The maximum support is 17 M2, maximum source support
diameter is 24, maximum emitted word is 3,907 elementary primitives, and
maximum one-way route length is 44 hops. Elementary parity residual, prefix
parity failures, radius-one failures, route-operand failures, route-return
failures, and semantic multi-site rotations are all zero.

The dirty opposite-rail token mutation has minimum seam residual
`1.4142135623730947`; on the independent four-control dense accumulator its
residual is `5.65685424949238`. The correct accumulator and both control orders
have dense isometry residual zero.

## Inputs / diagnostic outputs / open repair

### Supplied

- the landed Cycle-720 recurrent seam rows and placement;
- the Cycle-789/794 fixed chart, registers, route convention, and factor order;
- the Cycle-821 even-pair diagonalizer and extended-parity domain;
- two clean dual-rail token M2 in `|10>` for a serialized seam factor;
- route-workspace M2, fixed route program, and program occurrence.

### Diagnostic outputs inside the rejected grading

- literal returned radius-one factor words for every Cycle-821 controlled pair;
- literal returned radius-one factor words for all held recurrent seam rows;
- exact clean-token return and order/pivot independence;
- elementary and cumulative-prefix trial product-Z commutation, explicitly
  not landed `P_ext` commutation;
- active wrong-SWAP, deleted-return, and dirty-token mutations.

### Open

- genesis, local enforcement, and renewal of token and route-workspace modes;
- autonomous occurrence or translation-invariant enforcement of the program;
- a two-body-only decomposition of the allowed radius-one Fredkin star;
- physical time/rate and the broader source, Record/Born, and prediction
  bridges.

The corrected atlas note owns the positive physical result. This historical
artifact makes no route-independent negative or no-go claim.
