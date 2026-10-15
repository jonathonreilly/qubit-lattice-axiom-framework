# Focused independent check of block 02 and the separate intake probe

Checker: `/root/common_action_check`, 2026-10-15. Root remains the author.
This is a bounded research check, not landing review, formal audit, empirical
validation, or a source of retained status. Writes were confined to this
`independent_block02` directory. No author's block-02 runner was read or used.
No lock, git, network, PR, or audit action was performed.

## Exact source and final disposition

| Source in the parent pack | SHA-256 |
| --- | --- |
| `BLOCK02_DERIVATION_v1.md` | `2b65e7cc57f06b145792ab4623dd78d78e9b86f747a2bb5b927cff9295e8f448` |
| **Final checked source: `BLOCK02_DERIVATION_v2.md`** | `6af03812dccdf6c77322b20591f5cc72300c84e304f7fff56bf680af7e066c1e` |
| Checked dependency `BLOCK01_DERIVATION_v5.md` | `5c2eb165f317192fbc6c8f3c548e442ce40d60d55915c363e57a4311d4d0f586` |
| Separate probe `BLOCK01_READOUT_INTAKE_v1.md` | `6d8dc4094320a13731ee1366cf5343076f82b7c106fded48496807fd6d933e33` |

Block-02 v1, v2 and the intake probe were read completely. Block-01 v5 was
already read and independently checked in this same checker session; its
unchanged hash is verified here. No current Git SHA was queried because the
current dispatch excludes Git actions. Source hashes above identify the exact
bytes checked rather than implying an unqueried branch or commit state.

No material mathematical error or unsupported physical inference was found
within the stated hypotheses. One wording qualification was requested:
an increasing smooth relabeling may have a zero derivative, which exits the
`q,P>0` chart. V2 now requires a strictly positive derivative throughout.
I read v2 completely and confirmed that this is its sole change from v1;
the runner verifies the exact replacement. No correction request remains
unresolved within this scope.

The tested bounds apply to aligned functions with certified value and
derivative errors. They do not create such certificates from finite samples,
provide a statistical confidence level, or determine cross-environment field
normalization. The explicit finite-sample ambiguity establishes a limitation
of the unrestricted observation-function class. It is not a collection of
healthy solutions of one scalar action or a physical no-go. Those limitations
are stated in the source and are necessary to its valid interpretation.

## Shared-label inverse and primitive bound

From the checked block-01 formula, the endpoint factor is

```text
(S/S0)(r0/r)(A0/A)
 = (P/P0)(q0/q)(r0/r)(D0/D)(R/R0)^2,
```

and the integral density transforms as

`R^2 S^2 dr/(r A)=R^4 P^2 dz/(q r D)`.

These independently give the stated `E` and `J`. Under a shared reparametrization
`z=f(t)` with `f'>0`, both `P` and `q` acquire a factor `f'`. Their endpoint
quotient is unchanged and the new integral density is `f' J(f(t))`, as required.
The missing-Jacobian mutation fails this test. Relabeling the channels separately
does not have this cancellation.

I checked the deterministic estimate by exact finite differences rather than
using the source's gradient-bound implementation. First,

```text
Dhat-D = Rhat^2-R^2
 -[(rhat^2-r^2) Omegahat^2+r^2(Omegahat^2-Omega^2)]/c^2.
```

The difference-of-squares bounds give precisely equation (2). No stochastic
independence is used, and a change in the same measured `R` necessarily changes
`D` as well.

For the integral, write `J=R^4 P^2/(q r D)`. Its exact difference is

```text
Jhat-J = (Rhat^4-R^4) Phat^2/(qhat rhat Dhat)
       + R^4(Phat^2-P^2)/(qhat rhat Dhat)
       + R^4 P^2(1/qhat-1/q)/(rhat Dhat)
       + R^4 P^2(1/rhat-1/r)/(q Dhat)
       + R^4 P^2(1/Dhat-1/D)/(q r).
```

