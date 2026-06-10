"""Block 09 runner -- the three ADM-2 color-depolarization mechanisms collapse
to TWO irreducible gauge-structure admissions, neither supplied by Lattice + Quantum + Record.

Context. The gauge-link / color-einselection campaign reduced the undelivered
gauge-link generator's R2 input to a single matter question (ADM-2): does the
matter dynamics depolarize the single-carrier color density rho_color to the
color-blind I3/3 on the C^3 fundamental carrier? Blocks 04-08 mapped that input
onto THREE distinct mechanisms, each gated by a named admission:

  * TWIRL (block 05; landed Fierz-channel reading): an averaging map needing a
    >=2-element complementary-frame / multi-instrument average with a UNIFORM
    weight Record does not supply;
  * PRIMITIVITY (blocks 06/07): a single record frame B + a PRIMITIVE matter
    color unitary U (unistochastic S_ij = |<e_i|U|e_j>|^2 primitive) -> I3/3;
  * ENTANGLEMENT (block 08): a partial trace of a GLOBAL-SU(3)-invariant joint
    two-carrier matter state (Schur) -> I3/3.

Continuing to relocate ADM-2 onto a fresh admission per block is corollary
churn. This runner consolidates instead: it records, with exact finite-
dimensional linear algebra, that the three mechanisms collapse to exactly TWO
irreducible admissions, and that BOTH coincide with the gauge-structure objects
the campaign is trying to induce -- so neither is supplied by Lattice + Quantum + Record.

  COLLAPSE STEP 1 (TWIRL == PRIMITIVITY).  The twirl's load-bearing element --
  the UNIFORM averaging weight that lands the marginal exactly on I3/3 rather
  than at some other diagonal point -- is supplied by Quantum, not by
  Record: for ANY unitary U the unistochastic matrix S_ij = |U_ij|^2 is doubly
  stochastic (rows AND columns sum to 1), so its stationary vector is forced
  uniform (= I3/3) whenever S is primitive. A generic NON-unitary primitive
  column-stochastic kick relaxes to a NON-uniform stationary vector -- so the
  uniform weight is pinned by unitarity, not chosen. What then survives of the
  twirl mechanism is exactly the primitivity mechanism's residual: a named
  record frame B (record_formation_not_unconditionally_forced = retained_no_go)
  PLUS a primitive U. And a primitive S requires a generic non-diagonal SU(3)
  link V != I3 -- a presupposed LOCAL connection (the gauge link the campaign
  induces; circular). Free color-diagonal hopping gives S = I frame-
  INDEPENDENTLY (no depolarization).

  COLLAPSE STEP 2 (ENTANGLEMENT == GLOBAL GAUSS-LAW ADMISSION).  Schur delivers
  rho_A = I3/3 from a GLOBAL-invariant joint state, but the step "the realized
  matter STATE is a global SU(3) singlet" is NOT entailed by "observables are
  SU(3)-invariant": invariance of the observable algebra constrains the
  commutant and leaves the superselection sector free; a polarized marginal is
  consistent with every invariant observable. Selecting the singlet sector is a
  physical-state (color Gauss-law) condition. Total color charge is moreover
  conserved under the global/covariant action, so neutrality is an initial-
  condition admission, not dynamically forced.

So the THREE mechanisms gate on TWO admissions:
  (A) a presupposed LOCAL SU(3) connection V != I3 (+ a named record frame B)
      -- covers TWIRL and PRIMITIVITY;
  (B) a GLOBAL color-singlet / Gauss-law physical-state condition
      -- covers ENTANGLEMENT.
(A) is the gauge link the campaign seeks to INDUCE (circular to consume); (B)
is global color confinement (an import; the confinement corpus on main is
unaudited and imports scale-setting, not axiom-derived). Neither is supplied by
Lattice + Quantum + Record. This BOUNDS ADM-2 depolarization as admission-gated across all
mechanisms mapped this campaign and identifies the two gates with the two
undelivered gauge-structure objects. NO hat is discharged (ADM-1, R1 link
generator, R2 link-measure delivery, blocking isometry untouched); this is a
bounded consolidation, NOT a no-go -- the open paths are auditing #3332's
local-connection forcing, a future structural color-Gauss-law premise, and the
comparatively unworked blocking-isometry hat.

All checks are exact finite-dimensional linear algebra on C^3 and C^3 (x) C^3;
random SU(3) / unitary elements with fixed seeds are witnesses for already-
proven identities, NOT Monte-Carlo fits in the logic path. Memory-safe (3x3
and 9-dim only; no large dense inverses).
"""

