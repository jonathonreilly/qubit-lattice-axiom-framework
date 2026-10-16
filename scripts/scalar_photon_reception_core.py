"""Root exact primitive-reception-gain candidate, generated from full solutions."""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import hashlib,json
from pathlib import Path
import sympy as s
checks={};details={}

def zero(name,expr):
    arr=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
    val=[s.factor(s.cancel(s.expand(v))) for v in arr]
    checks[name]=all(v==0 for v in val)
    if not checks[name]:details[name]=[str(v) for v in val]

def coefficients(C,d,e,h,beta,k,K,dt,L):
    AA=h+C-beta;FF=e-d*beta;bb1=dt(d)+(h-2*beta)*d
    bb0=L(FF)+(h-2*beta)*FF;MM=-2*beta
    NN=-2*dt(beta)+2*beta*beta-2*(h+C)*beta;zz=2*beta+k
    return [-zz,C-beta,L(AA)-zz*AA+K-dt(h),
            d,dt(d)+bb1-zz*d,L(bb1)-zz*bb1+MM,
            FF,L(FF)+bb0-zz*FF,L(bb0)-zz*bb0+MM*h+NN,
            2*MM,L(MM)-zz*MM+2*NN,
            L(NN)-(h+zz)*NN-MM*(dt(h)+h*h)-2*K*beta]

def general_commutator():
    eta,r=s.symbols('eta r');a=s.Function('a')(eta)
    dt=lambda v:s.diff(v,eta)/a;L=lambda v:(s.diff(v,eta)+s.diff(v,r))/a
    h=dt(a)/a;C=s.Function('C')(eta);g=s.Function('g')(eta+r)
    beta=dt(g)/g;V=s.Function('V')(eta,r);B=s.Function('B')(eta,r)
    W=L(V)-2*beta*V+2*beta*B;U=-dt(V)-(C-beta)*V
    N=dt(W-2*beta*B)+(h+C-beta)*(W-2*beta*B)+L(U)+(h-2*beta)*U
    K=dt(C)+h*C
    zero('generic_gained_commutator',N+K*V)
    zero('generic_reception_beta_constraint',L(beta)-2*dt(beta)-h*beta)
    # Direct abstract coefficient expansion retaining the two path identities.
    t=s.symbols('tau');h,C,d,e,k=[s.Function(n)(t) for n in ['h','C','d','e','k']]
    b,bp,bpp=s.symbols('beta beta_prime beta_second')
    DT=lambda z:s.diff(z,t)+s.diff(z,b)*bp+s.diff(z,bp)*bpp
    LC=lambda z:s.diff(z,t)+s.diff(z,b)*(2*bp+h*b)+s.diff(z,bp)*(2*bpp+2*h*bp+(s.diff(h,t)+h*h)*b)
    K=DT(C)+h*C
    wt,lw,w,llxt,lxt,xt,llx,lx,x,btt,bt,bb,O=s.symbols('Wt LW W LLXt LXt Xt LLX LX X Btt Bt B O')
    AA=h+C-b;FF=e-d*b;bb1=DT(d)+(h-2*b)*d
    bb0=LC(FF)+(h-2*b)*FF;MM=-2*b;NN=-2*bp+2*b*b-2*(h+C)*b
    terms=[(1,wt),(AA,w),(d,lxt),(bb1,xt),(FF,lx),(bb0,x),(MM,bt),(NN,bb)]
    image={wt:O-h*lw-DT(h)*w,w:lw,lxt:llxt,xt:lxt,lx:llx,x:lx,
           bt:2*btt-(DT(h)+h*h)*bb+xt+h*x,bb:2*bt-h*bb+x}
    N=sum(c*v for c,v in terms)
    op=sum(LC(c)*v+c*image[v] for c,v in terms)-(2*b+k)*N+K*(w-2*b*bb)
    th=coefficients(C,d,e,h,b,k,K,DT,LC)
    cols=[wt,lw,w,llxt,lxt,xt,llx,lx,x,btt,bt,bb]
    zero('complete_twelve_column_expansion',op-O-sum(c*v for c,v in zip(th,cols)))
    zero('proposed_beta_coefficient',th[9]+4*b)
    zero('proposed_C_coefficient',th[1]+b-C)
    zero('proposed_e_coefficient',th[6]+th[3]*b-e)

