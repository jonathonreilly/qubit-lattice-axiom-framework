# Gravity Route C — bounded direct density/current search

**Date:** 2026-07-17

**Type:** positive conditional construction plus bounded linear/PSD search

**Status:** `partial-attempt-with-named-untested-routes`

**Authority:** none

**Audit:** unset

**Constitutional effect:** none. This note does not edit or propose an axiom,
foundation clause, Qualification rule, primitive, registry, policy, queue, or
audit status. It creates no shared obstruction and no axiom pressure.

Companion runner:

```text
scripts/gravity_route_c_bounded_direct_current_search_2026_07_17.py
```

## Question

Within the smallest already available physical-M2 matter/contact code and
finite-coin mediator, can a proper-cubic, positive, phase-reference-robust,
additive local density and edge flux simultaneously:

1. obey exact local continuity;
2. preserve the one-particle mass fixture;
3. distinguish the ordinary Cycle-230 contact action at fixed total number;
4. compose independently and ignore spectator registers; and
5. match the Cycle-216 scalar source/response fixture?

The search is over a declared basis. It is not a classification of every local
Hermitian operator, action, auxiliary code, current, or time-dependent law.

## Result up front

There is a constructive direct current, but it does not contain the contact
action.

On the mapped even-CAR code, write

```text
n_(x,d) = (I-B_(x,d))/2,
N_x     = sum_d n_(x,d).
```

For an onsite number-preserving coin `C`, define the positive directed-edge
operator

```text
J_(x,d) = Gamma(C)^dagger n_(x,d) Gamma(C).
```

With the one-edge stream and the actual onsite
`W_g=exp(i g binom(N_x,2))`, the exact Heisenberg identity is

```text
G^dagger N_x G - N_x
  = sum_d [J_(x-e_d,d)-J_(x,d)].
```

The contact commutes with `N_x`, so it does not alter this identity. The same
formula holds for the six-direction finite-coin mediator, whose onsite carrier
embeds in three M2 sites. Numerical matrix residuals on the complete `L=3`
one-particle blocks are

```text
matter continuity residual:   1.2187194808943674e-15
mediator continuity residual: 1.4147177804096531e-15
matter residual after U -> exp(0.41 i)U:
                              1.7083776624986694e-15
```

The densities and edge operators are positive semidefinite up to eigensolver
roundoff below `3.4e-16`. Thus this is a phase-reference-robust positive norm/
number current, not the Cycle-228/229 chosen-reference deviation current.
Nothing here calls it physical energy or stress.

Multiplication by the supplied common-family mass

```text
m = 0.4534056541748852
```

gives an additive candidate mass/source charge. It is unchanged by a normalized
spectator and reproduces the Cycle-216 scalar Green response after the additional
identification `Q=mN` is supplied. It is blind to the Cycle-289 equal-total-`N`
contact branches: both receive `4m`, while their contact pair counts are `1`
and `6`.

The contact-sensitive part was therefore searched separately and then restored
to an explicit combined basis. In the proper-cubic, translation-invariant,
direction-blind diagonal two-body separation basis, every tested bounded
radius-1/2/3 positive contact-normalized candidate has a nonzero necessary
global-conservation residual. Odd held-out tori connect the full
separation-orbit graph and supply
a numerical row-space dual certificate. Even tori expose a second conserved
coordinate: global relative checkerboard parity. That escape uses arbitrarily
separated particle pairs and gives a cross-pair contribution when independently
composing two one-particle systems, so it is not a bounded additive density.

This is a narrow disposition of one direct static diagonal route. Off-diagonal,
direction-dependent, mediator-coupled, action-derived, auxiliary, and
micromotion currents remain live.

## Declared combined matter + mediator/contact basis

The search basis is

| symbol | physical code-space object | support/role |
|---|---|---|
| `M` | `m N_x` on the mapped matter even-CAR algebra | positive onsite density; radius-one number flux |
| `F` | six-direction mediator number on its 3-M2 code block | positive onsite density; radius-one number flux |
| `P_r` | cubic average of diagonal two-particle density at relative separation orbit `r` | 18 M2 per occupied cell; pair union 35--36 M2 through tested radii 1--3 |
| `K` | selected Cycle-216 `2I-U-U^dagger` finite-coin stiffness response | positive radius-one static-response coordinate at a supplied phase representative |

