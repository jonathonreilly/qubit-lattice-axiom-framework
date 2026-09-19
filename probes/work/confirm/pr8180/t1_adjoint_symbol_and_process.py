#!/usr/bin/env python3
"""J:confirm:J-attack-g-PR8180 -- independent test of block 35's T1 gloss (PR #8180).

Statement tested (note, Theorem T1): on the nonzero modes the stationary kernel is
    C_s(k) = sigma^2 phi(k)^s / (1 - |phi(k)|^2),
    "i.e.  C_s = sigma^2 (I - P P*)^{-1} P*^s  as an operator on the plane",
with phi(k) = (1 + e^{ik1} + e^{ik2})/3 the multiplier of theta_{t+1} = P theta_t + xi.

The finder (grok-4.6) computed Rayleigh quotients of the finite-t matrix Sigma_t (P^s)^T
on L = 3 in a hand-rolled Q(i sqrt 3).  This script uses other machinery:

  A. exact, L = 4, Gaussian rationals (sympy DomainMatrix over QQ_I): the STATIONARY
     operator exactly as written, G (P^T)^s with G the pseudo-inverse of I - P P^T on the
     mean-zero plane, conjugated by the full character matrix U (columns chi with
     P chi = phi chi); every off-diagonal entry and every diagonal entry compared;
     both predecessor orientations (x - e_i as in the runner, and x + e_i);
  B. floating point, L = 3..10, both orientations: eigenvalue of the written operator on
     the character where P acts by phi, against phi^s/(1-u) and conj(phi)^s/(1-u);
  C. Monte Carlo of the recursion itself (L = 12, runner orientation, mean removed):
     the empirical matrix E[theta(t) theta(t+s)^T] -- the note's own proof line -- against
     the written operator and its transpose entrywise, its eigenvalue on the phi-character,
     and the conjugate-first mode covariance E[conj(a(t)) a(t+s)] of the amplitude
     a = chi^H theta, which obeys a(t+1) = phi a(t) + noise.
"""
from __future__ import annotations

import cmath
import itertools

import numpy as np
from sympy.polys.domains import QQ, QQ_I
from sympy.polys.matrices import DomainMatrix


# ----------------------------------------------------------------------------- common
def site(L, i, j):
    return (i % L) * L + (j % L)


def predecessor_offsets(orientation):
    # "A": predecessors x, x - e1, x - e2 (the runner's shift_matrix); "B": x, x + e1, x + e2
    return ((0, 0), (-1, 0), (0, -1)) if orientation == "A" else ((0, 0), (1, 0), (0, 1))


# ----------------------------------------------------------------------------- A: exact, L = 4, QQ_I
def gi(a, b=0):
    return QQ_I(QQ(a), QQ(b))


def gconj(z):
    return QQ_I(z.x, -z.y)


I_POW = [gi(1), gi(0, 1), gi(-1), gi(0, -1)]  # i^m


