#!/usr/bin/env python3
"""Direct-parent perturbation and initial-condition calculations; H0=c=1."""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import sys
import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm
import sympy as sy

ROOT = Path(__file__).resolve().parent
FIX = json.loads((ROOT / 'NUMERICAL_FIXTURES.json').read_text())
CHECKS = []


def check(name, passed, **detail):
    CHECKS.append(dict(name=name, passed=bool(passed), **detail))


def bg(N, a, m=FIX['m']):
    matter = m * np.exp(-3 * N)
    H = np.sqrt(matter + 1 - m)
    Om = matter / H**2
    D = 1.5 * Om / (1 + a)
    return H, -1.5 * Om, D, np.sqrt(a * D)


def symbolic_controls():
    s, D, x, Q, eta = sy.symbols('s D x Q eta', nonzero=True)
    P, d, T, u, c, wu, wc = sy.symbols('P d T u c wu wc')
    h = -(1 + s*s)*D
    pp = -P + D*T/Q + x*c
    rhs = {D:(-3-2*h)*D, x:(-sy.Rational(3,2)-h)*x,
           Q:-2*(1+h)*Q, P:pp, d:-T+3*pp,
           T:-(2+h)*T+Q*(P+s*u), u:wu, c:wc,
           wu:-(3+h)*wu-(Q+(1+eta+s*s)*D)*u-3*x*c/s-D*s*d,
           wc:-(3+h)*wc-3*x*u/s-(Q+sy.Rational(9,4)
               +sy.Rational(3,2)*(1+s*s)*D)*c+4*x*pp+3*x*P}
    derivative = lambda v: sum(sy.diff(v,z)*rz for z,rz in rhs.items())
    reduce = lambda v: sy.factor(v.subs(D,x*x/(s*s)))
    constraint = (Q-x*x)*P+D*d+3*D*T/Q+x*wc+sy.Rational(3,2)*x*c
    identities = {
        'constraint_propagation':reduce(derivative(constraint)-(-3-2*h)*constraint),
        'spatial_trace':reduce(derivative(pp)+(4+h)*pp+(3+2*h)*P
                       -x*wc+x*x*P-sy.Rational(3,2)*x*c-D*s*u),
        'Jordan_number_conservation':sy.expand((-T+3*pp)-3*s*wu
                                               -(-T+3*(pp-s*wu))),
        'physical_density_from_rest_density':sy.expand(d+s*u-4*s*u-(d-3*s*u))}
    for name, value in identities.items():check(name, value==0)
    return {k:str(v) for k,v in identities.items()}


def growing_integral(N, m=FIX['m']):
    R = np.exp(N)
    b = (1-m)*R**3/m
    J = quad(lambda t: t**1.5/(1+b*t**3)**1.5, 0, 1,
             epsabs=1e-12, epsrel=1e-12)[0]
    I = R**2.5 * J / m**1.5
    H, h, _, _ = bg(N,0,m)
    return 2.5*m*H*I, h+1/(R**2 * H**3 * I)


def growth_controls():
    def rhs(N,z):
        _,h,D,_=bg(N,0)
        return [z[1],-(2+h)*z[1]+D*z[0]]
    sol=solve_ivp(rhs,(FIX['growth_initial_N'],0),FIX['growth_ode_initial'],
                  method='DOP853',rtol=2e-12,atol=2e-14,max_step=.02,dense_output=True)
    check('growth_integrator_success',sol.success)
    rows=[]
    for N in FIX['linear_sites_N']:
        g,fg=growing_integral(N); y=sol.sol(N); fgode=y[1]/y[0]
        check('growth_integral_ODE_'+str(N),abs(fg-fgode)<FIX['growth_compare_tolerance'])
        rows.append(dict(N=N,Dg_integral=g,fg_integral=fg,fg_ode=fgode))
    return rows


