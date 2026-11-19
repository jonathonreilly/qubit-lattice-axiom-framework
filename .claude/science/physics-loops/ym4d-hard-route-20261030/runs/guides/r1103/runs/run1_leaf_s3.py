# Run 1: exhaustive test of the leaf lemma C2 and the periodic factor C2' on S_3.
import itertools, math, random
G = list(itertools.permutations(range(3)))
idx = {g:i for i,g in enumerate(G)}
def mul(a,b): return tuple(a[b[i]] for i in range(3))
def inv(a):
    r=[0]*3
    for i,x in enumerate(a): r[x]=i
    return tuple(r)
def fixed(g): return sum(1 for i in range(3) if g[i]==i)
def sign(g):
    s=1
    for i in range(3):
        for j in range(i+1,3):
            if g[i]>g[j]: s=-s
    return s
chi = {'triv': lambda g:1, 'sign': sign, 'std': lambda g: fixed(g)-1}
dim = {'triv':1,'sign':1,'std':2}
def f(beta): return {g: math.exp(beta*chi['std'](g)/2) for g in G}
f0, f1 = f(0.9), f(1.7)
def c(fw, j):
    m = sum(fw.values())/6
    return sum(fw[g]*chi[j](g) for g in G)/6/m/dim[j]
random.seed(1103)
Psi = {t: 0.2+random.random() for t in itertools.product(G, repeat=4)}  # (a0,a1,b0,b1)
# --- free ladder, two rungs
marg = {t:0.0 for t in Psi}
joint = {}
for (a0,a1,b0,b1),psi in Psi.items():
    ib0, ib1 = inv(b0), inv(b1)
    for M0 in G:
        for M1 in G:
            P0 = mul(mul(mul(M0,a0),inv(M1)),ib0)
            w0 = f0[P0]
            for M2 in G:
                P1 = mul(mul(mul(M1,a1),inv(M2)),ib1)
                w = psi*w0*f1[P1]
                marg[(a0,a1,b0,b1)] += w
                k=(P0,P1,a0,a1,b0,b1)
                joint[k]=joint.get(k,0.0)+w
Z = sum(marg.values()); sPsi = sum(Psi.values())
dev_marg = max(abs(marg[t]/Z - Psi[t]/sPsi) for t in Psi)
s0, s1 = sum(f0.values()), sum(f1.values())
dev_joint = 0.0
for (P0,P1,a0,a1,b0,b1),w in joint.items():
    pred = f0[P0]*f1[P1]*Psi[(a0,a1,b0,b1)]/(s0*s1*sPsi)
    dev_joint = max(dev_joint, abs(w/Z - pred))
missing = 36*len(Psi) - len(joint)
print('free ladder: max dev marginal = %.3e ; max dev joint = %.3e ; (P0,P1,a,b) cells not hit = %d' % (dev_marg, dev_joint, missing))
# --- periodic ladder, L = 2 (M2 = M0)
m0, m1 = s0/6, s1/6
dev_per = 0.0
for (a0,a1,b0,b1) in Psi:
    ib0, ib1 = inv(b0), inv(b1)
    tot = 0.0
    for M0 in G:
        for M1 in G:
            P0 = mul(mul(mul(M0,a0),inv(M1)),ib0)
            P1 = mul(mul(mul(M1,a1),inv(M0)),ib1)
            tot += f0[P0]*f1[P1]
    lhs = tot/36/(m0*m1)
    A = mul(a0,a1); Binv = inv(mul(b0,b1))
    rhs = sum(c(f0,j)*c(f1,j)*chi[j](A)*chi[j](Binv) for j in chi)
    dev_per = max(dev_per, abs(lhs-rhs))
print('periodic ladder: max dev of the factor = %.3e' % dev_per)
print('c_j(f_0.9) =', {j: round(c(f0,j),6) for j in chi}, ' c_j(f_1.7) =', {j: round(c(f1,j),6) for j in chi})
