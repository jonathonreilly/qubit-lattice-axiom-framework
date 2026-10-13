"""F3 validation with explicit 4x4 matrices (no reduced formula), full-BZ midpoint grid, t = 0 (unstrained root law):
 (1) the exact D-H dressing H' = V H V^dag (V = expm(i eps G_f)) equals f3_lib.rotate's (c, M) rotation;
 (2) matrix one-loop beta-component of Sigma(P=0) (Q0 done analytically by H's spectral decomposition) equals f3_lib.dm_gen
     on the same nodes, undressed and dressed;
 (3) linear response L[G] = d/d eps dm[V H V^dag] for representative generators of every nonempty (P,T,C) sector of the
     cubic-covariant space (f3_sym.out): symmetry-odd ones must give 0 (proved symmetry lemma), symmetric ones not;
 (4) literal-branch generators ([G, beta] = 0) all give 0.
Matrix formula (psi-bar form as f1_validate2.py:25-29, with S = (iQ0 + H)^-1 g0):
  dm = < sum_j tr(beta T_j)/4 /(2 Om) >  + < tr(beta X)/4 - sum_j tr(beta V_j X V_j)/4 >,  X = sum_n P_n sgn(E_n)/(2 Om (|E_n| + Om)),
  V_j = Psym divided differences of H' (hermitian), T_j = [H'(q_j e_j) + H'(-q_j e_j) - 2 H'(0)]/(2 d_j^2)."""
import numpy as np, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch'))
from f3_dirac import *
from f3_lib import *

t0 = time.time()
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)

def Hfun(k):                      # undressed root H at k (..., 3)
    c = [F.s(k[..., j]) for j in range(3)]
    M = F.W(k[..., 0]) + F.W(k[..., 1]) + F.W(k[..., 2])
    return H_of(c, M)

ib = [1j*beta @ alpha[j] for j in range(3)]
def mk(mats_funcs):
    """generator G(k) = sum (matrix x scalar function)."""
    def Gk(k):
        out = 0
        for Mt, fn in mats_funcs:
            out = out + np.multiply.outer(fn(k), Mt)
        return out
    return Gk
sx = lambda j: (lambda k: np.sin(k[..., j]))
cc = lambda k: np.cos(k[..., 0]) + np.cos(k[..., 1]) + np.cos(k[..., 2])
ccc = lambda k: np.cos(k[..., 0])*np.cos(k[..., 1]) + np.cos(k[..., 1])*np.cos(k[..., 2]) + np.cos(k[..., 2])*np.cos(k[..., 0])
s2j = lambda j: (lambda k: np.sin(k[..., j])*(np.cos(k[..., (j+1) % 3]) + np.cos(k[..., (j+2) % 3])))
GEN = {
    'G1 = sum i beta alpha_j sin k_j': mk([(ib[j], sx(j)) for j in range(3)]),
    'G2 = sum i beta alpha_j sin k_j (cos k_l + cos k_m)': mk([(ib[j], s2j(j)) for j in range(3)]),
    'beta (const)': mk([(beta, lambda k: np.ones(k.shape[:-1]))]),
    'beta sum cos k_j': mk([(beta, cc)]),
    'beta sum cos k_j cos k_l': mk([(beta, ccc)]),
    'sum alpha_j sin k_j': mk([(alpha[j], sx(j)) for j in range(3)]),
    'sum alpha_j sin k_j (cos+cos)': mk([(alpha[j], s2j(j)) for j in range(3)]),
    '1 x sum cos k_j (commutes)': mk([(I4, cc)]),
    'sum Sigma_j sin k_j': mk([(Sigma[j], sx(j)) for j in range(3)]),
    'sum beta Sigma_j sin k_j': mk([(beta @ Sigma[j], sx(j)) for j in range(3)]),
    'g5 (const)': mk([(g5, lambda k: np.ones(k.shape[:-1]))]),
    'i beta g5 sum cos k_j': mk([(1j*beta @ g5, cc)]),
    'g5 sum cos k_j': mk([(g5, cc)]),
    'sum g5 alpha_j sin k_j': mk([(g5 @ alpha[j], sx(j)) for j in range(3)]) if np.allclose(g5 @ alpha[0], (g5 @ alpha[0]).conj().T) else None,
}
GEN = {k: v for k, v in GEN.items() if v is not None}

R3 = [rot90(a) for a in range(3)]; SR = [spin90(a) for a in range(3)]
rng = np.random.default_rng(3); Ks = rng.uniform(-np.pi, np.pi, (30, 3))
def parities(Gk):
    g = Gk(Ks)
    cub = max(np.abs(Gk(Ks @ R3[a].T) - SR[a] @ g @ SR[a].conj().T).max() for a in range(3))
    out = {}
    for nm, op in (('P', lambda: beta @ Gk(-Ks) @ beta), ('T', lambda: -U_T @ Gk(-Ks).conj() @ U_T.conj().T),
                   ('C', lambda: -U_C @ Gk(-Ks).conj() @ U_C.conj().T)):
        h = op()
        out[nm] = '+' if np.allclose(h, g) else ('-' if np.allclose(h, -g) else '?')
    comm_b = np.abs(g @ beta - beta @ g).max()
    return cub, out, comm_b

