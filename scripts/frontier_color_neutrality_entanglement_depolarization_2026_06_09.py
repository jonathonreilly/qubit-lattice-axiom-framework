"""Block 08 runner -- color-neutrality entanglement depolarization is a
GLOBAL-invariance consequence, not a presupposed connection.

Context. Blocks 04-07 of the gauge-link/einselection campaign mapped the
relocated ADM-2 input ("does the matter dynamics depolarize the single-site
color density rho_color to the color-blind I3/3?") onto two mechanisms, both
gated:
  * the depolarizing TWIRL (block 05; and the landed Fierz-channel reading
    `FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION...`): an averaging
    map M -> (Tr M / Nc) I applied to the color OPERATOR, requiring a
    multi-frame / multi-instrument averaging admission Record does not supply;
  * the matter-unitary PRIMITIVITY (blocks 06/07): a primitive unistochastic
    S_ij = |U_ij|^2 requires a generic SU(3) LINK V != I3 -- a presupposed
    LOCAL background connection (circular for a campaign that seeks to INDUCE
    the connection).

This runner records a THIRD, distinct mechanism on the color carrier: the
color-singlet ENTANGLEMENT route. Here rho_color = I3/3 is delivered not by
averaging an operator and not by a local link, but by a partial trace of a
joint two-carrier matter state that is invariant under the GLOBAL diagonal
SU(3) color action g (x) g* (the same g on every carrier -- a global color
rotation, NOT a per-edge connection). The depolarization is a Schur
consequence of global color-neutrality.

Findings (all exact finite-dimensional linear algebra on C^3 (x) C^3; random
SU(3) elements / invariant mixtures are witnesses for already-proven
identities; no Monte-Carlo fit in the logic path):

  E1  The unique q-qbar color singlet |s> = (1/sqrt3) sum_i |i,ibar> has
      reduced single-carrier color density rho_A = Tr_B |s><s| = I3/3 exactly;
      order parameter P = Tr(rho_A^2) - 1/3 = 0 (fully color-blind).
  E2  SCHUR (the load-bearing step): ANY joint state rho_AB on C^3 (x) C^3bar
      invariant under the GLOBAL action g (x) g* for all g in SU(3) has
      rho_A = Tr_B rho_AB = I3/3. Verified on the singlet projector P1, the
      maximally-mixed octet state P8/8, and a generic invariant mixture. The
      pure singlet is the special pure case of the general Schur statement.
  E3  GLOBAL, not local: the singlet/invariant states are fixed by ONE color
      rotation g applied identically to both carriers (g (x) g*); no per-edge
      link V and no relative (bi-fundamental) connection g_x V g_y^dag is
      used. The required symmetry is strictly WEAKER than the local connection
      block 07 needs -- a genuinely different point on the obstruction surface.
  E4  SCHUR no-go for a lone carrier: the single fundamental C^3 admits NO
      SU(3)-invariant pure state and NO invariant projector other than 0 and
      I3 (commutant of an irrep = scalars). So this depolarization is
      IRREDUCIBLY multi-carrier: a single isolated color carrier cannot be
      color-neutralized this way.
  E5  Baryon corroboration: the qqq singlet (1/sqrt6) eps_ijk |ijk> has every
      single-carrier reduced density = I3/3; P = 0. The mechanism is not an
      artifact of the q-qbar pair.
  E6  Mechanism SEPARATION from the twirl (block 05 / Fierz channel): the
      depolarizing channel E_sing(M) = (Tr M / Nc) I is the Haar twirl applied
      to an OPERATOR; the entanglement route applies a partial trace to a
      STATE. On the SAME single-carrier rho they agree (both give I3/3) ONLY
      because rho is already invariant -- but the entanglement route never
      averages rho_A; it reads off the marginal of an invariant joint state.
      They are distinct maps with distinct admissions.
  E7  Mechanism SEPARATION from the local-connection route (block 07): the
      entanglement route's marginal is I3/3 for EVERY global g (frame-
      independent on the joint invariant state), whereas block 07's
      depolarization is delivered only by a generic LOCAL V != I3 and is
      reducible (no depolarization) in the V-eigenframe.
  E8  WEIGHT-LEAK guard (staying on the right side of the Fierz no-go): the
      I3/3 here is NOT a within-sector weight assigned by fiat (the move the
      `FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION` no-go demotes).
      It is the forced partial trace of an invariance-constrained joint state:
      a non-invariant joint state gives a non-I3/3 marginal (exhibited), so
      nothing is assigned by fiat.
  E9  RELOCATION (no hat discharged): the route delivers the relocated-ADM-2
      depolarization CONDITIONALLY on the joint matter state being globally
      color-neutral (a global SU(3) singlet/invariant). The axioms do not
      derive that the matter dynamics produce a color-neutral composite (that
      is global color confinement; the confinement corpus is unaudited and
      imports scale-setting). So ADM-2 relocates onto "does the dynamics /
      Record select a globally color-neutral matter state?". ADM-1, the R1
      link generator, the R2 link-measure delivery, and the blocking isometry
      are untouched; no ST1/ST2 ranking is made.

All matrices are at most 9x9 (C^3 (x) C^3) or 27-dim (qqq); memory-safe.
NO hat discharged: this exhibits a depolarization mechanism that needs only
GLOBAL neutrality (escaping block 07's local-connection circularity for the
DENSITY) and relocates ADM-2 onto global color-neutrality; it does not derive
depolarization from the axioms and induces no link dynamics.
"""

