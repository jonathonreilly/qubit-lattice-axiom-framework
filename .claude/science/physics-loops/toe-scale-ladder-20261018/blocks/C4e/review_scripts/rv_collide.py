"""Reviewer re-derivation of the C4e collision table (pair+single, head-on pairs)."""
import os
import rv_core as C

HERE = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(HERE, 'logs', 'collide.txt'), 'w')
ck = C.Check(f)

P = frozenset([(0, 0, 0), (1, 1, 0)])  # moves +e3
Q = frozenset([(0, 0, 0), (1, -1, 0)])  # moves -e3


def split_pairs(c):
    """decompose into isolated face pairs + rest (greedy by cheb<=1 components)"""
    c = set(c)
    comps = []
    while c:
        x = c.pop()
        comp = {x}
        st = [x]
        while st:
            y = st.pop()
            for z in list(c):
                if C.cheb(y, z) <= 2:
                    c.remove(z)
                    comp.add(z)
                    st.append(z)
        comps.append(frozenset(comp))
    return comps


# pair + single at (a,b,3)
trans = refl = other = 0
lags = {}
for a in range(-3, 5):
    for b in range(-3, 5):
        s = (a, b, 3)
        c = P | {s}
        T = 40
        cur = c
        for _ in range(T):
            cur = C.U(cur)
        free = C.tr(P, (0, 0, T)) | {s}
        if cur == free:
            trans += 1
            continue
        comps = split_pairs(cur)
        singles = [k for k in comps if len(k) == 1]
        pairs = [k for k in comps if len(k) == 2]
        if singles == [frozenset([s])] and len(pairs) == 1:
            pr = sorted(pairs[0])
            rho = C.sub(pr[1], pr[0])
            if rho in [(1, -1, 0), (-1, 1, 0)] and pr[0][2] < 0:
                refl += 1
                # lag relative to a pair that turned at z=... record z after T ticks
                lags[(a, b)] = pr[0][2]
                continue
        other += 1
ck(trans == 48 and refl == 16 and other == 0,
   f"pair{{0,e1+e2}} + single at (a,b,3), a,b in [-3,4]: transparent {trans}, reflected (single unmoved, pair now (1,-1,0) moving -e3) {refl}, other {other} (claim 48/16)")
ck.info(f"   reflected cases: final z of pair after 40 ticks: {lags}")

# head-on pairs, lateral offsets [-2,2]^2, gaps 5,6
npass = 0
nrefl = 0
noth = 0
shifts = set()
tot = 0
for gap in (5, 6):
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            Q0 = C.tr(Q, (dx, dy, gap))
            c = P | Q0
            if len(c) != 4:
                continue
            tot += 1
            T = 40
            cur = C.U(c)
            for _ in range(T - 1):
                cur = C.U(cur)
            comps = split_pairs(cur)
            prs = [sorted(k) for k in comps if len(k) == 2]
            if len(prs) != 2 or len(comps) != 2:
                noth += 1
                continue
            up = [p for p in prs if C.sub(p[1], p[0]) in [(1, 1, 0), (-1, -1, 0)]]
            dn = [p for p in prs if C.sub(p[1], p[0]) in [(1, -1, 0), (-1, 1, 0)]]
            if len(up) == 1 and len(dn) == 1 and up[0][0][2] > dn[0][0][2]:
                npass += 1
                # shift relative to free motion
                fu = sorted(C.tr(P, (0, 0, T)))
                fd = sorted(C.tr(Q0, (0, 0, -T)))
                su = C.sub(up[0][0], fu[0])
                sd = C.sub(dn[0][0], fd[0])
                shifts.add((su, sd))
            else:
                nrefl += 1
ms = max(max(map(abs, a + b)) for a, b in shifts) if shifts else None
ck(npass == tot and noth == 0, f"head-on (1,1,0) up and (1,-1,0) down, offsets [-2,2]^2, gaps 5,6: {tot} non-overlapping cases, {npass} pass through, {nrefl} reflect, {noth} other (claim all 50 pass)")
ck(ms is not None and ms <= 2, f"   pass-through position shifts (up, down) set: {sorted(shifts)}; max |shift| component {ms} (claim 0-2)")
ck.total()
