"""Independent exact tests; finite evidence only, no uniform-norm certificate."""
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial
import json

class Q3:
    def __init__(self,a=0,b=0):
        if isinstance(a,Q3): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self,t):
        t=Q3(t); return Q3(self.a+t.a,self.b+t.b)
    __radd__=__add__
    def __neg__(self): return Q3(-self.a,-self.b)
    def __sub__(self,t): return self+-Q3(t)
    def __rsub__(self,t): return Q3(t)+-self
    def __mul__(self,t):
        t=Q3(t); return Q3(self.a*t.a+3*self.b*t.b,self.a*t.b+self.b*t.a)
    __rmul__=__mul__
    def __truediv__(self,t):
        t=Q3(t); den=t.a*t.a-3*t.b*t.b
        return self*Q3(t.a/den,-t.b/den)
    def __rtruediv__(self,t): return Q3(t)/self
    def __pow__(self,n):
        if n<0: return (1/self)**(-n)
        out=Q3(1); t=self
        while n:
            if n&1: out=out*t
            t=t*t;n//=2
        return out
    def rational(self):
        assert self.b==0,(self.a,self.b)
        return self.a

root=Q3(0,1); r=Q3(-2,1)

def image_green(a,m):
    """Sum_q c_(a-mq), sum_q q c_(a-mq), by geometric series."""
    q,s=divmod(a,m); u=r**m
    z=root*(r**s+r**(m-s))/(1-u)
    first=q*z+root*(r**(m-s)-r**(m+s))/(1-u)**2
    return z,first

def b3(x):
    z=abs(x)
    if z<1:return (4-6*z*z+3*z*z*z)/6
    if z<2:return (2-z)**3/6
    return F(0)

def b2_primitive(x):
    # Integral of the centered degree-two cardinal B-spline from -infinity.
    return sum(F(c,6)*max(x+F(3,2)-i,0)**3 for i,c in enumerate((1,-3,3,-1)))

def winding_path(start,end,n):
    # Fixed lift, no shortest representative and no harmonic projection.
    row=[0]*n
    if start<=end:
        for p in range(start,end):row[p%n]+=1
    else:
        for p in range(end,start):row[p%n]-=1
    return row

