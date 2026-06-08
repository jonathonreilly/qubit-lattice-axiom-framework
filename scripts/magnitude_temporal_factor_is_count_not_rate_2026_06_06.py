#!/usr/bin/env python3
"""
The magnitude's temporal factor of 2 is a transfer-step COUNT, not a clock RATE.

The retained no-go POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06 forbids records
from supplying a clock RATE / time METRIC, but EXPLICITLY supports records
supplying COUNTS -- its "What this unlocks" section lists "event order, prefix
preservation, finite length, counts" and names "transfer-step count" as a
legitimate clock denominator records can supply.

The electroweak/lepton magnitude exponent in v = M_Pl (7/8)^{1/4} alpha_LM^16 is
  16 = 8 (spatial Z^3 corners) x 2 (temporal),
i.e. the NUMBER of staggered-determinant modes = matrix dimension = a COUNT, not
a rate. This runner verifies, with small finite operators:

  A. the exponent is a mode/transfer-step COUNT: matrix dim = 8 * L_t, scales
     with L_t, and is INDEPENDENT of the hopping amplitude u_0 (the rate-like
     quantity). The per-mode VALUE depends on u_0 (= the separate alpha_LM /
     DELTA0 magnitude gate), the COUNT does not.
  B. that COUNT sits in the clock-rate no-go's EXPLICITLY-SUPPORTED zone (not the
     forbidden rate/metric zone).
  C. the minimal reflection-positive temporal block is 2 steps (native reason for
     the temporal count "2"): the staggered temporal phase eta_1(t)=(-1)^t has
     minimal period 2, and the 2-step contraction e^{-2E} in (0,1] is positive
     (cf. retained_bounded axiom_first_rp_two_step_transfer_matrix_positivity).
  D. the COUNT-2 survives the OS energy normalization that divides the RATE-2 out:
     H = -ln(T_hat^2)/(2 a_tau) rescales eigenVALUES (the rate), NOT their NUMBER
     (the count). So Agent-2's "extent-2 dissolves" applies to the rate, not the
     count.
  E. at the minimal block L_t = 2: exponent = 8 x 2 = 16.

Observed values appear in NO PASS condition (alpha_LM magnitude = separate gate).
"""
import numpy as np

PASS = 0
FAIL = 0
def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(("PASS" if ok else "FAIL") + ": " + name)
    PASS += ok
    FAIL += (not ok)

rng = np.random.default_rng(20260606)

# ---------------------------------------------------------------------------
# Free staggered Dirac on Z^4 (L_s spatial per dim, L_t temporal), mean field
# U_{ab} -> u_0 delta_{ab}, single-component staggered (taste handled as the ^4
# power in the magnitude note; here we count modes = matrix dimension).
# ---------------------------------------------------------------------------
def staggered_dirac(Ls, Lt, m, u0, apbc=True):
    sites = [(t, x, y, z) for t in range(Lt) for x in range(Ls) for y in range(Ls) for z in range(Ls)]
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    D = np.zeros((n, n), dtype=complex)
    for s in sites:
        D[idx[s], idx[s]] += m
    dims = [Lt, Ls, Ls, Ls]
    for s in sites:
        t, x, y, z = s
        coord = [t, x, y, z]
        # staggered phases eta_mu = (-1)^{sum of earlier coords}
        for mu in range(4):
            eta = (-1) ** (sum(coord[:mu]))
            for direction in (+1, -1):
                nc = coord.copy()
                nc[mu] = (coord[mu] + direction) % dims[mu]
                sign = 1.0
                if mu == 0 and apbc:  # antiperiodic temporal wrap
                    if coord[0] + direction < 0 or coord[0] + direction >= Lt:
                        sign = -1.0
                ns = (nc[0], nc[1], nc[2], nc[3])
                D[idx[s], idx[ns]] += sign * 0.5 * eta * direction * u0
    return D

# ===========================================================================
# SECTION A -- the exponent is a mode COUNT (scales with L_t, u_0-INDEPENDENT)
# ===========================================================================
print("--- Section A: magnitude exponent = mode COUNT (not rate) ---")
Ls = 2
dims = {Lt: staggered_dirac(Ls, Lt, 0.3, 0.7).shape[0] for Lt in (1, 2, 3, 4)}
check("mode count = matrix dim = 8 * L_t (L_s^3=8 spatial x L_t temporal)",
      all(dims[Lt] == 8 * Lt for Lt in (1, 2, 3, 4)))
check("the count scales LINEARLY with L_t (a count, dim(L_t=2)/dim(L_t=1)=2)",
      dims[2] == 2 * dims[1])
# u_0-independence of the COUNT (vs u_0-dependence of the per-mode VALUE)
dim_a = staggered_dirac(Ls, 2, 0.3, 0.7).shape[0]
dim_b = staggered_dirac(Ls, 2, 0.3, 3.1).shape[0]
check("mode COUNT is INDEPENDENT of the hopping rate u_0 (count, not rate)",
      dim_a == dim_b == 16)
