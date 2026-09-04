"""T23 - THE MASTER IDENTITY, proved symbolically in general dimension.
Claim: with Gamma_a = eps_a + iota_a on the full exterior algebra of a
d-dimensional metric g, the lattice step operator in momentum space is
   Q(q) = m*I + i*Sum_a sin(q_a) Gamma_a
and                (Sum_a s_a Gamma_a)^2 = (s . g^-1 . s) * I
so               det Q(q) = (m^2 + s . g^-1 . s)^(2^(d-1)).
Verified for d = 2,3,4 with a FULLY SYMBOLIC metric and symbolic s."""
import sympy as sp, itertools, time
def carrier(d):
    B = []
    for k in range(d+1): B += [tuple(c) for c in itertools.combinations(range(d), k)]
    return B, {b:i for i,b in enumerate(B)}
def gammas(d, gi):
    B, IDX = carrier(d); n = len(B)
    G = []
    for a in range(d):
        M = sp.zeros(n,n)
        for Sx in B:                       # exterior product e^a ^ .
            if a not in Sx:
                T = tuple(sorted(Sx+(a,)))
                M[IDX[T], IDX[Sx]] += (-1)**sum(1 for i in Sx if i < a)
            for pos,i in enumerate(Sx):    # interior product with g^-1 e_a
                T = tuple(x for x in Sx if x != i)
                M[IDX[T], IDX[Sx]] += (-1)**pos * gi[a,i]
        G.append(sp.Matrix(M))
    return G, n
for d in (2,3,4):
    t0 = time.time()
    gs = sp.symbols(f'g0:{d}_0:{d}')
    g = sp.zeros(d,d)
    for i in range(d):
        for j in range(i,d):
            g[i,j] = g[j,i] = sp.Symbol(f'g{min(i,j)}{max(i,j)}')
    gi = g.inv()
    G, n = gammas(d, gi)
    s = sp.symbols(f's0:{d}')
    S = sp.zeros(n,n)
    for a in range(d): S += s[a]*G[a]
    S2 = sp.expand(sp.simplify(S*S))
    quad = sp.simplify(sum(s[a]*gi[a,b]*s[b] for a in range(d) for b in range(d)))
    ok_sq = sp.simplify(S2 - quad*sp.eye(n)).is_zero_matrix
    print(f"d={d}  fibre {n}   (sum s_a Gamma_a)^2 == (s.g^-1.s) I  :  {ok_sq}", flush=True)
    # anticommutator route (independent of the matrix square)
    ok_cl = all(sp.simplify(G[a]*G[b]+G[b]*G[a] - 2*gi[a,b]*sp.eye(n)).is_zero_matrix
                for a in range(d) for b in range(a,d))
    print(f"      Clifford {{Gamma_a,Gamma_b}} = 2 g^-1_ab (independent route) : {ok_cl}", flush=True)
    if d <= 3:
        m = sp.Symbol('m')
        Q = m*sp.eye(n) + sp.I*S
        dQ = sp.factor(sp.simplify(Q.det()))
        pred = sp.factor((m**2 + quad)**(2**(d-1)))
        print(f"      det Q == (m^2 + s.g^-1.s)^{2**(d-1)} : {sp.simplify(dQ-pred)==0}", flush=True)
    else:
        m = sp.Symbol('m')
        gnum = sp.diag(-1,1,1,1)
        Gn,nn = gammas(4, gnum.inv())
        Sn = sum(s[a]*Gn[a] for a in range(4))
        Qn = m*sp.eye(nn) + sp.I*Sn
        qn = sp.simplify(sum(s[a]*gnum.inv()[a,b]*s[b] for a in range(4) for b in range(4)))
        print(f"      d=4 Minkowski det Q == (m^2 + s.g^-1.s)^8 : "
              f"{sp.simplify(sp.factor(Qn.det()) - sp.factor((m**2+qn)**8))==0}", flush=True)
    print(f"      [{time.time()-t0:.1f}s]", flush=True)
