# nr55_2.py -- exact non-convexity witness for the SU(2) Wilson action at a uniform-field background on a 2D patch.
# Criteria: checks/nr55_2_criteria.md (written first). Verdicts: Fractions only. Floats only to SEARCH for a direction.
import sys, math
from fractions import Fraction as Fr

def cadd(a, b): return (a[0]+b[0], a[1]+b[1])
def csub(a, b): return (a[0]-b[0], a[1]-b[1])
def cmul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def cscale(s, a): return (s*a[0], s*a[1])
def cconj(a): return (a[0], -a[1])
Z = (Fr(0), Fr(0)); O = (Fr(1), Fr(0)); I_ = (Fr(0), Fr(1))
def madd(A, B): return tuple(cadd(A[k], B[k]) for k in range(4))
def mmul(A, B):
    return (cadd(cmul(A[0], B[0]), cmul(A[1], B[2])), cadd(cmul(A[0], B[1]), cmul(A[1], B[3])),
            cadd(cmul(A[2], B[0]), cmul(A[3], B[2])), cadd(cmul(A[2], B[1]), cmul(A[3], B[3])))
def mscale(s, A): return tuple(cscale(s, A[k]) for k in range(4))
ID = (O, Z, Z, O); ZM = (Z, Z, Z, Z)
S1 = (Z, O, O, Z); S2 = (Z, (Fr(0), Fr(-1)), (Fr(0), Fr(1)), Z); S3 = (O, Z, Z, (Fr(-1), Fr(0)))
def imul(A): return tuple(cmul(I_, A[k]) for k in range(4))
GEN = [imul(S1), imul(S2), imul(S3)]   # i sigma_a
def Xof(a, b, c):
    return madd(madd(mscale(Fr(a), GEN[0]), mscale(Fr(b), GEN[1])), mscale(Fr(c), GEN[2]))
DEG = 2
def pexp(X, sign):
    return [ID, mscale(Fr(sign), X), mscale(Fr(1, 2), mmul(X, X))]
def pconst(M): return [M, ZM, ZM]
def pmul(P, Q):
    R = [ZM]*(DEG+1)
    for i in range(DEG+1):
        if P[i] == ZM: continue
        for j in range(DEG+1-i):
            if Q[j] == ZM: continue
            R[i+j] = madd(R[i+j], mmul(P[i], Q[j]))
    return R
def ptr(P): return [cadd(P[d][0], P[d][3]) for d in range(DEG+1)]

def cpow(z, n):
    r = O
    if n < 0:
        z = cconj(z); n = -n   # |z| = 1
    for _ in range(n): r = cmul(r, z)
    return r

def setup(N, tau):
    tau = Fr(tau)
    w = (Fr(1) - tau*tau, 2*tau); den = 1 + tau*tau
    w = (w[0]/den, w[1]/den)   # (1+i tau)/(1-i tau) = (1 - tau^2 + 2 i tau)/(1+tau^2)
    def onb(s): return s[0] in (0, N) or s[1] in (0, N)
    links = []
    for i in range(N):
        for j in range(N+1): links.append(((i, j), 1))
    for i in range(N+1):
        for j in range(N): links.append(((i, j), 2))
    def ends(l):
        (i, j), mu = l
        return ((i, j), (i+1, j)) if mu == 1 else ((i, j), (i, j+1))
    var = [l for l in links if not (onb(ends(l)[0]) and onb(ends(l)[1]))]
    idx = {l: k for k, l in enumerate(var)}
    def C(l):
        (i, j), mu = l
        if mu == 2: return ID
        return (cpow(w, -j), Z, Z, cpow(w, j))
    def Cinv(l):
        M = C(l); return (cconj(M[0]), Z, Z, cconj(M[3]))   # diagonal unitary
    plaqs = []
    for i in range(N):
        for j in range(N):
            plaqs.append([((i, j), 1), ((i+1, j), 2), ((i, j+1), 1), ((i, j), 2)])
    return dict(N=N, tau=tau, w=w, var=var, idx=idx, C=C, Cinv=Cinv, plaqs=plaqs)

def plaq_trace_poly(G, pl, Xmap):
    l1, l2, l3, l4 = pl
    def E(l, sign):
        X = Xmap.get(l)
        return pexp(X, sign) if X is not None else pconst(ID)
    P = pmul(E(l1, 1), pconst(G['C'](l1)))
    P = pmul(P, E(l2, 1)); P = pmul(P, pconst(G['C'](l2)))
    P = pmul(P, pconst(G['Cinv'](l3))); P = pmul(P, E(l3, -1))
    P = pmul(P, pconst(G['Cinv'](l4))); P = pmul(P, E(l4, -1))
    return ptr(P)

def vec_to_Xmap(G, v):
    Xm = {}
    for k, l in enumerate(G['var']):
        a, b, c = v[3*k], v[3*k+1], v[3*k+2]
        if a == 0 and b == 0 and c == 0: continue
        Xm[l] = Xof(a, b, c)
    return Xm

def Q_and_grad(G, v):
    Xm = vec_to_Xmap(G, v)
    q = Fr(0); g = Fr(0); imag = Fr(0)
    for pl in G['plaqs']:
        if not any(l in Xm for l in pl): continue
        t = plaq_trace_poly(G, pl, Xm)
        q += -t[2][0]; g += -Fr(1, 2)*t[1][0]; imag += abs(t[2][1]) + abs(t[1][1])
    return q, g, imag    # Q(v) = 2[eps^2]S = -[eps^2] sum tr ; G(v) = [eps^1]S

