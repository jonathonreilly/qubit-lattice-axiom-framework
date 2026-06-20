# Block01 section — R-N4-REGDIR (clause N4, axis-label)

**Route:** R-N4-REGDIR — genuinely attempt to DERIVE a *non-transportable*
registration-direction bridge for B-AXIS clause N4 (which Euclidean direction is
the time/evolution axis), modeling record-accumulation as a Lieb-Robinson /
causal-cone monotone over the `Z^3` lattice, WITHOUT presupposing a generator.

**Date:** 2026-06-20
**Runner:** `scripts/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py`
**Cached log:** `logs/runner-cache/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.txt`
**Runner result:** `TOTAL: PASS=20 FAIL=0`

**Posture:** this was a genuine fresh derivation attempt — the one route every
in-flight single-clock branch flagged "live-positive" but none built. The
attempt was carried out for real and the load-bearing wall is named below with
its retained authority.

## The exact thing attempted

The standing N4 wall is the exact signed exchange certificate on the staggered
surface
```
W = P_{tau<->1} . diag((-1)^{x_tau x_1}),    W M_KS W^T = M_KS   (resid 0).
```
No *static* Euclidean-surface structure breaks `W` (OS/GNS, durability,
chirality, finite-speed cone — all transport, prior 2026-06-11 no-go). The open
question this route attacks: does a **record-accumulation / causal-cone
monotone** — a dynamical object rather than a static surface structure —
single out a unique evolution-generating direction intrinsically, breaking `W`,
using **A_min content only** (Lattice adjacency + Quantum one-qubit algebra +
Record durable additive registration)?

A CRACK would be: a monotone built from A_min that breaks `W` without being
handed a generator/arrow/pointer datum. The honest alternative is RELOCATION:
the monotone is `W`-transportable, or it only breaks `W` by importing an
explicit OPEN-GATE datum.

## A_min-only method and worked steps

Four legs, each a real construction checked with explicit residuals.

**[BALL] The A_min-only record-accumulation monotone is direction-free.**
The most honest record-accumulation monotone available from A_min is
`m(r) = #{registered sites within lattice graph-distance r of a base region}`
— Lattice supplies graph distance, Record supplies the finitely-additive count.
This object carries **no candidate direction**: graph distance on `Z^3` is
invariant under `x_mu -> -x_mu` in every axis, so "accumulation along `d`" equals
"accumulation along `-d`". Computed: the ball operator `B_r` commutes with every
single-axis reflection (`max resid 0`), `W B_r W^T = B_r` exactly (`resid 0`),
and Record additivity over disjoint graph-distance shells `I(ball)=sum_k I(shell_k)`
holds with undirected shells (`resid 0`). A *ball*, not a *cone*. To turn it into
a cone one must add a generator and a time variable — both outside A_min.
→ **Relocation 1.**

