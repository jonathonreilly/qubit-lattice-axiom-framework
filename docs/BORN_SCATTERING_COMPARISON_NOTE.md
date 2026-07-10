# Born/Eikonal Scattering Comparison — Gaussian Pole Theorem and Finite-Harness Negative Boundary

**Date:** 2026-04-08; 2026-07-10 exact-observable and Gaussian-integrability
revision.
**Claim type:** no_go
**Actual current-surface status:** bounded negative boundary with an exact
Gaussian pole subtheorem and a deterministic floating-point finite-harness
ray/adjoint discriminator; independent audit is required.
**Status authority:** independent audit lane only.
**Runner:**
[`scripts/gaussian_beam_eikonal.py`](../scripts/gaussian_beam_eikonal.py)
**Runner cache:**
[`logs/runner-cache/gaussian_beam_eikonal.txt`](../logs/runner-cache/gaussian_beam_eikonal.txt)
**Claim scope:** on the supplied Fam1 finite propagation harness at
`H=0.25`, historically empirical/tuned `beta=0.8`, Fam1 seed `0`, drift
`0.20`, restore `0.70`, physical half-width `6`, `k H=2.5`, source fraction
`1/3`, maximum connection distance `3`, field regularizer `0.1`, normalized
last-layer `z`-centroid detector, `b in {3,4,5,6}`, and
`T_phys in {7.5,15}`, neither the finite-path plane-ray function nor the
old 2D/3D Gaussian ray formulas provide a derivation of the literal
first-order detector-centroid response. The plane-ray function has a
discriminated path-length shape change, while the exact signed-adjoint
detector response has a stable four-point shape on the two supplied harnesses.
The Gaussian ray formulas, as written, cross a zero-impact pole and do not
define ordinary angular expectations. This is not a global no-go against
geometric optics, a core-regularized ray model, or a coherent 3D
amplitude/adjoint construction.

## Result

The old positive comparison does not close. The reason is now a derivation,
not an appeal to the numerical gap between two imported slopes.

There are two independent walls.

1. **Bounded wrong path-length shape.** The finite-path ray law has the exact scale
   form

   ```text
   I_ray(b; L, qL) = b^-1 F_q(b/L).
   ```

   Using the literal last-layer endpoints, its four-point slopes are
   `-1.561304` and `-1.279251`. The literal first-order detector-centroid response, recomputed
   as the exact signed-adjoint edge sum without ingesting a target exponent,
   has slopes `-1.4356` and `-1.433549`. Thus the ray shape changes by
   about `0.282`, while the literal response shape changes by about `0.002`.
   This is a deterministic floating-point finite-harness comparison, not an
   interval-certified exact inequality.

2. **The old Gaussian ray averages do not exist as ordinary expectations.**
   For every fitted `b`, the angular family contains a ray satisfying
   `b_eff = b - x_src tan(theta) = 0`. Near that ray,

   ```text
   I_ray(b_eff) = 2/b_eff + O(b_eff).
   ```

   Both the 2D Gaussian weight and the old 3D angular marginal are strictly
   positive at the pole. The left and right one-sided angular integrals
   therefore diverge with opposite signs. The historical code obtained finite
   values only by skipping `|b_eff| < 0.05`, which is an extra excision/core
   cutoff and not a derived Gaussian-beam expectation. A Cauchy principal
   value is a separate possible limiting prescription.

The prior claim that the plane value is scientifically preferred because its
slope is numerically closer to a separately supplied lattice value is
withdrawn. Numerical proximity between two different observables is not an
observable bridge.

## Minimal premises and forbidden imports

The runner uses the following supplied structure:

- the supplied finite directed propagation rule and its declared harness
  parameters;
- complex-linear forward propagation;
- the derivative of the supplied detector-centroid functional with respect to
  the weak source parameter;
- finite-dimensional adjoint differentiation, elementary calculus, and
  log-log regression.

### Complete supplied finite-harness inventory

