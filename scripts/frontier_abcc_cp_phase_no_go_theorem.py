"""Finite chart/pairing comparison with supplied historical cuts; inertia does not determine CP sign."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300

import math
import itertools

import numpy as np
from scipy.optimize import fsolve, minimize

np.set_printoptions(precision=6, suppress=True, linewidth=120)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition



GAMMA = 0.5
E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0

T_M = np.array([[1,0,0],[0,0,1],[0,1,0]], dtype=complex)
T_DELTA = np.array([[0,-1,1],[-1,1,0],[1,0,-1]], dtype=complex)
T_Q = np.array([[0,1,1],[1,0,1],[1,1,0]], dtype=complex)
H_BASE = np.array([
    [0, E1, -E1-1j*GAMMA],
    [E1, 0, -E2],
    [-E1+1j*GAMMA, -E2, 0],
], dtype=complex)

PHYSICAL_SIGMA = (2, 1, 0)

BASIN_X_NATIVE_SIGMA = (2, 0, 1)

TARGET_S12SQ = 0.307
TARGET_S13SQ = 0.0218
TARGET_S23SQ = 0.545

T2K_3SIGMA_SIN_BOUND = 0.247  # Supplied historical numerical cut; no confidence-level claim is tested here.

PDG_LO = np.array([[0.801,0.513,0.143],[0.234,0.471,0.637],[0.271,0.477,0.613]])
PDG_HI = np.array([[0.845,0.579,0.155],[0.500,0.689,0.776],[0.525,0.694,0.756]])


def H_mat(m, d, q):
    return H_BASE + m*T_M + d*T_DELTA + q*T_Q


def pmns_obs(m, d, q, perm=PHYSICAL_SIGMA):
    Hm = H_mat(m, d, q)
    w, V = np.linalg.eigh(Hm)
    order = np.argsort(np.real(w))
    w = np.real(w[order]); V = V[:, order]
    P = V[list(perm), :]
    s13sq = abs(P[0,2])**2; c13sq = max(1-s13sq, 1e-18)
    s12sq = abs(P[0,1])**2/c13sq; s23sq = abs(P[1,2])**2/c13sq
    s12=math.sqrt(max(s12sq,0)); c12=math.sqrt(max(1-s12sq,0))
    s13=math.sqrt(max(s13sq,0)); c13=math.sqrt(max(c13sq,0))
    s23=math.sqrt(max(s23sq,0)); c23=math.sqrt(max(1-s23sq,0))
    J = (P[0,0]*P[0,1].conjugate()*P[1,0].conjugate()*P[1,1]).imag
    denom = s12*c12*s23*c23*s13*c13*c13
    sin_dcp = float(max(-1, min(1, J/denom))) if denom > 1e-18 else 0.0
    det_H = float(np.linalg.det(Hm).real)
    chi2 = (s12sq-TARGET_S12SQ)**2 + (s13sq-TARGET_S13SQ)**2 + (s23sq-TARGET_S23SQ)**2
    n_pass = int(np.sum((np.abs(P) >= PDG_LO) & (np.abs(P) <= PDG_HI)))
    return {"s12sq": s12sq, "s13sq": s13sq, "s23sq": s23sq,
            "sin_dcp": sin_dcp, "det_H": det_H, "chi2": chi2,
            "n_pass": n_pass, "eigvals": w, "P": P}


def find_basin(x0, perm=PHYSICAL_SIGMA):
    def f_eq(x):
        obs = pmns_obs(*x, perm=perm)
        return [obs["s12sq"]-TARGET_S12SQ, obs["s13sq"]-TARGET_S13SQ,
                obs["s23sq"]-TARGET_S23SQ]
    def f_chi2(x):
        return pmns_obs(*x, perm=perm)["chi2"]
    res = minimize(f_chi2, x0, method="Nelder-Mead",
                   options=dict(xatol=1e-8, fatol=1e-14, maxiter=50000))
    if res.fun > 1e-6:
        return np.array(x0)
    sol = fsolve(f_eq, res.x, full_output=True, xtol=1e-14)
    return sol[0]


def all_sigma_sin_dcp(m, d, q):
    """Return {sigma: sin(delta_CP)} for all 6 S_3 permutations."""
    Hm = H_mat(m, d, q)
    w, V = np.linalg.eigh(Hm)
    order = np.argsort(np.real(w)); V = V[:, order]
    result = {}
    for perm in itertools.permutations([0,1,2]):
        P = V[list(perm), :]
        s13sq = abs(P[0,2])**2; c13sq = max(1-s13sq, 1e-18)
        s12sq = abs(P[0,1])**2/c13sq; s23sq = abs(P[1,2])**2/c13sq
        s12=math.sqrt(max(s12sq,0)); c12=math.sqrt(max(1-s12sq,0))
        s13=math.sqrt(max(s13sq,0)); c13=math.sqrt(max(c13sq,0))
        s23=math.sqrt(max(s23sq,0)); c23=math.sqrt(max(1-s23sq,0))
        J = (P[0,0]*P[0,1].conjugate()*P[1,0].conjugate()*P[1,1]).imag
        denom = s12*c12*s23*c23*s13*c13*c13
        sin_dcp = float(max(-1, min(1, J/denom))) if denom > 1e-18 else 0.0
        n_pass = int(np.sum((np.abs(P) >= PDG_LO) & (np.abs(P) <= PDG_HI)))
        result[perm] = (sin_dcp, n_pass)
    return result






























def main() -> int:
    print('Pairing (2,1,0), angle targets, magnitude bands and 0.247 cut are supplied historical comparators, not revalidated experimental bounds.')
    obs1=pmns_obs(.657061,.933806,.715042)
    x2=find_basin([28.,21.,5.]);obs2=pmns_obs(*x2)
    xx=find_basin([21.,13.,2.],perm=BASIN_X_NATIVE_SIGMA)
    obsx=pmns_obs(*xx);native=pmns_obs(*xx,perm=BASIN_X_NATIVE_SIGMA)
    check('Pinned angle residual below original tolerance',obs1['chi2']<1e-10)
    check('Basin-2 fitted angle residual below original tolerance',obs2['chi2']<1e-8)
    check('Basin-X native-pairing residual below original tolerance',native['chi2']<1e-8)
    check('Pinned sine is negative',obs1['sin_dcp']<-.9)
    check('Both displayed negative-determinant candidates exceed supplied sine cut',obs2['sin_dcp']>T2K_3SIGMA_SIN_BOUND and obsx['sin_dcp']>T2K_3SIGMA_SIN_BOUND and obs2['det_H']<0 and obsx['det_H']<0)
    H=H_mat(.657061,.933806,.715042)
    vals,V=np.linalg.eigh(H);vals_c,Vc=np.linalg.eigh(H.conjugate())
    def j(A):
        P=A[list(PHYSICAL_SIGMA),:]
        return float((P[0,0]*P[0,1].conjugate()*P[1,0].conjugate()*P[1,1]).imag)
    check('Conjugation keeps spectrum/inertia and reverses nonzero J',np.max(abs(vals-vals_c))<1e-12 and abs(j(V)+j(Vc))<1e-12 and abs(j(V))>1e-6)
    for name,obs in [('pin',obs1),('Basin 2',obs2),('Basin X under supplied pairing',obsx)]:print(name,obs['sin_dcp'],obs['det_H'])
    print('Conjugate control is for Hermitian matrices generally; fixed positive-gamma chart membership is not claimed.')
    print('No all-basin exclusion, observational confidence level, or framework falsification follows.')
    print("per_element: supplied matrix entries and eigenvector quartet checked; no entrywise physical selection rule derived.")
    print("per_site: not executed; no spatial sites or site-dependent dynamics are represented in this finite chart comparison.")
    print("per_mode: not executed; no physical mode decomposition or mode-dependent CP selector is constructed.")
    print("per_block: the supplied three-dimensional pin, two fitted candidates and conjugate matrix are checked; no exhaustive block family certified.")
    print("lattice_wide: not executed; no lattice limit, all-basin exclusion or physical source-selection theorem is established.")
    print(f'PASS={PASS_COUNT} FAIL={FAIL_COUNT}')
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
