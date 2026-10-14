"""F5 branch MF (NOT registered; a stated choice, used only to SIZE the T2g coefficient gamma' that F1's frame class cannot give):
the photon is strained by a CONSTANT vielbein E = exp((t/2) h) acting on LINK fields with the unstrained (odd) lattice symbols
d_j(q) = sign(q_j) h(|q_j|):  frame field a~ = E a, gauge a_j -> a_j + d_j chi (so the generalized-link denominators vanish only at
q_j = 0: regular for every h), Feynman gauge in frame fields.  Link-field propagator P_jl/(Q0^2 + Om^2), P = E^-1 E^-T = exp(-t h),
Om^2 = d.exp(t h).d.  In the photon's linear region (|q_j| < 2.9435, where its SF flow is the linear map E) this equals the SF photon;
it differs from F1's frame-component SF photon only near the photon box edge.  Dirac: D_t = D o Phi^F_t (SF), Psym links as F1.
Mass part (general symmetric P, Psym so a' = a):
  exchange num = M + sum_jl P_jl [ (a_j.a_l - b_j b_l) M - b_j (a_l.c) - b_l (a_j.c) ],  a_j = L_j^c/d_j, b_j = L_j^M/d_j
  tadpole = sum_j P_jj M(j)/d_j^2 + sum_{j!=l} P_jl T^M_jl,
  T^M_jl = -(1/(2 d_j d_l)) { (2/3)[M(j) + M(l) - M(jl)] + (1/3)[M(jm) + M(lm) - M(q) - M(m)] }   (j != l, m the third axis)
  [Psym off-diagonal seagull at (q, -q): average over the 6 orderings of the j-leg x l-leg Wilson-line product; the 4 orderings with
   no leg between j and l give the first bracket, the 2 with m between give the second; M = M_t at the flowed box corners].
  Longitudinal Ward: sum_jl d_j d_l T^M_jl = M(q) - ... (checked numerically below, '--ward').
argv: mode ('ward' | 'hess') h ('Eg' | 'T2g') n hmax mph d"""
import numpy as np, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f5_lib import *
from scipy.linalg import expm


def dodd(G, q):
    return np.sign(q)*G.d(q) + (q == 0)*0.0


def corners(F, h, X, Y, Z, t, nrk=2):
    s, W = F.s, F.W
    def DF(a, b, c):
        u, v, w = flow3(F, h, a, b, c, t, nrk)
        return (s(u), s(v), s(w), W(u) + W(v) + W(w))
    z0 = 0.0*X*Y*Z
    C = {}
    C['x'] = DF(X + z0, z0, z0); C['y'] = DF(z0, Y + z0, z0); C['z'] = DF(z0, z0, Z + z0)
    C['xy'] = DF(X + z0, Y + z0, z0); C['xz'] = DF(X + z0, z0, Z + z0); C['yz'] = DF(z0, Y + z0, Z + z0)
    C['q'] = DF(X + z0, Y + z0, Z + z0)
    C['0'] = (z0, z0, z0, z0)
    return C


def vert(C):
    def diff(A, B): return tuple(a - b for a, b in zip(A, B))
    def avg4(A, B, Cc, D): return tuple((2*a + b + c + 2*d)/6.0 for a, b, c, d in zip(A, B, Cc, D))
    Vx = avg4(diff(C['x'], C['0']), diff(C['xy'], C['y']), diff(C['xz'], C['z']), diff(C['q'], C['yz']))
    Vy = avg4(diff(C['y'], C['0']), diff(C['xy'], C['x']), diff(C['yz'], C['z']), diff(C['q'], C['xz']))
    Vz = avg4(diff(C['z'], C['0']), diff(C['xz'], C['x']), diff(C['yz'], C['y']), diff(C['q'], C['xy']))
    return (Vx, Vy, Vz)


AX = ('x', 'y', 'z')
def pair_key(a, b):
    return ''.join(sorted(a + b, key=lambda k: AX.index(k)))


def seagull_M(C, dd):
    """T^M_jl (3x3) at the points; diagonal M(j)/d_j^2."""
    M = {k: C[k][3] for k in C}
    T = [[None]*3 for _ in range(3)]
    for j in range(3):
        T[j][j] = M[AX[j]]/dd[j]**2
    for j in range(3):
        for l in range(3):
            if j == l: continue
            m = 3 - j - l
            aj, al, am = AX[j], AX[l], AX[m]
            b1 = M[aj] + M[al] - M[pair_key(aj, al)]
            b2 = M[pair_key(aj, am)] + M[pair_key(al, am)] - M['q'] - M[am]
            T[j][l] = -(2.0/3.0*b1 + 1.0/3.0*b2)/(2*dd[j]*dd[l])
    return T


