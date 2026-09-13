#!/usr/bin/env python3
"""Small same-author refutation checks of the preceding analytical construction.

Native operators are built from computational-basis bit actions, without
importing a parent science runner. Numerical trig/dilation checks support,
but do not replace, the algebraic proof in the canonical source note.
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 180

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
import hashlib
import itertools
import json
from pathlib import Path
import time

import numpy as np
from scipy.linalg import expm

HERE = Path(__file__).resolve().parents[1]
TOL = 2e-12


class Native:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = tuple(edges)
        assert all(i < j for i, j in edges)
        self.dim = 1 << len(edges)
        self.I = np.eye(self.dim, dtype=complex)
        self.Z = [self.word(0, 1 << e) for e in range(len(edges))]
        self.B = []
        for v in range(vertices):
            mask = sum(1 << e for e, pair in enumerate(edges) if v in pair)
            self.B.append(self.word(0, mask))
        self.T = []
        for i, j in edges:
            self.T.append(.5j * self.A(i, j) @ (self.B[i] - self.B[j]))

    def word(self, xmask, zmask):
        out = np.zeros((self.dim, self.dim), dtype=complex)
        for state in range(self.dim):
            out[state ^ xmask, state] = (-1) ** ((state & zmask).bit_count())
        return out

    def A(self, i, j):
        e = self.edges.index(tuple(sorted((i, j))))
        zmask = 0
        for v, other in ((i, j), (j, i)):
            for f, pair in enumerate(self.edges):
                if v in pair and f != e:
                    neighbor = pair[1] if pair[0] == v else pair[0]
                    if neighbor < other:
                        zmask ^= 1 << f
        return (1 if i < j else -1) * self.word(1 << e, zmask)

    def cycle(self, vertices):
        out = (1j ** (len(vertices) - 1)) * self.I
        for i, j in zip(vertices[:-1], vertices[1:]):
            out = out @ self.A(i, j)
        return out


def error(a, b):
    return float(np.max(np.abs(a-b)))


def run():
    started = time.monotonic()
    checks = []

    def close(name, a, b):
        residual = error(a, b)
        assert residual < TOL, (name, residual)
        checks.append({"name": name, "max_residual": residual})

    def reject(name, a, b):
        residual = error(a, b)
        assert residual > .01, (name, residual)
        checks.append({"name": name, "negative_control_residual": residual})

    # Two adjacent squares; removing both upper horizontal edges leaves a tree.
    g = Native(6, ((0,1),(0,2),(1,3),(2,3),(2,4),(3,5),(4,5)))
    candidates = (2,5)
    protected = tuple(e for e in range(7) if e not in candidates)
    cycles = (g.cycle((1,3,2,0,1)), g.cycle((3,5,4,2,3)))
    P = (g.I+cycles[0]) @ (g.I+cycles[1]) / 4
    close("code_projector", P@P, P)
    close("code_dimension_32", np.trace(P), 32)
    H = sum(g.T[e] for e in protected)
    N = sum((g.I-b)/2 for b in g.B)
    close("protected_number_conservation", H@N, N@H)
    observables = g.B + [g.A(*g.edges[e]) for e in protected] + [H, H@H]
    instruments = []
    for cidx, (edge, S) in enumerate(zip(candidates, cycles)):
        Z = g.Z[edge]
        Y = 1j*Z@S
        close(f"cycle_{cidx}_involution", S@S, g.I)
        close(f"cycle_{cidx}_code", S@P, P)
        close(f"pulse_{cidx}_Hermitian", Y.conj().T, Y)
        close(f"pulse_{cidx}_involution", Y@Y, g.I)
        for theta in (-np.pi/6,0,np.pi/6):
            c,s = np.cos(theta/2), np.sin(theta/2)
            U = c*g.I-s*Z@S
            close(f"unitarity_{cidx}_{theta}", U.conj().T@U, g.I)
            for z in (-1,1):
                Q=(g.I+z*Z)/2
                K=Q@U
                p=(1+z*np.sin(theta))/2
                close(f"branch_amplitude_{cidx}_{theta}_{z}", K@P, (c+z*s)*Q@P)
                close(f"scalar_effect_{cidx}_{theta}_{z}", P@K.conj().T@K@P, p*P)
                residual=max(error(P@K.conj().T@O@K@P,p*P@O@P) for O in observables)
                assert residual<TOL
                checks.append({"name":f"protected_algebra_{cidx}_{theta}_{z}","max_residual":residual})
            if theta == np.pi/6:
                instruments.append(tuple(((g.I+z*Z)/2)@U for z in (-1,1)))
        U=np.cos(np.pi/12)*g.I+np.sin(np.pi/12)*Z@S
        wrong=np.cos(np.pi/12)*g.I-np.sin(np.pi/12)*Z@S
        Q=(g.I+Z)/2
        reject(f"wrong_sign_{cidx}", P@wrong.conj().T@Q@wrong@P, .75*P)
        missing=np.cos(np.pi/12)*g.I+np.sin(np.pi/12)*Z
        # This mutant acts correctly on the code; global unitarity rejects it.
        close(f"missing_cycle_agrees_on_code_{cidx}", missing@P,U@P)
        reject(f"missing_cycle_not_unitary_{cidx}",missing.conj().T@missing,g.I)
        reject(f"retired_hop_breaks_energy_{cidx}",(H+g.T[edge])@Z,Z@(H+g.T[edge]))
    history_error=0.
    for zi,zj in itertools.product(range(2), repeat=2):
        K,L=instruments[0][zi],instruments[1][zj]
        close(f"physical_history_commutation_{zi}_{zj}", K@L,L@K)
        p=(.25,.75)[zi]*(.25,.75)[zj]
        for O in observables+[g.I]:
            history_error=max(history_error,error(P@K.conj().T@L.conj().T@O@L@K@P,p*P@O@P))
        # Both old Record values have the proper sign on the outgoing branch.
        for edge,z in zip(candidates,((-1,1)[zi],(-1,1)[zj])):
            close(f"history_Record_{zi}_{zj}_{edge}",g.Z[edge]@L@K@P,z*L@K@P)
    close("complete_history_protected_algebra",history_error,0.)

    # A four-edge native square, one fuel qubit, a three-level fresh environment.
    q=Native(4,((0,1),(0,2),(1,3),(2,3)))
    S=q.cycle((0,1,3,2,0)); Z=q.Z[2]
    U=np.cos(np.pi/12)*q.I+np.sin(np.pi/12)*Z@S
    Ks=[(q.I+z*Z)@U/2 for z in (-1,1)]
    lower=np.array([[0,1],[0,0]],complex)
    P0=np.diag([1,0]);P1=np.diag([0,1])
    env=np.eye(3,dtype=complex)
    source=np.kron(np.kron(q.I,P1),np.outer(env[:,0],env[:,0]))
    B=sum(np.kron(np.kron(K,lower),np.outer(env[:,j+1],env[:,0])) for j,K in enumerate(Ks))
    V=B+B.conj().T
    close("star_partial_isometry",B.conj().T@B,source)
    close("star_nilpotent",B@B,0*B)
    close("star_cubic",V@V@V,V)
    survival=np.exp(-.37/2); beta=np.arccos(survival)
    dilation=expm(-1j*beta*V)
    close("star_unitarity",dilation.conj().T@dilation,np.eye(len(V)))
    embedded=dilation.reshape(q.dim*2,3,q.dim*2,3)
    close("channel_idle",embedded[:,0,:,0],np.kron(q.I,P0+survival*P1))
    for j,K in enumerate(Ks):
        close(f"channel_jump_{j}",embedded[:,j+1,:,0],-1j*np.sqrt(1-survival**2)*np.kron(K,lower))
    protectedH=sum(q.T[e] for e in (0,1,3))
    totalH=np.kron(protectedH,np.eye(6))
    close("collision_protected_energy",dilation@totalH,totalH@dilation)
    # The used environment permits reversal: permanence requires fresh storage.
    reject("same_collision_can_reverse_a_used_environment",source@dilation@B,0*B)
    return {"status":"passed","checks":checks,"count":len(checks),
            "seconds":time.monotonic()-started,
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "note_sha256":hashlib.sha256((HERE/'docs/NATIVE_GROWING_FORMATION_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-13.md').read_bytes()).hexdigest(),
            "scope":"same-author finite sign, history and dilation checks; no independent audit"}
