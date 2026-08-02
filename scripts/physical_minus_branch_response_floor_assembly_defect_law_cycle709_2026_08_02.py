#!/usr/bin/env python3
"""Cycle-709 runner -- the minus-branch response floor as the solve image of the
Hessian-assembly equivariance defect.

Paired note:
  docs/PHYSICAL_MINUS_BRANCH_RESPONSE_FLOOR_ASSEMBLY_DEFECT_LAW_CYCLE709_NOTE_2026-08-02.md

Measures, on the cycle-696 compiled chain imported verbatim (never re-implemented):
  C0  frame scope, constant-sign census, dof-transport bijection, solver scope
  C1  upstream transport floors: source vector exact, load vector at summation level
  C2  assembly-stage equivariance defect E: branch dichotomy and size independence
  C3  exact two-term decomposition of the response-stage transport defect
  C4  zero-parameter first-order law: the commutator term is the response image of E
  C5  finite-difference step sweep: roundoff character of E on the all-minus branch
  C6  size scaling: the floor's growth in L is response-side, not assembly-side

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

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
EYE3 = np.eye(3, dtype=np.int64)
U = float(np.finfo(float).eps)
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
    print("L={} n_dof={} null_dim={} lam_min={} |w|max={} u|Q|/lam_min={} |eps0|_2={}".format(
        L, model["dim"], sol["null_dim"], fmt(lam_min), fmt(Qn), fmt(wrong),
        fmt(np.linalg.norm(eps0))))
    ctx[L] = {"null": sol["null_dim"], "n_dof": model["dim"],
              "lam_min": lam_min, "wrong": wrong}

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
        pred = push(eps_of(E @ eps0), m)
        resid = float(np.linalg.norm(term2 - pred) / np.linalg.norm(term2))
        cos = float(term2 @ pred /
                    (np.linalg.norm(term2) * np.linalg.norm(pred)))
        print("L={} {}: dQ={} drho={} db={} deps={} term1={} term2={} closure={}".format(
            L, tag, fmt(dQ), fmt(drho), fmt(db_max), fmt(deps_max), fmt(t1),
            fmt(t2), fmt(closure)))
        print("      law: |term2-pred|/|term2|={} cos(term2,pred)={}".format(
            fmt(resid), fmt(cos)))
        ctx[(L, tag)] = {"bij": bij, "dQ": dQ, "drho": drho, "db": db_max,
                         "deps": deps_max, "t1": t1, "t2": t2,
                         "closure": closure, "resid": resid, "cos": cos}

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
print("scaling: lam_min L3/L7={} floor L7/L3={} dQ L7/L3={}".format(
    fmt(lam_ratio), fmt(floor_ratio), fmt(dQ_ratio)))

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

print("== C3 exact decomposition of the response-stage defect ==")
for L in L_LIST:
    for tag in ("plus", "minus"):
        c = ctx[(L, tag)]
        check("c3.closure.L{}.{}".format(L, tag), c["closure"] <= 1e-13,
              "closure " + fmt(c["closure"]))
        check("c3.term1.L{}.{}".format(L, tag), c["t1"] <= 1e-12,
              "term1 " + fmt(c["t1"]))
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

print("== C5 step sweep: roundoff character of E on the all-minus branch ==")
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

print("== C6 size scaling: floor growth is response-side ==")
check("c6.lam", 30.0 <= lam_ratio <= 60.0, "lam_min softening " + fmt(lam_ratio))
check("c6.floor", 10.0 <= floor_ratio <= 40.0, "minus floor growth " + fmt(floor_ratio))
check("c6.attrib", dQ_ratio <= 1.1 and floor_ratio >= 10.0,
      "defect flat, floor grows: response-side")
for L in L_LIST:
    q = ctx[(L, "minus")]["deps"] / ctx[L]["wrong"]
    check("c6.reject.L{}".format(L), q >= 100.0,
          "floor / spectral-solve scale " + fmt(q))

def branch_receipt(L, tag):
    c = ctx[(L, tag)]
    return {"dQ": fmt(c["dQ"]), "drho": fmt(c["drho"]), "db": fmt(c["db"]),
            "deps": fmt(c["deps"]), "term1": fmt(c["t1"]),
            "term2": fmt(c["t2"]), "closure": fmt(c["closure"]),
            "resid": fmt(c["resid"]), "cos": fmt(c["cos"])}


receipt = {
    "witness": {"plus_g": PLUS_G, "minus_g": MINUS_G,
                "n_plus": N_PLUS, "n_minus": N_MINUS},
    "levels": {
        "L{}".format(L): {
            "n_dof": ctx[L]["n_dof"],
            "lam_min": fmt(ctx[L]["lam_min"]),
            "wrong_model_scale": fmt(ctx[L]["wrong"]),
            "plus": branch_receipt(L, "plus"),
            "minus": branch_receipt(L, "minus"),
        } for L in L_LIST
    },
    "sweep": {"steps": [fmt(s) for s in sweep_steps],
              "E_minus_F": [fmt(v) for v in sweep_minus],
              "E_plus_F": [fmt(v) for v in sweep_plus],
              "scale_const": fmt(scale_const)},
    "scaling": {"lam_ratio": fmt(lam_ratio), "floor_ratio": fmt(floor_ratio),
                "dQ_ratio": fmt(dQ_ratio)},
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
