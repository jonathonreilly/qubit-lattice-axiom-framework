"""Root independent-channel reception-gain candidate; exact forward fields."""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import hashlib, importlib.util, json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
checks={};details={}
def zero(name,expr):
    seq=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
    vals=[s.factor(s.cancel(s.together(z))) for z in seq]
    checks[name]=all(z==0 for z in vals)
    if not checks[name]: details[name]=[str(z) for z in vals]

def coefficients(C,D,E,h,sigma,ss,v,k,K,dt,L):
    reduce=lambda x:s.factor(s.cancel(s.together(x)))
    A=reduce(h+C-sigma); m=reduce(L(D)+(h-2*sigma)*D); n=reduce(L(E)+(h-2*sigma)*E)
    tt=reduce(dt(ss)+A*ss+v); j=reduce(dt(v)+A*v); z=reduce(2*sigma+k); J=reduce(dt(h)+h*h)
    return [-z,C-sigma,L(A)-z*A+K-dt(h),
            D,L(D)+m-z*D,L(m)-z*m+2*h*ss+tt,
            E,L(E)+n-z*E,L(n)-z*n+J*ss+h*tt+j,
            ss,2*ss,L(ss)+(h-z)*ss+2*tt,
            L(tt)-z*tt-J*ss+2*j+K*ss,
            L(j)-(h+z)*j-(dt(J)+h*J)*ss-J*tt+K*v]

def general_expansion():
    # Separate abstract jet identities from the genuinely forward fixture.
    Wt,LW,W,LLXt,LXt,Xt,LLX,LX,X,Xtt,Bttt,Btt,Bt,B,O=s.symbols('Wt LW W LLXt LXt Xt LLX LX X Xtt Bttt Btt Bt B O')
    A,D,m,E,n,ss,tt,j,z,K,v,h,hp,Jp=s.symbols('A D m E n ss tt j z K v h hp Jp')
    LA,LD,Lm,LE,Ln,Ls,Lt,Lj=s.symbols('LA LD Lm LE Ln Ls Lt Lj')
    J=hp+h*h
    terms=[(1,Wt,0),(A,W,LA),(D,LXt,LD),(m,Xt,Lm),(E,LX,LE),(n,X,Ln),(ss,Btt,Ls),(tt,Bt,Lt),(j,B,Lj)]
    image={Wt:O-h*LW-hp*W,W:LW,LXt:LLXt,Xt:LXt,LX:LLX,X:LX,
           Btt:2*Bttt+h*Btt-J*Bt-(Jp+h*J)*B+Xtt+2*h*Xt+J*X,
           Bt:2*Btt-J*B+Xt+h*X,B:2*Bt-h*B+X}
    N=sum(c*obs for c,obs,_ in terms)
    actual=sum(lc*obs+c*image[obs] for c,obs,lc in terms)-z*N+K*(W+ss*Bt+v*B)
    th=[-z,A-h,LA-z*A+K-hp,D,LD+m-z*D,Lm-z*m+2*h*ss+tt,
        E,LE+n-z*E,Ln-z*n+J*ss+h*tt+j,ss,2*ss,Ls+(h-z)*ss+2*tt,
        Lt-z*tt-J*ss+2*j+K*ss,Lj-(h+z)*j-(Jp+h*J)*ss-J*tt+K*v]
    cols=[Wt,LW,W,LLXt,LXt,Xt,LLX,LX,X,Xtt,Bttt,Btt,Bt,B]
    zero('generic_complete_fourteen_expansion',actual-O-sum(c*x for c,x in zip(th,cols)))
    C,beta,sigma,rho,rhop,k=s.symbols('C beta sigma rho rhop k')
    ss=2*(rho-1);sp=2*rhop;v=-ss*h-2*rho*beta
    theta12=2*sp+(h-2*sigma-k)*ss+2*(sp+(h+C-sigma)*ss+v)
    zero('generic_beta_extraction',theta12-(4*sp+(h+2*(C-sigma)-2*sigma-k)*ss-4*rho*beta))

