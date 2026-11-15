"""checks/tg1b_ledger.py -- repair round for TGAUGE_PRICE.md (session 25).

Criteria: checks/tg1b_criteria.md, written BEFORE this script. tg1_criteria.md NOT amended;
tg1_price.py / tg1_out.txt / tg1_err.txt kept unaltered with their three FAILs.

B0  non-vacuity: T_res != 0, D(S) != 0, mu_flat != 0, mu_pt != 0
B1  the closed ledger on ONE source:
      (i) d*C(j) = D(S);  (ii) D(S) root-supported, neutral;  (iii) M = P + T_res;
      (iv) dP := n^2 <C(j), dmu> = 0;  (v) dM := n^2 <Chat, dmu> = -T_res, i.e. rho = 1
B2  DESIGNED-FAIL CONTROL 1: mu_root outside Lambda_* -> dP != 0 AND rho_root != 1
B3  the repaired estimator: rho_est closed forms, and rho_tv in [1,2] decreasing in k
B4  SOURCE-DISAGREES: Q_str^{(0->l)}(d mu) = d(A^{(0->l)}mu) and != d(ev^{(0->l)}mu)
B5  DESIGNED-FAIL CONTROL 2: flat longitudinal multiplicity -> mass assertion + B4(i) must FAIL
"""
from fractions import Fraction as F
from itertools import permutations, product
import sys
sys.path.insert(0, "")

L = 3
OFFH = (L - 1) // 2


def off(l):
    return (L ** l - 1) // 2


def avatar(Y, l, d):
    return tuple(off(l) + L ** l * Y[i] for i in range(d))


def relevel(Y, l, m, d):
    s = (off(l) - off(m)) // L ** m
    return tuple(s + L ** (l - m) * Y[i] for i in range(d))


def sites(side, d):
    return list(product(range(side), repeat=d))


def shift(z, mu, s, side, d):
    w = list(z)
    w[mu] = (w[mu] + s) % side
    return tuple(w)


def d_of(f, side, d):
    out = {}
    cand = set(f.keys())
    for Y in list(cand):
        for mu in range(d):
            cand.add(shift(Y, mu, -1, side, d))
    for Y in cand:
        for mu in range(d):
            val = f.get(shift(Y, mu, 1, side, d), F(0)) - f.get(Y, F(0))
            if val:
                out[(Y, mu)] = val
    return out


def dstar(v, side, d):
    out, cand = {}, set()
    for (z, mu) in v:
        cand.add(z)
        cand.add(shift(z, mu, 1, side, d))
    for z in cand:
        tot = F(0)
        for mu in range(d):
            tot += v.get((shift(z, mu, -1, side, d), mu), F(0)) - v.get((z, mu), F(0))
        if tot:
            out[z] = tot
    return out


def pair(v, w):
    return sum(val * w.get(key, F(0)) for key, val in v.items())


def add(a, b, c=F(1)):
    for key, val in b.items():
        a[key] = a.get(key, F(0)) + c * val
    return a


# ----------------------------------------------------------- straight average, with the control hook
def mult_table(flat=False):
    """t -> #{(r,j) in [0,L)^2 : r + j = t}; the control replaces it by the flat table."""
    if flat:
        return {t: 1 for t in range(2 * L - 1)}
    return {t: L - abs(t - (L - 1)) for t in range(2 * L - 1)}


def mass_ok(tm):
    """kernel mass assertion: the longitudinal multiplicities must sum to L^2."""
    return sum(tm.values()) == L ** 2


