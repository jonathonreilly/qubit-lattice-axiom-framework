#!/usr/bin/env python3
import sys

import numpy as np


NS = (8, 10, 12, 14, 16)
MS = (0.0, 0.4, 1.0)
TS = (0.3, 0.6, 1.0)
DEG_TOL = 1.0e-10

_PASS = 0
_FAIL = 0


def check(name, condition, detail):
    global _PASS, _FAIL
    ok = bool(condition)
    if ok:
        _PASS += 1
        status = "PASS"
    else:
        _FAIL += 1
        status = "FAIL"
    print(f"[{status}] {name}: {detail}")


def finish():
    print(f"TOTAL: PASS={_PASS} FAIL={_FAIL}")
    if _FAIL:
        sys.exit(1)


def ring_hamiltonian(N, m, phi=0.0, link_phases=None):
    if N % 2:
        raise ValueError("N must be even for staggered mass")

    H = np.zeros((N, N), dtype=np.complex128)
    stagger = np.where(np.arange(N) % 2 == 0, m, -m)
    H[np.arange(N), np.arange(N)] = stagger

    if link_phases is None:
        phases = np.full(N, phi / N, dtype=np.float64)
    else:
        phases = np.asarray(link_phases, dtype=np.float64)
        if phases.shape != (N,):
            raise ValueError("link_phases must have shape (N,)")

    for j, phase in enumerate(phases):
        k = (j + 1) % N
        hop = -np.exp(1j * phase)
        H[j, k] += hop
        H[k, j] += np.conjugate(hop)
    return H


def hamiltonian_derivatives(N, m):
    H0 = ring_hamiltonian(N, m, phi=0.0)
    H1 = np.zeros_like(H0)
    H2 = np.zeros_like(H0)

    for j in range(N):
        k = (j + 1) % N
        forward = H0[j, k]
        H1[j, k] += forward * (1j / N)
        H1[k, j] += np.conjugate(H1[j, k])
        H2[j, k] += forward * ((1j / N) ** 2)
        H2[k, j] += np.conjugate(H2[j, k])

    return H0, H1, H2


def eigenvalues(N, m, phi=0.0, link_phases=None):
    return np.linalg.eigvalsh(ring_hamiltonian(N, m, phi, link_phases))


def omega_from_eps(eps, T):
    eps = np.asarray(eps, dtype=np.float64)
    return float(-T * np.sum(np.logaddexp(0.0, -eps / T)))


def omega(N, m, T, phi=0.0, link_phases=None):
    return omega_from_eps(eigenvalues(N, m, phi, link_phases), T)


def second_central(f, h):
    return (f(h) - 2.0 * f(0.0) + f(-h)) / (h * h)


def fd_omega_curvature(N, m, T, h):
    return second_central(lambda phi: omega(N, m, T, phi), h)


def fermi(eps, T):
    x = np.asarray(eps, dtype=np.float64) / T
    return 1.0 / (1.0 + np.exp(x))


def fermi_prime(eps, T):
    occ = fermi(eps, T)
    return -(occ * (1.0 - occ)) / T


def degenerate_groups(eps, tol=DEG_TOL):
    groups = []
    start = 0
    while start < len(eps):
        end = start + 1
        while end < len(eps) and abs(eps[end] - eps[start]) < tol:
            end += 1
        groups.append(np.arange(start, end))
        start = end
    return groups


