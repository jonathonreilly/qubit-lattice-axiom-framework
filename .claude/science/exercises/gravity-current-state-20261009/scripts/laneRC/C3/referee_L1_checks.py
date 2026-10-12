"""Independent checks for the Lane-RN L1 referee report.

This does not import any l1_* worker module.  It checks (i) the scalar
continuity identities in exact rational arithmetic, (ii) the reported
matter-only closure residual by a dense SVD rather than sparse LSQR, and
(iii) the TT susceptibility by a different quadrature.  The last block also
prints the seagull contribution forced by an isospectral unitary completion.
"""
from fractions import Fraction as F

import numpy as np
from numpy.polynomial.legendre import leggauss


AX = range(3)


def exact_scalar_check(L=3, mass=F(3, 5)):
    """Evaluate E and M exactly on deterministic integer phase-space data."""
    sites = [(a, b, c) for a in range(L) for b in range(L) for c in range(L)]

    def add(x, j, n=1):
        y = list(x)
        y[j] = (y[j] + n) % L
        return tuple(y)

    phi = {x: F(((17*x[0] + 11*x[1] + 5*x[2] + 3) % 13) - 6) for x in sites}
    pi = {x: F(((7*x[0] + 19*x[1] + 2*x[2] + 1) % 11) - 5) for x in sites}

    def d(field, x, j):
        return field[add(x, j)] - field[x]

    phidot = pi
    pidot = {
        x: sum((phi[add(x, j)] + phi[add(x, j, -1)] - 2*phi[x] for j in AX), F(0))
        - mass*mass*phi[x]
        for x in sites
    }

    def product_dot(a, adot, b, bdot):
        return adot*b + a*bdot

    P = {(x, j): F(1, 2)*(pi[x] + pi[add(x, j)])*d(phi, x, j) for x in sites for j in AX}
    dP = {}
    for x in sites:
        for j in AX:
            av = F(1, 2)*(pi[x] + pi[add(x, j)])
            adv = F(1, 2)*(pidot[x] + pidot[add(x, j)])
            dv = d(phi, x, j)
            ddv = d(phidot, x, j)
            dP[x, j] = product_dot(av, adv, dv, ddv)

    dT00 = {}
    Tdiag = {}
    Toff = {}
    for x in sites:
        val = pi[x]*pidot[x] + mass*mass*phi[x]*phidot[x]
        for j in AX:
            val += F(1, 2)*(d(phi, x, j)*d(phidot, x, j)
                            + d(phi, add(x, j, -1), j)*d(phidot, add(x, j, -1), j))
        dT00[x] = val
        for j in AX:
            tj = F(1, 2)*pi[x]**2 - F(1, 2)*mass**2*phi[x]**2
            tj += F(1, 2)*d(phi, x, j)*d(phi, add(x, j, -1), j)
            for i in AX:
                if i != j:
                    tj -= F(1, 4)*(d(phi, x, i)**2 + d(phi, add(x, i, -1), i)**2)
            Tdiag[x, j] = tj
        for i in AX:
            for j in AX:
                if i < j:
                    Toff[x, i, j] = F(1, 4)*(d(phi, x, i) + d(phi, add(x, j), i)) \
                                              *(d(phi, x, j) + d(phi, add(x, i), j))

    e_res = []
    m_res = []
    for x in sites:
        divp = sum((P[x, j] - P[add(x, j, -1), j] for j in AX), F(0))
        e_res.append(dT00[x] - divp)
        for j in AX:
            gt = Tdiag[add(x, j), j] - Tdiag[x, j]
            for i in AX:
                if i != j:
                    key = (min(i, j), max(i, j))
                    gt += Toff[(x,) + key] - Toff[(add(x, i, -1),) + key]
            m_res.append(dP[x, j] - gt)
    return max(map(abs, e_res)), max(map(abs, m_res))


def qform(vecs, n):
    """Matrix A for Q=1/2 z^T A z from (coefficient,u,v) products."""
    out = np.zeros((2*n, 2*n))
    for coefficient, u, v in vecs:
        out += coefficient*(np.outer(u, v) + np.outer(v, u))
    return out


