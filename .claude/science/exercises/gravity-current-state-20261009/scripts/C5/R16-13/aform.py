"""R16-13: A-form (pointwise, box-free) evaluator of the Dirac identity
   Xi_F = (Nc/8) < |G|^2 (|d_z c|^2 - 1)/E^3 >  -  (Nc/32) < |V|^2 A_zz / E^5 >,   |V|^2 = 4 (c.G)^2, A_zz = Hess_zz(E^2/2) - 1
for D1 (4-comp, non-separable), G perpendicular to beta (vertex V0).  Both integrands vanish for k_z in the box."""
import numpy as np
from dirac import kgrid
def d1_aform(law, m, N, Nc=4, zchunk=None):
    k = kgrid(N)
    S, Sp, Spp = law.S(k), law.dS(k), law.d2S(k)
    W, Wp, Wpp = law.W(k), law.dW(k), law.d2W(k)
    I = np.arange(N); X, Y = np.meshgrid(I, I, indexing='ij')
    Sx, Sy = S[X][..., None], S[Y][..., None]
    Mp = m + W[X][..., None] + W[Y][..., None]
    M = Mp + W[None, None, :]
    E2 = Sx**2 + Sy**2 + S[None, None, :]**2 + M**2
    cp2 = (Sp**2 + Wp**2)[None, None, :]
    Azz = (Sp**2 + S*Spp + Wp**2)[None, None, :] + M*Wpp[None, None, :] - 1
    G2 = 0.25*(Sx**2 + Sy**2)
    out = {}
    for pol, cG in (('T2g', Sx*Sy), ('Eg', 0.5*(Sx**2 - Sy**2))):
        aterm = (Nc/8)*float(np.mean(G2*(cp2 - 1)/E2**1.5))
        sterm = -(Nc/32)*float(np.mean(4*cG**2*Azz/E2**2.5))
        out[pol] = (aterm + sterm, aterm, sterm)
    return out