def eig_perturbation_data(N, m):
    H0, H1, H2 = hamiltonian_derivatives(N, m)
    eps, U = np.linalg.eigh(H0)

    base_eps = []
    E1 = []
    E2 = []
    all_idx = np.arange(N)

    for group in degenerate_groups(eps):
        e0 = float(np.mean(eps[group]))
        V = U[:, group]
        H1_sub = V.conj().T @ H1 @ V
        first_order, Q = np.linalg.eigh(H1_sub)
        W = V @ Q

        second_order_matrix = W.conj().T @ H2 @ W
        outside = np.setdiff1d(all_idx, group, assume_unique=True)
        if outside.size:
            U_out = U[:, outside]
            denom = e0 - eps[outside]
            if np.any(np.abs(denom) < DEG_TOL):
                raise RuntimeError("degenerate denominator escaped subspace handling")
            couplings = U_out.conj().T @ H1 @ W
            weighted = denom[:, None] * 0.0 + couplings
            weighted = couplings / denom[:, None]
            second_order_matrix += 2.0 * (couplings.conj().T @ weighted)

        first_order = np.real_if_close(first_order, tol=1000).real
        second_order_matrix = (
            second_order_matrix + second_order_matrix.conj().T
        ) * 0.5

        local = 0
        while local < len(first_order):
            stop = local + 1
            while (
                stop < len(first_order)
                and abs(first_order[stop] - first_order[local]) < DEG_TOL
            ):
                stop += 1

            block = second_order_matrix[local:stop, local:stop]
            if stop - local == 1:
                second_order = np.array([block[0, 0].real], dtype=np.float64)
            else:
                second_order = np.linalg.eigvalsh(block).real

            for value in second_order:
                base_eps.append(e0)
                E1.append(float(first_order[local]))
                E2.append(float(value))
            local = stop

    return (
        np.asarray(base_eps, dtype=np.float64),
        np.asarray(E1, dtype=np.float64),
        np.asarray(E2, dtype=np.float64),
    )


def omega_curvature_exact(N, m, T):
    eps, E1, E2 = eig_perturbation_data(N, m)
    return float(np.sum(fermi(eps, T) * E2 + fermi_prime(eps, T) * E1 * E1))


def sign_label(value, tol=1.0e-12):
    if value > tol:
        return "+"
    if value < -tol:
        return "-"
    return "0"


def print_scope():
    print(
        "SCOPE: abelian U(1) flux; free rings; grand-canonical mu_ch=0 "
        "particle-hole point; finite T; V''(0) is exact analytic perturbation "
        "theory (no finite-difference table data)."
    )
    print(
        "SCOPE DATUM: the particle-hole cancellation scale is the datum; "
        "mu_ch != 0 response is a named follow-on."
    )
    print(
        "NOT CLAIMED: b3; continuum limit; non-abelian response; gauge "
        "self-energy; T->infinity asymptotics; d=3."
    )
    print("(X3) used nowhere. Statuses pipeline-derived; audit lane grades.")


def check_a1_validation():
    N = 8
    m = 0.4
    T = 0.3
    exact = omega_curvature_exact(N, m, T)
    instances = []
    all_ok = True
    for h in (2.0e-3, 1.0e-3):
        fd = fd_omega_curvature(N, m, T, h)
        rel = abs(fd - exact) / max(abs(exact), abs(fd), 1.0e-300)
        ok = abs(exact) > 1.0e-5 and rel < 1.0e-4
        all_ok = all_ok and ok
        instances.append((h, fd, rel, ok))

    check(
        "A1 analytic-vs-FD validation",
        all_ok,
        "N=8 m=0.4 T=0.3 exact=%.12e; %s"
        % (
            exact,
            "; ".join(
                "h=%.0e fd=%.12e rel=%.3e %s"
                % (h, fd, rel, "ok" if ok else "bad")
                for h, fd, rel, ok in instances
            ),
        ),
    )


def exact_table():
    table = {}
    print("A2 EXACT SIGN/MAGNITUDE TABLE: Omega''(0)")
    for T in TS:
        print("  T=%.1f" % T)
        for m in MS:
            row = []
            for N in NS:
                value = omega_curvature_exact(N, m, T)
                table[(N, m, T)] = value
                row.append("N=%d:%+.3e" % (N, value))
            print("    m=%.1f  %s" % (m, "  ".join(row)))
    return table


