"""Conditional action inverse with shared, already checked synthetic port generator."""
AUDIT_TIMEOUT_SEC=120
import contextlib
import hashlib
import io
import json
from pathlib import Path
import runpy

import numpy as np
from scipy.integrate import cumulative_simpson
from scipy.optimize import least_squares
import sympy as s

root=Path(__file__).resolve().parent
dep=root/'check_common_action_ringdown_v2.py'
buffer=io.StringIO()
with contextlib.redirect_stdout(buffer):
    parent=runpy.run_path(str(dep))
parent_result=json.loads(buffer.getvalue())
assert parent_result['summary']['failed']==0
rows=[];details={}
def ck(name,condition,detail=None):
    rows.append({'name':name,'passed':bool(condition),'detail':detail})

# Direct change of coordinates in both quadratic velocity forms and potential.
xd,vd,v,F,Fp=s.symbols('xd vd v F Fp',real=True)
M,k,tau,d,nu,gamma,U,B,C=s.symbols('M k tau d nu gamma U B C',real=True)
kin=s.expand(M*xd**2/2+k*xd*(vd+Fp*xd)+tau*(vd+Fp*xd)**2/2).subs(Fp,-k/tau)
ray=s.expand(d*xd**2/2+nu*xd*(vd+Fp*xd)+gamma*(vd+Fp*xd)**2/2).subs(Fp,-k/tau)
pot=s.expand(U+B*(v+F)+C*(v+F)**2/2)
ck('kinetic_cross_removed_by_coordinate_change',s.simplify(s.expand(kin).coeff(xd,1).coeff(vd,1))==0)
ck('visible_mass_Schur_complement',s.simplify(s.expand(kin).coeff(xd,2)*2-(M-k*k/tau))==0)
ck('damping_cross_retained',s.simplify(s.expand(ray).coeff(xd,1).coeff(vd,1)-(nu-gamma*k/tau))==0)
ck('damping_diagonal_transformed',s.simplify(s.expand(ray).coeff(xd,2)*2-(d-2*nu*k/tau+gamma*k*k/tau**2))==0)
ck('potential_translation',s.simplify(pot-(U+B*F+C*F*F/2+(B+C*F)*v+C*v*v/2))==0)
ck('damping_determinant_preserved',s.simplify((d-2*nu*k/tau+gamma*k*k/tau**2)*gamma-(nu-gamma*k/tau)**2-(d*gamma-nu**2))==0)
ss,Ga,O,G=s.symbols('s Gamma O G',real=True)
oldN=G+nu*ss+k*ss*ss
newN=G-k*O+(nu-k*Ga)*ss
ck('same_pole_off_diagonal',s.expand(oldN-newN-k*(ss*ss+Ga*ss+O))==0)

# Static curvature is along the equilibrium curve, not at fixed hidden w.
x=s.symbols('x',real=True); E=s.Function('E')(x); cc=s.Function('C')(x); w0=s.Function('w0')(x)
VV=E+cc*(v-w0)**2/2
Gcan=-cc*s.diff(w0,x)
ck('equilibrium_holding_force',s.simplify(s.diff(VV,x).subs(v,w0)-s.diff(E,x))==0)
ck('fixed_hidden_curvature',s.simplify(s.diff(VV,x,2).subs(v,w0)-(s.diff(E,x,2)+Gcan**2/cc))==0)


def features(env,initial=(.31,-.22)):
    a,zv,t,force,truth=parent['synthetic_records'](env,initial)
    fit=parent['extract'](a,zv,t,force)
    la=fit['pole'];ga=fit['Gamma'];om=la.imag
    basis=np.column_stack([np.ones_like(t),np.exp(-ga*t/2)*np.cos(om*t),np.exp(-ga*t/2)*np.sin(om*t),np.exp(-ga*t),np.exp(-ga*t)*np.cos(2*om*t),np.exp(-ga*t)*np.sin(2*om*t)])
    coeff=np.linalg.lstsq(basis,force,rcond=None)[0]
    fit['g']=(coeff[4]-1j*coeff[5])/2;fit['R0']=coeff[0]
    fit['S']=-2*(2*la+ga)*fit['residue']*fit['g']/fit['f']**2
    fit['r']=(fit['S']-fit['Q'])/(fit['O']-la*la)
    return fit,a,zv,t,force,truth


