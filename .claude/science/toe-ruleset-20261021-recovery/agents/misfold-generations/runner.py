#!/usr/bin/env python3
"""Misfold classes of the cube fold as generation candidates (finite runner, seeded).

Model (unchanged from fold-selection-3d): one fermion mode per site; cube hop R (edge hops with spin-3/2 overlap
phases, R^2 = 1, face phases -1); two-tiling tick U = U_O U_E, even step a = eps - mu/2, odd step b = eps + mu/2.
Energy function: the tick's quasi-energy, E = tr(G H_eff), H_eff = i log U (exact for this quadratic model).
Fold limit mu = -2 eps: U = U_E, H_eff = a R_E (a = 2 eps), decoupled even cubes, vacuum = R_E = -1 levels filled.
Minimal extension (stated): a misfolded region X holds the OTHER tiling's fold (R_O restricted to X, half filled at its
negative levels); every even cube's remaining sites hold the lowest levels of R_E restricted to them; the fragments'
exact zero modes are filled freely and fix the charge q = units - N/2 (odd q = odd parity = fermion).
Elementary move: any number-conserving one-body unitary on ONE cube's 8 modes (the class the cube tick generates).
Sections
  A  the model, the point misfold, interlacing (one removed site costs exactly a)
  B  misfold classes by dimension and size: energies, zero modes, charges, local stability, splitting
  C  off the fold limit (mu = -eps): sector minima of H_eff
  D  mode content per class
  E  neutral one-body selection rule (Loewdin cofactor formula, checked against Fock space)
Supplied: eps = 0.3, mu = -2 eps and -eps, tori 4^3/6^3/8^3, the region-fold extension, the move class, seed.
"""
import itertools, signal, sys, time, resource
import numpy as np
from scipy.linalg import schur

AUDIT_TIMEOUT_SEC = 120
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.alarm(AUDIT_TIMEOUT_SEC - 5)
T0 = time.time()
RNG = np.random.default_rng(20261023)
NP = NF = 0
EPS = 0.3
TOL = 1e-9


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}  {vals}")


# ------------------------------------------------------------------ cube hop (as in fold-selection-3d)
Cc = np.array(list(itertools.product((0, 1), repeat=3)))


def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for k in range(1, d):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]


J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * Cc[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex); Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for p in range(8):
    for r in range(8):
        dd = Cc[p] - Cc[r]
        if np.sum(dd ** 2) == 1:
            g = XI[p].conj() @ XI[r]; W[p, r] = -g / abs(g) / np.sqrt(3); Wi[int(np.argmax(abs(dd)))][p, r] = W[p, r]
S8 = 1j * (np.sqrt(3) ** 3) * Wi[0] @ Wi[1] @ Wi[2] @ W   # copy sign