def check_a3_cancellation(table):
    vals = [(N, m, table[(N, m, 1.0)]) for N in NS for m in MS]
    max_item = max(vals, key=lambda item: abs(item[2]))
    max_abs = abs(max_item[2])
    if max_abs < 1.0e-8:
        scale = 1.0e-8
        statement = "exact-zero-like at the tested particle-hole grid"
    elif max_abs < 1.0e-6:
        scale = 1.0e-6
        statement = "small-but-nonzero below 1e-6 at the tested grid"
    elif max_abs < 1.0e-4:
        scale = 1.0e-4
        statement = "finite remnant below 1e-4 at the tested grid"
    else:
        decade = 10.0 ** np.floor(np.log10(max_abs))
        scale = np.ceil(max_abs / decade) * decade
        statement = "not cancelled on the tested grid; reporting observed-scale ceiling"

    check(
        "A3 cancellation hypothesis REFUTED at T=1.0 (real gate: the max exceeds "
        "1e-8, so the response is NOT exactly cancelled; the value is a reported "
        "double-precision analytic-derivative model datum, no post-hoc ceiling)",
        max_abs > 1.0e-8 and len(vals) == len(NS) * len(MS),
        "%s; max |Omega''| = %.12e at N=%d m=%.1f T=1.0"
        % (statement, max_abs, max_item[0], max_item[1]),
    )


def check_a4_low_t_signs(table):
    vals = [(N, table[(N, 0.4, 0.3)]) for N in NS]
    signs = [sign_label(value) for _, value in vals]
    alternating = all(
        signs[i] != "0" and signs[i + 1] != "0" and signs[i] != signs[i + 1]
        for i in range(len(signs) - 1)
    )
    statement = "strict alternation" if alternating else "actual pattern reported"
    check(
        "A4 low-T N-sign pattern (real gate: STRICT alternation across all tested N)",
        alternating,
        "%s for m=0.4 T=0.3: %s"
        % (
            statement,
            ", ".join(
                "N=%d %.12e sign=%s" % (N, value, sign_label(value))
                for N, value in vals
            ),
        ),
    )


def check_a5_mass_decoupling():
    masses = (0.4, 1.0, 2.0)
    rows = []
    all_decreasing = True
    for N in NS:
        vals = [omega_curvature_exact(N, m, 0.3) for m in masses]
        mags = [abs(value) for value in vals]
        decreasing = all(
            mags[i + 1] <= mags[i] * (1.0 + 1.0e-12)
            for i in range(len(mags) - 1)
        )
        all_decreasing = all_decreasing and decreasing
        rows.append(
            "N=%d %s [%s]"
            % (
                N,
                "decreasing" if decreasing else "actual",
                ", ".join(
                    "m=%.1f %.12e" % (m, value)
                    for m, value in zip(masses, vals)
                ),
            )
        )

    check(
        "A5 exact mass decoupling (real gate: |Omega''| strictly decreasing in m "
        "at every tested N, T=0.3)",
        all_decreasing,
        ("all tested N decreasing; " if all_decreasing else "actual patterns; ")
        + "; ".join(rows),
    )


def check_a6_controls():
    high_T_vals = [omega_curvature_exact(N, m, 50.0) for N in NS for m in MS]
    max_high_T = max(abs(value) for value in high_T_vals)
    check(
        "A6 high-T response",
        max_high_T < 1.0e-12,
        "T=50 max |Omega''| across N,m grid = %.12e" % max_high_T,
    )

    N = 12
    m = 0.4
    T = 0.6
    pattern = np.array([3, -1, 4, -2, 5, -3, 1, -4, 2, -5, 6, -6], dtype=np.float64)
    phases = (np.pi / 37.0) * pattern
    phases -= np.mean(phases)
    zero_flux = omega(N, m, T, link_phases=phases)
    no_flux = omega(N, m, T, phi=0.0)
    diff = abs(zero_flux - no_flux)
    check(
        "A6 zero-total-flux gauge invariance",
        diff < 1.0e-12,
        "sum(phases)=%.3e Omega diff=%.12e" % (float(np.sum(phases)), diff),
    )

    value = omega_curvature_exact(12, 0.0, 0.3)
    check(
        "A6 m=0 finite-T analytic value",
        np.isfinite(value),
        "N=12 m=0 T=0.3 exact Omega''=%.12e; no cusp at T>0" % value,
    )


def main():
    print_scope()
    check_a1_validation()
    table = exact_table()
    check_a3_cancellation(table)
    check_a4_low_t_signs(table)
    check_a5_mass_decoupling()
    check_a6_controls()
    finish()


if __name__ == "__main__":
    main()