import numpy as np

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name}")


def haar_unitary(n, rng):
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diagonal(r)
    return q @ np.diag(d / np.abs(d))


def special_unitary(n, rng):
    """Haar U(n) witness phase-normalized into SU(n); absolute entries are unchanged."""
    U = haar_unitary(n, rng)
    root = np.exp(1j * np.angle(np.linalg.det(U)) / n)
    return U / root


def stationary_col_stochastic(S):
    """Right eigenvector of column-stochastic S for eigenvalue 1, normalized to a
    probability vector (S p = p)."""
    w, V = np.linalg.eig(S)
    idx = int(np.argmin(np.abs(w - 1.0)))
    p = np.real(V[:, idx])
    return p / p.sum()


def marginal_A(psi_or_rho):
    """Partial trace over carrier B of a C^3 (x) C^3 vector or 9x9 density op."""
    arr = np.asarray(psi_or_rho)
    if arr.ndim == 1:
        rho = np.outer(arr, arr.conj())
    else:
        rho = arr
    return np.einsum("ijkj->ik", rho.reshape(3, 3, 3, 3))


I3 = np.eye(3)
TOL = 1e-10


def order_param(rho):
    """P = Tr(rho^2) - 1/3 ; zero iff rho = I3/3 (color-blind floor)."""
    return float(np.real(np.trace(rho @ rho)) - 1.0 / 3.0)


# ======================================================================
# GROUP 1 -- COLLAPSE STEP 1a: the twirl's uniform weight is Quantum-supplied
#            (unitarity => doubly stochastic => uniform stationary).
# ======================================================================
rng = np.random.default_rng(20260609)

ds_ok = True
unif_ok = True
for _ in range(200):
    U = haar_unitary(3, rng)
    S = np.abs(U) ** 2
    if not (np.allclose(S.sum(0), 1.0, atol=TOL) and np.allclose(S.sum(1), 1.0, atol=TOL)):
        ds_ok = False
check("G1.1 unitary U => S_ij=|U_ij|^2 is doubly stochastic (rows & cols sum 1)", ds_ok)

# uniform vector is exactly stationary for every doubly-stochastic S
unif = np.ones(3) / 3.0
for _ in range(200):
    U = haar_unitary(3, rng)
    S = np.abs(U) ** 2
    if not np.allclose(S @ unif, unif, atol=TOL):
        unif_ok = False
check("G1.2 uniform (1/3,1/3,1/3) is stationary for every unitary-induced S", unif_ok)

# for a PRIMITIVE unitary-induced S the stationary vector is the UNIQUE uniform one
prim_unique = True
for _ in range(50):
    U = haar_unitary(3, rng)
    S = np.abs(U) ** 2
    if np.min(S) <= 1e-6:  # skip degenerate (a Haar U a.s. has no zero amplitude)
        continue
    p = stationary_col_stochastic(S)
    if not np.allclose(p, unif, atol=1e-8):
        prim_unique = False
check("G1.3 primitive unitary-induced S => UNIQUE stationary vector = uniform", prim_unique)

# ======================================================================
# GROUP 2 -- COLLAPSE STEP 1b: the uniform weight is NOT free -- a generic
#            NON-unitary primitive column-stochastic kick relaxes to a
#            NON-uniform stationary vector. So uniformity needs unitarity,
#            i.e. it is Quantum-supplied, not a Record-supplied averaging weight.
# ======================================================================
nonunif_seen = False
for _ in range(200):
    A = rng.random((3, 3))
    A = A / A.sum(0)  # generic column-stochastic, primitive (all entries > 0)
    p = stationary_col_stochastic(A)
    if np.max(np.abs(p - unif)) > 1e-3:
        nonunif_seen = True
