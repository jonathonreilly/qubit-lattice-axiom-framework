# ru55_2b (criteria: checks/ru55_2b_criteria.md, written first). Read-only use of dag55_2_dag.py, ru55_2_variants.py, ru55_2_dag.py.
import os, importlib.util, copy
HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


drv = load("ru55_2_dag", "ru55_2_dag.py")
dag, var = drv.dag, drv.var
S_CUT = "𝒢_x := Σ_{N≤n_♯}Σ_{S∋x}𝓖^{(N)}_S/|S|"


def add_cut(nodes, edges):
    n, e = copy.deepcopy(nodes), copy.deepcopy(edges)
    e.append(dict(src="n_sharp", dst="SC_k", kind="implicit", file="PLD.md", string=S_CUT, note="Codex DAG §3.1"))
    return n, e


def cut_scc(nodes, edges):
    for c in drv.sccs(nodes, edges, False):
        if "n_sharp" in c:
            return c
    return []


def main():
    n0, e0 = dag.load_graph(dag.GRAPH_PATH)
    W0 = add_cut(n0, e0)
    W6 = add_cut(*var.v6(n0, e0))
    n8, e8 = copy.deepcopy(W6[0]), copy.deepcopy(W6[1])
    var._remove_one(e8, "a_ret", "theta", "le")
    W8 = (n8, e8)
    ok = True
    for tag, (n, e) in (("W0", W0), ("W6", W6), ("W8", W8)):
        sch, miss = dag.schema(n, e), dag.string_audit(n, e)
        st = drv.sccs(n, e, True)
        cs = cut_scc(n, e)
        ok &= (not sch) and (not miss) and st == []
        print(f"{tag}: schema {len(sch)} misses {len(miss)}; B-strict SCCs {st}; cutoff SCC [{len(cs)}]: {cs}")
        print(f"     a_ret in cutoff SCC: {'a_ret' in cs}; theta in cutoff SCC: {'theta' in cs}; SC_k in: {'SC_k' in cs}")
    c0 = cut_scc(*W0)
    repro = len(c0) == 14 and "SC_k" in c0 and "a_ret" in c0
    print(f"REPRO (Codex: 14 nodes incl. SC_k, a_ret): {repro}")
    claim = ("a_ret" in cut_scc(*W6)) and ("a_ret" not in cut_scc(*W8))
    print(f"U1-LOOP claim 'a_ret is in the cutoff loop only through the fallback edge a_ret -> theta': {claim}")
    nC, eC = copy.deepcopy(W8[0]), copy.deepcopy(W8[1])
    eC.append(dict(src="gamma0", dst="n_sharp", kind="le", file="PLD.md", string=S_CUT, note="control injected"))
    ctl = "a_ret" in cut_scc(nC, eC)
    print(f"Control (inject gamma0 -> n_sharp into W8): a_ret back in the cutoff SCC: {'FIRES' if ctl else 'DOES NOT FIRE'}")
    print(f"FINAL: B-strict/audit {'PASS' if ok else 'FAIL'}; REPRO {repro}; claim {claim}; control {'fires' if ctl else 'does not fire'}")


if __name__ == "__main__":
    main()
