# Beta=6 SU(3) Wilson Single-Plaquette — Exact Order-beta^7 Connected Coefficient and Tadpole/Geometric Verdict

**Date:** 2026-05-30
**Type:** bounded_theorem (one exact strong-coupling series coefficient + one
analytic-continuation falsification verdict; does NOT close beta=6)
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome for any cited claim_id; all statuses quoted
below are read-offs from `docs/audit/data/audit_ledger.json`
(`rows[<claim_id>]['effective_status']`) on the dates stated.
**Primary runner:** [`scripts/frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py)
**Verdict harness:** [`scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`](../scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py)

## 0. Scope and what this note is for

This note records the exact order-`beta^7` connected coefficient of the SU(3)
Wilson single-plaquette strong-coupling series, computed by an optimized
extension of the retained mixed-cumulant connected-cluster enumeration, and the
resulting tadpole / geometric analytic-continuation verdict from the landed
resummation test harness. Writing

```text
Delta(beta) := P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n,
   P_full = <(1/3) Re Tr U_{p0}>_Wilson,
   P_1plaq = the single-plaquette-in-isolation expectation,
```

the retained anchor is `d_5 = 4/18^5 = 1/472392`
(`gauge_vacuum_plaquette_mixed_cumulant_audit_note`, recorded as `retained` in
the 2026-05-29 frontier-map read-off), and the order-`beta^6` coefficient
`d_6 = 7/5668704` is the prior cycle's exact result
([`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md)).
This note delivers the next coefficient exactly,

```text
d_7 = 5/17006112     (exact).
```

Equivalently, per cube shell `d_7 = 5/68024448` (four identical shells), and the
per-order ratio is `d_7 / d_6 = 5/21`. With `d_6 / d_5 = 7/12`, the per-order
ratio is **not constant**, which **falsifies** the tadpole / geometric
single-pole continuation (Section 5).