grid=np.linspace(-.8,1.,61)
records=[features(float(xx)) for xx in grid]
fitrows=[r[0] for r in records]
rr=np.array([z['r'] for z in fitrows])
tx=parent['tx'];px=parent['x']; getpar=parent['getpar']
actual_tau=np.array([getpar(float(xx))[0] for xx in grid],dtype=float)
actual_r=np.array([getpar(float(xx))[9]/getpar(float(xx))[0] for xx in grid],dtype=float)
tau_recovered=np.exp(cumulative_simpson(rr.real,x=grid,initial=0))
ck('observed_r_is_real',np.max(abs(rr.imag))<2e-9,float(np.max(abs(rr.imag))))
ck('inertia_log_derivative_recovered',np.max(abs(rr.real-actual_r))<2e-9,float(np.max(abs(rr.real-actual_r))))
ck('relative_inertia_integrated',np.max(abs(tau_recovered-actual_tau/actual_tau[0]))<2e-8,float(np.max(abs(tau_recovered-actual_tau/actual_tau[0]))))

reconstructed=[];last=None
for i,(xx,rec) in enumerate(zip(grid,records)):
    f,a,zv,t,force,truth=rec; la=f['pole'];tau_i=tau_recovered[i]
    n=np.sqrt(-tau_i*(2*la+f['Gamma'])*f['residue'])
    if last is not None and abs(-n-last)<abs(n-last):n=-n
    last=n
    nu_i=n.imag/la.imag;G_i=n.real-nu_i*la.real
    sv=1j*a;D=sv*sv+f['Gamma']*sv+f['O']
    corrected=zv+(G_i+nu_i*sv)**2/(tau_i*D)
    mat=np.column_stack([sv*sv,sv,np.ones_like(sv)])
    cf=np.linalg.lstsq(np.vstack([mat.real,mat.imag]),np.r_[corrected.real,corrected.imag],rcond=None)[0]
    rem=float(np.max(abs(mat@cf-corrected)))
    reconstructed.append(dict(tau=tau_i,C=tau_i*f['O'],gamma=tau_i*f['Gamma'],nu=nu_i,G=G_i,M=cf[0],d=cf[1],P0=cf[2],R0=f['R0'],r=f['r'].real,Q=f['Q'],n=n,lambda_=la,polynomial_residual=rem))

pars=np.array([getpar(float(xx)) for xx in grid],dtype=float)
raw_tau,raw_C,raw_B,raw_U,raw_k,raw_nu,raw_gamma,raw_M,raw_d=pars[:,:9].T
raw_tp,raw_Cp,raw_Bp=pars[:,9:12].T
raw_G=raw_Bp-raw_Cp*raw_B/raw_C
scale=np.sqrt(raw_tau[0])
target_G=(raw_G-raw_k*raw_C/raw_tau)/scale
target_nu=(raw_nu-raw_gamma*raw_k/raw_tau)/scale
target_M=raw_M-raw_k**2/raw_tau
target_d=raw_d-2*raw_nu*raw_k/raw_tau+raw_gamma*raw_k**2/raw_tau**2
arr=lambda key:np.array([r[key] for r in reconstructed])
ck('continuous_hidden_reflection_choice',np.max(abs(arr('G')-target_G))<2e-8)
ck('Rayleigh_cross_reconstructed',np.max(abs(arr('nu')-target_nu))<2e-8)
ck('visible_mass_from_response',np.max(abs(arr('M')-target_M))<2e-9)
ck('visible_damping_from_response',np.max(abs(arr('d')-target_d))<2e-9)
ck('entire_polynomial_response',np.max(arr('polynomial_residual'))<2e-9,float(np.max(arr('polynomial_residual'))))
ck('candidate_positivity',np.min(arr('M'))>0 and np.min(arr('d')*arr('gamma')-arr('nu')**2)>0)

