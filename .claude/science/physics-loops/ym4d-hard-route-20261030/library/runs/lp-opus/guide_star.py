# GUIDE only. One link e with six i.i.d. Haar staples; conditional law of U_e
# proportional to exp(s h). Theorem P needs only this conditional law, so its
# bounds must hold here. Computes h, u, v by importance weights.
import random, math
random.seed(7)
def haar():
    x=[random.gauss(0,1) for _ in range(4)]; n=math.sqrt(sum(t*t for t in x)); return [t/n for t in x]
def qmul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return [a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0]
S=200000
samp=[]
for _ in range(S):
    H=[0.0]*4
    for i in range(6):
        b=haar(); H=[H[k]+b[k] for k in range(4)]
    U=haar()
    # h = Re(U H) = (1/2) tr(U H)
    h=qmul(U,H)[0]; u=sum(t*t for t in H); samp.append((h,u))
def U_s(s,M): return min(6,10*s*M/(20+math.sqrt(400+60*s*s*M)))
def L_s(s,M,N): return max(0,s*M/(4+6*s),s*M/(4+6*s*s),s*M/4-s**3*N/96)
for s in [0.0,0.05,0.3,1.0,2.0,4.0]:
    W=[math.exp(s*h) for h,u in samp]; Z=sum(W)
    E=lambda f: sum(w*f(h,u) for w,(h,u) in zip(W,samp))/Z
    m=E(lambda h,u:h); M=E(lambda h,u:u); N=E(lambda h,u:u*u)
    A1=E(lambda h,u:u-h*h); A2=E(lambda h,u:(u-h*h)**2); V=A2-A1*A1
    ward1=3*m-s*A1
    pred=s**3*V/(3*(20+3*s*(U_s(s,M)+m))) if U_s(s,M)<6 else float('nan')
    print(f"s={s:4.2f} L={L_s(s,M,N):.4f} m={m:.4f} U={U_s(s,M):.4f} M={M:.3f} N={N:.2f} A1={A1:.3f} VarV={V:.3f} ward1_resid={ward1:+.4f} U-m={U_s(s,M)-m:.5f} pred={pred:.5f}")
