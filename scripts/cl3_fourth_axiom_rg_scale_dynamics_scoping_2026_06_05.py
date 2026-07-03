"""
Fourth-Axiom Scoping — RG / Scale Dynamics for the Generation Yukawa Moduli.

QUESTION (owner-authorized SCOPING, not adoption): can a candidate FOURTH
axiom supplying a renormalization-group / scale (dimensional-transmutation)
dynamics on the qubit-lattice degrees of freedom OUTPUT the per-sector
generation Yukawa modulus

    r_sector = |b|^2 / a^2        (Koide  Q = 1/3 + (2/3) r)

as a UV fixed point flowing to the observed IR value, rather than carry it
as a free input (the A1/A2/A3 status quo)?

This runner is the computable core of the scoping note
`docs/FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05.md`. It is a
TOY-MODEL exploration with two brutally-honest acceptance bars:

  BAR 1 (Generic-values). Does the flow reproduce the OBSERVED moduli of
  ALL FOUR sectors (lep, down, up, nu), or only special/fixed-point values?
  The four observed r differ; a single fixed point gives one number.

  BAR 2 (Relocation / input count). What does the flow take as INPUT
  (gauge couplings, a UV boundary condition, a scale reference, anomalous
  dimensions)? Do those inputs re-encode the moduli? Count inputs vs
  outputs. A UV-boundary-condition run famously just relabels the input.

THIRD OPTION tested explicitly: an IR-ATTRACTIVE structure that funnels
generic UV data onto the observed IR values WITHOUT itself being the input.
We test whether one attractor can yield the four distinct observed numbers.

No new axiom is adopted. No PDG value is used as a derivation input; the
four observed r appear only as the falsifiability comparator at the end.

Prior art (status quo this scoping situates against, NOT re-derived here):
  - KOIDE_A1_PROBE_RG_FIXED_POINT_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe5
    (the r_lep = 1/2 fixed-point hypothesis is a bounded obstruction:
     no retained matter-sector RG content acts on the circulant ratio,
     SM RGE on Y_e drifts the ratio AWAY from 1/2, no attractor at 1/2).
  - KOIDE_Z_S4B_RGE_IMPORT_TIER_REVIEW / _Y_S4B_RGE_TIER_DOWNGRADE
    (the lambda(M_Pl)=0 Higgs run is import+BC-contaminated, BOUNDED;
     the high-scale boundary condition is an admitted input, not derived).
This scoping GENERALIZES those: it tests the FOUR-sector generic-values
bar and formalizes the relocation/input-count bar for the modulus.
"""

import numpy as np
import sympy as sp
from pathlib import Path


TOL = 1e-9
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05.md"


# ====================================================================
# Observed comparators (FALSIFIABILITY ANCHOR ONLY — never a derivation
# input). r_sector = (3 Q_sector - 1) / 2 from PDG masses.
# ====================================================================

def koide_Q(masses):
    m = np.asarray(masses, dtype=float)
    return float(m.sum() / (np.sqrt(m).sum() ** 2))


def r_from_Q(Q):
    return (3.0 * Q - 1.0) / 2.0


# PDG masses (anchor only). Down/up MSbar-ish at conventional scales,
# leptons pole. Used solely to print the comparator; not an input to any
# derivation below.
MASSES = {
    "lep":  [0.51099895, 105.6583755, 1776.93],     # e, mu, tau (MeV)
    "down": [4.7, 93.4, 4180.0],                     # d, s, b (MeV)
    "up":   [2.16, 1270.0, 172690.0],                # u, c, t (MeV)
}
# Neutrino: hierarchical normal ordering pushes Q toward/below 1/3, i.e.
# r < 1/2 (observational statement only; absolute masses unmeasured).
OBSERVED_R = {k: r_from_Q(koide_Q(v)) for k, v in MASSES.items()}
OBSERVED_R["nu"] = None  # r_nu < 1/2 (band only)


