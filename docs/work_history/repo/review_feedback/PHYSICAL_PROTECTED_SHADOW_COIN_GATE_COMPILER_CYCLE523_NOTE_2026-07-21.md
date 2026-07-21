# Physical protected-shadow coin gate compiler — Cycle 523 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py`.

## Result

Cycle 523 closes the bare onsite-gate obligation left by Cycle 520's
protected-shadow candidate.  Put six private occupation M2s on the face
centres of the Cycle-231 `3 x 3 x 3` physical supercell and one parity-tag M2
at its centre.  Every face-centre M2 is one physical lattice edge from the
tag.  For the actual Cycle-219 `beta=-0.3` coin, adjacent complex QR produces
**10 Givens** rotations and one onsite phase.  Routing each Givens through the
temporarily blank tag gives 31 one-/two-M2 calls.  The **15 contact** phases
at `g=0.37` route through the same star in 45 calls, and six CNOTs uncompute
and recompute the tag.

On the full local M64—not only the `N<=2` sector—the resulting seven-M2
unitary satisfies

\[
 G_7E_7=E_7\,W_g\Gamma(C)
\]

with Frobenius intertwiner residual
`5.272182555577386e-15`, maximum column residual
`9.992007221626409e-16`, and zero terminal code leakage.  Its inverse
roundtrip residual is `7.504184205291937e-15`.  The compiled rest mass is
`0.453405654174885`, differing from the Cycle-219 fixture by
`2.220446049250313e-16`.

The local physical frame is also primitive.  A geometric permutation of the
six face sites alone fails the exterior coin in 22 of 24 frames, with maximum
residual `9.237604307034013`.  For each frame, the exterior/Koszul sign
cocycle is a product of CZs on the inversion pairs of its six-direction
permutation.  Routing those CZs through the tag gives at most 45 two-M2 calls.
The compiled cocycle residual is zero, the corrected code-covariance residual
is at most `8.102539046077842e-15`, and all 576 frame products close exactly.

Cycle 523 also independently closes the value-decoding part of synchronizing
this private occupation register with Cycle 522's selected native shell.  On
each of its 160 valid local term patterns, the six occupation shadows obey

\[
 q_d = c_d\mathbin{\mathrm{XOR}}i_d
       \mathbin{\mathrm{XOR}}(c_d\mathbin{\mathrm{AND}}f)
       \mathbin{\mathrm{XOR}}(c_{\bar d}\mathbin{\mathrm{AND}}i_d)
       \mathbin{\mathrm{XOR}}(c_{\bar d}\mathbin{\mathrm{AND}}f).
\]

The relation passes 327,360 all-cell direction tests across L5 and held L6,
plus all-frame role, term, and 576-product tests.  Its six-output circuit uses
282 bare one-/two-M2 calls to compute and 282 to uncompute.  This is exact
logical synchronization on the selected patterns; nearest-neighbour routing
and the native shell's bare recurrent amplitude transition remain open.

This is a strong constructive partial closure, not the full Cycle-230
compiler.  During the tested protected update the old tag is uncomputed to
zero before the direct occupation gates.  Consequently the intercell
endpoint-FSWAP layer is still exactly Cycle 231's direct stream.  At L5 it
has 60,600 wrong exchange signs among 280,875 two-particle basis pairs; held
L6 has 154,800 among 839,160.  A basis witness has exact/local phases `-1/+1`,
so the operator-norm residual remains exactly 2 even after common onsite
unitaries are added.  Recomputing the tag gets the final cell parities right
but does not repair those amplitudes.

No shared obstruction or axiom pressure is inferred.

## Exact seven-M2 encoding and primitive vocabulary

For each coarse cell `x`, place

```text
q_(x,d) at 3x - D_d,  d=0,...,5,
tau_x    at 3x.
```

The remaining 20 sites of the 27-site supercell are blank.  The code is

\[
 E_7|n_0\ldots n_5\rangle
 =|n_0\ldots n_5,\tau=\textstyle\sum_dn_d\bmod2\rangle.
\]

Its allowed runtime primitives are:

1. a one-M2 phase `diag(1,e^{i theta})`;
2. the exterior lift of any supplied two-mode `U(2)` Givens, whose occupied
   pair entry is `det U` rather than the ordinary-qubit value one;
