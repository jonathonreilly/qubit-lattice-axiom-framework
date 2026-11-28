from quat import *  # noqa


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


