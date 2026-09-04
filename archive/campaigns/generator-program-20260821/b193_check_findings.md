# Block 193 adversarial check: window law / cutoff mechanism

Status: **FINAL — CORE CONFIRMED, PARITY EXTENSION REFUTED** (exact SymPy
`Rational`/QQ only; no approximate reconstruction).

## Scope and provenance

- Fixture requested: `m = 9/20`, `c = 5/13`, base `T = 16`, width probes at `T = 20`.
- Construction authorities selected from landed block branches:
  - block 190 commit `e75ad9f4998ae4cc6a25a2e20191e0b9d76ff3fd` (width-family transfer/monodromy note and runner);
  - block 191 commit `36f54ab2ad6e51cbe2bf6b8b604b63236f2c936e` (boundary-mode volume-sensitivity note and runner).
- Fresh fetch on 2026-08-25 found no landed block-192 hybridization/support-cutoff note. The only remote block-192 branch was `toe-axiom-closure-block192-full-temporal-carrier-20260825`, whose note is unrelated to this package, so it is excluded.
- The shared checkout contains unrelated dirty work and is treated as read-only. Only the two files in this scratchpad are created by this check.

## Claim checklist

- C1 identity iff first-order invariance: **CONFIRMED on the requested six cases and both finite amplitudes**.
- C2 18-cell odd-core window law: **CONFIRMED 18/18 (and for all four spatial translates)**.
- C3 attack on last-slice exemption: **NOT REFUTED on the odd cores; stronger basis exhaustion passed**.
- C4 harmonic-response/two-step derivation: **CONFIRMED**.
- P1 width: **CONFIRMED 9/9 at `T=20`**.
- P2 parity: **REFUTED — even cores carry a one-slice-shifted window**.
- P3 all-delta: **CONFIRMED at three distinct exact rationals**.

## Exact reconstruction controls

The independent checker is `b193_exact_check.py` in this directory. It rebuilds
the wrap-edge staggered kernel, grading projectors, restricted raising part,
reflection glue, cell embeddings, reflected Hodge profile, `Q`, `G`, `K_c`,
`L_2`, and `W` from the displayed formulas rather than importing either landed
runner. All large inverses use `DomainMatrix(...).convert_to(QQ).inv()`.

At `T=16`:

- the requested `dB` is exactly `d/dδ B(c,1-δ)|_{δ=0}`;
- `Q G - I` has `0` nonzero entries;
- `Ps H Ps - H` has `0` nonzero entries;
- `Ps Q Ps - Q^T` has `0` nonzero entries.
- as a construction fingerprint, the independently rebuilt deep
  `charpoly(W)` at core `t0=3` is exactly
  `(22569375 z^2 - 233631106 z + 22569375)^2
   (39529825 z^2 - 109432706 z + 39529825)^2`, matching the landed notes;
- the independently rebuilt finite `{2,3}`, `δ=1/5` factors at cores
  `1,3,5` match all coefficients in the block-191 claim register, including
  the exact baseline survivor at core `5`.

The clean-worktree audit pipeline was also attempted at landed block-191 commit
`36f54ab...`; it stopped at step 7 because that historical branch's
`dependency_policy_epoch.json` no longer matches the current governed policy
sources. This stale-branch governance mismatch is not used
as scientific evidence. The exact scoped checker itself completed with exit 0.

## C1 — finite identity iff first-order invariance

For the bump derivative, `dH` is the sum of the reflected one-cell derivatives
over all four spatial cells at each named positive anchor. With
`dG = -G dQ G`, `R = dL_2 - dK_c W`, and `dW = K_c^{-1}R`, the six requested
cases are:

| bump, core | `nnz(R)` | `nnz(dW)` | `nnz(W(1/5)-W(0))` | `nnz(W(1/3)-W(0))` |
| --- | ---: | ---: | ---: | ---: |
| `{1,2}`, `5` | 0 | 0 | 0 | 0 |
| `{2,3}`, `5` | 0 | 0 | 0 | 0 |
| `{4,5}`, `1` | 0 | 0 | 0 | 0 |
| `{3,4}`, `5` | 64 | 64 | 64 | 64 |
| `{2,3}`, `1` | 64 | 64 | 64 | 64 |
| `{2,3}`, `3` | 64 | 64 | 64 | 64 |

Thus both directions hold on the stipulated table, entrywise over `QQ`, for
both finite amplitudes. This is not being generalized from the six cases.

## C2 — the odd-core window law at `T=16`

The source is one reflected cell at spatial anchor `x=0`; checking `x=1,2,3`
as well gives the identical zero/nonzero pattern. Every breaking residual is
fully dense (`nnz(R)=64`), and every compatible residual is the exact zero
matrix:

| core `t0` | measured breaking cells | measured compatible cells | expected |
| ---: | --- | --- | --- |
| 1 | `{1,2,3}` | `{4,5,6}` | match |
| 3 | `{2,3,4,5}` | `{1,6}` | match |
| 5 | `{4,5,6}` | `{1,2,3}` | match |

Therefore, on the requested odd cores,

`R=0 iff {s,s+1} ∩ [t0,t0+2] = ∅ iff s ∉ [t0-1,t0+2]`

holds in all 18 cases, and the same incidence result holds for all four
spatial translates of the source cell.

## C3 — attack on the `t0+3` exemption

For the odd cores governed by C2, the exemption survived every attempted
attack:

- the admissible reflected Block-105 volume tangent cell at `s=t0+3` gives
  `nnz(R)=0` for all four spatial positions at `t0=1` and `t0=3`;
- every one of the 16 (including asymmetric) `4x4` cell-block matrix-unit
  directions, embedded in that cell and completed by its `P4` image, gives
  `R=0` at both cores;
- every raw same-slice matrix unit `E_{(s,x),(s,y)}`, including asymmetric and
  reflection-completed variants, gives `R=0`;
- more strongly, all raw matrix units whose **row** lies on any positive slice
  from `t0+3` through the fixed slice `T/2`, with an arbitrary column anywhere
  in the 64-dimensional carrier, give `R=0`: 1280/1280 basis directions at
  `t0=1`, and 768/768 at `t0=3`; the corresponding reflected-image units and
  reflection-completed sums also give zero in every basis direction.

So no linear source whose positive-side row support begins at `t0+3` can break
the odd-core relation. The proposed asymmetric-source refutation therefore
fails. This conclusion is scoped to the tested valid odd cores and the finite
`T=16` carrier.

## P1 — width spot check at `T=20`

The same odd-core incidence law holds in all nine requested cases:

| cell `s` | core 3 | core 5 | core 7 |
| ---: | :---: | :---: | :---: |
| 3 | BRK (64) | OK (0) | OK (0) |
| 4 | BRK (64) | BRK (64) | OK (0) |
| 7 | OK (0) | BRK (64) | BRK (64) |

## P2 — parity refutation and corrected finite rule

The proposed parity-independent window is false. At the even cores the
measured break set is shifted forward by one slice:

| core `t0` | proposed breaks (within `s=1..6`) | measured breaks | mismatches |
| ---: | --- | --- | --- |
| 2 | `{1,2,3,4}` | `{2,3,4,5}` | `s=1` false positive; `s=5` false negative |
| 4 | `{3,4,5,6}` | `{4,5,6}` within the requested range; `{4,5,6,7}` when `s=7` is added | `s=3` false positive; omitted `s=7` is a break |

The finite rule supported by these data is instead

`even t0: R=0 iff {s,s+1} ∩ [t0+1,t0+3] = ∅`,

equivalently `s ∉ [t0,t0+3]`. This also explains why an admissible
`s=t0+3` cell breaks with `nnz(R)=32` at even `t0=2,4`, while it is exempt on
the odd cores.

An exact unexpected-break witness is