def physical():
    t=s.symbols('t',positive=True);eta=s.symbols('eta',negative=True);r=s.symbols('r',positive=True);ell=s.symbols('ell',integer=True,positive=True)
    pp=s.Rational(3,2);y=s.Rational(5,2);speed=s.sqrt(y);sigma=3*pp-2
    b=sigma/speed;aE=t**pp;Ac=t**sigma;H=pp/t;v=speed/t
    rr=(2*pp-y)/t**2;rho=rr/Ac;pot=(3*pp*pp-2*pp+y/2)/t**2
    DP=lambda z:s.diff(z,t)/v
    force=s.simplify(DP(pot)+rho*DP(Ac));mass=s.simplify(DP(DP(pot))+rho*DP(DP(Ac)))
    zero('background_Friedmann',3*H*H-v*v/2-rr-pot)
    zero('background_Raychaudhuri',-2*s.diff(H,t)-v*v-rr)
    zero('background_scalar',s.diff(v,t)+3*H*v+force)
    zero('background_dust',s.diff(rho,t)+3*H*rho)
    P,j,jw,ve=s.symbols('P j jw ve');ys=[P,j,jw,ve]
    pdt=(speed*j/b-(2*pp-y)*ve)/2-pp*P
    density=s.simplify((-6*pp*(pdt+pp*P)-(speed/b)*jw+y*P-(force*t*t/b)*j)/(2*pp-y))
    jwdt=s.simplify((1-3*pp)*jw-mass*t*t*j-b*b*(2*pp-y)*density+4*b*speed*pdt-2*b*force*t*t*P)
    vedt=-P-j-(sigma+1)*ve
    ff=s.Matrix([pdt,jw,jwdt,vedt]);M=ff.jacobian(ys)
    total=lambda z:s.diff(z,t)+sum(s.diff(z,yy)*fy/t for yy,fy in zip(ys,ff))
    zero('generic_original_dust_continuity',total(density)-3*pdt/t)
    Wphys=j/b;Wdot=jw/(b*t)
    zero('generic_original_scalar',total(Wdot)+3*H*Wdot+mass*Wphys+b*rr*density-4*v*pdt/t+2*force*P)
    zero('generic_original_spatial_pressure',2*(total(pdt/t)+4*H*pdt/t+(2*s.diff(H,t)+3*H*H)*P)-v*Wdot+v*v*P+DP(pot)*Wphys)
    exponent_list=[0,s.Rational(-3,2),s.Integer(-2),s.Rational(-5,2)]
    eigens={}
    for m in exponent_list:
        vec=(M-m*s.eye(4)).nullspace()[0];vec=vec/vec[0]
        zero(f'eigenmode_{m}',M*vec-m*vec);eigens[int(-2*m)]=vec
    a=256/eta**8;dt=lambda z:s.diff(z,eta)/a;L=lambda z:(s.diff(z,eta)+s.diff(z,r))/a
    h=dt(a)/a;rate=(-eta/2)**7;q=sigma*rate;G=rate;R=s.Rational(1,2)*rate**2
    C=R/G;d=2/G;e=1+d*(h-q);K=dt(C)+h*C;k=dt(K)/K
    u=eta+r;gain=(u+11)/10;gain_u=s.Rational(1,10);beta=dt(gain)/gain
    th=[s.factor(z) for z in coefficients(C,d,e,h,beta,k,K,dt,L)]
    point={eta:-2,r:1};th0=s.Matrix([s.factor(z.subs(point)) for z in th])
    cols_at={};rhs_at={};mode_report={}
    for n,vec in eigens.items():
        Pfield=eta**n*r**ell;Jfield=vec[1]*Pfield
        Zfield=-128*vec[3]*eta**(n-7)*r**ell
        Y=-Pfield-Jfield+s.diff(Zfield,r)/a
        integral=sum(s.binomial(n,jj)*u**(n-jj)*(-1)**jj*r**(ell+jj+1)/(ell+jj+1) for jj in range(n+1))
        X=gain*Pfield;B=a*gain*integral;W=gain*Y+2*gain_u*integral
        zero(f'n={n}/original_Euler',dt(Zfield)+Pfield+Jfield)
        zero(f'n={n}/original_momentum',dt(Zfield)+C*Zfield+d*dt(Pfield)+e*Pfield)
        zero(f'n={n}/regular_harmonic',s.diff(r**ell,r,2)+2*s.diff(r**ell,r)/r-ell*(ell+1)*r**ell/r**2)
        zero(f'n={n}/path_identity',L(B)-2*dt(B)+h*B-X)
        zero(f'n={n}/path_derivative',L(dt(B))-2*dt(dt(B))+(dt(h)+h*h)*B-dt(X)-h*X)
        N=dt(W-2*beta*B)+(h+C-beta)*(W-2*beta*B)+L(d*(dt(X)-beta*X)+e*X)+(h-2*beta)*(d*(dt(X)-beta*X)+e*X)
        zero(f'n={n}/hidden_velocity',N+K*gain*Zfield)
        cols=[dt(W),L(W),W,L(L(dt(X))),L(dt(X)),dt(X),L(L(X)),L(X),X,dt(dt(B)),dt(B),B]
        O=L(dt(W))+h*L(W)+dt(h)*W
        cv=[s.factor(z.subs(point)) for z in cols];ov=s.factor((-O).subs(point))
        zero(f'n={n}/physical_twelve_column_identity',sum(c*z for c,z in zip(th0,cv))-ov)
        cols_at[n]=cv;rhs_at[n]=ov;mode_report[n]=[str(z) for z in vec]
    rows=[];target=[];ids=[];ns=[0,3,4,5]
    for i in range(48):
        n=ns[i%4];ll=i+2
        rows.append([z.subs(ell,ll) for z in cols_at[n]]);target.append(rhs_at[n].subs(ell,ll));ids.append({'n':n,'ell':ll})
    matrix=s.Matrix(rows);target=s.Matrix(target);rank=matrix.rank();aug=matrix.row_join(target).rank()
    # Rank failure is recorded as a scientific outcome, not concealed by a new fixture.
    checks['candidate_rank_twelve_attained']=rank==12
    selected=list(matrix.T.rref()[1]);minor=matrix[selected,:]
    report={'rank':rank,'augmented_rank':aug,'rows':len(rows),'selected_rows':selected,
            'mode_ids':[ids[i] for i in selected],'theta_at_point':[str(z) for z in th0],
            'eigenvectors':mode_report,'point':{'eta':-2,'r':1,'t':1,'u':-1},
            'source_gain':'(u+11)/10','data_role':'Exact constructed original-action solutions; no observed arrays'}
    if rank==12:
        solved=minor.inv()*target[selected,:]
        zero('actual_observed_coefficient_recovery',solved-th0)
        betar=-solved[9]/4;Cr=solved[1]+betar;dr=solved[3];er=solved[6]+dr*betar
        qr=4-(er-1)/dr;Gr=2/dr;Rr=2*Cr/dr
        zero('recovered_gain_background',s.Matrix([betar-s.Rational(1,10),Cr-s.Rational(1,2),dr-2,er-4,qr-s.Rational(5,2),Gr-1,Rr-s.Rational(1,2)]))
        report['minor_determinant']=str(s.factor(minor.det()))
        report['recovered']={'beta':str(betar),'C':str(Cr),'d':str(dr),'e':str(er),'q':str(qr),'G':str(Gr),'R':str(Rr)}
    else:
        report['null_vectors']=[[str(z) for z in vv] for vv in matrix.nullspace()]
    return report


def run_checks():
    checks.clear(); details.clear()
    general_commutator(); case=physical()
    return [{"name":n,"pass":bool(v)} for n,v in checks.items()], {"failures":dict(details),"fixture":case}
