# Gauge-Invariant Meson Same-Matrix Wick-Minor / Exact Finite-Kernel Identity on Listed Carriers — Bounded Note

**Date:** 2026-05-30
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Review boundary:** source-surface finite certificate. The downstream effective status is not set here.
**Primary runner:** [`scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py`](../scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py)
**Cached runner output:** [`logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt`](../logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt)
**Source packet verifier:** [`scripts/meson_os_transfer_source_packet_manifest_2026_06_06.py`](../scripts/meson_os_transfer_source_packet_manifest_2026_06_06.py)
**Source packet verifier cache:** [`logs/runner-cache/meson_os_transfer_source_packet_manifest_2026_06_06.txt`](../logs/runner-cache/meson_os_transfer_source_packet_manifest_2026_06_06.txt)
**Source packet verifier JSON:** [`outputs/meson_os_transfer_source_packet_manifest_2026_06_06.json`](../outputs/meson_os_transfer_source_packet_manifest_2026_06_06.json)
**Restricted source packet verifier:** [`scripts/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.py`](../scripts/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.py)
**Restricted source packet verifier cache:** [`logs/runner-cache/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.txt`](../logs/runner-cache/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.txt)
**Restricted source packet verifier JSON:** [`outputs/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.json`](../outputs/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.json)

## Exact finite claim

For every gauge background in the runner's four listed finite carrier/sample
sets, one full staggered matrix `M[U]` with temporal extent `Lt=28` supplies
all of the following:

1. `slogdet(M[U])`, used in the finite determinant-weighted average;
2. `M[U]^{-1}`, used to form the two cross-reflection covariance blocks;
3. temporal isometries `W_a[U]` and `W_b[U]`, recovered from those blocks;
4. the explicit four-field `2 x 2` Wick minor and its disconnected subtraction.

Let `g^a_j[U]` and `g^b_j[U]` be the selected positive eigenvalues of
the finite cross-reflection blocks of that same `M[U]`. For each listed
Wilson-line matrix `V[U]`, define

```text
G_a[U] = Q[U] diag(g^a_j[U]) Q[U]^dag,
G_b[U] = Q[U] diag(g^b_j[U]) Q[U]^dag,
L[U] = W_b[U] V[U] W_a[U]^dag.
```

The finite spectral construction gives the cross-block intertwiners

```text
A W_a = W_a G_a,
C W_b = -W_b G_b,
W_a^dag W_a = W_b^dag W_b = I,
```

and evaluates the connected part of the explicit Wick minor as

```text
K_Wick(U; V_left, V_right)
  = - sum L_left[p,q]^* L_right[k,l] C[p,k] A[l,q].
```

Those relations give the finite-matrix trace-kernel identity

```text
K_Wick(U; V_left, V_right)
  = Tr[V_left^dag G_b[U] V_right G_a[U]].
```

For `V_left = V_right`, the right side is a matrix Gram,

```text
Tr[V^dag G_b V G_a]
  = ||G_b^(1/2) V G_a^(1/2)||_F^2 >= 0.
```

This is the theorem certified here: an explicit same-`M` connected Wick minor
equals its exact finite spectral trace kernel, configuration by configuration
and after the same finite determinant weights. The runner checks the finite
equalities to floating-point residual, but they are algebraic consequences of
the displayed finite spectral definitions. It is not presented as a
Hilbert-space operator-correlator theorem.

The distinct kernel

```text
G_infinity[U] = 2 Q[U] diag(exp(-2 E_j[U])) Q[U]^dag
```

is retained only as a large-temporal-extent comparator. At the listed open
finite extent `Lt=28`, `G_a`, `G_b`, and `G_infinity` agree within the measured
bounds below but are not asserted to be exactly equal.

## Why the same matrix matters

The prior artifact exposed a reduced connected-loop formula while weighting
with a determinant from a different temporal matrix. The current runner builds
`M[U]` once per configuration. Its determinant, inverse, cross blocks,
isometries, and minor therefore have one common finite carrier.

With

```text
w_U = exp(-S_G[U]) det(M[U]),
Z_Q = sum_(U in Q) w_U,
```

the runner checks

```text
(1/Z_Q) sum_(U in Q) w_U K_Wick(U; V_I, V_J)
  = (1/Z_Q) sum_(U in Q) w_U Tr[V_I^dag G_b[U] V_J G_a[U]].
```

