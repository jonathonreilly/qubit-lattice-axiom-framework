# Two-block complete-Q<=2 many-field transport — Cycle 423

Date: 2026-07-19
Authority: none
Audit: unset

## Construction and code

Cycle 423 composes two seven-M2 reservoir/field stars across one physical edge. The installation has **two reservoir M2 and twelve field M2**. The executed basis is the **complete total-Q<=2 code** of the fourteen hard-core bits:

```text
Q=0:  1 state
Q=1: 14 states
Q=2: 91 states
total dimension 106.
```

This includes every reservoir/field placement and every two-excitation collision state allowed by the fourteen M2. It is not the Cycle-419 vacuum/Q1-only code and has no global field blockade.

The fixed local schedule is:

1. the existing full hard-core field coin on each six-field block—it acts by the Cycle-214 coin on field number one and by identity on the other local field-number sectors;
2. the **Cycle-421 many-field vertex** on each reservoir-plus-field star;
3. one exact **directed field-bit SWAP** between block A direction `d` and block B direction `reverse(d)`.

All three factors preserve total excitation number. The adjoint executes the exact reverse schedule.

## Operator and continuity controls

The runner materializes the entire 106-dimensional update, rather than sampling histories only. It checks finite unitarity and inverse on every basis column, the commutator with total `Q`, and the block-local continuity identity

```text
G^dagger Q_A G - Q_A
 = L^dagger (S^dagger Q_A S - Q_A) L,
```

where `L` is the local coin-plus-vertex layer and `S` is the boundary SWAP. This is a local excitation ledger, **not energy, source, work, time, probability, or a Record**.

The two seven-site stars contain one adjacent boundary-rail pair. Rotating both stars and the chosen edge sends `G_d` to `G_(R d)`. The full 106-state update is checked in **all 24 proper-cubic edge frames**.

## One-source history and adjoint return

The one-source history begins at `|R_A=1>` with every other bit blank. One fixed update emits a hard-core scalar field and transports the selected boundary component to block B. The neighboring field weight is

```text
sin^2(theta)/6.
```

A second forward update remains inside `Q=1`. Applying the adjoint to the first-update state returns and reabsorbs every amplitude into the original reservoir exactly. This is scheduled inverse recovery. An autonomous same-forward return is not claimed.

Coupling/vertex deletion leaves every field rail blank. Transport deletion leaves the emitted field in block A and zero field weight in block B.

Thus coupling and transport deletion are tested independently.

## Two-source, collision, and saturation history

The two-source history begins at

```text
|R_A=1> tensor |R_B=1>,  Q_total=2.
```

The two Cycle-421 vertices generate total two-field weight

```text
sin^4(theta) = 0.01585061262182459.
```

The boundary SWAP moves single occupied edge rails across the edge. Consequently it creates positive **same-block two-field** weight: one transported edge excitation can arrive beside the other block's non-edge excitation. With transport deleted, the same-block two-field weight is exactly zero. This directly witnesses genuine two-field transport rather than only two independent untransported emissions.

The `11` occupied-edge collision is a lawful hard-core SWAP input and remains `11`; no excitation is deleted or duplicated. Separately, the Cycle-421 locally saturated `R=1,F=111111` state has zero emission and remains unchanged. Both controls are explicit even though local field saturation lies outside the global `Q<=2` execution code.

Together these are the explicit saturation and collision controls.

Applying the adjoint returns the transported two-source state exactly. A second forward update retains nonzero two-field content and exact `Q=2` conservation.

## Comparison boundary

Cycle 423 preserves the Cycle-421 two-independent-vertex total two-field weight because the field coin and boundary SWAP preserve field number. The older two-tick candidate reported

```text
two-field weight                 0.002201473975253681
missing conjugate source value  -0.15248255286187232.
```

The present weight differs because the schedules and preparations differ. The runner reports the difference and ratio but does not force a match. Cycle 423 has no carried source coordinate, so the older missing coordinate remains open rather than being declared canceled.

## Matter/contact spectator

One M64 matter cell and its intrinsic contact phase are joined as identity spectators. The resulting `64 x 106 = 6784` basis update has an exact sparse inverse, zero matter-block leakage, and zero contact commutator. The Cycle-219 mass-normalized angle is preserved. This is a compatibility control, not matter recoil or source work.

## Supplied, derived, and open

Supplied:

1. two seven-M2 star blocks, the finite boundary, chosen directed edge, and total-`Q<=2` preparation;
2. the Cycle-421 many-field vertex and fixed mass-normalized angle;
3. the existing full hard-core field coin and coin–vertex–stream order;
4. ordinary two-M2 directional SWAP and proper-cubic direction action;
5. one M64 matter/contact spectator and the diagnostic initial histories/readout.

Derived:

1. the complete 106-state update with exact inverse, `Q` conservation, and local continuity;
2. all-24 directed-edge covariance and independent deletion visibility;
3. a one-source transported history with exact adjoint return/reabsorption;
4. a two-source history with genuine same-block two-field transport plus collision and saturation controls.

Open:

1. autonomous same-forward recurrence/return rather than scheduled adjoint recovery;
2. a larger cubic lattice, carried reservoir/matter, recoil, contact work, and source calibration;
3. closure of the older missing source coordinate under a common frozen schedule;
4. energy/source interpretation, physical time, Born law, actual Records, metric, and gravity.

No squared-norm expectation controls a gate. No schedule is called time, number is not called energy, and a two-field weight is not called a Born probability. This is a bounded construction with no negative, no-go, shared-obstruction, or axiom-pressure claim.
