# Parity-doubling spectator compiler — Cycle 248

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset

This is an exploratory compiler probe, not an axiom, policy, registry, queue,
qualification, or audit-status change.  It does not alter any protected
surface.

## Result up front

The local parity-doubling idea produces a useful but non-closing result on the
actual Cycle-230/235 graph.

For one spectator beside every direction mode, the occupation-copy map

```text
E_mode |n_1,...,n_M>
  = |n_1,n_1; ...; n_M,n_M>
```

is an exact isometry of the **full Fock code**, including both total-parity
sectors.  On its code projector `P=E_mode E_mode^dagger`,

```text
phi(O) = E_mode O E_mode^dagger
```

is an exact isometric algebra homomorphism: multiplication, adjoint, and the
code unit all have zero residual in the two-mode executable control.  Each
equality `Z_data,i Z_spectator,i=+1` is local, independent, and sufficient to
make the doubled occupation locally neutral.  The original local `B_t` parity
is readable on either member of the pair with zero residual.  Copy preparation
is one parallel layer of local `CNOT(data -> spectator)` gates and asks no
global parity service, sector label, membrane, boundary, or reference charge.

That exact state map does **not** make the full CAR image local.  The exact odd
creation image retains the logical parity prefix.  Replacing it by the local
pair creator makes distinct modes hard-core bosons: the two local pair
creators commute, and their anticommutator on the encoded vacuum has norm `2`
instead of zero.  More decisively for this campaign, an endpoint-only doubled
FSWAP is exact in the isolated two-mode block but fails with residual
`2 sqrt(2)` when a third Fock-ordered mode lies between the endpoints.  The
actual Cycle-235 outer/B edges contain precisely such nonadjacent pairs under
any single tensor ordering. Even after supplying a fixed total-parity sector
so that each ordering string may be replaced by its shorter cyclic
complement, the encoded hopping/FSWAP images have maximum weights

```text
L = 3, 4, 5, 6:  58, 100, 154, 220 = 6 L^2 + 4.
```

These are favorable fixed-sector support bounds. On the full both-parity code,
choosing the cyclic complement itself needs a parity-controlled operation;
without that extra service the fixed-order supports can be longer. Thus the
displayed `E_mode` is a bounded full-state isometry and exact code
algebra embedding, but the corresponding exact `G_physical` for the actual
Cycle-230 stream is not bounded.  The endpoint shortcut is not a physical-site
compiler.  Spectator doubling alone has moved the parity-sector problem into
the locality of exchange/CAR; it has not removed it.

One spectator per coarse cell is cheaper and exactly carries the cell coin and
contact, but it is not a lawful realization on the actual Cycle-235 mode
graph.  Six equalities between one shared spectator and the six direction
modes have rank six on seven qubits and leave only one logical qubit, deleting
five of the required six.  Keeping only the one cell-parity equality restores
the `2^6` code dimension only by changing the gauging vertex from each
direction mode to the whole coarse cell.  That is a changed target, not a
solution on the declared graph.

The strongest constructive result is therefore a **local, reference-free,
full-parity spectator state code plus exact bounded onsite coin/contact
intertwiners and exact two-mode exchange gadgets**.  It preserves the supplied
one-particle mass value and the rank-73 seam state algebraically.  It does not
close the actual-graph stream locality or canonical state covariance.  This is
a route-specific partial closure.  There is no shared impossibility result,
no minimum-content result, and **no axiom pressure**.

## 1. Exact code and local constraints

### 1.1 Per-mode spectator

For `M=6L^3` original modes, use `2M` ordinary physical `M_2` factors.  The
constraints

```text
C_i = Z_(data,i) Z_(spectator,i) = +1
```

have bounded support two and independent rank `M`.  The `2M-M=M` code
exponent is exactly the original full Fock exponent.  A one-particle state is
sent to two nearby occupied physical factors, so its *combined auxiliary
charge* is even while its original occupation and local `B_t` remain
available.  This is a supplied encoding convention; it is not a derivation of
why nature should duplicate charge.

For arbitrary logical operators `O_1,O_2`, the executable small-block checks

```text
E^dagger E = I,
phi(O_1) phi(O_2) = phi(O_1 O_2),
phi(O^dagger) = phi(O)^dagger,
phi(I) = P.
```

All residuals are zero at machine representation.  This distinguishes exact
algebra homomorphism on the code from locality of its images.  `phi` is exact;
some `phi(O)` are not bounded-support operators.

