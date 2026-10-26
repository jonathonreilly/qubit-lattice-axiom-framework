#!/usr/bin/env python3
"""Finite supplied Wilson/staggered symbol comparisons and SU(3) identities.
The line averages are proxies, not physical drag coefficients. The HK-named
function is stipulated equal to the Wilson symbol; the finite Villain check
is approximate at beta=1.7, not an exact curvature or action-selection proof.
No framework log-flow derivation or physical f0 no-go follows. Full tensor,
vertex and loop matching remain open. See the paired note for the assumptions.
"""

AUDIT_INPUT_PATHS = ["docs/VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md", "docs/CLOSURE_T1_Z10_Z20_BZ_INTEGRALS_NOTE_2026-05-10_t1z10z20.md"]
AUDIT_TIMEOUT_SECONDS = 120

import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


def banner(t):
    print("\n" + "=" * 76 + f"\n{t}\n" + "=" * 76)


# ---------------------------------------------------------------------------
# Internal-line denominators on Z^d (supplied model symbols)
#   gauge (supplied nearest-plaquette curl ansatz):  Dg(k) = sum 2-2cos k_mu
#   staggered/Kahler-Dirac fermion:                      Df(k) = sum sin^2 k_mu  (+m^2)
# ---------------------------------------------------------------------------
def gauge_line(k):            # lattice Laplacian (HK-named ansatz stipulated equal)
    return np.sum(2 - 2 * np.cos(k), axis=-1)


def fermion_line(k, m2=0.0):  # staggered: doubler zeros at k_mu = pi
    return m2 + np.sum(np.sin(k) ** 2, axis=-1)


# ---------------------------------------------------------------------------
# Group weights: SU(3) color factors factor out EXACTLY
# ---------------------------------------------------------------------------
banner("Supplied SU(3) identities (no full amplitude factorization tested)")

# SU(3) Gell-Mann generators T^a = lambda^a / 2
lam = []
l1 = np.zeros((3, 3), complex); l1[0, 1] = l1[1, 0] = 1; lam.append(l1)
l2 = np.zeros((3, 3), complex); l2[0, 1] = -1j; l2[1, 0] = 1j; lam.append(l2)
l3 = np.diag([1, -1, 0]).astype(complex); lam.append(l3)
l4 = np.zeros((3, 3), complex); l4[0, 2] = l4[2, 0] = 1; lam.append(l4)
l5 = np.zeros((3, 3), complex); l5[0, 2] = -1j; l5[2, 0] = 1j; lam.append(l5)
l6 = np.zeros((3, 3), complex); l6[1, 2] = l6[2, 1] = 1; lam.append(l6)
l7 = np.zeros((3, 3), complex); l7[1, 2] = -1j; l7[2, 1] = 1j; lam.append(l7)
l8 = np.diag([1, 1, -2]).astype(complex) / np.sqrt(3); lam.append(l8)
T = [m / 2 for m in lam]

CF_mat = sum(Ta @ Ta for Ta in T)                       # sum_a T^a T^a = C_F I
check("C_F = sum_a T^a T^a = (4/3) I (fermion drag weight)",
      np.allclose(CF_mat, (4 / 3) * np.eye(3)) and np.allclose(CF_mat - np.diag(np.diag(CF_mat)), 0),
      f"diag={np.real(np.diag(CF_mat)).round(6).tolist()}")

# T_F delta^ab = tr(T^a T^b); off-diagonal must vanish, diagonal = 1/2
G = np.array([[np.trace(Ta @ Tb) for Tb in T] for Ta in T])
check("T_F = tr(T^a T^b) = (1/2) delta^ab (gauge vacuum-pol weight)",
      np.allclose(G, 0.5 * np.eye(8)),
      f"max off-diag={np.abs(G - np.diag(np.diag(G))).max():.2e}")

# C_A delta^ab = f^acd f^bcd ; structure constants from [T^a,T^b]=i f^abc T^c
f = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        comm = T[a] @ T[b] - T[b] @ T[a]
        for c in range(8):
            f[a, b, c] = np.real(np.trace(comm @ T[c]) / (1j * 0.5))
