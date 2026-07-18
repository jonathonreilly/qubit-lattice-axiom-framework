# Physical finite menu-normalization checker — Cycle 388 (2026-07-18)

Status: **positive finite exact-integer construction; authority: none; audit:
unset.**  This cycle does not alter axioms, foundation, Qualification,
primitives, registries, policies, queues, or audit status.  It makes no
minimum-content, no-go, obstruction, constitutional, or axiom claim.  There
is no axiom pressure.

Runner:
`scripts/physical_finite_menu_normalization_checker_cycle388_2026_07_18.py`

## Bounded reversible finite menu-normalization checker at code-space level

Cycle 388 constructs a fixed reversible integer reference update for the nine
effect classes of the current-campaign Cycle-386 registry.  Every grade numerator is
stored in one of nine six-M2 grade registers at exact denominator 48.  A
program-controlled eight-M2 modular accumulator adds the numerators appearing
in one Cycle-382 coarse menu.  A one-M2 equality gate flips exactly when the
sum is 48 and the Cycle-384 program-registration bit is set.

Two distinct strictly positive tables pass every menu: the same fixed checker
accepts both for all six programs.  The coarse-CP process tags remain
unchanged.  This is
an explicit finite underdetermination witness for these finite normalization
constraints: more than one supplied grade table is admitted by the same
code-space arithmetic reference.

It is not probability, does not select a grade table, and supplies no Born
law or actuality or frequency inference.

## Exact class multiplicities and denominator

Cycle 386 locally rederives the 14 lawful `(program, coarse outcome)` rows as
9 effect classes and 11 coarse-CP classes.  Grouping its effect classes by
the six Cycle-382 programs gives

```text
program 0: (0, 1)
program 1: (0, 1)
program 2: (2, 3, 4)
program 3: (5, 5)
program 4: (6, 7)
program 5: (8, 8, 8)
```

The corresponding process-class rows are

```text
program 0: (0, 1)
program 1: (0, 1)
program 2: (2, 3, 4)
program 3: (5, 5)
program 4: (6, 7)
program 5: (8, 9, 10)
```

For numerator (n_e\in\{1,\ldots,47\}) assigned to effect class (e), exact
normalization at denominator 48 is the finite integer system

\[
\begin{aligned}
 n_0+n_1&=48,\\
 n_2+n_3+n_4&=48,\\
 2n_5&=48,\\
 n_6+n_7&=48,\\
 3n_8&=48.
\end{aligned}
\]

The repeated program-0/program-1 row is checked twice because both physical
program labels remain present.  Denominator 48 represents halves and thirds
exactly and leaves every register within six M2.  The denominator remains
supplied as a fixed arithmetic scale; it is not derived as a universal
normalization unit.

## Two strictly positive witnesses

The runner independently constructs and verifies:

```text
table A = (12, 36,  8, 16, 24, 24, 20, 28, 16)
table B = (18, 30, 12, 14, 22, 24,  7, 41, 16)
```

All 18 entries lie strictly between 0 and 48.  In both tables the six menu
sums are exactly

```text
(48, 48, 48, 48, 48, 48).
```

The tables differ on classes 0, 1, 2, 3, 4, 6, and 7.  They agree where the
finite repeated-class equations fix (n_5=24) and (n_8=16).  Their
existence is a positive finite construction, not a claim about every menu
family or every denominator.

## Reversible arithmetic

One checker state contains:

| Register | M2 |
|---|---:|
| program | 3 |
| Cycle-384 registration bit | 1 |
| nine exact numerators | 54 |
| three padded coarse-CP process tags | 12 |
| modular accumulator | 8 |
| equality check | 1 |
| reference/state width | 79 |

For program (p), let (S_p(n)) be the integer sum of the numerator table
over the supplied effect-class row above.  The fixed modular-adder layer is

\[
 U_+|p,r,n,j,a,b\rangle
 =|p,r,n,j,a+S_p(n)\pmod {256},b\rangle.
\]

The fixed equality layer is

\[
 U_=|p,r,n,j,a,b\rangle
 =|p,r,n,j,a,b\mathbin{\mathrm{xor}}[r=1\land a=48]\rangle.
\]

The 79-M2 reference/state update is `G_388 = U_check` composed after `U_add`.
Its exact inverse applies `U_check` and then subtracts (S_p(n)) modulo 256.  The runner
tests 144 states spanning both tables, all programs, accumulator values
including 0 and 255, and both check-bit values.  It reports:

- inverse failures: 0;
- equality-gate involution failures: 0; and
- modular-range failures: 0.

The same code-space update function receives table A or table B as a prepared
register state.  There is no table-specific branch or separately fitted checker.

## Exact code-space E/G and process-tag preservation

Let (E_{\rm in}) encode either admitted nine-register table, one of the six
program labels, the Cycle-384 registration value 1, the exact three-slot
process row, and blank accumulator/check ancillas.  Let (G_{\rm coarse})
write exact sum 48 and check value 1 while preserving every other field.  The
runner checks

\[
 E_{\rm out}G_{\rm coarse}=G_{388}E_{\rm in}
\]

on all 12 table/program states with exact E/G failures 0.  Applying the
explicit inverse recovers all 12 source states exactly.

The process tags are spectator registers in both reversible layers.  Their
carry residual is exactly zero.  In particular, the cubic-axis menu uses one
effect class three times and therefore presents numerator row `(16,16,16)` in
both grade tables, while retaining distinct coarse-CP tags `(8,9,10)`.  Grade
normalization therefore does not erase the Cycle-386 same-effect process
separator.

