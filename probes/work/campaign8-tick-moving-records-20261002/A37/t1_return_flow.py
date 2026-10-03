"""A37 t1: the return-flow lemma and the classification of 'push' bookkeeping (EXACT enumeration).

A record steps x -> y.  Before, the shared possibilities occupy the window W minus x; after, W minus y.
A conservative step is a bijection f: W\\{x} -> W\\{y} of site contents (classical), or a unitary
V: H_{W\\x} -> H_{W\\y} (quantum).  'Nearest-neighbour reach' means |f(z) - z|_1 <= 1.

(a) 1D windows: every NN bijection has f(y) = x and is otherwise a product of adjacent transpositions
    (swap + unrelated local swaps).  With one item allowed to enter at the left end and one to leave at the
    right end (a segment of an infinite line), the only extra map is the global shift (record rides along).
    With a fresh item at x and one item leaving at the right end, the only map is the half-line conveyor.
(b) 2D windows: the record's move closes a lattice loop through the bond (x,y) of even length (2 = swap,
    >= 4 = flow around).  Net possibility inflow into every cut region containing x but not y is exactly 1;
    the sum of displacements is exactly -e.
(c) 3D window: NN bijections that commute with the quarter turns about the step axis all send y's content
    to x (deterministic covariant flow-around is impossible); non-covariant loops exist.
(d) Quantum: for ANY unitary V between the two possibility spaces, (1/2)[I(K1:R2) - I(K2:R1)] = 1 qubit
    across every cut separating x from y, and 0 across cuts that do not (Choi-state mutual informations).
"""
import signal, itertools
import numpy as np
signal.alarm(55)
rng = np.random.default_rng(37)

def enum_bijections(dom, cod, nbrs):
    """All bijections f: dom -> cod with f(z) in nbrs[z] (backtracking). dom, cod: lists of sites."""
    dom = sorted(dom, key=lambda z: len([w for w in nbrs[z] if w in cod]))
    codset = set(cod)
    out, cur, used = [], {}, set()
    def rec(i):
        if i == len(dom):
            out.append(dict(cur)); return
        z = dom[i]
        for w in nbrs[z]:
            if w in codset and w not in used:
                used.add(w); cur[z] = w
                rec(i + 1)
                used.discard(w); del cur[z]
    rec(0)
    return out

# ---------------- (a) 1D ----------------
print("(a) 1D windows, record at x stepping to y = x+1, every content moving at most one site")
for n, x, others in [(6, 2, []), (8, 3, []), (10, 4, []), (10, 4, [8]), (10, 4, [1, 8])]:
    y = x + 1
    W = list(range(n)); dom = [z for z in W if z != x and z not in others]
    cod = [z for z in W if z != y and z not in others]
    nb = {z: [w for w in (z - 1, z, z + 1) if 0 <= w < n] for z in W}
    maps = enum_bijections(dom, cod, nb)
    ok = 0
    for f in maps:
        swaplike = f[y] == x and all(f[f[z]] == z for z in dom if z != y and f[z] != x)
        ok += swaplike
    print(f"   n={n:2d} x={x} other records {others}: {len(maps):4d} maps; f(y)=x and the rest adjacent "
          f"transpositions in {ok}/{len(maps)}")
# segment of an infinite line: one item may enter at the left end (-1 -> 0) and one leave at the right end
n, x = 8, 3; y = 4
W = list(range(n))
nb = {z: [w for w in (z - 1, z, z + 1) if -1 <= w <= n] for z in range(-1, n)}
dom = [-1] + [z for z in W if z != x]; cod = [z for z in W if z != y] + [n]
maps = enum_bijections(dom, cod, nb)
print(f"   through-flow (one item in at the left, one out at the right), n={n}: {len(maps)} map(s); "
      f"global shift: {[all(f[z] == z + 1 for z in dom) for f in maps]}")
nbf = dict(nb); nbf["fresh"] = [x]
dom = ["fresh"] + [z for z in W if z != x]; cod = [z for z in W if z != y] + [n]
maps = enum_bijections(dom, cod, nbf)
conv = [f for f in maps if all(f[z] == z + 1 for z in range(y, n)) and all(f[z] == z for z in range(0, x))]
print(f"   fresh content at x, one item out at the right end: {len(maps)} map(s); "
      f"half-line conveyor (left part fixed, right part shifted): {len(conv)}"
      f"{' (others differ only by adjacent swaps on the left)' if len(maps) > len(conv) else ''}")

# ---------------- (b) 2D ----------------
print("(b) 2D windows: the loop through the record's bond, flux and displacement identities")
for (a, b) in [(3, 3), (3, 4), (4, 4), (4, 5)]:
    W = [(i, j) for i in range(a) for j in range(b)]
    x = (1, 1); y = (2, 1) if a > 2 else None
    e = (1, 0)
    nb = {z: [w for w in [z, (z[0]+1, z[1]), (z[0]-1, z[1]), (z[0], z[1]+1), (z[0], z[1]-1)] if w in W] for z in W}
    dom = [z for z in W if z != x]; cod = [z for z in W if z != y]
    maps = enum_bijections(dom, cod, nb)
    lengths = {}
    flux_bad = disp_bad = 0
    cuts = [[z for z in W if z[0] <= 1], [z for z in W if z[0] <= 1 and z[1] <= 1], [x],
            [z for z in W if z != y and abs(z[0]-1) + abs(z[1]-1) <= 1]]
    for f in maps:
        F = dict(f); F[x] = y
        L = 1; z = y
        while z != x:
            z = F[z]; L += 1
        lengths[L] = lengths.get(L, 0) + 1
        for S in cuts:
            Sset = set(S)
            inflow = sum(1 for z in dom if z not in Sset and f[z] in Sset) - sum(1 for z in dom if z in Sset and f[z] not in Sset)
            flux_bad += inflow != 1
        dsum = np.sum([np.subtract(f[z], z) for z in dom], axis=0)
        disp_bad += not np.array_equal(dsum, -np.array(e))
    print(f"   {a}x{b} window: {len(maps):6d} maps; loop length through the record's bond: "
          f"{dict(sorted(lengths.items()))}; flux identity failures {flux_bad} (over {len(cuts)} cuts each); "
          f"displacement-sum failures {disp_bad}")