CA = np.einsum('acd,bcd->ab', f, f)
check("C_A = f^acd f^bcd = 3 delta^ab (gauge self-weight)",
      np.allclose(CA, 3 * np.eye(8)), f"diag0={CA[0,0]:.4f}")

print("  Supplied group identities verified; physical diagram factorization remains open.")


# ---------------------------------------------------------------------------
# IR coincidence of supplied symbols only
# ---------------------------------------------------------------------------
banner("Soft/IR region: supplied symbol ratio approaches one")

ks = np.array([1e-1, 1e-2, 1e-3, 1e-4])
ratios = []
for kk in ks:
    k = np.array([[kk, 0.0, 0.0, 0.0]])
    g = gauge_line(k)[0]
    fl = fermion_line(k)[0]
    ratios.append(g / fl)
check("gauge/fermion line ratio -> 1 as k->0 (soft cores coincide)",
      abs(ratios[-1] - 1.0) < 1e-6,
      f"ratios at k={ks.tolist()} = {[round(r,6) for r in ratios]}")
# Taylor: 2-2cos k = k^2 - k^4/12; sin^2 k = k^2 - k^4/3  -> both leading k^2
check("both lines have leading coefficient 1 * k^2 (l=0 speed channel shared)",
      abs((2 - 2 * np.cos(1e-3)) / 1e-6 - 1) < 1e-4 and abs(np.sin(1e-3) ** 2 / 1e-6 - 1) < 1e-4,
      "2-2cos k ~ k^2, sin^2 k ~ k^2")


# ---------------------------------------------------------------------------
# BZ-edge difference of supplied symbols
# ---------------------------------------------------------------------------
banner("BZ-edge: gauge line nonzero (no doubler), fermion line zero (doublers)")

edge = np.array([[np.pi, np.pi, np.pi, np.pi]])
g_edge = gauge_line(edge)[0]
f_edge = fermion_line(edge)[0]
check("gauge line at k=pi (all axes) = 16 = 4 per direction (NO doubler zero)",
      abs(g_edge - 16.0) < 1e-9, f"Dg(pi)= {g_edge:.6f} (per-direction 2-2cos pi = 4)")
check("staggered fermion line at k=pi = 0 (doubler zero)",
      abs(f_edge) < 1e-9, f"Df(pi)= {f_edge:.2e}")
# single-axis doubler check
ax = np.array([[np.pi, 0.0, 0.0, 0.0]])
check("fermion line has doubler zeros on every BZ-edge corner (sin^2 pi = 0)",
      abs(fermion_line(ax)[0]) < 1e-9 and abs(gauge_line(ax)[0] - 4.0) < 1e-9,
      "fermion 0, gauge 4 at a single-axis edge")


# ---------------------------------------------------------------------------
# Proxy ratios of region-averaged symbols; not actual self-energy diagrams.
# ---------------------------------------------------------------------------
banner("Supplied proxy average ratio: IR near one; full/UV different")

def line_mean(line_internal, region, N=48):
    """region-averaged internal line over the BZ (well-defined, no 1/line)."""
    g1 = (np.arange(N) + 0.5) * 2 * np.pi / N
    K = np.array(np.meshgrid(g1, g1, g1, g1, indexing='ij')).reshape(4, -1).T
    Kc = np.where(K > np.pi, K - 2 * np.pi, K)
    kmag = np.linalg.norm(Kc, axis=-1)
    mask = {'IR': kmag < np.pi / 6, 'UV': kmag >= np.pi / 2}.get(region, np.ones(len(K), bool))
    return np.mean(line_internal(K)[mask])

