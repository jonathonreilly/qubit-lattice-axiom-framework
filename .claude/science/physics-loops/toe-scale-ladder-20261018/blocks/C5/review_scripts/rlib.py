"""Reviewer's own helpers (independent of the worker's w3lib)."""
import itertools, numpy as np
S = [np.eye(2, dtype=complex), np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]],complex), np.diag([1,-1]).astype(complex)]
EPS = [(p, (1 if (p[0],p[1],p[2]) in [(0,1,2),(1,2,0),(2,0,1)] else -1)) for p in itertools.permutations(range(3))]
class Ck:
    def __init__(s): s.p=s.f=0
    def __call__(s, name, ok):
        ok=bool(ok); s.p+=ok; s.f+=(not ok); print(('PASS' if ok else 'FAIL')+': '+name, flush=True)
    def total(s): print(f'TOTAL: PASS={s.p} FAIL={s.f}'); return int(s.f>0)
def w3_GL(U, dU):
    """(1/24pi^2) int sum_eps tr(A_a A_b A_c), A = U^{-1} dU, from grid mean (uniform grid on [0,2pi)^3).
    Full epsilon sum, general inverse (no unitarity assumed)."""
    Ui = np.linalg.inv(U)
    A = [Ui @ d for d in dU]
    t = 0
    for (a,b,c), s in EPS:
        t = t + s*np.trace(A[a] @ A[b] @ A[c], axis1=-2, axis2=-1)
    return (2*np.pi)**3 * t.mean() / (24*np.pi**2)
def grid(N, off):
    k = 2*np.pi*(np.arange(N)+off)/N
    return np.meshgrid(k,k,k, indexing='ij')
