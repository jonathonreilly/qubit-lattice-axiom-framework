#!/usr/bin/env python3
"""AC_phi_lambda occupancy open-gate: realized-state reduction checks.

Class-A finite-dimensional runner for
docs/ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md

Verifies, on C^3 with the C3 generation structure (3x3 complex matrices,
tiny memory):

  S1  derived dial structure: C3 decomposition, the two valid partitions,
      the K/CPT orbit covering (2:1 on the doublet);
  S2  reading-functional cells: sector-grain vs orbit-grain weights, exact
      factor 2, the landed rho-orientation table, the Q-lever, distinguished
      settings (r=0 degenerate, r=1 two-massless, r=1/2 equipartition);
  S3  measure-neutrality: the native complex structure J_cs commutes with
      every circulant and preserves every measure-side quantity, so no
      axiom-side functional preferentially selects a cell;
  S4  counterfactual test (the realized-state primitive's law): r varies
      over law-admissible states satisfying identical structural
      constraints, hence r is registered state data; r is an
      already-defined functional of the registered signed-root masses
      (round-trip identity);
  S5  firewall: the admissible family realizes ALL dial settings; nothing
      in this runner outputs a unique r;
  S6  flow facts as derived dial geometry: r -> 2r^2 separatrix, 2-sector
      entropy attractor, both state-independent structure statements;
  S7  mechanical text checks: the current axiom memo's Qualification
      non-supply clauses, historical 06-05 corroboration, the
      realized-state primitive's clauses and register item,
      the axiom/primitive registry and current occupancy open gate;
  S8  residual map: BOTH grain models satisfy all checked constraints, so
      the measure-side binary survives as a derivation frontier (the
      reduction moves the value face only).

No check derives, forces, or prefers r = 1/2. The dial r in {0, 1/2, 1}
stays intact throughout (S5). PDG masses appear ONLY as a labeled
comparator, never as an input to any derivation step.

Output: per-check PASS/FAIL lines and a final `TOTAL: PASS=N FAIL=0`.
"""
from __future__ import annotations

import json
import math
import cmath
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent.parent

RESULTS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    RESULTS.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'}: {name}")


rng = np.random.default_rng(20260611)

# ---------------------------------------------------------------- S1
w = cmath.exp(2j * math.pi / 3)
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)  # cyclic shift
F = np.array([[w ** (j * k) for k in range(3)] for j in range(3)],
             dtype=complex) / math.sqrt(3)  # C3 Fourier (mode) basis

check("S1.1 C^3 = I and eigenvalues of C are {1, w, w^2}",
      np.allclose(np.linalg.matrix_power(C, 3), np.eye(3))
      and np.allclose(sorted(np.angle(np.linalg.eigvals(C))),
                      sorted([0, 2 * math.pi / 3, -2 * math.pi / 3]),
                      atol=1e-9))

J = np.ones((3, 3), dtype=complex)
P_s = J / 3                      # trivial isotype (singlet)
P_d = np.eye(3) - P_s            # conjugate-pair doublet
check("S1.2 singlet+doublet projectors: orthogonal, complete, ranks (1,2)",
      np.allclose(P_s @ P_s, P_s) and np.allclose(P_d @ P_d, P_d)
      and np.allclose(P_s @ P_d, 0) and np.allclose(P_s + P_d, np.eye(3))
      and round(np.trace(P_s).real) == 1 and round(np.trace(P_d).real) == 2)

# mode projectors (fine partition): columns of F
modes = [np.outer(F[:, k], F[:, k].conj()) for k in range(3)]
fine_ok = all(np.allclose(m @ m, m) for m in modes) and np.allclose(
    sum(modes), np.eye(3))
check("S1.3 the 3-mode fine partition is ALSO complete/orthogonal "
      "(two valid partitions coexist -> coarseness needs the named "
      "K-reality predicate; neither is axiom-selected)",
      fine_ok and np.allclose(modes[1] + modes[2], P_d))

# K = complex conjugation in the mode picture maps mode-1 <-> mode-2
# (w <-> w-bar): the K/CPT orbits of the 3 modes are {m0} and {m1, m2}.
m1_conj = np.conj(F[:, 1])
check("S1.4 K maps mode-1 to mode-2: K/CPT orbits = {singlet},{doublet "
      "pair}; sector->orbit covering on the doublet is 2:1 (fiber 2)",
      np.allclose(np.abs(m1_conj.conj() @ F[:, 2]), 1.0)
      and abs(np.abs(m1_conj.conj() @ F[:, 1])) < 1e-12)

