# Cycle 703 BKSF vacuum gauge/ancilla addendum

**Date:** 2026-07-25

**Authority:** none

**Audit:** unset

**Dependencies:**
`CYCLE703_LOCAL_GAUSS_REFERENCE_ADVERSARIAL_NOTE_2026-07-25.md` and
`CYCLE703_LOCAL_GAUSS_HELD_PATCH_GRAMMAR_ADDENDUM_2026-07-25.md`

## Result

This addendum attacks autonomous genesis of the all-`B` BKSF vacuum by a
gauge/ancilla route distinct from the Cycle-703 even-operator grammar.  It
tests bounded face-ancilla controlled-loop preparation, coherent syndrome
correction, a translation-compatible bounded-radius linear correction rule,
and a subsystem interpretation of the three periodic Wilson characters.

The result is a layered partial closure:

- The all-`B` plus full-cycle stabilizer family is an exact one-state tableau
  after the Wilson character is fixed.  This closes with zero phase,
  Hermiticity, or commutator failures on the L and held 2x2 patches, open
  cube `L=2`, and periodic cubes `L=3,4,5`.
- Bounded face-controlled loop gates preserve every `B_v`, but stabilize
  `X_f L_f`, not the required edge-only `L_f`.  Every independent edge-loop
  projector has expectation zero and leakage `1/2`.  Measuring every face
  ancilla in `X` and postselecting `+` prepares the target, but its success
  probability is `2^{-rank(H)}` and therefore is not autonomous preparation.
- An exact coherent correction exists at every tested finite size.  For loop
  syndrome `s`, a computed `Z` correction `A_s` obeys

  ```text
  A_s P_s |0_Z> = P_+ |0_Z>.
  ```

  This is a positive state identity, not a local compiler: its maximum
  correction weight grows from `23` at open `L=2` through `117,241,413` at
  periodic `L=3,4,5`.
- A translation-linear correction kernel with 24 edge types and 18 syndrome
  types was tested through the exact equation

  ```text
  H R H = H
  ```

  on lawful loop syndromes.  Radius 1 closes only on the whole-torus `L=3`
  case and fails without refit at `L=4,5`; radius 2 closes only on the
  whole-torus `L=5` case and fails held `L=6`.  This falsifies the tested
  fixed-radius translation-linear architecture, not general local Clifford,
  nonlinear measurement-decoder, or recurrent local dynamics.
- The three periodic Wilson characters can be retained as inert typed gauge
  qubits.  Every local `A/B` generator commutes with them, so the correct
  domain and intertwining claim are

  ```text
  E_direct_sum : H_matter tensor C^8_gauge -> H_local_code
  U_physical E_direct_sum
      = E_direct_sum (U_matter tensor I_8).
  ```

  A matter-only encoder still requires a selected or prepared gauge vector.
  The eight-dimensional factor cannot be silently discarded.

There is no broad preparation no-go and no axiom pressure.  The dense exact
identity and Wilson direct-sum typing are constructive results.  Bounded
nonlinear and recurrent correction routes remain live in this subroute; the
separate Cycle-703 echo/ack addendum subsequently constructs one such
radius-one recurrent correction with returned work and a factorized retained
record.

## Exact vacuum tableaus and preparation controls

| Fixture | BKSF edge qubits | `rank(B)` | local-loop rank | Wilson rank added | full cycle rank | fixed tableau rank | max dense `Z` weight |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| L patch | 304 | 111 | 193 | 0 | 193 | 304 | 6 |
| held 2x2 patch | 380 | 139 | 241 | 0 | 241 | 380 | 6 |
| open cube `L=2` | 168 | 55 | 113 | 0 | 113 | 168 | 23 |
| periodic cube `L=3` | 648 | 188 | 457 | 3 | 460 | 648 | 117 |
| periodic cube `L=4` | 1536 | 447 | 1086 | 3 | 1089 | 1536 | 241 |
| periodic cube `L=5` | 3000 | 874 | 2123 | 3 | 2126 | 3000 | 413 |

For every fixture:

- `rank(B)=|V|-1` and the target loop basis reaches the full graph cycle
  rank `|E|-|V|+1`;
- the combined stabilizer rank is exactly `|E|`, with zero inconsistent
  phases, zero non-Hermitian rows, and zero pairwise commutator failures;
- every displayed local loop has edge-only expectation zero after the
  face-controlled circuit and projector leakage `1/2`;
- the postselection log-probability is minus the independent local-loop rank,
  or minus the full cycle rank when the Wilson sector is also fixed;
- the dense right inverse has one correction for every independent cycle,
  with zero syndrome failures;
- deleting one correction column produces one syndrome failure; and
- deleting one independent loop row lowers the target rank by one.

The maximum local-loop Pauli weight is `36`.  Greedy conflict coloring uses
`11,11,15,27,30,29` colors on the six displayed fixtures.  These are finite
bounded-support circuit schedules, but the edge-only target is obtained from
them only by exponentially unlikely postselection or by the separate
coherent correction.

## Translation-linear held-size test

For translation radius `r`, the candidate right inverse uses coefficients
indexed only by output-edge type, syndrome-loop type, and a displacement in
`[-r,r]^3`.  It has `24 * 18 * (2r+1)^3` binary variables, independent of
volume.  The exact consistency results are:

| periodic size | radius | variables | equations reached | rank | result | first failed `(check type,input edge)` |
| ---: | ---: | ---: | ---: | ---: | --- | --- |
| 3 | 0 | 432 | 850 | 360 | fail | `(15,487)` |
| 3 | 1 | 11664 | 11664 | 7739 | consistent | none |
| 4 | 1 | 11664 | 14140 | 8356 | fail | `(15,1363)` |
| 5 | 1 | 11664 | 14346 | 8372 | fail | `(15,2425)` |
| 5 | 2 | 54000 | 54000 | 36061 | consistent | none |
| held 6 | 2 | 54000 | 58506 | 36960 | fail | `(15,4927)` |

The two consistent cases have radius equal to the centered torus diameter;
they are finite dense diagnostics, not held evidence for a size-independent
local kernel.  The `L=6,r=2` row is evaluated with the same type/displacement
ansatz and no fitted table exported from `L=5`.

## Wilson direct-sum and covariance audit

| periodic size | BKSF edge qubits | local-loop+`D` rank | plus three Wilsons | direct-sum exponent | fixed-sector exponent |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 648 | 483 | 486 | 165 = `6N+3` | 162 = `6N` |
| 4 | 1536 | 1149 | 1152 | 387 = `6N+3` | 384 = `6N` |

On both sizes, every actual BKSF `A` edge generator and every `B` vertex
generator commutes with all three Wilsons: zero failures.  No one-site
Pauli both preserves the local loop+`D` code and changes a Wilson character.
Deleting one Wilson lowers the rank by one.  Thus the local even update acts
sector-identically as `U_matter tensor I_8`; it neither erases nor chooses the
gauge input.

On periodic `L=3`, the 24 proper-cubic frames induce exactly the six
permutations of the three Wilson basis characters:

```text
(1,2,4) (1,4,2) (2,1,4) (2,4,1) (4,1,2) (4,2,1).
```

Coordinate failures, reconstructed-Pauli phase failures, and all 576 ordered
composition failures are zero.  The `+++` character is invariant.  This is
an exact covariance result for the Wilson gauge factor; transformed physical
common-E covariance remains a separate obligation.

## Supplied and derived structure

Supplied:

- the Cycle-703 seven-mode local-`D` BKSF graph, its local incidence gauge,
  and the L/2x2 held patch grammar;
- product edge state `|0_Z>`, blank face/syndrome ancillas, and availability
  of controlled local Pauli loops for the preparation attack;
- fixed periodic boundary conditions for the torus tests;
- translation-linearity and a fixed displacement radius for the linear
  decoder subroute; and
- either an explicit three-qubit gauge input or, for a matter-only encoder,
  a separately selected Wilson vector.

Derived and executed here:

- the full all-`B`/cycle stabilizer tableaus, phases, ranks, and deletion
  controls on the six fixtures;
- the exact dense coherent identity and active right-inverse columns;
- the radius-0/1/2 translation-linear consistency systems and held `L=6`
  contradiction;
- the `6N+3 = 6N + 3` direct-sum dimension and sector-identical action; and
- the exact 24/576 proper-cubic representation on Wilson characters.

Not supplied or derived:

- a fixed-radius autonomous circuit preparing the all-`B` edge vacuum from
  product ancillas;
- within this runner, a nonlinear local measurement decoder or recurrent
  radius-one controller with bounded returned work (the separate
  `CYCLE703_REVERSIBLE_ECHO_ACK_CONTROLLER_NOTE_2026-07-25.md` constructs one);
- an arbitrary-matter-state BKSF edge-qubit common E and direct
  `U_physical E - E U_matter` residual; or
- a matter-only selection of one Wilson character without an admitted gauge
  vector or preparation mechanism.

## No-Go Discipline Gate

**Gate result: FAIL for a broad no-go.  Retain only the route-specific
negative and the constructive partial closures.**

- **N1 — Alternative-route enumeration.** Attempted: bounded face-ancilla
  graph state, face-`X` postselection, dense coherent correction,
  translation-linear fixed-radius correction, and Wilson subsystem/direct
  sum.  The dense route is exact and the subsystem route closes Wilson typing.
  Nonlinear local measurement decoding and recurrent radius-one correction
  remain untested inside this runner; the independent echo/ack companion now
  provides a positive construction rather than support for this negative.
- **N2 — Wall independence.** Loop disentangling and correction locality are
  one coupled preparation wall.  Wilson selection is separate and is
  conditionally retired by taking a typed gauge input.  Arbitrary-state
  physical-site common E is separate again.
- **N3 — Hidden-wall scan.** Product `|0_Z>`, blank ancillas, controlled-Pauli
  availability, translation-linearity, fixed radius, periodic boundaries,
  and the fixed/typed Wilson choice are explicit assumptions.
- **N4 — Residual matching.** The Wilson rank witness is used only for Wilson
  dimension and covariance.  It is not credited as a face-decoder no-go.
  Dense right-inverse closure is credited as a finite state identity, not as
  locality.
- **N5 — Resolution and rhetoric.** The negative applies only to the tested
  face-ancilla circuit and translation-linear fixed-radius kernel.  It does
  not claim failure of all Clifford circuits, nonlinear decoders, recurrent
  dynamics, or local preparation mechanisms.
- **N6 — Partial closure path.** The dense identity supplies the exact target
  action.  A nonlinear cellular decoder with retained syndrome gauge qubits,
  or a recurrent local implementation of that correction followed by
  ancilla cleanup, is a concrete next construction.
- **N7 — Steelman.** A radius-one recurrent dynamics run for a growing number
  of recurrences can propagate syndrome information without a precomputed
  dense feedforward table.  Its acceptance test is an explicit local unitary,
  exact target stabilization, and returned ancillas on training and held
  sizes.
- **N8 — Cross-cycle echo.** Cycle-232's uniform-reference failure was retired
  by local `D` in Cycle 703.  The present route-specific preparation failures
  cannot be echoed into a constitutional obstruction.

The gate therefore bars an impossibility, minimum-content, or axiom-pressure
claim.  This is unfinished implementation with an exact global diagnostic.

## Reproduction

```bash
PYTHONPATH=scripts python3 -u \
  scripts/frontier_cycle703_bksf_vacuum_gauge_ancilla_addendum_2026_07_25.py
```

Expected terminal:

```text
DENSE_COHERENT_VACUUM_AND_WILSON_GAUGE_POSITIVE_FIXED_RADIUS_LOCAL_PREP_OPEN
```

The retained run passed 8 checks, failed 0, used 232.25 MB peak RSS, and took
10.092988916905597 seconds.  Certificate SHA-256:
`f3df92574675cfeebc8362dbe10d1589d59c9e73cd177fef190a79801524650f`.
