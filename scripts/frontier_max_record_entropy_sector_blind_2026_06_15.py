#!/usr/bin/env python3
"""
Max-record-entropy is SECTOR-BLIND inside a supplied separable C3 selector class.

Class-A finite-dim exact checks. The make-or-break is the WEIGHT-LEAK ACID TEST: does
maximizing the 2-sector (singlet|doublet) record entropy on the C3 generation space give a
SECTOR-DEPENDENT r (firewall-OK) or pin r=1/2 UNIVERSALLY (a weight-leak against the
registered quark/neutrino comparators)? Result: under the supplied hypothesis that every
sector uses the same C3 isotype record partition and color/charge enter only as a separable
factor that cancels in the normalized record fractions, max-record-entropy returns r=1/2 for
every sector in that class. It is a sharper CHARACTERIZATION of the registered charged-lepton
setting (the symmetric / max-uncertainty point), NOT a derivation of the dial and NOT a proof
that all physical fermion sectors realize the supplied separable carrier.

This runner does NOT force r=1/2 (it shows that forcing it universally = a weight-leak) and does
NOT derive any sector's r. r and the sector weights are free / registered data.

Prints "TOTAL: PASS=N FAIL=0".
"""
from pathlib import Path

import numpy as np

NOTE_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md"
)

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}")


def shannon2(w_s, w_d):
    """Shannon entropy (nats) of the 2-cell record weights {w_s, w_d}."""
    w = np.array([w_s, w_d], float)
    w = w[w > 0]
    return float(-(w * np.log(w)).sum())


def record_weights(r):
    """2-sector record weights from the Koide block ratio r = |b|^2 / a^2.
    Singlet power a^2 (=1), doublet power 2|b|^2 (=2r); normalized."""
    Z = 1.0 + 2.0 * r
    return 1.0 / Z, 2.0 * r / Z


# ---- C3 generation structure (finite M3(C) carrier from cited generation theorems) ----
w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], complex)  # cyclic shift = the [111] 3-fold
# isotype projectors: P_s = trivial (+1 eigenvector (1,1,1)/sqrt3), P_d = the 2-dim doublet
v_s = np.ones(3, complex) / np.sqrt(3)
P_s = np.outer(v_s, v_s.conj())
P_d = np.eye(3, dtype=complex) - P_s
check("P_s rank 1, P_d rank 2 (C3 isotype split 1+2)",
      np.linalg.matrix_rank(P_s) == 1 and np.linalg.matrix_rank(P_d) == 2)
check("P_s, P_d commute with C (isotype projectors of C3)",
      np.allclose(C @ P_s, P_s @ C) and np.allclose(C @ P_d, P_d @ C))


# ============================================================================
# 1. SETUP (already landed, retained_bounded): S2(r) is maximized exactly at r=1/2.
# ============================================================================
print("\n[1] 2-sector record entropy S2(r) is maximized at r=1/2 (setup; retained-bounded siblings)")
rs = np.linspace(1e-4, 3.0, 400001)
S = np.array([shannon2(*record_weights(r)) for r in rs])
r_star = rs[int(np.argmax(S))]      # the COMPUTED max-entropy selector (used downstream, not hardcoded)
check("argmax_r S2(r) = 1/2 (grid, 4e5 pts)", abs(r_star - 0.5) < 1e-4)
check("S2(1/2) = ln 2 (equipartition w_s=w_d=1/2)", abs(shannon2(*record_weights(0.5)) - np.log(2)) < 1e-12)
ws, wd = record_weights(0.5)
check("at r=1/2 the record weights are equal (w_s=w_d=1/2)", abs(ws - 0.5) < 1e-12 and abs(wd - 0.5) < 1e-12)


# ============================================================================
# 2. THE MAKE-OR-BREAK: supplied separable color is SECTOR-BLIND to the generation record.
#    Tensor a color factor (uniform over the supplied generation triplet), trace it out:
#    the generation-record weights are UNCHANGED => max-entropy argmax stays r=1/2 for ALL sectors.
# ============================================================================
print("\n[2] MAKE-OR-BREAK conditional test: separable color cancels => argmax r=1/2")


def gen_record_weights_with_color(r, d_color):
    """Build rho_gen (block weights w_s,w_d at ratio r) tensor maximally-mixed color (dim d_color),
    take the generation 2-sector record P_s|P_d (the supplied separable selector hypothesis),
    and return the GENERATION-marginal record weights."""
    w_s, w_d = record_weights(r)
    rho_gen = w_s * P_s + w_d * (P_d / 2.0)              # uniform within each block
    rho_full = np.kron(rho_gen, np.eye(d_color) / d_color)  # gauge-uniform color factor
    Ps_full = np.kron(P_s, np.eye(d_color))
    Pd_full = np.kron(P_d, np.eye(d_color))
    return float(np.trace(Ps_full @ rho_full).real), float(np.trace(Pd_full @ rho_full).real)