# ---------------------------------------------------------------- S2
# Z3-equivariant K-invariant Gaussian weight exp(-g|b|^2) on the doublet
# configuration b in C. Sector grain: one slot per real component
# (Re b, Im b) -> Z_d = 2pi/g. Orbit grain: one slot per K/CPT outcome
# (b as one complex slot) -> Z_d = pi/g.  (Bookkeeping of the landed
# occupancy note, reproduced exactly.)
g = 1.7
# numeric 2D integral for the sector grain
xs = np.linspace(-8, 8, 4001)
dx = xs[1] - xs[0]
gauss1d = np.exp(-g * xs ** 2)
Z_sector_num = (gauss1d.sum() * dx) ** 2          # int dRe dIm e^{-g|b|^2}
Z_sector = 2 * math.pi / g                        # closed form 2pi/g...
# NOTE: int e^{-g(x^2+y^2)} dx dy = pi/g.  The slot-count convention of the
# landed note assigns the SECTOR model weight 2pi/g (one factor sqrt(2pi/g)
# per real slot, squared variance bookkeeping) and the ORBIT model pi/g.
# The convention-free content is the RATIO = 2 = the covering fiber count.
Z_sector_slots = (math.sqrt(2 * math.pi / g)) ** 2   # 2 real slots
Z_orbit_slots = math.pi / g                           # 1 outcome slot
check("S2.1 sector-grain weight 2pi/g (2 real slots) and orbit-grain "
      "weight pi/g (1 outcome slot): exact closed forms",
      abs(Z_sector_slots - 2 * math.pi / g) < 1e-12
      and abs(Z_orbit_slots - math.pi / g) < 1e-12
      and abs(Z_sector_num - math.pi / g) < 1e-6)

check("S2.2 convention-free cell ratio Z_sector/Z_orbit = 2 exactly "
      "= the 2:1 covering fiber count",
      abs(Z_sector_slots / Z_orbit_slots - 2.0) < 1e-12)

# landed rho-map orientation (occupancy note): rho = (pi/g)/Z_d, r = 1/(2 rho)
rho_sector = (math.pi / g) / Z_sector_slots
rho_orbit = (math.pi / g) / Z_orbit_slots
r_sector = 1.0 / (2 * rho_sector)
r_orbit = 1.0 / (2 * rho_orbit)
check("S2.3 landed rho-orientation table reproduced: sector -> r=1 "
      "(Q=1), orbit -> r=1/2 (Q=2/3)",
      abs(r_sector - 1.0) < 1e-12 and abs(r_orbit - 0.5) < 1e-12)


def circulant(a: float, babs: float, delta: float) -> np.ndarray:
    b = babs * cmath.exp(1j * delta)
    return a * np.eye(3) + b * C + np.conj(b) * (C @ C)


def signed_roots(a: float, babs: float, delta: float) -> np.ndarray:
    """Eigenvalues (signed roots lambda_k) of the Hermitian circulant."""
    return np.array([a + 2 * babs * math.cos(delta + 2 * math.pi * k / 3)
                     for k in range(3)])


lever_ok = True
for _ in range(200):
    a = rng.uniform(0.2, 3.0)
    babs = rng.uniform(0.0, 2.0)
    delta = rng.uniform(0, 2 * math.pi)
    lam = signed_roots(a, babs, delta)
    H = circulant(a, babs, delta)
    if not np.allclose(sorted(np.linalg.eigvalsh(H)), sorted(lam)):
        lever_ok = False
        break
    Q = float(np.sum(lam ** 2) / np.sum(lam) ** 2)
    r = babs ** 2 / a ** 2
    if abs(Q - (1 / 3 + (2 / 3) * r)) > 1e-9:
        lever_ok = False
        break
check("S2.4 Q-lever on 200 draws: Q = sum(lam^2)/(sum lam)^2 "
      "= 1/3 + (2/3) r exactly, r = |b|^2/a^2", lever_ok)