Deleting one independent equality enlarges the code exponent by one for
one-, two-, three-, and six-mode cells.  The deletion control therefore sees a
real leakage channel rather than a redundant stabilizer.  Omitting spectator
transport from an exchange gives leakage norm `sqrt(2)` in the two-mode test.

### 1.2 Per-cell spectator

The comparator

```text
E_cell |n_1,...,n_6>
  = |n_1,...,n_6, (sum_a n_a) mod 2>
```

uses one constraint

```text
Z_s product_(a=1)^6 Z_a = +1.
```

It has the right six-qubit code exponent and a six-`CNOT` local preparation.
Because the fixed Cycle-230 coin and contact preserve cell parity,
`coin tensor I_s` and `contact tensor I_s` intertwine exactly; their residuals
are below `2e-12` and `2e-15` respectively.

But the actual Cycle-235 dual graph has one charge vertex per direction mode,
not one vertex per coarse cell.  Requiring the same spectator to neutralize
each of those six vertices imposes six independent equalities and leaves code
exponent one.  The cheaper layout is retained only as a target-changing
comparator.

## 2. Spectator transport, hopping/FSWAP, and exchange/CAR

In an isolated two-mode block, let `F_d` be FSWAP on the two data factors,
`S_s` ordinary SWAP on the spectators, `F_s` spectator FSWAP, and `CZ_d` the
data endpoint controlled phase.  On the equality code,

```text
(F_d S_s) E_2             = E_2 F_coarse,
(CZ_d F_d F_s) E_2        = E_2 F_coarse.
```

Both residuals are zero.  Two FSWAPs without the compensating `CZ_d` square
the fermionic sign into a bosonic sign and have residual `2`.  Acting on data
alone violates the equality code.  These are exact necessary transport and
exchange controls.

They are not sufficient on a graph.  For three coarse modes ordered
`0,1,2`, exchange of `0` and `2` in the intrinsic CAR representation depends
on the occupation of mode `1`.  Both endpoint-only doubled gates are blind to
that occupation:

```text
||G_endpoint E_3 - E_3 Gamma((0 2))||_F = 2 sqrt(2).
```

The failures occur on coarse basis states `011` and `110`.  Adding the exact
logical prefix repairs the intertwiner but restores an ordering string.  On
the repository's actual Cycle-235 outer-edge order, the fixed-sector shortened
prefix grows as `6L^2`; doubling adds four endpoint operators, giving the
weights `6L^2+4` reported above. The held-out `L=6` value `220` follows the
same law. On the full direct sum, selecting that shorter complement is an
additional parity-control import, so these numbers are not presented as a
sector-blind full-code implementation.

This exact residual prevents a false positive: an isolated FSWAP truth table
does not establish local fermionic exchange on a branching three-dimensional
graph.

For the per-cell comparator, a crossing changes both endpoint cell parities.
Four local `CNOT`s, from each endpoint occupation into both endpoint parity
spectators before the data exchange, give zero intertwining residual on the
one-active-mode slice.  Deleting those updates leaks by `sqrt(2)`.  Since one
cell spectator is shared by six incident streams, a bounded edge-coloring or
serialization schedule is also supplied.  This schedule is compiler control,
not causal time.

## 3. Coin, contact, mass, and seam

The per-mode code admits a bounded 12-qubit logical extension for every onsite
six-mode operator:

```text
G_cell = E_cell-block U_cell E_cell-block^dagger + U_off (I-P_cell),
```

with any supplied unitary off-code completion `U_off` compatible with the code
projector.  For the fixed Cycle-230 factors at `beta=-0.3`:

- the Fock-lifted coin is parity even and has onsite bounded support;
- the contact `exp(i g binom(N_x,2))` is diagonal and onsite;
- the contact is identity on the zero- and one-particle sectors;
- the copied occupation retains the Cycle-230 rest/analytic mass values
  `0.4534056541748851` and `0.4534056541748852` exactly within the
  predecessor tolerance;
- the Cycle-230 `L=3` principal sea still has original rank `73`; after copying,
  combined data-plus-spectator parity is even; and
- the sampled rank-73 seam block retains singular range
  `[0.9998884863600149, 1.0]` as an algebraically inherited fixture.

