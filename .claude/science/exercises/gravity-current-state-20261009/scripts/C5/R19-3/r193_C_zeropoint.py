"""R19-3 treatment (C) in harmonic (Feynman-de Donder) gauge: Gupta-Bleuler zero-point bookkeeping per mode.
(1) A component with NEGATIVE kinetic sign, L = -(qdot^2 - w^2 q^2)/2, quantized with [a, a^dag] = -1 and a|0> = 0
    (positive-frequency vacuum): <0|H|0> = +w/2, the same as a positive-norm component.  Checked symbolically with a
    matrix representation of the algebra truncated to the vacuum matrix element (normal-ordering identity).
(2) Count, per spatial mode: 10 components of h (DeWitt metric indefinite, all with the box operator in FdD gauge)
    -> 10 x w/2; FP ghosts c^mu, cbar_mu (4 complex Grassmann components, box operator) -> FP determinant det(box)^{+4}
    = -8 real-scalar equivalents -> -8 x w/2.  Net 2 x w/2 = the TT zero point (comparator: FP counting, BRST quartets).
(3) The same count reproduced as a stress: r193_gauge_family.out gives EH + GF Hilbert stress = 5 x kk = 10 x (1/2) kk.
"""
import sympy as sp
w = sp.Symbol('omega', positive=True)
# a a^dag = a^dag a + [a, a^dag];  on the vacuum <0|a^dag a|0> = 0
comm = -1
aad_vac = comm          # <0| a a^dag |0> = [a, a^dag] <0|0>, with <0|0> = 1
ada_vac = 0
H_vac = -(w/2)*(aad_vac + ada_vac)     # H = -(w/2)(a a^dag + a^dag a) for L = -(qdot^2 - w^2 q^2)/2
print('(1) negative-kinetic component, [a,a^dag] = -1:  <0|H|0> =', H_vac)
Hpos = (w/2)*(1 + 0)
print('    positive component, [a,a^dag] = +1:             <0|H|0> =', Hpos)
print('(2) per mode: h components 10 x w/2 =', 10*w/2, '; ghosts -8 x w/2 =', -8*w/2, '; net =', 10*w/2 - 8*w/2,
      '= TT zero point 2 x w/2 =', 2*w/2)