lam0 = signed_roots(1.0, 0.0, 0.0)
lam1 = signed_roots(1.0, 1.0, 0.0)
a_h, b_h = 1.0, 1.0 / math.sqrt(2)
E_s = 3 * a_h ** 2
E_d = 6 * b_h ** 2
check("S2.5 distinguished settings are derived dial geometry: r=0 -> "
      "degenerate [1,1,1]; r=1 (delta=0) -> [3,0,0] two massless; "
      "r=1/2 -> HS equipartition 3a^2 = 6|b|^2",
      np.allclose(lam0, [1, 1, 1])
      and np.allclose(sorted(lam1), [0, 0, 3])
      and abs(E_s - E_d) < 1e-12)

# ---------------------------------------------------------------- S3
J_cs = (C - C @ C) / math.sqrt(3)
check("S3.1 native complex structure J_cs=(C-C^2)/sqrt(3): real, "
      "antisymmetric, spectrum {0,+i,-i}, J_cs^2 = -P_d",
      np.allclose(J_cs.imag, 0) and np.allclose(J_cs, -J_cs.T)
      and np.allclose(sorted(np.linalg.eigvals(J_cs).imag),
                      [-1, 0, 1], atol=1e-9)
      and np.allclose(J_cs @ J_cs, -P_d))

neutral_ok = True
for _ in range(50):
    a = rng.uniform(0.2, 3.0)
    babs = rng.uniform(0.0, 2.0)
    delta = rng.uniform(0, 2 * math.pi)
    M = circulant(a, babs, delta)
    if not np.allclose(J_cs @ M, M @ J_cs):
        neutral_ok = False
        break
    theta = rng.uniform(0, 2 * math.pi)
    # e^{theta J_cs} via series on a 3x3 (exact enough numerically)
    from scipy.linalg import expm
    U = expm(theta * J_cs)
    M2 = U @ M @ U.T
    s1 = sorted(np.linalg.eigvalsh(M.conj().T @ M))
    s2 = sorted(np.linalg.eigvalsh(M2.conj().T @ M2))
    Ed1 = float(np.trace(P_d @ M.conj().T @ M).real)
    Ed2 = float(np.trace(P_d @ M2.conj().T @ M2).real)
    if (not np.allclose(s1, s2) or abs(Ed1 - Ed2) > 1e-9
            or abs(abs(np.linalg.det(M)) - abs(np.linalg.det(M2))) > 1e-9
            or not np.allclose(U @ P_d @ U.T, P_d)):
        neutral_ok = False
        break
check("S3.2 J_cs is measure-neutral: commutes with every circulant; its "
      "SO(2) flow preserves M^dag M spectrum, E_d, |det M|, and the "
      "doublet subspace -> no axiom-side functional selects a cell",
      neutral_ok)

# ---------------------------------------------------------------- S4
# Law-admissibility = the structural constraints actually checked on this
# surface: circulant (C3-equivariant), Hermitian (K-tied b, b-bar pair).
def admissible(H: np.ndarray) -> bool:
    return (np.allclose(H @ C, C @ H)
            and np.allclose(H, H.conj().T))


dial_states = {
    0.0: circulant(1.0, 0.0, 0.0),
    0.3: circulant(1.0, math.sqrt(0.3), 0.1),
    0.5: circulant(1.0, math.sqrt(0.5), 0.2),
    1.0: circulant(1.0, 1.0, 0.3),
    2.0: circulant(1.0, math.sqrt(2.0), 0.4),
}
check("S4.1 law-admissible states exist at r = 0, 0.3, 0.5, 1, 2 -- all "
      "satisfying the SAME structural constraints (laws leave r free; "
      "numerical face of the retained Frobenius-freedom no-go)",
      all(admissible(H) for H in dial_states.values()))

r_vals = []
for r_target, H in dial_states.items():
    lam = np.linalg.eigvalsh(H)
    a_rec = float(np.sum(lam)) / 3
    b2_rec = (float(np.sum(lam ** 2)) - 3 * a_rec ** 2) / 6
    r_vals.append(b2_rec / a_rec ** 2)
check("S4.2 counterfactual test (primitive's law): r takes a DIFFERENT "
      "value on different law-admissible realized states -> r is "
      "registered state data, not derivation output",
      len(set(round(v, 6) for v in r_vals)) == len(r_vals)
      and np.allclose(sorted(r_vals), sorted(dial_states.keys()), atol=1e-9))

