# Arbitrary-size/root-free cutoff and gauge-preparation tournament — Cycle 598

Date: 2026-07-22

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, audit-status, or PR-control surface changes.

## Result up front

Cycle 598 separates and constructively moves all three Cycle-593 imports, but
does not retire them simultaneously.

1. For every declared finite box, choosing `k(L)` as the least prime strictly
   above `6L^3` makes the modular Gauss cutoff exact. L7 uses `k(7)=2063`, so
   the Cycle-593 alias is gone. The exact price is three
   `ceil(log2(k(L)))`-M2 link words per cell: per-cell overhead grows as
   `9 log2(L)+O(1)`, and the cubic-fixed root remains.
2. Three mobile capacity/anti-charge carrier species remove both the root and
   growing modulus. Their local bind/co-hop law is translation covariant and
   proper-cubic covariant, and the coherent one-particle mass fixture has exact
   intertwiner residual below numerical roundoff. But exactly one carrier of
   each species is still a supplied global sector. A remote duplicate-species
   N4 word passes every declared bounded local check.
3. A nearest-neighbour spanning-tree circuit is an exact affine bijection from
   uniform chord registers to the full uniform gauge fiber. This retires
   “preparation supplied” only relative to a supplied root, tree, postorder,
   blank accumulators, and exact prime-qudit Fourier gates; its depth grows
   with volume. Root-free local plaquette moves are translation/all24
   covariant, but preserve both malformed Gauss syndrome and three harmonic
   winding coordinates, so they are a sector uniformizer rather than a full
   autonomous pure-state preparer.

Thus the strongest exact construction is an arbitrary-finite-size physical
compiler family with explicit logarithmic resource scaling. It is not a
constant-overhead arbitrary-size compiler. The strongest root-free result is
a locally conserved prepared carrier sector, not locally generated capacity.
No route-independent obstruction survives the positive partial closures, and
there is no axiom pressure.

## Target contract and inherited shore

```text
Target:
  retire Cycle593's L6-selected modulus, cubic-fixed root/background,
  and supplied uniform gauge-fiber preparation

Required probes:
  A  size-indexed k(L)>6L^3 with literal M2 scaling
  B  three mobile anti-charges / translation-covariant neutral reservoir
  C  autonomous local gauge-code / uniform-fiber preparation

Train: L3
Held: L6
Held-out size: L7
Arithmetic: exact integer/modular, numeric tolerance 5e-9 only for inherited fixtures
Caps: 360 seconds, 3 GiB maximum RSS

Forbidden weakenings:
  growing w(L) called constant overhead
  conservation of a prepared carrier count called unique genesis
  a scheduled circuit called autonomous dynamics or physical time
  classical plaquette mixing called a pure uniform-fiber isometry
  gauge preparation called local constraint enforcement
  flux called energy, stress, source, or gravity
```

The executable pins accepted Cycle 593 at commit `70a1c54281`, including its
runner, receipt, cold transcript, and accepted post-run note appendix. It
inherits the Cycle-590 physical square, one-particle mass, local contact, and
Cycle-230 seam fixtures through that shore. The matter/contact law and the
53-M2-per-cell physical compiler are not changed.

## Route A — size-indexed prime Gauss family

For a periodic box of linear size `L`, define

```text
V(L) = L^3
Nmax(L) = 6 L^3
k(L) = least prime strictly greater than Nmax(L)
w(L) = ceil(log2(k(L))).
```

Keep the Cycle-593 three root spectator bits and fixed background `-3`, and
replace every `Z_1297` link by `Z_k(L)`. The local equation remains

```text
div f(x) = q_x + (S-3) delta_(x,root) mod k(L).
```

Periodic telescoping gives `N+S-3=0 mod k(L)`. Because
`0 <= N <= 6L^3`, `0 <= S <= 3`, and `k(L)>6L^3`, the next congruent value
after 3 is larger than the full `N+S` range. Therefore only

```text
(N,S) = (0,3), (1,2), (2,1), (3,0)
```

is admitted for every declared finite `L`.

The executable checks the complete `(N,S)` range on:

