# Guide checks of the algebra in gap-crux2-astra62.md: force convention,
# Gauss law (10), the pattern (11), tree-gauge invariance of div j,
# identity (5), the Gram step, and the Lipschitz constants in (13).
import math
import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quat import *  # noqa

rng = random.Random(20261118)
b = 2.45
lat = Lattice([3, 3, 4, 3], rng=rng, cold=False)

# 1. Force convention: d/deps S(exp(eps c) U_e) = -c . N_e
maxerr = 0.0
for trial in range(5):
    x = rng.choice(lat.sites)
    mu = rng.randrange(4)
    c = (rng.gauss(0, 1), rng.gauss(0, 1), rng.gauss(0, 1))
    N = lat.force(x, mu, b)
    u0 = lat.U[(x, mu)]
    h = 1e-6
    lat.U[(x, mu)] = qmul(qexp(c, h), u0)
    sp = lat.action(b)
    lat.U[(x, mu)] = qmul(qexp(c, -h), u0)
    sm = lat.action(b)
    lat.U[(x, mu)] = u0
    fd = (sp - sm)/(2*h)
    maxerr = max(maxerr, abs(fd + vdot(c, N)))
print("force convention |dS/deps + c.N| max:", "%.2e" % maxerr)

# 2. Gauss law at every site: sum_out N = sum_in Ad(U)^-1 N
gmax = 0.0
F = {}
for x in lat.sites:
    for mu in range(4):
        F[(x, mu)] = lat.force(x, mu, b)
for z in lat.sites:
    out = (0.0, 0.0, 0.0)
    inn = (0.0, 0.0, 0.0)
    for mu in range(4):
        out = vadd(out, F[(z, mu)])
        y = lat.sh(z, mu, -1)
        inn = vadd(inn, ad_inv(lat.U[(y, mu)], F[(y, mu)]))
    gmax = max(gmax, math.sqrt(vnorm2(vsub(out, inn))))
print("Gauss law residual max over sites:", "%.2e" % gmax)
print("max |N_e|/(6b):", "%.3f" % max(math.sqrt(vnorm2(v))/(6*b) for v in F.values()))

# 3. Pattern (11): all links 1 except U_l = u, U_m = w, l=(y,i), m=(y,j), z=y+i
lat2 = Lattice([5, 5, 5, 5], cold=True)
y = (2, 2, 2, 2)
res = []
for (i, j) in [(0, 1), (1, 0), (2, 3), (0, 3)]:
    for key in list(lat2.U.keys()):
        lat2.U[key] = ONE
    u = (0.6, 0.0, 0.0, 0.0)
    u = (3/5, 4/5, 0.0, 0.0)          # (3 + 4 i)/5
    w = (3/5, 0.0, 4/5, 0.0)          # (3 + 4 j)/5
    lat2.U[(y, i)] = u
    lat2.U[(y, j)] = w
    z = lat2.sh(y, i)
    B = (0.0, 0.0, 0.0)
    for mu in range(4):
        t = lat2.sh(z, mu, -1)
        N = lat2.force(t, mu, b)
        B = vadd(B, vsub(ad_inv(lat2.U[(t, mu)], N), N))
    res.append(((i, j), tuple(round(v/b, 6) for v in B)))
print("B_z/b for the (11) pattern, by (i,j):", res)
print("expected 32/25 =", 32/25)

# 4. Tree-gauge invariance: div j^{T,v}(z) in the original gauge equals
#    v.B_z computed in the tree gauge (whole torus as the cell).
def random_spanning_tree(lat, rng):
    edges = [(x, mu) for x in lat.sites for mu in range(4)]
    rng.shuffle(edges)
    parent = {x: x for x in lat.sites}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    tree = set()
    for (x, mu) in edges:
        yv = lat.sh(x, mu)
        ra, rb = find(x), find(yv)
        if ra != rb:
            parent[ra] = rb
            tree.add((x, mu))
    return tree


def transport_frame(lat, tree, root, v):
    adj = {x: [] for x in lat.sites}
    for (x, mu) in tree:
        yv = lat.sh(x, mu)
        adj[x].append((yv, (x, mu), 'tail'))   # x is the tail of link
        adj[yv].append((x, (x, mu), 'head'))   # yv is the head of link
    n = {root: v}
    g = {root: ONE}
    stack = [root]
    while stack:
        p = stack.pop()
        for (c, link, role) in adj[p]:
            if c in n:
                continue
            Ul = lat.U[link]
            if role == 'tail':
                # parent p is the tail, child c the head: n_c = Ad(U)^-1 n_p
                n[c] = ad_inv(Ul, n[p])
                g[c] = qmul(g[p], Ul)
            else:
                # parent p is the head, child c the tail: n_c = Ad(U) n_p
                n[c] = ad(Ul, n[p])
                g[c] = qmul(g[p], qconj(Ul))
            stack.append(c)
    return n, g


