# Independent boundary V2 result

V2 has exactly one admissible central calibration solution under the declared
ordered-flavor identification. It fits the two chosen summaries but still fails
the atmospheric-angle and fixed mass-gap summary checks. This is a separately
supplied physical hypothesis, motivated by V1's failure; theta12 is now a
calibration input. It is not a blind prediction, a TOE derivation, a quantified
experimental exclusion or a change in audit standing. Public-source conditioning
and overlap are documented in `V1_PRIMARY_COMPARISON.md` and remain in force.

The independent V2 protocol/code were frozen at18:16:09Z and the initial results
at18:17:04Z, before reading root's code or numerical outputs. Only root's frozen
protocol had been read. A post-fit exact algebra validation then completed.
Author results were first read at18:20:07Z; the central results agree to floating
roundoff. No author function was imported and no author code was read.

| Quantity | Independent central value |
|---|---:|
| s | 3.21050804503348 |
| b | 2.12389107560436 |
| delta=b−s | −1.08661696942912 |
| ordered x | (.999461803080464,4.11036348362882,9.43508187896204) |
| sin²theta23 | .370143843770920 |
| r21/31, p=1 | .368781625128280 |
| r21/31, p=2 | .180593395434937 |
| r21/32, p=1 | .584237784907998 |
| r21/32, p=2 | .220395337832059 |
| deltaCP / JCP | 0 / 0 |
| infinite positivity margin b−1 | 1.12389107560436 |
| zero-mass atom | absent |

The direct recurrence is

\[
v(x)=\left(1,{b-x\over\sqrt s},
{(s+2-x)(b-x)-s\over\sqrt{2s(s+1)}}\right)^T.
\]

At the central solution it agrees with a symmetric eigensolver within2.5e-16;
the eigen residual is below1.8e-15. An independent inverse spectral construction
provides more than a numerical multistart check. Set the measured electron
weights to w3=(1−sqrt(1−.0851))/2, w2=.3092(1−w3), w1=1−w2−w3, and
normalize ordered eigenvalue nodes to y=(0,r,1), 0<r<1. Write A=M1,
h=M2−A², N=M3−2AM2+A³, Q=(1+r−A)h−N, where Mj=sum wi yi^j.
The Jacobi diagonal entries after normalization are a0=A,a1=N/h,a2=Q/h.
The fixed physical diagonal difference forces k=2/(a2−a1)>0 and
s=k²h, b=s+2−k*a1+k*A. The second offdiagonal condition becomes

\[
G(r)=(1+r^2-A^2-6h)h^2-2(N^2+Q^2-NQ)=0.
\]

This degree-six condition is necessary and sufficient after the positive-scale
and domain checks: the unique Jacobi matrix for the three positive weights and
distinct ordered nodes reconstructs the specified entries. Exact Sturm
arithmetic over Q(sqrt9149) counts two roots in(0,1) for the small-theta13
branch and zero for the alternative amplitude branch with w3>.5.
The roots are r≈.170734043322 and .368781625128. Exact rational interval
evaluation on the isolated root intervals proves that the first has
a2−a1 in[−.424742371439,−.424742371160], hence a forbidden negative scale.
For the second it proves

```
s  in [3.210508040445,3.210508047928]
b  in [2.123891068893,2.123891081935]
x1 in [.999461797180,.999461808866]
```

so it is inside the declared domain and strictly above the infinite-support
positivity threshold. Together these certify one admissible central solution.
This exact statement treats the decimal calibration centers as exact numbers;
it is not an exact treatment of experimental uncertainties. The floating-point
renderings of the bounds above are rounded presentations; code comparisons use
exact rational intervals. No Lean or formal claim audit has been performed.

The independent bounded search used78 prescribed starts. Forty-two reached
the same zero residual root; the other36 stopped at nonzero-residual minima.
All statuses, residuals and boundary scans are retained. These numerical solver
convergence labels alone would not have proved uniqueness. The inverse
polynomial, Sturm count and rational sign/domain checks supply that additional
central algebra result. The initial combined calculation took0.91s with one
numerical thread; the interval validation is also small.

The four separate ±1.96-error calibration corners each produced one numerical
admissible small-branch solution. Their theta23 values are .36622449,
.35761470, .38362431 and .37379776. Their r21/31 values span .36123871–.37610745
for p1 and .17308580–.18994628 for p2. These are four corner outputs, **not a
proved envelope or joint confidence region**. No theta23, mass gap or CP target
was used to fit s or b.

The central theta23 and all four corner values lie below the NOvA2026
no-reactor-constraint68% HPD set [.465,.509] union [.517,.562]. The central
fixed-map gap ratios remain far above the separate-summary r21/31 rectangle
[.0290117,.0307730]. Those are the same limited forward comparisons already
defined in V1. No combined significance follows: solar assumptions remain in
the accelerator summaries, and Daya Bay/JUNO share constraints and reference
data. In particular a fixed mass map producing such a large solar/atmospheric
gap ratio does not inherit Daya Bay's already-conditioned calibration likelihood
unchanged. CP=0 by itself is not excluded by the pinned joint NO three-sigma
interval. A free mass exponent cannot change theta23.

The scalar mathematical construction remains admissible but its measure is
changed. At this root s>2,b>1, so the exact results in
`BOUNDARY_ADMISSIBILITY.md` give no threshold atom or negative eigenvalue.
The continuous measure is rho_delta=rho_s/|1+delta*m0(x+i0)|², normalized to
one. Its low-x exponent remains s−1 and its leading coefficient relative to
rho_s is ((s−1)/(b−1))²=3.86843901. Useful exact normalization checks are

\[
\langle x\rangle=b,\quad\langle x^2\rangle=b^2+s,\quad
\langle x^3\rangle=b^3+2bs+s(s+2),
\]
\[
\langle x^{-1}\rangle={1\over b-1}=.88976594,\qquad
\langle x^{-2}\rangle={s-1\over(s-2)(b-1)^2}=1.44569265.
\]

The same deformed measure, and independent scale ell, must enter both static
and vacuum kernels. The old gamma force/noise law is not its forward model.
Fitting the neutrino centers does not validate this scalar shape empirically,
especially because the neutrino holdouts fail. The constructive conclusion is
to retire this specific endpoint/boundary identification as a successful
flavor explanation, while retaining the admissible spectral construction and
the inverse-polynomial method as tools. Any further flavor architecture needs
a new stated physical reason and a new protocol; adding a mass-law fit first
would leave the decisive angle mismatch intact.

Reproduce with `independent_v2.py --out <runtime>/independent_v2_results.json`
and `v2_exact_admissibility.py --out <runtime>/v2_exact_admissibility.json`.
Protocols, code, results, exact checks and author-concordance receipt are sealed
in `V2_DELIVERY_FREEZE.json`. No V1 artifact was changed.
