"""Probe F1 (scale ladder, formation lane).
Supplied model only: six Bloch-axis labels (+x,-x,+y,-y,+z,-z), covariant
product rule r(s|eta) ~ prod_y phi(s, eta_y), phi = p (parallel), q (antiparallel),
r (orthogonal).  Compare on an L^3 torus:
  (a) FORMATION reading with iid priorities (uniform random order = iid Exp clocks);
  (b) STATIC reading: Gibbs measure with the same full conditionals (heat bath,
      checkerboard), started from ordered and from random configurations.
Observables: magnetisation |<v>|, connected correlation C(d) along an axis,
block susceptibility chi_b = Var(sum_block v)/b^3 (block-spin RG diagnostic),
and the longest decreasing-ancestor path (coding depth) under formation.
"""
import numpy as np, sys, time, json
rng = np.random.default_rng(20261018)
VEC = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], float)

def phi_matrix(p, q, r):
    P = np.full((6,6), float(r))
    for a in range(3):
        P[2*a,2*a] = P[2*a+1,2*a+1] = p
        P[2*a,2*a+1] = P[2*a+1,2*a] = q
    return np.log(P)

def nbrs(L):
    idx = np.arange(L**3).reshape(L,L,L)
    out = []
    for ax in range(3):
        for sh in (1,-1):
            out.append(np.roll(idx, sh, axis=ax).ravel())
    return np.stack(out, 1)  # (N,6)

def formation_sample(L, logP, NB):
    N = L**3
    order = rng.permutation(N)
    lw = np.zeros((N,6)); lab = -np.ones(N, int); depth = np.zeros(N, int)
    u = rng.random(N)
    for x in order:
        w = np.exp(lw[x] - lw[x].max()); c = np.cumsum(w); s = int(np.searchsorted(c, u[x]*c[-1]))
        lab[x] = s
        nb = NB[x]
        formed = lab[nb] >= 0
        depth[x] = 1 + (depth[nb[formed]].max() if formed.any() else 0) - 1 if formed.any() else 0
        if formed.any(): depth[x] = 1 + depth[nb[formed]].max()
        lw[nb[~formed]] += logP[:, s]
    return lab, depth

def static_sample(L, logP, NB, sweeps, init):
    N = L**3
    lab = init.copy()
    co = np.indices((L,L,L)).sum(0).ravel() % 2
    subs = [np.where(co==0)[0], np.where(co==1)[0]]
    for _ in range(sweeps):
        for S in subs:
            lw = logP[:, lab[NB[S]]].sum(axis=2).T if False else sum(logP[lab[NB[S][:,k]]] for k in range(6))
            # logP symmetric so logP[t,:] == logP[:,t]
            lw -= lw.max(1, keepdims=True); w = np.exp(lw); c = np.cumsum(w,1)
            u = rng.random(len(S))[:,None]*c[:,-1:]
            lab[S] = (c < u).sum(1)
    return lab

def observables(lab, L):
    v = VEC[lab].reshape(L,L,L,3)
    m = np.linalg.norm(v.mean((0,1,2)))
    C = []
    for d in range(L//2+1):
        C.append(np.mean([(v*np.roll(v,d,axis=ax)).sum(-1).mean() for ax in range(3)]))
    chi = {}
    for b in (1,2,4,8):
        if L % b: continue
        B = v.reshape(L//b,b,L//b,b,L//b,b,3).sum((1,3,5))
        chi[b] = float(((B**2).sum(-1)).mean()/b**3)
    return m, np.array(C), chi

def run(name, pqr, L=16, nform=60, nstat=30, sweeps=300):
    logP = phi_matrix(*pqr); NB = nbrs(L)
    res = {}
    t = time.time()
    ms, Cs, chis, depths = [], [], [], []
    for i in range(nform):
        lab, dep = formation_sample(L, logP, NB)
        m, C, chi = observables(lab, L); ms.append(m); Cs.append(C); chis.append(chi); depths.append(dep.max())
    Cm = np.mean(Cs,0); mm2 = np.mean(np.array(ms)**2)
    res['formation'] = dict(m_rms=float(np.sqrt(mm2)), C=[round(float(c),5) for c in Cm],
        chi_b={b: round(float(np.mean([c[b] for c in chis])),4) for b in chis[0]},
        max_ancestor_depth_mean=float(np.mean(depths)), max_ancestor_depth_max=int(np.max(depths)), secs=round(time.time()-t,1))
    for init_name in ('ordered','random'):
        t = time.time(); ms, Cs, chis = [], [], []
        lab = np.zeros(L**3,int) if init_name=='ordered' else rng.integers(0,6,L**3)
        lab = static_sample(L, logP, NB, sweeps, lab)  # burn-in
        for i in range(nstat):
            lab = static_sample(L, logP, NB, 10, lab)
            m, C, chi = observables(lab, L); ms.append(m); Cs.append(C); chis.append(chi)
        res['static_'+init_name] = dict(m_rms=float(np.sqrt(np.mean(np.array(ms)**2))), C=[round(float(c),5) for c in np.mean(Cs,0)],
            chi_b={b: round(float(np.mean([c[b] for c in chis])),4) for b in chis[0]}, secs=round(time.time()-t,1))
    print('==', name, 'pqr=', pqr, 'L=', L); print(json.dumps(res, indent=1)); sys.stdout.flush()
    return res

if __name__ == '__main__':
    out = {}
    out['native_312'] = run('native (3,1,2)', (3,1,2))
    out['strong_ferro_20_1_1'] = run('strong ferro (20,1,1)', (20,1,1))
    out['very_strong_200_1_1'] = run('very strong (200,1,1)', (200,1,1), nform=40, nstat=20)
    # coding-depth bound check: P(longest decreasing path >= n) <= 6*5^(n-1)/(n+1)!
    from math import factorial
    print('bound n:', {n: 6*5**(n-1)/factorial(n+1) for n in range(6,16,2)})
    json.dump(out, open(sys.argv[1] if len(sys.argv)>1 else '/dev/null','w'), indent=1)
