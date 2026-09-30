"""T77 Test A: fully covariant one-qubit-per-site balance rule, solution counts.
tau_s in {+1,-1} at every site of the torus Z_L^3 (L even). For every site s the
neighbour sum must lie in an allowed set A. Bipartite => count = c_E * c_O = c^2 (c on one sublattice).
Also a control: parity-typed ice (3 of 6 links occupied at each vertex) on the fine 4x4x4 torus (landed count 9600).
Usage: python3 testA_count.py
"""
import sys, itertools, time
sys.setrecursionlimit(10000)

def torus_nbrs(L, x, y, z):
    return [((x+1)%L,y,z),((x-1)%L,y,z),(x,(y+1)%L,z),(x,(y-1)%L,z),(x,y,(z+1)%L),(x,y,(z-1)%L)]

def count_sublattice(L, A, cap=10**7):
    """count +-1 assignments on the even sublattice E with, for each odd site o, sum of its 6 E-neighbours in A."""
    E = [(x,y,z) for x in range(L) for y in range(L) for z in range(L) if (x+y+z)%2==0]
    O = [(x,y,z) for x in range(L) for y in range(L) for z in range(L) if (x+y+z)%2==1]
    idx = {s:i for i,s in enumerate(E)}
    cons = [[idx[t] for t in torus_nbrs(L,*o)] for o in O]      # each constraint: 6 variable indices
    var2cons = [[] for _ in E]
    for ci,c in enumerate(cons):
        for v in c: var2cons[v].append(ci)
    # a torus with L=4 has distinct neighbours; L>=4 assumed
    psum = [0]*len(cons); rem = [6]*len(cons)
    Aset = set(A)
    def feasible(s, r):
        # can we reach a value in A from partial sum s with r remaining +-1 terms?
        for a in Aset:
            d = a - s
            if abs(d) <= r and (d - r) % 2 == 0:
                return True
        return False
    nvar = len(E)
    val = [0]*nvar
    count = 0
    nodes = 0
    aborted = False
    def rec(i):
        nonlocal count, nodes, aborted
        if aborted: return
        if i == nvar:
            count += 1
            if count >= cap: aborted = True
            return
        nodes += 1
        for t in (1,-1):
            val[i] = t
            ok = True
            for ci in var2cons[i]:
                psum[ci] += t; rem[ci] -= 1
            for ci in var2cons[i]:
                if not feasible(psum[ci], rem[ci]): ok = False; break
            if ok: rec(i+1)
            for ci in var2cons[i]:
                psum[ci] -= t; rem[ci] += 1
            if aborted: return
    rec(0)
    return count, nvar, aborted, nodes

def control_ice():
    """fine 4x4x4 torus: vertices (even,even,even); links = sites with exactly one odd coordinate; 3 of 6 links occupied per vertex."""
    L = 4
    V = [(x,y,z) for x in range(0,L,2) for y in range(0,L,2) for z in range(0,L,2)]
    links = [(x,y,z) for x in range(L) for y in range(L) for z in range(L) if (x%2)+(y%2)+(z%2)==1]
    lidx = {s:i for i,s in enumerate(links)}
    cons = [[lidx[t] for t in torus_nbrs(L,*v)] for v in V]
    n = len(links)
    cnt = 0
    # DFS with constraint pruning on occupations (0/1)
    var2c = [[] for _ in links]
    for ci,c in enumerate(cons):
        for v in c: var2c[v].append(ci)
    ps=[0]*len(cons); rm=[6]*len(cons)
    def rec(i):
        nonlocal cnt
        if i==n:
            cnt+=1; return
        for t in (0,1):
            ok=True
            for ci in var2c[i]:
                ps[ci]+=t; rm[ci]-=1
            for ci in var2c[i]:
                if ps[ci]>3 or ps[ci]+rm[ci]<3: ok=False;break
            if ok: rec(i+1)
            for ci in var2c[i]:
                ps[ci]-=t; rm[ci]+=1
    rec(0)
    return cnt, n

if __name__=="__main__":
    t0=time.time()
    c,n = control_ice()
    print(f"CONTROL parity-typed ice, fine 4x4x4 torus: count={c} (landed 9600), links={n}, log2/link={__import__('math').log2(c)/n:.4f}  [{time.time()-t0:.1f}s]")
    import math
    for name,A in (("A0={0}",[0]),("A1={-2,0,2}",[-2,0,2])):
        for L in (4,6,8):
            t1=time.time()
            cap = 10**7
            c,nv,ab,nodes = count_sublattice(L, A, cap=cap)
            tot = f"{c}^2" if not ab else f">={cap}"
            lg = (math.log2(c)/nv) if (c>0 and not ab) else float('nan')
            print(f"{name} L={L}: vars/sublattice={nv} count_one_sublattice={c}{' (cap hit)' if ab else ''} total={tot} log2(c)/vars={lg:.4f} nodes={nodes} [{time.time()-t1:.1f}s]", flush=True)
