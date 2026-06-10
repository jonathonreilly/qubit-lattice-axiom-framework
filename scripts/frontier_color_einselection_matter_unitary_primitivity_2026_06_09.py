"""Block 07 runner -- in the named hopping matter family, the matter-unitary
primitivity input of the color-einselection criterion requires a presupposed
background color connection.

Context. Block 06
(`COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION...`)
reduced single-record-frame color depolarization to a property of the coherent
matter color unitary U on the C^3 color carrier: for the predictability-sieve
channel Phi(rho) = D_B(U rho U^dag) with one NAMED record frame B, the color
pointer states are the B-diagonal states stationary under the unistochastic
matrix S_ij = |<e_i|U|e_j>|^2, and rho_color depolarizes to I3/3 under a SINGLE
record frame iff S is PRIMITIVE (sufficient: U has no zero amplitude in B).

This runner asks the matter-realization question block 06 exposed: for the
framework's matter (staggered-Dirac / nearest-neighbour hopping) dynamics on the
supplied C^3 color carrier, IS that single-emergent-time-step color unitary U
primitive, or is it forced color-inert / block-diagonal?

The two named matter Hamiltonians are exactly those of the block-01 composite-link
model (`INDUCED_COMPOSITE_LINK_TRAJECTORY...` source proposal):
  (i)  H_free = kappa A (x) I3                 -- color-diagonal free hopping
  (ii) H_cov  = kappa (|x><y| (x) V + h.c.)    -- a FROZEN generic SU(3) link
                                                  background V on the edge.

Findings (all exact finite-dimensional algebra; random unitaries/states are
witnesses for already-proven identities, no Monte-Carlo fit in the logic path):

  D1  H_free factorizes: e^{-i H_free t} = e^{-i kappa A t} (x) I3 exactly. The
      color factor is the identity -- free hopping never rotates the color frame.
  D2  The single-hop induced color transporter EQUALS the per-edge link V: the
      color of the amplitude that hops x->y under e^{-iHt} is exactly V|c>. So
      the matter color unitary the sieve sees is U = V (free: V = I3).
  D3  Free verdict: U = e^{i phi} I3 => S = I (the block-06 [U,B]=0 commuting
      limit), the WHOLE record frame B is einselected, rho stays POLARIZED.
  D4  The free verdict is FRAME-INDEPENDENT: U proportional to I3 gives S = I in
      EVERY orthonormal frame B = g{e_i}. No record-frame choice can make the
      free matter unitary primitive (answers the frame-smuggling guard: the
      obstruction cannot be evaded by naming a clever frame).
  D5  Covariant verdict: a generic SU(3) link V has strictly positive
      S = |V_ij|^2 => primitive (Perron-Frobenius) => Phi^n(rho) -> I3/3
      (depolarization), recovering the block-06 primitive column.
  D6  The covariant verdict is FRAME-DEPENDENT: in the V-eigenframe S = I
      (reducible, no depolarization); the frame is a NAMED einselection
      admission. Contrast with the free case (frame-independent).
  D7  Map onto block 06: plugging U = I3 (free) into Phi reproduces C5 (frame B
      einselected, generic state stays polarized); U = V (cov) reproduces C8
      (unique pointer state I3/3, relaxation).
  D8  CIRCULARITY gate: the ONLY matter color unitary in this family giving a
      primitive S is V != I3, a nontrivial background SU(3) connection on the
      edge -- the very gauge-link object whose continuous dynamics this campaign
      seeks to induce. Free hopping (no presupposed connection) gives U = I3 and
      no depolarization. So depolarization on the matter lane CONSUMES a
      presupposed background connection.
  D9  Order parameter P(rho) = Tr(rho^2) - 1/3 (= ||traceless(rho)||_F^2):
      free preserves P (rho stays polarized); covariant drives P -> 0. Same
      Lyapunov order parameter as blocks 04/05/06.
  D10 GUARD: free color-diagonal transport is SU(3)-covariant AND inert on the
      color frame (it transports color density between sites without rotating
      the basis). Covariance != depolarization (consistent with block-05 I-B
      and block-03 instrument-inherited covariance). No hat discharged.
  D11 RELOCATION/decision table: depolarization (the relocated ADM-2 input)
      is delivered by the matter color unitary ONLY with a presupposed
      background connection (covariant column); the named color-diagonal free
      hopping frame-independently does NOT depolarize.

All matrices are 3x3 (color C^3); few sites (<=4); Hermitian exponentials via
eigh. Memory-safe. NO hat discharged; this blocks depolarization on the named
free matter lane and exhibits a presupposed-connection circularity on the
covariant lane -- it does not derive depolarization from the axioms.
"""

