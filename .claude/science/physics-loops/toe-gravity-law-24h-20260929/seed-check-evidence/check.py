import sympy as s
from itertools import product
from fractions import Fraction as F

# Independent coordinates: three diagonal and three face strains.
a,b,w,K=s.symbols('alpha beta w K', nonzero=True, real=True)
v=s.Matrix(s.symbols('v11 v22 v33 v12 v13 v23'))
P=s.Matrix(s.symbols('P11 P22 P33 P12 P13 P23'))
L=(a*(sum(v[i]**2 for i in range(3))+2*sum(v[i]**2 for i in range(3,6)))+b*sum(v[:3])**2)/w
Hess=s.hessian(L,list(v))
vel=Hess.inv()*P
T=s.factor((P.dot(vel)-L.subs(dict(zip(v,vel)), simultaneous=True))/w)
c=b/(a+3*b)
expected=(sum(P[i]**2 for i in range(3))-c*sum(P[:3])**2)/(4*a)+sum(P[i]**2 for i in range(3,6))/(8*a)
assert s.simplify(T-expected)==0
print('Legendre dual: diagonal 1/(4 alpha), independent face 1/(8 alpha), c=beta/(alpha+3 beta); exact')
print('Kinetic Hessian determinant:',s.factor(Hess.det()))

N=s.symbols('N00 N10 N01 N11'); M=s.symbols('M00 M10 M01 M11')
dN=N[0]-N[1]-N[2]+N[3]; dM=M[0]-M[1]-M[2]+M[3]
# Standard canonical bracket, spatial constraint +K R1. R1 face derivative is 2*dN.
xi=lambda np,mp,nq,mq:K*(nq*mp-np*mq)/(4*a)
Gface=xi(N[1],M[1],N[3],M[3])-xi(N[0],M[0],N[2],M[2])+xi(N[2],M[2],N[3],M[3])-xi(N[0],M[0],N[1],M[1])
for name,corners in [('four',(0,1,2,3)),('diagonal',(0,3)),('antidiagonal',(1,2)),('one',(0,))]:
    avg=lambda xs:sum(xs[i] for i in corners)/len(corners)
    B=K*(avg(M)*dN-avg(N)*dM)/(2*a)
    residual=s.factor(B-Gface)
    if name!='one':assert residual==0
    else:
        witness={N[0]:0,N[1]:1,N[2]:0,N[3]:0,M[0]:1,M[1]:0,M[2]:0,M[3]:0}
        print('One-corner witness: B=',s.simplify(B.subs(witness)),' G=',s.simplify(Gface.subs(witness)))
        assert s.simplify(B.subs(witness)-2*Gface.subs(witness))==0
    print('Face polynomial residual',name,':',residual)

N0,M0,DN,DM,DjN,DjM,C=s.symbols('N0 M0 DN DM DjN DjM c')
rN=-DN+DjN; rM=-DM+DjM
Bdiag=s.expand(K*(M0*(rN+2*C*DN)-N0*(rM+2*C*DM))/(2*a))
Gdiag=K*(M0*DjN-N0*DjM)/(2*a)
assert s.simplify(Bdiag-Gdiag-K*(2*C-1)*(M0*DN-N0*DM)/(2*a))==0
print('Diagonal residual:',s.factor(Bdiag-Gdiag))
print('At c=1/2: Bdiag=K(M Delta_j N-N Delta_j M)/(2 alpha)=2 D_j^- xi_j')
print('Standard {h,P}=+1, C=T+sigma K R1: B=sigma G at c=1/2; action Hamiltonian potential has sigma=-1')

# Exhaustive lapse-basis pairs on 3^3, directly from local incidence stencils.
side=3; sites=list(product(range(side),repeat=3)); pairs=[(0,1),(0,2),(1,2)]
sh=lambda x,j,d=1:tuple((x[t]+(d if t==j else 0))%side for t in range(3))
# Use alpha=1,K=4, hence xi has unit coefficient.
checks=0
for xn in sites:
    for xm in sites:
        n={x:int(x==xn) for x in sites}; m={x:int(x==xm) for x in sites}
        X=lambda x,j:n[sh(x,j)]*m[x]-n[x]*m[sh(x,j)]
        for x in sites:
            for j in range(3):
                B=2*(m[x]*(n[sh(x,j)]+n[sh(x,j,-1)]-2*n[x])-n[x]*(m[sh(x,j)]+m[sh(x,j,-1)]-2*m[x]))
                assert B==2*(X(x,j)-X(sh(x,j,-1),j)); checks+=1
            for i,j in pairs:
                z=[x,sh(x,i),sh(x,j),sh(sh(x,i),j)]
                dn=n[z[0]]-n[z[1]]-n[z[2]]+n[z[3]]; dm=m[z[0]]-m[z[1]]-m[z[2]]+m[z[3]]
                g=X(sh(x,i),j)-X(x,j)+X(sh(x,j),i)-X(x,i)
                for subset in [(0,1,2,3),(0,3),(1,2)]:
                    bv=F(2,len(subset))*(sum(m[z[t]] for t in subset)*dn-sum(n[z[t]] for t in subset)*dm)
                    assert bv==g; checks+=1
print('3^3 all 729 ordered delta-lapse pairs: exact coefficient identities checked=',checks)