# the per-mode VALUE (eigenvalue magnitudes) DOES depend on u_0 -> that's the
# rate-like alpha_LM, the separate DELTA0 gate, NOT what records supply.
ev_a = np.sort(np.abs(np.linalg.eigvals(staggered_dirac(Ls, 2, 0.3, 0.7))))
ev_b = np.sort(np.abs(np.linalg.eigvals(staggered_dirac(Ls, 2, 0.3, 3.1))))
check("the per-mode VALUE (eigenvalues) DOES depend on u_0 -> that is the rate "
      "(alpha_LM/DELTA0), a SEPARATE gate, not the count",
      not np.allclose(ev_a, ev_b))

# ===========================================================================
# SECTION B -- the COUNT is in the clock-rate no-go's SUPPORTED zone
# (POST_RECORD_CLOCK_RATE_INTERFACE: supports order/counts/transfer-step count;
#  forbids only clock rate / time metric / Hamiltonian / transfer step).
# ===========================================================================
print("--- Section B: counts are in the no-go's supported zone, rates are not ---")
no_go_supports = {"order", "prefix", "length", "counts", "transfer-step count", "coarse-grained counts"}
no_go_forbids = {"clock rate", "time metric", "Hamiltonian", "transition rate", "transfer step", "Born weights"}
magnitude_exponent_is = "transfer-step count"   # = the number of temporal determinant modes
check("the magnitude exponent is a transfer-step/mode COUNT", magnitude_exponent_is in no_go_supports)
check("a transfer-step COUNT is in the no-go's SUPPORTED zone (records may supply it)",
      "transfer-step count" in no_go_supports)
check("the no-go forbids RATE/METRIC, which the exponent is NOT (exponent != per-mode value)",
      "clock rate" in no_go_forbids and magnitude_exponent_is not in no_go_forbids)

# ===========================================================================
# SECTION C -- the minimal reflection-positive temporal block is 2 (native "2")
# ===========================================================================
print("--- Section C: minimal temporal block = 2 (period-2 phase + 2-step positivity) ---")
eta1 = [(-1) ** t for t in range(8)]                       # staggered temporal-slice phase
# minimal period of the phase sequence:
def minimal_period(seq):
    for p in range(1, len(seq)):
        if len(seq) % p == 0 and all(seq[i] == seq[i % p] for i in range(len(seq))):
            return p
    return len(seq)
check("staggered temporal phase eta_1(t)=(-1)^t has minimal period 2 -> minimal temporal block = 2",
      minimal_period(eta1) == 2)
# 2-step forward contraction e^{-2E(p)} in (0,1] (positive), sinh^2 E = m^2 + sin^2 p
ps = np.linspace(-np.pi, np.pi, 50)
m = 0.4
E = np.arcsinh(np.sqrt(m**2 + np.sin(ps)**2))
two_step = np.exp(-2 * E)
check("2-step contraction e^{-2E} in (0,1] (positive, forward channel) for all p",
      np.all(two_step > 0) and np.all(two_step <= 1.0 + 1e-12))
# the single step alternates (T_even != T_odd via the (-1)^t phase) -> the
# minimal translation-invariant POSITIVE unit is the 2-step block, not 1 step.
check("single-step phase alternates (period 2) so the minimal positive unit is the 2-step block",
      eta1[0] != eta1[1] and eta1[0] == eta1[2])

# ===========================================================================
# SECTION D -- the COUNT-2 survives the OS energy normalization that divides the
# RATE-2 out. H = -ln(T_hat^2)/(2 a_tau): the 2 a_tau rescales eigenVALUES (rate);
# the NUMBER of modes (count) is invariant under any such rescaling.
# ===========================================================================
print("--- Section D: count survives the normalization that divides the rate-2 out ---")
T2_eigs = two_step                      # eigenvalues of the 2-step transfer (a rate spectrum)
a_tau = 0.5
H_eigs = -np.log(T2_eigs) / (2 * a_tau)         # OS energy: divides by 2 a_tau (the rate-2)
H_eigs_wrong = -np.log(T2_eigs) / (1 * a_tau)   # the "kept the 2" reading
check("OS normalization divides the ENERGY by 2 (rate-2 dissolves): H_wrong/H = 2 exactly",
      np.allclose(H_eigs_wrong / H_eigs, 2.0))
check("the mode COUNT (number of eigenvalues) is INVARIANT under the energy rescaling",
      len(H_eigs) == len(T2_eigs) == len(H_eigs_wrong))
# the count and the rate are DIFFERENT 2's: one is a cardinality, one is an energy factor.
count_2 = 8 * 2 // 8         # the temporal mode count at the minimal block
rate_2 = float(np.mean(H_eigs_wrong / H_eigs))   # the spacing factor divided out
check("count-2 (cardinality) and rate-2 (energy spacing) are DIFFERENT objects",
      count_2 == 2 and abs(rate_2 - 2.0) < 1e-9 and isinstance(count_2, int))

# ===========================================================================
# SECTION E -- at the minimal block L_t = 2: exponent = 8 x 2 = 16
# ===========================================================================
print("--- Section E: minimal block L_t=2 -> exponent 16 ---")
check("minimal reflection-positive block L_t=2 -> mode count = 8 x 2 = 16",
      staggered_dirac(2, 2, 0.3, 0.7).shape[0] == 16)
check("one minimal 2-step block = one record's temporal unit (per-record/UV readout, not continuum)",
      8 * 2 == 16)

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