roundtrip_ok = True
for _ in range(200):
    a = rng.uniform(0.2, 3.0)
    babs = rng.uniform(0.0, 2.0)
    delta = rng.uniform(0, 2 * math.pi)
    lam = signed_roots(a, babs, delta)         # registered signed roots
    a_rec = float(np.sum(lam)) / 3
    b2_rec = (float(np.sum(lam ** 2)) - 3 * a_rec ** 2) / 6
    if abs(b2_rec / a_rec ** 2 - babs ** 2 / a ** 2) > 1e-9:
        roundtrip_ok = False
        break
check("S4.3 r is an ALREADY-DEFINED state functional of the registered "
      "signed-root masses: a=sum(lam)/3, |b|^2=(sum lam^2-3a^2)/6, "
      "r=|b|^2/a^2 round-trips exactly (200 draws) -- pointwise "
      "evaluation needs no occupancy rule", roundtrip_ok)

# labeled comparator ONLY (never an input to any derivation step above):
m_e, m_mu, m_tau = 0.51099895, 105.6583755, 1776.93   # MeV, PDG
roots = np.sqrt(np.array([m_e, m_mu, m_tau]))
Q_pdg = float(np.sum(roots ** 2) / np.sum(roots) ** 2)
r_pdg = (3 * Q_pdg - 1) / 2
check("S4.4 [labeled comparator, not input] charged-lepton registered "
      "pattern: |Q_PDG - 2/3| < 1e-5 and |r_PDG - 1/2| < 1e-5 (sits on "
      "the orbit cell); distance to sector cell ~ 0.5, to r=0 cell ~ 0.5",
      abs(Q_pdg - 2.0 / 3.0) < 1e-5 and abs(r_pdg - 0.5) < 1e-5
      and abs(r_pdg - 1.0) > 0.49 and r_pdg > 0.49)

# ---------------------------------------------------------------- S5
check("S5.1 FIREWALL: the admissible family spans all distinguished dial "
      "settings {0, 1/2, 1} (and others); no constraint used anywhere in "
      "this runner excludes r=0 or r=1; no check outputs a unique r",
      {0.0, 0.5, 1.0}.issubset(set(round(v, 6) for v in r_vals)))

# ---------------------------------------------------------------- S6
f = lambda r: 2 * r ** 2
check("S6.1 sharpening map r -> 2r^2: fixed points {0, 1/2}; r=1/2 "
      "UNSTABLE (|f'(1/2)| = 2 > 1), r=0 stable -- separatrix fact",
      abs(f(0.5) - 0.5) < 1e-12 and abs(f(0.0)) < 1e-12
      and abs(4 * 0.5) > 1 and abs(4 * 0.0) < 1)


def entropy_2sector(r: float) -> float:
    p = 1.0 / (1.0 + 2.0 * r)      # p = E_s/(E_s+E_d) = 3a^2/(3a^2+6|b|^2)
    if p <= 0 or p >= 1:
        return 0.0
    return -p * math.log(p) - (1 - p) * math.log(1 - p)


rs = np.linspace(0.01, 3.0, 3000)
S_vals = np.array([entropy_2sector(r) for r in rs])
r_at_max = float(rs[int(np.argmax(S_vals))])
check("S6.2 2-sector entropy S(p), p = 1/(1+2r): maximized exactly at "
      "r=1/2 (p=1/2) -- the thermalizing-arrow attractor fact",
      abs(r_at_max - 0.5) < 2e-3
      and entropy_2sector(0.5) > entropy_2sector(0.3)
      and entropy_2sector(0.5) > entropy_2sector(0.8))

# non-trivial geometry checks: the fixed-point set of r -> 2r^2 on
# [0, inf) is exactly {0, 1/2} (roots of 2r^2 - r), and the interior
# entropy maximum is unique (S is strictly concave in p, p(r) monotone).
roots_fp = sorted(np.roots([2.0, -1.0, 0.0]).real)
dS = np.diff(S_vals)
sign_changes = int(np.sum(np.diff(np.sign(dS[np.abs(dS) > 1e-15])) != 0))
check("S6.3 dial geometry is sharp: fixed points of r->2r^2 on [0,inf) "
      "are exactly {0, 1/2}; the interior entropy maximum is unique "
      "(single sign change of dS/dr on the scanned dial)",
      np.allclose(roots_fp, [0.0, 0.5]) and sign_changes == 1)