Use `|Rhat^4-R^4|<=4(R^*)^3 e_R`,
`|Phat^2-P^2|<=2P^* e_P`, and
`|1/xhat-1/x|<=e_x/x_*^2`. Bounding the remaining factors gives exactly all
five displayed `K` coefficients. Applying the positive-domain log bound to
both endpoints gives `2e_P/P_*`, `2e_q/q_*`, `2e_r/r_*`, `2e_D/D_*` and
`4e_R/R_*`. Integrating the uniform bound on `Jhat-J` proves equation (3).
This proof uses only the values of the supplied correlated data; it neither
replaces `D` by an independent measurement nor needs the intermediate tuples
to satisfy physical equations.

Three deterministic numeric controls were run with envelopes established
analytically, not estimated from a finite grid:

| Control | Actual absolute log error | Valid bound | Deliberately invalid bound |
| --- | ---: | ---: | ---: |
| Joint radius, clock, orbit, radar-derivative and label-derivative changes | 0.0163778844 | 0.5058798192 | — |
| Clock error near small positive `D`, retained consistently in `D` | 48.81774639 | 361.31922433 | 0.59157436 if the clock contribution to `e_D` is dropped |
| Radius offset with other channels fixed | 0.0480010240 | 0.2 | 0 if radius error is dropped |

For the joint control on `0<=z<=1`, the baseline is

```text
r=2+z, q=1, P=1+z/5,
R=(r/2)^(1/4), Omega=R/(2r), c=1.
```

The hatted channels are `rhat=r+z/100`, `qhat=1.01`,
`Phat=P+z/50`, `Rhat=R(1+z/200)`, and
`Omegahat=Omega(1-z/250)`. Monotonicity and elementary bounds supply
`r_*=2`, `R_*=q_*=P_*=1`, `D_*=0.43`,
`r^*=3.01`, `R^*=1.12`, `O^*=0.25`, `P^*=1.22`.
In particular,

```text
(3/2)(201/200)^4 < (28/25)^4,
1-(301/100)^2(1/4)^2 > 43/100,
```

certify the nontrivial `R` and `D` envelopes exactly. The channel errors used
are `(e_r,e_R,e_O,e_P,e_q)=(0.01,0.0056,0.001,0.02,0.01)`.

For the shared-clock control, the baseline metric is `N=r^p`, `B=r^(-2p)`,
with `p=0.999`, `r=1+z`, `0<=z<=0.1`, and `P=q=1`.
Thus `R=r^p`, `Omega=sqrt(p)R/r`, and `D=(1-p)R^2`.
Only the hatted clock channel is multiplied by `1+0.01z`. The lower bound
`D_*=1-p` is analytic; the radius, clock and orbit extrema follow by
monotonicity. The noisy hatted channels need not themselves obey exact geodesic
consistency. This is a synthetic conditioning example, not an observed source
or a demonstrated healthy scalar-action solution.

For the radius control, take `r=2+z`, `rhat=2.1+z`, `P=2`, `q=R=1`,
`Omega=0`, and `0<=z<=1`. The exact functional is
`L=3 log(r/r0)`, which gives the displayed nonzero radius sensitivity.

## Finite radar bins and the explicit ambiguity

An independent proof of equation (4) comes from completing the square. Let
`delta=integral S dr` and `H=integral (1/w) dr`. Then

`I-delta^2/H = integral w [S-delta/(H w)]^2 dr >= 0`.

This proves the lower bound and shows that equality requires
`S=delta/(H w)` almost everywhere; for smooth functions it holds everywhere.
The exact refinement gain is the stated nonnegative
`(k*x-h*y)^2/[h*k*(h+k)]`. If only `delta>=delta^-` and `H<=H^+` are known,
monotonicity of the quotient gives the source's clamped uncertain-data bound.
No endpoint value of `S` follows from this argument.

For `w=1/r` on `[1,2]`, the equality family `S=k r` was checked exactly.
For `S=1`, the strict gap is `log 2-2/3>0`; the completed-square integrand is
nonzero. Refining at `r=3/2` raises the lower bound from `2/3` to `24/35`,
an exact increase of `2/105`. The source correctly keeps the separate endpoint
slowness and orbit factors in the formula for `F(b)/F(a)`.

The baseline needed for the bump witness exists for every stated `0<A<b-a`:
choose a compactly supported smooth function `0<=f<=1` with
`integral f>A`, and set `S0=1-(A/integral f)f`. Then `S0>0`, it equals one
near the endpoints, and its area is `(b-a)-A`.

For a concrete independent realization on `[1,2]`, use

