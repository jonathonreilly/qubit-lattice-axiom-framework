"""C1b: continuous-time finite-temperature QMC for the cubic spin-1/2 link ring model with
plaquette-cluster (Swendsen-Wang-type) updates, static ice-loop (winding-changing) moves and
parallel tempering in beta.  Written independently of C1's qmc.py (only C1's lattice.py geometry
conventions are reused, through a copy of its arrays).

Configuration (u = tau/beta in [0,1)):  base state s0 (sigma^z on links, +-1) + F events (u, plaquette).
Marginal weight  (g beta)^nF * exp(-V beta Ibar),  Ibar = int_0^1 N_circ(u) du.
Augmented by P markers (Poisson, rate g beta on circulating plaquette-time): weight
(g beta)^(nF+nP) exp(-(g+V) beta Ibar), which integrates back to the marginal weight.
"""
import numpy as np
import numba as nb
import os, sys

sys.path.insert(0, os.path.dirname(__file__))


ORI = ((0, 1), (1, 2), (0, 2))


class Lat:
    """Same conventions as blocks/C1/scripts/lattice.py: vid=(x*L+y)*L+z, link 3*vid+a,
    plaquette 3*vid+o, o: 0:(x,y) 1:(y,z) 2:(x,z), links (v,a)+,(v+a,b)+,(v+b,a)-,(v,b)-."""

    def __init__(self, L):
        self.L = L
        nv = L ** 3
        self.nv, self.nl, self.np = nv, 3 * nv, 3 * nv
        co = np.array([(x, y, z) for x in range(L) for y in range(L) for z in range(L)])
        self.coords = co
        vid = lambda c: ((c[0] % L) * L + c[1] % L) * L + c[2] % L
        E = np.eye(3, dtype=int)
        self.tail = np.repeat(np.arange(nv), 3).astype(np.int64)
        self.head = np.array([vid(co[v] + E[a]) for v in range(nv) for a in range(3)], dtype=np.int64)
        pl = np.zeros((self.np, 4), dtype=np.int64)
        for v in range(nv):
            for o, (a, b) in enumerate(ORI):
                c = co[v]
                pl[3 * v + o] = [3 * v + a, 3 * vid(c + E[a]) + b, 3 * vid(c + E[b]) + a, 3 * v + b]
        self.plinks = pl
        self.psign = np.array([1, 1, -1, -1], dtype=np.int64)
        lp = [[] for _ in range(self.nl)]
        for p in range(self.np):
            for l in pl[p]:
                lp[l].append(p)
        assert all(len(x) == 4 for x in lp)
        self.lplaqs = np.array(lp, dtype=np.int64)
        st = np.zeros((nv, 6), dtype=np.int64)
        ss = np.zeros((nv, 6), dtype=np.int64)
        cnt = np.zeros(nv, dtype=np.int64)
        for l in range(self.nl):
            for v, s in ((self.tail[l], 1), (self.head[l], -1)):
                st[v, cnt[v]] = l
                ss[v, cnt[v]] = s
                cnt[v] += 1
        assert np.all(cnt == 6)
        self.star, self.starsgn = st, ss
        self.ldir = np.tile(np.arange(3), nv).astype(np.int64)
        # cross-section selector for winding: links of direction a with tail coordinate a = 0
        self.wsel = np.array([(co[self.tail[l]][self.ldir[l]] == 0) for l in range(self.nl)])
        self.lpos = np.array([co[v] + 0.5 * E[a] for v in range(nv) for a in range(3)])

    def arrays(self):
        return (self.plinks, self.psign, self.lplaqs, self.tail, self.head, self.star, self.starsgn)

    def div(self, s):
        d = np.zeros(self.nv, dtype=np.int64)
        np.add.at(d, self.tail, s)
        np.add.at(d, self.head, -s)
        return d

    def canonical(self):
        s = np.zeros(self.nl, dtype=np.int64)
        for v in range(self.nv):
            x, y, z = self.coords[v]
            s[3 * v + 0] = (-1) ** y
            s[3 * v + 1] = (-1) ** x
            s[3 * v + 2] = (-1) ** x
        assert np.all(self.div(s) == 0)
        return s

    def winding(self, s):
        w = np.zeros(3, dtype=np.int64)
        for a in range(3):
            sel = self.wsel & (self.ldir == a)
            w[a] = s[sel].sum()
        assert np.all(w % 2 == 0)
        return w // 2


