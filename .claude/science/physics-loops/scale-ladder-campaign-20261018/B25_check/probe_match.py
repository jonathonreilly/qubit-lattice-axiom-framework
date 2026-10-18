"""probe: does the chk_core-gauge build reproduce B25-model spectra, and under which momentum map k_core = eps k_model + c?"""
import sys, os, itertools, numpy as np
import corelib as cl
sys.path.insert(0, os.path.join(cl.HERE, '..', 'B25_spectral_tastes'))
import b25lib as B
B.ALL.update(B.PLANE6)
print("Hon levels", cl.HLEV, "Lam levels", cl.LLEV)
rng = np.random.default_rng(3)
words = [(('S', 'o'), ('L313',)), (('S', 'R', 'o'), ('H03',)), (('S2', 'p', 'S2', 'o'), ('P5', 'L031')), (('S4', 'p', 'S4', 'o', 'S4', 'q', 'S4', 'o'), ('P1', 'L130', 'P11', 'L130')),
         (('S', 'o', 'S', 'R', 'o'), ('H00', 'H12')), (('S', 'o'), ('L5.6.3',)), (('S', 'R', 'o'), ('H4.5',))]
def spec(W): return np.sort(np.mod(np.angle(np.linalg.eigvals(W)), 2*np.pi))
def same(a, b):
    za, zb = np.exp(1j*a), np.exp(1j*b); D = np.abs(za[:, None]-zb[None]); return D.min(1).max() < 1e-7 and D.min(0).max() < 1e-7
shifts = [np.array(c)*np.pi for c in itertools.product((0, 1), repeat=3)]
for sk, nm in words:
    wm = B.build24(sk, nm); wc = cl.build(sk, nm)
    ks = rng.uniform(-np.pi, np.pi, (3, 3)); found = []
    for eps in (1, -1):
        for c in shifts:
            for gph in (1, -1):
                if all(same(spec(gph*cl.Wc(wc, (eps*k + c)[None])[0]), spec(B.Wb(wm, k[None])[0])) for k in ks): found.append((eps, tuple(c/np.pi), gph))
    print(sk, nm, found)
