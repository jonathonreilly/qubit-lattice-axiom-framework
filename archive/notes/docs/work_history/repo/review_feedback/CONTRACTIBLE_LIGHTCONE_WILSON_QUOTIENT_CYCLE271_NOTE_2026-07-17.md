# Contractible-lightcone Wilson quotient — Cycle 271

**Date:** 2026-07-17

**Type:** exact contractible-local-observable / finite-light-cone compiler
theorem with a first finite-torus topology discriminator

**Status:** positive eight-sector local quotient constructed for the actual
Cycle-230 even update; global fixed-label and preparation claims remain out of
scope

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/contractible_lightcone_wilson_quotient_cycle271_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface.

## Result up front

Cycle 271 executes the positive N7 steelman left by Cycle 269. The complete
connected local-check-only edge code is not one fixed finite-torus target
tensor three spectator gauge qubits. It is nevertheless an exact compiler for
the **contractible local observable net for every finite compiler cone that
does not wrap**.

The statement is an isomorphism of sector-indexed local observable nets. It is
not literal equality of globally fixed operator labels. For each finite cone
and Wilson character `w`, a patch-dependent matter-parity transport
`J_(w,K)` moves the three twist seams outside the entire gate cone. After that
transport, every gate in the cone is the same actual Cycle-230 gate:

In the runner's contract language, **the seam can be moved outside** the
complete cone exactly on this domain.

- the actual six-mode Fock-lifted onsite coin at `beta=-0.3`;
- the actual onsite contact at `g=0.37`;
- the actual onsite `A` direction-reversal FSWAP layer; and
- the actual intercell `B` FSWAP layer.

Thus, for every even observable `O` in the declared patch algebra and every
integer compiler iteration `t` whose complete Heisenberg gate cone `K_t(O)`
has trivial Wilson holonomy,

```text
J_(w,K)^(-1) rho_w(G_w^(-t) O G_w^t) J_(w,K)
    = rho_0(G_0^(-t) O_0 G_0^t)
```

with the observable itself transported by the same local identification.
Equivalently, the eight restricted process algebras are exactly isomorphic.
No sector probability, measurement, or state preparation is used.

The seam-removal criterion is exact. Write a Wilson twist as a `Z_2` coarse-
edge cocycle `h`, and let `K` be the subgraph of `B`-stream edges in the full
Heisenberg gate cone. A cellwise matter-parity conjugacy is a zero-cochain
`f`; it moves the seam by the coboundary `delta f`. Then

```text
there exists f with (h + delta f)|K = 0
    iff
sum_(e in gamma) h(e) = 0 mod 2 for every cycle gamma in K.
```

This is the **contractible-lightcone Wilson quotient theorem**. The forward
direction follows because a coboundary sums to zero around every cycle. The
reverse direction follows by fixing one potential value per connected
component and integrating `h` along paths; cycle-triviality makes the result
path independent. The runner constructs the potentials and moved physical
face-`Z` membranes explicitly.

For an onsite full-cell patch, the exact first-wrap iterations are:

| `L` | sector-equivalent compiler iterations | first wrapped iteration |
|---:|---|---:|
| 3 | `t=0,1` | 2 |
| 4 | `t=0,1` | 2 |
| 5 | `t=0,1,2` | 3 |
| 6 held out | `t=0,1,2` | 3 |

The threshold is `ceil(L/2)` for the tested onsite cones. At that iteration
the cone first contains one complete coarse stream loop in each axis. Its
paired seam cannot be moved outside. The same cone contains the actual
`3L`-factor mapped hopping word

```text
i^(3L) product_(e in Wilson loop) A_e = W_axis.
```

The two Wilson characters give scalar residual `2`. Deleting one loop edge
restores seam avoidability for that isolated loop; deleting one hopping factor
gives a distinct Pauli word with normalized Hilbert-Schmidt residual
`sqrt(2)`. This is the first explicit topology discriminator. It does **not**
say every observable whose upper cone wraps distinguishes sectors.

All local ranks, eight sectors, patch cones, and topology controls are tested
at `L=3,4,5` and held-out `L=6`. At `L=3`, all 24 proper-cubic frames and the
**full 27-element L=3 translation group** preserve the three-dimensional Wilson
quotient/subspace and the pre-wrap/wrap classification. They do not preserve
one fixed seam representative.

