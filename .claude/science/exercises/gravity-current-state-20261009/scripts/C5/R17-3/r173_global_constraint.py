"""R17-3 probe (b): global constraints for C in R16-6's homogeneous H-Z model with g == 0 (3H^2 = rho_tot - C, kappa = 1).
B1  Early-time sensitivity: two branches agreeing up to u1 and ending in V_hi or V_lo.  With Lambda_late = 0 on each,
    C = V_late, so 3H^2(u) differs by exactly Delta V at every u < u1 (Theorem NA's content, made quantitative).
B2  A final-state rule C = V_late is not an initial-value law: with a Hubble-sensitive decay trigger at u1
    (decay iff H^2(u1) < Hs^2, type 1; or iff H^2(u1) > Hs^2, type 2) there are windows of Hs with
    NO self-consistent history (type 1) or TWO (type 2).  Enumerated exactly.
B3  The causal running 4-volume average of the w = -1 part, C(t) = int a^3 rho_v dt / int a^3 dt (a vacuum-detecting
    reader is GRANTED here), is time-dependent, so g = C'/3 != 0 (R15-1 signalling) after every vacuum change;
    only its t -> infinity limit is constant and equals V_late (a final-state datum).
Subtraction named before the run: C only.  Units kappa = 1, radiation rho_r0 e^{-4u}.
"""
import numpy as np
rr0, u1 = 1.0, 2.0
Vhi, Vlo = 0.02, 0.0
dV = Vhi - Vlo
print("B1  Early-time expansion on the two branches (C = V_late on each):")
for u in [0.0, 1.0, 1.9]:
    rho = rr0*np.exp(-4*u) + Vhi
    H2a = (rho - Vhi)/3; H2b = (rho - Vlo)/3
    print("   u=%.1f: 3H^2(no decay) = %.6f  3H^2(decay later) = %.6f  difference = %.6f (= Delta V = %.3f) ; relative %.3e"
          % (u, 3*H2a, 3*H2b, 3*(H2b - H2a), dV, (H2b - H2a)/H2a))
print("B2  Final-state rule C = V_late with a decay trigger at u1 = %.1f:" % u1)
rho1 = rr0*np.exp(-4*u1) + Vhi
for trig in [1, 2]:
    rows = []
    for Hs2 in np.linspace(0.0, 0.03, 13):
        sols = []
        for C, Vl in [(Vhi, Vhi), (Vlo, Vlo)]:
            H2 = (rho1 - C)/3
            decays = (H2 < Hs2) if trig == 1 else (H2 > Hs2)
            Vlate = Vlo if decays else Vhi
            if np.isclose(Vlate, C): sols.append('C=V_hi' if C == Vhi else 'C=V_lo')
        rows.append((Hs2, sols))
    print("   trigger type %d (decay iff H^2(u1) %s Hs^2); H^2(u1) = %.5f if C=V_hi, %.5f if C=V_lo:"
          % (trig, '<' if trig == 1 else '>', (rho1 - Vhi)/3, (rho1 - Vlo)/3))
    for Hs2, sols in rows:
        print("      Hs^2=%.4f: consistent histories: %d %s" % (Hs2, len(sols), sols))
print("B3  Causal running 4-volume average (vacuum part granted), matter era a ~ t^(2/3) after a step at t_tr = 1:")
for T in [2.0, 10.0, 1e2, 1e4, 1e6]:
    # vacuum Vhi on [0, t_tr], Vlo after ; weight a^3 ~ t^2 (matter era throughout, for the illustration)
    num = Vhi*(1.0**3)/3 + Vlo*(T**3 - 1)/3
    den = T**3/3
    C = num/den
    # dC/dt = (a^3/int a^3)(rho_v - C) = 3/T * (Vlo - C) ; H = 2/(3T) ; g = (1/3) dC/du = dC/dt/(3H)
    dCdt = 3/T*(Vlo - C)
    H = 2/(3*T)
    g = dCdt/(3*H)
    print("   T=%.0e: C - V_late = %.3e (Delta V (t_tr/T)^3 = %.3e) ; g = C'/3 = %.3e ; g/H^2 = %.3e"
          % (T, C - Vlo, dV/T**3, g, g/H**2))
print("   -> g != 0 at every finite time after the step (signalling, R15-1); C -> V_late only as T -> infinity (final state).")
# Sizes of the running-average residual today for early SM steps (orders of magnitude; RECALLED inputs, a_i, t_i)
print("B3' Order-of-magnitude residual of the causal running average today (RECALLED a, t; 4-volume fraction ~ (a_i/a0)^3 (t_i/t0)):")
t0 = 4.35e17
for name, ai, ti, dVr in [('EW', 1e-15, 1e-11, 4.7e54), ('QCD', 1e-12, 1e-5, 1e44), ('inflation', 1e-28, 1e-36, 2.6e111)]:
    f = ai**3*ti/t0
    print("   %-9s: 4-volume fraction ~ %.1e ; residual ~ %.1e rho_Lambda" % (name, f, f*dVr))
