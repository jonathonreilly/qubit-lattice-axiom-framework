"""R9-5 script 5 (d = 3 feasibility): a tricoordinated, 3-edge-coloured subgraph of Z^3 using every site
once (one qubit per site), on which Kitaev's construction applies verbatim.
A = X+Y+Z even.  A(X,Y,Z) bonds: x -> B(X+sx,Y,Z), y -> B(X,Y+sy,Z), z -> B(X,Y,Z+sz) with
sx = (-1)^{f}, sy = (-1)^{g}, sz = (-1)^{h} constant along the bond's own axis (so each B gets exactly
one bond of each colour).  Check: degrees, colours, connectivity on a periodic 8^3 box, and whether the
dimer (z-bond) graph spans 3D (rank of the cycle-displacement lattice)."""
import numpy as np, itertools, sys
L = 8
def build(sx, sy, sz):
    nb = {}
    for X, Y, Z in itertools.product(range(L), repeat=3):
        if (X+Y+Z) % 2: continue
        a = (X, Y, Z)
        for col, (dx, dy, dz) in [('x', (sx(Y, Z), 0, 0)), ('y', (0, sy(X, Z), 0)), ('z', (0, 0, sz(X, Y)))]:
            b = ((X+dx) % L, (Y+dy) % L, (Z+dz) % L)
            nb.setdefault(a, []).append((b, col, (dx, dy, dz))); nb.setdefault(b, []).append((a, col, (-dx, -dy, -dz)))
    return nb
def check(name, sx, sy, sz):
    nb = build(sx, sy, sz)
    deg_ok = all(len(v) == 3 and sorted(c for _, c, _ in v) == ['x', 'y', 'z'] for v in nb.values()) and len(nb) == L**3
    # BFS with unwrapped displacements: collect winding vectors of closed walks -> span
    start = (0, 0, 0); pos = {start: np.zeros(3, int)}; queue = [start]; winds = []
    while queue:
        u = queue.pop()
        for (v, c, d) in nb[u]:
            pv = pos[u] + np.array(d)
            if v not in pos: pos[v] = pv; queue.append(v)
            else:
                w = pv - pos[v]
                if np.any(w): winds.append(w)
    comp = len(pos)
    rank = np.linalg.matrix_rank(np.array(winds)) if winds else 0
    print('%-48s deg3+colours ok: %s ; component of origin: %d/%d sites ; winding rank: %d' % (name, deg_ok, comp, L**3, rank))
check('all signs +1 (stacked 2D sheets?)', lambda Y, Z: 1, lambda X, Z: 1, lambda X, Y: 1)
check('sx=(-1)^Z, sy=(-1)^X, sz=(-1)^Y', lambda Y, Z: (-1)**Z, lambda X, Z: (-1)**X, lambda X, Y: (-1)**Y)
check('sx=(-1)^(Y+Z), sy=(-1)^(X+Z), sz=(-1)^(X+Y)', lambda Y, Z: (-1)**(Y+Z), lambda X, Z: (-1)**(X+Z), lambda X, Y: (-1)**(X+Y))
check('sx=(-1)^Y, sy=1, sz=1', lambda Y, Z: (-1)**Y, lambda X, Z: 1, lambda X, Y: 1)
check('sx=(-1)^Y, sy=(-1)^Z, sz=1', lambda Y, Z: (-1)**Y, lambda X, Z: (-1)**Z, lambda X, Y: 1)