This is a **bounded** result: an exact strong-coupling series coefficient plus a
clean falsification verdict. It does **not** close beta=6, does not assert
`P(6)`, does not posit a closed boosting form, and reuses no target-fit exponent.
The doubly-walled lane-killer (the boundary character measure `rho_{p,q}(6)` is
under-determined by local character + intertwiner data AND its exact `L_s>=3`
evaluation is treewidth-29 infeasible) is recorded in
[`BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md).
The Monte-Carlo comparator `<P>(beta=6) ~= 0.594`
(`plaquette_4d_mc_fss_numerical_theorem_note_2026-05-05`) is **not** a derivation
input here.

## 1. The order-beta^7 contribution: structure (settled in the prior cycle)

A GF(3)-closable distinct support is a 2-cycle of the face->edge boundary map.
The prior cycle's GF(3) cycle-space certificate establishes that on the
distance-2 patch around `p0` the 28 elementary 3-cube boundaries **span** the
cycle space, and the only 2-cycles through `p0` of weight `<= 8` are the four
single-cube boundaries (weight 6) — there is no weight-7 or weight-8 2-cycle
through `p0` (the next weights are 10, 11, 12). Hence **no distinct action
support of size 6 or 7 is color-closable**, and `d_7`, like `d_6`, receives
contributions **only from the four cube shells via order-7 multiplicity** (one
face tripled; two faces doubled; one face doubled with `m_{p0}=1`; the marked
plaquette inserted twice; etc.). The runner re-checks this certificate
(`maxorder=7`, V5) before computing the multiplicity sum.

Concretely, for each cube shell the order-7 contribution is the
multiplicity-vector sum

```text
contribution(shell, 7) = sum_{mult vectors, total = 7}
        (1 / (m_{p0}! prod_s m_s!)) * kappa(X_{p0}; ...),
```

over the 21 multiplicity vectors of total 7 across the marked plaquette plus the
five shell faces (each `>= 1`). Every such cumulant is an **8-plaquette** joint
connected cumulant, evaluated by the exact set-partition (Moebius) sum of
free-Haar moments, each moment factorized over links and integrated by the exact
SU(3) single-link Haar integral.

## 2. Beating the order-beta^7 contraction wall (the optimized engine)

The prior cycle reduced `d_7` to the four cube shells' order-7 multiplicity sum
but hit a per-link `3^(2k)` invariant-projector contraction wall (`> 30 min`):
the 8-plaquette moments reach single links carrying up to four fundamental + four
conjugate factors, and with the sympy engine a single such moment (summed over
its `2^8` orientations) takes `~270 s`. This cycle removes the wall with **no
change to the maths** by re-engineering only the contraction:

1. **Sparse link-integral tensor.** The exact single-link integral
   `int dU prod U^{(x)p} (x) conj(U)^{(x)q}` is built **sparsely** from the
   invariant-basis supports — outer products
   `e_a (x) (G^{-1})_{ab} (x) e_b` over only the nonzero basis index-tuples —
   instead of scanning the `3^(2(p+q))` dense index grid. For a `(4,4)` link the
   dense grid is `3^16 ~ 4.3e7` slots, while the integral tensor has `<= 639^2 ~
   4e5` nonzeros built from a 639-element support. The invariant basis and exact
   Gram inverse are **reused** from the validated `projector(p, q)`; only the
   contraction is new.
2. **Pure-int Fraction arithmetic + variable elimination.** The per-link tensors
   are contracted over the shared plaquette-corner indices by a min-degree
   variable-elimination order with `fractions.Fraction` values (no sympy object
   churn in the hot loop), keeping every intermediate sparse.
3. **Early zero on unbalanced links.** Any orientation that leaves a link with no
   SU(3) singlet (empty projector basis) zeroes the whole word immediately,
   pruning most of the `2^n` orientation terms.

Result: the worst 8-plaquette moment drops from `~270 s` to `~0.5 s`, and the
exact `d_7` is a `~2 min` computation. This is the engine optimization the prior
cycle's handoff anticipated; it advances the connected-coefficient frontier by
one order without any new physics.

## 3. Two-engine confirmation

The optimized Fraction engine is validated against the prior cycle's sympy
engine (runner V4b, V5, V6):

- it reproduces the sympy `d_5 = 1/472392` and `d_6 = 7/5668704` **exactly**
  (this validates the optimized SU(3) link-integral formulas against the
  independently-computed order-5 and order-6 values);
- it agrees with the sympy moment on a spread of plaquette multisets up to size
  8, including the worst-case 8-plaquette moment (both engines return
  `1/11337408`);
- both integrators reproduce the `O(1)` Haar values (`<X_{p0}^2> = 1/18`,
  `<X_{p0}^3> = 1/108`), and the single-link integrator passes the
  high-precision Haar Monte-Carlo cross-check (`<|TrU|^2> = 1`,
  `<(TrU)^3> = 1`, `<|TrU|^4> = 2`).

The `d_7` assembly uses the identical set-partition and multiplicity-vector
enumeration as the validated `d_5`/`d_6` assembly. The two engines **agree**;
`d_7 = 5/17006112` is the exact value.

## 4. Result

With the retained anchor and the prior-cycle coefficient:

```text
Delta(beta) = (1/472392) beta^5 + (7/5668704) beta^6 + (5/17006112) beta^7 + O(beta^8)
d_5 = 1/472392    = 2.11688598e-06
d_6 = 7/5668704   = 1.23485015e-06    d_6/d_5 = 7/12
d_7 = 5/17006112  = 2.94011941e-07    d_7/d_6 = 5/21
```

Per cube shell `d_7 = 5/68024448` (four identical shells, runner V5). The exact
connected coefficients are clean rationals, as expected for a finite connected
cluster sum whose SU(3) link integrals are rational (the framework's algebraic
closure is `QbarQ(pi)`; no transcendental enters a finite strong-coupling
coefficient). The per-order ratios `d_6/d_5 = 7/12` and `d_7/d_6 = 5/21` are
**different**: the connected series does not have a constant per-order ratio
through this order.

## 5. The tadpole / geometric verdict: FALSIFIED

The landed resummation harness
([`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md))
exposes the tadpole / boosted-PT geometric predictive test. A boosted-coupling
continuation with a single nearest real boosting singularity `beta*` maps the
connected series onto a leading geometric tail, so it predicts a **constant**
per-order ratio: from `{d_5, d_6}` it predicts

