"""Root full rolling response; supplied action, synthetic histories only."""
from pathlib import Path
import json, math, hashlib, datetime
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


def symbolic_checks():
    Q,H,rho,s,p2,phi,X,Z,n,v,V1,V2,b,b1=sp.symbols('Q H rho s p2 phi X Z n v V1 V2 b b1', nonzero=True)
    pd=-H*phi+(s*X-rho*v)/(2*Q)
    flow={H:-(s*s+rho)/(2*Q),rho:(-3*H+b*s)*rho,s:-3*H*s-V1-b*rho,
          p2:-2*H*p2,phi:pd,X:Z,Z:-3*H*Z-(p2+V2+b1*rho)*X+4*s*pd-2*(V1+b*rho)*phi-b*rho*(n+b*X),
          n:p2*v+3*pd,v:-phi-b*X-b*s*v,V1:V2*s,b:b1*s}
    C=(2*Q*p2-s*s)*phi+rho*n+s*Z+(V1+b*rho+3*H*s)*X-3*H*rho*v
    Cd=sp.expand(sum(sp.diff(C,z)*zd for z,zd in flow.items()))
    out=[{'name':'constraint_propagation','residual':str(sp.factor(Cd+3*H*C)),'passed':sp.factor(Cd+3*H*C)==0}]
    A=sp.symbols('A',positive=True); Cc=H+b*s
    # Jordan continuity and Euler directly in common Einstein coordinate time.
    dJ=n-3*b*X; Phi=phi-b*X; Psi=phi+b*X
    dt=lambda f:sum(sp.diff(f,z)*zd for z,zd in flow.items())+sp.diff(f,A)*A*b*s
    for name,res in [('Jordan_continuity',dt(dJ)-p2*v-3*dt(Phi)),
                     ('Jordan_velocity',dt(A*v)/A+Psi)]:
        out.append({'name':name,'residual':str(sp.factor(res)),'passed':sp.factor(res)==0})
    q=2*Q*b*b; x=-2*b*s/Cc; S=2*phi; D=-2*b*X; F=Q/A**2
    res=dt(S)/A+Cc*S/A+rho/A**4*(A*v)/F-(-2*b*s/A)*(D/(2*q)-S/2)
    out.append({'name':'Jordan_momentum','residual':str(sp.factor(res)),'passed':sp.factor(res)==0})
    return out


def candidate(k,nu):
    u=sp.symbols('u',real=True); beta=(1-k)*(1+3*k)/4; al=math.sqrt(beta)
    ss=(1+k)/(k*(1-3*k)); ex=sp.exp(2*al*u); f=1+ss*ex; j=1+(1-3*beta)*ss*ex
    K=j/f**2; C=(1+ss)*ex/f; A=sp.sqrt(C)
    U=sp.Rational(3,2)+3*ss*(ex-1)**2/(2*f**2)+nu*(1+ss)*u*u/(2*f**2)
    cu=sp.sqrt(2*K); L=sp.diff(sp.log(A),u); b=L/cu; V=2*U
    V1=sp.diff(V,u)/cu; V2=sp.diff(V1,u)/cu; b1=sp.diff(b,u)/cu
    names=['K','Ku','A','L','U','Uu','cu','b','b1','V','V1','V2']
    funcs=sp.lambdify(u,[K,sp.diff(K,u),A,L,U,sp.diff(U,u),cu,b,b1,V,V1,V2],'numpy',cse=True)
    def values(x):return dict(zip(names,map(float,funcs(x))))
    return values, {'beta':beta,'s_parameter':ss,'Fc':ss/(1+ss)}


