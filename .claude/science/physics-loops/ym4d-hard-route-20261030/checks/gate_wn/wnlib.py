"""Reviewer's own lattice helpers. Link field: array shape (d, T, ..., T). Written from the definitions in witness.md Text 0, 2."""
import numpy as np


def khat2(T, d):
    ks = np.meshgrid(*[2 * np.pi * np.fft.fftfreq(T) for _ in range(d)], indexing="ij")
    return sum(4 * np.sin(k / 2) ** 2 for k in ks)


def green(field, T, d):
    """(-Delta)^-1 on zero-mean functions, per direction."""
    kh = khat2(T, d)
    kh[(0,) * d] = np.inf
    out = np.empty_like(field)
    for mu in range(d):
        out[mu] = np.fft.ifftn(np.fft.fftn(field[mu]) / kh).real
    return out


def edge(x, mu, T, d, sign=+1):
    return (tuple(int(c) % T for c in x), mu, sign)


def add(x, mu, n=1):
    y = list(x)
    y[mu] += n
    return tuple(y)


def line(x, mu, n):
    """Straight path from x along +mu for n steps (or -mu for n < 0). Returns path list and end."""
    p = []
    y = tuple(x)
    if n >= 0:
        for _ in range(n):
            p.append((y, mu, +1))
            y = add(y, mu)
    else:
        for _ in range(-n):
            y = add(y, mu, -1)
            p.append((y, mu, -1))
    return p, y


def plaq(x, mu, nu):
    """x -> x+mu -> x+mu+nu -> x+nu -> x"""
    return [(tuple(x), mu, +1), (add(x, mu), nu, +1), (add(x, nu), mu, -1), (tuple(x), nu, -1)]


def inv(path):
    return [(b[0], b[1], -b[2]) for b in reversed(path)]


def lasso(tail, loop):
    return list(tail) + list(loop) + inv(tail)


def norm(path, T):
    return [(tuple(c % T for c in b[0]), b[1], b[2]) for b in path]


def current(path, T, d):
    J = np.zeros((d,) + (T,) * d)
    for x, mu, s in norm(path, T):
        J[(mu,) + x] += s
    return J


def incr(E, path, T):
    return np.array([s * E[(mu,) + x] for x, mu, s in norm(path, T)])


def levy(path, E, F, T):
    e = incr(E, path, T)
    f = incr(F, path, T)
    n = len(e)
    tot = 0.0
    for s in range(n):
        for t in range(s + 1, n):
            tot += e[s] * f[t] - e[t] * f[s]
    return tot


def K_comp(paths, Es, T):
    return -12 * (levy(paths[0], Es[1], Es[2], T) + levy(paths[1], Es[2], Es[0], T) + levy(paths[2], Es[0], Es[1], T))


def sumV(E1, E2, E3, T, d):
    """12 sum_p V_p / 12: sum over all plaquettes once, orientation mu < nu, base at x."""
    tot = 0.0
    for mu in range(d):
        for nu in range(mu + 1, d):
            inc = []
            for E in (E1, E2, E3):
                e0 = E[mu]
                e1 = np.roll(E[nu], -1, axis=mu)
                e2 = -np.roll(E[mu], -1, axis=nu)
                e3 = -E[nu]
                inc.append([e0, e1, e2, e3])
            P = [sum(inc[k]) for k in range(3)]
            for s in range(4):
                for t in range(s + 1, 4):
                    a = [P[k] for k in range(3)]
                    b = [inc[k][s] for k in range(3)]
                    c = [inc[k][t] for k in range(3)]
                    det = (a[0] * (b[1] * c[2] - b[2] * c[1])
                           - a[1] * (b[0] * c[2] - b[2] * c[0])
                           + a[2] * (b[0] * c[1] - b[1] * c[0]))
                    tot += det.sum()
    return tot


def grad0(theta, d):
    return np.stack([np.roll(theta, -1, axis=mu) - theta for mu in range(d)])


def curl_at(E, x, mu, nu, T):
    return sum(incr(E, plaq(x, mu, nu), T))
