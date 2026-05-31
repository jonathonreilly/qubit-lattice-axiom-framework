# Koide: the per-block count is orientation-blind; the ω-forcing of Q=2/3 reduces to one identification (is b a field or a coupling?)

**Date:** 2026-05-30
**Claim type:** bounded structural localization (positive); reduces the value to one gate
**Status:** structural result. Approves no axiom and no import; sets no audit verdict.
The audit lane sets status and the per-block-vs-per-dimension convention tier.
**Primary runner:**
`scripts/frontier_koide_orientation_blind_count_b_field_gate_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_orientation_blind_count_b_field_gate_2026_05_30.txt`.

## Result (one sentence)

The charged-lepton Koide value reduces to exactly **one** identification — whether the
generation-doublet circulant coupling `b` in `H = aI + bC + b-bar C^2` is the
**dynamical amplitude of a first-order matter field** (`-> ` phase space `-> ` per-block
`-> Q=2/3`) or a **static background coupling** (`-> ` configuration `-> ` per-dim
`-> Q=1`) — with the orientation (conjugation-even) and dynamical (records/cooling)
walls now **cleared** from the per-block count.

## What is cleared

**The count is orientation-blind (F2 — the key theorem).** On the native doublet
Kähler triple (`g=6I_2`, `J2=[[0,-1],[1,0]]` with `J2^2=-I`, `omega=g.J2`,
nondegenerate `det 36`, compatibility `omega(u,v)=g(u,J2 v)` — F1), the conjugation
`b -> b-bar` is the real-linear involution `c=diag(1,-1)`. It **flips the orientation**
(`c J2 c^-1 = -J2`, `c^T omega c = -omega` — "bit i", the `+i`-vs-`-i` choice) but
**preserves the metric** (`c^T g c = g`) and hence the polarization-rank **count**
(`= dim/2 = 1` — "bit ii"). So counting `b` as one mode needs only that `J2`/`omega`
**exist** (they do, natively), **not** a choice of `+i` over `-i`. The conjugation-even
obstruction (which kills the orientation) therefore does **not** block the per-block
count. `Q = trace(H^2)/trace(H)^2 = (1+2r)/3` is `theta`-independent, `= 2/3` at
`r=1/2` (F3).

**Dynamical state-selection cannot reach per-block.** A pure-dark-state **cooling**
channel toward a doublet vacuum needs a jump operator `|f1><f2|` that is provably
**off** the native circulant algebra `span{I,C,C^2}` (Hilbert-Schmidt residual = full
norm — F5; it is off-diagonal in `C`'s eigenbasis, where every circulant is diagonal),
so it is an off-algebra import; and the native dynamics is reversible-unitary +
entropy-increasing **records**, which drives the generation sector to the
maximally-mixed `I/3 = ` trace `= Q=1`. So the per-block reading is **not** reachable by
dynamics.

## What decides it (the action order = the role of b)

The mere **existence** of the native `omega` does **not** force per-block (F4): a
one-complex-dimensional symplectic phase space `(R^2, omega)` geometrically quantizes
to **one** mode regardless of polarization, but the per-dimension reading lives on the
**distinct** 4-dimensional cotangent bundle `T*(R^2)` (`b` a configuration coordinate
with its own momentum) `-> ` **two** modes. The decider is the **order of the action**
`=` the **role of b**:

- **`b` a first-order field-amplitude** (its plane is the phase space, `omega` its
  Faddeev-Jackiw symplectic form) `-> ` 1 mode `-> ` per-block `-> Q=2/3`.
- **`b` a static coupling** (a Yukawa parameter of a fixed `H`) `-> ` configuration
  `-> ` per-dim `-> Q=1`.

The native `(g, J2, omega)` triple is **silent** on which role `b` plays.

## The one remaining gate (and why it is currently an import)

The forcing of `Q=2/3` is conditional on the **B-coupling `->` B-field**
identification: that `b` is natively the dynamical amplitude of the first-order
Kähler-Dirac matter field along the `C_3` doublet isotype, so that
`int dtau b-bar (i d_tau) b` is that field's own kinetic term and `(Re b, Im b)` are its
canonical pair. This is **not** supplied by `omega`. The obstacle (F6): the
retained_bounded Kähler-Dirac field
(`staggered_dirac_substep2_kahler_dirac_equivalence`) is indexed by the cube-corner
**Hamming-weight / form-degree** label of `Lambda*(C^d)`, and its within-generation
(`Lambda^1 -> Lambda^1`) block of `D_KD` is **identically zero** — so the first-order
kinetic structure does **not** directly land on the circulant coupling `b`. The shared
letter `b` is a **notation collision**, not an identification. Supplying the bridge is a
new identification beyond `A1+A2+`retained `->` requires explicit user approval. With it
`-> Q=2/3`; without it, per-block-vs-per-dim reverts to the retained_bounded block-weight
frontier (`koide_q23_block_weight_frontier`, "physical selection unproved").

## Boundary

This is **not** a derivation of `Q=2/3`; it is the sharpest localization: the value is
exactly the **role of `b`** (dynamical field `-> Q=2/3` vs static coupling `-> Q=1`),
with the orientation and dynamical walls cleared. **The next path** (concrete): build
the B-coupling `->` B-field bridge — a representation-theoretic map from the
`Lambda*(C^d)` graded/Hamming-weight pieces onto the `Z_3` regular-rep isotypes, so that
the mass bilinear and a first-order kinetic bilinear factor through the same complex
field whose doublet component is `b`. ("import-required" is current-state, not terminal.)

## Tier (live-ledger-verified)

Load-bearing retained: `koide_q23_block_weight_frontier` (retained_bounded),
`staggered_dirac_substep2_kahler_dirac_equivalence` (retained_bounded),
`koide_c3_generator_rephasing_obstruction`, `koide_circulant_q_two_thirds_algebraic`,
`cpt_exact_real_anti_hermitian_d`, `angular_kernel_underdetermination` (retained_no_go —
the `SO(2)` orientation weight is not unique = the bit-i pin). **Note:**
`koide_emergent_time_eta_conjugation_parity` is **unaudited** on origin/main (its content
is used only, not load-bearing); `koide_signed_eigenvalue_vs_singular_value` is
**audited_FAILED** (not cited). `Q=(1+2r)/3` is re-derived here independently. Complements
`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE` (the canonical consolidated statement).
