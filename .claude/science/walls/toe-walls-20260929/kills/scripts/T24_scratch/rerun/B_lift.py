"""T24 test B: what can a period-2 (translation-breaking) covariant bilinear term lift?

B1: exact diagonalisation on an 8^3 torus of  H = sigma.S + eps(x)(s Gs + t Gt).
B2: linearised general covariant corner mass matrix M (S3-commutant, 20 real parameters): if the remainder is
    fully gapped at E=0 (pencil M - lambda X has no nonzero real eigenvalue), is the light set chirality balanced?
"""
import itertools
import json
import numpy as np

rng = np.random.default_rng(2424)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]


def torus_ops(L):
    N = L ** 3
    idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    T = []
    for a in range(3):
        M = np.zeros((N, N))
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    c = [x, y, z]
                    d = list(c); d[a] += 1
                    M[idx(*c), idx(*d)] = 1.0     # (T psi)(c) = psi(c + e_a)
        T.append(M)
    eps = np.array([(-1) ** (x + y + z) for x in range(L) for y in range(L) for z in range(L)], float)
    return T, eps


def B1(L=8):
    lines = []
    T, eps = torus_ops(L)
    N = L ** 3
    S = [(T[a] - T[a].T) / (2j) for a in range(3)]
    C = [(T[a] + T[a].T) / 2 for a in range(3)]
    H0 = sum(np.kron(SIG[a], S[a]) for a in range(3))          # coin x site
    sig2 = C[0] @ C[1] + C[1] @ C[2] + C[2] @ C[0]
    Gs = 2 * (np.eye(N) + sig2)
    Gt = 3 * np.eye(N) - sig2
    E = np.diag(eps)
    res = {}
    def zero_count(H, tol=1e-9):
        ev = np.linalg.eigvalsh(H)
        return int((np.abs(ev) < tol).sum()), ev
    # momentum data for the formula
    ks = 2 * np.pi * np.arange(L) / L
    def spectrum_formula(s, t):
        vals = []
        for kx, ky, kz in itertools.product(range(L), repeat=3):
            k = ks[[kx, ky, kz]]
            kq = (kx + L // 2, ky + L // 2, kz + L // 2)
            # take one representative per Q-pair
            if (kx, ky, kz) > tuple(q % L for q in kq):
                continue
            c = np.cos(k)
            sg2 = c[0] * c[1] + c[1] * c[2] + c[2] * c[0]
            m = s * 2 * (1 + sg2) + t * (3 - sg2)
            e = np.sqrt(np.sum(np.sin(k) ** 2) + m ** 2)
            vals += [e, e, -e, -e]
        return np.sort(np.array(vals))
    lines.append(f"B1: torus L={L}, dim {2*N}")
    for (s, t) in [(0, 0), (0.05, 0), (0, 0.05), (0.05, 0.05), (-0.03, 0), (0, -0.07)]:
        H = H0 + np.kron(np.eye(2), E @ (s * Gs + t * Gt))
        assert np.allclose(H, H.conj().T)
        nz, ev = zero_count(H)
        pred = spectrum_formula(s, t)
        err = np.abs(np.sort(ev) - pred).max()
        lines.append(f"   s={s:+.2f} t={t:+.2f}: zero modes = {nz:2d}; spectrum vs +-sqrt(|sin k|^2+m^2): max err = {err:.1e}")
        res[f"s{s}_t{t}"] = dict(zero=nz, err=float(err))
    # random covariant even-displacement G, projected to vanish on singlets / triplets / neither
    Vs_list = []
    counts = {}
    ws = [w for w in itertools.product(range(-3, 4), repeat=3) if sum(w) % 2 == 0 and w != (0, 0, 0)]
    Ts = {}
    coords = np.array(list(itertools.product(range(L), repeat=3)))
    def Tw(w):
        tgt = (coords + np.array(w)) % L
        perm = (tgt[:, 0] * L + tgt[:, 1]) * L + tgt[:, 2]
        M = np.zeros((N, N))
        M[np.arange(N), perm] = 1.0
        return M
    # covariant (O-invariant) even-displacement symbol: g_w depends only on the sorted |w| triple
    orbit_coef = {}
    def coef(w):
        key = tuple(sorted(abs(x) for x in w))
        if key not in orbit_coef:
            orbit_coef[key] = rng.normal()
        return orbit_coef[key]
    Gr_terms = {}
    for trial in range(12):
        orbit_coef.clear()
        G = np.zeros((N, N))
        g_sing = 0.0; g_trip = 0.0
        for w in ws:
            g = coef(w)
            P = Tw(w); G += g * (P + P.T) / 2 * 0.5   # each w and -w both appear in ws: factor 0.5 cancels double count
            g_sing += g * 1.0                       # cos(pi n . w) with n=000
            g_trip += g * (-1) ** abs(w[0])         # n = (1,0,0)
        # fix: symbol at corner = sum_w g_w cos(pi n.w) ; (T+T^T)/2 has symbol cos(k.w); factor 0.5 for double listing
        g_sing *= 0.5; g_trip *= 0.5
        mode = trial % 3
        Gp = G.copy()
        # subtract multiples of Gs (corner values 8, 0) and Gt (0, 4)
        if mode == 0:      # vanish on singlets only
            Gp = G - (g_sing / 8) * Gs
        elif mode == 1:    # vanish on triplets only
            Gp = G - (g_trip / 4) * Gt
        elif mode == 2:    # vanish on neither
            Gp = G
        amp = 0.1
        H = H0 + np.kron(np.eye(2), E @ (amp * Gp))
        nz, ev = zero_count(H, 1e-8)
        counts[nz] = counts.get(nz, 0) + 1
        lines.append(f"   random covariant even G, mode {['singlets=0', 'triplets=0', 'generic'][mode]}: zero modes = {nz}")
    res["random_counts"] = counts
    lines.append(f"   distinct zero-mode counts over random covariant even G: {sorted(counts)}")
    return lines, res


def B2(nsamp=40000):
    """S3-covariant corner mass matrix M (8x8) and velocity matrix X. Basis order:
    a0=|000>, a1=sym hw1, a2=sym hw2, a3=|111>  (A-isotype),  e1,e2 (standard rep of S3 inside hw1, hw2; each 2-dim)."""
    lines = []
    def rand_herm(n, kernel_dim):
        Z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        Q, _ = np.linalg.qr(Z)
        mu = rng.normal(size=n)
        mu[:kernel_dim] = 0.0
        return Q @ np.diag(mu) @ Q.conj().T, Q[:, :kernel_dim]
    xsets = {
        "walker (+,-,+,-)": (1, -1, 1, -1),
        "alt   (+,+,-,-)": (1, 1, -1, -1),
    }
    out = {}
    for name, x in xsets.items():
        for velmag in ["equal", "random"]:
            stats = {}
            for it in range(nsamp):
                kA = rng.integers(0, 5); kE = rng.integers(0, 3)
                MA, KA = rand_herm(4, kA)
                ME, KE = rand_herm(2, kE)
                if velmag == "equal":
                    mags = np.ones(4)
                else:
                    mags = rng.uniform(0.3, 3.0, size=4)
                XA = np.diag(np.array(x) * mags)
                XE = np.diag(np.array([x[1], x[2]]) * mags[[1, 2]])
                # pencils decouple; E block multiplicity 2
                def pencil(M, X):
                    ev = np.linalg.eigvals(np.linalg.solve(X, M))
                    return ev
                evA = pencil(MA, XA); evE = pencil(ME, XE)
                tol = 1e-7
                realA = np.abs(evA.imag) < 1e-7 * (1 + np.abs(evA)); realE = np.abs(evE.imag) < 1e-7 * (1 + np.abs(evE))
                nonzero_real = (realA & (np.abs(evA) > tol)).any() or (realE & (np.abs(evE) > tol)).any()
                gapped = not nonzero_real
                # signature of X on ker M (Hermitian form v^dag X v on kernel basis)
                sig = 0
                for (K, X, mult) in [(KA, XA, 1), (KE, XE, 2)]:
                    if K.shape[1] > 0:
                        form = K.conj().T @ X @ K
                        w = np.linalg.eigvalsh((form + form.conj().T) / 2)
                        sig += mult * (int((w > 1e-9).sum()) - int((w < -1e-9).sum()))
                lightdim = kA + 2 * kE
                key = (int(kA), int(kE))
                d = stats.setdefault(key, dict(n=0, gapped=0, sigs=set()))
                d["n"] += 1
                if gapped:
                    d["gapped"] += 1
                    d["sigs"].add(sig)
            lines.append(f"B2: X signs {name}, velocity magnitudes {velmag}: key=(dim ker in A-block, dim ker in E-block); light-state count = kA+2kE")
            viol = 0
            for key in sorted(stats):
                d = stats[key]
                lines.append(f"    ker dims {key} (light states {key[0]+2*key[1]}): samples {d['n']}, gapped remainder {d['gapped']}, "
                             f"signature(X|ker) among gapped = {sorted(d['sigs'])}")
                if any(sg != 0 for sg in d["sigs"]):
                    viol += 1
            lines.append(f"    keys with a gapped remainder and nonzero signature: {viol}")
            out[f"{name}|{velmag}"] = {str(k): dict(n=v["n"], gapped=v["gapped"], sigs=sorted(v["sigs"])) for k, v in stats.items()}
    return lines, out


if __name__ == "__main__":
    l1, r1 = B1()
    for l in l1: print(l)
    l2, r2 = B2()
    for l in l2: print(l)
    json.dump(dict(B1=r1, B2=r2), open("B_lift_results.json", "w"), indent=1, default=str)
