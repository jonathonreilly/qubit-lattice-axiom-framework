"""N1 of CRITERIA.md. Gaussian field composed with a quadratic map, no vertex in the measure. Corner cluster T."""
import itertools, sys, time
import numpy as np
from wnlib import plaq, current, green, K_comp, sumV, khat2

T = 8
d = 4
rng = np.random.default_rng(4242)
kh = khat2(T, d)
kh0 = kh.copy()
kh0[(0,) * d] = np.inf
SQ = 1 / np.sqrt(kh0)
IG = 1 / kh0
eps = np.zeros((3, 3, 3))
eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1
eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1


def apply_filter(field, filt):
    return np.fft.ifftn(np.fft.fftn(field, axes=(2, 3, 4, 5)) * filt, axes=(2, 3, 4, 5)).real


def sample(beta):
    xi = rng.normal(size=(3, d) + (T,) * d)
    return np.sqrt(4 / beta) * apply_filter(xi, SQ)


def grad_S3(A):
    """Gradient in A of S3tilde = sum_p Phi_p . Q_p, Q_p = -1/2 sum_{s<t} e_s x e_t, e = signed increments."""
    g = np.zeros_like(A)
    for mu in range(d):
        for nu in range(mu + 1, d):
            e0 = A[:, mu]
            e1 = np.roll(A[:, nu], -1, axis=1 + mu)
            e2 = -np.roll(A[:, mu], -1, axis=1 + nu)
            e3 = -A[:, nu]
            es = [e0, e1, e2, e3]
            ge = [np.zeros_like(e0) for _ in range(4)]
            for r in range(4):
                for s in range(4):
                    for t in range(s + 1, 4):
                        if r in (s, t):
                            continue
                        # -1/2 e_r . (e_s x e_t): derivatives in each slot; the scalar triple product is unchanged under cyclic moves
                        ge[r] += -0.5 * np.cross(es[s], es[t], axis=0)
                        ge[s] += -0.5 * np.cross(es[t], es[r], axis=0)
                        ge[t] += -0.5 * np.cross(es[r], es[s], axis=0)
            g[:, mu] += ge[0]
            g[:, nu] += np.roll(ge[1], +1, axis=1 + mu)
            g[:, mu] += -np.roll(ge[2], +1, axis=1 + nu)
            g[:, nu] += -ge[3]
    return g


def quat(A):
    # A shape (3, ...): q = (w, v), U = w + i v.sigma
    r = np.sqrt((A ** 2).sum(0))
    w = np.cos(r / 2)
    s = np.sinc(r / 2 / np.pi) / 2
    return np.concatenate([w[None], s[None] * A], axis=0)


def qm(p, q):
    w = p[0] * q[0] - (p[1:] * q[1:]).sum(0)
    v = p[0][None] * q[1:] + q[0][None] * p[1:] - np.cross(p[1:], q[1:], axis=0)
    return np.concatenate([w[None], v], axis=0)


def qc(q):
    return np.concatenate([q[:1], -q[1:]], axis=0)


def plaquettes(U):
    P = {}
    for mu in range(d):
        for nu in range(mu + 1, d):
            pa = qm(qm(qm(U[mu], np.roll(U[nu], -1, axis=1 + mu)), qc(np.roll(U[mu], -1, axis=1 + nu))), qc(U[nu]))
            P[(mu, nu)] = pa
            # reversed orientation based at the same site: x -> x+nu -> x+nu+mu -> x+mu -> x
            P[(nu, mu)] = qc(pa)
    return P


def Tmean(A):
    U = [quat(A[:, mu]) for mu in range(d)]
    P = plaquettes(U)
    tot = 0
    cnt = 0
    for (m, n, r) in itertools.permutations(range(d), 3):
        W1, W2, W3 = P[(m, n)], P[(n, r)], P[(r, m)]
        v = [W1[1:], W2[1:], W3[1:]]
        tot += (2 * (v[0] * np.cross(v[1], v[2], axis=0)).sum(0)).mean()
        cnt += 1
    return tot / cnt


def run(beta, N, composite):
    vals = np.empty(N)
    for i in range(N):
        a = sample(beta)
        if composite:
            A = a - (1 / 3) * apply_filter(grad_S3(a), IG)
        else:
            A = a
        vals[i] = Tmean(A)
    return beta ** 2 * vals.mean(), beta ** 2 * vals.std(ddof=1) / np.sqrt(N)


def exact():
    x = (T // 2,) * d
    paths = [plaq(x, 0, 1), plaq(x, 1, 2), plaq(x, 2, 0)]
    Es = [green(current(p, T, d), T, d) for p in paths]
    kc = K_comp(paths, Es, T)
    kv = 12 * sumV(*Es, T, d)
    return kc, kv


def check_gradient():
    A = rng.normal(size=(3, d) + (T,) * d) * 0.1

    def S3(A):
        tot = 0
        for mu in range(d):
            for nu in range(mu + 1, d):
                es = [A[:, mu], np.roll(A[:, nu], -1, axis=1 + mu), -np.roll(A[:, mu], -1, axis=1 + nu), -A[:, nu]]
                Phi = sum(es)
                for s in range(4):
                    for t in range(s + 1, 4):
                        tot += (-0.5 * (Phi * np.cross(es[s], es[t], axis=0))).sum()
        return tot
    g = grad_S3(A)
    D = rng.normal(size=A.shape)
    h = 1e-5
    fd = (S3(A + h * D) - S3(A - h * D)) / (2 * h)
    print(f"gradient check: {(g*D).sum():.8f} vs finite difference {fd:.8f}", flush=True)


if __name__ == "__main__":
    check_gradient()
    kc, kv = exact()
    print(f"T={T}: K_comp {kc:.5f}, K_vert {kv:.5f}, K_total {kc+kv:.5f}", flush=True)
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    for beta in (64, 128, 256):
        t0 = time.time()
        m, s = run(beta, N, True)
        m0, s0 = run(beta, N // 3, False)
        print(f"beta={beta}: composite beta^2<T> = {m:.4f}({s:.4f}); plain Gaussian potential {m0:.4f}({s0:.4f}); {time.time()-t0:.0f}s", flush=True)
