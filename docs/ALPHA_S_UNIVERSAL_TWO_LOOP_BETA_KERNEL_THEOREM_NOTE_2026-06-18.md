# Defined Two-Coefficient Polynomial Vector-Field Algebra Theorem Note (2026-06-18)

**Type:** positive_theorem
**Primary runner:** `scripts/frontier_alpha_s_universal_beta_kernel_2026_06_18.py`
**Runner cache:**
`logs/runner-cache/frontier_alpha_s_universal_beta_kernel_2026_06_18.txt`
**Dependencies:** none. All symbols and coefficient polynomials used below are
defined theorem data.

## 1. Exact theorem data

Work over exact rational arithmetic and let `n` be a rational parameter. Set

```text
N = 3,
C_A = N = 3,
C_F = (N^2 - 1)/(2N) = 4/3,
T_F = 1/2.
```

These equalities are definitions inside this theorem packet. They are not
claims that a physical colour carrier, a gauge theory, or a matter spectrum
has been selected.

Define two affine coefficient polynomials by

```text
b0(n) = (11/3) C_A - (4/3) T_F n,

b1(n) = (34/3) C_A^2
        - 4 C_F T_F n
        - (20/3) C_A T_F n.
```

No QFT calculation, universality statement, or physical beta-function
interpretation is part of these definitions.

## 2. Formal coefficient theorem

Direct exact substitution gives

```text
b0(n) = 11 - 2n/3,
b1(n) = 102 - 38n/3.
```

Consequently, for every rational `n`,

```text
b0(n + 1) - b0(n) = -2/3,
b1(n + 1) - b1(n) = -38/3.
```

The exact listed specializations are

```text
b0(6) = 7,       b0(5) = 23/3,
b1(6) = 26,      b1(5) = 116/3,
b1(4) = 154/3,   b1(3) = 64.
```

The roots are `b0(33/2) = 0` and `b1(153/19) = 0`. Thus, on
nonnegative integers,

```text
b0(n) > 0 for 0 <= n <= 16 and b0(n) < 0 for n >= 17,
b1(n) > 0 for 0 <= n <= 8  and b1(n) < 0 for n >= 9.
```

These are sign facts about the defined affine polynomials only. Terms such as
"active flavour" and "asymptotic freedom" would add physical semantics that
this theorem does not supply.

## 3. Defined vector field and induced variables

Let `pi` denote the exact positive constant and let `g` be a real formal
coordinate. Define the polynomial vector field

```text
V_g(g,n) = -b0(n) g^3/(16 pi^2)
           -b1(n) g^5/(16 pi^2)^2.
```

For any differentiable real trajectory `g(s)` satisfying
`dg/ds = V_g(g,n)`, define the induced variables

```text
alpha = g^2/(4 pi),
a = alpha/(4 pi),
```

Because `pi > 0` and `g` is real, the induced variables satisfy
`alpha >= 0` and `a >= 0`. The square map is many-to-one, so this is not a
global invertible coordinate change on the real line. The chain rule gives,
on the induced nonnegative half-lines,

```text
V_alpha(alpha,n)
  = -b0(n) alpha^2/(2 pi)
    -b1(n) alpha^3/(8 pi^2),

V_a(a,n)
  = -2 b0(n) a^2 - 2 b1(n) a^3.
```

The first identity follows from `d alpha/dg = g/(2 pi)` and the exact
substitutions `g^4 = 16 pi^2 alpha^2` and
`g^6 = 64 pi^3 alpha^3`. The second follows from
`d a/d alpha = 1/(4 pi)` and `alpha = 4 pi a`. Their polynomial right-hand
sides have unique algebraic extensions to arbitrary real `alpha` and `a`, but
only the nonnegative values are induced by a real `g`. The trajectory
parameter `s` is untyped formal data; no physical scale interpretation is
used. No numerical coupling value, small-coupling estimate, convergence
statement, or running solution is used.

## 4. Exact scope firewall

The theorem proves only algebra about explicitly defined polynomials and their
explicitly defined vector field. In particular, it does not establish that

- `b0` or `b1` is a QCD, gauge-theory, loop, or scheme-independent
  coefficient;
- `N=3`, `C_F`, `C_A`, or `T_F` describes a physical colour sector;
- `n` counts physical or active flavours, or that any threshold selects a
  value of `n`;
- `g`, `alpha`, or `a` is a physical coupling, `s` is `ln(mu)` or any other
  physical scale variable, or the vector field governs physical running;
- the displayed coefficient templates follow from the framework axioms,
  approved primitives, Casimirs, a matter carrier, or QFT;
- higher coefficients, counterterms, a renormalization scheme, threshold
  matching, `alpha_s(M_Z)`, a Wilson action, scale setting, sea-quark
  transfer, or `g_bare` normalization have been supplied.

Those physical and QFT identifications remain separate inputs or open bridges.
They are not dependencies of this formal theorem because none is used in its
proof.

## 5. Falsification and reproducibility

The runner uses exact `Fraction` and SymPy identities. It provides:

- a normal derivation of the coefficient, slope, root, sign, and induced-variable
  identities;
- an independent symbolic reconstruction and multiple rational `(n,g)`
  examples;
- hostile controls that must reject changed coefficients, signs, convention
  factors, and physical-semantics requests; and
- individually selectable intentional-failure fixtures. Every individual
  fixture and the aggregate fixture exit nonzero when the mutation is
  detected.

Run:

```bash
python3 scripts/frontier_alpha_s_universal_beta_kernel_2026_06_18.py --mode normal
python3 scripts/frontier_alpha_s_universal_beta_kernel_2026_06_18.py --mode independent
python3 scripts/frontier_alpha_s_universal_beta_kernel_2026_06_18.py --mode hostile
python3 scripts/frontier_alpha_s_universal_beta_kernel_2026_06_18.py --mode intentional-failure --fixture all
```

The default mode is `normal`. The cached output records that default run.

## 6. Direct-consumer boundary

The direct consumer
`ALPHA_S_4LOOP_RUNNING_DERIVATION_PARTIAL_NOTE_2026-05-10_4loop.md` may consume
the exact formal identities above only after keeping the QFT
coefficient templates and every physical interpretation explicit. This row
cannot be cited as authority for physical QCD coefficients, universality,
scheme independence, active-flavour selection, or physical running.