| Input | Value / definition | Role |
|---|---|---|
| refinement | `H=0.25` | converts physical extents to layer/node counts |
| nominal durations | `T_phys={7.5,15}` | set `NL=round(T_phys/H)` |
| literal ray endpoints | `L_det=(NL-1)H={7.25,14.75}` | endpoint-matched plane-ray comparison |
| transverse half-width | `PW_PHYS=6` | finite node window and detector slice width |
| phase scale | `K_PER_H=kH=2.5`, hence `k=10` | free phase and source derivative |
| source layer | `SRC_LAYER_FRAC=1/3`, rounded to the lattice | gives `x_src={2.5,5}` |
| angular fixture | `beta=0.8` | historically empirical/tuned; weights the propagator |
| grown geometry | Fam1 seed `0`, drift `0.20`, restore `0.70`, `max_d_phys=3` | fixes the finite directed edge set |
| field/source | `1/(sqrt((x-x_src)^2+(z-b)^2)+0.1)` | supplied 2D denominator and core regularizer |
| impact window | `b={3,4,5,6}` | four-point log-log fit domain |
| detector | normalized intensity-weighted `z` centroid on layer `NL-1` | literal response functional |

These choices are premises of the bounded adjoint calculation. In particular,
`beta=0.8` is recorded as empirical/tuned in the directional-measure history;
the present runner holds it fixed and does not derive it.

The following are forbidden and are not supplied to the runner:

- the exponent `-1.43` as a target or fitted input;
- any within-packet retuning of the supplied `beta=0.8` fixture or finite
  window to improve agreement with a target constant;
- a Schrodinger, Klein-Gordon, Fermat, gravitational-lensing, or eikonal label
  used as an unproved semantic bridge;
- the centered finite-path surrogate used as the literal detector observable;
- an incoherent Gaussian ray mixture substituted for coherent complex
  propagation without derivation.

The four minimal framework axioms do not themselves supply a transfer
operator, source law, `beta`, packet geometry, or detector observable. This
note therefore establishes a reproducible bounded finite-harness negative
result. It does not claim a zero-input numerical prediction from those axioms.

`beta=0.8` is not derived here. The directional-measure history classifies it
as an empirical/tuned supplied value. It is load-bearing for the two literal
adjoint tables, while the Gaussian pole theorem needs only that the displayed
angular weights remain positive at the zero-impact ray. The runner does not
ingest the target exponent, but that does not make the supplied harness
first-principles.

## Derivation 1: the plane-ray law and its scale response

For a straight ray with transverse distance `b` from a source at `x_src`, the
finite-path transverse-gradient integral is

```text
I_ray(b; x_src, L)
  = integral_0^L b dx / ((x-x_src)^2+b^2)^(3/2)
  = (1/b) [
      x_src/sqrt(x_src^2+b^2)
      + (L-x_src)/sqrt((L-x_src)^2+b^2)
    ].
```

Set `x_src=qL` and `u=b/L`. Then

```text
I_ray(b; L, qL) = b^-1 F_q(u),

F_q(u) = q/sqrt(q^2+u^2)
       + (1-q)/sqrt((1-q)^2+u^2).
```

Each term in `F_q` has logarithmic `u`-derivative

```text
-u^2/(a^2+u^2),
```

strictly between `-1` and `0`. Hence the local log-slope of `I_ray` is
strictly between `-2` and `-1` at finite positive `u`; it approaches `-2` in
the short-path limit and `-1` in the long-path limit. The runner also checks
the exact covariance

```text
I_ray(rho b; rho x_src, rho L) = rho^-1 I_ray(b; x_src, L).
```

The path-length dependence is part of the candidate's theorem, not a numerical
artifact.

### Target-constant-free plane-ray computation

The DAG contains layers `0,...,NL-1`, so the literal ray endpoint is
`L_det=(NL-1)H`, not the nominal `T_phys`. The historical target formula used
the nominal convention `L=15`; the runner replays that value separately, then
uses the literal endpoints for the cross-harness discriminator.

