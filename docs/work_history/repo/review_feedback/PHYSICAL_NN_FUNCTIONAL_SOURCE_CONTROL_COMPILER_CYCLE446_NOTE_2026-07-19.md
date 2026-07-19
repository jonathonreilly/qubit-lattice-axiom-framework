# Physical NN functional source-control compiler — Cycle 446

Date: 2026-07-19
Authority: none
Audit: unset

## Decision

Cycle 446 is a positive bounded **physical NN functional source-control
compiler**.  It compiles each of the two Cycle-445 dense controls

\[
U_s=\exp\!\left(i\tau M(S)\otimes H_{\rm ex}\right),\qquad \tau=0.05,
\]

onto a seventeen-M2 line.  Sites `0..8` encode exactly one occupied
nine-cycle register mode and sites `9..16` encode exactly one occupied mode
among the reservoir, six field rails, and receiver.  The declared code is
therefore `Q1 x Q1` with constant 17-M2 support.

The Cayley and principal remain unselected supplied functional laws.  Each
full operator is compiled before any state or sector menu: explicitly, the
**full operator before any state or sector menu**.  Its fixed
spectral values are law constants computed from the full analytic nine-cycle
operator.  There is **no eigenray lookup** and no state-conditioned table.  There is
no branch-host control.

## Fixed analytic transforms

The nine-cycle shift is diagonalized by a fixed analytic F9.  The compiler
uses the convention

\[
(F_9)_{jk}=9^{-1/2}\exp(-2\pi i jk/9).
\]

The exact source exchange couples the reservoir to the normalized uniform
six-field mode.  A fixed analytic source-mode basis consists of

\[
|+\rangle=(|R\rangle+|u\rangle)/\sqrt2,\qquad
|-\rangle=(|R\rangle-|u\rangle)/\sqrt2,
\]

five fixed nontrivial F6 field characters, and the untouched receiver.  In
that basis the source eigenvalues are `(1,-1,0,0,0,0,0,0)`.

Adjacent-row complex QR decomposes fixed analytic F9 dagger into 36 adjacent
number-preserving two-M2 Givens rotations.  It decomposes the fixed analytic
source-mode transform into 16 such rotations and one one-M2 phase.  After the
spectral phase layer, the exact reversed adjoints invert both transforms.
Onsite phases are one-M2 primitives.

No general dense completion is invoked by the executed schedule.  Every
Givens primitive is extended on two physical M2 as identity on `|00>` and
`|11>` plus the declared two-mode unitary on the one-particle block.

## Q-preserving nearest-neighbor routing

For a spectral pair `(k,l)`, the router moves register mode `k` only inside
sites `0..8` and source mode `l` only inside sites `9..16`.  The controlled
phase acts only on adjacent boundary sites 8 and 9.  Both SWAP paths are then
reversed.  This route restoration returns the exact logical placement after
every pair phase and preserves both one-hot charges at every primitive
boundary.

The mass-zero F9 character produces two analytic identity pair phases; the
optimized schedule omits them.  The remaining 16 pair phases require 128
routed SWAPs.  Per competing law the exact resource inventory is:

| primitive | count |
|---|---:|
| adjacent number-preserving Givens | 104 |
| one-M2 phases | 2 |
| adjacent register/source controlled phases | 16 |
| within-sector routed SWAPs | 128 |
| total serial primitives | 250 |
| physical M2 | 17 |

The full schedule is declared serial.  The runner also reports a greedy
dependency layering that can execute ordered gates on disjoint supports in
parallel.  Compiler depth is not time, duration, rate, or proper time.

## Frozen tests

The runner must certify separately for the full Cayley and principal
operators:

- reconstruction of all 72 `Q1 x Q1` basis columns;
- physical-code E/G, unitarity, explicit reversed inverse, and leakage;
- primitive unitarity and maximum support two M2;
- exact adjacent boundary placement for every controlled phase;
- exact placement restoration for every routed pair;
- preservation of the two separate Q1 charges at every primitive;
- train and held coherent superpositions, including one seeded superposition
  containing all three train sectors and the held sector;
