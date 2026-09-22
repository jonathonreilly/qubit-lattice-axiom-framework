"""Independent exact minimum of the counted family's cost E - 3(|S|-1) - c|A| over marked trees through a root x,
by a level-by-level connectivity dynamic programme (no integer programming, no code from probes/lib).

Family, read off its definition: a tree whose nodes are 1-sites and contains x; every non-seed node carries exactly one
downward arrow to a 1-predecessor that is in the tree; seeds (no 1-predecessor) carry none; the remaining edges are forks
between same-level 1-sites differing by e_a - e_b.  Arrows drop one level and forks stay in a level, so edges touching
level l are all decided once level l+1 has been processed; a component with no node on the newest level can never grow.
State = component labels of the tree's nodes on the previous level and on the processed prefix of the current level."""
E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
FORK = {tuple(E3[a][i] - E3[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b}


def lev(z):
    return z[0] + z[1] + z[2]


def canon(labels):
    m = {}
    out = []
    for q in labels:
        if q == 0:
            out.append(0)
        else:
            if q not in m:
                m[q] = len(m) + 1
            out.append(m[q])
    return tuple(out)


def exact_min(eta, x, c=1, rooted=False):
    ones = {z for z, v in eta.items() if v == 1}
    assert x in ones
    p1 = {z: [tuple(z[i] - E3[j][i] for i in range(3)) for j in range(3)] for z in ones}
    p1 = {z: [p for p in ps if p in ones] for z, ps in p1.items()}
    kind = {z: ("seed" if not p1[z] else "amp" if len(p1[z]) == 1 else "proc") for z in ones}
    w = {"proc": 1, "amp": -c, "seed": -3}
    lx = lev(x)
    top = lx if rooted else max(lev(z) for z in ones)
    V = {l: sorted(z for z in ones if lev(z) == l) for l in range(-1, top + 2)}
    best = None
    states = {(): 0}          # labels of the previous level's nodes (level -1: none)
    for l in range(0, top + 2):
        prevV, curV = V[l - 1], V[l]
        npv = len(prevV)
        pidx = {z: j for j, z in enumerate(prevV)}
        work = {st: val for st, val in states.items()}      # st = prev labels + processed current labels
        for i, u in enumerate(curV):
            new = {}

            def put(key, v):
                if key not in new or v < new[key]:
                    new[key] = v
            for st, val in work.items():
                if u != x:
                    put(canon(st + (0,)), val)
                if kind[u] == "seed":
                    opts = [max(st, default=0) + 1]
                else:
                    opts = sorted({st[pidx[p]] for p in p1[u] if st[pidx[p]] != 0})
                if not opts:
                    continue
                partners = [npv + k for k in range(i) if st[npv + k] != 0 and tuple(u[t] - curV[k][t] for t in range(3)) in FORK]
                for lab in opts:
                    for mask in range(1 << len(partners)):
                        labels = list(st) + [lab]
                        ok = True
                        for b, k in enumerate(partners):
                            if mask >> b & 1:
                                la, lb = labels[-1], labels[k]
                                if la == lb:
                                    ok = False
                                    break
                                labels = [la if q == lb else q for q in labels]
                        if ok:
                            put(canon(tuple(labels)), val + w[kind[u]])
            work = new
        # level l complete: components on level l-1 that do not reach level l are closed for good
        states = {}
        for st, val in work.items():
            prev_labs = {q for q in st[:npv] if q}
            cur_labs = {q for q in st[npv:] if q}
            if prev_labs - cur_labs:
                if len(prev_labs) == 1 and not cur_labs and l - 1 >= lx:
                    best = val if best is None else min(best, val)
                continue
            key = canon(st[npv:])
            if key not in states or val < states[key]:
                states[key] = val
    return None if best is None else best + 3
