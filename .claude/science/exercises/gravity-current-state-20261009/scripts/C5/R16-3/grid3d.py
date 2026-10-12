"""Direct 3D zone-grid evaluation of Xi (R9-9 Theorem T), both forms, looping over k_x slices.
A-form: Xi = (1/32) <|V|^2 A_zz / eps^5>, A_zz = g''(k_z)/2 - 1 = sigma'^2 + sigma sigma'' - 1.
IBP form: Xi = (1/32) <|V|^2 (5 f_z^2 - eps^2)/eps^7>."""
import numpy as np
def samples_full(law, N):
    kk = 2*np.pi*(np.arange(N)+0.5)/N - np.pi; a = np.abs(kk)
    s = np.interp(a, law.k, law.sig); sp = np.interp(a, law.k, law.sp)
    spp_f = np.gradient(law.sp, law.k); spp = np.interp(a, law.k, spp_f)
    g = s*s; f = np.sign(kk)*s*sp; A = sp*sp + s*spp - 1.0
    return g, f, A
def xi3d(law, m, N):
    g, f, A = samples_full(law, N); f2 = f*f
    gy = g[:, None]; gz = g[None, :]; fy2 = f2[:, None]; fz2 = f2[None, :]; Az = A[None, :]
    acc = {}
    names = ['M,T2g', 'M,Eg', 'U,T2g', 'U,Eg']
    for v in names: acc[v] = [0.0, 0.0]
    for i in range(N):
        gx, fx2 = g[i], f2[i]
        e2 = m*m + gx + gy + gz
        cA = Az/e2**2.5; cI = (5*fz2 - e2)/e2**3.5
        V = {'M,T2g': 4*gx*gy, 'M,Eg': (gx-gy)**2, 'U,T2g': 4*fx2*fy2, 'U,Eg': (fx2-fy2)**2}
        for v in names:
            Vv = np.broadcast_to(V[v], (N, 1)) if np.ndim(V[v]) == 2 else V[v]
            acc[v][0] += np.sum(Vv*cA); acc[v][1] += np.sum(Vv*cI)
    return {v: (acc[v][0]/N**3/32, acc[v][1]/N**3/32) for v in names}