Those fixture statements are conditional on the exact isometry.  Because the
actual stream has no bounded physical intertwiner in this route, they are not
reported as a completed physical update or a completed rank-73 seam compiler.
Wrapped phase remains wrapped phase; it is not physical energy.  The contact
generator element remains an element, not a rate.

## 4. Constant overhead and lawful domains

If the 15 Cycle-235 face gauge factors are retained for direct comparison, the
censuses are:

| `L` | cells `N` | per-mode matter `12N` | per-cell matter `7N` | face gauge `15N` | per-mode total `27N` | per-cell total `22N` |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 324 | 189 | 405 | 729 | 594 |
| 4 | 64 | 768 | 448 | 960 | 1728 | 1408 |
| 5 | 125 | 1500 | 875 | 1875 | 3375 | 2750 |
| 6 held out | 216 | 2592 | 1512 | 3240 | 5832 | 4752 |

The spectator state code itself needs only the matter columns: 12 physical
`M_2` factors per coarse cell in the per-mode layout, or seven in the
target-changing per-cell layout.  The gauge columns are supplied comparison
structure, not secretly counted as a derived necessity.  Local neutrality
does not by itself construct a physical face-gauge state, autonomous gauge
preparation, or a new local CAR dictionary.

The tested periodic lawful domains are `L=3,4,5`, with `L=6` held out until the
formulae were fixed.  Equality rank, census, graph edge class, and maximum
exact hopping weight all pass at `L=6`.  The growing hopping weight fails the
bounded-support requirement uniformly; it is not a finite-size leakage
artifact.

## 5. Translations and all 24 proper-cubic frames

The *descriptor family* consisting of colocated data/spectator equalities,
endpoint spectator transport, and direction-permuted local gate templates is
carried into itself by unit coarse translations and all 24 proper-cubic
frames at `L=3,4,5,6`.  No direction, face, or local port is selected by that
family.

State covariance is stricter.  A canonical plain permutation of the physical
tensor blocks does not reproduce the fermionic Fock permutation sign.  In the
three-mode cyclic control,

```text
||U_plain E - E Gamma(T)||_F = 2 sqrt(2),
||U_sign-lane E - E Gamma(T)||_F = 0.
```

The second line supplies a fermionic sign lane.  On a bounded onsite direction
permutation that correction can be a bounded cell gate; on the actual spatial
graph and its nonadjacent stream edges it again needs the parity information
identified in Section 2.  Therefore this route passes covariance of its local
rule templates in all 24 frames but fails canonical plain-`M_2` state
covariance for the full actual-graph Fock compiler.  The sign lane is reported
as supplied structure, not erased from the ledger.

## 6. Cycle-245 two-sector correction: one physical update

Cycle 245 constructed separate even/odd state-gauging images.  Its observable
sign depends on the connection representative `h`.  A new exact triangle
control tests whether the two sectorwise maps can nevertheless share one
bounded physical update on the same matter edge.

For even `h=0` and odd `h_01=1`, the separately signed edge FSWAPs each have
zero intertwining residual.  Least-squares fitting one operator on the same
three-qubit matter-edge/gauge-edge support to both equations has best joint
residual `2`.  A single exact update exists only after adding the
Wilson-controlled projector:

```text
G_joint = P_even G_even + P_odd G_odd,
```

which has zero residual in the triangle control.  On the actual torus the
controlling Wilson support has weight `3L`.  The alternative is to write the
position of the odd representative's membrane into the gate table.  That is a
preferred membrane/host sign, not a bounded covariant physical law.

Therefore the Cycle-245 sectorwise maps do not join into one bounded
**single physical update** without a Wilson-controlled projector or a supplied
membrane-position sign.  Parity doubling sends both original parity sectors
to locally even combined occupations, so it avoids this particular
even-versus-odd `h` split.  It does not avoid the distinct actual-graph CAR
locality residual proved in Section 2.

## 7. Direct comparison with the Cycle-247 rough-terminal sector

Cycle 247 and this cycle close complementary halves of the compiler interface;
their auxiliary factors are not the same resource under different names.

| property | Cycle-247 rough terminal | Cycle-248 per-mode spectator |
|---|---|---|
| locally enforced code exponent | `7N-1` versus target `6N` | exactly `6N` after `6N` equalities |
| extra logical sector | `N-1` rough-boundary logicals | none on the equality code |
| both original matter parities | yes | yes |
| bounded exact even-CAR stream algebra | yes | no for the endpoint-copy image on the actual graph |
| bounded state isometry with image equal to declared code | not constructed | yes |
| mass/contact/rank-73 state domain | firewalled by missing image selector | algebraically present, but full stream still nonlocal |

