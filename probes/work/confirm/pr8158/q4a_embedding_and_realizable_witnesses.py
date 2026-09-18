#!/usr/bin/env python3
"""J:confirm:J-attack-PR8158 - independent test of the finder's witness-realizability HIT on block 24 (PR #8158): Q4(a), "W a plaquette, E
one site adjacent to two adjacent corners", in a note whose declared setting is "the nearest-neighbour graph of Z^3 restricted to W u E".

Different machinery from the finder (who built the abstract five-vertex graph and looked for a triangle):
  * the note's setting sentence and Q4(a) are read from the note, and the runner's own Q4(a) bond list from the runner, at the PR head;
  * an exhaustive search in Z^3: for each of the three plaquette orientations, every site of a box around it is tested for adjacency to
    two corners (adjacent or diagonal); and the parity 2-colouring (x_1 + x_2 + x_3 mod 2) is applied to the runner's graph;
  * the stated total-variation values are recomputed through Q1's product form (the unrecorded site summed into the factor
    F(v_c0, v_c1) = (phi^2)(v_c0, v_c1)) rather than by the runner's enumeration of the five-site law, to show which graph they belong to;
  * the Z^3-realizable windows that do carry a component touching two recorded sites are computed the same way: the cube with its top
    face unrecorded (the note's Q4(b); ring contraction of 6 x 6 matrices) and the smallest single-component bridge, two sites stacked
    over an edge of the plaquette (factor phi^3).
Prints "HIT: confirmed - ..." when this test reaches the finder's conclusion, or "SUMMARY: not reproduced - ...".
"""
import itertools
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
BRANCH = "physics-loop/admissibility-induced-law-block24-unrecorded-sites-free-window-versus-integrated-exterior-fork-20260915"
HEAD = "dd78e677ba6cda496d6de20cfc215ef8bd09374f"
NOTE = ("docs/ADMISSIBILITY_RULE_UNRECORDED_SITES_FREE_WINDOW_VERSUS_INTEGRATED_EXTERIOR_READINGS_DIFFER_IFF_AN_UNRECORDED_COMPONENT_"
        "TOUCHES_TWO_RECORDED_SITES_BOUNDED_THEOREM_NOTE_2026-09-15.md")
RUNNER = "scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py"


def show(path):
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def phi_mat(p, q, r):
    return np.array([[p if a == b else (q if a == b ^ 1 else r) for b in range(6)] for a in range(6)], dtype=object)


def tv_plaquette(p, q, r, F):
    """R1 on the four-cycle c0 c1 c2 c3 against R2 = R1 times the exterior factor F(v) (Q1's product form)."""
    P = phi_mat(p, q, r)
    w1, w2 = {}, {}
    for v in itertools.product(range(6), repeat=4):
        b = P[v[0], v[1]] * P[v[1], v[2]] * P[v[2], v[3]] * P[v[3], v[0]]
        w1[v] = b
        w2[v] = b * F(v)
    z1, z2 = sum(w1.values()), sum(w2.values())
    return sum(abs(Fraction(w1[v], z1) - Fraction(w2[v], z2)) for v in w1) / 2