def qstr_fwd(w, side_l, d, tm):
    out = {}
    side_u = side_l // L
    for (z, m), v in w.items():
        base = [z[i] // L for i in range(d)]
        t0 = z[m] % L
        for t in (t0, t0 + L):
            if t > 2 * L - 2:
                continue
            Y = list(base)
            Y[m] = ((z[m] - t) // L) % side_u
            key = (tuple(Y), m)
            out[key] = out.get(key, F(0)) + v * F(tm[t], L ** d)
    return {k: v for k, v in out.items() if v != 0}


def qstr_T(psi, side_up, d):
    out = {}
    side_l = side_up * L
    for (Y, m), v in psi.items():
        for r in product(range(L), repeat=d):
            for j in range(L):
                z = [(L * Y[i] + r[i]) % side_l for i in range(d)]
                z[m] = (z[m] + j) % side_l
                key = (tuple(z), m)
                out[key] = out.get(key, F(0)) + v / L ** d
    return {k: v for k, v in out.items() if v != 0}


def qstr_T_chain(psi, i, sl, d):
    cur = psi
    for lvl in range(i, 0, -1):
        cur = qstr_T(cur, sl[lvl], d)
    return cur


def qstr_fwd_chain(v, i, sl, d, tm):
    cur = v
    for lvl in range(i):
        cur = qstr_fwd(cur, sl[lvl], d, tm)
    return cur


# ----------------------------------------------------------- h_i
def axial(a, b, order):
    out, z = [], list(a)
    for c in order:
        while z[c] != b[c]:
            if b[c] > z[c]:
                out.append((tuple(z), c, 1)); z[c] += 1
            else:
                w = list(z); w[c] -= 1; out.append((tuple(w), c, -1)); z[c] -= 1
    return out


def build_HT(d):
    perms = list(permutations(range(d)))
    W = F(1, len(perms) * L ** d)
    HT = {}
    for sig in perms:
        for o in product(range(-OFFH, OFFH + 1), repeat=d):
            for (z, c, s) in axial([0] * d, list(o), sig):
                HT[(z, c)] = HT.get((z, c), F(0)) + s * W
    return {k: v for k, v in HT.items() if v != 0}


def h_fwd(w, Y, HT, side_i, d):
    tot = F(0)
    for (z, c), wt in HT.items():
        tot += wt * w.get((tuple((L * Y[i] + OFFH + z[i]) % side_i for i in range(d)), c), F(0))
    return tot


def h_T(f, HT, side_i, d):
    out = {}
    for Y, a in f.items():
        for (z, c), wt in HT.items():
            key = (tuple((L * Y[i] + OFFH + z[i]) % side_i for i in range(d)), c)
            out[key] = out.get(key, F(0)) + a * wt
    return {k: v for k, v in out.items() if v != 0}


def Phi_all(v, Xs, k, HT, sl, d, tm):
    tot = {X: F(0) for X in Xs}
    cur = v
    for i in range(k):
        if i:
            cur = qstr_fwd(cur, sl[i - 1], d, tm)
        for X in Xs:
            tot[X] += h_fwd(cur, relevel(X, k, i + 1, d), HT, sl[i], d)
    return tot


def A_blk_sparse(mu, l, sl, d):
    out = {}
    side_u = sl[l]
    for z, v in mu.items():
        Y = tuple((z[i] // L ** l) % side_u for i in range(d))
        out[Y] = out.get(Y, F(0)) + v / L ** (d * l)
    return {k: v for k, v in out.items() if v != 0}


def ev_pull(mu, l, sl, d):
    return {Y: mu.get(avatar(Y, l, d), F(0)) for Y in sites(sl[l], d)}


def sigma5(num, den):
    t = F(num, den)
    if t >= 1:
        return F(0)
    return 1 - (10 * t ** 3 - 15 * t ** 4 + 6 * t ** 5)


def per(a, side):
    a %= side
    return min(a, side - a)


def chi5(w, cX, n, side, d):
    v = F(1)
    for nu in range(d):
        v *= sigma5(per(w[nu] - cX[nu], side), n)
        if v == 0:
            return F(0)
    return v


def rng(seed):
    x = seed

    def nxt():
        nonlocal x
        x = (1103515245 * x + 12345) % (1 << 31)
        return F((x % 199) - 99, 1 + (x // 199) % 17)
    return nxt


# ================================================================= run
print("tg1b: TGAUGE_PRICE session 25 repair round.")
print("criteria: checks/tg1b_criteria.md (written first). tg1 criteria and outputs untouched.")
TM = mult_table()
print(f"kernel mass assertion on the true multiplicity table: sum_t mult(t) = {sum(TM.values())} "
      f"== L^2 = {L**2}: {mass_ok(TM)}")
assert mass_ok(TM), "true multiplicity table failed its own mass assertion"
verd = {}
rho_tv_store = {}

for tag, d, k, T, seed in [("Q1 (d=2,k=2,T=3)", 2, 2, 3, 23),
                           ("Q2 (d=2,k=3,T=2)", 2, 3, 2, 29),
                           ("Q3 (d=4,k=2,T=2)", 4, 2, 2, 31)]:
    n = L ** k
    sl = {l: T * L ** (k - l) for l in range(k + 1)}
    HT = build_HT(d)
    Xs = sites(sl[k], d)
    X0 = tuple(0 for _ in range(d))
    X1 = tuple(([1] + [0] * (d - 1))[i] for i in range(d))
    cX0, cX1 = avatar(X0, k, d), avatar(X1, k, d)
    print(f"\n{'='*78}\n=== {tag}: n={n}, level-0 side={sl[0]}, {len(Xs)} boxes, |HT|={len(HT)} ===")

    # ---------- the single source: a level-(k-1) path from X0's avatar to X1's ----------
    lj = k - 1
    Y0, Y1 = relevel(X0, k, lj, d), relevel(X1, k, lj, d)
    j = {}
    zz = list(Y0)
    for nu_ in range(d):
        while zz[nu_] != Y1[nu_]:
            stp = 1 if Y1[nu_] > zz[nu_] else -1
            w = list(zz)
            if stp < 0:
                w[nu_] -= 1
            j[(tuple(x % sl[lj] for x in w), nu_)] = F(-stp)
            zz[nu_] += stp
    dsj = dstar(j, sl[lj], d)
    DS = {}
    for Y, val in dsj.items():
        DS[avatar(Y, lj, d)] = DS.get(avatar(Y, lj, d), F(0)) + val
    DS = {z: v for z, v in DS.items() if v != 0}
    rootset = set(avatar(X, k, d) for X in Xs)
    b1ii = all(z in rootset for z in DS) and sum(DS.values()) == 0
    print(f"B1(ii) D(S) root-supported & neutral: {b1ii}  (supp {sorted(DS)}, sum {sum(DS.values())})")

    # ---------- C(j), Chat_def, Chat ----------
    Cj = dict(qstr_T_chain(j, lj, sl, d))
    for i in range(lj):
        up = {}
        for Y, val in dsj.items():
            Yi = relevel(Y, lj, i + 1, d)
            up[Yi] = up.get(Yi, F(0)) + val
        Cj = add(Cj, qstr_T_chain(h_T(up, HT, sl[i], d), i, sl, d), F(-1))
    dsC = dstar(Cj, sl[0], d)
    keys = set(dsC) | set(DS)
    b1i = all(dsC.get(z, F(0)) == DS.get(z, F(0)) for z in keys)
    print(f"B1(i)  d*C(j) == D(S) at all {len(keys)} sites: {b1i}")

    Cdef = {}
    for i in range(k):
        R = {}
        for X in Xs:
            val = DS.get(avatar(X, k, d), F(0))
            if val:
                Y = relevel(X, k, i + 1, d)
                R[Y] = R.get(Y, F(0)) + val
        Cdef = add(Cdef, qstr_T_chain(h_T(R, HT, sl[i], d), i, sl, d))
    Chat = add(dict(Cj), Cdef)
    verd[f"B1-i/{tag}"] = b1i
    verd[f"B1-ii/{tag}"] = b1ii

    # ---------- the test fields ----------
    nxt = rng(seed)
    x0_blk = {}
    for q in range(3):
        z = tuple((cX0[nu] + ((q + nu) % ((n + 1) // 2))) % sl[0] for nu in range(d))
        for m in range(d):
            x0_blk[(z, m)] = nxt()
    x0_mix = dict(x0_blk)
    for q in range(5):
        z = tuple((5 * q + 7 * nu + 2) % sl[0] for nu in range(d))
        for m in range(d):
            x0_mix[(z, m)] = nxt()

    for ftag, x0 in (("one-block", x0_blk), ("mixed", x0_mix)):
        Ph = Phi_all(x0, Xs, k, HT, sl, d, TM)
        nu = {X: -v for X, v in Ph.items() if v != 0}
        Tres = n ** 2 * sum(DS.get(avatar(X, k, d), F(0)) * Ph[X] for X in Xs)
        P = n ** 2 * pair(Cj, x0)
        M = n ** 2 * pair(Chat, x0)
        print(f"\n--- field {ftag}: #(nu != 0) = {len(nu)};  T_res = {Tres}  "
              f"({'NONZERO' if Tres != 0 else 'ZERO'})")
        print(f"B1(iii) M = {M};  P + T_res = {P + Tres};  equal: {M == P + Tres}   (P = {P})")
        b0 = (Tres != 0) and bool(DS)
        verd[f"B1-iii/{tag}/{ftag}"] = (M == P + Tres)

        scale = 1 / (1 - F(1, L ** (d * k)))
        mu_flat, mu_pt, mu_root = {}, {}, {}
        for X, val in nu.items():
            cX = avatar(X, k, d)
            for s in product(range(L ** k), repeat=d):
                z = tuple((L ** k * X[i] + s[i]) % sl[0] for i in range(d))
                if z != cX:
                    mu_flat[z] = mu_flat.get(z, F(0)) + val * scale
            zp = list(cX); zp[0] = (zp[0] + 1) % sl[0]
            mu_pt[tuple(zp)] = mu_pt.get(tuple(zp), F(0)) + val * L ** (d * k)
            mu_root[cX] = mu_root.get(cX, F(0)) - val * scale
        b0 = b0 and bool(mu_flat) and bool(mu_pt)
        print(f"B0      non-vacuity (T_res != 0, D(S) != 0, mu_flat != 0, mu_pt != 0): {b0}")
        verd[f"B0/{tag}/{ftag}"] = b0

        res = {}
        for mtag, mu in (("mu_flat", mu_flat), ("mu_pt", mu_pt), ("mu_root", mu_root)):
            dmu = d_of(mu, sl[0], d)
            dP = n ** 2 * pair(Cj, dmu)
            dM = n ** 2 * pair(Chat, dmu)
            x0g = add(dict(x0), dmu)
            Phg = Phi_all(x0g, Xs, k, HT, sl, d, TM)
            Tnew = n ** 2 * sum(DS.get(avatar(X, k, d), F(0)) * Phg[X] for X in Xs)
            Mnew = n ** 2 * pair(Chat, x0g)
            rho = abs(dM) / abs(Tres) if Tres else None
            res[mtag] = (dP, dM, rho)
            print(f"B1(iv/v) {mtag:8s}: dP = {dP};  dM = {dM};  -T_res = {-Tres};  "
                  f"rho = {rho};  T_res(gauged) = {Tnew};  M(gauged) = {Mnew}  "
                  f"(== P: {Mnew == P})")
        verd[f"B1-iv/{tag}/{ftag}"] = (res["mu_flat"][0] == 0 and res["mu_pt"][0] == 0)
        verd[f"B1-v/{tag}/{ftag}"] = (res["mu_flat"][1] == -Tres and res["mu_pt"][1] == -Tres)
        fired = (res["mu_root"][0] != 0) and (res["mu_root"][2] != 1)
        print(f"B2      CONTROL 1 (mu_root outside Lambda_*): dP = {res['mu_root'][0]} (!= 0: "
              f"{res['mu_root'][0] != 0}), rho_root = {res['mu_root'][2]} (!= 1: "
              f"{res['mu_root'][2] != 1}) -> control "
              f"{'FIRES (PASS of the control)' if fired else 'DOES NOT FIRE -> B1(v) has no power over Lambda_*'}")
        verd[f"B2/{tag}/{ftag}"] = fired

        # ---------------- B3: the repaired estimator ----------------
        if ftag == "one-block":
            osc1 = F(0)
            for X in Xs:
                for m in range(d):
                    osc1 = max(osc1, abs(nu.get(X, F(0)) - nu.get(shift(X, m, 1, sl[k], d), F(0))))
            tent = {}
            if (2 * n - 1) ** d <= 200000:
                Psi = {}
                for X in nu:
                    cX = avatar(X, k, d)
                    for w in product(*[range(cX[i] - n + 1, cX[i] + n) for i in range(d)]):
                        ww = tuple(x % sl[0] for x in w)
                        cv = chi5(ww, cX, n, sl[0], d)
                        if cv:
                            Psi[ww] = Psi.get(ww, F(0)) + nu[X] * cv
                for l in range(k):
                    tent[l] = sum(abs(v) for v in
                                  d_of(ev_pull(Psi, l, sl, d), sl[l], d).values())
            okf, okp, oktv = True, True, True
            for mtag, mu in (("mu_flat", mu_flat), ("mu_pt", mu_pt)):
                for l in range(k):
                    tv = sum(abs(v) for v in d_of(A_blk_sparse(mu, l, sl, d), sl[l], d).values())
                    denom = F(n, L ** l) ** (d - 1) * osc1
                    rho_est = tv / denom
                    if mtag == "mu_flat":
                        want = 2 * d * scale * (1 + F(1, L ** l) * F(1, n ** (d - 1)))
                        okf = okf and (rho_est == want)
                        rtv = tv / tent[l] if tent.get(l) else None
                        if rtv is not None:
                            rho_tv_store[(tag, l)] = rtv
                            oktv = oktv and (1 <= rtv <= 2)
                        print(f"B3      mu_flat l={l}: rho_est = {rho_est} = {float(rho_est)}; "
                              f"want {want} = {float(want)}: {rho_est == want};  "
                              f"rho_tv = {rtv} ({float(rtv) if rtv is not None else 'skipped'})")
                    else:
                        want = 2 * d * L ** (k - l)
                        okp = okp and (rho_est == want)
                        print(f"B3      mu_pt   l={l}: rho_est = {rho_est} = {float(rho_est)}; "
                              f"want 2d*L^(k-l) = {want}: {rho_est == want}")
            verd[f"B3-i/{tag}"] = okf
            verd[f"B3-ii/{tag}"] = okp
            if tent:
                verd[f"B3-iii-range/{tag}"] = oktv

    # ---------------- B4 / B5 ----------------
    nxtm = rng(seed + 77)
    muT = {}
    for X in Xs:
        muT[avatar(X, k, d)] = nxtm()
    for q in range(40):
        muT[tuple((3 * q + 5 * nu + 1) % sl[0] for nu in range(d))] = nxtm()
    dmuT = d_of(muT, sl[0], d)
    okA, diff_ev = True, False
    for l in range(1, k + 1):
        lhs = qstr_fwd_chain(dmuT, l, sl, d, TM)
        rhsA = d_of(A_blk_sparse(muT, l, sl, d), sl[l], d)
        rhsE = d_of(ev_pull(muT, l, sl, d), sl[l], d)
        kk = set(lhs) | set(rhsA)
        eqA = all(lhs.get(key, F(0)) == rhsA.get(key, F(0)) for key in kk)
        kk2 = set(lhs) | set(rhsE)
        eqE = all(lhs.get(key, F(0)) == rhsE.get(key, F(0)) for key in kk2)
        okA = okA and eqA
        diff_ev = diff_ev or (not eqE)
        print(f"B4      l={l}: Q_str^(0->l)(d mu) == d(A^(0->l)mu): {eqA};   "
              f"== d(ev^(0->l)mu): {eqE}")
    verd[f"B4-i/{tag}"] = okA
    verd[f"B4-ii/{tag}"] = diff_ev

    TMbad = mult_table(flat=True)
    massfired = not mass_ok(TMbad)
    lhsbad = qstr_fwd_chain(dmuT, 1, sl, d, TMbad)
    rhsA1 = d_of(A_blk_sparse(muT, 1, sl, d), sl[1], d)
    kk = set(lhsbad) | set(rhsA1)
    b4bad = all(lhsbad.get(key, F(0)) == rhsA1.get(key, F(0)) for key in kk)
    fired5 = massfired and (not b4bad)
    print(f"B5      CONTROL 2 (flat longitudinal multiplicity): mass assertion rejects it "
          f"(sum_t mult = {sum(TMbad.values())} != {L**2}): {massfired};  B4(i) then holds: {b4bad} "
          f"-> control {'FIRES (PASS of the control)' if fired5 else 'DOES NOT FIRE -> B4(i) is insensitive to the straight average'}")
    verd[f"B5/{tag}"] = fired5

print(f"\n{'='*78}\n=== B3 (iii): rho_tv decreasing in k at fixed l (d = 2) ===")
for l in (0, 1):
    a = rho_tv_store.get(("Q1 (d=2,k=2,T=3)", l))
    b = rho_tv_store.get(("Q2 (d=2,k=3,T=2)", l))
    if a is not None and b is not None:
        print(f"  l={l}: Q1 (k=2) rho_tv = {a} = {float(a):.6f};  Q2 (k=3) rho_tv = {b} = "
              f"{float(b):.6f};  decreasing: {b < a}")
        verd[f"B3-iii-dec/l={l}"] = (b < a)

print(f"\n{'='*78}\n=== VERDICTS ===")
for key in sorted(verd):
    print(f"  {key:34s}: {'PASS' if verd[key] else 'FAIL'}")
print(f"  OVERALL: {'ALL PASS' if all(verd.values()) else 'NOT ALL PASS'}")
print(f"  FAILS: {[k for k, v in verd.items() if not v]}")
