#!/usr/bin/env python3
"""Cycle-709 runner -- the minus-branch response floor as the solve image of the
Hessian-assembly equivariance defect.

Paired note:
  docs/PHYSICAL_MINUS_BRANCH_RESPONSE_FLOOR_ASSEMBLY_DEFECT_LAW_CYCLE709_NOTE_2026-08-02.md

Measures, on the cycle-696 compiled chain imported verbatim (never re-implemented):
  C0  frame scope, constant-sign census, dof-transport bijection, solver scope
  C1  upstream transport floors: source vector exact, load vector at summation level
  C2  assembly-stage equivariance defect E: branch dichotomy, max-entry size
      independence, and the measured GROWTH of E's global measures with the box
  C3  two-term decomposition of the response-stage transport defect, with live
      wrong-value rejectors for deleting either term
  C4  zero-parameter first-order law: the commutator term is the response image of E
  C5  finite-difference step sweep: the measured step direction of E on the
      all-minus branch over the sampled decade
  C6  size scaling: how much of the floor's growth in L the response carries

Read inventory.  External/ancestral scientific input: the cycle-696 compiler module
and its transitive scripts/ imports, declared in AUDIT_INPUT_PATHS below and loaded
as a library; every physical quantity below is computed through them.  No other
repository file is read, and no sibling cycle's measured value is read or copied in.
Package-local write activity: one paired receipt under outputs/.  This runner
performs no self-hash or receipt-verification integrity read.

All floating quantities print through one format ({:.1e}); the receipt carries the
same strings. Honest-miss rule: every gate band was fixed before this runner ran;
a miss prints FAIL and the total line reports it.
"""
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_c709", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