def physical():
    # Import our immutable original-equation fixture, not an inverse-generated design.
    import scalar_photon_reception_core as base
    source=Path(base.__file__)
    baseline=base.physical()
    checks['inherited_original_fixture_all_checks']=all(base.checks.values())
    eta=s.symbols('eta',negative=True);r=s.symbols('r',positive=True);ell=s.symbols('ell',integer=True,positive=True)
    a=256/eta**8;dt=lambda f:s.diff(f,eta)/a;L=lambda f:(s.diff(f,eta)+s.diff(f,r))/a
    h=dt(a)/a;rate=(-eta/2)**7;C=rate/2;d=2/rate;e=s.Integer(4);K=dt(C)+h*C;k=dt(K)/K
    u=eta+r;g=(u+11)/10;f=(u+21)/16;rho=f/g;beta=dt(g)/g;sigma=dt(f)/f
    D=rho*d;E=rho*(e-d*beta);ss=2*(rho-1);v=-ss*h-2*rho*beta
    theta=[s.factor(s.cancel(z)) for z in coefficients(C,D,E,h,sigma,ss,v,k,K,dt,L)]
    point={eta:-2,r:1};th0=s.Matrix([s.factor(z.subs(point)) for z in theta])
    zero('relative_gain_reception_identity',L(rho)-2*dt(rho))
    zero('relative_gain_time_identity',dt(rho)-rho*(sigma-beta))
    zero('physical_beta_recovery',(4*dt(ss)+(h+2*theta[1]+theta[0])*ss-theta[11])/(4*rho)-beta)
    cols_at={};targets_at={}
    for n in [0,3,4,5]:
        vec=[s.sympify(z) for z in baseline['eigenvectors'][n]]
        P=eta**n*r**ell;Jfield=vec[1]*P;Z=-128*vec[3]*eta**(n-7)*r**ell
        Y=-P-Jfield+s.diff(Z,r)/a
        I=sum(s.binomial(n,ii)*u**(n-ii)*(-1)**ii*r**(ell+ii+1)/(ell+ii+1) for ii in range(n+1))
        I1=s.diff(I,eta);X=g*P;B=a*g*I
        W=f*Y+2*(g-f)*I1+I/5
        T=W+ss*dt(B)+v*B;F=D*dt(X)+E*X;V=f*Z
        zero(f'n{n}/recorded_actual_event_primitive',T-f*Y)
        zero(f'n{n}/original_momentum',dt(V)+(C-sigma)*V+F)
        zero(f'n{n}/original_characteristic',L(V)-2*sigma*V-T)
        zero(f'n{n}/path_third_derivative',L(dt(dt(B)))-2*dt(dt(dt(B)))-h*dt(dt(B))+(dt(h)+h*h)*dt(B)+(dt(dt(h)+h*h)+h*(dt(h)+h*h))*B-dt(dt(X))-2*h*dt(X)-(dt(h)+h*h)*X)
        N=dt(T)+(h+C-sigma)*T+L(F)+(h-2*sigma)*F
        zero(f'n{n}/hidden_velocity',N+K*V)
        cols=[dt(W),L(W),W,L(L(dt(X))),L(dt(X)),dt(X),L(L(X)),L(X),X,dt(dt(X)),dt(dt(dt(B))),dt(dt(B)),dt(B),B]
        O=L(dt(W))+h*L(W)+dt(h)*W
        cv=[s.factor(z.subs(point)) for z in cols];ov=s.factor((-O).subs(point))
        zero(f'n{n}/full_fourteen_relation',sum(t*x for t,x in zip(th0,cv))-ov)
        cols_at[n]=cv;targets_at[n]=ov
    rows=[];targets=[];ids=[]
    for ii in range(48):
        n=[0,3,4,5][ii%4];ll=ii+2
        rows.append([z.subs(ell,ll) for z in cols_at[n]]);targets.append(targets_at[n].subs(ell,ll));ids.append({'n':n,'ell':ll})
    matrix=s.Matrix(rows);target=s.Matrix(targets);rank=matrix.rank();aug=matrix.row_join(target).rank()
    checks['rank_fourteen_attained']=rank==14
    piv=list(matrix.T.rref()[1]);minor=matrix[piv,:]
    report={'rank':rank,'augmented_rank':aug,'selected_rows':piv,'mode_ids':[ids[i] for i in piv],
            'theta_at_point':[str(z) for z in th0],'row_count':len(rows),
            'fixture_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'inherited_fixture_controls':{'passed':sum(base.checks.values()),'failed':sum(not q for q in base.checks.values())},
            'scope':'Exact original-action local solid harmonics, no observed data; independent positive reception gains, actual-event convention'}
    if rank==14:
        solution=minor.inv()*target[piv,:]
        zero('full_observed_coefficient_recovery',solution-th0)
        rhor=1+solution[10]/4;dr=solution[3]/rhor
        # Drift uses derivative of measured coefficient function, separately verified exactly above.
        br=s.factor(((4*dt(ss)+(h+2*theta[1]+theta[0])*ss-theta[11])/(4*rho)).subs(point))
        sr=br+s.factor((dt(rho)/rho).subs(point));Cr=solution[1]+sr;er=solution[6]/rhor+dr*br
        zero('gain_background_recovery',s.Matrix([rhor-s.Rational(5,4),br-s.Rational(1,10),sr-s.Rational(1,20),Cr-s.Rational(1,2),dr-2,er-4]))
        report.update({'minor_determinant':str(s.factor(minor.det())),'recovered':{key:str(z) for key,z in [('rho',rhor),('beta',br),('sigma',sr),('C',Cr),('d',dr),('e',er)]}})
    else:report['null_vectors']=[[str(z) for z in vv] for vv in matrix.nullspace()]
    return report


def run_checks():
    checks.clear(); details.clear()
    general_expansion(); case=physical()
    return [{"name":n,"pass":bool(v)} for n,v in checks.items()], {"failures":dict(details),"fixture":case}
