"""R19-26: placement repair of the R19-9/R19-16 photon kernel at the wrapped-transfer cut q_j = +-pi.

Importing this module imports lib1916 (which patches lib199 with R0/R1/R2) and then, if patch() is called, replaces
lib199.spatial_VW by the RE-PLACED VW spatial kernel

    M~^{ij}(k1, k2) = F(q_i) F(q_j) VW^{ij}(k1, k2)   (i != j),     M~^{ii} = VW^{ii},     q = wrap(k1 - k2)   (graviton rep.)
    F(q) = (9 cos(q/2) - cos(3q/2))/8 :  antiperiodic, F(0) = 1, F''(0) = 0  (F = 1 - 3 q^4/128 + O(q^6)), F(+-pi) = 0.

Why (diagnosis, see r1926_diag.py): R18-13's VWa-geo places every off-diagonal bilinear at the SITE ("both fields averaged
along their own index -> site", vwface.py:6-10), while R9-9's graviton (and lib199's tilde bookkeeping, lib199.py:7-10)
needs T^{ij} at (e_i + e_j)/2.  Using VW^{ij} itself as the tilde kernel is an exact half-shift e^{-i(q_i+q_j)/2} of a site
operator: on the q-torus it is discontinuous at q_i = +-pi or q_j = +-pi (the referee's cut).  e^{-iq/2} F(q) is a
4-point local average (offsets +-1/2, +-3/2) that moves a site operator to the half-integer position; it is periodic and
C^infinity.  Diagonal T^{ii} sits at e_i (integer shift): local already, unchanged.
Everything else (R0/R1/R2, pieces C/A/B, glue, fibre identification, dsym, SIGN) is lib1916/lib199's, unmodified."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib1916 as R16
L = R16.L
from r99_profiles import wrap

def Fplace(q):
    q = np.asarray(q, float)
    return (9.0*np.cos(0.5*q) - np.cos(1.5*q))/8.0

_VW_ORIG = L.spatial_VW

def spatial_VW_placed(k1, k2, a=L.A_R, wd=L.WD_R, wo=L.WO_R):
    M = _VW_ORIG(k1, k2, a, wd, wo)
    f = Fplace(wrap(k1 - k2))
    for i in range(3):
        for j in range(3):
            if i != j:
                M[i, j] = M[i, j]*f[i]*f[j]
    return M

def patch():
    L.spatial_VW = spatial_VW_placed
def unpatch():
    L.spatial_VW = _VW_ORIG

# ---- placement bookkeeping used by the checks ------------------------------------------------------------------------
# p_{mu nu} = (e_mu + e_nu)/2, e_0 = 0  (R9-9's 09-14 placement; lib199.py:7-8).  Twice the l-th component:
def two_p(mu, nu, l):
    return int(mu == l + 1) + int(nu == l + 1)

def cut_sign(l):
    """(4,4) array: the factor (-1)^{2 p_l} by which the tilde kernel (graviton representative q = wrap(k1 - k2)) of ANY
    local stress at R9-9's placement must change when q_l crosses +-pi with k1, k2 fixed in the zone interior."""
    s = np.ones((4, 4))
    for mu in range(4):
        for nu in range(4):
            s[mu, nu] = (-1.0)**two_p(mu, nu, l)
    return s

def face_T(l):
    """rotated-frame face twist T_l on the 6 field components (lib199 / R19-9 r199_fiber_check.py)."""
    T = np.ones(6); T[l] = -1; T[3:] = -1; T[3 + l] = 1
    return T

def vertex_geo_F_factory(V0):
    """R18-13 vwface.vertex_geo (pair convention, s = k1 + k2) with the re-placement F(q_i)F(q_j), q = wrap(s), on every
    off-diagonal (i, j) pair; vertex_geo is linear in e (same wrapper as r1926_rows.py)."""
    def vertex_geo_F(e, c1, c2, s, a, wd=0.0, wo=0.0):
        ME, MB = V0(np.diag(np.diag(e)), c1, c2, s, a, wd, wo)
        f = Fplace(wrap(s))
        for i in range(3):
            for j in range(i + 1, 3):
                if e[i, j] == 0 and e[j, i] == 0: continue
                eij = np.zeros((3, 3)); eij[i, j] = e[i, j]; eij[j, i] = e[j, i]
                Mo, Bo = V0(eij, c1, c2, s, a, wd, wo); fac = (f[..., i]*f[..., j])[..., None, None]
                ME = ME + fac*Mo; MB = MB + fac*Bo
        return ME, MB
    return vertex_geo_F
