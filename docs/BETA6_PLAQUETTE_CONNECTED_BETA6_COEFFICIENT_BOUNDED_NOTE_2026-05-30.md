# Beta=6 SU(3) Wilson Single-Plaquette — Exact Order-beta^6 and Order-beta^7 Connected Coefficients

**Date:** 2026-05-30
**Type:** bounded_theorem (two exact strong-coupling series coefficients; does
NOT close beta=6)
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome for any cited claim_id; all statuses quoted
below are read-offs from `docs/audit/data/audit_ledger.json`
(`rows[<claim_id>]['effective_status']`) on the dates stated.
**Primary runner:** [`scripts/frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py)

## 0. Scope and what this note is for

This note records the next exact coefficient of the SU(3) Wilson single-plaquette
strong-coupling series, computed by extending the retained mixed-cumulant
connected-cluster enumeration one order, and a rigorous reduction of the order
after that. Writing

```text
Delta(beta) := P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n,
   P_full = <(1/3) Re Tr U_{p0}>_Wilson,
   P_1plaq = the single-plaquette-in-isolation expectation,
```

the retained anchor is `d_5 = 4/18^5 = 1/472392` (the four closed cube shells
through the marked plaquette, `gauge_vacuum_plaquette_mixed_cumulant_audit_note`,
recorded as `retained` in the 2026-05-29 frontier-map read-off). This note
delivers the next coefficient exactly,

```text
d_6 = 7 / 5668704     (exact).
```

Equivalently, per cube shell `d_6 = 7/22674816 = 7/(12 * 18^5)`, and the clean
per-shell rational ratio is `d_6 / d_5 = 7/12`. It further **reduces `d_7`
rigorously** to the four cube shells' order-7 multiplicity sum (Section 3c: a
GF(3) cycle-space certificate proves no order-beta^6 or order-beta^7 distinct
support is color-closable); the runner computes that exact `d_7` rational, at
the per-link contraction ceiling that marks `beta^7` as the practical frontier
(Section 6).

This is a **bounded** result: an exact strong-coupling series coefficient. It
does **not** close beta=6, does not assert `P(6)`, does not posit a closed
boosting form, and reuses no target-fit exponent. The doubly-walled lane-killer
(the boundary character measure `rho_{p,q}(6)` is under-determined by local
character + intertwiner data AND its exact L_s>=3 evaluation is treewidth-29
infeasible) is recorded in
[`BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md).
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
uniform-source identity `d/dbeta = sum_r d/dJ_r` of the retained
`gauge_vacuum_plaquette_connected_hierarchy_theorem_note` applied at `beta = 0`.
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
distinct face shares exactly one edge of `p0` (retained
`gauge_vacuum_plaquette_distinct_shell_theorem` Thm 1 / its narrow-core note
`...DISTINCT_SHELL_EXACT_CORE_NARROW_THEOREM_NOTE_2026-05-29`). The minimal
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
wall (frontier `> 1e7`, OOM). Therefore `d_7`, like `d_6`, receives
contributions **only from the four cube shells via order-7 multiplicity** (one
face tripled, two faces doubled, one face doubled with `m_{p0}=1`, etc.).

## 4. Result

Each cube shell contributes `7/22674816 = 7/(12 * 18^5)` to `d_6`; with four
shells, `d_6 = 4 * 7/22674816 = 7/5668704`. So, with the retained anchor
`d_5 = 1/472392`:

```text
Delta(beta) = (1/472392) beta^5 + (7/5668704) beta^6 + d_7 beta^7 + O(beta^8)
d_5 = 1/472392   = 2.11688598e-06
d_6 = 7/5668704  = 1.23485015e-06     d_6/d_5 = 7/12
```

The exact connected coefficients are clean rationals, as expected for a finite
connected cluster sum whose SU(3) link integrals are rational (the framework's
algebraic closure is QbarQ(pi); no transcendental enters a finite
strong-coupling coefficient).

**Order beta^7.** Section 3c reduces `d_7` rigorously to the **four cube shells'
order-7 multiplicity sum** (the GF(3) cycle-space certificate proves no size-6/7
distinct support is closable). That sum is the exact `d_7`. The runner computes
it (`maxorder=7`); the order-7 multiplicity cumulants reach single links with up
to four fundamental factors, whose exact `3^(2k)` invariant-projector
contraction makes the order-7 evaluation **substantially heavier than order 6**
-- this is the concrete onset of the named computational wall (Section 6):
`beta^7` is the practical ceiling. The exact `d_7` rational is the runner's
order-7 output; the geometric prediction it tests against is
`d_7^pred = (d_6/d_5) d_6 = (7/12) d_6 = 49/68024448 ~= 7.20e-07` (Section 5).

