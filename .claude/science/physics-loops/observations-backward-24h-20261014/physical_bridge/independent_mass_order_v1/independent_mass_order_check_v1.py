#!/usr/local/bin/python3
"""Independent clock-only KG interference counterexample; no author inputs."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import erfc
ROOT=Path(__file__).resolve().parent
started=time.perf_counter();checks=[]
def check(name,value,tol=2e-10):
    err=float(np.max(np.abs(value)));ok=bool(np.isfinite(err) and err<=tol)
    checks.append(dict(name=name,passed=ok,error=err,tolerance=tol));assert ok,(name,err,tol)
def truth(name,ok,**more):
    checks.append(dict(name=name,passed=bool(ok),**more));assert ok,(name,more)
pi=np.pi;T=40.;omega0=2*pi;mu=pi*np.sqrt(23)/6
points=np.array([[-.75,0,0],[.75,0,0],[0,np.sqrt(7)/4,0]])
a=np.array([1.,1.,-2.]);dist=np.linalg.norm(points[:,None,:]-points[None,:,:],axis=2)
check('exact_spatial_distances',dist-np.array([[0,1.5,1],[1.5,0,1],[1,1,0]]))
check('pointwise_spatial_weight_sum',a.sum())
truth('points_noncollinear',np.linalg.norm(np.cross(points[1]-points[0],points[2]-points[0]))>.5)
def M(omega,mass,dist=dist):
    if omega<=mass:return np.zeros_like(dist)
    k=np.sqrt(omega*omega-mass*mass)
    return (k/omega)*np.sinc(k*dist/pi)
def q(omega,mass):return float(a@M(omega,mass)@a)
def F(k):return 6*k+(4/3)*np.sin(1.5*k)-8*np.sin(k)
def sphere(nz,nphi):
    z,w=leggauss(nz);phi=2*pi*np.arange(nphi)/nphi
    zz,pp=np.meshgrid(z,phi,indexing='ij');rr=np.sqrt(1-zz*zz)
    dirs=np.column_stack([(rr*np.cos(pp)).ravel(),(rr*np.sin(pp)).ravel(),zz.ravel()])
    weights=np.repeat(w,nphi)*2*pi/nphi
    return dirs,weights
def angular_q(omega,mass,nz=32,nphi=64):
    if omega<=mass:return 0.
    k=np.sqrt(omega*omega-mass*mass);dirs,w=sphere(nz,nphi)
    values=np.exp(1j*k*(dirs@points.T))@a
    return float(k/omega*np.dot(w,np.abs(values)**2)/(4*pi))
k0=np.sqrt(omega0**2-mu**2)
check('chosen_radial_frequency',k0-11*pi/6)
exact0=6.;exactmu=5.5+2/pi+np.sqrt(2)/(3*pi)
check('massless_frequency_factor',q(omega0,0)-exact0)
check('massive_frequency_factor',q(omega0,mu)-exactmu)
truth('fixed_frequency_mass_order_fails',exactmu>exact0,exact_gap=exactmu-exact0)
check('cosine_kernel_negative_direction',a@np.cos(omega0*dist)@a+4)
truth('cosine_distance_matrix_indefinite',np.linalg.eigvalsh(np.cos(omega0*dist))[0]<-.9)
for i,w in enumerate([mu-.1,mu+.05,omega0-.1,omega0,omega0+.1,8.]):
    for j,mass in enumerate([0.,mu]):
        if w>mass:check(f'closed_scalar_factor_{i}_{j}',q(w,mass)-F(np.sqrt(w*w-mass*mass))/w)
        check(f'angular_sinc_low_{i}_{j}',angular_q(w,mass,24,48)-q(w,mass),2e-11)
        check(f'angular_sinc_high_{i}_{j}',angular_q(w,mass,40,80)-q(w,mass),2e-11)
# Conditions that make the analytic band lower bound valid, not a grid proof.
wlo=omega0-.1;whi=omega0+.1;klo=np.sqrt(wlo*wlo-mu*mu);khi=np.sqrt(whi*whi-mu*mu)
truth('analytic_band_ranges',wlo>6.18 and klo>5.64 and khi<5.88 and whi/klo<1.14)
truth('analytic_band_cosine_signs',1-(2*pi-5.64)**2/2>.75 and 1.5*5.64>2.5*pi and 1.5*5.88<3.5*pi and 1.5*wlo>2.5*pi and 1.5*whi<3.5*pi)
center_difference=F(k0)-F(omega0)
truth('analytic_center_bounds',exactmu-exact0>.286 and abs(center_difference)<1.81)
lip=8.56/6.18+2.666/6.18**2
truth('analytic_band_lower_bound',lip<1.456 and .286-.1*lip>.13,derived_lower=.286-.1*lip)
samples=np.linspace(wlo,whi,81);mingap=min(q(w,mu)-q(w,0) for w in samples)
truth('band_grid_consistency_only',mingap>.13,minimum_sampled_gap=mingap)
# Collinear ordering controls: arbitrary complex temporal vectors are covered by PSD.
collinear=np.array([-.7,0,1.3,2.9]);cd=np.abs(collinear[:,None]-collinear[None,:])
for i,w in enumerate([.6,2.,4.,7.,12.]):
    for j,frac in enumerate([0.,.2,.6,.9,1.1]):
        diff=M(w,0,cd)-M(w,frac*w,cd)
        mineig=float(np.linalg.eigvalsh(diff)[0]);truth(f'collinear_order_{i}_{j}',mineig>-3e-12,min_eigenvalue=mineig)
        cosmineig=float(np.linalg.eigvalsh(np.cos(w*cd))[0]);truth(f'collinear_cosine_Gram_{i}_{j}',cosmineig>-3e-12)
# Explicit smooth compact cutoff, with no need to impose zero temporal integral.
def cutoff(t):
    z=np.abs(np.asarray(t))/T-8;out=np.ones_like(z,dtype=float);out[z>=1]=0
    use=(z>0)&(z<1);v=z[use];logratio=-1/v+1/(1-v)
    # stable logistic for the smooth step
    step=np.empty_like(v);positive=logratio>=0
    step[positive]=1/(1+np.exp(-logratio[positive]));ex=np.exp(logratio[~positive]);step[~positive]=ex/(1+ex)
    out[use]=1-step;return out
def g(t):return np.exp(-t*t/(2*T*T))*np.cos(omega0*t)
def f(t):return cutoff(t)*g(t)
def Cgauss(w):return np.sqrt(2*pi)*T/2*(np.exp(-T*T*(w-omega0)**2/2)+np.exp(-T*T*(w+omega0)**2/2))
def temporal_rule(order,panel):
    edges=np.linspace(0,9*T,int(round(9*T/panel))+1);x,w=leggauss(order)
    nodes=((edges[:-1,None]+edges[1:,None])/2+(edges[1:,None]-edges[:-1,None])/2*x).ravel()
    weights=((edges[1:,None]-edges[:-1,None])/2*w).ravel()
    return nodes,weights
def Ccompact(omegas,order=20,panel=1.):
    nodes,weights=temporal_rule(order,panel)
    return 2*(np.cos(np.outer(np.atleast_1d(omegas),nodes))@(weights*f(nodes)))
check('cutoff_core_and_support',cutoff(np.array([0.,100.,320.,360.,400.]))-np.array([1,1,1,0,0]))
check('exact_summed_time_weights',np.sum(a[:,None]*f(np.linspace(-370,370,121)),axis=0))
probes=omega0+np.array([-.2,-.1,-.025,0,.025,.1,.2])
c1=Ccompact(probes,16,1.);c2=Ccompact(probes,24,1.5)
check('independent_temporal_rules',c1-c2,3e-10)
check('compact_transform_vs_analytic_gaussian_with_tiny_cutoff',c2-Cgauss(probes),3e-10)
check('real_even_temporal_transform',Ccompact(-probes,24,1.5)-c2,3e-10)
# Positive-frequency integration on the narrow peak; remainders bounded below.
def frequency_product(order,use_compact):
    z,w=leggauss(order);omega=omega0+12*z/T;weights=12*w/T
    C=Ccompact(omega,24,1.5) if use_compact else Cgauss(omega)
    values={}
    for mass in [0.,mu]:values[str(mass)]=float(np.dot(weights,C*C*np.array([q(v,mass) for v in omega]))/(2*pi*pi))
    return values
spectral_gauss=frequency_product(160,False);spectral_compact=frequency_product(160,True);spectral_fine=frequency_product(240,False)
for mass in [0.,mu]:
    key=str(mass)
    check('spectral_resolution_'+key,spectral_gauss[key]-spectral_fine[key],2e-10)
    check('direct_compact_transform_integral_'+key,spectral_compact[key]-spectral_gauss[key],3e-9)
gap=spectral_compact[str(mu)]-spectral_compact['0.0']
truth('integrated_counterexample',gap>1.,massless=spectral_compact['0.0'],massive=spectral_compact[str(mu)],gap=gap)
# Complete analytic Gaussian-tail plus compact-cutoff error bound.
Iall=pi**1.5*T/2*(1+np.exp(-T*T*omega0*omega0))
eta_bound=2*erfc(4)+erfc(T*omega0)
eta_elementary=2*np.exp(-16)/(4*np.sqrt(pi))
truth('gaussian_band_tail_bound',eta_bound<eta_elementary<3.2e-8,exact_upper=eta_bound,elementary_upper=eta_elementary)
gaussian_gap_lower=Iall/(2*pi*pi)*(.13-(16+.13)*3.2e-8)
delta_bound=np.sqrt(T*np.exp(-64)/8);gnorm=np.sqrt(Iall/pi)
cutoff_form_error=16/pi*(2*gnorm+delta_bound)*delta_bound
strict_gap=gaussian_gap_lower-cutoff_form_error
truth('compact_tail_L2_bound',delta_bound<3e-14,bound=delta_bound)
truth('compact_quadratic_perturbation_bound',cutoff_form_error<1e-10,bound=cutoff_form_error)
truth('analytic_strict_compact_counterexample',strict_gap>.7,strict_lower_bound=strict_gap)
# Deliberately erroneous spatial phase reuse would miss the positive gain.
wrong=(k0/omega0)*q(omega0,0)
truth('massless_spatial_phase_substitution_fails',wrong<q(omega0,0) and q(omega0,mu)>q(omega0,0),wrong=wrong,correct=q(omega0,mu))
# Independently construct real Riesz h0 and integrate its actual 3D energy.
field_values=[];dirs,aw=sphere(32,64);alpha=(2*pi)**(-1.5)
for mass in [0.,mu]:
    lo=np.sqrt((omega0-.5)**2-mass*mass);hi=np.sqrt((omega0+.5)**2-mass*mass)
    z,zw=leggauss(180);ks=(hi+lo)/2+(hi-lo)/2*z;kw=(hi-lo)/2*zw
    om=np.sqrt(ks*ks+mass*mass);cc=Cgauss(om)
    energy=0.;observable=0.;symerr=0.
    for k,w,omega,C in zip(ks,kw,om,cc):
        kv=k*dirs;S=np.exp(-1j*(kv@points.T))@a
        hhat=alpha*C*S/(omega*omega)
        hminus=alpha*C*(np.exp(1j*(kv@points.T))@a)/(omega*omega)
        symerr=max(symerr,float(np.max(np.abs(hminus-hhat.conj()))))
        energy+=w*k*k*np.dot(aw,omega*omega*np.abs(hhat)**2)
        observable+=w*k*k*np.dot(aw,np.real(alpha*C*(np.exp(1j*(kv@points.T))@a)*hhat))
    check('real_Riesz_conjugate_symmetry_'+str(mass),symerr,2e-13)
    check('Riesz_energy_equals_observation_'+str(mass),energy-observable,2e-10)
    check('independent_radial_energy_norm_'+str(mass),energy-spectral_gauss[str(mass)],3e-9)
    field_values.append(dict(mass=mass,finite_band_norm_squared=float(energy),finite_band_observation=float(observable)))
result=dict(created_at=datetime.now(timezone.utc).isoformat(),reviewer='/root/localized_history_check',checks_passed=len(checks),checks=checks,points=points.tolist(),spatial_weights=a.tolist(),omega0=omega0,mass=mu,packet_scale=T,packet_core_radius=8*T,packet_support_radius=9*T,frequency_factors=dict(massless=exact0,massive=exactmu,gap=exactmu-exact0),finite_spectral_values=spectral_compact,finite_spectral_gap=gap,finite_spectral_ratio=spectral_compact[str(mu)]/spectral_compact['0.0'],analytic_bounds=dict(gaussian_band_tail=eta_bound,elementary_band_tail=eta_elementary,gaussian_gap_lower=gaussian_gap_lower,compact_L2_difference=delta_bound,compact_quadratic_error=cutoff_form_error,strict_compact_gap_lower=strict_gap),field_controls=field_values,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),precheck_sha256=hashlib.sha256((ROOT/'MASS_ORDER_PRECHECK_v1.md').read_bytes()).hexdigest(),author_sources_read=False,other_reviewers_read=False,empirical_tests=0,elapsed_seconds=time.perf_counter()-started,scope='General pure-clock fixed noncollinear-point KG functional only. Counterexample uses identical physical smooth compact temporal weights across masses and exact pointwise zero summed weights. No conclusion about a specific coherent count/force fixture.')
with (ROOT/'INDEPENDENT_MASS_ORDER_RESULTS_v1.json').open('x') as out:json.dump(result,out,indent=2);out.write('\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
