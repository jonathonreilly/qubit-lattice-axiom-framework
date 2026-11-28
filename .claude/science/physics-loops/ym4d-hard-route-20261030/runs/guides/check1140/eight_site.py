# Guide only (no proof): the eight-site graph of S9, reduced to the two bridge endpoints.
# f(u) is proportional to K^4(u, Hu) = sum_n d_n^4/(n+1)^3 U_n(u.Hu), d_n = 2(n+1) I_{n+1}(b)/b,
# u.Hu = cos(2 alpha) in Hopf coordinates. Then
# Z_f(t)  ~ int int w w f f I0(t ca cb) I0(t sa sb),
# Z_f'(t) ~ int int w w f f [ca cb I1(t ca cb) I0(t sa sb) + sa sb I0(t ca cb) I1(t sa sb)], w = sin cos.
import math, sys
def besselI(nu, x, terms=80):
    s=0.0; t=(x/2)**nu/math.gamma(nu+1)
    for m in range(terms):
        s+=t
        t*= (x/2)**2/((m+1)*(m+1+nu))
        if t < 1e-18*abs(s): break
    return s
def gauss_legendre(n):
    xs=[];ws=[]
    for i in range(1,n+1):
        x=math.cos(math.pi*(i-0.25)/(n+0.5))
        for _ in range(100):
            p0,p1=1.0,x
            for k in range(2,n+1):
                p0,p1=p1,((2*k-1)*x*p1-(k-1)*p0)/k
            dp=n*(x*p1-p0)/(x*x-1)
            dx=p1/dp; x-=dx
            if abs(dx)<1e-15: break
        xs.append(x); ws.append(2/((1-x*x)*dp*dp))
    return xs,ws
NQ=int(sys.argv[1]) if len(sys.argv)>1 else 48
xs,ws=gauss_legendre(NQ)
al=[(x+1)*math.pi/4 for x in xs]; wa=[w*math.pi/4 for w in ws]   # alpha in [0, pi/2]
def fvals(b, N=None):
    if N is None: N=int(3*b)+40
    d=[2*(n+1)*besselI(n+1,b)/b for n in range(N+1)]
    c=[d[n]**4/(n+1)**3 for n in range(N+1)]
    out=[]
    for a in al:
        z=math.cos(2*a); U0,U1=1.0,2*z; s=c[0]*U0+c[1]*U1
        for n in range(2,N+1):
            U0,U1=U1,2*z*U1-U0; s+=c[n]*U1
        out.append(s)
    return out
def expect(f, t):
    Z=0.0; Zp=0.0
    for i,a in enumerate(al):
        ca,sa=math.cos(a),math.sin(a)
        for j,bb in enumerate(al):
            cb,sb=math.cos(bb),math.sin(bb)
            w=wa[i]*wa[j]*sa*ca*sb*cb*f[i]*f[j]
            A=t*ca*cb; B=t*sa*sb
            i0A,i0B=besselI(0,A),besselI(0,B)
            Z+=w*i0A*i0B
            Zp+=w*(ca*cb*besselI(1,A)*i0B+sa*sb*i0A*besselI(1,B))
    return Zp/Z
def sqrt_dummy(): pass
bs=[0.25,0.5,1.0,1.5,2.0,2.3,2.45,2.6,math.sqrt(8),3.5,5.0,8.0]
print("NQ",NQ)
print(" b        E_I(quad)       I2/I1         E_R           E_R-E_I        b/4     f(1)/f(j)")
for b in bs:
    f=fvals(b); one=[1.0]*len(al)
    EI=expect(one,b); C0=besselI(2,b)/besselI(1,b); ER=expect(f,b)
    # ratio of root weights at u=1 (u.Hu=1) and u=j (u.Hu=-1)
    N=int(3*b)+40; d=[2*(n+1)*besselI(n+1,b)/b for n in range(N+1)]
    k4p=sum(d[n]**4/(n+1)**3*(n+1) for n in range(N+1)); k4m=sum(d[n]**4/(n+1)**3*(n+1)*(-1)**n for n in range(N+1))
    print("%6.4f  %.12f  %.12f  %.12f  %+.3e  %.4f  %.6g"%(b,EI,C0,ER,ER-EI,b/4,k4p/k4m))