def direct_images(L,m):
    n=L*m;S=[];M=[];S1=[]
    for y in range(n):
        t=F(y,L); indices=range(y//L-2,y//L+3)
        a=[];winding=Q3()
        for j in range(m):
            z=Q3();w=Q3()
            for s in indices:
                g,first=image_green(s-j,m);z+=b3(t-s)*g;w+=b3(t-s)*first
            a.append(z.rational());winding+=w
        winding=winding.rational();S.append(a)
        row=[-winding]*n
        for j in range(m):
            p=winding_path(L*j,y,n)
            row=[v+a[j]*p[e] for e,v in enumerate(row)]
        M.append(row)
        b=[]
        for j in range(m):
            z=Q3()
            for s in range(y//L-2,(y+1)//L+4):
                mass=b2_primitive(F(y+1,L)-s+F(1,2))-b2_primitive(t-s+F(1,2))
                g,_=image_green(s-1-j,m);z+=mass*g
            b.append(z.rational())
        S1.append(b)
    for y in range(n):
        assert sum(S[y])==1
        assert sum(M[y])==0
        assert sum(S1[y])==F(1,L)
        if y%L==0:
            assert S[y]==[F(j==y//L) for j in range(m)]
            assert M[y]==[0]*n
        for x in range(n):
            assert M[y][(x-1)%n]-M[y][x]==F(x==y)-(S[y][x//L] if x%L==0 else 0)
            assert M[(y+1)%n][x]-M[y][x]==F(y==x)-S1[y][x//L]
        for j in range(m):
            assert S[(y+1)%n][j]-S[y][j]==S1[y][(j-1)%m]-S1[y][j]
    merged=[]
    for y in range(n):
        merged.append(sum(S[y][j]*((y-L*j+n//2)%n-n//2) for j in range(m)))
    if m in (3,5,9): assert any(merged)
    return {'L':L,'coarse_count':m,'fine_count':n,'all_exact_identities':True,'merged_harmonic_at_1':str(merged[1])}


def segments(z,order,nu,L):
    """Whole segments (start,end,direction); no per-edge contour implementation."""
    p=(0,)*len(z);go=[]
    for i in order:
        q=list(p);q[i]=z[i];q=tuple(q)
        if q!=p:go.append((p,q,i))
        p=q
    end=list(z);end[nu]+=L;end=tuple(end)
    shift=lambda v:tuple(v[i]+L*(i==nu) for i in range(len(z)))
    return go+[(z,end,nu)]+[(shift(q),shift(p),i) for p,q,i in reversed(go)]

def segment_moments(ss,d):
    zero=[F(0)]*d;first=[[F(0)]*d for _ in range(d)]
    for p,q,i in ss:
        length=q[i]-p[i];zero[i]+=length
        # Exact midpoint edge sum equals line integral of every affine coordinate.
        for j in range(d): first[i][j]+=F(length*(p[j]+q[j]),2)
    return zero,first

def moments(d,L):
    orders=list(permutations(range(d))); offset=range(-(L-1)//2,(L-1)//2+1)
    checks=0
    for nu in range(d):
        expected0=[F(L*(i==nu)) for i in range(d)]
        expected1=[[F(L*L*(i==nu)*(j==nu),2) for j in range(d)] for i in range(d)]
        # Each order separately has the required centered average.
        for order in orders:
            zz=[F(0)]*d;ff=[[F(0)]*d for _ in range(d)]
            for z in product(offset,repeat=d):
                z0,z1=segment_moments(segments(z,order,nu,L),d)
                # Stronger per-contour formula, before centering.
                assert z0==expected0
                assert z1==[[F(-L*(j==nu)*z[i]+(i==nu)*(L*z[j]+F(L*L*(j==nu),2))) for j in range(d)] for i in range(d)]
                zz=[a+b for a,b in zip(zz,z0)]
                ff=[[a+b for a,b in zip(ar,br)] for ar,br in zip(ff,z1)]
            assert [a/L**d for a in zz]==expected0
            assert [[a/L**d for a in row] for row in ff]==expected1
            checks+=1
        transverse=(nu+1)%d
        # Lower-corner offsets have mean (L-1)/2, leaving -L mean(z_transverse).
        bad=sum(segment_moments(segments(z,orders[0],nu,L),d)[1][transverse][nu] for z in product(range(L),repeat=d))/L**d
        assert bad==-F(L*(L-1),2) and bad!=0
    return {'d':d,'L':L,'orders_times_output_directions':checks,'all_moments_exact':True,'uncentered_control_detected':True}


def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)
def bracket(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def periodic_ac1():
    # d=2 exact su(2)-isomorphic bracket data; side 3 forces wrapping.
    d,L,n=2,3,3;nu=0
    mu=lambda p:(F((p[0]%n)**2-(p[1]%n)),F((p[0]%n)*(p[1]%n)),F((p[1]%n)**2+2*(p[0]%n)))
    field=lambda p,i:(F(1+i+2*(p[0]%n)),F(3*(p[1]%n)-i),F(1+(p[0]%n)*(p[1]%n)+i))
    coarse=(F(7),F(-4),F(2)) # independent of B(field)
    end=(L,0);coarse_mu=scale(F(1,2),add(mu((0,0)),mu(end)))
    by=ba=cross_term=(F(0),)*3;count=factorial(d)*L**d
    wrap_count=0
    for z in product((-1,0,1),repeat=d):
        for order in permutations(range(d)):
            for p,q,i in segments(z,order,nu,L):
                sg=1 if q[i]>p[i] else -1
                for coordinate in range(min(p[i],q[i]),max(p[i],q[i])):
                    tail=list(p);tail[i]=coordinate;head=tail.copy();head[i]+=1
                    if any(c<0 or c>=n for c in tail+head):wrap_count+=1
                    y=field(tail,i);bar=scale(F(1,2),add(mu(tail),mu(head)))
                    by=add(by,scale(F(sg,count),y))
                    ba=add(ba,scale(F(-sg,count),bracket(y,bar)))
                    cross_term=add(cross_term,scale(F(-sg,count),bracket(y,add(bar,scale(-1,coarse_mu)))))
    lhs=add(ba,bracket(coarse,coarse_mu))
    rhs=add(scale(-1,bracket(add(by,scale(-1,coarse)),coarse_mu)),cross_term)
    assert lhs==rhs and wrap_count
    # Top gauge values vanish on roots, giving coarse_mu=0 here; a shifted lower-level
    # test changes the independent coarse term and checks its sign separately.
    shift=(F(2),F(-1),F(3));shifted=add(coarse_mu,shift)
    # Add constant gauge shift to all fine endpoints: ba -> ba-[By,shift].
    shifted_ba=add(ba,scale(-1,bracket(by,shift)))
    lhs2=add(shifted_ba,bracket(coarse,shifted))
    rhs2=add(scale(-1,bracket(add(by,scale(-1,coarse)),shifted)),cross_term)
    bad=add(scale(-1,bracket(add(by,coarse),shifted)),cross_term)
    assert lhs2==rhs2 and lhs2!=bad
    return {'wrapping_oriented_steps':wrap_count,'top_root_zero_identity':list(map(str,lhs)),'independent_coarse_background_identity':list(map(str,lhs2)),'wrong_coarse_sign_detected':True}


def scale_bookkeeping():
    # Exponents below denote powers of L; no floating arithmetic or tuned constant.
    count=0
    for k in range(1,21):
        for l in range(k):
            for m in range(l,k):
                h_l=-(k-l);h_m=-(k-m);H=-(k-1-m)
                propagated=4*(m-l)+3*h_l
                assert propagated==3*h_m
                # s_m=w_(m+1), own->coarse and R weights.
                direct=3*(m+1-l)+3*h_l+2*(k-1-m)+F(1,2)*(k-m)
                expected=F(1,2)+(1-F(1,2))*H
                assert direct==expected
                for alpha,theta in ((F(1,4),F(1,2)),(F(1,3),F(2,3)),(F(3,4),F(7,8))):
                    curvature=propagated-2*h_m-alpha*h_m-theta*h_m
                    assert curvature==(1-alpha-theta)*h_m
                    if m==0:
                        unweighted=propagated-(2+alpha)*h_m
                        assert unweighted==(1-alpha)*h_m
                    count+=1
    L=81;theta=F(1,2);alpha=F(1,4)
    for k in range(1,21):
        weights=[F(1,9**(k-l)) for l in range(1,k)]
        assert sum(weights,F(0))<=F(1,8) # 1/(L^theta-1)
        for m in range(1,k):
            assert sum(weights[:m],F(0))<=F(9,8)*F(1,9**(k-m))
        nres=sum((F(1,3**q) for q in range(1,k)),F(0))
        assert nres<=F(1,2) # 1/(L^(theta-alpha)-1)
    assert sum(F(1) for q in range(1,20))==19 # equality has no geometric bound
    # Residual-chart correction: s=L^-theta H^(2+theta), delta=H eta.
    # At fine level h=H/L, its Pc price is L^(3+theta)*L^-theta=L^3.
    assert (3+theta)-theta==3
    # At coarse level the price is L^-theta.
    assert (3+theta)-(3+theta)==0
    # Phi-G: G own h^2, Phi h^2 eta^2, current currency h^-3 -> h^1.
    assert 2+2-3==1
    return {'independent_exponent_identities':count,'finite_geometric_sums_checked_through_k':20,'boundary_alpha_plus_theta_one':True,'theta_equal_alpha_control_sum_at_k20':19,'lower_residual_chart_L_exponent':3,'Phi_G_h_exponent':1}


print(scale_bookkeeping())
