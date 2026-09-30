"""T77 Test B: defect price of directed nearest-neighbour ice formation as a function of the formation ORDER.
Model = ICE_SUPPORT note (2026-09-22) soldered model: a vertex takes a uniform consistent record (one of the 20 ice
patterns consistent with its already-recorded links) or none; a link copies the assignments of its formed, recorded
end vertices, takes a fair coin if none, and has no record if two disagree. Coarse vertices of Z^3, links between them.
Orders: lex (open box), diag (open box), random (torus), diagjit (open box, Gaussian jitter on vertex times),
lex_torus (closed volume). Link time = midpoint of its end vertex times (so a link always forms between its ends);
half-links to vertices outside the open box form at t_inside + 0.5, outside vertices never form.
"""
import random, math, itertools, sys, statistics
DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
PATS = [p for p in itertools.product((0,1), repeat=6) if sum(p)==3]   # 20 ice patterns; index d = direction index

def run(L, order, sigma=0.0, seed=0, torus=False):
    rng = random.Random(seed)
    inside = lambda v: all(0 <= c < L for c in v)
    def norm(v): return tuple(c % L for c in v) if torus else v
    verts = [(x,y,z) for x in range(L) for y in range(L) for z in range(L)]
    tv = {}
    if order == 'lex':
        for v in verts: tv[v] = float((v[0]*L+v[1])*L+v[2])
    elif order == 'diag':
        for v in verts: tv[v] = float(sum(v)) + 1e-3*rng.random()
    elif order == 'diagjit':
        for v in verts: tv[v] = float(sum(v)) + rng.gauss(0.0, sigma)
    elif order == 'random':
        for v in verts: tv[v] = rng.random()*len(verts)
    else: raise ValueError(order)
    # links keyed by (v, axis): between v and v+e_axis
    links = []
    for v in ([(x,y,z) for x in range(-1,L) for y in range(-1,L) for z in range(-1,L)] if not torus else verts):
        for a in range(3):
            w = list(v); w[a] += 1; w = tuple(w)
            if torus:
                w = norm(w)
                links.append((v,a))
            else:
                if inside(v) or inside(w): links.append((v,a))
    ev = []
    for v in verts: ev.append((tv[v], 0, v))
    for (v,a) in links:
        w = list(v); w[a] += 1; w = tuple(w)
        if torus: w = norm(w)
        tin = [tv[u] for u in (v,w) if u in tv]
        t = sum(tin)/2.0 if len(tin)==2 else tin[0] + 0.5
        ev.append((t, 1, (v,a)))
    ev.sort()
    pat = {}          # vertex -> tuple(6 bits) or None (formed)
    val = {}          # link -> 0/1/None (formed)
    nprior = {}       # vertex -> number of formed links at its formation time
    for t,kind,obj in ev:
        if kind == 0:
            v = obj
            cons = {}
            nf = 0
            for d,dv in enumerate(DIRS):
                if dv[0]+dv[1]+dv[2] == 1:
                    a = dv.index(1); key = (v,a)
                else:
                    a = dv.index(-1); u = list(v); u[a] -= 1; u = tuple(u); key = (norm(u) if torus else u, a)
                if key in val:
                    nf += 1
                    if val[key] is not None: cons[d] = val[key]
            nprior[v] = nf
            ok = [p for p in PATS if all(p[d]==b for d,b in cons.items())]
            pat[v] = rng.choice(ok) if ok else None
        else:
            v,a = obj
            w = list(v); w[a] += 1; w = tuple(w)
            if torus: w = norm(w)
            bits = []
            if v in pat and pat[v] is not None: bits.append(pat[v][2*a])        # v's +a direction index 2a
            if w in pat and pat[w] is not None: bits.append(pat[w][2*a+1])      # w's -a direction index 2a+1
            if not bits: val[obj] = rng.randint(0,1)
            elif len(set(bits)) == 1: val[obj] = bits[0]
            else: val[obj] = None
    return verts, links, pat, val, nprior, torus

