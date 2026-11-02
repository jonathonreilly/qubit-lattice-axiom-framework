# dag55_1 checker (criteria: checks/dag55_1_criteria.md, written before this script and before the graph data).
# Plain python 3, standard library only, no floats in any verdict. Run: python3 -I -B checks/dag55_1_dag.py
import os, sys, copy, importlib.util
from collections import deque, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
GRAPH_PATH = os.path.join(HERE, "dag55_1_graph.py")

KINDS = {"def", "le", "order", "req", "implicit", "fixedpoint"}
STRICT_EXCLUDE = {"implicit", "fixedpoint"}
GROWTH_SEED = {"K", "T", "Tk"}
GROWTH_WEAK = {"Tfix", "unstated-K", "unstated-T"}
LIVES = {"live", "off", "superseded", "unplaced"}
TIERS = {0, 1, 2, 3, 4}
BAD_STRING = "ZZZ-NOT-IN-ANY-FILE-dag55"


def load_graph(path):
    spec = importlib.util.spec_from_file_location("dag55_1_graph", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.NODES, m.EDGES


_cache = {}
def file_text(f):
    p = os.path.normpath(os.path.join(LANE, f))
    if p not in _cache:
        with open(p, encoding="utf-8") as fh:
            _cache[p] = fh.read()
    return _cache[p]


# ---------------- A. schema S and string audit S2 ----------------
def schema(nodes, edges):
    errs = []
    for nid, n in nodes.items():
        for k in ("sym", "file", "string", "live", "status", "tier"):
            if k not in n or n[k] in ("", None):
                errs.append(f"node {nid}: missing {k}")
        if n.get("live") not in LIVES:
            errs.append(f"node {nid}: bad live {n.get('live')!r}")
        if n.get("tier") not in TIERS:
            errs.append(f"node {nid}: bad tier {n.get('tier')!r}")
        for t in n.get("growth", []):
            if t.get("tag") not in GROWTH_SEED | GROWTH_WEAK:
                errs.append(f"node {nid}: bad growth tag {t.get('tag')!r}")
            if not t.get("file") or not t.get("string"):
                errs.append(f"node {nid}: growth tag without file/string")
    for i, e in enumerate(edges):
        rid = f"edge#{i} {e.get('src')}->{e.get('dst')}"
        if e.get("src") not in nodes:
            errs.append(f"{rid}: src not a node")
        if e.get("dst") not in nodes:
            errs.append(f"{rid}: dst not a node")
        if e.get("kind") not in KINDS:
            errs.append(f"{rid}: bad kind {e.get('kind')!r}")
        if not e.get("file") or not e.get("string"):
            errs.append(f"{rid}: missing file/string")
        if e.get("absorbs") and not e.get("absorb_string"):
            errs.append(f"{rid}: absorbs without its own string")
    return errs


def string_audit(nodes, edges):
    misses = []
    def chk(rid, f, s):
        try:
            t = file_text(f)
        except OSError as ex:
            misses.append((rid, f, s, "NOFILE " + str(ex)))
            return
        if s not in t:
            misses.append((rid, f, s, "MISS"))
    for nid, n in nodes.items():
        chk(f"node {nid}", n["file"], n["string"])
        if n.get("string2"):
            chk(f"node {nid} (string2)", n.get("file2", n["file"]), n["string2"])
        for t in n.get("growth", []):
            chk(f"node {nid} growth {t['tag']}", t["file"], t["string"])
    for i, e in enumerate(edges):
        rid = f"edge#{i} {e['src']}->{e['dst']}"
        chk(rid, e["file"], e["string"])
        if e.get("string2"):
            chk(rid + " (string2)", e.get("file2", e["file"]), e["string2"])
        if e.get("absorbs"):
            chk(rid + " (absorb)", e.get("absorb_file", e["file"]), e["absorb_string"])
    return misses


# ---------------- B. strongly connected components (iterative Tarjan) ----------------
def adjacency(nodes, edges, exclude=frozenset(), keep=None):
    adj = {n: [] for n in nodes if keep is None or n in keep}
    for i, e in enumerate(edges):
        if e["kind"] in exclude:
            continue
        if e["src"] in adj and e["dst"] in adj:
            adj[e["src"]].append((e["dst"], i))
    for n in adj:
        adj[n].sort()
    return adj


def tarjan(adj):
    index = {}
    low = {}
    onstack = set()
    stack = []
    sccs = []
    counter = [0]
    for root in sorted(adj):
        if root in index:
            continue
        work = [(root, 0)]
        while work:
            v, pi = work.pop()
            if pi == 0:
                index[v] = low[v] = counter[0]
                counter[0] += 1
                stack.append(v)
                onstack.add(v)
            recurse = False
            nbrs = adj[v]
            while pi < len(nbrs):
                w = nbrs[pi][0]
                pi += 1
                if w not in index:
                    work.append((v, pi))
                    work.append((w, 0))
                    recurse = True
                    break
                elif w in onstack:
                    low[v] = min(low[v], index[w])
            if recurse:
                continue
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stack.pop()
                    onstack.discard(w)
                    comp.append(w)
                    if w == v:
                        break
                sccs.append(sorted(comp))
            if work:
                u = work[-1][0]
                low[u] = min(low[u], low[v])
    return sccs


def nontrivial(sccs, adj):
    out = []
    for c in sccs:
        if len(c) >= 2:
            out.append(c)
        else:
            v = c[0]
            if any(w == v for (w, _) in adj[v]):
                out.append(c)
    return out


def shortest_path(adj, a, b, within=None):
    """BFS shortest path a -> b; returns list of edge indices, or None."""
    prev = {a: None}
    dq = deque([a])
    while dq:
        v = dq.popleft()
        for (w, ei) in adj[v]:
            if within is not None and w not in within:
                continue
            if w not in prev:
                prev[w] = (v, ei)
                if w == b:
                    path = []
                    x = w
                    while prev[x] is not None:
                        u, ej = prev[x]
                        path.append(ej)
                        x = u
                    return list(reversed(path))
                dq.append(w)
    return None


def cycle_through(adj, comp):
    s = comp[0]
    cset = set(comp)
    best = None
    for (w, ei) in adj[s]:
        if w not in cset:
            continue
        if w == s:
            return [ei]
        p = shortest_path(adj, w, s, within=cset)
        if p is not None and (best is None or len(p) + 1 < len(best)):
            best = [ei] + p
    return best


# ---------------- C. growth propagation ----------------
def propagate(nodes, edges, seed_tags, keep=None, seeds_override=None):
    """Return (seeds, parent) where parent[n] = (prev_node, edge_index) on a shortest witness path."""
    if seeds_override is not None:
        seeds = list(seeds_override)
    else:
        seeds = sorted(n for n, r in nodes.items()
                       if (keep is None or n in keep) and any(t["tag"] in seed_tags for t in r.get("growth", [])))
    adj = defaultdict(list)
    for i, e in enumerate(edges):
        if e.get("absorbs"):
            continue
        if keep is not None and (e["src"] not in keep or e["dst"] not in keep):
            continue
        adj[e["src"]].append((e["dst"], i))
    parent = {s: None for s in seeds}
    dq = deque(seeds)
    while dq:
        v = dq.popleft()
        for (w, ei) in sorted(adj[v]):
            if w not in parent:
                parent[w] = (v, ei)
                dq.append(w)
    return seeds, parent


def witness(parent, n):
    path = [n]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]][0])
    return list(reversed(path))


