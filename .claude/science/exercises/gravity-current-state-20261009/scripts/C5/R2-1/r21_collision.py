"""R2-1 probe (f): the O(kappa*lambda) part of any exact (GW-modified or not) identity requires
the interacting matter theory to carry an exact continuous translation symmetry, whose one-particle
charge tau_j(k) must be an additive collision invariant on the real 2->2 shell (with umklapp).
CHECK (not a proof; the proof is analytic, see report Lemma T): for the nearest-neighbour Euclidean
KG band on Z^4 (transfer-matrix dispersion cosh w = 1 + (m^2 + sum_j 2(1-cos k_j))/2, d = 3
spatial), no odd finite-range (trig-polynomial) charge with unit slope is a collision invariant,
and the miss does not shrink with range R. Controls:
 (C1) non-umklapp collisions only, tau = k_1 (lifted): residual = machine zero (locally fine);
 (C2) all collisions, tau = sawtooth k_1: residual 2*pi on umklapp rows (the tower's charge folded);
 (C3) even basis + w itself: w is an exact collision invariant (residual ~ 1e-15).
"""
import numpy as np
rng = np.random.default_rng(7)
m = 0.5
d = 3

def w(k):
    return np.arccosh(1 + (m * m + np.sum(2 * (1 - np.cos(k)), axis=-1)) / 2)

def wrap(k):
    return (k + np.pi) % (2 * np.pi) - np.pi

def sample(nwant, local=None):
    out = []
    tries = 0
    while len(out) < nwant and tries < 200 * nwant:
        tries += 1
        if local is None:
            k1 = rng.uniform(-np.pi, np.pi, d); k2 = rng.uniform(-np.pi, np.pi, d)
            shift = np.pi * rng.integers(0, 2, d)
        else:
            k1 = rng.uniform(-local, local, d); k2 = rng.uniform(-local, local, d)
            shift = np.zeros(d)
        P = k1 + k2; W = w(k1) + w(k2)
        c = P / 2 + shift
        u = rng.normal(size=d); u /= np.linalg.norm(u)
        f = lambda s: w(c + s * u) + w(P - c - s * u) - W
        ss = np.linspace(0, np.pi * np.sqrt(d), 200)
        fs = np.array([f(s) for s in ss])
        idx = np.where(np.sign(fs[:-1]) * np.sign(fs[1:]) < 0)[0]
        if len(idx) == 0:
            continue
        i = rng.choice(idx); a, b = ss[i], ss[i + 1]
        for _ in range(60):
            mid = (a + b) / 2
            if np.sign(f(a)) * np.sign(f(mid)) <= 0: b = mid
            else: a = mid
        k3 = c + a * u; k4 = P - k3
        ks = [wrap(k1), wrap(k2), wrap(k3), wrap(k4)]
        if abs(w(ks[0]) + w(ks[1]) - w(ks[2]) - w(ks[3])) > 1e-10:
            continue
        um = np.any(np.abs(ks[0] + ks[1] - ks[2] - ks[3]) > 1e-8)
        if local is not None and um:
            continue
        out.append((ks, um))
    return out

def odd_basis(R):
    ns = []
    for n in np.ndindex(*(2 * R + 1,) * d):
        n = np.array(n) - R
        if np.all(n == 0): continue
        # half-space representative
        nz = n[np.nonzero(n)[0][0]]
        if nz > 0: ns.append(n)
    return np.array(ns)

def rows(samples, funcs):
    A = []
    for ks, um in samples:
        A.append(funcs(ks[0]) + funcs(ks[1]) - funcs(ks[2]) - funcs(ks[3]))
    return np.array(A)

S = sample(3000)
um_frac = np.mean([um for _, um in S])
print("R2-1 collision-invariant check: NN Euclidean KG band, d=%d spatial, m=%.2f" % (d, m))
print("samples: %d real 2->2 shell points (sampler fraction umklapp = %.2f; sampler, not invariant measure)" % (len(S), um_frac))

# (C3) w is exact
r = rows(S, lambda k: np.array([w(k)]))
print("(C3) w as charge: max |sum_in w - sum_out w| = %.2e" % np.max(np.abs(r)))
# (C2) sawtooth k_1
r = rows(S, lambda k: np.array([k[0]]))
umv = np.array([um for _, um in S])
print("(C2) tau = sawtooth k_1: max|res| non-umklapp rows = %.2e ; umklapp rows: |res|/2pi values = %s" % (
    np.max(np.abs(r[~umv])), np.unique(np.round(np.abs(r[umv, 0]) / (2 * np.pi), 6))[:6]))
