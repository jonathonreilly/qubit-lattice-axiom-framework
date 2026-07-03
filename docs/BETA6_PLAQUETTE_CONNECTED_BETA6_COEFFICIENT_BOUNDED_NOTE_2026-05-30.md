# Beta=6 SU(3) Wilson Single-Plaquette — Exact Order-beta^6 and Order-beta^7 Coefficients

**Date:** 2026-05-30
**Type:** bounded_theorem (two exact strong-coupling series coefficients plus a
finite order-beta^7 support reduction; does NOT close beta=6)
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not quote, set, or predict audit outcomes.
**Primary runner:** [`scripts/frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py)
**Maxorder-7 packet runner:** [`scripts/frontier_beta6_d7_maxorder7_packet_2026_06_05.py`](../scripts/frontier_beta6_d7_maxorder7_packet_2026_06_05.py)
**Maxorder-7 packet cache:** [`logs/runner-cache/frontier_beta6_d7_maxorder7_packet_2026_06_05.txt`](../logs/runner-cache/frontier_beta6_d7_maxorder7_packet_2026_06_05.txt)
**Source-packet verifier:** [`scripts/frontier_beta6_d7_source_packet_manifest_2026_06_05.py`](../scripts/frontier_beta6_d7_source_packet_manifest_2026_06_05.py)
**Source-packet verifier cache:** [`logs/runner-cache/frontier_beta6_d7_source_packet_manifest_2026_06_05.txt`](../logs/runner-cache/frontier_beta6_d7_source_packet_manifest_2026_06_05.txt)
**Source-packet verifier JSON:** [`outputs/frontier_beta6_d7_source_packet_manifest_2026_06_05.json`](../outputs/frontier_beta6_d7_source_packet_manifest_2026_06_05.json)
**D7 companion note:** `BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`

## 0. Scope and what this note is for

This note records the next exact coefficient of the SU(3) Wilson single-plaquette
strong-coupling series, and the maxorder-7 source packet now records the
completed coefficient one order after that. Both coefficients are computed by
extending the cited mixed-cumulant connected-cluster enumeration. Writing

```text
Delta(beta) := P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n,
   P_full = <(1/3) Re Tr U_{p0}>_Wilson,
   P_1plaq = the single-plaquette-in-isolation expectation,
```

the cited anchor is `d_5 = 4/18^5 = 1/472392` (the four closed cube shells
through the marked plaquette,
[`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)).
This note delivers the next coefficient exactly,

```text
d_6 = 7 / 5668704     (exact).
```

Equivalently, per cube shell `d_6 = 7/22674816 = 7/(12 * 18^5)`, and the clean
per-shell rational ratio is `d_6 / d_5 = 7/12`. It further gives a **structural
order-beta^7 support reduction**: Section 3c's GF(3) cycle-space certificate
proves no order-beta^6 or order-beta^7 distinct support is color-closable, so
`d_7` only has contributions from the four cube shells' order-7 multiplicity
terms. The completed maxorder-7 packet computes that reduced sum exactly:

```text
d_7 = 5 / 17006112     (exact),     d_7 / d_6 = 5/21.
```

