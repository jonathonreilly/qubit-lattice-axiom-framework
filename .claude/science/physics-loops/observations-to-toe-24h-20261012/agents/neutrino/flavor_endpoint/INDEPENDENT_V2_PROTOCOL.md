# Independent boundary V2 protocol

Frozen after the V1 delivery receipt, before V2 numerical calculation. Root's
`gravity/flavor_boundary/PROTOCOL.md` was read (SHA256
323ea798305ae758ebe41eaaec1f6c59b941843980e9b6931188b37db43904a7).
Root's V2 runner and numerical outputs have not been read. V1 remains unchanged.
Public inputs/targets are exposed, not blind. theta12 is now explicitly
repurposed from V1's test to this new candidate's calibration.

Match the author's supplied matrix J00=b, remaining diagonal s+2,s+4 and
offdiagonal -sqrt(s), -sqrt(2(s+1)), normal ordering, electron/muon/tau slots.
Physical scalar support conditions: s in [.01,10], b in [min(s,1),30]. The
endpoint equality requires the atom analysis in BOUNDARY_ADMISSIBILITY.md.
Calibrate only a13=.0851 and q12=.3092. The separate ±1.96 error rectangle is
a sensitivity probe, not a joint confidence region: Daya Bay and JUNO share
inputs. Standard propagation and all source-conditioning limitations persist.

Independent direct recurrence:

```
P(x) = (x-b)[(x-s-2)(x-s-4)-2(s+1)] - s(x-s-4)
v(x) = [1, (b-x)/sqrt(s),
        ((s+2-x)(b-x)-s)/sqrt(2s(s+1))]
```

Normalize v to derive weights and mixing angles; cross-check against eigh.

A separate inverse spectral reduction avoids importing root's solver. With
w3=(1-sqrt(1-a13))/2, w2=q12(1-w3), w1=(1-q12)(1-w3), choose ordered
dimensionless nodes y=(0,r,1), 0<r<1. Let Mj=sum wi*yi^j, A=M1,
h=M2-A²>0, N=M3-2AM2+A³, a1=N/h,
a2=1+r-A-a1, beta1²=h, and
2beta2²=1+r²-A²-a1²-a2²-2h.

For a physical shift/scale x=q+k*y, the fixed diagonal difference requires
k=2/(a2-a1)>0. Thus s=k²h, q=s+2-k*a1, b=q+k*A, and the remaining
offdiagonal condition is

```
F(r) = 2beta2² - 4h - (a2-a1)² = 0.
Q(r) = (1+r-A)*h-N
h²F = (1+r²-A²-6h)*h² - 2*(N²+Q²-N*Q).
```

The displayed smaller w3 branch is the one consistent with the published
standard-sector fits. Before numerical execution, also retain the algebraic
larger branch w3=(1+sqrt(1-a13))/2 as a diagnostic: amplitude alone has this
ambiguity, and the author's bounded (s,b) search may otherwise find it. Such
a root would not inherit the published JUNO small-theta13 summary likelihood.
Report it separately rather than silently discarding or interpreting it.

This is a degree-at-most-six polynomial with known calibration-weight
coefficients. Enumerate all numerical polynomial roots, retain real roots in
(0,1), check the direct recurrence and k>0, then apply infinite positivity and
bounded-search conditions. Keep rejected algebraic roots with their reasons.
Perform the root enumeration for both w3 branches. This finite root enumeration
is a useful independent check, not automatically
an exact uniqueness certificate. If feasible use symbolic exact algebra with
the decimal calibrations as rationals and sqrt(9149) for a13 to count/isolate
roots; do not claim such certification unless it actually succeeds.

Cross-check by bounded multistart least-squares in (s,u), with
b=min(s,1)+(30-min(s,1))*u, u in[0,1]. Use a fixed mesh s=(.0101,.03,.1,.3,
.7,.99,1.01,1.5,2,3,5,7,9.99), u=(0,.02,.1,.3,.6,.95), tolerances1e-12,
maximum2000 evaluations. Keep every solver residual/status and all distinct
roots. Scan/minimize residual along each boundary as a diagnostic. This
bounded search is numerical evidence, not a general nonexistence proof.

Evaluate the four corner inputs (.0851±1.96*.0024,.3092±1.96*.0087)
through the same polynomial construction; keep admissible roots and forward
theta23, CP and p=1,2 gap outputs. Do not fit theta23 or a mass-map exponent.
If the full corner rectangle is traversed, it remains a sensitivity rectangle,
not a confidence region. Compare to the pinned primary summaries only under
their actual interval and prior definitions. Scalar measure must be deformed
with the same b and s; determine whether any threshold atom is present.
