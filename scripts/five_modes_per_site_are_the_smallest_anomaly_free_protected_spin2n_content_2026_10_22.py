AUDIT_INPUT_PATHS = ('docs/FIVE_MODES_PER_SITE_ARE_THE_SMALLEST_ANOMALY_FREE_PROTECTED_SPIN2N_CONTENT_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Why five modes per site: N identical fermion modes, frame group Spin(2N), content = one parity half S+.

For N = 1..7 (and weights-only N = 8, 9) this computes exactly:
  (A) the half-spinor S+ (dim 2^(N-1)) from Jordan-Wigner Majoranas, its irreducibility and weights;
  (B) chirality: is the weight multiset of S+ closed under negation (self-conjugate)?
  (C) perturbative anomalies: the cubic form Tr_{S+} X^3 and the linear (gravitational) form Tr_{S+} X,
      exactly on the Cartan (integer weight sums) and numerically on random generic X;
  (D) protection: the Spin(2N)-invariant bilinears on S+ (symmetric = Majorana mass allowed);
  (E) old SU(2) (Witten) index 2 Tr J3^2 mod 2 for SU(2) subgroups;
  (F) the centre Z4 (N odd): z = exp(i pi (n - N/2)) and the Spin-Z4 count nu = n(+i) - n(-i) mod 16;
  (G) the selection table and the smallest passing N;
  (H) subgroup-loophole catalogue for N = 1..4 (tori, named Lie subgroups, principal SU(2));
  (Z) zoom diagnostic: odd O_h-symmetric clusters of one-mode sites.
Global anomalies beyond the computed indices (pi_4 values, WWW new SU(2) anomaly, Z16 bordism,
Wang-Wen all-anomaly freedom of the Spin(10) 16) are CITED, not rederived.
Supplied model; exact finite group theory; no physical identification.
"""
import itertools, signal, sys
import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 90
signal.signal(signal.SIGALRM, lambda *a: (print('TIMEOUT'), sys.exit(1)))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
rng = np.random.default_rng(20261022)
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'}: {name}" + (f"  [{detail}]" if detail else ''))


def majoranas(N):
    a = np.array([[0, 1], [0, 0]], complex); Z = np.diag([1., -1.]).astype(complex); I = np.eye(2, dtype=complex)
    gs = []
    for j in range(N):
        ops = [Z] * j + [a] + [I] * (N - j - 1)
        c = ops[0]
        for o in ops[1:]:
            c = np.kron(c, o)
        gs += [c + c.conj().T, 1j * (c.conj().T - c)]
    return gs


def spin_data(N):
    g = majoranas(N); d = 2 ** N
    occ = np.array([[(s >> (N - 1 - j)) & 1 for j in range(N)] for s in range(d)])
    even = np.where(occ.sum(1) % 2 == 0)[0]
    gens = {}
    for a, b in itertools.combinations(range(2 * N), 2):
        gens[(a, b)] = (0.5j * g[a] @ g[b])[np.ix_(even, even)]
    E = 2 * occ[even] - 1          # integer weights 2w = +-1 (Cartan M_{2j,2j+1} = n_j - 1/2)
    return gens, E, occ[even]


def bilinears(gens, E, sym):
    d = E.shape[0]
    pos = [(i, j) for i in range(d) for j in range(i if sym else i + 1, d) if not (E[i] + E[j]).any()]
    if not pos:
        return 0
    cols = []
    for (i, j) in pos:
        B = np.zeros((d, d), complex); B[i, j] += 1; B[j, i] += (1 if sym else -1)
        cols.append(np.concatenate([(T.T @ B + B @ T).ravel() for T in gens.values()]))
    M = np.array(cols).T
    s = np.linalg.svd(M, compute_uv=False)
    return int(sum(s < 1e-9)) + max(0, len(pos) - len(s))


def cubic_linear(E):
    N = E.shape[1]
    cub = {(i, j, k): int((E[:, i] * E[:, j] * E[:, k]).sum())
           for i in range(N) for j in range(i, N) for k in range(j, N)}
    return cub, E.sum(0)


def irreducible(gens, E):
    # weights distinct + raising graph connected => commutant = scalars (Schur)
    d = E.shape[0]
    distinct = len({tuple(r) for r in E}) == d
    adj = sum(np.abs(T) for T in gens.values()) > 1e-9
    seen, todo = {0}, [0]
    while todo:
        i = todo.pop()
        for j in np.where(adj[i])[0]:
            if j not in seen:
                seen.add(j); todo.append(j)
    return distinct and len(seen) == d


def witten_index(J3):
    return 2 * np.trace(J3 @ J3).real


def su2_factors(gens, q):  # self-dual / anti-self-dual su(2) on Majoranas q[0..3]
    M = lambda a, b: gens[(min(a, b), max(a, b))] * (1 if a < b else -1)
    out = []
    for s in (+1, -1):
        J = [0.5 * (M(q[1], q[2]) + s * M(q[0], q[3])), 0.5 * (M(q[2], q[0]) + s * M(q[1], q[3])),
             0.5 * (M(q[0], q[1]) + s * M(q[2], q[3]))]
        ok = np.allclose(J[0] @ J[1] - J[1] @ J[0], 1j * J[2]) or np.allclose(J[0] @ J[1] - J[1] @ J[0], -1j * J[2])
        out.append((ok, J[2]))
    return out


print("== A-D: half-spinor S+ of Spin(2N) for N = 1..7 ==")
table = {}
for N in range(1, 8):
    gens, E, occ = spin_data(N); d = E.shape[0]
    irr = irreducible(gens, E) if N > 1 else True
    selfconj = sorted(map(tuple, E)) == sorted(map(tuple, -E))
    cub, lin = cubic_linear(E)
    cubic0 = all(v == 0 for v in cub.values()); lin0 = not lin.any()
    X = sum(rng.normal() * T for T in gens.values())
    tr3, tr1 = np.trace(X @ X @ X).real, np.trace(X).real
    nsym, nanti = bilinears(gens, E, True), bilinears(gens, E, False)
    table[N] = dict(d=d, chiral=not selfconj, cubic0=cubic0 and lin0, nsym=nsym, nanti=nanti, gens=gens, E=E)
    nz = {k: v for k, v in cub.items() if v}
    okD = (nsym, nanti) == ({0: (1, 0), 2: (0, 1)}[N % 4] if N % 2 == 0 else (0, 0))
    okC = (cubic0 == (N not in (1, 3))) and (lin0 == (N != 1)) and (abs(tr3) < 1e-8) == cubic0
    check(f"ABCD{N} N={N}: S+ dim {d} irr; selfconj={selfconj}; cubic0={cubic0} lin0={lin0} "
          f"{' coeffs ' + str(nz) if nz else ''}; bilinears sym={nsym} anti={nanti}"
          f" -> mass {'ALLOWED' if nsym else 'forbidden'}",
          d == 2 ** (N - 1) and irr and selfconj == (N % 2 == 0) and okC and okD)

print("== Weights-only N = 8, 9 (cubic form of S+) ==")
for N in (8, 9):
    E = np.array([[2 * ((s >> j) & 1) - 1 for j in range(N)] for s in range(2 ** N) if bin(s).count('1') % 2 == 0])
    cub, lin = cubic_linear(E)
    check(f"C{N} N={N}: cubic and linear forms vanish; self-conjugate = {N % 2 == 0}",
          all(v == 0 for v in cub.values()) and not lin.any()
          and (sorted(map(tuple, E)) == sorted(map(tuple, -E))) == (N % 2 == 0))

print("== E: old SU(2) (Witten) index 2 Tr J3^2 mod 2 ==")
witten = {1: False}
for N in (2, 3, 4, 5, 6, 7):
    gens = table[N]['gens']; idx = []
    for ok, J3 in su2_factors(gens, [0, 1, 2, 3]):
        idx.append(round(witten_index(J3)) if ok else None)
    J3v = gens[(0, 1)]  # SO(3) on Majoranas 0,1,2 (vector-type SU(2))
    idx.append(round(witten_index(J3v)))
    odd = any(i % 2 for i in idx if i is not None); witten[N] = odd
    check(f"E{N} N={N}: Spin(4)_L, Spin(4)_R, Spin(3)_vec indices {idx} -> Witten "
          f"{'ANOMALOUS' if odd else 'even'}" + (' (from cubic)' if N == 3 else ''),
          None not in idx and odd == (N in (2, 3)))

print("== F: centre Z4 and Spin-Z4 (Z16) count, N odd ==")
for N in (1, 3, 5, 7):
    gens, E = table[N]['gens'], table[N]['E']
    X = sum(gens[(2 * j, 2 * j + 1)] for j in range(N))       # n - N/2 inside so(2N)
    z = np.diag(np.exp(1j * np.pi * np.diag(X).real))
    ev = np.round(np.diag(z), 9)
    uniform = np.allclose(ev, ev[0]) and abs(abs(ev[0].imag) - 1) < 1e-9
    nu = abs(int(sum(np.isclose(ev, 1j)) - sum(np.isclose(ev, -1j))))
    check(f"F{N} N={N}: z on S+ = {complex(ev[0]):.0f} x 1_{len(ev)} (z^2 = -1), |nu| = {nu} = {nu % 16} mod 16",
          uniform and np.allclose(z @ z, -np.eye(len(ev))) and nu == 2 ** (N - 1))
E5 = table[5]['E']; sing = [i for i, r in enumerate(E5) if not (r - r[0]).any()]
check("F5b N=5: dropping the SU(5)-singlet state (nu^c) leaves nu = 15 mod 16 != 0",
      len(sing) == 1 and (len(E5) - 1) % 16 == 15)

print("== G: selection table (full Spin(2N) frame group) ==")
z16 = {N: (N % 2 == 0) or (2 ** (N - 1)) % 16 == 0 for N in range(1, 8)}
passing = []
for N in range(1, 8):
    t = table[N]; ok = t['cubic0'] and not witten[N] and z16[N] and t['nsym'] == 0
    passing.append(N) if ok else None
    print(f"  N={N}: chiral={t['chiral']!s:5} pert-free={t['cubic0']!s:5} Witten-free={not witten[N]!s:5} "
          f"Z16-free={z16[N]!s:5} protected={t['nsym'] == 0!s:5} -> {'PASS' if ok else 'fail'}")
check(f"G1 smallest N passing (ii)-(iv) WITHOUT using (i) = {passing[0]}; passing set <= 7: {passing}",
      passing[0] == 5 and passing == [5, 6, 7])
check("G2 chirality (i) is an OUTPUT at the minimum: N=5 is chiral; N=6 (pseudoreal 32) needs (i) to drop",
      table[5]['chiral'] and not table[6]['chiral'])

print("== H: subgroup loophole catalogue, N = 1..4 ==")
q = sp.symbols('q1:4')
f = sp.factor(sum(x ** 3 for x in q) - sum(q) ** 3)
check(f"H1 tori on 4 Weyl (N=3): sum q = 0 => sum q^3 = {f}; anomaly-free => pairs cancel => vectorlike",
      sp.expand(f + 3 * (q[0] + q[1]) * (q[0] + q[2]) * (q[1] + q[2])) == 0)
r1 = sp.solve(q[0] ** 3, q[0]); r2 = sp.solve(q[0] + q[1], q[1])
check(f"H2 tori: 1 Weyl q^3=0 -> q={r1} (massable); 2 Weyl q1+q2=0 -> q2={r2} (vectorlike)",
      r1 == [0] and r2 == [-q[0]])
g3 = table[3]['gens']; S = lambda keys: {k: g3[k] for k in keys}
sub = {'Spin(5)=Sp(4) [Maj 0-4]': [k for k in g3 if max(k) <= 4],
       'Spin(3)xSpin(3) [Maj 012|345]': [k for k in g3 if max(k) <= 2 or min(k) >= 3]}
E3 = table[3]['E']
for nm, keys in sub.items():
    G = S(keys); ns, na = bilinears(G, np.zeros_like(E3), True), bilinears(G, np.zeros_like(E3), False)
    print(f"  N=3 {nm}: invariant bilinears sym={ns} antisym={na}")
    if nm.startswith('Spin(5)'):
        w = [round(witten_index(J3)) for ok, J3 in su2_factors(G, [0, 1, 2, 3]) if ok]
        check(f"H3 N=3 Sp(4): pseudoreal (antisym {na}), Witten indices {w} odd -> ANOMALOUS", ns == 0 and na == 1 and all(i % 2 for i in w))
    else:
        check(f"H4 N=3 SO(4)~(2,2): real (sym {ns}) -> mass ALLOWED", ns == 1)
T = np.array([[1.5, 0, 0, 0], [0, .5, 0, 0], [0, 0, -.5, 0], [0, 0, 0, -1.5]])
Jp = np.diag([np.sqrt(3), 2, np.sqrt(3)], 1)
Jx, Jy = (Jp + Jp.T) / 2, (Jp - Jp.T) / 2j
span = np.array([v.ravel() for v in g3.values()]).T
res = [np.linalg.norm(span @ np.linalg.lstsq(span, J.ravel(), rcond=None)[0] - J.ravel()) for J in (Jx, Jy, T)]
inside = np.linalg.matrix_rank(span) == 15 and max(res) < 1e-10
Gp = {('x',): Jx, ('y',): Jy, ('z',): T}
ns, na = bilinears(Gp, np.zeros((4, 1), int), True), bilinears(Gp, np.zeros((4, 1), int), False)
check(f"H5 N=3 principal SU(2) (j=3/2) inside su(4): Witten index {round(witten_index(T))} even, "
      f"bilinears sym={ns} antisym={na}: protected, old-anomaly-free -> LOOPHOLE unless WWW new anomaly (cited)",
      inside and round(witten_index(T)) == 10 and (ns, na) == (0, 1))
check("H6 N=4: S+ = 8s real; every subgroup keeps the symmetric invariant -> mass allowed for all G",
      table[4]['nsym'] == 1)

print("== Z: zoom diagnostic (odd O_h clusters of one-mode sites) ==")
ops = [np.array(p) * np.array(s) for p in itertools.permutations(range(3)) for s in itertools.product((1, -1), repeat=3)]
mats = [np.diag(s)[list(p)] for p in itertools.permutations(range(3)) for s in itertools.product((1, -1), repeat=3)]
orb = {}
for centre in [(0, 0, 0), (.5, .5, .5), (.5, .5, 0), (.5, 0, 0)]:
    pts = {tuple(np.array(v) - centre) for v in itertools.product(range(-3, 4), repeat=3)
           if sum((np.array(v) - centre) ** 2) <= 6}
    sizes = sorted({len({tuple(m @ np.array(p)) for m in mats}) for p in pts})
    orb[centre] = sizes
odd_ok = all(s % 2 == 0 for c, ss in orb.items() if c != (0, 0, 0) for s in ss) and \
    sorted(s for s in orb[(0, 0, 0)] if s % 2) == [1]
check(f"Z1 O_h orbit sizes: site-centred {orb[(0, 0, 0)]}, other centres all even -> odd clusters = 1 + even;"
      f" 5 unreachable, smallest odd >= 5 is 7 (site + 6 neighbours)", odd_ok and min(s for s in orb[(0, 0, 0)] if s > 1) == 6)
E7 = table[7]['E']; a = (E7[:, :5] > 0).sum(1) % 2
check("Z2 N=7 under Spin(10)xSpin(4): 64 = (16,(2,1)) + (16bar,(1,2)) [vectorlike under Spin(10)]",
      sum(a == 0) == 32 and sum(a == 1) == 32)

print("== W: owner test - five modes from a cluster of one-mode sites ==")
OH = np.array(mats)                                    # 48 signed permutations
box = np.array(list(itertools.product((-1, 0, 1), repeat=3)))
others = [p for p in box if p.any()]


def norm_codes(P):                                     # P (M,k,3) -> translation-normalised sorted codes
    c = (P[..., 0] + 9) * 361 + (P[..., 1] + 9) * 19 + (P[..., 2] + 9)
    m = np.argmin(c, axis=1)
    Q = P - P[np.arange(len(P)), m][:, None, :]
    c = (Q[..., 0] + 9) * 361 + (Q[..., 1] + 9) * 19 + (Q[..., 2] + 9)
    return np.sort(c, axis=1)


def cluster_stab(P):                                   # (M,48) bool: g C is a translate of C
    base = norm_codes(P)
    return np.stack([(norm_codes(P @ g.T) == base).all(1) for g in OH], 1)


def tilings(P, p):                                     # index-p lattices ker(a mod p) tiled by C
    reps = [a for a in itertools.product(range(p), repeat=3) if any(a) and a[next(i for i in range(3) if a[i])] == 1]
    out = []
    for a in reps:
        r = np.sort((P @ np.array(a)) % p, axis=1)
        ok = (r == np.arange(p)).all(1)
        av = np.array(a)
        lat = np.array([any(((g.T @ av - l * av) % p == 0).all() for l in range(1, p)) for g in OH])
        out.append((a, ok, lat))
    return out


P5 = np.array([[np.zeros(3, int), *c] for c in itertools.combinations(others, 4)])
st5 = cluster_stab(P5); so5 = st5.sum(1)
best_tile, best_desc = 0, None
for a, ok, lat in tilings(P5, 5):
    if ok.any():
        sym = (st5[ok] & lat[None, :]).sum(1)
        k = int(np.argmax(sym))
        if sym[k] > best_tile:
            best_tile, best_desc = int(sym[k]), (a, P5[ok][k].tolist())
check(f"W1 5-clusters in a 3^3 box ({len(P5)}): largest cluster stabiliser {so5.max()}/48 (site + 4 body"
      f" diagonals = one tetrahedron, T_d), so none is O_h-covariant (Z1)", so5.max() == 24)
named = {'tetrahedral (site+4 alt. diagonals)': [[0, 0, 0], [1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]],
         'site+3 forward+diagonal': [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]],
         'site+4 in-plane (plus)': [[0, 0, 0], [1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0]],
         'cube 5 of 8 (complement = 3 around a corner)': [[1, 1, 1], [0, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1]]}
for nm, c in named.items():
    Pc = np.array([c]); s = cluster_stab(Pc)[0]
    t = [(a, int((s & lat).sum())) for a, ok, lat in tilings(Pc, 5) if ok[0]]
    tmax = max([x[1] for x in t], default=0)
    print(f"  {nm}: cluster stab {s.sum()}/48, tiles Z^3 by {len(t)} index-5 lattices, best tiling stab {tmax}/48")
check(f"W2 best covariance of ANY 5-site tiling = {best_tile}/48 point operations "
      f"(lopsided by {np.log2(48 / best_tile):.1f} bits)", best_tile < 48)
star = np.array([[[0, 0, 0], [1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]])
tst = [int(lat.sum()) for a, ok, lat in tilings(star, 7) if ok[0]]
check(f"W3 the 7-star (stab 48) tiles Z^3 ({len(tst)} perfect-code lattices) but the tiling keeps "
      f"at most {max(tst)}/48", cluster_stab(star)[0].sum() == 48 and max(tst) < 48)


def hnf_lattices(n):
    for a in range(1, n + 1):
        for d in range(1, n // a + 1):
            if n % (a * d):
                continue
            f = n // (a * d)
            for b, c, e in itertools.product(range(a), range(a), range(d)):
                yield np.array([[a, 0, 0], [b, d, 0], [c, e, f]])


def reduce(H, w):
    w = np.array(w, int).copy()
    for i in (2, 1, 0):
        w = w - (w[..., i] // H[i, i])[..., None] * H[i]
    return w


cov = []
for n in range(2, 31):
    for H in hnf_lattices(n):
        if not all((reduce(H, H @ g.T) == 0).all() for g in OH):
            continue
        for ctr in (np.zeros(3), np.full(3, .5)):
            pts = [np.array(v) for v in itertools.product(range(-3, 5), repeat=3) if sum((np.array(v) - ctr) ** 2) <= 9]
            orbs, seen = [], set()
            for v in pts:
                if tuple(v) in seen:
                    continue
                o = {tuple(np.rint(g @ (v - ctr) + ctr).astype(int)) for g in OH}
                seen |= o; orbs.append(sorted(o))
            for m in range(1, len(orbs) + 1):
                for sub in itertools.combinations(orbs, m):
                    if sum(map(len, sub)) != n:
                        continue
                    R = reduce(H, np.array([p for o in sub for p in o]))
                    if len({tuple(r) for r in R}) == n:
                        cov.append(n)
cov = sorted(set(cov))
check(f"W4 fully O_h-covariant tiling blocks of size <= 30: {cov}; odd: 27 = 3^3 only; "
      "8, 16 fail (N = 0 mod 4: real), so smallest covariant PASSING block = 27", cov == [8, 16, 27])
gv = [np.zeros((10, 10)) for _ in range(45)]
for t, (a, b) in enumerate(itertools.combinations(range(10), 2)):
    gv[t][a, b], gv[t][b, a] = 1, -1
K = np.array([np.kron(np.eye(10), A) - np.kron(A.T, np.eye(10)) for A in gv]).reshape(-1, 100)
dimK = int(sum(np.linalg.svd(K, compute_uv=False) < 1e-9))
check(f"W5 Spin(10)-invariant couplings between two clusters' Majorana 10-vectors: dim {dimK} (identity only)"
      " -> mode-diagonal hops along l in L; NN on 3 axes => L = Z^3 => N = 1", dimK == 1)
nbr = lambda x: {tuple(np.array(x) + s * e) for e in np.eye(3, dtype=int) for s in (1, -1)}
cn = max(len(nbr((0, 0, 0)) & nbr(tuple(v))) for v in box if np.array(v).any())
check(f"W6 two distinct sites share <= {cn} neighbours, so no K(5,5) of NN bonds: a gauge-covariant"
      " NN inter-cluster hop cannot exist either", cn == 2)
g5f = majoranas(5); ev = np.array([bin(s).count('1') % 2 == 0 for s in range(32)])
Gp = {k: (0.5j * g5f[k[0]] @ g5f[k[1]])[np.ix_(ev, ev)] for k in itertools.combinations(range(10), 2)}
Gm = {k: (0.5j * g5f[k[0]] @ g5f[k[1]])[np.ix_(~ev, ~ev)] for k in itertools.combinations(range(10), 2)}
Mx = np.array([np.kron(Gp[k].T, np.eye(16)) + np.kron(np.eye(16), Gm[k].T) for k in Gp]).reshape(-1, 256)
dpm = int(sum(np.linalg.svd(Mx, compute_uv=False) < 1e-9))
check(f"W7 inter-cluster pairing S+ x S+: 0 invariants (D5); S+ x S-: {dpm} -> protection needs the SAME parity half"
      " on every cluster, else a Dirac mass", dpm == 1 and table[5]['nsym'] == 0)

print("VERDICT: full Spin(2N) on S+: smallest anomaly-free protected N = 5 (chirality is an output);")
print("  loopholes: j=3/2 SU(2) at N=3 (cited WWW), finite groups at N=1,2. Clusters of one-mode sites:")
print("  no covariant 5-tiling, no NN dynamics with exact Spin(10); 5 = per-site multiplicity (bends Qubit).")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
