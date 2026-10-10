"""R2 step 3 (speed/isotropy tunings) + lattice BZ check + step 4 matter checks
for the scalar-charge versions S and S-tl (the only versions with a stable linear
helicity-2 branch in the strong class)."""
import numpy as np
from r2_common import *

np.set_printoptions(precision=5, suppress=True, linewidth=150)


def Bmat(k):
    """9x6: A (6-vec) -> B_ij = eps_iac k_a A_cj (3x3 flattened)."""
    out = np.zeros((9, 6))
    for b in range(6):
        A = mat(np.eye(6)[b])
        B = np.einsum('iac,a,cj->ij', EPS, k, A)
        out[:, b] = B.ravel()
    return out


def proj9():
    I9 = np.eye(9)
    Pas = np.zeros((9, 9)); Pd = np.zeros((9, 9)); Po = np.zeros((9, 9))
    for c in range(9):
        X = I9[c].reshape(3, 3)
        Pas[:, c] = ((X - X.T) / 2).ravel()
        S = (X + X.T) / 2
        D = np.diag(np.diag(S)) - np.trace(S) / 3 * np.eye(3)
        Pd[:, c] = D.ravel()
        Po[:, c] = (S - np.diag(np.diag(S))).ravel()
    return Pas, Pd, Po


PAS, PD, PO = proj9()
SYM6 = np.array([vec(((np.eye(9)[c].reshape(3, 3)) + (np.eye(9)[c].reshape(3, 3)).T) / 2) for c in range(9)]).T  # 6x9


def model_S(p, k):
    kA1, kE, kT2, mT1, mE, mT2 = p
    K = kA1 * P_A1 + kE * P_E + kT2 * P_T2
    Bm = Bmat(k)
    Q = Bm.T @ (mT1 * PAS + mE * PD + mT2 * PO) @ Bm
    return K, Q


def model_X(x, k):
    xE, xT2 = x
    return 1j * (xE * P_E + xT2 * P_T2) @ SYM6 @ Bmat(k)


def helicity_signed(a, n):
    L = -np.einsum('abc,c->ab', EPS, n)
    La = vec(L @ mat(a) - mat(a) @ L)
    return np.real(1j * np.vdot(a, La)) / np.real(np.vdot(a, a))


def h2_block(p, n, Vf, extra=None):
    """Dynamical matrix D = Kp^1/2 Qp Kp^1/2 (omega^2/k^2) on the physical subspace
    and its helicity-2 eigenvectors at this p."""
    K, Q = model_S(p, n)
    P = phys_projector(Vf(n), extra)
    Kp = P.T @ K @ P; Qp = P.T @ Q @ P
    w, U = np.linalg.eigh(Kp)
    Kh = U @ np.diag(np.sqrt(w)) @ U.T
    D = Kh @ Qp @ Kh
    return D, P, Kh


rng = np.random.default_rng(5)
DIRS = [np.array([0, 0, 1.]), np.array([1, 1, 0]) / S2, np.ones(3) / np.sqrt(3)] + list(rand_dirs(9, rng))


def tuning_count(p0, Vf, free_idx, extra=None, label=''):
    """local codimension of {p : helicity-2 branch isotropic & degenerate} at an
    isotropic point p0, among the parameters free_idx."""
    rows_all = []
    nconds = 0
    blocks = []
    for n in DIRS:
        D0, P, Kh = h2_block(p0, n, Vf, extra)
        w, Y = np.linalg.eigh(D0)
        # helicity of the corresponding A eigenvector a ~ Kh y (up to scale)
        hel = [helicity_sq(P @ (Kh @ Y[:, j]), n) for j in range(len(w))]
        idx = [j for j in range(len(w)) if abs(hel[j] - 4) < 1e-6]
        assert len(idx) == 2, (hel, w)
        assert abs(w[idx[0]] - w[idx[1]]) < 1e-9
        Uh = Y[:, idx]
        blocks.append((n, Uh, w[idx[0]]))
    # Jacobian of the 2x2 helicity-2 blocks w.r.t. parameters; unknown common shift c
    J = []
    h = 1e-6
    for i in free_idx:
        dp = np.array(p0, float); dp[i] += h
        col = []
        for (n, Uh, w0) in blocks:
            D1, _, _ = h2_block(dp, n, Vf, extra)
            D0, _, _ = h2_block(p0, n, Vf, extra)
            M = Uh.T @ (D1 - D0) @ Uh / h
            col += [M[0, 0], M[1, 1], M[0, 1]]
        J.append(col)
    J = np.array(J).T  # (3*ndirs) x nfree
    # allow common isotropic shift: column pattern [1,1,0,...]
    c = np.array([1, 1, 0] * len(blocks), float)[:, None]
    # conditions = rank([J c]) - rank(c)  ... tangent space dim = nfree - (rank(J|c) - 1)
    r = np.linalg.matrix_rank(np.hstack([J, c]), tol=1e-6)
    ncond = r - 1
    print(f'{label}: free params {len(free_idx)}, helicity-2 isotropy conditions (local codim) = {ncond}')
    return ncond


