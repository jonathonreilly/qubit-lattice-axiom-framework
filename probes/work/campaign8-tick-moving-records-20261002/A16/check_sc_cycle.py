"""A16 hostile check: is A10's plain 6-layer cycle 'schedule covariant' (image = cyclic restart of the SAME cycle)
under site-centred lattice symmetries, in the ONE-record sector?  L=6 torus, 216 sites (L=4 is degenerate: shift by 2 = shift by -2), one excitation.
Layer L_{a,p}: block M = cos t I - i sin t sigma_x on every pair (s, s+e_a) with s_a = p mod 2 (global phase dropped)."""
import numpy as np, itertools
L = 6; th = 0.6
sites = list(itertools.product(range(L), repeat=3)); idx = {s: i for i, s in enumerate(sites)}; N = len(sites)
def layer(a, p):
    U = np.zeros((N, N), complex)
    for s in sites:
        if s[a] % 2 != p: continue
        t = list(s); t[a] = (t[a] + 1) % L; t = tuple(t)
        i, j = idx[s], idx[t]
        U[i, i] = U[j, j] = np.cos(th); U[i, j] = U[j, i] = -1j * np.sin(th)
    return U
word = [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]          # xe, xo, ye, yo, ze, zo (xe acts first)
Ls = [layer(a, p) for a, p in word]
def cyc(seq):
    U = np.eye(N, dtype=complex)
    for M in seq: U = M @ U
    return U
U = cyc(Ls)
restarts = [cyc(Ls[k:] + Ls[:k]) for k in range(6)]
def perm(f):
    P = np.zeros((N, N));
    for s in sites: P[idx[tuple(c % L for c in f(s))], idx[s]] = 1
    return P
def eq_phase(A, B):
    k = np.unravel_index(np.argmax(abs(B)), B.shape); ph = A[k] / B[k]
    return np.max(abs(A - ph * B)) if abs(abs(ph) - 1) < 1e-9 else 9.0
syms = {
 "cube-centred C2z (1-x,1-y,z)": lambda s: (1 - s[0], 1 - s[1], s[2]),
 "cube-centred C4z (1-y,x,z)":   lambda s: (1 - s[1], s[0], s[2]),
 "unit translation T_x":         lambda s: (s[0] + 1, s[1], s[2]),
 "unit translation T_y":         lambda s: (s[0], s[1] + 1, s[2]),
 "translation T_x T_y":          lambda s: (s[0] + 1, s[1] + 1, s[2]),
 "site-centred C2z (-x,-y,z)":   lambda s: (-s[0], -s[1], s[2]),
 "site-centred C4z (-y,x,z)":    lambda s: (-s[1], s[0], s[2]),
}
for name, f in syms.items():
    P = perm(f); img = P @ U @ P.T
    res = [eq_phase(img, R) for R in restarts]
    best = int(np.argmin(res))
    # film check: does the symmetry map the layer SEQUENCE to a cyclic shift of itself?
    imgL = [P @ M @ P.T for M in Ls]
    film = [max(eq_phase(imgL[j], Ls[(j + sh) % 6]) for j in range(6)) for sh in range(6)]
    print(f"{name:32s} min_k |img - restart_k| = {min(res):.1e} (k={best});  film-shift residual min = {min(film):.1e}")

# Extension: allow the REVERSED round as well (A10 S16 'odd rotations may reverse the schedule').
rev = Ls[::-1]
rev_restarts = [cyc(rev[k:] + rev[:k]) for k in range(6)]
more = dict(syms)
more.update({"translation T_x T_y T_z": lambda s: (s[0] + 1, s[1] + 1, s[2] + 1),
             "translation (1,1,0) only": lambda s: (s[0] + 1, s[1] + 1, s[2])})
for name, f in more.items():
    P = perm(f); img = P @ U @ P.T
    fwdres = min(eq_phase(img, Rm) for Rm in restarts)
    revres = min(eq_phase(img, Rm) for Rm in rev_restarts)
    print(f"{name:32s} forward-restart residual {fwdres:.1e};  reversed-restart residual {revres:.1e}")