This is the strongest constructive **Wilson-sector local-process quotient**
currently available for the Cycle-230-to-physical-M2 campaign:

```text
eight twisted finite-torus sectors
  -> one exact contractible local process net before topology enters its cone.
```

It does not construct one global target tensor identity, a bounded preparation
of the local-check code, the odd one-particle state sector, or the Cycle-230
rank-73 sea. There is no shared obstruction and no axiom pressure.

Cycle 251 remains the strongest sectorwise physical-M2 operator/subsystem
result for the actual mass/contact/seam fixture. The two results are
complementary and are not combined into one full compiler here.

**Compiler iteration is not physical time. A Wilson label is not a Record.**

## 1. The actual Cycle-230 gate contract

The theorem uses the actual free-plus-contact update rather than a support-only
surrogate.

At one coarse cell, the runner imports the Cycle-219/Cycle-230 six-mode coin
and constructs its `64 x 64` Fock lift. At `beta=-0.3`, all 36 one-particle
coin entries are nonzero. Hence conjugating the declared full-cell mode
algebra reaches all six directions in that cell. The coin commutes with total
cell parity to numerical residual zero on the current fixture.

The contact is

```text
W_g(x)=exp(i g binom(N_x,2)),  g=0.37.
```

It commutes with cell parity and is exactly identity on `N_x=0,1`. Deleting it
with `g=0` gives identity exactly. Consequently the supplied one-particle
rest/analytic mass equality remains unchanged at the coarse-CAR operator
level.

The actual one-particle stream factorization is

```text
S = B A.
```

`A` swaps opposite directions onsite. `B` swaps the corresponding modes
across every coarse edge. The exact permutation is checked on every mode for
`L=3,4,5,6`, and the full imported `L=3` matrices give zero `S-BA` residual.
On one edge, the physical even polynomial is

```text
F_+=(B_u+B_v+iB_u A_e-iB_v A_e)/2.
```

Across a chosen Wilson seam, `A_e` changes sign and the block is `F_-`. The
runner checks

```text
F_+ = FSWAP,
||F_+-F_-||_op = 2,
F_- = B_u F_+ B_u.
```

The last equality is exactly why a cell-parity coboundary moves a seam.
Onsite coin/contact commute with the same cell parity, so no new sector term
appears when the seam is deformed.

## 2. Exact full-cell Heisenberg cone

For the state update `G=W_g Gamma(B A C)`, backwards Heisenberg propagation
has the support order

```text
contact -> B -> A -> coin.
```

Contact, `A`, and coin stay inside one coarse cell. The dense six-direction
coin makes all six directional supports present for the declared full-cell
algebra. The `B` layer then crosses every outer edge incident on the current
cell set. One iteration therefore replaces the current support cells by their
six nearest neighbours and records every crossed `B` edge in the gate cone.

The runner retains every intermediate cell slice and the union of every
stream gate touched up to iteration `t`. It does not inspect only the final
support. Seam removal is required on that **entire** accumulated gate cone.

For an arbitrary smaller subalgebra this is a safe upper cone. For the
declared full onsite algebra it is exact because the imported coin is dense.
This lawfully fixes the theorem domain rather than claiming minimal support
for every specially chosen observable.

## 3. Cohomological seam-removal algorithm

The Cycle-269 flat membrane for axis `a` is a `Z` mask on the `L^2` outer
faces crossing one periodic cut. A product of all six target parities in a
coarse cell contributes the graph cut of that cell. Internal edges occur
twice and cancel; only outer stream edges remain. A product over cells with
`f(x)=1` therefore adds `delta f` to the seam.

On every forbidden cone edge `(x,y)`, seam removal demands

```text
f(x)+f(y)=h(x,y) mod 2.
```

The runner solves these equations by graph traversal. If it succeeds, it
checks all of the following exactly:

1. the moved seam has zero intersection with every cone stream edge;
2. it commutes with every bounded elementary local check;
3. it retains the same three Wilson pairings as the original seam; and
4. every XOR combination for the eight Wilson sectors also avoids the cone.