# (C1) local, non-umklapp only
SL = sample(800, local=0.6)
r = rows(SL, lambda k: np.array([k[0]]))
print("(C1) local non-umklapp sample (%d rows), tau = k_1: max|res| = %.2e" % (len(SL), np.max(np.abs(r))))

print("odd finite-range charges tau = sum_n c_n sin(n.k), |n|_inf <= R, unit slope d tau_1/dk_1(0) = 1:")
print("  R  #basis  min RMS residual (unit slope)   smallest sing. value of A/sqrt(rows)   [local-only sample, unit slope]")
for R in [1, 2, 3]:
    ns = odd_basis(R)
    f = lambda k, ns=ns: np.sin(ns @ k)
    A = rows(S, f) / np.sqrt(len(S))
    AL = rows(SL, f) / np.sqrt(len(SL))
    s = ns[:, 0].astype(float)  # slope of sin(n.k) along k_1 at 0
    def minres(A):
        U, sv, Vt = np.linalg.svd(A, full_matrices=False)
        # minimize |A c|^2 s.t. s.c = 1 : 1/ (s^T (A^T A)^-1 s), regularized
        Minv = Vt.T @ np.diag(1 / np.maximum(sv, 1e-13) ** 2) @ Vt
        return 1 / np.sqrt(s @ Minv @ s), sv[-1]
    mr, smin = minres(A)
    mrL, _ = minres(AL)
    print("  %d  %5d   %.4e                     %.4e                              %.4e" % (R, len(ns), mr, smin, mrL))
print("Reading: on the full shell (umklapp included) no odd finite-range unit-slope charge is an")
print("invariant and the miss does not go to zero with R; locally (no umklapp) the miss shrinks with R")
print("because sin-polynomials approximate k_1 near 0. The obstruction is periodicity + umklapp")
print("(equivalently analyticity + periodicity), not the specific dispersion.")

print()
print("Normalization matters: unit slope at the single point k=0 admits oscillatory charges")
print("(e.g. sin(N k_1)/N) whose residual falls with R; that is not a momentum. Two physical")
print("normalizations follow.")
print("(N1) Fourier truncations of the lattice momentum (sawtooth k_1), tau_R = sum_{n<=R} 2(-1)^{n+1} sin(n k_1)/n:")
print("   R    RMS res (all rows)   RMS res (non-umklapp rows)   RMS res (umklapp rows)")
for R in [1, 2, 4, 8, 16, 32, 64]:
    f = lambda k, R=R: np.array([sum(2 * (-1) ** (n + 1) * np.sin(n * k[0]) / n for n in range(1, R + 1))])
    r = rows(S, f)[:, 0]
    print("  %3d   %.4f              %.4f                       %.4f" % (R, np.sqrt(np.mean(r ** 2)),
          np.sqrt(np.mean(r[~umv] ** 2)), np.sqrt(np.mean(r[umv] ** 2))))
print("(N2) best odd finite-range charge that equals k_1 on the soft ball |k|<0.5 (least squares,")
print("     weight 1e3), collision residual on the full shell:")
ball = rng.uniform(-0.5, 0.5, (3000, d)); ball = ball[np.linalg.norm(ball, axis=1) < 0.5]
print("   R  #basis  local fit RMS   collision RMS (all)   (umklapp rows)")
for R in [1, 2, 3]:
    ns = odd_basis(R)
    f = lambda k, ns=ns: np.sin(ns @ k)
    A = rows(S, f) / np.sqrt(len(S))
    Bm = np.sin(ball @ ns.T) / np.sqrt(len(ball))
    mu = 1e3
    M = np.vstack([A, mu * Bm]); y = np.concatenate([np.zeros(len(A)), mu * ball[:, 0] / np.sqrt(len(ball))])
    c, *_ = np.linalg.lstsq(M, y, rcond=None)
    loc = np.sqrt(np.mean((np.sin(ball @ ns.T) @ c - ball[:, 0]) ** 2))
    rr = rows(S, f) @ c
    print("   %d  %5d   %.3e       %.4f                %.4f" % (R, len(ns), loc, np.sqrt(np.mean(rr ** 2)), np.sqrt(np.mean(rr[umv] ** 2))))
