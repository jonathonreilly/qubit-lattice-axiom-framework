"""Independent synthetic curvature/control evidence; no author curvature sources."""
from pathlib import Path
import hashlib,json,time,sys,platform,datetime
import numpy as np
import scipy
from scipy.integrate import solve_ivp,quad,quad_vec
import sympy as S

OUT=Path(__file__).resolve().parent
START=time.perf_counter()
checks=[]
def check(name,passed,**details):
    checks.append(dict(name=name,passed=bool(passed),**details))
def equal(name,x):
    z=S.simplify(x);check(name,z==0,exact_residual=str(z))
def close(name,got,want,tol=5e-10):
    err=float(np.max(np.abs(np.asarray(got)-np.asarray(want))))
    check(name,err<=tol,error=err,tolerance=tol)
def cq(fun):
    x,e=quad_vec(fun,0.,1.,epsabs=2e-12,epsrel=2e-12,limit=500)
    return x,float(e)

# Independent symbolic derivations before numerical mode controls.
t,H,B,q,ht,hp=S.symbols('t H B q h hp',real=True)
a=1/(1-H*t);calH=H*a;M2=(B-2)*H**2;m2=B*H**2
chi=S.Function('chi')(t);h=chi/a
lhs=S.diff(h,t,2)+2*calH*S.diff(h,t)+(q*q+a*a*m2)*h
equal('chi_field_equation',lhs.subs(S.diff(chi,t,2),-(q*q+M2*a*a)*chi))
equal('desitter_curvature_shift',S.diff(a,t,2)/a-2*H**2*a*a)
physical=a*(hp*hp+(q*q+a*a*m2)*ht*ht)
actual_derivative=S.diff(physical,t)+S.diff(physical,ht)*hp+S.diff(physical,hp)*(-2*calH*hp-(q*q+a*a*m2)*ht)
equal('actual_comoving_energy_derivative',actual_derivative-a*calH*(-3*hp*hp+q*q*ht*ht+3*a*a*m2*ht*ht))
comp0=(hp+H*ht)**2+q*q*ht*ht+M2*ht*ht
phys0=hp*hp+(q*q+m2)*ht*ht
equal('initial_energy_cross_term',comp0-phys0-2*H*ht*hp+H*H*ht*ht)
lam=S.symbols('lam');mat=S.Matrix([[1,1/S.sqrt(B)],[1/S.sqrt(B),1-1/B]])
for label,sgn in [('minus',-1),('plus',1)]:
    val=1-S.Rational(1,2)/B+sgn*S.sqrt(4*B+1)/(2*B)
    equal('energy_equivalence_eigenvalue_'+label,(mat-lam*S.eye(2)).det().subs(lam,val))
equal('B12_lower_constant',(1-S.Rational(1,24)-S.sqrt(49)/24)-S.Rational(2,3))
equal('B12_upper_constant',(1-S.Rational(1,24)+S.sqrt(49)/24)-S.Rational(5,4))
cc,ww,uu,eta,z,zp=S.symbols('c W u eta z zp',real=True)
sigma=1-uu**2
original=cc*z/a-sigma*ww*(S.I*q*eta*z/a+uu*(zp-calH*z)/a)
C=(cc+sigma*calH*ww*uu)/a
transformed=C*z-sigma*ww/a*(S.I*q*eta*z+uu*zp)
equal('observation_transform_plus_clock_term',original-transformed)
equal('missing_clock_term_exact_defect',original-(cc*z/a-sigma*ww/a*(S.I*q*eta*z+uu*zp))-sigma*H*ww*uu*z)
equal('integrated_potential_difference',S.integrate(M2*(a*a-1),(t,0,S.symbols('T',positive=True)))-M2*H*S.symbols('T',positive=True)**2/(1-H*S.symbols('T',positive=True)))

# Entirely rational one-dimensional reference and compact polynomial weights.
H0=S.Rational(1,10);B0=S.Integer(16);T0=S.Integer(1)
u=S.Rational(1,10)+t/20;x=t/10+t*t/40
win=16*t*t*(1-t)**2;c=S.Rational(2,5)*win
sigma=1-u*u;ainv=1-H0*t
Wtilde=ainv*win;P=S.expand(sigma*Wtilde);J=S.expand(-P*u)
C=S.expand(ainv*c+sigma*H0*win*u)
A=S.expand(C-S.diff(J,t));BB=S.expand(P+u*J)
equal('integrated_force_multiplier',BB-sigma*sigma*Wtilde)
phase=S.exp(S.I*q*eta*x)
equal('mode_integration_by_parts_identity',phase*(C*z+J*zp-S.I*q*eta*P*z)-phase*(A-S.I*q*eta*BB)*z-(S.diff(J,t)*phase*z+J*S.diff(phase,t)*z+J*phase*zp))
for name,p in [('W',win),('Bvec',BB)]:
    equal(name+'_left_trace',p.subs(t,0));equal(name+'_right_trace',p.subs(t,1))

