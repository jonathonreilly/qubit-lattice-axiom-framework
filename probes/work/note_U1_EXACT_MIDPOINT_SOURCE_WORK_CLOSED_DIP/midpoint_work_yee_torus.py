"""Independent exact check of the U1 exact-midpoint source-work note on periodic cubic tori beyond L=3.

Own construction of the Yee incidence (edges, faces, cubes) on an L^3 torus; exact Fractions throughout.
  (1) midpoint work law  dH = h J.(E+E')/2  for the sourced tick, random exact data, several h (in and beyond the CFL range), L = 4, 5, 6
  (2) closed unit dipole: charges, E2/B2 formulae, Gauss laws, no harmonic part, exact energy, work ledger, reversal, control
  (3) source-free exact energy conservation and support growth on L = 32 for 12 cycles with sparse exact rationals
"""
import sys, itertools, random, time
from fractions import Fraction as Fr

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")

class Torus:
    def __init__(self, L):
        self.L = L
        self.sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
        self.sid = {s: n for n, s in enumerate(self.sites)}
        self.ne = 3 * len(self.sites)
        # edge (s, a) index = 3*sid + a ; face (s, n) index = 3*sid + n, face spans axes (b, c) = cyclic successors of n
        self.face_edges = []   # per face: [(edge, sign)] counterclockwise
        for s in self.sites:
            for n in range(3):
                b, c = (n + 1) % 3, (n + 2) % 3
                self.face_edges.append([(self.e(s, b), 1), (self.e(self.sh(s, b), c), 1), (self.e(self.sh(s, c), b), -1), (self.e(s, c), -1)])
        self.edge_faces = [[] for _ in range(self.ne)]
        for f, lst in enumerate(self.face_edges):
            for e, sg in lst: self.edge_faces[e].append((f, sg))
        self.edge_ends = []    # (tail vertex, head vertex)
        for s in self.sites:
            for a in range(3): self.edge_ends.append((self.sid[s], self.sid[self.sh(s, a)]))
        # cubes: cube at s has 6 faces with outward signs
        self.cube_faces = []
        for s in self.sites:
            lst = []
            for n in range(3):
                lst.append((self.f(s, n), -1)); lst.append((self.f(self.sh(s, n), n), 1))
            self.cube_faces.append(lst)
    def sh(self, s, a, d=1):
        t = list(s); t[a] = (t[a] + d) % self.L; return tuple(t)
    def e(self, s, a): return 3 * self.sid[s] + a
    def f(self, s, n): return 3 * self.sid[s] + n
    def curl(self, E):        # faces <- edges
        return [sum(sg * E[e] for e, sg in lst) for lst in self.face_edges]
    def curlT(self, B):       # edges <- faces
        out = [Fr(0)] * self.ne
        for f, lst in enumerate(self.face_edges):
            if B[f]:
                for e, sg in lst: out[e] += sg * B[f]
        return out
    def div0T(self, J):       # vertices <- edges: head +, tail -
        out = [Fr(0)] * len(self.sites)
        for e, (t, h) in enumerate(self.edge_ends):
            out[h] += J[e]; out[t] -= J[e]
        return out
    def div2(self, B):        # cubes <- faces
        return [sum(sg * B[f] for f, sg in lst) for lst in self.cube_faces]

def vadd(a, b, k=1): return [x + k * y for x, y in zip(a, b)]
def vsc(a, k): return [k * x for x in a]
def dot(a, b): return sum(x * y for x, y in zip(a, b))

def tick(T, E, B, h, J):
    B1 = vadd(B, T.curl(E), h / 2)
    E2 = vadd(vadd(E, T.curlT(B1), -h), J, h)
    B2 = vadd(B1, T.curl(E2), h / 2)
    return E2, B2
def energy(T, E, B, h):
    cE = T.curl(E)
    return Fr(1, 2) * (dot(E, E) + dot(B, B)) - h * h / 8 * dot(cE, cE)

