"""A37 t3: (1) clashes between two records whose PUSH regions overlap; (2) where the stepped-into content goes,
as seen by later records that are compared with a distant linked partner.  Supplied 1D toys (5 and 6 qubits).

(1) Sites q0 = A (record, content rA), q1 = y1, q2 = y2, q3 = B (record, content rB), q4 = b (distant).
    y1 is Bell-linked with b.  A pushes right (capped push PL1: A -> y1, y1 -> y2, y2 -> A's old site);
    B pushes left (B -> y2, y2 -> y1, y1 -> B's old site).  The targets differ, but the push regions overlap.
    Rules: 'literal'  = independent claims at y1 and y2; if both accepted, A wins with odds wA/(wA+wB) computed
                        from the actual state (nonlinear);
           'uniform'  = same, ties broken by a fair coin (odds-blind);
           'joint'    = ONE instrument on (y1,y2) with outcomes A-goes / B-goes / neither,
                        E_A = (c/2) W_A(y1), E_B = (c/2) W_B(y2), E_none = 1 - E_A - E_B.
    b's distant choice: no record / record with menu Z / menu X (outcome unread).  Signalling = TV of the record
    law across b's choices.
(2) Sites x (record, content |0>), y, y+1, y+2, y+3, b; y Bell-linked with b, others in the emptiness |1>.
    The record steps x -> y under each rule; then Z-records (and, separately, X-records) at each site are compared
    with the same kind of record at b: P(agree), and the mutual information I(site : b).
"""
import signal, itertools
import numpy as np
signal.alarm(55)
I2 = np.eye(2)
k0 = np.array([1.0, 0]); k1 = np.array([0, 1.0]); kp = (k0 + k1) / np.sqrt(2); km = (k0 - k1) / np.sqrt(2)

def op_on(ops, N):
    out = np.array([[1.0 + 0j]])
    for k in range(N):
        out = np.kron(out, ops.get(k, I2))
    return out

def perm_op(pi, N):
    """Qubit at site i moves to site pi[i] (pi a permutation dict)."""
    Dm = 2 ** N; P = np.zeros((Dm, Dm))
    for bb in range(Dm):
        bits = [(bb >> (N - 1 - k)) & 1 for k in range(N)]
        nb = [0] * N
        for i in range(N):
            nb[pi[i]] = bits[i]
        P[sum(bit << (N - 1 - k) for k, bit in enumerate(nb)), bb] = 1
    return P

def sqrtm_psd(A):
    w, V = np.linalg.eigh(A)
    return (V * np.sqrt(np.clip(w, 0, None))) @ V.conj().T

def red1(rho, keep, N):
    t = rho.reshape([2] * (2 * N))
    ii = list(range(2 * N))
    for i in range(N):
        if i != keep:
            ii[i + N] = ii[i]
    return np.einsum(t, ii, [keep, keep + N])

# ---------------------------------------------------------------- (1) clashes
N = 5
alpha, beta, c = 0.15, 0.85, 0.9
rA, rB = k0, kp
G = lambda r: beta * I2 + (alpha - beta) * np.outer(r, r)
bell = (np.kron(k0, k0) + np.kron(k1, k1)) / np.sqrt(2)          # (y1, b)
psi = np.einsum("a,bf,c,d->abcdf", rA, bell.reshape(2, 2), k1, rB).reshape(-1)
rho0 = np.outer(psi, psi.conj())
PUSH_A = perm_op({0: 1, 1: 2, 2: 0, 3: 3, 4: 4}, N)   # record A: q0 -> q1; y1 content -> q2; y2 content -> q0
PUSH_B = perm_op({3: 2, 2: 1, 1: 3, 0: 0, 4: 4}, N)   # record B: q3 -> q2; y2 content -> q1; y1 content -> q3
EA1 = (c / 2) * G(rA); EB1 = (c / 2) * G(rB)

def after_choice(rho, choice):
    if choice == "none":
        return [(1.0, rho)]
    basis = (k0, k1) if choice == "Z" else (kp, km)
    out = []
    for v in basis:
        P = op_on({4: np.outer(v, v)}, N)
        s = P @ rho @ P; w = np.real(np.trace(s))
        out.append((w, s / w))
    return out

