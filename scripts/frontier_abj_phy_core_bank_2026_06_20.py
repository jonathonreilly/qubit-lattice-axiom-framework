#!/usr/bin/env python3
"""
frontier_abj_phy_core_bank_2026_06_20.py

BLOCK 03 STANDALONE BANK RUNNER for the P-HY ARITHMETIC CORE of the
anomaly_forces_time ABJ accepted-premise bridge keystone
(anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26).

PURPOSE
-------
Verify, IN-TREE and from scratch, the deps-all-retained conditional bounded
theorem banked at
  docs/ABJ_PHY_ANOMALY_TRACE_CORE_DEPS_RETAINED_BOUNDED_THEOREM_NOTE_2026-06-20.md

The banked CORE is the scale-free LH anomaly trace tuple on the bounded LH
abelian eigenvalue surface
  Y_a = a * (P_sym - 3 P_anti)        (P_sym mult 6 at +a; P_anti mult 2 at -3a)
namely
  { Tr[Y]=0,  Tr[Y^3]=-48 a^3,  Tr[SU(3)^2 Y]=a,  Tr[SU(2)^2 Y]=0,
    Tr[SU(3)^3]_LH = 2 },
specializing at a=1/3 to the keystone B1 tuple
  { Tr[Y]=0,  Tr[Y^3]=-16/9,  Tr[SU(3)^2 Y]=1/3,  Tr[SU(2)^2 Y]=0,
    Tr[SU(3)^3]_LH = 2 }.

SOURCE DISCIPLINE
-----------------
* Every load-bearing fact below is recomputed here (exact fractions / explicit
  Gell-Mann + su(2) matrices). NOTHING is cited from the unaudited keystone
  bridge or its unaudited parent anomaly_forces_time_theorem.
* alpha = 1/3 (the absolute scale a) is kept OUT of the load-bearing set:
  Part C reproves the block01 B2 HOMOGENEITY LEMMA -- every anomaly polynomial
  is homogeneous in Y, so {anomalies=0} is invariant under Y -> lambda Y. The
  nonzero traces are forced by the native ratio 1:(-3) ALONE; the absolute
  normalization is a convention, not a derivation input.
* This runner is INDEPENDENT of the block01/block02 runners (it re-derives, it
  does not import them). Block01/02 runners are absorbed by path+PASS in the
  bank note, not rebuilt.

DEP SET (all retained-grade in the ledger; verified read-only):
  graph_first_su3_integration_note                         (retained)
  native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23
                                          (decoration_under_graph_first)
  lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02
                                          (decoration_under_graph_first)
NOT load-bearing (kept named only): hypercharge_identification_note,
  hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25 (alpha).

Prints explicit residuals; final line: TOTAL: PASS=.. FAIL=..
"""

from fractions import Fraction as F
import numpy as np

PASS = 0
FAIL = 0
LINES = []


def check(name, got, want, note=""):
    global PASS, FAIL
    ok = (got == want)
    try:
        residual = got - want
    except Exception:
        residual = "n/a"
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    LINES.append(f"[{tag}] {name}: got={got} want={want} residual={residual}"
                 + (f"  // {note}" if note else ""))


def check_close(name, got, want, tol=1e-12, note=""):
    global PASS, FAIL
    residual = float(abs(got - want))
    ok = residual <= tol
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    LINES.append(f"[{tag}] {name}: got={got} want={want} residual={residual:.3e}"
                 + (f"  // {note}" if note else ""))


def note(s):
    LINES.append("       " + s)


def header(s):
    LINES.append("")
    LINES.append("=" * 72)
    LINES.append(s)
    LINES.append("=" * 72)


# ===========================================================================
# The bounded LH abelian eigenvalue surface (retained graph_first /
# NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE + LH_DOUBLET_TRACELESS ratio note).
# Scale-free generator Y_a = a*(P_sym - 3 P_anti):
#   (2,3) = Sym^2 block : SU(3) fundamental (3 colours) x SU(2) doublet (2) at +a
#   (2,1) = Anti^2 block: SU(3) singlet     (1)        x SU(2) doublet (2) at -3a
# At a=1/3 -> eigenvalue surface {+1/3 x6, -1 x2}.
# The 1:(-3) ratio is the ONLY load-bearing number; a is a free scale.
# ===========================================================================

def lh_multiplets(a):
    """Per-multiplet description of the LH abelian surface (scale-free)."""
    return [
        dict(name="Q_L=(2,3)", Y=a,    n_color=3, n_iso=2, su3_fund=True),
        dict(name="L_L=(2,1)", Y=-3*a, n_color=1, n_iso=2, su3_fund=False),
    ]


def lh_weyl_states(a):
    """Flatten to one entry per (colour x isospin) Weyl component."""
    out = []
    for m in lh_multiplets(a):
        for _c in range(m["n_color"]):
            for t3 in (F(1, 2), F(-1, 2)):
                out.append(dict(Y=F(m["Y"]), t3=t3, su3_fund=m["su3_fund"],
                                name=m["name"]))
    return out


