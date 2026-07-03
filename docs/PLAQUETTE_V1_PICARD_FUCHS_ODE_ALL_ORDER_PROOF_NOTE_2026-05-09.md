# Plaquette V=1 Picard-Fuchs ODE: Finite-Window Boundary Packet

**Date:** 2026-05-09; 2026-06-08 finite-window boundary narrow.
**Claim type:** bounded_theorem
**Status:** bounded-support boundary packet; audit status is set only by the independent audit lane.
**Primary runner:** [`scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py`](../scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py)
(`SUMMARY: FINITE-WINDOW BOUNDARY PASS=5 FAIL=0`)
**Cached runner output:** [`logs/runner-cache/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.txt`](../logs/runner-cache/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.txt)

The claim ID and runner filename contain the historical phrase `all_order`.
They are kept stable for audit and citation tooling. The live mathematical
scope of this packet is the finite-window boundary stated below.

**Companion notes:**

- [`PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md`](PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md) - origin V=1 ODE finite-runner note.
- [`PLAQUETTE_V1_PICARD_FUCHS_ODE_BOUNDED_SYNTHESIS_NOTE_2026-05-06.md`](PLAQUETTE_V1_PICARD_FUCHS_ODE_BOUNDED_SYNTHESIS_NOTE_2026-05-06.md) - bounded-synthesis predecessor.
- [`PLAQUETTE_V1_PICARD_FUCHS_ODE_KOUTSCHAN_MINIMALITY_NOTE_2026-05-06.md`](PLAQUETTE_V1_PICARD_FUCHS_ODE_KOUTSCHAN_MINIMALITY_NOTE_2026-05-06.md) - finite-grid minimality support.
- [`PLAQUETTE_V1_PICARD_FUCHS_ODE_RANK_BOUND_CITATION_NOTE_2026-05-06.md`](PLAQUETTE_V1_PICARD_FUCHS_ODE_RANK_BOUND_CITATION_NOTE_2026-05-06.md) - current finite-window rank-bound boundary note.

## 2026-06-08 Audit-Targeted Narrow

The independent audit blocker for this row is:

> `scope_too_broad: narrow this row to the runner-backed finite-window boundary packet, or provide an auditable all-degree R=3,D=2 bridge theorem before re-auditing the all-order claim.`

This revision takes the first path. It narrows the row to the runner-backed
finite-window boundary packet and preserves the unresolved all-degree
`R=3,D=2` bridge as an open premise.

This packet does **not** claim that the displayed Picard-Fuchs operator is the
minimal all-degree annihilator of the SU(3) single-plaquette integral. It does
not claim an all-order closure of `L . J = 0` from repo-native inputs. It
records exact finite-window checks, a D-finiteness witness, Frobenius-branch
evidence for the candidate operator, and conditional Bostan-Salvy-Schost
threshold arithmetic.

## Setup

```text
J(beta) = integral_{SU(3)} exp(beta Re Tr U / 3) dU,      J(0) = 1
L       = 6 beta^2 d^3
        + (60 beta - beta^2) d^2
        + (-4 beta^2 - 2 beta + 120) d
        - (beta^2 + 10 beta)
```

The candidate statement under finite-window study is:

```text
L . J(beta) = 0
```

with `J(beta)` normalized as the analytic branch at `beta = 0`. The runner
checks this candidate in exact rational arithmetic through the safe degree
window `[beta^0, ..., beta^196]` and records what additional theorem would be
needed to upgrade the finite-window packet.

## Runner Certificates

### [T1] D-Finiteness Witness

The Bars Bessel-determinant formula writes the SU(3) single-plaquette integral
as

```text
J(beta) = sum_{k in Z} det[I_{i-j+k}(beta/3)]_{i,j=0..2}.
```

The runner explicitly constructs, via `sympy.holonomic`, a finite-order
polynomial-coefficient annihilator for the `k=0` determinant summand `D_0`.
It then verifies that constructed annihilator against the closed-form Taylor
series of `D_0` through degree 58 in exact arithmetic.

This is a useful D-finiteness witness and source-integrity check. By itself it
does not supply an all-degree minimal-annihilator bound for the full `k`-sum.

### [T2] Finite-Grid Lower-Order Exclusion

The runner replays the Koutschan-style finite-grid search:

- all scanned order `<= 2`, degree `<= 30` annihilator cells have zero kernel;
- the first non-trivial candidate in the scanned grid appears at order `3`,
  degree `2`;
- the kernel direction at `(r,d) = (3,2)` matches the displayed operator `L`
  up to rational scalar normalization.

This is strong bounded support inside the scanned grid. It is not a proof that
no lower-order annihilator exists at arbitrary coefficient degree.

### [T3] Conditional Bostan-Salvy-Schost Arithmetic

For a D-finite series with an externally supplied annihilator bound of order
`R` and coefficient degree `D`, the standard finite-window sufficiency bound
checks a candidate operator of order `r` and degree `d` through

```text
M_0 = (r + 1)(d + 1) + R + D
```

Taylor coefficients. If an external all-degree `R=3,D=2` bound were supplied,
then for this `r=3,d=2` operator the threshold would be

```text
M_0 = 17.
```

The runner verifies the residual through degree 196, so the threshold
arithmetic would be passed with margin 179 under that external premise. The
runner does not certify the premise.

### [T4] Frobenius-Branch Evidence At beta = 0

The runner computes the candidate operator's indicial polynomial:

```text
6 s (s + 3)(s + 4),       roots = {-4, -3, 0}.
```

