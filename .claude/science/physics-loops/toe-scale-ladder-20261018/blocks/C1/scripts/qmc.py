"""Continuous-time worldline path integral for H = -g sum_p F_p + V sum_p n_p (Gauss sector, rho=0).

Weight of a path: g^{#kinks} * exp(-V int N_flip(tau) dtau), all nonnegative (stoquastic, g>0).
mode OPEN (0): path on [0,T] with free ends and uniform (guide-free) trial state on both ends:
   Z = sum_{s0} <1| e^{-T H} |s0>-paths ; middle ~ |psi0|^2 as T -> inf.  Moves: pair insert/remove,
   kink shift, single-kink end moves at tau=0 and tau=T (these change every flip-count class).
mode PERIODIC (1): trace on the circle [0,beta), moves pair insert/remove + shift only (local; conserves
   the net signed flip count of every plaquette -> class-restricted; used as an ergodicity control).
Data: s0 = link state at tau=0+, kt[p, :kc[p]] = sorted kink times of plaquette p.
"""
import numpy as np
from numba import njit

INF = 1e300


@njit(cache=True)
def seed_rng(s):
    np.random.seed(s)


@njit(cache=True)
def cnt_lt(kt, kc, p, t):
    lo = 0
    hi = kc[p]
    while lo < hi:
        mid = (lo + hi) >> 1
        if kt[p, mid] < t:
            lo = mid + 1
        else:
            hi = mid
    return lo


@njit(cache=True)
def cnt_le(kt, kc, p, t):
    lo = 0
    hi = kc[p]
    while lo < hi:
        mid = (lo + hi) >> 1
        if kt[p, mid] <= t:
            lo = mid + 1
        else:
            hi = mid
    return lo


@njit(cache=True)
def link_state(s0, kt, kc, lplaqs, l, t):
    par = 0
    for j in range(4):
        par += cnt_lt(kt, kc, lplaqs[l, j], t)
    if par & 1:
        return -s0[l]
    return s0[l]


@njit(cache=True)
def circ_at(s0, kt, kc, lplaqs, plinks, psign, p, t):
    c = 0
    for k in range(4):
        c += psign[k] * link_state(s0, kt, kc, lplaqs, plinks[p, k], t)
    return c


@njit(cache=True)
def next_evt(kt, kc, nbh, nnb, p, t, per, beta):
    """earliest kink time > t among nbh(p); periodic: wraps (returns value in (t, t+beta]) ; INF if none."""
    best = INF
    for j in range(nnb[p]):
        q = nbh[p, j]
        i = cnt_le(kt, kc, q, t)
        if i < kc[q]:
            if kt[q, i] < best:
                best = kt[q, i]
        elif per and kc[q] > 0:
            if kt[q, 0] + beta < best:
                best = kt[q, 0] + beta
    return best


@njit(cache=True)
def prev_evt(kt, kc, nbh, nnb, p, t, per, beta):
    best = -INF
    for j in range(nnb[p]):
        q = nbh[p, j]
        i = cnt_lt(kt, kc, q, t)
        if i > 0:
            if kt[q, i - 1] > best:
                best = kt[q, i - 1]
        elif per and kc[q] > 0:
            if kt[q, kc[q] - 1] - beta > best:
                best = kt[q, kc[q] - 1] - beta
    return best


@njit(cache=True)
def ins_kink(kt, kc, p, t):
    n = kc[p]
    if n >= kt.shape[1]:
        return False
    i = cnt_lt(kt, kc, p, t)
    for j in range(n, i, -1):
        kt[p, j] = kt[p, j - 1]
    kt[p, i] = t
    kc[p] = n + 1
    return True


@njit(cache=True)
def del_kink(kt, kc, p, i):
    n = kc[p]
    for j in range(i, n - 1):
        kt[p, j] = kt[p, j + 1]
    kc[p] = n - 1


