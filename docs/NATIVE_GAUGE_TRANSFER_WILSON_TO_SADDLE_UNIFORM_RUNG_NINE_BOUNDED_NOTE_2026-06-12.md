# Native Gauge Transfer Wilson-To-Saddle Uniform Obstruction Note

**Date:** 2026-06-12
**Claim type:** open_gate
**Type:** source-side obstruction note

**Claim boundary:** this note attempts the requested Route B value-side
Wilson-to-saddle uniform estimate for the exact repo-native `SU(3)` Wilson
character coefficient diagonal. It does not derive the missing uniform
constant. Honest outcome: obstruction-at-exact-step. The exact resisting term
is the absent uniform large-argument Bessel/determinant remainder for
determinant indices and summation modes of size `O(sqrt(beta))`. No
continuum, Clay, physical `beta = 6`, or audit-status claim is made.

Status authority: independent audit lane only. This source note does not set or predict an audit outcome.

Primary runner:
[native_gauge_transfer_wilson_to_saddle_uniform_rung_nine_bounded_2026_06_12.py](../scripts/native_gauge_transfer_wilson_to_saddle_uniform_rung_nine_bounded_2026_06_12.py)

Runner cache:
[native_gauge_transfer_wilson_to_saddle_uniform_rung_nine_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_wilson_to_saddle_uniform_rung_nine_bounded_2026_06_12.txt)

No new axiom, literature value, external comparator, fitted selector, fitted
constant, rounded anchor, proxy substitution, or target-fed value is used.
The runner witnesses finite rows and falsifiers; it does not use those rows
as proof of `K_W`.

## One-Hop Authorities

- [NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md)
  supplies the operator-remainder target, the leading saddle profile, the
  already-derived geometric piece, and the perturbation-transfer arithmetic.
  Quote anchor:

```text
wilson_to_saddle_uniform(a):
| beta^(-3/2) r_(p,q)(beta)
  - beta^(-3/2) d_(p,q) exp[-3 C2(p,q)/beta] |
 <= K_W(a) beta^(-1/2)
```

  Quote anchor:

```text
K_diag(a) = K_W(a) + K_geom(a).
```

  Quote anchor:

```text
K_geom(a) = 6 a^4 + 3 a^2 + 3 a + 1.
```

  Quote anchor:

```text
beta^(-3/2) r_(p,q)(beta)
    -> H(x,y) exp[-Q(x,y)],
H(x,y) = x y (x+y) / 2,
Q(x,y) = x^2 + x y + y^2.
```

  Quote anchor for the later perturbation arithmetic:

```text
If a later operator estimate supplies

epsilon(beta) <= K / sqrt(beta),
```

- [GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)
  supplies the source-character recurrence. Quote anchor:

```text
X = (chi_(1,0) + chi_(0,1)) / 6
```

  Quote anchor:

```text
X chi_(p,q)
 = (1/6) [ chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1)
         + chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q) ]
```

- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  supplies the repo-internal Wilson Bessel-determinant coefficient convention.
  Quote anchor:

```text
a_(p,q)(beta) = sum_(n in Z) det[I_(n + lambda_j + i - j)(beta/3)]_(i,j=1)^3
```

Implementation pointer, not an additional source authority:
[frontier_su3_wilson_closed_form_fanout_2026_05_04.py](../scripts/frontier_su3_wilson_closed_form_fanout_2026_05_04.py).

## Target Object

Let `t = beta/3`, `lambda = (p+q, q, 0)`, and

```text
c_(p,q)(beta)
  = sum_(n in Z) det[I_(n + lambda_j + i - j)(t)]_(i,j=1..3),
r_(p,q)(beta) = c_(p,q)(beta) / c_(0,0)(beta).
```

The requested value-side estimate is:

```text
| beta^(-3/2) r_(p,q)(beta)
  - beta^(-3/2) d_(p,q) exp[-3 C2(p,q)/beta] |
 <= K_W(a) beta^(-1/2)
```

uniformly on the active window `0 <= p,q <= a sqrt(beta)`. If a future
source note derives this estimate, rung eight already gives the next path it
opens:

```text
K_diag(a) follows by adding the Wilson piece to
K_geom(a) = 6 a^4 + 3 a^2 + 3 a + 1.
```

No source-side value of K_W(a) is derived in this note.

## Attempted Expansion

The determinant entry index is

```text
k = n + lambda_j + i - j.
```

On the active window, `lambda_j = O(sqrt(beta))`. The determinant sum also has
load-bearing modes `n = O(sqrt(beta))` after the Gaussian factor in the Bessel
kernel is exposed. Thus the entry-level expansion needed for the determinant
is a uniform expansion in the regime

```text
k = O(sqrt(beta)),   t = beta/3.
```