@nb.njit(cache=True)
def nb_seed(s):
    np.random.seed(s)


@nb.njit(cache=True)
def _circ4(a0, a1, a2, a3):
    # psign = (1,1,-1,-1): circulating iff a0 == a1 == -a2 == -a3
    return (a0 == a1) and (a2 == a0 * -1) and (a3 == a2)


@nb.njit(cache=True)
def _find(par, x):
    r = x
    while par[r] != r:
        r = par[r]
    while par[x] != r:
        n = par[x]
        par[x] = r
        x = n
    return r


@nb.njit(cache=True)
def build_csr(nl, vt, vp, nV, plinks):
    """per-link time-ordered vertex lists. returns off, lst, vpos (vertex -> position in each of its 4 lists)"""
    order = np.argsort(vt[:nV])
    cnt = np.zeros(nl + 1, dtype=np.int64)
    for k in range(nV):
        for j in range(4):
            cnt[plinks[vp[k], j] + 1] += 1
    off = np.cumsum(cnt)
    fill = off[:-1].copy()
    lst = np.empty(4 * nV, dtype=np.int64)
    vpos = np.empty((nV, 4), dtype=np.int64)
    for ii in range(nV):
        k = order[ii]
        for j in range(4):
            l = plinks[vp[k], j]
            lst[fill[l]] = k
            vpos[k, j] = fill[l]
            fill[l] += 1
    return off, lst, vpos


@nb.njit(cache=True)
def plaq_integral(q, plinks, off, lst, vt, sstate, sclus, c, lflip, s0):
    """returns (int circ_old, int circ_new) over u in [0,1) for plaquette q.
    piece state of link = sstate of current segment (segment after vertex), the wrap segment before the
    first vertex; new state flips if segment belongs to cluster root c, or if lflip[link]."""
    ptr = np.empty(4, dtype=np.int64)
    end = np.empty(4, dtype=np.int64)
    cur = np.empty(4, dtype=np.int64)  # current segment position, -1 if link has no vertices
    so = np.empty(4, dtype=np.int64)
    sn = np.empty(4, dtype=np.int64)
    for j in range(4):
        l = plinks[q, j]
        ptr[j] = off[l]
        end[j] = off[l + 1]
        if end[j] > ptr[j]:
            cur[j] = end[j] - 1
        else:
            cur[j] = -1
    Iold = 0.0
    Inew = 0.0
    tprev = 0.0
    while True:
        for j in range(4):
            l = plinks[q, j]
            if cur[j] < 0:
                so[j] = s0[l]
                sn[j] = s0[l] * (-1 if lflip[l] else 1)
            else:
                so[j] = sstate[cur[j]]
                f = (sclus[cur[j]] == c) or lflip[l]
                sn[j] = so[j] * (-1 if f else 1)
        tn = 2.0
        for j in range(4):
            if ptr[j] < end[j]:
                t = vt[lst[ptr[j]]]
                if t < tn:
                    tn = t
        tt = tn if tn < 1.5 else 1.0
        if _circ4(so[0], so[1], so[2], so[3]):
            Iold += tt - tprev
        if _circ4(sn[0], sn[1], sn[2], sn[3]):
            Inew += tt - tprev
        if tn > 1.5:
            break
        tprev = tt
        for j in range(4):
            if ptr[j] < end[j] and vt[lst[ptr[j]]] == tn:
                cur[j] = ptr[j]
                ptr[j] += 1
    return Iold, Inew


