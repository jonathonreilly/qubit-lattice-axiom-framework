# Alpha_s Heavy-Threshold Matching Kernel Theorem Note (2026-06-18)

**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded support theorem; independent re-audit required
**Primary runner:** `scripts/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.py`
**Runner summary:** `SUMMARY: PASS=40 FAIL=0`
**Parent audit pressure:** `alpha_s_direct_wilson_loop_honest_status_audit_note_2026-05-02`

## 1. Purpose

The audited alpha_s direct Wilson-loop lane is blocked, in part, because the
QCD running step imported threshold matching as textbook machinery. This note
closes the leading-order part of that import. For one heavy flavor in
continuum SU(3) QCD renormalized in MSbar, the one-loop heavy-quark vacuum
polarization gives the coupling decoupling factor. At the mass-fixed matching
point `M = m_h^(n_f)(M)`, its only one-loop term is a logarithm and vanishes.
The resulting no-jump relation then supplies the Lambda-parameter transition
and finite piecewise inverse-coupling map.

This is not a retained alpha_s(M_Z) theorem. It is a kernel theorem that can be
composed with later scale-setting, sea-quark, and higher-loop bridges.

The equality in this note is perturbative and order-qualified:

```text
alpha_s^(n_f-1)(M) = alpha_s^(n_f)(M) + O(alpha_s^3)
```

Equivalently, the coupling is exactly continuous after truncation through
one-loop matching. This note does not assert all-orders continuity.

## 2. Boundary Clauses

This note does not derive the numerical value of a physical threshold mass.
It proves the matching statement at any positive mass-fixed point
`M = m_h^(n_f)(M)` for which perturbative matching is applicable.

This note does not supply two-loop or higher MSbar decoupling constants. In
particular, it does not erase the finite two-loop matching correction.

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

This algebraic segment identity holds on positive scales for which the evolved
inverse coupling remains positive. Its physical use is restricted to the
perturbative domain; the theorem does not continue the one-loop formula
through its Landau pole. It does not use numerical quark masses.

## 4. One-Loop MSbar Decoupling Derivation

Let the full theory have `n_f` flavors, one of them a heavy quark `h` with
running MSbar mass `m_h(mu)`. The low-energy effective theory has
`n_l = n_f - 1` light flavors. Define the coupling decoupling factor by

```text
alpha_s^(n_l)(mu) = zeta_g^2(mu, m_h) alpha_s^(n_f)(mu).
```

For the leading-power, dimension-four background-gluon kinetic coefficient at
one loop, the only full-theory diagram absent from the effective theory is the
heavy-quark contribution to the background-gluon two-point function,

```text
i Pi_h,mu nu^ab(q) = -g_s^2 T_F delta^ab mu^(2 epsilon)
  integral[d^d k/(2 pi)^d]
  Tr[gamma_mu (k_slash + m_h) gamma_nu (k_slash + q_slash + m_h)]
  / [(k^2-m_h^2)((k+q)^2-m_h^2)].
```

The Dirac trace and Feynman parametrization make the result transverse. After
MSbar subtraction, its zero-momentum scalar coefficient is

```text
Pi_h^MSbar(0; mu, m_h)
  = (2 alpha_s T_F / pi)
    integral_0^1 dx x(1-x) log(mu^2/m_h^2)
  = (alpha_s T_F / (3 pi)) log(mu^2/m_h^2),
```

because `integral_0^1 dx x(1-x) = 1/6`. Here is the field-normalization step
that turns this polarization into coupling matching. Write the low-energy
background field as

```text
A_l = sqrt(zeta_3) A_h,
zeta_3 = 1 + Pi_h^MSbar(0) + O(alpha_s^2).
```

The light-field covariant derivative must be the same operator in both
descriptions. Background-gauge covariance therefore requires

```text
g_l A_l = g_h A_h,
zeta_g sqrt(zeta_3) = 1.
```

Consequently, through one-loop matching,

```text
zeta_g^2(mu, m_h)
  = [1 + Pi_h^MSbar(0; mu, m_h)]^(-1) + O(alpha_s^2)
  = 1 - Pi_h^MSbar(0; mu, m_h) + O(alpha_s^2)
  = 1 - [alpha_s T_F/(3 pi)] log(mu^2/m_h^2) + O(alpha_s^2).
```

For SU(3), `T_F = 1/2`, hence

```text
zeta_g^2(mu, m_h)
  = 1 - [alpha_s/(6 pi)] log(mu^2/m_h^2) + O(alpha_s^2).
```

