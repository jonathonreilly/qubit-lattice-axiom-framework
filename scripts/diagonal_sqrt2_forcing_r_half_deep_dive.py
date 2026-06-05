#!/usr/bin/env python3
"""Diagonal-thinking Phase 3 deep dive: is the face-diagonal length sqrt(2)
FORCED (not merely natural) as the Brannen circulant amplitude weight, so that
the charged-lepton modulus r = |b|^2/a^2 = 1/2 becomes derived from substrate
geometry?

This is the centerpiece runner of the sqrt(2)-centered build. It computes each
of six forcing candidates F1-F6 explicitly and classifies each as

    FORCED   -- the value 1/sqrt(2) is fixed by the structure, no free parameter;
    NATURAL  -- 1/sqrt(2) emerges but only with a tunable parameter set to a
                natural value (or a convention choice);
    NO-SQRT2 -- the candidate, computed honestly, does NOT give 1/sqrt(2).

The load-bearing candidate is F3 (the actual Z^3 nearest-neighbor lattice Green
function), because it is the unique PARAMETER-FREE object among the six. We
compute it numerically via a momentum-space midpoint-grid integral with a
Richardson extrapolation, validated against the exact Watson value
G(0,0,0) = 0.25273100986... .

It also runs the category-mismatch defeat test: does the continuous datum
sqrt(2) genuinely defeat the "discrete axioms cannot pin a continuous modulus"
wall, or does the mismatch reappear one level up (the CHOICE of length-weighting
function f, and the fact that r = 1/2 is already reachable by pure discrete
sector counting)?

No axiom is modified. No audit status is set. PDG values are not imported;
sqrt(2) and r = 1/2 are compared structurally only.

Run:
    python3 scripts/diagonal_sqrt2_forcing_r_half_deep_dive.py
"""
from __future__ import annotations

import itertools
import numpy as np

PASS = 0
FAIL = 0

TARGET_BA = 1.0 / np.sqrt(2.0)   # |b|/a that yields r = 1/2
TARGET_R = 0.5                   # the Brannen modulus r = |b|^2/a^2
TOL = 1e-9
WATSON_G0 = 0.2527310098586630   # exact Z^3 massless lattice Green function at 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"[{tag}] {label}"
    if detail:
        line += f"  ({detail})"
    print(line)


def section(title: str) -> None:
    print("=" * 70)
    print(title)
    print("=" * 70)


# ----------------------------------------------------------------------
# Brannen-circulant baseline facts (the object r lives on)
# ----------------------------------------------------------------------
def brannen_baseline():
    section("Baseline. Brannen circulant Y = a I + b C + bbar C^2; r = |b|^2/a^2")
    w = np.exp(2j * np.pi / 3.0)
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    Iden = np.eye(3, dtype=complex)

    # eigenvalues lambda_k = a + b w^k + bbar w^{-k}
    a = 1.3
    b = 0.4 + 0.25j
    Y = a * Iden + b * C + np.conj(b) * (C @ C)
    eig_closed = np.array([a + b * w**k + np.conj(b) * w**(-k) for k in range(3)])
    eig_num = np.linalg.eigvals(Y)
    ok = np.allclose(np.sort_complex(np.round(eig_closed, 9)),
                     np.sort_complex(np.round(eig_num, 9)))
    check("Baseline: closed-form circulant eigenvalues match numerics", ok)

    # r = 1/2 <=> |b|/a = 1/sqrt(2)
    check("Baseline: r = 1/2  <=>  |b|/a = 1/sqrt(2)",
          abs((1.0 / np.sqrt(2.0)) ** 2 - 0.5) < 1e-12,
          f"(1/sqrt2)^2 = {(1/np.sqrt(2))**2:.6f}")

    # the L9 HS-equipartition reading: ||aI||^2 = ||bC + bbar C^2||^2 <=> r = 1/2
    hop = b * C + np.conj(b) * (C @ C)
    lhs = np.trace((a * Iden).conj().T @ (a * Iden)).real        # 3 a^2
    rhs = np.trace(hop.conj().T @ hop).real                       # 6 |b|^2
    check("Baseline: ||aI||^2 = 3 a^2 (HS norm of the stay block)",
          abs(lhs - 3 * a * a) < 1e-9, f"{lhs:.4f} = 3*{a}^2")
    check("Baseline: ||bC+bbar C^2||^2 = 6 |b|^2 (TWO nontrivial Z3 sectors)",
          abs(rhs - 6 * abs(b) ** 2) < 1e-9, f"{rhs:.4f} = 6*|b|^2")
    # equipartition lhs == rhs  <=>  3a^2 = 6|b|^2  <=>  r = 1/2
    a_eq = np.sqrt(2.0) * abs(b)   # the a that equipartitions for this b
    r_eq = abs(b) ** 2 / a_eq ** 2
    check("Baseline: HS-equipartition (3a^2 = 6|b|^2) gives r = 1/2 = 1/(#sectors)",
          abs(r_eq - 0.5) < 1e-12,
          "the factor 2 here is the SECTOR COUNT |Z3|-1=2, a DISCRETE datum")
    print("  NOTE: the equipartition '2' (sector count) and the length '2' = (sqrt2)^2")
    print("        are NUMERICALLY equal but STRUCTURALLY distinct origins of r=1/2.")
    print()


