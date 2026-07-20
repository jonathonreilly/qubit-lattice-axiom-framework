# Physical-M2 translation-impulse inertia bridge — Cycle 489

Date: 2026-07-20

Authority: none

Audit: unset

## Target freeze before the final held row

Cycle 489 freezes a translation-character impulse and same-law
passive/kinematic target instead of another
phase-to-clock or source-to-lapse relabel.  A bounded onsite number-phase
gradient shifts the exact lattice translation character of a packet evolved
by the same free coin, specifically the Cycle-219 family.  The operational coordinate is the change in
dimensionless displacement per declared update between opposite kicks.  Its
inverse susceptibility is compared only afterward with the independently
derived origin-curvature mass.

The train fixtures are `beta=(-0.2,-0.3,-0.4)`, `L=4096`, and exact lattice
harmonics `h=(2,4)`.  The common packet width is `0.01`, evolution has 160
declared applications, and the displacement fit uses applications 40–160.
The row `beta=-0.35,L=8192,h=3` was touched during exploration and is
disclosed as a pilot, not held.  Before any `beta=-0.37` result, the final
held row was frozen at `beta=-0.37,L=12288,h=7`.

The fixed susceptibility convention is

```text
q = 2 pi h/L,
chi_impulse = -(d_plus-d_minus)/(2q),
M_impulse = 1/chi_impulse.
```

The minus sign follows the repository FFT/stream convention: multiplication
by `exp(+iqx)` shifts the translation character by `+q` and the packet
displacement in the displayed coordinate by the opposite sign.  Required
thresholds are exact character residual below `3e-13`, opposite-kick
displacement residual below `3e-11`, relative impulse/curvature mass residual
below `1%`, selected-band weight above `0.9995`, boundary weight below
`1e-16`, and physical E/G, inverse, leakage, constraint, covariance,
deletion, and malformed-domain controls under their frozen tolerances.

Beta preparation remains supplied.  No mass law is selected by assertion:
the update consumes only the coin and kick, while the curvature formula is an
independent post-evolution comparator.

## Semantic boundary

Phase is not energy.  Update count is not time.  A generator element is not a
rate.  Response is not gravity.  Norm weights are not probability.  The
centroid effect is not a Record, occurrence, Born frequency, or realized
history.  There is no no-go, minimum-content, shared-obstruction, or axiom
pressure claim.

## Frozen result

The immutable run returns `11 PASS / 0 FAIL` and

```text
RESULT PHYSICAL_M2_TRANSLATION_IMPULSE_INERTIA_BRIDGE_CERTIFIED
```

The exact character-shift maximum is `1.3357370765021415e-16`.  The
opposite-kick displacement sum has maximum absolute residual
`5.551115123125783e-17`.  The independently extracted impulse and curvature
coordinates are:

| disposition | beta | L | h | `M_impulse` | `M_curvature` | relative residual |
|---|---:|---:|---:|---:|---:|---:|
| train | -0.20 | 4096 | 2 | `0.29958207570229667` | `0.30100403975735984` | `0.004724069670989928` |
| train | -0.20 | 4096 | 4 | `0.29990560220442597` | `0.30100403975735984` | `0.0036492452188326974` |
| train | -0.30 | 4096 | 2 | `0.45338628318931673` | `0.4534056690336209` | `0.00004275606951598121` |
| train | -0.30 | 4096 | 4 | `0.4535485186538038` | `0.4534056690336209` | `0.0003150591841680761` |
| train | -0.40 | 4096 | 2 | `0.6099070355444604` | `0.6081301180758897` | `0.002921936302370254` |
| train | -0.40 | 4096 | 4 | `0.6100544397800189` | `0.6081301180758897` | `0.003164325605542695` |
| disclosed pilot | -0.35 | 8192 | 3 | `0.528507440762527` | `0.5304258709057169` | `0.003616773329540246` |
| held | -0.37 | 12288 | 7 | `0.5642976694520323` | `0.5614195348806557` | `0.005126530860719791` |

