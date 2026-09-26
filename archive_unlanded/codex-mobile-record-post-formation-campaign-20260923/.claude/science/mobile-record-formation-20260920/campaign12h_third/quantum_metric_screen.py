#!/usr/bin/env python3
"""Exploratory floating-point contraction test for the frozen two-pair code.

This is an author screen, not an exact certificate or an independent check.
All declared sizes and both transverse profile orientations are reported.
"""
from pathlib import Path
import datetime, hashlib, itertools, json, math
import numpy as np

HERE = Path(__file__).resolve().parent

def construct():
    group = []
    for p in itertools.permutations(range(3)):
        parity = (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
        for signs in itertools.product((-1, 1), repeat=3):
            if parity * math.prod(signs) != 1:
                continue
            R = np.zeros((3, 3), dtype=int)
            for i in range(3):
                R[i, p[i]] = signs[i]
            U = np.zeros((4, 4), dtype=int)
            U[0, 0] = 1
            U[1:, 1:] = R
            group.append((R, np.kron(U, U)))
    labels = [(0, np.eye(3, dtype=int)[i] * s) for i in range(3) for s in (1, -1)]
    labels += [(1, np.array(b)) for b in itertools.product((-1, 1), repeat=3)]
    starts = [np.array([1, 0, 0]), np.ones(3, dtype=int)]
    seeds = [np.array([(7*i*i+3*i+5)%17-8 for i in range(16)]),
             np.array([(11*i**3+4*i+1)%19-9 for i in range(16)])]
    matrices = []
    for origin, v in zip(starts, seeds):
        terms = [V @ v for R, V in group if np.array_equal(R @ origin, origin)]
        matrices.append(np.eye(16, dtype=int) + sum(np.outer(w, w) for w in terms))
    rho = []
    for orbit, label in labels:
        V = next(V for R, V in group if np.array_equal(R @ starts[orbit], label))
        M = V @ matrices[orbit] @ V.T
        rho.append(M / np.trace(M))
    return labels, np.array(rho)

def main():
    labels, rho = construct()
    tau = np.mean(rho, axis=0)
    inverse = np.linalg.inv(tau)
    vx = np.array([float(z[1][1])/2 if z[0] == 0 else 0 for z in labels])
    vy = np.array([float(z[1][2])/8 if z[0] == 1 else 0 for z in labels])
    dx = np.einsum('a,aij->ij', vx, rho)
    dy = np.einsum('a,aij->ij', vy, rho)
    u = np.trace(dx @ inverse @ dx)
    v = np.trace(dy @ inverse @ dy)
    cross = np.trace(dx @ inverse @ dy)
    k0 = 1.1
    gamma = 1.
    scans = []
    for N in [8, 12, 16, 24, 32, 48, 64, 96, 128, 256, 512, 1024]:
        k = 2 * np.pi / N
        damping = k0 * (1-np.cos(2*k)+4*(1-np.cos(k)))
        g = gamma * (np.sin(4*k)-np.sin(2*k)) / 14
        M = -damping * np.eye(2) - 1j*g*np.array([[0,1],[4,0]])
        H = np.array([[u,cross],[cross,v]])
        criterion = H @ M + M.conj().T @ H
        scans.append(dict(N=N, microscopic_k=k, damping=damping, antisymmetric=g,
                          contraction_eigenvalues=np.linalg.eigvalsh(criterion).tolist(),
                          equal_amplitude_profile_derivatives=[float(-damping*(u+v)+s*g*(u-4*v)) for s in [-1,1]]))
    out = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               status='exploratory_float_screen', code='Frozen positive two-pair stabilizer construction; author recreation',
               minimum_tau_eigenvalue=float(np.linalg.eigvalsh(tau)[0]),
               local_chi_squared_metric={'X2_X2':float(u),'Y3_Y3':float(v),'X2_Y3':float(cross),'mismatch_u_minus_4v':float(u-4*v)},
               rates={'k0':k0,'gamma':gamma},scan=scans,
               scope='Necessary quantum contraction test using the proposed full generator linearization at the uniform encoded product law. Exact proof, microscopic linearization verification and independent review remain pending.',
               script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'QUANTUM_METRIC_SCREEN_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    main()
