#!/usr/bin/env python3
"""Coordinator's check of A37 Step 1 (quantum return flow): for ANY unitary step V: H_{W\\x} -> H_{W\\y} on a window W
(record moves x -> y), and any split W = W1 + W2 with x in W1, y in W2, the Choi-state flux
 1/2 [ I(K1:R2) - I(K2:R1) ] = 1 qubit (from y's side to x's side).
Window W = {x, y, a, b}; W1 = {x, a}, W2 = {y, b}. Inputs: H1 = {a}, H2 = {y, b}; outputs: K1 = {x, a}, K2 = {b}."""
import numpy as np
from scipy.stats import unitary_group
def entropy(rho):
    w = np.linalg.eigvalsh(rho); w = w[w > 1e-14]
    return float(-np.sum(w * np.log2(w)))
def ptrace(psi, dims, keep):
    n = len(dims); psi = psi.reshape(dims)
    keep = sorted(keep); trace = [i for i in range(n) if i not in keep]
    perm = keep + trace
    m = np.transpose(psi, perm).reshape(int(np.prod([dims[i] for i in keep])), -1)
    return m @ m.conj().T
rng = np.random.default_rng(3)
for trial in range(5):
    V = unitary_group.rvs(8, random_state=rng)          # input order (y, a, b) -> output order (x, a, b)
    # Choi: |Phi> = sum_i V|i> (x) |i>_R, R = (R_y, R_a, R_b); normalize
    psi = np.zeros((8, 8), complex)
    for i in range(8):
        psi[:, i] = V[:, i]
    psi = psi.reshape(-1) / np.sqrt(8)
    # subsystems: outputs x(0) a(1) b(2); references Ry(3) Ra(4) Rb(5)
    dims = [2]*6
    K1 = [0, 1]; K2 = [2]; R1 = [4]; R2 = [3, 5]           # R1 = refs of H1={a}; R2 = refs of H2={y,b}
    def I(A, B):
        return entropy(ptrace(psi, dims, A)) + entropy(ptrace(psi, dims, B)) - entropy(ptrace(psi, dims, A + B))
    flux = 0.5 * (I(K1, R2) - I(K2, R1))
    print("random unitary step %d: I(K1:R2) = %.4f, I(K2:R1) = %.4f, flux = %.6f qubit" % (trial, I(K1, R2), I(K2, R1), flux))
