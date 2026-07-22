# Root-free full-N<=3 carrier compiler and unique-genesis tournament — Cycle 600

Date: 2026-07-22

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, audit-status, or PR-control surface changes.

## Result up front

Cycle 600 closes Cycle 598's coherent-carrier update residual, but not its
global-sector genesis residual.

The strongest exact result is a standalone carrier presentation. For a box
with `V=L^3` coarse cells, define three normalized neutral orbitals

```text
chi_r = V^(-1/2) sum_x |x,r>,  r=0,1,2,
```

and the full-volume encoder

```text
E_L : Fock_(N<=3)(C^(6V))
      -> wedge^3(C^(6V) direct-sum span{chi_0,chi_1,chi_2}),

E_L psi_N = chi_0 wedge ... wedge chi_(2-N) wedge psi_N.
```

The three wedge factors are auxiliary species. Every species permutation acts
by its global sign, hence on the same ray. Species identities do not descend
as locally physical particle labels; only `S3`-invariant observables and
updates are declared. The Cycle-219 massive coin, torus stream, Cycle-230
onsite even contact, and seam signs all lift functorially and exactly for
`N=0,1,2,3`.

The executable certifies the theorem by an exhaustive 42-column local table,
an executed 1,000-row three-word table, normalized site-word realizations of
all three neutral orbitals on L3/L6/L7, exact torus stream/contact word tests,
every translation, all 24 proper-cubic frames, and all 576 frame products.
The 729 occupied-orbital rows become 1,000 rows when the required absent word
is included.

This is **not** a `53+12` composition with the accepted Cycle-590 matter
update. It is a standalone 12-M2/cell carrier presentation replacing that
matter representation. No correlated matter-tensor-carrier update was
executed, so no such composition is claimed.

Exactly one carrier of each species remains a supplied global sector. Local
four-M2 word validity, matter-mode collision rejection, and local update tables
do not enforce global count: an extra remote neutral carrier or a missing
carrier passes every declared local check. Topological winding, reversible
saturation, dissipative coalescence, and deterministic blank cellular-automaton
routes do not close that sector in this cycle. Those are scoped route results,
not a shared obstruction. There is no axiom pressure.

## Exact target contract

```text
Target A:
  one coherent root-free carrier representation carrying the complete
  Cycle219/230 N=0,1,2,3 coin + stream + contact + seam law

Target B/C:
  replace supplied exactly-one-of-each carrier sector by a local,
  translation-covariant genesis/enforcement mechanism

Allowed:
  accepted Cycles219/230/590/593/598 laws and fixtures
  three auxiliary species, provided their identities quotient to rays
  bounded local M2 words and transported compile-time frame families

Forbidden weakenings:
  carrier-only EG called matter-tensor-carrier EG
  conserved supplied count called locally generated count
  scan/coalescence output called static enforcement
  a selected Wilson line called autonomous topology
  species names called physical particle identities
  schedules called physical time
  carrier bookkeeping called empirical charge, energy, stress, or source

Train: L3
Held: L6
Held-out size: L7
Tolerance: exact integer/word checks or 5e-9 for inherited numeric fixtures
Caps: 360 seconds and 3 GiB maximum RSS
```

Complete N4 interactions remain separate. Cycle 600 concerns exact `N<=3`
action and enforcement of that domain; it does not supply or claim N4
interactions.

## Exact shore

The runner pins accepted Cycle 598 at commit `fed7cc8183`, including its
runner, receipt, cold transcript, and accepted independent-parent appendix.
Through that shore it inherits:

- the Cycle-219 `beta=-0.3` proper-cubic massive six-ray coin;
- the Cycle-230 onsite CAR contact and seam fixtures;
- the Cycle-590 mass/contact/seam benchmark values as regression references
  only, not as a standalone-carrier physical EG proof;
- the Cycle-598 four-M2 carrier-role coordinates and root-free translation
  audit;
- the explicit finding that exactly one carrier per species was supplied.

The accepted Cycle-598 receipt retains its pre-appendix note hash; the current
accepted note hash is pinned separately.

## Route A — full exterior carrier compiler

### Physical word and local/global split

Each species owns one four-M2 word at every coarse cell:

```text
0       absent: this species' carrier is at another cell
1..3    neutral type r=0,1,2
4..9    bound to one of six local matter directions
10..15  rejected malformed labels
```

Thus each occupied carrier has nine local levels—six matter directions plus
three neutral types—while the tenth valid local word is absence. Three species
use exactly 12 M2/cell. The standalone layouts are:

| split | L | cells | carrier M2 | M2/cell | max fine-L1 radius |
|---|---:|---:|---:|---:|---:|
| train | 3 | 27 | 324 | 12 | 3 |
| held | 6 | 216 | 2,592 | 12 | 3 |
| held-out | 7 | 343 | 4,116 | 12 | 3 |

The runner reconstructs the literal Cycle-598 carrier coordinates, records
their hashes, and checks transported wire injection/group laws. The earlier
53 M2/cell matter representation is not counted and not independently
updated.

Local checks reject labels 10..15 and multiple species bound to the same
matter direction. Matter occupation is decoded from the bound carrier words;
there is no separate matter register in this presentation. The checks ensure
consistent words at a cell. They intentionally
do not count a species across the torus. On vacuum samples, global counts
`(1,1,1)`, `(0,1,1)`, and `(2,1,1)` all pass the same local table. This cleanly
separates local one-word/collision checks from the supplied exactly-one sector.

### Signed coherent isometry

For a local logical occupation subset `S` with `N=|S|<=3`, form the ordered
three-orbital list consisting of neutral types `0..2-N` and the modes in `S`.
The code column is the normalized Slater sum

```text
E |S> = (1/sqrt(3!)) sum_(pi in S3) sgn(pi)
        |orbital_pi(0), orbital_pi(1), orbital_pi(2)>_species.
```

There are

```text
sum_(N=0)^3 binomial(6,N) = 1+6+15+20 = 42
```

logical local columns. The three four-M2 words give `10^3=1,000` local table
rows. Restricting away the absent word leaves `9^3=729` occupied-orbital rows;
the complete exterior has dimension `binomial(9,3)=84` and the declared
neutral-pattern code has dimension 42.

Every one of the six species permutations multiplies all 42 columns by the
permutation's global sign. The massive coin, contact, stream, and number
observable preserve the same sign sector. Therefore the update and declared
`S3`-invariant observables descend to rays. A species-resolved probe is outside
the quotient code; species are not classical particle labels.

### Complete coin/contact/stream action

Extend the six-direction massive coin `C` to each ten-level local word by

```text
U_word = 1_absent direct-sum I_neutral(3) direct-sum C_bound(6).
```

Apply the identical `U_word` to all three species. Exterior functoriality gives

```text
wedge^3(U_word) E_N = E_N wedge^N(C)
```

for every `N=0,1,2,3`. The runner executes the full 42-by-1,000 code table,
its inverse, and a coherent random superposition spanning all four number
sectors. Deleting the coin from one species creates a large code-leakage
signal. This proves that identical species action is load-bearing.

Carrier-collision/Pauli rejection is also explicit. The signed Slater columns
have zero amplitude whenever two species occupy the same matter direction,
and the post-coin collision amplitude remains zero. The corresponding
off-code local collision words are rejected.

The onsite contact phase is

```text
exp(i g n_x(n_x-1)/2).
```

It depends only on the decoded bound matter orbitals, not species. The local
table exhausts all 42 logical subsets. On global L3/L6/L7 words, the physical
phase is independently reconstructed from each three-carrier word by decoding
every matter orbital's cell; neutral labels contribute zero. It exactly
matches the logical product of onsite contact phases.

The torus stream applies the same one-particle permutation to each bound
carrier and identity to neutral words. Reordering its image inside the exterior
product automatically supplies the fermionic sign. Explicit seam samples
exercise both `+1` and `-1`; no runtime Jordan-Wigner order, parity service,
global matching, or host query is used. The accepted Cycle-230 contact/seam
fixture residuals are inherited unchanged because neutral exterior factors are
spectators of the matter operator.

Here “inherited unchanged” is an algebraic logical-law statement: the same
coin and contact/seam matrix elements acquire normalized neutral exterior
spectators. It does not import the Cycle-590 53-M2 physical intertwiner into
this different standalone representation.

The physical crossed-link gate is also enumerated independently. For each of
six directions it swaps the two-word rows `(bound,absent)` and
`(absent,bound)` and fixes the other rows. All `6*16^2` rows invert exactly and
valid labels never leak into 10..15. Deleting the carrier stream update while
the logical mode streams gives a nonzero word residual at every tested size.

The full-volume matrix is not materialized. The certificate is factorized:

1. the exact 42-column/1,000-row onsite table;
2. the explicit normalized neutral-W site orbitals;
3. exact L3/L6/L7 global stream and independently decoded contact words;
4. exterior-algebra identities valid for arbitrary `V`.

This is an algebraic/compiler theorem with executed finite certificates, not a
claim that a huge full-volume tensor was stored.

### Neutral orbitals and covariance