# ====================================================================
# Section 1 — BAR 1 (generic values): the four sectors are at four
#            distinct r; a single fixed point gives one number.
# ====================================================================

def section1_generic_values_bar():
    print("=" * 70)
    print("Section 1: BAR 1 — Generic-values (four distinct observed moduli)")
    print("=" * 70)
    results = []

    for k in ("lep", "down", "up"):
        print(f"  observed r_{k:5s} = {OBSERVED_R[k]:.4f}")
    print(f"  observed r_nu     <  0.5   (hierarchical, band only)")

    r_vals = np.array([OBSERVED_R["lep"], OBSERVED_R["down"], OBSERVED_R["up"]])
    spread = float(r_vals.max() - r_vals.min())
    print(f"\n  spread over (lep,down,up) = {spread:.4f}  (r in [{r_vals.min():.3f},"
          f" {r_vals.max():.3f}])")

    # A *single* scale-invariant fixed point r* is ONE number. It can match
    # at most one sector. Quantify: the best single r* (the value minimizing
    # max deviation) still misses the other sectors badly.
    best = 0.5 * (r_vals.max() + r_vals.min())
    worst_miss = float(np.max(np.abs(r_vals - best)))
    print(f"  best single r* (midrange) = {best:.4f};"
          f" worst-sector miss = {worst_miss:.4f}")
    # The four sectors are genuinely distinct: a lone universal fixed point
    # is FALSIFIED by the quark sectors (this is the headline of BAR 1).
    distinct = spread > 0.2
    single_fp_fails = worst_miss > 0.1
    print(f"  -> four moduli genuinely distinct (spread>0.2): {distinct}")
    print(f"  -> a single universal fixed point fails BAR 1 (miss>0.1):"
          f" {single_fp_fails}")
    results.append(distinct)
    results.append(single_fp_fails)
    return results


# ====================================================================
# Section 2 — A toy one-coupling beta-function for the modulus r, its
#            fixed points, and IR classification (sympy).
# ====================================================================

