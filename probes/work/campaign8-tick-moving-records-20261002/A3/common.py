"""Shared helpers for the lane-M moving-record toys (supplied models only).

Conventions
-----------
* One-excitation sector: state psi has shape (N*d,), index x*d + s (site x, internal s).
* Born odds of the record site: P(x) = sum_s |psi[x,s]|^2.
* A coupling pi[x, y] >= 0 has row sums P_t and column sums P_{t+1};
  the move rule is T[x, y] = pi[x, y] / P_t[x].
* Margenau-Hill (MH) split of one tick psi' = U psi:
      K[x, y]  = <psi'| Pi_y U Pi_x |psi>          (complex)
      pi_MH    = Re K   (row sums P_t, column sums P_{t+1}, exactly)
      J_MH     = pi_MH - pi_MH^T   (net flow, antisymmetric)
"""
import numpy as np
from scipy.optimize import linprog
from scipy.stats import chi2


def haar_unitary(n, rng):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    ph = np.diag(r) / np.abs(np.diag(r))
    return q * ph


def rand_state(n, rng):
    v = rng.normal(size=n) + 1j * rng.normal(size=n)
    return v / np.linalg.norm(v)


def ring_allowed(N):
    """Boolean N x N: True iff cyclic distance <= 1."""
    a = np.zeros((N, N), dtype=bool)
    for x in range(N):
        for dx in (-1, 0, 1):
            a[x, (x + dx) % N] = True
    return a


def site_probs(psi, N, d):
    return (np.abs(psi.reshape(N, d)) ** 2).sum(axis=1)


def mh_split(U, psi, N, d):
    """Return (pi_MH, K, psi_next) for one tick psi_next = U psi."""
    psin = U @ psi
    Ub = U.reshape(N, d, N, d)          # Ub[y, s, x, t] = <y s|U|x t>
    ps = psi.reshape(N, d)
    pn = psin.reshape(N, d)
    K = np.einsum('ys,ysxt,xt->xy', pn.conj(), Ub, ps)
    return K.real.copy(), K, psin


def rule_from_flow(J, P, tol=1e-14):
    """Minimal (no-counterflow) rule T = J^+/P.  Returns (T, max outflow excess)."""
    N = len(P)
    Jp = np.maximum(J, 0.0)
    np.fill_diagonal(Jp, 0.0)
    out = Jp.sum(axis=1)
    excess = float(np.max(out - P))
    T = np.zeros((N, N))
    for x in range(N):
        if P[x] > tol:
            T[x] = Jp[x] / P[x]
            T[x, x] = 1.0 - T[x].sum()
        else:
            T[x, x] = 1.0
    return T, excess


def rule_from_coupling(pi, P, tol=1e-14):
    N = len(P)
    T = np.zeros((N, N))
    for x in range(N):
        if P[x] > tol:
            T[x] = pi[x] / P[x]
        else:
            T[x, x] = 1.0
    return T


def tv(p, q):
    return 0.5 * float(np.abs(p - q).sum())


def _marginal_constraints(n_from, n_to, pairs):
    """Equality constraints for a coupling on the listed (x, y) pairs (drop one redundant row)."""
    m = len(pairs)
    A = np.zeros((n_from + n_to - 1, m))
    for k, (x, y) in enumerate(pairs):
        A[x, k] = 1.0
        if y < n_to - 1:
            A[n_from + y, k] = 1.0
    return A


def lp_coupling(P, Q, allowed, objective='moves'):
    """Coupling of P -> Q supported on `allowed` (bool matrix).

    objective='moves'  : minimise total off-diagonal mass (L1-minimal rule)
    objective='zero'   : pure feasibility
    Returns (status_ok, pi or None, objective value).
    """
    nf, nt = allowed.shape
    pairs = [(x, y) for x in range(nf) for y in range(nt) if allowed[x, y]]
    A = _marginal_constraints(nf, nt, pairs)
    b = np.concatenate([P, Q[:-1]])
    if objective == 'moves':
        c = np.array([0.0 if x == y else 1.0 for (x, y) in pairs])
    else:
        c = np.zeros(len(pairs))
    res = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method='highs')
    if res.status != 0:
        return False, None, None
    pi = np.zeros((nf, nt))
    for k, (x, y) in enumerate(pairs):
        pi[x, y] = res.x[k]
    return True, pi, res.fun


def min_long_jump(P, Q, allowed):
    """Least mass that must use a non-allowed pair in any coupling P -> Q."""
    n = len(P)
    pairs = [(x, y) for x in range(n) for y in range(n)]
    A = _marginal_constraints(n, n, pairs)
    b = np.concatenate([P, Q[:-1]])
    c = np.array([0.0 if allowed[x, y] else 1.0 for (x, y) in pairs])
    res = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method='highs')
    return float(res.fun)


def lp_circulation_range(P, Q, allowed, bond_from, bond_to):
    """Min and max net flow across one bond over all couplings (ring circulation interval)."""
    nf, nt = allowed.shape
    pairs = [(x, y) for x in range(nf) for y in range(nt) if allowed[x, y]]
    A = _marginal_constraints(nf, nt, pairs)
    b = np.concatenate([P, Q[:-1]])
    c = np.zeros(len(pairs))
    for k, (x, y) in enumerate(pairs):
        if (x, y) == (bond_from, bond_to):
            c[k] = 1.0
        elif (x, y) == (bond_to, bond_from):
            c[k] = -1.0
    lo = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method='highs')
    hi = linprog(-c, A_eq=A, b_eq=b, bounds=(0, None), method='highs')
    return float(lo.fun), float(-hi.fun)


def mc_trajectories(T_list, X0, rng):
    """Sample M independent record trajectories; return list of histograms per tick."""
    n = T_list[0].shape[0]
    X = X0.copy()
    hists = [np.bincount(X, minlength=n)]
    for T in T_list:
        cum = np.cumsum(T, axis=1)
        cum[:, -1] = 1.0 + 1e-9
        u = rng.random(len(X))
        X = (u[:, None] >= cum[X]).sum(axis=1)
        hists.append(np.bincount(X, minlength=n))
    return hists


def chi2_check(hist, P, M):
    """Pearson chi^2 with cells of expected count < 5 pooled; returns (stat, dof, p)."""
    E = M * P
    big = E >= 5
    obs = list(hist[big])
    exp = list(E[big])
    if (~big).any():
        obs.append(hist[~big].sum())
        exp.append(E[~big].sum())
    obs = np.array(obs, float)
    exp = np.array(exp, float)
    keep = exp > 0
    obs, exp = obs[keep], exp[keep]
    if len(obs) < 2:
        return 0.0, 0, 1.0
    stat = float(((obs - exp) ** 2 / exp).sum())
    dof = len(obs) - 1
    return stat, dof, float(chi2.sf(stat, dof))
