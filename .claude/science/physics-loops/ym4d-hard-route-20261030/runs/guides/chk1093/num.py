# Row 1093 guide run: G1, G2 by quadrature (independent theta-grid path), and a
# refutation attempt of FST-BD (i), (iii), (iv) on a small Ising cycle. Pure Python, serial.
import math, random, itertools
random.seed(1093)
out = []
# ---------- G1 and G2 on a theta grid ----------
n = 1000
th = [2*math.pi*k/n for k in range(n)]
co = [math.cos(t) for t in th]; si = [math.sin(t) for t in th]
gam = [math.atan2(abs(s), abs(c)) for c, s in zip(co, si)]   # gamma in [0, pi/2]
def moments(J, h):
    Z = E12 = Ec1 = Eg1 = Eg2 = Eg12 = 0.0
    for i in range(n):
        a1 = h*co[i]
        for j in range(n):
            cd = co[i]*co[j] + si[i]*si[j]
            w = math.exp(J*cd + a1 - h*co[j])
            Z += w; E12 += w*cd; Ec1 += w*co[i]
            Eg1 += w*gam[i]; Eg2 += w*gam[j]; Eg12 += w*gam[i]*gam[j]
    return E12/Z, Ec1/Z, Eg12/Z - (Eg1/Z)*(Eg2/Z)
for h in (0.5, 1.0, 2.0):
    m0 = moments(0.0, h); mp = moments(0.01, h); mm = moments(-0.01, h)
    # J = 0 one-site quantities under e^{h cos}
    Z1 = sum(math.exp(h*c) for c in co)
    r = sum(c*math.exp(h*c) for c in co)/Z1
    v = sum(c*c*math.exp(h*c) for c in co)/Z1 - r*r
    # gamma marginal a ~ cosh(h cos gamma): use site-1 law at J = 0 on the grid
    Eg = sum(g*math.exp(h*c) for g, c in zip(gam, co))/Z1
    phi = [abs(c)*math.tanh(h*abs(c)) for c in co]
    Ep = sum(p*math.exp(h*c) for p, c in zip(phi, co))/Z1
    Egp = sum(g*p*math.exp(h*c) for g, p, c in zip(gam, phi, co))/Z1
    kcov = Egp - Eg*Ep
    out.append("G1 h=%.1f: E0cos(t1-t2)=%.6f (-r^2=%.6f); dJ Ecos t1 (fd)=%.6f (-r Var=%.6f); Ecos(t1-t2) at J=.01: %.6f" % (
        h, m0[0], -r*r, (mp[1]-mm[1])/0.02, -r*v, mp[0]))
    out.append("G2 h=%.1f: Cov_J(g1,g2) J=0: %.2e, J=.01: %.3e; dJ Cov (fd)=%.6f; -[Cov_a(g,phi)]^2=%.6f; Cov_a=%.5f" % (
        h, m0[2], mp[2], (mp[2]-mm[2])/0.02, -kcov*kcov, kcov))