`M` and `F` are exact current blocks. `P_r` is the contact-sensitive search
block. `K` is included only to impose the existing static source/response
fixture; its continuity identity is not rederived and it is not renamed energy.

All six mapped `B_(x,d)` operators and their products commute with local checks
and Wilson operators. For `L=3,4,5,6`, the onsite support union is exactly 18
physical M2 sites, the adjacent two-cell union is 35, and the union over every
tested separation at Manhattan radii 1--3 is at most 36. Leakage is zero in
those controls. The six-mode mediator embeds in a three-M2 onsite block. The
complete density/source basis is invariant under all 24 proper-cubic frames;
directed logical fluxes transform by the corresponding direction permutation.
The runner does not instantiate that flux or the coin/stream update on the M2
code; physical-M2 current/update intertwining remains inherited rather than
freshly proved here.

The full matching coefficients would set

```text
(c_M,c_F,c_P,c_K) = (1,1,1,1).
```

The first two blocks then have zero continuity residual. On the training
`L=3`, radius-one block, `P` has normalized orbit-incidence residual
`0.38254602783800334`. At momentum `(0.41,-0.23,0.17)`, the selected scalar
stiffness response changes from `12.133172216206441` to
`41.05831967362574` under the projective rephasing `U -> exp(-0.4 i)U`.
Hence the exact contact-matching coefficient leaves a necessary
global-conservation residual, and
the exact static-response coefficient retains the phase-zero import. This is an
explicit four-component combined search, not an inference from separate
candidate slogans.

## Exact positive local continuity

Let `C_global` be the block-onsite coin and `S` the direction-preserving stream.
For the one-particle update `U=S C_global`,

```text
U^dagger N_x U
 = C_global^dagger S^dagger N_x S C_global
 = sum_d C_global^dagger n_(x-e_d,d) C_global.
```

Because `C_global` is onsite and number preserving,

```text
N_x = sum_d C_global^dagger n_(x,d) C_global.
```

Subtracting gives the displayed divergence identity. Second quantization
preserves the operator identity. The onsite Fock coin and actual contact have
commutator residuals below `3e-13` and `2e-15`, respectively, with local number.
No source schedule, clock rate, spectral logarithm, or phase zero enters this
current.

The same construction with the Cycle-215 field coin gives the mediator current.
The Cycle-214 source/pair vertex can exchange weight between its zero- and
one-field sectors, but its complete local density/current and connection to the
static `K` action were not included in this diagonal four-component search. That
is a live combined-interaction route, not negative evidence.

## Contact-sensitive linear/PSD search

### Basis and constraint

On the two-particle sector, let `o(r)` denote the proper-cubic orbit of relative
cell separation `r`, including periodic minimal-image reduction. The candidate
is diagonal:

```text
H_P = sum_pairs c_(o(x_2-x_1)) |x_1,d_1;x_2,d_2><...|,
```

with direction-independent coefficients. Radius `R` means `c_o=0` whenever
the minimal-image Manhattan distance of `o` exceeds `R`. Positivity is exactly
`c_o>=0`. Contact normalization is

```text
c_(0,0,0)-c_(1,0,0)=1.
```

The free two-particle update is the antisymmetric exterior square of the
Cycle-219 coin/stream. The actual contact gate is diagonal in this basis and
does not change the conservation constraint. Every nonzero exterior-square
matrix element from orbit `o` to `o'` contributes

```text
sqrt(w_(o,o')) (c_o-c_o') = 0.
```

These rows form the weighted incidence matrix `A`. `A c=0` is necessary for a
periodic local continuity equation because the sum of every edge divergence
vanishes.

### Results and held-out controls

The table reports the positive least-residual fit at contact normalization.
The displayed number is the normalized weighted orbit-incidence residual.  It
is a necessary global-conservation residual for this diagonal ansatz, not a
constructed cellwise-current residual.  The second beta `-0.35` is held out;
its values agree to the displayed digits.

