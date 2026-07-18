# Physical Cycle-269 local contact intertwiner — 2026-07-17

Type: constructive encoded operator block

Status: exact Cycle-230 contact on the fixed-Wilson, reference-relative
localized identical-pair lift; larger coherent and full-Fock compilation open

Authority: none

Audit: unset

Constitutional effect: none

Runner:
`scripts/physical_cycle269_local_contact_intertwiner_2026_07_17.py`

## Result

The Cycle-230 contact has an exact bounded physical Cycle-269 representative
on the reference-relative localized pair code.

For every one of the six mapped matter occupations at a coarse cell, use

```text
n_v=(I-B_v)/2.
```

Compile the local contact as fifteen pair projectors:

```text
C_x(g) = product_(u<v in cell x) exp(i g n_u n_v)
       = exp(i g binom(N_x,2)),

g=0.37.
```

All `B_v` are pure `Z`, so the factors commute even where their physical face
supports overlap. No pair ordering or phase schedule is part of the law.

On the localized state lift, column zero has the source/carrier pair in two
adjacent modes of one cell and receives `e^{ig}`. Column one has the two
streamed occupations in distinct neighboring cells and receives one. Hence
the declared coarse contact is

```text
C_coarse = diag(e^{ig},1).
```

Each encoded stabilizer-state column is an exact common eigenstate of all
literal `B_v` projectors. The physical pair-polynomial therefore acts by the
same scalar diagonal on those two columns, with no column mixing. Therefore

```text
E C_coarse = C_physical E
```

exactly on every declared two-column code space. Here `C_physical` denotes
this restricted physical action on the reviewed reference-relative lift. The
restricted physical action is not a full-Hilbert-space contact matrix. The
runner does not assemble such a matrix. This is a contact-block intertwiner,
not an assembled contact-plus-stream update. Contact and stream do not commute
on this code, and their schedule remains explicit.

## Local physical gate and support

Each projector `n_u n_v` is a polynomial in `B_u`, `B_v`, and `B_u B_v`.
Across the physical Cycle-269 cellulation:

- a perpendicular direction pair has nine-face support;
- an opposite direction pair has ten-face support;
- the union of all fifteen pair gates at one cell has eighteen-face support;
- the gate uses no auxiliary port M2 directly; and
- the inherited allocation remains fifteen face plus six auxiliary port M2
  per coarse cell, or 21 M2/cell.

The eighteen-face neighborhood includes the cell’s internal triangular faces
and its shared outer faces. It is a constant radius-one neighborhood,
independent of `L`.

The runner explicitly constructs the complete diagonal spectrum of every
pair type on its `2^9`- or `2^10`-dimensional physical support. Each
`n_u n_v` has only eigenvalues zero and one, is idempotent, and gives an exact
unitary phase. Changing `g` to `-g` is the inverse. The g=0 deletion is exact
identity.

On the abstract local six-mode occupation basis, multiplying the fifteen
factors reproduces `exp(i g binom(N,2))` on all 64 states, not only on the
selected pair fixture. The Frobenius reconstruction residual is
`2.2562397986482602e-15`, with zero unitarity, `g=0`, and `N<=1` residuals at
the declared tolerance.

## Constraint leakage controls

The physical contact is a function only of the commuting mapped occupations.
The runner constructs every literal extended constraint
`B_v Z_port(v)`—not a proxy comparison to another occupation—and checks the
underlying pure-`Z` occupation family pairwise. It therefore verifies that the
contact:

- commutes with every inherited bounded local check;
- commutes with all three Wilsons;
- preserves every local auxiliary constraint `B_v Z_port(v)=+1`;
- preserves each complete `B_v` occupation pattern; and
- commutes with contact factors at overlapping neighboring cells.

These properties are checked at training `L=3,4,5` and held `L=6`. Pair
support remains `[9,10]`, full-cell support remains eighteen, the maximum
periodic owner-cell Chebyshev radius is one, and every literal-constraint,
local-check, Wilson, occupation-form, and pairwise-commutation failure count
is zero. The `15+6=21` M2/cell counts are computed from each built code.

The fixed +++ Wilson vacuum and the localized physical state lift are supplied
by the preceding reference-relative artifact. This contact result does not
prepare that vacuum.

## Exact encoded action, inverse, and deletion

For every ordered adjacent source/carrier description, the runner evaluates
each literal projector eigenvalue from whether the actual physical Pauli
representative commutes or anticommutes with `B_v`; decoded occupations are a
separate comparison, not the definition of the physical action. Because the
column is a simultaneous `B` eigenstate, the polynomial action is scalar. It
checks:

- input column phase exactly `e^{ig}`;
- separated output column phase exactly one;
- equality of literal physical and decoded phases, and hence zero mixing of
  either common-eigenstate column;
- exact unitarity and the `g -> -g` inverse;
- exact identity under g=0 deletion; and
- that the unique active literal factor is exactly the source/carrier pair,
  every other pair projector is inactive on the fixture, and deletion leaves
  residual `|e^{ig}-1| = 0.36789306705608243`.