The Cycle-247 excess is an **auxiliary rough-boundary/gauge-code
multiplicity**: its exact bounded even-algebra representation remains lawful in
the oversized locally enforced code, but no bounded constraints or preparation
select the required `6N`-dimensional image.  This note does not strengthen that
description into a claim that the `N-1` logicals are physically pure gauge;
that quotient is precisely what Cycle 247 did not construct.

The Cycle-248 spectator factors are different.  They are locally slaved to the
matter occupations, so they add no logical multiplicity on code.  If the exact
homomorphism `phi` is retained, original fermion exchange is retained too, but
its actual-graph image is nonlocal.  If the parity prefix is deleted to obtain
endpoint-only local gates, the auxiliary does not become a harmless gauge
sector: it changes the exchange representation.  Disjoint local pair creators
commute as hard-core bosons, and the nonadjacent FSWAP residual is
`2 sqrt(2)`.  Therefore the spectator's “extra sector” is either constrained
away or becomes off-code leakage; it is not the `N-1` rough gauge
multiplicity.

The natural synthesis target is consequently sharp: use Cycle 247's exact
bounded even-algebra action while replacing its `N-1` boundary multiplicity by
a bounded, locally prepared image selector.  Simply imposing Cycle-248-style
occupation equalities on the rough terminals is not licensed: Cycle 247
already found that local terminal-`Z` fixes and edge equalities leak under the
dressed stream.  A subsystem/non-diagonal selector or explicit local isometry
must be constructed and tested.

## 8. Supplied-structure and deletion inventory

Supplied here, not derived:

1. the choice to add one spectator per mode or one parity spectator per cell;
2. the data/spectator role distinction and their colocated pairing;
3. the local equality signs `+1` and the initial spectator-zero convention;
4. local `CNOT` preparation and any off-code unitary completion;
5. the six direction labels, square-pyramid graph, coarse-cell placement, and
   proper-cubic action inherited from Cycles 219, 230, and 235;
6. the Fock phase convention used to write `E` as an ordinary tensor matrix;
7. the endpoint exchange sign or equivalent local `CZ` correction;
8. any parity prefix, sign lane, Wilson projector, membrane representative, or
   edge-coloring schedule used by a repaired comparator;
9. the 15 face gauge factors when the Cycle-235 comparison census is quoted;
10. the coin parameter, contact coupling/order, sea phase cut, finite torus,
    rank-73 state, and seam sampling inherited from the predecessor fixtures;
11. the physical placement scale and macrocell convention; and
12. the distinction between compiler gate layers and physical temporal data.

Deletion controls:

- delete an equality: one spurious logical qubit is admitted;
- delete local spectator preparation: an original odd occupation is not in the
  equality code;
- delete spectator transport: equality leakage norm is `sqrt(2)`;
- delete the compensating exchange sign: doubled FSWAP residual is `2`;
- delete the logical parity prefix on a nonadjacent actual edge: residual is
  `2 sqrt(2)` and local odd images commute as hard-core bosons;
- delete per-cell endpoint parity updates: leakage norm is `sqrt(2)`;
- delete the Cycle-245 Wilson control while demanding one two-sector update:
  best residual is `2`; and
- delete contact (`g=0`): the declared interaction becomes identity, while the
  free/mass fixtures remain.

No deletion is described as a Record operation.  Copying an occupation into a
spectator is not a Record.

## 9. Prior-art and novelty boundary

This cycle directly compares against the Haegeman state-gauging engine already
bounded in Cycle 245 because the `h`-dependent single-update issue is an input
to this discriminator.  It does not extend that engine or treat it as the
default framework.  Cycle 235's higher-form construction supplies the actual
square-pyramid graph and the even-sector boundary.  No external result is used
to claim the spectator construction closes.

Fixture-specific new work is limited to:

- the per-mode and per-cell spectator isometries on the Cycle-230/235 census;
- exact code-homomorphism, local-`B_t`, preparation, equality-rank, leakage,
  and deletion controls;
- the isolated two-mode doubled exchange repair and its three-mode
  nonadjacent-edge falsifier;
