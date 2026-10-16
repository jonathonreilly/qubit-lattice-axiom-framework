# Integer-history author-source correspondence v1

Reviewer: `/root/force_energy_bridge_check`. This is a narrow **post-author-exposure** correspondence check. The independent quotient derivation and its 114 controls were completed and frozen first; they remain unchanged. This report does not convert an author-suite rerun or post-exposure fixture into independent blind evidence, and is not a formal audit.

## Exact scope and finding

I read the complete 176-line `INTEGER_HISTORY_QUOTIENT_WORKING_v1.md` and complete 103-line `integer_history_controls_v1.py` pinned by `AUTHOR_FREEZE_v1.json`. Their SHA256 values are respectively:

- Note: `90c7356e9ea988969d13cb69269fd673d9c3de0c5bdf3fa7c65ff13231508568`.
- Program: `e9997f5679c08bfe726bfa604fc243f5f403375b375092f6f304ebadbd987807`.
- Author freeze: `6b8aadf3251f05f6606f70f196185497ba50675d565d713f581292ee67ab2a0e`.

Exact copies and the exposure chronology are preserved in this directory. Mathematical sections 1–3 and the mathematical scope limitations in section 4 agree with the independently frozen result. I found no mathematical discrepancy in the quotient, periods, energy convention, curved-weight dense-image witness, SPD lattice minimum, or completeness proof for the exact-input enumeration.

There is one actionable **input-domain guard gap** in the program's `projected_period`: it documents exact rational coefficients but accepts a Python float through `Fraction(x)`. In particular, `projected_period([sqrt(2),1])`, where sqrt is the floating library function, returns `1/4503599627370496`. That is the period of the binary-rational encoding, not evidence that the intended irrational coefficient has a discrete image group. The displayed theorem and current exact calls are unaffected. Before general/canonical use, explicitly reject floating weights and periods, or expose an equally explicit exact-input boundary that cannot be mistaken for physical rationality. No rounding scheme can decide rationality of an unknown physical coefficient. This finding was sent to the author. It is not repaired by the passing current fixtures.

The source note contains development-data totals, format citations and receiver-semantics claims. They were encountered while reading the whole note but were **not checked here**. I did not open the development script/results, protocol, raw observations, citations or later data products. Only their names/hashes in the author's freeze manifest were exposed. This report supplies no empirical or receiver-calibration verdict.

## Quotient, characters, periods and real resets

The author's consecutive-endpoint incidence D is an integer quotient-coordinate choice equivalent to my anchor-difference K on each supplied chain. D has an integer right inverse obtained by cumulative summation. Therefore the arbitrary integer endpoint ambiguity maps onto all edge integers. Segment constants cancel within the chain, and M integer plus arbitrary unit-cycle histories gives the one-cycle quotient. The distinction between the native M-cycle quotient without that extra history premise and the one-cycle quotient with it is correct.

For a P-lattice, `exp(2 pi i a^T x)` is invariant precisely when every P a_j is integer. For a scalar integer v, its natural projected period is `P gcd(|v_j|)`, not necessarily P. The rational half-weight example correctly changes output period, and the note explicitly rescales the signal and real error rather than claiming free precision. The known-baseline subtraction is valid only with the separately supplied baseline/transfer identification, as stated.

The discussion of dense real projections is limited appropriately. A dense scalar projected ambiguity destroys continuous scalar information in that projection; it does not erase the original torus vector, prove all inference impossible, or apply to bounded integer histories automatically. Arbitrary real resets are explicitly not eliminated. The chain/loop distinction is also honest: independent edge integers on a looped graph are a conservative enlargement, not an assertion of exact endpoint-image equality.

For the one-second count example, `(1,-2,1)D=(-1,3,-3,1)`. The endpoint vector annihilates polynomial degrees 0,1,2 at equal time steps. Durations must be restored before testing the induced phase weights. This does not prove an arbitrary frequency-normalized row is a character.

## Curved-weight dense-image witness

At the declared rational times `t_i=7/5+i`, `L=3/5`, the physical curved endpoint coefficients are

```
beta_i=(1-H(1/5+i)) gamma_i,
gamma=(-1,3,-3,1).
```

Their sum vanishes, so the arbitrary real segment offset is annihilated. Nevertheless their integer-history image contains both

```
beta_0+beta_3=-3H,
16 beta_0+beta_3=-15.
```

For irrational dimensionless H, `15 Z+3H Z` is dense. Thus that real-valued curved row need not descend to a useful scalar circle under unrestricted integer histories. This is an actual arithmetic mismatch between a selected real row and the quotient, not a sign or normalization error in the preceding curved response. The physical real-count row remains valid when an appropriate real calibrated phase/history is supplied.

The conclusion is coordinate/premise aware: the witness assumes these rational dimensionless times in the chosen units and irrational H in those same units. It does not claim to infer physical irrationality from finite measurement precision. My focused controls verify the full beta cancellation and both generating combinations exactly, including an illustrative irrational H inside the previous chart interval. The finite Pell sequence is only a diagnostic; the limiting integer-group argument carries the density result.

## Exact energy convention and finite Gram geometry

