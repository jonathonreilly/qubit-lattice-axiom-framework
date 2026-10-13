"""R19-23 (c): are Goldstone (Stueckelberg) kinetic terms forced by the five Ward-violating rows?
Goldstone quadratic form G(p; xi) = (p xi + xi p).Pi(p).(p xi + xi p) = 4 xi_nu xi_sigma p_mu p_rho Pi^{mu nu rho sigma}(p).
Degree 2 part: 4 xi xi p p B p p, i.e. B symmetrized over (mu, rho, a, b) for each (nu, sigma).
Find the B-subspace with G == 0 identically (Goldstones without any quadratic term) and the subspace where G has no
omega-dependence (Goldstones auxiliary), and their images in the six rows."""
import numpy as np, sys, itertools
sys.path.insert(0, '.')
from kernels import *
def gold4(B):
    C = B.transpose(1, 3, 0, 2, 4, 5)          # (nu, sigma, mu, rho, a, b)
    out = np.zeros_like(C)
    perms = list(itertools.permutations(range(4)))
    for pm in perms:
        out += C.transpose((0, 1) + tuple(2+k for k in pm))
    out /= len(perms)
    out = (out + out.transpose(1, 0, 2, 3, 4, 5))/2
    return out
def gold_time(B):
    """omega-dependent part: components of the symmetrized tensor with at least one of (mu,rho,a,b) = 0"""
    G4 = gold4(B); mask = np.zeros(G4.shape, bool)
    for idx in itertools.product(range(4), repeat=6):
        if 0 in idx[2:]: mask[idx] = True
    return G4[mask]
rowsB = np.array([rows(0*Ab[0], B)[:4] for B in Bb]).T     # 4 x 26 (speed rows only)
for label, fn in [('G == 0 identically', lambda B: gold4(B).ravel()), ('G omega-independent (auxiliary Goldstones)', gold_time)]:
    Mc = np.array([fn(B) for B in Bb]).T
    N = nullspace(Mc)
    img = rowsB @ N
    rk = np.linalg.matrix_rank(img, tol=1e-9) if img.size else 0
    print('[%s] dim = %d of 26; rank of image in (Xi_Eg, Xi_T2g, face1, face2) = %d' % (label, N.shape[1], rk))
    if rk:
        u, s, vt = np.linalg.svd(img); print('   image basis:\n', np.round(u[:, :rk].T, 4))
# the FULL-Ward family for reference
img = rowsB @ NB_full; print('[FULL Ward] dim %d, image rank %d' % (NB_full.shape[1], np.linalg.matrix_rank(img, tol=1e-9)))
img = rowsB @ NB_sp; print('[SPATIAL Ward] dim %d, image rank %d' % (NB_sp.shape[1], np.linalg.matrix_rank(img, tol=1e-9)))
# degree 0: Goldstone form from A: 4 xi xi p p A -> components A^{mu nu rho sigma} symmetrized over (mu, rho)
def gold_A(A):
    C = A.transpose(1, 3, 0, 2); C = (C + C.transpose(0, 1, 3, 2))/2; C = (C + C.transpose(1, 0, 2, 3))/2
    return C
for nm, A in [('solid (trh)^2', None)]: pass

# mode count for kernels whose Goldstone form is omega-independent (17-dim) or identically zero (9-dim), plus the solid
src = open('r1923_modes.py').read()
exec(src.split("# ---- Part 1")[0].replace('from kernels import *', ''))
rngg = np.random.default_rng(5)
Maux = np.array([gold_time(B) for B in Bb]).T; N_aux = nullspace(Maux)
M0 = np.array([gold4(B).ravel() for B in Bb]).T; N_0 = nullspace(M0)
for nm, NS in [('aux (17-dim)', N_aux), ('G==0 (9-dim)', N_0)]:
    for t in range(3):
        B = combB(NS @ rngg.normal(size=NS.shape[1]))
        classify(solid(0.7, 1.0, 0.6), B, fd3, 'Goldstone-%s sample %d + solid' % (nm, t), eps_list=(1e-4, 1e-6), q_list=(1e-2, 1e-3))
        classify(solid(0.7, 1.0, 0.6), B, z3, 'Goldstone-%s sample %d + solid, q along z' % (nm, t), eps_list=(1e-6,), q_list=(1e-2,))
