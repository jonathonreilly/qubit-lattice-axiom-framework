#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
C/N grounding on the channel surface: the peripheral unitary summand
====================================================================
Companion runner for
docs/CHANNEL_SURFACE_CN_GROUNDING_PERIPHERAL_UNITARY_SUMMAND_BOUNDED_THEOREM_NOTE_2026-06-11.md.

CONTEXT.  The kinetic-isotropy retirement chain rests on two readings named
by the spectrum-reflection cycle (TICK_UNITARITY, 2026-06-10):
  (N) the realized tick is norm-nonincreasing on its carrier fiber
      (channel envelope), and
  (C) the realized tick carries a tick-level transport of a retained
      spectrum-reflection identity.
This runner checks the theorem package that grounds both on the channel
surface itself:

THE THEOREMS (finite-dimensional, exact).
  (T1, N derived)  A unital trace-preserving CP fiber tick is a
       HILBERT-SCHMIDT CONTRACTION:  the operator-Schwarz inequality
       Phi(a)^dag Phi(a) <= Phi(a^dag a) (unitality) plus trace
       preservation give  ||Phi(a)||_2 <= ||a||_2.  Both hypotheses are
       load-bearing: amplitude damping (TP, non-unital) has HS-norm
       1.107 > 1; a unital CP non-TP Stinespring map has HS-norm
       1.016 > 1.  Unitality on the carrier fiber is exactly
       sea-state stationarity (the K-real maximally mixed state is
       stationary), so N reduces to {CPTP class + sea-stationarity}.
  (T2, peripheral structure)  A finite-dimensional contraction splits as
       T = U_per (+) T_cnu: every unimodular eigenvalue's eigenvector is a
       joint eigenvector of T^dag (the contraction equality case), the
       peripheral eigenspaces reduce T orthogonally to a unitary summand,
       and the completely-non-unitary remainder has spectral radius < 1.
  (T3, C derived on the summand)  The peripheral summand carries the
       CANONICAL spectrum-reflection conjugacy (complex conjugation in its
       spectral frame: the spectrum-reflection cycle's converse), so the
       part of the tick that carries undamped spectral content satisfies
       C automatically -- no extra transport premise.
  (T4, asymptotic consumer reduction)  Tick-separation covariance data
       C(n) = (peripheral oscillation) + (cnu transient) converges to the
       peripheral band geometrically in finite dimension; the runner's
       diagonal witness measures window-Prony error tracking rho_cnu^{n0}.
       Spectral consumers factor through the peripheral summand when read
       at large separation / faithful asymptotic window.  Separate
       finite-window covariance and record-production premises remain with
       the downstream consumer notes.
  (T5, residual)  On this channel-surface slice, C and N reduce to three
       named items: the CPTP-class reading (the record-dominated
       pointer-transport surface's class), sea-stationarity (= fiber
       unitality), and BAND PERSISTENCE (the realized carrier band lives in
       the peripheral summand -- the sharpened form of the dichotomy
       chain's reduced-P4 "dispersiveness").

COMPOSITION WITH THE TRANSCRIPTION CYCLE.  The registration-dressed fiber
of the stack-transcription model (sigma_x-dephasing x rotation) is a
doubly stochastic channel: its Bloch transfer has HS-norm exactly 1 and its
registered sector M(eps) is a strict contraction for eps > 0 (empty
peripheral part, band slightly damped), becoming peripheral exactly at
eps = 0 -- the faithful limit of the transcription cycle is the peripheral
restoration of this note's summand.  The two cycles compose without
tension.

EVERY HYPOTHESIS GETS A HOSTILE WITNESS:
  drop unitality   -> amplitude damping: HS-norm > 1 (N fails);
  drop trace pres. -> unital Stinespring non-TP map: HS-norm > 1 (N fails);
  drop band persistence -> a fully cnu tick: no peripheral band; the
       large-separation data dies geometrically (nothing for the chain to
       read) -- persistence is exactly what "the carrier has a band" means.

WHAT THIS DOES NOT CLAIM.  No audit status is set or predicted.  That the
realized tick is in the CPTP class is the pointer-transport surface's
reading; that the sea state is stationary is the chain's standing sea
reading; that the carrier band is peripheral (undamped) is the sharpened
persistence residual -- all three NAMED, none derived here.  No new axiom,
no new primitive, no Tier-A admission.

Run: python3 scripts/channel_surface_cn_grounding_peripheral_summand_2026_06_11.py
"""
from __future__ import annotations

import sys

import numpy as np

PASS, FAIL = 0, 0
RNG = np.random.default_rng(20260611)


def check(label, ok, detail=""):
    """An INDEPENDENT computed test. ok must be a computed boolean, never a hard-coded True."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


def rand_unitary(n):
    z = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


SX = np.array([[0, 1], [1, 0]], dtype=complex)

# ----------------------------------------------------------------------------
print("PART A -- T1 step 1: the operator-Schwarz inequality for unital CP maps")
print("=" * 78)
ok_schwarz = True
for _ in range(30):
    d, k = 3, 2
    A = RNG.normal(size=(d * k, d)) + 1j * RNG.normal(size=(d * k, d))
    V, _ = np.linalg.qr(A)  # isometry: V^dag V = I_d  =>  Phi(a) = V^dag (a (x) I_k) V is unital CP

    def Phi(a, V=V, d=d, k=k):
        return V.conj().T @ np.kron(a, np.eye(k)) @ V

    a = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
    gap = Phi(a.conj().T @ a) - Phi(a).conj().T @ Phi(a)
    ok_schwarz &= np.min(np.linalg.eigvalsh(gap)) > -1e-10
check("A1 Phi(a)^dag Phi(a) <= Phi(a^dag a) (PSD gap) on 30 random unital CP Stinespring maps",
      ok_schwarz, "unitality is what powers the Schwarz step")

# ----------------------------------------------------------------------------
print("\nPART B -- T1: doubly stochastic ticks are Hilbert-Schmidt contractions")
print("=" * 78)
ok_hs, ok_chain = True, True
for _ in range(30):
    d = int(RNG.integers(2, 5))
    m = int(RNG.integers(2, 5))
    ps = RNG.dirichlet(np.ones(m))
    Us = [rand_unitary(d) for _ in range(m)]
    S = sum(p * np.kron(U.conj(), U) for p, U in zip(ps, Us))  # superoperator on vec(a)
    ok_hs &= np.linalg.norm(S, 2) <= 1 + 1e-10
    # the trace chain, stepwise: tr(Phi(a)^dag Phi(a)) <= tr(Phi(a^dag a)) = tr(a^dag a)
    a = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
    Pa = sum(p * U @ a @ U.conj().T for p, U in zip(ps, Us))
    Paa = sum(p * U @ (a.conj().T @ a) @ U.conj().T for p, U in zip(ps, Us))
    ok_chain &= (np.trace(Pa.conj().T @ Pa).real <= np.trace(Paa).real + 1e-10
                 and abs(np.trace(Paa).real - np.trace(a.conj().T @ a).real) < 1e-10)
check("B1 mixed-unitary (doubly stochastic) superoperators have HS-norm <= 1 (30 instances)",
      ok_hs, "N derived: the channel envelope is a THEOREM on this class")
check("B2 the proof chain holds stepwise: tr(Phi(a)^dag Phi(a)) <= tr(Phi(a^dag a)) = tr(a^dag a)",
      ok_chain, "Schwarz (unitality) then trace preservation")

# ----------------------------------------------------------------------------
print("\nPART C -- hostile witnesses: both hypotheses of T1 are load-bearing")
print("=" * 78)
g = 0.4
K0 = np.diag([1.0, np.sqrt(1 - g)])
K1 = np.zeros((2, 2))
K1[0, 1] = np.sqrt(g)
S_AD = np.kron(K0.conj(), K0) + np.kron(K1.conj(), K1)
tp_ok = np.allclose(K0.conj().T @ K0 + K1.conj().T @ K1, np.eye(2), atol=1e-12)
unital = np.allclose(K0 @ K0.conj().T + K1 @ K1.conj().T, np.eye(2), atol=1e-12)
check("C1 drop unitality: amplitude damping (TP, NOT unital) has HS-norm > 1",
      tp_ok and (not unital) and np.linalg.norm(S_AD, 2) > 1 + 1e-3,
      f"HS-norm = {np.linalg.norm(S_AD,2):.5f}")
found, nval = False, 0.0
for _ in range(300):
    d, k = 2, 3
    A = RNG.normal(size=(d * k, d)) + 1j * RNG.normal(size=(d * k, d))
    V, _ = np.linalg.qr(A)
    Sup = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            E = np.zeros((d, d))
            E[i, j] = 1
            Sup[:, i * d + j] = (V.conj().T @ np.kron(E, np.eye(k)) @ V).reshape(-1)
    nrm = np.linalg.norm(Sup, 2)
    if nrm > 1 + 1e-6:
        found, nval = True, nrm
        break
check("C2 drop trace preservation: a unital CP non-TP map with HS-norm > 1 exists (witness found)",
      found, f"HS-norm = {nval:.5f}: both T1 hypotheses are load-bearing")

# ----------------------------------------------------------------------------
print("\nPART D -- T2: the peripheral unitary summand of a contraction")
print("=" * 78)
ok_eq, ok_orth, ok_split = True, True, True
for _ in range(20):
    d1, d2 = int(RNG.integers(1, 3)), int(RNG.integers(2, 4))
    Uper = rand_unitary(d1)
    Ccnu = RNG.normal(size=(d2, d2)) + 1j * RNG.normal(size=(d2, d2))
    Ccnu = 0.7 * Ccnu / np.linalg.norm(Ccnu, 2)
    W = rand_unitary(d1 + d2)
    T = W @ np.block([[Uper, np.zeros((d1, d2))], [np.zeros((d2, d1)), Ccnu]]) @ W.conj().T
    ev, vec = np.linalg.eig(T)
    for i, l in enumerate(ev):
        if abs(abs(l) - 1) < 1e-9:
            x = vec[:, i]
            # the contraction equality case: T^dag x = conj(lambda) x
            ok_eq &= np.allclose(T.conj().T @ x, np.conj(l) * x, atol=1e-8)
    per_idx = [i for i, l in enumerate(ev) if abs(abs(l) - 1) < 1e-9]
    cnu_ev = [l for l in ev if abs(abs(l) - 1) > 1e-9]
    ok_split &= len(per_idx) == d1 and (max(abs(np.array(cnu_ev))) < 0.99 if cnu_ev else True)
check("D1 unimodular eigenvectors of a contraction are joint T^dag eigenvectors (the equality case)",
      ok_eq, "the mechanism that makes the peripheral part an orthogonal reducing summand")
check("D2 the split T = U_per (+) T_cnu holds with cnu spectral radius < 1 (20 constructed contractions)",
      ok_split)

# ----------------------------------------------------------------------------
print("\nPART E -- T3: the canonical conjugacy lives on the summand (C derived there)")
print("=" * 78)
ok_conj = True
for _ in range(20):
    d1 = int(RNG.integers(2, 5))
    Uper = rand_unitary(d1)
    lam, Wf = np.linalg.eig(Uper)
    Winv = np.linalg.inv(Wf)
    M = Wf @ np.conj(Winv @ Uper @ Wf) @ Winv
    ok_conj &= np.allclose(M, np.linalg.inv(Uper), atol=1e-8)
check("E1 Theta = W o K o W^{-1} on the peripheral summand gives Theta U_per Theta^{-1} = U_per^{-1}",
      ok_conj, "the spectrum-reflection cycle's converse: C holds on the summand with NO transport premise")

# ----------------------------------------------------------------------------
print("\nPART F -- T4: large-separation data factors through the peripheral summand")
print("=" * 78)
omega, rho_cnu = 0.9, 0.5
w1, w2 = 0.7, 0.3
Cfun = lambda n: w1 * np.exp(-1j * omega * n) + w2 * (rho_cnu * np.exp(-1j * 0.4)) ** n
errs = []
for n0 in (2, 6, 10):
    c0, c1 = Cfun(n0), Cfun(n0 + 1)
    err = abs(abs(np.angle(c1 / c0)) - omega)
    errs.append((n0, err))
ok_geo = all(err < 2.0 * (w2 / w1) * rho_cnu ** n0 for n0, err in errs) and errs[0][1] > errs[1][1] > errs[2][1]
check("F1 asymptotic window recovery error tracks the cnu suppression rho^{n0} (offsets 2, 6, 10)",
      ok_geo, "; ".join(f"n0={n0}: err={err:.2e} (bound {2.0*(w2/w1)*rho_cnu**n0:.2e})" for n0, err in errs))
# fully cnu tick: nothing survives at large separation
Cdead = lambda n: (rho_cnu * np.exp(-1j * 0.4)) ** n
check("F2 hostile witness: a fully cnu tick's covariance dies geometrically -- no band for the chain to read",
      abs(Cdead(12)) < 1e-3 and abs(Cdead(2)) > 1e-2,
      "band persistence = the peripheral summand is nonempty: the sharpened P4 residual")

# ----------------------------------------------------------------------------
print("\nPART G -- composition with the transcription cycle (no tension)")
print("=" * 78)
for eps in (0.3, 0.15):
    c, s = np.cos(eps) ** 2, np.sin(eps) ** 2
    # sigma_x-dephasing channel: Kraus {cos(e) I, sin(e) sigma_x}: doubly stochastic
    Sdeph = c * np.eye(4) + s * np.kron(SX.conj(), SX)
    ok_ds = abs(np.linalg.norm(Sdeph, 2) - 1) < 1e-10
    M = np.array([[np.cos(0.9), -np.sin(0.9)], [np.sin(0.9), np.cos(0.9)]]) @ np.diag([1.0, np.cos(2 * eps)])
    evM = np.abs(np.linalg.eigvals(M))
    check(f"G[eps={eps}] the transcription model's channel is doubly stochastic (HS-norm 1); its registered sector is a strict contraction (peripheral part empty for eps > 0)",
          ok_ds and np.all(evM < 1 - 1e-6) and np.linalg.norm(M, 2) <= 1 + 1e-12,
          f"|eig M| = {np.round(evM,5)}: the faithful limit eps -> 0 is the peripheral restoration")

print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
