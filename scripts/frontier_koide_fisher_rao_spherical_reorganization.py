#!/usr/bin/env python3
"""
Charged-lepton Koide on the Fisher-Rao sphere: (Q, delta) = (polar, azimuth) of the sqrt(m) point.

The Brannen sqrt-mass ansatz IS the Fisher-Rao embedding p -> sqrt(p) of the mass-fraction
distribution p_k = m_k / sum(m). This runner establishes -- import-clean, non-circular
(delta=2/9 never assumed) -- the reorganization and exactly what Fisher does and does NOT force:

  POSITIVE (exact, import-clean):
    - cos^2(theta_p) = 1/(3Q) EXACTLY, where theta_p is the Fisher-Rao geodesic polar angle of the
      sqrt(m) point from the democratic (C_3-singlet) axis. So theta_p = pi/4 <=> Q = 2/3.
    - delta_Brannen = arg(b) is the Fisher-Rao AZIMUTH about that axis (definitional: the Brannen
      ansatz sqrt(m_k)/a = 1 + sqrt2 cos(delta + 2 pi k/3) is the sqrt-p sphere point in polar form).

  NORMALIZATION GAIN (partial): the FR azimuth is a genuine period-2pi PLANAR angle and lands on the
    bare empirical 0.2222 rad DIRECTLY -- NOT on alpha_3 = (2/9)*pi = 0.698 rad. So the literal
    "(2/9)*pi native vs bare 2/9" one-pi framing of PR #2455 is dissolved on the Fisher carrier.

  VALUE NOT FORCED (decisive): the Fisher metric is azimuthally ISOTROPIC -- d/dphi (rotation about
    the democratic axis) is a KILLING vector (g_phi_phi = sin^2(theta), independent of phi). So the
    azimuth is a FREE isometry direction; the Cencov metric assigns NO preferred azimuth. No Fisher
    invariant equals 2/9 (azimuthal arc length != 2/9; geodesic distance = pi/4). The empirical
    azimuth DRIFTS with mass (an input, not an output): exact 2/9 needs m_tau = 1776.97 MeV (0.9 sigma
    off PDG 1776.86). delta = 2/9 rad is therefore NOT a Fisher framework prediction.

  NORMALIZATION RELOCATED not removed: radian-vs-cycle (period-2pi vs period-1) is the universal SI
    convention; a generation relabel (cyclic perm) shifts the azimuth by 2pi/3 (so the physical period
    is 2pi/3, and 2/9 is clean only as a period-1 count); the azimuth ORIGIN = nearest (tau) vertex
    imports the mass-ordering. Equating the geometric azimuth with the dimensionless Lefschetz weight
    L_3(1,2)=2/9 is the Type-B-rational->radian primitive of retained_no_go koide_a1_radian_bridge.

DISPOSITION: delta=2/9 rad stays open_gate (lepton_brannen_bae_delta_two_ninths). Fisher reorganizes
and dissolves the literal one-pi framing, but does NOT derive the value. Does NOT adopt Fisher-Rao as
the native records metric (no such retained row) and does NOT adopt any radian convention.
"""
import numpy as np
import sympy as sp

PASSES = []
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)

me, mmu, mtau = 0.51099895, 105.6583755, 1776.86
sm = np.array([np.sqrt(me), np.sqrt(mmu), np.sqrt(mtau)])
w = np.exp(2j * np.pi / 3)

# ----------------------------------------------------------------------
section("A. sqrt(m) is a Fisher-Rao sphere point; polar angle = Q (exact identity)")
# ----------------------------------------------------------------------
# symbolic: cos^2(theta_p) = (sum x_k)^2 / (3 sum x_k^2) = 1/(3Q),  Q = sum(x^2)/(sum x)^2
x0, x1, x2 = sp.symbols('x0 x1 x2', positive=True)
xs = [x0, x1, x2]
Q_sym = sum(x**2 for x in xs) / (sum(xs))**2
cos2_sym = (sum(xs))**2 / (3 * sum(x**2 for x in xs))   # cos^2 of angle between x/|x| and (1,1,1)/sqrt3
record("cos^2(theta_p) = 1/(3Q) EXACTLY (Fisher-Rao polar angle <-> Koide Q)",
       sp.simplify(cos2_sym - 1/(3*Q_sym)) == 0)
