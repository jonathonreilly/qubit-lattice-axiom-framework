"""A49 fwd16: forward test of candidate rules H(c) on the 16-site cluster, for rules in the dual-SU(2)-invariant
subspace (Klein duals of SU(2)-invariant rules).  In the dual frame such a rule is
   H = sum_p w_p (s_i.s_j) + sum_{four-sets, pairings} w (s_u.s_v)(s_x.s_y),   s.s = 2 P - 1  (P = exchange),
so it acts inside the dual S^z = 0 sector (12870 states) by permutation gathers.  Both signs of c are tested.
Reports: lowest levels per site, the parton energy, variance and its overlap with the ground space / lowest levels,
and the weakly ordered references' energies.  Usage: fwd16.py rules.npz"""
import sys, signal, time, itertools, numpy as np, scipy.sparse.linalg as sla
signal.alarm(288)
sys.path.insert(0, __file__.rsplit("/", 2)[0] + "/A49")
from a49lib import *
t0 = time.time()
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]); N = cl.N
ops = [(nm, cls, "b", op) for nm, cls, op in bilinear_basis()] + [(nm, cls, "4", d4) for nm, cls, d4, sold in four_basis()]
T = Tables(cl, ops); n = len(T.names)
confs = np.array([sum(1 << i for i in c) for c in itertools.combinations(range(N), N // 2)], dtype=np.int64)  # set bits = down
pos = -np.ones(2 ** N, dtype=np.int64); pos[confs] = np.arange(len(confs)); D = len(confs)
perm = {}
for i in range(N):
    for j in range(i + 1, N):
        bi = (confs >> i) & 1; bj = (confs >> j) & 1
        perm[(i, j)] = pos[np.where(bi != bj, confs ^ ((1 << i) | (1 << j)), confs)]
P = lambda i, j: perm[(min(i, j), max(i, j))]
bits = bits_table(N)
def vec(Phi):
    p = projected_vector(Phi, bits)[confs]; return p / np.linalg.norm(p)
states = {"parton": vec(mf_state(cl)[0]), "neel_z_0.05": vec(mf_state(cl, m=0.05)[0]),
          "col_z_0.1": vec(mf_state(cl, m=0.1, pattern="collinear")[0])}
print(f"S^z=0 sector {D}; norms kept in sector: parton {np.linalg.norm(projected_vector(mf_state(cl)[0], bits)[confs])/np.linalg.norm(projected_vector(mf_state(cl)[0], bits)):.6f}  [{time.time()-t0:.0f}s]", flush=True)

def build(c):
    w1 = np.einsum('k,kcp->cp', c, T.W1); w2 = np.einsum('k,kmp->mp', c, T.W2)
    assert np.abs(w1).max() < 1e-10 and np.abs(w2).max() < 1e-10, "rule not dual-SU(2)-invariant"
    w0 = c @ T.W0; w4 = np.einsum('k,kqp->qp', c, T.W4)
    terms2 = [(P(int(T.pi[p]), int(T.pj[p])), w0[p]) for p in range(T.np_) if abs(w0[p]) > 1e-14]
    terms4 = []
    for q in range(T.ns):
        S = T.sets[q]
        for pi in range(3):
            if abs(w4[q, pi]) < 1e-14: continue
            (u, v), (x, y) = PAIRINGS[pi]; a = P(int(S[u]), int(S[v])); b = P(int(S[x]), int(S[y]))
            terms4.append((a, b, a[b], w4[q, pi]))
    const = -sum(w for _, w in terms2) + sum(w for *_, w in terms4)
    def mv(x):
        x = np.asarray(x).ravel(); out = const * x
        for pm, w in terms2: out = out + 2 * w * x[pm]
        for a, b, ab, w in terms4: out = out + w * (4 * x[ab] - 2 * x[a] - 2 * x[b])
        return out
    return mv

rules = np.load(sys.argv[1])
for lab in [l for l in rules.files if l.endswith("inv")]:
    c0 = rules[lab]
    for sgn in (+1, -1):
        mv = build(sgn * c0)
        op = sla.LinearOperator((D, D), matvec=mv, dtype=complex)
        vals, vecs = sla.eigsh(op, k=5, which='SA', tol=1e-9); o = np.argsort(vals); vals, vecs = vals[o] / N, vecs[:, o]
        deg = int(np.sum(vals - vals[0] < 1e-7))
        line = f"{lab} sign {sgn:+d}: E0/N {vals[0]:+.5f} (deg {deg}); next levels/N " + " ".join(f"{v:+.5f}" for v in vals[1:5])
        for nm, p in states.items():
            Hp = mv(p); E = np.vdot(p, Hp).real / N; var = (np.vdot(Hp, Hp).real - (E * N) ** 2) / N
            ov = float(np.sum(np.abs(vecs[:, :deg].conj().T @ p) ** 2)); ovs = np.abs(vecs.conj().T @ p) ** 2
            line += f"\n     {nm:12s}: <H>/N {E:+.5f}  var/N {var:.4g}  overlap(ground space) {ov:.4f}  overlaps(lowest 5) " + " ".join(f"{x:.3f}" for x in ovs)
        print(line + f"   [{time.time()-t0:.0f}s]", flush=True)