if __name__ == '__main__':
    VS = VERSIONS['S']; VT = VERSIONS['S-tl']
    # sanity: gauge invariance and isotropic point
    k = np.array([0.3, -0.7, 0.5])
    K, Q = model_S([1.3, 0.8, 1.1, 0.6, 0.9, 1.2], k)
    print('S gauge check |Q V| =', np.linalg.norm(Q @ VS(k)))
    print('S-tl: |Q vec(I)| with mT1=0:', np.linalg.norm(model_S([1, 1, 1, 0, 0.9, 1.2], k)[1] @ V_trace(k)),
          ' with mT1!=0:', np.linalg.norm(model_S([1, 1, 1, 0.6, 0.9, 1.2], k)[1] @ V_trace(k)))
    print()
    print('STEP 3: helicity-2 speeds along axes for generic cubic p (S version)')
    p = [1.3, 0.8, 1.15, 0.6, 0.9, 1.25]
    for n in DIRS[:3]:
        D, P, Kh = h2_block(p, n, VS)
        w, Y = np.linalg.eigh(D)
        hel = [helicity_sq(P @ (Kh @ Y[:, j]), n) for j in range(len(w))]
        print(' n=', np.round(n, 3), ' v^2 =', np.round(w, 4), ' <m^2> =', np.round(hel, 3))
    print('  along [001] the two helicity-2 polarisations have v^2 = kE*mT2 and kT2*mE (cubic irreps E/T2 of D4 differ)')
    print('  kE*mT2 =', p[1] * p[5], ' kT2*mE =', p[2] * p[4])
    print()
    p0 = [1.3, 1.0, 1.0, 0.6, 1.0, 1.0]  # isotropic point: kE=kT2, mE=mT2
    tuning_count(p0, VS, [0, 1, 2, 3, 4, 5], label='S (params kA1,kE,kT2,mT1,mE,mT2)')
    tuning_count(p0, VT, [1, 2, 4, 5], extra=V_trace(np.zeros(3)) * 0 + vec(np.eye(3))[:, None], label='S-tl (params kE,kT2,mE,mT2)') if False else None
    # S-tl: physical subspace excludes the trace direction too
    p0t = [1.0, 1.0, 1.0, 0.0, 1.0, 1.0]
    def VTf(n):
        return VT(n)
    tuning_count(p0t, lambda n: VT(n), [1, 2, 4, 5], label='S-tl (params kE,kT2,mE,mT2)')
    print()
    # T-odd / P-odd mixed term E:B -> helicity +2 / -2 splitting
    print('STEP 3b: mixed E:B terms (P-odd, T-odd) at the isotropic point: helicity +2/-2 splitting')
    for x in [(0.1, 0.0), (0.0, 0.1), (0.1, 0.1), (0.1, -0.1)]:
        spl = []
        for n in DIRS[:6]:
            K, Q = model_S(p0, n)
            P = phys_projector(VS(n))
            om, A, Pm = frequencies(K, Q, P, model_X(x, n))
            res = []
            for j in range(len(om)):
                if om[j].real > 1e-9:
                    a = Pm @ A[:, j]
                    res.append((om[j].real, helicity_signed(a, n), helicity_sq(a, n)))
            h2 = sorted([r for r in res if r[2] > 3.0], key=lambda r: r[1])
            spl.append(h2[-1][0] - h2[0][0] if len(h2) >= 2 else np.nan)
        print(f'  (xE,xT2)={x}: omega(+2)-omega(-2) over 6 directions =', np.round(spl, 5))
    print()
    # ---------- lattice BZ check (S, strong, q = 2 sin(k/2), harmonic multiplier)
    print('LATTICE: S model on Z^3 with k->q=2sin(k/2), Q multiplied by f(k)=1+0.4*sum(1-cos k_i)')
    pl = [1.3, 0.8, 1.15, 0.6, 0.9, 1.25]
    L = 14
    ks = [2 * np.pi * np.array(i) / L - np.pi for i in np.ndindex(L, L, L)]
    minw = np.inf; maxim = 0.0; nzero = 0
    for kk in ks:
        q = 2 * np.sin(kk / 2)
        if np.linalg.norm(q) < 1e-12:
            continue
        K, Q = model_S(pl, q)
        Q = Q * (1 + 0.4 * np.sum(1 - np.cos(kk)))
        P = phys_projector(VS(q))
        om, A, Pm = frequencies(K, Q, P)
        pos = om.real[om.real > 0]
        maxim = max(maxim, np.max(np.abs(om.imag)))
        minw = min(minw, pos.min())
        nzero += int(np.sum(np.abs(om) < 1e-8))
    print(f'  {L}^3 grid minus Gamma: min omega = {minw:.4f}, max |Im omega| = {maxim:.1e}, zero modes off Gamma = {nzero}')
    for kap in [0.2, 0.1, 0.05, 0.025]:
        q = 2 * np.sin(kap * np.array([0.31, -0.62, 0.72]) / np.linalg.norm([0.31, -0.62, 0.72]) / 2)
        K, Q = model_S(pl, q)
        P = phys_projector(VS(q))
        om, A, Pm = frequencies(K, Q, P)
        pos = np.sort(om.real[om.real > 0])
        print(f'  |k|={kap}: omega/|k| =', np.round(pos / kap, 4))
    print()
    # ---------- step 4: matter vacuum polarisation through its lattice stress
    print('STEP 4: free lattice scalar coupled to A via hopping (1+A_ii): uniform shear response (paramagnetic)')
    for m in [0.5, 1.0]:
        L = 40
        g = 2 * np.pi * (np.arange(L) + 0.5) / L - np.pi
        qx, qy, qz = np.meshgrid(2 * np.sin(g / 2), 2 * np.sin(g / 2), 2 * np.sin(g / 2), indexing='ij')
        W = qx ** 2 + qy ** 2 + qz ** 2 + m ** 2
        PiE = -np.mean((qx ** 2 - qy ** 2) ** 2 / W ** 1.5) / 8
        print(f'  m={m}: d2E_vac/d eps^2 (E channel, per site) = {PiE:.5f}  (nonzero: a label-dependent shear mass term is generated unless a contact term is tuned)')
