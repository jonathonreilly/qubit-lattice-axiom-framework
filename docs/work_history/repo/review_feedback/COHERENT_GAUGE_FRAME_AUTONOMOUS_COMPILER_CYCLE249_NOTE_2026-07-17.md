# Autonomous coherent gauge-frame compiler for the square-pyramid code — Cycle 249

**Date:** 2026-07-17

**Type:** constructive coherent local-compiler instantiation with exact
state-preparation and sector boundaries

**Status:** exact autonomous even-code sign-frame compiler; full-Fock and
absolute physical-state compiler remain open

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

Companion runner:

```text
scripts/coherent_gauge_frame_autonomous_compiler_cycle249_2026_07_17.py
```

This note and runner change no axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit surface.  They are Cycle-249 artifacts only.

## Result up front

The Cycle-244 coherent steelman works on the declared Cycle-235 **total-even**
code.  It avoids the even-torus deterministic-section obstruction because it
never computes or outputs a deterministic representative `z(s)`.
In contract shorthand: there is **no deterministic representative**,
**branch interference** is retained, paired gauge motion is separated from a
**distinct data-only logical action**, **absolute preparation** remains open,
and the **odd sector remains absent**.

For every Cycle-235 data-face qubit `Q_f`, attach a face-frame qubit `F_f`.
For every local primal-edge check, attach a coherent syndrome qubit `S_e`.
Starting from a lawful Cycle-235 encoded state, product `|+>` face frames, and
product `|0>` check carriers, apply

```text
C_H = product_(e,f in boundary e) CNOT(F_f -> S_e),
W   = product_f CZ(F_f,Q_f).
```

The result is the **uniform coherent frame orbit**

```text
E_coh |psi>
  = 2^(-abs(F)/2) sum_z
      |z>_F |H z>_S Z_Q(z) E_0 |psi>.
```

Every branch is lawful because its check word is exactly `Hz`, but no branch
is actualized, measured, decoded, or preferred.  There is no global
Jordan-Wigner order, global parity service, or host-side feedforward.

For the already mapped Cycle-235 even update `G_0`, one fixed autonomous law
works on every coherent branch:

```text
G_physical = W (I_FS tensor G_0) W^dagger.
```

It is one sector-blind unitary, not a classical table of gates `G_z`.  Exact
unitary conjugation gives

```text
E_coh G = G_physical E_coh
```

on the declared Cycle-235 code space.  The runner tests the fixed Cycle-230
six-mode Fock coin at `beta=-0.3`, both Cycle-230 `A/B` FSWAP factors, and
the Cycle-230 contact.  Intertwining and coherent uncompute residuals are at
most `1.82e-16`; branch-probability residuals are at most `1.39e-17`.  The update
uses no projective instrument and has ideal code leakage zero.

The quantum-controlled signs are local.  On the square-pyramid map, the
onsite coin touches at most 18 data faces and their 18 frame partners, an
`A/B` FSWAP touches at most 9 data faces and their 9 partners, and contact is
diagonal in mapped occupation flux and needs no frame control.  Globally,
`W` is a parallel product of matching role-local pair gates, so it contributes
one role-level layer on either side of the supplied mapped update.  In the
explicit physical placement the pairs are separated by bounded distance;
nearest-neighbor routing is supplied macrocode data, not executed as a new
homogeneous physical-law theorem here.

The important gauge distinction is exact.  A local `k=B_t` lies in `ker H`.
The data-only operation `Z_Q(k)` changes the actual coin and FSWAP, with
commutator norms `10.6219092546` and `2.82842712475`; it is not a redundancy.
The **paired** operation

```text
K(k) = X_F(k) Z_Q(k)
```

is a stabilizer of the uniform joint state and commutes exactly with the one
fixed `G_physical`.  Thus Cycle 244's distinct logical action has not been
renamed gauge: it becomes gauge only after its compensating frame shift is
included.

The construction is stronger than a conditional supplied-frame branch, but
it does not close the full campaign:

1. `E_0` is still the Cycle-235 closed-code state map.  It imports the
   total-even restriction, one combined spin/Wilson sector, its state
   preparation, the square-pyramid presentation, and the macro layout.
2. The coherent frame layer can be prepared in bounded depth **relative to an
   already prepared `E_0` state**.  Absolute `E_0` and fixed-Wilson
   preparation are not constructed.