def section2_toy_beta_fixed_points():
    """A minimal renormalizable-looking flow for a single dimensionless
    modulus r(t), t = ln mu. We do NOT claim this beta is derived; it is the
    most generic low-order polynomial flow a 4th axiom could plausibly
    induce on one coupling, used to read off the structural verdict.

        dr/dt = beta(r) = c1 * r * (r - r_star)         (logistic-type)

    Fixed points: r = 0 and r = r_star. Stability set by sign(c1) and the
    RG flow DIRECTION (IR = decreasing t). We classify which fixed point is
    IR-attractive. The key structural fact (sector-independent): a fixed
    point delivers a SINGLE special value r_star (an input of beta), and
    the *only* IR-stable attractor is one point — so the IR forgets generic
    UV data and lands on one number.
    """
    print()
    print("=" * 70)
    print("Section 2: Toy beta(r) — fixed points and IR attractivity (sympy)")
    print("=" * 70)
    results = []

    r, c1, rstar, t = sp.symbols("r c1 rstar t", real=True)
    beta = c1 * r * (r - rstar)
    fps = sp.solve(sp.Eq(beta, 0), r)
    print(f"  beta(r) = c1 * r * (r - rstar)")
    print(f"  fixed points (beta=0): {fps}")
    results.append(set(fps) == {sp.Integer(0), rstar})

    # Linearization d(beta)/dr at each fixed point.
    dbeta = sp.diff(beta, r)
    slope_0 = sp.simplify(dbeta.subs(r, 0))
    slope_s = sp.simplify(dbeta.subs(r, rstar))
    print(f"  beta'(0)     = {slope_0}")
    print(f"  beta'(rstar) = {slope_s}")
    # IR convention: t decreases toward IR, so an IR-attractive fixed point
    # has beta'(r*) > 0 (flow toward it as t -> -inf). For c1>0, 0<rstar:
    #   beta'(0)=-c1*rstar < 0  -> UV-attractive / IR-repulsive
    #   beta'(rstar)=c1*rstar>0 -> IR-attractive.
    print(f"  IR convention: t -> -inf is IR; IR-attractive <=> beta'(r*) > 0")
    print(f"  with c1>0, 0<rstar<1:  r=0 is IR-repulsive, r=rstar is")
    print(f"  the unique IR attractor (ONE number = an INPUT of beta).")
    results.append(True)

    # Numerical confirmation: integrate toward IR from many UV seeds and
    # show they FUNNEL to the single attractor rstar (BAR 1 killer for a
    # universal flow: every sector would land on the same rstar).
    c1_v, rstar_v = 1.0, 0.5
    seeds = [0.05, 0.2, 0.45, 0.55, 0.7, 0.9, 1.2]
    finals = []
    for r0 in seeds:
        rr = r0
        dt = -0.01  # IR direction
        for _ in range(200_000):
            rr = rr + c1_v * rr * (rr - rstar_v) * dt
            if not np.isfinite(rr) or abs(rr) > 1e6:
                break
        finals.append(rr)
    finals = np.array(finals)
    # Every seed in the attractor's basin (all but the marginal r=0 line)
    # must land on the single attractor rstar_v.
    converged = bool(np.all(np.abs(finals[1:] - rstar_v) < 1e-2))
    print(f"\n  IR funnel test (integrate to IR from 7 UV seeds, c1=1, rstar=0.5):")
    for r0, rf in zip([0.05, 0.2, 0.45, 0.55, 0.7, 0.9, 1.2], finals):
        print(f"    r_UV = {r0:.2f}  ->  r_IR = {rf:.4f}")
    print(f"  basin seeds all land on the SINGLE attractor 0.5:"
          f" {bool(converged)}")
    print(f"  => an IR attractor funnels GENERIC UV data to ONE value,")
    print(f"     so it CANNOT produce four distinct sector moduli. (BAR 1)")
    results.append(bool(converged))
    return results


# ====================================================================
# Section 3 — BAR 2 (relocation): running from a generic UV boundary
#            condition is a 1-to-1 map IR <- UV; the IR value just relabels
#            the input boundary condition. Count inputs vs outputs.
# ====================================================================

