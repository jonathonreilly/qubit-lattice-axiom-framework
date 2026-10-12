"""C5 R12-1, script 1: matter-bilinear order of the lattice constraint algebra (R11-2's O(kappa^2)).

Matter: R7-1's number-conserving box fermion (one mode per site), one-body symbols
    s(k)   = rho(k) k + (1 - rho(k)) sin k      (per component; = k on |k_i| <= b)
    eps(k) = sqrt(m^2 + sum_i s(k_i)^2)
Densities (midpoint / first-moment placement, as R7-1's K):
    <k+p| T00[e^{ipx}] |k>      = (eps(k+p) + eps(k))/2
    <k+p| P_j[e_j e^{ipx}] |k>  = (s_j(k+p) + s_j(k))/2
Lattice comparators: "naive" (s = sin k, eps^2 = m^2 + sum sin^2 k) and "NN" (C3/R7-1 comparator:
    eps^2 = m^2 + sum (2 - 2 cos k), P symbol sin k; there {H,K} = P is exact and the cos k defect sits in [K,P]).
Second quantisation of number-conserving bilinears is a Lie homomorphism with no c-number
([c^dag A c, c^dag B c] = c^dag [A,B] c), so the one-body symbols decide everything.

Bracket defects (Poisson-like {A,B} := -i[A,B]), structure functions = undeformed flat HDA,
smearing derivative = the gravity side's box symbol d(p) (= p near 0):
    D_SS(p,p';k) = {T_p, T_p'} - sigma  * i (d(p') - d(p)) . P(p+p')
    D_JS(p,p';k) = {P_c,p, T_p'} - sigma' * i d_c(p') T(p+p')
    D_JJ(p,p';k) = {P_c,p, P_e,p'} - sigma''* i (d_c(p') P_e - d_e(p) P_c)(p+p')
Completion images (gravity-dependent completions, R12-1 Theorem K):
    SS: s(p).tau(p',p,k) - s(p').tau(p,p',k), s_ij(p) = d_i d_j - |d|^2 delta_ij  (ideal of quadratics)
    JS: Kill(p) . A + s(p') . B        (Kill = symmetrised gradient symbol of the shift)
    JJ: Kill(p) . A - Kill(p') . A'
So the ONLY conditions are the Killing jets (Theorem K):
    SS: bidegree (<=1, <=1) Taylor part in (p, p') vanishes
    JS: p-order 0 and antisymmetric p-order 1, each to p'-order <= 1
    JJ: Killing x Killing jets
Checked here: (A) Killing jets vanish on the box, not off it; (B) non-Killing jets are nonzero
even on the box (so completions are needed: the local Dirac-Schwinger algebra fails for
number-conserving positive-energy densities, absorbable); (C) the completion that must absorb
the JS slice stays bounded as p' -> 0 in the box and diverges like 1/|p'| off it;
(D) the quadratic ideal is spanned by the s_ij(p) components (d = 2, 3).
"""
import numpy as np
import itertools

np.set_printoptions(precision=3, linewidth=140)
rng = np.random.default_rng(20261012)
M = 0.3
B_IN, B_OUT = 2.0, 3.1


def _f(t):
    t = np.asarray(t, float)
    out = np.zeros_like(t)
    pos = t > 0
    out[pos] = np.exp(-1.0 / t[pos])
    return out


def step(t):
    return _f(t) / (_f(t) + _f(1.0 - t))


def rho(k):
    a = np.abs(np.mod(k + np.pi, 2 * np.pi) - np.pi)
    return 1.0 - step((a - B_IN) / (B_OUT - B_IN))


def s_box(k):
    kk = np.mod(k + np.pi, 2 * np.pi) - np.pi
    r = rho(k)
    return r * kk + (1 - r) * np.sin(k)


def s_lat(k):
    return np.sin(k)


# models: (momentum symbol s, energy^2 symbol)
MODEL = {"box": (s_box, lambda k: M * M + np.sum(s_box(k) ** 2, axis=-1)),
         "naive": (s_lat, lambda k: M * M + np.sum(np.sin(k) ** 2, axis=-1)),
         "NN": (s_lat, lambda k: M * M + np.sum(2 - 2 * np.cos(k), axis=-1))}