The potential is a change of sector trivialization, not a host-side control
applied during the update. Each sector block has a patch-dependent
identification, and under that identification its complete cone circuit is
the untwisted circuit. The implementing parity product may be system-spanning;
it is an algebraic comparison map, not a bounded physical circuit or a
prepared auxiliary resource.

The theorem is stronger than testing translated flat planes. At `L=3`, the
one-step onsite cone projects onto every coordinate value, so no flat plane is
generically outside it. A deformed cocycle representative still avoids the
contractible star exactly.

## 4. Patch tournament

Three patch algebras are tested:

- one complete onsite six-mode cell;
- a two-cell `x` bond; and
- a four-cell `xy` plaquette.

The first iterations at which at least one Wilson class cannot be removed are:

| `L` | onsite | `x` bond | `xy` plaquette |
|---:|---:|---:|---:|
| 3 | 2 | 1 (`x`) | 1 (`x,y`) |
| 4 | 2 | 2 | 2 |
| 5 | 3 | 2 (`x`) | 2 (`x,y`) |
| 6 held out | 3 | 3 | 3 |

Parentheses name the first obstructed axes when the other classes are still
removable. Every earlier iteration passes all eight sector comparisons.

These finite-size thresholds are not proposed as a continuum light speed.
They count applications of the declared compiler decomposition. A physical
time interpretation would require the causal-time lane's clock/rate
calibration and is not supplied here.

## 5. First wrap and topology discriminator

For the onsite patch, `t=ceil(L/2)` contains the complete coarse loop at
fixed transverse coordinates in all three directions. The paired seam has
odd holonomy on that loop. If it vanished on every loop edge, its loop sum
would be zero, contradicting the Wilson pairing. The runner's potential
solver rejects it exactly while continuing to accept the two unpaired seam
classes.

At `t-1`, that complete loop is absent. Deleting any one edge from the
isolated loop changes it into a path and restores a solution. This supplies a
clause-delete control for the topology criterion.

The mapped hopping product on the corresponding square-pyramid loop uses
`3L` bounded `A_e` generators and equals the Wilson Pauli including its
presentation phase. It is an explicit observable available inside the
wrapped cone algebra. Its sector values differ by `2`.

This supports only the following narrow boundary:

> A Wilson cocycle paired with a noncontractible cycle contained in the
> declared cone cannot be moved completely outside that cycle by a cellwise
> parity coboundary.

It does not prove that every operator with a wrapped upper cone is
sector-sensitive. Cancellations, smaller actual support, and Wilson-blind
observables remain possible.

## 6. Proper-cubic and translation covariance

At `L=3`, the runner transforms the three seam cochains under all 24
proper-cubic frames and all 27 coarse translations. For every transformation:

- the transformed cochains commute with all bounded local checks;
- their three Wilson-pairing vectors retain rank three;
- translations retain the standard three quotient characters; and
- the one-step onsite cone remains removable while its two-step cone is
  wrapped.

There are `24*27=648` combined patch classification controls. No fixed seam
set is invariant: frames permute axes and translations move/deform cuts. The
covariant object is the cohomology/Wilson quotient subspace and the
contractible-versus-wrapped classification.

This is why the result is stated at the quotient/subspace level rather than
by privileging one membrane presentation.

## 7. Leakage, deletion, and iteration controls

The eight-sector code census is rerun rather than inherited as a status
label:

| `L` | local rank | local-code exponent | lawful Wilson sectors | each sector exponent |
|---:|---:|---:|---:|---:|
| 3 | 241 | 164 | 8 | 161 |
| 4 | 574 | 386 | 8 | 383 |
| 5 | 1123 | 752 | 8 | 749 |
| 6 held out | 1942 | 1298 | 8 | 1295 |

All `B_v/A_e` matter generators commute with every local check and every
Wilson. Therefore the mapped coin, contact, and FSWAP polynomials have zero
ideal-code leakage and zero Wilson transitions.

The `L=3` physical local-check family has 297 rows and rank 241. Deleting any
one redundant physical row leaves the rank unchanged. Reducing to an
independent basis and deleting one basis relation lowers the rank by one and
adds a spurious logical. This prevents physical redundancy from being
mistaken for dispensability of the constraint space.

Iteration has two different roles:

1. bounded repetition expands the gate cone and is covered by the quotient
   theorem until its topology changes; and
2. the explicit `3L` hopping composition constructs a Wilson discriminator.

Neither role is a clock. **Compiler iteration is not physical time**, and a
generator element is not called a rate.

## 8. Lawful domain and state/preparation limitations

The exact lawful domain is:

```text
even observables supported in the declared full-cell patch algebra,
transported sector by sector,
for finite compiler cones whose stream subgraph has zero pairing with the
Wilson cocycles being quotiented.
```

The theorem does not include:

- a Wilson loop or its conjugate membrane;
- a fixed global operator labeling shared without transport by all sectors;
- a bounded physical implementation of the patch-dependent comparison map;
- arbitrary unmatched states selected independently in different sectors;
- a preparation circuit for the local-check code;
- odd total-parity matter states; or
- a physical-time, Record, or probability interpretation.

Equal local operators do not force equal expectation values for arbitrary
states. Expectation comparison requires sector states with matching reduced
functionals under `J_(w,K)`. The quotient theorem supplies the algebra and
update identification, not those states.

The natural basis-diagonal occupation-to-face-flux encoder still has tested
minimum separated-pair string lengths

```text
L=3,4,5,6 -> 3,6,6,9.
```

This is only that encoder's preparation bill; no general bounded quantum
encoder no-go is asserted.

The actual Cycle-230 one-particle sector and its rank-73 principal sea are
both odd. They are absent from the total-even closed edge-code block. The
contact's one-particle identity proves operator-law coexistence with the mass
fixture, but this code does not prepare or represent that odd fixture state.

A Wilson label is a conserved central spin/twist character. **A Wilson label
is not a Record**: no branch is selected, written, or made into a
realized-history fact by this construction.

## 9. Supplied-structure inventory

The construction supplies:

1. periodic cubic sizes `L=3,4,5,6` and one macro origin for patch displays;
2. the complete connected square-pyramid graph with 15 face `M_2` factors per
   coarse cell;
3. the `11L^3` bounded local-check rows and their `+1` signs;
4. the three Wilson cohomology classes and eight central characters;
5. the total-even target matter restriction;
6. the actual Cycle-230 `beta=-0.3` coin, `g=0.37` contact, and `A/B` schedule;
7. the graph-to-matter `B_v/A_e` dictionary and incident-order Clifford
   presentation inherited from Cycle 235;
8. a declared full-cell even observable patch algebra;
9. a number of compiler iterations and the complete accumulated gate cone;
10. a patch-dependent zero-cochain/seam trivialization for each sector;
11. the proper-cubic and translation action on the quotient; and
12. product/basis-diagonal inputs only for the separate preparation control.

The macro origin, seam representative, zero-cochain, compiler schedule,
iteration index, Wilson character, and state comparison map are supplied
compiler data. None is a Record or physical clock.

## 10. Prior-art and novelty boundary

Bravyi–Kitaev edge encodings and their local cycle constraints are prior art.
Chen–Kapustin and Chen make the spin-structure/topological-sector dependence
of three-dimensional bosonization explicit. Cycle 271 does not claim a new
general bosonization theorem or global novelty priority.

The fixture-specific constructive result is narrower:

1. the exact cell-coboundary seam-removal criterion on the complete connected
   Cycle-235/269 edge code;
2. its application to the actual Cycle-230 coin/contact/A-B-FSWAP cone;
3. exact onsite, bond, and plaquette thresholds through held-out `L=6`;
4. the first wrapped-cone Wilson discriminator and deletion repair;
5. all-24/full-translation quotient covariance; and
6. the separation between local update equivalence and state preparation.

Nys–Carleo's distinction between constant-depth local evolution and global
constraint preparation is a useful comparison boundary, not a theorem
imported into this 3-D fixture. No Thirring construction is used or compared.

## 11. N1–N8 no-go-discipline gate

The main result is positive. The only negative boundary is the exact
cell-coboundary statement for a cone containing a paired noncontractible
cycle. No universal bounded-encoder, local-observable, or finite-time no-go is
claimed.

### N1 — Alternative-route enumeration

1. **ATTEMPTED — move only a translated flat seam.** Flat planes are too
   restrictive even for the `L=3,t=1` onsite cone; the general zero-cochain
   solver succeeds and supplies the positive theorem.