@njit(cache=True)
def delta_toggle(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, ta, tb, buf):
    """int_{ta}^{tb} [N_flip(with p's links negated) - N_flip(current)] dtau, assuming p's links are constant
    on (ta,tb) and 0 <= ta < tb <= period (no wrap)."""
    if tb <= ta:
        return 0.0
    tot = 0.0
    for jq in range(1, nnb[p]):
        q = nbh[p, jq]
        # event times in (ta,tb) of plaquettes touching q's links
        m = 0
        for jr in range(nnb[q]):
            r = nbh[q, jr]
            i0 = cnt_le(kt, kc, r, ta)
            i1 = cnt_lt(kt, kc, r, tb)
            for i in range(i0, i1):
                buf[m] = kt[r, i]
                m += 1
        b = np.sort(buf[:m])
        prev = ta
        for k in range(m + 1):
            nxt = b[k] if k < m else tb
            if nxt > prev:
                tm = 0.5 * (prev + nxt)
                c = 0
                ct = 0
                for kk in range(4):
                    l = plinks[q, kk]
                    sl = psign[kk] * link_state(s0, kt, kc, lplaqs, l, tm)
                    c += sl
                    inp = False
                    for k2 in range(4):
                        if plinks[p, k2] == l:
                            inp = True
                    ct += -sl if inp else sl
                f0 = 1.0 if (c == 4 or c == -4) else 0.0
                f1 = 1.0 if (ct == 4 or ct == -4) else 0.0
                tot += (f1 - f0) * (nxt - prev)
            prev = nxt
    return tot


@njit(cache=True)
def delta_toggle_cyc(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, ta, tb, beta, buf):
    """cyclic interval (ta, tb) with 0<=ta<beta, ta<tb<=ta+beta."""
    if tb <= beta:
        return delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, ta, tb, buf)
    return (delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, ta, beta, buf)
            + delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, 0.0, tb - beta, buf))


@njit(cache=True)
def flip_s0(s0, plinks, p):
    for k in range(4):
        s0[plinks[p, k]] = -s0[plinks[p, k]]


