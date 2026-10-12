"""R11-4: compare the box-sector stress's full pole-dipole moments on the bound triplet with the flat-space
Dixon pole-dipole stress of a spinning particle, T = p^(mu u^nu) delta/u0 - d_rho(S^{rho(mu} u^nu) delta/u0),
in the Newton-Wigner SSC S^{a0} = d_a = (P x S)_a/(M+H)  (S^{ab} = eps_abc S_c).  Dixon moments at z = 0:
  int T00 = E, int x_a T00 = S^{a0};  int T0i = P_i,  int x_a T^{0i} = (S^{a0} v_i + S^{ai} + S^{i0} v_a)/2;
  int T^ij = P_i v_j,  int x_a T^ij = (S^{ai} v_j + S^{aj} v_i)/2 + v_a (S^{i0} v_j + S^{j0} v_i)/2.
Uses the closed-form box-sector stress of r114_bsector.py (imported)."""
import numpy as np, sys, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import r114_bsector as rb
eps3, S, I3 = rb.eps3, rb.S, rb.I3
for Mb in (0.95, 0.85, 0.70):
    B = rb.Bsector(Mb)
    for P in (np.array([0.0, 0.0, 0.0]), np.array([0.21, -0.13, 0.30]), np.array([0.0, 0.5, 0.1])):
        h = B.h(P); v = P/h; d = B.d(P)
        Sab = np.einsum('abc,cij->abij', eps3, S)
        m1 = rb.fd1(lambda P_, Q_: B.tau(P_, Q_), P)
        e = 0.0
        for a in range(3):
            e = max(e, np.abs(m1[a,0,0] - d[a]).max())
            for i in range(3):
                dix = 0.5*(d[a]*v[i] + Sab[a,i] + d[i]*v[a])
                e = max(e, np.abs(m1[a,0,i+1] - dix).max())
                for j in range(3):
                    dix = 0.5*(Sab[a,i]*v[j] + Sab[a,j]*v[i]) + 0.5*v[a]*(d[i]*v[j] + d[j]*v[i])
                    e = max(e, np.abs(m1[a,i+1,j+1] - dix).max())
        print('M_b = %.2f, P = %s: max |box first moments - Dixon(NW SSC)| over all (a, mu, nu) = %.1e' % (Mb, np.round(P, 2), e))