For every L3/L6/L7 neutral type, the runner constructs the literal vector
`V^(-1/2) sum_x |x,r>` over local four-M2 site words. The three-orbital Gram
residual, every-translation residual, and all24 proper-cubic residual are zero.
Coin, stream, and contact act locally as identity on neutral words.

Every torus translation is tested against the six-ray stream on every mode.
All 24 proper-cubic frames commute with the stream and massive coin, and all
576 frame products satisfy the group law. This is exact translation and
proper-cubic covariance, not Lorentz covariance.

### Physical support and open gate synthesis

The executed onsite code table reads three four-M2 words: 12-M2 support. A
single-species crossed-link hop reads two four-M2 words: eight-M2 support. The
local contact reads the three words and is diagonal on decoded bound counts.

No elementary M2 decomposition of the 12-role 1,000-row table is executed, and
no elementary gate count is claimed. A unitary code table exists and is
tested; physical elementary synthesis remains open.

## Route B — topological winding-loop genesis

For each auxiliary species, Route B uses three outgoing `Z2` link bits and one
mark bit per cell. A straight noncontractible loop has zero local Gauss
syndrome and unit winding in one axis. The orbit of all axes and transverse
positions contains exactly `3L^2` straight loops and is permuted by every
translation and all 24 proper-cubic frames.

A selected Wilson-line schedule toggles the L edges of one loop. Intermediate
words have two endpoint syndromes; the final word is Gauss-lawful and has unit
winding. The reverse schedule restores blank, and deleting one edge produces
two syndrome sites. This is an explicit local-gate construction with depth L,
not autonomous genesis. Its selected axis, transverse line, starting phase,
and schedule are supplied. Schedule is not time.

Local plaquette updates preserve the three winding coordinates exactly. A
uniform superposition over the `3L^2` orbit would restore spatial/cubic
covariance, but its preparation is not constructed.

Most importantly, winding is not a point binding. A local mark-on-loop check
accepts a second remote mark on the same loop. Exactly one mark remains a
supplied sector, so the loop does not independently enforce one matter-bound
carrier.

## Route C — fixed-alphabet saturation and creation comparators

### C1 reversible saturation scan

A nearest-neighbour snake carries a `seen` bit. The first active carrier stays
active; every later active word is moved into a local debris bit. From three
inputs the final counts are one active and two debris. The inverse reconstructs
all three inputs exactly. Blank debris, a unique head, the base path, and the
transported schedule are supplied.

Deleting one saturation call leaves two active carriers. Nonblank overlapping
debris is rejected. Every translated path family, all24 rotated families, and
all576 products are exact on L3/L6/L7.

The scan adds three debris M2 and two head/seen-track M2 per cell. If composed
with the standalone carrier presentation it uses 17 M2/cell, or 3,672 M2 on
held L6. It does not make the pre-scan remote duplicate locally inadmissible.
Erasing the debris while keeping reversibility would erase which-input
information, so no such erase is claimed.

### C2 dissipative coalescence

The distinct local reaction family uses transported nearest-neighbour
diffusion `10->01` and coalescence `11->01`. It leaves one survivor from every
tested nonempty word. Deleting the coalescence rule leaves all three. Vacuum
remains vacuum.

This route is dissipative and scheduled; it is not a coherent unitary lift of
Route A and does not generate a carrier from blank.

### C3 deterministic blank cellular automata

All 256 elementary radius-one binary rules are exhausted from a uniform blank
on the L3/L6/L7 site counts. Every output remains uniform and none has exactly
one occupied site. The general scoped reason is translation equivariance: a
deterministic translation-equivariant rule maps a translation-fixed input to a
translation-fixed output.

This is only a classical deterministic blank-to-localized-one comparator. A
quantum translation-invariant W-state parent Hamiltonian or dissipative dark
state remains a concrete untested route.

## Route dispositions

| route | disposition | exact gain | explicit residual |
|---|---|---|---|
| A exterior carrier | **pass; strongest** | full coherent N=0..3 coin/stream/contact/seam EG, S3 ray quotient, collision cancellation, neutral-W covariance, 12 M2/cell | exactly-one sector and W preparation supplied; elementary gate decomposition open; no Cycle590 tensor composition |
| B winding loop | pass as scoped audit | local loop/Gauss law, Wilson generation/inverse, orbit covariance | selected topological sector/schedule and one mark supplied |
| C1 reversible scan | pass as scoped audit | exact one-active-plus-debris normalization and inverse | pre-scan duplicates, head/path/debris supplied; not static enforcement |
| C2 coalescence | pass as scoped audit | one survivor from tested nonempty inputs | nonunitary, scheduled, vacuum stays empty |
| C3 blank CA | pass as scoped classical comparator | exhaustive 256-rule uniform-output certificate | quantum W-state and nonuniform seeds untested |

