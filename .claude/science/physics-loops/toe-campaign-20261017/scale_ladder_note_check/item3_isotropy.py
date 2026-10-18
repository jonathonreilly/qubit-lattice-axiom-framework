"""Item 3: cone-speed anisotropy vs |q| with an own direction set, own X seeds, several parameter points."""
import itertools, time
import numpy as np
from common import *

t0 = time.time()
def H0(t1, t2):
    H = np.zeros((nV, nV))
    for key in EDGES:
        i, j = tuple(key); t = t1 if C['edges'][key] == 'onsite' else t2
        H[i, j] = H[j, i] = -t * (-1.0) ** u[EID[key]]
    return H
def symm(Hm):
    Y = sum(conj_mat(Hm, TR[t]) for t in TV) / 64
    Y = sum(conj_mat(Y, A) for A in ROT) / 24
    return (Y + conj_mat(Y, INV)) / 2
def makeX(seed):
    rng = np.random.default_rng(seed); A = np.zeros((nV, nV))
    for i in loc0:
        for j in range(nV):
            dd = [abs(dmod(y - x)) for x, y in zip(VERTS[i][0], VERTS[j][0])]
            if i != j and sum(dd) <= 1: A[i, j] = rng.normal()
    X = symm(1j * (A - A.T)); return X / np.abs(X).max()
def blocks(Hm):
    bl = {}
    for a in loc0:
        for b in range(nV):
            if abs(Hm[a, b]) > 1e-12:
                sh = tuple(dmod(x) for x in VERTS[b][0])
                bl.setdefault(sh, np.zeros((12, 12), complex))[CI[VERTS[a][1]], CI[VERTS[b][1]]] += Hm[a, b]
    return bl
def Hk(bl, k): return sum(M * np.exp(1j * np.dot(k, sh)) for sh, M in bl.items())
def fib(n):
    i = np.arange(n) + 0.5; th = np.arccos(1 - 2 * i / n); ph = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], 1)
DIRS_ = np.vstack([fib(400), np.eye(3), np.array(list(itertools.product((1, -1), repeat=3))) / 3 ** 0.5,
                   np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]]) / 2 ** 0.5])
if __name__ != '__main__':
    pass
else:
  Bk = Bloch(kst)
  Xs = {s: makeX(s) for s in (5, 99)}
  print(f"X built {time.time()-t0:.1f}s; X real?", np.allclose(Xs[5].imag, 0), " imaginary-Hermitian:", np.allclose(Xs[5].real, 0))
  for (t1, t2, dl, seed) in [(-1, 0.2, 0.05, 5), (-1, 0.2, 0.05, 99), (-1, 0.4, 0.05, 5), (-1, 0.2, 0.2, 5), (-1, 0.1, 0.02, 99), (-1, 0.5, 0.3, 99)]:
      Hm = H0(t1, t2) + dl * Xs[seed]; bl = blocks(Hm)
      assert np.allclose(Hk(bl, kst), Bk.conj().T @ Hm @ Bk)
      ev = np.linalg.eigvalsh(Hk(bl, kst))
      # doublet levels at k*
      dbl = [i for i in range(11) if abs(ev[i + 1] - ev[i]) < 1e-9 and (i == 0 or abs(ev[i] - ev[i - 1]) > 1e-9) and (i + 2 > 11 or abs(ev[i + 2] - ev[i]) > 1e-9)]
      print(f"\nparams t1={t1} t2={t2} X={dl} seed={seed}: k* levels {np.round(ev, 4)}")
      for i in dbl[:2]:
          EN = ev[i]; row = []
          for dq in (0.08, 0.04, 0.02, 0.01, 0.005):
              sp = []
              for d in DIRS_:
                  e = np.linalg.eigvalsh(Hk(bl, kst + dq * d)); j = np.argsort(np.abs(e - EN))[:2]; a, b = sorted(e[j])
                  sp.append((b - a) / (2 * dq))
              sp = np.array(sp); row.append((dq, sp.mean(), np.ptp(sp) / sp.mean(), sp[-6] / sp[400]))
          an = [r[2] for r in row]
          print(f"  doublet at E={EN:.5f} (index {i}): v={row[-1][1]:.6f}")
          print("    dq      aniso       ratio-to-next   v[110]/v[100]-1")
          for n, r in enumerate(row):
              print(f"    {r[0]:<7} {r[2]:.4e}  {an[n]/an[n+1] if n+1 < len(an) else float('nan'):8.4f}   {r[3]-1:+.3e}")
  print(f"\ntime {time.time()-t0:.1f}s")
