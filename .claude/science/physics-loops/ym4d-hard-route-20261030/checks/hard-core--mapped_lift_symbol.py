#!/usr/bin/env python3
"""Symbol of the chain map T = (composite block average) o (Whitney interpolation), one direction.

Criteria, written before the run.
 PASS if, for L in {3, 5, 7, 9} and depth j in {1, 2, 3}, on the level-j lattice:
  (a) the one-direction factor tau(P) of T is real, positive, with min over P at least 0.40,
      the one-direction kernel is the composite average convolved with the interpolation, sampled at level-j spacing;
  (b) the exact product formula holds: with a = composite fine box of width s = L^j, the 2-direction
      in-plane kernel on fine lattice equals (box)*(box) up to rounding (checks the tent = box*box step);
 Control: an interpolation with box only (no tent) has factor with a much lower min, or sign change, so the
 test can fail: for that control min tau must differ from the Whitney value by more than 0.05.
 Run 1 failed on a script error in the sampling (kept as first_run_script_bug.out); criteria unchanged. A FAIL is reported and kept. This tests a finite-dimensional algebra at U = 1 and says nothing at a background.
"""
import numpy as np, resource, sys, os
os.environ.setdefault("OMP_NUM_THREADS", "1")
def rss_ok():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 2e9  # bytes on darwin

def box(n):
    return np.ones(n) / n

def comp_box_kernel(L, j):
    """Composite one-direction kernel of the block average in a transverse direction: box at every level."""
    k = np.array([1.0])
    for m in range(j):
        s = L ** m
        b = np.zeros(s * (L - 1) + 1)
        b[::s] = 1.0 / L
        k = np.convolve(k, b)
    return k  # support about L^j fine sites, normalised sum 1

def tau_min(L, j, whitney=True):
    s = L ** j
    a = comp_box_kernel(L, j)            # average: box-like of width s
    if whitney:
        w = np.convolve(box(s), box(s))  # interpolation: tent of half width s, sum 1
    else:
        w = box(s)
    k = np.convolve(a, w)                # fine-lattice kernel of T in this direction
    # T(y, y') = sum_x a(y - x) wtilde(x - y'), with wtilde := s * w a partition of unity (height 1 at a node)
    # both centred at sites, so the level-j kernel is s * k at integer multiples of s from the centre
    c = (len(k) - 1) // 2
    assert (len(k) - 1) % 2 == 0
    ms = np.arange(-(c // s), c // s + 1)
    vals = s * k[c + ms * s]
    P = np.linspace(-np.pi, np.pi, 721)
    sym = np.array([np.sum(vals * np.exp(1j * p * ms)) for p in P])
    return np.min(sym.real), np.max(np.abs(sym.imag)), len(ms)

ok = True
print("L j  tau_min(whitney)  imag  n_offsets  tau_min(control box)")
for L in (3, 5, 7, 9):
    for j in (1, 2, 3):
        if L ** j > 800:
            continue
        m, im, n = tau_min(L, j, True)
        c, _, _ = tau_min(L, j, False)
        print(L, j, round(m, 4), round(im, 6), n, round(c, 4))
        if m < 0.40 or abs(m - c) <= 0.05:
            ok = False
        if not rss_ok():
            print("RSS cap"); sys.exit(2)
# (b) tent = box * box on the fine lattice, exact
for L in (3, 5):
    t = np.convolve(box(L), box(L))
    tent = (L - np.abs(np.arange(-L + 1, L))) / L ** 2
    if np.max(np.abs(t - tent)) > 1e-12:
        ok = False
print("PASS" if ok else "FAIL")