3. The three Wilson degrees remain topological.  Bounded local affine-frame
   stabilizers define a three-Wilson-qubit subsystem; selecting a pure fixed
   affine coset needs three noncontractible conditions.
4. The closed code exponent remains `6L^3-1`.  The odd one-particle state and
   the Cycle-230 rank-73 sea still have no image, so neither fixture is
   reported as physically reproduced.
5. The explicit role placement is a period-64 macrocode.  It is proper-cubic
   and coarse-translation covariant but does not retire the unit-translation
   macro-marker.

This is a genuine constructive gain in `C_local`: autonomous coherent sign
consumption is possible without deterministic gauge fixing.  It is not a
full physical-site CAR compiler, a preparation theorem for the base code, a
Record mechanism, a clock, or an odd-sector repair.  There is no shared
substrate obstruction and **no axiom pressure**.

## 1. Exact coherent code definition

Let `H` be the Cycle-244 binary incidence map from face corrections to local
modified-Gauss syndromes.  There are, per coarse cell,

```text
15 Q data-face qubits,
15 F face-frame qubits,
11 S coherent check qubits.
```

The abstract coherent extension therefore has 41 `M_2` roles per coarse
cell.  `C_H` computes the linear function `Hz` reversibly, and `W` applies
the face sign to the corresponding data face.  Neither unitary depends on a
measurement result.

For normalized `|psi>` and orthogonal computational frame words, `E_coh` is
an isometry immediately:

```text
E_coh^dagger E_coh = E_0^dagger E_0 = I
```

on the declared input code.  The word “declared” is load bearing: Cycle 235
provides only the total-even closed-code Hilbert space after a Wilson sector
is chosen.

### Local stabilizers

Write the Cycle-235 local modified-Gauss Pauli as `g_e^Q`, with `X` support
equal to the face row `H_e`.  Clifford conjugation gives three bounded
families:

```text
P_e = Z_(S_e) product_(f in H_e) Z_(F_f),

D_e = g_e^Q product_(f in H_e) Z_(F_f),

K_f = X_(F_f) Z_(Q_f)
      product_(e incident f) X_(S_e).
```

`P_e` enforces `S=Hz`; `D_e` is the dressed data Gauss relation; `K_f` is the
coherent face-gauge generator.  At `L=3`, all 999 displayed stabilizer rows
have zero pairwise commutator failures, zero phase inconsistencies, and rank
943.  The support maxima are independent of size:

| family | maximum weight |
|---|---:|
| `P_e` | 9 |
| `D_e` | 36 |
| `K_f` | 6 |

The ranks and code exponents through the held-out size are:

| `L` | `Q` | `F` | `S` | local rank | local exponent | Wilson-fixed exponent |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 405 | 405 | 297 | 943 | 164 | 161 |
| 4 | 960 | 960 | 704 | 2238 | 386 | 383 |
| 5 | 1875 | 1875 | 1375 | 4373 | 752 | 749 |
| 6 held out | 3240 | 3240 | 2376 | 7558 | 1298 | 1295 |

The ancillary stabilizers add no spurious logical dimension.  They are the
Clifford images of product `X_F`, product `Z_S`, and the original data Gauss
relations.

## 2. One fixed physical update, not a family

Suppose the already mapped even-code update obeys

```text
E_0 G = G_0 E_0.
```

Since `C_H` acts only on ancillary registers, it commutes with `G_0`.
Therefore

```text
G_physical E_coh
 = W G_0 W^dagger W C_H (|+>|0> tensor E_0)
 = W C_H (|+>|0> tensor G_0 E_0)
 = E_coh G.
```

This is an operator identity.  The branch notation

```text
G_z = Z_Q(z) G_0 Z_Q(z)
```

is only the computational-basis block decomposition of the single quantum
unitary `G_physical`.  There is no classical selector, preferred `z`, or
host-controlled conditional instruction.

### Actual Cycle-219 and Cycle-230 factors

The executable controls use the fixed Cycle-230 update:

- `Gamma(C(-0.3))`, the actual `64 x 64` exterior lift of the Cycle-230
  six-mode coin from the Cycle-219 family;
