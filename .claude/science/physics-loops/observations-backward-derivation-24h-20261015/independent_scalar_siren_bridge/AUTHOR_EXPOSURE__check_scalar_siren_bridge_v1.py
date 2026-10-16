"""Conditional scalar-wave measurement contract; no empirical data."""
AUDIT_TIMEOUT_SEC = 120
import hashlib
import json
from pathlib import Path
import numpy as np
from numpy.polynomial import Polynomial
from scipy.integrate import solve_ivp, quad
import sympy as s

P = Path(__file__).resolve().parent
plan = json.loads((P / 'SCALAR_SIREN_PLAN_v1.json').read_text())
assert hashlib.sha256((P / plan['source']).read_bytes()).hexdigest() == plan['source_sha256']
rows = []
details = {}
def ck(name, passed, detail=None):
    rows.append({'name': name, 'passed': bool(passed), 'detail': detail})

# Direct arbitrary-gradient projection, without setting the scalar wave to zero.
b = s.Matrix(s.symbols('b0:4')); kc = s.Matrix([-1, 0, 0, 1])
metric = s.diag(-1, 1, 1, 1)
stress = b * kc.T + kc * b.T - metric * (b[0] + b[3])
ep = s.diag(0, 1, -1, 0)
ec = s.zeros(4); ec[1, 2] = ec[2, 1] = 1
ck('scalar_derivative_TT_plus', s.simplify(s.trace(ep * stress)) == 0)
ck('scalar_derivative_TT_cross', s.simplify(s.trace(ec * stress)) == 0)
ck('background_gradient_square_not_generically_TT_zero', s.trace(ep * (b*b.T)) != 0)
x = s.symbols('x', real=True); O=s.Function('O')(x); A=s.Function('A')(x); kf=s.Function('k')(x)
current_E = s.diff(O**4 * A**2 * O**-2 * kf, x)/O**4
ck('conformal_current_power', s.simplify(O**4*current_E-s.diff(O**2*A**2*kf,x)) == 0)
ck('wrong_conformal_power_detected', s.simplify(O**4*current_E-s.diff(O**3*A**2*kf,x)) != 0)

# Independent quadrupole differentiation gives the two source normalizations.
t, om, mu, radius, GT, Gc, mass, R, eta = s.symbols('t om mu r GT Gc M R eta', positive=True)
pos=s.Matrix([radius*s.cos(om*t),radius*s.sin(om*t),0])
I=mu*(pos*pos.T-s.eye(3)*radius**2/3)
I3=I.diff(t,3)
contract=s.trigsimp(sum(z*z for z in I3))
ck('quadrupole_flux_contraction', s.simplify(contract-32*mu**2*radius**4*om**6)==0)
hplus=(GT/R)*(I[0,0]-I[1,1]).diff(t,2)
hcross=(2*GT/R)*I[0,1].diff(t,2)
ck('faceon_tensor_amplitude', s.trigsimp(hplus**2+hcross**2-(4*GT*mu*radius**2*om**2/R)**2)==0)
energy=-mu*(Gc*mass)**s.Rational(2,3)*om**s.Rational(2,3)/2
flux=(GT*contract/5).subs(radius,(Gc*mass/om**2)**s.Rational(1,3))
chirp=s.simplify(-flux*(1+eta)/s.diff(energy,om))
K=GT*mu*(Gc*mass)**s.Rational(2,3)
ck('energy_balance_with_separate_couplings',s.simplify(chirp-s.Rational(96,5)*K*om**s.Rational(11,3)*(1+eta))==0)
z,oo,DL,rho=s.symbols('z oo DL rho', positive=True)
observed_chirp=s.simplify(chirp.subs(om,(1+z)*oo)/(1+z)**2)
Kz=K*(1+z)**s.Rational(5,3)
H=4*Kz*oo**s.Rational(2,3)*s.sqrt(rho)/DL
D=s.simplify(s.Rational(5,24)*observed_chirp/(H*oo**3))
ck('redshift_and_chirp_distance',s.simplify(D-DL*(1+eta)/s.sqrt(rho))==0)
ck('naive_no_extra_loss_wrong',s.simplify((DL/D)**2-rho)!=0)