The cache-addressable packet is
[`logs/runner-cache/frontier_beta6_d7_maxorder7_packet_2026_06_05.txt`](../logs/runner-cache/frontier_beta6_d7_maxorder7_packet_2026_06_05.txt).
It delegates to the full untruncated source runner
[`scripts/frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py)
with argv `7` and prints the current primary-runner SHA-256 into the
cache, and the source-packet verifier
[`scripts/frontier_beta6_d7_source_packet_manifest_2026_06_05.py`](../scripts/frontier_beta6_d7_source_packet_manifest_2026_06_05.py)
checks the source markers, cache freshness, and linked evidence. The companion
bounded note
`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`
records the order-7 coefficient and the bounded tadpole/geometric ansatz
falsification.

This is a **bounded** result: an exact strong-coupling series coefficient. It
does **not** close beta=6, does not assert `P(6)`, does not posit a closed
boosting form, and reuses no target-fit exponent. The double obstruction
(the boundary character measure `rho_{p,q}(6)` is under-determined by local
character + intertwiner data AND its exact L_s>=3 evaluation is treewidth-29
infeasible) is recorded in the non-load-bearing frontier map
`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`.
The Monte-Carlo comparator `<P>(beta=6) ~= 0.594`
(`plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05`) is **not** a
derivation input here.

## 1. Setup: connected-cumulant linked-cluster expansion

With the marked observable `O = X_{p0}`, `X_p = (Tr U_p + Tr U_p^dag)/6`, the
Wilson expectation expands at `beta = 0` (free Haar measure, each link
independent) as

```text
<X_{p0}>_beta = sum_{n>=0} (beta^n / n!) sum_{q_1..q_n}
                   kappa(X_{p0}; X_{q_1}, ..., X_{q_n}),
```

where `kappa` is the exact connected free-Haar cumulant. This is the BBGKY /
uniform-source identity `d/dbeta = sum_r d/dJ_r` of the cited
[`GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md)
applied at `beta = 0`.
`P_1plaq(beta)` collects the all-`q_i = p0` terms; `Delta(beta)` is the
remainder, so

```text
d_n = (1/n!) sum'_{q_1..q_n} kappa(X_{p0}; X_{q_1}, ..., X_{q_n})   (not all q_i = p0).
```

Organize by the distinct action support `S` (set of distinct plaquettes != p0)
and a multiplicity vector `(m_{p0} >= 0, {m_s >= 1}_{s in S})` with total `n`:

```text
contribution(S, n) = sum_{mult vectors} (1 / (m_{p0}! prod_s m_s!))
                     * kappa(X_{p0}; [m_{p0} copies of X_{p0}] + [m_s copies of X_s]).
```

Each joint cumulant is the exact set-partition (Moebius) sum of free-Haar
moments; each moment factorizes over links and is evaluated by an exact SU(3)
single-link Haar integral (Section 2).

## 2. Exact SU(3) single-link Haar integral (the 3nj / Clebsch content)

The free-Haar moment of a plaquette multiset factorizes over links: for each
link the integrand is a product of fundamental matrices `U` (from forward loop
traversals) and `conj(U)` (from backward traversals). The exact single-link
integral

```text
int_{SU(3)} dU  prod_{a=1..p} U_{i_a j_a}  prod_{b=1..q} conj(U)_{k_b l_b}
```

is the orthogonal projector onto SU(3)-invariants of `V^{(x)p} (x) (V*)^{(x)q}`,
expressed in the computational basis. We build it **exactly** from a spanning
set of invariant tensors — delta-caps (pairing a fundamental slot with an
antifundamental slot) and epsilon-triples (the SU(3) det / baryon sector,
contracting three fundamental or three antifundamental slots) — reduced to a
linearly-**independent** basis (the raw delta/epsilon spanning set is
over-complete at higher degree by SU(3) epsilon-delta identities, so the naive
Gram is singular; we take the Gram-RREF pivot subset and invert). The link
integral is then `T[rows, cols] = sum_{a,b} e_a[rows] (G^{-1})_{ab} e_b[cols]`.
This is the genuine 3nj / Clebsch contraction content of each cluster; it is
exact rational.

The integrator is validated (runner V0) against the closed forms
`int U Ubar = (1/3) delta_ik delta_jl`, `int U U U = (1/6) eps_ijk eps_lmn`,
the degree-(2,2) U(3) Weingarten result, and the SU(3) singlet-multiplicity
table `N0(p,q)` (e.g. `N0(1,1)=1, N0(2,2)=2, N0(3,0)=1, N0(3,3)=6, N0(4,1)=3`),
and (runner V6) against high-precision Haar Monte-Carlo on O(1) quantities
(`<|TrU|^2>=1`, `<(TrU)^3>=1`, `<|TrU|^4>=2`).

## 3. Cluster topologies contributing at order beta^6

### 3a. The contributing distinct support is unchanged from order 5