The sign and factor also follow independently from renormalization-group
consistency. Write the logarithmic term as
`c (alpha_s/pi) log(mu^2/m_h^2)`. Since removing one flavor changes
`b0` by `b0(n_f-1)-b0(n_f)=2/3`, differentiating the matching relation with
respect to `log(mu)` gives

```text
2 c alpha_s^2/pi
  = -[b0(n_f-1)-b0(n_f)] alpha_s^2/(2 pi),
```

and therefore `c=-1/6`. The runner checks agreement between this beta-function
route and the Feynman-parameter route.

Choose the matching point to satisfy the standard mass-fixed condition

```text
M = m_h^(n_f)(M).
```

The logarithm then vanishes. Therefore

```text
alpha_s^(n_f-1)(M) = alpha_s^(n_f)(M) + O(alpha_s^3),
x_(n_f-1)(M) = x_(n_f)(M) + O(alpha_s).
```

On the one-loop-running/one-loop-matching truncation used by this theorem, the
remainders are outside scope and the threshold map is exactly the no-jump map.
The runner now constructs each event by evaluating `zeta_g^2` at
`mu = m_h = M`; it no longer assigns `x_below = x_above` as an independent
premise. It also checks that a mismatched `mu/m_h` produces a nonzero log and
therefore is not a no-jump event. An exact coefficient check verifies
`zeta_g^2(1+Pi_h)=1+O(alpha_s^2)` at linear order.

For convention and provenance, this derivation agrees with K. G. Chetyrkin,
B. A. Kniehl, and M. Steinhauser, *Decoupling Relations to O(alpha_s^3) and
their Connection to Low-Energy Theorems*, Nucl. Phys. B510 (1998) 61--87,
[arXiv:hep-ph/9708255](https://arxiv.org/abs/hep-ph/9708255): their equations
(7), (18), and (23) define the same decoupling relation and give the same
one-loop logarithm. The source is a convention cross-check; the displayed
one-loop integral and its evaluation are the load-bearing derivation here.

The zero-momentum projection is essential. Power corrections such as
`q^2/m_h^2` belong to higher-dimension effective operators and are not part of
this coupling-matching theorem.

## 5. Lambda-Parameter Transition

On a one-loop segment,

```text
x(mu) = [b0(n_f)/(2 pi)] log(mu / Lambda_nf).
```

The derived one-loop no-jump relation at `M = m_h(M)` imposes, at the theorem's
truncation order,

```text
b0(n_f_hi) log(M / Lambda_hi)
  = b0(n_f_lo) log(M / Lambda_lo).
```

Solving gives the framework-local transition law

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

with active flavor count dropping by one at each threshold, assume that every
event is its own mass-fixed MSbar point,

```text
M_j = m_h_j^(n_f_j)(M_j),
```

and that `x` remains positive on every segment. The piecewise map is then

```text
x(mu_lo) =
  x(mu_hi)
  - sum_j [b0(n_f_j)/(2 pi)] log(mu_j^hi / mu_j^lo).
```

The runner verifies that:

1. fixed-`n_f` segments compose as a semigroup;
2. upward and downward fixed-`n_f` maps invert each other;
3. the multi-threshold kernel equals the summed-log closed form;
4. each threshold event evaluates the one-loop MSbar decoupling factor at its
   mass-fixed point and therefore implements the derived no-jump relation in
   `x = 1/alpha_s`;
5. non-descending thresholds, out-of-domain thresholds, skipped flavor
   crossings, nonpositive initial coupling, and Landau-pole crossings are
   rejected.

## 7. Falsifier

The runner includes a deliberate false event where `alpha_s` is multiplied
across a threshold. This produces a nonzero inverse-coupling jump and is
detected. The theorem therefore pins a checkable conditional implementation
class, not just a numerical output.

## 8. Audit Implication

If independently audited clean, this theorem retires the leading-order
no-jump condition together with the algebraic Lambda transition and
piecewise-composition part of the threshold-matching import. It does not close
the broader alpha_s direct Wilson-loop row. Remaining bridge work includes:

- physical threshold placement or a framework-native replacement for it;
- higher-loop MSbar running and decoupling;
- Sommer-scale or alternate Wilson-loop physical scale anchoring;
- pure-gauge-to-full-QCD transfer;
- the separate `g_bare`/normalization dependency surface.

The intended downstream use is as a bounded perturbative kernel. Any
downstream proof still needs separate authority for physical threshold masses,
the chosen perturbative domain, and every correction beyond this order.

## 9. Reproducibility

Run:

```bash
python3 scripts/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.py
```

Expected summary:

```text
SUMMARY: PASS=40 FAIL=0
```

The cached output is recorded at
`logs/runner-cache/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.txt`.
