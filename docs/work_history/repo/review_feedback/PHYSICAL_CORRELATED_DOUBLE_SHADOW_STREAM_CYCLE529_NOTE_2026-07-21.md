# Physical correlated double-shadow stream — Cycle 529

Date: 2026-07-21  
Authority: none  
Audit: unset  
Constitutional effect: none

Companion runner:

`scripts/physical_correlated_double_shadow_stream_cycle529_2026_07_21.py`

## Result

Cycle 529 constructs the first exact **stateful correlated-shadow runtime**
for the complete Cycle-230 B matching.  It repairs every fermionic exchange
sign, not only a one-link action, and its auxiliary state is updated into the
lawful output shadow rather than returned independently link by link.

The construction is not yet a physical M2 compiler.  Its shadow constraints
and preparation are defined by the supplied site-major mode order, have
size-growing support, and fail fixed-chart proper-cubic code covariance in 23
of 24 frames.  The local runtime gate geometry is bounded and all-frame
covariant, but the declared code is not.  Thus the retained result is exact
algebraic/stateful B closure with an explicit charted-preparation wall, not a
solution to the campaign question and not a local-gauge no-go.

## Quadratic residual and correlated encoding

Let `P` be Cycle 230's involutive B permutation of the `M=6L^3` modes.  For
`i<j`, the intrinsic exterior action contributes the inversion coefficient

\[
 e_{ij}=[P(i)>P(j)],
\]

while the endpoint-FSWAP product contributes

\[
 \ell_{ij}=[P(i)=j].
\]

Define the exact residual matrix

\[
 A_{ij}=e_{ij}\oplus\ell_{ij}\quad(i<j),\qquad A_{ij}=0\quad(i\ge j).
\]

For an occupation word `n`, introduce two M2 shadow banks

\[
 a=An,\qquad b=APn
\]

over GF(2).  In the runner and frozen contract these appear literally as
`a=An` and `b=APn`.  The encoded basis state is

\[
 E_A|n\rangle=|n,a=An,b=APn\rangle.
\]

This uses six `a` M2 and six `b` M2 per coarse cell, in addition to Cycle
523's six occupation M2 and centre tag: 19 active M2 per cell.

## Exact stateful runtime update

The physical B candidate is the fixed three-layer circuit

1. apply `CZ(q_i,a_i)` for every mode;
2. apply the three-per-cell endpoint FSWAP matching `P`;
3. apply `SWAP(a_i,b_i)` for every mode.

On the code, the first layer supplies

\[
 (-1)^{\sum_i n_i a_i}
 =(-1)^{\sum_{i<j}A_{ij}n_in_j},
\]

which is exactly the exterior/endpoint residual coefficient by coefficient.
The matter becomes `Pn`.  The final bank swap gives

\[
 (a,b)\longmapsto(APn,An),
\]

which is exactly the encoding required for `Pn`, because `P^2=1`.  Therefore

\[
 G_{B,\mathrm{shadow}}E_A=E_A\Gamma(P)
\]

on every Fock sector as an algebraic identity.  The output is ready for the
next involutive B application; no host chooses or recomputes a bank at
runtime.

This is genuinely non-diagonal/stateful in the auxiliary sector: the banks
are swapped.  It is outside Cycle 528's product-prepared endpoint-diagonal
response class.

## Exact tests

The runner verifies all pair coefficients, zero constant/linear terms, and
therefore the full Fock identity.  It also performs direct state tests:

- complete vacuum, N=1, and N=2 censuses at L5 and held L6;
- two neighboring cells on their complete 4,096-state Fock space;
- straight and bent three-cell patches through total N=3, 988 states each,
  matching Cycle 525's recurrent domain size;
- deterministic high-sector states at weights 4, 6, `M/4`, `M/2`, and
  `M-1`;
- two successive B applications, bank-lawfulness, inverse, leakage,
  deleted-CZ, deleted-bank-swap, deleted-preparation-coefficient, and
  perturbed-CZ controls.

The complete low-sector table is:

| size | vacuum | N=1 | N=2 | baseline failures | failures after deleting all shadow CZs |
|---:|---:|---:|---:|---:|---:|
| L5 | 1 | 750 | 280,875 | 0 | 60,600 |
| L6 held | 1 | 1,296 | 839,160 | 0 | 154,800 |

Deleting the correction therefore reproduces Cycle 523/528's exact endpoint
residual.  Deleting the bank swap leaves the correlated output outside the
declared code on named states.  Perturbing the first active CZ by `1e-4`
produces the expected basis residual `|exp(i 1e-4)-1|`.

The quadratic residual contains 60,600 coefficients at L5 and 154,800 at
L6.  The corresponding symmetric GF(2) ranks are 576 and 1,040.  These ranks
are diagnostics of this factorization; they are not claimed as minimum
physical content.

## Bounded physical runtime layout

Use a period-eight macrocell with the roles

```text
q_(x,d) at 8x - D_d,
a_(x,d) at 8x - 2D_d,
b_(x,d) at 8x - 3D_d,
tau_x    at 8x.
```

The 19 offsets are distinct and form four proper-cubic orbits: centre plus
three six-direction shells.  L5 and L6 recurrent placements have no
collisions.  Matter–`a` CZ and `a`–`b` SWAP pairs have physical L1 distance
one.  The B matter partners have constant distance six in this expanded
layout.  Every runtime call has support two M2; nearest-neighbor routing of
the distance-six B call is not synthesized, but its neighborhood is bounded
independently of L.

Per cell the B compiler uses six CZs, three endpoint FSWAPs, and six bank
SWAPs: 15 calls.  Cycle 523 has 97 non-B calls per cell, so the combined
bounded two-M2 call count is 112 per cell.  This is a fixed schedule without
runtime host branching.  The role/edge family and gate list are mapped into
themselves by all 24 proper-cubic frames, and the geometric mode maps close on
all 576 frame products.

## Why this is not yet the physical compiler

The code conditions are

\[
 a_i=\bigoplus_jA_{ij}n_j,
 \qquad
 b_i=\bigoplus_jA_{ij}n_{P(j)}.
\]

They are not bounded local constraints.  The maximum support is 601 M2 at L5
and 1,081 M2 at L6.  Direct CNOT preparation of both banks uses 121,200 calls
at L5 and 309,600 at L6, or 969.6 and 1,433.33 calls per cell.  A dependency
reaches coarse periodic L1 distance 6 at L5 and 9 at L6, furnishing matching
radius-one preparation-depth witnesses.  Deleting one `A_ij` preparation
coefficient flips a named lawful shadow bit exactly.

The fixed `A` chart is also not proper-cubic covariant.  Plain geometric
transport of the shadow constraints passes only the identity frame and fails
the other 23 at both sizes.  The complete 24-chart orbit is finite and closes
abstractly under all 576 frame products, but selecting and preparing the
active chart locally—without a supplied frame/order register—has not been
constructed.  Storing an orbit is not the same as synthesizing a covariant
code.

Finally, the Cycle-523 coin and reverse-A factors change occupation
amplitudes/configurations before B.  A full recurrent update would have to
apply both while coherently maintaining `a=An` and `b=APn`.  Conjugating them
by the global charted encoder merely renames the same preparation wall.  Cycle
525's successful dense joint-code completion is useful bounded algebraic
precedent, but it does not supply this primitive recurrent shadow transition.
Hence mass/contact fixtures are preserved as comparators, while a full
combined physical intertwiner is not claimed.

## Mass, contact, and seam fixtures

The runner re-executes Cycle 523's full local M64 onsite compiler and Cycle
230's seam block.  It retains:

- onsite intertwiner residual `5.272182555577386e-15` and zero leakage;
- inverse residual `7.504184205291937e-15`;
- Cycle 219's beta `-0.3` mass with residual `2.220446049250313e-16`;
- all 15 `g=0.37` contact phases and deletion residual;
- the two Cycle-230 seam singular values.

These fixtures are not promoted to a full update theorem because the
correlated-shadow coin/recode has not been locally compiled.