def stats(L, order, sigma, nsamp, torus=False, margin=2, seed0=0):
    vfrac=[]; lfrac=[]; byn={}
    qvar={b:[] for b in (2,3,4)}
    for s in range(nsamp):
        verts, links, pat, val, nprior, tor = run(L, order, sigma, seed=seed0+s, torus=torus)
        vs = [v for v in verts if (torus or all(margin<=c<L-margin for c in v))]
        vfrac.append(sum(1 for v in vs if pat[v] is None)/len(vs))
        for v in vs:
            n = nprior[v]; byn.setdefault(n,[0,0]); byn[n][0]+=1; byn[n][1]+= (pat[v] is None)
        # links whose both ends are in region
        def endv(v,a):
            w=list(v); w[a]+=1; w=tuple(w); return (tuple(c%L for c in w) if torus else w)
        ls = [(v,a) for (v,a) in links if (v in set(vs) and endv(v,a) in set(vs))] if False else None
        vset=set(vs)
        ls=[(v,a) for (v,a) in links if v in vset and endv(v,a) in vset]
        lfrac.append(sum(1 for l in ls if val[l] is None)/len(ls))
        # Gauss charge at an unrecorded vertex: (sum of its six recorded link occupations) - 3
        def links_at(v):
            out=[]
            for d,dv in enumerate(DIRS):
                if dv[0]+dv[1]+dv[2]==1:
                    out.append((v,dv.index(1)))
                else:
                    u=list(v); u[dv.index(-1)]-=1; u=tuple(u); out.append((tuple(c%L for c in u) if torus else u, dv.index(-1)))
            return out
        chg={}
        for v in vs:
            if pat[v] is None:
                vv=[val.get(l) for l in links_at(v)]
                if all(x is not None for x in vv): chg[v]=sum(vv)-3
        # block variance of charge over cubes of side b inside region (positions on a coarse grid)
        lo=margin if not torus else 0; hi=L-margin if not torus else L
        for b in qvar:
            for x0 in range(lo,hi-b+1,b):
                for y0 in range(lo,hi-b+1,b):
                    for z0 in range(lo,hi-b+1,b):
                        q=sum(chg.get((x,y,z),0) for x in range(x0,x0+b) for y in range(y0,y0+b) for z in range(z0,z0+b))
                        qvar[b].append(q)
    out = dict(order=order, sigma=sigma, L=L, torus=torus, nsamp=nsamp,
               vert_defect=statistics.mean(vfrac), vert_defect_se=(statistics.stdev(vfrac)/math.sqrt(len(vfrac)) if len(vfrac)>1 else float('nan')),
               link_defect=statistics.mean(lfrac),
               byn={n:(c, (u/c if c else 0.0)) for n,(c,u) in sorted(byn.items())},
               qvar_per_vol={b:(statistics.mean([q*q for q in qs])/(b**3) if qs else float('nan')) for b,qs in qvar.items()})
    return out

if __name__ == '__main__':
    nsamp = int(sys.argv[1]) if len(sys.argv)>1 else 20
    L = 10
    rows = []
    for (order,sigma,torus) in (('lex',0.0,False),('diag',0.0,False),('diagjit',0.05,False),('diagjit',0.15,False),('diagjit',0.3,False),('diagjit',0.6,False),('diagjit',1.2,False),('random',0.0,True),('lex',0.0,True)):
        r = stats(L, order, sigma, nsamp, torus=torus)
        print(f"{order:8s} sigma={sigma:<4} torus={torus!s:5} vert_defect={r['vert_defect']:.4f}+-{r['vert_defect_se']:.4f} link_defect={r['link_defect']:.4f} byn(count,defect)={ {n:(c,round(d,3)) for n,(c,d) in r['byn'].items()} } Q2/vol={ {b:round(v,4) for b,v in r['qvar_per_vol'].items()} }", flush=True)
