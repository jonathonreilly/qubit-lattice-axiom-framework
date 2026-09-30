"""T77 Test A2: transfer matrix for the every-site balance rule on a prism Z_Lx x Z_Ly x Z_n (periodic in all),
one sublattice (E = x+y+z even). State = (layer z-1, layer z) E-configs. Layer z contains E sites with (x+y+z) even.
Constraint at each odd site (x,y,z): 4 in-plane neighbours (layer z, E) + tau(x,y,z-1) + tau(x,y,z+1) in A.
Reports number of closed walks (= torus count on one sublattice for z-period n even) and dominant growth rate.
"""
import itertools, sys, numpy as np, math
def layer_sites(Lx, Ly, parity):
    return [(x,y) for x in range(Lx) for y in range(Ly) if (x+y)%2==parity]
def run(Lx, Ly, A, ns):
    A=set(A)
    S0 = layer_sites(Lx,Ly,0); S1 = layer_sites(Lx,Ly,1)   # layer z even -> E sites have x+y even; layer z odd -> x+y odd
    idx0 = {s:i for i,s in enumerate(S0)}; idx1 = {s:i for i,s in enumerate(S1)}
    m = len(S0); assert m==len(S1)
    # O sites of layer z even are (x,y) with x+y odd (= S1 positions); their in-plane neighbours are S0 sites
    def inplane_sum(cfg, sites_idx, p):
        x,y=p; s=0
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            s += cfg[sites_idx[((x+dx)%Lx,(y+dy)%Ly)]]
        return s
    cfgs = list(itertools.product((1,-1), repeat=m))
    # layer types alternate: even layer uses S0 config, odd layer uses S1 config
    # constraint at O-sites of even layer z: positions p in S1 : tau_{z-1}(p) [odd layer config, p in S1] + tau_{z+1}(p) + inplane(even cfg at p)
    # constraint at O-sites of odd layer z: positions p in S0 : tau_{z-1}(p)[even layer cfg] + tau_{z+1}(p) + inplane(odd cfg at p)
    def ok(prev, cur, nxt, cur_is_even):
        if cur_is_even:
            for p in S1:
                s = inplane_sum(cur, idx0, p) + prev[idx1[p]] + nxt[idx1[p]]
                if s not in A: return False
        else:
            for p in S0:
                s = inplane_sum(cur, idx1, p) + prev[idx0[p]] + nxt[idx0[p]]
                if s not in A: return False
        return True
    # states: (c_{z-1}, c_z, z parity of c_z). Build transitions over two-step (even, odd) to make the transfer operator layer-parity independent:
    # use state = (c_even, c_odd) pair; step adds two layers.  Simpler: state (a,b) with a in layer z-1 type t, b layer z type 1-t; next state (b,c). Track type in state.
    states = {}
    trans = {}
    for t in (0,1):
        for a in cfgs:
            for b in cfgs:
                states[(t,a,b)] = None
    # reduce: only keep states extendable
    import collections
    adj = collections.defaultdict(list)
    for t in (0,1):       # t = parity of layer of 'b'  (cur). need cur_is_even = (t==0)
        for a in cfgs:
            for b in cfgs:
                for c in cfgs:
                    if ok(a,b,c, t==0):
                        adj[(t,a,b)].append((1-t,b,c))
    # prune states without successors/predecessors iteratively
    changed=True
    preds = collections.defaultdict(set)
    while changed:
        changed=False
        for s in list(adj.keys()):
            adj[s] = [u for u in adj[s] if u in adj and adj[u]]
            if not adj[s]: del adj[s]; changed=True
    nodes = sorted(adj.keys(), key=lambda s: (s[0], s[1], s[2]))
    ni = {s:i for i,s in enumerate(nodes)}
    M = np.zeros((len(nodes),len(nodes)), dtype=object)
    for s in nodes:
        for u in adj[s]:
            if u in ni: M[ni[s], ni[u]] += 1
    Mf = M.astype(float)
    ev = np.linalg.eigvals(Mf) if len(nodes)>0 else []
    rho = max(abs(ev)) if len(nodes)>0 else 0.0
    res = {}
    if len(nodes)>0:
        P = np.eye(len(nodes), dtype=object)
        cur = np.eye(len(nodes), dtype=object)
        for n in range(1, max(ns)+1):
            cur = cur.dot(M)
            if n in ns:
                res[n] = int(sum(cur[i,i] for i in range(len(nodes))))
    return len(nodes), rho, res
if __name__=="__main__":
    for (Lx,Ly) in ((4,4),):
        for name,A in (("A0",[0]),):
            n_states, rho, res = run(Lx,Ly,A,ns=[2,4,6,8,10,12])
            print(f"cross-section {Lx}x{Ly} {name}: reachable states={n_states} spectral radius={rho:.4f} closed walks by z-period n: {res}", flush=True)