The strongest held result is therefore a `0.513%` match, not an exact mass
identity.  The finite packet width, kick, and fit window remain visible in
that residual.  Doubling the longitudinal size from `4096` to `8192` at the
same `beta=-0.3` and exactly the same `q` changes `M_impulse` by only
`7.55e-15`; this is a size control, not a continuum theorem.

The minimum selected-branch norm weight is `0.9996865123092888`, the maximum
boundary norm weight is `2.053419978387062e-30`, the maximum opposite-kick
inverse residual is `1.9373049248589925e-13`, and maximum norm drift is below
`9.75e-14`.  These are norm diagnostics, not probabilities.

## What is operational and what is compared afterward

Let `T_x` be the one-cell translation on the periodic longitudinal direction.
For an exact lattice character `q=2 pi h/L`, the physical onsite number phase
obeys on the declared code

```text
K_q^dagger T_x K_q = exp(i q) T_x.
```

Thus `q` is fixed by an executed translation-character identity, not chosen
from the desired mass.  The same Cycle-219 coin then evolves both `+q` and
`-q` packets.  The centroid-effect slope over the frozen update window gives
the dimensionless displacements `d_plus,d_minus`.  Only after constructing
`chi_impulse` does the runner call the independent origin-curvature routine.

The response calculation is the exact transverse-zero-momentum reduction of
a declared periodic `L x 3 x 3` torus.  Uniform transverse amplitudes make the
two transverse streams act trivially on that reduced coordinate without
deleting them from the physical law.  The runner does not materialize the
entire `L=12288` physical word.  Literal finite-volume physical E/G is checked
separately on train `4 x 3 x 3` and held `6 x 3 x 3` representatives, while
the large response uses the same local factor rules in their exact reduced
sector.

This is a kinematic impulse/mobility coordinate under a supplied kick.  It is
not the Cycle-204 weak-lapse force law, not the Cycle-442/447 source corridor,
and not the Cycle-464 prepared-field backreaction fixture.  It makes no
claim of sustained acceleration.

## Physical M2 compiler surfaces

There are three deliberately separated compiler statements.

1. **Direct Q1 corridor.**  Each coarse occupation mode maps to one physical
   M2 excitation.  An onsite coin acts on six M2, each nearest-neighbor stream
   is a two-M2 FSWAP, and contact has six-M2 onsite support.  On global Q1,
   FSWAP equals SWAP and there is no parity string.  The finite-volume code
   has 216 train and 324 held columns, zero leakage words, and maximum E/G,
   inverse, and norm residual `5.241284188561028e-16`.  This route uses six
   physical M2 per cell at constant overhead.
2. **Full local M64 preservation.**  The Cycle-311 role-gauge compiler checks
   all 64 local Fock columns, not just Q1.  At compiler sizes `L=3` and held
   `L=6`, the coin and number-phase kick have maximum E/G, inverse, leakage,
   constraint, and Gram residual `6.2861550631145756e-15`.  The kick is the
   complete number lift `exp(i q x n)` and commutes exactly with the onsite
   contact phase.  This surface uses the inherited 23-M2 installed cell.
3. **Physical edge preservation.**  The actual Cycle-315 two-cell role-gauge
   encoding on total `Q<=1` has 13 logical columns and 244 physical rays.
   Both the free-plus-contact edge and character-kick ambient completions
   intertwine and invert with maximum residual
   `4.3649382034753955e-16`.  All 24 edge frames, 93,312 role group-law tests,
   and 4,374 translations have zero failures.

The direct Q1 volume compiler supplies the large-response sector.  The full
local M64 and bounded edge compilers prove compatibility with the existing
physical matter substrate.  They do not amount to a full-number recurrent
M64 volume theorem; overlapping role registers and a recurrent all-number
schedule remain open.  The direct Q1 sector is preserved dynamically but its
global-one-particle preparation is supplied rather than locally generated.

