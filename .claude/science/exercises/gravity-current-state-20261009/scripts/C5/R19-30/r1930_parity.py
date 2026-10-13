"""R19-30 (a): offset-parity content of the midpoint kernels.  For component ij the class sigma = tau_ij = (e_i + e_j) mod 2
is the one that sits at R9-9's placement p_ij; every other class is displaced by half a lattice step in the directions
where sigma_l != tau_l.  RMS over the zone (uniform kbar sample) of each class, relative to the whole component."""
import numpy as np
import lib1930 as L
DI, SC = L.Dirac(m=0.01), L.Scalar(m=0.01)
kb = np.random.default_rng(193011).uniform(-np.pi, np.pi, (20000, 3))
for lab, fun_of in (('Dirac UD', lambda i, j: (lambda kk: DI.UDcoef(kk, i, j))),
                    ('scalar E1 U', lambda i, j: (lambda kk: (SC.f(kk[..., i])*SC.f(kk[..., j]))[..., None]))):
    for (i, j) in ((0, 1), (0, 0)):
        parts = L.parity_parts(fun_of(i, j), kb); tot = np.sqrt(np.mean(np.sum(fun_of(i, j)(kb)**2, -1)))
        t = tuple(L.tau(i, j)); s = sorted(parts.items(), key=lambda kv: -np.mean(np.sum(kv[1]**2, -1)))
        txt = ', '.join('%s%s %.3f' % (''.join(map(str, kk)), '*' if kk == t else '', np.sqrt(np.mean(np.sum(v**2, -1)))/tot) for kk, v in s if np.sqrt(np.mean(np.sum(v**2, -1)))/tot > 1e-12)
        print('%-11s T^%s%s: RMS share by class sigma (* = sits at p_ij): %s' % (lab, 'xyz'[i], 'xyz'[j], txt))
