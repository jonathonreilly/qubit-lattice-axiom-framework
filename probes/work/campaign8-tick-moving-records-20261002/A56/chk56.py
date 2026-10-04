"""A56 chk56: (1) term-set checks for the 24-site blocks (independent pair enumeration; four-sets = restriction of the
10^3-torus operator to the block); (2) table kernel vs A53's _matvec_gen; (3) EXACT 8- and 16-site energies (cube,
2x2x4 [A53 check], edge pair, corner pair, gapped pair) and start-vector spin checks; (4) 24-site matvec timing.
Usage: chk56.py KEY"""
import sys, signal, time, numpy as np, scipy.sparse.linalg as sla
signal.alarm(280)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a56lib import *
t0 = time.time(); key = sys.argv[1]; L = 6
ks, J, c4 = load_rule(L, key)
Jcls = {tuple(sorted(k)): j for k, j in zip(ks, J) if abs(j) > 1e-14}
cl = cube(10); XT = [np.array(s) for s in cl.sites]; fT = periodic_index(cl); FT = four_sets(XT, fT, c4)
for name in ['line3', 'L3', 'line2', 'edge2']:
    X, cid, pairs, fours = block_terms(name, L, key); n = len(X)
    exp = {}
    for i in range(n):
        for j in range(i + 1, n):
            c = tuple(sorted(abs(int(v)) for v in X[i] - X[j]))
            if c in Jcls: exp[(i, j)] = Jcls[c]
    okp = set(exp) == set(pairs) and max(abs(exp[p] - pairs[p]) for p in exp) == 0.
    tix = {fT(x): i for i, x in enumerate(X)}; restr = {}
    for Sg, w in FT.items():
        if all(s in tix for s in Sg):
            loc = [tix[s] for s in Sg]; o = sorted(range(4), key=lambda q: loc[q]); inv = {o[q]: q for q in range(4)}
            acc = restr.setdefault(tuple(loc[q] for q in o), np.zeros(3))
            for pi, ((u, v), (x, y)) in enumerate(PAIRINGS):
                pr = tuple(sorted(tuple(sorted((inv[a], inv[b]))) for a, b in ((u, v), (x, y))))
                acc[PAIRINGS.index(pr)] += w[pi]
    okf = set(restr) == set(fours) and max(np.abs(restr[q] - fours[q]).max() for q in fours) < 1e-14
    ncub = [len(set(cid[s] for s in Sg)) for Sg in fours]; npc = [len(set((cid[i], cid[j]))) for (i, j) in pairs]
    print(f"{name}: n={n} pairs {len(pairs)} (inter-cube {npc.count(2)}; independent enumeration match {okp}); "
          f"four-sets {len(fours)} (spanning 1/2/3 cubes: {ncub.count(1)}/{ncub.count(2)}/{ncub.count(3)}; "
          f"10^3-torus restriction match {okf})", flush=True)
# kernel check + exact small blocks
gsd, wc, sing, Ec = cube_gs(L, key)
print(f"cube: E {Ec:+.10f} (E/N {Ec/8:+.6f}); lowest singlets {[round(wc[q],5) for q in sing[:3]]}; "
      f"lowest levels {np.round(wc[:4],5)}", flush=True)
res = {'cube': Ec}
for name in ['line2', 'edge2', 'corner2', 'far2']:
    X, cid, pairs, fours = block_terms(name, L, key); n = len(X)
    S = Sector(n, flip=True); H = TabHam(pairs, fours, n); mv = make_mv_tab(H, S)
    G = GenHam(pairs, fours, n); mvg = make_mv_gen(G, S)
    r = np.random.default_rng(1).standard_normal(S.D); dk = np.abs(mv(r) - mvg(r)).max()
    op = sla.LinearOperator((S.D, S.D), matvec=mv, dtype=float)
    w, U = sla.eigsh(op, k=6, which='SA', tol=1e-12); o = np.argsort(w); w, U = w[o], U[:, o]
    Ss = [abs(paircorr(U[:, q], S).sum()) for q in range(6)]; q0 = [q for q in range(6) if Ss[q] < 1e-6][0]
    res[name] = w[q0]
    p0 = cube_product(S, 2, gsd); rs = random_singlet(S)
    print(f"{name}: kernel |tab - gen| {dk:.1e}; S=0 GS E {w[q0]:+.10f} (E/N {w[q0]/n:+.6f}; state {q0} of the "
          f"flip-even sector, sum<s.s> {Ss[q0]:.1e}); Delta = E - 2 E_cube {w[q0]-2*Ec:+.6f}; "
          f"<prod|H|prod> - 2E_cube {p0@mv(p0)-2*Ec:+.1e}; start S-checks sum<s.s>: prod {paircorr(p0,S).sum():.1e} "
          f"rand-singlet {paircorr(rs,S).sum():.1e}  [{time.time()-t0:.0f}s]", flush=True)
for name in ['line3', 'L3']:
    X, cid, pairs, fours = block_terms(name, L, key); n = len(X)
    S = Sector(n, flip=True); H = TabHam(pairs, fours, n); mv = make_mv_tab(H, S)
    r = np.random.default_rng(2).standard_normal(S.D); mv(r[:]); t1 = time.time(); y1 = mv(r); tt = time.time() - t1
    msg = ""
    if name == 'line3':
        G = GenHam(pairs, fours, n); mvg = make_mv_gen(G, S); mvg(r); t1 = time.time(); y2 = mvg(r); tg = time.time() - t1
        msg = f"; |tab - gen| {np.abs(y1-y2).max():.1e} (gen kernel {tg:.1f}s)"
    p0 = cube_product(S, 3, gsd)
    print(f"{name}: D={S.D}; tab matvec {tt:.2f}s{msg}; <prod|H|prod> - 3E_cube {p0@mv(p0)-3*Ec:+.1e}  [{time.time()-t0:.0f}s]", flush=True)
print("RESULT " + " ".join(f"{k}={v:+.10f}" for k, v in res.items()))