| `T_phys` | `L_det` | `x_src` | values on `b={3,4,5,6}` | fitted slope | `R^2` |
|---:|---:|---:|---|---:|---:|
| `7.5` | `7.25` | `2.5` | `0.495224, 0.323728, 0.227193, 0.167553` | `-1.561304` | `0.999237` |
| `15` | `14.75` | `5` | `0.604424, 0.426509, 0.319385, 0.248640` | `-1.279251` | `0.999221` |
| historical nominal convention | `15` | `5` | `0.605106, 0.427336, 0.320307, 0.249613` | `-1.275288` | `0.999242` |

No detector-centroid values enter this calculation.

## Derivation 2: the Gaussian-ray pole obstruction

The historical 2D expression attempted to define

```text
G_2(b) = integral w_2(theta) I_ray(b-x_src tan(theta)) dtheta
         / integral w_2(theta) dtheta,

w_2(theta) = exp(-beta theta^2).
```

The historical 3D expression replaces `w_2` by a positive marginal

```text
w_3(theta_z) = integral exp[-beta(theta_y^2+theta_z^2)]
                       cos^2(sqrt(theta_y^2+theta_z^2)) dtheta_y.
```

For each declared `b` there is a pole inside the integrated angular chart at

```text
theta_0 = arctan(b/x_src),
b_eff(theta_0) = 0.
```

Because the source lies strictly inside the path,

```text
lim_(y -> 0) y I_ray(y; x_src,L) = 2.
```

Also

```text
db_eff/dtheta at theta_0 = -x_src sec^2(theta_0) != 0.
```

Thus each weighted integrand is a nonzero constant times
`1/(theta-theta_0)` plus a bounded term. Its two one-sided improper integrals
do not converge. The 3D factor cannot cure the pole because `w_3(theta_0)>0`:
its integration domain contains a neighborhood of `theta_y=0` on which the
integrand defining `w_3` is positive.

The runner makes the logarithmic divergence visible without relying on an
unstable uniform angular grid. For `b=3`, each shrinking decade surrounding
the pole carries the following absolute integral:

| shell in `|b_eff|` | absolute integral |
|---|---:|
| `0.01 .. 0.1` | `1.072283716050` |
| `0.001 .. 0.01` | `1.072252843496` |
| `0.0001 .. 0.001` | `1.072252534442` |
| analytic limiting mass per decade | `1.072252531320` |

Since infinitely many shrinking decades each carry the same nonzero absolute
mass, the absolute integral diverges logarithmically. A symmetric principal
value, a finite source core, diffraction, or another regularization may define
a new model. None is selected by a Gaussian angular weight alone.

Consequently the old quoted `-0.35` 2D and `-0.77` 3D slopes are withdrawn as
beam-correction predictions. They were outputs of an exposed numerical excision
rule, and the 3D angular factor did not resolve the mathematical wall.

## Derivation 3: the literal first-order detector observable

For the supplied coherent propagator, let `A_i` be the free forward amplitude,
`W_ij` the free edge transfer, and `lambda_j` the reverse detector-centroid
sensitivity. Differentiating the source phase and then the normalized detector
centroid gives

```text
alpha_adj(b)
  = 2 Re sum_(i->j) lambda_j A_i W_ij
      [-i k L_ij / (r_ij(b)+0.1)]
  = sum_e c_e / (r_e(b)+0.1),

c_e = 2 Re[lambda_j A_i W_ij (-i k L_ij)].
```

This is the exact signed-adjoint edge identity derived in
[`LENSING_ADJOINT_KERNEL_NOTE.md`](LENSING_ADJOINT_KERNEL_NOTE.md). The target
runner does not read that note's four response values. It rebuilds the directed
geometry, propagates `A`, backpropagates `lambda`, constructs every `c_e`, and
sums the field denominators for each `b`.

### Direct recomputation

| `T_phys` | edge terms | signed-adjoint values on `b={3,4,5,6}` | fitted slope | `R^2` |
|---:|---:|---|---:|---:|
| `7.5` | `31,245,797` | `2.455550, 1.668763, 1.211138, 0.903854` | `-1.4356` | `0.9985` |
| `15` | `65,528,627` | `5.986043, 3.819639, 2.826383, 2.211718` | `-1.433549` | `0.998404` |