# ---------------- (c) 3D, quarter turns about the step axis ----------------
print("(c) 3D window around the bond (x,y): NN bijections that commute with the quarter turns about the step axis")
x = (0, 0, 0); y = (1, 0, 0)
W = [x, y, (-1, 0, 0), (2, 0, 0)] + [(a, s, 0) for a in (0, 1) for s in (1, -1)] + [(a, 0, s) for a in (0, 1) for s in (1, -1)]
R = lambda p: (p[0], -p[2], p[1])                     # quarter turn about the x axis
assert all(R(p) in W for p in W)
def nbrs3(z):
    c = [z] + [tuple(np.add(z, d)) for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
    return [w for w in c if w in W]
nb = {z: nbrs3(z) for z in W}
dom = [z for z in W if z != x]; cod = [z for z in W if z != y]
maps = enum_bijections(dom, cod, nb)
eq = [f for f in maps if all(f[R(z)] == R(f[z]) for z in dom)]
print(f"   {len(W)}-site window: {len(maps)} NN maps; f(y)=x in {sum(f[y]==x for f in maps)}; "
      f"loops (f(y) a side site) in {sum(f[y] not in (x,) for f in maps)}")
print(f"   commuting with the quarter turns: {len(eq)} maps; f(y)=x in {sum(f[y]==x for f in eq)} of them")

# ---------------- (d) quantum kinematic flux ----------------
print("(d) quantum: Choi-state information flux of a unitary step between the two possibility spaces")
def entropy_bits(rho):
    w = np.linalg.eigvalsh(rho); w = w[w > 1e-14]
    return float(-(w * np.log2(w)).sum())
def reduced(psi, keep, nq):
    t = psi.reshape([2] * nq)
    rest = [i for i in range(nq) if i not in keep]
    m = np.transpose(t, keep + rest).reshape(2 ** len(keep), -1)
    return m @ m.conj().T
def mi(psi, A, B, nq):
    return entropy_bits(reduced(psi, A, nq)) + entropy_bits(reduced(psi, B, nq)) - entropy_bits(reduced(psi, A + B, nq))
def perm_unitary(in_sites, out_sites, f):
    """Unitary moving the content of input site z to output site f[z] (qubit orderings in_sites/out_sites)."""
    k = len(in_sites); V = np.zeros((2 ** k, 2 ** k))
    pos = [out_sites.index(f[z]) for z in in_sites]
    for bidx in range(2 ** k):
        bits = [(bidx >> (k - 1 - i)) & 1 for i in range(k)]
        ob = [0] * k
        for i in range(k):
            ob[pos[i]] = bits[i]
        V[sum(bt << (k - 1 - i) for i, bt in enumerate(ob)), bidx] = 1
    return V
# window 0..4, record x=1 -> y=2. Inputs (before) sites [0,2,3,4]; outputs (after) sites [0,1,3,4].
ins, outs = [0, 2, 3, 4], [0, 1, 3, 4]
k = 4
def flux(V, cut):
    """cut: sites < cut on the left. Returns (I(K1:R2), I(K2:R1), half difference) in bits/qubits."""
    omega = np.zeros(4 ** k)
    for i in range(2 ** k):
        omega[i * 2 ** k + i] = 1
    omega /= np.sqrt(2 ** k)
    psi = np.kron(V, np.eye(2 ** k)) @ omega            # qubits 0..k-1 outputs, k..2k-1 references
    K1 = [i for i, s in enumerate(outs) if s < cut]; K2 = [i for i, s in enumerate(outs) if s >= cut]
    R1 = [k + i for i, s in enumerate(ins) if s < cut]; R2 = [k + i for i, s in enumerate(ins) if s >= cut]
    a = mi(psi, K1, R2, 2 * k) if K1 and R2 else 0.0
    b = mi(psi, K2, R1, 2 * k) if K2 and R1 else 0.0
    return a, b, (a - b) / 2
SWv = perm_unitary(ins, outs, {0: 0, 2: 1, 3: 3, 4: 4})
PL1 = perm_unitary(ins, outs, {0: 0, 2: 3, 3: 1, 4: 4})          # y -> y+1, y+1 jumps back to x
A = rng.normal(size=(16, 16)) + 1j * rng.normal(size=(16, 16)); RU, _ = np.linalg.qr(A)
for name, V in [("swap", SWv), ("capped line push L=1", PL1), ("random unitary", RU)]:
    rows = []
    for cut in (1, 2, 3, 4):
        a, b, d = flux(V, cut)
        rows.append(f"cut {cut-0.5:.1f}: {a:.6f}-{b:.6f} -> {d:+.6f}")
    print(f"   {name:22s} " + " | ".join(rows))
print("   (cut 1.5 separates x=1 from y=2; the others do not)")
