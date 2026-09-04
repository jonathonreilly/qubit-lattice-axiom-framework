"""Full star evaluation, including exact handling of LIGHTLIKE bounding rays.

A wedge whose bounding ray is null has an individually DIVERGENT angle
(the rapidity blows up at the light cone).  But the two wedges that share that
null ray diverge with opposite signs, so their sum is finite.  We therefore
book-keep each wedge as an "arc"

      arc(start_ray, end_ray, m)   contributing   m*pi/2 - i*(q_end - q_start)

where m is the number of light-cone crossings, counted with the convention
"a light ray is charged to the arc that DEPARTS from it, not the one that
arrives at it".  Arcs sharing a null ray are then merged, which cancels the
divergent rapidity exactly.  Around a closed star all the finite rapidities
telescope and sum(m) must be 4.
"""
import math

from lorentzian_angles import HingeFrame, wedge_angle, check_wedge_branch

TWOPI = 2.0 * math.pi
NULLTOL = 1e-11


def _ray_data(fr, R):
    """(kind,index,q) with kind 's' (sector k, rapidity q) or 'n' (light ray j)."""
    t, x = -float(R @ _ETA @ fr.T), float(R @ _ETA @ fr.X)
    q2 = x * x - t * t
    scale = max(t * t, x * x)
    if abs(q2) <= NULLTOL * scale:
        j = 0 if (t > 0 and x > 0) else 1 if (t > 0 and x < 0) else 2 if x < 0 else 3
        return ("n", j, None, t, x)
    if q2 > 0.0:
        m = math.sqrt(q2)
        return ("s", 0 if x > 0 else 2, math.asinh(t / m if x > 0 else -t / m), t, x)
    m = math.sqrt(-q2)
    return ("s", 1 if t > 0 else 3, math.asinh(x / m if t > 0 else -x / m), t, x)


import numpy as np
_ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def eval_star(fr, entries, P, a):
    """Sum of complex dihedral angles around one hinge.

    entries : list of (simplex_id, (d,e)) -- the wedges
    Returns (total_dphi, total_crossings, n_null_rays, max_branch_err).
    Raises ValueError if the bookkeeping is inconsistent.
    """
    if fr.kind == "E":
        tot, worst = 0.0 + 0j, 0.0
        for _, (d, e) in entries:
            D, E = fr.project(P(d) - P(a)), fr.project(P(e) - P(a))
            dphi, _ = wedge_angle(fr, D, E)
            worst = max(worst, check_wedge_branch(fr, D, E, dphi))
            tot += dphi
        return tot, 0, 0, worst

    # ---- Lorentzian orthogonal plane -------------------------------------
    rays = {}          # apex vertex -> ray data
    arcs = []          # (start_apex, end_apex, m)
    worst = 0.0
    for _, (d, e) in entries:
        for v in (d, e):
            if v not in rays:
                rays[v] = _ray_data(fr, fr.project(P(v) - P(a)))
        pd, pe = rays[d], rays[e]
        # orient: convex cone runs CCW from first to second  <=>  D^E > 0
        if pd[3] * pe[4] - pd[4] * pe[3] < 0.0:      # t_d*x_e - x_d*t_e  (=-D^E)
            first, second = d, e
        else:
            first, second = e, d
        f, s = rays[first], rays[second]
        if f[0] == "s" and s[0] == "s":
            m = (s[1] - f[1]) % 4
            if m == 3:
                raise ValueError("non-convex wedge")
            D, E = fr.project(P(first) - P(a)), fr.project(P(second) - P(a))
            worst = max(worst, check_wedge_branch(fr, D, E, complex(m * math.pi / 2,
                                                                    -(s[2] - f[2]))))
        elif f[0] == "s":                            # arrive at a light ray
            m = (s[1] - f[1]) % 4
        elif s[0] == "s":                            # depart from a light ray
            m = (s[1] - f[1]) % 4
            if m == 0:
                m = 4
        else:                                        # both ends lightlike
            m = 1 + ((s[1] - f[1] - 1) % 4)
        arcs.append([first, second, m])

    # ---- merge arcs across null rays -------------------------------------
    n_null = sum(1 for r in rays.values() if r[0] == "n")
    if n_null:
        changed = True
        while changed:
            changed = False
            starts = {}
            for i, arc in enumerate(arcs):
                if arc is None:
                    continue
                starts.setdefault(arc[0], i)
            for i, arc in enumerate(arcs):
                if arc is None or rays[arc[1]][0] != "n":
                    continue
                j = starts.get(arc[1])
                if j is None or j == i:
                    continue
                nxt = arcs[j]
                arcs[i] = [arc[0], nxt[1], arc[2] + nxt[2]]
                arcs[j] = None
                changed = True
                break
        arcs = [a_ for a_ in arcs if a_ is not None]

    tot = 0.0 + 0j
    mtot = 0
    for st, en, m in arcs:
        rs, re = rays[st], rays[en]
        if rs[0] == "n" or re[0] == "n":
            raise ValueError("unmerged null ray remains")
        tot += complex(m * math.pi / 2.0, -(re[2] - rs[2]))
        mtot += m
    return tot, mtot, n_null, worst
