#!/usr/bin/env python3
"""Conditional exact-vacuum weighted inverse; no empirical parameter fit.

Numerical protocol adapted from the direct-author campaign implementation.
Independent checks are archived separately; this is not an independent runner.
"""
from pathlib import Path
import argparse,itertools,json,math,tempfile
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp,quad

AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=(
    'docs/EXPONENTIAL_SCALAR_FINITE_MODE_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-14.md',
    'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md',
)

def measured_checks(check,zero):
    Ah,kh,sh1,sh2,bh1,bh2,ds1,ds2,db1,db2,dA,dk=s.symbols('Ah kh sh1 sh2 bh1 bh2 ds1 ds2 db1 db2 dA dk',real=True)
    D=sh2-sh1;trueA=((bh1-db1)-(bh2-db2))/((sh2-ds2)-(sh1-ds1))
    zero('measured_A_error_identity',(trueA-Ah-(-(db1-db2)+Ah*(ds2-ds1))/(D-(ds2-ds1))).subs(bh1,bh2+Ah*D))
    truek=bh1-db1+(Ah+dA)*(sh1-ds1)
    zero('measured_k_error_identity',truek-(bh1+Ah*sh1)-(-db1-Ah*ds1+dA*(sh1-ds1)))
    nu=lambda A,k:(A+2)*(1-3*k)/4-3*(1+k)
    zero('nu_exact_error',nu(Ah+dA,kh+dk)-nu(Ah,kh)-((1-3*kh)*dA-3*(Ah+6)*dk-3*dA*dk)/4)
    k=s.Rational(1,20);n=s.Integer(1);A=4*(3*(1+k)+n)/(1-3*k)-2;s1=s.Rational(1,100);s2=s.Rational(1,40);b1=k-A*s1;b2=k-A*s2
    es1=s.Rational(1,100000);es2=s.Rational(1,200000);eb1=eb2=s.Rational(1,100000);Es=es1+es2;Eb=eb1+eb2
    corners=[];badwitness=None
    for i,signs in enumerate(itertools.product([-1,1],repeat=4)):
     dx1,dx2,dy1,dy2=[sign*err for sign,err in zip(signs,[es1,es2,eb1,eb2])]
     hs1=s1+dx1;hs2=s2+dx2;hb1=b1+dy1;hb2=b2+dy2;hd=hs2-hs1
     ha=(hb1-hb2)/hd;hk=hb1+ha*hs1;hn=nu(ha,hk)
     ea=(Eb+abs(ha)*Es)/(abs(hd)-Es);ek=eb1+abs(ha)*es1+(abs(hs1)+es1)*ea;en=(abs(1-3*hk)*ea+3*abs(ha+6)*ek+3*ea*ek)/4
     check(f'corner{i}_rank',abs(hd)>Es)
     for name,error,bound in [('A',abs(A-ha),ea),('k',abs(k-hk),ek),('nu',abs(n-hn),en)]:check(f'corner{i}_{name}',error<=bound,error=str(error),bound=str(bound))
     corners.append({'signs':signs,'Ahat':str(ha),'khat':str(hk),'nuhat':str(hn),'eA':str(ea),'ek':str(ek),'enu':str(en),'certifies_physical_domain':bool(hk-ek>0 and hk+ek<s.Rational(1,3) and hn-en>0)})
     wrong=Eb/(abs(hd)-Es)
     if abs(A-ha)>wrong:badwitness={'corner':i,'error':str(abs(A-ha)),'wrong_bound':str(wrong)}
    check('omit_Ahat_times_rank_error_rejected',badwitness is not None,witness=badwitness)
    zero('nu_cross_term_is_necessary',nu(Ah+dA,kh+dk)-nu(Ah,kh)-((1-3*kh)*dA-3*(Ah+6)*dk)/4+3*dA*dk/4)
    check('strict_rank_margin_not_automatic',not(abs(s.Rational(1,1000000))>Es))
    return corners


