# al55_nec.py -- exact check of Lemma DW, Lemma LC, Proposition NEC (ALIGN55.md section 3).
# Criteria: checks/al55_nec_criteria.md (written first). Fractions/ints only. stdout only.
from fractions import Fraction as F
import random
from collections import deque

random.seed(5501)
D = 2          # dimension of the model
L = 3          # blocking factor
N0 = 18        # level-0 torus side (T = 2, k = 2)
OFF = {0: 0, 1: 1, 2: 4}      # level-l sites: coordinates = OFF[l] mod 3**l
STEP = {0: 1, 1: 3, 2: 9}

results = []
def rep(name, ok, info=""):
    results.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name + ((" | " + info) if info else ""))
def ctl(name, fired, info=""):
    results.append((name, fired))
    print(("CONTROL FIRES " if fired else "CONTROL DOES NOT FIRE ") + name + ((" | " + info) if info else ""))

# ---------- su(2) = R^3 vectors and rational SO(3) ----------
Z3 = (F(0), F(0), F(0))
def vadd(a, b): return (a[0]+b[0], a[1]+b[1], a[2]+b[2])
def vsub(a, b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def vsc(c, a): return (c*a[0], c*a[1], c*a[2])
def vdot(a, b): return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
def mv(M, v): return tuple(M[i][0]*v[0] + M[i][1]*v[1] + M[i][2]*v[2] for i in range(3))
def mT(M): return tuple(tuple(M[j][i] for j in range(3)) for i in range(3))
def mm(A, B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def quat_rot(a, b, c, d):
    n = F(a*a + b*b + c*c + d*d)
    return ((F(a*a+b*b-c*c-d*d)/n, F(2*(b*c-a*d))/n, F(2*(b*d+a*c))/n),
            (F(2*(b*c+a*d))/n, F(a*a-b*b+c*c-d*d)/n, F(2*(c*d-a*b))/n),
            (F(2*(b*d-a*c))/n, F(2*(c*d+a*b))/n, F(a*a-b*b-c*c+d*d)/n))
I3 = ((F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1)))
def rand_rot(big=8):
    return quat_rot(big, random.randint(-2, 2), random.randint(-2, 2), random.randint(-2, 2))
def rand_vec(r=5):
    return (F(random.randint(-r, r)), F(random.randint(-r, r)), F(random.randint(-r, r)))

# ---------- lattices ----------
def sites(l):
    s = STEP[l]; o = OFF[l]
    return [((o + s*i) % N0, (o + s*j) % N0) for i in range(N0 // s) for j in range(N0 // s)]
def shift(y, mu, n):
    z = list(y); z[mu] = (z[mu] + n) % N0; return tuple(z)
def links(l):
    return [(y, mu) for y in sites(l) for mu in range(D)]
def head(b, l): return shift(b[0], b[1], STEP[l])
SITES = {l: sites(l) for l in (0, 1, 2)}
ROOTS = set(SITES[2])
LINKS = {l: links(l) for l in (0, 1, 2)}

def d_flat(lam, l):          # lam: dict site->vec (level-l sites)
    return {b: vsub(lam[head(b, l)], lam[b[0]]) for b in LINKS[l]}
def dT_flat(j, l):           # adjoint of d_flat: charges on level-l sites
    q = {y: Z3 for y in SITES[l]}
    for b, v in j.items():
        q[head(b, l)] = vadd(q[head(b, l)], v)
        q[b[0]] = vsub(q[b[0]], v)
    return q
def restrict(lam, l): return {y: lam[y] for y in SITES[l]}
def Xi1(nu):                 # chain gradient of a level-0 function: levels 0 and 1 (k = 2)
    return {0: d_flat(nu, 0), 1: d_flat(restrict(nu, 1), 1)}
def pair_links(a, b): return sum((vdot(a[k], b[k]) for k in a if k in b), F(0))

# ---------- background (pure gauge) ----------
Gs = {y: rand_rot() for y in SITES[0]}
def AdZ_pg(b, l):            # Ad of Z_l(b) = G(tail) G(head)^-1
    return mm(Gs[b[0]], mT(Gs[head(b, l)]))

# ---------- A1/A2: line current (Lemma LC) ----------
y0 = (4, 1)
assert y0 in SITES[1] and y0 not in ROOTS
line_sites = [((1 + 3*i) % N0, 1) for i in range(N0 // 3)]
line_links = [(y, 0) for y in line_sites]              # b_i from y_i to y_{i+1}
def line_current(AdZ, v):
    j = {}; cur = v
    for i, b in enumerate(line_links):
        j[b] = cur
        cur = mv(mT(AdZ(b, 1)), cur)                     # Ad^{-1} = Ad^T
    return j
def cov_charge(j, AdZ, l):
    q = {y: Z3 for y in SITES[l]}
    for b, v in j.items():
        q[head(b, l)] = vadd(q[head(b, l)], mv(mT(AdZ(b, l)), v))
        q[b[0]] = vsub(q[b[0]], v)
    return q
v = rand_vec()
jline = line_current(AdZ_pg, v)
cq = cov_charge(jline, AdZ_pg, 1)
rep("A1 covariant charges of the line current vanish (PG)", all(c == Z3 for c in cq.values()) and
    all(vdot(w, w) == vdot(v, v) for w in jline.values()), "|v|^2=%s" % vdot(v, v))
qflat = dT_flat(jline, 1)
ok2 = True
for i, y in enumerate(line_sites):
    bprev = line_links[i - 1]
    expect = vsub(jline[bprev], mv(mT(AdZ_pg(bprev, 1)), jline[bprev]))
    ok2 = ok2 and (qflat[y] == expect)
ok2 = ok2 and all(qflat[y] == Z3 for y in SITES[1] if y not in line_sites)
rep("A2 flat charges = (1 - Ad^-1)j, q(y0) != 0", ok2 and qflat[y0] != Z3, "q(y0)=%s" % (tuple(str(c) for c in qflat[y0]),))

# ---------- left inverses ----------
def nbr_steps(order):
    return [(order[0], 1), (order[0], -1), (order[1], 1), (order[1], -1)]
def forest(sites_l, roots, l, order, allowed=None):
    par = {r: None for r in roots}; dq = deque(roots)
    sset = set(sites_l) if allowed is None else allowed
    while dq:
        y = dq.popleft()
        for mu, sg in nbr_steps(order):
            z = shift(y, mu, sg*STEP[l])
            if z in sset and z not in par:
                par[z] = (y, mu, sg); dq.append(z)
    return par
def integral_step(x_l, y, mu, sg, l):     # integral of x along the step y -> y + sg*STEP*e_mu
    if sg == 1: return x_l[(y, mu)]
    return vsc(F(-1), x_l[(shift(y, mu, -STEP[l]), mu)])
def solve_forest(x_l, par, l, base):     # lam(z) = lam(parent) - integral(parent -> z)
    lam = dict(base)
    order = sorted(par.keys(), key=lambda z: 0)
    done = set(k for k, p in par.items() if p is None)
    pending = [z for z in par if par[z] is not None]
    while pending:
        nxt = []
        for z in pending:
            y, mu, sg = par[z]
            if y in done:
                lam[z] = vsub(lam[y], integral_step(x_l, y, mu, sg, l)); done.add(z)
            else:
                nxt.append(z)
        pending = nxt
    return lam
PAR_A = forest(SITES[0], sorted(ROOTS), 0, (0, 1))
PAR_B = forest(SITES[0], sorted(ROOTS), 0, (1, 0))
assert len(PAR_A) == len(SITES[0]) and len(PAR_B) == len(SITES[0])
def Lam_A(x): return solve_forest(x[0], PAR_A, 0, {r: Z3 for r in ROOTS})
def Lam_B(x): return solve_forest(x[0], PAR_B, 0, {r: Z3 for r in ROOTS})
PAR_H1 = forest(SITES[1], sorted(ROOTS), 1, (0, 1))
assert len(PAR_H1) == len(SITES[1])
BLOCK = {Y: set(shift(shift(Y, 0, a), 1, b) for a in (-1, 0, 1) for b in (-1, 0, 1)) for Y in SITES[1]}
PAR_HB = {Y: forest(None, [Y], 0, (0, 1), allowed=BLOCK[Y]) for Y in SITES[1]}
def Lam_H(x):
    lam1 = solve_forest(x[1], PAR_H1, 1, {r: Z3 for r in ROOTS})
    lam = {}
    for Y in SITES[1]:
        part = solve_forest(x[0], PAR_HB[Y], 0, {Y: lam1[Y]})
        lam.update(part)
    return lam

def rand_Lambda0():
    nu = {y: rand_vec() for y in SITES[0]}
    for r in ROOTS: nu[r] = Z3
    return nu
ok3 = True
for _ in range(3):
    nu = rand_Lambda0(); x = Xi1(nu); mnu = {y: vsc(F(-1), nu[y]) for y in nu}
    for Lam in (Lam_A, Lam_B, Lam_H):
        ok3 = ok3 and (Lam(x) == mnu)
rep("A3 Lambda_A, Lambda_B, Lambda_H are left inverses of -Xi_1 (3 random nu)", ok3)

# ---------- A4-A6 ----------
vp = rand_vec()
phi = {y: Z3 for y in SITES[0]}; phi[y0] = vp
xphi = {0: d_flat(phi, 0), 1: {b: Z3 for b in LINKS[1]}}
mphi = {y: vsc(F(-1), phi[y]) for y in phi}
rep("A4 Lambda_A x^phi = -phi and Lambda_B x^phi = -phi", Lam_A(xphi) == mphi and Lam_B(xphi) == mphi)
def PiT_S_at(Lam):
    lam = Lam(xphi)
    moved1 = d_flat(restrict(lam, 1), 1)            # level-1 component of Xi_1 lam; x^phi_1 = 0
    return pair_links(jline, moved1)
target = -vdot(qflat[y0], vp)
vA, vB, vH = PiT_S_at(Lam_A), PiT_S_at(Lam_B), PiT_S_at(Lam_H)
rep("A5 (Pi^T S)(x^phi) = -<q(y0), v'> for Lambda_A, Lambda_B, and != 0", vA == target and vB == target and target != 0,
    "value=%s" % target)
rep("A6 hierarchical Lambda_H gives (Pi^T S)(x^phi) = 0", vH == 0)

# ---------- Q_l (linearised S4' map) and A7 ----------
def axial_path_steps(c, y, order, l):   # list of (site, mu, sg) steps from c to y (displacements in {-1,0,1} block steps)
    steps = []; cur = c
    for mu in order:
        dlt = ((y[mu] - cur[mu] + N0 // 2) % N0) - N0 // 2
        n = dlt // STEP[l]
        sg = 1 if n > 0 else -1
        for _ in range(abs(n)):
            steps.append((cur, mu, sg)); cur = shift(cur, mu, sg*STEP[l])
    assert cur == y
    return steps
def path_int(x_l, steps, l):
    tot = Z3
    for (y, mu, sg) in steps: tot = vadd(tot, integral_step(x_l, y, mu, sg, l))
    return tot
def blk(X, l):   # level-l sites in the block of level-(l+1) site X
    s = STEP[l]
    return [shift(shift(X, 0, a*s), 1, b*s) for a in (-1, 0, 1) for b in (-1, 0, 1)]
def Q(x_l, l):   # level l -> level l+1 links
    out = {}
    for (X, mu) in LINKS[l+1]:
        Xn = head((X, mu), l+1)
        tot = Z3
        for order in ((0, 1), (1, 0)):
            for y in blk(X, l):
                yL = shift(y, mu, STEP[l+1])
                t = path_int(x_l, axial_path_steps(X, y, order, l), l)
                t = vadd(t, path_int(x_l, [(shift(y, mu, i*STEP[l]), mu, 1) for i in range(L)], l))
                t = vsub(t, path_int(x_l, axial_path_steps(Xn, yL, order, l), l))
                tot = vadd(tot, t)
        out[(X, mu)] = vsc(F(1, 2*9), tot)
    return out
devphi = d_flat(restrict(phi, 1), 1)
Q0dphi = Q(xphi[0], 0)
rep("A7a Q_0 d phi = d ev^(1) phi (contour definition)", Q0dphi == devphi)
def plaq(x_l, l):
    s = STEP[l]
    return {y: vsub(vadd(x_l[(y, 0)], x_l[(shift(y, 0, s), 1)]), vadd(x_l[(shift(y, 1, s), 0)], x_l[(y, 1)])) for y in SITES[l]}
def residual(x, l):          # r_l(x) = Q_l x_l - x_{l+1}; x_2 = 0
    Qx = Q(x[l], l)
    if l + 1 <= 1:
        return {b: vsub(Qx[b], x[l+1][b]) for b in Qx}
    return Qx
r0 = residual(xphi, 0); r1 = residual(xphi, 1)
ok7 = True; mism5 = False
for _ in range(5):
    G0 = {y: rand_vec() for y in SITES[0]}; G1 = {y: rand_vec() for y in SITES[1]}
    j0 = {b: rand_vec() for b in LINKS[0]}; j1 = {b: rand_vec() for b in LINKS[1]}
    s0 = {b: rand_vec() for b in LINKS[1]}; s1 = {b: rand_vec() for b in LINKS[2]}
    full = (sum((vdot(G0[y], p) for y, p in plaq(xphi[0], 0).items()), F(0))
            + sum((vdot(G1[y], p) for y, p in plaq(xphi[1], 1).items()), F(0))
            + pair_links(j0, xphi[0]) + pair_links(j1, xphi[1])
            + pair_links(s0, r0) + pair_links(s1, r1))
    two = pair_links(j0, xphi[0]) + pair_links(s0, devphi)
    ok7 = ok7 and (full == two)
    if pair_links(j0, xphi[0]) != full: mism5 = True
rep("A7b full pairing y(x^phi) = <j_0, d phi> + <s_0, d ev phi> (5 random representations)", ok7)

# ---------- A8 hierarchy of Lambda_H ----------
xr = {0: {b: rand_vec() for b in LINKS[0]}, 1: {b: rand_vec() for b in LINKS[1]}}
base1 = restrict(Lam_H(xr), 1)
xr0 = {0: {b: vadd(xr[0][b], rand_vec()) for b in LINKS[0]}, 1: xr[1]}
xr1 = {0: xr[0], 1: {b: vadd(xr[1][b], rand_vec()) for b in LINKS[1]}}
rep("A8 ev^(1) Lambda_H x independent of x_0, dependent on x_1",
    restrict(Lam_H(xr0), 1) == base1 and restrict(Lam_H(xr1), 1) != base1)

# ---------- controls ----------
CVrot = {b: rand_rot() for b in LINKS[1]}
def AdZ_cv(b, l): return CVrot[b]
jcv = line_current(AdZ_cv, rand_vec())
ctl("C1 curved line holonomy, generic v: covariant charge at y_1 != 0", cov_charge(jcv, AdZ_cv, 1)[line_sites[0]] != Z3)
nu = rand_Lambda0(); x = Xi1(nu)
twoA = {y: vsc(F(2), w) for y, w in Lam_A(x).items()}
ctl("C2 2*Lambda_A is not a left inverse", twoA != {y: vsc(F(-1), nu[y]) for y in nu})
ctl("C3 Lambda_A is not hierarchical: ev^(1) Lambda_A x^phi != 0", any(w != Z3 for w in restrict(Lam_A(xphi), 1).values()))
yr = sorted(ROOTS)[0]
phir = {y: Z3 for y in SITES[0]}; phir[yr] = vp
xphir = {0: d_flat(phir, 0), 1: {b: Z3 for b in LINKS[1]}}
ctl("C4 at a level-2 root, Lambda_A x^phi != -phi", Lam_A(xphir) != {y: vsc(F(-1), phir[y]) for y in phir})
ctl("C5 dropping the s_0 term mismatches", mism5)

# informational: Lambda_A and Lambda_B differ as maps
xi = {0: {b: rand_vec() for b in LINKS[0]}, 1: {b: Z3 for b in LINKS[1]}}
print("INFO Lambda_A != Lambda_B on a random non-gradient field:", Lam_A(xi) != Lam_B(xi))

print("SUMMARY: %d items, all ok = %s" % (len(results), all(ok for _, ok in results)))