@njit(cache=True)
def sweep(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, g, V, T, per, nmoves, buf, stats, pr):
    """stats[0..9]: tried/accepted for insert, remove, shift, end-insert, end-remove (pairs)."""
    npl = plinks.shape[0]
    useV = V != 0.0
    ok = True
    for _ in range(nmoves):
        r = np.random.random()
        p = np.random.randint(npl)
        if r < pr[0]:  # ---------------- pair insertion
            stats[0] += 1
            t1 = np.random.random() * T
            c = circ_at(s0, kt, kc, lplaqs, plinks, psign, p, t1)
            if c != 4 and c != -4:
                continue
            tb = next_evt(kt, kc, nbh, nnb, p, t1, per, T)
            if tb >= INF:
                tb = (t1 + T) if per else T
            elif (not per) and tb > T:
                tb = T
            t2 = t1 + np.random.random() * (tb - t1)
            ratio = g * g * T * (tb - t1) / (kc[p] + 2)
            if useV:
                if per:
                    ratio *= np.exp(-V * delta_toggle_cyc(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, t1, t2, T, buf))
                else:
                    ratio *= np.exp(-V * delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, t1, t2, buf))
            if np.random.random() < ratio:
                if per and t2 >= T:
                    t2 -= T
                    flip_s0(s0, plinks, p)
                if not ins_kink(kt, kc, p, t1):
                    ok = False
                    break
                if not ins_kink(kt, kc, p, t2):
                    ok = False
                    break
                stats[1] += 1
        elif r < pr[1]:  # ---------------- pair removal
            stats[2] += 1
            n = kc[p]
            if n < 2:
                continue
            k = np.random.randint(n)
            t1 = kt[p, k]
            if k + 1 < n:
                t2 = kt[p, k + 1]
                k2 = k + 1
            elif per:
                t2 = kt[p, 0] + T
                k2 = 0
            else:
                continue
            # no other neighbourhood event strictly between t1 and t2
            bad = False
            for j in range(1, nnb[p]):
                q = nbh[p, j]
                i = cnt_le(kt, kc, q, t1)
                if i < kc[q]:
                    if kt[q, i] < t2:
                        bad = True
                        break
                elif per and kc[q] > 0:
                    if kt[q, 0] + T < t2:
                        bad = True
                        break
            if bad:
                continue
            # segment end after removal: next event after t2 excluding the pair
            tb = INF
            for j in range(1, nnb[p]):
                q = nbh[p, j]
                t2m = t2 - T if t2 >= T else t2
                i = cnt_le(kt, kc, q, t2m)
                if i < kc[q]:
                    v = kt[q, i] + (T if t2 >= T else 0.0)
                    if v < tb:
                        tb = v
                elif per and kc[q] > 0:
                    v = kt[q, 0] + T + (T if t2 >= T else 0.0)
                    if v < tb:
                        tb = v
            if n > 2:
                if per:
                    k3 = (k2 + 1) % n
                    v = kt[p, k3]
                    while v <= t2:
                        v += T
                    if v < tb:
                        tb = v
                elif k + 2 < n:
                    if kt[p, k + 2] < tb:
                        tb = kt[p, k + 2]
            if per:
                if tb > t1 + T:
                    tb = t1 + T
            elif tb > T:
                tb = T
            ratio = n / (g * g * T * (tb - t1))
            if useV:
                if per:
                    ratio *= np.exp(-V * delta_toggle_cyc(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, t1, t2, T, buf))
                else:
                    ratio *= np.exp(-V * delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, t1, t2, buf))
            if np.random.random() < ratio:
                if k2 > k:
                    del_kink(kt, kc, p, k2)
                    del_kink(kt, kc, p, k)
                else:  # wrapped pair (k = n-1, k2 = 0)
                    del_kink(kt, kc, p, k)
                    del_kink(kt, kc, p, 0)
                    flip_s0(s0, plinks, p)
                stats[3] += 1
        elif r < pr[2]:  # ---------------- shift one kink
            stats[4] += 1
            n = kc[p]
            if n == 0:
                continue
            k = np.random.randint(n)
            t = kt[p, k]
            ta = prev_evt(kt, kc, nbh, nnb, p, t, per, T)
            tb = next_evt(kt, kc, nbh, nnb, p, t, per, T)
            if per:
                if ta <= -INF or tb >= INF or tb - ta >= T:
                    continue  # lone kink in its neighbourhood: skip (control mode only)
            else:
                if ta < 0.0:
                    ta = 0.0
                if tb > T:
                    tb = T
            tn = ta + np.random.random() * (tb - ta)
            ratio = 1.0
            if useV:
                lo = t if tn > t else tn
                hi = tn if tn > t else t
                if per:
                    lo2 = lo % T
                    d = delta_toggle_cyc(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, lo2, lo2 + (hi - lo), T, buf)
                else:
                    d = delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, lo, hi, buf)
                ratio = np.exp(-V * d)
            if np.random.random() < ratio:
                del_kink(kt, kc, p, k)
                if per:
                    # crossing tau=0 toggles s0 for p
                    if tn < 0.0:
                        tn += T
                        flip_s0(s0, plinks, p)
                    elif tn >= T:
                        tn -= T
                        flip_s0(s0, plinks, p)
                ins_kink(kt, kc, p, tn)
                stats[5] += 1
        else:  # ---------------- end moves (open only)
            if per:
                continue
            atstart = np.random.random() < pr[3]
            ins = np.random.random() < 0.5
            if atstart:
                tf = next_evt(kt, kc, nbh, nnb, p, -1.0, 0, T)
                if tf > T:
                    tf = T
                if ins:
                    stats[6] += 1
                    c = circ_at(s0, kt, kc, lplaqs, plinks, psign, p, 0.0)
                    if c != 4 and c != -4:
                        continue
                    t = np.random.random() * tf
                    ratio = g * tf
                    if useV:
                        ratio *= np.exp(-V * delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, 0.0, t, buf))
                    if np.random.random() < ratio:
                        flip_s0(s0, plinks, p)
                        if not ins_kink(kt, kc, p, t):
                            ok = False
                            break
                        stats[7] += 1
                else:
                    stats[8] += 1
                    if kc[p] == 0 or kt[p, 0] != tf:
                        continue
                    t = kt[p, 0]
                    # first event after 0 in post-removal configuration
                    tf2 = T
                    for j in range(1, nnb[p]):
                        q = nbh[p, j]
                        if kc[q] > 0 and kt[q, 0] < tf2:
                            tf2 = kt[q, 0]
                    if kc[p] > 1 and kt[p, 1] < tf2:
                        tf2 = kt[p, 1]
                    ratio = 1.0 / (g * tf2)
                    if useV:
                        ratio *= np.exp(-V * delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, 0.0, t, buf))
                    if np.random.random() < ratio:
                        del_kink(kt, kc, p, 0)
                        flip_s0(s0, plinks, p)
                        stats[9] += 1
            else:
                tl = prev_evt(kt, kc, nbh, nnb, p, T + 1.0, 0, T)
                if tl < 0.0:
                    tl = 0.0
                if ins:
                    stats[6] += 1
                    c = circ_at(s0, kt, kc, lplaqs, plinks, psign, p, T)
                    if c != 4 and c != -4:
                        continue
                    t = tl + np.random.random() * (T - tl)
                    ratio = g * (T - tl)
                    if useV:
                        ratio *= np.exp(-V * delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, t, T, buf))
                    if np.random.random() < ratio:
                        if not ins_kink(kt, kc, p, t):
                            ok = False
                            break
                        stats[7] += 1
                else:
                    stats[8] += 1
                    n = kc[p]
                    if n == 0 or kt[p, n - 1] != tl:
                        continue
                    t = kt[p, n - 1]
                    tl2 = 0.0
                    for j in range(1, nnb[p]):
                        q = nbh[p, j]
                        if kc[q] > 0 and kt[q, kc[q] - 1] > tl2:
                            tl2 = kt[q, kc[q] - 1]
                    if n > 1 and kt[p, n - 2] > tl2:
                        tl2 = kt[p, n - 2]
                    ratio = 1.0 / (g * (T - tl2))
                    if useV:
                        ratio *= np.exp(-V * delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, t, T, buf))
                    if np.random.random() < ratio:
                        del_kink(kt, kc, p, n - 1)
                        stats[9] += 1
    return ok


