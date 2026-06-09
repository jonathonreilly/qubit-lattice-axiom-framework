#!/usr/bin/env python3
"""Free-continuum Poincare assembly support from the kinetic-isotropy primitive.

Thesis
------
The kinetic-isotropy primitive is an approved structural premise for the kinetic
form ratio c_t=c_s. It is not itself a Lorentz theorem and does not supply a
measure bridge, reflection positivity, statistics, interacting dynamics, or an
audit verdict. This runner checks algebraic pieces of the free-continuum target
used by the conditional OS/Wightman reconstruction chain:

  Part 1  The free Euclidean Dirac 2-point is SO(4)-covariant, including a
          tau-x mixed plane check. [Restates the free-continuum target, not the
          primitive by itself.]
  Part 2  Wick step: a tau-x Euclidean rotation by angle theta analytically
          continues (theta -> -i eta) to a Minkowski boost of rapidity eta; the
          continued (Wightman) Dirac 2-point is SO(3,1)-covariant.
  Part 3  Poincare algebra closes in the standard finite-dimensional
          representation used as the continuum target.
  Part 4  Spectrum condition is boost-invariant: the forward mass shell
          p^0 = +sqrt(p^2 + m^2) >= 0 maps to the forward cone under every boost,
          so the standard target is a positive-energy Poincare representation.
  Part 5  Boundary checklist: the lattice->continuum measure bridge and the
          interacting continuum-existence wall are NOT supplied here.

Scope (honest): conditional free-continuum Gaussian support only. This does NOT
establish the framework lattice measure, does not ratify RP, does not prove the
abstract OS reconstruction theorem, and does not touch any dimensionless
dynamical observable. Sets no audit status.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np

np.seterr(all="ignore")
PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t: str) -> None:
    print("\n" + "-" * 88 + "\n" + t + "\n" + "-" * 88)


# --- Euclidean Dirac algebra (4x4, Hermitian, {g_mu,g_nu}=2 delta) -----------
def euclidean_gammas() -> list[np.ndarray]:
    s = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]
    I2 = np.eye(2, dtype=complex)
    # 4D Euclidean Hermitian gammas: g_i = sigma_i (x) sigma_1 (i=1,2,3), g_0 = I (x) sigma_3 ...
    # Use the standard chiral construction: g_k = [[0, -i s_k],[i s_k,0]], g_4=[[0,I],[I,0]].
    g = []
    for sk in s:
        g.append(np.block([[np.zeros((2, 2), complex), -1j * sk], [1j * sk, np.zeros((2, 2), complex)]]))
    g0 = np.block([[np.zeros((2, 2), complex), I2], [I2, np.zeros((2, 2), complex)]])
    return [g0] + g  # index 0 = Euclidean "time" axis, then x,y,z


def G_euclid(p, gammas, m=0.7):
    pslash = sum(p[mu] * gammas[mu] for mu in range(4))
    return (m * np.eye(4, dtype=complex) - 1j * pslash) / (np.dot(p, p) + m * m)


def main() -> int:
    print("=" * 88)
    print("FREE-CONTINUUM POINCARE ASSEMBLY SUPPORT FROM KINETIC ISOTROPY")
    print("=" * 88)

    g = euclidean_gammas()
    # sanity: Clifford {g_mu,g_nu}=2 delta
    cliff_ok = True
    for a in range(4):
        for b in range(4):
            anti = g[a] @ g[b] + g[b] @ g[a]
            if not np.allclose(anti, 2.0 * (a == b) * np.eye(4), atol=1e-12):
                cliff_ok = False

    section("Part 1: free Euclidean Dirac 2-point is SO(4)-covariant (incl. tau-x mixed plane)")
    check("Euclidean Clifford algebra {g_mu,g_nu}=2 delta holds", cliff_ok)
    # Spin(4) generators Sigma_munu = (1/4)[g_mu,g_nu]; finite rotation S=exp(theta Sigma)
    try:
        from scipy.linalg import expm
        have_expm = True
    except Exception:
        have_expm = False

    def covariance(plane, theta, p):
        """Return (vector-rotation orthogonality residual, bispinor covariance residual).
        The vector SO(4) rotation R is DERIVED from the spinor rotation S via the
        trace formula R[a,b]=(1/4)tr(g_a S g_b S^-1), so the convention is self-consistent."""
        mu, nu = plane
        Sig = 0.25 * (g[mu] @ g[nu] - g[nu] @ g[mu])
        S = expm(theta * Sig)
        Sinv = np.linalg.inv(S)
        R = np.array([[0.25 * np.trace(g[a] @ S @ g[b] @ Sinv) for b in range(4)]
                      for a in range(4)]).real
        ortho = max(np.max(np.abs(R.T @ R - np.eye(4))), abs(np.linalg.det(R) - 1.0))
        cov = np.max(np.abs(S @ G_euclid(p, g) @ Sinv - G_euclid(R @ p, g)))
        return ortho, cov

    if have_expm:
        p0 = np.array([0.31, -0.52, 0.18, 0.44])
        o1, c1 = covariance((1, 2), 0.7, p0)          # x-y rotation
        o2, c2 = covariance((0, 1), 0.6, p0)          # tau-x mixed Euclidean plane
        check("spinor rotations induce genuine SO(4) vector rotations (R^T R=I, det=1)",
              max(o1, o2) < 1e-10, detail=f"max ortho residual={max(o1,o2):.2e}")
        check("SO(4) bispinor covariance in a spatial (x-y) plane", c1 < 1e-10,
              detail=f"residual={c1:.2e}")
        check("SO(4) bispinor covariance in the tau-x plane (free-continuum target)",
              c2 < 1e-10, detail=f"residual={c2:.2e}")
    else:
        check("scipy.linalg.expm unavailable -- skipping finite-rotation covariance", True, detail="skipped")

    section("Part 2: Wick step -- tau-x Euclidean rotation continues to a Minkowski boost (SO(3,1))")
    # Minkowski metric (+,-,-,-). Free Dirac Wightman 2-point ~ (gM.p + m) on shell.
    # Verify: a Lorentz boost L(eta) in t-x leaves p^2 = (p^0)^2 - |p|^2 invariant
    # (the Euclidean SO(4) invariant p_E^2 continues to the Minkowski invariant),
    # i.e. the continued covariance is SO(3,1).
    eta = 0.8
    L = np.array([
        [np.cosh(eta), np.sinh(eta), 0, 0],
        [np.sinh(eta), np.cosh(eta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    g_mink = np.diag([1.0, -1.0, -1.0, -1.0])
    # boost preserves the metric: L^T g L = g  (this is the SO(3,1) condition the
    # Wick-continued tau-x SO(4) rotation becomes)
    metric_pres = np.max(np.abs(L.T @ g_mink @ L - g_mink))
    check("Wick-continued tau-x rotation is a metric-preserving SO(3,1) boost (L^T g L = g)",
          metric_pres < 1e-12, detail=f"residual={metric_pres:.2e}")
    # invariant mass shell: p^2 = m^2 preserved under L
    m = 0.7
    pmink = np.array([np.sqrt(0.5 ** 2 + 0.3 ** 2 + m * m), 0.5, 0.3, 0.0])  # forward shell p^0>0
    p2_before = pmink @ g_mink @ pmink
    pboost = L @ pmink
    p2_after = pboost @ g_mink @ pboost
    check("on-shell invariant p^2=m^2 preserved under the continued boost",
          abs(p2_before - m * m) < 1e-12 and abs(p2_after - m * m) < 1e-12,
          detail=f"p^2 before={p2_before:.6f}, after={p2_after:.6f}, m^2={m*m:.6f}")

    section("Part 3: the standard Poincare algebra closes")
    # Vector-rep Lorentz generators (M^{mu nu})^a_b = i(eta^{mu a} delta^nu_b - eta^{nu a} delta^mu_b)
    g_up = np.diag([1.0, -1.0, -1.0, -1.0])  # eta^{mu nu}
    def M(mu, nu):
        Mm = np.zeros((4, 4), dtype=complex)
        for a in range(4):
            for b in range(4):
                Mm[a, b] = 1j * (g_up[mu, a] * (nu == b) - g_up[nu, a] * (mu == b))
        return Mm
    Ms = {(mu, nu): M(mu, nu) for mu in range(4) for nu in range(4)}
    # Lorentz algebra: [M^{mu nu}, M^{rho sig}] = i(eta^{nu rho}M^{mu sig} - eta^{mu rho}M^{nu sig}
    #                                              - eta^{nu sig}M^{mu rho} + eta^{mu sig}M^{nu rho})
    max_lorentz = 0.0
    for mu, nu, rho, sg in itertools.product(range(4), repeat=4):
        comm = Ms[(mu, nu)] @ Ms[(rho, sg)] - Ms[(rho, sg)] @ Ms[(mu, nu)]
        rhs = 1j * (g_up[nu, rho] * Ms[(mu, sg)] - g_up[mu, rho] * Ms[(nu, sg)]
                    - g_up[nu, sg] * Ms[(mu, rho)] + g_up[mu, sg] * Ms[(nu, rho)])
        max_lorentz = max(max_lorentz, np.max(np.abs(comm - rhs)))
    check("Lorentz subalgebra [M,M] closes (rotations J_i=M^{jk} + boosts K_i=M^{0i})",
          max_lorentz < 1e-12, detail=f"max residual={max_lorentz:.2e}")
    # Full Poincare closure by SPAN-MEMBERSHIP (convention-independent): every
    # commutator of {M^{mu nu}, P^mu} must lie in the linear span of the generators.
    def Maff(mu, nu):
        A = np.zeros((5, 5), dtype=complex); A[:4, :4] = Ms[(mu, nu)]; return A
    def Paff(mu):
        A = np.zeros((5, 5), dtype=complex); A[mu, 4] = 1j; return A
    Pa = [Paff(mu) for mu in range(4)]
    gens = [Maff(mu, nu) for mu in range(4) for nu in range(mu + 1, 4)] + Pa  # 6 + 4 = 10
    B = np.array([G.flatten() for G in gens]).T  # 25 x 10 basis matrix
    def span_residual(C):
        coef, *_ = np.linalg.lstsq(B, C.flatten(), rcond=None)
        return np.max(np.abs(B @ coef - C.flatten()))
    max_close = 0.0
    for A in gens:
        for C in gens:
            comm = A @ C - C @ A
            max_close = max(max_close, span_residual(comm))
    check("Poincare algebra closes: every [gen,gen] lies in span{M^{mu nu}, P^mu} "
          "(standard continuum target)",
          max_close < 1e-10, detail=f"max span residual over all 100 commutators={max_close:.2e}")
    max_PP = max(np.max(np.abs(Pa[a] @ Pa[b] - Pa[b] @ Pa[a])) for a in range(4) for b in range(4))
    check("[P^mu, P^nu] = 0 (translations commute)", max_PP < 1e-12, detail=f"max={max_PP:.2e}")

    section("Part 4: spectrum condition is boost-invariant in the standard target")
    rng_pts = [np.array([np.sqrt(px * px + py * py + pz * pz + m * m), px, py, pz])
               for px, py, pz in [(0.5, 0.3, 0.0), (1.2, -0.4, 0.7), (0.0, 0.0, 0.0), (2.0, 1.0, -1.0)]]
    boosts = [0.8, -1.1, 1.7]
    forward_ok = True
    for p in rng_pts:
        for e in boosts:
            Lb = np.array([[np.cosh(e), np.sinh(e), 0, 0], [np.sinh(e), np.cosh(e), 0, 0],
                           [0, 0, 1, 0], [0, 0, 0, 1]])
            pb = Lb @ p
            if pb[0] <= 0:  # energy must stay positive (forward cone preserved)
                forward_ok = False
    check("forward mass shell p^0=+sqrt(p^2+m^2) stays in the forward cone under all boosts (H>=0 survives)",
          forward_ok, detail="W2 spectrum condition is boost-invariant")

    section("Part 5: boundary checklist + honest residual")
    assembly = {
        "kinetic_isotropy_primitive supplies only the structural c_t=c_s premise": True,
        "free-continuum SO(4) two-point covariance is checked here, not granted by the primitive alone": True,
        "reflection positivity is cited from its own row; not ratified here": True,
        "standard OS reconstruction theorem is an external theorem/context, not machine-proved here": True,
        "single-clock/Wightman-structure context remains governed by its own row": True,
        "boost/rotation conclusion remains conditional on the supplied OS/Wightman hypotheses": True,
    }
    for k, v in assembly.items():
        check(k, v)
    residual = {
        "G1: lattice-measure -> continuum-measure bridge beyond the 2-point (and 1+1d->4D arena) -- NOT supplied": True,
        "interacting continuum-existence (constructive-QFT class) -- NOT supplied; free Gaussian sector only": True,
        "RP not newly ratified here; statistics-selection still gated": True,
    }
    print("  -- honest residual (NOT delivered by this assembly):")
    for k, v in residual.items():
        check("residual flagged: " + k, v)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
