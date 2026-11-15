#!/usr/bin/env python3
"""Independent direct finite-character strip and periodization checks."""
import itertools,json,time,sys,traceback
import numpy as np
from math import pi,exp,cosh,tanh,sqrt
checks=[];details={};start=time.time()
def record(name,ok,**kw):checks.append(dict(name=name,passed=bool(ok),**kw))
def maxabs(x):return float(np.max(np.abs(x)))
def character(n,w):
    w=np.asarray(w,dtype=complex)
    return np.mean(np.exp(-1j*w[...,None]*np.arange(n)/n),axis=-1)
def scalar_noise(s,z):
    ks=np.arange(-(s//2),s//2+1) if s>1 else np.array([0])
    vals=z+2*pi*ks
    delta=character(s,vals)*character(s,-vals)
    return np.sum(delta*delta)/s**2

def symbols(L,kappas,z,u):
    n=L**len(kappas);kap=kappas[-1];ks=np.arange(-(n//2),n//2+1)
    theta=[z[a]+2*pi*ks for a in range(4)]
    D=[character(n,t) for t in theta]; Db=[character(n,-t) for t in theta]
    ds=[D[a]*Db[a] for a in range(4)]
    fs=[2*n*n*(1-np.cos(t/n)) for t in theta]
    reshape=lambda a,v:np.asarray(v).reshape(tuple(n if j==a else 1 for j in range(4)))
    shape=(n,)*4; prod=np.ones(shape,complex);prodD=np.ones(shape,complex);phiall=np.zeros(shape,complex);phase=np.ones(shape,complex)
    for a in range(4):
        prod*=reshape(a,ds[a]);prodD*=reshape(a,D[a]);phiall+=reshape(a,fs[a]);phase*=reshape(a,np.exp(1j*theta[a]*u[a]/n))
    mask=np.ones(shape,bool);mask[(n//2,)*4]=False
    a0=kap*np.prod([ds[a][n//2] for a in range(4)])
    phi0=sum(fs[a][n//2] for a in range(4));delta0=np.array([ds[a][n//2] for a in range(4)]);phic=np.array([fs[a][n//2] for a in range(4)])
    R=[];P=[]
    for mu in range(4):
        numer=prod*reshape(mu,ds[mu]);Z=np.sum((numer[mask]/phiall[mask]))
        A=sum(kap/kappas[-1-m]*scalar_noise(L**m,z[mu]) for m in range(len(kappas)))
        R.append(A+kap*Z);P.append(A+kap*np.sum(numer/phiall))
    R=np.array(R);P=np.array(P);beta=a0*delta0+phi0*R
    nu=np.expm1(1j*z);nub=np.expm1(-1j*z);Delta=nu*nub
    Psi=1-np.sum(phic*R/beta);Sigma=np.sum(Delta/beta)
    ip=1/P;den=np.sum(Delta*ip);res=np.diag(ip)-np.outer(nu*ip,nub*ip)/den
    near=np.empty((4,4),complex);away=near.copy()
    for mu in range(4):
        for v in range(4):
            near[mu,v]=a0*nub[v]/(beta[mu]*beta[v]*Psi)
            away[mu,v]=phi0*nub[v]/(beta[mu]*beta[v]*Sigma)
    K=np.zeros((6,4),complex);zero_direct=np.zeros_like(K);zero_cancel=np.zeros_like(K)
    center=(n//2,)*4;Dzero=np.array([D[a][n//2] for a in range(4)]);vf=n*np.expm1(1j*z/n);phase0=np.exp(1j*np.dot(z,u)/n);prod0=np.prod(Dzero)
    for j,(rho,sigma) in enumerate(itertools.combinations(range(4),2)):
        weightS=prodD*reshape(sigma,D[sigma]);weightR=prodD*reshape(rho,D[rho])
        nR=reshape(rho,n*np.expm1(1j*theta[rho]/n));nS=reshape(sigma,n*np.expm1(1j*theta[sigma]/n))
        for b in range(4):
            summand=kap*phase*(nR*weightS*res[sigma,b]-nS*weightR*res[rho,b])/phiall
            K[j,b]=np.sum(summand);zero_direct[j,b]=summand[center]
            first=prod0*(vf[rho]*Dzero[sigma]*(b==sigma)/beta[sigma]-vf[sigma]*Dzero[rho]*(b==rho)/beta[rho])
            second=prod0/Psi*vf[rho]*vf[sigma]*(R[sigma]/beta[sigma]-R[rho]/beta[rho])*nub[b]/beta[b]
            zero_cancel[j,b]=kap*phase0*(first+second)
    return dict(n=n,beta=beta,phi=phi0,a=a0,P=P,R=R,Psi=Psi,Sigma=Sigma,near=near,away=away,res=res,K=K,zero_direct=zero_direct,zero_cancel=zero_cancel,phiall=phiall,mask=mask)

def sufficient(eta,r0,kap=1,hat=1,L=3):
    eps=np.expm1(eta);b=min(kap,24/pi**2);R=1+hat/(L**2-1)+kap/9;Gamma=max(pi**2/4,R)
    lam=1-4*eta**2*cosh(eta)**2/9;eZ=(4*eta**2/9+4*eta/3)*cosh(eta)
    cZ=(eps*exp(4*eta)+4*exp(3*eta)*eps*(1+exp(eta))+eZ)/(9*lam)
    eR=hat*eps/(L**2-1)+kap*cZ
    rho=(1+pi**2/4*eps)**5-1+(4*eta**2/b+4*eta/sqrt(b))*cosh(eta)*(R+eR)+eR
    ePsi=((4*eta**2+4*eta*r0)*cosh(eta)*(R+eR)+r0**2*eR)/((1-rho)*b)+rho/(1-rho)
    PsiU=kap*(1-r0**2/6)/(kap+r0**2*R);psi0=4*r0**2/pi**2
    f0=(4*eta**2/psi0+4*eta/sqrt(psi0))*cosh(eta)
    bracket=1/((1+rho)*Gamma)-f0/(1-rho);required=.5/((1+rho)*Gamma)
    flags=list(map(bool,[lam>0,rho<=.5,ePsi<=PsiU/2,bracket>=required,f0<=.15]))
    return dict(eta=eta,r0=r0,lambda_alias=lam,rho_beta=float(rho),ePsi=float(ePsi),PsiU=PsiU,bracket=float(bracket),required=float(required),fine_condition=f0,conditions=flags,accepted=all(flags))

def periodized_1d(a,T,x):
    x=x%T
    return (exp(-a*x)+exp(-a*(T-x)))/(1-exp(-a*T))

def main():
    samples=[np.array([.13+.004j,-.21-.003j,.04+.002j,.07-.004j]),np.array([pi+.004j,-pi+.002j,.8-.004j,-1.2+.003j]),np.array([1e-4+.001j,2e-4-.002j,-3e-4+.003j,4e-4+.001j])]
    rows=[]
    for kappas in ([1.],[.7,1.4],[.4,1.,.8]):
        n=3**len(kappas);u=np.array([n-1,n//2,1,0])
        for si,z in enumerate(samples):
            s=symbols(3,kappas,z,u);real=symbols(3,kappas,z.real,u)
            e=maxabs(s['P']-s['beta']/s['phi']); e2=maxabs(s['a']*s['Sigma']-s['phi']*s['Psi'])
            # Relative scale is used only to avoid magnifying small-denominator roundoff.
            rel=e/max(1,maxabs(s['P']));nearaway=maxabs(s['near']-s['away'])/max(1,maxabs(s['near']))
            cancel=maxabs(s['zero_direct']-s['zero_cancel'])/max(1,maxabs(s['zero_cancel']))
            aliasratio=float(np.min(np.abs(s['phiall'][s['mask']])/real['phiall'][real['mask']].real))
            eta=float(max(abs(z.imag)));lam=1-4*eta**2*cosh(eta)**2/9
            record(f'alias_dual_identity_n{n}_sample{si}',rel<1e-10,error=rel)
            record(f'Psi_Sigma_identity_n{n}_sample{si}',e2<1e-9,error=e2)
            record(f'two_residual_formulas_n{n}_sample{si}',nearaway<1e-9,error=nearaway)
            record(f'zero_alias_curvature_cancellation_n{n}_sample{si}',cancel<1e-8,error=cancel)
            record(f'nonzero_alias_pole_bound_n{n}_sample{si}',aliasratio>=lam-1e-10,minimum_ratio=aliasratio,lower_bound=lam)
            b=min(kappas[-1],24/pi**2)
            record(f'real_beta_lower_bound_n{n}_sample{si}',float(np.min(real['beta'].real))>=b-1e-10,minimum=float(np.min(real['beta'].real)),bound=b)
            if si==1:
                shifted=symbols(3,kappas,z+np.array([2*pi,0,0,0]),u)
                per=max(maxabs(s['res']-shifted['res']),maxabs(s['K']-shifted['K']))
                record(f'full_alias_periodic_gluing_n{n}',per<2e-8,error=per)
            rows.append({'n':n,'sample':si,'K_max':maxabs(s['K']),'residual_max':maxabs(s['res'])})
    narrow=sufficient(.005,.57);wide=sufficient(.1,.57)
    record('all_sufficient_strip_conditions_with_f0',narrow['accepted'],**{k:v for k,v in narrow.items() if k!='accepted'})
    record('oversized_sufficient_strip_certificate_rejected',not wide['accepted'],**{k:v for k,v in wide.items() if k!='accepted'})
    # Test omission of f0 as an obligation, independently of success of other sufficient conditions.
    record('fine_curvature_obligation_present','fine_condition' in narrow and len(narrow['conditions'])==5)
    # Periodization is checked against exact infinite geometric sums on the actual mesh.
    for T in [3,5]:
        a=.4;S=(1/tanh(a/2))**4
        one=sum(periodized_1d(a,T,-y) for y in range(T))
        row=one**4
        for r in [3,9]:
            col=sum(periodized_1d(a,T,x/r) for x in range(T*r))**4
            exact=(1/tanh(a/(2*r)))**4
            record(f'periodic_image_unfold_row_T{T}_r{r}',abs(row-S)<1e-9,error=abs(row-S))
            record(f'periodic_image_unfold_column_T{T}_r{r}',abs(col-exact)/exact<1e-12,error=abs(col-exact)/exact,density=r**4)
            record(f'mesh_density_bound_T{T}_r{r}',col<=r**4*S*(1+1e-12),ratio=col/(r**4*S))
            nearest=sum(exp(-a*min(x/r,T-x/r)) for x in range(T*r))**4
            record(f'periodic_image_deletion_rejected_T{T}_r{r}',abs(nearest-col)>1,exact=col,nearest_only=nearest)
    # Anchored quartic estimates: absolute input/output counting, all depths in a closed sum.
    for n in [1,2,6,20]:
        good=sum(3.**(4*s)*(3.**(-2*s))**4 for s in range(n+1))
        exact=(1-3.**(-4*(n+1)))/(1-3.**-4)
        bad=sum(3.**(4*s)*(3.**(-s))**4 for s in range(n+1))
        record(f'quartic_geometric_sum_depth{n}',abs(good-exact)<1e-12,sum=good)
        record(f'uncurled_amplitude_mutation_depth{n}_rejected',bad>1/(1-3.**-4)+.5,sum=bad,uniform_curvature_bound=1/(1-3.**-4))
    details['sample_bounds']=rows

exception=None
try:main()
except Exception:
    exception=traceback.format_exc();traceback.print_exc()
print(json.dumps({'schema':'review-uniform-soft-independent02-v1','passed':sum(x['passed'] for x in checks),'total':len(checks),'checks':checks,'details':details,'exception':exception,'elapsed_seconds':time.time()-start,'finite_scope_only':True,'author_or_predecessor_helpers_imported':False},indent=2))
sys.exit(0 if exception is None and all(x['passed'] for x in checks) else 1)