def make(model):
    s, e2 = MODEL[model]

    def eps(k):
        return np.sqrt(e2(k))

    def aT(p, k):
        return 0.5 * (eps(k + p) + eps(k))

    def aP(p, k, j):
        return 0.5 * (s(k + p)[..., j] + s(k)[..., j])

    d = s_box  # gravity-side smearing symbol (box); = p near p = 0

    def comm(a, b, p, q, k):
        # <k+p+q| [A_p, B_q] |k>
        return a(p, k + q) * b(q, k) - b(q, k + p) * a(p, k)

    def D_SS(p, q, k):
        lhs = -1j * comm(aT, aT, p, q, k)
        rhs = sum(1j * (d(q)[j] - d(p)[j]) * aP(p + q, k, j) for j in range(len(k)))
        return lhs + rhs            # sigma = -1 (fitted analytically on the (1,0) jet)

    def D_JS(c):
        def f(p, q, k):
            lhs = -1j * comm(lambda pp, kk: aP(pp, kk, c), aT, p, q, k)
            return lhs + 1j * d(q)[c] * aT(p + q, k)      # sigma' = -1
        return f

    def D_JJ(c, e):
        def f(p, q, k):
            lhs = -1j * comm(lambda pp, kk: aP(pp, kk, c), lambda pp, kk: aP(pp, kk, e), p, q, k)
            rhs = 1j * (d(q)[c] * aP(p + q, k, e) - d(p)[e] * aP(p + q, k, c))
            return lhs + rhs        # sigma'' = -1
        return f

    return eps, D_SS, D_JS, D_JJ


def grad(f, x, h=1e-4):
    g = []
    for i in range(len(x)):
        e = np.zeros_like(x); e[i] = h
        g.append((f(x + e) - f(x - e)) / (2 * h))
    return np.array(g)


def jets_SS(D, k, dim, h=1e-3):
    """Taylor jets of D(p,q;k) at p=q=0 of bidegree (0,0),(1,0),(0,1),(1,1)."""
    z = np.zeros(dim)
    out = {}
    out["00"] = abs(D(z, z, k))
    out["10"] = np.max(np.abs(grad(lambda p: D(p, z, k), z)))
    out["01"] = np.max(np.abs(grad(lambda q: D(z, q, k), z)))
    mx = 0.0
    for a in range(dim):
        for b in range(dim):
            ea = np.zeros(dim); ea[a] = h
            eb = np.zeros(dim); eb[b] = h
            v = (D(ea, eb, k) - D(ea, -eb, k) - D(-ea, eb, k) + D(-ea, -eb, k)) / (4 * h * h)
            mx = max(mx, abs(v))
    out["11"] = mx
    return out


def jets_JS(Dc_list, k, dim, h=1e-3):
    """p-order 0 and antisymmetric p-order 1 (rotations), each to q-order <= 1."""
    z = np.zeros(dim)
    worst = {"transl_q0": 0.0, "transl_q1": 0.0, "rot_q0": 0.0, "rot_q1": 0.0}
    for c, Dc in enumerate(Dc_list):
        worst["transl_q0"] = max(worst["transl_q0"], abs(Dc(z, z, k)))
        worst["transl_q1"] = max(worst["transl_q1"], np.max(np.abs(grad(lambda q: Dc(z, q, k), z))))
    # rotation: R_cb(q) = d/dp_b D_c - d/dp_c D_b, at p = 0
    for c in range(dim):
        for b in range(c + 1, dim):
            def R(q):
                return (grad(lambda p: Dc_list[c](p, q, k), z)[b] - grad(lambda p: Dc_list[b](p, q, k), z)[c])
            worst["rot_q0"] = max(worst["rot_q0"], abs(R(z)))
            worst["rot_q1"] = max(worst["rot_q1"], np.max(np.abs(grad(R, z, h))))
    return worst


def jets_JJ(DJJ, k, dim, h=1e-3):
    """Killing x Killing: (transl,transl), (transl,rot), (rot,rot)."""
    z = np.zeros(dim)
    worst = {"TT": 0.0, "TR": 0.0, "RR": 0.0}
    for c in range(dim):
        for e in range(dim):
            worst["TT"] = max(worst["TT"], abs(DJJ[c][e](z, z, k)))
    # translation (component c, p=0) with rotation (e,b) in q
    for c in range(dim):
        for e in range(dim):
            for b in range(e + 1, dim):
                v = (grad(lambda q: DJJ[c][e](z, q, k), z)[b] - grad(lambda q: DJJ[c][b](z, q, k), z)[e])
                worst["TR"] = max(worst["TR"], abs(v))
    for c in range(dim):
        for a in range(c + 1, dim):
            for e in range(dim):
                for b in range(e + 1, dim):
                    def Dmix(p, q, C, E):
                        return DJJ[C][E](p, q, k)
                    acc = 0
                    for (C, A, sC) in ((c, a, 1), (a, c, -1)):
                        for (E, Bq, sE) in ((e, b, 1), (b, e, -1)):
                            ea = np.zeros(dim); ea[A] = h
                            eb = np.zeros(dim); eb[Bq] = h
                            v = (Dmix(ea, eb, C, E) - Dmix(ea, -eb, C, E) - Dmix(-ea, eb, C, E)
                                 + Dmix(-ea, -eb, C, E)) / (4 * h * h)
                            acc += sC * sE * v
                    worst["RR"] = max(worst["RR"], abs(acc))
    return worst