```text
d_7^pred = (d_6 / d_5) * d_6 = (7/12) * d_6 = 49/68024448 ~= 7.20e-07.
```

The exact `d_7 = 5/17006112 ~= 2.94e-07` was computed **independently** (Sections
1-4: the shell multiplicity sum + exact SU(3) integrals), and only **then**
compared. It misses the geometric prediction by far more than the harness' 5%
support window:

```text
d_7^pred = 49/68024448 ~= 7.203e-07
d_7^exact = 5/17006112  ~= 2.940e-07
relative miss = |pred - exact| / exact = 1.45   (window 0.05)
```

Dropping `EXACT_HIGHER = {6: Fraction(7,5668704), 7: Fraction(5,17006112)}` into
the harness reads off

```text
[FALSIFY] tadpole/geometric: d_7 predicted = 7.2032926e-7, exact = 2.9401194e-7,
          rel = 1.45 (window 0.05)
```

**Verdict: the tadpole / geometric single-pole ansatz is FALSIFIED at order 7.**
A single nearest boosting pole does **not** organize the connected series — the
per-order ratio drops from `7/12` to `5/21` rather than staying constant. This
forecloses the one cheap predictive route the harness could test in-runway: the
resummation route does **not** reduce to a geometric tail, so a closed boosting
form is not supported by the exact data. (This is the predictive-test outcome
the harness was built to deliver; either outcome is a result, and this is the
honest one — nothing here is fitted to the comparator.)

### 5a. Forward `<P>(6)` under the exact truncation (NOT a closure)

For completeness the harness also reports the **forward** truncation. With the
exact `{d_5, d_6, d_7}` the truncated `Delta(6) = sum_{n=5}^{7} d_n 6^n` gives

```text
<P>(6)_trunc = P_1plaq(6) + Delta(6)_trunc ~= 0.5789   (comparator 0.594, gap ~0.0151).
```

This is a **truncated partial sum** toward the Monte-Carlo comparator, **not** a
closure: the three-term truncation lands `~0.015` below `0.594`, but with the
geometric continuation falsified there is **no proven analytic continuation of
`Delta` to `beta=6` in-runway**, and the next coefficient `d_8` is at/past the
treewidth wall (Section 6). A truncated series approaching a comparator is not a
derivation of it; reading `0.5789 -> 0.594` as a near-closure would be exactly
the comparator-fitting the no-go ledger forbids. The d-log-Pade **predictive**
test needs `{d_5..d_8}` (= `beta^8`), so only its forward sensitivity test is
in-runway, and the forward truncation above is reported as a sensitivity datum,
not a result about `P(6)`.

## 6. Computational reach and the named wall

The optimized engine moves the connected-coefficient frontier to `beta^7` exactly
and keeps `beta^7` `~2 min`, but the two compounding costs the frontier map names
remain. The number of leafless connected clusters grows like the lattice-animal
constant `mu^n` (`mu ~ 8`), and `d_8` adds 56 multiplicity vectors per shell of
9-plaquette cumulants (Bell(9) = 21147 set partitions each) reaching links with
even higher factor counts; together with the distinct-support side reopening at
larger area, `beta^8` is at/past the practical ceiling, and any depth approaching
the ~15-40 exact coefficients a genuine resummation would need collides with the
retained treewidth-29 infeasibility
(`su3_wigner_l3_treewidth_infeasible_2026-05-04`, `audited_conditional` on
2026-05-29). With the geometric continuation now falsified and the d-log-Pade
predictive test out of runway, the exact-coefficient route has delivered its
decisive in-runway verdict; closing `<P>(6)` requires a genuinely new dynamical
input for `rho_{p,q}(6)` (Section 7), not another brute coefficient.

## 7. What this note claims / does not claim

Claims:
- the exact value `d_7 = 5/17006112` of the order-`beta^7` connected coefficient
  of `Delta(beta)`, on the accepted Wilson `3 spatial + 1 derived-time` surface,
  computed by an optimized contraction with two-engine (sympy + Fraction)
  agreement and reproduction of the retained `d_5` and prior-cycle `d_6`;