There is no global Jordan-Wigner order, no global parity service, and no host
query during an update.  The proper-cubic frame transports the whole
`L x 3 x 3` apparatus and its kick axis.  Carried covariance is not a boost or
Lorentz theorem.

## Mass, contact, deletion, and malformed controls

All response momenta are rotated through all 24 proper-cubic frames; maximum
band-phase covariance residual is `6.38378239159465e-16`.  The Cycle-219 mass
fixture remains `0.4534056541748851`.  The independent three-cell Cycle-230
contact remains nontrivial on 645 columns.  Contact is identity in the packet
Q1 sector and is therefore a preservation control, not the cause of the
impulse response.

Required controls return:

| control | result |
|---|---:|
| kick deletion response numerator | `0` |
| intact `beta=-0.3,h=2` response numerator | `0.01353354386546458` |
| coin deletion response numerator | `2.3055816991538262e-17` |
| one stream-arm deletion state residual | `0.6005436878794883` |
| malformed non-character seam residual | `1.2822600789086944` |
| malformed beta/size/harmonic rejections | `3/3` |

The kick, coin, and stream are all load-bearing for this response.  These are
route-local necessities, not minimum-content claims.

## Current common-controller boundary

Cycle 441 can place beta in a coherent nine-M2 register and construct its
common Cayley mass operator without a beta-specific host lookup.  Cycle 489
does not compose that dense controller because the response target is already
a discriminator of the free coin itself, and importing the controller would
add supplied ring orientation, sector preparation, matrix functions, and
scales without changing the observable.  Beta/species preparation and mass
spectrum generation therefore remain explicit supplied structure.  A future
controller-plus-impulse composition can test coherent superpositions of
mobilities without a lookup seam.

## Supplied, derived, and open inventory

Supplied:

1. the Cycle-219 one-parameter coin family and each beta preparation;
2. the direct Q1 occupation meaning, blank physical M2 state, and global-Q1
   packet preparation;
3. the Cycle-311/315 role-gauge encoders and off-code identity completions;
4. periodic `L x 3 x 3` apparatuses, origin, axis, packet width, kick
   harmonics, 160 applications, fit window, centroid effect, thresholds, and
   tolerances;
5. proper-cubic frame transport and factor order; and
6. compile-time coefficient synthesis for the bounded onsite matrices.

Derived and executed:

1. the exact translation-character shift for every kick;
2. opposite-kick displacement susceptibility and train/pilot/held inertia
   rows without using the curvature mass in the update;
3. direct finite-volume Q1 E/G and inverse plus full local M64 and bounded-edge
   physical compatibility;
4. selected-branch, boundary, inverse, covariance, size, deletion, malformed,
   and resource controls; and
5. unchanged mass and 645-column contact fixtures.

Open:

1. physical generation or empirical selection of beta and a mass spectrum;
2. autonomous packet, kick, and centroid-effect preparation plus primitive
   synthesis;
3. a full-number recurrent volume compiler beyond direct global Q1;
4. calibration of the dimensionless character and displacement coordinates to
   observed momentum and duration;
5. interaction-dressed inertia, material source law, passive gravity, and
   reciprocal backreaction; and
6. Record formation, occurrence, Born probability, and realized history.

## Prior-art and novelty boundary

Quantum-walk group displacement, phase-gradient kicks, finite-difference
mobility, fermionic occupation encodings, exterior lifts, and FSWAP circuits
are prior-art territory.  Cycle 489 claims only the repository-specific
composition: the Cycle-219 common coin, exact translation-character kick,
direct physical-M2 Q1 volume compiler, compatibility with the Cycle-311/315
role-gauge M64/edge substrate, all-frame and held controls, and the resulting
operational impulse/curvature comparison.  Global novelty priority is not
asserted.  Thirring machinery is neither used nor compared.

## TOE dependency ledger