3. the Cycle-230 FSWAP `diag(1,SWAP,-1)`;
4. a controlled phase `diag(1,1,1,e^{ig})`; and
5. `CNOT(q_(x,d) -> tau_x)` for parity compute/uncompute.

Every primitive acts on one or two physical M2s.  Every two-M2 call inside a
cell lies on a face-centre/tag edge of physical L1 length one.  The Cycle-230
outer-edge FSWAP endpoints are also physical nearest neighbours in this
supercell layout.

For a two-mode even gate `V` on leaves `i,j`, the routed macro is

```text
FSWAP(q_i,tau); V(tau,q_j); FSWAP(q_i,tau).
```

On the blank-tag subspace it is exactly `V(q_i,q_j)` and returns the tag to
zero.  The contact/CZ specialization is exact even off that blank subspace.
The coin specialization is required only after parity uncompute; its
off-code completion is the displayed three-gate unitary and is not silently
called a direct two-leaf gate.

## Actual coin factorization

The compiled target is precisely

\[
 C=e^{i\phi}\left(P_{\rm scalar}-P_{\rm even}
   +e^{-0.3i}P_{\rm vector}\right),
 \qquad \phi=\tan(0.15),
\]

from Cycle 219.  The QR elimination has diagonalization residual
`1.2391324586559453e-15`.  Its 10 adjacent Givens plus one nontrivial phase
reconstruct the one-particle matrix with residual
`1.0979470389962261e-15` and unitarity residual
`1.0806226211343075e-15`.  The frozen coefficient/order digest is

```text
0fdb7f3f8a29f532961e48c04fac9aa4d0fd2f37dd3e9cdd0d5f4246bf3d4ea0
```

Exterior-lifting and routing the factors reproduces the complete 64-state
coin with residual `4.845707866508042e-15`.  The QR and its coefficient
ordering are compile-time supplied work.  There is no measurement, input
branch, or host-side adaptive control in the runtime list once `beta` is
fixed.

## Contact and parity conjugation

The fifteen pair gates obey

\[
 \prod_{0\leq i<j<6}e^{ig n_i n_j}
 =e^{ig\binom N2}.
\]

The routed 128-state reconstruction residual is
`3.658686032644649e-15`.  Exactly 15 local two-particle basis states are
active.  Deleting contact gives the exact single-active-pair residual
`0.36789306705608243`.

Let

\[
 W=\prod_{d=0}^5\operatorname{CNOT}(q_d\rightarrow\tau).
\]

The six CNOTs commute, `W^2=I` exactly, and `WE_7` is the direct occupation
register with a blank tag.  The protected onsite update is

\[
 G_7=W\,G_{\rm contact}\,G_{\rm coin}\,W.
\]

It is unitary on the entire 128-state physical block, with unitarity residual
`8.132563207440339e-15`; only its action on the declared 64-state code is
assigned the coarse-CAR meaning.

## Selected-native-shell occupation-shadow decoder

Cycle 522's selected grammar has 160 terms and 160 distinct native auxiliary
role patterns per cell.  Write `c_d` for the centre port in direction `d`,
`c_bar` for the centre port in direction `d^1`, `i_d` for the inward
neighbour's opposite port, and `f` for the cell flag.  Exhaustive algebra on
the selected rows gives the degree-two relational decoder

```text
q_d = c_d XOR i_d XOR (c_d AND f) XOR (c_bar AND i_d) XOR (c_bar AND f).
```

The 14-role native shell contributes 13 roles to the six decoders; the role
`r` is unused.  All 64 logical six-bit occupation words occur.  The complete
degree-at-most-two feature matrix has shape `160 x 106`, rank 68, and nullity
38.  Thus this formula is a verified completion on the selected patterns,
not a uniqueness claim for invalid native patterns.  Its canonical role-row
digest is

```text
97532e93082b7624d7a4fdb923541ad3457a3b39359571b072d7559964183f38
```

| size | cells | all-cell direction tests | frame-role tests | frame-transformed term tests |
|---:|---:|---:|---:|---:|
| L5 train | 125 | 120,000 | 18,000 | 23,040 |
| held L6 | 216 | 207,360 | 31,104 | 23,040 |

