"""R2-5 check 6: is the route-P2 hard label rule reflection positive across a bond-centred plane?
Cross-plane factor C(a, b), a = s(x, 0), b = s(x, 1), theta maps U <-> D (B, R, L fixed for a time
reflection).  Single-column RP needs M(a', b) = C(theta a', b) positive semidefinite (product over
columns of PSD kernels is PSD; on-site weights w factor as F * theta F).  Also check the same for
the soft scalar toy (W(s,s') = eps^[s != s']).  And the row-level check for 1+1 with L = 2.
"""
import numpy as np, itertools
B, U, D, R, LF = 0, 1, 2, 3, 4
th = {B: B, U: D, D: U, R: R, LF: LF}
def C(a, b):
    if a == U and b != U: return 0.0
    if b == D and a != D: return 0.0
    return 1.0
M = np.array([[C(th[ap], b) for b in range(5)] for ap in range(5)])
print("P2 cross-plane kernel M(a',b) =\n", M)
print("symmetric:", np.allclose(M, M.T), " eigenvalues:", np.round(np.linalg.eigvalsh(M), 6))
for eps in (0.3, 0.9, 1.0):
    W = np.array([[1, eps], [eps, 1]])
    print(f"scalar toy eps={eps}: eigenvalues {np.linalg.eigvalsh(W)}")
