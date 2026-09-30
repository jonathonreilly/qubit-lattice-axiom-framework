"""Pure-gauge SU(3) Wilson lattice Monte Carlo (Cabibbo-Marinari heat bath + overrelaxation), numba.
Written for the T32 attack.  Periodic lattice dims (Lx,Ly,Lz,Lt); site index s = ((x*Ly+y)*Lz+z)*Lt+t.
Links U[s, mu] are 3x3 complex128.  Action S = beta * sum_p (1 - Re Tr U_p / 3).
"""
import math
import numpy as np
import numba as nb

# ---------------------------------------------------------------- lattice tables
def make_tables(dims):
    Lx, Ly, Lz, Lt = dims
    V = Lx * Ly * Lz * Lt
    coords = np.zeros((V, 4), dtype=np.int64)
    s = 0
    for x in range(Lx):
        for y in range(Ly):
            for z in range(Lz):
                for t in range(Lt):
                    coords[s] = (x, y, z, t)
                    s += 1
    def idx(c):
        return ((c[0] % Lx * Ly + c[1] % Ly) * Lz + c[2] % Lz) * Lt + c[3] % Lt
    up = np.zeros((4, V), dtype=np.int64)
    dn = np.zeros((4, V), dtype=np.int64)
    for s in range(V):
        for mu in range(4):
            c = coords[s].copy(); c[mu] += 1; up[mu, s] = idx(c)
            c = coords[s].copy(); c[mu] -= 1; dn[mu, s] = idx(c)
    return up, dn, coords


def cold_start(V):
    U = np.zeros((V, 4, 3, 3), dtype=np.complex128)
    for i in range(3):
        U[:, :, i, i] = 1.0
    return U

# ---------------------------------------------------------------- small 3x3 helpers
@nb.njit(cache=True)
def mm(a, b, c):
    for i in range(3):
        for j in range(3):
            s = a[i, 0] * b[0, j] + a[i, 1] * b[1, j] + a[i, 2] * b[2, j]
            c[i, j] = s

@nb.njit(cache=True)
def dag(a, c):
    for i in range(3):
        for j in range(3):
            c[i, j] = np.conj(a[j, i])

@nb.njit(cache=True)
def staple(U, up, dn, s, mu, A, t1, t2, t3, d1, d2):
    for i in range(3):
        for j in range(3):
            A[i, j] = 0.0
    for nu in range(4):
        if nu == mu:
            continue
        s_pm = up[mu, s]
        s_pn = up[nu, s]
        s_mn = dn[nu, s]
        s_pm_mn = dn[nu, s_pm]
        # forward: U_nu(x+mu) U_mu^dag(x+nu) U_nu^dag(x)
        dag(U[s_pn, mu], d1)
        mm(U[s_pm, nu], d1, t1)
        dag(U[s, nu], d2)
        mm(t1, d2, t2)
        for i in range(3):
            for j in range(3):
                A[i, j] += t2[i, j]
        # backward: U_nu^dag(x+mu-nu) U_mu^dag(x-nu) U_nu(x-nu)
        dag(U[s_pm_mn, nu], d1)
        dag(U[s_mn, mu], d2)
        mm(d1, d2, t1)
        mm(t1, U[s_mn, nu], t2)
        for i in range(3):
            for j in range(3):
                A[i, j] += t2[i, j]

# ---------------------------------------------------------------- SU(2) subgroup updates
@nb.njit(cache=True)
def kp_a0(alpha):
    while True:
        r1 = 1.0 - np.random.random()
        r2 = np.random.random()
        r3 = 1.0 - np.random.random()
        r4 = np.random.random()
        c = math.cos(2.0 * math.pi * r2)
        x = -(math.log(r1) + c * c * math.log(r3)) / alpha
        if r4 * r4 <= 1.0 - 0.5 * x:
            return 1.0 - x

