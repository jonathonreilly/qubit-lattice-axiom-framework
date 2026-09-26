#!/usr/bin/env python3
"""Full categorical-current checks and a labeled numerical approximation."""
from pathlib import Path
import hashlib,json
import numpy as np
from numpy.polynomial import Chebyshev
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,ok,detail=None):
    if not ok: raise AssertionError((name,detail))
    checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)


def main():
    qs=s.Matrix(s.symbols('q1:4',real=True));gs=s.Matrix(s.symbols('g1:4',real=True))
    rho=sum(qs);F=s.Function('F')(rho)
    Cqq=s.diag(*qs)-qs*qs.T;Cqg=s.diag(*gs)-qs*gs.T;Cgg=s.diag(*qs)-gs*gs.T
    C=Cqq.row_join(Cqg).col_join(Cqg.T.row_join(Cgg))
    R=s.symbols('rho',positive=True);Fp=s.Function('F')(R);D=2*R*Fp+R**2*s.diff(Fp,R)
    axis_slice=dict(zip(qs,[R/3]*3));zero_g=dict(zip(gs,[0]*3))
    K=s.symbols('kx ky kz',real=True);A=s.zeros(6)
    for i in range(3):
        Psi=F*(2*rho-3*qs[i])*gs[i]
        gradient=s.Matrix([s.diff(Psi,x) for x in list(qs)+list(gs)])
        current=C*gradient
        jq=current[:3,0];jg=current[3:,0]
        reduced=current.subs(axis_slice).applyfunc(s.simplify)
        predicted_q=s.ones(3,1)*(1-R)*D*gs[i]/3
        predicted_g=s.Matrix([R**2*Fp*s.KroneckerDelta(i,j)/3
            +(1-R)*(2*Fp+R*s.diff(Fp,R))*gs[i]*gs[j]
            -3*Fp*s.KroneckerDelta(i,j)*gs[i]**2 for j in range(3)])
        check(f'complete_nonlinear_currents_axis_{i}',all(s.simplify(x)==0 for x in reduced-predicted_q.col_join(predicted_g)))
        check(f'invariant_axis_occupation_slice_{i}',all(s.simplify(x)==0 for x in (jq-s.ones(3,1)*sum(jq)/3).subs(axis_slice)))
        jac=current.jacobian(list(qs)+list(gs)).subs(axis_slice).subs(zero_g).applyfunc(s.simplify)
        A+=K[i]*jac
    expected=s.zeros(6)
    top=(1-R)*D*s.ones(3)*s.diag(*K)/3
    bottom=D*s.diag(*K)*s.ones(3)/3
    expected[:3,3:]=top;expected[3:,:3]=bottom
    check('complete_six_field_all_direction_matrix',all(s.simplify(x)==0 for x in A-expected))
    speed2=(1-R)*D**2*sum(k*k for k in K)/3
    check('cubic_minimal_polynomial',all(s.simplify(x)==0 for x in A**3-speed2*A))
    P=R**2*Fp/3
    check('pressure_derivative_acoustic_identity',s.simplify((1-R)*D**2/3-3*(1-R)*s.diff(P,R)**2)==0)

    # Demonstrate C1 approximation on one compact interval. Grid errors below
    # are numerical diagnostics, not certified supremum error bounds.
    interval=(.2,.8);target_c=.4;scale=2*target_c/np.sqrt(3)
    def target_f(x): return 3*scale*(1-np.sqrt(1-x))/x**2
    def target_df(x): return 3*scale*(1/(2*np.sqrt(1-x)*x**2)-2*(1-np.sqrt(1-x))/x**3)
    grid=np.linspace(*interval,10001);records=[]
    for degree in (4,8,12,20):
        derivative=Chebyshev.interpolate(target_df,degree-1,domain=interval)
        approximation=derivative.integ(lbnd=interval[0],k=target_f(interval[0]))
        fp=approximation(grid);dfp=approximation.deriv()(grid)
        speed=np.sqrt((1-grid)/3)*np.abs(2*grid*fp+grid**2*dfp)
        record=dict(degree=degree,tensor_degree=degree+2,maximum_read_footprint=2*(degree+2),
                    max_grid_speed_error=float(np.max(np.abs(speed-target_c))),
                    max_grid_F_error=float(np.max(np.abs(fp-target_f(grid)))),
                    max_grid_derivative_error=float(np.max(np.abs(dfp-target_df(grid)))),
                    chebyshev_coefficients=approximation.coef.tolist())
        records.append(record)
    check('compact_interval_speed_approximation_example',records[-1]['max_grid_speed_error']<1e-6,
          dict(scope='Numerical grid check of a supplied pressure design; not a physical speed derivation.',interval=interval,target_speed=target_c,approximations=records))
    result=dict(checks=checks,count=len(checks),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                scope='Full symbolic current identities plus an explicitly chosen numerical pressure target. No empirical physical prediction or continuum limit with increasing range.')
    (HERE/'ACOUSTIC_PRESSURE_DESIGN_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('TOTAL:',len(checks),'PASS',flush=True)


if __name__=='__main__': main()
