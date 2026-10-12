"""Diagnostic for r154_bbn: local exponents of rho and of E during e+e- annihilation; the 'fast-reader' limit
rho_hat -> E / x_E (x_E := -dlnE/du), against rho; and a consistency check rho(u) = int_u^inf E du' (+ tail)."""
import numpy as np, sys
sys.argv = ['x']
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import importlib.util
src = open(__file__.rsplit('/', 1)[0] + '/r154_bbn.py').read().split('Ei = lambda')[0]
exec(src)
xr = E / rho
xE = -np.gradient(np.log(E), ugrid)
tail = rho[-1]  # pure radiation after: int_{u_end}^inf E = rho(u_end)
cum = np.concatenate([np.cumsum(((E[1:] + E[:-1]) / 2 * np.diff(ugrid))[::-1])[::-1], [0.0]]) + tail
for Tq in (1.0, 0.5, 0.3, 0.2, 0.158, 0.1, 0.07, 0.05, 0.03):
    i = np.argmin(np.abs(Ts - Tq))
    print(f'T={Ts[i]:.3f} MeV: x_rho={xr[i]:.4f}, x_E={xE[i]:.4f}, fast-reader E/x_E / rho - 1 = {E[i]/xE[i]/rho[i]-1:+.3e}, '
          f'int_u^inf E / rho - 1 = {cum[i]/rho[i]-1:+.2e}')
