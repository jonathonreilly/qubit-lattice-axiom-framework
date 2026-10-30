"""Class-inverting automorphisms (Chen-Fallbacher-Mahanthappa-Ratz-Trautner 2014 'type' test) for F21 = T7 (code point
stabiliser) and Delta(27) (PR #10077 (ii)), plus AGammaL(1,8). Brute force over generator images."""
import itertools
def mk(gens, mul, e):
    G = {e}; fr = [e]
    while fr:
        nf = []
        for a in fr:
            for g in gens:
                c = mul(a, g)
                if c not in G: G.add(c); nf.append(c)
        fr = nf
    return G
def analyse(name, gens, mul, e, inv):
    G = mk(gens, mul, e); G = list(G)
    cls = {}
    for g in G:
        if g in cls: continue
        C = frozenset(mul(mul(h, g), inv(h)) for h in G)
        for c in C: cls[c] = C
    # words: express every element as product of generators (BFS)
    word = {e: []}; fr = [e]
    while fr:
        nf = []
        for a in fr:
            for i, g in enumerate(gens):
                c = mul(a, g)
                if c not in word: word[c] = word[a] + [i]; nf.append(c)
        fr = nf
    n_aut = 0; n_ci = 0
    for imgs in itertools.product(G, repeat=len(gens)):
        phi = {}
        for g, w in word.items():
            x = e
            for i in w: x = mul(x, imgs[i])
            phi[g] = x
        if len(set(phi.values())) != len(G): continue
        if not all(phi[mul(a, b)] == mul(phi[a], phi[b]) for a in G for b in G): continue
        n_aut += 1
        if all(phi[g] in cls[inv(g)] for g in G): n_ci += 1
    print(f"{name}: |G| = {len(G)}, classes {len(set(cls.values()))}, |Aut| = {n_aut}, class-inverting automorphisms: {n_ci}")
# F21 as affine maps x -> a x + b on Z7, a in {1,2,4}
mul21 = lambda p, q: ((p[0] * q[0]) % 7, (p[0] * q[1] + p[1]) % 7)
inv21 = lambda p: (pow(p[0], -1, 7), (-pow(p[0], -1, 7) * p[1]) % 7)
analyse("F21 = Z7 x| Z3 (T7)", [(1, 1), (2, 0)], mul21, (1, 0), inv21)
# Delta(27) = Heisenberg group mod 3: (a,b,c)*(a',b',c') = (a+a', b+b', c+c'+a b')
mulH = lambda p, q: ((p[0] + q[0]) % 3, (p[1] + q[1]) % 3, (p[2] + q[2] + p[0] * q[1]) % 3)
invH = lambda p: ((-p[0]) % 3, (-p[1]) % 3, (-p[2] + p[0] * p[1]) % 3)
analyse("Delta(27) = Heis(Z3)", [(1, 0, 0), (0, 1, 0)], mulH, (0, 0, 0), invH)
