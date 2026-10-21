#!/usr/bin/env python3
"""C2b / KI+ and the C2 one-loop two-velocity flow (U(1) + N_f = 1 Dirac, toy content of C2 sec. 5).

Flow equations are quoted from blocks/C2/NOTE.md sec. 0.4 (derived and independently reviewed there):
  d ln eta/dl = (e^2/12 pi^2) [1/eta - 3 eta + 8/(1+eta)^2],   d(1/e^2)/dl = (eta + 1/eta)/(12 pi^2).
Checks:
  (1) eta = 1 is an exact zero of the beta function for every e (sympy): KI+ imposed at the cutoff gives
      delta(l) = 0 for all l at one loop -- provided the cutoff matching itself produces delta = 0.
  (2) Matching: a regulator that satisfies only KI+_w (universal dimension-4 forms, B4-breaking irrelevant terms)
      supplies a threshold delta_th = C (alpha/4pi) eps (toy coefficient from kip_collins_toy; illustrative).
      The flow then carries 0.78 delta_th to the IR (C2's suppression factor; recomputed here by integration).
"""
import sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

PASS = FAIL = 0


def check(name, ok, tag):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} [{tag}] {name}", flush=True)


eta, e = sp.symbols('eta e', positive=True)
beta = e**2/(12*sp.pi**2)*(1/eta - 3*eta + 8/(1 + eta)**2)
check('beta_eta(eta = 1) = 0 identically in e: the KI+ point is an exact fixed point of the one-loop flow', sp.simplify(beta.subs(eta, 1)) == 0, 'exact')
lin = sp.simplify(sp.diff(beta, eta).subs(eta, 1))
check(f'linearisation d delta/dl = {lin} delta = -(2 alpha/pi) delta (C2 value, alpha = e^2/4pi)', sp.simplify(lin + 2*(e**2/(4*sp.pi))/sp.pi) == 0, 'exact')


def rhs(l, y):
    d, inv_e2 = y
    et = np.exp(d); e2 = 1/inv_e2
    return [e2/(12*np.pi**2)*(1/et - 3*et + 8/(1 + et)**2), (et + 1/et)/(12*np.pi**2)]


alpha_IR = 1/137.036; L = 51.0
# alpha_UV from Lorentz-limit running (eta = 1): d(1/e^2)/dl = 1/(6 pi^2)
inv_e2_UV = 1/(4*np.pi*alpha_IR) - L/(6*np.pi**2)
for d0 in (0.0, 1e-6, 1e-3):
    sol = solve_ivp(rhs, (0, L), [d0, inv_e2_UV], rtol=1e-12, atol=1e-30)
    dIR = sol.y[0, -1]
    if d0 == 0.0:
        check(f'delta_UV = 0 (KI+ at the cutoff) stays 0 over l = {L}: delta_IR = {dIR:.1e}', dIR == 0.0, 'numerical')
    else:
        print(f"  delta_UV = {d0:.0e} -> delta_IR = {dIR:.4e}, ratio {dIR/d0:.5f}")
        if d0 == 1e-6:
            r = dIR/d0
check(f'small-mismatch IR/UV ratio {r:.4f} matches C2 value 0.781 to 1e-3', abs(r - 0.7813) < 1e-3, 'numerical')
# illustrative threshold from a KI+_w-only regulator (toy coefficient, see kip_collins_toy.log)
for C, eps in ((0.3, 0.05), (0.3, 1.0)):
    dth = C*alpha_IR/(4*np.pi)*eps
    print(f"  illustrative KI+_w threshold: C = {C}, eps = {eps}: delta_th ~ {dth:.1e} -> delta_IR ~ {r*dth:.1e}"
          f"  (vs illustrative bound 1e-15: excess factor {r*dth/1e-15:.0e})")
check('a KI+_w-only threshold of the toy size exceeds a 1e-15 bound by > 1e8 even for eps = 0.05',
      r*0.3*alpha_IR/(4*np.pi)*0.05 > 1e-7, 'numerical (illustrative)')
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
