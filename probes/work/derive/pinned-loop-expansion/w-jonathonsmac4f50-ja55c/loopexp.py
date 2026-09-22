"""pinned-scale loop expansion, exact (six-axis menu): brute force by layered DP; the leafless expansion with strand kernels."""
import itertools
from fractions import Fraction as F

AX = [(1, 0), (-1, 0), (1, 1), (-1, 1), (1, 2), (-1, 2)]

def Kmat(p, q, r):
    S = p + q + 4 * r
    return [[F(p if (a == b) else q if a[1] == b[1] else r, S) for b in AX] for a in AX]

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(6)) for j in range(6)] for i in range(6)]

def kpow(K, L):
    R = [[F(int(i == j)) for j in range(6)] for i in range(6)]
    for _ in range(L): R = matmul(R, K)
    return R

def grid(dims):
    V = list(itertools.product(*[range(d) for d in dims]))
    E = []
    for v in V:
        for i in range(len(dims)):
            w = list(v); w[i] += 1; w = tuple(w)
            if w[i] < dims[i]: E.append((v, w))
    return V, E

def phi_brute(V, E, K):
    """Phi = E_s[prod_e 6K(s_e)] over independent uniform contents, by eliminating vertices in order (exact)."""
    k = [[6 * K[a][b] for b in range(6)] for a in range(6)]
    # generic variable elimination over the vertex list order
    factors = [((u, v), {(a, b): k[a][b] for a in range(6) for b in range(6)}) for (u, v) in E]
    for x in V:
        involved = [f for f in factors if x in f[0]]
        rest = [f for f in factors if x not in f[0]]
        scope = sorted({y for f in involved for y in f[0] if y != x})
        table = {}
        for assign in itertools.product(range(6), repeat=len(scope)):
            env = dict(zip(scope, assign)); tot = F(0)
            for a in range(6):
                env[x] = a; prod = F(1)
                for sc, tab in involved:
                    prod *= tab[tuple(env[y] for y in sc)]
                tot += prod
            table[assign] = tot / 6
        factors = rest + [(tuple(scope), table)]
    val = F(1)
    for sc, tab in factors: val *= tab[()]
    return val

def leafless_subsets(E):
    out = []
    for k in range(len(E) + 1):
        for H in itertools.combinations(E, k):
            deg = {}
            for u, v in H:
                deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
            if all(d >= 2 for d in deg.values()): out.append(H)
    return out

def strands_of(H):
    deg = {}; adj = {}
    for e in H:
        u, v = e
        deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
        adj.setdefault(u, []).append((v, e)); adj.setdefault(v, []).append((u, e))
    comps = []; seen = set()
    for v0 in deg:
        if v0 in seen: continue
        st = [v0]; comp = {v0}
        while st:
            x = st.pop()
            for y, _ in adj[x]:
                if y not in comp: comp.add(y); st.append(y)
        seen |= comp; comps.append(comp)
    out = []
    for comp in comps:
        branch = sorted(v for v in comp if deg[v] >= 3)
        cedges = [e for e in H if e[0] in comp]
        if not branch:
            out.append((None, len(cedges))); continue
        used = set(); strands = []
        for b in branch:
            for (y, e) in adj[b]:
                if e in used: continue
                L = 1; used.add(e); cur = y
                while deg[cur] == 2:
                    (n1, e1), (n2, e2) = adj[cur]
                    nxt, ne = ((n1, e1) if e1 not in used else (n2, e2))
                    used.add(ne); L += 1; cur = nxt
                strands.append((b, cur, L))
        out.append((branch, strands))
    return out

def w_transfer(H, K, lam=None):
    """leafless weight by the transfer rule: each component = E over branch-vertex contents of prod over strands of
    (6 K^L - 1)(s_u, s_v); a pure cycle of length n gives tr(K^n) - 1 = 3 l1^n + 2 l2^n."""
    if not H: return F(1)
    total = F(1)
    for comp in strands_of(H):
        if comp[0] is None:
            n = comp[1]
            Kn = kpow(K, n)
            total *= sum(Kn[i][i] for i in range(6)) - 1
            continue
        branch, strands = comp
        kers = [[[6 * x - 1 for x in row] for row in kpow(K, L)] for (_, _, L) in strands]
        pos = {b: i for i, b in enumerate(branch)}
        acc = F(0)
        for assign in itertools.product(range(6), repeat=len(branch)):
            prod = F(1)
            for (u, v, L), ker in zip(strands, kers):
                prod *= ker[assign[pos[u]]][assign[pos[v]]]
                if prod == 0: break
            acc += prod
        total *= acc / F(6) ** len(branch)
    return total