For a nonzero connected cumulant, every one of `p0`'s four links must be
SU(3)-color-balanced, hence covered by at least one distinct action face; a
distinct face shares exactly one edge of `p0` (cited
[`GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_THEOREM_NOTE.md)
Thm 1 / its narrow-core note). The minimal
connected leaf-free distinct support is the **six-face elementary cube boundary**
(`p0` + five action faces), and there are exactly four such cube shells through
`p0` (offsets +-1 in the two transverse directions 2 and 3).

### 3b. New finite-geometry fact at order beta^6: no new distinct support

Exhaustive GF(3) link-balance enumeration over the radius-1 candidate patch
(runner V3) classifies all connected leaf-free distinct action supports by total
size:

```text
size 4: 28 leaf-free, 0 GF(3)-closable
size 5: 452 leaf-free, 4 GF(3)-closable  (the four cube shells)
size 6: 5966 leaf-free, 0 GF(3)-closable
```

So **zero order-beta^6 distinct connected supports are SU(3)-color-closable**:
no new closed surface appears between the cube boundary (5 action faces) and the
next closable structure. Therefore `d_6` receives contributions **only from the
four cube shells via order-6 multiplicity**:

- one shell face inserted twice (`m_s = 2`, weight `1/2!`), summed over the five
  faces; and
- the marked plaquette inserted once more among the sources (`m_{p0} = 1`).

Both are genuine connected-cumulant contributions absent at order 5 (where
`sum m = 5` forces every multiplicity to 1). They are computed exactly by the
set-partition Moebius cumulant — the `m_{p0}=1` term, for instance, is a
connected cumulant with `X_{p0}` appearing twice, evaluated mechanically as a
sum of products of exact link-factorized moments, not by any closed-form
shortcut.

### 3c. Order beta^7: a GF(3) cycle-space certificate settles the structure

A GF(3)-closable distinct support is a **2-cycle** of the face->edge boundary
map (its faces sum to zero edge-charge mod 3 for some orientation). On the
distance-2 patch around `p0` (141 faces, 200 edges) the GF(3) cycle space has
dimension 28, and the 28 elementary 3-cube boundaries **span** it (rank 28). So
every 2-cycle is a GF(3)-combination of cube boundaries; the only 2-cycles
through `p0` of weight `<= 8` are the four single-cube boundaries (weight 6) --
there is **no weight-7 or weight-8 2-cycle through `p0`** (the next weights are
10, 11, 12). Hence **no distinct action support of size 6 or 7 is closable**
(size 6 also confirmed directly by the radius-1 enumeration, runner V3). This
GF(3) cycle-space certificate is the tractable replacement for the size-7
connected-subset enumeration, which collides with the `mu^n` cluster-growth
wall (frontier `> 1e7`, OOM). Therefore the exact `d_7` computation, like
`d_6`, receives contributions **only from the four cube shells via order-7
multiplicity** (one face tripled, two faces doubled, one face doubled with
`m_{p0}=1`, etc.). The completed maxorder-7 packet linked in the header
executes this restricted computation.

## 4. Result

Each cube shell contributes `7/22674816 = 7/(12 * 18^5)` to `d_6`; with four
shells, `d_6 = 4 * 7/22674816 = 7/5668704`. The completed order-7 multiplicity
sum gives per-shell `5/68024448`, hence `d_7 = 5/17006112`. So, with the cited
anchor `d_5 = 1/472392`:

```text
Delta(beta) = (1/472392) beta^5 + (7/5668704) beta^6
              + (5/17006112) beta^7 + O(beta^8)
d_5 = 1/472392   = 2.11688598e-06
d_6 = 7/5668704  = 1.23485015e-06     d_6/d_5 = 7/12
d_7 = 5/17006112 = 2.94011941e-07     d_7/d_6 = 5/21
```

The exact connected coefficients are clean rationals, as expected for a finite
connected cluster sum whose SU(3) link integrals are rational (the framework's
algebraic closure is QbarQ(pi); no transcendental enters a finite
strong-coupling coefficient).

**Order beta^7.** Section 3c reduces the `d_7` distinct-support search to the
**four cube shells' order-7 multiplicity sum** (the GF(3) cycle-space
certificate proves no size-6/7 distinct support is closable), and the
maxorder-7 packet computes that sum exactly. The single-ratio geometric
prediction tested by the later harness is
`d_7^pred = (d_6/d_5) d_6 = (7/12) d_6 = 49/68024448 ~= 7.20e-07`; the exact
value `d_7 = 5/17006112` has ratio `d_7/d_6 = 5/21`, so the single-ratio
geometric continuation is falsified at order 7 (Section 5).

## 5. How this feeds the resummation test harness (#2255)

The non-load-bearing consumer harness
`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md` (runner
`scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`) exposes a
one-line drop-in `EXACT_HIGHER = {6: ..., 7: ...}`. The completed exact packet
now supplies both entries:

```text
EXACT_HIGHER = {6: Fraction(7,5668704), 7: Fraction(5,17006112)}
```

The tadpole / boosted-PT geometric prediction formed from `{d_5, d_6}` is

```text
d_7^pred = (d_6 / d_5) * d_6 = (7/12) * d_6 = 49/68024448 ~= 7.20e-07.
```

The exact value is `d_7 = 5/17006112`, with `d_7/d_6 = 5/21`, so the
tadpole/geometric SUPPORT-or-FALSIFY line is a bounded **FALSIFY** for the
specific single-ratio continuation pattern. This is not a beta=6 plaquette
derivation; it only rejects that local coefficient-continuation ansatz. The
d-log-Pade predictive test instead needs `{d_5..d_8}` (= beta^8, at/past the
treewidth wall), so only its forward `<P>(6)` sensitivity test is in-runway.

This note therefore supplies exact `{d_6, d_7}` coefficient evidence and the
source-packet links needed to inspect the completed maxorder-7 computation. The
beta=6 closure problem remains open.

## 6. Computational reach and the named wall

The connected-coefficient frontier is bounded by two compounding costs (the same
barrier the frontier map names): the number of leafless connected clusters grows
like the lattice-animal constant `mu^n` (`mu ~ 8`; calibrated by the order-5
audit's 37,176-candidate classification and the 5966 leaf-free size-6 supports
here), and each cluster's exact SU(3) Haar weight is a per-link
`3^(2k)` invariant-projector contraction in the number `k` of fundamental
factors on a link, which rises with multiplicity (doubled / tripled faces). At
order beta^7 the cube-shell multiplicity clusters reach links with up to four
factors (`3^8` per-link contraction); beta^7-beta^8 is the practical ceiling.
Any depth approaching the ~15-40 exact coefficients a genuine resummation would
need collides with the cited treewidth-29 infeasibility
(`su3_wigner_l3_treewidth_infeasible_2026-05-04`). This note advances the
frontier by one order and sharpens the obstruction; it does not, and cannot by
itself, close beta=6.

## 7. What this note claims / does not claim

Claims:
- the exact value `d_6 = 7/5668704` of the order-beta^6 connected coefficient of
  `Delta(beta)`, on the accepted Wilson `3 spatial + 1 derived-time` surface;
- the exact value `d_7 = 5/17006112` of the order-beta^7 connected coefficient
  of `Delta(beta)`, computed from the four cube shells' order-7 multiplicity
  sum by the completed maxorder-7 packet;
- the rigorous reduction of the `d_7` distinct-support search to the four cube
  shells' order-7 multiplicity sum, via the GF(3) cycle-space certificate (no
  size-6/7 distinct support is closable);
- the exact finite-geometry facts that zero order-beta^6 distinct connected
  supports are GF(3)-closable (and, via the cycle-space certificate, none at
  size 7), so `d_6` and `d_7` are the four cube shells' multiplicity
  contributions;
- reproduction of the cited anchor `d_5 = 1/472392` by the same engine.

Does NOT claim:
- any value of `P(beta=6)`, `beta_eff(6)`, `u_0`, or `alpha_s`;
- any closed boosting / reduction-law form;
- closure or repinning of the canonical same-surface plaquette value;
- any audit status (independent audit lane only);
- any new axiom, tag, vocabulary, or meta-framing.

## 8. Validation (runner scorecard)

`python3 scripts/frontier_beta6_connected_coefficient_2026_05_30.py [maxorder]`
(default `maxorder=6`; pass `7` to also compute `d_7` -- the order-7
multiplicity cumulants are at the per-link `3^(2k)` contraction edge and take
substantially longer than order 6). The default `maxorder=6` run also
verifies the maxorder-7 cache header, wrapper SHA, primary-runner SHA, and
`d_7` scorecard snippets so the registered primary runner exposes the
completed order-7 evidence without rerunning the multi-minute path. The
cache-addressable audit packet
[`scripts/frontier_beta6_d7_maxorder7_packet_2026_06_05.py`](../scripts/frontier_beta6_d7_maxorder7_packet_2026_06_05.py)
delegates to the full source runner with argv `7`; its paired cache is
[`logs/runner-cache/frontier_beta6_d7_maxorder7_packet_2026_06_05.txt`](../logs/runner-cache/frontier_beta6_d7_maxorder7_packet_2026_06_05.txt).

- V0 single-link integrator: closed forms (`UUbar`, `UUU`, the `(2,2)` U(3)
  Weingarten check is embedded in the dimension table) + singlet-dimension
  table `N0(p,q)`.
- V1 free-Haar moments: `<X_p0>=0`, `<X_p0^2>=1/18`, `<X_p0^3>=1/108`.
- V2 per-shell connected cumulant `= 2*(1/6)^6*3^(V-E) = 1/18^5` (note Thm 4);
  `d_5 = 1/472392` reproduced.
- V3 zero GF(3)-closable order-beta^6 distinct supports.
- V4 `d_6 = 7/5668704`; per-shell ratio `d_6/d_5 = 7/12`.
- V5 (maxorder>=7) GF(3) cycle-space certificate (cube boundaries span the
  cycle space; no weight-7/8 2-cycle through `p0`) plus the exact
  `d_7 = 5/17006112` computation from the four cube shells (order-7
  multiplicity; heavy).
- V6 Haar Monte-Carlo validation of the integrator on O(1) quantities
  (`<|TrU|^2>=1`, `<(TrU)^3>=1`, `<|TrU|^4>=2`).

All exact-computation checks PASS. The completed maxorder-7 packet cache reports
`SCORECARD: PASS=22 FAIL=0`, and the source-packet verifier cache reports
`SUMMARY: BETA6 D7 SOURCE PACKET PASS=53 FAIL=0`.

## 9. Key files / cross-references

- [`scripts/frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py)
- [`scripts/frontier_beta6_d7_maxorder7_packet_2026_06_05.py`](../scripts/frontier_beta6_d7_maxorder7_packet_2026_06_05.py)
- [`logs/runner-cache/frontier_beta6_d7_maxorder7_packet_2026_06_05.txt`](../logs/runner-cache/frontier_beta6_d7_maxorder7_packet_2026_06_05.txt)
- [`scripts/frontier_beta6_d7_source_packet_manifest_2026_06_05.py`](../scripts/frontier_beta6_d7_source_packet_manifest_2026_06_05.py)
- [`logs/runner-cache/frontier_beta6_d7_source_packet_manifest_2026_06_05.txt`](../logs/runner-cache/frontier_beta6_d7_source_packet_manifest_2026_06_05.txt)
- [`outputs/frontier_beta6_d7_source_packet_manifest_2026_06_05.json`](../outputs/frontier_beta6_d7_source_packet_manifest_2026_06_05.json)
- `BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md) (cited d_5 anchor)
- [`GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md) (BBGKY identity)
- [`GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_THEOREM_NOTE.md) (cube-shell geometry)
- `BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md` (non-load-bearing consumer harness #2255)
- `BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md` (non-load-bearing frontier map / double-wall)

## 10. Methodology comparator (cross-check, NOT a derivation input)

The fundamental-representation SU(3) Wilson plaquette strong-coupling series is a
standard object (Balian-Drouffe-Itzykson character / connected-graph expansion;
Munster's strong-coupling computations). The structure used here — connected
(linked-cluster) graphs, leaf factorization, the closed-surface link-integral
collapse to `3^(V-E)` — mirrors that standard organization. The comparator is
cited for **methodology** only; no external series coefficient or numerical
value is consumed as a derivation input. The exact coefficients here are
computed from primitives (exact SU(3) Haar integrals on the framework's accepted
Wilson surface), and the only external anchor reproduced is the in-repo cited
`d_5 = 1/472392`.