def part_a(smax=4):
    L = 4
    N = L * L
    zero, one = gi(0), gi(1)
    modes = [(n1, n2) for n1, n2 in itertools.product(range(L), repeat=2)]
    report = {}
    for orientation in ("A", "B"):
        rows = [[zero] * N for _ in range(N)]
        for i, j in itertools.product(range(L), repeat=2):
            for di, dj in predecessor_offsets(orientation):
                rows[site(L, i, j)][site(L, i + di, j + dj)] += gi(QQ(1, 3))
        P = DomainMatrix(rows, (N, N), QQ_I)
        PT = P.transpose()
        Id = DomainMatrix.eye(N, QQ_I)
        J = DomainMatrix([[gi(QQ(1, N))] * N for _ in range(N)], (N, N), QQ_I)
        A = Id - P * PT
        G = (A + J).inv() - J  # pseudo-inverse of I - P P^T on the mean-zero plane
        assert G * A == Id - J and A * G == Id - J

        # characters: chi_{+/-}(x) = e^{+/- i k.x}, k = 2 pi n / 4, so e^{i k.x} = i^{n.x}
        cols, phis = [], []
        for n1, n2 in modes:
            phi = (one + I_POW[n1 % 4] + I_POW[n2 % 4]) / gi(3)
            chosen = None
            for sign in (-1, 1):
                chi = [I_POW[(sign * (n1 * i + n2 * j)) % 4] for i in range(L) for j in range(L)]
                v = DomainMatrix([[c] for c in chi], (N, 1), QQ_I)
                if P * v == v * DomainMatrix([[phi]], (1, 1), QQ_I):
                    chosen = chi
                    break
            assert chosen is not None
            cols.append(chosen)
            phis.append(phi)
        U = DomainMatrix([[cols[m][x] for m in range(N)] for x in range(N)], (N, N), QQ_I)
        UH = DomainMatrix([[gconj(cols[m][x]) for x in range(N)] for m in range(N)], (N, N), QQ_I)
        nN = gi(N)  # U^H U = N I, so U^H M U = N diag(...) for every circulant M

        def diag_of(M):
            rows_ = (UH * M * U).to_list()
            off = sum(1 for a in range(N) for b in range(N) if a != b and rows_[a][b] != zero)
            return [rows_[a][a] / nN for a in range(N)], off

        dP, offP = diag_of(P)
        dPT, offPT = diag_of(PT)
        ok_P = offP == 0 and all(dP[m] == phis[m] for m in range(N))
        ok_PT = offPT == 0 and all(dPT[m] == gconj(phis[m]) for m in range(N))

        slots = offdiag_nonzero = eq_conj = eq_phi = nonreal = 0
        t_eq_phi = 0
        witness = None
        PTs, Ps = Id, Id
        for s in range(1, smax + 1):
            PTs = PTs * PT
            Ps = Ps * P
            dW, offW = diag_of(G * PTs)
            dT, offT = diag_of(G * Ps)
            offdiag_nonzero += offW + offT
            for m, (n1, n2) in enumerate(modes):
                if (n1, n2) == (0, 0):
                    continue
                phi = phis[m]
                u = phi * gconj(phi)
                stated = phi ** s / (one - u)
                conj_form = gconj(phi) ** s / (one - u)
                got = dW[m]
                slots += 1
                eq_conj += got == conj_form
                eq_phi += got == stated
                nonreal += (phi ** s).y != 0
                t_eq_phi += dT[m] == stated
                if witness is None and got != stated:
                    witness = (s, n1, n2, phi, stated, got)
        report[orientation] = dict(ok_P=ok_P, ok_PT=ok_PT, slots=slots, offdiag_nonzero=offdiag_nonzero, eq_conj=eq_conj,
                                   eq_phi=eq_phi, nonreal=nonreal, t_eq_phi=t_eq_phi, witness=witness)
    return report


# ----------------------------------------------------------------------------- B: floating scan, L = 3..10
def build_P_float(L, orientation):
    N = L * L
    P = np.zeros((N, N))
    for i, j in itertools.product(range(L), repeat=2):
        for di, dj in predecessor_offsets(orientation):
            P[site(L, i, j), site(L, i + di, j + dj)] += 1.0 / 3.0
    return P


def phi_char(L, n1, n2, P):
    k1, k2 = 2 * np.pi * n1 / L, 2 * np.pi * n2 / L
    phi = (1 + cmath.exp(1j * k1) + cmath.exp(1j * k2)) / 3
    for sign in (-1, 1):
        chi = np.array([cmath.exp(sign * 1j * (k1 * i + k2 * j)) for i in range(L) for j in range(L)])
        if np.allclose(P @ chi, phi * chi, atol=1e-12):
            return phi, chi
    raise AssertionError("no character with multiplier phi")


def stationary_G(P):
    N = P.shape[0]
    J = np.full((N, N), 1.0 / N)
    A = np.eye(N) - P @ P.T
    return np.linalg.inv(A + J) - J


def part_b(Ls=range(3, 11), smax=4, tol_nonreal=1e-9):
    worst_conj = 0.0
    min_gap_phi = np.inf
    slots = nonreal_slots = 0
    for L in Ls:
        for orientation in ("A", "B"):
            P = build_P_float(L, orientation)
            G = stationary_G(P)
            PTs = np.eye(L * L)
            for s in range(1, smax + 1):
                PTs = PTs @ P.T
                Cw = G @ PTs
                for n1, n2 in itertools.product(range(L), repeat=2):
                    if (n1, n2) == (0, 0):
                        continue
                    phi, chi = phi_char(L, n1, n2, P)
                    u = abs(phi) ** 2
                    lam = np.vdot(chi, Cw @ chi) / (L * L)
                    slots += 1
                    worst_conj = max(worst_conj, abs(lam - np.conj(phi) ** s / (1 - u)))
                    if abs((phi ** s).imag) > tol_nonreal:
                        nonreal_slots += 1
                        min_gap_phi = min(min_gap_phi, abs(lam - phi ** s / (1 - u)) / abs(phi ** s / (1 - u)))
    return dict(slots=slots, nonreal=nonreal_slots, worst_conj=worst_conj, min_rel_gap_phi=min_gap_phi)


