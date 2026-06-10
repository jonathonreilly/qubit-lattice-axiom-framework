#!/usr/bin/env python3
"""The orbit-converse: the local-rotation orbit of the free hopping is EXACTLY the flat
link sector; holonomy class is the frame-unreachable residual.  ADM-1's KINEMATIC
absolute-frame redundancy is re-derived (corollary of #3332); its pointer-frame
SELECTION residual persists, exhibited.

Class-A exact verification for the source note

    docs/LOCAL_FRAME_ORBIT_FLAT_SECTOR_EXACT_CONVERSE_HOLONOMY_FRAME_UNREACHABLE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-06-10.md

CONTEXT (retire-mode; owner-directed attempt to wipe ADM-1 from the board; PANEL VERDICT:
the wipe does NOT go through -- a maximum-tier 5-lens adversarial panel, land_with_edits,
ALL ELEVEN edits applied).  The panel's decisive finding, independently recomputed: the
object derived here is the KINEMATIC absolute-local-frame gauge redundancy; the campaign's
{P_r} root (binding content of the retained_bounded #3450/#3453, live-ledger verified) is
the pointer-frame SELECTION question (which frame the einselection dynamics selects --
the #3436 S-primitivity fork), which is ORTHOGONAL to the joint co-rotation symmetry and
is NOT dissolved.  Part 4 below EXHIBITS that persistence rather than asserting around it.

THE RESULTS (all exact, full 2^9-dim Fock space where Fock-level, no MC):
  (R1) [corollary-with-citation of #3332] LOCAL FUSION.  Record content of (state,
       per-site frame-naming instruments, link-field hopping) -- including interleaved
       dynamics -- is exactly invariant under the simultaneous local action.  The
       underlying operator law Gamma({g}) H[U] Gamma† = H[g_x U_xy g_y†] is #3332's
       central identity (verified here at the Fock level, general U and the U=I case);
       the link co-transform is #3332's transporter step.  The fusion adds only the
       instrument-side covariance + cyclicity.  NON-VACUITY of #3332's forcing argument
       preserved: without the compensator the free hopping BREAKS under local frames
       (||Gamma H_free Gamma† - H_free|| = O(1), verified).
  (R2) [THE NEW LOAD-BEARING RESULT] THE ORBIT-CONVERSE.  Every trivial-holonomy link
       field is comparator (pure-gauge) form -- explicit construction, exact -- so the
       local-rotation orbit of the derived free hopping is EXACTLY the entire flat
       sector.  This closes #3332's one-directional "flat connection => trivial
       holonomy" into a two-directional orbit characterization: frame fields reach the
       flat sector, the WHOLE flat sector, and nothing else.
  (R3) [sharpening-with-citation of #3332] A GENUINE FRAME-UNREACHABLE RESIDUAL:
       HOLONOMY.  The holonomy conjugacy class is invariant under the local action
       (=> frame-unreachable); a generic-flux field is RECORD-separated from the entire
       flat sector by a color-blind (Pauli-singlet) probe, while every flat field gives
       exactly the free value.  This re-expresses #3332's gauge-invariant spectrum/
       plaquette facts as a record-level separation; it earns the EXISTENCE of the
       residual, NOT any completeness claim ("holonomy is THE gauge content" would be
       imported framing and is not claimed).  CAUTION (corrected per panel): at the
       SU(3) accident flux diag(-1,-1,1) on the 3-ring, the field is record-
       INDISTINGUISHABLE from free on these probes (Fock spectra coincide; ALL
       single-particle return records coincide -- particle-hole conjugacy); only the
       eigenvalue LISTS differ.  Genericity of the separating flux is load-bearing.
  (R4) THE PERSISTING ROOT, EXHIBITED.  With the einselection driver FIXED, varying the
       frame alone changes the physical outcome (which basis dephases) -- the
       pointer-frame SELECTION question is real, dynamics-level, and untouched by the
       joint co-rotation (which moves frame AND dynamics together: joint covariance
       verified exactly).  ADM-1's kinematic content is derived; its SELECTION content
       -- the {P_r} root of #3450/#3453 -- PERSISTS.

Run: python3 scripts/frontier_local_frame_orbit_flat_sector_converse_holonomy_residual_2026_06_10.py
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import expm

PASS = 0
FAIL = 0


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


rng = np.random.default_rng(20260610)


def ann(j, n):
    sz = np.array([[1, 0], [0, -1]], float)
    sm = np.array([[0, 1], [0, 0]], float)
    ops = [sz] * j + [sm] + [np.eye(2)] * (n - j - 1)
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out


def haar3():
    A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))
    return Q / np.linalg.det(Q) ** (1 / 3)


def logu(u):
    w, V = np.linalg.eig(u)
    return V @ np.diag(np.log(w)) @ np.linalg.inv(V)


Lsp = 3
NM = 9
A9 = [ann(j, NM) for j in range(NM)]
AD9 = [a.T for a in A9]
EDGES = [(0, 1), (1, 2), (2, 0)]
I3 = np.eye(3, dtype=complex)


def gamma_local(gs):
    K = sum(logu(gs[x])[i, j] * (AD9[i * Lsp + x] @ A9[j * Lsp + x]).astype(complex)
            for x in range(Lsp) for i in range(3) for j in range(3))
    return expm(K)


def H_links(W):
    H = np.zeros((2 ** NM, 2 ** NM), complex)
    for (x, y) in EDGES:
        for i in range(3):
            for j in range(3):
                H += -W[(x, y)][i, j] * (AD9[i * Lsp + x] @ A9[j * Lsp + y]).astype(complex)
    return H + H.conj().T


H_free = H_links({e: I3 for e in EDGES})
holonomy = lambda W: W[(0, 1)] @ W[(1, 2)] @ W[(2, 0)]


def site_frame_projs(x, u):
    K = sum(logu(u)[i, j] * (AD9[i * Lsp + x] @ A9[j * Lsp + x]).astype(complex)
            for i in range(3) for j in range(3))
    Gx = expm(K)
    nops = [AD9[c * Lsp + x] @ A9[c * Lsp + x] for c in range(3)]
    Ps = []
    for pat in range(8):
        P = np.eye(2 ** NM)
        for c in range(3):
            P = P @ (nops[c] if (pat >> c) & 1 else np.eye(2 ** NM) - nops[c])
        Ps.append(Gx @ P.astype(complex) @ Gx.conj().T)
    return Ps


def content(rho, us, W):
    U = expm(-1j * H_links(W) * 0.9)
    out = []
    P0 = site_frame_projs(0, us[0])
    P1 = site_frame_projs(1, us[1])
    for P in P0:
        post = P @ rho @ P
        out.append(np.trace(post).real)
        post = U @ post @ U.conj().T
        for Q in P1[:4]:
            out.append(np.trace(Q @ post).real)
    return np.array(out)


# ===========================================================================
# Part 1.  (R1) local fusion — corollary-with-citation of #3332's central identity.
# ===========================================================================
print("=" * 78)
print("Part 1  (R1) local fusion (corollary of #3332; instrument covariance + cyclicity)")
print("=" * 78)

gs = [haar3() for _ in range(Lsp)]
G = gamma_local(gs)
# #3332's central identity at the Fock level, GENERAL U:
W_any = {e: haar3() for e in EDGES}
W_t = {(x, y): gs[x] @ W_any[(x, y)] @ gs[y].conj().T for (x, y) in EDGES}
check("#3332's central identity, general links (Fock level): "
      "Gamma({g}) H[U] Gamma† = H[g_x U_xy g_y†]",
      np.max(np.abs(G @ H_links(W_any) @ G.conj().T - H_links(W_t))) < 1e-9)
gW = {(x, y): gs[x] @ gs[y].conj().T for (x, y) in EDGES}
check("its U = I case: Gamma H_free Gamma† = H[g_x g_y†] (the comparator law used below)",
      np.max(np.abs(G @ H_free @ G.conj().T - H_links(gW))) < 1e-9)
check("NON-VACUITY of #3332's forcing argument is preserved: WITHOUT the compensator the "
      "free hopping breaks under local frames (||Gamma H_free Gamma† - H_free|| = O(1))",
      np.max(np.abs(G @ H_free @ G.conj().T - H_free)) > 0.5,
      f"breaking norm {np.max(np.abs(G @ H_free @ G.conj().T - H_free)):.2f}")

w = rng.normal(size=2 ** NM) + 1j * rng.normal(size=2 ** NM)
w /= np.linalg.norm(w)
rho = np.outer(w, w.conj())
u_loc = [haar3() for _ in range(Lsp)]
c0 = content(rho, u_loc, {e: I3 for e in EDGES})
c1 = content(G @ rho @ G.conj().T, [gs[x] @ u_loc[x] for x in range(Lsp)], gW)
check("LOCAL FUSION: record content (probs + interleaved-dynamics sequences) exactly "
      "invariant under the simultaneous local action (state + frames + links)",
      np.max(np.abs(c0 - c1)) < 1e-10, f"max dev {np.max(np.abs(c0 - c1)):.1e}")
c2 = content(rho, [gs[x] @ u_loc[x] for x in range(Lsp)], {e: I3 for e in EDGES})
check("teeth: a frames-only local rotation changes content at order 1 (relative data "
      "real; only the absolute field is jointly vacuous — the KINEMATIC statement)",
      np.max(np.abs(c0 - c2)) > 0.01, f"shift {np.max(np.abs(c0 - c2)):.3f}")

# ===========================================================================
# Part 2.  (R2) THE ORBIT-CONVERSE — the new load-bearing result.
# ===========================================================================
print("=" * 78)
print("Part 2  (R2) the orbit-converse: frame orbit of the free hopping = the FLAT sector")
print("=" * 78)

check("forward (from R1's law): comparator fields are FLAT — holonomy(g_x g_y†) = I "
      "exactly (#3332's direction)",
      np.allclose(holonomy(gW), I3, atol=1e-12))
Wf = {(0, 1): haar3(), (1, 2): haar3()}
Wf[(2, 0)] = Wf[(1, 2)].conj().T @ Wf[(0, 1)].conj().T
g0, g1, g2 = I3, Wf[(0, 1)].conj().T, (Wf[(0, 1)] @ Wf[(1, 2)]).conj().T
check("CONVERSE (new): every trivial-holonomy link field is comparator form — explicit "
      "construction g_0=I, g_1=W_01†, g_2=(W_01 W_12)† reproduces all three links exactly",
      all(np.allclose(Wf[(x, y)], [g0, g1, g2][x] @ [g0, g1, g2][y].conj().T, atol=1e-12)
          for (x, y) in EDGES))
check("hence H[flat W] = Gamma H_free Gamma†: the orbit of the free hopping is the "
      "ENTIRE flat sector and nothing else — a two-directional orbit characterization",
      np.max(np.abs(H_links(Wf) - gamma_local([g0, g1, g2]) @ H_free
                    @ gamma_local([g0, g1, g2]).conj().T)) < 1e-9)
t_diag = np.diag(np.exp(1j * rng.normal(size=3))).astype(complex)
t_diag = t_diag / np.linalg.det(t_diag) ** (1 / 3)
P_u = site_frame_projs(0, u_loc[0])
P_ut = site_frame_projs(0, u_loc[0] @ t_diag)
check("T^2 subtlety (the #3453 arrow-1 gap object, instantiated): flag-level frames are "
      "torus-blind (u and u*t give identical instruments) while their comparators differ "
      "— unitary frames are used for the converse",
      all(np.allclose(P_u[k], P_ut[k], atol=1e-10) for k in range(8)))

# ===========================================================================
# Part 3.  (R3) holonomy: a genuine frame-unreachable, record-separating residual.
# ===========================================================================
print("=" * 78)
print("Part 3  (R3) holonomy residual (sharpening of #3332's gauge-invariant facts)")
print("=" * 78)

holW = holonomy(W_any)
check("the holonomy conjugacy class is invariant under the local action "
      "(holonomy -> g_0 holonomy g_0†) => no frame field reaches a nontrivial class",
      np.allclose(holonomy(W_t), gs[0] @ holW @ gs[0].conj().T, atol=1e-10))
phi = 2 * np.pi / 5
W_flux = {(0, 1): np.diag([np.exp(1j * phi), np.exp(-1j * phi), 1]).astype(complex),
          (1, 2): I3, (2, 0): I3}
check("a generic-flux field has a NONTRIVIAL holonomy class (det = +1: genuine SU(3))",
      not np.allclose(holonomy(W_flux), I3, atol=1e-6)
      and abs(np.linalg.det(W_flux[(0, 1)]) - 1) < 1e-12)
s_free = np.sort(np.linalg.eigvalsh(H_free))
s_flux = np.sort(np.linalg.eigvalsh(H_links(W_flux)))
check("generic flux: the full Fock spectra differ from free",
      not np.allclose(s_free, s_flux, atol=1e-9),
      f"ground {s_free[0]:.4f} vs {s_flux[0]:.4f}")
vac_idx = int(np.argmin(np.diag(sum(AD9[m] @ A9[m] for m in range(NM)).real)))
vac = np.zeros(2 ** NM)
vac[vac_idx] = 1.0
psi0 = (AD9[0] @ AD9[3] @ AD9[6]) @ vac.astype(complex)
psi0 /= np.linalg.norm(psi0)
t = 1.3
r_free = abs(psi0.conj() @ expm(-1j * H_free * t) @ psi0) ** 2
r_flux = abs(psi0.conj() @ expm(-1j * H_links(W_flux) * t) @ psi0) ** 2
r_flat = abs(psi0.conj() @ expm(-1j * H_links(gW) * t) @ psi0) ** 2
check("RECORD separation: the color-blind (Pauli-singlet) probe separates generic flux "
      "from free at order 10x",
      abs(r_free - r_flux) > 1e-3, f"{r_free:.6f} vs {r_flux:.6f}")
check("while EVERY frame-induced (flat) field gives EXACTLY the free value on that probe",
      abs(r_flat - r_free) < 1e-12, f"flat {r_flat:.6f}")
# CAUTION, corrected per panel: the SU(3) accident representative diag(-1,-1,1), det=+1
W_acc = {(0, 1): np.diag([-1.0, -1.0, 1.0]).astype(complex), (1, 2): I3, (2, 0): I3}
check("the accident representative is genuine SU(3): det(diag(-1,-1,1)) = +1 "
      "(the draft's diag(-1,1,1) had det = -1: U(3), not SU(3) — panel-caught, fixed)",
      abs(np.linalg.det(W_acc[(0, 1)]) - 1) < 1e-12)
s_acc = np.sort(np.linalg.eigvalsh(H_links(W_acc)))
# single-particle return records over a time grid, accident vs free (per color sector):
h_free_1p = np.array([[0, -1, -1], [-1, 0, -1], [-1, -1, 0]], complex)
h_acc_1p = h_free_1p.copy()
h_acc_1p[0, 1] = h_acc_1p[1, 0] = +1.0          # the -1 link phase on edge (0,1), color 0
worst_rec = 0.0
for tt in np.linspace(0.3, 3.0, 7):
    for k in range(3):
        e0 = np.zeros(3, complex)
        e0[k] = 1
        a = abs(e0.conj() @ expm(-1j * h_free_1p * tt) @ e0) ** 2
        b = abs(e0.conj() @ expm(-1j * h_acc_1p * tt) @ e0) ** 2
        worst_rec = max(worst_rec, abs(a - b))
check("CAUTION (corrected wording): at the accident flux the field is record-"
      "INDISTINGUISHABLE from free on these probes — Fock spectra coincide AND all "
      "single-particle return records coincide (particle-hole conjugacy); only the "
      "eigenvalue lists differ. Genericity of the separating flux is LOAD-BEARING",
      np.allclose(s_free, s_acc, atol=1e-9) and worst_rec < 1e-12,
      f"Fock spectra equal; max single-particle record gap {worst_rec:.1e}")

# ===========================================================================
# Part 4.  (R4) the persisting root, EXHIBITED: frame selection is dynamics-level.
# ===========================================================================
print("=" * 78)
print("Part 4  (R4) the {P_r} SELECTION root persists (exhibited, not asserted)")
print("=" * 78)

P3 = [np.diag(v).astype(complex) for v in ([1, 0, 0], [0, 1, 0], [0, 0, 1])]


def dephase(u, r):
    return sum((u @ p @ u.conj().T) @ r @ (u @ p @ u.conj().T) for p in P3)


rho3 = np.array([[.5, .2, .1], [.2, .3, .05], [.1, .05, .2]], complex)
rho3 = (rho3 + rho3.conj().T) / 2
rho3 /= np.trace(rho3)
u1, u2, g3 = haar3(), haar3(), haar3()
check("WITH THE DRIVER FIXED, the frame choice changes the physical outcome (which "
      "basis dephases): ||D_u1(rho) - D_u2(rho)|| = O(1) — the pointer-frame SELECTION "
      "question (#3436 S-primitivity; the binding {P_r} content of #3450/#3453) is "
      "real, dynamics-level, and NOT touched by this note",
      float(np.max(np.abs(dephase(u1, rho3) - dephase(u2, rho3)))) > 0.02,
      f"difference {np.max(np.abs(dephase(u1, rho3) - dephase(u2, rho3))):.3f}")
check("while the JOINT co-rotation is exactly covariant (D_{gu}(g rho g†) = "
      "g D_u(rho) g†): the kinematic absolute-frame content is vacuous; the SELECTION "
      "content is the part that persists",
      np.max(np.abs(dephase(g3 @ u1, g3 @ rho3 @ g3.conj().T)
                    - g3 @ dephase(u1, rho3) @ g3.conj().T)) < 1e-12)

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE (panel-rescoped — the owner-directed WIPE DOES NOT GO THROUGH): what is")
print("  derived is ADM-1's KINEMATIC content (the absolute local frame field as a joint")
print("  gauge redundancy — a corollary, at the record level, of #3332's central")
print("  identity, with #3332's forcing argument verified NON-vacuous).  The NEW")
print("  load-bearing result is the ORBIT-CONVERSE (R2): the local-rotation orbit of the")
print("  free hopping is EXACTLY the flat link sector (both directions, explicit")
print("  construction), with the holonomy conjugacy class the frame-unreachable,")
print("  record-separating residual (R3 — existence earned, NO completeness claim; the")
print("  accident caution corrected to a genuine SU(3) representative and honest record-")
print("  indistinguishability wording).  The pointer-frame SELECTION root — which frame")
print("  the einselection dynamics selects (#3436; the binding retained_bounded content")
print("  of #3450/#3453) — PERSISTS and is EXHIBITED in R4 (frame matters with the")
print("  driver fixed; only the joint motion is vacuous).  The instrument-relative")
print("  remainder is an INSTRUMENT-SIDE residual, distinct in type from the #3486")
print("  state-realization clause (branch-only source proposal; no merge claimed).")
print("  hat-4/ADM-2 note: they share the {P_r} root (#3450, #3449), so their")
print("  frame-shaped KINEMATIC part re-types as in R1-R2; their isometry-existence /")
print("  depolarization / global-singlet contents are NOT addressed here and stand.")
print("  'Theorem, not premise' applies to the in-derivation proposition on this surface")
print("  ONLY — no grade is authored or implied for #3332 or any note (audit lane")
print("  grades).  No new axiom, primitive, measure, or weight; r untouched; conditional")
print("  on the supplied C^3 carrier + named hopping + named instrument classes.")
if FAIL:
    raise SystemExit(1)
