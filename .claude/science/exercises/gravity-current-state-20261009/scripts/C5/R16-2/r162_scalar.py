"""R16-2: ON-SHELL one-loop speed of a charged complex scalar (spin 0) on a separable band eps^2 = m^2 + sum_j u(k_j),
Peierls-gauged (axis paths) to R8-5's non-compact box photon (W^2 = sum_j d(q_j)^2 + lam^2), Feynman gauge, Z^3 x R.
Euclidean action |(d_tau + i e A_tau) phi|^2 + phi^dag u_A phi + m^2 |phi|^2; Gamma_2 = p0^2 + eps^2(p) + Pi(p0, p),
Pi = <S_2> - (1/2)<S_1 S_1>_c (per e^2):
  Pi = < [1 + sum_j (u(p_j+q_j) + u(p_j-q_j) - 2u(p_j)) / (2 d_j^2)] / (2W) >_q                       (seagulls)
     - < J0(W, E_k, p0) + sum_j (u(p_j) - u(k_j))^2 / d_j^2 * J1(W, E_k, p0) >_q,   k = p - q           (exchange)
  J1 = int dq0/2pi D Delta,  J0 = int dq0/2pi (2p0 - q0)^2 D Delta (closed forms, r162_j0_check.out), at p0 = iE_p:
  J1 = (W+Ek)/(2 W Ek (W+Ek-E)(W+Ek+E)),  J0 = (W^2 Ek + W Ek^2 - W E^2 - 4 Ek E^2)/(2 W Ek (W+Ek-E)(W+Ek+E)).
On shell (first order): E^2(p) = eps^2(p) + Pi(iE_p, p);  c^2 - 1 = d Pi(iE_p, p)/d(p^2) at p = 0 (Richardson), dc = (c^2-1)/2.
Seagull speed term (exact, m-independent): <A(q_x)/(2 d_x^2 W)> in c^2 - 1, A = u''/2 - 1 (scalar boost anomaly).
Heavy-mass check (R13-7 Theorem H analogue; spatial exchange is O(1/m)): dc -> (1/4)<A (d_y^2 + d_z^2 + lam^2)/(d_x^2 W^3)>.
Photon side: Theorem T' (R10-1, refereed): dc_gamma(scalar) = (1/32)<u'(k_y)^2 A(k_x)/eps^5>.
Subtractions named before any run: none.
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r162_laws import GScal
from r85_box_qed_copy import kgrid1

U = 16*np.pi**2

def Pi_onshell(law, N, lam, ps, chunk=8):
    q1 = kgrid1(N)
    QY, QZ = np.meshgrid(q1, q1, indexing='ij')
    dy2, dz2 = law.d(QY)**2, law.d(QZ)**2
    uy, uz = law.u(QY), law.u(QZ)
    Vyz = uy**2/dy2 + uz**2/dz2                     # (u(0) - u(-q))^2/d^2, u(0) = 0, u even
    out = {}
    for p in ps:
        up = float(law.u(np.array(p))); Ep = np.sqrt(law.m**2 + up)
        sea = 0.0; exch = 0.0; sea_const = 0.0
        for i0 in range(0, N, chunk):
            qx = q1[i0:i0+chunk][:, None, None]
            dx2 = law.d(qx)**2
            W = np.sqrt(dx2 + dy2[None] + dz2[None] + lam**2)
            kx = p - qx
            Ek = np.sqrt(law.m**2 + law.u(kx) + uy[None] + uz[None])
            V2 = (up - law.u(kx))**2/dx2 + Vyz[None]
            den = 2*W*Ek*(W + Ek - Ep)*(W + Ek + Ep)
            J1 = (W + Ek)/den
            J0 = (W**2*Ek + W*Ek**2 - W*Ep**2 - 4*Ek*Ep**2)/den
            exch += np.sum(J0 + V2*J1)
            sea += np.sum((law.u(p + qx) + law.u(p - qx) - 2*up)/(2*dx2)/(2*W) + 0*W)
        V = N**3
        out[p] = dict(Ep=Ep, Pi=(sea - exch)/V, sea=sea/V, exch=exch/V)
    return out

def dc_scalar(law, N, lam, h):
    r = Pi_onshell(law, N, lam, [0.0, h, 2*h])
    def d2(key):
        D1 = (r[h][key] - r[0.0][key])/h**2; D2 = (r[2*h][key] - r[0.0][key])/(4*h**2)
        return (4*D1 - D2)/3
    return d2('Pi')/2*U, d2('sea')/2*U

def seagull_closed(law, N, lam):
    q1 = kgrid1(N); QX, QY, QZ = np.meshgrid(q1, q1, q1, indexing='ij')
    dx2, dy2, dz2 = law.d(QX)**2, law.d(QY)**2, law.d(QZ)**2
    W = np.sqrt(dx2 + dy2 + dz2 + lam**2); A = law.upp(QX)/2 - 1
    return np.mean(A/(2*dx2*W))/2*U, np.mean(A*(dy2 + dz2 + lam**2)/(dx2*W**3))/4*U

def photon_moment(law, N):
    k1 = kgrid1(N); KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    eps = np.sqrt(law.m**2 + law.u(KX) + law.u(KY) + law.u(KZ))
    return np.mean(law.up(KY)**2*(law.upp(KX)/2 - 1)/eps**5)/32*U

def hstep(m, lam):
    return min(0.02, 0.3*np.sqrt(2*m*lam))

if __name__ == '__main__':
    mode = sys.argv[1]; t0 = time.time()
    if mode == 'heavy':   # validation: heavy-mass limit against the closed form
        for (b, c1, c2) in [(1.0, None, None), (1.4, 1.0, 2.0)]:
            lam = 0.05; N = 96
            L = GScal(b, c1, c2, 1.0); sc, hv = seagull_closed(L, N, lam)
            print('G(b=%.1f) ph=%s lam=%.2f N=%d: seagull closed %+9.4f | heavy closed form %+9.4f' % (b, c1, lam, N, sc, hv), flush=True)
            vals = []
            for m in (12.8, 25.6, 51.2, 102.4):
                L = GScal(b, c1, c2, m); dc, dsea = dc_scalar(L, N, lam, 0.02); vals.append((m, dc))
                print('   m=%6.1f  dc0*U = %+9.4f  [seagull part %+9.4f]' % (m, dc, dsea), flush=True)
            (m1, v1), (m2, v2) = vals[-2], vals[-1]
            print('   Richardson in 1/m (51.2, 102.4): %+9.4f   vs closed form %+9.4f' % (2*v2 - v1, hv), flush=True)
    if mode == 'conv':
        for (b, c1, c2) in [(1.0, None, None), (1.4, None, None)]:
            for m in (0.1, 0.05):
                for lam in (0.05, 0.02, 0.01):
                    for N in (96, 128, 192):
                        L = GScal(b, c1, c2, m); dc, dsea = dc_scalar(L, N, lam, hstep(m, lam))
                        print('G b=%.1f ph=%s m=%.3f lam=%.3f N=%3d  F0*U=%+9.4f [seagull %+9.4f, rest %+8.4f]'
                              % (b, c1, m, lam, N, dc, dsea, dc - dsea), flush=True)
    if mode == 'family':
        N = int(sys.argv[2]); lam = 0.02
        for b in (0.6, 1.0, 1.4, 2.0, 2.6):
            for (c1, c2) in [(None, None), (1.0, 2.0), (2.0, 3.0)]:
                row = []
                for m in (0.2, 0.1, 0.05):
                    L = GScal(b, c1, c2, m); dc, dsea = dc_scalar(L, N, lam, hstep(m, lam)); row.append((m, dc, dsea))
                ms = np.array([x[0] for x in row]); Fs = np.array([x[1] for x in row]); c = np.polyfit(ms, Fs, 2)
                G0 = photon_moment(GScal(b, c1, c2, 0.05), N)
                print('G(b=%.1f) ph=%-4s N=%d | F0(0.2,0.1,0.05)= %+8.4f %+8.4f %+8.4f | seagull %+8.4f | F0_extrap %+8.4f slope %+7.3f | G0(0.05) %+8.4f'
                      % (b, c1, N, Fs[0], Fs[1], Fs[2], row[2][2], c[2], c[1], G0), flush=True)
    print('elapsed %.1fs' % (time.time() - t0))