The overall response changes strongly with path length, but its four-point
shape barely changes. The finite-path ray primitive predicts the opposite kind
of change on this window. This is a direct discriminator between the two
observables, not a fit of the ray model to the adjoint result.

## What the revision retires

- **Imported lattice exponent:** retired from the no-go proof. The target
  runner computes the literal finite-harness response before fitting its
  exponent.
- **Open dispersion label:** removed. No dispersion classification is needed
  for the finite-dimensional derivative or the ray-family existence theorem.
- **2D and 3D Gaussian beam corrections:** withdrawn as ordinary expectations;
  their zero-impact poles require an additional regularization premise.
- **The old proximity conclusion:** withdrawn as physics. The plane value at
  one path can be numerically near the adjoint value without identifying the
  observables.
- **Universal L-independence language:** not claimed. The runner establishes
  shape stability only on the two declared finite harnesses.

## What remains open

This packet does not derive an analytic closed form for the signed-adjoint
four-point exponent. It computes that exponent directly from the supplied
finite propagation law. The remaining positive problem is to reduce

```text
sum_e c_e/(r_e(b)+0.1)
```

to a controlled analytic `b`-law while preserving the signed, detector-adjoint
coefficients. A coherent 3D extension would likewise have to derive the
forward amplitude, source derivative, and detector adjoint in 3D; an
incoherent ray average is not a substitute.

The harness choices enumerated above remain supplied finite-model inputs rather
than consequences of the minimal framework axioms. For that reason this source
note does not use
`proposed_retained` wording for a zero-input numerical theorem.

## No-go discipline gate

**Disposition:** PASS for the declared ray/eikonal-to-detector-centroid bridge
on the two supplied finite harnesses.

- **Alternative routes:** plane finite-path ray (executed and discriminated);
  2D Gaussian rays (undefined without a new pole prescription); 3D Gaussian
  rays (same pole); centered surrogate (already ruled out); signed-adjoint
  finite response (executed); coherent 3D amplitude/adjoint route (open).
- **Independent walls:** plane path-length shape and Gaussian nonintegrability
  are independent. Removing the Gaussian pole does not repair the plane
  shape, and changing the path length does not define the Gaussian integral.
- **Hidden-input scan:** the target constant and observational target values
  are not ingested, and no within-packet retuning occurs. The historically
  tuned `beta=0.8` and every other supplied harness input are listed above.
- **Residual matching:** the no-go addresses only the claimed identification
  of these ray formulas with the literal detector centroid. It does not rule
  out geometric optics for a different observable.
- **Rhetoric audit:** `no_go` is restricted to the displayed model class and
  two finite harnesses.
- **Partial-closure path:** the exact signed-adjoint edge law is the valid
  current finite-harness route and is recomputed here.
- **Steelman:** a finite-core or principal-value ray model can be constructed,
  and a coherent geometric-optics limit might govern another readout. Either
  is a new theorem target, not a repair of the old unregularized comparison.
- **Cross-cycle consistency:** the conclusion agrees with the independently
  audited centered finite-path negative boundary in
  [`LENSING_FINITE_PATH_EXPLANATION_NOTE.md`](LENSING_FINITE_PATH_EXPLANATION_NOTE.md)
  within that note's scope. The related
  `LENSING_CENTROID_MULTIPOLE_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md` is
  context only because it attacks a different nonnegative `1/r` residual; it
  is not a load-bearing dependency here.

## Bottom line

> The plane finite-path formula is a legitimate ray surrogate, but it is not a
> derivation of the supplied detector-centroid response: its endpoint-matched
> four-point shape changes materially across the two paths, while a
> target-constant-free signed-adjoint recomputation gives a stable shape on the
> same two finite harnesses. The old 2D and 3D Gaussian ray formulas are even less complete:
> their zero-impact rays make the ordinary angular expectations divergent, and
> the historical finite slopes came from an added excision rule. The numerical
> proximity of the long-path plane slope to the adjoint slope therefore does
> not close an observable bridge. The positive residual preserved here
> is the signed-adjoint edge law itself, not another unregularized ray average.