| split | L | capacity | k(L) | w(L) | extended physical M2 |
|---|---:|---:|---:|---:|---:|
| train | 3 | 162 | 163 | 8 | `77*27+3 = 2,082` |
| held | 6 | 1296 | 1297 | 11 | `86*216+3 = 18,579` |
| held-out size | 7 | 2058 | 2063 | 12 | `89*343+3 = 30,530` |

The layout is literal: the inherited compiler owns 53 M2/cell, each cell adds
three `w(L)`-M2 outgoing flux words, and the root owns three spectators. The
runner allocates every fine-lattice coordinate, records the new-role layout
hash and maximum support radius, and tests wire injection under all 24
proper-cubic frames and all 576 frame products.

The largest root Gauss projector reads `6w(L)+9` M2 (six incident words, six
matter bits, three spectators); a non-root check reads `6w(L)+6`. A crossed
link update reads `w(L)+2` M2. Thus the exact root/update supports are
`57/10`, `75/13`, and `81/14` M2 on L3/L6/L7 respectively; support in physical
M2 as well as storage grows with `L`.

The signed-current link recurrence is unchanged:

```text
j_xa = n_(x,+a) - n_(x+e_a,-a)
f_xa <- f_xa - j_xa mod k(L).
```

Every link word and both current controls are exhaustively invertible for each
tested modulus. L3/L6/L7 Gauss words remain lawful through stream/inverse, and
the update commutes with all 24 frames. The Cycle-593 every-code-word argument
therefore applies at each `k(L)`: onsite mass/contact preserve charge, stream
translates a lawful flux fiber bijectively, and linearity gives exact
`E G = G_physical E` on the declared gauge code.

Deleting the crossed-link flux update creates a two-site Gauss syndrome at
every tested size. Invalid binary labels are locally rejected, and the fixed
root translation test supplies an independent malformed-law control.

This closes the L7 alias, but not the original constant-overhead target:
`w(L)=3 log2(L)+O(1)`. A materially independent CRT comparator reaches the
same boundary. Simultaneous Gauss checks in the first coprime clock factors
separate the finite train/held boxes when their product exceeds `6L^3`; a
fixed factor catalog aliases, while an expanding factor catalog grows the
aggregate link width.

The root audit is also explicit. Proper-cubic frames fix the selected root,
but a one-cell translation of matter and links while the background remains
at the root creates two nonzero Gauss syndromes. Route A is not translation
covariant with a fixed root.

## Route B — root-free mobile capacity carriers

Each cell owns one four-M2 word for each of three species. Its valid labels
and rejected interval are exactly:

```text
0       absent
1       inactive neutral carrier
2..7    carrier bound to one of the six local matter directions.
8..15   rejected malformed labels
```

A bounded cell check says that every occupied matter mode has exactly one
bound species and every bound species has its named matter mode. A bound
carrier contributes a local `-1` bookkeeping anti-charge; an inactive carrier
is neutral. The matter and its carrier co-hop, while onsite direction changes
co-rotate the carrier label. No root, background delta, modulus, parity
ordering, global count query, or runtime frame query appears in the local
table.

Relative to exactly one prepared word of each species, at most three matter
occupations exist. Local reversible co-hop conserves those counts on L3, L6,
and L7. The runner tests every torus translation, all 24 proper-cubic frames,
and all 576 frame products, with zero residual. Persistent overhead is twelve
M2/cell, so held L6 has `65*216 = 14,040` M2. The runner allocates all twelve
carrier M2 per cell on the fine lattice, records the coordinate hash and
support radius, and checks transported-layout injection and group laws.

The coherent matter audit is positive but scoped. For the accepted held
`beta=-0.3` six-ray massive coin, encode a one-particle state into the uniform
superposition over the three unobserved species labels. The physical labeled
coin is three identical blocks. The isometry, mass-coin intertwiner, and all24
embedding-covariance residuals are numerical zero. The accepted local contact
phase is label-independent, and the seam permutation co-transports the bound
word, so those basis fixtures lift exactly.

This is not yet the complete indistinguishable many-body lift. More directly,
unique genesis is not locally enforced: four separated particles labeled
`(0,1,2,0)` pass every cell check, while species counts are `(2,1,1)`. Deleting
a carrier hop creates a local mismatch, and an off-grid word is rejected, but
neither control repairs the duplicate. Conservation preserves a supplied
sector; it does not generate that sector.