def main():
    note = show(NOTE)
    runner = show(RUNNER)
    setting = "with the nearest-neighbour graph of `Z³` restricted to `W ∪ E`" in note
    q4a = re.search(r"\(a\) `W` a plaquette, `E` one site adjacent to two adjacent corners: `(\d+)/(\d+)` at `\(3, 1, 2\)`, `(\d+)/(\d+)` at "
                    r"`\(5, 2, 4\)`, `(\d+)/(\d+)` at `\(2, 1, 2\)`", note)
    stated = [Fraction(int(q4a.group(1)), int(q4a.group(2))), Fraction(int(q4a.group(3)), int(q4a.group(4))), Fraction(int(q4a.group(5)), int(q4a.group(6)))]
    cube_stated = Fraction(*map(int, re.search(r"\(b\) `W` the bottom face of the unit cube.*?: `(\d+)/(\d+)` at `\(3, 1, 2\)`", note).groups()))
    w4b = re.search(r'W4B = \[\("c0", "c1"\), \("c1", "c2"\), \("c2", "c3"\), \("c3", "c0"\)\]', runner) is not None
    extra = re.search(r'W4B \+ \[\("c0", "x"\), \("c1", "x"\)\]', runner) is not None
    print(f"[inputs] at {HEAD[:10]}: setting sentence 'nearest-neighbour graph of Z^3 restricted to W u E' present: {setting}; Q4(a) stated "
          f"{[str(x) for x in stated]}; the runner's Q4(a) bonds = the four-cycle c0-c1-c2-c3 plus c0-x and c1-x (c0, c1 bonded): {w4b and extra}")
    # ---- Z^3 search
    units = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    add = lambda a, b: tuple(x + y for x, y in zip(a, b))
    adj = lambda a, b: sum(abs(x - y) for x, y in zip(a, b)) == 1
    worst = {}
    for i, j in itertools.combinations(range(3), 2):
        c = [(0, 0, 0), units[i], add(units[i], units[j]), units[j]]
        touch2 = []
        for x in itertools.product(range(-2, 4), repeat=3):
            if x in c:
                continue
            hit = [k for k in range(4) if adj(x, c[k])]
            if len(hit) >= 2:
                touch2.append((x, hit))
        worst[(i, j)] = touch2
    none = all(not v for v in worst.values())
    # parity colouring of the runner's graph
    verts = ["c0", "c1", "c2", "c3", "x"]
    edges = [("c0", "c1"), ("c1", "c2"), ("c2", "c3"), ("c3", "c0"), ("c0", "x"), ("c1", "x")]
    two_col = any(all(col[a] != col[b] for a, b in edges) for col in (dict(zip(verts, bits)) for bits in itertools.product((0, 1), repeat=5)))
    print(f"[Z^3] sites in the box [-2, 3]^3 adjacent to two corners of a plaquette, three orientations: "
          f"{sum(len(v) for v in worst.values())} (none: {none}); the runner's Q4(a) graph has a proper 2-colouring (every induced subgraph of "
          f"Z^3 has one, by the parity of x_1 + x_2 + x_3): {two_col}")
    # ---- the stated values through the product form, on the triangle graph
    triples = [(3, 1, 2), (5, 2, 4), (2, 1, 2)]
    got = []
    for (p, q, r) in triples:
        P2 = phi_mat(p, q, r).dot(phi_mat(p, q, r))
        got.append(tv_plaquette(p, q, r, lambda v, P2=P2: P2[v[0], v[1]]))
    same = got == stated
    # ---- Z^3-realizable windows: the stacked bridge over edge c0-c1 and the cube's top face
    bridge = []
    for (p, q, r) in triples:
        P3 = phi_mat(p, q, r).dot(phi_mat(p, q, r)).dot(phi_mat(p, q, r))
        bridge.append(tv_plaquette(p, q, r, lambda v, P3=P3: P3[v[0], v[1]]))
    P = phi_mat(3, 1, 2)

    def top(v):
        M = np.identity(6, dtype=object)
        for k in range(4):
            M = M.dot(np.diag([P[v[k], u] for u in range(6)]).dot(P))
        return sum(M[u, u] for u in range(6))

    cube = tv_plaquette(3, 1, 2, top)
    sites_b = {"c0": (0, 0, 0), "c1": (1, 0, 0), "c2": (1, 1, 0), "c3": (0, 1, 0), "x": (0, 0, 1), "y": (1, 0, 1)}
    ind = sorted(tuple(sorted((a, b))) for a, b in itertools.combinations(sites_b, 2) if adj(sites_b[a], sites_b[b]))
    want = sorted(tuple(sorted(e)) for e in [("c0", "c1"), ("c1", "c2"), ("c2", "c3"), ("c3", "c0"), ("c0", "x"), ("x", "y"), ("y", "c1")])
    print(f"[values] product-form TV on the triangle graph at (3,1,2), (5,2,4), (2,1,2): {[str(x) for x in got]}; equal to Q4(a)'s stated values: "
          f"{same}; the Z^3 bridge x = (0,0,1), y = (1,0,1) over the edge c0-c1 (its induced Z^3 graph is the four-cycle plus c0-x, x-y, y-c1: "
          f"{ind == want}): TV = {[str(x) for x in bridge]} = {[f'{float(x):.6f}' for x in bridge]}; the cube with its top face unrecorded at "
          f"(3,1,2): {cube} (stated {cube_stated}: {cube == cube_stated})")
    hits = []
    if setting and none and not two_col and same:
        hits.append(f"Q4(a)'s configuration is not a window of the declared setting: no site of Z^3 is adjacent to two corners of a plaquette "
                    f"(exhaustive search, three orientations), the runner's Q4(a) graph (four-cycle plus c0-x, c1-x with c0 ~ c1) contains the "
                    f"triangle c0-c1-x and has no parity 2-colouring, and the stated values {', '.join(str(x) for x in stated)} are exactly that "
                    f"triangle graph's (recomputed through Q1's product form)")
    for h in hits:
        print("HIT: confirmed - " + h)
    print(f"SUMMARY: {'confirmed' if hits else 'not reproduced'} - Q4(a) is a non-Z^3 graph in a note whose sites are declared as the Z^3 "
          f"nearest-neighbour graph; the qualitative conclusion it illustrates survives on Z^3 windows: the cube witness Q4(b) recomputes to the "
          f"stated {cube} and the two-site bridge over an edge gives TV = {float(bridge[0]):.6f}, {float(bridge[1]):.6f}, {float(bridge[2]):.6f} at "
          f"(3,1,2), (5,2,4), (2,1,2)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
