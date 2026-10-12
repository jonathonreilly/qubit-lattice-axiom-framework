#!/usr/bin/env python3
"""Symbolic and numerical prototype for a QUMOND quadrupole response kernel."""
import json
import mpmath as mp
import sympy as sp
mp.mp.dps=70
t,s=sp.symbols('t s',positive=True)
d=1-s*s
c=(t*t+d)/(2*t)
raw=t**(-sp.Rational(3,2))*(-t*(3*c*c-1)+c*(5*c*c-3))
F=-t**sp.Rational(5,2)/20+(3*d/4-1)*sp.sqrt(t)+(d-3*d*d/4)*t**(-sp.Rational(3,2))-5*d**3*t**(-sp.Rational(7,2))/28
assert sp.simplify(sp.diff(F,t)-raw)==0
branches={}
for side,lo in [('below',1-s),('above',s-1)]:
 k=sp.simplify(F.subs(t,1+s)-F.subs(t,lo))
 branches[side]=str(k)
print(json.dumps({'derivative_identity':True,'symbolic_kernel':branches},indent=2))
def antider(t,s):
 d=1-s*s
 return -t**mp.mpf('2.5')/20+(3*d/4-1)*mp.sqrt(t)+(d-3*d*d/4)/t**mp.mpf('1.5')-5*d**3/(28*t**mp.mpf('3.5'))
def kernel(s):return antider(1+s,s)-antider(abs(1-s),s)
rows=[]
for ss in ['.01','.1','.5','.9','.99','1.01','1.1','2','5','10']:
 q=mp.mpf(ss);k=kernel(q)
 def integrand(tt):
  cc=(tt*tt+1-q*q)/(2*tt)
  return tt**(-mp.mpf('1.5'))*(-tt*(3*cc*cc-1)+cc*(5*cc*cc-3))
 direct=mp.quad(integrand,[abs(1-q),1+q])
 rows.append({'s':ss,'kernel':mp.nstr(k,40),'direct_error':mp.nstr(abs(k-direct),8)})
print(json.dumps({'kernel_samples':rows},indent=2))
# Piecewise primitive of s*K(s) is the step-response kernel, if integrable.
for side,lo in [('below',1-s),('above',s-1)]:
 k=F.subs(t,1+s)-F.subs(t,lo)
 # Explicit radical expansion lets the elementary power antiderivative operate.
 terms=sp.expand(s*k)
 integ=sp.integrate(terms,s)
 print('PRIMITIVE_'+side+' '+str(integ))