2. **ATTEMPTED — arbitrary deformed cell-coboundary seam.** This is the full
   route at the declared representation level. It succeeds exactly before
   wrap and fails on the paired Wilson loop by the odd cycle sum.
3. **ATTEMPTED — move the paired seam after translating the patch.** All 27
   `L=3` translations preserve the same pre-wrap/wrap classification; they
   move representatives but not the loop pairing.
4. **ATTEMPTED — rotate into another proper-cubic frame.** All 24 frames
   permute the Wilson quotient. They do not turn an odd pairing into zero.
5. **ATTEMPTED — delete one edge of the discriminator.** This succeeds: the
   loop becomes a path and seam avoidance is restored. It narrows the
   boundary to a complete paired cycle rather than a large support slogan.
6. **ATTEMPTED — restrict to a Wilson-blind observable inside a wrapped upper
   cone.** This remains live; the runner proves only that the uniform seam-
   removal theorem stops, while the explicit Wilson word supplies one actual
   discriminator.
7. **ATTEMPTED — fix one Wilson block.** This recovers the Cycle-235 global
   representation but selects a sector instead of quotienting all eight.
8. **OPEN — change topology or code.** Open boundaries, another subsystem
   code, and thermodynamic local nets remain outside the narrow boundary.

The successful deformed-seam and edge-deletion routes prevent a broad
topological no-go.

### N2 — Condition-independence audit

The collapsed condition set has two members:

- `C_net`: every Wilson class being quotiented is cycle-trivial on the full
  accumulated stream-gate cone; and
- `C_state`: compared sector states have matching local functionals under the
  patch identification, or a preparation theorem supplies them.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `C_net`,`C_state` | no—an algebra isomorphism prepares no state | no—matched states do not remove a Wilson cocycle from a gate cone | yes |

Coin/contact parity, FSWAP conjugacy, seam solving, and Wilson-word iteration
are witnesses for `C_net`, not four extra walls. String length and odd-sector
absence are evidence only for `C_state`/preparation scope. Physical clock and
Record semantics are not counted as walls because the theorem makes neither
claim.

### N3 — Hidden-condition scan

The load-bearing conditions are explicit: closed periodic topology; complete
connected graph; local checks with fixed signs; total-even matter; actual
Cycle-230 gate schedule; full-cell even patch algebra; accumulated compiler
gate cone; sector-dependent transported observable labels; and matched states
only when expectations are compared.

The prescribed phrases “we assume,” “by construction,” “as is standard,”
“the framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” and “registered/canonical” were scanned.
“Canonical” occurs only in prior Cycle-230's named number-preserving lift and
is not used as proof here. “By construction” is avoided in the load-bearing
argument. No hidden condition is promoted.

### N4 — Residual matching

| witness | residual there | Cycle-271 use | match? |
|---|---|---|---:|
| `WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md`, N7 | contractible local net may quotient the Wilson center | executes that exact positive steelman | yes |
| same note, Sections 3–5 | seams move by cell-plane parity and full stream sees topology | generalizes flat planes to arbitrary cell coboundaries and locates first cone wrap | yes |
| `SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md`, spatial construction | actual coin, contact, and A/B stream at six-mode CAR resolution | uses those actual gates and schedule | yes |
| `EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md` | fixed-sector even-algebra map and growing basis-diagonal preparation strings | retains local map and keeps state preparation separate | yes |
| `DISTRIBUTED_PHASE_FIELD_CAR_COMPILER_CYCLE263_NOTE_2026-07-17.md` | isolated-cycle holonomies | no proof role in the complete connected graph | no; dropped |

The proof is the new exact cochain solver plus the actual gate-cone census;
prior status labels are not used as evidence.

### N5 — Resolution and rhetoric audit

| resolution | tested result |
|---|---|
| one onsite coin/contact | sector identity under cell-parity transport |
| one seam FSWAP | exact sign conjugacy and residual `2` before transport |
| onsite/bond/plaquette finite cone | exact eight-sector equivalence while all paired cocycles are removable |
| first complete coarse loop | paired cocycle cannot vanish on the loop |
| `3L` bounded hopping word | exact Wilson discriminator, residual `2` |
| arbitrary observable with a wrapped upper cone | not classified; may remain Wilson-blind |
| full finite-torus update | Cycle-269 sector-indexed twisted family, not one target tensor identity |
| arbitrary bounded quantum state encoder | not tested |