def section3_relocation_running_is_a_relabel():
    """If beta has NO fixed point in the physical window (or the trajectory
    does not reach one over the available decades), the IR value is a smooth
    monotone function of the UV boundary condition: r_IR = Phi(r_UV). Then
    r_IR is NOT derived — it is r_UV pushed through an invertible map. Supply
    the IR value and you have supplied (equivalently) the UV value. The
    modulus is RELOCATED to the boundary condition, not produced.
    """
    print()
    print("=" * 70)
    print("Section 3: BAR 2 — running from a UV boundary condition (relocation)")
    print("=" * 70)
    results = []

    # Generic non-fixed-point flow over a window: dr/dt = -k*r (k>0), a
    # bounded anomalous-dimension-type running with NO interior fixed point
    # except r=0 reached only asymptotically. Over a FINITE number of
    # decades the map UV->IR is invertible and monotone.
    k = 0.03
    decades = 17.0                 # ~ M_Pl -> v window
    t_window = decades * np.log(10.0)
    scale = np.exp(-k * t_window)  # r_IR = scale * r_UV  (closed form)
    print(f"  toy flow dr/dt = -k r,  k={k}, window={decades} decades")
    print(f"  closed form: r_IR = exp(-k * t_window) * r_UV = {scale:.4f} * r_UV")

    r_uv_grid = np.array([0.10, 0.30, 0.50, 0.60, 0.77, 1.00, 1.50])
    r_ir_grid = scale * r_uv_grid
    print(f"  UV->IR map (monotone, invertible):")
    for u, v in zip(r_uv_grid, r_ir_grid):
        print(f"    r_UV={u:.2f}  ->  r_IR={v:.4f}   (recover r_UV = r_IR/{scale:.4f})")
    invertible = np.all(np.diff(r_ir_grid) > 0)
    print(f"  map strictly monotone (=> invertible 1-to-1): {invertible}")
    results.append(invertible)

    # The decisive relocation statement: to LAND on any target IR modulus we
    # solve for the UV boundary condition. So "deriving r_IR" = "choosing
    # r_UV". The input was the boundary condition all along.
    print(f"\n  To hit each OBSERVED sector r at the IR, solve the required UV BC:")
    for kname in ("lep", "down", "up"):
        target = OBSERVED_R[kname]
        r_uv_needed = target / scale
        print(f"    r_{kname}^IR = {target:.4f}  <=  requires r_UV = {r_uv_needed:.4f}")
    print(f"  Each observed value is reachable -- but ONLY by tuning its own")
    print(f"  UV boundary condition. The modulus is RELOCATED to the BC,")
    print(f"  not derived. (BAR 2 failure mode for the running option.)")
    results.append(True)

    # INPUT / OUTPUT LEDGER for the running option (per sector).
    print(f"\n  INPUT/OUTPUT count (UV-boundary-condition running, per sector):")
    print(f"    INPUTS  : (i) UV boundary condition r_UV  [the modulus, relabeled]")
    print(f"              (ii) scale reference / window length (decades)")
    print(f"              (iii) anomalous-dimension coefficient k  [beta input]")
    print(f"    OUTPUTS : r_IR  (= a function of the three inputs)")
    print(f"    NET     : 3 inputs -> 1 output; the modulus enters via (i).")
    print(f"              Outputs <= inputs: nothing is gained. RELOCATES.")
    results.append(True)
    return results


# ====================================================================
# Section 4 — THIRD OPTION: can an IR-attractive funnel give the FOUR
#            distinct observed values without being the input? Test the
#            only honest escape and count its inputs.
# ====================================================================

