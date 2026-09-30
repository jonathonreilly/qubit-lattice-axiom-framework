"""T69 test: does the filled sea (the zero-temperature log-det readout) supply the
lapse field's stiffness, and is that number walk-independent?

Model (landed notes b53-b55, b76, b130): H = sum_a sigma_a s(k_a) (3D) or sigma_3 s(k) (1D),
H_w = phi H phi, phi = exp(u/2), u = eps cos(q.x); sea = all negative levels filled.
a2(q) = coefficient of eps^2 in E_-/site.  kappa = 4 (a2(q)-a2(0))/|q|^2_lat.

Two independent computations of a2(q) are compared (gate G0):
  ED : exact diagonalisation on an antiperiodic torus, central second difference in eps
  BZ : second-order perturbation theory in k-space (formula below), any mesh size
BZ formula (derived here; symbol h(k) = sigma.s(k), n = s/|s|, s'=s(k+q)):
  a2 = < -|s|/8 - (1/16) n.(s(k+q)+s(k-q)) >_k - (1/16) < (|s|-|s'|)^2 (1 - n.n') / (|s|+|s'|) >_k
"""
import numpy as np, sys, json, time

def s_fun(k, mu):
    return (1 - mu) * np.sin(k) + mu * np.sin(2 * k) / 2

# ---------------------------------------------------------------- BZ formula
def a2_bz(N, mshift, mu=0.0, dim=3, direction='x'):
    """coefficient of eps^2 in E_-/site, and c0=E_-/site, on the antiperiodic N^dim mesh,
    q = 2 pi mshift / N along x-hat ('x') or (1,1,1) ('d')."""
    ks = 2 * np.pi * (np.arange(N) + 0.5) / N
    if dim == 3:
        kx, ky, kz = np.meshgrid(ks, ks, ks, indexing='ij')
        s = np.stack([s_fun(kx, mu), s_fun(ky, mu), s_fun(kz, mu)], axis=-1)
        axes = (0,) if direction == 'x' else (0, 1, 2)
    else:
        s = np.stack([0 * ks, 0 * ks, s_fun(ks, mu)], axis=-1)
        axes = (0,)
    absS = np.linalg.norm(s, axis=-1)
    n = s / absS[..., None]
    sp = np.roll(s, -mshift, axis=axes)   # s(k+q)
    sm = np.roll(s, +mshift, axis=axes)   # s(k-q)
    absSp = np.linalg.norm(sp, axis=-1)
    npv = sp / absSp[..., None]
    diag = -absS / 8 - (1 / 16) * np.einsum('...i,...i->...', n, sp + sm)
    pert = -(1 / 16) * (absS - absSp) ** 2 * (1 - np.einsum('...i,...i->...', n, npv)) / (absS + absSp)
    c0 = -absS.mean()
    return diag.mean() + pert.mean(), c0

def qlat2(N, mshift, dim=3, direction='x'):
    q = 2 * np.pi * mshift / N
    if dim == 3 and direction == 'd':
        return 3 * (2 - 2 * np.cos(q))  # lattice Laplacian symbol; continuum |q|^2 = 3 q^2
    return 2 - 2 * np.cos(q)

# ---------------------------------------------------------------- ED
def build_H(L, mu, dim=3):
    """dense H = sum_a sigma_a s(-i d_a), antiperiodic torus, s via hoppings sin -> (T-T^-1)/2i, sin2k -> (T^2-T^-2)/2i"""
    sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    dims = [L] * dim
    nsite = L ** dim
    def idx(c):
        i = 0
        for a in range(dim):
            i = i * L + c[a]
        return i
    coords = np.array(np.meshgrid(*[np.arange(L)] * dim, indexing='ij')).reshape(dim, -1).T
    H = np.zeros((2 * nsite, 2 * nsite), complex)
    for a in range(dim):
        sg = sig[a] if dim == 3 else sig[2]
        for c in coords:
            i = idx(c)
            for p, wgt in ((1, (1 - mu) / (2j)), (2, mu / 2 / (2j))):
                if abs(wgt) == 0:
                    continue
                for sign in (+1, -1):     # (T^p - T^-p)/(2i) : T^p psi(x)=psi(x+p e)
                    c2 = c.copy()
                    c2[a] += sign * p
                    phase = 1.0
                    if c2[a] >= L:
                        c2[a] -= L; phase = -1.0
                    if c2[a] < 0:
                        c2[a] += L; phase = -1.0
                    j = idx(c2)
                    H[2 * i:2 * i + 2, 2 * j:2 * j + 2] += sign * wgt * phase * sg
    assert np.allclose(H, H.conj().T)
    return H, coords

def E_minus(H, coords, L, eps, mshift, mu, direction='x', dim=3):
    q = 2 * np.pi * mshift / L
    if dim == 3 and direction == 'd':
        u = eps * np.cos(q * coords.sum(1))
    else:
        u = eps * np.cos(q * coords[:, 0])
    phi = np.exp(np.repeat(u, 2) / 2)
    Hw = phi[:, None] * H * phi[None, :]
    ev = np.linalg.eigvalsh(Hw)
    return ev[ev < 0].sum()

def a2_ed(L, mshift, mu=0.0, dim=3, direction='x'):
    H, coords = build_H(L, mu, dim)
    nsite = L ** dim
    E0 = E_minus(H, coords, L, 0.0, mshift, mu, direction, dim)
    def sec(e):
        return (E_minus(H, coords, L, e, mshift, mu, direction, dim)
                + E_minus(H, coords, L, -e, mshift, mu, direction, dim) - 2 * E0) / (2 * e * e)
    e = 0.004
    v1, v2 = sec(e), sec(2 * e)
    return ((4 * v1 - v2) / 3) / nsite, E0 / nsite

if __name__ == '__main__':
    out = {}
    t0 = time.time()
    # ------------------------------------------------ G0: ED vs BZ
    g0 = []
    for (L, m, mu, dim, d) in [(6, 1, 0.0, 3, 'x'), (6, 2, 0.0, 3, 'x'), (6, 1, 0.0, 3, 'd'), (6, 1, 0.25, 3, 'x'),
                              (64, 1, 0.0, 1, 'x'), (64, 3, 0.3, 1, 'x')]:
        aed, c0ed = a2_ed(L, m, mu, dim, d)
        abz, c0bz = a2_bz(L, m, mu, dim, d)
        g0.append(dict(L=L, m=m, mu=mu, dim=dim, dir=d, a2_ED=aed, a2_BZ=abz, c0_ED=c0ed, c0_BZ=c0bz,
                       rel=abs(aed - abz) / abs(abz)))
        print('G0', g0[-1], flush=True)
    out['G0'] = g0
    out['G0_pass'] = all(r['rel'] < 1e-7 for r in g0)
    print('G0 pass:', out['G0_pass'], 'time', time.time() - t0, flush=True)
    json.dump(out, open('T69_results_partial.json', 'w'), indent=1)