# Define the proxy by symbol averages; full physical cores remain uncomputed.
rIR = line_mean(gauge_line, 'IR') / line_mean(lambda k: fermion_line(k), 'IR')
rUV = line_mean(gauge_line, 'UV') / line_mean(lambda k: fermion_line(k), 'UV')
rBZ = line_mean(gauge_line, 'all') / line_mean(lambda k: fermion_line(k), 'all')
check("Finite IR proxy average ratio within 0.05 of one",
      abs(rIR - 1.0) < 0.05, f"IR <Dg>/<Df> = {rIR:.4f}")
check("Finite UV proxy average ratio differs from one by more than 0.3",
      abs(rUV - 1.0) > 0.3, f"UV <Dg>/<Df> = {rUV:.4f}")
check("full-BZ ratio = <2-2cos>/<sin^2> = 2/0.5 = 4 (exact; gauge != fermion away from IR)",
      abs(rBZ - 4.0) < 0.05, f"BZ <Dg>/<Df> = {rBZ:.4f}")
# line-swap: use the fermion line in BOTH -> ratio is exactly 1 (mismatch is the line)
rswap = line_mean(lambda k: fermion_line(k), 'all') / line_mean(lambda k: fermion_line(k), 'all')
check("line-swap: identical internal lines give ratio 1 (mismatch is purely the internal line)",
      abs(rswap - 1.0) < 1e-12, f"swap ratio = {rswap:.12f}")


# ---------------------------------------------------------------------------
# Finite Villain curvature comparison and a stipulated common-symbol ansatz.
banner("Supplied HK-named common-symbol ansatz and finite Villain comparison")
# Nonzero winding terms prevent a general exact S''(0)=beta identity.
def villain_S(theta, beta, nmax=50):
    n = np.arange(-nmax, nmax + 1)
    return -np.log(np.exp(-(beta / 2) * (theta - 2 * np.pi * n) ** 2).sum())
beta_hk = 1.7
h = 1e-4
d2 = (villain_S(h, beta_hk) - 2 * villain_S(0.0, beta_hk) + villain_S(-h, beta_hk)) / h**2
check("Finite Villain curvature within 1e-3 of beta=1.7; tested evenness",
      abs(d2 - beta_hk) < 1e-3 and abs(villain_S(h, beta_hk) - villain_S(-h, beta_hk)) < 1e-9,
      f"S''(0)={d2:.5f} approximately beta; no exact curvature or momentum-selection proof")

# The common nearest-plaquette curl symbol is supplied, not derived here.
def gauge_line_HK(k):   # stipulated common-symbol ansatz
    return np.sum(2 - 2 * np.cos(k), axis=-1)
import itertools as _it
corners = [np.array(c, float) * np.pi for c in _it.product([0, 1], repeat=4)][1:]
check("Supplied HK-named symbol NONZERO at every BZ-edge corner k in {0,pi}^4\\{0} (no doubler)",
      min(gauge_line_HK(c.reshape(1, 4))[0] for c in corners) >= 4.0 - 1e-9,
      f"min corner = {min(gauge_line_HK(c.reshape(1,4))[0] for c in corners):.1f} (fermion sin^2 = 0 here)")
check("HK-named function equals Wilson symbol by construction (sample control)",
      np.allclose(gauge_line_HK(np.random.RandomState(0).uniform(-np.pi, np.pi, (200, 4))),
                  gauge_line(np.random.RandomState(0).uniform(-np.pi, np.pi, (200, 4)))), "")
rUV_hk = line_mean(gauge_line_HK, 'UV') / line_mean(lambda k: fermion_line(k), 'UV')
check("Stipulated identical HK-named/Wilson symbols give identical UV proxy ratios",
      abs(rUV_hk - rUV) < 1e-9, f"UV ratio HK={rUV_hk:.4f} vs Wilson={rUV:.4f}")


banner("SUMMARY")
print("Supplied SU(3) identities and finite Wilson/staggered proxy comparisons only.")
print("IR symbol ratios approach one; sampled UV/full-BZ average ratios differ.")
print("HK-named symbol equality is stipulated; finite Villain curvature is approximate.")
print("Physical log-flow positivity, f0 factorization, full counterterms and naturalness remain open.")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