## 5. How this feeds the resummation test harness (#2255)

The landed harness
[`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md)
(runner `scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`) exposes
a one-line drop-in `EXACT_HIGHER = {6: ..., 7: ...}`. Supplying the exact `d_6`
**activates** the cheapest decisive falsifier — the tadpole / boosted-PT
geometric predictive test, which needs two contiguous coefficients `{d_5, d_6}`
and predicts

```text
d_7^pred = (d_6 / d_5) * d_6 = (7/12) * d_6 = 49/68024448 ~= 7.20e-07.
```

The moment an exact `d_7` is supplied, the harness reports `SUPPORT` (within its
5% window) or `FALSIFY`. This cycle reduces `d_7` to the four cube shells'
order-7 multiplicity sum (Section 3c) and the runner computes that exact
rational (`maxorder=7`); dropping
`EXACT_HIGHER = {6: Fraction(7,5668704), 7: <runner d_7>}` into the harness then
reads off the tadpole/geometric SUPPORT-or-FALSIFY verdict against
`d_7^pred = (7/12) d_6` (the harness run is the next cycle). The d-log-Pade
predictive test instead needs `{d_5..d_8}` (= beta^8, at/past the treewidth
wall), so only its forward `<P>(6)` sensitivity test is in-runway.

This note therefore **activates** the tadpole verdict (it supplies the exact
`d_6` that the predictive test needs, plus the structure for `d_7`); the harness
run that reads off SUPPORT/FALSIFY is the next cycle.

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
need collides with the retained treewidth-29 infeasibility
(`su3_wigner_l3_treewidth_infeasible_2026-05-04`, audited_conditional on
2026-05-29). This note advances the frontier by one order and sharpens the
obstruction; it does not, and cannot by itself, close beta=6.

## 7. What this note claims / does not claim

Claims:
- the exact value `d_6 = 7/5668704` of the order-beta^6 connected coefficient of
  `Delta(beta)`, on the accepted Wilson `3 spatial + 1 derived-time` surface;
- the rigorous reduction of `d_7` to the four cube shells' order-7 multiplicity
  sum, via the GF(3) cycle-space certificate (no size-6/7 distinct support is
  closable); the runner computes that exact rational (`maxorder=7`);
- the exact finite-geometry facts that zero order-beta^6 distinct connected
  supports are GF(3)-closable (and, via the cycle-space certificate, none at
  size 7), so `d_6` and `d_7` are the four cube shells' multiplicity
  contributions;
- reproduction of the retained anchor `d_5 = 1/472392` by the same engine.

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
substantially longer than order 6).

- V0 single-link integrator: closed forms (`UUbar`, `UUU`, the `(2,2)` U(3)
  Weingarten check is embedded in the dimension table) + singlet-dimension
  table `N0(p,q)`.
- V1 free-Haar moments: `<X_p0>=0`, `<X_p0^2>=1/18`, `<X_p0^3>=1/108`.
- V2 per-shell connected cumulant `= 2*(1/6)^6*3^(V-E) = 1/18^5` (note Thm 4);
  `d_5 = 1/472392` reproduced.
- V3 zero GF(3)-closable order-beta^6 distinct supports.
- V4 `d_6 = 7/5668704`; per-shell ratio `d_6/d_5 = 7/12`.
- V5 (maxorder>=7) GF(3) cycle-space certificate (cube boundaries span the
  cycle space; no weight-7/8 2-cycle through `p0`) + exact `d_7` from the four
  cube shells (order-7 multiplicity; heavy).
- V6 Haar Monte-Carlo validation of the integrator on O(1) quantities
  (`<|TrU|^2>=1`, `<(TrU)^3>=1`, `<|TrU|^4>=2`).

All exact-computation checks PASS.

## 9. Key files / cross-references

- [`scripts/frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py)
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md) (retained d_5 anchor)
- [`GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md) (BBGKY identity)
- [`GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_THEOREM_NOTE.md) (cube-shell geometry)
- [`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md) (consumer harness #2255)
- [`BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md) (frontier map / double-wall)

## 10. Methodology comparator (cross-check, NOT a derivation input)

The fundamental-representation SU(3) Wilson plaquette strong-coupling series is a
standard object (Balian-Drouffe-Itzykson character / connected-graph expansion;
Munster's strong-coupling computations). The structure used here — connected
(linked-cluster) graphs, leaf factorization, the closed-surface link-integral
collapse to `3^(V-E)` — mirrors that standard organization. The comparator is
cited for **methodology** only; no external series coefficient or numerical
value is consumed as a derivation input. The exact coefficients here are
computed from primitives (exact SU(3) Haar integrals on the framework's accepted
Wilson surface), and the only external anchor reproduced is the in-repo retained
`d_5 = 1/472392`.