The process tags are validated against the selected program before admission;
padding value 15 is used only for absent third outcomes of two-outcome menus.

## Deletion and lawful-domain controls

The fixed checker rejects the complete adversarial surface:

- all 18 one-entry `+1` attacks, one for every class in both tables;
- all 12 menu-term deletions, one for every program/table pair;
- all 12 modular-adder deletions;
- all 12 equality-layer deletions; and
- all 11 malformed-domain calls.

The domain calls cover a short grade table, numerator 0, numerator 48, wrong
denominator 47, invalid program, nonregistered program state, accumulator
overflow, invalid check bit, altered coarse-CP tag, missing menu row, and
effect-class overflow.  Thus strict positivity, fixed denominator, local
program registration, process identity, and arithmetic widths are each
tested separately from normalization itself.

## Scalar matter-code extension and envelope inventory

The arithmetic and class/process registers are treated as scalar local
metadata and as the identity on the physical matter code.  The reported
matter-code E/G residual is the zero code-space mismatch scalar-extended by
each Cycle-317 two-ray encoding.  It is 0 at L=3 and held L=6.  This preserves
the accepted matter embedding interface; it is not a primitive-gate
compilation of the integer arithmetic.

The combined state envelope containing the inherited physical apparatus,
registration M2, nine grade registers, three process tags, accumulator, and
check M2 has the inventory:

- 138-M2 envelope/support inventory; and
- 105 M2 per cell as an inherited-accounting envelope figure.

Neither number is a completed physical arithmetic compiler or a maximum
primitive support certificate.  This is not a completed physical arithmetic
compiler.  In particular:

- physical arithmetic gate compiler: none;
- nearest-neighbor decomposition: none;
- maximum primitive support M2: none; and
- primitive-boundary leakage audit: none.

At both sizes:

- matter-code leakage is (2.6803154833\times10^{-16});
- role-constraint residual is 0;
- actual-contact intertwiner residual is 0; and
- port, local-check, and Wilson failures are 0.

The scalar normalization registers commute with physical frame action.  The
inherited carrier passes all 24 proper-cubic frames with zero branch failure
and zero carrier residual.  The one-particle mass relative residual remains
(2.2204460493\times10^{-16}).  No global parity service or preferred spatial
ordering is introduced.

## Provenance and novelty boundary

- The landed Cycle-317/321/323 substrate supplies the physical matter code,
  contact, mass fixture, effect/CP distinctions, fixed carrier, bounded
  physical realization, and covariance controls.
- The current-campaign Cycle-382 compiler supplies the fixed six-program
  coarse menus.
- The current-campaign Cycle-383 bridge supplies the exact effect versus
  coarse-CP distinction discipline used downstream.
- The current-campaign Cycle-384 bridge supplies the local program-registration
  bit.
- The current-campaign Cycle-386 registry supplies the nine effect classes,
  eleven coarse-CP classes, class multiplicities, and retained process tags.

Cycle 388 adds the exact denominator-48 numerator representation, two
strictly positive table states, one fixed modular-adder/equality code-space
reference update, and deletion/domain controls.  It does not add a law
selecting either table, promote finite normalization to a universal grade
law, or compile the reference update into nearest-neighbor physical gates.

## Supplied inventory and semantic boundary

The following remain explicit inputs:

- grade-table selection remains supplied;
- denominator remains supplied;
- arithmetic ancillas remain supplied: blank eight-M2 accumulator and
  one-M2 check register;
- preparation of all nine six-M2 grade registers remains supplied;
- preparation and binding of the program-registration and coarse-CP process
  tags remain supplied;
- admission and schedule remain supplied for the grade tables, class/menu
  map, modular-add layer, and equality layer;
- program and coarse-menu selection remain supplied; and
- continuous coefficient/ray synthesis for the underlying apparatus remains
  supplied.

The physical arithmetic gate compiler, nearest-neighbor decomposition,
maximum primitive support M2, and primitive-boundary leakage audit are all
`None`.  Therefore the 138-M2 number is an envelope inventory, not a physical
arithmetic implementation certificate.

This finite algebraic normalization is not probability.  The grades are not
outcome chances, and there is no Born law.  Passing the check is not
occurrence, actuality, a Record, a sampler, or a frequency statement.  There
is no actuality or frequency inference.

## Dependency-ledger effect

- `C_ref`: unchanged.
- `C_num`: narrowed only at the finite apparatus interface: exact positive
  denominator-48 grade tables and a reversible normalization checker now
  exist.  The explicit two-table witness leaves grade-table selection,
  denominator selection, admission, and numerical-law genesis supplied.
- `C_wrap`: unchanged; no occurrence, actuality, Record, permanence, or
  history selection is introduced.
- `C_int`: preserved, not advanced; mass and contact remain green.
- `C_local`: narrowed only for the fixed Cycle-386 finite logical/code-space
  arithmetic and scalar embedding interface: the reversible reference update
  has exact E/G and inverse checks, attacks, held size, and 24-frame matter
  controls.  Nearest-neighbor arithmetic-gate decomposition, primitive
  support, primitive-boundary leakage, general table/class genesis, and a law
  selecting one admitted table remain outside this result.
- `C_source`: unchanged.

Cold-run command:

```text
python3 scripts/physical_finite_menu_normalization_checker_cycle388_2026_07_18.py
```

Expected summary: `SUMMARY PASS=6 FAIL=0`.
