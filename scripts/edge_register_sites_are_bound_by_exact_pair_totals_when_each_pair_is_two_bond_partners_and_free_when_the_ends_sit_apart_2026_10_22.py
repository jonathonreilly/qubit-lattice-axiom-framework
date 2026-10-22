AUDIT_INPUT_PATHS = ('docs/EDGE_REGISTER_SITES_ARE_BOUND_BY_EXACT_PAIR_TOTALS_WHEN_EACH_PAIR_IS_TWO_BOND_PARTNERS_AND_FREE_WHEN_THE_ENDS_SIT_APART_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Edge-register sites under the bound-site rule (finite runner, seeded).

CL-2: a site is bound when some set A containing it and A's mirror A' across
one of A's bonds hold a definite total n_A + n_A' that A alone does not
(n_A indefinite); bound sites get no record.  Edge register (CL-1 Edges, built
like rishons as in edge-source item 6): N = (4 + Delta)s sites per end, one
site per flavour a at each end, raising operator V = S+ f(n1) with
S+ = sum_a c+_{1a} c_{2a}, normalised on its domain (V|n> = |n+1>).

Sections
  A  one register at site level, S = 1, 2, 3 (N = 2S): every pair total
     n_1a + n_2a and the end total commute with the register's terms; the
     window forces one unit per pair; vacuum sites indefinite; value-level
     reduction exact
  B  one tetrahedron of six registers (value level, positive-volume projector,
     one- and two-register hops), S = 1, 2, 3: no register sits surely at an
     extreme value, so every pair site is indefinite while its pair is definite
  C  register + 12-site matter ring with value-controlled matter hops: the
     rule (cap |A| <= 2, and every set) with partners as bond partners vs
     ends far apart; whole-system sets bind everything in a finite toy
  D  BMV numbers and decoherence: records never enter the odds
Supplied: hop weights, phase stiffness, toy sizes, layouts, seeds, TOL.
"""
import itertools
import numpy as np
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import eigsh, LinearOperator, expm_multiply

AUDIT_TIMEOUT_SEC = 120
RNG = np.random.default_rng(20261022)
TOL = 1e-10
NP = NF = 0


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}  {vals}")


def popc(s):
    return bin(s).count("1")


def hop(s, i, j):
    """c+_i c_j on bitstring s with Jordan-Wigner sign; (None, 0) if zero."""
    if not (s >> j) & 1 or (s >> i) & 1:
        return None, 0
    lo, hi = min(i, j), max(i, j)
    mid = (s >> (lo + 1)) & ((1 << (hi - lo - 1)) - 1)
    return s ^ (1 << i) ^ (1 << j), (-1) ** popc(mid)


def nend(s, E):
    return sum((s >> x) & 1 for x in E)


def reg_V(basis, idx, E1, E2, M=None):
    """normalised raising operator S+ f(n1) (or flavour-mixing c+_1 M c_2)."""
    N = len(E1)
    r, c, v = [], [], []
    for n, s in enumerate(basis):
        n1 = nend(s, E1)
        if n1 >= N:
            continue
        f = 1 / np.sqrt((n1 + 1) * (N - n1))
        pairs = [(a, a, 1.0) for a in range(N)] if M is None else \
            [(a, b, M[a, b]) for a in range(N) for b in range(N)]
        for (a, b, w) in pairs:
            t, sg = hop(s, E1[a], E2[b])
            if t is not None and t in idx:
                r.append(idx[t]); c.append(n); v.append(sg * f * w)
    D = len(basis)
    return coo_matrix((v, (r, c)), shape=(D, D)).tocsr()


def bound_flags(p, B, cap=None, skip=None, drop=True, adjacent=True):
    """CL-2 rule on a 1D chain: planes between sites q, q+1; A on one side,
    containing the site next to the plane (so the plane is at one of A's
    bonds), A' = mirror(A).  skip: a site set (the toy's finite stand-in for
    the infinite sea); pairs whose union covers it are left out.  Returns
    bound flags and whether a covering pair was used."""
    L = B.shape[1]
    bound = np.zeros(L, bool)
    whole_used = False
    for q in range(L - 1):
        left = [x for x in range(q + 1) if 0 <= 2 * q + 1 - x < L]
        others = [x for x in left if x != q] if adjacent else left
        base = [q] if adjacent else []
        kmax = len(others) if cap is None else cap - len(base)
        for k in range(0 if adjacent else 1, kmax + 1):
            for sub in itertools.combinations(others, k):
                A = base + list(sub)
                Am = [2 * q + 1 - x for x in A]
                whole = skip is not None and set(skip) <= set(A + Am)
                if whole and drop:
                    continue
                sA = B[:, A].sum(1)
                sT = sA + B[:, Am].sum(1)
                vA = p @ sA ** 2 - (p @ sA) ** 2
                vT = p @ sT ** 2 - (p @ sT) ** 2
                if vA > TOL and vT < TOL:
                    bound[A] = True
                    bound[Am] = True
                    whole_used |= whole
    return bound, whole_used


def bits(basis, L):
    return np.array([[(s >> x) & 1 for x in range(L)] for s in basis], float)


# ---------------------------------------------------------------- A
print("== A. one edge register at site level (N = 2S sites per end)")
k_ph, t_h = 0.5, 1.0
A1, A3, A4 = [], [], []
for S in (1, 2, 3):
    N = 2 * S
    L = 2 * N
    E1, E2 = [2 * a for a in range(N)], [2 * a + 1 for a in range(N)]
    basis = list(range(1 << L)) if S < 3 else [s for s in range(1 << L) if popc(s) == N]
    idx = {s: i for i, s in enumerate(basis)}
    n0 = 3 * N / 5
    V = reg_V(basis, idx, E1, E2)
    ph = diags([0.5 * k_ph * (nend(s, E1) - n0) ** 2 for s in basis])
    H = (-t_h * (V + V.T) + ph).tocsr()
    Bb = bits(basis, L)
    comm = []
    for a in range(N):
        P = diags(Bb[:, E1[a]] + Bb[:, E2[a]])
        comm.append(abs(H @ P - P @ H).max())
    Pe = diags(Bb[:, E1].sum(1) + Bb[:, E2].sum(1))
    ce = abs(H @ Pe - Pe @ H).max()
    Q, _ = np.linalg.qr(RNG.standard_normal((N, N)))
    VM = reg_V(basis, idx, E1, E2, Q)
    HM = (-t_h * (VM + VM.T) + ph).tocsr()
    cm = max(abs(HM @ diags(Bb[:, E1[a]] + Bb[:, E2[a]]) - diags(Bb[:, E1[a]] + Bb[:, E2[a]]) @ HM).max()
             for a in range(N))
    cme = abs(HM @ Pe - Pe @ HM).max()
    A1.append((S, max(comm), ce, cm, cme))
    # vacuum in the one-unit-per-pair sector
    sec = [s for s in basis if all(((s >> E1[a]) & 1) + ((s >> E2[a]) & 1) == 1 for a in range(N))]
    isec = [idx[s] for s in sec]
    Hs = H[isec][:, isec].toarray()
    w, U = np.linalg.eigh(Hs)
    p = U[:, 0] ** 2
    Bs = bits(sec, L)
    m = p @ Bs
    pv = [p @ (Bs[:, E1[a]] + Bs[:, E2[a]]) ** 2 - (p @ (Bs[:, E1[a]] + Bs[:, E2[a]])) ** 2 for a in range(N)]
    bf, _ = bound_flags(p, Bs, cap=2)
    A3.append((S, float(min(m * (1 - m))), float(max(pv)), int(bf.sum()), L))
    # value-level reduction: same ground energy and n1 law
    Hv = np.diag([0.5 * k_ph * (n - n0) ** 2 for n in range(N + 1)]) - t_h * (np.eye(N + 1, k=1) + np.eye(N + 1, k=-1))
    wv, Uv = np.linalg.eigh(Hv)
    n1s = np.array([nend(s, E1) for s in sec])
    pn = np.array([p[n1s == n].sum() for n in range(N + 1)])
    A4.append((S, abs(w[0] - wv[0]), abs(pn - Uv[:, 0] ** 2).max()))
check(all(r[1] < 1e-12 and r[2] < 1e-12 for r in A1), "A1 [T]",
      "every pair total n_1a + n_2a and the end total n_1 + n_2 commute with the register's terms (normalised S+ hop and "
      "any function of n1), at every S: the pair form of the register hop conserves each pair",
      "; ".join(f"S={r[0]}: pair {r[1]:.0e}, end {r[2]:.0e}" for r in A1))
check(all(r[3] > 1e-3 and r[4] < 1e-12 for r in A1), "A1b [T, control]",
      "a flavour-mixing hop c+_1 Q c_2 (Q random orthogonal) breaks the pair totals but keeps the end total, so then "
      "only the whole-end set pair can bind (needs the ends to be mirror layers)",
      "; ".join(f"S={r[0]}: pair comm {r[3]:.2f}, end {r[4]:.0e}" for r in A1))
S = 2; N = 4
ok = True
for e in range(N + 1):
    for d in range(N + 1 - e):
        ss = [s for s in range(1 << 8) if
              sum(((s >> (2 * a)) & 1) + ((s >> (2 * a + 1)) & 1) == 0 for a in range(N)) == e and
              sum(((s >> (2 * a)) & 1) + ((s >> (2 * a + 1)) & 1) == 2 for a in range(N)) == d]
        rng_ = {nend(s, [0, 2, 4, 6]) for s in ss}
        ok &= rng_ == set(range(d, N - e + 1))
check(ok, "A2 [T]", "with e empty and d doubly filled pairs the length value runs over [d, N - e] only, so the full "
      "window n = 0..N (an eighth to 2^(1+Delta) of the flat length) needs exactly one unit in every pair",
      "enumerated for S = 2, all (e, d)")
check(all(r[1] > 0.2 and r[2] < 1e-12 and r[3] == r[4] for r in A3), "A3 [T+D]",
      "in the register's vacuum each site is indefinite while each pair holds exactly one unit; with partners as bond "
      "partners the rule (|A| <= 2) binds every register site",
      "; ".join(f"S={r[0]}: min site var {r[1]:.3f}, pair var {r[2]:.0e}, bound {r[3]}/{r[4]}" for r in A3))
check(all(r[1] < 1e-10 and r[2] < 1e-10 for r in A4), "A4 [T+D]",
      "the site-level vacuum is the value-level one (top multiplet): same energy and length law, so value-level "
      "registers (section B) stand for the sites, every site having P(occupied) = <n>/N",
      "; ".join(f"S={r[0]}: dE {r[1]:.0e}, dP {r[2]:.0e}" for r in A4))

# ---------------------------------------------------------------- B
print("== B. one corner tetrahedron, six registers (value level, positive-volume projector)")
VERT = np.array([[1, 0, 0], [0, 0, 0], [1, 1, 0], [1, 0, 1]], float)
EDG = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
FLAT = np.array([np.linalg.norm(VERT[a] - VERT[b]) for a, b in EDG])
NEIGH = [(e, f) for e in range(6) for f in range(e + 1, 6) if set(EDG[e]) & set(EDG[f])]


def cm_ok(l):
    """positive tetrahedron volume and positive face areas (Cayley-Menger)."""
    d2 = l ** 2
    D = np.zeros(l.shape[:-1] + (4, 4))
    for e, (a, b) in enumerate(EDG):
        D[..., a, b] = D[..., b, a] = d2[..., e]
    C = np.ones(l.shape[:-1] + (5, 5))
    C[..., 0, 0] = 0
    C[..., 1:, 1:] = D
    ok = np.linalg.det(C) > 1e-9
    for tri in itertools.combinations(range(4), 3):
        es = [e for e, (a, b) in enumerate(EDG) if a in tri and b in tri]
        x, y, z = (l[..., e] for e in es)
        ok &= (x + y > z + 1e-9) & (y + z > x + 1e-9) & (x + z > y + 1e-9)
    return ok


def shift(psi, ax, d):
    out = np.zeros_like(psi)
    sl_o = [slice(None)] * 6
    sl_i = [slice(None)] * 6
    if d > 0:
        sl_o[ax], sl_i[ax] = slice(1, None), slice(None, -1)
    else:
        sl_o[ax], sl_i[ax] = slice(None, -1), slice(1, None)
    out[tuple(sl_o)] = psi[tuple(sl_i)]
    return out


Bres = []
for S in (1, 2, 3):
    N = 2 * S
    n = np.arange(N + 1)
    grids = np.meshgrid(*([n] * 6), indexing="ij")
    nv = np.stack(grids, -1).astype(float)
    lens = FLAT * 2.0 ** (5 * nv / N - 3)
    mask = cm_ok(lens)
    n0 = 3 * N / 5
    diag = 0.5 * k_ph * ((nv - n0) ** 2).sum(-1)
    t1, t2 = 1.0, 0.25
    shp = mask.shape

    def Hop(x):
        psi = x.reshape(shp) * mask
        out = diag * psi
        for e in range(6):
            out -= t1 * (shift(psi, e, 1) + shift(psi, e, -1))
        for (e, f) in NEIGH:
            for de in (1, -1):
                for df in (1, -1):
                    out -= t2 * shift(shift(psi, e, de), f, df)
        return (out * mask).ravel()

    D = mask.size
    Hl = LinearOperator((D, D), matvec=Hop, dtype=complex)
    v0 = (mask * (1 + 0.1 * RNG.random(shp))).ravel().astype(complex)
    w, U = eigsh(Hl, k=1, which="SA", v0=v0, tol=1e-9)
    gs = U[:, 0].reshape(shp)
    # random allowed start, evolved by the projected tick (Taylor steps)
    psi = (RNG.standard_normal(shp) + 1j * RNG.standard_normal(shp)) * mask
    psi /= np.linalg.norm(psi)
    dt, nst = 0.02, 50
    for _ in range(nst):
        term, acc = psi.ravel(), psi.ravel().copy()
        for kk in range(1, 13):
            term = Hop(term) * (-1j * dt) / kk
            acc += term
        psi = acc.reshape(shp)
    stats = []
    for st in (gs, psi):
        P = abs(st) ** 2
        P /= P.sum()
        leak = P[~mask].sum()
        mins, extr = 1.0, 0.0
        for e in range(6):
            pe = P.sum(axis=tuple(a for a in range(6) if a != e))
            mn = (pe * n).sum() / N
            mins = min(mins, mn * (1 - mn))
            extr = max(extr, max(pe[0], pe[N]))
        stats.append((mins, extr, leak))
    Bres.append((S, mask.mean(), stats, abs(np.linalg.norm(psi) - 1)))
check(all(r[2][0][1] < 1 - 1e-6 and r[2][1][1] < 1 - 1e-6 and r[2][0][0] > 1e-3 and r[2][1][0] > 1e-3 for r in Bres),
      "B1 [D]", "in a tetrahedron of six registers with the positive-volume projector and one- and two-register hops, "
      "no register sits surely at an extreme value in the vacuum or in an evolved random state, so every register "
      "site is indefinite (variance p(1-p), p = <n>/N) while its pair is exact (A1): every edge site bound",
      "; ".join(f"S={r[0]}: allowed {r[1]:.2f}, min site var gs {r[2][0][0]:.3f} / evolved {r[2][1][0]:.3f}, "
                f"max P(extreme) {max(r[2][0][1], r[2][1][1]):.2f}" for r in Bres))
check(all(r[2][0][2] < 1e-20 and r[2][1][2] < 1e-20 and r[3] < 1e-8 for r in Bres), "B2 [T+D]",
      "the projected tick never leaves the allowed set and is unitary there; the projector is a function of the "
      "values, so it commutes with every pair total (A1) at every S",
      "; ".join(f"S={r[0]}: leak {max(r[2][0][2], r[2][1][2]):.0e}, norm err {r[3]:.0e}" for r in Bres))

# ---------------------------------------------------------------- C
print("== C. register (S = 1) + 12-site matter ring, 16-site chain, two layouts")
LAY = {"partners adjacent": ([0, 2], [1, 3], list(range(4, 16))),
       "ends far apart": ([0, 1], [9, 8], list(range(2, 8)) + list(range(10, 16)))}
Cres = {}
for name, (E1, E2, MS) in LAY.items():
    Lc = 16
    basis = [s for s in range(1 << Lc) if nend(s, MS) == 6 and
             all(((s >> E1[a]) & 1) + ((s >> E2[a]) & 1) == 1 for a in range(2))]
    idx = {s: i for i, s in enumerate(basis)}
    Dc = len(basis)
    V = reg_V(basis, idx, E1, E2)
    n1 = np.array([nend(s, E1) for s in basis], float)
    r, c, v = [], [], []
    for j in range(12):
        x, y = MS[j], MS[(j + 1) % 12]
        for nn, s in enumerate(basis):
            for (i1, i2) in ((x, y), (y, x)):
                t, sg = hop(s, i1, i2)
                if t is not None and t in idx:
                    amp = (1 + 0.4 * (n1[nn] - 1)) if j == 0 else 1.0
                    r.append(idx[t]); c.append(nn); v.append(-sg * amp)
    Hm = coo_matrix((v, (r, c)), shape=(Dc, Dc)).tocsr()
    Bc = bits(basis, Lc)
    stag = Bc[:, MS] @ np.array([0.3 * (-1) ** j for j in range(12)])
    Hc = (Hm - (V + V.T) + diags(0.5 * k_ph * (n1 - 1.2) ** 2 + stag + 0.5 * Bc[:, MS[0]] * (n1 - 1))).tocsr()
    herm = abs(Hc - Hc.T.conj()).max()
    w, U = eigsh(Hc, k=1, which="SA", tol=1e-12)
    psi0 = RNG.standard_normal(Dc) + 1j * RNG.standard_normal(Dc)
    psi0 /= np.linalg.norm(psi0)
    psiT = expm_multiply(-1j * 3.0 * Hc, psi0)
    out = []
    for st in (U[:, 0], psiT):
        p = abs(st) ** 2
        p /= p.sum()
        b2, _ = bound_flags(p, Bc, cap=2)
        bx, _ = bound_flags(p, Bc, cap=None, skip=MS)
        bw, wu = bound_flags(p, Bc, cap=None, skip=MS, drop=False)
        reg = E1 + E2
        bf, _ = bound_flags(p, Bc, cap=None, skip=MS, adjacent=False)
        out.append(tuple((int(b[reg].sum()), int(b[MS].sum())) for b in (b2, bx, bw)) + (wu,) +
                   ((int(bf[reg].sum()), int(bf[MS].sum())),))
    Cres[name] = (out, herm, Dc)
ad, far = Cres["partners adjacent"][0], Cres["ends far apart"][0]
check(all(o[0] == (4, 0) and o[1] == (4, 0) for o in ad), "C1 [T+D]",
      "partners as bond partners: the rule binds all 4 register sites and no matter site, in the coupled vacuum and "
      "an evolved random state, with |A| <= 2 and with every set (pairs covering the whole matter ring aside); "
      "the value-controlled matter hop binds no matter site", f"(register, matter) bound: vacuum {ad[0][:2]}, evolved {ad[1][:2]}")
check(all(o[0] == (0, 0) and o[1] == (0, 0) for o in far), "C2 [T+D]",
      "ends far apart (the edge's two vertices): no set pair is definite, so every register site is FREE under "
      "the rule as written and would be recorded each half-tick", f"vacuum {far[0][:2]}, evolved {far[1][:2]}")
check(all(o[2] == (4, 12) and o[3] for o in ad + far), "C3 [T, finite-size]",
      "in a finite toy a set pair covering the whole matter ring (with partners adjacent the ring alone is a closed "
      "component) holds its conserved number and binds every matter site; on Z^3 the sea is infinite, no finite set "
      "pair covers it and its region counts fluctuate, so this is a finite-size artefact (a closed universe would "
      "show it)",
      f"with covering pairs: adjacent {ad[0][2]}, far {far[0][2]}; dims {Cres['partners adjacent'][2]}, "
      f"herm err {max(Cres[k][1] for k in Cres):.0e}")

check(all(o[4] == (4, 0) for o in ad + far), "C4 [T+D, variant]",
      "reading variant 'mirror across any lattice plane' (A need not touch the plane): binds the far-apart register "
      "too, and still no matter site (covering pairs aside); it makes the role read correlations at the edge's length",
      f"(register, matter): far vacuum {far[0][4]}, evolved {far[1][4]}; adjacent {ad[0][4]}")

# ---------------------------------------------------------------- D
print("== D. BMV numbers and decoherence (estimates against the register's prediction)")
G, hb, c = 6.674e-11, 1.0546e-34, 2.998e8
m, d, dx, T = 1e-14, 200e-6, 250e-6, 2.5
kap = G * m ** 2 * T / hb
phi_in = kap / d
dphi = kap * (1 / d + 1 / (d + 2 * dx) - 2 / (d + dx))
conc = abs(np.sin(dphi / 2))
check(abs(phi_in - 0.79) < 0.01 and abs(conc - 0.156) < 0.002, "D1 [E]",
      "the register's BMV numbers: inner-branch phase G m^2 T/(hbar d) and concurrence |sin(dphi/2)| for the linear "
      "two-arm geometry", f"phi_in {phi_in:.3f} rad, dphi {dphi:.3f}, concurrence {conc:.3f}")
om = 2 * np.pi / T
Q3 = m * dx ** 2 * om ** 3
Ng = G / (5 * c ** 5) * Q3 ** 2 * T / (hb * om)
check(Ng < 1e-50, "D2 [E]",
      "records never condition the odds (CL-2), so readable distributions, and the witness, do not depend on which "
      "sites are recorded (matter sites of the masses are already recorded every half-tick); the decoherence that "
      "does act is in the odds: quadrupole gravitons emitted per run, the same whether edges are recorded or not",
      f"N_graviton ~ {Ng:.1e} per run")
s_, Dl, be = 135, 1, 40
check(True, "D3 [E]", "if edge sites were free: records per cell per half-tick from edge registers, 12(4+Delta)s/b_e^3 "
      "(6 registers per block site, two ends)", f"{12 * (4 + Dl) * s_ / be ** 3:.3f} at s = {s_}, Delta = {Dl}, "
      f"b_e = {be}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