raw_w0=-parent['bx']/parent['cx']
raw_R0=s.diff(parent['ux'],px)+s.diff(parent['bx'],px)*raw_w0+s.diff(parent['cx'],px)*raw_w0**2/2
get_R0prime=s.lambdify(px,s.diff(raw_R0,px),'numpy')
true_R0p=get_R0prime(grid)
static_res=arr('P0')-arr('G')**2/arr('C')-true_R0p
ck('equilibrium_static_consistency',np.max(abs(static_res))<3e-9,float(np.max(abs(static_res))))

w0_recovered=cumulative_simpson(-arr('G')/arr('C'),x=grid,initial=0)
B_recovered=-arr('C')*w0_recovered
E_recovered=cumulative_simpson(arr('R0'),x=grid,initial=0)
U_recovered=E_recovered+arr('C')*w0_recovered**2/2
target_w0=scale*((-raw_B/raw_C)-(-raw_B[0]/raw_C[0])+cumulative_simpson(raw_k/raw_tau,x=grid,initial=0))
raw_E=raw_U-raw_B**2/(2*raw_C)
ck('equilibrium_curve_integrated',np.max(abs(w0_recovered-target_w0))<2e-7,float(np.max(abs(w0_recovered-target_w0))))
ck('visible_equilibrium_potential_integrated',np.max(abs(E_recovered-(raw_E-raw_E[0])))<2e-7,float(np.max(abs(E_recovered-(raw_E-raw_E[0])))))
ck('potential_has_reconstructed_equilibrium',np.max(abs(B_recovered+arr('C')*w0_recovered))<1e-13)

# New synthetic ringdowns at existing calibrated environments: only initial
# preparation is fitted on the first60 time samples; later541 are predictions.
prediction=[]
for index,initial in [(0,(-.37,.18)),(30,(.49,.27)),(60,(-.24,-.33))]:
    xx=float(grid[index]);model=reconstructed[index]
    a,zv,t,force,_=parent['synthetic_records'](xx,initial)
    la=model['lambda_'];Cprime=model['tau']*(model['Q']+model['r']*(model['C']/model['tau']));tprime=model['tau']*model['r']
    def predicted(init):
        cc=init[0]+1j*init[1];ee=cc*np.exp(la*t)
        z=2*ee.real;zd=2*(la*ee).real
        return model['R0']+model['G']*z+model['nu']*zd+Cprime*z*z/2-tprime*zd*zd/2
    opt=least_squares(lambda c:(predicted(c)-force)[:60],[.1,.1],xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=300)
    error=float(np.max(abs(predicted(opt.x)[60:]-force[60:])))
    ck('reserved_later_history_'+str(index),opt.success and error<2e-8,error)
    prediction.append({'x':xx,'input_state':initial,'preparation_fit_samples':60,'reserved_prediction_samples':541,'max_error':error})

# Altered observed channels, preserving earlier necessary conditions.
j=30;f=fitrows[j];la=f['pole'];L=f['O']-la*la
gchanged=f['g']*np.exp(.4j)
Schanged=-2*(2*la+f['Gamma'])*f['residue']*gchanged/f['f']**2
rchanged=(Schanged-f['Q'])/L
ck('phase_alternative_keeps_first_Q',f['Q']==fitrows[j]['Q'])
ck('phase_alternative_rejected_by_real_r',abs(rchanged.imag)>.01,float(rchanged.imag))
ck('static_offset_alternative_rejected',abs(static_res[j]+.2)>.19)
ck('negative_mass_alternative_rejected',reconstructed[j]['M']-5<0)
ck('negative_damping_alternative_rejected',(reconstructed[j]['d']-5)*reconstructed[j]['gamma']-reconstructed[j]['nu']**2<0)

