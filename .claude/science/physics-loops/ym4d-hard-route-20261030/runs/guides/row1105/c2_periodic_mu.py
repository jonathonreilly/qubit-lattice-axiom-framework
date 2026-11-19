# Guide run for C2 (leaf lemma) with direction mu PERIODIC (length Lm) and nu FREE (levels 0..Ln).
# Group S_3. Measure: Psi(nu-links) * prod_p f_p(U_p), Psi random positive, f_p different weights.
# Check: joint law of (plaquettes, nu-links) equals prod_p f_p(P_p) * Psi(nu)/sum(Psi) exactly.
import itertools, math, random, sys
G = list(itertools.permutations(range(3)))
def mul(a,b): return tuple(a[b[i]] for i in range(3))
def inv(a):
    r=[0]*3
    for i,x in enumerate(a): r[x]=i
    return tuple(r)
def chi_std(g): return sum(1 for i in range(3) if g[i]==i)-1
def run(Lm, Ln, seed):
    rnd = random.Random(seed)
    # mu-links: (xm, k) for xm in Z_Lm, k in 0..Ln ; nu-links: (xm, k) for xm in Z_Lm, k in 0..Ln-1
    mul_links = [(xm,k) for xm in range(Lm) for k in range(Ln+1)]
    nu_links  = [(xm,k) for xm in range(Lm) for k in range(Ln)]
    plaqs = [(xm,k) for xm in range(Lm) for k in range(Ln)]   # plaquette with mu-edges (xm,k),(xm,k+1)
    # weights: different beta per plaquette, normalized
    fp = {}
    for p in plaqs:
        b = rnd.uniform(0.3, 2.0)
        w = {g: math.exp(b*chi_std(g)) for g in G}
        s = sum(w.values()); fp[p] = {g: w[g]*6/s for g in G}   # density wrt normalized Haar (counting/6)
    Psi = {cfg: 0.1+rnd.random() for cfg in itertools.product(G, repeat=len(nu_links))}
    sPsi = sum(Psi.values())
    joint = {}
    Z = 0.0
    for numap in itertools.product(G, repeat=len(nu_links)):
        nu = dict(zip(nu_links, numap)); ps = Psi[numap]
        for mumap in itertools.product(G, repeat=len(mul_links)):
            M = dict(zip(mul_links, mumap))
            w = ps; P = []
            for (xm,k) in plaqs:
                a = nu[((xm+1)%Lm, k)]; b = nu[(xm, k)]
                Pk = mul(mul(mul(M[(xm,k)], a), inv(M[(xm,k+1)])), inv(b))
                P.append(Pk); w *= fp[(xm,k)][Pk]
            key = (tuple(P), numap)
            joint[key] = joint.get(key, 0.0) + w
            Z += w
    nP = len(plaqs)
    dev = 0.0; cells = 0
    for Pt in itertools.product(G, repeat=nP):
        for numap in Psi:
            pred = Psi[numap]/sPsi
            for i,p in enumerate(plaqs): pred *= fp[p][Pt[i]]/6
            got = joint.get((Pt, numap), 0.0)/Z
            dev = max(dev, abs(got-pred)); cells += 1
    return dev, cells, len(mul_links)+len(nu_links)
for (Lm, Ln) in [(1,1),(1,2),(2,1),(3,1)]:
    if 6**((Lm*(Ln+1))+Lm*Ln) > 2*10**6: 
        print('skip', Lm, Ln); continue
    dev, cells, nl = run(Lm, Ln, 1105+10*Lm+Ln)
    print('Lmu=%d (periodic) Lnu=%d (free): links=%d, cells=%d, max |joint - product| = %.3e' % (Lm, Ln, nl, cells, dev))