# Complete leading waveform ambiguity, including an optional dipole-shaped loss.
base=plan['chirp_controls']['base'];lo,hi,n=plan['chirp_controls']['frequency_grid'];freq=np.linspace(lo,hi,n)
def observables(ww,pars):
    ee=pars['eta0']+pars['b']*(ww/pars['omega_ref'])**(-2/3)
    dot=(96/5)*pars['Kz']*ww**(11/3)*(1+ee)
    amp=4*pars['Kz']*ww**(2/3)*np.sqrt(pars['rho'])/pars['DL']
    return dot,amp,ee
source_rows=[]
for bv in [0.,base['b']]:
    pp={**base,'b':bv};dot,amp,ee=observables(freq,pp)
    for scale in plan['chirp_controls']['rescalings']:
        qq={**pp,'Kz':pp['Kz']/scale,'rho':pp['rho']*scale**2,'eta0':scale*(1+pp['eta0'])-1,'b':scale*pp['b']}
        dq,hq,eq=observables(freq,qq)
        ck('source_invariance_'+str((bv,scale)),np.max(abs(dq/dot-1))<1e-10 and np.max(abs(hq/amp-1))<1e-10 and np.min(eq)>=0)
        # Integrate time and phase along the frequency history in each parameterization.
        ff=np.linspace(lo,hi,15)
        hist=[]
        for rr in [pp,qq]:
            times=np.array([quad(lambda ww:1/observables(ww,rr)[0],lo,v,epsabs=1e-9,epsrel=1e-12)[0] for v in ff])
            phase=np.array([quad(lambda ww:2*ww/observables(ww,rr)[0],lo,v,epsabs=1e-9,epsrel=1e-12)[0] for v in ff])
            hist.append((times,phase,observables(ff,rr)[1]*np.cos(phase)))
        err=max(float(np.max(abs(aa-bb))/max(1.,np.max(abs(aa)))) for aa,bb in zip(hist[0],hist[1]))
        ck('full_leading_waveform_'+str((bv,scale)),err<1e-10,err)
        source_rows.append({'eta_dipole_coefficient':bv,'rescaling':scale,'rho_before':pp['rho'],'rho_after':qq['rho'],'max_fractional_history_difference':err})
    dc=(5/24)*dot/(amp*freq**3)
    naive=(pp['DL']/dc)**2
    ck('eta_ignored_bias_'+str(bv),np.max(abs(naive-pp['rho']))>.1,{'true_rho':pp['rho'],'naive_min':float(min(naive)),'naive_max':float(max(naive))})
details['leading_source_ambiguity']=source_rows

# Monotone interval transfer uses bounds, not an assumed equality of endpoint fields.
cfg=plan['interval_controls'];rng=np.random.default_rng(cfg['seed'])
qlo,qhi=cfg['q_interval'];elo,ehi=cfg['eta_interval'];xslo,xshi=cfg['xs_interval'];xolo,xohi=cfg['xo_interval']
rl=(qlo*(1+elo))**2;rh=(qhi*(1+ehi))**2
cl=np.log(rl)-xshi+xolo;ch=np.log(rh)-xslo+xohi
for i in range(cfg['draws']):
    q=rng.uniform(qlo,qhi);ee=rng.uniform(elo,ehi);xs=rng.uniform(xslo,xshi);xo=rng.uniform(xolo,xohi)
    rr=(q*(1+ee))**2;logc=np.log(rr)-xs+xo
    ck('registration_interval_'+str(i),rl<=rr<=rh and cl<=logc<=ch)
details['intervals']={'rho':[rl,rh],'log_Cs_over_Co':[float(cl),float(ch)],'scope':'deterministic synthetic control, no observational interval'}