- the actual `4 x 4` fermionic SWAP for both Cycle-230 `A` and `B` stream
  matchings; and
- the actual `64 x 64` onsite contact at diagnostic coupling `g=0.37`.

| factor | intertwining residual | interference-uncompute residual | data-only gauge commutator |
|---|---:|---:|---:|
| Cycle-230 coin | `1.8158e-16` | `1.8158e-16` | `10.6219092546` |
| Cycle-230 `A` FSWAP | `0` | `0` | `2.82842712475` |
| Cycle-230 `B` FSWAP | `0` | `0` | `2.82842712475` |
| Cycle-230 contact | `1.1696e-16` | `1.1696e-16` | `0` |

The matrix test explicitly starts with coherent frame amplitudes, applies the
branch blocks of the single controlled unitary, and uncomputes the local frame
sign.  The original frame amplitude matrix is recovered tensored with the
updated matter state.  This is a branch-interference control, not merely a
test of diagonal branch probabilities.

The actual mapped support bounds are:

| factor | data-face support bound | data plus frame support bound |
|---|---:|---:|
| onsite coin | 18 | 36 |
| one `A/B` FSWAP | 9 | 18 |
| contact | 18 | 18; no frame controls |

The physical synthesis of `G_0` remains the supplied Cycle-235 mapped-even
gate synthesis.  Cycle 249 adds the fixed pairwise `W` dressing; it does not
silently claim a new decomposition of the arbitrary onsite exterior coin
into nearest-neighbor `M_2` gates.

## 3. Gauge-kernel equivalence versus distinct logical action

For a single pyramid/mode `t`, its five-face boundary `B_t` obeys

```text
H B_t = 0.
```

Multiplying the five corresponding `K_f` generators cancels every check
ancilla because `HB_t=0` and yields

```text
K(B_t) = X_F(B_t) Z_Q(B_t).
```

It has weight 10.  The uniform coherent state is invariant under it, and
`G_physical` commutes with it exactly because in the undressed frame it is
only a shift of the product `|+>_F` register.

This does not erase Cycle 244's kernel ambiguity.  Removing `X_F(B_t)` leaves
`Z_Q(B_t)`, which flips an incident mapped hopping sign.  The actual coin and
FSWAP commutators quoted above are nonzero.  Contact commutes because it is an
occupation polynomial.  The joint transformation is gauge; the data-only
transformation is a distinct logical/frame action.

## 4. Full joint state versus one fixed affine coset

The all-syndrome joint state and a fixed-syndrome affine state must not be
conflated.

### Full coherent graph state

`E_coh` sums over every face word `z` and stores `Hz` in `S`.  From an already
prepared `E_0` state, it has an explicit bounded relative preparation:

- the incidence graph has check degree at most 8 and face degree at most 4;
- a deterministic conflict-free schedule uses 10 CNOT colors at
  `L=3,4,5,6`;
- the pairwise face-data CZ product is one additional role-level layer.

All CNOT factors compute the same linear map and commute algebraically; the
coloring is a circuit schedule, not a branch controller.  The full unitary is
defined by incidence and is translation/proper-cubic covariant even though a
particular coloring order is presentation data.

### Fixed-s affine frame

For a supplied lawful syndrome `s`, one can instead write

```text
E_s |psi> proportional to
  sum_(z: H z=s) |z>_F |s>_S Z_Q(z) E_0 |psi>.
```

The runner resolves the topology of this definition exactly.  The local
kernel words `{B_t}` have rank `6L^3-1`.  Three noncontractible membranes
raise the rank to

```text
dim ker H = 6L^3+2.
```

Consequently the bounded local `H` and `B_t` stabilizers specify a subsystem
with exactly three Wilson logical qubits:

| `L` | `rank H` | local-kernel rank | full `ker H` rank | local logical Wilson qubits |
|---:|---:|---:|---:|---:|
| 3 | 241 | 161 | 164 | 3 |
| 4 | 574 | 383 | 386 | 3 |
| 5 | 1123 | 749 | 752 | 3 |
| 6 held out | 1942 | 1295 | 1298 | 3 |

A pure uniform state over the entire affine fiber needs the three
noncontractible membrane `X` stabilizers.  A pure orbit of only the local
kernel equivalently needs three noncontractible Wilson `Z` labels.  Thus a
fixed affine **subsystem** has a bounded local definition, while selecting one
pure Wilson-resolved coset reintroduces three topological conditions.