check("G2.1 generic non-unitary primitive col-stochastic => NON-uniform stationary", nonunif_seen)

# a deliberately biased doubly-stochastic-broken example: column-stochastic but
# rows not summing to 1 -> stationary tilts away from uniform (witness)
A = np.array([[0.8, 0.1, 0.1], [0.1, 0.8, 0.2], [0.1, 0.1, 0.7]])
p = stationary_col_stochastic(A)
check("G2.2 non-doubly-stochastic witness has stationary != uniform", np.max(np.abs(p - unif)) > 1e-3)

# ======================================================================
# GROUP 3 -- COLLAPSE STEP 1c: free color-diagonal hopping gives S=I
#            FRAME-INDEPENDENTLY (no primitivity, no depolarization); a
#            primitive S requires a generic non-diagonal SU(3) link V != I3.
# ======================================================================
phases = [0.0, 0.7, 1.3, -2.1]
free_SI = all(np.allclose(np.abs(np.exp(1j * ph) * I3) ** 2, I3) for ph in phases)
check("G3.1 free color-diagonal U = e^{i phi} I3 => S = I3 (not primitive)", free_SI)

# frame independence: a scalar unitary stays scalar (S = I) in EVERY orthonormal frame
frame_indep = True
for _ in range(100):
    W = haar_unitary(3, rng)
    Up = W.conj().T @ (np.exp(0.9j) * I3) @ W
    if not np.allclose(np.abs(Up) ** 2, I3, atol=TOL):
        frame_indep = False
check("G3.2 scalar U is frame-INDEPENDENT: S = I3 in every frame (no frame rescue)", frame_indep)

# a generic SU(3) link V != I3 induces a primitive S that depolarizes:
# iterate Phi(rho) = D(V rho V^dag) (D = dephasing in the computational frame)
def dephase(rho):
    return np.diag(np.diag(rho))


def phi_step(rho, V):
    return dephase(V @ rho @ V.conj().T)


V = special_unitary(3, rng)  # generic SU(3) link, no zero amplitude a.s.
rho0 = np.diag([1.0, 0.0, 0.0])  # polarized start, P = 2/3
rho = rho0.copy()
for _ in range(400):
    rho = phi_step(rho, V)
check("G3.3 generic link V != I3 => primitive S => rho -> I3/3 (P -> 0)", abs(order_param(rho)) < 1e-6)

# but that depolarizing object IS a non-diagonal SU(3) link (off-diagonal weight),
# i.e. exactly the presupposed connection (S = |V|^2 != I3):
check("G3.4 the depolarizing U is a non-diagonal link (S != I3 = a connection)",
      not np.allclose(np.abs(V) ** 2, I3, atol=1e-3))

# the free lane does NOT depolarize: Phi with V = I3 is the identity on diagonal
rho = rho0.copy()
for _ in range(400):
    rho = phi_step(rho, I3)
check("G3.5 free lane (V = I3): rho stays polarized (P unchanged = 2/3)",
      abs(order_param(rho) - 2.0 / 3.0) < TOL)

# ======================================================================
# GROUP 4 -- continuity of the collapse: a 1-parameter family U(theta) from the
#            scalar subgroup (theta=0) to a generic link shows the depolarization
#            onset coincides exactly with U LEAVING the color-diagonal (scalar)
#            sector -- i.e. acquiring connection content. (twirl/primitivity
#            depolarization <=> a non-trivial local connection.)
# ======================================================================
X = haar_unitary(3, rng)
# Hermitian generator with off-diagonal content; theta scales the OFF-diagonal mixing
H = X + X.conj().T
Hoff = H - np.diag(np.diag(H))  # purely off-diagonal Hermitian generator


def U_theta(theta):
    from numpy.linalg import eigh
    w, Vv = eigh(theta * Hoff)
    return Vv @ np.diag(np.exp(-1j * w)) @ Vv.conj().T


# theta = 0 -> identity scalar -> no depolarization; theta generic -> depolarizes
def depolarizes(theta, nsteps=600):
    U = U_theta(theta)
    rho = rho0.copy()
    for _ in range(nsteps):
        rho = dephase(U @ rho @ U.conj().T)
    return abs(order_param(rho)) < 1e-5