```text
phi(t)=exp[-1/(1-4t^2)] for |t|<1/2, and zero otherwise,
Z=integral phi, psi(t)=2*phi(2t)/Z,
f(r)=e*phi((r-3/2)/(4/5)), A=1/4,
S0=1-[A/integral f]f.
```

The support of `psi` is `[-1/4,1/4]`, strictly inside the source's open
`(-1/2,1/2)`. Flatness of the exponential at the support boundary gives smoothness.
Also `integral f>4/15>A`: on `|t|<=1/4`,
`e*phi(t)>=exp(-1/3)>2/3`. Hence the baseline coefficient is below `15/16`
and `S0>1/16` throughout. The bound `exp(-1/3)>2/3` follows, for example,
from the power-series inequality `exp(x)<1/(1-x)` at `x=1/3`.

Changing variables inside the added bump gives its area exactly `A`. Thus
every gap increment remains one and endpoint slownesses remain one. Because
all added terms are nonnegative,

`integral w S_epsilon^2 >= (w_* A^2/epsilon) integral psi^2`.

The positive squared bump integral proves divergence as `epsilon` tends to
zero, without a numerical limit argument. The check evaluates the integral
in rescaled bump coordinates so no narrow spike is missed by a fixed grid.
Six scales from `epsilon=1/4` through `1/128` were evaluated, while gap
increments and endpoint slownesses agree. Their values are preserved in the
evidence; the divergence claim follows from the analytic bound, not those
finite numerical examples.

Holding `R` and the orbit channel fixed keeps `w` fixed. The constructed curves
are positive kinematic data and can define positive static radial metric
coefficients, but the argument does not check the nonzero-`u` chart, kinetic
sign, one common action, source completion, or actual apparatus bandwidth.
Its force is precisely the finite-sample limitation the source states.

## Separate static coherent-transfer probe

Only the self-contained ideal calculation and metric witness in
`BLOCK01_READOUT_INTAKE_v1.md` were checked. Its Moyer citation, prior-note
provenance, metadata, and empirical implications were not independently verified;
network access was outside this dispatch.

For static endpoints, local photon frequency scales as inverse lapse. Therefore
the outward transfer divides by `R`, an immediate coherent turnaround multiplies
by `k`, and the inward transfer multiplies by `R`. The carrier returns with
frequency `k nu_emit`, independent of the remote lapse. A time-dependent
emission phase or endpoint motion can still encode delay and dynamics; those
effects are not excluded by the static cancellation.

For `N=r^p`, `B=r^(-2p)`, `r0=1`, and `0<p<1`, direct substitution gives
`S=1`, `rho=r-1`, `R=r^p`, and circular local speed squared `p`.
Different choices of `p` therefore share the stipulated radar/coherent-carrier
functions while having different clock ratios. This proves the stated limited
metric-level ambiguity, with no same-healthy-action or real-data exclusion.

## Reproduction, failures, and next obligation

Run:

```text
python3 .claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_block02/check_block02.py
```

`computed_evidence.json` and `run_stdout.txt` preserve the final computation,
including source/runner hashes and runtime versions. The original run and its
exact runner bytes are retained as `run01_evidence.json`, `run01_stdout.txt`,
and `run01_checker.py`; the second run is likewise preserved under `run02_*`.
The second run changed only provenance coverage and one evidence-category
label. A final run rescaled the test bump to put its closed support strictly
inside the specified open interval; this checker-side domain correction is
recorded in `SESSION_FAILURES.md`.
The final run has 42 successful checks: 16 symbolic identities, six exact
inequalities, four defect controls, ten synthetic numeric controls, one
metric nonuniqueness witness, and five provenance checks. These are mathematical
and software controls, not independent empirical observations. The two
command-path failures are explicitly recorded in `SESSION_FAILURES.md`, with
the final-launch error output preserved separately.
There were no mathematical check failures.

The next physical obligation is unchanged: derive a normalization transport or
calibrated relative-field readout that determines `log(C1/C2)` across the
proposed environments. A material-stress equation and a justified connected
field solution are plausible next subjects, but this block does not establish
that regularity fixes their homogeneous integration constants. Applying these
bounds to observations additionally requires actual derivative/shape and
alignment certificates, or a justified finite-bin strategy with the endpoint
factors retained.
