"""A53 t1_16: 16-site exact ground state anatomy under A51's |d|^2 <= 4 rules (B4_r4 from 6^3 and 8^3), wrapped as in
A49/A51 fwd16.  Cross-checks: star kernel vs generic kernel, flip-reduced vs full S^z = 0 sector, A51 fwd16 numbers.
Reports: E0, GS spin, energy decomposition, <s.s> by wrapped class, four-spin expectations, singlet weights of
pairs / plaquettes / cubes, parton for comparison.  Usage: t1_16.py"""
import sys, signal, time, numpy as np, scipy.sparse.linalg as sla
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
t0 = time.time()
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]); N = cl.N; X = [np.array(s) for s in cl.sites]; f = periodic_index(cl)
Sf = Sector(N, flip=False); Sr = Sector(N, flip=True)
print(f"16-site: sectors {Sf.D} (S^z=0) / {Sr.D} (flip-even)  [{time.time()-t0:.1f}s]", flush=True)
# wrapped displacement structure: for each pair, the list of displacement vectors |d|^2 <= 4 connecting it
disp = [d for k in [(0, 0, 1), (0, 1, 1), (1, 1, 1), (0, 0, 2)] for d in class_vectors(k)]
mult = {}
for i in range(N):
    for d in disp:
        j = f(X[i] + np.array(d)); key = (min(i, j), max(i, j))
        mult.setdefault(key, []).append(tuple(sorted(np.abs(d))))
def ptype(i, j):
    v = mult.get((min(i, j), max(i, j)))
    if v is None: return "far"
    ks = sorted(set(v)); return "+".join(f"{k[0]}{k[1]}{k[2]}x{v.count(k)}" for k in ks)
types = {}
for i in range(N):
    for j in range(i + 1, N):
        types.setdefault(ptype(i, j), []).append((i, j))
print("pair types (class x multiplicity of the wrapped operator): " + ", ".join(f"{t}:{len(v)}" for t, v in sorted(types.items())))
cubes = [[f(X[a] + np.array(o)) for o in itertools.product((0, 1), repeat=3)] for a in range(N)]
plaqs = []
for a in range(N):
    for (p, q) in ((0, 1), (0, 2), (1, 2)):
        e = np.eye(3, dtype=int); plaqs.append([f(X[a]), f(X[a] + e[p]), f(X[a] + e[p] + e[q]), f(X[a] + e[q])])
P8 = spin_projectors(8); P4 = spin_projectors(4)
Phi, gap = mf_state(cl); psi_p = parton_vector(cl, Sf, Phi)
print(f"parton: MF gap {gap:.4f}; max |Im| {np.abs(psi_p.imag).max():.1e}", flush=True)
psi_p = psi_p.real / np.linalg.norm(psi_p.real)
# flip parity of the parton
rk = Sf.offset[((~Sf.confs) & Sf.full) >> Sf.h] + Sf.idxlo[((~Sf.confs) & Sf.full) & Sf.lomask]
print(f"parton flip parity: max |psi(~c) - psi(c)| = {np.abs(psi_p[rk] - psi_p).max():.1e}")
rk_r = Sf.offset[Sr.confs >> Sf.h] + Sf.idxlo[Sr.confs & Sf.lomask]       # positions of flip reps in full sector

def analyse(lab, x, S, mv, H, ks, J, c4):
    x = x / np.linalg.norm(x); E = x @ mv(x) / N
    C = paircorr(x, S); spin = C.sum() / 4.
    out = f"  [{lab}] <H>/N {E:+.5f}; 4S(S+1)/4 = {spin:.2e}\n   <s.s> by pair type: " + \
        " ".join(f"{t}:{np.mean([C[i, j] for i, j in v]):+.3f}" for t, v in sorted(types.items()))
    v = full_vector(x, S)
    cw = [np.trace(rdm(v, N, cb) @ P8[0.0]) for cb in cubes]; pw = [np.trace(rdm(v, N, pq) @ P4[0.0]) for pq in plaqs]
    out += f"\n   singlet weight: cubes mean {np.mean(cw):.3f} (min {np.min(cw):.3f}, max {np.max(cw):.3f}; random 14/256 = 0.055)" + \
           f"; plaquettes mean {np.mean(pw):.3f} (min {np.min(pw):.3f} max {np.max(pw):.3f}; random 0.125)"
    # energy decomposition: bilinear classes and each four-spin op
    parts = []
    for kc, Jc in zip(ks, J):
        if abs(Jc) < 1e-12: continue
        Hc = Ham(X, f, [kc], [1.], np.zeros(8)); e = x @ make_mv(Hc, S)(x) / N; parts.append(f"{kc}:{Jc:+.3f}*{e:+.3f}")
    for k in range(8):
        if abs(c4[k]) < 1e-12: continue
        Hk = Ham(X, f, [], [], np.eye(8)[k]); e = x @ make_mv(Hk, S)(x) / N; parts.append(f"{F4N[k]}:{c4[k]:+.3f}*{e:+.3f}")
    return out + "\n   decomposition (coef * <op>/N): " + " ".join(parts)

for L in (6, 8):
    ks, J, c4 = load_rule(L, "B4_r4")
    Hs = Ham(X, f, ks, J, c4); Hg = GenHam(bilinear_pairs(X, f, ks, J), four_sets(X, f, c4), N)
    res = {}
    for nm, H, S, mk in (("star/full", Hs, Sf, make_mv), ("gen/full", Hg, Sf, make_mv_gen), ("star/flip", Hs, Sr, make_mv), ("gen/flip", Hg, Sr, make_mv_gen)):
        mv = mk(H, S); op = sla.LinearOperator((S.D, S.D), matvec=mv, dtype=float)
        vals, vecs = sla.eigsh(op, k=4, which='SA', tol=1e-11); o = np.argsort(vals); res[nm] = (vals[o] / N, vecs[:, o[0]], mv, S)
    print(f"\nL{L} B4_r4 rule: {len(Hs.pairs)} pairs, {len(Hg.fours)} four-sets, star tables {len(Hs.fsl)} local sets [{time.time()-t0:.1f}s]")
    for nm, (vals, *_ ) in res.items():
        print(f"  {nm:10s} lowest/N: " + " ".join(f"{v:+.6f}" for v in vals))
    vals, x, mv, S = res["star/full"]
    xr = x[rk_r]; print(f"  GS flip-even weight: {2 * np.sum(xr**2):.6f}")
    ep = psi_p @ mv(psi_p) / N; vp = (np.linalg.norm(mv(psi_p)) ** 2 / N ** 2 - ep ** 2) * N
    ov = (x @ psi_p) ** 2
    print(f"  parton <H>/N {ep:+.5f} (A51 fwd16: {'-1.77524' if L == 6 else '-1.76626'}); var/N {vp:.4f}; |<GS|parton>|^2 {ov:.2e}; gap to GS {ep - vals[0]:+.4f}/site")
    print(analyse("GS", x, S, mv, Hs, ks, J, c4))
    print(analyse("parton", psi_p, S, mv, Hs, ks, J, c4), flush=True)
    np.save(f"gs16_L{L}.npy", x)
print(f"done [{time.time()-t0:.1f}s]")