@njit(cache=True)
def states_at(s0, kt, kc, lplaqs, times, out):
    """out[i, l] = link state at times[i]."""
    nl = s0.shape[0]
    for i in range(times.shape[0]):
        t = times[i]
        for l in range(nl):
            out[i, l] = link_state(s0, kt, kc, lplaqs, l, t)


@njit(cache=True)
def kinks_in(kt, kc, ta, tb):
    n = 0
    for p in range(kc.shape[0]):
        n += cnt_lt(kt, kc, p, tb) - cnt_le(kt, kc, p, ta)
    return n


@njit(cache=True)
def gauss_ok(sig, tail, head, nv):
    d = np.zeros(nv, dtype=np.int64)
    for l in range(sig.shape[0]):
        d[tail[l]] += sig[l]
        d[head[l]] -= sig[l]
    for v in range(nv):
        if d[v] != 0:
            return False
    return True


@njit(cache=True)
def path_valid(s0, kt, kc, lplaqs, plinks, psign, T):
    """Replay certificate: every kink acts on a flippable plaquette (state just before the kink)."""
    for p in range(kc.shape[0]):
        for i in range(kc[p]):
            c = circ_at(s0, kt, kc, lplaqs, plinks, psign, p, kt[p, i])  # cnt_lt excludes the kink itself
            if c != 4 and c != -4:
                return False
            if i > 0 and kt[p, i] <= kt[p, i - 1]:
                return False
            if kt[p, i] < 0.0 or kt[p, i] >= T:
                return False
    return True


@njit(cache=True)
def delta_toggle_fast(s0, kt, kc, lplaqs, plinks, psign, nbh, nnb, p, ta, tb, buf):
    """Same quantity as delta_toggle, computed with incremental link states (checked equal in tests)."""
    if tb <= ta:
        return 0.0
    tot = 0.0
    tmid0 = ta  # states evaluated just after ta: no events of q's links exactly at ta except possibly p's own
    for jq in range(1, nnb[p]):
        q = nbh[p, jq]
        st = np.empty(4, dtype=np.int64)
        inp = np.zeros(4, dtype=np.bool_)
        m = 0
        for kk in range(4):
            l = plinks[q, kk]
            for k2 in range(4):
                if plinks[p, k2] == l:
                    inp[kk] = True
            # state just after ta: count kinks <= ta
            par = 0
            for j in range(4):
                r = lplaqs[l, j]
                par += cnt_le(kt, kc, r, tmid0)
            st[kk] = -s0[l] if (par & 1) else s0[l]
            if not inp[kk]:
                for j in range(4):
                    r = lplaqs[l, j]
                    i0 = cnt_le(kt, kc, r, ta)
                    i1 = cnt_lt(kt, kc, r, tb)
                    for i in range(i0, i1):
                        buf[2 * m] = kt[r, i]
                        buf[2 * m + 1] = kk
                        m += 1
        # sort events by time (insertion sort; m is small)
        for a in range(1, m):
            tv = buf[2 * a]
            kv = buf[2 * a + 1]
            b = a - 1
            while b >= 0 and buf[2 * b] > tv:
                buf[2 * b + 2] = buf[2 * b]
                buf[2 * b + 3] = buf[2 * b + 1]
                b -= 1
            buf[2 * b + 2] = tv
            buf[2 * b + 3] = kv
        prev = ta
        for e in range(m + 1):
            nxt = buf[2 * e] if e < m else tb
            if nxt > prev:
                c = 0
                ct = 0
                for kk in range(4):
                    sl = psign[kk] * st[kk]
                    c += sl
                    ct += -sl if inp[kk] else sl
                f0 = 1.0 if (c == 4 or c == -4) else 0.0
                f1 = 1.0 if (ct == 4 or ct == -4) else 0.0
                tot += (f1 - f0) * (nxt - prev)
            if e < m:
                kk = int(buf[2 * e + 1])
                st[kk] = -st[kk]
            prev = nxt if nxt > prev else prev
    return tot
