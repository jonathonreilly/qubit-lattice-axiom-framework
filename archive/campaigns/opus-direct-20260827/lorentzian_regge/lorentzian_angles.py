"""
Lorentzian Regge calculus: complex dihedral angles with explicit light-cone
bookkeeping (Sorkin's prescription), implemented as a single uniform
analytic continuation of the Euclidean angle.

DERIVATION (the thing the three failed attempts were missing)
------------------------------------------------------------
For a hinge h = triangle(a,b,c) inside a 4-simplex whose two remaining
vertices are d,e:

  P     = span(b-a, c-a)                      (the hinge 2-plane)
  Pperp = Minkowski-orthogonal complement of P
  D, E  = orthogonal projections of (d-a),(e-a) onto Pperp

The orthogonal projection of the whole simplex onto Pperp is the triangle
conv(0,D,E), so the "wedge" the simplex occupies around the hinge is exactly
the convex cone cone(D,E).  The wedges of the simplices around a hinge tile
Pperp.  That is true in either signature; only the meaning of "angle" changes.

Case A -- Pperp positive definite ("Euclidean-orthogonal" hinge; the hinge
itself is timelike).  Ordinary angle, wedges tile the circle, sum = 2*pi.

Case B -- Pperp Lorentzian ("Lorentzian-orthogonal" hinge; the hinge itself is
spacelike).  Pick an eta-orthonormal frame (T,X) of Pperp, <T,T>=-1,<X,X>=+1,
and write vectors as (t,x).  Parametrise directions by a COMPLEX angle phi via

      u(phi) = ( i*sin(phi),  cos(phi) )        in (t,x) components

This satisfies <u,u> = sin^2+cos^2 = 1 and, crucially,

      < u(phi1), u(phi2) > = cos(phi2 - phi1)

exactly as in Euclidean signature.  So phi IS the analytic continuation of the
Euclidean angle.  Real directions sit on a zig-zag contour in the complex
phi-plane, one vertical line per light-cone sector:

  k=0  right  (x>|t|)   D = |D|( sinh q,  cosh q)     phi = 0     - i q
  k=1  future (t>|x|)   D = |D|( cosh q,  sinh q)     phi = pi/2  - i q
  k=2  left  (-x>|t|)   D = |D|(-sinh q, -cosh q)     phi = pi    - i q
  k=3  past  (-t>|x|)   D = |D|(-cosh q, -sinh q)     phi = 3pi/2 - i q

with |D| = sqrt(|<D,D>|).  q is the rapidity.  Going counter-clockwise
(right -> future -> left -> past) the real part of phi increases by pi/2 per
light-cone crossing, while Im(phi) = -q runs to -inf and comes back from -inf
on the next line, so DIFFERENCES stay finite:

  wedge angle  dphi = (dk)*pi/2 - i*(q_E - q_D),      dk = (k_E-k_D) mod 4

The two divergences cancel because the same rapidity normalisation is used on
both sides of the light ray.  (Attempt 3 failed precisely here: it tried to
telescope real rapidities, which diverge at the cone.)

Orientation: the wedge is the convex cone, i.e. the pair (D,E) ordered so that
the 2-form D^E is positive in the chosen frame.  A convex cone spans at most a
half plane, so dk in {0,1,2}.  Flipping the frame's handedness maps
k -> (2-k) mod 4 and q -> -q and swaps the ordering, leaving dphi invariant --
so dphi is intrinsic, independent of frame and of the simplex's time
orientation.

Flat-space totals.  Around any hinge the wedges tile Pperp, so the phi's
telescope around a closed loop:

      sum_wedges dphi = 2*pi      (BOTH hinge classes)

because Re increases by 4*(pi/2)=2pi (four light-cone crossings) and the
imaginary parts cancel exactly.  Hence one single deficit formula:

      delta = 2*pi - sum_wedges dphi                for every hinge

Sorkin's normalisation (real boosts, -i*pi/2 per light-cone crossing) is
theta_Sorkin = -i*dphi; then sum(theta) = -2*pi*i, i.e. the boost parts sum to
0 and there are exactly 4 crossings each worth -i*pi/2.  Same content.

Areas use the matching branch sqrt(z - i0):  A = (1/2)*sqrt(det Gram_P), real
for a spacelike hinge and -i*(1/2)*sqrt(|det|) for a timelike one.
"""

