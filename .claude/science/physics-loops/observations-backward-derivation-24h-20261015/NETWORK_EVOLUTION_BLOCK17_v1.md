# Several adaptive neighbors: a sign test without choosing one mode

This extends the explicit block15 candidate, not observed quantum theory.
It removes the chosen single hidden oscillator from a necessary frequency
constraint. The positive-energy quadratic hidden sector, coupling form,
stationarity and measurement identification remain supplied. Standard positive
Gram and divided-difference algebra is used; there is no mathematical novelty
claim for that machinery and no empirical validation.

## Explicit finite class and its stability condition

Take any finite number of hidden coordinates w_j, with tau_j,C_j>0:

    V=k*q^2/2 + sum_j [C_j*w_j^2/2+g_j*w_j*q^2/2]
      +lambda4*q^4,  k>0,
    T=m*qdot^2/2+sum_j tau_j*wdot_j^2/2,  m>0.

Completing each square gives boundedness and coercivity exactly when

    lambda4 >= sum_j g_j^2/(8*C_j).

This is an inequality on an allowed action family. No argument prefers its
boundary, selects a number of modes, or fixes their scales.

For a prescribed positive-frequency q=A*cos(omega*t), require the periodic
particular hidden solution and exclude every 2omega=sqrt(C_j/tau_j).
The third-harmonic force coefficient divided by A^3 is

    B(x)=lambda4-sum_j a_j/(s_j-x),
    x=4*omega^2, s_j=C_j/tau_j>0, a_j=g_j^2/(8*tau_j)>=0.

Zero residues are omitted and equal s_j may be combined. This follows by
linearity of each hidden forced equation plus the same cubic trigonometric
products as block15. Arbitrary homogeneous hidden modes do not decay in this
conservative class. Identifying a measured harmonic with B requires the
particular branch, or a separately justified transient-removal method.
Block16 supplies a state-free time-domain identity for the one-mode candidate;
it does not automatically certify the multi-mode harmonic readout.

## Four distinct frequencies and a two-by-two determinant

Choose two ordered row settings x1<x2 and two ordered column settings y1<y2,
all four distinct, nonnegative, and below every coupled s_j. For actual
separate harmonics they are strictly positive. Define

    L_ij = -(B(x_i)-B(y_j))/(x_i-y_j)
         = sum_j a_j/[(s_j-x_i)*(s_j-y_j)].

The bare quartic lambda4 cancels. For two distinct poles s_p<s_q the
two-column Cauchy determinant in the x settings is

    -(x2-x1)*(s_q-s_p) /
       product_(i=1,2) [(s_p-x_i)*(s_q-x_i)].

The y determinant has the same negative sign. Expanding det(L) by pairs
of columns therefore gives

    det(L) = sum_(p<q) a_p*a_q*(x2-x1)*(y2-y1)*(s_q-s_p)^2 /
       {product_i[(s_p-x_i)*(s_q-x_i)] *
        product_j[(s_p-y_j)*(s_q-y_j)]} >= 0.

Every denominator is positive in the stated below-pole domain. The determinant
is zero for zero or one distinct coupled frequency, and strictly positive
for at least two positive residues at distinct frequencies. This tests the
chosen one-mode reduction without fixing an alternative number of modes.
It also gives a necessary sign restriction on this entire finite passive
adaptive class. It does not exclude other kinds of evolving networks.

Replacing B by a common real affine readout u+v*B multiplies L by v and the
determinant by v^2. The sign and exact zero survive; v=0 loses all information.
Frequency-dependent gain, complex phase, changing offsets or nonlinear
readout can spoil the test and must not be treated as already cancelled.
The pole-free interval is an additional physical condition, not inferred
from a successful four-point check.

## Finite deterministic uncertainty

For known settings and measured B values with pointwise errors eps_z,
the entry error is

    e_ij=(eps_xi+eps_yj)/|x_i-y_j|.

Let Lhat use the measured values. A determinant error bound is

    E=|Lhat11|*e22+|Lhat22|*e11+e11*e22
      +|Lhat12|*e21+|Lhat21|*e12+e12*e21.

This follows from expanding each perturbed product. Correlations between
shared measurements are allowed. Lhat determinant below -E conflicts with
the stated passive class and measurement contract. A value above E rejects
its zero-or-one-pole subclass, within that same contract. A value inside the
interval is inconclusive; it does not establish a one-mode world.
Uncertain frequencies, errors in extracting a harmonic and unbounded
transients require additional bounds.

## A local spectral check, with a different observational burden

For |x|<min s_j, expand B=lambda4-sum_(n>=0) M_n*x^n, where
M_n=sum_j a_j/s_j^(n+1). The first three nonconstant coefficients obey

    M1*M3-M2^2 >= 0.

Indeed set weights rho_j=a_j/s_j^2 and h_j=1/s_j; the expression is
(sum rho)*(sum rho*h^2)-(sum rho*h)^2. Equality means at most one
distinct h carrying positive weight. Derivatives or a controlled analytic
fit are needed to obtain these coefficients; four separated frequency
measurements are not secretly derivatives. The static coefficient
lambda4-M0 remains free and stability only bounds it below by zero.

The useful observation-first direction is to estimate one common response
on development histories, then test these necessary multi-mode restrictions
on reserved rate and amplitude settings with a frozen readout model. A
chosen number of hidden modes or a preferred spectral shape is not a
derivation of the network.