The last control makes the physical pair gate load-bearing. Deleting an
unoccupied pair factor is not expected to change that particular fixture.

Contact and the two-column stream exchange have operator-commutator norm
`0.36789306705608243`, checked against `|e^{ig}-1|` rather than merely against
a nonzero threshold. This is a schedule distinction only. A compiler substep
is not physical time, the coupling is not a rate, and the wrapped phase is not
physical energy.

## Held size and lawful domain

The encoded contact is tested on all `24 L^3` ordered localized lifts:

| `L` | domain | localized contact intertwiners |
|---:|---|---:|
| 3 | training | 648 |
| 4 | training | 1,536 |
| 5 | training | 3,000 |
| 6 | held | 5,184 |

Held `L=6` was not used to select `g`, the occupation dictionary, pair
factorization, support limits, encoded diagonal, thresholds, or deletion
tests.

The lawful domain requires a finite real coupling, periodic `L>=3`, and one
valid adjacent even pair with matching auxiliary tags. This runner directly
rejects complex and nonfinite couplings, undersized tori, and coincident,
opposite, nonlocal, mistagged, and out-of-range pair fixtures.

## Proper-cubic and translation covariance

The fifteen unordered direction pairs are a complete permutation-invariant
set. Under each of all 24 proper-cubic frames, a cell maps to a cell, its six
`B` occupations permute, and the physical pair-projector family maps onto
itself. Using the preceding lift's reviewed reference-tableau repair, the
runner also transforms both actual physical columns, checks their common
relative scalar and port tags against the mapped target lift, and reevaluates
the literal projector action. The encoded input phase remains `e^{ig}` and the
separated output phase remains one.

The same descriptor and transformed-physical-column checks pass all L=3
translations. There is no selected direction pair, source direction,
coordinate origin, or contact-factor ordering.

## One-particle mass fixture

The supplied contact is identity for `N=0,1`. The runner repeats the imported
Cycle-219/Cycle-230 one-particle mass controls:

- rest mass equals analytic mass;
- curvature/dispersion mass matches the analytic value; and
- forced-response mass remains within its declared tolerance.

The imported values are analytic mass `0.4534056541748852`, rest mass
`0.4534056541748851`, dispersion mass `0.4534056690336209`, and forced-response
mass `0.45444242813733504`, under their inherited relative tolerances
`2e-12`, `4e-6`, and `0.007`.

Thus the one-particle mass fixture is preserved when contact is absent. This
is a coarse one-particle control: the fixed-even physical Cycle-269 state code
does not encode a lone odd one-particle state. No physical one-particle state
intertwiner is inferred from the imported mass equality.

## Identical-pair and reference-relative boundary

The encoded pair is the same identical-fermion ray under source/carrier role
reversal, up to the inherited minus sign. The contact depends only on total
occupation and does not create independent source and carrier species.

The result remains reference-relative to a supplied global fixed-Wilson
vacuum. It does not provide:

- bounded absolute preparation of that vacuum;
- a coherent position superposition or independent source-role encoder;
- the actual six-mode coin with coherent auxiliary-port routing;
- a larger contact/stream macrostep closed under the coin;
- a full-Fock compiler or rank-73 sea state; or
- a source law, gravity, physical time, Record, or probability semantics.

There is no full-Fock compiler, no broad impossibility claim, and no axiom
pressure. This result does not call the coupling physical energy, does not call
the contact phase a rate, and is not gravity.

## Supplied-structure inventory

The exact supplied-structure inventory is:

1. Cycle-230’s local contact form and `g=0.37`;
2. the Cycle-269 dictionary `n_v=(I-B_v)/2`;
3. the fixed +++ Wilson unique stabilizer vacuum;
4. the reference-relative two-column localized identical-pair lift;
5. six auxiliary port M2 per cell and constraints `B_v Z_port(v)=+1`;
6. the declared contact-only schedule position;
7. training `L=3,4,5`, held `L=6`, all-frame and translation tests, including
   the preceding lift's supplied reference-tableau repair; and
8. the imported Cycle-219 one-particle mass fixtures and tolerances.

Derived here are the fifteen-factor physical contact polynomial, exact
64-state reconstruction, bounded support, its restricted physical action on
the declared columns, the encoded contact intertwiner, inverse, deletion,
leakage, covariance, held-size result, and mass-preservation firewall. A
full-Hilbert-space contact matrix and a larger invariant code are not derived.

## Disposition

```text
physical fifteen-factor Cycle-230 contact:          PASS
exact encoded contact intertwiner:                  PASS
unitarity, inverse, g=0, and pair deletion:         PASS
constraint/local-check/Wilson preservation:         PASS
all frames/translations and held L=6:               PASS
coarse one-particle mass preservation:              PASS
independent source/carrier species:                 NOT CONSTRUCTED
absolute vacuum or coherent-position encoder:       OPEN
coin/port routing and full-Fock compiler:            OPEN
energy, rate, source, gravity, Record semantics:     NOT CLAIMED
```