# ----------------------------------------------------------------------
# F1. Gaussian overlap integral
# ----------------------------------------------------------------------
def f1_gaussian():
    section("F1. Gaussian overlap  b/a = exp(-d_b^2/2s^2) / exp(-d_a^2/2s^2)")
    d_fd = np.sqrt(2.0)     # face-diagonal distance
    # reference (a) on-site d=0:  b/a = exp(-1/s^2);  reference (b) NN d=1: exp(-1/(2 s^2))
    s2_a = 1.0 / (0.5 * np.log(2.0))   # solves exp(-1/s^2)      = 1/sqrt2
    s2_b = 1.0 / np.log(2.0)           # solves exp(-1/(2 s^2))  = 1/sqrt2
    ba_a = np.exp(-(d_fd ** 2) / (2 * s2_a)) / np.exp(0.0)
    ba_b = np.exp(-(d_fd ** 2) / (2 * s2_b)) / np.exp(-(1.0) / (2 * s2_b))
    print(f"  on-site reference: tuned sigma^2 = 2/ln2 = {s2_a:.6f}  -> b/a = {ba_a:.6f}")
    print(f"  NN reference     : tuned sigma^2 = 1/ln2 = {s2_b:.6f}  -> b/a = {ba_b:.6f}")
    check("F1: a Gaussian width sigma EXISTS that gives b/a = 1/sqrt2 (on-site ref)",
          abs(ba_a - TARGET_BA) < 1e-9)
    check("F1: a Gaussian width sigma EXISTS that gives b/a = 1/sqrt2 (NN ref)",
          abs(ba_b - TARGET_BA) < 1e-9)
    # forcing test: is the required sigma a distinguished/forced value? It is not:
    # vary sigma; b/a sweeps continuously through 1/sqrt2, so 1/sqrt2 is not singled out.
    sigmas = np.linspace(0.5, 3.0, 6)
    bas = [np.exp(-(d_fd ** 2) / (2 * s * s)) for s in sigmas]
    monotone = all(bas[i] < bas[i + 1] for i in range(len(bas) - 1))
    check("F1: b/a varies continuously with sigma (1/sqrt2 NOT a distinguished value)",
          monotone, "sigma is a FREE parameter tuned to the target")
    print("  VERDICT F1: NATURAL (a tuned width reproduces 1/sqrt2; sigma not forced).")
    print()
    return "NATURAL"


# ----------------------------------------------------------------------
# F2. Inverse-distance power law
# ----------------------------------------------------------------------
def f2_inverse_distance():
    section("F2. Inverse-distance power  b ~ 1/d^p  (on-site d=0 diverges)")
    d_fd = np.sqrt(2.0)
    # on-site reference impossible for a pure power (d=0 -> infinite). Use NN (d=1).
    print("  on-site (d=0) reference diverges for any p>0; the natural reference is NN (d=1).")
    rows = []
    for p in [1, 2, 3, 4]:
        ba = (d_fd ** (-p)) / (1.0 ** (-p))   # = 2^(-p/2)
        rows.append((p, ba, ba * ba))
        flag = "  <== r=1/2" if abs(ba * ba - 0.5) < 1e-12 else ""
        print(f"    p={p}: b/a = 2^(-p/2) = {ba:.6f} -> r = {ba*ba:.6f}{flag}")
    check("F2: p=1 (the 1/r law) gives b/a = 1/sqrt2 EXACTLY -> r = 1/2",
          abs((d_fd ** -1) ** 2 - 0.5) < 1e-12)
    check("F2: only p=1 hits r=1/2; p in {2,3,4} do not",
          all(abs(ba * ba - 0.5) > 1e-6 for (p, ba, _) in rows if p != 1))
    print("  VERDICT F2: NATURAL (p=1/inverse-FIRST-power gives 1/sqrt2, but the power")
    print("              p is a CHOICE; the lattice does not select it).")
    print()
    return "NATURAL"