- the per-order ratios `d_6/d_5 = 7/12` and `d_7/d_6 = 5/21` (not constant);
- the tadpole / geometric single-pole continuation is **falsified** at order 7
  (exact `d_7` misses the geometric prediction `(7/12) d_6` by `~59%` measured
  against the prediction, `1.45` relative to the exact value — far outside the
  harness' 5% support window).

Does NOT claim:
- any value of `P(beta=6)`, `beta_eff(6)`, `u_0`, or `alpha_s` (the forward
  `<P>(6) ~ 0.5789` is a truncated partial sum toward a comparator, not a
  derivation);
- any closed boosting / reduction-law form (the geometric form is falsified);
- closure or repinning of the canonical same-surface plaquette value;
- any audit status (independent audit lane only);
- any new axiom, tag, vocabulary, or meta-framing.

## 8. Validation (runner + harness scorecards)

Runner `python3 scripts/frontier_beta6_connected_coefficient_2026_05_30.py 7`
(PASS=22 / FAIL=0; `~3.5 min`):
- V0 single-link integrator closed forms (`UUbar`, `UUU`, `(2,2)` Weingarten via
  the dimension table) + singlet-dimension table `N0(p,q)`.
- V1 free-Haar moments (`<X_p0>=0`, `<X_p0^2>=1/18`, `<X_p0^3>=1/108`).
- V2 per-shell connected cumulant `= 2*(1/6)^6*3^(V-E) = 1/18^5`; `d_5 = 1/472392`.
- V3 zero GF(3)-closable order-`beta^6` distinct supports.
- V4 `d_6 = 7/5668704`; per-shell ratio `d_6/d_5 = 7/12`.
- V4b **two-engine agreement**: optimized Fraction engine reproduces sympy `d_5`,
  `d_6` exactly.
- V5 GF(3) cycle-space certificate (cube boundaries span; no weight-7/8 2-cycle
  through `p0`) + **exact `d_7 = 5/17006112`** (four identical shells, optimized
  engine).
- V5b **tadpole/geometric verdict**: `d_7/d_6 = 5/21 != 7/12` => FALSIFIED.
- V6 Haar Monte-Carlo validation of the single-link integrator + Fraction-vs-sympy
  `O(1)` moment agreement.

Harness `python3 scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`
(PASS=20 / FAIL=0) with the drop-in `EXACT_HIGHER = {6: 7/5668704, 7: 5/17006112}`
reads off the live `[FALSIFY] tadpole/geometric` verdict (Section 4a of the
harness) and the forward `<P>(6)_trunc = 0.5789` sensitivity datum.

## 9. Key files / cross-references

- [`scripts/frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py) (optimized engine + exact d_7 + verdict)
- [`scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`](../scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py) (consumer harness)
- [`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md) (prior-cycle exact d_6 + d_7 reduction)
- [`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md) (harness methodology)
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md) (retained d_5 anchor)
- [`GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_CONNECTED_HIERARCHY_THEOREM_NOTE.md) (BBGKY identity)
- [`GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_THEOREM_NOTE.md) (cube-shell geometry)
- [`BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md) (frontier map / double-wall)

## 10. Methodology comparator (cross-check, NOT a derivation input)

The fundamental-representation SU(3) Wilson plaquette strong-coupling series is a
standard object (Balian-Drouffe-Itzykson character / connected-graph expansion;
Munster's strong-coupling computations), and a non-constant per-order ratio in a
connected strong-coupling series is the generic expectation rather than the
constant ratio of a single geometric pole. The comparator is cited for
**methodology** only; no external series coefficient or numerical value is
consumed as a derivation input. The exact coefficients here are computed from
primitives (exact SU(3) Haar integrals on the framework's accepted Wilson
surface), and the only external anchors reproduced are the in-repo retained
`d_5 = 1/472392` and the prior-cycle `d_6 = 7/5668704`.

This note advances the exact-coefficient frontier by one order and delivers the
in-runway analytic-continuation verdict; it does not, and cannot by itself, close
beta=6.
