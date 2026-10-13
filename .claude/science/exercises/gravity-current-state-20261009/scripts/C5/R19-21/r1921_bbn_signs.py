"""R19-21 (b)/(d): BBN-epoch numbers and the sign structure of the fixed-state shear mismatch.
Imports r1921_history.py's functions (same inputs). Even (twisted-type) part: mu_UV = c + R2 <|phi|^2>/v^2 in mean field, so
Delta mu(T) = R2 (<|phi|^2>_T - v^2)/v^2: above T_c <|phi|^2>_T ~ 4<dphi_1^2> (~ T^2/3 massless), below T_c ~ v(T)^2 (+ massive fluctuations).
Zero crossing near T* = sqrt(3) v (massless estimate) -> opposite signs on the two sides, whatever the sign of R2."""
import io, contextlib, numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import r1921_history as H
Tbbn = 1e-3
dx = H.dx_lin(Tbbn)
print('BBN, T = 1 MeV: dx (linear response, free e+- etc.; hadrons ignored) = %.2e' % dx)
for edge, r in (('W', 'E'), ('W', 'T'), ('tw', 'E'), ('tw', 'T')):
    d = H.C[edge][r][0]*H.S1*dx + H.R2(edge, r)*(2*dx + dx*dx)   # dx passed directly (1 + dx underflows in double precision)
    print('  %-7s mu_%s: Delta mu %+.2e  ->  m_g^2/H^2 = %+.2e' % ({'W': 'Wilson', 'tw': 'twisted'}[edge], r, d, 16*np.pi*d/H.Ha2(Tbbn)))
rr = (np.pi**2/30)*10.75*(Tbbn/H.MP)**4
print('  one-point enthalpy (D1 dW/dm = -0.6923 per field, r1921_enthalpy.out): |Delta W|/rho_rad = %.1e (Wilson-type), %.1e (twisted, dW/dm^2 = -0.4503)'
      % (abs(0.6923204*H.S1*dx)/rr, abs(0.450262*H.S2*2*dx)/rr))
print('\nEven part: Delta mu(T)/R2 = (<|phi|^2>_T - v^2)/v^2 (mean field), R2 = sum n c2 (ma)^2 per row:')
for r in ('E', 'T'):
    print('  R2(twisted, mu_%s) = %+.3e' % (r, H.R2('tw', r)))
for T in (1e3, 600, 450, 426, 400, 300, 170, 150, 100, 10):
    if T > H.Tc: phi2 = 4*H.Jb(np.sqrt(0.4)*T, T)
    else: phi2 = (1 + H.dx_lin(T))**2*H.v**2 + 4*H.Jb(H.mH, T)
    print('  T = %-6g GeV: (<|phi|^2> - v^2)/v^2 = %+.3f' % (T, (phi2 - H.v**2)/H.v**2))
# electron-only BBN shift (free quarks are unphysical below the QCD crossover; the line above includes them)
me = 0.000511
dxe = -2*me*me*2*H.Jf(me, Tbbn)/(H.v**2*H.mH**2)
print('\nBBN electron-only: dx = %.2e' % dxe)
for edge, r in (('W', 'E'), ('W', 'T'), ('tw', 'E'), ('tw', 'T')):
    d = H.C[edge][r][0]*H.S1*dxe + H.R2(edge, r)*2*dxe
    print('  %-7s mu_%s: Delta mu %+.2e -> m_g^2/H^2 = %+.2e' % ({'W': 'Wilson', 'tw': 'twisted'}[edge], r, d, 16*np.pi*d/H.Ha2(Tbbn)))
print('  enthalpy |Delta W|/rho_rad = %.1e (Wilson-type D1), %.1e (twisted)' % (abs(0.6923204*H.S1*dxe)/rr, abs(0.450262*H.S2*2*dxe)/rr))
