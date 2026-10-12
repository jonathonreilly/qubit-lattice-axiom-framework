#!/usr/bin/env python3
import sympy as sp
s,z=sp.symbols('s z',positive=True)
p=12*s**3-6*s*s+s-2
q=12*s**3+6*s*s+s+2
Ip=sp.integrate(2*(z*z+1)*p.subs(s,z*z+1),z)
Im=sp.integrate(-2*(1-z*z)*p.subs(s,1-z*z),z)
Iq=sp.integrate(2*(z*z-1)*q.subs(s,z*z-1),z)
above=sp.Rational(4,35)*(Ip.subs(z,sp.sqrt(s-1))-Iq.subs(z,sp.sqrt(s+1)))
below=-sp.Rational(4,35)*(Im.subs(z,sp.sqrt(1-s))+Iq.subs(z,sp.sqrt(s+1)))
print('ABOVE',sp.factor(above))
print('BELOW',sp.factor(below))
print('AT_ZERO',sp.simplify(below.subs(s,0)))
print('CONTINUITY',sp.simplify(below.subs(s,1)-above.subs(s,1)))
print('INFINITY',sp.limit(above,s,sp.oo))
print('KPLUS_POSITIVITY',sp.factor(p*p*(s+1)-q*q*(s-1)))
print('KMINUS_SIGN',sp.factor(q*q*(1-s)-p*p*(1+s)))
print('A_SMALL',sp.series(below,s,0,8))
print('A_LARGE',sp.series(above.subs(s,1/z),z,0,4))