Every listed test has zero failures.  Direction/opposite-direction roles
transform covariantly in all 24 proper-cubic frames, and each size also has
zero failures in all 576 frame products.  Deleting the five displayed
monomials one at a time gives respectively `48, 48, 8, 16, 8` failures on
the 160 patterns for every direction and both sizes.

Per direction the decoder uses two CNOTs and three Toffolis.  The standard
exact no-ancilla Toffoli decomposition used here has 15 one-/two-M2 gates
(nine one-M2 and six two-M2), maximum algebraic support two,
reconstruction residual `7.346882794269506e-16`, and inverse residual
`1.2749064385906742e-15`.  The six-direction compute therefore costs 282
bare calls; compute plus uncompute costs 564.

This closes a real synchronization subwall, but not the whole native-shell
compiler.  The bare CNOT/Toffoli decomposition specifies support cardinality,
while a nearest-neighbour routing from the 14 native auxiliary positions to
the new shadows has not been synthesized.  Compute/uncompute is exact if the
native controls are unchanged.  Cycle 522 supplies a bounded dense on-shell
algebraic lift, but does not decompose it into primitive recurrent gates.
Once coin or stream evolution changes native term amplitudes, a compatible
bare selected-shell transition must update the controls consistently before
the shadows can be erased.  Neither that primitive transition nor its
recurrent edge geometry is claimed here.

## Leakage, inverse, deletion, and perturbation

The full local M64 code gives:

| control | Frobenius residual | maximum column | terminal leakage |
|---|---:|---:|---:|
| baseline intertwiner | `5.272182555577386e-15` | `9.992007221626409e-16` | `0` |
| delete first Givens core | `4.329622682145759` | `0.7653763896310886` | `0` |
| delete first routing FSWAP | `8.000000000000004` | `1.4142135623730956` | `5.6568542494923815` |
| delete first contact phase | `1.4715722682243304` | `0.36789306705608227` | `0` |
| delete first final parity CNOT | `8.000000000000004` | `1.414213562373096` | `5.656854249492382` |
| perturb first Givens by `1e-4` | `0.0005656854247137266` | `9.999999995866999e-05` | `0` |

The final-CNOT deletion corrupts 63 of 64 actual coin/contact columns.  The
vacuum is the only unaffected column.  Reversing the primitive list and
daggering each primitive supplies the explicit inverse; the complete
128-state forward/inverse residual is `7.504184205291937e-15`.

## Proper-cubic frame and schedule audit

For a proper frame `R`, let `P_R` permute the six directions and let `Q_R`
be the ordinary permutation of the six face-centre tensor factors.  The
coarse CAR frame is `Gamma(P_R)`, not `Q_R`.  Define

\[
 D_R=\Gamma(P_R)Q_R^\dagger.
\]

`D_R` is diagonal.  For every inversion `i<j` with `P_R(i)>P_R(j)`, it has
one CZ between the target leaves `P_R(i),P_R(j)`.  The frame representation

\[
 R_{\rm phys}=D_RQ_R
\]

is therefore compiled using only the same bounded star.  Across all 24
frames:

- the number of CZ pairs has histogram
  `{0:1, 2:3, 5:6, 7:2, 8:2, 10:6, 13:3, 15:1}`;
- routed-cocycle reconstruction and frame-code residuals are exactly zero;
- mapped-gate-list versus geometric conjugacy residual is at most
  `1.5535550445956367e-15`;
- corrected protected-update covariance is at most
  `8.102539046077842e-15`;
- contact geometric covariance is exact; and
- all 576 products have zero failures and zero maximum residual.

The pure geometric control is retained: it fails the coin in 22 frames.  The
bounded Koszul correction, not a preferred global ordering, is what closes
the onsite frame representation.

At L5 and held L6 every proper frame is also checked on the whole physical
layout.  It bijects the complete cell set and maps the outer-edge FSWAP pair
set to itself with zero failures.  Local star edges and outer edges both have
physical L1 length one.

## L5/held-L6 schedule census

The candidate factor order inherited from Cycle 230 is

```text
parity-uncompute -> coin -> reverse-A -> edge-B -> contact -> parity-compute.
```

Per cell the concrete call census is:

| factor | calls per cell |
|---|---:|
| parity uncompute plus compute | 12 |
| routed coin | 31 |
| routed onsite reverse-A | 9 |
| outer-edge B FSWAP share | 3 |
| routed contact | 45 |
| total | **100** |

The serial factor-order depth upper bound is 98 because all disjoint B edges
form one layer.  The lattice censuses are:

| size | cells | active M2 | physical supercell sites | gate calls |
|---:|---:|---:|---:|---:|
| L5 train | 125 | 875 | 3,375 | 12,500 |
| held L6 | 216 | 1,512 | 5,832 | 21,600 |

This list is deterministic after the supplied coefficients and lattice size
are fixed.  The list order is a derived discrete update order.  It is not
called causal time, physical elapsed duration, a Hamiltonian element, a rate,
physical energy, or realized history.  No physical duration is inferred from
the depth 98 bound.

## Exact stream boundary

The direct outer-edge B layer permutes `6L^3` modes.  In the globally ordered
CAR occupation basis its exact exterior lift attaches the parity of all
crossings induced by that permutation.  A product of endpoint FSWAPs sees
only double occupation of each selected endpoint pair.  The protected-shadow
schedule tested here uncomputes every tag before that layer, so it supplies no
additional exchange phase.

| size | modes | two-particle pairs | wrong endpoint signs | first witness | exact/local phase |
|---:|---:|---:|---:|---|---|
| L5 | 750 | 280,875 | 60,600 | `(0,1)` | `-1/+1` |
| held L6 | 1,296 | 839,160 | 154,800 | `(0,1)` | `-1/+1` |

All vacuum and one-particle actions agree, and terminal parity tags can be
recomputed without leakage.  The fixed-number witness nevertheless gives
norm 2.  Multiplication by the common compiled coin, reverse-A, contact, and
parity unitaries cannot change that norm.  Therefore Cycle 523 does not claim

\[
 E G_{\rm coarse}=G_{\rm physical}E
\]

for the full Cycle-230 update.  It claims that equality for the complete
onsite `W_g Gamma(C)` block and supplies a concrete bounded primitive list for
every local factor.  No global Jordan-Wigner ordering or parity service is
used to conceal the stream residual.

## Supplied structure and novelty boundary

| item | status in Cycle 523 |
|---|---|
| Cycle-219 `beta=-0.3` coin and common-cone phase | supplied candidate-law coefficients |
| Cycle-230 `g=0.37`, factor order, reverse/edge split | supplied candidate law |
| Cycle-231 face-centre supercell and endpoint-stream countercontrol | retained bounded layout and exact negative comparator |
| Cycle-520 parity-tag encoding and protected conjugation | retained architecture |
| Cycle-522 selected 160-term native grammar | retained candidate representation |
| complex QR angles/order | computed once and frozen; not dynamically selected |
| one-/two-M2 exterior Givens, FSWAP, CP, CNOT semantics | explicit primitive matrices in this runner |
| 15 contact decomposition | derived exactly here from pair occupation |
| Koszul frame cocycle | derived and bare-gate compiled here |
| `3 x 3 x 3` block origin and blank pattern | supplied preparation/layout condition |
| beta/contact selection | not derived |
| full exterior B-stream phase service | not supplied or claimed |
| selected native term-to-shadow value synchronization | derived exactly here on all valid patterns |
| decoder outside the 160 selected native patterns | nonunique and unassigned |
| native-to-shadow nearest-neighbour routing | not synthesized or claimed |
| bare recurrent native selected-shell amplitude transition compatible with this decoder | not synthesized or claimed; Cycle 522's dense algebraic lift is retained prior work |

The novelty is the small explicit full-M64 bare circuit, its parity-hub
routing, and its primitive all-frame correction.  Generic QR compilation,
fermionic Givens gates, and controlled pair phases are standard finite
machinery and are not claimed as new physics.

## N1–N8 no-go discipline

Gate status for a broad stream/compiler impossibility or axiom-pressure
claim: **FAIL / DO NOT SHIP**.  The shipped negative is only the exact tested
statement that blank-tag endpoint FSWAP does not implement the exterior B
layer on the declared direct occupation encoding.

### N1 — alternative-route map

The normalized route families differ in primary carrier and terminal proof
obligation:

1. **Blank-tag endpoint FSWAP — ATTEMPTED.**  It is bounded, tag-clean, and
   exact at number zero and one, but has the displayed 60,600/154,800
   two-particle sign mismatches.
2. **Global ordered/Jordan-Wigner stream — RULED OUT BY PRIOR for the campaign
   contract.**  Cycle 231 gives an exact intertwiner, but its interval support
   grows with held size and violates the no-global-order requirement.
3. **Edge-gauge/auxiliary Majorana stream — UNTESTED / LIVE HERE.**  Cycle 236
   gives bounded update gates conditional on a link sector; a new bounded
   local preparation/constraint mechanism could close the present stream
   residual.
4. **Staggered parity shuttle — UNTESTED / LIVE HERE.**  Cycle 260 computes
   the crossing sign locally over microsteps, but its `4L-1` macro depth and
   head/orientation preparation remain to be retired.
5. **Changed native representative/opposite carrier — PARTIALLY ATTEMPTED /
   LIVE HERE.**  Cycle 522 removes the local Gram collision and re-earns a
   dense seam.  The selected term-to-shadow value decoder is exact here, but
   its nearest-neighbour routing, bare recurrent native amplitude transition, and
   recurrent edge synthesis remain terminal duties.
6. **Non-Pauli subsystem gauge or larger protected edge shadow — UNTESTED /
   LIVE.**  A bounded link register can carry the crossing character without
   blanking it before B, but needs an explicit local code and all-frame update.

Because four constructive families remain live, the broad no-go fails N1.

### N2 — wall-independence audit

For the direct protected-shadow replacement architecture, the one collapsed
open condition is `W_stream`: reproduce the exterior B-layer signs with a
bounded locally prepared carrier.  The onsite coin, contact, parity, inverse,
and frame-correction obligations are closed here.

If the older Wilson/native branch shell is required in addition rather than
replaced, Cycle 523 closes its selected term-to-shadow value decoder.  The
remaining conditional `W_native-dynamics` wall is bare recurrent amplitude update,
erasure, and nearest-neighbour routing.  Stream repair does not close those
duties, and value synchronization alone does not repair the B sign.
Beta/contact selection and physical elapsed time are not inflated into
compiler walls; they are respectively supplied law content and outside this
discrete update theorem.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| `W_stream` / conditional `W_native-dynamics` | no | no | yes |

The reported default wall count is one; the second is explicitly conditional
on retaining the native shell.

### N3 — hidden-wall scan

The proof does not use “standard QFT,” a background parity service, a global
ordering gate, or runtime frame selection.  Compile-time QR, the supercell
origin, blank-site preparation, beta, contact, and factor order are explicit
in the supplied inventory.  “Exterior,” “geometric,” “primitive,” “code,”
and “covariant” are separated.  The only canonical object used is the
explicitly hashed Cycle-219 coin matrix; that is cited retained input, not a
hidden uniqueness assertion.

### N4 — residual matching

| witness | witness residual | Cycle-523 residual | match? |
|---|---|---|---|
| Cycle 219 | actual `beta=-0.3` coin/mass fixture | same matrix and mass | yes |
| Cycle 230 | exterior coin, `g=0.37` contact, `C -> S -> W_g` order | same coin/contact and declared factor order | yes |
| Cycle 231 | endpoint-FSWAP versus exterior B signs | same direct encoding and B-layer mismatch at L5/L6 | yes |
| Cycle 516 | exterior/Koszul versus geometric frame action | same local sign cocycle, now decomposed into CZ macros | yes for local frame correction |
| Cycle 520 | protected-shadow coin/routing obligation | exact seven-M2 onsite primitive completion | yes |
| Cycle 260 | growing staggered shuttle | not the blank-tag endpoint residual | no; live alternative only |
| Cycle 522 | selected opposite-carrier grammar and dense algebraic lift | same 160 valid term patterns; exact value decoder, primitive recurrent transition still open | yes for value synchronization; no for stream residual |

The last two are not used as evidence for the narrow negative.

### N5 — rhetoric audit