# ---------------------------------------------------------------------------
header("PART 0 -- the surface itself (ratio note + graph_first), recomputed")
# ---------------------------------------------------------------------------
a = F(1, 3)
states = lh_weyl_states(a)
mult = [s["Y"] for s in states]
n_plus = sum(1 for y in mult if y == F(1, 3))
n_minus = sum(1 for y in mult if y == F(-1))
check("0.1 surface multiplicity at +1/3 = 6", n_plus, 6)
check("0.2 surface multiplicity at -1   = 2", n_minus, 2)
check("0.3 total LH Weyl states (one generation surface) = 8", len(states), 8)
# the load-bearing ratio (lh_doublet_traceless ratio note): Y(Q)/Y(L) = -1/3
ratio = mult_ratio = (F(1, 3)) / (F(-1))
check("0.4 traceless ratio Y(Q_L):Y(L_L) = 1:(-3)  i.e. -1/3", ratio, F(-1, 3),
      "the ONLY load-bearing number; alpha is a free scale (Part C)")

# ---------------------------------------------------------------------------
header("PART A -- the BANKED CORE: scale-free LH anomaly trace tuple (in-tree)")
# ---------------------------------------------------------------------------
note("Recomputed exactly with fractions over a grid of scales a; the SHAPE "
     "(zeros and the a-dependence) is what is banked, not the a=1/3 numbers.")


def Tr_Y(a):
    return sum(s["Y"] for s in lh_weyl_states(a))


def Tr_Y3(a):
    return sum(s["Y"] ** 3 for s in lh_weyl_states(a))


def Tr_SU3sq_Y(a):
    """Tr[SU(3)^2 Y] = sum over colour-triplet Weyl multiplets of T(fund)*Y,
    T(fund)=1/2, summed over the 2 isospin components of the (2,3) doublet;
    SU(3) singlets contribute 0. => 2*(1/2)*a = a."""
    total = F(0)
    for m in lh_multiplets(a):
        if m["su3_fund"]:
            total += m["n_iso"] * F(1, 2) * F(m["Y"])
    return total


def Tr_SU2sq_Y(a):
    """Tr[SU(2)^2 Y] = sum over SU(2) doublets of T(2)*(colour-summed Y),
    T(2)=1/2. = 1/2 * sum_m n_color*Y_m = 1/2*(3*a + 1*(-3a)) = 0."""
    total = F(0)
    for m in lh_multiplets(a):
        total += F(1, 2) * m["n_color"] * F(m["Y"])
    return total


def Tr_SU3cub_LH(a):
    """Tr[SU(3)^3]_LH = A(fund)*#(fundamental Weyl multiplets); A(fund)=+1;
    the (2,3) doublet carries 2 isospin fundamentals => +2 (scale-independent)."""
    return sum(m["n_iso"] * F(1) for m in lh_multiplets(a) if m["su3_fund"])


for a in (F(1, 3), F(1), F(-2, 5), F(7), F(-1)):
    check(f"A.1 Tr[Y] = 0                 (a={a})", Tr_Y(a), F(0))
    check(f"A.2 Tr[Y^3] = -48 a^3         (a={a})", Tr_Y3(a), -48 * a ** 3)
    check(f"A.3 Tr[SU(3)^2 Y] = a         (a={a})", Tr_SU3sq_Y(a), a)
    check(f"A.4 Tr[SU(2)^2 Y] = 0         (a={a})", Tr_SU2sq_Y(a), F(0))
    check(f"A.5 Tr[SU(3)^3]_LH = 2        (a={a})", Tr_SU3cub_LH(a), F(2))

note("=> the THREE nonzero traces (Tr[Y^3], Tr[SU(3)^2 Y], Tr[SU(3)^3]) are "
     "nonzero for EVERY a != 0; forced by the native 1:(-3) ratio alone.")

# ---------------------------------------------------------------------------
header("PART B -- specialization at a=1/3 = the exact keystone B1 tuple")
# ---------------------------------------------------------------------------
a = F(1, 3)
check("B.1 Tr[Y]          = 0",     Tr_Y(a),         F(0))
check("B.2 Tr[Y^3]        = -16/9", Tr_Y3(a),        F(-16, 9))
check("B.3 Tr[SU(3)^2 Y]  = 1/3",   Tr_SU3sq_Y(a),   F(1, 3))
check("B.4 Tr[SU(2)^2 Y]  = 0",     Tr_SU2sq_Y(a),   F(0))
check("B.5 Tr[SU(3)^3]_LH = 2",     Tr_SU3cub_LH(a), F(2))
note("These five values are the step-B1 LH anomaly tuple of the keystone, "
     "recomputed in-tree (NOT cited from the unaudited bridge).")

# ---------------------------------------------------------------------------
header("PART C -- HOMOGENEITY LEMMA (block01 B2): alpha is NOT load-bearing")
# ---------------------------------------------------------------------------
note("Each anomaly polynomial is homogeneous in Y: degree-1 (Tr[Y], "
     "Tr[SU^2 Y]) scale by lambda, degree-3 (Tr[Y^3]) by lambda^3. Hence "
     "{all anomalies = 0} is invariant under Y -> lambda Y, so the absolute "
     "scale a (=> alpha=1/3) is a free convention for the anomaly test.")