Both readings of the Bessel-asymptotic instruction are:

1. **Fixed-index reading.** Use the displayed fixed-order next term
   `I_k(t) ~ exp(t) / sqrt(2 pi t) * (1 - (4 k^2 - 1)/(8t) + ...)`.
   This reading fails as a uniform active-window proof input. If
   `k = 2 sqrt(t)`, then the displayed next factor is
   `-1 + 1/(8t)`, negative for `t > 1/8`, while `I_k(t)` is positive.
   The correction is order one, not a `1/t` remainder.

2. **Uniform local-CLT reading.** Replace the fixed-index series by a true
   uniform expansion of the form
   `exp(-t) I_k(t) = (2 pi t)^(-1/2) exp[-k^2/(2t)]
   (1 + P_1(k/sqrt(t))/t + R_2(k,t))`, with an explicit bound on `R_2`
   for all determinant indices and with a summable tail for the mode `n`.
   This is the correct type of input for the active window, but that
   uniform remainder is not supplied by the retained material used here.

The exact obstruction is therefore not the leading saddle shape. Rung six
already identifies that shape numerically and structurally. The obstruction is
the next load-bearing step:

```text
uniformly bound the determinant sum after substituting a Bessel expansion
valid for k = O(sqrt(beta)), including the determinant cofactor cancellations
and the c_(0,0) normalization.
```

Without that bound, deriving `K_W` would require importing a uniform Bessel
remainder or fitting a constant from grid residuals. Both are outside this
source note's allowed inputs.

## Runner Witnesses

The runner recomputes the exact coefficient ratio by the Bessel determinant
using scaled `I_k` entries, so the common exponential factor cancels in
`c_(p,q)/c_(0,0)`.

Fixed-index obstruction witness:

| row | value |
|---|---:|
| `z = 100`, `nu = 20`, normalized actual `exp(-z) I_nu(z) sqrt(2 pi z)` | `0.135056069303` |
| fixed-index next factor `1 - (4 nu^2 - 1)/(8z)` | `-0.998750000000` |
| Gaussian local factor `exp[-nu^2/(2z)]` | `0.135335283237` |

Leading saddle witness rows, not a proof of a uniform constant:

| beta | `(p,q)` | exact `r_(p,q)` | saddle `d exp[-3 C2/beta]` | relative difference |
|---:|---:|---:|---:|---:|
| `48` | `(4,3)` | `25.894978539180` | `26.882522035981` | `-3.673552e-02` |
| `96` | `(6,5)` | `73.579022615880` | `75.023779892741` | `-1.925732e-02` |
| `192` | `(10,8)` | `207.380571748836` | `209.688188327461` | `-1.100499e-02` |

Active-grid witness rows, again not proof inputs:

| beta | cap `floor(1.25 sqrt(beta))` | max `sqrt(beta)` scaled exact-to-saddle diagonal difference | max `sqrt(beta)` scaled exact-to-`H exp[-Q]` profile difference |
|---:|---:|---:|---:|
| `48` | `8` | `2.710006e-02` | `2.103009e-01` |
| `96` | `12` | `1.907302e-02` | `2.095674e-01` |

Falsifiers at `beta = 96`, `(p,q) = (6,5)`, all displayed as
`beta^(-3/2)` scaled values:

| substitution | value |
|---|---:|
| correct exact determinant ratio | `0.078225286971` |
| correct saddle `d exp[-3 C2/beta]` | `0.079761275743` |
| wrong `N_c = 2` saddle constant | `0.122681758828` |
| wrong `N_c = 4` saddle constant | `0.051856618041` |
| wrong dimension, missing A2 factor | `0.012270965499` |
| wrong Bessel highest-weight index `lambda = (p,q,0)` | `0.030362625798` |

These falsifiers make the normalization sensitive in the real object. They do
not supply `K_W`.

## Outcome

Honest outcome: obstruction-at-exact-step.

What is new here versus the existing operator-remainder rung-eight note:

- rung eight restated the leading saddle profile;
- rung eight gave the geometric `K_geom(a)` piece and named `K_W`;
- this note isolates why the fixed-index Bessel next term cannot be used as
  the active-window uniform proof, and names the exact uniform remainder
  object needed before a source-side `K_W` can be written.

What is restated:

- the target `wilson_to_saddle_uniform(a)` estimate;
- the already-proven `K_geom(a)`;
- the exact Bessel-determinant coefficient convention.

The Route B value side is therefore still missing the uniform
Wilson-to-saddle determinant remainder. The next path this opens is a focused
uniform Bessel/local-CLT determinant expansion with explicit remainder and
mode-tail constants, followed by determinant-sum and `c_(0,0)` normalization
bounds.

## No-Go Discipline Gate

