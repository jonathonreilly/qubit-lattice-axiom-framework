#!/usr/bin/env python3
"""Local fibre-frame redundancy bridge for the minimal-coupling lane.

This runner checks a finite operator-algebra bridge used by

    docs/FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md

Claim scope:
  On the current graph-first SU(3) / tensor-product hopping surface, a local
  U(3) change of fibre basis is a passive trivialization change for the
  registered weak-sector and Record-sector data currently present in the
  cited authorities. The flat U=I hopping reference is therefore a choice of
  cross-site trivialization, not a canonical physical pinning of fibre bases.

Non-claims:
  The runner does not derive gauge action/dynamics, physical SU(3)_c
  identification, a Born/measurement rule, or a future theorem saying every
  possible color readout is unregistered. It only checks the current-surface
  finite algebra needed by the kinematic minimal-coupling source note.
"""

from __future__ import annotations

import itertools
from pathlib import Path
import numpy as np

PASS = 0
FAIL = 0
ATOL = 1e-10


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def unitary_from_hermitian(H: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eigh(H)
    return v @ np.diag(np.exp(1j * w)) @ v.conj().T


def random_u3(rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    h = z + z.conj().T
    return unitary_from_hermitian(h)


def block_diag(blocks: list[np.ndarray]) -> np.ndarray:
    n = sum(b.shape[0] for b in blocks)
    out = np.zeros((n, n), dtype=complex)
    k = 0
    for b in blocks:
        m = b.shape[0]
        out[k : k + m, k : k + m] = b
        k += m
    return out


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def hopping_two_site(link: np.ndarray) -> np.ndarray:
    """Two-site single-particle hopping with internal block `link`.

    Site 0 <- site 1 carries `link`; the Hermitian conjugate carries link^dag.
    """
    n = link.shape[0]
    h = np.zeros((2 * n, 2 * n), dtype=complex)
    h[:n, n:] = link
    h[n:, :n] = link.conj().T
    return h


def invariant_fibre_dimension() -> int:
    """Dimension of fibre matrices commuting with the full u(3) generator set."""
    e = []
    for i, j in itertools.product(range(3), repeat=2):
        m = np.zeros((3, 3), dtype=complex)
        m[i, j] = 1.0
        e.append(m)

    generators: list[np.ndarray] = [np.eye(3, dtype=complex)]
    # Hermitian matrix-unit basis for u(3).
    for i in range(3):
        m = np.zeros((3, 3), dtype=complex)
        m[i, i] = 1.0
        generators.append(m)
    for i in range(3):
        for j in range(i + 1, 3):
            s = np.zeros((3, 3), dtype=complex)
            s[i, j] = s[j, i] = 1.0
            a = np.zeros((3, 3), dtype=complex)
            a[i, j] = -1j
            a[j, i] = 1j
            generators.extend([s, a])

    rows = []
    for gen in generators:
        for basis in e:
            c = commutator(basis, gen)
            rows.append(c.reshape(-1))
    # We want all coefficient vectors x with sum_i x_i [E_i, gen] = 0.
    # Build the linear map column-wise.
    cols = []
    for basis in e:
        pieces = [commutator(basis, gen).reshape(-1) for gen in generators]
        cols.append(np.concatenate(pieces))
    mat = np.stack(cols, axis=1)
    rank = np.linalg.matrix_rank(mat, tol=1e-10)
    return 9 - rank


print("=" * 78)
print("Local fibre-frame redundancy bridge: current-surface finite algebra")
print("=" * 78)

rng = np.random.default_rng(20260609)

I2 = np.eye(2, dtype=complex)
I3 = np.eye(3, dtype=complex)
I6 = np.eye(6, dtype=complex)

sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
weak_ops = [np.kron(s, I3) for s in (sx, sy, sz)]

u0 = random_u3(rng)
u1 = random_u3(rng)
g0 = np.kron(I2, u0)
g1 = np.kron(I2, u1)
G = block_diag([g0, g1])

print("\nPart 1. Frame rotations commute with current registered weak-sector data")
check("site-0 fibre frame rotation is unitary", np.allclose(g0.conj().T @ g0, I6, atol=ATOL))
check("site-1 fibre frame rotation is unitary", np.allclose(g1.conj().T @ g1, I6, atol=ATOL))
check(
    "local U(3) fibre rotations commute with graph-first weak su(2) generators",
    all(np.allclose(commutator(g0, w), 0, atol=ATOL) for w in weak_ops)
    and all(np.allclose(commutator(g1, w), 0, atol=ATOL) for w in weak_ops),
    "G_x = I_weak tensor u_x",
)

p_up = np.kron(np.array([[1, 0], [0, 0]], dtype=complex), I3)
p_dn = np.kron(np.array([[0, 0], [0, 1]], dtype=complex), I3)
check("weak central-sector projectors are fixed by fibre-frame rotations",
      np.allclose(g0 @ p_up @ g0.conj().T, p_up, atol=ATOL)
      and np.allclose(g0 @ p_dn @ g0.conj().T, p_dn, atol=ATOL))
check("finite Record-sector scalar additivity is unchanged on these projectors",
      int(round(np.trace(p_up).real)) + int(round(np.trace(p_dn).real)) == int(round(np.trace(I6).real)),
      "rank(P_up)+rank(P_down)=rank(I)")

print("\nPart 2. No fibre-basis vector is selected by the current U(3)-invariant surface")
dim_inv = invariant_fibre_dimension()
check("only scalar fibre operators commute with the full local U(3) frame group",
      dim_inv == 1,
      f"invariant fibre-operator dimension={dim_inv}")
e00 = np.diag([1.0, 0.0, 0.0]).astype(complex)
perm = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)
check("a candidate colour/fibre basis projector is not U(3)-invariant",
      not np.allclose(perm @ e00 @ perm.conj().T, e00, atol=ATOL),
      "basis colour labels would add extra structure")

print("\nPart 3. The retained U=I hopping is a flat trivialization, not a local-frame invariant")
h_flat = hopping_two_site(I6)
flat_link_after_local_frame = g0 @ I6 @ g1.conj().T
h_flat_rewritten = hopping_two_site(flat_link_after_local_frame)
check("local basis changes rewrite the identity link as g_x g_y^dag, generally not I",
      not np.allclose(flat_link_after_local_frame, I6, atol=1e-8))
check("same local basis change maps H[U=I] to H[U'=g_x g_y^dag]",
      np.allclose(G @ h_flat @ G.conj().T, h_flat_rewritten, atol=ATOL))
check("global fibre rotations leave the flat identity link fixed",
      np.allclose(g0 @ I6 @ g0.conj().T, I6, atol=ATOL))

print("\nPart 4. General link transporters are the coordinate form of cross-site comparison")
u_link = np.kron(I2, random_u3(rng))
h_link = hopping_two_site(u_link)
u_link_prime = g0 @ u_link @ g1.conj().T
h_link_prime = hopping_two_site(u_link_prime)
check("transformed link remains unitary",
      np.allclose(u_link_prime.conj().T @ u_link_prime, I6, atol=ATOL))
check("passive frame covariance: G H[U] G^dag = H[g_x U g_y^dag]",
      np.allclose(G @ h_link @ G.conj().T, h_link_prime, atol=ATOL))
check("the check is nontrivial: the sampled local frames are not equal",
      not np.allclose(g0, g1, atol=1e-8))
check("sampled link differs from identity",
      not np.allclose(u_link, I6, atol=1e-8))

print("\nPart 5. Guardrails")
note_text = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md"
).read_text(encoding="utf-8")
check("source note disclaims gauge action or dynamics",
      "No Yang-Mills/Wilson gauge action or gauge-field dynamics." in note_text)
check("source note disclaims physical SU(3)_c identification",
      "No physical `SU(3)_c` identification beyond the graph-first algebraic fibre." in note_text)
check("source note leaves future colour-readout theorems outside this bridge",
      "No theorem saying future colour-readout contexts cannot register additional" in note_text)
check("source note limits bridge role to the minimal-coupling kinematic target",
      "one-hop kinematic bridge needed by the minimal-coupling source" in note_text)

print("\nSummary")
print(f"PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
