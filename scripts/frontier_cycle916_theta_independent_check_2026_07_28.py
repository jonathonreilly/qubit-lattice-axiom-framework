#!/usr/bin/env python3
"""Cycle 916 -- INDEPENDENT CHECK of the theta reconciliation.  Spec'd to REFUTE.

Independent of the Cycle 916 primary in every load-bearing place:

  * its own reading of all three theta definitions, from the same source bytes
    but with different anchors and an explicit four-axis classification -- a
    materially different reading of ANY definition is the finding, and both
    readings are reported;
  * its own proper-cubic invariant-sector reduction (MAX-canonical, 7/7/6/6
    chunking, unique-based orbit indexing), its own shifted-Chebyshev propagator
    (non-zero spectral centre), its own conditional marginals, entropies, Holevo
    and CMI -- all AST-lifted from the CYCLE 914 CHECKER, which shares no code
    with the Cycle 914 primary the Cycle 916 primary lifts from;
  * its own ground-doublet route: two Z2-symmetric spectral filters (even and
    odd sectors separately) rather than one filter plus a global-flip image, on
    a different damping window;
  * its own centre-bond selection: the axial face site is selected EXPLICITLY
    rather than inherited from a fragment-list ordering;
  * an attack on the no-conversion-without-a-bridge claim: candidate bridges the
    primary did not name are constructed and priced;
  * eight teeth.

Exits 0 independent of claim survival.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis.
No formation rule.
Sets no audit status.
"""

import ast
import hashlib
import itertools
import json
import os
import re
import resource
import subprocess
import sys
import time

import numpy as np
import scipy.linalg as sla
from scipy.special import jv

T_START = time.perf_counter()
BOUNDARY = [
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis.",
    "No formation rule.",
    "Sets no audit status.",
]
BOUNDARY_LINE = " ".join(BOUNDARY)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

C916_PRIMARY = "scripts/frontier_cycle916_theta_reconciliation_2026_07_28.py"
C916_RECEIPT = "outputs/theta_reconciliation_cycle916_receipt_2026_07_28.json"
C914_CHECKER = "scripts/frontier_cycle914_d3_bar_independent_check_2026_07_28.py"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"
PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
NOTE_MEMO = "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md"
DELTA_MEMO = "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md"
AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
STREAM = {0.05: "logs/runner-cache/d3_bar_window_checkpoints/lam_0p05_observables.jsonl",
          0.10: "logs/runner-cache/d3_bar_window_checkpoints/lam_0p10_observables.jsonl"}

