AUDIT_INPUT_PATHS = ('docs/EDGE_REGISTERS_ADVANCE_ONCE_PER_BLOCK_HALF_TICK_AND_THE_CUBE_TICK_HAS_A_LOCAL_QUASI_ENERGY_DENSITY_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""cadence-quasienergy probe (TOE-ruleset campaign, 2026-10-22).

Supplied finite toys for two flags of the compact laws:
 (A) edge cadence: block registers advance once per block half-tick;
 (B) per-cube quasi-energy: a local density of the tick's Floquet generator.
Labels: [T] theorem-level identity checked numerically, [D] finite diagnostic,
[E] estimate against measurement (supplied inputs named in the line).
Self-contained: numpy + scipy only.
"""
AUDIT_TIMEOUT_SEC = 120
import time, math
import numpy as np
from scipy.linalg import expm, schur, eigh
import scipy.sparse as sp

t0 = time.time()
NP = [0, 0]
def report(ok, tag, msg):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] [{tag}] {msg}")

sx = np.array([[0, 1], [1, 0]], complex); sz = np.diag([1., -1]).astype(complex); I2 = np.eye(2)
eps0 = 0.1          # toy step (the register's eps0 is 0.0075-0.0375; toys use a larger step to see effects)

# ---------------------------------------------------------------- A1 block lapse
print("== A. edge cadence")
rng = np.random.default_rng(7)
worst = 0.0
for be in range(2, 13):
    for _ in range(20):
        Mx = rng.normal(size=(3, 3)); g_inv = Mx @ Mx.T + 0.3 * np.eye(3)   # cube-rung gamma^ij
        Nc = math.sin(eps0) / (math.sqrt(3) * math.sqrt(np.mean(np.diag(g_inv))))
        gB = g_inv / be**2                                                 # same edges, block-rung units
        NB = math.sin(eps0) / (math.sqrt(3) * math.sqrt(np.mean(np.diag(gB))))
        worst = max(worst, abs(NB / (be * Nc) - 1))
report(worst < 1e-13, "T", f"A1 lapse rule read at the block rung gives N_B = b_e N for every metric (b_e 2..12, max rel err {worst:.1e}): "
       "one block half-tick has the proper time of b_e cube half-ticks, the same fraction sin(eps0) of the block's light crossing")

# ---------------------------------------------------------------- 2D toy walk
Wx = np.kron(sx, I2); Wy = np.kron(sz, sx)            # anticommuting plaquette hops (supplied 2D phases)
idx = [(0, 0), (0, 1), (1, 0), (1, 1)]
def R4(wx, wy): return (wx * Wx + wy * Wy) / math.hypot(wx, wy)
def bloch2d(k, wx, wy, eps, mu):
    R = R4(wx, wy); Ue = expm(-1j * (eps - mu / 2) * R)
    P = np.zeros((4, 4), complex)
    for j, (dx, dy) in enumerate(idx):
        sub = ((1 + dx) % 2, (1 + dy) % 2); sh = ((1 + dx) // 2, (1 + dy) // 2)
        P[idx.index(sub), j] = np.exp(1j * (k[0] * sh[0] + k[1] * sh[1]))
    return P @ expm(1j * (eps + mu / 2) * R) @ P.conj().T @ Ue
def real2d(L, wx, wy, eps, mu):
    R = R4(wx, wy); ue = expm(-1j * (eps - mu / 2) * R); uo = expm(1j * (eps + mu / 2) * R)
    Ue = np.zeros((L * L, L * L), complex); Uo = np.zeros_like(Ue)
    for U, u, off in ((Ue, ue, 0), (Uo, uo, 1)):
        for i in range(0, L, 2):
            for j in range(0, L, 2):
                s = [((i + off + dx) % L) * L + (j + off + dy) % L for dx, dy in idx]
                U[np.ix_(s, s)] = u
    return Ue, Uo

d = 5; lx = [2 ** ((n - 2) / 2) for n in range(d)]; ly = 1.0      # one block register sets l_x (supplied s = 2)
def lapse2d(wx, wy): return math.sin(eps0) / (math.sqrt(2) * math.sqrt((wx**2 + wy**2) / 2))
mass = 0.3
L = 8
V = np.diag(np.ones(d - 1), -1)                                    # raise, normalised on its domain
UE = expm(-1j * (0.3 * (V + V.T) + np.diag(0.05 * np.arange(d))))  # edge hop + a supplied edge phase
for be in (3, 4):
    fine = []
    for par in (0, 1):
        blocks = []
        for n in range(d):
            wx, wy = 1 / lx[n], 1 / ly; mu = mass * lapse2d(wx, wy)
            Ue, Uo = real2d(L, wx, wy, eps0, mu); blocks.append((Ue, Uo)[par])
        Pn = [np.diag(np.eye(d)[n]) for n in range(d)]
        fine.append(sum(np.kron(Pn[n], blocks[n]) for n in range(d)))
    Ublk = np.eye(d * L * L, dtype=complex)
    for h in range(be): Ublk = fine[h % 2] @ Ublk
    Ublk = np.kron(UE, np.eye(L * L)) @ Ublk
    un = np.abs(Ublk.conj().T @ Ublk - np.eye(d * L * L)).max()
    comm = max(np.abs(f @ np.kron(Pn[m], np.eye(L * L)) - np.kron(Pn[m], np.eye(L * L)) @ f).max() for f in fine for m in range(d))
    psi = rng.normal(size=d * L * L) + 1j * rng.normal(size=d * L * L); psi /= np.linalg.norm(psi)
    pe = lambda v: (np.abs(v.reshape(d, L * L))**2).sum(1)
    phi = psi.copy()
    for h in range(be): phi = fine[h % 2] @ phi
    dfine = np.abs(pe(phi) - pe(psi)).max(); dE = np.abs(pe(np.kron(UE, np.eye(L * L)) @ phi) - pe(phi)).max()
    report(un < 1e-12 and comm < 1e-13 and dfine < 1e-13 and dE > 1e-3, "T",
           f"A2 b_e={be}: block half-tick (b_e cube half-ticks controlled on the held register, then the edge unitary) is unitary "
           f"(err {un:.0e}); cube layers commute with every register projector (err {comm:.0e}), so register odds are unchanged "
           f"between edge updates (max {dfine:.0e}) and change only at them ({dE:.2f})")

# A3 effective metric: proper dispersion collapses over register values and axes
k0 = np.array([0.0, math.pi]); dk = 0.004; spd = []; rest = []; coll = []
Ks = np.array([0.0, 0.01, 0.02, 0.04])
for n in range(d):
    wx, wy = 1 / lx[n], 1 / ly; N = lapse2d(wx, wy)
    for dirv in ((1, 0), (0, 1), (1 / math.sqrt(2), 1 / math.sqrt(2))):
        K = dk; kk = (K * dirv[0] / wx, K * dirv[1] / wy)                   # proper K -> cell k_i = K_i l_i
        om = np.min(np.abs(np.angle(np.linalg.eigvals(bloch2d(k0 + kk, wx, wy, eps0, 0)))))
        spd.append(om / N / K)
    mu = mass * N
    row = []
    for K in Ks:
        kk = (K / wx, 0.0)
        om = np.min(np.abs(np.angle(np.linalg.eigvals(bloch2d(k0 + kk, wx, wy, eps0, mu)))))
        row.append(om / N)
    rest.append(row[0]); coll.append(row)
spd = np.array(spd); coll = np.array(coll)
csp = np.ptp(spd) / spd.mean(); cm = np.ptp(np.array(rest)) / np.mean(rest)
c0 = spd.mean(); pred = np.sqrt(np.array(rest).mean()**2 + (c0 * Ks)**2)
dcol = np.abs(coll / pred - 1).max()
report(csp < 2e-3 and cm < 2e-3 and dcol < 5e-3, "T",
       f"A3 2D toy: for register lengths l_x = 0.5..2 (l_y = 1) the proper cone speed is the same on x, y and the diagonal "
       f"(spread {csp:.1e}) and the proper rest energy is m (spread {cm:.1e}); Omega(K) = sqrt(m^2 + c^2 K^2) to {dcol:.1e}: "
       "matter's effective metric is diag(-N^2, l_x^2, l_y^2), the block's")

# A4 kickback: the controlled cube tick already applies the matter phase to the register
Lc = 8; Ns = 2 * Lc; lE = [2 ** ((n - 2) / 4) for n in range(d)]
def real1d(eps, mu):
    ue = expm(-1j * (eps - mu / 2) * sx); uo = expm(1j * (eps + mu / 2) * sx)
    Ue = np.zeros((Ns, Ns), complex); Uo = np.zeros_like(Ue)
    for j in range(Lc):
        a, b = 2 * j, 2 * j + 1; Ue[np.ix_([a, b], [a, b])] = ue
        a, b = 2 * j + 1, (2 * j + 2) % Ns; Uo[np.ix_([a, b], [a, b])] = uo
    return Uo @ Ue
mt = 0.4
Uc = sum(np.kron(np.diag(np.eye(d)[n]), real1d(eps0, mt * lE[n] * math.sin(eps0))) for n in range(d))
plus = np.ones(Ns) / math.sqrt(Ns)                     # k = 0 state, sublattice-symmetric (eigenvector of every branch)
edge = np.ones(d) / math.sqrt(d); st = np.kron(edge, plus); T = 37
for _ in range(T): st = Uc @ st
amp = st.reshape(d, Ns) @ plus.conj()
ph = -np.angle(amp / amp[0]); want = np.array([mt * lE[n] * math.sin(eps0) for n in range(d)])
want = -(want - want[0]) * T
errk = np.abs(np.angle(np.exp(1j * (ph - want)))).max()
report(errk < 1e-10, "T",
       f"A4 kickback: T = {T} ticks of the edge-controlled cube tick give the register branch n the phase T m N_n (err {errk:.0e}), "
       "the rest-phase part of the total phase; an edge tick that also applies the matter phase counts it twice")
# vacuum share in the kickback
def bands1d(mu, eps):
    ks = 2 * np.pi * np.arange(400) / 400; e = []
    for k in ks:
        Ue = expm(-1j * (eps - mu / 2) * sx); B = np.array([[0, 1], [np.exp(1j * k), 0]])
        Uo = expm(1j * (eps + mu / 2) * np.array([[0, np.exp(-1j * k)], [np.exp(1j * k), 0]]))
        e.append(np.sort(np.angle(np.linalg.eigvals(Uo @ Ue))))
    return np.array(e)
Es = [bands1d(mt * lE[n] * math.sin(eps0), eps0)[:, 0].sum() / 400 for n in (0, d - 1)]
dsea = abs(Es[1] - Es[0]); dpar = abs(want[-1] / T)
report(Lc * dsea > dpar, "D", f"A4b the filled band's kickback changes by {dsea:.1e} per cell per tick across the register range, "
       f"{Lc*dsea:.1e} on the {Lc}-cell chain, vs {dpar:.1e} for one rest particle: it grows with volume, so the vacuum share needs a counter-phase on the edges")

# A5 strict cone of the combined circuit (reachability of influence)
def front(be, nb=41, Tb=12):
    ns = nb * be; site = np.zeros(ns, bool); site[ns // 2] = True
    P = np.zeros(nb, bool); Q = np.zeros(nb, bool); fr = []
    for t in range(Tb):
        for h in range(be):
            off = h % 2
            for a in range(off, ns - 1, 2):
                blk = a // be
                if site[a] or site[a + 1]: P[blk] = True
                if site[a] or site[a + 1] or Q[blk]: site[a] = site[a + 1] = True
        Q = Q | P
        for sub in (0, 1):
            for j in range(sub, nb - 1, 2):
                if Q[j] or Q[j + 1]: Q[j] = Q[j + 1] = True
        x = np.nonzero(site)[0]; fr.append(max(x.max() - ns // 2, ns // 2 - x.min()))
    return (fr[-1] - fr[3]) / ((Tb - 4) * be)
vs = {be: front(be) for be in (4, 8)}
def om1(k, eps, mu):
    Ue = expm(-1j * (eps - mu / 2) * sx)
    Uo = expm(1j * (eps + mu / 2) * np.array([[0, np.exp(-1j * k)], [np.exp(1j * k), 0]]))
    return np.max(np.angle(np.linalg.eigvals(Uo @ Ue)))
vd = om1(0.004, eps0, 0) / 0.004    # cells per tick = sites per half-tick (2 sites per cell)
report(all(1 < v < 4 for v in vs.values()), "D",
       f"A5 strict cone of matter + held registers + brickwork edge hops: {vs[4]:.2f} (b_e 4), {vs[8]:.2f} (b_e 8) sites per cube "
       f"half-tick, finite and b_e-independent; the dressed cone (~{vd:.3f} sites per half-tick at eps {eps0}) lies inside: causal")

# ---------------------------------------------------------------- B. quasi-energy density
print("== B. per-cube quasi-energy")
def fermions(L):
    a = sp.csr_matrix(np.array([[0, 1], [0, 0]], complex)); Z = sp.csr_matrix(sz); I = sp.identity(2, format="csr")
    cs = []
    for j in range(L):
        ops = [Z] * j + [a] + [I] * (L - j - 1); m = ops[0]
        for o in ops[1:]: m = sp.kron(m, o, format="csr")
        cs.append(m)
    return cs
def chain(L, Nf, eps, mu, Vint):
    cs = fermions(L); dim = 2**L
    nocc = np.array([bin(i).count("1") for i in range(dim)])
    keep = np.arange(dim) if Nf is None else np.nonzero(nocc == Nf)[0]
    def red(m): return m.toarray()[np.ix_(keep, keep)]
    terms = []
    for b in range(L - 1):
        hop = cs[b].getH() @ cs[b + 1]; hop = hop + hop.getH()
        nb_ = cs[b].getH() @ cs[b]; nc_ = cs[b + 1].getH() @ cs[b + 1]; Id = sp.identity(dim, format="csr")
        inter = (nb_ - 0.5 * Id) @ (nc_ - 0.5 * Id)
        if b % 2 == 0: a_c = (eps - mu / 2) * hop + eps * Vint * inter
        else:          a_c = -(eps + mu / 2) * hop + eps * Vint * inter
        terms.append(red(a_c))
    nops = [red(c.getH() @ c) for c in cs]
    return terms, nops
def floquet(terms):
    Ae = sum(terms[0::2]); Ao = sum(terms[1::2])
    w, v = eigh(Ae); Ue = (v * np.exp(-1j * w)) @ v.conj().T
    w, v = eigh(Ao); Uo = (v * np.exp(-1j * w)) @ v.conj().T
    return Ae, Ao, Uo @ Ue
def hlog(U):
    Tm, Z = schur(U, output="complex"); ph = np.angle(np.diag(Tm))
    return (Z * (-ph)) @ Z.conj().T
def cm(a, b): return a @ b - b @ a
def bch(Ae, Ao, n):
    H = Ae + Ao
    if n >= 2: H = H - 0.5j * cm(Ao, Ae)
    if n >= 3: H = H - (cm(Ao, cm(Ao, Ae)) + cm(Ae, cm(Ae, Ao))) / 12
    return H
def density(terms):
    """q_c: own term + equal share of every nested commutator among the distinct cubes it touches (BCH to 3rd order)."""
    nc = len(terms); q = [t.astype(complex).copy() for t in terms]
    ev = [c for c in range(nc) if c % 2 == 0]; od = [c for c in range(nc) if c % 2 == 1]
    near = lambda a, b: abs(a - b) <= 1
    for o in od:
        for e in ev:
            if near(o, e):
                x = -0.5j * cm(terms[o], terms[e]); q[o] += x / 2; q[e] += x / 2
    for (X, Y) in ((od, ev), (ev, od)):            # [A_X,[A_X,A_Y]]: clusters x1,x2 in X, y in Y
        for y in Y:
            for x2 in X:
                if not near(x2, y): continue
                inner = cm(terms[x2], terms[y])
                for x1 in X:
                    if not (near(x1, x2) or near(x1, y)): continue
                    x = -cm(terms[x1], inner) / 12; cl = {x1, x2, y}
                    for c in cl: q[c] += x / len(cl)
    return q
L, Nf, Vint, muf = 10, 5, 1.0, 0.3
res = {}
for eps in (0.05, 0.1):
    terms, nops = chain(L, Nf, eps, muf * eps, Vint)
    Ae, Ao, U = floquet(terms); HF = hlog(U)
    res[eps] = dict(dF=[np.linalg.norm(HF - bch(Ae, Ao, n), 2) for n in (1, 2, 3)],
                    dC=[np.linalg.norm(U.conj().T @ bch(Ae, Ao, n) @ U - bch(Ae, Ao, n), 2) for n in (1, 2, 3)])
    if eps == 0.1:
        q = density(terms); H3 = bch(Ae, Ao, 3); idn = np.abs(sum(q) - H3).max()
        far = max(np.abs(cm(terms[a], terms[b])).max() for a in range(len(terms)) for b in range(len(terms)) if abs(a - b) > 1)
        keep = (terms, nops, U, q, H3, Ae, Ao)
report(idn < 1e-12 and far < 1e-13, "T",
       f"B1 local density: q_c = own term + equal shares of the nested commutators of the cubes it touches; sum_c q_c = H_F^(3) "
       f"(err {idn:.0e}); non-touching cube terms commute (max {far:.0e}), so q_c lives on its cube and its neighbours")
sl = [math.log(res[0.1]["dF"][i] / res[0.05]["dF"][i]) / math.log(2) for i in range(3)]
sc = [math.log(res[0.1]["dC"][i] / res[0.05]["dC"][i]) / math.log(2) for i in range(3)]
report(all(abs(sl[i] - (i + 2)) < 0.35 for i in range(3)) and all(abs(sc[i] - (i + 3)) < 0.35 for i in range(3)), "D",
       f"B2 L=10 interacting chain (V=1): |H_F - H^(n)| ~ eps^{{{sl[0]:.2f},{sl[1]:.2f},{sl[2]:.2f}}} and per-tick change "
       f"|U'H^(n)U - H^(n)| ~ eps^{{{sc[0]:.2f},{sc[1]:.2f},{sc[2]:.2f}}} for n = 1,2,3: order n misses H_F by eps^(n+1) and changes by eps^(n+2) per tick, without accumulating")
terms, nops, U, q, H3, Ae, Ao = keep
w, v = eigh(H3); psi = v[:, 0].copy()
kick = expm(1j * 0.8 * (keep[0][0] / 0.1)); psi = kick @ psi; psi /= np.linalg.norm(psi)   # local packet at the left end
E = []; Qc = []
for t in range(600):
    E.append(np.real(psi.conj() @ H3 @ psi)); Qc.append([np.real(psi.conj() @ x @ psi) for x in q]); psi = U @ psi
E = np.array(E); Qc = np.array(Qc)
drift = abs(E[-100:].mean() - E[:100].mean()); osc = E.std(); loc = np.ptp(Qc, axis=0).max()
report(drift < 5 * osc + 1e-12 and osc < 1e-3 * loc, "D",
       f"B3 600 ticks: sum_c <q_c> oscillates by {osc:.1e} with no drift ({drift:.1e}) while single cubes change by up to {loc:.2f}: "
       "the total is kept, each cube's mean moves by currents")
# continuity with a local current
cut = 4; J = sum(U.conj().T @ q[c] @ U - q[c] for c in range(cut + 1))
cuts = [np.linalg.norm(cm(J, nops[x]), 2) for x in range(L)]
near_ = max(cuts[cut:cut + 3]); farv = max(cuts[0], cuts[-1])
report(farv < 1e-2 * near_, "D",
       f"B4 continuity: J = sum_(c<=4)(U'q_cU - q_c) acts at the cut ({near_:.2f}) and only at {farv:.1e} at the chain ends: "
       "d<q_c>/tick = -(face currents), so zero mean in every cube is kept iff the mean face currents vanish")
# exact log locality, full Fock L=8
def pauli_span_weights(H, L):
    P = np.array([I2, sx, np.array([[0, -1j], [1j, 0]]), sz])
    T = H.reshape([2] * (2 * L))
    for q_ in range(L):
        T = np.tensordot(P, T, axes=([2, 1], [0, L - q_]))   # row i_q is axis 0, col j_q is axis L-q
        T = np.moveaxis(T, 0, -1)
    C = T.reshape([4] * L) / 2**L
    w = np.zeros(L + 1)
    it = np.indices([4] * L).reshape(L, -1).T; cf = np.abs(C.reshape(-1))**2
    nz = it != 0; anyp = nz.any(1)
    lo = np.argmax(nz, 1); hi = L - 1 - np.argmax(nz[:, ::-1], 1)
    span = np.where(anyp, hi - lo + 1, 0)
    np.add.at(w, span, cf)
    return w
tails = {}
for eps in (0.1, 0.25):
    terms8, _ = chain(8, None, eps, muf * eps, Vint)
    _, _, U8 = floquet(terms8); H8 = hlog(U8); H8 = H8 - np.trace(H8) / 256 * np.eye(256)
    w8 = pauli_span_weights(H8, 8); tails[eps] = w8[3:] / w8[2]
dec = all(np.all(np.diff(np.log(tails[e][:4])) < 0) for e in tails) and tails[0.1][3] < tails[0.25][3]
report(dec, "D", "B5 exact i log U_F (L=8 full Fock): Pauli weight at span 3..6 relative to span 2: eps 0.1 "
       + ",".join(f"{x:.0e}" for x in tails[0.1][:4]) + "; eps 0.25 " + ",".join(f"{x:.0e}" for x in tails[0.25][:4])
       + ": quasi-local, faster decay at smaller step")
# free tick: exact quadratic log, exponentially local
Ns1 = 60
def real1d_n(Lc_, eps, mu):
    ns = 2 * Lc_; ue = expm(-1j * (eps - mu / 2) * sx); uo = expm(1j * (eps + mu / 2) * sx)
    Ue = np.zeros((ns, ns), complex); Uo = np.zeros_like(Ue)
    for j in range(Lc_):
        a, b = 2 * j, 2 * j + 1; Ue[np.ix_([a, b], [a, b])] = ue
        a, b = 2 * j + 1, (2 * j + 2) % ns; Uo[np.ix_([a, b], [a, b])] = uo
    return Uo @ Ue
hs = hlog(real1d_n(Ns1 // 2, eps0, 0.3 * eps0)); prof = [np.abs(np.diag(hs, r)).max() for r in range(1, 16)]
rate = -np.polyfit(np.arange(3, 15), np.log(np.array(prof[2:14]) + 1e-300), 1)[0]
report(rate > 1.0, "T", f"B6 free tick: one-particle i log U is exactly conserved (no heating) and local, |h(x,x+r)| ~ exp(-{rate:.1f} r) "
       "while the bands stay below pi (band max 2 eps0 < pi)")
# heating proxy: diagonal ensemble in the N=5 sector
fr = {}
for Vv in (0.0, 1.0):
    out = []
    for eps in (0.1, 0.3, 0.6, 1.2):
        terms, _ = chain(L, Nf, eps, muf * eps, Vv); Ae, Ao, U = floquet(terms); Href = bch(Ae, Ao, 2)
        w, v = eigh(Href); p0 = v[:, 0]; Tm, Z = schur(U, output="complex")
        c = np.abs(Z.conj().T @ p0)**2; Ed = np.real(np.einsum("ia,ij,ja->a", Z.conj(), Href, Z)) @ c
        out.append((Ed - w[0]) / (np.trace(Href).real / len(w) - w[0]))
    fr[Vv] = out
report(fr[1.0][0] < 0.01 and fr[1.0][-1] > 5 * fr[1.0][0] and max(fr[0.0]) < max(fr[1.0]), "D",
       "B7 diagonal-ensemble absorbed fraction of H^(2) (L=10, N=5) at eps 0.1/0.3/0.6/1.2: V=1 " + "/".join(f"{x:.1e}" for x in fr[1.0])
       + "; free " + "/".join(f"{x:.1e}" for x in fr[0.0]) + ": small at small step (finite chain cannot show the exponent)")
# current = momentum (T^{0i} = T^{i0}) on the 1D walk, proper units
def om1(k, eps, mu):
    Ue = expm(-1j * (eps - mu / 2) * sx)
    Uo = expm(1j * (eps + mu / 2) * np.array([[0, np.exp(-1j * k)], [np.exp(1j * k), 0]]))
    return np.max(np.angle(np.linalg.eigvals(Uo @ Ue)))
def epsc(mu):   # CL-1 dressed-cone calibration of the step on the 1D walk: sin^2 eps - sin^2(mu/2) = sin^2 eps0
    return math.asin(math.sqrt(math.sin(eps0)**2 + math.sin(mu / 2)**2))
lC = 1.0; N1 = lC * math.sin(eps0); m1 = 0.5; mu1 = m1 * N1; out = []; e1 = epsc(mu1)
uncal = abs((om1(1e-3, eps0, mu1)**2 - mu1**2) / (om1(1e-3, eps0, 0)**2) - 1)
for Kp in (0.05, 0.2):
    k = Kp * lC; h = 1e-5
    w0 = om1(k, e1, mu1); v = (om1(k + h, e1, mu1) - om1(k - h, e1, mu1)) / (2 * h) * lC / N1
    E1 = w0 / N1; c2 = ((om1(1e-3, eps0, 0) / 1e-3) * lC / N1)**2
    out.append(abs(E1 * v / (c2 * Kp) - 1))
report(out[0] < 1e-3 and out[1] / out[0] > 8, "D",
       f"B8 1D walk: with the step at its cone value (uncalibrated, c^2 is off by {uncal:.1e} = (mu/2eps)^2) the mean quasi-energy current "
       f"E v_g equals c^2 K (the momentum) to {out[0]:.1e} at Ka = 0.05 and {out[1]:.1e} at 0.2 "
       "(vanishing as Ka -> 0): face currents are the momentum density, so the momentum constraint on the mean keeps zero mean per cube")
# split: rung mismatch of a passed excitation's proper quasi-energy
mis = []
for pa in (0.05, 0.1, 0.2):
    NP_, NC_ = math.sin(eps0) * 1.0, math.sin(eps0) * 0.5
    EP = om1(pa, epsc(m1 * NP_), m1 * NP_) / NP_; EC = om1(pa / 2, epsc(m1 * NC_), m1 * NC_) / NC_
    mis.append(abs(EP / EC - 1))
sl2 = math.log(mis[2] / mis[0]) / math.log(4)
report(3.0 < sl2 < 4.6, "D", f"B9 split passing at fixed momentum, both rungs cone-calibrated: parent/child proper quasi-energy mismatch {mis[0]:.1e}, {mis[1]:.1e}, "
       f"{mis[2]:.1e} at pa 0.05/0.1/0.2 (slope {sl2:.2f}): zero mean maps to zero mean only up to ~(pa)^4 E per passed quantum")
# volume additivity under subdivision (Lambda term), exact
Pt = rng.normal(size=(4, 3)); vol = lambda P: abs(np.linalg.det((P[1:] - P[0]))) / 6
m_ = {(i, j): (Pt[i] + Pt[j]) / 2 for i in range(4) for j in range(i + 1, 4)}
M = lambda i, j: m_[(min(i, j), max(i, j))]
kids = [np.array([Pt[i]] + [M(i, j) for j in range(4) if j != i]) for i in range(4)]
octa = [M(0, 1), M(0, 2), M(0, 3), M(1, 2), M(1, 3), M(2, 3)]
oct_t = [np.array([M(0, 1), M(2, 3), a, b]) for a, b in ((M(0, 2), M(0, 3)), (M(0, 3), M(1, 3)), (M(1, 3), M(1, 2)), (M(1, 2), M(0, 2)))]
vs_ = sum(vol(k) for k in kids) + sum(vol(t) for t in oct_t)
report(abs(vs_ / vol(Pt) - 1) < 1e-12, "T", f"B10 a flat tetrahedron cut into 8 children keeps its volume (err {abs(vs_/vol(Pt)-1):.0e}); new hinges "
       "inside a flat parent or on a shared face have zero deficit and split hinges keep theirs, so the Regge and Lambda terms map exactly")

# ---------------------------------------------------------------- C. heating vs age (estimates)
print("== C. heating time vs the age (Planck units, cell l_c = 1 l_P supplied)")
tage = 8.08e60; H0 = 1.18e-61; rho_c = 3 * H0**2 / (8 * math.pi); f_bound = 1e-5   # injected <~ 1e-5 rho_crit (supplied)
lines = []
for e0 in (0.0075, 0.02, 0.0375):
    tt = math.sin(e0) / math.sqrt(3); Nt = tage / tt; Eev = 2 * math.pi / tt
    need = -math.log(f_bound * rho_c * tt / (Eev * Nt))       # ln(1/Gamma) per cube per tick
    nstar = math.ceil(math.pi / (2 * e0)); have = 2 * nstar * math.log(1 / e0)
    lines.append((e0, Nt, need, nstar, have, need * e0))
for e0, Nt, need, nstar, have, kap in lines:
    print(f"   eps0 {e0}: ticks in the age {Nt:.1e}; need ln(1/Gamma) > {need:.0f} (one cube outliving the age: > {math.log(Nt):.0f}); "
          f"wrap needs {nstar} pairs, vertex amplitude <= eps0 gives {have:.0f}; exp(-kappa/eps0) needs kappa > {kap:.1f}")
ok = lines[0][4] > lines[0][2] and lines[2][4] < lines[2][2]
report(ok, "E", "C1 heating: the free tick never heats; interacting wrap processes need ceil(pi/2eps0) pairs; with vertex amplitude "
       "<= eps0 the injection bound holds for eps0 below ~0.026 (inside the register's 0.0075-0.0375 window, cutting its top)")
print("theorems: A1-A4, B1, B6, B10; diagnostics: A4b, A5, B2-B5, B7-B9; estimates: C1")
print("supplied: 2D plaquette phases, toy register lengths, toy eps 0.1, V = 1 interaction stand-in, cell = l_P, 1e-5 rho_crit bound")
print(f"elapsed_seconds {time.time()-t0:.1f}")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