“Not a full stream compiler” means: full local M64 is positive; full L5/L6
edge geometry is positive; all one-particle stream states are positive; the
complete two-particle endpoint sign census is negative.  Higher-number
stream sectors were not exhausted and are not needed for the witnessed norm
2, but no lattice-wide impossibility is inferred.  “No host-side adaptive
control” means the runtime list has no input-dependent branch; it does not
deny that QR and coefficient freezing are supplied compile-time work.
“Discrete update order is not causal time” is a scope firewall, not a claim
that no causal-time construction exists.

### N6 — partial-closure path

Cycle 523 itself is the partial closure: it retires the coin, contact, tag
conjugation, local routing, inverse, leakage, and frame-cocycle parts without
an axiom change.  It also retires the native selected-term value-decoding
subwall by a five-monomial relational circuit.  `W_stream` can be retired by
an explicit edge-gauge code, a bounded preparation for the Cycle-236 link
sector, a truly constant-depth
staggered carrier, or a changed representation.  None is a labeling
convention masquerading as new physics, and none requires an axiom merely
because it is unfinished.

### N7 — hostile steelman

A hostile reviewer should reject any global obstruction claim: Cycle 236
already shows that a link Majorana can cancel the offending hopping strings
while keeping runtime update support bounded, and Cycle 523 now supplies the
previously missing elementary onsite circuit and local Koszul frame
correction.  The actionable next construction is to keep one covariant edge
shadow live through the B layer instead of blanking every tag, enforce its
link sector with bounded local checks, and combine its dressed edge gate with
the 100-call-per-cell schedule here.  If the Cycle-522 shell is retained, the
displayed decoder should compute the occupation shadows, while the missing
bare recurrent native transition and physical routing are tested explicitly.  The
terminal obligations are exact:
bounded preparation, `E G = G_physical E` on fixed-number two-particle
witnesses and then full Fock, all 24 frames, inverse, leakage, deletion, and
L5/L6 constant-depth recurrence.  That concrete route makes a broad no-go
premature.

### N8 — cross-cycle echo

Cycle 231's direct occupation compiler first exposed the norm-2 stream sign.
Cycle 236 moved that sign into an auxiliary link sector and obtained bounded
runtime gates, though preparation stayed nonlocal.  Cycle 260 moved it into a
dynamical shuttle, exposing growing macro depth.  Cycles 515/516 showed that
local factor and frame failures can be repaired by relational roles and a
Koszul character.  Cycle 520 then isolated the protected-shadow coin wall,
which Cycle 523 closes locally.  Cycle 522's opposite-carrier route further
shows that representation changes can remove earlier collisions; the exact
degree-two decoder here now connects its selected terms to the private
occupation shadows without assuming independent preparation.  Its dynamic
update and routing boundaries remain explicit.  The cross-cycle record
therefore supports another constructive edge-gauge attempt, not axiom
pressure.

## Dependency impact and next campaign

| wall | Cycle-523 change | remaining obligation |
|---|---|---|
| `C_ref` | unchanged; beta, `g`, block origin, and blank preparation remain supplied | law selection/reference preparation |
| `C_num` | advanced: parity-tag compute/uncompute is exact on full local M64; selected native auxiliaries decode all six shadows exactly | bounded stream-sign carrier; bare recurrent native dynamics if that shell is retained |
| `C_wrap` | L5/L6 supercell and edge sets close under all frames with no geometry failures | larger-size recurrence after stream repair |
| `C_int` | major advance: actual coin and all 15 contacts now have bare two-M2 circuits, inverse, mass, deletion; native value sync is explicit | exact exterior B stream and, conditionally, a primitive recurrent native transition |
| `C_local` | major advance: protected onsite support two, physical radius one, local Koszul frame circuit; native decoder has support-two algebra | bounded local stream-gauge preparation and nearest-neighbour native decoder routing |
| `C_source` | unchanged | autonomous source/response bridge |

The optimal next campaign is a protected-edge tournament centered on the
stream residual.  First try a one-link shadow that remains populated through
B and is locally constrained; compare it directly with the Cycle-236
Majorana sector and a constant-depth reformulation of Cycle 260.  Reuse the
Cycle-523 onsite schedule unchanged.  In parallel, if Cycle 522 remains the
native representative, route its exact decoder on the physical auxiliary
layout and derive a coherent native selected-shell transition.  Require the
first successful edge route to pass the exact L5/L6 two-particle sign census
before expanding to full Fock and recurrent volume.