# ---------------- D. order (Kahn on the condensation, tie-break by (tier, id)) ----------------
def condensed_order(nodes, edges, exclude=frozenset(), keep=None):
    adj = adjacency(nodes, edges, exclude=exclude, keep=keep)
    sccs = tarjan(adj)
    comp_of = {}
    for ci, c in enumerate(sccs):
        for v in c:
            comp_of[v] = ci
    key = {ci: (min(nodes[v]["tier"] for v in c), min(c)) for ci, c in enumerate(sccs)}
    succ = defaultdict(set)
    indeg = {ci: 0 for ci in range(len(sccs))}
    for v in adj:
        for (w, _) in adj[v]:
            a, b = comp_of[v], comp_of[w]
            if a != b and b not in succ[a]:
                succ[a].add(b)
                indeg[b] += 1
    import heapq
    heap = [(key[ci], ci) for ci in indeg if indeg[ci] == 0]
    heapq.heapify(heap)
    order = []
    while heap:
        _, ci = heapq.heappop(heap)
        order.append(ci)
        for b in sorted(succ[ci]):
            indeg[b] -= 1
            if indeg[b] == 0:
                heapq.heappush(heap, (key[b], b))
    ok = len(order) == len(sccs)
    pos = {}
    for p, ci in enumerate(order):
        for v in sccs[ci]:
            pos[v] = p
    bad = []
    for v in adj:
        for (w, ei) in adj[v]:
            if comp_of[v] != comp_of[w] and not pos[v] < pos[w]:
                bad.append(ei)
    return [sccs[ci] for ci in order], ok and not bad, bad