def dense_closure_residual(L=4, mass=0.6):
    """Independent dense-SVD version of the worker's 3D matter-only fit."""
    V = L**3
    shape = (L, L, L)
    index = np.arange(V).reshape(shape)

    def site(x):
        return index[tuple(np.asarray(x) % L)]

    def unit(slot):
        v = np.zeros(2*V)
        v[slot] = 1
        return v

    T00 = []
    P = [[], [], []]
    coords = list(np.ndindex(shape))
    for xt in coords:
        x = np.asarray(xt)
        terms = [(0.5, unit(V + site(x)), unit(V + site(x))),
                 (0.5*mass**2, unit(site(x)), unit(site(x)))]
        for j in AX:
            e = np.eye(3, dtype=int)[j]
            for y in (x, x-e):
                df = unit(site(y+e)) - unit(site(y))
                terms.append((0.25, df, df))
        T00.append(qform(terms, V))
        for j in AX:
            e = np.eye(3, dtype=int)[j]
            pav = 0.5*(unit(V + site(x)) + unit(V + site(x+e)))
            df = unit(site(x+e)) - unit(site(x))
            P[j].append(qform([(1.0, pav, df)], V))

    omega = np.block([[np.zeros((V, V)), np.eye(V)], [-np.eye(V), np.zeros((V, V))]])
    rng = np.random.default_rng(8102026)
    xi = [rng.standard_normal(V) for _ in AX]
    eta = [rng.standard_normal(V) for _ in AX]
    pxi = sum((xi[j][x]*P[j][x] for j in AX for x in range(V)), np.zeros_like(omega))
    peta = sum((eta[j][x]*P[j][x] for j in AX for x in range(V)), np.zeros_like(omega))
    bracket = pxi@omega@peta - peta@omega@pxi
    basis = [P[j][x] for j in AX for x in range(V)] + T00
    design = np.column_stack([b.ravel() for b in basis])
    coeff, *_ = np.linalg.lstsq(design, bracket.ravel(), rcond=None)
    residual = np.linalg.norm(design@coeff - bracket.ravel())/np.linalg.norm(bracket)
    overlap = np.linalg.norm(design.T@bracket.ravel())/np.linalg.norm(bracket)
    return residual, overlap


def tt_quadrature(order=80):
    """Tensor Gauss-Legendre quadrature on [-pi,pi]^3, not the worker's grid."""
    x, weight = leggauss(order)
    k = np.pi*x
    weight = weight/2  # normalized one-dimensional Brillouin-zone average
    sx = np.sin(k)
    q2 = (2*np.sin(k/2))**2
    out = {}
    # Slice over k_z to avoid allocating several order^3 work arrays.
    for mass in (0.0, 0.5, 1.0):
        num_e = 0.0
        num_t = 0.0
        for iz in range(order):
            w2 = mass*mass + q2[:, None] + q2[None, :] + q2[iz]
            omega = np.sqrt(w2)
            xe = sx[:, None]**2 - sx[None, :]**2
            xt = 2*sx[:, None]*sx[None, :]
            ww = weight[:, None]*weight[None, :]*weight[iz]
            num_e += np.sum(ww*xe**2/omega**3)
            num_t += np.sum(ww*xt**2/omega**3)
        para_e = -num_e/8
        para_t = -num_t/8
        # If H(h)=exp(-i K_h) H(0) exp(+i K_h),
        # H_sg=-(1/2)[K_h,[K_h,H(0)]].  The f-sum rule fixes its
        # vacuum Hessian to the exact opposite of the paramagnetic Hessian.
        out[mass] = (para_e, para_t, -para_e, -para_t)
    return out


if __name__ == "__main__":
    er, mr = exact_scalar_check()
    print("exact rational scalar residuals: E =", er, "M =", mr)
    residual, overlap = dense_closure_residual()
    print(f"dense-SVD 3D {{P,P}} fit: relative residual = {residual:.12f}; normalized basis overlap = {overlap:.3e}")
    print("Gauss-Legendre TT Hessians (paramagnetic E,T2; unitary-seagull E,T2):")
    for mass, values in tt_quadrature().items():
        print(f"m={mass:.1f}: {values[0]:+.9f} {values[1]:+.9f}; {values[2]:+.9f} {values[3]:+.9f}; sums {values[0]+values[2]:+.1e} {values[1]+values[3]:+.1e}")