import itertools
import math
from collections import defaultdict

import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def ip(u, v):
    """Minkowski inner product with signature (-,+,+,+)."""
    return float(u[0] * v[0] * -1.0 + u[1] * v[1] + u[2] * v[2] + u[3] * v[3])


def gram(vs):
    n = len(vs)
    G = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            G[i, j] = ip(vs[i], vs[j])
    return G


def sqrt_mi0(z):
    """sqrt with the -i0 branch: sqrt(negative) = -i*sqrt(|.|)."""
    if z >= 0.0:
        return complex(math.sqrt(z), 0.0)
    return complex(0.0, -math.sqrt(-z))


# --------------------------------------------------------------------------
# hinge frame
# --------------------------------------------------------------------------

class HingeFrame:
    """Minkowski-orthogonal 2-plane of a hinge, with an eta-orthonormal frame.

    kind = 'E'  Pperp positive definite  (hinge timelike)  -> ordinary angles
    kind = 'L'  Pperp Lorentzian         (hinge spacelike) -> boost angles
    kind = 'N'  Pperp degenerate (null hinge plane)        -> angle undefined
    """

    def __init__(self, p1, p2, tol=1e-10):
        # Pperp = null space of the 2x4 matrix rows p_i^T eta
        M = np.vstack([p1 @ ETA, p2 @ ETA])
        _, sv, Vt = np.linalg.svd(M)
        if sv[1] <= tol * max(sv[0], 1.0):
            self.kind = "N"          # hinge edges dependent: not a triangle
            return
        N = Vt[2:, :]                # 2x4, Euclidean-orthonormal rows
        Gp = np.array([[ip(N[i], N[j]) for j in range(2)] for i in range(2)])
        w, Q = np.linalg.eigh(Gp)
        scale = max(abs(w[0]), abs(w[1]), 1e-300)
        if abs(w[0]) <= tol * scale or abs(w[1]) <= tol * scale:
            self.kind = "N"          # null 2-plane: dihedral angle undefined
            self.detGperp = float(w[0] * w[1])
            return
        # basis vectors of Pperp diagonalising the induced metric
        f = Q.T @ N                  # rows f[k] with <f[k],f[l]> = w[k] delta
        if w[0] < 0.0 < w[1]:
            self.kind = "L"
            self.T = f[0] / math.sqrt(-w[0])   # <T,T> = -1
            self.X = f[1] / math.sqrt(w[1])    # <X,X> = +1
        elif w[0] > 0.0 and w[1] > 0.0:
            self.kind = "E"
            self.U = f[0] / math.sqrt(w[0])
            self.V = f[1] / math.sqrt(w[1])
        else:
            # both negative is impossible in signature (-,+,+,+)
            raise RuntimeError("impossible Pperp signature %r" % (w,))
        self.N = N
        self.Gp = Gp
        self.Gpinv = np.linalg.inv(Gp)
        self.detGperp = float(w[0] * w[1])

    def project(self, w):
        """Orthogonal projection of w onto Pperp, in Pperp components."""
        rhs = np.array([ip(self.N[0], w), ip(self.N[1], w)])
        a = self.Gpinv @ rhs
        return a @ self.N


# --------------------------------------------------------------------------
# the complex angle of one wedge
# --------------------------------------------------------------------------

def _sector_and_rapidity(t, x, tol):
    """Return (k, q) with phi = k*pi/2 - i*q, or (None,None) if null."""
    q2 = x * x - t * t
    scale = max(t * t, x * x)
    if abs(q2) <= tol * scale:
        return None, None            # direction on the light cone
    if q2 > 0.0:                     # spacelike
        m = math.sqrt(q2)
        if x > 0.0:
            return 0, math.asinh(t / m)
        return 2, math.asinh(-t / m)
    m = math.sqrt(-q2)               # timelike
    if t > 0.0:
        return 1, math.asinh(x / m)
    return 3, math.asinh(-x / m)