@nb.njit(cache=True)
def sweep(s0, ft, fp, nF, beta, g, V, plinks, lplaqs, tail, head, star, starsgn, nloops, giant_frac, merge=True,
          fixm_t=np.zeros(1), fixm_p=np.zeros(1, dtype=np.int64), nfix=-1):
    nl = s0.shape[0]
    npl = plinks.shape[0]
    nv = star.shape[0]
    gb = g * beta
    # ---------- 1. F-only CSR and Gibbs resampling of P markers ----------
    offF, lstF, _vp = build_csr(nl, ft, fp, nF, plinks)
    cap = int(gb * npl * 1.0) + 64
    mt = np.empty(cap, dtype=np.float64)
    mp = np.empty(cap, dtype=np.int64)
    nM = 0
    ptr = np.empty(4, dtype=np.int64)
    end = np.empty(4, dtype=np.int64)
    st = np.empty(4, dtype=np.int64)
    Ibar_old = 0.0
    for q in range(npl):
        for j in range(4):
            l = plinks[q, j]
            ptr[j] = offF[l]
            end[j] = offF[l + 1]
            st[j] = s0[l]
        tprev = 0.0
        while True:
            tn = 2.0
            for j in range(4):
                if ptr[j] < end[j]:
                    t = ft[lstF[ptr[j]]]
                    if t < tn:
                        tn = t
            tt = tn if tn < 1.5 else 1.0
            if _circ4(st[0], st[1], st[2], st[3]):
                Ibar_old += tt - tprev
                k = np.random.poisson(gb * (tt - tprev)) if nfix < 0 else 0
                for _ in range(k):
                    if nM >= cap:
                        cap2 = cap * 2
                        mt2 = np.empty(cap2, dtype=np.float64)
                        mp2 = np.empty(cap2, dtype=np.int64)
                        mt2[:nM] = mt[:nM]
                        mp2[:nM] = mp[:nM]
                        mt, mp, cap = mt2, mp2, cap2
                    mt[nM] = tprev + (tt - tprev) * np.random.random()
                    mp[nM] = q
                    nM += 1
            if tn > 1.5:
                break
            tprev = tt
            for j in range(4):
                if ptr[j] < end[j] and ft[lstF[ptr[j]]] == tn:
                    st[j] = -st[j]
                    ptr[j] += 1
    # ---------- 2. all vertices, CSR, segments ----------
    if nfix >= 0:
        mt = fixm_t.copy()
        mp = fixm_p.copy()
        nM = nfix
    nV = nF + nM
    vt = np.empty(nV, dtype=np.float64)
    vp = np.empty(nV, dtype=np.int64)
    vt[:nF] = ft[:nF]
    vp[:nF] = fp[:nF]
    vt[nF:] = mt[:nM]
    vp[nF:] = mp[:nM]
    off, lst, vpos = build_csr(nl, vt, vp, nV, plinks)
    nseg = 4 * nV
    sstate = np.empty(nseg, dtype=np.int64)
    seglink = np.empty(nseg, dtype=np.int64)
    for l in range(nl):
        s = s0[l]
        for pos in range(off[l], off[l + 1]):
            if lst[pos] < nF:
                s = -s
            sstate[pos] = s
            seglink[pos] = l
    # ---------- 3. clusters (union-find on half vertices: 2k lower, 2k+1 upper) ----------
    par = np.arange(2 * nV)
    for l in range(nl):
        m = off[l + 1] - off[l]
        for i in range(m):
            a = 2 * lst[off[l] + i] + 1
            b = 2 * lst[off[l] + (i + 1) % m]
            ra = _find(par, a)
            rb = _find(par, b)
            if ra != rb:
                par[ra] = rb
    sclus = np.empty(nseg, dtype=np.int64)
    for pos in range(nseg):
        sclus[pos] = _find(par, 2 * lst[pos] + 1)
    # super-clusters: at every site v (tau=0 slice), merge all clusters whose own flip would leave a Gauss
    # charge at v (|Q_v(c)| != 0), together with the vertex-free links at v (which always carry |Q|=1).
    # Merging happens only at sites where at least one vertex cluster is charged.  |Q_v(c)| and the
    # vertex-free status are invariant under any flip of super-clusters, so the partition is identical in
    # forward and reverse configurations (detailed balance kept).
    NN = 2 * nV + nl
    par2 = np.arange(NN)
    rr = np.empty(6, dtype=np.int64)
    qq = np.empty(6, dtype=np.int64)
    if merge:
        for v in range(nv):
            nr6 = 0
            anych = False
            for j in range(6):
                l = star[v, j]
                if off[l + 1] > off[l]:
                    r0 = sclus[off[l + 1] - 1]
                    found = -1
                    for t in range(nr6):
                        if rr[t] == r0:
                            found = t
                    if found < 0:
                        rr[nr6] = r0
                        qq[nr6] = 0
                        found = nr6
                        nr6 += 1
                    qq[found] += starsgn[v, j] * s0[l]
            for t in range(nr6):
                if qq[t] != 0:
                    anych = True
            if not anych:
                continue
            first = -1
            for t in range(nr6):
                if qq[t] != 0:
                    if first < 0:
                        first = rr[t]
                    else:
                        ra = _find(par2, rr[t])
                        rb = _find(par2, first)
                        if ra != rb:
                            par2[ra] = rb
            for j in range(6):
                l = star[v, j]
                if off[l + 1] == off[l]:
                    ra = _find(par2, 2 * nV + l)
                    rb = _find(par2, first)
                    if ra != rb:
                        par2[ra] = rb
        for pos in range(nseg):
            sclus[pos] = _find(par2, sclus[pos])
    froot = -np.ones(nl, dtype=np.int64)
    for l in range(nl):
        if off[l + 1] == off[l]:
            froot[l] = _find(par2, 2 * nV + l)
    # group segments and merged free links by root
    csize = np.zeros(NN + 1, dtype=np.int64)
    for pos in range(nseg):
        csize[sclus[pos] + 1] += 1
    coff = np.cumsum(csize)
    cfill = coff[:-1].copy()
    cseg = np.empty(nseg, dtype=np.int64)
    for pos in range(nseg):
        r = sclus[pos]
        cseg[cfill[r]] = pos
        cfill[r] += 1
    fsize = np.zeros(NN + 1, dtype=np.int64)
    for l in range(nl):
        if froot[l] >= 0:
            fsize[froot[l] + 1] += 1
    foff = np.cumsum(fsize)
    ffill = foff[:-1].copy()
    flk = np.empty(nl, dtype=np.int64)
    for l in range(nl):
        if froot[l] >= 0:
            flk[ffill[froot[l]]] = l
            ffill[froot[l]] += 1
    stamp = np.zeros(npl, dtype=np.int64)
    sstamp = np.zeros(nv, dtype=np.int64)
    lflip = np.zeros(nl, dtype=np.bool_)
    ntry = 0
    dIacc = 0.0
    nacc = 0
    nill = 0
    ngiant = 0
    maxc = 0
    stampid = 0
    roots = np.empty(NN, dtype=np.int64)
    nr = 0
    for r in range(NN):
        if coff[r + 1] > coff[r]:
            roots[nr] = r
            nr += 1
    perm = np.random.permutation(nr)
    for ii in range(nr):
        r = roots[perm[ii]]
        sz = coff[r + 1] - coff[r]
        if sz > maxc:
            maxc = sz
        if sz > giant_frac * nseg:
            ngiant += 1
            continue
        ntry += 1
        stampid += 1
        # legality: flip base on wrap segments and merged free links, check, revert
        legal = True
        for kk in range(coff[r], coff[r + 1]):
            pos = cseg[kk]
            l = seglink[pos]
            if pos == off[l + 1] - 1:
                s0[l] = -s0[l]
        for kk in range(foff[r], foff[r + 1]):
            s0[flk[kk]] = -s0[flk[kk]]
        for kk in range(coff[r], coff[r + 1] + foff[r + 1] - foff[r]):
            if kk < coff[r + 1]:
                pos = cseg[kk]
                l = seglink[pos]
                if pos != off[l + 1] - 1:
                    continue
            else:
                l = flk[foff[r] + kk - coff[r + 1]]
            for v in (tail[l], head[l]):
                if sstamp[v] != stampid:
                    sstamp[v] = stampid
                    d = 0
                    for j in range(6):
                        d += starsgn[v, j] * s0[star[v, j]]
                    if d != 0:
                        legal = False
        for kk in range(coff[r], coff[r + 1]):
            pos = cseg[kk]
            l = seglink[pos]
            if pos == off[l + 1] - 1:
                s0[l] = -s0[l]
        for kk in range(foff[r], foff[r + 1]):
            s0[flk[kk]] = -s0[flk[kk]]
        dI = 0.0
        if legal:
            for kk in range(foff[r], foff[r + 1]):
                lflip[flk[kk]] = True
            for kk in range(coff[r], coff[r + 1] + foff[r + 1] - foff[r]):
                if kk < coff[r + 1]:
                    l = seglink[cseg[kk]]
                else:
                    l = flk[foff[r] + kk - coff[r + 1]]
                for j in range(4):
                    q = lplaqs[l, j]
                    if stamp[q] != stampid:
                        stamp[q] = stampid
                        Io, In = plaq_integral(q, plinks, off, lst, vt, sstate, sclus, r, lflip, s0)
                        dI += In - Io
            for kk in range(foff[r], foff[r + 1]):
                lflip[flk[kk]] = False
        acc = legal and (np.random.random() < np.exp(-(g + V) * beta * dI))
        if acc:
            nacc += 1
            dIacc += dI
            for kk in range(coff[r], coff[r + 1]):
                pos = cseg[kk]
                sstate[pos] = -sstate[pos]
                l = seglink[pos]
                if pos == off[l + 1] - 1:
                    s0[l] = -s0[l]
            for kk in range(foff[r], foff[r + 1]):
                s0[flk[kk]] = -s0[flk[kk]]
        elif not legal:
            nill += 1
    # NOTE on s0 inside plaq_integral: only links with no vertices read s0, and such links are never in a
    # cluster, so temporarily flipped wrap links (which have vertices) are not read through s0.
    # ---------- 4. static ice loops on vertex-free links ----------
    visit = -np.ones(nv, dtype=np.int64)
    path_l = np.empty(4 * nv + 8, dtype=np.int64)
    path_v = np.empty(4 * nv + 8, dtype=np.int64)
    cand = np.empty(6, dtype=np.int64)
    nltry = 0
    nlacc = 0
    nlwind = 0
    nlabort = 0
    for it in range(nloops):
        v0 = np.random.randint(nv)
        u = v0
        nst = 0
        closed = False
        while True:
            if visit[u] >= 0:
                closed = True
                break
            if nst >= 4 * nv:
                break
            visit[u] = nst
            path_v[nst] = u
            kc = 0
            for j in range(6):
                l = star[u, j]
                if off[l + 1] == off[l] and starsgn[u, j] * s0[l] == 1:
                    cand[kc] = l
                    kc += 1
            if kc == 0:
                break
            l = cand[np.random.randint(kc)]
            path_l[nst] = l
            nst += 1
            u = head[l] if tail[l] == u else tail[l]
        if not closed:
            nlabort += 1
            for i in range(nst):
                visit[path_v[i]] = -1
            visit[u] = -1
            continue
        i0 = visit[u]
        for i in range(nst):
            visit[path_v[i]] = -1
        nltry += 1
        for i in range(i0, nst):
            lflip[path_l[i]] = True
        stampid += 1
        dI = 0.0
        for i in range(i0, nst):
            l = path_l[i]
            for j in range(4):
                q = lplaqs[l, j]
                if stamp[q] != stampid:
                    stamp[q] = stampid
                    Io, In = plaq_integral(q, plinks, off, lst, vt, sstate, sclus, -7, lflip, s0)
                    dI += In - Io
        # winding change of the loop (net crossings of the a=0 planes)
        if np.random.random() < np.exp(-(g + V) * beta * dI):
            nlacc += 1
            dIacc += dI
            for i in range(i0, nst):
                s0[path_l[i]] = -s0[path_l[i]]
            nlwind += 0
        for i in range(i0, nst):
            lflip[path_l[i]] = False
    # ---------- 5. read off new F events (vertices with a state change) ----------
    nFn = 0
    for k in range(nV):
        pos = vpos[k, 0]
        l = plinks[vp[k], 0]
        prev = pos - 1 if pos > off[l] else off[l + 1] - 1
        if sstate[pos] != sstate[prev]:
            nFn += 1
    ftn = np.empty(nFn + 16, dtype=np.float64)
    fpn = np.empty(nFn + 16, dtype=np.int64)
    i = 0
    for k in range(nV):
        pos = vpos[k, 0]
        l = plinks[vp[k], 0]
        prev = pos - 1 if pos > off[l] else off[l + 1] - 1
        if sstate[pos] != sstate[prev]:
            ftn[i] = vt[k]
            fpn[i] = vp[k]
            i += 1
    mtn = np.empty(nV - nFn + 1, dtype=np.float64)
    mpn = np.empty(nV - nFn + 1, dtype=np.int64)
    i = 0
    for k in range(nV):
        pos = vpos[k, 0]
        l = plinks[vp[k], 0]
        prev = pos - 1 if pos > off[l] else off[l + 1] - 1
        if sstate[pos] == sstate[prev]:
            mtn[i] = vt[k]
            mpn[i] = vp[k]
            i += 1
    # base state consistency: s0 must equal the wrap-segment states
    for l in range(nl):
        if off[l + 1] > off[l]:
            if sstate[off[l + 1] - 1] != s0[l]:
                print("INCONSISTENT base state", l)
    # ---------- 6. global reversal (exact symmetry) ----------
    if np.random.random() < 0.5:
        for l in range(nl):
            s0[l] = -s0[l]
    stats = np.array([ntry, nacc, nill, ngiant, maxc, nseg, nltry, nlacc, nlabort, nM], dtype=np.int64)
    return ftn, fpn, nFn, stats, Ibar_old + dIacc, mtn, mpn, nV - nFn


