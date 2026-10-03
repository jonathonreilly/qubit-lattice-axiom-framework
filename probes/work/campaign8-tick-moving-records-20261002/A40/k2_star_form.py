"""A40 k2: where does A25's (h,pi) form keep content, and is every term inside one star?
Reuses A25's builder stag2.build (supplied linear toy).  Z^3 site of a component with offset o in
cell x is y = 2x + o (side 2L, periodic).  Checks:
 (a) each curl row (a C component at an odd site y) touches only h at even sites within Manhattan 1 of y;
 (b) Vp = 1/2 Curl^T J Curl equals the sum over odd sites y of 1/2 Curl_y^T J_y Curl_y, each term
     supported on star(y) minus y itself ('hollow star'); no h, p content sits on odd sites;
 (c) Mp (kinetic) is on-site;
 (d) role distances: min Manhattan distance between role classes, and which roles occur in each star.
"""
import sys, signal, itertools
import numpy as np, scipy.sparse as sp
signal.alarm(28)
sys.path.insert(0, '/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A25')
import stag2 as S

L = 4
ops = S.build(L)
lat = ops['lat']; n = lat.n; N2 = 2 * L
def site(off, cell):
    return tuple((2 * lat.coords[cell][k] + off[k]) % N2 for k in range(3))
def mdist(a, b):
    return sum(min((a[k] - b[k]) % N2, (b[k] - a[k]) % N2) for k in range(3))
hpos = [site(S.H_OFF[c], x) for c in range(6) for x in range(n)]
cpos = [site(S.C_OFF[c], x) for c in range(9) for x in range(n)]
par = lambda y: sum(y) % 2
print("h/p components on even sites only:", all(par(y) == 0 for y in hpos))
print("C components on odd sites only   :", all(par(y) == 1 for y in cpos))
Cu = ops['Curl'].tocoo()
print("(a) max Manhattan distance curl row (odd site) -> h input:",
      max(mdist(cpos[i], hpos[j]) for i, j in zip(Cu.row, Cu.col)),
      "; inputs at the odd site itself:", sum(cpos[i] == hpos[j] for i, j in zip(Cu.row, Cu.col)))
# (b) star decomposition of the potential
Curl = ops['Curl'].tocsr(); J = ops['J'].tocsr()
odd_sites = sorted(set(cpos))
rows_at = {y: [i for i, p in enumerate(cpos) if p == y] for y in odd_sites}
Vsum = sp.csr_matrix((6 * n, 6 * n))
worst = 0; hollow_ok = True
for y, rows in rows_at.items():
    Cy = Curl[rows, :]
    Jy = J[rows, :][:, rows]
    Ty = (0.5 * Cy.T @ Jy @ Cy).tocoo()
    Vsum = Vsum + Ty
    for i, j in zip(Ty.row, Ty.col):
        worst = max(worst, mdist(hpos[i], y), mdist(hpos[j], y))
        if hpos[i] == y or hpos[j] == y:
            hollow_ok = False
diff = abs(Vsum - ops['Vp']).max()
print("(b) |sum_y star term - Vp| =", diff, "; max distance of a star term's support from its centre:", worst,
      "; centre content never used:", hollow_ok, "; number of odd centres:", len(odd_sites))
Vc = ops['Vp'].tocoo()
print("    Vp couples even sites at Manhattan distances:",
      sorted(set(mdist(hpos[i], hpos[j]) for i, j in zip(Vc.row, Vc.col))))
Mc = ops['Mp'].tocoo()
print("(c) kinetic term max Manhattan distance:", max(mdist(hpos[i], hpos[j]) for i, j in zip(Mc.row, Mc.col)))
Rc = ops['R'].tocoo()
vpos = [site(S.VERT_OFF[0], x) for x in range(n)]
print("    Hamiltonian row (lapse) sits on role V; it reads h within Manhattan",
      max(mdist(vpos[i], hpos[j]) for i, j in zip(Rc.row, Rc.col)))
# (d) role geometry on Z^3 (layout s = 0)
def role(r):
    w = sum(r)
    return {0: 'V', 1: 'E', 2: 'F', 3: 'C'}[w] + ('' if w in (0, 3) else 'xyz'[r.index(1 if w == 1 else 0)])
cls = list(itertools.product((0, 1), repeat=3))
print("(d) min Manhattan distance between role classes (Z^3, layout s=0):")
names = [role(r) for r in cls]
for a in cls:
    row = []
    for b in cls:
        dmin = min(sum(abs(b[k] + 2 * t[k] - a[k]) for k in range(3)) if b != a or any(t) else 99
                   for t in itertools.product((-1, 0, 1), repeat=3))
        row.append(dmin)
    print("   ", role(a).ljust(3), dict(zip(names, row)))
nb = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
for a in cls:
    print("    star of", role(a).ljust(3), "holds neighbours of roles",
          sorted(role(tuple((a[k] + d[k]) % 2 for k in range(3))) for d in nb))
