# Finite Directed-Reversal Certificates — Exact Rational Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem
**Status:** proposed_retained exact structural theorem over explicitly defined
finite probability spaces; physical bridges remain open.
**Status authority:** independent audit lane only. This source note proposes a
narrow formal theorem and does not set or predict an audit verdict.
**Primary runner:**
[`scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py`](../scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_directed_certificate_examples_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_directed_certificate_examples_2026_06_06.txt)

## Claim scope

> **Theorem (finite rational reversal identities).** Let `W` be a finite set
> of finite words closed under reversal, and let `mu: W -> Q_{≥0}` have
> total mass one. Write `rho(w)` for reversal of a word and define the
> reversed law by
>
> ```text
> mu_rev(w) = mu(rho(w)).
> ```
>
> For every rational-valued statistic `f`,
>
> ```text
> E_mu_rev[f] = E_mu[f o rho].                              (1)
> ```
>
> Consequently, every reversal-invariant statistic has the same pushforward
> under `mu` and `mu_rev`. In particular, the complete vector of letter counts
> is reversal-invariant.
>
> For the three explicit rational laws below, direct enumeration gives:
>
> ```text
> signed-transition drift:   -1/2 forward,  1/2 reversed;
> marker lag:                  7/6 forward, 11/6 reversed;
> low-to-high boundary event:  1/2 forward,  1/6 reversed.
> ```
>
> In all three examples, the letter-count pushforward is unchanged by
> reversal while the displayed directed statistic changes.

This is a theorem about explicitly defined finite probability spaces. The
words `forward`, `reversed`, `marker`, and `boundary` are mathematical labels
inside those examples. They are not physical identifications.

## Definitions and exact examples

For a word `w=(w_0,...,w_{n-1})`, set

```text
rho(w) = (w_{n-1},...,w_0).
```

The reversed law is the pushforward `rho_* mu`. For each example, `W` is the
reversal closure of the displayed support and unlisted words have mass zero.
Since `rho` is a bijective involution, `mu_rev` is again normalized and
nonnegative.

### Example 1: signed transition drift

Take equal mass `1/4` on

```text
ABC, ACB, BAC, CBA.
```

Give directed edges `AB` and `BC` score `+1`, their reverses score `-1`,
and all other adjacent pairs score zero. Summing adjacent-edge scores gives
the exact forward distribution

```text
{-2: 1/4, -1: 1/2, 2: 1/4}
```

and the exact reversed distribution

```text
{-2: 1/4, 1: 1/2, 2: 1/4}.
```

Their expectations are `-1/2` and `1/2`, respectively.

### Example 2: marker lag

Take masses `1/2`, `1/3`, and `1/6` on

```text
AMBB, ABMC, MCAB.
```

Let marker lag be the zero-based index of `M`. The forward and reversed
distributions are

```text
forward:  {0: 1/6, 1: 1/2, 2: 1/3},
reversed: {1: 1/3, 2: 1/2, 3: 1/6},
```

with expectations `7/6` and `11/6`.

### Example 3: low-to-high boundary event

Take masses `1/2`, `1/6`, and `1/3` on

```text
LAH, HAL, LBA.
```

Let the statistic be one exactly when the first letter is `L` and the last is
`H`, and zero otherwise. Its expectation, equivalently its event
probability, is `1/2` forward and `1/6` after reversal.

## Proof

For any statistic `f`, use the bijection `u=rho(w)` and `rho^2=id`:

```text
E_mu_rev[f]
  = sum_w f(w) mu(rho(w))
  = sum_u f(rho(u)) mu(u)
  = E_mu[f o rho].
```

If `g o rho = g`, equation (1) gives equality of every point mass in the
pushforward distribution of `g`. Letter counts are unchanged by reversing a
word, so their pushforward is equal. The three displayed values then follow
from the finite Fraction enumerations written above and reproduced by the
runner. No limiting, floating-point, or fitted step enters the proof.

## Load-bearing boundary

The load-bearing inputs are only the displayed rational masses, word lists,
reversal map, and statistics. They are definitions of finite mathematical
objects, not framework premises or physical data.

This theorem does **not** derive or identify:

- a physical orientation or arrow;
- a clock, rate, Hamiltonian, transfer operator, instrument, or production
  kernel;
- a physical probability law from Record or any other framework axiom;
- a map from the example words or letters to physical records;
- a selected dial, target vector, observable, or unbounded dynamics law.

Any physical claim using this theorem requires separately supported bridge
inputs; this theorem supplies none. No repository-row census enters the
theorem or runner.

## Verification

The runner uses exact `fractions.Fraction` arithmetic and has four modes:

```bash
python3 scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py --mode normal
python3 scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py --mode independent
python3 scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py --mode hostile
python3 scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py --mode intentional-failure --mutation all
```

Normal mode reconstructs the theorem and all three examples. Independent mode
re-enters the fixtures through a separate direct-summation implementation.
Hostile mode rejects malformed or floating-point probability laws,
floating-point or wrong certificate values, scope mismatches, and missing
orientation labels. Intentional-failure mode
offers five selectable mutations; the aggregate and every individual mutation
must exit nonzero.

The runner also checks source shape: the formal scope and open physical
bridges must be stated, and physical-selection overclaims are forbidden. Those
guards police the claim boundary; the positive theorem itself is established
by exact enumeration and the displayed change-of-variable proof.

## Independent audit handoff

```yaml
proposed_claim_type: positive_theorem
proposed_claim_scope: |
  For each of three explicitly defined finite rational laws, word reversal
  preserves the complete letter-count pushforward and gives the exact stated
  directed-statistic expectations. More generally,
  E_{rho_*mu}[f] = E_mu[f o rho] on every finite rational word law.
  No physical orientation, clock, kernel, Record bridge, or dynamics law is
  derived or identified.
proposed_load_bearing_step_class: A
declared_one_hop_deps: []
status_authority: independent audit lane only
```
