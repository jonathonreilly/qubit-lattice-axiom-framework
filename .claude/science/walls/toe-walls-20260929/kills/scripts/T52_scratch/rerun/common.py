"""Shared helpers for the T52 attack (copies chart constants from the repo; repo untouched)."""
import math, numpy as np

# ---- repo-quoted 3-sigma comparators (PMNS_DCP_FORECAST_..._NUFIT6 note, 2026-06-08)
BOX61 = {"s12": (0.2893, 0.3295), "s13": (0.02070, 0.02418), "s23": (0.435, 0.584)}   # intersection of no-SK / with-SK
BOX53 = {"s12": (0.275, 0.345), "s13": (0.02029, 0.02391), "s23": (0.430, 0.596)}    # lane runner NuFit 5.3 3 sigma
def inbox(a, B):  # a = (s12, s13, s23)
    return all(B[k][0] <= v <= B[k][1] for k, v in zip(("s12", "s13", "s23"), a))

# ---- corner-basis objects on the hw=1 triplet
W  = np.ones(3) / math.sqrt(3)
XI = np.array([2., -1., -1.]) / math.sqrt(6)
ETA = np.array([0., 1., -1.]) / math.sqrt(2)
I3 = np.eye(3)
S   = 2 * np.outer(W, W) - I3                 # magic reflection
P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], float)
SP  = S @ P23
assert np.allclose(SP, P23 @ S)

def observables(U):
    """(s12^2, s13^2, s23^2, sin d, cos d) from a unitary with rows (e,mu,tau), cols (nu1,nu2,nu3)."""
    a = np.abs(U) ** 2
    s13 = a[0, 2]; c13 = 1 - s13
    s12 = a[0, 1] / c13; s23 = a[1, 2] / c13
    c12 = 1 - s12; c23 = 1 - s23
    J = (U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])).imag
    den = math.sqrt(max(s12 * c12 * s23 * c23, 0)) * c13 * math.sqrt(max(s13, 0))
    sd = J / den if den > 1e-15 else float("nan")
    # cos d from |U_tau1|^2 = s12 s23 + c12 s13 c23 - 2 sqrt(s12 c12 s23 c23) sqrt(s13) c13^(1/2)... (standard param)
    # exact: |U_tau1|^2 = s12^2 s23^2 + c12^2 c23^2 s13^2 - 2 s12 c12 s23 c23 s13 cos d (angles, not squares)
    s12a, c12a = math.sqrt(s12), math.sqrt(c12)
    s23a, c23a = math.sqrt(s23), math.sqrt(c23)
    s13a = math.sqrt(s13)
    num = s12 * s23 + c12 * c23 * s13 - a[2, 0]
    cd = num / (2 * s12a * c12a * s23a * c23a * s13a) if s13a > 1e-15 else float("nan")
    return s12, s13, s23, sd, cd

def order_by_electron_content(w, V):
    """Assign columns (nu1,nu2,nu3) by decreasing |U_e|^2 (the lane's sigma_hier premise, electron = row 0)."""
    o = np.argsort(-np.abs(V[0, :]) ** 2)
    return w[o], V[:, o]
