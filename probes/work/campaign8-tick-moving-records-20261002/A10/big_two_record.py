"""NOT RUN (too big for the 60 s / 300 MB budget): two-record sector of the plain six-layer cycle on an
8x8x8 torus (dimension C(512,2) = 130816).  Measures (a) how far the C4-rotated cycle's record odds drift
from the original over n cycles, versus theta; (b) two-record bound states (Floquet eigenphases split off
the two-record continuum), via sparse Arnoldi on U.  Expected cost: basis build ~ minutes in pure Python,
memory ~ 150 MB.  Run with nice -n 10 and single-thread BLAS."""
import numpy as np, itertools, scipy.sparse as sp, scipy.sparse.linalg as sla
L, th = 8, 0.6
coords = [(x, y, z) for z in range(L) for y in range(L) for x in range(L)]
sid = lambda x, y, z: (x % L) + L * (y % L) + L * L * (z % L)
basis = list(itertools.combinations(range(L ** 3), 2)); index = {b: i for i, b in enumerate(basis)}
def layer(axis, par):
    partner = {}
    for (x, y, z) in coords:
        s = [x, y, z]
        if s[axis] % 2 == par:
            t = list(s); t[axis] += 1; a, b = sid(*s), sid(*t); partner[a] = b; partner[b] = a
    c, s_ = np.cos(th), np.sin(th); R, C, V = [], [], []
    for j, conf in enumerate(basis):
        occ = set(conf); opts = []
        for p in conf:
            q = partner[p]
            opts.append([(p, 1.0)] if q in occ else [(p, np.exp(1j*th)*c), (q, np.exp(1j*th)*(-1j)*s_)])
        for ch in itertools.product(*opts):
            new = tuple(sorted(x for x, _ in ch))
            if len(set(new)) == 2:
                R.append(index[new]); C.append(j); V.append(np.prod([a for _, a in ch]))
    return sp.csr_matrix((V, (R, C)), shape=(len(basis),) * 2)
Lm = [layer(a, p) for a in range(3) for p in (0, 1)]
U = sla.LinearOperator(Lm[0].shape, matvec=lambda v: Lm[5] @ (Lm[4] @ (Lm[3] @ (Lm[2] @ (Lm[1] @ (Lm[0] @ v))))), dtype=complex)
# (b) eigenphases nearest to the two-record band edges: shift-invert is unavailable for a LinearOperator;
# use eigs on U with which='LM' and sigma=None on a symmetrized projector, or time-series + FFT of <v|U^n|v>
v = np.zeros(len(basis), complex); v[index[(sid(0, 0, 0), sid(1, 0, 0))]] = 1   # adjacent pair on an x-even bond
amp = []
w = v.copy()
for n in range(400):
    w = U @ w; amp.append(np.vdot(v, w))
spec = np.abs(np.fft.fft(np.array(amp))) ** 2      # sharp peaks outside the continuum = bound pairs
np.save("two_record_return_spectrum.npy", spec)