# Exact change of variable, then two independently integrated wave equations.
F=s.Function('F')(x);u=s.Function('u')(x);kk=s.symbols('k',positive=True)
hh=u/s.sqrt(F)
op=s.simplify(s.sqrt(F)*(s.diff(hh,x,2)+s.diff(F,x)/F*s.diff(hh,x)+kk**2*hh))
potential=s.diff(s.sqrt(F),x,2)/s.sqrt(F)
ck('exact_wave_transform',s.simplify(op-s.diff(u,x,2)-(kk**2-potential)*u)==0)
step=Polynomial([0,0,0,10,-15,6]);bump=Polynomial([0,0,0,64,-192,192,-64])
def scatter(a,b,k,scale=1.,method='u'):
    logf=a*step+b*bump;lp=logf.deriv();lpp=lp.deriv()
    def q(xx):return .5*lpp(xx)+.25*lp(xx)**2
    if method=='u':
        fun=lambda xx,y:np.array([y[1],(q(xx)-k*k)*y[0]])
        init=np.array([np.exp(1j*k),1j*k*np.exp(1j*k)])
    else:
        fun=lambda xx,y:np.array([y[1],-lp(xx)*y[1]-k*k*y[0]])
        init=np.array([np.exp(1j*k),1j*k*np.exp(1j*k)])/np.sqrt(scale*np.exp(a))
    sol=solve_ivp(fun,[1.,0.],init,method='DOP853',rtol=1e-10,atol=1e-12)
    assert sol.success,sol.message
    v,dv=sol.y[:,-1];AA=(v+dv/(1j*k))/2;BB=(v-dv/(1j*k))/2
    if method=='h':
        return np.array([1/(np.sqrt(scale*np.exp(a))*AA),BB/AA])
    # Safe analytic J bound, intentionally conservative; not a measured gradient certificate.
    Jbar=7.5*abs(a)+60*abs(b)+.25*(1.875*abs(a)+12*abs(b))**2
    Jnum=quad(lambda xx:abs(q(xx)),0.,1.,epsabs=1e-10,limit=200)[0]
    mm=Jbar*np.exp(Jbar/k)/(2*k)
    tt=1/AA;rr=BB/AA
    return {'transmission':np.exp(-a/2)*tt,'reflection':rr,'u_transmission':tt,'A':AA,'B':BB,'J_numeric':Jnum,'J_bound':Jbar,'error_bound':mm}
def cv(z):return [float(z.real),float(z.imag)]
scattering=[];by_profile={}
profiles=plan['profiles']['development']+plan['profiles']['reserved']
for i,(aa,bb) in enumerate(profiles):
    for kval in plan['profiles']['frequencies']:
        result=scatter(aa,bb,kval);direct=scatter(aa,bb,kval,method='h');tv=result['transmission'];rv=result['reflection'];ut=result['u_transmission'];m=result['error_bound']
        delta=max(abs(tv-direct[0]),abs(rv-direct[1]));wr=abs(abs(result['A'])**2-abs(result['B'])**2-1)
        ck('direct_h_vs_u_'+str((i,kval)),delta<3e-8,float(delta))
        ck('real_potential_flux_'+str((i,kval)),wr<3e-8 and abs(abs(rv)**2+np.exp(aa)*abs(tv)**2-1)<3e-8,float(wr))
        ck('analytic_gradient_bound_'+str((i,kval)),result['J_numeric']<=result['J_bound']+1e-10)
        ck('certified_proxy_error_'+str((i,kval)),abs(ut-1)<=m+3e-8 and abs(rv)<=min(m,1)+3e-8 and abs(ut)+3e-8>=1/np.sqrt(1+m*m))
        for scale in plan['profiles']['global_scalings']:
            scaled=scatter(aa,bb,kval,scale=scale,method='h')
            ck('absolute_scale_unidentifiable_'+str((i,kval,scale)),max(abs(scaled[0]-tv),abs(scaled[1]-rv))<3e-8)
        item={'profile_index':i,'role':'development' if i<2 else 'reserved_synthetic','a':aa,'b':bb,'k':kval,'strain_transmission':cv(tv),'reflection':cv(rv),'endpoint_only_transmission':float(np.exp(-aa/2)),'complex_endpoint_error':float(abs(ut-1)),'J_numeric':result['J_numeric'],'J_analytic_bound':result['J_bound'],'complex_error_bound':m,'direct_equation_difference':float(delta),'wronskian_error':float(wr)}
        scattering.append(item);by_profile[(i,kval)]=result
for kval in [3,9]:
    difference=abs(by_profile[(0,kval)]['transmission']-by_profile[(1,kval)]['transmission'])
    ck('same_endpoints_different_finite_wave_'+str(kval),difference>1e-3,float(difference))
for i in range(len(profiles)):
    low=abs(by_profile[(i,3)]['u_transmission']-1);high=abs(by_profile[(i,180)]['u_transmission']-1)
    ck('high_frequency_endpoint_approach_'+str(i),high<low,{'low':float(low),'high':float(high)})
details['scattering_proxy']=scattering

output={'source_sha256':plan['source_sha256'],'plan_sha256':hashlib.sha256((P/'SCALAR_SIREN_PLAN_v1.json').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'summary':{'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows)},'checks':rows,'details':details,'empirical_validation':False,'scope':'Conditional source/transport contract and 1D proxy. No exact scalar-background or full PN-waveform claim.'}
print(json.dumps(output,indent=2));assert output['summary']['failed']==0