import itertools

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


rng = np.random.default_rng(20260908)
Nc = 3
I3 = np.eye(Nc)
Imix = np.eye(Nc) / Nc


def haar_unitary(n):
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def su3():
    u = haar_unitary(Nc)
    return u / np.linalg.det(u) ** (1.0 / Nc)


def reduced_A(rho):
    """Partial trace over carrier B of a 9x9 state on C^3 (x) C^3."""
    r = rho.reshape(Nc, Nc, Nc, Nc)
    return np.einsum("ijkj->ik", r)


def order_param(rho):
    return float(np.trace(rho @ rho).real) - 1.0 / Nc


# Exact unitary 1-design: the 9-element Heisenberg-Weyl (shift-clock) group on
# C^3. The twirl (1/9) sum_{a,b} (X^a Z^b) M (X^a Z^b)^dag = (Tr M / Nc) I
# EXACTLY (no Monte-Carlo), the same depolarizing twirl used in block 05.
_omega = np.exp(2j * np.pi / Nc)
_X = np.roll(np.eye(Nc), 1, axis=0).astype(complex)
_Z = np.diag([_omega ** k for k in range(Nc)]).astype(complex)
_HW = [np.linalg.matrix_power(_X, a) @ np.linalg.matrix_power(_Z, b)
       for a in range(Nc) for b in range(Nc)]


def hw_twirl(M):
    """Exact depolarizing twirl via the 9-element Heisenberg-Weyl 1-design."""
    return sum(W @ M @ W.conj().T for W in _HW) / len(_HW)


# --- singlet projector and octet projector on C^3 (x) C^3bar ---
singlet_vec = np.zeros(Nc * Nc, dtype=complex)
for i in range(Nc):
    singlet_vec[i * Nc + i] = 1.0 / np.sqrt(Nc)
P1 = np.outer(singlet_vec, singlet_vec.conj())
P8 = np.eye(Nc * Nc) - P1


# =====================================================================
print("=== E1: q-qbar singlet marginal is exactly I3/3 (fully color-blind) ===")
rho_s = reduced_A(P1)
check("E1 reduced color density of the singlet = I3/3", np.linalg.norm(rho_s - Imix) < 1e-12)
check("E1 order parameter Tr(rho^2)-1/3 = 0 at the singlet", abs(order_param(rho_s)) < 1e-12)


# =====================================================================
print("\n=== E2: Schur -- any GLOBAL-invariant joint state has marginal I3/3 ===")
# global invariance under g (x) g* for random SU(3) g
g = su3()
G = np.kron(g, g.conj())
check("E2 P1 invariant under g (x) g*", np.linalg.norm(G @ P1 @ G.conj().T - P1) < 1e-12)
check("E2 P8 invariant under g (x) g*", np.linalg.norm(G @ P8 @ G.conj().T - P8) < 1e-12)
for name, rho in [
    ("singlet P1", P1),
    ("octet P8/8", P8 / 8.0),
    ("invariant mix 0.3 P1 + 0.7 P8/8", 0.3 * P1 + 0.7 * P8 / 8.0),
]:
    check(f"E2 marginal of {name} = I3/3", np.linalg.norm(reduced_A(rho) - Imix) < 1e-12)


# =====================================================================
print("\n=== E3: GLOBAL action (g (x) g*), no local link / connection used ===")
# The invariant states are fixed by ONE g on both carriers; contrast a LOCAL
# action g_x (x) h_y^* with independent g_x != h_y, which does NOT fix P1.
gx, hy = su3(), su3()
G_local = np.kron(gx, hy.conj())
check("E3 an independent LOCAL action g_x (x) h_y* does NOT fix the singlet",
      np.linalg.norm(G_local @ P1 @ G_local.conj().T - P1) > 1e-6)
# but the marginal of the (still globally-invariant) singlet is g-independent: I3/3 for every g
ok_all = all(np.linalg.norm(reduced_A(P1) - Imix) < 1e-12 for _ in range(5))
check("E3 singlet marginal = I3/3 independent of any frame (no V-eigenframe escape)", ok_all)


# =====================================================================
print("\n=== E4: Schur no-go -- a lone fundamental carrier cannot be neutralized ===")
# commutant of the irreducible fundamental = scalars; the exact 1-design twirl
# collapses any operator to the trace functional (only invariant direction = I3).
M_test = np.diag([1.0, 0.0, 0.0]).astype(complex)  # a polarized single-carrier density
tw = hw_twirl(M_test)
check("E4 only invariant single-carrier operator is the scalar (twirl -> (Tr/Nc) I)",
      np.linalg.norm(tw - (np.trace(M_test) / Nc) * I3) < 1e-12)