# ---------------- reporting helpers ----------------
def fmt_edge(edges, ei):
    e = edges[ei]
    s = f"    {e['src']} -> {e['dst']}  [{e['kind']}]  {e['file']}: \"{e['string']}\""
    if e.get("string2"):
        s += f"  + \"{e['string2']}\" ({e.get('file2', e['file'])})"
    return s


def report_cycles(title, nodes, edges, exclude):
    adj = adjacency(nodes, edges, exclude=exclude)
    nts = nontrivial(tarjan(adj), adj)
    print(f"\n== {title}: {len(nts)} nontrivial SCC(s)")
    for c in nts:
        print(f"  SCC ({len(c)} nodes): {', '.join(c)}")
        cyc = cycle_through(adj, c)
        if cyc:
            print("  one explicit cycle:")
            for ei in cyc:
                print(fmt_edge(edges, ei))
    return nts


def run_real(nodes, edges):
    print("=" * 100)
    print("REAL GRAPH")
    print("=" * 100)
    errs = schema(nodes, edges)
    print(f"S (schema): {'PASS' if not errs else 'FAIL'}  ({len(errs)} error(s))")
    for x in errs:
        print("  ", x)
    misses = string_audit(nodes, edges)
    print(f"S2 (string audit): {'PASS' if not misses else 'FAIL'}  ({len(misses)} miss(es))")
    for m in misses:
        print("   ", m)
    if errs or misses:
        print("Schema or string audit failed: no further verdict on the real graph (criteria A).")
        return None

    # E. counts
    by_live = defaultdict(int)
    for n in nodes.values():
        by_live[n["live"]] += 1
    by_kind = defaultdict(int)
    for e in edges:
        by_kind[e["kind"]] += 1
    print(f"\nE. counts: nodes {len(nodes)} {dict(sorted(by_live.items()))}; edges {len(edges)} {dict(sorted(by_kind.items()))}; "
          f"absorbing edges {sum(1 for e in edges if e.get('absorbs'))}")
    print("DAG-F3 (unplaced) nodes:")
    for nid in sorted(n for n in nodes if nodes[n]["live"] == "unplaced"):
        print(f"  {nid}: {nodes[nid]['sym']} -- {nodes[nid].get('note', '')}")

    # B. cycles
    nts_all = report_cycles("B-all (every edge)", nodes, edges, frozenset())
    nts_strict = report_cycles("B-strict (without implicit/fixedpoint edges)", nodes, edges, frozenset(STRICT_EXCLUDE))
    live = {n for n, r in nodes.items() if r["live"] == "live"}
    adj_live = adjacency(nodes, edges, keep=live)
    nts_live = nontrivial(tarjan(adj_live), adj_live)
    print(f"\n== B-all restricted to live nodes: {len(nts_live)} nontrivial SCC(s): " + "; ".join("{" + ", ".join(c) + "}" for c in nts_live))
    print(f"\nDAG-F1 verdict: {'FOUND' if nts_all else 'NOT FOUND'} in B-all; "
          f"{'FOUND' if nts_strict else 'NOT FOUND'} in B-strict (def/le/order/req only).")

    # C. growth
    sinks = sorted(n for n, r in nodes.items() if r["tier"] == 4)
    print("\n== C. growth seeds (K, T, Tk) with evidence:")
    for n in sorted(nodes):
        for t in nodes[n].get("growth", []):
            if t["tag"] in GROWTH_SEED:
                print(f"  [{nodes[n]['live']}] {n} {t['tag']}: {t['file']}: \"{t['string']}\"")
    print("== C. weak (uniformity-not-established) tags (Tfix, unstated-K, unstated-T) with evidence:")
    for n in sorted(nodes):
        for t in nodes[n].get("growth", []):
            if t["tag"] in GROWTH_WEAK:
                print(f"  [{nodes[n]['live']}] {n} {t['tag']}: {t['file']}: \"{t['string']}\"")
    for label, keep in (("full graph", None), ("live subgraph", live)):
        for cls, tags in (("GROWTH (K/T/Tk)", GROWTH_SEED), ("UNIFORMITY-NOT-ESTABLISHED (Tfix/unstated)", GROWTH_WEAK)):
            seeds, parent = propagate(nodes, edges, tags, keep=keep)
            tainted = sorted(parent)
            print(f"\n-- {cls} on the {label}: seeds {seeds}; tainted {len(tainted)} node(s)")
            for n in tainted:
                if n in seeds:
                    continue
                print(f"   {n}: " + " -> ".join(witness(parent, n)))
            for s in sinks:
                if keep is not None and s not in keep:
                    continue
                print(f"   SINK {s}: {'TAINTED via ' + ' -> '.join(witness(parent, s)) if s in parent else 'not tainted'}")
    live_seeds = sorted(n for n in nodes if nodes[n]["live"] == "live"
                        and any(t["tag"] in GROWTH_SEED for t in nodes[n].get("growth", [])))
    print(f"\nDAG-F2 verdict: {'FOUND' if live_seeds else 'NOT FOUND'} (live seeds: {live_seeds})")

    # D. order
    for label, exclude, keep in (("live subgraph, B-strict edges", frozenset(STRICT_EXCLUDE), live),
                                 ("live subgraph, all edges (SCCs condensed)", frozenset(), live),
                                 ("full graph, all edges (SCCs condensed)", frozenset(), None)):
        order, valid, bad = condensed_order(nodes, edges, exclude=exclude, keep=keep)
        print(f"\n== D. order ({label}): {len(order)} position(s); validity re-check {'PASS' if valid else 'FAIL'}"
              + (f" (bad edges {bad})" if bad else ""))
        for p, comp in enumerate(order):
            tiers = sorted({nodes[v]['tier'] for v in comp})
            print(f"  {p:3d} t{tiers} " + (" + ".join(comp) if len(comp) > 1 else comp[0]))

    # volume table
    print("\n== volume behaviour as stated by the sources (informational 'vol' field):")
    for n in sorted(nodes, key=lambda x: (nodes[x]["live"], nodes[x]["tier"], x)):
        print(f"  [{nodes[n]['live']:10s}] t{nodes[n]['tier']} {n:16s} {nodes[n].get('vol', '')}")
    return dict(nts_all=nts_all, nts_strict=nts_strict, live_seeds=live_seeds)