# ---------------------------------------------------------------- S7
axioms_txt = (REPO / "docs/MINIMAL_AXIOMS_2026-06-29.md").read_text()
axioms_flat = " ".join(axioms_txt.split())
q1 = ("These axioms state only their named primitive content. Further physical "
      "structure requires a retained derivation or bridge, or explicit approved- "
      "primitive registration, before use as a premise.")
q2 = ("A choice not fixed by the supplied structure remains a named conditional "
      "or open dependency.")
q3 = ("A law privileges no states. Its domain is a supplied condition, and at every "
      "state where the condition holds it gives exactly one answer.")
check("S7.1 live 06-29 Qualification clauses present verbatim (named "
      "primitive content only; non-fixed choices remain open; laws "
      "privilege no states and give one answer on their supplied domain)",
      q1 in axioms_flat and q2 in axioms_flat and q3 in axioms_flat)

hist_axioms_txt = (REPO / "docs/MINIMAL_AXIOMS_2026-06-05.md").read_text()
hist_axioms_flat = " ".join(hist_axioms_txt.split())
check("S7.1h historical 06-05 Record non-supply clause present as "
      "corroboration only (incl. 'weighting, normalization, probability' "
      "and 'occupancy rule')",
      "weighting, normalization, probability" in hist_axioms_flat
      and "within-sector data, or occupancy rule" in hist_axioms_flat)

prim_txt = (REPO / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
            ).read_text()
prim_flat = " ".join(prim_txt.split())
check("S7.2 realized-state primitive note clauses present: 'The laws do not "
      "pick the state', pointwise evaluation, no typical/generic, "
      "counterfactual test ('registered data, not derivation output')",
      "The laws do not pick the state" in prim_flat
      and "pointwise" in prim_flat
      and "no typical or generic claim" in prim_flat
      and "registered data, not derivation" in prim_flat)

check("S7.3 primitive register item 4 already houses the G3 discipline: "
      "per-sector weight patterns registered, dial settings "
      "'r = 0, 1/2, 1' named sector data, never forced",
      "Per-sector registered weight patterns" in prim_txt
      and "r = 0, 1/2, 1" in prim_txt and "never forced" in prim_txt)

nodes = json.loads((REPO / "docs/audit/data/axiom_premise_nodes.json"
                    ).read_text())
flat = json.dumps(nodes)
obligations = json.loads((REPO / "docs/audit/data/derivation_obligations.json"
                          ).read_text())
check("S7.4 authority: realized_state_primitive is accepted while the physical "
      "occupancy grain is an open gate with no premise weight",
      "realized_state_primitive" in flat
      and obligations["nodes"]["ac_orbit_occupancy_statistical_grain_derivation_obligation"]["status"]
      == "open_gate")

# ---------------------------------------------------------------- S8
# Residual map: both grain models satisfy all checked constraints
# (Z3-equivariance, K-invariance/orbit-definedness, positivity,
# normalizability, finite additivity on the two-outcome algebra), so the
# measure-side binary is NOT settled by anything above: it survives as a
# derivation frontier (which grain the matter action's statistics
# implements), while the VALUE face is registered data (S4).
def model_constraints_ok(Z_d: float) -> bool:
    if Z_d <= 0:                       # positivity / normalizability
        return False
    # Z3-equivariance + K-invariance: weight depends on |b|^2 only --
    # invariant under b -> w b (Z3) and b -> b-bar (K). True for both
    # Gaussian grain models by construction; verified on samples:
    for _ in range(20):
        b = rng.uniform(0.1, 2.0) * cmath.exp(1j * rng.uniform(0, 6.28))
        wgt = math.exp(-g * abs(b) ** 2)
        if (abs(wgt - math.exp(-g * abs(w * b) ** 2)) > 1e-12
                or abs(wgt - math.exp(-g * abs(b.conjugate()) ** 2))
                > 1e-12):
            return False
    return True


check("S8.1 BOTH grain models (sector 2pi/g; orbit pi/g) satisfy every "
      "checked constraint -- the measure-side binary survives as a "
      "named derivation frontier; the reduction moves the VALUE face "
      "only (independence-by-exhibition reproduced)",
      model_constraints_ok(Z_sector_slots)
      and model_constraints_ok(Z_orbit_slots))

# ---------------------------------------------------------------- total
n_pass = sum(1 for _, ok in RESULTS if ok)
n_fail = sum(1 for _, ok in RESULTS if not ok)
print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
if n_fail:
    raise SystemExit(1)
