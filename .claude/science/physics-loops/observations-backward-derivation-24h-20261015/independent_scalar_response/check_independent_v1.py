"""Independent neutral-contract derivation and full linear initial-value controls."""
from pathlib import Path
import hashlib,json
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
O=Path(__file__).resolve().parent
CHECKS=[]
def check(name,condition,detail=None):CHECKS.append({'name':name,'passed':bool(condition),'detail':detail})
def zero(name,expr):
 val=s.simplify(expr);check(name,val==0,str(val));return val

def symbolic():
 e,t,k=s.symbols('e t k');aa=s.Function('a')(t);ph=s.Function('phi')(t);ch=s.Function('chi')(t);pp=s.Function('P')(t);qq=s.Function('Q')(t)
 det=aa**3*(1+e*(pp-3*qq));g00=-(1-2*e*pp);field=ph+e*ch
 box=s.diff(s.diff(det*g00*s.diff(field,t),t)/det,e).subs(e,0)-k**2/aa**2*ch
 target=-s.diff(ch,t,2)-3*s.diff(aa,t)/aa*s.diff(ch,t)-k**2/aa**2*ch+s.diff(ph,t)*(s.diff(pp,t)+3*s.diff(qq,t))+2*pp*(s.diff(ph,t,2)+3*s.diff(aa,t)/aa*s.diff(ph,t))
 zero('direct determinant inverse metric scalar wave variation',box-target)
 x,a=s.symbols('x a',positive=True);q=s.Function('q')(x);grad=[-e*s.diff(q,x),0,0];delta=lambda i,j:int(i==j)
 G=[[[delta(i,l)*grad[j]+delta(j,l)*grad[i]-delta(i,j)*grad[l] for j in range(3)] for i in range(3)] for l in range(3)]
 def dx(expr,j):return s.diff(expr,x) if j==0 else 0
 Ric=[[sum(dx(G[l][i][j],l)-dx(G[l][i][l],j)+sum(G[l][l][m]*G[m][i][j]-G[l][j][m]*G[m][i][l] for m in range(3)) for l in range(3)) for j in range(3)] for i in range(3)]
 R3=s.exp(2*e*q)/a**2*sum(Ric[i][i] for i in range(3));zero('direct spatial Christoffel curvature',s.diff(R3,e).subs(e,0)-4*s.diff(q,x,2)/a**2)
 H,P,Qd,v,chi,Pi,Vp,Ap,A,rho,dr,M,F,mu,alpha,alphap,V,Vpp,K2,Pd,chiDD=s.symbols('H P Qd v chi Pi Vp Ap A rho dr M F mu alpha alphap V Vpp K2 Pd chiDD',real=True)
 Kmixed=-(H-e*Qd)/(1+e*P);zero('ADM extrinsic curvature term',s.diff(6*Kmixed**2,e).subs(e,0)+12*H*(Qd+H*P))
 energy=(v+e*Pi)**2/(2*(1+e*P)**2)+V+e*Vp*chi+(A+e*Ap*chi)*(rho+e*dr)
 zero('direct proper-energy variation',s.diff(energy,e).subs(e,0)-(A*dr+v*Pi-v**2*P+(Vp+Ap*rho)*chi))
 density=(-2*M**2*(K2*P+3*H*(Pd+H*P))-v*Pi+v**2*P-F*chi)/A
 original=chiDD+3*H*Pi+(K2+mu)*chi+A*alpha*dr-4*v*Pd+2*F*P
 eliminated=chiDD+(3*H-alpha*v)*Pi+(K2+mu-alpha*F)*chi-(6*M**2*alpha*H+4*v)*Pd-(2*M**2*alpha*K2+6*M**2*alpha*H**2-alpha*v**2-2*F)*P
 zero('source elimination all linear terms',original.subs(dr,density)-eliminated)
 r=s.symbols('r',real=True)
 zero('curvature convention',((mu-alpha*F).subs({mu:Vpp+r*(alphap+alpha**2),F:Vp+alpha*r}))-(Vpp-alpha*Vp+r*alphap))
 pcoef=6*M**2*alpha*H**2-alpha*v**2-2*F
 zero('Friedmann simplification preserves metric correction',pcoef.subs({H**2:(r+v**2/2+V)/(3*M**2),F:Vp+alpha*r})-(2*alpha*V-2*Vp))
 cp,cpp,ptau,kj=s.symbols('cp cpp ptau kj',real=True)
 clock=s.expand(eliminated.subs({chiDD:A**2*cpp+A*alpha*v*cp,Pi:A*cp,Pd:A*ptau,K2:A**2*kj**2})/A**2)
 h=H/A;sig=v/A
 expected=cpp+3*h*cp+(kj**2+(mu-alpha*F)/A**2)*chi-(6*M**2*alpha*h+4*sig)*ptau-(2*M**2*alpha*kj**2+6*M**2*alpha*h**2-alpha*sig**2-2*F/A**2)*P
 zero('matter-clock acceleration and damping conversion',clock-expected)
 zero('Jordan lapse potential',s.diff((1+2*e*alpha*chi)*(1+2*e*P),e).subs(e,0)-2*(P+alpha*chi))
 zero('Jordan spatial potential',s.diff((1+2*e*alpha*chi)*(1-2*e*P),e).subs(e,0)+2*(P-alpha*chi))
 zero('slip ratio normalization',((P+alpha*chi)-(P-alpha*chi))/(2*P)-alpha*chi/P)
 # Full dust conventions, trace equation and Hamiltonian propagation.
 U,d=s.symbols('U d',real=True);Hd=-(r+v**2)/(2*M**2);vd=-3*H*v-F;rd=(alpha*v-3*H)*r
 pd=(v*chi-r*U)/(2*M**2)-H*P;ud=-P-alpha*chi-alpha*v*U;dd=3*pd+K2*U
 pid=-3*H*Pi-(K2+mu)*chi-alpha*r*d+4*v*pd-2*F*P
 pdd=-Hd*P-H*pd+(vd*chi+v*Pi-rd*U-r*ud)/(2*M**2)
 trace=pdd+4*H*pd+(2*Hd+3*H**2)*P-(v*Pi-v**2*P-(F-alpha*r)*chi)/(2*M**2)
 zero('momentum Euler background imply dynamic spatial trace',trace)
 theta=-K2*U;thetad=2*H*K2*U-K2*ud
 zero('proper velocity divergence Euler factors',thetad+(2*H+alpha*v)*theta-K2*(P+alpha*chi))
 zero('bare proper number continuity',dd+theta-3*pd)
 hc=-2*M**2*K2*P-3*H*(v*chi-r*U)-r*d-v*Pi+v**2*P-F*chi
 variables=[K2,P,H,v,chi,r,U,d,Pi,F]
 rates=[-2*H*K2,pd,Hd,vd,Pi,rd,ud,dd,pid,mu*v-3*H*alpha*r]
 hcd=sum(s.diff(hc,z)*rate for z,rate in zip(variables,rates))
 zero('Hamiltonian propagation exact',hcd+3*H*hc)
 # Number convention replacement must act on both equations.
 dn=s.symbols('dn');hn=(-2*M**2*(K2*P+3*H*(Pd+H*P))-v*Pi+v**2*P-F*chi)/(A*rho)-3*P
 zero('coordinate-number convention consistent elimination',original.subs(dr,rho*(dn+3*P)).subs(dn,hn)-eliminated)
 check('positive dust precludes static H',Hd.subs({r:1,v:0,M:1})<0)
 return {'hamiltonian_constraint_evolution':'Cdot+3H C=0 with the action-derived momentum, scalar, number and Euler equations','gravity_normalization':'M^2 R/2','independent_neutral_contract_only':True}

