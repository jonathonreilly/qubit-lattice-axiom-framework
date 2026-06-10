#!/usr/bin/env python3
"""(e) deep-dive: is the cross-block rank degeneracy generic, and does it break the
increment dU = U(n)U(n-1)† that the whole note is built on? Plus: how widespread is the
E[dU]-is-scalar (centrality-holds) outcome across states?

If the polar decomposition of the cross block G[0:3,3:6] is rank-deficient on a branch,
then polar_u(M) = M V diag(w^-1/2) V† is ILL-DEFINED (division by ~0 eigenvalue): the
orientation in the null direction is arbitrary, so dU is not a well-defined SU/U(3)
element. The draft's polar_u uses w**-0.5 with NO guard, so it silently emits garbage.
"""
from __future__ import annotations
import numpy as np
from scipy.linalg import expm, polar as scipy_polar
from numpy.linalg import svd, matrix_rank

np.set_printoptions(precision=4, suppress=True, linewidth=140)
L, NM = 3, 9
SZ = np.array([[1, 0], [0, -1]], float); SM = np.array([[0, 1], [0, 0]], float); I2 = np.eye(2)

def ann(j, n):
    mats = [SZ]*j + [SM] + [I2]*(n-j-1)
    out = np.array([[1.0]])
    for m in mats: out = np.kron(out, m)
    return out
A = [ann(j, NM) for j in range(NM)]; AD = [a.conj().T for a in A]
NDAGN = [[(AD[i] @ A[j]).astype(complex) for j in range(NM)] for i in range(NM)]
hmat = np.zeros((NM, NM))
for x in range(L):
    for c in range(3):
        a_, b_ = 3*x+c, 3*((x+1)%L)+c
        hmat[a_, b_] = hmat[b_, a_] = -1.0
H = sum(hmat[i, j]*NDAGN[i][j] for i in range(NM) for j in range(NM))
U_step = expm(-1j*H*0.35)
def Gof(psi):
    return np.array([[psi.conj() @ NDAGN[i][j] @ psi for j in range(NM)] for i in range(NM)])
def cross(psi): return Gof(psi)[0:3, 3:6]

ew, evec = np.linalg.eigh(hmat)
def fermi_sea(nfill):
    vac = np.zeros(2**NM, complex)
    n_of = sum(AD[m] @ A[m] for m in range(NM)).real
    vac[int(np.argmin(np.diag(n_of)))] = 1.0
    psi = vac
    for k in range(nfill):
        orb = evec[:, k]
        psi = sum(orb[m]*AD[m].astype(complex) for m in range(NM)) @ psi
    return psi/np.linalg.norm(psi)

# draft's EXACT polar (unguarded) vs scipy
def polar_draft(M):
    w, V = np.linalg.eigh(M.conj().T @ M)
    return M @ V @ np.diag(w**-0.5) @ V.conj().T
def polar_scipy(M):
    U, _ = scipy_polar(M, side='right'); return U

def KB_pair(eps):
    Nop = sum(AD[c] @ A[c] for c in range(3))
    w, V = np.linalg.eigh(Nop)
    Nt = (w-w.mean())/max(abs(w-w.mean()))
    Kp = (V @ np.diag(np.sqrt((1+eps*Nt)/2)) @ V.conj().T).astype(complex)
    Km = (V @ np.diag(np.sqrt((1-eps*Nt)/2)) @ V.conj().T).astype(complex)
    return Kp, Km
KB = KB_pair(0.6)

print("=== How often is the cross block rank-deficient along the tree? (per state) ===")
for nfill in range(1, 9):
    psi0 = fermi_sea(nfill)
    branches = [(1.0, psi0)]
    rank_def = 0; total = 0; min_sv_global = 1e9
    draft_vs_scipy_gap = 0.0
    for n in range(5):
        new = []
        for (wt, ps) in branches:
            ps_f = U_step @ ps
            for Kop in KB:
                phi = Kop @ ps_f
                p = float(np.real(phi.conj() @ phi))
                if p < 1e-14: continue
                phi = phi/np.sqrt(p)
                cb = cross(phi)
                s = svd(cb, compute_uv=False)
                total += 1
                min_sv_global = min(min_sv_global, s.min())
                if s.min() < 1e-8:
                    rank_def += 1
                    # show the draft polar vs scipy polar disagreement on THIS block
                    u1 = polar_draft(cb); u2 = polar_scipy(cb)
                    gap = min(np.max(np.abs(u1-u2)), np.max(np.abs(u1+u2)))
                    draft_vs_scipy_gap = max(draft_vs_scipy_gap, gap)
                    # is the draft polar even unitary?
                    nonunit = np.max(np.abs(u1.conj().T @ u1 - np.eye(3)))
                new.append((wt*p, phi))
        branches = new
    print(f"  nfill={nfill}: rank-deficient cross blocks {rank_def}/{total}, "
          f"global min-sv={min_sv_global:.2e}, draft-vs-scipy polar gap={draft_vs_scipy_gap:.3f}")

