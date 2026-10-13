"""R19-16: why the law must be evaluated analytically (R0).  With R19-9's sigma (archived 400001-point trapezoid table, linear
interpolation beyond b) the EXACT divided difference (sigma1^2 - sigma2^2)/q has, as q -> 0, the limit 2 sigma x (chord slope of
the table cell), which jumps at every table node: the kernel cannot be continuous on the q_j = 0 planes whatever fallback is
used.  Measured: Delta at q = 1e-10 centred 1e-9 left / right of a node, archived table vs analytic law."""
import numpy as np, lib1916 as R
L = R.L; tab = L.LAW
a = tab.a; i0 = np.searchsorted(a, 3.05); q = 1e-10
def dd_tab(k1, k2):
    s1, s2 = R.ORIG['sig'](np.array([k1]))[0], R.ORIG['sig'](np.array([k2]))[0]; return (s1*s1 - s2*s2)/(k1 - k2)
mx_tab = mx_an = 0.0
for i in range(i0, i0 + 2000, 37):
    node = a[i]; h = a[1] - a[0]
    for (xl, xr) in ((node - 1e-9, node + 1e-9),):
        jt = abs(dd_tab(xl + q/2, xl - q/2) - dd_tab(xr + q/2, xr - q/2))
        ja = abs(R.dd1(xl + q/2, xl - q/2) - R.dd1(xr + q/2, xr - q/2))
        mx_tab, mx_an = max(mx_tab, jt), max(mx_an, ja)
print(f'table cell h = {a[1]-a[0]:.3e}; 55 nodes in the transition near k = 3.05: |Delta(node - 1e-9) - Delta(node + 1e-9)| at q = 1e-10:'
      f' archived-table sigma {mx_tab:.2e} (a jump) | analytic sigma (lib1916) {mx_an:.2e} (the smooth change g\'\' x 2e-9)')