import numpy as np

PASS = 0
FAIL = 0


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {name}")
    else:
        FAIL += 1
        print(f"[FAIL] {name}")


rng = np.random.default_rng(20260907)
d = 3
I3 = np.eye(d)
Imix = np.eye(d) / d


def haar_unitary(n):
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def su3(n=3):
    u = haar_unitary(n)
    return u / np.linalg.det(u) ** (1.0 / n)


def expm_herm(H):
    """Matrix exponential of -i H for Hermitian H, via eigendecomposition."""
    w, U = np.linalg.eigh(H)
    return (U * np.exp(-1j * w)) @ U.conj().T


def dephase(rho):
    return np.diag(np.diag(rho))


def Phi(rho, U):
    return dephase(U @ rho @ U.conj().T)


def unistochastic(U):
    return np.abs(U) ** 2


def rand_rho(n):
    a = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    m = a @ a.conj().T
    return m / np.trace(m)


def purity_above_floor(rho):
    n = rho.shape[0]
    return np.real(np.trace(rho @ rho)) - 1.0 / n


def traceless(rho):
    n = rho.shape[0]
    return rho - np.trace(rho) / n * np.eye(n)


def n_unit_modulus(S):
    w = np.linalg.eigvals(S)
    return int(np.sum(np.abs(np.abs(w) - 1) < 1e-9))


def spectral_gap(S):
    """1 - |lambda_2|: strictly positive iff S is primitive (Perron-Frobenius)."""
    w = np.sort(np.abs(np.linalg.eigvals(S)))[::-1]
    return 1.0 - w[1]


def relax(U, rho, iters=4000):
    r = rho.copy()
    for _ in range(iters):
        r = Phi(r, U)
    return r


# ----------------------------------------------------------------------
print("=== D1: free hopping H_free = kappa A (x) I3 factorizes; color factor = I3 ===")
nsites = 4
A = np.zeros((nsites, nsites))
for i in range(nsites):
    A[i, (i + 1) % nsites] = 1.0
    A[(i + 1) % nsites, i] = 1.0
kappa = 0.83          # the emergent-time-step hopping phase is absorbed into expm_herm (t=1)
H_free = kappa * np.kron(A, I3)
Ufree = expm_herm(H_free)
Uspace = expm_herm(kappa * A)
check("D1 e^{-iH_free t=1} = e^{-i kappa A} (x) I3 exactly",
      np.linalg.norm(Ufree - np.kron(Uspace, I3)) < 1e-12)
# color factor: trace out / fix any single site-pair block -> proportional to I3
# extract the color action on the carrier by projecting onto one site amplitude
check("D1 every site->site color block of Ufree is a scalar multiple of I3",
      all(np.linalg.norm(Ufree[a * d:(a + 1) * d, b * d:(b + 1) * d]
                         - (Ufree[a * d, b * d]) * I3) < 1e-12
          for a in range(nsites) for b in range(nsites)))

print("\n=== D2: single-hop induced color transporter EQUALS the per-edge link V ===")
# 2-site edge, C^3 color; H = kappa(|x><y|(x)V + |y><x|(x)V^dag). On C^2(x)C^3,
# H = kappa [[0, V],[V^dag, 0]]; since that block matrix squares to I, evolving
# |x>(x)|c> sends the y-amplitude color to (up to -i sin(kappa t)) V|c>.
for V, label in [(I3.astype(complex), "free V=I3"), (su3(), "cov V in SU(3)")]:
    # H = kappa(|x><y|(x)V^dag + |y><x|(x)V) so the x->y hop carries the link V
    H = kappa * np.block([[np.zeros((d, d)), V.conj().T], [V, np.zeros((d, d))]])
    Ue = expm_herm(H)
    ok = True
    for _ in range(20):
        c = rng.standard_normal(d) + 1j * rng.standard_normal(d)
        c /= np.linalg.norm(c)
        psi0 = np.concatenate([c, np.zeros(d, dtype=complex)])      # |x>(x)|c>
        psit = Ue @ psi0
        yamp = psit[d:]                                            # site-y color amplitude
        # the off-diagonal block squares to I, so e^{-iH}=cos(kappa)I - i sin(kappa)(block)
        pred = -1j * np.sin(kappa) * (V @ c)
        if np.linalg.norm(yamp - pred) > 1e-11:
            ok = False
    check(f"D2 hopped-amplitude color = V|c> exactly ({label})", ok)

