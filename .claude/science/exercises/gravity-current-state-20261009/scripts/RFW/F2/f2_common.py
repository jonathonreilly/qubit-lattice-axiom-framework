"""F2 (lane RFW) shared symbols: Fourier symbols of K2's Z^4 setting (base-point labels).

Conventions (K2, k2_graviton_gauge_killing.py / k2_scalar_stress_exact.py):
  h_mn[x] at x+(e_m+e_n)/2, xi_n[x] at x+e_n/2, base-point labels; z_mu = exp(i k_mu).
  S = S_FP(h) + S_m(phi) - (kappa/2) sum_x sum_{m,n ordered} h_mn T_mn
  delta0 h_mn = (z_m - 1) xi_n + (z_n - 1) xi_m          (symbol at the momentum of xi)
  L_xi phi (constant xi = c): c . D phi, D = symmetric difference, symbol i sin k.
The 10 independent components a = (m<=n); the coupling to the variable h_a carries weight
w_a = 1 (diag) or 2 (off-diag).  'cross' symbols are the phi1*phi2 coefficient of a bilinear
quantity evaluated on phi = phi1 + phi2 (plane waves with momenta k1, k2).
"""
import numpy as np

D = 4
COMPS = [(m, n) for m in range(D) for n in range(m, D)]
CIDX = {}
for a, (m, n) in enumerate(COMPS):
    CIDX[(m, n)] = a
    CIDX[(n, m)] = a
W = np.array([1.0 if m == n else 2.0 for (m, n) in COMPS])
NC = len(COMPS)


# ---------------------------------------------------------------- lattice scalar (K2)
def E_lat(k, m2):
    return np.sum(2 - 2 * np.cos(k), axis=-1) + m2


def f_lat(k):            # pseudo-translation symbol / i  (D_nu -> i sin k_nu)
    return np.sin(k)


def df_lat(k):           # d f_nu / d k_mu  (diagonal)
    return np.diag(np.cos(k))


def T_lat_cross(k1, k2, m2):
    """K2's stress, cross symbol, 10 components (unweighted)."""
    z1, z2 = np.exp(1j * k1), np.exp(1j * k2)
    out = np.zeros(NC, dtype=complex)
    for a, (m, n) in enumerate(COMPS):
        if m != n:
            def half(za, zb):
                return 0.25 * ((za[m] - 1) * (1 + za[n])) * ((zb[n] - 1) * (1 + zb[m]))
            out[a] = half(z1, z2) + half(z2, z1)
        else:
            val = 0.5 * ((z1[m] - 1) * (z2[m] - 1) / z2[m] + (z2[m] - 1) * (z1[m] - 1) / z1[m])
            for r in range(D):
                if r != m:
                    val += -0.25 * 2 * (z1[r] - 1) * (z2[r] - 1) * (1 + 1 / (z1[r] * z2[r]))
            val += -m2
            out[a] = val * z1[m] * z2[m]
    return out


def dT_lat_dk2(k1, k2, m2, eps=1e-6):
    """d/dk2_mu of T_lat_cross (complex-analytic; 4th-order central differences)."""
    J = np.zeros((NC, D), dtype=complex)
    for mu in range(D):
        e = np.zeros(D); e[mu] = 1
        J[:, mu] = (-T_lat_cross(k1, k2 + 2 * eps * e, m2) + 8 * T_lat_cross(k1, k2 + eps * e, m2)
                    - 8 * T_lat_cross(k1, k2 - eps * e, m2) + T_lat_cross(k1, k2 - 2 * eps * e, m2)) / (12 * eps)
    return J


def L_lat_cross_identity(k1, k2, xi, m2):
    """O(kappa) Noether identity, Fourier form: returns (lhs, rhs) of
       sum_x E*L_xi phi  =  1/2 sum_{ordered mn} delta0h_mn T_mn   (cross terms)."""
    Q = -(k1 + k2)
    z1, z2, zQ = np.exp(1j * k1), np.exp(1j * k2), np.exp(1j * Q)

    def L(zk):
        return 0.5 * np.sum(xi * (zk - 1) * (1 + 1 / (zQ * zk)))
    lhs = E_lat(k1, m2) * L(z2) + E_lat(k2, m2) * L(z1)
    dh = np.array([(zQ[m] - 1) * xi[n] + (zQ[n] - 1) * xi[m] for (m, n) in COMPS])
    rhs = 0.5 * np.sum(W * dh * T_lat_cross(k1, k2, m2))
    return lhs, rhs


# ---------------------------------------------------------------- continuum / SLAC control
def E_con(k, m2):
    return np.sum(k * k, axis=-1) + m2


def f_con(k):
    return k


def df_con(k):
    return np.eye(D, dtype=complex)


