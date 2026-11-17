# Guide: rank over GF(2) of the plaquette -> link boundary map on periodic 4-boxes (CW cells; sides may be 1 or 2).
import itertools
def rank_gf2(rows):
    piv = {}; r = 0
    for v in rows:
        while v:
            h = v.bit_length()-1
            if h in piv: v ^= piv[h]
            else: piv[h] = v; r += 1; break
    return r
def run(Ls):
    sites = list(itertools.product(*[range(L) for L in Ls])); V = len(sites)
    sid = {s:i for i,s in enumerate(sites)}
    def sh(s, mu): t = list(s); t[mu] = (t[mu]+1) % Ls[mu]; return tuple(t)
    def link(s, mu): return 4*sid[s]+mu
    rows = []
    for s in sites:
        for mu, nu in itertools.combinations(range(4), 2):
            m = 0
            for l in (link(s,mu), link(sh(s,mu),nu), link(sh(s,nu),mu), link(s,nu)):
                m ^= 1 << l      # mod 2: a link met twice cancels (CW boundary)
            rows.append(m)
    r = rank_gf2(rows)
    print('sides', Ls, 'V', V, 'plaquettes', len(rows), 'rank', r, '3V-3', 3*V-3, 'match', r == 3*V-3)
for Ls in [(3,3,3,3),(2,2,2,2),(1,2,3,4),(4,3,3,2),(1,1,1,1),(2,3,5,1)]:
    run(Ls)