## Route C — uniform-fiber preparation

### C1: reversible affine tree preparer

For a connected periodic lattice over `Z_k`, choose a nearest-neighbour
spanning tree. There are `E=3V` link words, `V-1` tree links, and
`E-V+1=2V+1` chord registers. Initialize every chord register in the uniform
`Z_k` state. For each chord assignment, compute the residual local charge,
aggregate it from leaves to the root, and write the unique tree flux that
solves Gauss. Reverse the aggregation and clear the vertex accumulators.

The chord-to-flux map is an affine bijection. Hence the output is the exact
pure uniform superposition over all `k^(2V+1)` solutions, and signed-current
translation preserves the exact Cycle-593 matter-only intertwiner. The runner
samples 24 chord assignments at each L3/L6/L7, obtains zero Gauss residual,
and recovers every chord word exactly. Deleting one nonzero written tree edge
creates an endpoint Gauss syndrome at every size.

The literal resource and recurrence are:

```text
link storage:             3 w(L) M2/cell (already in Route A)
temporary accumulators:   w(L) M2/cell
maximum modular gate:     2 w(L) M2 support on neighboring words
scheduled word operations <= 14 L^3 + 3(L^3-1)
depth upper bound:        D(L) <= 14 L^3 + 3(L^3-1)
```

This circuit is exact preparation, but it is not autonomous or root-free.
The root, tree, postorder, blank work words, compile schedule, and exact
`k`-point Fourier gate embedded in binary M2 are supplied. Schedule is not
time.

### C2: local plaquette cooling/uniformization proxy

Adding an oriented elementary plaquette boundary touches four local links and
preserves Gauss exactly. The family of all such moves is translation
covariant; the executable tests every translation, all 24 proper-cubic
frames, and all 576 products on L3/L6/L7. Its physical support is `4w(L)` M2:
32, 44, and 48 on the three tested sizes.

On a three-torus the divergence-free link space has dimension `2V+1`, while
contractible plaquette boundaries span dimension `2V-2`. The remaining three
coordinates are harmonic winding sectors. Plaquette moves preserve those
coordinates exactly. They also preserve any malformed Gauss syndrome rather
than repairing it. A local random plaquette law can therefore uniformize a
lawful supplied sector, but it cannot by itself prepare the full pure uniform
fiber from blank or correct off-code input. The displayed single-tracer gap
proxy `1-cos(2 pi/L)` also shrinks with size; it is only a comparator, not a
broad mixing no-go.

Deleting three of the four plaquette legs leaves the explicit one-link
malformed word and creates two Gauss-syndrome endpoints. Valid modular updates
cannot leak to the rejected binary-label interval.

Preparation is not enforcement. A local constraint defines the lawful code;
a tree circuit or cooling proxy is a separate mechanism for reaching a state
inside it.

## Route dispositions

| route | disposition | exact gain | remaining import |
|---|---|---|---|
| A prime Gauss | pass as scoped compiler | arbitrary finite L, L7 alias removed, exact E/G, winding recurrence, all24/576, literal layout | logarithmic per-cell words; fixed root/background |
| A-CRT comparator | pass as scaling audit | independent finite-product exact separator | fixed product aliases; growing catalog grows width |
| B mobile carrier | pass as scoped root-free sector | constant overhead, all translations, all24/576, coherent N1 mass and basis contact/seam lifts | exactly-one genesis and full N<=3 indistinguishable coin lift |
| C1 tree preparer | pass as exact scheduled preparation | pure uniform fiber by affine bijection | root/tree/order/Fourier gates and growing depth |
| C2 plaquette proxy | pass as scoped local uniformizer | root-free local covariance and exact Gauss preservation | harmonic sectors, syndrome repair, pure-state preparation |

No individual route meets arbitrary-size, root-free, constant-overhead,
locally generated capacity, and autonomous pure preparation simultaneously.
That is unfinished construction across separable imports, not a shared
substrate obstruction.

## Supplied / derived / open inventory