# ----------------------------------------------------------------------------- C: Monte Carlo of the recursion
def part_c(L=12, R=256, burn=400, T=4000, smax=3, seed=8180):
    rng = np.random.default_rng(seed)
    N = L * L
    P = build_P_float(L, "A")
    G = stationary_G(P)
    theta = np.zeros((R, L, L))

    def step(th):
        return (th + np.roll(th, 1, axis=1) + np.roll(th, 1, axis=2)) / 3.0 + rng.standard_normal(th.shape)

    # check the vectorised step is P: (roll by +1 on axis 1 puts theta_{i-1,j} at (i,j))
    probe = rng.standard_normal((1, L, L))
    assert np.allclose(((probe + np.roll(probe, 1, axis=1) + np.roll(probe, 1, axis=2)) / 3.0).reshape(N), P @ probe.reshape(N))

    for _ in range(burn):
        theta = step(theta)
    hist = []
    acc = [np.zeros((N, N)) for _ in range(smax + 1)]
    n_acc = 0
    for t in range(T + smax):
        theta = step(theta)
        x = theta.reshape(R, N)
        x = x - x.mean(axis=1, keepdims=True)  # the mean-zero plane (the zero mode random-walks)
        hist.append(x)
        if len(hist) > smax + 1:
            hist.pop(0)
        if len(hist) == smax + 1:
            x0 = hist[0]
            for s in range(smax + 1):
                acc[s] += x0.T @ hist[s]
            n_acc += R
    Chat = [a / n_acc for a in acc]  # Chat[s][x, y] ~ E[theta_x(t) theta_y(t+s)]

    out = {}
    PTs, Ps = np.eye(N), np.eye(N)
    scale = np.abs(G).max()
    for s in range(1, smax + 1):
        PTs = PTs @ P.T
        Ps = Ps @ P
        Cw, Ct = G @ PTs, G @ Ps
        out[f"entry_dev_written_s{s}"] = np.abs(Chat[s] - Cw).max() / scale
        out[f"entry_dev_transposed_s{s}"] = np.abs(Chat[s] - Ct).max() / scale
        out[f"written_vs_transposed_s{s}"] = np.abs(Cw - Ct).max() / scale

    # eigenvalue of the empirical operator on the phi-character, and the conjugate-first mode covariance
    closer_conj = closer_phi = counted = 0
    worst_op_conj = worst_mode_phi = 0.0
    for n1, n2 in itertools.product(range(L), repeat=2):
        if (n1, n2) == (0, 0):
            continue
        phi, chi = phi_char(L, n1, n2, P)
        v0 = np.vdot(chi, Chat[0] @ chi).real
        for s in range(1, smax + 1):
            lam = np.vdot(chi, Chat[s] @ chi) / v0  # chi^H E[theta(t) theta(t+s)^T] chi / Var  (= E[a(t) conj a(t+s)]/Var)
            mode = np.vdot(chi, Chat[s].T @ chi) / v0  # = E[conj a(t) a(t+s)] / Var for a = chi^H theta
            if abs((phi ** s).imag) >= 0.05:
                counted += 1
                d_conj, d_phi = abs(lam - np.conj(phi) ** s), abs(lam - phi ** s)
                closer_conj += d_conj < d_phi
                closer_phi += d_phi < d_conj
                worst_op_conj = max(worst_op_conj, d_conj)
                worst_mode_phi = max(worst_mode_phi, abs(mode - phi ** s))
    out.update(counted=counted, closer_conj=closer_conj, closer_phi=closer_phi, worst_op_conj=worst_op_conj,
               worst_mode_phi=worst_mode_phi, samples=n_acc)
    return out


def fmt(z):
    return f"{z.x}{'+' if z.y >= 0 else '-'}{abs(z.y)}i"


