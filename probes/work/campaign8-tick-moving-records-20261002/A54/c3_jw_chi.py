"""A54 c3: the explicit (non-local) chi.  Order the corners (lexicographic), K[u,w] = 1 iff pos(u) < pos(w),
Lambda = sublattice parity (even coarse sizes).  M = D^T (K^T + Lambda) D,  B = M + d (symmetric, zero
diagonal), linear part b from the exact phases of S_p.  chi = (-1)^{sum_{l<m} B_lm n_l n_m + b.n}.
Checks: (1) chi X^{dp} chi = S_p as exact Pauli strings (all sectors);  (2) spin-1/2 ice BFS (A52 c4):
chi(n')chi(n) = sign of the dressed flip on every edge, and chi agrees with A52's BFS chi up to one sign;
(3) Q2: chi t_l chi = X_l * (Gauss parities on the JW interval) -- anticommute iff one shared corner,
commute with every bare ring, string lengths;  (4) range of chi's CZ pattern.
Usage: c3_jw_chi.py Lx,Ly,Lz [uniform|random] [bfs_cap]"""
import signal, sys, time
signal.alarm(118)
from collections import deque
from a54lib import *

shape = tuple(int(t) for t in sys.argv[1].split(','))
rk = sys.argv[2] if len(sys.argv) > 2 else 'uniform'
cap = int(sys.argv[3]) if len(sys.argv) > 3 else 50000
assert all(L % 2 == 0 for L in shape), "even coarse sizes (bipartite corner graph) for the +-1 version"
t0 = time.time()
tor, recs, hops, dcol, loops, dp, Ddp = setup(shape, 0, rk, seed=21)
n = tor.n; NP = len(dp)
corners = sorted(tor.corners, key=lambda c: c[::-1]); pos = {c: k for k, c in enumerate(corners)}
lam = {c: (sum(c) // 2) % 2 for c in corners}
star = {c: gauss_string(tor, c)[1] for c in corners}
J = []; Mcol = []
for l in range(n):
    v, i, w, ip = tor.ends(l)
    a, b2 = (v, w) if pos[v] < pos[w] else (w, v)
    Js = {c for c in corners if pos[a] < pos[c] <= pos[b2]}
    if a == b2: Js = set()
    for c in (v, w):
        if lam[c]: Js ^= {c}
    J.append(Js)
    m = 0
    for c in Js: m ^= star[c]
    Mcol.append(m)
Bcol = [Mcol[l] ^ dcol[l] for l in range(n)]
sym = sum(((Bcol[l] >> m) & 1) != ((Bcol[m] >> l) & 1) for l in range(n) for m in range(n))
diag = sum((Bcol[l] >> l) & 1 for l in range(n))
mdp = 0
for p in range(NP):
    z = 0
    for l in bits_of(dp[p]): z ^= Mcol[l]
    mdp += z != 0
print("torus %s, records %s: B asymmetric entries %d, diagonal ones %d, plaquettes with M dp != 0: %d" % (
    shape, rk, sym, diag, mdp))
def Bx(x):
    z = 0
    for l in bits_of(x): z ^= Bcol[l]
    return z
def quad(x):
    s = 0
    for l in bits_of(x): s += popc(Bcol[l] & x)
    assert s % 2 == 0
    return (s // 2) & 1
S = stabilizer_signs_ok(tor, hops, loops)
assert all(S[p][0] == dp[p] and S[p][1] == Ddp[p] for p in range(NP))
odd = sum(S[p][2] % 2 for p in range(NP))
G = GF2()
for p in range(NP):
    tau = (S[p][2] // 2 + quad(dp[p])) & 1
    row = tau
    for l in bits_of(dp[p]): row ^= 1 << (l + 1)
    G.add(row)
bsol = G.solve(n)
print("  S_p phases: odd (i or -i) %d; linear part b: %s" % (odd, 'found' if bsol is not None else 'NONE (sign obstruction)'))
bvec = bsol if bsol is not None else 0
def chi_conj(P):
    x, z, ph = P
    return (x, z ^ Bx(x), (ph + 2 * (quad(x) + popc(bvec & x))) % 4)
bad = sum(chi_conj((dp[p], 0, 0)) != S[p] for p in range(NP))
print("  (1) chi X^{dp} chi == S_p exactly (Pauli strings incl. phase): mismatches %d of %d" % (bad, NP))
def chi_val(st):
    return -1 if (quad(st) + popc(bvec & st)) & 1 else 1
# (2) spin-1/2 ice BFS, A52 c4 conventions
st0 = 0
for l in range(n):
    v, i, w, ip = tor.ends(l); a = i // 2
    if (-1) ** (sum(v[bb] // 2 for bb in range(3) if bb != a)) == -1: st0 |= 1 << l
lps = [[(l, SIGN[i]) for (l, v, i, w, ip) in lp] for lp in loops]
def flip(st, loop, dagger, dressed):
    seq = loop if not dagger else loop[::-1]; sign = 1
    for (l, s) in seq:
        e = -1 if (st >> l) & 1 else 1
        if s * e != (-1 if not dagger else 1): return None
        if dressed and popc(st & dcol[l]) % 2: sign = -sign
        st ^= 1 << l
    return st, sign
chiB = {st0: 1}; q = deque([st0]); edges = 0; badE = 0; incons = 0
while q and len(chiB) < cap:
    st = q.popleft()
    for loop in lps:
        for dg in (False, True):
            r = flip(st, loop, dg, True)
            if r is None: continue
            st2, sg = r; edges += 1
            badE += chi_val(st2) * chi_val(st) != sg
            if st2 in chiB:
                incons += chiB[st2] != chiB[st] * sg
            else:
                chiB[st2] = chiB[st] * sg; q.append(st2)
rel = {chi_val(s) * c for s, c in chiB.items()}
print("  (2) spin-1/2 ice BFS: states %d%s, edges %d; edges where chi fails %d; BFS sign inconsistencies %d;"
      " chi * chi_BFS takes values %s" % (len(chiB), '' if not q else ' (capped)', edges, badE, incons, sorted(rel)))
# (3) Q2: conjugated hops
H2 = [chi_conj(h) for h in hops]
okform = sum(H2[l][0] != (1 << l) or H2[l][1] != Mcol[l] for l in range(n))
pairbad = 0
for l in range(n):
    vl, _, wl, _ = tor.ends(l)
    for m in range(l + 1, n):
        vm, _, wm, _ = tor.ends(m)
        want = len({vl, wl} & {vm, wm}) % 2
        pairbad += anticomm(H2[l], H2[m]) != want
        pairbad += anticomm(hops[l], hops[m]) != anticomm(H2[l], H2[m])
ringbad = sum(anticomm(H2[l], (dp[p], 0, 0)) for l in range(n) for p in range(NP))
lens = [len(Js) for Js in J]
print("  (3) chi t_l chi = X_l * prod_{v in J(l)} G_v: form mismatches %d; pair rule (anticommute iff one shared corner)"
      " violations %d; anticommutations with bare rings %d; Gauss-string length min/mean/max %d/%.1f/%d"
      % (okform, pairbad, ringbad, min(lens), sum(lens) / n, max(lens)))
far = max(link_d2(tor, l, m) for l in range(n) for m in bits_of(Bcol[l]))
ncz = sum(popc(c) for c in Bcol) // 2
print("  (4) chi = CZ on %d link pairs; farthest coupled pair distance^2 %d (torus max %d)" % (
    ncz, far, max(link_d2(tor, 0, m) for m in range(n))))
print("done (%.1f s)" % (time.time() - t0))
