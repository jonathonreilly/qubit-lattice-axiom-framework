AUDIT_INPUT_PATHS = ('docs/RULESET_B_MODE_SPLIT_IS_SUPPLIED_AND_ITS_SPIN_AND_FAMILY_READINGS_FAIL_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""minimal-toe-b-tests: hostile checks of the information-minimal ruleset B.

Ruleset B (agents/minimal-toe-b) takes the site modes C^2 (qubit levels) (+) C^3
(owned links), the exterior algebra Lambda(C^5) and the frame group S(U2xU3).
This runner checks, with exact integer/rational arithmetic where it matters:
  1. mode-split forcing: description-cost measures, chirality and anomalies for
     the alternatives (C1+C3, C2+C3, C2xC3, C1+C6, C2+C6, C2+C3+C3, C5 unsplit);
  2. spin vs isospin: commutant of S(U2xU3) on Lambda(C^5); the R2 reading
     (qubit SU(2) = rotations) against measured spin; a separate spin on the
     2^3 cell x qubit (16-dim); axis-labelled transport vs colour SU(3);
  3. families: are the three record-axis sectors new states; which S3 acts;
     is the invariant mass matrix rank 1.
Seeded, no observed number enters except the spin-1/2 of every SM fermion.
"""
AUDIT_TIMEOUT_SEC = 60
from fractions import Fraction as Fr
from itertools import combinations, permutations
from collections import Counter
import numpy as np

RNG = np.random.default_rng(20261022)
P = F = 0
def check(name, ok, info=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))

# ---------------- Part 1: mode-split alternatives ----------------
def mode_weights(kind, blocks):
    """Integer Cartan weights of each one-excitation mode under the frame group."""
    if kind == "sum":                      # S(U(b1) x U(b2) x ...): Cartan = traceless diag
        n = sum(blocks)
        return [tuple(n * (j == i) - 1 for j in range(n)) for i in range(n)]
    a, b = blocks                          # tensor: SU(a) x SU(b) acting on C^a (x) C^b
    def cart(m):                           # Cartan basis of su(m), integer
        return [[(1 if k < r else (-r if k == r else 0)) for k in range(m)] for r in range(1, m)]
    ca, cb = cart(a), cart(b)
    return [tuple([h[i] for h in ca] + [h[j] for h in cb]) for i in range(a) for j in range(b)]

def even_half(w):
    n, r = len(w), len(w[0])
    out = []
    for k in range(0, n + 1, 2):
        for S in combinations(range(n), k):
            out.append(tuple(sum(w[i][c] for i in S) for c in range(r)))
    return out

def analyse(kind, blocks):
    w = mode_weights(kind, blocks); ev = even_half(w); r = len(w[0])
    chiral = Counter(ev) != Counter(tuple(-x for x in v) for v in ev)
    grav = all(sum(v[c] for v in ev) == 0 for c in range(r))
    cubic = all(sum(v[i] * v[j] * v[k] for v in ev) == 0
                for i in range(r) for j in range(i, r) for k in range(j, r))
    return chiral, grav and cubic, len(ev)

def dimG(kind, blocks):
    return sum(b * b for b in blocks) - 1 if kind == "sum" else blocks[0]**2 + blocks[1]**2 - 2

cands = [("C1+C3   qubit=1 mode, owned links", "sum", (1, 3)),
         ("C2+C3   ruleset B", "sum", (2, 3)),
         ("C2xC3   tensor (level,axis)", "ten", (2, 3)),
         ("C1+C6   qubit=1 mode, 6 links", "sum", (1, 6)),
         ("C2+C6   6 oriented links", "sum", (2, 6)),
         ("C2+C3+C3 fwd/back blocks", "sum", (2, 3, 3)),
         ("C1+C4   other split of 5", "sum", (1, 4)),
         ("C5      unsplit", "sum", (5,))]
print("name                              n  Kst KfU KfB chiral anomfree states")
res = {}
for nm, kind, bl in cands:
    n = sum(bl) if kind == "sum" else bl[0] * bl[1]
    ch, af, ns = analyse(kind, bl)
    g = dimG(kind, bl)
    KfU, KfB = n * n - g, n * (2 * n - 1) - g      # params fixed vs U(n), vs Spin(2n) Bogoliubov
    res[nm[:8].strip()] = (n, ch, af, KfU, KfB)
    print(f"{nm:33s} {n:2d} {n:4d} {KfU:3d} {KfB:3d} {str(ch):6s} {str(af):8s} {ns}")
R = res
check("1a chirality of the even half = n odd, for every split and the tensor",
      all(v[1] == (v[0] % 2 == 1) for v in R.values()))
check("1b tensor C2xC3 (6 modes) and oriented C2+C6 (8 modes) are vectorlike",
      not R["C2xC3"][1] and not R["C2+C6"][1])
check("1c chiral + anomaly-free is NOT unique to C2+C3: C1+C4, C5, C1+C6 also pass",
      all(R[k][1] and R[k][2] for k in ["C2+C3", "C1+C4", "C5", "C1+C6"]))
check("1d splits of C5 are indistinguishable by consistency (same Cartan, rank 4)",
      R["C2+C3"][1:3] == R["C1+C4"][1:3] == R["C5"][1:3])
ch = {k: v for k, v in R.items() if v[1] and v[2]}
minKfU = min(v[3] for v in ch.values()); minKfB = min(v[4] for v in ch.values())
check("1e least frame information fixed (IM: privilege no frames) picks C5 unsplit, not C2+C3",
      [k for k, v in ch.items() if v[3] == minKfU] == ["C5"] and R["C2+C3"][3] > minKfU,
      f"KfU: C5={R['C5'][3]}, C1+C4={R['C1+C4'][3]}, C2+C3={R['C2+C3'][3]}; vs Bogoliubov C2+C3 fixes {R['C2+C3'][4]} of 45")
check("1f least state bits (Kst=n) overall picks C1+C3 (vectorlike, 16 states)",
      min(R, key=lambda k: R[k][0]) == "C1+C3" and not R["C1+C3"][1])
# consistent unit counting: a binary unit (link or qubit) = one exclusive mode
check("1g count: one qubit is Lambda(C^1) (dim 2); Lambda(C^2) has dim 4 = two qubits",
      len(even_half(mode_weights("sum", (1,)))) * 2 == 2 and len(even_half(mode_weights("sum", (2,)))) * 2 == 4, "C2 counts levels, C3 counts binary links: unequal rule")
# owned-forward links: stabiliser in O_h of {+x,+y,+z}
dirs = [(s, a) for a in range(3) for s in (1, -1)]
Oh = [(p, sg) for p in permutations(range(3)) for sg in np.ndindex(2, 2, 2)]
def act(g, d):
    p, sg = g; s, a = d
    return (s * (1 - 2 * sg[p[a]]), p[a])
own = {(1, 0), (1, 1), (1, 2)}
stab = sum(1 for g in Oh if {act(g, d) for d in own} == own)
check("1h 'owned forward links' is lopsided: stabiliser 6 of 48 in O_h, 3 bits of convention",
      len(Oh) == 48 and stab == 6, f"orbit={48 // stab}")
cond = [nm for nm, kind, bl in cands if kind == "sum" and len(bl) == 2 and bl[0] == 2
        and R[nm[:8].strip()][1]]
check("1i C2+C3 is the Kst minimum only after conditioning on: qubit=2 modes, 2 blocks, chirality",
      [c[:5] for c in cond] == ["C2+C3"], "'+' vs 'x' cost one rule token each: rule text ties")

# ---------------- Part 2: spin vs isospin ----------------
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1.]).astype(complex)
I2 = np.eye(2)
def kron(*ms):
    out = np.eye(1)
    for m in ms: out = np.kron(out, m)
    return out
def annih(n):
    lo = np.array([[0, 1], [0, 0]], complex)
    return [kron(*([Z] * i + [lo] + [I2] * (n - i - 1))) for i in range(n)]
c = annih(5)                       # modes 0,1 = qubit levels; 2,3,4 = links
def onebody(h):                    # h: 5x5 one-body matrix -> Fock operator
    return sum(h[a, b] * c[a].conj().T @ c[b] for a in range(5) for b in range(5))
gens = []                          # s(u2+u3): off-diagonal + traceless diagonal per block, and Y
for blk in [(0, 1), (2, 3, 4)]:
    for a in blk:
        for b in blk:
            if a != b:
                h = np.zeros((5, 5), complex); h[a, b] = 1; gens.append(onebody(h))
    for a in blk[1:]:
        h = np.zeros((5, 5), complex); h[blk[0], blk[0]] = 1; h[a, a] = -1; gens.append(onebody(h))
gens.append(onebody(np.diag([Fr(1, 2)] * 2 + [Fr(-1, 3)] * 3).astype(float)))
D = 32; L = np.zeros((D * D, D * D), complex)
for G in gens:
    A = np.kron(np.eye(D), G) - np.kron(G.T, np.eye(D)); L += A.conj().T @ A
ev = np.linalg.eigvalsh(L); nul = int(np.sum(ev < 1e-9))
full = D - 1                        # basis index of |00000> is 0, all-filled is 31
X0 = np.zeros((D, D)); X0[full, 0] = 1
x0c = all(np.allclose(G @ X0, X0 @ G) for G in gens)
check("2a commutant of S(U2xU3) on Lambda(C^5): dim 14 = 10 sectors + M2 on {|0>,|full>}",
      nul == 14 and x0c, f"null={nul}; only (0,0)~(3,2) are isomorphic (both Y=0 singlets)")
check("2b its only su(2) acts on 2 neutral singlet states and kills every charged sector: not spin",
      x0c and nul - 12 == 2)
# R2 reading: rotations = qubit SU(2) on levels (+) SO(3) vector on links
eps = np.zeros((3, 3, 3))
for i, j, k in permutations(range(3)):
    eps[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])
J = []
for i, s in enumerate([X, Y, Z]):
    h = np.zeros((5, 5), complex); h[:2, :2] = s / 2; h[2:, 2:] = -1j * eps[i]
    J.append(onebody(h))
Gv = np.array([g.ravel() for g in gens]).T
inside = all(np.linalg.norm(Gv @ np.linalg.lstsq(Gv, Ji.ravel(), rcond=None)[0] - Ji.ravel()) < 1e-9 for Ji in J)
check("2c rotation generators of the R2 reading lie inside s(u2+u3): rotations ARE frame changes",
      inside)
J2 = sum(Ji @ Ji for Ji in J)
nq = onebody(np.diag([1, 1, 0, 0, 0.])).real.diagonal(); nl = onebody(np.diag([0, 0, 1, 1, 1.])).real.diagonal()
spins = {}
lab = {(0, 0): "nu^c", (0, 2): "e^c", (1, 1): "Q", (2, 0): "u^c", (2, 2): "d^c", (3, 1): "L"}
for (kl, kq), nm in lab.items():
    idx = [s for s in range(D) if round(nl[s]) == kl and round(nq[s]) == kq]
    Pj = np.zeros((D, D)); Pj[idx, idx] = 1
    jj = np.linalg.eigvalsh(Pj @ J2 @ Pj)[-len(idx):]
    spins[nm] = sorted({round((-1 + np.sqrt(1 + 4 * x)) / 2, 6) for x in jj})
print("R2-reading spin content:", {k: [float(x) for x in v] for k, v in spins.items()})
check("2d R2 reading contradicts measured spin-1/2 of all SM fermions (e^c spin 0, u^c spin 1)",
      spins["e^c"] == [0.0] and spins["u^c"] == [1.0] and spins["Q"] == [0.5, 1.5])
# separate spin on the 2^3 cell x qubit (16-dim)
G3 = [kron(X, I2, I2), kron(Z, X, I2), kron(Z, Z, X)]
S = [-0.5j * G3[1] @ G3[2], -0.5j * G3[2] @ G3[0], -0.5j * G3[0] @ G3[1]]
alg = all(np.allclose(S[i] @ S[(i + 1) % 3] - S[(i + 1) % 3] @ S[i], 1j * S[(i + 2) % 3]) for i in range(3))
cas = np.allclose(sum(s @ s for s in S), 0.75 * np.eye(8))
S16 = [np.kron(s, I2) for s in S]; T16 = [np.kron(np.eye(8), s / 2) for s in (X, Y, Z)]
comm = all(np.allclose(a @ b, b @ a) for a in S16 for b in T16)
Lc = sum((lambda A: A.conj().T @ A)(np.kron(np.eye(8), s) - np.kron(s.T, np.eye(8))) for s in S)
tastes = int(np.sum(np.linalg.eigvalsh(Lc) < 1e-9))
check("2e cell Clifford spin su(2) on C^8 x C^2 exists, j=1/2, commutes with the qubit SU(2)",
      alg and cas and comm)
check("2f but it carries 4 tastes (commutant M4: dim 16): 2 spin x 4 taste x 2 qubit = 16",
      tastes == 16, f"commutant dim={tastes}")
# axis-labelled transport on Z_3^3 vs colour SU(3)
Lx = 3; N = Lx ** 3
def shift(ax):
    T = np.zeros((N, N))
    for s in range(N):
        x = list(np.unravel_index(s, (Lx,) * 3)); x[ax] = (x[ax] + 1) % Lx
        T[np.ravel_multi_index(x, (Lx,) * 3), s] = 1
    return T
H = sum(np.kron(np.diag(np.eye(3)[i]), shift(i) + shift(i).T) for i in range(3))
lam1 = np.zeros((3, 3)); lam1[0, 1] = lam1[1, 0] = 1; lam3 = np.diag([1., -1, 0])
n1 = np.linalg.norm(H @ np.kron(lam1, np.eye(N)) - np.kron(lam1, np.eye(N)) @ H)
n3 = np.linalg.norm(H @ np.kron(lam3, np.eye(N)) - np.kron(lam3, np.eye(N)) @ H)
check("2g if link mode i moves along axis i, transport breaks colour SU(3) to its torus",
      n1 > 1 and n3 < 1e-12, f"|[H,l1]|={n1:.2f}, |[H,l3]|={n3:.0e}")

# ---------------- Part 3: families ----------------
def expm_h(h):
    w, v = np.linalg.eigh(h); return v @ np.diag(np.exp(1j * w)) @ v.conj().T
Ux = expm_h(onebody(np.pad(-np.pi / 4 * Y, ((0, 3), (0, 3)))))      # z-axis -> x-axis
Uy = expm_h(onebody(np.pad(np.pi / 4 * X, ((0, 3), (0, 3)))))       # z-axis -> y-axis
fam = np.hstack([np.eye(D), Ux, Uy])
rk = np.linalg.matrix_rank(fam)
check("3a the three record-axis 'families' span 32 states, not 96: same family, rotated basis",
      rk == 32, f"rank={rk}")
check("3b the axis change is an SU(2)_qubit frame change (gauge), so sectors are gauge-equivalent",
      np.allclose(Ux.conj().T @ Ux, np.eye(D)) and inside)
perms = [np.eye(3)[list(p)] for p in permutations(range(3))]
def inv_dim(pairs):
    Av = sum(np.kron(p, q) for p, q in pairs) / len(pairs)
    return int(round(np.trace(Av)))
dprod = inv_dim([(p, q) for p in perms for q in perms]); ddiag = inv_dim([(p, p) for p in perms])
check("3c S3_L x S3_R invariants: dim 1 (democratic J); diagonal S3 invariants: dim 2 (aI + bJ)",
      dprod == 1 and ddiag == 2)
a_, b_ = RNG.normal(size=2)
m = a_ * np.eye(3) + b_ * np.ones((3, 3)); sv = np.sort(np.abs(np.linalg.eigvalsh(m)))
check("3d a cubic rotation permutes axes once for all fields (diagonal S3): generic rank 3",
      np.linalg.matrix_rank(m) == 3 and abs(sv[0] - sv[1]) < 1e-12,
      f"masses={np.round(sv, 3)}; rank 1 needs a=0 (extra rule)")
print(f"TOTAL: PASS={P} FAIL={F}")