def poly_bounds(p):
    poly=S.Poly(S.expand(p),t)
    coeff={mon[0]:abs(v) for mon,v in poly.terms()}
    return dict(inf=sum(coeff.values(),S.Integer(0)),tv=sum((v for j,v in coeff.items() if j),S.Integer(0)),l1=sum((v/(j+1) for j,v in coeff.items()),S.Integer(0)))
pa,pb,pbp=poly_bounds(A),poly_bounds(BB),poly_bounds(S.diff(BB,t))
delta=S.Rational(17,20);J1=S.Rational(1,20);U1=J1;J2=S.Integer(0)
SA=S.factor((2*pa['inf']+pa['tv'])/delta+pa['inf']*J1/delta**2)
SB=S.factor((2*pb['inf']+pb['tv'])/delta+pb['inf']*J1/delta**2)
Zinf=pbp['inf']/delta+pb['inf']*U1/delta**2
TVZ=pbp['tv']/delta+2*pbp['inf']*J1/delta**2+pb['inf']*J2/delta**2+2*pb['inf']*U1*J1/delta**3
SZ=(2*Zinf+TVZ)/delta+Zinf*J1/delta**2
M20=(B0-2)*H0**2;M0=S.sqrt(M20);D=S.factor(M20*H0/(1-H0))
L=S.factor(D*(pa['l1']/M20+pb['l1']/(2*M0)))
Kvals=[S.Rational(1,4),S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(4),S.Integer(8)]
bounds=[]
for K in Kvals:
    sq=(K**3*L**2/3+D**2*(SB**2/K+SA*SB/K**2+SA**2/(3*K**3)))/(2*S.pi**2)
    bounds.append(dict(K=str(K),squared_exact=str(sq),epsilon=float(S.sqrt(sq))))
fun=S.lambdify(t,[x,u,win,c,C,P,J,A,BB],'numpy')
HH=float(H0);MM2=float(M20);MM=float(M0);mass2=float(B0*H0*H0)
Dnum=float(D);SAf=float(SA);SBf=float(SB);A1=float(pa['l1']);B1=float(pb['l1'])

check('energy_can_be_below_naive_identification',S.Rational(15,16)<1,ratio='15/16',data='zero momentum, h=1, hprime=0; mode limit, not finite spatial constant')
check('energy_can_be_above_naive_identification',S.Rational(18,17)>1,ratio='18/17',data='zero momentum, h=1, hprime=H; mode limit, not finite spatial constant')

