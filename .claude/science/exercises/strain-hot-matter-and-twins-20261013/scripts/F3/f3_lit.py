"""F3 literal branch D-L (D -> V D V^dag on F1's Euclidean spatial D = i g.c + M):
 (1) for V not commuting with g0 (e.g. the D-H-symmetric G1), V D V^dag changes the band energies (eigenvalues of H' = g0 V D V^dag),
     so the spectrum-preserving literal class is the g0-commutant, where D-L = D-H;
 (2) the nontrivial cubic-covariant g0-commuting generators on the S19 stencil (f3_sym.out: 7 = 3 + 2 + 2, all P-, T- or C-odd) are
     spanned by 7 named representatives; a random element of their span has zero linear response (matrix code, full-BZ grid)."""
import numpy as np, sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from f3_dirac import *
from f3_lib import *
import f3_mat as FM          # reuses dm_mat, Hfun, GEN (runs its own checks at import: output goes to this .out too)

rng = np.random.default_rng(11)
K = rng.uniform(-np.pi, np.pi, (300, 3))
F = FM.F
H = FM.Hfun(K); D = g0 @ H
print('\n[f3_lit] (1) literal V D V^dag with V = exp(i eps G1), eps = 1e-2: band energies |eig(g0 D\') - eig(H)| (300 random k)')
lam, U = np.linalg.eigh(FM.GEN['G1 = sum i beta alpha_j sin k_j'](K))
V = U @ (np.exp(1j*1e-2*lam)[..., None]*U.conj().swapaxes(-1, -2))
Dl = V @ D @ V.conj().swapaxes(-1, -2)
ev = np.sort(np.linalg.eigvals(g0 @ Dl).real, -1); ev0 = np.linalg.eigvalsh(H)
print('   max change %.2e ; median %.2e ; max |Im eig| %.1e   (D-H dressing of the same G1: 3.6e-15, f3_mat (1))'
      % (np.abs(ev - ev0).max(), np.median(np.abs(ev - ev0).max(-1)), np.abs(np.linalg.eigvals(g0 @ Dl).imag).max()))

ones = lambda k: np.ones(k.shape[:-1])
cc = lambda k: np.cos(k[..., 0]) + np.cos(k[..., 1]) + np.cos(k[..., 2])
ccc = lambda k: np.cos(k[..., 0])*np.cos(k[..., 1]) + np.cos(k[..., 1])*np.cos(k[..., 2]) + np.cos(k[..., 2])*np.cos(k[..., 0])
sx = lambda j: (lambda k: np.sin(k[..., j]))
s2j = lambda j: (lambda k: np.sin(k[..., j])*(np.cos(k[..., (j+1) % 3]) + np.cos(k[..., (j+2) % 3])))
REP = {'beta': [(beta, ones)], 'beta sum cos': [(beta, cc)], 'beta sum cos cos': [(beta, ccc)],
       'beta Sigma.sin': [(beta @ Sigma[j], sx(j)) for j in range(3)], 'beta Sigma.sin(c+c)': [(beta @ Sigma[j], s2j(j)) for j in range(3)],
       'Sigma.sin': [(Sigma[j], sx(j)) for j in range(3)], 'Sigma.sin(c+c)': [(Sigma[j], s2j(j)) for j in range(3)],
       'trivial 1 x sum cos': [(I4, cc)]}
def gfun(terms, coef=1.0):
    def Gk(k):
        return sum(coef*np.multiply.outer(fn(k), Mt) for Mt, fn in terms)
    return Gk
Ks = rng.uniform(-np.pi, np.pi, (40, 3)); Hs = FM.Hfun(Ks)
vec = lambda A: np.concatenate([A.real.ravel(), A.imag.ravel()])
imgs = []
for nm, terms in REP.items():
    Gk = gfun(terms); cub, par, cb = FM.parities(Gk)
    imgs.append(vec(Gk(Ks) @ Hs - Hs @ Gk(Ks)))
    print('   rep %-22s cubic %.0e  P%s T%s C%s  |[G,beta]| %.0e' % (nm, cub, par['P'], par['T'], par['C'], cb))
print('   rank of commutator images of the 7 nontrivial reps: %d (f3_sym S19 literal-branch nontrivial total: 3 + 2 + 2 = 7)'
      % np.linalg.matrix_rank(np.stack(imgs[:7], 1), 1e-8))
coef = rng.normal(size=len(REP))
def Grand(k):
    return sum(c*gfun(terms)(k) for c, terms in zip(coef, REP.values()))
for N in (16, 24):
    L = (FM.dm_mat(Grand, 1e-3, N) - FM.dm_mat(Grand, -1e-3, N))/2e-3
    Lfin = (FM.dm_mat(Grand, 0.2, N) - FM.dm_mat(None, 0.0, N))
    print('   (2) random element of the literal-branch span, N = %d: L = %+.2e ; finite eps = 0.2 shift dm(0.2) - dm(0) = %+.2e (O(eps^2) allowed)' % (N, L, Lfin), flush=True)