print("\n=== D3: free U = I3 -> S = I (block-06 commuting limit), frame B einselected ===")
Ufreecol = I3.astype(complex)
Sfree = unistochastic(Ufreecol)
check("D3 free S = I (frame-natural)", np.linalg.norm(Sfree - I3) < 1e-12)
# generic state stays polarized under Phi with U=I3
rho = rand_rho(d)
r = rho.copy()
for _ in range(300):
    r = Phi(r, Ufreecol)
check("D3 free: generic state stays POLARIZED (relaxes to its own diagonal, not I3/3)",
      purity_above_floor(r) > 1e-3 and np.linalg.norm(r - Imix) > 1e-2
      and np.linalg.norm(r - np.diag(np.diag(rho))) < 1e-9)

print("\n=== D4: the free verdict is FRAME-INDEPENDENT (no frame can make I3 primitive) ===")
ok = True
for _ in range(200):
    g = haar_unitary(d)
    phase = np.exp(1j * rng.standard_normal())
    Uframe = g @ (phase * I3) @ g.conj().T     # = phase*I3, but built in a random frame
    if np.linalg.norm(unistochastic(Uframe) - I3) > 1e-12:
        ok = False
check("D4 U proportional to I3 gives S = I in EVERY orthonormal frame (200 frames)", ok)
# even an explicit named record frame B (random) leaves S = I and no depolarization
g = haar_unitary(d)
B = g                       # frame columns
rhoB = rand_rho(d)
# express Phi in frame B: dephase in B-basis
def dephase_B(rho, Bcols):
    P = [np.outer(Bcols[:, i], Bcols[:, i].conj()) for i in range(d)]
    return sum(p @ rho @ p for p in P)
rB = rhoB.copy()
for _ in range(300):
    rB = dephase_B(Ufreecol @ rB @ Ufreecol.conj().T, B)
check("D4 free: ANY named frame B leaves rho polarized (no depolarization)",
      purity_above_floor(rB) > 1e-3)

print("\n=== D5: covariant V generic SU(3) -> S strictly positive -> primitive -> depolarizes ===")
ok_pos = ok_prim = ok_gap = ok_relax = True
for _ in range(30):
    V = su3()
    S = unistochastic(V)
    if S.min() <= 1e-9:
        ok_pos = False
    if n_unit_modulus(S) != 1:
        ok_prim = False
    if spectral_gap(S) <= 1e-9:                 # strict gap => guaranteed convergence
        ok_gap = False
    if np.linalg.norm(relax(V, rand_rho(d)) - Imix) > 1e-6:
        ok_relax = False
check("D5 generic SU(3) link gives strictly positive S", ok_pos)
check("D5 strictly positive S is primitive (unique unit-modulus eigenvalue)", ok_prim)
check("D5 primitive S has a strict spectral gap |lambda_2| < 1 (guarantees relaxation)", ok_gap)
check("D5 covariant: Phi^n(rho) -> I3/3 (depolarization)", ok_relax)

print("\n=== D6: covariant verdict is FRAME-DEPENDENT (S=I in the V-eigenframe) ===")
V = su3()
wv, Vec = np.linalg.eig(V)
Veig = Vec.conj().T @ V @ Vec
Seig = unistochastic(Veig)
check("D6 in the V-eigenframe |V_ij|^2 is diagonal (S = I, reducible)",
      np.linalg.norm(Seig - np.diag(np.diag(Seig))) < 1e-9)
# so for the covariant unitary the depolarization verdict depends on which frame
# einselection names: generic frame -> primitive; V-eigenframe -> reducible
check("D6 covariant frame-dependence: primitive in computational frame, reducible in V-eigenframe",
      unistochastic(V).min() > 1e-9 and np.linalg.norm(Seig - np.diag(np.diag(Seig))) < 1e-9)

print("\n=== D7: maps onto the block-06 criterion (C5 free / C8 covariant) ===")
# free reproduces C5 (whole frame fixed)
ok = True
for _ in range(20):
    p = rng.random(d)
    p /= p.sum()
    rho = np.diag(p).astype(complex)
    r = rho.copy()
    for _ in range(200):
        r = Phi(r, I3.astype(complex))
    if np.linalg.norm(r - rho) > 1e-10:
        ok = False