def linear_rhs(N,z,a,eta,q0):
    H,h,D,x=bg(N,a);Q=(q0/(np.exp(N)*H))**2;s=np.sqrt(a)
    P,d,T,u,c,wu,wc=z
    pp=-P+D*T/Q+x*c
    out=np.empty_like(z)
    out[0]=pp;out[1]=-T+3*pp;out[2]=-(2+h)*T+Q*(P+s*u)
    out[3]=wu;out[4]=wc
    out[5]=-(3+h)*wu-(Q+(1+eta+a)*D)*u-3*np.sqrt(D)*c-D*s*d
    out[6]=-(3+h)*wc-3*np.sqrt(D)*u-(Q+2.25+1.5*(1+a)*D)*c+4*x*pp+3*x*P
    return out


def initialize_constraint(N,z,a,q0):
    H,_,D,x=bg(N,a);Q=(q0/(np.exp(N)*H))**2
    z[0]=-(D*z[1]+3*D*z[2]/Q+x*z[6]+1.5*x*z[4])/(Q-x*x)
    return z


def constraint_terms(N,z,a,q0):
    H,_,D,x=bg(N,a);Q=(q0/(np.exp(N)*H))**2
    return np.array([(Q-x*x)*z[0],D*z[1],3*D*z[2]/Q,x*z[6],1.5*x*z[4]])


def solve_linear(z0,a,eta,q0,refinement):
    shape=z0.shape
    def rhs(N,z):return linear_rhs(N,z.reshape(shape),a,eta,q0).reshape(-1)
    return solve_ivp(rhs,FIX['linear_interval_N'],z0.reshape(-1),method='DOP853',
                     rtol=FIX['linear_rtol'][refinement],atol=FIX['linear_atol'][refinement],
                     max_step=FIX['linear_max_steps'][refinement],dense_output=True)


def linear_basis_controls():
    rows=[]; Ni=FIX['linear_interval_N'][0]; sites=np.array(FIX['linear_sites_N'])
    for a in FIX['a_weak']:
        for eta in FIX['linear_eta']:
            for q0 in FIX['linear_q0']:
                z0=np.zeros((7,6));z0[1:]=np.diag([1,1,np.sqrt(a),np.sqrt(a),np.sqrt(a),np.sqrt(a)])
                initialize_constraint(Ni,z0,a,q0)
                histories=[]
                for r in range(2):
                    sol=solve_linear(z0,a,eta,q0,r)
                    check(f'linear_success_{a}_{eta}_{q0}_{r}',sol.success)
                    ys=sol.sol(sites).reshape(7,6,len(sites)); histories.append(ys)
                    for j,N in enumerate(sites):
                        terms=constraint_terms(N,ys[:,:,j],a,q0)
                        residual=np.abs(terms.sum(axis=0))/(1+np.abs(terms).sum(axis=0))
                        check(f'linear_constraint_{a}_{eta}_{q0}_{r}_{j}',
                              np.max(residual)<FIX['constraint_relative_tolerance'],
                              max_scaled_residual=float(np.max(residual)))
                difference=np.abs(histories[1]-histories[0])
                scale=FIX['linear_refinement_atol']+FIX['linear_refinement_rtol']*np.maximum(np.abs(histories[0]),np.abs(histories[1]))
                check(f'linear_refinement_{a}_{eta}_{q0}',np.max(difference/scale)<=1,
                      maximum_tolerance_units=float(np.max(difference/scale)))
                rows.append(dict(a=a,eta=eta,q0=q0,initial=z0.tolist(),sites=sites.tolist(),
                                 coarse=histories[0].tolist(),fine=histories[1].tolist(),
                                 endpoint_response_singular_values=np.linalg.svd(histories[1][:,:,-1],compute_uv=False).tolist()))
    return rows


