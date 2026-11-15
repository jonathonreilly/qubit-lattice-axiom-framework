"""s7: lane F session 7 (SF.md §21-§23). Criteria: checks/s7_criteria.md (written first).
Certificate (𝔠_∞-cert) for PROOF's level-0 trivial-background operator Õ_0 (Setting N5-bg at (1, 1), κ_0 = 1, d = 4, L = 3):
  A  exact rational rows of Õ_0, exact hyperoctahedral covariance (+ negative control), q = N_0(|ΠQ^TQΠ|);
  B  column-wise approximate inverse K̃ (n = 12 torus inverse, midpoint support R = 5, exactly Stab-invariant canonical columns),
     rigorous residual enclosure (Higham γ_n, upward rounding), row sums by exact covariance; exact spot checks of E; controls;
  C  arithmetic: 𝔠_∞^♯, λ_min, rates, CHEB-f, BR1 / (TH-ch″), N5-sf0 re-evaluation (proposed), DX′-1, the TH-2 table.
Lane F's own code (the operator construction follows the definitions of PROOF Setting N5-0/N5-bg/N5-sl, as c36 C does)."""
import itertools, math, os, resource, sys, time
from fractions import Fraction
import numpy as np
from mpmath import mp, mpf, sqrt as msqrt, log as mlog, exp as mexp, coth as mcoth, acosh as macosh, ceil as mceil

T0 = time.time()
mp.dps = 50
OK = {}


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20


def stamp(s):
    print(f"[{time.time()-T0:7.1f}s, RSS {rss():5.0f} MB] {s}", flush=True)


# ====================================================================================================== operator (exact)
d, L = 4, 3
h = (L - 1) // 2
c0 = (h,) * d
ORD = list(itertools.permutations(range(d)))
EU = [tuple(int(i == j) for i in range(d)) for j in range(d)]
LINKS0 = [(u, mu) for u in itertools.product(range(L), repeat=d) for mu in range(d)]
LIDX = {b: i for i, b in enumerate(LINKS0)}
NT = 324


def plus(x, mu, s=1):
    return tuple(x[i] + s * EU[mu][i] for i in range(d))


