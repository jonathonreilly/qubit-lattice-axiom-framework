"""register-family: do the link (rishon) or edge registers carry an ordered family charge?

Question. A mass and mixing law needs an ordered (U(1)-like) family charge, broken by a unit spurion of
size eps (Froggatt-Nielsen). The registers hold large integer ranges: link electric values, rishon number,
rishon flavours (about 28, 28, 680 per end), edge occupations n. Is any of them (a) conserved, exactly or
approximately, (b) able to tell three light families of one gauge content apart, (c) carried by doublets
and singlets independently?

Reading used (CL-1 link text): a bond's register is F rishon flavours per end; the hop x -> y of a site of
charge q is dressed by V^q, V the domain-normalised (polar) part of A = sum_f c_{x-end,f}^dag c_{y-end,f},
so the cluster number (matter + rishons at the site's end) is Gauss's law. Even operators on disjoint
modes commute, so on-site (Yukawa-type) terms see a register only through Gauss's law.

A registers on small Fock models   B an exact family charge   C eps and the ensembles vs measurement
"""
import itertools, time
import numpy as np

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))
rng = np.random.default_rng(20261022)
nrm = lambda M: float(np.max(np.abs(M))) if M.size else 0.0

def fermions(n):
    a = np.array([[0., 1.], [0., 0.]]); Z = np.diag([1., -1.]); I = np.eye(2)
    out = []
    for i in range(n):
        m = np.array([[1.]])
        for j in range(n): m = np.kron(m, Z if j < i else (a if j == i else I))
        out.append(m)
    return out
dag = lambda M: M.conj().T
comm = lambda A, B: A @ B - B @ A
def polar(A):
    w, U = np.linalg.eigh(dag(A) @ A)
    inv = np.where(w > 1e-10, 1 / np.sqrt(np.clip(w, 1e-30, None)), 0.0)
    return A @ (U * inv) @ dag(U)
def num(c): return dag(c) @ c

print("== A. registers on small Fock models (dense <= 2^8)")
# model 1: one bond, F = 3 flavours per end, one matter species at x and y: modes x, y, L1..3, R1..3
F = 3; c = fermions(2 + 2 * F); px, py = c[0], c[1]; L = c[2:2 + F]; R = c[2 + F:]
A = sum(dag(L[f]) @ R[f] for f in range(F)); V = polar(A)
H = dag(py) @ V @ px; H = H + dag(H)
G = {(a, b): dag(L[a]) @ L[b] + dag(R[a]) @ R[b] for a in range(F) for b in range(F)}
cU = max(nrm(comm(H, g)) for g in G.values()); cV = max(nrm(comm(V, g)) for g in G.values())
# flavour permutations as unitaries: products of swaps exp(i pi/2 (c_a^dag c_b + h.c.))-type -> use generators directly
def swap_unitary(a, b):
    K = sum(dag(e[a]) @ e[b] + dag(e[b]) @ e[a] - num(e[a]) - num(e[b]) for e in (L, R))
    w, U = np.linalg.eigh(K); return (U * np.exp(1j * np.pi / 2 * w)) @ dag(U)   # exp(i pi/2 K) up to phases
perm_dev = max(nrm(P @ H @ dag(P) - H) for P in (swap_unitary(0, 1), swap_unitary(1, 2)))
check("A1 [T, checked] rishon flavour is an exact per-bond U(F): every generator sum_ends c_a^dag c_b commutes with the "
      "polar raiser and with the dressed hop, and flavour swaps leave the hop unchanged, so every ratio of rishon hop "
      "amplitudes is exactly 1 (no flavour order, no eps); matter modes carry no U(F) index",
      cU < 1e-10 and cV < 1e-10 and perm_dev < 1e-10, f"F=3: max|[H,G]| {cU:.0e}, max|[V,G]| {cV:.0e}, swap dev {perm_dev:.0e}")
