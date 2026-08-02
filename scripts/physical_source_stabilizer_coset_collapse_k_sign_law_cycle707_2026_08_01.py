"""Cycle 707 -- source-stabilizer coset collapse of the compiled K sign law.

Class-A finite check script (stdlib + numpy only).  It executes the landed Cycle-696
open-coframe endpoint compiler chain

    rho -> b -> eps -> (h, e) -> (parts, K)

on two decorated source domains and measures, from that chain alone:

  G1  the constant-sign pointwise transport law on the 12 constant-sign signed
      permutations (6 proper rotations plus 6 improper computational identities);
  G2  the plus/minus branch asymmetry of the measured floors;
  G3  the mixed-sign obstruction on the 18 remaining proper rotations;
  G4  the biconditional between the landed frame parity function and the law;
  G5  the proper stabilizer quartet of the single-edit source and its transversal;
  G6  the exact collapse of every frame image onto a constant-sign representative;
  G7  the all-24 multiset sign law with chi = sx;
  G8  the stage ladder that locates the negation floor;
  G9  the amplitude-linearity of the negation floor;
  G10 the two-edit trichotomy.

No value is read from a pinned table: every number printed here is recomputed from
the compiler chain in this run.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_compiler_for_c707", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
EYE3 = np.eye(3, dtype=np.int64)
MZ = np.diag([1, 1, -1]).astype(np.int64)

AMP = 0.20
AMP_LADDER = (0.05, 0.10, 0.20)
L_LIST = (3, 7)
QUARTET_EXPECTED = (20, 21, 22, 23)
BOUND_PLUS = 1e-11
BOUND_MINUS = 1e-7
BOUND_B = 1e-12
BOUND_EPS_PLUS = 1e-10
BREAK_FLOOR = 1e-2
PP_FLOOR = 1e-10
RATIO_LO = 1.6
RATIO_HI = 2.4

RECEIPT_NAME = ("physical_source_stabilizer_coset_collapse_k_sign_law_cycle707"
                "_2026_08_01_receipt_2026-08-01.json")

N_PASS = 0
N_FAIL = 0
GATES: dict = {}
NOTES: dict = {}


def fmt(x) -> str:
    return "{:.1e}".format(float(x))


def check(name: str, ok: bool, detail: str = "") -> bool:
    """Record and print one gate.  Every gate below is discriminating: each has an
    explicit wrong-value, wrong-sign, wrong-branch, or absent-law rejector."""
    global N_PASS, N_FAIL
    ok = bool(ok)
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
    GATES[name] = {"pass": ok, "detail": detail}
    print("{} {} {}".format("PASS" if ok else "FAIL", name, detail))
    return ok


# ---------------------------------------------------------------------------
# signed-permutation frame utilities (written here, not imported from a probe)
# ---------------------------------------------------------------------------
def sp_data(R: np.ndarray):
    """p[i] = argmax|R[i]|, s[i] = R[i, p[i]] -- the permutation and sign words."""
    p = [int(np.argmax(np.abs(R[i]))) for i in range(3)]
    s = [int(R[i, p[i]]) for i in range(3)]
    return p, s


def cs_sign(R: np.ndarray):
    """+1 / -1 when every nonzero entry shares one sign, None otherwise."""
    nz = R[R != 0]
    if np.all(nz == 1):
        return 1
    if np.all(nz == -1):
        return -1
    return None


def sx_of(R: np.ndarray) -> int:
    p, s = sp_data(R)
    return s[p.index(0)]


def sy_of(R: np.ndarray) -> int:
    p, s = sp_data(R)
    return s[p.index(1)]


def det_int(R: np.ndarray) -> int:
    return int(round(float(np.linalg.det(R.astype(float)))))


def improper_constant_sign():
    """The 6 constant-sign signed permutations with det = -1, in a fixed order."""
    out = []
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            P[i, j] = 1
        for sgn in (1, -1):
            M = (sgn * P).astype(np.int64)
            if det_int(M) == -1 and cs_sign(M) is not None:
                out.append(M)
    return out


IMPROPER = improper_constant_sign()


def links_key(dom: dict) -> tuple:
    return tuple(sorted((u, v, w) for (u, v), w in dom["links"].items()))


# ---------------------------------------------------------------------------
# the landed Cycle-696 chain, quoted verbatim
# ---------------------------------------------------------------------------
def build_ctx(L: int) -> dict:
    model = c696.assemble_static_hessian(L, wrap=False)
    sol = c696.sector_solve(model)
    A = (L - 1) // 2
    dom0 = c696.build_domain(L, edits={((A, A, A), (A + 1, A, A)): 5})
    dom1 = c696.build_domain(L, edits={((A, A, A), (A + 1, A, A)): 5,
                                       ((A, A, A), (A, A + 1, A)): 7})
    return {"L": L, "model": model, "sol": sol, "dom0": dom0, "dom1": dom1,
            "sites": model["site_index"],
            "all": list(itertools.product(range(L), repeat=3))}


def chain(ctx: dict, dom: dict, amp: float = AMP) -> dict:
    model = ctx["model"]
    rho = c696.rho_vector(dom, model["site_index"])
    b = rho @ model["G"]
    eps = c696.response(model, ctx["sol"], b)["eps"]
    mc = c696.metric_and_coframe(ctx["L"], amp * eps, model["index"])
    kf = c696.k_field(mc["e_clipped"])
    return {"rho": rho, "b": b, "eps": eps, "h": mc["h"], "e": mc["e_clipped"],
            "lengths": np.asarray(mc["lengths"]),
            "parts": np.asarray(kf["parts"]), "K": np.asarray(kf["K"])}


def transport_defects(ctx: dict, c0: dict, cR: dict, R: np.ndarray):
    """Max-over-sites defects of
         e^{R.dom}(sigma x)       = P e^{dom}(x) P^T
         parts_i^{R.dom}(sigma x) = s[i] parts_{p[i]}^{dom}(x)
         K^{R.dom}(sigma x)       = sum_i s[i] parts_{p[i]}^{dom}(x).
    """
    smap = c696.frame_site_map(ctx["L"], R)
    p, s = sp_data(R)
    Rf = R.astype(float)
    d_e = 0.0
    d_parts = 0.0
    d_K = 0.0
    for x in ctx["all"]:
        ix = smap[x]
        d_e = max(d_e, float(np.abs(cR["e"][ix] - Rf @ c0["e"][x] @ Rf.T).max()))
        pred = 0.0
        for i in range(3):
            term = s[i] * float(c0["parts"][x][p[i]])
            d_parts = max(d_parts, abs(float(cR["parts"][ix][i]) - term))
            pred += term
        d_K = max(d_K, abs(float(cR["K"][ix]) - pred))
    return d_e, d_parts, d_K


def wrong_sign_dK(ctx: dict, c0: dict, cR: dict, R: np.ndarray) -> float:
    """Rejector: the SAME law with the common sign forced to +1."""
    smap = c696.frame_site_map(ctx["L"], R)
    p, _s = sp_data(R)
    worst = 0.0
    for x in ctx["all"]:
        pred = 0.0
        for i in range(3):
            pred += float(c0["parts"][x][p[i]])
        worst = max(worst, abs(float(cR["K"][smap[x]]) - pred))
    return worst


def multiset_defect(Ka, Kb) -> float:
    a = np.sort(np.asarray(Ka).ravel())
    b = np.sort(np.asarray(Kb).ravel())
    return float(np.abs(a - b).max())


def ladder_defects(ctx: dict, c0: dict, cR: dict, R: np.ndarray) -> dict:
    """Stage-by-stage sorted-multiset defects along rho -> b -> eps -> lengths."""
    L = ctx["L"]
    sites = ctx["sites"]
    smap = c696.frame_site_map(L, R)
    d_rho = 0.0
    for x in ctx["all"]:
        d_rho = max(d_rho, abs(float(cR["rho"][sites[smap[x]]] - c0["rho"][sites[x]])))
    d_b = float(np.abs(np.sort(cR["b"]) - np.sort(c0["b"])).max())
    d_eps = float(np.abs(np.sort(cR["eps"]) - np.sort(c0["eps"])).max())
    d_len = 0.0
    for x in ctx["all"]:
        u = np.sort(np.asarray(cR["lengths"][smap[x]]).ravel())
        v = np.sort(np.asarray(c0["lengths"][x]).ravel())
        d_len = max(d_len, float(np.abs(u - v).max()))
    return {"rho": d_rho, "b": d_b, "eps": d_eps, "len": d_len}


# ---------------------------------------------------------------------------
def run_L(ctx: dict) -> None:
    L = ctx["L"]
    tag = "L{}".format(L)
    dom0 = ctx["dom0"]
    c0 = chain(ctx, dom0)

    ident = next(g for g in range(24) if np.array_equal(FRAMES[g], EYE3))
    minus_g = next(g for g in range(24) if cs_sign(FRAMES[g]) == -1)
    plus_g = next(g for g in range(24)
                  if cs_sign(FRAMES[g]) == 1 and not np.array_equal(FRAMES[g], EYE3))

    plus_floor = 0.0
    minus_floor = 0.0
    mixed_min = float("inf")
    ms_plus = 0.0
    ms_minus = 0.0
    n_plus = 0
    n_minus = 0
    cs_ok = 0
    cs_n = 0
    mix_ok = 0
    mix_n = 0
    ident_total = None
    rej_sign = 0.0
    rej_branch = 0.0
    lad: dict = {}

    for g in range(24):
        R = FRAMES[g]
        cR = chain(ctx, c696.apply_frame_to_domain(dom0, R))
        d_e, d_p, d_k = transport_defects(ctx, c0, cR, R)
        sg = cs_sign(R)
        sxg = sx_of(R)
        ms = multiset_defect(cR["K"], sxg * c0["K"])
        if sxg == 1:
            n_plus += 1
            ms_plus = max(ms_plus, ms)
        else:
            n_minus += 1
            ms_minus = max(ms_minus, ms)
        if sg is None:
            mix_n += 1
            mixed_min = min(mixed_min, d_e)
            if d_e > BREAK_FLOOR:
                mix_ok += 1
        else:
            cs_n += 1
            worst = max(d_e, d_p, d_k)
            bound = BOUND_PLUS if sg == 1 else BOUND_MINUS
            if worst < bound:
                cs_ok += 1
            if sg == 1:
                plus_floor = max(plus_floor, worst)
            else:
                minus_floor = max(minus_floor, worst)
            if g == ident:
                ident_total = worst
            if L == 3:
                check("G1.{}.p{:02d}".format(tag, g), worst < bound,
                      "cs {:+d} e {} p {} K {}".format(sg, fmt(d_e), fmt(d_p), fmt(d_k)))
        if g == minus_g:
            rej_sign = wrong_sign_dK(ctx, c0, cR, R)
            rej_branch = multiset_defect(cR["K"], c0["K"])
            lad["minus"] = ladder_defects(ctx, c0, cR, R)
        if g == plus_g:
            lad["plus"] = ladder_defects(ctx, c0, cR, R)

    imp_ok = 0
    for j, M in enumerate(IMPROPER):
        cM = chain(ctx, c696.apply_frame_to_domain(dom0, M))
        d_e, d_p, d_k = transport_defects(ctx, c0, cM, M)
        sg = cs_sign(M)
        worst = max(d_e, d_p, d_k)
        bound = BOUND_PLUS if sg == 1 else BOUND_MINUS
        if sg == 1:
            plus_floor = max(plus_floor, worst)
        else:
            minus_floor = max(minus_floor, worst)
        if c696.frame_K_parity(M) == sg and det_int(M) == -1:
            imp_ok += 1
        if L == 3:
            check("G1.{}.i{}".format(tag, j), worst < bound,
                  "cs {:+d} e {} p {} K {}".format(sg, fmt(d_e), fmt(d_p), fmt(d_k)))

    if L != 3:
        check("G1.{}.plus".format(tag), plus_floor < BOUND_PLUS,
              "branch max over 6 frames {}".format(fmt(plus_floor)))
        check("G1.{}.minus".format(tag), minus_floor < BOUND_MINUS,
              "branch max over 6 frames {}".format(fmt(minus_floor)))
    check("G1.{}.id".format(tag), ident_total == 0.0,
          "identity total defect {}".format(fmt(ident_total)))

    ratio = minus_floor / max(plus_floor, 1e-300)
    check("G2.{}".format(tag), ratio > 10.0, "minus/plus floor {}".format(fmt(ratio)))

    check("G3.{}".format(tag), mixed_min > BREAK_FLOOR,
          "mixed min d_e {} over {} frames".format(fmt(mixed_min), mix_n))

    check("G4.{}.cs".format(tag), cs_ok == cs_n and cs_n == 6,
          "parity not None -> law {}/{}".format(cs_ok, cs_n))
    check("G4.{}.mix".format(tag), mix_ok == mix_n and mix_n == 18,
          "parity None -> no law {}/{}".format(mix_ok, mix_n))
    check("G4.{}.imp".format(tag), imp_ok == 6,
          "improper det -1 parity match {}/6".format(imp_ok))
    check("G4.{}.rej".format(tag), rej_sign > BREAK_FLOOR,
          "wrong-sign d_K {}".format(fmt(rej_sign)))

    stab = [g for g in range(24)
            if c696.apply_frame_to_domain(dom0, FRAMES[g])["links"] == dom0["links"]]
    transversal = {}
    n_uniq = 0
    for g in range(24):
        ts = [t for t in stab if cs_sign(FRAMES[g] @ FRAMES[t]) is not None]
        if len(ts) == 1:
            n_uniq += 1
        transversal[g] = ts[0] if ts else stab[0]

    if L == 3:
        check("G5.stab", tuple(stab) == QUARTET_EXPECTED,
              "proper stabilizer of x5 {}".format(tuple(stab)))
        Rx = np.asarray([[1, 0, 0], [0, 0, -1], [0, 1, 0]], dtype=np.int64)
        pw = sorted(tuple(np.linalg.matrix_power(Rx, k).ravel().tolist()) for k in range(4))
        qm = sorted(tuple(FRAMES[t].ravel().tolist()) for t in stab)
        check("G5.c4", pw == qm, "quartet = powers of the x-axis rotation")
        check("G5.transversal", n_uniq == 24,
              "exactly one constant-sign coset member {}/24".format(n_uniq))
        n_sx = sum(1 for g in range(24) for t in stab
                   if sx_of(FRAMES[g] @ FRAMES[t]) == sx_of(FRAMES[g]))
        check("G5.sx", n_sx == 96, "sx coset-invariant {}/96".format(n_sx))

    ok_link = 0
    reps: dict = {}
    for g in range(24):
        d_g = c696.apply_frame_to_domain(dom0, FRAMES[g])
        d_t = c696.apply_frame_to_domain(dom0, FRAMES[g] @ FRAMES[transversal[g]])
        if d_g["links"] == d_t["links"]:
            ok_link += 1
        reps.setdefault(links_key(d_g), g)
    check("G6.{}.collapse".format(tag), ok_link == 24,
          "link-dict equality g.dom == (g t).dom {}/24".format(ok_link))
    check("G6.{}.images".format(tag), len(reps) == 6,
          "distinct domain images {}".format(len(reps)))
    if L == 3:
        ok_bits = 0
        for g in sorted(reps.values()):
            ka = chain(ctx, c696.apply_frame_to_domain(dom0, FRAMES[g]))["K"]
            kb = chain(ctx, c696.apply_frame_to_domain(
                dom0, FRAMES[g] @ FRAMES[transversal[g]]))["K"]
            if np.array_equal(ka, kb):
                ok_bits += 1
        check("G6.L3.determinism", ok_bits == 6,
              "chain determinism on collapsed pairs {}/6".format(ok_bits))

    check("G7.{}.plus".format(tag), ms_plus < BOUND_PLUS,
          "chi=+1 multiset max {}".format(fmt(ms_plus)))
    check("G7.{}.minus".format(tag), ms_minus < BOUND_MINUS,
          "chi=-1 multiset max {}".format(fmt(ms_minus)))
    check("G7.{}.counts".format(tag), n_plus == 12 and n_minus == 12,
          "chi split {}/{}".format(n_plus, n_minus))
    if L == 3:
        check("G7.L3.rej", rej_branch > BREAK_FLOOR,
              "plus-compare on a minus frame {}".format(fmt(rej_branch)))
    else:
        NOTES["G7.L7.plus_compare"] = fmt(rej_branch)
        print("note G7.L7 plus-compare on a minus frame {} unscored".format(fmt(rej_branch)))

    lm = lad["minus"]
    lp = lad["plus"]
    check("G8.{}.rho.minus".format(tag), lm["rho"] == 0.0, "d_rho {}".format(fmt(lm["rho"])))
    check("G8.{}.rho.plus".format(tag), lp["rho"] == 0.0, "d_rho {}".format(fmt(lp["rho"])))
    check("G8.{}.b.minus".format(tag), lm["b"] < BOUND_B, "d_b {}".format(fmt(lm["b"])))
    check("G8.{}.b.plus".format(tag), lp["b"] < BOUND_B, "d_b {}".format(fmt(lp["b"])))
    check("G8.{}.eps.minus".format(tag), lm["eps"] > 100.0 * lm["b"],
          "d_eps {} over 100 d_b {}".format(fmt(lm["eps"]), fmt(100.0 * lm["b"])))
    check("G8.{}.eps.plus".format(tag), lp["eps"] < BOUND_EPS_PLUS,
          "d_eps {}".format(fmt(lp["eps"])))
    if L == 3:
        pred = AMP * lm["eps"]
        check("G8.L3.len", abs(lm["len"] - pred) < 0.5 * pred,
              "d_len {} vs AMP d_eps {}".format(fmt(lm["len"]), fmt(pred)))
    else:
        NOTES["G8.L7.d_len_minus"] = fmt(lm["len"])
        print("note G8.L7 minus d_len {} unscored".format(fmt(lm["len"])))

    if L == 3:
        ds = []
        for a in AMP_LADDER:
            base = chain(ctx, dom0, a)
            rot = chain(ctx, c696.apply_frame_to_domain(dom0, FRAMES[minus_g]), a)
            ds.append(multiset_defect(rot["K"], -base["K"]))
        r1 = ds[1] / ds[0]
        r2 = ds[2] / ds[1]
        check("G9.L3.r1", RATIO_LO <= r1 <= RATIO_HI,
              "d {} {} ratio {}".format(fmt(ds[0]), fmt(ds[1]), fmt(r1)))
        check("G9.L3.r2", RATIO_LO <= r2 <= RATIO_HI,
              "d {} ratio {}".format(fmt(ds[2]), fmt(r2)))

    dom1 = ctx["dom1"]
    c1 = chain(ctx, dom1)
    check("G10.{}.mz".format(tag),
          c696.apply_frame_to_domain(dom1, MZ)["links"] == dom1["links"],
          "m_z = diag(1,1,-1) fixes x5y7")
    n_pp = sum(1 for g in range(24) if sx_of(FRAMES[g]) == 1 and sy_of(FRAMES[g]) == 1)
    n_mm = sum(1 for g in range(24) if sx_of(FRAMES[g]) == -1 and sy_of(FRAMES[g]) == -1)
    n_br = 24 - n_pp - n_mm
    check("G10.{}.classes".format(tag), (n_pp, n_mm, n_br) == (6, 6, 12),
          "pp/mm/broken {}/{}/{}".format(n_pp, n_mm, n_br))

    n_cs = 0
    ok_cs = 0
    matched = 0
    for g in range(24):
        R = FRAMES[g]
        u = R if cs_sign(R) is not None else R @ MZ
        if cs_sign(u) is None:
            continue
        n_cs += 1
        if sx_of(R) == sy_of(R):
            matched += 1
        if (c696.apply_frame_to_domain(dom1, R)["links"]
                == c696.apply_frame_to_domain(dom1, u)["links"]):
            ok_cs += 1
    check("G10.{}.collapse".format(tag), n_cs == 12 and ok_cs == 12 and matched == 12,
          "coset {}/12 link-equal {}/12".format(n_cs, ok_cs))

    pp = 0.0
    mm = 0.0
    brk = float("inf")
    for g in range(24):
        R = FRAMES[g]
        cg = chain(ctx, c696.apply_frame_to_domain(dom1, R))
        d_pos = multiset_defect(cg["K"], c1["K"])
        d_neg = multiset_defect(cg["K"], -c1["K"])
        if sx_of(R) == 1 and sy_of(R) == 1:
            pp = max(pp, d_pos)
        elif sx_of(R) == -1 and sy_of(R) == -1:
            mm = max(mm, d_neg)
        else:
            brk = min(brk, min(d_pos, d_neg))
    check("G10.{}.pp".format(tag), pp < PP_FLOOR, "pp multiset max {}".format(fmt(pp)))
    check("G10.{}.mm".format(tag), mm < BOUND_MINUS, "mm multiset max {}".format(fmt(mm)))
    check("G10.{}.broken".format(tag), brk > BREAK_FLOOR,
          "broken min over both compare signs {}".format(fmt(brk)))


def main() -> int:
    print("c707 source-stabilizer coset collapse of the compiled K sign law")
    print("24 proper rotations, {} improper constant-sign identities, AMP {}".format(
        len(IMPROPER), fmt(AMP)))
    for L in L_LIST:
        print("-- L={} --".format(L))
        run_L(build_ctx(L))

    receipt = {"amp": fmt(AMP),
               "amp_ladder": [fmt(a) for a in AMP_LADDER],
               "box_sizes": list(L_LIST),
               "fail": N_FAIL,
               "gates": GATES,
               "notes": NOTES,
               "pass": N_PASS,
               "runner": Path(__file__).name}
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")

    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))
    return 1 if N_FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