mode_records=[];max_errors={}
for qq in [0.,.1,.4,2.,10.,50.]:
    omega=np.sqrt(qq*qq+MM2)
    def ode(tt,y):
        aa=1/(1-HH*tt);HHH=HH*aa;om2=qq*qq+MM2*aa*aa;omh2=qq*qq+mass2*aa*aa
        return [y[1],-om2*y[0],y[3],-om2*y[2],y[5],-2*HHH*y[5]-omh2*y[4],y[7],-2*HHH*y[7]-omh2*y[6]]
    init=[1/omega,0.,0.,1.,1/omega,-HH/omega,0.,1.]
    sol=solve_ivp(ode,[0.,1.],init,method='DOP853',rtol=3e-12,atol=3e-14,dense_output=True,max_step=min(.02,1/(12*omega)))
    check(f'mode_solver_success_q{qq}',sol.success,nfev=sol.nfev)
    grid=np.linspace(0,1,65);ys=sol.sol(grid);aa=1/(1-HH*grid);hmath=HH*aa
    close(f'h_chi_transformation_q{qq}',ys[[0,2]]/aa,ys[[4,6]],3e-11)
    close(f'hprime_chi_transformation_q{qq}',(ys[[1,3]]-hmath*ys[[0,2]])/aa,ys[[5,7]],3e-10)
    amp=np.max(np.linalg.norm(ys[[0,2]],axis=0)*omega)
    check(f'phase_uniform_amplitude_bound_q{qq}',amp<=1+2e-11,max_ratio=float(amp))
    vbound=np.max(np.linalg.norm(ys[[1,3]],axis=0)*omega/np.sqrt(qq*qq+MM2*aa*aa))
    check(f'phase_uniform_derivative_bound_q{qq}',vbound<=1+2e-11,max_ratio=float(vbound))
    growth=[]
    for j,tt in enumerate(grid):
        ot=np.sqrt(qq*qq+MM2*aa[j]**2)
        N=np.array([[ot*ys[0,j],ot*ys[2,j]],[ys[1,j],ys[3,j]]])
        growth.append(np.linalg.norm(N,2)/(ot/omega))
    check(f'mode_energy_growth_matrix_q{qq}',max(growth)<=1+2e-11,max_ratio=float(max(growth)))
    def frozen(tt):return np.array([np.cos(omega*tt)/omega,np.sin(omega*tt)/omega])
    def frozen_p(tt):return np.array([-np.sin(omega*tt),np.cos(omega*tt)])
    Egrid=ys[[0,2]]-np.array([frozen(ti) for ti in grid]).T
    EPgrid=ys[[1,3]]-np.array([frozen_p(ti) for ti in grid]).T
    check(f'pointwise_difference_bound_q{qq}',np.max(np.linalg.norm(Egrid,axis=0))<=Dnum/omega**2+2e-11,observed=float(np.max(np.linalg.norm(Egrid,axis=0))),bound=Dnum/omega**2)
    check(f'pointwise_derivative_difference_bound_q{qq}',np.max(np.linalg.norm(EPgrid,axis=0))<=Dnum/omega+2e-11,observed=float(np.max(np.linalg.norm(EPgrid,axis=0))),bound=Dnum/omega)
    def vocint(ss,derivative=False):
        rr=MM2*((1-HH*ss)**-2-1)
        kernel=np.cos(omega*(1-ss)) if derivative else np.sin(omega*(1-ss))/omega
        return -kernel*rr*sol.sol(ss)[[0,2]]
    voc,ve=cq(vocint);vocp,vpe=cq(lambda s:vocint(s,True))
    close(f'Duhamel_field_endpoint_q{qq}',ys[[0,2],-1]-frozen(1),voc,3e-11)
    close(f'Duhamel_derivative_endpoint_q{qq}',ys[[1,3],-1]-frozen_p(1),vocp,3e-10)
    for et in [-1.,-.35,.4,1.]:
        def integrand(tt,kind):
            xx,uu,ww,cc,CC,PP,JJ,AA,bb=map(float,fun(tt));yp=sol.sol(tt);phase=np.exp(1j*qq*et*xx)
            if kind=='h':return phase*(cc*yp[[4,6]]-(1-uu*uu)*ww*(1j*qq*et*yp[[4,6]]+uu*yp[[5,7]]))
            if kind=='chi':return phase*(CC*yp[[0,2]]+JJ*yp[[1,3]]-1j*qq*et*PP*yp[[0,2]])
            if kind=='integrated':return phase*(AA-1j*qq*et*bb)*yp[[0,2]]
            if kind=='frozen':return phase*(AA-1j*qq*et*bb)*frozen(tt)
            if kind=='wrong_clock':return phase*((1-HH*tt)*cc*yp[[0,2]]+JJ*yp[[1,3]]-1j*qq*et*PP*yp[[0,2]])
            raise ValueError(kind)
        oh,eh=cq(lambda s:integrand(s,'h'));oc,ec=cq(lambda s:integrand(s,'chi'));oi,ei=cq(lambda s:integrand(s,'integrated'));of,ef=cq(lambda s:integrand(s,'frozen'));ow,ew=cq(lambda s:integrand(s,'wrong_clock'))
        tag=f'q{qq}_eta{et}'
        close('original_h_vs_transformed_chi_'+tag,oh,oc,5e-11)
        close('integrated_weight_identity_'+tag,oc,oi,5e-11)
        actual=float(np.linalg.norm(oi-of));lo=Dnum*(A1+qq*B1)/omega**2;hi=Dnum*(SAf+qq*SBf)/omega**3
        check('low_momentum_readout_bound_'+tag,actual<=lo+5e-11,observed=actual,bound=lo)
        check('oscillatory_readout_bound_'+tag,actual<=hi+5e-11,observed=actual,bound=hi)
        frozenbound=float(SA+SZ)/omega**2
        check('frozen_functional_row_bound_'+tag,float(np.linalg.norm(of))<=frozenbound+5e-11,observed=float(np.linalg.norm(of)),bound=frozenbound)
        mode_records.append(dict(q=qq,eta=et,delta_row_norm=actual,low_bound=lo,high_bound=hi,omitted_transformed_clock_discrepancy=float(np.linalg.norm(ow-oc)),max_quad_error=max(eh,ec,ei,ef,ew),delta_row_real=(oi-of).real.tolist(),delta_row_imag=(oi-of).imag.tolist()))
        if qq in [.4,10.] and et==.4:
            def outer(ss):
                def inner(tt):
                    xx,uu,ww,cc,CC,PP,JJ,AA,bb=map(float,fun(tt))
                    return np.exp(1j*qq*et*xx)*(AA-1j*qq*et*bb)*np.sin(omega*(tt-ss))/omega
                inn,qe=quad_vec(inner,ss,1.,epsabs=2e-12,epsrel=2e-12,limit=500)
                rr=MM2*((1-HH*ss)**-2-1)
                return -rr*sol.sol(ss)[[0,2]]*inn
            swapped,se=cq(outer)
            close('swapped_Duhamel_observation_'+tag,oi-of,swapped,6e-11)