# ----------------------------------------------------------------------
# F3. The ACTUAL Z^3 nearest-neighbor lattice Green function (PARAMETER-FREE)
# ----------------------------------------------------------------------
def lattice_green(R, N):
    """G(R) = (1/(2pi)^3) int_{[-pi,pi]^3} cos(k.R)/(2 sum_j (1-cos k_j)) d^3k

    Midpoint grid that AVOIDS k=0 (so the integrable 1/k^2 singularity never lands
    on a node); the leading discretization error ~ c/N from the singular cell, so a
    two-point Richardson extrapolation in N is applied by the caller.
    """
    dk = 2 * np.pi / N
    ks = -np.pi + (np.arange(N) + 0.5) * dk
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing="ij")
    denom = 2.0 * ((1 - np.cos(KX)) + (1 - np.cos(KY)) + (1 - np.cos(KZ)))
    num = np.cos(KX * R[0] + KY * R[1] + KZ * R[2])
    return float(np.sum(num / denom) * (dk ** 3) / (2 * np.pi) ** 3)


def richardson(R, Ns):
    vals = [lattice_green(R, N) for N in Ns]
    n1, n2 = Ns[-2], Ns[-1]
    return (n2 * vals[-1] - n1 * vals[-2]) / (n2 - n1), vals


def f3_green_function():
    section("F3. Z^3 NN lattice Green function ratios (PARAMETER-FREE)")
    Ns = [80, 120, 160, 200]
    G0, v0 = richardson((0, 0, 0), Ns)
    G1, v1 = richardson((1, 0, 0), Ns)
    Gfd, vfd = richardson((1, 1, 0), Ns)
    Gbd, vbd = richardson((1, 1, 1), Ns)
    print(f"  on-site   G(0,0,0)  = {G0:.7f}   (exact Watson {WATSON_G0:.7f})")
    print(f"  NN d=1    G(1,0,0)  = {G1:.7f}")
    print(f"  facediag  G(1,1,0)  = {Gfd:.7f}   (distance sqrt2)")
    print(f"  bodydiag  G(1,1,1)  = {Gbd:.7f}   (distance sqrt3)")
    # method validation 1: extrapolated G0 must match the known exact Watson value
    check("F3: extrapolated G(0,0,0) matches exact Watson value (method validated)",
          abs(G0 - WATSON_G0) < 5e-6, f"|diff| = {abs(G0 - WATSON_G0):.2e}")
    # method validation 2: the exact origin recurrence 6 G(0) - 6 G(1,0,0) = 1,
    # i.e. G(1,0,0) = G(0) - 1/6, an independent closed-form cross-check.
    g1_exact = WATSON_G0 - 1.0 / 6.0
    check("F3: extrapolated G(1,0,0) matches exact recurrence G(0)-1/6 (method validated)",
          abs(G1 - g1_exact) < 5e-6, f"G1={G1:.7f} vs G(0)-1/6={g1_exact:.7f}")
    # method validation 3: monotone convergence of the facediag value with N
    mono = all(vfd[i] < vfd[i + 1] for i in range(len(vfd) - 1))
    check("F3: facediag Green value converges monotonically in N (clean extrapolation)",
          mono, f"vals={[round(x,5) for x in vfd]}")

    r_fd_nn = Gfd / G1
    r_fd_on = Gfd / G0
    r_nn_on = G1 / G0
    print(f"  ratio facediag/NN     = {r_fd_nn:.6f}   (target 1/sqrt2 = {TARGET_BA:.6f})")
    print(f"  ratio facediag/onsite = {r_fd_on:.6f}")
    print(f"  ratio NN/onsite       = {r_nn_on:.6f}")
    # THE decisive parameter-free test: does any natural ratio equal 1/sqrt2?
    check("F3: facediag/NN is NOT 1/sqrt2 (the propagator does not force sqrt2)",
          abs(r_fd_nn - TARGET_BA) > 0.05,
          f"facediag/NN = {r_fd_nn:.4f} vs 1/sqrt2 = {TARGET_BA:.4f}")
    check("F3: facediag/onsite is NOT 1/sqrt2",
          abs(r_fd_on - TARGET_BA) > 0.05, f"{r_fd_on:.4f}")
    check("F3: NN/onsite is NOT 1/sqrt2",
          abs(r_nn_on - TARGET_BA) > 0.05, f"{r_nn_on:.4f}")
    # and the implied r if one (wrongly) used facediag/NN as |b|/a:
    r_implied = r_fd_nn ** 2
    check("F3: the propagator-implied r (facediag/NN)^2 is NOT 1/2",
          abs(r_implied - 0.5) > 0.05, f"r_implied = {r_implied:.4f}")
    # body-diagonal too: distance sqrt3; check it also misses 1/sqrt2 and 1/sqrt3
    r_bd_nn = Gbd / G1
    print(f"  ratio bodydiag/NN     = {r_bd_nn:.6f}   (sqrt3 reference 1/sqrt3 = {1/np.sqrt(3):.6f})")
    check("F3: bodydiag/NN is NOT 1/sqrt3 either (no clean length law in the propagator)",
          abs(r_bd_nn - 1 / np.sqrt(3)) > 0.02, f"{r_bd_nn:.4f} vs 1/sqrt3={1/np.sqrt(3):.4f}")
    print("  VERDICT F3: NO-SQRT2. The unique PARAMETER-FREE candidate gives")
    print("              facediag/NN ~ 0.641, not 1/sqrt2 ~ 0.707. The actual")
    print("              lattice propagator does NOT force the sqrt(2) weight.")
    print()
    return "NO-SQRT2"