The author's `N=||h||^2` is a Hilbert squared norm. `sigma_v=||A* v||`, hence `sigma_v^2=v^T G v`. The scalar bound

```
N >= max(dist(v^T r,gP Z)-eta_v,0)^2/sigma_v^2
```

matches the independent result, including g=gcd(v), the zero-response feasibility case, the zero contrast and the need for a supplied nonnegative error bound. The physical conversion is separately `E>=q N`, q>0; no extra 1/2 is to be inserted unless it is part of that supplied q. The bound does not choose a physical state or a real-error magnitude. Combining shared endpoints through D^T v before taking an error bound is correct.

For the scalar-only, error-free sharpness claim, Bezout realizes the desired multiple in v^T k and the nonzero Riesz representer realizes the scalar response. The note explicitly limits sharpness to that scalar observation; the remaining vector rows can impose stronger constraints.

For SPD G, every finite target is achievable by `A*G^(-1)y`, with minimum norm `y^T G^(-1)y`. Minimizing over `r+Pk` is exactly the lattice problem; its sign convention is equivalent to `r-Pk`. Coercivity gives attainment. If the error set is **supplied** as the G-inverse ellipsoid of radius eta>=0, the inner norm minimum is the distance to that ball, giving `max(sqrt(Ninf)-eta,0)^2`. The formula is not valid for an arbitrarily chosen replacement of the actual error set, and the note does not make that replacement. Singular G is explicitly deferred with a required range condition.

The two-count counterexample uses the earlier physical Gram `[[3064,-1871],[-1871,3064]]/(1620 pi)`. The code sets Gtilde to the same matrix without `1/pi`. Consequently its objective is **N/pi**, exactly as its result fields `minimum_N_over_pi` and `component_rounding_N_over_pi` state. The physical Gram convention is not missing a pi. A separate exact symbolic check confirms this bookkeeping.

The executed example gives

```
minimum N/pi = 16132149/98124250,
componentwise principal-wrap N/pi = 194481/298250,
minimizing lifts = (-1,0) and (0,-1).
```

That is the same correlated-Gram failure mechanism as my independently constructed different example. It is a synthetic mathematical fixture, not an observed residual.

## Complete finite enumeration bound

For an SPD two-dimensional G and x=r+Pk,

```
x^T G^(-1)x >= ||x||^2/lambda_max(G)
              >= ||x||^2/trace(G).
```

The code's incumbent is the feasible k=0 objective I. Every candidate with objective no larger than I obeys `||x||^2<=I trace(G)`. It chooses an integer R with `R^2>=I trace(G)` by exact squared comparisons and enumerates the enclosing coordinate box

```
ceil((-R-r_i)/P) <= k_i <= floor((R-r_i)/P).
```

This contains every improving or tied candidate, including the incumbent; it is not a heuristic neighborhood of a principal wrap. The R=0 case with r=0 also retains k=0. Symmetry, positive leading entry and positive determinant are the exact two-dimensional SPD conditions used by the helper. Its fixtures use exact rational data, so no floating truncation is introduced into the box endpoints. The argument establishes completeness, not efficiency for large unreduced lifts or arbitrary-dimensional problems.

I compared nine exact rational SPD/input/period combinations with a separately implemented enumerator using a different incumbent (coordinate-rounded feasible lift), a Gershgorin eigenvalue bound and Fraction arithmetic. Every minimum and minimizing-lift set agreed. A further nine controls independently checked the author's exact squared radius, least integer radius, and representative first-excluded points. These are post-exposure correspondence diagnostics; the general completeness proof above is the justification beyond those finite examples.

## Executions and preserved evidence

I executed the frozen author program **once**, from its exact unchanged copy in this reviewer directory, so its `__file__`-relative output stayed here. It exited 0 with 31 checks passed and empty stderr. Its output SHA256 `b0c685ab0e34ad0a0949c9caea0d87e22e4924e2d15df9918abf7ff5387bf314` exactly matches the author's frozen result identity. This is a recorded reproduction, not an independent scientific check.

The additional focused post-source script did not invoke the author's aggregate runner. It produced 24 passing diagnostics with no failed run or code repair. One diagnostic explicitly **demonstrates** the still-open float-input guard gap, so the passing count must not be mistaken for closure of that finding. Script SHA256: `c8467d86600e7f34be0ff04652d558a210852581bfbcdce3166442fa9854e32e`. Results SHA256: `ad362f08988d8635112a035d6f79006a61a1e93624160e6e677d1a78b7559da2`.

The original independent report remains SHA256 `a50044f679a3d4dd6e9e279c31a657969d30c2deafb712f03e83f96f5abf547a`, identity `51b8abb7795054e2f07ae588fc3654f3daec5bb77934152b1a7f13326028091d`. Its 114 pre-author-source controls are distinct from both the 31 reproduced author checks and these 24 post-exposure diagnostics. The exposure record SHA256 is `a355c13836f62638074ef40cbfca7cf7ee20c1e7b50c5051571e326bc49888fe`.

Only reviewer-directory files were written. No root scientific source, empirical product, Git/index state, branch, lock, PR, network resource or audit record was changed. A later canonical adaptation or guard repair should receive a separately frozen affected-source confirmation, preserving this original finding and source identity.