def assemble_H(G):
    n = 3*len(G['var'])
    H = [dict() for _ in range(n)]
    for pl in G['plaqs']:
        loc = []
        for l in pl:
            if l in G['idx']:
                k = G['idx'][l]; loc += [3*k, 3*k+1, 3*k+2]
        if not loc: continue
        def qloc(coefs):
            v = {}
            for a, cval in coefs: v[a] = v.get(a, 0) + cval
            Xm = {}
            for l in pl:
                if l in G['idx']:
                    k = G['idx'][l]
                    a, b, c = v.get(3*k, 0), v.get(3*k+1, 0), v.get(3*k+2, 0)
                    if a or b or c: Xm[l] = Xof(a, b, c)
            t = plaq_trace_poly(G, pl, Xm)
            return -t[2][0]
        diag = {a: qloc([(a, 1)]) for a in loc}
        for a in loc:
            H[a][a] = H[a].get(a, Fr(0)) + diag[a]
        for ii in range(len(loc)):
            for jj in range(ii+1, len(loc)):
                a, b = loc[ii], loc[jj]
                val = (qloc([(a, 1), (b, 1)]) - diag[a] - diag[b])/2
                if val != 0:
                    H[a][b] = H[a].get(b, Fr(0)) + val
                    H[b][a] = H[b].get(a, Fr(0)) + val
    return H

def quad_exact(H, v):
    s = Fr(0)
    for a, row in enumerate(H):
        if v[a] == 0: continue
        for b, hab in row.items():
            if v[b] != 0: s += v[a]*hab*v[b]
    return s

def lowest_vec_float(H, iters=4000, seed=1):
    n = len(H)
    Hf = [{b: float(x) for b, x in row.items()} for row in H]
    c = max(sum(abs(x) for x in row.values()) for row in Hf) + 1.0
    import random
    rnd = random.Random(seed)
    x = [rnd.uniform(-1, 1) for _ in range(n)]
    for it in range(iters):
        y = [c*x[a] - sum(hab*x[b] for b, hab in Hf[a].items()) for a in range(n)]
        nrm = math.sqrt(sum(t*t for t in y)); x = [t/nrm for t in y]
    rq = sum(x[a]*sum(hab*x[b] for b, hab in Hf[a].items()) for a in range(n))
    return x, rq

def rationalize(x, D=10**6):
    return [Fr(round(t*D), D) for t in x]

results = []
def gate(name, ok, detail):
    results.append((name, ok)); print(f"{name}: {'PASS' if ok else 'FAIL'} | {detail}"); sys.stdout.flush()

def run(N, tau, tag):
    G = setup(N, tau)
    n = 3*len(G['var'])
    print(f"--- run {tag}: N={N}, tau={tau}, variable links={len(G['var'])}, variables={n}")
    w = G['w']; one_minus_w = csub(O, w); nw2 = one_minus_w[0]**2 + one_minus_w[1]**2
    print(f"    plaquette |1-w|^2 = {nw2} (= 4tau^2/(1+tau^2)), operator norm ~ {math.sqrt(float(nw2)):.6f}")
    # G5a criticality
    bad = 0
    for a in range(n):
        e = [Fr(0)]*n; e[a] = Fr(1)
        _, g, im = Q_and_grad(G, e)
        if g != 0: bad += 1
    gate(f"G5a[{tag}] criticality", bad == 0, f"nonzero gradient components = {bad} of {n}")
    H = assemble_H(G)
    xf, rq = lowest_vec_float(H)
    print(f"    float search: lowest Rayleigh quotient ~ {rq:.6e}")
    v = rationalize(xf)
    qH = quad_exact(H, v)
    qD, gD, imD = Q_and_grad(G, v)
    nv = sum(t*t for t in v)
    gate(f"G5b[{tag}] non-convexity Q_C(v) < 0", (qH == qD) and qD < 0 and imD == 0,
         f"Q_C(v) exact = {float(qD):.6e} (two code paths agree: {qH == qD}); |v|^2 = {float(nv):.6f}; RQ = {float(qD/nv):.6e}")
    G0 = setup(N, 0)
    q0, g0, _ = Q_and_grad(G0, v)
    gate(f"G5c[{tag}] free Hessian positive on v", q0 > 0, f"Q_1(v) = {float(q0):.6e}; RQ_1 = {float(q0/nv):.6e}")
    w9 = cpow(w, 9); om9 = csub(O, w9); n9 = om9[0]**2 + om9[1]**2
    gate(f"G5d[{tag}] blocked 3x3 plaquette larger than fine one", n9 > nw2, f"|1-w^9|^2 = {float(n9):.6f} vs |1-w|^2 = {float(nw2):.6f}")
    # control G5n2: zero charged components
    vab = [v[a] if a % 3 == 2 else Fr(0) for a in range(n)]
    qab, _, _ = Q_and_grad(G, vab)
    gate(f"G5n2[{tag}] (control: abelian part must NOT be negative)", not (qab < 0), f"Q_C(v_abelian) = {float(qab):.6e}")
    return G

run(8, Fr(1, 4), "tau=1/4,N=8")
# control G5n at tau = 0
G0 = setup(8, 0)
H0 = assemble_H(G0)
x0, rq0 = lowest_vec_float(H0)
v0 = rationalize(x0)
q00 = quad_exact(H0, v0)
gate("G5n (control tau=0: Q_1(v0) < 0 must FAIL)", not (q00 < 0), f"Q_1(v0) = {float(q00):.6e}, float RQ ~ {rq0:.3e}")
if len(sys.argv) > 1 and sys.argv[1] == "second":
    run(12, Fr(1, 8), "tau=1/8,N=12")
print("SUMMARY:", sum(1 for _, o in results if o), "/", len(results), "gates PASS (controls PASS = fired as designed)")