# ---------- FST-BD refutation attempt: Ising cycle ----------
def run_bd(nsite, Js, hs, blocks, a, trials):
    states = list(itertools.product((-1, 1), repeat=nsite))
    idx = {s: i for i, s in enumerate(states)}
    def logw(s):
        return sum(Js[i]*s[i]*s[(i+1) % nsite] for i in range(nsite)) + sum(hs[i]*s[i] for i in range(nsite))
    W = [math.exp(logw(s)) for s in states]; Ztot = sum(W)
    mu = [x/Ztot for x in W]
    dist = lambda x, y: min(abs(x-y), nsite-abs(x-y))
    def cond(V, s):  # conditional law on V given s outside V: list of (state index, prob)
        res = []
        for xi in itertools.product((-1, 1), repeat=len(V)):
            t = list(s)
            for k, u in enumerate(V): t[u] = xi[k]
            res.append(idx[tuple(t)])
        ws = [W[i] for i in res]; zz = sum(ws)
        return list(zip(res, [x/zz for x in ws]))
    def PV(V, f):
        g = [0.0]*len(states)
        for i, s in enumerate(states):
            g[i] = sum(p*f[j] for j, p in cond(V, s))
        return g
    def osc(f, x):
        m = 0.0
        for i, s in enumerate(states):
            t = list(s); t[x] = -t[x]
            m = max(m, abs(f[i]-f[idx[tuple(t)]]))
        return m
    # influences k^V_{x->u}: max TV of block law under a flip at x, assigned to every u in V
    k = {}
    for bi, V in enumerate(blocks):
        for x in range(nsite):
            if x in V: continue
            tv = 0.0
            for s in states:
                t = list(s); t[x] = -t[x]
                A = cond(V, s); B = cond(V, tuple(t))
                # same ordering of xi in both lists
                tv = max(tv, 0.5*sum(abs(p-q) for (_, p), (_, q) in zip(A, B)))
            for u in V: k[(bi, x, u)] = tv
    nu = [sum(1 for V in blocks if u in V) for u in range(nsite)]
    gam_u = []
    for u in range(nsite):
        ssum = sum(math.exp(a*dist(x, u))*k[(bi, x, u)] for bi, V in enumerate(blocks) if u in V for x in range(nsite) if x not in V)
        gam_u.append(ssum/nu[u])
    gamma = max(gam_u); N = len(blocks); theta = 1 - (1-gamma)*min(nu)/N
    worst = {"i": 0.0, "iii": 0.0, "iv": 0.0}
    if gamma >= 1: return gamma, None
    diam = max(max(dist(x, y) for x in V for y in V) for V in blocks)
    X = 0.25*math.exp(a*diam)
    cov = lambda f, g: sum(m*fi*gi for m, fi, gi in zip(mu, f, g)) - sum(m*fi for m, fi in zip(mu, f))*sum(m*gi for m, gi in zip(mu, g))
    for tr in range(trials):
        f = [random.uniform(-1, 1) for _ in states]
        if tr % 3 == 0:  # spin-like f
            x0 = random.randrange(nsite); f = [s[x0] + 0.1*random.uniform(-1, 1) for s in states]
        # (i) with w = e^{-a d(x, x1)}
        x1 = random.randrange(nsite); w = [math.exp(-a*dist(x, x1)) for x in range(nsite)]
        Pf = [sum(PV(V, f)[i] for V in blocks)/N for i in range(len(states))] if tr < 6 else None
        if Pf is not None:
            lhs = sum(w[x]*osc(Pf, x) for x in range(nsite)); rhs = theta*sum(w[x]*osc(f, x) for x in range(nsite))
            worst["i"] = max(worst["i"], lhs/rhs)
        # (iii): g on B = {b0} or {b0, b0+1}
        b0 = random.randrange(nsite); B = {b0} if tr % 2 else {b0, (b0+1) % nsite}
        gv = {}
        g = []
        for s in states:
            key = tuple(s[b] for b in sorted(B))
            if key not in gv: gv[key] = random.uniform(-1, 1)
            g.append(gv[key])
        Bp = set(B)
        for V in blocks:
            if set(V) & B: Bp |= set(V)
        dB = lambda x: min(dist(x, y) for y in Bp)
        lhs = abs(cov(f, g)); gn = max(abs(t) for t in g)
        rhs3 = 2*gn*(max(nu)/min(nu))/(1-gamma)*sum(osc(f, x)*math.exp(-a*dB(x)) for x in range(nsite))
        worst["iii"] = max(worst["iii"], lhs/rhs3)
        # (iv): general g
        g2 = [random.uniform(-1, 1) for _ in states] if tr % 2 else [s[random.randrange(nsite)] for s in states]
        of = [osc(f, x) for x in range(nsite)]; og = [osc(g2, x) for x in range(nsite)]
        rhs4 = X*max(nu)/((1-gamma)*min(nu))*sum(of[x]*og[b]*math.exp(-a*dist(x, b)) for x in range(nsite) for b in range(nsite))
        worst["iv"] = max(worst["iv"], abs(cov(f, g2))/rhs4)
    return gamma, worst
ns = 7
Js = [random.uniform(0.15, 0.35) for _ in range(ns)]; hs = [random.uniform(-0.6, 0.6) for _ in range(ns)]
single = [(u,) for u in range(ns)]; pairs = [(u, (u+1) % ns) for u in range(ns)]
for name, bl in (("single-site blocks", single), ("pair blocks", pairs)):
    for a in (0.0, 0.2):
        gmm, worst = run_bd(ns, Js, hs, bl, a, 40)
        out.append("FST-BD %s a=%.1f: gamma=%.3f; max lhs/rhs: %s" % (name, a, gmm, worst))
print("\n".join(out))