check("G4.1 theta=0 (U scalar, no connection content): does NOT depolarize", not depolarizes(0.0))
check("G4.2 theta generic (U off-diagonal = connection content): DOES depolarize", depolarizes(0.6))

# the onset is tied to off-diagonal (connection) content: S = I iff Hoff content = 0
check("G4.3 S = I3 exactly at theta = 0 (scalar) and != I3 for generic theta",
      np.allclose(np.abs(U_theta(0.0)) ** 2, I3) and not np.allclose(np.abs(U_theta(0.6)) ** 2, I3, atol=1e-3))

# ======================================================================
# GROUP 5 -- COLLAPSE STEP 2: the ENTANGLEMENT mechanism gates on a GLOBAL
#            color-singlet / Gauss-law admission, distinct from a connection.
# ======================================================================
# singlet |s> = (1/sqrt3) sum_i |i,ibar>  -> marginal = I3/3
s = np.zeros(9)
for i in range(3):
    s[i * 3 + i] = 1.0 / np.sqrt(3.0)
rhoA_singlet = marginal_A(s)
check("G5.1 q-qbar singlet marginal = I3/3 (P = 0)", abs(order_param(rhoA_singlet)) < TOL)

# Schur: a GLOBAL-invariant mixture (singlet projector + octet identity) -> I3/3
P1 = np.outer(s, s.conj())
P8 = np.eye(9) - P1  # complement; both are g(x)gbar invariant subspaces (1 (+) 8 split)
rho_inv = 0.3 * P1 + 0.7 * (P8 / 8.0)
check("G5.2 Schur: generic GLOBAL-invariant joint state has marginal I3/3",
      abs(order_param(marginal_A(rho_inv))) < TOL)

# verify invariance of rho_inv under g (x) conj(g) for random g (witness of the premise)
inv_ok = True
for _ in range(50):
    g = special_unitary(3, rng)
    G = np.kron(g, g.conj())
    if not np.allclose(G @ rho_inv @ G.conj().T, rho_inv, atol=1e-9):
        inv_ok = False
check("G5.3 the Schur premise really is GLOBAL-action invariance g (x) conj(g)", inv_ok)

# CRUX: "observables invariant" does NOT entail "state singlet": a NON-invariant
# (polarized) joint state has a POLARIZED marginal -> neutrality is a real extra
# constraint, not automatic.
prod = np.zeros(9)
prod[0] = 1.0  # |0, 0bar>, a non-singlet product state
check("G5.4 non-singlet product state => POLARIZED marginal (P = 2/3 > 0)",
      abs(order_param(marginal_A(prod)) - 2.0 / 3.0) < TOL)

# color charge is CONSERVED under the global action: a charged (non-singlet)
# two-carrier state stays charged -> dynamics does not drive it to the singlet.
def casimir_total(psi):
    """Quadratic Casimir of the TOTAL color on C^3 (x) C^3bar via the generators
    T^a (x) I + I (x) (-T^a*) summed; nonzero iff the joint state carries net color."""
    # Gell-Mann (normalized Tr(T^a T^b) = 1/2 delta_ab)
    lam = gellmann()
    Ta = [0.5 * l for l in lam]
    rho = np.outer(psi, psi.conj())
    val = 0.0
    for T in Ta:
        Jtot = np.kron(T, np.eye(3)) + np.kron(np.eye(3), -T.conj())
        val += np.real(np.trace(rho @ (Jtot @ Jtot)))
    return val


def gellmann():
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / np.sqrt(3.0)
    return [l1, l2, l3, l4, l5, l6, l7, l8]


C_singlet = casimir_total(s)
C_charged = casimir_total(prod)
check("G5.5 total-color Casimir = 0 on the singlet, > 0 on the charged state",
      abs(C_singlet) < 1e-9 and C_charged > 1e-6)