This is not promoted to a universal finite-depth-preparation no-go.  It is an
exact stabilizer-rank distinction between the locally specified subsystem and
a pure topologically selected state.

## 5. Wilson separation

At `L=3,4,5,6`, the three Cycle-244 membranes have weights
`L^2`, zero local syndrome, and identity pairing with the three Wilson cycles.
Their paired coherent-gauge products have weights `2L^2`.

The full joint state therefore retains coherent branches related by every
Wilson membrane.  If the input `E_0` has a fixed combined Wilson label, the
joint state has that same fixed **relational** label; data-only Wilson labels
vary with the frame branch.  Local coherent constraints neither choose nor
prepare the combined label.

This is the closure boundary:

- full `S=Hz` joint framing is bounded-depth relative to `E_0`;
- fixed-s local stabilizers leave three topological logical qubits;
- pure fixed-coset selection needs three noncontractible conditions; and
- absolute fixed-Wilson preparation remains supplied through `E_0`.

No Wilson loop, membrane, circuit layer, or update count is called a physical
winding history or time.

## 6. Translation, proper-cubic covariance, and physical M2 placement

The incidence circuit passes every unit **coarse-cell** translation at
`L=3,4,5,6`.  Its 15 face roles and 11 check roles are permuted exactly by
all 24 proper-cubic frames.  The fixed Cycle-230 coin and contact Fock
matrices commute with all 24 frame representations to residual below
`2e-12`; the `A/B` outer-edge matching is carried by the checked graph
permutation.  Every frame permutes `F_f` and `Q_f` together, so
`product_f CZ(F_f,Q_f)` is invariant.  The inherited Cycle-235 local
Clifford framing repair is diagonal in `Z/CZ` after the face permutation and
therefore commutes with the new diagonal dressing.

An explicit period-64 physical placement is provided to avoid hiding
co-located tensor factors:

```text
data internal faces:     8 (D_a + D_b)                 [12]
data outer faces:       32 e_axis modulo the macrocell [3]
frame internal faces:   12 (D_a + D_b)                 [12]
frame outer faces:      32 (e_i + e_j) modulo 64       [3]
spoke-check ancillas:   16 (plus/minus 1,1,1)          [8]
grid-check blocks:      plus/minus 20 e_axis           [6]
```

The three unoriented grid-edge checks use two-site repetition blocks, adding
three bounded local equality constraints.  The explicit placement therefore
uses 44 distinct physical `M_2` sites per coarse cell rather than the 41
logical roles.  All four site orbits are collision free and invariant under
all 24 proper rotations.

On an `L=3` physical torus, translation by 64 has active-set symmetric
difference zero while translation by one has symmetric difference 2376.
The placement is a proper-cubic macrocode; its period-64 origin, role
assignment, blanks, repetition convention, and bounded routing are supplied.
It does not establish a homogeneous unit-translation law on undifferentiated
physical sites.

## 7. Leakage and deletion controls

Ideal leakage is zero on the declared code.  `G_0` commutes with every base
modified-Gauss relation, while `G_physical` and every coherent constraint are
their images under the same Clifford circuit.

The runner retains failures rather than projecting them away:

- deleting one incidence CNOT makes the `S=Hz` parity relation fail at that
  check on the `z_f=1` branch;
- deleting one face-data CZ makes every incident combined data/check relation
  fail, giving three or four local violations depending on the face;
- flipping one check bit alone lies outside `im H` at all four sizes and is
  rejected by the lawful-domain guard;
- deleting one side of the sign conjugation gives actual coin residual
  `10.6219092546` and FSWAP residual `2.82842712475`; and
- the corresponding contact residual is exactly zero, as required by its
  sign independence.

No deletion residual is called a stochastic rate or probability.

## 8. Odd sector, mass, contact, and seam

Ancillary Clifford conjugation cannot change the logical exponent of the
Cycle-235 base code.  After three combined Wilson labels are fixed, the
exponents remain:

| `L` | coherent Wilson-fixed exponent | full Fock exponent | odd sector |
|---:|---:|---:|---|
| 3 | 161 | 162 | absent |
| 4 | 383 | 384 | absent |
| 5 | 749 | 750 | absent |
| 6 held out | 1295 | 1296 | absent |