def nonkilling_SS(D, k, dim, h=2e-2):
    """bidegree (2,1) coefficient d^2/dp_a^2 d/dq_a along axis a (non-Killing); five-point stencils."""
    z = np.zeros(dim)
    vals = []
    for a in range(dim):
        e = np.zeros(dim); e[a] = 1.0
        def g(t, u):
            return D(t * e, u * e, k)
        # d^3/dt^2 du at 0
        d2 = lambda u: (g(h, u) - 2 * g(0, u) + g(-h, u)) / h ** 2
        vals.append(abs((d2(h) - d2(-h)) / (2 * h)))
    return max(vals)


print("=== R12-1 script 1: matter-bilinear closure, box fermion vs NN lattice ===")
print(f"m = {M}, box plateau |k_i| <= {B_IN}, transition to sin k by {B_OUT}")
for dim in (2, 3):
    print(f"\n----- d = {dim} -----")
    for model in ("box", "naive", "NN"):
        eps, D_SS, D_JS, D_JJ = make(model)
        DJS = [D_JS(c) for c in range(dim)]
        DJJ = [[D_JJ(c, e) for e in range(dim)] for c in range(dim)]
        for label, kset in (("k in box (|k_i|<=1.6)", rng.uniform(-1.6, 1.6, (3, dim))),
                            ("k off box (|k_1| in [2.4,3.0])", np.column_stack(
                                [rng.uniform(2.4, 3.0, 3)] + [rng.uniform(-1.0, 1.0, 3) for _ in range(dim - 1)]))):
            wSS = {"00": 0, "10": 0, "01": 0, "11": 0}
            wJS = {"transl_q0": 0, "transl_q1": 0, "rot_q0": 0, "rot_q1": 0}
            wJJ = {"TT": 0, "TR": 0, "RR": 0}
            nk = 0
            for k in kset:
                j1 = jets_SS(D_SS, k, dim); j2 = jets_JS(DJS, k, dim); j3 = jets_JJ(DJJ, k, dim)
                for kk in wSS: wSS[kk] = max(wSS[kk], j1[kk])
                for kk in wJS: wJS[kk] = max(wJS[kk], j2[kk])
                for kk in wJJ: wJJ[kk] = max(wJJ[kk], j3[kk])
                nk = max(nk, nonkilling_SS(D_SS, k, dim))
            if model == "lattice" and label.startswith("k off"):
                pass
            print(f"[{model:7s}] {label}:")
            print("    SS Killing jets (00,10,01,11): " + " ".join(f"{wSS[x]:.1e}" for x in ("00", "10", "01", "11")))
            print("    JS Killing jets (T q0, T q1, R q0, R q1): " + " ".join(f"{wJS[x]:.1e}" for x in ("transl_q0", "transl_q1", "rot_q0", "rot_q1")))
            print("    JJ Killing jets (TT, TR, RR): " + " ".join(f"{wJJ[x]:.1e}" for x in ("TT", "TR", "RR")))
            print(f"    SS non-Killing jet (2,1) [must be absorbed by completions]: {nk:.3e}")

# (C) ray test: completion needed for the JS slice p = 0 (constant shift), q -> 0
print("\n=== (C) JS slice p=0: |D_JS(0,q;k)| / |s(q)| along q = t u (completion symbol needed) ===")
dim = 3
for model in ("box", "naive", "NN"):
    eps, D_SS, D_JS, D_JJ = make(model)
    for label, k in (("in box", np.array([0.7, -0.4, 1.1])), ("off box", np.array([2.7, 0.3, -0.5]))):
        u = np.array([0.6, 0.48, 0.64]); u /= np.linalg.norm(u)
        row = []
        for t in (1e-1, 1e-2, 1e-3):
            q = t * u
            dq = s_box(q)
            snorm = np.sqrt(np.sum((np.outer(dq, dq) - np.dot(dq, dq) * np.eye(3)) ** 2))
            val = max(abs(D_JS(c)(np.zeros(3), q, k)) for c in range(3))
            row.append(val / snorm)
        print(f"[{model:7s}] {label}: t = 1e-1, 1e-2, 1e-3 -> {row[0]:.3e} {row[1]:.3e} {row[2]:.3e}")

# (D) ideal check: span of s_ij(p) = p_i p_j - |p|^2 delta_ij components = all quadratic monomials
print("\n=== (D) the s_ij(p) = p_i p_j - |p|^2 delta_ij components span all quadratic monomials ===")
for dim in (2, 3):
    mons = [(a, b) for a in range(dim) for b in range(a, dim)]
    rows = []
    for i in range(dim):
        for j in range(dim):
            v = np.zeros(len(mons))
            for n, (a, b) in enumerate(mons):
                if i != j and (a, b) == (min(i, j), max(i, j)):
                    v[n] = 1.0
                if i == j and a == b:
                    v[n] = (1.0 if a == i else 0.0) - 1.0
            rows.append(v)
    rk = np.linalg.matrix_rank(np.array(rows))
    print(f"d = {dim}: rank = {rk} of {len(mons)} quadratic monomials")