# ---------- structural checks of my incidence ----------
T3 = Torus(3)
check("L=3 block has 81 edges + 81 faces = 162 fields", T3.ne == 81 and len(T3.face_edges) == 81)
for L in (4, 5, 6):
    T = Torus(L)
    random.seed(L)
    Ev = [Fr(random.randint(-9, 9)) for _ in range(T.ne)]
    check(f"L={L}: cube divergence of curl vanishes on random edge data (complex property)", all(v == 0 for v in T.div2(T.curl(Ev))))
    Jv = [Fr(random.randint(-9, 9)) for _ in range(T.ne)]
    Gc = [Fr(random.randint(-9, 9)) for _ in range(len(T.sites))]
    # gradient of a vertex potential is curl-free
    grad = [Gc[hd] - Gc[tl] for tl, hd in T.edge_ends]
    check(f"L={L}: curl of a gradient vanishes", all(v == 0 for v in T.curl(grad)))
    # divergence pairing: <d0^T J, phi> = <J, grad phi>
    check(f"L={L}: vertex divergence is the adjoint of the gradient", dot(T.div0T(Jv), Gc) == dot(Jv, grad))

# ---------- (1) midpoint work law ----------
hs = [Fr(1, 2), Fr(1, 3), Fr(2, 5), Fr(3, 7), Fr(1), Fr(5, 4)]
for L in (4, 5, 6):
    T = Torus(L); random.seed(100 + L); bad = 0; cnt = 0; jz = 0
    for h in hs:
        for trial in range(3):
            E = [Fr(random.randint(-20, 20), random.randint(1, 7)) for _ in range(T.ne)]
            B = [Fr(random.randint(-20, 20), random.randint(1, 7)) for _ in range(T.ne)]
            J = [Fr(random.randint(-20, 20), random.randint(1, 7)) for _ in range(T.ne)]
            E2, B2 = tick(T, E, B, h, J)
            lhs = energy(T, E2, B2, h) - energy(T, E, B, h)
            rhs = h * dot(J, vadd(E, E2)) / 2
            cnt += 1; bad += (lhs != rhs)
            # J = 0: exact conservation
            E0, B0 = tick(T, E, B, h, [Fr(0)] * T.ne)
            jz += (energy(T, E0, B0, h) != energy(T, E, B, h))
    check(f"L={L}: dH = h J.(E+E')/2 exactly for {cnt} random rational states across h in {{1/2,1/3,2/5,3/7,1,5/4}}", bad == 0)
    check(f"L={L}: source-free tick conserves H_h exactly for the same states", jz == 0)

# largest eigenvalue of C^T C on L=4, 6 (dense power iteration in exact arithmetic is overkill; use the plane-wave symbol check instead)
import numpy as np
for L in (4, 6):
    T = Torus(L)
    C = np.zeros((len(T.face_edges), T.ne))
    for f, lst in enumerate(T.face_edges):
        for e, sg in lst: C[f, e] += sg
    lam = np.linalg.eigvalsh(C.T @ C)
    check(f"L={L}: largest eigenvalue of C^T C is 12, so M_E = I - (h/2)^2 C^T C is positive exactly for h < 2/sqrt(12)=0.5774", abs(lam.max() - 12) < 1e-9, f"lam_max={lam.max():.12f} ; at h=1/2 the smallest eigenvalue of M_E is {1 - lam.max()/16:.4f}")

# ---------- (2) closed unit dipole ----------
def dipole_run(T, e0, h):
    J1 = [Fr(0)] * T.ne; J1[e0] = 1 / h
    J2 = vsc(J1, -1)
    zero = [Fr(0)] * T.ne
    E1, B1 = tick(T, zero, zero, h, J1)
    rho1 = vsc(T.div0T(J1), h)
    E2, B2 = tick(T, E1, B1, h, J2)
    rho2 = vadd(rho1, vsc(T.div0T(J2), h))
    work1 = h * dot(J1, vadd(zero, E1)) / 2
    work2 = h * dot(J2, vadd(E1, E2)) / 2
    return J1, J2, E1, B1, E2, B2, rho1, rho2, work1, work2