`R[0,4] = 303717414128393981002946552450301011272963193469691599136505997554493148222247708710000000 / 77707725095998816829080256798567544217876202163787270905242891606801827087957579200283634261`

for `(t0,s)=(2,5)`. Conversely, `(t0,s)=(2,1)` and `(4,3)` give the exact zero
matrix even though the proposed parity-independent rule labels them breaking.

## C4 — direct harmonic-response derivation

Let `y_a = dQ G[:,theta_a]` and `u_a = G y_a` as in the prompt.

1. For each of the six one-cell sources and every one of the eight core-frame
   columns at each `t0=1,3,5` (144 exact column checks),
   `Q u_a - y_a = 0`. The row support of `y_a` equals the full row support of
   `dQ` in all 144 cases, with no cancellation. The `dQ` row-support sizes for
   `s=1..6` are `(14,16,16,16,16,14)`. Their slice supports are respectively
   `{0,1,2,14,15}`, `{2,3,4,12,13,14}`, `{2,3,4,12,13,14}`,
   `{4,5,6,10,11,12}`, `{4,5,6,10,11,12}`, and `{6,7,8,9,10}`.
   Hence `(Q u_a)_r=0` on every row outside the source row support: the response
   is exactly `Q`-harmonic there.
2. At unperturbed cores `t0=1,3,5`, `K_c W-L_2=0_8` entrywise, i.e.

   `G[b+2,theta_a] = sum_{b'} G[b',theta_a] W[b',b]`.

   For all 18 odd-core source/core pairs, the independently assembled response
   residual obeys

   `u_a[b+2] - sum_{b'} u_a[b'] W[b',b] = -R[a,b]`

   entrywise (zero discrepancy in all 18 matrix checks). Thus `R=0` is exactly
   the statement that the response field obeys the same two-step frame
   relation. Algebraically this is also `R=K_c dW`, since differentiating
   `L_2=K_c W` gives `dL_2=dK_c W+K_c dW`; invertibility of `K_c` makes
   `R=0 iff dW=0`.

## P3 — three exact finite amplitudes

For the zero case bump `{2,3}` at core `t0=5`,
`W(δ)-W(0)=0_8` entrywise at each of
`δ = 1/5, 1/3, 2/5`. This satisfies the requested three-rational alternative
to a symbolic-`δ` proof; it does not by itself promote the result to a formal
all-`δ` theorem.

## Adversarial verdict and handoff

**Verdict.** C1, C2, C3, C4, P1, and P3 survive at their explicitly tested
scope. P2 is refuted. The core odd-`t0` cutoff mechanism is therefore supported
exactly, but it is **not parity-independent**.

Issue: the proposed extension of the odd-core window `[t0,t0+2]` to even
cores is false. At `t0=2`, sources `s=1` and `s=5` give the opposite statuses
from that rule; at `t0=4`, `s=3` and the added `s=7` do likewise.

Why this blocks: a theorem stated without a core-parity hypothesis would make
incorrect exact predictions, including treating the even-core last slice
`s=t0+3` as exempt when its admissible one-cell residual has 32 nonzero
entries.

Repair target: replace the parity-independent statement by the measured
piecewise rule

- odd `t0`: effective response window `[t0,t0+2]`, so breaks are
  `s in [t0-1,t0+2]`;
- even `t0`: effective response window `[t0+1,t0+3]`, so breaks are
  `s in [t0,t0+3]`;

then prove that piecewise law from the staggered `Q` recurrence (or state it as
a finite exact table until that proof exists).

Claim boundary until fixed: the requested odd-core `T=16` table (18/18), the
odd-core `T=20` spot check (9/9), the six C1 finite-bump equivalences, the
odd-core exemption attack, and both C4 derivation pillars remain intact.

## Reproduction

Run:

```bash
python3 b193_exact_check.py
```

The checker prints one line per claim/probe and ends with
`TOTAL: PASS=6 FAIL=1`; the sole failure is P2. Its source contains no float,
numeric-evaluation, tolerance, or forbidden simplification path.
