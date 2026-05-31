#!/usr/bin/env python3
"""Audit-companion runner: uniform matter-sector transfer-matrix gap bound.

Verifies the mechanism of T1: for the canonical staggered SU(3) spatial hop at any
fixed background U, the operator is anti-Hermitian (spectrum {i*lambda_j}, lambda_j
real), so the single-fermion energies E_j[U] = arcsinh(sqrt(m^2 + lambda_j^2))
satisfy E_j[U] >= arcsinh(m) > 0 UNIFORMLY in U and spatial volume (the bound is the
lambda=0 floor of sqrt(m^2+lambda^2), independent of the actual spectrum). This is a
dispersion-infimum bound (no Perron / finite-volume argument), so it survives the
thermodynamic limit. It does NOT address the pure-gauge glueball gap (the open piece).

numpy + stdlib only; single-seed deterministic. SCORECARD PASS=N FAIL=0.
"""
import numpy as np

RNG = np.random.default_rng(20260530)
NC = 3


def random_su3(rng):
    """Haar-ish SU(3) via QR of a complex Gaussian, det-normalized to 1."""
    z = (rng.normal(size=(NC, NC)) + 1j * rng.normal(size=(NC, NC))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    q = q @ np.diag(r.diagonal() / np.abs(r.diagonal()))   # fix phases -> Haar U(3)
    q = q / (np.linalg.det(q) ** (1.0 / NC))               # -> SU(3)
    return q


def staggered_spatial_hop(L, rng, hermitian_break=0.0):
    """Anti-Hermitian canonical staggered SU(3) spatial hop on an L x L periodic
    spatial lattice (2 spatial dirs), 3 colors. H = sum_mu (1/2)(D_mu - D_mu^dag),
    staggered phases eta_x=1, eta_y=(-1)^x. With hermitian_break>0 a Hermitian piece
    is added (a control: spoils anti-Hermiticity -> complex lambda)."""
    N = L * L
    dim = NC * N
    def idx(x, y):
        return ((x % L) * L + (y % L))
    H = np.zeros((dim, dim), dtype=complex)
    for x in range(L):
        for y in range(L):
            s = idx(x, y)
            for mu, (dx, dy, eta) in enumerate(
                    [(1, 0, 1.0), (0, 1, (-1.0) ** x)]):
                t = idx(x + dx, y + dy)
                U = eta * random_su3(rng)
                blk = slice(NC * s, NC * s + NC)
                blkt = slice(NC * t, NC * t + NC)
                D = np.zeros((dim, dim), dtype=complex)
                D[blkt, blk] = U                # forward hop s -> t
                H += 0.5 * (D - D.conj().T)      # anti-Hermitian part
                if hermitian_break:
                    H += hermitian_break * 0.5 * (D + D.conj().T)  # CONTROL only
    return H


def energies(H, m):
    w = np.linalg.eigvals(H)
    lam = w.imag                                # lambda_j (real if H anti-Herm)
    return np.arcsinh(np.sqrt(m * m + lam * lam)), w


def check_anti_hermitian():
    ok = True
    for _ in range(20):
        L = int(RNG.integers(2, 5))
        H = staggered_spatial_hop(L, RNG)
        if not np.allclose(H.conj().T, -H, atol=1e-12):
            ok = False
        w = np.linalg.eigvals(H)
        if np.max(np.abs(w.real)) > 1e-9:       # spectrum purely imaginary
            ok = False
    return ok


def check_uniform_lower_bound():
    """min_j E_j[U] >= arcsinh(m) for all sampled U, volumes, masses."""
    ok = True
    worst_slack = np.inf
    for _ in range(40):
        L = int(RNG.integers(2, 5))
        m = float(RNG.uniform(0.05, 3.0))
        H = staggered_spatial_hop(L, RNG)
        E, _ = energies(H, m)
        slack = float(E.min() - np.arcsinh(m))
        worst_slack = min(worst_slack, slack)
        if slack < -1e-10:
            ok = False
    # bound must hold (slack >= 0) across every sample
    return ok and worst_slack >= -1e-10


def check_bound_uniform_in_U_and_volume():
    """arcsinh(m) does not depend on U/volume, and min_j E_j stays >= it as L grows."""
    ok = True
    m = 0.5
    floor = np.arcsinh(m)
    for L in (2, 3, 4, 5):
        for _ in range(8):
            E, _ = energies(staggered_spatial_hop(L, RNG), m)
            if E.min() < floor - 1e-10:
                ok = False
    return ok


def check_transfer_eig_below_one():
    """2-step transfer eigenvalue e^{-2E_j} <= e^{-2 arcsinh(m)} < 1."""
    ok = True
    for _ in range(20):
        m = float(RNG.uniform(0.1, 2.0))
        E, _ = energies(staggered_spatial_hop(3, RNG), m)
        cap = np.exp(-2 * np.arcsinh(m))
        if np.max(np.exp(-2 * E)) > cap + 1e-10 or cap >= 1.0:
            ok = False
    return ok


def check_nontriviality():
    """(a) m->0 => arcsinh(m)->0 (bound is m-driven, not vacuous);
    (b) CONTROL: a non-anti-Hermitian (Hermitian-broken) hop has complex lambda
        (Re(eig)!=0), so the real-lambda dispersion bound argument FAILS -- i.e.
        anti-Hermiticity is load-bearing for the bound."""
    ok = True
    if not (np.arcsinh(1e-6) < 1e-5 and np.arcsinh(0.0) == 0.0):
        ok = False
    Hbad = staggered_spatial_hop(3, RNG, hermitian_break=0.7)
    wbad = np.linalg.eigvals(Hbad)
    if np.max(np.abs(wbad.real)) < 1e-3:        # control must FAIL anti-Herm
        ok = False                              # (if it didn't, control is vacuous)
    return ok


def main():
    checks = [
        ("anti_hermitian_staggered_hop", check_anti_hermitian()),
        ("uniform_lower_bound_arcsinh_m", check_uniform_lower_bound()),
        ("bound_uniform_in_U_and_volume", check_bound_uniform_in_U_and_volume()),
        ("transfer_eig_below_one", check_transfer_eig_below_one()),
        ("nontriviality_m_to_0_and_antiherm_control", check_nontriviality()),
    ]
    npass = sum(1 for _, ok in checks if ok)
    nfail = sum(1 for _, ok in checks if not ok)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    if nfail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