def bl(x):
    return tuple(v // L for v in x)


def add(dct, k, v):
    if v:
        nv = dct.get(k, 0) + v
        if nv:
            dct[k] = nv
        else:
            dct.pop(k, None)


def axial_steps(c, y, order):
    x = list(c); out = []
    for mu in order:
        while x[mu] != y[mu]:
            if y[mu] > x[mu]:
                out.append((tuple(x), mu, +1)); x[mu] += 1
            else:
                xb = list(x); xb[mu] -= 1; out.append((tuple(xb), mu, -1)); x[mu] -= 1
    return out


def centre(X):
    return tuple(L * Xi + h for Xi in X)


def contour_steps(X, mu, order, y):
    cX = centre(X)
    Y = list(X); Y[mu] += 1; cY = centre(Y)
    st = axial_steps(cX, y, order)
    z = list(y)
    for _ in range(L):
        st.append((tuple(z), mu, +1)); z[mu] += 1
    back = axial_steps(cY, tuple(z), order)
    st += [(xb, nu, -s) for (xb, nu, s) in reversed(back)]
    return st


class Ops:
    def __init__(self, kap):
        self.kap = kap
        norm = Fraction(1, 24 * L ** d)
        wt = {}
        for y in itertools.product(range(L), repeat=d):
            for o in ORD:
                for (xb, mu, s) in axial_steps(c0, y, o):
                    wt[(xb, mu)] = wt.get((xb, mu), 0) + s
        self.w = {k: v * norm for k, v in wt.items() if v != 0}
        self.qt = []
        for mu in range(d):
            acc = {}
            for y in itertools.product(range(L), repeat=d):
                for o in ORD:
                    for (xb, nu, s) in contour_steps((0,) * d, mu, o, y):
                        acc[(xb, nu)] = acc.get((xb, nu), 0) + s
            self.qt.append({k: v * norm for k, v in acc.items() if v != 0})
        self.w2 = sum(v * v for v in self.w.values())
        self.qinv = {}
        for mu in range(d):
            for (xb, nu), v in self.qt[mu].items():
                self.qinv.setdefault((nu, tuple(c % L for c in xb)), []).append((mu, xb, v))

    def Pi(self, v):
        w, w2 = self.w, self.w2
        out = dict(v); blocks = {}
        for (x, mu), a in v.items():
            if bl(x) == bl(plus(x, mu)):
                X = bl(x); key = (tuple(x[i] - L * X[i] for i in range(d)), mu)
                if key in w:
                    blocks[X] = blocks.get(X, 0) + w[key] * a
        for X, s in blocks.items():
            if s:
                for (xb, mu), wv in w.items():
                    add(out, (tuple(xb[i] + L * X[i] for i in range(d)), mu), -wv * s / w2)
        return out

    @staticmethod
    def dd(v):
        F = {}
        for (y, a), val in v.items():
            for mu in range(d):
                for nu in range(mu + 1, d):
                    if a == mu:
                        add(F, (y, mu, nu), val); add(F, (plus(y, nu, -1), mu, nu), -val)
                    if a == nu:
                        add(F, (plus(y, mu, -1), mu, nu), val); add(F, (y, mu, nu), -val)
        out = {}
        for (x, mu, nu), f in F.items():
            add(out, (x, mu), f); add(out, (plus(x, nu), mu), -f)
            add(out, (plus(x, mu), nu), f); add(out, (x, nu), -f)
        return out

    def QtQ(self, v):
        cv = {}
        for (x, nu), val in v.items():
            for (mu, xb, q) in self.qinv.get((nu, tuple(c % L for c in x)), ()):
                add(cv, (tuple((x[i] - xb[i]) // L for i in range(d)), mu), q * val)
        out = {}
        for (X, mu), cval in cv.items():
            for (xb, nu), q in self.qt[mu].items():
                add(out, (tuple(xb[i] + L * X[i] for i in range(d)), nu), q * cval)
        return out

    @staticmethod
    def fix(v):
        nB = L ** d - 1
        f = {}
        for (x, mu), val in v.items():
            add(f, plus(x, mu), val); add(f, x, -val)
        byb = {}
        for s, val in f.items():
            byb.setdefault(bl(s), {})[s] = val
        g = {}
        for X, fs in byb.items():
            cX = centre(X)
            fs = dict(fs); fs.pop(cX, None)
            m = sum(fs.values())
            if m:
                for y in itertools.product(range(L), repeat=d):
                    s = tuple(L * X[i] + y[i] for i in range(d))
                    if s != cX:
                        add(fs, s, -m / nB)
            for s, val in fs.items():
                add(g, s, val)
        out = {}
        for s, val in g.items():
            for mu in range(d):
                add(out, (s, mu), -val); add(out, (plus(s, mu, -1), mu), val)
        return out

    def Ot(self, v):
        pv = self.Pi(v)
        Ov = self.dd(pv)
        for k, val in self.QtQ(pv).items():
            add(Ov, k, self.kap * val)
        for k, val in self.fix(pv).items():
            add(Ov, k, val)
        out = self.Pi(Ov)
        for k, val in v.items():
            add(out, k, val)
        for k, val in pv.items():
            add(out, k, -val)
        return out

    def rows(self):
        return [self.Ot({b: Fraction(1)}) for b in LINKS0]

    def one_minus_pi_rows(self):
        out = []
        for b in LINKS0:
            pv = self.Pi({b: Fraction(1)}); r = {b: Fraction(1)}
            for k, val in pv.items():
                add(r, k, -val)
            out.append(r)
        return out


def canon_type(b):
    x, mu = b; X = bl(x)
    return LIDX[(tuple(x[i] - L * X[i] for i in range(d)), mu)], X


def g_link(g, b):
    """hyperoctahedral element g = (perm, sg) about the block-0 centre: (gx)_{perm[i]} = h + sg[i](x_i - h)."""
    x, mu = b; perm, sg = g
    y = [0] * d
    for i in range(d):
        y[perm[i]] = h + sg[i] * (x[i] - h)
    y = tuple(y); nu = perm[mu]
    if sg[mu] > 0:
        return (y, nu), 1
    return (plus(y, nu, -1), nu), -1


def g_link_wrong(b):
    """reflection x_0 -> -x_0 (a plane through a site, NOT the block centre): negative control."""
    x, mu = b
    y = (-x[0],) + tuple(x[1:])
    if mu != 0:
        return (y, mu), 1
    return (plus(y, 0, -1), 0), -1


GENS = [((1, 0, 2, 3), (1, 1, 1, 1)), ((1, 2, 3, 0), (1, 1, 1, 1)), ((0, 1, 2, 3), (-1, 1, 1, 1))]


def covariance_mismatches(rowset, maps):
    bad = 0
    for gl in maps:
        for i, b in enumerate(LINKS0):
            gb, s = gl(b)
            j, T = canon_type(gb)
            tgt = rowset[j]
            for bp, val in rowset[i].items():
                gbp, sp = gl(bp)
                key = (tuple(gbp[0][k] - L * T[k] for k in range(d)), gbp[1])
                if tgt.get(key, 0) != s * sp * val:
                    bad += 1
            if len(tgt) != len(rowset[i]):
                bad += 1
    return bad


ZS = list(itertools.product((-1, 0, 1), repeat=4)); ZI = {Z: k for k, Z in enumerate(ZS)}


def part_A():
    stamp("== Part A: exact rows ==")
    O1 = Ops(Fraction(1)); rows = O1.rows(); omp = O1.one_minus_pi_rows()
    stamp(f"rows at kappa = 1 built; nnz per row in {sorted(set(len(r) for r in rows))}")
    # A1: support, symmetry, N_0
    supp = all(all(-1 <= v <= 1 for v in canon_type(k)[1]) for r in rows for k in r)
    sym = True
    for i, r in enumerate(rows):
        for k, val in r.items():
            j, Z = canon_type(k)
            back = (tuple(LINKS0[i][0][q] - L * Z[q] for q in range(d)), LINKS0[i][1])
            if rows[j].get(back, 0) != val:
                sym = False; break
        if not sym:
            break
    N0 = max(sum(abs(v) for v in r.values()) for r in rows)
    OK["A1"] = supp and sym and N0 == Fraction(10462237, 410670)
    print(f"A1: support in 3^4 blocks {supp}; exact symmetry {sym}; N_0(|O~_0|) = {N0} = {float(N0):.10f}  "
          f"{'PASS' if OK['A1'] else 'FAIL'}")
    # A2, A2n
    gm = [lambda b, g=g: g_link(g, b) for g in GENS]
    b1 = covariance_mismatches(rows, gm); b2 = covariance_mismatches(omp, gm)
    OK["A2"] = (b1 == 0 and b2 == 0)
    print(f"A2: hyperoctahedral covariance mismatches (3 generators): O~_0 {b1}, 1 - Pi {b2}  {'PASS' if OK['A2'] else 'FAIL'}")
    bn = covariance_mismatches(rows, [g_link_wrong])
    OK["A2n"] = bn > 0
    print(f"A2n: reflection through x_0 = 0 (not the block centre): mismatches {bn}  {'PASS' if OK['A2n'] else 'FAIL'}")
    # (1 - Pi) is block-diagonal: matrix on block 0
    Mo = np.zeros((NT, NT)); Mo_ok = True
    for i, r in enumerate(omp):
        for k, val in r.items():
            j, Z = canon_type(k)
            if any(Z):
                Mo_ok = False
            Mo[i, j] = float(val)
    nuw = max(sum(abs(v) for v in r.values()) for r in omp)
    print(f"    1 - Pi block-diagonal: {Mo_ok}; N_0(|1 - Pi|) = {nuw} (PROOF nu_w = 30/13)")
    # A4: q = N_0(|Pi Q^T Q Pi|) = rows(1) - rows(0)
    O0 = Ops(Fraction(0)); rows0 = O0.rows()
    qmax = Fraction(0)
    for r1, r0 in zip(rows, rows0):
        keys = set(r1) | set(r0)
        qmax = max(qmax, sum(abs(r1.get(k, 0) - r0.get(k, 0)) for k in keys))
    del rows0, O0
    print(f"A4 (report): q = N_0(|Pi Q^T Q Pi|) = {qmax} = {float(qmax):.10f}")
    # float blocks, integer numerators, coupling range D_A (midpoint l1), a_ij
    Af = np.zeros((81, NT, NT)); Dc = 1
    for r in rows:
        for v in r.values():
            Dc = Dc * v.denominator // math.gcd(Dc, v.denominator)
    Anum = np.zeros((81, NT, NT), np.int64); DA2 = 0
    for i, r in enumerate(rows):
        mi = np.array(LINKS0[i][0]) * 2 + np.array(EU[LINKS0[i][1]])
        for k, val in r.items():
            j, Z = canon_type(k)
            Af[ZI[Z], i, j] = float(val)
            nv = val * Dc
            assert nv.denominator == 1 and abs(nv.numerator) < 2 ** 62
            Anum[ZI[Z], i, j] = nv.numerator
            mk = np.array(k[0]) * 2 + np.array(EU[k[1]])
            DA2 = max(DA2, int(np.abs(mk - mi).sum()))
    DA = DA2 / 2.0
    aij = np.abs(Af).sum(0) * (1 + 2 * 81 * 2.0 ** -53)
    print(f"    common denominator D = {Dc}; coupling range D_A (midpoint l1) = {DA}; float conversion is correctly rounded")
    del rows, omp
    return Af, Anum, Dc, Mo, N0, qmax, DA, aij


# ====================================================================================================== certificate machinery
u = 2.0 ** -53


def up(x):
    return np.nextafter(x, np.inf)


def gam(n):
    return float(up(up(1.01 * n * u)))


def group_data():
    G = [(p, s) for p in itertools.permutations(range(d)) for s in itertools.product((1, -1), repeat=d)]
    pi = np.zeros((len(G), NT), np.int64); dl = np.zeros((len(G), NT, 4), np.int64); sg = np.zeros((len(G), NT), np.int64)
    lin = np.zeros((len(G), 4, 4), np.int64)
    for a, g in enumerate(G):
        perm, s = g
        for i in range(4):
            lin[a, perm[i], i] = s[i]
        for t, b in enumerate(LINKS0):
            gb, sgn = g_link(g, b)
            j, Z = canon_type(gb)
            pi[a, t] = j; dl[a, t] = Z; sg[a, t] = sgn
    return lin, pi, dl, sg


U4 = np.array([b[0] for b in LINKS0]); MU = np.array([b[1] for b in LINKS0])
MID0 = 2 * U4 + np.eye(4, dtype=np.int64)[MU]


def box_Z(lo, n):
    r = np.arange(lo, lo + n)
    return np.stack(np.meshgrid(r, r, r, r, indexing="ij"), -1).reshape(-1, 4)


def support_mask(lo, n, R):
    M = 6 * box_Z(lo, n)[:, None, :] + MID0[None]
    return np.all(np.abs(M - 2) <= 2 * (3 * R) + 3, axis=-1)          # doubled units: |m - c| <= 3R + 3/2


def torus_columns(A, cols, n):
    k1 = 2 * np.pi * np.arange(n) / n
    nh = n // 2 + 1
    Zarr = np.array(ZS)
    X = np.zeros((n, n, n, nh, NT, len(cols)), complex)
    rhs = np.zeros((NT, len(cols))); rhs[cols, np.arange(len(cols))] = 1.0
    diag = []; res = 0.0
    for kv in itertools.product(range(n), range(n), range(n), range(nh)):
        ph = np.exp(1j * (Zarr @ k1[list(kv)]))
        Ah = np.tensordot(ph, A, axes=(0, 0))
        x = np.linalg.solve(Ah, rhs); X[kv] = x
        if kv in ((n // 2,) * 4, (0, 0, 0, 0)):
            diag.append((kv, float(np.linalg.eigvalsh(Ah)[0])))
            res = max(res, float(np.abs(Ah @ x - rhs).max()))
    lo = -(n // 2)
    idx = np.arange(lo, lo + n) % n
    out = []
    for q in range(len(cols)):
        o = np.fft.irfftn(X[..., q], s=(n, n, n, n), axes=(0, 1, 2, 3))
        out.append(np.ascontiguousarray(o[np.ix_(idx, idx, idx, idx)]).reshape(n ** 4, NT)); del o
    del X
    return out, lo, diag, res


def canonicalise(col, lo, n, c, lin, pi, dl, sg, mask):
    stab = [a for a in range(len(pi)) if pi[a, c] == c and not dl[a, c].any()]
    Zb = box_Z(lo, n); nb = n ** 4
    own = np.arange(nb * NT, dtype=np.int32).reshape(nb, NT)
    best = own.copy(); bsg = np.ones((nb, NT), np.int8); zero = np.zeros((nb, NT), bool)
    for a in stab:
        GZ = Zb @ lin[a].T
        li = np.zeros((nb, NT), np.int32); bad = np.zeros((nb, NT), bool)
        for i in range(4):
            zi = (GZ[:, i][:, None] + dl[a][None, :, i] - lo).astype(np.int32)
            bad |= (zi < 0) | (zi >= n)
            li = li * n + np.clip(zi, 0, n - 1)
        li = li * NT + pi[a][None, :].astype(np.int32)
        assert not (bad & mask).any(), "support not invariant"
        assert not (mask & ~mask.ravel()[li.ravel()].reshape(nb, NT)).any(), "support not invariant (image)"
        s = sg[a][None, :].astype(np.int8)
        zero |= (li == own) & (s < 0) & mask
        upd = mask & (li < best)
        best = np.where(upd, li, best); bsg = np.where(upd, s, bsg)
        del li, bad, GZ
    del own
    K = np.where(mask, bsg * col.ravel()[best.ravel()].reshape(nb, NT), 0.0)
    K[zero] = 0.0
    return K, len(stab), int(zero.sum())


def mid_dist_rows(Zrows, c):
    """midpoint l1 distances from the link (0, c) to all links of the blocks Zrows: (len, 324)."""
    M = 6 * Zrows[:, None, :] + MID0[None]
    return np.abs(M - MID0[c]).sum(-1) / 2.0


MS = [0.0, 0.005, 0.01, 0.02, 0.03]
WINF = 1 + 1e-13            # covers the evaluation error of exp and of the product by |x| (both <= a few ulp)


def weighted_type_sums(X, lo, n, c):
    """for each m in MS: rigorous upper bounds of sum_Z |X(Z, i)| e^{m d((Z,i),(0,c))} per type i (X on the box)."""
    Xb = X.reshape(n, n ** 3, NT)
    out = np.zeros((len(MS), NT)); cnt = n ** 4
    for q0 in range(n):
        Zr = box_Z(lo, n).reshape(n, n ** 3, 4)[q0]
        dist = mid_dist_rows(Zr, c); ax = np.abs(Xb[q0])
        for a, m in enumerate(MS):
            out[a] += (ax * np.exp(m * dist)).sum(0)
    return up(up(out * (1 + 2 * gam(cnt + 1)) * WINF))


def residual_column(Af, K, lo, n, c, rng, nsample=20):
    """fl(E) = fl(O~ K) - e_(0,c) on the box [lo-1, lo+n]^4, slab by slab; returns the weighted type sums of |fl E|,
    the identity entry, a sample of entries (Z, i, flE) and the E box parameters."""
    Kb = K.reshape(n, n, n, n, NT)
    m = n + 2
    P = np.zeros((m + 2, m + 2, m + 2, m + 2, NT)); P[2:n + 2, 2:n + 2, 2:n + 2, 2:n + 2] = Kb
    lo2 = lo - 1
    S = np.zeros((len(MS), NT)); top = []; rand = []; idv = None
    for q0 in range(m):
        o = np.zeros((m, m, m, NT))
        for Y in ZS:
            o += P[q0 + 1 + Y[0], 1 + Y[1]:1 + Y[1] + m, 1 + Y[2]:1 + Y[2] + m, 1 + Y[3]:1 + Y[3] + m] @ Af[ZI[Y]].T
        o = o.reshape(m ** 3, NT)
        Zr = box_Z(lo2, m).reshape(m, m ** 3, 4)[q0]
        if q0 + lo2 == 0:
            r0 = int(np.where(np.all(Zr == 0, axis=1))[0][0])
            idv = float(o[r0, c]); o[r0, c] -= 1.0
        dist = mid_dist_rows(Zr, c); ao = np.abs(o)
        for a, mm in enumerate(MS):
            S[a] += (ao * np.exp(mm * dist)).sum(0)
        fl = ao.ravel()
        for p in np.argpartition(fl, -nsample)[-nsample:]:
            top.append((float(fl[p]), tuple(int(v) for v in Zr[p // NT]), int(p % NT), float(o.ravel()[p])))
        nz = np.nonzero(fl)[0]
        if nz.size:
            for p in rng.choice(nz, size=min(2, nz.size), replace=False):
                rand.append((float(fl[p]), tuple(int(v) for v in Zr[p // NT]), int(p % NT), float(o.ravel()[p])))
        del o, ao
    del P
    top.sort(reverse=True)
    sample = top[:nsample] + [rand[i] for i in rng.choice(len(rand), size=min(nsample, len(rand)), replace=False)]
    cnt = m ** 4
    return up(up(S * (1 + 2 * gam(cnt + 1)) * WINF)), idv, sample


def exact_check(sample, Af, Anum, Dc, K, lo, n, c):
    """exact E(z) = sum O~_exact(z, z') K(z') - delta (K's floats are exact dyadics) against fl(E) +- radius."""
    Kb = K.reshape(n, n, n, n, NT); worst = 0.0; ok = True
    gn = gam(81 * NT + 1)
    for (_, Z, i, flv) in sample:
        absAK = 0.0; ex = Fraction(0)
        for Y in ZS:
            W = tuple(Z[q] + Y[q] - lo for q in range(4))
            if all(0 <= W[q] < n for q in range(4)):
                kv = Kb[W]
                absAK += float(np.abs(Af[ZI[Y], i]) @ np.abs(kv))
                nzj = np.nonzero(Anum[ZI[Y], i])[0]
                for j in nzj:
                    if kv[j] != 0.0:
                        ex += int(Anum[ZI[Y], i, j]) * Fraction(float(kv[j]))
        ex = ex / Dc
        if Z == (0, 0, 0, 0) and i == c:
            ex -= 1
        rad = (gn + 2 * u) * (1 + gn) * absAK * (1 + 1e-12) + 4 * u * abs(flv)
        diffF = abs(ex - Fraction(flv))
        diff = float(diffF)
        worst = max(worst, diff / rad if rad > 0 else (0.0 if diff == 0 else np.inf))
        if diffF > Fraction(rad):
            ok = False
    return ok, worst


def part_B(Af, Anum, Dc, Mo, DA, aij):
    stamp("== Part B: certificate ==")
    lin, pi, dl, sg = group_data()
    reps = sorted(set(int(pi[:, t].min()) for t in range(NT)))
    orb = {c: sorted(set(int(v) for v in pi[:, c])) for c in reps}
    cover = sorted(t for c in reps for t in orb[c])
    OK["A3"] = (cover == list(range(NT)))
    print(f"A3: canonical column types {reps}, orbit sizes {[len(orb[c]) for c in reps]} (sum {len(cover)})  "
          f"{'PASS' if OK['A3'] else 'FAIL'}")
    # h_j: an element mapping type j to its canonical type
    hj = {}
    for c in reps:
        for j in orb[c]:
            hj[j] = (c, int(np.where(pi[:, j] == c)[0][0]))
    n, R = 12, 5
    lo = -(n // 2)
    mask = support_mask(lo, n, R)
    mask2 = support_mask(lo, n, 2)
    rng = np.random.default_rng(7)
    gn = gam(81 * NT + 1)
    TK, TKp, SE, Tfull = {}, {}, {}, {}
    B1 = 0.0; B2x_ok = True; B2x_w = 0.0; diags = None; tres = 0.0; nzero = 0
    for bi in range(0, len(reps), 2):
        batch = reps[bi:bi + 2]
        cols, lo_, diag, res = torus_columns(Af, batch, n); tres = max(tres, res)
        if diags is None:
            diags = diag
        stamp(f"torus inverse columns {batch} done (solve residual at sampled k {res:.1e})")
        for k, c in enumerate(batch):
            col = cols[k]
            Tfull[c] = np.abs(col).sum(0)
            K, ns, nz = canonicalise(col, lo, n, c, lin, pi, dl, sg, mask); nzero += nz
            B1 = max(B1, float(np.abs(K - col)[mask].max()))
            TK[c] = weighted_type_sums(K, lo, n, c)
            Kp = K.copy()
            r0 = int(np.where(np.all(box_Z(lo, n) == 0, axis=1))[0][0])
            Kp[r0] -= Mo[:, c]
            TKp[c] = weighted_type_sums(Kp, lo, n, c); del Kp
            S, idv, sample = residual_column(Af, K, lo, n, c, rng)
            # rounding radius: (gamma_n + 2u)(1 + gamma_n) e^{m D_A} sum_j a_ij v_j^m, v^m = TK; plus the identity entry
            err = np.array([(gn + 2 * u) * (1 + gn) * math.exp(m * DA) * WINF * (aij @ TK[c][a]) for a, m in enumerate(MS)])
            S = up(up(S + err * (1 + 1e-12)))
            S[:, c] = up(S[:, c] + 4 * u * (abs(idv) + 1))
            SE[c] = S
            okx, wx = exact_check(sample, Af, Anum, Dc, K, lo, n, c)
            B2x_ok &= okx; B2x_w = max(B2x_w, wx)
            if c == reps[0]:
                K2 = np.where(mask2, K, 0.0)
                S2, _, _ = residual_column(Af, K2, lo, n, c, rng, nsample=1)
                ctrl = (float(S2[0].sum()), float(SE[c][0].sum())); del K2
            stamp(f"  column {c}: |Stab| = {ns}, zeroed {nz}; K type-sum max {TK[c][0].max():.4f}, "
                  f"E type-sum max {SE[c][0].max():.3e} (total {SE[c][0].sum():.3e}); exact spot check {okx} (worst ratio {wx:.2e})")
            del K, col
            cols[k] = None
        del cols
    OK["B1"] = B1 <= 1e-12
    print(f"B1: max |K~ - torus column| on the support = {B1:.2e}  {'PASS' if OK['B1'] else 'FAIL'}; "
          f"sign-forced zeros {nzero}; torus solve residual {tres:.1e}")

    def rowsum(T):
        out = np.zeros((T[reps[0]].shape[0], NT))
        for j in range(NT):
            c, a = hj[j]
            out += T[c][:, pi[a]]
        return up(up(out * (1 + 2 * gam(NT + 1))))

    e = rowsum(SE).max(1); k = rowsum(TK).max(1); kp = rowsum(TKp).max(1)
    full = np.zeros(NT)
    for j in range(NT):
        c, a = hj[j]; full += Tfull[c][pi[a]]
    full = float(full.max())
    OK["B2"] = bool(e[0] < 1)
    OK["B2x"] = B2x_ok
    print("B2: certified (midpoint metric)  m      k_m          k'_m         e_m")
    for a, m in enumerate(MS):
        print(f"                                {m:<6} {k[a]:<12.6f} {kp[a]:<12.6f} {e[a]:.6e}")
    print(f"B2: e_0 = {e[0]:.6e} < 1: {'PASS' if OK['B2'] else 'FAIL'}")
    print(f"B2x: exact rational spot checks of E (top + random, every canonical column): {'PASS' if B2x_ok else 'FAIL'} "
          f"(worst |E_exact - fl E| / radius = {B2x_w:.2e})")
    gam0 = Fraction(1, 3500000) * Fraction(1, 2) / 9
    dlt = float(gam0 / 2)
    OK["B3"] = bool(e[0] + dlt * k[0] < 1)
    print(f"B3: e_0 + delta k_0 = {e[0] + dlt*k[0]:.6e} < 1 (delta = gamma_0/2 = {dlt:.4e}): {'PASS' if OK['B3'] else 'FAIL'}")
    lam_cert = (1 - e[0]) / k[0]
    lam_meas = min(v for (_, v) in diags)
    OK["B4"] = bool(full <= k[0] / (1 - e[0]) and lam_meas >= lam_cert)
    print(f"B4: float N_0(|G_12|) = {full:.6f} <= certified k_0/(1 - e_0) = {k[0]/(1-e[0]):.6f}; float lambda_min(symbol) at "
          f"K = (pi,...) {diags} >= certified (1 - e_0)/k_0 = {lam_cert:.6e}: {'PASS' if OK['B4'] else 'FAIL'}")
    OK["B5n"] = ctrl[0] > ctrl[1]
    print(f"B5n: residual column total, R = 2: {ctrl[0]:.4e} vs R = 5: {ctrl[1]:.4e}: {'PASS' if OK['B5n'] else 'FAIL'}")
    return [Fraction(float(x)) for x in k], [Fraction(float(x)) for x in kp], [Fraction(float(x)) for x in e], full, lam_meas


def part_C(k, kp, e, N0, q, full, lam_meas):
    stamp("== Part C: arithmetic ==")
    gam0 = Fraction(1, 3500000) * Fraction(1, 2) / 9
    dl = gam0 / 2
    r1 = 20
    # C1
    den = 1 - e[0] - dl * k[0]
    cinf = kp[0] + dl + k[0] * (e[0] + dl * k[0]) / den
    lam = den / k[0]
    lam0 = (1 - e[0]) / k[0]
    c_triv = kp[0] + k[0] * e[0] / (1 - e[0])
    print(f"C1: c_inf^# = {float(cinf):.6f}  (trivial background: c^nat_0 = {float(c_triv):.6f}; PROOF's 2.0e37; float N_0(|G_12|) "
          f"= {full:.4f})")
    print(f"    lambda_min(O~(U,V)) >= {float(lam):.6e} on N(alpha_*) (real); lambda_min(O~_0) >= {float(lam0):.6e}; measured {lam_meas:.6f}")
    best = None
    for a, m in enumerate(MS):
        dm = Fraction(math.exp(m * (r1 + 1)) * (1 + 1e-12)) * dl
        if m > 0 and e[a] + dm * k[a] < 1:
            Cm = kp[a] + dm + k[a] * (e[a] + dm * k[a]) / (1 - e[a] - dm * k[a])
            best = (m, Cm)
            print(f"    m = {m}: N_m^mid(|C(U,V)|) <= {float(Cm):.4f}; |C(b,b')| <= {float(Cm)*math.exp(m):.4f} e^(-{m} d_base(b,b'))")
    winw = den / (2 * q * k[0])
    print(f"    kappa-window (CI-0/CI-bg with half the margin): |kappa - 1| <= {float(winw):.4e}")
    OK["C1"] = cinf > 0 and lam > 0 and best is not None
    print(f"    pre-registered target c_inf^# <= 1e3: {'MET' if cinf <= 1000 else 'NOT MET'}")
    # C2 CHEB-f
    a_ = mpf(lam.numerator) / lam.denominator; b_ = mpf(N0.numerator) / N0.denominator + mpf(dl.numerator) / dl.denominator
    sig = (b_ + a_) / (b_ - a_); rho0 = sig + msqrt(sig ** 2 - 1); th = mlog(rho0)
    rho = msqrt(rho0); mu = mlog(rho) / 24
    cc, AA = (a_ + b_) / 2, (b_ - a_) * (rho + 1 / rho) / 4
    xL, xR = cc - AA, cc + AA

    def Nmu(M, f0):
        x = mexp(12 * mu) / rho
        tot = f0 * mexp(8 * mu); D = 1
        while True:
            ND = (2 * D + 1) ** 4 - (2 * D - 1) ** 4
            term = ND * 2 * M * rho ** (-(D - 1)) / (rho - 1) * mexp(mu * (12 * D + 8))
            tot += term
            if D > 10 and ((D + 1) / mpf(D)) ** 3 * x < 1 and term < tot * mpf(10) ** -30:
                xr = ((D + 1) / mpf(D)) ** 3 * x
                tot += term * xr / (1 - xr)
                break
            D += 1
        return 324 * tot, D
    Nh, D1 = Nmu(msqrt(xR), msqrt(b_))
    Nmh, D2 = Nmu(1 / msqrt(xL), 1 / msqrt(a_))
    print(f"C2: CHEB-f: a = {float(a_):.6e}, b = {float(b_):.6f}, theta = ln rho_0 = {float(th):.6e}/block; rho = rho_0^(1/2), "
          f"mu = ln(rho)/24 = {float(mu):.6e}/fine unit")
    print(f"    N_mu(|O~^(1/2)|) <= {float(Nh):.4e} (summed to D = {D1} + geometric tail); N_mu(|O~^(-1/2)|) <= {float(Nmh):.4e}")
    OK["C2"] = bool(xL > 0 and Nh < mpf(10) ** 30)
    # C3 BR1 / (TH-ch'')
    N = 3; pL = 11; KFP = mpf("514.5"); cm = mpf(cinf.numerator) / cinf.denominator
    Cbg = mpf("1.011") * msqrt(N) * max(1 + 48 * cm, 36 * pL * cm)
    f1 = mpf("1.011") * msqrt(N)
    tauA, ebgA = mpf("3.602e-31"), mpf("2.08e-34"); tauS, ebgS = mpf("1.0995e-14"), mpf("6.36e-18")
    eps_star_proof = mpf("1.7e-24")
    print(f"C3: C_bg = {float(Cbg):.6e} (PROOF constants: 1.39e40)")
    print(f"    eps_br entries: eps_*/(1 + 36 p_L c) = {float(eps_star_proof/(1+36*pL*cm)):.3e}/C_Delta (PROOF eps_*); "
          f"1/(24 c^2 C_flat) = {float(1/(24*cm**2)):.3e}/C_flat; r_flat/(24 c) = {float(1/(24*cm)):.3e} r_flat; "
          f"r_flat/144; 1/(1728 c K_FP) = {float(1/(1728*cm*KFP)):.3e}")
    for nm, tau, ebg in (("tau^A", tauA, ebgA), ("tau^#", tauS, ebgS)):
        th1 = min(tau, tau / (2 * Cbg), ebg / Cbg)
        print(f"    (TH-ch'') at {nm}: eps_1 <= min{{ {float(th1):.3e} [(TH-ch') entries], {float(eps_star_proof/(1+36*pL*cm)/f1):.3e}/C_Delta, "
              f"{float(1/(24*cm**2)/f1):.3e}/C_flat, {float(1/(24*cm)/f1):.3e} r_flat, {float(1/(144*f1)):.3e} r_flat, "
              f"{float(1/(1728*cm*KFP)/f1):.3e} }}")
    OK["C3"] = True
    # C4 N5-sf0 chain as a function of gamma
    M1 = mpf(449171) / 10935; N0m = mpf(N0.numerator) / N0.denominator

    def chain(g):
        # m: M1 m (1 + 40 m) = g/4
        m = (-1 + msqrt(1 + 160 * g / (4 * M1))) / 80
        a = m / 2
        cda = (g / 4) * mexp(-20 * m)
        gp = g - cda
        Sp = N0m + g / 4 + cda * mexp(20 * m)
        R = mceil(2 * mlog(16 * Sp * mcoth(a / 4) ** 4 / gp) / (a * 3))
        return m, R, 4 * R + 6, cda / (10 * 11 * (4 * R + 5) * 3)
    g0 = mpf(gam0.numerator) / gam0.denominator
    m0, R0, T0_, es0 = chain(g0)
    m1, Rn, Tn, esn = chain(mpf(lam0.numerator) / lam0.denominator)
    print(f"C4: control (gamma_0): m = {float(m0):.4e}, R_* = {float(R0):.4e}, T_0 = {float(T0_):.4e}, eps_* = {float(es0):.4e}/C_Delta "
          f"(PROOF: 9.66e-11, 1.7e12, 6.9e12, 1.7e-24)")
    print(f"    with certified lambda_min(O~_0) = {float(lam0):.6e}: m = {float(m1):.4e}, R_* = {float(Rn):.4e}, T_0 = {float(Tn):.4e}, "
          f"eps_* = {float(esn):.4e}/C_Delta  (proposed; gain x{float(esn/es0):.3e})")
    print(f"    eps_br's first entry with it: {float(esn/(1+36*pL*cm)):.3e}/C_Delta; (TH-ch'') eps_1 entry {float(esn/(1+36*pL*cm)/f1):.3e}/C_Delta")
    OK["C4"] = bool(abs(es0 / mpf("1.7e-24") - 1) < 0.05)
    # C5 DX'-1
    def dx(rho_band, rsol, mu_, Cn, Nprime):
        a_sh = rho_band / (16 * 81 * mexp(mu_ * 8) * Nprime)
        Rsh = mlog(rsol / a_sh) / mu_
        msh = (2 * Rsh / 3 + 3) ** 4; OmB = 4 * (2 * Rsh + 3) ** 4
        ap = a_sh ** 2 / (8 * N * Cn * msh)
        return ap / OmB, Rsh, msh, OmB
    old = dx(mpf("2.280e-61"), mpf("1.03e-30"), mpf("4.83e-11"), 1 / mpf("6.6e-10"), 1)
    print(f"C5: control (session-5 inputs): g_DX'^2 C_Omega N'^2 f^8 ~ {float(old[0]):.3e} (SF: 1.49e-237), R_sh = {float(old[1]):.3e}")
    lamm = mpf(lam.numerator) / lam.denominator
    a1 = dx(mpf("1.89e-33"), mpf("9.40e-17"), mpf("4.83e-11"), 1 / mpf("6.6e-10"), 1)
    a2 = dx(mpf("1.89e-33"), mpf("9.40e-17"), mpf("4.83e-11"), 1 / lamm, 1)
    a3 = dx(mpf("1.89e-33"), mpf("9.40e-17"), mu, 1 / lamm, Nh)
    print(f"    tau^A column, N_r = 1: (i) old gap and rate: {float(a1[0]):.3e}/C_Omega; (ii) certified ||C|| <= 1/lambda: "
          f"{float(a2[0]):.3e}/C_Omega; (iii) + CHEB-f rate mu and its N_mu(|O~^(1/2)|): {float(a3[0]):.3e}/C_Omega "
          f"(R_sh = {float(a3[1]):.3e}, m_sh = {float(a3[2]):.3e}, |Omega_B| = {float(a3[3]):.3e})")
    OK["C5"] = bool(abs(old[0] / mpf("1.49e-237") - 1) < 0.05)
    # C6 TH-2 table
    c37 = mpf("2.0e37"); e2 = 1 / (24 * c37 ** 2); e1 = e2 / f1
    sc = (mpf("0.5") / e1) ** 2
    print(f"C6: 1/(24 c^2) = {float(e2):.4e}; /(1.011 sqrt 3) = {float(e1):.4e}; n_* = {float(382*sc):.3e}/{float(255*sc):.3e}; "
          f"n_# joint {float(5e11*sc):.2e}-{float(4e15*sc):.2e}; RS {float(4e13*sc**2):.2e}-{float(3e17*sc**2):.2e}; "
          f"a_bad {float(mpf('1.7e-210')*(e1/mpf('1.81e-102'))**2):.2e}; levels {float(mlog(382*sc)/4/mlog(3)):.1f}")
    # the same rows at the certified c_inf^# (TH-ch'') with C_flat = C_Delta = 1, r_flat = 1/(20 p_L) as illustrations
    epsA = min(min(tauA, tauA / (2 * Cbg), ebgA / Cbg), esn / (1 + 36 * pL * cm) / f1, 1 / (24 * cm ** 2) / f1,
               1 / (1728 * cm * KFP) / f1, 1 / (24 * cm * 220) / f1)
    sc2 = (mpf("0.5") / epsA) ** 2
    print(f"    at c_inf^# (C_flat = C_Delta = 1, r_flat = 1/220, proposed eps_*): eps_1 = {float(epsA):.3e}; n_* = {float(382*sc2):.3e}; "
          f"levels {float(mlog(382*sc2)/4/mlog(3)):.1f}; a_bad {float(mpf('1.7e-210')*(epsA/mpf('1.81e-102'))**2):.2e}")
    OK["C6"] = bool(abs(e1 / mpf("5.95e-77") - 1) < 0.01)


if __name__ == "__main__":
    Af, Anum, Dc, Mo, N0, q, DA, aij = part_A()
    k, kp, e, full, lam_meas = part_B(Af, Anum, Dc, Mo, DA, aij)
    part_C(k, kp, e, N0, q, full, lam_meas)
    wall = time.time() - T0
    OK["R1"] = wall < 1200 and rss() < 1024
    print(f"R1: wall {wall:.1f} s, peak RSS {rss():.0f} MB: {'PASS' if OK['R1'] else 'FAIL'}")
    for kk in sorted(OK):
        print(kk, "PASS" if OK[kk] else "FAIL")
    print(f"OVERALL {'PASS' if all(OK.values()) else 'FAIL'} {sum(OK.values())}/{len(OK)}")