- `L=3,4,5` plus held-out `L=6` overhead and exact-string scaling;
- rule-family versus canonical-state covariance separation; and
- the exact two-sector/local-chain proof that Cycle 245 needs a nonlocal
  Wilson control for one common update; and
- the explicit separation of Cycle-247 rough-boundary multiplicity from the
  spectator route's exchange-changing local shortcut.

## 10. No-go discipline N1–N8

The claim under stress is narrow: **the two displayed spectator-copy routes do
not yet provide a bounded, canonical, actual-graph full-Fock compiler.**  It is
not a claim that all local fermion encodings are impossible.

### N1 — alternative-route enumeration

At least five materially distinct routes were kept separate:

| route | marker | result |
|---|---|---|
| per-mode occupation copy with local equality constraints | **ATTEMPTED** | exact full-state isometry and exact code algebra; even the fixed-sector-shortened hopping weight grows as `6L^2+4` |
| one cell-parity spectator with one equality | **ATTEMPTED** | exact coin/contact and state rank; changes the Cycle-235 gauging graph |
| one shared cell spectator constrained to all six mode vertices | **ATTEMPTED** | rank six constraints leave one logical qubit; five logical qubits deleted |
| data FSWAP plus ordinary spectator SWAP sign lane | **ATTEMPTED** | exact for isolated two modes; residual `2 sqrt(2)` for a nonadjacent graph edge |
| double FSWAP with local endpoint `CZ` correction | **ATTEMPTED** | exact for isolated two modes; same nonadjacent residual |
| exact code homomorphism with logical/Jordan–Wigner prefix | **ATTEMPTED** | exact CAR and stream; the favorable fixed-sector-shortened support is `6L^2+4`, already violating bounded support |
| parity-doubled matter followed by Cycle-235 face gauging | **ATTEMPTED** | combined charge is locally even; no bounded physical gauge-state map or exchange dictionary constructed |
| Cycle-245 even/odd sector direct sum with one Wilson-controlled update | **ATTEMPTED** | exact only with a weight-`3L` Wilson control or preferred membrane sign |
| Cycle-247 rough terminal plus a local image selector | **LIVE, PARTLY ATTEMPTED** | bounded even algebra is exact; tested terminal-`Z`/edge-equality selectors leak, while subsystem/non-diagonal selectors remain live |
| local Majorana-edge/subsystem or graded-tensor encoding | **LIVE, NOT RULED OUT** | not instantiated by spectator occupation copying |
| autonomous dynamical gauge/link fermionization | **LIVE, NOT RULED OUT** | may store exchange signs locally in link flux; preparation and covariance remain to be built |

The two live constructive classes alone forbid a route-independent no-go.

### N2 — condition-independence audit

The residual conditions are:

- `K_CAR`: a bounded actual-graph image for the required even CAR stream
  algebra, not only isolated endpoint truth tables;
- `K_sym`: one canonical physical translation/proper-frame representation
  intertwining the code without a growing sign lane; and
- `K_gaugeprep`: locally lawful auxiliary/gauge state preparation and
  preservation without global sector/reference input.

Pairwise independence is tested by the constructions already present:

| pair | one can close without the other? | witness |
|---|---|---|
| `K_CAR`, `K_sym` | yes | a fixed-order exact prefix closes CAR algebraically while failing bounded/canonical symmetry; rule templates are frame covariant while CAR locality fails |
| `K_CAR`, `K_gaugeprep` | yes | local CNOT equality preparation closes the spectator code while nonadjacent hopping fails; an algebraic JW image closes hopping while no gauge preparation is supplied |
| `K_sym`, `K_gaugeprep` | yes | the equality family and preparation are all-frame covariant as descriptors, while canonical fermionic state signs fail; supplying a sign representation says nothing about autonomous preparation |

They are not one renamed premise.  None is promoted to constitutional content.

### N3 — hidden-condition scan

The hidden-condition scan explicitly searched: global parity queries; chosen
Fock order; boundary charge; Wilson sector; membrane representative; selected
origin; port/direction labels; background gauge state; spectator-zero
preparation; off-code unitary completion; schedule/edge coloring; use of two
different sector updates; ignored middle occupations; forbidden leakage;
finite-size-only support; phase reference; physical clock; energy zero; and
source/stress data.  The order, sign lane, preparation, schedule, macrocell,
and gauge-state obligations remain in the supplied inventory.  No global
spectator parity or reference preparation is silently used.