- preservation of the Cycle-445 mass fixture and selected receiver-weight
  fixtures;
- all 24 proper-cubic frames and the six-direction uniform-source covariance;
- F9 transform, source transform, spectral-phase, and route-restore deletions;
- Q0/Q2, malformed-operator, non-NN, and non-boundary refusal;
- an anti-lookup source scan and construction-order audit; and
- exact resource counts and schedule hashes.

The frozen finite residual tolerance is `2e-11`.  Every destructive deletion
must change the target action by more than `1e-4`.

## Scope and dependency boundary

This closes the narrow Cycle-441/Cycle-445 primitive-synthesis wall for the
two displayed fixed 72-dimensional source controls.  It does not derive the
nine-cycle, its internal orientation, either functional mass law, tau, the
one-hot preparations, the primitive gate alphabet, line layout, serial
schedule, selected receiver rail, or autonomous repetition.  Cayley and
principal remain unselected.

The Cycle-445 receiver squared norm remains a coherent branch diagnostic, not
occurrence and not probability.  This compiler neither selects a realized
branch nor changes the Cycle-445 Record, clock-rate/lapse-candidate, passive
trajectory, proper-time, or gravity boundaries.

The analytic bases, their phase conventions, every Givens angle, spectral
phase angle, routing order, and gate alphabet are supplied compiler
structure.  Derived inside that supplied finite circuit are only its
reconstruction, locality, inverse, code preservation, fixtures, covariance,
and resource counts.

This cycle makes no no-go, minimum-content, shared-obstruction, or
axiom-pressure claim.  It does not edit axioms, foundation, Qualification,
primitives, registries, policies, queues, or audit state.

## Exact result surface

Final cold run: **10 pass / 0 fail**.

| diagnostic | Cayley | principal |
|---|---:|---:|
| analytic F9 diagonalization residual | `3.305600861343288e-14` | `1.8268710471091384e-14` |
| analytic source-basis diagonalization residual | `1.4173565436700267e-15` | `1.4173565436700267e-15` |
| full 72-column E/G residual | `9.109330070266079e-15` | `6.460221477206606e-15` |
| compiled unitarity residual | `1.16186978188901e-14` | `1.136123807368508e-14` |
| explicit reversed-inverse residual | `1.2122720485044512e-14` | `1.1807342712670243e-14` |
| Q1 x Q1 leakage | `0.0` | `0.0` |
| held receiver squared norm | `0.09418478131620463` | `0.0014001584922212088` |
| schedule SHA-256 | `cf6e471dc7d724e67a7742ff25ba7e24042f67e880882f84bc3f336e2f99bdea` | `9c039c09087871707ef8fc7b86b6cda8ed66dc6d2773d6c108661e95dff80599` |

Both schedules have 250 serial primitives and greedy dependency depth 154.
Every primitive has support one or two M2; the largest literal physical
primitive-unitarity residual is `6.292776661376589e-16`.  Physical primitive
charge failures, non-nearest-neighbor failures, boundary-placement failures,
route-restoration failures, and all-frame locality failures are all zero.
The maximum source-target covariance residual is exactly zero.

The maximum train/held/coherent fixture residual, including mass expectation,
is `1.0658141036401503e-14`.  The seeded coherent receiver squared norms are
`0.04270223016115056` for Cayley and `0.004118898680233246` for principal.

Deletion residuals against the intact Cayley compiler are:

| deleted primitive class | residual |
|---|---:|
| F9 transform gate | `7.391036260090295` |
| source-basis transform gate | `7.839377789258258` |
| one spectral phase | `0.05458875491722737` |
| one route-restore SWAP | `5.656854249492378` |

All four exceed the frozen `1e-4` visibility threshold.  The lawful-domain
suite refuses all `9/9` Q0/Q2, non-NN, non-boundary, undeclared-law, wrong-size,
and nonfunctional-operator cases.  The anti-lookup scan finds none of its
forbidden tokens, and the construction trace is exactly
`cayley-full-operator-compiled`, `principal-full-operator-compiled`, then
`state-menu-built`.
