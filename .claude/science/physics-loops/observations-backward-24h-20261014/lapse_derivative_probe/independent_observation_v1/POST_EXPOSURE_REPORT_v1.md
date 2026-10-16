# Focused comparison of the proposed M17 extension

Disposition: **support appending this coherent extension to the existing M17 PR 9614**. No separate PR is recommended. This is a source/measurement-scope judgment, not a formal audit, complete numerical review, landing approval or statement that the synthetic geometry is physically realized.

Root remains author. The complete `WORKING_v2.md`, SHA-256 `92d5f254b652c176fa3ee668ccc2c55ad84ed9c0700ca0345dbdb8ff2faba7f8`, was read only after `INDEPENDENT_FREEZE_v1.json` fixed this reviewer's independent conclusions. All original frozen files remain unchanged. The M17 premise note remains the previously reviewed commit source `9a19c88e254a4d0eed3d4f4ed76ffa5e0082b6db`.

## Derivative reduction and physical input correspondence

The displayed change of variable genuinely cancels the standalone lapse-Laplacian term within the stated power family. With `ell=ln N`, direct product differentiation gives coefficients `p-lambda` for `Delta_h ell` and `p(p+1)-lambda` for the squared lapse gradient. Setting `p=lambda` leaves

```text
C = lambda R3/2 + lambda^2 |grad_h ell|^2,
L_(N^(2lambda+1)) w + Cw = S/N^lambda.
```

This agrees with the independent curvature decomposition. It is not an assumed identification of `R3` with `R4`, and it does not require a new physical law. The exponent is fixed within that family; the draft does not claim uniqueness among all conceivable transformations.

The global minimum `m=min_closure N` is essential: `w>zB/m^lambda` implies `z=N^lambda w>zB>=1` throughout the domain, so the inherited source sign applies. A boundary-only lapse minimum would not suffice. The draft correctly retains the global minimum, the full static scalar premise, regularity, positive chart and every boundary component. Constant coordinate-clock normalization cancels from the bound; physical clock/radius calibration remains.

Its spherical input formula is consistent with the blind derivation:

```text
B=4/(f^2 g^2),
C=lambda[2B(f'/f+g'/g)/r+(1-B)/r^2]
  +lambda^2 B(f'/f)^2.
```

The input therefore has no explicit `f''`, but still contains `g'=tau''` and first lapse slopes. The draft explicitly says so, preserves `C3` lapse/metric regularity, and declines to infer derivative errors from discrete samples. It also retains independently calibrated areal radius, the ideal static outward-vacuum measurement model, whole-domain coverage and the inner boundary of an annulus. These are consistent with the frozen primary-source findings.

The additional qualification root has proposed should be retained in the canonical extension: removal of a standalone lapse-Laplacian input does not remove spatial-curvature/combined-center error suppliers, and finite data may need higher regularity to estimate even first slopes. In particular the regular-ball formula needs a certified limit for `(1-B)/r^2` and `B'/r`. The current draft already refers to regular central limits and actual regularity; the explicit sentence prevents “first-clock-derivative” from being read as a universal observational derivative-order claim. Final canonical source confirmation must bind that eventual wording. No actual measurement has discharged these conditions.

## Strict synthetic usefulness claim

The supplied family is a valid smooth kinematic test of two comparison criteria. For `B=1` and `ell=epsilon[cos(Kr)-1]/K`, the lapse is smooth as a radial function on the ball because its expansion contains only even powers. `ell'=-epsilon sin(Kr)` is bounded uniformly, while `ell''=-epsilon K cos(Kr)` grows with `n`. Thus `R3=0`, and the new positive source is exactly `lambda^2 epsilon^2 sin^2(Kr)`. The lapse range is `exp[epsilon/(pi n)]`.

The rational envelope follows without a numerical fit. At `k=1/10`, direct evaluation of `a/(1-3a)` gives `lambda=117/49`. With `epsilon=3/20`,

```text
x=283/980, y=117/980,
Ebar=41067/1366120,
1/[(1-y)(1-Ebar)] = 1338797600/1143520739
                  = approximately 1.17076809746 < 6/5.
```

The inequalities `pi>3`, `n>=1` and `exp(t)<=1/(1-t)` for `0<=t<1` justify using those constants uniformly. This is an analytic ceiling for any compatible solution satisfying the stated boundary premises, not a claim that the prescribed metric has a complete compatible material solution.

The original M17 source is correctly

```text
c=[epsilon K cos(Kr)-epsilon^2 sin^2(Kr)
                              +2epsilon sin(Kr)/r]_+.
```

Because `m<=N<=1`, its center Green value obeys `P0>=m integral_0^1 r(1-r)c dr`. Restricting that nonnegative integrand to `[1/4,3/4]` gives the factor `3/16`. On this interval, `c>=epsilon K(cos Kr)_+-(epsilon^2+8epsilon)`. For even `n`, there are exactly `n/2` full cosine periods, whose positive-part integral is `1/(2pi)`. This gives the displayed lower bound without multiplying a possibly negative pointwise lower estimate by the wrong weight: first lower-bound the nonnegative weighted integral by `3/16` times its integral, then integrate the source inequality.

At `n=64`, `exp[-epsilon/(pi n)]>1-epsilon/(3n)` yields the exact rational lower bound

```text
lambda P0 > 3228248439/802816000
           = approximately 4.02115607935 > 4.
```

The independent arithmetic file records both strict rational margins. Hence the old `eta<1` sufficient condition definitely fails on this supplied metric while the new condition is satisfied with the stated finite ceiling. This is a strict separation of the criteria on kinematic geometries. It is not a counterexample to M17, a proof that the new criterion uniformly dominates the old one, or a physical improvement already established for a real gravitating body. The working draft makes the decisive realization limitation explicit.

The exact choice `B=1` supplies `R3=0` and the central cancellation analytically. It does not demonstrate that finite independent clock/ranging measurements can certify the same cancellation or the same envelope with useful errors. That distinction must remain when discussing usefulness.

## Author evidence and disposition limits

I read the numerical repair receipt and protocol, and inspected result counts/failure rows. The original v3 artifact preserves **60 passed, 3 failed**: refined Green disagreement at `n=16` and `n=64`, and the `n=64` scalar BVP node-limit failure. The v4 artifact records **63 passed, 0 failed**. These are author diagnostic results, not my independent numerical execution or a continuum error certificate. The protocol describes source-root splitting and a node budget change from 40,000 to 120,000 with thresholds unchanged. This review does not certify the implementation delta or reproduce those solves; its analytic strict-separation conclusion does not depend on them.

The extension belongs with M17: the same complete action, source-sign argument, physical domain, boundary assumptions and Green comparison gain a different calibrated-input certificate and an explicit separation witness. Packaging it with the earlier four-curvature bound allows the bounds to remain complementary. A second algebra-only PR would add review overhead without a separate physical claim. The narrower measurement premise is substantive, but calibrated spatial curvature, lapse/gradient enclosures, state, scales, complete boundary and full matter/metric consistency remain open suppliers.

No new primary acquisition or empirical data was used. Prior source readings are reused at their frozen scopes; they are not evidence for a new observational success or priority claim. No canonical file, Git state, PR or audit authority was changed. This report applies to the identified working source; later canonical adaptation needs its own source-bound confirmation.