# (1) rotation formula vs expm
print('(1) exact D-H dressing vs f3_lib.rotate (eps = 0.3, 200 random k):')
K1 = rng.uniform(-np.pi, np.pi, (200, 3))
for nm in ('G1', 'G2'):
    Gk = GEN[[k for k in GEN if k.startswith(nm)][0]]
    lam, U = np.linalg.eigh(Gk(K1)); V = U @ (np.exp(1j*0.3*lam)[..., None]*U.conj().swapaxes(-1, -2))
    Hd = V @ Hfun(K1) @ V.conj().swapaxes(-1, -2)
    c0 = tuple(F.s(K1[:, j]) for j in range(3)); M0 = F.W(K1[:, 0]) + F.W(K1[:, 1]) + F.W(K1[:, 2])
    c2, M2 = rotate(c0, M0, fvec(nm, K1[:, 0], K1[:, 1], K1[:, 2]), 0.3)
    print('   %s: max|H_expm - H_rot| = %.1e ; E preserved: %.1e' % (nm, np.abs(Hd - H_of(c2, M2)).max(),
          np.abs(np.linalg.eigvalsh(Hd) - np.linalg.eigvalsh(Hfun(K1))).max()))

def dm_mat(Gk, eps, N):
    """matrix one-loop dm on the full-BZ midpoint grid (N^3), dressing V = expm(i eps G)."""
    x = -np.pi + (np.arange(N) + 0.5)*2*np.pi/N
    d = G.d(x); w = 1.0/N
    def Hd(k):
        H = Hfun(k)
        if Gk is None or eps == 0.0:
            return H
        lam, U = np.linalg.eigh(Gk(k)); V = U @ (np.exp(1j*eps*lam)[..., None]*U.conj().swapaxes(-1, -2))
        return V @ H @ V.conj().swapaxes(-1, -2)
    def P3(a, b, c):
        a, b, c = np.broadcast_arrays(a, b, c)
        return np.stack([a, b, c], -1)
    z = 0*x
    H0 = Hd(np.zeros(3))
    Hx, Hy, Hz = Hd(P3(x, z, z)), Hd(P3(z, x, z)), Hd(P3(z, z, x))
    Hxm, Hym, Hzm = Hd(P3(-x, z, z)), Hd(P3(z, -x, z)), Hd(P3(z, z, -x))
    T = [(Hx + Hxm - 2*H0)/(2*d[:, None, None]**2), (Hy + Hym - 2*H0)/(2*d[:, None, None]**2), (Hz + Hzm - 2*H0)/(2*d[:, None, None]**2)]
    trb = lambda A: np.real(np.einsum('ab,...ba->...', beta, A))/4
    Tb = [trb(Tj) for Tj in T]
    Hxy = Hd(P3(x[:, None], x[None, :], 0*x[:, None]))
    tot = 0.0
    for iz in range(N):
        zz = x[iz]
        Hq = Hd(P3(x[:, None], x[None, :], zz + 0*x[:, None]))
        Hxz = Hd(P3(x, z, zz + z))[:, None]; Hyz = Hd(P3(z, x, zz + z))[None, :]
        Hz1 = Hd(np.array([0, 0, zz]))
        Cx = Hx[:, None]; Cy = Hy[None, :]; Cxy = Hxy
        dX = d[:, None, None, None]; dY = d[None, :, None, None]; dZ = d[iz]
        Vx = (2*(Cx - H0) + (Cxy - Cy) + (Hxz - Hz1) + 2*(Hq - Hyz))/6/dX
        Vy = (2*(Cy - H0) + (Cxy - Cx) + (Hyz - Hz1) + 2*(Hq - Hxz))/6/dY
        Vz = (2*(Hz1 - H0) + (Hxz - Cx) + (Hyz - Cy) + 2*(Hq - Cxy))/6/dZ
        Om = np.sqrt(d[:, None]**2 + d[None, :]**2 + d[iz]**2)
        E, U = np.linalg.eigh(Hq)
        X = U @ ((np.sign(E)/(2*Om[..., None]*(np.abs(E) + Om[..., None])))[..., None]*U.conj().swapaxes(-1, -2))
        val = trb(X) - sum(trb(V @ X @ V) for V in (Vx, Vy, Vz))
        tad = (Tb[0][:, None] + Tb[1][None, :] + Tb[2][iz])/(2*Om)
        tot += float((val + tad).sum())*w**3
    return tot

N = int(sys.argv[1]) if len(sys.argv) > 1 else 16
xf = -np.pi + (np.arange(N) + 0.5)*2*np.pi/N; wf = np.full(N, 1.0/N)
dfx = G.d(xf)
print('\n(2) matrix formula vs reduced dm_gen on the same full-BZ midpoint grid N = %d:' % N)
for nm, e in (('undressed', 0.0), ('G1', 0.05), ('G2', 0.05)):
    Gk = None if nm == 'undressed' else GEN[[k for k in GEN if k.startswith(nm)][0]]
    a = dm_mat(Gk, e, N)
    b = dm_gen(make_cM(F, 0.0, None if nm == 'undressed' else nm, eps=e), dfx, dfx, dfx, xf, wf)
    print('   %-10s eps=%.2f: matrix %+.14e  reduced %+.14e  diff %.1e' % (nm, e, a, b, a - b), flush=True)

print('\n(3)/(4) linear response L = d dm/d eps at eps = 0 (central, eps = +-1e-3), full-BZ midpoint N = %d (matrix code):' % N)
print('   %-52s %-7s %-6s %-9s %s' % ('generator', 'cubic', 'P T C', '|[G,b]|', 'L'))
base = dm_mat(None, 0.0, N)
for nm, Gk in GEN.items():
    cub, par, cb = parities(Gk)
    L = (dm_mat(Gk, 1e-3, N) - dm_mat(Gk, -1e-3, N))/2e-3
    print('   %-52s %.0e   %s %s %s  %.1e   %+.6e' % (nm, cub, par['P'], par['T'], par['C'], cb, L), flush=True)
print('   (undressed dm on this grid: %+.10f)' % base)
print('time %.0f s' % (time.time() - t0))