def main():
    print("A. exact, L = 4, Gaussian rationals; stationary written operator G (P^T)^s, s = 1..4, full character basis")
    ra = part_a()
    for o, r in ra.items():
        lab = "x-e_i (runner)" if o == "A" else "x+e_i (reversed)"
        print(f"  orientation {lab}: U^H P U = diag(phi) {r['ok_P']}; U^H P^T U = diag(conj phi) {r['ok_PT']}; "
              f"nonzero off-diagonal entries of U^H C U (written and transposed) {r['offdiag_nonzero']}")
        print(f"    slots {r['slots']}: written operator's eigenvalue == conj(phi)^s/(1-u) {r['eq_conj']}/{r['slots']}; "
              f"== phi^s/(1-u) {r['eq_phi']}/{r['slots']} (phi^s non-real in {r['nonreal']}); "
              f"transposed G P^s == phi^s/(1-u) {r['t_eq_phi']}/{r['slots']}")
        s, n1, n2, phi, stated, got = r["witness"]
        print(f"    witness s={s} k=2pi({n1},{n2})/4: phi={fmt(phi)}  stated C_s(k)={fmt(stated)}  written operator gives {fmt(got)}")

    print("B. floating point, L = 3..10, both orientations, s = 1..4")
    rb = part_b()
    print(f"  slots {rb['slots']}: max |eigenvalue - conj(phi)^s/(1-u)| = {rb['worst_conj']:.2e}; "
          f"on the {rb['nonreal']} slots with non-real phi^s, min relative distance to phi^s/(1-u) = {rb['min_rel_gap_phi']:.3e}")

    print("C. Monte Carlo of theta_{t+1} = P theta_t + xi on L = 12 (runner orientation), mean removed, seed 8180")
    rc = part_c()
    for s in (1, 2, 3):
        print(f"  s={s}: max entry |E^[theta(t)theta(t+s)^T] - G(P^T)^s| = {rc[f'entry_dev_written_s{s}']:.4f}, "
              f"vs transposed G P^s = {rc[f'entry_dev_transposed_s{s}']:.4f}  (the two operators differ by {rc[f'written_vs_transposed_s{s}']:.4f}; units of max|G|)")
    print(f"  {rc['samples']} sample pairs; {rc['counted']} (mode, s) slots with |Im phi^s| >= 0.05: empirical operator eigenvalue closer to "
          f"conj(phi)^s in {rc['closer_conj']}, to phi^s in {rc['closer_phi']}; max |ratio - conj(phi)^s| = {rc['worst_op_conj']:.4f}; "
          f"conjugate-first mode covariance max |ratio - phi^s| = {rc['worst_mode_phi']:.4f}")

    a_ok = all(r["ok_P"] and r["ok_PT"] and r["offdiag_nonzero"] == 0 and r["eq_conj"] == r["slots"]
               and r["eq_phi"] == r["slots"] - r["nonreal"] and r["nonreal"] > 0 and r["t_eq_phi"] == r["slots"] for r in ra.values())
    b_ok = rb["worst_conj"] < 1e-9 and rb["min_rel_gap_phi"] > 1e-6
    c_ok = (all(rc[f"entry_dev_written_s{s}"] < 0.25 * rc[f"written_vs_transposed_s{s}"] for s in (1, 2, 3))
            and rc["closer_conj"] == rc["counted"] and rc["counted"] > 0)
    if a_ok and b_ok and c_ok:
        rA = ra["A"]
        print(f"HIT: confirmed - block 35 T1's 'i.e.' is off by complex conjugation: at the character where P acts by phi(k), the written "
              f"operator sigma^2 (I - P P*)^{{-1}} P*^s acts by sigma^2 conj(phi)^s/(1-|phi|^2), not the stated sigma^2 phi^s/(1-|phi|^2) "
              f"(exact L=4: {rA['eq_conj']}/{rA['slots']} conj, {rA['eq_phi']}/{rA['slots']} phi = exactly the slots with real phi^s, both "
              f"orientations; float L=3..10: {rb['nonreal']} non-real slots all off, min relative gap {rb['min_rel_gap_phi']:.3f}); the operator "
              f"is the process's E[theta(t)theta(t+s)^T] (Monte Carlo), while phi^s/(1-u) is the conjugate-first mode covariance, whose operator "
              f"is the transpose sigma^2 (I - P P*)^{{-1}} P^s")
        print("SUMMARY: confirmed - T1's mode formula and its operator gloss differ by conjugation (P*^s should be P^s, or phi^s should be "
              "conj phi^s) on every nonzero mode with non-real phi^s, exact on L=4, float on L=3..10, and in a Monte Carlo of the recursion; "
              "the runner's cosine characters and real-phi symbolic check cannot see it")
    else:
        print(f"SUMMARY: not reproduced - exact {a_ok}, float {b_ok}, Monte Carlo {c_ok}; see the counts above")


if __name__ == "__main__":
    main()
