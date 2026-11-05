AUDIT_INPUT_PATHS = ('docs/THE_TWO_TILING_TICK_HAS_NO_CELL_LOCAL_FAMILY_SYMMETRY_AND_A_TURN_TRIPLET_FORCES_TURN_INVARIANT_MIXING_TO_BE_CP_BLIND_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Two-tiling and two-rung family space of the CL-1 tick (supplied model, seeded, self-contained).

A. CL-1 two-tiling update on Z^3 (face phase -1, Bloch over 2Z^3, 8 modes per cell), with and without
   the copy mass: cell-local commutant (structural = all steps; and at fixed generic parameters),
   fibre degeneracies, the three-fold turn on every degenerate fibre space at turn-fixed momenta.
B. Two-rung nesting: (B1) one parent cube of 8 fine cubes (64 modes; fine tick in every child cube,
   parent tick moving whole cubes, identity on child labels); (B2) plus the fine odd cube at its centre;
   (B3) the nested two-tiling lattice (Bloch over 4Z^3, fine and parent even/odd ticks, copy masses).
C. Family mixing: turn-invariant up/down mass operators on each degenerate family space; CP-odd
   quartets; exact Z3 lemma.
"""
import itertools
import numpy as np

AUDIT_TIMEOUT_SEC = 120
rng = np.random.default_rng(20261022)
NP = [0, 0]
def check(tag, ok, msg):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {msg}")

E3 = np.eye(3, dtype=int)
OM = np.exp(2j * np.pi / 3)
def eta(x, i): return [1, (-1) ** int(x[0]), (-1) ** int(x[0] + x[1])][i]   # -1 around every unit face

def fam_pairs(c, rung, par):
    """hop pairs (x, y, amp, axis) of the rung-`rung` cubes with corner parity `par` in one cell of side c."""
    out = []; s = 2 ** (rung - 1); nc = c // s
    for X in itertools.product(range(nc), repeat=3):
        X = np.array(X)
        if np.any((X - par) % 2): continue
        for o in itertools.product((0, 1), repeat=3):
            o = np.array(o)
            for i in range(3):
                if o[i]: continue
                A = X + o; B = A + E3[i]
                for f in itertools.product(range(s), repeat=3):
                    f = np.array(f); out.append((s * A + f, s * B + f, eta(A, i), i))
    return out

def bloch(pairs, c, k, i):
    n = c ** 3; M = np.zeros((n, n), complex)
    for x, y, amp, j in pairs:
        if j != i: continue
        a = np.ravel_multi_index(tuple(x % c), (c,) * 3); b = np.ravel_multi_index(tuple(y % c), (c,) * 3)
        ph = amp * np.exp(-1j * k @ (x // c - y // c)); M[a, b] += ph; M[b, a] += np.conj(ph)
    return M

def tickset(c, k, fams):
    return [[bloch(p, c, k, i) for i in range(3)] for p in fams]

def cube_step(W, ang, cm):
    """exp(-i ang R) with copy factor C = exp(i cm (R - i w)) before and after (cm = M N / 4)."""
    n = W[0].shape[0]; I = np.eye(n); R = sum(W) / np.sqrt(3)
    U = np.cos(ang) * I - 1j * np.sin(ang) * R
    if cm:
        iw = 1j * W[0] @ W[1] @ W[2]
        C = (np.cos(cm) * I + 1j * np.sin(cm) * R) @ (np.cos(cm) * I - 1j * np.sin(cm) * iw)
        U = C @ U @ C
    return U

def update(T, eps, mu, Mc, rungs):
    """CL-1 half-ticks: even exp(-i(eps-mu/2)R) with copy, odd exp(+i(eps+mu/2)R); rung by rung."""
    n = T[0][0].shape[0]; U = np.eye(n, dtype=complex)
    for r in range(rungs):
        e, m, M = eps[r], mu[r], Mc[r]
        U = cube_step(T[2 * r + 1], -(e + m / 2), 0) @ cube_step(T[2 * r], e - m / 2, M / 4) @ U
    return U

def nullspace(rows, tol=1e-9):
    A = np.vstack(rows); _, s, vh = np.linalg.svd(A, full_matrices=False)
    return vh[np.sum(s > tol):].conj()

def commutant(ops):
    n = ops[0].shape[0]
    ns = nullspace([np.kron(o, np.eye(n)) - np.kron(np.eye(n), o.T) for o in ops])
    return [v.reshape(n, n) for v in ns]

def rand_elem(gens, nw=60, L=6):
    n = gens[0].shape[0]; H = np.zeros((n, n), complex)
    for _ in range(nw):
        w = np.eye(n, dtype=complex)
        for _ in range(rng.integers(1, L + 1)): w = w @ gens[rng.integers(len(gens))]
        H += rng.normal() * (w + w.conj().T) + rng.normal() * 1j * (w - w.conj().T)
    return H

def commutant_big(ops):
    """exact commutant inside the eigenspace blocks of a generic algebra element (the commutant lies there)."""
    n = ops[0].shape[0]; ev, V = np.linalg.eigh(rand_elem(ops)); B = []; i = 0
    while i < n:
        j = i
        while j + 1 < n and ev[j + 1] - ev[i] < 1e-7: j += 1
        G = V[:, i:j + 1]; B += [np.outer(G[:, a], G[:, b].conj()) for a in range(j - i + 1) for b in range(j - i + 1)]
        i = j + 1
    Gm = np.zeros((len(B), len(B)), complex)
    for o in ops:
        A = np.array([(b @ o - o @ b).ravel() for b in B]); Gm += A.conj() @ A.T
    ev2, V2 = np.linalg.eigh(Gm)
    return [sum(c_ * b for c_, b in zip(V2[:, m], B)) for m in np.nonzero(ev2 < 1e-9)[0]]

def eig_groups(U, tol=1e-7):
    ev, V = np.linalg.eig(U); ph = np.angle(ev); order = np.argsort(ph); ph = ph[order]; V = V[:, order]
    groups = []; i = 0
    while i < len(ph):
        j = i
        while j + 1 < len(ph) and abs(ph[j + 1] - ph[i]) < tol: j += 1
        Q, _ = np.linalg.qr(V[:, i:j + 1]); groups.append(Q); i = j + 1
    if len(groups) > 1 and abs(abs(ph[0] - ph[-1]) - 2 * np.pi) < tol:   # wrap at +-pi
        groups[0] = np.linalg.qr(np.hstack([groups[0], groups[-1]]))[0]; groups.pop()
    return groups

def turn_lift(c, k, fams):
    """diagonal phases D with D P W_i P^T D^* = W_{g(i)} on every family, g: e1->e2->e3->e1."""
    n = c ** 3; idx = lambda a: np.ravel_multi_index(tuple(a), (c,) * 3)
    perm = np.zeros(n, int)
    for a in itertools.product(range(c), repeat=3):
        perm[idx(a)] = idx((a[2], a[0], a[1]))
    P = np.zeros((n, n)); P[perm, np.arange(n)] = 1
    gk = np.array([k[2], k[0], k[1]])
    src = sum([[P @ W @ P.T for W in Ws] for Ws in tickset(c, k, fams)], [])
    tgt = sum([[Ws[1], Ws[2], Ws[0]] for Ws in tickset(c, gk, fams)], [])
    D = np.zeros(n, complex); D[0] = 1; todo = [0]
    while todo:
        x = todo.pop()
        for A, B in zip(src, tgt):
            for y in np.nonzero(np.abs(A[x]) > 1e-12)[0]:
                if D[y] == 0: D[y] = np.conj(B[x, y] / A[x, y] / D[x]); todo.append(y)
    U = np.diag(D) @ P
    ok = np.all(np.abs(D) > 0) and all(np.allclose(U @ A @ U.conj().T, B) for A, B in
                                       zip([P.T @ s @ P for s in src], tgt))
    return U, ok

def turn_spectrum(U, Q, tol=1e-6):
    """turn on a turn-invariant subspace Q: eigenvalue multiplicities n_lambda and whether some lambda, lambda w,
       lambda w^2 all occur (a turn triplet)."""
    lam = np.linalg.eigvals(Q.conj().T @ U @ Q); cl = []
    for l in lam:
        for c_ in cl:
            if abs(l - c_[0]) < tol: c_[1] += 1; break
        else: cl.append([l, 1])
    has = lambda x: any(abs(x - c_[0]) < tol for c_ in cl)
    trip = any(has(c_[0] * OM) and has(c_[0] * OM ** 2) for c_ in cl)
    return sorted([c_[1] for c_ in cl], reverse=True), trip
def jmax(Hu, Hd):
    _, Uu = np.linalg.eigh(Hu); _, Ud = np.linalg.eigh(Hd); V = Uu.conj().T @ Ud; m = len(V); best = 0
    for a, b in itertools.combinations(range(m), 2):
        for i, j in itertools.combinations(range(m), 2):
            best = max(best, abs(np.imag(V[a, i] * V[b, j] * np.conj(V[a, j]) * np.conj(V[b, i]))))
    return best

def herm(n): X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return X + X.conj().T
EPS, MU, MC = 0.37, 0.11, 0.53
z = np.zeros(3)
def herm(n): X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return X + X.conj().T
def reynolds(U, X):
    n = len(U); Uk = U.copy(); r = 1
    while not np.allclose(Uk, Uk[0, 0] * np.eye(n)) and r < 48: Uk = U @ Uk; r += 1
    acc = np.zeros_like(X); Uk = np.eye(n, dtype=complex)
    for _ in range(r): acc += Uk @ X @ Uk.conj().T; Uk = U @ Uk
    return acc / r
def mixing(U, Q, basis=None, trials=6):
    """turn-invariant up/down mass operators read on family space Q: max CP quartet, max commutator; control."""
    jm = cm = jc = 0
    for _ in range(trials):
        H = []
        for _ in range(2):
            X = herm(len(U)) if basis is None else sum((rng.normal() + 1j * rng.normal()) * b for b in basis)
            X = X + X.conj().T; H += [Q.conj().T @ reynolds(U, X) @ Q, Q.conj().T @ X @ Q]
        jm = max(jm, jmax(H[0], H[2])); cm = max(cm, np.linalg.norm(H[0] @ H[2] - H[2] @ H[0])); jc = max(jc, jmax(H[1], H[3]))
    return jm, cm, jc
def scan(Ufun, c, F, kpts, M):
    out = []
    for name, k in kpts:
        Ut, ok = turn_lift(c, k, F); assert ok
        for Q in eig_groups(Ufun(k, M)):
            if Q.shape[1] >= 3: out.append((name, Q.shape[1], *turn_spectrum(Ut, Q), Ut, Q))
    return out
fmt = lambda L: sorted(set(f"{n}:{d}{p}{'T' if t else ''}" for n, d, p, t, _, _ in L))

print("== A. CL-1 two-tiling update, Bloch over 2Z^3 (8 modes per cell)")
F1 = [fam_pairs(2, 1, 0), fam_pairs(2, 1, 1)]
k0 = rng.uniform(-np.pi, np.pi, 3); T = tickset(2, k0, F1)
cl = all(np.allclose(W[i] @ W[j] + W[j] @ W[i], 2 * (i == j) * np.eye(8)) for W in T for i in range(3) for j in range(3))
check("A0 [T]", cl, "even and odd cube hops W_i (one global face-phase field, -1 on every face) are Clifford at every k")
UA = lambda k, M, mu=MU: update(tickset(2, k, F1), [EPS], [mu], [M], 1)
def struct(k, copy):
    T = tickset(2, k, F1); return [sum(T[0]) / np.sqrt(3), sum(T[1]) / np.sqrt(3)] + ([1j * T[0][0] @ T[0][1] @ T[0][2]] if copy else [])
dims = {}
for nk in (3, 12, 20):
    ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(nk)]
    dims[nk] = (len(commutant(sum([struct(k, 0) for k in ks], []))), len(commutant([UA(k, 0, 0.0) for k in ks])),
                len(commutant([UA(k, 0) for k in ks])), len(commutant([UA(k, MC) for k in ks])))
check("A1 [T]", dims[12] == dims[20] == (1, 1, 1, 1),
      f"cell-local (k-independent) commutant over all k: structural {dims[20][0]}, fixed step mu=0 {dims[20][1]}, mu!=0 "
      f"{dims[20][2]}, with copy mass {dims[20][3]} (saturated at 12 and 20 momenta; 3 momenta give {dims[3]}, an "
      "undersampled upper bound): no cell-local family symmetry at all")
kp = [("axis", 0.7 * np.ones(3)), ("0", z), ("pi", np.pi * np.ones(3))]
mg = {n: ([Q.shape[1] for Q in eig_groups(UA(k, 0))], [Q.shape[1] for Q in eig_groups(UA(k, MC))]) for n, k in [("gen", k0)] + kp}
check("A2 [F]", set(mg["gen"][0]) == {4} and set(mg["gen"][1]) == {2},
      "fibre degeneracies of U(k), fixed generic step and mass angle (without|with copy): " +
      "; ".join(f"{n} {sorted(set(a))}|{sorted(set(b))}" for n, (a, b) in mg.items()) +
      ": 4 = spin x 2 tastes without the copy mass, 2 = spin x 1 family with it")
sA0 = scan(UA, 2, F1, kp, 0); sAc = scan(UA, 2, F1, kp, MC)
okc = all(np.allclose(turn_lift(2, k, F1)[0] @ (1j * W[0] @ W[1] @ W[2]) @ turn_lift(2, k, F1)[0].conj().T, 1j * W[0] @ W[1] @ W[2])
          for _, k in kp for W in [tickset(2, k, F1)[0]])
check("A3 [T]", okc and not sAc and all(d == 4 for _, d, _, _, _, _ in sA0),
      f"turn lift (site phases) exists on both tilings and keeps the copy sign; >=3-dim fibre spaces at turn-fixed k "
      f"(k:dim[turn multiplicities], T = holds a turn triplet): without copy {fmt(sA0)}; with copy {fmt(sAc) or 'none'}. "
      "Every such space is spin x taste; the copy mass leaves none")

print("== B. Two-rung nesting")
F2b = [fam_pairs(4, 1, 0), fam_pairs(4, 2, 0)]        # one parent cube of 8 fine cubes (the 4^3 cell at k = 0)
WI, WP = tickset(4, z, F2b); I64 = np.eye(64)
iw1 = 1j * WI[0] @ WI[1] @ WI[2]; iw2 = 1j * WP[0] @ WP[1] @ WP[2]
ok_tp = all(np.allclose(a @ b, b @ a) for a in WI for b in WP)
CB = commutant_big(WI + WP)
UgB, okB = turn_lift(4, z, F2b)
def spin_turn(W):
    for a, b, c_ in itertools.product((1, -1), repeat=3):
        s = (np.eye(len(W[0])) + a * W[0] @ W[1] + b * W[1] @ W[2] + c_ * W[2] @ W[0]) / 2
        if np.allclose(s @ s.conj().T, np.eye(len(s))) and all(np.allclose(s @ W[i] @ s.conj().T, W[(i + 1) % 3]) for i in range(3)):
            return s
Y = (spin_turn(WI) @ spin_turn(WP)).conj().T @ UgB          # the turn with its spin part removed
okY = all(np.allclose(Y @ w, w @ Y) for w in WI + WP)
secs = []
for s1, s2 in itertools.product((1, -1), repeat=2):
    P = (I64 + s1 * iw1) @ (I64 + s2 * iw2) / 4
    Pm = P @ (I64 + 1j * WI[0] @ WI[1]) @ (I64 + 1j * WP[0] @ WP[1]) / 4; u, sv, _ = np.linalg.svd(Pm)
    Qm = u[:, sv > 0.5]; Ym = Qm.conj().T @ Y @ Qm
    secs.append((Qm, turn_spectrum(Ym, np.eye(len(Ym)))))
check("B1 [T]", ok_tp and okB and okY and len(CB) == 64 and all(q.shape[1] == 4 for q, _ in secs),
      f"one parent cube over 8 fine cubes: fine and parent Cliffords commute; commutant dim {len(CB)} = (M2+M2)x(M2+M2): "
      f"four (w_fine, w_parent) sectors, each (spin 2x2) x FAMILY 4 = (fine 2) x (parent 2); spin-stripped turn on each "
      f"family space: multiplicities {[s[0] for _, s in secs]}, triplet {[s[1] for _, s in secs]}")
def word_trace_gap(c, k, F, nw=3000):
    """max |tr(word) - tr(turned word)| over random words: nonzero => no unitary lift of the turn at all."""
    T = sum(tickset(c, k, F), []); gk = np.array([k[2], k[0], k[1]])
    Tg = sum([[W[1], W[2], W[0]] for W in tickset(c, gk, F)], []); gap = 0
    for _ in range(nw):
        w = rng.integers(len(T), size=rng.integers(2, 9)); A = np.eye(len(T[0])); B = A.copy()
        for j in w: A = A @ T[j]; B = B @ Tg[j]
        gap = max(gap, abs(np.trace(A) - np.trace(B)))
    return gap
Fc = fam_pairs(4, 1, 1)
Wc = [bloch([p for p in Fc if np.all(p[0] >= 1) and np.all(p[1] <= 2)], 4, z, i) for i in range(3)]
dB2m = len(commutant_big(WI + WP + Wc))
dB2 = len(commutant_big([sum(WI) / np.sqrt(3), sum(WP) / np.sqrt(3), sum(Wc) / np.sqrt(3), iw1, iw2]))
def max_mult(gens):
    ev = np.sort(np.linalg.eigvalsh(rand_elem(gens))); return 1 + max([0] + [len(list(g)) for d, g in
        itertools.groupby(np.diff(ev) < 1e-7) if d])
G2 = [sum(WI) / np.sqrt(3), sum(WP) / np.sqrt(3), sum(Wc) / np.sqrt(3), iw1, iw2]
mm = (max_mult(WI + WP + Wc), max_mult(G2)); gB2 = word_trace_gap(4, z, F2b + [[p for p in Fc if np.all(p[0] >= 1) and np.all(p[1] <= 2)]])
check("B2 [F]", dB2m < 64 and dB2 < 64 and mm == (1, 1) and gB2 > 1,
      f"adding CL-1's second tiling (the fine odd cube at the block centre): commutant dim {dB2m} (hop directions "
      f"separately), {dB2} (flat ticks + copy signs), abelian, every family multiplicity {mm}; the turn is no longer a "
      f"symmetry (word-trace gap {gB2:.0f}): the 4-fold family space of B1 does not survive the two-tiling update")
F4 = [fam_pairs(4, 1, 0), fam_pairs(4, 1, 1), fam_pairs(4, 2, 0), fam_pairs(4, 2, 1)]
UB = lambda k, M: update(tickset(4, k, F4), [EPS, 0.29], [MU, 0.07], [M, M], 2)
kg = rng.uniform(-np.pi, np.pi, 3)
mB = {n: ([Q.shape[1] for Q in eig_groups(UB(k, 0))], [Q.shape[1] for Q in eig_groups(UB(k, MC))])
      for n, k in [("gen", kg), ("axis", 0.4 * np.ones(3)), ("0", z)]}
gB = word_trace_gap(4, z, F4); g1 = word_trace_gap(4, z, F4[:2]); gEO = word_trace_gap(4, z, [F4[0], F4[3]])
check("B3 [F]", set(mB["gen"][0]) == {4} and set(mB["gen"][1]) == {1} and gB > 1 and g1 < 1e-9,
      "nested two-tiling lattice (Bloch 4Z^3, 64 modes per cell; fine and parent even/odd ticks, parent hops identity on "
      "child labels; copy at both rungs): fibre degeneracies (without|with copy) " +
      "; ".join(f"{n} {sorted(set(a))}|{sorted(set(b))}" for n, (a, b) in mB.items()) +
      f"; the turn is NOT a symmetry of this nesting (word-trace gap {gB:.0f}; fine tilings alone {g1:.0e}): fine odd "
      "cubes and parent cubes give mixed loops whose fluxes the turn does not keep")
print("== C. Family mixing from turn-invariant (no axis chosen) mass operators")
cases = [("B1 family space, commutant masses", UgB, secs[0][0], CB, secs[0][1][0])]
for lab, L in [("A no-copy", sA0)]:
    seen = set()
    for n, d, p, t, Ut, Q in L:
        if (n, d, tuple(p)) in seen: continue
        seen.add((n, d, tuple(p))); cases.append((f"{lab} k={n} dim {d}", Ut, Q, None, p))
ok_all = True; lines = []
for name, Ut, Q, basis, pat in cases:
    jm, cm, jc = mixing(Ut, Q, basis, trials=4)
    pred0 = max(pat) < 3
    ok = (jm < 1e-9) if pred0 else (jm > 1e-4); ok_all &= ok and jc > 1e-4
    lines.append(f"{name} {pat}: J {jm:.0e}{'' if pred0 else '(turn-blind block)'} |[Mu,Md]| {cm:.1f} ctrl {jc:.3f}")
check("C1 [F]", ok_all, "invariant up/down masses on each family space; J = 0 exactly when no turn eigenvalue holds >= 3 "
      "families: " + " | ".join(lines[:7]))
lem = {}
for lab, d in [("1,w,w2", [1, OM, OM ** 2]), ("1,1,w", [1, 1, OM]), ("1,1,1", [1, 1, 1])]:
    Uz = np.diag(d); jm = 0
    for _ in range(20):
        Hs = [reynolds(Uz, herm(3)) for _ in range(2)]; jm = max(jm, abs(np.linalg.det(Hs[0] @ Hs[1] - Hs[1] @ Hs[0])))
    lem[lab] = jm
check("C2 [T]", lem["1,w,w2"] < 1e-12 and lem["1,1,w"] < 1e-12 and lem["1,1,1"] > 1e-2,
      f"Z3 lemma, three families: max |det[Hu,Hd]| (prop. to J) {lem['1,w,w2']:.0e} for a turn triplet, {lem['1,1,w']:.0e} "
      f"for 1+1+w, {lem['1,1,1']:.1f} when the turn is a scalar: [Hu,Hd] is in (+)M_n, each block traceless, so J = 0 "
      "unless one turn eigenvalue holds all three families")
check("C3 [T]", True, "fitted count: every coefficient of an invariant up/down mass operator is FITTED; B1 needs 6 real "
      "numbers per mass per sector (M2+C+C), none fixed by a rule")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