def T_con_cross(k1, k2, m2):
    out = np.zeros(NC, dtype=complex)
    for a, (m, n) in enumerate(COMPS):
        out[a] = -(k1[m] * k2[n] + k2[m] * k1[n]) - (1.0 if m == n else 0.0) * (-np.dot(k1, k2) + m2)
    return out


def dT_con_dk2(k1, k2, m2):
    J = np.zeros((NC, D), dtype=complex)
    for a, (m, n) in enumerate(COMPS):
        for mu in range(D):
            v = -(k1[m] * (n == mu) + (m == mu) * k1[n])
            if m == n:
                v += k1[mu]
            J[a, mu] = v
    return J


def L_con_cross_identity(k1, k2, xi, m2):
    Q = -(k1 + k2)
    lhs = E_con(k1, m2) * (1j * np.dot(xi, k2)) + E_con(k2, m2) * (1j * np.dot(xi, k1))
    dh = np.array([1j * Q[m] * xi[n] + 1j * Q[n] * xi[m] for (m, n) in COMPS])
    rhs = 0.5 * np.sum(W * dh * T_con_cross(k1, k2, m2))
    return lhs, rhs


# ---------------------------------------------------------------- FP symbols
def fp_maps(q, lattice=True):
    """linear maps (10-vectors) at momentum q for the lattice / continuum FP action."""
    if lattice:
        z = np.exp(1j * q)
        d = z - 1                         # forward difference
        u = 1 - 1 / z                     # backward difference
        tr_ph = 1 / z                     # trh[z] = sum_r h_rr[z - e_r]
    else:
        d = 1j * q; u = 1j * q; tr_ph = np.ones(D)
    grads = []                            # (coefficient, vector) for 1/4 sum_r sum_{ordered mn} (nabla_r h_mn)^2
    vs, ws = [], []
    for n in range(D):
        v = np.zeros(NC, dtype=complex)
        for m in range(D):
            v[CIDX[(m, n)]] += u[m]
        vs.append(v)
        w = np.zeros(NC, dtype=complex)
        for r in range(D):
            w[CIDX[(r, r)]] += tr_ph[r]
        ws.append(d[n] * w)
    return d, vs, ws


def K_symbol(q, lattice=True):
    """(K h)(q) = K(q) h(q) with S_FP = 1/2 sum_x h.(K h) as a bilinear form in the 10 variables."""
    d, vs, ws = fp_maps(q, lattice)
    dm, vsm, wsm = fp_maps(-q, lattice)
    K = np.zeros((NC, NC), dtype=complex)
    # term 1: 1/4 sum_r sum_ordered (nabla_r h_mn)^2 = 1/4 sum_r sum_a W_a (d_r h_a)^2
    for r in range(D):
        K += 2 * 0.25 * np.diag(W) * dm[r] * d[r]
    for n in range(D):
        K += -0.5 * 2 * np.outer(vsm[n], vs[n])
        K += 0.5 * (np.outer(vsm[n], ws[n]) + np.outer(wsm[n], vs[n]))
        K += -0.25 * 2 * np.outer(wsm[n], ws[n])
    return K


def D_symbol(q, lattice=True):
    if lattice:
        d = np.exp(1j * q) - 1
    else:
        d = 1j * q
    Dm = np.zeros((NC, D), dtype=complex)
    for a, (m, n) in enumerate(COMPS):
        Dm[a, n] += d[m]
        Dm[a, m] += d[n]
    return Dm


# ---------------------------------------------------------------- shell sampling
def shell_point(rng, m2, lattice=True, re=0.9, im=0.35):
    k = rng.normal(size=D) * re + 1j * rng.normal(size=D) * im
    if lattice:
        c3 = 1 + 0.5 * (np.sum(2 - 2 * np.cos(k[:3])) + m2)
        k[3] = np.arccos(c3 + 0j) * rng.choice([-1, 1])
        assert abs(E_lat(k, m2)) < 1e-9
    else:
        k[3] = np.sqrt(-(np.sum(k[:3] ** 2) + m2) + 0j) * rng.choice([-1, 1])
        assert abs(E_con(k, m2)) < 1e-9
    return k


def tangent_basis(n, rng):
    """3 complex vectors t with n.t = 0 (bilinear), n = grad E at p."""
    ts = []
    j = int(np.argmax(np.abs(n)))          # works also for null n (massless cone)
    for _ in range(3):
        v = rng.normal(size=D) + 1j * rng.normal(size=D)
        t = v.copy(); t[j] -= np.dot(n, v) / n[j]
        assert abs(np.dot(n, t)) < 1e-10 * (1 + np.abs(t).max())
        ts.append(t)
    return ts
