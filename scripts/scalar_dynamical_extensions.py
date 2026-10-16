"""Exact covariance/background identities and conditional potential diagnostics."""
import math
import sympy as s
import numpy as np

def checks():
    rows=[]
    def zero(name,v):
     r=s.factor(v);rows.append({'name':name,'passed':r==0,'residual':str(r)})
    Q,H,rho,ss,p2,phi,X,Z,n,v,V1,V2,b,b1=s.symbols('Q H rho ss p2 phi X Z n v V1 V2 b b1', nonzero=True)
    pd=-H*phi+(ss*X-rho*v)/(2*Q)
    flow={H:-(ss*ss+rho)/(2*Q),rho:(-3*H+b*ss)*rho,ss:-3*H*ss-V1-b*rho,
     p2:-2*H*p2,phi:pd,X:Z,Z:-3*H*Z-(p2+V2+b1*rho)*X+4*ss*pd-2*(V1+b*rho)*phi-b*rho*(n+b*X),
     n:p2*v+3*pd,v:-phi-b*X-b*ss*v,V1:V2*ss,b:b1*ss}
    dt=lambda f:sum(s.diff(f,z)*zd for z,zd in flow.items())
    zero('Einstein_spatial_trace_propagates',dt(pd)+4*H*pd+(2*flow[H]+3*H*H)*phi-(ss*Z-ss*ss*phi-V1*X)/(2*Q))
    beta,kap,q1,q2=s.symbols('beta kap q1 q2',nonzero=True)
    R1=(beta-q1)/(beta*kap*(1-3*q1));R2=(beta-q2)/(beta*kap*(1-3*q2))
    zero('two_epoch_candidate_rank',q1*R2*(1-3*q2)-q2*R1*(1-3*q1)-(q1-q2)/kap)
    aa,SS,CW,dSW,dWW,Swp=s.symbols('aa SS CW dSW dWW Swp',nonzero=True)
    PP=-aa*SS/CW;PPd=-aa*SS/CW-aa*dSW/CW+aa*SS*dWW/CW**2
    MM=-aa*(dSW-Swp+SS)/CW;g=dWW/(2*CW);eta=Swp/SS
    zero('covariance_derivative_split',MM-PPd-PP*(2*g-eta))

    # Exact finite ensemble at an admissible background event. No common transfer.
    Qv=s.Integer(1);Hv=s.Rational(2,3);rv=s.Rational(1,2);sv=s.Rational(1,5);bv=s.Rational(1,3);b1v=s.Rational(1,11);V1v=s.Rational(2,7)
    Cc=Hv+bv*sv;Hdot=-(sv**2+rv)/2;sdot=-3*Hv*sv-V1v-bv*rv;Cdot=Hdot+b1v*sv**2+bv*sdot
    Rtrue=rv/(3*Cc**2);xtrue=-2*bv*sv/Cc;ytrue=xtrue/(2*bv*bv)
    weights=[s.Rational(1,2),s.Rational(1,3),s.Rational(1,6)];ensembles=[];matrix=[];rhs=[]
    for mode in range(3):
     data=[];K2=s.Integer((mode+1)**2);DD=K2/(3*Cc**2)
     for j in range(3):
      ph=-s.Rational(j+1,1000);vel=s.Rational(2+j+mode*(j+1),1300);xi=s.Rational((mode+1)*(j-1)+2,7000)
      phdot=-Hv*ph+(sv*xi-rv*vel)/2;veldot=-ph-bv*xi-bv*sv*vel
      W=K2*vel/Cc;Wp=(K2*(veldot-2*Hv*vel)/Cc-W*Cdot/Cc)/Cc
      data.append({'S':2*ph,'Sp':2*phdot/Cc,'T':2*bv*xi,'W':W,'Wp':Wp})
     cov=lambda a,b:sum(w*r[a]*r[b] for w,r in zip(weights,data))
     ww=cov('W','W');sw=cov('S','W');tw=cov('T','W');spw=cov('Sp','W');swp=cov('S','Wp');wpw=cov('Wp','W')
     coeff=[ww,DD*sw/2,DD*tw/2];target=-DD*(spw+sw);matrix.append(coeff);rhs.append(target)
     zero('ensemble_momentum_'+str(mode),sum(c*z for c,z in zip(coeff,[Rtrue,xtrue,ytrue]))-target)
     P=-DD*sw/ww;M=-DD*(spw+sw)/ww;g=wpw/ww;eta=swp/sw;wrong_minus_true=P*(eta-g)
     ensembles.append({'mode':mode,'gW':str(g),'eta':str(eta),'wrong_M_minus_true':str(s.factor(wrong_minus_true)),'differs':wrong_minus_true!=0})
    mat=s.Matrix(matrix);got=mat.inv()*s.Matrix(rhs)
    for i,name in enumerate(['R','x','y']):zero('ensemble_inverse_'+name,got[i]-[Rtrue,xtrue,ytrue][i])
    rows.append({'name':'common_transfer_counterexample','passed':all(r['differs'] for r in ensembles),'witnesses':ensembles})

    return rows