## Supplied structure and dependency disposition

Supplied rather than derived are the Cycle-219 coin, Cycle-230 contact and
factor order, Cycle-523 QR schedule, Cycle-525 three-cell domain shape, the
site-major mode order defining `A`, and the period-eight origin.  Shadow
values are defined by the encoding but not locally prepared.  No global
parity service, runtime host choice, physical duration, energy, Record, or
source law is supplied or inferred.

- `C_ref`: unchanged; the globally ordered CAR exterior action remains the
  coarse reference.
- `C_num`: unchanged; the finite GF(2) theorem is exact but is not a continuum
  estimate.
- `C_wrap`: unchanged; no phase is called physical energy or time.
- `C_int`: fixtures preserved, but no new interaction law.
- `C_local`: advances from one-link closure to exact recurrent full-Fock B
  runtime on a correlated algebraic code.  Bounded local code constraints,
  preparation, onsite recurrence, and fixed-code covariance remain open.
- `C_source`: unchanged.

There is no shared obstruction and no axiom pressure.

## No-go discipline N1–N8

Broad no-go gate status: **FAIL / DO NOT SHIP**.  The result is demoted to
`partial-attempt-with-named-untested-routes`.  The charted double-shadow
construction is one route, and its failure to meet preparation/covariance
does not close the gauge or higher-form families.

### Exact target contract

| field | contract |
|---|---|
| Target | bounded covariant locally prepared M2 compiler for the complete recurrent B stream |
| Domain | all lawful Fock states; complete L5/held-L6 vacuum/N1/N2 controls |
| Allowed | Cycle-219/230 law, Cycle-523 onsite schedule, bounded fixed M2 gates and local constraints |
| Forbidden | global order/parity service, preferred frame, host-selected chart, or supplied nonlocal preparation |
| Edge cases | odd parity, periodic seams, inverse, deletion, leakage, higher sectors, 24/576 covariance |
| Completion witness | locally prepared `E` and bounded `G` with `GE=E Gamma(P)` and recurrent onsite compatibility |
| Not closure | algebraic sign factorization, exact runtime on nonlocally prepared shadows, or an abstract chart orbit |

### N1 — alternative-route normalization

| family | object / mechanism / terminal obligation | status |
|---|---|---|
| double shadow | two linear parity banks / quadratic residual / local covariant preparation plus onsite recurrence | **ATTEMPTED** — runtime exact; terminal obligation remains |
| local Gauss link code | edge qubits / divergence and flux attachment / all-parity recurrent isometry | **OPEN — NOT CLOSED** |
| higher-form face code | plaquette/face qubits / local bosonization cocycle / bounded spin-sector preparation | **OPEN — NOT CLOSED** |
| 24-chart relational code | cubic orbit of shadow charts / internal frame gauge / no-selector covariant code | **ATTEMPTED PARTIALLY** — orbit closes; selector/preparation absent |
| gauge-redundant prefix | unanchored prefix sectors / local recode modulo gauge / odd-sector and seam-free phase | **OPEN — NOT CLOSED** |
| Cycle-236 correlated Majorana | auxiliary fermionic link sector / string cancellation / bounded qubit constraints and prep | **OPEN — NOT CLOSED** |
| overlapping Cycle-525 roles | joint recurrent selected patches / shared role algebra / primitive volume transition | **OPEN — NOT CLOSED** |

Multiple normalized families remain live, so a broad negative cannot ship.

### N2 — wall-independence audit

The raw conditions—nonlocal constraints, growing preparation, failed
fixed-chart covariance, preferred order, and missing onsite shadow
recurrence—share the same upstream object: the site-major `A` chart.  They
are collapsed into one `W_charted-encoding` wall rather than counted as five
independent walls.  Replacing `A` by a genuinely local covariant Gauss/higher-
form code could change all of them together.  The bounded distance-six
matter routing is a separate primitive-routing obligation, but the requested
bounded-neighborhood result does not treat it as a failure.

### N3 — hidden-wall scan