@nb.njit(cache=True)
def ibar(s0, ft, fp, nF, plinks):
    """int_0^1 N_circ(u) du and N_circ at u=0 for the F-only configuration."""
    nl = s0.shape[0]
    npl = plinks.shape[0]
    offF, lstF, _ = build_csr(nl, ft, fp, nF, plinks)
    ptr = np.empty(4, dtype=np.int64)
    end = np.empty(4, dtype=np.int64)
    st = np.empty(4, dtype=np.int64)
    I = 0.0
    for q in range(npl):
        for j in range(4):
            l = plinks[q, j]
            ptr[j] = offF[l]
            end[j] = offF[l + 1]
            st[j] = s0[l]
        tprev = 0.0
        while True:
            tn = 2.0
            for j in range(4):
                if ptr[j] < end[j]:
                    t = ft[lstF[ptr[j]]]
                    if t < tn:
                        tn = t
            tt = tn if tn < 1.5 else 1.0
            if _circ4(st[0], st[1], st[2], st[3]):
                I += tt - tprev
            if tn > 1.5:
                break
            tprev = tt
            for j in range(4):
                if ptr[j] < end[j] and ft[lstF[ptr[j]]] == tn:
                    st[j] = -st[j]
                    ptr[j] += 1
    return I


@nb.njit(cache=True)
def states_at(s0, ft, fp, nF, plinks, us):
    out = np.empty((us.shape[0], s0.shape[0]), dtype=np.int64)
    for a in range(us.shape[0]):
        out[a, :] = s0
    for k in range(nF):
        for a in range(us.shape[0]):
            if ft[k] < us[a]:
                for j in range(4):
                    out[a, plinks[fp[k], j]] *= -1
    return out


@nb.njit(cache=True)
def check_config(s0, ft, fp, nF, plinks, star, starsgn):
    """full validity check: Gauss law of base, every F event on a circulating plaquette, periodicity.
    returns 0 if valid, else an error code."""
    nv = star.shape[0]
    for v in range(nv):
        d = 0
        for j in range(6):
            d += starsgn[v, j] * s0[star[v, j]]
        if d != 0:
            return 1
    order = np.argsort(ft[:nF])
    s = s0.copy()
    for ii in range(nF):
        k = order[ii]
        q = fp[k]
        if not _circ4(s[plinks[q, 0]], s[plinks[q, 1]], s[plinks[q, 2]], s[plinks[q, 3]]):
            return 2
        for j in range(4):
            s[plinks[q, j]] *= -1
    for l in range(s.shape[0]):
        if s[l] != s0[l]:
            return 3
    return 0