def law(rule, rho):
    """Record law {('A'|'B'|'-')} for one tick."""
    if rule == "joint":
        EA = op_on({1: EA1}, N); EB = op_on({2: EB1}, N)
        En = np.eye(2 ** N) - EA - EB
        assert np.linalg.eigvalsh(En).min() > -1e-12
        return {"A": np.real(np.trace(EA @ rho)), "B": np.real(np.trace(EB @ rho)), "-": np.real(np.trace(En @ rho))}
    wA = np.real(np.trace(G(rA) @ red1(rho, 1, N))); wB = np.real(np.trace(G(rB) @ red1(rho, 2, N)))
    q = wA / (wA + wB) if rule == "literal" else 0.5
    out = {"A": 0.0, "B": 0.0, "-": 0.0}
    for a, b_ in itertools.product([True, False], repeat=2):
        Ea = EA1 if a else I2 - EA1; Eb = EB1 if b_ else I2 - EB1
        p = np.real(np.trace(op_on({1: Ea, 2: Eb}, N) @ rho))
        if a and b_:
            out["A"] += q * p; out["B"] += (1 - q) * p
        elif a:
            out["A"] += p
        elif b_:
            out["B"] += p
        else:
            out["-"] += p
    return out

def avg_law(rule, choice):
    tot = {"A": 0.0, "B": 0.0, "-": 0.0}
    for w, s in after_choice(rho0, choice):
        for k, v in law(rule, s).items():
            tot[k] += w * v
    return tot

def tv(l1, l2):
    return 0.5 * sum(abs(l1[k] - l2[k]) for k in l1)

print("(1) two records whose capped pushes overlap (different targets, shared push region); b Bell-linked with y1")
for rule in ["literal", "uniform", "joint"]:
    L = {ch: avg_law(rule, ch) for ch in ["none", "Z", "X"]}
    print(f"   {rule:8s} law(no choice) A {L['none']['A']:.6f} B {L['none']['B']:.6f} neither {L['none']['-']:.6f}; "
          f"TV none/Z {tv(L['none'], L['Z']):.2e}, none/X {tv(L['none'], L['X']):.2e}, Z/X {tv(L['Z'], L['X']):.2e}")
wA = np.real(np.trace(G(rA) @ red1(rho0, 1, N))); wB = np.real(np.trace(G(rB) @ red1(rho0, 2, N)))
Lj = avg_law("joint", "none")
print(f"   joint rule: P(A goes | someone goes) = {Lj['A']/(Lj['A']+Lj['B']):.6f}; relative odds wA/(wA+wB) = {wA/(wA+wB):.6f}")
# a non-symmetric check of the relative odds: y2 holds a state with a different overlap with rB
for th in (0.3, 1.1):
    v2 = np.cos(th) * k0 + np.sin(th) * k1
    ps = np.einsum("a,bf,c,d->abcdf", rA, bell.reshape(2, 2), v2, rB).reshape(-1)
    rr = np.outer(ps, ps.conj())
    la = law("joint", rr)
    wa = np.real(np.trace(G(rA) @ red1(rr, 1, N))); wb = np.real(np.trace(G(rB) @ red1(rr, 2, N)))
    print(f"   joint rule, y2 = cos({th})|0>+sin({th})|1>: P(A | someone) = {la['A']/(la['A']+la['B']):.6f}, "
          f"wA/(wA+wB) = {wa/(wa+wb):.6f}")
# completeness of the joint instrument with the pushes applied
EA = op_on({1: EA1}, N); EB = op_on({2: EB1}, N)
KA = PUSH_A @ sqrtm_psd(EA); KB = PUSH_B @ sqrtm_psd(EB); Kn = sqrtm_psd(np.eye(2 ** N) - EA - EB)
print(f"   joint instrument completeness error {np.abs(KA.conj().T @ KA + KB.conj().T @ KB + Kn.conj().T @ Kn - np.eye(2**N)).max():.1e}")