The Cycle-219 one-particle mass fixture is odd and has no `E_0` image.  The
Cycle-230 principal sea has rank 73 and is odd, so its seam state also has no
image.  The runner therefore does not print a fake zero residual for either
state intertwiner.

The result retained here is operator-level and even-code state-level:

- the actual coin, FSWAP, and contact have one bounded autonomous coherent
  sign consumer;
- contact remains sign independent;
- ideal even-code leakage is zero; and
- one-particle mass and rank-73 seam preservation remain unavailable.

Cycle 245's marked-charge/common-Wilson direct sum is a live separate route to
the odd dimension count, but it changes the state-map contract and has its own
reference/topological/update-sign obligations.  It is not silently combined
with Cycle 249.

## 9. Record and time firewall

The `F` register remains coherent and is never read.  The `S` register is a
coherent reversible carrier of `Hz`, not an actualized outcome.  **Ancilla
pointers are not Records.**  No rule is supplied that makes either carrier a
permanent readable lock of one admissible local possibility.

The 10 CNOT colors, one role-level CZ layer, conjugation depth, and gate order are
compiler resources.  **Compiler layers are not physical time.**  No clock,
duration, rate, occurrence, measurement, realized preparation history, or
record-formation law is derived.

## 10. Supplied-structure inventory

Cycle 249 supplies or inherits explicitly:

1. the Cycle-235 square-pyramid cellulation and its 15 data-face roles;
2. the Cycle-235 local incident-face order, Pauli framing repair, modified
   Gauss relations, and mapped even-algebra synthesis;
3. the total-even `E_0` state map and one combined Wilson/spin sector;
4. preparation of the input `E_0|psi>` state and its topological label;
5. one `F` qubit per face and one logical `S` qubit per local check;
6. product `|+>_F` and `|0>_S` ancillary initialization;
7. the incidence CNOT circuit, a 10-color implementation schedule, and
   pairwise `W_CZ` dressing;
8. the Cycle-230 coin at `beta=-0.3`, from the Cycle-219 common family;
9. the Cycle-230 `A/B` FSWAP/contact order and diagnostic contact coupling;
10. the period-64 placement, macro origin, blanks, routing, and two-site grid
    check repetition convention;
11. the closed periodic `L` family and boundary condition; and
12. if a pure fixed affine coset is requested, three Wilson/topological
    stabilizer eigenvalues and their state preparation.

None is declared derived from the current axioms in this cycle.  Scale
reference, kinetic isotropy, and realized-state evaluation do not provide
these structures.

## 11. Prior-art and novelty boundary

Cycle 235 supplies the face-qubit even algebra and square-pyramid
instantiation.  Cycle 244 supplies `H`, the deterministic-section witness,
the sign-frame consumer relation, local kernel ambiguity, and Wilson
membranes.  Cycle 249 composes those retained finite objects into an explicit
coherent Clifford dilation and tests the actual repository gates.

The elementary controlled-conjugation identity itself is not claimed as new
quantum-information theory.  The fixture-specific constructive content is:

1. the exact `Q/F/S` stabilizer presentation on the square-pyramid code;
2. one fixed branch-independent physical update for the actual
   coin/FSWAP/contact;
3. the exact paired-gauge versus data-only logical-action audit;
4. the all-size rank split between local affine stabilizers and three Wilson
   logical qubits;
5. bounded relative preparation through held-out `L=6`;
6. the explicit 44-site proper-cubic M2 placement and macro audit; and
7. deletion, branch-interference, odd-sector, Record, and time controls.

No global novelty priority is claimed.  No Thirring engine is used or
compared.

## 12. TOE dependency ledger after Cycle 249

