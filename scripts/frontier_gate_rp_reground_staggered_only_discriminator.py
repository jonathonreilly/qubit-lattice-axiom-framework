#!/usr/bin/env python3
"""Finite staggered determinant diagnostics; no reflection-positivity inference.
Includes zero singular values and a positive-weight counterexample to RP.
"""

from __future__ import annotations

import itertools

import numpy as np

AUDIT_TIMEOUT_SEC = 120

rng = np.random.default_rng(0)
TOL = 1.0e-9
PASS = 0
FAIL = 0
L = 4  # even periodic; avoids the L=2 forward/backward collision


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        st = "PASS"
    else:
        FAIL += 1
        st = "FAIL"
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return cond


def sites():
    return list(itertools.product(range(L), repeat=3))


def random_su3():
    a = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    q, r = np.linalg.qr(a)
    q = q @ np.diag(np.exp(-1j * np.angle(np.diag(r))))  # U(3)
    q = q / (np.linalg.det(q) ** (1 / 3))                # project to SU(3)
    return q


def eta(n, mu):
    # staggered phases: eta_x=1, eta_y=(-1)^x, eta_z=(-1)^{x+y}
    if mu == 0:
        return 1.0
    if mu == 1:
        return -1.0 if (n[0] % 2) else 1.0
    return -1.0 if ((n[0] + n[1]) % 2) else 1.0


def build_M_KS():
    S = sites()
    idx = {n: i for i, n in enumerate(S)}
    N = len(S)
    M = np.zeros((3 * N, 3 * N), dtype=complex)

    def blk(i, j, B):
        M[3 * i:3 * i + 3, 3 * j:3 * j + 3] += B

    for n in S:
        for mu in range(3):
            m = list(n); m[mu] = (m[mu] + 1) % L; m = tuple(m)
            U = random_su3()
            A = 0.5 * eta(n, mu) * U          # forward block n -> n+mu
            blk(idx[m], idx[n], A)
            blk(idx[n], idx[m], -A.conj().T)  # backward = -A^dagger  (anti-Hermitian)
    return M, idx, S


def epsilon(idx, S):
    N = len(S)
    e = np.zeros((3 * N, 3 * N), dtype=complex)
    for n in S:
        s = -1.0 if (sum(n) % 2) else 1.0
        i = idx[n]
        e[3 * i:3 * i + 3, 3 * i:3 * i + 3] = s * np.eye(3)
    return e


def main() -> int:
    print("=" * 76)
    print("STAGGERED DETERMINANT POSITIVITY; RP REMAINS SEPARATE")
    print("=" * 76)

    M, idx, S = build_M_KS()
    eps = epsilon(idx, S)
    m_mass = 0.7

    print("\n" + "-" * 76)
    print("Staggered M_KS structure (random SU(3) links, L=4)")
    print("-" * 76)
    check("M_KS is anti-Hermitian", np.linalg.norm(M + M.conj().T) < TOL,
          detail=f"||M+M^dag||={np.linalg.norm(M + M.conj().T):.1e}")
    check("eps is a Hermitian involution (eps^2 = I)",
          np.linalg.norm(eps @ eps - np.eye(eps.shape[0])) < TOL)
    check("{eps, M_KS} = 0 (staggered chirality grading)",
          np.linalg.norm(eps @ M + M @ eps) < TOL,
          detail=f"||{{eps,M}}||={np.linalg.norm(eps @ M + M @ eps):.1e}")

    print("\n" + "-" * 76)
    print("Case A: eigenvalues are +/- i sigma pairs; det(M+mI) = prod(m^2+sigma^2) > 0")
    print("-" * 76)
    ev = np.linalg.eigvals(M)
    check("all eigenvalues are pure imaginary", np.max(np.abs(ev.real)) < 1e-8,
          detail=f"max|Re|={np.max(np.abs(ev.real)):.1e}")
    sig = np.sort(ev.imag)
    # paired +/-: sorted should be antisymmetric
    check("eigenvalues come in +/- sigma pairs",
          np.allclose(sig, -sig[::-1], atol=1e-7))
    sign, logdet = np.linalg.slogdet(M + m_mass * np.eye(M.shape[0]))
    check("det(M_KS + mI) > 0", abs(sign-1)<1e-8, detail=f"sign={sign.real:+.0f}")
    # SVD includes zero singular values, which contribute m^2.
    parity=np.real(np.diag(eps))
    K=M[np.ix_(parity>0,parity<0)]
    singular=np.linalg.svd(K,compute_uv=False)
    logprod=np.log(m_mass**2+singular**2).sum()
    check("determinant SVD product including zero modes",abs(logdet-logprod)<1e-6)
    Kzero=np.diag([0.,2.])
    Mzero=np.block([[np.zeros((2,2)),Kzero],[-Kzero.T,np.zeros((2,2))]])
    check("zero-mode fixture contributes m squared",np.isclose(np.linalg.det(m_mass*np.eye(4)+Mzero),m_mass**2*(m_mass**2+4)))

    print("\n" + "-" * 76)
    print("Robustness: det > 0 for several random SU(3) configurations")
    print("-" * 76)
    allpos = True
    for t in range(5):
        M2, _, _ = build_M_KS()
        s2, _ = np.linalg.slogdet(M2 + m_mass * np.eye(M2.shape[0]))
        allpos = allpos and abs(s2-1)<1e-8
    check("det(M_KS + mI) > 0 for all 5 random SU(3) configs", allpos)

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    weights=np.array([[1.,2.],[2.,1.]])
    spins=np.array([-1.,1.])
    reflected_form=np.sum(weights*np.outer(spins,spins))/weights.sum()
    check("strictly positive reflection-invariant weights can fail RP",
          np.all(weights>0) and np.allclose(weights,weights.T) and np.isclose(reflected_form,-1/3),
          detail=f"<Theta F F>={reflected_form}")
    print("Determinant identities do not certify reflection positivity or gate closure.")
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
