# Focused independent mathematical check of block 01

Checker: `/root/common_action_check`, 2026-10-15. This is a scoped research
check, not landing review, formal audit, empirical validation, or retained
status. Root remains the scientific author. No primary source was edited.

## Source identity and scope

Worktree HEAD and `origin/main` at the check were
`bbada1fe09b2d10d610560864d86b68c24a59713`; branch
`codex/observations-backward-derivation-20261015`.

The complete sources read were:

| Source in the parent pack | SHA-256 |
| --- | --- |
| `BLOCK01_DERIVATION_v1.md` | `266753576b127818bfed666d6cd773954106d0887db4170c2f6c69797609f86b` |
| `BLOCK01_DERIVATION_v3.md` | `c02f88316ff57d743c6c92d8de671c46136651118e98bcdc27ec53f01b9337fb` |
| `BLOCK01_DERIVATION_v4.md` | `8830c6bd57902e1cbbd6053c3ce4f9c477a8e9e54b50af32239edb1c00ede1d1` |
| `BLOCK01_DERIVATION_v5.md` | `5c2eb165f317192fbc6c8f3c548e442ce40d60d55915c363e57a4311d4d0f586` |

The source bytes of v1 and v3 are exact prefixes of v4. The v1 check therefore
covers unchanged sections 1–5 in v4; sections 6–7 were checked after the root's
explicit scope extension. The final v5 was read completely; its only difference
from v4 is the confirmed frequency-direction clarification described below.
The evidence script checks that exact sole replacement. The final source bound
by this report is v5. v2 was not used as evidence. No author's runner was
read, imported, or executed. The candidate formulas were necessarily known to
the checker, so this is a different derivation and implementation, not a blind
prediction or a different-model-family independence claim.

The supplied local instructions, repository `AGENTS.md`, cached planning
instructions at `origin/ai/execution` SHA
`3a4b2c66a1ead7a1c48b4359627e968f681e3c39`, current science workflow, and scoped
worker guidance were inspected. The science workflow in this checkout equals
the `origin/main` copy (SHA-256
`05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce`).
No workflow launch, network access, external application action, lock change,
commit, push, or audit operation was performed. Prior-art attribution was not
independently checked in this no-network scope.

## Findings

No material mathematical error or overstated inference was found in the
specified smooth, positive, material-vacuum chart. The local inverse, converse,
translation criterion on overlapping field ranges, explicit two-patch common
action, relative-field integral, deterministic input-error bound, and ideal
clock/radar/orbit map are consistent.

One presentation clarification was requested and is resolved in v5: for a
photon emitted at `r` and received at `r0`, the source now explicitly states
`R(r)=nu_received(r0)/nu_emitted(r)`. The mathematical definition `R=N/N(r0)`
already fixed this orientation correctly. I checked the final delta in this
same checker session; equations (12)–(15) and all other source bytes are
unchanged. No unresolved correction request remains within this check.

The qualifications below are essential to reuse, but the source already
substantially states them:

- Gluing on an open union is not a theorem of smooth extension through
  arbitrary excluded endpoints. Two generic smooth functions on disjoint open
  intervals need not admit a global smooth extension if their endpoint jets
  diverge. The explicit step-function example does admit the claimed extension.
- Separate choices of `C_i` are possible while the action functions are being
  reconstructed. They are not independent symmetries of an action that has
  already been fixed. The fixed-action normalization mutation below detects
  this distinction.
- Equation (15) is available only where the stipulated clock, radar and
  timelike circular-geodesic channels exist and the geometric/field chart
  hypotheses apply. Connectedness of a spacetime alone is insufficient to
  put separate source environments in one static, spherical, vacuum chart.
- The primitive orbit measurement can be independent of the clock channel,
  while the derived `v^2=r^2 Omega0^2/(c^2 R^2)` shares its `R` uncertainty.
  This does not make the consistency equation tautological, but its error
  analysis must keep that dependence.

## Independent variational derivation

Keep the sphere radius `A(r)` free before variation:

`ds^2=-N^2 dt^2+B^-1 dr^2+A^2 dOmega^2`.

Use the warped-product curvature identity

`R4=R2+2(1-B A'^2)/A^2-4 box2(A)/A`,

where `R2=-(2B N''+B'N')/N` and
`box2(A)=B A''+(B N'/N+B'/2)A'`.
For compactly supported variations, integration over the sphere and time
followed by integration by parts gives