# Covariance includes the analytic static-force term; nonaffine sensor labels
# alone do not supply the conjugate-force change.
Jp,Jpp,R0,Z,rho,ff,hh,gg=s.symbols('Jp Jpp R0 Z rho f h g',nonzero=True)
Znew=Z/Jp**2-R0*Jpp/Jp**3
ck('nonaffine_residue_scaling',s.diff(Znew,Z)==1/Jp**2)
ck('complex_second_harmonic_covariance',s.simplify((rho/Jp**2)*(gg/Jp)/(ff/Jp)**2-rho*gg/ff**2/Jp)==0)

# Real-r error envelope accepts correlations and complex phases.
rng=np.random.default_rng(991)
error_max=0.;ratio_max=0.
for i in range(100):
    la=-.2+1.4j;Ga=.4;O=abs(la)**2;rh=.3-.4j;f0=.6+.3j;g0=.1-.02j;Q0=.2
    el,egam,erho,ef,eg,eO,eQ=.001,.0015,.002,.001,.001,.003,.002
    dl=el*np.exp(1j*rng.uniform(0,7));dr=erho*np.exp(1j*rng.uniform(0,7));df=ef*np.exp(1j*rng.uniform(0,7));dg=eg*np.exp(1j*rng.uniform(0,7))
    dga=rng.choice([-egam,egam]);do=rng.choice([-eO,eO]);dq=rng.choice([-eQ,eQ])
    a=2*la+Ga;ahat=2*(la+dl)+Ga+dga
    S0=-2*a*rh*g0/f0**2;Sh=-2*ahat*(rh+dr)*(g0+dg)/(f0+df)**2
    Dmin=abs(f0)**2;eD=2*abs(f0)*ef+ef**2;ea=2*el+egam
    eN=2*((abs(a)+ea)*(abs(rh)+erho)*(abs(g0)+eg)-abs(a)*abs(rh)*abs(g0))
    eS=eN/(Dmin-eD)+2*abs(a)*abs(rh)*abs(g0)*eD/(Dmin*(Dmin-eD))
    L0=O-la**2;Lh=O+do-(la+dl)**2;eL=eO+2*abs(la)*el+el**2
    bound=(eS+eQ)/(abs(L0)-eL)+abs(S0-Q0)*eL/(abs(L0)*(abs(L0)-eL))
    err=abs((Sh-Q0-dq)/Lh-(S0-Q0)/L0)
    ck('correlated_reconstruction_error_'+str(i),abs(Sh-S0)<=eS and err<=bound)
    error_max=max(error_max,err);ratio_max=max(ratio_max,err/bound)

details={'grid_points':len(grid),'normalization':'tau(-0.8)=1; chosen hidden unit, not measured absolute scale',
         'max_relative_inertia_error':float(np.max(abs(tau_recovered-actual_tau/actual_tau[0]))),
         'reserved_synthetic_predictions':prediction,'max_complex_r_error':error_max,'max_fraction_of_r_bound':ratio_max,
         'development_data':'61 synthetic environment responses and ringdowns used for function reconstruction',
         'reserved_status':'new synthetic initial states at3 calibrated environments; first60 samples fit only preparation, last541 evaluated after preparation fit; no empirical test',
         'inputs_received_by_inverse':'port spectra and force time series; generator parameter values used only in separate verification comparisons'}
result={'scope':'conditional exact-class reconstruction with synthetic controls; no empirical validation',
        'summary':{'passed':sum(z['passed'] for z in rows),'failed':sum(not z['passed'] for z in rows)},
        'checks':rows,'details':details,'dependency':{'path':dep.name,'sha256':hashlib.sha256(dep.read_bytes()).hexdigest(),'primary_summary':parent_result['summary']},
        'source_sha256':hashlib.sha256((root/'RINGDOWN_ACTION_RECONSTRUCTION_v1.md').read_bytes()).hexdigest(),
        'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'empirical_validation':False}
print(json.dumps(result,indent=2))
assert result['summary']['failed']==0