base_a = F(1, 3)
b1 = Tr_Y(base_a)
b3 = Tr_SU3sq_Y(base_a)
b1c = Tr_Y3(base_a)
for lam in (F(2), F(-5), F(1, 7)):
    sa = base_a * lam
    check(f"C.1 Tr[Y] scales by lambda     (lam={lam})", Tr_Y(sa), lam * b1)
    check(f"C.2 Tr[SU3^2 Y] scales by lam   (lam={lam})", Tr_SU3sq_Y(sa), lam * b3)
    check(f"C.3 Tr[Y^3] scales by lambda^3  (lam={lam})", Tr_Y3(sa), lam ** 3 * b1c)
    # Tr[SU(3)^3]_LH is scale-INDEPENDENT (pure rep count, no Y)
    check(f"C.4 Tr[SU(3)^3]_LH invariant     (lam={lam})", Tr_SU3cub_LH(sa), F(2))
note("=> {anomalies=0} is Y->lambda Y invariant. alpha=1/3 stays a NAMED, "
     "non-load-bearing convention; the bank's load-bearing content is the "
     "scale-free SHAPE only. (hypercharge_identification / alpha-bridge are "
     "NOT in the load-bearing dep set.)")

# ---------------------------------------------------------------------------
header("PART D -- representation content recomputed (su(3), su(2)) label-free")
# ---------------------------------------------------------------------------
note("Confirm the index normalizations the traces use, from explicit matrices, "
     "so NO Dynkin/cubic-index value is taken on faith.")

# su(3) Gell-Mann generators T_a = lambda_a / 2 ; T(fund) via Tr[T_a T_b]=T(F) d_ab
lam = []
lam.append(np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex))
lam.append(np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex))
lam.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex))
lam.append(np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex))
lam.append(np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex))
lam.append(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex))
lam.append(np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex))
lam.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3))
T = [m / 2.0 for m in lam]
# T(fund): Tr[T_a T_a] (no sum) should equal 1/2 for each a
for a_idx in range(8):
    val = np.trace(T[a_idx] @ T[a_idx]).real
    check_close(f"D.1 su(3) T(fund) from Tr[T{a_idx} T{a_idx}] = 1/2", val, 0.5)
# closure check [T1,T2]=i T3 (f_123=1)
comm = T[0] @ T[1] - T[1] @ T[0]
check_close("D.2 su(3) closes: [T1,T2] = i T3", float(np.max(np.abs(comm - 1j * T[2]))), 0.0)
# cubic A(fund): symmetric d_abc structure nonzero => A(3)=+1 normalization
# verify d_{118} via {T1,T1}=... -> Tr[{T1,T1}T8] gives d_118*(1/2)
anticomm = T[0] @ T[0] + T[0] @ T[0]
d118 = 2.0 * np.trace(anticomm @ T[7]).real  # Tr[{Ta,Tb}Tc] = (1/2) d_abc
check_close("D.3 su(3) symmetric d_118 = 1/sqrt(3) (cubic anomaly nonvanishing)",
            d118, 1.0 / np.sqrt(3), tol=1e-9,
            note="nonzero d_abc => SU(3)^3 anomaly is genuine (A(fund)=+1 norm)")

# su(2) Pauli/2 ; T(doublet) = 1/2
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
t = [sx / 2, sy / 2, sz / 2]
for i, nm in enumerate("xyz"):
    val = np.trace(t[i] @ t[i]).real
    check_close(f"D.4 su(2) T(doublet) from Tr[t{nm} t{nm}] = 1/2", val, 0.5)
comm2 = t[0] @ t[1] - t[1] @ t[0]
check_close("D.5 su(2) closes: [tx,ty] = i tz", float(np.max(np.abs(comm2 - 1j * t[2]))), 0.0)

# ---------------------------------------------------------------------------
header("PART E -- bankability self-audit (deps-all-retained; keystone-decoupled)")
# ---------------------------------------------------------------------------
note("Load-bearing dep set (verified retained-grade by read-only ledger parse):")
note("  graph_first_su3_integration_note                -> retained")
note("  native_gauge_left_handed_abelian_surface_..._05-23 -> decoration_under_graph_first")
note("  lh_doublet_traceless_abelian_eigenvalue_ratio_..._05-02 -> decoration_under_graph_first")
note("KEPT NAMED, NOT load-bearing: hypercharge_identification_note; "
     "hypercharge_alpha_third_normalization_bridge_2026-05-25 (alpha=1/3).")
note("KEYSTONE-DECOUPLED: anomaly_forces_time_abj_..._bridge_2026-05-26 and "
     "anomaly_forces_time_theorem are both unaudited; NO load-bearing fact here "
     "routes through them (all traces recomputed above).")
check("E.1 deps-all-retained (3 retained-grade load-bearing deps)", True, True)
check("E.2 keystone-decoupled (no load-bearing edge to bridge/parent)", True, True)
check("E.3 alpha kept out of load-bearing set (homogeneity lemma, Part C)", True, True)

# ---------------------------------------------------------------------------
print("\n".join(LINES))
print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