for d_c, label in [(1, "lepton Nc=1"), (3, "quark Nc=3"), (2, "weak-doublet"), (8, "adjoint")]:
    # pick an arbitrary r; the generation-record weights must NOT depend on d_color
    w0 = record_weights(0.37)
    wc = gen_record_weights_with_color(0.37, d_c)
    check(f"[{label}] supplied separable factor d={d_c} leaves generation record weights invariant",
          abs(wc[0] - w0[0]) < 1e-12 and abs(wc[1] - w0[1]) < 1e-12)

# argmax over r of the colored generation record entropy stays = the bare selector for every color dim
rs_coarse = rs[::40]
colored_selectors = {}
for d_c in [1, 2, 3, 8]:
    Sc = np.array([shannon2(*gen_record_weights_with_color(r, d_c)) for r in rs_coarse])
    rc_star = rs_coarse[int(np.argmax(Sc))]
    colored_selectors[d_c] = rc_star
    check(f"argmax_r S2(r; color d={d_c}) equals the bare selector r_star (sector-blind)",
          abs(rc_star - r_star) < 2e-3)
check("all color dims give the SAME selector (max-entropy is sector-blind, computed not assumed)",
      max(colored_selectors.values()) - min(colored_selectors.values()) < 2e-3)


# NEGATIVE CONTROL: break the supplied uniformity. If the gauge rep acted with DIFFERENT multiplicity on
# the singlet vs the doublet (alpha_s != alpha_d), the cancellation fails and the argmax MOVES off the
# bare selector to r = alpha_s/(2 alpha_d). This proves the sector-blindness hinges on the supplied
# separable hypothesis, not on the entropy functional alone.
def nonuniform_record_weights(r, alpha_s, alpha_d):
    """Singlet/doublet block multiplicities alpha_s, alpha_d (uniform route <=> alpha_s == alpha_d)."""
    a_s = alpha_s * 1.0
    a_d = alpha_d * 2.0 * r
    Z = a_s + a_d
    return a_s / Z, a_d / Z

# uniform recovers the bare selector...
S_u = np.array([shannon2(*nonuniform_record_weights(r, 1.0, 1.0)) for r in rs_coarse])
check("CONTROL alpha_s=alpha_d (supplied uniform route): argmax recovers r_star=1/2",
      abs(rs_coarse[int(np.argmax(S_u))] - r_star) < 2e-3)
# ...non-uniform (alpha_s=3, alpha_d=1) SHIFTS the argmax to r = 3/2, proving the hinge.
S_nu = np.array([shannon2(*nonuniform_record_weights(r, 3.0, 1.0)) for r in rs_coarse])
r_nu = rs_coarse[int(np.argmax(S_nu))]
check("CONTROL alpha_s=3,alpha_d=1 (non-uniform route): argmax shifts to r=3/2 (= alpha_s/2alpha_d)",
      abs(r_nu - 1.5) < 2e-3)
check("CONTROL: the non-uniform argmax is NOT 1/2 (sector-blindness requires supplied uniformity)",
      abs(r_nu - 0.5) > 0.5)


# ============================================================================
# 3. The registered quark values are STRICTLY SUB-MAXIMAL entropy => a universal
#    max-entropy selection (which gives r=1/2) FALSIFIES them. This is the weight leak.
# ============================================================================
print("\n[3] registered quark r are sub-maximal entropy => universal max-entropy falsifies them")
S_half = shannon2(*record_weights(0.5))
for r_q, name in [(0.597, "r_down"), (0.773, "r_up")]:
    check(f"S2({name}={r_q}) < S2(1/2) strictly (sub-maximal => not the max-entropy point)",
          shannon2(*record_weights(r_q)) < S_half - 1e-6)
# the disqualifier: the COMPUTED max-entropy selector (r_star, sector-blind) conflicts with the
# registered quark settings -- so applied universally it weight-leaks (uses the computed value, not 0.5).
check("COMPUTED max-entropy selector r_star conflicts with registered r_down=0.597 => weight-leak",
      abs(r_star - 0.597) > 1e-2)
check("COMPUTED max-entropy selector r_star conflicts with registered r_up=0.773 => weight-leak",
      abs(r_star - 0.773) > 1e-2)