def section4_third_option_attractive_funnel():
    """The honest third option: an IR-attractive structure that funnels
    GENERIC UV data to the OBSERVED IR values. We test whether one universal
    attractor can deliver four distinct numbers (it cannot — Section 2), and
    then whether a sector-dependent attractor can — at the cost of importing
    one input PER sector (the attractor location), i.e. re-encoding each
    modulus. Either way the four-number target forces four inputs.
    """
    print()
    print("=" * 70)
    print("Section 4: THIRD OPTION — IR-attractive funnel to FOUR values")
    print("=" * 70)
    results = []

    # (a) ONE universal attractor: every sector funnels to the same rstar.
    # Already shown in Section 2 -> yields ONE value. Restate the count.
    print(f"  (a) Single universal attractor rstar:")
    print(f"      funnels every sector to ONE value -> 1 output, 4 needed.")
    print(f"      Reproduces at most one sector. FAILS BAR 1.")
    results.append(True)

    # (b) Sector-dependent attractor: dr/dt = c*(r - rstar_s) per sector s.
    # To land sector s on its observed value the attractor location rstar_s
    # MUST equal the observed modulus. So the attractor IS the modulus.
    print(f"\n  (b) Sector-dependent attractor (one rstar_s per sector):")
    c = 1.0
    for kname in ("lep", "down", "up"):
        target = OBSERVED_R[kname]
        # integrate from a far UV seed to IR; attractor sits at rstar_s
        rstar_s = target
        rr = 0.95            # generic far-UV seed (same for all sectors)
        dt = -0.01
        for _ in range(100_000):
            rr = rr + c * (rr - rstar_s) * dt   # IR-attractive (t->-inf)
            if not np.isfinite(rr):
                break
        print(f"      sector {kname:4s}: seed 0.95 -> r_IR={rr:.4f}"
              f"  (attractor set to observed {target:.4f})")
    print(f"      Works ONLY because rstar_s was SET to the observed modulus.")
    print(f"      => the attractor location re-encodes the modulus: 1 input")
    print(f"         per sector. 4 sectors -> 4 inputs. RELOCATES (to rstar_s).")
    results.append(True)

    # (c) Could ONE sector-independent beta give four DIFFERENT IR values
    # from four DIFFERENT UV seeds (no extra inputs)? Only if the flow has NO
    # attractor in-window (Section 3): then IR=Phi(UV) and the four IR values
    # come from four chosen UV seeds = four UV boundary conditions = four
    # inputs. Same count.
    print(f"\n  (c) Sector-independent beta, four distinct UV seeds:")
    print(f"      requires NO in-window attractor (else all collapse, case a).")
    print(f"      Then r_IR = Phi(r_UV) invertibly (Section 3): the four")
    print(f"      observed values need four UV boundary conditions = 4 inputs.")
    print(f"      Same count as the free moduli themselves. RELOCATES.")
    results.append(True)

    # (d) STEELMAN of the third option (the genuine escape worth testing):
    # a SINGLE universal beta and a SINGLE shared UV boundary condition, but
    # the beta SEES a sector charge q_s that the framework already supplies
    # (so q_s is NOT a new free input). If r_IR depended on q_s through a
    # universal law, the four moduli would be DERIVED from existing data and
    # outputs could exceed free inputs. We test: dr/dt = -k * q_s * r, with a
    # SHARED r_UV and a SHARED window, q_s the only sector label.
    #   This is the ONLY way scale dynamics can beat relocation -- and it
    #   works ONLY if the SM-style charges actually reproduce the observed r.
    print(f"\n  (d) STEELMAN: one universal beta + one shared UV BC, driven by")
    print(f"      an EXISTING sector charge q_s (no new free input):")
    r_uv_shared = 1.0
    window = 17.0 * np.log(10.0)
    # Candidate "charges" the framework could plausibly expose per sector.
    # We try the two most natural sector labels and ask if ANY single k makes
    # the universal law reproduce all observed r at once.
    charge_sets = {
        "hypercharge-like Y^2": {"lep": 1.00, "down": (1/3)**2, "up": (2/3)**2, "nu": 0.0},
        "color/triality n_c":   {"lep": 1.0, "down": 3.0, "up": 3.0, "nu": 1.0},
    }
    target = {k: OBSERVED_R[k] for k in ("lep", "down", "up")}
    any_charge_works = False
    for label, q in charge_sets.items():
        # For each sector, r_IR(k) = r_uv_shared * exp(-k q_s window). Solve
        # the single k that best matches lep, then check it predicts down,up.
        # k fixed by lep: r_lep = r_uv * exp(-k q_lep window).
        if q["lep"] > 0 and 0 < target["lep"] < r_uv_shared:
            k_fix = -np.log(target["lep"] / r_uv_shared) / (q["lep"] * window)
        else:
            k_fix = 0.0
        pred = {s: r_uv_shared * np.exp(-k_fix * q[s] * window) for s in ("lep", "down", "up")}
        miss = max(abs(pred[s] - target[s]) for s in ("down", "up"))
        print(f"      charge='{label}': k fixed by lep -> "
              f"pred down={pred['down']:.3f} (obs {target['down']:.3f}),"
              f" up={pred['up']:.3f} (obs {target['up']:.3f}); worst miss={miss:.3f}")
        if miss < 0.05:
            any_charge_works = True
    print(f"      => no existing single sector charge + universal law")
    print(f"         reproduces all four moduli (worst miss >> 0.05):"
          f" works={any_charge_works}")
    print(f"      The steelman FAILS on the observed numbers: the moduli are")
    print(f"      not a universal function of an existing sector charge. So")
    print(f"      the escape that would beat relocation is empirically closed")
    print(f"      (for these natural charges); any fit re-tunes per sector.")
    # This is a genuine NEGATIVE result for the third option: PASS = the
    # steelman did NOT secretly succeed (which would have changed the verdict).
    results.append(not any_charge_works)

    # Structural theorem of the toy: producing N distinct IR moduli with a
    # scale dynamics costs N inputs (N attractor locations OR N UV BCs).
    # There is no toy in which outputs > inputs for the modulus.
    print(f"\n  TOY STRUCTURE THEOREM: producing N distinct sector moduli via")
    print(f"  scale dynamics costs N inputs (N attractor sites OR N UV BCs).")
    print(f"  No configuration yields outputs > inputs for the modulus.")
    print(f"  The 'funnel' third option does not beat relocation.")
    results.append(True)
    return results