def slow_matter_controls():
    rows=[];Ni=FIX['linear_interval_N'][0]; sites=np.array(FIX['linear_sites_N'])
    fg0=growing_integral(Ni)[1]
    for a in FIX['high_k_a']:
        for q0 in FIX['high_k_q0']:
            H,_,D,_=bg(Ni,a);Q=(q0/(np.exp(Ni)*H))**2
            pl=-D/Q;u=np.sqrt(a)*pl
            z0=np.array([0.,1.,-fg0+3*(fg0-1)*pl,u,0.,(fg0-1)*u,0.])
            initialize_constraint(Ni,z0,a,q0)
            histories=[]
            for r in range(2):
                sol=solve_linear(z0,a,FIX['high_k_eta'],q0,r)
                check(f'slow_matter_success_{a}_{q0}_{r}',sol.success)
                histories.append(sol.sol(sites))
            scale=FIX['linear_refinement_atol']+FIX['linear_refinement_rtol']*np.maximum(np.abs(histories[0]),np.abs(histories[1]))
            check(f'slow_matter_refinement_{a}_{q0}',np.max(np.abs(histories[1]-histories[0])/scale)<=1)
            points=[]
            for j,N in enumerate(sites):
                z=histories[1][:,j];zp=linear_rhs(N,z,a,3,q0)
                H,_,D,_=bg(N,a);Q=(q0/(np.exp(N)*H))**2
                P,d,T,u,c,wu,wc=z;zet=np.sqrt(a)*u;deltaJ=d-3*zet
                psi=P+zet;phi=P-zet
                mu=-Q*psi/((1+a)*D*deltaJ);Sigma=-Q*P/((1+a)*D*deltaJ)
                gamma=phi/psi;fg=(zp[1]-3*np.sqrt(a)*wu)/deltaJ
                terms=constraint_terms(N,z,a,q0)
                check(f'slow_constraint_{a}_{q0}_{j}',abs(terms.sum())/(1+abs(terms).sum())<FIX['constraint_relative_tolerance'])
                points.append(dict(N=float(N),Q=float(Q),mu=float(mu),Sigma=float(Sigma),gamma=float(gamma),
                                   fg_J=float(fg),fg_regular_GR=growing_integral(N)[1],state=z.tolist()))
            target=dict(mu=1.,Sigma=1/(1+a),gamma=(1-a)/(1+a))
            for k in FIX['high_k_comparisons']:
                err=abs(points[-1][k]-target[k]);bound=FIX['high_k_endpoint_error_bound_coefficient']/q0**2
                check(f'finite_asymptotic_control_{a}_{q0}_{k}',err<=bound,absolute_error=err,declared_bound=bound)
            rows.append(dict(a=a,q0=q0,eta=3,initial=z0.tolist(),points=points,limiting_coefficients=target))
    return rows


def potential(phi,a,eta,m=FIX['m']):
    s=np.sqrt(a);vl=1.5*(1-m);k=np.sqrt(1.5*(1+a)/a);c=vl/(1+a)
    chic=np.arcsinh(np.sqrt(m/(1-m)))/k;u,ch=phi
    z=k*(ch-chic);S=c*np.sinh(z)**2;Sp=c*k*np.sinh(2*z);Spp=2*c*k*k*np.cosh(2*z)
    F=(u-s)**2+eta*u*u;B=(1+eta)*u-s
    V=vl+.5*S*F;grad=np.array([S*B,.5*Sp*F])
    Hess=np.array([[(1+eta)*S,Sp*B],[Sp*B,.5*Spp*F]])
    return V,grad,Hess


def homogeneous_rhs_jac(Y,a,eta):
    phi=Y[:2];v=Y[2:4];sig=np.exp(Y[4]);alpha=np.array([np.sqrt(a),0.])
    V,gV,Hess=potential(phi,a,eta);H=np.sqrt((2*sig+v@v+2*V)/3)
    g=gV+alpha*sig;F=np.concatenate((v/H,-3*v-g/H,[-3+alpha@v/H]))
    dh=np.concatenate((gV,v,[sig]))/(3*H*H)
    Jac=np.zeros((5,5),dtype=np.result_type(Y))
    Jac[:2,2:4]=np.eye(2)/H;Jac[:2]-=np.outer(v/H,dh)
    Jac[2:4,:2]=-Hess/H;Jac[2:4,2:4]=-3*np.eye(2);Jac[2:4,4]=-alpha*sig/H
    Jac[2:4]+=np.outer(g/H,dh);Jac[4]=alpha@Jac[:2]
    return F,Jac,H