def wedge_angle(frame, D, E, tol=1e-11):
    """Complex angle of the convex cone(D,E) in the hinge's orthogonal plane.

    Returns (dphi, crossings) where dphi is the analytic continuation of the
    Euclidean dihedral angle and crossings = number of light-cone crossings
    (always 0 for a Euclidean-orthogonal hinge).
    Raises ValueError on a null bounding ray.
    """
    if frame.kind == "E":
        dd, ee, de = ip(D, D), ip(E, E), ip(D, E)
        if dd <= 0.0 or ee <= 0.0:
            raise ValueError("non-spacelike ray in a definite plane")
        c = de / math.sqrt(dd * ee)
        return complex(math.acos(min(1.0, max(-1.0, c))), 0.0), 0

    tD, xD = -ip(D, frame.T), ip(D, frame.X)
    tE, xE = -ip(E, frame.T), ip(E, frame.X)

    kD, qD = _sector_and_rapidity(tD, xD, tol)
    kE, qE = _sector_and_rapidity(tE, xE, tol)
    if kD is None or kE is None:
        raise ValueError("null bounding ray: wedge angle diverges")

    # orient: the convex cone runs counter-clockwise from the first to the
    # second vector, i.e. the ordered pair must satisfy D^E > 0.
    if xD * tE - tD * xE < 0.0:
        kD, qD, kE, qE = kE, qE, kD, qD

    dk = (kE - kD) % 4
    if dk == 3:
        raise ValueError("non-convex wedge (dk=3)")
    return complex(dk * math.pi / 2.0, -(qE - qD)), dk


def check_wedge_branch(frame, D, E, dphi):
    """Fully independent verification of the complex angle.

    With D = c_D u(phi_D), E = c_E u(phi_E) and c = sqrt(<.,.> - i0):

        cos(dphi) =    <D,E> / (c_D c_E)          (metric)
        sin(dphi) = -i (D^E) / (c_D c_E)          (orientation 2-form)

    Checking BOTH pins dphi uniquely mod 2*pi -- any error in the light-cone
    crossing count dk or in the sign of a rapidity shows up immediately.
    Returns max(|cos error|, |sin error|).
    """
    if frame.kind != "E":
        # use the same convex ordering wedge_angle used
        tD, xD = -ip(D, frame.T), ip(D, frame.X)
        tE, xE = -ip(E, frame.T), ip(E, frame.X)
        if xD * tE - tD * xE < 0.0:
            D, E = E, D
    cD, cE = sqrt_mi0(ip(D, D)), sqrt_mi0(ip(E, E))
    den = cD * cE
    ecos = abs(np.cos(dphi) - ip(D, E) / den)
    if frame.kind == "E":
        return ecos
    tD, xD = -ip(D, frame.T), ip(D, frame.X)
    tE, xE = -ip(E, frame.T), ip(E, frame.X)
    wedge2 = xD * tE - tD * xE                   # D ^ E in the (X,T) frame
    esin = abs(np.sin(dphi) + 1j * wedge2 / den)
    return max(ecos, esin)


# --------------------------------------------------------------------------
# simplex-level quantities
# --------------------------------------------------------------------------

def hinge_area(pa, pb, pc):
    """Complex triangle area, branch sqrt(z - i0)."""
    G = gram([pb - pa, pc - pa])
    return 0.5 * sqrt_mi0(float(np.linalg.det(G)))


def simplex_wedge(P, hinge, others):
    """(frame, dphi, crossings) for one hinge of one 4-simplex.

    P      : dict/list giving the 4-vector of each vertex
    hinge  : (a,b,c) vertex keys, in a FIXED order shared by all simplices
    others : (d,e) the remaining two vertex keys
    """
    a, b, c = hinge
    d, e = others
    fr = HingeFrame(P[b] - P[a], P[c] - P[a])
    if fr.kind == "N":
        return fr, None, None
    D = fr.project(P[d] - P[a])
    E = fr.project(P[e] - P[a])
    dphi, cr = wedge_angle(fr, D, E)
    return fr, dphi, cr