@nb.njit(cache=True)
def update_link(U, s, mu, A, beta, overrelax, W, R, t1):
    # W = U A ; act on the three SU(2) subgroups with left multiplication U <- V U
    mm(U[s, mu], A, W)
    for p in range(3):
        if p == 0:
            i = 0; j = 1
        elif p == 1:
            i = 0; j = 2
        else:
            i = 1; j = 2
        a = W[i, i]; b = W[i, j]; c = W[j, i]; d = W[j, j]
        q0 = 0.5 * (a.real + d.real)
        q3 = 0.5 * (a.imag - d.imag)
        q1 = 0.5 * (b.imag + c.imag)
        q2 = 0.5 * (b.real - c.real)
        k = math.sqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3)
        if k < 1e-12:
            continue
        u0 = q0 / k; u1 = q1 / k; u2 = q2 / k; u3 = q3 / k
        if overrelax:
            v0 = u0 * u0 - u1 * u1 - u2 * u2 - u3 * u3
            f = -2.0 * u0
            v1 = f * u1; v2 = f * u2; v3 = f * u3
            Va = complex(v0, v3); Vb = complex(v2, v1); Vc = complex(-v2, v1); Vd = complex(v0, -v3)
        else:
            alpha = 2.0 * beta * k / 3.0
            x0 = kp_a0(alpha)
            rr = math.sqrt(max(0.0, 1.0 - x0 * x0))
            ct = 2.0 * np.random.random() - 1.0
            st = math.sqrt(max(0.0, 1.0 - ct * ct))
            ph = 2.0 * math.pi * np.random.random()
            x1 = rr * st * math.cos(ph); x2 = rr * st * math.sin(ph); x3 = rr * ct
            Xa = complex(x0, x3); Xb = complex(x2, x1); Xc = complex(-x2, x1); Xd = complex(x0, -x3)
            Ua = complex(u0, -u3); Ub = complex(-u2, -u1); Uc = complex(u2, -u1); Ud = complex(u0, u3)
            Va = Xa * Ua + Xb * Uc; Vb = Xa * Ub + Xb * Ud
            Vc = Xc * Ua + Xd * Uc; Vd = Xc * Ub + Xd * Ud
        for r in range(3):
            for cc in range(3):
                R[r, cc] = 0.0
        for r in range(3):
            R[r, r] = 1.0
        R[i, i] = Va; R[i, j] = Vb; R[j, i] = Vc; R[j, j] = Vd
        mm(R, U[s, mu], t1)
        for r in range(3):
            for cc in range(3):
                U[s, mu][r, cc] = t1[r, cc]
        mm(R, W, t1)
        for r in range(3):
            for cc in range(3):
                W[r, cc] = t1[r, cc]

@nb.njit(cache=True)
def reunitarize(m):
    # Gram-Schmidt rows, third row = conj(cross(r0,r1)) -> SU(3)
    n0 = 0.0
    for j in range(3):
        n0 += (m[0, j] * np.conj(m[0, j])).real
    n0 = math.sqrt(n0)
    for j in range(3):
        m[0, j] /= n0
    dot = 0j
    for j in range(3):
        dot += np.conj(m[0, j]) * m[1, j]
    for j in range(3):
        m[1, j] -= dot * m[0, j]
    n1 = 0.0
    for j in range(3):
        n1 += (m[1, j] * np.conj(m[1, j])).real
    n1 = math.sqrt(n1)
    for j in range(3):
        m[1, j] /= n1
    m[2, 0] = np.conj(m[0, 1] * m[1, 2] - m[0, 2] * m[1, 1])
    m[2, 1] = np.conj(m[0, 2] * m[1, 0] - m[0, 0] * m[1, 2])
    m[2, 2] = np.conj(m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0])

@nb.njit(cache=True)
def seed(n):
    np.random.seed(n)