def homogeneous_initial(N,a):
    m=FIX['m'];k=np.sqrt(1.5*(1+a)/a);chic=np.arcsinh(np.sqrt(m/(1-m)))/k
    chi=chic-np.arcsinh(np.sqrt(m/(1-m))*np.exp(-1.5*N))/k
    sig=1.5*m*np.exp(-3*N)/(1+a)
    return np.array([0.,chi,0.,np.sqrt(a*sig),np.log(sig)])


def homogeneous_controls():
    rows=[];Ni,Nf=FIX['homogeneous_interval_N'];sites=np.array(FIX['homogeneous_sites_N'])
    for a in FIX['homogeneous_a']:
        for eta in FIX['homogeneous_eta']:
            Y0=homogeneous_initial(Ni,a);F,J,H=homogeneous_rhs_jac(Y0,a,eta)
            cs=np.column_stack([np.imag(homogeneous_rhs_jac(Y0.astype(complex)+1e-27j*np.eye(5)[j],a,eta)[0])/1e-27 for j in range(5)])
            check(f'analytic_homogeneous_jacobian_{a}_{eta}',np.allclose(J,cs,rtol=2e-11,atol=2e-11),max_error=float(np.max(abs(J-cs))))
            scales=np.array([np.sqrt(a),np.sqrt(a),np.sqrt(a)*H,np.sqrt(a)*H,1.])
            def vari_rhs(N,z):
                Y=z[:5];F,J,_=homogeneous_rhs_jac(Y,a,eta)
                return np.concatenate((F,(J@z[5:].reshape(5,5)).reshape(-1)))
            vsol=solve_ivp(vari_rhs,(Ni,Nf),np.concatenate((Y0,np.diag(scales).reshape(-1))),method='DOP853',
                          rtol=FIX['homogeneous_rtol'][1],atol=FIX['homogeneous_atol'][1],max_step=FIX['homogeneous_max_steps'][1],dense_output=True)
            check(f'variational_success_{a}_{eta}',vsol.success)
            vari=vsol.sol(sites);mat=vari[5:].reshape(5,5,len(sites));runs=[]
            for axis in range(5):
                for eps in FIX['homogeneous_eps']:
                    results=[]
                    for r in range(2):
                        signs=[]
                        for sign in [-1,1]:
                            initial=Y0.copy();initial[axis]+=sign*eps*scales[axis]
                            sol=solve_ivp(lambda N,Y:homogeneous_rhs_jac(Y,a,eta)[0],(Ni,Nf),initial,method='DOP853',
                                  rtol=FIX['homogeneous_rtol'][r],atol=FIX['homogeneous_atol'][r],max_step=FIX['homogeneous_max_steps'][r],dense_output=True)
                            check(f'homogeneous_success_{a}_{eta}_{axis}_{eps}_{r}_{sign}',sol.success)
                            signs.append(sol.sol(sites))
                        results.append(np.array(signs))
                    central=(results[1][1]-results[1][0])/(2*eps)
                    scaled_error=np.max(abs(central-mat[:,axis,:])/scales[:,None])
                    check(f'homogeneous_variation_{a}_{eta}_{axis}_{eps}',scaled_error<FIX['homogeneous_variation_scaled_error_tolerance'],maximum_scaled_error=float(scaled_error))
                    re=np.max(abs(results[0]-results[1])/scales[None,:,None])
                    check(f'homogeneous_refinement_{a}_{eta}_{axis}_{eps}',re<FIX['homogeneous_refinement_scaled_tolerance'],maximum_scaled_error=float(re))
                    endpoints=[]
                    for ii,sign in enumerate([-1,1]):
                        Y=results[1][ii,:,-1];A=np.exp(np.sqrt(a)*Y[0]);Ff,_,Hf=homogeneous_rhs_jac(Y,a,eta)
                        drift=2*np.sqrt(a)*Y[2]/A*FIX['H0_per_second_illustrative']*FIX['seconds_per_year_supplied']
                        endpoints.append(dict(sign=sign,u=float(Y[0]),u_over_initial_scalar_scale=float(Y[0]/np.sqrt(a)),
                                              G_ratio_to_u_zero=float(A*A),drift_per_year=float(drift),H_J_over_H0=float((Hf+np.sqrt(a)*Y[2])/A)))
                    runs.append(dict(axis=axis,eps=eps,coarse=results[0].tolist(),fine=results[1].tolist(),
                                     maximum_scaled_variation_error=float(scaled_error),endpoints=endpoints))
            rows.append(dict(a=a,eta=eta,sites=sites.tolist(),initial=Y0.tolist(),scales=scales.tolist(),
                             variational=vari.tolist(),nonlinear_runs=runs))
    return rows