M=1.4;MODES=[.5,2.,15.]
def model(phi,rho):
 A=np.exp(.2*phi+.07*phi**2);alpha=.2+.14*phi;alphap=.14;r=A*rho
 V=.5+.08*phi+.18*phi**2+.025*phi**4;Vp=.08+.36*phi+.1*phi**3;Vpp=.36+.3*phi**2
 return A,alpha,r,V,Vp,Vpp+rho*A*(alphap+alpha*alpha),Vp+rho*A*alpha

def rhs(t,y):
 a,phi,v,H,rho=y[:5];A,alpha,r,V,Vp,mu,F=model(phi,rho);Hd=-(r+v*v)/(2*M*M)
 out=[H*a,v,-3*H*v-F,Hd,-3*H*rho]
 for n,kk in enumerate(MODES):
  chi,Pi,P,U,d=y[5+5*n:10+5*n];K2=(kk/a)**2
  Pd=(v*chi-r*U)/(2*M*M)-H*P
  Pid=-3*H*Pi-(K2+mu)*chi-alpha*r*d+4*v*Pd-2*F*P
  Ud=-P-alpha*chi-alpha*v*U;dd=3*Pd+K2*U
  out.extend([Pi,Pid,Pd,Ud,dd])
 return np.array(out)

def numerical():
 a,phi,v,rho=1.,.4,.13,.7;A,alpha,r,V,Vp,mu,F=model(phi,rho);H=np.sqrt((r+.5*v*v+V)/(3*M*M));initial=[a,phi,v,H,rho]
 for kk in MODES:
  chi=1e-4*(1+.1*kk);Pi=-2e-5;P=-2e-5/(1+kk*kk);U=2e-5/(1+kk)
  Pd=(v*chi-r*U)/(2*M*M)-H*P
  d=(-2*M*M*(kk*kk*P+3*H*(Pd+H*P))-v*Pi+v*v*P-F*chi)/r
  initial.extend([chi,Pi,P,U,d])
 epochs=np.linspace(0,1.7,35)
 sol=solve_ivp(rhs,(0,1.7),initial,method='DOP853',t_eval=epochs,rtol=2e-11,atol=2e-13,max_step=.025)
 check('coupled integration success',sol.success,sol.message);rows=[];maxima={'friedmann':0.,'hamiltonian':0.,'eliminated':0.,'trace':0.,'matter_clock':0.,'slip_identity':0.};naive_differences=[]
 for j,t in enumerate(sol.t):
  y=sol.y[:,j];dy=rhs(t,y);a,phi,v,H,rho=y[:5];ad,phid,vd,Hd,rhod=dy[:5];A,alpha,r,V,Vp,mu,F=model(phi,rho);rd=(alpha*v-3*H)*r
  bg=3*M*M*H*H-r-v*v/2-V;maxima['friedmann']=max(maxima['friedmann'],abs(bg))
  for n,kk in enumerate(MODES):
   chi,Pi,P,U,d=y[5+5*n:10+5*n];_,Pid,Pd,Ud,dd=dy[5+5*n:10+5*n];K2=(kk/a)**2
   hc=-2*M*M*(K2*P+3*H*(Pd+H*P))-(r*d+v*Pi-v*v*P+F*chi)
   er=Pid+(3*H-alpha*v)*Pi+(K2+mu-alpha*F)*chi-(6*M*M*alpha*H+4*v)*Pd-(2*M*M*alpha*K2+6*M*M*alpha*H*H-alpha*v*v-2*F)*P
   Pdd=-Hd*P-H*Pd+(vd*chi+v*Pi-rd*U-r*Ud)/(2*M*M)
   tr=Pdd+4*H*Pd+(2*Hd+3*H*H)*P-(v*Pi-v*v*P-Vp*chi)/(2*M*M)
   cp=Pi/A;cpp=(Pid-alpha*v*Pi)/A**2;ptau=Pd/A;h=H/A;sig=v/A;kj2=K2/A**2
   jr=cpp+3*h*cp+(kj2+(mu-alpha*F)/A**2)*chi-(6*M*M*alpha*h+4*sig)*ptau-(2*M*M*alpha*kj2+6*M*M*alpha*h*h-alpha*sig*sig-2*F/A**2)*P
   psij=P+alpha*chi;phij=P-alpha*chi
   slip=alpha*chi/P if abs(P)>1e-12 else None
   if slip is not None:
    si=(psij-phij)/(psij+phij);maxima['slip_identity']=max(maxima['slip_identity'],abs(si-slip));proxy=2*M*M*alpha**2*K2/(K2+mu);naive_differences.append(abs(slip-proxy))
   else:proxy=None
   for key,val in [('hamiltonian',hc),('eliminated',er),('trace',tr),('matter_clock',jr)]:maxima[key]=max(maxima[key],abs(val))
   rows.append({'t_E':float(t),'k_com':kk,'a_E':float(a),'phi':float(phi),'v':float(v),'H_E':float(H),'rho_bare':float(rho),'A':float(A),'alpha':float(alpha),'Fforce':float(F),'mu_fixed_bare':float(mu),'mu_minus_alpha_F':float(mu-alpha*F),'K_E':float(np.sqrt(K2)),'chi':float(chi),'chi_dot':float(Pi),'P_E':float(P),'U':float(U),'theta_physical':float(-K2*U),'delta_bare':float(d),'Psi_J':float(psij),'Phi_J':float(phij),'slip':None if slip is None else float(slip),'naive_static_fixed_bare_proxy':None if proxy is None else float(proxy),'residuals':{'friedmann':float(bg),'hamiltonian':float(hc),'eliminated':float(er),'spatial_trace':float(tr),'matter_clock':float(jr)}})
 for key,val in maxima.items():check('finite coupled trajectory '+key,val<2e-9,val)
 check('positive dust expanding fixture',all(q['rho_bare']>0 and q['H_E']>0 and q['A']>0 for q in rows))
 check('rolling no-minimum fixture',any(abs(q['v'])>.01 and abs(q['Fforce'])>.01 for q in rows))
 check('automatic static slip identification counterexample',max(naive_differences)>.1,max(naive_differences))
 return {'initial':initial,'modes':MODES,'epochs':epochs.tolist(),'solver':{'method':'DOP853','rtol':2e-11,'atol':2e-13,'max_step':.025,'nfev':sol.nfev,'success':sol.success},'max_residuals':maxima,'maximum_slip_naive_proxy_difference':max(naive_differences),'rows':rows,'limitations':'Double precision finite linear-equation trajectory, no interval proof or observed background; large ratio near P=0 is not precision evidence.'}

def main():
 symbolic_result=symbolic();numeric=numerical();result={'scope':'Independent action/geometry, dust conventions and finite full coupled equation checks from neutral contract only','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'contract_sha256':hashlib.sha256((O/'NEUTRAL_CONTRACT_SNAPSHOT_v1.json').read_bytes()).hexdigest(),'symbolic':symbolic_result,'numerical':numeric,'checks':CHECKS,'passed':sum(c['passed'] for c in CHECKS),'failed':sum(not c['passed'] for c in CHECKS),'author_response_or_matter_clock_read':False}
 (O/'INDEPENDENT_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':result['passed'],'failed':result['failed'],'max_residuals':numeric['max_residuals'],'maximum_slip_naive_proxy_difference':numeric['maximum_slip_naive_proxy_difference'],'failed_controls':[q for q in CHECKS if not q['passed']]},indent=2));assert result['failed']==0
if __name__=='__main__':main()
