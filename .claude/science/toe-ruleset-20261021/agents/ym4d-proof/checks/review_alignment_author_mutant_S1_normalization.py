from fractions import Fraction as F
from itertools import product, permutations
from collections import defaultdict


def inverse(a):
    n=len(a); a=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j]); a[j],a[p]=a[p],a[j]
        t=a[j][j]; a[j]=[x/t for x in a[j]]
        for i in range(n):
            if i!=j:
                t=a[i][j]; a[i]=[x-t*y for x,y in zip(a[i],a[j])]
    return [r[n:] for r in a]

def b3(t):
    t=abs(t)
    return (4-6*t*t+3*t*t*t)/6 if t<1 else ((2-t)**3/6 if t<2 else F(0))

def spline_check(m,L=3):
    n=L*m
    coll=[[F(4*(i==j)+(i==(j+1)%m)+(i==(j-1)%m),6) for j in range(m)] for i in range(m)]
    inv=inverse(coll)
    s=[]
    for y in range(n):
        bv=[sum((b3(F(y,L)-j+m*w) for w in range(-2,3)),F(0)) for j in range(m)]
        s.append([sum((bv[t]*inv[t][j] for t in range(m)),F(0)) for j in range(m)])
    merged=[]
    for y in range(n):
        row=[F(0)]*n
        for j in range(m):
            start=L*j; disp=(y-start+n//2)%n-n//2
            step=1 if disp>=0 else -1
            for t in range(abs(disp)):
                edge=(start+t if step>0 else start-t-1)%n
                row[edge]+=step*s[y][j]
        merged.append(row)
    img=[[z-sum(row)/n for z in row] for row in merged]
    s1=[]
    for y in range(n):
        q=[s[(y+1)%n][j]-s[y][j] for j in range(m)]
        r=[F(0)]
        for j in range(1,m):r.append(r[-1]-q[j])
        shift=(F(1)-sum(r))/m; r=[z+shift for z in r]
        assert all(r[(j-1)%m]-r[j]==q[j] for j in range(m))
        s1.append(r)
    assert all(sum(row)==0 for row in img)
    for y in range(n):
        for x in range(n):
            md=img[y][(x-1)%n]-img[y][x]
            target=F(y==x)-(s[y][x//L] if x%L==0 else 0)
            assert md==target
            e=img[(y+1)%n][x]-img[y][x]-F(y==x)+s1[y][x//L]
            assert e==0
    failed_h=any(sum(row)!=0 for row in merged)
    failed_e=any(merged[(y+1)%n][x]-merged[y][x]-F(y==x)+s1[y][x//L]!=0 for y in range(n) for x in range(n))
    assert failed_h and failed_e
    print(f'P m={m}: Md, harmonic, completion PASS; merged controls FIRE; Mmerged(1)[1]={sum(merged[1])}')


def path_to(z,order):
    p=[0]*len(z); steps=[]
    for a in order:
        direction=1 if z[a]>=0 else -1
        for _ in range(abs(z[a])):
            steps.append((tuple(p),a,direction)); p[a]+=direction
    return steps

def contour(z,order,nu,L):
    d=len(z); p=path_to(z,order); out=list(p); t=list(z)
    for _ in range(L):out.append((tuple(t),nu,1)); t[nu]+=1
    for v,a,sgn in reversed(p):
        start=list(v); start[a]+=sgn; start[nu]+=L
        out.append((tuple(start),a,-sgn))
    return out

def positive_edge(v,a,sgn):
    v=list(v)
    if sgn<0:v[a]-=1
    return tuple(v)

def contour_kernel(d,L,nu,center=True):
    o=(L-1)//2; offs=range(-o,o+1) if center else range(L)
    kernel=defaultdict(int); total=0
    zm=[0]*d; mm=[[0]*d for _ in range(d)]; area=[[0]*d for _ in range(d)]
    for z in product(offs,repeat=d):
        for order in permutations(range(d)):
            total+=1; prefix=[0]*d
            for v,a,sgn in contour(z,order,nu,L):
                base=positive_edge(v,a,sgn); kernel[(base,a)]+=sgn; zm[a]+=sgn
                for j in range(d):
                    mm[a][j]+=sgn*(2*base[j]+(a==j))
                    area[j][a]+=prefix[j]*sgn
                    area[a][j]-=prefix[j]*sgn
                prefix[a]+=sgn
            assert prefix==[L*(j==nu) for j in range(d)]
    kernel={b:F(w,total) for b,w in kernel.items() if w}
    return kernel,[F(z,total) for z in zm],[[F(z,total) for z in r] for r in mm],[[F(z,total) for z in r] for r in area]

def moments():
    saved=None
    for L in (3,5):
        for nu in range(4):
            ker,z,m,a=contour_kernel(4,L,nu)
            assert z==[L*(j==nu) for j in range(4)]
            assert m==[[L*L*(i==nu)*(j==nu) for j in range(4)] for i in range(4)]
            assert all(v==0 for row in a for v in row)
            if L==3 and nu==0:saved=ker
        print(f'C d=4 L={L}: all four directions zeroth/midpoint moments and BCH2 areas PASS')
    bad,z,m,a=contour_kernel(4,3,0,False)
    assert any(v for row in a for v in row)
    assert m!=[[9*(i==0)*(j==0) for j in range(4)] for i in range(4)]
    z=(0,1,0,0); order=(0,1,2,3); ar=0; prefix=[0]*4
    for v,a,sgn in contour(z,order,0,3):
        ar+=prefix[1]*sgn*(a==0)-prefix[0]*sgn*(a==1);prefix[a]+=sgn
    assert ar!=0
    print('C controls: lower-corner and single transverse contour FIRE')
    return saved,bad


def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def times(c,a):return tuple(c*x for x in a)
def mu(v,h):return (1+h*(v[0]+2*v[2]),-2+h*(v[1]-v[3]),3+h*(v[0]+v[1]))
def y(v,a,h,affine):
    base=((a+1),(-1)**a,a-2)
    slope=(v[(a+1)%4],v[a]+v[3],2*v[2]-v[0]) if affine else (0,0,0)
    return plus(times(h,base),times(h*h,slope))
def comm_res(ker,h,affine):
    by=(F(0),)*3; bp=(F(0),)*3
    for (v,a),w in ker.items():
        vp=list(v);vp[a]+=1
        av=times(F(1,2),plus(mu(v,h),mu(vp,h)))
        yy=y(v,a,h,affine);by=plus(by,times(w,yy));bp=plus(bp,times(-w,cross(yy,av)))
    avtop=times(F(1,2),plus(mu((0,0,0,0),h),mu((3,0,0,0),h)))
    return plus(bp,cross(by,avtop))

def ac_checks(ker,bad):
    vals=[comm_res(ker,F(1,3**q),True) for q in (1,2,3)]
    assert vals[0]!=(0,0,0)
    assert vals[1]==times(F(1,27),vals[0]) and vals[2]==times(F(1,27),vals[1])
    assert all(comm_res(ker,F(1,3**q),False)==(0,0,0) for q in (1,2,3))
    control=[comm_res(bad,F(1,3**q),False) for q in (1,2)]
    assert control[0]!=(0,0,0) and control[1]==times(F(1,9),control[0])
    print('A centered commutator: constant/affine cancellation PASS; affine/affine cubic scaling PASS; first residual='+str(vals[0]))
    print('A uncentered quadratic control FIRE; first residual='+str(control[0]))

for m in (3,5,9):spline_check(m)
ker,bad=moments();ac_checks(ker,bad)
a,t=F(1,4),F(1,2)
assert all((a+t-1)*depth<=0 for depth in range(1,41))
a,t=F(3,4),F(7,8)
assert all((a+t-1)*depth>0 for depth in range(1,41))
print('W G0 exponent: lane alpha=1/4 theta=1/2 PASS; outside-window upper-bound growth control FIRE (not a theorem counterexample)')
print('OVERALL PASS: exact finite identities and controls only; uniform/analytic statements require note proofs')
