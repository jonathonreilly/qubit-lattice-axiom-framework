# Cycle 822 Route A fixed-type-atlas correction

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Baseline:** the first Route-A runner and note in this Cycle-822 package,
constructed from the landed Cycle-821 surface

**Status:** the first Route-A typing is rejected; a corrected conditional
compiler is positive on an explicitly enlarged charged-carrier/neutral-work
atlas

## Correction

Cycle 821 protects one fixed

\[
P_{\rm ext}=P_{\rm matter}\prod_{c\in\mathrm{carrier}}Z_c.
\]

Companion, syndrome, token, and neutral-work modes are neutral. The first
Route-A runner instead formed product Z on every local gate support. That test
was not the Cycle-821 test: it charged companion and token modes, and it allowed
the same coordinate to serve charged and neutral routes in different factors.
Its claim that all 328 seam factors had a physical Cycle-821 compiler is
demoted.

The correction runner is
`scripts/frontier_cycle822_route_a_fixed_type_atlas_correction_2026_07_30.py`.
It first audits the old emitted words unchanged, then builds one fixed global
type atlas for the complete seam dictionary of each held box and recompiles
every factor against that atlas.

## Exact legacy failure census

On `(2,1,1)`, `(3,1,1)`, `(3,2,2)`, and `(5,3,2)`, the old program emitted
337,496 primitives for 328 factors. Under the actual fixed `P_ext` it has:

- 10,112 elementary parity failures;
- 9,784 failing route FSWAP factors;
- 164 failing mixed-type `U_dagger` factors and 164 failing mixed-type `U`
  factors;
- 337,496 failed cumulative-prefix certificates by factorwise induction; and
- 1,445 coordinates demanded as both charged and neutral.

The per-box `(factors, primitives, elementary failures, failed prefixes,
conflict coordinates)` rows are:

- `(2,1,1)`: `(4, 1564, 36, 1564, 8)`;
- `(3,1,1)`: `(8, 3128, 72, 3128, 16)`;
- `(3,2,2)`: `(80, 87008, 2640, 87008, 371)`; and
- `(5,3,2)`: `(236, 245796, 7364, 245796, 1050)`.

The first failing primitive occurs before every old factor's first certified
prefix, hence all old prefixes fail the elementary-factor induction. This is a
failure of the submitted route, not a route-independent no-go.

## One fixed corrected atlas

For each held box, all landed matter coordinates are fixed charged and all
landed companion coordinates fixed neutral. The compiler allocates two
disjoint connected routing networks once for the whole box:

- a charged network of explicitly counted carrier-relay M2, included in
  `P_ext`; and
- a neutral network of companion/token route-work M2, excluded from `P_ext`.

No coordinate occurs in both networks. Every route FSWAP has endpoints of the
same fixed type.

The clean token is a neutral diagonal rail pair. Two different lattice sites
are adjacent to both rails: one is declared a charged carrier center and the
other a neutral-work center. Thus a charged control reaches the charged center
only through carrier relays, while a neutral control reaches the neutral center
only through neutral work. Both can control the same local Fredkin. Fredkin
never changes its control occupation, so a charged-control/neutral-rail
Fredkin commutes exactly with `Z_control`.

The atlas resource counts `(charged carrier relays, neutral work including the
two token rails, total typed coordinates)` are:

- `(2,1,1)`: `(94, 66, 178)`;
- `(3,1,1)`: `(122, 83, 232)`;
- `(3,2,2)`: `(1205, 726, 2039)`; and
- `(5,3,2)`: `(2751, 1634, 4655)`.

These are supplied routing resources. They are not hidden inside, or claimed
to follow from, the landed Cycle-821 65-M2/cell palette.

## Type-correct algorithms

### Controlled pair

The syndrome control is neutral and both matter/carrier targets are charged.
The two targets use a charged carrier-relay route. The control uses a disjoint
neutral route whose last neutral site is adjacent to the charged pivot; the
local CZ is diagonal across that type boundary. The chronological word remains
returned `U_dagger`, returned CZ, returned `U`.

All eight letter/pivot cases have maximum dense target residual
`1.78534970688577e-15`, zero elementary and prefix `P_ext` residual, and zero
mixed-type route FSWAPs. The wrong-SWAP and deleted-return dense residuals are
respectively `7.999999999999999` and `8.0`; deleting a return leaves two label
mismatches.

### Mixed recurrent seam word

The X/Y sites are partitioned by fixed atlas type before pairing. Every landed
seam row has two charged X/Y sites and two neutral X/Y sites. The compiler
therefore applies one charged-charged Cycle-821 diagonalizer and one
neutral-neutral diagonalizer, never the old charged-neutral pairs. Z singleton
controls retain their fixed type and approach the matching token center.

The token phase, row-sign correction, reverse Fredkins, and reverse
diagonalizers are otherwise unchanged. Both pivot choices and both accumulator
orders execute for all seven typed row templates, including all operator
columns of the 17-site templates.

Across all 328 factors there are zero:

- fixed-atlas type conflicts;
- mixed-type route FSWAPs;
- elementary `P_ext` failures;
- cumulative-prefix failures by exact factorwise induction;
- radius-one failures;
- operand failures; and
- route-return failures.

The maximum exhaustive operator residual is
`3.1401849173675503e-16`. The dirty opposite-rail mutation has minimum residual
`1.4142135623730947`, and deleting a return leaves at least two label
mismatches. A separate dense accumulator with two charged and two neutral
controls has zero clean-isometry residual, zero prefix `P_ext` residual for
both control orders, and zero charged-control Fredkin commutator.

## Parity proof

The same fixed atlas defines every prefix. Each primitive separately commutes
with its restriction of the global `P_ext`:

- route FSWAPs and their CZ sign firewalls act within one type;
- charged `U/U_dagger` gates contain two charged X/Y legs;
- neutral `U/U_dagger` gates have no charged legs;
- local CZ and token phases are diagonal;
- Fredkin preserves its control and only swaps neutral rails.

Therefore, if prefix `V_k` commutes with the fixed `P_ext`, so does
`g_{k+1}V_k`. The runner performs this induction for every emitted primitive.
The dense controlled-pair and mixed-accumulator executors independently
multiply all prefixes against that same fixed parity matrix.

## Claim boundary

The correction does not reinstate the first runner's landed-palette claim. It
constructs all 328 physical words only on the explicitly enlarged typed atlas.
Genesis, enforcement, and renewal of the added charged carrier relays and
neutral work remain supplied, as do chart, program, occurrence, and the clean
token. No autonomous schedule, translation-invariant law, two-body Fredkin
decomposition, or physical-time claim is made.

No no-go claim is made.
