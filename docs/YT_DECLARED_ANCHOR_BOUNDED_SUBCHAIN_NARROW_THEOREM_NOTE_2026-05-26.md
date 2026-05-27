# YT Declared-Anchor Bounded Subchain Narrow Theorem

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Claim scope:** bounded algebraic subchain of the top-Yukawa lane over the
declared premises `<P>`, `F_adj`, `kappa_EW`, and the Ward-boundary Clebsch
factor. This note proves only the algebraic consequences of those declared
anchors; it does not claim a zero-import numerical prediction and does not
derive the anchors from `Cl(3)` / `Z^3`.
**Primary runner:** `scripts/frontier_yt_declared_anchor_bounded_subchain.py`
**Status authority:** independent audit lane only.

## Inputs

```text
N_c = 3
<P>(beta=6) = 0.5934
F_adj = (N_c^2 - 1) / N_c^2 = 8/9
kappa_EW = 0
Ward Clebsch = 1/sqrt(6)
```

The theorem is intentionally bounded because `<P>` and `kappa_EW=0` are not
derived here. The bounded status is the point of the split: it separates the
closed algebra above declared anchors from the stronger full zero-import
claim, which remains conditional until those anchors are retained-grade.

## Theorem

Given the inputs above and `alpha_bare = 1/(4*pi)`, define

```text
u_0        = <P>^(1/4)
alpha_LM   = alpha_bare / u_0
alpha_s(v) = alpha_bare / u_0^2
K_EW       = 1 / (F_adj + kappa_EW/N_c^2)
g_lattice  = sqrt(4*pi*alpha_LM)
y_t(M_Pl)  = g_lattice / sqrt(6)
```

Then:

```text
alpha_LM^2 = alpha_bare * alpha_s(v)
K_EW(0) = 1/F_adj = 9/8
sqrt(K_EW(0)) = sqrt(9/8)
(7/8) * T_F * F_adj = 7/18     with T_F = 1/2
y_t(M_Pl) = sqrt(4*pi*alpha_LM) / sqrt(6)
```

These are the load-bearing subchain identities that the historical
`YT_ZERO_IMPORT_CHAIN_NOTE.md` used above its declared anchors.

## Non-Claims

This note does not:

- derive `<P>(beta=6)=0.5934` from the lattice path integral;
- derive `kappa_EW=0`;
- run or validate the full two-loop Standard Model RGE stack;
- compare to observed `m_t`, `alpha_s(M_Z)`, `sin^2(theta_W)`, or `v`;
- claim that the historical zero-import prediction is retained.

## Relation To The Historical YT Chain

The audited-conditional parent `YT_ZERO_IMPORT_CHAIN_NOTE.md` had a
`scope_too_broad` repair target: split the clean bounded algebraic/RGE subchain
over declared `<P>`, `F_adj`, `kappa_EW`, and Ward-boundary premises from the
full zero-import numerical prediction.

This note performs that source-side split. It is a reusable bounded theorem
packet for the algebra above declared anchors. The full prediction still needs
separate retained-grade bridge notes for the bounded plaquette insertion and
the connected-trace matching rule before it can be promoted beyond the
conditional perimeter.

## Validation

```bash
PYTHONPATH=scripts python3 scripts/frontier_yt_declared_anchor_bounded_subchain.py
```

Expected result:

```text
FAIL=0
```