def dm_mf(F, G, h, xs, ys, zs, t, mprop=0.0, nrk=2, chunk=None, parts=False):
    x, wx = xs; y, wy = ys; z, wz = zs
    Nx, Ny = len(x), len(y)
    if chunk is None:
        chunk = max(1, int(6e4/(Nx*Ny)))
    P = expm(-t*np.asarray(h, float)); Gm = expm(t*np.asarray(h, float))
    tad = 0.0; loop = 0.0
    for i0 in range(0, len(z), chunk):
        iz = np.arange(i0, min(len(z), i0 + chunk))
        X = x[:, None, None]; Y = y[None, :, None]; Z = z[iz][None, None, :]
        C = corners(F, h, X, Y, Z, t, nrk)
        dd = [dodd(G, X) + 0*Y*Z, dodd(G, Y) + 0*X*Z, dodd(G, Z) + 0*X*Y]
        Om = np.sqrt(sum(Gm[j, l]*dd[j]*dd[l] for j in range(3) for l in range(3)))
        V = vert(C)
        c = C['q'][:3]; M = mprop + C['q'][3]
        E = np.sqrt(c[0]**2 + c[1]**2 + c[2]**2 + M*M)
        a = [[V[j][k]/dd[j] for k in range(3)] for j in range(3)]
        b = [V[j][3]/dd[j] for j in range(3)]
        num = M
        for j in range(3):
            for l in range(3):
                if P[j, l] == 0.0: continue
                aa = a[j][0]*a[l][0] + a[j][1]*a[l][1] + a[j][2]*a[l][2]
                ajc = a[j][0]*c[0] + a[j][1]*c[1] + a[j][2]*c[2]
                alc = a[l][0]*c[0] + a[l][1]*c[1] + a[l][2]*c[2]
                num = num + P[j, l]*((aa - b[j]*b[l])*M - b[j]*alc - b[l]*ajc)
        T = seagull_M(C, dd)
        tadj = sum(P[j, l]*T[j][l] for j in range(3) for l in range(3) if P[j, l] != 0.0)
        ww = wx[:, None, None]*wy[None, :, None]*wz[iz][None, None, :]
        tad += float((ww*tadj/(2*Om)).sum())
        loop += float((ww*num/(2*E*Om*(E + Om))).sum())
    if parts:
        return tad + loop, tad, loop
    return tad + loop


if __name__ == '__main__':
    t00 = time.time()
    mode = sys.argv[1]
    F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
    if mode == 'ward':
        rng = np.random.default_rng(1)
        for lab, h in (('E_g', H_EG), ('T2g', H_T2), ('nn[110]', 0.5*np.array([[1., 1, 0], [1, 1, 0], [0, 0, 0]]))):
            q = rng.uniform(-np.pi, np.pi, (3, 2000))
            X, Y, Z = q[0], q[1], q[2]
            C = corners(F, h, X, Y, Z, 0.3, 4)
            dd = [dodd(G, X), dodd(G, Y), dodd(G, Z)]
            T = seagull_M(C, dd)
            lhs = sum(dd[j]*dd[l]*T[j][l] for j in range(3) for l in range(3))
            V = vert(C)
            w1 = [sum(V[j][k] for j in range(3)) - C['q'][k] for k in range(4)]   # sum_j d_j (V_j^link) = sum_j avg L_j = D_t(q) - D_t(0)
            print('%-8s t=0.3: two-photon longitudinal Ward  max|sum_jl d_j d_l T^M_jl - M_t(q)| = %.2e (scale %.2f);  one-photon Ward max %.2e'
                  % (lab, np.max(np.abs(lhs - C['q'][3])), np.max(np.abs(C['q'][3])), max(np.max(np.abs(w)) for w in w1)), flush=True)
        sys.exit(0)
    which, n, hm, mph, d = sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
    br = mkbreaks(ROOT[0], CPH, mph)
    xo = panels(br, n, hm); xs = panels_sym(br, n, hm)
    if which == 'Eg':
        h, dom = H_EG, (xo, xo, xo)
    else:
        h, dom = H_T2, (xs, xo, xo)
    f0 = dm_mf(F, G, h, *dom, 0.0); f1 = dm_mf(F, G, h, *dom, d); f2 = dm_mf(F, G, h, *dom, 2*d)
    fm = dm_mf(F, G, h, *dom, -d)
    h1 = 2*(f1 - f0)/d**2; h2 = 2*(f2 - f0)/(2*d)**2
    print('branch MF, %s, grid n=%d hmax=%.2f mph=%d (%d nodes/half-axis), d=%.4f' % (which, n, hm, mph, len(xo[0]), d))
    print('  dm0 %+.10f (F1 t=0: +0.0418583908)  dm(d) %+.13e dm(-d) %+.13e (evenness diff %.1e)' % (f0, f1, fm, f1 - fm))
    print('  Hess (d) %+.7e (2d) %+.7e Rich %+.7e   [%.0f s]' % (h1, h2, (4*h1 - h2)/3, time.time() - t00), flush=True)
