# QUMOND quadrupole as a linear response functional

Research target: reduce the independently derived three-dimensional Poisson
Hessian to a one-dimensional linear functional of the supplied response nu,
then determine whether monotonic response enforces a sign or a lower bound.
The sign/bound question is open at this freeze. This is a mathematical
reformulation of the same QUMOND candidate, not a refit of its response law.

Use h=Hzz*rM/a0, eta>0, v=1/x and the root independently derived parts form.
Set u=v^2, s=q/eta and t=u/eta. The angular substitution gives
c=(t^2+1-s^2)/(2t), |1-s|<=t<=1+s, and

h=(3/4) eta^(3/2) integral_0^infinity ds s [nu(eta*s)-1] K(s),
K(s)=integral_|1-s|^(1+s) dt t^(-3/2)
 [-t(3c^2-1)+c(5c^2-3)].

Writing d=1-s^2, an algebraic antiderivative candidate is
F(t;s)=-t^(5/2)/20+(3d/4-1)t^(1/2)
 +(d-3d^2/4)t^(-3/2)-5d^3 t^(-7/2)/28.
K=F(1+s;s)-F(|1-s|;s), with the s=1 endpoint limit treated separately.
This formula needs symbolic differentiation, direct angular-kernel checks,
and comparison with the already exposed two-form numerical Hessian. Such
comparison is independent implementation verification, not a blind test.

The prototype will inspect signs at fixed s={.01,.1,.5,.9,.99,1.01,1.1,2,5,10}
and derive piecewise radical forms symbolically. No numerical root or
parameter will be selected from the solar quadrupole observation. Any later
candidate response or optimization requires its own exposure/freeze record.