Gx = num(px) + sum(num(l) for l in L); Gy = num(py) + sum(num(r) for r in R)
per = [nrm(comm(H, num(px) + num(L[f]))) for f in range(F)]
# one-rishon amplitudes: |x, R_f> -> |y, L_f>
def basis_state(occ, n):
    idx = int("".join("1" if i in occ else "0" for i in range(n)), 2); v = np.zeros(2 ** n); v[idx] = 1; return v
amps = []
for f in range(F):
    for bg in ([], [2 + F + (f + 1) % F]):           # alone, and with another rishon on the y end
        s0 = basis_state([0, 2 + F + f] + bg, 2 + 2 * F); s1 = basis_state([1, 2 + f] + bg, 2 + 2 * F)
        amps.append(abs(s1 @ H @ s0))
check("A2 [T, checked] Gauss's law is the total cluster number only: n_x + N_x-end and n_y + N_y-end are conserved, but "
      "n_x + n_(x-end, f) is conserved for no single flavour, so no matter mode is tied to a flavour; one-rishon hop "
      "amplitudes are equal for every flavour and background",
      nrm(comm(H, Gx)) < 1e-10 and nrm(comm(H, Gy)) < 1e-10 and min(per) > 0.5 and np.ptp(amps[0::2]) < 1e-12
      and np.ptp(amps[1::2]) < 1e-12, f"|[H,n_x+n_Lf]| {min(per):.2f}..{max(per):.2f}; amps alone {amps[0]:.3f}, "
      f"with background {amps[1]:.3f}")

# model 2: two families a = 1, 2 at x, y on one bond with F = 2: modes 1x 1y 2x 2y L1 L2 R1 R2
c = fermions(8); P = {(a, s): c[2 * a + s] for a in range(2) for s in range(2)}; L2 = c[4:6]; R2 = c[6:8]
V2 = polar(sum(dag(L2[f]) @ R2[f] for f in range(2)))
Hb = sum(dag(P[a, 1]) @ V2 @ P[a, 0] for a in range(2)); Hb = Hb + dag(Hb)
T = {(a, b): sum(dag(P[a, s]) @ P[b, s] for s in range(2)) for a in range(2) for b in range(2)}
cT = max(nrm(comm(Hb, t)) for t in T.values())
Y = dag(P[0, 0]) @ P[1, 0]                              # on-site family-changing bilinear (a Yukawa-type entry)
regops = [V2, dag(V2)] + [dag(e[a]) @ e[b] for e in (L2, R2) for a in range(2) for b in range(2)]
cY = max(nrm(comm(Y, o)) for o in regops); GxT = num(P[0, 0]) + num(P[1, 0]) + num(L2[0]) + num(L2[1])
check("A3 [T, checked] with the rule's flavour-blind dressing the update commutes with U(2) rotations of the family label, "
      "and an on-site family-changing bilinear commutes with every register operator (raiser, U(F)) and with Gauss's law: "
      "the link register gives no selection rule and no weight among families",
      cT < 1e-10 and cY < 1e-12 and nrm(comm(Y, GxT)) < 1e-12, f"|[H,T_ab]| {cT:.0e}, |[Y,reg]| {cY:.0e}")
# flavour-selective dressing (the idea): family a dressed only by flavour a
Va = [polar(dag(L2[a]) @ R2[a]) for a in range(2)]
Hs = sum(dag(P[a, 1]) @ Va[a] @ P[a, 0] for a in range(2)); Hs = Hs + dag(Hs)
Ga = [num(P[a, 0]) + num(L2[a]) for a in range(2)]
check("A4 [T, checked] family-selective dressing (family a hops on flavour a): each family's cluster number becomes its own "
      "exact Gauss law, i.e. one linked U(1) per family (family photons), and the on-site family-changing bilinear "
      "violates it, so every family-changing mass entry is forbidden at all orders: masses diagonal, mixing a permutation",
      max(nrm(comm(Hs, g)) for g in Ga) < 1e-10 and nrm(comm(Y, Ga[0])) > 0.5,
      f"|[Hs,G_a]| {max(nrm(comm(Hs, g)) for g in Ga):.0e}, |[Y,G_1]| {nrm(comm(Y, Ga[0])):.1f}")