| `L` | separation-orbit nullity | radius 1 | radius 2 | radius 3 | disposition |
|---:|---:|---:|---:|---:|---|
| 3 | 1 | 0.3825460 | 0.3440718 | 0.3277978 | every orbit connected |
| 4 | 2 | 0.2367429 | 0.1998961 | 0.1998961 | global relative-parity coordinate |
| 5 | 1 | 0.2304286 | 0.1923670 | 0.1913957 | every orbit connected |
| 6 | 2 | 0.1604714 | 0.1345584 | 0.1345584 | global relative-parity coordinate |

For odd `L=3,5`, the nullspace contains only the constant vector. The contact
difference vector

```text
d = e_(0,0,0)-e_(1,0,0)
```

is in the row space of `A`. The runner constructs `y` satisfying

```text
A^T y = d
```

with residuals below `3e-15`. Therefore `A c=0` implies `d^T c=0`, which is
incompatible with the declared `d^T c=1` contact matching. This is the dual
certificate for the stated finite orbit basis.

The runner also stacks the exact finite-support equations `c_o=0` outside
each declared radius with `A c=0`.  For every `L=3,4,5,6`, radius 1--3, and
both beta values, it constructs a row-space dual for the contact contrast with
residual below `8e-15`.  This stronger finite certificate excludes even signed
coefficients on those bounded finite domains.  It does not use odd wrapping to
make the even-size conclusion, and it still does not classify an infinite
lattice or construct a local flux.

For even `L`, the two components are relative checkerboard parity. Assigning
one to every even-separation pair and zero to every odd-separation pair is
positive, conserved, and contact sensitive. It is not a bounded-support
solution: its support extends across the complete torus/infinite lattice. It
also fails independent composition. Two isolated one-particle systems each
have zero pair value, while their union at an even separation receives one.
This is the explicit global-parity escape, not a contradiction hidden by the
finite search.

## Mass, composition, spectator, and contact controls

The candidate number charge gives

```text
one particle: m
two independent particles: 2m
Cycle-289 branch A, N=4: 4m = 1.8136226166995408
Cycle-289 branch B, N=4: 4m = 1.8136226166995408
```

The corresponding ordinary contact coordinates are

```text
g * pair_count = (0.37, 2.22),
difference      = 5g = 1.85.
```

Thus the number current preserves the one-particle mass fixture and independent
composition but does not encode the local contact action. Tensoring a normalized
spectator changes the one-particle charge by only `2e-16` in the runner.

## Static source/response fixture

After supplying

```text
Q_x = m N_x,
source vector = |s> = (1,1,1,1,1,1)/sqrt(6),
K = 2I-U-U^dagger,
```

the `L=11` zero-mean point source satisfies

```text
<s|K^+|s> = 3 L^+,
```

with position-space Green residual `3.9972584646685294e-15`. Doubling `Q`
doubles the response with zero numerical residual. This is exact matching to
the existing Cycle-216 fixture.

The source map remains supplied. The direct number current does not select
`Q=mN`, the static quadratic action, the coupling, the attraction sign, the
zero-mode subtraction, or the phase representative. In particular, the
displayed scalar inverse response changes under a `0.4` rephasing even though
the number current does not. The result therefore joins a phase-robust source
charge to a conditional selected-response fixture; it does not derive a
phase-robust complete gravity action.

## Supplied-structure inventory

The route supplies:

1. the Cycle-269 mapped even-CAR physical code and its macro-cell roles;
2. the six-direction matter and mediator coins;
3. `beta=-0.3`, the held `beta=-0.35`, and the common-family mass map;
4. the contact coupling `g=0.37` and coin/stream/contact order;
5. the direction-blind diagonal separation-orbit ansatz and radii 1–3;
6. periodic `L=3,4,5,6` boundaries and minimal-image orbits;
7. the identification `Q=mN`;
8. the Cycle-216 stiffness/action, phase zero, source vector, coupling, and
   zero-mode subtraction;
9. the prepared source and state used to evaluate the response.

No item is attributed to the scale-reference, kinetic-isotropy, or
realized-state primitive. The scale reference only converts a derived scale;
kinetic isotropy only supplies its registered OS0 form; realized-state
evaluation does not select a state, source, measure, or action.

## No-Go Discipline Gate

Gate disposition:

```text
general direct-current impossibility: FAIL — not claimed
narrow finite algebraic certificate: valid on declared ansatz/domains
  (not a separate N1–N8 PASS)
status: partial-attempt-with-named-untested-routes
```

### N1 — alternative-route enumeration

| route | marker | result |
|---|---|---|
| mapped number density/current | ATTEMPTED | exact positive, phase-robust local continuity; mass/source candidate; contact blind |
| bounded diagonal separation density, radii 1–3 | ATTEMPTED | nonzero positive orbit-incidence residual on `L=3..6`; bounded signed and odd full-basis dual certificates |
| global relative checkerboard parity | ATTEMPTED | conserves contact contrast on even/bipartite domains but is unbounded and fails independent composition |
| selected finite-coin stiffness `K` | ATTEMPTED AS RESPONSE CONTROL | matches static Green fixture but retains the supplied phase representative; its Cycle-228/229 current is not duplicated |
| off-diagonal even-CAR bilinear/quartic densities | OPEN / UNTESTED | may carry interaction coherence and evade the diagonal incidence certificate |
| direction-dependent cubic tensor densities | OPEN / UNTESTED | may use direction/separation intertwiners removed by the direction-blind scalar ansatz |
| two-slice micromotion or discrete-action current | OPEN / UNTESTED | contact work may live in a time-face term rather than a static density |
| Cycle-214 autonomous source/pair direct-sum current | OPEN / UNTESTED | a joint vertex ledger may cancel field emission against a local source reservoir |
| bounded gauge/auxiliary current | OPEN / UNTESTED | local auxiliaries may store the relative parity/contact work without a global service |
| relative-update/deformation response | OPEN / UNTESTED | a compactly supported law deformation may produce stress without a static conserved scalar |

Because at least six constructive routes remain open, no general no-go can
pass N1.

### N2 — condition-independence audit

The raw failures collapse into four route conditions:

```text
C_basis   = direction-blind diagonal static separation basis;
C_contact = contact matching plus exact periodic continuity;
C_phase   = phase-reference robustness of the selected static response;
C_joint   = one local matter-field-interaction ledger.
```

| pair | closing first closes second? | closing second closes first? | independent here? |
|---|---:|---:|---:|
| `C_basis,C_contact` | no | no | yes; a richer basis may close contact, while this basis could be retained without matching it |
| `C_basis,C_phase` | no | no | yes |
| `C_basis,C_joint` | no | no | yes |
| `C_contact,C_phase` | no | no | yes |
| `C_contact,C_joint` | no | no; a joint norm ledger need not contain contact action | yes |
| `C_phase,C_joint` | no | no | yes |

These are workstreams, not proposed axioms or route-independent walls.

### N3 — hidden-condition scan

The load-bearing conditions are explicit: code-space intertwiner, coin family,
contact order, periodic boundary, two-particle sector, direction-blind diagonal
ansatz, finite radius, positivity, source map, stiffness, phase zero, and
zero-mode convention. “By construction” appears only in the runner's explicit
matrix definitions. “Background,” “naturally,” “obviously,” “standard QFT,”
and “canonical” are not used as proof steps. Registered primitives are listed
only to state what they do not silently supply.

### N4 — residual matching

| witness | witness residual | residual used here | match? |
|---|---|---|---:|
| `LOCAL_GENERATOR_SOURCE_TOURNAMENT_CYCLE228_NOTE_2026-07-17.md:32,67-70,595` | `K` and spectral coordinates require a phase reference | Cycle-216 `K` response changes under rephasing | yes |
| `FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md:70-74,275-294` | local deviation-norm current is not Fock energy or stress | boundary separating the new number current from the prior `K` current | yes, boundary only |
| `VIRTUAL_EXCHANGE_GREEN_KERNEL_CYCLE216_NOTE_2026-07-16.md:59,129` | quadratic action/source interpretation remains supplied | static Green fixture and supplied-action inventory | yes |
| `UNCONTROLLED_CONTACT_COLLISION_CURRENT_SYNDROME_CYCLE289_NOTE_2026-07-17.md:34-53` | equal-total-`N` branches have pair counts 1 and 6 | number-current contact-blind control | yes |
| `ROUGH_TERMINAL_SUBSYSTEM_GAUGE_FACTORIZATION_CYCLE251_NOTE_2026-07-17.md:21,77` | bounded mapped operators have tested weight at most 18 | onsite physical support control | yes |