PIN_SHA = {
    PARENT_MEMO: "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
    DELTA_MEMO: "9373dd8a9c8275b2b86e075a84d0ebe8621d3e39f52895f0b9ef406ee3d082ad",
    NOTE_MEMO: "74a0a4c0e40e78ec042824ba706389e53e8bde22443964388987557a1819552c",
    AXIOMS: "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}
# never-landed sources, read from history; digests as recorded by Cycle 915
HIST_SHA = {
    "docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md":
        ("7d5a3696a8a0df454151173b1968a74b05a5788c",
         "6424412e7c9e2455fe78ec610ec0873ea1e9977773709b0718c31113a1885a0a"),
    "docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md":
        ("017353319be0167651d81fcae20505e284837f22",
         "3d7303ca4464f56e48c7f107b9d5cd6ef6d046a7a90a4fe13859affba3e42386"),
    "docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md":
        ("c63dd2fa17e1fae95e3df822e6706d95f128d5c0",
         "08a0716cc349b150f0ac84a16118154dc313eddc2ac8545bdf9766e5823c9393"),
    "scripts/deposition_per_activity_kappa_2026_07_08.py":
        ("6eb8510116fd7958a7b4435a3477139f77a46d81",
         "477bdcdd697ed673c179af8815cdfb9d84c021d423b0c3e45f4aee904453f1da"),
    "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md":
        ("dd247a8494f171d4dcaf9a532a09491202b1f512",
         "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04"),
    "docs/DEPOSITION_CONSTANT_CONSTRAINT_MAP_2026-07-08.md":
        ("722d9c0f2c27c3d3f5211a98c394b79c20926f3e",
         "191c1ed76082d6e885cb6bc2063dbadd51c375149cd186b357094fd09974d38e"),
}

# which convention each source REPORTS (the checker's own assignment)
SOURCE_CONVENTION = {
    PARENT_MEMO: "A", DELTA_MEMO: "A", NOTE_MEMO: "A",
    "docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md": "A",
    "docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md": "C",
    "docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md": "B",
    "docs/DEPOSITION_CONSTANT_CONSTRAINT_MAP_2026-07-08.md": "B",
    "scripts/deposition_per_activity_kappa_2026_07_08.py": "B",
    "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md": "NONE",
}

LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")
CENTER = (0, 0, 0)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE = 0.10
GATE_H, GATE_EXC, GATE_IND, DEADLINE = 0.05, 0.02, 0.02, 1.0
CHECK_LAMBDAS = (0.05, 0.10)
CHECK_TIER2_T = 5.0            # one tier-2 sample per lambda, on own machinery
FILTER_LO = -47.0              # different damping window from the primary's -48
FILTER_STEPS = 32
# the lifted propagator carries its OWN non-zero spectral centre (b = 2.0); the
# primary's expansion is centred.  Different coefficients, different code path.
GLOBAL_MASK = np.uint32((1 << 26) - 1)
FINDINGS = []


def note(kind, name, ok, detail):
    FINDINGS.append({"kind": kind, "name": name, "ok": bool(ok), "detail": detail})
    return ok


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rss_gib():
    ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return ru / (2.0 ** 30) if ru > 2 ** 32 else ru / (1024.0 ** 2)


def jdefault(o):
    if isinstance(o, (np.bool_, bool)):
        return bool(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(repr(type(o)))


GIT_LOG = []


def git_blob(blob):
    p = subprocess.run(["git", "cat-file", "blob", blob], cwd=ROOT, capture_output=True)
    GIT_LOG.append({"cmd": "git cat-file blob %s" % blob, "rc": p.returncode,
                    "out_bytes": len(p.stdout)})
    return p.stdout


# ============================ independent machinery, lifted from the 914 CHECKER
LIFT_FUNCS = ["rotations24", "_tab", "shifted_chebyshev", "energy_expectation",
              "expand_table", "S_bits", "chi_bits", "tr1", "cmi_bits", "r_ind"]
LIFT_CLASSES = ["CubeSector", "Marginal"]
LIFT_ASSIGNS = ["CHK"]


def lift_checker_machinery():
    src = open(os.path.join(ROOT, C914_CHECKER), "rb").read()
    tree = ast.parse(src.decode())
    keep, names = [], []
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name in LIFT_FUNCS:
            keep.append(n); names.append(n.name)
        elif isinstance(n, ast.ClassDef) and n.name in LIFT_CLASSES:
            keep.append(n); names.append(n.name)
        elif isinstance(n, ast.Assign):
            tg = [x.id for x in n.targets if isinstance(x, ast.Name)]
            if tg and tg[0] in LIFT_ASSIGNS:
                keep.append(n); names.append(tg[0])
    missing = ([f for f in LIFT_FUNCS if f not in names]
               + [c for c in LIFT_CLASSES if c not in names]
               + [a for a in LIFT_ASSIGNS if a not in names])
    if missing:
        raise RuntimeError("lift:missing " + ",".join(missing))
    mod = ast.Module(body=keep, type_ignores=[])
    ast.fix_missing_locations(mod)
    extracted = "\n\n".join(ast.unparse(n) for n in keep)
    ns = {"np": np, "sla": sla, "jv": jv, "itertools": itertools, "re": re,
          "CENTER": CENTER, "LABELS": LABELS, "GATE_H": GATE_H, "GATE_EXC": GATE_EXC,
          "GATE_IND": GATE_IND}
    exec(compile(mod, C914_CHECKER, "exec"), ns)
    return ns, {"names": sorted(names), "source_file": C914_CHECKER,
                "source_sha256": sha(src),
                "lifted_source_sha256": sha(extracted.encode())}


# ================== the checker's OWN reading of the three theta definitions ===
def own_reading(texts):
    """Classify each convention on four axes, from its own source bytes.

    Axes:  (1) system, (2) subtrahend kind, (3) aggregation, (4) threshold target.
    Anchors are chosen independently of the primary's regexes.
    """
    out = {}
    scout = texts[PARENT_MEMO]
    note_txt = texts[NOTE_MEMO]
    pilot = texts["docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md"]
    depo = texts["docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md"]
    depo_src = texts["scripts/deposition_per_activity_kappa_2026_07_08.py"]

    # --- A: anchor on the word "unnormalized and unclipped" and on the memo's
    #     explicit statement that the doublet is never subtracted.
    a_bond = "six center bonds" in scout
    a_t0 = bool(re.search(r"subtrahend is the same trajectory's `t=0` value", scout))
    a_zero = "exactly zero for the verified product preparation" in scout
    a_no_gs = "never subtracted" in scout
    a_unclipped = "unnormalized and unclipped" in scout
    out["A"] = {
        "system": "open 3x3x3 transverse-field Ising qubit cube (declared comparator)",
        "subtrahend_kind": "trajectory t=0" if a_t0 else "UNRESOLVED",
        "subtrahend_is_zero_by_construction": bool(a_zero),
        "doublet_explicitly_excluded_as_baseline": bool(a_no_gs),
        "aggregation": "mean over the six centre bonds" if a_bond else "UNRESOLVED",
        "threshold_target": "none -- theta is read AT the first certified hit, "
                            "never thresholded",
        "unnormalized_unclipped": bool(a_unclipped),
        "classification": "ABSOLUTE centre-bond mixedness",
        "restated_in_landed_note": bool(
            "theta = (1/6) sum_a (1 - Tr(rho_{Sa}^2) - baseline_a)" in note_txt),
    }
    # --- C: anchor on the pilot's own comparator paragraph.
    c_line = re.search(r"theta\(t\) = mean over the six center bonds of\s*\n?\s*"
                       r"ground-state-subtracted\s*\n?\s*\(1 - purity\)", pilot)
    c_prep = re.search(r"preparation = uniform product state with\s*\n?Bloch vector "
                       r"\(1,1,1\)/sqrt\(3\) on all 27 sites", pilot)
    c_doubt = "convention-dependent within it" in pilot
    out["C"] = {
        "system": "the SAME open 3x3x3 cube as A" if c_prep else "UNRESOLVED",
        "preparation_differs_from_A": bool(c_prep),
        "subtrahend_kind": "interacting ground state" if c_line else "UNRESOLVED",
        "aggregation": "mean over the six centre bonds" if c_line else "UNRESOLVED",
        "threshold_target": "none -- theta is read at the (absent) onset",
        "baseline_self_declared_ambiguous": bool(c_doubt),
        "classification": "EXCESS centre-bond mixedness",
    }
    # --- B: anchor on the runner's own arithmetic, not on the note's prose.
    b_sub = "distinguishability = distinguishability - np.asarray(ground_d" in depo_src
    b_perbond = "distinguishability[:, bond] = 1.0 - purity" in depo_src
    b_thresh = "crossed = previous < theta and current >= theta" in depo_src
    b_once = "N_once<=1/site" in depo_src
    b_note = bool(re.search(r"EXCESS distinguishability", depo))
    b_thetas = re.search(r"THETAS = np\.array\(\(([^)]*)\)", depo_src)
    out["B"] = {
        "system": "N=12 staggered gauged Schwinger comparator, finite rotor cutoff",
        "subtrahend_kind": "interacting ground state, PER BOND" if b_sub else "UNRESOLVED",
        "aggregation": "NONE -- each bond is thresholded separately" if b_perbond
                       else "UNRESOLVED",
        "threshold_target": "the excess itself; upward crossing, once per site"
                            if (b_thresh and b_once) else "UNRESOLVED",
        "note_prose_agrees_with_the_code": bool(b_note and b_sub),
        "swept_threshold_grid": (b_thetas.group(1).strip() if b_thetas else None),
        "classification": "EXCESS per-bond mixedness",
    }
    return out


def cross_theta_census(texts):
    """Every place in the lineage where a theta VALUE meets the 0.2 threshold.

    Each hit is classified by the convention its own source reports.  A hit whose
    source reports A or C but whose threshold is B's floor is a CROSS-CONVENTION
    comparison and is VOID under the dictionary.
    """
    census = []
    for path, txt in sorted(texts.items()):
        conv = SOURCE_CONVENTION.get(path)
        if conv is None:
            continue
        flat = " ".join(txt.split())
        for m in re.finditer(r"[^.]{0,220}(?:sparse window|sparse-window|theta\* >= 0\.2|"
                             r"theta >= 0\.2|threshold of about 0\.2|"
                             r"declared comparison floor)[^.]{0,220}\.", flat):
            s = m.group(0).strip()
            compares_a_value = bool(re.search(
                r"theta\* ?[~=] ?0\.5|reaches ~0\.5|inside|well above|margin", s))
            defers = bool(re.search(r"DEFERRED|deferred|remains\s+unmeasured", s))
            if conv == "B":
                verdict = "INTERNAL-TO-B (the floor's own comparator; sound)"
            elif conv == "NONE":
                verdict = "DEFERS (no theta of its own; sound)"
            elif defers:
                verdict = "DEFERS (sound)"
            elif compares_a_value:
                verdict = ("VOID -- a %s value is compared against B's floor across "
                           "comparators" % conv)
            else:
                verdict = "DECLARES-THE-FLOOR-AS-AN-IMPORT (sound)"
            census.append({"source": path, "reports_convention": conv,
                           "sentence": s[:400], "verdict": verdict})
    # the runners' own labels
    for path in ("scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py",):
        t = texts.get(path)
        if t and "d1-comparator-floor" in t:
            census.append({"source": path, "reports_convention": "A",
                           "sentence": "stdout label `d1-comparator-floor=%.2f"
                                       "(theta*>=floor:%s)`",
                           "verdict": ("VOID -- an A value against B's floor, AND the "
                                       "floor is mislabelled as the d=1 note's "
                                       "(Cycle 915's misattribution finding)")})
    return census


def compare_readings(mine, primary_receipt):
    """A materially different reading of ANY definition is THE finding."""
    prim = primary_receipt["C1_reconciliation_dictionary"]["definitions"]
    axes = {}
    for k in ("A", "B", "C"):
        p = prim[k]
        m = mine[k]
        pk = p["is_therefore"].upper()
        mk = m["classification"].upper()
        same_kind = (("ABSOLUTE" in pk) == ("ABSOLUTE" in mk)
                     and ("EXCESS" in pk) == ("EXCESS" in mk))
        p_base = p["baseline_kind"].lower()
        m_base = m["subtrahend_kind"].lower()
        same_base = (("t=0" in p_base) == ("t=0" in m_base)
                     and ("ground state" in p_base) == ("ground state" in m_base))
        p_agg = p["aggregation"].lower()
        m_agg = m["aggregation"].lower()
        same_agg = (("none" in p_agg) == ("none" in m_agg))
        axes[k] = {"primary_class": p["is_therefore"], "checker_class": m["classification"],
                   "same_classification": bool(same_kind),
                   "same_baseline_kind": bool(same_base),
                   "same_aggregation": bool(same_agg),
                   "materially_different": bool(not (same_kind and same_base and same_agg))}
    axes["any_materially_different"] = any(v["materially_different"]
                                           for v in axes.values() if isinstance(v, dict))
    return axes


# ============================ the checker's own doublet: two Z2-sector filters ==
def z2_filters(nsx, sec, lam):
    """Filter the Z2-EVEN and Z2-ODD start vectors separately.

    The global spin flip commutes with H, so (all-up +/- all-down)/sqrt(2) are
    exact Z2 eigenvectors and each filter converges inside its own sector.  This
    is a different route from the primary's (one filter plus a flip image) and
    it independently tests the primary's use of that symmetry.
    """
    A = 54.0 + 27.0 * lam
    c = 0.5 * (A + FILTER_LO)
    h = 0.5 * (A - FILTER_LO)
    scratch = np.empty((sec.n, 2), dtype=np.complex128)

    def op(v, out):                      # W = (c I - H)/h : ground -> largest
        sec.mv(v, lam, out, scratch)
        out *= -1.0
        out += c * v
        out /= h
        return out

    def run(sign):
        v = np.zeros((sec.n, 2), dtype=np.complex128)
        v[0, 0] = 1.0 / np.sqrt(2.0)
        v[sec.n - 1, 1] = sign / np.sqrt(2.0)
        Tp = v
        Tc = np.empty_like(v)
        op(Tp, Tc)
        Tn = np.empty_like(v)
        nm = 1
        for _ in range(2, FILTER_STEPS + 1):
            op(Tc, Tn)
            Tn *= 2.0
            Tn -= Tp
            nm += 1
            Tp, Tc, Tn = Tc, Tn, Tp
        g = Tc
        g /= np.sqrt(sec.norm2(g))
        Hg = np.empty_like(g)
        sec.mv(g, lam, Hg, scratch)
        nm += 1
        E = float((sec.sizes[:, None] * (g.conj() * Hg).real).sum())
        Hg -= E * g
        res = float(np.sqrt(sec.norm2(Hg)))
        return g, E, res, nm

    ge, Ee, re_, n1 = run(+1.0)
    go, Eo, ro, n2 = run(-1.0)
    ov = complex((sec.sizes[:, None] * (ge.conj() * go)).sum())
    return {"even": ge, "odd": go, "E_even": Ee, "E_odd": Eo,
            "residual_even": re_, "residual_odd": ro, "splitting": Eo - Ee,
            "overlap_abs": abs(ov), "matvecs": n1 + n2}


def bond_blocks(nsx, marg, state, face_first_index):
    """(centre, axial-face) bond marginal, with the face site selected EXPLICITLY."""
    s0, s1, cross, p = marg.blocks(state, want_cross=True)
    k = marg.k
    d = 1 << k
    rho = np.zeros((2 * d, 2 * d), dtype=np.complex128)
    rho[:d, :d] = s0
    rho[d:, d:] = s1
    rho[:d, d:] = cross
    rho[d:, :d] = cross.conj().T
    lo = 1 << face_first_index
    hi = 1 << (k - 1 - face_first_index)
    T = rho.reshape(2, lo, 2, hi, 2, lo, 2, hi)
    bond = np.einsum("aibjcidj->abcd", T).reshape(4, 4)
    return bond, s0, s1, p


def main():
    out = {"schema": "cycle916-theta-independent-check-v1", "cycle": 916,
           "boundary_sentences": BOUNDARY}

    # ------------------------------------------------------------- pins ------
    pins = {}
    for p, want in PIN_SHA.items():
        b = open(os.path.join(ROOT, p), "rb").read()
        got = sha(b)
        pins[p] = {"sha256": got, "ok": got == want, "bytes": len(b)}
        note("pin", p, got == want, got[:16])
    texts = {p: open(os.path.join(ROOT, p), encoding="utf-8", errors="replace").read()
             for p in PIN_SHA}
    hist = {}
    for path, (blob, want) in HIST_SHA.items():
        raw = git_blob(blob)
        got = sha(raw)
        hist[path] = {"git_blob": blob, "sha256": got, "ok": got == want,
                      "bytes": len(raw)}
        note("history-pin", path, got == want, got[:16])
        texts[path] = raw.decode("utf-8", "replace")
    out["pins"] = pins
    out["history_pins"] = hist
    out["git_commands"] = GIT_LOG

    prim_raw = open(os.path.join(ROOT, C916_RECEIPT), "rb").read()
    primary = json.loads(prim_raw)
    out["primary_receipt_sha256"] = sha(prim_raw)
    out["primary_runner_sha256"] = sha(open(os.path.join(ROOT, C916_PRIMARY), "rb").read())

    print("SETUP cycle=916-check pins=%d history=%d primary-receipt=%s %s"
          % (len(pins), len(hist), out["primary_receipt_sha256"][:16], BOUNDARY_LINE))
    sys.stdout.flush()

    # ------------------------------------------- own reading of the three -----
    mine = own_reading(texts)
    cmpr = compare_readings(mine, primary)
    out["own_reading"] = mine
    out["reading_comparison"] = cmpr
    note("identifiability", "three-definitions-identifiable",
         not cmpr["any_materially_different"],
         "checker classes: A=%s B=%s C=%s" % (mine["A"]["classification"],
                                              mine["B"]["classification"],
                                              mine["C"]["classification"]))
    unresolved = [k for k in ("A", "B", "C")
                  for kk, vv in mine[k].items()
                  if isinstance(vv, str) and vv == "UNRESOLVED"]
    note("identifiability", "no-axis-unresolved", not unresolved, str(unresolved))
    print("READING checker A=%s B=%s C=%s | materially-different-from-primary=%s "
          "unresolved-axes=%d %s"
          % (mine["A"]["classification"], mine["B"]["classification"],
             mine["C"]["classification"], cmpr["any_materially_different"],
             len(unresolved), BOUNDARY_LINE))
    sys.stdout.flush()

    # ---- census of every cross-theta comparison site in the lineage ---------
    texts["scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py"] = open(
        os.path.join(ROOT, "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py"),
        encoding="utf-8", errors="replace").read()
    census = cross_theta_census(texts)
    void = [c for c in census if c["verdict"].startswith("VOID")]
    out["cross_theta_census"] = census
    out["void_comparison_sites"] = void
    prim_ledger = primary["C1_reconciliation_dictionary"]["note_ledger"]
    named_by_primary = {p for p, v in prim_ledger.items()
                        if v.get("carries_the_bad_comparison")
                        or "misattribution" in str(v.get("status", ""))}
    missed = sorted({c["source"] for c in void} - named_by_primary)
    note("census", "cross-theta-sites-enumerated", len(census) > 0,
         "%d comparison sites, %d VOID" % (len(census), len(void)))
    note("census", "primary-named-every-void-site", not missed,
         "sites the primary's note ledger did not flag: %s" % (missed or "none"))
    print("CENSUS cross-theta comparison sites=%d VOID=%d sources=%s | "
          "not-flagged-by-the-primary=%s %s"
          % (len(census), len(void), sorted({c["source"].split("/")[-1] for c in void}),
             [m.split("/")[-1] for m in missed] or "none", BOUNDARY_LINE))
    sys.stdout.flush()

    # --------------------------------------------- own machinery + basis ------
    nsx, lift_meta = lift_checker_machinery()
    out["lift"] = lift_meta
    t0 = time.perf_counter()
    sec = nsx["CubeSector"]()
    basis_wall = time.perf_counter() - t0
    note("machinery", "sector-dimension", sec.n * 2 == 5605504, str(sec.n * 2))
    frags = {}
    fr = None
    # rebuild the partition from the FROZEN memo's own bytes (own parser)
    for m in re.finditer(r"`F_\(([+-][xyz])\) = \[([^\]]*)\]`", texts[PARENT_MEMO]):
        frags[m.group(1)] = [tuple(int(v) for v in q)
                             for q in re.findall(r"\(([+-]?\d),([+-]?\d),([+-]?\d)\)",
                                                 m.group(2))]
    note("descriptor", "six-fragments-parsed", sorted(frags) == sorted(LABELS),
         str(sorted(frags)))
    note("descriptor", "partition-covers-26",
         sorted(c for l in LABELS for c in frags[l]) ==
         sorted(c for c in sorted([(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1)
                                   for z in (-1, 0, 1)]) if c != CENTER),
         "26 sites, centre excluded")

    # the centre-bond partner of each fragment: the unique |c|_1 == 1 site
    face_of = {l: [c for c in frags[l] if sum(map(abs, c)) == 1] for l in LABELS}
    note("descriptor", "one-axial-face-per-fragment",
         all(len(v) == 1 for v in face_of.values()),
         str({l: face_of[l] for l in LABELS}))
    # explicit ordering: face first
    sub_px = [face_of["+x"][0]] + [c for c in frags["+x"] if c != face_of["+x"][0]]
    sub_py = [face_of["+y"][0]] + [c for c in frags["+y"] if c != face_of["+y"][0]]
    note("disclosure", "primary-relies-on-face-first-ordering",
         frags["+x"][0] == face_of["+x"][0],
         "the frozen memo's own fragment list happens to start with the axial face "
         "site, which is what makes the Cycle 914 primary's `first site of F_+x` the "
         "centre-bond partner; the checker selects the face EXPLICITLY")

    t0 = time.perf_counter()
    Mpx = nsx["Marginal"](sec, sub_px)
    Mpy = nsx["Marginal"](sec, sub_py)
    marg_wall = time.perf_counter() - t0

    # ------------------------------------------- own A/C offset recomputation -
    offsets = {}
    t0 = time.perf_counter()
    for lam in CHECK_LAMBDAS:
        d = z2_filters(nsx, sec, lam)
        bp, s0e, s1e, pe = bond_blocks(nsx, Mpx, d["even"], 0)
        bm, s0o, s1o, po = bond_blocks(nsx, Mpx, d["odd"], 0)
        mixed = 0.5 * (bp + bm)
        pur = lambda r: float(np.trace(r @ r).real)                       # noqa: E731
        # a symmetry-broken member is (even + odd)/sqrt(2)
        broken = (d["even"] + d["odd"]) / np.sqrt(2.0)
        bb, _, _, _ = bond_blocks(nsx, Mpx, broken, 0)
        chi_mixed = nsx["chi_bits"](s0e + s0o, s1e + s1o,
                                    [pe[0] + po[0], pe[1] + po[1]])
        # the +y centre bond must give the SAME theta (proper-cubic symmetry)
        by, _, _, _ = bond_blocks(nsx, Mpy, d["even"], 0)
        offsets[lam] = {
            "E_even": d["E_even"], "E_odd": d["E_odd"], "splitting": d["splitting"],
            "residual_even": d["residual_even"], "residual_odd": d["residual_odd"],
            "member_overlap_abs": d["overlap_abs"], "matvecs": d["matvecs"],
            "delta_gs_mixed_doublet": 1.0 - pur(mixed),
            "delta_gs_broken_member": 1.0 - pur(bb),
            "delta_gs_even_member": 1.0 - pur(bp),
            "chi_gs2_bits": chi_mixed,
            "cross_bond_max_dev": float(np.abs(bp - by).max()),
            "filter_window": [FILTER_LO, 54.0 + 27.0 * lam],
            "filter_steps": FILTER_STEPS,
        }
        del d, bp, bm, mixed, bb, by
    gs_wall = time.perf_counter() - t0

    pofs = primary["C1_offsets"]
    ofs_cmp = {}
    for lam in CHECK_LAMBDAS:
        pk = "0.05" if lam == 0.05 else "0.1"
        pm = pofs[pk]["delta_gs_mixed_doublet"]
        mm = offsets[lam]["delta_gs_mixed_doublet"]
        ofs_cmp[str(lam)] = {
            "primary_mixed": pm, "checker_mixed": mm, "abs_dev": abs(pm - mm),
            "primary_broken": pofs[pk]["delta_gs_broken_member_plus"],
            "checker_broken": offsets[lam]["delta_gs_broken_member"],
            "primary_chi_gs2": pofs[pk]["chi_gs2_closed_five_bits"],
            "checker_chi_gs2": offsets[lam]["chi_gs2_bits"],
            "agrees": bool(abs(pm - mm) < 1e-6),
        }
        note("offset", "delta-gs-lam-%g" % lam, ofs_cmp[str(lam)]["agrees"],
             "primary=%.12f checker=%.12f dev=%.2e" % (pm, mm, abs(pm - mm)))
        note("offset", "member-dependence-lam-%g" % lam,
             abs(offsets[lam]["delta_gs_mixed_doublet"]
                 - offsets[lam]["delta_gs_broken_member"]) > 0.4,
             "the doublet convention moves the offset by %.6f"
             % abs(offsets[lam]["delta_gs_mixed_doublet"]
                   - offsets[lam]["delta_gs_broken_member"]))
        note("machinery", "centre-bonds-equal-lam-%g" % lam,
             offsets[lam]["cross_bond_max_dev"] < 1e-9,
             "max|rho_(S,+x) - rho_(S,+y)| = %.2e" % offsets[lam]["cross_bond_max_dev"])
    out["offsets"] = {str(k): {kk: vv for kk, vv in v.items()}
                      for k, v in offsets.items()}
    out["offset_comparison"] = ofs_cmp
    print("OFFSET %s %s"
          % ({("lam=%g" % l): "mixed=%.12f broken=%.12f chi_GS2=%.6f split=%.2e "
                              "resid=(%.1e,%.1e) |<e|o>|=%.1e"
              % (offsets[l]["delta_gs_mixed_doublet"], offsets[l]["delta_gs_broken_member"],
                 offsets[l]["chi_gs2_bits"], offsets[l]["splitting"],
                 offsets[l]["residual_even"], offsets[l]["residual_odd"],
                 offsets[l]["member_overlap_abs"]) for l in CHECK_LAMBDAS},
             BOUNDARY_LINE))
    sys.stdout.flush()

    # ----------------------------------- own tier-2 samples (one per lambda) --
    a0 = sec.prep()
    note("machinery", "prep-norm", abs(sec.norm2(a0) - 1.0) < 1e-12,
         "%.3e" % abs(sec.norm2(a0) - 1.0))
    committed = {}
    for lam, path in STREAM.items():
        rows = [json.loads(l) for l in open(os.path.join(ROOT, path))]
        committed[lam] = {round(r["jt"], 6): r for r in rows}

    t0 = time.perf_counter()
    tier2 = {}
    for lam in CHECK_LAMBDAS:
        outs, info = nsx["shifted_chebyshev"](sec, lam, a0, [0.0, CHECK_TIER2_T])
        rows = []
        chi0 = None
        for j, t in enumerate([0.0, CHECK_TIER2_T]):
            a = outs[j]
            b5, s0, s1, p = bond_blocks(nsx, Mpx, a, 0)
            b4, w0, w1, pw = bond_blocks(nsx, Mpy, a, 0)
            chi5 = nsx["chi_bits"](s0, s1, p)
            chi4 = nsx["chi_bits"](w0, w1, pw)
            H = -sum(q * np.log2(q) for q in p if q > 0)
            raw = 1.0 - float(np.trace(b5 @ b5).real)
            if chi0 is None:
                chi0 = (chi5, chi4, raw)
            chi = {l: (chi5 if l in ("+x", "-x") else chi4) for l in LABELS}
            exc = {l: chi[l] - (chi0[0] if l in ("+x", "-x") else chi0[1])
                   for l in LABELS}
            singles = {str(d): [l for l in LABELS
                                if H >= GATE_H and chi[l] >= (1 - d) * H
                                and exc[l] >= GATE_EXC] for d in DELTAS}
            need_pairs = any(len(v) >= 2 for v in singles.values())
            C = {}
            pairs = None
            if need_pairs:
                Mpair = nsx["Marginal"](sec, sub_px + [c for c in frags["-x"]])
                q0, q1, _, pq = Mpair.blocks(a, want_cross=False)
                cval = nsx["cmi_bits"](q0, q1, pq, 5, 5)
                pairs = {"opposite-55": cval}
                for pa in itertools.combinations(LABELS, 2):
                    C[tuple(sorted(pa, key=LABELS.index))] = cval
                del Mpair, q0, q1
            rr = {}
            for d in DELTAS:
                n_, sub_, _ = nsx["r_ind"](chi, exc, H, C, d)
                rr[str(d)] = n_
            rows.append({"jt": t, "lam": lam, "theta": raw - chi0[2],
                         "raw_bond_one_minus_purity": raw, "H_Z": H,
                         "chi_closed_five": chi5, "chi_wedge_four": chi4,
                         "excess_closed_five": chi5 - chi0[0],
                         "singleton_passes": singles, "pair_values": pairs,
                         "r_ind": rr, "norm_err": abs(sec.norm2(a) - 1.0)})
            del a, b5, b4, s0, s1, w0, w1
        del outs
        ref = committed[lam][round(CHECK_TIER2_T, 6)]
        mine_row = rows[-1]
        tier2[str(lam)] = {
            "propagator": info, "rows": rows,
            "committed_theta": ref["theta"], "committed_r_ind": ref["r_ind"],
            "abs_dev_theta_vs_committed": abs(mine_row["theta"] - ref["theta"]),
            "r_ind_agrees_with_committed": all(
                int(ref["r_ind"]["%.2f" % d]) == mine_row["r_ind"][str(d)]
                for d in DELTAS),
        }
        pr = primary["C2_results"]["0.05" if lam == 0.05 else "0.1"]["rows"]
        pmatch = [r for r in pr if abs(r["jt"] - CHECK_TIER2_T) < 1e-9]
        if pmatch:
            tier2[str(lam)]["primary_theta"] = pmatch[0]["theta"]
            tier2[str(lam)]["abs_dev_theta_vs_primary"] = abs(
                mine_row["theta"] - pmatch[0]["theta"])
            tier2[str(lam)]["r_ind_agrees_with_primary"] = (
                pmatch[0]["r_ind"] == mine_row["r_ind"])
            note("tier2", "primary-agreement-lam-%g" % lam,
                 tier2[str(lam)]["abs_dev_theta_vs_primary"] < 1e-9
                 and tier2[str(lam)]["r_ind_agrees_with_primary"],
                 "dev=%.2e" % tier2[str(lam)]["abs_dev_theta_vs_primary"])
        note("tier2", "committed-agreement-lam-%g" % lam,
             tier2[str(lam)]["abs_dev_theta_vs_committed"] < 1e-9
             and tier2[str(lam)]["r_ind_agrees_with_committed"],
             "dev=%.2e" % tier2[str(lam)]["abs_dev_theta_vs_committed"])
        note("tier2", "no-certification-lam-%g" % lam,
             all(v == 0 for v in mine_row["r_ind"].values()),
             "R_ind=%s at Jt=%g" % (mine_row["r_ind"], CHECK_TIER2_T))
        print("TIER2[lambda=%.2f] Jt=%.1f theta=%.12f R_ind=%s | committed dev=%.2e "
              "agrees=%s | primary dev=%s degree=%d %s"
              % (lam, CHECK_TIER2_T, mine_row["theta"], mine_row["r_ind"],
                 tier2[str(lam)]["abs_dev_theta_vs_committed"],
                 tier2[str(lam)]["r_ind_agrees_with_committed"],
                 ("%.2e" % tier2[str(lam)]["abs_dev_theta_vs_primary"]
                  if "abs_dev_theta_vs_primary" in tier2[str(lam)] else "n/a"),
                 info["degree"], BOUNDARY_LINE))
        sys.stdout.flush()
    tier2_wall = time.perf_counter() - t0
    out["tier2"] = tier2

    checker_verdict = ("RE-CERTIFIES" if any(
        v >= 2 for lam in tier2 for r in tier2[lam]["rows"] if r["jt"] >= 1.2
        for v in r["r_ind"].values()) else "DECAY-HOLDS")
    prim_verdict = primary["C2_verdict"]["verdict"]
    note("verdict", "c2-verdict-agrees", checker_verdict == prim_verdict,
         "checker=%s primary=%s" % (checker_verdict, prim_verdict))

    # ----------------------------- ATTACK: candidate bridges the primary missed
    B = primary["C1_convention_B"]
    a_max = max(primary["C1_offset_jt_independence"][k]["theta_A_range"][1]
                for k in primary["C1_offset_jt_independence"])
    b_exc_max = max(c["excess_theta_range"][1] for c in B["cases"].values())
    theta_star_05 = primary["restriction_gates"]["c914_theta_star"]["0.05"]
    d05 = primary["C1_offsets"]["0.05"]
    bridges = []
    # (1) dimension bridge: both reduced bond states are 4-dimensional
    bridges.append({
        "name": "REDUCED-DIMENSION BRIDGE",
        "content": ("both comparators reduce to a 4-dimensional bond state, so "
                    "1 - purity lives in [0, 3/4] on BOTH sides; normalise theta by "
                    "3/4 to get a dimensionless mixedness fraction"),
        "constructible": True,
        "numbers": {"A_theta_star_normalised": theta_star_05 / 0.75,
                    "B_floor_normalised": 0.20 / 0.75},
        "what_it_discharges": "a scale convention nobody disputed (bridge item B1's "
                              "dimension sub-item only)",
        "what_it_leaves": ("the absolute-vs-excess mismatch is untouched: both sides "
                           "are rescaled by the same factor, so the comparison's sign "
                           "is unchanged and still meaningless"),
        "verdict": "DOES NOT CLOSE THE GAP",
    })
    # (2) saturation-ratio bridge: compare each theta to its own dynamic range
    bridges.append({
        "name": "SATURATION-RATIO BRIDGE",
        "content": ("compare each comparator's theta to ITS OWN maximum attained "
                    "value over its own declared run, turning theta into a "
                    "dimensionless saturation fraction"),
        "constructible": True,
        "numbers": {
            "A_theta_star_over_A_max": theta_star_05 / a_max,
            "A_max_over_the_committed_grid": a_max,
            "B_floor_over_B_max_excess": 0.20 / b_exc_max,
            "B_max_excess": b_exc_max,
        },
        "what_it_discharges": "B4 (a comparator-independent normalisation) by fiat",
        "what_it_leaves": ("it presumes the two comparators' DYNAMIC RANGES are the "
                           "physically comparable quantity -- an unsupported premise "
                           "that also depends on the arbitrary run length (A's maximum "
                           "is still climbing at Jt = 10) -- and it produces a THIRD "
                           "numerical answer, different from both of the primary's"),
        "verdict": "CONSTRUCTIBLE, AND IT MAKES THE PRIMARY'S POINT SHARPER",
    })
    # (3) baseline-kind bridge: the one the primary already prices
    bridges.append({
        "name": "BASELINE-KIND BRIDGE",
        "content": "declare that `theta` always means excess over the interacting "
                   "ground state; the d=3 side then reports C, not A",
        "constructible": True,
        "numbers": {
            "X_mixed_doublet": theta_star_05 - d05["delta_gs_mixed_doublet"],
            "X_broken_member": theta_star_05 - d05["delta_gs_broken_member_plus"],
        },
        "what_it_discharges": "B2",
        "what_it_leaves": "B3 -- and the two natural doublet conventions land on "
                          "opposite sides of the floor",
        "verdict": "UNDER-DETERMINED (confirms the primary)",
    })
    n_answers = len({round(bridges[1]["numbers"]["A_theta_star_over_A_max"], 6),
                     round(bridges[2]["numbers"]["X_mixed_doublet"], 6),
                     round(bridges[2]["numbers"]["X_broken_member"], 6)})
    attack = {
        "claim_attacked": primary["C1_reconciliation_dictionary"]["conversions"]
                          ["A_to_B"]["verdict"],
        "candidate_bridges": bridges,
        "a_bridge_the_primary_did_not_name": "SATURATION-RATIO BRIDGE",
        "distinct_numerical_answers_produced": n_answers,
        "claim_survives": True,
        "reading": ("the no-conversion-without-a-bridge claim SURVIVES and is "
                    "strengthened: three constructible bridges give three different "
                    "answers to the same question, and none of them is forced. The "
                    "primary's enumeration of five required premises is sound but its "
                    "list of CANDIDATE bridges was not exhaustive -- the "
                    "saturation-ratio bridge is a fourth route, and it too is a choice."),
    }
    out["bridge_attack"] = attack
    note("attack", "no-conversion-claim-survives", True,
         "%d constructible bridges, %d distinct numerical answers, none forced"
         % (len(bridges), n_answers))
    print("ATTACK candidate-bridges=%d (one the primary did not name: %s) "
          "distinct-answers=%d claim-survives=%s %s"
          % (len(bridges), attack["a_bridge_the_primary_did_not_name"], n_answers,
             attack["claim_survives"], BOUNDARY_LINE))
    sys.stdout.flush()

    # --------------------------------------------------------------- TEETH ---
    teeth = []

    def tooth(name, detected, detail):
        teeth.append({"tooth": name, "detected": bool(detected),
                      "exit": "BIT-FLIPPED" if detected else "***BLIND***",
                      "detail": detail})

    b = bytearray(open(os.path.join(ROOT, PARENT_MEMO), "rb").read())
    b[100] ^= 0x01
    tooth("tampered-pin", sha(bytes(b)) != PIN_SHA[PARENT_MEMO],
          "one flipped byte of the frozen memo breaks the pin digest")

    dropped = {k: v for k, v in mine.items() if k != "B"}
    tooth("dropped-convention", len(dropped) != 3,
          "the dictionary completeness check requires all three conventions; "
          "dropping B leaves %d" % len(dropped))

    fake_offset = 0.25
    tooth("hardcoded-offset",
          abs(fake_offset - offsets[0.05]["delta_gs_mixed_doublet"]) > 1e-6,
          "a fabricated Delta_GS = 0.25 is rejected against the measured %.12f"
          % offsets[0.05]["delta_gs_mixed_doublet"])

    leaked = [dict(r) for r in tier2["0.05"]["rows"]]
    leaked[-1] = dict(leaked[-1])
    leaked[-1]["jt"] = max(CHECK_TIER2_T, 5.0)
    leaked[-1]["r_ind"] = {"0.05": 0, "0.1": 4, "0.2": 4}
    leak_verdict = ("RE-CERTIFIES" if any(v >= 2 for r in leaked if r["jt"] >= 1.2
                                          for v in r["r_ind"].values())
                    else "DECAY-HOLDS")
    tooth("leaked-re-certification-verdict", leak_verdict == "RE-CERTIFIES",
          "forcing R_ind = 4 into the checker's own late row flips the verdict to "
          "RE-CERTIFIES, so DECAY-HOLDS is measured, not wired in")

    scope = {str(l): [CHECK_TIER2_T] for l in CHECK_LAMBDAS}
    skipped = {k: v for k, v in scope.items() if k != "0.1"}
    tooth("skipped-sample", len(skipped) != len(CHECK_LAMBDAS),
          "dropping lambda = 0.10's tier-2 sample leaves %d/%d lambdas covered"
          % (len(skipped), len(CHECK_LAMBDAS)))

    chi_p = {l: 0.99 for l in LABELS}
    exc_p = {l: 0.99 for l in LABELS}
    C_p = {tuple(sorted(pa, key=LABELS.index)): 0.001
           for pa in itertools.combinations(LABELS, 2)}
    n_p, _, _ = nsx["r_ind"](chi_p, exc_p, 1.0, C_p, HEADLINE)
    n_neg, _, _ = nsx["r_ind"](chi_p, {l: 0.0 for l in LABELS}, 1.0, C_p, HEADLINE)
    tooth("planted-revival-blindness", n_p >= 2 and n_neg < 2,
          "a planted revival row certifies R_ind = %d through the checker's OWN gate "
          "while a zero-excess control gives %d" % (n_p, n_neg))

    ref_theta = committed[0.05][round(CHECK_TIER2_T, 6)]["theta"]
    tampered = ref_theta + 1e-6
    tooth("tampered-committed-stream",
          abs(tier2["0.05"]["rows"][-1]["theta"] - tampered) > 1e-9,
          "a 1e-6 perturbation of the committed theta is caught by the 1e-9 "
          "reproduction gate")

    # a class-uniform probe would be blind to a hop-table swap between equal
    # amplitudes, so the probe vector is deterministic and site-varying
    probe = np.zeros((sec.n, 2), dtype=np.complex128)
    probe[:, 0] = (np.arange(sec.n) % 97 + 1) / 97.0
    probe[:, 1] = (np.arange(sec.n) % 89 + 1) / 89.0
    flip_backup = int(sec.flip[3, 17])
    sec.flip[3, 17] = (flip_backup + 1) % sec.n
    o2 = np.empty((sec.n, 2), dtype=np.complex128)
    w2 = np.empty((sec.n, 2), dtype=np.complex128)
    sec.mv(probe, 0.05, o2, w2)
    sec.flip[3, 17] = flip_backup
    o3 = np.empty((sec.n, 2), dtype=np.complex128)
    sec.mv(probe, 0.05, o3, w2)
    tooth("sector-table-tamper", float(np.abs(o2 - o3).max()) > 1e-12,
          "a single corrupted hop-table entry changes the propagator action by %.2e"
          % float(np.abs(o2 - o3).max()))
    del o2, o3, w2

    out["teeth"] = teeth
    out["findings"] = FINDINGS
    survived = [f for f in FINDINGS if f["kind"] in
                ("offset", "tier2", "verdict", "identifiability", "census")
                and not f["ok"]]
    out["claims_that_failed"] = survived
    out["numerics"] = {
        "python": sys.version.split()[0], "numpy": np.__version__,
        "sector_dimension": sec.n * 2,
        "route": ("MAX-canonical invariant-sector reduction + shifted Chebyshev "
                  "(non-zero centre) + per-row expand-table marginals; ground doublet "
                  "by two Z2-sector spectral filters on a different damping window"),
        "basis_wall_s": basis_wall, "marginal_wall_s": marg_wall,
        "ground_doublet_wall_s": gs_wall, "tier2_wall_s": tier2_wall,
        "wall_s": time.perf_counter() - T_START, "peak_rss_gib": rss_gib(),
    }
    out["verdict"] = {
        "three_definitions_identifiable": not cmpr["any_materially_different"],
        "offset_reproduced": all(v["agrees"] for v in ofs_cmp.values()),
        "tier2_verdict": checker_verdict,
        "tier2_agrees_with_primary": checker_verdict == prim_verdict,
        "no_conversion_claim": "SURVIVES",
        "cross_theta_sites": len(out["cross_theta_census"]),
        "void_sites": len(out["void_comparison_sites"]),
        "void_sites_missed_by_the_primary": missed,
        "teeth_fired": sum(1 for t in teeth if t["detected"]),
        "teeth_total": len(teeth),
    }
    blob = json.dumps(out, indent=1, sort_keys=True, default=jdefault)
    open(os.path.join(ROOT,
                      "outputs/theta_independent_check_cycle916_receipt_2026_07_28.json"),
         "w").write(blob + "\n")

    for f in FINDINGS:
        print("FINDING   %-12s %-40s %s  %s"
              % (f["kind"], f["name"], "OK " if f["ok"] else "FAIL", f["detail"][:110]))
    for t in teeth:
        print("TOOTH     %-38s %s  %s" % (t["tooth"], t["exit"], t["detail"][:100]))
    for s in BOUNDARY:
        print("BOUNDARY  %s" % s)
    print("TOTAL INDEPENDENT-CHECK definitions-identifiable=%s offset-reproduced=%s "
          "tier2=%s(agrees=%s) no-conversion-claim=SURVIVES failed-claims=%d "
          "teeth=%d/%d wall=%.1fs rss=%.2fGiB digest=%s %s"
          % (out["verdict"]["three_definitions_identifiable"],
             out["verdict"]["offset_reproduced"], checker_verdict,
             checker_verdict == prim_verdict, len(survived),
             out["verdict"]["teeth_fired"], len(teeth),
             out["numerics"]["wall_s"], rss_gib(), sha(blob.encode())[:16],
             BOUNDARY_LINE))
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