def de_sitter_controls():
    L=np.sqrt(1-FIX['m']);A=np.array([[0,1,0,0],[0,-3*L,0,0],[0,0,0,1],[0,0,-2.25*L*L,-3*L]])
    rows=[]
    for t in [0,.1,1,4,8]:
        U=expm(A*t);E=np.zeros((4,4));e=np.exp(-3*L*t);f=np.exp(-1.5*L*t)
        E[:2,:2]=[[1,(1-e)/(3*L)],[0,e]]
        E[2:,2:]=f*np.array([[1+1.5*L*t,t],[-2.25*L*L*t,1-1.5*L*t]])
        check('vacuum_modes_'+str(t),np.allclose(U,E,rtol=2e-12,atol=2e-13))
        rows.append(dict(t=t,matrix=U.tolist(),neutral_mode=U[:,0].tolist()))
    return rows


def empirical_summary():
    N=-np.log1p(FIX['EG_z']);_,fg=growing_integral(N)
    rows=[]
    for a in [0]+FIX['a_weak']:
        prediction=FIX['m']/((1+a)*fg)
        rows.append(dict(a=a,m=FIX['m'],z=FIX['EG_z'],fg=fg,EG=prediction,
                         difference_from_same_m_GR=prediction-FIX['m']/fg,
                         observed_summary=FIX['EG_summary'],reported_uncertainty=FIX['EG_reported_uncertainty'],
                         standardized_summary_residual=(prediction-FIX['EG_summary'])/FIX['EG_reported_uncertainty']))
    check('EG_endpoint_fractional_difference',abs(rows[-1]['EG']/rows[0]['EG']-2499/2500)<2e-15)
    return dict(role=FIX['EG_data_role'],source=FIX['EG_source'],rows=rows,
                additional_lensing_calibration_fraction_not_combined=FIX['EG_additional_lensing_calibration_fraction'],
                limitations='No raw estimator/covariance or revised geometry/nonlinear corrections. Scale-independent slowly varying matter mode and same-tracer bridges supplied.')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    out=dict(author='direct parent',versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=sy.__version__),
             source_sha256={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ['PROTOCOL.md','DIRECT_PERTURBATION_RESPONSE.md','NUMERICAL_FIXTURES.json','check_perturbation_response.py']})
    for name,fn in [('symbolic',symbolic_controls),('growth',growth_controls),('linear_basis',linear_basis_controls),
                    ('slow_matter',slow_matter_controls),('homogeneous',homogeneous_controls),('de_sitter',de_sitter_controls),('EG_summary',empirical_summary)]:
        print('START',name,flush=True);out[name]=fn();print('DONE',name,flush=True)
    out['checks']=CHECKS;out['checks_count']=len(CHECKS);out['all_passed']=all(c['passed'] for c in CHECKS)
    Path(args.output).write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(checks_count=len(CHECKS),all_passed=out['all_passed'],failures=[x for x in CHECKS if not x['passed']])),flush=True)
    if not out['all_passed']:sys.exit(1)


if __name__=='__main__':main()
