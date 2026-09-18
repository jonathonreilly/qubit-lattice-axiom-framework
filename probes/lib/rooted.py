"""the hard inductive case: processed z all of whose 1-predecessors u have rooted minimum v(u) = 0 (seeds or tight processed nodes).
Print v(z), the kinds of the preds, and the optimal rooted tree of z (nodes by level, seeds/forks)."""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from mintree import MinTree, run_automaton, level, preds
import family as m

def rooted(eta, z, c=1.0):
    mt2 = MinTree(eta, z)
    cost = np.zeros(mt2.nvar)
    for w in mt2.V: cost[mt2.idx[w]] = {"proc": 1.0, "amp": -c, "seed": -3.0}[mt2.kind[w]]
    ub = mt2.bounds.ub.copy(); lb = mt2.bounds.lb.copy()
    for w in mt2.V:
        if level(w) > level(z): ub[mt2.idx[w]] = 0
    res = milp(cost, constraints=[LinearConstraint(mt2.A, mt2.lo, mt2.hi)], integrality=mt2.integrality, bounds=Bounds(lb, ub), options={"disp": False, "time_limit": 60})
    if res.status != 0: return None, None
    xv = res.x
    nodes = [w for w in mt2.V if xv[mt2.idx[w]] > 0.5]
    arrows = [(a, b) for k, (a, b) in enumerate(mt2.arrows) if xv[mt2.off_a + k] > 0.5]
    forks = [(a, b) for k, (a, b) in enumerate(mt2.forks) if xv[mt2.off_f + k] > 0.5]
    E = sum(1 for w in nodes if mt2.kind[w] == "proc"); A = sum(1 for w in nodes if mt2.kind[w] == "amp"); Sn = sum(1 for w in nodes if mt2.kind[w] == "seed")
    return E - 3 * (Sn - 1) - A, dict(nodes=nodes, arrows=arrows, forks=forks, E=E, A=A, S=Sn, kind=mt2.kind)

