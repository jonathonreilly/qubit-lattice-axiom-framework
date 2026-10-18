"""R1: P generations (L), internal R, one E (strain) spurion at angle theta from a tetragonal line.
Check: the third-generation direction appears at order eps^2 with weight |sin 3 theta|."""
import sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import native_menu as nm
G = nm.group_for(['E'])
for th in [0.0, 0.05, 0.1, 0.2, 0.37, np.pi / 6]:
    n = np.array([np.sin(th), np.cos(th)])
    B0 = nm.equivariant_images('E', 'P', None, n, 0, G); B1 = nm.equivariant_images('E', 'P', None, n, 1, G)
    B2 = nm.equivariant_images('E', 'P', None, n, 2, G)
    span01 = np.vstack([B0, B1])
    # component of the degree-2 image orthogonal to span(F_1)
    Q, _ = np.linalg.qr(span01.T)
    perp = max(np.linalg.norm(b - Q @ (Q.T @ b)) for b in B2) if len(B2) else 0.0
    print(f'theta={th:.3f}  dim F0,F1={len(B0)},{np.linalg.matrix_rank(span01)}  new-direction weight at order 2 = {perp:.4f}'
          f'   |sin 3theta| = {abs(np.sin(3*th)):.4f}  ratio = {perp/max(abs(np.sin(3*th)),1e-12):.4f}')