Route-specific residuals are not constitutional evidence. Route A itself is a
positive closure of Cycle 598's full coherent-action residual.

## Supplied / derived / open inventory

Supplied:

- accepted Cycle-219 coin and Cycle-230 contact/seam law;
- periodic L3/L6/L7 geometry and three auxiliary species;
- neutral-type convention `r=0,1,2` and which `3-N` types are occupied;
- exactly one carrier word of each species across the torus;
- normalized neutral-W preparation and coherent signed code preparation;
- identical species-local coin blocks and exact noiseless code-table gates;
- off-code unitary extension and elementary M2 synthesis;
- Route-B winding/mark sector, selected Wilson line, axis, origin, and schedule;
- Route-C nonempty input, blank debris, unique head, path, frame schedule, and
  irreversible reservoir where used;
- finite arithmetic, random seeds, tolerances, and resource caps.

Derived:

- exact exterior isometry and all six S3 ray signs;
- exact descended number/contact observables and species-symmetric updates;
- exhaustive N=0,1,2,3 coin/contact/stream tables and inverse;
- coherent cross-number superposition residual;
- zero carrier-collision amplitude and deletion leakage signal;
- explicit L3/L6/L7 neutral-W normalization and covariance;
- global stream/seam signs and independently decoded contact phases;
- literal standalone 12-M2/cell layouts and support counts;
- topological loop orbit, winding, Wilson inverse/deletion controls;
- reversible saturation, dissipative coalescence, and 256-rule blank-CA
  controls;
- every translation, all24, all576, held-size, malformed, deletion, and
  leakage checks named above;
- fresh normalized N1–N8 audit.

Open:

- autonomous local generation/enforcement of exactly one carrier per species;
- autonomous preparation of the three neutral-W orbitals;
- an elementary M2 gate decomposition of the 12-role local code table;
- a topological mechanism that yields exactly one local point binding without
  a supplied mark sector;
- reversible debris retirement or a coherent saturation reservoir;
- quantum W-state parent/dark-state construction with finite-size gap and
  preparation law;
- any correlated composition with the Cycle-590 53-M2 representation;
- complete N4 interactions, noise, continuum/Lorentz limits, gravity/source,
  and Born/actuality laws.

## Six-wall ledger and maturity

| wall | movement | residual |
|---|---|---|
| `C_ref` | root-free S3 species quotient and translation-uniform neutral orbitals are explicit | exactly-one and neutral-W preparations supplied |
| `C_num` | constant three-carrier capacity supports exact N<=3 with no growing modulus | global sector genesis open |
| `C_wrap` | full stream/seam exterior signs exact; loop orbit covariant | winding and one-mark sectors supplied |
| `C_int` | major: complete N=0..3 coin/stream/contact/seam carrier EG | elementary table synthesis and N4 interactions open |
| `C_local` | bounded standalone 12-M2/cell tables and layouts | static autonomous genesis not obtained |
| `C_source` | every carrier/neutral/loop/mark/debris role is explicit bookkeeping | not empirical charge, energy, stress, source, or gravity |

Evidence-planning maturity becomes operational quantum/Records `4.80/5`
repository and `4.65/5` strict; causal time `3.95/5` and `3.80/5`;
inertia/matter `4.92/5` and `4.94/5`; gravity/source `4.10/5` and `3.85/5`;
Born/probability `4.20/5` and `3.65/5`. These are planning coordinates, not
probabilities, audit grades, or constitutional status.

## Fresh N1–N8 no-go discipline

### N1 — normalized alternatives

Five materially distinct families are attempted and normalized by primary
object, mechanism, and terminal obligation: the exterior carrier compiler;
topological winding loops; reversible saturation with debris; dissipative
coalescence; and deterministic blank cellular automata. Quantum W-state
genesis is a sixth concrete live/unattempted family. No agents, notations, or
artifact types are counted as separate approaches.

### N2 — directional wall independence

All 21 directional pairs among exactly-one sector genesis, neutral-W
preparation, elementary 12-role synthesis, winding preparation, one loop mark,
head/path/debris retirement, and coherent reversible saturation are recorded.
None of the tested closures supplies the named mechanism for another.

### N3 — hidden-condition scan

The neutral pattern, sign convention, exactly-one species sector, W
preparation, off-code extension, elementary decomposition, winding/mark
sector, Wilson/scan/coalescence schedules, blank debris, unique head, and
irreversible reservoir are all explicit supplies. There is no hidden
“standard,” “obvious,” or background step.

### N4 — residual matching