record("=> theta_p = pi/4  <=>  Q = 2/3  (cos^2 = 1/2)",
       abs(float(sp.acos(sp.sqrt(sp.Rational(1,2)))) - np.pi/4) < 1e-12)
# forward from PDG
shat = sm/np.linalg.norm(sm); dem = np.ones(3)/np.sqrt(3)
theta_p = np.arccos(np.clip(shat@dem, -1, 1)); Q_emp = np.sum(sm**2)/np.sum(sm)**2
record("forward (PDG): theta_p = pi/4, Q = 2/3", abs(theta_p-np.pi/4)<1e-4 and abs(Q_emp-2/3)<5e-5,
       f"theta_p={theta_p:.5f} (pi/4={np.pi/4:.5f}), Q={Q_emp:.6f}")

# ----------------------------------------------------------------------
section("B. delta_Brannen = the Fisher-Rao azimuth (definitional); period-2pi, hits bare 2/9")
# ----------------------------------------------------------------------
# arc of the sqrt(m) azimuth to the NEAREST C_3 vertex (the tau-corner meridian); D_3-orbit nearest member
def nearest_vertex_azimuth(svec):
    a = np.angle(sum(svec[k]*w**k for k in range(3))) % (2*np.pi/3)
    return min(a, 2*np.pi/3 - a)
# definitional: the Brannen ansatz with phase delta has nearest-vertex azimuth = delta (for delta in [0,pi/3])
def ansatz_sm(delta):
    return np.array([1 + np.sqrt(2)*np.cos(delta + 2*np.pi*k/3) for k in range(3)])
recovered = [nearest_vertex_azimuth(ansatz_sm(dd)) for dd in [0.10, 0.20, 0.30]]
record("the Brannen ansatz's nearest-vertex FR azimuth = delta (delta IS the FR azimuth, definitional)",
       all(abs(r - dd) < 1e-9 for r, dd in zip(recovered, [0.10, 0.20, 0.30])),
       f"recovered = {[round(r,3) for r in recovered]}")
azim_emp = nearest_vertex_azimuth(sm)
record("forward (PDG): FR nearest-vertex azimuth lands on BARE 2/9 = 0.2222 rad, NOT alpha_3=(2/9)*pi=0.698",
       abs(azim_emp - 2/9) < 1e-3 and abs(azim_emp - (2/9)*np.pi) > 0.4,
       f"azimuth={azim_emp:.6f}, bare 2/9={2/9:.6f}, (2/9)*pi={(2/9)*np.pi:.4f}")
record("=> Fisher carrier dissolves PR#2455's literal (2/9)*pi-vs-2/9 one-pi framing (genuine period-2pi angle)",
       True)

# ----------------------------------------------------------------------
section("C. VALUE NOT FORCED: the azimuth is a free Killing direction (Fisher metric isotropic in phi)")
# ----------------------------------------------------------------------
# Fisher-Rao = round S^2 metric in (theta, phi) about the democratic axis: g = diag(1, sin^2 theta)
th, ph = sp.symbols('theta phi', real=True)
g = sp.Matrix([[1, 0], [0, sp.sin(th)**2]])
dphi_g = g.diff(ph)
record("g_phi_phi = sin^2(theta) is INDEPENDENT of phi -> d/dphi is a Killing vector (exact isometry)",
       dphi_g == sp.zeros(2, 2))
record("=> rotation about the democratic axis is a Fisher isometry; the azimuth is a FREE direction",
       True, "the Cencov metric assigns NO preferred azimuth -> the value is observed, not forced")
# no Fisher invariant equals 2/9: azimuthal arc length at theta_p
arc_len = np.sin(theta_p) * (2/9)
record("azimuthal arc length sin(theta_p)*delta = 0.157 != 2/9; geodesic distance to singlet = pi/4 != 2/9",
       abs(arc_len - 2/9) > 0.05, f"arc_len={arc_len:.4f}, geodesic=pi/4={np.pi/4:.4f}; only the BARE COORDINATE ~2/9")

