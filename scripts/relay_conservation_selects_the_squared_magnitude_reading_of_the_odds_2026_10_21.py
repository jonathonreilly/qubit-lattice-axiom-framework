#!/usr/bin/env python3
"""Relay conservation selects the squared-magnitude reading of the odds.

Hypotheses (supplied, named in the note): the tick is a direction shift composed with a
block-local unitary mixing C (CL-1 read as unitarity); the odds of (block, direction) are a
common continuous function f of that amplitude alone, f(0) = 0 (local additive reading);
f is blind to the amplitude's phase. CL-4 conserves relays and CL-6 switches them only
inside a block, so each block's total odds must be unchanged by C. Checks: the exact
Jensen step for two modes (n = 2 suffices; no Gleason, no dimension 3), the Lie-closure
step for a general non-monomial C (including the block-of-eight mass mixing), numerical
drift and relay-teleport fractions for |a|^p readings in a supplied 1D two-direction walk,
the normalised nonlocal p-reading, and controls (Gleason fails on a qubit; a real coin
leaves a phase-sensitive quadratic reading alive).
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/RELAY_CONSERVATION_SELECTS_THE_SQUARED_MAGNITUDE_READING_OF_THE_ODDS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import sys, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
def _timeout(*args):
    raise TimeoutError('Owning 120-second aggregate cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np, sympy as sp
from scipy.linalg import expm

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

rng = np.random.default_rng(20261021)

# ---------- 1. exact two-mode step ----------
print("1. Two-mode Jensen step (exact)")
t, th, c = sp.symbols('t theta c', positive=True)
x = sp.sqrt(t); y = sp.sqrt(t) * sp.exp(sp.I * th)
o1 = sp.simplify(sp.expand(sp.Abs((x + y) / sp.sqrt(2))**2).rewrite(sp.cos))
o2 = sp.simplify(sp.expand(sp.Abs((x - y) / sp.sqrt(2))**2).rewrite(sp.cos))
check("balanced mixing of |x|^2=|y|^2=t gives block weights t(1+cos th), t(1-cos th)",
      sp.simplify(o1 - t * (1 + sp.cos(th))) == 0 and sp.simplify(o2 - t * (1 - sp.cos(th))) == 0)
check("so G(S)+G(2t-S)=2G(t) for every S in [0,2t]: Jensen on [0,inf)",
      sp.simplify((o1 + o2) - 2 * t) == 0, "S = t(1+cos th) sweeps [0,2t]")
check("G(s)=c s solves it identically", sp.simplify(c * o1 + c * o2 - 2 * c * t) == 0)
pp = sp.Rational(3, 2); S = sp.symbols('S', positive=True)
jg = sp.simplify((S**(pp / 2) + (2 - S)**(pp / 2) - 2).subs(S, sp.Rational(1, 2)))
check("G(s)=s^(p/2), p=3/2, violates Jensen at t=1, S=1/2", jg != 0, f"residual {float(jg):.4f}")
for p in (1, 3, 4):
    r = float((S**sp.Rational(p, 2) + (2 - S)**sp.Rational(p, 2) - 2).subs(S, 0))
    check(f"p={p}: residual at S=0 (full constructive interference) nonzero", abs(r) > 0.1, f"{r:+.4f}")

# ---------- 2. Lie closure for a general non-monomial C ----------
print("2. Lie closure: diagonal phases + non-monomial C contain a two-mode rotation")
def lie_closure(gens, n, tol=1e-9, maxit=6):
    def vec(A): return np.concatenate([A.real.ravel(), A.imag.ravel()])
    basis = []
    def add(A):
        v = vec(A)
        if basis:
            M = np.array(basis); v = v - M.T @ (M @ v)
        if np.linalg.norm(v) > tol: basis.append(v / np.linalg.norm(v)); return True
        return False
    mats = []
    for g in gens:
        if add(g): mats.append(g)
    for _ in range(maxit):
        new = []
        for i in range(len(mats)):
            for j in range(i + 1, len(mats)):
                X = mats[i] @ mats[j] - mats[j] @ mats[i]
                if add(X): new.append(X)
        if not new: break
        mats += new
    return len(basis), mats
def root_pairs(mats, n, tol=1e-8):
    pairs = set()
    for A in mats:
        for j in range(n):
            for k in range(j + 1, n):
                if abs(A[j, k]) > tol: pairs.add((j, k))
    return pairs
def tick_mix(C):
    n = C.shape[0]
    T = [1j * np.diag(np.eye(n)[i]) for i in range(n)]
    return T + [C @ h @ C.conj().T for h in T]
m = 0.3
C2 = np.array([[np.cos(m), -1j * np.sin(m)], [-1j * np.sin(m), np.cos(m)]])
d2, mats2 = lie_closure(tick_mix(C2), 2)
check("2-mode mass coin: closure is all of u(2) (dim 4)", d2 == 4, f"dim {d2}")
I2 = np.eye(2); Mm = np.zeros((8, 8))
for (a_, b_) in ((0, 2), (4, 6)): Mm[a_:a_+2, b_:b_+2] = .05 * I2; Mm[b_:b_+2, a_:a_+2] = .05 * I2
for (a_, b_) in ((0, 6), (4, 2)): Mm[a_:a_+2, b_:b_+2] = .5 * I2; Mm[b_:b_+2, a_:a_+2] = .5 * I2
C8 = expm(-1j * Mm)
mono = all(np.count_nonzero(np.abs(C8[i]) > 1e-12) == 1 for i in range(8))
check("block-of-eight mass mixing is unitary and non-monomial",
      np.allclose(C8 @ C8.conj().T, np.eye(8)) and not mono)
d8, mats8 = lie_closure(tick_mix(C8), 8)
pr = root_pairs(mats8, 8)
check("its closure with diagonal phases contains two-mode root spaces", len(pr) > 0 and d8 > 8,
      f"dim {d8}, mode pairs {sorted(pr)}")
P = np.eye(8)[[1, 0, 3, 2, 5, 4, 7, 6]]
dP, _ = lie_closure(tick_mix(P), 8)
check("control: a monomial (relabelling) C adds nothing beyond the diagonal torus", dP == 8, f"dim {dP}")

# ---------- 3. supplied 1D two-direction walk ----------
print("3. Supplied 1D walk, L=32 blocks, 2 directions, coin mass m=0.3, 60 ticks")
L, T = 32, 60
def coin(psi): return psi @ C2.T          # in-block mixing (CL-6 switching happens here)
def shift(psi): return np.stack([np.roll(psi[:, 0], 1), np.roll(psi[:, 1], -1)], axis=1)  # CL-4 step
psi0 = rng.normal(size=(L, 2)) + 1j * rng.normal(size=(L, 2)); psi0 /= np.linalg.norm(psi0)
res = {}
for p in (1.0, 1.5, 2.0, 2.5, 3.0, 4.0):
    psi = psi0.copy(); W0 = np.sum(np.abs(psi)**p); drift = 0.; tele = 0.; teleN = 0.
    for _ in range(T):
        mid = coin(psi)
        w, w2 = np.abs(psi)**p / W0, np.abs(mid)**p / W0
        wn, wn2 = np.abs(psi)**p / np.sum(np.abs(psi)**p), np.abs(mid)**p / np.sum(np.abs(mid)**p)
        tele = max(tele, 0.5 * np.sum(np.abs(w2.sum(1) - w.sum(1))))
        teleN = max(teleN, 0.5 * np.sum(np.abs(wn2.sum(1) - wn.sum(1))))
        psi = shift(mid); drift = max(drift, abs(np.sum(np.abs(psi)**p) / W0 - 1))
    res[p] = (drift, tele, teleN)
    print(f"   p={p:3.1f}: total drift {drift:.2e}  teleport (additive) {tele:.2e}  teleport (normalised) {teleN:.2e}")
check("p=2: total odds conserved and no relay must change block", max(res[2.0]) < 1e-13, f"{max(res[2.0]):.1e}")
check("every p != 2 forces relays to change block (additive reading)",
      all(res[p][1] > 1e-3 for p in res if p != 2.0), f"min {min(res[p][1] for p in res if p != 2.0):.2e}")
check("every p != 2 forces relays to change block (normalised nonlocal reading)",
      all(res[p][2] > 1e-3 for p in res if p != 2.0), f"min {min(res[p][2] for p in res if p != 2.0):.2e}")
check("every p != 2 drifts the total of the additive reading", all(res[p][0] > 1e-3 for p in res if p != 2.0))

# ---------- 4. controls ----------
print("4. Controls")
fz = lambda u: (1 + u[..., 2]**3) / 2
U3 = rng.normal(size=(2000, 3)); U3 /= np.linalg.norm(U3, axis=1, keepdims=True)
check("Gleason fails on a qubit: (1+u_z^3)/2 is a non-Born frame function on all bases",
      np.allclose(fz(U3) + fz(-U3), 1) and np.max(np.abs(fz(U3) - (1 + U3[:, 2]) / 2)) > .1)
Q = lambda z, a=1.0, b=3.0: a * z.real**2 + b * z.imag**2
R = np.array([[np.cos(m), -np.sin(m)], [np.sin(m), np.cos(m)]])
ph = rng.normal(size=(500, 2)) + 1j * rng.normal(size=(500, 2))
dR = np.max(np.abs(Q(ph @ R.T).sum(1) - Q(ph).sum(1)))
dC = np.max(np.abs(Q(ph @ C2.T).sum(1) - Q(ph).sum(1)))
check("control: a real coin conserves the phase-sensitive weight Re^2+3Im^2 (phase blindness needed)", dR < 1e-12, f"{dR:.1e}")
check("the complex mass coin does not conserve it", dC > 1e-2, f"{dC:.2f}")

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
