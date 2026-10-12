"""C5 R10-5, script 3: Lemma PD (photon/photino doubling for a lattice gauge superpotential), numerical illustration.

In the SUSY-QM class the photon energy is 1/2 |dW/dA|^2 = 1/2 A.C^2.A and the photino one-particle operator is
C = Hess_AA W (Hermitian 3x3 symbol on T^3), gauge invariance C(q) Dhat(q) = 0.  Near q=0 the only C^1 Hermitian
linear symbol with C1(q) q = 0 and C1^2 = q^2 P_T is C1 = +-i eps.q (proved in the report).  Its upper transverse
band has Chern number +-2 on any small sphere around 0 (photon helicity monopole).  On T^3 minus a ball that sphere
is a boundary, so a smooth upper band defined on all of T^3\{0} would have Chern number 0: contradiction.  Hence the
transverse eigenvalues must hit 0 at some q != 0 (a photon zero mode = photon/photino doubler).

Here: (a) Chern number (Fukui-Hatsugai-Suzuki lattice field strength on a theta-phi grid) of the upper band of
i eps.q on a sphere; (b) for the natural lattice symbol C = i eps.s(q), s_j = sin q_j (gauge symbol i s(q), real):
the Chern numbers around each of the 8 zeros of s, which sum to 0 (Nielsen-Ninomiya-type bookkeeping);
(c) a generic smooth Hermitian deformation C' = C + eps*R(q) (random smooth periodic Hermitian, projected to keep
C' s = 0): scan of min over q != 0 of the smallest |transverse eigenvalue| (zeros persist).
"""
import numpy as np, time
t0 = time.time()
def curl(n):
    # (i eps.n) v = i n x v  as a 3x3 matrix
    nx, ny, nz = n
    return 1j * np.array([[0, -nz, ny], [nz, 0, -nx], [-ny, nx, 0]])

def upper_vec(Cq):
    w, U = np.linalg.eigh(Cq)
    return U[:, -1], w

def chern_sphere(Cfun, center, rad, nth=60, nph=120):
    th = np.linspace(1e-3, np.pi - 1e-3, nth); ph = np.linspace(0, 2 * np.pi, nph, endpoint=False)
    V = np.empty((nth, nph, 3), complex)
    for i, t in enumerate(th):
        for j, p in enumerate(ph):
            q = np.array(center) + rad * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])
            V[i, j] = upper_vec(Cfun(q))[0]
    F = 0.0
    for i in range(nth - 1):
        for j in range(nph):
            a, b, c, d = V[i, j], V[i + 1, j], V[i + 1, (j + 1) % nph], V[i, (j + 1) % nph]
            u = np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, d) * np.vdot(d, a)
            F += np.angle(u)
    # polar caps: add the small loops around the poles
    for i in (0, nth - 1):
        loop = np.prod([np.vdot(V[i, j], V[i, (j + 1) % nph]) for j in range(nph)])
        F += np.angle(loop) * (1 if i == 0 else -1)
    return F / (2 * np.pi)

print('(a) upper band of i eps.q, sphere radius 0.1 around 0: Chern = %+.4f' % chern_sphere(lambda q: curl(q), (0, 0, 0), 0.1))
print('    lower band check (-i eps.q): Chern = %+.4f' % chern_sphere(lambda q: curl(-q), (0, 0, 0), 0.1))
Clat = lambda q: curl(np.sin(q))
tot = 0.0
print('(b) lattice symbol C = i eps.sin(q): Chern of upper band around each zero of sin(q):')
for c in [(a, b, d) for a in (0, np.pi) for b in (0, np.pi) for d in (0, np.pi)]:
    ch = chern_sphere(Clat, c, 0.15)
    tot += ch
    print('    q0 = (%s) : %+.3f' % (', '.join('pi' if x else '0' for x in c), ch))
print('    sum = %+.3f' % tot)
# (c) generic smooth Hermitian deformation keeping the kernel s(q)
rng = np.random.default_rng(3)
H = [rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)) for _ in range(6)]
H = [(h + h.conj().T) / 2 for h in H]
def Cdef(q, e):
    s = np.sin(q)
    R = H[0] * np.cos(q[0]) + H[1] * np.cos(q[1]) + H[2] * np.cos(q[2]) + H[3] * np.sin(q[0] + q[1]) + H[4] * np.cos(q[1] - q[2]) + H[5]
    R = R * (np.dot(s, s))                     # vanish to 2nd order at the zeros: keeps the linear terms there
    n2 = np.dot(s, s)
    P = np.eye(3) - (np.outer(s, s) / n2 if n2 > 1e-14 else 0)
    return Clat(q) + e * P @ R @ P
for e in (0.3, 1.0):
    N = 40
    g = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    mins = []
    best = (9, None)
    for a in g:
        for b in g:
            for c in g:
                q = np.array([a, b, c])
                if np.linalg.norm(q) < 0.3: continue
                w = np.linalg.eigvalsh(Cdef(q, e))
                w = w[np.argsort(np.abs(w))][1:]          # drop the gauge zero (kernel s)
                if np.min(np.abs(w)) < best[0]: best = (np.min(np.abs(w)), q)
    print('(c) eps=%.1f: min over the N=40 grid (|q|>0.3) of smallest transverse |eigenvalue| = %.3e at q = %s' % (e, best[0], np.round(best[1], 3)))
    print('    Chern of upper band around 0 (r=0.1): %+.3f' % chern_sphere(lambda q: Cdef(q, e), (0, 0, 0), 0.1))
print('elapsed %.1fs' % (time.time() - t0))