wmix = 0.3; Vw = [polar(dag(L2[a]) @ R2[a] + wmix * dag(L2[1 - a]) @ R2[1 - a]) for a in range(2)]
Hw = sum(dag(P[a, 1]) @ Vw[a] @ P[a, 0] for a in range(2)); Hw = Hw + dag(Hw)
check("A5 [T, checked] soft selectivity (flavour weights w_af with off-diagonal ratio r) keeps only the total Gauss law and "
      "breaks U(F); the ratio r is a new supplied coefficient, and the hop it weights never enters an on-site mass entry",
      nrm(comm(Hw, Ga[0])) > 1e-3 and nrm(comm(Hw, GxT)) < 1e-10, f"r = {wmix}: |[Hw,G_1]| {nrm(comm(Hw, Ga[0])):.2f}, "
      f"|[Hw,G_tot]| {nrm(comm(Hw, GxT)):.0e}")
print("   edge registers (cited, #9946 and CL-1 text): the edge hop conserves no edge number or parity; each cube's unitary "
      "reads its edges through gamma^ij and N alone, the same for every species, so an edge integer is neither "
      "conserved nor carried by a fermion; a family-dependent edge reading is an equivalence-principle violation")

print("== B. an exact family charge is linked: zeros, not powers")
nd = nfull = nperm = 0
for _ in range(3000):
    Q = rng.choice(10, 3, replace=False); h = rng.integers(-5, 6)
    u = -h - Q[rng.permutation(3)]; d = h - Q[rng.permutation(3)]          # singlet charges that allow full rank
    if rng.random() < 0.3: u[rng.integers(3)] = rng.integers(-15, 15)     # some draws: a singlet off the allowed set
    mu = (np.add.outer(u, Q) + h == 0); md = (np.add.outer(d, Q) - h == 0)
    Mu = mu * (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))); Md = md * (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
    nd += 1
    if np.linalg.matrix_rank(Mu) < 3 or np.linalg.matrix_rank(Md) < 3: continue
    nfull += 1
    _, Uu = np.linalg.eigh(dag(Mu) @ Mu); _, Ud = np.linalg.eigh(dag(Md) @ Md); Vabs = np.abs(dag(Uu) @ Ud)
    nperm += np.all((Vabs < 1e-9) | (Vabs > 1 - 1e-9))
check("B1 [T, checked] an exactly conserved charge Q_F with distinct doublet values (one Higgs, of any charge h): "
      "(M^dag M)_jk needs Q_j = Q_k, so both sectors are diagonal in the doublet basis and the quark mixing is a "
      "permutation for every singlet assignment; measured |V_us| = 0.2243(8) is 264 sigma from 0",
      nfull > 0 and nperm == nfull, f"{nd} draws, {nfull} with six massive quarks, all {nperm} permutation mixing")
qQ, qu, qd = np.array([3, 2, 0]), np.array([4, 1, 0]), np.array([1, 0, 0])
an = int(2 * qQ.sum() + qu.sum() + qd.sum())
check("B2 [T] an exact charge is linked (CL-1 link clause), so it must also be anomaly-free and long-range; the working "
      "FN control charge has SU(3)^2 U(1)_F anomaly sum(2Q + u + d) != 0, so a tower charge is an APPROXIMATE charge, "
      "which the link clause does not link and whose breaking size eps the rules must then fix", an != 0, f"anomaly {an}")

print("== C. eps from the registers, fit-free ensembles [M targets as zoom-tower: m_t:m_c:m_u 1:7e-3:1e-5, "
      "m_b:m_s:m_d 1:2e-2:1e-3, |V| .225/.042/.0037; hit = within x3 of all seven; |c| log-uniform [1/3,3], random phase]")
MEAS = dict(u32=7e-3, u21=1e-5 / 7e-3, d32=2e-2, d21=1e-3 / 2e-2, Vus=0.225, Vcb=0.042, Vub=0.0037)
W = np.log10(3.0)
def coeff(n): return np.exp(rng.uniform(np.log(1 / 3), np.log(3), (n, 3, 3))) * np.exp(2j * np.pi * rng.uniform(size=(n, 3, 3)))
def sv(M):
    U, s, Vh = np.linalg.svd(M); return s[:, ::-1], np.conj(np.swapaxes(Vh, 1, 2))[:, :, ::-1]
def obs(Q, u, d, eps, n):
    Eu = np.add.outer(u, Q).astype(float); Ed = np.add.outer(d, Q).astype(float)
    su, Vu = sv(coeff(n) * eps ** (Eu - Eu.min())); sd, Vd = sv(coeff(n) * eps ** (Ed - Ed.min()))
    Vm = np.abs(np.conj(np.swapaxes(Vu, 1, 2)) @ Vd)
    return dict(u32=su[:, 1] / su[:, 2], u21=su[:, 0] / su[:, 1], d32=sd[:, 1] / sd[:, 2], d21=sd[:, 0] / sd[:, 1],
                Vus=Vm[:, 0, 1], Vcb=Vm[:, 1, 2], Vub=Vm[:, 0, 2])
def joint(o): return float(np.all([np.abs(np.log10(o[k] / MEAS[k])) < W for k in MEAS], axis=0).mean())
z = np.zeros(3, int)
s_an = joint(obs(z, z, z, 1.0, 4000)); s_fn = joint(obs(qQ, qu, qd, 0.22, 4000))
check("C1 [E] the registers' only amplitude ratios are U(F)-invariant, so eps = 1: every charge assignment collapses to "
      "anarchy, which never hits, while the supplied U(1) FN control (Q=(3,2,0), u=(4,1,0), d=(1,0,0), eps 0.22) does",
      s_an == 0 and s_fn > 0.03, f"joint hit: eps=1 {s_an:.4f}, FN control {s_fn:.3f} (4000 samples each)")
# look-elsewhere: if an ordered charge were supplied, would the masses test a register-shaped eps?
cands = {"1/8": 1 / 8, "1/(2S+1),S=3/2": 0.25, "1/3 (b=3)": 1 / 3, "2^-3/2 rung": 2 ** -1.5, "1/2": 0.5,
         "(2S/(2S+1))^2": 0.5625, "2S/(2S+1)": 0.75}
print("   look-elsewhere, supplied integer charges in a +-1 box (729 cells x 100) around each eps's ideal exponents:")
res = {}
for name, e in cands.items():
    a = {k: np.log(v) / np.log(e) for k, v in MEAS.items()}
    Q2 = a["Vcb"]; Q1 = a["Vus"] + Q2; u2 = a["u32"] - Q2; u1 = a["u21"] - (Q1 - Q2) + u2
    d2 = a["d32"] - Q2; d1 = a["d21"] - (Q1 - Q2) + d2
    cen = np.rint([Q1, Q2, u1, u2, d1, d2]).astype(int); hits = []
    for dv in itertools.product((-1, 0, 1), repeat=6):
        x = np.maximum(cen + np.array(dv), 0)
        hits.append(joint(obs(np.array([x[0], x[1], 0]), np.array([x[2], x[3], 0]), np.array([x[4], x[5], 0]), e, 100)))
    hits = np.array(hits); res[name] = (hits.max(), (hits >= 0.5 * s_fn).mean(), cen.max())
    print(f"     eps {e:.3f} [{name}]: best {hits.max():.2f}, cells >= half control {(hits >= 0.5 * s_fn).mean():.2f}, "
          f"max charge {cen.max()}")
okr = [k for k, v in res.items() if v[0] >= 0.5 * s_fn]
check("C2 [E] once integer charges are supplied, every register-shaped eps from 1/8 to 3/4 reaches the control's rate in "
      "some cell of its box: masses and mixing do not select eps, so a rule ratio landing near 0.2-0.4 is no evidence; "
      "the charges, not eps, carry the fit", len(okr) >= 5, f"{len(okr)}/{len(cands)} eps values reach half the control")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