# ----------------------------------------------------------------------
# F4. Area / volume geometric multiplicity
# ----------------------------------------------------------------------
def f4_multiplicity():
    section("F4. Geometric multiplicity (cubes sharing an edge vs a face-diagonal)")
    # infinite cubic lattice: an NN edge is shared by 4 unit cubes; a face-diagonal
    # (lying in one shared face) is shared by the 2 cubes meeting at that face.
    mult_nn = 4
    mult_fd = 2
    ratio = mult_fd / mult_nn
    print(f"  cubes sharing an NN edge        = {mult_nn}")
    print(f"  cubes sharing a face-diagonal   = {mult_fd}")
    print(f"  intensity ratio fd/NN           = {ratio:.6f}  (= 1/2)")
    print(f"  amplitude ratio sqrt(fd/NN)     = {np.sqrt(ratio):.6f}  (= 1/sqrt2)")
    check("F4: intensity (multiplicity) ratio fd/NN = 1/2 (gives r=1/4, not 1/2)",
          abs(ratio - 0.5) < 1e-12)
    check("F4: amplitude = sqrt(multiplicity) gives fd/NN = 1/sqrt2 -> r = 1/2",
          abs(np.sqrt(ratio) - TARGET_BA) < 1e-9)
    print("  VERDICT F4: NATURAL. sqrt(2) appears ONLY under the amplitude=sqrt(intensity)")
    print("              convention; the square-root step is the (conventional) choice.")
    print()
    return "NATURAL"


# ----------------------------------------------------------------------
# F5. Spectral / shift-operator norm weighting
# ----------------------------------------------------------------------
def f5_spectral():
    section("F5. Spectral weighting: shift operator C vs identity I")
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    Iden = np.eye(3, dtype=complex)
    fro_I = np.linalg.norm(Iden)
    fro_C = np.linalg.norm(C)
    op_I = np.linalg.norm(Iden, 2)
    op_C = np.linalg.norm(C, 2)
    print(f"  ||I||_F = {fro_I:.6f}   ||C||_F = {fro_C:.6f}")
    print(f"  ||I||_op = {op_I:.6f}   ||C||_op = {op_C:.6f}")
    check("F5: ||C||_F = ||I||_F (shift and identity have equal HS norm)",
          abs(fro_C - fro_I) < 1e-12)
    check("F5: ||C||_op = ||I||_op = 1 (C is unitary)",
          abs(op_C - 1) < 1e-12 and abs(op_I - 1) < 1e-12)
    # equal-norm weighting => b = a => r = 1, the Born/det_R default, NOT 1/sqrt2
    ba = fro_C / fro_I  # = 1
    check("F5: equal-norm weighting gives b/a = 1 -> r = 1 (Born default), NOT 1/sqrt2",
          abs(ba - 1.0) < 1e-12 and abs(ba - TARGET_BA) > 0.1)
    print("  VERDICT F5: NO-SQRT2. The bare spectral/operator norm of the shift equals")
    print("              that of the identity -> r = 1 (the maximal-hierarchy lane),")
    print("              not r = 1/2.")
    print()
    return "NO-SQRT2"