Skill freshness: the repo-native no-go discipline instructions were read
before review. This gate records a partial obstruction with named residuals
only.

N1 - Alternative route enumeration:

1. Fixed-index Bessel next term. ATTEMPTED. It fails for the active-window
   proof because the entry index has `k = O(sqrt(beta))`; the runner's
   `z=100, nu=20` row makes the displayed next factor negative while the
   Bessel entry is positive.
2. Uniform local-CLT Bessel expansion. ATTEMPTED. This is the appropriate
   analytic shape, but the retained authorities above do not supply the
   explicit `R_2(k,t)` bound and mode-tail constants needed to insert it into
   the determinant sum.
3. Determinant-level cofactor expansion. ATTEMPTED. The leading saddle is
   witnessed and matches the profile restated by the rung-eight note, but the
   next determinant remainder still depends on the missing uniform entry-level
   bound and on bounding the determinant cancellations after summing over `n`.
4. Recurrence/random-walk route from the six-neighbor character graph.
   ATTEMPTED. The recurrence authority supplies the exact graph operator, but
   not an Edgeworth/local-CLT theorem with constants for the growing
   `sqrt(beta)` dominant-weight window.
5. Numerical residual grid. ATTEMPTED as witness only. It is rejected as a
   proof path because a fitted constant would violate the no-fit and
   anti-fabrication rules.
6. True-tail consequence from rung eight. ATTEMPTED. The saddle tail is
   available there, but the true Wilson tail still depends on this same
   Wilson-to-saddle uniform estimate or on a separate true-tail proof.

N2 - Wall-independence audit:

| wall | relation |
|---|---|
| `W1`: uniform Bessel/local-CLT entry remainder with explicit constants | needed before the determinant expansion can be made load-bearing |
| `W2`: determinant-sum cofactor and `c_(0,0)` normalization bound | depends on `W1`, but closing `W1` alone would still leave determinant algebra to check |
| `W3`: true-tail consequence | downstream of `K_W` plus the rung-eight saddle-tail estimate, or replaceable by a separate true-tail proof |

The current note ships the narrow obstruction at `W1`, with `W2` named as the
next algebraic step rather than an independent completed wall. `W3` is not
counted as a separate current obstruction for deriving `K_W`.

N3 - Hidden-wall scan:

The phrases "active window", "saddle diagonal", "true Wilson", and
"Bessel-determinant" are load-bearing and are tied to the one-hop authorities
quoted above. The note avoids using "standard", "obvious", "by construction",
or similar phrases as proof steps. "Runner witnesses" are explicitly labeled
as non-proof numerical checks.

N4 - Residual matching:

| citation | residual named there | residual here | match |
|---|---|---|---|
| operator-remainder rung-eight note | `wilson_to_saddle_uniform(a)` and the leading saddle profile | exact same target estimate; profile context only | yes for the target; the profile is not used as a completed Wilson-bound witness |
| character-recurrence note | exact recurrence for `J` | recurrence route input | not a residual witness |

N5 - Rhetoric audit:

The negative statement is scoped to this source note and this attempted
derivation path: `K_W` is not derived here under the no-import rules. It is
not a statement that a uniform Bessel/local-CLT proof cannot be supplied by a
future source note.

N6 - Partial-closure path scan:

This obstruction does not require a new axiom. Plausible closure paths remain:
a uniform Bessel/local-CLT determinant expansion from the exact coefficient
formula, a recurrence-based local-CLT expansion with explicit constants, or a
separate true-tail estimate if the value-side active-window proof is pursued
in pieces. No convention reframe closes the analytic remainder by itself.

N7 - Steelman:

A hostile reviewer could push the exact Bessel determinant harder: start from
the same repo coefficient formula, apply a uniform contour/Laplace expansion
for `exp(-t) I_k(t)` with `k = O(sqrt(t))`, keep the polynomial correction in
`k/sqrt(t)`, then sum over the determinant mode `n` by Poisson or Gaussian
tail bounds. The rung-eight profile context already points at the leading
saddle as the right object, so such a proof could plausibly produce the
missing `K_W` without changing the operator. This is why the current note is
a partial obstruction record, not a broader impossibility claim.

N8 - Cross-cycle echo:

Repo search found the same named wall in rung eight and many finite-packet or
fixed-beta Bessel certificates elsewhere. Those finite certificates do not
match the growing `sqrt(beta)` active-window residual. The relevant echo is
therefore rung eight's exact `wilson_to_saddle_uniform(a)` wall, sharpened
here to the uniform Bessel/determinant remainder term.

## Verification

Run:

```bash
python3 scripts/native_gauge_transfer_wilson_to_saddle_uniform_rung_nine_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=12, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/native_gauge_transfer_wilson_to_saddle_uniform_rung_nine_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
