---
claim_id: yt_ew_neutral_projector_same_surface_carrier_theorem_note_2026-06-18
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T EW Neutral-Projector Same-Surface Carrier Theorem

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Role:** exact defined-projector algebra; physical carrier bridge remains open.
**Status:** exact support; no positive Y_T closure.
**Primary runner:**
`scripts/frontier_yt_ew_neutral_projector_same_surface_carrier.py`
**Generated output:**
`outputs/yt_ew_neutral_projector_same_surface_carrier_2026-06-18.json`

This is a spectral-projector theorem on one explicitly defined copy of `C^2`.
It identifies a lower coordinate ray by functional calculus of `Q_H`; it does
not identify that vector space with a physical EW, Higgs, or Y_T carrier.

## Claim

On the defined `C^2` surface, introduce the endomorphism

```text
Q_H = T_3 + Y_H,
T_3 = diag(1/2, -1/2),
Y_H = (1/2) I.
```

Thus

```text
Q_H = diag(1, 0),
P_ch = 1_{1}(Q_H) = Q_H,
P_neut = 1_{0}(Q_H) = I - Q_H.
```

The two projectors are orthogonal, rank-one, sum to `I`, and live on the same
defined two-dimensional vector space. With the qubit-shaped notation

```text
P_+ = (I + sigma_z) / 2,
P_- = (I - sigma_z) / 2,
```

the spectral identification forced by `Q_H` gives

```text
P_+ = P_ch,
P_- = P_neut.
```

This proves only that the two displayed projector formulas coincide after both
are placed on the same defined basis. It does not prove that a Y_T
signed-record source and an electroweak/Higgs ray are the same physical
carrier. That same-surface physical identification remains an unsupplied
bridge.

Equivalently, the signed two-outcome generator on this carrier is

```text
epsilon_H = P_ch - P_neut
          = 2 Q_H - I
          = I - 2 P_neut.
```

A source coupled to `epsilon_H` is therefore affinely equivalent to a source
coupled to neutral-ray occupation:

```text
exp(h epsilon_H) = exp(h) exp(-2 h P_neut).
```

The common `exp(h)` factor cancels in the normalized source family, so the
source-coordinate change is `j = -2h`.

## Cited Authority Surface

- [`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md)
  supplies the defined matrices `T_3`, `Y`, their sum, and the lower vector
  `h0 = (0,v/sqrt(2))^T`. It supplies no physical carrier, hypercharge,
  vacuum, or charge operator.
- [`YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md`](YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md)
  supplies the signed-record source-action support packet.
- [`YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md`](YT_SOURCE_COORDINATE_INVARIANT_TOP_W_RATIO_GATE_NOTE_2026-05-25.md)
  supplies the statement that a common top/W response ratio is invariant under
  local source-coordinate reparameterization.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  supplies only the one-qubit algebraic carrier language. It does not derive
  a gauge group, particle content, the Higgs sector, or a physical
  identification with the separately defined `C^2` above.

## Proof

The exact matrices on the defined `C^2` carrier are

```text
I = [[1, 0], [0, 1]],
sigma_z = [[1, 0], [0, -1]],
T_3 = sigma_z / 2,
Y_H = I / 2.
```

Therefore

```text
Q_H = T_3 + Y_H
    = [[1, 0], [0, 0]].
```

Because `Q_H` is a rank-one self-adjoint projector, its spectral projectors
are exactly

```text
P_ch = Q_H,
P_neut = I - Q_H = [[0, 0], [0, 1]].
```

These are also the Pauli projectors `P_+` and `P_-`. The defined lower vector
and any scalar multiple along that ray obey

```text
P_neut H_0 = H_0,
P_ch H_0 = 0,
Q_H H_0 = 0,
P_neut dH/ds = dH/ds,
Q_H dH/ds = 0.
```

The charged upper ray is the complementary spectral projector:

```text
Q_H (1,0)^T = (1,0)^T.
```

The source statement follows from the same projector algebra:

```text
epsilon_H = P_ch - P_neut = I - 2 P_neut.
```

Since `I` and `P_neut` commute,

```text
exp(h epsilon_H)
  = exp(h I - 2h P_neut)
  = exp(h) exp(-2h P_neut).
```

After normalization, the scalar factor `exp(h)` cancels. This is an affine
source-coordinate identity once both expressions are stipulated on the same
defined carrier; it does not supply that physical stipulation.

## Frame Invariance

If a unitary frame change `U` is applied to the defined carrier, then

```text
Q_H' = U Q_H U^dagger,
P_neut' = U P_neut U^dagger,
epsilon_H' = U epsilon_H U^dagger.
```

All projector identities above are preserved. The theorem is therefore not a
coordinate naming trick; it is a spectral-projector identity on the same
two-dimensional carrier.

## Exact Boundary Of The Result

This note supplies the exact projector equality
`P_- = 1_0(T_3+Y)` on a single defined `C^2`. It does not supply the missing
physical same-surface theorem requested for
`yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`. In particular,
equality of two formulas after a shared-basis stipulation cannot establish
that the qubit source and a physical EW/Higgs carrier are the same object.

## What This Does Not Close

This note does not derive positive Y_T closure. It does not claim:

- a top coefficient theorem;
- a coefficient-fixed top/W Feynman-Hellmann response row;
- canonical scalar LSZ normalization;
- physical-scale `g_2(v)`;
- retained top-Yukawa carrier authority;
- retained hypercharge uniqueness authority;
- `m_t`, `y_t`, `v = 246 GeV`, or any observed mass value.

The theorem uses no observed masses, no fitted selector, no `H_unit`, no
`yt_ward_identity`, no `y_t_bare`, no `alpha_LM`, no plaquette/u0 input, and
no PDG comparator.

## Verification

```text
python3 scripts/frontier_yt_ew_neutral_projector_same_surface_carrier.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```

The green result means the defined neutral-projector algebra is internally
checked. It does not prove a physical same-surface carrier identification.