Supplied:

- accepted Cycles 219/230/560/563/569/590/593 matter and physical compiler;
- periodic L3/L6/L7 geometry and compile-time `L`;
- Route-A prime selection, binary label convention, fixed root/background,
  root spectator preparation, local check coefficient, and exact gates;
- Route-B exactly-one-carrier-per-species sector and unused-carrier state;
- Route-C tree, root, postorder, blank accumulators, chord Fourier states, and
  modular arithmetic gates;
- plaquette update law, lawful initial syndrome/harmonic sector, numeric caps.

Derived:

- exact complete-range cutoff for L3/L6/L7 and `k(7)=2063`;
- exact `w(L)`, invalid-label counts, physical M2 layout, role hashes, radii,
  local support, inverse, all24 and all576 checks;
- fixed-root translation-syndrome falsifier;
- CRT factor/product/word-width comparator;
- root-free twelve-M2/cell carrier table, co-hop/inverse/deletion/off-grid tests,
  every-translation and proper-cubic covariance;
- coherent one-particle massive-coin carrier isometry;
- exact chord-to-fiber affine bijection, fiber cardinality, schedule recurrence,
  and sampled inverse;
- plaquette Gauss/winding/syndrome invariants and size-dependent gap proxy;
- fresh five-attempt N1-N8 audit.

Open:

- fixed local-alphabet arbitrary-size cutoff with constant M2/cell;
- local unique genesis of exactly three mobile capacity carriers;
- full antisymmetric N<=3 carrier lift of the six-mode massive coin;
- root-free, autonomous, pure uniform-fiber preparation;
- autonomous preparation of the three harmonic sectors and coherent repair of
  arbitrary malformed Gauss syndromes;
- noise, continuum/thermodynamic and Lorentz limits;
- empirical energy, stress, source, gravity, Born, or actuality laws.

## Six-wall ledger and maturity

| wall | movement | residual |
|---|---|---|
| `C_ref` | root/background removed on the prepared mobile-carrier sector | local unique carrier genesis open |
| `C_num` | `k(L)>6L^3` removes every finite-size alias, including L7 | prime/CRT words grow; empirical units open |
| `C_wrap` | every prime family is recurrent under winding | preparation leaves three harmonic sectors supplied |
| `C_int` | mass/contact/seam survive; coherent N1 carrier coin closes | full indistinguishable N<=3 carrier coin open |
| `C_local` | arbitrary-finite local enforcement and exact scheduled preparation both constructed | constant overhead plus root-free autonomous preparation not joined |
| `C_source` | background/carriers made explicit as capacity bookkeeping | not energy, stress, source, gravity, or a source law |

Evidence-planning maturity remains operational quantum/Records `4.80/5`
repository and `4.65/5` strict; causal time `3.95/5` and `3.80/5`;
inertia/matter `4.90/5` and `4.93/5`; gravity/source `4.10/5` and `3.85/5`;
Born/probability `4.20/5` and `3.65/5`. These are planning coordinates, not
probabilities, audit grades, or constitutional status.

## Fresh N1–N8 no-go discipline

### N1 — normalized alternatives

Five materially distinct families are attempted, each normalized by primary
object, mechanism, and terminal obligation: size-indexed prime Gauss words;
finite-product CRT Gauss words; mobile capacity carriers; reversible affine
tree preparation; and local plaquette cooling/uniformization. A sixth local
Gauss-projector/decoder family remains live and untested. No notation variant
is counted as a separate attempt.

### N2 — directional wall independence

All 28 directional pairs among size-uniform word, root-free reference, unique
carrier genesis, coherent many-body lift, pure uniform preparation, autonomous
bounded-depth control, harmonic coverage, and malformed-syndrome repair are
recorded. Closing any one does not automatically supply the named mechanism
for another.

### N3 — hidden-condition scan

The compile-time size/prime, root/background, exactly-one carrier sector,
tree/root/order, blank accumulators, prime-qudit Fourier gates, lawful
plaquette seed, fixed syndrome, and harmonic sector are all promoted to
explicit supplies. No “standard” or “obvious” step hides them.

### N4 — residual matching