| Workstream | Cycle-249 effect | Remaining dependency |
|---|---|---|
| `C_ref` | no classical branch representative or actualized outcome is needed; quantum frame origin is relational | base `E_0` state, combined Wilson label, physical sea, law parameters, macro origin, and realized preparation remain supplied |
| `C_num` | unchanged exact boundary | closed code remains total-even; odd one-particle and rank-73 sectors are absent |
| `C_wrap` | three Wilson logicals isolated from local affine stabilizers; coherent compiler layers firewalled | pure fixed-coset/Wilson preparation, phase wrapping, clock, and realized winding history remain separate |
| `C_int` | strong gain: one fixed local quantum-controlled consumer for actual coin, A/B FSWAP, and contact | odd seam state, coupling/law selection, iteration, and physical rate remain open |
| `C_local` | major gain: deterministic decoder is unnecessary; exact 41-role coherent code, bounded relative preparation, 44-site placement, all translations/frames, and held-out L=6 pass | base even-sector state compiler/preparation, unit-translation marker, pure Wilson selection, and odd-sector E remain open |
| `C_source` | unchanged | no physical energy, action, stress, source, or gravitational coupling is selected |

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.
Autonomous coherent unitary control is an operational-quantum gain, but it
does not form a Record, derive occurrence weights, or add the missing odd
matter state.

## No-go discipline gate

The fresh `origin/main` no-go-discipline procedure and current primitive
registry were applied because this note names exact remaining preparation,
odd-sector, Wilson, and marker boundaries.

> **N1-N8 result: PASS for the narrow statement that this coherent extension
> closes deterministic sign-frame selection only on the declared Cycle-235
> total-even code and does not itself construct absolute `E_0`, pure Wilson,
> odd-sector, or unit-translation preparation.  FAIL for a general coherent
> gauge-compiler no-go, a fixed-coset finite-depth no-go, minimum physical
> content, shared substrate obstruction, or axiom pressure.**

### N1 — alternative routes

| Route | Honesty marker | Attempt and disposition |
|---|---|---|
| full all-`S=Hz` coherent graph extension | **ATTEMPTED** | succeeds with bounded relative preparation and one fixed `G_physical` |
| pure fixed-s uniform affine fiber | **ATTEMPTED** | exact code definition exists; three noncontractible membrane stabilizers are needed to select one pure topological state |
| bounded local affine subsystem without Wilson selection | **ATTEMPTED** | succeeds and leaves exactly three Wilson logical qubits |
| check-syndrome register without face frames | **ATTEMPTED** | the Cycle-244 test is repeated on the actual gate matrices: contact works, but local `ker H` ambiguity changes the coin and FSWAP |
| paired frame/data kernel quotient | **ATTEMPTED** | succeeds as `X_F(k)Z_Q(k)`; data-only `Z_Q(k)` remains a distinct action |
| branch-classical `G_z` table | **ATTEMPTED AND RETIRED** | replaced by the single fixed quantum unitary `W G_0 W^dagger` |
| absolute product-state preparation of the full compiler | **ATTEMPTED AS FACTORIZATION AUDIT** | frame layer is bounded relative to `E_0`; base even-code and fixed-Wilson preparation remain unconstructed |

Seven distinct routes are visible.  Cycle 245's marked odd
charge/common-Wilson direct sum is additionally live but is not counted as an
attempt in this runner.  The tested routes' mixed successes prohibit a broad
negative claim.

### N2 — condition independence

The coherent-frame selector/consumer pair collapses to one closed condition:
`K_frame` is supplied constructively by `E_coh` and `G_physical`.  The remaining
conditions are:

- `K_E0`: an actual local state map/preparation for the Cycle-235 even code
  within a supplied spin sector;
- `K_spin`: selection/preparation of three combined Wilson labels;
- `K_odd`: a full-Fock odd-sector image;
- `K_marker`: autonomous unit-translation physical roles; and
- `K_law`: physical selection of coin/contact parameters and update law.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| `K_E0`,`K_spin` | no | no | yes |
| `K_E0`,`K_odd` | no | no | yes |
| `K_E0`,`K_marker` | no | no | yes |
| `K_E0`,`K_law` | no | no | yes |
| `K_spin`,`K_odd` | no | no | yes |
| `K_spin`,`K_marker` | no | no | yes |
| `K_spin`,`K_law` | no | no | yes |
| `K_odd`,`K_marker` | no | no | yes |
| `K_odd`,`K_law` | no | no | yes |
| `K_marker`,`K_law` | no | no | yes |

`K_spin` is not inflated into four conditions for the three Wilson bits.
Relative frame preparation is closed and is not retained as a wall.  A
particular circuit coloring is presentation data inside `K_marker`, not a new
physics dependency.

### N3 — hidden-condition scan