No cited predecessor is used to claim the new diagonal-basis certificate. The
runner computes that certificate independently.

### N5 — resolution and rhetoric audit

Tested resolutions are:

| resolution | tested content |
|---|---|
| per mode | positive `n_(x,d)` and coin-conjugated flux |
| per cell | exact divergence identity and 18-M2 support |
| adjacent cells | 35-M2 pair-basis support and zero code leakage |
| radius-1/2/3 cell pairs | 35--36-M2 support and zero code leakage |
| two-particle block | all internal-direction transitions on one representative per separation orbit |
| finite torus | `L=3..6`, both parity classes, beta training/holdout, bounded signed duals at radii 1--3 |
| lattice-wide | not classified; only the explicit global relative-parity escape is identified |

Accordingly, the note says only that the declared bounded static diagonal
separation basis does not meet all constraints on the tested domains. It does
not say that contact action is not locally conservable, that no stress tensor
exists, or that the physical M2 framework cannot source gravity.

### N6 — partial-closure path scan

The positive number current already closes locality, positivity, projective
phase robustness, mass matching, spectator invariance, and composition for a
candidate `mN` charge. Explicit partial-closure routes are:

1. admit the Cycle-216 action/phase zero conditionally, prove its bound, then
   audit whether an autonomous reference retires the import;
2. replace the static pair density by a discrete action/time-face current;
3. include the Cycle-214 source/pair sector and derive a joint vertex balance;
4. enlarge the local operator basis to off-diagonal mapped even-CAR terms;
5. add bounded auxiliary storage and audit whether it remains local and
   composition-safe.

None requires an automatic new axiom classification. Approved primitives retain
only their registered scope.

### N7 — steelman

A hostile constructive reviewer should reject any broad negative reading. The
contact gate is a local time-dependent action, so its conserved contribution
need not be diagonal in instantaneous pair separation. A discrete variational
or relative-update construction can put contact work on time faces or in
matter-field interaction terms; the Cycle-214 reversible source/pair vertex is
already a concrete bounded mediator sector in which weight moves locally
between source and field. Off-diagonal mapped even-CAR operators and bounded
auxiliaries can also store precisely the coherence discarded by this route's
direction-blind diagonal ansatz. The present dual vector therefore certifies a
small linear search domain, not the physical absence of a local source/stress
ledger.

### N8 — cross-cycle echo

- Cycle 228's static-generator tournament left direct currents, actions,
  micromotion, and Fock lifts open; this route closes only the number-current
  branch and executes one diagonal contact branch.
- Cycle 229 converted a spectral sign problem into a Fock bookkeeping result
  while keeping sea/reference and local energy current open. That history warns
  against treating the current diagonal certificate as final.
- Cycles 247–251 found rough physical factorization but preserved bounded
  auxiliary/gauge routes. Those same routes may localize contact work.
- Cycles 289–292 repeatedly closed apparent action/readout seams by adding
  bounded coherent carriers and explicit geometry. The analogous interaction-
  current carrier remains live here.

The cross-cycle pattern is constructive seam repair, not constitutional
foreclosure.

## Route disposition and next construction

```text
positive mapped number current: PASS
finite-coin mediator number current: PASS
mass/composition/spectator controls: PASS
conditional Q=mN static source response: PASS with supplied map/action
bounded diagonal contact-sensitive current: finite-radius residual
global relative-parity escape: live algebraically, rejected for bounded local additive target
combined physical source/stress ledger: OPEN
shared obstruction: none
axiom pressure: none
```

The highest-value continuation is a discrete action or relative-update search
on the same physical code, including off-diagonal mapped even-CAR contact terms
and the Cycle-214 source/pair mediator sector. The decisive test is an exact
matter + field + interaction cellwise continuity identity whose scalar
deformation matches Cycle 216 while remaining phase-reference explicit and
composition-safe.

## Verification

```text
python3 -m py_compile \
  scripts/gravity_route_c_bounded_direct_current_search_2026_07_17.py

PYTHONPATH=scripts python3 \
  scripts/gravity_route_c_bounded_direct_current_search_2026_07_17.py
```
