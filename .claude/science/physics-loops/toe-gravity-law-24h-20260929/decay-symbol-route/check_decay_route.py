#!/usr/bin/env python3
"""Small exact controls for a new conditional decay-symbol discovery.

This is not an independent review of the preceding finite-support report.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json,time
import sympy as s

HERE=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')

def budget():
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
    assert not (RUNTIME/'STOP_REQUESTED.json').exists()

def mat(prefix):return s.Matrix(2,2,s.symbols(prefix+'0:4'))

def matrix_control():
    D,F,A,Ds,L=map(mat,('d','f','a','b','l'))
    m0,m1=s.symbols('m0 m1');I=s.eye(2);Fi=F.inv()
    R0=D*F+F*Ds-m0*F
    RA=L*F+D*A+A*Ds-m0*A-m1*F
    # Do not assume any pair of matrices commutes, or Ds=-D.
    expected=L+D*A*Fi-A*Fi*D-m1*I
    actual=(RA-A*Fi*R0)*Fi
    assert (actual-expected).applyfunc(s.cancel)==s.zeros(2)
    assert s.cancel(s.trace(expected)-s.trace(L)+2*m1)==0
    return {'generic_noncommuting_elimination':True,'trace_commutator':True}

def stencil_control():
    out=[]
    for R in range(1,7):
        a={r:Q(2*(-1)**(r+1)*factorial(R)**2,
               r*factorial(R-r)*factorial(R+r)) for r in range(1,R+1)}
        assert sum(c*r for r,c in a.items())==1
        for j in range(1,R):assert sum(c*r**(2*j+1) for r,c in a.items())==0
        lead=sum(c*r**(2*R+1) for r,c in a.items())
        assert lead==(-1)**(R+1)*factorial(R)**2
        deriv_lead=(-1)**R*lead/Q(factorial(2*R))
        assert deriv_lead==-Q(factorial(R)**2,factorial(2*R))
        out.append({'R':R,'coefficients':[str(a[r]) for r in a],
                    'leading_derivative_residual':str(deriv_lead),
                    'Taylor_bound_coefficient':str(sum(abs(c)*r**(2*R+1) for r,c in a.items())/factorial(2*R))})
    return out

def bump_control():
    k=s.symbols('k',real=True);t=2*k-1
    transition=k*(1-10*t**3+15*t**4-6*t**5)
    for j in range(3):
        assert s.diff(transition,k,j).subs(k,s.Rational(1,2))==s.diff(k,k,j).subs(k,s.Rational(1,2))
        assert s.diff(transition,k,j).subs(k,1)==0
    f=(1-4*k*k)**4
    for j in range(4):assert s.diff(f,k,j).subs(k,s.Rational(1,2))==0
    # On the support of f, d=k exactly; outside it f=0.
    D=s.I*k;F=f;A=-s.I*s.diff(f,k)/2
    assert s.simplify(D*F+F*s.conjugate(D))==0
    assert s.simplify(A-s.conjugate(A)+s.I*s.diff(F,k))==0
    assert s.simplify(-s.I*s.diff(D,k)*F+D*A+A*s.conjugate(D)-F)==0
    assert F.subs(k,0)==1
    return {'explicit_piecewise_polynomial_D_C2':True,'F_C3':True,
            'first_absolute_Fourier_moments_finite_by_three_integrations_by_parts':True,
            'reduced_uniform_and_affine_equations':True,'F0':1,
            'kinetic_zero_region':'|k|>=1/2','full_algebra_completion':False}

def slac_control():
    def kernel(r):return Q(0) if r==0 else Q(1 if r%2 else -1,r)
    profiles=[{0:(Q(1),Q(0))},
              {-2:(Q(1,3),Q(2)),0:(Q(-3),Q(1,4)),3:(Q(2),Q(-1))},
              {-4:(Q(2),Q(1)),1:(Q(-2,7),Q(3)),4:(Q(1),Q(-2))},
              {0:(Q(1),Q(2)),1:(Q(1),Q(2))}]
    out=[]
    for p in profiles:
        bracket=sum(sum(p[x][c]*kernel(y-x)*y*p[y][c] for c in range(2)) for x in p for y in p)
        target=sum(v*v for pair in p.values() for v in pair)/2
        alternating=[sum((1 if x%2==0 else -1)*v[c] for x,v in p.items()) for c in range(2)]
        expected=-sum(v*v for v in alternating)/2
        assert bracket-target==expected
        out.append({'bracket':str(bracket),'target':str(target),'defect':str(expected),
                    'alternating_moment':[str(v) for v in alternating]})
    return out

def main():
    budget();start=time.time()
    out={'matrix':matrix_control(),'stencils':stencil_control(),
         'summable_counterexample':bump_control(),'SLAC_compact_fields':slac_control()}
    budget();out['elapsed_seconds']=time.time()-start
    (HERE/'results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