| Phrase or possible hidden condition | Classification |
|---|---|
| “lawful Cycle-235 state” | explicit `E_0` import and total-even restriction |
| “uniform” | exact product `|+>_F` followed by declared Clifford circuit; no probability claim |
| “autonomous” | fixed unitary without measurement/feedforward; does not mean self-prepared macro roles |
| “local” | bounded coarse-role support and period-64 routing; unit physical translations separately fail |
| “one fixed update” | exact `W G_0 W^dagger`, with `G_0` still supplied |
| “gauge” | only the paired joint action; data-only action remains distinct |
| “fixed affine coset” | requires supplied lawful `s` and three topological conditions for a pure state |
| “background spin structure” | explicit `K_spin`, never hidden as context |
| “prepared” | relative coherent layer versus absolute base/topological preparation separated |
| “Record” / “time” | explicitly not inferred from coherent pointers or circuit layers |

The phrases “we assume,” “by construction,” “as is standard,” “the framework
provides,” “bridge context,” “background,” “naturally,” “obviously,”
“standard QFT,” “registered,” and “canonical” were scanned.  Any occurrences
in descriptive prose are non-load-bearing; every scientific input is in the
supplied-structure inventory.

### N4 — residual matching

| Witness | Exact residual there | Cycle-249 use | Match? |
|---|---|---|---:|
| `EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md:32,66,95-107` | exact local even algebra; bounded full-Fock E, Wilson preparation, and odd fixtures absent | supplies `E_0/G_0` boundary and exact odd/Wilson residual | yes |
| `TRANSLATION_CUBIC_LOCAL_SYNDROME_DECODER_CYCLE244_NOTE_2026-07-17.md:83,272-291,549` | deterministic local section fails on even torus; coherent field remains live | directly constructs the named coherent alternative | yes |
| same Cycle-244 note `:328-335` | odd code and rank-73 state absent | verifies unchanged exponent and fixture boundary | yes |
| `COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md:32-45` | proper-cubic one-particle coin/mass family | uses the fixed Cycle-230 `beta=-0.3` member; mass state remains absent in `E_0` | yes |
| `SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md:32-56` | actual CAR coin/FSWAP/contact and rank-73 seam | tests the actual even gates; does not claim the absent seam state | yes |
| `HAEGEMAN_PARITY_SECTOR_GAUGING_CYCLE245_NOTE_2026-07-17.md:54-82` | marked odd/common-Wilson sector route | live alternative only, not evidence against coherent even framing | no; scoped away |
| `OFF_CODE_LOCAL_AUXILIARY_COMPLETION_CYCLE246_NOTE_2026-07-17.md:36-45,232-257` | free auxiliary algebra and Wilson/odd completion failures in a different ansatz | context only | no; not used as proof |

The constructive identity is self-contained.  No negative result from a
different auxiliary family is imported as evidence against this route.

### N5 — resolution audit

| Resolution | Tested | Not established |
|---|---|---|
| one face/check neighborhood | exact stabilizers, deletion residuals, support | noisy/fault-tolerant implementation |
| one onsite cell | actual six-mode coin/contact | selected physical law or continuum limit |
| one stream edge | actual A/B FSWAP and mapped support | full hardware synthesis of arbitrary `G_0` |
| coherent branches | amplitudes, uncompute interference, paired gauge commutator | measurement outcomes or Born weights |
| `L=3,4,5` plus held-out `L=6` | counts, ranks, translations, Wilsons, schedules | thermodynamic preparation theorem |
| all 24 proper frames | incidence, placement, actual coin/contact, W dressing | boosts/Lorentz closure |
| fixed-s subsystem | exact three-logical rank | unique pure state from local stabilizers alone |
| pure affine coset | exact need for three nonlocal stabilizer labels in this CSS presentation | universal finite-depth preparation no-go |
| physical M2 lattice | explicit 44-site macro placement | unit-translation autonomous marker formation |
| full Fock | exponent audited | odd-sector state image |

Every negative phrase is restricted to the resolution actually tested.

### N6 — partial-closure and primitive scan

The current primitive registry and every relevant `current_path` note were
read.  Scale reference, kinetic isotropy, and realized-state evaluation are
approved premises and are not walls or bounded-status sources.  Their grants
do not include a face/check code, coherent ancillary state, state-preparation
law, Wilson sector, CAR parity completion, macro-marker, coin/contact
selection, measurement instrument, or Record formation.

