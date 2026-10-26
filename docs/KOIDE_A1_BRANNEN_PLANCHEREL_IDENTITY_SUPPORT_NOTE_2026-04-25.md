# Supplied real Fourier and plane-coordinate identities

**Date:** 2026-04-25
**Type:** bounded_theorem
**Status:** conditional algebra and calibrated finite fixtures; no physical phase selection.
**Primary runner:** `scripts/frontier_koide_a1_brannen_plancherel_identity_support.py`

## Fourier identity with explicit orientation

For V0,c>0 and real delta, supply real amplitudes
v_j=V0[1+c cos(delta+2pi j/3)], j=0,1,2. They need not all be positive;
positivity of each component is an additional premise to interpret them as
positive square roots of masses. Let omega=exp(2pi i/3) and define

```
a0=(v0+v1+v2)/sqrt(3)
b=(v0+conj(omega)v1+omega v2)/sqrt(3).
```

The sum of the three roots of unity vanishes. Expanding cos as the sum of
its two exponentials gives sum cos=0 and
sum_j omega^(-j) cos(delta+2pi j/3)=(3/2)exp(i delta).
Therefore a0=sqrt(3)V0 and b=(sqrt(3)/2)V0 c exp(i delta).
Since V0,c>0, b is nonzero and arg(b) = δ modulo2pi, with δ=delta.
This is a coordinate identity inside a supplied parameterization, not a
physical derivation of the parameterization or its phase.

## Exact plane convention

For any real vector v, let p1=(v0−v1)/sqrt(2),
p2=(v0+v1−2v2)/sqrt(6). Direct expansion gives

```
b=exp(i*pi/6)(p1−i*p2)/sqrt(2).
```

For a nonzero doublet, writing alpha=atan2(p2,p1) yields
arg(b)=pi/6−alpha modulo2pi. Thus consistent wrapped angle differences
have opposite signs in this convention. No Berry connection or holonomy
is defined by this coordinate change. In particular an angle offset is
not an invariant open-path geometric phase.

## Phase remains free even at Q=2/3

For c=sqrt(2), root-of-unity sums give sum v_j=3V0 and
sum v_j²=6V0², hence Q=sum v_j²/(sum v_j)²=2/3 for every delta.
At delta=0 all components are positive: V0(1+sqrt(2),1−1/sqrt(2),1−1/sqrt(2)).
At delta=pi/24, the smallest cosine is cos(17pi/24)>cos(3pi/4)=−1/sqrt(2),
so all three components are again positive. Their phases differ while Q
and the three-component dimension agree. Defining r=Q/3 gives2/9 but
cannot determine this freely varying delta. A law delta=r is extra input.

## Finite calibrated fixtures

The supplied mass triple (GeV) is (0.51099895e−3,105.6583745e−3,1776.86e−3).
The runner fits V0 and c from its square roots, then compares a folded phase
and reconstruction with the supplied value2/9. Sign/cyclic folding is a
chosen unordered comparison convention. The reconstruction is calibrated,
not an independent prediction. The4pi/9 fixture has a negative component
for those same calibrated parameters; it only rejects that positive-amplitude
instance, not other lifts, models or physical phases.

A second self-contained fixture supplies gamma=1/2,E1=sqrt(8/3),E2=sqrt8/3,
s=sqrt6/3 and the matrices written explicitly in the runner, then evaluates
exp(Hbase+m Tm+s(Td+Tq)). It reads two diagonal entries, supplies the smaller
root of the cone quadratic, and compares plane angles at hard-coded
m0=−0.265815998702 and mstar=−1.160443440065. The1e−12 comparisons are finite
coordinate witnesses, not exact dynamics selection. All original tolerances
and meaningful predicates remain; the exact plane formula and orientation
control supplement them. The runner imports no repository helper or geometry
runner. The symbolic proof is distinct from these finite tests.

## Historical correction and execution scope

The old instruction to promote a Berry theorem into authority is withdrawn.
Physical observable identification, dynamics, source and mass interpretation
remain unproved here; no claim is made that a single radian bridge is the only
missing premise. Historical no-go/Brannen/OP arguments are preserved in source
recovery but are not proof dependencies of these elementary identities.
The old tautological closure flags are not evidence. No audit status is changed.

The primary declares this note as its sole input and a120-second cap, checks
input availability, resets its check list and returns nonzero on failed checks.
Prior source/cache are preserved; no new execution is claimed by this source
revision. Independent source confirmation precedes any authorized capture.
