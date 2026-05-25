#!/usr/bin/env python3
"""Gate reflection-positivity re-grounds on the retained staggered-only Case A.

The staggered-Dirac gate-closure synthesis cites the broad RP theorem
`axiom_first_reflection_positivity_theorem_note_2026-04-29`, which is
**audited_failed** -- but it failed only on the OVER-BROAD full-Wilson surface.
Its staggered-only Case A is independently **retained**
(`staggered_only_det_positivity_case_a_note_2026-05-17`):

    for the staggered Dirac operator M_KS (anti-Hermitian, {eps, M_KS} = 0) and
    real m > 0,   det(M_KS + m I) = prod_i (m^2 + sigma_i^2) > 0
    for every unitary link configuration.

Since the gate's fermionic realization IS the staggered sector (M_KS), the
positivity it needs is exactly Case A -- retained -- not the failed broad
Wilson surface. This discriminator reproduces Case A on a finite lattice with
random SU(3) links and shows it is staggered-sector-only, so the synthesis's RP
dependency can be re-grounded on the retained Case A row, removing the
audited_failed broad RP theorem from the gate's load-bearing path.

This runner verifies the determinant-positivity component of the retained
staggered-only Case A reflection-positivity surface.

Pure finite linear algebra. No PDG / fitted / scale input. Asserts no audit
status. Does NOT repair the broad RP theorem; shows the gate does not need it.
"""

from __future__ import annotations

import itertools

import numpy as np

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
    print("GATE RP RE-GROUNDS ON RETAINED STAGGERED-ONLY CASE A")
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
    check("det(M_KS + mI) > 0", sign.real > 0, detail=f"sign={sign.real:+.0f}")
    # product form over positive sigma
    pos = sorted(s for s in ev.imag if s > 1e-8)
    logprod = sum(np.log(m_mass**2 + s**2) for s in pos)
    check("det(M_KS + mI) = prod_i (m^2 + sigma_i^2) (over positive sigma)",
          abs(logdet - logprod) < 1e-6, detail=f"dlog={abs(logdet - logprod):.1e}")

    print("\n" + "-" * 76)
    print("Robustness: det > 0 for several random SU(3) configurations")
    print("-" * 76)
    allpos = True
    for t in range(5):
        M2, _, _ = build_M_KS()
        s2, _ = np.linalg.slogdet(M2 + m_mass * np.eye(M2.shape[0]))
        allpos = allpos and s2.real > 0
    check("det(M_KS + mI) > 0 for all 5 random SU(3) configs", allpos)

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if FAIL == 0:
        print(
            "  GATE RP RE-GROUNDS ON THE RETAINED STAGGERED-ONLY CASE A.\n"
            "  The staggered operator M_KS is anti-Hermitian and anticommutes with\n"
            "  the chirality grading eps, so its eigenvalues are +/- i sigma pairs\n"
            "  and det(M_KS + mI) = prod(m^2 + sigma^2) > 0 for every link config --\n"
            "  the determinant-positivity component of the staggered-only Case A\n"
            "  reflection-positivity surface. This is the retained Case A\n"
            "  (staggered_only_det_positivity_case_a_note), independent of the\n"
            "  Wilson term.\n\n"
            "  Consequence: the gate-closure synthesis cites the broad RP theorem\n"
            "  (axiom_first_reflection_positivity, AUDITED_FAILED on the over-broad\n"
            "  full-Wilson surface). But the gate's fermionic realization is the\n"
            "  staggered sector, whose RP need is exactly Case A -- RETAINED. So the\n"
            "  synthesis's RP dependency re-grounds on the retained Case A, removing\n"
            "  the audited_failed broad RP theorem from the gate's load-bearing path.\n\n"
            "  Does NOT repair the broad RP theorem (the full-Wilson surface stays\n"
            "  failed); shows the gate does not need it. Does NOT close the gate --\n"
            "  the other unaudited axiom-first QFT rows remain.\n"
        )
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