@nb.njit(cache=True)
def sweep(U, up, dn, beta, n_or):
    V = U.shape[0]
    A = np.zeros((3, 3), dtype=np.complex128)
    W = np.zeros((3, 3), dtype=np.complex128)
    R = np.zeros((3, 3), dtype=np.complex128)
    t1 = np.zeros((3, 3), dtype=np.complex128)
    t2 = np.zeros((3, 3), dtype=np.complex128)
    t3 = np.zeros((3, 3), dtype=np.complex128)
    d1 = np.zeros((3, 3), dtype=np.complex128)
    d2 = np.zeros((3, 3), dtype=np.complex128)
    # one heat bath sweep then n_or overrelaxation sweeps
    for rep in range(1 + n_or):
        orflag = rep > 0
        for s in range(V):
            for mu in range(4):
                staple(U, up, dn, s, mu, A, t1, t2, t3, d1, d2)
                update_link(U, s, mu, A, beta, orflag, W, R, t1)
    # reunitarize
    for s in range(V):
        for mu in range(4):
            reunitarize(U[s, mu])

# ---------------------------------------------------------------- observables
@nb.njit(cache=True)
def plaquette_avg(U, up):
    V = U.shape[0]
    t1 = np.zeros((3, 3), dtype=np.complex128)
    t2 = np.zeros((3, 3), dtype=np.complex128)
    d1 = np.zeros((3, 3), dtype=np.complex128)
    d2 = np.zeros((3, 3), dtype=np.complex128)
    tot = 0.0
    for s in range(V):
        for mu in range(4):
            for nu in range(mu + 1, 4):
                mm(U[s, mu], U[up[mu, s], nu], t1)
                dag(U[up[nu, s], mu], d1)
                dag(U[s, nu], d2)
                mm(t1, d1, t2)
                mm(t2, d2, t1)
                tot += (t1[0, 0] + t1[1, 1] + t1[2, 2]).real / 3.0
    return tot / (V * 6.0)

@nb.njit(cache=True)
def polyakov(U, up, coords, Lt):
    """Return complex Polyakov loop for every spatial site (loop along direction 3)."""
    V = U.shape[0]
    Ls = V // Lt
    out = np.zeros(Ls, dtype=np.complex128)
    t1 = np.zeros((3, 3), dtype=np.complex128)
    P = np.zeros((3, 3), dtype=np.complex128)
    n = 0
    for s in range(V):
        if coords[s, 3] != 0:
            continue
        for i in range(3):
            for j in range(3):
                P[i, j] = 1.0 if i == j else 0.0
        cur = s
        for k in range(Lt):
            mm(P, U[cur, 3], t1)
            for i in range(3):
                for j in range(3):
                    P[i, j] = t1[i, j]
            cur = up[3, cur]
        out[n] = (P[0, 0] + P[1, 1] + P[2, 2]) / 3.0
        n += 1
    return out

@nb.njit(cache=True)
def ape_smear_spatial(U, up, dn, w, nsteps):
    """3D APE smearing of links mu=0,1,2 (staples only in spatial planes), reunitarized. Returns new array."""
    V = U.shape[0]
    Uc = U.copy()
    Un = U.copy()
    t1 = np.zeros((3, 3), dtype=np.complex128)
    t2 = np.zeros((3, 3), dtype=np.complex128)
    d1 = np.zeros((3, 3), dtype=np.complex128)
    d2 = np.zeros((3, 3), dtype=np.complex128)
    S = np.zeros((3, 3), dtype=np.complex128)
    for it in range(nsteps):
        for s in range(V):
            for mu in range(3):
                for i in range(3):
                    for j in range(3):
                        S[i, j] = 0.0
                for nu in range(3):
                    if nu == mu:
                        continue
                    s_pm = up[mu, s]; s_pn = up[nu, s]; s_mn = dn[nu, s]; s_pm_mn = dn[nu, s_pm]
                    dag(Uc[s_pn, mu], d1)
                    mm(Uc[s_pm, nu], d1, t1)
                    dag(Uc[s, nu], d2)
                    mm(t1, d2, t2)
                    dag(t2, d1)
                    for i in range(3):
                        for j in range(3):
                            S[i, j] += d1[i, j]
                    dag(Uc[s_pm_mn, nu], d1)
                    dag(Uc[s_mn, mu], d2)
                    mm(d1, d2, t1)
                    mm(t1, Uc[s_mn, nu], t2)
                    dag(t2, d1)
                    for i in range(3):
                        for j in range(3):
                            S[i, j] += d1[i, j]
                for i in range(3):
                    for j in range(3):
                        Un[s, mu][i, j] = Uc[s, mu][i, j] + w * S[i, j]
                reunitarize(Un[s, mu])
        for s in range(V):
            for mu in range(3):
                for i in range(3):
                    for j in range(3):
                        Uc[s, mu][i, j] = Un[s, mu][i, j]
    return Uc

