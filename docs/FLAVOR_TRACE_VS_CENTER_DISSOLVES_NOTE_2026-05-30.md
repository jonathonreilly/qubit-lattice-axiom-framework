# Flavor Trace-vs-Center Restricted Source Packet

**Date:** 2026-05-30; repaired 2026-06-06
**Claim type:** bounded_theorem.
**Claim boundary:** restricted finite `C_3` circulant algebra/source packet. This
note instantiates the trace formula, center/block-count inventory formula,
Bures/SLD sector-balance value, heat/Seeley coefficient endpoint behavior, and
positive-chamber eigenvalue-as-mass computation. It does not derive the
physical charged-lepton readout, the block-count selector, or the Fourier
modulus.
**Runner:** [`scripts/flavor_trace_vs_center_dissolves_2026_05_30.py`](../scripts/flavor_trace_vs_center_dissolves_2026_05_30.py)
(SCORECARD PASS=17 FAIL=0).
**Cached runner output:** [`logs/runner-cache/flavor_trace_vs_center_dissolves_2026_05_30.txt`](../logs/runner-cache/flavor_trace_vs_center_dissolves_2026_05_30.txt)

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The finite formulas named in the audit blocker are now instantiated, but the physical readout and selector remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setup

The source packet uses the two-level real `C_3` circulant chamber

```text
H = a I + b(C + C^2),      C^3 = I,      a > 0,
lambda_s = a + 2b,         lambda_d = a - b,      r = b^2/a^2.
```

The doublet eigenvalue has multiplicity two in the matrix trace. The
block-count formula below is a separate inventory functional: it weights the
complex doublet block once while keeping the same trace normalization. That
functional is not asserted to be the physical readout unless a later theorem
selects it.

## Exact Packet Results

### 1. Signed trace/dimension formula

With the signed/Hermitian readout,

```text
Q_trace =
((a + 2b)^2 + 2(a - b)^2) / ((a + 2b) + 2(a - b))^2
= (a^2 + 2b^2)/(3a^2)
= 1/3 + (2/3) r.
```

Therefore `Q_trace = 2/3` if and only if `r = 1/2`. This is an exact finite
algebra identity. It does not by itself prove that charged-lepton masses use the
signed/Hermitian readout.

### 2. Center/block-count inventory formula

The restricted center/block-count inventory functional replaces the doublet's
two real trace dimensions by one complex block:

```text
Q_block = (3a^2 + 3b^2)/(3a)^2
        = 1/3 + (1/3) r.
```

Thus `Q_block = 2/3` occurs at `r = 1`, not at `r = 1/2`; at `r = 1/2`, this
functional gives `Q_block = 1/2`. This is the exact formula behind the
"center/block-count" line. It is a modeled block functional, not a physical
trace theorem.

### 3. Eigenvalue-as-mass is separated from singular-value readout

On the positive chamber with `x = b/a in (0,1)`, the eigenvalue-as-mass readout
uses `m_s = lambda_s`, `m_d = lambda_d`, so

```text
Q_eig-mass =
3 / (sqrt(1 + 2x) + 2 sqrt(1 - x))^2.
```

Solving `Q_eig-mass = 2/3` gives

```text
16x^2 - 8x - 7 = 0,
x = 1/4 + sqrt(2)/2,
r = x^2 = 9/16 + sqrt(2)/4 ~= 0.916053.
```

This computation is only the positive-chamber eigenvalue-as-mass solve. It is
not a global singular-value/Yukawa readout claim. A singular-value readout uses
`|lambda_k|` across sign and phase chambers, so it is a separate residual.

### 4. Fisher and Bures/SLD sector balances

The unnormalized eigenvalue-Fisher sector balance

```text
((d lambda_s/dr)^2 / lambda_s^2)
= 2 ((d lambda_d/dr)^2 / lambda_d^2)
```

lands at

```text
r = 17/2 - 6 sqrt(2) ~= 0.014719.
```

For the commuting normalized spectral density

```text
p_s = (1 + 2x)/3,
p_d = (1 - x)/3     for each doublet copy,
```

the Bures/SLD metric is one quarter of the classical Fisher metric. Equating
singlet and total-doublet SLD sector contributions gives

```text
r = 1/16.
```

Neither metric balance selects `r = 1/2`.

### 5. Heat/Seeley coefficient endpoint behavior

In the same chamber, the even heat coefficients are

```text
A_n(r) = Tr(H^(2n)) = (1 + 2x)^(2n) + 2(1 - x)^(2n),      x = sqrt(r).
```

The runner checks `n = 1..4` symbolically. Each derivative has no interior root
on `x in (0,1)`, so coefficient-level extremization selects only endpoints
`r = 0` or `r = 1`; it does not select the interior point `r = 1/2`.

The related action-axis packet
[`FLAVOR_NATIVE_ACTION_PREDICTS_Q1_2026-06-02.md`](FLAVOR_NATIVE_ACTION_PREDICTS_Q1_2026-06-02.md)
separately checks five displayed spectral-action cutoffs and likewise does not
derive `r = 1/2`.

## What This Repairs

The prior note displayed the right trace identity but left several numerical
inventory entries too implicit. The repaired runner now instantiates:

| entry | repaired status |
| --- | --- |
| signed trace formula | exact symbolic derivation |
| center/block-count formula | exact restricted functional, scoped as non-physical unless selected |
| eigenvalue-as-mass `r ~= 0.916053` | exact positive-chamber solve |
| Bures/SLD `r = 1/16` | exact normalized spectral-sector balance |
| heat/Seeley endpoint behavior | exact coefficient endpoint checks for `n = 1..4` |

## Remaining Residuals

The current source packet does not close the science. The residuals are:

- **readout class:** why charged leptons should use the signed/Hermitian
  square-root readout rather than a singular-value/Yukawa readout;
- **block selector:** why the physical functional should be trace/dimension,
  block-count, or another native reference state;
- **modulus selector:** why `r = 1/2` should be selected rather than merely
  matched by `Q_trace = 2/3`;
- **phase/sign chamber:** how the broader `b = |b|e^{i phi}` chamber is selected.

No new axiom, measured mass input, or audit verdict is introduced here.

## Next Useful Path

The highest-value closure route remains a native selector theorem: records,
KMS/modular structure, or matter-action dynamics would need to select both the
signed/Hermitian readout and the `r = 1/2` modulus. A theorem selecting the
dimension/trace reading instead would point the packet to `r = 1`/`Q = 1`, not
to the charged-lepton Koide value.