The determinant phase is numerically `+1` on every listed configuration. The
determinant input is linked to
[`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md),
but this note uses only the explicit finite determinants recomputed by its own
runner.

## 2026-07-29 Same-Matrix Four-Field Repair

The applied audit repair target was:

> expose complete SHA-pinned source and stdout and add an independent
> fixed-configuration four-field Wick/minor computation using the same finite
> M whose determinant weights the gauge average.

The repair now exposes the complete runner, a SHA-fresh cached transcript, two
source-packet manifests, and the direct four-field computation. The primary
runner reports `SCORECARD PASS=116 FAIL=0`. The restricted and linked packet
manifests report `PASS=36 FAIL=0` and `PASS=37 FAIL=0`.

The load-bearing numerical bounds are:

| check | worst listed residual |
|---|---:|
| explicit Wick permutation sum vs `2 x 2` covariance minor | `< 1e-12` |
| fixed-background same-`M` minor vs exact finite trace kernel | `8.92e-16` |
| determinant-weighted finite average vs exact finite trace kernel | `3.20e-16` |
| temporal-isometry orthogonality | `< 1e-12` |
| exact finite-kernel cross-block intertwining | `8.89e-16` |
| finite cross-block spectrum vs large-time `2 exp(-2E)` | `3.36e-12` |
| finite normalization vs large-time `C_BLOCK=2` | `8.81e-12` |
| gauge-transformed same-`M` minor | `< 1e-10` |

An independent index contraction checks the Wick sign, conjugation, and
ordering without using the runner's trace helper:
`-Tr(L^dag C L A) = Tr(V^dag G_b V G_a)`. The finite-open correction to the
separate `2 exp(-2E)` comparator is therefore exposed rather than absorbed into
that identity.

## Exact tested domain

The certificate is limited to `m=0.5`, `BETA=0.9`, `NT_BULK=14`, periodic
spatial identifications, and an open temporal chain `t=-14,...,13` with no
temporal wrap. Temporal links are fixed to the identity (temporal gauge), and
each spatial link background is copied unchanged on every time slice. The
tested gauge symmetry is consequently the residual time-independent spatial
gauge transformation. Within that domain, the deterministic runner sets are:

| group and spatial carrier | configurations |
|---|---:|
| U(1), `2 x 2 x 1` | 16-point global-twist quadrature on a fixed link seed |
| SU(3), `2 x 2 x 1` | 6 fixed pseudorandom link configurations |
| SU(3), `2 x 1 x 1` | 8 fixed pseudorandom link configurations |
| U(1), `2 x 1 x 1` | 16-point global-twist quadrature on a fixed link seed |

The U(1) sets are one-parameter global-twist quadratures, not product-Haar
quadratures over all links. The SU(3) sets are finite samples, not exact Haar
integration. Other temporal boundary conditions, nontrivial temporal links,
time-dependent spatial backgrounds, and general time-dependent gauge
transformations remain outside the tested domain.

## Interpretation boundary

The code also confirms that the empty-vacuum number-conserving operator
`Fhat_V = c^dag V c` obeys `Fhat_V|Omega> = 0`. Consequently a literal
empty-vacuum sandwich `Omega^dag Fhat_V^dag T Fhat_V Omega` vanishes. This
runner does not construct a quark-antiquark sector, filled vacuum, or another
operator-space map that would identify the nonzero trace kernel with a
physical transfer-matrix meson correlator. That bridge is separate work.

The certificate likewise supplies no exact full-Haar integral, uniform theorem
in mass/extent/carrier size, extension to other temporal boundaries or the full
time-dependent gauge group, continuum limit, Wightman reconstruction,
Euclidean rotational restoration, Wilson-boundary positivity theorem, or full
interacting reflection-positivity closure. These are exclusions from the
theorem's domain, not impossibility results.

Runner controls K2--K4 are diagnostics of the displayed finite constructions:
they record a per-mode replacement gap, a flat-versus-determinant-weighted
average gap, and a single-step block-metric eigenvalue. No general negative
claim is inferred from them.

## Reproduction

```bash
python3 scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py
python3 scripts/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.py
python3 scripts/meson_os_transfer_source_packet_manifest_2026_06_06.py
```

Expected summaries:

```text
SCORECARD PASS=116 FAIL=0
SUMMARY: MESON OS TRANSFER SOURCE PACKET PASS=36 FAIL=0
SUMMARY: MESON OS SOURCE PACKET PASS=37 FAIL=0
```