tree = random_spanning_tree(lat, rng)
root = lat.sites[0]
v = (0.48, -0.6, 0.64)
nv = math.sqrt(vnorm2(v))
v = vscale(1/nv, v)
n, g = transport_frame(lat, tree, root, v)
assert len(n) == len(lat.sites) and len(tree) == len(lat.sites) - 1
# tree defects are zero
tmax = 0.0
for (x, mu) in tree:
    yv = lat.sh(x, mu)
    tmax = max(tmax, math.sqrt(vnorm2(vsub(n[x], ad(lat.U[(x, mu)], n[yv])))))
print("defect on tree links max:", "%.2e" % tmax)
divj = {}
for z in lat.sites:
    s = 0.0
    for mu in range(4):
        s += vdot(n[z], F[(z, mu)])
        t = lat.sh(z, mu, -1)
        s -= vdot(n[t], F[(t, mu)])
    divj[z] = s
# tree gauge
latg = Lattice(lat.sides, cold=True)
for (x, mu) in lat.U:
    yv = lat.sh(x, mu)
    latg.U[(x, mu)] = qmul(qmul(g[x], lat.U[(x, mu)]), qconj(g[yv]))
tg = max(abs(latg.U[l][0] - 1.0) for l in tree)
print("tree links in tree gauge, max |Re - 1|:", "%.2e" % tg)
dmax = 0.0
for z in lat.sites:
    B = (0.0, 0.0, 0.0)
    for mu in range(4):
        t = latg.sh(z, mu, -1)
        N = latg.force(t, mu, b)
        B = vadd(B, vsub(ad_inv(latg.U[(t, mu)], N), N))
    dmax = max(dmax, abs(vdot(v, B) - divj[z]))
print("max |div j(z) - v.B_z(tree gauge)|:", "%.2e" % dmax)
print("sample div j values:", [round(divj[z], 4) for z in lat.sites[:5]])

# 5. Identity (5) and Gram step on random rotations
e5 = 0.0
gr = 0.0
for trial in range(2000):
    h1, h2 = haar(rng), haar(rng)
    vv = (rng.gauss(0, 1), rng.gauss(0, 1), rng.gauss(0, 1))
    a1, a2 = ad(h1, vv), ad(h2, vv)
    Kv = vscale(1/3, vadd(vv, vadd(a1, a2)))
    lhs = vnorm2(vv) - vnorm2(Kv)
    rhs = (vnorm2(vsub(vv, a1)) + vnorm2(vsub(vv, a2)) + vnorm2(vsub(a1, a2)))/9
    e5 = max(e5, abs(lhs - rhs))
    u1, u2 = im(h1), im(h2)
    D4 = lam_min_cross([u1, u2])
    G = [[vdot(u1, u1), vdot(u1, u2)], [vdot(u1, u2), vdot(u2, u2)]]
    tr = G[0][0] + G[1][1]
    det = G[0][0]*G[1][1] - G[0][1]**2
    gmin = tr/2 - math.sqrt(max(0.0, tr*tr/4 - det))
    gr = max(gr, abs(D4 - gmin))
    big, small = (u1, u2) if vnorm2(u1) >= vnorm2(u2) else (u2, u1)
    bh = vscale(1/math.sqrt(vnorm2(big)), big)
    assert gmin >= vnorm2(vcross(small, bh))/2 - 1e-12
print("identity (5) max error:", "%.2e" % e5, "; D/4 vs Gram min eig max error:", "%.2e" % gr)

# 6. (13) constants: ||j(n)-j(n')|| <= 12 b ||n-n'||, ||div|| <= 4
r1 = 0.0
r2 = 0.0
for trial in range(20):
    nn = {x: vscale(1/math.sqrt(vnorm2(t)), t) for x in lat.sites
          for t in [(rng.gauss(0, 1), rng.gauss(0, 1), rng.gauss(0, 1))]}
    nn2 = {x: vscale(1/math.sqrt(vnorm2(t)), t) for x in lat.sites
           for t in [(rng.gauss(0, 1), rng.gauss(0, 1), rng.gauss(0, 1))]}
    j1 = {l: vdot(nn[l[0]], F[l]) for l in F}
    j2 = {l: vdot(nn2[l[0]], F[l]) for l in F}
    dj = math.sqrt(sum((j1[l] - j2[l])**2 for l in F))
    dn = math.sqrt(sum(vnorm2(vsub(nn[x], nn2[x])) for x in lat.sites))
    r1 = max(r1, dj/(12*b*dn))
    div = 0.0
    for z in lat.sites:
        s = 0.0
        for mu in range(4):
            s += j1[(z, mu)] - j1[(lat.sh(z, mu, -1), mu)]
        div += s*s
    r2 = max(r2, math.sqrt(div)/(4*math.sqrt(sum(t*t for t in j1.values()))))
print("(13) ratios (must be <= 1): ||dj||/(12b||dn||) max %.3f, ||div j||/(4||j||) max %.3f" % (r1, r2))