The L7 alias residual exactly matches Cycle 593 and is closed by `k(7)=2063`.
The root residual is closed only on the supplied carrier sector. Gauge
preparation is closed only by the scheduled tree circuit; autonomy/root freedom
remain. Cycle-563 parity/order and older CAR decoder walls are not reused as
obstruction witnesses.

### N5 — rhetoric resolution

Every negative is family-specific: this binary prime/CRT implementation has
growing words; this carrier table admits a remote duplicate; this tree circuit
has growing scheduled depth; these plaquette moves preserve syndrome and
winding. None is generalized to every fixed-alphabet code, mobile reservoir,
preparer, or local dissipative law.

### N6 — partial-closure paths

Live paths are a topological/local-defect genesis rule for three carriers; the
full antisymmetric N<=3 carrier compiler; autonomous harmonic registers plus
coherent defect routing; and hierarchical fixed-alphabet counters. They are
constructive import-retirement programs, not automatic axioms.

### N7 — hostile steelman

A hostile reviewer should reject a shared obstruction. Route A closes every
finite size if logarithmic words are allowed. Route B closes root and
translation covariance if a three-carrier sector is prepared. Route C closes
exact pure-fiber preparation if a tree schedule and Fourier gates are allowed.
Those positive partial closures show that the imports can move independently.

### N8 — cross-cycle echo

Cycles 560, 563, 590, and 593 repeatedly retired one host/global import while
exposing the next. Cycle 598 repeats that constructive pattern: the L7 alias,
root choice, and preparation supply are separately movable. Their present
conjunction is not constitutional evidence.

Broad no-go, minimum-content, shared-obstruction, and axiom-pressure claims:
**DO NOT SHIP**. There is no axiom pressure.

## Interpretation firewall and next campaign

- Schedule is not time.
- Flux is not energy, stress, source, or gravity.
- Mobile anti-charge is capacity bookkeeping, not empirical charge.
- Preparation is not enforcement.
- Conservation is not unique genesis.
- A classical uniform mixture is not a pure uniform-fiber isometry.
- Proper-cubic and translation covariance are not Lorentz covariance.
- Arbitrary finite size with growing words is not constant overhead.
- Exact N<=3 enforcement is not complete N4 dynamics.

The optimal next campaign is to compile the complete antisymmetric N<=3
massive coin/contact/stream lift on the root-free carrier sector and attack
unique three-carrier genesis with a translation-covariant topological or
local-defect mechanism. In parallel, replace the tree schedule by coherent
syndrome routing plus autonomous harmonic-sector preparation.

## Independent parent reproduction

The worker-frozen four-path bundle had SHA-256 values
`89c733e3be55ec287e338c4d9ed6062ec8cb222345ff72596662c43b3f1ae6a5`
(runner),
`8938c4d0392c3e99b79b43b3fe723b0ee107430f4a0620f9e8f1bbc7dedca700`
(note before this appendix),
`d5a47bf415883fdf95e2faf0c74f4e8b0e2caa7b75c8fc504f89e984834f19b6`
(receipt), and
`19811196cdedba8ebea3607e6a38ab3f83a5c68d6f264ceed795c13cb8fe44a9`
(cold transcript). The worker passed 7/7 checks in 39.66 external seconds
(38.860 internal), with 157,368,320 bytes maximum RSS, 145,769,024 bytes peak
footprint, and zero swaps.

The parent independently reran the frozen runner while redirecting only its
receipt to `/tmp/cycle598_parent_receipt_20260722.json`; the worker receipt and
transcript were not overwritten. It again passed 7/7 checks in 44.02 external
seconds (43.265 internal), with 151,322,624 bytes maximum RSS, 145,080,896
bytes peak footprint, and zero swaps. After removing only the expected
run-dependent `HEAD`, elapsed-time, and memory fields, the parent receipt is
byte-identical to the worker receipt. The independent transcript SHA-256 is
`c0665c35ba76767b917d49ba091de6cf03cc044890af9049c3aa87d1e778d3cd`;
the redirected receipt SHA-256 is
`6d9371d41643f1187cc8e24ac27ea4f03534fadc09c4facffa1db68e40a000eb`.