@nb.njit(cache=True)
def wloops(U, up, mu, nu, Rmax, Tmax):
    """<W(R,T)> (real part of normalised trace) with R along mu, T along nu, averaged over all sites.
    Uses line products; loop closes on itself for R,T < L."""
    V = U.shape[0]
    Wsum = np.zeros((Rmax + 1, Tmax + 1))
    S = np.zeros((V, Rmax + 1, 3, 3), dtype=np.complex128)   # S[s,R] = prod_{k<R} U_mu(x + k mu)
    T = np.zeros((V, Tmax + 1, 3, 3), dtype=np.complex128)   # T[s,T] = prod_{k<T} U_nu(x + k nu)
    t1 = np.zeros((3, 3), dtype=np.complex128)
    for s in range(V):
        for i in range(3):
            S[s, 0, i, i] = 1.0
            T[s, 0, i, i] = 1.0
    for r in range(1, Rmax + 1):
        for s in range(V):
            cur = s
            # S[s,r] = S[s,r-1] * U_mu(x + (r-1) mu)
            cur = s
            for k in range(r - 1):
                cur = up[mu, cur]
            mm(S[s, r - 1], U[cur, mu], t1)
            for i in range(3):
                for j in range(3):
                    S[s, r, i, j] = t1[i, j]
    for tt in range(1, Tmax + 1):
        for s in range(V):
            cur = s
            for k in range(tt - 1):
                cur = up[nu, cur]
            mm(T[s, tt - 1], U[cur, nu], t1)
            for i in range(3):
                for j in range(3):
                    T[s, tt, i, j] = t1[i, j]
    a = np.zeros((3, 3), dtype=np.complex128)
    b = np.zeros((3, 3), dtype=np.complex128)
    c = np.zeros((3, 3), dtype=np.complex128)
    d = np.zeros((3, 3), dtype=np.complex128)
    for r in range(1, Rmax + 1):
        for tt in range(1, Tmax + 1):
            acc = 0.0
            for s in range(V):
                sr = s
                for k in range(r):
                    sr = up[mu, sr]
                st = s
                for k in range(tt):
                    st = up[nu, st]
                # W = tr[ S(s,r) T(s+r mu, tt) S(s+tt nu, r)^dag T(s,tt)^dag ]
                mm(S[s, r], T[sr, tt], a)
                dag(S[st, r], b)
                mm(a, b, c)
                dag(T[s, tt], d)
                mm(c, d, a)
                acc += (a[0, 0] + a[1, 1] + a[2, 2]).real / 3.0
            Wsum[r, tt] = acc / V
    return Wsum

@nb.njit(cache=True)
def glue_op(U, up, Lt, coords):
    """Zero-momentum 0++ operator per time slice: sum over spatial plaquettes (3 planes) of Re tr U_p /3.
    U should be spatially smeared."""
    V = U.shape[0]
    out = np.zeros(Lt)
    t1 = np.zeros((3, 3), dtype=np.complex128)
    t2 = np.zeros((3, 3), dtype=np.complex128)
    d1 = np.zeros((3, 3), dtype=np.complex128)
    d2 = np.zeros((3, 3), dtype=np.complex128)
    for s in range(V):
        tcoord = coords[s, 3]
        for mu in range(3):
            for nu in range(mu + 1, 3):
                mm(U[s, mu], U[up[mu, s], nu], t1)
                dag(U[up[nu, s], mu], d1)
                dag(U[s, nu], d2)
                mm(t1, d1, t2)
                mm(t2, d2, t1)
                out[tcoord] += (t1[0, 0] + t1[1, 1] + t1[2, 2]).real / 3.0
    return out