# conservation: under the global action g (x) conj(g) (the SAME action that
# defines the invariance premise and the total-color generator) the total
# Casimir is invariant -- a charged state cannot be rotated into the singlet by
# the global/covariant dynamics.
cons_ok = True
for _ in range(50):
    g = special_unitary(3, rng)
    G = np.kron(g, g.conj())  # global color action on 3 (x) 3bar
    psi2 = G @ prod
    if abs(casimir_total(psi2) - C_charged) > 1e-7:
        cons_ok = False
check("G5.6 total color Casimir conserved under global action (charge not driven to 0)", cons_ok)

# ======================================================================
# GROUP 6 -- the lone carrier cannot self-depolarize (Schur): no SU(3)-invariant
#            pure state and no invariant projector beyond 0, I3 on a single C^3.
#            (entanglement route is irreducibly multi-carrier; distinct from a
#            local connection or a frame.)
# ======================================================================
lam = gellmann()
# the only operators commuting with all generators on the irrep C^3 are scalars.
# EXACT check: the commutant {M : [M, lam_a] = 0 for all a} has dimension 1.
# Build the stacked superoperator whose null space is the commutant.
rows = []
for l in lam:
    # vec([M, l]) = (I (x) M - M^T (x) I) vec ... use the adjoint map L(M)=M l - l M
    L = np.kron(l.T, I3) - np.kron(I3, l)  # vec(M l - l M) = (l^T (x) I - I (x) l) vec(M)
    rows.append(L)
A_comm = np.vstack(rows)  # (8*9) x 9
sv = np.linalg.svd(A_comm, compute_uv=False)
null_dim = int(np.sum(sv < 1e-9))
check("G6.1 Schur on C^3 (EXACT): commutant of the SU(3) generators is 1-dimensional (= C.I3)",
      null_dim == 1)

# ======================================================================
# GROUP 7 -- discipline gates (each an explicit guarded fact, no check(True)).
# ======================================================================
# D1 no hat discharged: this consolidation delivers depolarization on NEITHER
#    admission -- both lanes still require an undelivered object. Encode as: the
#    free/scalar lane does NOT reach I3/3 AND the singlet lane needs a non-product
#    (entangled, neutrality-constrained) state, i.e. neither Lattice/Quantum/Record default
#    (free hopping + arbitrary product matter state) depolarizes.
rho = rho0.copy()
for _ in range(400):
    rho = phi_step(rho, I3)
free_default_polarized = abs(order_param(rho) - 2.0 / 3.0) < TOL
product_default_polarized = abs(order_param(marginal_A(prod)) - 2.0 / 3.0) < TOL
check("G7.1 no hat discharged: free-hop + product-state default stays POLARIZED on both lanes",
      free_default_polarized and product_default_polarized)

# D2 the two admissions are DISTINCT objects: a local connection (single-carrier,
#    off-diagonal SU(3)) vs a global singlet (two-carrier, entangled). A local
#    connection on one carrier does NOT make a product state's marginal mixed
#    unless it is itself primitive+iterated (lane A), and the global singlet uses
#    NO local connection (lane B). Witness: applying g (x) g* (global, no link)
#    leaves a product state's marginal polarized.
g = special_unitary(3, rng)
Gg = np.kron(g, g.conj())
prod_rot = Gg @ prod
check("G7.2 admissions distinct: global action alone leaves a non-neutral marginal polarized",
      order_param(marginal_A(prod_rot)) > 1e-3)

# D3 weight-leak guard (Fierz no-go side): I3/3 here is FORCED by invariance /
#    unitarity, never assigned by fiat -- a non-invariant / non-unitary input gives
#    a non-I3/3 result (already shown G2.1, G5.4). Encode the paired guard:
check("G7.3 weight-leak guard: I3/3 forced (invariant->mixed, non-invariant->polarized)",
      abs(order_param(rhoA_singlet)) < TOL and order_param(marginal_A(prod)) > 1e-3)

# D4 no closing language / not a no-go: the bound is conditional on the named
#    matter family + carrier; encode the conditionality witness -- a DIFFERENT
#    (presupposed-connection) input DOES depolarize, so the wall is the missing
#    object, not an impossibility.
check("G7.4 not-a-no-go witness: supplying the named object (a link) DOES depolarize",
      depolarizes(0.6))

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