# ============================================================================
# 4. NON-UNIQUENESS of "max entropy": weight-uniform vs state-uniform give DIFFERENT r.
#    (maximally-mixed generation state I/3 = max von Neumann entropy => block weights (1/3,2/3) => r=1.)
# ============================================================================
print("\n[4] 'max entropy' is ambiguous: weight-uniform -> r=1/2, state-uniform (I/3) -> r=1")
# weight-uniform: w_s=w_d=1/2 -> r=1/2
r_weight_uniform = 0.5
# state-uniform: rho = I/3, block weights = (tr P_s /3, tr P_d /3) = (1/3, 2/3) -> w_d/(2 w_s) = 1
ws_su, wd_su = 1.0 / 3.0, 2.0 / 3.0
r_state_uniform = wd_su / (2.0 * ws_su)
check("state-uniform (I/3) gives r=1 (dimension weighting)", abs(r_state_uniform - 1.0) < 1e-12)
check("the two max-entropy readings give DIFFERENT r (1/2 != 1) => the reading is a measure choice",
      abs(r_weight_uniform - r_state_uniform) > 0.4)


# ============================================================================
# 5. Supplied degree-0/inert gauge channel: a color charge acts as a SCALAR on the
#    generation index, commutes with C, and leaves the isotype projector invariant.
# ============================================================================
print("\n[5] conditional degree-0 gauge channel is scalar on the generation index")
G = 1.7  # an arbitrary gauge Casimir eigenvalue
Gop = G * np.eye(3, dtype=complex)  # supplied uniform route => scalar on the 3 generations
check("supplied uniform gauge operator commutes with C", np.allclose(Gop @ C, C @ Gop))
P0 = (np.eye(3, dtype=complex) + C + C @ C) / 3.0  # = P_s
check("isotype projector P0=(I+C+C^2)/3 equals the singlet projector P_s", np.allclose(P0, P_s))
check("supplied uniform gauge operator leaves the isotype projector invariant ([Gop,P0]=0)",
      np.allclose(Gop @ P0, P0 @ Gop))
# discriminating control: a NON-uniform generation operator (diag 1,2,3) does NOT commute with C
Gbad = np.diag([1.0, 2.0, 3.0]).astype(complex)
check("CONTROL: a generation-NON-uniform operator breaks [.,C]=0 (would be needed to shift r)",
      not np.allclose(Gbad @ C, C @ Gbad))


# ============================================================================
# 6. FIREWALL: r=1/2, 0.597, 0.773, 1 are ALL valid dial outputs; the runner forces none.
# ============================================================================
print("\n[6] firewall: the map forces no r; all sector settings are valid dial outputs")
def koide_Q(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r
sector_rs = [0.0, 0.5, 0.597, 0.773, 1.0]
valid = all(1.0 / 3.0 - 1e-9 <= koide_Q(r) <= 1.0 + 1e-9 for r in sector_rs)
check("Q(r)=1/3+2r/3 in [1/3,1] for r in {0,1/2,0.597,0.773,1} (all valid, none forced)", valid)
# genuine firewall test (not a tautology): the registered sector settings map to DISTINCT Koide Q,
# and the (sector-blind) max-entropy selector coincides with ONLY the lepton setting -- so the
# functional cannot be the universal selector; the other settings are free registered dial data.
Qs = [round(koide_Q(r), 6) for r in [0.5, 0.597, 0.773, 1.0]]
check("the four sector settings map to four DISTINCT Koide Q (free dial, none privileged by the map)",
      len(set(Qs)) == 4)
check("max-entropy selector r_star matches ONLY the lepton setting, not the quark/dimension settings",
      abs(r_star - 0.5) < 1e-3 and min(abs(r_star - r) for r in [0.597, 0.773, 1.0]) > 1e-2)


# ============================================================================
# 7. Source-boundary guard: keep the note narrowed to the audited repair scope.
# ============================================================================
print("\n[7] source-boundary guard: conditional algebraic selector theorem, not physical bridge")
note_text = NOTE_PATH.read_text(encoding="utf-8")
check("source claim type uses canonical no_go vocabulary", "**Claim type:** no_go" in note_text)
check("source names the supplied gauge-uniform separable selector hypothesis",
      "supplied gauge-uniform separable selector hypothesis" in note_text)
check("source says the separable carrier is not a retained physical bridge",
      "not a retained physical bridge" in note_text)
check("registered quark values are non-load-bearing comparators",
      "non-load-bearing comparators" in note_text)
check("source no longer claims retained gauge-uniformity",
      "retained gauge-uniformity" not in note_text)


print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
assert FAIL == 0, "discriminating checks failed"