# The load-bearing repository-source closure: the cycle-696 compiler loaded above
# plus every scripts/ module it imports transitively.  Declared so the runner cache
# pins their bytes and rejects input drift.
AUDIT_INPUT_PATHS = (
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

# Declared audit timeout, in seconds.  Observed runtime is a few seconds at L = 7;
# the margin covers the dense L = 7 solve on a slow audit host.
AUDIT_TIMEOUT_SEC = 600

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
EYE3 = np.eye(3, dtype=np.int64)
# float64 unit roundoff for round-to-nearest: 2^-53.  numpy's finfo(float).eps is
# the spacing from 1 to the next representable double, 2^-52 -- twice this.
U = float(np.finfo(float).eps) / 2.0
L_LIST = (3, 7)
STEP_FACTORS = (0.25, 0.5, 1.0, 2.0, 4.0)
RECEIPT_NAME = ("physical_minus_branch_response_floor_assembly_defect_law_"
                "cycle709_2026_08_02_receipt_2026-08-02.json")

fmt = "{:.1e}".format
PASS = 0
FAIL = 0


def check(tag, cond, detail):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("ok   {} {}".format(tag, detail))
    else:
        FAIL += 1
        print("FAIL {} {}".format(tag, detail))


def cs_sign(R):
    nz = R[R != 0]
    if np.all(nz == 1):
        return 1
    if np.all(nz == -1):
        return -1
    return None


def dof_perm(L, index, R):
    """m[i] = dof index of the image of dof i under the site map s -> R(s-c)+c.

    dof (cls, x) is the undirected edge [x, x + v_cls]; the image edge is
    canonicalized to direction |R v| and low corner g(x) + min(R v, 0)."""
    smap = c696.frame_site_map(L, R)
    dir2class = {tuple(c696.regge.DIRS15[c][:3]): c for c in c696.SPATIAL_CLASSES}
    n = len(index)
    m = np.empty(n, dtype=np.int64)
    for (cls, x), i in index.items():
        v = np.asarray(c696.regge.DIRS15[cls][:3], dtype=np.int64)
        gx = np.asarray(smap[x], dtype=np.int64)
        w = R @ v
        vp = tuple(int(t) for t in np.abs(w))
        xp = tuple(int(t) for t in (gx + np.minimum(w, 0)))
        m[i] = index[(dir2class[vp], xp)]
    return m


def push(vec, m):
    out = np.empty_like(vec)
    out[m] = vec
    return out


# ---------------- measurement pass ----------------
print("== measurements (cycle-696 chain, open box, central-edge label-5 edit) ==")
MINUS_G = next(g for g in range(24) if cs_sign(FRAMES[g]) == -1)
PLUS_G = next(g for g in range(24)
              if cs_sign(FRAMES[g]) == 1 and not np.array_equal(FRAMES[g], EYE3))
N_PLUS = sum(1 for R in FRAMES if cs_sign(R) == 1)
N_MINUS = sum(1 for R in FRAMES if cs_sign(R) == -1)
DETS = [int(round(float(np.linalg.det(R)))) for R in FRAMES]
print("witnesses: plus g={} minus g={} census {}+{} constant-sign of 24".format(
    PLUS_G, MINUS_G, N_PLUS, N_MINUS))

ctx = {}
for L in L_LIST:
    model = c696.assemble_static_hessian(L, wrap=False)
    sol = c696.sector_solve(model)
    A = (L - 1) // 2
    dom0 = c696.build_domain(L, edits={((A, A, A), (A + 1, A, A)): 5})
    sites = model["site_index"]
    rho0 = np.asarray(c696.rho_vector(dom0, sites))
    b0 = rho0 @ model["G"]

    def eps_of(b, model=model, sol=sol):
        return c696.response(model, sol, b)["eps"]

    eps0 = eps_of(b0)
    w = sol["w"]
    reg = sol["regular"]
    lam_min = float(np.abs(w[reg]).min())
    Qn = float(np.abs(w).max())
    wrong = U * Qn / lam_min
    print("L={} n_dof={} null_dim={} lam_min={} |w|max={} |eps0|_2={} "
          "u*kappa_2(Q)={} (relative) heuristic absolute solve scale={}".format(
              L, model["dim"], sol["null_dim"], fmt(lam_min), fmt(Qn),
              fmt(np.linalg.norm(eps0)), fmt(wrong),
              fmt(wrong * float(np.linalg.norm(eps0)))))
    # `wrong` is u * kappa_2(Q): a RELATIVE conditioning indicator, not an absolute
    # forward-error scale. Multiplying by the response magnitude gives an absolute
    # scale up to an unpinned, dimension- and algorithm-dependent stability factor.
    eps0_norm = float(np.linalg.norm(eps0))
    ctx[L] = {"null": sol["null_dim"], "n_dof": model["dim"],
              "lam_min": lam_min, "wrong": wrong, "eps0_norm": eps0_norm,
              "wrong_abs": wrong * eps0_norm}

    for tag, g in (("plus", PLUS_G), ("minus", MINUS_G)):
        R = FRAMES[g]
        m = dof_perm(L, model["index"], R)
        bij = len(set(m.tolist())) == model["dim"]
        E = model["Q"][np.ix_(m, m)] - model["Q"]
        dQ = float(np.abs(E).max())
        domR = c696.apply_frame_to_domain(dom0, R)
        rhoR = np.asarray(c696.rho_vector(domR, sites))
        smap = c696.frame_site_map(L, R)
        rho_push = np.empty_like(rho0)
        for s, i in sites.items():
            rho_push[sites[smap[s]]] = rho0[i]
        drho = float(np.abs(rhoR - rho_push).max())
        bR = rhoR @ model["G"]
        db = bR - push(b0, m)
        db_max = float(np.abs(db).max())
        epsR = eps_of(bR)
        deps = epsR - push(eps0, m)
        deps_max = float(np.abs(deps).max())
        term1 = eps_of(db)
        term2 = eps_of(push(b0, m)) - push(eps0, m)
        t1 = float(np.abs(term1).max())
        t2 = float(np.abs(term2).max())
        closure = float(np.abs(deps - (term1 + term2)).max())
        # Live wrong-value rejectors on the SAME comparison path: what the residual
        # becomes if either term is deleted from the decomposition.  These are what
        # make C3 discriminating -- deleting a term inside `closure` above turns
        # `closure` into one of these and the ratio gates below stop holding.
        drop1 = float(np.abs(deps - term2).max())
        drop2 = float(np.abs(deps - term1).max())
        # Global measures of the assembly defect and of its load-specific forcing.
        # dQ is one max entry; these say how much of E the box actually carries.
        Ee = E @ eps0
        e_fro = float(np.linalg.norm(E))
        e_nnz = int(np.count_nonzero(E))
        ee_2 = float(np.linalg.norm(Ee))
        ee_max = float(np.abs(Ee).max())
        pred = push(eps_of(E @ eps0), m)
        resid = float(np.linalg.norm(term2 - pred) / np.linalg.norm(term2))
        cos = float(term2 @ pred /
                    (np.linalg.norm(term2) * np.linalg.norm(pred)))
        print("L={} {}: dQ={} drho={} db={} deps={} term1={} term2={} closure={}".format(
            L, tag, fmt(dQ), fmt(drho), fmt(db_max), fmt(deps_max), fmt(t1),
            fmt(t2), fmt(closure)))
        print("      law: |term2-pred|/|term2|={} cos(term2,pred)={}".format(
            fmt(resid), fmt(cos)))
        print("      decomposition rejectors: closure={} drop-term1={} drop-term2={}"
              " | E: |E|_F={} nnz={} |E eps0|_2={} |E eps0|_max={}".format(
                  fmt(closure), fmt(drop1), fmt(drop2), fmt(e_fro), e_nnz,
                  fmt(ee_2), fmt(ee_max)))
        ctx[(L, tag)] = {"bij": bij, "dQ": dQ, "drho": drho, "db": db_max,
                         "deps": deps_max, "t1": t1, "t2": t2,
                         "closure": closure, "resid": resid, "cos": cos,
                         "drop1": drop1, "drop2": drop2, "e_fro": e_fro,
                         "e_nnz": e_nnz, "ee_2": ee_2, "ee_max": ee_max}

# step sweep at L=3, both branches
sweep_steps = []
sweep_minus = []
sweep_plus = []
for f in STEP_FACTORS:
    step = c696.FD_H * f
    model_s = c696.assemble_static_hessian(3, wrap=False, step=step)
    m_minus = dof_perm(3, model_s["index"], FRAMES[MINUS_G])
    m_plus = dof_perm(3, model_s["index"], FRAMES[PLUS_G])
    Em = model_s["Q"][np.ix_(m_minus, m_minus)] - model_s["Q"]
    Ep = model_s["Q"][np.ix_(m_plus, m_plus)] - model_s["Q"]
    Fm = float(np.linalg.norm(Em))
    Fp = float(np.linalg.norm(Ep))
    sweep_steps.append(step)
    sweep_minus.append(Fm)
    sweep_plus.append(Fp)
    print("sweep L=3 step={} |E_minus|_F={} |E_plus|_F={}".format(
        fmt(step), fmt(Fm), fmt(Fp)))
scale_const = ctx[(3, "minus")]["dQ"] * 2.0 * c696.FD_H / U
print("scale check: dQ_minus * 2*step / u = {} (problem gradient scale, |w|max decade)".format(
    fmt(scale_const)))
lam_ratio = ctx[3]["lam_min"] / ctx[7]["lam_min"]
floor_ratio = ctx[(7, "minus")]["deps"] / ctx[(3, "minus")]["deps"]
dQ_ratio = ctx[(7, "minus")]["dQ"] / ctx[(3, "minus")]["dQ"]
efro_ratio = ctx[(7, "minus")]["e_fro"] / ctx[(3, "minus")]["e_fro"]
ennz_ratio = ctx[(7, "minus")]["e_nnz"] / ctx[(3, "minus")]["e_nnz"]
ee2_ratio = ctx[(7, "minus")]["ee_2"] / ctx[(3, "minus")]["ee_2"]
eemax_ratio = ctx[(7, "minus")]["ee_max"] / ctx[(3, "minus")]["ee_max"]
print("scaling: lam_min L3/L7={} floor L7/L3={} dQ L7/L3={}".format(
    fmt(lam_ratio), fmt(floor_ratio), fmt(dQ_ratio)))
print("scaling (global E, minus): |E|_F L7/L3={} nnz L7/L3={} |E eps0|_2 L7/L3={}"
      " |E eps0|_max L7/L3={}".format(
          fmt(efro_ratio), fmt(ennz_ratio), fmt(ee2_ratio), fmt(eemax_ratio)))

# ---------------- gates ----------------
print("== C0 frame scope, witnesses, solver scope ==")
check("c0.det", all(d == 1 for d in DETS), "24 frames, det=+1 for all")
check("c0.census_plus", N_PLUS == 3, "all-plus constant-sign count {}".format(N_PLUS))
check("c0.census_minus", N_MINUS == 3, "all-minus constant-sign count {}".format(N_MINUS))
for L in L_LIST:
    for tag in ("plus", "minus"):
        check("c0.bij.L{}.{}".format(L, tag), ctx[(L, tag)]["bij"],
              "dof transport bijective")
    check("c0.null.L{}".format(L), ctx[L]["null"] == 0,
          "null_dim={}".format(ctx[L]["null"]))

print("== C1 upstream transport: source exact, load at summation level ==")
for L in L_LIST:
    for tag in ("plus", "minus"):
        c = ctx[(L, tag)]
        check("c1.rho.L{}.{}".format(L, tag), c["drho"] <= 0.0,
              "drho " + fmt(c["drho"]))
        check("c1.b.L{}.{}".format(L, tag), c["db"] <= 1e-13,
              "db " + fmt(c["db"]))

print("== C2 assembly defect: branch dichotomy, size independence ==")
for L in L_LIST:
    check("c2.plus.L{}".format(L), ctx[(L, "plus")]["dQ"] <= 1e-13,
          "dQ_plus " + fmt(ctx[(L, "plus")]["dQ"]))
    check("c2.minus.L{}".format(L),
          1e-11 <= ctx[(L, "minus")]["dQ"] <= 1e-9,
          "dQ_minus " + fmt(ctx[(L, "minus")]["dQ"]))
    check("c2.sep.L{}".format(L),
          ctx[(L, "minus")]["dQ"] >= 1e3 * ctx[(L, "plus")]["dQ"],
          "branch separation " + fmt(ctx[(L, "minus")]["dQ"] / ctx[(L, "plus")]["dQ"]))
check("c2.size", 0.9 <= dQ_ratio <= 1.1, "dQ_minus L7/L3 " + fmt(dQ_ratio))
# The max entry is size independent; the global measures are NOT. Gated as a
# positive measured fact so no surface can read "the defect is size-independent"
# as a statement about the assembled operator rather than about one entry.
check("c2.global_fro", efro_ratio >= 2.0,
      "|E|_F grows with the box, L7/L3 " + fmt(efro_ratio))
check("c2.global_nnz", ennz_ratio >= 2.0,
      "nnz(E) grows with the box, L7/L3 " + fmt(ennz_ratio))
check("c2.global_forcing", ee2_ratio >= 2.0,
      "|E eps0|_2 grows with the box, L7/L3 " + fmt(ee2_ratio))

print("== C3 two-term decomposition with live wrong-value rejectors ==")
for L in L_LIST:
    for tag in ("plus", "minus"):
        c = ctx[(L, tag)]
        check("c3.closure.L{}.{}".format(L, tag), c["closure"] <= 1e-13,
              "closure " + fmt(c["closure"]))
        check("c3.term1.L{}.{}".format(L, tag), c["t1"] <= 1e-12,
              "term1 " + fmt(c["t1"]))
        # Deleting term2 must be rejected by the same live comparison, in every cell.
        check("c3.reject_t2.L{}.{}".format(L, tag),
              c["drop2"] >= 10.0 * c["closure"],
              "drop-term2 residual / closure " + fmt(c["drop2"] / c["closure"]))
for L in L_LIST:
    # Deleting term1 is rejected only where term1 is resolvable above the solve's
    # own linearity residual -- that is the minus branch. Both gates below fail if
    # term1 is dropped from the closure computation, because `closure` then equals
    # `drop1` and neither ratio can hold.
    c = ctx[(L, "minus")]
    check("c3.reject_t1.L{}.minus".format(L), c["drop1"] >= 4.0 * c["closure"],
          "drop-term1 residual / closure " + fmt(c["drop1"] / c["closure"]))
    check("c3.resolved_t1.L{}.minus".format(L), c["closure"] <= 0.5 * c["t1"],
          "closure / term1 " + fmt(c["closure"] / c["t1"]))
for L in L_LIST:
    # Honest converse on the plus branch: term1 there sits at the closure residual,
    # so the split is NOT resolvable and no discrimination is claimed for it.
    c = ctx[(L, "plus")]
    check("c3.unresolved_t1.L{}.plus".format(L), c["drop1"] <= 10.0 * c["closure"],
          "plus-branch term1 at closure noise, ratio " + fmt(c["drop1"] / c["closure"]))
for L in L_LIST:
    c = ctx[(L, "minus")]
    check("c3.dom.L{}".format(L), c["t1"] <= 1e-2 * c["t2"],
          "term1/term2 " + fmt(c["t1"] / c["t2"]))
check("c3.floor.L3", 4e-11 <= ctx[(3, "minus")]["deps"] <= 1.2e-10,
      "minus deps " + fmt(ctx[(3, "minus")]["deps"]))
check("c3.floor.L7", 8e-10 <= ctx[(7, "minus")]["deps"] <= 3e-9,
      "minus deps " + fmt(ctx[(7, "minus")]["deps"]))
for L in L_LIST:
    check("c3.plusfloor.L{}".format(L), ctx[(L, "plus")]["deps"] <= 1e-11,
          "plus deps " + fmt(ctx[(L, "plus")]["deps"]))

print("== C4 first-order law: term2 = push(response(E @ eps0)) ==")
for L in L_LIST:
    c = ctx[(L, "minus")]
    check("c4.resid.L{}".format(L), c["resid"] <= 1e-2,
          "minus rel residual " + fmt(c["resid"]))
    check("c4.cos.L{}".format(L), 1.0 - c["cos"] <= 1e-2,
          "minus cos " + fmt(c["cos"]))
for L in L_LIST:
    check("c4.reject.L{}".format(L), ctx[(L, "plus")]["resid"] >= 0.3,
          "plus-branch rejector residual " + fmt(ctx[(L, "plus")]["resid"]))

print("== C5 step sweep: measured step direction of E over the sampled decade ==")
for i in range(4):
    check("c5.mono.{}".format(i + 1), sweep_minus[i] > sweep_minus[i + 1],
          "|E|_F {} > {}".format(fmt(sweep_minus[i]), fmt(sweep_minus[i + 1])))
sweep_ratio = sweep_minus[0] / sweep_minus[-1]
check("c5.ratio", 4.0 <= sweep_ratio <= 1e4,
      "F(smallest)/F(largest) " + fmt(sweep_ratio))
for i, f in enumerate(STEP_FACTORS):
    check("c5.plus.{}".format(i + 1), sweep_plus[i] <= 2e-13,
          "|E_plus|_F " + fmt(sweep_plus[i]) + " at step " + fmt(sweep_steps[i]))
check("c5.scale", 20.0 <= scale_const <= 500.0,
      "dQ*2s/u " + fmt(scale_const))

print("== C6 size scaling: how much of the floor growth the response carries ==")
check("c6.lam", 30.0 <= lam_ratio <= 60.0, "lam_min softening " + fmt(lam_ratio))
check("c6.floor", 10.0 <= floor_ratio <= 40.0, "minus floor growth " + fmt(floor_ratio))
check("c6.attrib", dQ_ratio <= 1.1 and floor_ratio >= 10.0,
      "max local entry flat while the floor grows; the response is a substantial "
      "contributor, and the forcing |E eps0|_2 grows by " + fmt(ee2_ratio)
      + " so the growth is NOT assigned to the response alone")
for L in L_LIST:
    # HEURISTIC scale comparison, not an exclusion: no dimension- or
    # algorithm-dependent stability factor is pinned, so this says the floor sits
    # above the naive absolute solve-noise scale, nothing more.
    q = ctx[(L, "minus")]["deps"] / ctx[L]["wrong_abs"]
    check("c6.scale_cmp.L{}".format(L), q >= 1.0,
          "heuristic: floor / (u kappa_2(Q) |eps0|_2) " + fmt(q)
          + " (no stability factor pinned; not an exclusion)")

def branch_receipt(L, tag):
    c = ctx[(L, tag)]
    return {"dQ": fmt(c["dQ"]), "drho": fmt(c["drho"]), "db": fmt(c["db"]),
            "deps": fmt(c["deps"]), "term1": fmt(c["t1"]),
            "term2": fmt(c["t2"]), "closure": fmt(c["closure"]),
            "closure_drop_term1": fmt(c["drop1"]),
            "closure_drop_term2": fmt(c["drop2"]),
            "E_frobenius": fmt(c["e_fro"]), "E_nonzeros": c["e_nnz"],
            "E_eps0_2norm": fmt(c["ee_2"]), "E_eps0_max": fmt(c["ee_max"]),
            "resid": fmt(c["resid"]), "cos": fmt(c["cos"])}


receipt = {
    "witness": {"plus_g": PLUS_G, "minus_g": MINUS_G,
                "n_plus": N_PLUS, "n_minus": N_MINUS},
    "levels": {
        "L{}".format(L): {
            "n_dof": ctx[L]["n_dof"],
            "lam_min": fmt(ctx[L]["lam_min"]),
            "eps0_2norm": fmt(ctx[L]["eps0_norm"]),
            "relative_conditioning_u_kappa2": fmt(ctx[L]["wrong"]),
            "heuristic_absolute_solve_scale": fmt(ctx[L]["wrong_abs"]),
            "plus": branch_receipt(L, "plus"),
            "minus": branch_receipt(L, "minus"),
        } for L in L_LIST
    },
    "sweep": {"steps": [fmt(s) for s in sweep_steps],
              "E_minus_F": [fmt(v) for v in sweep_minus],
              "E_plus_F": [fmt(v) for v in sweep_plus],
              "scale_const": fmt(scale_const)},
    "scaling": {"lam_ratio": fmt(lam_ratio), "floor_ratio": fmt(floor_ratio),
                "dQ_ratio": fmt(dQ_ratio), "E_frobenius_ratio": fmt(efro_ratio),
                "E_nonzeros_ratio": fmt(ennz_ratio),
                "E_eps0_2norm_ratio": fmt(ee2_ratio),
                "E_eps0_max_ratio": fmt(eemax_ratio)},
    "total": {"PASS": PASS, "FAIL": FAIL},
}
outdir = HERE.parent / "outputs"
outdir.mkdir(exist_ok=True)
with open(outdir / RECEIPT_NAME, "w") as fh:
    json.dump(receipt, fh, indent=2, sort_keys=True)
    fh.write("\n")
print("RECEIPT: outputs/" + RECEIPT_NAME)
print("TOTAL: PASS={} FAIL={}".format(PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