# ---------------------------------------------------------------- (2) where the stepped-into content goes
N2 = 6      # q0 = x (record), q1 = y, q2 = y+1, q3 = y+2, q4 = y+3, q5 = b
psi2 = np.einsum("a,bf,c,d,e->abcdef", k0, bell.reshape(2, 2), k1, k1, k1).reshape(-1)
rho2 = np.outer(psi2, psi2.conj())
emp = np.outer(k1, k1)
def channel(rule, rho):
    """Post-step state (record now at q1).  Returns rho on the same 6 qubits (q1 holds the record content |0>)."""
    if rule == "SW":
        P = perm_op({0: 1, 1: 0, 2: 2, 3: 3, 4: 4, 5: 5}, N2); return P @ rho @ P.T
    if rule == "PL1":
        P = perm_op({0: 1, 1: 2, 2: 0, 3: 3, 4: 4, 5: 5}, N2); return P @ rho @ P.T
    if rule == "PL2":
        P = perm_op({0: 1, 1: 2, 2: 3, 3: 0, 4: 4, 5: 5}, N2); return P @ rho @ P.T
    if rule in ("Pwin", "PF"):
        # Pwin: window version of the line conveyor: y->y+1->y+2->y+3, y+3's content discarded, fresh emptiness at x
        # PF: y's content discarded, fresh emptiness at x
        if rule == "Pwin":
            P = perm_op({0: 1, 1: 2, 2: 3, 3: 4, 4: 0, 5: 5}, N2)    # y+3's content lands on q0, then is reset
        else:
            P = perm_op({0: 1, 1: 0, 2: 2, 3: 3, 4: 4, 5: 5}, N2)    # y's content lands on q0, then is reset
        r = P @ rho @ P.T
        t = r.reshape([2] * 12)
        red = np.einsum(t, [0] + list(range(1, 6)) + [0] + list(range(7, 12)), list(range(1, 6)) + list(range(7, 12)))
        red = red.reshape(2 ** 5, 2 ** 5)
        return np.kron(emp, red)
    if rule == "PA":
        # push the train of non-emptiness at y up to the first emptiness; implemented as a train-length measurement
        out = np.zeros_like(rho)
        Pe = np.outer(k1, k1); Pn = np.outer(k0, k0)
        # train length 0: y holds emptiness -> nothing pushed; y's (emptiness) content is overwritten, x gets emptiness
        K0 = perm_op({0: 1, 1: 0, 2: 2, 3: 3, 4: 4, 5: 5}, N2) @ op_on({1: Pe}, N2)
        # train length 1: y non-empty, y+1 empty -> y's content to y+1, the emptiness at y+1 goes to x
        K1 = perm_op({0: 1, 1: 2, 2: 0, 3: 3, 4: 4, 5: 5}, N2) @ op_on({1: Pn, 2: Pe}, N2)
        # longer trains (cannot occur here: y+1 is emptiness) kept for completeness
        K2 = perm_op({0: 1, 1: 2, 2: 3, 3: 0, 4: 4, 5: 5}, N2) @ op_on({1: Pn, 2: Pn, 3: Pe}, N2)
        K3 = perm_op({0: 1, 1: 2, 2: 3, 3: 4, 4: 0, 5: 5}, N2) @ op_on({1: Pn, 2: Pn, 3: Pn}, N2)
        comp = sum(K.T @ K for K in (K0, K1, K2, K3))
        assert np.abs(comp - np.eye(2 ** N2)).max() < 1e-12
        return sum(K @ rho @ K.T for K in (K0, K1, K2, K3))
    raise ValueError(rule)

def pair_red(rho, i, j, N):
    t = rho.reshape([2] * (2 * N))
    keep = [i, j]
    ii = list(range(2 * N))
    for k in range(N):
        if k not in keep:
            ii[k + N] = ii[k]
    return np.einsum(t, ii, [i, j, i + N, j + N]).reshape(4, 4)

def ent(r):
    w = np.linalg.eigvalsh(r); w = w[w > 1e-14]; return float(-(w * np.log2(w)).sum())

def agree(r2, basis):
    P = 0.0
    for v in basis:
        Pv = np.kron(np.outer(v, v), np.outer(v, v))
        P += np.real(np.trace(Pv @ r2))
    return P

names = {0: "x", 2: "y+1", 3: "y+2", 4: "y+3"}
print("(2) record steps x -> y; y was Bell-linked with b.  P(Z-records agree with b), P(X-records agree), I(site:b) bits")
for rule in ["SW", "PL1", "PL2", "Pwin", "PA", "PF"]:
    r = channel(rule, rho2)
    cells = []
    for s in (0, 2, 3, 4):
        r2 = pair_red(r, s, 5, N2)
        I = (ent(np.einsum("ijkj->ik", r2.reshape(2, 2, 2, 2))) +
             ent(np.einsum("ijil->jl", r2.reshape(2, 2, 2, 2))) - ent(r2))
        cells.append(f"{names[s]}: Z {agree(r2, (k0, k1)):.3f} X {agree(r2, (kp, km)):.3f} I {I:.3f}")
    print(f"   {rule:4s} " + " | ".join(cells) + f"   (global purity {np.real(np.trace(r @ r)):.3f})")
