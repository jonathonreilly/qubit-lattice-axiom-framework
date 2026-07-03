# eps* Coefficient Richardson and m != 0 Kernel Sign-Flip Check (Bounded, 2026-06-12)

**Status:** source proposal; the audit lane grades.
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_epsstar_coefficient_richardson_moff0_2026_06_12.py`

## Claim

On the one-particle finite Harper/PT surface with `Q=24`, `Ly=2`, `N=48`,
`GL=20`, and the fixed branch bracket `[1.2, 2.4]`, the genuine fixed-sequence
eta^2 Richardson readout replaces the earlier damped value. The old readout
came from an invalid formula tied to `d_measured`; that path is removed.

The runner now performs the two required calculations separately:

- S1 computes the fixed eta trace from the PT response machinery and fits
  `chi(mu0, eta)/eta^2 = a + b eta^2`. The extrapolated alpha is converted
  from the fitted intercept only.
- S2 independently computes the `mu*(T)^2` root-locus slope `d_measured` and
  reports the measured gap to the S1 extrapolant.

The m=0 anchors reproduce the landed values to full printed precision:

```text
mu0                         = 1.515550712171
alpha_seagull               = -9.266358431847
alpha_full_onepoint(eta=.05)= +4.141818423703
d_measured                  = +3.877078419950
```

## Genuine Eta^2 Richardson

The fixed eta sequence is:

```text
eta=0.080  chi_over_eta2=-4.188319247706e+01  alpha_eta=+0.496321835810
eta=0.040  chi_over_eta2=-7.939270764633e+02  alpha_eta=+9.408149684512
eta=0.020  chi_over_eta2=-4.933473478972e+03  alpha_eta=+58.462368057151
eta=0.010  chi_over_eta2=+8.556903931964e+03  alpha_eta=-101.400538430462
```

The least-squares fit of `chi_over_eta2` against `[1, eta^2]` gives:

```text
chi_over_eta2_extrap        = +1.408325248641e+03
chi_over_eta2_slope         = -3.347859777074e+05
alpha_full_extrap           = -16.688856113481
alpha_eta2_slope            = +3.967261835404e+03
max alpha fit residual      = 85.10840850052
```

This is an honest finite-cell diagnostic: the small-eta sequence is
non-asymptotic under the requested fixed set, and the extrapolant is poor.

## Honest Comparison

The independent root-locus fit is:

```text
T=0.100  mu=1.576146132255  mu2=2.484236630223
T=0.150  mu=1.618806032391  mu2=2.620532970507
T=0.200  mu=1.631150561591  mu2=2.660652154577
T=0.250  mu=1.645930351011  mu2=2.709086720380

mu*(T)^2 = c + d*T^2
c                            = 2.487775722248
d_measured                   = +3.877078419950
max_abs_residual             = 4.552298380935e-02
```

The measured comparison is:

```text
alpha_full_extrap            = -16.688856113481
alpha_kernel_extrap          = -7.422497681634
onepoint_gap_to_d_measured   = 2.647400037535e-01
extrap_gap_to_d_measured     = 2.056593453343e+01
relative_gap_to_d_measured   = 5.304492792203
```

Therefore the genuine fixed-sequence eta^2 Richardson extrapolant does not
improve on the one-point estimate. At m=0 the extrapolated split also does not
satisfy the sign-flip inequalities because `alpha_kernel_extrap < 0`.

## m != 0 Check

At the fixed off-axis mass `m=0.2`, the mirrored machinery still gives the
previous sign-flip result:

```text
mu0(m=0.2)             = 1.528582818440
alpha_seagull(m=0.2)  = -10.989261976026
alpha_kernel(m=0.2)   = +15.113333065709
alpha_full(m=0.2)     = +4.124071089683
```

The kernel term still flips the seagull sign at `m=0.2`:

```text
alpha_seagull(m=0.2) < 0
alpha_kernel(m=0.2) > 0
|alpha_kernel(m=0.2)| > |alpha_seagull(m=0.2)|
```

## Gates

The runner freezes and gates:

- the landed m=0 branch root at `1.515550712171`;
- the landed seagull coefficient at `-9.266358431847`;
- the landed one-point full coefficient at `+4.141818423703`;
- nonzero interband `H1` weight at the PT root;
- the fixed eta set `{0.08, 0.04, 0.02, 0.01}`;
- the genuine eta^2 extrapolated alpha at `-16.688856113481`;
- the eta^2 fit residual below the frozen honest bound `86`;
- the finite-root slope at `+3.877078419950`;
- the measured relative gap below the frozen honest bound `5.4`;
- the measured non-improvement against the one-point estimate;
- the m=0 extrapolated split not satisfying the sign-flip inequalities;
- the m=0.2 kernel sign-flip inequalities.

Smoke:

```text
TOTAL: PASS=12 FAIL=0
```

## Scope

This is a bounded finite-cell, one-particle statement on the m=0 and m=0.2
axes. It does not claim a continuum theorem, a full `(m,T)` surface theorem, a
successful m=0 Richardson improvement, or a gauge-self-energy derivation.
Memory: one-particle only.

The audit lane grades.