check('omitted_scale_clock_term_detected',max(r['omitted_transformed_clock_discrepancy'] for r in mode_records)>1e-3,max_discrepancy=max(r['omitted_transformed_clock_discrepancy'] for r in mode_records))
# Polynomial coefficients bound all times analytically; samples only cross-check implementation.
for label,pol,bnd in [('A',A,pa),('Bvec',BB,pb)]:
    values=S.lambdify(t,pol,'numpy')(np.linspace(0,1,1001))
    check(label+'_exact_coefficient_sup_bound',float(np.max(abs(values)))<=float(bnd['inf']),sample_max=float(np.max(abs(values))),exact_bound=str(bnd['inf']))
# Distinct translated paths use the SAME initial data and keep a coherent cross term.
rr=next(r for r in mode_records if r['q']==.4 and r['eta']==.4)
row=np.array(rr['delta_row_real'])+1j*np.array(rr['delta_row_imag'])
translation_phase=np.exp(1j*.4*.4*2.)
combined=(1+translation_phase)*row
separate_sq=2*float(np.vdot(row,row).real)
cross=2*np.cos(.4*.4*2.)*float(np.vdot(row,row).real)
close('distinct_paths_shared_initial_energy_cross_term',float(np.vdot(combined,combined).real)-separate_sq,cross,1e-14)
check('distinct_paths_independent_budgets_wrong',abs(cross)>1e-10,omitted_cross=float(cross))
check('distinct_paths_common_mode_difference_bound',float(np.linalg.norm(combined))<=2*rr['high_bound'],observed=float(np.linalg.norm(combined)),bound=2*rr['high_bound'])
for label,sgn in [('minus',-1),('plus',1)]:
    mu=(2*B-1+sgn*S.sqrt(4*B+1))/(2*(B-2))
    inverse_lambda=1-S.Rational(1,2)/B-sgn*S.sqrt(4*B+1)/(2*B)
    equal('physical_to_chi_inverse_orientation_'+label,mu*inverse_lambda-1)

result=dict(created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer='/root/inertial_response_check',scope='Independent curved scalar/energy/weight and finite-observation frozen-potential comparison; synthetic Fourier-mode controls, no author curvature exposure or observations',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),precheck_sha256=hashlib.sha256((OUT/'PRECHECK_v1.md').read_bytes()).hexdigest(),author_curvature_sources_opened=False,empirical_tests=0,python=sys.version,numpy=np.__version__,scipy=scipy.__version__,sympy=S.__version__,platform=platform.platform(),elapsed_seconds=time.perf_counter()-START,checks=checks,counts=dict(total=len(checks),passed=sum(c['passed'] for c in checks),failed=sum(not c['passed'] for c in checks)),fixture=dict(H=str(H0),B=str(B0),T='1',path=str(x),W=str(win),c=str(c),A_polynomial=str(A),B_polynomial=str(BB),M_squared=str(M20),D=str(D),A_bounds={k:str(v) for k,v in pa.items()},B_bounds={k:str(v) for k,v in pb.items()},S_A=str(SA),S_B=str(SB),S_Z=str(S.factor(SZ)),lambda_minus=float(1-S.Rational(1,2)/B0-S.sqrt(4*B0+1)/(2*B0)),lambda_plus=float(1-S.Rational(1,2)/B0+S.sqrt(4*B0+1)/(2*B0))),operator_difference_bounds=bounds,mode_records=mode_records,limitations=['Numerical ODE and quadrature comparisons are not interval certificates.','The BV/polynomial coefficient and Fourier-tail estimates are handwritten analytic bounds, not inferred from sampled agreement.','Individual Fourier modes are diagnostics of the solution operator, not finite-energy global scalar states.','No action selection, actual environmental reconstruction, observed count calibration or initial-state selection is performed.'])
out=OUT/'RESULTS_v1.json'
with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'counts':result['counts'],'elapsed_seconds':result['elapsed_seconds'],'result_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'source_sha256':result['source_sha256'],'best_displayed_bound':min(bounds,key=lambda r:r['epsilon'])},indent=2))
raise SystemExit(0 if result['counts']['failed']==0 else 1)