# ---------------- controls ----------------
def controls(nodes, edges):
    print("\n" + "=" * 100)
    print("CONTROLS")
    print("=" * 100)
    results = {}
    sink = "g0"
    thr = "eps1"
    # C1: injected back-edge sink -> threshold
    adj_strict = adjacency(nodes, edges, exclude=frozenset(STRICT_EXCLUDE))
    pre = shortest_path(adj_strict, thr, sink)
    e2 = copy.deepcopy(edges)
    inj = dict(src=sink, dst=thr, kind="le", file="RLARGE.md", string="a := min{θa_bad, a_A}", note="INJECTED (control C1)")
    e2.append(inj)
    ok1 = True
    for title, excl in (("B-all", frozenset()), ("B-strict", frozenset(STRICT_EXCLUDE))):
        adj = adjacency(nodes, e2, exclude=excl)
        nts = nontrivial(tarjan(adj), adj)
        hit = [c for c in nts if sink in c and thr in c]
        path = shortest_path(adj, thr, sink)
        uses = path is not None
        print(f"C1 {title}: SCC containing {sink} and {thr}: {'yes' if hit else 'no'}; cycle through the injected edge: "
              + (f"{thr} -> ... -> {sink} -> {thr} ({len(path) + 1} edges)" if uses else "none"))
        if uses:
            for ei in path:
                print(fmt_edge(e2, ei))
            print(f"    {sink} -> {thr}  [le]  INJECTED")
        ok1 = ok1 and bool(hit) and uses
    print(f"C1 (pre-condition: strict path {thr} -> {sink} exists in the real graph: {'yes' if pre else 'no'}) -> "
          f"{'FIRES (as designed)' if ok1 and pre else 'DOES NOT FIRE'}")
    results["C1"] = ok1 and bool(pre)
    # C2: injected K-growth on a tier-0 source with a path to the sink
    src = "kappa_pm"
    seeds, parent = propagate(nodes, edges, GROWTH_SEED, seeds_override=[src])
    ok2 = sink in parent and witness(parent, sink)[0] == src and nodes[src]["tier"] == 0
    print(f"C2: seed {src} (tier {nodes[src]['tier']}) tagged K (INJECTED); sink {sink} "
          + ("TAINTED via " + " -> ".join(witness(parent, sink)) if sink in parent else "not tainted")
          + f" -> {'FIRES (as designed)' if ok2 else 'DOES NOT FIRE'}")
    results["C2"] = ok2
    # C3: schema with a dangling edge
    e3 = copy.deepcopy(edges)
    e3.append(dict(src="eps1", dst="ZZZ_nonexistent", kind="le", file="RLARGE.md", string="a := min{θa_bad, a_A}"))
    errs = schema(nodes, e3)
    ok3 = any("ZZZ_nonexistent" in x or "dst not a node" in x for x in errs)
    print(f"C3: schema on a graph with a dangling edge -> {'FAIL (as designed)' if ok3 else 'PASS (control did not fire)'}: {errs[-1:] if errs else []}")
    results["C3"] = ok3
    # C4: null control, unique order
    n4 = {k: dict(sym=k, file="x", string="x", live="live", status="x", tier=t, growth=[])
          for k, t in (("a", 0), ("b", 1), ("c", 1), ("d", 2), ("e", 3), ("f", 4))}
    e4 = [dict(src=s, dst=d, kind="def", file="x", string="x") for s, d in
          (("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"), ("a", "d"), ("b", "f"))]
    adj4 = adjacency(n4, e4)
    nts4 = nontrivial(tarjan(adj4), adj4)
    order4, valid4, _ = condensed_order(n4, e4)
    flat4 = [c[0] for c in order4]
    expected4 = ["a", "b", "c", "d", "e", "f"]
    ok4 = (not nts4) and flat4 == expected4 and valid4
    print(f"C4: null control: SCCs {nts4}; order {flat4} (expected {expected4}) -> {'PASS (as designed)' if ok4 else 'FAIL'}")
    results["C4"] = ok4
    # C5: positive control, one 3-cycle
    n5 = {k: dict(sym=k, file="x", string="x", live="live", status="x", tier=1, growth=[]) for k in ("a", "b", "c", "d")}
    e5 = [dict(src=s, dst=d, kind="le", file="x", string="x") for s, d in (("a", "b"), ("b", "c"), ("c", "a"), ("c", "d"))]
    adj5 = adjacency(n5, e5)
    nts5 = nontrivial(tarjan(adj5), adj5)
    ok5 = nts5 == [["a", "b", "c"]]
    print(f"C5: positive control: nontrivial SCCs {nts5} (expected [['a', 'b', 'c']]) -> {'FIRES (as designed)' if ok5 else 'DOES NOT FIRE'}")
    results["C5"] = ok5
    # C6: absorb control
    n6 = {k: dict(sym=k, file="x", string="x", live="live", status="x", tier=1, growth=[]) for k in ("s", "x", "y")}
    n6["s"]["growth"] = [dict(tag="K", file="x", string="x")]
    e6 = [dict(src="s", dst="x", kind="def", file="x", string="x"),
          dict(src="x", dst="y", kind="def", file="x", string="x", absorbs=True, absorb_string="x")]
    _, par6 = propagate(n6, e6, GROWTH_SEED)
    ok6 = ("x" in par6) and ("y" not in par6)
    print(f"C6: absorb control: x tainted {('x' in par6)}, y tainted {('y' in par6)} -> {'PASS (as designed)' if ok6 else 'FAIL'}")
    results["C6"] = ok6
    # C7: string audit designed FAIL
    e7 = copy.deepcopy(edges)
    victim = 0
    e7[victim]["string"] = BAD_STRING
    misses = string_audit(nodes, e7)
    ok7 = len(misses) == 1 and misses[0][0].startswith(f"edge#{victim} ")
    print(f"C7: string audit with edge#{victim}'s string replaced -> {'FAIL on exactly that record (as designed)' if ok7 else 'unexpected'}: {misses}")
    results["C7"] = ok7
    allok = all(results.values())
    print(f"\nCONTROLS: {results} -> checker {'ABLE TO DECIDE' if allok else 'UNABLE TO DECIDE'}")
    return allok


def main():
    nodes, edges = load_graph(GRAPH_PATH)
    print(f"dag55_1: graph {GRAPH_PATH}")
    real = run_real(nodes, edges)
    able = controls(nodes, edges)
    print("\n" + "=" * 100)
    if real is None:
        print("FINAL: real graph failed schema/string audit; no DAG verdict (fix under a new id).")
    else:
        print(f"FINAL: checker {'ABLE TO DECIDE' if able else 'UNABLE TO DECIDE'}; "
              f"DAG-F1 {'FOUND' if real['nts_all'] else 'NOT FOUND'} (B-all), "
              f"{'FOUND' if real['nts_strict'] else 'NOT FOUND'} (B-strict); "
              f"DAG-F2 {'FOUND' if real['live_seeds'] else 'NOT FOUND'} (live seeds {real['live_seeds']}).")


if __name__ == "__main__":
    main()