print("\n=== Is the draft's UNGUARDED polar_u even UNITARY on a rank-deficient block? ===")
psi0 = fermi_sea(5)
branches = [(1.0, psi0)]
bad_examples = []
for n in range(5):
    new = []
    for (wt, ps) in branches:
        ps_f = U_step @ ps
        for Kop in KB:
            phi = Kop @ ps_f
            p = float(np.real(phi.conj() @ phi))
            if p < 1e-14: continue
            phi = phi/np.sqrt(p)
            cb = cross(phi)
            s = svd(cb, compute_uv=False)
            if s.min() < 1e-8 and len(bad_examples) < 3:
                ud = polar_draft(cb)
                nonunit = np.max(np.abs(ud.conj().T @ ud - np.eye(3)))
                hasnan = np.any(~np.isfinite(ud))
                bad_examples.append((s, nonunit, hasnan))
            new.append((wt*p, phi))
    branches = new
for s, nonunit, hasnan in bad_examples:
    print(f"  block svals={s}, draft polar ||U†U - I||={nonunit:.3e}, contains nan/inf={hasnan}")

print("\n=== Does the SPREAD value depend on which polar path (draft vs scipy)? (fermi_sea5) ===")
def tree_inc(psi0, polar):
    branches = [(1.0, psi0, [])]
    for n in range(5):
        new = []
        for (wt, ps, hist) in branches:
            ps_f = U_step @ ps
            for Kop in KB:
                phi = Kop @ ps_f
                p = float(np.real(phi.conj() @ phi))
                if p < 1e-14: continue
                phi = phi/np.sqrt(p)
                new.append((wt*p, phi, hist+[polar(cross(phi))]))
        branches = new
    incs = [(wt, h[-1] @ h[-2].conj().T) for (wt, _, h) in branches]
    Z = sum(wt for wt, _ in incs)
    Em = sum(wt*d for wt, d in incs)/Z
    var = float(sum(wt*np.linalg.norm(d-Em)**2 for wt, d in incs)/Z)
    return var, Em
for sname, nf in [("fermi_sea5", 5), ("fermi_sea1", 1), ("fermi_sea2", 2)]:
    psi0 = fermi_sea(nf)
    v_d, Em_d = tree_inc(psi0, polar_draft)
    v_s, Em_s = tree_inc(psi0, polar_scipy)
    print(f"  {sname}: var(draft polar)={v_d:.5f}  var(scipy polar)={v_s:.5f}  "
          f"|diff|={abs(v_d-v_s):.5f}  ||Em_d-Em_s||={np.max(np.abs(Em_d-Em_s)):.4f}")

print("\n=== CENTRALITY robustness: fraction of random Slater states with SCALAR E[dU] ===")
rng = np.random.default_rng(13)
n_scalar = 0; n_total = 0; offs = []
for trial in range(40):
    nfill = rng.integers(1, 9)
    C = rng.normal(size=(NM, nfill)) + 1j*rng.normal(size=(NM, nfill))
    C, _ = np.linalg.qr(C)
    vac = np.zeros(2**NM, complex)
    n_of = sum(AD[m] @ A[m] for m in range(NM)).real
    vac[int(np.argmin(np.diag(n_of)))] = 1.0
    psi = vac
    for k in range(nfill):
        psi = sum(C[m, k]*AD[m].astype(complex) for m in range(NM)) @ psi
    psi /= np.linalg.norm(psi)
    _, Em = tree_inc(psi, polar_scipy)
    off = np.linalg.norm(Em - (np.trace(Em)/3)*np.eye(3))
    offs.append(off); n_total += 1
    if off < 1e-6: n_scalar += 1
print(f"  {n_scalar}/{n_total} random Slater states have EXACTLY scalar E[dU] (centrality holds there)")
print(f"  off-scalar norm: min={min(offs):.4f} median={np.median(offs):.4f} max={max(offs):.4f}")