### N4 — residual matching

The current residuals match, rather than overwrite, the predecessor boundaries:

| predecessor evidence | predecessor residual | Cycle-248 match |
|---|---|---|
| `SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md:34-56,109-115` | intrinsic six-mode CAR update exists, but `M_64` coarse cell is not an `M_2` physical-site compiler | exact spectator state code and onsite gates are supplied; actual-graph stream still fails bounded physical support |
| same file `:59-65,206-230` | rank-73 sea and phase cut are supplied, not physically selected | the odd state is retained by `E`, but no sea selector or completed physical stream is claimed |
| same file `:87-106,298-315` | contact seam is a generator fixture, not probability/rate/energy | seam block is conditionally inherited only; the rate/energy firewall is unchanged |
| `EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md:35-56` | actual graph has six mode 3-cells and 15 face factors per cell | all spectator rank and edge controls use that graph and census |
| same file `:66-108` | closed face code carries total-even sector only and misses one-particle/rank-73 states | spectator copying retains both original sectors but does not inherit a local face-gauge compiler for free |
| same file `:255-279` | all-frame macro placement passes while unit physical translation remains supplied | this cycle separates covariant local descriptors from canonical state covariance and does not claim unit-site closure |
| same file `:281-307` | even update operators are local in the gauge algebra, but odd state fixtures are absent | the state absence is repaired algebraically; the exchange locality residual replaces, rather than erases, the compiler wall |
| `HAEGEMAN_PARITY_SECTOR_GAUGING_CYCLE245_NOTE_2026-07-17.md:35-82,61-69` | ordinary qubits retain CAR strings; direct-sum sectors use different `h` signs | fixed-sector-shortened `6L^2+4` doubled strings and best common-update residual `2` confirm both boundaries |
| same file `:240-318` | local coin/contact images exist; actual CAR hopping retains a growing matter interval | spectator coin/contact pass; the three-mode control rejects the endpoint-only shortcut |
| `LOCAL_ROUGH_PUNCTURE_ODD_SECTOR_CYCLE247_NOTE_2026-07-17.md:37-57,177-245,289-305` | rough terminals give an exact bounded even algebra with both parities but retain `N-1` boundary logicals and no image selector | spectator equalities close state rank without gauge multiplicity, but their local exchange shortcut fails; the two constructions are complementary, not equivalent |

### N5 — resolution/rhetoric audit

Every retained negative statement states its tested resolution:

- isolated two-mode doubled gates: exact residual `0`;
- nonadjacent three-mode intertwiner: Frobenius residual `2 sqrt(2)`;
- deleted exchange sign: residual `2`;
- favorable fixed-sector-shortened hopping support: `58,100,154,220` at
  `L=3,4,5,6`;
- plain three-mode symmetry action: residual `2 sqrt(2)`;
- supplied sign-lane symmetry action: residual `0`;
- separate Cycle-245 sector updates: residuals `(0,0)`;
- best one bounded same-edge update for both sectors: residual `2`;
- Wilson-controlled update: residual `0`; and
- fixture seam singular range: `[0.9998884863600149,1.0]`.

The prose uses “this route,” “the displayed maps,” and “not yet” where
appropriate.  It does not turn growth at four sizes into a theorem about all
encodings.

### N6 — partial-closure paths

Retained partial closures are real and reusable:

1. the equality code solves the global parity/reference-state loss that hit
   the closed Cycle-235 and standard Cycle-245 maps;
2. local preparation and local `B_t` solve the spectator reference bus issue;
3. onsite coin, mass, contact, and seam algebra are exactly inherited;
4. spectator transport and the endpoint exchange correction are necessary
   components of any completed route; and
5. the Cycle-245 one-update audit identifies the exact Wilson control that a
   local repair must replace.

Live completion paths are auxiliary Majorana/link degrees of freedom, a
subsystem/superfast encoding adapted to the square-pyramid graph, a genuinely
dynamical local gauge field carrying exchange flux, or a graded physical
tensor action with an explicit `M_2` realization.  None is ruled out by the
spectator-copy residual.

### N7 — steelman

The strongest hostile reading is that the campaign only needs one even update,
not local odd creation operators, and that fermionic statistics can be encoded
by the local endpoint `CZ` accumulated during motion.  Under that reading the
per-mode map looks like a complete 12-site compiler: state preparation is
local, the code has the right dimension, coin/contact are onsite, and every
individual stream edge has a four-factor gate.