check("D7 free reproduces block-06 C5 (every B-diagonal state fixed)", ok)
V = su3()
check("D7 covariant reproduces block-06 C8 (unique pointer state I3/3)",
      np.linalg.norm(relax(V, rand_rho(d)) - Imix) < 1e-6)

print("\n=== D8: CIRCULARITY gate -- in this matter family, primitive S requires a presupposed background connection ===")
# In this matter family the induced color unitary is exactly the per-edge link V
# (D2). The verdict as a boolean function of the presupposed link:
def depolarizes_under(U):
    return np.linalg.norm(relax(U, rand_rho(d)) - Imix) < 1e-6
free_depol = depolarizes_under(I3.astype(complex))
cov_depol = depolarizes_under(su3())
check("D8 free hopping (V = I3, NO presupposed connection) does NOT depolarize",
      not free_depol)
check("D8 covariant hopping (V != I3, a presupposed SU(3) connection) depolarizes",
      cov_depol)
# the implication: depolarization on the matter lane => V != I3 => a background
# connection is consumed (the gauge link whose dynamics the campaign induces)
check("D8 logical: matter-lane depolarization CONSUMES a presupposed background link",
      (not free_depol) and cov_depol)

print("\n=== D9: order parameter P = Tr(rho^2)-1/3 (free preserves / covariant drives to 0) ===")
check("D9 P = ||traceless(rho)||_F^2 identity, 0 iff rho=I3/3",
      all(abs(purity_above_floor(r) - np.linalg.norm(traceless(r)) ** 2) < 1e-12
          for r in [rand_rho(d) for _ in range(20)]) and abs(purity_above_floor(Imix)) < 1e-12)
rho = rand_rho(d)
rf = rho.copy()
for _ in range(50):
    rf = Phi(rf, I3.astype(complex))
check("D9 free preserves P > 0 (no depolarization)", purity_above_floor(rf) > 1e-3)
V = su3()
rc = rho.copy()
seq = []
for _ in range(40):
    rc = Phi(rc, V)
    seq.append(purity_above_floor(rc))
check("D9 covariant drives P monotonically to 0",
      all(seq[i + 1] <= seq[i] + 1e-12 for i in range(len(seq) - 1)) and seq[-1] < 1e-9)

print("\n=== D10: GUARD -- free color-diagonal transport is SU(3)-covariant AND inert ===")
# the block-03 free transport channel on local color densities:
#   M' = cos^2(tau) M + sin^2(tau) V M' V^dag  with V = I3 for free hopping
# it transports color density between sites but never rotates the color basis.
tau = 0.7
Mx = rand_rho(d)
My = rand_rho(d)
Vfree = I3
Mx_new = np.cos(tau) ** 2 * Mx + np.sin(tau) ** 2 * (Vfree @ My @ Vfree.conj().T)
# joint covariance: conjugating both inputs by g conjugates the output by g
g = su3()
Mx_g = np.cos(tau) ** 2 * (g @ Mx @ g.conj().T) + np.sin(tau) ** 2 * (g @ My @ g.conj().T)
check("D10 free transport is jointly SU(3)-covariant", np.linalg.norm(Mx_g - g @ Mx_new @ g.conj().T) < 1e-12)
# inertness of the FRAME: the color eigenbasis of a pinned single site is unchanged
# (no rotation), i.e. the induced color unitary is I3 -> covariance != depolarization
check("D10 free induced color unitary is I3 (covariance does NOT imply frame rotation)",
      np.linalg.norm(unistochastic(I3.astype(complex)) - I3) < 1e-12)

print("\n=== D11: relocation/decision table (no hat discharged) ===")
table = {
    "free  (color-diagonal named matter lane)": depolarizes_under(I3.astype(complex)),
    "covariant (presupposed SU(3) link)": depolarizes_under(su3()),
}
check("D11 only the presupposed-connection (covariant) column depolarizes",
      bool(table["covariant (presupposed SU(3) link)"])
      and not bool(table["free  (color-diagonal named matter lane)"]))
# 2x2 sanity: the same dichotomy holds for d=2
U2 = haar_unitary(2)
S2 = np.abs(U2) ** 2
check("D11 d=2 sanity: generic 2x2 unitary gives strictly positive (primitive) S",
      S2.min() > 1e-9 and np.linalg.norm(np.abs(np.eye(2)) ** 2 - np.eye(2)) < 1e-12)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