# Trace residual projected on transverse slice.
n={x:int(x==(0,0,0)) for x in sites}; m={x:int(x==(1,0,0)) for x in sites}
D=lambda f,x:sum(f[sh(x,j)]+f[sh(x,j,-1)]-2*f[x] for j in range(3))
z={x: -2*(m[x]*D(n,x)-n[x]*D(m,x)) for x in sites}
assert z[(0,0,0)]==2 and z[(1,0,0)]==-2
print('c=0 minus c=1/2 yy slice sums, alpha=1,K=4:',[sum(z[x] for x in sites if x[0]==u) for u in range(side)])
print('All 2 D_y^- xi_y have zero y,z slice sums: nonzero residual cannot be a relabelling')

# Generic tensor variation and source identity, no coordinate rotation needed.
px,py,pz=s.symbols('px py pz',real=True); p=s.Matrix([px,py,pz]); p2=p.dot(p)
h11,h22,h33,h12,h13,h23=s.symbols('h11 h22 h33 h12 h13 h23',real=True)
h=s.Matrix([[h11,h12,h13],[h12,h22,h23],[h13,h23,h33]])
zeta=s.symbols('zeta',real=True); hp=h*p
R1=p2*s.trace(h)-(p.T*h*p)[0]; R2=-p2*s.trace(h*h)/4+hp.dot(hp)/2-(p.T*h*p)[0]*s.trace(h)/2+p2*s.trace(h)**2/4
hs=h+p*p.T*zeta; hsp=hs*p
R1s=p2*s.trace(hs)-(p.T*hs*p)[0]; R2s=-p2*s.trace(hs*hs)/4+hsp.dot(hsp)/2-(p.T*hs*p)[0]*s.trace(hs)/2+p2*s.trace(hs)**2/4
assert s.expand(R1s-R1)==0 and s.expand(R2s-R2)==0
print('R1 and R2 invariance under h->h+p p^T zeta: exact generic-vector polynomial identity')
v11,v22,v33,v12,v13,v23,zd,zdd=s.symbols('v11 v22 v33 v12 v13 v23 zd zdd', real=True)
V=s.Matrix([[v11,v12,v13],[v12,v22,v23],[v13,v23,v33]])
Vs=V+p*p.T*zd
Rdot=p2*s.trace(V)-(p.T*V*p)[0]
kin0=(a*s.trace(V*V)+b*s.trace(V)**2)/w
kins=(a*s.trace(Vs*Vs)+b*s.trace(Vs)**2)/w
deltafield=kins-kin0-2*a*R1*zdd/w
boundaryder=-2*a*(Rdot*zd+R1*zdd)/w
remainder=(a+b)*(2*p2*s.trace(V)*zd+p2**2*zd**2)/w
assert s.expand(deltafield-boundaryder-remainder)==0
E,Edd,ptheta=s.symbols('E Edd ptheta')
deltasource=2*a*E*zdd/(K*w**2)+ptheta*zeta/2
sourceboundaryder=2*a*(E*zdd-Edd*zeta)/(K*w**2)
assert s.expand(deltasource-sourceboundaryder-zeta*(2*a*Edd/(K*w**2)+ptheta/2))==0
print('Generic finite gradient variation: exact remainder=(alpha+beta)(2 p^2 tr(V) zdot+p^4 zdot^2)/w')
print('At beta=-alpha, delta L_field=d[-2 alpha R1 zetadot/w]/dt; source residual=zeta[2 alpha e_ddot/(K w^2)+p.Theta.p/2]')

# Exact stationary two-wave witness independently factored into spin response and symbol contraction.
e=s.sqrt(2146)/65; q=s.Matrix([-8,2,0])/s.sqrt(65)
s1=s.Matrix([39,25,0])/65; s2=s.Matrix([-25,39,0])/65
chi1=s.Matrix([s1[0]-s.I*s1[1],e]); chi2=s.Matrix([s2[0]-s.I*s2[1],e])
sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.Matrix([[1,0],[0,-1]])]
resp=s.Matrix([s.simplify((s.conjugate(chi1).T*x*chi2)[0]) for x in sigma])
Theta=(resp*(s1+s2).T+(s1+s2)*resp.T)/4
pTheta=s.simplify(q.T*Theta)
ptp=s.simplify((q.T*Theta*q)[0]); expected=128*s.sqrt(2146)*(1-s.I)/65**4
assert s.simplify(ptp-expected)==0 and all(s.simplify(x)!=0 for x in pTheta)
print('Two-wave energy squared:',s.factor(s1.dot(s1)),s.factor(s2.dot(s2)))
print('q-symbol p:',list(q)); print('p.Theta.p:',ptp)
print('p.Theta_sym:',[s.factor(x) for x in pTheta])
print('Independent checks complete. No repository runner imported or executed.')

# A one-corner global face obstruction, not merely a mismatch with a chosen xi.
n={x:int(x==(1,0,0)) for x in sites}; m={x:int(x==(0,0,0)) for x in sites}
face_sum=0
for x in sites:
    z=[x,sh(x,0),sh(x,1),sh(sh(x,0),1)]
    dn=n[z[0]]-n[z[1]]-n[z[2]]+n[z[3]]; dm=m[z[0]]-m[z[1]]-m[z[2]]+m[z[3]]
    face_sum+=2*(m[x]*dn-n[x]*dm)
assert face_sum==-2
print('One-corner global xy-face coefficient sum, alpha=1,K=4:',face_sum,'; every relabelling has sum 0')
weights=s.symbols('w00 w10 w01 w11')
Bweighted=K*(sum(weights[i]*M[i] for i in range(4))*dN-sum(weights[i]*N[i] for i in range(4))*dM)/(2*a)
poly=s.Poly(s.expand(4*a*(Bweighted-Gface)/K),*N,*M)
sol=s.linsolve(poly.coeffs(),weights)
print('All fixed normalized local linear face timings closing the polynomial:',sol)
