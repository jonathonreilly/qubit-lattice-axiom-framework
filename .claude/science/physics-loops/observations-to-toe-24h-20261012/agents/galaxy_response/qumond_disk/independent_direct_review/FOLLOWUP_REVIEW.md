# Independent fixed-three scoring and solar-basis check

2026-10-12. The assigned fixed-three numerical gates and scores reproduce, and
the new scalar response-basis calculation passes this narrow mathematical
check. No material source defect was found. This confirms the completed gates
left open in [FINAL_REVIEW.md](FINAL_REVIEW.md); it does not review the
concurrently authored galaxy response operator or inversion constraints.

## Source and provenance

| Source | SHA-256 |
| --- | --- |
| `direct_fixed_comparison.py` | `8ebffde646e012b3cc198680deabb3737aad45099d76ffbfc697702238a65d40` |
| `direct_qumond_disk.py` | `701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00` |
| `DIRECT_RESPONSE_INVERSION_TARGET.md` | `fe721b5abdf2e4312893a2ab76de2febe68d7e0fdf95fc1d69edbf28bd1eb231` |
| `DIRECT_RESPONSE_BASIS_RESULTS.md` | `f1111c82ad6e2129d454ec6cea1725990289ba7113c225e0e9c1c561dd3262c2` |
| `direct_response_basis.py` | `da0c24cdf104a79abc8bb796056e64d06dfb8c248fe39ca3de7325c629293f4f` |

The complete new source and notes were read. The inherited solar Hessian
definition and positive-kernel derivation were read as necessary context;
their exact snapshots are retained with the new sources in this directory.
The fixed-field solver and contract retain the prior same-session review.
`followup_source_freeze.json` and `followup_review_receipt.json` in the runtime
review directory bind the source, input, receipt and report hashes.

Every gate-referenced force receipt matches its recorded SHA-256. Each uses
the frozen NPZ hash, original metadata/source row, U=0.5605122519882025 and
a0=7.658058668049826e-11 SI. Source versions `0d02f2a...`, `144cf1f...` and
`701bc4d...` have the previously inspected dispositions: controls and
zero-force diagnostics changed, while the positive-field projection is the
same. Final boundary receipts and the scalar controls use `701bc4d...`.
No earlier result was restamped with a later solver hash. The four source
files pinned by the original forward contract still match exactly.

## Numerical gates and scores

[check_fixed_scores.py](check_fixed_scores.py) reads saved force arrays and
the selected target arrays, without importing author scoring helpers or
rerunning any field solve. It recomputes even the Newtonian midplane error
from the frozen component forward arrays. All values below are maximum
relative force differences using the comparison code's reference denominator.

| Galaxy | Newtonian midplane | Newtonian projection | Last angular refinement | Boundary/Hankel/grid change |
| --- | ---: | ---: | ---: | ---: |
| NGC2976 | 6.89e-13 | 2.24304e-5 | 0.0031394730 | 2.93965e-5 |
| UGC07577 | 1.01e-12 | 4.70080e-4 | 0.0041126033 | 1.11213e-4 |
| KK98-251 | 7.03e-13 | 3.56976e-5 | 0.0016509750 | 3.43291e-5 |
| Frozen limit | 2e-6 | 0.003 | 0.005 | 0.003 |

All pass. The UGC refinement compares ell256 to ell512. Its often quoted
0.0041296 value uses the final force as denominator; the gate's 0.0041126
uses the previous force. This convention difference changes no disposition.
The final runs halve the inner cutoff, double the outer cutoff and Hankel
order to 4096, and retain 1536 radial points and the latest angular grid.
These checks supply the declared finite-resolution evidence. Simultaneously
changing the boundaries, Hankel order and radial spacing does not separate
their error contributions or certify a rigorous one-percent error bound;
the gate receipt states that limitation correctly.

The independently reconstructed masks are exactly `R>0` and `R>=0.5 Rd`.
There are 21, 7 and 12 selected points, with no score-dependent omission.
Radii, processed velocities and their copied errors match both the forward
and target arrays. All selected forces and velocities are positive. Units
are consistent: force in `(km/s)^2/kpc` times R in kpc gives velocity squared.

The independent score uses
`r_i=(log10 R_i+log10 g_i)/2-log10 Vobs_i`, rather than the author's
log of its computed velocity ratio. Per galaxy it uses `sqrt(mean(r_i^2))`.
The aggregate observation weight is `1/(3*n_galaxy)`, giving equal total
weight to each galaxy. The processed errors are reported but are not weights.

| Fixed prediction | Equal-galaxy RMS log10 velocity | Equal-galaxy mean log10 velocity |
| --- | ---: | ---: |
| Newtonian | 0.1344548130557855 | -0.1152631614359590 |
| Algebraic | 0.1981509070862624 | 0.1534609168228968 |
| Local full norm | 0.1660528314066034 | 0.1249152226970457 |
| Full PDE | 0.1653530502305255 | 0.1204724544065365 |

The full-PDE per-galaxy RMS values are 0.01556580152688085,
0.2679343743097495 and 0.09996884788615303 in the displayed galaxy order.
All prediction arrays, individual log residuals, means, RMS values and
aggregates agree within floating-point roundoff.