Cycle 598's uncertified coherent many-body carrier lift exactly matches Route
A and is closed. Its remote duplicate/unique-genesis residual exactly matches
Routes B/C and remains. Cycle 598's harmonic preparation residual matches the
Wilson-line/topological audit. Older parity/order walls are not used as
obstruction witnesses.

### N5 — rhetoric resolution

The species quotient is tested on every local code column, all species
permutations, updates, and symmetric observables. The loop negative is only for
this marked straight-loop family. The scan negative is only for this supplied
path/head/debris table. The blank symmetry result is only classical,
deterministic, translation-equivariant genesis from a uniform blank; the
quantum W-state resolution is explicitly untested.

### N6 — partial-closure paths

Live constructive paths are a local one-excitation parent Hamiltonian or
dissipative W dark state; elementary synthesis of the 12-role table; a loop
used only as a topological certificate plus a separate endpoint/mark code; and
coherent debris retained as a gauge reservoir rather than erased. These are
import-retirement programs, not new axioms.

### N7 — hostile steelman

A hostile reviewer should accept the compiler half and reject any genesis
no-go. The exterior code proves that auxiliary identities can quotient to a
ray. A frustration-free one-excitation parent Hamiltonian or
translation-invariant dissipative dark-state construction could prepare a W
carrier without a classical localized seed. That concrete quantum route was
not attempted, so genesis is unfinished construction, not a shared
obstruction.

### N8 — cross-cycle echo

Cycles 560/563 retired decoder/order services by bounded tables, and Cycle 598
removed the fixed root on a prepared sector. Cycle 600 now closes the full
carrier-update residual while exposing sector preparation. The same
import-retirement pattern supports another constructive campaign rather than
constitutional language.

Broad no-go, minimum-content, shared-obstruction, and axiom-pressure claims:
**DO NOT SHIP**. There is no axiom pressure.

The unique genesis residual is therefore retained. The cellular automaton
comparator is one deliberately classical resolution, not the untested quantum
resolution.

## Interpretation firewall and next campaign

- Schedule is not time.
- Carrier bookkeeping is not empirical charge, energy, stress, source, or
  gravity.
- Species permutations are ray redundancy, not locally physical identities.
- A supplied exactly-one sector is not locally enforced genesis.
- Conservation is not genesis.
- Saturation output is not static enforcement.
- Dissipative coalescence is not a coherent unitary compiler.
- Proper-cubic and translation covariance are not Lorentz covariance.
- The standalone carrier presentation is not a Cycle590 tensor composition.
- Exact N<=3 action/enforcement is not complete N4 interactions.

The optimal next campaign is a translation-invariant one-excitation parent
Hamiltonian or dissipative dark-state preparer for each carrier/neutral
species, with gap, leakage, malformed-sector, deletion, L3/L6/L7, all24, and
autonomy controls. In parallel, compile the executed 12-role exterior table
into accepted elementary M2 gates.

## Independent parent verification

The parent independently inspected the standalone-versus-composed boundary,
the factorized full-volume certificate, the independently decoded contact
test, and the local-versus-global carrier constraints before rerunning the
frozen runner.

- worker runner SHA-256: `5b9bb9c1ae8585b7395f1a1a94040016ff8cc73e5cfbb430b16183e7133b64ba`;
- worker note SHA-256 before this appendix: `492d41772d95bdf8ce4dc7c1ae753ab4f2a7f258ce5369b0449ccb4881b9ba64`;
- worker receipt SHA-256: `2832d1e7768034b5aabac7d1cc760aee01b189e53493d25526f0322437f2cd63`;
- worker cold transcript SHA-256: `ae85d6e4dc29b240d5eb2374ce22a2836dc0c7b0f85831406462779b1803f183`;
- parent rerun: `7 PASS / 0 FAIL`, `30.080885541043244 s`, maximum
  RSS `238,567,424` bytes;
- parent receipt SHA-256: `3bddb02e1297440781fbd960a07e1b4ee021c9eadba8a6a5372dbb9812fb7cbd`;
- parent transcript SHA-256: `daa7ee2e7b8a24796460ca38ffada347b9abdbb16afbc0456b47a2b00ecb699e`.

After deleting only `elapsed_seconds` and `maximum_RSS_bytes`, the worker and
parent receipts are byte-identical under sorted JSON normalization. The
parent therefore accepts the exact standalone 12-M2/cell full-`N<=3` carrier
compiler theorem and its deletion, covariance, and held-size controls. It
does not accept a `53+12` Cycle590 composition, an elementary M2
decomposition, local enforcement of exactly one carrier per species,
autonomous neutral-W preparation, a genesis no-go, shared obstruction, or
axiom pressure.