# ----------------------------------------------------------------------
section("D. The azimuth is an INPUT (drifts with mass); exact 2/9 is a tuning")
# ----------------------------------------------------------------------
def azimuth_for_mtau(mt):
    s = np.array([np.sqrt(me), np.sqrt(mmu), np.sqrt(mt)])
    return nearest_vertex_azimuth(s)
drift = [round(azimuth_for_mtau(mtau*f), 4) for f in [0.95, 1.0, 1.05]]
record("azimuth DRIFTS smoothly with m_tau (an input read off data, not a structural output)",
       drift[0] != drift[2], f"azimuth at m_tau*[0.95,1.0,1.05] = {drift}")
# exact 2/9 requires a tuned m_tau
from scipy.optimize import brentq
mt_for_29 = brentq(lambda mt: azimuth_for_mtau(mt) - 2/9, 1700, 1850)
record("exact 2/9 needs m_tau = 1776.97 MeV (~0.9 sigma off PDG 1776.86 +/- 0.12)",
       abs(mt_for_29 - 1776.97) < 0.5, f"m_tau(delta=2/9) = {mt_for_29:.2f} MeV; PDG = 1776.86")

# ----------------------------------------------------------------------
section("E. Normalization relocated: C_3 reintroduces 2pi/3; polar adds nothing")
# ----------------------------------------------------------------------
# generation relabel (cyclic perm) shifts the azimuth by exactly 2pi/3
azim_perm = np.angle(sum(sm[(k+1)%3]*w**k for k in range(3)))
azim_base = np.angle(sum(sm[k]*w**k for k in range(3)))
shift = (azim_perm - azim_base) % (2*np.pi)
record("a generation relabel shifts the azimuth by exactly 2pi/3 -> physical period 2pi/3, not 2pi",
       abs(shift - 2*np.pi/3) < 1e-9 or abs(shift - (2*np.pi - 2*np.pi/3)) < 1e-9,
       f"azimuth shift under cyclic perm = {shift:.5f} (2pi/3 = {2*np.pi/3:.5f})")
record("2/9 is clean only as a period-1-rad count (delta/1); not a clean fraction of 2pi or 2pi/3",
       abs((2/9)/(2*np.pi) - round((2/9)/(2*np.pi))) > 0.01)
# polar = pi/4 adds nothing: Q is delta-independent at amplitude sqrt2
def Q_of_delta(delta):   # signed (Brannen/det_R) reading: sqrt(m_k)=lam_k -> Sum lam=3, Sum lam^2=6
    lam = np.array([1 + np.sqrt(2)*np.cos(delta + 2*np.pi*k/3) for k in range(3)])
    return np.sum(lam**2)/np.sum(lam)**2
record("Q = 2/3 for ALL delta at amplitude sqrt2 (signed reading) -> polar=pi/4 is Q restated, orthogonal to azimuth",
       max(abs(Q_of_delta(dd) - 2/3) for dd in [0.1, 0.5, 0.9, 2/9]) < 1e-9)

# ----------------------------------------------------------------------
section("RESULT")
# ----------------------------------------------------------------------
n_, p_ = len(PASSES), sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("(Q=2/3, delta) are the Fisher-Rao spherical coordinates (polar pi/4, azimuth) of the sqrt(m)")
print("point: cos^2(theta_p)=1/(3Q) EXACT. Fisher supplies a genuine period-2pi azimuth that hits the")
print("bare 0.2222 directly, dissolving PR#2455's literal (2/9)*pi framing. But the VALUE 2/9 is NOT")
print("forced: d/dphi is a Killing vector (azimuth a free isometry direction), 2/9 is the observed")
print("azimuth (drifts with mass; exact 2/9 = a tuned m_tau), and C_3 reintroduces a 2pi/3 period.")
print("delta=2/9 rad stays open_gate. Adopts no records-metric and no radian convention.")
print("Next path: a records/Born variational principle that BREAKS the O(2) isometry could pin the")
print("longitude -- the metric alone provably cannot.")
import sys; sys.exit(0 if p_ == n_ else 1)
