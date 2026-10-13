"""R19-9 (c): linear-response knob shift of the 6-knob root under the exact-vertex corner, dx = -J^{-1} dR(r), dR = 12 r^4 C_e
(exact to O(dR^2)); J as in r199_resolve.py. Also the shift per unit r^4 and the size of the second-order term (bound)."""
import numpy as np
C = np.load('corner_coeffs.npy')   # T2g, Eg, xz, face1, face2, body (per vector)
JF = np.load('facejac.npy')
Jax = np.array([[-5.6655e-04, 1.1701e-01, 8.2232e-03, 1.3886e+01], [-3.4987e-04, 7.8186e-02, 4.6650e-02, 1.3412e+01],
                [3.0830e-02, -5.6584e-01, 3.1372e-01, 0.0], [0.0, -3.2764e-02, 6.2509e-02, 0.0]])
J = np.zeros((6, 6)); J[:4, :4] = Jax; J[4:, :4] = JF; J[4:, 4:] = 12*np.array([[1.397040e-01, 2.892797e-01], [0.0, 5.785714e-01]])
dR1 = 12*np.array([C[0], C[1], 0, 0, C[3], C[4]])
dx1 = -np.linalg.solve(J, dR1)
print('per unit r^4: dR =', np.array2string(dR1, precision=4), '\n  dx (b_s, b_f, r_D, a, w_d, w_o) =', np.array2string(dx1, precision=4))
for r in (0.05, 0.1, 0.2):
    print(f'r = {r}: dx = {np.array2string(dx1*r**4, precision=3)}  | max|dx| {np.abs(dx1).max()*r**4:.2e}')