For the candidate operator, the only analytic local branch at `beta = 0` has
exponent `s = 0`. The Bessel-determinant Taylor coefficients give

```text
a_0 = 1,   a_1 = 0,   a_2 = 1/36.
```

Thus, if the candidate operator is the governing operator, the normalized
analytic branch is uniquely pinned to the single-plaquette integral branch.
This is branch-identification support for the candidate, not standalone
all-degree closure.

### [T5] Depth-200 Regression

The runner rechecks the original Taylor-annihilation and coefficient-recurrence
certificates at depth 200:

- `L . J` vanishes through the safe range `[beta^0, ..., beta^196]`;
- the induced recurrence holds exactly for `N = 2` through `199`.

Both checks run in exact rational arithmetic.

## What This Packet Establishes

This packet establishes the following bounded support:

- a complete runner-backed finite-window certificate for the V=1
  single-plaquette candidate operator;
- a source-level D-finiteness witness for the `D_0` Bessel-determinant summand;
- finite-grid exclusion of lower-order operators only through degree `30`;
- conditional threshold arithmetic showing what an external all-degree
  `R=3,D=2` theorem would buy;
- Frobenius-branch evidence for the displayed candidate operator at
  `beta = 0`;
- depth-200 exact regression of the Taylor residual and recurrence.

## What This Packet Does Not Establish

This packet does not establish:

- all-degree exclusion of lower-order polynomial-coefficient annihilators;
- all-order minimal-annihilator closure for the SU(3) V=1 integral;
- a thermodynamic-limit, multi-plaquette, higher-irrep, or downstream coupling
  result;
- any audit verdict or repo-wide status promotion.

The remaining mathematical bridge is precise: provide a repo-auditable
all-degree `R=3,D=2` theorem, or keep this row at the finite-window boundary.

## Audit Registration

```yaml
claim_id: plaquette_v1_picard_fuchs_ode_all_order_proof_note_2026-05-09
note_path: docs/PLAQUETTE_V1_PICARD_FUCHS_ODE_ALL_ORDER_PROOF_NOTE_2026-05-09.md
runner_path: scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py
claim_type: bounded_theorem
claim_scope: >
  Finite-window boundary packet for the V=1 single-plaquette SU(3) Wilson
  Picard-Fuchs candidate operator L. The runner supplies exact rational
  checks through degree 196, a D_0 holonomic-closure witness, finite-grid
  order <= 2 exclusion through degree 30, conditional Bostan-Salvy-Schost
  arithmetic under an external all-degree R=3,D=2 premise, Frobenius-branch
  evidence at beta=0, and depth-200 regression. Excludes all-degree
  lower-order exclusion, all-order minimal-annihilator closure,
  thermodynamic-limit claims, multi-plaquette claims, higher-irrep claims,
  downstream coupling claims, and audit verdicts.
intrinsic_status: bounded-support
targeted_audit_repair: scope_too_broad_narrow_to_runner_backed_finite_window_boundary
companion_for_reaudit: plaquette_v1_picard_fuchs_ode_note_2026-05-05
deps:
  - PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md
  - PLAQUETTE_V1_PICARD_FUCHS_ODE_BOUNDED_SYNTHESIS_NOTE_2026-05-06.md
  - PLAQUETTE_V1_PICARD_FUCHS_ODE_KOUTSCHAN_MINIMALITY_NOTE_2026-05-06.md
  - Bessel-determinant identity (Bars 1980)
  - D-finite closure context (Stanley 1980; Lipshitz 1988)
  - SU(N) Wilson character holonomic context (Brower-Nauenberg 1981)
  - D-finite finite-window sufficiency context (Bostan 2010; Mallinger 1996;
    Salvy-Zimmermann 1994)
audit_authority: independent audit lane
```

## Command

```bash
python3 scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py
```

Expected summary:

```text
SUMMARY: FINITE-WINDOW BOUNDARY PASS=5 FAIL=0
```

with output `outputs/su3_v1_picard_fuchs_all_order_certificate_2026_05_09.json`
recording per-certificate detail. Total wall-clock time is about 45-50 seconds
on this local machine.

## Cited Authorities

[1] **Stanley, R. P.** "Differentiably finite power series,"
    *European J. Combin.* 1, 175-188 (1980). Closure of D-finite power
    series under sums and products.

[2] **Lipshitz, L.** "The diagonal of a D-finite power series is
    D-finite," *J. Algebra* 113(2), 373-378 (1988). Closure context for
    D-finite constructions.

[3] **Bars, I.** "U(N) integral for the generating functional in lattice
    gauge theory," *J. Math. Phys.* 21(11), 2678-2681 (1980).
    Bessel-determinant identity for SU(N) Wilson character integrals.

[4] **Brower, R. and Nauenberg, M.** "Group integration for lattice gauge
    theory at large N and at small coupling," *Nucl. Phys. B* 180, 221-247
    (1981). SU(N) holonomic-operator context for Wilson character integrals.

[5] **Mallinger, C.** "Algorithmic Manipulations and Transformations of
    Univariate Holonomic Functions and Sequences," MSc thesis, RISC Linz
    (1996). Explicit finite-window sufficiency bound for D-finite identity
    verification.

[6] **Bostan, A.** "Algorithms for D-finite power series and holonomic
    D-modules," lecture notes / tutorial (2010). Standard D-finite
    finite-window verification context.

[7] **Salvy, B. and Zimmermann, P.** "Gfun: a Maple package for the
    manipulation of generating and holonomic functions," *ACM Trans. Math.
    Softw.* 20(2), 163-177 (1994). D-finite manipulation and finite-window
    verification context.