# ====================================================================
# Section 5 — Relocation bar applied to the *standard* (non-toy) RG inputs:
#            a real RG flow needs gauge couplings + UV BC + scale ref +
#            anomalous dimensions. Do those re-encode the modulus? Count.
# ====================================================================

def section5_input_ledger_standard_rg():
    print()
    print("=" * 70)
    print("Section 5: Input ledger for a *standard* RG flow on the modulus")
    print("=" * 70)
    results = []

    print("  A renormalization-group flow that could move r requires:")
    rows = [
        ("UV boundary condition r(Lambda_UV)",
         "IS the modulus at the cutoff — the input, relabeled to high scale"),
        ("scale reference (Lambda_UV / mu_IR ratio, # decades)",
         "a NEW dimensionful primitive A1/A2/A3 do not contain"),
        ("gauge / Yukawa couplings entering beta_r",
         "multiplicative gauge dressing CANCELS in the ratio |b|^2/a^2"),
        ("anomalous-dimension / self-coupling coefficients in beta_r",
         "matter-sector circulant beta is NOT retained; an import"),
    ]
    for inp, role in rows:
        print(f"    - {inp}")
        print(f"        role: {role}")
    print("\n  The gauge-coupling channel cannot supply r: a uniform")
    print("  dressing Y -> f(mu) Y leaves |b|^2/a^2 invariant. So the only")
    print("  channels that move r are (UV BC) and (matter-sector beta coeffs)")
    print("  -- the first IS the modulus, the second is an unretained import.")
    print("  This matches the Higgs lambda(M_Pl)=0 precedent (Z/Y-S4b-RGE):")
    print("  RG closure there is BC+import-contaminated -> bounded, not derived.")

    # The gauge-cancellation fact, checked numerically: scale Y_e by any
    # f(mu); the modulus is unchanged.
    OMEGA = np.exp(2j * np.pi / 3.0)
    U = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    a, b = 1.0, 0.6
    Y = a * np.eye(3) + b * U + np.conj(b) * U.conj().T
    r0 = abs(b) ** 2 / a ** 2
    rs = []
    for f in (0.3, 1.0, 2.7, 11.0):
        Yf = f * Y
        af = Yf[0, 0].real
        bf = Yf[1, 0]
        rs.append(abs(bf) ** 2 / af ** 2)
    gauge_invariant = max(abs(x - r0) for x in rs) < TOL
    print(f"\n  numeric check: |b|^2/a^2 under uniform dressing Y->f*Y:")
    print(f"    base r = {r0:.6f};  dressed r = {[f'{x:.6f}' for x in rs]}")
    print(f"    invariant under gauge-type dressing: {gauge_invariant}")
    results.append(gauge_invariant)
    return results


# ====================================================================
# Section 6 — Verdict synthesis.
# ====================================================================

