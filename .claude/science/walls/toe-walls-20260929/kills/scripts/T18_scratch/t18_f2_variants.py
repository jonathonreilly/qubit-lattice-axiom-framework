"""T18 Test A variants (importing t18_f2_locality):
 (1) sanity: the fermion cochain is flat on every commuting square (two disjoint hops) and on every
     single-record plaquette loop whose partner is not on the plaquette;
 (2) far hops carry the covariant PI-FLUX one-body rule (the coin walker's plaquette holonomy is -1)
     instead of zero flux: is the fermion class still unreachable by a bounded-range rule?
"""
import itertools
from t18_f2_locality import build, config_edges, fermion_sign, cheb

def sanity(L=5):
    sites, nbrs, confs, cidx = build(L, 2, 2)
    adj = {}
    for (a,b,u,v,o) in config_edges(sites, nbrs, confs, cidx):
        s = fermion_sign(u,v,o)
        adj[(a,b)] = s; adj[(b,a)] = s
    bad_sq = 0; nsq = 0
    # commuting squares: S={x,y}; x->x2 (edge), y->y2 (edge), all four configs valid and closures disjoint
    E = [(i,j) for i in range(len(sites)) for j in nbrs[i] if i<j]
    for (x,x2) in E:
        for (y,y2) in E:
            if len({x,x2,y,y2})<4: continue
            c = [tuple(sorted(p)) for p in ((x,y),(x2,y),(x2,y2),(x,y2))]
            if any(k not in cidx for k in c): continue
            ids = [cidx[k] for k in c]
            par = 0
            for i in range(4):
                par ^= adj[(ids[i], ids[(i+1)%4])]
            nsq += 1; bad_sq += par
    # single-record plaquette loops with partner off the plaquette
    bad_pl = 0; npl = 0
    for i,s in enumerate(sites):
        x,y = s
        if x+1<L and y+1<L:
            corners = [i, sites.index((x+1,y)), sites.index((x+1,y+1)), sites.index((x,y+1))]
            for w in range(len(sites)):
                if w in corners: continue
                c = [tuple(sorted((k,w))) for k in corners]
                ids = [cidx[k] for k in c]
                par = 0
                for j in range(4):
                    par ^= adj[(ids[j], ids[(j+1)%4])]
                npl += 1; bad_pl += par
    return nsq, bad_sq, npl, bad_pl

def solvable_pi(L, r):
    sites, nbrs, confs, cidx = build(L, 2, 2)
    edges = config_edges(sites, nbrs, confs, cidx)
    nconf = len(confs); keys = {}; piv = {}
    def var(c): return 1 << (c+1)
    for (a,b,u,v,o) in edges:
        near = tuple(w for w in o if min(cheb(sites,w,u),cheb(sites,w,v))<=r)
        rhs = fermion_sign(u,v,o)
        row = var(a) ^ var(b)
        if near:
            key = ((min(u,v),max(u,v)),near)
            keys.setdefault(key, nconf+len(keys)); row ^= var(keys[key])
        else:
            # far hop carries the pi-flux one-body rule: sign (-1)^x on hops along axis 1
            (x1,y1),(x2,y2) = sites[u], sites[v]
            if y1 != y2:      # hop along y  -> sign (-1)^x
                rhs ^= (x1 & 1)
        if rhs: row ^= 1
        while True:
            xx = row & ~1
            if xx == 0:
                if row & 1: return False
                break
            lb = xx & -xx
            if lb in piv: row ^= piv[lb]
            else: piv[lb] = row; break
    return True

if __name__ == "__main__":
    print("sanity (fermion cochain flat on commuting squares / partner-off plaquettes):", sanity(5))
    for L in range(3,8):
        res = [(r, solvable_pi(L, r)) for r in range(0, L)]
        rs = next((r for r,ok in res if ok), None)
        print(f"pi-flux one-body far rule, 2D N=2 L={L}: r*={rs}  {res}")