for L in (4, 5, 6):
    T = Torus(L)
    for axis in range(3):
        s0 = (1 % L, 2 % L, 0); e0 = T.e(s0, axis)
        allok = {}
        for h in (Fr(1, 2), Fr(1, 3), Fr(2, 5), Fr(1, 4)):
            J1, J2, E1, B1, E2, B2, rho1, rho2, w1, w2 = dipole_run(T, e0, h)
            tail, head = T.edge_ends[e0]
            ok1 = rho1[tail] == -1 and rho1[head] == 1 and sum(1 for v in rho1 if v != 0) == 2
            ok2 = all(v == 0 for v in rho2)
            cJ = T.curl(J1)
            CtC = T.curlT(cJ)
            Ef = vsc(CtC, -h ** 3)
            Bf = vadd(vsc(cJ, h * h), T.curl(CtC), -(h ** 4) / 2)
            okform = (E2 == Ef and B2 == Bf)
            gauss = all(v == 0 for v in T.div0T(E2)) and all(v == 0 for v in T.div2(B2))
            groupsE = [sum(E2[3 * n + a] for n in range(len(T.sites))) for a in range(3)]
            groupsB = [sum(B2[3 * n + a] for n in range(len(T.sites))) for a in range(3)]
            noharm = all(v == 0 for v in groupsE + groupsB)
            H2 = energy(T, E2, B2, h)
            okE = (H2 == w1 + w2) and H2 > 0
            allok[h] = (ok1, ok2, okform, gauss, noharm, okE, H2)
        for name, k in (("first pulse makes only the unit neighbour dipole", 0), ("second pulse returns every vertex charge to zero", 1), ("two-step fields equal the curl / co-curl formulae", 2), ("both Gauss laws hold on the residual", 3), ("no constant (harmonic) part in any of the six groups", 4), ("residual energy is positive and equals the accumulated midpoint work", 5)):
            check(f"L={L} edge axis {axis}: {name} for h in (1/2,1/3,2/5,1/4)", all(v[k] for v in allok.values()))
        check(f"L={L} edge axis {axis}: residual energy is exactly 2 h^2 for J=1/h at every h tried (the note's 1/2 is the h=1/2 case)", all(v[6] == 2 * h * h for h, v in allok.items()))
        if axis == 0:
            print("   residual energy H_2 by h:", {str(h): str(v[6]) for h, v in allok.items()})
    # control and reversal (once per L)
    h = Fr(1, 2); e0 = T.e((0, 1, 2 % L), 1)
    Jp = [Fr(0)] * T.ne; Jp[e0] = 1 / h
    zero = [Fr(0)] * T.ne
    Ec, Bc = tick(T, zero, zero, h, zero)
    Es, Bs = tick(T, zero, zero, h, vadd(Jp, vsc(Jp, -1)))
    check(f"L={L}: simultaneous +J and -J (zero net current) leaves zero field", all(v == 0 for v in Es + Bs))
    E1, B1 = tick(T, zero, zero, h, Jp)
    E2, B2 = tick(T, E1, B1, h, vsc(Jp, -1))
    # reversal: apply -h with the source values in reverse time order
    Er, Br = tick(T, E2, B2, -h, vsc(Jp, -1))
    Er, Br = tick(T, Er, Br, -h, Jp)
    check(f"L={L}: reversed history with -h and reversed source order returns exactly to the vacuum", all(v == 0 for v in Er + Br))
    # pulse orientation reversal negates fields, preserves energy
    Ea, Ba = tick(T, *tick(T, zero, zero, h, Jp), h, vsc(Jp, -1))
    Eb, Bb = tick(T, *tick(T, zero, zero, h, vsc(Jp, -1)), h, Jp)
    check(f"L={L}: reversing pulse orientation reverses every field component and preserves the energy", Eb == vsc(Ea, -1) and Bb == vsc(Ba, -1) and energy(T, Ea, Ba, h) == energy(T, Eb, Bb, h))

# ---------- (3) source-free propagation, exact and sparse, L=32 ----------
L = 32; h = Fr(1, 2)
T = Torus(L)
def sparse_curl(Ed):
    out = {}
    for e, v in Ed.items():
        for f, sg in T.edge_faces[e]:
            out[f] = out.get(f, 0) + sg * v
    return {k: v for k, v in out.items() if v}
def sparse_curlT(Bd):
    out = {}
    for f, v in Bd.items():
        for e, sg in T.face_edges[f]:
            out[e] = out.get(e, 0) + sg * v
    return {k: v for k, v in out.items() if v}
def sadd(a, b, k):
    out = dict(a)
    for key, v in b.items():
        nv = out.get(key, 0) + k * v
        if nv: out[key] = nv
        else: out.pop(key, None)
    return out
def stick(Ed, Bd, J):
    B1 = sadd(Bd, sparse_curl(Ed), h / 2)
    E1 = sadd(sadd(Ed, sparse_curlT(B1), -h), J, h)
    B2 = sadd(B1, sparse_curl(E1), h / 2)
    return E1, B2
def senergy(Ed, Bd):
    cE = sparse_curl(Ed)
    return Fr(1, 2) * (sum(v * v for v in Ed.values()) + sum(v * v for v in Bd.values())) - h * h / 8 * sum(v * v for v in cE.values())
e0 = T.e((0, 0, 0), 0)       # source edge from (0,0,0) to (1,0,0); centre (1,0,0) in doubled coordinates
def dcenter_edge(e):
    n, a = divmod(e, 3); s = T.sites[n]; c = [2 * s[0], 2 * s[1], 2 * s[2]]; c[a] += 1; return c