Partial closures that require no axiom edit are explicit:

| Path | Status | What it closes |
|---|---|---|
| full all-syndrome coherent graph state | executable | deterministic frame selection and feedforward |
| local affine subsystem | executable | bounded fixed-s code definition while retaining Wilson logicals |
| supply three Wilson labels/resource state | conditional | pure affine-coset selection |
| combine with a genuine odd-sector state map | live | `K_odd`, subject to update and locality audit |
| autonomous translation-orbit marker law | live | `K_marker` |
| derive/select one coin/contact law | live | `K_law` |

These are construction/import-retirement paths.  None justifies “new axiom
required.”

### N7 — steelman

> A hostile reviewer should reject any suggestion that Cycle 249 exposes a
> coherent-gauge obstruction.  The main route succeeds: a product face frame,
> local linear-syndrome circuit, and diagonal controlled conjugation already
> produce one exact branch-independent unitary and bounded relative
> preparation.  The three Wilson qubits can be retained as a subsystem rather
> than selected, so their pure-state preparation need not be part of the
> operational compiler.  Cycle 245 also supplies a rank-complete even/odd
> sector schema whose remaining marked signs might themselves be carried by a
> second coherent register.  An open boundary or dynamical charge can alter the
> closed parity identity.  Finally, the period-64 role pattern may be generated
> by a future autonomous marker law.  The present result therefore closes one
> serious decoder wall but cannot support a full-compiler no-go or axiom claim.

This steelman is convincing.  It fixes the disposition as a positive partial
compiler with named remaining construction targets.

### N8 — cross-cycle echo

The required repository phrase search and every physics-loop
`NO_GO_LEDGER.md` path were scanned.  No ledger contains the exact Cycle-249
coherent-frame residual.  Similar mechanisms were handled as follows:

| Earlier boundary | Retirement/live mechanism | Cycle-249 response |
|---|---|---|
| Cycle 235 nonlocal basis-frame/state preparation | introduce local ancillary degrees and Clifford dilation | frame layer retired relatively; base `E_0` remains explicit |
| Cycle 244 deterministic inverse wall | retain the full gauge orbit rather than select a section | retired exactly by the coherent joint state |
| Cycle 244 Wilson decoder separation | subsystem/topological-label split | retained as exactly three logical qubits |
| prior auxiliary completion warnings | off-code local carriers may add multiplicity or anchors | rank is checked; no spurious logicals are added |
| prior marker walls | proper-cubic role orbit plus explicit macro marker | covariance retained; autonomous marker not claimed |
| prior readable-pointer/Record walls | pointer state does not imply Record formation | coherent `S` carrier is not called a Record |
| prior circuit-depth/time walls | implementation layers are not physical time | firewall retained |

No earlier retirement mechanism is ignored.  In particular, auxiliary-field
reformulation succeeds here, so the cross-cycle audit argues against a broad
negative.

## Route disposition and optimal next campaign

**Retain:** the uniform full-joint isometry, local stabilizer presentation,
one fixed `G_physical`, actual-gate branch/interference residuals, paired
kernel gauge theorem, bounded relative preparation, affine-subsystem rank,
held-out/all-frame tests, and deletion controls.

**Do not claim:** a full-Fock compiler, one-particle mass preservation,
rank-73 seam reproduction, absolute base/topological preparation, a pure
fixed-coset local-preparation theorem, unit-translation physical law, Record,
time, rate, probability, source, or axiom consequence.

The highest-value next campaign is the **odd-sector coherent join**.  Take
Cycle 245's exact even/odd common-Wilson sector maps and replace its classical
sector/membrane sign choice by a quantum control register analogous to `F`.
The decisive test is whether one bounded proper-cubic unitary can join both
parity sectors, preserve the actual coin/FSWAP/contact and rank-73 seam, and
avoid a marked charge, noncontractible controlled membrane, or global parity
service.  Keep base-state and macro-marker preparation as separate audits.

There is no shared obstruction, no axiom pressure, and no axiom conclusion.

## Verification

```text
python3 scripts/coherent_gauge_frame_autonomous_compiler_cycle249_2026_07_17.py
```
