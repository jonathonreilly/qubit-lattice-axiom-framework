# ru55_2 driver (criteria: checks/ru55_2_criteria.md, written first). Uses the checker functions of checks/dag55_2_dag.py
# and the data of checks/dag55_2_graph.py read-only; variants from checks/ru55_2_variants.py. Run: python3 -I -B ru55_2_dag.py
import os, sys, importlib.util, copy, io, contextlib
from collections import deque, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


dag = load("dag55_2_dag", "dag55_2_dag.py")
var = load("ru55_2_variants", "ru55_2_variants.py")


def sccs(nodes, edges, strict):
    excl = frozenset(dag.STRICT_EXCLUDE) if strict else frozenset()
    adj = dag.adjacency(nodes, edges, exclude=excl)
    return sorted([sorted(c) for c in dag.nontrivial(dag.tarjan(adj), adj)], key=lambda c: (len(c), c))


def desc(nodes, edges, src):
    adj = dag.adjacency(nodes, edges)
    seen, dq = set(), deque([src])
    while dq:
        v = dq.popleft()
        for (w, _) in adj[v]:
            if w not in seen:
                seen.add(w)
                dq.append(w)
    return seen


def analyse(tag, nodes, edges):
    r = {}
    r["schema"] = dag.schema(nodes, edges)
    r["misses"] = dag.string_audit(nodes, edges)
    r["strict"] = sccs(nodes, edges, True)
    r["all"] = sccs(nodes, edges, False)
    live = {k for k, v in nodes.items() if v["live"] == "live"}
    r["live_seeds"] = sorted(k for k in live if any(t["tag"] in dag.GROWTH_SEED for t in nodes[k].get("growth", [])))
    _, par_g = dag.propagate(nodes, edges, dag.GROWTH_SEED, keep=live)
    _, par_w = dag.propagate(nodes, edges, dag.GROWTH_WEAK, keep=live)
    r["gtaint"], r["wtaint"], r["par_w"], r["par_g"] = set(par_g), set(par_w), par_w, par_g
    order, valid, bad = dag.condensed_order(nodes, edges, exclude=frozenset(dag.STRICT_EXCLUDE), keep=live)
    pos = {}
    for p, comp in enumerate(order):
        for v in comp:
            pos[v] = p
    r["pos"], r["valid"] = pos, valid
    print(f"\n== {tag}: nodes {len(nodes)} edges {len(edges)}; schema errors {len(r['schema'])}; string-audit misses {len(r['misses'])}")
    for x in r["schema"]:
        print("   schema:", x)
    for m in r["misses"]:
        print("   MISS:", m)
    print(f"   B-strict nontrivial SCCs ({len(r['strict'])}): {r['strict']}")
    print(f"   B-all nontrivial SCCs ({len(r['all'])}): " + "; ".join(f"[{len(c)}] {c}" for c in r["all"]))
    print(f"   live GROWTH seeds: {r['live_seeds']}; order validity re-check: {'PASS' if valid else 'FAIL'}")
    return r