def dcenter_face(f):
    n, a = divmod(f, 3); s = T.sites[n]; c = [2 * s[0], 2 * s[1], 2 * s[2]]; c[(a + 1) % 3] += 1; c[(a + 2) % 3] += 1; return c
src = dcenter_edge(e0)
def dist(c):
    return sum(min((c[i] - src[i]) % (2 * L), (src[i] - c[i]) % (2 * L)) for i in range(3))
def radius_stats(Ed, Bd, cut):
    r = max([dist(dcenter_edge(e)) for e in Ed] + [dist(dcenter_face(f)) for f in Bd])
    tot = sum(v * v for v in Ed.values()) + sum(v * v for v in Bd.values())
    inside = sum(v * v for e, v in Ed.items() if dist(dcenter_edge(e)) <= cut) + sum(v * v for f, v in Bd.items() if dist(dcenter_face(f)) <= cut)
    mean_r = (sum(v * v * dist(dcenter_edge(e)) for e, v in Ed.items()) + sum(v * v * dist(dcenter_face(f)) for f, v in Bd.items())) / tot
    return r, float(inside / tot), float(mean_r)
E, B = stick({}, {}, {e0: 1 / h})
E, B = stick(E, B, {e0: -1 / h})
H0 = senergy(E, B)
print("packet after the two source ticks: energy", H0, "; nonzero entries", len(E), len(B))
check("packet energy is exactly 1/2 on L=32", H0 == Fr(1, 2))
radii = []; frac3 = []; frac6 = []; mean_r = []; ok_energy = True; t0 = time.time()
def record(E, B):
    r, f3, m = radius_stats(E, B, 3); _, f6, _ = radius_stats(E, B, 6)
    radii.append(r); frac3.append(f3); frac6.append(f6); mean_r.append(m)
record(E, B)
NCYC = 12
for cyc in range(NCYC):
    E, B = stick(E, B, {})
    ok_energy &= (senergy(E, B) == H0)
    record(E, B)
print(f"support radius (doubled-coordinate Manhattan from the source-edge centre) by cycle: {radii}   ({time.time()-t0:.0f}s)")
print("squared-amplitude-weighted mean radius by cycle:", [round(v, 3) for v in mean_r])
print("fraction of squared amplitude within doubled radius 3:", [round(v, 5) for v in frac3])
print("fraction of squared amplitude within doubled radius 6:", [round(v, 5) for v in frac6])
check("energy stays exactly 1/2 (exact rational, no tolerance) through 12 source-free cycles on L=32", ok_energy)
check("support radius starts at 3 and grows by exactly 2 per cycle (3,5,...,27)", radii == [3 + 2 * k for k in range(NCYC + 1)])
check("squared-amplitude mean radius rises strictly over the note's eight cycles", all(a < b for a, b in zip(mean_r[:9], mean_r[1:9])))
check("squared-amplitude mean radius keeps rising strictly through cycle 12 (beyond the note's cycles)", all(a < b for a, b in zip(mean_r, mean_r[1:])))
check("after 8 cycles less than 0.2% of squared amplitude is within doubled radius 3", frac3[8] < 0.002, f"{frac3[8]:.5f}")
rebound = max(frac3[9:])
print(f"extension (informational, not a note claim): the near-source fraction is not monotone: minimum {min(frac3[8:]):.5f} at cycle {8 + int(np.argmin(frac3[8:]))}, back up to {rebound:.5f} by cycle {9 + int(np.argmax(frac3[9:]))}; the 0.2% figure holds at cycle 8 and 9 only")
check("the 0.2% near-source figure is a snapshot: it is exceeded again after cycle 9 (measured, reported not asserted as a defect)", rebound > 0.002)

if FAIL == 0:
    print(f"SUMMARY: no falsifier fires: midpoint work law exact on L=4,5,6 tori for random states and six values of h; closed dipole, formulae, Gauss laws, energy = accumulated work, reversal and controls exact; L=32 packet energy exactly 1/2 for 12 cycles with support radius 3..27 and residual energy 2h^2 for J=1/h at four values of h; the near-source fraction below 0.2% is a snapshot at cycles 8-9 (rebounds to about 0.8% by cycle 11); {PASS} checks pass")
else:
    print(f"SUMMARY: {FAIL} of my own checks failed; see the [FAIL] lines above")
sys.exit(0)