| phrase/hit | classification |
|---|---|
| “define A” / “by the encoding” | load-bearing site-major chart; explicit `W_charted-encoding` |
| “proper-cubic orbit” | abstract family closure only; active chart selection explicitly unsynthesized |
| “Cycle 523/525 supplies” | retained comparator/domain shape, not a shadow-preparation authority |
| “standard”, “obvious”, “naturally” | absent from proof obligations |

The period-eight origin, chart, coefficients, and patch shapes are all in the
supplied-structure inventory.

### N4 — residual matching

| predecessor | predecessor residual | Cycle-529 use | match? |
|---|---|---|---|
| Cycle 523 | endpoint FSWAP versus intrinsic full B sign | deleted-CZ comparator | yes: 60,600/154,800 exactly |
| Cycle 528 | product-prepared endpoint-diagonal response class | correlated two-bank stateful route | no; Cycle 528 is a boundary, not a witness against this route |
| Cycle 525 | joint selected-patch algebraic recurrence versus primitive volume recurrence | 988-state higher-sector domain only | yes for domain shape; no primitive authority imported |

### N5 — rhetoric audit

| resolution | result |
|---|---|
| each quadratic coefficient | exact exhaustive identity |
| complete global vacuum/N1/N2 | exact L5/L6 stateful intertwiner |
| two-cell full Fock | exact 4,096-state test |
| three-cell N<=3 | exact 988-state straight and corner tests |
| all global Fock sectors | exact consequence of the quadratic-character theorem, plus high-sector controls |
| local physical code/preparation | not achieved |
| other correlated gauge formulations | not tested |

The result is called an exact charted runtime, not a physical-site compiler or
general impossibility.

### N6 — partial-closure path

The double-bank swap is reusable primitive structure: any local covariant
replacement that supplies the same residual syndrome can retain the 15-call
B schedule and Cycle-523 onsite fixture.  The 24-chart orbit supplies a finite
covariance target.  A local Gauss/face constraint presentation could retire
`W_charted-encoding` without an axiom change.  No new axiom is proposed.

### N7 — hostile steelman

A hostile reviewer should reject any negative inference from the charted
preparation failure.  Cycle 529 proves that stateful auxiliary recurrence is
enough algebraically; the only missing mechanism is a local covariant
presentation of its syndrome.  Cycle 236 shows string cancellation by an
auxiliary fermionic sector, and Cycle 528 left correlated preparation and
non-diagonal gauge transitions explicitly open.  The actionable counter-route
is to encode the two syndrome banks as Gauss-law equivalence classes rather
than fixed parity words, then test a two-cell/full-Fock local isometry and
recurrent L5/L6 update.  That route could invalidate every chart-specific
wall at once.

### N8 — cross-cycle echo

| prior cycle | prior wall | Cycle-529 change |
|---|---|---|
| 236 | exact dressed action but nonlocal JW constraint/prep | replaces independent links by exact global syndrome, but still lacks local prep |
| 260 | exact phase but growing shuttle preparation | makes B recurrence constant-depth by bank swapping, while initial/onsite prep remains global |
| 523 | exact onsite schedule but norm-2 B stream | closes B signs algebraically and preserves the onsite fixture separately |
| 525 | exact shared-cell algebraic recurrence but primitive volume transition open | matches its N<=3 patch domain and retains the same algebraic/physical boundary |
| 528 | exact one link, product sector fails | moves to correlated stateful banks outside the falsified class |

No prior echo retires `W_charted-encoding`; several identify mechanisms that
could reopen it.  Therefore no route-independent obstruction is claimed.

## Optimal next campaign

Replace the fixed `A` words by a local gauge equivalence class.  Begin with a
two-cell/full-Fock patch carrying matter plus edge/face syndrome qubits.
Require local Gauss constraints, a constant-depth preparation from arbitrary
matter, the same CZ/FSWAP/stateful-bank action modulo gauge, and a primitive
onsite Givens transition.  Only after the two-cell code and inverse/leakage
controls pass should it widen to the Cycle-525 straight/corner N<=3 patches
and complete L5/held-L6 census.