def main():
    nodes0, edges0 = dag.load_graph(dag.GRAPH_PATH)
    print(f"ru55_2: base graph {dag.GRAPH_PATH}")
    V = {"V0": (nodes0, edges0), "V1": var.v1(nodes0, edges0), "V2": var.v2(nodes0, edges0), "V3": var.v3(nodes0, edges0),
         "V4": var.v4(nodes0, edges0), "V5": var.v5(nodes0, edges0), "V6": var.v6(nodes0, edges0)}
    R = {k: analyse(k, *v) for k, v in V.items()}
    audit_ok = all(not R[k]["schema"] and not R[k]["misses"] for k in R)
    print(f"\nschema + string audit on all variants: {'PASS' if audit_ok else 'FAIL'}")
    fam = lambda k: sorted(tuple(c) for c in R[k]["all"])
    # V0 reproduction
    v0ok = (R["V0"]["strict"] == [] and sorted(len(c) for c in R["V0"]["all"]) == [4, 12]
            and R["V0"]["live_seeds"] == ["C_fun", "V_LF"])
    print(f"V0 reproduces dag55_2 (B-strict 0; B-all sizes [4, 12]; live seeds [C_fun, V_LF]): {'YES' if v0ok else 'NO -> UNABLE TO DECIDE'}")
    # U3
    u3_cycle = R["V1"]["strict"] == [] and fam("V1") == fam("V0")
    gt, wt = R["V1"]["gtaint"], R["V1"]["wtaint"]
    u3_growth = (R["V1"]["live_seeds"] == R["V0"]["live_seeds"] and "eta_star" not in gt
                 and (("eta_star" in wt) == ("eps_loc" in R["V0"]["wtaint"])))
    print(f"\nU3 NO-CYCLE: {'PASS' if u3_cycle else 'FAIL'} (V1 B-strict {R['V1']['strict']}; B-all family equal to V0: {fam('V1') == fam('V0')})")
    print(f"U3 NO-GROWTH: {'PASS' if u3_growth else 'FAIL'} (eta_star GROWTH-tainted: {'eta_star' in gt}; weak-tainted: {'eta_star' in wt}"
          f" vs eps_loc weak-tainted in V0: {'eps_loc' in R['V0']['wtaint']})")
    if "eta_star" in wt:
        print("   eta_star weak witness: " + " -> ".join(dag.witness(R["V1"]["par_w"], "eta_star")))
    p = R["V1"]["pos"]
    u3_order = R["V1"]["valid"] and p["eta_q"] < p["eta_star"] and p["eps_loc"] < p["eta_star"] < p["a_cb"]
    print(f"U3 ORDER: {'PASS' if u3_order else 'FAIL'} (pos eta_q {p['eta_q']}, eps_loc {p['eps_loc']}, eta_star {p['eta_star']}, a_cb {p['a_cb']}, a_D {p['a_D']}, a {p['a']}, g0 {p['g0']})")
    d1 = desc(*V["V1"], "eta_star")
    d2 = desc(*V["V2"], "eta_quiet")
    print(f"U3 SCOPE: |desc(eta_star) in V1| = {len(d1)}; |desc(eta_quiet) in V2| = {len(d2)}; "
          f"strict subset: {d1 < d2}; in V2 but not V1: {sorted(d2 - d1)}")
    print(f"   desc(eta_star): {sorted(d1)}")
    # U1
    lit = [c for c in R["V3"]["strict"] if "a_A" in c and "theta" in c]
    print(f"\nU1 LITERAL 2-CYCLE (C-A): {'FIRES' if lit else 'claim not reproduced'}: {lit}")
    u1_res = R["V4"]["strict"] == []
    print(f"U1 RESOLVED: {'PASS' if u1_res else 'FAIL'} (V4 B-strict {R['V4']['strict']})")
    print(f"   V4 B-all family vs V0: removed {sorted(set(fam('V0')) - set(fam('V4')))}; added {sorted(set(fam('V4')) - set(fam('V0')))}")
    p4 = R["V4"]["pos"]
    print(f"   V4 order: a_A0 {p4['a_A0']} < theta {p4['theta']} < a_A {p4['a_A']} < a {p4['a']}: "
          f"{p4['a_A0'] < p4['theta'] < p4['a_A'] < p4['a']}")
    # FI-1
    p5 = R["V5"]["pos"]
    fi1 = R["V5"]["strict"] == [] and fam("V5") == fam("V0") and p5["gamma"] < p5["g1_FLOW"] and p5["gamma"] < p5["g0"]
    print(f"\nFI-1 NO-CYCLE: {'PASS' if fi1 else 'FAIL'} (V5 B-strict {R['V5']['strict']}; B-all equal V0: {fam('V5') == fam('V0')}; "
          f"pos R {p5['R']}, gamma {p5['gamma']}, g1_FLOW {p5['g1_FLOW']}, g0 {p5['g0']})")
    # V6
    print("\n== checker's own controls C1-C7 on V6 (output of dag55_2_dag.controls, verbatim) ==")
    able = dag.controls(*V["V6"])
    v6ok = R["V6"]["strict"] == [] and R["V6"]["live_seeds"] == R["V0"]["live_seeds"] and able
    print(f"\nV6: {'PASS' if v6ok else 'FAIL'} (B-strict {R['V6']['strict']}; live seeds {R['V6']['live_seeds']}; controls able: {able})")
    print(f"   V6 B-all family: " + "; ".join(f"[{len(c)}] {list(c)}" for c in fam('V6')))
    # driver controls
    nB, eB = copy.deepcopy(V["V1"][0]), copy.deepcopy(V["V1"][1])
    eB.append(dict(src="eta_q", dst="eps_loc", kind="le", file="RLARGE.md", string="ε_loc/2 ≥ (16N + 3)A_dη_q", note="C-B"))
    eB.append(dict(src="a_cb", dst="eta_q", kind="le", file="RLARGE.md", string="ε_loc/2 ≥ (16N + 3)A_dη_q", note="C-B injected"))
    cB = [c for c in sccs(nB, eB, True) if "eta_star" in c or "a_cb" in c]
    print(f"\nC-B (injected a_cb -> eta_q back-edge in V1): B-strict SCC through the new node: {'FIRES' if cB else 'DOES NOT FIRE'} {cB}")
    nC, eC = copy.deepcopy(V["V1"][0]), V["V1"][1]
    nC["eta_star"]["growth"] = [dict(tag="K", file="RLARGE_U55.md", string=var.S_ETA)]
    live = {k for k, v in nC.items() if v["live"] == "live"}
    _, parC = dag.propagate(nC, eC, dag.GROWTH_SEED, keep=live, seeds_override=["eta_star"])
    cC = "g0" in parC
    print(f"C-C (K tag injected on eta_star): sink g0 tainted: {'FIRES' if cC else 'DOES NOT FIRE'}"
          + (f" via {' -> '.join(dag.witness(parC, 'g0'))}" if cC else ""))
    ok = all([audit_ok, v0ok, u3_cycle, u3_growth, u3_order, bool(lit), u1_res, fi1, v6ok, bool(cB), cC])
    print(f"\nFINAL: {'ALL PRE-REGISTERED VERDICTS PASS, ALL CONTROLS FIRE' if ok else 'NOT ALL PASS / FIRE (see above)'}")


if __name__ == "__main__":
    main()
