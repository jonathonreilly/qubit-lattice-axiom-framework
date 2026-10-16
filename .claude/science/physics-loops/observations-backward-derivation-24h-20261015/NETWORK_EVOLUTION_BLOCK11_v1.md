# Removing common calibration and zero-state requirements from an intervention test

Author: root, personal exploration; conditional candidate mathematics. This is a
separate development unit, not part of the frozen canonical intervention PR.
No new observation is fitted or tested. The finite linear network action remains
supplied. The goal is to identify which measurement assumptions can be eliminated
algebraically and which must still be established physically.

## Four settings and a common unknown instrument

At one complex frequency, the previously derived rank-one response is
g(theta)=g0-theta H/(1+theta J). Let the physical stiffness change be
theta=a+b*u for a measured command u, with a,b common but unknown. Suppose the
recorded complex response is y(u)=B+G*g(a+b*u), with common unknown B,G.
The resulting y is fractional linear: y(u)=(A+D*u)/(C+E*u). Its denominator
must be nonzero at the measured settings. The constant-response case is allowed
but uninformative. This is a transfer-response statement, not a statement about
raw individual quantum outcome probabilities.

For four settings u1,u2,u3,u4, define yij=yi-yj and uij=ui-uj. Then

    P = u14*u23*y13*y24 - u13*u24*y14*y23 = 0.

Proof: y(ui)-y(uj)=(D*C-A*E)*(ui-uj)/[(C+E*ui)(C+E*uj)]. Substitution gives
the same product of four denominators and the same numerator in both terms.
No division by response differences is needed. Useful identifiability requires
distinct settings and nonconstant responses; otherwise this polynomial may
vanish trivially. The relation does not determine a microscopic network.

Thus neither an absolute response gain/offset nor the physical zero and overall
scale of an affine intervention calibration is needed for this necessary test.
The shared instrument and affine calibration remain conditional. In fact a
fractional-linear calibration theta(u) also passes, so passing does not identify
the affine calibration: this is an explicit ambiguity, not a calibration proof.
A setting-dependent instrument can both break the identity for a valid candidate
and manufacture it for another candidate. That dependence must be constrained.

This is ordinary cross-ratio invariance, not new mathematics or a new metrology
principle. The original NIST-hosted paper by Lewandowski et al., "A Multireflect-
Thru Method of Vector Network Analyzer Calibration", DOI10.1109/TMTT.2016.2627036,
uses the same known invariance in equationsA.1-A.2. The author read the abstract,
measurement-model equations1-9 and AppendixA aroundA.1-A.2, not its complete
experimental validation. Primary URL: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920602 .
Here the useful connection is to the stated single-connection intervention class.
Its physical action and control map are still supplied.

## A deterministic error bound

Suppose measured vi satisfy |vi-yi|<=ei. For vij=vi-vj put eij=ei+ej, so
|vij-yij|<=eij even for correlated measurement errors. Define

    B(ij,kl)=eij*|vkl|+ekl*|vij|+eij*ekl.

Under the model,

    |P(v)| <= |u14*u23|*B(13,24) + |u13*u24|*B(14,23).

This follows by expanding each product error and applying triangle inequalities.
The bound is in instrument units; it does not infer the ei, their confidence
meaning, or command uncertainty. A common additive error cancels exactly before
this conservative bound. An unknown common multiplicative transfer factor
preserves the zero identity at each frequency, provided the same transfer factor
really applies across settings. Frequency-dependent factors need not be known
to test this identity; they do matter for interpreting time-domain path orders.

## Reproducible unknown preparation instead of a zero initial state

Fix one stiffness K>0 and source f(t)b. In paired experiments apply +f and -f
from the same unknown initial displacement and velocity. Linearity gives
Qplus=Qhom+Qforced and Qminus=Qhom-Qforced, hence
(Qplus-Qminus)/2=Qforced. The initial homogeneous response cancels exactly.
Repeating this within each intervention setting does not require that the
unknown initial state be the same between different settings, only within each
opposite-source pair. It does require stable K, a linear signed source and
readout, and reproducible pair preparation; no physical reset has been derived.

If the two initial states instead differ by (deltaQ,deltaV), define the difference
energy E=1/2*(deltaV.deltaV+deltaQ.K.deltaQ). Its homogeneous evolution preserves
E. A readout c has residual half-difference bounded uniformly in time by

    |c.deltaQ(t)/2| <= sqrt(E*(c.K^(-1).c)/2).

Proof: Cauchy-Schwarz in the K metric gives
|c.deltaQ|^2 <= (c.K^(-1).c)*(deltaQ.K.deltaQ) <= 2E*(c.K^(-1).c).
This is a valid deterministic certificate if E and K are known or bounded; it is
not an estimate of unobserved preparation errors from endpoint records.

## Finite forcing instead of an ideal impulse

For collocated readout/source e and a rank-one perturbation, let d be the first
nonzero moment mu_d=w^T K^d e. The earlier exact impulse difference has leading
term theta*mu_d^2*t^(4d+3)/(4d+3)!. For a force f(t)=fr*t^r/r! over0<=t<=T,
integer r>=0, convolution and the beta integral give

    response0-response_theta
      = theta*mu_d^2*fr*t^(4d+r+4)/(4d+r+4)! + remainder,
    |remainder| <= 2*M^(2d+2)*|fr|*t^(4d+r+6)/(4d+r+6)!
                   *cosh(sqrt(M)*t),

where M>=max(||K||,||Ktheta||) and0<=t<=T. The positive convolution kernel
bound follows by taking the cosh factor at t outside the integral; exact
integration of (t-s)^(4d+5)*s^r supplies the factorial. If f has further terms,
their convolution must also be bounded; an uncalibrated instrument impulse
response can alter the apparent order. Finite bandwidth/noise and hidden-state
preparation remain experimental obligations. No relativistic propagation speed
or scalar scale follows from this local finite network.

## Actual gain and exact gap

Within the candidate, absolute common gain/offset and affine control zero/scale
are eliminated from the four-setting necessary identity. Exact zero preparation
can be exchanged for reproducible opposite-source preparation, with a bound for
specified mismatch. Neither exchange derives the candidate dynamics or the
physical apparatus assumptions. The next observation route is an independently
characterized variable-coupling system with reserved intervention settings and
paired source trials. A scalar environment application must first show that the
same action and readout produce that response contract. Nothing here derives
Born probabilities, the selected initial ensemble, or a full physical network.
