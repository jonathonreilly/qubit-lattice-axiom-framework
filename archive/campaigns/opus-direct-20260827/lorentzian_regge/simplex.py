"""Single 4-simplex: reconstruction from squared edge lengths, areas, angles."""
import itertools
import math

import numpy as np

from lorentzian_angles import HingeFrame, wedge_angle, sqrt_mi0, ip, gram

EDGES = list(itertools.combinations(range(5), 2))          # 10
TRIS = list(itertools.combinations(range(5), 3))           # 10


def embed(s2):
    """s2: dict (i,j)->squared length. Return 5 Minkowski coordinates.
    Raises ValueError unless the signature is (-,+,+,+)."""
    def s(i, j):
        return 0.0 if i == j else s2[(min(i, j), max(i, j))]
    G = np.array([[0.5 * (s(0, i) + s(0, j) - s(i, j)) for j in range(1, 5)]
                  for i in range(1, 5)])
    w, V = np.linalg.eigh(G)
    if not (w[0] < 0 < w[1]):
        raise ValueError("not a Lorentzian 4-simplex: eigenvalues %s" % w)
    C = V * np.sqrt(np.abs(w))          # columns scaled; row i = vertex i+1
    P = [np.zeros(4)] + [C[i, :].copy() for i in range(4)]
    return P


def volume2(s2):
    """Cayley-Menger squared 4-volume (negative for a Lorentzian simplex)."""
    n = 5
    M = np.ones((n + 1, n + 1))
    M[0, 0] = 0.0
    for i in range(n):
        for j in range(n):
            M[i + 1, j + 1] = 0.0 if i == j else s2[(min(i, j), max(i, j))]
    # V^2 = (-1)^(n+1) det(CM) / (2^n (n!)^2)  with n = 4
    return -np.linalg.det(M) / (2.0 ** 4 * math.factorial(4) ** 2)


def areas_and_angles(s2):
    """For each of the 10 triangles: (complex area, complex dihedral angle)."""
    P = embed(s2)
    out = {}
    for tri in TRIS:
        a, b, c = tri
        d, e = [v for v in range(5) if v not in tri]
        A = 0.5 * sqrt_mi0(float(np.linalg.det(gram([P[b] - P[a], P[c] - P[a]]))))
        fr = HingeFrame(P[b] - P[a], P[c] - P[a])
        if fr.kind == "N":
            raise ValueError("degenerate hinge %s" % (tri,))
        D, E = fr.project(P[d] - P[a]), fr.project(P[e] - P[a])
        th, _ = wedge_angle(fr, D, E)
        out[tri] = (A, th, fr.kind)
    return out


def random_lorentzian_simplex(rng, spread=1.0, tries=200):
    """Random 5 points in Minkowski R^{1,3} with a non-degenerate Lorentzian
    simplex and 10 non-degenerate hinges."""
    for _ in range(tries):
        P = rng.standard_normal((5, 4)) * spread
        s2 = {(i, j): ip(P[j] - P[i], P[j] - P[i]) for i, j in EDGES}
        try:
            aa = areas_and_angles(s2)
        except (ValueError, RuntimeError, np.linalg.LinAlgError):
            continue
        v2 = volume2(s2)
        sc = spread ** 8
        if not (v2 < -1e-3 * sc):        # comfortably non-degenerate, Lorentzian
            continue
        # require every hinge comfortably non-degenerate too
        ok = True
        for tri in TRIS:
            a, b, c = tri
            g = np.linalg.det(gram([P[b] - P[a], P[c] - P[a]]))
            if abs(g) < 1e-2 * spread ** 4:
                ok = False
                break
        if ok:
            return s2, P
    raise RuntimeError("failed to draw a good simplex")
