# Alpha_s Heavy-Threshold Matching Kernel Theorem Note (2026-06-18)

**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded algebraic kernel conditional on the explicit LO no-jump
matching input
**Primary runner:** `scripts/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.py`
**Runner summary:** `SUMMARY: PASS=27 FAIL=0`
**Parent audit pressure:** `alpha_s_direct_wilson_loop_honest_status_audit_note_2026-05-02`

## 1. Purpose

The audited alpha_s direct Wilson-loop lane is blocked, in part, because the
QCD running step imported threshold matching as textbook machinery. This note
removes one precise algebraic part of that import: given the leading-order
continuity matching condition for a heavy-flavor threshold and the explicit
SU(3) one-loop running surface stated below, the Lambda-parameter transition
and finite piecewise inverse-coupling map follow algebraically.

This is not a retained alpha_s(M_Z) theorem. It is a kernel theorem that can be
composed with later scale-setting, sea-quark, and higher-loop bridges.

This theorem's object is the leading-order continuity matching kernel
**conditional on** the no-jump condition. The continuity condition is an
explicit conditional matching input here, not a theorem derived in this row.

## 2. Boundary Clauses

This note does not derive physical threshold masses.

This note does not derive the LO heavy-threshold no-jump condition
`alpha_s^hi(M) = alpha_s^lo(M)`. That condition is the explicit conditional
matching input for this bounded kernel.

This note does not supply higher-loop MSbar decoupling constants.

This note does not promote any downstream alpha_s(M_Z) value to retained status.

This note does not derive the Sommer scale, a Wilson-loop physical scale
anchor, a pure-gauge-to-full-QCD sea-quark transfer map, or a framework-native
four-loop beta function.

## 3. Explicit One-Loop Surface

For this bounded kernel, the supplied surface is the same one-loop SU(3)
running surface used by
`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`:

```text
x(mu) := 1 / alpha_s(mu)
d x / d ln(mu) = b0(n_f) / (2 pi)
b0(n_f) = (11/3) C_A - (4/3) T_F n_f
C_A = 3,  T_F = 1/2
```

Therefore

```text
b0(n_f) = 11 - 2 n_f / 3.
```

For fixed active flavor count `n_f`, running from `mu_hi` down to `mu_lo`
gives the affine inverse-coupling map

```text
x(mu_lo) = x(mu_hi) - [b0(n_f)/(2 pi)] log(mu_hi / mu_lo).
```

This is a theorem on arbitrary positive scales. It does not use numerical
quark masses.

## 4. Explicit Conditional Threshold Continuity Input

Let a heavy threshold sit at an abstract positive scale `M`, with active flavor
count `n_f_hi` above the threshold and `n_f_lo = n_f_hi - 1` below it. The
single explicit conditional matching input is continuity of the coupling:

```text
alpha_s^hi(M) = alpha_s^lo(M)
```

Equivalently,

```text
x_hi(M) = x_lo(M).
```

The runner verifies the algebraic consequences of this input as a structural
event in the piecewise running map: at each threshold, the inverse-coupling
value is carried across without a jump, while the slope changes from
`b0(n_f_hi)/(2 pi)` to `b0(n_f_lo)/(2 pi)`. The runner does not derive the
no-jump matching condition itself.

## 5. Lambda-Parameter Transition

On a one-loop segment,

```text
x(mu) = [b0(n_f)/(2 pi)] log(mu / Lambda_nf).
```

The explicit continuity input at `M` imposes

```text
b0(n_f_hi) log(M / Lambda_hi)
  = b0(n_f_lo) log(M / Lambda_lo).
```

Solving gives the conditional framework-local transition law

```text
Lambda_lo = M * (Lambda_hi / M) ** [b0(n_f_hi) / b0(n_f_lo)].
```

The runner checks that this law exactly preserves the explicit threshold
coupling and that reconstructing `Lambda_nf` from `x(M)` inverts the one-loop
solution.

## 6. Composition Theorem

For a strictly descending list of abstract thresholds

```text
mu_hi > M_1 > M_2 > ... > M_k > mu_lo > 0,
```

with active flavor count dropping by one at each threshold, the piecewise map
is

```text
x(mu_lo) =
  x(mu_hi)
  - sum_j [b0(n_f_j)/(2 pi)] log(mu_j^hi / mu_j^lo).
```

The runner verifies that:

1. fixed-`n_f` segments compose as a semigroup;
2. upward and downward fixed-`n_f` maps invert each other;
3. the multi-threshold kernel equals the summed-log closed form;
4. each threshold event implements the explicit continuity condition in
   `x = 1/alpha_s`;
5. non-descending thresholds, out-of-domain thresholds, and skipped flavor
   crossings are rejected.

## 7. Falsifier

The runner includes a deliberate false event where `alpha_s` is multiplied
across a threshold. This produces a nonzero inverse-coupling jump and is
detected. The theorem therefore pins a checkable conditional implementation
class, not just a numerical output.

## 8. Audit Implication

If accepted, this theorem partially retires the algebraic Lambda-transition
and piecewise-composition part of the "threshold matching" import for the
alpha_s audit lane at the leading-order kernel level. It does not retire the
no-jump matching condition itself, and it does not close the audited alpha_s
row by itself. Remaining bridge work includes:

- retained/native derivation or approved-premise registration of the LO
  threshold no-jump condition;
- physical threshold placement or a framework-native replacement for it;
- higher-loop MSbar running and decoupling;
- Sommer-scale or alternate Wilson-loop physical scale anchoring;
- pure-gauge-to-full-QCD transfer;
- the separate `g_bare`/normalization dependency surface.

If independently retained, the intended downstream use is as an algebraic
kernel that future alpha_s repairs can cite in parallel with standard QCD
references, rather than importing the Lambda-transition and multi-threshold
composition steps as unproved black boxes. Any downstream proof still needs
separate authority for the threshold-continuity input.

## 9. Reproducibility

Run:

```bash
python3 scripts/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.py
```

Expected summary:

```text
SUMMARY: PASS=27 FAIL=0
```

The cached output is recorded at
`logs/runner-cache/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.txt`.