```text
L = sqrt(B)[(A^2 F'+2 A F A')N' + N F A'^2 +2 N A F'A']
    +NF/sqrt(B) -N A^2 sqrt(B) Z(F)F'^2/2 -N A^2 V(F)/sqrt(B),
```

with the exact removed boundary expression
`-A^2 F sqrt(B)N'-2 N A F sqrt(B)A'`.
The runner verifies the total-derivative identity before taking any equations.

Writing `EL_q=partial L/partial q-d(partial L/partial q')/dr`, the mixed
equation residuals after `A=r` are

```text
E_t = -sqrt(B) EL_N/r^2,
E_r = 2B sqrt(B) EL_B/(N r^2),
E_a = -sqrt(B) EL_A/(2N r),
E_F = sqrt(B) EL_F/(N r^2).
```

All agree with the source's metric and scalar equations. Varying `A` before
fixing the areal gauge avoids losing the angular equation in a gauge-fixed
radial action. In particular,

`E_a-E_t=F a-dF'`.

The nonzero `d` condition therefore gives `F'/F=u=a/d`. Because `u` is smooth
and nonzero on a connected interval, it has fixed sign; `F=C exp(int u)` is
strictly monotone, and its inverse is smooth on its image. The reconstructed
action functions are consequently well-defined there.

There is also a direct check of the converse that does not use Bianchi as its
computational mechanism. Leave `u` arbitrary, define `omega=H/(B u^2)` and `W`
by the source formulas, and use the chain rule

```text
Z_F=(omega'-omega*u)/(u*F^2),
V_F=W+W'/u.
```

The scalar residual from the independently varied action simplifies exactly to

`E_F = 2(a-d*u)/(r*u)`.

Thus the angular relation makes the scalar equation vanish, while the time
and radial equations already vanish. This establishes the claimed converse
on the chart, with no endpoint continuation or constant-field case added.

## Independent exact-patch and common-action checks

Inserting the two specified actions and profiles into the reduced action,
varying it again, and then substituting the metrics gives zero time, radial,
angular and scalar residuals for both patches. Four changes at fixed remaining
data give these nonzero residuals:

| Changed input | Tested residual |
| --- | --- |
| Patch A: `omega=1/10` | `E_t=1/(40r)` |
| Patch A: `V=-1/F` | `E_t=-1/(2r)` |
| Patch A: `F=r^2` | `E_a-E_t=-1/2` |
| Patch B: `F=r^2`, retaining `V=-4` | `E_t=-3` |

An additional conformal check covers the entire `c>0` family. With
`b=1/(c+1)`, transform to the Einstein metric `gE=F g` and its areal radius
`rho=sqrt(C) r^((c+2)/2)`. Then

```text
N_E proportional to rho^(c/(c+2)),
B_E=(c+2)^2/[4(c+1)],
phi=sqrt(2c/(c+2))*log(rho)+constant,
U=V/F^2=-c/(2rho^2).
```

The canonical Einstein scalar satisfies all three independent Einstein
components and `box_E phi=U_phi` identically. In particular, the negative
Jordan potential does not obstruct this local solution. This check supplies
no global energy or nonlinear stability result.

For a common action, equality at equal `F` means
`x_2=x_1+log(C_1/C_2)`. Both `omega` and `V/F` must agree there, with no
extra independent vertical scaling of `V/F`. Equality on an open intersection
glues smooth functions on the open union. Constants in the normalization of
static time do not affect this test: only derivatives of `log N` enter, and
the relative clock ratio later removes that coordinate freedom explicitly.

For the explicit global example, `h(t)` is flat at both endpoints: near zero,
its numerator is flat and the denominator tends to a nonzero value; apply
the same argument to `1-h` near one. Hence the interpolated `omega,V` are
smooth for all `F>0` and match every derivative of both patch actions. Also
`0<=chi<=1` implies `2omega+3=3-chi>=2`. On the artificially equal-normalization
overlap, the kinetic discrepancy is exactly `1/2`, which cannot be repaired
by a potential adjustment. This verifies the limited existence witness and
the conditional overlap obstruction, not compatibility of arbitrary metrics
with one connected global source solution.

## Relative-field recovery and its deterministic bound

A separate integrating-factor form of the angular relation is