| wall | Cycle-489 movement | residual |
|---|---|---|
| `C_ref` | momentum displacement is fixed by an exact translation-character identity rather than a host mass lookup | beta/species, packet, kick origin/harmonic, and effect preparation remain supplied |
| `C_num` | train, pilot, held beta/kick rows plus exact doubled-size control | no empirical calibration, asymptotic packet theorem, or continuum/boost limit |
| `C_wrap` | none | update count is not time; displacement per update is not a physical rate |
| `C_int` | free-coin kinematic response reaches physical M2 and preserves contact | contact is inactive in Q1; interaction-dressed inertia and a selected impulse interaction remain open |
| `C_local` | direct Q1 volume E/G plus full local M64 and bounded-edge compatibility | full-number recurrent volume role compatibility and primitive synthesis remain open |
| `C_source` | none | kick is supplied, not a material source; source/stress/gravity response remains open |

The matter/inertia lane advances from a phase/curvature label to a same-law
finite displacement susceptibility on physical M2.  The time, source/gravity,
Record, and Born terminals do not advance.

## No-Go Discipline Gate

The newer `origin/main` no-go skill was read directly after the dirty-worktree
freshness check.  This is a bounded positive result with named open structure,
so N1–N8 are recorded.  Gate result: **FAIL for any broad substrate,
full-number, mass-law, gravity, or axiom-pressure negative.**  The positive
Q1 result remains certified.

### N1 — normalized alternative-route enumeration

| family: object / mechanism / terminal obligation | marker | disposition |
|---|---|---|
| direct Q1 occupation volume / character kick plus free displacement / operational impulse coordinate | `ATTEMPTED` | positive in Cycle 489 |
| Cycle-311/315 role-gauge M64 / bounded ambient completion / local and edge physical compatibility | `ATTEMPTED` | positive locally and on one edge; recurrent full-number volume remains open |
| coherent Cycle-441 beta register / common mass functional plus controlled kick / superposed mobility without lookup | `OPEN — NOT ATTEMPTED` | concrete next composition |
| Cycle-210/204 position gradient / repeated weak forcing / long trajectory inertia | `RULED IN BY PRIOR` | positive comparator with a supplied host gradient, not the current physical kick theorem |
| local quantum field scattering / exchanged character and reciprocal recoil / autonomous impulse transfer | `OPEN — NOT ATTEMPTED` | would remove the externally prepared kick |
| interacting bound M64 packet / contact-dressed band response / equality of free and dressed inertial coordinates | `OPEN — NOT ATTEMPTED` | contact is only preserved here |
| Cycle-464 relaxed field / reciprocal field-matter vertex / sourced passive response | `RULED IN BY PRIOR` | bounded positive response but different source/gravity residual |

These are distinct in primary object, load-bearing mechanism, and terminal
obligation.  The constructive and open routes defeat every broad negative.

### N2 — wall-independence audit

Collapse the open structure to `W_beta` (spectrum/preparation), `W_inst`
(autonomous kick/packet/effect instrument), `W_full` (full-number recurrent
volume and dressed inertia), and `W_cal` (physical momentum/duration
calibration).

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `W_beta,W_inst` | no | no | yes |
| `W_beta,W_full` | no | no | yes |
| `W_beta,W_cal` | no | no | yes |
| `W_inst,W_full` | no | no | yes |
| `W_inst,W_cal` | no | no | yes |
| `W_full,W_cal` | no | no | yes |

Source/gravity, Records, and Born occurrence are downstream lanes, not extra
walls inflated into this kinematic target.

### N3 — hidden-condition scan

The note exposes beta, Q1 preparation, physical encoders, identity
completions, torus sizes, transverse reduction, origin, axis, packet width,
harmonics, applications, fit window, centroid effect, frames, coefficients,
thresholds, and tolerances.  Trigger phrases were scanned.  “Physical M2” is
backed by the displayed encodings rather than a background identification.
No “naturally,” “obviously,” “standard QFT,” “framework provides,” or hidden
“bridge context” supplies a load-bearing step.

### N4 — residual matching