The exact three-mode test is the decisive answer to that steelman.  On a graph
with a nonadjacent edge, the endpoint gate does not intertwine the same
intrinsic Fock update; basis states with an occupied intermediate mode acquire
the wrong sign.  Selecting a different ordering can make one edge adjacent but
cannot make all edges of the branching Cycle-235 graph adjacent.  The exact
prefix repairs the sign and reproduces the update, but even its
fixed-sector-shortened support grows as `6L^2+4`. Conversely, this only
defeats the endpoint-copy compiler;
a link-flux or subsystem encoding could answer the steelman differently.

### N8 — cross-cycle echo

- Cycle 230 opened the `M_64`-to-physical-`M_2` compiler wall.
- Cycle 235 localized the even CAR algebra but exposed the closed odd-sector
  loss.
- Cycle 241 showed that rank completion and common-Wilson labels do not by
  themselves give an operator/state compiler.
- Cycle 245 showed that ordinary retained matter qubits keep the CAR string and
  that sectorwise maps can disagree on the physical update sign.
- Cycle 247 closed the bounded even stream algebra with rough terminals while
  leaving `N-1` auxiliary boundary logicals and no state-image selector.
- Cycle 248 repairs the state-rank/reference problem with local spectators,
  then independently reproduces the CAR-locality wall and proves the
  two-sector single-update mismatch in a minimal exact control.

This is a cross-cycle echo of one unresolved interface, not route-independent
constitutional evidence.  Majorana/subsystem/dynamical-gauge routes remain
live.  Therefore the audit ends with no broad no-go and no axiom pressure.

## 11. Dependency ledger and next route

| wall | Cycle-248 change | residual |
|---|---|---|
| `C_ref` | genuine gain: local spectator preparation retains odd states with no global parity/reference charge | Fock phase convention, coarse placement, sea phase cut, and any gauge background remain supplied |
| `C_num` | genuine gain: full `6N` logical exponent with `6N` local equalities; original rank 73 becomes combined-even | why charge is doubled and how physical matter number is selected remain open |
| `C_wrap` | unchanged | no clock, rate, physical energy, or realized winding history is derived |
| `C_int` | conditional gain: coin/contact and seam algebra intertwine on the state code | no bounded actual-graph full update, transition probability, or interaction selection |
| `C_local` | gain plus discriminator: local state code, constraints, preparation, onsite update, transport necessities | even fixed-sector-shortened stream/CAR support grows as `6L^2+4`; canonical state covariance is not closed |
| `C_source` | unchanged | no energy density, stress, gravity source, or resource accounting derived |

The optimal next constructive route is the **Cycle-247 rough-terminal algebra
plus a subsystem/non-diagonal local image selector**, because that starts from
the only current route that already closes the actual-graph even algebra.
The selector must remove exactly `N-1` boundary logicals without leaking under
the dressed stream and must provide a bounded preparation/isometry.  If that
fails, the next comparator is a square-pyramid-graph local Majorana/link or
subsystem compiler in which the sign missed by the three-mode test is stored
on bounded incident links.  Either route must immediately test: exact full-code
dimension; one physical `G`; all-24 frame group composition; `L=3,4,5` plus
held-out `L=6`; one-particle/rank-73 state tests; and local
preparation/leakage/deletion controls.  No route-independent conclusion is
licensed until these live classes are actually attempted.

## Time firewall

`E`, preparation depth, gate order, edge coloring, FSWAP layers, Wilson
projectors, and compiler schedules are algebraic/compiler coordinates.  None
is causal time, proper time, physical frequency, physical energy, a generator
rate, a Record, or realized history.  Wrapped phase is not called physical
energy; a generator element is not called a rate; spectator copying is not
called a Record; and this coarse CAR state code is not called a completed
physical-site compiler.

## Executable artifact

```text
scripts/parity_doubling_spectator_compiler_cycle248_2026_07_17.py
```

The runner checks the note contract, exact isometry/homomorphism, local `B_t`,
CAR versus hard-core pair creators, two-mode and nonadjacent three-mode
exchange, spectator transport, per-cell rank, coin/contact, deletion/leakage,
one-particle mass, rank-73 seam, `L=3,4,5,6` census and support growth,
translations, all 24 proper-cubic frames, and the Cycle-245 single-update
Wilson control.