`(F N sqrt(B) r^2 y)'=F N/sqrt(B)`, with `y=1/r-N'/N`.

Dividing by the nonzero product and integrating yields equation (9), including
its single `-2 log(r/r0)` endpoint term. The symbolic check derives this form
directly and verifies that its derivative equals `a/d`. On the separated
domain, the right-hand side is a continuous functional of `N` in `C^1` and
`B` in `C^0`. That extension of the functional is not a claim that nonsmooth
inputs solve the original field equations.

For the error estimate, the two log-`N` endpoints contribute at most
`2eN/n0`; the half-weighted two log-`B` endpoints contribute `eB/b0`; the
two log-`|y|` endpoints contribute `2ey/y0`. The integrand difference obeys

```text
1/(Bhat*yhat)-1/(B*y)
 = (B-Bhat)/(Bhat*B*yhat) + (y-yhat)/(B*yhat*y),
```

so its magnitude is at most
`eB/(b0^2*y0)+ey/(b0*y0^2)`. Integrating `1/s^2` over the segment gives
`|1/r0-1/r|`, exactly as in equation (10). This is valid for either shared sign
of `y`; the chart must stay separated from zero. Finally,

`Nhat'/Nhat-N'/N=(Nhat'-N')/Nhat+N'(N-Nhat)/(Nhat*N)`

gives equation (11). These inequalities establish the general bound; the two
high-precision controls with positive and negative `y` are only diagnostic
examples, not its proof. In those controls, the actual log errors were
approximately `0.01119` and `0.19539`, below bounds `0.75600` and `1.45681`.

## Clock/radar/orbit map

For a static photon, the conserved Killing energy gives locally measured
frequency proportional to `1/N`. This yields the frequency-ratio orientation
stated in the clarification above. A radial null path gives

`c tau_roundtrip/2 = integral_[r0,r] ds/[R(s) sqrt(B(s))]`,

for an outward reflection, so `S=1/(R sqrt(B))` and equation (12) follows.

Independently varying the radial coordinate of the geodesic Lagrangian
`(-c^2 N^2 tdot^2+rdot^2/B+r^2 phidot^2)/2` and then taking a circular orbit
gives `(dphi/dt)^2=c^2 N N'/r`. Converting to the reference proper time
`tau0=N(r0)t` yields equation (13). Dividing by the local lapse yields
`v^2=rN'/N`. Timelike normalization requires `v^2<1`; stable circular motion
requires a further condition. Integrating `N'/N=v^2/r` gives equation (14).

Substitution of `y=(1-v^2)/r` and `B=1/(R^2 S^2)` into the endpoint and
integral factors separately yields equation (15). In particular,

`(N(r0)/N(r))*sqrt(B(r0)/B(r))=S(r)/S(r0)`.

The exponent of the stated power-law control agrees exactly. Omitting `R`
from the radar map changes the reconstructed `B`; perturbing the independently
supplied orbit channel with clocks held fixed violates equation (14). These
controls detect the relevant normalization and independence failures.

## Reproduction and exact remaining obligation

Run from the stated worktree:

```text
python3 .claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_block01/check_reduced_action.py
python3 .claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_block01/check_relative_map.py
```

Actual stdout is preserved in `run_stdout.txt` and `relative_map_stdout.txt`.
Structured evidence is in `computed_evidence.json` and
`relative_map_evidence.json`, including runner/source hashes and runtime
versions. The core run has 28 successful checks: 22 symbolic identities,
four action/profile mutations, one overlap obstruction, and one provenance
check. The final relative-map run has 27 successful checks: 15 symbolic identities,
three deliberate defective-map/endpoint controls, two synthetic bound examples,
and seven provenance checks. There were no failing checks or unrecorded failed
runs. These counts are synthetic implementation evidence, not independent
empirical tests or a measure of scientific completeness.

The decisive next obligation is to derive, from an actual measurement and
boundary/dynamical construction, a controlled relative normalization
`delta=log(C1/C2)` in one common field and length convention. The new map is a
candidate route only if an admissible connected domain transporting one field
normalization is established, or another calibrated local response supplies
the missing registration. Its observational use additionally needs bounds
from primitive clock, roundtrip-time, orbit and areal-radius data, preserving
shared-channel errors and the separation from `v^2=1`. Adding more synthetic
patches or declaring `C1=C2` does not discharge this obligation.