def experiment(case,protocol):
    if protocol["units"] != {"Q":1.0,"Hv":1.0} or protocol["inverse_modes"] != [0,1,2] or protocol["reserved_mode"] != 3:
        raise ValueError("This fixed numerical protocol is specialized to Q=Hv=1 and its declared four modes")
    vals,par=candidate(case['kappa_model'],case['nu'])
    cv=vals(case['u']); initial_u=[case['u'],case['u_dot'],case['rho_E'],1/cv['A']]
    Hinit=math.sqrt((cv['K']*case['u_dot']**2+cv['V']+case['rho_E'])/3)
    H0=(Hinit+cv['L']*case['u_dot'])/cv['A']; phi0=protocol['initial_phi_E']; ss0=cv['cu']*case['u_dot']
    ki=np.array(protocol['mode_K_over_HE0'])*Hinit*initial_u[3]
    state=initial_u.copy()
    for i,km in enumerate(ki):
        p2=(km/initial_u[3])**2
        X=protocol['initial_bX_over_phi'][i]*phi0/cv['b']
        Z=protocol['initial_bZ_over_HE_phi'][i]*Hinit*phi0/cv['b']
        v=-protocol['initial_minus_v_HE_over_phi'][i]*phi0/Hinit
        n=(-(2*p2-ss0**2)*phi0-ss0*Z-(cv['V1']+cv['b']*case['rho_E']+3*Hinit*ss0)*X+3*Hinit*case['rho_E']*v)/case['rho_E']
        state.extend([phi0,X,Z,n,v])
    def rhs(t,y):
        u,ud,rho,ae=y[:4];c=vals(u);ss=c['cu']*ud
        H=math.sqrt((c['K']*ud**2+c['V']+rho)/3)
        udd=-3*H*ud-c['Ku']*ud**2/(2*c['K'])-c['Uu']/c['K']-c['L']*rho/(2*c['K'])
        out=[ud,udd,(-3*H+c['L']*ud)*rho,H*ae]
        for i,km in enumerate(ki):
            phi,X,Z,n,v=y[4+5*i:9+5*i];p2=(km/ae)**2;pd=-H*phi+(ss*X-rho*v)/2
            out.extend([pd,Z,-3*H*Z-(p2+c['V2']+c['b1']*rho)*X+4*ss*pd-2*(c['V1']+c['b']*rho)*phi-c['b']*rho*(n+c['b']*X),p2*v+3*pd,-phi-c['b']*X-c['b']*ss*v])
        return out
    T=protocol['duration_times_HE0']/Hinit;sc=protocol['solver']
    sol=solve_ivp(rhs,(0,T),state,method=sc['method'],rtol=sc['rtol'],atol=sc['atol'],max_step=T*sc['max_step_fraction'],dense_output=True)
    assert sol.success,sol.message
    epochs=[];all_constraint=[]
    def readout(t):
        y=sol.sol(t);dy=rhs(t,y);u,ud,rho,ae=y[:4];c=vals(u);ss=c['cu']*ud
        H=math.sqrt((c['K']*ud**2+c['V']+rho)/3);Hd=-(ss*ss+rho)/2
        sd=-3*H*ss-c['V1']-c['b']*rho;Cc=H+c['b']*ss
        Ccd=Hd+c['b1']*ss*ss+c['b']*sd;HJ=Cc/c['A'];HJd=(Ccd-Cc*c['b']*ss)/c['A']
        h=HJd/(Cc*HJ);aj=c['A']*ae;F=1/c['A']**2;q=2*c['b']**2;x=-2*c['b']*ss/Cc
        R=rho*ae**3*c['A']/(3*H0**2);rows=[]
        for i,km in enumerate(ki):
            phi,X,Z,n,v=y[4+5*i:9+5*i];pd=dy[4+5*i];vd=dy[8+5*i];p2=(km/ae)**2
            W=p2*v/Cc;Wd=p2*(vd-2*H*v)/Cc-W*Ccd/Cc;S=2*phi
            P=-aj**3*(p2/c['A']**2)*S/(3*H0**2*W);P3=Wd/(Cc*W)
            robs=2*(HJ/H0)**2*aj**3*(P3+2+h)/(3*P)-1
            rmetric=c['b']*X/phi;M=P*(1+pd/(Cc*phi))
            C=(2*p2-ss*ss)*phi+rho*n+ss*Z+(c['V1']+c['b']*rho+3*H*ss)*X-3*H*rho*v
            scale=sum(abs(a) for a in [(2*p2-ss*ss)*phi,rho*n,ss*Z,(c['V1']+c['b']*rho+3*H*ss)*X,3*H*rho*v])+1e-30
            rows.append({'mode':i,'K_over_HJ':math.sqrt(p2)/(c['A']*HJ),'phi_E':phi,'X':X,'Xdot':Z,'number_contrast':n,'velocity':v,'W':W,'W_N':Wd/Cc,'P':P,'P3':P3,'r':robs,'r_metric':rmetric,'M':M,'constraint':C,'constraint_scaled':abs(C)/scale,'momentum_residual':R-M-P*x/2-P*robs*x/(2*q)})
        return {'t':t,'N':math.log(aj),'u':u,'u_dot':ud,'rho_E':rho,'H_E':H,'H_J':HJ,'h_J':h,'H0_J':H0,'a_J':aj,'F':F,'q_true':q,'x_true':x,'R_true':R,'y_true':x/q,'rows':rows}
    for frac in protocol['sample_fractions']:
        e=readout(frac*T);rows=e['rows'];mat=np.array([[1,-r['P']/2,-r['P']*r['r']/2] for r in rows[:3]])
        vec=np.array([r['M'] for r in rows[:3]])
        inferred=np.linalg.solve(mat,vec);R,x,yy=inferred;qi=x/yy
        rr=rows[3];res=R-rr['M']-rr['P']*x/2-rr['P']*rr['r']*yy/2
        e.update({'inferred':{'R':R,'x':x,'y':yy,'q':qi},'matrix':mat.tolist(),'condition_number':float(np.linalg.cond(mat)),'reserved_mode_residual':res})
        epochs.append(e)
    ia,ib=protocol['candidate_calibration_epoch_indices'];ma=[]
    for idx in [ia,ib]:
        inv=epochs[idx]['inferred'];q=inv['q'];ma.append([q,inv['R']*(1-3*q)])
    betainv,kap=np.linalg.solve(ma,[1,1]);beta=1/betainv
    candidate_res=[]
    for idx in protocol['candidate_reserved_epoch_indices']:
        inv=epochs[idx]['inferred'];candidate_res.append(inv['q']/beta+inv['R']*(1-3*inv['q'])*kap-1)
    kaptrue=3*H0**2*par['Fc']/(case['rho_E']/cv['A']**4)
    for t in np.linspace(0,T,301):all_constraint.extend(r['constraint_scaled'] for r in readout(float(t))['rows'])
    mx=lambda f:max(f(e) for e in epochs)
    checks=[('solver_success',sol.success),('propagated_constraint',max(all_constraint)<protocol['checks']['constraint_scaled_max']),
            ('Euler_metric_slip',mx(lambda e:max(abs(r['r']-r['r_metric']) for r in e['rows']))<1e-8),
            ('inverse_q',mx(lambda e:abs(e['inferred']['q']-e['q_true']))<protocol['checks']['inverse_absolute_max']),
            ('inverse_Rxy',mx(lambda e:max(abs(e['inferred'][k]-e[k+'_true']) for k in ['R','x','y']))<protocol['checks']['inverse_absolute_max']),
            ('reserved_mode',mx(lambda e:abs(e['reserved_mode_residual']))<protocol['checks']['reserved_scaled_max']),
            ('candidate_beta',abs(beta-par['beta'])<protocol['checks']['candidate_absolute_max']),
            ('candidate_kappa',abs(kap-kaptrue)<protocol['checks']['candidate_absolute_max']),
            ('candidate_later',max(map(abs,candidate_res))<protocol['checks']['reserved_scaled_max'])]
    return {'case':case,'initial_state':state,'comoving_modes':ki.tolist(),'duration':T,'epochs':epochs,'candidate':{'beta_inferred':beta,'beta_true':par['beta'],'kappa_inferred':kap,'kappa_true':kaptrue,'matrix':ma,'reserved_residuals':candidate_res},'constraint_max':max(all_constraint),'maximum_abs_r_minus_q':mx(lambda e:max(abs(r['r']-e['q_true']) for r in e['rows'])),'checks':[{'name':n,'passed':bool(x)} for n,x in checks],'solver':{'nfev':sol.nfev,'steps':len(sol.t),'success':sol.success}}