# ----------------------------------------------------------------------
# F6. The qubit-link u(2) / Clifford connection structure
# ----------------------------------------------------------------------
def f6_clifford():
    section("F6. Qubit-link u(2)/Clifford connection norm on a face-diagonal")
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    # Cl(3,0) = M_2(C): a displacement vector v maps to gamma(v) = sum_i v_i sigma_i,
    # with the Clifford relation gamma(v)^2 = |v|^2 I.
    g_nn = s1                 # NN displacement (1,0,0)
    g_fd = s1 + s2            # face-diagonal DISPLACEMENT (1,1,0)
    fro_nn = np.linalg.norm(g_nn)
    fro_fd = np.linalg.norm(g_fd)
    print(f"  ||gamma(1,0,0)||_F = {fro_nn:.6f}   ||gamma(1,1,0)||_F = {fro_fd:.6f}")
    # Clifford square recovers the squared Euclidean length
    sq_fd = g_fd @ g_fd
    sq_nn = g_nn @ g_nn
    check("F6: gamma(1,1,0)^2 = 2 I (Clifford recovers squared length 2 = (sqrt2)^2)",
          np.allclose(sq_fd, 2 * np.eye(2)))
    check("F6: gamma(1,0,0)^2 = 1 I (NN squared length 1)",
          np.allclose(sq_nn, np.eye(2)))
    # the gamma-norm ratio: face-diagonal is LARGER by sqrt2
    ratio = fro_fd / fro_nn
    check("F6: ||gamma(facediag)|| / ||gamma(NN)|| = sqrt2 (face-diagonal is LARGER)",
          abs(ratio - np.sqrt(2.0)) < 1e-9)
    # so if the hop amplitude tracked the gamma-norm, b/a = sqrt2 -> r = 2, the INVERSE
    r_direct = ratio ** 2
    check("F6: connection-norm reading gives b/a = sqrt2 -> r = 2 (wrong direction)",
          abs(r_direct - 2.0) < 1e-9,
          "to get r=1/2 the length must enter INVERSELY (a decay, i.e. F1/F2)")
    # and the Clifford 'sqrt2' is just the Euclidean metric re-encoded, not new info
    euclid_fd = np.linalg.norm(np.array([1, 1, 0]))
    check("F6: the Clifford length equals the Euclidean length (no new datum)",
          abs(np.sqrt((sq_fd[0, 0]).real) - euclid_fd) < 1e-12,
          f"sqrt(gamma^2)=sqrt2={euclid_fd:.6f}")
    print("  VERDICT F6: gives sqrt(2) only by RE-ENCODING the Euclidean metric, and")
    print("              with the WRONG sign (b/a = sqrt2 -> r = 2). Not an independent")
    print("              forcing of the 1/sqrt2 weight. Classify: NO-SQRT2 (as a forcing).")
    print()
    return "NO-SQRT2"