def run_checks(out):
    out.mkdir(parents=True,exist_ok=False)
    rows=[]
    def check(name,ok,**extra):rows.append(dict(name=name,passed=bool(ok),**extra))
    def zero(name,x):check(name,s.simplify(x)==0,residual=str(s.simplify(x)))
    # Independent symbolic differentiation and parameter inversion.
    z,N,A,k,nu=s.symbols('z N A k nu',positive=True); f=s.Function('f')(z)
    DN=lambda x:-z*s.diff(x,z)
    zero('clock.z_to_N',DN(DN(f))+DN(f)-z*z*s.diff(f,z,2))
    B=4*(3*(1+k)+nu)/(1-3*k)
    # Reconstruct the coupled mass and coupling directly from the displayed action.
    t=s.symbols('t',real=True)
    a=(1-k)*(1+3*k)/4;ss=(1+k)/(k*(1-3*k));E=s.exp(2*t);F=1+ss*E;J=1+(1-3*a)*ss*E
    K=J/F**2;C=(1+ss)*E/F
    U=s.Rational(3,2)+3*ss*(E-1)**2/(2*F**2)+nu*(1+ss)*t**2/(2*a*F**2)
    zero('action.vacuum_C',C.subs(t,0)-1)
    zero('action.vacuum_U',U.subs(t,0)-s.Rational(3,2))
    zero('action.vacuum_gradient',s.diff(U,t).subs(t,0))
    zero('action.coupling_norm',(a*s.diff(C,t)**2/(4*C**2*K)).subs(t,0)-k)
    zero('action.coupled_mass',(a*s.diff(U,t,2)/K).subs(t,0)-B)
    zero('action.mass_lower_margin',B-12-(48*k+4*nu)/(1-3*k))
    zero('action.transverse_x_mass',k/((1+ss)*4*k/(9*(1+ss)))-s.Rational(9,4))
    zero('action.transverse_y_mass',(2*k/3)/((1+ss)*k/(3*(1+ss)))-2)
    # Vacuum source metric constraints and scalar rescaling, retaining free waves.
    H,p,Q,rho,Phi,bb,yy,yN,yNN=s.symbols('H p Q rho Phi bb yy yN yNN',nonzero=True)
    zero('metric.00',p**2*(-rho/(2*Q*p**2))+rho/(2*Q))
    zero('metric.momentum',-H*Phi+H*Phi)
    zero('metric.pressure',H**2*Phi+4*H*(-H*Phi)+3*H**2*Phi)
    # xi=b Phi y, Phi_N=-Phi, delta rho/(2Q)=-p^2 Phi.
    scalar=bb*Phi*(H**2*(yNN-2*yN+yy)+3*H**2*(yN-yy)+(p**2+B*H**2)*yy-p**2)
    zero('mode.original_scalar_rescaling',scalar/(bb*Phi*H**2)-(yNN+yN+(p**2/H**2+B-2)*yy-p**2/H**2))
    c=s.symbols('c')
    zero('identifiability.constant_ratio_substitution',(DN(DN(c*z*z))+DN(c*z*z)+(z*z+A)*c*z*z-k*z*z)/z**2-(c*(z*z+A+2)-k))
    zero('identifiability.constant_ratio_derivative',DN(c*(z*z+A+2)-k)+2*c*z*z)
    zero('potential.nu_inverse',(B*(1-3*k)/4-3*(1+k))-nu)
    zero('domain.A_lower_margin',(B-2)-(10+18*k)/(1-3*k)-4*nu/(1-3*k))
    w=s.Function('w')(N);g=s.Function('g')(N)
    # Boundary concomitant explicitly differentiated: integral proof needs its zero endpoints.
    boundary=w*s.diff(g,N)-s.diff(w,N)*g+w*g
    zero('weak.integration_by_parts',w*(s.diff(g,N,2)+s.diff(g,N))-(s.diff(w,N,2)-s.diff(w,N))*g-s.diff(boundary,N))
    U1,U2,V1,V2,L1,L2=s.symbols('U1 U2 V1 V2 L1 L2')
    D=V1*U2-V2*U1
    kinv=(L1*U2-L2*U1)/D; Ainv=(V2*L1-V1*L2)/D
    zero('inverse.row1',L1+Ainv*U1-kinv*V1)
    zero('inverse.row2',L2+Ainv*U2-kinv*V2)
    zero('inverse.original_k',kinv.subs({L1:k*V1-A*U1,L2:k*V2-A*U2})-k)
    zero('inverse.original_A',Ainv.subs({L1:k*V1-A*U1,L2:k*V2-A*U2})-A)
    x=s.symbols('x',real=True); polynomial=140*x**3*(1-x)**3
    zero('weight.unit_integral',s.integrate(polynomial,(x,0,1))-1)
    for n in range(3):
     for b in [0,1]:zero(f'weight.endpoint_{n}_{b}',s.diff(polynomial,x,n).subs(x,b))
    wv=s.lambdify(x,polynomial,'numpy');wd=s.lambdify(x,s.diff(polynomial,x),'numpy');wdd=s.lambdify(x,s.diff(polynomial,x,2),'numpy')
    windows=[(0,.4),(.5,.9),(1,1.4)];z0=50.; zend=z0*math.exp(-1.4)
    def weights(nn,interval):
     left,right=interval;T=right-left;t=(nn-left)/T
     return float(wv(t))/T,float(wd(t))/T**2,float(wdd(t))/T**3

    def moments(gf,interval):
     left,right=interval
     def parts(nn):
      ww,wp,wpp=weights(nn,interval); zz=z0*math.exp(-nn)
      return ww, wpp-wp+zz*zz*ww, zz
     U,Uerr=quad(lambda nn:parts(nn)[0]*gf(nn),left,right,epsabs=2e-11,epsrel=2e-12,limit=400)
     V,Verr=quad(lambda nn:parts(nn)[0]*parts(nn)[2]**2,left,right,epsabs=2e-11,epsrel=2e-12,limit=400)
     L,Lerr=quad(lambda nn:parts(nn)[1]*gf(nn),left,right,epsabs=2e-11,epsrel=2e-12,limit=400)
     norm,normerr=quad(lambda nn:abs(parts(nn)[1]),left,right,epsabs=2e-10,epsrel=2e-12,limit=400)
     return dict(U=U,V=V,L=L,s=U/V,b=L/V,weight_norm=1.,operator_weight_norm=norm,quad_error_estimates=[Uerr,Verr,Lerr,normerr])
    def inverse(ms):
     m1,m2=ms[:2];det=m1['V']*m2['U']-m2['V']*m1['U']
     kk=(m1['L']*m2['U']-m2['L']*m1['U'])/det
     aa=(m2['V']*m1['L']-m1['V']*m2['L'])/det
     return kk,aa,((aa+2)*(1-3*kk)/4-3*(1+kk)),det
    cases=[]
    # Alternate preparations fixed as additions before any computation; not fitted.
    for ks,ns,y0,yp0 in [('1/20','1',.9,.03),('2/17','3/5',1.2,-.07)]:
     kv=float(s.Rational(ks));nv=float(s.Rational(ns));av=4*(3*(1+kv)+nv)/(1-3*kv)-2
     for prep in [0,1]:
      yy=y0+.37*prep;yyz=yp0-.11*prep
      label=f'k_{ks.replace("/","_")}_prep_{prep}';records=[]
      def rhs_z(zz,state):return [state[1],1-(1+av/zz**2)*state[0]]
      def rhs_N(nn,state):
       zz=z0*math.exp(-nn)
       return [state[1],zz*zz-state[1]-(zz*zz+av)*state[0]]
      solz=solve_ivp(rhs_z,(z0,zend),[yy,yyz],method='DOP853',rtol=1e-11,atol=1e-13,max_step=.1,dense_output=True)
      soln=solve_ivp(rhs_N,(0,1.4),[yy,-z0*yyz],method='Radau',rtol=2e-12,atol=2e-14,max_step=.002,dense_output=True)
      check(label+'.solvers',solz.success and soln.success)
      samples=np.linspace(0,1.4,1001);zs=z0*np.exp(-samples)
      yz=solz.sol(zs);yn=soln.sol(samples)
      transformed=np.stack([yz[0],-zs*yz[1]])
      discrepancy=float(np.max(np.abs(transformed-yn)/(1+np.abs(yn))))
      check(label+'.coordinate_method_agreement',discrepancy<2e-8,max_scaled_error=discrepancy)
      np.savez_compressed(out/(label+'_profiles.npz'),N=samples,z=zs,DOP853_y_yN=transformed,Radau_y_yN=yn)
      for method,gf in [('DOP853_z',lambda nn:kv*float(solz.sol(z0*math.exp(-nn))[0])),('Radau_N',lambda nn:kv*float(soln.sol(nn)[0]))]:
       ms=[moments(gf,win) for win in windows]; kk,aa,nn,det=inverse(ms)
       check(label+'.'+method+'.k',abs(kk-kv)<2e-8,recovered=kk,expected=kv)
       check(label+'.'+method+'.A',abs(aa-av)<2e-6,recovered=aa,expected=av)
       check(label+'.'+method+'.nu',abs(nn-nv)<2e-6,recovered=nn,expected=nv)
       test=ms[2]['L']+aa*ms[2]['U']-kk*ms[2]['V']
       check(label+'.'+method+'.reserved_window',abs(test)<2e-7,residual=test)
       # Exact amplitude perturbation bound, using a declared synthetic error envelope.
       eps=1e-8;esm=[eps/m['V'] for m in ms[:2]];ebm=[eps*m['operator_weight_norm']/m['V'] for m in ms[:2]]
       Es=sum(esm);Eb=sum(ebm);sep=abs(ms[1]['s']-ms[0]['s'])
       check(label+'.'+method+'.error_denominator',sep>Es,separation=sep,error_sum=Es)
       BA=(Eb+abs(av)*Es)/(sep-Es)
       BK=ebm[0]+abs(av)*esm[0]+(abs(ms[0]['s'])+esm[0])*BA
       noisy=lambda tt:gf(tt)+eps*math.sin(13*tt+.2)
       mn=[moments(noisy,win) for win in windows];kn,an,_,_=inverse(mn)
       check(label+'.'+method+'.bounded_bias',abs(an-aa)<=BA+2e-7 and abs(kn-kk)<=BK+2e-9,A_error=abs(an-aa),A_bound=BA,k_error=abs(kn-kk),k_bound=BK)
       # An alternate third-window data trace; calibration moments remain identical.
       interval=windows[2];T=interval[1]-interval[0]
       shifted=lambda tt:gf(tt)+1e-3*(wv((tt-interval[0])/T)/wv(.5))
       mt=moments(shifted,interval);bad=mt['L']+aa*mt['U']-kk*mt['V']
       check(label+'.'+method+'.altered_reserved_window',abs(bad)>1e-3,residual=bad)
       records.append(dict(method=method,moments=ms,recovered=dict(k=kk,A=aa,nu=nn,det=det),reserved_residual=test,altered_reserved_residual=bad,amplitude_error_envelope=eps,A_error_bound=BA,k_error_bound=BK,quadrature_error_is_estimate_not_rigorous_enclosure=True))
      cases.append(dict(label=label,k=ks,nu=ns,initial_y=yy,initial_y_z=yyz,coordinate_method_discrepancy=discrepancy,source_amplitude_arbitrarily_small_on_finite_interval=True,records=records,solver_stats=dict(DOP853_z=dict(nfev=solz.nfev,steps=len(solz.t)),Radau_N=dict(nfev=soln.nfev,njev=soln.njev,steps=len(soln.t)))))
    measured_corners=measured_checks(check,zero)
    result=dict(scope='Conditional finite comoving mode, supplied action and exact vacuum. Synthetic development/calibration and reserved synthetic interval only; no empirical test.',checks=rows,counts=dict(passed=sum(r['passed'] for r in rows),failed=sum(not r['passed'] for r in rows)),cases=cases,measured_error_corners=measured_corners)
    (out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    output=args.output if args.output else Path(tempfile.mkdtemp(prefix='scalar-mode-check-'))/'profiles'
    result=run_checks(output)
    print(json.dumps(result,indent=2,allow_nan=False))
    raise SystemExit(bool(result['counts']['failed']))
