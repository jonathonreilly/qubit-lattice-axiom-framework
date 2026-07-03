#!/usr/bin/env python3
"""Open-shell invariant-locus neutrality and no derived selector.

Class-A exact verification for the source note

    docs/OPEN_SHELL_INVARIANT_LOCUS_CONDITIONAL_NEUTRALITY_NO_DERIVED_SELECTOR_BOUNDED_THEOREM_NOTE_2026-06-10.md

Scope: conditional on the supplied C^3 carrier, named color-diagonal hopping,
half-filled open-shell ground manifold, and named color-blind instrument class.
The realized-state locus remains open; this runner checks the invariant-locus
neutrality theorem, non-selection by the named derived structure, and the
continuous all-site departure parameter.

THE THEOREMS (exact):
  (T1) INVARIANT-LOCUS NEUTRALITY.  The
       open-shell ground manifold (deg 20 in the L=3 instance) is SU(3)-invariant as a
       subspace and decomposes as 4 x singlet (+) 2 x octet (Casimir eigenvalues 0 x 4 and
       12 x 16 in the un-halved-lambda normalization; commutant dimension exactly
       4^2 + 2^2 = 20).  EVERY SU(3)-invariant
       density supported on it -- the full 20-dim commutant, sampled exhaustively by
       basis and randomly by PSD combinations -- has rho_color(x) = I_3/3 EXACTLY at
       EVERY site by a finite-dimensional Schur/commutant mechanism.  The
       obstruction is a property of NON-invariant
       (color-polarized) pure selections, not of the manifold.
  (T2) NO DERIVED SELECTOR (exact equivariance + stability).  The named color-diagonal
       hopping, the color-blind instrument class, and the count/Casimir conservation
       laws all commute with the global SU(3) action.  Hence (a) the invariant locus is
       DYNAMICALLY STABLE under the interleaved (Hamiltonian + record) flow -- an
       invariant state stays invariant, so stays neutral at every site; and (b) nothing
       derived selects against it either: color-blind records preserve a non-invariant
       state's per-site rho_color exactly, and nothing derived lifts the degeneracy.
       The selection is underived in BOTH directions.  (Preservation only -- consistent
       with blocks 05-07: derived structure cannot CREATE depolarization.)
  (T3) THE REGISTRABLE ORDER PARAMETER (continuous; all-site).  Define
       D = max_x [ Tr(rho_color(x)^2) - 1/3 ]  (the worst-site purity excess -- a
       manifestly SU(3)-invariant, two-copy-estimable functional; block-04's order
       parameter in all-site form.  A max-entry-norm trial form was NOT unitarily
       invariant -- caught by this runner's own invariance check and replaced).
       Invariance => D = 0 (T1); D > 0 certifies departure.
       D is CONTINUOUS: convex mixtures sweep it smoothly to 0 (verified) -- the
       residual is "the invariant locus {D=0 via invariance} versus its
       complement, separated by a continuous invariant order parameter", NOT a binary.
       Faithfulness check: a single-site purity can read ~1/3 on a state broken at
       other sites (reproduced); the separator must be ALL-SITE, as defined here.
  (T4) HONESTY/TEETH.  A non-invariant ground state sits at EXACTLY the ground energy
       (no derived lifting); frame-naming instruments break the equivariance.  NO claim about which locus the
       realized state occupies: the equipartition state P_gs/20 -- the maximally-mixed
       invariant state -- appears as an
       EXISTENCE witness only (and it is NOT the Haar twirl of a non-invariant manifold
       state: the twirl's spectrum is non-flat); no weight is assigned.
       Decimal values quoted in checks are instance/basis artifacts, not constants.

Run: python3 scripts/frontier_open_shell_invariant_locus_no_derived_selector_2026_06_10.py
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


def gell_mann():
    return [np.array(m, complex) for m in (
        [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]],
        [[1, 0, 0], [0, -1, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
        [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])] + [np.diag([1, 1, -2]).astype(complex) / np.sqrt(3)]


LAM = gell_mann()
Lsp, NCOL = 3, 3
NM = Lsp * NCOL                       # mode index m = color*Lsp + site
A9 = [ann(j, NM) for j in range(NM)]
AD9 = [a.T for a in A9]
h_spat = np.zeros((Lsp, Lsp))
for x in range(Lsp):
    h_spat[x, (x + 1) % Lsp] = h_spat[(x + 1) % Lsp, x] = -1.0
H = sum(h_spat[x, y] * (AD9[c * Lsp + x] @ A9[c * Lsp + y])
        for c in range(NCOL) for x in range(Lsp) for y in range(Lsp))
Ntot = sum(AD9[m] @ A9[m] for m in range(NM))
wN, VN = np.linalg.eigh(Ntot)
P6 = VN[:, np.isclose(wN, 6.0)]
H6 = P6.T @ H @ P6
eH, vH = np.linalg.eigh(H6)
GS = P6 @ vH[:, np.isclose(eH, eH[0], atol=1e-9)]      # the open-shell ground manifold
DEG = GS.shape[1]
Pgs = GS @ GS.T


def rho_color(rho, x):
    G = np.array([[np.trace(rho @ (AD9[i * Lsp + x] @ A9[j * Lsp + x])) for j in range(3)]
                  for i in range(3)])
    return G / np.trace(G)


def D_allsite(rho):
    """All-site order parameter: worst-site PURITY EXCESS Tr(rho_color^2) - 1/3 >= 0.
    Manifestly SU(3)-invariant (a unitarily invariant functional of the marginal),
    two-copy estimable, zero iff the marginal
    is I3/3 at that site (block-04's order parameter, all-site form)."""
    return max(float(np.real(np.trace(rho_color(rho, x) @ rho_color(rho, x)))) - 1 / 3
               for x in range(Lsp))


def gamma_global(xi):
    K = sum(xi[i, j] * (AD9[i * Lsp + x] @ A9[j * Lsp + x]).astype(complex)
            for i in range(3) for j in range(3) for x in range(Lsp))
    return expm(K)


# ===========================================================================
# Part 1.  (T1) invariant-locus neutrality: rep content + the full commutant is neutral.
# ===========================================================================
print("=" * 78)
print(f"Part 1  (T1) invariant-locus neutrality on the deg-{DEG} manifold: 4 x singlet (+) 2 x octet")
print("=" * 78)

xi = sum(rng.normal() * 1j * lam for lam in LAM) * 0.3
Gg = gamma_global(xi)
check("the ground manifold is SU(3)-invariant as a subspace ([Gamma(g), P_gs] = 0)",
      np.max(np.abs(Gg @ Pgs.astype(complex) - Pgs.astype(complex) @ Gg)) < 1e-10)

# restrict the 8 charges to the manifold and decompose
Qs_full = [sum(lam[i, j] * sum((AD9[i * Lsp + x] @ A9[j * Lsp + x]).astype(complex)
                               for x in range(Lsp)) for i in range(3) for j in range(3))
           for lam in LAM]
QM = [GS.T.conj().astype(complex) @ q @ GS.astype(complex) for q in Qs_full]
C2M = sum(q @ q.conj().T for q in QM)
ev_c2 = np.sort(np.real(np.linalg.eigvalsh(C2M)))
n_singlet = int(np.sum(ev_c2 < 1e-9))
# charges built from un-halved Gell-Mann lambdas: C2 = 4 x C2(T=lambda/2); adjoint C2 = 3
# in the T-normalization => 12 here
n_octet_states = int(np.sum(np.abs(ev_c2 - 12.0) < 1e-6))
check("rep content: Casimir eigenvalues on the manifold are 0 (x4) and 12 (x16, the "
      "adjoint value in the un-halved-lambda normalization) => 4 x singlet (+) 2 x octet",
      n_singlet == 4 and n_octet_states == 16 and n_singlet + n_octet_states == DEG,
      f"singlets {n_singlet}, octet states {n_octet_states}")

# the commutant of the restricted action: solve [X, QM_a] = 0 for all a
M = []
for q in QM:
    L_op = np.kron(np.eye(DEG), q.T) - np.kron(q, np.eye(DEG))
    M.append(L_op)
M = np.vstack(M)
_, sv, Vh = np.linalg.svd(M)
null = Vh[np.sum(sv > 1e-9 * sv[0]):].conj()
check("the commutant of the SU(3) action on the manifold has dimension EXACTLY "
      "4^2 + 2^2 = 20 (multiplicity squares)",
      null.shape[0] == 20, f"commutant dim {null.shape[0]}")

# EVERY invariant density is neutral at EVERY site: exhaust the commutant basis +
# random PSD invariant combinations
worst = 0.0
for k in range(null.shape[0]):
    X = null[k].reshape(DEG, DEG)
    X = (X + X.conj().T) / 2
    Xf = GS.astype(complex) @ X @ GS.T.conj().astype(complex)
    # use as a (possibly non-PSD) invariant Hermitian functional: neutrality of the
    # bilinear trace only needs tr(Xf a^dag a); normalize by trace when nonzero
    tr = np.trace(Xf)
    if abs(tr) < 1e-12:
        continue
    rho_k = Xf / tr
    worst = max(worst, D_allsite(rho_k))
for trial in range(50):
    w = rng.normal(size=null.shape[0])
    X = sum(w[k] * null[k].reshape(DEG, DEG) for k in range(null.shape[0]))
    X = (X + X.conj().T) / 2
    X = X @ X.conj().T                              # PSD invariant
    rho_r = GS.astype(complex) @ (X / np.trace(X)) @ GS.T.conj().astype(complex)
    worst = max(worst, D_allsite(rho_r))
check("EVERY invariant density on the manifold is neutral at EVERY site (full commutant "
      "basis + 50 random invariant PSD states; all-site deviation < 1e-12)",
      worst < 1e-12, f"worst all-site dev {worst:.1e}")

rho_proj = (Pgs / np.trace(Pgs)).astype(complex)
check("the equipartition invariant state P_gs/20 (the maximally-mixed invariant state; "
      "EXISTENCE witness only, no realization "
      "claimed, no weight assigned): all-site neutral",
      D_allsite(rho_proj) < 1e-12, f"D = {D_allsite(rho_proj):.1e}")
# P_gs/20 is NOT the Haar twirl of a non-invariant manifold state in disguise:
# the twirl of a broken pure state has NON-flat spectrum.
psi_b = GS[:, 0] + GS[:, 1]
psi_b = (psi_b / np.linalg.norm(psi_b)).astype(complex)
rho_b = np.outer(psi_b, psi_b.conj())
# project rho_b onto the commutant (= its exact group average over the manifold action)
rb_M = GS.T.conj().astype(complex) @ rho_b @ GS.astype(complex)
coeffs = null.conj() @ rb_M.flatten()
twirl_M = sum(coeffs[k] * null[k].reshape(DEG, DEG) for k in range(null.shape[0]))
twirl_M = (twirl_M + twirl_M.conj().T) / 2
ev_tw = np.sort(np.real(np.linalg.eigvalsh(twirl_M)))
flat = np.allclose(ev_tw, ev_tw[-1], atol=1e-6)
check("P_gs/20 is NOT the twirl of the broken exhibit in disguise: the broken state's "
      "exact group average has a NON-flat manifold spectrum (the equipartition witness "
      "is not the demoted uniform-weight move applied to anything)",
      not flat, f"twirl spectrum spread {ev_tw[-1]-ev_tw[0]:.3f}")

# ===========================================================================
# Part 2.  (T2) no derived selector: equivariance + stability of the invariant locus.
# ===========================================================================
print("=" * 78)
print("Part 2  (T2) equivariance (exact); the invariant locus is dynamically stable")
print("=" * 78)

check("[Gamma(g), H] = 0: the named hopping is exactly equivariant",
      np.max(np.abs(Gg @ H.astype(complex) - H.astype(complex) @ Gg)) < 1e-10)
n_site0 = sum(AD9[c * Lsp] @ A9[c * Lsp] for c in range(3))
wS, VS = np.linalg.eigh(n_site0)
PK = [VS[:, np.isclose(wS, k)] @ VS[:, np.isclose(wS, k)].T for k in range(4)]
worst = max(float(np.max(np.abs(Gg @ P.astype(complex) - P.astype(complex) @ Gg))) for P in PK)
check("[Gamma(g), I-B site-occupation projectors] = 0: the color-blind instrument class "
      "is exactly equivariant", worst < 1e-10, f"max dev {worst:.1e}")
C2_full = sum(q @ q.conj().T for q in Qs_full)
check("[Gamma(g), Casimir/counts] = 0 (conservation laws equivariant)",
      np.max(np.abs(Gg @ C2_full - C2_full @ Gg)) < 1e-8)

U = expm(-1j * H.astype(complex) * 0.7)
rho_t = U @ rho_proj @ U.conj().T
rho_r = sum(P.astype(complex) @ rho_t @ P.astype(complex) for P in PK)
inv_after = float(np.max(np.abs(Gg @ rho_r - rho_r @ Gg)))
check("STABILITY: after a Hamiltonian step + an I-B record step an invariant state is "
      "STILL invariant (hence still all-site neutral by T1) -- preservation only, "
      "consistent with blocks 05-07",
      inv_after < 1e-10 and D_allsite(rho_r) < 1e-12,
      f"invariance dev {inv_after:.1e}, D {D_allsite(rho_r):.1e}")

# ===========================================================================
# Part 3.  (T3) the continuous, all-site registrable order parameter.
# ===========================================================================
print("=" * 78)
print("Part 3  (T3) the order parameter D: all-site, invariant, registrable, CONTINUOUS")
print("=" * 78)

check("the non-invariant exhibit sits at EXACTLY the ground energy (no derived lifting)",
      abs(float(np.real(psi_b.conj() @ H.astype(complex) @ psi_b)) - eH[0]) < 1e-9)
D_b = D_allsite(rho_b)
check("and departs the locus: D > 0 (purity excess; instance/basis-dependent value, "
      "not a physical constant)", D_b > 1e-3, f"D = {D_b:.4f} (instance artifact)")
check("D is SU(3)-invariant content (D(g rho g+) = D(rho) exactly): registrable via "
      "two-copy invariant estimators per site, worst over sites",
      abs(D_allsite(Gg @ rho_b @ Gg.conj().T) - D_b) < 1e-10,
      f"|D(g rho g+) - D(rho)| = {abs(D_allsite(Gg @ rho_b @ Gg.conj().T) - D_b):.1e}")
# The convex family sweeps D smoothly to 0 -- NOT a binary.
Ds = [D_allsite(((1 - t) * rho_b + t * rho_proj)) for t in (0, 0.25, 0.5, 0.75, 1.0)]
mono = all(Ds[i] >= Ds[i + 1] - 1e-12 for i in range(4))
check("D is CONTINUOUS: the convex family (1-t) rho_broken + t rho_invariant sweeps D "
      "smoothly and monotonically to 0 -- the restructured residual is 'the invariant "
      "locus vs its complement under a CONTINUOUS order parameter', NOT a binary",
      mono and Ds[0] > 1e-3 and Ds[-1] < 1e-12,
      f"D(t) = {[round(d,4) for d in Ds]}")
# A single-site reading can MISS a broken state.
# construct a state broken mostly away from site 0 by rotating colors with a
# site-localized frame change... exhibit via search over manifold states:
# precompute the site-resolved bilinears restricted to the 20-dim manifold (fast search)
BM = [[[GS.T.conj().astype(complex) @ (AD9[i * Lsp + x] @ A9[j * Lsp + x]).astype(complex)
        @ GS.astype(complex) for j in range(3)] for i in range(3)] for x in range(Lsp)]


def site_purity_excess(w, x):
    G = np.array([[w.conj() @ BM[x][i][j] @ w for j in range(3)] for i in range(3)])
    G = G / np.trace(G)
    return float(np.real(np.trace(G @ G))) - 1 / 3


best = None
w_best = None
for trial in range(2000):
    w = rng.normal(size=DEG) + 1j * rng.normal(size=DEG)
    w /= np.linalg.norm(w)
    p0 = site_purity_excess(w, 0)
    pall = max(site_purity_excess(w, x) for x in range(Lsp))
    score = pall - 20 * p0
    if best is None or score > best[0]:
        best, w_best = (score, p0, pall), w
for refine in range(400):                      # local refinement around the best
    w = w_best + 0.08 * (rng.normal(size=DEG) + 1j * rng.normal(size=DEG))
    w /= np.linalg.norm(w)
    p0 = site_purity_excess(w, 0)
    pall = max(site_purity_excess(w, x) for x in range(Lsp))
    score = pall - 20 * p0
    if score > best[0]:
        best, w_best = (score, p0, pall), w
check("FAITHFULNESS: a manifold state exists whose SITE-0 purity excess is "
      "small while the ALL-SITE D is large -- single-site readings are not faithful; "
      "the separator must be all-site as defined (search on the restricted manifold)",
      best is not None and best[1] < best[2] / 10 and best[2] > 1e-3,
      f"site-0 excess {best[1]:.5f} vs all-site D {best[2]:.4f}")

# ===========================================================================
# Part 4.  (T4) teeth: no derived selection either way; the frame-naming exception.
# ===========================================================================
print("=" * 78)
print("Part 4  (T4) honesty: nothing derived selects either way")
print("=" * 78)

rho_b_rec = sum(P.astype(complex) @ rho_b @ P.astype(complex) for P in PK)
check("color-blind records do NOT move a non-invariant state toward the locus: its "
      "per-site rho_color is preserved EXACTLY by I-B (block-02 lineage) => D conserved",
      abs(D_allsite(rho_b_rec) - D_b) < 1e-12,
      f"D change {abs(D_allsite(rho_b_rec)-D_b):.1e}")
xiF = sum(rng.normal() * 1j * lam for lam in LAM) * 0.5
uF = expm(xiF)
w0, V0 = np.linalg.eig(uF)
loguF = V0 @ np.diag(np.log(w0)) @ np.linalg.inv(V0)
GF = expm(sum(loguF[i, j] * (AD9[i * Lsp] @ A9[j * Lsp]).astype(complex)
              for i in range(3) for j in range(3)))
frame_named_projector = GF @ (AD9[0] @ A9[0]).astype(complex) @ GF.conj().T
dev_eq = float(np.max(np.abs(Gg @ frame_named_projector - frame_named_projector @ Gg)))
check("a FRAME-NAMING projector does NOT commute with the global rotation (the named "
      "exception to the color-blind instrument class; instance-dependent magnitude)",
      dev_eq > 0.05, f"non-equivariance {dev_eq:.3f} (instance artifact)")

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: conditional on the realized state lying in the SU(3)-invariant locus")
print("  of the open-shell ground manifold, all-site neutrality holds and persists")
print("  under the named derived structure. Which locus the realized state occupies")
print("  is NOT resolved here; nothing derived selects either way. Departure is")
print("  measured by the continuous, all-site, SU(3)-invariant order parameter D.")
print("  The equipartition witness P_gs/20 is existence-only and no weight is")
print("  assigned. Conditional on the supplied C^3 carrier, named hopping, and named")
print("  instrument classes. No audit grade is authored here.")
if FAIL:
    raise SystemExit(1)