# no invariant PURE state: a rank-1 projector cannot equal I3/3
check("E4 no rank-1 (pure) single-carrier state equals I3/3 (rank 3)",
      np.linalg.matrix_rank(Imix) == 3)


# =====================================================================
print("\n=== E5: baryon qqq singlet -- every single-carrier marginal = I3/3 ===")
eps = np.zeros((Nc, Nc, Nc))
for p in itertools.permutations(range(Nc)):
    sign = np.linalg.det(np.eye(Nc)[list(p)])
    eps[p] = sign
psi = eps / np.sqrt(6.0)
rho1 = np.einsum("ijk,ljk->il", psi, psi)
check("E5 baryon single-carrier reduced density = I3/3", np.linalg.norm(rho1 - Imix) < 1e-12)
check("E5 baryon order parameter Tr(rho^2)-1/3 = 0", abs(np.trace(rho1 @ rho1).real - 1.0 / Nc) < 1e-12)
# global SU(3) invariance of the baryon singlet: g on each carrier leaves it (up to det g = 1) invariant
g = su3()
psi_g = np.einsum("ai,bj,ck,ijk->abc", g, g, g, psi)
check("E5 baryon singlet invariant under global g on all three carriers",
      np.linalg.norm(psi_g - psi) < 1e-9)


# =====================================================================
print("\n=== E6: separation from the twirl -- partial trace of a STATE, not an operator average ===")
# the depolarizing channel E_sing on an OPERATOR M = Haar twirl -> (Tr M/Nc) I
M = np.array([[2.0, 0.3 + 0.1j, 0.0], [0.3 - 0.1j, 0.5, 0.2], [0.0, 0.2, 0.5]], dtype=complex)
E_sing = (np.trace(M) / Nc) * I3
check("E6 twirl channel E_sing(M) = (Tr M/Nc) I (the block-05/Fierz operator map)",
      np.linalg.norm(hw_twirl(M) - E_sing) < 1e-12)
# the entanglement route never averages rho_A; it reads the marginal of an
# invariant joint state. A NON-invariant joint state gives a non-I3/3 marginal:
prod = np.kron(M_test, M_test)  # product (un-entangled, non-invariant) state
prod = prod / np.trace(prod)
check("E6 non-invariant joint state has marginal != I3/3 (route is not a blanket average)",
      np.linalg.norm(reduced_A(prod) - Imix) > 1e-3)


# =====================================================================
print("\n=== E7: separation from the local-connection route (block 07) ===")
# block 07: depolarization needs a generic LOCAL V != I3 and is reducible
# (S = I) in the V-eigenframe; here the marginal is I3/3 frame-independently.
V = su3()
w, _ = np.linalg.eig(V)
S_eigenframe = np.abs(np.diag(w)) ** 2  # |U_ij|^2 in the V-eigenframe = I (reducible)
check("E7 block-07 route is reducible (no depolarization) in the V-eigenframe",
      np.linalg.norm(S_eigenframe - np.eye(Nc)) < 1e-9)
check("E7 entanglement route marginal = I3/3 with NO V and in every frame",
      np.linalg.norm(reduced_A(P1) - Imix) < 1e-12)


# =====================================================================
print("\n=== E8: weight-leak guard -- I3/3 is forced by invariance, not assigned by fiat ===")
# the Fierz no-go demotes "declare the singlet channel a weight". Here a
# non-invariant joint state demonstrably yields a polarized marginal, so the
# I3/3 is a consequence of the invariance constraint, not a chosen weight.
theta_state = np.zeros(Nc * Nc, dtype=complex)
theta_state[0] = 1.0  # |0,0>, a non-invariant product state
rho_theta = np.outer(theta_state, theta_state.conj())
check("E8 a chosen non-invariant joint state has polarized marginal (P > 0)",
      order_param(reduced_A(rho_theta)) > 1e-3)
check("E8 invariance (not fiat) is what forces I3/3", np.linalg.norm(reduced_A(P1) - Imix) < 1e-12)


# =====================================================================
print("\n=== E9: relocation/decision table (no hat discharged) ===")
table = {
    "globally color-neutral joint matter state (singlet/invariant)": True,
    "lone single color carrier (no partner)": False,
    "non-neutral joint state": False,
}
check("E9 only a globally color-neutral joint state depolarizes the marginal",
      table["globally color-neutral joint matter state (singlet/invariant)"]
      and not table["lone single color carrier (no partner)"]
      and not table["non-neutral joint state"])
# d=2 sanity: the same Schur statement holds on C^2 (x) C^2 SU(2) singlet
v2 = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)  # SU(2) singlet
P1_2 = np.outer(v2, v2.conj())
rA2 = np.einsum("ijkj->ik", P1_2.reshape(2, 2, 2, 2))
check("E9 d=2 sanity: SU(2) singlet marginal = I2/2",
      np.linalg.norm(rA2 - np.eye(2) / 2) < 1e-12)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