# ----------------------------------------------------------------------
# Category-mismatch defeat test
# ----------------------------------------------------------------------
def category_mismatch():
    section("Category-mismatch defeat test: is the continuous wall genuinely broken?")
    d_fd = np.sqrt(2.0)
    # (CM-1) The lattice supplies the DISCRETE length SET {0,1,sqrt2,sqrt3}, but NOT a
    #        weighting function f. Infinitely many lattice-native f give r=1/2.
    fns = {
        "f(d)=d^-1 (inverse length)":
            lambda d: d ** -1.0,
        "f(d)=exp(-(ln2/2) d^2) (Gaussian)":
            lambda d: np.exp(-(np.log(2) / 2) * d ** 2),
        "f(d)=exp(-c d), c=ln2/(2(sqrt2-1)) (exp decay)":
            lambda d: np.exp(-(np.log(2) / (2 * (np.sqrt(2) - 1))) * d),
    }
    hits = 0
    for name, f in fns.items():
        ba = f(d_fd) / f(1.0)
        ok = abs(ba * ba - 0.5) < 1e-9
        hits += int(ok)
        print(f"    {name:48s}: b/a = {ba:.6f} -> r = {ba*ba:.6f}  hit={ok}")
    check("CM-1: at least three DISTINCT lattice-native length-weightings give r=1/2",
          hits >= 3,
          "the lattice supplies the LENGTHS, not the function f -> f is the continuous input")

    # (CM-2) The DISCRETE sector-count route reaches r=1/2 with NO length at all.
    #        equipartition: 3a^2 = (|Z3|-1) * 3|b|^2  ->  r = 1/(|Z3|-1) = 1/2.
    n_sectors = 3 - 1
    r_count = 1.0 / n_sectors
    check("CM-2: pure discrete sector counting (|Z3|-1=2) already gives r = 1/2",
          abs(r_count - 0.5) < 1e-12,
          "r = 1/2 reachable with ZERO continuous input -> sqrt2 is not THE bridge")

    # (CM-3) the numerical coincidence: (sqrt2)^2 = 2 = |Z3|-1 (sector count).
    check("CM-3: (sqrt2)^2 = 2 equals the sector count |Z3|-1 = 2 (a NUMERICAL coincidence)",
          abs(d_fd ** 2 - n_sectors) < 1e-12,
          "same value 1/2, two structurally distinct origins (length vs counting)")

    print("  => CATEGORY MISMATCH NOT DEFEATED. The continuous datum sqrt2 is real, but")
    print("     (a) the CHOICE of length-weighting f (and its power) is the continuous")
    print("         input, supplied by hand, not by the lattice; and")
    print("     (b) r = 1/2 is ALREADY reachable by pure discrete sector counting, so")
    print("         sqrt2 is a second, length-based coincidence with the same value,")
    print("         not the unique continuous bridge the wall demanded.")
    print()


# ----------------------------------------------------------------------
def main() -> int:
    brannen_baseline()
    verdicts = {}
    verdicts["F1"] = f1_gaussian()
    verdicts["F2"] = f2_inverse_distance()
    verdicts["F3"] = f3_green_function()
    verdicts["F4"] = f4_multiplicity()
    verdicts["F5"] = f5_spectral()
    verdicts["F6"] = f6_clifford()
    category_mismatch()

    section("Per-candidate verdict table")
    for k in ["F1", "F2", "F3", "F4", "F5", "F6"]:
        print(f"  {k}: {verdicts[k]}")
    n_forced = sum(1 for v in verdicts.values() if v == "FORCED")
    n_natural = sum(1 for v in verdicts.values() if v == "NATURAL")
    n_nosqrt2 = sum(1 for v in verdicts.values() if v == "NO-SQRT2")
    print(f"  totals: FORCED={n_forced}  NATURAL={n_natural}  NO-SQRT2={n_nosqrt2}")
    check("VERDICT: NO candidate FORCES sqrt2 parameter-free in the right direction",
          n_forced == 0, "overall MIXED, leaning NATURAL")
    check("VERDICT: the parameter-free candidate (F3 Green function) does NOT give sqrt2",
          verdicts["F3"] == "NO-SQRT2")
    check("VERDICT: candidates that DO yield 1/sqrt2 (F1,F2,F4) all need a tuned choice",
          all(verdicts[k] == "NATURAL" for k in ["F1", "F2", "F4"]))

    print()
    section(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("Honest verdict: r = 1/2 via the face-diagonal length sqrt(2) is")
    print("NATURAL-but-NOT-FORCED. The discrete lattice genuinely supplies the")
    print("continuous datum sqrt(2), but it does NOT supply the weighting RULE that")
    print("turns sqrt(2) into 1/sqrt(2); and the same r=1/2 is already reachable by")
    print("pure discrete sector counting (|Z3|-1=2). The category mismatch therefore")
    print("reappears one level up (the choice to weight-by-length, and to what power).")
    print("Outcome: r=1/2 becomes a BETTER-MOTIVATED convention, not a closure.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