**[DYN] A genuine Lieb-Robinson cone requires a generator, and the generator
transports under `W`.** Built a real 5-site nearest-neighbor TFIM and the
Heisenberg cone `C(x,y;t)=||[alpha_t(O_x),O_y]||`, `alpha_t(O)=e^{itH}O e^{-itH}`.
(i) At `t=0` the cone is a single point: `[O_x,O_y]=0` for all `y != source` by
raw equal-time tensor locality (M1) — no propagation front, no direction
(`equal-time cone = [2.0,0,0,0,0]`). (ii) With a supplied `H` the cone spreads
(`cone(t=0.6)=[1.82,0.82,0.07,0.002,0]`) — a genuine LR front exists ONLY once a
Hamiltonian is supplied (the M1 note states M2 "requires a Hamiltonian ...
Heisenberg evolution," out of A_min scope). (iii) The `W`-conjugate generator
`H' = P_pi H P_pi^T` gives an **identical** cone after relabeling
(`max|cone - relabeled| = 7e-16`): the dynamical cone transports *with* the
generator. Supplying `H` to make the cone non-degenerate also supplies the axis
it would "select" — the cone consumes B-AXIS to derive B-AXIS (circular).
→ **Relocation 2.**

**[ARROW] The accumulation direction is a supplied boundary (past hypothesis).**
A "record-accumulation monotone" presupposes a *direction* of accumulation
(records go up). Reproduced the ARROW note's structural fact on an explicit
time-symmetric update: the SAME map gives an increasing record profile from a
low-record start and a decreasing one from a high-record start — the arrow is the
boundary's, not the map's. Per `ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05`,
record formation derives the arrow's *direction* = "away from the low-record
boundary" but its existence is "in the initial condition, not the dynamics" = the
past hypothesis = a **universal-floor OPEN input**. So the monotone's
directionality is a supplied boundary datum. → **Relocation 3.**

**[PROD] The real crack attempt — does record-PRODUCTION break `W`? No.**
Modeled record production as a CPTP map. (i) An axis-agnostic site-diagonal
registration/dephasing map `D` is exactly `W`-covariant: `D(W M W^T)=W D(M) W^T`
(`resid 0`) — `W` is a signed site permutation, so it preserves the site-diagonal
production subalgebra. (ii) The uniform realized-outcome broadcast POVM
`{P_a ⊗ P_b}` is complete (`sum K^dag K = I`) and is permuted into itself by the
site-swap (covariant) — a site-symmetric A_min production map is exchange-
symmetric. (iii) FALSIFIER/WALL: a production map that registers along ONE
distinguished register axis (asymmetric pointer basis) DOES break swap-covariance
(`break = 3.44`) — but that axis is a **supplied readout-context / pointer-basis
datum**, exactly what Record withholds ("A record supplies no readout context,
decomposition"). That datum *is* the registration-direction bridge, undischarged.

## Honest OUTCOME

**Relocated to open gate — NOT cracked.** Every A_min-only record/causal-cone
monotone is either `W`-transportable (the static accumulation ball; the
record-production superoperator) or becomes direction-selecting only by importing
an explicit OPEN-GATE datum: a generator (the LR cone), an arrow/initial-
condition boundary (the past hypothesis), or an asymmetric pointer/readout axis
(the registration-direction datum itself). Record-production does NOT break the
`tau<->x_1` exchange intrinsically. The route confirms — by genuine construction,
not assertion — that the live-positive flag was optimistic: the registration
direction relocates cleanly onto the record-production-dynamics / arrow OPEN GATE.

## Named load-bearing wall + authority

**Wall:** record-production dynamics, the arrow/initial-condition (past
hypothesis), and the readout-context/pointer-basis are EXPLICIT OPEN GATES
outside axiom content. A_min (Lattice/Quantum/Record) supplies no dynamics, no
causal cone, no time metric, no readout context, and no arrow; therefore no
A_min-only monotone can be non-transportable across the `W`-equivalent axes.

**Retained authority:**
- `MINIMAL_AXIOMS_2026-06-05.md` — Lattice "does not supply a dynamics, ...
  causal cone"; Record "supplies no readout context, decomposition, ...
  measurement/decoherence dynamics, time metric, ... occupancy rule"; and the
  open-gate list "arrow, measurement, decoherence, record-production dynamics."
- `ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`
  (bounded reading) — the arrow's existence is in the initial condition (past
  hypothesis / universal floor), not the dynamics.
- `POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md` (retained_no_go) — record
  event order carries no lattice-axis label and no clock direction without a
  supplied clock map.
- `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md` (retained_no_go) — N4
  (axis/transfer uniqueness) is the clause attacked; Stone uniqueness is
  transfer- and tau-relative.
- `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`
  (M1, generator-free) — equal-time `[O_x,O_y]=0`; the (M2) LR lightcone
  "requires a Hamiltonian ... Heisenberg evolution," out of A_min scope.

## What the consolidated no-go should carry forward (N1/N7)

R-N4-REGDIR is now a *genuinely built* (not deferred) entry. For the N1
≥5-route enumeration it adds three distinct, recomputed witnesses that the
record-accumulation/causal-cone route fails:
1. the A_min record-accumulation monotone is a direction-symmetric **ball**
   (`W`-invariant, reflection-symmetric in every axis) — counting supplies a
   magnitude, never an axis;
2. a non-degenerate **Lieb-Robinson cone requires a supplied generator**, and the
   `W`-conjugate generator gives an identical cone (cone transports with `H`;
   circularity — consuming B-AXIS to derive B-AXIS);
3. record-**production** is `W`-covariant when axis-agnostic; it breaks `W` only
   when handed an asymmetric pointer/readout-axis datum = the registration-
   direction datum, which Record explicitly withholds.

For N7 (steelman): the "record-production singles out the evolution direction"
steelman is answered — production per se is exchange-symmetric; its directional
content is entirely the supplied arrow/pointer-basis datum, an OPEN GATE. B-AXIS
stays LIVE; this route does not close it and sets no audit status (independent
audit lane remains sole status authority).