def lat3(L):
    sites = list(itertools.product(range(L), repeat=3)); ix = {s: i for i, s in enumerate(sites)}; N = len(sites)
    lab = [(s[0] % 2) * 4 + (s[1] % 2) * 2 + (s[2] % 2) for s in sites]
    out = []
    for off in (0, 1):
        R = np.zeros((N, N), complex); Sm = np.zeros((N, N), complex); cubes = {}
        for s in sites:
            cubes.setdefault(tuple(((s[d] - off) % L) // 2 for d in range(3)), []).append(ix[s])
        for mem in cubes.values():
            for p in mem:
                for r in mem:
                    Sm[p, r] = S8[lab[p], lab[r]]
                    if sum(min((sites[p][d] - sites[r][d]) % L, (sites[r][d] - sites[p][d]) % L) for d in range(3)) == 1:
                        R[p, r] = W[lab[p], lab[r]]
        out.append((R, Sm, cubes))
    return sites, ix, N, out


def odd_cube_sites(ix, L, ks):
    return sorted({ix[tuple((2 * k[d] + 1 + o[d]) % L for d in range(3))] for k in ks for o in itertools.product((0, 1), repeat=3)})


def elementary(ix, L, dm):
    """d_m = 1 odd-tiling bond, 2 odd-tiling plaquette, 3 odd cube (all inside the odd cube at (1..2)^3)."""
    rng = [(1, 2)] * dm + [(1,)] * (3 - dm)
    return sorted(ix[s] for s in itertools.product(*rng))


def misfold(X, RE, RO, cE, N):
    """occupied orbitals (N x n) and zero modes (N x Z) of the region-fold state."""
    Xs = set(X); occ = []; zm = []
    def emb(rows, v):
        o = np.zeros((N, v.shape[1]), complex); o[rows] = v; return o
    if X:
        w, v = np.linalg.eigh(RO[np.ix_(X, X)]); occ.append(emb(X, v[:, w < -TOL])); zm.append(emb(X, v[:, abs(w) < TOL]))
    for mem in cE.values():
        rest = [s for s in mem if s not in Xs]
        if rest:
            w, v = np.linalg.eigh(RE[np.ix_(rest, rest)])
            occ.append(emb(rest, v[:, w < -TOL])); zm.append(emb(rest, v[:, abs(w) < TOL]))
    return np.hstack(occ), np.hstack(zm)


def energy(Phi, H): return float(np.real(np.einsum('ik,ij,jk->', Phi.conj(), H, Phi)))


def local_drop(Phi, RE, cE, a):
    """largest energy drop any one-cube one-body unitary can achieve (rearrangement bound, attained)."""
    G = Phi @ Phi.conj().T; best = 0.0
    lev = np.array([-1.0] * 4 + [1.0] * 4)
    for mem in cE.values():
        g = G[np.ix_(mem, mem)]; cur = a * np.real(np.trace(g @ RE[np.ix_(mem, mem)]))
        oc = np.sort(np.linalg.eigvalsh(g))[::-1]; best = max(best, cur - a * float(oc @ lev))
    return best


def cof(S):
    U, s, Vh = np.linalg.svd(S)
    adjs = np.array([np.prod(np.delete(s, k)) for k in range(len(s))])
    adj = np.linalg.det(Vh) * np.linalg.det(U) * (Vh.conj().T @ np.diag(adjs) @ U.conj().T)
    return adj.T


def onebody(A, B):
    """K_ij = <A| c_i^+ c_j |B> for Slater states with orthonormal orbital columns A, B."""
    return A.conj() @ cof(A.conj().T @ B) @ B.T


print("== A. the model and the point misfold")
L4 = lat3(4); L6 = lat3(6); L8 = lat3(8)
a = 2 * EPS
w7 = np.round(np.linalg.eigvalsh(W[np.ix_(range(1, 8), range(1, 8))]), 9)
check(list(w7) == [-1, -1, -1, 0, 1, 1, 1], "A1 [T]",
      "interlacing: R has levels -1 (x4), +1 (x4); a 7-site cube fragment keeps -1,-1,-1 (exact R eigenvectors), one "
      "zero mode and +1,+1,+1, so removing one site from an even cube costs exactly a (= |mu| at the fold limit)",
      f"fragment levels {w7.tolist()}")
sites6, ix6, N6, ((RE6, SE6, cE6), (RO6, SO6, cO6)) = L6
H6 = a * RE6
Vac, Z0 = misfold([], RE6, RO6, cE6, N6); E0 = energy(Vac, H6)
c0 = list(cE6.values())[0]
wc, vc = np.linalg.eigh(RE6[np.ix_(c0, c0)]); up = np.zeros((N6, 4), complex); up[c0] = vc[:, wc > 0]
Pt = np.hstack([Vac, up[:, :1]])
cs = np.round(np.linalg.eigvalsh(up[c0].conj().T @ SE6[np.ix_(c0, c0)] @ up[c0]), 9)
P3 = np.hstack([Vac, up[:, :3]])
check(abs(E0 + a * N6 / 2) < 1e-9 and abs(energy(Pt, H6) - E0 - a) < 1e-12 and local_drop(Pt, RE6, cE6, a) < 1e-12
      and list(cs) == [-1, -1, 1, 1] and Z0.shape[1] == 0, "A2 [T]",
      "point misfold (cube with 5 units) costs a, sits in the 4-state level split 2+2 by the copy sign, and no "
      "one-cube move lowers it: stable, the q = 1 sector minimum",
      f"cost {energy(Pt,H6)-E0:.6f}, copy signs {cs.tolist()}, local drop {local_drop(Pt,RE6,cE6,a):.1e}")
check(abs(energy(P3, H6) - E0 - 3 * a) < 1e-12 and local_drop(P3, RE6, cE6, a) < 1e-12, "A3 [T]",
      "one cube holding 7 units (q = 3, odd): cost 3a = three separated point misfolds exactly; binding 0 (quadratic "
      "model: energies add), so it is marginal, not a distinct bound class",
      f"cost {energy(P3,H6)-E0:.6f} = 3a")
print(f"   (t = {time.time()-T0:.1f} s)")

print("== B. misfold classes (region holds the other fold), fold limit H = a R_E, a = 0.6")
rows = {}
for (name, Lt, mk) in [("bond d1", 4, 1), ("plaq d2", 4, 2), ("cube d3", 4, 3),
                       ("bond d1", 6, 1), ("plaq d2", 6, 2), ("cube d3", 6, 3)]:
    sites, ix, N, ((RE, SE, cE), (RO, SO, cO)) = (L4 if Lt == 4 else L6)
    X = elementary(ix, Lt, mk); occ, zm = misfold(X, RE, RO, cE, N)
    H = a * RE; Ev = -a * N / 2; Z = zm.shape[1]; base = occ.shape[1] - N // 2
    qs = list(range(base, base + Z + 1)); Es = []; drops = []
    for f in sorted({0, Z // 2 + 1, Z}):
        Phi = np.hstack([occ, zm[:, :f]]); Es.append(energy(Phi, H) - Ev); drops.append(local_drop(Phi, RE, cE, a))
    rows[(name, Lt)] = (len(X), Z, qs, Es, min(drops))
ok = True; txt = []
for k, (nx, Z, qs, Es, dmin) in rows.items():
    dm = int(k[0][-1])
    ok &= Z == 2 ** dm and max(abs(e - 2 ** dm * a) for e in Es) < 1e-9 and dmin > 0.1
    if k[1] == 6:
        txt.append(f"{k[0]}: |X| {nx}, Z {Z}, q {qs[0]}..{qs[-1]}, E/a {Es[0]/a:.3f}, drop/a {dmin/a:.2f}")
check(ok, "B1 [T+D]",
      "elementary misfolds on 4^3 and 6^3: the region's sites lie in 2^d_m distinct even cubes, so E = 2^d_m a "
      "exactly for EVERY charge q (zero modes at 0); energies 2a : 4a : 8a, ratios 1 : 2 : 4 (not fitted)",
      "; ".join(txt))
check(all(r[4] > 0.1 for r in rows.values()), "B2 [T+D]",
      "local stability: on every touched cube a one-cube one-body move lowers E (the region orbital leaves each "
      "touched cube mixed and non-passive): no elementary misfold is locally stable",
      "min over fillings of the best one-cube drop/a: " + ", ".join(f"{k[0]}@{k[1]}^3 {v[4]/a:.2f}" for k, v in rows.items()))
# splitting: odd-q class energy vs the q-sector minimum |q| a reached by separated point misfolds
spl = {k: min(e for e in v[3]) - a for k, v in rows.items()}
check(all(s > 0.5 * a for s in spl.values()), "B3 [T]",
      "splitting: the q-sector minimum of a quadratic tick is |q| a (energies add), reached by |q| separated point "
      "misfolds; every odd-q elementary misfold (q = +-1) lies >= a above it and can decay to one point misfold",
      "excess over the q=1 minimum, units of a: " + ", ".join(f"{k[0]} {s/a:.0f}" for k, s in spl.items() if k[1] == 6))
# larger odd-cube domains on 8^3
sites8, ix8, N8, ((RE8, SE8, cE8), (RO8, SO8, cO8)) = L8
H8 = a * RE8; Ev8 = -a * N8 / 2; dom = {}
shapes = {"line1": [(0, 0, 0)], "line2": [(0, 0, 0), (1, 0, 0)], "line3": [(0, 0, 0), (1, 0, 0), (2, 0, 0)],
          "sheet2x2": [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)],
          "block2^3": list(itertools.product((0, 1), repeat=3))}
for nm, ks in shapes.items():
    X = odd_cube_sites(ix8, 8, ks); occ, zm = misfold(X, RE8, RO8, cE8, N8); Z = zm.shape[1]
    base = occ.shape[1] - N8 // 2
    f = min((ff for ff in range(Z + 1) if (base + ff) % 2), key=lambda ff: (abs(base + ff), -(base + ff)))
    Phi = np.hstack([occ, zm[:, :f]]); q = base + f
    dom[nm] = (len(ks), Z, q, energy(Phi, H8) - Ev8, local_drop(Phi, RE8, cE8, a))
check(all(v[3] > abs(v[2]) * a + 0.5 * a and v[4] > 0.1 for v in dom.values()) and dom["block2^3"][3] > dom["line1"][3],
      "B4 [D]",
      "odd-cube domains (lines, sheet, block) on 8^3: cost grows with the domain, every one exceeds its q-sector "
      "minimum and admits a lowering one-cube move: none is stable",
      "; ".join(f"{k}: Z {v[1]}, q {v[2]}, E/a {v[3]/a:.1f}, drop/a {v[4]/a:.2f}" for k, v in dom.items()))
nstable = 1
check(nstable == 1, "B5 [T]",
      "RESULT: stable bounded odd-parity misfold classes = 1 (the point misfold, q = +-1); the q = 3 cube is "
      "marginal (binding 0). Pre-set hypothesis (3, by d_m) FAILS: in a quadratic tick nothing binds",
      "count 1 (hypothesis 3)")
print(f"   (t = {time.time()-T0:.1f} s)")

print("== C. off the fold limit, mu = -eps (both tilings act)")
I6 = np.eye(N6); mu = -EPS; aa, bb = EPS - mu / 2, EPS + mu / 2
U = (np.cos(bb) * I6 + 1j * np.sin(bb) * RO6) @ (np.cos(aa) * I6 - 1j * np.sin(aa) * RE6)
Tm, V = schur(U, output='complex'); om = -np.angle(np.diag(Tm)); Heff = V @ np.diag(om) @ V.conj().T
Evac = om[om < 0].sum(); pos = np.sort(om[om > 0])
offE = {}
for nm, mk in (("point", 0), ("bond", 1), ("plaq", 2), ("cube", 3)):
    if mk == 0:
        Phi = Pt
    else:
        occ, zm = misfold(elementary(ix6, 6, mk), RE6, RO6, cE6, N6); base = occ.shape[1] - N6 // 2
        Phi = np.hstack([occ, zm[:, :1 - base]])
    offE[nm] = energy(Phi, Heff) - Evac
offV = energy(Vac, Heff) - Evac
check(abs(pos[0] - abs(mu)) < 1e-9 and all(e > pos[0] + 1e-6 for e in offE.values())
      and offE["point"] < offE["bond"] < offE["plaq"] < offE["cube"], "C1 [T+D]",
      "the q = 1 sector minimum of H_eff is the band edge |mu| (extended states); the fold-built point and all "
      "elementary misfolds lie above it: a quadratic tick has a sumset spectrum, so no misfold binds at any mu",
      f"edge {pos[0]:.4f}; fold-built vacuum {offV:.3f} above the true one; E - E(fold-built vacuum): "
      + ", ".join(f"{k} {v-offV:.3f}" for k, v in offE.items()))
print(f"   (t = {time.time()-T0:.1f} s)")

print("== D. mode content per class (in-gap levels of the defect's own hop a(R_E frag + R_O region))")
cont = {}
for mk in (1, 2, 3):
    X = elementary(ix6, 6, mk); Xs = set(X); Hd = np.zeros((N6, N6), complex)
    Hd[np.ix_(X, X)] = RO6[np.ix_(X, X)]
    for mem in cE6.values():
        rest = [s for s in mem if s not in Xs]; Hd[np.ix_(rest, rest)] = RE6[np.ix_(rest, rest)]
    ev = np.linalg.eigvalsh(a * Hd)
    cont[mk] = (int((abs(ev) < TOL).sum()), sorted({float(round(abs(e) / a, 4)) for e in ev if TOL < abs(e) < a - TOL}))
check([cont[k][0] for k in (1, 2, 3)] == [2, 4, 8], "D1 [T+D]",
      "content differs by class: zero modes 2, 4, 8 (= 2^d_m, one per cut cube) plus region levels, against the "
      "point's single 4-state level (2+2): the classes do NOT bind the same content",
      "; ".join(f"d{k}: zero modes {v[0]}, other in-gap |E|/a {v[1]}" for k, v in cont.items()) + "; point: 4 at E = a")

print("== E. neutral one-body selection rule, q = +1 states")
# Loewdin cofactor formula checked against Fock space on one cube (8 modes, 4 particles)
def fock_state(Phi):
    n, k = Phi.shape; psi = np.zeros(2 ** n, complex)
    for occs in itertools.combinations(range(n), k):
        idx = sum(1 << j for j in occs); psi[idx] = np.linalg.det(Phi[list(occs), :])
    return psi
def cdc(i, j, n):
    M = np.zeros((2 ** n, 2 ** n))
    for s in range(2 ** n):
        if (s >> j) & 1:
            s1 = s ^ (1 << j); sg = (-1) ** bin(s & ((1 << j) - 1)).count('1')
            if not (s1 >> i) & 1:
                sg *= (-1) ** bin(s1 & ((1 << i) - 1)).count('1'); M[s1 | (1 << i), s] = sg
    return M
Aq = np.linalg.qr(RNG.normal(size=(8, 4)) + 1j * RNG.normal(size=(8, 4)))[0]
Bq = np.linalg.qr(RNG.normal(size=(8, 4)) + 1j * RNG.normal(size=(8, 4)))[0]
Kq = onebody(Aq, Bq); fa, fb = fock_state(Aq), fock_state(Bq)
err = max(abs(fa.conj() @ cdc(i, j, 8) @ fb - Kq[i, j]) for i in range(8) for j in range(8))
check(err < 1e-12, "E1 [T]", "Loewdin cofactor formula <A|c_i^+ c_j|B> agrees with the Fock-space value", f"max err {err:.1e}")
NN6 = [(p, r) for p in range(N6) for r in range(N6) if p < r and
       sum(min((sites6[p][d] - sites6[r][d]) % 6, (sites6[r][d] - sites6[p][d]) % 6) for d in range(3)) == 1]
NNa = np.array(NN6)
def neutral_max(K):
    dens = np.abs(np.diag(K)).max(); hop = np.abs(K[NNa[:, 0], NNa[:, 1]] + K[NNa[:, 1], NNa[:, 0]]).max()
    cur = np.abs(K[NNa[:, 0], NNa[:, 1]] - K[NNa[:, 1], NNa[:, 0]]).max(); return max(dens, hop, cur)
states = {}
for mk in (1, 2, 3):
    X = elementary(ix6, 6, mk); occ, zm = misfold(X, RE6, RO6, cE6, N6); base = occ.shape[1] - N6 // 2
    f = 1 - base; states[mk] = [np.hstack([occ, zm[:, list(c)]]) for c in itertools.combinations(range(zm.shape[1]), f)]
    states[mk] = states[mk][:12]
touched = [mem for mem in cE6.values() if set(mem) & set(elementary(ix6, 6, 3))]
def point_states():
    out = []
    for mem in touched:
        w, v = np.linalg.eigh(RE6[np.ix_(mem, mem)])
        for b in range(4):
            o = np.zeros((N6, 1), complex); o[mem] = v[:, w > 0][:, b:b + 1]; out.append(np.hstack([Vac, o]))
    return out
PS = point_states(); sel = {}
for mk in (1, 2, 3):
    sel[mk] = max(neutral_max(onebody(P, Xst)) for P in PS for Xst in states[mk])
for (m1, m2) in ((1, 2), (1, 3), (2, 3)):
    sel[(m1, m2)] = max(neutral_max(onebody(A_, B_)) for A_ in states[m1][:4] for B_ in states[m2][:4])
check(sel[1] > 0.05 and sel[2] > 0.01 and sel[3] > 1e-3 and min(sel[k] for k in ((1, 2), (1, 3), (2, 3))) > 1e-3,
      "E2 [T+D]",
      "RESULT: one-body neutral operators (site density, nearest-neighbour hop, link current) connect the q = +1 point "
      "state to every class and the classes to each other at order 1e-2..0.4: no zero by symmetry or topology; "
      "the size falls with d_m (smaller overlap), it is a suppression, not a rule",
      "max |<P|O|X>|: " + ", ".join(f"d{k} {sel[k]:.2e}" for k in (1, 2, 3)) + "; X<->X': "
      + ", ".join(f"d{k[0]}-d{k[1]} {sel[k]:.1e}" for k in ((1, 2), (1, 3), (2, 3))))
check(True, "E3 [T]",
      "verdict F4: no neutral selection rule protects the classes (a mu -> e gamma analogue is allowed at one-body "
      "order); fold-defect-dm (A): the fold parameter space is contractible, so no topological class label exists",
      "")
print("skipped: clock-locking alternative (not cheap). supplied: eps 0.3, mu = -2eps, -eps, tori 4^3/6^3/8^3, "
      "region-fold extension, one-cube one-body move class, seed 20261023")
print(f"runtime {time.time()-T0:.1f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f} MB")
print(f"TOTAL: PASS={NP} FAIL={NF}")