The scoring code asserts every gate before opening `sealed_targets.npz`.
The preserved gate timestamp precedes the score timestamp, and every force
receipt predates the gate. This verifies the ordering of this execution,
not historical blindness: these three sources were previously exposed
training data. The comparison properly claims neither refitting, likelihood,
statistical significance, complete covariance treatment, full-sample
calibration nor survival of the prior Solar prediction. The inherited
baryonic geometry, fixed nuisance parameters and isolated boundary remain
conditions. The aggregate values do not identify a generally preferred
gravity theory.

## Response basis: sign, units and regularity

The retained sign convention is `deltaPhi=-Q2*(z^2-r^2/3)/2`, so
`Q2=-3 Hzz/2`. Starting with the source Hessian and this convention gives
the positive coefficient in the reviewed notes, not its negative.

For A=a0*q, `nu'(q)=a0*N'(A)` and `dq=dA/a0`. Together with
`eta=g_Ne/a0`, multiplication by the physical factor
`a0^(3/2)/sqrt(GM)` cancels every power of a0. The result is

    Q2 = (9/8) g_Ne^(3/2)/sqrt(GM)
         integral W(A/g_Ne) [-N'(A)] dA.

`g_Ne^(3/2)/sqrt(GM)` has dimension `time^-2`; the integral is dimensionless.
For `0<L<H` and `g_Ne>0`, a unit log ramp has
`-b'(A)=1/(A log(H/L))` on `(L,H)` and zero elsewhere. Its derivative
measure has total mass one. This gives the stated
`F=9/(8 log(h/l)) integral_l^h W(s) ds/s`, positive for every finite
positive-width interval. Weights are dimensionless. A galaxy operator using
the existing code's acceleration units must evaluate this physical-A basis
at `ACC*|U|`; that future implementation was not part of this assignment.

The ramp is continuous at both knots; its first weak derivative has no delta
terms. Piecewise integration by parts cancels the common boundary value at L
and the zero value at H. The regularity extension in the results note is
sufficient for this finite-knot family: positive smooth mollifications of the
log-derivative have common compact support away from zero and a uniform
derivative bound. Their integrated responses converge uniformly. Near the
Sun every response is exactly Newtonian; near the field saddle it is constant.
Away from those regions the chain rule applies almost everywhere. At infinity
the source is bounded by C*r^-3, even if the external field lies exactly at
a knot, and the Hessian kernel with volume measure gives an integrable
`r^-4 dr` tail. Thus a common integrable bound supplies the same weak-source
and Hessian limit. This does not cover a discontinuous step or an arbitrary
measure without further argument.

For a fixed baryonic U and fixed homogeneous boundary choice, Poisson
projection is linear in the supplied response N. Therefore the proposed
force-column reduction is correct. The radial columns need not be positive,
whereas the solar columns are positive for decreasing ramps. Changing stellar
M/L changes U and its response argument, so it cannot be absorbed into an
unchanged linear column. The notes correctly restrict this finite bounded
low-acceleration family and do not claim an unbounded deep-MOND tail, an
empirical feasibility result, or a universal observational exclusion.

## Independent synthetic integral

[check_response_basis.py](check_response_basis.py) accesses no empirical
velocity, acceleration or Solar-constraint input. Its independent expectation
integrates the non-rationalized square-root expression for W at 55 digits in
log acceleration. A second independent path changes the source-Hessian
integration order: at eta=1, let `s=q`, `t=w^2` and
`c=(t^2+1-s^2)/(2t)`. The Jacobian is `s/(2t^(3/2))`, with
`|1-s|<=t<=1+s`. Direct substitution of the log-ramp derivative yields

    F = -3/(4 log(h/l)) integral_l^h ds/s
        integral_|1-s|^(1+s) dt/sqrt(t)
        P2(c) [s^2-3(t-c)^2].

The reviewer evaluates this with `s=exp(u)` and `t=z^2`, independent of the
author's w/c knot splitter and response functions. Author functions are
then executed only as subjects against the completed independent values.

All four original intervals agree. The largest discrepancy of the independent
density calculation from the 55-digit reference is `9.12e-11` relative, and
the largest author's discrepancy is `5.21e-11`. Fresh intervals give

- `[0.37,1.63]`: F=0.242606047472064074037928871999;
- `[2.3,9.7]`: F=0.214713914277569845542544036513.

The basis check ran in 0.257 seconds at approximately 82 MB maximum RSS, with
one configured numerical thread. These are finite checks, not interval
certificates. The actual failed first attempt and its matching source remain
preserved; they fail by 0.00517 and 4.728 relative on the two above-external
intervals. The corrected radial knot split is mathematically appropriate:
`w^2=eta+q_knot` or `w^2=abs(eta-q_knot)`. No response interval or acceptance
threshold was changed to cure that defect.

Evidence: runtime review files `fixed_score_check.json`,
`response_basis_check.json`, their logs, and `followup_review_receipt.json`.
No author files were edited, no new empirical hypotheses were fitted, and no
heavy field solve, formal audit, commit, push or main-status change was run.
The original packaging deadline and stop markers remain controlling. Any
changed basis/source or eventual response operator needs its own affected
source and numerical confirmation.
