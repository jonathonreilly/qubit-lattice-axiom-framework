"""Independent re-derivation of T33 Tests A and C numbers (own RGE code, written from scratch, Claude Sonnet 5.5).
Uses alpha_i^-1 variables, 1-loop analytic + 2-loop by simple RK4 in t=ln mu; no scipy."""
import math
PI=math.pi
MZ=91.1876; MPL=1.2209e19; V=246.28
aem_inv=127.951; s2=0.23122; as_=0.1179; yt0=0.98
# GUT-normalised: alpha1 = 5/3 alpha_Y
b=[41/10,-19/6,-7.0]
B=[[199/50,27/10,44/5],[9/10,35/6,12],[11/10,9/2,-26]]
D=[17/10,3/2,2]
def beta(a,yt):
    # a = [a1,a2,a3] alphas ; d alpha_i/dt = alpha_i^2/(2pi) * (b_i + (1/(4pi)) sum_j B_ij alpha_j - D_i yt^2/(16 pi^2)*... )
    # From dg/dt = g^3/(16pi^2) (b + (1/16pi^2)(sum B g_j^2 - D yt^2)); alpha=g^2/4pi, g_j^2=4 pi alpha_j
    out=[]
    for i in range(3):
        two=(sum(B[i][j]*4*PI*a[j] for j in range(3)) - D[i]*yt**2)/(16*PI**2)
        out.append(a[i]**2/(2*PI)*(b[i]+two))
    return out
def dyt(a,yt):
    g2=[4*PI*x for x in a]
    return yt/(16*PI**2)*(4.5*yt**2-17/20*g2[0]-9/4*g2[1]-8*g2[2])
def rk4(y,t0,t1,n=4000):
    h=(t1-t0)/n
    def f(y):
        a=y[:3]; yt=y[3]
        return beta(a,yt)+[dyt(a,yt)]
    for _ in range(n):
        k1=f(y)
        k2=f([y[i]+h/2*k1[i] for i in range(4)])
        k3=f([y[i]+h/2*k2[i] for i in range(4)])
        k4=f([y[i]+h*k3[i] for i in range(4)])
        y=[y[i]+h/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]) for i in range(4)]
    return y
# inputs at MZ
aem=1/aem_inv
a2=aem/s2
aY=aem/(1-s2)
a1=5/3*aY
y0=[a1,a2,as_,yt0]
up=rk4(y0,math.log(MZ),math.log(MPL))
a1,a2,a3,yt=up
aY=3/5*a1
print("M_Pl alphas (GUT norm a1): 1/a1=%.3f 1/a2=%.3f 1/a3=%.3f  yt=%.3f"%(1/a1,1/a2,1/a3,yt))
g2s={'g3^2':4*PI*a3,'g2^2':4*PI*a2,'gY^2 (SM norm)':4*PI*aY,'g1^2 (GUT norm)':4*PI*a1}
print({k:round(v,4) for k,v in g2s.items()})
def spread(v):
    m=sum(v)/len(v); return (max(v)-min(v))/m
print("spread SM-norm  (g3,g2,gY): %.3f"%spread([g2s['g3^2'],g2s['g2^2'],g2s['gY^2 (SM norm)']]))
print("spread GUT-norm (g3,g2,g1): %.3f"%spread([g2s['g3^2'],g2s['g2^2'],g2s['g1^2 (GUT norm)']]))
# spread vs scale, both normalisations
print("\nscale GeV   spread(SM norm)  spread(GUT norm)")
for lg in (3,4,6,8,10,12,14,15,16,17,18,19,19.087):
    mu=10**lg
    y=rk4(y0,math.log(MZ),math.log(mu),2000)
    s_sm=spread([4*PI*y[2],4*PI*y[1],4*PI*3/5*y[0]]); s_gut=spread([4*PI*y[2],4*PI*y[1],4*PI*y[0]])
    print("1e%-6.2f  %.3f  %.3f"%(lg,s_sm,s_gut))
# Test C by own code: run down from M_Pl with pair (g2^2,gY^2) and g3,yt from upward run
def down(g22,gY2):
    a=[5/3*gY2/(4*PI), g22/(4*PI), a3, yt]
    r=rk4(a,math.log(MPL),math.log(MZ))
    a1_,a2_=r[0],r[1]
    aY_=3/5*a1_
    e2inv=1/a2_+1/aY_    # 1/alpha_em = 1/a2+1/aY
    return aY_/(aY_+a2_) if False else (1/aY_)**-1/( (1/aY_)**-1+(1/a2_)**-1) , e2inv
for name,(g22,gY2) in {'counting (1/4,1/5)':(.25,.2),'PS (1/4,3/14)':(.25,3/14),'universal 1/4':(.25,.25),
                       'PS with g4^2=SM g3^2':(0.25,1/(4+(2/3)/(4*PI*a3))),'data pair at MPl':(4*PI*a2,4*PI*aY)}.items():
    s,ai=down(g22,gY2)
    print("%-28s gY^2=%.4f  sin2=%.4f (%+.1f%%)  1/aem=%.2f (%+.1f%%)"%(name,gY2,s,(s/s2-1)*100,ai,(ai/aem_inv-1)*100))