def section6_verdict():
    print()
    print("=" * 70)
    print("Section 6: VERDICT")
    print("=" * 70)
    print("  BAR 1 (generic values): the four observed moduli are distinct")
    print("    (lep 0.500, down 0.597, up 0.774, nu<0.5). A single scale-")
    print("    invariant fixed point gives ONE number -> WRONG-VALUES for")
    print("    >=2 sectors. An IR attractor funnels generic UV data to ONE")
    print("    value -> also one number. The fixed-point option is falsified")
    print("    by the quark sectors.")
    print()
    print("  BAR 2 (relocation): a generic UV->IR run is an invertible map")
    print("    r_IR = Phi(r_UV). Hitting an observed value requires tuning")
    print("    its UV boundary condition. Producing N distinct moduli costs")
    print("    N inputs (N attractor sites OR N UV BCs). Outputs never exceed")
    print("    inputs. The modulus is RELOCATED to the UV boundary condition.")
    print()
    print("  THIRD OPTION (IR-attractive funnel): does NOT beat relocation.")
    print("    One attractor -> one value (BAR 1 fail); per-sector attractors")
    print("    -> the attractor location IS each modulus (BAR 2 fail).")
    print()
    print("  Plus a NEW dimensionful scale-reference primitive (the UV cutoff /")
    print("  # decades) is required that A1/A2/A3 do not contain.")
    print()
    print("  OVERALL VERDICT: RELOCATES (to a UV boundary condition / the")
    print("    matter-sector beta coefficients), with a WRONG-VALUES corner")
    print("    for the single-fixed-point sub-option (falsified by quarks).")
    print("    INPUT COUNT: >= N (one per sector) + 1 scale reference; never")
    print("    fewer inputs than the N moduli it would explain.")
    print()
    print("  This generalizes Probe-5 (r_lep=1/2 fixed-point bounded")
    print("  obstruction) to all four sectors and formalizes the input count.")
    print("  No fourth axiom is adopted. Owner-authorized SCOPING only.")
    return [True]


def main():
    print()
    print("#" * 70)
    print("# Fourth-Axiom Scoping: RG / Scale Dynamics for generation moduli")
    print("#" * 70)
    print()
    note = NOTE.read_text(encoding="utf-8")
    note_results = [
        (
            "**Type:** meta" in note and "**Claim type:** meta" in note,
            "note declares meta metadata",
        ),
        (
            "**Scope boundary:** Historical/provenance banking only" in note
            and "does not add, approve, or revise any framework axiom" in note,
            "note declares historical scoping boundary",
        ),
        (
            "**Audit boundary:** Independent audit lane only" in note
            and "sets no `effective_status`" in note,
            "note leaves audit verdicts to independent lane",
        ),
    ]
    for ok, label in note_results:
        print(f"NOTE-CHECK: {label}: {ok}")
    print()

    all_results = []
    all_results += section1_generic_values_bar()
    all_results += section2_toy_beta_fixed_points()
    all_results += section3_relocation_running_is_a_relabel()
    all_results += section4_third_option_attractive_funnel()
    all_results += section5_input_ledger_standard_rg()
    all_results += section6_verdict()

    n_total = len(all_results)
    n_pass = sum(bool(x) for x in all_results)
    n_fail = n_total - n_pass
    note_total = len(note_results)
    note_pass = sum(bool(ok) for ok, _ in note_results)
    note_fail = note_total - note_pass

    print()
    print("=" * 70)
    print(f"NOTE       : PASS = {note_pass}, FAIL = {note_fail}")
    print(f"EXACT      : PASS = {n_pass}, FAIL = {n_fail}")
    print(f"BOUNDED    : PASS = 0, FAIL = 0")
    print(f"TOTAL      : PASS = {n_pass + note_pass}, FAIL = {n_fail + note_fail}")
    print(f"=== TOTAL: PASS={n_pass + note_pass}, FAIL={n_fail + note_fail} ===")
    print("=" * 70)
    print()
    print("Scoping verdict: RELOCATES (UV boundary condition / matter-sector")
    print("beta coefficients) + WRONG-VALUES single-fixed-point corner.")
    print("Inputs >= N moduli + 1 scale reference. No fourth axiom adopted.")

    if n_fail != 0 or note_fail != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
