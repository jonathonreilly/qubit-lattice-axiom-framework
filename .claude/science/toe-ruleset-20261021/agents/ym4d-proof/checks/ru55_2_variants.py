# ru55_2 variant DATA builder (criteria: checks/ru55_2_criteria.md, written first). No checker logic here.
# Reads checks/dag55_2_graph.py read-only (via the checker's own loader) and returns deep-copied, modified graphs.
import copy

U55 = "RLARGE_U55.md"
S_ETA = "η* := min{η_q, ε_loc/(2(16N + 3)A_d)}"
S_ACB = "a_cb♯ := min{c_pr·min{ε_loc²/4, t_pr²}, κε_loc²/(64N), c_pr·min{η*², t_pr²}}"
S_ETAQ = "η′ := η_q/R"
S_AFL = "a_fl(η′/2) = a_fl(η_q/2)/R²"
S_AA_LIT = "a_A := min{λκε_1²/256, 6θa_bad}"          # PLD.md l.2485
S_AA0 = "a_A° := the θ-free entries of the route's a_A"
S_TH = "θ := min{θ_cap, a_A°/a_bad}"
S_AA = "a_A := min{a_A°, 6θa_bad}"
S_GAM = "γ^{-2} ≥ max{2R, 2/min{1, κ}} + R + (3/2)β_0'log L"


def _node(sym, string, status, tier, vol="as ε_1"):
    return dict(sym=sym, file=U55, string=string, live="live", status=status, tier=tier, vol=vol, note="", growth=[])


def _edge(src, dst, kind, string, file=U55, note=""):
    return dict(src=src, dst=dst, kind=kind, file=file, string=string, note=note)


def _remove_one(edges, src, dst, kind):
    idx = [i for i, e in enumerate(edges) if e["src"] == src and e["dst"] == dst and e["kind"] == kind]
    assert len(idx) == 1, f"expected exactly one edge {src}->{dst} [{kind}], found {len(idx)}"
    del edges[idx[0]]


def v1(nodes, edges):
    n, e = copy.deepcopy(nodes), copy.deepcopy(edges)
    _remove_one(e, "eta_q", "eps_loc", "le")                       # (TC) is no longer a hypothesis
    n["eta_star"] = _node("η* (W-cb♯ split threshold)", S_ETA, "DEF (RLARGE_U55 §2.2)", 2)
    for s in ("eta_q", "eps_loc", "N", "A_d"):
        e.append(_edge(s, "eta_star", "def", S_ETA))
    e.append(_edge("eta_star", "a_cb", "def", S_ACB))
    n["a_cb"]["status"] = "CONDITIONAL ⇐ (CLS-min) [W-cb♯: (TC) removed]"
    return n, e


def v2(nodes, edges):
    n, e = copy.deepcopy(nodes), copy.deepcopy(edges)
    _remove_one(e, "eta_q", "eps_loc", "le")
    n["eta_quiet"] = _node("η′ := η_q/R (lowered quietness threshold)", S_ETAQ, "DEF (SMALLNESS_DAG §8.1 form)", 2)
    for s in ("eta_q", "eps_loc", "N", "A_d"):
        e.append(_edge(s, "eta_quiet", "def", S_ETAQ))
    e.append(_edge("eta_quiet", "a_cb", "def", S_ETAQ))
    e.append(_edge("eta_quiet", "a_ret", "def", S_AFL))
    return n, e


def v3(nodes, edges):
    n, e = copy.deepcopy(nodes), copy.deepcopy(edges)
    e.append(_edge("theta", "a_A", "def", S_AA_LIT, file="PLD.md", note="route (iii), PLD §18.7, literal"))
    return n, e


def v4(nodes, edges):
    n, e = v3(nodes, edges)
    _remove_one(e, "a_A", "theta", "le")
    n["a_A0"] = _node("a_A° (θ-free entries of a_A)", S_AA0, "DEF (RLARGE_U55 §1.5)", 1)
    e.append(_edge("kappa_RL", "a_A0", "def", S_AA0))
    e.append(_edge("eps1", "a_A0", "def", S_AA0))
    e.append(_edge("a_A0", "theta", "le", S_TH))
    e.append(_edge("a_A0", "a_A", "def", S_AA))
    return n, e


def v5(nodes, edges):
    n, e = copy.deepcopy(nodes), copy.deepcopy(edges)
    for s in ("R", "kappa_RL", "L"):
        e.append(_edge(s, "gamma", "le", S_GAM))
    return n, e


def v6(nodes, edges):
    n, e = v1(nodes, edges)
    # V4 on top of V1
    e.append(_edge("theta", "a_A", "def", S_AA_LIT, file="PLD.md", note="route (iii), PLD §18.7, literal"))
    _remove_one(e, "a_A", "theta", "le")
    n["a_A0"] = _node("a_A° (θ-free entries of a_A)", S_AA0, "DEF (RLARGE_U55 §1.5)", 1)
    e.append(_edge("kappa_RL", "a_A0", "def", S_AA0))
    e.append(_edge("eps1", "a_A0", "def", S_AA0))
    e.append(_edge("a_A0", "theta", "le", S_TH))
    e.append(_edge("a_A0", "a_A", "def", S_AA))
    # V5 on top
    for s in ("R", "kappa_RL", "L"):
        e.append(_edge(s, "gamma", "le", S_GAM))
    return n, e