| witness | witness residual | Cycle-489 residual | match? |
|---|---|---|---:|
| Cycle 219 | rest/curvature/forced inertia of the common coin with beta supplied | same free coin and origin-curvature comparator | yes |
| Cycle 311 | full local M64 physical coin/contact compiler | local full-M64 compatibility of kick and coin | yes |
| Cycle 315/319 | physical edge and multi-edge M2 seams | bounded edge compatibility and 645-contact preservation | yes locally; not cited for volume closure |
| Cycle 204 | host weak-gradient passive trajectory | externally supplied force comparator | no; context only, not support |
| Cycle 442/447 | source-driven sustained trajectory classifier | no sustained-trajectory claim here | no; context only, not negative support |
| Cycle 464 | prepared relaxed-field passive response | no field source in Cycle 489 | no; distinct residual and context only |

Nonmatching trajectory and source citations are not counted as evidence for
the positive impulse compiler or against other routes.

### N5 — rhetoric and resolution audit

“Direct Q1 is not full-number volume” is proved only at sector resolution:
the literal volume E/G covers global Q1, while full local M64 and one edge are
checked separately.  No lattice-wide full-number negative is made.  “Phase is
not energy,” “update count is not time,” “response is not gravity,” and “norm
weight is not probability” are semantic non-identification firewalls: this
runner supplies no calibration or terminal law at site, mode, block, or
lattice resolution.  They are not impossibility claims.

### N6 — partial-closure path scan

No new axiom is implicated.  Cycle 441 supplies a direct coherent-beta
composition path; the direct occupation compiler can be widened sector by
sector; Cycle 319's joint-role and staggered-slot mechanisms can attack
overlap scheduling; a local field-scattering vertex can replace the supplied
kick; and an operational clock comparison can calibrate the dimensionless
displacement coordinate.  Each is an import-retirement construction under
the current substrate.

### N7 — hostile steelman

A hostile reviewer should grant only a reversible Q1 mobility fixture under a
prepared character kick.  The response packet, beta, harmonic, fit window,
and centroid effect are supplied; the large physical word is reduced rather
than materialized; contact does no work in Q1; and the full role-gauge M64
volume remains uncompiled.  Cycle 441 already gives a concrete way to remove
beta-specific lookup, while a local field-scattering preparation could make
the impulse autonomous and interaction-dressed.  Those terminal obligations
are mathematically actionable and untested, so a broad closure or obstruction
claim would be premature.

### N8 — cross-cycle echo

Cycle 204 turned a dispersion coordinate into a trajectory observable but
left the gradient on the host.  Cycle 219 aligned the common-coin mass
coordinates without generating beta.  Cycles 311/315/319 successively
physicalized local and shared-edge M64 factors.  Cycle 441 removed the
beta-specific lookup at the cost of a supplied dense controller.  Cycles
442/447 showed that one source corridor can fail a sustained classifier,
while Cycle 464 later recovered a different bounded passive response on a
relaxed 3D field.  The repeating mechanism is constructive enlargement and
composition, not constitutional change.  The same mechanism can close the
current spectrum, instrument, full-number, or calibration imports.

**Broad no-go: FAIL. Minimum-content claim: FAIL. Shared obstruction: FAIL.
Axiom pressure: FAIL.**  There is no axiom pressure.

## Verification

```bash
python3 -m py_compile \
  scripts/physical_m2_translation_impulse_inertia_bridge_cycle489_2026_07_20.py
python3 \
  scripts/physical_m2_translation_impulse_inertia_bridge_cycle489_2026_07_20.py
```

The final runner SHA-256 is
`8e1d042b68f6505e62cb6c0c92469cd5fa3bdb84779f6ba7e96144a4254b69f0`.
The final cold run completed in `8.39 s` external wall time with raw Darwin
maximum RSS `144654336` bytes, below the declared ordinary campaign envelope.
After removing the last legacy API name from the norm-weight implementation,
an independent root cold rerun returned the same `11 PASS / 0 FAIL` and
certification token in `7.69 s` real, `7.08 s` user, and `0.13 s` system,
with `144,506,880` bytes maximum resident set size.
No axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit-status
surface is edited.