def potential_diagnostics(old):
    potentials=[]
    for case in old['cases']:
     bet=case['candidate']['beta_inferred'];epochrows=[]
     for ep in case['epochs']:
      row=potential_readout(bet,ep['inferred']['q'],ep['inferred']['R'],ep['inferred']['x'],ep['H_J']/ep['H0_J'],ep['a_J'])
      epochrows.append({**row,'u_true':ep['u']})
     inds=[0,2];design=np.array([[epochrows[i]['U0'],epochrows[i]['U1']] for i in inds]);tar=np.array([epochrows[i]['target'] for i in inds]);gamma,gnu=np.linalg.solve(design,tar);nu=gnu/gamma
     res=[row['target']-gamma*row['U0']-gnu*row['U1'] for row in epochrows[3:]]
     potentials.append({'case':case['case']['id'],'gamma_inferred':gamma,'gamma_true':1/case['epochs'][0]['H0_J']**2,'nu_inferred':nu,'nu_true':case['case']['nu'],'nu_error':nu-case['case']['nu'],'basis_condition':float(np.linalg.cond(design)),'reserved_residuals':res,'epoch_rows':epochrows,'status':'diagnostic; no error envelope or observational inference'})
    return potentials


def background_checks():
    Q,H,A,b,b1,v,rho,V1,H0,a=s.symbols('Q H A b b1 v rho V1 H0 a', nonzero=True)
    G=H+b*v
    flow={H:-(v*v+rho)/(2*Q),A:A*b*v,b:b1*v,v:-3*H*v-V1-b*rho,
          rho:(-3*H+b*v)*rho,a:H*a}
    dt=lambda f:sum(s.diff(f,z)*zd for z,zd in flow.items())
    x=-2*b*v/G;q=2*Q*b*b;omega=(1/q-3)/2;E2=G*G/(A*A*H0*H0)
    h=(dt(G)/G-b*v)/G;R=rho*A*a**3/(3*H0*H0*Q);aj=A*a
    acceleration=dt(x)/G+(h-1)*x+(omega+1)*x*x+2*h+3*R/(aj**3*E2)
    relative=dt(R)/G/R+x
    potential=3*E2*(1+x)-omega*E2*x*x/2-3*R/aj**3
    source=(3*Q*H*H-v*v/2-rho)/(Q*A*A*H0*H0)
    return [{'name':name,'passed':s.factor(res)==0,'residual':str(s.factor(res))}
            for name,res in [('relative_F',relative),('Jordan_background_acceleration',acceleration),('Jordan_potential_value',potential-source)]]


def potential_readout(bet,q,R,x,E,aj):
    modelk=(1-2*math.sqrt(1-3*bet))/3
    st=(1+modelk)/(modelk*(1-3*modelk));om=(1/q-3)/2
    vp=3*E*E*(1+x)-om*E*E*x*x/2-3*R/aj**3
    ex=(bet/q-1)/((1-3*bet)*st);uu=math.log(ex)/(2*math.sqrt(bet))
    FF=1+st*ex;CC=(1+st)*ex/FF
    U0=1.5+3*st*(ex-1)**2/(2*FF**2);U1=(1+st)*uu*uu/(2*FF**2)
    return {'u_inferred':uu,'U0':U0,'U1':U1,'target':vp*CC/2}


def potential_decoder_check():
    # Independently assembled exact event: k=1/6, exp(2alpha*u)=2, s_m=14.
    u=2*s.log(2)/s.sqrt(5);om=(s.Rational(44,5)-3)/2
    vp=3*s.Rational(169,100)*(1+s.Rational(3,50))-om*s.Rational(169,100)*s.Rational(9,2500)/2-s.Rational(6,5)
    expected={'u_inferred':u,'U0':s.Rational(3,2)+s.Rational(21,841),'U1':15*u*u/(2*841),'target':vp*s.Rational(15,29)}
    got=potential_readout(5/16,5/44,2/5,3/50,13/10,1)
    errors={k:abs(got[k]-float(v)) for k,v in expected.items()}
    return {'name':'potential_decoder_exact_event','passed':max(errors.values())<1e-13,'absolute_errors':errors,'scope':'exact-backed software control, separate from ill-conditioned two-epoch diagnostic'}
