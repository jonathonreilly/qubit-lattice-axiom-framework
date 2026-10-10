"""Lane RS / S1 item 3: exact cluster check of the natural momentum P_x = 1/2{J_x, h}
(free one-particle symbol 1/2 sin 2p_x, = (T_{2e1} - T_{2e1}^+)/(4i) up to sign)
for interacting 2D staggered fermions on Lx x Ly PBC clusters (Lx = 6: on Lx = 4 the
symbol 1/2 sin 2p vanishes identically on the allowed momenta).
Reports, vs interaction strength V:
  ||[H,P]||_op  (N-particle sector, dense),
  on-shell O(V) obstruction  ||Pi_E [H_int, P] Pi_E||  over degenerate free levels
     (the part no dressing P1, local or not, can cancel at O(V)),
  distance of P to the nearest exactly conserved operator  ||P - Pbar||/||P||,
     Pbar = sum over exact eigen-spaces Pi P Pi (time average).
"""
import numpy as np, itertools, sys
from math import comb

def one_body(Lx, Ly, m):
    sites = [(x, y) for x in range(Lx) for y in range(Ly)]
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    h = np.zeros((n, n), complex)
    for (x, y) in sites:
        s = idx[(x, y)]
        # j = 1 (x direction): eta = 1 ; j = 2 (y): eta = (-1)^x
        for (dx, dy, eta) in ((1, 0, 1), (0, 1, (-1)**x)):
            t = idx[((x+dx) % Lx, (y+dy) % Ly)]
            h[s, t] += 0.5j*eta; h[t, s] += -0.5j*eta
        h[s, s] += m*(-1)**(x+y)
    T2 = np.zeros((n, n), complex)
    for (x, y) in sites:
        T2[idx[(x, y)], idx[((x+2) % Lx, y)]] += 1
    P = (T2 - T2.conj().T)/(4j)
    return sites, idx, h, P

def nn_pairs(Lx, Ly, sites, idx, kind):
    K = {}
    if kind == 'nn':
        for (x, y) in sites:
            for (dx, dy) in ((1, 0), (0, 1)):
                a, b = idx[(x, y)], idx[((x+dx) % Lx, (y+dy) % Ly)]
                K[(min(a, b), max(a, b))] = K.get((min(a, b), max(a, b)), 0) + 1.0
    elif kind == 'cube':  # sum over all plaquettes y of (sum_{x in plaquette} n_x)^2, two-body part 2 sum_{a<b} n_a n_b
        for (x, y) in sites:
            cell = [idx[((x+dx) % Lx, (y+dy) % Ly)] for dx in (0, 1) for dy in (0, 1)]
            for a, b in itertools.combinations(cell, 2):
                K[(min(a, b), max(a, b))] = K.get((min(a, b), max(a, b)), 0) + 2.0
    return K

def fock(nsite, N):
    states = [sum(1 << i for i in c) for c in itertools.combinations(range(nsite), N)]
    return states, {s: i for i, s in enumerate(states)}

def second_quant(M, states, pos, nsite):
    D = len(states); out = np.zeros((D, D), complex)
    for col, s in enumerate(states):
        for j in range(nsite):
            if not (s >> j) & 1: continue
            for i in range(nsite):
                if M[i, j] == 0: continue
                if i != j and (s >> i) & 1: continue
                s1 = s & ~(1 << j)
                sign = (-1)**bin(s1 & ((1 << j) - 1)).count('1')
                sign *= (-1)**bin(s1 & ((1 << i) - 1)).count('1')
                s2 = s1 | (1 << i)
                out[pos[s2], col] += sign*M[i, j]
    return out

def diag_int(K, states):
    return np.diag([sum(w for (a, b), w in K.items() if (s >> a) & 1 and (s >> b) & 1) for s in states]).astype(complex)

def run(Lx, Ly, N, m, kind, Vs):
    sites, idx, h, P1 = one_body(Lx, Ly, m)
    ns = len(sites)
    c1 = np.linalg.norm(h@P1 - P1@h)
    ev = np.sort(np.linalg.eigvalsh(P1))
    print(f"\n== {Lx}x{Ly} PBC, N={N}, m={m}, interaction {kind}: one-body ||[h,P]||_F = {c1:.1e}; "
          f"P spectrum range [{ev[0]:.3f},{ev[-1]:.3f}]")
    states, pos = fock(ns, N)
    H0 = second_quant(h, states, pos, ns); P = second_quant(P1, states, pos, ns)
    Hint = diag_int(nn_pairs(Lx, Ly, sites, idx, kind), states)
    nP = np.linalg.norm(P, 2)
    # on-shell O(V) obstruction in the free eigenbasis
    e0, U0 = np.linalg.eigh(H0)
    X = U0.conj().T @ (Hint@P - P@Hint) @ U0
    same = np.abs(e0[:, None] - e0[None, :]) < 1e-9
    onshell = np.where(same, X, 0)
    print(f"  dim {len(states)}; ||P||_op {nP:.3f}; ||[H_int,P]||_op {np.linalg.norm(X, 2):.4f}; "
          f"on-shell (degenerate free levels) part ||Pi[H_int,P]Pi||_op {np.linalg.norm(onshell, 2):.4f} "
          f"(Frobenius {np.linalg.norm(onshell):.4f} of {np.linalg.norm(X):.4f})")
    for V in Vs:
        H = H0 + V*Hint
        C = H@P - P@H
        e, Uv = np.linalg.eigh(H)
        Pv = Uv.conj().T @ P @ Uv
        samev = np.abs(e[:, None] - e[None, :]) < 1e-8
        Pbar = np.where(samev, Pv, 0)
        H0v = Uv.conj().T @ H0 @ Uv; H0bar = np.where(samev, H0v, 0)
        print(f"  V={V:7.3f}: ||[H,P]||_op = {np.linalg.norm(C, 2):.4e}  ||[H,P]||_F/sqrt(dim) = {np.linalg.norm(C)/np.sqrt(len(states)):.4e}  "
              f"dist(P, commutant(H))_HS/||P||_HS = {np.linalg.norm(Pv - Pbar)/np.linalg.norm(P):.4f} (op-norm ratio {np.linalg.norm(Pv - Pbar, 2)/nP:.3f}); "
              f"control dist(H0, commutant(H))_HS/||H0||_HS = {np.linalg.norm(H0v - H0bar)/np.linalg.norm(H0):.2e}")
    sys.stdout.flush()

if __name__ == '__main__':
    Vs = [0.0, 1e-3, 1e-2, 0.05, 0.2, 1.0]
    for kind in ('nn', 'cube'):
        for m in (0.5, 0.0):
            run(6, 4, 3, m, kind, Vs)
            run(6, 4, 2, m, kind, Vs)
    run(6, 6, 2, 0.5, 'nn', Vs)
    run(8, 4, 3, 0.5, 'nn', Vs)