Accordingly, the note says “the uniform cell-coboundary local-net theorem
stops at a paired cycle,” not “all wrapped local observations depend on the
Wilson sector.”

### N6 — Partial-closure path scan

The positive import-retirement paths are:

1. use the exact contractible local quotient established here for bounded
   local experiments;
2. fix one Wilson block for a global finite-torus representation;
3. keep the eight twisted targets as a direct-sum law family;
4. prove a preparation theorem for matched local states without changing the
   operator quotient;
5. use open boundaries or a thermodynamic local-observable limit; or
6. construct another code in which topology is a genuine spectator subsystem.

All are law/theorem routes. None implies a new axiom. No primitive-registry
absence claim is made.

### N7 — Steelman

> A hostile reviewer should object that the first wrapped **upper** cone is
> not itself an operational sector measurement. Many observables have smaller
> true supports or cancel the Wilson-sensitive terms, and the runner exhibits
> only one explicit Wilson word that distinguishes the blocks. A more refined
> observable-dependent cone, an open-boundary compiler, a thermodynamic local
> net, or another subsystem code may extend local equivalence beyond these
> conservative full-cell thresholds. Moreover, even the successful algebra
> quotient predicts expectation values only after sector states are matched or
> prepared. Therefore the result is a strong positive local-net theorem and a
> narrow failure of one uniform seam-removal proof—not a universal topological
> obstruction.

This steelman is accepted. It fixes the scope of the negative boundary and
identifies the next positive route: observable-specific cancellations and
matched-state preparation.

### N8 — Cross-cycle echo

Cycle 235 separated the exact even-algebra map from global state preparation.
Cycle 251 separated algebra factorization from bounded initialization. Cycle
263 found a local/global holonomy split on a disconnected graph and is not
used as proof. Cycle 265 returned to the complete graph and retained Wilson
selection. Cycle 269 constructed all eight twisted blocks, rejected a false
spectator-`M_8` interpretation, and explicitly proposed the contractible-net
quotient.

Cycle 271 applies the constructive mechanism that retired similar earlier
walls: make the operational quotient exact rather than demand equality of a
presentation. It retires Wilson selection for pre-wrap contractible local
operator processes, but not for global words, arbitrary state preparation, or
one fixed finite-torus target. Repository no-go ledgers contain Wilson-mark,
Wilson-measure, and plaquette rows with different residuals; none is used as
proof here.

**N1–N8 status: PASS for the narrow paired-cycle/cell-coboundary boundary.**

There is no shared obstruction and no axiom pressure.

## 12. Disposition and next probe

| clause | disposition |
|---|---|
| actual Cycle-230 onsite coin/contact | included; sector identity under transport |
| actual `A/B` FSWAP stream | included through held-out `L=6` |
| contractible finite cones | exact eight-sector quotient compiler |
| onsite first-wrap threshold | `2,2,3,3` for `L=3,4,5,6` |
| first topology discriminator | complete coarse loop plus exact `3L` Wilson word |
| all 24/full `L=3` translations | quotient/subspace covariance closed |
| leakage | zero for mapped even algebra |
| deletion | contact, loop-edge, hopping-factor, and check-basis controls pass |
| one-particle mass operator fixture | unchanged by contact; odd state absent from code |
| arbitrary sector states/preparation | not supplied |
| physical time | not claimed |
| Wilson as Record | explicitly rejected |
| shared obstruction / axiom pressure | none |

The highest-value next probe is an observable-specific cancellation and
matched-state tournament: determine whether physically used finite record
observables remain Wilson-blind beyond the conservative full-cell first-wrap
threshold, and separately construct or falsify a bounded preparation of
locally matched sector states. That can strengthen the local compiler without
misreporting a global tensor factor.

## Verification

Run:

```bash
python3 scripts/contractible_lightcone_wilson_quotient_cycle271_2026_07_17.py
```

The runner must report zero failures. PASS totals are regression controls, not
a count of independent physical facts.
